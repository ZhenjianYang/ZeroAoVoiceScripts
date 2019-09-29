from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t0600.bin",                # FileName
        "t0600",                    # MapName
        "t0600",                    # Location
        0x0069,                     # MapIndex
        "ed7301",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x20,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 105, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0600",                  # 0
        "霍夫曼矿山长",           # 1
        "矿工玛尔罗",             # 2
        "矿工冈兹",               # 3
        "矿工罗基",               # 4
        "矿工马库斯",             # 5
        "亚雷库",                 # 6
    ))

    AddCharChip((
        "chr/ch26300.itc",                   # 00
        "chr/ch26200.itc",                   # 01
        "chr/ch30700.itc",                   # 02
        "chr/ch23000.itc",                   # 03
    ))

    DeclNpc(-31850,  0,       32080,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4139,    0,       6690,    90,   261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-11470,  0,       15090,   19,   261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-17250,  50,      30370,   180,  261,  0x0, 0,   1,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(-28860,  0,       56150,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)

    DeclActor(132500,  0,       18000,   1200,    132500,  1750,    18000,   0x007C, 0,  4,  0x0000)
    DeclActor(-22540,  0,       54760,   1200,    -22540,  1500,    54760,   0x007C, 0,  11, 0x0000)

    ChipFrameInfo(452, 0)                                        # 0

    ScpFunction((
        "Function_0_1C4",          # 00, 0
        "Function_1_27C",          # 01, 1
        "Function_2_2A7",          # 02, 2
        "Function_3_38F",          # 03, 3
        "Function_4_3AD",          # 04, 4
        "Function_5_453",          # 05, 5
        "Function_6_D37",          # 06, 6
        "Function_7_1515",         # 07, 7
        "Function_8_19C7",         # 08, 8
        "Function_9_2238",         # 09, 9
        "Function_10_290B",        # 0A, 10
        "Function_11_2A50",        # 0B, 11
    ))


    def Function_0_1C4(): pass

    label("Function_0_1C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_204"),
        (1, "loc_210"),
        (2, "loc_21C"),
        (3, "loc_228"),
        (4, "loc_234"),
        (5, "loc_240"),
        (6, "loc_24C"),
        (SWITCH_DEFAULT, "loc_258"),
    )


    label("loc_204")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_210")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_21C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_228")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_234")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_240")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_24C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_258")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_264")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_27B")

    Return()

    # Function_0_1C4 end

    def Function_1_27C(): pass

    label("Function_1_27C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A6")
    OP_94(0xFE, 0xFFFFA7FE, 0x7F4E, 0xFFFFC3B0, 0x6AA4, 0x3E8)
    Sleep(300)
    Jump("Function_1_27C")

    label("loc_2A6")

    Return()

    # Function_1_27C end

    def Function_2_2A7(): pass

    label("Function_2_2A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2B5")
    Jump("loc_38E")

    label("loc_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2C3")
    Jump("loc_38E")

    label("loc_2C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2D1")
    Jump("loc_38E")

    label("loc_2D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DF")
    Jump("loc_38E")

    label("loc_2DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2ED")
    Jump("loc_38E")

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2FB")
    Jump("loc_38E")

    label("loc_2FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30E")
    SetChrFlags(0xA, 0x80)
    Jump("loc_38E")

    label("loc_30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31C")
    Jump("loc_38E")

    label("loc_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_343")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_38E")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36C")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -400, 50, 3770, 0)
    Jump("loc_38E")

    label("loc_36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_38E")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E")
    SetChrFlags(0xC, 0x10)

    label("loc_38E")

    Return()

    # Function_2_2A7 end

    def Function_3_38F(): pass

    label("Function_3_38F")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -22700, 0, 54850, 10000, 2000, 45000)
    Return()

    # Function_3_38F end

    def Function_4_3AD(): pass

    label("Function_4_3AD")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着车辆杂志《导力车爱好者vol.1》。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36E, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44F")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "导力车喷漆式样\x01\x07\x02",

            "『魅力色彩』\x07\x00",
            "已经记下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36E, 1)

    label("loc_44F")

    TalkEnd(0xFF)
    Return()

    # Function_4_3AD end

    def Function_5_453(): pass

    label("Function_5_453")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_515")

    #C0003
    ChrTalk(
        0xFE,
        (
            "和镇长商量了一下，\x01",
            "决定重新开放矿山。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "玛因兹如果想向前走，\x01",
            "矿山显然是不可缺少的……\x01",
            "我是这样想的。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "……嘿嘿，已经好久没有挖矿了，\x01",
            "一定要拼命努力！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_542")

    label("loc_515")


    #C0006
    ChrTalk(
        0xFE,
        (
            "已经好久没有挖矿了，\x01",
            "一定要拼命努力！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_542")

    Jump("loc_D33")

    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_555")
    Jump("loc_D33")

    label("loc_555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_563")
    Jump("loc_D33")

    label("loc_563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A")

    #C0007
    ChrTalk(
        0xFE,
        (
            "玛因兹被占领的时候，\x01",
            "我们发起了反击，\x01",
            "希望能将那些猎兵赶走……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "但刚一交手，\x01",
            "就被他们轻松打倒了，\x01",
            "腰到现在还有些疼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "虽然没有受重伤，\x01",
            "但米兰达还是大发雷霆，\x01",
            "怪我太过莽撞。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6B4")

    label("loc_63A")


    #C0010
    ChrTalk(
        0xFE,
        (
            "虽然腰到现在还有些疼，\x01",
            "但我完全不后悔\x01",
            "奋起反抗的做法。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "不管怎么说，其他矿工\x01",
            "和镇上的各位都没受伤，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B4")

    Jump("loc_D33")

    label("loc_6B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_867")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DF")

    #C0012
    ChrTalk(
        0xFE,
        (
            "在矿山，难免会遇到塌方事故，\x01",
            "有时还会出现魔兽，\x01",
            "矿工的工作就是在拼命。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "如果想把这样的工作做下去，\x01",
            "彼此信赖，并对这份工作\x01",
            "充满自豪是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "矿工们最近非常团结，\x01",
            "看来他们也明白\x01",
            "这一点了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "嘿嘿，能与这样的同伴们共事，\x01",
            "我这个矿山长真是太幸福了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_862")

    label("loc_7DF")


    #C0016
    ChrTalk(
        0xFE,
        (
            "从某种意义上说，\x01",
            "做矿工其实就是在搏命，\x01",
            "所以互相信赖是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "嘿嘿，能与这样的同伴们共事，\x01",
            "我这个矿山长真是太幸福了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_862")

    Jump("loc_D33")

    label("loc_867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91F")

    #C0018
    ChrTalk(
        0xFE,
        (
            "玛尔罗那小子，\x01",
            "今天异常地有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "昨天还是一副世界末日就要到来的表情呢，\x01",
            "这到底是怎么回事……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "算啦，只要他能努力工作，\x01",
            "我就没什么好说的了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9AA")

    label("loc_91F")


    #C0021
    ChrTalk(
        0xFE,
        (
            "玛尔罗那小子突然变得那么有精神，\x01",
            "和昨天相比，简直就像变了个人一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "唔，真是搞不懂啊……\x01",
            "只要他能努力工作，\x01",
            "我就没什么好说的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AA")

    Jump("loc_D33")

    label("loc_9AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A48")

    #C0023
    ChrTalk(
        0xFE,
        (
            "玛尔罗那小子，\x01",
            "最近好像总是\x01",
            "无法集中精神工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "我想请他喝一杯，让他转换一下心情，\x01",
            "结果也被拒绝了……\x01",
            "到底是怎么了？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A9E")

    label("loc_A48")


    #C0025
    ChrTalk(
        0xFE,
        (
            "说起来，冈兹那小子\x01",
            "这休息时间也太长了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "真是的，一个一个的\x01",
            "全都这么懒散。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9E")

    Jump("loc_D33")

    label("loc_AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1B")

    #C0027
    ChrTalk(
        0xFE,
        (
            "今天好像是亚雷库学习\x01",
            "主日学校课程的日子。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "希望贝卡莱先生家的\x01",
            "奇米也一起\x01",
            "认真学习。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B69")

    label("loc_B1B")


    #C0029
    ChrTalk(
        0xFE,
        (
            "我们这些矿工全都是\x01",
            "没上过学的大老粗。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "希望亚雷库他们\x01",
            "能多学点知识。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B69")

    Jump("loc_D33")

    label("loc_B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B7C")
    Jump("loc_D33")

    label("loc_B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C00")

    #C0031
    ChrTalk(
        0xFE,
        "（咕噜噜……）\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "……啊，不好，\x01",
            "好像忘了\x01",
            "带盒饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "把手头的工作完成之后，\x01",
            "回家去取一趟吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C58")

    label("loc_C00")


    #C0034
    ChrTalk(
        0xFE,
        (
            "出门时把带盒饭的事情\x01",
            "忘得一干二净。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "把手头的工作完成之后，\x01",
            "回家去取一趟吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C58")

    Jump("loc_D33")

    label("loc_C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_D33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF0")

    #C0036
    ChrTalk(
        0xFE,
        (
            "虽然很在意旧矿山的事情……\x01",
            "但身为矿工，还是要专心挖矿。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "那边的事情就交给冈兹和镇长吧，\x01",
            "我们必须集中精神工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D33")

    label("loc_CF0")


    #C0038
    ChrTalk(
        0xFE,
        (
            "身为矿工，就要专心挖矿。\x01",
            "无论发生什么情况都必须集中精神工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D33")

    TalkEnd(0xFE)
    Return()

    # Function_5_453 end

    def Function_6_D37(): pass

    label("Function_6_D37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD7")

    #C0039
    ChrTalk(
        0xFE,
        (
            "虽然发生了异常事态……\x01",
            "但我们必须竭尽全力，\x01",
            "让玛因兹更加繁荣。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "哈哈，只要努力下去，\x01",
            "说不定琉卡小姐\x01",
            "有朝一日就会看上我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E1B")

    label("loc_DD7")


    #C0041
    ChrTalk(
        0xFE,
        (
            "虽然发生了异常事态……\x01",
            "但我们必须竭尽全力，\x01",
            "让玛因兹更加繁荣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1B")

    Jump("loc_1511")

    label("loc_E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_E2E")
    Jump("loc_1511")

    label("loc_E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_E3C")
    Jump("loc_1511")

    label("loc_E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F07")

    #C0042
    ChrTalk(
        0xFE,
        (
            "玛因兹矿山总算从昨天开始\x01",
            "重新开放，今后可以继续采矿了。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "虽然想了很多关于\x01",
            "克洛斯贝尔今后局势的问题……\x01",
            "但现在最重要的还是工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "我们这些矿工能做的\x01",
            "也只有挖矿了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F7B")

    label("loc_F07")


    #C0045
    ChrTalk(
        0xFE,
        (
            "在矿山镇被占领时，\x01",
            "酒馆的琉卡小姐\x01",
            "好像相当害怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "虽然我除了挖矿\x01",
            "什么都不会……\x01",
            "但真希望她能早日恢复精神。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F7B")

    Jump("loc_1511")

    label("loc_F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_FE6")

    #C0047
    ChrTalk(
        0xFE,
        (
            "多亏冈兹，\x01",
            "我总算可以集中精神\x01",
            "工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "作为答谢，\x01",
            "他今晚的酒钱\x01",
            "就由我来出吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1511")

    label("loc_FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_10ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1086")

    #C0049
    ChrTalk(
        0xFE,
        (
            "冈兹昨天把我\x01",
            "硬拉到了酒馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "之后，琉卡小姐\x01",
            "鼓励了最近一直\x01",
            "无精打采的我。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "呼，看来我并没有\x01",
            "被她讨厌呢……\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_10E8")

    label("loc_1086")


    #C0052
    ChrTalk(
        0xFE,
        (
            "琉卡小姐昨天\x01",
            "鼓励了最近一直\x01",
            "无精打采的我。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "呼，看来我并没有\x01",
            "被她讨厌呢……\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E8")

    Jump("loc_1511")

    label("loc_10ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_11E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1190")

    #C0054
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "不知为何，做什么事情都提不起精神。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "我好像被琉卡小姐\x01",
            "讨厌了，\x01",
            "以后连酒馆都不能去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "今天不如早点\x01",
            "收工回家吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11E4")

    label("loc_1190")


    #C0057
    ChrTalk(
        0xFE,
        (
            "我好像被琉卡小姐\x01",
            "讨厌了，\x01",
            "以后连酒馆都不能去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "呼……都没心情工作了。\x02",
    )

    CloseMessageWindow()

    label("loc_11E4")

    Jump("loc_1511")

    label("loc_11E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1307")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A2")

    #C0059
    ChrTalk(
        0xFE,
        (
            "在参加宴会时，我为什么\x01",
            "要对琉卡小姐说那种话呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "不仅被她无视了，\x01",
            "而且那种借酒示好的做法\x01",
            "本来就很难看吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "唉……真想狠揍\x01",
            "昨晚的我一百拳……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1302")

    label("loc_12A2")


    #C0062
    ChrTalk(
        0xFE,
        (
            "我昨晚竟然那种样子，\x01",
            "应该被琉卡小姐彻底讨厌了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "唉……真想狠揍\x01",
            "昨晚的我一百拳……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1302")

    Jump("loc_1511")

    label("loc_1307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1315")
    Jump("loc_1511")

    label("loc_1315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_13FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AC")

    #C0064
    ChrTalk(
        0xFE,
        (
            "嗯？冈兹去\x01",
            "镇长家了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "……呼，话说回来，\x01",
            "昨天的琉卡小姐\x01",
            "真可爱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "为了她那副笑脸，\x01",
            "无论让我做什么都可以。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_13FA")

    label("loc_13AC")


    #C0067
    ChrTalk(
        0xFE,
        (
            "……哎，那孩子……\x01",
            "不是矿山长的孩子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "他一个人来这种地方\x01",
            "做什么？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FA")

    Jump("loc_1511")

    label("loc_13FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1511")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A8")

    #C0069
    ChrTalk(
        0xFE,
        (
            "冈兹最近很有积极性呢。\x01",
            "他以前总是抱怨不断，\x01",
            "现在真是完全变了个人。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "他当初被卷入教团事件，\x01",
            "害我们那么担心，\x01",
            "看来还是产生了一些效果。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1511")

    label("loc_14A8")


    #C0071
    ChrTalk(
        0xFE,
        (
            "虽然冈兹离不开酒\x01",
            "和赌博的习性\x01",
            "还是没有改变……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "但我们从小就是好朋友，\x01",
            "这点小事就不说他什么了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1511")

    TalkEnd(0xFE)
    Return()

    # Function_6_D37 end

    def Function_7_1515(): pass

    label("Function_7_1515")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A2")

    #C0073
    ChrTalk(
        0xFE,
        (
            "现在已经可以进市里了，\x01",
            "有空时去巴鲁卡玩玩\x01",
            "倒也不错……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "但现在必须\x01",
            "努力把工作干好。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "好！开工吧！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_15DD")

    label("loc_15A2")


    #C0076
    ChrTalk(
        0xFE,
        (
            "把工作完成以后，\x01",
            "再去巴鲁卡尽兴玩！\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "好！开工吧！\x02",
    )

    CloseMessageWindow()

    label("loc_15DD")

    Jump("loc_19C3")

    label("loc_15E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_15F0")
    Jump("loc_19C3")

    label("loc_15F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_15FE")
    Jump("loc_19C3")

    label("loc_15FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_174E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16EB")

    #C0078
    ChrTalk(
        0xFE,
        (
            "占领玛因兹的那些猎兵中\x01",
            "有个头目级的女孩，\x01",
            "我总觉得她很眼熟……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "以前有一伙人来玛因兹\x01",
            "购买了很多大颗粒的七耀石，\x01",
            "她好像就是其中一员。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "那样的女孩子竟然\x01",
            "能把警备队打得溃不成军……\x01",
            "我至今都难以相信。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1749")

    label("loc_16EB")


    #C0081
    ChrTalk(
        0xFE,
        (
            "那样的女孩子竟然\x01",
            "能把警备队打得溃不成军……\x01",
            "我至今都难以相信。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "简直就像噩梦一样啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1749")

    Jump("loc_19C3")

    label("loc_174E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_183F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E6")

    #C0083
    ChrTalk(
        0xFE,
        (
            "今天早上挖到了\x01",
            "相当大的苍耀石结晶。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "嘿嘿，最近的工作状况\x01",
            "好像很顺利呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "如果在巴鲁卡玩时\x01",
            "也能这么顺利就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_183A")

    label("loc_17E6")


    #C0086
    ChrTalk(
        0xFE,
        (
            "嘿嘿，最近的工作状况\x01",
            "好像很顺利呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "如果在巴鲁卡玩时\x01",
            "也能这么顺利就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183A")

    Jump("loc_19C3")

    label("loc_183F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_189C")

    #C0088
    ChrTalk(
        0xFE,
        (
            "看样子，玛尔罗那家伙\x01",
            "已经恢复精神了。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "嘿嘿，这小子真是不让人省心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19C3")

    label("loc_189C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_18AA")
    Jump("loc_19C3")

    label("loc_18AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_199E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193D")

    #C0090
    ChrTalk(
        0xFE,
        (
            "自从昨晚的宴会结束之后，\x01",
            "玛尔罗那小子\x01",
            "就一直无精打采的……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "……好，\x01",
            "身为他的童年玩伴，\x01",
            "我就去助他一臂之力吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1999")

    label("loc_193D")


    #C0092
    ChrTalk(
        0xFE,
        (
            "在当初的教团事件中，\x01",
            "玛尔罗非常为我担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "现在就轮到我去助\x01",
            "童年玩伴一臂之力了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1999")

    Jump("loc_19C3")

    label("loc_199E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_19AC")
    Jump("loc_19C3")

    label("loc_19AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_19BA")
    Jump("loc_19C3")

    label("loc_19BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_19C3")

    label("loc_19C3")

    TalkEnd(0xFE)
    Return()

    # Function_7_1515 end

    def Function_8_19C7(): pass

    label("Function_8_19C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A76")

    #C0094
    ChrTalk(
        0xFE,
        (
            "矿山总算重新开放了，\x01",
            "虽然工作很麻烦……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "但如果不能在矿山里工作，\x01",
            "心情总是有些差呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "哈哈，矿工的工作已经\x01",
            "深深烙印在我的身体内了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1AD8")

    label("loc_1A76")


    #C0097
    ChrTalk(
        0xFE,
        (
            "如果不能在矿山里工作，\x01",
            "心情总是有些差呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "哈哈，矿工的工作已经\x01",
            "深深烙印在我的身体内了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AD8")

    Jump("loc_2234")

    label("loc_1ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1AEB")
    Jump("loc_2234")

    label("loc_1AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1AF9")
    Jump("loc_2234")

    label("loc_1AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB8")

    #C0099
    ChrTalk(
        0xFE,
        (
            "好不容易才把占领玛因兹的\x01",
            "人赶走，这次竟然在市里\x01",
            "发生了袭击事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "我必须要为玛因兹和\x01",
            "克洛斯贝尔市做些力所能及的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "……可是，我究竟\x01",
            "能做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C16")

    label("loc_1BB8")


    #C0102
    ChrTalk(
        0xFE,
        (
            "我必须要为玛因兹和\x01",
            "克洛斯贝尔市做些力所能及的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "……可是，我究竟\x01",
            "能做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C16")

    Jump("loc_2234")

    label("loc_1C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C8D")

    #C0104
    ChrTalk(
        0xFE,
        (
            "每到下雨时，\x01",
            "坑道内也会\x01",
            "很寒冷。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "虽然只要多活动一下，\x01",
            "身体就会变暖了，\x01",
            "但总这样很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2234")

    label("loc_1C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1DD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D60")

    #C0106
    ChrTalk(
        0xFE,
        (
            "奶奶最近总是\x01",
            "催我赶快找个\x01",
            "老婆……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "自从我工作不再偷懒之后，\x01",
            "她似乎很开心，\x01",
            "但这样催我真是很烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "我又不像矿山长和\x01",
            "马库斯前辈那么有上进心，\x01",
            "还是一个人生活更加轻松自在。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1DCE")

    label("loc_1D60")


    #C0109
    ChrTalk(
        0xFE,
        (
            "奶奶总是催我赶快找老婆，\x01",
            "真是烦人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "我还是一个人生活更加轻松自在，\x01",
            "结婚这种事情还是先催催亚米吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DCE")

    Jump("loc_2234")

    label("loc_1DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF5")

    #C0111
    ChrTalk(
        0xFE,
        (
            "我刚才到外面休息，\x01",
            "矿山长的儿子来找我搭话。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "他问我『矿工的工作开心吗』，\x01",
            "我觉得这个问题很难回答，\x01",
            "就随便敷衍了几句。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "……说起来，我上次\x01",
            "也回答得很消极，\x01",
            "还害他沮丧了一阵子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "唉，我这性格真是不好。\x01",
            "当时应该说得积极一些，\x01",
            "多鼓励鼓励他才对……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1F52")

    label("loc_1EF5")


    #C0115
    ChrTalk(
        0xFE,
        (
            "矿山长的儿子\x01",
            "好像很想成为\x01",
            "一名矿工。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "我当时应该说得积极一些，\x01",
            "多鼓励鼓励他才对……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F52")

    Jump("loc_2234")

    label("loc_1F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_20C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2045")

    #C0117
    ChrTalk(
        0xFE,
        (
            "只不过是休息一天而已，\x01",
            "就觉得又要懒下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "毕竟我以前一直都在偷懒，已经习惯了嘛。\x01",
            "不知道是因为体力跟不上，\x01",
            "还是懒惰怕累……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "不过，我现在还是在努力工作。\x01",
            "怎么说也不能再恢复到\x01",
            "以前那样的偷懒状态。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_20C2")

    label("loc_2045")


    #C0120
    ChrTalk(
        0xFE,
        (
            "只不过是休息一天而已，\x01",
            "就觉得又要懒下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "不过，我现在还是在努力工作。\x01",
            "怎么说也不能再恢复到\x01",
            "以前那样的偷懒状态。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C2")

    Jump("loc_2234")

    label("loc_20C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_20D5")
    Jump("loc_2234")

    label("loc_20D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_222B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219F")

    #C0122
    ChrTalk(
        0xFE,
        (
            "我最近终于体会到在工作结束\x01",
            "之后喝杯啤酒有多么爽快了……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "虽然很累很麻烦，但我已经不再偷懒，\x01",
            "而是开始努力工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "……奶奶好像也很为我开心，\x01",
            "这样的状态倒也不错。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2226")

    label("loc_219F")


    #C0125
    ChrTalk(
        0xFE,
        (
            "我最近终于体会到在工作结束\x01",
            "之后喝杯啤酒有多么爽快了……\x01",
            "所以已经不再偷懒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "……奶奶好像也很为我开心，\x01",
            "这样的状态倒也不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2226")

    Jump("loc_2234")

    label("loc_222B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2234")

    label("loc_2234")

    TalkEnd(0xFE)
    Return()

    # Function_8_19C7 end

    def Function_9_2238(): pass

    label("Function_9_2238")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_232A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E2")

    #C0127
    ChrTalk(
        0xFE,
        (
            "哈哈，矿山总算重新开放了，\x01",
            "大家终于又能在一起工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        "……噢噢，我也很激动呢！\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "挖矿挖矿，不停挖矿……\x01",
            "这才是我们矿工的生活！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2325")

    label("loc_22E2")


    #C0130
    ChrTalk(
        0xFE,
        (
            "已经好久没有挖矿了，\x01",
            "拿出全部干劲吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        "噢噢，真是激动啊！\x02",
    )

    CloseMessageWindow()

    label("loc_2325")

    Jump("loc_2907")

    label("loc_232A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2338")
    Jump("loc_2907")

    label("loc_2338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2346")
    Jump("loc_2907")

    label("loc_2346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_245D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E1")

    #C0132
    ChrTalk(
        0xFE,
        (
            "矿山镇竟然会被\x01",
            "那种家伙占领……\x01",
            "实在是有损我们矿工的声誉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "可恶，那些猎兵\x01",
            "以后要是敢再来，\x01",
            "我绝对不会轻易放过他们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2458")

    label("loc_23E1")


    #C0134
    ChrTalk(
        0xFE,
        (
            "不单是玛因兹被占领，\x01",
            "竟然连克洛斯贝尔市\x01",
            "都被搞得一团糟……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "那些猎兵以后要是敢再来，\x01",
            "我绝对不会轻易放过他们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2458")

    Jump("loc_2907")

    label("loc_245D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24C7")

    #C0136
    ChrTalk(
        0xFE,
        (
            "好像已经快挖到\x01",
            "目标地层了。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "嘿嘿，堆积如山的七耀石就在眼前。\x01",
            "拿出干劲，继续挖吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2907")

    label("loc_24C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2537")

    #C0138
    ChrTalk(
        0xFE,
        (
            "好，今天也要\x01",
            "拼命采掘。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "嘿嘿，反正早晚要挖，干脆一鼓作气，\x01",
            "把明天的定额也一起完成好了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2907")

    label("loc_2537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_267F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_261C")

    #C0140
    ChrTalk(
        0xFE,
        (
            "最近出现的那种\x01",
            "来历不明的大型魔兽\x01",
            "让我老婆非常担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "其实我们早就对涌入矿山的\x01",
            "魔兽见怪不怪了，\x01",
            "并不需要那么担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "……话说回来，我以前\x01",
            "还曾遭到军犬袭击而受伤，\x01",
            "倒也不能把话说得太满……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_267A")

    label("loc_261C")


    #C0143
    ChrTalk(
        0xFE,
        (
            "总之，还是多小心那种\x01",
            "来历不明的魔兽吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "不管怎么说，我可\x01",
            "不想出事，让老婆为我伤心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_267A")

    Jump("loc_2907")

    label("loc_267F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2766")

    #C0145
    ChrTalk(
        0xFE,
        (
            "昨天，我和矿山长\x01",
            "从白天就开始\x01",
            "一起喝酒……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "喝到晚上，从巴鲁卡归来的\x01",
            "冈兹他们也过来加入了。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "因为机会难得，\x01",
            "我们把罗基也叫了过来，\x01",
            "举办了一场大宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "和同伴们一起喝酒\x01",
            "果然是最高享受啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_27BE")

    label("loc_2766")


    #C0149
    ChrTalk(
        0xFE,
        (
            "昨天晚上，全体矿工\x01",
            "共同举办了一场大宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "和同伴们一起喝酒\x01",
            "果然是最高享受啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27BE")

    Jump("loc_2907")

    label("loc_27C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_27D1")
    Jump("loc_2907")

    label("loc_27D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_284A")

    #C0151
    ChrTalk(
        0xFE,
        (
            "罗基那小子总算有干劲了，\x01",
            "这真是件好事，\x01",
            "但他的工作技术还差得远。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "身为前辈，\x01",
            "我必须得好好教导他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2907")

    label("loc_284A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2907")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D6")

    #C0153
    ChrTalk(
        0xFE,
        (
            "为了我老婆，\x01",
            "挖哟～挖哟～¤\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "为了玛因兹，\x01",
            "挖哟～挖哟～¤\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    #C0155
    ChrTalk(
        0xFE,
        (
            "嘿嘿，今天一天\x01",
            "也要努力采矿。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 4)
    Jump("loc_2907")

    label("loc_28D6")


    #C0156
    ChrTalk(
        0xFE,
        (
            "为了我老婆和这座矿山镇，\x01",
            "今天也要努力采矿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2907")

    TalkEnd(0xFE)
    Return()

    # Function_9_2238 end

    def Function_10_290B(): pass

    label("Function_10_290B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_291C")
    Jump("loc_2A4C")

    label("loc_291C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_292A")
    Jump("loc_2A4C")

    label("loc_292A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2938")
    Jump("loc_2A4C")

    label("loc_2938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2946")
    Jump("loc_2A4C")

    label("loc_2946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2954")
    Jump("loc_2A4C")

    label("loc_2954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2962")
    Jump("loc_2A4C")

    label("loc_2962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F2")

    #C0157
    ChrTalk(
        0xFE,
        (
            "哇，矿山里面\x01",
            "原来是这样的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "又黑又广阔……\x01",
            "好像会有幽灵出现呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "嗯，爸爸在什么地方呢？\x01",
            "开始探险吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2A3E")

    label("loc_29F2")


    #C0160
    ChrTalk(
        0xFE,
        (
            "我想看看爸爸\x01",
            "在工作时的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "嗯，爸爸到底在哪里呢～\x01",
            "开始探险吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3E")

    Jump("loc_2A4C")

    label("loc_2A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2A4C")

    label("loc_2A4C")

    TalkEnd(0xFE)
    Return()

    # Function_10_290B end

    def Function_11_2A50(): pass

    label("Function_11_2A50")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门被坚固的门锁锁住了。\x01",
            "对面好像是废坑。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_11_2A50 end

    SaveToFile()

Try(main)
