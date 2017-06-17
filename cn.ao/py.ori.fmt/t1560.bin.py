from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1560.bin",                # FileName
        "t1560",                    # MapName
        "t1560",                    # Location
        0x0053,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 83, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1560",                  # 0
    ))

    ChipFrameInfo(160, 0)                                        # 0

    ScpFunction((
        "Function_0_A0",           # 00, 0
        "Function_1_A4",           # 01, 1
        "Function_2_B7",           # 02, 2
    ))


    def Function_0_A0(): pass

    label("Function_0_A0")

    Event(0, 2)
    Return()

    # Function_0_A0 end

    def Function_1_A4(): pass

    label("Function_1_A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_B6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B6")

    Return()

    # Function_1_A4 end

    def Function_2_B7(): pass

    label("Function_2_B7")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 1500, 0, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_121")
    SetChrPos(0x1, 300, 0, 800, 90)

    label("loc_121")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140")
    SetChrPos(0x2, 300, 0, -800, 90)

    label("loc_140")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F")
    SetChrPos(0x3, -700, 0, 0, 90)

    label("loc_15F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_188")
    SetChrPos(0x4, -1700, 0, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_188")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B1")
    SetChrPos(0x5, -1700, 0, 800, 90)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1B1")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22D")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "★【 ３Ｆ 】")
    MenuCmd(1, 0, "　【 ２Ｆ 】")
    MenuCmd(1, 0, "　【 １Ｆ 】")
    MenuCmd(1, 0, "　【离  开】")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F8")

    label("loc_22D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_295")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　【 ３Ｆ 】")
    MenuCmd(1, 0, "★【 ２Ｆ 】")
    MenuCmd(1, 0, "　【 １Ｆ 】")
    MenuCmd(1, 0, "　【离  开】")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F8")

    label("loc_295")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　【 ３Ｆ 】")
    MenuCmd(1, 0, "　【 ２Ｆ 】")
    MenuCmd(1, 0, "★【 １Ｆ 】")
    MenuCmd(1, 0, "　【离  开】")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F8")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31F")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_39C")

    label("loc_31F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_358")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_39C")

    label("loc_358")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_391")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_39C")

    label("loc_391")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_39C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FC")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3C7"),
        (1, "loc_3D7"),
        (2, "loc_3E7"),
        (SWITCH_DEFAULT, "loc_3F7"),
    )


    label("loc_3C7")

    EventEnd(0x5)
    NewScene("t1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_3F7")

    label("loc_3D7")

    EventEnd(0x5)
    NewScene("t1540", 103, 0, 0)
    IdleLoop()
    Jump("loc_3F7")

    label("loc_3E7")

    EventEnd(0x5)
    NewScene("t1530", 102, 0, 0)
    IdleLoop()
    Jump("loc_3F7")

    label("loc_3F7")

    Jump("loc_45A")

    label("loc_3FC")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_418"),
        (1, "loc_42E"),
        (2, "loc_444"),
        (SWITCH_DEFAULT, "loc_45A"),
    )


    label("loc_418")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_45A")

    label("loc_42E")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1540", 103, 0, 0)
    IdleLoop()
    Jump("loc_45A")

    label("loc_444")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1530", 102, 0, 0)
    IdleLoop()
    Jump("loc_45A")

    label("loc_45A")

    Return()

    # Function_2_B7 end

    SaveToFile()

Try(main)
