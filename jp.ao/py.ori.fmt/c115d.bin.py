from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c115d.bin",                # FileName
        "c115d",                    # MapName
        "c115d",                    # Location
        0x0018,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 2500, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "c115d",                  # 0
        "フラン",                 # 1
        "ドノバン警部",           # 2
        "レイモンド捜査官",       # 3
        "警官隊",                 # 4
        "警官隊",                 # 5
        "警官隊",                 # 6
        "警官隊",                 # 7
        "SE制御",                 # 8
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(404, 0)                                        # 0

    ScpFunction((
        "Function_0_194",          # 00, 0
        "Function_1_1A4",          # 01, 1
        "Function_2_1A5",          # 02, 2
        "Function_3_D09",          # 03, 3
        "Function_4_D2E",          # 04, 4
        "Function_5_D53",          # 05, 5
        "Function_6_D6C",          # 06, 6
        "Function_7_D85",          # 07, 7
    ))


    def Function_0_194(): pass

    label("Function_0_194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1A3")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_1A3")

    Return()

    # Function_0_194 end

    def Function_1_1A4(): pass

    label("Function_1_1A4")

    Return()

    # Function_1_1A4 end

    def Function_2_1A5(): pass

    label("Function_2_1A5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06900.itc", 0x1E)
    LoadChrToIndex("chr/ch30300.itc", 0x23)
    LoadChrToIndex("apl/ch51509.itc", 0x24)
    LoadChrToIndex("apl/ch51508.itc", 0x28)
    LoadChrToIndex("apl/ch51236.itc", 0x2D)
    LoadEffect(0x0, "event/ev15025.eff")
    LoadEffect(0x1, "event/ev15026.eff")
    LoadEffect(0x2, "battle/ms00101.eff")
    LoadEffect(0x3, "event/ev15010.eff")
    SoundLoad(2720)
    SoundLoad(2721)
    SoundLoad(2722)
    SoundLoad(868)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xC, 0x2D)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetMapObjFlags(0x11, 0x1000)
    SetMapObjFrame(0xFF, "isu", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu_sd", 0x0, 0x1)
    SetMapObjFrame(0xFF, "stop", 0x0, 0x1)
    SetChrPos(0x8, -19150, -1950, 6300, 90)
    SetChrPos(0x9, -1900, 0, 11450, 180)
    SetChrPos(0xA, -3000, 0, 11850, 180)
    SetChrPos(0xC, 4700, 0, 10710, 225)
    SetChrPos(0xD, 2800, 0, 13150, 180)
    SetChrPos(0xE, 850, 0, 15100, 180)
    OP_68(0, 1000, 1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(15000, 0)
    OP_68(0, 1000, 2000, 3000)
    BeginChrThread(0x9, 1, 0, 3)
    BeginChrThread(0xF, 1, 0, 7)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x9, 0x1)
    BeginChrThread(0x9, 1, 0, 4)
    OP_68(-2550, 1000, 8600, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25400, 0)
    OP_68(-2550, 1000, 11600, 3000)
    SetCameraDistance(22400, 3000)
    Sleep(2000)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0001
    ChrTalk(
        0xA,
        "#5Pひ、ひいいいっ……！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(50)

    #C0002
    ChrTalk(
        0xA,
        (
            "#5P警部、早く僕らも\x01",
            "地下に避難しましょうよ～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    #C0003
    ChrTalk(
        0x9,
        (
            "バカヤロウ！\x01",
            "まだ各階の避難が\x01",
            "完了してねぇだろうが！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "それより気を抜くな！\x01",
            "いつシャッターが破られても\x01",
            "おかしくねえんだぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xA,
        (
            "#5Pだ、大丈夫ですよ！\x01",
            "警備隊が暴れた時だって\x01",
            "破られなかったくらいですから！\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xA,
        "#5Pだから僕らも早く避難を……！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-15350, 1000, 6300, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20400, 0)
    OP_68(-3350, 1000, 11500, 4000)
    MoveCamera(45, 24, 0, 4000)
    OP_6E(400, 4000)
    SetCameraDistance(22400, 4000)
    OP_95(0x8, -15350, 0, 6300, 4000, 0x0)
    OP_95(0x8, -8500, 0, 10000, 4000, 0x0)
    OP_95(0x8, -4750, 0, 11550, 4000, 0x0)
    TurnDirection(0x8, 0x9, 500)
    OP_0D()
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    #C0007
    ChrTalk(
        0x8,
        (
            "#01901F#2720V#6P#30W全職員、地下の機密区画に\x01",
            "避難完了しましたー！\x02\x03",

            "#2721V#30W皆さんも早く来てください！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAA1)
    OP_C9(0x1, 0x80000000)
    SetChrSubChip(0xA, 0x2)

    def lambda_692():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_692)
    Sleep(50)

    def lambda_6A2():
        TurnDirection(0xB, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_6A2)
    Sleep(50)

    def lambda_6B2():
        TurnDirection(0xC, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_6B2)
    Sleep(50)

    def lambda_6C2():
        TurnDirection(0xD, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6C2)
    Sleep(50)

    def lambda_6D2():
        TurnDirection(0xE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_6D2)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)

    #C0008
    ChrTalk(
        0x9,
        "#11Pおお、ご苦労さん！\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xA,
        "#5P助かった、これで──\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x9, -2650, 0, 11450, 180)
    SetChrPos(0xA, -3750, 0, 11850, 180)
    SetChrPos(0x8, -5000, 0, 11550, 180)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xF, 0x1)
    OP_68(-490, 1000, 1890, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Sound(880, 0, 100, 0)
    Sound(200, 0, 100, 0)
    Sound(868, 2, 50, 0)
    OP_68(0, 1000, 5000, 300)
    MoveCamera(40, 20, 0, 300)
    SetCameraDistance(18000, 300)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0x0, 0x50, 0x0, 0x0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 0, 0, 1000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(200)
    OP_82(0x64, 0x64, 0xBB8, 0x5DC)
    Sleep(800)
    OP_68(-3700, 1000, 11100, 3000)
    MoveCamera(35, 25, 0, 3000)
    SetCameraDistance(22000, 3000)
    SetChrSubChip(0xA, 0x0)

    def lambda_952():
        OP_92(0x9, 0x0, 0x9C4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_952)
    Sleep(50)

    def lambda_968():
        OP_92(0x8, 0x0, 0x9C4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_968)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x8, 0)

    def lambda_986():
        OP_92(0xB, 0x0, 0x9C4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_986)
    Sleep(50)

    def lambda_99C():
        OP_92(0xC, 0x0, 0x9C4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_99C)
    Sleep(50)

    def lambda_9B2():
        OP_92(0xD, 0x0, 0x9C4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_9B2)
    Sleep(50)

    def lambda_9C8():
        OP_92(0xE, 0x0, 0x9C4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_9C8)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    OP_79(0x11)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0xFA0)
    OP_6F(0x79)

    #C0010
    ChrTalk(
        0xA,
        "#5Pへ……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "#5Pしまった！\x01",
            "急いで地下へ──\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(0, 1000, 1500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21750, 0)
    OP_68(-3350, 800, 11350, 3000)
    MoveCamera(45, 30, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15500, 3000)
    BeginChrThread(0xF, 1, 0, 5)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 100, -1000, -31, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_ACD():
        OP_92(0x9, 0xFFFFF5A6, 0x235A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_ACD)
    Sleep(50)

    def lambda_AE3():
        OP_92(0xA, 0xFFFFF5A6, 0x235A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_AE3)
    Sleep(50)

    def lambda_AF9():
        OP_92(0x8, 0xFFFFF5A6, 0x235A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_AF9)
    Sleep(50)

    def lambda_B0F():
        OP_92(0xC, 0xFFFFF5A6, 0x235A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_B0F)
    Sleep(50)

    def lambda_B25():
        OP_92(0xD, 0xFFFFF5A6, 0x235A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_B25)
    Sleep(50)

    def lambda_B3B():
        OP_92(0xE, 0xFFFFF5A6, 0x235A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_B3B)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    OP_0D()
    Sleep(1500)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_6F(0x79)

    #C0012
    ChrTalk(
        0xA,
        "#5P#25Aば、爆弾……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0013
    ChrTalk(
        0x9,
        "#5P#13Aくそおおおおおっ！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0xF, 1, 0, 6)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -2650, 0, 8550, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_C9(0x0, 0x80000000)

    #C0014
    ChrTalk(
        0x8,
        "#01911F#2722V#6P#40W#10Aお姉ちゃん──\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    FadeToDark(1000, 16777215, -1)
    OP_82(0x64, 0x64, 0xBB8, 0xBB8)
    StopSound(868, 2000, 40)
    SetChrFlags(0xA, 0x20)

    def lambda_C91():
        OP_9A(0xFE, 0x8, 0x0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C91)

    def lambda_CA5():
        OP_A0(0xFE, 500, 0x3, 0x4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_CA5)
    SetChrChipByIndex(0x9, 0x24)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x20)

    def lambda_CC0():
        OP_96(0xFE, 0xFFFFEC78, 0x0, 0x2B2A, 0x352, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CC0)

    def lambda_CDA():
        OP_A0(0xFE, 500, 0x0, 0x3)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_CDA)
    SetChrChipByIndex(0x8, 0x28)
    SetChrFlags(0x8, 0x2)

    def lambda_CF0():
        OP_A0(0xFE, 500, 0x5, 0x6)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_CF0)
    OP_0D()
    Sleep(2000)
    SetScenarioFlags(0x22, 1)
    NewScene("c150B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1A5 end

    def Function_3_D09(): pass

    label("Function_3_D09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D2D")
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sleep(800)
    Jump("Function_3_D09")

    label("loc_D2D")

    Return()

    # Function_3_D09 end

    def Function_4_D2E(): pass

    label("Function_4_D2E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D52")
    OP_82(0x14, 0x0, 0xBB8, 0x1F4)
    Sleep(800)
    Jump("Function_4_D2E")

    label("loc_D52")

    Return()

    # Function_4_D2E end

    def Function_5_D53(): pass

    label("Function_5_D53")

    Sound(809, 0, 70, 0)
    Sleep(1200)
    Sound(555, 0, 100, 0)
    Sleep(500)
    Sound(555, 0, 100, 0)
    Return()

    # Function_5_D53 end

    def Function_6_D6C(): pass

    label("Function_6_D6C")

    Sound(934, 0, 60, 0)
    Sleep(1500)
    Sound(556, 0, 100, 0)
    Sleep(500)
    Sound(200, 0, 80, 0)
    Return()

    # Function_6_D6C end

    def Function_7_D85(): pass

    label("Function_7_D85")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DB3")
    Sound(196, 0, 50, 0)
    Sound(880, 0, 50, 0)
    Sleep(700)
    Sound(196, 0, 40, 0)
    Sound(880, 0, 40, 0)
    Sleep(1200)
    Jump("Function_7_D85")

    label("loc_DB3")

    Return()

    # Function_7_D85 end

    SaveToFile()

Try(main)
