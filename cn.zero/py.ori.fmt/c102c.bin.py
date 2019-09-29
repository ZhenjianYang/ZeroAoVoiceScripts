from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c102c.bin",                # FileName
        "c102c",                    # MapName
        "c102c",                    # Location
        0x0014,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 20, 0, 1, 0, 2],
    )

    BuildStringList((
        "c102c",                  # 0
        "赛尔丹分部长",           # 1
        "克潘",                   # 2
        "彼德",                   # 3
    ))

    AddCharChip((
        "chr/ch32200.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch24200.itc",                   # 02
    ))

    DeclNpc(7230,    0,       9069,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-519,    0,       43310,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(7230,    0,       6780,    0,    389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)

    DeclActor(6580,    0,       7980,    1500,    7230,    1500,    9070,    0x007E, 0,  3,  0x0000)
    DeclActor(-3170,   0,       51750,   1200,    -2860,   1500,    52600,   0x007C, 0,  9,  0x0000)
    DeclActor(470,     0,       43660,   1200,    470,     1500,    43360,   0x007C, 0,  15, 0x0000)

    ScpFunction((
        "Function_0_1A0",          # 00, 0
        "Function_1_258",          # 01, 1
        "Function_2_2D9",          # 02, 2
        "Function_3_316",          # 03, 3
        "Function_4_31A",          # 04, 4
        "Function_5_DE5",          # 05, 5
        "Function_6_16EB",         # 06, 6
        "Function_7_18FA",         # 07, 7
        "Function_8_1A71",         # 08, 8
        "Function_9_2555",         # 09, 9
        "Function_10_2F8E",        # 0A, 10
        "Function_11_2FAA",        # 0B, 11
        "Function_12_3177",        # 0C, 12
        "Function_13_3221",        # 0D, 13
        "Function_14_52A5",        # 0E, 14
        "Function_15_5538",        # 0F, 15
    ))


    def Function_0_1A0(): pass

    label("Function_0_1A0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1E0"),
        (1, "loc_1EC"),
        (2, "loc_1F8"),
        (3, "loc_204"),
        (4, "loc_210"),
        (5, "loc_21C"),
        (6, "loc_228"),
        (SWITCH_DEFAULT, "loc_234"),
    )


    label("loc_1E0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_1EC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_1F8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_204")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_210")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_21C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_228")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_234")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_240")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_257")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_257")

    Return()

    # Function_0_1A0 end

    def Function_1_258(): pass

    label("Function_1_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26B")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2BF")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_279")
    Jump("loc_2BF")

    label("loc_279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_287")
    Jump("loc_2BF")

    label("loc_287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_295")
    Jump("loc_2BF")

    label("loc_295")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_2AC")
    SetChrFlags(0x8, 0x80)
    Jump("loc_2BF")

    label("loc_2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2BF")
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x80)

    label("loc_2BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D8")
    Event(0, 8)

    label("loc_2D8")

    Return()

    # Function_1_258 end

    def Function_2_2D9(): pass

    label("Function_2_2D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EF")
    OP_65(0x0, 0x1)

    label("loc_2EF")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_315")
    OP_66(0x1, 0x1)

    label("loc_315")

    Return()

    # Function_2_2D9 end

    def Function_3_316(): pass

    label("Function_3_316")

    Call(0, 4)
    Return()

    # Function_3_316 end

    def Function_4_31A(): pass

    label("Function_4_31A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_45D")

    #C0001
    ChrTalk(
        0x8,
        (
            "对了，罗伊德团员，你知道\x01",
            "『等级认证考试』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "在钓公师团，根据垂钓的实力，\x01",
            "会划分出不同的『等级』。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "哇哈哈，如果取得了高阶的钓师等级，肯定就会\x01",
            "在垂钓爱好者圈子里受到无数赞赏与崇拜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "好了，要是还有什么不明白的事，可以随时来问我。\x01",
            "我一定会耐心详细地告诉你的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 1)
    TalkEnd(0x8)
    Return()

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_797")

    #C0005
    ChrTalk(
        0x8,
        "欢迎来到钓公师团！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "呵呵，你是罗伊德团员吧？\x01",
            "早就听说过你的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "你是在克潘的邀请之下\x01",
            "才加入我们团的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "我是钓公师团·克洛斯贝尔分部\x01",
            "的分部长赛尔丹。\x01",
            "以后还请多多关照啊，罗伊德团员！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#0003F那个，请多指教……\x02\x03",

            "#0005F不对，我是\x01",
            "什么时候……加入\x01",
            "钓公师团的啊？\x02\x03",

            "#0003F以前确实收下过\x01",
            "克潘先生赠送的钓竿，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "哇哈哈，那种小事就不用在意啦！\x01",
            "总之，你已经彻底成为我们的同伴啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#0006F（这、这真是强拉硬拽啊……）\x02\x03",

            "#0000F（算啦，反正大家也有着相同的爱好，\x01",
            "  在钓鱼方面，应该会很聊得来……）\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "对了，罗伊德团员，你知道\x01",
            "『等级认证考试』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "在钓公师团，根据垂钓的实力，\x01",
            "会划分出不同的『等级』。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "哇哈哈，如果取得了高阶的钓师等级，肯定就会\x01",
            "在垂钓爱好者圈子里受到无数赞赏与崇拜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "好了，要是还有什么不明白的事，可以随时来问我。\x01",
            "我一定会耐心详细地告诉你的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 1)
    TalkEnd(0x8)
    Return()

    label("loc_797")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_8B7")

    #C0016
    ChrTalk(
        0x8,
        (
            "恭喜！\x01",
            "听说你终于入团了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "话说回来，克潘那家伙动作可真快啊。\x01",
            "我还想亲自拉你加入，他就已经先下手了……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0003F……果然\x01",
            "是这么回事啊。\x02\x03",

            "#0005F不对，我是\x01",
            "什么时候……加入\x01",
            "钓公师团的啊？\x02\x03",

            "#0003F我只记得自己曾经收下过\x01",
            "克潘先生赠送的钓竿而已……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D0")

    label("loc_8B7")


    #C0019
    ChrTalk(
        0x8,
        (
            "恭喜你入团！\x01",
            "罗伊德团员，很高兴见到你啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "我是钓公师团·克洛斯贝尔分部\x01",
            "的分部长赛尔丹。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        "以后还请多多关照啊，罗伊德团员！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#0004F哈哈，好的……\x02\x03",

            "#0005F可是，话说我是什么时候\x01",
            "加入钓公师团……的呢？\x01",
            "有这种事吗？\x02\x03",

            "#0003F我只记得曾经收下过\x01",
            "克潘先生赠送的钓竿而已……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D0")


    #C0023
    ChrTalk(
        0x8,
        (
            "哇哈哈，那种小事就不用在意啦！\x01",
            "总之，你已经彻底成为我们的同伴啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#0003F（这、这真是强拉硬拽啊……）\x02\x03",

            "#0000F（算啦，反正大家也有着相同的爱好，\x01",
            "  在钓鱼方面，应该会很聊得来……）\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "对了，罗伊德团员，你知道\x01",
            "『等级认证考试』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "在钓公师团，根据垂钓的实力，\x01",
            "会划分出不同的『等级』。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "哇哈哈，如果取得了高阶的钓师等级，肯定就会\x01",
            "在垂钓爱好者圈子里受到无数赞赏与崇拜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "好了，要是还有什么不明白的事，可以随时来问我。\x01",
            "我一定会耐心详细地告诉你的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 1)
    TalkEnd(0x8)
    Return()

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_END)), "loc_DD7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD2")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C71")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_C1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3C")
    OP_AF(0x37)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C6C")

    label("loc_C3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C50")
    Jump("loc_C6C")

    label("loc_C50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_C6C")

    Jump("loc_DCD")

    label("loc_C71")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D4D")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "鉴定等级\x01",      # 1
            "购物\x01",          # 2
            "放弃\x01",          # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBF")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_CBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE3")
    Call(0, 14)
    Call(0, 13)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D48")

    label("loc_CE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D18")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D07")
    OP_AF(0x36)
    Jump("loc_D09")

    label("loc_D07")

    OP_AF(0x37)

    label("loc_D09")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D48")

    label("loc_D18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D2C")
    Jump("loc_D48")

    label("loc_D2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D48")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_D48")

    Jump("loc_DCD")

    label("loc_D4D")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "鉴定等级\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9D")
    Call(0, 14)
    Call(0, 13)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCD")

    label("loc_D9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB1")
    Jump("loc_DCD")

    label("loc_DB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_DCD")

    Jump("loc_BBE")

    label("loc_DD2")

    Jump("loc_DDA")

    label("loc_DD7")

    Call(0, 5)

    label("loc_DDA")

    TalkEnd(0x8)
    OP_93(0x8, 0xB4, 0x0)
    Return()

    # Function_4_31A end

    def Function_5_DE5(): pass

    label("Function_5_DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_11EF")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F33")

    #C0029
    ChrTalk(
        0x8,
        "罗伊德团员，你听说过这个传闻吗？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "在克洛斯贝尔，栖息着传说中的鱼王\x01",
            "——『霸王蛇鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "它们以艾鲁姆湖为主要栖息地，\x01",
            "性情可谓凶残非常，\x01",
            "据说在从前，连渔民都惧怕它们。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "但是，最近这十几年来，\x01",
            "却几乎没有人目击过它们……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "如果能把这家伙钓上来，\x01",
            "毫无疑问就能得到荣誉勋章了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FEF")

    label("loc_F33")


    #C0034
    ChrTalk(
        0x8,
        (
            "『霸王蛇鱼』简直是\x01",
            "鱼王中的鱼王……\x01",
            "钓到那家伙可是我们钓公师团的共同梦想。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "虽然这十几年来都没有人目击过它们，\x01",
            "但如果是已经成为『特级钓师』的你，\x01",
            "说不定还真有可能将它钓上来吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FEF")

    Jump("loc_11EA")

    label("loc_FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1176")

    #C0036
    ChrTalk(
        0x8,
        (
            "不愧是罗伊德团员，\x01",
            "都成了『钓圣』还这么谦虚。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "哇哈哈，我非常欣赏你！\x01",
            "今天晚上不如去夜钓吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "我们分部在举办联欢会时，\x01",
            "就经常会去夜钓！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，不好意思。\x01",
            "今天晚上稍微有些不方便……\x02\x03",

            "下次如果有机会，\x01",
            "我绝对乐意奉陪到底。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        "哇哈哈哈，连拒绝的方式都这么谦逊有礼！\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "好吧！那等你有空时，就来和我说。\x01",
            "到时候连同庆祝会一起，举办一场钓鱼大赛吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11EA")

    label("loc_1176")


    #C0042
    ChrTalk(
        0x8,
        (
            "一定要庆祝罗伊德团员\x01",
            "取得了『钓圣』的称号啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "到时候把你钓到霸王蛇鱼的神勇经过\x01",
            "慢慢说给我听吧，哇哈哈哈！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EA")

    Jump("loc_16EA")

    label("loc_11EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1255")

    #C0044
    ChrTalk(
        0x8,
        (
            "那么，我今天也出去\x01",
            "钓鱼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "市内最近好像不是很太平，\x01",
            "不然就去玛因兹一带好啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16EA")

    label("loc_1255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_136E")

    #C0046
    ChrTalk(
        0x8,
        (
            "听说在克洛斯贝尔的某个地方，\x01",
            "栖息着一种被称为『鱼王』\x01",
            "的巨大鱼类……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "除此之外，也还有电鳗、\x01",
            "魔鬼巨鲶等体型相当\x01",
            "惊人的大型鱼。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1332")

    #C0048
    ChrTalk(
        0x8,
        (
            "……罗伊德团员，如果你有兴趣，\x01",
            "请一定去试着挑战啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1369")

    label("loc_1332")


    #C0049
    ChrTalk(
        0x8,
        (
            "……罗伊德团员，如果你有兴趣\x01",
            "请一定要再去挑战啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1369")

    Jump("loc_16EA")

    label("loc_136E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1421")

    #C0050
    ChrTalk(
        0x8,
        (
            "钓公师团的团长是一位\x01",
            "名叫费瑟尔的男爵。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "本想趁着纪念庆典，\x01",
            "请他来这里看看的，\x01",
            "但他的行程果然还是排不开啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "团长先生现在大概\x01",
            "也很忙吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1494")

    label("loc_1421")


    #C0053
    ChrTalk(
        0x8,
        (
            "费瑟尔男爵为了在各国\x01",
            "设立钓公师团的分部，\x01",
            "正在四处奔波。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "日程安排实在是太过紧凑，\x01",
            "所以没能把他请过来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1494")

    Jump("loc_16EA")

    label("loc_1499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1583")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1501")

    #C0055
    ChrTalk(
        0x8,
        "昨天垂钓的收获真是很棒呢！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "罗伊德团员，就保持这种势头\x01",
            "继续努力吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_157E")

    label("loc_1501")


    #C0057
    ChrTalk(
        0x8,
        (
            "虽说是纪念庆典，\x01",
            "但钓鱼也不能懈怠啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "长时间把鱼竿扔着不用的话，\x01",
            "垂钓技术是会下降的，\x01",
            "最好能保持每天都垂钓一下呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157E")

    Jump("loc_16EA")

    label("loc_1583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_16EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1678")

    #C0059
    ChrTalk(
        0x8,
        (
            "……罗伊德团员，\x01",
            "警察的工作很忙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0000F啊，是很忙呢……\x01",
            "毕竟是在纪念庆典期间嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "是吗……\x01",
            "不好意思，提了奇怪的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "请不用在意，在本职工作上多努力吧。\x01",
            "但闲暇时也不要忘了追求更大的垂钓成果啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16EA")

    label("loc_1678")


    #C0063
    ChrTalk(
        0x8,
        (
            "罗伊德团员，不用在意我们的事，\x01",
            "请在本职工作上多加努力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "当然，闲暇时也不要忘了\x01",
            "追求更大的垂钓成果啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16EA")

    Return()

    # Function_5_DE5 end

    def Function_6_16EB(): pass

    label("Function_6_16EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_18F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A1")
    OP_4B(0x8, 0xFF)

    #C0065
    ChrTalk(
        0xFE,
        (
            "嗯，其实我也曾询问过\x01",
            "游击士艾丝蒂尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "但有本职工作的团员\x01",
            "果然都很忙吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "在不妨碍本职工作的前提下尽情享受\x01",
            "垂钓之趣，这是我们的基本理念。\x01",
            "虽然很遗憾，但还是不要叫她了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "呵呵，可是她自己吵着说\x01",
            "无论如何也要参加呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "说是要把工作放下，暂时休假……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0070
    ChrTalk(
        0x8,
        (
            "呵呵，那还真是令人期待啊。\x01",
            "让我们来个久违的大狂欢吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#0005F（？？？\x01",
            "  ……在说些什么呢？）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_18F6")

    label("loc_18A1")


    #C0072
    ChrTalk(
        0xFE,
        "呵呵，很令人期待吧。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "从上个月就开始计划的重量级活动……\x01",
            "大家一起来狂欢吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F6")

    TalkEnd(0xFE)
    Return()

    # Function_6_16EB end

    def Function_7_18FA(): pass

    label("Function_7_18FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A6D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_197C")

    #C0074
    ChrTalk(
        0xFE,
        (
            "彼德先生和那位特级钓师\x01",
            "好像去了米修拉姆的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "……嘁～\x01",
            "本来还想和他\x01",
            "再来一场垂钓比赛呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6D")

    label("loc_197C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0D")

    #C0076
    ChrTalk(
        0xFE,
        (
            "虽然不太了解具体状况，\x01",
            "但警察的工作也很辛苦的说～\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "啊，请不用在意\x01",
            "我啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "反正闲着也是闲着，我也出去\x01",
            "钓钓鱼好啦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A6D")

    label("loc_1A0D")


    #C0079
    ChrTalk(
        0xFE,
        (
            "彼德先生和那位特级钓师\x01",
            "好像去了米修拉姆的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "我也没事可做，\x01",
            "干脆找个地方去转转好了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6D")

    TalkEnd(0xFE)
    Return()

    # Function_7_18FA end

    def Function_8_1A71(): pass

    label("Function_8_1A71")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1500, 1400, 700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22440, 0)
    SetChrPos(0x101, -1580, 0, -580, 45)
    SetChrPos(0x102, -580, 0, -1580, 45)
    SetChrPos(0x104, -1580, 0, -2580, 45)
    SetChrPos(0x103, -2580, 0, -1580, 45)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 11910, 1670, 7920, 180)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(2100, 1400, 1510, 3000)
    MoveCamera(45, 22, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(22440, 3000)

    def lambda_1B72():
        OP_95(0xFE, 1310, 0, 2330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B72)

    def lambda_1B8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B8C)
    Sleep(300)

    def lambda_1BA0():
        OP_95(0xFE, 2310, 0, 1130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BA0)

    def lambda_1BBA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1BBA)
    Sleep(300)

    def lambda_1BCE():
        OP_95(0xFE, 110, 0, 1130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BCE)

    def lambda_1BE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1BE8)
    Sleep(300)

    def lambda_1BFC():
        OP_95(0xFE, 1310, 0, 130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1BFC)

    def lambda_1C16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C16)
    Sleep(3000)

    #C0081
    ChrTalk(
        0x101,
        "#5P#0000F打扰了～……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x12C)
    Sleep(300)
    OP_93(0x101, 0x0, 0x12C)
    Sleep(300)
    OP_93(0x101, 0x2D, 0x12C)

    #C0082
    ChrTalk(
        0x101,
        (
            "#5P#0003F……好像没有人在啊。\x02\x03",

            "#0001F本来还以为\x01",
            "能在这里探查到\x01",
            "约亚西姆医生的行踪呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#12P#0300F难道是已经去了\x01",
            "那个钓鱼比赛了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x102,
        (
            "#11P#0106F……那样的话，\x01",
            "线索就中断了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x103,
        (
            "#6P#0200F……等一下，\x01",
            "建筑物内似乎还有人在。\x02",
        )
    )

    CloseMessageWindow()

    #N0086
    NpcTalk(
        0x9,
        "青年的声音",
        "……迟、迟到了的说～！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1DC3():

        label("loc_1DC3")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1DC3")

    QueueWorkItem2(0x0, 1, lambda_1DC3)

    def lambda_1DD5():

        label("loc_1DD5")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1DD5")

    QueueWorkItem2(0x1, 1, lambda_1DD5)

    def lambda_1DE7():

        label("loc_1DE7")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1DE7")

    QueueWorkItem2(0x2, 1, lambda_1DE7)

    def lambda_1DF9():

        label("loc_1DF9")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1DF9")

    QueueWorkItem2(0x3, 1, lambda_1DF9)
    Fade(500)
    OP_68(9180, 1400, 3560, 0)
    OP_0D()

    def lambda_1E22():
        OP_95(0xFE, 11480, 0, 3930, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E22)
    Sleep(100)
    OP_68(2630, 1400, 2250, 2700)
    WaitChrThread(0x9, 1)

    def lambda_1E54():
        OP_95(0xFE, 3740, 0, 3740, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E54)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    #C0087
    ChrTalk(
        0x9,
        (
            "#11P……啊？\x01",
            "这不是罗伊德警官嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#6P#0000F克潘先生，您来得正是时候。\x01",
            "稍微有些事情想\x01",
            "问问您，不知……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "#11P不行的说，\x01",
            "我在赶时间啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "#11P我现在必须要马上去参加在\x01",
            "乌尔斯拉间道的河滩上举办的\x01",
            "『费瑟尔杯』。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#12P#0105F费瑟尔杯……？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        "#12P#0305F就是那个钓鱼比赛吧？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "#11P你也知道吗？\x01",
            "身为垂钓爱好者，当然不能置身事外的说～\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "#11P之所以将比赛名定为费瑟尔杯，\x01",
            "是为了赞誉钓公师团的名誉会长\x01",
            "费瑟尔氏的功绩……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "#11P……哎呀，已经没空\x01",
            "在这里闲扯了！\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "#11P要是再不快点，有利的钓鱼点\x01",
            "就会被前辈们抢先占领的说～！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#6P#0011F再、再问一个！再问一个问题就好！\x02\x03",

            "#0000F请问，在参加钓鱼大赛的人\x01",
            "里面，有没有一位蓝色头发，\x01",
            "戴着眼镜的白衣男性呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        "#11P嗯嗯？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "#11P莫非你指的是\x01",
            "约亚西姆先生吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        "#11P他今天应该会来参加的说。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        "#12P#0301F……看来是猜对了啊。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#6P#0001F……嗯。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "#11P……莫非，你们几位也要\x01",
            "去参加大赛吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        "#11P那样的话，把这个给你们吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0105
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34, 1)

    #C0106
    ChrTalk(
        0x101,
        "#6P#0005F哎！这、这是……？\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "#12P#11P只要是费瑟尔杯的参加者，\x01",
            "都可以免费得到这个的说，\x01",
            "也就是所谓的参加奖。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#6P#0006F（其实根本就没说过要参加啊……\x01",
            "  这样真的好吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "#11P……啊，把已经迟到的事情\x01",
            "都忘了的说！\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "#11P我得快走了，以后再聊吧！\x01",
            "你们也抓紧时间吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(940, 1400, 910, 1000)
    OP_95(0x9, -1250, 0, -1260, 7000, 0x0)

    def lambda_238C():
        OP_95(0xFE, -3050, 0, -3060, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_238C)

    def lambda_23A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_23A6)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    Sleep(500)

    #C0111
    ChrTalk(
        0x102,
        (
            "#11P#0105F……匆匆忙忙地\x01",
            "就跑出去了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#5P#0003F总之……\x02\x03",

            "#0000F约亚西姆医生似乎\x01",
            "是去了位于乌尔斯拉间道中段的\x01",
            "河滩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#6P#0200F赶快出发的说。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        "#12P#0309F……他说话的腔调传染给你了啊，阿缇。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        "#6P#0203F…………………………\x02",
    )

    OP_57(0x1)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 1210, 0, 1210, 45)
    SetChrPos(0x1, 1210, 0, 1210, 45)
    SetChrPos(0x2, 1210, 0, 1210, 45)
    SetChrPos(0x3, 1210, 0, 1210, 45)
    OP_4C(0x9, 0xFF)
    OP_49()
    OP_68(1210, 1400, 1210, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_29(0x16, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_8_1A71 end

    def Function_9_2555(): pass

    label("Function_9_2555")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x9, 0xFF)
    OP_68(-2830, 1100, 51870, 0)
    MoveCamera(41, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18470, 0)
    SetChrPos(0x101, -3450, 0, 51000, 0)
    SetChrPos(0x102, -3450, 0, 49640, 0)
    SetChrPos(0x103, -2510, 0, 51000, 0)
    SetChrPos(0x104, -2510, 0, 49640, 0)
    SetChrPos(0x9, -1490, 0, 45300, 315)
    SetChrFlags(0x9, 0x40)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    LoadEffect(0x7, "event\\eva00_00.eff")
    FadeToBright(1000, 0)
    OP_0D()

    #C0116
    ChrTalk(
        0x102,
        "#6P#0105F这是……好大的鱼缸啊。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        "#11P#0202F有鱼在里面游动，看上去好像很安宁自得呢。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#6P#0003F说起来，鱼鳞\x01",
            "会反射光线，所以看上去闪闪发亮啊。\x02\x03",

            "#0000F『温暖的水中小乐园』……\x01",
            "莫非指的就是这里吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(860, 0, 100, 0)
    PlayEffect(0x7, 0x7, 0xFF, 0x0, -3230, 1000, 53150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    StopEffect(0x7, 0x2)
    Sleep(500)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0119
    ChrTalk(
        0x101,
        "#6P#0005F啊……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x104,
        "#12P#0305F里面好像落入了什么东西啊！？\x02",
    )

    CloseMessageWindow()

    #N0121
    NpcTalk(
        0x9,
        "青年的声音",
        "那个，怎么了？\x02",
    )

    CloseMessageWindow()
    OP_68(-3020, 1400, 49800, 1800)
    BeginChrThread(0x9, 1, 0, 10)
    Sleep(300)

    def lambda_2834():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2834)

    def lambda_2841():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2841)

    def lambda_284E():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_284E)

    def lambda_285B():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_285B)
    WaitChrThread(0x9, 1)

    #C0122
    ChrTalk(
        0x102,
        (
            "#5P#0100F抱歉，真是打扰了。\x01",
            "说来话长……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#5P#0000F总之，有张卡片掉进了\x01",
            "这个鱼缸里，请问能不能想个办法\x01",
            "帮我们拿出来呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        "#12P哎……？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0125
    ChrTalk(
        0x9,
        "#12P我觉得那个很难做到的说。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "#12P看来只有用钓鱼钩之类的东西\x01",
            "把它勾上来啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        "#12P总不能直接跳进鱼缸里吧。\x02",
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
    Sleep(1200)

    #C0128
    ChrTalk(
        0x103,
        "#11P#0200F果然只能如此了啊……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        "#11P#0306F是啊，而且要将它勾上来可需要相当高超的技术……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "#12P嗯～没办法的说～\x01",
            "让我来钓钓看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-3150, 1200, 49570, 0)
    MoveCamera(41, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18470, 0)
    SetChrPos(0x101, -3080, 0, 49720, 0)
    SetChrPos(0x102, -3880, 0, 47530, 0)
    SetChrPos(0x103, -2670, 0, 48590, 0)
    SetChrPos(0x104, -2670, 0, 47530, 0)
    SetChrPos(0x9, -3010, 0, 51090, 180)
    Sleep(1200)
    Sound(11, 0, 100, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0131
    ChrTalk(
        0x9,
        "#5P钓到啦。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#6P#0012F不、不愧是钓公师团的成员……\x02\x03",

            "#0000F给您添了那么多麻烦，实在是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "#5P没什么啦，不必客气的说。\x01",
            "这种程度对我来说，不过就是饭前小运动而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "#5P话说回来……那卡片\x01",
            "到底是什么啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#6P#0006F哎，这～这个嘛……\x01",
            "说起来就很复杂了……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "#5P……嗯～？\x01",
            "算啦，是什么都无所谓的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        (
            "#6P#0301F噢，罗伊德，\x01",
            "赶快看看卡片上说了什么吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C9E():

        label("loc_2C9E")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_2C9E")

    QueueWorkItem2(0x102, 1, lambda_2C9E)

    def lambda_2CB0():

        label("loc_2CB0")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_2CB0")

    QueueWorkItem2(0x104, 1, lambda_2CB0)

    def lambda_2CC2():

        label("loc_2CC2")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_2CC2")

    QueueWorkItem2(0x103, 1, lambda_2CC2)
    OP_95(0x101, -3920, 0, 48810, 1000, 0x0)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x103, 0x1)

    def lambda_2CF4():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CF4)

    def lambda_2D01():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D01)

    def lambda_2D0E():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D0E)

    def lambda_2D1B():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D1B)
    Sleep(300)

    #C0138
    ChrTalk(
        0x102,
        "#6P#0105F嗯，我来看看……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, 90, -1, 3)
    SetChrName("")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "９－７－１４－９－１９\x01",
            " 前去查看发出喑哑响声\x01",
            "　　 的中央之箱吧　　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    #C0140
    ChrTalk(
        0x104,
        (
            "#12P#0301F什么意思啊……完全搞不懂。\x01",
            "前面那些数字是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x103,
        (
            "#11P#0200F或许是暗号的一种吧。\x02\x03",

            "#0203F比如说……看上去是数字，\x01",
            "其实却是指代一些文字。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        (
            "#6P#0003F是啊……\x01",
            "思考一下各种可能性，然后再去探索吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -2910, 0, 49460, 0)
    SetChrPos(0x9, -520, 0, 43310, 90)
    ClearChrFlags(0x9, 0x40)
    OP_4C(0x9, 0xFF)
    OP_CA(0x1, 0xFF, 0x0)
    OP_65(0x1, 0x1)
    OP_29(0x22, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_2555 end

    def Function_10_2F8E(): pass

    label("Function_10_2F8E")

    OP_95(0x9, -3370, 0, 47470, 1500, 0x0)
    OP_93(0x9, 0x0, 0x1F4)
    Return()

    # Function_10_2F8E end

    def Function_11_2FAA(): pass

    label("Function_11_2FAA")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(6970, 1400, 7010, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19720, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_302B")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0xEF, 7400, 0, 6250, 0)
    SetChrPos(0x153, 6200, 0, 5050, 0)
    Jump("loc_3153")

    label("loc_302B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_309D")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)
    SetChrPos(0x109, 6200, 0, 3850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_3153")

    label("loc_309D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_310F")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)
    SetChrPos(0x10A, 6200, 0, 3850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_3153")

    label("loc_310F")

    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)

    label("loc_3153")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    Return()

    # Function_11_2FAA end

    def Function_12_3177(): pass

    label("Function_12_3177")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3195")
    Jump("loc_31CF")

    label("loc_3195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31B2")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_31CF")

    label("loc_31B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31CF")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_31CF")

    label("loc_31CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31E2")
    Jump("loc_31FF")

    label("loc_31E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31F5")
    Jump("loc_31FF")

    label("loc_31F5")

    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_31FF")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 5410, 0, 6840, 45)
    TurnDirection(0x8, 0x0, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Return()

    # Function_12_3177 end

    def Function_13_3221(): pass

    label("Function_13_3221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34C0")

    #C0143
    ChrTalk(
        0x8,
        (
            "钓公师团为了普及钓鱼文化，提高钓鱼技术\x01",
            "而设立了『等级认定考试』。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "在对你的钓鱼技术进行鉴定后，\x01",
            "我们还会授予各种荣誉称号及奖品哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "嗯，因为罗伊德团员才刚刚入团，\x01",
            "所以现在的等级是『新手钓师』。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33DE")

    #C0146
    ChrTalk(
        0x8,
        (
            "提升至下一个等级的条件是\x01",
            "钓得『４种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "打开钓鱼手册，就可以查看\x01",
            "已经钓到过的鱼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        "如果钓到４种以上的话，一定要来报告啊。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "哇哈哈，钓鱼很快乐吧？\x01",
            "多下些工夫，继续挑战吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B8")

    label("loc_33DE")


    #C0150
    ChrTalk(
        0x8,
        (
            "提升至下一个等级的条件是\x01",
            "钓到『４种以上的鱼』……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "……嗯，怎么了。\x01",
            "已经钓到过４种以上的鱼了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "嗯，反正我会仔细检查\x01",
            "你的钓鱼手册的。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "要检查的话，就再来找我吧。\x01",
            "哇哈哈，要进行升至下个等级的鉴定吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B8")

    SetScenarioFlags(0x69, 6)
    Jump("loc_52A4")

    label("loc_34C0")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_37A0")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赛尔丹分部长检查了\x01",
            "罗伊德的钓鱼手册。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0155
    ChrTalk(
        0x8,
        (
            "噢……罗伊德团员，\x01",
            "你的钓鱼成果挺不错呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x8,
        (
            "干得好。\x01",
            "从今天开始，你就是『业余钓师』了！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "等级上升为『业余钓师』！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "作为褒奖，",
            scpstr(SCPSTR_CODE_ITEM, 0x5A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x5A, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0159
    ChrTalk(
        0x8,
        (
            "这是我以前\x01",
            "爱用的草帽，\x01",
            "钓鱼的时候就戴着它吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "罗伊德团员，把这个带在身上，\x01",
            "今后也继续努力钓鱼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        (
            "#0002F这是钓鱼的必备道具啊，\x01",
            "那我就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x8,
        (
            "嗯，『业余钓师』的话，级别只能算是\x01",
            "马马虎虎，如果继续提高等级，\x01",
            "还能得到更多豪华的奖品哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "呵呵……顺便把下一个等级的\x01",
            "鉴定条件告诉你好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x8,
        (
            "如果想提升至下一个等级，\x01",
            "就必须钓到『８种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        "多下些工夫，努力去挑战吧。\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_38AC")

    label("loc_37A0")


    #C0166
    ChrTalk(
        0x8,
        (
            "罗伊德团员现在的等级是\x01",
            "『新手钓师』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x8,
        (
            "如果想提升至下一个等级，\x01",
            "就要钓到『４种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "如果想知道自己目前已经钓到过哪几种鱼，\x01",
            "只要查看钓鱼手册，就全都一目了然啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x8,
        (
            "呵呵……等垂钓有了更大成果之后，再将手册拿来给我看吧。\x01",
            "到时我会给你鉴定等级的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38AC")

    Jump("loc_52A4")

    label("loc_38B1")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3D38")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0170
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赛尔丹分部长检查了\x01",
            "罗伊德的钓鱼手册。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0171
    ChrTalk(
        0x8,
        (
            "噢……罗伊德团员\x01",
            "你的钓鱼成果相当不错呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x8,
        (
            "做得好。\x01",
            "从今天开始，你就是『专业钓师』啦！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "等级上升为『专业钓师』！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "作为褒奖，",
            scpstr(SCPSTR_CODE_ITEM, 0x9E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x9E, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0175
    ChrTalk(
        0x8,
        (
            "你又让我回忆起了自己\x01",
            "刚成为『专业钓师』的那一天……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "原本就喜好钓鱼的我，出于工作原因\x01",
            "去了利贝尔王国，在那里遇到了一名\x01",
            "自称是『钓公师团』成员的男子。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x8,
        (
            "哇哈哈，不用我说，恐怕你也猜到了，\x01",
            "他就是传说中的钓师费瑟尔团长！\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "经过一番曲折之后，团长亲自将\x01",
            "『专业钓师』的等级授予我了。\x01",
            "真是怀念啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#0012F是、是这样啊。\x01",
            "（分部长的过往经历吗……\x01",
            "  似乎要讲上很久呢。）\x02\x03",

            "#0000F哎，不过，因为工作原因\x01",
            "而前往利贝尔王国……\x01",
            "莫非您以前是贸易商之类的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x8,
        (
            "哇哈哈，不不不，\x01",
            "只是帮我家老头子做些事。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x8,
        (
            "虽然还算是精明能干，但现在\x01",
            "因为分部长的工作而忙得不可开交啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#0012F啊，原来如此……\x01",
            "（果然是个把兴趣摆在第一位的人呀……）\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        (
            "哦……忘了一件事。\x01",
            "把下一个等级的鉴定条件\x01",
            "告诉你吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x8,
        (
            "罗伊德团员，如果想提升至下一个等级，\x01",
            "就必须钓到『１２种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        (
            "这可需要花费相当多的工夫啊，\x01",
            "好好努力吧！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_3DF1")

    label("loc_3D38")


    #C0186
    ChrTalk(
        0x8,
        (
            "罗伊德团员的等级是\x01",
            "『业余钓师』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x8,
        (
            "如果想提升至下一个等级，\x01",
            "就必须钓到『８种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x8,
        (
            "呵呵……等垂钓有了更大成果之后，再将手册拿来给我看吧。\x01",
            "到时我会给你鉴定等级的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF1")

    Jump("loc_52A4")

    label("loc_3DF6")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42AC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_41EC")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赛尔丹分部长检查了\x01",
            "罗伊德的钓鱼手册。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0190
    ChrTalk(
        0x8,
        (
            "噢……罗伊德团员，\x01",
            "你的钓鱼成果真是相当了得呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x8,
        (
            "干得漂亮。\x01",
            "从今天开始，你就是『二级钓师』了！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    #A0192
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "等级上升为『二级钓师』！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(17, 0, 100, 0)

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "作为褒奖，",
            scpstr(SCPSTR_CODE_ITEM, 0xA4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33E, 1)
    AddItemNumber(0xA4, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0195
    ChrTalk(
        0x8,
        (
            "你还真有一套啊，罗伊德团员。\x01",
            "我以前取得『二级钓师』这个等级时\x01",
            "也是下了相当大的苦功。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x8,
        (
            "哇哈哈，想当年，我还\x01",
            "钻到深山老林中去修行……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        (
            "在大自然中不断磨练自己的感觉，\x01",
            "最后终于钓到了稀有的珍珠草，\x01",
            "才成为了『二级钓师』！\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "……罗伊德团员也很辛苦吧，但你付出\x01",
            "的这份汗水，正是钓师的勋章啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x8,
        (
            "罗伊德团员，今后也继续努力吧，\x01",
            "我期待着你的活跃表现！\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#0009F哈哈，谢谢您。\x02\x03",

            "#0000F话说回来……既然是『二级』，\x01",
            "那肯定也有『一级』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "这个自然，\x01",
            "接下来的等级就是『一级钓师』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "如果想晋升为『一级钓师』，\x01",
            "就要钓到『１６种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x8,
        (
            "罗伊德团员终于也步入\x01",
            "高等级成员的队伍了啊。\x01",
            "哇哈哈，我也很期待你今后的表现！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_42A7")

    label("loc_41EC")


    #C0204
    ChrTalk(
        0x8,
        (
            "罗伊德团员的等级是\x01",
            "『专业钓师』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x8,
        (
            "如果想提升至下一个等级，\x01",
            "就必须钓到『１２种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x8,
        (
            "呵呵……等垂钓有了更大成果之后，再将手册拿来给我看吧。\x01",
            "到时我会给你鉴定等级的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42A7")

    Jump("loc_52A4")

    label("loc_42AC")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4796")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0207
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赛尔丹分部长检查了\x01",
            "罗伊德的钓鱼手册。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0208
    ChrTalk(
        0x8,
        (
            "噢……看来你的钓鱼成果\x01",
            "还真的再度提高了呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x8,
        (
            "罗伊德团员，你非常了不起。\x01",
            "从今天开始，你就是『一级钓师』了！\x01",
            "哎呀，你还真是厉害啊！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "等级上升为『一级钓师』！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33F, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0212
    ChrTalk(
        0x8,
        (
            "罗伊德团员终于也成为『一级钓师』了吗，\x01",
            "速度还真是快啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x8,
        (
            "我大概在五六年前取得了这个等级，\x01",
            "这也是我决心在克洛斯贝尔\x01",
            "设立分部的契机。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        (
            "回想当年，在我做出这个提议的时候，\x01",
            "费瑟尔团长感动得眼含热泪……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0215
    ChrTalk(
        0x8,
        (
            "……好啦。\x01",
            "罗伊德团员，接下来\x01",
            "告诉你一件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "成为一级钓师的人，\x01",
            "就可以在本分部购买\x01",
            "『熬炼丸子ＤＸ』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x8,
        (
            "这是我们研制出来的\x01",
            "万能鱼饵哦，\x01",
            "各种鱼类都会来吃的。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#0005F这好像是全新的鱼饵啊。\x02\x03",

            "#0008F……我记得如果更换鱼饵，\x01",
            "就能钓到不同种类的鱼，\x01",
            "这样一来，就可以尝试其它搭配了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        "哇哈哈，不愧是罗伊德团员啊。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        (
            "如你所说，即使是在常去的钓鱼点，\x01",
            "一旦更换了鱼饵，也相当于进入了全新的垂钓世界。\x01",
            "多去尝试一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x8,
        (
            "接下来……就把下一个等级\x01",
            "的鉴定条件告诉你吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "接下来的等级可就是『特级钓师』了。\x01",
            "如果想成为『特级钓师』，\x01",
            "就必须钓到『２３种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x8,
        (
            "这个条件实在是相当艰难呢……\x01",
            "但还是要努力去挑战呀，罗伊德团员！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_48AE")

    label("loc_4796")


    #C0224
    ChrTalk(
        0x8,
        (
            "罗伊德团员的等级是『二级钓师』啊。\x01",
            "虽然这个等级已经很厉害了……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x8,
        (
            "但如果想提升至下一个等级，\x01",
            "就必须钓到『１６种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        (
            "尝试各种鱼饵，寻找各种钓鱼点，\x01",
            "确实是很耗费精力的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "呵呵……等垂钓有了更大成果之后，再将手册拿来给我看吧。\x01",
            "到时我会给你鉴定等级的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48AE")

    Jump("loc_52A4")

    label("loc_48B3")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DFA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4CAF")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0228
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赛尔丹分部长检查了\x01",
            "罗伊德的钓鱼手册。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0229
    ChrTalk(
        0x8,
        (
            "噢……！？\x01",
            "连那梦幻之鱼『锦鲤』和『金鲑』\x01",
            "也都被你钓到了吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        (
            "罗伊德团员，你真是太了不起啦。\x01",
            "从今天开始，你就是『特级钓师』了！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "等级上升为『特级钓师』！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x340),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x37),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x340, 1)
    AddItemNumber(0x37, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0234
    ChrTalk(
        0x8,
        (
            "罗伊德团员终于升到了\x01",
            "和我同样的等级了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x8,
        (
            "从今以后，无论是对于金鲑那绝妙的尾鳍角度，\x01",
            "还是钓到锦鲤时的那种独特手感……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "我们都可以畅所欲言\x01",
            "地进行交流啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "哇哈哈，所谓的特级钓师，就是要对\x01",
            "有关垂钓的一切事情都知无不尽。\x01",
            "可以尽情讨论的朋友又多了一个，我真是很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x8,
        (
            "……罗伊德团员，我已经没有什么东西可以教你了。\x01",
            "从今以后，就请你尽情贯彻自己的钓鱼之道吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        (
            "#0009F哈哈哈……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        (
            "不过，在克洛斯贝尔的某处，\x01",
            "还栖息着传说中的鱼王，\x01",
            "它可是个超级庞然大物。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        (
            "这次送给你的钓竿『水中魔法师』\x01",
            "就蕴藏着将其钓到的可能性……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x8,
        (
            "罗伊德团员，如果你有此意向的话，\x01",
            "就去挑战传说中的鱼王吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    Call(0, 12)
    Jump("loc_4DF5")

    label("loc_4CAF")


    #C0243
    ChrTalk(
        0x8,
        (
            "罗伊德团员的等级是『一级钓师』啊。\x01",
            "在如此短的时间内就能取得如此成绩，真是很了不起。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x8,
        (
            "但是，在此之上，还有更高的等级\x01",
            "『特级钓师』在等着你。\x01",
            "授予条件是钓到『２３种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x8,
        (
            "确实是相当困难啊……\x01",
            "必须要把『锦鲤』\x01",
            "和『金鲑』也给钓到才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x8,
        (
            "……罗伊德团员，等你取得更大的垂钓成果后，\x01",
            "就来这里将手册拿给我看吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF5")

    Jump("loc_52A4")

    label("loc_4DFA")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52A4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_51AA")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0247
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赛尔丹分部长检查了\x01",
            "罗伊德的钓鱼手册。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0248
    ChrTalk(
        0x8,
        (
            "什么……！？\x01",
            "罗伊德团员，你竟然钓到了\x01",
            "传说中的『霸王蛇鱼』吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x8,
        (
            "难以置信……\x01",
            "终于成功了啊，\x01",
            "哇哈哈哈……！\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#0005F那、那个果然就是\x01",
            "传说中的鱼王啊。\x02\x03",

            "#0003F尺寸非常大，\x01",
            "当时确实是吃了一惊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "这家伙可是咱们克洛斯贝尔\x01",
            "分部的全体成员常年追寻的\x01",
            "最大对手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x8,
        "你竟然能把它给钓到……\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "好！现在就授予你\x01",
            "特别的称号吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x8,
        (
            "那就是『钓圣』……\x01",
            "这可是每个分部中仅限一人\x01",
            "才能得到的传说称号哦！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    #A0255
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "得到了『钓圣』的称号！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    #A0256
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x60),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x60, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0257
    ChrTalk(
        0x8,
        (
            "居然能超越我，\x01",
            "成为钓圣……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "今后也请多多关照了，\x01",
            "『克洛斯贝尔的钓圣』！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#0012F唔……总觉得有点不好意思呢。\x02\x03",

            "#0000F嗯，总之，长久以来承蒙关照了。\x01",
            "今后也请您继续\x01",
            "指点我。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "喔，罗伊德团员还真是\x01",
            "谦虚啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "哇哈哈，真是名不虚传呀！\x01",
            "哇哈哈哈哈……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    Call(0, 12)
    Jump("loc_52A4")

    label("loc_51AA")


    #C0262
    ChrTalk(
        0x8,
        "罗伊德团员的等级是『特级钓师』啊。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x8,
        (
            "在钓公师团的克洛斯贝尔分部，\x01",
            "已经没有等级比你更高的成员了。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x8,
        (
            "不过，如果是罗伊德团员的话，\x01",
            "说不定还能钓到更大的家伙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        (
            "哇哈哈，如果以后真的钓到了，\x01",
            "可一定要拿来给我看看呀。\x01",
            "我可是很想拜见一下的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52A4")

    Return()

    # Function_13_3221 end

    def Function_14_52A5(): pass

    label("Function_14_52A5")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52CA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_52CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52E5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_52E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5300")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5300")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_531B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_531B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5336")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5336")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5351")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5351")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_536C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_536C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5387")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5387")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53A2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_53A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53BD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_53BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53D8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_53D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53F3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_53F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_540E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_540E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5429")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5429")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5444")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5444")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_545F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_545F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_547A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_547A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5495")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5495")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54B0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_54B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54CB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_54CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54E6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_54E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5501")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5501")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_551C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_551C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5537")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5537")

    Return()

    # Function_14_52A5 end

    def Function_15_5538(): pass

    label("Function_15_5538")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0266
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放着书籍《简单的鱼类料理》。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_END)), "loc_55EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55EE")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法写在书里。\x02",
        )
    )

    CloseMessageWindow()

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x8)

    label("loc_55EE")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_15_5538 end

    SaveToFile()

Try(main)
