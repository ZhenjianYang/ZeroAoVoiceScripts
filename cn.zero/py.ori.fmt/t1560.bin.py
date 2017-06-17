from ZeroScenarioHelper import *

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
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 83, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1560",                  # 0
    ))

    ScpFunction((
        "Function_0_A0",           # 00, 0
        "Function_1_A4",           # 01, 1
        "Function_2_F4",           # 02, 2
    ))


    def Function_0_A0(): pass

    label("Function_0_A0")

    Event(0, 2)
    Return()

    # Function_0_A0 end

    def Function_1_A4(): pass

    label("Function_1_A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_F3")

    label("loc_C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_F3")

    label("loc_DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_F3")

    Return()

    # Function_1_A4 end

    def Function_2_F4(): pass

    label("Function_2_F4")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 1500, 50, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E")
    SetChrPos(0x1, 300, 50, 800, 90)

    label("loc_15E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17D")
    SetChrPos(0x2, 300, 50, -800, 90)

    label("loc_17D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C")
    SetChrPos(0x3, -900, 50, 0, 90)

    label("loc_19C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB")
    SetChrPos(0x4, -2100, 0, -800, 90)

    label("loc_1BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA")
    SetChrPos(0x5, -2100, 0, 800, 90)

    label("loc_1DA")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_256")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "★【 ３Ｆ 】")
    MenuCmd(1, 0, "　【 ２Ｆ 】")
    MenuCmd(1, 0, "　【 １Ｆ 】")
    MenuCmd(1, 0, "　【 离开 】")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_321")

    label("loc_256")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　【 ３Ｆ 】")
    MenuCmd(1, 0, "★【 ２Ｆ 】")
    MenuCmd(1, 0, "　【 １Ｆ 】")
    MenuCmd(1, 0, "　【 离开 】")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_321")

    label("loc_2BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_321")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　【 ３Ｆ 】")
    MenuCmd(1, 0, "　【 ２Ｆ 】")
    MenuCmd(1, 0, "★【 １Ｆ 】")
    MenuCmd(1, 0, "　【 离开 】")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_321")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_348")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_3C5")

    label("loc_348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_381")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_3C5")

    label("loc_381")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BA")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_3C5")

    label("loc_3BA")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_3C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_425")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3F0"),
        (1, "loc_400"),
        (2, "loc_410"),
        (SWITCH_DEFAULT, "loc_420"),
    )


    label("loc_3F0")

    EventEnd(0x5)
    NewScene("t1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_420")

    label("loc_400")

    EventEnd(0x5)
    NewScene("t1540", 103, 0, 0)
    IdleLoop()
    Jump("loc_420")

    label("loc_410")

    EventEnd(0x5)
    NewScene("t1530", 102, 0, 0)
    IdleLoop()
    Jump("loc_420")

    label("loc_420")

    Jump("loc_483")

    label("loc_425")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_441"),
        (1, "loc_457"),
        (2, "loc_46D"),
        (SWITCH_DEFAULT, "loc_483"),
    )


    label("loc_441")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_483")

    label("loc_457")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1540", 103, 0, 0)
    IdleLoop()
    Jump("loc_483")

    label("loc_46D")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1530", 102, 0, 0)
    IdleLoop()
    Jump("loc_483")

    label("loc_483")

    Return()

    # Function_2_F4 end

    SaveToFile()

Try(main)
