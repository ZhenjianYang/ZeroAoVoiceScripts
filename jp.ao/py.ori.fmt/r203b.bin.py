from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r203b.bin",                # FileName
        "r203b",                    # MapName
        "r203b",                    # Location
        0x0062,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x13,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 0, 0, 1],
    )

    BuildStringList((
        "r203b",                  # 0
        "グレイス",               # 1
        "レインズ",               # 2
        "警備隊員",               # 3
        "警備隊員",               # 4
        "警備隊員",               # 5
        "警備隊員",               # 6
        "警備隊員",               # 7
        "警備隊員",               # 8
        "警備隊員",               # 9
        "猟兵",                   # 10
        "猟兵",                   # 11
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(492, 0)                                        # 0

    ScpFunction((
        "Function_0_1EC",          # 00, 0
        "Function_1_1FC",          # 01, 1
        "Function_2_226",          # 02, 2
        "Function_3_7D0",          # 03, 3
        "Function_4_90A",          # 04, 4
        "Function_5_943",          # 05, 5
        "Function_6_98A",          # 06, 6
        "Function_7_9D1",          # 07, 7
        "Function_8_A01",          # 08, 8
    ))


    def Function_0_1EC(): pass

    label("Function_0_1EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1FB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_1FB")

    Return()

    # Function_0_1EC end

    def Function_1_1FC(): pass

    label("Function_1_1FC")

    SoundDistance(0x7A, 0xFFFF2C20, 0x0, 0x3087C, 0x2710, 0x13880, 0x64, 0x0)
    OP_E3(0xFFFFADBC, 0x0, 0x20E54)
    Return()

    # Function_1_1FC end

    def Function_2_226(): pass

    label("Function_2_226")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("apl/ch50314.itc", 0x1F)
    LoadChrToIndex("apl/ch50378.itc", 0x20)
    LoadChrToIndex("chr/ch31250.itc", 0x23)
    LoadChrToIndex("apl/ch50123.itc", 0x24)
    LoadChrToIndex("chr/ch41950.itc", 0x28)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -38000, 0, 121800, 315)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -39750, 0, 119500, 315)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -27300, 0, 112800, 225)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -35400, 0, 115450, 135)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -32750, 0, 95650, 315)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -43850, 6000, 63300, 300)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -41500, 6850, 62300, 300)
    SetChrChipByIndex(0x11, 0x28)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -63570, 0, 149380, 135)
    SetChrChipByIndex(0x12, 0x28)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -65410, 0, 148410, 135)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -49950, 6000, 67400, 15)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -50400, 6000, 69550, 15)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    SetMapObjFrame(0x1, "mark01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetMapObjFrame(0x2, "mark01", 0x0, 0x1)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetMapObjFrame(0x3, "mark01", 0x0, 0x1)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    SetMapObjFrame(0x4, "mark01", 0x0, 0x1)
    OP_68(-92140, 10600, 218400, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_68(-91350, 10600, 216400, 4000)
    SetCameraDistance(25000, 4000)
    PlayBGM("ed7571", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x23B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-64550, 1200, 148820, 0)
    MoveCamera(15, 20, 0, 0)
    SetCameraDistance(15500, 0)
    MoveCamera(20, 22, 0, 6000)
    SetCameraDistance(27000, 6000)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-45810, 1300, 125000, 0)
    MoveCamera(20, 25, 0, 0)
    SetCameraDistance(25400, 0)
    OP_68(-31320, 1300, 111920, 8000)
    MoveCamera(52, 19, 0, 8000)
    SetCameraDistance(28000, 8000)
    BeginChrThread(0xC, 3, 0, 4)
    BeginChrThread(0xD, 3, 0, 5)
    BeginChrThread(0xE, 3, 0, 6)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-50290, 7400, 68960, 0)
    MoveCamera(15, 15, 0, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17500, 3000)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 3, 0, 3)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    OP_68(-49850, 7400, 67550, 3000)
    MoveCamera(15, 22, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(18000, 3000)
    BeginChrThread(0xF, 3, 0, 7)
    BeginChrThread(0x10, 3, 0, 8)
    WaitChrThread(0xF, 3)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x20)

    def lambda_602():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_602)
    WaitChrThread(0x10, 3)
    TurnDirection(0x8, 0x10, 500)
    OP_6F(0x79)
    Sleep(1000)

    def lambda_61F():

        label("loc_61F")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_61F")

    QueueWorkItem2(0x8, 2, lambda_61F)
    OP_95(0x10, -50400, 6000, 66000, 2000, 0x0)
    OP_95(0x10, -51150, 6000, 67800, 2000, 0x0)
    TurnDirection(0x10, 0x8, 500)
    Sleep(500)
    Sound(811, 0, 40, 0)

    def lambda_669():
        OP_95(0xFE, -50750, 6000, 67700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_669)
    EndChrThread(0x8, 0x2)
    OP_93(0x8, 0x64, 0x0)
    Sleep(100)
    OP_95(0x8, -49600, 6000, 67350, 5000, 0x0)
    TurnDirection(0x8, 0x10, 500)
    Sleep(500)
    OP_63(0x8, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    Sound(25, 0, 100, 0)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x3E8, 0x1F40)
    Sleep(500)
    OP_93(0x8, 0x64, 0x0)
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    SetCameraDistance(20000, 3000)

    def lambda_720():

        label("loc_720")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_720")

    QueueWorkItem2(0x9, 2, lambda_720)

    def lambda_732():

        label("loc_732")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_732")

    QueueWorkItem2(0xF, 2, lambda_732)

    def lambda_744():
        OP_95(0xFE, -45000, 6000, 60750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_744)
    Sleep(250)

    def lambda_761():
        OP_95(0xFE, -45000, 6000, 60750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_761)
    Sleep(250)
    EndChrThread(0x9, 0x2)

    def lambda_782():
        OP_95(0xFE, -45000, 6000, 60750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_782)
    Sleep(1500)
    EndChrThread(0xF, 0x2)

    def lambda_7A3():
        OP_95(0xFE, -45000, 6000, 60750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7A3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c150B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_226 end

    def Function_3_7D0(): pass

    label("Function_3_7D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_909")
    SetChrChipByIndex(0xFE, 0x20)
    OP_96(0xFE, 0xFFFF3D14, 0x1770, 0x10EB4, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    Sound(810, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    SetChrChipByIndex(0xFE, 0x20)
    OP_96(0xFE, 0xFFFF38C8, 0x1770, 0x110A8, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    Sound(810, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    SetChrChipByIndex(0xFE, 0x20)
    OP_96(0xFE, 0xFFFF3B20, 0x1770, 0x10FAE, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    Sound(810, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Jump("Function_3_7D0")

    label("loc_909")

    Return()

    # Function_3_7D0 end

    def Function_4_90A(): pass

    label("Function_4_90A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_942")
    OP_93(0xFE, 0x13B, 0x64)
    Sleep(1000)
    OP_93(0xFE, 0xE1, 0x64)
    Sleep(1000)
    OP_93(0xFE, 0x87, 0x64)
    Sleep(1000)
    OP_93(0xFE, 0xE1, 0x64)
    Sleep(1000)
    Jump("Function_4_90A")

    label("loc_942")

    Return()

    # Function_4_90A end

    def Function_5_943(): pass

    label("Function_5_943")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_989")
    OP_95(0xFE, -23800, 0, 103800, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    OP_95(0xFE, -35400, 0, 115450, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Jump("Function_5_943")

    label("loc_989")

    Return()

    # Function_5_943 end

    def Function_6_98A(): pass

    label("Function_6_98A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D0")
    OP_95(0xFE, -35750, 0, 111500, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    OP_95(0xFE, -30750, 0, 93650, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Jump("Function_6_98A")

    label("loc_9D0")

    Return()

    # Function_6_98A end

    def Function_7_9D1(): pass

    label("Function_7_9D1")

    OP_95(0xFE, -44300, 6000, 63600, 3000, 0x0)
    OP_95(0xFE, -48850, 6000, 68900, 3000, 0x0)
    TurnDirection(0xFE, 0x9, 500)
    Return()

    # Function_7_9D1 end

    def Function_8_A01(): pass

    label("Function_8_A01")

    OP_95(0xFE, -44300, 6000, 63600, 3000, 0x0)
    OP_95(0xFE, -48500, 6000, 67000, 3000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_8_A01 end

    SaveToFile()

Try(main)
