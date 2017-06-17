from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c130c.bin",                # FileName
        "c130c",                    # MapName
        "c130c",                    # Location
        0x001B,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 27, 0, 1, 0, 2],
    )

    BuildStringList((
        "c130c",                  # 0
        "警备员比尔斯",           # 1
        "中央广场",               # 2
        "西街",                   # 3
        "行政区",                 # 4
        "住宅街",                 # 5
        "欢乐街",                 # 6
        "东街",                   # 7
        "旧城区",                 # 8
        "港湾区",                 # 9
        "ＩＢＣ",                 # 10
        "站前街道",               # 11
        "后巷",                   # 12
        "乌尔斯拉间道",           # 13
        "东克洛斯贝尔街道",       # 14
        "西克洛斯贝尔街道",       # 15
        "玛因兹山道",             # 16
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
    ))

    DeclNpc(3910,    0,       5050,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)

    DeclActor(7000,    0,       2300,    1200,    7000,    1700,    2300,    0x007C, 0,  4,  0x0000)

    PlaceName(-133.72000122070312, 0.0, -187.47999572753906, 0x0000, 0x0000, "中央广场")
    PlaceName(-223.1999969482422, 0.0, -181.35000610351562, 0x0000, 0x0000, "西街")
    PlaceName(-96.97000122070312, 0.0, -66.3499984741211, 0x0000, 0x0000, "行政区")
    PlaceName(-306.2300109863281, 0.0, -79.95999908447266, 0x0000, 0x0000, "住宅街")
    PlaceName(-206.8699951171875, 0.0, -90.8499984741211, 0x0000, 0x0000, "欢乐街")
    PlaceName(-23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0000, "东街")
    PlaceName(25.18000030517578, 0.0, -293.6400146484375, 0x0000, 0x0000, "旧城区")
    PlaceName(14.970000267028809, 0.0, -128.9499969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-20.420000076293945, 0.0, -1.0199999809265137, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-118.41000366210938, 0.0, -281.3900146484375, 0x0000, 0x0000, "站前街道")
    PlaceName(-182.3699951171875, 0.0, -139.83999633789062, 0x0000, 0x0000, "后巷")
    PlaceName(-122.48999786376953, 0.0, -323.5799865722656, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(50.36000061035156, 0.0, -199.72999572753906, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-292.6199951171875, 0.0, -183.38999938964844, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-284.45001220703125, 0.0, -47.290000915527344, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-163.66000366210938, 0.0, -206.52999877929688, 0x0000, 0x0051, "")
    PlaceName(-90.51000213623047, 0.0, -171.14999389648438, 0x0000, 0x0054, "")
    PlaceName(-130.32000732421875, 0.0, -217.4199981689453, 0x0000, 0x0057, "")
    PlaceName(-164.67999267578125, 0.0, -167.05999755859375, 0x0000, 0x0053, "")
    PlaceName(-136.77999877929688, 0.0, -134.39999389648438, 0x0000, 0x0053, "")
    PlaceName(-205.85000610351562, 0.0, -173.8699951171875, 0x0000, 0x0053, "")
    PlaceName(-219.1199951171875, 0.0, -145.2899932861328, 0x0000, 0x0053, "")
    PlaceName(-186.4600067138672, 0.0, -101.7300033569336, 0x0000, 0x0052, "")
    PlaceName(-179.99000549316406, 0.0, -119.43000030517578, 0x0000, 0x0053, "")
    PlaceName(-168.0800018310547, 0.0, -131.0, 0x0000, 0x0053, "")
    PlaceName(-129.3000030517578, 0.0, -34.369998931884766, 0x0000, 0x0051, "")
    PlaceName(23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0052, "")
    PlaceName(0.0, 0.0, -341.95001220703125, 0x0000, 0x0053, "")
    PlaceName(-17.690000534057617, 0.0, -316.7699890136719, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_330",          # 00, 0
        "Function_1_3E8",          # 01, 1
        "Function_2_4A1",          # 02, 2
        "Function_3_4AC",          # 03, 3
        "Function_4_8C7",          # 04, 4
    ))


    def Function_0_330(): pass

    label("Function_0_330")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_370"),
        (1, "loc_37C"),
        (2, "loc_388"),
        (3, "loc_394"),
        (4, "loc_3A0"),
        (5, "loc_3AC"),
        (6, "loc_3B8"),
        (SWITCH_DEFAULT, "loc_3C4"),
    )


    label("loc_370")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_37C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_388")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_394")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3A0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3AC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3E7")

    Return()

    # Function_0_330 end

    def Function_1_3E8(): pass

    label("Function_1_3E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_497")
    SetChrPos(0x0, -230, -1450, -33980, 0)
    SetChrPos(0x1, -230, -1450, -33980, 0)
    SetChrPos(0x2, -230, -1450, -33980, 0)
    SetChrPos(0x3, -230, -1450, -33980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46F")
    SetChrPos(0x4, -230, -1450, -33980, 0)
    SetChrPos(0x5, -230, -1450, -33980, 0)
    Jump("loc_48E")

    label("loc_46F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48E")
    SetChrPos(0x4, -230, -1450, -33980, 0)

    label("loc_48E")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_497")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_3E8 end

    def Function_2_4A1(): pass

    label("Function_2_4A1")

    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x14)
    Return()

    # Function_2_4A1 end

    def Function_3_4AC(): pass

    label("Function_3_4AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_592")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_50B")

    #C0001
    ChrTalk(
        0xFE,
        (
            "明天是银行的临时休息日。\x01",
            "如果要利用银行业务，就要趁现在办好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58D")

    label("loc_50B")


    #C0002
    ChrTalk(
        0xFE,
        "明天是银行的临时休息日。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "虽然迟了点，但毕竟是纪念庆典，ＩＢＣ自然也要\x01",
            "停业休息一天。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "想取钱的话，就要趁现在啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_58D")

    Jump("loc_8C3")

    label("loc_592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_66C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_60F")

    #C0005
    ChrTalk(
        0xFE,
        (
            "当然了，楼顶\x01",
            "是禁止外人上去的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "因为那里和总裁室很近，\x01",
            "出于安全方面考虑，是不允许靠近的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_667")

    label("loc_60F")


    #C0007
    ChrTalk(
        0xFE,
        (
            "总有人来询问，\x01",
            "是否能去ＩＢＣ的\x01",
            "楼顶看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "哎呀呀，这里又不是\x01",
            "旅游景点啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_667")

    Jump("loc_8C3")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6D7")

    #C0009
    ChrTalk(
        0xFE,
        "今天好像有游行活动呢。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "大概是因为这个缘故吧，从一大早开始，\x01",
            "ＩＢＣ就来了很多人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C3")

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_765")

    #C0011
    ChrTalk(
        0xFE,
        (
            "纪念庆典期间，\x01",
            "商务会谈和宴会好像格外频繁。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "只要待在自治州这个地方，\x01",
            "就休想过上清静悠闲的生活啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7ED")

    label("loc_765")


    #C0013
    ChrTalk(
        0xFE,
        (
            "库罗伊斯总裁\x01",
            "又出门了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "看来今天的商务会谈和宴会\x01",
            "也安排得满满当当。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "就连待在自治州内的时候，\x01",
            "总裁也会忙得团团转啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_7ED")

    Jump("loc_8C3")

    label("loc_7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_85A")

    #C0016
    ChrTalk(
        0xFE,
        (
            "顺便一说……在纪念庆典期间，\x01",
            "来取钱的人也特别多。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ真是一天\x01",
            "都不能休息呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C3")

    label("loc_85A")


    #C0018
    ChrTalk(
        0xFE,
        "啊，你们好啊。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "港湾区的公园好像在举办\x01",
            "各种各样的活动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "热闹的欢呼声\x01",
            "都传到这里了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_8C3")

    TalkEnd(0xFE)
    Return()

    # Function_3_4AC end

    def Function_4_8C7(): pass

    label("Function_4_8C7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ｉ．Ｂ．Ｃ\x01",
            "International Bank of Crossbell\x01\x01",
            "如果想咨询大楼内各个公司的情况，\x01",
            "请到一层的服务窗口\x01",
            "进行询问。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_8C7 end

    SaveToFile()

Try(main)
