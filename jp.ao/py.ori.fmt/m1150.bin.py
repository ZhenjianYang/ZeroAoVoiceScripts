from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1150.bin",                # FileName
        "m1150",                    # MapName
        "m1150",                    # Location
        0x0073,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 115, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1150",                  # 0
    ))

    DeclActor(0,       7200,    -34700,  1200,    0,       8700,    -34700,  0x007C, 0,  2,  0x0000)

    ChipFrameInfo(200, 0)                                        # 0

    ScpFunction((
        "Function_0_C8",           # 00, 0
        "Function_1_D8",           # 01, 1
        "Function_2_13B",          # 02, 2
        "Function_3_172",          # 03, 3
    ))


    def Function_0_C8(): pass

    label("Function_0_C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)

    label("loc_D7")

    Return()

    # Function_0_C8 end

    def Function_1_D8(): pass

    label("Function_1_D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_111")
    SetMapObjFlags(0x1, 0x10)
    SetMapObjFlags(0x2, 0x4)
    OP_65(0x0, 0x1)
    Jump("loc_13A")

    label("loc_111")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_134")
    SetMapObjFlags(0x1, 0x10)
    SetMapObjFlags(0x2, 0x4)
    OP_65(0x0, 0x1)
    Jump("loc_13A")

    label("loc_134")

    ClearMapObjFlags(0x1, 0x10)

    label("loc_13A")

    Return()

    # Function_1_D8 end

    def Function_2_13B(): pass

    label("Function_2_13B")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は結界によって封じられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_2_13B end

    def Function_3_172(): pass

    label("Function_3_172")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x2, 0x4)
    OP_68(1770, 8400, -33450, 0)
    MoveCamera(36, 16, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(30730, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    SetMapObjFlags(0x2, 0x4)
    SetCameraDistance(29730, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 0)
    NewScene("m1140", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_172 end

    SaveToFile()

Try(main)
