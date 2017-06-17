from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1170.bin",                # FileName
        "c1170",                    # MapName
        "c1170",                    # Location
        0x0018,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 24, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1170",                  # 0
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
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 0, 0, 400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F")
    SetChrPos(0x1, -500, 0, -700, 0)

    label("loc_10F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E")
    SetChrPos(0x2, 500, 0, -700, 0)

    label("loc_12E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D")
    SetChrPos(0x3, 0, 0, -1700, 0)

    label("loc_14D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C")
    SetChrPos(0x4, -1200, 0, -1900, 0)

    label("loc_16C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B")
    SetChrPos(0x5, -1200, 0, 1900, 0)

    label("loc_18B")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC")

    Menu(
        0,
        10,
        10,
        0,
        (
            "★【 ３Ｆ 】\x01",      # 0
            "　【 １Ｆ 】\x01",      # 1
            "　【 离开 】\x01",      # 2
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_234")

    label("loc_1EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_234")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【 ３Ｆ 】\x01",      # 0
            "★【 １Ｆ 】\x01",      # 1
            "　【 离开 】\x01",      # 2
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_234")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_2D8")

    label("loc_25B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_294")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_2D8")

    label("loc_294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CD")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_2D8")

    label("loc_2CD")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_2D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_322")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2FD"),
        (1, "loc_30D"),
        (SWITCH_DEFAULT, "loc_31D"),
    )


    label("loc_2FD")

    EventEnd(0x5)
    NewScene("c1160", 100, 0, 0)
    IdleLoop()
    Jump("loc_31D")

    label("loc_30D")

    EventEnd(0x5)
    NewScene("c1150", 101, 0, 0)
    IdleLoop()
    Jump("loc_31D")

    label("loc_31D")

    Jump("loc_36A")

    label("loc_322")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_338"),
        (1, "loc_351"),
        (SWITCH_DEFAULT, "loc_36A"),
    )


    label("loc_338")

    Sound(160, 0, 100, 0)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1160", 100, 0, 0)
    IdleLoop()
    Jump("loc_36A")

    label("loc_351")

    Sound(160, 0, 100, 0)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1150", 101, 0, 0)
    IdleLoop()
    Jump("loc_36A")

    label("loc_36A")

    Return()

    # Function_2_A5 end

    SaveToFile()

Try(main)
