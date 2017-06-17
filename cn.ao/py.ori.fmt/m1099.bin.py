from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m1099.bin",                # FileName
        "m1099",                    # MapName
        "m1099",                    # Location
        0x00A2,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 162, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1099",                  # 0
        "『神速』杜巴莉",         # 1
        "先驱者",                 # 2
        "先驱者",                 # 3
        "bm1010",                 # 4
    ))

    ATBonus("ATBonus_118", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_1D8", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1DC", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E0", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1B8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1BC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_1C0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_1C4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_1C8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_1CC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_1D0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D4", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_1F8", 0x0052, 255, 6, 45, 3, 3, 30, 0, "bm1010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms43100.dat", "ms80000.dat", "ms80000.dat", 0, 0, 0, "ms43101.dat", 0, "MonsterBattlePostion_1D8", "MonsterBattlePostion_1B8", "ed7452", "ed7453", "ATBonus_118"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(624, 0)                                        # 0

    ScpFunction((
        "Function_0_270",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_2E7",          # 02, 2
        "Function_3_1084",         # 03, 3
        "Function_4_10A0",         # 04, 4
        "Function_5_10BB",         # 05, 5
        "Function_6_1101",         # 06, 6
        "Function_7_1160",         # 07, 7
        "Function_8_11EA",         # 08, 8
        "Function_9_126D",         # 09, 9
        "Function_10_129C",        # 0A, 10
        "Function_11_12C1",        # 0B, 11
        "Function_12_1DA5",        # 0C, 12
    ))


    def Function_0_270(): pass

    label("Function_0_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28B")
    SetMapFlags(0x10000000)
    Event(0, 2)
    Jump("loc_2B3")

    label("loc_28B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B3")
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_2B3")

    Return()

    # Function_0_270 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E6")
    SetMapObjFlags(0x0, 0x4)

    label("loc_2E6")

    Return()

    # Function_1_2B4 end

    def Function_2_2E7(): pass

    label("Function_2_2E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_343")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)

    label("loc_343")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_361")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch03151.itc", 0x27)

    label("loc_361")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37F")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch03251.itc", 0x27)

    label("loc_37F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39D")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch02951.itc", 0x29)

    label("loc_39D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BB")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch03151.itc", 0x29)

    label("loc_3BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D9")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch03251.itc", 0x29)

    label("loc_3D9")

    LoadChrToIndex("chr/ch43150.itc", 0x2A)
    LoadChrToIndex("chr/ch43151.itc", 0x2B)
    LoadChrToIndex("chr/ch43152.itc", 0x2C)
    LoadChrToIndex("chr/ch43154.itc", 0x2E)
    LoadChrToIndex("chr/ch43100.itc", 0x2F)
    LoadChrToIndex("monster/ch80050.itc", 0x30)
    LoadChrToIndex("monster/ch80051.itc", 0x31)
    LoadEffect(0x0, "event/ev10007.eff")
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\cr035100.eff")
    SoundLoad(832)
    SoundLoad(825)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 0, -26000, 0)
    SetChrPos(0x102, -1530, 0, -27030, 0)
    SetChrPos(0x103, -350, 0, -27010, 0)
    SetChrPos(0x104, 1020, 0, -26920, 0)
    SetChrPos(0xF4, -810, 0, -28050, 0)
    SetChrPos(0xF5, 530, 0, -28030, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 0, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x30)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 0, 0, 3)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -3000, 0, 2000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x30)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 3)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 3000, 0, 2000, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapFlags(0x10000000)
    FadeToBright(1000, 0)
    OP_68(0, 1800, -20000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(24000, 0)
    OP_68(0, 1800, 0, 10000)

    def lambda_5D6():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D6)
    Sleep(30)

    def lambda_5EE():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5EE)
    Sleep(30)

    def lambda_606():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_606)
    Sleep(30)

    def lambda_61E():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_61E)
    Sleep(30)

    def lambda_636():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_636)
    Sleep(30)

    def lambda_64E():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_64E)
    Sleep(3000)
    Fade(1000)
    OP_68(710, 1100, 11810, 0)
    MoveCamera(57, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(41050, 0)
    OP_68(-200, 1100, 0, 8500)
    MoveCamera(45, 28, 0, 8500)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 1000, -4500, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    SetCameraDistance(15000, 2800)
    OP_6F(0x79)
    OP_0D()
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("女孩的声音")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            "#3C唔，没想到你们\x01",
            "可以闯到此处……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("女孩的声音")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "#3C真是的，她们两个\x01",
            "到底在做什么！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(200)
    Fade(500)
    OP_68(0, 1000, 0, 0)
    MoveCamera(0, 23, 0, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(13000, 3000)
    Sound(832, 2, 100, 0)
    BeginChrThread(0x8, 3, 0, 6)
    WaitChrThread(0x8, 3)
    StopSound(832, 500, 100)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)

    #N0003
    NpcTalk(
        0x8,
        "骑士装扮的少女",
        (
            "#5P我是铁机队成员──\x01",
            "『神速』杜巴莉。\x02",
        )
    )

    CloseMessageWindow()

    #N0004
    NpcTalk(
        0x8,
        "骑士装扮的少女",
        (
            "#5P你们竟能击退艾奈丝和恩奈雅，\x01",
            "的确很了不起……\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "骑士装扮的少女",
        (
            "#5P但我绝不会让你们再接近\x01",
            "阿瑞安赫德大人所在之处一步！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(12500, 0)
    Sound(540, 0, 70, 0)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x0)
    OP_6F(0x79)
    OP_0D()
    CancelBlur(500)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0006
    ChrTalk(
        0x8,
        "#4S#5P来吧！我们决一胜负！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    OP_68(0, 1000, -3500, 0)
    MoveCamera(55, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13800, 0)
    SetCameraDistance(14300, 3000)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)
    OP_0D()

    #C0007
    ChrTalk(
        0x101,
        "#00011F#12P那个……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE9")

    #C0008
    ChrTalk(
        0x105,
        (
            "#10406F#12P唔……你如此爽快，\x01",
            "我们自然是求之不得，但……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B23")

    label("loc_AE9")


    #C0009
    ChrTalk(
        0x109,
        (
            "#10111F#12P呼，你如此爽快，\x01",
            "我们自然求之不得，但……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B23")

    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    #C0010
    ChrTalk(
        0x8,
        (
            "#5P怎、怎么了？\x01",
            "为何要摆出那种微妙的表情！？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        (
            "#00204F#12P没什么，只是原本还在想，\x01",
            "身为三人之首的成员究竟会是个怎样的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#00309F#12P没想到意外地可爱，\x01",
            "或者说让人有好感呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1100)

    #C0013
    ChrTalk(
        0x8,
        (
            "#5P可爱！？\x01",
            "这、这是何等的屈辱……！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#5P很好！\x01",
            "既然如此，我要拿出全力了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_68(0, 1000, 0, 5000)
    MoveCamera(0, 23, 0, 5000)
    OP_6E(650, 5000)
    SetCameraDistance(13500, 5000)
    BeginChrThread(0x8, 2, 0, 10)
    BeginChrThread(0x8, 3, 0, 7)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(400)
    Fade(150)
    Sound(817, 0, 100, 0)
    BeginChrThread(0x9, 3, 0, 5)
    BeginChrThread(0xA, 3, 0, 5)
    WaitChrThread(0x8, 3)
    EndChrThread(0x8, 0x2)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    BeginChrThread(0x8, 3, 0, 8)
    WaitChrThread(0x8, 3)
    Sleep(300)
    OP_68(0, 1000, -2000, 2000)
    MoveCamera(0, 23, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(13500, 2000)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF8")
    Sound(540, 0, 50, 0)

    label("loc_DF8")

    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()

    #C0015
    ChrTalk(
        0x101,
        "#00013F#5P这是……！\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        "#00107F#5P好惊人的斗气……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1000, -3000, 0)
    MoveCamera(60, 25, 5, 0)
    MoveCamera(45, 23, 5, 3000)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    OP_0D()

    #C0017
    ChrTalk(
        0x8,
        (
            "#5P人称可以逼近『剑帝』的\x01",
            "神速之剑……\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(14000, 0)
    Sound(540, 0, 70, 0)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x0)
    OP_6F(0x79)
    OP_0D()
    CancelBlur(500)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0018
    ChrTalk(
        0x8,
        "#4S#5P这就让你们好好见识一下！\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        "#00307F#11P来了……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F94")

    #C0020
    ChrTalk(
        0x106,
        "#10707F#11P拿出全力吧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_FB2")

    label("loc_F94")


    #C0021
    ChrTalk(
        0x109,
        "#10107F#11P全力应战！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_FB2")

    StopEffect(0x0, 0x2)
    StopSound(825, 500, 90)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 1000, -4500, 500)
    SetCameraDistance(10000, 500)
    BeginChrThread(0x8, 0, 0, 9)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 0x31)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 0, 0, 4)

    def lambda_FFF():
        OP_9B(0x1, 0xFE, 0xFFF1, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FFF)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x31)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 0, 0, 4)

    def lambda_1027():
        OP_9B(0x1, 0xFE, 0xF, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1027)
    Sleep(500)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    OP_24(0x340)
    OP_24(0x339)
    Battle("BattleInfo_1F8", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Call(0, 11)
    Return()

    # Function_2_2E7 end

    def Function_3_1084(): pass

    label("Function_3_1084")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_109F")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_3_1084")

    label("loc_109F")

    Return()

    # Function_3_1084 end

    def Function_4_10A0(): pass

    label("Function_4_10A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10BA")
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_4_10A0")

    label("loc_10BA")

    Return()

    # Function_4_10A0 end

    def Function_5_10BB(): pass

    label("Function_5_10BB")

    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 100, 0, 0, 0, 0, 1650, 1650, 1650, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
    Return()

    # Function_5_10BB end

    def Function_6_1101(): pass

    label("Function_6_1101")

    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 100, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(222, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 100, 0)

    def lambda_114F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_114F)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_6_1101 end

    def Function_7_1160(): pass

    label("Function_7_1160")

    Sound(357, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x1, 0x0, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x2E)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x4B0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    StopEffect(0x0, 0x2)
    Sleep(1000)
    Sound(222, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 100, 0)
    StopSound(832, 500, 100)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_7_1160 end

    def Function_8_11EA(): pass

    label("Function_8_11EA")

    Fade(500)
    Sound(833, 0, 60, 0)
    Sound(881, 0, 60, 0)
    Sound(825, 2, 100, 0)
    OP_82(0x0, 0x1F4, 0x1388, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(12500, 500)
    PlayEffect(0x2, 0x0, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    OP_0D()
    CancelBlur(500)
    BeginChrThread(0x8, 2, 0, 10)
    Return()

    # Function_8_11EA end

    def Function_9_126D(): pass

    label("Function_9_126D")

    SetChrChip(0x0, 0xFE, 0x32, 0x1F4)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1282():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1282)
    OP_A1(0xFE, 0x7D0, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_9_126D end

    def Function_10_129C(): pass

    label("Function_10_129C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12C0")
    OP_82(0x1E, 0x32, 0x1388, 0x3E8)
    Sleep(1000)
    Jump("Function_10_129C")

    label("loc_12C0")

    Return()

    # Function_10_129C end

    def Function_11_12C1(): pass

    label("Function_11_12C1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12FF")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_12FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1317")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_1317")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_132F")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_132F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1347")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_1347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_135F")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_135F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1377")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_1377")

    LoadChrToIndex("chr/ch43150.itc", 0x24)
    LoadChrToIndex("chr/ch43153.itc", 0x25)
    LoadChrToIndex("chr/ch43154.itc", 0x26)
    LoadChrToIndex("chr/ch43100.itc", 0x27)
    LoadEffect(0x0, "event/ev10006.eff")
    LoadEffect(0x1, "event/ev10007.eff")
    SoundLoad(832)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 0, -5000, 0)
    SetChrPos(0x102, -1530, 0, -6030, 0)
    SetChrPos(0x103, -350, 0, -6010, 0)
    SetChrPos(0x104, 1020, 0, -5920, 0)
    SetChrPos(0xF4, -810, 0, -7050, 0)
    SetChrPos(0xF5, 530, 0, -7030, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x22)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x23)
    SetChrSubChip(0xF5, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 0, 180)
    OP_68(0, 1000, -3000, 0)
    OP_68(0, 1000, -1500, 3000)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    def lambda_14D7():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_14D7)
    WaitChrThread(0x8, 2)
    Sleep(500)

    #C0022
    ChrTalk(
        0x8,
        "#30W#5P难、难以置信……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#30W#5P我竟会败得如此难看……\x01",
            "该如何向阿瑞安赫德\x01",
            "大人谢罪才好……！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#00015F#12P唔……呼……呼……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15BD")

    #C0025
    ChrTalk(
        0x106,
        (
            "#10701F#12P#N居然……\x01",
            "比我还要快……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_15FA")

    label("loc_15BD")


    #C0026
    ChrTalk(
        0x105,
        (
            "#10410F#12P#N号称可以逼近『剑帝』，\x01",
            "似乎并非虚言……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_15FA")


    #C0027
    ChrTalk(
        0x104,
        "#00306F#12P好厉害的小姑娘……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "#5P唔……败了就要承认。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#5P虽然很不甘心，\x01",
            "但我这就为你们让出道路。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_1672():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1672)
    Sleep(200)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    WaitChrThread(0x8, 2)
    Sleep(300)
    Sound(531, 0, 50, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x8, 0x26)
    Sound(534, 0, 50, 0)
    OP_A1(0x8, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(16500, 0)
    Sound(357, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    Sleep(500)

    #C0030
    ChrTalk(
        0x102,
        (
            "#00101F#12P#N等、等一下……！\x02\x03",

            "#00107F你们几个……\x01",
            "不，难道那个\x01",
            "『钢之圣女』就是……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0031
    ChrTalk(
        0x8,
        "#5P……………………………\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "#5P……在上方等待着你们的，\x01",
            "是位于武之领域顶峰的人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#5P你们一定要将自己的灵魂与决心\x01",
            "完全贯彻至武器之中……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        "#5P切记我的话。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(15000, 2000)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(222, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 100, 0)
    StopSound(832, 1000, 100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_18B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_18B7)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    CancelBlur(1000)
    Sleep(1000)
    OP_6F(0x79)
    Sleep(500)
    OP_68(0, 1000, -4500, 3000)
    SetCameraDistance(16500, 3000)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_191C")
    Sound(540, 0, 50, 0)

    label("loc_191C")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()

    def lambda_1952():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1952)
    Sleep(50)

    def lambda_1962():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1962)
    Sleep(50)

    def lambda_1972():
        TurnDirection(0x104, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1972)
    Sleep(50)

    def lambda_1982():
        TurnDirection(0xF4, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1982)
    Sleep(50)

    def lambda_1992():
        TurnDirection(0xF5, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1992)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0035
    ChrTalk(
        0x103,
        (
            "#00208F#11P……艾莉前辈，\x01",
            "你刚才想问什么？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A51")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A0B")
    OP_FC(0xC)
    Jump("loc_1A20")

    label("loc_1A0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A20")
    OP_FC(0xB)

    label("loc_1A20")


    #C0036
    ChrTalk(
        0x109,
        (
            "#10105F#13P是不是察觉到\x01",
            "她们的来历了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7C")

    label("loc_1A51")


    #C0037
    ChrTalk(
        0x101,
        (
            "#00005F#5P是不是察觉到\x01",
            "她们的身份了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A7C")

    TurnDirection(0x102, 0x103, 500)

    #C0038
    ChrTalk(
        0x102,
        (
            "#00106F#6P……不，\x01",
            "只是产生了一种\x01",
            "很荒谬的想法而已。\x02\x03",

            "#00108F为了不让大家头脑混乱，\x01",
            "暂时还是不说为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#00001F#5P是吗……明白了。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#00303F#11P算啦，既然大小姐都这么说了，\x01",
            "那我们就不谈这个了。\x02\x03",

            "#00301F话说回来，\x01",
            "终于要面对『钢之圣女』了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BF5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BAB")
    OP_FC(0xC)
    Jump("loc_1BC0")

    label("loc_1BAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BC0")
    OP_FC(0xB)

    label("loc_1BC0")


    #C0041
    ChrTalk(
        0x105,
        (
            "#10408F#13P她好像在塔顶的\x01",
            "大钟前等着我们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C58")

    label("loc_1BF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C0F")
    OP_FC(0xC)
    Jump("loc_1C24")

    label("loc_1C0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C24")
    OP_FC(0xB)

    label("loc_1C24")


    #C0042
    ChrTalk(
        0x106,
        (
            "#10708F#13P……她似乎在塔顶的\x01",
            "大钟前等着我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CD2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C82")
    OP_FC(0xC)
    Jump("loc_1C97")

    label("loc_1C82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C97")
    OP_FC(0xB)

    label("loc_1C97")


    #C0043
    ChrTalk(
        0x109,
        (
            "#10101F#13P做好万全准备之后，\x01",
            "就登上阶梯吧……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D33")

    label("loc_1CD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CEC")
    OP_FC(0xC)
    Jump("loc_1D01")

    label("loc_1CEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D01")
    OP_FC(0xB)

    label("loc_1D01")


    #C0044
    ChrTalk(
        0x106,
        (
            "#10701F#13P……坚定决心之后，\x01",
            "就登上阶梯吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D33")


    #C0045
    ChrTalk(
        0x101,
        "#00007F嗯#5P……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_37()
    SetChrPos(0x0, 0, 0, -2000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A5, 1)
    OP_29(0xB0, 0x1, 0x5)
    OP_24(0x340)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_12C1 end

    def Function_12_1DA5(): pass

    label("Function_12_1DA5")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1980, 2790, -24940, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(24000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F1A")
    SetChrPos(0x101, 200, 0, -28330, 0)
    SetChrPos(0x102, -1300, 0, -28330, 0)
    SetChrPos(0x103, 1300, 0, -28330, 0)
    SetChrPos(0x104, -1300, 0, -29910, 0)
    SetChrPos(0x109, 0, 0, -29910, 0)
    SetChrPos(0x105, 1300, 0, -29910, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_1E6F():
        OP_95(0xFE, 200, 0, -18100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E6F)
    Sleep(20)

    def lambda_1E8C():
        OP_95(0xFE, -1300, 0, -18330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E8C)
    Sleep(20)

    def lambda_1EA9():
        OP_95(0xFE, 1300, 0, -18330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1EA9)
    Sleep(20)

    def lambda_1EC6():
        OP_95(0xFE, -1300, 0, -19910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1EC6)
    Sleep(20)

    def lambda_1EE3():
        OP_95(0xFE, 0, 0, -19910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1EE3)
    Sleep(20)

    def lambda_1F00():
        OP_95(0xFE, 1300, 0, -19910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1F00)
    Jump("loc_2007")

    label("loc_1F1A")

    SetChrPos(0x101, -650, 0, -28330, 0)
    SetChrPos(0x102, 650, 0, -28330, 0)
    SetChrPos(0x104, -1300, 0, -29910, 0)
    SetChrPos(0x109, 0, 0, -29910, 0)
    SetChrPos(0x105, 1300, 0, -29910, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_1F7E():
        OP_95(0xFE, -650, 0, -18330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F7E)
    Sleep(20)

    def lambda_1F9B():
        OP_95(0xFE, 650, 0, -18330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F9B)
    Sleep(20)

    def lambda_1FB8():
        OP_95(0xFE, -1300, 0, -19910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1FB8)
    Sleep(20)

    def lambda_1FD5():
        OP_95(0xFE, 0, 0, -19910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1FD5)
    Sleep(20)

    def lambda_1FF2():
        OP_95(0xFE, 1300, 0, -19910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1FF2)

    label("loc_2007")

    OP_68(-1700, 2790, -17940, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x105, 1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2089")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_2089")

    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0046
    ChrTalk(
        0x101,
        "#00013F这里也……！\x02",
    )

    CloseMessageWindow()
    OP_68(-40, 2790, 13920, 5000)
    MoveCamera(45, 19, 0, 5000)
    OP_6E(550, 5000)
    SetCameraDistance(24000, 5000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21B2")
    SetChrPos(0x101, 200, 0, -1100, 0)
    SetChrPos(0x102, -1300, 0, -1330, 0)
    SetChrPos(0x103, 1300, 0, -1330, 0)
    SetChrPos(0x104, -1300, 0, -2910, 0)
    SetChrPos(0x109, 0, 0, -2910, 0)
    SetChrPos(0x105, 1300, 0, -2910, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_2211")

    label("loc_21B2")

    SetChrPos(0x101, -650, 0, -1330, 0)
    SetChrPos(0x102, 650, 0, -1330, 0)
    SetChrPos(0x104, -1300, 0, -2910, 0)
    SetChrPos(0x109, 0, 0, -2910, 0)
    SetChrPos(0x105, 1300, 0, -2910, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_2211")

    Sleep(1000)
    Fade(1000)
    OP_68(-3490, 2790, -730, 0)
    MoveCamera(36, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20580, 0)
    OP_0D()

    #C0047
    ChrTalk(
        0x109,
        (
            "#10101F……莫非是被\x01",
            "那个『教团』的\x01",
            "成员带走的？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#00108F……有这种可能。\x02\x03",

            "#00103F他们似乎与建造此塔的\x01",
            "炼金术师们存在着某种关系，\x01",
            "可能是想抹消对自己不利的情报吧……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2397")

    #C0049
    ChrTalk(
        0x103,
        (
            "#00203F可是，如今已经\x01",
            "没有教团残党了吧……？\x02\x03",

            "#00208F约亚西姆·琼塔……\x01",
            "就是教团最后的一员了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_23FD")

    label("loc_2397")


    #C0051
    ChrTalk(
        0x101,
        (
            "#00001F……但如今应该\x01",
            "已经没有教团残党了。\x02\x03",

            "#00003F约亚西姆·琼塔……\x01",
            "应该就是教团最后的一员了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23FD")


    #C0052
    ChrTalk(
        0x104,
        "#00306F啧……真是搞不懂啊。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-8330, 2790, 8380, 0)
    MoveCamera(28, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(12320, 0)
    OP_0D()

    #C0053
    ChrTalk(
        0x105,
        (
            "#10305F……不过，似乎还\x01",
            "留下了几本呢。\x02\x03",

            "#10302F虽说委托内容只是来此调查，\x01",
            "但我们还是把这几本书\x01",
            "带回去为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00003F……嗯，有道理。\x01",
            "如今的情况真是让人毫无头绪……\x02\x03",

            "#00000F我们就先把剩下的这些书带回去，\x01",
            "向迈尔斯叔叔报告吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x22, 0)
    NewScene("c1130", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1DA5 end

    SaveToFile()

Try(main)
