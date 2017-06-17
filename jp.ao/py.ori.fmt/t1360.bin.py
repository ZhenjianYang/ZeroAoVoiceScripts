from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1360.bin",                # FileName
        "t1360",                    # MapName
        "t1360",                    # Location
        0x00B8,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 184, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1360",                  # 0
    ))

    ChipFrameInfo(164, 0)                                        # 0

    ScpFunction((
        "Function_0_A4",           # 00, 0
        "Function_1_A8",           # 01, 1
        "Function_2_A9",           # 02, 2
        "Function_3_565",          # 03, 3
    ))


    def Function_0_A4(): pass

    label("Function_0_A4")

    Event(0, 2)
    Return()

    # Function_0_A4 end

    def Function_1_A8(): pass

    label("Function_1_A8")

    Return()

    # Function_1_A8 end

    def Function_2_A9(): pass

    label("Function_2_A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_543")
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetChrPos(0x101, 500, 300, 3, 0)
    SetChrFlags(0x101, 0x8)
    OP_68(0, 2200, 0, 0)
    MoveCamera(10, -5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(11440, 0)
    PlayBGM("ed7590", 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5C), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E1")
    BeginChrThread(0x0, 1, 0, 3)
    FadeToBright(500, 0)
    OP_0D()
    SetChrName("")
    SetMessageWindowPos(120, 308, 28, 1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            "　　　誰と乗りますか？",
            scpstr(0x18),
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        250,
        48,
        1,
        (
            "エリィ\x01",        # 0
            "ティオ\x01",        # 1
            "ランディ\x01",      # 2
            "ワジ\x01",          # 3
            "ノエル\x01",        # 4
            "リーシャ\x01",      # 5
            "キーア\x01",        # 6
            "フラン\x01",        # 7
            "セシル\x01",        # 8
            "イリア\x01",        # 9
            "シュリ\x01",        # 10
            "やめる\x01",        # 11
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(500, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x1)
    Jump("loc_2D1")

    label("loc_1E1")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_22C"),
        (1, "loc_23B"),
        (2, "loc_24A"),
        (3, "loc_259"),
        (4, "loc_268"),
        (5, "loc_277"),
        (6, "loc_286"),
        (7, "loc_295"),
        (8, "loc_2A4"),
        (9, "loc_2B3"),
        (10, "loc_2C2"),
        (SWITCH_DEFAULT, "loc_2D1"),
    )


    label("loc_22C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1")

    label("loc_23B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1")

    label("loc_24A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1")

    label("loc_259")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1")

    label("loc_268")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1")

    label("loc_277")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1")

    label("loc_286")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1")

    label("loc_295")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1")

    label("loc_2A4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1")

    label("loc_2B3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1")

    label("loc_2C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D1")

    label("loc_2D1")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31D"),
        (1, "loc_34A"),
        (2, "loc_377"),
        (3, "loc_3A4"),
        (4, "loc_3D1"),
        (5, "loc_3FE"),
        (6, "loc_42B"),
        (7, "loc_458"),
        (8, "loc_485"),
        (9, "loc_4B2"),
        (10, "loc_4DF"),
        (SWITCH_DEFAULT, "loc_50C"),
    )


    label("loc_31D")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_516")

    label("loc_34A")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_516")

    label("loc_377")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_516")

    label("loc_3A4")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_516")

    label("loc_3D1")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_516")

    label("loc_3FE")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_516")

    label("loc_42B")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_516")

    label("loc_458")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_516")

    label("loc_485")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_516")

    label("loc_4B2")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_516")

    label("loc_4DF")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_516")

    label("loc_50C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_516")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52A")
    Jump("loc_543")

    label("loc_52A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53E")
    Jump("loc_543")

    label("loc_53E")

    Jump("Function_2_A9")

    label("loc_543")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5C), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_562")
    SetScenarioFlags(0x22, 0)
    NewScene("t1350", 0, 0, 0)
    IdleLoop()
    Jump("loc_564")

    label("loc_562")

    OP_B9(0x2)

    label("loc_564")

    Return()

    # Function_2_A9 end

    def Function_3_565(): pass

    label("Function_3_565")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58F")
    MoveCamera(350, -5, 0, 20000)
    OP_6F(0x40)
    MoveCamera(10, -5, 0, 20000)
    OP_6F(0x40)
    Jump("Function_3_565")

    label("loc_58F")

    Return()

    # Function_3_565 end

    SaveToFile()

Try(main)
