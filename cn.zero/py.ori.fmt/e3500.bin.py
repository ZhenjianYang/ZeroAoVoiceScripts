from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "e3500.bin",                # FileName
        "e3500",                    # MapName
        "e3500",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "e3500",                  # 0
        "赛尔盖科长",             # 1
        "琪雅",                   # 2
        "蔡特",                   # 3
        "罗伊德",                 # 4
        "艾莉",                   # 5
        "缇欧",                   # 6
        "兰迪",                   # 7
        "琪雅影",                 # 8
        "罗伊德影",               # 9
        "艾莉影",                 # 10
        "缇欧影",                 # 11
        "兰迪影",                 # 12
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_218",          # 00, 0
        "Function_1_234",          # 01, 1
        "Function_2_253",          # 02, 2
        "Function_3_30B",          # 03, 3
        "Function_4_31B",          # 04, 4
        "Function_5_31C",          # 05, 5
        "Function_6_1324",         # 06, 6
        "Function_7_1349",         # 07, 7
        "Function_8_1418",         # 08, 8
        "Function_9_1474",         # 09, 9
        "Function_10_14C5",        # 0A, 10
        "Function_11_1537",        # 0B, 11
    ))


    def Function_0_218(): pass

    label("Function_0_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_233")
    OP_A1(0xFE, 0x4B0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_218")

    label("loc_233")

    Return()

    # Function_0_218 end

    def Function_1_234(): pass

    label("Function_1_234")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_252")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_1_234")

    label("loc_252")

    Return()

    # Function_1_234 end

    def Function_2_253(): pass

    label("Function_2_253")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_293"),
        (1, "loc_29F"),
        (2, "loc_2AB"),
        (3, "loc_2B7"),
        (4, "loc_2C3"),
        (5, "loc_2CF"),
        (6, "loc_2DB"),
        (SWITCH_DEFAULT, "loc_2E7"),
    )


    label("loc_293")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_29F")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2AB")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2B7")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2C3")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2CF")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2DB")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2E7")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30A")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_30A")

    Return()

    # Function_2_253 end

    def Function_3_30B(): pass

    label("Function_3_30B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 0)), scpexpr(EXPR_END)), "loc_31A")
    ClearScenarioFlags(0x5E, 0)
    Event(0, 5)

    label("loc_31A")

    Return()

    # Function_3_30B end

    def Function_4_31B(): pass

    label("Function_4_31B")

    Return()

    # Function_4_31B end

    def Function_5_31C(): pass

    label("Function_5_31C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    LoadChrToIndex("apl/ch50561.itc", 0x1F)
    LoadChrToIndex("apl/ch50563.itc", 0x20)
    LoadChrToIndex("apl/ch50564.itc", 0x21)
    LoadChrToIndex("apl/ch50565.itc", 0x22)
    LoadChrToIndex("apl/ch50567.itc", 0x23)
    LoadChrToIndex("apl/ch50568.itc", 0x24)
    LoadChrToIndex("apl/ch50569.itc", 0x25)
    LoadChrToIndex("apl/ch50570.itc", 0x26)
    LoadChrToIndex("apl/ch50571.itc", 0x27)
    LoadChrToIndex("apl/ch50572.itc", 0x28)
    SetChrPos(0x101, -300, 0, 2200, 90)
    SetChrPos(0x102, -300, 0, 1200, 45)
    SetChrPos(0x104, -1100, 0, 3400, 135)
    SetChrPos(0x103, 0, 0, 3600, 135)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 1900, 0, 2200, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, 2000, 0, 4100, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 4000, 30, 2200, 270)
    BeginChrThread(0xA, 0, 0, 1)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0xA)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis177.itp")
    CreatePortrait(1, 13, 87, 269, 215, 0, 0, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x1, "c_vis178.itp")
    CreatePortrait(2, 13, 178, 269, 306, 0, 0, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x1, "c_vis179.itp")
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W之后────\x02\x03",

            "白热化的市长竞选落下帷幕，\x01",
            "我们也回到了正常工作中……\x02\x03",

            "而琪雅背着\x01",
            "崭新的书包，\x01",
            "站在了特别任务支援科的门前。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7105", 0)
    OP_68(1010, 1100, 2620, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(20500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0002
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯……真的没问题吗？\x02\x03",

            "#0001F第一天果然还是\x01",
            "由我陪着比较好吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x9,
        (
            "#11P#1103F没问题，\x01",
            "路线我都记住了。\x02\x03",

            "#1100F而且亨利和隆\x01",
            "也会和我一起去。\x02\x03",

            "#1110F罗伊德，你太爱操心了！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#6P#0011F可、可是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0005
    ChrTalk(
        0x102,
        (
            "#12P#0106F真是的……\x01",
            "简直就像是个唠叨的父亲一样。\x02\x03",

            "#0111F你小时候也曾在\x01",
            "没有大人陪同的情况下，\x01",
            "和同龄的伙伴们一起上学吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0006
    ChrTalk(
        0x101,
        "#5P#0012F哈哈，话是这样说啦……\x02",
    )

    CloseMessageWindow()

    def lambda_759():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_759)
    Sleep(100)

    def lambda_769():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_769)
    Sleep(50)

    def lambda_779():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_779)
    WaitChrThread(0x104, 2)

    #C0007
    ChrTalk(
        0x103,
        (
            "#5P#0202F……话说回来，艾莉前辈\x01",
            "不是也很紧张吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#12P#0112F呃……\x02\x03",

            "#0113F这、这是……\x01",
            "出于保护者的意识……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#5P#0304F……哎呀呀，对阿琪来说，\x01",
            "这可是个难得的好日子啊。\x02\x03",

            "#0300F现在也没有人打她的主意了，\x01",
            "就安心地目送她上学吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        "#11P#1200F呜噜噜……嗷呜。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0011
    ChrTalk(
        0x101,
        (
            "#12P#0006F啊，那个……\x01",
            "虽然这些我全都明白，但还是……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#12P#0106F……我也理解你那种\x01",
            "为人父般的心情。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#5P#1004F呵呵……\x02\x03",

            "#1002F──对了，新市长不是\x01",
            "要找你们商量些事情吗？\x02\x03",

            "差不多也该出发了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_96D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_96D)
    Sleep(100)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)

    def lambda_985():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_985)

    def lambda_992():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_992)
    Sleep(50)

    def lambda_9A2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9A2)
    Sleep(50)

    def lambda_9B2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9B2)
    WaitChrThread(0x104, 2)

    #C0014
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊，是……\x02\x03",

            "#0000F……对了，科长，\x01",
            "您知道些什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#6P#0205F到底要商量什么呢？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#5P#1004F呵呵，这个嘛，你们还是\x01",
            "直接去问新市长更好吧。\x02\x03",

            "#1002F──总之，\x01",
            "对你们来说，\x01",
            "今天应该是崭新的一天。\x02\x03",

            "给我打起精神来。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#6P#0002F……明白了。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        (
            "#3P#0309F哎呀呀，\x01",
            "好像又有得忙了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#6P#0204F呼，虽然忙碌\x01",
            "早就是常事了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)

    #C0020
    ChrTalk(
        0x102,
        (
            "#6P#0102F那么，小琪雅，\x01",
            "我们就顺路送你到大街那边吧。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    def lambda_B61():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B61)
    Sleep(50)

    def lambda_B71():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B71)
    Sleep(50)

    def lambda_B81():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B81)
    Sleep(50)

    def lambda_B91():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B91)
    Sleep(50)

    def lambda_BA1():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BA1)
    SetChrSubChip(0xA, 0x0)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x9, 2)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    BeginChrThread(0x9, 3, 0, 6)
    Sleep(500)

    #C0021
    ChrTalk(
        0x9,
        "#11P#1109F嗯！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x9, 3)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x800)
    ClearChrFlags(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x1)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x1)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x2)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x1)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x1)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0x9, 301000, 0, 2500, 0)
    SetChrPos(0xB, 300250, 0, 2650, 0)
    SetChrPos(0xC, 299700, 0, 3600, 0)
    SetChrPos(0xD, 301750, 0, 2700, 0)
    SetChrPos(0xE, 302300, 0, 3900, 0)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x1)
    SetChrChipByIndex(0xF, 0x27)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x100)
    SetChrFlags(0xF, 0x800)
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0xF, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0xF, 0xFFFEA070, 0x2BF20, 0x0, 0x0)
    OP_52(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x1)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x100)
    SetChrFlags(0x10, 0x800)
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x10, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0x10, 0xFFFEA070, 0x2BF20, 0xFFFFEC78, 0x0)
    OP_52(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x1)
    SetChrChipByIndex(0x11, 0x26)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x100)
    SetChrFlags(0x11, 0x800)
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x11, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0x11, 0xFFFEA070, 0x2BF20, 0xFFFFCD38, 0x0)
    OP_52(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x1)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x100)
    SetChrFlags(0x12, 0x800)
    OP_52(0x12, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x12, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0x12, 0xFFFEA070, 0x2BF20, 0x1388, 0x0)
    OP_52(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x2)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x1)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x100)
    SetChrFlags(0x13, 0x800)
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x13, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0x13, 0xFFFEA070, 0x2BF20, 0x32C8, 0x0)
    OP_52(0x13, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_E3(0xA)
    WaitBGM()
    Sleep(10)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ed.pmf", 0x3, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(500)
    Sound(2043, 255, 90, 0)    #voice#KeA
    Sleep(1600)
    Sound(2179, 255, 90, 1)    #voice#KeA
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(500)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x1, 0xFF, 0x0)
    Sleep(500)
    OP_DE(0x29, 0x0)
    OP_DE(0x1B, 0x0)
    OP_DE(0x1C, 0x0)
    OP_DE(0x1D, 0x0)
    OP_DE(0x80, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2C, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1275")
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "ＥＸＴＲＡ模式开启。\x02",
        )
    )

    CloseMessageWindow()

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "从标题画面\x01",
            "可以进入ＥＸＴＲＡ模式。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    label("loc_1275")

    SetMessageWindowPos(14, 280, 60, 3)

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～　关于通关存档　～\x01",
            "建立通关存档后，从标题画面读取，\x01",
            "便可继承各项数据，进行二周目的游戏。",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveClearMenu()
    OP_57(0x0)
    OP_5A()
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C7(0x1, 0x10)
    OP_B7(0x0)
    Return()

    # Function_5_31C end

    def Function_6_1324(): pass

    label("Function_6_1324")

    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x3)
    Sleep(110)
    SetChrSubChip(0x9, 0x4)
    Sleep(110)
    SetChrSubChip(0x9, 0x5)
    Sleep(110)
    SetChrSubChip(0x9, 0x4)
    Sleep(110)
    SetChrSubChip(0x9, 0x3)
    Return()

    # Function_6_1324 end

    def Function_7_1349(): pass

    label("Function_7_1349")

    Sleep(150)
    SetChrChipByIndex(0xF, 0x27)
    SetChrSubChip(0xFE, 0x7)
    Sleep(70)
    SetChrSubChip(0xFE, 0x6)
    Sleep(70)
    SetChrSubChip(0xFE, 0x5)
    Sleep(70)
    SetChrSubChip(0xFE, 0x4)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    OP_A7(0xF, 0x0, 0x0, 0x0, 0x50, 0x0)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(400)
    SetChrSubChip(0xFE, 0xF)
    OP_A7(0xF, 0x0, 0x0, 0x0, 0x80, 0x0)
    Sleep(110)
    SetChrSubChip(0xFE, 0xE)
    Sleep(110)
    SetChrSubChip(0xFE, 0xD)
    Sleep(110)
    SetChrSubChip(0xFE, 0x10)
    Sleep(110)
    SetChrSubChip(0xFE, 0x21)
    OP_A7(0xF, 0x0, 0x0, 0x0, 0x50, 0x0)
    Sleep(110)
    SetChrSubChip(0xFE, 0x22)
    Sleep(110)
    SetChrSubChip(0xFE, 0x23)
    Sleep(110)
    SetChrSubChip(0xFE, 0x24)
    OP_A7(0xF, 0x0, 0x0, 0x0, 0x80, 0x0)
    Sleep(110)
    SetChrSubChip(0xFE, 0x25)
    Sleep(110)
    SetChrSubChip(0xFE, 0x20)
    Sleep(110)
    SetChrSubChip(0xFE, 0x21)
    OP_A7(0xF, 0x0, 0x0, 0x0, 0x50, 0x0)
    Return()

    # Function_7_1349 end

    def Function_8_1418(): pass

    label("Function_8_1418")

    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    Sleep(70)
    SetChrSubChip(0xFE, 0x4)
    Sleep(70)
    SetChrSubChip(0xFE, 0x5)
    Sleep(70)
    SetChrSubChip(0xFE, 0x6)
    OP_A7(0x10, 0x0, 0x0, 0x0, 0x50, 0x0)
    Sleep(1400)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(3100)
    Return()

    # Function_8_1418 end

    def Function_9_1474(): pass

    label("Function_9_1474")

    Sleep(600)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    Sleep(70)
    SetChrSubChip(0xFE, 0x4)
    Sleep(70)
    SetChrSubChip(0xFE, 0x5)
    Sleep(70)
    SetChrSubChip(0xFE, 0x6)
    Sleep(500)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(3000)
    Return()

    # Function_9_1474 end

    def Function_10_14C5(): pass

    label("Function_10_14C5")

    Sleep(900)
    SetChrSubChip(0xFE, 0x0)
    OP_A7(0x13, 0x0, 0x0, 0x0, 0x50, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    OP_A7(0x13, 0x0, 0x0, 0x0, 0x80, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    OP_A7(0x13, 0x0, 0x0, 0x0, 0x50, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x4)
    Sleep(70)
    SetChrSubChip(0xFE, 0x5)
    Sleep(70)
    SetChrSubChip(0xFE, 0x6)
    Sleep(700)
    SetChrSubChip(0xFE, 0x6)
    Sleep(50)
    SetChrSubChip(0xFE, 0x7)
    Sleep(50)
    SetChrSubChip(0xFE, 0x8)
    Sleep(50)
    SetChrSubChip(0xFE, 0x9)
    Sleep(3000)
    Return()

    # Function_10_14C5 end

    def Function_11_1537(): pass

    label("Function_11_1537")

    Sleep(450)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    OP_A7(0x11, 0x0, 0x0, 0x0, 0x50, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    Sleep(70)
    SetChrSubChip(0xFE, 0x4)
    OP_A7(0x11, 0x0, 0x0, 0x0, 0x80, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x5)
    Sleep(70)
    SetChrSubChip(0xFE, 0x6)
    Sleep(1100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(2300)
    Return()

    # Function_11_1537 end

    SaveToFile()

Try(main)
