from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1020.bin",                # FileName
        "c1020",                    # MapName
        "c1020",                    # Location
        0x0014,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 20, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1020",                  # 0
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
    DeclNpc(-519,    0,       43310,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(7530,    0,       6780,    0,    261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(6580,    0,       7980,    1500,    7230,    1500,    9070,    0x007E, 0,  3,  0x0000)
    DeclActor(470,     0,       43660,   1200,    470,     1500,    43360,   0x007C, 0,  14, 0x0000)

    ScpFunction((
        "Function_0_178",          # 00, 0
        "Function_1_230",          # 01, 1
        "Function_2_3DC",          # 02, 2
        "Function_3_410",          # 03, 3
        "Function_4_414",          # 04, 4
        "Function_5_F07",          # 05, 5
        "Function_6_25BE",         # 06, 6
        "Function_7_2AB0",         # 07, 7
        "Function_8_349B",         # 08, 8
        "Function_9_375E",         # 09, 9
        "Function_10_3F6E",        # 0A, 10
        "Function_11_413B",        # 0B, 11
        "Function_12_41F8",        # 0C, 12
        "Function_13_627E",        # 0D, 13
        "Function_14_6511",        # 0E, 14
    ))


    def Function_0_178(): pass

    label("Function_0_178")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1B8"),
        (1, "loc_1C4"),
        (2, "loc_1D0"),
        (3, "loc_1DC"),
        (4, "loc_1E8"),
        (5, "loc_1F4"),
        (6, "loc_200"),
        (SWITCH_DEFAULT, "loc_20C"),
    )


    label("loc_1B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_200")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_20C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_22F")

    Return()

    # Function_0_178 end

    def Function_1_230(): pass

    label("Function_1_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_26A")
    SetChrPos(0x9, -3550, 0, 51630, 0)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 4310, 0, 310, 90)
    Jump("loc_3B5")

    label("loc_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_27D")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_290")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2A3")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B1")
    Jump("loc_3B5")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2C4")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2D7")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_2D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2F6")
    SetChrPos(0xA, 4310, 0, 310, 90)
    Jump("loc_3B5")

    label("loc_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_304")
    Jump("loc_3B5")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_317")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_3B5")

    label("loc_317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_32A")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_3B5")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_342")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_3B5")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_37E")
    SetChrPos(0x9, -3550, 0, 51630, 0)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_379")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_379")

    Jump("loc_3B5")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3B5")
    SetChrPos(0x9, -3550, 0, 51630, 0)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B5")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_3B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DB")
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_3DB")

    Return()

    # Function_1_230 end

    def Function_2_3DC(): pass

    label("Function_2_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F8")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_40F")

    label("loc_3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_40F")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_40F")

    label("loc_40F")

    Return()

    # Function_2_3DC end

    def Function_3_410(): pass

    label("Function_3_410")

    Call(0, 4)
    Return()

    # Function_3_410 end

    def Function_4_414(): pass

    label("Function_4_414")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43E")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Call(0, 9)
    Return()

    label("loc_43E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_CCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_581")

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

    label("loc_581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8BB")

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

    label("loc_8BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_9D9")

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
            "是这么回事。\x02\x03",

            "#0005F不对，我是\x01",
            "什么时候……加入\x01",
            "钓公师团的啊？\x02\x03",

            "#0003F我只记得自己曾经收下过\x01",
            "克潘先生赠送的钓竿而已……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF2")

    label("loc_9D9")


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

    label("loc_AF2")


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

    label("loc_CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_END)), "loc_EF9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF4")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D93")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_D3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5E")
    OP_AF(0x37)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D8E")

    label("loc_D5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D72")
    Jump("loc_D8E")

    label("loc_D72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_D8E")

    Jump("loc_EEF")

    label("loc_D93")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6F")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_DE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E05")
    Call(0, 13)
    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E6A")

    label("loc_E05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3A")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E29")
    OP_AF(0x36)
    Jump("loc_E2B")

    label("loc_E29")

    OP_AF(0x37)

    label("loc_E2B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E6A")

    label("loc_E3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E4E")
    Jump("loc_E6A")

    label("loc_E4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_E6A")

    Jump("loc_EEF")

    label("loc_E6F")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBF")
    Call(0, 13)
    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EEF")

    label("loc_EBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED3")
    Jump("loc_EEF")

    label("loc_ED3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_EEF")

    Jump("loc_CE0")

    label("loc_EF4")

    Jump("loc_EFC")

    label("loc_EF9")

    Call(0, 5)

    label("loc_EFC")

    TalkEnd(0x8)
    OP_93(0x8, 0xB4, 0x0)
    Return()

    # Function_4_414 end

    def Function_5_F07(): pass

    label("Function_5_F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_F8B")

    #C0029
    ChrTalk(
        0x8,
        (
            "这条街最西边的建筑\x01",
            "是一栋名为洋槐庄园的公寓。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "没记错的话，应该有一间房一直空着。\x01",
            "你们要找的应该就是那里吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BD")

    label("loc_F8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1395")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D9")

    #C0031
    ChrTalk(
        0x8,
        "罗伊德团员，你听说过这个传闻吗？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "在克洛斯贝尔，栖息着传说中的鱼王\x01",
            "——『霸王蛇鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "它们以艾鲁姆湖为主要栖息地，\x01",
            "性情可谓凶残非常，\x01",
            "据说在从前，连渔民都惧怕它们。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "但是，最近这十几年来，\x01",
            "却几乎没有人目击过它们……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "如果能把这家伙钓上来，\x01",
            "毫无疑问就能得到荣誉勋章了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1195")

    label("loc_10D9")


    #C0036
    ChrTalk(
        0x8,
        (
            "『霸王蛇鱼』简直是\x01",
            "鱼王中的鱼王……\x01",
            "钓到那家伙可是我们钓公师团的共同梦想。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "虽然这十几年来都没有人目击过它们，\x01",
            "但如果是已经成为『特级钓师』的你，\x01",
            "说不定还真有可能将它钓上来吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1195")

    Jump("loc_1390")

    label("loc_119A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131C")

    #C0038
    ChrTalk(
        0x8,
        (
            "不愧是罗伊德团员，\x01",
            "都成了『钓圣』还这么谦虚。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "哇哈哈，我非常欣赏你！\x01",
            "今天晚上不如去夜钓吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "我们分部在举办联欢会时，\x01",
            "就经常会去夜钓！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
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

    #C0042
    ChrTalk(
        0x8,
        "哇哈哈哈，连拒绝的方式都这么谦逊有礼！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "好吧！那等你有空时，就来和我说。\x01",
            "到时候连同庆祝会一起，举办一场钓鱼大赛吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1390")

    label("loc_131C")


    #C0044
    ChrTalk(
        0x8,
        (
            "一定要庆祝罗伊德团员\x01",
            "取得了『钓圣』的称号啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "到时候把你钓到霸王蛇鱼的神勇经过\x01",
            "慢慢说给我听吧，哇哈哈哈！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1390")

    Jump("loc_25BD")

    label("loc_1395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_140B")

    #C0046
    ChrTalk(
        0x8,
        (
            "太阳下山了啊……\x01",
            "不然就去市外的\x01",
            "什么地方逛逛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "我感觉今晚的夜钓\x01",
            "会遇到前所未闻的\x01",
            "大家伙哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BD")

    label("loc_140B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_14D9")

    #C0048
    ChrTalk(
        0x8,
        (
            "奇怪了……\x01",
            "联系不上约亚西姆大师。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "我们可是昨晚就约好\x01",
            "要一起去夜钓的。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0006F（……莫非还在埋头检验\x01",
            "  那个药物的成分吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#0300F（如果是那位医生的话，\x01",
            "  应该很有可能吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BD")

    label("loc_14D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1571")

    #C0052
    ChrTalk(
        0x8,
        (
            "金鲑是传说中的梦幻之鱼，\x01",
            "据说它栖息在玛因兹地区\x01",
            "的某个地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "流光溢彩的金色鳞片\x01",
            "排列成流线型……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "简直是鲑鱼中的\x01",
            "极品鲑鱼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BD")

    label("loc_1571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_16C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1665")

    #C0055
    ChrTalk(
        0x8,
        "罗伊德团员，不得了啦！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "今天早上，约亚西姆团员\x01",
            "钓起一条超级大的\x01",
            "锦鲤呢！！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "所以那家伙终于如愿以偿，\x01",
            "晋升为特级钓师了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#0200F约亚西姆医生……\x01",
            "还是老样子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#0000F等一会去向塞茜尔姐姐\x01",
            "告密吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16BB")

    label("loc_1665")


    #C0060
    ChrTalk(
        0x8,
        (
            "约亚西姆团员已经\x01",
            "升为特级钓师了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "从今往后，\x01",
            "不得不称呼他为约亚西姆大师了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BB")

    Jump("loc_25BD")

    label("loc_16C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_172C")

    #C0062
    ChrTalk(
        0x8,
        (
            "话说回来，罗伊德团员，\x01",
            "最近好像一直都没有看到你啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "没有退步吧，\x01",
            "有坚持一日一钓吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BD")

    label("loc_172C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_18CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185B")

    #C0064
    ChrTalk(
        0x8,
        (
            "其实我正考虑\x01",
            "趁着纪念庆典办一场比赛……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "我想从利贝尔\x01",
            "请一位\x01",
            "技艺高超的钓师来。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x8, 0x101, 500)

    #C0066
    ChrTalk(
        0x8,
        (
            "嗯，话说回来……\x01",
            "你的名字也是『罗伊德』呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        "哇哈哈，这可真巧……！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#0005F什、什么啊……？？\x01",
            "……怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "那个，没什么。\x01",
            "这事还没定下来呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18CA")

    label("loc_185B")


    #C0070
    ChrTalk(
        0x8,
        (
            "我正在考虑趁着纪念庆典，\x01",
            "从利贝尔请位\x01",
            "技艺高超的钓师来。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "就是所谓的特别嘉宾。\x01",
            "哇哈哈，很令人期待吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CA")

    Jump("loc_25BD")

    label("loc_18CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1A82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A1F")

    #C0072
    ChrTalk(
        0x8,
        (
            "这个时节的最佳晨钓地点\x01",
            "大概非乌尔斯拉间道莫属吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "其实在乌尔斯拉医院\x01",
            "有我们的同好。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "他经常在工作时间偷溜出来钓鱼，\x01",
            "他可是对垂钓十分痴迷呢，\x01",
            "哇哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0075
    ChrTalk(
        0x101,
        "#0005F乌尔斯拉医院的垂钓爱好者……？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        "#0306F不、不会是……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A7D")

    label("loc_1A1F")


    #C0077
    ChrTalk(
        0x8,
        (
            "这个时节的最佳晨钓地点\x01",
            "大概非乌尔斯拉间道莫属吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "罗伊德团员有兴趣的话\x01",
            "就去看看吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A7D")

    Jump("loc_25BD")

    label("loc_1A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1B17")

    #C0079
    ChrTalk(
        0x8,
        (
            "如果钓不到自己想钓的鱼，\x01",
            "可以试着变换钓竿或者鱼饵。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        "这样一来，能钓到的鱼就会随之变化了。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        "总之，整个过程就是要不断尝试。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25BD")

    label("loc_1B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1CF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C57")

    #C0082
    ChrTalk(
        0x8,
        "欢迎来到钓公师团。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "罗伊德团员，\x01",
            "垂钓还顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#0000F呵呵，还算过得去吧。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "是吗，不过听说你们\x01",
            "警察确实忙呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C0D")

    #C0086
    ChrTalk(
        0x8,
        (
            "有好成果时\x01",
            "一定要来报告哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "随着钓师等级的上升\x01",
            "我们会赠送豪华奖品哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C4F")

    label("loc_1C0D")


    #C0088
    ChrTalk(
        0x8,
        (
            "如果钓到了大家伙，\x01",
            "一定要来向我报告哦。\x01",
            "我很期待你的成果呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4F")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1CF0")

    label("loc_1C57")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB9")

    #C0089
    ChrTalk(
        0x8,
        (
            "等级认定考试的内容\x01",
            "就是要钓得\x01",
            "指定的鱼。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "有好成果时\x01",
            "一定要来报告哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF0")

    label("loc_1CB9")


    #C0091
    ChrTalk(
        0x8,
        (
            "罗伊德团员，如果再钓上大家伙\x01",
            "一定要来向我报告哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF0")

    Jump("loc_25BD")

    label("loc_1CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_202A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F99")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    TurnDirection(0xA, 0x101, 0)

    #C0092
    ChrTalk(
        0xA,
        "罗伊德团员，你听说了吗？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "其实前几天，我们分部又增加了\x01",
            "一个团员哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#0000F哎，是吗？\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "嗯，还是一位女钓师哦，\x01",
            "而且相当厉害。\x02",
        )
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
    Sleep(1200)

    #C0096
    ChrTalk(
        0xA,
        (
            "她叫艾丝蒂尔，\x01",
            "听说是个有名的游击士呢。\x01",
            "你没在杂志上看到过吗？\x02",
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
    Sleep(1200)

    #C0097
    ChrTalk(
        0x8,
        (
            "我也跟她一起\x01",
            "去钓过一次鱼，\x01",
            "真不愧是游击士，反应就是敏捷……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "哼哼，罗伊德团员，\x01",
            "强敌出现了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#0006F之前便已经\x01",
            "是强敌了……\x01",
            "（没想到她连钓鱼都会……）\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        (
            "#0300F艾丝蒂尔，\x01",
            "好像无所不能啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x6C, 6)
    Jump("loc_2025")

    label("loc_1F99")


    #C0101
    ChrTalk(
        0x8,
        (
            "听说艾丝蒂尔团员\x01",
            "在利贝尔王国时\x01",
            "就喜欢上钓鱼了……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "说到利贝尔\x01",
            "那可是我们钓公师团的创办地。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "罗伊德团员，你可\x01",
            "不能马虎大意哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2025")

    Jump("loc_25BD")

    label("loc_202A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_22E0")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20E8")

    #C0104
    ChrTalk(
        0x8,
        (
            "我们钓公师团\x01",
            "是为了普及钓鱼文化\x01",
            "而成立的团体。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "为了让大家更加具备上进心，\x01",
            "我们才实施了这个『等级认定考试』。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "有什么不懂的问题，\x01",
            "随时都可以来问我！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DB")

    label("loc_20E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2267")

    #C0107
    ChrTalk(
        0x8,
        (
            "不愧是罗伊德团员，\x01",
            "成了『钓圣』还如此谦虚。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "哇哈哈，我看好你哦！\x01",
            "今天晚上不如去夜钓吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "我们分部在举办联欢会时，\x01",
            "就经常会去夜钓！\x02",
        )
    )

    CloseMessageWindow()

    #C0110
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

    #C0111
    ChrTalk(
        0x8,
        "哇哈哈哈，连拒绝的方式都这么谦逊有礼！\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "好吧！那等你有空时，就来和我说。\x01",
            "到时候连同庆祝会一起，\x01",
            "举办一场钓鱼大赛吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_22DB")

    label("loc_2267")


    #C0113
    ChrTalk(
        0x8,
        (
            "一定要庆祝罗伊德团员\x01",
            "取得了『钓圣』的称号啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "到时候把你钓到霸王蛇鱼的神勇经过\x01",
            "慢慢说给我听吧，哇哈哈哈！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22DB")

    Jump("loc_25BD")

    label("loc_22E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_238D")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0115
    ChrTalk(
        0x8,
        (
            "克潘那小子，\x01",
            "又钓上大家伙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "彼德，这样的话，\x01",
            "我们也不能输给他哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "是啊，\x01",
            "我已经开始技痒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "呵呵，今晚\x01",
            "一起去\x01",
            "夜钓好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_25BD")

    label("loc_238D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2411")

    #C0119
    ChrTalk(
        0x8,
        (
            "彼德团员，\x01",
            "你知道我喜欢\x01",
            "比赛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "哇哈哈，那就开个溪流垂钓\x01",
            "大赛如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x102,
        "#0105F（他们是什么人啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_25BD")

    label("loc_2411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F6")

    #C0122
    ChrTalk(
        0x8,
        (
            "我们钓公师团\x01",
            "一直欢迎新人加入。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 0)

    #C0123
    ChrTalk(
        0x8,
        (
            "如何啊，年轻人，要不要\x01",
            "成为我们的伙伴呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "呵呵，如果是有经验的人，\x01",
            "我们更加欢迎哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#0006F抱歉，我们还在执行公务，所以……\x01",
            "（现在可没有那个空闲啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25BD")

    label("loc_24F6")


    #C0126
    ChrTalk(
        0x8,
        (
            "我们钓公师团\x01",
            "一直欢迎新人加入哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "如果你们觉得我在骗人，只需入团看看就好啦。\x01",
            "哇哈哈哈哈！\x02",
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
    Sleep(1200)

    label("loc_25BD")

    Return()

    # Function_5_F07 end

    def Function_6_25BE(): pass

    label("Function_6_25BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2637")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2609")

    #C0128
    ChrTalk(
        0xFE,
        "来，这是鱼食的说，\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        "多吃点吧。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2632")

    label("loc_2609")


    #C0130
    ChrTalk(
        0xFE,
        (
            "……剩下一些红虫没用完，\x01",
            "仅此而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2632")

    Jump("loc_2AAC")

    label("loc_2637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2645")
    Jump("loc_2AAC")

    label("loc_2645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_274F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C6")

    #C0131
    ChrTalk(
        0xFE,
        "啊，你们好。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "分部长他们在下边\x01",
            "有事请去找他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "先听听等级认定考试的事\x01",
            "是没有坏处的说。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x70, 6)
    Jump("loc_274A")

    label("loc_26C6")


    #C0134
    ChrTalk(
        0xFE,
        (
            "鱼饵不同，\x01",
            "可以钓到的鱼也会随之变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "如果钓不到自己想钓的鱼，\x01",
            "可以试着变换鱼饵的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "总之，鱼饵的选择就是不断尝试。\x02",
    )

    CloseMessageWindow()

    label("loc_274A")

    Jump("loc_2AAC")

    label("loc_274F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_28B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2841")

    #C0137
    ChrTalk(
        0xFE,
        (
            "咦，大家也是坐巴士\x01",
            "回来的吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "感觉我们乘坐的\x01",
            "好像不是同一班车的说……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        "……不过算了。\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "已经事先跟分部长他们说过了。\x01",
            "大家都在下边，\x01",
            "有事请去找他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "先听听等级认定考试的事\x01",
            "是没有坏处的说。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x70, 6)
    Jump("loc_28AE")

    label("loc_2841")


    #C0142
    ChrTalk(
        0xFE,
        "你们好。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "我经常来这里，\x01",
            "有什么不明白的地方，\x01",
            "可以随时问我的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "我会给你推荐\x01",
            "很棒的钓鱼点哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28AE")

    Jump("loc_2AAC")

    label("loc_28B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_28C1")
    Jump("loc_2AAC")

    label("loc_28C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295D")

    #C0145
    ChrTalk(
        0xFE,
        (
            "为什么我要\x01",
            "负责打扫鱼缸啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "啊，好累。\x01",
            "真麻烦……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#0005F这、这么大的鱼缸！\x01",
            "（这里到底是\x01",
            "  什么地方呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29AC")

    label("loc_295D")


    #C0148
    ChrTalk(
        0xFE,
        (
            "这个鱼缸是我们\x01",
            "从导力商店特别定做的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        "因为我们的分部长是个有钱人。\x02",
    )

    CloseMessageWindow()

    label("loc_29AC")

    Jump("loc_2AAC")

    label("loc_29B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A63")

    #C0150
    ChrTalk(
        0xFE,
        (
            "所谓的『钓公师团』，就是由一群\x01",
            "住在克洛斯贝尔的垂钓爱好者所组成的集团。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "嗯，我也算是团员之一的说。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "我是团员Ｎｏ．３，克潘。\x01",
            "等级是特级钓师的说。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AAC")

    label("loc_2A63")


    #C0153
    ChrTalk(
        0xFE,
        (
            "虽说也是团员，\x01",
            "但我却不太喜欢与他们一起行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "因为觉得很麻烦。\x02",
    )

    CloseMessageWindow()

    label("loc_2AAC")

    TalkEnd(0xFE)
    Return()

    # Function_6_25BE end

    def Function_7_2AB0(): pass

    label("Function_7_2AB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ADA")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Call(0, 9)
    Return()

    label("loc_2ADA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2C6F")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B85")

    #C0155
    ChrTalk(
        0xFE,
        (
            "哦！罗伊德团员，\x01",
            "这是要去夜钓？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "呵呵，加油哦。\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "以你的实力，说不定可以\x01",
            "获得特级钓师之上的称号哦。\x01",
            "我有这种预感。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BCB")

    label("loc_2B85")


    #C0158
    ChrTalk(
        0xFE,
        (
            "以你的实力，说不定可以\x01",
            "获得特级钓师之上的称号呢。\x01",
            "要加油夜钓哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BCB")

    Jump("loc_2C6A")

    label("loc_2BD0")


    #C0159
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "真不愧是罗伊德团员啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "入团后这么短的时间内\x01",
            "就成为了『钓圣』。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "呵呵，我们今后也要一起\x01",
            "把钓公师团·克洛斯贝尔分部\x01",
            "办得风生水起。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6A")

    Jump("loc_3497")

    label("loc_2C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2D08")

    #C0162
    ChrTalk(
        0xFE,
        (
            "从利贝尔来的客人\x01",
            "上周已经回国了。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "呵呵，通过与那位钓师的比赛，\x01",
            "我获得了很宝贵的经验。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "我必须要更加努力地\x01",
            "锻炼自己的技巧了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3497")

    label("loc_2D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2D82")

    #C0165
    ChrTalk(
        0xFE,
        (
            "今天我也打算\x01",
            "出去钓鱼哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "那位游击士\x01",
            "艾丝蒂尔小姐似乎\x01",
            "收获颇丰啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "呵呵，我可不能\x01",
            "输给她。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3497")

    label("loc_2D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E0F")

    #C0168
    ChrTalk(
        0xFE,
        (
            "罗伊德团员，\x01",
            "你去西克洛斯贝尔街道\x01",
            "看过吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "最近，导力巴士\x01",
            "又增加了好几班哦。\x01",
            "所以想到哪里钓鱼都可以了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E88")

    label("loc_2E0F")


    #C0170
    ChrTalk(
        0xFE,
        (
            "啊，对了，听说克潘\x01",
            "去了玛因兹山道。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "大概是在山道中段的巴士站下了车，\x01",
            "正在瀑布附近钓鱼吧。\x01",
            "那是他喜欢的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E88")

    Jump("loc_3497")

    label("loc_2E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_319F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312E")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    TurnDirection(0xA, 0x101, 0)

    #C0172
    ChrTalk(
        0xA,
        "罗伊德团员，你听说了吗？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "今天新加入了\x01",
            "一名团员哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        "#0000F哎，是吗？\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x8,
        (
            "嗯，还是一位女钓师哦，\x01",
            "而且相当厉害。\x02",
        )
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
    Sleep(1200)

    #C0176
    ChrTalk(
        0xA,
        (
            "她叫艾丝蒂尔，\x01",
            "听说是个有名的游击士呢。\x01",
            "你没在杂志上看到过吗？\x02",
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
    Sleep(1200)

    #C0177
    ChrTalk(
        0x8,
        (
            "我也跟她一起\x01",
            "去钓过一次鱼，\x01",
            "不愧是游击士，反应就是敏捷……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "哼哼，罗伊德团员，\x01",
            "强敌出现了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#0006F之前便已经\x01",
            "是强敌了……\x01",
            "（没想到她连钓鱼都会……）\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x104,
        (
            "#0300F艾丝蒂尔，\x01",
            "好像无所不能啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x6C, 6)
    Jump("loc_319A")

    label("loc_312E")


    #C0181
    ChrTalk(
        0xFE,
        (
            "听说艾丝蒂尔小姐在利贝尔\x01",
            "拥有很高等级的\x01",
            "钓师称号哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "虽然她好像工作很忙，\x01",
            "但我真想\x01",
            "跟她比试一次。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_319A")

    Jump("loc_3497")

    label("loc_319F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_33C0")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_328A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3241")

    #C0183
    ChrTalk(
        0xFE,
        "我已经从克潘那里听说了哦！\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "有新同伴加入\x01",
            "真是令人高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "如果钓到了大鱼\x01",
            "请一定要来哦。\x01",
            "我们都十分期待呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3285")

    label("loc_3241")


    #C0186
    ChrTalk(
        0xFE,
        (
            "呵呵，如果钓到了大鱼，\x01",
            "请一定再来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "我们都\x01",
            "十分期待呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3285")

    Jump("loc_33BB")

    label("loc_328A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3369")

    #C0188
    ChrTalk(
        0xFE,
        (
            "罗伊德团员，恭喜你获得\x01",
            "『钓圣』的称号。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "钓公师团在克洛斯贝尔和\x01",
            "利贝尔王国都有设立据点……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "成为『钓圣』的成员，\x01",
            "包括罗伊德团员你在内\x01",
            "也只有两名哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "『利贝尔的钓圣』听说\x01",
            "是名女游击士呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33BB")

    label("loc_3369")


    #C0192
    ChrTalk(
        0xFE,
        (
            "罗伊德团员，恭喜你获得\x01",
            "『钓圣』称号。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "今后我们也要把分部\x01",
            "办得风生水起。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BB")

    Jump("loc_3497")

    label("loc_33C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_33D1")
    Call(0, 4)
    Jump("loc_3497")

    label("loc_33D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3450")

    #C0194
    ChrTalk(
        0xFE,
        (
            "呵呵，在玛因兹山道\x01",
            "的溪流垂钓是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "真期待呢。\x01",
            "感觉好兴奋啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        "#0000F（他们好像正在聊天……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3497")

    label("loc_3450")


    #C0197
    ChrTalk(
        0xFE,
        (
            "各位如果有机会，\x01",
            "也请加入钓公师团。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        "呵呵，我们很欢迎各位哦。\x02",
    )

    CloseMessageWindow()

    label("loc_3497")

    TalkEnd(0xFE)
    Return()

    # Function_7_2AB0 end

    def Function_8_349B(): pass

    label("Function_8_349B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(470, 1400, 310, 0)
    MoveCamera(45, 33, 0, 0)
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
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(1850, 1400, 1760, 3000)
    MoveCamera(45, 34, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(20100, 3000)

    def lambda_358C():
        OP_95(0xFE, 1310, 0, 2330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_358C)

    def lambda_35A6():
        OP_95(0xFE, 2310, 0, 1130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_35A6)

    def lambda_35C0():
        OP_95(0xFE, 1310, 0, 130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_35C0)

    def lambda_35DA():
        OP_95(0xFE, 110, 0, 1130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_35DA)

    def lambda_35F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35F4)

    def lambda_3605():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3605)

    def lambda_3616():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3616)

    def lambda_3627():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3627)
    Sleep(3000)

    #C0199
    ChrTalk(
        0x101,
        (
            "#5P#0005F游击士协会的右侧……\x01",
            "嗯？这里应该是空无一人的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(3480, 1400, 3380, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24740, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_0D()
    Sleep(700)

    #C0200
    ChrTalk(
        0x103,
        (
            "#5P#0200F但怎么看\x01",
            "都不像是空着的呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x104,
        (
            "#11P#0300F总之先问问\x01",
            "接待人员吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1210, 0, 1210, 45)
    SetChrPos(0x1, 1210, 0, 1210, 45)
    SetChrPos(0x2, 1210, 0, 1210, 45)
    SetChrPos(0x3, 1210, 0, 1210, 45)
    ClearMapFlags(0x10000000)
    OP_29(0x3, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_8_349B end

    def Function_9_375E(): pass

    label("Function_9_375E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_68(5760, 1300, 6920, 0)
    MoveCamera(19, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22710, 0)
    SetChrPos(0x101, 4560, 0, 6480, 45)
    SetChrPos(0x102, 5370, 0, 5660, 45)
    SetChrPos(0x103, 3590, 0, 5480, 45)
    SetChrPos(0x104, 4390, 0, 4680, 45)
    OP_93(0x8, 0x87, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0202
    ChrTalk(
        0xA,
        (
            "#11P真想再来一次\x01",
            "垂钓之旅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x8,
        "#5P哇哈哈，真是期待呢。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#5P#0005F那个，不好意思。\x01",
            "我们是……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0x8, 0xE1, 0x1F4)
    OP_93(0xA, 0xE1, 0x1F4)
    Sleep(300)

    #C0205
    ChrTalk(
        0x8,
        (
            "#11P哦，是想入团吗？\x01",
            "哇哈哈，欢迎欢迎！\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xA,
        "#11P欢迎来到我们『钓公师团』！\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xA,
        (
            "#11P真开心啊，竟然会有这么多年轻人\x01",
            "想要加入我们团……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(10)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(10)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0208
    ChrTalk(
        0x104,
        "#6P#0305F加入……『钓公师团』……？\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        "#5P#0006F不好意思，这里到底是……\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x8,
        (
            "#11P哦，这里可是钓鱼爱好者的聚集地——\x01",
            "『钓公师团』的克洛斯贝尔分部呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x8,
        (
            "#11P嗯……穿夹克的年轻人，\x01",
            "你似乎有钓鱼的经验啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "#11P想隐藏也没用，我都看得出来。\x01",
            "……如何，要加入我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#5P#0005F咦……？\x01",
            "确、确实，我在小时候\x01",
            "曾经钓过一段时间的鱼……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0214
    ChrTalk(
        0x101,
        (
            "#5P#0011F不过……那个……\x01",
            "我现在还在执行公务，所以不好意思了！\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        (
            "#12P#0109F（啊哈哈……似乎\x01",
            "  被猜中了啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x103,
        "#6P#0203F（总觉得这些大叔都很奇怪呢。）\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#5P#0006F（呼，真是有点不知所措……）\x02\x03",

            "#0000F那个……总之\x01",
            "这里并不是空房吧？\x02\x03",

            "但根据市政府的记录，\x01",
            "这里应该是空着的……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0218
    ChrTalk(
        0xA,
        (
            "#11P不不，\x01",
            "那不可能。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xA,
        (
            "#11P如你们所见，我们的\x01",
            "活动正进展得如火如荼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        "#11P唔，说到空房……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0221
    ChrTalk(
        0x8,
        (
            "#11P这条街最西边的建筑\x01",
            "是一栋名为洋槐庄园的公寓。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "#11P那里好像有一间房间是空房哦。\x01",
            "你们说的应该是那里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x8,
        (
            "#11P洋槐庄园在我们隔壁两栋处，\x01",
            "在游击士协会的左边。\x02",
        )
    )

    CloseMessageWindow()
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

    def lambda_3E10():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E10)

    def lambda_3E1D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E1D)

    def lambda_3E2A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3E2A)

    def lambda_3E37():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3E37)
    Sleep(500)

    #C0224
    ChrTalk(
        0x104,
        (
            "#0303F#12P与实际地址相差两栋建筑……\x01",
            "也就是说，市政府的资料出错了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯……\x01",
            "有可能。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        (
            "#12P#0100F总之，市政府的记录\x01",
            "好像不太准确……\x01",
            "我们还是去实际确认一下为好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetChrPos(0x0, 4780, 0, 5260, 225)
    SetChrPos(0x1, 4780, 0, 5260, 225)
    SetChrPos(0x2, 4780, 0, 5260, 225)
    SetChrPos(0x3, 4780, 0, 5260, 225)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    OP_29(0x3, 0x1, 0x4)
    SetScenarioFlags(0x0, 3)
    EventEnd(0x5)
    Return()

    # Function_9_375E end

    def Function_10_3F6E(): pass

    label("Function_10_3F6E")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(6970, 1400, 7010, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19720, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FEF")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0xEF, 7400, 0, 6250, 0)
    SetChrPos(0x153, 6200, 0, 5050, 0)
    Jump("loc_4117")

    label("loc_3FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4061")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)
    SetChrPos(0x109, 6200, 0, 3850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_4117")

    label("loc_4061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40D3")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)
    SetChrPos(0x10A, 6200, 0, 3850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_4117")

    label("loc_40D3")

    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)

    label("loc_4117")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    Return()

    # Function_10_3F6E end

    def Function_11_413B(): pass

    label("Function_11_413B")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4159")
    Jump("loc_4193")

    label("loc_4159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4176")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_4193")

    label("loc_4176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4193")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_4193")

    label("loc_4193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41A6")
    Jump("loc_41D6")

    label("loc_41A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41B9")
    Jump("loc_41D6")

    label("loc_41B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41CC")
    Jump("loc_41D6")

    label("loc_41CC")

    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_41D6")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 5410, 0, 6840, 45)
    TurnDirection(0x8, 0x0, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Return()

    # Function_11_413B end

    def Function_12_41F8(): pass

    label("Function_12_41F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4497")

    #C0227
    ChrTalk(
        0x8,
        (
            "钓公师团为了普及钓鱼文化，提高钓鱼技术\x01",
            "而设立了『等级认定考试』。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x8,
        (
            "在对你的钓鱼技术进行鉴定后，\x01",
            "我们还会授予各种荣誉称号及奖品哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "嗯，因为罗伊德团员才刚刚入团，\x01",
            "所以现在的等级是『新手钓师』。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43B5")

    #C0230
    ChrTalk(
        0x8,
        (
            "提升至下一个等级的条件是\x01",
            "钓得『４种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x8,
        (
            "打开钓鱼手册，就可以查看\x01",
            "已经钓到过的鱼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x8,
        "如果钓到４种以上的话，一定要来报告啊。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x8,
        (
            "哇哈哈，钓鱼很快乐吧？\x01",
            "多下些工夫，继续挑战吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_448F")

    label("loc_43B5")


    #C0234
    ChrTalk(
        0x8,
        (
            "提升至下一个等级的条件是\x01",
            "钓到『４种以上的鱼』……\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x8,
        (
            "……嗯，怎么了。\x01",
            "已经钓到过４种以上的鱼了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "嗯，反正我会仔细检查\x01",
            "你的钓鱼手册的。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "要检查的话，就再来找我吧。\x01",
            "哇哈哈，要进行升至下个等级的鉴定吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_448F")

    SetScenarioFlags(0x69, 6)
    Jump("loc_627D")

    label("loc_4497")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4888")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4777")
    Call(0, 10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0238
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

    #C0239
    ChrTalk(
        0x8,
        (
            "噢……罗伊德团员，\x01",
            "你的钓鱼成果挺不错呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
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

    #A0241
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

    #A0242
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "作为褒奖，",
            scpstr(SCPSTR_CODE_ITEM, '草帽'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('草帽', 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0243
    ChrTalk(
        0x8,
        (
            "这是我以前\x01",
            "爱用的草帽，\x01",
            "钓鱼的时候就戴着它吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x8,
        (
            "罗伊德团员，把这个带在身上，\x01",
            "今后也继续努力钓鱼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#0002F这是钓鱼的必备道具啊，\x01",
            "那我就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x8,
        (
            "嗯，『业余钓师』的话，级别只能算是\x01",
            "马马虎虎，如果继续提高等级，\x01",
            "还能得到更多豪华的奖品哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x8,
        (
            "呵呵……顺便把下一个等级的\x01",
            "鉴定条件告诉你好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x8,
        (
            "如果想提升至下一个等级，\x01",
            "就必须钓到『８种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x8,
        "多下些工夫，努力去挑战吧。\x02",
    )

    CloseMessageWindow()
    Call(0, 11)
    Jump("loc_4883")

    label("loc_4777")


    #C0250
    ChrTalk(
        0x8,
        (
            "罗伊德团员现在的等级是\x01",
            "『新手钓师』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "如果想提升至下一个等级，\x01",
            "就要钓到『４种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x8,
        (
            "如果想知道自己目前已经钓到过哪几种鱼，\x01",
            "只要查看钓鱼手册，就全都一目了然啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "呵呵……等垂钓有了更大成果之后，再将手册拿来给我看吧。\x01",
            "到时我会给你鉴定等级的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4883")

    Jump("loc_627D")

    label("loc_4888")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DCD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4D0F")
    Call(0, 10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0254
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

    #C0255
    ChrTalk(
        0x8,
        (
            "噢……罗伊德团员\x01",
            "你的钓鱼成果相当不错呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
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

    #A0257
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

    #A0258
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "作为褒奖，",
            scpstr(SCPSTR_CODE_ITEM, '混乱之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('混乱之刃', 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0259
    ChrTalk(
        0x8,
        (
            "你又让我回忆起了自己\x01",
            "刚成为『专业钓师』的那一天……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "原本就喜好钓鱼的我，出于工作原因\x01",
            "去了利贝尔王国，在那里遇到了一名\x01",
            "自称是『钓公师团』成员的男子。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "哇哈哈，不用我说，恐怕你也猜到了，\x01",
            "他就是传说中的钓师费瑟尔团长！\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        (
            "经过一番曲折之后，团长亲自将\x01",
            "『专业钓师』的等级授予我了。\x01",
            "真是怀念啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
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

    #C0264
    ChrTalk(
        0x8,
        (
            "哇哈哈，不不不，\x01",
            "只是帮我家老头子做些事。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        (
            "虽然还算是精明能干，但现在\x01",
            "因为分部长的工作而忙得不可开交啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        (
            "#0012F啊，原来如此……\x01",
            "（果然是个把兴趣摆在第一位的人呀……）\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x8,
        (
            "哦……忘了一件事。\x01",
            "把下一个等级的鉴定条件\x01",
            "告诉你吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x8,
        (
            "罗伊德团员，如果想提升至下一个等级，\x01",
            "就必须钓到『１２种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x8,
        (
            "这可需要花费相当多的工夫啊，\x01",
            "好好努力吧！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 11)
    Jump("loc_4DC8")

    label("loc_4D0F")


    #C0270
    ChrTalk(
        0x8,
        (
            "罗伊德团员的等级是\x01",
            "『业余钓师』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "如果想提升至下一个等级，\x01",
            "就必须钓到『８种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x8,
        (
            "呵呵……等垂钓有了更大成果之后，再将手册拿来给我看吧。\x01",
            "到时我会给你鉴定等级的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DC8")

    Jump("loc_627D")

    label("loc_4DCD")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5283")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_51C3")
    Call(0, 10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0273
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

    #C0274
    ChrTalk(
        0x8,
        (
            "噢……罗伊德团员，\x01",
            "你的钓鱼成果真是相当了得呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
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

    #A0276
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

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '月之宝珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(17, 0, 100, 0)

    #A0278
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "作为褒奖，",
            scpstr(SCPSTR_CODE_ITEM, '破脚之牙'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('月之宝珠', 1)
    AddItemNumber('破脚之牙', 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0279
    ChrTalk(
        0x8,
        (
            "你还真有一套啊，罗伊德团员。\x01",
            "我以前取得『二级钓师』这个等级时\x01",
            "也是下了相当大的苦功。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x8,
        (
            "哇哈哈，想当年，我还\x01",
            "钻到深山老林中去修行……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        (
            "在大自然中不断磨练自己的感觉，\x01",
            "最后终于钓到了稀有的珍珠草，\x01",
            "才成为了『二级钓师』！\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "……罗伊德团员也很辛苦吧，但你付出\x01",
            "的这份汗水，正是钓师的勋章啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x8,
        (
            "罗伊德团员，今后也继续努力吧，\x01",
            "我期待着你的活跃表现！\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        (
            "#0009F哈哈，谢谢您。\x02\x03",

            "#0000F话说回来……既然是『二级』，\x01",
            "那肯定也有『一级』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "这个自然，\x01",
            "接下来的等级就是『一级钓师』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "如果想晋升为『一级钓师』，\x01",
            "就要钓到『１６种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x8,
        (
            "罗伊德团员终于也步入\x01",
            "高等级成员的队伍了啊。\x01",
            "哇哈哈，我也很期待你今后的表现！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 11)
    Jump("loc_527E")

    label("loc_51C3")


    #C0288
    ChrTalk(
        0x8,
        (
            "罗伊德团员的等级是\x01",
            "『专业钓师』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x8,
        (
            "如果想提升至下一个等级，\x01",
            "就必须钓到『１２种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "呵呵……等垂钓有了更大成果之后，再将手册拿来给我看吧。\x01",
            "到时我会给你鉴定等级的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_527E")

    Jump("loc_627D")

    label("loc_5283")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_588A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_576D")
    Call(0, 10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0291
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

    #C0292
    ChrTalk(
        0x8,
        (
            "噢……看来你的钓鱼成果\x01",
            "还真的再度提高了呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
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

    #A0294
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

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '星之光玉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('星之光玉', 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0296
    ChrTalk(
        0x8,
        (
            "罗伊德团员终于也成为『一级钓师』了吗，\x01",
            "速度还真是快啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x8,
        (
            "我大概在五六年前取得了这个等级，\x01",
            "这也是我决心在克洛斯贝尔\x01",
            "设立分部的契机。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
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

    #C0299
    ChrTalk(
        0x8,
        (
            "……好啦。\x01",
            "罗伊德团员，接下来\x01",
            "告诉你一件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x8,
        (
            "成为一级钓师的人，\x01",
            "就可以在本分部购买\x01",
            "『熬炼丸子ＤＸ』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x8,
        (
            "这是我们研制出来的\x01",
            "万能鱼饵哦，\x01",
            "各种鱼类都会来吃的。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
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

    #C0303
    ChrTalk(
        0x8,
        "哇哈哈，不愧是罗伊德团员啊。\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x8,
        (
            "如你所说，即使是在常去的钓鱼点，\x01",
            "一旦更换了鱼饵，也相当于进入了全新的垂钓世界。\x01",
            "多去尝试一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x8,
        (
            "接下来……就把下一个等级\x01",
            "的鉴定条件告诉你吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x8,
        (
            "接下来的等级可就是『特级钓师』了。\x01",
            "如果想成为『特级钓师』，\x01",
            "就必须钓到『２３种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x8,
        (
            "这个条件实在是相当艰难呢……\x01",
            "但还是要努力去挑战呀，罗伊德团员！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 11)
    Jump("loc_5885")

    label("loc_576D")


    #C0308
    ChrTalk(
        0x8,
        (
            "罗伊德团员的等级是『二级钓师』啊。\x01",
            "虽然这个等级已经很厉害了……\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "但如果想提升至下一个等级，\x01",
            "就必须钓到『１６种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x8,
        (
            "尝试各种鱼饵，寻找各种钓鱼点，\x01",
            "确实是很耗费精力的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x8,
        (
            "呵呵……等垂钓有了更大成果之后，再将手册拿来给我看吧。\x01",
            "到时我会给你鉴定等级的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5885")

    Jump("loc_627D")

    label("loc_588A")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DD3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5C88")
    Call(0, 10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0312
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

    #C0313
    ChrTalk(
        0x8,
        (
            "噢……！？\x01",
            "连那梦幻之鱼『锦鲤』和『金鲑』\x01",
            "也都被你钓到了吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0314
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

    #A0315
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

    #A0316
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '苦西红柿酱'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0317
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '幸运刻印'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('苦西红柿酱', 1)
    AddItemNumber('幸运刻印', 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0318
    ChrTalk(
        0x8,
        (
            "罗伊德团员终于升到了\x01",
            "和我同样的等级了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x8,
        (
            "从今以后，无论是对于金鲑那绝妙的尾鳍角度，\x01",
            "还是钓到锦鲤时的那种独特手感……\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x8,
        (
            "我们都可以畅所欲言\x01",
            "地进行交流啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x8,
        (
            "哇哈哈，所谓的特级钓师，就是要对\x01",
            "有关垂钓的一切事情都知无不尽。\x01",
            "可以尽情讨论的朋友又多了一个，我真是很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        (
            "……罗伊德团员，我已经没有什么东西可以教你了。\x01",
            "从今以后，就请你尽情贯彻自己的钓鱼之道吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#0009F哈哈哈……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x8,
        (
            "不过……在克洛斯贝尔的某处，\x01",
            "还栖息着传说中的鱼王，\x01",
            "它可是个超级庞然大物。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x8,
        (
            "这次送给你的钓竿『水中魔法师』\x01",
            "就蕴藏着将其钓到的可能性……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        (
            "罗伊德团员，如果你有此意向的话，\x01",
            "就去挑战传说中的鱼王吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 0)
    Call(0, 11)
    Jump("loc_5DCE")

    label("loc_5C88")


    #C0327
    ChrTalk(
        0x8,
        (
            "罗伊德团员的等级是『一级钓师』啊。\x01",
            "在如此短的时间内就能取得如此成绩，真是很了不起。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x8,
        (
            "但是，在此之上，还有更高的等级\x01",
            "『特级钓师』在等着你。\x01",
            "授予条件是钓到『２３种以上的鱼』。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        (
            "确实是相当困难啊……\x01",
            "必须要把『锦鲤』\x01",
            "和『金鲑』也给钓到才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        (
            "……罗伊德团员，等你取得更大的垂钓成果后，\x01",
            "就来这里将手册拿给我看吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DCE")

    Jump("loc_627D")

    label("loc_5DD3")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_627D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6183")
    Call(0, 10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0331
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

    #C0332
    ChrTalk(
        0x8,
        (
            "什么……！？\x01",
            "罗伊德团员，你竟然钓到了\x01",
            "传说中的『霸王蛇鱼』吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x8,
        (
            "难以置信……\x01",
            "终于成功了啊，\x01",
            "哇哈哈哈……！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
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

    #C0335
    ChrTalk(
        0x8,
        (
            "这家伙可是咱们克洛斯贝尔\x01",
            "分部的全体成员常年追寻的\x01",
            "最大对手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x8,
        "你竟然能把它给钓到……\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x8,
        (
            "好！现在就授予你\x01",
            "特别的称号吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
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

    #A0339
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

    #A0340
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

    #C0341
    ChrTalk(
        0x8,
        (
            "居然能超越我，\x01",
            "成为钓圣……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x8,
        (
            "今后也请多多关照了，\x01",
            "『克洛斯贝尔的钓圣』！\x02",
        )
    )

    CloseMessageWindow()

    #C0343
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

    #C0344
    ChrTalk(
        0x8,
        (
            "喔，罗伊德团员还真是\x01",
            "谦虚啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x8,
        (
            "哇哈哈，真是名不虚传呀！\x01",
            "哇哈哈哈哈……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 0)
    Call(0, 11)
    Jump("loc_627D")

    label("loc_6183")


    #C0346
    ChrTalk(
        0x8,
        "罗伊德团员的等级是『特级钓师』啊。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "在钓公师团的克洛斯贝尔分部，\x01",
            "已经没有等级比你更高的成员了。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x8,
        (
            "不过，如果是罗伊德团员的话，\x01",
            "说不定还能钓到更大的家伙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x8,
        (
            "哇哈哈，如果以后真的钓到了，\x01",
            "可一定要拿来给我看看呀。\x01",
            "我可是很想拜见一下的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_627D")

    Return()

    # Function_12_41F8 end

    def Function_13_627E(): pass

    label("Function_13_627E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62A3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_62A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62BE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_62BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62D9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_62D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62F4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_62F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_630F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_630F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_632A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_632A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6345")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6345")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6360")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6360")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_637B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_637B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6396")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6396")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63B1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_63B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63CC")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_63CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63E7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_63E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6402")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6402")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_641D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_641D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6438")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6438")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6453")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6453")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_646E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_646E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6489")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6489")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64A4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_64A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64BF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_64BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64DA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_64DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64F5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_64F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6510")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6510")

    Return()

    # Function_13_627E end

    def Function_14_6511(): pass

    label("Function_14_6511")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0350
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放着书籍《简单的鱼类料理》。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_END)), "loc_65C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65C7")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0351
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '炸鱼排'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法写在书里。\x02",
        )
    )

    CloseMessageWindow()

    #A0352
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '炸鱼排'),
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

    label("loc_65C7")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_14_6511 end

    SaveToFile()

Try(main)
