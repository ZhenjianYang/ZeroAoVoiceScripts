from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m0012.bin",                # FileName
        "m0012",                    # MapName
        "m0012",                    # Location
        0x0067,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 103, 0, 1, 0, 2],
    )

    BuildStringList((
        "m0012",                  # 0
        "MapThread",              # 1
    ))

    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-10700,  3000,    11000,   2000,    -10700,  4000,    11000,   0x007C, 0,  4,  0x0000)
    DeclActor(2500,    0,       212500,  1200,    2500,    1500,    212500,  0x007C, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_10C",          # 00, 0
        "Function_1_137",          # 01, 1
        "Function_2_138",          # 02, 2
        "Function_3_2C1",          # 03, 3
        "Function_4_3B4",          # 04, 4
    ))


    def Function_0_10C(): pass

    label("Function_0_10C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_136")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12E")
    Sound(148, 0, 100, 0)
    Sleep(900)
    Jump("loc_131")

    label("loc_12E")

    Sleep(30)

    label("loc_131")

    Jump("Function_0_10C")

    label("loc_136")

    Return()

    # Function_0_10C end

    def Function_1_137(): pass

    label("Function_1_137")

    Return()

    # Function_1_137 end

    def Function_2_138(): pass

    label("Function_2_138")

    ClearScenarioFlags(0x0, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, -30, 2960, -8450, 4000, 2000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, -6170, 2920, 5360, 4000, 2000, 135000)
    SetBarrier(0x0, 0x2, 0x1, 0x0, -110, 2970, 8410, 4000, 2000, 0)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 8310, 2800, -120, 4000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 5)), scpexpr(EXPR_END)), "loc_1F8")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetMapObjFrame(0x3, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "wing00", 0x2, "stop_kp")
    Jump("loc_269")

    label("loc_1F8")

    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetMapObjFrame(0x3, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "wing00", 0x2, "rotate")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_269")
    SetScenarioFlags(0x0, 0)

    label("loc_269")

    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    Return()

    # Function_2_138 end

    def Function_3_2C1(): pass

    label("Function_3_2C1")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_396")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x4, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x4, 0x0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x4)
    OP_71(0x4, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x4, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_396")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B2")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_3B2")

    Return()

    # Function_3_2C1 end

    def Function_4_3B4(): pass

    label("Function_4_3B4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 5)), scpexpr(EXPR_END)), "loc_3F1")
    TalkBegin(0xFF)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "换气扇已经停止了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_5A8")

    label("loc_3F1")

    EventBegin(0x1)

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有换气扇的控制装置。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A1")
    Fade(500)
    SetChrPos(0x0, -10030, 3000, 9790, 315)
    SetChrPos(0x1, -8170, 2970, 8950, 315)
    SetChrPos(0x2, -9170, 2960, 7950, 315)
    SetChrPos(0x3, -8000, 2940, 7350, 315)
    OP_68(-9740, 3960, 8470, 0)
    MoveCamera(22, 40, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    OP_0D()
    SetMapObjFrame(0x3, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)

    def lambda_4F0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4F0)
    Sleep(500)

    def lambda_500():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_500)
    Sleep(10)

    def lambda_510():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_510)
    Sleep(10)

    def lambda_520():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_520)
    Sleep(500)
    Fade(500)
    SetMapObjFrame(0xFF, "wing00", 0x2, "stop")
    OP_68(-950, 4500, -2380, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(33000, 0)
    OP_0D()
    Sleep(3200)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sound(149, 0, 100, 0)
    ClearScenarioFlags(0x0, 0)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetScenarioFlags(0x54, 5)

    label("loc_5A1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_5A8")

    Return()

    # Function_4_3B4 end

    SaveToFile()

Try(main)
