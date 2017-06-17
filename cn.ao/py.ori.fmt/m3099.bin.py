from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m3099.bin",                # FileName
        "m3099",                    # MapName
        "m3099",                    # Location
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
        "m3099",                  # 0
        "魔人约亚西姆",           # 1
        "SE控制",                 # 2
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(224, 0)                                        # 0

    ScpFunction((
        "Function_0_E0",           # 00, 0
        "Function_1_F0",           # 01, 1
        "Function_2_F1",           # 02, 2
        "Function_3_5C0",          # 03, 3
        "Function_4_5E5",          # 04, 4
    ))


    def Function_0_E0(): pass

    label("Function_0_E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_EF")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_EF")

    Return()

    # Function_0_E0 end

    def Function_1_F0(): pass

    label("Function_1_F0")

    Return()

    # Function_1_F0 end

    def Function_2_F1(): pass

    label("Function_2_F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    LoadChrToIndex("apl/ch50548.itc", 0x1E)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis064.itp")
    LoadEffect(0x0, "event\\ev620_00.eff")
    LoadEffect(0x1, "event\\ev614_01.eff")
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    OP_49()
    SetChrPos(0x8, -2000, 0, -8000, 0)
    OP_D5(0x8, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0xF1, 0x118, 0x0, 0x20)
    PlayEffect(0x0, 0x6, 0x8, 0x0, -3300, 0, 3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x7, 0x8, 0x0, -3600, 0, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x101, -11300, 1000, -7000, 90)
    SetChrPos(0x102, -12200, 1000, -5600, 90)
    SetChrPos(0x103, -12700, 1000, -9400, 90)
    SetChrPos(0x104, -13400, 1000, -7900, 90)
    ClearChrFlags(0x101, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x1)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x102, 0x10)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x3)
    ClearChrFlags(0x103, 0x1)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x103, 0x10)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x2)
    ClearChrFlags(0x104, 0x1)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x1)
    PlayEffect(0x1, 0x0, 0x101, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0x1, 0x102, 0x0, 0, -1000, 0, 30, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0x2, 0x103, 0x0, 0, -1000, 0, 70, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0x3, 0x104, 0x0, 0, -1000, 0, 130, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "normal0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "broken0", 0x1, 0x1)
    BeginChrThread(0x8, 3, 0, 3)
    OP_7D(0xFF, 0x6E, 0x64, 0x0, 0x0)
    OP_11(0xA0, 0x0, 0x2D, 0xF, 0x3C, 0x0)
    OP_68(-9300, 1500, -8000, 0)
    MoveCamera(47, 17, -5, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    BeginChrThread(0x9, 1, 0, 4)
    Sound(961, 2, 50, 0)
    MoveCamera(57, 17, -20, 11000)
    SetCameraDistance(14500, 11000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    #N0001
    NpcTalk(
        0x102,
        "　",
        "#20A#00117F#6P#50W　　　　　　\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)

    #N0002
    NpcTalk(
        0x104,
        "　",
        (
            "#25A#6P#00317F#50W　　　　\x01",
            "　　　　　　　　　\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)

    #N0003
    NpcTalk(
        0x103,
        "　",
        "#20A#6P#00217F#50W　　　　　　\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)

    #N0004
    NpcTalk(
        0x101,
        "　",
        (
            "#20A#6P#00016F#50W　　　　　　　　　　\x01",
            "　　　　　　　\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(1000)
    EndChrThread(0x9, 0x1)
    FadeToDark(2000, 16711680, -1)
    OP_0D()
    StopSound(961, 1000, 50)
    OP_68(-9300, 100500, -8000, 0)
    MoveCamera(57, -90, -20, 0)
    Sleep(500)
    FadeToBright(500, 16711680)
    OP_0D()
    FadeToDark(0, 0, -1)
    Sound(824, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Sound(4130, 255, 80, 0)    #voice#KeA
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(3000)
    ReplaceBGM("ed7513", "ed7000")
    SetScenarioFlags(0x22, 2)
    NewScene("t108B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_F1 end

    def Function_3_5C0(): pass

    label("Function_3_5C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E4")
    OP_82(0x0, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_3_5C0")

    label("loc_5E4")

    Return()

    # Function_3_5C0 end

    def Function_4_5E5(): pass

    label("Function_4_5E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FE")
    Sound(824, 0, 40, 0)
    Sleep(1800)
    Jump("Function_4_5E5")

    label("loc_5FE")

    Return()

    # Function_4_5E5 end

    SaveToFile()

Try(main)
