from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t2520.bin",                # FileName
        "t2520",                    # MapName
        "t2520",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 90, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2520",                  # 0
        "诺艾尔上士",             # 1
        "索妮亚副司令",           # 2
        "弗拉米队员",             # 3
        "巴雷尔队员",             # 4
        "游客贝尔缇亚",           # 5
    ))

    AddCharChip((
        "chr/ch34100.itc",                   # 00
        "apl/ch50147.itc",                   # 01
        "chr/ch00800.itc",                   # 02
        "chr/ch05702.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch34500.itc",                   # 05
    ))

    DeclNpc(740,     0,       4469,    349,  257,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(6210,    150,     -150,    260,  341,  0x0, 0,   3,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-30899,  0,       43400,   0,    257,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-70010,  449,     -32430,  90,   469,  0x0, 0,   1,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-52060,  0,       5650,    225,  385,  0x0, 0,   5,   0,   0,   1,   0,   11,  255,  0)

    DeclActor(-28890,  10,      42110,   1200,    -28890,  1500,    42110,   0x007C, 0,  20, 0x0000)
    DeclActor(4760,    0,       -280,    1200,    6210,    1500,    -150,    0x007E, 0,  6,  0x0000)

    ScpFunction((
        "Function_0_1D4",          # 00, 0
        "Function_1_28C",          # 01, 1
        "Function_2_2B7",          # 02, 2
        "Function_3_459",          # 03, 3
        "Function_4_4EE",          # 04, 4
        "Function_5_14A6",         # 05, 5
        "Function_6_168E",         # 06, 6
        "Function_7_1692",         # 07, 7
        "Function_8_3602",         # 08, 8
        "Function_9_37B3",         # 09, 9
        "Function_10_3E79",        # 0A, 10
        "Function_11_3F8A",        # 0B, 11
        "Function_12_4044",        # 0C, 12
        "Function_13_4B9C",        # 0D, 13
        "Function_14_4D71",        # 0E, 14
        "Function_15_5328",        # 0F, 15
        "Function_16_5D23",        # 10, 16
        "Function_17_5D42",        # 11, 17
        "Function_18_5D61",        # 12, 18
        "Function_19_5D80",        # 13, 19
        "Function_20_5D9F",        # 14, 20
    ))


    def Function_0_1D4(): pass

    label("Function_0_1D4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_214"),
        (1, "loc_220"),
        (2, "loc_22C"),
        (3, "loc_238"),
        (4, "loc_244"),
        (5, "loc_250"),
        (6, "loc_25C"),
        (SWITCH_DEFAULT, "loc_268"),
    )


    label("loc_214")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_220")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_22C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_238")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_244")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_250")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_25C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_268")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_274")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_28B")

    Return()

    # Function_0_1D4 end

    def Function_1_28C(): pass

    label("Function_1_28C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B6")
    OP_94(0xFE, 0xFFFF2E82, 0x1770, 0xFFFF3CB0, 0x170C, 0x3E8)
    Sleep(300)
    Jump("Function_1_28C")

    label("loc_2B6")

    Return()

    # Function_1_28C end

    def Function_2_2B7(): pass

    label("Function_2_2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2CF")
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jump("loc_445")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2EE")
    SetChrPos(0x8, 3980, 0, -150, 90)
    Jump("loc_445")

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_31C")
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -69630, 0, -30590, 180)
    Jump("loc_445")

    label("loc_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_32A")
    Jump("loc_445")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_338")
    Jump("loc_445")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3BA")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_363")
    Event(0, 15)

    label("loc_363")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_374")
    Jump("loc_3B5")

    label("loc_374")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_397")
    SetChrPos(0x8, 6080, 0, 2120, 270)
    Jump("loc_3B5")

    label("loc_397")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3B5")
    SetChrPos(0x8, 6080, 0, 2120, 180)

    label("loc_3B5")

    Jump("loc_445")

    label("loc_3BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3C8")
    Jump("loc_445")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3E0")
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jump("loc_445")

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3EE")
    Jump("loc_445")

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_445")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_406")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 14)

    label("loc_406")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_428")
    SetChrPos(0x8, 6080, 0, 2120, 270)
    Jump("loc_445")

    label("loc_428")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_445")
    SetChrPos(0x8, 6080, 0, 2120, 270)

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_458")
    ClearChrFlags(0xC, 0x80)

    label("loc_458")

    Return()

    # Function_2_2B7 end

    def Function_3_459(): pass

    label("Function_3_459")

    SetMapObjFrame(0xFF, "futon00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futon01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_485")
    Jump("loc_4AC")

    label("loc_485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4AC")
    SetMapObjFrame(0xFF, "futon00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futon01", 0x1, 0x1)

    label("loc_4AC")

    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D7")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4D7")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ED")
    OP_66(0x0, 0x1)

    label("loc_4ED")

    Return()

    # Function_3_459 end

    def Function_4_4EE(): pass

    label("Function_4_4EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4FF")
    Jump("loc_14A2")

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D")
    Call(0, 5)
    SetScenarioFlags(0x0, 1)
    Jump("loc_5D2")

    label("loc_51D")


    #C0001
    ChrTalk(
        0xFE,
        (
            "#0502F啊，是各位啊……\x01",
            "昨天真是谢谢你们了。\x02\x03",

            "#0504F因为副司令说\x01",
            "报告越早提交越好，\x01",
            "所以我昨天忙着做报告。\x02\x03",

            "#0508F凭借七耀教会的协助，\x01",
            "要是能将那个钟的事情\x01",
            "调查清楚自然最好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D2")

    Jump("loc_14A2")

    label("loc_5D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5E5")
    Jump("loc_14A2")

    label("loc_5E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_754")

    #C0002
    ChrTalk(
        0xFE,
        (
            "#0500F我们接到了报告，\x01",
            "据说昨天有游客闯入了\x01",
            "阿尔摩利卡古战场。\x02\x03",

            "#0504F听说是各位率先\x01",
            "把游客救出来的……\x01",
            "真的十分感谢。\x02\x03",

            "#0508F虽然我们为了防止类似事件的发生，\x01",
            "都会定期巡逻，但还是疏忽了……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#0002F不用客气，因为我们接到了紧急委托，\x01",
            "所以这是分内之事。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x104,
        (
            "#0300F没错没错，\x01",
            "不用这么客气啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "#0504F不好意思……\x01",
            "还是很谢谢你们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_7B0")

    label("loc_754")


    #C0006
    ChrTalk(
        0xFE,
        (
            "#0504F阿尔摩利卡古战场的事……\x01",
            "真的十分感谢。\x02\x03",

            "#0500F今后我们一定会\x01",
            "加强巡逻的力度……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B0")

    Jump("loc_14A2")

    label("loc_7B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_852")

    #C0007
    ChrTalk(
        0xFE,
        (
            "#0501F克洛斯贝尔还有很多\x01",
            "被司令白白放弃，\x01",
            "未经调查的遗迹。\x02\x03",

            "#0506F像『星见之塔』那种\x01",
            "情况未知的场所，\x01",
            "明明是个不定时炸弹……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8CD")

    label("loc_852")


    #C0008
    ChrTalk(
        0xFE,
        (
            "#0501F要是有正式的调查许可，\x01",
            "就可以彻底调查\x01",
            "与『星见之塔』类似的场所了……\x02\x03",

            "#0506F但对这些事，\x01",
            "司令都不愿意拨出预算。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CD")

    Jump("loc_14A2")

    label("loc_8D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C3E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_92F")

    #C0009
    ChrTalk(
        0xFE,
        (
            "#0502F堵截作战好像成功了啊！\x02\x03",

            "我也帮上了一点忙，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C39")

    label("loc_92F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_9C2")

    #C0010
    ChrTalk(
        0xFE,
        (
            "#0503F怎么才能抓住仿冒名牌的生产商，\x01",
            "这是一个让国境门\x01",
            "十分苦恼的问题。\x02\x03",

            "#0501F今年有了各位的协助，\x01",
            "一定要把那些人都揪出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C39")

    label("loc_9C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6F")

    #C0011
    ChrTalk(
        0xFE,
        (
            "#0500F今天也有警备队员\x01",
            "执行巡逻任务。\x02\x03",

            "#0506F现在游客的人数激增，\x01",
            "必须得加强\x01",
            "警戒的力度。\x02\x03",

            "#0501F因为克洛斯贝尔还有很多\x01",
            "与『星见之塔』类似的\x01",
            "危险场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#0309F哈哈，你要好好加油啊，后辈。\x02\x03",

            "#0302F不过，如果有需要，\x01",
            "可以来找我们帮忙哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#0202F……原来如此，\x01",
            "这就是所谓的爱摆前辈架子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        "#0310F唔……！？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#0104F哎呀，缇欧。\x01",
            "别说得这么直白啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#0306F大、大小姐……\x01",
            "你也帮我否定下啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C39")

    label("loc_B6F")


    #C0017
    ChrTalk(
        0xFE,
        (
            "#0509F那个……兰迪前辈，\x01",
            "我完全不觉得\x01",
            "前辈您是在摆架子……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        (
            "#0308F哈哈……\x01",
            "你这么安慰完全是反效果啊……\x02\x03",

            "#0306F反正我……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "#0501F唔……\x01",
            "前、前辈你要振作啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0006F兰迪，你别再装了……\x02",
    )

    CloseMessageWindow()

    label("loc_C39")

    Jump("loc_14A2")

    label("loc_C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_105E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_E23")

    #C0021
    ChrTalk(
        0xFE,
        (
            "#0502F啊……罗伊德警官，\x01",
            "昨天谢谢你了。\x02\x03",

            "#0504F托你的福，\x01",
            "芙兰好像玩得很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#0002F不用客气，\x01",
            "我还要感谢你们的邀请。\x02\x03",

            "#0004F很少有机会\x01",
            "能去听小型演唱会，\x01",
            "所以我也很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "#0509F呵呵，那就好。\x02\x03",

            "#0500F……没关系啦，\x01",
            "你还会有机会的，\x01",
            "请不要气馁。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0012F（……果然好像是误会了……）\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#0301F……我说，有美女姐妹花相陪啊！\x01",
            "真是让人羡慕。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        "#0106F我们科的男士们真是……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        "#0211F……花心萝卜。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0011F（……又被误会了！？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF7")

    label("loc_E23")


    #C0029
    ChrTalk(
        0xFE,
        (
            "#0500F那个……罗伊德警官、兰迪前辈。\x01",
            "你们昨天是不是\x01",
            "去听了港湾公园的小型演唱会？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#0005F啊？为什么会知道……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "#0502F果然！\x01",
            "因为我昨天有假，\x01",
            "所以和芙兰去听了哦。\x02\x03",

            "#0504F我当时就觉得好像\x01",
            "看到了你们……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#0302F什么嘛，\x01",
            "那怎么也不来打声招呼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "#0509F那、那个……\x02\x03",

            "当时你们旁边有三名女士，\x01",
            "好像玩得很开心，\x01",
            "所以我们就不好意思打扰了……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        "#0111F哦……？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        "#0211F……看来你们玩得很开心啊。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        "#0309F哈哈哈。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        "#0006F（这、这眼神好锐利……）\x02",
    )

    CloseMessageWindow()

    label("loc_FF7")

    SetScenarioFlags(0x0, 2)
    Jump("loc_1059")

    label("loc_FFF")


    #C0038
    ChrTalk(
        0xFE,
        (
            "#0504F昨天难得请了次假，\x01",
            "好好放松了一下。\x02\x03",

            "#0502F芙兰也很有精神的样子，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1059")

    Jump("loc_14A2")

    label("loc_105E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_106C")
    Jump("loc_14A2")

    label("loc_106C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_10E3")

    #C0039
    ChrTalk(
        0xFE,
        (
            "#0500F我现在准备去\x01",
            "郊外巡逻。\x02\x03",

            "#0503F因为危险的场所太多了，\x01",
            "为了防止游客闯入，\x01",
            "我们必须十分注意……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A2")

    label("loc_10E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_14A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1172")

    #C0040
    ChrTalk(
        0xFE,
        (
            "#0503F见识到各位的战斗方式后，\x01",
            "我深刻感觉到了自己实力的不足。\x02\x03",

            "#0501F只有更加努力训练，\x01",
            "才能保护好\x01",
            "克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A2")

    label("loc_1172")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_11D6")

    #C0041
    ChrTalk(
        0xFE,
        (
            "#0500F如果能和各位进行演习的话，\x01",
            "会对新队员的进步\x01",
            "十分有益。\x02\x03",

            "务必拜托了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A2")

    label("loc_11D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_124A")

    #C0042
    ChrTalk(
        0xFE,
        (
            "#0500F特别任务支援科的各位……\x01",
            "辛苦了。\x02\x03",

            "索妮亚副司令\x01",
            "有任务要\x01",
            "委托你们，\x02\x03",

            "能否直接和她谈呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A2")

    label("loc_124A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1442")

    #C0043
    ChrTalk(
        0xFE,
        (
            "#0508F啊，是各位啊……\x01",
            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#0005F……怎么了？\x01",
            "好像很没精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "#0506F……前段时间那起魔兽事件的犯人，\x01",
            "也就是那些黑手党手下……\x02\x03",

            "#0508F他们最近被\x01",
            "保释出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0108F……这样啊……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        "#0203F……因为支付了保释金吧。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0306F喂喂，别那么沮丧啦。\x02\x03",

            "#0300F从某种程度上来说，这是意料之中的事，\x01",
            "也没办法啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#0000F……说的没错。\x01",
            "这种体制一定\x01",
            "会慢慢完善的。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "#0503F……说得也是呢。\x01",
            "现在我只有做好\x01",
            "自己力所能及的事了。\x02\x03",

            "#0502F谢谢你们，\x01",
            "我觉得稍微轻松点了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_14A2")

    label("loc_1442")


    #C0051
    ChrTalk(
        0xFE,
        (
            "#0500F谢谢你们，\x01",
            "我觉得稍微轻松点了。\x02\x03",

            "#0503F总之，现在警备队必须\x01",
            "做好自己力所能及的事……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A2")

    TalkEnd(0xFE)
    Return()

    # Function_4_4EE end

    def Function_5_14A6(): pass

    label("Function_5_14A6")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x9, 0x0)
    TurnDirection(0x8, 0x9, 0)

    #C0052
    ChrTalk(
        0x9,
        (
            "#2003F原来如此……\x01",
            "这就是那个遗迹的\x01",
            "调查结果吧。\x02\x03",

            "#2002F做得不错哦，诺艾尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#0504F哪里，这全都靠\x01",
            "特别任务支援科的各位全力协助。\x02\x03",

            "#0501F那么……关于这件事，\x01",
            "今后要采取何种对策呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "#2003F……报告书中所写的\x01",
            "那个会召唤『魔物』的『钟』……\x02\x03",

            "#2001F很可能与古代遗物\x01",
            "存在着某种关联。\x02\x03",

            "去洛斯贝尔大圣堂问问艾拉尔达大主教\x01",
            "的意见吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#0503F所言极是……我明白了。\x02\x03",

            "#0501F那我现在就去联络大圣堂，\x01",
            "看看能不能直接与大主教对话。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        "#2000F嗯，拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_5_14A6 end

    def Function_6_168E(): pass

    label("Function_6_168E")

    Call(0, 7)
    Return()

    # Function_6_168E end

    def Function_7_1692(): pass

    label("Function_7_1692")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1726")
    Jump("loc_1770")

    label("loc_1726")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1746")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1770")

    label("loc_1746")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1766")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1770")

    label("loc_1766")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1770")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8A")

    #C0057
    ChrTalk(
        0x9,
        (
            "#2005F哎呀，是你们啊。\x02\x03",

            "#2000F诺艾尔上士已经带着\x01",
            "那处遗迹的资料，\x01",
            "前往大圣堂了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#0000F您决定要和七耀教会\x01",
            "合作了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#0301F……没得到那个司令的许可，\x01",
            "不要紧吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "#2003F……其实，『星见之塔』的\x01",
            "再调查请求已经被他回绝了。\x02\x03",

            "#2000F本次事件的情况与星见之塔\x01",
            "很相似，所以我认为，\x01",
            "还是交由大主教阁下来负责比较合适。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#0003F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#0103F……是因为他并没有亲眼所见，\x01",
            "所以无法了解事态的紧急性吗？还是……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        (
            "#0200F……只是纯粹\x01",
            "怕麻烦而已吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        "#0301F嘁……应该两个原因都有吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19F4")

    #C0065
    ChrTalk(
        0x10A,
        (
            "#0603F看样子，警备队的腐败情况\x01",
            "也已经到了相当严重的地步啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F4")


    #C0066
    ChrTalk(
        0x9,
        (
            "#2003F……总之，\x01",
            "这件事会由七耀教会和唐古拉姆的部队\x01",
            "跟进负责的。\x02\x03",

            "#2000F多亏了你们的协助，\x01",
            "我们才能努力做到这一步，\x01",
            "再次对你们表示感谢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B27")

    label("loc_1A8A")


    #C0067
    ChrTalk(
        0x9,
        (
            "#2003F『星见之塔』，还有上次的遗迹……\x02\x03",

            "#2000F这两个地方可能与古代遗物\x01",
            "有相当大的关联，\x01",
            "必须慎重对待。\x02\x03",

            "今后应该会与七耀教会\x01",
            "继续协作，共同展开调查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B27")

    Jump("loc_35FA")

    label("loc_1B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1C16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4A")
    Call(0, 5)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C11")

    label("loc_1B4A")


    #C0068
    ChrTalk(
        0x9,
        (
            "#2000F各位……\x01",
            "昨天辛苦了啊。\x02\x03",

            "#2003F你们成功完成了遗迹的调查工作，\x01",
            "并顺利消除了魔物在不明原因下\x01",
            "不断涌现的怪异现象。\x02\x03",

            "就现阶段来说，\x01",
            "这已经是最好的结果了。\x02\x03",

            "#2000F后续调查就\x01",
            "交给我们警备队吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C11")

    Jump("loc_35FA")

    label("loc_1C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1F49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EAF")

    #C0069
    ChrTalk(
        0x9,
        (
            "#2000F诺艾尔上士……\x01",
            "你好像顺利得到了他们的协助啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x109,
        "#0500F是的，他们很果断地答应了。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        (
            "#0109F当、当然啦。\x01",
            "呵呵……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#0004F艾莉，你真的没事吗？\x01",
            "样子有点奇怪啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        (
            "#0107F我、我不都说过我没事了嘛！\x02\x03",

            "#0112F好啦，要调查的话\x01",
            "就快点出发吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        "#0305F大小姐气势汹汹呢……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#0203F……嗯，艾莉前辈\x01",
            "很有勇气呢，\x01",
            "这样看来应该是没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "#2000F呵呵……你们小队的气氛还是一样热闹啊。\x02\x03",

            "#2003F……警备队对遗迹的调查\x01",
            "已经失败过了一次。\x02\x03",

            "如果再失败的话，\x01",
            "司令阁下非常有可能下令\x01",
            "取消调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        "#0303F……也是呢。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#2000F……不过，当然还是要把\x01",
            "自己的安全放在第一位哦，\x01",
            "请务必小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#0001F知道了，\x01",
            "我们将谨记于心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F44")

    label("loc_1EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC1")
    Call(0, 8)
    Jump("loc_1F44")

    label("loc_1EC1")


    #C0080
    ChrTalk(
        0x9,
        (
            "#2000F警备队对遗迹的调查\x01",
            "已经失败过了一次。\x02\x03",

            "#2003F虽然没有负伤者，\x01",
            "但有队员\x01",
            "被怪物吓得昏迷不醒……\x02\x03",

            "#2000F请你们务必要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F44")

    Jump("loc_35FA")

    label("loc_1F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_21D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2104")

    #C0081
    ChrTalk(
        0x9,
        "#2006F…………………………\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0005F……那、那个……索妮亚副司令？\x01",
            "我们脸上有什么吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "#2003F……没什么。\x02\x03",

            "只是你们的表情\x01",
            "让我感觉很熟悉。\x02\x03",

            "#2000F是想要违反秩序时……\x01",
            "才会出现的表情哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#0005F（咽口水……）\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#0101F（竞拍会的事情……\x01",
            "  她好像有所察觉啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#0200F（这就是女人的第六感吧。）\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        "#0306F（敏锐得让人不舒服啊……）\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "#2004F……呵呵，\x01",
            "我好像说了些奇怪的话呢，\x01",
            "别放在心上。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21CD")

    label("loc_2104")


    #C0089
    ChrTalk(
        0x9,
        (
            "#2003F你们可千万不要像上次的\x01",
            "魔兽事件时一样逞强哦。\x02\x03",

            "#2000F如果有什么难处理的事，\x01",
            "最好先去找赛尔盖商量。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#0001F好、好的……\x02\x03",

            "#0006F（就是因为科长一定不会同意，\x01",
            "  所以才没办法跟他商量啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21CD")

    Jump("loc_35FA")

    label("loc_21D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_258F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2508")
    SetChrSubChip(0x9, 0x0)

    #C0091
    ChrTalk(
        0x9,
        "#2003F……嗯，这样就行了。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#0005F副司令……\x01",
            "您在忙什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22C2")
    Jump("loc_230C")

    label("loc_22C2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22E2")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_230C")

    label("loc_22E2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2302")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_230C")

    label("loc_2302")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_230C")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    #C0093
    ChrTalk(
        0x9,
        (
            "#2000F嗯……\x01",
            "我在整理上次那个\x01",
            "『星见之塔』的资料。\x02\x03",

            "等司令回来后，\x01",
            "我想拿这些资料直接去跟他\x01",
            "要求组建相关调查队。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        (
            "#0301F……没问题吧？\x02\x03",

            "#0303F那个司令\x01",
            "绝对会一口回绝的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "#2003F……嗯，可能性非常之高。\x02\x03",

            "#2000F不过，即使被回绝，\x01",
            "只要考虑其它解决办法就好。\x02\x03",

            "上次我也说过，\x01",
            "如果我们放弃，\x01",
            "事情就永远没有解决的希望了。\x02\x03",

            "#2002F所以我们才要竭尽所能，\x01",
            "做好自己力所能及的事，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        "#0103F您说得正是……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#0000F我们也得做好自己力所能及的事啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_258A")

    label("loc_2508")


    #C0098
    ChrTalk(
        0x9,
        (
            "#2000F等司令回来后，\x01",
            "我想拿这些资料直接去跟他\x01",
            "要求组建相关调查队。\x02\x03",

            "如果不行的话，\x01",
            "再准备些更有说服力的\x01",
            "资料去跟他请示就好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_258A")

    Jump("loc_35FA")

    label("loc_258F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2C45")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_262B")

    #C0099
    ChrTalk(
        0x9,
        (
            "#2000F之前，警察局总部的\x01",
            "多诺邦警督\x01",
            "联系了我。\x02\x03",

            "说顺利抓到了\x01",
            "假货贩子。\x02\x03",

            "#2004F呵呵……你们作为搜查官，\x01",
            "终于做得有点像样了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C40")

    label("loc_262B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2840")

    #C0100
    ChrTalk(
        0x9,
        (
            "#2003F来自共和国方向的巴士\x01",
            "还有一段时间才会抵达。\x02\x03",

            "#2000F你们现在要是在这里等待的话，\x01",
            "应该可以得到充分休息哦。\x02\x03",

            "怎么样，要不要\x01",
            "帮你们准备房间呢？\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还没准备好】\x01",                # 0
            "【等待来自共和国的巴士】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2719"),
        (1, "loc_2786"),
        (SWITCH_DEFAULT, "loc_283B"),
    )


    label("loc_2719")

    OP_60(0x0)

    #C0101
    ChrTalk(
        0x101,
        (
            "#0001F这样啊……\x01",
            "我们还想再准备一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "#2004F嗯，知道了。\x02\x03",

            "#2000F准备好之后就跟我说一声吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_283B")

    label("loc_2786")

    OP_60(0x0)

    #C0103
    ChrTalk(
        0x101,
        (
            "#0000F那么，承蒙您的好意，\x01",
            "我们就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "#2004F知道了。\x02\x03",

            "#2000F巴士抵达之后，\x01",
            "我会去叫你们的。\x02\x03",

            "你们就好好休息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        "#0000F是！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1B, 0x1, 0x3)
    SetScenarioFlags(0x5C, 0)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Jump("loc_283B")

    label("loc_283B")

    Jump("loc_2C40")

    label("loc_2840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7A")

    #C0106
    ChrTalk(
        0x9,
        (
            "#2002F……我听说了哦，\x01",
            "你们和不良团伙、游击士\x01",
            "大闹了一场啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        "#0306F咦咦……都传到您耳边了啊。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#0006F那、那个。\x01",
            "昨天是有原因的……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "#2003F不用找借口了。\x01",
            "虽然是不良团伙，但也算是平民，\x01",
            "警察可不应该对他们出手啊……\x02\x03",

            "#2000F……虽然我应该这样说，\x01",
            "但实际上我没意见。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x104,
        "#0305F哎……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "#2003F以警察的职责来说，\x01",
            "无论如何也应该把抑制骚乱者，\x01",
            "平息事态作为唯一的行动方针。\x02\x03",

            "#2000F但你们『特别任务支援科』\x01",
            "是比较特别的存在……\x01",
            "可以采取多种不同的处理办法。\x02\x03",

            "#2004F面对愤懑积累已久的不良团伙，\x01",
            "创造一个让他们将力量发散出去的机会，\x01",
            "我觉得这种做法并不坏。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        (
            "#0200F……副司令，您说这种话\x01",
            "合适吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        (
            "#2004F赛尔盖都没说什么，\x01",
            "我就更没理由摆架子斥责你们了吧。\x02\x03",

            "#2000F呵呵……今后\x01",
            "你们也要保持这种势头，好好努力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#0005F知……知道了。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x102,
        (
            "#0100F（……应对相当灵活……\x01",
            "  真是不错的上司啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C40")

    label("loc_2B7A")


    #C0116
    ChrTalk(
        0x9,
        (
            "#2004F赛尔盖都没有说什么，\x01",
            "我就更没理由摆架子斥责你们了吧。\x01",
            "你们继续保持这种势头，好好努力啊。\x02\x03",

            "#2000F但是我希望你们以后在\x01",
            "采取违反常规的做法前，\x02\x03",

            "先好好考虑一下那种做法产生的后果\x01",
            "再采取行动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C40")

    Jump("loc_35FA")

    label("loc_2C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2E44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D88")

    #C0117
    ChrTalk(
        0x9,
        (
            "#2000F哎呀，是你们啊……\x01",
            "在纪念庆典玩得开心吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        (
            "#0306F哪有，您应该知道\x01",
            "我们这边也是很忙的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#0000F算、算啦，知足吧，\x01",
            "第一天不是还\x01",
            "放了假嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "#2003F看来都已经养足精神了啊。\x02\x03",

            "#2000F我想，在纪念庆典期间，\x01",
            "应该会出现很多突发情况……\x02\x03",

            "要将这当成你们发挥实力的机会，\x01",
            "好好努力哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E3F")

    label("loc_2D88")


    #C0121
    ChrTalk(
        0x9,
        (
            "#2000F虽然能做的并不多……\x01",
            "但还是整理一下『星见之塔』\x01",
            "的资料吧……\x02\x03",

            "#2003F根据诺艾尔上士的报告，\x01",
            "那里似乎不能\x01",
            "一直放着不管啊……\x02\x03",

            "#2000F如果可能的话，\x01",
            "有必要尽快组建一支调查队。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E3F")

    Jump("loc_35FA")

    label("loc_2E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_30A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3060")

    #C0122
    ChrTalk(
        0x9,
        "#2005F……哎呀，你们有事吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 1)), scpexpr(EXPR_END)), "loc_2FAA")

    #C0123
    ChrTalk(
        0x101,
        (
            "#0003F（对了，关于星见之塔的探索……\x01",
            "  还是向副司令申请许可比较好吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0303F（这个……算了吧，\x01",
            "  还是先别和她说了。）\x02\x03",

            "#0300F（否则可能会很麻烦的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#0006F（嗯、嗯，\x01",
            "  那样好吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "#2005F……？\x01",
            "你们说什么悄悄话呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#0011F没、没什么。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Jump("loc_3058")

    label("loc_2FAA")


    #C0128
    ChrTalk(
        0x101,
        "#0000F我们只是碰巧来到了这附近而已。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        (
            "#0205F……对了，\x01",
            "怎么没看到诺艾尔上士啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "#2000F她现在正在\x01",
            "郊外巡逻，\x02\x03",

            "应该会在傍晚回来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        "#0103F嗯，好像很忙啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3058")

    SetScenarioFlags(0x0, 1)
    Jump("loc_30A1")

    label("loc_3060")


    #C0132
    ChrTalk(
        0x9,
        (
            "#2003F不好意思，今天我很忙。\x01",
            "如果有事的话，改天再来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A1")

    Jump("loc_35FA")

    label("loc_30A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_324C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A3")

    #C0133
    ChrTalk(
        0x9,
        (
            "#2000F不久之前，\x01",
            "在从这个国境门通往共和国某个市的路上，\x01",
            "有辆导力车遭遇了可疑的事故。\x02\x03",

            "#2003F因为有些在意，就派人调查了一下，\x01",
            "似乎是鲁巴彻在不久前引发魔兽骚动\x01",
            "事件时所驾驶的车辆。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        "#0000F（……难道是……黑月干的吗？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3247")

    label("loc_31A3")


    #C0135
    ChrTalk(
        0x9,
        (
            "#2003F不久之前，黑手党的导力车\x01",
            "在这一带发生的可疑事故……\x02\x03",

            "#2001F……既然受害方是鲁巴彻，\x01",
            "我想这就不仅是事故而已了。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        "#0001F（不愧是副司令，很敏锐啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_3247")

    Jump("loc_35FA")

    label("loc_324C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_35FA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_32EB")

    #C0137
    ChrTalk(
        0x9,
        (
            "#2000F你们也\x01",
            "继续努力吧。\x02\x03",

            "我们需要帮助时，\x01",
            "会向你们提出支援请求的。\x02\x03",

            "对于特别任务支援科的活动，\x01",
            "我们会在心里默默为你们加油的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35FA")

    label("loc_32EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_333A")

    #C0138
    ChrTalk(
        0x9,
        (
            "#2000F演习随时都可以开始，\x02\x03",

            "你们做好战斗的准备了吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 13)
    Jump("loc_35FA")

    label("loc_333A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_334E")
    Call(0, 12)
    Jump("loc_35FA")

    label("loc_334E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_353E")

    #C0139
    ChrTalk(
        0x9,
        (
            "#2005F啊……你们\x01",
            "居然直接到这来了，真是罕见呢。\x01",
            "出了什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#0000F不，只是偶尔到了这附近，\x01",
            "所以来打个招呼而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        (
            "#0303F#2S虽然我\x01",
            "其实不太想来……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x9,
        (
            "#2004F……哎呀，即使如此，\x01",
            "还是特意跑过来见我了吗？\x01",
            "真是不胜荣幸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x104,
        (
            "#0305F咦！？\x01",
            "……您、您听到了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        (
            "#2002F呵呵，看表情就大概明白了。\x01",
            "先不说那个……\x02\x03",

            "#2003F正如前些天的魔兽事件一样，\x01",
            "今后估计也会有事件\x01",
            "需要你们的协助吧。\x02\x03",

            "#2000F需要帮忙就来找我吧，\x01",
            "我会尽我所能帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#0000F好的，十分感谢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_35FA")

    label("loc_353E")


    #C0146
    ChrTalk(
        0x9,
        (
            "#2003F克洛斯贝尔的腐败\x01",
            "已经蔓延到了警备队……\x02\x03",

            "#2000F不过，因为你们并没有牵涉其中，所以我觉得\x01",
            "你们可以解决警备队无论如何也解决不了\x01",
            "的案件。\x02\x03",

            "需要帮忙就来找我吧，\x01",
            "我会尽我所能帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35FA")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)
    Return()

    # Function_7_1692 end

    def Function_8_3602(): pass

    label("Function_8_3602")


    #C0147
    ChrTalk(
        0x9,
        (
            "#2000F对了……\x01",
            "你们看书吗？\x02\x03",

            "愿意的话，\x01",
            "收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0149
    ChrTalk(
        0x104,
        (
            "#0300F咦……副司令也\x01",
            "看娱乐小说呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "#2003F不管是娱乐小说还是启蒙书，\x01",
            "只要是阅读文字，\x01",
            "都能增进修养哦。\x02\x03",

            "#2002F至少比你喜欢看的那些\x01",
            "登载着女性不雅姿势的杂志\x01",
            "好无数倍吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#0306F我觉得那种写真集\x01",
            "不错啊……\x02\x03",

            "#0309F我已经离不开那个了，\x01",
            "那可是我的活力源泉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#0006F（真令人叹息……）\x02",
    )

    CloseMessageWindow()
    AddItemNumber('黑市医生格伦　12卷', 1)
    SetScenarioFlags(0x9D, 3)
    Return()

    # Function_8_3602 end

    def Function_9_37B3(): pass

    label("Function_9_37B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3846")

    #C0153
    ChrTalk(
        0xFE,
        (
            "为慎重起见，诺艾尔上士\x01",
            "昨天又指挥着部队，\x01",
            "去那处遗迹进行了调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "那些诡异的魔兽\x01",
            "果然已经不会再出现了，\x01",
            "暂且可以安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E75")

    label("loc_3846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_398C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38FD")

    #C0155
    ChrTalk(
        0xFE,
        (
            "警备队员都不能调查\x01",
            "的那个遗迹，诺艾尔上士和\x01",
            "你们却能调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "你们每个人的潜力都在\x01",
            "我们之上呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "身为索妮亚副司令的部下，\x01",
            "我们是不会输的……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3987")

    label("loc_38FD")


    #C0158
    ChrTalk(
        0xFE,
        (
            "索妮亚副司令与诺艾尔上士\x01",
            "现在好像在副司令室中进行\x01",
            "重要的商谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "副司令说，她想\x01",
            "向你们表示感谢。\x01",
            "方便的话，就请去副司令室见她吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3987")

    Jump("loc_3E75")

    label("loc_398C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_39F3")

    #C0160
    ChrTalk(
        0xFE,
        (
            "虽然巴雷尔完全\x01",
            "昏过去了，\x01",
            "但基本没有外伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "只要休息一段时间\x01",
            "就可以完全复原了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E75")

    label("loc_39F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3A32")

    #C0162
    ChrTalk(
        0xFE,
        (
            "我可没空在这里休息呢，\x01",
            "必须去给大家帮忙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E75")

    label("loc_3A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3AD3")

    #C0163
    ChrTalk(
        0xFE,
        (
            "警备队员是在\x01",
            "警察学校的警备专业接受训练的……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "诺艾尔上士作为一名女性队员，\x01",
            "毕业成绩可谓十分优秀。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "我也不能输呢。\x01",
            "要不断磨砺自我……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E75")

    label("loc_3AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B58")

    #C0166
    ChrTalk(
        0xFE,
        (
            "索妮亚副司令\x01",
            "在评估队员时，\x01",
            "只看实力，并不在乎性别。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "虽然这样一来，就必须比别人努力一倍……\x01",
            "但也是值得的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E75")

    label("loc_3B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3CA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C2C")

    #C0168
    ChrTalk(
        0xFE,
        (
            "昨天诺艾尔上士和索妮亚副司令\x01",
            "都不当班。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "诺艾尔上士好像\x01",
            "和她妹妹出去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "……索妮亚副司令\x01",
            "做什么了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "虽然我很想知道，\x01",
            "但副司令她没什么生活情趣，\x01",
            "所以很难想象……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3C9B")

    label("loc_3C2C")


    #C0172
    ChrTalk(
        0xFE,
        (
            "索尼娅副司令\x01",
            "现在好像是单身……\x01",
            "难道有什么浪漫艳遇……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "因为工作中聊闲话会被骂，\x01",
            "所以我不敢问……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C9B")

    Jump("loc_3E75")

    label("loc_3CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3D10")

    #C0174
    ChrTalk(
        0xFE,
        (
            "一般来说，警备队员\x01",
            "都要在所执勤的国境门那里待命。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "诺艾尔上士他们平常\x01",
            "也会在这边过夜哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E75")

    label("loc_3D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3E75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E02")

    #C0176
    ChrTalk(
        0xFE,
        (
            "索妮亚副司令和警察局的赛尔盖科长\x01",
            "好像是旧识。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "而且也时常用导力通讯进行\x01",
            "直接联络……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "……仔细一想的话，\x01",
            "总觉得这两人的关系有点可疑呢。\x01",
            "难道…………？\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "……咳咳，我失言了。\x01",
            "请忘记我刚才所说的话吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3E75")

    label("loc_3E02")


    #C0180
    ChrTalk(
        0xFE,
        "暂且不说关系是否可疑……\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "上司之间关系好的话，\x01",
            "两个组织间的合作也会变得更加容易。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "今后也一起努力吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3E75")

    TalkEnd(0xFE)
    Return()

    # Function_9_37B3 end

    def Function_10_3E79(): pass

    label("Function_10_3E79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6C")

    #C0183
    ChrTalk(
        0xFE,
        "……嗯……怪、怪物……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x109,
        (
            "#0503F他在对那处遗迹进行调查时\x01",
            "遭遇到了诡异的魔兽。\x02\x03",

            "#0501F因为胆子不是很大，所以\x01",
            "被吓得不省人事了……\x01",
            "只能暂时撤退。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        "#0101F（咽口水……）\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#0001F这……还是做好心理准备\x01",
            "比较好啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F86")

    label("loc_3F6C")


    #C0187
    ChrTalk(
        0xFE,
        "呜呜……怪、怪物……\x02",
    )

    CloseMessageWindow()

    label("loc_3F86")

    TalkEnd(0xFE)
    Return()

    # Function_10_3E79 end

    def Function_11_3F8A(): pass

    label("Function_11_3F8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FFD")

    #C0188
    ChrTalk(
        0xFE,
        (
            "这里好像\x01",
            "并不是候车室呢，\x01",
            "我没注意……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "而且，\x01",
            "总觉得这里很乱。\x01",
            "好、好想打扫一下……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4040")

    label("loc_3FFD")


    #C0190
    ChrTalk(
        0xFE,
        (
            "好不容易出来旅行，\x01",
            "居然会想打扫……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        "大概是女仆的习惯吧。\x02",
    )

    CloseMessageWindow()

    label("loc_4040")

    TalkEnd(0xFE)
    Return()

    # Function_11_3F8A end

    def Function_12_4044(): pass

    label("Function_12_4044")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0xE1, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_68(3870, 1200, -590, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25200, 0)
    SetChrPos(0x101, 3000, 0, 0, 90)
    SetChrPos(0x102, 3000, 0, -1500, 90)
    SetChrPos(0x103, 1500, 0, -1500, 90)
    SetChrPos(0x104, 1500, 0, 0, 90)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0192
    ChrTalk(
        0x9,
        (
            "#11P#2002F呵呵……终于来了呢。\x02\x03",

            "等你们很久了，特别任务支援科的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        "#5P#0500F辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#6P#0000F二位也辛苦了，\x01",
            "索妮亚副司令、诺艾尔上士。\x02\x03",

            "我们为了确认支援请求\x01",
            "而过来拜访了……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x104,
        (
            "#6P#0300F#2S虽然我\x01",
            "其实不太想来……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "#11P#2004F……哎呀，即使如此，\x01",
            "还是特意跑过来见我了吗？\x02\x03",

            "真是不胜荣幸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x104,
        (
            "#6P#0305F咦！？\x01",
            "……您、您听到了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x9,
        (
            "#11P#2004F呵呵，看表情就大概明白了。\x02\x03",

            "#2000F那么，\x01",
            "快点进入关于委托的话题吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        "#6P#0100F嗯，请多指教。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        (
            "#11P#2000F呵呵，好的。\x01",
            "那么，诺艾尔上士，拜托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "#5P#0501F是。\x02\x03",

            "这次要拜托大家的\x01",
            "不是别的。\x02\x03",

            "#0503F而是关于今天将举行的，\x01",
            "警备队新人队员们的实战演习……\x02\x03",

            "#0501F在此想要拜托各位\x01",
            "当他们的对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#6P#0005F与警备队员进行实战演习吗……\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#6P#0100F虽说是新人，\x01",
            "但毫无疑问，\x01",
            "他们都具有相当的实力。\x02\x03",

            "因为我听说过警备队聚集了\x01",
            "许多战斗精英。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        (
            "#11P#2002F呵呵……你很清楚呢。\x02\x03",

            "#2003F与他们进行训练，\x01",
            "也可以锻炼你们的能力……\x01",
            "很划算吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#6P#0200F……话说回来，\x01",
            "为什么会对我们提出委托？\x02\x03",

            "#0203F虽然我这么说也许不太合适，\x01",
            "但我想除了我们之外，\x01",
            "善于战斗的人要多少有多少。\x02\x03",

            "#0200F比如……游击士等。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        "#6P#0011F喂、喂喂，缇欧……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x104,
        (
            "#6P#0303F……不！\x01",
            "我的意见和阿缇完全一致。\x02\x03",

            "训练嘛，对手当然越强\x01",
            "越好。\x02\x03",

            "#0309F要不，现在就立刻去\x01",
            "委托游击士吧，\x01",
            "这样不是更好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x9,
        (
            "#11P#2004F呵呵……\x01",
            "听起来，你好像是想\x01",
            "找理由逃避我呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x104,
        "#6P#0306F呃。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x9,
        (
            "#11P#2003F不过……我对此并不否认。\x02\x03",

            "跟只成立了一两个月的支援科比起来，\x01",
            "恐怕还是老练的游击士们\x01",
            "实力更强吧。\x02\x03",

            "#2000F但是，你们解决了\x01",
            "警备队处理不了的\x01",
            "魔兽事件，功劳众所皆知。\x02\x03",

            "从这件事中，不仅是战斗力，\x01",
            "我感到了你们独有的力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        "#6P#0005F我们独有的……\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "#5P#0500F兰迪前辈在\x01",
            "贝尔加德门时也是\x01",
            "知名的强者……\x02\x03",

            "大家好像都评价他是\x01",
            "不可多得的人才，实力上\x01",
            "也毫不逊色于那些游击士哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_47DA():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47DA)
    Sleep(100)

    def lambda_47EA():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47EA)
    Sleep(50)

    def lambda_47FA():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_47FA)
    Sleep(800)

    #C0213
    ChrTalk(
        0x101,
        "#6P#0005F是、是吗！？\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x103,
        "#6P#0205F第一次听说。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        (
            "#6P#0105F真的很令人惊讶呢。\x02\x03",

            "#0100F这么难得的事情，\x01",
            "你为什么不告诉我们呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        (
            "#6P#0300F……哎，都是以前的事了，\x01",
            "也没什么好说的。\x02\x03",

            "#0306F不过，\x01",
            "还是不感兴趣啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x9,
        (
            "#11P#2003F就我个人而言，你不参加\x01",
            "也没关系。\x02\x03",

            "#2002F如果对于向支援科推荐你的我，\x01",
            "没有感到任何恩情的话……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4957():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4957)
    Sleep(100)

    def lambda_4967():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4967)
    Sleep(50)

    def lambda_4977():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4977)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0218
    ChrTalk(
        0x104,
        (
            "#6P#0306F呜……！\x01",
            "您这下还真的说到我的痛处了……\x02\x03",

            "#0301F知、知道了啊！\x01",
            "我参加就行了吧，我参加！\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x9,
        "#11P#2003F……很好。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#6P#0012F（如果今后也一直是这种状况，\x01",
            "　好像会被使唤得很惨呢……）\x02\x03",

            "#0003F嗯，总之，\x01",
            "情况我们大致已经明白了。\x02\x03",

            "#0000F演习……\x01",
            "什么时候开始呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "#11P#2000F只要和队员们说一声\x01",
            "就可以马上开始。\x02\x03",

            "你们\x01",
            "做好战斗的准备了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xF, 0x1, 0x0)
    Call(0, 13)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3000, 0, 0, 90)
    SetChrPos(0x1, 3000, 0, 0, 90)
    SetChrPos(0x2, 3000, 0, 0, 90)
    SetChrPos(0x3, 3000, 0, 0, 90)
    OP_68(3000, 900, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_12_4044 end

    def Function_13_4B9C(): pass

    label("Function_13_4B9C")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还没有准备好】\x01",      # 0
            "【开始演习】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4BDC"),
        (1, "loc_4C52"),
        (SWITCH_DEFAULT, "loc_4D70"),
    )


    label("loc_4BDC")

    OP_60(0x0)

    #C0222
    ChrTalk(
        0x101,
        (
            "#6P#0006F抱歉，\x01",
            "装备方面还有些\x01",
            "小问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x9,
        (
            "#11P#2004F是吗，明白了。\x02\x03",

            "#2000F做好战斗准备后\x01",
            "再叫我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D70")

    label("loc_4C52")

    OP_4B(0x8, 0xFF)
    OP_60(0x0)

    #C0224
    ChrTalk(
        0x101,
        "#6P#0000F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x9,
        (
            "#11P#2004F是吗。\x02\x03",

            "#2000F那么，诺艾尔上士，\x01",
            "带他们去停车场吧。\x02\x03",

            "演习将在那里进行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 300)

    #C0226
    ChrTalk(
        0x8,
        (
            "#5P#0501F明白了。\x02\x03",

            "#0500F那么，\x01",
            "各位请跟我来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【关于参加警备队演习的请求】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x5C, 0)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_4D70")

    label("loc_4D70")

    Return()

    # Function_13_4B9C end

    def Function_14_4D71(): pass

    label("Function_14_4D71")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0xE1, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_68(3870, 1200, -590, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26200, 0)
    SetChrPos(0x101, 3000, 0, 0, 90)
    SetChrPos(0x102, 3000, 0, -1500, 90)
    SetChrPos(0x103, 1500, 0, -1500, 90)
    SetChrPos(0x104, 1500, 0, 0, 90)
    Sleep(500)
    SetCameraDistance(25200, 1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0228
    ChrTalk(
        0x9,
        (
            "#11P#2004F那么……再次\x01",
            "向你们表示感谢。\x02\x03",

            "#2000F谢谢你们协助\x01",
            "我们进行演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#6P#0000F不不……这对我们来说\x01",
            "也是一次很好的经验。\x02\x03",

            "与警备队员战斗这种事，\x01",
            "一般是体验不到的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        (
            "#6P#0109F嗯……\x01",
            "这次演习也给了我们很多启发。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_4FBD")
    OP_2C(0xF, 0x3)

    #C0231
    ChrTalk(
        0x104,
        (
            "#6P#0309F能打赢现役警备队员\x01",
            "真的很痛快啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x103,
        (
            "#6P#0203F你不是很嚣张地\x01",
            "说要给人家当陪练吗，\x01",
            "要是输了岂不是很没面子。\x02\x03",

            "#0200F取胜之后，\x01",
            "兰迪前辈不是也可以安心了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_4FBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_5071")
    OP_2C(0xF, 0x1)

    #C0233
    ChrTalk(
        0x104,
        (
            "#6P#0309F能打赢现役警备队员\x01",
            "真的很痛快啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x103,
        (
            "#6P#0203F不过，在诺艾尔小姐\x01",
            "指挥时确实是输了。\x02\x03",

            "#0200F平时总是摆出一副老资格的\x01",
            "兰迪前辈也觉得很丢人吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5123")

    label("loc_5071")


    #C0235
    ChrTalk(
        0x104,
        (
            "#6P#0300F竟然被现役警备队员打败了，\x01",
            "这让我有点接受不了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x103,
        (
            "#6P#0203F因为你很嚣张地\x01",
            "说要给人家当陪练，\x01",
            "结果却输了呢。\x02\x03",

            "#0200F今晚兰迪前辈一定会\x01",
            "一个人孤寂地哭湿枕头吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5123")


    #C0237
    ChrTalk(
        0x104,
        "#6P#0306F阿缇，你啊……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x8,
        (
            "#5P#0509F啊、啊哈哈……\x01",
            "前辈被说得哑口无言了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x9,
        (
            "#11P#2004F呵呵……\x02\x03",

            "#2000F你们也\x01",
            "继续努力吧。\x02\x03",

            "我们需要帮助时，\x01",
            "会向你们提出支援请求的。\x02\x03",

            "对于特别任务支援科的活动，\x01",
            "我们会在心里默默为你们加油的。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        "#6P#0000F……是，十分感谢！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【关于参加警备队演习的请求】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3000, 0, 0, 90)
    SetChrPos(0x1, 3000, 0, 0, 90)
    SetChrPos(0x2, 3000, 0, 0, 90)
    SetChrPos(0x3, 3000, 0, 0, 90)
    OP_68(3000, 900, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    OP_29(0xF, 0x1, 0x4)
    OP_29(0xF, 0x4, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_4D71 end

    def Function_15_5328(): pass

    label("Function_15_5328")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x9, 0x2)
    OP_68(6140, 900, -20, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24460, 0)
    SetChrPos(0x101, -3000, 0, 0, 90)
    SetChrPos(0x102, -3000, 0, -1500, 90)
    SetChrPos(0x103, -4500, 0, -1500, 90)
    SetChrPos(0x104, -4500, 0, 0, 90)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0242
    ChrTalk(
        0x101,
        "#0000F──打扰了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xE1, 0x1F4)
    SetChrSubChip(0x9, 0x0)
    OP_68(3870, 1200, -590, 5000)
    MoveCamera(55, 17, 0, 5000)
    SetCameraDistance(26200, 5000)
    BeginChrThread(0x101, 3, 0, 16)
    BeginChrThread(0x102, 3, 0, 17)
    BeginChrThread(0x103, 3, 0, 18)
    BeginChrThread(0x104, 3, 0, 19)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    #C0243
    ChrTalk(
        0x101,
        (
            "#0000F辛苦了，\x01",
            "索妮亚副司令、诺艾尔上士。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x8,
        "#5P#0500F辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x9,
        (
            "#11P#2000F辛苦了。\x02\x03",

            "#2001F……你们会特意\x01",
            "跑过来，\x01",
            "是出什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#6P#0001F嗯，其实，\x01",
            "我们有些事想与您商量……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0247
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德说明了来唐古拉姆门的目的\x01",
            "是为了堵截假货贩子。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0248
    ChrTalk(
        0x9,
        (
            "#11P#2003F……原来如此，\x01",
            "情况我已经了解了。\x02\x03",

            "#2000F明白了，\x01",
            "我们唐古拉姆门部队\x01",
            "也会提供协助的。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#6P#0000F感谢你们的协助。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        (
            "#6P#0305F不过，没问题吗？\x02\x03",

            "纪念庆典期间，国境门这边好像\x01",
            "特别忙碌呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "#5P#0500F前辈，请不要在意。\x02\x03",

            "#0503F执行堵截作战本来就是我们这些\x01",
            "守卫国境门的警备队员的工作。\x02\x03",

            "#0500F虽说时间和人手有些不够，\x01",
            "不过我认为我们有参加\x01",
            "的义务。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x9,
        (
            "#11P#2004F嗯，正是如此，\x01",
            "你们并没有必要\x01",
            "为此在意。\x02\x03",

            "#2000F但因为分不出人手，\x01",
            "所以我们所能做的\x01",
            "就只有后援工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        "#6P#0202F即使如此，也很令人安心了。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#6P#0001F那么，事不宜迟……\x01",
            "有没有什么机会能让我们\x01",
            "调查来自共和国的旅行者呢？\x02\x03",

            "#0003F根据警察局总部得到的情报来看，\x01",
            "假货贩子可能将在今天\x01",
            "白天到达……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x9,
        (
            "#11P#2003F嗯，我记得……\x01",
            "来自共和国的巴士\x01",
            "差不多要抵达了。\x02\x03",

            "如果情报准确，恐怕\x01",
            "假货贩子就在\x01",
            "那辆巴士上。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x8,
        (
            "#5P#0501F从旅客巴士换乘克洛斯贝尔\x01",
            "自治州内的巴士时，\x01",
            "其间有一段时间间隔。\x02\x03",

            "在那段时间，我们应该可以\x01",
            "安排旅客们去食堂\x01",
            "稍微休息一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x104,
        (
            "#6P#0300F那么，作战计划就决定了呢。\x02\x03",

            "#0303F上士不露痕迹地引导乘客\x01",
            "们到食堂那边去。\x02\x03",

            "#0300F在那之后，我们\x01",
            "再若无其事地进入食堂\x01",
            "搜寻假货贩子。\x02\x03",

            "#0309F是展现搜查官本领的时候了，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，交给我吧。\x02\x03",

            "虽说时间很短，\x01",
            "但已经足够观察乘客们\x01",
            "并确定目标了。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x103,
        (
            "#6P#0200F我们如果不表明身份，\x01",
            "不知道能不能顺利和他们攀谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        "#6P#0101F不、不知为何，紧张起来了呢……\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x9,
        (
            "#11P#2003F来自共和国方向的巴士\x01",
            "还有一段时间才会抵达。\x02\x03",

            "你们要是在这里等待的话，\x01",
            "应该可以得到充分休息。\x02\x03",

            "#2000F怎么样，要不要\x01",
            "帮你们准备房间呢？\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还没有准备好】\x01",              # 0
            "【等待来自共和国的巴士】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5B53"),
        (1, "loc_5C63"),
        (SWITCH_DEFAULT, "loc_5D22"),
    )


    label("loc_5B53")

    OP_60(0x0)

    #C0262
    ChrTalk(
        0x101,
        (
            "#0003F这样啊……\x01",
            "可以的话，我想稍微做些准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x9,
        (
            "#11P#2000F嗯，明白了。\x02\x03",

            "准备好之后就跟我说一声吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 3000, 0, 0, 90)
    SetChrPos(0x1, 3000, 0, 0, 90)
    SetChrPos(0x2, 3000, 0, 0, 90)
    SetChrPos(0x3, 3000, 0, 0, 90)
    OP_68(3000, 900, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    OP_93(0x8, 0x10E, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    OP_29(0x1B, 0x1, 0x2)
    EventEnd(0x5)
    Jump("loc_5D22")

    label("loc_5C63")

    OP_60(0x0)

    #C0264
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么，承蒙您的好意，\x01",
            "我们就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x9,
        (
            "#11P#2000F明白了。\x02\x03",

            "巴士抵达之后，\x01",
            "我会去叫你们的。\x02\x03",

            "你们就好好休息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        "#6P#0001F好！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1B, 0x1, 0x2)
    OP_29(0x1B, 0x1, 0x3)
    SetScenarioFlags(0x5C, 0)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Jump("loc_5D22")

    label("loc_5D22")

    Return()

    # Function_15_5328 end

    def Function_16_5D23(): pass

    label("Function_16_5D23")


    def lambda_5D28():
        OP_95(0xFE, 3000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D28)
    WaitChrThread(0x101, 1)
    Return()

    # Function_16_5D23 end

    def Function_17_5D42(): pass

    label("Function_17_5D42")


    def lambda_5D47():
        OP_95(0xFE, 3000, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D47)
    WaitChrThread(0x102, 1)
    Return()

    # Function_17_5D42 end

    def Function_18_5D61(): pass

    label("Function_18_5D61")


    def lambda_5D66():
        OP_95(0xFE, 1500, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D66)
    WaitChrThread(0x103, 1)
    Return()

    # Function_18_5D61 end

    def Function_19_5D80(): pass

    label("Function_19_5D80")


    def lambda_5D85():
        OP_95(0xFE, 1500, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5D85)
    WaitChrThread(0x104, 1)
    Return()

    # Function_19_5D80 end

    def Function_20_5D9F(): pass

    label("Function_20_5D9F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F84")

    #C0267
    ChrTalk(
        0x103,
        (
            "#0205F这个玩偶……\x02\x03",

            "#0203F……这个外形，\x01",
            "好像在哪里见过。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x109,
        (
            "#0509F啊哈哈……\x01",
            "这是我的私人物品。\x02\x03",

            "#0500F其实是芙兰\x01",
            "送给我用来\x01",
            "装饰宿舍的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E94")

    #C0269
    ChrTalk(
        0x101,
        (
            "#0002F啊，这么说来……\x01",
            "这个和芙兰的玩偶\x01",
            "颜色不同，款式一样呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EF6")

    label("loc_5E94")


    #C0270
    ChrTalk(
        0x101,
        (
            "#0005F啊，这么说来……\x02\x03",

            "#0002F以前拜访芙兰家时，\x01",
            "好像见过与这个颜色不同，\x01",
            "款式一样的玩偶呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EF6")


    #C0271
    ChrTalk(
        0x104,
        "#0309F哈哈，应该是一对的吧。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x102,
        (
            "#0104F姐妹关系真好呢，\x01",
            "我都有点羡慕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x109,
        (
            "#0509F是、是、是这样吗？\x01",
            "（总觉得有点难为情……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 2)
    Jump("loc_5FFC")

    label("loc_5F84")

    SetChrName("")

    #A0274
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "诺艾尔的玩偶。\x01",
            "与芙兰的玩偶好像是一对。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0275
    ChrTalk(
        0x109,
        (
            "#0506F（总觉得有点不好意思……\x01",
            "  要是提前收起来\x01",
            "  就好了啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FFC")

    TalkEnd(0xFF)
    Return()

    # Function_20_5D9F end

    SaveToFile()

Try(main)
