from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4820.bin",                # FileName
        "e4820",                    # MapName
        "e4820",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4820",                  # 0
        "SE制御",                 # 1
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(204, 0)                                        # 0

    ScpFunction((
        "Function_0_CC",           # 00, 0
        "Function_1_DC",           # 01, 1
        "Function_2_E1",           # 02, 2
        "Function_3_55F",          # 03, 3
        "Function_4_58D",          # 04, 4
        "Function_5_5AC",          # 05, 5
        "Function_6_5E3",          # 06, 6
    ))


    def Function_0_CC(): pass

    label("Function_0_CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_DB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_DB")

    Return()

    # Function_0_CC end

    def Function_1_DC(): pass

    label("Function_1_DC")

    OP_F0(0x1, 0x7D0)
    Return()

    # Function_1_DC end

    def Function_2_E1(): pass

    label("Function_2_E1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(941)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_68(351190, 0, 1160, 0)
    MoveCamera(31, 38, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(16000, 0)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_70(0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x0, 0x18F, 0x0, 0x20)
    ClearScenarioFlags(0x0, 0)
    Sound(940, 0, 100, 0)
    Sound(941, 2, 100, 0)
    Sound(933, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("？？？")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "へえ、これはこれは。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-14610, 0, 13590, 0)
    MoveCamera(141, -14, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(12500, 0)
    OP_71(0x0, 0x0, 0x257, 0x0, 0x20)
    Sleep(1000)
    SetMessageWindowPos(30, 140, -1, -1)
    SetChrName("ヨナ")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#02310Fハッ……\x01",
            "てめえがボクのベースを\x01",
            "滅茶苦茶にした犯人か！\x02\x03",

            "#02307Fゼッテー許さねえ！\x01",
            "吠え面かかせてやるっ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("？？？")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "あはは、威勢がいいなぁ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    OP_68(349820, 0, -5340, 0)
    MoveCamera(156, 31, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(17000, 0)
    BeginChrThread(0x8, 2, 0, 6)
    OP_71(0x1, 0x1A9, 0x20D, 0x0, 0x0)
    OP_79(0x1)
    Fade(250)
    OP_68(362840, 0, -9750, 0)
    MoveCamera(293, -7, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(5500, 0)
    BeginChrThread(0x0, 3, 0, 3)
    OP_0D()
    Sleep(600)
    BeginChrThread(0x8, 1, 0, 5)
    SetMessageWindowPos(100, 30, -1, -1)
    SetChrName("ティオの声")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10A……そこまでです。\x02",
        )
    )
    #Auto

    Sleep(1000)
    OP_57(0x0)
    OP_5A()
    OP_AD(0x0)
    ClearScenarioFlags(0x0, 0)
    SetMessageWindowPos(50, 10, -1, -1)
    SetChrName("ティオ")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#00201F大人しくタワーの制御を\x01",
            "解放してもらいましょうか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 50, -1, -1)
    SetChrName("？？？")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "うふふ、仕方ない。\x02\x03",

            "まあ、ほんの暇潰しだったし\x01",
            "愉しめたから満足かな。\x02\x03",

            "それじゃあせいぜい\x01",
            "死なないように頑張ってね㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(345290, 0, 1120, 0)
    MoveCamera(296, 25, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(14500, 0)
    BeginChrThread(0x0, 3, 0, 4)
    OP_0D()
    Sleep(500)
    Sound(222, 0, 100, 0)
    Sound(223, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(30, 130, -1, -1)
    SetChrName("ヨナ")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#02310Fああっ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_AD(0x0)
    ClearScenarioFlags(0x0, 0)
    SetMessageWindowPos(50, 10, -1, -1)
    SetChrName("ティオ")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#00207Fそちらは後です！\x01",
            "早くタワーの制御を！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopSound(941, 1000, 100)
    StopSound(933, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 2)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E1 end

    def Function_3_55F(): pass

    label("Function_3_55F")

    OP_71(0x1, 0x552, 0x574, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x1F1, 0x270, 0x0, 0x0)
    OP_79(0x1)
    SetScenarioFlags(0x0, 0)
    OP_71(0x1, 0x271, 0x2A2, 0x0, 0x20)
    Return()

    # Function_3_55F end

    def Function_4_58D(): pass

    label("Function_4_58D")

    OP_71(0x1, 0x2A3, 0x320, 0x0, 0x0)
    OP_79(0x1)
    SetScenarioFlags(0x0, 0)
    OP_71(0x1, 0x320, 0x383, 0x0, 0x20)
    Return()

    # Function_4_58D end

    def Function_5_5AC(): pass

    label("Function_5_5AC")

    Sleep(1540)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(180)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(180)
    Sound(251, 0, 50, 0)
    Sound(259, 0, 70, 0)
    Sleep(1200)
    Sound(940, 0, 100, 0)
    Return()

    # Function_5_5AC end

    def Function_6_5E3(): pass

    label("Function_6_5E3")

    Sleep(500)
    Sound(940, 0, 100, 0)
    Sleep(1000)
    Sound(935, 0, 100, 0)
    Return()

    # Function_6_5E3 end

    SaveToFile()

Try(main)
