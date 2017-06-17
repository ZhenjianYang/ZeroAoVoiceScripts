from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r0210.bin",                # FileName
        "r0210",                    # MapName
        "r0210",                    # Location
        0x00A5,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x04,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0210",                  # 0
        "赛尔丹分部长",           # 1
        "彼德",                   # 2
        "费瑟尔",                 # 3
        "雷克罗德Ⅲ世",           # 4
        "『龙宫』辉夜",           # 5
    ))

    AddCharChip((
        "chr/ch32200.itc",                   # 00
        "chr/ch24200.itc",                   # 01
        "chr/ch46100.itc",                   # 02
        "chr/ch45600.itc",                   # 03
        "chr/ch45800.itc",                   # 04
    ))

    DeclNpc(-389,    0,       -1149,   188,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(1080,    0,       -1110,   270,  389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(6010,    0,       -8220,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(529,     0,       -1149,   270,  389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-449,    0,       -1190,   90,   389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(1510,    0,       3420,    1200,    1510,    750,     3420,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(384, 0)                                        # 0

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_230",          # 01, 1
        "Function_2_39C",          # 02, 2
        "Function_3_3E7",          # 03, 3
        "Function_4_490",          # 04, 4
        "Function_5_1462",         # 05, 5
        "Function_6_1912",         # 06, 6
        "Function_7_19AF",         # 07, 7
        "Function_8_1ACA",         # 08, 8
        "Function_9_216A",         # 09, 9
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
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

    # Function_0_180 end

    def Function_1_230(): pass

    label("Function_1_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_243")
    SetChrFlags(0x8, 0x80)
    Jump("loc_39B")

    label("loc_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_274")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_26A")

    SetChrFlags(0x8, 0x80)
    Jump("loc_39B")

    label("loc_274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_287")
    SetChrFlags(0x8, 0x80)
    Jump("loc_39B")

    label("loc_287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2B6")
    SetChrPos(0xA, 1080, 0, -1110, 270)
    ClearChrFlags(0xA, 0x80)
    TurnDirection(0x8, 0xA, 0)

    label("loc_2B6")

    Jump("loc_39B")

    label("loc_2BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2C9")
    Jump("loc_39B")

    label("loc_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_308")
    SetChrPos(0x8, -390, 0, -1150, 90)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x9, 1080, 0, -1110, 270)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_39B")

    label("loc_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_316")
    Jump("loc_39B")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_324")
    Jump("loc_39B")

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_341")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C")
    SetChrFlags(0x8, 0x80)

    label("loc_33C")

    Jump("loc_39B")

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34F")
    Jump("loc_39B")

    label("loc_34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_35D")
    Jump("loc_39B")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_37A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_375")
    SetChrFlags(0x8, 0x80)

    label("loc_375")

    Jump("loc_39B")

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_38D")
    SetChrFlags(0x8, 0x80)
    Jump("loc_39B")

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_39B")
    SetChrFlags(0x8, 0x80)

    label("loc_39B")

    Return()

    # Function_1_230 end

    def Function_2_39C(): pass

    label("Function_2_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_3AE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E6")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_3E6")

    Return()

    # Function_2_39C end

    def Function_3_3E7(): pass

    label("Function_3_3E7")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着《点心王国　第二卷》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_48C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x12)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『溜滑杏仁豆腐』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_48C")

    TalkEnd(0xFF)
    Return()

    # Function_3_3E7 end

    def Function_4_490(): pass

    label("Function_4_490")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81D")
    TurnDirection(0xFE, 0x101, 0)

    #C0003
    ChrTalk(
        0xFE,
        (
            "哦哦，罗伊德团员，\x01",
            "你终于露面了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#00005F赛尔丹分部长，这里是……\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "哦，这座建筑物\x01",
            "原本是租船小屋。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "自从几年前停业之后，\x01",
            "就一直废弃在这里没人管理，\x01",
            "所以我就用很便宜的价格租下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "对于从头开始的我们来说，\x01",
            "这里是最适合不过的新分部了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "对了，罗伊德团员，\x01",
            "关于我们和钓皇俱乐部之间的『爆钓比赛』，\x01",
            "我想向你做个说明……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#00005F爆、爆钓比赛……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00003F原来如此，是和钓皇俱乐部的\x01",
            "五名成员展开钓鱼比赛啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "嗯，正是。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "关于这场比赛，\x01",
            "我们本想靠自己的力量\x01",
            "设法解决……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "不过，如果可以的话，\x01",
            "希望你也能帮帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00004F好的，我也不希望\x01",
            "以后不能在自己\x01",
            "喜欢的地方钓鱼。\x02\x03",

            "#00000F一定会尽最大努力的。\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从现在开始，可以向钓皇俱乐部成员发起挑战，\x01",
            "展开『爆钓比赛』了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "关于比赛的详细规则，\x01",
            "可以向东街『钓皇俱乐部』的\x01",
            "接待小姐塞拉姆咨询。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x1C0, 0)

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_912")
    TurnDirection(0xFE, 0x101, 0)

    #C0017
    ChrTalk(
        0xFE,
        (
            "哦哦，罗伊德团员，\x01",
            "你这么快就来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "如你所见，这个地方什么都没有，\x01",
            "不过，在这里你就好好放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "对了，我们还准备了一些商品。\x01",
            "但由于材料不足，\x01",
            "所以价格有些高。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "如果有需要，不妨随意看看。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 7)

    label("loc_912")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_91C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_971")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_986")

    label("loc_971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_986")
    TurnDirection(0xFE, 0x0, 0)

    label("loc_986")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_END)), "loc_9B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9AE")
    OP_AF(0x37)
    Jump("loc_9B0")

    label("loc_9AE")

    OP_AF(0x3B)

    label("loc_9B0")

    Jump("loc_9C7")

    label("loc_9B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9C5")
    OP_AF(0x36)
    Jump("loc_9C7")

    label("loc_9C5")

    OP_AF(0x3A)

    label("loc_9C7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E6")
    TurnDirection(0xFE, 0x9, 0)

    label("loc_9E6")

    Jump("loc_1459")

    label("loc_9EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1459")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A95")
    TurnDirection(0xFE, 0x101, 0)

    #C0021
    ChrTalk(
        0xFE,
        (
            "罗伊德团员，希望你也帮帮忙，\x01",
            "与钓皇俱乐部的人进行爆钓比赛。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "不管怎么说，毕竟这场比赛\x01",
            "直接关系到钓公师团的未来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1459")

    label("loc_A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_AA3")
    Jump("loc_1459")

    label("loc_AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_EC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_B38")
    TurnDirection(0xFE, 0x101, 0)

    #C0023
    ChrTalk(
        0xFE,
        (
            "唔，罗伊德大师，\x01",
            "我们对你的感激之情真是无以言表啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "希望你今后能继续\x01",
            "保持这种状态，\x01",
            "为我们创造出更多的传说。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBB")

    label("loc_B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B9F")

    #C0025
    ChrTalk(
        0xFE,
        (
            "唔，再等一阵子，\x01",
            "那位先生就会来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        "等到那时，一定可以……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_EBB")

    label("loc_B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4D")
    TurnDirection(0xFE, 0x101, 0)

    #C0027
    ChrTalk(
        0xFE,
        (
            "罗伊德团员，那些奖牌是……\x01",
            "难道说……你把四天王全都打败了？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#00000F是的……总算成功了。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "哈哈，真不愧是罗伊德团员！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "唔，既然如此，我就可以把\x01",
            "这个东西安心交托给你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "请收下我们的\x01",
            "『灵魂』吧！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0032
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '虹丸ＥＸ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('虹丸ＥＸ', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0033
    ChrTalk(
        0x101,
        "#00005F这、这是……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "这是我们为了与钓皇俱乐部对抗，\x01",
            "呕心沥血开发出来的\x01",
            "终极钓饵。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "因为原材料是耀晶片，所以价格比较高……\x01",
            "但只要你需要，想要多少都可以。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00004F原来如此……也就是说，\x01",
            "这是大家血汗的结晶呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "嗯，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "罗伊德团员……\x01",
            "请你用它来灭掉\x01",
            "那个雷克罗德的威风吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "罗伊德团员，\x01",
            "你一定能做到的！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00001F好、好的……我会努力的！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 5)
    Jump("loc_EBB")

    label("loc_E4D")

    TurnDirection(0xFE, 0x101, 0)

    #C0041
    ChrTalk(
        0xFE,
        (
            "罗伊德团员……\x01",
            "请你带着我们的心愿，\x01",
            "灭掉那个雷克罗德的威风吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "罗伊德团员，\x01",
            "你一定能做到的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EBB")

    Jump("loc_1459")

    label("loc_EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_ECE")
    Jump("loc_1459")

    label("loc_ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F05")

    #C0043
    ChrTalk(
        0xFE,
        (
            "唔～话说回来，\x01",
            "真不愧是终极武器啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1459")

    label("loc_F05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F13")
    Jump("loc_1459")

    label("loc_F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1029")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB0")

    #C0044
    ChrTalk(
        0xFE,
        "可恶，这已经是第几次了！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "『银螭』特里同……\x01",
            "真是个可怕的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "不愧是四天王之首，果然不能\x01",
            "把他和其他人相提并论。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1024")

    label("loc_FB0")


    #C0047
    ChrTalk(
        0xFE,
        (
            "『银螭』特里同……\x01",
            "真是个可怕的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "在那种地方钓鱼，竟然都能那么轻松……\x01",
            "难道他能看到水面下的情况吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1024")

    Jump("loc_1459")

    label("loc_1029")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_109B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1041")
    Jump("loc_1096")

    label("loc_1041")

    TurnDirection(0xFE, 0x101, 0)

    #C0049
    ChrTalk(
        0xFE,
        (
            "罗伊德团员，\x01",
            "今天真的谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "托你的福，\x01",
            "今晚似乎可以睡个好觉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1096")

    Jump("loc_1459")

    label("loc_109B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1230")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A6")
    TurnDirection(0xFE, 0x101, 0)

    #C0051
    ChrTalk(
        0xFE,
        "罗伊德团员，你知道吗？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "战胜钓皇俱乐部的成员之后，\x01",
            "好像可以得到\x01",
            "一些古怪的称号。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "顺便一提，我昨天已经\x01",
            "击败了那个叫纳西斯的家伙，\x01",
            "于是得到了『水狂猎手』这个称号。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "哈哈，虽然是敌人想出的主意，\x01",
            "不过还真是挺有趣的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_122B")

    label("loc_11A6")


    #C0055
    ChrTalk(
        0xFE,
        (
            "我昨天已经击败了\x01",
            "那个叫纳西斯的家伙，\x01",
            "于是得到了『水狂猎手』这个称号。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "哈哈，虽然是敌人想出的主意，\x01",
            "不过还真是挺有趣的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_122B")

    Jump("loc_1459")

    label("loc_1230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_13C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132C")

    #C0057
    ChrTalk(
        0xFE,
        (
            "话说回来，怀着这样的心情，\x01",
            "全身心投入钓鱼……\x01",
            "好像已经很久没有过这种体验了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "在年轻的时候，\x01",
            "我曾以钓具为赌注，\x01",
            "莽撞地向别人提出爆钓比赛……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "该怎么说呢，虽然现在的情况很麻烦，\x01",
            "但也让我有种难以形容的兴奋感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13C3")

    label("loc_132C")


    #C0060
    ChrTalk(
        0xFE,
        (
            "嗯，怀着这样的心情，\x01",
            "全身心投入钓鱼……\x01",
            "好像已经很久没有过这种体验了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "该怎么说呢，虽然现在的情况很麻烦，\x01",
            "但也让我有种难以形容的兴奋感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C3")

    Jump("loc_1459")

    label("loc_13C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1442")
    TurnDirection(0xFE, 0x101, 0)

    #C0062
    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "钓公师团·克洛斯贝尔分部\x01",
            "就要从这里重新开始了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "罗伊德团员，我们\x01",
            "一起加油吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1459")

    label("loc_1442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1450")
    Jump("loc_1459")

    label("loc_1450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1459")

    label("loc_1459")

    Jump("loc_91C")

    label("loc_145E")

    TalkEnd(0xFE)
    Return()

    # Function_4_490 end

    def Function_5_1462(): pass

    label("Function_5_1462")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17A4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('绀碧竿', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥珀轴', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翡翠线', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('红莲钩', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1496")
    Jump("loc_17A4")

    label("loc_1496")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('绀碧竿', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥珀轴', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翡翠线', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('红莲钩', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17A4")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 500)

    #C0064
    ChrTalk(
        0xFE,
        "罗伊德，这是……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00003F嗯，我想应该\x01",
            "是钓具的部件，\x01",
            "还真是漂亮呢。\x02\x03",

            "#00000F我在从四天王手中夺回的垂钓场所\x01",
            "钓到了很罕见的鱼……\x01",
            "这就是那条鱼吐出来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        "……不会有错的。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "这就是过去某位飘泊的钓鱼大师\x01",
            "所使用过的传说钓具的部件。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "听说他在离开克洛斯贝尔的时候，\x01",
            "将这套钓具\x01",
            "封存在了这片土地上……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "没想到……竟然会以\x01",
            "这样的形式再现于世！\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00005F是、是那么\x01",
            "珍贵的东西吗……\x02\x03",

            "#00003F那该怎么办呢？\x01",
            "还是交还给那个人为好吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "不，没有那个必要。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……因为他曾经说过，\x01",
            "这套钓具就送给找到它的人使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "罗伊德，\x01",
            "这套钓具的部件共有四个。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "如果你获得了所有部件，\x01",
            "请务必拿到我这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "我应该可以把这些部件\x01",
            "重新组合起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00005F原、原来如此……\x01",
            "明白了，我会留心的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x8, 0)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x1C0, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_17A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_181A")
    TurnDirection(0xFE, 0x101, 0)

    #C0077
    ChrTalk(
        0xFE,
        (
            "已被封存多年的传说钓具\x01",
            "居然会在这种时候出现……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "唔，罗伊德，\x01",
            "也许这就是命运吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x8, 0)
    Jump("loc_190E")

    label("loc_181A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1828")
    Jump("loc_190E")

    label("loc_1828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1836")
    Jump("loc_190E")

    label("loc_1836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1844")
    Jump("loc_190E")

    label("loc_1844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_18A3")

    #C0079
    ChrTalk(
        0xFE,
        (
            "克潘好像\x01",
            "也在比赛中\x01",
            "碰壁了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "单靠我们的力量，\x01",
            "恐怕已经无能为力了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190E")

    label("loc_18A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_18B1")
    Jump("loc_190E")

    label("loc_18B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_18BF")
    Jump("loc_190E")

    label("loc_18BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_18CD")
    Jump("loc_190E")

    label("loc_18CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_18DB")
    Jump("loc_190E")

    label("loc_18DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_18E9")
    Jump("loc_190E")

    label("loc_18E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_18F7")
    Jump("loc_190E")

    label("loc_18F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1905")
    Jump("loc_190E")

    label("loc_1905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_190E")

    label("loc_190E")

    TalkEnd(0xFE)
    Return()

    # Function_5_1462 end

    def Function_6_1912(): pass

    label("Function_6_1912")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1923")
    Jump("loc_19AB")

    label("loc_1923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_19AB")
    TurnDirection(0xFE, 0x101, 0)

    #N0081
    NpcTalk(
        0xFE,
        "费瑟尔团长",
        (
            "罗伊德大师，你是\x01",
            "我们钓公师团的骄傲。\x02",
        )
    )

    CloseMessageWindow()

    #N0082
    NpcTalk(
        0xFE,
        "费瑟尔团长",
        (
            "如果以后有机会，真希望能在\x01",
            "利贝尔和你一起钓鱼啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19AB")

    TalkEnd(0xFE)
    Return()

    # Function_6_1912 end

    def Function_7_19AF(): pass

    label("Function_7_19AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19CC")
    Call(0, 8)
    TalkEnd(0xFE)
    Return()

    label("loc_19CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A43")

    #C0083
    ChrTalk(
        0xB,
        (
            "我们不但懂得野外生存技能，\x01",
            "而且还有艾尼格玛。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xB,
        (
            "不需要你们担心，\x01",
            "如果听明白了，就赶快走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6")

    label("loc_1A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A51")
    Jump("loc_1AC6")

    label("loc_1A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1AAF")

    #C0085
    ChrTalk(
        0xB,
        (
            "唔，话说回来，\x01",
            "独立无效宣言啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xB,
        (
            "如此一来，情况越来越\x01",
            "跌宕起伏了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6")

    label("loc_1AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1ABD")
    Jump("loc_1AC6")

    label("loc_1ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1AC6")

    label("loc_1AC6")

    TalkEnd(0xFE)
    Return()

    # Function_7_19AF end

    def Function_8_1ACA(): pass

    label("Function_8_1ACA")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B84")

    #C0087
    ChrTalk(
        0xB,
        (
            "『大陆诸国联盟』的提案，\x01",
            "以及祖国埃雷波尼亚的内战……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xB,
        (
            "在这短短的一个月中，\x01",
            "世间竟然发生了如此大的变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        (
            "是的……所谓晴天霹雳，\x01",
            "就是指这样的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5C")

    label("loc_1B84")


    #C0090
    ChrTalk(
        0xB,
        (
            "『大陆诸国联盟』的提案，\x01",
            "以及祖国埃雷波尼亚的内战……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xB,
        (
            "在这短短的一个月中，\x01",
            "世间竟然发生了如此大的变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xB,
        (
            "……而且，事到如今，\x01",
            "竟然还出现了独立无效宣言。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xC,
        (
            "是的……所谓晴天霹雳，\x01",
            "就是指这样的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5C")

    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 500)
    Sleep(500)
    TurnDirection(0xC, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D12")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不做变更】\x01",      # 0
            "【已战胜】\x01",        # 1
            "【未战胜】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D00")
    SetScenarioFlags(0x191, 1)
    Jump("loc_1D12")

    label("loc_1D00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D12")
    ClearScenarioFlags(0x191, 1)

    label("loc_1D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_1D4D")

    #C0094
    ChrTalk(
        0xB,
        (
            "哦，这不是钓公师团的\x01",
            "罗伊德·班宁斯吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D76")

    label("loc_1D4D")


    #C0095
    ChrTalk(
        0xB,
        (
            "唔，是钓公师团的\x01",
            "罗伊德·班宁斯啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D76")


    #C0096
    ChrTalk(
        0x101,
        (
            "#00005F您是钓皇俱乐部的\x01",
            "雷克罗德先生……\x01",
            "您为何会在这里？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xB,
        (
            "哼，没什么，只是为了\x01",
            "修炼垂钓技术而来此罢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xB,
        (
            "再怎么说，我也是俱乐部的部长……\x01",
            "在输掉比赛的情况下，\x01",
            "总不能厚着脸皮，就这么回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00006F原、原来如此……\x02\x03",

            "#00001F可是，您也不能\x01",
            "一直待在这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        (
            "#00200F是啊，我们可以把您\x01",
            "护送到阿尔摩利卡村，\x01",
            "请您先做好避难的准备……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xC,
        (
            "哼，你们能不能\x01",
            "别管我们？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xC,
        (
            "身为钓师，我们早已\x01",
            "习惯了户外的危险，\x01",
            "不用担心我们会饿死。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        (
            "是啊，而且要说危险的话，\x01",
            "我觉得在哪里都是一样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#00005F可、可是……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        (
            "总而言之，我们还有艾尼格玛，\x01",
            "老实说，你的担心完全是多余的。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xB,
        "如果听明白了，就赶快走吧。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        "#00006F好、好的……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2143")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0108
    ChrTalk(
        0xB,
        (
            "哦……对了，你难得过来一趟，\x01",
            "就带些礼物走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "鱼钓得有点多了，\x01",
            "我们也吃不完。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0110
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '鲤鱼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了１０条。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('鲤鱼', 10)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0111
    ChrTalk(
        0xB,
        (
            "还有，这个是\x01",
            "鱼吐出来的东西。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0112
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '还魂粉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('还魂粉', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0113
    ChrTalk(
        0x101,
        "#00005F非、非常感谢。\x02",
    )

    CloseMessageWindow()

    label("loc_2143")

    SetScenarioFlags(0x1BD, 2)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)
    Return()

    # Function_8_1ACA end

    def Function_9_216A(): pass

    label("Function_9_216A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2187")
    Call(0, 8)
    TalkEnd(0xFE)
    Return()

    label("loc_2187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21DF")

    #C0114
    ChrTalk(
        0xC,
        "……话已经说完了？\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        (
            "我们还有很多事情要忙，\x01",
            "请不要打扰我们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2287")

    label("loc_21DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21ED")
    Jump("loc_2287")

    label("loc_21ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2270")

    #C0116
    ChrTalk(
        0xC,
        (
            "我已经下定了决心，\x01",
            "不管遇到什么困难，\x01",
            "都要和雷克罗德先生共同渡过难关。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xC,
        (
            "其实，我更希望\x01",
            "我们两人就这样……⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2287")

    label("loc_2270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_227E")
    Jump("loc_2287")

    label("loc_227E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2287")

    label("loc_2287")

    TalkEnd(0xFE)
    Return()

    # Function_9_216A end

    SaveToFile()

Try(main)
