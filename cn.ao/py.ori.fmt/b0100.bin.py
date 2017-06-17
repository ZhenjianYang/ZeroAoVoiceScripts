from ScenarioHelper import *

def main():
    CreateScenaFile(
        "b0100.bin",                # FileName
        "b0100",                    # MapName
        "b0100",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "b0100",                  # 0
    ))

    ChipFrameInfo(404, 0)                                        # 0

    ScpFunction((
        "Function_0_194",          # 00, 0
        "Function_1_245",          # 01, 1
        "Function_2_246",          # 02, 2
        "Function_3_557",          # 03, 3
    ))


    def Function_0_194(): pass

    label("Function_0_194")

    Event(0, 2)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis120.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x1, "c_vis120.itp")
    OP_C9(0x0, 0x10)
    SetMapFlags(0x80)
    OP_16(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x20), scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_214")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_214")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x20), scpexpr(EXPR_PUSH_LONG, 0x239), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x239), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x20), scpexpr(EXPR_PUSH_LONG, 0x245), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_244")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x245), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_244")

    Return()

    # Function_0_194 end

    def Function_1_245(): pass

    label("Function_1_245")

    Return()

    # Function_1_245 end

    def Function_2_246(): pass

    label("Function_2_246")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0xC8, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0x0, 0x1F4, 0x0, 0x0)
    Sleep(100)
    ClearMapFlags(0x2000000)
    SetChrName("")
    SetMessageWindowPos(120, 0, 28, 1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            "　　　　　事件一览　　",
            scpstr(0x18),
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E0(0x28, 0x1)"), scpexpr(EXPR_END)), "loc_2BE")
    MenuCmd(1, 0, "与艾莉的羁绊")
    Jump("loc_2D2")

    label("loc_2BE")

    MenuCmd(1, 0, "？？？？？？")
    MenuCmd(3, 0, 0x0)

    label("loc_2D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E0(0x29, 0x1)"), scpexpr(EXPR_END)), "loc_2F1")
    MenuCmd(1, 0, "与缇欧的羁绊")
    Jump("loc_305")

    label("loc_2F1")

    MenuCmd(1, 0, "？？？？？？")
    MenuCmd(3, 0, 0x1)

    label("loc_305")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E0(0x2A, 0x1)"), scpexpr(EXPR_END)), "loc_324")
    MenuCmd(1, 0, "与兰迪的羁绊")
    Jump("loc_338")

    label("loc_324")

    MenuCmd(1, 0, "？？？？？？")
    MenuCmd(3, 0, 0x2)

    label("loc_338")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E0(0x25, 0x1)"), scpexpr(EXPR_END)), "loc_359")
    MenuCmd(1, 0, "与诺艾尔的羁绊")
    Jump("loc_36D")

    label("loc_359")

    MenuCmd(1, 0, "？？？？？？")
    MenuCmd(3, 0, 0x3)

    label("loc_36D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E0(0x26, 0x1)"), scpexpr(EXPR_END)), "loc_38C")
    MenuCmd(1, 0, "与瓦吉的羁绊")
    Jump("loc_3A0")

    label("loc_38C")

    MenuCmd(1, 0, "？？？？？？")
    MenuCmd(3, 0, 0x4)

    label("loc_3A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E0(0x27, 0x1)"), scpexpr(EXPR_END)), "loc_3BF")
    MenuCmd(1, 0, "与莉夏的羁绊")
    Jump("loc_3D3")

    label("loc_3BF")

    MenuCmd(1, 0, "？？？？？？")
    MenuCmd(3, 0, 0x5)

    label("loc_3D3")

    MenuCmd(1, 0, "返回")
    MenuCmd(4, 0, 0x3)
    MenuCmd(2, 0, -1, 56, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_3F9")
    MenuCmd(5, 0, 0x0)
    Jump("loc_44E")

    label("loc_3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_40B")
    MenuCmd(5, 0, 0x1)
    Jump("loc_44E")

    label("loc_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_41D")
    MenuCmd(5, 0, 0x2)
    Jump("loc_44E")

    label("loc_41D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_42F")
    MenuCmd(5, 0, 0x3)
    Jump("loc_44E")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_441")
    MenuCmd(5, 0, 0x4)
    Jump("loc_44E")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_44E")
    MenuCmd(5, 0, 0x5)

    label("loc_44E")

    ClearScenarioFlags(0x22, 0)
    ClearScenarioFlags(0x1AA, 3)
    ClearScenarioFlags(0x1AA, 4)
    ClearScenarioFlags(0x1AA, 5)
    ClearScenarioFlags(0x1AA, 6)
    ClearScenarioFlags(0x1AA, 7)
    ClearScenarioFlags(0x1AB, 0)
    MenuEnd(0x0)
    MenuCmd(6, 1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_497"),
        (1, "loc_4AE"),
        (2, "loc_4C5"),
        (3, "loc_4DC"),
        (4, "loc_4F3"),
        (5, "loc_50A"),
        (SWITCH_DEFAULT, "loc_521"),
    )


    label("loc_497")

    SetScenarioFlags(0x22, 0)
    SetScenarioFlags(0x1AA, 3)
    Call(0, 3)
    NewScene("e440B", 0, 0, 0)
    IdleLoop()
    Jump("loc_556")

    label("loc_4AE")

    SetScenarioFlags(0x22, 0)
    SetScenarioFlags(0x1AA, 4)
    Call(0, 3)
    NewScene("e440B", 0, 0, 0)
    IdleLoop()
    Jump("loc_556")

    label("loc_4C5")

    SetScenarioFlags(0x22, 0)
    SetScenarioFlags(0x1AA, 5)
    Call(0, 3)
    NewScene("e440B", 0, 0, 0)
    IdleLoop()
    Jump("loc_556")

    label("loc_4DC")

    SetScenarioFlags(0x22, 0)
    SetScenarioFlags(0x1AA, 6)
    Call(0, 3)
    NewScene("e440B", 0, 0, 0)
    IdleLoop()
    Jump("loc_556")

    label("loc_4F3")

    SetScenarioFlags(0x22, 0)
    SetScenarioFlags(0x1AA, 7)
    Call(0, 3)
    NewScene("e440B", 0, 0, 0)
    IdleLoop()
    Jump("loc_556")

    label("loc_50A")

    SetScenarioFlags(0x22, 0)
    SetScenarioFlags(0x1AB, 0)
    Call(0, 3)
    NewScene("e440B", 0, 0, 0)
    IdleLoop()
    Jump("loc_556")

    label("loc_521")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(1000)
    OP_B9(0x2)
    Jump("loc_556")

    label("loc_556")

    Return()

    # Function_2_246 end

    def Function_3_557(): pass

    label("Function_3_557")

    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    StopBGM(0x3E8)
    Sleep(500)
    OP_C9(0x1, 0x10)
    Return()

    # Function_3_557 end

    SaveToFile()

Try(main)
