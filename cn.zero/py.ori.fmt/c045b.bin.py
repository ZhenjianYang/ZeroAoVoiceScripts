from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c045b.bin",                # FileName
        "c045b",                    # MapName
        "c045b",                    # Location
        0x0024,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "c045b",                  # 0
        "接待员凯尔",             # 1
        "德莉丝",                 # 2
        "亚伦",                   # 3
        "雷缇希亚经理",           # 4
        "住宿客",                 # 5
        "住宿客",                 # 6
        "住宿客",                 # 7
        "住宿客",                 # 8
        "住宿客",                 # 9
        "冈兹",                   # 10
        "女公关",                 # 11
        "女公关",                 # 12
        "餐具",                   # 13
        "餐具",                   # 14
        "餐具",                   # 15
        "酒",                     # 16
        "酒",                     # 17
        "酒",                     # 18
        "酒",                     # 19
        "酒",                     # 20
    ))

    AddCharChip((
        "apl/ch50403.itc",                   # 00
        "chr/ch26802.itc",                   # 01
        "chr/ch26902.itc",                   # 02
        "apl/ch50090.itc",                   # 03
        "apl/ch50091.itc",                   # 04
        "chr/ch22000.itc",                   # 05
        "chr/ch25700.itc",                   # 06
        "chr/ch27500.itc",                   # 07
        "chr/ch27900.itc",                   # 08
        "chr/ch20200.itc",                   # 09
        "chr/ch34300.itc",                   # 0A
        "chr/ch21800.itc",                   # 0B
        "chr/ch33000.itc",                   # 0C
        "chr/ch32400.itc",                   # 0D
    ))

    DeclNpc(65440,   0,       59970,   270,  261,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4909,    0,       59669,   270,  277,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3529,    0,       59669,   90,   277,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-3990,   0,       7000,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(115110,  0,       62319,   0,    277,  0x0, 0,   9,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(112750,  0,       57849,   270,  261,  0x0, 0,   10,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(153279,  0,       61220,   180,  261,  0x0, 0,   11,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(1769,    0,       7150,    270,  261,  0x0, 0,   12,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2640,    0,       7760,    270,  261,  0x0, 0,   13,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(168500,  150,     6300,    180,  311,  0x0, 0,   0,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(167699,  150,     6300,    180,  261,  0x0, 1,   2,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(169300,  150,     6300,    180,  261,  0x0, 2,   1,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(168500,  349,     4599,    0,    374,  0x0, 0,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(167800,  349,     4599,    0,    374,  0x0, 1,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(169199,  349,     4599,    0,    374,  0x0, 5,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168500,  449,     4199,    0,    374,  0x0, 28,  3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168899,  449,     4199,    0,    374,  0x0, 28,  3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168100,  449,     4199,    0,    374,  0x0, 28,  3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168300,  449,     3799,    0,    374,  0x0, 29,  3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168699,  449,     3799,    0,    374,  0x0, 30,  3,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(168500,  0,       4000,    1500,    168500,  1650,    6300,    0x007E, 0,  16, 0x0000)
    DeclActor(-3500,   0,       7000,    1500,    -3990,   1500,    7000,    0x007E, 0,  5,  0x0000)
    DeclActor(64300,   0,       59970,   1500,    65440,   1500,    59970,   0x007E, 0,  7,  0x0000)
    DeclActor(68050,   0,       11560,   1200,    68050,   1500,    11560,   0x007C, 0,  18, 0x0000)

    ScpFunction((
        "Function_0_3DC",          # 00, 0
        "Function_1_494",          # 01, 1
        "Function_2_4F5",          # 02, 2
        "Function_3_520",          # 03, 3
        "Function_4_521",          # 04, 4
        "Function_5_539",          # 05, 5
        "Function_6_53D",          # 06, 6
        "Function_7_76E",          # 07, 7
        "Function_8_772",          # 08, 8
        "Function_9_986",          # 09, 9
        "Function_10_9FD",         # 0A, 10
        "Function_11_A77",         # 0B, 11
        "Function_12_ACF",         # 0C, 12
        "Function_13_AF7",         # 0D, 13
        "Function_14_B68",         # 0E, 14
        "Function_15_C44",         # 0F, 15
        "Function_16_CA5",         # 10, 16
        "Function_17_CA9",         # 11, 17
        "Function_18_CC0",         # 12, 18
        "Function_19_DA5",         # 13, 19
    ))


    def Function_0_3DC(): pass

    label("Function_0_3DC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_41C"),
        (1, "loc_428"),
        (2, "loc_434"),
        (3, "loc_440"),
        (4, "loc_44C"),
        (5, "loc_458"),
        (6, "loc_464"),
        (SWITCH_DEFAULT, "loc_470"),
    )


    label("loc_41C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_428")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_434")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_440")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_44C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_458")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_464")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_470")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_47C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_493")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_493")

    Return()

    # Function_0_3DC end

    def Function_1_494(): pass

    label("Function_1_494")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F4")
    OP_95(0xFE, 72280, 0, 9750, 1000, 0x0)
    OP_95(0xFE, 72280, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 9750, 1000, 0x0)
    Jump("Function_1_494")

    label("loc_4F4")

    Return()

    # Function_1_494 end

    def Function_2_4F5(): pass

    label("Function_2_4F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51F")
    OP_94(0xFE, 0x604, 0xD714, 0x17C0, 0xFB9A, 0x3E8)
    Sleep(300)
    Jump("Function_2_4F5")

    label("loc_51F")

    Return()

    # Function_2_4F5 end

    def Function_3_520(): pass

    label("Function_3_520")

    Return()

    # Function_3_520 end

    def Function_4_521(): pass

    label("Function_4_521")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_538")
    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_538")

    Return()

    # Function_4_521 end

    def Function_5_539(): pass

    label("Function_5_539")

    Call(0, 6)
    Return()

    # Function_5_539 end

    def Function_6_53D(): pass

    label("Function_6_53D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A")

    #C0001
    ChrTalk(
        0xB,
        "欢迎光临『千禧酒店』。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xB,
        (
            "呵呵，本酒店\x01",
            "为您提供多种多样的服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xB,
        (
            "可以让您在欢乐之都克洛斯贝尔\x01",
            "享受完美的一天。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在酒店或酒馆里休息\x01",
            "可以回复ＣＰ。\x02",
        )
    )

    CloseMessageWindow()

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在普通酒馆里可以回复ＣＰ１００，\x01",
            "在高级酒店里可以回复ＣＰ２００。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x4B, 4)

    label("loc_66A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_674")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76A")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E4")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_765")

    label("loc_6E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F8")
    Jump("loc_765")

    label("loc_6F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_765")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0006
    ChrTalk(
        0xB,
        "哎呀，要住店吗？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xB,
        (
            "今天未被预约的房间\x01",
            "只剩下一间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xB,
        (
            "还请\x01",
            "尽早下决定。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_765")

    Jump("loc_674")

    label("loc_76A")

    TalkEnd(0xB)
    Return()

    # Function_6_53D end

    def Function_7_76E(): pass

    label("Function_7_76E")

    Call(0, 8)
    Return()

    # Function_7_76E end

    def Function_8_772(): pass

    label("Function_8_772")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87B")

    #C0009
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎光临『千禧酒店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "如果需要预约房间，\x01",
            "请在本服务台办理手续。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在酒店或酒馆里休息\x01",
            "可以回复ＣＰ。\x02",
        )
    )

    CloseMessageWindow()

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在普通酒馆里可以回复ＣＰ１００，\x01",
            "在高级酒店里可以回复ＣＰ２００。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x4B, 4)

    label("loc_87B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_885")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_982")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_8D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F5")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97D")

    label("loc_8F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_909")
    Jump("loc_97D")

    label("loc_909")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0013
    ChrTalk(
        0x8,
        (
            "本酒店的豪华客房\x01",
            "在酒店顶层。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "这边是副馆接待处，\x01",
            "从楼梯上去，\x01",
            "即可到达豪华客房。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97D")

    Jump("loc_885")

    label("loc_982")

    TalkEnd(0x8)
    Return()

    # Function_8_772 end

    def Function_9_986(): pass

    label("Function_9_986")

    TalkBegin(0xFE)
    OP_4B(0x9, 0xFF)

    #C0015
    ChrTalk(
        0xA,
        (
            "小费也是那位客人的一番好意……\x01",
            "德莉丝，你就收下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "还有，不要在其他客人的面前\x01",
            "商量这种事哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_9_986 end

    def Function_10_9FD(): pass

    label("Function_10_9FD")

    TalkBegin(0xFE)
    OP_4B(0xA, 0xFF)

    #C0017
    ChrTalk(
        0x9,
        (
            "住在顶层的客人\x01",
            "给了我一笔\x01",
            "数额惊人的小费。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "这、这么多钱，该怎么办呀……\x01",
            "还是报告给经理比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_10_9FD end

    def Function_11_A77(): pass

    label("Function_11_A77")

    TalkBegin(0xFE)

    #C0019
    ChrTalk(
        0xFE,
        (
            "唔～真是个美好的夜晚，\x01",
            "我都想喝杯极品美酒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "呼哈哈，呼哈哈哈哈……！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_A77 end

    def Function_12_ACF(): pass

    label("Function_12_ACF")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        (
            "爸爸真是的，\x01",
            "得意什么呢……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_ACF end

    def Function_13_AF7(): pass

    label("Function_13_AF7")

    TalkBegin(0xFE)

    #C0022
    ChrTalk(
        0xFE,
        (
            "拜托交易对象订了旅馆，\x01",
            "没想到是这么高级的酒店。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "这有一半算是应酬吧。\x01",
            "唉唉，真不知道之后会怎样。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_AF7 end

    def Function_14_B68(): pass

    label("Function_14_B68")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD7")

    #C0024
    ChrTalk(
        0xFE,
        (
            "我和我太太预约了\x01",
            "顶层的一间客房。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "待在克洛斯贝尔的这段期间，\x01",
            "就决定住在这里了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C40")

    label("loc_BD7")


    #C0026
    ChrTalk(
        0xFE,
        (
            "如此说来……\x01",
            "听说有个人\x01",
            "把这里的豪华套房包下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "呵呵，是哪里的有钱少爷吗？\x01",
            "挺让人感兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C40")

    TalkEnd(0xFE)
    Return()

    # Function_14_B68 end

    def Function_15_C44(): pass

    label("Function_15_C44")

    TalkBegin(0xFE)

    #C0028
    ChrTalk(
        0xFE,
        (
            "说到千禧酒店，\x01",
            "一直都是以格调高雅而闻名的。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "住宿还是应该\x01",
            "选择值得信赖的地方呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_C44 end

    def Function_16_CA5(): pass

    label("Function_16_CA5")

    Call(0, 17)
    Return()

    # Function_16_CA5 end

    def Function_17_CA9(): pass

    label("Function_17_CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBF")
    Call(0, 19)
    Jump("loc_CBF")

    label("loc_CBF")

    Return()

    # Function_17_CA9 end

    def Function_18_CC0(): pass

    label("Function_18_CC0")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0030
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("冈兹的声音")

    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……嗯啊～……呼啊～……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA1")

    #C0032
    ChrTalk(
        0x101,
        (
            "#0001F冈兹先生，\x01",
            "好像醉倒睡着了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#0106F差不多该回支援科了吧。\x01",
            "小琪雅还在等着我们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#6P#0000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_DA1")

    TalkEnd(0xFF)
    Return()

    # Function_18_CC0 end

    def Function_19_DA5(): pass

    label("Function_19_DA5")

    EventBegin(0x0)
    Fade(1000)
    OP_68(168500, 1000, 4800, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 169000, 0, 2900, 0)
    SetChrPos(0x103, 169300, 0, 1800, 0)
    SetChrPos(0x102, 167700, 0, 2100, 0)
    SetChrPos(0x104, 168000, 0, 2900, 0)
    SetChrPos(0x11, 168500, 150, 6300, 180)
    SetChrPos(0x12, 167700, 150, 6300, 180)
    SetChrPos(0x13, 169300, 150, 6300, 180)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis083.itp")
    OP_0D()
    SetChrSubChip(0x12, 0x0)
    Sleep(50)
    SetChrSubChip(0x13, 0x0)
    Sleep(300)

    #C0035
    ChrTalk(
        0x12,
        "#11P啊～兰迪先生？\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x13,
        "#11P哎呀，好久不见啦。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        "#0309F#5P哈哈，好久不见了。\x02",
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0x11,
        "喝醉的男子",
        "#11P嗯嗯？你们是什么人……？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#6P#0003F──打扰了，\x01",
            "我们是克洛斯贝尔警察局的人。\x02\x03",

            "#0000F您是玛因兹的冈兹先生吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x11,
        "#11P嗝，是啊……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x11,
        (
            "#11P我好像\x01",
            "在哪里见过你们几个……？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#6P#0211F……话说，这个人……\x02\x03",

            "不就是军犬风波的时候\x01",
            "差点被袭击的\x01",
            "矿工之一吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#6P#0011F啊……！\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x3C, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)

    #A0045
    AnonymousTalk(
        0x102,
        "#0105F是那时的……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    VolumeBGM(0x64, 0x1F4)

    #C0046
    ChrTalk(
        0x11,
        "#11P哦？还有过那种事吗？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x11,
        (
            "#11P想起来了……\x01",
            "确实是当时的那些警察小鬼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x11,
        "#11P你们找本大爷有什么事？嗝！\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#6P#0006F那个，其实是玛因兹的\x01",
            "镇长先生拜托我们……\x02\x03",

            "#0000F来寻找您的下落。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0050
    ChrTalk(
        0x11,
        "#11P镇长找我……？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x11,
        (
            "#11P嗝……\x01",
            "到底有什么事？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#0301F#5P你啊，都过来两个星期了，\x01",
            "也没给镇上一个联络吧？\x02\x03",

            "那边还以为你失踪了，\x01",
            "担心得不得了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#6P#0100F所以才委托我们\x01",
            "过来寻找您的。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x11,
        "#11P嗝，原来如此啊。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x11,
        (
            "#11P那不就没事了吗～\x01",
            "反正现在都已经找到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x11,
        (
            "#11P呵呵，话虽如此，\x01",
            "但我可没打算再回\x01",
            "什么玛因兹了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0057
    ChrTalk(
        0x101,
        "#6P#0005F是、是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        "#6P#0205F到底是为什么……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x96, 0x0, 0xBB8, 0x190)

    #C0059
    ChrTalk(
        0x11,
        "#11P哇哈哈，那还用问吗！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x11,
        (
            "#11P因为我已经得到了！\x01",
            "得到了天才般的技巧！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x11,
        (
            "#11P不光是技术与直觉！\x01",
            "连女神的幸运也都属于本大爷了！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x11,
        (
            "#11P谁还要回那种乡下地方，\x01",
            "挖什么破矿洞啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        "#6P#0106F怎么这样……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        "#0301F#5P喂喂……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#6P#0006F那个，这样好吗？\x02\x03",

            "#0001F大家都很担心您，\x01",
            "至少也先跟镇长先生联络一下……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0066
    ChrTalk(
        0x11,
        (
            "#11P#4S烦死了！\x01",
            "少对我指手划脚的！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x11,
        (
            "#11P哼哼，再赚一票，\x01",
            "然后就去米修拉姆吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0x1)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0068
    ChrTalk(
        0x11,
        (
            "#5P喂，小姐们！\x01",
            "周末我带你们\x01",
            "去主题公园吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x11,
        (
            "#5P去宝石店和精品店，\x01",
            "喜欢什么就给你们买什么！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x13, 0x2)
    Sleep(300)

    #C0070
    ChrTalk(
        0x12,
        "#5P哇～真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x13,
        (
            "#11P呵呵……\x01",
            "那我们就尽情期待啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    LoadChrToIndex("chr/ch26800.itc", 0x1E)
    LoadChrToIndex("chr/ch26900.itc", 0x1F)
    LoadChrToIndex("apl/ch50011.itc", 0x20)
    OP_68(68000, 1000, 10700, 0)
    MoveCamera(300, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 68000, 0, 13000, 180)
    SetChrPos(0x102, 68000, 0, 13000, 180)
    SetChrPos(0x103, 68000, 0, 13000, 180)
    SetChrPos(0x104, 68000, 0, 13000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x12, 68000, 0, 13000, 180)
    SetChrPos(0x13, 68000, 0, 13000, 180)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(2000, 0)
    Sleep(1000)
    ClearMapObjFlags(0x1, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    OP_68(68000, 1000, 7700, 3000)

    def lambda_17AE():
        OP_96(0xFE, 0x109A0, 0x0, 0x1A2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17AE)

    def lambda_17C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17C8)
    Sleep(500)

    def lambda_17DC():
        OP_96(0xFE, 0x105B8, 0x0, 0x1E14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17DC)

    def lambda_17F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_17F6)
    Sleep(300)

    def lambda_180A():
        OP_96(0xFE, 0x10D88, 0x0, 0x1E14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_180A)

    def lambda_1824():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1824)
    Sleep(500)

    def lambda_1838():
        OP_96(0xFE, 0x109A0, 0x0, 0x21FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1838)

    def lambda_1852():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1852)
    WaitChrThread(0x101, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)

    def lambda_1879():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1879)
    WaitChrThread(0x102, 1)

    def lambda_188A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_188A)
    WaitChrThread(0x103, 1)

    def lambda_189B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_189B)
    WaitChrThread(0x104, 1)

    def lambda_18AC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_18AC)
    WaitChrThread(0x104, 2)
    OP_79(0x1)
    OP_6F(0x1)

    #C0072
    ChrTalk(
        0x104,
        (
            "#0303F#11P……无可救药了啊，这个人。\x02\x03",

            "#0301F完全得意忘形了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#6P#0006F嗯……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        (
            "#0106F#5P很遗憾，看来也只能\x01",
            "把这情况转告给镇长先生了。\x02\x03",

            "#0101F由我们来说服他的话，\x01",
            "似乎也不太合适……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#12P#0206F是啊……\x01",
            "留在这里毕竟是他本人的意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#6P#0008F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C0077
    ChrTalk(
        0x102,
        (
            "#0105F#5P……罗伊德，\x01",
            "你有什么在意的事吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A2C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1A2C)

    #C0078
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯……是有点。\x02\x03",

            "原本既没有好运也没有敏锐的直觉，\x01",
            "是个水平很低，只在周末才来\x01",
            "玩一玩的门外汉……\x02\x03",

            "#0001F为什么会突然变得\x01",
            "百战百胜呢……\x01",
            "我实在是想不通。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        "#0105F#5P这……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#0301F#11P唔，的确很令人在意啊。\x02\x03",

            "#0306F话说～真希望他能\x01",
            "把其中的窍门传授给我啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(150)

    #C0081
    ChrTalk(
        0x103,
        (
            "#6P#0205F听说兰迪前辈的\x01",
            "技术也挺强的……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#0300F#11P那只是状态好的时候啦。\x02\x03",

            "#0306F可是，连着两个星期大获全胜，\x01",
            "赚到五十万米拉，再怎么说我也做不到。\x02\x03",

            "#0302F哈，不过，如果是杰克那样的\x01",
            "超强牌技师，说不定能行吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        "#0106F#5P那只是小说里的故事吧……\x02",
    )

    CloseMessageWindow()
    OP_68(68000, 1000, 9700, 2000)
    MoveCamera(310, 23, 0, 2000)
    SetCameraDistance(23500, 2000)
    Sound(103, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)

    def lambda_1C8F():
        OP_96(0xFE, 0x10B94, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1C8F)

    def lambda_1CA9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1CA9)

    def lambda_1CBA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1CBA)
    Sleep(50)

    def lambda_1CCA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CCA)
    Sleep(50)

    def lambda_1CDA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1CDA)
    Sleep(400)

    def lambda_1CEA():
        OP_96(0xFE, 0x107AC, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1CEA)

    def lambda_1D04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1D04)

    def lambda_1D15():
        OP_96(0xFE, 0x109A0, 0x0, 0x2008, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D15)
    WaitChrThread(0x13, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    WaitChrThread(0x12, 1)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0084
    ChrTalk(
        0x13,
        "#11P哎呀……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x12,
        "#5P怎么，你们还在啊？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#0306F#6P喂喂，这话说的。\x02\x03",

            "#0300F对了……\x01",
            "能不能跟你们打听点事？\x02\x03",

            "是关于那位\x01",
            "叫冈兹的老兄……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x13,
        "#11P呵呵，没问题呀。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x12,
        (
            "#5P怎么了？怎么了？\x01",
            "莫非是和犯罪有关的事？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        (
            "#0303F#6P不，那倒不是……\x02\x03",

            "#0301F那位老兄，\x01",
            "一直都是那副德性吗？\x02\x03",

            "虽说是喝了酒，\x01",
            "但那态度也太蛮横了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x13,
        "#11P嗯～这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x13,
        (
            "#11P一开始的时候，\x01",
            "的确没有这么\x01",
            "嚣张……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x12,
        (
            "#5P不过，他的架子\x01",
            "渐渐就越来越大了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x12,
        (
            "#5P不过，我们的生意就是接待客人，\x01",
            "所以也不是太介意啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        "#0303F#6P唔，是吗……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#6P#0008F如此说来，那种态度，\x01",
            "并不完全是因为喝了酒啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x13,
        (
            "#11P话说回来，\x01",
            "他可真是厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x13,
        (
            "#11P简直就像是可以看透\x01",
            "未翻开的牌一样，\x01",
            "直觉灵敏得不得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x12,
        (
            "#5P嗯嗯！\x01",
            "玩轮盘时还能\x01",
            "准确猜中数字呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x12,
        (
            "#5P就像是能看穿\x01",
            "庄家的想法一样哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        "#0105F#6P那可真够厉害呢……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#6P#0006F呼～如果真的厉害到这种地步，\x01",
            "与其说是直觉，倒不如说是超能力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#0310F#6P呜，为什么这种力量\x01",
            "没有在我身上觉醒呢～！\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x103,
        "#6P#0208F………………………………\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x13,
        (
            "#11P嗯，关于冈兹先生，\x01",
            "我们就知道这么多了……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x12,
        "#5P这些足够了吗？\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#0309F#6P哦哦，多谢了。\x02\x03",

            "#0302F下次有空的时候，\x01",
            "我再去你们店里玩哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x13,
        (
            "#11P呵呵……\x01",
            "虽然不抱期待，不过等你来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x12,
        "#5P那么，下次见～\x02",
    )

    CloseMessageWindow()

    def lambda_2208():

        label("loc_2208")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_2208")

    QueueWorkItem2(0x101, 2, lambda_2208)

    def lambda_221A():

        label("loc_221A")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_221A")

    QueueWorkItem2(0x102, 2, lambda_221A)

    def lambda_222C():

        label("loc_222C")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_222C")

    QueueWorkItem2(0x103, 2, lambda_222C)

    def lambda_223E():

        label("loc_223E")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_223E")

    QueueWorkItem2(0x104, 2, lambda_223E)

    def lambda_2250():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2250)
    Sleep(50)

    def lambda_2260():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2260)
    WaitChrThread(0x12, 2)
    OP_68(65000, 1000, 7700, 5000)

    def lambda_2282():
        OP_96(0xFE, 0x9E34, 0x0, 0x157C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2282)
    WaitChrThread(0x13, 2)

    def lambda_22A0():
        OP_96(0xFE, 0x9E34, 0x0, 0x157C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_22A0)
    OP_6F(0x79)
    Fade(500)
    OP_68(68000, 1000, 7700, 0)
    MoveCamera(300, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x104, 68000, 0, 8700, 270)
    OP_93(0x103, 0x10E, 0x0)
    OP_93(0x104, 0x10E, 0x0)
    OP_0D()
    TurnDirection(0x102, 0x101, 500)

    #C0109
    ChrTalk(
        0x102,
        (
            "#0101F#5P……总而言之，\x01",
            "还是先联络镇长先生\x01",
            "为好吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2377():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2377)

    def lambda_2384():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2384)
    TurnDirection(0x101, 0x102, 500)

    #C0110
    ChrTalk(
        0x101,
        "#6P#0006F嗯，是啊……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德拨通了之前记下的\x01",
            "比克森镇长家的联络号码。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetChrSubChip(0x101, 0x5)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(902, 0, 100, 0)
    Sleep(2800)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "喂喂，\x01",
            "我是比克森……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0113
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000F您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦哦，是你啊。\x02\x03",

            "莫非有什么\x01",
            "消息了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0115
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F不，这个……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德向比克森镇长说明了事情的来龙去脉。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A0117
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "怎么会……\x01",
            "居然有这种事吗！？\x02\x03",

            "没想到那个冈兹\x01",
            "竟然大赢了一笔，\x01",
            "还住在高级酒店里……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0118
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006F我们实在没办法说服他自愿回去，\x01",
            "当然也无法强行将他送回……\x02\x03",

            "#0000F不过，至少先向您报告一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A0119
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，这就足够了。\x02\x03",

            "既然这样，\x01",
            "那我明天就去市里，\x01",
            "到时和他直接谈谈吧。\x02\x03",

            "谢谢你们，真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0120
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0004F哪里，您不必客气。\x02\x03",

            "#0000F如果以后还有什么事情的话，\x01",
            "请随时联络我们。\x02\x03",

            "我们会尽力\x01",
            "帮忙的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A0121
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "谢谢……\x01",
            "到时就要再麻烦你们了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0122
    ChrTalk(
        0x102,
        "#0101F#5P镇长先生怎么说？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0123
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯，他好像也\x01",
            "吓了一跳。\x02\x03",

            "#0000F说是打算明天来克洛斯贝尔市，\x01",
            "直接跟他谈谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0300F#11P嗯，老熟人去跟他谈，\x01",
            "应该是最好不过的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x103,
        "#12P#0203F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 500)

    #C0126
    ChrTalk(
        0x101,
        (
            "#5P#0005F……缇欧？\x02\x03",

            "#0001F从刚才开始，你就一直沉默着，\x01",
            "是有什么在意的事吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_293C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_293C)
    Sleep(50)

    def lambda_294C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_294C)

    #C0127
    ChrTalk(
        0x103,
        (
            "#12P#0203F不……\x02\x03",

            "#0200F只是今天发生了很多事，\x01",
            "我好像有点累了……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        (
            "#5P#0002F是吗……\x01",
            "毕竟还调查了那个遗迹嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#0104F#5P天色都已经暗了，\x01",
            "差不多也该回支援科了吧。\x02\x03",

            "#0102F小琪雅还在等着我们呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    #C0130
    ChrTalk(
        0x103,
        (
            "#12P#0204F呵呵，是啊……\x02\x03",

            "#0202F一看到琪雅的笑容，\x01",
            "疲劳似乎也都会烟消云散了。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#5P#0009F哈哈，太夸张啦。\x02\x03",

            "#0002F不过，心情倒是可以理解啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x104,
        (
            "#0304F#11P哎呀呀，简直就像一群\x01",
            "溺爱孩子的笨蛋爸妈啊……\x02\x03",

            "#0302F那么，就赶快\x01",
            "回去看看阿琪的小脸吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_68(68000, 1500, 9000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 68000, 0, 9000, 180)
    SetChrPos(0x1, 68000, 0, 9000, 180)
    SetChrPos(0x2, 68000, 0, 9000, 180)
    SetChrPos(0x3, 68000, 0, 9000, 180)
    SetScenarioFlags(0xC2, 0)
    OP_29(0x4A, 0x1, 0x5)
    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_19_DA5 end

    SaveToFile()

Try(main)
