from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1610.bin",                # FileName
        "t1610",                    # MapName
        "t1610",                    # Location
        0x0054,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 84, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1610",                  # 0
    ))

    ScpFunction((
        "Function_0_A0",           # 00, 0
        "Function_1_A4",           # 01, 1
        "Function_2_A5",           # 02, 2
    ))


    def Function_0_A0(): pass

    label("Function_0_A0")

    Event(0, 2)
    Return()

    # Function_0_A0 end

    def Function_1_A4(): pass

    label("Function_1_A4")

    Return()

    # Function_1_A4 end

    def Function_2_A5(): pass

    label("Function_2_A5")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 1500, 50, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F")
    SetChrPos(0x1, 300, 50, 800, 90)

    label("loc_10F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E")
    SetChrPos(0x2, 300, 50, -800, 90)

    label("loc_12E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D")
    SetChrPos(0x3, -900, 50, 0, 90)

    label("loc_14D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C")
    SetChrPos(0x4, -2100, 0, -800, 90)

    label("loc_16C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B")
    SetChrPos(0x5, -2100, 0, 800, 90)

    label("loc_18B")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_217")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "★【 ４Ｆ 】")
    MenuCmd(1, 0, "　【 ３Ｆ 】")
    MenuCmd(1, 0, "　【 ２Ｆ 】")
    MenuCmd(1, 0, "　【 １Ｆ 】")
    MenuCmd(1, 0, "　【 离开 】")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37A")

    label("loc_217")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28F")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　【 ４Ｆ 】")
    MenuCmd(1, 0, "★【 ３Ｆ 】")
    MenuCmd(1, 0, "　【 ２Ｆ 】")
    MenuCmd(1, 0, "　【 １Ｆ 】")
    MenuCmd(1, 0, "　【 离开 】")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37A")

    label("loc_28F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_307")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　【 ４Ｆ 】")
    MenuCmd(1, 0, "　【 ３Ｆ 】")
    MenuCmd(1, 0, "★【 ２Ｆ 】")
    MenuCmd(1, 0, "　【 １Ｆ 】")
    MenuCmd(1, 0, "　【 离开 】")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37A")

    label("loc_307")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　【 ４Ｆ 】")
    MenuCmd(1, 0, "　【 ３Ｆ 】")
    MenuCmd(1, 0, "　【 ２Ｆ 】")
    MenuCmd(1, 0, "★【 １Ｆ 】")
    MenuCmd(1, 0, "　【 离开 】")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37A")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_41E")

    label("loc_3A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3DA")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_41E")

    label("loc_3DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_413")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_41E")

    label("loc_413")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_41E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_494")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_44F"),
        (1, "loc_45F"),
        (2, "loc_46F"),
        (3, "loc_47F"),
        (SWITCH_DEFAULT, "loc_48F"),
    )


    label("loc_44F")

    EventEnd(0x5)
    NewScene("t1650", 117, 0, 0)
    IdleLoop()
    Jump("loc_48F")

    label("loc_45F")

    EventEnd(0x5)
    NewScene("t1640", 117, 0, 0)
    IdleLoop()
    Jump("loc_48F")

    label("loc_46F")

    EventEnd(0x5)
    NewScene("t1630", 110, 0, 0)
    IdleLoop()
    Jump("loc_48F")

    label("loc_47F")

    EventEnd(0x5)
    NewScene("t1620", 117, 0, 0)
    IdleLoop()
    Jump("loc_48F")

    label("loc_48F")

    Jump("loc_51A")

    label("loc_494")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4B6"),
        (1, "loc_4CF"),
        (2, "loc_4E8"),
        (3, "loc_501"),
        (SWITCH_DEFAULT, "loc_51A"),
    )


    label("loc_4B6")

    Sound(160, 0, 100, 0)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1650", 117, 0, 0)
    IdleLoop()
    Jump("loc_51A")

    label("loc_4CF")

    Sound(160, 0, 100, 0)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1640", 117, 0, 0)
    IdleLoop()
    Jump("loc_51A")

    label("loc_4E8")

    Sound(160, 0, 100, 0)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1630", 110, 0, 0)
    IdleLoop()
    Jump("loc_51A")

    label("loc_501")

    Sound(160, 0, 100, 0)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1620", 117, 0, 0)
    IdleLoop()
    Jump("loc_51A")

    label("loc_51A")

    Return()

    # Function_2_A5 end

    SaveToFile()

Try(main)
