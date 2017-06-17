from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t104b.bin",                # FileName
        "t104b",                    # MapName
        "t104b",                    # Location
        0x0044,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 68, 0, 2, 0, 3],
    )

    BuildStringList((
        "t104b",                  # 0
        "鲁特",                   # 1
        "梅夏",                   # 2
        "少女",                   # 3
        "青年",                   # 4
        "游客",                   # 5
        "老人",                   # 6
        "老妇人",                 # 7
        "薇娜",                   # 8
        "德罗娜",                 # 9
        "游客",                   # 10
    ))

    AddCharChip((
        "chr/ch25000.itc",                   # 00
        "chr/ch34500.itc",                   # 01
        "chr/ch21302.itc",                   # 02
        "chr/ch21202.itc",                   # 03
        "chr/ch21602.itc",                   # 04
        "chr/ch33002.itc",                   # 05
        "chr/ch21702.itc",                   # 06
        "chr/ch27900.itc",                   # 07
        "chr/ch26600.itc",                   # 08
        "chr/ch24400.itc",                   # 09
    ))

    DeclNpc(-104069, 0,       2980,    90,   257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-101099, 0,       5880,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-104949, 0,       8989,    45,   341,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-102970, 0,       10960,   225,  341,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-93940,  0,       11039,   225,  341,  0x0, 0,   4,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-97919,  0,       18979,   45,   341,  0x0, 0,   5,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-97930,  0,       20979,   135,  341,  0x0, 0,   6,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-1860,   0,       10640,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4159,    0,       2349,    0,    257,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(3950,    0,       3309,    270,  257,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(-1770,   0,       8810,    1000,    -1860,   1500,    10640,   0x007E, 0,  12, 0x0000)
    DeclActor(-101650, 0,       2470,    1000,    -104070, 1500,    2980,    0x007E, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_260",          # 00, 0
        "Function_1_318",          # 01, 1
        "Function_2_3A1",          # 02, 2
        "Function_3_3A8",          # 03, 3
        "Function_4_3A9",          # 04, 4
        "Function_5_3AD",          # 05, 5
        "Function_6_88C",          # 06, 6
        "Function_7_8FA",          # 07, 7
        "Function_8_AC5",          # 08, 8
        "Function_9_C44",          # 09, 9
        "Function_10_DEB",         # 0A, 10
        "Function_11_F5D",         # 0B, 11
        "Function_12_10C7",        # 0C, 12
        "Function_13_10CB",        # 0D, 13
        "Function_14_1290",        # 0E, 14
        "Function_15_12FD",        # 0F, 15
        "Function_16_13AD",        # 10, 16
    ))


    def Function_0_260(): pass

    label("Function_0_260")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2A0"),
        (1, "loc_2AC"),
        (2, "loc_2B8"),
        (3, "loc_2C4"),
        (4, "loc_2D0"),
        (5, "loc_2DC"),
        (6, "loc_2E8"),
        (SWITCH_DEFAULT, "loc_2F4"),
    )


    label("loc_2A0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2AC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2B8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2C4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2D0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2DC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_300")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_317")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_317")

    Return()

    # Function_0_260 end

    def Function_1_318(): pass

    label("Function_1_318")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A0")
    OP_95(0xFE, -98090, 0, 5880, 2000, 0x0)
    OP_95(0xFE, -98090, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 5880, 2000, 0x0)
    Jump("Function_1_318")

    label("loc_3A0")

    Return()

    # Function_1_318 end

    def Function_2_3A1(): pass

    label("Function_2_3A1")

    BeginChrThread(0x9, 0, 0, 1)
    Return()

    # Function_2_3A1 end

    def Function_3_3A8(): pass

    label("Function_3_3A8")

    Return()

    # Function_3_3A8 end

    def Function_4_3A9(): pass

    label("Function_4_3A9")

    Call(0, 5)
    Return()

    # Function_4_3A9 end

    def Function_5_3AD(): pass

    label("Function_5_3AD")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_888")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_40A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_883")

    label("loc_42A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43E")
    Jump("loc_883")

    label("loc_43E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_883")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_811")

    #C0001
    ChrTalk(
        0x8,
        (
            "晚餐中供应的是\x01",
            "从帝国直送过来的上等葡萄酒，\x01",
            "『艾尔·沃瓦鲁』，请享用。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "该红酒价格不菲，其芳醇的香气\x01",
            "与著名的『格兰·夏利拿』相比，\x01",
            "也是毫不逊色。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_595")

    #C0003
    ChrTalk(
        0x102,
        (
            "#0103F『格兰·夏利拿』……\x01",
            "那好像是利贝尔王国酿造的\x01",
            "上等葡萄酒哦。\x02\x03",

            "#0100F几年前曾在利贝尔王国内拍卖，\x01",
            "最后以五十万米拉的价格成交。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61C")

    label("loc_595")


    #C0004
    ChrTalk(
        0x102,
        (
            "#5303F『格兰·夏利拿』……\x01",
            "那好像是利贝尔王国酿造的\x01",
            "陈年葡萄酒吧。\x02\x03",

            "#5300F几年前在利贝尔王国内拍卖，\x01",
            "最后以五十万米拉的价格成交。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61C")


    #C0005
    ChrTalk(
        0x101,
        (
            "#5005F五、五十万米拉……！？\x01",
            "一瓶葡萄酒竟然这么值钱……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_684")

    #C0006
    ChrTalk(
        0x103,
        "#0203F难以理解的世界。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A0")

    label("loc_684")


    #C0007
    ChrTalk(
        0x103,
        "#5403F难以理解的世界。\x02",
    )

    CloseMessageWindow()

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_700")

    #C0008
    ChrTalk(
        0x104,
        (
            "#0304F如果真有这等美酒，\x01",
            "那可一定要尝尝看啊。\x02\x03",

            "#0309F怎么样，我先来一杯……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_751")

    label("loc_700")


    #C0009
    ChrTalk(
        0x104,
        (
            "#5604F如果真有这等美酒，\x01",
            "那可一定要尝尝看啊。\x02\x03",

            "#5609F怎么样，我先来一杯……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_780")

    #C0010
    ChrTalk(
        0x103,
        "#0211F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A0")

    label("loc_780")


    #C0011
    ChrTalk(
        0x103,
        "#5411F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_7A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D1")

    #C0012
    ChrTalk(
        0x104,
        "#0306F……我、我开个玩笑啦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F3")

    label("loc_7D1")


    #C0013
    ChrTalk(
        0x104,
        "#5606F……我、我开个玩笑啦！\x02",
    )

    CloseMessageWindow()

    label("loc_7F3")


    #C0014
    ChrTalk(
        0x101,
        "#5003F明白就好。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_883")

    label("loc_811")


    #C0015
    ChrTalk(
        0x8,
        (
            "『艾尔·沃瓦鲁』是一种\x01",
            "与『格兰·夏利拿』相比\x01",
            "也毫不逊色的上等葡萄酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        "不嫌弃的话，请在晚餐时尽情享用。\x02",
    )

    CloseMessageWindow()

    label("loc_883")

    Jump("loc_3BA")

    label("loc_888")

    TalkEnd(0x8)
    Return()

    # Function_5_3AD end

    def Function_6_88C(): pass

    label("Function_6_88C")

    TalkBegin(0xFE)

    #C0017
    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "纪念庆典到今天就该结束了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "看起来，市里好像\x01",
            "也相当热闹呢……\x01",
            "呜呜……好想去啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_88C end

    def Function_7_8FA(): pass

    label("Function_7_8FA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_98E")
    Jump("loc_9D8")

    label("loc_98E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9AE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D8")

    label("loc_9AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D8")

    label("loc_9CE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9D8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A80")

    #C0019
    ChrTalk(
        0xFE,
        "（狼吞虎咽）……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "（大吃大喝）……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "嗯！这料理简直太棒了！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "买不到宝石的愤怒\x01",
            "立刻就烟消云散了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_ABD")

    label("loc_A80")


    #C0023
    ChrTalk(
        0xFE,
        "唔唔……真好吃。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x2)

    #C0024
    ChrTalk(
        0xFE,
        (
            "……不好意思，\x01",
            "再给我来一份⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABD")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_8FA end

    def Function_8_AC5(): pass

    label("Function_8_AC5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B59")
    Jump("loc_BA3")

    label("loc_B59")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B79")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BA3")

    label("loc_B79")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B99")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BA3")

    label("loc_B99")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BA3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C17")

    #C0025
    ChrTalk(
        0xFE,
        "还……还吃得下啊？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "存、存款啊……\x01",
            "我的全部财产……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C3C")

    label("loc_C17")


    #C0027
    ChrTalk(
        0xFE,
        (
            "存、存款啊……\x01",
            "我的全部财产……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_AC5 end

    def Function_9_C44(): pass

    label("Function_9_C44")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CD8")
    Jump("loc_D22")

    label("loc_CD8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CF8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D22")

    label("loc_CF8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D18")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D22")

    label("loc_D18")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D22")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D99")

    #C0028
    ChrTalk(
        0xFE,
        "我吃饱啦。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "能与美食邂逅，\x01",
            "真是满足，好满足啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_DE3")

    label("loc_D99")


    #C0030
    ChrTalk(
        0xFE,
        (
            "能与如此美食邂逅。\x01",
            "特地跑到克洛斯贝尔这种地方来，\x01",
            "也算是不虚此行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_C44 end

    def Function_10_DEB(): pass

    label("Function_10_DEB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E7F")
    Jump("loc_EC9")

    label("loc_E7F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E9F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC9")

    label("loc_E9F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EBF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC9")

    label("loc_EBF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EC9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0031
    ChrTalk(
        0xFE,
        (
            "哎呀……\x01",
            "议长宅邸的宴会\x01",
            "就要开始了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "我还是第一次带妻子来这里。\x01",
            "如果她能玩得开心就好了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_DEB end

    def Function_11_F5D(): pass

    label("Function_11_F5D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FF1")
    Jump("loc_103B")

    label("loc_FF1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1011")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_103B")

    label("loc_1011")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1031")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_103B")

    label("loc_1031")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_103B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0033
    ChrTalk(
        0xFE,
        (
            "我先生今天\x01",
            "好像要带我去参加\x01",
            "米修拉姆的宴会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "呵呵，好期待啊，\x01",
            "会是个怎样的宴会呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_F5D end

    def Function_12_10C7(): pass

    label("Function_12_10C7")

    Call(0, 13)
    Return()

    # Function_12_10C7 end

    def Function_13_10CB(): pass

    label("Function_13_10CB")

    TalkBegin(0xF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_128C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1128")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1128")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1148")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1287")

    label("loc_1148")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115C")
    Jump("loc_1287")

    label("loc_115C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1287")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1250")

    #C0035
    ChrTalk(
        0xF,
        "客人，这套衣服真是非常适合您啊。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xF,
        (
            "这是采用了最近的流行元素，\x01",
            "并经过精心搭配的\x01",
            "典雅样式……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xF,
        (
            "瓦吉先生的衣着品位\x01",
            "让身为职业者的我都自愧不如呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#5005F（那家伙……到底是什么人呢……？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1287")

    label("loc_1250")


    #C0039
    ChrTalk(
        0xF,
        (
            "瓦吉先生的衣着品位\x01",
            "让身为职业者的我都自愧不如呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1287")

    Jump("loc_10D8")

    label("loc_128C")

    TalkEnd(0xF)
    Return()

    # Function_13_10CB end

    def Function_14_1290(): pass

    label("Function_14_1290")

    TalkBegin(0xFE)
    TurnDirection(0x10, 0x11, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AC")
    Call(0, 16)
    Jump("loc_12F9")

    label("loc_12AC")


    #C0040
    ChrTalk(
        0xFE,
        "不知客人是否中意……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "不然，我们就换一种风格，\x01",
            "您看这顶帽子怎么样？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F9")

    TalkEnd(0xFE)
    Return()

    # Function_14_1290 end

    def Function_15_12FD(): pass

    label("Function_15_12FD")

    TalkBegin(0xFE)
    OP_93(0xFE, 0x10E, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1319")
    Call(0, 16)
    Jump("loc_13A9")

    label("loc_1319")


    #C0042
    ChrTalk(
        0xFE,
        (
            "（真、真麻烦啊……\x01",
            "　本来想随便敷衍几句\x01",
            "　就赶快回去的……）\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "（被如此热情地推荐，\x01",
            "　不买点东西就离开的话，\x01",
            "　良心上也过不去吧……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A9")

    TalkEnd(0xFE)
    Return()

    # Function_15_12FD end

    def Function_16_13AD(): pass

    label("Function_16_13AD")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0044
    ChrTalk(
        0x10,
        (
            "这样啊……\x01",
            "您好像更喜欢\x01",
            "休闲类的打扮啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x10,
        (
            "我想，这顶帽子或许\x01",
            "更适合您吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x11,
        (
            "那、那个……\x01",
            "今天就不用了吧～……\x01",
            "因为……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_16_13AD end

    SaveToFile()

Try(main)
