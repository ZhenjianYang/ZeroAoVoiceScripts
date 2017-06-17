from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1210.bin",                # FileName
        "t1210",                    # MapName
        "t1210",                    # Location
        0x004A,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 74, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1210",                  # 0
    ))

    DeclActor(65000,   0,       -4500,   1200,    65000,   1500,    -4500,   0x007C, 0,  2,  0x0000)
    DeclActor(-49500,  0,       -2500,   1200,    -49500,  1500,    -2500,   0x007C, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_EC",           # 00, 0
        "Function_1_ED",           # 01, 1
        "Function_2_EE",           # 02, 2
        "Function_3_1E1",          # 03, 3
    ))


    def Function_0_EC(): pass

    label("Function_0_EC")

    Return()

    # Function_0_EC end

    def Function_1_ED(): pass

    label("Function_1_ED")

    Return()

    # Function_1_ED end

    def Function_2_EE(): pass

    label("Function_2_EE")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C3")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x2, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x2, 0x0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x2, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1DF")

    Return()

    # Function_2_EE end

    def Function_3_1E1(): pass

    label("Function_3_1E1")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0002
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B6")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x3, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x3, 0x0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x3, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D2")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2D2")

    Return()

    # Function_3_1E1 end

    SaveToFile()

Try(main)
