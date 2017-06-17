from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t103b.bin",                # FileName
        "t103b",                    # MapName
        "t103b",                    # Location
        0x0041,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t103b",                  # 0
        "工作人员",               # 1
        "工作人员",               # 2
        "男孩",                   # 3
        "男性",                   # 4
        "女性",                   # 5
        "男孩",                   # 6
        "男性",                   # 7
        "翠雀酒店方向",           # 8
        "主题公园方向",           # 9
    ))

    AddCharChip((
        "chr/ch28300.itc",                   # 00
        "chr/ch20600.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch24600.itc",                   # 04
        "chr/ch24200.itc",                   # 05
    ))

    DeclNpc(4750,    4400,    0,       180,  257,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-4000,   4400,    0,       180,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-200,    4219,    -15479,  90,   257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-9,      4250,    -14289,  0,    273,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(980,     4219,    -15399,  270,  257,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-3829,   0,       -55380,  90,   273,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-3650,   0,       -54209,  180,  257,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)

    DeclEvent(0x0000, 0, 12,  0.0,                   4.150000095367432,     3.0,                   81.0,                  [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.6666666865348816,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -2.766666889190674,    -0.6000000238418579,   1.0])

    DeclActor(-14170,  4000,    -6040,   1200,    -14170,  5500,    -6040,   0x007C, 0,  10, 0x0000)
    DeclActor(-6650,   4000,    1550,    1200,    -6650,   5500,    1550,    0x007C, 0,  11, 0x0000)

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "翠雀酒店方向")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "主题公园方向")

    ScpFunction((
        "Function_0_278",          # 00, 0
        "Function_1_330",          # 01, 1
        "Function_2_340",          # 02, 2
        "Function_3_37D",          # 03, 3
        "Function_4_3CF",          # 04, 4
        "Function_5_45A",          # 05, 5
        "Function_6_4FA",          # 06, 6
        "Function_7_525",          # 07, 7
        "Function_8_622",          # 08, 8
        "Function_9_667",          # 09, 9
        "Function_10_6EB",         # 0A, 10
        "Function_11_74E",         # 0B, 11
        "Function_12_7F3",         # 0C, 12
        "Function_13_9A6",         # 0D, 13
    ))


    def Function_0_278(): pass

    label("Function_0_278")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2B8"),
        (1, "loc_2C4"),
        (2, "loc_2D0"),
        (3, "loc_2DC"),
        (4, "loc_2E8"),
        (5, "loc_2F4"),
        (6, "loc_300"),
        (SWITCH_DEFAULT, "loc_30C"),
    )


    label("loc_2B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_300")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_30C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_318")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_32F")

    Return()

    # Function_0_278 end

    def Function_1_330(): pass

    label("Function_1_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_33F")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_33F")

    Return()

    # Function_1_330 end

    def Function_2_340(): pass

    label("Function_2_340")

    SoundDistance(0x375, 0x92E0, 0xFA0, 0x44D4, 0x15F90, 0xEA60, 0x64, 0x0)
    OP_E1(0xFFFFF646, 0xFA0, 0x2800)
    OP_E1(0xFFFED040, 0xFA0, 0x466E)
    Sound(918, 1, 100, 0)
    Return()

    # Function_2_340 end

    def Function_3_37D(): pass

    label("Function_3_37D")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        "看到烟花了吗？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "为了让整个米修拉姆的人都能看到，\x01",
            "特意放得很高呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_37D end

    def Function_4_3CF(): pass

    label("Function_4_3CF")

    TalkBegin(0xFE)

    #C0003
    ChrTalk(
        0xFE,
        (
            "里面现在正在进行\x01",
            "夜间游行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "以咪西为代表，\x01",
            "主题公园的吉祥物\x01",
            "正在热热闹闹地巡游。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "这是只有入园者才能\x01",
            "享受到的乐趣。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_3CF end

    def Function_5_45A(): pass

    label("Function_5_45A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C8")

    #C0006
    ChrTalk(
        0xFE,
        (
            "过山车也\x01",
            "非常好玩！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "#4S『嗖』地一下！！！！#3S\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "……那种感觉真是难以形容！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4F6")

    label("loc_4C8")


    #C0009
    ChrTalk(
        0xFE,
        (
            "过山车太棒了！\x01",
            "景色瞬间就\x01",
            "飞到身后了呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F6")

    TalkEnd(0xFE)
    Return()

    # Function_5_45A end

    def Function_6_4FA(): pass

    label("Function_6_4FA")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "唔哇……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_4FA end

    def Function_7_525(): pass

    label("Function_7_525")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E9")

    #C0012
    ChrTalk(
        0xFE,
        (
            "我老公真是的，明明很怕\x01",
            "乘坐这种刺激型的娱乐设施，\x01",
            "还非要硬着头皮上去。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "但是，已经好久没有全家同乐了，\x01",
            "真是非常开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "必须要感谢\x01",
            "在百忙之中抽出时间\x01",
            "的老公呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_61E")

    label("loc_5E9")


    #C0015
    ChrTalk(
        0xFE,
        (
            "孩子好像也玩得很高兴。\x01",
            "呵呵，必须要感谢老公啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61E")

    TalkEnd(0xFE)
    Return()

    # Function_7_525 end

    def Function_8_622(): pass

    label("Function_8_622")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64D")

    #C0016
    ChrTalk(
        0xFE,
        "（迷迷糊糊）……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_663")

    label("loc_64D")


    #C0017
    ChrTalk(
        0xFE,
        "（昏昏欲睡）……\x02",
    )

    CloseMessageWindow()

    label("loc_663")

    TalkEnd(0xFE)
    Return()

    # Function_8_622 end

    def Function_9_667(): pass

    label("Function_9_667")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B1")

    #C0018
    ChrTalk(
        0xFE,
        (
            "哎呀呀，儿子好像玩得太兴奋，\x01",
            "已经精疲力尽了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6E7")

    label("loc_6B1")

    TurnDirection(0xFE, 0xD, 0)

    #C0019
    ChrTalk(
        0xFE,
        (
            "喂，再坚持一下啊，\x01",
            "水上巴士马上就要来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E7")

    TalkEnd(0xFE)
    Return()

    # Function_9_667 end

    def Function_10_6EB(): pass

    label("Function_10_6EB")

    TalkBegin(0xFF)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "主题公园的游览图上\x01",
            "画得很清楚。\x02\x03",

            "在这片广大的场地中，\x01",
            "建有各种各样的\x01",
            "娱乐设施。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_10_6EB end

    def Function_11_74E(): pass

    label("Function_11_74E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～致各位游客～\x01\x01",
            "本主题公园\x01",
            "严令禁止不正当行为\x01",
            "以及携带危险品。\x01\x01",
            "请各位带着小孩的\x01",
            "家长务必看管好\x01",
            "自己的孩子。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_74E end

    def Function_12_7F3(): pass

    label("Function_12_7F3")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_939")

    #C0022
    ChrTalk(
        0x101,
        (
            "#5003F主题公园那边好像\x01",
            "很热闹啊……\x02\x03",

            "#5000F不过，这次没时间游玩了。\x01",
            "差不多也做好准备了，\x01",
            "我们这就去拍卖会场吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_899")

    #C0023
    ChrTalk(
        0x103,
        "#0203F……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AF")

    label("loc_899")


    #C0024
    ChrTalk(
        0x103,
        "#5403F……明白。\x02",
    )

    CloseMessageWindow()

    label("loc_8AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DA")

    #C0025
    ChrTalk(
        0x102,
        "#0100F迟到就不好了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F6")

    label("loc_8DA")


    #C0026
    ChrTalk(
        0x102,
        "#5300F迟到就不好了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91B")

    #C0027
    ChrTalk(
        0x104,
        "#0300F好，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_931")

    label("loc_91B")


    #C0028
    ChrTalk(
        0x104,
        "#5600F好，走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_931")

    SetScenarioFlags(0x0, 4)
    Jump("loc_98F")

    label("loc_939")


    #C0029
    ChrTalk(
        0x101,
        (
            "#5000F这次没时间去\x01",
            "主题公园玩了……\x02\x03",

            "差不多也做好准备了，\x01",
            "我们这就去拍卖会场吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98F")

    Sleep(50)
    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x4)
    Return()

    # Function_12_7F3 end

    def Function_13_9A6(): pass

    label("Function_13_9A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t105B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_9A6 end

    SaveToFile()

Try(main)
