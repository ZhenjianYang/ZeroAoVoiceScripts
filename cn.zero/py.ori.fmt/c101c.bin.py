from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c101c.bin",                # FileName
        "c101c",                    # MapName
        "c101c",                    # Location
        0x0013,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 19, 0, 1, 0, 2],
    )

    BuildStringList((
        "c101c",                  # 0
        "接待员米歇尔",           # 1
        "亚里欧斯",               # 2
        "游击士斯克特",           # 3
        "游击士温蔡尔",           # 4
        "游击士林",               # 5
        "游击士艾欧莉娅",         # 6
    ))

    AddCharChip((
        "chr/ch09100.itc",                   # 00
        "chr/ch02400.itc",                   # 01
        "chr/ch27200.itc",                   # 02
        "chr/ch27300.itc",                   # 03
        "chr/ch32002.itc",                   # 04
        "chr/ch32102.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(1000,    0,       12819,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(970,     0,       10300,   0,    405,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-10729,  0,       51650,   270,  405,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-12170,  0,       51490,   90,   405,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-5929,   150,     43069,   180,  469,  0x0, 0,   4,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-5869,   150,     40840,   0,    469,  0x0, 0,   5,   0,   255, 255, 0,   9,   255,  0)

    DeclActor(5500,    0,       6000,    1200,    5500,    1500,    6000,    0x007C, 0,  10, 0x0000)
    DeclActor(8000,    0,       6000,    1200,    8000,    1500,    6000,    0x007C, 0,  11, 0x0000)
    DeclActor(5500,    0,       2500,    1200,    5500,    1500,    2500,    0x007C, 0,  11, 0x0000)
    DeclActor(8000,    0,       2500,    1200,    8000,    1500,    2500,    0x007C, 0,  11, 0x0000)
    DeclActor(680,     0,       11370,   1700,    1000,    1500,    12820,   0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_298",          # 00, 0
        "Function_1_350",          # 01, 1
        "Function_2_3B0",          # 02, 2
        "Function_3_3B1",          # 03, 3
        "Function_4_3B5",          # 04, 4
        "Function_5_D01",          # 05, 5
        "Function_6_E59",          # 06, 6
        "Function_7_1034",         # 07, 7
        "Function_8_10C6",         # 08, 8
        "Function_9_130E",         # 09, 9
        "Function_10_157E",        # 0A, 10
        "Function_11_1BC2",        # 0B, 11
    ))


    def Function_0_298(): pass

    label("Function_0_298")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2D8"),
        (1, "loc_2E4"),
        (2, "loc_2F0"),
        (3, "loc_2FC"),
        (4, "loc_308"),
        (5, "loc_314"),
        (6, "loc_320"),
        (SWITCH_DEFAULT, "loc_32C"),
    )


    label("loc_2D8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2E4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2F0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2FC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_308")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_314")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_320")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_32C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_338")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_34F")

    Return()

    # Function_0_298 end

    def Function_1_350(): pass

    label("Function_1_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_368")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_3AF")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_38A")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x8, 0x10)
    Jump("loc_3AF")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_398")
    Jump("loc_3AF")

    label("loc_398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3A6")
    Jump("loc_3AF")

    label("loc_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3AF")

    label("loc_3AF")

    Return()

    # Function_1_350 end

    def Function_2_3B0(): pass

    label("Function_2_3B0")

    Return()

    # Function_2_3B0 end

    def Function_3_3B1(): pass

    label("Function_3_3B1")

    Call(0, 4)
    Return()

    # Function_3_3B1 end

    def Function_4_3B5(): pass

    label("Function_4_3B5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_574")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FB")

    #C0001
    ChrTalk(
        0x8,
        (
            "啊，是你们几个啊。\x01",
            "又要出远门了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        "#0012F嗯，有些工作……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        "是吗……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "……算啦。\x01",
            "我并没有打算插手\x01",
            "你们警察内部的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "虽然不知道你们要去哪里，\x01",
            "但要努力做好自己分内的事哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#0001F……是。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x103,
        "#0203F（似乎隐隐被察觉到什么了呢……）\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x104,
        "#0301F（呼，还真是敏锐啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_56F")

    label("loc_4FB")


    #C0009
    ChrTalk(
        0x8,
        (
            "算啦，警察局内部也有很多隐情，\x01",
            "我没有随便插嘴的立场。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "总之就好好努力吧。\x01",
            "只是，一定不要忘记自己的责任呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56F")

    Jump("loc_CFD")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58F")
    Call(0, 5)
    Jump("loc_5E5")

    label("loc_58F")


    #C0011
    ChrTalk(
        0x8,
        (
            "哎呀呀，其实是想让亚里欧斯\x01",
            "多休息一下的。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "……小滴她，\x01",
            "是不是觉得很寂寞呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E5")

    Jump("loc_CFD")

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_72E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_682")

    #C0013
    ChrTalk(
        0x8,
        (
            "差不多也该到游客们\x01",
            "前往市外的时候了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "我们派艾丝蒂尔他们\x01",
            "去乌尔斯拉医院那边了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "呵，你们几个也请\x01",
            "多加小心吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_729")

    label("loc_682")


    #C0016
    ChrTalk(
        0x8,
        "亚里欧斯正在对付通缉魔兽……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "那游行方面就交给\x01",
            "林她们吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "至于那件事就拜托斯克特来处理，\x01",
            "让温蔡尔留守待命……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "啊啊，真是的！\x01",
            "真希望人手能加倍啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_729")

    Jump("loc_CFD")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3D")

    #C0020
    ChrTalk(
        0x8,
        (
            "你们几个，昨天好像\x01",
            "相当出风头啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "竟然比艾丝蒂尔他们还领先一步，\x01",
            "还真是出人意料的大冷门呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……\x01",
            "其实我们也有同感。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#0306F毕竟稍微用上了一点\x01",
            "犯规手段嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "呵呵，就保持这种势头，继续成长，\x01",
            "然后减轻我们的负担吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "对了……\x01",
            "昨天晚上，亚里欧斯终于\x01",
            "出差回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "市政厅那边传来了请求，\x01",
            "所以已经拜托他立刻去进行\x01",
            "研讨会的警备工作了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0027
    ChrTalk(
        0x101,
        (
            "#0005F哎，研讨会的警备工作\x01",
            "不是由警察来负责的么……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#0200F是啊，搜查一科应该也\x01",
            "接到了这个任务的。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        "呵，反正就是合作警备啦。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "因为外国的ＶＩＰ也会参加那个会议，\x01",
            "所以要尽可能地保障会场安全，\x01",
            "不是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#0000F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#0300F是啊，如果有『风之剑圣』在场，\x01",
            "那还真是绝对万无一失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#0100F在这样的场合下，\x01",
            "警察和协会也会联手合作呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB3, 5)
    Jump("loc_B80")

    label("loc_A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE5")

    #C0034
    ChrTalk(
        0x8,
        (
            "说起来……\x01",
            "艾丝蒂尔他们说是\x01",
            "有些私事要办。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "好像是去了某些\x01",
            "比较偏远的地方呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "算啦，反正亚里欧斯已经回来了，\x01",
            "就让他们稍微放松一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B80")

    label("loc_AE5")


    #C0037
    ChrTalk(
        0x8,
        (
            "亚里欧斯负责市政厅，\x01",
            "艾丝蒂尔他们有私事……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "斯克特负责ＩＢＣ，\x01",
            "林她们是负责大圣堂呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "……呼，掌握成员们的行动\x01",
            "也并不是一件轻松的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B80")

    Jump("loc_CFD")

    label("loc_B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_CFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C47")

    #C0040
    ChrTalk(
        0x8,
        "啊，小朋友们，辛苦啦。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "应总部请求出差在外的亚里欧斯\x01",
            "推迟了回国日期啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "最后，都没能赶上\x01",
            "纪念庆典的第一天呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "我也免不了要对总部的人\x01",
            "大发牢骚啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CFD")

    label("loc_C47")


    #C0044
    ChrTalk(
        0x8,
        (
            "在纪念庆典期间，需要出差的任务\x01",
            "基本都被临时取消了，\x01",
            "我们的惯例是倾全员之力处理庆典期间的委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "真是的……总部连亚里欧斯\x01",
            "都想独自霸占，我可必须要\x01",
            "好好对他们倾泻一下怨言了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFD")

    TalkEnd(0x8)
    Return()

    # Function_4_3B5 end

    def Function_5_D01(): pass

    label("Function_5_D01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_E55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF8")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0046
    ChrTalk(
        0x8,
        (
            "虽然刚回来就让你这么辛苦，真是不好意思，\x01",
            "但能否稍微占用你一点时间呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "雷米菲利亚分部就在不久前\x01",
            "发来了联络……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "#1403F是关于那件事吗……\x02\x03",

            "#1400F……明白了。\x01",
            "将详细情况告诉我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_E55")

    label("loc_DF8")


    #C0049
    ChrTalk(
        0x9,
        (
            "#1403F……不用在意之前的事情。\x02\x03",

            "#1400F你们还有工作在身吧？\x01",
            "按照自己的步调去努力就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E55")

    TalkEnd(0xFE)
    Return()

    # Function_5_D01 end

    def Function_6_E59(): pass

    label("Function_6_E59")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1030")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA1")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0050
    ChrTalk(
        0xA,
        (
            "如果能趁现在将接到的工作顺利完成，\x01",
            "下周你就可以不用出差了——\x01",
            "米歇尔是这么说的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        "温蔡尔，莫非你……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xB,
        (
            "偶尔也想一个人出趟差……\x01",
            "我只是提出了这样的请求而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "纪念庆典中最忙的时期也已经结束了。\x01",
            "……你偶尔也要和未婚妻在一起度过嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xA,
        "……多谢了，搭档。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_1030")

    label("loc_FA1")


    #C0055
    ChrTalk(
        0xFE,
        (
            "下周就像温蔡尔说的那样……\x01",
            "和帕尔在一起度过好啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "……也必须要尽早确认一下\x01",
            "她那边的日程啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "已经好久没见面了，\x01",
            "真有些紧张呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1030")

    TalkEnd(0xFE)
    Return()

    # Function_6_E59 end

    def Function_7_1034(): pass

    label("Function_7_1034")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_10C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1052")
    Call(0, 6)
    Jump("loc_10C2")

    label("loc_1052")


    #C0058
    ChrTalk(
        0xFE,
        (
            "斯克特对工作太过拼命了，\x01",
            "都已经好久没有见过未婚妻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "偶尔创造一些只属于两个人的\x01",
            "时间也是很重要的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C2")

    TalkEnd(0xFE)
    Return()

    # Function_7_1034 end

    def Function_8_10C6(): pass

    label("Function_8_10C6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_115A")
    Jump("loc_11A4")

    label("loc_115A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_117A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11A4")

    label("loc_117A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_119A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11A4")

    label("loc_119A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11A4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_127D")

    #C0060
    ChrTalk(
        0xFE,
        (
            "游行的警备工作\x01",
            "终于结束了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "在人山人海中工作，\x01",
            "实在是累得要死啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        "#0300F噢噢……真是辛苦啦。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "嗯，谢谢。\x01",
            "总之，我得先好好休息一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1306")

    label("loc_127D")


    #C0064
    ChrTalk(
        0xFE,
        (
            "说起来，在人潮之中，\x01",
            "似乎看到过一张有些印象的面孔……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "不，大概只是我的错觉吧。\x01",
            "因为并没有收到联络说\x01",
            "那个人要来克洛斯贝尔啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1306")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_10C6 end

    def Function_9_130E(): pass

    label("Function_9_130E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13A2")
    Jump("loc_13EC")

    label("loc_13A2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13C2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13EC")

    label("loc_13C2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13E2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13EC")

    label("loc_13E2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13EC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1576")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1509")

    #C0066
    ChrTalk(
        0xFE,
        (
            "……啊，那不是小缇欧吗！\x01",
            "果然好可爱好可爱啊……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "姐姐我工作得好累呢。\x01",
            "能不能来给我治愈一下呀？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        "#0211F……可我并不清楚具体方法。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "只要让我紧紧～地\x01",
            "抱一抱就好啦！⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x103,
        "#0203F容我拒绝。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "（打击）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1576")

    label("loc_1509")


    #C0072
    ChrTalk(
        0xFE,
        (
            "唉，好遗憾……\x01",
            "没办法，我受到的心灵创伤\x01",
            "就用外出买午餐吃来抚平吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "最近很喜欢『摩尔吉』的\x01",
            "汉堡呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1576")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_130E end

    def Function_10_157E(): pass

    label("Function_10_157E")

    TalkBegin(0xFF)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "张贴着游击士们的轮值表。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_16F1")
    SetChrName("")

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　 　　　　　 　   去向\x01",
            "━━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：   雷米菲利亚公国\x01",
            " 　 斯克特 　： 　  『待命中』\x01",
            " 　 温蔡尔 　： 　  『待命中』\x01",
            " 　　 林 　　： ※休息（龙老饭店）\x01",
            " 　艾欧莉娅　： ※休息（面包咖啡馆）\x01",
            " 　艾丝蒂尔　： 　　  大圣堂\x01",
            " 　 约修亚 　： 　　  大圣堂\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_1BAB")

    label("loc_16F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_182D")
    SetChrName("")

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　 　　　　　 　   去向\x01",
            "━━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：     『待命中』\x01",
            " 　 斯克特 　： ※休息（龙老饭店）\x01",
            " 　 温蔡尔 　： ※休息（龙老饭店）\x01",
            " 　　 林 　　：     『待命中』\x01",
            " 　艾欧莉娅　：     『待命中』\x01",
            " 　艾丝蒂尔　： 　　乌尔斯拉医院\x01",
            " 　 约修亚 　： 　　乌尔斯拉医院\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_1BAB")

    label("loc_182D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_195A")
    SetChrName("")

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　 　　　　　 　   去向\x01",
            "━━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：      市外巡逻\x01",
            " 　 斯克特 　： 　   市外巡逻\x01",
            " 　 温蔡尔 　： 　   武器商会\x01",
            " 　　 林 　　：       行政区\x01",
            " 　艾欧莉娅　：       行政区\x01",
            " 　艾丝蒂尔　： 　　乌尔斯拉医院\x01",
            " 　 约修亚 　： 　　乌尔斯拉医院\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_1BAB")

    label("loc_195A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A8C")
    SetChrName("")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　 　　　　　 　   去向\x01",
            "━━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：       市政厅\x01",
            " 　 斯克特 　： 　    ＩＢＣ\x01",
            " 　 温蔡尔 　： 　    ＩＢＣ\x01",
            " 　　 林 　　：       大圣堂\x01",
            " 　艾欧莉娅　：       大圣堂\x01",
            " 　艾丝蒂尔　： 　※私事（山道一带）\x01",
            " 　 约修亚 　： 　※私事（山道一带）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_1BAB")

    label("loc_1A8C")

    SetChrName("")

    #A0079
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　 　　　　　 　   去向\x01",
            "━━━━━━━━━━━━━━━━━\x01",
            " 　亚里欧斯　：      列曼总部\x01",
            " 　 斯克特 　： 　  唐古拉姆门\x01",
            " 　 温蔡尔 　： 　  唐古拉姆门\x01",
            " 　　 林 　　：    阿尔摩利卡村\x01",
            " 　艾欧莉娅　：    阿尔摩利卡村\x01",
            " 　艾丝蒂尔　： 　　  行政区\x01",
            " 　 约修亚 　： 　　  行政区\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1BAB")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_10_157E end

    def Function_11_1BC2(): pass

    label("Function_11_1BC2")

    TalkBegin(0xFF)
    SetChrName("")

    #A0080
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "张贴着很多交付给\x01",
            "游击士协会的委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_11_1BC2 end

    SaveToFile()

Try(main)
