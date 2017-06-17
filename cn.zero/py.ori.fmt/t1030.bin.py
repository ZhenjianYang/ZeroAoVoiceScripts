from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1030.bin",                # FileName
        "t1030",                    # MapName
        "t1030",                    # Location
        0x0041,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1030",                  # 0
        "工作人员",               # 1
        "工作人员",               # 2
        "咪西",                   # 3
        "女性",                   # 4
        "女孩",                   # 5
        "男孩",                   # 6
        "男性",                   # 7
        "游客",                   # 8
        "本德",                   # 9
        "库雷优",                 # 10
        "萨妮塔",                 # 11
        "玛丽",                   # 12
        "SE控制",                 # 13
        "翠雀酒店方向",           # 14
        "主题公园方向",           # 15
    ))

    AddCharChip((
        "chr/ch28300.itc",                   # 00
        "chr/ch23500.itc",                   # 01
        "chr/ch23900.itc",                   # 02
        "chr/ch24600.itc",                   # 03
        "chr/ch24200.itc",                   # 04
        "chr/ch32200.itc",                   # 05
        "chr/ch10200.itc",                   # 06
        "chr/ch27600.itc",                   # 07
        "chr/ch33300.itc",                   # 08
        "chr/ch34400.itc",                   # 09
        "chr/ch39000.itc",                   # 0A
    ))

    DeclNpc(4750,    4400,    0,       180,  257,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-4000,   4400,    0,       180,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(360,     4159,    -15840,  180,  385,  0x0, 0,   6,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-9810,   4000,    -5130,   45,   385,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-8970,   4000,    -4289,   225,  385,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-3690,   4000,    -19149,  180,  385,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-3690,   1639,    -23280,  0,    385,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-7409,   4000,    -6219,   180,  385,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(7699,    4000,    -1519,   135,  389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(9159,    4000,    -1759,   270,  389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(7889,    4000,    -3069,   360,  405,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(6949,    4000,    -3160,   45,   389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 16,  0.0,                   -48.0,                 -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  16.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 15,  0.0,                   4.150000095367432,     3.0,                   81.0,                  [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.6666666865348816,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -2.766666889190674,    -0.6000000238418579,   1.0])

    DeclActor(-14170,  4000,    -6040,   1200,    -14170,  5500,    -6040,   0x007C, 0,  18, 0x0000)
    DeclActor(-6650,   4000,    1550,    1200,    -6650,   5500,    1550,    0x007C, 0,  19, 0x0000)
    DeclActor(4180,    4250,    -9540,   1200,    4180,    4250,    -9540,   0x007C, 0,  17, 0x0000)

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "翠雀酒店方向")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "主题公园方向")

    ScpFunction((
        "Function_0_3D0",          # 00, 0
        "Function_1_488",          # 01, 1
        "Function_2_526",          # 02, 2
        "Function_3_647",          # 03, 3
        "Function_4_895",          # 04, 4
        "Function_5_BDE",          # 05, 5
        "Function_6_CD8",          # 06, 6
        "Function_7_D2D",          # 07, 7
        "Function_8_D51",          # 08, 8
        "Function_9_D77",          # 09, 9
        "Function_10_E63",         # 0A, 10
        "Function_11_EA3",         # 0B, 11
        "Function_12_F60",         # 0C, 12
        "Function_13_FA5",         # 0D, 13
        "Function_14_FF1",         # 0E, 14
        "Function_15_100A",        # 0F, 15
        "Function_16_122A",        # 10, 16
        "Function_17_1977",        # 11, 17
        "Function_18_1AFC",        # 12, 18
        "Function_19_1B59",        # 13, 19
    ))


    def Function_0_3D0(): pass

    label("Function_0_3D0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_410"),
        (1, "loc_41C"),
        (2, "loc_428"),
        (3, "loc_434"),
        (4, "loc_440"),
        (5, "loc_44C"),
        (6, "loc_458"),
        (SWITCH_DEFAULT, "loc_464"),
    )


    label("loc_410")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_41C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_428")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_434")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_440")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_44C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_458")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_464")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_470")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_487")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_470")

    label("loc_487")

    Return()

    # Function_0_3D0 end

    def Function_1_488(): pass

    label("Function_1_488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_496")
    Jump("loc_525")

    label("loc_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_525")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_4B2")
    Jump("loc_525")

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4C0")
    Jump("loc_525")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_4CE")
    Jump("loc_525")

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4EB")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_525")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_51C")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_525")

    label("loc_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_525")

    label("loc_525")

    Return()

    # Function_1_488 end

    def Function_2_526(): pass

    label("Function_2_526")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_543")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_583")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "t1030_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1030_sky_y", 0x1, 0x1)
    Jump("loc_5A7")

    label("loc_583")

    SetMapObjFrame(0xFF, "t1030_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1030_sky_y", 0x0, 0x1)

    label("loc_5A7")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_610")
    LoadEffect(0x1, "event\\eva00_00.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0x0, 4180, 4250, -9540, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_610")

    SoundDistance(0x375, 0x92E0, 0xFA0, 0x44D4, 0x15F90, 0xEA60, 0x64, 0x0)
    OP_E1(0xFFFFF646, 0xFA0, 0x2800)
    OP_E1(0xFFFED040, 0xFA0, 0x466E)
    Return()

    # Function_2_526 end

    def Function_3_647(): pass

    label("Function_3_647")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_658")
    Jump("loc_891")

    label("loc_658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_666")
    Jump("loc_891")

    label("loc_666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_674")
    Jump("loc_891")

    label("loc_674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_682")
    Jump("loc_891")

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_690")
    Jump("loc_891")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_70B")

    #C0001
    ChrTalk(
        0xFE,
        (
            "为了参加主题公园的夜场\x01",
            "而在这个时间入园的客人\x01",
            "也非常多。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "充满浪漫气氛的夜场，\x01",
            "非常受情侣们欢迎哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_891")

    label("loc_70B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_888")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E0")

    #C0003
    ChrTalk(
        0xFE,
        (
            "欢迎来到米修拉姆\x01",
            "引以为傲的主题公园。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "请问您有门票吗？\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0000F不……这次还有要事。\x01",
            "不好意思，就不进去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "哦哦，是吗……\x01",
            "那可真遗憾。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "期待您下次前来时\x01",
            "入园游玩。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_883")

    label("loc_7E0")


    #C0008
    ChrTalk(
        0xFE,
        (
            "您这次似乎\x01",
            "不打算进入主题公园……\x01",
            "真是遗憾。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "不过，米修拉姆还有其它很多\x01",
            "值得一去的好地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "入夜后，就算在园外，\x01",
            "应该也可以看到烟花，\x01",
            "请不要错过哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_883")

    Jump("loc_891")

    label("loc_888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_891")

    label("loc_891")

    TalkEnd(0xFE)
    Return()

    # Function_3_647 end

    def Function_4_895(): pass

    label("Function_4_895")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_8A6")
    Jump("loc_BDA")

    label("loc_8A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_8B4")
    Jump("loc_BDA")

    label("loc_8B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_8C2")
    Jump("loc_BDA")

    label("loc_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_8D0")
    Jump("loc_BDA")

    label("loc_8D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_8DE")
    Jump("loc_BDA")

    label("loc_8DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_A2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99D")

    #C0011
    ChrTalk(
        0xFE,
        (
            "园内除了各种游乐设施之外，\x01",
            "还有贩卖咪西\x01",
            "周边产品的商店哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "其中最推荐的是\x01",
            "『咪西猫耳头饰』！\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "在园内特有的热烈气氛中，\x01",
            "体验一下彻底放松的感觉如何呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A25")

    label("loc_99D")


    #C0014
    ChrTalk(
        0xFE,
        (
            "园内除了各种游乐设施之外，\x01",
            "还有贩卖咪西\x01",
            "周边产品的商店哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "除了『咪西猫耳头饰』之外，\x01",
            "还有挂绳等小装饰，\x01",
            "各种周边应有尽有哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A25")

    Jump("loc_BDA")

    label("loc_A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_BD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0C")

    #C0016
    ChrTalk(
        0xFE,
        (
            "刚才进去的旅行者……\x01",
            "真是很有趣的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "说着『要确认一下\x01",
            "  主题公园里\x01",
            "  有没有另一只咪西！』\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "……感觉气势十足哦。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#0006F（是雷克特先生吧……）\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        "#0106F（他到底在干什么呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BCC")

    label("loc_B0C")


    #C0021
    ChrTalk(
        0xFE,
        (
            "呵呵，不必担心。\x01",
            "咪西是不可能\x01",
            "出现第二只的。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#0003F（嗯～因为扮演人员的值班日程\x01",
            "  一定排得很紧吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0211F（……请不要说这种\x01",
            "  破坏别人梦想的话。）\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0011F（对、对不起。）\x02",
    )

    CloseMessageWindow()

    label("loc_BCC")

    Jump("loc_BDA")

    label("loc_BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BDA")

    label("loc_BDA")

    TalkEnd(0xFE)
    Return()

    # Function_4_895 end

    def Function_5_BDE(): pass

    label("Function_5_BDE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8D")

    #C0025
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "大家好！\x01",
            "欢迎来到奇幻乐园。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，要玩得开心哦～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        "#0201F……真的咪西……！！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0005F缇、缇欧？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        (
            "#0203F……咳，\x01",
            "没什么。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_CD4")

    label("loc_C8D")


    #C0030
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "大家好！\x01",
            "欢迎来到奇幻乐园。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，要玩得开心哦～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD4")

    TalkEnd(0xFE)
    Return()

    # Function_5_BDE end

    def Function_6_CD8(): pass

    label("Function_6_CD8")

    TalkBegin(0xFE)

    #C0032
    ChrTalk(
        0xFE,
        (
            "哇～……\x01",
            "这就是主题公园啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "……真是好大啊，\x01",
            "要是能玩个遍就好了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_CD8 end

    def Function_7_D2D(): pass

    label("Function_7_D2D")

    TalkBegin(0xFE)

    #C0034
    ChrTalk(
        0xFE,
        (
            "哇！\x01",
            "我早就想来这里了！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_D2D end

    def Function_8_D51(): pass

    label("Function_8_D51")

    TalkBegin(0xFE)
    OP_93(0xFE, 0xB4, 0x0)

    #C0035
    ChrTalk(
        0xFE,
        "爸爸～快进去吧～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_D51 end

    def Function_9_D77(): pass

    label("Function_9_D77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE6")
    OP_93(0xFE, 0x0, 0x0)

    #C0036
    ChrTalk(
        0xD,
        (
            "爸爸～！\x01",
            "你在干什么～？\x01",
            "快点进去啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "好好，知道了，知道了，\x01",
            "稍微等一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_E5F")

    label("loc_DE6")


    #C0038
    ChrTalk(
        0xFE,
        (
            "话说，小孩子还真是\x01",
            "喜欢这种地方啊。\x01",
            "都已经傍晚了，竟然还那么精神。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "要是不管他的话，一定会\x01",
            "玩到精疲力尽为止吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5F")

    TalkEnd(0xFE)
    Return()

    # Function_9_D77 end

    def Function_10_E63(): pass

    label("Function_10_E63")

    TalkBegin(0xFE)

    #C0040
    ChrTalk(
        0xFE,
        (
            "虽然刚刚傍晚，不过还是趁着\x01",
            "开始拥挤之前先回酒店吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_E63 end

    def Function_11_EA3(): pass

    label("Function_11_EA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_EF3")

    #C0041
    ChrTalk(
        0x10,
        "其实我还有工作没做完。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x10,
        (
            "不能一直玩啊……\x01",
            "算、算了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5C")

    label("loc_EF3")


    #C0043
    ChrTalk(
        0x10,
        (
            "偶尔也要照顾到家人的情绪……\x01",
            "……虽然这么想。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x10,
        (
            "但她们两个的热情也太高涨了吧……\x01",
            "算、算了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_F5C")

    TalkEnd(0xFE)
    Return()

    # Function_11_EA3 end

    def Function_12_F60(): pass

    label("Function_12_F60")

    TalkBegin(0xFE)

    #C0045
    ChrTalk(
        0x11,
        (
            "今天我先生\x01",
            "带我们来玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x11,
        (
            "呵呵，好期待\x01",
            "主题公园哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_F60 end

    def Function_13_FA5(): pass

    label("Function_13_FA5")

    TalkBegin(0xFE)

    #C0047
    ChrTalk(
        0x12,
        (
            "爸爸，萨妮塔\x01",
            "想去坐摩天轮。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x12,
        (
            "想和玛丽一起\x01",
            "升上最高\x01",
            "的地方。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_FA5 end

    def Function_14_FF1(): pass

    label("Function_14_FF1")

    TalkBegin(0xFE)

    #C0049
    ChrTalk(
        0x13,
        "喵～呜……¤\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_FF1 end

    def Function_15_100A(): pass

    label("Function_15_100A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_101A")
    Jump("loc_1216")

    label("loc_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_1028")
    Jump("loc_1216")

    label("loc_1028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_1036")
    Jump("loc_1216")

    label("loc_1036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1044")
    Jump("loc_1216")

    label("loc_1044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_1052")
    Jump("loc_1216")

    label("loc_1052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1161")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1125")

    #C0050
    ChrTalk(
        0x151,
        (
            "#5705F……现在要去\x01",
            "主题公园玩吗？\x02\x03",

            "#5702F买套咪西的玩偶服，\x01",
            "然后穿去参加竞拍会\x01",
            "似乎也挺有趣的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#0006F但那未免也太诡异了吧……\x02\x03",

            "#0000F总、总而言之，\x01",
            "现在还是先去精品店吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_115C")

    label("loc_1125")


    #C0052
    ChrTalk(
        0x101,
        (
            "#0000F现在不需要去主题公园，\x01",
            "先去精品店买正装吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115C")

    Jump("loc_1216")

    label("loc_1161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_120D")

    #C0053
    ChrTalk(
        0x101,
        (
            "#0003F这次的目标是『黑之竞拍会』，\x01",
            "主题公园只好放弃了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1208")

    #C0054
    ChrTalk(
        0x103,
        "#0208F…………………………\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#0011F（果、果然还是……觉得有些遗憾吗？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1208")

    Jump("loc_1216")

    label("loc_120D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1216")

    label("loc_1216")

    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x5)
    Return()

    # Function_15_100A end

    def Function_16_122A(): pass

    label("Function_16_122A")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadEffect(0x0, "event\\ev309_00.eff")
    FadeToBright(1000, 0)
    OP_68(0, 2200, -47400, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22940, 0)
    SetCameraDistance(21940, 2500)
    SetChrPos(0x101, 600, 0, -49200, 0)
    SetChrPos(0x102, -600, 0, -49200, 0)
    SetChrPos(0x103, 1200, 0, -50700, 0)
    SetChrPos(0x104, -1200, 0, -50700, 0)

    def lambda_12D7():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12D7)

    def lambda_12EC():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12EC)

    def lambda_1301():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1301)

    def lambda_1316():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1316)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0056
    ChrTalk(
        0x103,
        "#0205F#11P啊……！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#0005F#5P那就是主题公园吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 4500, -47400, 3000)
    MoveCamera(0, 0, 0, 3000)
    OP_6E(600, 0)
    SetCameraDistance(10020, 3000)
    OP_6F(0x79)
    Fade(1000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 4250, -9800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-20, 9500, -8210, 0)
    MoveCamera(337, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27300, 0)
    OP_68(-20, 5300, -8210, 8000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    StopEffect(0x0, 0x0)
    OP_68(-2830, 2200, -34120, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27290, 0)
    SetCameraDistance(25290, 3000)
    OP_90(0x101, -3930, 4000, -37980, 0)
    OP_90(0x102, -4800, 4000, -38790, 0)
    OP_90(0x103, -2750, 4000, -39310, 0)
    OP_90(0x104, -3800, 4000, -40070, 0)

    def lambda_151C():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_151C)
    Sleep(50)

    def lambda_1534():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1534)
    Sleep(50)

    def lambda_154C():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_154C)
    Sleep(50)

    def lambda_1564():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1564)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)
    OP_0D()
    Sleep(500)

    #C0058
    ChrTalk(
        0x103,
        "#0205F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#0012F#5P怎么说呢……\x01",
            "看上去，的确是个很欢乐的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#0302F#6P嗯，实际上也非常不错哦。\x02\x03",

            "#0304F有摩天轮和过山车。\x02\x03",

            "还有鬼屋和\x01",
            "旋转木马。\x02\x03",

            "#0300F甚至还建有童话故事里出现的\x01",
            "中世纪城堡哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#0011F好、好像很厉害呢。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#0104F#5P呵呵，这里是ＩＢＣ作为\x01",
            "旅游热点而开发的设施，\x01",
            "的确下了不少功夫呢。\x02\x03",

            "#0102F我也曾受贝尔的邀请，\x01",
            "进去玩过一次，\x01",
            "真是逛都逛不完哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        "#0205F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 500)

    def lambda_176D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_176D)

    def lambda_177A():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_177A)

    #C0064
    ChrTalk(
        0x101,
        (
            "#0012F#5P嗯……\x02\x03",

            "#0000F……虽然不能耽误太多时间，\x01",
            "不过，要不要稍微进去看一下呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#0208F#6P…………不………………\x02\x03",

            "#0206F我们又不是来玩的，\x01",
            "没必要特意进去。\x02\x03",

            "而且门票似乎也很贵。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#0303F#6P嗯，的确不便宜啊。\x02\x03",

            "#0300F现在才进去的话，\x01",
            "根本就玩不回本吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#0109F#5P还是等到下次休假时，\x01",
            "大家一起过来玩吧。\x02\x03",

            "#0102F到时候，一定要从上午开始，\x01",
            "痛痛快快地玩上一整天哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0068
    ChrTalk(
        0x103,
        "#0202F#12P……好的。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -3890, 0, -32460, 0)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xA4, 2)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_16_122A end

    def Function_17_1977(): pass

    label("Function_17_1977")

    EventBegin(0x0)
    Fade(500)
    OP_68(8380, 7250, -13860, 0)
    MoveCamera(313, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20350, 0)
    SetChrPos(0x101, 4970, 4250, -11650, 0)
    SetChrPos(0x102, 4400, 4250, -13060, 0)
    SetChrPos(0x103, 6270, 4000, -12400, 315)
    SetChrPos(0x104, 7200, 4000, -11960, 315)
    StopEffect(0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1A0D")
    SetChrPos(0x151, 5580, 4000, -13450, 0)

    label("loc_1A0D")

    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '咪雪玩偶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('咪雪玩偶', 1)

    #C0070
    ChrTalk(
        0x101,
        "#5P#0005F嗯，这个戒指是……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#12P#0300F说不定正是托马\x01",
            "那家伙说的订婚戒指啊。\x02\x03",

            "#0306F没办法，\x01",
            "稍后拿到酒店的房间里\x01",
            "给他看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x3)
    OP_65(0x2, 0x1)
    SetChrPos(0x0, 4970, 4250, -11650, 0)
    EventEnd(0x5)
    Return()

    # Function_17_1977 end

    def Function_18_1AFC(): pass

    label("Function_18_1AFC")

    TalkBegin(0xFF)
    SetChrName("")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里画着\x01",
            "主题公园的平面图。\x02\x03",

            "广阔的区域内\x01",
            "似乎遍布着\x01",
            "各种各样的游乐设施。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_18_1AFC end

    def Function_19_1B59(): pass

    label("Function_19_1B59")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " ～致各位来园宾客～\x01\x01",
            "本主题公园内\x01",
            "严禁喧闹生事，\x01",
            "或携带危险物品入园。\x01\x01",
            "此外，儿童必须\x01",
            "由监护人陪同入园，\x01",
            "敬请配合。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_1B59 end

    SaveToFile()

Try(main)
