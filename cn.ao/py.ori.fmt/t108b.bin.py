from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t108b.bin",                # FileName
        "t108b",                    # MapName
        "t108b",                    # Location
        0x0042,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 2, 0, 3],
    )

    BuildStringList((
        "t108b",                  # 0
        "莉夏",                   # 1
        "洛琪",                   # 2
        "佐尔克",                 # 3
        "兰迪",                   # 4
        "瓦吉",                   # 5
        "琪雅",                   # 6
    ))

    AddCharChip((
        "chr/ch05202.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch25900.itc",                   # 02
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-100709, 0,       8260,    270,  385,  0x0, 0,   1,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(-14840,  0,       6570,    90,   389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0040, 0, 12,  12.0,                  12.0,                  -1.0,                  56.25,                 [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666667014360428,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.8000000715255737,   -0.8000000715255737,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 16,  -110.0,                10.0,                  -1.0,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   55.0,                  -2.5,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 17,  -100.0,                14.0,                  -1.0,                  16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   25.0,                  -7.0,                  0.20000000298023224,   1.0])

    DeclActor(-13250,  0,       6540,    1500,    -14840,  1500,    6570,    0x007E, 0,  5,  0x0000)

    ChipFrameInfo(724, 0)                                        # 0

    ScpFunction((
        "Function_0_2D4",          # 00, 0
        "Function_1_38C",          # 01, 1
        "Function_2_3ED",          # 02, 2
        "Function_3_46A",          # 03, 3
        "Function_4_548",          # 04, 4
        "Function_5_835",          # 05, 5
        "Function_6_839",          # 06, 6
        "Function_7_8AE",          # 07, 7
        "Function_8_2B22",         # 08, 8
        "Function_9_2B84",         # 09, 9
        "Function_10_2BD1",        # 0A, 10
        "Function_11_329D",        # 0B, 11
        "Function_12_37D3",        # 0C, 12
        "Function_13_3BFB",        # 0D, 13
        "Function_14_52E3",        # 0E, 14
        "Function_15_58A4",        # 0F, 15
        "Function_16_5911",        # 10, 16
        "Function_17_598A",        # 11, 17
    ))


    def Function_0_2D4(): pass

    label("Function_0_2D4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_314"),
        (1, "loc_320"),
        (2, "loc_32C"),
        (3, "loc_338"),
        (4, "loc_344"),
        (5, "loc_350"),
        (6, "loc_35C"),
        (SWITCH_DEFAULT, "loc_368"),
    )


    label("loc_314")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_320")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_32C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_338")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_344")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_350")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_35C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_368")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_374")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_38B")

    Return()

    # Function_0_2D4 end

    def Function_1_38C(): pass

    label("Function_1_38C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EC")
    OP_95(0xFE, -106030, 0, 8260, 2000, 0x0)
    OP_95(0xFE, -106030, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 8260, 2000, 0x0)
    Jump("Function_1_38C")

    label("loc_3EC")

    Return()

    # Function_1_38C end

    def Function_2_3ED(): pass

    label("Function_2_3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_3FB")
    Jump("loc_418")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_418")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_42C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 7)
    Jump("loc_469")

    label("loc_42C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_443")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 11)
    Jump("loc_469")

    label("loc_443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_45A")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    Event(0, 14)
    Jump("loc_469")

    label("loc_45A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_469")
    ClearScenarioFlags(0x22, 3)
    Event(0, 13)

    label("loc_469")

    Return()

    # Function_2_3ED end

    def Function_3_46A(): pass

    label("Function_3_46A")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_47C")
    Jump("loc_489")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_489")
    OP_66(0x0, 0x1)

    label("loc_489")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A1")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B4")
    OP_1B(0x1, 0x0, 0xA)

    label("loc_4B4")

    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DB")
    OP_1B(0x6, 0x0, 0xF)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51F")
    OP_7D(0xAA, 0xAA, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x1, 0x1)
    Jump("loc_547")

    label("loc_51F")

    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_547")

    Return()

    # Function_3_46A end

    def Function_4_548(): pass

    label("Function_4_548")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_81A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_683")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_665")
    TurnDirection(0xFE, 0x105, 0)

    #C0001
    ChrTalk(
        0xFE,
        (
            "啊，客人……\x01",
            "您要走了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x105,
        "#10300F嗯，有人叫我们去迎宾馆。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "这、这样啊，\x01",
            "请您慢走……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "（怎、怎么会这样……\x01",
            "  还没有为瓦吉先生\x01",
            "  好好服务过呢～！）\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x105,
        "#10302F呵呵，奇怪的孩子。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#00006F……你其实很清楚她在想什么吧？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_67E")

    label("loc_665")


    #C0007
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "请您慢走……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67E")

    Jump("loc_815")

    label("loc_683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EA")

    #C0008
    ChrTalk(
        0xFE,
        "哎，瓦吉先生他……？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00000F哦，瓦吉好像已经\x01",
            "去迎宾馆了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "怎、怎么会这样……\x01",
            "还没有为瓦吉先生\x01",
            "好好服务过呢～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_73E")

    #C0011
    ChrTalk(
        0x102,
        "#00106F（瓦吉真是受欢迎啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E2")

    label("loc_73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_77B")

    #C0012
    ChrTalk(
        0x103,
        "#00203F（不愧是瓦吉先生，好受欢迎啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E2")

    label("loc_77B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_7AE")

    #C0013
    ChrTalk(
        0x104,
        "#00301F（那小子真受欢迎啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E2")

    label("loc_7AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_7E2")

    #C0014
    ChrTalk(
        0x109,
        "#10106F（不愧是瓦吉，真受欢迎呢……）\x02",
    )

    CloseMessageWindow()

    label("loc_7E2")

    SetScenarioFlags(0x0, 1)
    Jump("loc_815")

    label("loc_7EA")


    #C0015
    ChrTalk(
        0xFE,
        (
            "呼……本想再为瓦吉先生\x01",
            "服务一下呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_815")

    Jump("loc_831")

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_828")
    Jump("loc_831")

    label("loc_828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_831")

    label("loc_831")

    TalkEnd(0xFE)
    Return()

    # Function_4_548 end

    def Function_5_835(): pass

    label("Function_5_835")

    Call(0, 6)
    Return()

    # Function_5_835 end

    def Function_6_839(): pass

    label("Function_6_839")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_893")

    #C0016
    ChrTalk(
        0xA,
        (
            "吧台的营业\x01",
            "即将结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xA,
        (
            "在深夜期间\x01",
            "是无法点单的，\x01",
            "还请各位谅解。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AA")

    label("loc_893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8A1")
    Jump("loc_8AA")

    label("loc_8A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8AA")

    label("loc_8AA")

    TalkEnd(0xA)
    Return()

    # Function_6_839 end

    def Function_7_8AE(): pass

    label("Function_7_8AE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8D1")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8E8")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8FF")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7D), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_916")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_916")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7C), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_92D")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92D")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_96A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_987")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_987")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9A4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9C1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D8")
    SetScenarioFlags(0x147, 2)
    Jump("loc_A2F")

    label("loc_9D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EF")
    SetScenarioFlags(0x147, 3)
    Jump("loc_A2F")

    label("loc_9EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A06")
    SetScenarioFlags(0x147, 4)
    Jump("loc_A2F")

    label("loc_A06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1D")
    SetScenarioFlags(0x147, 5)
    Jump("loc_A2F")

    label("loc_A1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2F")
    SetScenarioFlags(0x147, 6)

    label("loc_A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B23")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆喜欢艾莉\x01",        # 0
            "◆喜欢缇欧\x01",        # 1
            "◆喜欢兰迪\x01",        # 2
            "◆喜欢诺艾尔\x01",      # 3
            "◆喜欢瓦吉\x01",        # 4
            "◆不做变更\x01",        # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_ABA"),
        (1, "loc_ACE"),
        (2, "loc_AE2"),
        (3, "loc_AF6"),
        (4, "loc_B0A"),
        (5, "loc_B1E"),
        (SWITCH_DEFAULT, "loc_B1E"),
    )


    label("loc_ABA")

    SetScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_B23")

    label("loc_ACE")

    ClearScenarioFlags(0x147, 2)
    SetScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_B23")

    label("loc_AE2")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    SetScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_B23")

    label("loc_AF6")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    SetScenarioFlags(0x147, 5)
    ClearScenarioFlags(0x147, 6)
    Jump("loc_B23")

    label("loc_B0A")

    ClearScenarioFlags(0x147, 2)
    ClearScenarioFlags(0x147, 3)
    ClearScenarioFlags(0x147, 4)
    ClearScenarioFlags(0x147, 5)
    SetScenarioFlags(0x147, 6)
    Jump("loc_B23")

    label("loc_B1E")

    Jump("loc_B23")

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_B35")
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_B78")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_B47")
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_B78")

    label("loc_B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_B59")
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_B78")

    label("loc_B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_B6B")
    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_B78")

    label("loc_B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_B78")
    AddParty(0x4, 0xEF, 0xFF)

    label("loc_B78")

    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(4111)
    SoundLoad(4112)
    SoundLoad(3397)
    SoundLoad(2912)
    SoundLoad(3518)
    SoundLoad(2758)
    SoundLoad(2678)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis246.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00200.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(5, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10301.itp")
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrPos(0x101, -100000, 0, -80000, 180)
    ClearMapObjFlags(0x7, 0x10)
    OP_74(0x7, 0xF)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0018
    AnonymousTalk(
        0x101,
        (
            "#00008F#30W好的……好的。\x02\x03",

            "#00000F……是吗，\x01",
            "那我就放心了。\x02\x03",

            "#00006F#20W真不好意思，把科长一个人留下，\x01",
            "只有我们几个过来玩……\x02\x03",

            "#00002F……哈哈，明白了，\x01",
            "我们会尽情享受的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-100000, 2000, -80000, 0)
    MoveCamera(325, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    FadeToBright(1000, 0)
    OP_68(-100000, 1000, -80000, 3000)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)
    Fade(250)
    Sound(802, 0, 100, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    #C0019
    ChrTalk(
        0x101,
        (
            "#00006F#11P呼……\x01",
            "支援科没有意外情况啊。\x02\x03",

            "#00008F看来我确实是\x01",
            "有点多虑了……\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 50, -1, -1)

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4111V#40W呵呵……\x01",
            "初次见面，支援科的诸位。\x02",
        )
    )

    CloseMessageWindow()

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4112V#40W作为亲近的证明，\x01",
            "我给你们留下了一些礼物，\x01",
            "希望大家玩得开心哟⊥\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0x1010)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_C9(0x1, 0x800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    Sleep(300)

    #C0022
    ChrTalk(
        0x101,
        (
            "#00003F#11P（多半就是那家伙将兰花塔\x01",
            "  的资料泄露给恐怖分子的吧。）\x02\x03",

            "（不过……他并不像是\x01",
            "  恐怖分子的同伴。）\x02\x03",

            "#00008F（同时也如『银』所说，\x01",
            "  并非黑月或赤色星座的成员……）\x02\x03",

            "#00001F（……究竟是什么人呢……？）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_150C")
    SetChrPos(0x102, -100000, 0, -74900, 180)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    #N0023
    NpcTalk(
        0x102,
        "艾莉的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3397V#2S#5P#30W#21A……罗伊德？\x01",
            "你在房间里吗？\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)

    #C0024
    ChrTalk(
        0x101,
        (
            "#00005F#6P哦，艾莉吗？\x02\x03",

            "#00002F在，进来吧。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 8)
    WaitChrThread(0x102, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0025
    AnonymousTalk(
        0x102,
        "哎，你刚才在和人联络吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0026
    ChrTalk(
        0x101,
        (
            "#00004F#6P嗯，和科长。\x02\x03",

            "#00008F……我们外出不在，不知支援科大楼\x01",
            "会不会发生什么意外情况，\x01",
            "担心之下就联系了科长……\x02\x03",

            "#00000F不过，看来只是我太过多虑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#00106F#11P这样啊……\x02\x03",

            "#00108F……想想在通商会议时\x01",
            "发生的事件，\x01",
            "担心也是可以理解的……\x02\x03",

            "#00102F不过，今天就别想任何事情了，\x01",
            "还是尽情享受休假吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈……说的对。\x02\x03",

            "#00002F抱歉，莫非你是\x01",
            "特意来接我的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#00112F#11P啊，嗯……\x01",
            "因为一直找不到你。\x02\x03",

            "#00108F要是不介意，就一起\x01",
            "去迎宾馆吧……\x02\x03",

            "#00113F……那个，如果没给你造成麻烦的话。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0030
    ChrTalk(
        0x101,
        (
            "#00011F#6P怎、怎么会有麻烦！\x02\x03",

            "#00006F真是的……\x01",
            "艾莉，你故意戏弄我吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        (
            "#00112F#11P并、并没有\x01",
            "戏弄的意思……\x02\x03",

            "#00109F那、那我们就\x01",
            "一起去迎宾馆吧。\x02\x03",

            "距离晚餐会还有一些时间，\x01",
            "先去其它地方逛逛也无妨。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00002F#6P说、说的也是啊，\x01",
            "那就顺便去商店里看看吧。\x02\x03",

            "#00012F（呃，在两人独处时，\x01",
            "  为何会如此紧张……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ADE")

    label("loc_150C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1A34")
    SetChrPos(0x103, -100000, 0, -74900, 180)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    #N0033
    NpcTalk(
        0x103,
        "缇欧的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2678V#2S#5P#30W#23A……罗伊德前辈，\x01",
            "现在方便吗？\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)

    #C0034
    ChrTalk(
        0x101,
        (
            "#00005F#6P哦，缇欧吗？\x02\x03",

            "#00002F方便啊，进来吧。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 8)
    WaitChrThread(0x103, 3)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0035
    AnonymousTalk(
        0x103,
        "……刚才是在和科长联络吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0036
    ChrTalk(
        0x101,
        (
            "#00004F#6P哈哈，你听出来了啊。\x02\x03",

            "#00008F……我们外出不在，不知支援科大楼\x01",
            "会不会发生什么意外情况，\x01",
            "担心之下就联系了科长……\x02\x03",

            "#00000F不过，看来只是我太过多虑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#00206F#11P原来如此……\x02\x03",

            "#00208F……连同那个神秘黑客在内，\x01",
            "确实残留着不少令人在意的事情……\x02\x03",

            "#00202F不过，难得的假期，\x01",
            "还是多休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00004F#6P哈哈……说的对。\x02\x03",

            "#00002F抱歉，莫非你是\x01",
            "特意来接我的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x103,
        (
            "#00203F#11P是的，大家已经\x01",
            "陆续前往迎宾馆了。\x02\x03",

            "#00200F不过，距离晚餐会\x01",
            "还有一些时间，\x01",
            "倒也不必太着急……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00000F#6P不，我也准备出发了。\x02\x03",

            "缇欧，如果可以，\x01",
            "我们一起去迎宾馆吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#00202F#11P………好。\x02\x03",

            "#00208F那个……路上顺便\x01",
            "去商店里看看可以吗？\x02\x03",

            "#00206F如果要我一个人进去，\x01",
            "多少还是有些抵触……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#00005F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#00201F#11P有、有什么奇怪的吗？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00012F#6P不不，没有没有！\x02\x03",

            "#00002F明白了，\x01",
            "那我们就去逛逛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#00202F#11P……嗯。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00004F#6P（唔……缇欧竟会对\x01",
            "  一般的商店感兴趣，真是少见啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ADE")

    label("loc_1A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1F05")
    SetChrPos(0x104, -100000, 0, -74900, 180)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #N0047
    NpcTalk(
        0x104,
        "兰迪的声音",
        (
            "#2758V#5P#30W#33A哦，你果然\x01",
            "还在房间里啊。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 9)
    OP_93(0x101, 0x0, 0x1F4)
    WaitChrThread(0x104, 3)

    #C0048
    ChrTalk(
        0x101,
        "#00002F#6P哦，兰迪啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0049
    AnonymousTalk(
        0x104,
        (
            "怎么，刚才在\x01",
            "和人联络吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    #C0050
    ChrTalk(
        0x101,
        (
            "#00006F#6P嗯，和科长。\x02\x03",

            "#00008F……我们外出不在，不知支援科大楼\x01",
            "会不会发生什么意外情况，\x01",
            "担心之下就联系了科长……\x02\x03",

            "#00000F不过，看来只是我太过多虑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#00308F#11P是吗……\x02\x03",

            "#00303F叔叔他们如今仍然\x01",
            "滞留在克洛斯贝尔……\x02\x03",

            "#00300F老实说，其实我也很担心，\x01",
            "不过今天还是\x01",
            "尽情享乐为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈……说的对。\x02\x03",

            "#00002F抱歉，莫非你是\x01",
            "特意来接我的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00304F#11P嗯，大家都已经\x01",
            "陆续前往迎宾馆啦。\x02\x03",

            "#00300F不过距离晚餐会\x01",
            "好像还有一些时间，\x01",
            "倒也不用太着急。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00004F#6P不，我也准备出发了。\x02\x03",

            "#00002F对了，兰迪，\x01",
            "你白天去逛了珠宝店吧？\x02\x03",

            "那里的东西怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x104,
        (
            "#00305F#11P哦，不愧是高档店，\x01",
            "里面有不少好东西……\x02\x03",

            "#00302F怎么？莫非你想\x01",
            "送礼物给喜欢的女孩？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#00011F#6P不、不是啦……\x01",
            "只是有点好奇而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#00309F#11P别害羞，别害羞。\x02\x03",

            "#00302F好！稍后顺便去转一下，\x01",
            "哥哥帮你一起挑吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00006F#6P都说不是那样了……\x02\x03",

            "#00000F算啦，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ADE")

    label("loc_1F05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_24E6")
    SetChrPos(0x109, -100000, 0, -74900, 180)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    #N0059
    NpcTalk(
        0x109,
        "诺艾尔的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3518V#2S#5P#30W#21A……罗伊德警官，\x01",
            "你在里面吗？\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)

    #C0060
    ChrTalk(
        0x101,
        (
            "#00005F#6P哦，诺艾尔吗？\x02\x03",

            "#00002F在的，进来吧。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 3, 0, 8)
    WaitChrThread(0x109, 3)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0061
    AnonymousTalk(
        0x109,
        (
            "啊，刚才在和\x01",
            "什么人联系吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)

    #C0062
    ChrTalk(
        0x101,
        (
            "#00004F#6P嗯，和科长。\x02\x03",

            "#00008F……我们外出不在，不知支援科大楼\x01",
            "会不会发生什么意外情况，\x01",
            "担心之下就联系了科长……\x02\x03",

            "#00000F不过，看来只是我太过多虑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x109,
        (
            "#10113F#11P……这样啊。\x02\x03",

            "#10106F毕竟发生过那样的事件，\x01",
            "确实是让人担心呢……\x02\x03",

            "#10108F………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#00011F#6P啊啊，真是的，怎么连你都\x01",
            "一脸愁容了，并没有发生什么严重的情况啊。\x02\x03",

            "#00006F那个……抱歉，\x01",
            "我说了些影响心情的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x109,
        (
            "#10112F#11P哪、哪里，是我不好。\x02\x03",

            "#10106F我的性格似乎是\x01",
            "有点容易多虑呢……\x02\x03",

            "#10100F有时候也挺羡慕\x01",
            "芙兰那种无忧无虑的性格。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00009F#6P哈哈，是吗。\x02\x03",

            "#00002F从这方面来看，\x01",
            "我们好像非常相似呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x109,
        (
            "#10111F#11P没、没有的事！\x01",
            "我的头脑比你差远了！\x02\x03",

            "#10112F我大概只是……\x01",
            "典型的警备队式性格而已吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#00012F#6P（唔……对自己的评价\x01",
            "  还是如此苛刻啊。）\x02\x03",

            "#00000F对了，你是……\x01",
            "特意来接我的吧？\x02\x03",

            "如果不介意，\x01",
            "一起去迎宾馆如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x109,
        (
            "#10102F#11P啊，好的！\x02\x03",

            "#10100F说起来，那场晚餐会好像要在\x01",
            "一座很惊人的豪宅中举办吧？\x02\x03",

            "听说是哈尔特曼前议长\x01",
            "以前的住所……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00006F#6P嗯，老实说，那所豪宅\x01",
            "的奢华程度简直让人难以置信。\x02\x03",

            "#00002F初次进入的人，\x01",
            "保证会震撼到瞪圆双眼。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x109,
        (
            "#10109F#11P啊哈哈……\x01",
            "真有点期待呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ADE")

    label("loc_24E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_2ADE")
    SetChrPos(0x105, -100000, 0, -74900, 180)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #N0072
    NpcTalk(
        0x105,
        "瓦吉的声音",
        (
            "#2912V#5P#30W#23A啊，果然还在\x01",
            "房间里啊。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 9)
    OP_93(0x101, 0x0, 0x1F4)
    WaitChrThread(0x105, 3)

    #C0073
    ChrTalk(
        0x101,
        "#00002F#6P哦，瓦吉啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_CB(0x5, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x5, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CC(0x0, 0x5, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0074
    AnonymousTalk(
        0x105,
        (
            "呵呵，原来如此。\x02\x03",

            "担心无人驻守的支援科大楼，\x01",
            "于是就联系了科长吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x5, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x5, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0075
    ChrTalk(
        0x101,
        "#00011F#6P你、你为何会知道！？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x105,
        (
            "#10304F#11P都已经共事一个多月了，\x01",
            "这种程度的小事还是可以猜到的。\x02\x03",

            "#10302F呵呵，看来你比我想象中的\x01",
            "更有队长风范啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#00004F#6P哈哈……只不过是爱操心罢了。\x02\x03",

            "#00008F真正优秀的队长\x01",
            "应该具有沉稳的气质。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x105,
        (
            "#10300F#11P可我却认为，衡量一个队长\x01",
            "是否优秀，标准是因人而异的。\x02\x03",

            "#10304F你虽然头脑不错，直觉也很敏锐，\x01",
            "但整体来说，终究是个普通的『凡人』而已。\x02\x03",

            "#10302F在能力允许的范围内尽量努力\x01",
            "也是个不坏的选择啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x101,
        (
            "#00006F#6P唔……说的好直接啊。\x02\x03",

            "#00013F但我并不讨厌你这种\x01",
            "有话直说，毫不矫揉造作的性格呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x105,
        (
            "#10304F#11P呵呵，我也很欣赏\x01",
            "你这种天真直爽的性格啊。\x02\x03",

            "#10302F说到底，无论是那个曹也好，\x01",
            "还是那个放荡不羁的帝国间谍也好，\x01",
            "那些精干的人永远都是那么精干。\x02\x03",

            "与其和他们在精干这方面拼，\x01",
            "还不如充分发挥你自身\x01",
            "特有的优势，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        "#00005F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x105,
        "#10305F#11P哎，我说了什么奇怪的话吗？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#00004F#6P不，只是我从来都\x01",
            "没往这方面考虑过……\x02\x03",

            "#00000F谢了，瓦吉，\x01",
            "我似乎受了一些启发呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x105,
        (
            "#10304F#11P呵呵，那就好。\x02\x03",

            "#10300F……对了，晚餐会就快开始了，\x01",
            "还不赶快出发吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#00002F#6P嗯，那我们就一起去吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2ADE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x0)
    OP_74(0x7, 0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -99290, 0, -79530, 0)
    SetScenarioFlags(0x145, 5)
    OP_29(0xA5, 0x1, 0x7)
    OP_1B(0x1, 0x0, 0xA)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_7_8AE end

    def Function_8_2B22(): pass

    label("Function_8_2B22")

    OP_68(-100000, 1000, -79000, 2500)
    Sound(121, 0, 100, 0)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)

    def lambda_2B4D():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B4D)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(890, 0, 100, 0)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_6F(0x79)
    Return()

    # Function_8_2B22 end

    def Function_9_2B84(): pass

    label("Function_9_2B84")

    OP_68(-100000, 1000, -79000, 2000)

    def lambda_2B9A():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B9A)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(890, 0, 100, 0)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_6F(0x79)
    Return()

    # Function_9_2B84 end

    def Function_10_2BD1(): pass

    label("Function_10_2BD1")

    EventBegin(0x0)
    Fade(500)
    OP_68(5700, 1000, 13400, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21380, 0)
    SetChrPos(0x101, 5700, 0, 13400, 315)
    SetChrPos(0xEF, 6700, 0, 12400, 315)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)

    #C0086
    ChrTalk(
        0x101,
        (
            "#00005F#5P对了，有人带着\x01",
            "琪雅吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_2D99")

    #C0087
    ChrTalk(
        0x102,
        (
            "#00104F#12P嗯，缇欧\x01",
            "带着她呢……\x02\x03",

            "#00100F应该已经在往迎宾馆走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00000F#5P是吗，那就放心了。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        "#00105F#12P那个……怎么了？\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#00006F#5P没什么，只是发生了不少事情，\x01",
            "未免有点神经质。\x02\x03",

            "#00002F不过她在主题公园\x01",
            "好像玩得很开心，\x01",
            "应该不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#00109F#12P呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_327E")

    label("loc_2D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_2EC8")

    #C0092
    ChrTalk(
        0x103,
        (
            "#00205F#12P嗯，艾莉前辈\x01",
            "带着她呢……\x02\x03",

            "#00202F现在应该已经在往迎宾馆走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00000F#5P是吗，那就放心了。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        "#00201F#12P……琪雅怎么了？\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00006F#5P没什么，只是发生了不少事情，\x01",
            "未免有点神经质。\x02\x03",

            "#00002F不过她在主题公园\x01",
            "好像玩得很开心，\x01",
            "应该不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        "#00202F#12P……嗯。\x02",
    )

    CloseMessageWindow()
    Jump("loc_327E")

    label("loc_2EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_2FFD")

    #C0097
    ChrTalk(
        0x104,
        (
            "#00305F#12P嗯，大小姐和阿缇\x01",
            "带着她呢……\x02\x03",

            "#00300F应该已经在往迎宾馆走了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00000F#5P是吗，那就放心了。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        "#00301F#12P嗯……？怎么了？\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#00006F#5P没什么，只是发生了不少事情，\x01",
            "未免有点神经质。\x02\x03",

            "#00002F不过她在主题公园\x01",
            "好像玩得很开心，\x01",
            "应该不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        "#00309F#12P哈哈，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_327E")

    label("loc_2FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_313B")

    #C0102
    ChrTalk(
        0x109,
        (
            "#10105F#12P啊，兰迪前辈和瓦吉\x01",
            "带着她呢……\x02\x03",

            "#10100F我想他们已经在往迎宾馆走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#00000F#5P是吗，那就放心了。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x109,
        (
            "#10101F#12P那个……\x01",
            "琪雅怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00006F#5P没什么，只是发生了不少事情，\x01",
            "未免有点神经质。\x02\x03",

            "#00002F不过她在主题公园\x01",
            "好像玩得很开心，\x01",
            "应该不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x109,
        "#10109F#12P呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_327E")

    label("loc_313B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_327E")

    #C0107
    ChrTalk(
        0x105,
        (
            "#10305F#12P哦，女士们\x01",
            "带着她呢。\x02\x03",

            "#10300F现在应该已在前往迎宾馆的路上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00000F#5P是吗，那就放心了。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x105,
        "#10301F#12P……发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#00006F#5P没什么，只是发生了不少事情，\x01",
            "未免有点神经质。\x02\x03",

            "#00002F不过她在主题公园\x01",
            "好像玩得很开心，\x01",
            "应该不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x105,
        (
            "#10309F#12P呵呵……\x01",
            "她确实玩得很兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_327E")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 5700, 0, 13400, 315)
    SetScenarioFlags(0x145, 6)
    OP_1B(0x1, 0xFF, 0xFFFF)
    EventEnd(0x5)
    Return()

    # Function_10_2BD1 end

    def Function_11_329D(): pass

    label("Function_11_329D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50106.itc", 0x1E)
    LoadChrToIndex("apl/ch51423.itc", 0x1F)
    LoadChrToIndex("apl/ch51424.itc", 0x20)
    LoadChrToIndex("apl/ch50107.itc", 0x21)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    SetChrPos(0x101, -104650, 400, -81200, 90)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xB, -104650, 400, -84300, 90)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, -104650, 400, -77900, 90)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x7, 0x10)
    OP_74(0x7, 0xF)
    OP_70(0x8, 0x2)
    OP_70(0x9, 0x2)
    OP_70(0xA, 0x2)
    OP_7D(0xAA, 0xAA, 0xFF, 0x0, 0x0)
    OP_68(-95000, 1000, 10000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    OP_68(-105000, 1000, 10000, 14000)
    Sleep(5000)
    OP_0D()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_68(-103000, 1000, -75900, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22000, 0)
    FadeToBright(2000, 0)
    OP_68(-104500, 1000, -81450, 8000)
    OP_6F(0x79)
    SetCameraDistance(21000, 3000)
    OP_6F(0x79)

    #C0112
    ChrTalk(
        0x101,
        (
            "#05203F#5P#30W（………………………………）\x02\x03",

            "#05208F（『壁障』……）\x02\x03",

            "（阻挡在前方的『壁障』……）\x02\x03",

            "#05201F（迪塔市长或许\x01",
            "　是在用他的方式\x01",
            "　来突破『壁障』吧……）\x02\x03",

            "#05206F（……可我们……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(800)
    SetCameraDistance(20500, 0)
    Sound(898, 0, 100, 0)
    OP_71(0x9, 0x2, 0x5, 0x0, 0x8)
    SetChrFlags(0x101, 0x20)

    def lambda_3514():
        OP_96(0xFE, 0xFFFE6736, 0x226, 0xFFFEC1D6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3514)
    OP_A0(0x101, 1200, 0x0, 0x5)
    ClearChrFlags(0x101, 0x20)
    Sound(812, 0, 100, 0)
    OP_79(0x9)
    OP_0D()
    Sleep(500)

    #C0113
    ChrTalk(
        0x101,
        (
            "#05208F#5P（……在黑手党横行的时期，\x01",
            "  『壁障』只是自行毁灭了而已……）\x02\x03",

            "（而在更加巨大的『壁障』\x01",
            "  矗立在眼前的现今……）\x02\x03",

            "#05203F（我们却……我却\x01",
            "  还是起不到什么作用……）\x02\x03",

            "#05213F（……这样真的好吗……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1400, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_A0(0x101, 1000, 0x5, 0x3)
    Sleep(500)

    #C0114
    ChrTalk(
        0x101,
        (
            "#05206F#5P（……不行，\x01",
            "  虽然很累，但完全睡不着。）\x02\x03",

            "#05200F（去休息室\x01",
            "  喝点水吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0x101, 0x7)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    OP_74(0x9, 0x5)

    def lambda_36B7():
        OP_98(0xFE, 0x0, 0x0, 0x12C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36B7)
    OP_71(0x9, 0x5, 0x7, 0x0, 0x8)
    OP_79(0x9)
    WaitChrThread(0x101, 1)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    OP_0D()
    Fade(250)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrPos(0x101, -104500, 0, -79950, 0)
    OP_0D()
    Sleep(200)
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_372D():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_372D)
    SetCameraDistance(20750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sleep(1000)
    Sound(121, 0, 70, 0)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x0)
    OP_74(0x7, 0x1E)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetChrPos(0x0, -100000, 0, 6750, 0)
    SetScenarioFlags(0x145, 7)
    OP_29(0xA5, 0x1, 0x8)
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x6, 0x0, 0xF)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_329D end

    def Function_12_37D3(): pass

    label("Function_12_37D3")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SoundLoad(2635)
    SoundLoad(3246)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01801.itp")
    SetChrPos(0x101, 4900, 0, 9150, 45)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 10600, 150, 15400, 90)
    OP_68(4900, 1000, 9150, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(1000, 0)
    Sleep(500)

    #C0115
    ChrTalk(
        0x101,
        "#00005F（啊……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(10600, 1000, 15400, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    SetCameraDistance(20000, 3000)
    OP_6F(0x79)
    OP_0D()

    #C0116
    ChrTalk(
        0x8,
        "#01808F#40W#5P……………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0117
    ChrTalk(
        0x101,
        "#11P……哟，莉夏。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(11200, 1000, 14250, 4000)
    MoveCamera(315, 23, 0, 4000)

    def lambda_3972():
        OP_95(0xFE, 11720, 0, 12790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3972)
    Sound(2635, 255, 80, 0)    #voice#Rixia
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0118
    AnonymousTalk(
        0x8,
        "#30W#3246V罗伊德警官吗……\x02",
    )

    CloseMessageWindow()
    OP_24(0xCAE)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0119
    ChrTalk(
        0x101,
        (
            "#00005F#6P……？\x02\x03",

            "#00012F抱歉，我突然出声，\x01",
            "吓到你了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "#01809F#30W#11P啊哈哈，怎么会……\x02\x03",

            "#01802F#30W我只是\x01",
            "发了一下呆而已……\x02\x03",

            "#01808F#30W………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#00006F#6P那个……\x02\x03",

            "#00002F我可以坐在这里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        "#01803F#30W#11P……………………（点头）\x02",
    )

    CloseMessageWindow()
    OP_68(12100, 1000, 15400, 2000)

    def lambda_3B6B():
        OP_95(0xFE, 13000, 0, 15400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B6B)
    Sleep(800)
    SetChrSubChip(0x8, 0x0)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    OP_6F(0x79)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 13450, 150, 15400, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    OP_68(12100, 1000, 16000, 3500)
    Sleep(700)
    SetChrSubChip(0x8, 0x1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 3)
    NewScene("e430B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_37D3 end

    def Function_13_3BFB(): pass

    label("Function_13_3BFB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch13600.itc", 0x1F)
    LoadChrToIndex("apl/ch51325.itc", 0x20)
    LoadChrToIndex("chr/ch05200.itc", 0x21)
    SoundLoad(3247)
    SoundLoad(3614)
    SoundLoad(3615)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis009.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01150.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis010.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01801.itp")
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 13450, 150, 15400, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 10600, 150, 15400, 90)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 4900, 0, 9150, 90)
    SetChrFlags(0xD, 0x8)
    OP_68(12100, 1000, 15400, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    FadeToBright(2000, 0)
    SetCameraDistance(20000, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrSubChip(0x8, 0x0)
    Sleep(150)

    #C0123
    ChrTalk(
        0x8,
        (
            "#01804F#5P罗伊德警官真是不可思议啊。\x02\x03",

            "#01810F在我希望有人陪伴在身边时，\x01",
            "你就真的出现了……\x02\x03",

            "不知为何，你光是待在这里，\x01",
            "就能让我感到很安心……\x02\x03",

            "#01809F呵呵，真羡慕\x01",
            "支援科的各位。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0124
    ChrTalk(
        0x101,
        (
            "#00002F#12P哈哈，你太过奖了。\x02\x03",

            "#00006F无论是身为一名正式搜查官，\x01",
            "还是身为大家的队长，\x01",
            "我都有很多不足之处呢。\x02\x03",

            "#00008F必须……\x01",
            "要变得更强大才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        "#01810F#5P#30W嘻嘻……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    StopBGM(0xFA0)

    #C0126
    ChrTalk(
        0x101,
        (
            "#00003F#12P对了，莉夏。\x02\x03",

            "#00008F虽然可能有些失礼……\x01",
            "不过可以问你一个问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "#01805F#5P……？\x02\x03",

            "#01810F失礼……\x01",
            "究竟是什么问题呢？\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    SetCameraDistance(19000, 70000)
    Sleep(500)

    #C0128
    ChrTalk(
        0x101,
        (
            "#00006F#12P为什么你……\x02\x03",

            "#00001F在面露笑容的时候，\x01",
            "目光却那么哀伤呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        "#01812F#5P……！\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#00008F#12P……仔细想想，从我们刚认识的时候开始，\x01",
            "你似乎就是这样。\x02\x03",

            "#00003F被伊莉娅小姐寄予厚望，\x01",
            "在最高级别的舞台上活跃表现……\x02\x03",

            "说起莉夏·毛，如今已经是\x01",
            "克洛斯贝尔的名人了。\x02\x03",

            "#00001F但你为什么……\x02\x03",

            "为什么总是显露出这种\x01",
            "看起来就像是放弃了什么重要之物\x01",
            "一样的微笑呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        "#01808F#5P你、你为何能察觉到……\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#00006F#12P……因为某位与我很亲密的人\x01",
            "在过去一段时间中也经常露出这样的笑脸。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)

    #C0133
    ChrTalk(
        0x101,
        (
            "#00008F#12P如今，已经不会在她的脸上\x01",
            "看到那种哀伤的笑容了……\x02\x03",

            "#00001F可是我突然意识到，\x01",
            "一直以来，总能在你的脸上看到那样的笑容。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        "#01806F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#00003F#12P那个人的笑容，\x01",
            "是因为要忍耐永远无法与\x01",
            "最爱之人再会的哀伤。\x02\x03",

            "#00001F而你呢……？\x02\x03",

            "最喜欢伊莉娅小姐的你，\x01",
            "为何会面露那样的笑容？\x02\x03",

            "她一直都在你身边啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        "#01808F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0137
    ChrTalk(
        0x8,
        (
            "#01803F#5P……老实说，我真是非常吃惊。\x02\x03",

            "#01810F虽然早就知道你很敏锐，\x01",
            "但没想到竟然连这些都能……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        "#00005F#12P……言下之意就是………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0139
    ChrTalk(
        0x8,
        (
            "#01804F#5P呵呵……你说的没错。\x02\x03",

            "#01810F我大概……在不久之后就会\x01",
            "离开克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0140
    ChrTalk(
        0x101,
        (
            "#00006F#12P……果然如此啊。\x02\x03",

            "#00008F理由……\x01",
            "大概不是我能问的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#01804F#5P……………嗯。\x02\x03",

            "#01808F……不过，也罢。\x01",
            "虽然不能说得太详细……\x02\x03",

            "#01810F我本来……\x01",
            "有一条注定要踏上的道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#00005F#12P注定要踏上的道路……？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "#01804F#5P呵呵，类似于继承家业吧。\x02\x03",

            "#01808F……我从很小的时候开始……\x01",
            "就将那个目标视为人生的全部了。\x02\x03",

            "从极其久远的往昔开始，\x01",
            "我的祖先便世代继承那条道路……\x02\x03",

            "#01803F现如今，早已不知\x01",
            "为何要踏上那条道路了。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#00003F#12P是吗……\x02\x03",

            "#00001F……不过，既然如此……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "#01810F#5P既然如此，所以没必要继续继承……？\x01",
            "这条道路也无法如此简单地否定。\x02\x03",

            "#01804F至少我的父亲\x01",
            "寻找到了继承这条道路\x01",
            "的意义。\x02\x03",

            "通过这条黑暗隐秘的道路，\x01",
            "可以影响到世界，\x01",
            "进而改变历史的轨迹……\x02\x03",

            "#01808F而我也继承了\x01",
            "父亲所选择的道路，\x01",
            "并一直走到了今天……\x02\x03",

            "#01810F……今后，也一样会……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        "#00001F#12P………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0147
    ChrTalk(
        0x8,
        (
            "#01804F#5P呵呵……我真是很奇怪呢。\x02\x03",

            "明明拒绝了伊莉娅小姐\x01",
            "递给我的葡萄酒……\x02\x03",

            "#01810F……或许是为\x01",
            "月光所沉醉了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#00002F#12P哈哈……也许吧。\x02\x03",

            "#00006F……抱歉，\x01",
            "我好像触及到你的隐私了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "#01804F#5P不，没关系。\x02\x03",

            "#01810F其实……\x01",
            "我的脑子里也非常混乱。\x02\x03",

            "#01809F你能听我说这么多，\x01",
            "真是非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#00004F#12P是吗……\x01",
            "那可真是我的荣幸。\x02\x03",

            "#00001F不过，莉夏，\x01",
            "莫非你——\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    ClearChrFlags(0xD, 0x8)
    OP_C9(0x0, 0x80000000)

    #N0151
    NpcTalk(
        0xD,
        "琪雅的声音",
        "#3614V#50W#13A……罗伊德……？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_24(0xE1E)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    OP_68(11200, 1000, 14250, 3500)
    MoveCamera(315, 23, 0, 3500)
    OP_9B(0x1, 0xD, 0xFFDD, 0x1770, 0x5DC, 0x0)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetMessageWindowPos(50, 140, -1, -1)

    #A0152
    AnonymousTalk(
        0x101,
        "#00005F琪雅……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 160, -1, -1)

    #A0153
    AnonymousTalk(
        0x8,
        "#01805F……哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)
    OP_95(0xD, 11720, 0, 12790, 1200, 0x0)
    OP_93(0xD, 0x0, 0x190)

    #C0154
    ChrTalk(
        0xD,
        (
            "#05805F#30W#6P……啊……\x01",
            "莉夏也在……\x02\x03",

            "#05800F#30W……莫非你们在谈话吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "#01809F#5P没、没有啦，\x01",
            "都已经谈完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#00002F#11P嗯，不用介意的。\x02\x03",

            "#00001F……你是不是\x01",
            "睡不着呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xD,
        (
            "#05808F#30W#6P…………嗯……\x02\x03",

            "#05806F#30W……好像做了一个\x01",
            "很可怕的梦……\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#00003F#11P是吗……\x02\x03",

            "#00000F要不要到我的床上一起睡？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xD,
        "#05812F#30W#6P……可以吗？\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#00009F#11P嗯，这次就破例吧。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x101, 0x4)
    SetChrPos(0x101, 13000, 0, 15400, 270)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    OP_68(11950, 1000, 14600, 1500)
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_4CBA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CBA)
    OP_93(0xD, 0x2D, 0x1F4)
    Sleep(500)

    def lambda_4CD9():
        OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4CD9)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xE1, 0x1F4)
    WaitChrThread(0xD, 1)
    OP_6F(0x1)
    SetChrFlags(0xD, 0x8)
    Fade(250)
    OP_68(11950, 1100, 14600, 500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    #N0161
    NpcTalk(
        0x101,
        "琪雅",
        "#05809F#30W#5P……嘿嘿嘿……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(150)

    #C0162
    ChrTalk(
        0x101,
        (
            "#00006F#6P抱歉啊，莉夏，\x01",
            "以这么奇怪的形式中断了谈话。\x02",
        )
    )

    CloseMessageWindow()
    Fade(300)
    Sound(812, 0, 100, 0)
    SetChrPos(0x8, 11000, 0, 15400, 90)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_93(0x8, 0x87, 0x1F4)

    #C0163
    ChrTalk(
        0x8,
        (
            "#01809F#5P呵呵，哪里。\x02\x03",

            "#01802F多亏罗伊德警官，\x01",
            "我大概也能睡着了。\x02\x03",

            "#01804F谢谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        "#00002F#6P是吗……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        (
            "#01808F#5P……至于刚才说的那些话，\x01",
            "还请对伊莉娅小姐\x01",
            "保密。\x02\x03",

            "#01810F时机合适的时候，\x01",
            "我会自己和她说的。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#00003F#6P……明白了。\x02\x03",

            "#00000F也许我很靠不住，\x01",
            "但如果遇到了什么事情，可以尽管和我说。\x02\x03",

            "只要我力所能及，\x01",
            "一定会尽力帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x8,
        (
            "#01809F#5P呵呵……\x01",
            "谢谢了。\x02\x03",

            "#01802F嗯，如果我遇到了什么困难，\x01",
            "一定会找你商量。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0168
    AnonymousTalk(
        0x8,
        (
            "#3247V#40W晚安，\x01",
            "罗伊德警官，琪雅。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCAF)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    #C0169
    ChrTalk(
        0x101,
        "#00002F#6P晚安，莉夏。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_C9(0x0, 0x80000000)

    #N0170
    NpcTalk(
        0x101,
        "琪雅",
        "#05809F#3615V#50W#12P晚安……\x02",
    )

    CloseMessageWindow()
    OP_24(0xE1F)
    OP_C9(0x1, 0x80000000)
    OP_68(12900, 1000, 13970, 5000)

    def lambda_5087():

        label("loc_5087")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5087")

    QueueWorkItem2(0x101, 2, lambda_5087)
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_50A0():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_50A0)
    WaitChrThread(0x8, 1)

    def lambda_50B9():
        OP_9B(0x0, 0xFE, 0xFFD3, 0x7D0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_50B9)
    WaitChrThread(0x8, 1)

    def lambda_50D2():
        OP_9B(0x0, 0xFE, 0xFFD3, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_50D2)
    Sleep(1200)
    EndChrThread(0x101, 0x2)
    Sleep(1000)
    Sound(121, 0, 100, 0)
    Sleep(300)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x8, 1)
    Sound(890, 0, 100, 0)
    SetChrFlags(0x8, 0x80)
    Sleep(800)
    OP_6F(0x79)

    #N0171
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#05808F#30W#6P……莉夏怎么了？\x02\x03",

            "#05812F#30W她平时的表情就有些哀伤，\x01",
            "不过刚才好像又不大一样呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#00008F#5P是吗……琪雅也看出来了啊。\x02\x03",

            "#00006F……嗯，情况比较复杂。\x02\x03",

            "#00000F总之，我会尽量\x01",
            "留意她的。\x02",
        )
    )

    CloseMessageWindow()

    #N0173
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#05809F#30W#6P嘿嘿嘿……\x01",
            "罗伊德好帅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#00011F别再捉弄我啦。\x02\x03",

            "#00004F好了……\x01",
            "我们赶快回床上睡觉吧。\x02\x03",

            "#00005F对了，去过厕所了吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0175
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#05801F#30W#6P唔唔唔……\x01",
            "罗伊德没神经！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19375, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrFlags(0xD, 0x80)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM(-1, -1)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("m3099", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_3BFB end

    def Function_14_52E3(): pass

    label("Function_14_52E3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50106.itc", 0x1E)
    LoadChrToIndex("apl/ch51423.itc", 0x1F)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SoundLoad(2913)
    SoundLoad(4107)
    SoundLoad(2759)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x5)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    SetChrPos(0x101, -104650, 550, -81450, 90)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x4)
    ClearChrFlags(0x104, 0x1)
    SetChrPos(0x104, -104650, 400, -84350, 90)
    OP_52(0x104, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x105, -104000, 300, -80000, 180)
    OP_70(0x8, 0x2)
    OP_70(0x9, 0x5)
    OP_70(0xA, 0x7)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声")

    #A0176
    AnonymousTalk(
        0xFF,
        "#2913V#2S#30W……罗伊德……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声")

    #A0177
    AnonymousTalk(
        0xFF,
        "#4107V#30W快起来啊……罗伊德……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0x100B)
    Sleep(150)
    #Sound(2078, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0178
    AnonymousTalk(
        0x101,
        "#05211F啊……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_24(0x81E)
    OP_C9(0x1, 0x80000000)
    Sound(811, 0, 20, 0)
    Sound(812, 0, 100, 0)
    OP_68(-104400, 1100, -81450, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(20500, 1500)
    OP_6F(0x79)
    OP_0D()

    #C0179
    ChrTalk(
        0x101,
        (
            "#05205F#30W#5P哎……\x02\x03",

            "#05208F……现在几点了？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x105,
        (
            "#10303F#11P大概夜里两点吧。\x02\x03",

            "#10300F你梦话说得很厉害，\x01",
            "到底怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        (
            "#05206F#5P哦，好像是做了个\x01",
            "很奇怪的梦……\x02\x03",

            "#05205F……嗯………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x6)
    Sound(898, 0, 80, 0)
    OP_74(0x9, 0x8)
    OP_71(0x9, 0x5, 0x8, 0x0, 0x8)
    OP_79(0x9)
    Sleep(300)

    #C0182
    ChrTalk(
        0x101,
        "#05211F#5P…………哎………？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(100)
    SetChrSubChip(0x101, 0x5)
    Sleep(130)
    SetChrSubChip(0x101, 0x7)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0183
    ChrTalk(
        0x104,
        "#14105F#2759V#6P#40W#17A#N怎么了……？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    SetChrSubChip(0x101, 0x5)
    Fade(500)
    OP_68(-104400, 1100, -82150, 1500)
    Sound(812, 0, 100, 0)
    OP_71(0x8, 0x2, 0x5, 0x0, 0x8)
    Sound(898, 0, 50, 0)
    SetChrSubChip(0x104, 0x1)
    SetChrPos(0x104, -104650, 550, -84550, 90)
    OP_79(0x8)
    SetChrSubChip(0x101, 0x6)
    OP_6F(0x79)
    OP_0D()
    Sleep(200)
    SetChrSubChip(0x104, 0x2)

    #C0184
    ChrTalk(
        0x101,
        (
            "#05208F#11P兰迪……\x01",
            "把你吵醒了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x104,
        (
            "#14106F#6P嗯，不用介意。\x02\x03",

            "#14101F对了……\x01",
            "阿琪怎么不见了？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x105,
        (
            "#10301F#11P你们刚才不是两个人\x01",
            "一起回来躺下的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#05206F#5P你们都注意到了啊。\x02\x03",

            "#05201F……对啊，\x01",
            "我们应该是睡在一起的……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0x105, 0x5A, 0x1F4)
    Sleep(500)

    #C0188
    ChrTalk(
        0x105,
        (
            "#10308F#5P嗯……？\x01",
            "她好像并不在房间里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x104,
        "#14100F#6P好啦，总之先去找找吧。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        "#05206F#5P嗯，不好意思，麻烦你们了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(20875, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    SetChrName("")

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人在三层寻找了一圈，\x01",
            "但找遍各处也没有发现琪雅的身影。\x02\x03",

            "之后，感知到三人气息的缇欧也走出房间，\x01",
            "并拜托女性同伴们一起寻找……\x02\x03",

            "最后，还叫来了酒店的工作人员，\x01",
            "在二层也寻找了一遍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ReplaceBGM("ed7513", "ed7564")
    SetScenarioFlags(0x22, 0)
    NewScene("t105B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_52E3 end

    def Function_15_58A4(): pass

    label("Function_15_58A4")

    EventBegin(0x1)

    #C0192
    ChrTalk(
        0x101,
        (
            "#00003F（现在就算回房间，\x01",
            "  大概也睡不着觉呢。）\x02\x03",

            "（先去休息厅平静一下头脑吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -100030, 0, 6530, 0)
    EventEnd(0x4)
    Return()

    # Function_15_58A4 end

    def Function_16_5911(): pass

    label("Function_16_5911")

    EventBegin(0x1)

    #C0193
    ChrTalk(
        0x101,
        (
            "#00006F（再怎么说，在如此深夜\x01",
            "  拜访别人也是很不妥当的。）\x02\x03",

            "（还是赶快去休息厅冷静一下吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -107740, 0, 9540, 90)
    EventEnd(0x4)
    Return()

    # Function_16_5911 end

    def Function_17_598A(): pass

    label("Function_17_598A")

    EventBegin(0x1)

    #C0194
    ChrTalk(
        0x101,
        (
            "#00006F（再怎么说，在如此深夜\x01",
            "  拜访别人也是很不妥当的。）\x02\x03",

            "（还是赶快去休息厅冷静一下吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -99710, 0, 11750, 180)
    EventEnd(0x4)
    Return()

    # Function_17_598A end

    SaveToFile()

Try(main)
