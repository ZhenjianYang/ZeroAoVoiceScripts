from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1310.bin",                # FileName
        "c1310",                    # MapName
        "c1310",                    # Location
        0x001C,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 300, 5000, 0, 0, 1, 28, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1310",                  # 0
        "警备员汪古",             # 1
        "警备员珀尔",             # 2
        "接待小姐兰菲",           # 3
        "接待小姐柯琳娜",         # 4
        "贸易商利泽罗",           # 5
        "研究员",                 # 6
        "罗伯兹主任",             # 7
        "市民",                   # 8
        "市民",                   # 9
        "游击士斯克特",           # 10
        "游击士温蔡尔",           # 11
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch27900.itc",                   # 01
        "chr/ch30500.itc",                   # 02
        "chr/ch27702.itc",                   # 03
        "chr/ch32800.itc",                   # 04
        "chr/ch29300.itc",                   # 05
        "chr/ch20900.itc",                   # 06
        "chr/ch20902.itc",                   # 07
        "chr/ch27200.itc",                   # 08
        "chr/ch27300.itc",                   # 09
    ))

    DeclNpc(8500,    0,       13310,   270,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-5730,   300,     29909,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       300,     31700,   180,  257,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(7110,    300,     32759,   90,   257,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-4840,   0,       18180,   90,   341,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(5000,    0,       17850,   90,   257,  0x0, 0,   4,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(6500,    0,       17850,   270,  257,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(6570,    300,     29760,   0,    257,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(8210,    300,     28309,   270,  469,  0x0, 0,   7,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(1820,    300,     25760,   315,  389,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(3220,    300,     25959,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)

    DeclEvent(0x0000, 0, 25,  9.5,                   16.0,                  -0.5,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -4.75,                 -5.333333492279053,    0.10000000894069672,   1.0])

    DeclActor(0,       300,     30300,   1500,    0,       1800,    31700,   0x007E, 0,  6,  0x0000)
    DeclActor(6650,    300,     31080,   1500,    7110,    1800,    32759,   0x007E, 0,  9,  0x0000)

    ScpFunction((
        "Function_0_300",          # 00, 0
        "Function_1_3B8",          # 01, 1
        "Function_2_5E3",          # 02, 2
        "Function_3_5EA",          # 03, 3
        "Function_4_684",          # 04, 4
        "Function_5_13AA",         # 05, 5
        "Function_6_216B",         # 06, 6
        "Function_7_216F",         # 07, 7
        "Function_8_27D4",         # 08, 8
        "Function_9_401A",         # 09, 9
        "Function_10_401E",        # 0A, 10
        "Function_11_4FF9",        # 0B, 11
        "Function_12_5F4A",        # 0C, 12
        "Function_13_666C",        # 0D, 13
        "Function_14_6949",        # 0E, 14
        "Function_15_6A21",        # 0F, 15
        "Function_16_70AC",        # 10, 16
        "Function_17_7121",        # 11, 17
        "Function_18_7238",        # 12, 18
        "Function_19_736D",        # 13, 19
        "Function_20_756D",        # 14, 20
        "Function_21_81DC",        # 15, 21
        "Function_22_8E80",        # 16, 22
        "Function_23_9574",        # 17, 23
        "Function_24_97DC",        # 18, 24
        "Function_25_9B79",        # 19, 25
    ))


    def Function_0_300(): pass

    label("Function_0_300")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_340"),
        (1, "loc_34C"),
        (2, "loc_358"),
        (3, "loc_364"),
        (4, "loc_370"),
        (5, "loc_37C"),
        (6, "loc_388"),
        (SWITCH_DEFAULT, "loc_394"),
    )


    label("loc_340")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_34C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_358")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_364")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_370")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_37C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_388")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_394")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_3A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_3B7")

    Return()

    # Function_0_300 end

    def Function_1_3B8(): pass

    label("Function_1_3B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D0")
    ClearScenarioFlags(0x5F, 1)
    Event(0, 2)

    label("loc_3D0")

    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_41E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_414")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1080, 300, 29510, 0)
    SetChrFlags(0xE, 0x10)

    label("loc_414")

    SetChrFlags(0xC, 0x80)
    Jump("loc_5C1")

    label("loc_41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_42C")
    Jump("loc_5C1")

    label("loc_42C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_43A")
    Jump("loc_5C1")

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_448")
    Jump("loc_5C1")

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_45B")
    SetChrFlags(0xC, 0x10)
    Jump("loc_5C1")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_46E")
    SetChrFlags(0xC, 0x10)
    Jump("loc_5C1")

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_486")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_5C1")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_494")
    Jump("loc_5C1")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4B8")
    SetChrPos(0xB, 7110, 300, 32759, 90)
    SetChrFlags(0xB, 0x10)
    Jump("loc_5C1")

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4C6")
    Jump("loc_5C1")

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrPos(0xB, 7110, 300, 32759, 90)
    SetChrFlags(0xB, 0x10)
    Jump("loc_5C1")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4F8")
    Jump("loc_5C1")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_53E")
    SetChrPos(0xB, 7110, 300, 32759, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 4)), scpexpr(EXPR_END)), "loc_539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)

    label("loc_539")

    Jump("loc_5C1")

    label("loc_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 4)), scpexpr(EXPR_END)), "loc_564")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)

    label("loc_564")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xB, 7110, 300, 32759, 90)
    SetChrFlags(0xB, 0x10)
    Jump("loc_5C1")

    label("loc_584")

    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 4)), scpexpr(EXPR_END)), "loc_5A1")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)

    label("loc_5A1")

    SetChrPos(0xB, 7110, 300, 32759, 90)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_5C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E2")
    Event(0, 23)

    label("loc_5E2")

    Return()

    # Function_1_3B8 end

    def Function_2_5E3(): pass

    label("Function_2_5E3")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_5E3 end

    def Function_3_5EA(): pass

    label("Function_3_5EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_603")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_609")

    label("loc_603")

    OP_10(0x0, 0x1)
    OP_10(0x2, 0x0)

    label("loc_609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_620")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63C")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_653")

    label("loc_63C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_653")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_653")

    label("loc_653")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_683")
    OP_1B(0x0, 0x0, 0xD)

    label("loc_683")

    Return()

    # Function_3_5EA end

    def Function_4_684(): pass

    label("Function_4_684")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6D0")

    #C0001
    ChrTalk(
        0xFE,
        (
            "嗯……感觉今天的\x01",
            "客人很少啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "大概是我的错觉吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13A6")

    label("loc_6D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_74B")

    #C0003
    ChrTalk(
        0xFE,
        (
            "避免让客人感到不安，\x01",
            "也是我们警备员的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "虽然发生了枪击事件，\x01",
            "但ＩＢＣ还是绝对安全的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BF")

    label("loc_74B")


    #C0005
    ChrTalk(
        0xFE,
        (
            "今天的警备员人数\x01",
            "比平时增加了两成左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "……因为听说港湾公园那边\x01",
            "发生了暴力事件呢。\x01",
            "还是小心一点为好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_7BF")

    Jump("loc_13A6")

    label("loc_7C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_90A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_859")

    #C0007
    ChrTalk(
        0xFE,
        (
            "我们保安部正在对\x01",
            "全世界的主要都市进行\x01",
            "治安等级的评定。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "为了保护好经常飞往世界\x01",
            "各地的库罗伊斯总裁，\x01",
            "这是十分必要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_905")

    label("loc_859")


    #C0009
    ChrTalk(
        0xFE,
        (
            "就在最近这两三个星期，\x01",
            "市内的治安等级有所恶化。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "按照我们保安部的评定标准，\x01",
            "都已经降到Ｃ级了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "像那些人烟稀少的小胡同是很危险的，\x01",
            "希望市民们也能多加注意。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_905")

    Jump("loc_13A6")

    label("loc_90A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_95A")

    #C0012
    ChrTalk(
        0xFE,
        (
            "作为警备员，绝对不能疏忽大意。\x01",
            "必须要时刻提高警惕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BB")

    label("loc_95A")


    #C0013
    ChrTalk(
        0xFE,
        "今天就是庆典的最终日了啊。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "正是在这种时候，\x01",
            "才最容易发生麻烦呢。\x01",
            "必须要提高警惕啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_9BB")

    Jump("loc_13A6")

    label("loc_9C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_A11")

    #C0015
    ChrTalk(
        0xFE,
        (
            "听说那些高层人员\x01",
            "今天一整天都要开会。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "嗯，真令人同情啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13A6")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AAA")

    #C0017
    ChrTalk(
        0xFE,
        (
            "虽然表面上是一片庆典期间的欢庆景象，\x01",
            "但克洛斯贝尔的治安仍然不能算很好。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "希望那些游客不要迷路，\x01",
            "然后被卷入什么事件中啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4C")

    label("loc_AAA")


    #C0019
    ChrTalk(
        0xFE,
        (
            "根据我们保安部的报告，\x01",
            "克洛斯贝尔市内的治安等级\x01",
            "好像再次下降了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "唔……警察们都在干什么啊。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "如果恶化程度太过严重，\x01",
            "我们也有必要强化保安体制了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B4C")

    Jump("loc_13A6")

    label("loc_B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BA2")

    #C0022
    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "如果没有认证卡片，\x01",
            "就无法启动导力梯啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C14")

    label("loc_BA2")


    #C0023
    ChrTalk(
        0xFE,
        (
            "之前有个陌生的客人\x01",
            "想来乘坐导力梯。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，那些讨厌的游客。\x01",
            "明明都和他们说过，\x01",
            "这里是禁止通行的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C14")

    Jump("loc_13A6")

    label("loc_C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C75")

    #C0025
    ChrTalk(
        0xFE,
        (
            "听说港湾公园那边\x01",
            "相当拥挤啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "客人比平时更多……\x01",
            "警备工作也要重视。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A6")

    label("loc_C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_CF5")

    #C0027
    ChrTalk(
        0xFE,
        (
            "这座大楼的\x01",
            "安全系统是\x01",
            "完全独立的。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "不管是遭受黑客入侵也好，\x01",
            "还是别的什么攻击也好，\x01",
            "应该都不会有问题的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A6")

    label("loc_CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_DB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_END)), "loc_D51")

    #C0029
    ChrTalk(
        0xFE,
        "有事要去上层吗？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "如果想乘坐导力梯，\x01",
            "只要使用认证卡片就好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB1")

    label("loc_D51")


    #C0031
    ChrTalk(
        0xFE,
        (
            "嗯……上面的楼层\x01",
            "是禁止无关人员前往的。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "如果有什么事情，\x01",
            "请先去综合服务台申请许可吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB1")

    Jump("loc_13A6")

    label("loc_DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_F09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8F")

    #C0033
    ChrTalk(
        0xFE,
        (
            "嗯，克洛斯贝尔周边地区\x01",
            "的治安等级似乎开始下降了……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "目前虽然还没有牵扯到\x01",
            "那些重大的问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "但在这自治州，并没有任何\x01",
            "管制雇佣兵方面的法律。\x01",
            "……所以任何事情都有可能发生呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F04")

    label("loc_E8F")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    #C0036
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市这片地区\x01",
            "其实是非常复杂的。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "绝对称不上是安全……\x01",
            "我们也必须提高警惕啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F04")

    Jump("loc_13A6")

    label("loc_F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_102B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F71")

    #C0038
    ChrTalk(
        0xFE,
        (
            "随着公司规模的扩大，\x01",
            "需要守卫的东西也会增加。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        "每个企业好像都很辛苦呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1026")

    label("loc_F71")


    #C0040
    ChrTalk(
        0xFE,
        (
            "最近有外国企业来找\x01",
            "我们保安部进行洽谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "有些是想委托我们对ＶＩＰ进行护卫，\x01",
            "有些是想请教警备工作的诀窍，\x01",
            "总之什么事情都有。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "不管是哪个公司，\x01",
            "保安工作都是很辛苦的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1026")

    Jump("loc_13A6")

    label("loc_102B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1170")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10AF")

    #C0043
    ChrTalk(
        0xFE,
        (
            "……你知道吗？\x01",
            "在这里的地下一层，\x01",
            "有个很大的员工食堂呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "咳咳，不，没什么。\x01",
            "现在还是执勤时间呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116B")

    label("loc_10AF")


    #C0045
    ChrTalk(
        0xFE,
        (
            "我为了保持自己的体力充沛，\x01",
            "每天早上都要跑１００赛尔矩。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "为了应对关键时刻，\x01",
            "平时就必须保持锻炼。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "……可是，一旦晨跑的话，\x01",
            "肚子饿得就会很快……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "咳咳，不，没什么啦……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_116B")

    Jump("loc_13A6")

    label("loc_1170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_12D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11D7")

    #C0049
    ChrTalk(
        0xFE,
        (
            "这座大楼是整个大陆中\x01",
            "安全系数最高的地方了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "在里面可以放心地\x01",
            "谈生意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CF")

    label("loc_11D7")


    #C0051
    ChrTalk(
        0xFE,
        (
            "这座大楼是整个大陆中\x01",
            "安全系数最高的地方了，\x01",
            "我们也引以为荣。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "这是一座重视防卫机能的近代建筑。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "使用了以导力技术为基础的\x01",
            "最新安全系统。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "而且，我们这些保安部的人\x01",
            "也都是受过正式训练的专业人士。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "任何邪恶之徒\x01",
            "都无法侵入这里。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_12CF")

    Jump("loc_13A6")

    label("loc_12D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1324")

    #C0056
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ大楼内的保安工作\x01",
            "就交给我们吧。\x01",
            "我们毕竟也是专业人士。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A6")

    label("loc_1324")


    #C0057
    ChrTalk(
        0xFE,
        (
            "哦，那个夹克……\x01",
            "你们是警察局的人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "我们是在ＩＢＣ集团\x01",
            "供职的保安人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ大楼内的保安工作\x01",
            "就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_13A6")

    TalkEnd(0xFE)
    Return()

    # Function_4_684 end

    def Function_5_13AA(): pass

    label("Function_5_13AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1481")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_140F")

    #C0060
    ChrTalk(
        0xFE,
        (
            "库罗伊斯总裁和\x01",
            "玛丽亚贝尔小姐今天都出差了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "感觉稍微有点寂寞呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_147C")

    label("loc_140F")


    #C0062
    ChrTalk(
        0xFE,
        (
            "玛丽亚贝尔小姐今天\x01",
            "出差去国外了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "她的出差次数\x01",
            "好像也在逐年增加呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        "越来越像她的父亲了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_147C")

    Jump("loc_2167")

    label("loc_1481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1501")

    #C0065
    ChrTalk(
        0xFE,
        (
            "是我的心理作用吗，\x01",
            "感觉今天的客人好像变少了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "呼……就算是我们，也不可能\x01",
            "将警备工作延伸到大楼外面啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2167")

    label("loc_1501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1643")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1565")

    #C0067
    ChrTalk(
        0xFE,
        (
            "是因为纪念庆典吗，\x01",
            "最近似乎有很多新企业前来驻扎。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        "我也有些在意呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_163E")

    label("loc_1565")


    #C0069
    ChrTalk(
        0xFE,
        (
            "莱恩福尔特公司的\x01",
            "营业部就入驻在\x01",
            "这座大楼中……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "但就在最近，他们的竞争对手\x01",
            "乌尔努公司好像也准备在此\x01",
            "设立分部，还前来商谈了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "嗯～早就听说过这两个公司\x01",
            "处处都要对立竞争，现在一看，\x01",
            "确实是互不相让啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_163E")

    Jump("loc_2167")

    label("loc_1643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_173C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16D3")

    #C0072
    ChrTalk(
        0xFE,
        (
            "虽然新闻媒体很少会报道……\x01",
            "但克洛斯贝尔过去也曾\x01",
            "发生过一些恐怖事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "纪念庆典要是能顺利结束，\x01",
            "那就再好不过了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1737")

    label("loc_16D3")


    #C0074
    ChrTalk(
        0xFE,
        "纪念庆典今天要结束了啊……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "虽然没能出去游玩稍微有些遗憾，\x01",
            "不过算了，没出什么事情就好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1737")

    Jump("loc_2167")

    label("loc_173C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_17AF")

    #C0076
    ChrTalk(
        0xFE,
        (
            "不久前，玛丽亚贝尔小姐\x01",
            "来看我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "对我们这些平时辛苦工作\x01",
            "的职员表示了慰问，\x01",
            "我真开心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2167")

    label("loc_17AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_18C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_181A")

    #C0078
    ChrTalk(
        0xFE,
        (
            "你听说过米修拉姆\x01",
            "的奇幻乐园吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "据说那里的吉祥物是\x01",
            "一只名叫『咪西』的猫。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BF")

    label("loc_181A")


    #C0080
    ChrTalk(
        0xFE,
        (
            "位于艾鲁姆湖对岸的\x01",
            "米修拉姆中有一座\x01",
            "主题公园。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "那里是由ＩＢＣ出资建造的，\x01",
            "很多人都喜欢全家一起去那里游玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "纪念庆典期间，\x01",
            "那里肯定也会相当热闹吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_18BF")

    Jump("loc_2167")

    label("loc_18C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_19B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1906")

    #C0083
    ChrTalk(
        0xFE,
        (
            "但和市内比起来，\x01",
            "那里也许还算安静吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19AD")

    label("loc_1906")


    #C0084
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，也有不少\x01",
            "从国外赶来的游客。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "我昨天还给好几个人\x01",
            "指了路……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0086
    ChrTalk(
        0xFE,
        (
            "但对这里一无所知的游客这么多，\x01",
            "确实是很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_19AD")

    Jump("loc_2167")

    label("loc_19B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A19")

    #C0087
    ChrTalk(
        0xFE,
        (
            "不知为何，罗伯兹主任\x01",
            "好像很开心……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "是不是在工作中\x01",
            "遇到了什么好事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8A")

    label("loc_1A19")


    #C0089
    ChrTalk(
        0xFE,
        (
            "我之前和爱普斯泰恩财团\x01",
            "的罗伯兹主任打了个招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "他一脸高兴地\x01",
            "出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "大概是遇到什么好事了吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1A8A")

    Jump("loc_2167")

    label("loc_1A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1BD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B05")

    #C0092
    ChrTalk(
        0xFE,
        (
            "玛丽亚贝尔小姐如此年轻，\x01",
            "就已经成功接管了\x01",
            "好几项业务。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "真不愧是库罗伊斯总裁\x01",
            "的千金。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD3")

    label("loc_1B05")


    #C0094
    ChrTalk(
        0xFE,
        (
            "玛丽亚贝尔小姐\x01",
            "是ＩＢＣ集团的\x01",
            "董事会成员之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "虽然并不直接负责\x01",
            "公司的运营工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "但年纪轻轻，就接手了多项业务，\x01",
            "并且经营得有声有色。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "我们也怀着对小姐的敬意，\x01",
            "全心做好她的警卫工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1BD3")

    Jump("loc_2167")

    label("loc_1BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1C3A")

    #C0098
    ChrTalk(
        0xFE,
        "今天也没有异常状况。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "因为ＩＢＣ总部大楼的警备体制\x01",
            "堪称万无一失。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8A")

    label("loc_1C3A")


    #C0100
    ChrTalk(
        0xFE,
        "今天也没有异常状况。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ总部大楼自从开业以来，\x01",
            "一直都平安无事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1C8A")

    Jump("loc_2167")

    label("loc_1C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1CDE")

    #C0102
    ChrTalk(
        0xFE,
        (
            "今天是ＩＢＣ集团\x01",
            "的高层会议召开日。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        "警备工作也要做好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2167")

    label("loc_1CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1DB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1D5D")

    #C0104
    ChrTalk(
        0xFE,
        (
            "我们保安部要对周围各国的各个地区\x01",
            "进行治安等级的详细评定。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "因为库罗伊斯总裁\x01",
            "经常要到各地出差。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAE")

    label("loc_1D5D")


    #C0106
    ChrTalk(
        0xFE,
        (
            "最近，市内的治安等级\x01",
            "好像有所下降呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "我们也必须要\x01",
            "多加注意才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1DAE")

    Jump("loc_2167")

    label("loc_1DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1EF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E37")

    #C0108
    ChrTalk(
        0xFE,
        (
            "只要到柜台办理手续，\x01",
            "无论从哪个国家的账户中\x01",
            "都可以取出米拉。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "……啊，我并没打算\x01",
            "要带你们去柜台啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEE")

    label("loc_1E37")


    #C0110
    ChrTalk(
        0xFE,
        (
            "我们ＩＢＣ银行\x01",
            "在全世界中有许多分部。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "旗下的银行也非常多，现在已经\x01",
            "成为全世界最大的银行网络了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "只要在这里的柜台办理手续，\x01",
            "无论从哪个国家的账户中\x01",
            "都可以取出米拉哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1EEE")

    Jump("loc_2167")

    label("loc_1EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2037")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F88")

    #C0113
    ChrTalk(
        0xFE,
        (
            "即使是在现代化程度如此高的克洛斯贝尔地区，\x01",
            "也一样会有魔兽侵害的事件发生啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "我们这些警备公司的人\x01",
            "也应该提高警惕呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2032")

    label("loc_1F88")


    #C0115
    ChrTalk(
        0xFE,
        (
            "魔兽好像出没于\x01",
            "各个地区呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        "我们公司的人也发来了联络。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "据说乌尔斯拉医科大学\x01",
            "那边也有实习生受到了袭击……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "受害者当时肯定很害怕吧，\x01",
            "真是非常同情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2032")

    Jump("loc_2167")

    label("loc_2037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_20BB")

    #C0119
    ChrTalk(
        0xFE,
        (
            "因为我在接待窗口附近守备，\x01",
            "所以经常会有客人向我询问。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "那个，如果想确认您的账户的话，\x01",
            "可以去服务柜台查询哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2167")

    label("loc_20BB")


    #C0121
    ChrTalk(
        0xFE,
        (
            "欢迎。\x01",
            "欢迎光临克洛斯贝尔国际银行。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "……我在这里就任已经有两年了，\x01",
            "经常引领顾客前往服务台。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "大概是因为一直都待在接待窗口的旁边吧，\x01",
            "经常会有顾客向我咨询。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2167")

    TalkEnd(0xFE)
    Return()

    # Function_5_13AA end

    def Function_6_216B(): pass

    label("Function_6_216B")

    Call(0, 7)
    Return()

    # Function_6_216B end

    def Function_7_216F(): pass

    label("Function_7_216F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2186")
    Call(0, 20)
    Return()

    label("loc_2186")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21B5")
    Call(0, 24)
    Return()

    label("loc_21B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D6")
    Call(0, 21)
    Return()

    label("loc_21D6")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2529")

    #C0124
    ChrTalk(
        0xA,
        (
            "欢迎。\x01",
            "欢迎光临克洛斯贝尔国际银行。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xA, 0x102, 500)

    #C0125
    ChrTalk(
        0xA,
        "啊呀，那位是……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "果然是艾莉小姐啊！\x01",
            "真是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#0005F（哎……？）\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        "#0205F（艾莉前辈……？）\x02",
    )

    CloseMessageWindow()

    def lambda_22A7():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22A7)

    def lambda_22B4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_22B4)

    def lambda_22C1():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22C1)
    Sleep(300)

    #C0129
    ChrTalk(
        0x102,
        (
            "#0100F您好，兰菲小姐。\x01",
            "真是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "自从您外出留学以来，\x01",
            "这还是第一次见面吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        (
            "……对了，\x01",
            "要不要我马上通知\x01",
            "玛丽亚贝尔小姐呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "虽然很不巧，她刚刚去米修拉姆\x01",
            "进行视察了。但如果通知她，\x01",
            "我想她一定会很乐意回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        (
            "#0104F呵呵……贝尔一点都没变，\x01",
            "还是那么忙啊。\x02\x03",

            "#0100F先不用了，我今天\x01",
            "也没有什么事情要找贝尔。\x02\x03",

            "还是改日再来拜访吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "是吗……\x01",
            "那么，我会把原话传达给她的。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0135
    ChrTalk(
        0x104,
        (
            "#0305F（大小姐……竟然和ＩＢＣ\x01",
            "  的人有来往吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#0005F（而且关系好像还\x01",
            "  相当亲近呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x103,
        (
            "#0203F（小声）果然是个真正的\x01",
            "  大小姐呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    #C0138
    ChrTalk(
        0x102,
        "#0113F……那个，我都听到了哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 4)
    Jump("loc_27D0")

    label("loc_2529")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26EB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2550")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E6")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "换钱\x01",              # 1
            "询问委托事宜\x01",      # 2
            "放弃\x01",              # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25AD")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_25AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E0")
    OP_AF(0xB5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 2)), scpexpr(EXPR_END)), "loc_25DB")
    Sleep(100)
    Call(0, 22)
    TalkEnd(0xA)
    Return()

    label("loc_25DB")

    Jump("loc_26E1")

    label("loc_25E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B1")

    #C0139
    ChrTalk(
        0xA,
        (
            "为了实际确认本项新业务，\x01",
            "希望各位能正式使用一下\x01",
            "我们的兑换服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "全部七种的耀晶片，\x01",
            "每种各三十个……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "用这个数量的耀晶片来兑换，\x01",
            "我想应该就足够了。\x01",
            "那就拜托各位了。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26E1")

    label("loc_26B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C5")
    Jump("loc_26E1")

    label("loc_26C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)

    label("loc_26E1")

    Jump("loc_2550")

    label("loc_26E6")

    Jump("loc_27D0")

    label("loc_26EB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D0")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "换钱\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2745")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2745")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_279B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2777")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2770")
    OP_AF(0xB7)
    Jump("loc_2772")

    label("loc_2770")

    OP_AF(0xB6)

    label("loc_2772")

    Jump("loc_278C")

    label("loc_2777")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_278A")
    OP_AF(0xB5)
    Jump("loc_278C")

    label("loc_278A")

    OP_AF(0xB4)

    label("loc_278C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27CB")

    label("loc_279B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27AF")
    Jump("loc_27CB")

    label("loc_27AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27CB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)

    label("loc_27CB")

    Jump("loc_26F5")

    label("loc_27D0")

    TalkEnd(0xA)
    Return()

    # Function_7_216F end

    def Function_8_27D4(): pass

    label("Function_8_27D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28FB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2888")

    #C0142
    ChrTalk(
        0xA,
        (
            "卡拉小姐好像向那位女仆\x01",
            "提出了很多指示呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "比如说，预订格兰赛尔\x01",
            "的酒店房间……之类的。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "她在大厅时，说话的声音\x01",
            "也很大。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F6")

    label("loc_2888")


    #C0145
    ChrTalk(
        0xA,
        "会议刚刚结束了……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        (
            "玛丽亚贝尔小姐现在\x01",
            "应该在总裁室呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        (
            "想找她的话，请乘坐导力梯\x01",
            "前往十六层吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F6")

    Jump("loc_4019")

    label("loc_28FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_29DF")

    #C0148
    ChrTalk(
        0xA,
        (
            "今天真是感谢\x01",
            "各位的协助了。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xA,
        (
            "如此一来，我们的新服务\x01",
            "应该就可以顺利施行了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "交给各位的那张卡片\x01",
            "已经正式生效了，\x01",
            "请善加利用。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#0000F哈哈……我们一定会好好使用的。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x104,
        "#0300F真是惊人的ＩＢＣ啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4019")

    label("loc_29DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A84")

    #C0153
    ChrTalk(
        0xA,
        (
            "听市政府的相关人员说，\x01",
            "克洛斯贝尔的空港好像\x01",
            "已经临时闭港了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        (
            "呼，虽然这次对我们\x01",
            "应该没什么影响……\x01",
            "不过事出突然，还真是吃了一惊啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B16")

    label("loc_2A84")


    #C0155
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔空港今天因为要临时检查，\x01",
            "好像要暂时闭港呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xA,
        (
            "呼，不过总裁和玛丽亚贝尔小姐\x01",
            "都已经出差去共和国那边了，\x01",
            "应该不会受什么影响……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2B16")

    Jump("loc_4019")

    label("loc_2B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2B94")

    #C0157
    ChrTalk(
        0xA,
        (
            "玛丽亚贝尔小姐已经和高层领导们\x01",
            "开过无数次协商会议了。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xA,
        (
            "但愿股价不要因此\x01",
            "而受到影响啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB5")

    label("loc_2B94")


    #C0159
    ChrTalk(
        0xA,
        (
            "这可该如何是好呢，\x01",
            "竟然在库罗伊斯总裁不在的时候……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#0000F是指港湾区的事件吧？\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#0100F兰菲小姐，这边\x01",
            "没出什么事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xA,
        (
            "嗯，我们虽然没受到\x01",
            "直接的实质性伤害。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "不过股价这种东西\x01",
            "可是相当敏感的……\x01",
            "说不定会受到什么影响呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        (
            "现在，高层领导们好像\x01",
            "正在进行协商会议呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2CB5")

    Jump("loc_4019")

    label("loc_2CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2D17")

    #C0165
    ChrTalk(
        0xA,
        (
            "库罗伊斯总裁\x01",
            "究竟在做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xA,
        (
            "明明说过\x01",
            "傍晚还有商谈计划的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E3E")

    label("loc_2D17")


    #C0167
    ChrTalk(
        0xA,
        (
            "啊，艾莉小姐，\x01",
            "您来得正巧呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "长期出差的库罗伊斯总裁\x01",
            "今天就要回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "……这个时间的话，\x01",
            "差不多也该到了…………\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_END)), "loc_2E3B")

    #C0170
    ChrTalk(
        0x102,
        (
            "#0100F啊哈哈……\x01",
            "其实我刚才在大楼前\x01",
            "就看到叔叔了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0171
    ChrTalk(
        0xA,
        "啊，是吗？\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "不过，总裁究竟在做什么呢，\x01",
            "是有什么很重要的事情吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E3B")

    SetScenarioFlags(0x0, 2)

    label("loc_2E3E")

    Jump("loc_4019")

    label("loc_2E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2E9D")

    #C0173
    ChrTalk(
        0xA,
        (
            "总裁今天也\x01",
            "出差了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        (
            "实在非常抱歉。\x01",
            "我想，他过几天就会回来了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4019")

    label("loc_2E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2FFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2F39")

    #C0175
    ChrTalk(
        0xA,
        (
            "按照日程安排，库罗伊斯总裁\x01",
            "从今晚开始就要出席各种庆祝会，\x01",
            "此外还有各种出差计划……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xA,
        (
            "在短时间之内，恐怕是\x01",
            "没机会见到他了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF9")

    label("loc_2F39")


    #C0177
    ChrTalk(
        0xA,
        (
            "玛丽亚贝尔小姐\x01",
            "刚才来过这里，\x01",
            "高层会议好像已经结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "不过，从今天晚上开始，\x01",
            "总裁就要出席各种庆祝会，\x01",
            "还要应付各种出差事务……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xA,
        (
            "在短时间之内，恐怕是\x01",
            "很难有机会见到他了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2FF9")

    Jump("loc_4019")

    label("loc_2FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3138")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3083")

    #C0180
    ChrTalk(
        0xA,
        (
            "说起来……今天好像\x01",
            "从一早开始就一直在开会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xA,
        (
            "明明是纪念庆典，却还要如此忙碌，\x01",
            "总裁也这样抱怨过哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3133")

    label("loc_3083")


    #C0182
    ChrTalk(
        0xA,
        (
            "今天的客人也很多，\x01",
            "但柯琳娜的工作效率很高，\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        (
            "只是……她的原则就是，\x01",
            "无论有多忙，都不\x01",
            "缩减休息时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xA,
        (
            "呼，只要一到了休息时间，\x01",
            "她就会消失不见呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3133")

    Jump("loc_4019")

    label("loc_3138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_325C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_31BA")

    #C0185
    ChrTalk(
        0xA,
        (
            "总裁和玛丽亚贝尔小姐\x01",
            "今天都不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        (
            "艾莉小姐，您若有什么要事，\x01",
            "可以去乌尔斯拉医科大学\x01",
            "那边看看哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3257")

    label("loc_31BA")


    #C0187
    ChrTalk(
        0xA,
        (
            "欢迎。\x01",
            "欢迎光临克洛斯贝尔国际银行。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        (
            "总裁和玛丽亚贝尔小姐\x01",
            "今天都不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        (
            "如果想找他们，\x01",
            "可以去乌尔斯拉医科大学哦。\x01",
            "他们现在应该已经到那边了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3257")

    Jump("loc_4019")

    label("loc_325C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_348D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 2)), scpexpr(EXPR_END)), "loc_32BA")

    #C0190
    ChrTalk(
        0xA,
        (
            "玛丽亚贝尔小姐现在\x01",
            "就在房间里哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xA,
        "现在去的话，应该能见到她。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3488")

    label("loc_32BA")


    #C0192
    ChrTalk(
        0xA,
        (
            "欢迎。\x01",
            "欢迎光临克洛斯贝尔国际银行──\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        "啊，是各位啊。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔迎来了创立七十周年纪念，\x01",
            "祝大家节日快乐哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x102,
        (
            "#0100F谢谢你。\x02\x03",

            "兰菲小姐好像\x01",
            "也很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xA,
        (
            "嗯，因为创立纪念庆典只是\x01",
            "克洛斯贝尔地区范围内的节日。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xA,
        (
            "我们作为国际性的银行，\x01",
            "自然是不能停止工作的。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xA,
        "全天都要正常营业呢。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        "#0006F那、那可真是很辛苦啊。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xA,
        (
            "呵呵，等到纪念庆典结束之后，\x01",
            "也会有倒休补假的，请不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xA,
        (
            "如果想使用银行服务项目，\x01",
            "请不用客气，随意吩咐便可。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 2)

    label("loc_3488")

    Jump("loc_4019")

    label("loc_348D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_35FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3509")

    #C0202
    ChrTalk(
        0xA,
        (
            "总裁出差了，\x01",
            "现在不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xA,
        (
            "玛丽亚贝尔小姐的话，\x01",
            "现在应该在自己的房间里。\x01",
            "请各位去那里找她吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35F9")

    label("loc_3509")


    #C0204
    ChrTalk(
        0xA,
        (
            "总裁出差了，\x01",
            "现在不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xA,
        (
            "我想，大概要过两个星期\x01",
            "左右才能回来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        "#0100F叔叔果然很忙啊……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xA,
        (
            "嗯，最近这几年来，\x01",
            "为了与国外的银行合作，\x01",
            "他付出了相当多的精力。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xA,
        (
            "一直过着常年奔波于各个国家，\x01",
            "偶尔才能回来一次的劳顿生活。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_35F9")

    Jump("loc_4019")

    label("loc_35FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_376C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_365D")

    #C0209
    ChrTalk(
        0xA,
        (
            "艾莉小姐，\x01",
            "欢迎您下次再来。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xA,
        (
            "玛丽亚贝尔小姐\x01",
            "肯定也会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3767")

    label("loc_365D")


    #C0211
    ChrTalk(
        0xA,
        (
            "太好了，\x01",
            "各位好像也见到\x01",
            "玛丽亚贝尔小姐了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xA,
        (
            "艾莉小姐，\x01",
            "认证卡片会一直有效，\x01",
            "今后还请随时光临哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xA,
        (
            "玛丽亚贝尔小姐\x01",
            "肯定也会很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        (
            "#0006F以她刚才的态度来看，\x01",
            "只要一见面，肯定就又会被缠住吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        (
            "#0106F嗯、嗯～……\x01",
            "（贝尔真是太强势了……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3767")

    Jump("loc_4019")

    label("loc_376C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_37D2")

    #C0216
    ChrTalk(
        0xA,
        (
            "总裁同意见你们，\x01",
            "请各位前往最上层的总裁室吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xA,
        (
            "导力梯就在这个大厅\x01",
            "的右侧位置。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4019")

    label("loc_37D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_394D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_387E")

    #C0218
    ChrTalk(
        0xA,
        (
            "只要一到了休息时间，\x01",
            "柯琳娜就会马上消失不见。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xA,
        (
            "连接待客人的工作，也会毫不犹豫地\x01",
            "抛到一边，虽然能力上确实是很优秀，\x01",
            "但感觉有些不太合适呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3948")

    label("loc_387E")


    #C0220
    ChrTalk(
        0xA,
        (
            "去年入职的柯琳娜\x01",
            "是个非常优秀的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xA,
        (
            "不过……只要一到了休息时间，\x01",
            "她马上就会消失不见。\x01",
            "态度上稍微有点问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xA,
        (
            "虽然能力上确实是很优秀……\x01",
            "但她总是到了休息时间\x01",
            "就毫不犹豫地停下工作啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3948")

    Jump("loc_4019")

    label("loc_394D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3A21")

    #C0223
    ChrTalk(
        0xA,
        (
            "最近这段时间的投资市场\x01",
            "比艾莉小姐还没去留学时\x01",
            "进一步扩大了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xA,
        (
            "各种各样的投资领域\x01",
            "日益增多，众多经销商们\x01",
            "也都在不断竞争。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xA,
        (
            "如果有兴趣了，欢迎随时光临。\x01",
            "我会为您做详细介绍的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA2")

    label("loc_3A21")


    #C0226
    ChrTalk(
        0xA,
        (
            "最近有很多客人来咨询\x01",
            "投资方面的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xA,
        (
            "关于ＩＢＣ证券的询问\x01",
            "好像也开始增多了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3AD5")

    #C0228
    ChrTalk(
        0xA,
        (
            "而且多亏各位的协助，\x01",
            "新服务也大受好评。\x01",
            "客人增多似乎也受了这一点的影响呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD5")


    #C0229
    ChrTalk(
        0xA,
        (
            "说起来……艾莉小姐好像已经很久\x01",
            "没做投资了，要不要重新体验一下呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xA,
        (
            "您以前使用的账户\x01",
            "还一直保留着呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        (
            "#0000F艾莉，你竟然还\x01",
            "做过投资吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x104,
        "#0309F哇～真是好厉害啊！\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x102,
        (
            "#0103F那个，只是以前为了学习而创建的而已。\x01",
            "投资情况也可以反映出政治动向，\x01",
            "可以从中学习到很多东西。\x02\x03",

            "#0100F不过，现在毕竟有了正式工作，\x01",
            "所以不能再像学生时代那样频繁关注这些了。\x01",
            "……真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xA,
        (
            "哪里哪里。\x01",
            "如果以后有需要，欢迎随时光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xA,
        "我会为您做详细介绍的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3CA2")

    Jump("loc_4019")

    label("loc_3CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D00")

    #C0236
    ChrTalk(
        0xA,
        (
            "玛丽亚贝尔小姐\x01",
            "非常担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xA,
        (
            "还请您不要太过\x01",
            "勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DFB")

    label("loc_3D00")


    #C0238
    ChrTalk(
        0xA,
        (
            "艾莉小姐的活跃表现，\x01",
            "连我都有所耳闻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x102,
        (
            "#0100F啊哈哈……\x01",
            "是看了克洛斯贝尔时代周刊的报道吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xA,
        (
            "嗯，前几天的那篇报道\x01",
            "十分引人注目呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xA,
        (
            "……玛丽亚贝尔小姐\x01",
            "非常担心艾莉\x01",
            "小姐您。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xA,
        (
            "虽然明白您有工作在身，\x01",
            "但还是请尽量别太勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3DFB")

    Jump("loc_4019")

    label("loc_3E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3E5F")

    #C0243
    ChrTalk(
        0xA,
        (
            "我们也提供介绍大楼内\x01",
            "各企业的服务哦。\x01",
            "如果有什么需要，请尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F09")

    label("loc_3E5F")


    #C0244
    ChrTalk(
        0xA,
        (
            "本接待也提供介绍大楼内\x01",
            "各企业的服务哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xA,
        (
            "算上本集团旗下的各个公司，\x01",
            "这座大楼内一共有二十多家公司呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xA,
        (
            "如果想与某个公司的人员联系，\x01",
            "就请来这里办理手续。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3F09")

    Jump("loc_4019")

    label("loc_3F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3F81")

    #C0247
    ChrTalk(
        0xA,
        (
            "我会负责把事情传达给\x01",
            "玛丽亚贝尔小姐的。\x01",
            "她一定会很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xA,
        (
            "艾莉小姐，\x01",
            "以后还请多光顾本行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4019")

    label("loc_3F81")


    #C0249
    ChrTalk(
        0xA,
        (
            "欢迎。\x01",
            "欢迎光临克洛斯贝尔国际银行。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "真是不巧，玛丽亚贝尔小姐\x01",
            "一早就出门视察了。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xA,
        "实在非常抱歉。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xA,
        (
            "今天的事情，\x01",
            "我一定会转达给她的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4019")

    Return()

    # Function_8_27D4 end

    def Function_9_401A(): pass

    label("Function_9_401A")

    Call(0, 10)
    Return()

    # Function_9_401A end

    def Function_10_401E(): pass

    label("Function_10_401E")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4105")

    #C0253
    ChrTalk(
        0xB,
        (
            "哎，利泽罗先生今天\x01",
            "好像没来啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xB,
        (
            "他可是这里的常客，直到昨天，\x01",
            "一直都是每天都来的～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_4100")

    #C0255
    ChrTalk(
        0x101,
        "#0001F（……就是律师他们说的那名行踪不明的贸易商啊……）\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x102,
        (
            "#0101F（好像是一位经常光顾ＩＢＣ\x01",
            "  的人呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4100")

    Jump("loc_4FF5")

    label("loc_4105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_41DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4159")

    #C0257
    ChrTalk(
        0xB,
        (
            "大楼内是\x01",
            "非常安全的～\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xB,
        "就是不知道股价会不会受影响～\x02",
    )

    CloseMessageWindow()
    Jump("loc_41D8")

    label("loc_4159")


    #C0259
    ChrTalk(
        0xB,
        (
            "袭击事件吗？\x01",
            "真是令人很无奈啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xB,
        (
            "算了，反正这座大楼中的保安部\x01",
            "已经做好了万全的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xB,
        "倒是完全不必担心的～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_41D8")

    Jump("loc_4FF5")

    label("loc_41DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_42F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4254")

    #C0262
    ChrTalk(
        0xB,
        (
            "……利泽罗先生最近\x01",
            "好像经常前来光顾啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xB,
        (
            "不过，这种时候频繁交易的话，\x01",
            "风险是非常大的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42EC")

    label("loc_4254")


    #C0264
    ChrTalk(
        0xB,
        (
            "……利泽罗先生最近\x01",
            "好像经常过来啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xB,
        (
            "今天早上，也向我交代了\x01",
            "堆积如山的投资事项。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xB,
        (
            "这样一来，他已经连续两周盈余了……\x01",
            "还真是相当能干啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_42EC")

    Jump("loc_4FF5")

    label("loc_42F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_435A")

    #C0267
    ChrTalk(
        0xB,
        (
            "ＩＢＣ明天\x01",
            "将会暂停营业。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xB,
        (
            "……只要撑过今天，\x01",
            "就能放假了呢～\x01",
            "真是让人期待不已啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF5")

    label("loc_435A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_441C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_439E")

    #C0269
    ChrTalk(
        0xB,
        (
            "玛丽亚贝尔小姐其实是个\x01",
            "心地很善良的人～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4417")

    label("loc_439E")


    #C0270
    ChrTalk(
        0xB,
        (
            "玛丽亚贝尔小姐\x01",
            "来探望我们这些在庆典期间\x01",
            "无法外出游玩的职员了～\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xB,
        (
            "领导如此关心下属，\x01",
            "我们的干劲也\x01",
            "涌出来了呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4417")

    Jump("loc_4FF5")

    label("loc_441C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_448F")

    #C0272
    ChrTalk(
        0xB,
        (
            "纪念庆典时，有很多\x01",
            "令人头疼的客人呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xB,
        (
            "申请文件之类的业务，\x01",
            "三十秒之内就能处理好～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4542")

    label("loc_448F")


    #C0274
    ChrTalk(
        0xB,
        (
            "就在不久前，有位客人\x01",
            "说是要为了纪念庆典\x01",
            "而创建一个ＩＢＣ账户。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xB,
        (
            "明明是自己提出的要求，结果因为\x01",
            "游行马上就要开始了，就\x01",
            "慌慌张张地把申请表填废了～\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xB,
        "真是让人头疼啊～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4542")

    Jump("loc_4FF5")

    label("loc_4547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4656")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_45A6")

    #C0277
    ChrTalk(
        0xB,
        (
            "纪念庆典时，有很多\x01",
            "令人头疼的客人呢～\x01",
            "为他们服务也是件很头疼的事～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4651")

    label("loc_45A6")


    #C0278
    ChrTalk(
        0xB,
        (
            "昨天的那位客人真是让我\x01",
            "费了不少力气来应付～\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xB,
        (
            "他完全都不理解\x01",
            "银行与存款储蓄\x01",
            "之类的概念～\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xB,
        (
            "一直都提一些让人没法回答的问题，\x01",
            "比如怎么借钱或是账户到底是什么～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4651")

    Jump("loc_4FF5")

    label("loc_4656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4720")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_46B7")

    #C0281
    ChrTalk(
        0xB,
        (
            "ＩＢＣ是国际性的大型集团，\x01",
            "所以平时是没有休息的。\x01",
            "真是让人够受的啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_471B")

    label("loc_46B7")


    #C0282
    ChrTalk(
        0xB,
        (
            "在纪念庆典期间，\x01",
            "自治州内的公司\x01",
            "基本都休业了。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xB,
        (
            "……单从这一点来说，\x01",
            "真是挺令人羡慕呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_471B")

    Jump("loc_4FF5")

    label("loc_4720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4817")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4786")

    #C0284
    ChrTalk(
        0xB,
        (
            "为了预防万一，公司内的终端\x01",
            "已经全部停止使用了。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xB,
        "这可真是让人头疼啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_4812")

    label("loc_4786")


    #C0286
    ChrTalk(
        0xB,
        (
            "根据保安部门的联络，\x01",
            "据说有可能被黑客利用的漏洞都已经处理完毕了……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xB,
        "……总算可以使用终端了呢。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xB,
        (
            "哎呀呀，\x01",
            "真是不容易～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)

    label("loc_4812")

    Jump("loc_4FF5")

    label("loc_4817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4880")

    #C0289
    ChrTalk(
        0xB,
        (
            "听说兰菲前辈原来\x01",
            "在秘书部工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xB,
        (
            "她的字写得非常漂亮，\x01",
            "连签名都能\x01",
            "让人看到入迷呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF5")

    label("loc_4880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_490D")

    #C0291
    ChrTalk(
        0xB,
        (
            "ＩＢＣ的接待业务可是一项\x01",
            "非常有挑战性和价值性的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xB,
        (
            "这份工作对时间要求非常严格，\x01",
            "所以工作起来很令人愉快～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A1B")

    label("loc_490D")


    #C0293
    ChrTalk(
        0xB,
        "（敲击键盘……！）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 300)

    #C0294
    ChrTalk(
        0xB,
        (
            "我以前曾在一家不怎么样的\x01",
            "中小企业中工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xB,
        (
            "但后来操作终端的技术被看中，\x01",
            "所以就跳槽来ＩＢＣ了。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xB,
        (
            "这边的工作很有挑战性，\x01",
            "对时间的要求也非常严格～\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xB,
        (
            "不过，也正因为如此，\x01",
            "才让我工作得非常开心呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_9E(0xB, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    ClearChrFlags(0xB, 0x10)

    label("loc_4A1B")

    Jump("loc_4FF5")

    label("loc_4A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4BFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4A9E")

    #C0298
    ChrTalk(
        0xB,
        (
            "欢迎～\x01",
            "欢迎光临ＩＢＣ总部接待处。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xB,
        (
            "本窗口可以为您提供\x01",
            "各种服务。\x01",
            "如果有什么需要，请尽管吩咐～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BFA")

    label("loc_4A9E")


    #C0300
    ChrTalk(
        0xB,
        (
            "欢迎～\x01",
            "欢迎光临ＩＢＣ总部接待处。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xB,
        (
            "本窗口可以办理创建账户、存取款、\x01",
            "各种证券交易等业务……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xB,
        (
            "有关投资、融资方面的介绍，\x01",
            "以及资产、不动产方面的运营等商谈\x01",
            "也可以来此处进行。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xB,
        "欢迎您多加利用～\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        (
            "#0005F（感觉ＩＢＣ的业务范围\x01",
            "  简直就是无所不包啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x102,
        (
            "#0100F（确实……只要是和\x01",
            "  金钱相关的业务，这里几乎\x01",
            "  全部都网罗在内了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4BFA")

    Jump("loc_4FF5")

    label("loc_4BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4C9E")

    #C0306
    ChrTalk(
        0xB,
        (
            "导力网络还处于实验阶段，\x01",
            "银行业务全部通过书面文件来办理。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xB,
        (
            "如果能尽早进入全面导力化阶段的话，\x01",
            "业务效率肯定也能得到大幅度提升～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8F")

    label("loc_4C9E")


    #C0308
    ChrTalk(
        0xB,
        (
            "本大楼在数年之前就已经\x01",
            "完全实施了导力化……\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xB,
        (
            "但这部终端，\x01",
            "现在也只能用来进行\x01",
            "公司内的联络而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xB,
        (
            "在业务部也刚刚\x01",
            "才开始使用而已～\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xB,
        (
            "而且，网络连接也只限于公司内部……\x01",
            "至于后台的那些银行业务，\x01",
            "现在都还在使用书面文件来办理～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4D8F")

    Jump("loc_4FF5")

    label("loc_4D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4DFF")

    #C0312
    ChrTalk(
        0xB,
        (
            "只要拥有了ＩＢＣ的账户，\x01",
            "就可以在世界各国的分部中进行交易。\x01",
            "请一定要多加利用～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EDC")

    label("loc_4DFF")


    #C0313
    ChrTalk(
        0xB,
        "（敲击键盘……！）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 300)

    #C0314
    ChrTalk(
        0xB,
        (
            "客人，\x01",
            "您要开通账户吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        (
            "只要拥有ＩＢＣ的账户，\x01",
            "在世界各国的分行都可以进行交易哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xB,
        (
            "在兄弟银行中也都可以使用，\x01",
            "非常方便。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xB,
        "请一定要多加利用～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_9E(0xB, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    ClearChrFlags(0xB, 0x10)

    label("loc_4EDC")

    Jump("loc_4FF5")

    label("loc_4EE1")

    OP_4B(0xF, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4F94")
    TurnDirection(0xF, 0x0, 0)
    TurnDirection(0xB, 0x0, 0)

    #C0318
    ChrTalk(
        0xF,
        (
            "啊……不好意思，\x01",
            "现在正在给我办理手续呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xB,
        (
            "实在非常抱歉，\x01",
            "请您坐在左边的沙发上\x01",
            "按顺序等待～\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xB, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    OP_9E(0xF, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_4FED")

    label("loc_4F94")


    #C0320
    ChrTalk(
        0xB,
        (
            "请稍等片刻哦～\x01",
            "（敲击键盘……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xB,
        (
            "目前正在确认\x01",
            "账户信息～\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xF,
        "嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4FED")

    OP_4C(0xF, 0xFF)
    OP_4C(0xB, 0xFF)

    label("loc_4FF5")

    TalkEnd(0xB)
    Return()

    # Function_10_401E end

    def Function_11_4FF9(): pass

    label("Function_11_4FF9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_508D")
    Jump("loc_50D7")

    label("loc_508D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_50AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50D7")

    label("loc_50AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50D7")

    label("loc_50CD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50D7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_520C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_516C")

    #C0323
    ChrTalk(
        0xFE,
        (
            "真让人难以置信，\x01",
            "这样的事情，在人生中还是初次遇到！\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        "感觉简直就像受到了侮辱！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5207")

    label("loc_516C")


    #C0325
    ChrTalk(
        0xFE,
        (
            "嗯，克洛斯贝尔时代周刊\x01",
            "竟然会临时休刊……？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "真不敢相信，这到底是怎么回事！\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "经济方面的专栏非常有意思，\x01",
            "我每期都很期待的，但这次竟然……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5207")

    Jump("loc_5F42")

    label("loc_520C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_530B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_527F")

    #C0328
    ChrTalk(
        0xFE,
        (
            "如果是投资方面的咨询，\x01",
            "交给我就可以啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "自从纪念庆典结束之后，\x01",
            "赚到的钱数不清啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5306")

    label("loc_527F")


    #C0330
    ChrTalk(
        0xFE,
        "哇哈哈，又赚到了！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "纪念庆典时的那点损失，\x01",
            "在眨眼之间就全部赚回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        (
            "哈哈哈哈哈……！\x01",
            "投资可真是件不错的事情啊……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5306")

    Jump("loc_5F42")

    label("loc_530B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_543C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5380")

    #C0333
    ChrTalk(
        0xFE,
        (
            "明明是庆典，却还要工作，\x01",
            "所以才会坏了事。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "嗯，没错，这次的大损失\x01",
            "给了我这样的启示。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5437")

    label("loc_5380")

    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0335
    ChrTalk(
        0xFE,
        (
            "终、终于弄明白了……！\x01",
            "为什么我的投资都会失败……！\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "……肯定都是因为我在纪念庆典期间\x01",
            "还要不停工作的缘故。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "嗯，今天就去什么地方\x01",
            "玩玩好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5437")

    Jump("loc_5F42")

    label("loc_543C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_551D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_54BA")

    #C0338
    ChrTalk(
        0xFE,
        (
            "数字居然只有三个零，\x01",
            "怎么想都不可能嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "嗯，肯定是眼花\x01",
            "看错了吧。\x01",
            "……………………（揉眼睛）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5518")

    label("loc_54BA")


    #C0340
    ChrTalk(
        0xFE,
        (
            "不、不可能……\x01",
            "怎么会……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        "……………………（揉眼睛）\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        "……真的不是看错了吗？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5518")

    Jump("loc_5F42")

    label("loc_551D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5578")

    #C0343
    ChrTalk(
        0xFE,
        "今天绝对要获利……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "要投入我剩余资产的三分之一。\x01",
            "这样总行了吧……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F42")

    label("loc_5578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5677")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_55C4")

    #C0345
    ChrTalk(
        0xFE,
        (
            "嗯嗯嗯，股价浮动得很激烈啊……\x01",
            "这可真麻烦啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5672")

    label("loc_55C4")


    #C0346
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，\x01",
            "各支股票的价格都在上涨……\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "但决定到底要买进哪支投资股，\x01",
            "反而也变成了一件很困难的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "咳咳，也就是说……\x01",
            "就算投资失败了，也是情有可原的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5672")

    Jump("loc_5F42")

    label("loc_5677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_572E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_56AF")

    #C0349
    ChrTalk(
        0xFE,
        (
            "这些游客……\x01",
            "真是让人心烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5729")

    label("loc_56AF")


    #C0350
    ChrTalk(
        0xFE,
        (
            "哎呀呀……你们也是\x01",
            "来取钱的游客吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        (
            "外出游玩需要花费的米拉，\x01",
            "事先就应该准备好才对！\x01",
            "真是一点理财头脑都没有！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5729")

    Jump("loc_5F42")

    label("loc_572E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5843")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_57B9")

    #C0352
    ChrTalk(
        0xFE,
        (
            "终端为什么停止运转了啊！？\x01",
            "谁来给我说明一下！？\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "要是耽误了正事，造成损失的话，\x01",
            "这个责任要由谁来负啊……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_583E")

    label("loc_57B9")


    #C0354
    ChrTalk(
        0xFE,
        (
            "刚才去接待处准备办理业务，\x01",
            "但终端却停止运转了，\x01",
            "结算也被延误了。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        "嗯……这到底是怎么回事。\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        "究竟是谁干的好事啊……？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_583E")

    Jump("loc_5F42")

    label("loc_5843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5957")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_58CF")

    #C0357
    ChrTalk(
        0xFE,
        (
            "如果想做好投资，年轻时培养\x01",
            "出来的感性是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "……要是能把投资和金融\x01",
            "编入主日学校的必修学科\x01",
            "就好了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5952")

    label("loc_58CF")


    #C0359
    ChrTalk(
        0xFE,
        (
            "哎呀……你们也有事情\x01",
            "要来ＩＢＣ办理吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        "真是年轻有为，佩服佩服。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        (
            "就照这种势头，不断磨练自己\x01",
            "对金融行业的感性吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5952")

    Jump("loc_5F42")

    label("loc_5957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_59BF")

    #C0362
    ChrTalk(
        0xFE,
        "哇哈哈，听了不要吃惊啊。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "也许你看不出，但我其实\x01",
            "也是个专业理财人士呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A61")

    label("loc_59BF")


    #C0364
    ChrTalk(
        0xFE,
        "我经营着一家贸易公司哦。\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "至于这边的投资，\x01",
            "哈，就算是闲暇时间的消遣吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "呵呵，不过，这也能让我赚到不少钱啊。\x01",
            "上个月差不多就\x01",
            "赚到了一百万米拉呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5A61")

    Jump("loc_5F42")

    label("loc_5A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5AF9")

    #C0367
    ChrTalk(
        0xFE,
        "纪念庆典是克洛斯贝尔最盛大的节日。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "周边诸国的大量人员和米拉\x01",
            "都会流入这里……\x01",
            "身为投资家，自然不能错过这个机会啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B88")

    label("loc_5AF9")


    #C0369
    ChrTalk(
        0xFE,
        "喔，今天的经济专栏……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "嗯，果然都是一些和纪念庆典\x01",
            "相关联的东西啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "身为一名投资专家，自然不能错过\x01",
            "纪念庆典这种大好时机啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5B88")

    Jump("loc_5F42")

    label("loc_5B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5D27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5C27")

    #C0372
    ChrTalk(
        0xFE,
        (
            "说起ＩＢＣ的起源，\x01",
            "是一家在中世纪末期\x01",
            "开始兴起的国际银行。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "自那之后不断发展，期间也曾历尽坎坷……\x01",
            "最终迎来了今日的繁荣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D22")

    label("loc_5C27")


    #C0374
    ChrTalk(
        0xFE,
        (
            "International Bank of Crossbell……\x01",
            "ＩＢＣ拥有最新的\x01",
            "导力设备。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "不过，ＩＢＣ其实是\x01",
            "一家相当古老的银行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "说起它的起源，可以追溯到中世纪，\x01",
            "创业至今已有接近三百年的时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "这家『克洛斯贝尔国际银行』可谓是\x01",
            "历史悠久，享誉盛名呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5D22")

    Jump("loc_5F42")

    label("loc_5D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5E49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5D8A")

    #C0378
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔，也还有很多\x01",
            "头脑顽固的家伙……\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        "这真是令人悲哀啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5E44")

    label("loc_5D8A")


    #C0380
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔在中世纪时期\x01",
            "通过贸易与七耀石的买卖\x01",
            "而走向繁荣。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "但是，步入到导力化时代以后，\x01",
            "那些老本行可就行不通了……\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "如今已是金融与投资的时代了，\x01",
            "那种小本生意可上不了台面。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E44")

    Jump("loc_5F42")

    label("loc_5E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5EAE")

    #C0383
    ChrTalk(
        0xFE,
        "喔……找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "如果没事的话，就请安静一点。\x01",
            "大厅里还有其他的客人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F42")

    label("loc_5EAE")


    #C0385
    ChrTalk(
        0xFE,
        "喔，先看看经济栏目……\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "嗯，ＩＢＣ要开始推出\x01",
            "新的服务了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "这样一来，股价应该又会开始浮动了。\x01",
            "哇哈哈，是不是应该去看看呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xC, 0x10)

    label("loc_5F42")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_4FF9 end

    def Function_12_5F4A(): pass

    label("Function_12_5F4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6395")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 3)), scpexpr(EXPR_END)), "loc_6049")

    #C0388
    ChrTalk(
        0xFE,
        (
            "关于这方面，毕竟是有规定的，\x01",
            "从财团那里收到的米拉，\x01",
            "我会像以往一样，先帮你汇入账户的。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "可是……嗯，\x01",
            "缇欧的心情，我很理解。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "是要用在什么地方，\x01",
            "还是要还给财团……\x01",
            "就由缇欧今后来决定吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x103,
        "#0200F是的，我会考虑的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6390")

    label("loc_6049")


    #C0392
    ChrTalk(
        0xFE,
        "（慌慌张张）……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 0)

    #C0393
    ChrTalk(
        0xFE,
        (
            "呀、呀啊，缇欧……\x01",
            "来ＩＢＣ有什么事吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x103,
        (
            "#0203F不，没什么。\x02\x03",

            "#0205F主任究竟在做什么……？\x01",
            "（举动好怪异……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0395
    ChrTalk(
        0xFE,
        "那个……只是过来汇点钱而已。\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0396
    ChrTalk(
        0xFE,
        (
            "缇欧的生活费，\x01",
            "爱普斯泰恩财团那边\x01",
            "都是准备好了的。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "……但缇欧连一次\x01",
            "都没有使用过。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x103,
        (
            "#0200F因为我现在有警察局支付的薪水了。\x02\x03",

            "#0208F而且……我现在想在支援科\x01",
            "这个地方自力更生。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x101,
        "#0000F……缇欧………\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        "是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "嗯，这也很符合\x01",
            "缇欧一贯的作风啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "明白了，那我暂时\x01",
            "就不多加干预啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "……所以啦，缇欧，那个…\x01",
            "今天的事情，就不要生气了吧？\x02",
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

    #C0404
    ChrTalk(
        0x103,
        (
            "#0211F就因为主任总是这样，\x01",
            "所以才会让我生气……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 3)
    ClearChrFlags(0xE, 0x10)

    label("loc_6390")

    Jump("loc_6668")

    label("loc_6395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_652D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63B0")
    Call(0, 15)
    Jump("loc_6528")

    label("loc_63B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64BF")

    #C0405
    ChrTalk(
        0xFE,
        (
            "是啊，从理论上说，虽然是可能的，\x01",
            "但实际演算能力却跟不上。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "即使是爱普斯泰恩财团制造的\x01",
            "最新装置，也一样会有极限，\x01",
            "大概就是这么一回事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#0005F（听起来好像\x01",
            "  很难懂啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x103,
        (
            "#0203F（……毕竟他在克洛斯贝尔是\x01",
            "  对这方面造诣最高的专家啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6528")

    label("loc_64BF")


    #C0409
    ChrTalk(
        0xFE,
        (
            "理论上虽然是可能的，\x01",
            "但实际演算能力却跟不上。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "不过，演算方法仍然\x01",
            "存在着进化与发展的\x01",
            "空间呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6528")

    Jump("loc_6668")

    label("loc_652D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_653F")
    Call(0, 15)
    Jump("loc_6668")

    label("loc_653F")

    TurnDirection(0xFE, 0x103, 0)

    #C0411
    ChrTalk(
        0xFE,
        "缇、缇欧，工作要加油啊。\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "还有……偶尔有空的话，\x01",
            "也来分部露个脸吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "缇欧平时都不怎么来报告……\x01",
            "我也很担心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x103,
        "#0203F这是多余的担心。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0415
    ChrTalk(
        0xFE,
        (
            "我、我果然还是被\x01",
            "缇欧讨厌了吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6668")

    TalkEnd(0xFE)
    Return()

    # Function_12_5F4A end

    def Function_13_666C(): pass

    label("Function_13_666C")

    EventBegin(0x1)
    Sound(160, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_66C4():
        OP_92(0x101, 0x251C, 0x3E80, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_66C4)
    Sleep(50)

    def lambda_66DA():
        OP_92(0x102, 0x251C, 0x3E80, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66DA)
    Sleep(50)

    def lambda_66F0():
        OP_92(0x103, 0x251C, 0x3E80, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_66F0)
    Sleep(50)

    def lambda_6706():
        OP_92(0x104, 0x251C, 0x3E80, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6706)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    EventBegin(0x0)
    Fade(500)
    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(9500, 1500, 16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0xE, 11000, 0, 16500, 270)
    SetChrPos(0xD, 11500, 0, 15600, 270)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_0D()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_68(5750, 1500, 17850, 4000)
    MoveCamera(44, 15, 0, 4000)
    BeginChrThread(0xE, 3, 0, 14)

    #N0416
    NpcTalk(
        0xE,
        "稍微年长的男性",
        "嗯嗯，好像起作用了呢。\x02",
    )

    CloseMessageWindow()

    #N0417
    NpcTalk(
        0xD,
        "研究员",
        "再次承蒙您的帮助了。\x02",
    )

    CloseMessageWindow()

    #N0418
    NpcTalk(
        0xD,
        "研究员",
        "真是帮大忙了啊，主任。\x02",
    )

    CloseMessageWindow()

    #N0419
    NpcTalk(
        0xD,
        "研究员",
        (
            "那种演算方式\x01",
            "实在是非常困难……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(0, 1900, 9000, 0)
    MoveCamera(35, 11, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 250, 300, 7750, 45)
    SetChrPos(0x102, 600, 300, 9100, 45)
    SetChrPos(0x104, -350, 300, 8750, 45)
    SetChrPos(0x103, 0, 300, 10150, 45)
    OP_0D()

    #C0420
    ChrTalk(
        0x103,
        "#0205F（……那是………）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    WaitChrThread(0xE, 3)
    SetChrPos(0x0, 0, 300, 7750, 0)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x6F, 4)
    EventEnd(0x5)
    Return()

    # Function_13_666C end

    def Function_14_6949(): pass

    label("Function_14_6949")


    def lambda_694E():
        OP_97(0xE, 0xFFFFEE6C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_694E)

    def lambda_6968():
        OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_6968)
    Sleep(50)

    def lambda_697C():
        OP_97(0xD, 0xFFFFE69C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_697C)

    def lambda_6996():
        OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_6996)
    Sleep(1250)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    WaitChrThread(0xE, 1)

    def lambda_69C3():
        OP_97(0xE, 0x0, 0x0, 0x546, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_69C3)
    WaitChrThread(0xE, 1)

    def lambda_69E1():
        OP_93(0xE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_69E1)
    WaitChrThread(0xD, 1)

    def lambda_69F2():
        OP_97(0xD, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_69F2)
    WaitChrThread(0xD, 1)

    def lambda_6A10():
        OP_93(0xD, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6A10)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xD, 1)
    Return()

    # Function_14_6949 end

    def Function_15_6A21(): pass

    label("Function_15_6A21")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(6500, 1200, 17000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x103, 6500, 0, 16350, 0)
    SetChrPos(0x102, 5900, 0, 15150, 0)
    SetChrPos(0x101, 7100, 0, 15350, 0)
    SetChrPos(0x104, 6500, 0, 14150, 0)
    OP_93(0xE, 0x10E, 0x0)
    OP_0D()

    #C0421
    ChrTalk(
        0x103,
        "#0205F主任，好久不见了呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0422
    ChrTalk(
        0xE,
        "这声音是……！？\x02",
    )

    CloseMessageWindow()

    def lambda_6AFA():
        TurnDirection(0xD, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6AFA)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    TurnDirection(0xE, 0x103, 500)

    #C0423
    ChrTalk(
        0xE,
        (
            "啊、啊……\x01",
            "……这不是缇欧吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xE,
        "最、最近还好吧～？\x02",
    )

    CloseMessageWindow()
    OP_64(0xE)
    TurnDirection(0x101, 0x103, 500)

    #C0425
    ChrTalk(
        0x101,
        (
            "#0000F主任……难道说，\x01",
            "这个人就是缇欧的上司……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0426
    ChrTalk(
        0x103,
        (
            "#0203F嗯，是我的直属上司──\x01",
            "魔导杖开发小组\x01",
            "的主任。\x02\x03",

            "#0200F他是导力网络技术的专家，\x01",
            "同时也算是爱普斯泰恩财团\x01",
            "克洛斯贝尔分部的负责人。\x02\x03",

            "……大概算是我的\x01",
            "现场监督吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6C53():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C53)
    Sleep(50)
    OP_93(0x101, 0x0, 0x1F4)

    #C0427
    ChrTalk(
        0xE,
        (
            "你们那个警察局的新部门\x01",
            "好像运作得不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xE,
        "嗯嗯，太好了～\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xE,
        (
            "缇欧，那个……\x01",
            "你平时都不怎么来报告……\x01",
            "我实在是很担心啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x103,
        (
            "#0205F所以就把魔导杖\x01",
            "偷偷放在武器店吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0431
    ChrTalk(
        0xE,
        "（慌张）……\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x101,
        (
            "#0000F说起来，\x01",
            "温蒂好像也说过，\x01",
            "财团的人会经常过来……\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xE,
        "（慌慌张张）……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0434
    ChrTalk(
        0xE,
        "那、那个，那是因为……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    #C0435
    ChrTalk(
        0xE,
        (
            "不好了，好像是惹\x01",
            "缇欧生气了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xE,
        (
            "那个……可是，再怎么说，把小孩子\x01",
            "一个人扔到大城市里不管，也未免……\x01",
            "（自言自语）……\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x103,
        "#0211F……主任，你的举动好可疑。\x02",
    )

    CloseMessageWindow()
    OP_9C(0xE, 0x0, 0x0, 0x0, 0x190, 0x2EE0)

    #C0438
    ChrTalk(
        0xE,
        "哇……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xE, 0x103, 500)

    #C0439
    ChrTalk(
        0x103,
        (
            "#0206F呼……\x02\x03",

            "#0205F不管怎么说，以后请不要再把\x01",
            "装备偷偷放在市里的各种地方了。\x02\x03",

            "这又不是在玩寻宝比赛。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xE,
        "（紧张）……\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xE,
        (
            "哈哈，我、我明白啦。\x01",
            "抱歉啊，缇欧，别再生气了好不好？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x103,
        (
            "#0211F……就是因为主任总是这样，\x01",
            "所以我才讨厌。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xE,
        (
            "（紧张不安）……\x01",
            "哈哈，说得也是啊，嗯，我知道啦……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0444
    ChrTalk(
        0x102,
        "#0106F（缇欧还真是得理不饶人啊……）\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x103,
        (
            "#0203F（……不知为什么，\x01",
            "  就是很火大呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 6500, 0, 16350, 0)
    OP_93(0xD, 0x5A, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x6C, 5)
    EventEnd(0x5)
    Return()

    # Function_15_6A21 end

    def Function_16_70AC(): pass

    label("Function_16_70AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_70EC")

    #C0446
    ChrTalk(
        0xFE,
        (
            "原、原来如此……\x01",
            "还有继续研究的必要啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_711D")

    label("loc_70EC")


    #C0447
    ChrTalk(
        0xFE,
        (
            "嗯嗯，原来如此……\x01",
            "主任的意见果然有道理啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_711D")

    TalkEnd(0xFE)
    Return()

    # Function_16_70AC end

    def Function_17_7121(): pass

    label("Function_17_7121")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7234")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71F1")

    #C0448
    ChrTalk(
        0xFE,
        (
            "今日接到ＩＢＣ大楼内的公司\x01",
            "的委托，过来工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        (
            "在这种现代化高科技的环境下工作，\x01",
            "心情实在是很难平静下来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x103,
        (
            "#0203F（现代化高科技……\x01",
            "  真是典型的大叔式\x01",
            "  词汇啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7234")

    label("loc_71F1")


    #C0451
    ChrTalk(
        0xFE,
        (
            "……发起委托的公司\x01",
            "到底在几楼呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        "去问问接待处的人员吧。\x02",
    )

    CloseMessageWindow()

    label("loc_7234")

    TalkEnd(0xFE)
    Return()

    # Function_17_7121 end

    def Function_18_7238(): pass

    label("Function_18_7238")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7369")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72F1")

    #C0453
    ChrTalk(
        0xFE,
        (
            "在这世界上，也有那么一种人，\x01",
            "完全只靠炒股来维持生计……\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "嗯……用这种方法来赚钱，\x01",
            "肯定会有不小的\x01",
            "成就感吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xFE,
        "……但那是和我完全无缘的世界啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7369")

    label("loc_72F1")


    #C0456
    ChrTalk(
        0xFE,
        (
            "还是说……通过股价的上下波动，\x01",
            "能让他们享受到赌博一样的乐趣呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "……无论如何，\x01",
            "总之那都是与我完全无缘的世界。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7369")

    TalkEnd(0xFE)
    Return()

    # Function_18_7238 end

    def Function_19_736D(): pass

    label("Function_19_736D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7563")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_740A")
    Jump("loc_7454")

    label("loc_740A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_742A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7454")

    label("loc_742A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_744A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7454")

    label("loc_744A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7454")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_74EE")

    #C0458
    ChrTalk(
        0xFE,
        (
            "我是来ＩＢＣ\x01",
            "取钱的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xFE,
        (
            "对克洛斯贝尔市民来说，\x01",
            "理财果然要来ＩＢＣ啊。\x01",
            "这里的利息也是最多的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7557")

    label("loc_74EE")


    #C0460
    ChrTalk(
        0xFE,
        (
            "我孙子的生日要到了，\x01",
            "我想给他买个稍微贵重点的礼物。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xFE,
        (
            "一张、两张、三张……\x01",
            "嗯，数额正确无误。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_7557")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_756C")

    label("loc_7563")

    TalkBegin(0xFE)
    Call(0, 10)
    TalkEnd(0xFE)

    label("loc_756C")

    Return()

    # Function_19_736D end

    def Function_20_756D(): pass

    label("Function_20_756D")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(1000)
    OP_68(0, 1300, 30100, 0)
    MoveCamera(37, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 0, 300, 28600, 0)
    SetChrPos(0x102, -1400, 300, 27300, 0)
    SetChrPos(0x103, -500, 300, 27000, 0)
    SetChrPos(0x104, 600, 300, 27600, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_795B")

    #C0462
    ChrTalk(
        0xA,
        (
            "#5P欢迎。\x01",
            "欢迎光临克洛斯贝尔国际银行。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xA,
        (
            "#5P……啊，艾莉小姐，\x01",
            "还有特别任务支援科的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xA,
        (
            "#5P之前真是多谢各位\x01",
            "对新服务的测试工作\x01",
            "进行协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xA,
        (
            "#5P托各位的福，新业务\x01",
            "大受好评呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x101,
        "#0002F#12P哈哈，是吗？\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x103,
        "#12P#0202F我们好像帮上忙了呢。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xA,
        (
            "#5P是啊，如果以后再有什么事情，\x01",
            "还要请各位多帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xA,
        (
            "#5P那么……今天来这里，\x01",
            "是有什么要事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#0001F#12P啊，那个……\x02",
    )

    CloseMessageWindow()

    def lambda_7781():
        OP_96(0xFE, 0xFFFFFDA8, 0x12C, 0x7274, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7781)
    WaitChrThread(0x102, 1)

    #C0471
    ChrTalk(
        0x102,
        (
            "#6P#0104F兰菲小姐，\x01",
            "其实是有些事情想向您咨询……\x02\x03",

            "#0100F请问迪塔总裁\x01",
            "现在在吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0472
    ChrTalk(
        0xA,
        (
            "#5P啊……原来不找玛丽亚贝尔小姐，\x01",
            "而是有事要找库罗伊斯总裁吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#6P#0103F嗯，也没有提前预约，\x01",
            "实在是很不好意思……\x02\x03",

            "#0101F那个……\x01",
            "果然还是不在吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xA,
        (
            "#5P不，今天还真是少见，\x01",
            "他正好在这里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0xA,
        (
            "#5P您的各位同事也要\x01",
            "一起前去会面吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x102,
        (
            "#6P#0102F嗯……关于某个事件，想找总裁谈谈，\x01",
            "所以希望能一起拜会他，\x01",
            "稍微打扰一下……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E54")

    label("loc_795B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_END)), "loc_7BFC")

    #C0477
    ChrTalk(
        0xA,
        (
            "#5P欢迎。\x01",
            "欢迎光临克洛斯贝尔国际银行。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xA,
        (
            "#5P……啊，艾莉小姐，\x01",
            "还有特别任务支援科的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xA,
        "#5P今天有何贵干呢？请尽管吩咐。\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x101,
        (
            "#12P#0012F哈哈，多谢。\x02\x03",

            "#0001F这个……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A1C():
        OP_96(0xFE, 0xFFFFFDA8, 0x12C, 0x7274, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A1C)
    WaitChrThread(0x102, 1)

    #C0481
    ChrTalk(
        0x102,
        (
            "#6P#0104F您好，兰菲小姐。\x01",
            "其实是有些事情想要向您咨询。\x02\x03",

            "#0100F请问迪塔总裁\x01",
            "现在在吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0482
    ChrTalk(
        0xA,
        (
            "#5P啊……原来不找玛丽亚贝尔小姐，\x01",
            "而是有事要找库罗伊斯总裁吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x102,
        (
            "#6P#0104F嗯，也没有提前预约，\x01",
            "实在是很不好意思……\x02\x03",

            "#0101F那个……\x01",
            "果然还是不在吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xA,
        (
            "#5P不，今天还真是少见，\x01",
            "他正好在这里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xA,
        (
            "#5P您的各位同事也要\x01",
            "一起前去会面吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x102,
        (
            "#6P#0102F嗯……关于某个事件，想找总裁谈谈，\x01",
            "所以希望能一起拜会他，\x01",
            "稍微打扰一下……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E54")

    label("loc_7BFC")


    #C0487
    ChrTalk(
        0xA,
        (
            "#5P欢迎。\x01",
            "欢迎光临克洛斯贝尔国际银行。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xA,
        "#5P今天有何贵干呢？请尽管吩咐。\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x101,
        "#0001F#12P那个……\x02",
    )

    CloseMessageWindow()

    def lambda_7C6A():
        OP_96(0xFE, 0xFFFFFDA8, 0x12C, 0x7274, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C6A)
    WaitChrThread(0x102, 1)

    #C0490
    ChrTalk(
        0x102,
        (
            "#6P#0104F您好，兰菲小姐。\x02\x03",

            "#0100F请问迪塔总裁\x01",
            "现在在吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0491
    ChrTalk(
        0xA,
        (
            "#5P啊，是艾莉小姐啊！\x01",
            "非常欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xA,
        (
            "#5P不找玛丽亚贝尔小姐，\x01",
            "而是有事要找库罗伊斯总裁吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x102,
        (
            "#6P#0103F嗯，也没有提前预约，\x01",
            "实在是很不好意思……\x02\x03",

            "#0101F那个……\x01",
            "果然还是不在吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xA,
        (
            "#5P不，今天还真是少见，\x01",
            "他正好在这里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xA,
        "#5P那个，这几位是……\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        (
            "#6P#0102F是我的同事，\x01",
            "都是克洛斯贝尔警察局的人。\x02\x03",

            "关于某个事件，想找总裁谈谈，\x01",
            "所以希望能一起拜会他，\x01",
            "稍微打扰一下……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E54")


    #C0497
    ChrTalk(
        0xA,
        "#5P啊，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xA,
        (
            "#5P明白了，\x01",
            "请稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0xA, 0x258, 0x7D00, 0x190)

    def lambda_7E99():
        OP_95(0xFE, 600, 300, 32000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7E99)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x190)
    Sleep(300)

    #C0499
    ChrTalk(
        0x104,
        (
            "#12P#0302F（不愧是大小姐……\x01",
            "  真吃得开啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_END)), "loc_7F38")

    #C0500
    ChrTalk(
        0x101,
        (
            "#0002F（哈哈……感觉真是\x01",
            "  和我们处在不同的世界呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F79")

    label("loc_7F38")


    #C0501
    ChrTalk(
        0x101,
        (
            "#0012F（确实……感觉就像是\x01",
            "  和我们处在完全不同的世界呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F79")


    #C0502
    ChrTalk(
        0xA,
        "#5P是的……好的……\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xA,
        (
            "#5P我知道了。\x01",
            "就让他们直接过去。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x190)

    def lambda_7FC4():
        OP_95(0xFE, 0, 300, 31700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7FC4)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0xB4, 0x190)

    #C0504
    ChrTalk(
        0xA,
        (
            "#5P──艾莉小姐，\x01",
            "总裁同意见你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xA,
        (
            "#5P请收好这张认证卡片，\x01",
            "拿着它直接去最上层的\x01",
            "总裁室就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x102,
        "#6P#0109F嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0507
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x320),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('受损的警察徽章', 1)
    OP_93(0x102, 0xB4, 0x1F4)

    #C0508
    ChrTalk(
        0x102,
        (
            "#0100F#5P好啦，各位，\x01",
            "我们这就去坐导力梯吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_80EE():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_80EE)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_END)), "loc_8170")

    #C0509
    ChrTalk(
        0x101,
        (
            "#0002F嗯，走吧。\x01",
            "……真是帮了大忙啊，艾莉。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x104,
        (
            "#0300F既然如此，我们就赶快\x01",
            "前去拜会总裁吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81B3")

    label("loc_8170")


    #C0511
    ChrTalk(
        0x101,
        "#0002F嗯……\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x104,
        (
            "#0300F……那么，我们就快点\x01",
            "前去拜会总裁吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81B3")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 300, 28800, 180)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x82, 2)
    OP_29(0x43, 0x1, 0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_20_756D end

    def Function_21_81DC(): pass

    label("Function_21_81DC")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(1000)
    OP_68(0, 1000, 30100, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 300, 28600, 0)
    SetChrPos(0x102, -1400, 300, 27300, 0)
    SetChrPos(0x103, -500, 300, 27000, 0)
    SetChrPos(0x104, 600, 300, 27600, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8775")

    #C0513
    ChrTalk(
        0xA,
        (
            "#5P欢迎。\x01",
            "欢迎光临克洛斯贝尔国际银行。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0514
    ChrTalk(
        0xA,
        "#5P啊呀，那位是……\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xA,
        (
            "#5P果然是艾莉小姐啊！ \x01",
            "真是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x101,
        "#11P#0005F（哎……？）\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x103,
        "#12P#0205F（艾莉前辈……？）\x02",
    )

    CloseMessageWindow()

    def lambda_832E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_832E)

    def lambda_833B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_833B)

    def lambda_8348():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8348)
    Sleep(300)

    #C0518
    ChrTalk(
        0x102,
        (
            "#12P#0100F您好，兰菲小姐。\x01",
            "真是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xA,
        (
            "#5P自从您外出留学以来，\x01",
            "这还是第一次见面吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xA,
        (
            "#5P……对了，\x01",
            "要不要我马上通知\x01",
            "玛丽亚贝尔小姐呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xA,
        (
            "#5P虽然很不巧，她刚刚去米修拉姆\x01",
            "进行视察了。但如果通知她，\x01",
            "我想她一定会很乐意回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x102,
        (
            "#12P#0104F呵呵……贝尔一点都没变，\x01",
            "还是那么忙啊。\x02\x03",

            "#0100F先不用了，我今天\x01",
            "也没有什么事情要找贝尔。\x02\x03",

            "还是改日再来拜访吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xA,
        (
            "#5P是吗……\x01",
            "那么，我会把原话传达给她的。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_84FA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84FA)

    def lambda_8507():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8507)
    Sleep(300)

    #C0524
    ChrTalk(
        0x104,
        (
            "#12P#0305F（大小姐……竟然和ＩＢＣ\x01",
            "  的人有来往吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        (
            "#11P#0005F（而且关系好像还\x01",
            "  相当亲近呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x103,
        (
            "#12P#0203F（小声）果然是个真正的\x01",
            "  大小姐呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    #C0527
    ChrTalk(
        0x102,
        "#6P#0113F……那个，我都听到了哦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0528
    ChrTalk(
        0x102,
        (
            "#6P#0100F罗伊德，今天不是\x01",
            "为了工作的事情而来的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0529
    ChrTalk(
        0x101,
        (
            "#11P#0012F啊，是啊。\x01",
            "（一不小心都忘了……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_867F():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_867F)

    def lambda_868C():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_868C)

    def lambda_8699():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8699)

    def lambda_86A6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_86A6)
    Sleep(300)

    #C0530
    ChrTalk(
        0x101,
        (
            "#11P#0000F自我介绍一下……\x01",
            "我们是克洛斯贝尔警察局·特别\x01",
            "任务支援科的成员。\x02\x03",

            "ＩＢＣ的人员好像向\x01",
            "我们发出了委托吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xA,
        "#5P啊，是那件事啊。\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xA,
        (
            "#5P不好意思，\x01",
            "我现在就给各位做个说明。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 4)
    Jump("loc_8899")

    label("loc_8775")


    #C0533
    ChrTalk(
        0xA,
        (
            "#5P欢迎。\x01",
            "欢迎光临克洛斯贝尔国际银行。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0534
    ChrTalk(
        0xA,
        (
            "#5P啊，艾莉小姐，\x01",
            "还有特别任务支援科的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x102,
        (
            "#12P#0100F兰菲小姐，\x01",
            "我们是接到委托而来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x101,
        (
            "#11P#0000F那个，ＩＢＣ的人员好像\x01",
            "向我们发起了委托吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xA,
        "#5P啊，是那件事啊。\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xA,
        (
            "#5P那么，我现在就给\x01",
            "各位做个说明吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8899")


    #C0539
    ChrTalk(
        0x102,
        "#12P#0100F嗯，拜托了。\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xA,
        (
            "#5P也许各位已经通过经济杂志\x01",
            "之类的渠道了解一二了……\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xA,
        (
            "#5PＩＢＣ预定将在近期正式实施\x01",
            "以耀晶片兑换米拉的\x01",
            "新服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xA,
        (
            "#5P具体来说，\x01",
            "就是将耀晶片以高于通常市值\x01",
            "的汇率兑换成米拉的服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x104,
        (
            "#12P#0300F原来如此……\x01",
            "也就是说，比普通的商店更加实惠啊，\x01",
            "那好像确实是很方便呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        (
            "#12P#0100F考虑到七耀石资源十分有限，\x01",
            "从而积极地储藏更多耀晶片，\x01",
            "这好像就是这项服务的目的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x103,
        (
            "#12P#0204F真不愧是ＩＢＣ……\x01",
            "这项服务看似普通，却能有效回收耀晶片呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xA,
        "#5P呵呵，多谢夸奖。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xA,
        (
            "#5P──只是，因为存在伪造耀晶片，\x01",
            "还有盗窃等方面的问题，\x01",
            "所以这项服务暂时只打算对会员开放……\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xA,
        (
            "#5P接下来，我们准备利用导力终端\x01",
            "来管理耀晶片的储藏工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xA,
        (
            "#5P希望各位能协助参与\x01",
            "这项计划的测试，\x01",
            "这就是本次的委托内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        (
            "#11P#0000F明白了。\x01",
            "那具体应该做些什么呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xA,
        (
            "#5P嗯，那么，就请收下\x01",
            "这张卡片吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0552
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x35B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x35B, 1)

    #C0553
    ChrTalk(
        0xA,
        (
            "#5P然后，就请根据我的提示，\x01",
            "用它来体验新服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xA,
        (
            "#5P另外，兑换米拉的耀晶片\x01",
            "需要达到一定的数量。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xA,
        (
            "#5P说得具体一点，大概就是七种耀晶片各三十个，\x01",
            "有这个数量的话，应该就足够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x101,
        (
            "#11P#0002F各三十个吗，\x01",
            "明白了。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x104,
        "#12P#0309F好，那我们就赶快试试看吧。\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x102,
        (
            "#12P#0104F嗯，并不一定非要\x01",
            "一次全部换够……\x02\x03",

            "#0100F我们可以在处理其它工作的间隙，\x01",
            "一点一点慢慢来。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0559
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【协助运用新服务项目】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)

    #A0560
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＩＢＣ的兑换服务已经可以正式使用了。\x02",
        )
    )

    CloseMessageWindow()

    #A0561
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "和兰菲对话，\x01",
            "并选择『换钱』，\x01",
            "再选择『EXCHANGE』即可进行兑换。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 300, 28800, 0)
    OP_4C(0xA, 0xFF)
    Sleep(500)
    OP_29(0x7, 0x1, 0x0)
    ClearScenarioFlags(0x49, 2)
    EventEnd(0x5)
    Return()

    # Function_21_81DC end

    def Function_22_8E80(): pass

    label("Function_22_8E80")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(1000)
    OP_68(0, 1000, 30100, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 300, 28600, 0)
    SetChrPos(0x102, -1400, 300, 27300, 0)
    SetChrPos(0x103, -500, 300, 27000, 0)
    SetChrPos(0x104, 600, 300, 27600, 0)
    OP_0D()

    #C0562
    ChrTalk(
        0xA,
        "#5P啊……\x02",
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xA,
        (
            "#5P这样一来，\x01",
            "七种耀晶片各三十个\x01",
            "都已经兑换过米拉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xA,
        "#5P那么，请稍等片刻。\x02",
    )

    CloseMessageWindow()
    OP_92(0xA, 0x258, 0x7D00, 0x190)

    def lambda_8F77():
        OP_95(0xFE, 600, 300, 32000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8F77)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x190)
    Sleep(300)

    #C0565
    ChrTalk(
        0xA,
        (
            "#5P这里是接待处……\x01",
            "想用每种耀晶片各三十个兑换米拉……\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xA,
        (
            "#5P嗯、嗯……\x01",
            "……好的，是这样吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xA,
        "#5P……嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x190)

    def lambda_9025():
        OP_95(0xFE, 0, 300, 31700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9025)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0xB4, 0x190)

    #C0568
    ChrTalk(
        0xA,
        "#5P业务人员那边已经确认完毕了。\x02",
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xA,
        (
            "#5P听说以前有个职员一时疏忽，\x01",
            "搞混了空属性的耀晶片和地属性的耀晶片……\x01",
            "不过错误操作立刻就得到了撤回。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xA,
        (
            "#5P以后应该就能\x01",
            "处理得更加顺畅了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x104,
        (
            "#12P#0300F哈哈，好像已经\x01",
            "开始习惯了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x102,
        (
            "#12P#0104F能帮上您的忙，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xA,
        (
            "#5P呵呵，真是\x01",
            "多谢各位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xA,
        (
            "#5P对了，虽然只是一点薄礼，\x01",
            "但还请赏光收下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0575
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×３获得了。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0576
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×２获得了。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0577
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×２获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('中回复药', 3)
    AddItemNumber('复苏药', 2)
    AddItemNumber('ＥＰ填充剂Ⅰ', 2)

    #C0578
    ChrTalk(
        0x103,
        "#12P#0205F不愧是ＩＢＣ，真是大方呢。\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0xA,
        "#5P呵呵，还有……\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0xA,
        (
            "#5P交给各位的卡片，\x01",
            "今后也可以直接继续使用哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xA,
        (
            "#5P各位是特别的贵客，\x01",
            "今后也可以继续使用\x01",
            "我们的兑换服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xA,
        (
            "#5P就请当作是协助我们\x01",
            "的谢礼之一好了。\x02",
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

    #C0583
    ChrTalk(
        0x101,
        (
            "#11P#0011F这样真的可以吗！？\x01",
            "感觉未免也太慷慨了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x104,
        (
            "#12P#0305F这种只对会员开放的服务，\x01",
            "竟然这么轻易就允许我们使用……\x02\x03",

            "#0309F该不会是看在大小姐的面子上，\x01",
            "才给我们特殊待遇吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x102,
        (
            "#12P#0109F啊哈哈哈哈……\x01",
            "我、我想应该不会是这样的。\x02\x03",

            "#0105F……兰菲小姐，根本就没有这种事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xA,
        "#5P嗯，当然没有了。\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xA,
        (
            "#5P各位，以后如果有什么需要，\x01",
            "还请随时光临哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0588
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【协助运用新服务项目】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 300, 28800, 180)
    OP_4C(0xA, 0xFF)
    OP_29(0x7, 0x4, 0x10)
    OP_29(0x7, 0x1, 0x1)
    SetScenarioFlags(0x1, 1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_22_8E80 end

    def Function_23_9574(): pass

    label("Function_23_9574")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(220, 5800, 11750, 0)
    MoveCamera(16, 14, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 700, 300, 1650, 0)
    SetChrPos(0x102, -700, 300, 1650, 0)
    SetChrPos(0x103, -700, 300, 0, 0)
    SetChrPos(0x104, 700, 300, 0, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0x9, 0x8000)

    def lambda_960B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_960B)

    def lambda_9620():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9620)

    def lambda_9635():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_9635)

    def lambda_964A():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_964A)
    OP_68(220, 1800, 11750, 4000)
    MoveCamera(16, 10, 0, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x3, 1)
    Sleep(300)
    Fade(800)
    OP_68(-90, 1800, 6110, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(16850, 0)
    OP_0D()

    #C0589
    ChrTalk(
        0x101,
        (
            "#11P#0000F那么……\x01",
            "虽然到了ＩＢＣ，但接下来……\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x104,
        (
            "#11P#0300F这里还是一点都没变啊，\x01",
            "感觉有一大堆很厉害的设备在运转。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x103,
        (
            "#11P#0200F离家出走的议员千金\x01",
            "应该是来过这里的……\x02\x03",

            "先问问接待人员吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x102,
        (
            "#5P#0100F嗯，我们去问问\x01",
            "兰菲小姐吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 300, 4570, 0)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    OP_29(0x2D, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_23_9574 end

    def Function_24_97DC(): pass

    label("Function_24_97DC")

    EventBegin(0x0)
    Fade(800)
    OP_4B(0xA, 0xFF)
    OP_68(0, 1200, 30100, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 300, 28600, 0)
    SetChrPos(0x102, -1400, 300, 27300, 0)
    SetChrPos(0x103, -500, 300, 27000, 0)
    SetChrPos(0x104, 600, 300, 27600, 0)
    OP_0D()

    #C0593
    ChrTalk(
        0xA,
        (
            "#5P啊，艾莉小姐，\x01",
            "今日有何贵干呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x102,
        (
            "#12P#0100F嗯，兰菲小姐，\x01",
            "其实是有些事情想向您咨询……\x02\x03",

            "今天有没有一位\x01",
            "名叫卡拉的小姐\x01",
            "来过这里呢？\x02\x03",

            "#0103F她应该是和女仆\x01",
            "一起来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xA,
        (
            "#5P卡拉小姐吗……\x01",
            "嗯，刚才确实来过啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xA,
        (
            "#5P好像说是有很紧急的要事，\x01",
            "想见玛丽亚贝尔小姐。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0597
    ChrTalk(
        0x102,
        "#12P#0105F找贝尔……？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xA,
        (
            "#5P因为已经得到了\x01",
            "玛丽亚贝尔小姐的许可，\x01",
            "所以就让她去上层了。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xA,
        (
            "#5P不过，她大概在一个小时之前\x01",
            "就已经回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x101,
        (
            "#12P#0003F那么……至于详细情况，\x01",
            "能否让我们直接去问玛丽亚贝尔小姐呢？\x02\x03",

            "#0001F因为，这件事其实与我们正在进行的调查有所关联。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xA,
        (
            "#5P嗯，现在这个时间的话，\x01",
            "应该是没有问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0xA,
        (
            "#5P我想，她现在应该在\x01",
            "总裁室呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x103,
        "#12P#0200F十分感谢。\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x104,
        "#12P#0300F好，我们走吧。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -370, 300, 28210, 180)
    OP_4C(0xA, 0xFF)
    OP_29(0x2D, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_24_97DC end

    def Function_25_9B79(): pass

    label("Function_25_9B79")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 500)

    #C0605
    ChrTalk(
        0x8,
        (
            "啊，这前面是\x01",
            "内部人员的专用区域。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x8,
        (
            "如果没有得到许可，\x01",
            "无关人员是不能进入的哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 6280, 0, 15970, 270)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_25_9B79 end

    SaveToFile()

Try(main)
