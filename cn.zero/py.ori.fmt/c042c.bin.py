from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c042c.bin",                # FileName
        "c042c",                    # MapName
        "c042c",                    # Location
        0x0023,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 2, 0, 3],
    )

    BuildStringList((
        "c042c",                  # 0
        "亚邦剧团长",             # 1
        "伊莉娅",                 # 2
        "莉夏",                   # 3
        "尼克鲁",                 # 4
        "海因兹",                 # 5
        "修利",                   # 6
    ))

    AddCharChip((
        "chr/ch05100.itc",                   # 00
        "chr/ch05200.itc",                   # 01
        "chr/ch27500.itc",                   # 02
        "chr/ch24200.itc",                   # 03
        "chr/ch36800.itc",                   # 04
        "chr/ch10100.itc",                   # 05
    ))

    DeclNpc(-1480,   0,       15689,   45,   261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-209,    0,       15550,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1330,    0,       15699,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-68150,  0,       2150,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-66489,  0,       7329,    0,    261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(64569,   0,       4590,    315,  389,  0x0, 0,   5,   0,   0,   1,   0,   9,   255,  0)

    ScpFunction((
        "Function_0_18C",          # 00, 0
        "Function_1_244",          # 01, 1
        "Function_2_26F",          # 02, 2
        "Function_3_330",          # 03, 3
        "Function_4_331",          # 04, 4
        "Function_5_779",          # 05, 5
        "Function_6_97D",          # 06, 6
        "Function_7_A52",          # 07, 7
        "Function_8_B21",          # 08, 8
        "Function_9_C19",          # 09, 9
        "Function_10_E4F",         # 0A, 10
        "Function_11_F45",         # 0B, 11
        "Function_12_278E",        # 0C, 12
        "Function_13_2DCD",        # 0D, 13
    ))


    def Function_0_18C(): pass

    label("Function_0_18C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1CC"),
        (1, "loc_1D8"),
        (2, "loc_1E4"),
        (3, "loc_1F0"),
        (4, "loc_1FC"),
        (5, "loc_208"),
        (6, "loc_214"),
        (SWITCH_DEFAULT, "loc_220"),
    )


    label("loc_1CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_1D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_1E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_1F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_1FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_208")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_214")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_220")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_22C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_243")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_243")

    Return()

    # Function_0_18C end

    def Function_1_244(): pass

    label("Function_1_244")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26E")
    OP_94(0xFE, 0xF4D8, 0x532, 0x1054A, 0x15AE, 0x3E8)
    Sleep(300)
    Jump("Function_1_244")

    label("loc_26E")

    Return()

    # Function_1_244 end

    def Function_2_26F(): pass

    label("Function_2_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2B3")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, -66690, 0, 4990, 0)
    SetChrPos(0xC, -66690, 0, 6530, 180)
    Jump("loc_32F")

    label("loc_2B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D3")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_32F")

    label("loc_2D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_30E")
    SetChrPos(0x8, -1880, 10, 15240, 135)
    SetChrPos(0xA, -210, 0, 13820, 0)
    OP_93(0x9, 0xB4, 0x0)
    Jump("loc_32F")

    label("loc_30E")

    BeginChrThread(0x9, 2, 0, 13)
    BeginChrThread(0xA, 2, 0, 13)
    BeginChrThread(0x8, 2, 0, 13)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_32F")

    Return()

    # Function_2_26F end

    def Function_3_330(): pass

    label("Function_3_330")

    Return()

    # Function_3_330 end

    def Function_4_331(): pass

    label("Function_4_331")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35A")
    Call(0, 11)
    Return()

    label("loc_35A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_43F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3BB")

    #C0001
    ChrTalk(
        0x8,
        (
            "今天这么多人，\x01",
            "出现走失的孩子也难怪吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "希望能早点找到他啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43A")

    label("loc_3BB")


    #C0003
    ChrTalk(
        0x8,
        (
            "哦，是罗伊德啊，\x01",
            "听说有小男孩走丢了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "唔，纪念庆典时的人这么多，\x01",
            "而且今天又有游行……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "真希望能早点找到啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_43A")

    Jump("loc_775")

    label("loc_43F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_450")
    Jump("loc_775")

    label("loc_450")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_6B7")

    #C0006
    ChrTalk(
        0x8,
        (
            "从明天开始，\x01",
            "伊莉娅的公演又要开始了……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "在如此重要的时期，\x01",
            "竟然会出现跟踪狂，\x01",
            "真是令人坐立不安啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "希望各位能尽快\x01",
            "帮忙将他逮捕归案啊！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_607")
    TalkEnd(0xFE)
    EventBegin(0x0)
    StopBGM(0x5DC)
    Fade(500)
    OP_68(-250, 1670, 13660, 0)
    MoveCamera(32, 29, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14970, 0)
    SetChrPos(0x101, 260, 120, 13350, 346)
    SetChrPos(0x102, -850, 450, 12100, 346)
    SetChrPos(0x103, -840, 0, 13680, 346)
    SetChrPos(0x104, 300, 450, 12100, 346)
    SetChrPos(0x8, -1480, 0, 15690, 180)
    SetChrPos(0xA, 1330, 0, 15700, 225)
    OP_93(0x9, 0xB4, 0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    OP_0D()
    OP_29(0x1D, 0x1, 0x1)
    Call(0, 12)
    Return()

    label("loc_607")


    #C0009
    ChrTalk(
        0x101,
        (
            "#0006F实在抱歉……我们\x01",
            "还有其它工作没有完成。\x01",
            "现在脱不开身呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "是吗……\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "如果有空了，就请来帮帮忙吧。\x01",
            "我们无论如何，也希望\x01",
            "能尽快解决这件事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_775")

    label("loc_6B7")


    #C0012
    ChrTalk(
        0xFE,
        (
            "唔，似乎有\x01",
            "尝试的价值呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "不过，莉夏也真是了不起啊。\x01",
            "竟然能够接受\x01",
            "伊莉娅那么胡来的要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "#1700F啊哈哈，因为她是莉夏嘛。\x02\x03",

            "#1709F毕竟是被我看中的人，我的眼光\x01",
            "是绝对不会错的～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_775")

    TalkEnd(0xFE)
    Return()

    # Function_4_331 end

    def Function_5_779(): pass

    label("Function_5_779")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A2")
    Call(0, 11)
    Return()

    label("loc_7A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_8B2")

    #C0015
    ChrTalk(
        0x9,
        (
            "#1704F好，趁现在\x01",
            "继续排练吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0xA, 0x9, 500)
    TurnDirection(0x8, 0x9, 500)

    #C0016
    ChrTalk(
        0xA,
        (
            "#1801F不，请等一下，\x01",
            "伊莉娅小姐！！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "是呀，现在还不行！\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    #C0018
    ChrTalk(
        0x9,
        (
            "#1706F嘁～有什么关系嘛。\x01",
            "反正也闲着～\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#0006F（看来，要接受任务的话，\x01",
            "  还是越早越好啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x1F4)
    OP_93(0x8, 0x87, 0x1F4)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    Jump("loc_979")

    label("loc_8B2")


    #C0020
    ChrTalk(
        0x9,
        (
            "#1700F关于下一个登场的时机，\x01",
            "还要再调整一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "#1800F是啊，那样的话，\x01",
            "我也更容易配合……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0000F（好像在商量排练的事呢。）\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#0100F（今天好像是休演日，\x01",
            "不过三个人的热情都很高呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_979")

    TalkEnd(0xFE)
    Return()

    # Function_5_779 end

    def Function_6_97D(): pass

    label("Function_6_97D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A6")
    Call(0, 11)
    Return()

    label("loc_9A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_A4B")

    #C0024
    ChrTalk(
        0xA,
        (
            "#1803F不好意思，伊莉娅小姐\x01",
            "对这种事很不重视。\x02\x03",

            "#1808F我也无法在\x01",
            "白天应对……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0025
    ChrTalk(
        0xA,
        (
            "#1801F那、那个，总之就\x01",
            "拜托各位了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4E")

    label("loc_A4B")

    Call(0, 5)

    label("loc_A4E")

    TalkEnd(0xFE)
    Return()

    # Function_6_97D end

    def Function_7_A52(): pass

    label("Function_7_A52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_AC3")

    #C0026
    ChrTalk(
        0xB,
        (
            "抱歉哦，演出的时候，\x01",
            "我也没有注意观众席。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        (
            "去问问伊莉娅小姐或普莉埃小姐\x01",
            "也许比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1D")

    label("loc_AC3")


    #C0028
    ChrTalk(
        0xB,
        "……哎，小男孩？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xB,
        (
            "这个……演出的时候精神会高度集中，\x01",
            "完全不会去注意观众啦……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_B1D")

    TalkEnd(0xFE)
    Return()

    # Function_7_A52 end

    def Function_8_B21(): pass

    label("Function_8_B21")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_BB7")

    #C0030
    ChrTalk(
        0xC,
        (
            "小孩子的话……应该没有\x01",
            "来过这附近哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xC,
        (
            "舞台装置的操作\x01",
            "非常精细，需要全神贯注。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xC,
        (
            "当然了，演出的时候，\x01",
            "我也会注意周围的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C15")

    label("loc_BB7")


    #C0033
    ChrTalk(
        0xC,
        (
            "今天是休演日，\x01",
            "所以正在进行舞台装置的统一检查。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xC,
        (
            "除了这种时候之外，\x01",
            "都没机会检查嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C15")

    TalkEnd(0xFE)
    Return()

    # Function_8_B21 end

    def Function_9_C19(): pass

    label("Function_9_C19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_DDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC6")

    #C0035
    ChrTalk(
        0xFE,
        "啊，你是……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#0000F哟，最近还好吗？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "关、关、关你什么事，\x01",
            "走开啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "我现在很忙的！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#0000F哈哈，还真是别扭啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D7C")

    label("loc_CC6")


    #C0040
    ChrTalk(
        0xFE,
        "啊，你是……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        "#0300F哟，还好吗？\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "关、关、关你什么事，\x01",
            "走开啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        "我现在很忙的！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0000F哈哈，还真别扭啊。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#0204F罗伊德前辈\x01",
            "被人讨厌了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#0006F呜……\x02",
    )

    CloseMessageWindow()

    label("loc_D7C")

    SetScenarioFlags(0x0, 2)
    Jump("loc_DDA")

    label("loc_D84")


    #C0047
    ChrTalk(
        0xFE,
        (
            "我还在学习工作的要领，\x01",
            "不懂的事情还有很多……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "接下来的路还很长，\x01",
            "别碍事哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDA")

    Jump("loc_E4B")

    label("loc_DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF1")
    Call(0, 10)
    Jump("loc_E4B")

    label("loc_DF1")


    #C0049
    ChrTalk(
        0xFE,
        (
            "……接下来要进行调整，\x01",
            "然后又是夜场的演出了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "我很忙的，\x01",
            "不要厚着脸皮跑进来啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4B")

    TalkEnd(0xFE)
    Return()

    # Function_9_C19 end

    def Function_10_E4F(): pass

    label("Function_10_E4F")


    #C0051
    ChrTalk(
        0x101,
        (
            "#0005F咦……？\x01",
            "剧团里还有这样的孩子吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EBE")

    #C0052
    ChrTalk(
        0xFE,
        (
            "……你是干什么的，\x01",
            "难道认识伊莉娅小姐吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EEF")

    label("loc_EBE")


    #C0053
    ChrTalk(
        0xFE,
        (
            "……你们是干什么的，\x01",
            "难道认识伊莉娅小姐吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEF")


    #C0054
    ChrTalk(
        0xFE,
        (
            "哼……\x01",
            "无关人员禁止进入剧团。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "就算认识伊莉娅小姐，\x01",
            "也别厚着脸皮进来啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 0)
    Return()

    # Function_10_E4F end

    def Function_11_F45(): pass

    label("Function_11_F45")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-250, 1670, 13660, 0)
    MoveCamera(32, 29, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14970, 0)
    SetChrPos(0x101, 260, 120, 13350, 346)
    SetChrPos(0x102, -850, 450, 12100, 346)
    SetChrPos(0x103, -840, 0, 13680, 346)
    SetChrPos(0x104, 300, 450, 12100, 346)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0x8, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_1024():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1024)
    Sleep(10)

    def lambda_1034():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1034)
    Sleep(12)

    def lambda_1044():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1044)
    Sleep(300)

    #C0056
    ChrTalk(
        0x9,
        (
            "#5P#1705F哎呀，这不是警察弟弟嘛。\x01",
            "久违～\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xA,
        (
            "#11P#1809F各位，好久不见了。\x01",
            "……抱歉，我们自顾自地\x01",
            "谈了起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        "#5P哈哈，抱歉。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#5P一说到排练，\x01",
            "就忍不住入迷了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#12P#0102F各位，好久不见了。\x01",
            "新剧目似乎大受好评呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "#5P#1704F呵呵，\x01",
            "那是当然了。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        (
            "#11P#1802F罗伊德警官第一天\x01",
            "也来看了吧。\x02\x03",

            "#1809F呵呵，多谢捧场了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#12P#0012F哪里……\x01",
            "我只是塞茜尔姐姐的跟班而已啦。\x02\x03",

            "#0002F不过，演出真是棒极了！\x02\x03",

            "伊莉娅小姐自不必说，\x01",
            "莉夏也开始让我崇拜了呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        "#11P#1810F哪、哪里……真不好意思。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(200)

    #C0065
    ChrTalk(
        0x9,
        "#5P#1705F哎呀呀，真亲昵呢。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(200)

    #C0066
    ChrTalk(
        0x9,
        (
            "#5P#1709F要不要把警察弟弟搭讪的事\x01",
            "向塞茜尔打个小报告呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#12P#0011F什么……\x01",
            "这才不是搭讪啦！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    #C0068
    ChrTalk(
        0xA,
        "#11P#1801F讨、讨厌啦，伊莉娅小姐真是的。\x02",
    )

    CloseMessageWindow()

    def lambda_1320():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1320)

    def lambda_132D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_132D)

    def lambda_133A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_133A)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)
    OP_64(0x103)
    OP_64(0x102)

    #C0069
    ChrTalk(
        0x103,
        (
            "#6P#0211F真羡慕罗伊德前辈啊。\x02\x03",

            "我们收到的票\x01",
            "都是下周的，\x01",
            "暂时还看不到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#12P#0310F而且还是跟塞茜尔小姐\x01",
            "来彩虹剧团约会！？\x02\x03",

            "昏暗的剧场、精彩的舞台……\x01",
            "两人一起享受这气氛，\x01",
            "真是太令人眼红啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        (
            "#12P#0104F……好啦好啦，你们两个。\x02\x03",

            "#0111F虽然继塞茜尔小姐之后\x01",
            "又是莉夏小姐，\x01",
            "确实是有点没节操……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)

    #C0072
    ChrTalk(
        0x101,
        (
            "#11P#0012F那个，你们在说什么啊！？\x02\x03",

            "#0001F虽说我一个人抢先看了表演，\x01",
            "好像是有点对不起大家……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#12P#0111F（瞪～）……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x103,
        "#6P#0211F（盯～）……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x104,
        "#12P#0301F……你这个长着娃娃脸的男性公敌！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#11P#0006F（呜呜，别这样啊……）\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "#5P#1702F啊哈哈，警察弟弟也真是不容易呢。\x02\x03",

            "#1709F要是我也插一脚的话，\x01",
            "岂不是更加有趣了吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)

    #C0078
    ChrTalk(
        0x101,
        "#12P#0006F请不要玩弄别人的人生啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x1F4)
    Sleep(200)

    #C0079
    ChrTalk(
        0xA,
        "#11P#1809F啊、啊哈哈哈……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "#5P好了好了，\x01",
            "玩笑就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "#5P伊莉娅，不要老是\x01",
            "捉弄年轻人啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "#5P#1704F是是，知道啦。\x02\x03",

            "#1700F好吧……那么，\x01",
            "今天是来找我们的吗？\x02\x03",

            "#1709F刚好是休演日，\x01",
            "要不要一起去喝个茶？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1762():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1762)

    def lambda_176F():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_176F)

    def lambda_177C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_177C)

    def lambda_1789():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1789)
    Sleep(300)

    #C0083
    ChrTalk(
        0x101,
        (
            "#12P#0005F啊，不……\x01",
            "其实是为了工作而来的。\x02\x03",

            "#0001F就是那个支援请求。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1200)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(10)

    def lambda_1854():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x258, 0x2EE0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1854)

    def lambda_1871():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x258, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1871)
    Sleep(800)

    #C0084
    ChrTalk(
        0x8,
        (
            "#5P对、对了……\x01",
            "都忘得一干二净了！！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "#11P#1805F对、对不起。\x01",
            "我们三个一开始就是在\x01",
            "讨论这件事的……\x02\x03",

            "#1806F结、结果不知不觉\x01",
            "就变成了排练方面的讨论……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0x9, 0x5A, 0x1F4)

    #C0086
    ChrTalk(
        0x9,
        "#5P#1705F哎？哎？什么事啊？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_1986():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1986)

    def lambda_1993():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1993)
    Sleep(300)

    #C0087
    ChrTalk(
        0x8,
        (
            "#5P伊莉娅～\x01",
            "拜托你清醒一点！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        (
            "#11P#1801F你忘了吗，就是昨晚说过的\x01",
            "那个跟踪狂的事啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "#5P#1705F啊……那件事吗，\x01",
            "你还是告诉他们了啊？\x02\x03",

            "#1706F其实对我也没有实际损害，\x01",
            "别去管它不就好了嘛～\x02",
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

    #C0090
    ChrTalk(
        0x104,
        (
            "#12P#0305F不、不愧是伊莉娅小姐啊，\x01",
            "这次明明都被\x01",
            "跟踪狂盯上了……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        (
            "#12P#0106F竟然完全不介意呢……\x01",
            "（同为女性，有点\x01",
            "  难以置信……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B58():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1B58)

    def lambda_1B65():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1B65)

    def lambda_1B72():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B72)
    Sleep(300)

    #C0092
    ChrTalk(
        0x8,
        (
            "#5P不、不好意思。\x01",
            "虽说是跟踪狂，\x01",
            "其实只是个小跟踪狂……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "#11P#1806F嗯，我们也是\x01",
            "昨晚才刚听伊莉娅小姐说的……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#12P#0003F（他们两个的状态好像都有点混乱。）\x02\x03",

            "#0001F嗯……总之，请两位\x01",
            "都先镇静一下。\x02\x03",

            "首先，能告诉我们\x01",
            "跟踪狂作案的情况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "#11P#1805F好、好的。\x01",
            "由我来说明吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 400)
    Sleep(200)

    #C0096
    ChrTalk(
        0xA,
        "#11P#1801F可以吧，伊莉娅小姐！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 400)
    Sleep(200)

    #C0097
    ChrTalk(
        0x9,
        (
            "#5P#1703F嗯，没办法～\x01",
            "好吧，莉夏，你就告诉他们吧。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x9C4)

    #C0098
    ChrTalk(
        0xA,
        "#11P#1801F是！\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x190)
    OP_93(0x9, 0xB4, 0x190)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    #C0099
    ChrTalk(
        0xA,
        (
            "#11P#1801F据伊莉娅小姐所说，\x01",
            "事情似乎就是在这一两周发生的。\x02\x03",

            "#1803F伊莉娅小姐的家里\x01",
            "好像出现了可疑的人物──\x01",
            "也就是跟踪狂。\x02\x03",

            "#1801F那人在公寓周围转来转去，\x01",
            "这几天甚至在公寓里\x01",
            "也被目击到了！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#12P#0001F跟到公寓去了吗……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "#5P#1700F只是，我和莉夏\x01",
            "都没见过他的样子呢。\x02\x03",

            "#1703F只是偶尔能感觉到视线，\x01",
            "或者说，只是有点奇怪的感觉而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        (
            "#6P#0205F连被跟踪者本人都无法发现，\x01",
            "似乎是个感觉敏锐、擅于隐藏的人物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x102,
        (
            "#12P#0101F不过……伊莉娅小姐的\x01",
            "住处是非公开的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "#5P嗯，那当然了。\x01",
            "为了防止崇拜者们追上门，\x01",
            "团员们的住处全都没有公开过。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#5P可是……到底是\x01",
            "从哪里找到的呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#12P#0301F既然有目击情报，\x01",
            "那么犯人的长相也就一清二楚了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "#11P#1803F据看见的人说，\x01",
            "好像是个十四五岁左右的\x01",
            "小个子少年……\x02\x03",

            "#1801F似乎用帽子遮住了脸，\x01",
            "所以不知道长相。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#12P#0303F唔，是年轻的\x01",
            "崇拜者吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#12P#0001F不，如果只是崇拜者，\x01",
            "明显做得有些过火了。\x02\x03",

            "而且，这种跟踪行为\x01",
            "还有可能会继续升级……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "#5P是啊，\x01",
            "我也是比较担心这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "#5P所以给各位发去了委托，\x01",
            "希望你们能尽快做出应对……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0112
    ChrTalk(
        0x9,
        (
            "#5P#1705F啊，这么一说……\x01",
            "我刚刚想起来。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(200)

    #C0113
    ChrTalk(
        0x9,
        (
            "#5P#1705F莉夏，你昨天\x01",
            "进过我的房间吗？\x02\x03",

            "#1700F我感觉东西的位置\x01",
            "好像不太一样……\x01",
            "有我家钥匙的，只有莉夏一人吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(200)
    TurnDirection(0xA, 0x9, 500)
    TurnDirection(0x8, 0x9, 500)
    Sleep(800)

    #C0114
    ChrTalk(
        0xA,
        "#11P#1805F伊莉娅小姐，这……！！\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "#5P这、这可不妙啊！\x01",
            "伊莉娅！\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        (
            "#12P#0005F难、难不成，都已经侵入到\x01",
            "伊莉娅小姐的家中了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        (
            "#12P#0101F如果这是真的，\x01",
            "案情就比想象中更加严重了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23A8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23A8)
    Sleep(10)

    def lambda_23B8():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_23B8)

    def lambda_23C5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23C5)
    Sleep(200)

    #C0118
    ChrTalk(
        0x8,
        (
            "#5P这、这可不能置之不理啊。\x01",
            "支援科的各位，\x01",
            "请尽快采取对策吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "#5P#1706F剧团长，你太夸张啦～\x01",
            "我那里又没有什么见不得人的东西。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_245C():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_245C)

    def lambda_2469():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2469)
    Sleep(300)

    #C0120
    ChrTalk(
        0xA,
        (
            "#11P#1801F问题的重点并不在这里啊！\x01",
            "伊莉娅小姐……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        "#5P是啊，伊莉娅……！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(800)
    OP_93(0x8, 0xB4, 0x190)
    OP_93(0xA, 0xE1, 0x190)
    Sleep(300)

    #C0122
    ChrTalk(
        0x8,
        (
            "#5P啊啊……不过，\x01",
            "和『银』的那次事件时一样，\x01",
            "希望各位别把事情闹大啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "#5P而且，犯人有可能只是狂热崇拜者，\x01",
            "所以就更应该低调行事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "#5P可能的话，请尽量用\x01",
            "平和的方法劝说他停止跟踪行为，\x01",
            "……如果实在不行的话，再逮捕他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        "#5P能拜托各位来处理吗？\x02",
    )

    CloseMessageWindow()
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2667")
    OP_29(0x1D, 0x1, 0x2)
    Call(0, 12)
    Jump("loc_278D")

    label("loc_2667")


    #C0126
    ChrTalk(
        0x101,
        (
            "#12P#0006F实在抱歉……我们\x01",
            "还有其它工作没有完成。\x01",
            "现在脱不开身呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "#5P是吗……\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "#5P如果有空了，就请来帮帮忙吧。\x01",
            "我们无论如何，也希望\x01",
            "能尽快解决这件事。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    SetChrPos(0x0, -400, 450, 11590, 0)
    SetChrPos(0x8, -1880, 10, 15240, 135)
    SetChrPos(0xA, -210, 0, 13820, 0)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_29(0x1D, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)

    label("loc_278D")

    Return()

    # Function_11_F45 end

    def Function_12_278E(): pass

    label("Function_12_278E")


    #C0129
    ChrTalk(
        0x101,
        (
            "#12P#0000F我明白了，\x01",
            "就交给我们吧。\x02\x03",

            "#0003F就这样置之不顾的话，\x01",
            "伊莉娅小姐或许会有危险呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "#5P哦哦，太感谢了！\x01",
            "那就拜托你们了！\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#12P#0301F反正犯人的行动范围\x01",
            "已经清楚了……\x02\x03",

            "在现场附近埋伏的话，\x01",
            "总会抓到的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "#5P#1705F啊，这样的话，\x01",
            "要不要把钥匙拿去？\x02\x03",

            "#1700F让你们随意进入我的房间，\x01",
            "应该会比较方便吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0133
    ChrTalk(
        0x101,
        "#12P#0005F可以吗……？\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "#5P#1700F完全没问题哦，\x01",
            "我刚好也有备用钥匙。\x02\x03",

            "顺带一提，\x01",
            "住址是西街的\x01",
            "『雷森别墅』。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A14")

    #C0135
    ChrTalk(
        0x101,
        (
            "#12P#0000F啊，雷森别墅……\x01",
            "就是西街最高级的\x01",
            "那座出租公寓吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "#5P#1702F对对，就在最顶层。\x02\x03",

            "给，这是钥匙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A88")

    label("loc_2A14")


    #C0137
    ChrTalk(
        0x101,
        (
            "#12P#0000F啊，是那个\x01",
            "高级出租公寓……\x02\x03",

            "记得是在顶层吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "#5P#1702F对对，你知道得真清楚呢。\x02\x03",

            "给，这是钥匙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A88")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x347),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x347, 1)

    #C0140
    ChrTalk(
        0x101,
        "#12P#0000F那我就暂时收下了。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "#11P#1803F不好意思，其实\x01",
            "我也很想帮忙的……\x02\x03",

            "#1801F可是他好像记住了我的脸，\x01",
            "所以无法接近。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B57():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B57)
    Sleep(8)

    def lambda_2B67():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B67)

    def lambda_2B74():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B74)
    Sleep(5)

    def lambda_2B84():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B84)
    Sleep(300)

    #C0142
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯，没关系，\x01",
            "我们会去调查的。\x02\x03",

            "莉夏就和伊莉娅小姐\x01",
            "在剧团耐心等待吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "#11P#1801F那么，如果顺利抓到了人，\x01",
            "就请联络我吧，\x01",
            "我和伊莉娅小姐会马上赶去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#12P#0002F哈哈，明白。\x01",
            "（只要事情一牵扯到伊莉娅小姐，\x01",
            "  莉夏就会很拼命啊。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_2C91():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C91)

    def lambda_2C9E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C9E)

    def lambda_2CAB():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2CAB)

    def lambda_2CB8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CB8)
    Sleep(400)

    #C0145
    ChrTalk(
        0x101,
        (
            "#5P#0001F那么，各位，\x01",
            "我们马上赶去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        "#12P#0101F嗯。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x103,
        "#6P#0200F好。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x104,
        (
            "#12P#0304F把那个狂热过头的崇拜者\x01",
            "好好教训一顿吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0149
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查跟踪狂！！】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_29(0x1D, 0x1, 0x1)
    SetScenarioFlags(0x5C, 1)
    NewScene("c020C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_278E end

    def Function_13_2DCD(): pass

    label("Function_13_2DCD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E27")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DFB")
    Sleep(400)
    Jump("loc_2E0D")

    label("loc_2DFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E0D")
    Sleep(750)

    label("loc_2E0D")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("Function_13_2DCD")

    label("loc_2E27")

    Return()

    # Function_13_2DCD end

    SaveToFile()

Try(main)
