from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c021b.bin",                # FileName
        "c021b",                    # MapName
        "c021b",                    # Location
        0x000B,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c021b",                  # 0
        "奥斯卡",                 # 1
        "摩尔吉",                 # 2
        "贝奈特",                 # 3
        "塔利兹",                 # 4
        "爱尔莎",                 # 5
        "小桃",                   # 6
    ))

    AddCharChip((
        "chr/ch07000.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch34300.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch24800.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch20700.itc",                   # 08
    ))

    DeclNpc(56290,   0,       2019,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(119120,  0,       -660,    275,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(51279,   1000,    12869,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(200,     0,       8500,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(54900,   0,       1720,    1000,    56290,   1500,    2020,    0x007E, 0,  4,  0x0000)
    DeclActor(300,     0,       6960,    1000,    200,     1500,    8500,    0x007E, 0,  9,  0x0000)
    DeclActor(-72380,  0,       8250,    1200,    -72380,  2450,    8250,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(516, 0)                                        # 0

    ScpFunction((
        "Function_0_204",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_2F0",          # 02, 2
        "Function_3_2F1",          # 03, 3
        "Function_4_398",          # 04, 4
        "Function_5_39C",          # 05, 5
        "Function_6_452",          # 06, 6
        "Function_7_5F0",          # 07, 7
        "Function_8_670",          # 08, 8
        "Function_9_6D1",          # 09, 9
        "Function_10_6D5",         # 0A, 10
        "Function_11_7CD",         # 0B, 11
        "Function_12_809",         # 0C, 12
        "Function_13_8BA",         # 0D, 13
    ))


    def Function_0_204(): pass

    label("Function_0_204")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_23C"),
        (1, "loc_248"),
        (2, "loc_254"),
        (3, "loc_260"),
        (4, "loc_26C"),
        (5, "loc_278"),
        (6, "loc_284"),
        (SWITCH_DEFAULT, "loc_290"),
    )


    label("loc_23C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_248")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_254")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_260")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_26C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_278")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_284")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_290")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_29C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_2B3")

    Return()

    # Function_0_204 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    SetChrFlags(0xA, 0x10)
    SetChrPos(0xC, -68850, 0, -980, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9")
    SetChrFlags(0xC, 0x10)

    label("loc_2D9")

    SetChrPos(0xD, -68700, 0, 340, 180)
    SetChrFlags(0xD, 0x10)
    Return()

    # Function_1_2B4 end

    def Function_2_2F0(): pass

    label("Function_2_2F0")

    Return()

    # Function_2_2F0 end

    def Function_3_2F1(): pass

    label("Function_3_2F1")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着《点心王国　第一卷》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_394")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_394")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『混合冰激凌』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_394")

    TalkEnd(0xFF)
    Return()

    # Function_3_2F1 end

    def Function_4_398(): pass

    label("Function_4_398")

    Call(0, 5)
    Return()

    # Function_4_398 end

    def Function_5_39C(): pass

    label("Function_5_39C")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_419")
    OP_AF(0xC9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_449")

    label("loc_419")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42D")
    Jump("loc_449")

    label("loc_42D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_449")

    Jump("loc_3A9")

    label("loc_44E")

    TalkEnd(0x8)
    Return()

    # Function_5_39C end

    def Function_6_452(): pass

    label("Function_6_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58B")

    #C0003
    ChrTalk(
        0x8,
        (
            "都这么晚了，\x01",
            "你们还在外面走动，\x01",
            "实在是少见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "其实都已经过了\x01",
            "关店时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "不过算啦，既然是你们，凡事都好商量。\x01",
            "请不必客气，随便挑选吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00000F谢啦，奥斯卡，\x01",
            "那我们就来挑一些……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x10A,
        "#00603F…………………………\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00006F（如、如果要买面包，\x01",
            "  动作还是迅速一些为好啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5EF")

    label("loc_58B")


    #C0009
    ChrTalk(
        0x8,
        (
            "其实都已经过了\x01",
            "关店时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "不过算啦，既然是你们，凡事都好商量。\x01",
            "请不必客气，随便挑选吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EF")

    Return()

    # Function_6_452 end

    def Function_7_5F0(): pass

    label("Function_7_5F0")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xFE,
        (
            "好，差不多也该开始\x01",
            "整理收拾一下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "面包店的准备工作\x01",
            "从凌晨三点就开始了。\x01",
            "为了准备明天的工作，必须得早点休息。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_5F0 end

    def Function_8_670(): pass

    label("Function_8_670")

    TalkBegin(0xFE)

    #C0013
    ChrTalk(
        0xFE,
        (
            "我做的面包……\x01",
            "销售额竟然输给了\x01",
            "奥斯卡做的面包……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "唔唔唔，明天一定要……！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_670 end

    def Function_9_6D1(): pass

    label("Function_9_6D1")

    Call(0, 10)
    Return()

    # Function_9_6D1 end

    def Function_10_6D5(): pass

    label("Function_10_6D5")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C9")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_732")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_732")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    OP_AF(0x29)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7C4")

    label("loc_752")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_766")
    Jump("loc_7C4")

    label("loc_766")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0015
    ChrTalk(
        0xB,
        (
            "欢迎，\x01",
            "有什么需要吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "距离关店还有\x01",
            "一段时间，\x01",
            "请慢慢看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C4")

    Jump("loc_6E2")

    label("loc_7C9")

    TalkEnd(0xB)
    Return()

    # Function_10_6D5 end

    def Function_11_7CD(): pass

    label("Function_11_7CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E2")
    Call(0, 12)
    Jump("loc_805")

    label("loc_7E2")


    #C0017
    ChrTalk(
        0xFE,
        (
            "呵呵，小桃好像\x01",
            "玩得很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_805")

    TalkEnd(0xFE)
    Return()

    # Function_11_7CD end

    def Function_12_809(): pass

    label("Function_12_809")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0018
    ChrTalk(
        0xD,
        (
            "……对了，对了，\x01",
            "隆想擅自闯进\x01",
            "兰花塔。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xD,
        (
            "结果连我和亨利\x01",
            "都被警察骂了……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xC,
        (
            "哎呀呀……\x01",
            "小桃运气真不好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xD,
        (
            "不过……\x01",
            "真是很开心呢……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_12_809 end

    def Function_13_8BA(): pass

    label("Function_13_8BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CF")
    Call(0, 12)
    Jump("loc_935")

    label("loc_8CF")


    #C0022
    ChrTalk(
        0xFE,
        (
            "隆真是很有趣啊。\x01",
            "他把所有责任\x01",
            "都推给亨利了……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "但谎话马上就被戳破，\x01",
            "被骂得更凶了。\x01",
            "嘻嘻……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_935")

    TalkEnd(0xFE)
    Return()

    # Function_13_8BA end

    SaveToFile()

Try(main)
