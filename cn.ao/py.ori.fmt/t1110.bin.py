from ScenarioHelper import *

def main():
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
        "声音",                   # 1
        "声音",                   # 2
        "声音",                   # 3
        "艾莉",                   # 4
        "麦克道尔议长",           # 5
        "约纳",                   # 6
        "SE控制",                 # 7
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
        "Function_3_CF6",          # 03, 3
        "Function_4_D1B",          # 04, 4
        "Function_5_D7C",          # 05, 5
        "Function_6_E63",          # 06, 6
        "Function_7_EBE",          # 07, 7
        "Function_8_F0D",          # 08, 8
        "Function_9_F2C",          # 09, 9
        "Function_10_F48",         # 0A, 10
        "Function_11_F64",         # 0B, 11
        "Function_12_2E68",        # 0C, 12
        "Function_13_2ED0",        # 0D, 13
        "Function_14_2F15",        # 0E, 14
        "Function_15_2F53",        # 0F, 15
        "Function_16_2F7D",        # 10, 16
        "Function_17_2F99",        # 11, 17
        "Function_18_2FAB",        # 12, 18
        "Function_19_2FBD",        # 13, 19
        "Function_20_30B5",        # 14, 20
        "Function_21_311B",        # 15, 21
        "Function_22_313F",        # 16, 22
        "Function_23_318A",        # 17, 23
        "Function_24_36B8",        # 18, 24
        "Function_25_36F8",        # 19, 25
        "Function_26_3720",        # 1A, 26
        "Function_27_3748",        # 1B, 27
        "Function_28_3786",        # 1C, 28
        "Function_29_37AE",        # 1D, 29
        "Function_30_380F",        # 1E, 30
        "Function_31_3870",        # 1F, 31
        "Function_32_38D1",        # 20, 32
        "Function_33_3932",        # 21, 33
        "Function_34_3993",        # 22, 34
        "Function_35_3C58",        # 23, 35
        "Function_36_3D10",        # 24, 36
        "Function_37_3D85",        # 25, 37
        "Function_38_3FEF",        # 26, 38
        "Function_39_401E",        # 27, 39
        "Function_40_404D",        # 28, 40
        "Function_41_4066",        # 29, 41
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
        "#00008F#11P一个人都没有……？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x106,
        (
            "#10708F#12P不……\x01",
            "我能感觉到某种反应。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x105,
        (
            "#10401F#12P嗯，但似乎不是\x01",
            "魔兽之类的东西。\x02",
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
            "Ｐ……发现入侵者。\x07\x00\x02",
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
        "#00207F#11P正面出现反应！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#00310F#11P啧……\x01",
            "扎克斯指的就是这家伙啊！\x02",
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
            "目标共六名。\x02",
        )
    )

    CloseMessageWindow()

    #A0008
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "包括三名特别任务支援科成员，\x01",
            "以及国防军的希卡少尉。\x02",
        )
    )

    CloseMessageWindow()

    #A0009
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外两名身份不明，\x01",
            "推测战斗力为Ａ级以上。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0010
    ChrTalk(
        0x105,
        "#10407F#12P#N什么……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0011
    ChrTalk(
        0x106,
        "#10707F#6P#N机械装置竟能如此……！\x02",
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
            "出动『十六夜』。\x02",
        )
    )

    CloseMessageWindow()

    #A0013
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "红色电磁傲武者Ⅱ型──\x01",
            "『村正』……\x02",
        )
    )

    CloseMessageWindow()

    #A0014
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开始执行歼灭行动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0015
    ChrTalk(
        0x101,
        "#00010F#12P#N来了……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0016
    ChrTalk(
        0x109,
        "#10107F#12P#N开始迎击！\x02",
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

    def lambda_C69():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C69)

    def lambda_C7E():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C7E)

    def lambda_C93():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C93)
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

    def Function_3_CF6(): pass

    label("Function_3_CF6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D1A")
    OP_82(0x0, 0x1E, 0x1388, 0x3E8)
    Sleep(1000)
    Jump("Function_3_CF6")

    label("loc_D1A")

    Return()

    # Function_3_CF6 end

    def Function_4_D1B(): pass

    label("Function_4_D1B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D7B")
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x96, 0x2EE)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xC8, 0x2EE)
    StopEffect(0x0, 0x2)
    Jump("Function_4_D1B")

    label("loc_D7B")

    Return()

    # Function_4_D1B end

    def Function_5_D7C(): pass

    label("Function_5_D7C")

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

    # Function_5_D7C end

    def Function_6_E63(): pass

    label("Function_6_E63")

    Sound(950, 2, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
    StopEffect(0x1, 0x2)
    StopSound(950, 1000, 100)
    BeginChrThread(0xFE, 0, 0, 10)
    Sleep(1000)
    Return()

    # Function_6_E63 end

    def Function_7_EBE(): pass

    label("Function_7_EBE")

    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
    StopEffect(0x2, 0x2)
    BeginChrThread(0xFE, 0, 0, 10)
    Sleep(1000)
    Return()

    # Function_7_EBE end

    def Function_8_F0D(): pass

    label("Function_8_F0D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F2B")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_8_F0D")

    label("loc_F2B")

    Return()

    # Function_8_F0D end

    def Function_9_F2C(): pass

    label("Function_9_F2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F47")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_9_F2C")

    label("loc_F47")

    Return()

    # Function_9_F2C end

    def Function_10_F48(): pass

    label("Function_10_F48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F63")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_10_F48")

    label("loc_F63")

    Return()

    # Function_10_F48 end

    def Function_11_F64(): pass

    label("Function_11_F64")

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

    def lambda_1346():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1346)
    Sleep(50)

    def lambda_1362():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1362)
    Sleep(50)

    def lambda_137E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_137E)
    Sleep(50)

    def lambda_139A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_139A)
    Sleep(50)

    def lambda_13B6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_13B6)
    Sleep(50)

    def lambda_13D2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_13D2)
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
            "#00015F#12P唔……\x01",
            "好厉害的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x106,
        (
            "#10708F#12P#N『结社』真是个\x01",
            "可怕的集团啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0019
    ChrTalk(
        0x104,
        (
            "#00306F#12P嗯，竟然能把那架红色的\x01",
            "武装智能兵器强化到这种程度……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#00211F#12P……肯定是那个博士\x01",
            "改造的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x105,
        "#10406F#12P很有可能……\x02",
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

    def lambda_1584():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1584)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sound(812, 0, 100, 0)
    WaitChrThread(0x101, 2)
    OP_0D()
    Fade(500)

    def lambda_15B5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_15B5)
    Sleep(50)

    def lambda_15D1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_15D1)
    Sleep(50)

    def lambda_15ED():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_15ED)
    Sleep(50)

    def lambda_1609():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1609)
    Sleep(50)

    def lambda_1625():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1625)
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

    def lambda_1730():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1730)
    Sleep(50)

    def lambda_1740():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1740)
    Sleep(50)

    def lambda_1750():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1750)
    Sleep(50)

    def lambda_1760():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1760)
    Sleep(50)

    def lambda_1770():
        OP_93(0x106, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1770)
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
            "#00004F#5P好，我们已经把\x01",
            "所有障碍都消除了。\x02\x03",

            "#00000F这就开始在室内搜索，\x01",
            "寻找艾莉和议长他们……\x02",
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

    def lambda_186A():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_186A)
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
        "#00011F#6P什么……！？\x02",
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
        "#10110F#12P可恶……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 23)
    WaitChrThread(0x8, 3)

    def lambda_19BB():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_19BB)
    Sleep(50)

    def lambda_19CB():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_19CB)
    Sleep(50)

    def lambda_19DB():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_19DB)
    Sleep(50)

    def lambda_19EB():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_19EB)
    Sleep(50)

    def lambda_19FB():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_19FB)
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
        "#00010F#6P#N糟了……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)

    def lambda_1A5E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1A5E)
    Sleep(50)

    def lambda_1A7A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1A7A)
    Sleep(50)

    def lambda_1A96():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1A96)
    Sleep(50)

    def lambda_1AB2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1AB2)
    Sleep(50)

    def lambda_1ACE():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1ACE)
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
        "#10107F#5P罗伊德警官……！\x02",
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
        "女孩的声音",
        "#3403V#1P#10A休想得逞！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0x8, 3, 0, 34)
    WaitChrThread(0x8, 3)

    #C0028
    ChrTalk(
        0x101,
        "#00005F#5P#N#8A哎……？\x02",
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

    def lambda_1D2A():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D2A)
    Sleep(50)

    def lambda_1D3A():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D3A)
    Sleep(50)

    def lambda_1D4A():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D4A)
    Sleep(50)

    def lambda_1D5A():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1D5A)
    Sleep(50)

    def lambda_1D6A():
        OP_93(0x106, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1D6A)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    OP_68(1000, 1500, 20000, 1500)
    SetCameraDistance(13500, 1500)

    def lambda_1DA8():
        OP_9B(0x1, 0xFE, 0x1E, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1DA8)
    Sleep(50)

    def lambda_1DC0():
        OP_9B(0x1, 0xFE, 0xFFE7, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1DC0)
    Sleep(50)

    def lambda_1DD8():
        OP_9B(0x1, 0xFE, 0xFFDA, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DD8)
    Sleep(50)

    def lambda_1DF0():
        OP_9B(0x1, 0xFE, 0x21, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DF0)
    Sleep(50)

    def lambda_1E08():
        OP_9B(0x1, 0xFE, 0xFFE2, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1E08)
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
        "#00206F#6P#6P呼……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x105,
        "#10406F#6P……哎呀呀。\x02",
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
        "#00002F#6P#N艾莉……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, 4700, 500, 20000, 90)

    #C0032
    ChrTalk(
        0x103,
        "#00202F#6P#N……艾莉前辈。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0033
    ChrTalk(
        0x104,
        "#00309F#6P#N哈哈，看来你平安无事啊。\x02",
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

    def lambda_1F97():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F97)
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
            "#00012F#6P那个……\x01",
            "该说什么好呢。\x02\x03",

            "#00004F还是先道谢好了。\x01",
            "谢谢，艾莉。\x02\x03",

            "#00002F多亏你救了我。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xB,
        "#00101F#11P…………！\x02",
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

    def lambda_20C7():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20C7)
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
        "#00011F#6P#7A哇哇……！？\x02",
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
            "#3404V#40W#35A太好了……\x01",
            "……真是太好了……\x02\x03",

            "#3405V#35A你平安无事……\x01",
            "……我们又能再次相会……\x02\x03",

            "#3406V#35A本以为……\x01",
            "本以为以后再也无法见面了……\x02",
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
        "#00002F#6P艾莉……\x02",
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
        "#00309F#6P（唉，该说什么好呢……）\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        (
            "#10114F#6P（那个……我们现在插话\x01",
            "  是不是不太好呢……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x106,
        "#10706F#6P（真、真伤脑筋呢……）\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        (
            "#10402F#6P（说起来，和你重逢时好像也是这样，\x01",
            "  这家伙可真是赚大了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        "#00211F#6P（……我可不记得有这回事。）\x02",
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
        "#00105F#11P哎……？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈……\x02\x03",

            "……虽然很开心，\x01",
            "但大家的视线终究\x01",
            "让人有些不自在呢……\x02",
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
            "#00112F#11P你、你们不要误会啊！\x02\x03",

            "我只是因为看到\x01",
            "罗伊德陷入险境，\x01",
            "所以情绪一时有些激动而已！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x105,
        "#10402F#6P哦，这样啊。（毫无语气）\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        "#00309F#6P原来如此，原来如此。（坏笑）\x02",
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
            "#00115F#11P#4S啊啊！真是的！都说了不要误会啦！\x02\x03",

            "#00112F#3S缇欧！诺艾尔小姐！\x01",
            "你们可不要误会啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x109,
        "#10112F#6P哎……啊，好的……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#00204F#6P#N我会努力的。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0053
    ChrTalk(
        0xB,
        (
            "#00113F#11P呜呜……还有莉夏小姐，\x01",
            "你也——\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0054
    ChrTalk(
        0xB,
        (
            "#00105F#11P#30W………哎…………\x02\x03",

            "为、为何连莉夏小姐\x01",
            "都在呢？\x02\x03",

            "#00108F而且诺艾尔小姐也和大家在一起，\x01",
            "瓦吉还换上了那种打扮……\x02\x03",

            "#00105F？？？？？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00012F#11P哈哈……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x106,
        "#10710F#6P这个……说来话长了。\x02",
    )

    CloseMessageWindow()

    #N0057
    NpcTalk(
        0xC,
        "老人的声音",
        (
            "#3P#2S呵呵……\x01",
            "好像发生了不少事情啊。\x02",
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

    def lambda_2940():

        label("loc_2940")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2940")

    QueueWorkItem2(0x101, 2, lambda_2940)

    def lambda_2952():

        label("loc_2952")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2952")

    QueueWorkItem2(0xB, 2, lambda_2952)
    BeginChrThread(0xC, 3, 0, 38)
    Sleep(300)
    BeginChrThread(0xD, 3, 0, 39)
    Sleep(3000)

    def lambda_2976():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x6A4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2976)

    def lambda_2990():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2990)
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
        "#00002F#5P议长，您没事吧？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        "#00205F#6P#N约……约纳！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xD,
        (
            "#02309F#11P哟，你们好啊，\x01",
            "真是很久没见了。\x02\x03",

            "#02302F哈哈～终于得救了！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xB,
        (
            "#00100F#11P那个……他是在我们遭到软禁之后，\x01",
            "被贝尔带到这里来的。\x02\x03",

            "#00106F好像是因为他多次对\x01",
            "兰花塔的中枢展开黑客攻击。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xD,
        (
            "#02310F#11P那个女人简直就是恶魔！\x02\x03",

            "居然把我关在\x01",
            "这种没有导力网络\x01",
            "的房子里！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00012F#5P是、是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        (
            "#00204F#6P#N对你来说，\x01",
            "这的确是最大的酷刑呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xC,
        (
            "#02503F#11P好了，这些事情之后再谈。\x02\x03",

            "#02500F你们是来\x01",
            "救我们的吧？\x02",
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
            "#00013F#5P是的……！\x01",
            "我们是来接各位的！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x105,
        (
            "#10400F#6P如果没有什么特殊问题，\x01",
            "可以随我们一同离开此地吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xC,
        (
            "#02503F#11P当然。\x02\x03",

            "#02501F如今这种状况已经不容\x01",
            "我们继续置身事外了。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        "#00106F#11P是的……\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#00301F#6P好，那我们就在叔叔他们的\x01",
            "增援到来之前逃离此地吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x109,
        (
            "#10101F#6P在确保退路的同时，\x01",
            "返回梅尔卡瓦！\x02",
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
            "就这样，罗伊德等人\x01",
            "与完成佯攻的蔡特会合，\x01",
            "一起返回梅尔卡瓦……\x02\x03",

            "并在『赤色星座』增援部队赶来之前\x01",
            "成功逃离米修拉姆。\x02\x03",

            "随后……\x07\x00\x02",
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

    # Function_11_F64 end

    def Function_12_2E68(): pass

    label("Function_12_2E68")


    def lambda_2E6D():
        OP_A6(0xFE, 0x0, 0x14, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E6D)
    WaitChrThread(0xFE, 2)
    Sound(905, 0, 70, 0)
    Sound(954, 0, 100, 0)

    def lambda_2E96():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E96)
    OP_A1(0xFE, 0x3E8, 0x4, 0x3, 0x2, 0x1, 0x0)
    OP_82(0x64, 0x64, 0x1388, 0x1F4)
    Sound(902, 0, 50, 0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_12_2E68 end

    def Function_13_2ED0(): pass

    label("Function_13_2ED0")

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

    # Function_13_2ED0 end

    def Function_14_2F15(): pass

    label("Function_14_2F15")

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

    # Function_14_2F15 end

    def Function_15_2F53(): pass

    label("Function_15_2F53")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_2F53 end

    def Function_16_2F7D(): pass

    label("Function_16_2F7D")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(750)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(750)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_16_2F7D end

    def Function_17_2F99(): pass

    label("Function_17_2F99")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_17_2F99 end

    def Function_18_2FAB(): pass

    label("Function_18_2FAB")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_18_2FAB end

    def Function_19_2FBD(): pass

    label("Function_19_2FBD")

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

    # Function_19_2FBD end

    def Function_20_30B5(): pass

    label("Function_20_30B5")

    OP_93(0xFE, 0x13B, 0x0)
    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_30DB():
        OP_9D(0xFE, 0x125C, 0x1F4, 0x4E20, 0x3E8, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30DB)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x3)
    Sound(514, 0, 100, 0)
    Sleep(500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_30B5 end

    def Function_21_311B(): pass

    label("Function_21_311B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_313E")
    OP_A6(0x8, 0x1E, 0x1E, 0x1F4, 0x1388)
    Jump("Function_21_311B")

    label("loc_313E")

    Return()

    # Function_21_311B end

    def Function_22_313F(): pass

    label("Function_22_313F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3189")
    PlayEffect(0x8, 0xFF, 0x8, 0x0, 0, -300, -500, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_22_313F")

    label("loc_3189")

    Return()

    # Function_22_313F end

    def Function_23_318A(): pass

    label("Function_23_318A")

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

    def lambda_320E():
        OP_9B(0x0, 0xFE, 0xFFEC, 0x2CEC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_320E)

    def lambda_3223():

        label("loc_3223")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3223")

    QueueWorkItem2(0x103, 2, lambda_3223)

    def lambda_3235():

        label("loc_3235")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3235")

    QueueWorkItem2(0x104, 2, lambda_3235)

    def lambda_3247():

        label("loc_3247")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3247")

    QueueWorkItem2(0x109, 2, lambda_3247)

    def lambda_3259():

        label("loc_3259")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3259")

    QueueWorkItem2(0x105, 2, lambda_3259)

    def lambda_326B():

        label("loc_326B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_326B")

    QueueWorkItem2(0x106, 2, lambda_326B)
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
            "#00310F#5P#N啧……\x01",
            "失控了吗！？\x02",
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

    def lambda_33BE():
        OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33BE)

    def lambda_33D3():

        label("loc_33D3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_33D3")

    QueueWorkItem2(0x103, 2, lambda_33D3)

    def lambda_33E5():

        label("loc_33E5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_33E5")

    QueueWorkItem2(0x104, 2, lambda_33E5)

    def lambda_33F7():

        label("loc_33F7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_33F7")

    QueueWorkItem2(0x109, 2, lambda_33F7)

    def lambda_3409():

        label("loc_3409")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3409")

    QueueWorkItem2(0x105, 2, lambda_3409)

    def lambda_341B():

        label("loc_341B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_341B")

    QueueWorkItem2(0x106, 2, lambda_341B)
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

    def lambda_3543():
        OP_9D(0xFE, 0xA8C, 0x1F4, 0x56B8, 0xBB8, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3543)

    def lambda_3560():

        label("loc_3560")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3560")

    QueueWorkItem2(0x103, 2, lambda_3560)

    def lambda_3572():

        label("loc_3572")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3572")

    QueueWorkItem2(0x104, 2, lambda_3572)

    def lambda_3584():

        label("loc_3584")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3584")

    QueueWorkItem2(0x109, 2, lambda_3584)

    def lambda_3596():

        label("loc_3596")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3596")

    QueueWorkItem2(0x105, 2, lambda_3596)

    def lambda_35A8():

        label("loc_35A8")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_35A8")

    QueueWorkItem2(0x106, 2, lambda_35A8)
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

    def lambda_3656():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3656)
    Sleep(50)

    def lambda_3666():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3666)
    Sleep(50)

    def lambda_3676():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3676)
    Sleep(50)

    def lambda_3686():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3686)
    Sleep(50)

    def lambda_3696():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_3696)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)
    Return()

    # Function_23_318A end

    def Function_24_36B8(): pass

    label("Function_24_36B8")


    #C0074
    ChrTalk(
        0x103,
        "#00210F#6P呀……！\x05\x02",
    )

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFF9C, 0x1F4, 0x40A6, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_36B8 end

    def Function_25_36F8(): pass

    label("Function_25_36F8")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF22C, 0x1F4, 0x49B6, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_36F8 end

    def Function_26_3720(): pass

    label("Function_26_3720")

    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFB5A, 0x1F4, 0x4998, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_3720 end

    def Function_27_3748(): pass

    label("Function_27_3748")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFBBE, 0x1F4, 0x4376, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    #C0075
    ChrTalk(
        0x105,
        "#10410F#5P呜……\x05\x02",
    )

    Return()

    # Function_27_3748 end

    def Function_28_3786(): pass

    label("Function_28_3786")

    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF5D8, 0x1F4, 0x42AE, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_3786 end

    def Function_29_37AE(): pass

    label("Function_29_37AE")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFFBC8, 0x1F4, 0x3DB8, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_37AE end

    def Function_30_380F(): pass

    label("Function_30_380F")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFE93A, 0x1F4, 0x5014, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_380F end

    def Function_31_3870(): pass

    label("Function_31_3870")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF4A2, 0x1F4, 0x45D8, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_3870 end

    def Function_32_38D1(): pass

    label("Function_32_38D1")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFF47A, 0x1F4, 0x3FDE, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_38D1 end

    def Function_33_3932(): pass

    label("Function_33_3932")

    Sound(501, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0xFFFFEAD4, 0x1F4, 0x4902, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_3932 end

    def Function_34_3993(): pass

    label("Function_34_3993")

    Sound(530, 0, 100, 0)
    Sound(566, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 15000, 2500, 20000, 282, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sound(902, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 2000, 0, 270, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3A1B():
        OP_A6(0xFE, 0x0, 0x4B, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A1B)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x3)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(2600, 2300, 22500, 150)
    OP_82(0x12C, 0x12C, 0x1388, 0x12C)

    def lambda_3A69():
        OP_96(0xFE, 0x79E, 0x1F4, 0x5A6E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A69)
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

    def lambda_3B13():
        OP_A6(0xFE, 0x0, 0x4B, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B13)
    SetChrSubChip(0xFE, 0x2)
    OP_68(1150, 2300, 22050, 150)
    OP_82(0x12C, 0x12C, 0x1388, 0x12C)

    def lambda_3B52():
        OP_96(0xFE, 0x258, 0x1F4, 0x5816, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B52)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_6F(0x79)
    Sound(530, 0, 100, 0)
    Sound(566, 0, 50, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 15000, 2500, 20000, 278, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Sound(902, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 2000, 0, 270, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3BF9():
        OP_A6(0xFE, 0x0, 0x4B, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3BF9)
    SetChrSubChip(0xFE, 0x1)
    OP_68(850, 2300, 23100, 150)
    OP_82(0x12C, 0x12C, 0x1388, 0x12C)

    def lambda_3C38():
        OP_96(0xFE, 0x0, 0x1F4, 0x5DC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C38)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_6F(0x79)
    Return()

    # Function_34_3993 end

    def Function_35_3C58(): pass

    label("Function_35_3C58")

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
        "#00307F#3P哦啊啊啊！\x05\x02",
    )

    Sound(532, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    BeginChrThread(0x8, 3, 0, 37)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x4, 0x5)
    WaitChrThread(0x8, 3)
    EndChrThread(0x8, 0x0)
    Return()

    # Function_35_3C58 end

    def Function_36_3D10(): pass

    label("Function_36_3D10")

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
        "#10707F#4P喝……！\x05\x02",
    )

    Sound(538, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x35)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x4, 0x5)
    Return()

    # Function_36_3D10 end

    def Function_37_3D85(): pass

    label("Function_37_3D85")

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

    # Function_37_3D85 end

    def Function_38_3FEF(): pass

    label("Function_38_3FEF")

    ClearChrFlags(0xFE, 0x4)

    def lambda_3FF9():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FF9)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_38_3FEF end

    def Function_39_401E(): pass

    label("Function_39_401E")

    ClearChrFlags(0xFE, 0x4)

    def lambda_4028():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4028)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_39_401E end

    def Function_40_404D(): pass

    label("Function_40_404D")

    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(1100)
    Sound(203, 0, 60, 0)
    Return()

    # Function_40_404D end

    def Function_41_4066(): pass

    label("Function_41_4066")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_409A")
    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(1100)
    Sound(203, 0, 60, 0)
    Sleep(800)
    Sound(203, 0, 50, 0)
    Sleep(1000)
    Jump("Function_41_4066")

    label("loc_409A")

    Return()

    # Function_41_4066 end

    SaveToFile()

Try(main)
