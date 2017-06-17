from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1090.bin",                # FileName
        "t1090",                    # MapName
        "t1090",                    # Location
        0x0042,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1090",                  # 0
        "琪雅",                   # 1
        "缇欧",                   # 2
        "艾莉",                   # 3
    ))

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch00100.itc",                   # 02
    ))

    DeclNpc(-98199,  800,     -3890,   0,    389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-98370,  0,       -200,    180,  389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-96000,  0,       3400,    0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(-98200,  0,       -2640,   1200,    -98200,  2500,    -3890,   0x007E, 0,  4,  0x0000)

    ChipFrameInfo(312, 0)                                        # 0

    ScpFunction((
        "Function_0_138",          # 00, 0
        "Function_1_1F0",          # 01, 1
        "Function_2_2C1",          # 02, 2
        "Function_3_35F",          # 03, 3
        "Function_4_372",          # 04, 4
        "Function_5_42A",          # 05, 5
        "Function_6_506",          # 06, 6
        "Function_7_6F5",          # 07, 7
    ))


    def Function_0_138(): pass

    label("Function_0_138")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_178"),
        (1, "loc_184"),
        (2, "loc_190"),
        (3, "loc_19C"),
        (4, "loc_1A8"),
        (5, "loc_1B4"),
        (6, "loc_1C0"),
        (SWITCH_DEFAULT, "loc_1CC"),
    )


    label("loc_178")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_184")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_190")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_19C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1EF")

    Return()

    # Function_0_138 end

    def Function_1_1F0(): pass

    label("Function_1_1F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C0")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x258, 0xDAC)
    Sleep(400)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xEA6)
    Sleep(250)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xDAC)
    Sleep(400)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xEA6)
    Sleep(250)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x258, 0xDAC)
    Sleep(400)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xEA6)
    Sleep(350)
    Jump("Function_1_1F0")

    label("loc_2C0")

    Return()

    # Function_1_1F0 end

    def Function_2_2C1(): pass

    label("Function_2_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_2CF")
    Jump("loc_35E")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_2DD")
    Jump("loc_35E")

    label("loc_2DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2EB")
    Jump("loc_35E")

    label("loc_2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2F9")
    Jump("loc_35E")

    label("loc_2F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_307")
    Jump("loc_35E")

    label("loc_307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_315")
    Jump("loc_35E")

    label("loc_315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_323")
    Jump("loc_35E")

    label("loc_323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_355")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x1)
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_35E")

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_35E")

    label("loc_35E")

    Return()

    # Function_2_2C1 end

    def Function_3_35F(): pass

    label("Function_3_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_371")
    OP_65(0x0, 0x1)

    label("loc_371")

    Return()

    # Function_3_35F end

    def Function_4_372(): pass

    label("Function_4_372")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_383")
    Jump("loc_426")

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_391")
    Jump("loc_426")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_39F")
    Jump("loc_426")

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_3AD")
    Jump("loc_426")

    label("loc_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_3BB")
    Jump("loc_426")

    label("loc_3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_3C9")
    Jump("loc_426")

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_41D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E4")
    Call(0, 6)
    Jump("loc_418")

    label("loc_3E4")

    SetChrPos(0x8, -98200, 800, -3890, 0)

    #C0001
    ChrTalk(
        0x8,
        "#01109F这床好有弹性！真有趣！\x02",
    )

    CloseMessageWindow()

    label("loc_418")

    Jump("loc_426")

    label("loc_41D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_426")

    label("loc_426")

    TalkEnd(0x8)
    Return()

    # Function_4_372 end

    def Function_5_42A(): pass

    label("Function_5_42A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_43B")
    Jump("loc_502")

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_449")
    Jump("loc_502")

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_457")
    Jump("loc_502")

    label("loc_457")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_467")
    Jump("loc_502")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_475")
    Jump("loc_502")

    label("loc_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_483")
    Jump("loc_502")

    label("loc_483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_491")
    Jump("loc_502")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC")
    Call(0, 6)
    Jump("loc_4F4")

    label("loc_4AC")


    #C0002
    ChrTalk(
        0x9,
        (
            "#00202F这床真是很诱人……\x02\x03",

            "#00206F……算了，我还是先把行李放下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F4")

    Jump("loc_502")

    label("loc_4F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_502")

    label("loc_502")

    TalkEnd(0xFE)
    Return()

    # Function_5_42A end

    def Function_6_506(): pass

    label("Function_6_506")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -98200, 800, -3890, 0)

    def lambda_524():
        TurnDirection(0x0, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_524)
    Sleep(0)

    def lambda_534():
        TurnDirection(0x1, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_534)
    Sleep(0)

    def lambda_544():
        TurnDirection(0x2, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_544)
    Sleep(0)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)

    #C0003
    ChrTalk(
        0x8,
        (
            "#01109F看啊看啊！缇欧！\x01",
            "这张床好有弹性！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "#00202F这床似乎是用\x01",
            "相当优质的材料制造的。\x02\x03",

            "#00204F机会难得，不然我也……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5DD():
        TurnDirection(0x0, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_5DD)
    Sleep(50)

    def lambda_5ED():
        TurnDirection(0x1, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_5ED)
    Sleep(50)

    def lambda_5FD():
        TurnDirection(0x2, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_5FD)
    Sleep(50)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)

    #C0005
    ChrTalk(
        0x101,
        (
            "#00006F如果你们两个一起上去胡闹，\x01",
            "未免也太吵了吧……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    #C0006
    ChrTalk(
        0x9,
        "#00206F……显然只是开个玩笑而已。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0007
    ChrTalk(
        0x104,
        "#00306F（她刚才绝对是认真的……）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    TurnDirection(0x9, 0x8, 0)
    Return()

    # Function_6_506 end

    def Function_7_6F5(): pass

    label("Function_7_6F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_706")
    Jump("loc_90D")

    label("loc_706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_714")
    Jump("loc_90D")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_722")
    Jump("loc_90D")

    label("loc_722")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_732")
    Jump("loc_90D")

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_740")
    Jump("loc_90D")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_74E")
    Jump("loc_90D")

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_75C")
    Jump("loc_90D")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_904")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A7")

    #C0008
    ChrTalk(
        0xA,
        (
            "#00100F没想到塞茜尔小姐她们也会来，\x01",
            "真是吃了一惊。\x02\x03",

            "#00106F特意安排这种惊喜，\x01",
            "还真符合贝尔的作风……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，拜她所赐，\x01",
            "男女比例一下就变得悬殊了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00009F不过，这的确是个\x01",
            "让人开心的惊喜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xA,
        (
            "#00109F这、这倒是没错。\x02\x03",

            "#00106F从小到大，她总能\x01",
            "让我一次又一次地吃惊，\x01",
            "还真有点不甘心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8FF")

    label("loc_8A7")


    #C0012
    ChrTalk(
        0xA,
        (
            "#00100F对了对了，\x01",
            "我刚刚听贝尔说\x01",
            "湖水浴场相当漂亮呢。\x02\x03",

            "#00109F呵呵，真是好期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FF")

    Jump("loc_90D")

    label("loc_904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_90D")

    label("loc_90D")

    TalkEnd(0xFE)
    Return()

    # Function_7_6F5 end

    SaveToFile()

Try(main)
