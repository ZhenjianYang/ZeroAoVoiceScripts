from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t053b.bin",                # FileName
        "t053b",                    # MapName
        "t053b",                    # Location
        0x0040,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 64, 0, 1, 0, 2],
    )

    BuildStringList((
        "t053b",                  # 0
        "贝卡莱",                 # 1
        "奇米",                   # 2
    ))

    AddCharChip((
        "chr/ch23400.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch22700.itc",                   # 02
    ))

    DeclNpc(-129,    0,       3640,    225,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-2009,   0,       2130,    45,   261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)

    DeclActor(-40,     0,       2120,    1000,    -130,    1500,    3640,    0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_118",          # 00, 0
        "Function_1_1D0",          # 01, 1
        "Function_2_1D1",          # 02, 2
        "Function_3_1D2",          # 03, 3
        "Function_4_1D6",          # 04, 4
        "Function_5_388",          # 05, 5
        "Function_6_472",          # 06, 6
    ))


    def Function_0_118(): pass

    label("Function_0_118")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_158"),
        (1, "loc_164"),
        (2, "loc_170"),
        (3, "loc_17C"),
        (4, "loc_188"),
        (5, "loc_194"),
        (6, "loc_1A0"),
        (SWITCH_DEFAULT, "loc_1AC"),
    )


    label("loc_158")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_164")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_170")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_17C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_188")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_194")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_1A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_1AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_1B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_1CF")

    Return()

    # Function_0_118 end

    def Function_1_1D0(): pass

    label("Function_1_1D0")

    Return()

    # Function_1_1D0 end

    def Function_2_1D1(): pass

    label("Function_2_1D1")

    Return()

    # Function_2_1D1 end

    def Function_3_1D2(): pass

    label("Function_3_1D2")

    Call(0, 4)
    Return()

    # Function_3_1D2 end

    def Function_4_1D6(): pass

    label("Function_4_1D6")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_384")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_233")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_233")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_252")
    OP_AF(0x56)
    Jump("loc_274")

    label("loc_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_262")
    OP_AF(0x55)
    Jump("loc_274")

    label("loc_262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_272")
    OP_AF(0x57)
    Jump("loc_274")

    label("loc_272")

    OP_AF(0x55)

    label("loc_274")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F")

    label("loc_283")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_297")
    Jump("loc_37F")

    label("loc_297")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_320")

    #C0001
    ChrTalk(
        0x8,
        (
            "……哦，这么晚过来，\x01",
            "胆子不小嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "喂，说说你想要的东西吧。\x01",
            "要是敢耍我，可饶不了你。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_37F")

    label("loc_320")


    #C0003
    ChrTalk(
        0x8,
        "喂，说你想要的东西吧，快说。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "既然打扰了我和女儿的宝贵时间，\x01",
            "要是敢耍我，可饶不了你。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37F")

    Jump("loc_1E3")

    label("loc_384")

    TalkEnd(0x8)
    Return()

    # Function_4_1D6 end

    def Function_5_388(): pass

    label("Function_5_388")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E")
    OP_93(0xFE, 0x2D, 0x0)
    OP_4B(0x8, 0xFF)

    #C0005
    ChrTalk(
        0xFE,
        (
            "爸爸，\x01",
            "都已经这么晚了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "今天晚饭吃什么呢～？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "哦，今天就做奇米\x01",
            "喜欢吃的肉饼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "哇～！最喜欢爸爸做的肉饼了！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_46E")

    label("loc_42E")

    TurnDirection(0xFE, 0x0, 0)

    #C0009
    ChrTalk(
        0xFE,
        (
            "爸爸虽然对镇上的人很严厉，\x01",
            "但是对奇米却非常温柔哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E")

    TalkEnd(0xFE)
    Return()

    # Function_5_388 end

    def Function_6_472(): pass

    label("Function_6_472")

    Return()

    # Function_6_472 end

    SaveToFile()

Try(main)
