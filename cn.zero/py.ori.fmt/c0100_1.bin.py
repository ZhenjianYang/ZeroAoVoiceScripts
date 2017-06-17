from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0100_1.bin",                # FileName
        "c0100",                    # MapName
        "c0100",                    # Location
        0x0004,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0100_1",                # 0
    ))

    ScpFunction((
        "Function_0_1CC",          # 00, 0
        "Function_1_CAD",          # 01, 1
        "Function_2_1AEA",         # 02, 2
        "Function_3_25BF",         # 03, 3
        "Function_4_3220",         # 04, 4
        "Function_5_37DF",         # 05, 5
        "Function_6_3E80",         # 06, 6
        "Function_7_480A",         # 07, 7
        "Function_8_49E3",         # 08, 8
        "Function_9_5C48",         # 09, 9
        "Function_10_6DFC",        # 0A, 10
        "Function_11_76F2",        # 0B, 11
        "Function_12_7843",        # 0C, 12
        "Function_13_7967",        # 0D, 13
        "Function_14_7ABF",        # 0E, 14
        "Function_15_7C44",        # 0F, 15
        "Function_16_8246",        # 10, 16
        "Function_17_84EB",        # 11, 17
    ))


    def Function_0_1CC(): pass

    label("Function_0_1CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_22A")

    #C0001
    ChrTalk(
        0xFE,
        "今天的东西已经都买完了呢。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "按照预定计划完成目标，\x01",
            "心情真是不错啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA9")

    label("loc_22A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_272")

    #C0003
    ChrTalk(
        0xFE,
        "呼啊～……早上好啊～\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "希望今天也是不错的一天啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA9")

    label("loc_272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_333")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF")

    #C0005
    ChrTalk(
        0xFE,
        "港湾区那边人山人海啊。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "连警察都来了，\x01",
            "总觉得气氛好像有点恐怖，\x01",
            "是不是发生什么事了啊～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_32E")

    label("loc_2EF")


    #C0007
    ChrTalk(
        0xFE,
        (
            "港湾区那里好像出了什么事，\x01",
            "……希望不是什么恐怖的事件啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32E")

    Jump("loc_CA9")

    label("loc_333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_341")
    Jump("loc_CA9")

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3C0")

    #C0008
    ChrTalk(
        0xFE,
        (
            "不知怎么回事，预算会议\x01",
            "好像要延长了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "算了，反正好像每年\x01",
            "都会像这样推延……\x01",
            "大家都已经不会很在意了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA9")

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_481")

    #C0010
    ChrTalk(
        0xFE,
        (
            "纪念庆典最终日的时候，\x01",
            "我在米修拉姆看了烟花哦，\x01",
            "真漂亮呀～\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "不过，听说那天晚上发生了骚乱，\x01",
            "真是够危险的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "拿不出在米修拉姆住宿的钱，\x01",
            "反而算是走运呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4E2")

    label("loc_481")


    #C0013
    ChrTalk(
        0xFE,
        (
            "听说在纪念庆典最终日那晚，\x01",
            "米修拉姆发生了骚乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "我在那之前就回去了，或许算是幸运的呢～\x02",
    )

    CloseMessageWindow()

    label("loc_4E2")

    Jump("loc_CA9")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AF")

    #C0015
    ChrTalk(
        0xFE,
        (
            "麦克道尔市长\x01",
            "给人的感觉是个非常\x01",
            "严肃正派的老爷爷啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "虽然是政治家，但却很亲切，\x01",
            "而且好像还很有活力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "不过……他一直都拄着\x01",
            "根拐杖呢。\x01",
            "身体果然还是不太好吗～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5F0")

    label("loc_5AF")


    #C0018
    ChrTalk(
        0xFE,
        (
            "爸爸说麦克道尔市长今年\x01",
            "就要退休了……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "但那是真的吗～？\x02",
    )

    CloseMessageWindow()

    label("loc_5F0")

    Jump("loc_CA9")

    label("loc_5F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_675")

    #C0020
    ChrTalk(
        0xFE,
        (
            "今年的纪念庆典将会\x01",
            "是什么样子的呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "所有的店铺好像都在\x01",
            "为庆典做准备呢，\x01",
            "呵呵，真是期待呀～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6CA")

    label("loc_675")


    #C0022
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔最盛大的庆典活动——\x01",
            "创立纪念庆典已经临近了……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "呵呵，好期待啊～\x02",
    )

    CloseMessageWindow()

    label("loc_6CA")

    Jump("loc_CA9")

    label("loc_6CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_736")

    #C0024
    ChrTalk(
        0xFE,
        "买完东西后才发现天已经快黑了。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "我只要一进入商店，\x01",
            "就会不知不觉逛上很长时间呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA9")

    label("loc_736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7B8")

    #C0026
    ChrTalk(
        0xFE,
        "今天看到了好多警察啊……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "从早上到现在就遇到了五六个。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "似乎也没有什么事件\x01",
            "发生啊……\x01",
            "到底是怎么了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA9")

    label("loc_7B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87C")

    #C0029
    ChrTalk(
        0xFE,
        (
            "唉～最后也还是没能弄到\x01",
            "彩虹剧团的门票。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "我和朋友两个人都已经\x01",
            "很努力地排队了～\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "就在只剩下五个人就排到我们时，\x01",
            "票便全部卖光了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "呜呜，真是很受打击啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8F2")

    label("loc_87C")


    #C0033
    ChrTalk(
        0xFE,
        "啊啊啊！光是回忆一下就好不甘心～！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "而且那里的门票\x01",
            "未免太贵了吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "就算把零花钱全部都贴进去\x01",
            "好像也不够。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F2")

    Jump("loc_CA9")

    label("loc_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_963")

    #C0036
    ChrTalk(
        0xFE,
        (
            "据说阿尔摩利卡村产的蔬菜\x01",
            "对健康大有益助呢，\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "能让皮肤变得润滑透亮，\x01",
            "我也吃吃看好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA9")

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D4")

    #C0038
    ChrTalk(
        0xFE,
        (
            "今天准备去西街的亲戚\x01",
            "家里玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "不过市内没有\x01",
            "巴士可以坐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "真是不方便。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A0C")

    label("loc_9D4")


    #C0041
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市很广阔的，\x01",
            "我觉得市内也应该通车\x01",
            "才对。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0C")

    Jump("loc_CA9")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A8A")

    #C0042
    ChrTalk(
        0xFE,
        "刚才看到一辆绿色的大车开过去了。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "车身还印有克洛斯贝尔警备队的徽章呢，\x01",
            "车上的是不是警备队的人呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA9")

    label("loc_A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_B85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B20")

    #C0044
    ChrTalk(
        0xFE,
        (
            "本来想和朋友找个\x01",
            "出租公寓住的……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "但是都没有找到便宜的\x01",
            "房子啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "看来还是要和父母一起住，\x01",
            "暂时就别想独立了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B80")

    label("loc_B20")


    #C0047
    ChrTalk(
        0xFE,
        (
            "最近的经济很景气，\x01",
            "房租也都变得很高。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "呼，实在不行的话，\x01",
            "是不是要考虑廉价合租房了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B80")

    Jump("loc_CA9")

    label("loc_B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_CA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3F")

    #C0049
    ChrTalk(
        0xFE,
        (
            "我的爸爸在大公司里\x01",
            "上班……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "说是公司里最近设置了\x01",
            "叫做『导力网络』的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "不过爸爸弄不懂使用方法，\x01",
            "每天都很郁闷呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "真是的，爸爸好没用哦～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CA9")

    label("loc_C3F")


    #C0053
    ChrTalk(
        0xFE,
        (
            "『导力网络』这种东西，好像\x01",
            "是种非常便利的装置……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "但要是不知道使用方法，\x01",
            "那不还是和没有一样嘛～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA9")

    TalkEnd(0xFE)
    Return()

    # Function_0_1CC end

    def Function_1_CAD(): pass

    label("Function_1_CAD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D41")
    Jump("loc_D8B")

    label("loc_D41")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D61")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D8B")

    label("loc_D61")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D81")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D8B")

    label("loc_D81")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D8B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_E6C")

    #C0055
    ChrTalk(
        0xFE,
        (
            "听说延迟了很久的预算会议\x01",
            "总算是结束了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "面向市民的结果发表是在后天……\x01",
            "哎呀呀，最后结果会是如何呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "和去年相比，希望至少也能\x01",
            "通过一些浪费比较少的\x01",
            "预算案啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE2")

    label("loc_E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_EC4")

    #C0058
    ChrTalk(
        0xFE,
        (
            "预算会议好像在今天\x01",
            "就能结束了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "今年似乎比往年\x01",
            "拖得都要长呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE2")

    label("loc_EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_F8C")

    #C0060
    ChrTalk(
        0xFE,
        "你们听说了吗，黑手党之间开战的传闻……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "真是令人厌恶啊……\x01",
            "在以前，如果发生了这种事件，\x01",
            "往往都会死人的。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "本以为克洛斯贝尔多少也都\x01",
            "变得和平一些了，\x01",
            "但看来还是不能安心啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE2")

    label("loc_F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_F9A")
    Jump("loc_1AE2")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_10D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1064")

    #C0063
    ChrTalk(
        0xFE,
        (
            "通向玛因兹矿山镇的隧道内有条岔路，\x01",
            "岔路的尽头有个遗迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "传说每到满月之夜，那里就会响起\x01",
            "美妙的钟声哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "那处遗迹好像是在中世纪建造的建筑，\x01",
            "除此之外就一无所知了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_10D4")

    label("loc_1064")


    #C0066
    ChrTalk(
        0xFE,
        (
            "通向玛因兹矿山镇的隧道内有条岔路，\x01",
            "岔路的尽头有个遗迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "传说每到满月之夜，那里就会响起\x01",
            "美妙的钟声哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D4")

    Jump("loc_1AE2")

    label("loc_10D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A0")

    #C0068
    ChrTalk(
        0xFE,
        (
            "从明天开始，预算会议就要在\x01",
            "市政厅召开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "那是决定克洛斯贝尔的各种公共事业\x01",
            "预算的重要会议……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "但是每年都没法在\x01",
            "预定的结束日顺利得出结论。\x01",
            "今年又会如何呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_120F")

    label("loc_11A0")


    #C0071
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的预算会议\x01",
            "每年都迟迟得不出结论。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "大概是市长与议长的对立\x01",
            "延迟了决议吧。\x01",
            "今年又会如何呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120F")

    Jump("loc_1AE2")

    label("loc_1214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1364")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EE")

    #C0073
    ChrTalk(
        0xFE,
        (
            "位于克洛斯贝尔市南部的\x01",
            "『星见之塔』据说是个建造于\x01",
            "中世纪的建筑。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔似乎从那时开始就是个\x01",
            "充斥着交易与战乱的地区。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "传闻说，那是当时的掌权者\x01",
            "为了进行占星术\x01",
            "而下令建造的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_135F")

    label("loc_12EE")


    #C0076
    ChrTalk(
        0xFE,
        (
            "据说『星见之塔』是中世纪时\x01",
            "为了占星术而建造的。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "不过，这种说法并没有\x01",
            "什么实际依据，\x01",
            "连真伪都无法断定。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135F")

    Jump("loc_1AE2")

    label("loc_1364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_143A")

    #C0078
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ的总裁迪塔先生，\x01",
            "一直都是支撑着克洛斯贝尔的\x01",
            "经济界第一人。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "他并不只会赚钱，\x01",
            "对公共事业和慈善·支援机关\x01",
            "也积极捐款。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "虽说是人无完人……\x01",
            "但感觉迪塔先生好像\x01",
            "真的是个非常完美的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE2")

    label("loc_143A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1493")

    #C0081
    ChrTalk(
        0xFE,
        "那么，我差不多也该回去了。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "总是在这种地方待着，\x01",
            "说不定会感冒呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE2")

    label("loc_1493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_153C")

    #C0083
    ChrTalk(
        0xFE,
        (
            "彩虹剧团那传闻中的新剧，\x01",
            "听说第二主角会由新人出演。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "如果那新人真如传闻所说，是被\x01",
            "那个伊莉娅·普拉提耶亲自发掘的，\x01",
            "那应该是个具有相当实力的人吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE2")

    label("loc_153C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_160B")

    #C0085
    ChrTalk(
        0xFE,
        (
            "住在克洛斯贝尔的人\x01",
            "最喜欢热闹场面。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "特别是像庆典这样的活动，\x01",
            "无论老少，全都会因此而热情高涨。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "下个月举办的将是七十周年的创立纪念庆典。\x01",
            "今年到底会热闹到什么程度呢？我非常期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE2")

    label("loc_160B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_16A0")

    #C0088
    ChrTalk(
        0xFE,
        (
            "『彩虹剧团』可是克洛斯贝尔\x01",
            "引以为傲的明星集团。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "在国外的名流阶层中都很受欢迎，\x01",
            "听说偷偷潜入自治州来欣赏的人\x01",
            "也都不在少数呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE2")

    label("loc_16A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1791")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1735")

    #C0090
    ChrTalk(
        0xFE,
        (
            "前段时间，我在后巷那边\x01",
            "发现了一家\x01",
            "诡异的古董店。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "店里陈列着各种奇怪的商品，\x01",
            "店主老婆婆也给人一种\x01",
            "很奇怪的感觉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_178C")

    label("loc_1735")


    #C0092
    ChrTalk(
        0xFE,
        (
            "前段时间，我在后巷那边\x01",
            "发现了一家\x01",
            "诡异的古董店。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "唔……以前有那样\x01",
            "一家店吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178C")

    Jump("loc_1AE2")

    label("loc_1791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_18C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1869")

    #C0094
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的人\x01",
            "最喜欢各种小道传闻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "光是每天出门散散步，\x01",
            "就能听到不少消息呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "从事件的背后隐情\x01",
            "到外国的经济动向……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔，\x01",
            "能打听到所有情报，\x01",
            "这么说都不过分。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18C1")

    label("loc_1869")


    #C0098
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的人\x01",
            "最喜欢各种小道传闻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "呵，毕竟是一直都从事着贸易业的\x01",
            "人民啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C1")

    Jump("loc_1AE2")

    label("loc_18C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_19D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198C")

    #C0100
    ChrTalk(
        0xFE,
        (
            "鲁巴彻商会的那群家伙\x01",
            "在很早以前就在克洛斯贝尔扎根了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        "……也就是所谓的黑手党啊。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "可悲的是，警察根本就\x01",
            "没有办法将他们取缔。\x01",
            "你们还是不要和他们扯上关系为好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19D4")

    label("loc_198C")


    #C0103
    ChrTalk(
        0xFE,
        (
            "连警察都制裁不了\x01",
            "鲁巴彻商会，\x01",
            "……你们还是不要和他们扯上关系为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D4")

    Jump("loc_1AE2")

    label("loc_19D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1AE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A90")

    #C0104
    ChrTalk(
        0xFE,
        (
            "百货店的翻修，\x01",
            "还有全新的导力商店……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的街道格局\x01",
            "可真是日新月异啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "这虽然是好事，\x01",
            "但也让人看得眼花缭乱，\x01",
            "似乎一不小心就会迷路呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AE2")

    label("loc_1A90")


    #C0107
    ChrTalk(
        0xFE,
        (
            "街道的格局变化如此之大，\x01",
            "连我这种土生土长的克洛斯贝尔人\x01",
            "一不小心都会迷路呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_1_CAD end

    def Function_2_1AEA(): pass

    label("Function_2_1AEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1B5E")

    #C0108
    ChrTalk(
        0xFE,
        (
            "刚才有警察从空港那边\x01",
            "撤离呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "好像在说什么\x01",
            "爆炸物之类的东西……\x01",
            "嗯嗯，果然是很危险啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BB")

    label("loc_1B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BD1")

    #C0110
    ChrTalk(
        0xFE,
        (
            "警车慌慌张张地\x01",
            "往空港那边驶去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "是不是发生什么事了？\x01",
            "总有种不好的预感啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C0F")

    label("loc_1BD1")


    #C0112
    ChrTalk(
        0xFE,
        (
            "警察一慌张，\x01",
            "就肯定不会有什么好事。\x01",
            "总有不好的预感呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0F")

    Jump("loc_25BB")

    label("loc_1C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1CB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7C")

    #C0113
    ChrTalk(
        0xFE,
        "你们听说……港湾区的事件了吗？\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "……看来以后不能让小孩子\x01",
            "跑太远了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1CB2")

    label("loc_1C7C")


    #C0115
    ChrTalk(
        0xFE,
        (
            "米米，不要从爸爸的\x01",
            "身边离开哦！不然会\x01",
            "很危险的～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB2")

    Jump("loc_25BB")

    label("loc_1CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1CC5")
    Jump("loc_25BB")

    label("loc_1CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1D5F")

    #C0116
    ChrTalk(
        0xFE,
        (
            "在导力车已经普及的今天，\x01",
            "我认为应该积极对\x01",
            "道路进行整顿。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "特别是中央广场的人流量很大，\x01",
            "如果有投入预算，\x01",
            "真希望能把道路扩张一下啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BB")

    label("loc_1D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1E7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E34")
    TurnDirection(0xFE, 0x153, 0)

    #C0118
    ChrTalk(
        0xFE,
        (
            "啊呀，你是……\x01",
            "特别任务支援科的那个孩子吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "如果愿意的话，和我家米米\x01",
            "也做个好朋友吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x153,
        "#1109F嗯，好呀～！\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#0002F（这么快就能和对方混熟…\x01",
            "  也是天性使然吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E78")

    label("loc_1E34")

    TurnDirection(0xFE, 0x153, 0)

    #C0122
    ChrTalk(
        0xFE,
        (
            "你和我家米米差不多大吧？\x01",
            "愿意的话，你们就做个好朋友吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E78")

    Jump("loc_25BB")

    label("loc_1E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1F10")

    #C0123
    ChrTalk(
        0xFE,
        (
            "纪念庆典期间，市内的交通状况\x01",
            "实在是令人担忧啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "有不少游客都是开着导力车\x01",
            "来克洛斯贝尔的，但愿他们\x01",
            "不要做出什么出格行为……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BB")

    label("loc_1F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2009")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB4")

    #C0125
    ChrTalk(
        0xFE,
        (
            "好像有很多媒体行业的人\x01",
            "被招待去欣赏彩虹剧团的\x01",
            "新剧预演了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "他们都能抢先享受到\x01",
            "新剧的舞台吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "稍微有点羡慕呢，哈哈哈。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2004")

    label("loc_1FB4")


    #C0128
    ChrTalk(
        0xFE,
        (
            "再过不久就是彩虹的新剧预演了……\x01",
            "虽然明知道自己无缘欣赏，\x01",
            "但还是很兴奋啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2004")

    Jump("loc_25BB")

    label("loc_2009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2052")
    TurnDirection(0xFE, 0xB, 0)

    #C0129
    ChrTalk(
        0xFE,
        (
            "喂～米米，\x01",
            "天色已经变暗了，\x01",
            "差不多也该回去啦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BB")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_210B")

    #C0130
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的新剧目\x01",
            "好像是『金之太阳、银之月』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "能看到那个伊莉娅·普拉提耶，\x01",
            "一定很令人期待吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "不过，因为我没有买到票……\x01",
            "所有只能通过写真集来一饱眼福了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BB")

    label("loc_210B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2210")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A3")

    #C0133
    ChrTalk(
        0xFE,
        (
            "彩虹剧团公演的门票，\x01",
            "连我都没有买到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "百货店的门口排起了长龙，\x01",
            "听说其它售票处也都在转瞬之间\x01",
            "就把票都给卖光了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_220B")

    label("loc_21A3")


    #C0135
    ChrTalk(
        0xFE,
        (
            "本来还想让米米也见识一下\x01",
            "伊莉娅·普拉提耶的精彩表演呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "没办法了，等两个月之后\x01",
            "再碰碰运气吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220B")

    Jump("loc_25BB")

    label("loc_2210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_22DE")

    #C0137
    ChrTalk(
        0xFE,
        (
            "如果想成为导力车的驾驶员，\x01",
            "只要在政府部门办理正式的手续就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "但现在似乎有很多驾驶技术\x01",
            "不佳的人开车上路呢，\x01",
            "撞车事故也时有发生。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "我觉得还是应该对驾照的发放\x01",
            "设立更严格的标准。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BB")

    label("loc_22DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_23ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2377")

    #C0140
    ChrTalk(
        0xFE,
        (
            "你们几个……莫非是\x01",
            "被人用导力车送回来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "呀，没什么，我只是有点羡慕而已啦。\x01",
            "哈哈哈……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_23E8")

    label("loc_2377")


    #C0143
    ChrTalk(
        0xFE,
        (
            "刚才那辆导力车是\x01",
            "共和国的乌尔努公司制造的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "虽说只是价格最实惠的\x01",
            "一款车型……\x01",
            "但有车果然就是好啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23E8")

    Jump("loc_25BB")

    label("loc_23ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2507")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B1")

    #C0145
    ChrTalk(
        0xFE,
        (
            "随着导力车的普及，\x01",
            "违章停车渐渐也成了隐患。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "随便停在路边的话，大概会给后面的车辆\x01",
            "与行人造成很大麻烦吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "道路是我们大家的，\x01",
            "希望每个人都能严格遵守规则啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2502")

    label("loc_24B1")


    #C0148
    ChrTalk(
        0xFE,
        "违章停车也成问题了。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "道路是我们大家的，\x01",
            "希望每个人都能严格遵守规则啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2502")

    Jump("loc_25BB")

    label("loc_2507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2583")

    #C0150
    ChrTalk(
        0xFE,
        (
            "我是城市规划科的，\x01",
            "负责交通流量的调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "……话虽如此，但今天是和女儿一起\x01",
            "出来玩的，所以彻底停工呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BB")

    label("loc_2583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_25BB")

    #C0152
    ChrTalk(
        0xFE,
        (
            "这里是克洛斯贝尔地区\x01",
            "人流量最大的广场哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25BB")

    TalkEnd(0xFE)
    Return()

    # Function_2_1AEA end

    def Function_3_25BF(): pass

    label("Function_3_25BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2624")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2609")

    #C0153
    ChrTalk(
        0xFE,
        "夕阳好美啊。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "该和爸爸一起回家啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_261F")

    label("loc_2609")


    #C0155
    ChrTalk(
        0xFE,
        "小孩子该回去了。\x02",
    )

    CloseMessageWindow()

    label("loc_261F")

    Jump("loc_321C")

    label("loc_2624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_27B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2781")

    #C0156
    ChrTalk(
        0xFE,
        "早上好～罗伊德哥哥，还有大家！\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        "特别任务支援科今天也有工作吗？\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#0000F嗯，算是有一点呢。\x01",
            "……话说回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，终于把我们\x01",
            "给记住了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "哎～？\x01",
            "米米至今为止，可是\x01",
            "连一次都没有说错过吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#0100F嗯、嗯～\x01",
            "算了，\x01",
            "就当是这样好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x103,
        "#0202F玩的时候要注意车哦。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        "嗯！大家工作也要加油哦！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_27AC")

    label("loc_2781")


    #C0164
    ChrTalk(
        0xFE,
        (
            "特别任务支援科的各位，\x01",
            "工作要加油啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27AC")

    Jump("loc_321C")

    label("loc_27B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_281F")

    #C0165
    ChrTalk(
        0xFE,
        (
            "不知道为什么，爸爸今天\x01",
            "好严厉呀～\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "不过，他说那都是为了米米好，\x01",
            "所以米米会乖乖听话的～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_321C")

    label("loc_281F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_282D")
    Jump("loc_321C")

    label("loc_282D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2880")

    #C0167
    ChrTalk(
        0xFE,
        (
            "今天小琪雅没和你们\x01",
            "在一起吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "哎，本来还想叫她一起玩呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_321C")

    label("loc_2880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2A40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A01")
    TurnDirection(0xFE, 0x153, 0)

    #C0169
    ChrTalk(
        0xFE,
        "咦，不认识的孩子呢……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "好羡慕哦～罗伊德大哥哥他们\x01",
            "在陪你一起玩吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x153,
        "#1104F嘿嘿，羡慕吧～！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2938")

    #C0172
    ChrTalk(
        0x102,
        "#0106F其实不是在玩啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2989")

    label("loc_2938")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_296B")

    #C0173
    ChrTalk(
        0x103,
        "#0206F这并不是在玩呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2989")

    label("loc_296B")


    #C0174
    ChrTalk(
        0x104,
        "#0306F这哪里像是在玩啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2989")


    #C0175
    ChrTalk(
        0x101,
        (
            "#0006F嗯～不过，这一个星期确实……\x02\x03",

            "只要跟琪雅在一起，\x01",
            "就会不知不觉地玩起来了呢……\x01",
            "……必须要注意一点了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2A3B")

    label("loc_2A01")


    #C0176
    ChrTalk(
        0xFE,
        "喂，下次也和我一起玩吧～\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x153,
        "#1109F嘿嘿嘿，好呀～！\x02",
    )

    CloseMessageWindow()

    label("loc_2A3B")

    Jump("loc_321C")

    label("loc_2A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2AAA")

    #C0178
    ChrTalk(
        0xFE,
        (
            "那边的那个姐姐，\x01",
            "说她会在庆典期间开店呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "米米还没吃过爆米花哦，\x01",
            "所以很期待的～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_321C")

    label("loc_2AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2B21")

    #C0180
    ChrTalk(
        0xFE,
        (
            "爸爸还有市里的大家\x01",
            "好像都很在意下个月的庆典。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "到时肯定会有很多\x01",
            "有趣的活动吧！\x01",
            "米米也很期待～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_321C")

    label("loc_2B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2B4B")

    #C0182
    ChrTalk(
        0xFE,
        "哎～还想再多玩一会呢！\x02",
    )

    CloseMessageWindow()
    Jump("loc_321C")

    label("loc_2B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2BD4")

    #C0183
    ChrTalk(
        0xFE,
        (
            "爸爸好像没有抢到\x01",
            "彩虹剧团的票。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "哈，那也是没办法的事啊，\x01",
            "毕竟彩虹剧团的公演那么受欢迎。\x01",
            "米米倒是不在意有没有票～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_321C")

    label("loc_2BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2DFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9E")

    #C0185
    ChrTalk(
        0xFE,
        (
            "啊，是罗伊德哥哥还有大家。\x01",
            "你们好呀～！\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#0000F你好啊。\x01",
            "哈哈，最近终于能把我的\x01",
            "名字记住了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "记住了呀～\x01",
            "特务支援科的\x01",
            "罗伊德哥哥一行！\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        (
            "#0106F嗯、嗯～\x01",
            "看来还是没能把『特别任务支援科』\x01",
            "这个全名记住呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        (
            "#0200F……话说回来……\x01",
            "人名好像也只记住了\x01",
            "罗伊德前辈一个人的啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        (
            "#0303F哼哼哼……罗伊德，真有一手啊。\x01",
            "竟然把本大爷撇在一边，\x01",
            "让这位年幼的小姐只对你一个人留下印象……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        "#0011F你、你在说什么梦话呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2DF5")

    label("loc_2D9E")


    #C0192
    ChrTalk(
        0xFE,
        (
            "特务支援科的各位，\x01",
            "今天在做什么工作呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "米米会声援你们的，所以一定要加油哦～\x02",
    )

    CloseMessageWindow()

    label("loc_2DF5")

    Jump("loc_321C")

    label("loc_2DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2E3C")

    #C0194
    ChrTalk(
        0xFE,
        "今天天气也很好啊～\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "要小心路上的车子啊～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_321C")

    label("loc_2E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2F49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EEE")

    #C0196
    ChrTalk(
        0xFE,
        (
            "啊！特务……\x01",
            "………特务什么科的哥哥姐姐们！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "辛苦啦～！\x01",
            "要加油工作哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        "#0002F哈哈，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#0106F（还是没能把名字\x01",
            "  给记住啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F44")

    label("loc_2EEE")


    #C0200
    ChrTalk(
        0xFE,
        (
            "我爸爸他啊，一直都\x01",
            "梦想着买一辆导力车。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "总是拿着车子的介绍单，\x01",
            "研究个没完～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F44")

    Jump("loc_321C")

    label("loc_2F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_30C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3094")

    #C0202
    ChrTalk(
        0xFE,
        "啊，你们好啊！\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        "#0000F嗯，你好。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "哎～那个……\x01",
            "特务……特务……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#0200F……是特别任务支援科。\x01",
            "呵，这名字可能是有些拗口。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "是特务支援科对吧！\x01",
            "米米记住啦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "今天也要加油工作呀～\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        "#0106F感、感觉稍微有点不对……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x104,
        (
            "#0300F算了，毕竟才刚刚一个月。\x01",
            "慢慢总会记住的，这样就行了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_30C1")

    label("loc_3094")


    #C0210
    ChrTalk(
        0xFE,
        (
            "特务支援科的各位～\x01",
            "今天也要加油工作呀～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C1")

    Jump("loc_321C")

    label("loc_30C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3131")

    #C0211
    ChrTalk(
        0xFE,
        (
            "嘟嘟～嘟嘟～……\x01",
            "很多车子开过去了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "知道吗？\x01",
            "这里可是克洛斯贝尔\x01",
            "车子最多的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_321C")

    label("loc_3131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_321C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CE")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0213
    ChrTalk(
        0xFE,
        (
            "啊，你们好！\x01",
            "你们是游客吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "哎，不是吗？\x01",
            "真遗憾～……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "米米本来还想带你们\x01",
            "参观克洛斯贝尔呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_321C")

    label("loc_31CE")


    #C0216
    ChrTalk(
        0xFE,
        (
            "米米将来要\x01",
            "成为一名导游哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "到那时，米米\x01",
            "会带你们游遍克洛斯贝尔的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_321C")

    TalkEnd(0xFE)
    Return()

    # Function_3_25BF end

    def Function_4_3220(): pass

    label("Function_4_3220")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_32A0")

    #C0218
    ChrTalk(
        0xFE,
        (
            "……我说你啊……\x01",
            "你现在大吃大喝，刚才\x01",
            "辛苦跑步的意义不就全没了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "呼～早知如此的话，\x01",
            "就不称赞你了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_32A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3302")

    #C0220
    ChrTalk(
        0xFE,
        "啊……总觉得脸似乎变瘦了一些呢。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "嗯嗯，\x01",
            "你节食很努力嘛，\x01",
            "了不起～了不起～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_3302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3379")

    #C0222
    ChrTalk(
        0xFE,
        (
            "啊～在百货店买零食吃，\x01",
            "果然是最幸福的\x01",
            "时刻呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "（嚼嚼嚼）……\x01",
            "怎么了，你干嘛一脸怨恨的表情啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_3379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_33EF")

    #C0224
    ChrTalk(
        0xFE,
        (
            "……最近没人说你变胖了吗？\x01",
            "你啊，脸都快变成圆球了。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "就是因为对节食有所懈怠，\x01",
            "体重才会反弹的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_33EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3447")

    #C0226
    ChrTalk(
        0xFE,
        (
            "哎？\x01",
            "你在吃什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "明明说好要一起减肥的，\x01",
            "偷偷吃零食可不行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_3447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3493")

    #C0228
    ChrTalk(
        0xFE,
        "我们认识也有很长时间了。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "你就没有过什么浪漫艳遇吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_3493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_34D7")

    #C0230
    ChrTalk(
        0xFE,
        "说起来，纪念庆典也快到了。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        "你有什么安排吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_34D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_353E")

    #C0232
    ChrTalk(
        0xFE,
        (
            "啊，这么一说……\x01",
            "彩虹剧团的票好像已经\x01",
            "开始出售了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "完全忘记了。\x01",
            "太糟糕了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_353E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_35AC")

    #C0234
    ChrTalk(
        0xFE,
        (
            "不久前我看到ＩＢＣ总裁的\x01",
            "豪华轿车了～\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "总裁先生人也很帅气潇洒，\x01",
            "完全是我喜欢的类型哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_35AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_35EB")

    #C0236
    ChrTalk(
        0xFE,
        "今天要去哪里？\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "也没心情去逛\x01",
            "百货店啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_35EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3641")

    #C0238
    ChrTalk(
        0xFE,
        "亚里欧斯大人好像又出差了呢。\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "暂时没法见到\x01",
            "他了呢……\x01",
            "真遗憾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_3641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3699")

    #C0240
    ChrTalk(
        0xFE,
        (
            "真想找个有车的\x01",
            "男朋友啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "那样就可以让他开车\x01",
            "带我去任何地方了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_3699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3705")

    #C0242
    ChrTalk(
        0xFE,
        (
            "好像发生魔兽闯入\x01",
            "城镇和村子的事件了。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "真是的～好可怕啊。\x01",
            "警备队的人到底在干什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_3705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3780")

    #C0244
    ChrTalk(
        0xFE,
        (
            "不过，话说回来，\x01",
            "你们看到克洛斯贝尔时代周刊上\x01",
            "刊登的那张照片了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "亚里欧斯大人果然\x01",
            "很英俊帅气呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_3780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_37DB")

    #C0246
    ChrTalk(
        0xFE,
        (
            "亚里欧斯大人好像又\x01",
            "立下了新功劳呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "我也好想被亚里欧斯大人\x01",
            "救出来呀～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37DB")

    TalkEnd(0xFE)
    Return()

    # Function_4_3220 end

    def Function_5_37DF(): pass

    label("Function_5_37DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3865")

    #C0248
    ChrTalk(
        0xFE,
        (
            "但、但是啊！\x01",
            "因为开始变瘦了嘛，\x01",
            "所以觉得就吃一点点，也可以吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "啊啊～不要丢下我嘛～！\x01",
            "我会继续加油的～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_38FB")
    OP_4B(0xC, 0xFF)

    #C0250
    ChrTalk(
        0xFE,
        (
            "是、是吗～\x01",
            "虽然自己还没发现……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "但跑步的成果已经有所显现了呢！\x01",
            "好～……！\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xC,
        "（嗯，只要她能拿出干劲，撒谎也值了。）\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    Jump("loc_3E7C")

    label("loc_38FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3990")

    #C0253
    ChrTalk(
        0xFE,
        (
            "啊啊～太狡猾啦！\x01",
            "我明明还在节食减肥呢，\x01",
            "却故意让我看到食物……！\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "……我说，稍微给我点食物嘛～！\x01",
            "就当是我努力晨跑的奖励啦！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_399E")
    Jump("loc_3E7C")

    label("loc_399E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3A02")

    #C0255
    ChrTalk(
        0xFE,
        (
            "好过分～！\x01",
            "就像事不关己一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "我从今天开始就要节食了，\x01",
            "帮忙监督我啦～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3A69")

    #C0257
    ChrTalk(
        0xFE,
        (
            "（嚼嚼）……所以说呢，\x01",
            "一日吃两餐是不可能的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        "没关系，从明天开始努力就好啦～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3AC0")

    #C0259
    ChrTalk(
        0xFE,
        (
            "如果有什么浪漫艳遇的话，\x01",
            "也就不会总是和你一起玩了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        "……唉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3AF7")

    #C0261
    ChrTalk(
        0xFE,
        (
            "嗯～和平常一样，\x01",
            "只是不停地逛街啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3B83")

    #C0262
    ChrTalk(
        0xFE,
        "算了，反正都已经卖光了。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的门票，\x01",
            "永远都是刚发售就被一抢而空。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "至少没有浪费时间去排队，\x01",
            "也算是幸运了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3BE3")

    #C0265
    ChrTalk(
        0xFE,
        (
            "亚里欧斯先生也罢，\x01",
            "迪塔先生也罢……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "你的眼里还真是\x01",
            "就只有帅气的大叔啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3C58")

    #C0267
    ChrTalk(
        0xFE,
        "找个地方喝杯茶去如何～？\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "……虽然想这么说，但我没钱啊……\x01",
            "果然还是只能在百货店里随便逛逛吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3CCE")

    #C0269
    ChrTalk(
        0xFE,
        (
            "亚里欧斯先生很受人欢迎，\x01",
            "但却总是在出差呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "警察这么靠不住，\x01",
            "真希望他能一直留在克洛斯贝尔啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3D39")

    #C0271
    ChrTalk(
        0xFE,
        (
            "不过，导力车是\x01",
            "非常贵的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "如果能钓到一个\x01",
            "有钱男人就好了，\x01",
            "但现实可是很严酷的啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3DB6")

    #C0273
    ChrTalk(
        0xFE,
        (
            "算了，反正在克洛斯贝尔市\x01",
            "大概也不会出现那种事件，\x01",
            "应该可以安心吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "不管怎么样，\x01",
            "也都有游击士协会呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3E18")

    #C0275
    ChrTalk(
        0xFE,
        "我看到了～\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "你们就是当时傻站在后面的\x01",
            "那些警察吧，\x01",
            "看起来就像是跟班一样呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3E7C")

    #C0277
    ChrTalk(
        0xFE,
        (
            "警察似乎也帮了\x01",
            "亚里欧斯大人的\x01",
            "一点忙吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "呵呵，最后功劳不还是\x01",
            "全都被人家占了嘛～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E7C")

    TalkEnd(0xFE)
    Return()

    # Function_5_37DF end

    def Function_6_3E80(): pass

    label("Function_6_3E80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3FA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F29")

    #C0279
    ChrTalk(
        0xFE,
        (
            "一想到孩子们接过气球那一\x01",
            "瞬间的笑脸……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "嗯，就觉得自己的工作\x01",
            "十分有意义啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "希望将来能受到孩子们的仰慕，\x01",
            "被喊为气球叔叔啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F9C")

    label("loc_3F29")


    #C0282
    ChrTalk(
        0xFE,
        (
            "总是可以看见孩子们的笑脸，\x01",
            "我觉得这份工作\x01",
            "真的很有价值。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "希望将来能受到孩子们的仰慕，\x01",
            "被喊为气球叔叔啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F9C")

    Jump("loc_4806")

    label("loc_3FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_40A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4037")

    #C0284
    ChrTalk(
        0xFE,
        "气球，要不要气球啊～\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "请注意，\x01",
            "不要把气球拿到\x01",
            "拥挤的地方哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "它是橡胶制成的，\x01",
            "受到挤压的话，很容易就会破掉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_40A3")

    label("loc_4037")


    #C0287
    ChrTalk(
        0xFE,
        (
            "气球终究也只是橡胶制品，\x01",
            "受到挤压的话，很容易就会破掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "那刺耳的破裂声，\x01",
            "我到现在都无法习惯……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40A3")

    Jump("loc_4806")

    label("loc_40A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4124")

    #C0289
    ChrTalk(
        0xFE,
        (
            "只要把气球拿在手里，\x01",
            "心情马上就会平静下来。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "看啊，这可爱的形状。\x01",
            "那些小小的烦恼都变得可笑起来了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4806")

    label("loc_4124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_4132")
    Jump("loc_4806")

    label("loc_4132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_41BE")

    #C0291
    ChrTalk(
        0xFE,
        "气球，拿个气球吧？\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "喔，今天没带着\x01",
            "那个活泼开朗的小女孩啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "所谓小孩子，如果不抽时间陪陪她，\x01",
            "可是会闹别扭的哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4806")

    label("loc_41BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_42DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A9")

    #C0294
    ChrTalk(
        0xFE,
        (
            "啊，小姑娘，\x01",
            "来个气球怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        "哈哈哈，你很喜欢气球吧。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x153,
        "#1111F嗯～？……一般啦。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        "不、不会吧……？\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "怎么会这样呢，小孩子\x01",
            "不是应该都很喜欢气球才对吗～……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        "#0006F（这是什么偏见……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_42DA")

    label("loc_42A9")


    #C0300
    ChrTalk(
        0xFE,
        (
            "……小孩子的话，\x01",
            "应该都喜欢气球才对吧～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42DA")

    Jump("loc_4806")

    label("loc_42DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4346")

    #C0301
    ChrTalk(
        0xFE,
        (
            "给气球充入瓦斯这种事情，必须要在\x01",
            "别人看不见的时候做。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        "不然会打破大家的幻想吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4806")

    label("loc_4346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_443C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43E8")

    #C0303
    ChrTalk(
        0xFE,
        (
            "瓦斯比空气更轻，\x01",
            "所以气球才能优雅地飘浮在空中。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "……喂，在这附近可一定\x01",
            "要小心火源啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "瓦斯遇火的话，会把我\x01",
            "都给炸飞的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4437")

    label("loc_43E8")


    #C0306
    ChrTalk(
        0xFE,
        "一定要非常小心火源啊。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "我虽然喜欢气球，但也不想\x01",
            "像气球一样在天上飞。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4437")

    Jump("loc_4806")

    label("loc_443C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4482")

    #C0308
    ChrTalk(
        0xFE,
        "嗯，今天就到这里吧。\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        "这份工作也并不轻松呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4806")

    label("loc_4482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_450E")

    #C0310
    ChrTalk(
        0xFE,
        (
            "如今到处都在用导力器，\x01",
            "几乎都已经见不到瓦斯驱动的机器了。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "你不觉得给气球充气算是瓦斯为数不多的\x01",
            "有效使用方法之一吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4806")

    label("loc_450E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4563")

    #C0312
    ChrTalk(
        0xFE,
        "气球、气球哦～\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "不小心松手的话，气球会飞掉的，\x01",
            "一定要注意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4806")

    label("loc_4563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_45D5")

    #C0314
    ChrTalk(
        0xFE,
        (
            "哈，今天也要充满干劲地\x01",
            "分发气球呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "从上午开始，中央广场的\x01",
            "游客就已经很多了，非常热闹呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4806")

    label("loc_45D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4634")

    #C0316
    ChrTalk(
        0xFE,
        "小兄弟，你们要不要来个气球呢？\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "不是游客也无所谓，\x01",
            "反正我也是随便发的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4806")

    label("loc_4634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_46C1")

    #C0318
    ChrTalk(
        0xFE,
        (
            "旅游业已经被公认为\x01",
            "克洛斯贝尔的主要产业之一了，\x01",
            "市里也都下发了补助预算。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "派发气球也是让旅游业更加兴旺的\x01",
            "重要工作哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4806")

    label("loc_46C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_47BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4765")

    #C0320
    ChrTalk(
        0xFE,
        "要来个气球吗～？\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "……啊啊，并不是有什么\x01",
            "特别的庆典啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "我只是一直都在派发气球而已。\x01",
            "克洛斯贝尔的人\x01",
            "都喜欢外表华丽的东西。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_47B9")

    label("loc_4765")


    #C0323
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的人都喜欢\x01",
            "华丽的东西，热闹的气氛。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "好啦好啦，\x01",
            "别客气，拿去吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47B9")

    Jump("loc_4806")

    label("loc_47BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4806")

    #C0325
    ChrTalk(
        0xFE,
        "要来个气球吗～？\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        (
            "游客可以来我这里\x01",
            "免费领取气球啦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4806")

    TalkEnd(0xFE)
    Return()

    # Function_6_3E80 end

    def Function_7_480A(): pass

    label("Function_7_480A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4909")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B1")

    #C0327
    ChrTalk(
        0xFE,
        (
            "那么，店铺的位置也\x01",
            "已经确认完毕了……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "反正机会难得，\x01",
            "稍微观光一下再回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "毕竟庆典开始之后\x01",
            "可能就再也没有观光的闲暇了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4904")

    label("loc_48B1")


    #C0330
    ChrTalk(
        0xFE,
        "那么，要去哪里观光好呢。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "话虽如此，因为是一日游，\x01",
            "也不能去太远的地方……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4904")

    Jump("loc_49DF")

    label("loc_4909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_49DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_497D")

    #C0332
    ChrTalk(
        0xFE,
        (
            "下个月的纪念庆典，\x01",
            "我会开个卖爆米花的露天店哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        "呵呵，能占上个好位置真不错啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_49DF")

    label("loc_497D")


    #C0334
    ChrTalk(
        0xFE,
        (
            "下个月的纪念庆典，\x01",
            "我会开个爆米花的露天店哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "今天是来检查位置的，\x01",
            "下个月还请多关照呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49DF")

    TalkEnd(0xFE)
    Return()

    # Function_7_480A end

    def Function_8_49E3(): pass

    label("Function_8_49E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_49F4")
    Jump("loc_5C44")

    label("loc_49F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4ACD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7E")
    OP_93(0xFE, 0xC5, 0x0)

    #C0336
    ChrTalk(
        0xFE,
        (
            "哔哔～哔哔～！\x01",
            "导力车请缓慢行驶～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0337
    ChrTalk(
        0xFE,
        (
            "……感觉今天的车流量\x01",
            "似乎有些少啊……\x01",
            "大概是错觉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4AC8")

    label("loc_4A7E")


    #C0338
    ChrTalk(
        0xFE,
        (
            "我每天都要疏导交通，\x01",
            "感觉今天街上似乎稍微有些寂寥啊。\x01",
            "或许是错觉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AC8")

    Jump("loc_5C44")

    label("loc_4ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4ADB")
    Jump("loc_5C44")

    label("loc_4ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4AE9")
    Jump("loc_5C44")

    label("loc_4AE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4DB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D1C")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0339
    ChrTalk(
        0xFE,
        "啊……这不是罗伊德嘛！\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "那个，听说你们经历了\x01",
            "很危险的事情啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        (
            "#0008F抱歉，凯特前辈，\x01",
            "让你担心了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4BCE")

    #C0342
    ChrTalk(
        0x102,
        (
            "#0100F我们没事的。\x02\x03",

            "比起这个……\x01",
            "最近街上的状况怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C6E")

    label("loc_4BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4C1B")

    #C0343
    ChrTalk(
        0x103,
        (
            "#0200F我们没事的。\x02\x03",

            "比起这个……\x01",
            "最近街上的状况怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C6E")

    label("loc_4C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4C6E")

    #C0344
    ChrTalk(
        0x104,
        (
            "#0300F哈，我们什么事\x01",
            "都没有啦。\x02\x03",

            "比起这个……\x01",
            "最近街上的情况如何了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C6E")


    #C0345
    ChrTalk(
        0xFE,
        (
            "街上很安静啊，\x01",
            "几乎都没有受到纪念庆典\x01",
            "余韵的影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        "麻烦事减少，倒是很令人高兴啦。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#0003F是吗……\x01",
            "（自那之后，鲁巴彻的家伙们\x01",
            "  也暂时安分下来了吗……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 0)
    Jump("loc_4DB3")

    label("loc_4D1C")


    #C0348
    ChrTalk(
        0xFE,
        "最近这一周，街上都很安静啊。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "似乎完全都没有\x01",
            "受到纪念庆典的影响啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "比起那个，实在是很担心\x01",
            "你们支援科的情况啊。\x01",
            "请不要做太危险的事情哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DB3")

    Jump("loc_5C44")

    label("loc_4DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4F3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED0")

    #C0351
    ChrTalk(
        0xFE,
        (
            "呼……今天早上也\x01",
            "发现有人违章停车。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "真是的，你们昨天才刚刚\x01",
            "取缔过的～\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        "#0000F哈哈，是那样吗……\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x104,
        (
            "#0300F算了，违章停车这种事\x01",
            "一直是屡禁不止的。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        "不过，你们不觉得不甘心吗？\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "我很不甘心。\x01",
            "所以要对那些违章停车的\x01",
            "车主提出严重警告！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4F3A")

    label("loc_4ED0")


    #C0357
    ChrTalk(
        0xFE,
        (
            "违章停车就是犯罪行为，\x01",
            "坏习惯就必须要改正。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "小恶可是会发展为大恶的！\x01",
            "必须要对他们严重警告才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F3A")

    Jump("loc_5C44")

    label("loc_4F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_504F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5003")
    OP_93(0xFE, 0xC5, 0x0)

    #C0359
    ChrTalk(
        0xFE,
        (
            "哔哔～哔哔～！\x01",
            "导力车请缓慢行驶～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 0)

    #C0360
    ChrTalk(
        0xFE,
        (
            "警察的工作就是要\x01",
            "踏踏实实地不断努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        (
            "好，罗伊德，还有各位，\x01",
            "今天也一起加油吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x101,
        "#0000F哈哈，也是呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_504A")

    label("loc_5003")


    #C0363
    ChrTalk(
        0xFE,
        (
            "警察的工作就是要\x01",
            "踏踏实实地不断努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        "好，今天也一起加油吧！\x02",
    )

    CloseMessageWindow()

    label("loc_504A")

    Jump("loc_5C44")

    label("loc_504F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_56C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 0)), scpexpr(EXPR_END)), "loc_524A")

    #C0365
    ChrTalk(
        0xFE,
        (
            "啊，罗伊德，是你们啊。\x01",
            "还在调查案件吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        "#0003F嗯，稍微有些事情……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0367
    ChrTalk(
        0x101,
        (
            "#0000F对了，凯特前辈\x01",
            "一直都在市内巡逻吧。\x02\x03",

            "对『银』这个名字\x01",
            "有没有什么印象呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "……『银』？\x01",
            "从没听说过啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0369
    ChrTalk(
        0xFE,
        "啊，说起来！\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的\x01",
            "新剧目好像就叫\x01",
            "『金之太阳、银之月』啊！\x02",
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

    #C0371
    ChrTalk(
        0x101,
        "#0006F唔～这样啊……\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        (
            "唔，嗯。\x01",
            "没能帮上忙，真抱歉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55C9")

    label("loc_524A")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0373
    ChrTalk(
        0xFE,
        "啊，是罗伊德，还有兰迪！\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "之前真是多谢你们\x01",
            "帮忙进行交通管理了～……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        "……啊，不对。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "罗伊德搜查官以及\x01",
            "特别任务支援科的各位，\x01",
            "衷心感谢你们的协作！\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x101,
        (
            "#0002F哈哈哈……\x01",
            "凯特前辈，不用那么\x01",
            "在意形式吧。\x02\x03",

            "我们也经常受你\x01",
            "关照的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        "呵呵，说来也是呢。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "那，以后如果有什么事情，\x01",
            "还能请你们助我一臂之力吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x104,
        (
            "#0304F噢～那当然，\x01",
            "请不要客气，随时联系我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        "谢谢，帮大忙了。\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "……不过，罗伊德，你们\x01",
            "还在进行调查吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x101,
        "#0003F嗯，还有些事情……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0384
    ChrTalk(
        0x101,
        (
            "#0000F对了，凯特前辈\x01",
            "一直都在市内巡逻吧。\x02\x03",

            "对『银』这个名字，\x01",
            "有没有什么印象呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "……『银』？\x01",
            "从没听说过啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0386
    ChrTalk(
        0xFE,
        "啊，说起来！\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的\x01",
            "新剧目好像就叫\x01",
            "『金之太阳、银之月』啊！\x02",
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

    #C0388
    ChrTalk(
        0x101,
        "#0006F唔～这样啊……\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "唔，嗯。\x01",
            "没能帮上忙，真抱歉啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55C9")

    SetScenarioFlags(0x92, 1)
    Jump("loc_56BC")

    label("loc_55D1")


    #C0390
    ChrTalk(
        0xFE,
        (
            "『银』……\x01",
            "没有什么特别的印象呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "嗯～抱歉啊，\x01",
            "好像没能帮上忙呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5670")

    #C0392
    ChrTalk(
        0x101,
        (
            "#0000F哪里，请不用在意。\x01",
            "我们正准备去拜访一位\x01",
            "相识的律师呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56BC")

    label("loc_5670")


    #C0393
    ChrTalk(
        0x101,
        (
            "#0000F哪里，是我们麻烦你了。\x01",
            "相关线索我们已经基本掌握了，\x01",
            "请不用在意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56BC")

    Jump("loc_5C44")

    label("loc_56C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5A2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59C8")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5794")

    #C0394
    ChrTalk(
        0xFE,
        (
            "啊，罗伊德，还有兰迪！\x01",
            "之前真是多谢你们\x01",
            "帮忙进行交通管理了～……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        "……啊，不对。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "罗伊德搜查官以及\x01",
            "特别任务支援科的各位，\x01",
            "衷心感谢你们的协作！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58A6")

    label("loc_5794")


    #C0397
    ChrTalk(
        0xFE,
        (
            "啊，罗伊德，是你们啊！\x01",
            "工作辛苦了～\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x101,
        (
            "#0000F啊，凯特前辈。\x01",
            "你辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x104,
        "#0300F嗨～今天早上承蒙指导了。\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "对了对了，你们两位今天早上\x01",
            "还帮忙进行交通管理了啊。\x01",
            "真是多谢啦～……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        "……啊，不对。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "罗伊德搜查官以及\x01",
            "特别任务支援科的各位，\x01",
            "衷心感谢你们的协作！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58A6")


    #C0403
    ChrTalk(
        0x101,
        (
            "#0002F哈哈哈……\x01",
            "凯特前辈，不用那么\x01",
            "在意形式吧。\x02\x03",

            "我们不是也经常\x01",
            "受你关照的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        "呵呵，说来也是呢。\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "那，以后如果有什么事情，\x01",
            "还能请你们助我一臂之力吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x104,
        (
            "#0304F噢～那当然，\x01",
            "请不要客气，随时联系我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        "谢谢，帮大忙了。\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "那么，任务辛苦啦！\x01",
            "你们也要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 0)
    Jump("loc_5A29")

    label("loc_59C8")


    #C0409
    ChrTalk(
        0xFE,
        (
            "或许是因为纪念庆典的临近，\x01",
            "各种小事件也在不断增多。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        "市内的巡逻工作还是不能掉以轻心啊。\x02",
    )

    CloseMessageWindow()

    label("loc_5A29")

    Jump("loc_5C44")

    label("loc_5A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5C44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C03")
    OP_93(0xFE, 0xC5, 0x0)

    #C0411
    ChrTalk(
        0xFE,
        "哔哔～哔哔～！\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "导力车请缓慢行驶。\x01",
            "为了市民们的安全，\x01",
            "请各位配合～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_5B01")

    #C0413
    ChrTalk(
        0xFE,
        (
            "啊，是罗伊德和各位，\x01",
            "准备去执行任务吗？\x01",
            "小心导力车呀！\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x101,
        "#0000F哈哈，谢谢了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BFB")

    label("loc_5B01")


    #C0415
    ChrTalk(
        0xFE,
        (
            "啊……罗伊德？\x01",
            "好久不见了啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x101,
        (
            "#0000F凯特前辈……\x01",
            "真是好久不见了，\x01",
            "在警察学校时承蒙你多加关照。\x02\x03",

            "……今天是在工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "嗯，我经常在这里进行\x01",
            "交通管理。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        (
            "罗伊德，你们也要去执行任务了吗？\x01",
            "要小心导力车呀！\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x101,
        "#0000F哈哈，谢谢了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 7)

    label("loc_5BFB")

    SetScenarioFlags(0x1, 1)
    Jump("loc_5C44")

    label("loc_5C03")

    OP_93(0xFE, 0xC5, 0x0)

    #C0420
    ChrTalk(
        0xFE,
        (
            "导力车请缓慢行驶。\x01",
            "为了市民们的安全，\x01",
            "请各位配合～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C44")

    TalkEnd(0xFE)
    Return()

    # Function_8_49E3 end

    def Function_9_5C48(): pass

    label("Function_9_5C48")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x1, 4)
    Call(1, 11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC8")

    #C0421
    ChrTalk(
        0x101,
        (
            "#0004F（说起来……\x01",
            "  有些食物似乎可以用来喂猫呢。）\x02\x03",

            "#0000F（喂给柯贝的话\x01",
            "  应该也不错啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x52, 0)

    label("loc_5CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DF5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DF0")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "对话")
    MenuCmd(1, 1, "喂食")
    MenuCmd(1, 1, "放弃")
    ClearScenarioFlags(0x1, 4)
    Call(1, 11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D85")
    MenuCmd(3, 1, 0x1)

    label("loc_5D85")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DB7")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5DB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DBB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5DF2")
    MenuCmd(1, 1, "雪花蟹")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5DF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_5E19")
    MenuCmd(1, 1, "阿尔摩利卡鲫鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5E19")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5E38")
    MenuCmd(1, 1, "橙河鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5E38")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5E57")
    MenuCmd(1, 1, "岩穴鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5E57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5E74")
    MenuCmd(1, 1, "鲤鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5E74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_5E93")
    MenuCmd(1, 1, "冷水鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5E93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5EB6")
    MenuCmd(1, 1, "蓝带神仙鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5ED5")
    MenuCmd(1, 1, "银伞鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5ED5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5EF4")
    MenuCmd(1, 1, "虹鳟鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EF4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5F11")
    MenuCmd(1, 1, "黑鲑")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5F2E")
    MenuCmd(1, 1, "鲑鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5F4B")
    MenuCmd(1, 1, "鳗鲡")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F4B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_5F6A")
    MenuCmd(1, 1, "珍珠草")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F6A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5F8B")
    MenuCmd(1, 1, "大口鲈鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5FAC")
    MenuCmd(1, 1, "云斑蛇头")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5FAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_5FCD")
    MenuCmd(1, 1, "暗纹蛇鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5FCD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_5FEA")
    MenuCmd(1, 1, "巨鲶")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5FEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6009")
    MenuCmd(1, 1, "巨血蟹")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6009")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_6026")
    MenuCmd(1, 1, "电鳗")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6026")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_6047")
    MenuCmd(1, 1, "魔鬼巨鲶")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6047")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_6066")
    MenuCmd(1, 1, "弧光蟹")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6066")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6083")
    MenuCmd(1, 1, "金鲑")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6083")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_60A0")
    MenuCmd(1, 1, "锦鲤")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_60A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_60C1")
    MenuCmd(1, 1, "霸王蛇鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_60C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_60DE")
    MenuCmd(1, 1, "猫食")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_60DE")

    MenuCmd(1, 1, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6126")
    Jump("loc_6DAC")

    label("loc_6126")

    EventBegin(0x1)
    Fade(500)
    SetChrPos(0x13, -21980, 1300, -19300, 270)
    SetChrPos(0x0, -23900, 1300, -19070, 89)
    SetChrPos(0x1, -23540, 1300, -20210, 89)
    SetChrPos(0x2, -25020, 1300, -19860, 89)
    SetChrPos(0x3, -25130, 1300, -18930, 89)
    SetChrPos(0x4, -26200, 1300, -19870, 89)
    SetChrPos(0x5, -26790, 1300, -19180, 89)
    OP_68(-23130, 3900, -19610, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    #C0422
    ChrTalk(
        0xFE,
        "喵喵……⊥\x02",
    )

    CloseMessageWindow()

    def lambda_61E8():

        label("loc_61E8")

        TurnDirection(0x0, 0x13, 0)
        Yield()
        Jump("loc_61E8")

    QueueWorkItem2(0x0, 1, lambda_61E8)

    def lambda_61FA():

        label("loc_61FA")

        TurnDirection(0x1, 0x13, 0)
        Yield()
        Jump("loc_61FA")

    QueueWorkItem2(0x1, 1, lambda_61FA)

    def lambda_620C():

        label("loc_620C")

        TurnDirection(0x2, 0x13, 0)
        Yield()
        Jump("loc_620C")

    QueueWorkItem2(0x2, 1, lambda_620C)

    def lambda_621E():

        label("loc_621E")

        TurnDirection(0x3, 0x13, 0)
        Yield()
        Jump("loc_621E")

    QueueWorkItem2(0x3, 1, lambda_621E)

    def lambda_6230():

        label("loc_6230")

        TurnDirection(0x4, 0x13, 0)
        Yield()
        Jump("loc_6230")

    QueueWorkItem2(0x4, 1, lambda_6230)

    def lambda_6242():

        label("loc_6242")

        TurnDirection(0x5, 0x13, 0)
        Yield()
        Jump("loc_6242")

    QueueWorkItem2(0x5, 1, lambda_6242)
    SetChrFlags(0x13, 0x8000)
    OP_93(0x13, 0x0, 0x1F4)
    Sleep(50)
    ClearChrFlags(0x13, 0x1)
    Sound(814, 0, 80, 0)

    def lambda_626E():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x708, 0x1F40)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_626E)
    WaitChrThread(0x13, 1)
    Sound(814, 0, 80, 0)

    def lambda_6295():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1130, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6295)
    WaitChrThread(0x13, 1)
    Sound(854, 0, 80, 0)

    def lambda_62BC():
        OP_9D(0xFE, 0xFFFFA75E, 0x514, 0xFFFFDFBC, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_62BC)
    WaitChrThread(0x13, 1)
    Sleep(2000)
    OP_93(0x13, 0xB4, 0x1F4)
    Sound(814, 0, 80, 0)

    def lambda_62ED():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1194, 0xFA0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_62ED)
    WaitChrThread(0x13, 1)
    Sound(814, 0, 80, 0)

    def lambda_6314():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6314)
    WaitChrThread(0x13, 1)
    Sound(854, 0, 80, 0)

    def lambda_633B():
        OP_9D(0xFE, 0xFFFFAA24, 0x514, 0xFFFFB49C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_633B)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x13, 0x1)
    OP_93(0x13, 0x10E, 0x1F4)
    ClearChrFlags(0x13, 0x8000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x4, 0x1)
    EndChrThread(0x5, 0x1)

    #C0423
    ChrTalk(
        0xFE,
        "喵～……\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6405")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63FB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('斗鱼', 1)

    #A0424
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('防御１', 1)

    label("loc_63FB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6405")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_644D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6443")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('雪花蟹', 1)

    #A0425
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔防２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('魔防２', 1)

    label("loc_6443")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_644D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6495")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_648B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('蓝带神仙鱼', 1)

    #A0426
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('ＥＰ３', 1)

    label("loc_648B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6495")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_64DD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64D3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('银伞鱼', 1)

    #A0427
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('攻击２', 1)

    label("loc_64D3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_64DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6525")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_651B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('阿尔摩利卡鲫鱼', 1)

    #A0428
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '琥耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('琥耀珠', 1)

    label("loc_651B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6525")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_656D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6563")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('乌龟', 1)

    #A0429
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '水耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('水耀珠', 1)

    label("loc_6563")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_656D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_65B5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65AB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('橙河鱼', 1)

    #A0430
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '行动力３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('行动力３', 1)

    label("loc_65AB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_65B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_65FD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65F3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('岩穴鱼', 1)

    #A0431
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '移动２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('移动２', 1)

    label("loc_65F3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_65FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6645")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_663B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('虹鳟鱼', 1)

    #A0432
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '冻结之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('冻结之刃', 1)

    label("loc_663B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6645")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_668D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6683")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('食人鱼', 1)

    #A0433
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('回避３', 1)

    label("loc_6683")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_668D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_66D5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66CB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鲤鱼', 1)

    #A0434
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('省ＥＰ１', 1)

    label("loc_66CB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_66D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_671D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6713")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('大口鲈鱼', 1)

    #A0435
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '光耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('光耀珠', 1)

    label("loc_6713")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_671D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_6765")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_675B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('黑鲑', 1)

    #A0436
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '精神３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('精神３', 1)

    label("loc_675B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6765")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_67AD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67A3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('角斗鱼', 1)

    #A0437
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('命中１', 1)

    label("loc_67A3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_67AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_67F5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67EB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('冷水鱼', 1)

    #A0438
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '黑耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('黑耀珠', 1)

    label("loc_67EB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_67F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_683D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6833")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('小鲵', 1)

    #A0439
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '妨害２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('妨害２', 1)

    label("loc_6833")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_683D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6885")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_687B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鲑鱼', 1)

    #A0440
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '绝耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('绝耀珠', 1)

    label("loc_687B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6885")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_68CD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68C3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('金龙鱼', 1)

    #A0441
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '翠耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('翠耀珠', 1)

    label("loc_68C3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_68CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_6915")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_690B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鳗鲡', 1)

    #A0442
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '冥王铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('冥王铃', 1)

    label("loc_690B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6915")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_695D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6953")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('钢壳龟', 1)

    #A0443
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('回避２', 1)

    label("loc_6953")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_695D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_69A5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_699B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨血蟹', 1)

    #A0444
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('防御３', 1)

    label("loc_699B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_69A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_69ED")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69E3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('珍珠龙鱼', 1)

    #A0445
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '封技之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('封技之刃', 1)

    label("loc_69E3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_69ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_6A35")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A2B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨鲶', 1)

    #A0446
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '金耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('金耀珠', 1)

    label("loc_6A2B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_6A7D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A73")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('金鲑', 1)

    #A0447
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '破盾之牙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('破盾之牙', 1)

    label("loc_6A73")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_6AC9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6ABF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('猫食', 1)

    #A0448
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽鱼肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×３收下了。\x02",
        )
    )

    AddItemNumber('魔兽鱼肉', 3)

    label("loc_6ABF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6AC9")

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AF0")
    SetScenarioFlags(0x4B, 3)

    label("loc_6AF0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B01")
    SetScenarioFlags(0x52, 1)

    label("loc_6B01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B12")
    SetScenarioFlags(0x52, 2)

    label("loc_6B12")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B23")
    SetScenarioFlags(0x52, 3)

    label("loc_6B23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B34")
    SetScenarioFlags(0x52, 4)

    label("loc_6B34")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B45")
    SetScenarioFlags(0x52, 5)

    label("loc_6B45")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B56")
    SetScenarioFlags(0x52, 6)

    label("loc_6B56")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 1)), scpexpr(EXPR_END)), "loc_6B73")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_END)), "loc_6B86")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_END)), "loc_6B99")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 4)), scpexpr(EXPR_END)), "loc_6BAC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 5)), scpexpr(EXPR_END)), "loc_6BBF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 6)), scpexpr(EXPR_END)), "loc_6BD2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C3B")

    #C0449
    ChrTalk(
        0xFE,
        "喵喵喵……¤\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0450
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '辰星铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('辰星铃', 1)
    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_6C3B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6C7B")

    #C0451
    ChrTalk(
        0x102,
        "#0105F啊……要把这个给我们吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D25")

    label("loc_6C7B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CB5")

    #C0452
    ChrTalk(
        0x103,
        "#0205F要把这个给我们吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D25")

    label("loc_6CB5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6D25")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D01")

    #C0453
    ChrTalk(
        0x104,
        "#0305F要把这东西给我们吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D25")

    label("loc_6D01")


    #C0454
    ChrTalk(
        0x101,
        "#0005F这个是要给我们的吗……？\x02",
    )

    CloseMessageWindow()

    label("loc_6D25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D66")

    #C0455
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，多谢啦～\x01",
            "我们会好好使用的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DA6")

    label("loc_6D66")


    #C0456
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，多谢啦～\x01",
            "……不过，究竟是从什么地方\x01",
            "拿来的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DA6")

    TalkEnd(0xFE)
    EventEnd(0x4)
    Return()

    label("loc_6DAC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6DEB")

    label("loc_6DBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DCF")
    Jump("loc_6DEB")

    label("loc_6DCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DEB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 10)

    label("loc_6DEB")

    Jump("loc_5D3D")

    label("loc_6DF0")

    Jump("loc_6DF8")

    label("loc_6DF5")

    Call(1, 10)

    label("loc_6DF8")

    TalkEnd(0x13)
    Return()

    # Function_9_5C48 end

    def Function_10_6DFC(): pass

    label("Function_10_6DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7127")

    #C0457
    ChrTalk(
        0x102,
        (
            "#0105F啊，这种地方竟然有小猫……\x02\x03",

            "#0109F呵呵，好可爱！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_END)), "loc_6EE4")

    #C0458
    ChrTalk(
        0x101,
        (
            "#0000F嗯，似乎在支援科搬进这里之前，\x01",
            "它就已经住在这里了。\x02\x03",

            "#0004F我记得克洛斯贝尔时代周刊社\x01",
            "原来就在这栋楼里……\x01",
            "说不定那个时候它就在了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F6B")

    label("loc_6EE4")


    #C0459
    ChrTalk(
        0x101,
        (
            "#0000F嗯～在支援科入驻之前\x01",
            "就已经定居在此的猫吗？\x02\x03",

            "#0004F我记得克洛斯贝尔时代周刊社\x01",
            "原来就在这栋楼里……\x01",
            "说不定那个时候它就在了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F6B")


    #C0460
    ChrTalk(
        0x104,
        (
            "#0309F……来来！\x01",
            "你叫什么名字呀～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x104, 500)
    Sound(823, 0, 100, 0)
    Sleep(500)

    #C0461
    ChrTalk(
        0x103,
        (
            "#0200F…………………………\x02\x03",

            "这孩子的名字是柯贝。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FFA")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6FFA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_701A")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_701A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_703A")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_703A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_705A")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_705A")

    Sleep(1000)

    #C0462
    ChrTalk(
        0x102,
        (
            "#0102F是缇欧起的吗？\x01",
            "好可爱的名字啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x103,
        (
            "#0203F不，这并不是\x01",
            "我起的名字……\x02\x03",

            "#0202F……总之，我想\x01",
            "称呼这孩子为柯贝就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x104,
        (
            "#0304F嗯，那就叫这个吧。\x02\x03",

            "#0300F以后时不时带点\x01",
            "吃的来喂它吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 3)
    Jump("loc_7667")

    label("loc_7127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7143")

    #C0465
    ChrTalk(
        0x13,
        "喵……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7667")

    label("loc_7143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7231")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_721C")

    #C0466
    ChrTalk(
        0x13,
        "喵～～嗝。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7214")

    #C0467
    ChrTalk(
        0x10A,
        (
            "#0605F（嗯……这只猫\x01",
            "  好像是克洛斯贝尔通讯社\x01",
            "  以前饲养的，不过……）\x02\x03",

            "#0603F（现在已经交托给特别任务支援科了吗？\x01",
            "  必须要补记在\x01",
            "  一科的资料里啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7214")

    SetScenarioFlags(0x0, 5)
    Jump("loc_722C")

    label("loc_721C")


    #C0468
    ChrTalk(
        0x13,
        "喵～～嗝。\x02",
    )

    CloseMessageWindow()

    label("loc_722C")

    Jump("loc_7667")

    label("loc_7231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_724D")

    #C0469
    ChrTalk(
        0x13,
        "喵啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7667")

    label("loc_724D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_731F")

    #C0470
    ChrTalk(
        0x13,
        "咕咕，喵～\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_72B4")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_72B4")


    #C0471
    ChrTalk(
        0x109,
        (
            "#0502F（嗯～好可爱……）\x02\x03",

            "#0506F（楼顶上竟然养着猫……\x01",
            "  我是不是也该在国境门那里养一只呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_732F")

    label("loc_731F")


    #C0472
    ChrTalk(
        0x13,
        "咕咕，喵～\x02",
    )

    CloseMessageWindow()

    label("loc_732F")

    Jump("loc_7667")

    label("loc_7334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7524")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74DF")

    #C0473
    ChrTalk(
        0x153,
        (
            "#1105F啊！是小猫～\x02\x03",

            "#1109F小小的好可爱哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x101,
        (
            "#0000F说起来，这好像是第一次\x01",
            "带琪雅来楼顶啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_7415")

    #C0475
    ChrTalk(
        0x102,
        (
            "#0104F是啊，在这里会被街上的人看到。\x02\x03",

            "#0100F考虑到小琪雅的安全，\x01",
            "这也是没办法的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74D4")

    label("loc_7415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_747A")

    #C0476
    ChrTalk(
        0x103,
        (
            "#0204F是啊，在这里会被别人看得清清楚楚。\x02\x03",

            "#0202F考虑到琪雅的安全，\x01",
            "这也没办法呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74D4")

    label("loc_747A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_74D4")

    #C0477
    ChrTalk(
        0x104,
        (
            "#0302F哈，在这里会被别人看个一清二楚，\x01",
            "考虑到阿琪的实际情况，这也没办法吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74D4")

    SetScenarioFlags(0xAE, 6)
    SetScenarioFlags(0x6A, 3)
    Jump("loc_751F")

    label("loc_74DF")


    #C0478
    ChrTalk(
        0x153,
        "#1110F小猫咪，到这边来～！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x153, 500)
    Sleep(300)

    #C0479
    ChrTalk(
        0x13,
        "喵呜呜呜～……⊥\x02",
    )

    CloseMessageWindow()

    label("loc_751F")

    Jump("loc_7667")

    label("loc_7524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7540")

    #C0480
    ChrTalk(
        0x13,
        "喵呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7667")

    label("loc_7540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_755A")

    #C0481
    ChrTalk(
        0x13,
        "喵……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7667")

    label("loc_755A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7572")

    #C0482
    ChrTalk(
        0x13,
        "喵～\x02",
    )

    CloseMessageWindow()
    Jump("loc_7667")

    label("loc_7572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_758A")

    #C0483
    ChrTalk(
        0x13,
        "喵？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7667")

    label("loc_758A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_75A4")

    #C0484
    ChrTalk(
        0x13,
        "喵喵。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7667")

    label("loc_75A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_75C2")

    #C0485
    ChrTalk(
        0x13,
        "喵喵喵……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7667")

    label("loc_75C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_75E0")

    #C0486
    ChrTalk(
        0x13,
        "喵～～嗝。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7667")

    label("loc_75E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_761C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_END)), "loc_760B")

    #C0487
    ChrTalk(
        0x13,
        "喵喵喵喵喵～⊥\x02",
    )

    CloseMessageWindow()
    Jump("loc_7617")

    label("loc_760B")


    #C0488
    ChrTalk(
        0x13,
        "喵～～\x02",
    )

    CloseMessageWindow()

    label("loc_7617")

    Jump("loc_7667")

    label("loc_761C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_END)), "loc_7643")

    #C0489
    ChrTalk(
        0x13,
        "喵喵喵～⊥\x02",
    )

    CloseMessageWindow()
    Jump("loc_7667")

    label("loc_7643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_END)), "loc_765B")

    #C0490
    ChrTalk(
        0x13,
        "喵～\x02",
    )

    CloseMessageWindow()
    Jump("loc_7667")

    label("loc_765B")


    #C0491
    ChrTalk(
        0x13,
        "喵喵？\x02",
    )

    CloseMessageWindow()

    label("loc_7667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76F1")

    #C0492
    ChrTalk(
        0x101,
        (
            "#0004F（柯贝是一直住在支援科\x01",
            "  的小猫……）\x02\x03",

            "#0000F（嗯，这家伙挺随性的，\x01",
            "  我们也只是偶尔给它\x01",
            "  带些吃的来而已。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 3)

    label("loc_76F1")

    Return()

    # Function_10_6DFC end

    def Function_11_76F2(): pass

    label("Function_11_76F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7700")
    SetScenarioFlags(0x1, 4)

    label("loc_7700")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_770E")
    SetScenarioFlags(0x1, 4)

    label("loc_770E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_771C")
    SetScenarioFlags(0x1, 4)

    label("loc_771C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_772A")
    SetScenarioFlags(0x1, 4)

    label("loc_772A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7738")
    SetScenarioFlags(0x1, 4)

    label("loc_7738")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_7746")
    SetScenarioFlags(0x1, 4)

    label("loc_7746")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7754")
    SetScenarioFlags(0x1, 4)

    label("loc_7754")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7762")
    SetScenarioFlags(0x1, 4)

    label("loc_7762")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7770")
    SetScenarioFlags(0x1, 4)

    label("loc_7770")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_777E")
    SetScenarioFlags(0x1, 4)

    label("loc_777E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_778C")
    SetScenarioFlags(0x1, 4)

    label("loc_778C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_779A")
    SetScenarioFlags(0x1, 4)

    label("loc_779A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_77A8")
    SetScenarioFlags(0x1, 4)

    label("loc_77A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_77B6")
    SetScenarioFlags(0x1, 4)

    label("loc_77B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_77C4")
    SetScenarioFlags(0x1, 4)

    label("loc_77C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_77D2")
    SetScenarioFlags(0x1, 4)

    label("loc_77D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_77E0")
    SetScenarioFlags(0x1, 4)

    label("loc_77E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_77EE")
    SetScenarioFlags(0x1, 4)

    label("loc_77EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_77FC")
    SetScenarioFlags(0x1, 4)

    label("loc_77FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_780A")
    SetScenarioFlags(0x1, 4)

    label("loc_780A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_7818")
    SetScenarioFlags(0x1, 4)

    label("loc_7818")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7826")
    SetScenarioFlags(0x1, 4)

    label("loc_7826")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_7834")
    SetScenarioFlags(0x1, 4)

    label("loc_7834")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_7842")
    SetScenarioFlags(0x1, 4)

    label("loc_7842")

    Return()

    # Function_11_76F2 end

    def Function_12_7843(): pass

    label("Function_12_7843")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7854")
    Jump("loc_7963")

    label("loc_7854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7949")

    #C0493
    ChrTalk(
        0x103,
        (
            "#0202F蔡特，琪雅就\x01",
            "拜托你照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x14,
        "#1200F呜噜噜噜……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_78EC")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_78EC")


    #C0495
    ChrTalk(
        0x109,
        (
            "#0508F（呜呜……\x01",
            "  我好像还是有点怕狗。）\x02\x03",

            "#0505F（啊，说来这不是狗，是狼呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7963")

    label("loc_7949")


    #C0496
    ChrTalk(
        0x14,
        "#1200F呜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    label("loc_7963")

    TalkEnd(0xFE)
    Return()

    # Function_12_7843 end

    def Function_13_7967(): pass

    label("Function_13_7967")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7978")
    Jump("loc_7ABB")

    label("loc_7978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7ABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A53")
    OP_93(0xFE, 0x0, 0x0)

    #C0497
    ChrTalk(
        0x15,
        (
            "#1110F嗯～好温暖啊～！\x02\x03",

            "#1109F蔡特，来午睡吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x14,
        "#1200F呜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x109,
        (
            "#0509F（好、好可爱……！）\x02\x03",

            "#0502F（嗯～难怪大家\x01",
            "  都那么喜欢她呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        "#0012F（哈哈……是啊。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7ABB")

    label("loc_7A53")


    #C0501
    ChrTalk(
        0x15,
        (
            "#1110F啊，是大家。\x01",
            "一路顺风哦～！\x02\x03",

            "#1109F消灭幽灵，要加油哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x102,
        (
            "#0109F嗯、嗯……\x01",
            "当然会努力啦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ABB")

    TalkEnd(0xFE)
    Return()

    # Function_13_7967 end

    def Function_14_7ABF(): pass

    label("Function_14_7ABF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7B7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7B22")

    #C0503
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈～！\x01",
            "原稿可怎么办啊～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xFE,
        "拜托请快点出现救救我啊～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B79")

    label("loc_7B22")


    #C0505
    ChrTalk(
        0xFE,
        (
            "真是败了～格蕾丝前辈\x01",
            "又不见踪影了。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xFE,
        (
            "前辈不在的话，\x01",
            "原稿可就无法完成了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_7B79")

    Jump("loc_7C40")

    label("loc_7B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7BDD")

    #C0507
    ChrTalk(
        0xFE,
        "格蕾丝前辈～你在哪里呀～！？\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xFE,
        (
            "……不会是又在哪个酒吧里面\x01",
            "大吃大喝吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C40")

    label("loc_7BDD")


    #C0509
    ChrTalk(
        0xFE,
        (
            "真是的，格蕾丝前辈\x01",
            "到底去哪里了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xFE,
        (
            "原稿的截止日期都已经临近了……\x01",
            "（自言自语）……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_7C40")

    TalkEnd(0xFE)
    Return()

    # Function_14_7ABF end

    def Function_15_7C44(): pass

    label("Function_15_7C44")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    SoundLoad(803)
    Sound(803, 2, 0, 0)
    BeginChrThread(0x23, 1, 0, 55)
    SetChrPos(0x101, 1420, 0, -14130, 0)
    SetChrPos(0x102, -290, 0, -16530, 45)
    SetChrPos(0x103, -700, 0, -14800, 90)
    SetChrPos(0x104, 1500, 0, -16379, 0)
    OP_68(-660, 3000, 3390, 0)
    MoveCamera(55, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16370, 0)
    MoveCamera(35, 3, 0, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-21970, 1900, 6540, 0)
    MoveCamera(351, 8, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14980, 0)
    MoveCamera(356, 8, 0, 3000)
    OP_6F(0x79)
    Fade(500)
    OP_68(19900, 3000, 6130, 0)
    MoveCamera(57, 4, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18430, 0)
    MoveCamera(55, -2, 0, 5000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-60, 5700, 23250, 0)
    MoveCamera(359, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11620, 0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    OP_6F(0x79)
    OP_68(-5540, 4000, 5000, 10000)
    MoveCamera(24, 29, 0, 10000)
    OP_6E(800, 10000)
    SetCameraDistance(35000, 10000)
    Sleep(2000)
    PlaceName2(340, 200, "c_plac02", 0x0, 1500)
    OP_6F(0x79)
    EndChrThread(0x23, 0x1)

    #C0511
    ChrTalk(
        0x104,
        (
            "#0300F哎呀呀……还是一点都没变，\x01",
            "真是条喧嚣吵闹的街道啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x101,
        (
            "#0004F因为这里算是克洛斯贝尔的\x01",
            "中心地区呢。\x02\x03",

            "#0000F到处都是大型商店，\x01",
            "如果需要买东西，基本都能在这里解决……\x02\x03",

            "想去其它街区的话，从这里走也都很方便。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x102,
        (
            "#0100F最近导力车的数量也增加了，\x01",
            "这里似乎越来越热闹了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x101,
        "#0002F哈哈，看来是这样呢。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x23, 1, 0, 56)
    Fade(500)
    OP_68(190, 1500, -15740, 0)
    MoveCamera(39, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)

    #C0515
    ChrTalk(
        0x101,
        (
            "#0000F对了，各位，\x01",
            "我们去『导力商店』里看看如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x104,
        (
            "#0305F啊，是那个大叔刚才\x01",
            "说过的导力工房吗？\x02\x03",

            "#0300F听说是个内部装修\x01",
            "焕然一新，十分时尚的工房呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x103,
        (
            "#0203F算是个提高了商业性的\x01",
            "新型工房吧。\x02\x03",

            "#0200F而且已经与警察方面签下了合同，\x01",
            "所以应该也可以进行战术导力器的改造，\x01",
            "或是结晶回路的采购。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x102,
        (
            "#0104F#6P以后大概会频繁去那里吧。\x02\x03",

            "#0100F那么，在去其它街区之前，\x01",
            "不如先进店里问候一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x101,
        "#0000F嗯，就是街角的那个建筑。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0520
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在中央广场，有百货店、导力商店、\x01",
            "武器商会、西餐厅等各种设施。\x02",
        )
    )

    CloseMessageWindow()

    #A0521
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "各种购物场所一应俱全，\x01",
            "因此，若想整理装备，\x01",
            "便可以前往中央广场。\x02",
        )
    )

    CloseMessageWindow()

    #A0522
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外，导力商店『原点』\x01",
            "位于广场的东侧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -290, 0, -16530, 45)
    ModifyEventFlags(0, 2, 0x80)
    SetScenarioFlags(0x44, 4)
    EndChrThread(0x23, 0x1)
    OP_24(0x323)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_7C44 end

    def Function_16_8246(): pass

    label("Function_16_8246")

    EventBegin(0x1)
    SetChrPos(0x18, -6460, -4200, -21000, 135)

    def lambda_825E():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_825E)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8487")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_833A")

    #C0523
    ChrTalk(
        0x101,
        (
            "#0005F噢……街角的那个店\x01",
            "看起来像是武器商会啊。\x02\x03",

            "#0000F之前也听科长说起过，\x01",
            "去里面看看吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_82E7():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_82E7)

    def lambda_82F4():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_82F4)

    def lambda_8301():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8301)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0524
    ChrTalk(
        0x102,
        "#0100F也是呢，进去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_847F")

    label("loc_833A")


    #C0525
    ChrTalk(
        0x101,
        (
            "#0005F噢……等一下。\x01",
            "街角的那个店好像是武器商会啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8378():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8378)

    def lambda_8385():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8385)

    def lambda_8392():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8392)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83F2")

    #C0526
    ChrTalk(
        0x103,
        (
            "#0203F好像是呢。\x02\x03",

            "#0200F了解，先去武器\x01",
            "商会看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_847F")

    label("loc_83F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_844A")

    #C0527
    ChrTalk(
        0x104,
        (
            "#0305F哦，看来没错呢。\x02\x03",

            "#0300F嗯，那就先去武器商会\x01",
            "里面看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_847F")

    label("loc_844A")


    #C0528
    ChrTalk(
        0x102,
        (
            "#0105F啊，真的呢……\x02\x03",

            "#0100F那就先进去\x01",
            "看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_847F")

    SetScenarioFlags(0x1, 3)
    Jump("loc_84D7")

    label("loc_8487")


    #C0529
    ChrTalk(
        0x101,
        (
            "#0000F街角的那个店\x01",
            "好像是武器商会。\x02\x03",

            "之前也听科长说起过，\x01",
            "先去里面看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84D7")

    SetChrPos(0x0, -8660, -4200, -18220, 180)
    EventEnd(0x4)
    Return()

    # Function_16_8246 end

    def Function_17_84EB(): pass

    label("Function_17_84EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x9E, 0xFF, 0xFF)
    OP_68(-640, 1500, 12830, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 0, 0, 14500, 180)
    SetChrPos(0x19F, 750, 0, 13750, 270)
    SetChrPos(0x109, 750, 0, 12750, 315)
    SetChrPos(0x102, -1250, 0, 14250, 135)
    SetChrPos(0x103, -1500, 0, 13000, 90)
    SetChrPos(0x104, -1250, 0, 12000, 45)
    FadeToBright(1000, 0)
    OP_0D()

    #C0530
    ChrTalk(
        0x101,
        (
            "#5P#0000F那么，我们赶快去\x01",
            "挑选礼物吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x104,
        (
            "#12P#0303F话虽如此，但我们已经没有时间了啊。\x02\x03",

            "#0300F小芙兰\x01",
            "不是应该已经前往\x01",
            "西餐厅了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x102,
        (
            "#5P#0103F是啊……如果让应邀而来的\x01",
            "芙兰小姐久等，\x01",
            "也很过意不去呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x19F,
        (
            "#11P那、那么……\x01",
            "该怎么办才好呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x103,
        (
            "#6P#0203F还是先来分工吧。\x02\x03",

            "#0200F我和艾莉前辈、兰迪前辈\x01",
            "先去西餐厅。\x02\x03",

            "向芙兰小姐转达你们\x01",
            "迟些就来的消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        (
            "#5P#0003F在这期间，我和上士\x01",
            "还有安敦先生\x01",
            "赶快去挑选礼物……\x02\x03",

            "#0000F……这样安排似乎比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x19F,
        (
            "#11P太谢谢了，\x01",
            "该怎么感谢你们大家……\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x19F,
        (
            "#11P我的运气实在太好了啊，\x01",
            "竟然有幸得到如此亲切\x01",
            "之人的帮助……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0538
    ChrTalk(
        0x109,
        "#11P#0506F请、请不要眼泪汪汪啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0539
    ChrTalk(
        0x101,
        (
            "#5P#0003F总、总之，\x01",
            "就这么分工吧。\x02\x03",

            "#0000F艾莉、缇欧、兰迪，\x01",
            "那边就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_88E0():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_88E0)

    def lambda_88ED():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_88ED)

    def lambda_88FA():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_88FA)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0540
    ChrTalk(
        0x102,
        "#5P#0100F明白了。\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x103,
        "#6P#0200F那么，稍后见。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x104,
        (
            "#12P#0300F一定要选个能\x01",
            "让她发自内心地感到惊喜的\x01",
            "好礼物哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8987():
        OP_97(0x103, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8987)
    Sleep(50)

    def lambda_89A4():
        OP_97(0x104, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_89A4)
    Sleep(50)

    def lambda_89C1():
        OP_97(0x102, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_89C1)

    def lambda_89DB():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_89DB)

    def lambda_89E8():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_89E8)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)

    def lambda_8A09():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A09)
    Sleep(50)

    def lambda_8A19():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8A19)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)

    #C0543
    ChrTalk(
        0x101,
        (
            "#5P#0000F那么，我们就\x01",
            "去百货店看看吧。\x02\x03",

            "上士，请你帮忙推荐一些\x01",
            "芙兰可能会\x01",
            "喜欢的礼物吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x109,
        "#11P#0506F……唉，没办法，我也来帮忙吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19F, 0x109, 500)

    #C0545
    ChrTalk(
        0x19F,
        "#11P拜托了啊，姐姐！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-10, 2700, 26140, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 0, 800, 24000, 0)
    SetChrPos(0x109, 750, 800, 23250, 0)
    SetChrPos(0x19F, -750, 800, 22500, 0)

    def lambda_8B41():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B41)
    Sleep(50)

    def lambda_8B5E():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8B5E)
    Sleep(50)

    def lambda_8B7B():
        OP_97(0x19F, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_8B7B)
    OP_0D()
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    Sleep(750)

    def lambda_8BB1():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8BB1)
    Sleep(50)

    def lambda_8BC5():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8BC5)
    Sleep(50)

    def lambda_8BD9():
        OP_A7(0x19F, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19F, 2, lambda_8BD9)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x19F, 0x1)
    EndChrThread(0x19F, 0x2)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x9E, 0xFF, 0xFF)
    OP_29(0x2A, 0x1, 0x3)
    NewScene("c0170", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_84EB end

    SaveToFile()

Try(main)
