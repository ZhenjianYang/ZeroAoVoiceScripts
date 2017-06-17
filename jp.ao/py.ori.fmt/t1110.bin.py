from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1110.bin",                # FileName
        "t1110",                    # MapName
        "t1110",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1110",                  # 0
        "音声",                   # 1
        "音声",                   # 2
        "音声",                   # 3
        "エリィ",                 # 4
        "マクダエル議長",         # 5
        "ヨナ",                   # 6
        "SE制御",                 # 7
        "bt1110",                 # 8
    ))

    ATBonus("ATBonus_188", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_248", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_24C", 3, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_250", 13, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_254", 3, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_258", 13, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_25C", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_260", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_228", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_22C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_230", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_234", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_238", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_23C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_240", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_244", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_268", 0x0052, 255, 6, 45, 3, 3, 30, 0, "bt1110", 0x00000000, 100, 0, 0, 0,
        (
            ("ms84000.dat", "ms84500.dat", "ms84500.dat", 0, 0, 0, "ms84500.dat", 0, "MonsterBattlePostion_248", "MonsterBattlePostion_228", "ed7451", "ed7453", "ATBonus_188"),
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(852, 0)                                        # 0

    ScpFunction((
        "Function_0_354",          # 00, 0
        "Function_1_375",          # 01, 1
        "Function_2_38E",          # 02, 2
        "Function_3_D24",          # 03, 3
        "Function_4_D49",          # 04, 4
        "Function_5_DAA",          # 05, 5
        "Function_6_E91",          # 06, 6
        "Function_7_EEC",          # 07, 7
        "Function_8_F3B",          # 08, 8
        "Function_9_F5A",          # 09, 9
        "Function_10_F76",         # 0A, 10
        "Function_11_F92",         # 0B, 11
        "Function_12_2FBA",        # 0C, 12
        "Function_13_3022",        # 0D, 13
        "Function_14_3067",        # 0E, 14
        "Function_15_30A5",        # 0F, 15
        "Function_16_30CF",        # 10, 16
        "Function_17_30EB",        # 11, 17
        "Function_18_30FD",        # 12, 18
        "Function_19_310F",        # 13, 19
        "Function_20_3207",        # 14, 20
        "Function_21_326D",        # 15, 21
        "Function_22_3291",        # 16, 22
        "Function_23_32DC",        # 17, 23
        "Function_24_3812",        # 18, 24
        "Function_25_3858",        # 19, 25
        "Function_26_3880",        # 1A, 26
        "Function_27_38A8",        # 1B, 27
        "Function_28_38E8",        # 1C, 28
        "Function_29_3910",        # 1D, 29
        "Function_30_3971",        # 1E, 30
        "Function_31_39D2",        # 1F, 31
        "Function_32_3A33",        # 20, 32
        "Function_33_3A94",        # 21, 33
        "Function_34_3AF5",        # 22, 34
        "Function_35_3DBA",        # 23, 35
        "Function_36_3E76",        # 24, 36
        "Function_37_3EEF",        # 25, 37
        "Function_38_4159",        # 26, 38
        "Function_39_4188",        # 27, 39
        "Function_40_41B7",        # 28, 40
        "Function_41_41D0",        # 29, 41
    ))


    def Function_0_354(): pass

    label("Function_0_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_365")
    Event(0, 2)

    label("loc_365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_374")
    ClearScenarioFlags(0x22, 0)
    Event(0, 11)

    label("loc_374")

    Return()

    # Function_0_354 end

    def Function_1_375(): pass

    label("Function_1_375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_387")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_387")

    Sound(124, 1, 50, 0)
    Return()

    # Function_1_375 end

    def Function_2_38E(): pass

    label("Function_2_38E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("monster/ch84050.itc", 0x24)
    LoadChrToIndex("monster/ch84051.itc", 0x25)
    LoadChrToIndex("monster/ch84052.itc", 0x26)
    LoadChrToIndex("monster/ch84550.itc", 0x27)
    LoadEffect(0x0, "event\\ev502_00.eff")
    SoundLoad(950)
    SoundLoad(825)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -500, 500, 13500, 0)
    SetChrPos(0x104, 500, 500, 13500, 0)
    SetChrPos(0x103, -500, 500, 12000, 0)
    SetChrPos(0x105, 500, 500, 12000, 0)
    SetChrPos(0x106, -1500, 500, 12750, 0)
    SetChrPos(0x109, 1500, 500, 13050, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 1500, 23000, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x1)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -4000, 500, 21000, 135)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 4000, 500, 21000, 225)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(320, 2500, 18250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(1000, 0)
    OP_68(320, 1500, 18250, 4000)

    def lambda_55D():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_55D)
    Sleep(30)

    def lambda_575():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_575)
    Sleep(30)

    def lambda_58D():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_58D)
    Sleep(30)

    def lambda_5A5():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5A5)
    Sleep(30)

    def lambda_5BD():
        OP_9B(0x0, 0x109, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5BD)
    Sleep(30)

    def lambda_5D5():
        OP_9B(0x0, 0x106, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5D5)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(320, 1500, 18250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x101,
        "#00008F#11P誰もいない……？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x106,
        (
            "#10708F#12Pいえ……\x01",
            "何かの気配を感じます。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x105,
        (
            "#10401F#12Pふむ、魔獣の類いじゃ\x01",
            "なさそうだけど。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    ReplaceBGM("ed7251", -1)
    ReplaceBGM("ed7565", -1)
    OP_68(0, 3300, 21000, 1500)
    MoveCamera(45, 15, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    Sound(903, 0, 100, 0)
    SetMessageWindowPos(70, 60, -1, -1)

    #A0004
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ｐ──侵入者を発見。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x8, 0, 0, 3)
    Sound(825, 2, 30, 0)
    Sleep(500)

    #C0005
    ChrTalk(
        0x103,
        "#00207F#11P正面に反応！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#00310F#11Pチッ……\x01",
            "連中#4R㈲　㈲#ってのはアイツらか！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    SetCameraDistance(14000, 500)
    BeginChrThread(0x8, 3, 0, 4)
    Sound(950, 2, 100, 0)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    EndChrThread(0x8, 0x3)
    StopEffect(0x0, 0x2)
    BeginChrThread(0x8, 3, 0, 5)
    WaitChrThread(0x8, 3)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    Sleep(1500)
    Fade(500)
    OP_68(390, 2600, 19220, 0)
    MoveCamera(331, 20, 0, 0)
    MoveCamera(0, 15, 0, 10000)
    OP_6E(600, 0)
    SetCameraDistance(12220, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(541, 0, 30, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    OP_0D()
    Sound(903, 0, 100, 0)
    SetMessageWindowPos(270, 90, -1, -1)

    #A0007
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "対象者６名──\x02",
        )
    )

    CloseMessageWindow()

    #A0008
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特務支援課３名、\x01",
            "国防軍シーカー少尉を確認。\x02",
        )
    )

    CloseMessageWindow()

    #A0009
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "２名は不明──ただし戦闘力は\x01",
            "Ａランク以上と推測する。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0010
    ChrTalk(
        0x105,
        "#10407F#12P#Nくっ……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0011
    ChrTalk(
        0x106,
        "#10707F#6P#N機械がそこまで……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-590, 2300, 19970, 0)
    MoveCamera(41, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13440, 0)
    OP_68(-590, 2300, 19970, 0)
    MoveCamera(41, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    SetCameraDistance(14000, 1500)
    BeginChrThread(0x8, 3, 0, 3)
    BeginChrThread(0x9, 3, 0, 6)
    BeginChrThread(0xA, 3, 0, 7)
    Sound(825, 2, 30, 0)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    EndChrThread(0x8, 0x3)
    Sound(903, 0, 100, 0)
    SetMessageWindowPos(50, 100, -1, -1)

    #A0012
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《イザヨイ》を展開。\x02",
        )
    )

    CloseMessageWindow()

    #A0013
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レジェネンコフⅡ型、\x01",
            "《ムラマサ》──\x02",
        )
    )

    CloseMessageWindow()

    #A0014
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "これより殲滅行動に入る。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0015
    ChrTalk(
        0x101,
        "#00010F#12P#N来るぞ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0016
    ChrTalk(
        0x109,
        "#10107F#12P#N迎撃を開始します！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x8, 0x0)
    Sound(905, 0, 100, 0)
    StopSound(825, 1000, 30)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0x8, 0x3E8, 0x2, 0x0, 0x1)
    Sleep(750)
    Sound(951, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-610, 2300, 19190, 500)
    SetCameraDistance(9500, 500)
    SetChrSubChip(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x9, 0x1000)
    SetChrFlags(0xA, 0x1000)
    SetChrChip(0x0, 0x8, 0x64, 0x1F4)
    SetChrChip(0x0, 0x9, 0x64, 0x1F4)
    SetChrChip(0x0, 0xA, 0x64, 0x1F4)

    def lambda_C97():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C97)

    def lambda_CAC():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CAC)

    def lambda_CC1():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CC1)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    OP_24(0x3B6)
    OP_24(0x339)
    Battle("BattleInfo_268", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 11)
    Return()

    # Function_2_38E end

    def Function_3_D24(): pass

    label("Function_3_D24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D48")
    OP_82(0x0, 0x1E, 0x1388, 0x3E8)
    Sleep(1000)
    Jump("Function_3_D24")

    label("loc_D48")

    Return()

    # Function_3_D24 end

    def Function_4_D49(): pass

    label("Function_4_D49")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DA9")
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x96, 0x2EE)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xC8, 0x2EE)
    StopEffect(0x0, 0x2)
    Jump("Function_4_D49")

    label("loc_DA9")

    Return()

    # Function_4_D49 end

    def Function_5_DAA(): pass

    label("Function_5_DAA")

    SetCameraDistance(15000, 4000)
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x9C4)
    Sleep(500)
    EndChrThread(0x8, 0x0)
    StopSound(825, 1000, 30)
    Fade(700)
    OP_68(0, 2300, 21500, 300)
    SetChrFlags(0xFE, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xDAC, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    StopSound(950, 1000, 100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x12C, 0x1F4, 0x1388, 0x3E8)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Sleep(1000)
    CancelBlur(500)
    OP_0D()
    Return()

    # Function_5_DAA end

    def Function_6_E91(): pass

    label("Function_6_E91")

    Sound(950, 2, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
    StopEffect(0x1, 0x2)
    StopSound(950, 1000, 100)
    BeginChrThread(0xFE, 0, 0, 10)
    Sleep(1000)
    Return()

    # Function_6_E91 end

    def Function_7_EEC(): pass

    label("Function_7_EEC")

    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
    StopEffect(0x2, 0x2)
    BeginChrThread(0xFE, 0, 0, 10)
    Sleep(1000)
    Return()

    # Function_7_EEC end

    def Function_8_F3B(): pass

    label("Function_8_F3B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F59")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_8_F3B")

    label("loc_F59")

    Return()

    # Function_8_F3B end

    def Function_9_F5A(): pass

    label("Function_9_F5A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F75")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_9_F5A")

    label("loc_F75")

    Return()

    # Function_9_F5A end

    def Function_10_F76(): pass

    label("Function_10_F76")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F91")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_10_F76")

    label("loc_F91")

    Return()

    # Function_10_F76 end

    def Function_11_F92(): pass

    label("Function_11_F92")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00100.itc", 0x1E)
    LoadChrToIndex("chr/ch05800.itc", 0x1F)
    LoadChrToIndex("chr/ch06100.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00051.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00251.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    LoadChrToIndex("chr/ch00351.itc", 0x26)
    LoadChrToIndex("chr/ch02950.itc", 0x27)
    LoadChrToIndex("chr/ch02951.itc", 0x28)
    LoadChrToIndex("chr/ch03150.itc", 0x29)
    LoadChrToIndex("chr/ch03151.itc", 0x2A)
    LoadChrToIndex("chr/ch03250.itc", 0x2B)
    LoadChrToIndex("chr/ch03251.itc", 0x2C)
    LoadChrToIndex("chr/ch00056.itc", 0x2D)
    LoadChrToIndex("chr/ch00256.itc", 0x2E)
    LoadChrToIndex("chr/ch00356.itc", 0x2F)
    LoadChrToIndex("chr/ch0295F.itc", 0x30)
    LoadChrToIndex("chr/ch0315F.itc", 0x31)
    LoadChrToIndex("chr/ch0325A.itc", 0x32)
    LoadChrToIndex("chr/ch00053.itc", 0x33)
    LoadChrToIndex("chr/ch00352.itc", 0x34)
    LoadChrToIndex("chr/ch03252.itc", 0x35)
    LoadChrToIndex("chr/ch00150.itc", 0x36)
    LoadChrToIndex("monster/ch84050.itc", 0x37)
    LoadChrToIndex("monster/ch84051.itc", 0x38)
    LoadChrToIndex("monster/ch84052.itc", 0x39)
    LoadChrToIndex("apl/ch51767.itc", 0x3A)
    LoadChrToIndex("chr/ch02952.itc", 0x3B)
    LoadChrToIndex("chr/ch00101.itc", 0x3C)
    LoadChrToIndex("apl/ch51713.itc", 0x3D)
    LoadEffect(0x0, "battle/ms00001.eff")
    LoadEffect(0x1, "event\\ev10008.eff")
    LoadEffect(0x3, "battle/cr001000.eff")
    LoadEffect(0x4, "event/ev17029.eff")
    LoadEffect(0x5, "event\\ev15010.eff")
    LoadEffect(0x6, "event\\ev14002.eff")
    LoadEffect(0x7, "event\\ev17030.eff")
    LoadEffect(0x8, "event\\\\eva04_00.eff")
    LoadEffect(0x9, "event\\\\ev17034.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00102.itp")
    SoundLoad(3403)
    SoundLoad(3404)
    SoundLoad(3405)
    SoundLoad(3406)
    SoundLoad(904)
    SoundLoad(579)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 500, 20500, 0)
    SetChrPos(0x104, -900, 500, 19200, 0)
    SetChrPos(0x109, 850, 500, 19650, 0)
    SetChrPos(0x105, 150, 500, 18550, 0)
    SetChrPos(0x103, 950, 500, 18000, 0)
    SetChrPos(0x106, -1200, 500, 17900, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x29)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x2B)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x3A)
    SetChrSubChip(0x8, 0x3)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 500, 24000, 180)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x36)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 11000, 500, 20000, 270)
    SetChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 16500, 1000, 20500, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 16500, 1000, 19500, 270)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_68(0, 1500, 24000, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    PlayEffect(0x4, 0x0, 0x8, 0x5, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xE, 1, 0, 40)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 4000)
    BeginChrThread(0x8, 3, 0, 12)
    WaitChrThread(0x8, 3)
    StopEffect(0x0, 0x2)
    EndChrThread(0xE, 0x1)
    OP_6F(0x79)
    OP_0D()
    OP_68(0, 1500, 21000, 2500)
    OP_6F(0x79)
    Fade(500)

    def lambda_1374():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1374)
    Sleep(50)

    def lambda_1390():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1390)
    Sleep(50)

    def lambda_13AC():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_13AC)
    Sleep(50)

    def lambda_13C8():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_13C8)
    Sleep(50)

    def lambda_13E4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_13E4)
    Sleep(50)

    def lambda_1400():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1400)
    Sound(898, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x2D)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x2E)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    Sound(514, 0, 40, 0)
    SetChrChipByIndex(0x104, 0x2F)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x109, 0x30)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x105, 0x31)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x106, 0x32)
    SetChrSubChip(0x106, 0x0)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x106, 2)
    OP_0D()

    #C0017
    ChrTalk(
        0x101,
        (
            "#00015F#12Pぐっ……\x01",
            "とんでもないヤツだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x106,
        (
            "#10708F#12P#N《結社》というのは\x01",
            "恐るべき集団ですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0019
    ChrTalk(
        0x104,
        (
            "#00306F#12Pああ、あの紅い武者人形が\x01",
            "ここまで強化されるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#00211F#12P……やはりあの博士が\x01",
            "改造したんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x105,
        "#10406F#12Pその可能性は高そうだね……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1500, 19500, 0)
    MoveCamera(135, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(14500, 1500)
    OP_6F(0x79)
    OP_0D()
    Fade(250)

    def lambda_15E0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15E0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sound(812, 0, 100, 0)
    WaitChrThread(0x101, 2)
    OP_0D()
    Fade(500)

    def lambda_1611():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1611)
    Sleep(50)

    def lambda_162D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_162D)
    Sleep(50)

    def lambda_1649():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1649)
    Sleep(50)

    def lambda_1665():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1665)
    Sleep(50)

    def lambda_1681():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1681)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x105, 0x29)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x106, 0x2B)
    SetChrSubChip(0x106, 0x2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x106, 2)
    OP_0D()
    SetCameraDistance(17000, 5000)
    MoveCamera(120, 25, 0, 5000)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(150)
    BeginChrThread(0x103, 3, 0, 14)
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(150)
    BeginChrThread(0x109, 3, 0, 16)
    Sleep(150)
    BeginChrThread(0x105, 3, 0, 17)
    Sleep(150)
    BeginChrThread(0x106, 3, 0, 18)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 1500, 21500, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(15000, 2000)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_178C():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_178C)
    Sleep(50)

    def lambda_179C():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_179C)
    Sleep(50)

    def lambda_17AC():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_17AC)
    Sleep(50)

    def lambda_17BC():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_17BC)
    Sleep(50)

    def lambda_17CC():
        OP_93(0x106, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_17CC)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    #C0022
    ChrTalk(
        0x101,
        (
            "#00004F#5Pよし、これで障害は\x01",
            "一通り排除できたはずだ。\x02\x03",

            "#00000F屋敷を捜索して\x01",
            "エリィと議長たちを──\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_68(0, 2000, 23000, 1000)
    MoveCamera(0, 33, 0, 1000)
    OP_6F(0x79)
    Sound(140, 0, 100, 0)
    PlayEffect(0x7, 0x0, 0x8, 0x5, 50, 1700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(655, 0, 50, 0)
    Sleep(950)
    Fade(500)

    def lambda_18CA():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_18CA)
    OP_A1(0x8, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    SetChrChipByIndex(0x8, 0x37)
    SetChrSubChip(0x8, 0x0)
    Sound(951, 0, 100, 0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 1, 0, 41)
    PlayEffect(0x4, 0x7, 0x8, 0x5, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x8, 0, 0, 8)
    WaitChrThread(0x8, 2)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)

    #C0023
    ChrTalk(
        0x101,
        "#00011F#6Pなに……！？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7455", 0)
    EndChrThread(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 21)
    BeginChrThread(0x8, 3, 0, 19)
    WaitChrThread(0x8, 3)
    OP_68(750, 2000, 20800, 750)
    MoveCamera(0, 20, 0, 750)
    OP_6E(600, 750)
    SetCameraDistance(15000, 750)
    OP_6F(0x79)
    Fade(250)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x3B)
    SetChrSubChip(0x109, 0x0)
    OP_A1(0x109, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    OP_0D()

    #C0024
    ChrTalk(
        0x109,
        "#10110F#12Pこのっ……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 23)
    WaitChrThread(0x8, 3)

    def lambda_1A1D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1A1D)
    Sleep(50)

    def lambda_1A2D():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A2D)
    Sleep(50)

    def lambda_1A3D():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1A3D)
    Sleep(50)

    def lambda_1A4D():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A4D)
    Sleep(50)

    def lambda_1A5D():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1A5D)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0025
    ChrTalk(
        0x101,
        "#00010F#6P#Nしまった──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)

    def lambda_1AC2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1AC2)
    Sleep(50)

    def lambda_1ADE():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1ADE)
    Sleep(50)

    def lambda_1AFA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1AFA)
    Sleep(50)

    def lambda_1B16():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1B16)
    Sleep(50)

    def lambda_1B32():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1B32)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x105, 0x29)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x106, 0x2B)
    SetChrSubChip(0x106, 0x2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x106, 2)
    OP_0D()

    #C0026
    ChrTalk(
        0x109,
        "#10107F#5Pロイドさん……！\x02",
    )

    CloseMessageWindow()
    OP_68(3550, 2300, 21350, 1000)
    MoveCamera(315, 26, 0, 1000)
    OP_6E(600, 1000)
    SetCameraDistance(13700, 1000)
    OP_6F(0x79)
    Fade(350)
    Sound(951, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x39)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    StopBGM(0xBB8)
    OP_C9(0x0, 0x80000000)

    #N0027
    NpcTalk(
        0xB,
        "娘の声",
        "#3403V#1P#10Aさせないッ──！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0x8, 3, 0, 34)
    WaitChrThread(0x8, 3)

    #C0028
    ChrTalk(
        0x101,
        "#00005F#5P#N#8Aえ──\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-2850, 1700, 21800, 0)
    OP_68(-4350, 1700, 21800, 500)
    MoveCamera(23, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    TurnDirection(0x103, 0x8, 0)
    TurnDirection(0x104, 0x8, 0)
    TurnDirection(0x105, 0x8, 0)
    TurnDirection(0x109, 0x8, 0)
    TurnDirection(0x106, 0x8, 0)
    OP_6F(0x79)
    OP_0D()
    BeginChrThread(0x106, 3, 0, 36)
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 35)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x106, 3)
    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    Fade(500)
    OP_82(0x7D, 0x7D, 0x1388, 0x3E8)
    OP_68(-1000, 1500, 21000, 0)
    OP_68(-1500, 1500, 20000, 2000)
    MoveCamera(35, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 80, 0)
    Sound(531, 0, 80, 0)
    Sound(540, 0, 40, 0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_0D()

    def lambda_1D8E():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D8E)
    Sleep(50)

    def lambda_1D9E():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D9E)
    Sleep(50)

    def lambda_1DAE():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DAE)
    Sleep(50)

    def lambda_1DBE():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1DBE)
    Sleep(50)

    def lambda_1DCE():
        OP_93(0x106, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1DCE)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    OP_68(1000, 1500, 20000, 1500)
    SetCameraDistance(13500, 1500)

    def lambda_1E0C():
        OP_9B(0x1, 0xFE, 0x1E, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1E0C)
    Sleep(50)

    def lambda_1E24():
        OP_9B(0x1, 0xFE, 0xFFE7, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E24)
    Sleep(50)

    def lambda_1E3C():
        OP_9B(0x1, 0xFE, 0xFFDA, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E3C)
    Sleep(50)

    def lambda_1E54():
        OP_9B(0x1, 0xFE, 0x21, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E54)
    Sleep(50)

    def lambda_1E6C():
        OP_9B(0x1, 0xFE, 0xFFE2, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1E6C)
    Sleep(50)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)

    #C0029
    ChrTalk(
        0x103,
        "#00206F#6P#6Pふう……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x105,
        "#10406F#6P……やれやれだね。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x8)
    OP_68(11000, 1500, 20000, 2200)
    MoveCamera(60, 25, 0, 2200)
    OP_6E(600, 2200)
    SetCameraDistance(14500, 2200)
    OP_6F(0x79)
    SetChrPos(0x101, 700, 500, 20000, 90)

    #C0031
    ChrTalk(
        0x101,
        "#00002F#6P#Nエリィ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, 4700, 500, 20000, 90)

    #C0032
    ChrTalk(
        0x103,
        "#00202F#6P#N……エリィさん。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0033
    ChrTalk(
        0x104,
        "#00309F#6P#Nはは、無事だったか。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    OP_0D()
    OP_68(9000, 1500, 20000, 1500)
    MoveCamera(60, 18, 0, 1500)
    SetCameraDistance(15500, 1500)
    OP_6F(0x79)

    #C0034
    ChrTalk(
        0xB,
        "#00106F#40W#11P………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_2003():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2003)
    Sleep(250)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x101, 2)
    OP_0D()
    Sleep(800)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)

    #C0035
    ChrTalk(
        0x101,
        (
            "#00012F#6Pその……\x01",
            "何て言ったらいいか。\x02\x03",

            "#00004F──とりあえず、\x01",
            "ありがとう、エリィ。\x02\x03",

            "#00002Fおかげで助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xB,
        "#00101F#11P……っ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)
    Fade(250)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    OP_0D()
    OP_68(5300, 1500, 20000, 1400)
    MoveCamera(45, 18, 0, 1400)
    SetCameraDistance(12000, 1400)
    SetChrChipByIndex(0xB, 0x3C)
    SetChrSubChip(0xB, 0x0)
    OP_95(0xB, 5800, 500, 20000, 5000, 0x0)
    Fade(250)
    Sound(898, 0, 100, 0)
    Sound(811, 0, 20, 0)

    def lambda_2149():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2149)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x3D)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x3D)
    SetChrSubChip(0x101, 0x8)
    WaitChrThread(0x101, 2)
    OP_6F(0x79)
    SetCameraDistance(11000, 20000)
    OP_0D()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x101,
        "#00011F#6P#7Aわわっ……！？\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0038
    AnonymousTalk(
        0xB,
        (
            "#3404V#40W#35Aよかった……\x01",
            "……本当によかった……\x02\x03",

            "#3405V#35A無事でいてくれて……\x01",
            "……こうしてまた会えて……\x02\x03",

            "#3406V#35Aもう二度と……\x01",
            "会えないかと思ったから……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #C0039
    ChrTalk(
        0x101,
        "#00002F#6Pエリィ……\x02",
    )

    CloseMessageWindow()
    OP_68(3000, 1500, 20000, 2000)
    SetCameraDistance(14000, 2000)
    Sleep(1500)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0040
    ChrTalk(
        0x104,
        "#00309F#6P（あー、なんつーか……）\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        (
            "#10114F#6P（えっと、声を掛けても\x01",
            "  いいんでしょうか……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x106,
        "#10706F#6P（こ、困りましたね……）\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        (
            "#10402F#6P（しかし君の時といい、\x01",
            "  つくづく彼も役得だよね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        "#00211F#6P（……記憶にないです。）\x02",
    )

    CloseMessageWindow()
    OP_68(3700, 1500, 20000, 1500)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    #Sound(2185, 255, 100, 0)    #voice#Elie

    #C0045
    ChrTalk(
        0xB,
        "#00105F#11Pあら……？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00012F#6Pはは……\x02\x03",

            "……嬉しいんだけど、\x01",
            "さすがにちょっと\x01",
            "視線が痛いかなって……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrSubChip(0xB, 0x1)
    SetChrSubChip(0x101, 0x9)
    SetChrPos(0xB, 6000, 500, 20000, 270)
    OP_0D()
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_68(3840, 1500, 19790, 2000)
    Sound(2177, 255, 80, 0)    #voice#Elie
    OP_96(0xB, 0x1770, 0x1F4, 0x4B00, 0x7D0, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x3D)
    OP_A1(0xB, 0x514, 0x8, 0x2, 0x3, 0x4, 0x3, 0x2, 0x3, 0x4, 0x3)
    OP_A1(0xB, 0x514, 0x4, 0x2, 0x3, 0x4, 0x3)

    #C0047
    ChrTalk(
        0xB,
        (
            "#00112F#11Pち、違うのよ！？\x02\x03",

            "今のはロイドが\x01",
            "危ないところだったから\x01",
            "つい夢中になってしまって！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x105,
        "#10402F#6Pへー。（棒読み）\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        "#00309F#6Pそうなんだー。（ニヤニヤ）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2183, 255, 100, 0)    #voice#Elie
    Fade(250)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    OP_0D()
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0050
    ChrTalk(
        0xB,
        (
            "#00115F#11P#4Sああもう、違うの！\x02\x03",

            "#00112F#3Sティオちゃん、ノエルさんも！\x01",
            "誤解しないでね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x109,
        "#10112F#6Pえ、あ、はい……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#00204F#6P#N努力はしてみます。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0053
    ChrTalk(
        0xB,
        (
            "#00113F#11Pううっ、それじゃあ\x01",
            "リーシャさんは──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0054
    ChrTalk(
        0xB,
        (
            "#00105F#11P#30W………あら…………\x02\x03",

            "ど、どうして\x01",
            "リーシャさんが一緒に？\x02\x03",

            "#00108Fそれにノエルさんもいるし、\x01",
            "ワジ君はそんな格好をしてるし……\x02\x03",

            "#00105F？？？？？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00012F#11Pはは……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x106,
        "#10710F#6Pその……色々ありまして。\x02",
    )

    CloseMessageWindow()

    #N0057
    NpcTalk(
        0xC,
        "老人の声",
        (
            "#3P#2Sフフ……\x01",
            "どうやらそのようだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(16500, 1500, 20000, 0)
    OP_68(3500, 1500, 20000, 6000)

    def lambda_29E4():

        label("loc_29E4")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_29E4")

    QueueWorkItem2(0x101, 2, lambda_29E4)

    def lambda_29F6():

        label("loc_29F6")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_29F6")

    QueueWorkItem2(0xB, 2, lambda_29F6)
    BeginChrThread(0xC, 3, 0, 38)
    Sleep(300)
    BeginChrThread(0xD, 3, 0, 39)
    Sleep(3000)

    def lambda_2A1A():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x6A4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A1A)

    def lambda_2A34():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2A34)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xB, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0xB, 0x2)
    OP_93(0x101, 0xE1, 0x1F4)
    OP_93(0xB, 0x10E, 0x1F4)
    OP_6F(0x79)

    #C0058
    ChrTalk(
        0x101,
        "#00002F#5P議長、ご無事でしたか。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        "#00205F#6P#Nそれに……ヨナ！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xD,
        (
            "#02309F#11Pよ、アンタら。\x01",
            "随分久しぶりじゃん。\x02\x03",

            "#02302Fいや～、ホント助かったぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xB,
        (
            "#00100F#11Pえっと、彼は私たちの後に\x01",
            "ベルに連れて来られたの。\x02\x03",

            "#00106F何でもオルキスタワーの中枢に\x01",
            "ハッキングを繰り返したみたいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xD,
        (
            "#02310F#11Pあの女、マジアクマだぜ！\x02\x03",

            "よりにもよって\x01",
            "導力ネットがない屋敷に\x01",
            "このボクを閉じ込めやがって！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00012F#5Pな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        (
            "#00204F#6P#N確かにあなたにとっては\x01",
            "一番のお灸でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xC,
        (
            "#02503F#11Pまあ、お互いの事情は後だ。\x02\x03",

            "#02500Fどうやら私たちを\x01",
            "助けに来てくれたようだが？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0066
    ChrTalk(
        0x101,
        (
            "#00013F#5Pはい……！\x01",
            "お迎えにあがりました！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x105,
        (
            "#10400F#6P特に問題がなければ\x01",
            "このまま脱出してもらえるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xC,
        (
            "#02503F#11P勿論だとも。\x02\x03",

            "#02501F安穏#4Rあんのん#としていられる状況は\x01",
            "とうに過ぎ去っているからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        "#00106F#11Pはい……\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#00301F#6Pよし、叔父貴どもの増援が\x01",
            "来る前にとっとと脱出するか！\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x109,
        (
            "#10101F#6P退路を確保しつつ、\x01",
            "メルカバに戻りましょう！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    StopSound(124, 1000, 40)
    SetCameraDistance(14300, 1000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちは\x01",
            "陽動に出ていたツァイトと合流して\x01",
            "メルカバに戻り……\x02\x03",

            "《赤い星座》の増援が来る前に\x01",
            "ミシュラムから離脱することに成功した。\x02\x03",

            "そして──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_24(0x388)
    OP_24(0x243)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 7)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_F92 end

    def Function_12_2FBA(): pass

    label("Function_12_2FBA")


    def lambda_2FBF():
        OP_A6(0xFE, 0x0, 0x14, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FBF)
    WaitChrThread(0xFE, 2)
    Sound(905, 0, 70, 0)
    Sound(954, 0, 100, 0)

    def lambda_2FE8():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FE8)
    OP_A1(0xFE, 0x3E8, 0x4, 0x3, 0x2, 0x1, 0x0)
    OP_82(0x64, 0x64, 0x1388, 0x1F4)
    Sound(902, 0, 50, 0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_12_2FBA end

    def Function_13_3022(): pass

    label("Function_13_3022")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_3022 end

    def Function_14_3067(): pass

    label("Function_14_3067")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_14_3067 end

    def Function_15_30A5(): pass

    label("Function_15_30A5")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_30A5 end

    def Function_16_30CF(): pass

    label("Function_16_30CF")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(750)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(750)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_16_30CF end

    def Function_17_30EB(): pass

    label("Function_17_30EB")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_17_30EB end

    def Function_18_30FD(): pass

    label("Function_18_30FD")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_18_30FD end

    def Function_19_310F(): pass

    label("Function_19_310F")

    Sound(905, 0, 100, 0)
    Fade(500)
    SetCameraDistance(14000, 500)
    Sound(904, 2, 100, 0)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    Sound(951, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(2000, 2000, 21000, 500)
    MoveCamera(345, 21, 0, 500)
    OP_6E(600, 500)
    SetCameraDistance(15000, 500)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 2000, 22000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x12C)
    Sound(833, 0, 100, 0)
    Sound(902, 0, 100, 0)
    Sound(2030, 255, 100, 0)    #voice#Lloyd
    BeginChrThread(0x101, 3, 0, 20)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    CancelBlur(500)
    Return()

    # Function_19_310F end

    def Function_20_3207(): pass

    label("Function_20_3207")

    OP_93(0xFE, 0x13B, 0x0)
    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_322D():
        OP_9D(0xFE, 0x125C, 0x1F4, 0x4E20, 0x3E8, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_322D)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x3)
    Sound(514, 0, 100, 0)
    Sleep(500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_3207 end

    def Function_21_326D(): pass

    label("Function_21_326D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3290")
    OP_A6(0x8, 0x1E, 0x1E, 0x1F4, 0x1388)
    Jump("Function_21_326D")

    label("loc_3290")

    Return()

    # Function_21_326D end

    def Function_22_3291(): pass

    label("Function_22_3291")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32DB")
    PlayEffect(0x8, 0xFF, 0x8, 0x0, 0, -300, -500, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_22_3291")

    label("loc_32DB")

    Return()

    # Function_22_3291 end

    def Function_23_32DC(): pass

    label("Function_23_32DC")

    OP_68(0, 2000, 22500, 500)
    Sound(905, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    BeginChrThread(0x8, 2, 0, 22)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x4)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    OP_68(1000, 2000, 14450, 1000)
    MoveCamera(330, 20, 0, 1000)
    OP_6E(600, 1000)
    SetCameraDistance(15000, 1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChip(0x0, 0xFE, 0x96, 0x2BC)
    Sound(579, 2, 100, 0)

    def lambda_3360():
        OP_9B(0x0, 0xFE, 0xFFEC, 0x2CEC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3360)

    def lambda_3375():

        label("loc_3375")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3375")

    QueueWorkItem2(0x103, 2, lambda_3375)

    def lambda_3387():

        label("loc_3387")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3387")

    QueueWorkItem2(0x104, 2, lambda_3387)

    def lambda_3399():

        label("loc_3399")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3399")

    QueueWorkItem2(0x109, 2, lambda_3399)

    def lambda_33AB():

        label("loc_33AB")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_33AB")

    QueueWorkItem2(0x105, 2, lambda_33AB)

    def lambda_33BD():

        label("loc_33BD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_33BD")

    QueueWorkItem2(0x106, 2, lambda_33BD)
    Sleep(100)
    Sound(844, 0, 100, 0)
    BeginChrThread(0x109, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 24)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 27)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x106, 3, 0, 28)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x106, 3)
    WaitChrThread(0xFE, 1)
    OP_24(0x243)
    PlayEffect(0x1, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x12C)
    Sound(833, 0, 70, 0)
    Sound(902, 0, 100, 0)
    Sleep(500)
    CancelBlur(500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x106, 0x2)
    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()

    #C0073
    ChrTalk(
        0x104,
        (
            "#00310F#5P#Nチッ……\x01",
            "暴走してんのか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0xFE, 0x13E, 0x1F4)
    OP_68(-5550, 2000, 23200, 1200)
    MoveCamera(315, 26, 0, 1200)
    OP_6E(600, 1200)
    SetCameraDistance(19000, 1200)
    SetChrChip(0x0, 0xFE, 0x96, 0x2BC)
    Sound(579, 2, 100, 0)

    def lambda_3518():
        OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3518)

    def lambda_352D():

        label("loc_352D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_352D")

    QueueWorkItem2(0x103, 2, lambda_352D)

    def lambda_353F():

        label("loc_353F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_353F")

    QueueWorkItem2(0x104, 2, lambda_353F)

    def lambda_3551():

        label("loc_3551")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3551")

    QueueWorkItem2(0x109, 2, lambda_3551)

    def lambda_3563():

        label("loc_3563")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3563")

    QueueWorkItem2(0x105, 2, lambda_3563)

    def lambda_3575():

        label("loc_3575")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3575")

    QueueWorkItem2(0x106, 2, lambda_3575)
    Sleep(350)
    BeginChrThread(0x103, 3, 0, 29)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 32)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 31)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0x106, 3, 0, 33)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x106, 3)
    WaitChrThread(0xFE, 1)
    OP_24(0x243)
    PlayEffect(0x1, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x12C)
    Sound(833, 0, 70, 0)
    Sound(902, 0, 100, 0)
    Sleep(500)
    CancelBlur(500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x106, 0x2)
    OP_6F(0x79)
    OP_93(0xFE, 0x78, 0x1F4)
    OP_68(3150, 2300, 19400, 1000)
    MoveCamera(300, 20, 0, 1000)
    OP_6E(600, 1000)
    SetCameraDistance(14700, 1000)
    SetChrChip(0x0, 0xFE, 0x96, 0x2BC)
    Sound(844, 0, 100, 0)
    ClearChrFlags(0xFE, 0x1)

    def lambda_369D():
        OP_9D(0xFE, 0xA8C, 0x1F4, 0x56B8, 0xBB8, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_369D)

    def lambda_36BA():

        label("loc_36BA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_36BA")

    QueueWorkItem2(0x103, 2, lambda_36BA)

    def lambda_36CC():

        label("loc_36CC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_36CC")

    QueueWorkItem2(0x104, 2, lambda_36CC)

    def lambda_36DE():

        label("loc_36DE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_36DE")

    QueueWorkItem2(0x109, 2, lambda_36DE)

    def lambda_36F0():

        label("loc_36F0")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_36F0")

    QueueWorkItem2(0x105, 2, lambda_36F0)

    def lambda_3702():

        label("loc_3702")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3702")

    QueueWorkItem2(0x106, 2, lambda_3702)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x2)
    EndChrThread(0x8, 0x2)
    PlayEffect(0x1, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x12C)
    Sound(833, 0, 70, 0)
    Sound(902, 0, 100, 0)
    Sleep(500)
    CancelBlur(500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x106, 0x2)

    def lambda_37B0():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_37B0)
    Sleep(50)

    def lambda_37C0():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_37C0)
    Sleep(50)

    def lambda_37D0():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_37D0)
    Sleep(50)

    def lambda_37E0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37E0)
    Sleep(50)

    def lambda_37F0():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_37F0)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)
    Return()

    # Function_23_32DC end

    def Function_24_3812(): pass

    label("Function_24_3812")


    #C0074
    ChrTalk(
        0x103,
        "#00210F#6Pきゃあ……！？\x05\x02",
    )

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFF9C, 0x1F4, 0x40A6, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_3812 end

    def Function_25_3858(): pass

    label("Function_25_3858")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF22C, 0x1F4, 0x49B6, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_3858 end

    def Function_26_3880(): pass

    label("Function_26_3880")

    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFB5A, 0x1F4, 0x4998, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_3880 end

    def Function_27_38A8(): pass

    label("Function_27_38A8")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFBBE, 0x1F4, 0x4376, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    #C0075
    ChrTalk(
        0x105,
        "#10410F#5Pくっ……\x05\x02",
    )

    Return()

    # Function_27_38A8 end

    def Function_28_38E8(): pass

    label("Function_28_38E8")

    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF5D8, 0x1F4, 0x42AE, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_38E8 end

    def Function_29_3910(): pass

    label("Function_29_3910")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFBC8, 0x1F4, 0x3DB8, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_3910 end

    def Function_30_3971(): pass

    label("Function_30_3971")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFE93A, 0x1F4, 0x5014, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_3971 end

    def Function_31_39D2(): pass

    label("Function_31_39D2")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF4A2, 0x1F4, 0x45D8, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_39D2 end

    def Function_32_3A33(): pass

    label("Function_32_3A33")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF47A, 0x1F4, 0x3FDE, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_3A33 end

    def Function_33_3A94(): pass

    label("Function_33_3A94")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFEAD4, 0x1F4, 0x4902, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_3A94 end

    def Function_34_3AF5(): pass

    label("Function_34_3AF5")

    Sound(530, 0, 100, 0)
    Sound(566, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 15000, 2500, 20000, 282, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sound(902, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 2000, 0, 270, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3B7D():
        OP_A6(0xFE, 0x0, 0x4B, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B7D)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x3)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(2600, 2300, 22500, 150)
    OP_82(0x12C, 0x12C, 0x1388, 0x12C)

    def lambda_3BCB():
        OP_96(0xFE, 0x79E, 0x1F4, 0x5A6E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BCB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_6F(0x79)
    Sleep(800)
    Sound(530, 0, 100, 0)
    Sound(566, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 15000, 2500, 20000, 283, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sound(902, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 2000, 0, 270, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3C75():
        OP_A6(0xFE, 0x0, 0x4B, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C75)
    SetChrSubChip(0xFE, 0x2)
    OP_68(1150, 2300, 22050, 150)
    OP_82(0x12C, 0x12C, 0x1388, 0x12C)

    def lambda_3CB4():
        OP_96(0xFE, 0x258, 0x1F4, 0x5816, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CB4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_6F(0x79)
    Sound(530, 0, 100, 0)
    Sound(566, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 15000, 2500, 20000, 278, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sound(902, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 2000, 0, 270, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3D5B():
        OP_A6(0xFE, 0x0, 0x4B, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D5B)
    SetChrSubChip(0xFE, 0x1)
    OP_68(850, 2300, 23100, 150)
    OP_82(0x12C, 0x12C, 0x1388, 0x12C)

    def lambda_3D9A():
        OP_96(0xFE, 0x0, 0x1F4, 0x5DC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D9A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_6F(0x79)
    Return()

    # Function_34_3AF5 end

    def Function_35_3DBA(): pass

    label("Function_35_3DBA")

    OP_68(-1500, 2300, 22700, 500)
    MoveCamera(45, 27, 0, 500)
    OP_6E(600, 500)
    SetCameraDistance(11000, 500)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x1)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFF9F2, 0x1F4, 0x5C30, 0x3E8, 0x1388)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_6F(0x79)
    #Sound(2315, 255, 100, 0)    #voice#Randy

    #C0076
    ChrTalk(
        0x104,
        "#00307F#3Pおらあああっ！\x05\x02",
    )

    Sound(532, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    BeginChrThread(0x8, 3, 0, 37)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x4, 0x5)
    WaitChrThread(0x8, 3)
    EndChrThread(0x8, 0x0)
    Return()

    # Function_35_3DBA end

    def Function_36_3E76(): pass

    label("Function_36_3E76")

    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x1)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    OP_9D(0xFE, 0xFFFFFB82, 0x1F4, 0x57BC, 0x3E8, 0x1388)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(250)
    #Sound(3183, 255, 100, 1)    #voice#Rixia

    #C0077
    ChrTalk(
        0x106,
        "#10707F#4Pはあっ……！\x05\x02",
    )

    Sound(538, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x35)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x4, 0x5)
    Return()

    # Function_36_3E76 end

    def Function_37_3EEF(): pass

    label("Function_37_3EEF")

    OP_93(0xFE, 0xE1, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Sound(196, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -670, 2000, 23530, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(50)
    OP_68(2170, 2400, 26370, 500)
    OP_96(0xFE, 0xA14, 0x1F4, 0x689C, 0x3A98, 0x0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    CancelBlur(500)
    Sleep(500)
    OP_6F(0x79)
    Sound(546, 0, 100, 0)
    StopEffect(0x7, 0x2)
    PlayEffect(0x4, 0x0, 0xFF, 0x0, 2020, 2500, 26630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x1, 0xFF, 0x0, 2820, 1750, 25760, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, 0x0, 1260, 2000, 27380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x3, 0xFF, 0x0, 2410, 3000, 26190, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetCameraDistance(10000, 2500)
    Sleep(1500)
    Sound(546, 0, 100, 0)
    OP_6F(0x79)
    Fade(250)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(8000, 250)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x12C, 0x12C, 0x1388, 0x7D0)
    SetCameraDistance(23500, 500)
    Sound(200, 0, 100, 0)
    Sound(833, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 2580, 500, 26780, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    EndChrThread(0xE, 0x1)
    StopSound(904, 500, 100)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    OP_6F(0x79)
    CancelBlur(2000)
    Return()

    # Function_37_3EEF end

    def Function_38_4159(): pass

    label("Function_38_4159")

    ClearChrFlags(0xFE, 0x4)

    def lambda_4163():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4163)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_38_4159 end

    def Function_39_4188(): pass

    label("Function_39_4188")

    ClearChrFlags(0xFE, 0x4)

    def lambda_4192():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4192)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_39_4188 end

    def Function_40_41B7(): pass

    label("Function_40_41B7")

    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(1100)
    Sound(203, 0, 60, 0)
    Return()

    # Function_40_41B7 end

    def Function_41_41D0(): pass

    label("Function_41_41D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4204")
    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(1100)
    Sound(203, 0, 60, 0)
    Sleep(800)
    Sound(203, 0, 50, 0)
    Sleep(1000)
    Jump("Function_41_41D0")

    label("loc_4204")

    Return()

    # Function_41_41D0 end

    SaveToFile()

Try(main)
