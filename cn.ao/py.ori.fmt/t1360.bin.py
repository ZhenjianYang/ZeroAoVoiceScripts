from ScenarioHelper import *

def main():
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
        "Function_3_553",          # 03, 3
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

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_531")
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5C), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CF")
    BeginChrThread(0x0, 1, 0, 3)
    FadeToBright(500, 0)
    OP_0D()
    SetChrName("")
    SetMessageWindowPos(120, 308, 28, 1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            "　　　要和谁一起乘坐呢？",
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
            "艾莉\x01",        # 0
            "缇欧\x01",        # 1
            "兰迪\x01",        # 2
            "瓦吉\x01",        # 3
            "诺艾尔\x01",      # 4
            "莉夏\x01",        # 5
            "琪雅\x01",        # 6
            "芙兰\x01",        # 7
            "塞茜尔\x01",      # 8
            "伊莉娅\x01",      # 9
            "修利\x01",        # 10
            "放弃\x01",        # 11
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(500, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x1)
    Jump("loc_2BF")

    label("loc_1CF")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_21A"),
        (1, "loc_229"),
        (2, "loc_238"),
        (3, "loc_247"),
        (4, "loc_256"),
        (5, "loc_265"),
        (6, "loc_274"),
        (7, "loc_283"),
        (8, "loc_292"),
        (9, "loc_2A1"),
        (10, "loc_2B0"),
        (SWITCH_DEFAULT, "loc_2BF"),
    )


    label("loc_21A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF")

    label("loc_229")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF")

    label("loc_238")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF")

    label("loc_247")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF")

    label("loc_256")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF")

    label("loc_265")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF")

    label("loc_274")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF")

    label("loc_283")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF")

    label("loc_292")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF")

    label("loc_2A1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF")

    label("loc_2B0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF")

    label("loc_2BF")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30B"),
        (1, "loc_338"),
        (2, "loc_365"),
        (3, "loc_392"),
        (4, "loc_3BF"),
        (5, "loc_3EC"),
        (6, "loc_419"),
        (7, "loc_446"),
        (8, "loc_473"),
        (9, "loc_4A0"),
        (10, "loc_4CD"),
        (SWITCH_DEFAULT, "loc_4FA"),
    )


    label("loc_30B")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504")

    label("loc_338")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504")

    label("loc_365")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504")

    label("loc_392")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504")

    label("loc_3BF")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504")

    label("loc_3EC")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504")

    label("loc_419")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504")

    label("loc_446")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504")

    label("loc_473")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504")

    label("loc_4A0")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504")

    label("loc_4CD")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_504")

    label("loc_4FA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_504")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_518")
    Jump("loc_531")

    label("loc_518")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52C")
    Jump("loc_531")

    label("loc_52C")

    Jump("Function_2_A9")

    label("loc_531")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5C), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_550")
    SetScenarioFlags(0x22, 0)
    NewScene("t1350", 0, 0, 0)
    IdleLoop()
    Jump("loc_552")

    label("loc_550")

    OP_B9(0x2)

    label("loc_552")

    Return()

    # Function_2_A9 end

    def Function_3_553(): pass

    label("Function_3_553")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57D")
    MoveCamera(350, -5, 0, 20000)
    OP_6F(0x40)
    MoveCamera(10, -5, 0, 20000)
    OP_6F(0x40)
    Jump("Function_3_553")

    label("loc_57D")

    Return()

    # Function_3_553 end

    SaveToFile()

Try(main)
