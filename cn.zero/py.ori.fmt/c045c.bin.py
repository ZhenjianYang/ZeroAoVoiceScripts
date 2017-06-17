from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c045c.bin",                # FileName
        "c045c",                    # MapName
        "c045c",                    # Location
        0x0024,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 36, 0, 4, 0, 5],
    )

    BuildStringList((
        "c045c",                  # 0
        "接待员凯尔",             # 1
        "德莉丝",                 # 2
        "亚伦",                   # 3
        "雷缇希亚经理",           # 4
        "游客",                   # 5
        "游客",                   # 6
        "游客",                   # 7
        "雾香",                   # 8
    ))

    AddCharChip((
        "chr/ch07300.itc",                   # 00
        "chr/ch21800.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch22300.itc",                   # 03
        "chr/ch25700.itc",                   # 04
        "chr/ch27500.itc",                   # 05
        "chr/ch27900.itc",                   # 06
        "chr/ch33200.itc",                   # 07
    ))

    DeclNpc(65440,   0,       59970,   270,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4090,    9,       59900,   225,  261,  0x0, 0,   4,   0,   0,   2,   0,   11,  255,  0)
    DeclNpc(50740,   0,       9750,    90,   261,  0x0, 0,   5,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(-3990,   0,       7000,    90,   261,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(112779,  0,       57889,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(116599,  0,       58169,   225,  261,  0x0, 0,   3,   0,   0,   3,   0,   13,  255,  0)
    DeclNpc(155360,  0,       59509,   135,  261,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(114040,  0,       5860,    270,  389,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(-3500,   0,       7000,    1500,    -3990,   1500,    7000,    0x007E, 0,  6,  0x0000)
    DeclActor(64300,   0,       59970,   1500,    65440,   1500,    59970,   0x007E, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_220",          # 00, 0
        "Function_1_2D8",          # 01, 1
        "Function_2_339",          # 02, 2
        "Function_3_364",          # 03, 3
        "Function_4_38F",          # 04, 4
        "Function_5_3F4",          # 05, 5
        "Function_6_3F5",          # 06, 6
        "Function_7_3F9",          # 07, 7
        "Function_8_A85",          # 08, 8
        "Function_9_A89",          # 09, 9
        "Function_10_1186",        # 0A, 10
        "Function_11_143D",        # 0B, 11
        "Function_12_16CD",        # 0C, 12
        "Function_13_1922",        # 0D, 13
        "Function_14_1A72",        # 0E, 14
        "Function_15_1C09",        # 0F, 15
        "Function_16_1FD0",        # 10, 16
    ))


    def Function_0_220(): pass

    label("Function_0_220")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_260"),
        (1, "loc_26C"),
        (2, "loc_278"),
        (3, "loc_284"),
        (4, "loc_290"),
        (5, "loc_29C"),
        (6, "loc_2A8"),
        (SWITCH_DEFAULT, "loc_2B4"),
    )


    label("loc_260")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_26C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_278")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_284")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_290")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_29C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2D7")

    Return()

    # Function_0_220 end

    def Function_1_2D8(): pass

    label("Function_1_2D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_338")
    OP_95(0xFE, 72280, 0, 9750, 1000, 0x0)
    OP_95(0xFE, 72280, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 9750, 1000, 0x0)
    Jump("Function_1_2D8")

    label("loc_338")

    Return()

    # Function_1_2D8 end

    def Function_2_339(): pass

    label("Function_2_339")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_363")
    OP_94(0xFE, 0x604, 0xD714, 0x17C0, 0xFB9A, 0x3E8)
    Sleep(300)
    Jump("Function_2_339")

    label("loc_363")

    Return()

    # Function_2_339 end

    def Function_3_364(): pass

    label("Function_3_364")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38E")
    OP_94(0xFE, 0x1C200, 0xDFAC, 0x1CB9C, 0xE8B2, 0x3E8)
    Sleep(300)
    Jump("Function_3_364")

    label("loc_38E")

    Return()

    # Function_3_364 end

    def Function_4_38F(): pass

    label("Function_4_38F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_39D")
    Jump("loc_3F3")

    label("loc_39D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C6")
    SetChrPos(0xF, 63400, 0, 59930, 90)
    ClearChrFlags(0xF, 0x80)

    label("loc_3C6")

    Jump("loc_3F3")

    label("loc_3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3D9")
    Jump("loc_3F3")

    label("loc_3D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3F3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3F3")
    ClearChrFlags(0xF, 0x80)

    label("loc_3F3")

    Return()

    # Function_4_38F end

    def Function_5_3F4(): pass

    label("Function_5_3F4")

    Return()

    # Function_5_3F4 end

    def Function_6_3F5(): pass

    label("Function_6_3F5")

    Call(0, 7)
    Return()

    # Function_6_3F5 end

    def Function_7_3F9(): pass

    label("Function_7_3F9")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_526")

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

    label("loc_526")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_530")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A81")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_580")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_580")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A0")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A7C")

    label("loc_5A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B4")
    Jump("loc_A7C")

    label("loc_5B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_639")

    #C0006
    ChrTalk(
        0xB,
        (
            "终于到了最终日……\x01",
            "我们会以满面笑容恭送\x01",
            "退房的客人们。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xB,
        (
            "衷心期待\x01",
            "他们明年\x01",
            "重游此地。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7C")

    label("loc_639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_712")

    #C0008
    ChrTalk(
        0xB,
        (
            "我听到游行队伍\x01",
            "通过时的音乐了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xB,
        (
            "虽然是从小就听惯了的音乐，\x01",
            "不过每次一听到，就总是……\x01",
            "忍不住兴高采烈起来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xB,
        (
            "身为经理，虽然应该掩饰这种心情，\x01",
            "不过，毕竟我身上也流着\x01",
            "克洛斯贝尔市民的血呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7C")

    label("loc_712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_86D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 4)), scpexpr(EXPR_END)), "loc_77C")

    #C0011
    ChrTalk(
        0xB,
        (
            "实在抱歉，\x01",
            "他应该没来过本前厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            "所有的客人\x01",
            "我都确认过，\x01",
            "应该不会弄错的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_868")

    label("loc_77C")


    #C0013
    ChrTalk(
        0x101,
        (
            "#0000F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0015
    ChrTalk(
        0xB,
        (
            "哎呀，好可爱的\x01",
            "小男孩啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "不过，他应该没有\x01",
            "来过本前厅呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#0000F是这样啊……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)

    label("loc_868")

    Jump("loc_A7C")

    label("loc_86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_944")

    #C0018
    ChrTalk(
        0xB,
        (
            "我听到游行队伍\x01",
            "通过时的音乐了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "虽然是从小就听惯了的音乐，\x01",
            "不过每次一听到，就总是……\x01",
            "忍不住兴高采烈起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xB,
        (
            "身为经理，虽然应该掩饰这种心情，\x01",
            "不过，毕竟我身上也流着\x01",
            "克洛斯贝尔市民的血呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7C")

    label("loc_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9BC")

    #C0021
    ChrTalk(
        0xB,
        (
            "今天的游行队伍\x01",
            "会从顶层豪华客房的\x01",
            "正下方经过。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        (
            "每到这个时期，\x01",
            "那里总是比其它房间\x01",
            "更早被订掉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7C")

    label("loc_9BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A11")

    #C0023
    ChrTalk(
        0xB,
        (
            "市政厅那边\x01",
            "今天好像有活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        (
            "也有出席者\x01",
            "在本酒店\x01",
            "预约了房间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7C")

    label("loc_A11")


    #C0025
    ChrTalk(
        0xB,
        (
            "从纪念庆典的第一天开始，\x01",
            "就有众多客人入住呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        (
            "对各位游客来说，\x01",
            "这条欢乐街也是\x01",
            "值得瞩目的景点呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7C")

    Jump("loc_530")

    label("loc_A81")

    TalkEnd(0xB)
    Return()

    # Function_7_3F9 end

    def Function_8_A85(): pass

    label("Function_8_A85")

    Call(0, 9)
    Return()

    # Function_8_A85 end

    def Function_9_A89(): pass

    label("Function_9_A89")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B92")

    #C0027
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎光临『千禧酒店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
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

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在酒店或酒馆里休息\x01",
            "可以回复ＣＰ。\x02",
        )
    )

    CloseMessageWindow()

    #A0030
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

    label("loc_B92")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1182")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BEC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_BEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0C")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_117D")

    label("loc_C0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C20")
    Jump("loc_117D")

    label("loc_C20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_C97")

    #C0031
    ChrTalk(
        0x8,
        (
            "到了最终日，\x01",
            "空房间也越来越多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "当天就可以直接入住，\x01",
            "还请随意吩咐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117D")

    label("loc_C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_CD8")

    #C0033
    ChrTalk(
        0x8,
        (
            "走失的孩子真令人担心呢。\x01",
            "……我也多加留意吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117D")

    label("loc_CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_E69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 5)), scpexpr(EXPR_END)), "loc_D49")

    #C0034
    ChrTalk(
        0x8,
        (
            "外面有许多游客，\x01",
            "也不确定是否见过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "唯一能确定的就是，\x01",
            "他并不是本酒店的客人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E64")

    label("loc_D49")


    #C0036
    ChrTalk(
        0x101,
        (
            "#0000F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0038
    ChrTalk(
        0x8,
        (
            "走失的孩子吗……\x01",
            "这可真令人担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "唔，不过，\x01",
            "是否见过，我就不确定了……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "因为外面的\x01",
            "游客实在是太多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)

    label("loc_E64")

    Jump("loc_117D")

    label("loc_E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_F50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_ED5")

    #C0042
    ChrTalk(
        0x8,
        (
            "在纪念庆典的最终日\x01",
            "以及翌日回国的\x01",
            "客人有很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "……衷心期待\x01",
            "他们再次光临。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F4B")

    label("loc_ED5")


    #C0044
    ChrTalk(
        0x8,
        (
            "雾香小姐似乎再待两天\x01",
            "就要回国了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "是打算在纪念庆典结束后的\x01",
            "翌日回国吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "……衷心期待\x01",
            "她的再度光临。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F4B")

    Jump("loc_117D")

    label("loc_F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_FFF")

    #C0047
    ChrTalk(
        0x8,
        (
            "有位名叫雾香的小姐\x01",
            "在本酒店入住……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "她似乎有\x01",
            "彩虹剧团的票，\x01",
            "今天去观赏剧场表演了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "她好像是演艺界人士，\x01",
            "真不愧是职业女性，\x01",
            "有种英姿飒爽的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117D")

    label("loc_FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1063")

    #C0050
    ChrTalk(
        0x8,
        (
            "本酒店凭借周到的服务\x01",
            "而闻名海外。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "有许多听说了传闻的\x01",
            "政界要人也会在此入住。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117D")

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10E9")

    #C0052
    ChrTalk(
        0x8,
        (
            "竟然误认您是\x01",
            "住宿的客人……\x01",
            "这件事请对经理保密。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "因为从昨天起\x01",
            "就有大量客人进出……\x01",
            "我的业务水平还远远不够啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117D")

    label("loc_10E9")


    #C0054
    ChrTalk(
        0x8,
        "客人，您忘了东西吗？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "……真是失礼，我竟然将您\x01",
            "误认为是住宿的客人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "因为从昨天起\x01",
            "就有大量客人进出……\x01",
            "我的业务水平还远远不够啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_117D")

    Jump("loc_B9C")

    label("loc_1182")

    TalkEnd(0x8)
    Return()

    # Function_9_A89 end

    def Function_10_1186(): pass

    label("Function_10_1186")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1200")

    #C0057
    ChrTalk(
        0xA,
        (
            "客人退房之后，\x01",
            "必须要尽快整理好房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        (
            "为了顺利迎接下一位客人，\x01",
            "我们这些员工\x01",
            "必须提高工作速度。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1439")

    label("loc_1200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_124A")

    #C0059
    ChrTalk(
        0xA,
        (
            "……唔，德莉丝似乎\x01",
            "已经重新打扫过了。\x01",
            "很不错，很不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1439")

    label("loc_124A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1357")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12D1")

    #C0060
    ChrTalk(
        0xA,
        (
            "为了让客人\x01",
            "住得舒心，\x01",
            "美好的空间是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "即使是纪念庆典也不可松懈，\x01",
            "一定要好好\x01",
            "提醒德莉丝才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1352")

    label("loc_12D1")


    #C0062
    ChrTalk(
        0xA,
        (
            "……走廊的扫除\x01",
            "似乎有点不够细致啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        (
            "为了让客人\x01",
            "住得舒心，\x01",
            "美好的空间是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        (
            "一定要好好\x01",
            "提醒德莉丝才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1352")

    Jump("loc_1439")

    label("loc_1357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_13D9")

    #C0065
    ChrTalk(
        0xA,
        (
            "手头宽裕的人们，\x01",
            "在纪念庆典期间\x01",
            "似乎住在米修拉姆的酒店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xA,
        (
            "我只是普通市民，\x01",
            "实在是效仿不了呢。\x01",
            "哈哈哈……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1439")

    label("loc_13D9")


    #C0067
    ChrTalk(
        0xA,
        (
            "豪华客房在\x01",
            "纪念庆典期间已经满员了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "这种房间平时都没有人住，\x01",
            "但一到纪念庆典就不同了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1439")

    TalkEnd(0xFE)
    Return()

    # Function_10_1186 end

    def Function_11_143D(): pass

    label("Function_11_143D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1475")

    #C0069
    ChrTalk(
        0x9,
        (
            "嗯，要补充沐浴套装，\x01",
            "还有还有……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C9")

    label("loc_1475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_14EC")

    #C0070
    ChrTalk(
        0x9,
        (
            "亚伦先生批评我\x01",
            "打扫得不仔细。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "我只好重新打扫了一遍……\x01",
            "因为忙碌就不够仔细，\x01",
            "到底还是不行的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C9")

    label("loc_14EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1548")

    #C0072
    ChrTalk(
        0x9,
        (
            "呼……感觉\x01",
            "有点疲惫了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "纪念庆典就到明天为止了，\x01",
            "必须得再加把劲……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C9")

    label("loc_1548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_15C7")

    #C0074
    ChrTalk(
        0x9,
        (
            "要把那个房间的床单\x01",
            "叠好并拿到储藏室，\x01",
            "然后整理这个房间的床铺……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "啊啊，再不赶快的话，\x01",
            "客人就要回来了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C9")

    label("loc_15C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1621")

    #C0076
    ChrTalk(
        0x9,
        (
            "这层楼的床铺已经\x01",
            "全部整理完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "有些客人还给了我小费，\x01",
            "真开心呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C9")

    label("loc_1621")


    #C0078
    ChrTalk(
        0x9,
        (
            "这层楼的床铺\x01",
            "已经全部整理完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "有些客人还按照最近流行的做法，\x01",
            "在枕头下面\x01",
            "放了小费呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "……失、失礼了。\x01",
            "我真是的，怎么能在\x01",
            "客人面前说这么丢人的话……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_16C9")

    TalkEnd(0xFE)
    Return()

    # Function_11_143D end

    def Function_12_16CD(): pass

    label("Function_12_16CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1720")

    #C0081
    ChrTalk(
        0xC,
        (
            "计划去看的彩虹剧团演出\x01",
            "也看完了，今天打算\x01",
            "和女儿悠闲地度过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_1720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_179E")

    #C0082
    ChrTalk(
        0xC,
        (
            "我和女儿去看了\x01",
            "彩虹剧团的公演。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xC,
        (
            "观赏了那场精彩的演出之后，\x01",
            "我女儿从今早开始就一直沉浸在演出的余韵中。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_179E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1821")

    #C0084
    ChrTalk(
        0xC,
        (
            "我们明天要去看\x01",
            "彩虹剧团的公演。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xC,
        (
            "我女儿好像没什么兴趣……\x01",
            "不过，只要看过一次，\x01",
            "她就一定会明白其精彩之处了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_1821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_187F")

    #C0086
    ChrTalk(
        0xC,
        (
            "彩虹剧团的舞台表演实在是太棒了。\x01",
            "真希望我女儿\x01",
            "也能体会到那种震撼的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_187F")


    #C0087
    ChrTalk(
        0xC,
        (
            "我们是趁着这次的纪念庆典\x01",
            "来观看彩虹剧团的\x01",
            "公演的。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xC,
        (
            "我以前也曾看过一次，\x01",
            "那已经是三年前的事了……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        (
            "这次他们上演了新剧目，\x01",
            "就带女儿一起来看了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_191E")

    TalkEnd(0xFE)
    Return()

    # Function_12_16CD end

    def Function_13_1922(): pass

    label("Function_13_1922")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_197B")

    #C0090
    ChrTalk(
        0xD,
        "我要和爸爸一起去逛欢乐街。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xD,
        "不知道有没有伊莉娅小姐的周边呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A6E")

    label("loc_197B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_19B9")

    #C0092
    ChrTalk(
        0xD,
        "伊莉娅大人……！\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xD,
        "啊，真是太棒了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A6E")

    label("loc_19B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A25")

    #C0094
    ChrTalk(
        0xD,
        (
            "克洛斯贝尔的欢乐街真是厉害呀，\x01",
            "到处都是玩乐的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xD,
        (
            "稍微休息一下，\x01",
            "再出去继续玩吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6E")

    label("loc_1A25")


    #C0096
    ChrTalk(
        0xD,
        "爸爸一直说精彩精彩的。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xD,
        (
            "不过是舞台表演而已吧，\x01",
            "能有那么精彩吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6E")

    TalkEnd(0xFE)
    Return()

    # Function_13_1922 end

    def Function_14_1A72(): pass

    label("Function_14_1A72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1AE5")

    #C0098
    ChrTalk(
        0xE,
        (
            "我终于回过神时……\x01",
            "不知不觉，就在『巴鲁卡』\x01",
            "花掉了相当多的米拉。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xE,
        "……那个地方太危险了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C05")

    label("loc_1AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1B47")

    #C0100
    ChrTalk(
        0xE,
        "昨天去了『巴鲁卡』。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xE,
        (
            "那种刺激感……\x01",
            "我似乎明白\x01",
            "为什么会有那么多人喜欢了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C05")

    label("loc_1B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1BA8")

    #C0102
    ChrTalk(
        0xE,
        (
            "难得来到克洛斯贝尔，\x01",
            "我想做些平时做不了的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xE,
        "『巴鲁卡』会不会很有趣呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C05")

    label("loc_1BA8")


    #C0104
    ChrTalk(
        0xE,
        (
            "能找到这么漂亮的酒店，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xE,
        (
            "东街的那种\x01",
            "破旧旅店，\x01",
            "实在是不符合我的个性嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C05")

    TalkEnd(0xFE)
    Return()

    # Function_14_1A72 end

    def Function_15_1C09(): pass

    label("Function_15_1C09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1D68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1CA4")

    #C0106
    ChrTalk(
        0xF,
        (
            "#3400F彩虹剧团的\x01",
            "共和国公演吗……\x02\x03",

            "要是能实现的话，\x01",
            "一定会大受欢迎吧。\x02\x03",

            "我已经传达过这边的意向了，\x01",
            "之后就看对方怎么回应了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D63")

    label("loc_1CA4")


    #C0107
    ChrTalk(
        0xF,
        (
            "#3400F彩虹剧团的公演\x01",
            "的确十分精彩。\x02\x03",

            "连我也都\x01",
            "看到入迷了……\x01",
            "可以这么说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#0000F哈哈哈……\x01",
            "那么，商谈的事情\x01",
            "怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xF,
        (
            "#3400F只是提了个建议而已，\x01",
            "之后就看对方怎么回应了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_1D63")

    Jump("loc_1FCC")

    label("loc_1D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1FCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 5)), scpexpr(EXPR_END)), "loc_1E29")

    #C0110
    ChrTalk(
        0xF,
        (
            "#3400F在接下来的工作方面，\x01",
            "似乎还需要\x01",
            "掌握各种信息呢。\x02\x03",

            "……但最终还是\x01",
            "要看对方怎么回应……\x02\x03",

            "不过，事先做好充分的准备\x01",
            "总是没错的。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#0000F（似乎相当认真呢……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FCC")

    label("loc_1E29")


    #C0112
    ChrTalk(
        0xF,
        "#3400F哎呀，刚才承蒙关照了。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#0000F雾香小姐……\x01",
            "原来您住在这家酒店啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        (
            "#0300F竟然住在高级酒店的套房，\x01",
            "真是厉害啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        "#0200F演艺界的职业人士果然层次不同。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xF,
        (
            "#3400F呵呵，其实酒店的级别\x01",
            "对我来说并不重要。\x02\x03",

            "只是这里的位置\x01",
            "刚好比较方便罢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        (
            "#0100F啊……因为彩虹剧团\x01",
            "就在眼前吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xF,
        (
            "#3400F嗯，而且\x01",
            "风景和视野都是最好的……\x02\x03",

            "明天的公演\x01",
            "我会好好欣赏一番的。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#0000F哈哈哈……\x01",
            "请尽情欣赏。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB7, 5)

    label("loc_1FCC")

    TalkEnd(0xFE)
    Return()

    # Function_15_1C09 end

    def Function_16_1FD0(): pass

    label("Function_16_1FD0")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_205E")
    OP_29(0x46, 0x1, 0x2)

    #C0120
    ChrTalk(
        0x101,
        (
            "#0000F（好，欢乐街的询问工作\x01",
            "  至此也就足够了吧。）\x02\x03",

            "（接下来是后巷……\x01",
            "  用同样方法，继续探听情报吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 3)

    label("loc_205E")

    Return()

    # Function_16_1FD0 end

    SaveToFile()

Try(main)
