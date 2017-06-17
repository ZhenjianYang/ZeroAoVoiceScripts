from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t161b.bin",                # FileName
        "t161b",                    # MapName
        "t161b",                    # Location
        0x0054,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 84, 0, 0, 0, 1],
    )

    BuildStringList((
        "t161b",                  # 0
    ))

    ScpFunction((
        "Function_0_A4",           # 00, 0
        "Function_1_A8",           # 01, 1
        "Function_2_C1",           # 02, 2
        "Function_3_578",          # 03, 3
    ))


    def Function_0_A4(): pass

    label("Function_0_A4")

    Event(0, 2)
    Return()

    # Function_0_A4 end

    def Function_1_A8(): pass

    label("Function_1_A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0")
    SetMapObjFrame(0xFF, "on_add", 0x0, 0x1)

    label("loc_C0")

    Return()

    # Function_1_A8 end

    def Function_2_C1(): pass

    label("Function_2_C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3")
    Call(0, 3)
    Jump("loc_1DE")

    label("loc_D3")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 1500, 50, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D")
    SetChrPos(0x1, 300, 50, 800, 90)

    label("loc_13D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C")
    SetChrPos(0x2, 300, 50, -800, 90)

    label("loc_15C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17B")
    SetChrPos(0x3, -900, 50, 800, 90)

    label("loc_17B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A")
    SetChrPos(0x4, -2100, 0, -800, 90)

    label("loc_19A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B9")
    SetChrPos(0x5, -2100, 0, 800, 90)

    label("loc_1B9")

    SetChrPos(0x4, -900, 50, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    label("loc_1DE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_268")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "★【 ４Ｆ 】")
    MenuCmd(1, 0, "　【 ３Ｆ 】")
    MenuCmd(1, 0, "　【 ２Ｆ 】")
    MenuCmd(1, 0, "　【 １Ｆ 】")
    MenuCmd(1, 0, "　【降りる】")
    MenuCmd(3, 0, 0x1)
    MenuCmd(3, 0, 0x2)
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E3")

    label("loc_268")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E8")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　【 ４Ｆ 】")
    MenuCmd(1, 0, "★【 ３Ｆ 】")
    MenuCmd(1, 0, "　【 ２Ｆ 】")
    MenuCmd(1, 0, "　【 １Ｆ 】")
    MenuCmd(1, 0, "　【降りる】")
    MenuCmd(3, 0, 0x1)
    MenuCmd(3, 0, 0x2)
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E3")

    label("loc_2E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_368")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　【 ４Ｆ 】")
    MenuCmd(1, 0, "　【 ３Ｆ 】")
    MenuCmd(1, 0, "★【 ２Ｆ 】")
    MenuCmd(1, 0, "　【 １Ｆ 】")
    MenuCmd(1, 0, "　【降りる】")
    MenuCmd(3, 0, 0x1)
    MenuCmd(3, 0, 0x2)
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E3")

    label("loc_368")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E3")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　【 ４Ｆ 】")
    MenuCmd(1, 0, "　【 ３Ｆ 】")
    MenuCmd(1, 0, "　【 ２Ｆ 】")
    MenuCmd(1, 0, "★【 １Ｆ 】")
    MenuCmd(1, 0, "　【降りる】")
    MenuCmd(3, 0, 0x1)
    MenuCmd(3, 0, 0x2)
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E3")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40A")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_487")

    label("loc_40A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_443")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_487")

    label("loc_443")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47C")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_487")

    label("loc_47C")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_487")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FD")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4B8"),
        (1, "loc_4C8"),
        (2, "loc_4D8"),
        (3, "loc_4E8"),
        (SWITCH_DEFAULT, "loc_4F8"),
    )


    label("loc_4B8")

    EventEnd(0x5)
    NewScene("t165B", 117, 0, 0)
    IdleLoop()
    Jump("loc_4F8")

    label("loc_4C8")

    EventEnd(0x5)
    NewScene("t164B", 117, 0, 0)
    IdleLoop()
    Jump("loc_4F8")

    label("loc_4D8")

    EventEnd(0x5)
    NewScene("t163B", 110, 0, 0)
    IdleLoop()
    Jump("loc_4F8")

    label("loc_4E8")

    EventEnd(0x5)
    NewScene("t162B", 117, 0, 0)
    IdleLoop()
    Jump("loc_4F8")

    label("loc_4F8")

    Jump("loc_577")

    label("loc_4FD")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_51F"),
        (1, "loc_535"),
        (2, "loc_54B"),
        (3, "loc_561"),
        (SWITCH_DEFAULT, "loc_577"),
    )


    label("loc_51F")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t165B", 117, 0, 0)
    IdleLoop()
    Jump("loc_577")

    label("loc_535")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t164B", 117, 0, 0)
    IdleLoop()
    Jump("loc_577")

    label("loc_54B")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t163B", 110, 0, 0)
    IdleLoop()
    Jump("loc_577")

    label("loc_561")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t162B", 117, 0, 0)
    IdleLoop()
    Jump("loc_577")

    label("loc_577")

    Return()

    # Function_2_C1 end

    def Function_3_578(): pass

    label("Function_3_578")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 1500, 50, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E2")
    SetChrPos(0x1, 300, 50, 800, 90)

    label("loc_5E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_601")
    SetChrPos(0x2, 300, 50, -800, 90)

    label("loc_601")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_620")
    SetChrPos(0x3, -900, 50, 800, 90)

    label("loc_620")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63F")
    SetChrPos(0x4, -2100, 0, -800, 90)

    label("loc_63F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65E")
    SetChrPos(0x5, -2100, 0, 800, 90)

    label("loc_65E")

    SetChrPos(0x4, -900, 50, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターのボタンを\x01",
            "押しても何も起こらない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77D")

    #C0002
    ChrTalk(
        0x101,
        "#0005F#6Pもしかして壊れているのか？\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        (
            "#0203F#6Pいえ、何らかの理由で\x01",
            "ロックされているようですね。\x02\x03",

            "#0200F動かすためには認証用の\x01",
            "カードが必要みたいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE6, 7)
    Jump("loc_7AC")

    label("loc_77D")

    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どうやらロックされているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7AC")

    Jump("loc_8B7")

    label("loc_7B1")

    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どうやらロックされているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_823")

    #C0006
    ChrTalk(
        0x101,
        (
            "#0000F#6P（よし……\x01",
            "  さっきのカードを使おう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_823")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "認証カードを使う\x01",      # 0
            "使わない\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_877"),
        (1, "loc_899"),
        (SWITCH_DEFAULT, "loc_8B7"),
    )


    label("loc_877")

    Fade(250)
    SetMapObjFrame(0xFF, "on_add", 0x1, 0x1)
    Sound(72, 0, 100, 0)
    OP_0D()
    SetScenarioFlags(0xE3, 4)
    Jump("loc_8B7")

    label("loc_899")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    SetScenarioFlags(0x5C, 0)
    NewScene("t162B", 0, 0, 0)
    IdleLoop()
    Jump("loc_8B7")

    label("loc_8B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DA")
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    SetScenarioFlags(0x5C, 0)
    NewScene("t162B", 0, 0, 0)
    IdleLoop()

    label("loc_8DA")

    Return()

    # Function_3_578 end

    SaveToFile()

Try(main)
