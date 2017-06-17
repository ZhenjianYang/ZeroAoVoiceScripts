from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t113b.bin",                # FileName
        "t113b",                    # MapName
        "t113b",                    # Location
        0x0049,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 73, 0, 4, 0, 5],
    )

    BuildStringList((
        "t113b",                  # 0
        "瓦吉",                   # 1
        "詹姆斯",                 # 2
        "艾维琳夫人",             # 3
        "尼基塔",                 # 4
        "帕梅拉",                 # 5
        "管家芬特",               # 6
        "管家克里斯托夫",         # 7
        "朱蒂",                   # 8
    ))

    AddCharChip((
        "apl/ch50353.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch33300.itc",                   # 02
        "chr/ch26800.itc",                   # 03
        "chr/ch25600.itc",                   # 04
        "chr/ch25900.itc",                   # 05
        "chr/ch25700.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-150,    100,     -1149,   180,  469,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(5349,    0,       -3500,   315,  385,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4000,    0,       -2150,   135,  385,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4500,    0,       -3500,   180,  385,  0x0, 0,   3,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(5599,    0,       -12590,  0,    257,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3859,    0,       -13729,  0,    257,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-3150,   0,       3569,    90,   385,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-2099,   0,       3569,    270,  385,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)

    ScpFunction((
        "Function_0_22C",          # 00, 0
        "Function_1_2E4",          # 01, 1
        "Function_2_395",          # 02, 2
        "Function_3_3C0",          # 03, 3
        "Function_4_41A",          # 04, 4
        "Function_5_533",          # 05, 5
        "Function_6_53D",          # 06, 6
        "Function_7_815",          # 07, 7
        "Function_8_883",          # 08, 8
        "Function_9_8D6",          # 09, 9
        "Function_10_9F2",         # 0A, 10
        "Function_11_C32",         # 0B, 11
        "Function_12_DB7",         # 0C, 12
        "Function_13_DE9",         # 0D, 13
        "Function_14_E23",         # 0E, 14
        "Function_15_17AF",        # 0F, 15
    ))


    def Function_0_22C(): pass

    label("Function_0_22C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_26C"),
        (1, "loc_278"),
        (2, "loc_284"),
        (3, "loc_290"),
        (4, "loc_29C"),
        (5, "loc_2A8"),
        (6, "loc_2B4"),
        (SWITCH_DEFAULT, "loc_2C0"),
    )


    label("loc_26C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_278")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_284")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_290")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_29C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2E3")

    Return()

    # Function_0_22C end

    def Function_1_2E4(): pass

    label("Function_1_2E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_394")
    OP_95(0xFE, 3320, 0, -13010, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, 3320, 0, -6980, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 3320, 0, -9020, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 3320, 0, -16960, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    Jump("Function_1_2E4")

    label("loc_394")

    Return()

    # Function_1_2E4 end

    def Function_2_395(): pass

    label("Function_2_395")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BF")
    OP_94(0xFE, 0x79E, 0xFFFFFB1E, 0x19E6, 0xFFFFFD8A, 0x3E8)
    Sleep(300)
    Jump("Function_2_395")

    label("loc_3BF")

    Return()

    # Function_2_395 end

    def Function_3_3C0(): pass

    label("Function_3_3C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_419")
    OP_95(0xFE, -5090, 0, -19580, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -5090, 0, -1190, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    Jump("Function_3_3C0")

    label("loc_419")

    Return()

    # Function_3_3C0 end

    def Function_4_41A(): pass

    label("Function_4_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_46A")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 4670, 0, -1000, 0)
    BeginChrThread(0xC, 0, 0, 2)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -5090, 0, -1190, 180)
    BeginChrThread(0xD, 0, 0, 3)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_521")

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4B0")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3020, 0, -13010, 360)
    BeginChrThread(0xC, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -5090, 0, -1190, 180)
    BeginChrThread(0xD, 0, 0, 3)
    Jump("loc_521")

    label("loc_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_4F0")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3020, 0, -13010, 360)
    BeginChrThread(0xC, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1660, 0, 4960, 180)
    Jump("loc_521")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_521")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_521")
    ClearChrFlags(0xB, 0x80)

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_532")
    Event(0, 14)

    label("loc_532")

    Return()

    # Function_4_41A end

    def Function_5_533(): pass

    label("Function_5_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_53C")

    label("loc_53C")

    Return()

    # Function_5_533 end

    def Function_6_53D(): pass

    label("Function_6_53D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D1")
    Jump("loc_61B")

    label("loc_5D1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61B")

    label("loc_5F1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_611")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61B")

    label("loc_611")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C8")

    #C0001
    ChrTalk(
        0x8,
        (
            "#5702F呵呵……稍后再见。\x02\x03",

            "#5709F这场争吵想必还会继续吧，\x01",
            "我会暂时待在这里。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_6F3")

    #C0002
    ChrTalk(
        0x102,
        (
            "#5306F你……\x01",
            "刚才明明是你煽动起来的，\x01",
            "现在却说得好像事不关己一样……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_6F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_729")

    #C0003
    ChrTalk(
        0x103,
        "#5411F……说得好像事不关己一样呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_794")

    label("loc_729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_794")

    #C0004
    ChrTalk(
        0x104,
        (
            "#5602F你刚才还说要和人家寻求刺激，\x01",
            "现在却像个没事人一样，\x01",
            "这种不负责任的话亏你说得出口啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_794")


    #C0005
    ChrTalk(
        0x101,
        "#5106F好、好啦……瓦吉你也适可而止吧？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_80D")

    label("loc_7C8")


    #C0006
    ChrTalk(
        0x8,
        (
            "#5702F呵呵……稍后再见。\x02\x03",

            "等到他们两个人吵完了，\x01",
            "我就会去会场。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_53D end

    def Function_7_815(): pass

    label("Function_7_815")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82A")
    Call(0, 9)
    Jump("loc_87F")

    label("loc_82A")

    TurnDirection(0x9, 0xA, 0)

    #C0007
    ChrTalk(
        0x9,
        (
            "事情就是这样！\x01",
            "让我道歉多少次都可以！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "所以，艾维琳……\x01",
            "请原谅我吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87F")

    TalkEnd(0xFE)
    Return()

    # Function_7_815 end

    def Function_8_883(): pass

    label("Function_8_883")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_898")
    Call(0, 9)
    Jump("loc_8D2")

    label("loc_898")

    TurnDirection(0xA, 0x9, 0)

    #C0009
    ChrTalk(
        0xA,
        (
            "我再也不会理你了！\x01",
            "既然如此，我就和瓦吉……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D2")

    TalkEnd(0xFE)
    Return()

    # Function_8_883 end

    def Function_9_8D6(): pass

    label("Function_9_8D6")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)

    #C0010
    ChrTalk(
        0x9,
        (
            "啊啊，艾维琳，等等！\x01",
            "是我不好……\x01",
            "请不要再说什么回娘家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "我和尼基塔，那个……\x01",
            "是我一时昏了头……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        "你还敢说这么厚颜无耻的话……！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "真是受够了！\x01",
            "我一定会向婆婆大人\x01",
            "报告这次的事情！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "怎、怎么可以！\x01",
            "只有这件事，请你饶了我吧……！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_9_8D6 end

    def Function_10_9F2(): pass

    label("Function_10_9F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_ACD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA2")

    #C0015
    ChrTalk(
        0xFE,
        "哎呀，那个孩子是……？\x02",
    )

    CloseMessageWindow()

    #N0016
    NpcTalk(
        0x101,
        "琪雅",
        "#5810F我叫琪雅！\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "那、那个……？\x01",
            "（客人中也有这么小的孩子吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#0001F对、对不起，我们还有急事！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_AC8")

    label("loc_AA2")


    #C0019
    ChrTalk(
        0xFE,
        "（客人中也有这么小的孩子吗……）\x02",
    )

    CloseMessageWindow()

    label("loc_AC8")

    Jump("loc_C2E")

    label("loc_ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_AEF")

    #C0020
    ChrTalk(
        0xFE,
        "啊啊，好忙……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C2E")

    label("loc_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_BBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B72")

    #C0021
    ChrTalk(
        0xFE,
        (
            "呼……刚才那对吵架的夫妻\x01",
            "终于平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "我还在想，要是出现流血场面的话，\x01",
            "可该如何是好呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BBA")

    label("loc_B72")


    #C0023
    ChrTalk(
        0xFE,
        (
            "总之，终于可以\x01",
            "开始打扫了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "已经耽误了不少时间，\x01",
            "赶快继续吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBA")

    Jump("loc_C2E")

    label("loc_BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_C2E")

    #C0025
    ChrTalk(
        0xFE,
        (
            "在这种地方吵架，害得我没法\x01",
            "打扫卫生，真是头疼。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "而且，看现在的气氛，\x01",
            "外人也很难介入劝架……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2E")

    TalkEnd(0xFE)
    Return()

    # Function_10_9F2 end

    def Function_11_C32(): pass

    label("Function_11_C32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_CA2")

    #C0027
    ChrTalk(
        0xFE,
        (
            "鲁巴彻商会的人\x01",
            "突然交代说\x01",
            "不许离开这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "害得我很紧张呢，\x01",
            "大概是发生了什么事吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB3")

    label("loc_CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_D0B")

    #C0029
    ChrTalk(
        0xFE,
        (
            "必须在拍卖会结束前\x01",
            "把晚宴的准备工作\x01",
            "给做好才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "这边的扫除也\x01",
            "必须要尽快做完……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB3")

    label("loc_D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_D79")

    #C0031
    ChrTalk(
        0xFE,
        (
            "这里是接待室……\x01",
            "为了款待贵宾而准备的场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "今天并不准备投入使用，\x01",
            "请您尽量不要进来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB3")

    label("loc_D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_DB3")

    #C0033
    ChrTalk(
        0xFE,
        (
            "……在那二位安静下来之前，\x01",
            "只有放弃打扫了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB3")

    TalkEnd(0xFE)
    Return()

    # Function_11_C32 end

    def Function_12_DB7(): pass

    label("Function_12_DB7")

    TalkBegin(0xFE)

    #C0034
    ChrTalk(
        0xFE,
        (
            "哎呀，这位客人……\x01",
            "到底发生什么事了？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_DB7 end

    def Function_13_DE9(): pass

    label("Function_13_DE9")

    TalkBegin(0xFE)

    #C0035
    ChrTalk(
        0xFE,
        (
            "屋里好像\x01",
            "很热闹的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "发生什么事了吗？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_DE9 end

    def Function_14_E23(): pass

    label("Function_14_E23")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrSubChip(0x8, 0x1)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, -150, 100, -1150, 180)
    SetChrPos(0xA, 3750, 0, -3000, 90)
    SetChrPos(0x9, 5150, 0, -3600, 270)
    SetChrPos(0xB, 5150, 0, -2400, 270)
    SetChrPos(0x101, -600, 0, 4900, 180)
    SetChrPos(0xEF, 600, 0, 4900, 180)
    OP_68(0, 1200, 6000, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0037
    NpcTalk(
        0x9,
        "男性的声音",
        (
            "不、不是都说了吗……\x01",
            "这只是个误会啊！\x02",
        )
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0x9,
        "男性的声音",
        (
            "我和这位女士\x01",
            "只是普通的工作关系……\x02",
        )
    )

    CloseMessageWindow()

    #N0039
    NpcTalk(
        0xA,
        "女性的声音",
        "不，我才不会被你哄骗！\x02",
    )

    CloseMessageWindow()

    #N0040
    NpcTalk(
        0xA,
        "女性的声音",
        (
            "我说你的样子怎么有些奇怪，\x01",
            "果然是和其他女人\x01",
            "勾搭在一起了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2850, 1200, -2450, 3500)
    OP_6F(0x1)
    Sleep(300)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-550, 1200, -1000, 4000)
    SetChrSubChip(0x8, 0x0)

    def lambda_1015():
        OP_95(0xFE, -1700, 0, -1250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1015)
    Sleep(150)
    SetChrSubChip(0x8, 0x2)
    Sleep(350)

    def lambda_1039():
        OP_95(0xFE, -1600, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1039)
    WaitChrThread(0x101, 1)

    def lambda_1057():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1057)
    WaitChrThread(0xEF, 1)

    def lambda_1068():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1068)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x1)

    #C0041
    ChrTalk(
        0x8,
        (
            "#5702F#11P各位，晚上好啊。\x01",
            "能顺利到达，真是万幸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#5104F#6P托你的福。\x02\x03",

            "#5101F……说起来，\x01",
            "这么吵闹，到底发生什么事了？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#5704F#11P呵呵……\x01",
            "如你们所见，气氛险恶到了极点呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4450, 1200, -3000, 2000)
    SetChrSubChip(0x8, 0x0)
    Sleep(150)
    SetChrSubChip(0x8, 0x1)
    OP_6F(0x1)

    #C0044
    ChrTalk(
        0x9,
        (
            "#11P──你、你还不是\x01",
            "和那种打扮古怪的\x01",
            "少年混在一起！\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "#11P难、难、难道说，\x01",
            "你们是那种关系吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xA,
        (
            "#5P这个男孩是在我困难的时候\x01",
            "出手相助的恩人！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xA,
        (
            "#5P我刚来克洛斯贝尔的时候毫无头绪，\x01",
            "是他在我一筹莫展的时候帮助了我……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xA,
        (
            "#5P带我来拍卖会场，\x01",
            "还耐心地陪伴我……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xA,
        (
            "#5P才不是你和这个女人\x01",
            "的那种暧昧关系！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        "#11P唔……\x02",
    )

    CloseMessageWindow()
    OP_68(1600, 1200, -2500, 1200)
    OP_6F(0x1)

    #C0051
    ChrTalk(
        0x8,
        (
            "#5709F#6P呵呵，如果您想更进一步，\x01",
            "我也是不介意的哦。\x02\x03",

            "#5702F──喂，这位夫人。\x02\x03",

            "别再理会那个薄情的男人了，\x01",
            "去和我寻求一些刺激如何？\x02\x03",

            "#5704F像夫人您这么活泼可爱的女性，\x01",
            "我可是一点也不讨厌呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x10E, 0x1F4)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0052
    ChrTalk(
        0xA,
        "#11P瓦、瓦吉，那种事……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(1000)
    OP_98(0x9, 0xFFFFFD12, 0x0, 0x0, 0x7D0, 0x0)

    #C0053
    ChrTalk(
        0x9,
        "#11P你、你这家伙！\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "#11P不要随便引诱\x01",
            "别人的妻子啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 500)

    #C0055
    ChrTalk(
        0xB,
        (
            "#5P啊啊，真是的……\x01",
            "我实在是受够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xB,
        (
            "#5P詹姆斯先生，\x01",
            "你要是想脚踩两条船，\x01",
            "还需要多练练哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1499():

        label("loc_1499")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_1499")

    QueueWorkItem2(0x9, 1, lambda_1499)

    def lambda_14AB():

        label("loc_14AB")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_14AB")

    QueueWorkItem2(0xA, 1, lambda_14AB)
    OP_93(0xB, 0x13B, 0x1F4)

    #C0057
    ChrTalk(
        0xB,
        (
            "#2P真是的，我要赶快去\x01",
            "找其他的客人了……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(950, 1200, -1850, 3000)
    BeginChrThread(0xB, 3, 0, 15)
    Sleep(500)

    #C0058
    ChrTalk(
        0x9,
        "#11P尼、尼基塔……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    OP_6F(0x1)
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x9, 500)

    #C0059
    ChrTalk(
        0xA,
        (
            "#5P说、说什么普通的工作关系，\x01",
            "果然都是骗我的啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        "#5P我、我已经彻底受够了！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "#5P我现在就要\x01",
            "回娘家去了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    #C0062
    ChrTalk(
        0x9,
        "#11P艾维琳，你怎么可以……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_166E")

    #C0063
    ChrTalk(
        0x102,
        (
            "#5306F#6P看、看起来，\x01",
            "不太好去打扰他们啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DB")

    label("loc_166E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_16A4")

    #C0064
    ChrTalk(
        0x103,
        (
            "#5400F#6P原来如此……\x01",
            "夫妻吵架吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DB")

    label("loc_16A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_16DB")

    #C0065
    ChrTalk(
        0x104,
        (
            "#5609F#6P哈，夫妻吵架，\x01",
            "外人不能插手啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DB")


    #C0066
    ChrTalk(
        0x101,
        (
            "#5112F#6P……那个，我们\x01",
            "先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sleep(200)

    #C0067
    ChrTalk(
        0x8,
        (
            "#5704F#11P呵呵，也好。\x02\x03",

            "#5702F──稍后见，\x01",
            "请尽情享受晚宴吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -2009, 0, -1560, 270)
    SetChrPos(0x9, 5350, 0, -3500, 315)
    SetChrPos(0xA, 4000, 0, -2150, 135)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetChrSubChip(0x8, 0x0)
    OP_49()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xA5, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_E23 end

    def Function_15_17AF(): pass

    label("Function_15_17AF")


    def lambda_17B4():
        OP_95(0xFE, 0, 0, 4600, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_17B4)
    WaitChrThread(0xB, 1)

    def lambda_17D2():
        OP_95(0xFE, 0, 0, 6750, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_17D2)
    Sleep(250)

    def lambda_17EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_17EF)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    Return()

    # Function_15_17AF end

    SaveToFile()

Try(main)
