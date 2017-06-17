from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "神速のデュバリィ",       # 1
        "ヴァンガード",           # 2
        "ヴァンガード",           # 3
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
        "Function_3_10C6",         # 03, 3
        "Function_4_10E2",         # 04, 4
        "Function_5_10FD",         # 05, 5
        "Function_6_1143",         # 06, 6
        "Function_7_11A2",         # 07, 7
        "Function_8_122C",         # 08, 8
        "Function_9_12AF",         # 09, 9
        "Function_10_12DE",        # 0A, 10
        "Function_11_1303",        # 0B, 11
        "Function_12_1EAB",        # 0C, 12
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
    SetChrName("娘の声")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            "#3Cくっ、まさか\x01",
            "ここまで辿り着くとは……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("娘の声")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "#3Cまったく２人とも\x01",
            "何をしていたのかしら！\x02",
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
        "騎士装束の娘",
        (
            "#5P──鉄機隊が隊士、\x01",
            "《神速》のデュバリィです。\x02",
        )
    )

    CloseMessageWindow()

    #N0004
    NpcTalk(
        0x8,
        "騎士装束の娘",
        (
            "#5Pアイネスとエンネアを\x01",
            "退けたのは見事ですが……\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "騎士装束の娘",
        (
            "#5Pアリアンロード様の所には\x01",
            "これ以上、一歩も近づけません！\x02",
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
        "#4S#5Pいざ──尋常に勝負ですっ！\x02",
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
        "#00011F#12Pえっと……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B05")

    #C0008
    ChrTalk(
        0x105,
        (
            "#10406F#12Pうーん、話が早く済むのは\x01",
            "助かるといえば助かるけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B41")

    label("loc_B05")


    #C0009
    ChrTalk(
        0x109,
        (
            "#10111F#12Pは、話が早く済むのは\x01",
            "正直助かりますけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B41")

    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    #C0010
    ChrTalk(
        0x8,
        (
            "#5Pな、なんですの？\x01",
            "その微妙そうな表情は！？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        (
            "#00204F#12Pいえ、筆頭というので\x01",
            "どんな方かと思ったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#00309F#12P意外と可愛らしいっつーか、\x01",
            "微笑ましいっつーか。\x02",
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
            "#5P可愛らしい！？\x01",
            "な、何という屈辱……！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#5P──いいでしょう！\x01",
            "本気で行かせてもらいます！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E20")
    Sound(540, 0, 50, 0)

    label("loc_E20")

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
        "#00013F#5Pこれは……！\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        "#00107F#5Pなんて闘気……！\x02",
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
            "#5Pかの《剣帝》に迫ると称されし、\x01",
            "神速の剣──\x05\x02",
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
        "#4S#5Pとくと味わいやがれですわっ！\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        "#00307F#11P来るぞ……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FCE")

    #C0020
    ChrTalk(
        0x106,
        "#10707F#11P全力で行きます！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_FF4")

    label("loc_FCE")


    #C0021
    ChrTalk(
        0x109,
        "#10107F#11P全力で撃破します！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_FF4")

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

    def lambda_1041():
        OP_9B(0x1, 0xFE, 0xFFF1, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1041)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x31)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 0, 0, 4)

    def lambda_1069():
        OP_9B(0x1, 0xFE, 0xF, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1069)
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

    def Function_3_10C6(): pass

    label("Function_3_10C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10E1")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_3_10C6")

    label("loc_10E1")

    Return()

    # Function_3_10C6 end

    def Function_4_10E2(): pass

    label("Function_4_10E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10FC")
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_4_10E2")

    label("loc_10FC")

    Return()

    # Function_4_10E2 end

    def Function_5_10FD(): pass

    label("Function_5_10FD")

    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 100, 0, 0, 0, 0, 1650, 1650, 1650, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
    Return()

    # Function_5_10FD end

    def Function_6_1143(): pass

    label("Function_6_1143")

    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 100, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(222, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 100, 0)

    def lambda_1191():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1191)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_6_1143 end

    def Function_7_11A2(): pass

    label("Function_7_11A2")

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

    # Function_7_11A2 end

    def Function_8_122C(): pass

    label("Function_8_122C")

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

    # Function_8_122C end

    def Function_9_12AF(): pass

    label("Function_9_12AF")

    SetChrChip(0x0, 0xFE, 0x32, 0x1F4)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    def lambda_12C4():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12C4)
    OP_A1(0xFE, 0x7D0, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_9_12AF end

    def Function_10_12DE(): pass

    label("Function_10_12DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1302")
    OP_82(0x1E, 0x32, 0x1388, 0x3E8)
    Sleep(1000)
    Jump("Function_10_12DE")

    label("loc_1302")

    Return()

    # Function_10_12DE end

    def Function_11_1303(): pass

    label("Function_11_1303")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1341")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_1341")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1359")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_1359")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1371")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_1371")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1389")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_1389")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13A1")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_13A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13B9")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_13B9")

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

    def lambda_1519():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1519)
    WaitChrThread(0x8, 2)
    Sleep(500)

    #C0022
    ChrTalk(
        0x8,
        "#30W#5Pし、信じられません……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#30W#5Pこのような無様……\x01",
            "アリアンロード様に\x01",
            "どう申し開きをすれば……！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#00015F#12Pくっ……はあはあ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1621")

    #C0025
    ChrTalk(
        0x106,
        (
            "#10701F#12P#Nまさか……\x01",
            "私の迅#2Rはや#さを上回るなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1670")

    label("loc_1621")


    #C0026
    ChrTalk(
        0x105,
        (
            "#10410F#12P#N《剣帝》に迫るっていうのも\x01",
            "あながち嘘じゃなさそうだね……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1670")


    #C0027
    ChrTalk(
        0x104,
        "#00306F#12Pとんでもねぇお嬢さんだな……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "#5Pくっ……勝負は勝負。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#5P口惜しいですが、\x01",
            "潔く道を開けましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_16F2():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_16F2)
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
            "#00101F#12P#Nま、待って……！\x02\x03",

            "#00107F貴女たちは……\x01",
            "いえ、ひょっとして\x01",
            "あの《鋼の聖女》は……！？\x02",
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
            "#5P……この上で待ち受けるは、\x01",
            "武における究極にして至高──\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#5P己の魂と決意を\x01",
            "どれだけ剣に込められるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        "#5Pゆめ、忘れるなかれですわ。\x02",
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

    def lambda_194B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_194B)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19B0")
    Sound(540, 0, 50, 0)

    label("loc_19B0")

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

    def lambda_19E6():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19E6)
    Sleep(50)

    def lambda_19F6():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_19F6)
    Sleep(50)

    def lambda_1A06():
        TurnDirection(0x104, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A06)
    Sleep(50)

    def lambda_1A16():
        TurnDirection(0xF4, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1A16)
    Sleep(50)

    def lambda_1A26():
        TurnDirection(0xF5, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1A26)
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
            "#00208F#11P……エリィさん。\x01",
            "先ほどのはいったい？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AFD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AA5")
    OP_FC(0xC)
    Jump("loc_1ABA")

    label("loc_1AA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1ABA")
    OP_FC(0xB)

    label("loc_1ABA")


    #C0036
    ChrTalk(
        0x109,
        (
            "#10105F#13P彼女たちの素性について\x01",
            "何か気付いたんですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B36")

    label("loc_1AFD")


    #C0037
    ChrTalk(
        0x101,
        (
            "#00005F#5P彼女たちの素性について\x01",
            "何か気付いたのか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B36")

    TurnDirection(0x102, 0x103, 500)

    #C0038
    ChrTalk(
        0x102,
        (
            "#00106F#6P……ううん。\x01",
            "ちょっとあり得ないことを\x01",
            "考えてしまっただけなの。\x02\x03",

            "#00108Fみんなを混乱させたくないから\x01",
            "あえて言わない方がいいと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#00001F#5Pそうか……分かった。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#00303F#11Pま、お嬢がそう言うんなら\x01",
            "その方がいいんだろう。\x02\x03",

            "#00301Fしかし──\x01",
            "いよいよ《鋼の聖女》か。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CE5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C89")
    OP_FC(0xC)
    Jump("loc_1C9E")

    label("loc_1C89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C9E")
    OP_FC(0xB)

    label("loc_1C9E")


    #C0041
    ChrTalk(
        0x105,
        (
            "#10408F#13Pどうやら屋上の鐘の前で\x01",
            "待ち受けているみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D52")

    label("loc_1CE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CFF")
    OP_FC(0xC)
    Jump("loc_1D14")

    label("loc_1CFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D14")
    OP_FC(0xB)

    label("loc_1D14")


    #C0042
    ChrTalk(
        0x106,
        (
            "#10708F#13P……屋上の鐘の前で\x01",
            "待ち受けているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D52")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DD2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D7C")
    OP_FC(0xC)
    Jump("loc_1D91")

    label("loc_1D7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D91")
    OP_FC(0xB)

    label("loc_1D91")


    #C0043
    ChrTalk(
        0x109,
        (
            "#10101F#13P万全の準備を固めて\x01",
            "階段を登りましょう……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E37")

    label("loc_1DD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DEC")
    OP_FC(0xC)
    Jump("loc_1E01")

    label("loc_1DEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E01")
    OP_FC(0xB)

    label("loc_1E01")


    #C0044
    ChrTalk(
        0x106,
        (
            "#10701F#13P……決意を固めて\x01",
            "階段を登りましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E37")


    #C0045
    ChrTalk(
        0x101,
        "#00007Fああ#5P……！\x02",
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

    # Function_11_1303 end

    def Function_12_1EAB(): pass

    label("Function_12_1EAB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1980, 2790, -24940, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(24000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2020")
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

    def lambda_1F75():
        OP_95(0xFE, 200, 0, -18100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F75)
    Sleep(20)

    def lambda_1F92():
        OP_95(0xFE, -1300, 0, -18330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F92)
    Sleep(20)

    def lambda_1FAF():
        OP_95(0xFE, 1300, 0, -18330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1FAF)
    Sleep(20)

    def lambda_1FCC():
        OP_95(0xFE, -1300, 0, -19910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1FCC)
    Sleep(20)

    def lambda_1FE9():
        OP_95(0xFE, 0, 0, -19910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1FE9)
    Sleep(20)

    def lambda_2006():
        OP_95(0xFE, 1300, 0, -19910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2006)
    Jump("loc_210D")

    label("loc_2020")

    SetChrPos(0x101, -650, 0, -28330, 0)
    SetChrPos(0x102, 650, 0, -28330, 0)
    SetChrPos(0x104, -1300, 0, -29910, 0)
    SetChrPos(0x109, 0, 0, -29910, 0)
    SetChrPos(0x105, 1300, 0, -29910, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_2084():
        OP_95(0xFE, -650, 0, -18330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2084)
    Sleep(20)

    def lambda_20A1():
        OP_95(0xFE, 650, 0, -18330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20A1)
    Sleep(20)

    def lambda_20BE():
        OP_95(0xFE, -1300, 0, -19910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20BE)
    Sleep(20)

    def lambda_20DB():
        OP_95(0xFE, 0, 0, -19910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_20DB)
    Sleep(20)

    def lambda_20F8():
        OP_95(0xFE, 1300, 0, -19910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_20F8)

    label("loc_210D")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_218F")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_218F")

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
        "#00013Fここもか……！\x02",
    )

    CloseMessageWindow()
    OP_68(-40, 2790, 13920, 5000)
    MoveCamera(45, 19, 0, 5000)
    OP_6E(550, 5000)
    SetCameraDistance(24000, 5000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22BA")
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
    Jump("loc_2319")

    label("loc_22BA")

    SetChrPos(0x101, -650, 0, -1330, 0)
    SetChrPos(0x102, 650, 0, -1330, 0)
    SetChrPos(0x104, -1300, 0, -2910, 0)
    SetChrPos(0x109, 0, 0, -2910, 0)
    SetChrPos(0x105, 1300, 0, -2910, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_2319")

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
            "#10101F……もしかして、\x01",
            "あの“教団”の関係者が\x01",
            "持ち去ってしまったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#00108F……ひとつの可能性ではありそうね。\x02\x03",

            "#00103Fこの《塔》を造ったという\x01",
            "錬金術師たちと関係があったみたいだし、\x01",
            "都合の悪い情報を消したくて……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24FD")

    #C0049
    ChrTalk(
        0x103,
        (
            "#00203Fですが、教団の残党は\x01",
            "もう残っていない筈ですよね……？\x02\x03",

            "#00208Fヨアヒム・ギュンター……\x01",
            "あの人が最後だと聞いていますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_2573")

    label("loc_24FD")


    #C0051
    ChrTalk(
        0x101,
        (
            "#00001F……だが、教団の残党は\x01",
            "もう残っていない筈だ。\x02\x03",

            "#00003Fヨアヒム・ギュンター……\x01",
            "彼が最後だと聞いているし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2573")


    #C0052
    ChrTalk(
        0x104,
        "#00306Fちっ……ワケわかんねえな。\x02",
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
            "#10305F……でも、何冊かは\x01",
            "残ってるみたいだね。\x02\x03",

            "#10302Fあくまで調査って依頼だったけど、\x01",
            "これだけでも回収しといた方が\x01",
            "いいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00003F……ああ、そうだな。\x01",
            "分からない事は多いけど……\x02\x03",

            "#00000Fひとまずあるだけ回収して、\x01",
            "おじさんに報告しにいこうか。\x02",
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

    # Function_12_1EAB end

    SaveToFile()

Try(main)
