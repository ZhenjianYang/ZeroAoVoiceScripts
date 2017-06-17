from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c047b.bin",                # FileName
        "c047b",                    # MapName
        "c047b",                    # Location
        0x0025,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c047b",                  # 0
        "多雷克老板",             # 1
        "切莉",                   # 2
        "加雷提",                 # 3
        "艾琳迪",                 # 4
        "雷特罗莎",               # 5
        "利凯爷爷",               # 6
    ))

    AddCharChip((
        "chr/ch20002.itc",                   # 00
        "chr/ch25800.itc",                   # 01
        "chr/ch25900.itc",                   # 02
        "chr/ch27000.itc",                   # 03
        "chr/ch27100.itc",                   # 04
        "chr/ch33302.itc",                   # 05
    ))

    DeclNpc(-899,    4000,    21299,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(6199,    -1000,   8000,    270,  261,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       -1000,   13649,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-6500,   -1000,   6000,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(1350,    -949,    11500,   0,    261,  0x0, 0,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(6699,    4269,    15750,   90,   261,  0x0, 0,   0,   0,   255, 255, 0,   12,  255,  0)

    DeclActor(-900,    4000,    20000,   2000,    -900,    5500,    21300,   0x007E, 0,  3,  0x0000)
    DeclActor(5240,    -1000,   8000,    1200,    6200,    500,     8000,    0x007E, 0,  5,  0x0000)
    DeclActor(-920,    -1000,   12050,   1700,    0,       500,     13650,   0x007E, 0,  7,  0x0000)
    DeclActor(-4500,   -1000,   6000,    1500,    -6500,   500,     6000,    0x007E, 0,  9,  0x0000)

    ScpFunction((
        "Function_0_218",          # 00, 0
        "Function_1_2D0",          # 01, 1
        "Function_2_2D1",          # 02, 2
        "Function_3_2FB",          # 03, 3
        "Function_4_2FF",          # 04, 4
        "Function_5_55C",          # 05, 5
        "Function_6_560",          # 06, 6
        "Function_7_6F8",          # 07, 7
        "Function_8_6FC",          # 08, 8
        "Function_9_7E2",          # 09, 9
        "Function_10_7E6",         # 0A, 10
        "Function_11_83F",         # 0B, 11
        "Function_12_A09",         # 0C, 12
    ))


    def Function_0_218(): pass

    label("Function_0_218")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_258"),
        (1, "loc_264"),
        (2, "loc_270"),
        (3, "loc_27C"),
        (4, "loc_288"),
        (5, "loc_294"),
        (6, "loc_2A0"),
        (SWITCH_DEFAULT, "loc_2AC"),
    )


    label("loc_258")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_264")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_270")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_27C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_288")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_294")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_2A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_2AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_2B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_2CF")

    Return()

    # Function_0_218 end

    def Function_1_2D0(): pass

    label("Function_1_2D0")

    Return()

    # Function_1_2D0 end

    def Function_2_2D1(): pass

    label("Function_2_2D1")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -6000, -1000, 16000, 5000, 5000, 0)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    Return()

    # Function_2_2D1 end

    def Function_3_2FB(): pass

    label("Function_3_2FB")

    Call(0, 4)
    Return()

    # Function_3_2FB end

    def Function_4_2FF(): pass

    label("Function_4_2FF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_395")

    #C0001
    ChrTalk(
        0x8,
        (
            "你们和冈兹先生说过话了吧……\x01",
            "他的直觉确实变得敏锐异常呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "真是的……他到底是在什么地方，\x01",
            "接受了怎样的直觉训练啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D0")

    label("loc_395")


    #C0003
    ChrTalk(
        0x8,
        (
            "呀，各位，情况如何啊？\x01",
            "见到了冈兹先生了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0003F唔，算是吧……\x01",
            "虽然觉得和预想中的不太一样，但总算是见到了。\x02\x03",

            "#0000F多谢您的帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#0301F话说回来，最让人费解的\x01",
            "还是他那惊人的能力。\x02\x03",

            "#0306F为什么我就\x01",
            "得不到那种能力啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        "#0106F呼，你还在纠结这个问题啊。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x103,
        "#0211F……………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_4D0")

    Jump("loc_558")

    label("loc_4D5")


    #C0008
    ChrTalk(
        0x8,
        (
            "冈兹先生是我们这里的常客哦。\x01",
            "不会搞错的。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "他现在应该暂时住在\x01",
            "千禧酒店顶层的\x01",
            "豪华客房中。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "有事的话，就去那里找他吧。\x02",
    )

    CloseMessageWindow()

    label("loc_558")

    TalkEnd(0x8)
    Return()

    # Function_4_2FF end

    def Function_5_55C(): pass

    label("Function_5_55C")

    Call(0, 6)
    Return()

    # Function_5_55C end

    def Function_6_560(): pass

    label("Function_6_560")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "兑换\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BD")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F0")
    SetScenarioFlags(0x6D, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5DF")
    OP_AF(0x3F)
    Jump("loc_5E1")

    label("loc_5DF")

    OP_AF(0x3E)

    label("loc_5E1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EF")

    label("loc_5F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_604")
    Jump("loc_6EF")

    label("loc_604")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_670")

    #C0011
    ChrTalk(
        0x9,
        (
            "冈兹先生\x01",
            "最近运势当头呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x9,
        "跟以前比起来，简直就是判若两人～\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EF")

    label("loc_670")


    #C0013
    ChrTalk(
        0x9,
        (
            "说起来，冈兹先生\x01",
            "最近样子有些奇怪呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "态度变得特别嚣张蛮横～\x01",
            "而且不断取胜～\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        "和以前相比，简直就像是变了个人。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_6EF")

    Jump("loc_56D")

    label("loc_6F4")

    TalkEnd(0x9)
    Return()

    # Function_6_560 end

    def Function_7_6F8(): pass

    label("Function_7_6F8")

    Call(0, 8)
    Return()

    # Function_7_6F8 end

    def Function_8_6FC(): pass

    label("Function_8_6FC")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_752")

    #C0016
    ChrTalk(
        0xA,
        (
            "以前玩牌的时候，他很少能获胜，\x01",
            "最近为什么会有这么好的运气呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DE")

    label("loc_752")


    #C0017
    ChrTalk(
        0xA,
        (
            "每次和冈兹先生较量，\x01",
            "他总是能抽到上等好牌。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "不过，可以确定的是，\x01",
            "他并没有耍诈……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xA,
        (
            "他的手气为什么会如此好，\x01",
            "实在是想不通。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_7DE")

    TalkEnd(0xA)
    Return()

    # Function_8_6FC end

    def Function_9_7E2(): pass

    label("Function_9_7E2")

    Call(0, 10)
    Return()

    # Function_9_7E2 end

    def Function_10_7E6(): pass

    label("Function_10_7E6")

    TalkBegin(0xB)

    #C0020
    ChrTalk(
        0xB,
        (
            "冈兹先生的运气和直觉\x01",
            "都不同寻常啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xB,
        (
            "我也第一次尝到了\x01",
            "连续败北的滋味。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_10_7E6 end

    def Function_11_83F(): pass

    label("Function_11_83F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D3")
    Jump("loc_91D")

    label("loc_8D3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8F3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91D")

    label("loc_8F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_913")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91D")

    label("loc_913")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_91D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_999")

    #C0022
    ChrTalk(
        0xC,
        "我也曾和他对阵过一次呢。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xC,
        (
            "但是他根本就不像是\x01",
            "技巧平庸的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A01")

    label("loc_999")


    #C0024
    ChrTalk(
        0xC,
        (
            "听说，那个叫冈兹的男人\x01",
            "原来只是个技巧\x01",
            "非常差的家伙……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xC,
        (
            "这是真的吗，\x01",
            "实在是让人无法想象啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_A01")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_83F end

    def Function_12_A09(): pass

    label("Function_12_A09")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A9D")
    Jump("loc_AE7")

    label("loc_A9D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ABD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AE7")

    label("loc_ABD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AE7")

    label("loc_ADD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AE7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0026
    ChrTalk(
        0xD,
        (
            "唔……玩得正在兴头上，\x01",
            "结果天这么快就黑了……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xD,
        (
            "讨厌，我还不想回去，\x01",
            "现在的状态超好呢！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_A09 end

    SaveToFile()

Try(main)
