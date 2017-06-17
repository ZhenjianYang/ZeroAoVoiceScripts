from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c131b.bin",                # FileName
        "c131b",                    # MapName
        "c131b",                    # Location
        0x001C,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 28, 0, 1, 0, 3],
    )

    BuildStringList((
        "c131b",                  # 0
        "接待小姐兰菲",           # 1
        "警备员比尔斯",           # 2
        "接待小姐柯琳娜",         # 3
        "蔡特",                   # 4
        "兰迪",                   # 5
        "基约姆师傅",             # 6
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch27900.itc",                   # 01
        "chr/ch30500.itc",                   # 02
        "chr/ch02708.itc",                   # 03
        "chr/ch00302.itc",                   # 04
        "chr/ch26400.itc",                   # 05
        "chr/ch02702.itc",                   # 06
    ))

    DeclNpc(0,       300,     31700,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(1190,    300,     4789,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(7110,    300,     32759,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-7300,   0,       23299,   180,  277,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-5710,   0,       23809,   180,  277,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(7150,    0,       20149,   270,  261,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)

    DeclEvent(0x0000, 0, 15,  9.5,                   16.0,                  -0.5,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -4.75,                 -5.333333492279053,    0.10000000894069672,   1.0])

    DeclActor(0,       300,     30300,   1500,    0,       1800,    31700,   0x007E, 0,  6,  0x0000)
    DeclActor(6650,    300,     31080,   1500,    7110,    1800,    32759,   0x007E, 0,  8,  0x0000)
    DeclActor(7670,    0,       13360,   1500,    7670,    1400,    13360,   0x007C, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_264",          # 00, 0
        "Function_1_31C",          # 01, 1
        "Function_2_3E4",          # 02, 2
        "Function_3_3EB",          # 03, 3
        "Function_4_463",          # 04, 4
        "Function_5_556",          # 05, 5
        "Function_6_6E0",          # 06, 6
        "Function_7_6E4",          # 07, 7
        "Function_8_9EA",          # 08, 8
        "Function_9_9EE",          # 09, 9
        "Function_10_D4E",         # 0A, 10
        "Function_11_E6C",         # 0B, 11
        "Function_12_141C",        # 0C, 12
        "Function_13_25FD",        # 0D, 13
        "Function_14_2AB0",        # 0E, 14
        "Function_15_2B25",        # 0F, 15
    ))


    def Function_0_264(): pass

    label("Function_0_264")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2A4"),
        (1, "loc_2B0"),
        (2, "loc_2BC"),
        (3, "loc_2C8"),
        (4, "loc_2D4"),
        (5, "loc_2E0"),
        (6, "loc_2EC"),
        (SWITCH_DEFAULT, "loc_2F8"),
    )


    label("loc_2A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_31B")

    Return()

    # Function_0_264 end

    def Function_1_31C(): pass

    label("Function_1_31C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_378")
    ClearScenarioFlags(0x5F, 1)
    SetChrPos(0x0, 7670, 0, 16000, 270)
    SetChrPos(0x1, 7670, 0, 16000, 270)
    SetChrPos(0x2, 7670, 0, 16000, 270)
    SetChrPos(0x3, 7670, 0, 16000, 270)
    Event(0, 2)

    label("loc_378")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_391")
    SetChrFlags(0xC, 0x80)

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_3D2")
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xB, -1330, 300, 17250, 135)
    SetChrPos(0xD, 1180, 300, 11650, 270)
    SetChrPos(0x9, -1440, 300, 5330, 180)

    label("loc_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_3E3")
    SetChrChipByIndex(0xB, 0x6)
    SetChrSubChip(0xB, 0x0)

    label("loc_3E3")

    Return()

    # Function_1_31C end

    def Function_2_3E4(): pass

    label("Function_2_3E4")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_3E4 end

    def Function_3_3EB(): pass

    label("Function_3_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B")
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_431")

    label("loc_41B")

    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_431")

    OP_1B(0x0, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44E")
    OP_1B(0x0, 0x0, 0xE)

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_462")
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x0, 0x10)

    label("loc_462")

    Return()

    # Function_3_3EB end

    def Function_4_463(): pass

    label("Function_4_463")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_538")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x1, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x1, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_538")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_554")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_554")

    Return()

    # Function_4_463 end

    def Function_5_556(): pass

    label("Function_5_556")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_5F4")

    #C0002
    ChrTalk(
        0xFE,
        (
            "门前的那些家伙\x01",
            "安置了导力炸弹一类的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "你们将其击退之后，\x01",
            "就由我们来负责拆除炸弹！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "……一定要十分小心啊，\x01",
            "愿女神保佑你们！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC")

    label("loc_5F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C")

    #C0005
    ChrTalk(
        0xFE,
        "你们来的这一路似乎也历经磨难呢……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "这里就交给我们\x01",
            "保安人员好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "只要待在ＩＢＣ里，就保证绝对\x01",
            "没人能碰你们一根手指头！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6DC")

    label("loc_68C")


    #C0008
    ChrTalk(
        0xFE,
        (
            "外面有保安人员在，\x01",
            "已经做好万全的警备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "不用担心，\x01",
            "这里就交给我们！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DC")

    TalkEnd(0xFE)
    Return()

    # Function_5_556 end

    def Function_6_6E0(): pass

    label("Function_6_6E0")

    Call(0, 7)
    Return()

    # Function_6_6E0 end

    def Function_7_6E4(): pass

    label("Function_7_6E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81D")
    TalkBegin(0x8)

    #C0010
    ChrTalk(
        0x8,
        (
            "是罗伊德警官啊……\x01",
            "事情的全部经过都听总裁说过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "今天真是发生了\x01",
            "不得了的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#0006F实在抱歉，\x01",
            "把这里的人们也卷进来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "不不，请不必\x01",
            "在意我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "而且，对库罗伊斯总裁来说，\x01",
            "面对如此事态，肯定\x01",
            "也是无法置之不理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "总之，就请让我们\x01",
            "也进行协助吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Jump("loc_9E9")

    label("loc_81D")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_82A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E6")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                # 0
            "购物（装备）\x01",        # 1
            "购物（消耗品）\x01",      # 2
            "放弃\x01",                # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_89B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_89B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BB")
    OP_AF(0xB8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E1")

    label("loc_8BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DB")
    OP_AF(0xB9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E1")

    label("loc_8DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8EF")
    Jump("loc_9E1")

    label("loc_8EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_96A")

    #C0016
    ChrTalk(
        0x8,
        (
            "没想到事态竟然会\x01",
            "演变至此啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "各位，请一定要小心啊，\x01",
            "祈祷你们旗开得胜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E1")

    label("loc_96A")


    #C0018
    ChrTalk(
        0x8,
        (
            "对库罗伊斯总裁来说，\x01",
            "面对如此事态，肯定\x01",
            "也是无法置之不理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "总之，请让我们这些职员\x01",
            "也尽己所能地协助各位吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E1")

    Jump("loc_82A")

    label("loc_9E6")

    TalkEnd(0x8)

    label("loc_9E9")

    Return()

    # Function_7_6E4 end

    def Function_8_9EA(): pass

    label("Function_8_9EA")

    Call(0, 9)
    Return()

    # Function_8_9EA end

    def Function_9_9EE(): pass

    label("Function_9_9EE")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B35")

    #C0020
    ChrTalk(
        0xA,
        (
            "操纵警备队……这种事\x01",
            "还真是诡异至极啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        "但可以肯定一点——各位都很幸运啊。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xA,
        (
            "因为这里可是天下闻名的\x01",
            "ＩＢＣ大厦呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0002F哈哈，说得也是呢。\x02\x03",

            "#0004F（确实，能顺利藏身在\x01",
            "  ＩＢＣ大厦之内，\x01",
            "  真是非常幸运呢。）\x02\x03",

            "#0008F（……必须要趁此机会，\x01",
            "  尽可能地整理一下\x01",
            "  身上的装备。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D4A")

    label("loc_B35")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4A")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "交换（装备）\x01",      # 1
            "交换（回路）\x01",      # 2
            "交换（其它）\x01",      # 3
            "放弃\x01",              # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BBB")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_BBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDB")
    OP_AF(0xBA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D45")

    label("loc_BDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFB")
    OP_AF(0xBB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D45")

    label("loc_BFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1B")
    OP_AF(0xBC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D45")

    label("loc_C1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2F")
    Jump("loc_D45")

    label("loc_C2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D45")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_CC5")

    #C0024
    ChrTalk(
        0xA,
        (
            "竟然都攻到了\x01",
            "ＩＢＣ大厦前……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xA,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xA,
        (
            "实在抱歉，\x01",
            "我们的命运，\x01",
            "就托付给各位了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D45")

    label("loc_CC5")


    #C0027
    ChrTalk(
        0xA,
        (
            "操纵警备队……这种事\x01",
            "还真是诡异至极啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xA,
        "但可以肯定一点：各位都很幸运啊。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xA,
        (
            "因为这里可是天下闻名的\x01",
            "ＩＢＣ大厦呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D45")

    Jump("loc_B3F")

    label("loc_D4A")

    TalkEnd(0xA)
    Return()

    # Function_9_9EE end

    def Function_10_D4E(): pass

    label("Function_10_D4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_DC6")

    #C0030
    ChrTalk(
        0xB,
        "#1201F呜噜噜噜噜………！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#0002F蔡特……\x01",
            "看守大楼的工作就交给你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        "#1200F呜噜噜噜……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E68")

    label("loc_DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 4)), scpexpr(EXPR_END)), "loc_E27")

    #C0033
    ChrTalk(
        0xB,
        "#1201F呜噜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#0005F（蔡特……？\x01",
            "  它的情绪好像很激昂呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E68")

    label("loc_E27")


    #C0035
    ChrTalk(
        0xB,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#0000F蔡特……\x01",
            "这里就交给你了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E68")

    TalkEnd(0xFE)
    Return()

    # Function_10_D4E end

    def Function_11_E6C(): pass

    label("Function_11_E6C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F00")
    Jump("loc_F4A")

    label("loc_F00")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F20")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F4A")

    label("loc_F20")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F40")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F4A")

    label("loc_F40")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 4)), scpexpr(EXPR_END)), "loc_122B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A4")
    OP_4B(0xB, 0xFF)

    #C0037
    ChrTalk(
        0x101,
        "#0001F兰迪，外面的情况如何？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xC,
        (
            "#0306F嗯，现在还没有动静。\x02\x03",

            "#0301F不过，他们差不多也该\x01",
            "循着味道追过来了。\x02\x03",

            "那辆豪华的高级轿车\x01",
            "是银行老板的爱车，\x01",
            "他们肯定会注意到这点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0003F……确实。\x02\x03",

            "#0000F蔡特，不好意思，\x01",
            "这里就拜托你啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        "#1200F呜～\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xC,
        (
            "#0309F哈哈……\x01",
            "这家伙还是和以前一样嚣张呢。\x02\x03",

            "#0304F──好啦，既然都到了这一步，\x01",
            "就不得不坚定决心，做好最坏打算啦。\x02\x03",

            "#0300F如果警备队向这里发起进攻，\x01",
            "多半将会是一波接一波的连续攻击。\x02\x03",

            "到时说不定要进行连续战斗，\x01",
            "最好趁现在做好补给工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#0000F嗯，了解。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0xE4, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1226")

    label("loc_11A4")


    #C0043
    ChrTalk(
        0xC,
        (
            "#0303F如果警备队向这里发起进攻，\x01",
            "多半将会是一波接一波的连续攻击。\x02\x03",

            "#0300F到时说不定要进行连续战斗，\x01",
            "最好趁现在做好补给工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1226")

    Jump("loc_1414")

    label("loc_122B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A0")
    OP_4B(0xB, 0xFF)

    #C0044
    ChrTalk(
        0x101,
        "#0001F兰迪，外面的情况如何？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xC,
        (
            "#0304F嗯，目前还没什么问题。\x02\x03",

            "#0300F不愧是高档名车，速度好快，\x01",
            "已经把那些家伙完全甩开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#0002F是吗……而且蔡特也在，\x01",
            "我们可以暂时安心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xB,
        "#1200F呜～\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        (
            "#0306F哈，事态已经发展至此，\x01",
            "不管发生什么状况也都\x01",
            "不足为奇啦。\x02\x03",

            "#0300F……罗伊德，\x01",
            "补给工作一定要做好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#0000F嗯，我明白。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE4, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4C(0xB, 0xFF)
    Jump("loc_1414")

    label("loc_13A0")


    #C0050
    ChrTalk(
        0xC,
        (
            "#0303F这里的警备员们似乎\x01",
            "正在外面巡逻呢。\x02\x03",

            "#0300F稍微休息一下之后，我们\x01",
            "就冷静下来，好好考虑一下今后的对策吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1414")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_E6C end

    def Function_12_141C(): pass

    label("Function_12_141C")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BF")

    #C0051
    ChrTalk(
        0xFE,
        (
            "噢，我都听说啦，\x01",
            "你们要出战了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "……已经做好万全的准备了吗？\x01",
            "装备和队列都要好好检查一下啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "好好加油啊，特别任务支援科！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 4)
    Jump("loc_19FB")

    label("loc_14BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FB")

    #C0054
    ChrTalk(
        0xD,
        (
            "哟……\x01",
            "情况好像变得\x01",
            "十分不得了啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 4)), scpexpr(EXPR_END)), "loc_15FA")

    #C0055
    ChrTalk(
        0x101,
        (
            "#0005F修理店的师傅……\x02\x03",

            "#0000F说起来，\x01",
            "您好像说过今天要去\x01",
            "财团分部露个面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xD,
        (
            "噢，是啊。\x01",
            "在那之后，我就来到了位于\x01",
            "这座大厦五层的分部。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xD,
        (
            "和罗伯兹那家伙\x01",
            "聊了聊发明方面的创意……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xD,
        (
            "真没想到，居然会发生\x01",
            "这样的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E0")

    label("loc_15FA")


    #C0059
    ChrTalk(
        0x101,
        (
            "#0005F您是旧城区修理店的……\x02\x03",

            "#0005F基约姆师傅，您怎么在这里啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xD,
        (
            "啊，那个嘛，今天我正好\x01",
            "到财团分部来拜访啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xD,
        (
            "和罗伯兹那家伙\x01",
            "聊了聊发明方面的创意，\x01",
            "不知不觉就耗到这么晚。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xD,
        (
            "但真是没想到，\x01",
            "居然会发生这样的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E0")


    #C0063
    ChrTalk(
        0x101,
        (
            "#0003F实在抱歉，把您也给卷进来了，\x01",
            "这都是我们的错。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xD,
        (
            "啊哈哈，用不着介意！\x01",
            "这并不是你们的错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xD,
        (
            "话说回来，我这种大叔\x01",
            "好像也能发挥一些作用啊，\x01",
            "我会尽全力协助你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xD,
        "工房道具准备得一应俱全哦。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xD,
        (
            "想改造导力器也好，\x01",
            "想强化武器也好，\x01",
            "不管有什么需求，尽管来和我说就是了！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#0000F非常感谢，我一定会\x01",
            "充分利用这个机会的。\x02\x03",

            "#0003F（对了……连同装备的调整，\x01",
            "  把导力器也好好检查一下吧。）\x02\x03",

            "（毕竟还不知道接下来\x01",
            "  将会出现怎样的状况呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E8")
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※与基约姆师傅对话，并选择『委托改造』后，\x01",
            "  便能调出可改造物品一览表。\x01",
            "  如果拥有改造所需的素材，就可以进行改造。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※经过改造的武器与防具都是\x01",
            "  无法在武器商会等地取得的强力装备，\x01",
            "  特别是有些武器还会附带特殊效果。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※改造所需的『素材』\x01",
            "  主要都是魔兽掉落的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    label("loc_19E8")

    SetScenarioFlags(0xEE, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xD)
    Return()

    label("loc_19FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CD2")

    #C0072
    ChrTalk(
        0xFE,
        (
            "话说回来，那东西……\x01",
            "不是『塞姆里亚石』吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "你带着相当宝贵的东西啊！\x01",
            "究竟是在哪里得到的！？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#0005F那个，这块石头莫非是\x01",
            "如此珍贵的物品吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "是啊，这种石头可是被\x01",
            "称为古代文明遗物的东西呢，\x01",
            "坚硬度无与伦比，根本无法炼化。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "不过……就在去年，终于听到了传闻，\x01",
            "说是已经发现了加工方法，\x01",
            "我也从财团那里打听到了具体方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "如果是用这种材料打造出的武器……\x01",
            "一定会拥有最强的威力。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#0005F这、这原来是如此惊人的东西啊！\x02\x03",

            "#0003F不过，最强的武器吗……\x01",
            "在如今这种状况下，\x01",
            "正需要那种东西呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "嘿嘿，正好我这里也有\x01",
            "不少最新的\x01",
            "武器设计图呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "如果愿意的话，\x01",
            "就用你手上的塞姆里亚石\x01",
            "来打造好啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "……使用一块石头，\x01",
            "我想应该够打造出一人份的武器吧……\x01",
            "如何，要试试看吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEF, 7)
    Call(0, 13)
    TalkEnd(0xD)
    Return()

    label("loc_1CD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2244")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223F")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "对话")
    MenuCmd(1, 0, "改造·合成（导力器）")
    MenuCmd(1, 0, "委托改造（装备）")
    MenuCmd(1, 0, "委托升级魔导杖")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D9C")
    MenuCmd(1, 0, "委托打造最强武器")

    label("loc_1D9C")

    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DCE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1DCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DF4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1DF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F25")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    #C0082
    ChrTalk(
        0xD,
        (
            "对了，你们知道\x01",
            "『结晶孔的强化』吗？\x02",
        )
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    #A0083
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※关于结晶孔的强化。\x02",
        )
    )

    CloseMessageWindow()

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※选择[SLOT]后，\x01",
            "  再选择已经开封过的结晶孔，\x01",
            "  就可以强化结晶孔的等级。\x02",
        )
    )

    CloseMessageWindow()

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※进行强化之后，结晶孔不仅可以镶嵌\x01",
            "  高级回路，最大ＥＰ量也会\x01",
            "  进一步得到提升。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD9, 3)
    OP_C7(0x1, 0x80)

    label("loc_1F25")

    OP_AF(0xAF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_223A")

    label("loc_1F36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F56")
    OP_AF(0xAE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_223A")

    label("loc_1F56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20E7")

    #C0086
    ChrTalk(
        0xD,
        "噢，要改造那个魔导杖吗。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xD,
        (
            "我已经全部准备好啦。\x01",
            "要使用材料\x01",
            "来进行改造吗？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是的】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2087")

    #C0088
    ChrTalk(
        0x101,
        "#0000F嗯，拜托了。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xD,
        (
            "好，那么，\x01",
            "就去和罗伯兹那家伙\x01",
            "说一声吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#0000F说得也是呢。\x01",
            "顺便也去和缇欧\x01",
            "说一声吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 1)
    NewScene("c1320", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_2087")


    #C0091
    ChrTalk(
        0xD,
        (
            "是吗，那以后如果想要进行升级，\x01",
            "就再来和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xD,
        "我这里已经准备充分了。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_223A")

    label("loc_20E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2112")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_210D")
    Call(0, 13)
    TalkEnd(0xD)
    Return()

    label("loc_210D")

    Jump("loc_223A")

    label("loc_2112")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2126")
    Jump("loc_223A")

    label("loc_2126")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_21B2")

    #C0093
    ChrTalk(
        0xFE,
        (
            "我都听说啦，\x01",
            "你们要出战了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "……已经做好万全的准备了吗？\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        "好好干啊，特别任务支援科！\x02",
    )

    CloseMessageWindow()
    Jump("loc_223A")

    label("loc_21B2")


    #C0096
    ChrTalk(
        0xD,
        (
            "爱普斯泰恩财团的分部\x01",
            "也在这栋大楼里呢，\x01",
            "设备方面完全没问题哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xD,
        (
            "如果有什么需要的话，\x01",
            "请不必客气，尽管和我说。\x01",
            "我会尽心对待的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223A")

    Jump("loc_1D16")

    label("loc_223F")

    Jump("loc_25F9")

    label("loc_2244")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_224E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F9")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "对话")
    MenuCmd(1, 0, "改造·合成（导力器）")
    MenuCmd(1, 0, "委托改造（装备）")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22C2")
    MenuCmd(1, 0, "委托打造最强武器")

    label("loc_22C2")

    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22F4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_22F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_231A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_231A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_245C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    #C0098
    ChrTalk(
        0xD,
        (
            "对了，你们知道\x01",
            "『结晶孔的强化』吗？\x02",
        )
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※关于结晶孔的强化。\x02",
        )
    )

    CloseMessageWindow()

    #A0100
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※选择[SLOT]后，\x01",
            "  再选择已经开封过的结晶孔，\x01",
            "　就可以强化结晶孔的等级。\x02",
        )
    )

    CloseMessageWindow()

    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※进行强化之后，结晶孔不仅可以镶嵌\x01",
            "  高级回路，最大ＥＰ量也会\x01",
            "  进一步得到提升。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD9, 3)
    OP_C7(0x1, 0x80)

    label("loc_244B")

    OP_AF(0xAF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25F4")

    label("loc_245C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_247C")
    OP_AF(0xAE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25F4")

    label("loc_247C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A7")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24A2")
    Call(0, 13)
    TalkEnd(0xD)
    Return()

    label("loc_24A2")

    Jump("loc_25F4")

    label("loc_24A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24BB")
    Jump("loc_25F4")

    label("loc_24BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_2568")

    #C0102
    ChrTalk(
        0xFE,
        (
            "我都听说啦，\x01",
            "你们要出战了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "……已经做好万全的准备了吗？\x01",
            "装备和队列都要好好检查一下啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "好好加油啊，特别任务支援科！\x02",
    )

    CloseMessageWindow()
    Jump("loc_25F4")

    label("loc_2568")


    #C0105
    ChrTalk(
        0xD,
        (
            "爱普斯泰恩财团的分部\x01",
            "也在这栋大楼里呢，\x01",
            "设备方面完全没问题哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xD,
        (
            "如果有什么需要，\x01",
            "请不必客气，尽管和我说。\x01",
            "我一定会拼尽全力来完成！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F4")

    Jump("loc_224E")

    label("loc_25F9")

    TalkEnd(0xD)
    Return()

    # Function_12_141C end

    def Function_13_25FD(): pass

    label("Function_13_25FD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【委托打造罗伊德的武器】\x01",      # 0
            "【委托打造艾莉的武器】\x01",        # 1
            "【委托打造缇欧的武器】\x01",        # 2
            "【委托打造兰迪的武器】\x01",        # 3
            "【放弃】\x01",                      # 4
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270B")

    #C0107
    ChrTalk(
        0xFE,
        (
            "很好，那我也要拿出\x01",
            "全部本领啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "要使用这塞姆里亚石\x01",
            "打造出我的最高杰作！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2726")

    label("loc_270B")


    #C0109
    ChrTalk(
        0xFE,
        (
            "好！就请\x01",
            "稍等片刻吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2726")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_4B(0xD, 0xFF)
    OP_68(6020, 1500, 19170, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(17100, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0x101, 5670, 0, 19810, 90)
    OP_93(0xD, 0x10E, 0x0)
    Sleep(1500)
    FadeToBright(2000, 0)
    OP_0D()

    #C0110
    ChrTalk(
        0xFE,
        "#2P#40W嗯，最后调整大概就是这样了……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "#2P……好，完成了。\x01",
            "收下吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2823")

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '雷神之佑'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber('雷神之佑', 1)
    Jump("loc_28A2")

    label("loc_2823")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_284F")

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白圣枪'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber('纯白圣枪', 1)
    Jump("loc_28A2")

    label("loc_284F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_287B")

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天启'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber('天启', 1)
    Jump("loc_28A2")

    label("loc_287B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28A2")

    #A0115
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天灾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber('天灾', 1)

    label("loc_28A2")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('塞姆里亚石', 1)
    OP_DE(0x18, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B7")

    #C0116
    ChrTalk(
        0x101,
        (
            "#0005F真的完成了啊……\x02\x03",

            "#0005F基约姆师傅，太谢谢您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "#2P没什么啦，能用上这样珍贵的\x01",
            "材料，对身为技师的我来说，\x01",
            "也算是上辈子修来的福份呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "#2P如果还有什么需要，\x01",
            "请不必客气，尽管开口啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        "#0000F好的，那就拜托您了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A31")

    label("loc_29B7")


    #C0120
    ChrTalk(
        0xFE,
        (
            "#2P正是在这种特殊时期，\x01",
            "它才能派上用场吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "#2P所以呢，就请加油吧！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#0000F是的，我们一定会\x01",
            "好好使用它的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A31")

    OP_5A()
    SetScenarioFlags(0xF0, 0)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xA, 0x8000)
    EventEnd(0x5)
    Jump("loc_2AAF")

    label("loc_2A45")


    #C0123
    ChrTalk(
        0xFE,
        (
            "是吗，好，如果还有什么需要，\x01",
            "尽管来和我说就是了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "只要是能做到的事情，\x01",
            "我一定会拼尽全力来完成！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAF")

    Return()

    # Function_13_25FD end

    def Function_14_2AB0(): pass

    label("Function_14_2AB0")

    EventBegin(0x1)

    #C0125
    ChrTalk(
        0x101,
        (
            "#0003F警备人员正在\x01",
            "外面巡逻呢……\x02\x03",

            "#0001F趁此机会，还是先去进行补给，\x01",
            "顺便休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -460, 300, 4950, 0)
    EventEnd(0x4)
    Return()

    # Function_14_2AB0 end

    def Function_15_2B25(): pass

    label("Function_15_2B25")

    EventBegin(0x1)

    #C0126
    ChrTalk(
        0x101,
        (
            "#0003F必须要拆除门前的导力炸弹，\x01",
            "并阻止警备队员的入侵啊。\x02\x03",

            "#0001F……没时间犹豫了。\x01",
            "正面迎击吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 6280, 0, 15970, 270)
    EventEnd(0x4)
    Return()

    # Function_15_2B25 end

    SaveToFile()

Try(main)
