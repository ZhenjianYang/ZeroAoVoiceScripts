from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0102.bin",                # FileName
        "m0102",                    # MapName
        "m0102",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 104, 0, 1, 0, 2],
    )

    BuildStringList((
        "m0102",                  # 0
        "アイスコンドル",         # 1
        "アイスコンドル",         # 2
        "アイスコンドル",         # 3
        "アイスコンドル",         # 4
        "アイスコンドル",         # 5
        "アイスコンドル",         # 6
        "アイスコンドル",         # 7
        "アイスコンドル",         # 8
        "bm0100",                 # 9
    ))

    ATBonus("ATBonus_208", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_248", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_24C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_250", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_254", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_258", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_25C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_260", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2E8", 0x0002, 255, 6, 45, 3, 3, 30, 0, "bm0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73200.dat", "ms73200.dat", "ms73200.dat", "ms73200.dat", "ms73200.dat", "ms73200.dat", "ms73200.dat", "ms73200.dat", "MonsterBattlePostion_248", "MonsterBattlePostion_2C8", "ed7451", "ed7453", "ATBonus_208"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 4,   -7.0,                  0.0,                   -1.0,                  144.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   2.3333334922790527,    -0.0,                  0.20000001788139343,   1.0])

    DeclActor(6670,    0,       -7120,   1200,    8890,    -8000,   -10760,  0x007C, 0,  3,  0x0000)

    ChipFrameInfo(840, 0)                                        # 0

    ScpFunction((
        "Function_0_348",          # 00, 0
        "Function_1_365",          # 01, 1
        "Function_2_366",          # 02, 2
        "Function_3_405",          # 03, 3
        "Function_4_4D9",          # 04, 4
        "Function_5_C0F",          # 05, 5
        "Function_6_C2E",          # 06, 6
    ))


    def Function_0_348(): pass

    label("Function_0_348")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_364")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_348")

    label("loc_364")

    Return()

    # Function_0_348 end

    def Function_1_365(): pass

    label("Function_1_365")

    Return()

    # Function_1_365 end

    def Function_2_366(): pass

    label("Function_2_366")

    SetMapFlags(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37F")
    VolumeBGM(0x64, 0x64)

    label("loc_37F")

    Sound(122, 1, 100, 0)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_39D")

    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 8890, -8000, -10760, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_2_366 end

    def Function_3_405(): pass

    label("Function_3_405")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0001
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(5850, 0, -9360, 1500)
    MoveCamera(50, 58, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(21500, 1500)
    Sleep(1000)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D4")
    OP_E2(0x2)
    MiniGame(0x6, 0x3, 0x1A0E, 0x0, 0xFFFFE430, 0xB4, 0x22BA, 0xFFFFE0C0, 0xFFFFD5F8)

    label("loc_4D4")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_3_405 end

    def Function_4_4D9(): pass

    label("Function_4_4D9")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    LoadChrToIndex("chr/ch00950.itc", 0x23)
    LoadChrToIndex("monster/ch73250.itc", 0x24)
    LoadChrToIndex("monster/ch73252.itc", 0x25)
    SetChrPos(0x101, -3700, 0, -600, 90)
    SetChrPos(0x102, -3700, 0, 600, 90)
    SetChrPos(0x104, -5000, 0, -1400, 90)
    SetChrPos(0x109, -5000, 0, 1400, 90)
    SetChrPos(0x105, -6300, 0, -600, 90)
    SetChrPos(0x10A, -6300, 0, 600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x1)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x1)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x1)
    SetChrFlags(0xD, 0x20)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x1)
    SetChrFlags(0xE, 0x20)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x1)
    SetChrFlags(0xF, 0x20)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-2500, 1000, 0, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)

    def lambda_798():
        OP_97(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_798)
    Sleep(50)

    def lambda_7B5():
        OP_97(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7B5)
    Sleep(50)

    def lambda_7D2():
        OP_97(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7D2)
    Sleep(50)

    def lambda_7EF():
        OP_97(0x109, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7EF)
    Sleep(50)

    def lambda_80C():
        OP_97(0x105, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_80C)
    Sleep(50)

    def lambda_829():
        OP_97(0x10A, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_829)
    OP_68(500, 1000, 0, 2500)
    SetCameraDistance(19000, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8B3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8B3)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8D8():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8D8)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8FD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8FD)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_922():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_922)
    Sleep(1000)
    WaitChrThread(0x10A, 0)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x10A, 0x23)
    SetChrSubChip(0x10A, 0x0)
    OP_0D()
    OP_68(500, 100, 0, 3000)
    MoveCamera(20, 25, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(27500, 3000)
    SetChrPos(0x8, -10000, -5000, -8000, 45)
    SetChrPos(0x9, -8000, -5000, -10000, 45)
    SetChrPos(0xA, 7500, -5000, 10000, 225)
    SetChrPos(0xB, 10000, -5000, 7500, 225)
    SetChrPos(0xC, 10000, -5000, -7000, 315)
    SetChrPos(0xD, 7000, -5000, -10000, 315)
    SetChrPos(0xE, -7000, -5000, 9500, 135)
    SetChrPos(0xF, -9500, -5000, 7000, 135)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    BeginChrThread(0x8, 3, 0, 5)
    BeginChrThread(0x8, 0, 0, 0)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 5)
    BeginChrThread(0xF, 0, 0, 0)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 5)
    BeginChrThread(0xA, 0, 0, 0)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 5)
    BeginChrThread(0xD, 0, 0, 0)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 5)
    BeginChrThread(0x9, 0, 0, 0)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 5)
    BeginChrThread(0xE, 0, 0, 0)
    Sleep(100)
    BeginChrThread(0xB, 3, 0, 5)
    BeginChrThread(0xB, 0, 0, 0)
    Sleep(50)
    BeginChrThread(0xC, 3, 0, 5)
    BeginChrThread(0xC, 0, 0, 0)
    WaitChrThread(0x8, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    Sleep(1000)
    OP_6F(0x79)
    BlurSwitch(0x5DC, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(500, 1100, 0, 1500)
    SetCameraDistance(11500, 1500)
    BeginChrThread(0x8, 3, 0, 6)
    BeginChrThread(0x9, 3, 0, 6)
    BeginChrThread(0xA, 3, 0, 6)
    BeginChrThread(0xB, 3, 0, 6)
    BeginChrThread(0xC, 3, 0, 6)
    BeginChrThread(0xD, 3, 0, 6)
    BeginChrThread(0xE, 3, 0, 6)
    BeginChrThread(0xF, 3, 0, 6)
    Sleep(1500)
    CancelBlur(0)
    Battle("BattleInfo_2E8", 0x30200011, 0x0, 0x100, 0x14, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0xE, 0xFF)
    EndChrThread(0xF, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    OP_49()
    OP_37()
    SetChrPos(0x0, 0, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x141, 3)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_4_4D9 end

    def Function_5_C0F(): pass

    label("Function_5_C0F")


    def lambda_C14():
        OP_98(0xFE, 0x0, 0x1B58, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C14)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_5_C0F end

    def Function_6_C2E(): pass

    label("Function_6_C2E")

    SetChrChip(0x0, 0xFE, 0x32, 0x12C)

    def lambda_C3B():
        OP_96(0xFE, 0x0, 0x3E8, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C3B)
    Sleep(900)
    OP_4B(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(420)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_6_C2E end

    SaveToFile()

Try(main)
