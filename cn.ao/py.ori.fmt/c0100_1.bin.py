from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0100_1.bin",                # FileName
        "c0100",                    # MapName
        "c0100",                    # Location
        0x0004,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 7, 0, 8],
    )

    BuildStringList((
        "c0100_1",                # 0
    ))

    ChipFrameInfo(256, 0)                                        # 0

    ScpFunction((
        "Function_0_100",          # 00, 0
        "Function_1_C22",          # 01, 1
        "Function_2_1BEB",         # 02, 2
        "Function_3_2767",         # 03, 3
        "Function_4_2CA6",         # 04, 4
        "Function_5_36E4",         # 05, 5
        "Function_6_389D",         # 06, 6
        "Function_7_3AED",         # 07, 7
        "Function_8_416A",         # 08, 8
        "Function_9_4254",         # 09, 9
        "Function_10_48EA",        # 0A, 10
        "Function_11_515F",        # 0B, 11
        "Function_12_53BC",        # 0C, 12
        "Function_13_5DFF",        # 0D, 13
        "Function_14_5F07",        # 0E, 14
        "Function_15_6046",        # 0F, 15
        "Function_16_615A",        # 10, 16
        "Function_17_61E6",        # 11, 17
        "Function_18_6236",        # 12, 18
        "Function_19_628F",        # 13, 19
        "Function_20_6394",        # 14, 20
        "Function_21_7AE7",        # 15, 21
        "Function_22_7F6D",        # 16, 22
        "Function_23_812E",        # 17, 23
        "Function_24_85BC",        # 18, 24
        "Function_25_872D",        # 19, 25
        "Function_26_8B94",        # 1A, 26
    ))


    def Function_0_100(): pass

    label("Function_0_100")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_183")

    #C0001
    ChrTalk(
        0xFE,
        (
            "总算可以出来了……\x01",
            "但那漂浮在空中的大树究竟是什么东西？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "该不会坠落到什么地方吧？\x01",
            "……真是太让人不安了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_191")
    Jump("loc_C1E")

    label("loc_191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269")

    #C0003
    ChrTalk(
        0xFE,
        (
            "总统说过去发生的那些事故\x01",
            "是由两大国的暗斗所引起的……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "也就是两国的间谍人员\x01",
            "相互争斗所招致的结果？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "……老实说，我以前从没仔细思考过这些，\x01",
            "但如果真是如此，那实在是不可饶恕啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2F5")

    label("loc_269")


    #C0006
    ChrTalk(
        0xFE,
        (
            "总统说过去发生的那些事故\x01",
            "是由两大国的暗斗所引起的……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "……老实说，我以前从没仔细思考过这些，\x01",
            "但如果真是如此，那实在是不可饶恕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5")

    Jump("loc_C1E")

    label("loc_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397")

    #C0008
    ChrTalk(
        0xFE,
        (
            "据说那个武装集团\x01",
            "是帝国政府雇佣的……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "既然如此，说不定他们\x01",
            "什么时候还会再来袭击吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "一想到这里，真是非常不安啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_401")

    label("loc_397")


    #C0011
    ChrTalk(
        0xFE,
        (
            "据说那个武装集团\x01",
            "是帝国政府雇佣的……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "一想到他们说不定什么时候还会再来袭击，\x01",
            "真是非常不安啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_401")

    Jump("loc_C1E")

    label("loc_406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_479")

    #C0013
    ChrTalk(
        0xFE,
        (
            "玛因兹的人们\x01",
            "现在一定很难熬吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "一群手持武器的人\x01",
            "突然闯来……\x01",
            "光是想象一下就觉得好可怕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4CC")

    #C0015
    ChrTalk(
        0xFE,
        "妈妈今天叫我去买东西。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "……屋子漏雨了，\x01",
            "要赶快买水桶来接。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_4CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_51B")

    #C0017
    ChrTalk(
        0xFE,
        (
            "竟然出动了那么多辆急救车……\x01",
            "看来是发生了相当严重的事故吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_599")

    #C0018
    ChrTalk(
        0xFE,
        "我真的渴望一个人生活吗？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "虽然的确有些向往独居生活，\x01",
            "不过，如果家里只有一个人在，\x01",
            "大概会相当寂寞吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69E")

    #C0020
    ChrTalk(
        0xFE,
        (
            "打工，打工……\x01",
            "要说稳定又合理的职业，也就是服务员之类的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "不过，如果想尽快多赚些钱，\x01",
            "也可以考虑考虑女公关这条路……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "……不对不对不对，\x01",
            "真是的，我到底在想什么嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "不管能赚到多少钱，\x01",
            "我也绝对不要陪老头子一起喝酒。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6DB")

    label("loc_69E")


    #C0024
    ChrTalk(
        0xFE,
        (
            "如果想一个人生活，就必须要打工……\x01",
            "哪种工作才适合我呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DB")

    Jump("loc_C1E")

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_84D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DA")

    #C0025
    ChrTalk(
        0xFE,
        (
            "如果要一个人生活，\x01",
            "最佳地点自然还是西街一带……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "但考虑到房租等现实问题，\x01",
            "还是应该在东街落户啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "旧城区的房租虽然很便宜，\x01",
            "但治安问题终究让人担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "话说回来，如果想自立，\x01",
            "首先还是要找份工作啊。\x01",
            "……呼。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_848")

    label("loc_7DA")


    #C0029
    ChrTalk(
        0xFE,
        (
            "如果要一个人生活，\x01",
            "最佳地点自然还是西街一带……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "……但话说回来，如果想自立，\x01",
            "首先还是要找份工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_848")

    Jump("loc_C1E")

    label("loc_84D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_89A")

    #C0031
    ChrTalk(
        0xFE,
        "啊，都已经这么晚了啊。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "必须得赶快回家\x01",
            "帮妈妈做事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_89A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_92B")

    #C0033
    ChrTalk(
        0xFE,
        (
            "各国首脑们在转眼之间\x01",
            "就已经进入克洛斯贝尔了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "首脑们都坐在车里，\x01",
            "所以看不清楚面孔……\x01",
            "但却仍然可以感觉到他们的气场呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_92B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C7")

    #C0035
    ChrTalk(
        0xFE,
        (
            "大概因为通商会议从明天就要开始了吧，\x01",
            "现在的警戒态势真是森严呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "刚才我被\x01",
            "巡逻的警察叫住了，\x01",
            "我还是第一次被警察盘问呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A4E")

    label("loc_9C7")


    #C0037
    ChrTalk(
        0xFE,
        (
            "我第一次被警察问话，\x01",
            "不过，总觉得对方很失礼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "毕竟谁都不愿意当众大声说，\x01",
            "自己的工作只是帮忙做家事……\x01",
            "这可是莫大的屈辱啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4E")

    Jump("loc_C1E")

    label("loc_A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_ABD")

    #C0039
    ChrTalk(
        0xFE,
        (
            "我很讨厌因为下雨\x01",
            "就得乖乖待在家里的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "不如撑起自己喜欢的雨伞，\x01",
            "来外面散散步¤\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B37")

    #C0041
    ChrTalk(
        0xFE,
        (
            "一下出动了那么多警车，\x01",
            "真是吓了我一跳。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "不过，这样才有警察的感觉，\x01",
            "倒也挺帅气的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE3")

    #C0043
    ChrTalk(
        0xFE,
        (
            "真是的，我爸爸为什么\x01",
            "要赤身裸体地在家里走来走去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "对已经成年的女儿未免也太欠考虑了……\x01",
            "甚至都可以算是犯罪行为了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        "啊～真想一个人生活啊～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C1E")

    label("loc_BE3")


    #C0046
    ChrTalk(
        0xFE,
        "啊～真想一个人生活啊～\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "嗯～哪里有\x01",
            "合适的房子呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1E")

    TalkEnd(0xFE)
    Return()

    # Function_0_100 end

    def Function_1_C22(): pass

    label("Function_1_C22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D11")

    #C0048
    ChrTalk(
        0xFE,
        (
            "虽然我不了解详情，\x01",
            "但听说政府已经失去了\x01",
            "那种名为『神机』的兵器啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "方法是对是错暂且不论……\x01",
            "迪塔总统确实准备了\x01",
            "足以守护克洛斯贝尔的力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "虽然最后导致了巨大的混乱，\x01",
            "但我觉得实在是无法责怪他啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_D9A")

    label("loc_D11")


    #C0051
    ChrTalk(
        0xFE,
        (
            "方法是对是错暂且不论……\x01",
            "迪塔总统确实准备了\x01",
            "足以守护克洛斯贝尔的力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "虽然最后导致了巨大的混乱，\x01",
            "但我觉得实在是无法责怪他啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9A")

    Jump("loc_1BE7")

    label("loc_D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_DAD")
    Jump("loc_1BE7")

    label("loc_DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5E")

    #C0053
    ChrTalk(
        0xFE,
        "唔……冻结资产宣言吗……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "没想到迪塔市长\x01",
            "竟会采取如此强硬的策略……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "但正如他所说，我们如果想挺起腰杆，\x01",
            "恐怕再没有比现在更合适的时机了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_ECE")

    label("loc_E5E")


    #C0056
    ChrTalk(
        0xFE,
        (
            "没想到迪塔市长\x01",
            "竟会采取如此强硬的策略……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "不过，我们如果想挺起腰杆，\x01",
            "恐怕再没有比现在更合适的时机了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECE")

    Jump("loc_1BE7")

    label("loc_ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1040")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBA")

    #C0058
    ChrTalk(
        0xFE,
        (
            "前些天的那起袭击事件……\x01",
            "肯定是帝国搞的鬼。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "虽然他们最近装出一副好人样，\x01",
            "但为达目的不择手段才是那些家伙的本性……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "暗中使用各种卑劣的手段，\x01",
            "伺机实现侵略的目的……\x01",
            "这正是埃雷波尼亚的真面目！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_103B")

    label("loc_FBA")


    #C0061
    ChrTalk(
        0xFE,
        (
            "前些天的那起袭击事件……\x01",
            "肯定是帝国搞的鬼。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "暗中使用各种卑劣的手段，\x01",
            "伺机实现侵略的目的……\x01",
            "这正是埃雷波尼亚的真面目！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_103B")

    Jump("loc_1BE7")

    label("loc_1040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10D4")

    #C0063
    ChrTalk(
        0xFE,
        "此次事件，说不定是帝国在幕后策划……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "……唔，若真是如此，\x01",
            "我们还像以往一样，处处服从于帝国，\x01",
            "或许根本就无法保卫克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BE7")

    label("loc_10D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_10E2")
    Jump("loc_1BE7")

    label("loc_10E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_11A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115D")

    #C0065
    ChrTalk(
        0xFE,
        (
            "西边好像发生了\x01",
            "什么事故啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "女神保佑，女神保佑……\x01",
            "空之女神爱德丝啊，请您保佑大家吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_119C")

    label("loc_115D")


    #C0067
    ChrTalk(
        0xFE,
        (
            "女神保佑，女神保佑……\x01",
            "空之女神爱德丝啊，请您保佑大家吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_119C")

    Jump("loc_1BE7")

    label("loc_11A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1297")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1240")

    #C0068
    ChrTalk(
        0xFE,
        (
            "虽然并非全部，\x01",
            "但很多年轻人\x01",
            "似乎都赞成独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "真是没经历过战争的一代人啊……\x01",
            "他们真的理解事情的\x01",
            "严重程度吗？太让人不安了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1292")

    label("loc_1240")


    #C0070
    ChrTalk(
        0xFE,
        (
            "真是没经历过战争的一代人啊……\x01",
            "他们真的理解事情的\x01",
            "严重程度吗？太让人不安了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1292")

    Jump("loc_1BE7")

    label("loc_1297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_137A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1348")

    #C0071
    ChrTalk(
        0xFE,
        (
            "唔，老实说，\x01",
            "真没想到，都这么一把年纪了，\x01",
            "还能听到独立这个词汇。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "独立……独立……\x01",
            "如果真能独立，自然像做梦一样，\x01",
            "但我可不认为能顺利成功……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1375")

    label("loc_1348")


    #C0073
    ChrTalk(
        0xFE,
        (
            "独立……独立……\x01",
            "这个美梦真的能成真吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1375")

    Jump("loc_1BE7")

    label("loc_137A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1561")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D9")

    #C0074
    ChrTalk(
        0xFE,
        (
            "通商会议禁止无关人员旁听，\x01",
            "也没有导力通讯的转播。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "也就是说，我们只能通过\x01",
            "市里的宣传报道和媒体界人士\x01",
            "来了解会议的结果了。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "一般来说，主要就是\x01",
            "人尽皆知的克洛斯贝尔时代周刊。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "报道的可信度、稳定性、时效性……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "无论从哪个方面来衡量，\x01",
            "在这个自治州内，想知道最新消息，\x01",
            "没有比克洛斯贝尔时代周刊更好的选择了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_155C")

    label("loc_14D9")


    #C0079
    ChrTalk(
        0xFE,
        (
            "通商会议禁止无关人员旁听，\x01",
            "也没有导力通讯的转播。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "也就是说，我们只能通过\x01",
            "市里的宣传报道和媒体界人士\x01",
            "来了解会议的结果了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_155C")

    Jump("loc_1BE7")

    label("loc_1561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1658")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1602")

    #C0081
    ChrTalk(
        0xFE,
        (
            "呀，不知不觉间，\x01",
            "太阳都已经下山了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "呵呵，这也是因为太过\x01",
            "沉浸于通商会议的气氛了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "必须得赶快回家了，免得老伴担心。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1653")

    label("loc_1602")


    #C0084
    ChrTalk(
        0xFE,
        (
            "呀，不知不觉间，\x01",
            "太阳都已经下山了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        "必须得赶快回家了，免得老伴担心。\x02",
    )

    CloseMessageWindow()

    label("loc_1653")

    Jump("loc_1BE7")

    label("loc_1658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_18C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16C7")

    #C0086
    ChrTalk(
        0xFE,
        (
            "刚才有个东方打扮的女性\x01",
            "进了那家餐厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "真是个充满知性气质\x01",
            "的美女啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BF")

    label("loc_16C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1830")

    #C0088
    ChrTalk(
        0xFE,
        (
            "唔，新市政厅大楼\x01",
            "终于呈现在大家眼前了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "从发表建筑计划的那天算起，已经过去整整五年了。\x01",
            "据传闻说，距离彻底竣工，\x01",
            "本来至少还要再花一年时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "但库罗伊斯市长就任之后，\x01",
            "立刻就决定投入ＩＢＣ的资本。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "拜其所赐，工程并没被无聊的\x01",
            "争权夺利行为所影响，进展得非常顺利，\x01",
            "最后终于在日前竣工了。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "呵呵，真是多亏了\x01",
            "库罗伊斯市长啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18BF")

    label("loc_1830")


    #C0093
    ChrTalk(
        0xFE,
        (
            "从发表建筑计划的那天算起，已经过去整整五年了。\x01",
            "据传闻说，距离彻底竣工，\x01",
            "本来至少还要再花一年时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "呵呵，真不愧是\x01",
            "库罗伊斯市长啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BF")

    Jump("loc_1BE7")

    label("loc_18C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_19EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198B")

    #C0095
    ChrTalk(
        0xFE,
        (
            "嗯，通商会议终于\x01",
            "要在明天开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "不管怎么说，会议的发起人\x01",
            "迪塔市长不仅担任市长一职，\x01",
            "同时也是ＩＢＣ的总裁。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "希望他能在会议过程中\x01",
            "充分发挥自己的领导能力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19E6")

    label("loc_198B")


    #C0098
    ChrTalk(
        0xFE,
        (
            "嗯，通商会议终于\x01",
            "要在明天开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "希望库罗伊斯市长\x01",
            "充分发挥出\x01",
            "自己的领导能力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E6")

    Jump("loc_1BE7")

    label("loc_19EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_19F9")
    Jump("loc_1BE7")

    label("loc_19F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1BE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A57")

    #C0100
    ChrTalk(
        0xFE,
        (
            "我在这里看到了\x01",
            "刚才的逮捕行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "看来警察也\x01",
            "很努力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BE7")

    label("loc_1A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B57")

    #C0102
    ChrTalk(
        0xFE,
        (
            "与教团事件有所牵连的帝国派、\x01",
            "共和国派渎职议员已经下台，\x01",
            "鲁巴彻也从黑道势力中覆灭。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "但即使如此，\x01",
            "帝国派议员在席位总数中占据首位\x01",
            "的现状仍然没有改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "听说库罗伊斯市长已经开始加大力度\x01",
            "修正法律了……但还是希望他能\x01",
            "再努力些啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BE7")

    label("loc_1B57")


    #C0105
    ChrTalk(
        0xFE,
        "……好像是叫黑月吧。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "鲁巴彻覆灭之后，\x01",
            "据说他们的势力\x01",
            "就越来越大了。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "希望库罗伊斯市长\x01",
            "再加把劲，\x01",
            "制定出能让市民们安心生活的法律。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BE7")

    TalkEnd(0xFE)
    Return()

    # Function_1_C22 end

    def Function_2_1BEB(): pass

    label("Function_2_1BEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1C75")

    #C0108
    ChrTalk(
        0xFE,
        (
            "接下来，我准备\x01",
            "回兰花塔去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "市政厅那边现在大概也是一片混乱吧，\x01",
            "但如果谁都不去，\x01",
            "混乱的情况就始终无法平息了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2763")

    label("loc_1C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1C83")
    Jump("loc_2763")

    label("loc_1C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C91")
    Jump("loc_2763")

    label("loc_1C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D37")

    #C0110
    ChrTalk(
        0xFE,
        "哈哈，米米天真无邪，真是可爱啊。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "武装集团为什么要\x01",
            "带走克洛斯贝尔的大钟呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "我认为那种东西\x01",
            "并不是那么值得盗取……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1D9C")

    label("loc_1D37")


    #C0113
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "武装集团为什么要\x01",
            "带走克洛斯贝尔的大钟呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "我认为那种东西\x01",
            "并不是那么值得盗取……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9C")

    Jump("loc_2763")

    label("loc_1DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1DF0")

    #C0115
    ChrTalk(
        0xFE,
        (
            "真担心玛因兹的人啊……\x01",
            "那里肯定也有和米米差不多大的孩子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2763")

    label("loc_1DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1E31")

    #C0116
    ChrTalk(
        0xFE,
        "米米，快看。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "小蜗牛在护栏上\x01",
            "爬来爬去呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2763")

    label("loc_1E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1EC8")

    #C0118
    ChrTalk(
        0xFE,
        (
            "急救车开得相当快啊，\x01",
            "不过这也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "那种在紧急时刻出动的\x01",
            "特殊车辆并没有速度限制，\x01",
            "每当看到的时候，还真是有点提心吊胆。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2763")

    label("loc_1EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1FF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8F")

    #C0120
    ChrTalk(
        0xFE,
        "嗯～导力车就是好啊～\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "但令人无奈的是，\x01",
            "它的价格实在太高，\x01",
            "平民根本买不起。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "就算价格降到现在的一半，也还是很难承受。\x01",
            "如果能降到两折以下，\x01",
            "就在接受范围之内了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1FED")

    label("loc_1F8F")


    #C0123
    ChrTalk(
        0xFE,
        "嗯～导力车就是好啊～\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "虽然现在肯定买不起，\x01",
            "但等我到了退休年龄时，\x01",
            "说什么也得买一辆。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FED")

    Jump("loc_2763")

    label("loc_1FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_217B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20FB")

    #C0125
    ChrTalk(
        0xFE,
        (
            "最近这段时间，\x01",
            "到处都在热烈讨论\x01",
            "有关独立的话题……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "但希望大家也不要忘记，\x01",
            "就在日前，基本交通法已经做出了修正。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "在这次的修正中，\x01",
            "除了以往的罚金制度之外，\x01",
            "还增加了『扣留驾照制度』。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "希望这种举措能使导力车\x01",
            "事故减少一些。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2176")

    label("loc_20FB")


    #C0129
    ChrTalk(
        0xFE,
        (
            "今后，如果触犯法规达到一定程度，\x01",
            "将会被暂时扣留驾照……\x01",
            "也就是不能开车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "希望这种举措能使导力车\x01",
            "事故减少一些。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2176")

    Jump("loc_2763")

    label("loc_217B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2189")
    Jump("loc_2763")

    label("loc_2189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_21DC")

    #C0131
    ChrTalk(
        0xFE,
        (
            "哎呀，让你们久等了，\x01",
            "真是不好意思啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        "那我们就赶快出发吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2763")

    label("loc_21DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21EA")
    Jump("loc_2763")

    label("loc_21EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2248")

    #C0133
    ChrTalk(
        0xFE,
        (
            "随着市政厅的迁址，\x01",
            "我暂时要在\x01",
            "兰花塔上班了。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        "呼，接下来可能会很忙啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2763")

    label("loc_2248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_257F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_250C")

    #C0135
    ChrTalk(
        0xFE,
        (
            "我昨天看见了……\x01",
            "你们开着一辆非常罕见的\x01",
            "导力车啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#00000F是的，那是\x01",
            "蔡斯中央工房的新型导力车。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    #C0137
    ChrTalk(
        0xFE,
        "什么！？蔡斯中央工房竟然制造导力车了！？\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        "顺、顺便问问，你们知道它的最高时速吗？\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x109,
        (
            "#10102F嗯，虽然还没有亲自尝试过，\x01",
            "但据说可以稳定保持在１５００赛尔矩。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "什、什么……！\x01",
            "那种车型竟然能达到如此高速，\x01",
            "蔡斯中央工房实在是有一套啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "唔～如此一来，\x01",
            "导力车的制造业\x01",
            "终于要进入三强抗衡的时代了。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "嗯，真是越来越期待\x01",
            "今后的发展了！\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x109,
        (
            "#10109F是啊～！\x02\x03",

            "竞争将会比以往更加激烈，\x01",
            "今后肯定会不断出现各种更棒的车型……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0144
    ChrTalk(
        0x101,
        "#00012F聊、聊得热火朝天啊。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        "#00109F呵呵，诺艾尔小姐真是很喜欢车呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 0)
    Jump("loc_257A")

    label("loc_250C")


    #C0146
    ChrTalk(
        0xFE,
        (
            "没想到蔡斯中央工房竟然\x01",
            "也开始开发导力车了！\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "嗯嗯，既然如此，\x01",
            "今后一定要密切关注各家制造商的动向啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_257A")

    Jump("loc_2763")

    label("loc_257F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2763")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25EF")

    #C0148
    ChrTalk(
        0xFE,
        (
            "交通法的修正\x01",
            "真是迫在眉睫了。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "现在让米米一个人在外面玩，\x01",
            "实在是很担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2763")

    label("loc_25EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B9")

    #C0150
    ChrTalk(
        0xFE,
        (
            "不久之前，我看到\x01",
            "一辆驾驶速度超快的导力车\x01",
            "从中央广场穿越而过。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "那种速度明显很危险，\x01",
            "于是我立刻通报给警察了……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "不知道最后有没有把驾驶者抓住，\x01",
            "真怕那种车今后再出现啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2763")

    label("loc_26B9")


    #C0153
    ChrTalk(
        0xFE,
        (
            "话说回来，依据现在的基本交通法，\x01",
            "就算因危险驾驶而遭到拘捕，\x01",
            "需要接受的处罚也仅仅是罚款而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "不过，议会最近正在讨论\x01",
            "加强交通处罚的提案，\x01",
            "期待今后能有所改善啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2763")

    TalkEnd(0xFE)
    Return()

    # Function_2_1BEB end

    def Function_3_2767(): pass

    label("Function_3_2767")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_27EB")

    #C0155
    ChrTalk(
        0xFE,
        (
            "老公要回市政厅，\x01",
            "我们准备先回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "虽然心里还是很不安……\x01",
            "但只要和家人在一起，\x01",
            "我就有勇气克服一切困难。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA2")

    label("loc_27EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_27F9")
    Jump("loc_2CA2")

    label("loc_27F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2872")

    #C0157
    ChrTalk(
        0xFE,
        (
            "在最近这一周，\x01",
            "基本没有看到过游客。\x01",
            "这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "……克洛斯贝尔的未来\x01",
            "究竟会是怎样的呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA2")

    label("loc_2872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_28FC")

    #C0159
    ChrTalk(
        0xFE,
        (
            "导游工作暂时歇业，\x01",
            "所以我们一家三口可以待在一起了。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "虽然心里还是很不安……\x01",
            "但只要看到孩子的笑脸，就觉得平静多了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA2")

    label("loc_28FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_290A")
    Jump("loc_2CA2")

    label("loc_290A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2918")
    Jump("loc_2CA2")

    label("loc_2918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2926")
    Jump("loc_2CA2")

    label("loc_2926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2934")
    Jump("loc_2CA2")

    label("loc_2934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2942")
    Jump("loc_2CA2")

    label("loc_2942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A30")

    #C0161
    ChrTalk(
        0xFE,
        "嗯，咳咳。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "各位右后方的那座建筑\x01",
            "是『导力商店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "它的名字是『原点』，\x01",
            "是一家经营整个大陆的导力制品，\x01",
            "远近闻名的商店。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "本地市民们自不必说，\x01",
            "这家处在时代最前端的商店\x01",
            "在游客群体中也很受欢迎哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2AAD")

    label("loc_2A30")


    #C0165
    ChrTalk(
        0xFE,
        (
            "嗯，各位右后方的那座建筑\x01",
            "是『导力商店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "本地市民们自不必说，\x01",
            "这家处在时代最前端的商店\x01",
            "在游客群体中也很受欢迎哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAD")

    Jump("loc_2CA2")

    label("loc_2AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2AF1")

    #C0167
    ChrTalk(
        0xFE,
        (
            "嗯，快走吧，\x01",
            "我和米米的肚子都饿得咕咕叫了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA2")

    label("loc_2AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B0C")
    Call(1, 6)
    Jump("loc_2C78")

    label("loc_2B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BFE")

    #C0168
    ChrTalk(
        0xFE,
        "嗯，咳咳。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "在各位的右手处所能看到的那口钟\x01",
            "名叫『克洛斯贝尔之钟』。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "据说，它的起源可以追溯到\x01",
            "５００年以前的中世纪时代。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "自七耀历１１８５年挖掘出土以来，\x01",
            "到如今已经成为这座城市的象征，\x01",
            "深受广大市民的喜爱。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C78")

    label("loc_2BFE")


    #C0172
    ChrTalk(
        0xFE,
        (
            "嗯，在各位的右手处所能看到的那口钟\x01",
            "名叫『克洛斯贝尔之钟』。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "据说，它的起源可以追溯到\x01",
            "５００年以前的中世纪时代。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C78")

    Jump("loc_2CA2")

    label("loc_2C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C8B")
    Jump("loc_2CA2")

    label("loc_2C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2C99")
    Jump("loc_2CA2")

    label("loc_2C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2CA2")

    label("loc_2CA2")

    TalkEnd(0xFE)
    Return()

    # Function_3_2767 end

    def Function_4_2CA6(): pass

    label("Function_4_2CA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2D9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D48")

    #C0174
    ChrTalk(
        0xFE,
        (
            "爸爸说他\x01",
            "还要去工作～\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "对了，罗伊德哥哥，\x01",
            "你们也一直在工作吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "米米会一直给你们\x01",
            "加油鼓劲的！\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        "#00000F嗯，谢谢啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2D95")

    label("loc_2D48")


    #C0178
    ChrTalk(
        0xFE,
        (
            "爸爸和罗伊德哥哥都在努力工作，\x01",
            "真了不起～\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "米米也要努力给大家加油。\x02",
    )

    CloseMessageWindow()

    label("loc_2D95")

    Jump("loc_36E0")

    label("loc_2D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2DA8")
    Jump("loc_36E0")

    label("loc_2DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2E51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E00")

    #C0180
    ChrTalk(
        0xFE,
        (
            "那辆装有显示屏的导力车\x01",
            "好帅啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        "爸爸应该很喜欢吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2E4C")

    label("loc_2E00")


    #C0182
    ChrTalk(
        0xFE,
        (
            "在市政厅工作的爸爸\x01",
            "现在十分繁忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "而妈妈所在的旅行公司\x01",
            "却在停业。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E4C")

    Jump("loc_36E0")

    label("loc_2E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2EF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC2")

    #C0184
    ChrTalk(
        0xFE,
        (
            "嗯，在各位的右手处所能看到的那口钟\x01",
            "名叫克洛斯贝尔之钟～\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "哎？\x01",
            "钟怎么不见了？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2EEB")

    label("loc_2EC2")


    #C0186
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的大钟\x01",
            "跑到什么地方去了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EEB")

    Jump("loc_36E0")

    label("loc_2EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_301C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FCA")

    #C0187
    ChrTalk(
        0xFE,
        (
            "不知是怎么回事，\x01",
            "今天有很多人愁眉不展呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "啊，罗伊德哥哥，你们也是……\x01",
            "这可不行啊，要打起精神来！\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        "#00000F啊……嗯，你说的对。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        "#00100F谢谢你，米米。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "哪里，\x01",
            "不客气哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3017")

    label("loc_2FCA")


    #C0192
    ChrTalk(
        0xFE,
        (
            "不知是怎么回事，\x01",
            "今天有很多人愁眉不展呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "大家会被太阳公公笑话的。\x02",
    )

    CloseMessageWindow()

    label("loc_3017")

    Jump("loc_36E0")

    label("loc_301C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3052")

    #C0194
    ChrTalk(
        0xFE,
        "哇，真的。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "它是不是迷路了呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_36E0")

    label("loc_3052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_30AC")

    #C0196
    ChrTalk(
        0xFE,
        (
            "当急救车通行的时候，\x01",
            "大家必须要把道路\x01",
            "让出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        "这是交通法规之一。\x02",
    )

    CloseMessageWindow()
    Jump("loc_36E0")

    label("loc_30AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_313F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3110")

    #C0198
    ChrTalk(
        0xFE,
        "嘟嘟～嘟嘟～\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "爸爸好像又在\x01",
            "想导力车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        "他真是很喜欢车啊～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_313A")

    label("loc_3110")


    #C0201
    ChrTalk(
        0xFE,
        "嘟嘟～嘟嘟～\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        "副驾驶席是米米的。\x02",
    )

    CloseMessageWindow()

    label("loc_313A")

    Jump("loc_36E0")

    label("loc_313F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_31F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31AB")

    #C0203
    ChrTalk(
        0xFE,
        (
            "嗯，在各位的右手处\x01",
            "所能看到的是……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        "？？？\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        "哎？右手处就是右手啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_31EE")

    label("loc_31AB")


    #C0206
    ChrTalk(
        0xFE,
        (
            "唔……妈妈是\x01",
            "怎么说的来着？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "在右手处能看到的是……右手？\x02",
    )

    CloseMessageWindow()

    label("loc_31EE")

    Jump("loc_36E0")

    label("loc_31F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_325D")

    #C0208
    ChrTalk(
        0xFE,
        "嗯嗯，原来如此，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "既然如此，一定得买些\x01",
            "特产回去啊。\x01",
            "咔擦咔擦（假装拍照）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E0")

    label("loc_325D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_32AE")

    #C0210
    ChrTalk(
        0xFE,
        "今天要在外面吃饭¤\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "米米想吃东街那家餐厅\x01",
            "的『东方料理』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E0")

    label("loc_32AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_332A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C9")
    Call(1, 6)
    Jump("loc_3325")

    label("loc_32C9")


    #C0212
    ChrTalk(
        0xFE,
        "嗯嗯，原来如此，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "既然如此，一定要\x01",
            "拍些照片才行啊。\x01",
            "咔擦咔擦（假装拍照）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3325")

    Jump("loc_36E0")

    label("loc_332A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_35B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_355F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F8")
    TurnDirection(0xB, 0x1A2, 0)
    Sleep(300)

    #C0214
    ChrTalk(
        0xB,
        (
            "啊，罗伊德哥哥，你们带着一个\x01",
            "米米不认识的孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xB,
        (
            "嘿嘿嘿，他的衣服好帅气啊。\x01",
            "这就是东方风格的服装吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0216
    ChrTalk(
        0x1A2,
        (
            "哦？你竟能看出这衣服的档次，\x01",
            "倒也很有眼光嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x1A2,
        (
            "哼哼，这可是全世界仅此一件\x01",
            "的特别定制服装哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        "特别定制？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "嘿，原来是\x01",
            "定制的戏服啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0220
    ChrTalk(
        0x1A2,
        "不对不对，不是的……\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#00002F（哈哈，他们两个的对话\x01",
            "  还真是天真有趣呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DC, 6)
    Jump("loc_355A")

    label("loc_34F8")

    TurnDirection(0xB, 0x1A2, 0)
    Sleep(300)

    #C0222
    ChrTalk(
        0xB,
        (
            "定制戏服……\x01",
            "哎？原来你是演员啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0223
    ChrTalk(
        0x1A2,
        "都说过不是了……\x02",
    )

    CloseMessageWindow()

    label("loc_355A")

    Jump("loc_35B0")

    label("loc_355F")


    #C0224
    ChrTalk(
        0xFE,
        (
            "爸爸说，他暂时不能\x01",
            "陪米米一起玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        "既然爸爸有工作要做，我必须要忍耐。\x02",
    )

    CloseMessageWindow()

    label("loc_35B0")

    Jump("loc_36E0")

    label("loc_35B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_364A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D0")
    Call(1, 5)
    Jump("loc_3645")

    label("loc_35D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3606")

    #C0226
    ChrTalk(
        0xFE,
        "哗哗，哗哗¤\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        "今天下雨哦～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3645")

    label("loc_3606")


    #C0228
    ChrTalk(
        0xFE,
        (
            "爸爸只要一看见导力车，\x01",
            "目光就再也移不开了～\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "真是的～\x02",
    )

    CloseMessageWindow()

    label("loc_3645")

    Jump("loc_36E0")

    label("loc_364A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_36E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_369F")

    #C0230
    ChrTalk(
        0xFE,
        (
            "开车时应该\x01",
            "遵守交通规则啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        "连米米都知道的～\x02",
    )

    CloseMessageWindow()
    Jump("loc_36E0")

    label("loc_369F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36B1")
    Call(1, 5)
    Jump("loc_36E0")

    label("loc_36B1")


    #C0232
    ChrTalk(
        0xFE,
        (
            "新·特别任务支援科的各位，\x01",
            "工作要加油哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E0")

    TalkEnd(0xFE)
    Return()

    # Function_4_2CA6 end

    def Function_5_36E4(): pass

    label("Function_5_36E4")


    #C0233
    ChrTalk(
        0xB,
        (
            "啊，罗伊德哥哥和艾莉姐姐！\x01",
            "还有……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0234
    ChrTalk(
        0xB,
        (
            "哎？缇欧姐姐和\x01",
            "兰迪哥哥呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xB,
        (
            "特别任务支援科\x01",
            "还在休假吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        (
            "#00012F不，\x01",
            "不是的……\x02\x03",

            "#00000F他们两人还有\x01",
            "其它的工作要处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        (
            "#00100F嗯，这两位是\x01",
            "特别任务支援科的新成员哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0238
    ChrTalk(
        0xB,
        "哎，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xB,
        (
            "那你们以后就该叫\x01",
            "新·特别任务支援科了吧¤\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x105,
        (
            "#10302F哈哈，这个名字\x01",
            "取得很准确呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x109,
        "#10109F呵呵，以后请多关照哦。\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xB,
        "嗯，请多关照！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 1)
    Return()

    # Function_5_36E4 end

    def Function_6_389D(): pass

    label("Function_6_389D")

    OP_4B(0xB, 0xFF)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0xF, 0x0, 0)

    #C0243
    ChrTalk(
        0xB,
        "啊，是罗伊德哥哥和大家。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xB,
        (
            "我来把妈妈介绍给你们吧。\x01",
            "妈妈的工作是导游哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xF,
        "呵呵，初次见面。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xF,
        (
            "我女儿总是\x01",
            "受到你们的关照，\x01",
            "真是多谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#00000F哪里，\x01",
            "我们也没做什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#00100F话说回来，观光导游这种工作\x01",
            "真是很棒呢。\x02\x03",

            "您今天也在工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xF,
        (
            "不，在通商会议期间，\x01",
            "我们暂时休假。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xF,
        (
            "所以我打算\x01",
            "陪着孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x105,
        "#10302F嗯？但还是穿着工作制服啊。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xF,
        "嗯，这是……\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xB,
        "是我要妈妈穿的。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xB,
        "我想让她陪我玩扮演导游的游戏。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#00302F哈哈，原来如此，\x01",
            "真不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xB,
        "对吧¤\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xB,
        (
            "罗伊德哥哥，\x01",
            "你们路上要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xB, 0x0, 0x0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x14A, 2)
    Return()

    # Function_6_389D end

    def Function_7_3AED(): pass

    label("Function_7_3AED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B2D")

    #C0258
    ChrTalk(
        0xFE,
        (
            "那棵巨大的树是什么……\x01",
            "怎么会有那种东西？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4166")

    label("loc_3B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3B3B")
    Jump("loc_4166")

    label("loc_3B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B65")

    #C0259
    ChrTalk(
        0xFE,
        "亚里欧斯先生太帅了～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4166")

    label("loc_3B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3BB9")

    #C0260
    ChrTalk(
        0xFE,
        (
            "今天好像要在\x01",
            "行政区那边召开\x01",
            "一场慈善宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        "要不要过去看看？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4166")

    label("loc_3BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3C62")

    #C0262
    ChrTalk(
        0xFE,
        (
            "神秘武装集团真是太可怕了。\x01",
            "但爸爸说，就算是为了让那些家伙\x01",
            "别再看扁我们，也应该坚持独立……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "居民投票啊……如果我们年满十八岁，\x01",
            "就可以参加投票了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4166")

    label("loc_3C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3C70")
    Jump("loc_4166")

    label("loc_3C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3CBB")

    #C0264
    ChrTalk(
        0xFE,
        (
            "急救车可真是气势汹汹啊。\x01",
            "……但愿别开得太急，发生事故。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4166")

    label("loc_3CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D20")

    #C0265
    ChrTalk(
        0xFE,
        "哎？你要停止减肥吗！？\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "唔唔唔，而且还一副很决绝的样子……\x01",
            "我可不要像你一样！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4166")

    label("loc_3D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D91")

    #C0267
    ChrTalk(
        0xFE,
        "…………………………………\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "……如果你为了减肥什么都愿意做的话，\x01",
            "可以试试运动，或者节食？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4166")

    label("loc_3D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E0C")

    #C0269
    ChrTalk(
        0xFE,
        (
            "亚里欧斯先生\x01",
            "和阿尔伯特大公\x01",
            "的关系好像很亲近啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "真不错啊～如果可能，\x01",
            "我也想和他们两位交个朋友～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4166")

    label("loc_3E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3E76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E2C")
    Call(1, 8)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_3E71")

    label("loc_3E2C")


    #C0271
    ChrTalk(
        0xFE,
        "嗯～这样啊。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "（……看她这样子，\x01",
            "  根本就已经不再跑了吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E71")

    Jump("loc_4166")

    label("loc_3E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F12")

    #C0273
    ChrTalk(
        0xFE,
        (
            "你看到阿尔伯特大公了吗！？\x01",
            "那大胡子是不是很帅？\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "奥斯本宰相也很帅气，\x01",
            "但总有点难以接近的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        "总之，他们两人的胡子都很帅气呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_4166")

    label("loc_3F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F9F")

    #C0276
    ChrTalk(
        0xFE,
        (
            "亚里欧斯先生自不用说，\x01",
            "迪塔市长也相当完美啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "呼，但相比恋人来说，\x01",
            "他还是更接近我理想中的爸爸。\x01",
            "能不能收我当养女呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4166")

    label("loc_3F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3FAD")
    Jump("loc_4166")

    label("loc_3FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4166")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FFB")

    #C0278
    ChrTalk(
        0xFE,
        "……嗯？有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        "我现在有点忙呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_4166")

    label("loc_3FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_411A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40C4")

    #C0280
    ChrTalk(
        0xFE,
        (
            "刚才被一个奇怪的\x01",
            "红发男子搭讪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "虽然他长得很帅，但并不是我喜欢的类型。\x01",
            "我对他说了自己的想法之后，\x01",
            "他却说『彼此彼此，不用介意☆』……\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        "气、气死我了～！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4115")

    label("loc_40C4")


    #C0283
    ChrTalk(
        0xFE,
        (
            "正常人会在自己主动搭讪\x01",
            "之后又说出那种失礼的话吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        "气、气死我了～！！\x02",
    )

    CloseMessageWindow()

    label("loc_4115")

    Jump("loc_4166")

    label("loc_411A")


    #C0285
    ChrTalk(
        0xFE,
        (
            "作业～？\x01",
            "谁会写那种东西嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "亚里欧斯先生好像又出差了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4166")

    TalkEnd(0xFE)
    Return()

    # Function_7_3AED end

    def Function_8_416A(): pass

    label("Function_8_416A")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0287
    ChrTalk(
        0xC,
        (
            "对了，利娜莉，\x01",
            "你还在坚持慢跑吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xD,
        (
            "哎？啊……嗯……\x01",
            "差不多吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xD,
        (
            "但我觉得勉强自己减肥\x01",
            "也不太好，\x01",
            "所以最近只在想跑的时候才去跑……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xC,
        "……这样啊。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xC,
        (
            "（……看她这样子，\x01",
            "  根本就已经不再跑了吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_8_416A end

    def Function_9_4254(): pass

    label("Function_9_4254")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_42B9")

    #C0292
    ChrTalk(
        0xFE,
        (
            "嗯，那蓝白色的光芒\x01",
            "虽然漂亮……\x01",
            "但真是非常诡异啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        "接下来会发生什么呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_48E6")

    label("loc_42B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_42C7")
    Jump("loc_48E6")

    label("loc_42C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4335")

    #C0294
    ChrTalk(
        0xFE,
        (
            "嗯嗯，那白色的军装\x01",
            "也非常适合他。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "只要有亚里欧斯先生在，\x01",
            "不管发生什么情况都不用担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E6")

    label("loc_4335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4390")

    #C0296
    ChrTalk(
        0xFE,
        (
            "好啊，参加慈善活动\x01",
            "是件很有意义的事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        "也邀请些其他朋友一起去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_48E6")

    label("loc_4390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_43FF")

    #C0298
    ChrTalk(
        0xFE,
        "我们只有十五岁呢。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "老实说，我并不是很了解独立的利弊……\x01",
            "不能参加投票，反而松了一口气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E6")

    label("loc_43FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_440D")
    Jump("loc_48E6")

    label("loc_440D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_444A")

    #C0300
    ChrTalk(
        0xFE,
        (
            "普鲁娜，你真是的，\x01",
            "不要说那么可怕的话啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E6")

    label("loc_444A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_449D")

    #C0301
    ChrTalk(
        0xFE,
        "我……决定了。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "我要放弃减肥，\x01",
            "寻找一个喜欢现在的我的男人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E6")

    label("loc_449D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_450C")

    #C0303
    ChrTalk(
        0xFE,
        (
            "呼～难道就没有既不用运动，\x01",
            "也不必节食的减肥方法吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        "无论什么方法都好，谁能教教我啊～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_48E6")

    label("loc_450C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4597")

    #C0305
    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "亚里欧斯先生曾经还被\x01",
            "雷米菲利亚公国授予过勋章呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "那两个人的关系之所以这么好，\x01",
            "说不定就是以此为契机的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E6")

    label("loc_4597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4618")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45B7")
    Call(1, 8)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_4613")

    label("loc_45B7")


    #C0307
    ChrTalk(
        0xFE,
        (
            "虽、虽说是只在想跑时才跑，\x01",
            "但我还是一直在坚持的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        (
            "唔……干脆今天\x01",
            "就跑步回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4613")

    Jump("loc_48E6")

    label("loc_4618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4771")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46EB")

    #C0309
    ChrTalk(
        0xFE,
        (
            "每句话都不离胡子……\x01",
            "普鲁娜还真是喜欢胡子大叔啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "相比之下，\x01",
            "站在奥利维特皇子身旁的\x01",
            "那个高个子军人才是我喜欢的类型。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "哪怕是一次也好，真想被\x01",
            "那种体格的人来一次公主抱啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_476C")

    label("loc_46EB")


    #C0312
    ChrTalk(
        0xFE,
        (
            "相比之下，\x01",
            "站在奥利维特皇子身旁的\x01",
            "那个高个子军人才是我喜欢的类型。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "哪怕是一次也好，真想被\x01",
            "那种体格的人来一次公主抱啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_476C")

    Jump("loc_48E6")

    label("loc_4771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_47CD")

    #C0314
    ChrTalk(
        0xFE,
        (
            "迪塔市长确实是\x01",
            "理想的爸爸呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "至少和我爸爸那样的\x01",
            "邋遢大叔完全不同。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E6")

    label("loc_47CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_47DB")
    Jump("loc_48E6")

    label("loc_47DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_48E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_482C")

    #C0316
    ChrTalk(
        0xFE,
        "危险驾驶？不知道～\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "我们正在专心\x01",
            "聊天呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E6")

    label("loc_482C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4893")

    #C0318
    ChrTalk(
        0xFE,
        (
            "……那个红头发的老兄\x01",
            "真是个怪人啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "他刚才跑进百货店了，\x01",
            "到底是什么人呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E6")

    label("loc_4893")


    #C0320
    ChrTalk(
        0xFE,
        (
            "啊～对了，今天傍晚\x01",
            "主日学校还有课呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        "普鲁娜，你把上次留的作业写完了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_48E6")

    TalkEnd(0xFE)
    Return()

    # Function_9_4254 end

    def Function_10_48EA(): pass

    label("Function_10_48EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_497C")

    #C0322
    ChrTalk(
        0xFE,
        (
            "为、为什么那么巨大的树\x01",
            "会飘浮在空中？\x01",
            "从物理角度讲，那根本不可能啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "话说回来，我现在还在这里发气球，\x01",
            "是不是有些……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_515B")

    label("loc_497C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_498A")
    Jump("loc_515B")

    label("loc_498A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4A09")

    #C0324
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔独立吗……\x01",
            "这可真是不得了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "虽然现在的气氛并不欢快，\x01",
            "但还是制作一款\x01",
            "建国纪念版的新气球吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_515B")

    label("loc_4A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4A17")
    Jump("loc_515B")

    label("loc_4A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4A93")

    #C0326
    ChrTalk(
        0xFE,
        (
            "我并不了解什么武装集团，\x01",
            "但他们真是做了很过分的事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "真希望他们能像松手的气球一样，\x01",
            "飞得越远越好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_515B")

    label("loc_4A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4AA1")
    Jump("loc_515B")

    label("loc_4AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4B07")

    #C0328
    ChrTalk(
        0xFE,
        (
            "要来个气球吗～？\x01",
            "……现在似乎不是说这些的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "唔～到底发生\x01",
            "什么事故了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_515B")

    label("loc_4B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4BDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B8E")

    #C0330
    ChrTalk(
        0xFE,
        "要来个气球吗～？\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "成年人也不必不好意思，\x01",
            "拿一个吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        (
            "偶尔忘掉那些烦心事，\x01",
            "找回久违的童心吧～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4BD6")

    label("loc_4B8E")


    #C0333
    ChrTalk(
        0xFE,
        (
            "成年人也不必不好意思，\x01",
            "拿一个吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "偶尔也\x01",
            "找回久违的童心吧～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BD6")

    Jump("loc_515B")

    label("loc_4BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CAB")

    #C0335
    ChrTalk(
        0xFE,
        (
            "之前有个\x01",
            "儿童游客问我\x01",
            "『气球为什么可以飘在空中』。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "我当时毫不迟疑\x01",
            "地回答道\x01",
            "『因为气球里面充满梦想』……\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "但现在的小孩子可真是过分啊，\x01",
            "听了之后，竟然不屑一顾地耻笑我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4CFE")

    label("loc_4CAB")


    #C0338
    ChrTalk(
        0xFE,
        "要怀有梦想啊，孩子们。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "比空气更轻的气体？\x01",
            "不不，气球里面包含的都是梦想。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CFE")

    Jump("loc_515B")

    label("loc_4D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4D5C")

    #C0340
    ChrTalk(
        0xFE,
        "要来个气球吗～？\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "现在可以领取印有参加通商会议\x01",
            "各国国徽的气球哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_515B")

    label("loc_4D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4DC5")

    #C0342
    ChrTalk(
        0xFE,
        "好了，今天差不多也该回去了。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        (
            "拜通商会议所赐，今天的人很多，\x01",
            "我发出去了很多气球。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_515B")

    label("loc_4DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E37")

    #C0344
    ChrTalk(
        0xFE,
        (
            "嘿～高级轿车通过这里的时候，\x01",
            "我还真是很紧张～\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "有一种和创立纪念庆典时\x01",
            "有所不同的激动感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_515B")

    label("loc_4E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_501E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F69")
    TurnDirection(0xE, 0x1A2, 0)
    Sleep(300)

    #C0346
    ChrTalk(
        0xE,
        (
            "哦，这位小朋友，\x01",
            "要拿个气球吗？\x01",
            "气球轻飘飘地浮在空中，很有趣哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x1A2,
        (
            "不要。\x01",
            "那种东西只会碍事而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xE,
        (
            "好，那你想要什么颜色……\x01",
            "……哎哎！？\x01",
            "你刚才说气球只会碍事？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        (
            "#00000F（哈哈，看来\x01",
            "  秦很讨厌会显得\x01",
            "  孩子气的行为。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1DD, 1)
    Jump("loc_4FD1")

    label("loc_4F69")


    #C0350
    ChrTalk(
        0xE,
        (
            "虽然也有不少孩子\x01",
            "对气球不感兴趣……\x01",
            "但真没想到会被否定得如此彻底啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xE,
        "这实在是让我有些受打击。\x02",
    )

    CloseMessageWindow()

    label("loc_4FD1")

    Jump("loc_5019")

    label("loc_4FD6")


    #C0352
    ChrTalk(
        0xFE,
        "要来个气球吗～？\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "红、蓝、黄，还有绿色，\x01",
            "各种颜色都有哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5019")

    Jump("loc_515B")

    label("loc_501E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_502C")
    Jump("loc_515B")

    label("loc_502C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_515B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50AA")

    #C0354
    ChrTalk(
        0xFE,
        (
            "我被刚才冲过去的导力车吓了一跳，\x01",
            "手里的气球飞走好几个！\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "啊啊，好可惜……\x01",
            "飞回来吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_515B")

    label("loc_50AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5115")

    #C0356
    ChrTalk(
        0xFE,
        (
            "要来个气球吗～？\x01",
            "请让它陪伴您\x01",
            "游览克洛斯贝尔吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "一定可以给您\x01",
            "带来愉快的心情～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_515B")

    label("loc_5115")


    #C0358
    ChrTalk(
        0xFE,
        (
            "我的气球也会发给\x01",
            "游客之外的人～\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "如果想要，\x01",
            "随时可以和我说～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_515B")

    TalkEnd(0xFE)
    Return()

    # Function_10_48EA end

    def Function_11_515F(): pass

    label("Function_11_515F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_5170")
    Jump("loc_53B8")

    label("loc_5170")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_520A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51EA")

    #C0360
    ChrTalk(
        0x11,
        "#01203F咕呜呜呜……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，还真有\x01",
            "警犬的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x11,
        "#01200F咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5205")

    label("loc_51EA")


    #C0363
    ChrTalk(
        0x11,
        "#01200F咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_5205")

    Jump("loc_53B8")

    label("loc_520A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_521B")
    Jump("loc_53B8")

    label("loc_521B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5229")
    Jump("loc_53B8")

    label("loc_5229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_524A")
    Call(1, 23)
    Return()

    label("loc_524A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5396")

    #C0364
    ChrTalk(
        0x11,
        "#01203F咕呜呜呜…………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5337")

    #C0365
    ChrTalk(
        0x101,
        "#00005F嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x11,
        "#01200F…………嗷。\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x1A5,
        "#01100F它说没什么。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        (
            "#00006F是、是吗。\x02\x03",

            "#00000F好，今天也拜托你看家啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x1A5,
        "#01109F蔡特，我们走啦！\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x11,
        "#01200F嗷。\x02",
    )

    CloseMessageWindow()
    Jump("loc_538E")

    label("loc_5337")


    #C0371
    ChrTalk(
        0x101,
        (
            "#00003F（它好像还想说些什么……\x01",
            "  要是缇欧或琪雅在的话，\x01",
            "  就能听懂它的意思了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_538E")

    SetScenarioFlags(0x1, 1)
    Jump("loc_53B3")

    label("loc_5396")


    #C0372
    ChrTalk(
        0x11,
        "#01203F咕呜呜呜…………\x02",
    )

    CloseMessageWindow()

    label("loc_53B3")

    Jump("loc_53B8")

    label("loc_53B8")

    TalkEnd(0xFE)
    Return()

    # Function_11_515F end

    def Function_12_53BC(): pass

    label("Function_12_53BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5511")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54A8")

    #C0373
    ChrTalk(
        0xFE,
        (
            "罗伊德，虽然发生了很严重的事情，\x01",
            "但一定不能沮丧消沉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "至今为止，你们已经\x01",
            "成功跨越了多道难关，\x01",
            "这次也一定能将事件解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "我可以保证这一点，\x01",
            "拿出自信吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……\x01",
            "谢谢，凯特前辈。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_550C")

    label("loc_54A8")


    #C0377
    ChrTalk(
        0xFE,
        (
            "罗伊德，你们绝对可以\x01",
            "将这次的事件顺利解决的。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "拿出自信吧！\x01",
            "我们公共安全科也会继续努力的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_550C")

    Jump("loc_5DFB")

    label("loc_5511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_551F")
    Jump("loc_5DFB")

    label("loc_551F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_552D")
    Jump("loc_5DFB")

    label("loc_552D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_553B")
    Jump("loc_5DFB")

    label("loc_553B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_56AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5631")

    #C0379
    ChrTalk(
        0xFE,
        (
            "玛因兹遭到占领的事件\x01",
            "虽然使很多市民\x01",
            "受到打击……\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "但似乎也有不少人认为\x01",
            "与己无关。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "另外，在这起事件的影响下，\x01",
            "赞同独立的呼声\x01",
            "瞬间便高涨了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "总之，我们一定要\x01",
            "努力安抚大家的不安情绪，\x01",
            "避免发生骚乱。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_56A5")

    label("loc_5631")


    #C0383
    ChrTalk(
        0xFE,
        (
            "在市民之中，\x01",
            "似乎存在着各种各样的\x01",
            "疑惑与想法……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "总之，我们一定要\x01",
            "努力安抚大家的不安情绪，\x01",
            "避免发生骚乱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56A5")

    Jump("loc_5DFB")

    label("loc_56AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_572E")

    #C0385
    ChrTalk(
        0xFE,
        (
            "听说铁路总算赶在\x01",
            "今天早上修复了，\x01",
            "真是让人松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "如果铁路无法使用，\x01",
            "再赶上这种雨天，\x01",
            "就真是很麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFB")

    label("loc_572E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_57D1")

    #C0387
    ChrTalk(
        0xFE,
        (
            "竟然会发生脱轨事故……\x01",
            "又发生了很严重的事态啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "总之，一段时间内，\x01",
            "导力车的通行量肯定会比以往有所增加。\x01",
            "必须要提起精神，做好交通管理工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFB")

    label("loc_57D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5928")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D1")
    OP_93(0xFE, 0xB4, 0x0)

    #C0389
    ChrTalk(
        0xFE,
        "嘟嘟！嘟嘟！\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "请导力车缓慢行驶。\x01",
            "为了城市的安全，请各位多加协助！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    #C0391
    ChrTalk(
        0xFE,
        (
            "最近这段时间，\x01",
            "来自外国的导力车似乎有所减少。\x01",
            "这大概也是受了独立提案的影响吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "话虽如此，但还是不能\x01",
            "放松警惕，以免发生事故啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5923")

    label("loc_58D1")

    OP_93(0xFE, 0xB4, 0x0)

    #C0393
    ChrTalk(
        0xFE,
        "嘟嘟！嘟嘟！\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "请导力车缓慢行驶。\x01",
            "为了城市的安全，请各位多加协助！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5923")

    Jump("loc_5DFB")

    label("loc_5928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A9B")

    #C0395
    ChrTalk(
        0xFE,
        (
            "最近这段时间，\x01",
            "不遵守交通法规的人\x01",
            "又开始增多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "就算抛开交通法规不谈，\x01",
            "身为驾驶员，\x01",
            "也应该拥有基本的道德与礼节啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "每个人都曾在主日学校中接受过道德教育，\x01",
            "但成年之后却不能自觉遵守规章制度……\x01",
            "这真是很可悲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "你们在驾驶车辆的时候，\x01",
            "也一定要随时注意\x01",
            "附近的行人哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x109,
        "#10100F嗯，那当然！\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        "#00003F……我们一定牢记在心。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5B45")

    label("loc_5A9B")


    #C0401
    ChrTalk(
        0xFE,
        (
            "就算抛开交通法规不谈，\x01",
            "身为驾驶员，\x01",
            "也应该拥有基本的道德与礼节啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "每个人都曾在主日学校中接受过道德教育，\x01",
            "但成年之后却不能自觉遵守规章制度……\x01",
            "这真是很可悲呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B45")

    Jump("loc_5DFB")

    label("loc_5B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5BC7")

    #C0403
    ChrTalk(
        0xFE,
        (
            "据说很有可能会出现\x01",
            "恐怖分子……\x01",
            "绝对不能掉以轻心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "必须要保持最大警觉，\x01",
            "注意一切可疑的人物与状况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFB")

    label("loc_5BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5C44")

    #C0405
    ChrTalk(
        0xFE,
        (
            "我负责引导了各国首脑们\x01",
            "所乘坐的轿车……\x01",
            "真是很紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "透过导力车，似乎都可以\x01",
            "感受到他们的强大气场。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFB")

    label("loc_5C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5CEC")

    #C0407
    ChrTalk(
        0xFE,
        (
            "大概是因为我们\x01",
            "从今天开始在各处巡逻，\x01",
            "违规停车的数量有了明显减少。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "要是平时一直如此该多好……\x01",
            "算啦，不管怎么说，这是件好事，\x01",
            "还是不要发牢骚了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFB")

    label("loc_5CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5DF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D95")
    OP_93(0xFE, 0xB4, 0x0)

    #C0409
    ChrTalk(
        0xFE,
        (
            "嘟嘟！嘟嘟！\x01",
            "请导力车缓慢行驶～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    #C0410
    ChrTalk(
        0xFE,
        (
            "在下雨天，交通状况\x01",
            "会比平时拥堵一些。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        (
            "路面也比较滑，\x01",
            "所以要比平时更加小心哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5DED")

    label("loc_5D95")


    #C0412
    ChrTalk(
        0xFE,
        (
            "在下雨天，交通状况\x01",
            "会比平时拥堵一些。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "路面也比较滑，\x01",
            "所以要比平时更加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DED")

    Jump("loc_5DFB")

    label("loc_5DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5DFB")

    label("loc_5DFB")

    TalkEnd(0xFE)
    Return()

    # Function_12_53BC end

    def Function_13_5DFF(): pass

    label("Function_13_5DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F06")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E3B")
    Call(0, 104)
    Jump("loc_5E9A")

    label("loc_5E3B")

    TalkBegin(0xFE)

    #C0414
    ChrTalk(
        0xFE,
        (
            "黑色的运输车在不久前\x01",
            "往东街那边开去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "如果要追的话，\x01",
            "你们最好也\x01",
            "驾驶导力车。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_5E9A")

    Return()

    label("loc_5E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EA9")
    Call(1, 26)
    Return()

    label("loc_5EA9")

    TalkBegin(0xFE)

    #C0416
    ChrTalk(
        0xFE,
        (
            "那些猎兵……\x01",
            "为何要盗取\x01",
            "『克洛斯贝尔之钟』呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "……算了，想这些\x01",
            "也没什么用。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_5F06")

    Return()

    # Function_13_5DFF end

    def Function_14_5F07(): pass

    label("Function_14_5F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6045")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F43")
    Call(0, 104)
    Jump("loc_5F9A")

    label("loc_5F43")

    TalkBegin(0xFE)

    #C0418
    ChrTalk(
        0xFE,
        (
            "之前那辆运输车用不了多久\x01",
            "应该就能抵达唐古拉姆门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        "祝愿各位行动顺利！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_5F9A")

    Return()

    label("loc_5F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FA9")
    Call(1, 26)
    Return()

    label("loc_5FA9")

    TalkBegin(0xFE)

    #C0420
    ChrTalk(
        0xFE,
        (
            "对警备队而言，\x01",
            "与两大国之间的紧张状况\x01",
            "才是目前最重要的课题。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xFE,
        (
            "虽然也会搜寻『钟』的下落，\x01",
            "但只是在巡逻时顺便搜索而已。\x01",
            "事情毕竟有缓急之分嘛。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_6045")

    Return()

    # Function_14_5F07 end

    def Function_15_6046(): pass

    label("Function_15_6046")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6096")

    #C0422
    ChrTalk(
        0xFE,
        (
            "通商会议终于要进入高潮阶段了……\x01",
            "必须要更加集中精神才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6156")

    label("loc_6096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6104")

    #C0423
    ChrTalk(
        0xFE,
        (
            "各国首脑终于都已\x01",
            "进入克洛斯贝尔了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "不管怎么说，揭幕式顺利结束，\x01",
            "真是让人松一口气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6156")

    label("loc_6104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6156")

    #C0425
    ChrTalk(
        0xFE,
        (
            "市内巡逻任务预计持续到\x01",
            "通商会议的最终日。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        "必须要拿出干劲才行。\x02",
    )

    CloseMessageWindow()

    label("loc_6156")

    TalkEnd(0xFE)
    Return()

    # Function_15_6046 end

    def Function_16_615A(): pass

    label("Function_16_615A")

    TalkBegin(0xFE)

    #C0427
    ChrTalk(
        0xFE,
        (
            "建立『国防军』的目的并非『战斗』，\x01",
            "它是为了『守护』而存在的。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "我们与野蛮的帝国军、\x01",
            "共和国军是完全不同的。\x01",
            "所以请各位放心。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_615A end

    def Function_17_61E6(): pass

    label("Function_17_61E6")

    TalkBegin(0xFE)

    #C0429
    ChrTalk(
        0xFE,
        (
            "竟然夺走城市的象征……\x01",
            "真是让人气愤。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        "珍贵的古物就这样消失了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_61E6 end

    def Function_18_6236(): pass

    label("Function_18_6236")

    TalkBegin(0xFE)

    #C0431
    ChrTalk(
        0xFE,
        (
            "看来大钟消失不见的传闻\x01",
            "是真的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        (
            "武装集团吗……\x01",
            "他们的目的真是个谜啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_6236 end

    def Function_19_628F(): pass

    label("Function_19_628F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_636D")

    #C0433
    ChrTalk(
        0x12,
        "#01111F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x101,
        (
            "#00005F……琪雅？\x01",
            "为什么呆呆出神？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x0, 500)
    Sleep(300)

    #C0435
    ChrTalk(
        0x12,
        (
            "#01105F啊……没什么。\x02\x03",

            "#01109F大家今天要加油工作哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x101,
        "#00005F…………？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x159, 1)
    SetScenarioFlags(0x151, 6)
    Jump("loc_6390")

    label("loc_636D")


    #C0437
    ChrTalk(
        0x12,
        "#01109F大家今天要加油工作哦。\x02",
    )

    CloseMessageWindow()

    label("loc_6390")

    TalkEnd(0xFE)
    Return()

    # Function_19_628F end

    def Function_20_6394(): pass

    label("Function_20_6394")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63AE")
    Call(1, 23)
    Return()

    label("loc_63AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64CA")

    #C0438
    ChrTalk(
        0x104,
        "#00302F哟，柯贝，你还好吗～？\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x10,
        "喵～～\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x105,
        (
            "#10300F看样子，它似乎是\x01",
            "饿了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x109,
        (
            "#10109F我、我想\x01",
            "喂喂它！\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x102,
        (
            "#00100F柯贝很爱吃\x01",
            "『猫食』和我们\x01",
            "钓到的鱼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x101,
        (
            "#00004F嗯，我们现在带着那些吗……？\x02\x03",

            "#00000F总之，一定不要忘记\x01",
            "每天早上来喂食啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 3)
    TalkEnd(0xFE)
    Return()

    label("loc_64CA")

    ClearScenarioFlags(0x1, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_64D9")
    Call(1, 22)

    label("loc_64D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6542")

    #C0444
    ChrTalk(
        0x101,
        (
            "#00005F（说起来……\x01",
            "  身上正好带着钓来的鱼。）\x02\x03",

            "#00004F（喂给柯贝\x01",
            "  似乎不错呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13A, 0)

    label("loc_6542")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_656D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 1)), scpexpr(EXPR_END)), "loc_6568")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6568")

    Jump("loc_6670")

    label("loc_656D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_658E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 0)), scpexpr(EXPR_END)), "loc_6589")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6589")

    Jump("loc_6670")

    label("loc_658E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_65AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 7)), scpexpr(EXPR_END)), "loc_65AA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65AA")

    Jump("loc_6670")

    label("loc_65AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_65D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 6)), scpexpr(EXPR_END)), "loc_65CB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65CB")

    Jump("loc_6670")

    label("loc_65D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_65F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 5)), scpexpr(EXPR_END)), "loc_65EC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65EC")

    Jump("loc_6670")

    label("loc_65F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 4)), scpexpr(EXPR_END)), "loc_660D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_660D")

    Jump("loc_6670")

    label("loc_6612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6633")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 3)), scpexpr(EXPR_END)), "loc_662E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_662E")

    Jump("loc_6670")

    label("loc_6633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 2)), scpexpr(EXPR_END)), "loc_664F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_664F")

    Jump("loc_6670")

    label("loc_6654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 1)), scpexpr(EXPR_END)), "loc_6670")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AE0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_668D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7ADB")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "对话")
    MenuCmd(1, 1, "喂食")
    MenuCmd(1, 1, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66F3")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_66F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AA6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_672C")
    MenuCmd(1, 1, "斗鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_672C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_674B")
    MenuCmd(1, 1, "雪花蟹")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_674B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_676E")
    MenuCmd(1, 1, "蓝带神仙鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_676E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_678D")
    MenuCmd(1, 1, "银伞鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_678D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_67B4")
    MenuCmd(1, 1, "阿尔摩利卡鲫鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_67B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_67D1")
    MenuCmd(1, 1, "乌龟")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_67D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_67F0")
    MenuCmd(1, 1, "橙河鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_67F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_680F")
    MenuCmd(1, 1, "岩穴鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_680F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_682E")
    MenuCmd(1, 1, "虹鳟鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_682E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_684D")
    MenuCmd(1, 1, "食人鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_684D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_686A")
    MenuCmd(1, 1, "鲤鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_686A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_688B")
    MenuCmd(1, 1, "大口鲈鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_688B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_68A8")
    MenuCmd(1, 1, "黑鲑")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_68A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_68C7")
    MenuCmd(1, 1, "角斗鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_68C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_68E6")
    MenuCmd(1, 1, "冷水鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_68E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_6903")
    MenuCmd(1, 1, "小鲵")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6903")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6920")
    MenuCmd(1, 1, "鲑鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6920")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_693F")
    MenuCmd(1, 1, "金龙鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_693F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_695C")
    MenuCmd(1, 1, "鳗鲡")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_695C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_697B")
    MenuCmd(1, 1, "钢壳龟")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_697B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_699A")
    MenuCmd(1, 1, "巨血蟹")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_699A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_69BB")
    MenuCmd(1, 1, "珍珠龙鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_69BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_69D8")
    MenuCmd(1, 1, "巨鲶")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_69D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_69F5")
    MenuCmd(1, 1, "金鲑")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_69F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_END)), "loc_6A12")
    MenuCmd(1, 1, "大鲵")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_END)), "loc_6A2F")
    MenuCmd(1, 1, "锦鲤")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A2F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6A52")
    MenuCmd(1, 1, "翠耀神仙鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A52")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6A75")
    MenuCmd(1, 1, "琥耀岩穴鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A75")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6A98")
    MenuCmd(1, 1, "红耀食人鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A98")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6ABB")
    MenuCmd(1, 1, "苍耀巨龙鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6ABB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6ADE")
    MenuCmd(1, 1, "巨骨龙皇鱼")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6ADE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_6AFB")
    MenuCmd(1, 1, "猫食")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6AFB")

    MenuCmd(1, 1, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6B43")
    Jump("loc_7A97")

    label("loc_6B43")

    TalkEnd(0xFE)
    EventBegin(0x1)
    OP_4B(0x10, 0xFF)
    Fade(500)
    SetChrPos(0x10, -21980, 1300, -19300, 270)
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

    #C0445
    ChrTalk(
        0xFE,
        "喵喵……⊥\x02",
    )

    CloseMessageWindow()

    def lambda_6C0C():

        label("loc_6C0C")

        TurnDirection(0x0, 0x10, 0)
        Yield()
        Jump("loc_6C0C")

    QueueWorkItem2(0x0, 1, lambda_6C0C)

    def lambda_6C1E():

        label("loc_6C1E")

        TurnDirection(0x1, 0x10, 0)
        Yield()
        Jump("loc_6C1E")

    QueueWorkItem2(0x1, 1, lambda_6C1E)

    def lambda_6C30():

        label("loc_6C30")

        TurnDirection(0x2, 0x10, 0)
        Yield()
        Jump("loc_6C30")

    QueueWorkItem2(0x2, 1, lambda_6C30)

    def lambda_6C42():

        label("loc_6C42")

        TurnDirection(0x3, 0x10, 0)
        Yield()
        Jump("loc_6C42")

    QueueWorkItem2(0x3, 1, lambda_6C42)

    def lambda_6C54():

        label("loc_6C54")

        TurnDirection(0x4, 0x10, 0)
        Yield()
        Jump("loc_6C54")

    QueueWorkItem2(0x4, 1, lambda_6C54)

    def lambda_6C66():

        label("loc_6C66")

        TurnDirection(0x5, 0x10, 0)
        Yield()
        Jump("loc_6C66")

    QueueWorkItem2(0x5, 1, lambda_6C66)
    SetChrFlags(0x10, 0x8000)
    OP_93(0x10, 0x0, 0x1F4)
    Sleep(50)
    ClearChrFlags(0x10, 0x1)
    Sound(809, 0, 80, 0)

    def lambda_6C92():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x708, 0x1F40)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6C92)
    WaitChrThread(0x10, 1)
    Sound(809, 0, 80, 0)

    def lambda_6CB9():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1130, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6CB9)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 80, 0)

    def lambda_6CE0():
        OP_9D(0xFE, 0xFFFFA75E, 0x514, 0xFFFFDFBC, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6CE0)
    WaitChrThread(0x10, 1)
    Sleep(2000)
    OP_93(0x10, 0xB4, 0x1F4)
    Sound(809, 0, 80, 0)

    def lambda_6D11():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1194, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6D11)
    WaitChrThread(0x10, 1)
    Sound(809, 0, 80, 0)

    def lambda_6D38():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6D38)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 80, 0)

    def lambda_6D5F():
        OP_9D(0xFE, 0xFFFFAA24, 0x514, 0xFFFFB49C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6D5F)
    WaitChrThread(0x10, 1)
    SetChrFlags(0x10, 0x1)
    OP_93(0x10, 0x10E, 0x1F4)
    ClearChrFlags(0x10, 0x8000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x4, 0x1)
    EndChrThread(0x5, 0x1)

    #C0446
    ChrTalk(
        0xFE,
        "喵～\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6E25")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E1B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('斗鱼', 1)

    #A0447
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('ＥＰ１', 1)

    label("loc_6E1B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E25")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_6E6D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E63")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('雪花蟹', 1)

    #A0448
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '精神１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('精神１', 1)

    label("loc_6E63")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6EB5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EAB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('蓝带神仙鱼', 1)

    #A0449
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔防２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('魔防２', 1)

    label("loc_6EAB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EB5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6EFD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EF3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('银伞鱼', 1)

    #A0450
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('省ＥＰ１', 1)

    label("loc_6EF3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EFD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6F45")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F3B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('阿尔摩利卡鲫鱼', 1)

    #A0451
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '移动１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('移动１', 1)

    label("loc_6F3B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6F45")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_6F8D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F83")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('乌龟', 1)

    #A0452
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('命中１', 1)

    label("loc_6F83")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6F8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6FD5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FCB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('橙河鱼', 1)

    #A0453
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '恶戏'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('恶戏', 1)

    label("loc_6FCB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6FD5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_701D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7013")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('岩穴鱼', 1)

    #A0454
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('防御２', 1)

    label("loc_7013")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_701D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7065")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_705B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('虹鳟鱼', 1)

    #A0455
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '情报'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('情报', 1)

    label("loc_705B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7065")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_70AD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70A3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('食人鱼', 1)

    #A0456
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '暗之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('暗之刃', 1)

    label("loc_70A3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_70F5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70EB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鲤鱼', 1)

    #A0457
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('ＨＰ１', 1)

    label("loc_70EB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_713D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7133")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('大口鲈鱼', 1)

    #A0458
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('攻击１', 1)

    label("loc_7133")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_713D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_7185")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_717B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('黑鲑', 1)

    #A0459
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '混乱之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('混乱之刃', 1)

    label("loc_717B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7185")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_71CD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71C3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('角斗鱼', 1)

    #A0460
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '妨害１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('妨害１', 1)

    label("loc_71C3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_71CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7215")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_720B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('冷水鱼', 1)

    #A0461
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '丹精'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('丹精', 1)

    label("loc_720B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7215")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_725D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7253")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('小鲵', 1)

    #A0462
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('回避１', 1)

    label("loc_7253")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_725D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_72A5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_729B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鲑鱼', 1)

    #A0463
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '驱动１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('驱动１', 1)

    label("loc_729B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_72A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_72ED")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72E3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('金龙鱼', 1)

    #A0464
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '炎伤之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('炎伤之刃', 1)

    label("loc_72E3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_72ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_7335")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_732B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('鳗鲡', 1)

    #A0465
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '行动力１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('行动力１', 1)

    label("loc_732B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7335")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_737D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7373")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('钢壳龟', 1)

    #A0466
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '石化之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('石化之刃', 1)

    label("loc_7373")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_737D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_73C5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73BB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨血蟹', 1)

    #A0467
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('攻击３', 1)

    label("loc_73BB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_73C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_740D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7403")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('珍珠龙鱼', 1)

    #A0468
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('命中３', 1)

    label("loc_7403")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_740D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_7455")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_744B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨鲶', 1)

    #A0469
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('防御３', 1)

    label("loc_744B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7455")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_749D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7493")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('金鲑', 1)

    #A0470
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天眼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('天眼', 1)

    label("loc_7493")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_749D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_END)), "loc_74E5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74DB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('大鲵', 1)

    #A0471
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('ＨＰ３', 1)

    label("loc_74DB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_74E5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_END)), "loc_752D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7523")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('锦鲤', 1)

    #A0472
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '幸运'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('幸运', 1)

    label("loc_7523")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_752D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7575")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_756B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('翠耀神仙鱼', 1)

    #A0473
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '美臭'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('美臭', 1)

    label("loc_756B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7575")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_75BD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75B3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('琥耀岩穴鱼', 1)

    #A0474
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '虎威'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('虎威', 1)

    label("loc_75B3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_75BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7605")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75FB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('红耀食人鱼', 1)

    #A0475
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '龙眼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('龙眼', 1)

    label("loc_75FB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7605")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_764D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7643")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('苍耀巨龙鱼', 1)

    #A0476
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '治愈'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('治愈', 1)

    label("loc_7643")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_764D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7695")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_768B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('巨骨龙皇鱼', 1)

    #A0477
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '混乱之刃２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('混乱之刃２', 1)

    label("loc_768B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7695")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_76E1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76D7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('猫食', 1)

    #A0478
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽鱼肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×３收下了。\x02",
        )
    )

    AddItemNumber('魔兽鱼肉', 3)

    label("loc_76D7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_76E1")

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7708")
    SetScenarioFlags(0x13B, 1)
    Jump("loc_778B")

    label("loc_7708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7719")
    SetScenarioFlags(0x13B, 0)
    Jump("loc_778B")

    label("loc_7719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_772A")
    SetScenarioFlags(0x13A, 7)
    Jump("loc_778B")

    label("loc_772A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_773B")
    SetScenarioFlags(0x13A, 6)
    Jump("loc_778B")

    label("loc_773B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_774C")
    SetScenarioFlags(0x13A, 5)
    Jump("loc_778B")

    label("loc_774C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_775D")
    SetScenarioFlags(0x13A, 4)
    Jump("loc_778B")

    label("loc_775D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_776E")
    SetScenarioFlags(0x13A, 3)
    Jump("loc_778B")

    label("loc_776E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_777F")
    SetScenarioFlags(0x13A, 2)
    Jump("loc_778B")

    label("loc_777F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_778B")
    SetScenarioFlags(0x13A, 1)

    label("loc_778B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 1)), scpexpr(EXPR_END)), "loc_77A8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_77A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 2)), scpexpr(EXPR_END)), "loc_77BB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_77BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 3)), scpexpr(EXPR_END)), "loc_77CE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_77CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 4)), scpexpr(EXPR_END)), "loc_77E1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_77E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 5)), scpexpr(EXPR_END)), "loc_77F4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_77F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 6)), scpexpr(EXPR_END)), "loc_7807")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 7)), scpexpr(EXPR_END)), "loc_781A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_781A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 0)), scpexpr(EXPR_END)), "loc_782D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_782D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 1)), scpexpr(EXPR_END)), "loc_7840")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7840")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7904")

    #C0479
    ChrTalk(
        0xFE,
        "喵喵喵～喵……¤\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('灵猫', 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78BD")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0480
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '灵猫'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('灵猫', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7904")

    label("loc_78BD")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0481
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '银耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('银耀珠', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7904")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7943")

    #C0482
    ChrTalk(
        0x102,
        "#00105F啊……要把这个给我吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A65")

    label("loc_7943")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7973")

    #C0483
    ChrTalk(
        0x103,
        "#00205F要把这个给我吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A65")

    label("loc_7973")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79A1")

    #C0484
    ChrTalk(
        0x104,
        "#00305F要把这个给我？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A65")

    label("loc_79A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79D3")

    #C0485
    ChrTalk(
        0x109,
        "#10105F哎，要把这个给我？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A65")

    label("loc_79D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A07")

    #C0486
    ChrTalk(
        0x105,
        "#10305F哦，要把这个给我吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A65")

    label("loc_7A07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A3E")

    #C0487
    ChrTalk(
        0x106,
        (
            "#10705F那个……\x01",
            "我可以收下吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A65")

    label("loc_7A3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A65")

    #C0488
    ChrTalk(
        0x10A,
        "#00605F要给我这个？\x02",
    )

    CloseMessageWindow()

    label("loc_7A65")


    #C0489
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，谢啦，\x01",
            "我们会好好使用的。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    EventEnd(0x4)
    Return()

    label("loc_7A97")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AD6")

    label("loc_7AA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7ABA")
    Jump("loc_7AD6")

    label("loc_7ABA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AD6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 21)

    label("loc_7AD6")

    Jump("loc_668D")

    label("loc_7ADB")

    Jump("loc_7AE3")

    label("loc_7AE0")

    Call(1, 21)

    label("loc_7AE3")

    TalkEnd(0xFE)
    Return()

    # Function_20_6394 end

    def Function_21_7AE7(): pass

    label("Function_21_7AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B72")

    #C0490
    ChrTalk(
        0x10,
        "喵……？\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x103,
        (
            "#00203F柯贝，暂时就靠你\x01",
            "留下看家啦。\x02\x03",

            "#00200F我们一定会把琪雅\x01",
            "带回这里的。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x10,
        "……喵呜呜～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7B84")

    label("loc_7B72")


    #C0493
    ChrTalk(
        0x10,
        "……喵呜呜～\x02",
    )

    CloseMessageWindow()

    label("loc_7B84")

    Jump("loc_7F6C")

    label("loc_7B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7B97")
    Jump("loc_7F6C")

    label("loc_7B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7BBB")

    #C0494
    ChrTalk(
        0x10,
        "呼喵喵～～咕……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F6C")

    label("loc_7BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7BD9")

    #C0495
    ChrTalk(
        0x10,
        "喵喔喔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F6C")

    label("loc_7BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7BF7")

    #C0496
    ChrTalk(
        0x10,
        "喵呜……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F6C")

    label("loc_7BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7C05")
    Jump("loc_7F6C")

    label("loc_7C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7C27")

    #C0497
    ChrTalk(
        0x10,
        "喵呀～～嗝……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F6C")

    label("loc_7C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7C45")

    #C0498
    ChrTalk(
        0x10,
        "喵喔喔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F6C")

    label("loc_7C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7C67")

    #C0499
    ChrTalk(
        0x10,
        "喵呀～～嗝……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F6C")

    label("loc_7C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7CF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CE3")

    #C0500
    ChrTalk(
        0x10,
        "喵。\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x103,
        (
            "#00202F呵呵……\x01",
            "好久不见了，柯贝。\x02\x03",

            "从今天开始，\x01",
            "我也来喂你了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x10,
        "喵呜呜～⊥\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7CF3")

    label("loc_7CE3")


    #C0503
    ChrTalk(
        0x10,
        "喵呜呜～⊥\x02",
    )

    CloseMessageWindow()

    label("loc_7CF3")

    Jump("loc_7F6C")

    label("loc_7CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7DD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DBD")

    #C0504
    ChrTalk(
        0x10,
        "喵呜。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x10A,
        (
            "#00600F在支援科养的猫啊。\x02\x03",

            "#00603F（抚摸……）\x01",
            "……你真是挑了个\x01",
            "很麻烦的住所啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x10,
        "喵噢～～喵……⊥\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#00002F（没想到达德利警官\x01",
            "  很会哄猫啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7DCB")

    label("loc_7DBD")


    #C0508
    ChrTalk(
        0x10,
        "喵噢……\x02",
    )

    CloseMessageWindow()

    label("loc_7DCB")

    Jump("loc_7F6C")

    label("loc_7DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_7DE8")

    #C0509
    ChrTalk(
        0x10,
        "喵？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F6C")

    label("loc_7DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7E06")

    #C0510
    ChrTalk(
        0x10,
        "喵喔喔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F6C")

    label("loc_7E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7E20")

    #C0511
    ChrTalk(
        0x10,
        "喵～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F6C")

    label("loc_7E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7E2E")
    Jump("loc_7F6C")

    label("loc_7E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7F6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F5C")

    #C0512
    ChrTalk(
        0x101,
        (
            "#00005F对了，\x01",
            "还要给柯贝喂食呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x10,
        "喵？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EA3")

    #C0514
    ChrTalk(
        0x1A5,
        "#01100F它说现在很饱了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7ED1")

    label("loc_7EA3")


    #C0515
    ChrTalk(
        0x105,
        (
            "#10300F不过，它看起来\x01",
            "似乎已经很饱了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7ED1")


    #C0516
    ChrTalk(
        0x102,
        (
            "#00100F科长出门之前，\x01",
            "好像刚给它喂过食。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x109,
        "#10106F呜呜，真遗憾。\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，算啦，如果以后钓到鱼，\x01",
            "就带过来喂它吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13B, 2)
    Jump("loc_7F6C")

    label("loc_7F5C")


    #C0519
    ChrTalk(
        0x10,
        "喵噢噢～⊥\x02",
    )

    CloseMessageWindow()

    label("loc_7F6C")

    Return()

    # Function_21_7AE7 end

    def Function_22_7F6D(): pass

    label("Function_22_7F6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7F7B")
    SetScenarioFlags(0x1, 3)

    label("loc_7F7B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_7F89")
    SetScenarioFlags(0x1, 3)

    label("loc_7F89")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7F97")
    SetScenarioFlags(0x1, 3)

    label("loc_7F97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7FA5")
    SetScenarioFlags(0x1, 3)

    label("loc_7FA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7FB3")
    SetScenarioFlags(0x1, 3)

    label("loc_7FB3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_7FC1")
    SetScenarioFlags(0x1, 3)

    label("loc_7FC1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7FCF")
    SetScenarioFlags(0x1, 3)

    label("loc_7FCF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7FDD")
    SetScenarioFlags(0x1, 3)

    label("loc_7FDD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7FEB")
    SetScenarioFlags(0x1, 3)

    label("loc_7FEB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_7FF9")
    SetScenarioFlags(0x1, 3)

    label("loc_7FF9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8007")
    SetScenarioFlags(0x1, 3)

    label("loc_8007")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8015")
    SetScenarioFlags(0x1, 3)

    label("loc_8015")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_8023")
    SetScenarioFlags(0x1, 3)

    label("loc_8023")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8031")
    SetScenarioFlags(0x1, 3)

    label("loc_8031")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_803F")
    SetScenarioFlags(0x1, 3)

    label("loc_803F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_804D")
    SetScenarioFlags(0x1, 3)

    label("loc_804D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_805B")
    SetScenarioFlags(0x1, 3)

    label("loc_805B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8069")
    SetScenarioFlags(0x1, 3)

    label("loc_8069")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_8077")
    SetScenarioFlags(0x1, 3)

    label("loc_8077")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_8085")
    SetScenarioFlags(0x1, 3)

    label("loc_8085")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_8093")
    SetScenarioFlags(0x1, 3)

    label("loc_8093")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_80A1")
    SetScenarioFlags(0x1, 3)

    label("loc_80A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_80AF")
    SetScenarioFlags(0x1, 3)

    label("loc_80AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_END)), "loc_80BD")
    SetScenarioFlags(0x1, 3)

    label("loc_80BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大鲵', 0x0)"), scpexpr(EXPR_END)), "loc_80CB")
    SetScenarioFlags(0x1, 3)

    label("loc_80CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('锦鲤', 0x0)"), scpexpr(EXPR_END)), "loc_80D9")
    SetScenarioFlags(0x1, 3)

    label("loc_80D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠耀神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_80E7")
    SetScenarioFlags(0x1, 3)

    label("loc_80E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥耀岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_80F5")
    SetScenarioFlags(0x1, 3)

    label("loc_80F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('红耀食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8103")
    SetScenarioFlags(0x1, 3)

    label("loc_8103")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('苍耀巨龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_8111")
    SetScenarioFlags(0x1, 3)

    label("loc_8111")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨骨龙皇鱼', 0x0)"), scpexpr(EXPR_END)), "loc_811F")
    SetScenarioFlags(0x1, 3)

    label("loc_811F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_812D")
    SetScenarioFlags(0x1, 3)

    label("loc_812D")

    Return()

    # Function_22_7F6D end

    def Function_23_812E(): pass

    label("Function_23_812E")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    SetChrPos(0x101, -25020, 1300, -19860, 90)
    SetChrPos(0x102, -25130, 1300, -18930, 90)
    SetChrPos(0x109, -26200, 1300, -19870, 90)
    SetChrPos(0x105, -26790, 1300, -19180, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81A9")
    SetChrPos(0x1A5, -24820, 1300, -16830, 133)

    label("loc_81A9")

    OP_68(-24880, 3000, -20830, 0)
    MoveCamera(43, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10510, 0)
    OP_0D()

    #C0520
    ChrTalk(
        0x11,
        "#01200F咕呜呜呜呜……\x02",
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x101,
        (
            "#6P#00000F蔡特，柯贝，\x01",
            "你们在一起啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x102,
        "#00102F哈，关系还是这么亲密。\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，是特别任务支援科\x01",
            "饲养的警犬啊。\x02\x03",

            "#10300F今后也请多多关照哦，蔡特。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x11,
        "#01203F咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_83C5")

    #C0525
    ChrTalk(
        0x1A5,
        (
            "#01104F它说『并不是什么饲养，\x01",
            "而是我在照顾他们』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0526
    ChrTalk(
        0x105,
        "#6P#10309F啊哈哈，我真是失言了。\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x101,
        (
            "#00006F是、是啊……\x01",
            "蔡特的确是经常帮助我们。\x01",
            "不过，它还是这么傲气啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8425")

    label("loc_83C5")


    #C0528
    ChrTalk(
        0x101,
        (
            "#00005F它好像是\x01",
            "有什么话想说……\x02\x03",

            "#00003F唔……要是缇欧或琪雅在的话，\x01",
            "就能明白它的意思了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8425")

    TurnDirection(0x109, 0x10, 500)

    #C0529
    ChrTalk(
        0x109,
        (
            "#6P#10102F我虽然有些怕狗，\x01",
            "但是和蔡特已经很熟了。\x02\x03",

            "#10105F这只黑猫又是……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10, 500)

    #C0530
    ChrTalk(
        0x101,
        (
            "#6P#00000F哦，它叫柯贝。\x02\x03",

            "在克洛斯贝尔通讯社\x01",
            "搬离这座大楼之前，\x01",
            "它好像就已经住在这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x10,
        "#11P喵。\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x109,
        (
            "#6P#10102F呵呵，真可爱。\x02\x03",

            "#10109F哈，以后可以在支援科\x01",
            "和猫咪亲密接触了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x102,
        (
            "#00109F诺艾尔小姐很喜欢猫吧。\x01",
            "呵呵，今后一定会很愉快啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x10,
        "#11P喵噢噢……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24690, 1300, -19050, 90)
    SetScenarioFlags(0x139, 7)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0xB4, 0x0)
    OP_4C(0x11, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_23_812E end

    def Function_24_85BC(): pass

    label("Function_24_85BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85F3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_85F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85F3")
    Call(1, 26)
    Return()

    label("loc_85F3")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0535
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "       『克洛斯贝尔之钟』\x01",
            "Ｓ１１８５，在克洛斯贝尔自治州\x01",
            "发掘出土的巨型大钟。\x01",
            "依据出土遗迹的情况来看，\x01",
            "可推断为中世纪时期的物品。\x01",
            "使用多种金属打造而成，\x01",
            "敲打时会发出悦耳的低音。\x02",
        )
    )

    CloseMessageWindow()

    #A0536
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "据推测，是由当时的权贵人士所制造，\x01",
            "但关于其具体用途，\x01",
            "目前仍然诸说纷纭。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_85BC end

    def Function_25_872D(): pass

    label("Function_25_872D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B5C")

    #C0537
    ChrTalk(
        0x1A2,
        (
            "基隆德武器商会……\x01",
            "原来如此，这里是一家合法的武器店啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x1A2,
        "好，那就进去看看吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_87EF")

    def lambda_87BF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_87BF)
    Sleep(50)

    def lambda_87CF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_87CF)
    Sleep(50)

    def lambda_87DF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_87DF)
    Sleep(300)
    Jump("loc_8866")

    label("loc_87EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_882D")

    def lambda_87FD():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_87FD)
    Sleep(50)

    def lambda_880D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_880D)
    Sleep(50)

    def lambda_881D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_881D)
    Sleep(300)
    Jump("loc_8866")

    label("loc_882D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_8866")

    def lambda_883B():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_883B)
    Sleep(50)

    def lambda_884B():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_884B)
    Sleep(50)

    def lambda_885B():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_885B)
    Sleep(300)

    label("loc_8866")


    #C0539
    ChrTalk(
        0x101,
        (
            "#00003F抱歉，秦。\x01",
            "正如你所说，这里是武器店。\x02\x03",

            "#00001F里面有不少危险的商品，\x01",
            "所以实在是不能带你进这种地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x1A2,
        (
            "哼，只要不触碰\x01",
            "那些商品就行了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x1A2,
        (
            "我对这个地方很有兴趣，\x01",
            "说进去就要进去。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0542
    ChrTalk(
        0x101,
        (
            "#00006F（呼……\x01",
            "  艾莉，拜托你了。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0543
    ChrTalk(
        0x102,
        "#00100F（呵呵，明白了。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0544
    ChrTalk(
        0x102,
        (
            "#00103F秦，你可是我们\x01",
            "最最重要的保护对象哦。\x02\x03",

            "所以说，\x01",
            "哪怕只有万分之一的可能性，\x01",
            "我们也必须要避免危险。\x02\x03",

            "#00100F秦这么聪明，\x01",
            "想必能理解这一点吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x1A2,
        (
            "唔……\x01",
            "理解倒是可以理解啦……\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x102,
        (
            "#00109F呵呵，太好了，\x01",
            "秦果然聪明啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x1A2,
        (
            "是、是的……\x01",
            "我一向都很聪明的！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_8ADA")

    #C0548
    ChrTalk(
        0x104,
        "#00309F（哈哈，大小姐的效果就是强大啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B54")

    label("loc_8ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_8B1E")

    #C0549
    ChrTalk(
        0x109,
        (
            "#10109F（啊哈哈，\x01",
            "  艾莉小姐的效果就是强大啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B54")

    label("loc_8B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_8B54")

    #C0550
    ChrTalk(
        0x105,
        "#10302F（呵呵，艾莉的效果就是强大啊。）\x02",
    )

    CloseMessageWindow()

    label("loc_8B54")

    SetScenarioFlags(0x1DC, 7)
    Jump("loc_8B90")

    label("loc_8B5C")


    #C0551
    ChrTalk(
        0x101,
        (
            "#00000F我们现在还带着秦，\x01",
            "不要进入武器商会了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B90")

    TalkEnd(0xFF)
    Return()

    # Function_25_872D end

    def Function_26_8B94(): pass

    label("Function_26_8B94")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x14, 0x0)
    OP_4B(0x15, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 150, 0, -3900, 0)
    SetChrPos(0x109, 1330, 0, -4640, 0)
    SetChrPos(0x102, 2590, 0, -3300, 315)
    SetChrPos(0x103, -1610, 0, -4590, 0)
    SetChrPos(0x105, -900, 0, -5970, 0)
    SetChrPos(0x104, 740, 0, -6130, 0)
    OP_68(-1190, 1900, -5280, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(11710, 0)
    SetChrFlags(0xF, 0x8)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_8E74")

    #C0552
    ChrTalk(
        0x14,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x15,
        (
            "特别任务支援科的各位，\x01",
            "还有诺艾尔上士，你们辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x109,
        "#10100F你也辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x14,
        (
            "对了，刚才的工作\x01",
            "已经解决了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8D75")

    #C0556
    ChrTalk(
        0x101,
        (
            "#00002F#2P嗯，已经解决了。\x01",
            "多亏你的帮忙，谢了，弗兰茨。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x14,
        (
            "哈哈，虽然不清楚是怎么回事，\x01",
            "但能帮上忙，真是我的荣幸啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E12")

    label("loc_8D75")


    #C0558
    ChrTalk(
        0x101,
        (
            "#00003F#2P啊……嗯……刚刚结束。\x02\x03",

            "#00006F（都怪我们无视弗兰茨说的话，\x01",
            "  才让诈骗犯逃脱……）\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x14,
        (
            "哈哈，虽然不清楚是怎么回事，\x01",
            "但事情能告一段落就好啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E12")


    #C0560
    ChrTalk(
        0x101,
        (
            "#00005F#2P对了，弗兰茨，\x01",
            "你今天负责在这里\x01",
            "警备吗？\x02\x03",

            "平时都是由凯特前辈\x01",
            "负责这片区域啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F3C")

    label("loc_8E74")


    #C0561
    ChrTalk(
        0x14,
        "呀，这不是罗伊德和各位吗。\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x15,
        (
            "特别任务支援科的各位，\x01",
            "还有诺艾尔上士，你们辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x109,
        "#10100F你也辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x101,
        (
            "#00005F#2P弗兰茨，\x01",
            "你今天负责在这里警备吗？\x02\x03",

            "平时都是由凯特前辈\x01",
            "负责这片区域啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F3C")


    #C0565
    ChrTalk(
        0x14,
        (
            "哦，前辈还有其它事情，\x01",
            "去别的地方了。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x14,
        (
            "所以由我临时负责\x01",
            "这一带的警备工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-2320, 2800, -900, 2000)
    MoveCamera(45, 8, 0, 2000)
    OP_6E(660, 2000)
    SetCameraDistance(15930, 2000)
    Sleep(2500)

    #C0567
    ChrTalk(
        0x102,
        (
            "#12P#00108F『克洛斯贝尔之钟』……\x01",
            "被赤色星座\x01",
            "盗走了呢。\x02\x03",

            "#00101F这一带的警备力度有所加强，\x01",
            "也是由于这个缘故吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x15,
        (
            "再怎么说，被盗走的毕竟是\x01",
            "克洛斯贝尔的重要文物。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x15,
        (
            "谨慎起见，我从警备队\x01",
            "赶到这里支援了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1190, 1900, -5280, 2000)
    MoveCamera(45, 21, 0, 2000)
    OP_6E(660, 2000)
    SetCameraDistance(11710, 2000)
    Sleep(2500)

    #C0570
    ChrTalk(
        0x103,
        (
            "#00206F#3P他们盗取大钟的目的，\x01",
            "还有大钟的去向，\x01",
            "现在都还不清楚吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x14,
        (
            "嗯，警察局和警备队\x01",
            "虽然展开了搜索，\x01",
            "但却毫无发现。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x104,
        (
            "#00303F#4P叔叔他们……\x01",
            "到底有什么\x01",
            "企图呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x105,
        (
            "#10300F#4P呵呵，那么大的东西，\x01",
            "想带走也很麻烦吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x101,
        (
            "#00003F#2P……总之，\x01",
            "『钟』的事情就交给相关人员来处理，\x01",
            "我们专心做好我们该做的工作吧。\x02\x03",

            "#00000F弗兰茨，我们就先告辞了，\x01",
            "市内警备的工作要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x14,
        "嗯，再见啦。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x14, 0x0)
    OP_4C(0x15, 0x0)
    ClearChrFlags(0xF, 0x8)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 150, 0, -3900, 0)
    SetScenarioFlags(0x190, 4)
    EventEnd(0x5)
    Return()

    # Function_26_8B94 end

    SaveToFile()

Try(main)
