from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3600.bin",                # FileName
        "e3600",                    # MapName
        "e3600",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3600",                  # 0
        "イリア",                 # 1
        "リーシャ",               # 2
        "シュリ",                 # 3
        "ユージーン",             # 4
        "テオドール",             # 5
        "ニコル",                 # 6
        "プリエ",                 # 7
        "セリーヌ",               # 8
        "血染めのシャーリィ",     # 9
        "猟兵",                   # 10
        "猟兵",                   # 11
        "猟兵",                   # 12
        "猟兵",                   # 13
        "観客",                   # 14
        "観客",                   # 15
        "観客",                   # 16
        "観客",                   # 17
        "観客",                   # 18
        "観客",                   # 19
        "観客",                   # 20
        "観客",                   # 21
        "観客",                   # 22
        "観客",                   # 23
        "観客",                   # 24
        "観客",                   # 25
        "観客",                   # 26
        "観客",                   # 27
        "観客",                   # 28
        "観客",                   # 29
        "観客",                   # 30
        "観客",                   # 31
        "観客",                   # 32
        "観客",                   # 33
        "降魔刀",                 # 34
        "SE制御",                 # 35
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1360, 0)                                       # 0

    ScpFunction((
        "Function_0_550",          # 00, 0
        "Function_1_574",          # 01, 1
        "Function_2_575",          # 02, 2
        "Function_3_2DC9",         # 03, 3
        "Function_4_2E0C",         # 04, 4
        "Function_5_2E25",         # 05, 5
        "Function_6_2E3E",         # 06, 6
        "Function_7_2E6E",         # 07, 7
        "Function_8_2E9E",         # 08, 8
        "Function_9_2ECE",         # 09, 9
        "Function_10_2F12",        # 0A, 10
        "Function_11_2F2E",        # 0B, 11
        "Function_12_2F5E",        # 0C, 12
        "Function_13_2F7A",        # 0D, 13
        "Function_14_2FAA",        # 0E, 14
        "Function_15_2FD3",        # 0F, 15
        "Function_16_3003",        # 10, 16
        "Function_17_302C",        # 11, 17
        "Function_18_305C",        # 12, 18
        "Function_19_3085",        # 13, 19
        "Function_20_30D5",        # 14, 20
        "Function_21_311B",        # 15, 21
        "Function_22_3161",        # 16, 22
        "Function_23_31A7",        # 17, 23
        "Function_24_31ED",        # 18, 24
        "Function_25_323D",        # 19, 25
        "Function_26_328D",        # 1A, 26
        "Function_27_32DD",        # 1B, 27
        "Function_28_32FE",        # 1C, 28
        "Function_29_3342",        # 1D, 29
        "Function_30_3386",        # 1E, 30
        "Function_31_33CA",        # 1F, 31
        "Function_32_340E",        # 20, 32
        "Function_33_3452",        # 21, 33
        "Function_34_3496",        # 22, 34
        "Function_35_34DA",        # 23, 35
        "Function_36_351E",        # 24, 36
        "Function_37_3572",        # 25, 37
        "Function_38_358A",        # 26, 38
        "Function_39_376C",        # 27, 39
        "Function_40_3D59",        # 28, 40
        "Function_41_49BA",        # 29, 41
        "Function_42_49DE",        # 2A, 42
        "Function_43_4A02",        # 2B, 43
        "Function_44_4A17",        # 2C, 44
        "Function_45_4A25",        # 2D, 45
        "Function_46_4A44",        # 2E, 46
        "Function_47_4A63",        # 2F, 47
        "Function_48_4AAE",        # 30, 48
        "Function_49_4AF4",        # 31, 49
        "Function_50_4B07",        # 32, 50
        "Function_51_4B23",        # 33, 51
        "Function_52_4DA2",        # 34, 52
        "Function_53_4F20",        # 35, 53
        "Function_54_5249",        # 36, 54
        "Function_55_527A",        # 37, 55
        "Function_56_58C4",        # 38, 56
        "Function_57_5E43",        # 39, 57
    ))


    def Function_0_550(): pass

    label("Function_0_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_564")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_573")

    label("loc_564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_573")
    ClearScenarioFlags(0x22, 1)
    Event(0, 57)

    label("loc_573")

    Return()

    # Function_0_550 end

    def Function_1_574(): pass

    label("Function_1_574")

    Return()

    # Function_1_574 end

    def Function_2_575(): pass

    label("Function_2_575")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32300.itc", 0x23)
    LoadChrToIndex("chr/ch32400.itc", 0x24)
    LoadChrToIndex("chr/ch33000.itc", 0x25)
    LoadChrToIndex("chr/ch33100.itc", 0x26)
    LoadChrToIndex("chr/ch33300.itc", 0x27)
    LoadChrToIndex("chr/ch26900.itc", 0x28)
    LoadChrToIndex("chr/ch28100.itc", 0x29)
    LoadChrToIndex("apl/ch50250.itc", 0x2D)
    LoadChrToIndex("apl/ch50251.itc", 0x2E)
    LoadChrToIndex("apl/ch50252.itc", 0x2F)
    LoadChrToIndex("apl/ch50253.itc", 0x30)
    LoadChrToIndex("apl/ch50254.itc", 0x31)
    LoadChrToIndex("chr/ch14150.itc", 0x37)
    LoadChrToIndex("chr/ch14151.itc", 0x38)
    LoadChrToIndex("chr/ch14152.itc", 0x39)
    LoadChrToIndex("chr/ch14153.itc", 0x3A)
    LoadChrToIndex("chr/ch14154.itc", 0x3B)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis410.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06200.itp")
    LoadEffect(0x0, "event/ev15001.eff")
    LoadEffect(0x1, "event/ev15002.eff")
    LoadEffect(0x2, "event/ev15003.eff")
    LoadEffect(0x3, "event/ev15009.eff")
    SoundLoad(818)
    SoundLoad(819)
    SoundLoad(3250)
    SoundLoad(3251)
    SoundLoad(3252)
    SoundLoad(3253)
    SoundLoad(3957)
    SoundLoad(3958)
    SoundLoad(3959)
    SoundLoad(3960)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    OP_71(0x1, 0x0, 0x0, 0x1, 0x0)
    OP_7D(0xA0, 0xA0, 0xD2, 0x0, 0x0)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 3500, 1800, 27700, 225)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 1250, 25500, 225)
    BeginChrThread(0x0, 0, 0, 38)
    OP_68(0, 2900, 24750, 0)
    MoveCamera(5, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30500, 0)
    OP_68(0, 2900, 24750, 8000)
    MoveCamera(-5, 10, 0, 8000)
    OP_6E(700, 8000)
    SetCameraDistance(30500, 8000)
    VolumeBGM(0x64, 0x3E8)
    BeginChrThread(0x2A, 1, 0, 49)
    FadeToBright(1000, 0)
    Sleep(7500)
    OP_68(0, 4900, 25220, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(16000, 0)
    OP_68(0, 2900, 25220, 8000)
    MoveCamera(5, 15, 1, 8000)
    SetCameraDistance(15000, 8000)
    BeginChrThread(0x2A, 1, 0, 50)
    Fade(500)
    WaitChrThread(0x0, 0)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0x8, 0xFF)
    OP_49()
    LoadChrToIndex("chr/ch36600.itc", 0x1E)
    LoadChrToIndex("chr/ch36700.itc", 0x1F)
    LoadChrToIndex("chr/ch36900.itc", 0x20)
    LoadChrToIndex("chr/ch37000.itc", 0x21)
    LoadChrToIndex("chr/ch36800.itc", 0x22)
    LoadChrToIndex("chr/ch41951.itc", 0x4B)
    LoadChrToIndex("chr/ch41952.itc", 0x4C)
    LoadChrToIndex("apl/ch51505.itc", 0x4D)
    LoadChrToIndex("chr/ch03450.itc", 0x46)
    LoadChrToIndex("chr/ch03452.itc", 0x47)
    LoadChrToIndex("chr/ch03456.itc", 0x48)
    LoadChrToIndex("chr/ch0345F.itc", 0x49)
    LoadChrToIndex("apl/ch51506.itc", 0x4A)
    LoadChrToIndex("chr/ch09800.itc", 0x41)
    LoadChrToIndex("apl/ch51503.itc", 0x42)
    LoadChrToIndex("apl/ch51507.itc", 0x43)
    LoadChrToIndex("apl/ch51504.itc", 0x32)
    LoadChrToIndex("apl/ch51501.itc", 0x3C)
    LoadChrToIndex("apl/ch51502.itc", 0x3D)
    LoadChrToIndex("chr/ch14100.itc", 0x3E)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev15021.eff")
    LoadEffect(0x2, "event/ev15000.eff")
    LoadEffect(0x3, "event/ev15010.eff")
    LoadEffect(0x4, "event/ev15011.eff")
    LoadEffect(0x5, "event/ev15020.eff")
    LoadEffect(0x6, "battle/ms00001.eff")
    SoundLoad(870)
    SoundLoad(875)
    SoundLoad(877)
    SoundLoad(566)
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(868)
    SoundLoad(926)
    SetChrChipByIndex(0x9, 0x41)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0x9, -62260, 0, 4180, 135)
    SetChrPos(0xD, -63950, 0, 3170, 90)
    SetChrPos(0xE, -63620, 0, 4410, 135)
    SetChrPos(0xF, -63000, 0, 2460, 90)
    SetChrPos(0xB, -64580, 0, 1750, 90)
    SetChrPos(0xC, -65410, 0, 2420, 90)
    OP_68(-63820, 1200, 3260, 0)
    MoveCamera(40, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetCameraDistance(16000, 1500)
    VolumeBGM(0x46, 0x3E8)
    Sound(818, 0, 40, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0xD,
        (
            "#5P凄い……\x01",
            "シュリ、頑張りましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xE,
        (
            "#5Pふふ、毎日一生懸命、\x01",
            "練習していたもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xF,
        (
            "#5Pふ、ふん……\x01",
            "まあまあですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xB,
        (
            "#6Pハハ、しかし新しいシーンが\x01",
            "１つ入るだけで変わるもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xC,
        (
            "#6Pああ、イリアと劇団長の\x01",
            "執念といったところだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0006
    AnonymousTalk(
        0x9,
        (
            "#30W………はい……………\x02\x03",

            "（シュリちゃんがいれば\x01",
            "  私が居なくなっても……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C6A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C6A)
    WaitChrThread(0x9, 2)
    Sleep(150)

    #C0007
    ChrTalk(
        0x9,
        "#06205F#5P#30Wえ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_CFB():
        TurnDirection(0xE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_CFB)
    Sleep(50)

    def lambda_D0B():
        TurnDirection(0xF, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_D0B)
    Sleep(50)

    def lambda_D1B():
        TurnDirection(0xB, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_D1B)
    Sleep(50)

    def lambda_D2B():
        TurnDirection(0xC, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_D2B)
    Sleep(50)

    def lambda_D3B():
        TurnDirection(0xD, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_D3B)
    Sleep(50)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)

    #C0008
    ChrTalk(
        0xE,
        "#5P……どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xB,
        "#6Pおかしな所でもあったか？\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "#6208F#5P#40W……こ、この気配は……\x02\x03",

            "#6203F#40W５……１０……\x01",
            "どうしてこんな時に……\x02\x03",

            "#6201F#20W……まさか…………！\x02",
        )
    )

    CloseMessageWindow()
    Sound(872, 0, 50, 0)
    Sleep(500)
    Sound(870, 2, 50, 0)
    Sleep(500)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_EAC():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_EAC)
    Sleep(50)

    def lambda_EBC():
        OP_93(0xE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_EBC)
    Sleep(50)

    def lambda_ECC():
        OP_93(0xF, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_ECC)
    Sleep(50)

    def lambda_EDC():
        OP_93(0xB, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_EDC)
    Sleep(50)

    def lambda_EEC():
        OP_93(0xC, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_EEC)
    Sleep(50)

    def lambda_EFC():
        OP_93(0xD, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_EFC)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)

    #C0011
    ChrTalk(
        0xF,
        "#5Pな、なんですの？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xD,
        "う、上から……！？\x02",
    )

    CloseMessageWindow()
    OP_68(-62820, 1200, 3260, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x10, 0x46)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 13500, 31350, 180)
    OP_68(0, 14500, 31350, 0)
    MoveCamera(15, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(0, 14500, 31350, 2000)
    MoveCamera(5, 15, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(16000, 2000)
    VolumeBGM(0x64, 0x3E8)
    StopSound(870, 1000, 40)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x10, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0013
    AnonymousTalk(
        0x10,
        (
            "ふふっ。\x01",
            "何とか間に合って良かった。\x02\x03",

            "せっかくの追加シーンを\x01",
            "ぶち壊すのは勿体ないけど……\x02\x03",

            "最高に盛り上がりそうだし、\x01",
            "構わないよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_68(0, 14750, 26900, 500)
    MoveCamera(330, 20, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(15500, 500)
    OP_F0(0x0, 0xB)
    SetChrChipByIndex(0x10, 0x47)
    SetChrSubChip(0x10, 0x0)
    Sound(844, 0, 100, 0)
    OP_9D(0x10, 0x0, 0x35B6, 0x6914, 0x5DC, 0x1B58)
    BeginChrThread(0x10, 3, 0, 4)
    Sound(872, 0, 100, 0)
    Sleep(500)
    Sound(870, 2, 90, 0)
    EndChrThread(0x10, 0x3)
    BeginChrThread(0x10, 3, 0, 5)
    OP_87(0x2, 0x0, 0x1, "CA00", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sound(875, 2, 90, 0)
    Sound(566, 0, 70, 0)
    Sound(358, 0, 70, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    #C0014
    ChrTalk(
        0x10,
        "#04612F#3957V#11P#5S#24A#30Wアハハハハ、落っちろ～！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_6B(0xFF)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)
    OP_87(0x6, 0x1, 0x1, "CA00", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_71(0x1, 0x2C, 0x50, 0x1, 0x8)
    Sound(873, 0, 100, 0)
    StopSound(870, 500, 80)
    StopSound(875, 500, 80)
    EndChrThread(0x10, 0x3)
    StopEffect(0x0, 0x0)
    SetChrChipByIndex(0x10, 0x49)
    SetChrSubChip(0x10, 0x2)
    Sound(834, 0, 100, 0)
    Sound(844, 0, 100, 0)
    OP_9D(0x10, 0x834, 0x34BC, 0x78B4, 0x7D0, 0x1B58)
    SetChrSubChip(0x10, 0x0)
    Fade(500)
    SetChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x2)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    SetChrPos(0x8, 1800, 1250, 28100, 225)
    SetChrPos(0xA, 0, 1250, 25450, 180)
    SetChrPos(0x9, -10000, 1250, 24750, 90)
    SetChrPos(0xB, -12500, 1250, 24750, 90)
    SetChrPos(0xC, -14000, 1250, 24750, 90)
    SetChrPos(0xD, -15500, 1250, 24750, 90)
    SetChrPos(0xF, -17000, 1250, 24750, 90)
    SetChrPos(0xE, -18500, 1250, 24750, 90)
    OP_68(0, 3250, 24900, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(18000, 500)
    OP_71(0x1, 0x0, 0x0, 0x1, 0x0)
    OP_0D()
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x3C)
    SetChrSubChip(0xA, 0x0)

    #C0015
    ChrTalk(
        0xA,
        "#12211F#7Aえ───\x02",
    )
    #Auto

    Sleep(600)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0016
    ChrTalk(
        0x8,
        "#06107F#4S#9A下がりなさいっ！！\x02",
    )
    #Auto

    Sleep(1500)
    SetChrChipByIndex(0x8, 0x2E)

    def lambda_140A():
        OP_9A(0xFE, 0xA, 0x1F4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_140A)
    Sleep(200)
    Sound(811, 0, 100, 0)
    Sound(862, 0, 100, 0)
    Fade(100)
    OP_71(0x1, 0x2C, 0x2C, 0x0, 0x0)
    OP_68(0, 11000, 25450, 0)
    MoveCamera(0, -30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_F0(0x0, 0xA)
    OP_68(0, 3250, 24900, 500)
    MoveCamera(0, 15, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(20000, 500)
    OP_74(0x1, 0xA)
    OP_71(0x1, 0x2C, 0x36, 0x1, 0x8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    Sleep(400)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x31)
    SetChrSubChip(0x8, 0x1)
    OP_93(0x8, 0xB4, 0x0)
    ClearChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x1)

    def lambda_14EC():
        OP_96(0xFE, 0xFFFFF1BE, 0x4E2, 0x5302, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14EC)

    def lambda_1506():
        OP_96(0xFE, 0xFFFFFAEC, 0x4E2, 0x5B04, 0x251C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1506)
    OP_68(0, 2250, 24900, 500)
    MoveCamera(0, 30, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(22000, 500)
    OP_74(0x1, 0x1E)
    OP_79(0x1)
    OP_71(0x1, 0x37, 0x50, 0x1, 0x8)
    Sound(876, 0, 100, 0)
    Sound(880, 0, 100, 0)
    Sound(200, 0, 40, 0)
    Sound(833, 0, 60, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 0, 1250, 25450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_71(0x5, 0x2, 0x1E, 0x0, 0x8)
    ClearMapObjFlags(0x6, 0x4)
    OP_71(0x6, 0x0, 0xC, 0x0, 0x8)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x32)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0x8, 0x20)
    OP_6F(0x79)
    StopBGM(0x3E8)
    Sleep(2000)
    PlayEffect(0x4, 0xFF, 0x8, 0x0, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(0, 2250, 24900, 20000)
    MoveCamera(0, 35, -5, 20000)
    OP_6E(600, 20000)
    SetCameraDistance(22000, 20000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    Sleep(1000)
    BeginChrThread(0x2A, 1, 0, 48)
    Sleep(1000)
    Sound(878, 0, 80, 0)

    #C0017
    ChrTalk(
        0x15,
        "#3Pうわわあああっ！？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x16,
        "#4Pイ、イリアが……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0019
    ChrTalk(
        0x17,
        "#4Sイリアが巻き込まれたぞ！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)
    Sound(802, 0, 100, 0)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x3D)
    SetChrSubChip(0xA, 0x0)

    #C0020
    ChrTalk(
        0xA,
        "#12211F#50Wあ……ああ……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0021
    ChrTalk(
        0x9,
        "#06214F#3250V#4Sイリアさんッ！！？\x02",
    )

    CloseMessageWindow()
    OP_24(0xCB2)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(-2550, 2250, 21750, 0)
    MoveCamera(345, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    MoveCamera(8, 26, 0, 3500)
    BeginChrThread(0x9, 3, 0, 6)
    BeginChrThread(0xB, 3, 0, 9)
    BeginChrThread(0xC, 3, 0, 11)
    BeginChrThread(0xD, 3, 0, 13)
    BeginChrThread(0xF, 3, 0, 15)
    BeginChrThread(0xE, 3, 0, 17)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)

    #C0022
    ChrTalk(
        0xA,
        "#12210F#6Pリ、リーシャ姉！\x02",
    )

    CloseMessageWindow()
    OP_6F(0x79)

    def lambda_1839():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1839)

    def lambda_1852():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1852)
    Sound(879, 0, 100, 0)
    OP_25(0x36D, 0x46)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x51, 0x67, 0x1, 0x8)
    OP_79(0x1)
    Sound(812, 0, 100, 0)

    def lambda_188E():

        label("loc_188E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_188E")

    QueueWorkItem2(0xD, 2, lambda_188E)

    def lambda_18A0():

        label("loc_18A0")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_18A0")

    QueueWorkItem2(0xF, 2, lambda_18A0)

    def lambda_18B2():

        label("loc_18B2")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_18B2")

    QueueWorkItem2(0xE, 2, lambda_18B2)

    def lambda_18C4():
        OP_96(0xFE, 0xFFFFF448, 0x4E2, 0x5460, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_18C4)
    SetChrFlags(0x8, 0x20)
    TurnDirection(0x8, 0x9, 0)

    def lambda_18EA():
        OP_96(0xFE, 0xFFFFF736, 0x4E2, 0x5686, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18EA)
    WaitChrThread(0x8, 1)
    ClearChrFlags(0x8, 0x20)
    WaitChrThread(0x9, 1)
    BeginChrThread(0x9, 3, 0, 7)
    WaitChrThread(0x9, 3)
    Sound(880, 0, 100, 0)
    OP_25(0x36D, 0x28)
    OP_71(0x1, 0x68, 0x72, 0x1, 0x8)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x42)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_79(0x1)
    EndChrThread(0xB, 0x3)

    def lambda_1960():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1960)
    Sleep(100)
    EndChrThread(0xC, 0x3)

    def lambda_1974():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1974)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xF, 0x2)
    EndChrThread(0xE, 0x2)
    OP_0D()
    OP_C9(0x0, 0x80000000)

    #C0023
    ChrTalk(
        0x9,
        (
            "#06212F#3251V#11Pイリアさん！？\x01",
            "いやあっ、イリアさんっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCB3)
    OP_C9(0x1, 0x80000000)

    #C0024
    ChrTalk(
        0xE,
        "#5P……なんてこと……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xF,
        "#5Pど、どうしてこんな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-2250, 2150, 22250, 20000)
    MoveCamera(6, 31, 0, 20000)
    OP_6E(500, 20000)
    SetCameraDistance(15500, 20000)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0x8, 0x2)
    OP_0D()

    #C0026
    ChrTalk(
        0x8,
        "#06110F#5P#80W#2S………ぅ……………\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0027
    ChrTalk(
        0x9,
        (
            "#06212F#11Pイリアさん！？\x01",
            "大丈夫ですか、イリアさん！？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "#06111F#5P#80W#2S…………シュリ……は……？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x38)
    OP_9A(0xA, 0x8, 0x2EE, 0x7D0, 0x0)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x3D)
    SetChrSubChip(0xA, 0x1)
    OP_0D()

    #C0029
    ChrTalk(
        0xA,
        (
            "#12210F#6Pぶ、無事だよっ！\x02\x03",

            "イリアさんが助けてくれたから\x01",
            "オレ……！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x8, 0x4)
    OP_0D()

    #C0030
    ChrTalk(
        0x8,
        (
            "#06110F#5P#80W#2S……そ……ぅ……よかった……\x02\x03",

            "#2S#80W……リー……シャ………\x01",
            "次の……幕は……アンタだけで……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(300)
    Sound(812, 0, 100, 0)
    SetCameraDistance(15000, 300)
    SetChrSubChip(0x8, 0x5)
    OP_0D()
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0031
    ChrTalk(
        0x9,
        (
            "#06214F#11P#4Sイリアさん！？\x01",
            "……イリアさんっっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        "#12210F#6Pうわあああああっ！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    #C0033
    ChrTalk(
        0xB,
        "#11Pテオ、運ぶぞっ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    #C0034
    ChrTalk(
        0xC,
        "#5P分かったッ……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 10)
    Sleep(300)
    BeginChrThread(0xC, 3, 0, 12)
    Sound(812, 0, 100, 0)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    Sleep(300)
    ClearChrFlags(0x10, 0x80)

    #N0035
    NpcTalk(
        0x10,
        "シャーリィの声",
        (
            "うっわー、そんなになってまで\x01",
            "舞台が大事なんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x10, 0x49)
    SetChrSubChip(0x10, 0x1)
    SetChrPos(0x10, 3900, 13500, 29750, 225)
    SetChrPos(0x9, -1800, 1250, 19850, 0)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x41)
    SetChrSubChip(0x9, 0x0)
    OP_68(3200, 8700, 30850, 0)
    MoveCamera(30, -15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(0, 6300, 30600, 2000)
    MoveCamera(0, 15, 0, 2000)
    SetCameraDistance(16500, 2000)
    SetChrChip(0x0, 0x10, 0x1E, 0xC8)
    OP_9D(0x10, 0x9F6, 0x1DB0, 0x7788, 0x3E8, 0x1B58)
    Sound(809, 0, 50, 0)
    OP_9D(0x10, 0x0, 0x14B4, 0x7788, 0x3E8, 0x1B58)
    SetChrSubChip(0x10, 0x0)
    Sound(326, 0, 30, 0)
    SetChrChipByIndex(0x10, 0x46)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x10, 0xB4, 0x1F4)
    SetChrChip(0x1, 0x10, 0x0, 0x0)
    OP_0D()
    OP_6F(0x79)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x2710)
    SetCameraDistance(15500, 20000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7544", 0)

    #C0036
    ChrTalk(
        0x10,
        (
            "#04609F#11Pあはっ！\x01",
            "やっぱりイリアは凄いよね！\x02\x03",

            "#04602Fリーシャが拘る理由も分かるよ♪\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        "#06211F#40W……血染めの#8Rブ ラ ッ デ ィ#シャーリィ……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xD,
        "お、女の子……？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xF,
        "だ、誰ですのっ……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 80, 0)
    SetChrChipByIndex(0x10, 0x48)
    OP_A1(0x10, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 50, 0)
    BeginChrThread(0x10, 3, 0, 19)
    Sleep(500)
    StopSound(865, 300, 100)
    StopSound(861, 300, 50)
    EndChrThread(0x10, 0x3)
    OP_0D()
    Sleep(300)
    Sound(878, 0, 80, 0)
    SetMessageWindowPos(-1, 200, -1, -1)

    #A0040
    AnonymousTalk(
        0x15,
        "きゃあああああっ！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 200, -1, -1)

    #A0041
    AnonymousTalk(
        0x16,
        "じゅ、銃だ！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 200, -1, -1)

    #A0042
    AnonymousTalk(
        0x1B,
        "銃を持ってるぞ！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    Sound(937, 0, 100, 0)
    SetChrChipByIndex(0x11, 0x4B)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x4B)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x4B)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x4B)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x11, 600, 2700, -4900, 0)
    SetChrPos(0x12, -600, 2700, -5400, 0)
    SetChrPos(0x13, 600, 2700, -6400, 0)
    SetChrPos(0x14, -600, 2700, -6900, 0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x4)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 3200, 2250, 2700, 350)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 2000, 1800, 4800, 350)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 2950, 1800, 5000, 350)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 3950, 1800, 5150, 350)
    SetChrChipByIndex(0x19, 0x26)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 4200, 1350, 7350, 350)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 5250, 1350, 7500, 350)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 2100, 900, 9150, 350)
    SetChrChipByIndex(0x1C, 0x27)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 2850, 900, 9300, 350)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 3800, 900, 9450, 350)
    SetChrChipByIndex(0x1E, 0x26)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 4800, 900, 9650, 350)
    SetChrChipByIndex(0x1F, 0x29)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -2100, 2250, 2600, 10)
    SetChrChipByIndex(0x20, 0x23)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -3250, 2250, 2800, 10)
    SetChrChipByIndex(0x21, 0x27)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, -3100, 1800, 4950, 10)
    SetChrChipByIndex(0x22, 0x25)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -4050, 1800, 5100, 10)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, -2150, 1350, 6800, 10)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, -3300, 1350, 7000, 10)
    SetChrChipByIndex(0x25, 0x26)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, -4300, 1350, 7150, 10)
    SetChrChipByIndex(0x26, 0x25)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, -1950, 900, 9000, 10)
    SetChrChipByIndex(0x27, 0x26)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, -2950, 900, 9150, 10)
    SetChrChipByIndex(0x28, 0x24)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, -3900, 900, 9300, 10)
    OP_68(0, 4000, -2800, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 700, 15500, 5000)
    MoveCamera(0, 17, -5, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(23500, 5000)

    def lambda_248D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_248D)

    def lambda_249E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_249E)

    def lambda_24AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_24AF)

    def lambda_24C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_24C0)
    BeginChrThread(0x11, 1, 0, 20)
    BeginChrThread(0x12, 1, 0, 21)
    BeginChrThread(0x13, 1, 0, 22)
    BeginChrThread(0x14, 1, 0, 23)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x14, 1)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 70, 0)
    SetChrChipByIndex(0x11, 0x4D)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x12, 0x4D)
    SetChrSubChip(0x12, 0x4)
    SetChrFlags(0x12, 0x2)
    SetChrChipByIndex(0x13, 0x4D)
    SetChrSubChip(0x13, 0x2)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x14, 0x4D)
    SetChrSubChip(0x14, 0x2)
    SetChrFlags(0x14, 0x2)
    OP_0D()
    Sound(865, 2, 100, 0)
    Sound(861, 2, 50, 0)
    BeginChrThread(0x11, 3, 0, 24)
    BeginChrThread(0x12, 3, 0, 25)
    BeginChrThread(0x13, 3, 0, 26)
    BeginChrThread(0x14, 3, 0, 26)
    Sleep(500)
    StopSound(865, 300, 100)
    StopSound(861, 300, 50)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x14, 0x3)
    OP_0D()
    Sound(878, 0, 100, 0)
    Sound(916, 0, 80, 0)

    #C0043
    ChrTalk(
        0x15,
        "ひいいいいっ！！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x16,
        (
            "た、助けて！\x01",
            "女神さまああああっ！\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x1, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 2, 30, 0)
    Sound(937, 0, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x2710)
    BeginChrThread(0x1F, 1, 0, 29)
    Sleep(50)
    BeginChrThread(0x16, 1, 0, 30)
    Sleep(50)
    BeginChrThread(0x23, 1, 0, 33)
    Sleep(50)
    BeginChrThread(0x1B, 1, 0, 34)
    Sleep(50)
    BeginChrThread(0x26, 1, 0, 35)
    Sleep(100)
    BeginChrThread(0x15, 1, 0, 28)
    Sleep(50)
    BeginChrThread(0x20, 1, 0, 29)
    Sleep(50)
    BeginChrThread(0x17, 1, 0, 30)
    Sleep(50)
    BeginChrThread(0x21, 1, 0, 31)
    Sleep(50)
    BeginChrThread(0x24, 1, 0, 33)
    Sleep(50)
    BeginChrThread(0x1C, 1, 0, 34)
    Sleep(50)
    BeginChrThread(0x27, 1, 0, 35)
    Sleep(100)
    BeginChrThread(0x18, 1, 0, 30)
    Sleep(50)
    BeginChrThread(0x22, 1, 0, 31)
    Sleep(50)
    BeginChrThread(0x19, 1, 0, 32)
    Sleep(50)
    BeginChrThread(0x25, 1, 0, 33)
    Sleep(50)
    BeginChrThread(0x1D, 1, 0, 34)
    Sleep(50)
    BeginChrThread(0x28, 1, 0, 35)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x22, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x26, 0x1)
    EndChrThread(0x27, 0x1)
    EndChrThread(0x28, 0x1)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_25(0x364, 0x32)
    OP_82(0x32, 0x32, 0xBB8, 0x0)
    Fade(500)
    SetMapObjFlags(0x2, 0x4)
    SetChrPos(0xA, -3650, 1250, 21050, 135)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x3E)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0x29, 0x4A)
    SetChrSubChip(0x29, 0x8)
    SetChrFlags(0x29, 0x8000)
    SetChrFlags(0x29, 0x2)
    SetChrFlags(0x29, 0x20)
    ClearChrFlags(0x29, 0x1)
    SetChrPos(0x29, 0, 5500, 30600, 0)
    OP_93(0x9, 0x0, 0x0)
    TurnDirection(0xB, 0x9, 0)
    TurnDirection(0xC, 0x9, 0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x42)
    SetChrSubChip(0x9, 0x3)
    OP_68(-1850, 2250, 20000, 0)
    MoveCamera(335, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    MoveCamera(315, 30, 0, 6000)
    SetCameraDistance(15000, 6000)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -8200, 0, 18930, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -3880, 7600, 30690, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 2310, 1250, 22120, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_0D()
    TurnDirection(0xB, 0x8, 500)
    Sleep(50)
    TurnDirection(0xC, 0x8, 500)
    BeginChrThread(0xE, 1, 0, 18)
    Sleep(300)
    BeginChrThread(0xF, 1, 0, 16)
    Sleep(500)
    BeginChrThread(0xD, 1, 0, 14)
    SetChrFlags(0x8, 0x20)
    BeginChrThread(0x8, 1, 0, 36)
    BeginChrThread(0xC, 1, 0, 36)
    BeginChrThread(0xB, 1, 0, 36)
    Sleep(2000)

    def lambda_294F():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_294F)
    WaitChrThread(0x9, 2)
    Sleep(800)

    def lambda_296F():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_296F)
    WaitChrThread(0x9, 2)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #C0045
    ChrTalk(
        0x9,
        (
            "#06213F#3252V#6P#50W……あなた……\x01",
            "…………あなたたちは……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCB4)
    OP_57(0x0)
    OP_5A()

    #C0046
    ChrTalk(
        0x10,
        (
            "#04612F#3958V#12P#N#30Wアハハ、そうそう！\x01",
            "それが見たかったんだよ！\x02\x03",

            "#04611F#3959Vまじりっけのない“強さ”！\x02\x03",

            "#3960V変装なんかで余計な力を使ってない\x01",
            "全力のリーシャ・マオをさ！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF78)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 5900, 30600, 0)
    MoveCamera(10, 20, 5, 0)
    OP_6E(500, 0)
    SetCameraDistance(13150, 0)
    OP_0D()
    Sound(540, 0, 50, 0)
    Sound(531, 0, 50, 0)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0x4A)
    OP_A0(0x10, 1500, 0x0, 0x1)
    Sleep(500)
    Sound(809, 0, 60, 0)
    OP_A0(0x10, 1500, 0x2, 0x3)
    SetChrSubChip(0x10, 0x4)
    OP_68(-950, 4550, 25250, 800)
    MoveCamera(359, -8, 0, 800)
    SetCameraDistance(18300, 800)
    ClearChrFlags(0x29, 0x80)
    Sound(926, 2, 100, 0)
    BeginChrThread(0x29, 3, 0, 37)
    OP_9D(0x29, 0xFFFFFC18, 0x320, 0x5366, 0x5DC, 0x1388)
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    EndChrThread(0x29, 0x3)
    SetChrSubChip(0x29, 0x7)
    Sound(645, 0, 100, 0)
    Sound(308, 0, 100, 0)
    Sound(540, 0, 50, 0)
    OP_24(0x39E)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x9, 0x2)
    OP_0D()
    OP_6F(0x79)

    #C0047
    ChrTalk(
        0x10,
        (
            "#04604F#11Pそれ、リーシャの部屋から\x01",
            "持ってきてあげたんだよ？\x02\x03",

            "#04602F最高の舞台を用意したんだから\x01",
            "思いっきり楽しもう！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1500, 1700, 20500, 1000)
    MoveCamera(0, 10, 0, 1000)
    SetCameraDistance(13300, 1000)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x41)
    SetChrSubChip(0x9, 0x0)
    OP_96(0x9, 0xFFFFFA24, 0x4B0, 0x5014, 0x3E8, 0x0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x43)
    SetChrSubChip(0x9, 0x0)
    OP_6F(0x79)
    Fade(250)
    Sound(308, 0, 100, 0)
    SetChrFlags(0x29, 0x80)
    OP_A0(0x9, 1500, 0x1, 0x2)
    Sound(540, 0, 50, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    OP_68(-950, 3550, 25250, 800)
    MoveCamera(5, -2, -5, 800)
    OP_6E(500, 800)
    SetCameraDistance(16370, 800)
    Sleep(100)
    OP_A0(0x9, 2000, 0x3, 0x4)
    Sleep(500)
    BeginChrThread(0x9, 0, 0, 3)
    OP_C9(0x0, 0x80000000)

    #C0048
    ChrTalk(
        0x9,
        (
            "#06215F#3253V#6P#32A#N#40W許さない……！！#800W！\x01",
            "#4S#30Wシャーリィ・オルランドォォォッ！！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    StopSound(868, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x9, 0)
    Sleep(500)
    OP_24(0x366)
    OP_24(0x36B)
    OP_24(0x36D)
    OP_24(0x361)
    OP_24(0x35D)
    OP_24(0x39E)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c040B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_575 end

    def Function_3_2DC9(): pass

    label("Function_3_2DC9")

    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(1500)
    OP_82(0x64, 0x64, 0x1388, 0x9C4)
    SetCameraDistance(18500, 4500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(500)
    CancelBlur(5000)
    Return()

    # Function_3_2DC9 end

    def Function_4_2E0C(): pass

    label("Function_4_2E0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E24")
    OP_A1(0xFE, 0xDAC, 0x2, 0x1, 0x2)
    Jump("Function_4_2E0C")

    label("loc_2E24")

    Return()

    # Function_4_2E0C end

    def Function_5_2E25(): pass

    label("Function_5_2E25")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E3D")
    OP_A1(0xFE, 0xDAC, 0x2, 0x4, 0x5)
    Jump("Function_5_2E25")

    label("loc_2E3D")

    Return()

    # Function_5_2E25 end

    def Function_6_2E3E(): pass

    label("Function_6_2E3E")

    OP_95(0x9, -5250, 1250, 25000, 4000, 0x0)
    OP_95(0x9, -1800, 1250, 22700, 4000, 0x0)
    TurnDirection(0x9, 0x8, 500)
    Return()

    # Function_6_2E3E end

    def Function_7_2E6E(): pass

    label("Function_7_2E6E")

    OP_95(0x9, -1800, 1250, 21400, 4000, 0x0)
    OP_95(0x9, -1850, 1250, 22500, 4000, 0x0)
    TurnDirection(0x9, 0x8, 500)
    Return()

    # Function_7_2E6E end

    def Function_8_2E9E(): pass

    label("Function_8_2E9E")

    OP_95(0x9, -1350, 1250, 21700, 4000, 0x0)
    OP_95(0x9, -1800, 1250, 19850, 4000, 0x0)
    TurnDirection(0x9, 0xC, 500)
    Return()

    # Function_8_2E9E end

    def Function_9_2ECE(): pass

    label("Function_9_2ECE")

    OP_95(0xB, -5250, 1250, 25000, 4000, 0x0)
    OP_95(0xB, -1450, 1250, 21550, 4000, 0x0)
    OP_95(0xB, -750, 1250, 22250, 4000, 0x0)
    OP_93(0xB, 0x0, 0x1F4)
    Return()

    # Function_9_2ECE end

    def Function_10_2F12(): pass

    label("Function_10_2F12")

    OP_95(0xB, -1850, 1250, 21700, 4000, 0x0)
    OP_93(0xB, 0x13B, 0x1F4)
    Return()

    # Function_10_2F12 end

    def Function_11_2F2E(): pass

    label("Function_11_2F2E")

    OP_95(0xC, -5250, 1250, 25000, 4000, 0x0)
    OP_95(0xC, -2800, 1250, 23300, 4000, 0x0)
    OP_93(0xC, 0x5A, 0x1F4)
    Return()

    # Function_11_2F2E end

    def Function_12_2F5E(): pass

    label("Function_12_2F5E")

    OP_95(0xC, -3000, 1250, 22400, 4000, 0x0)
    OP_93(0xC, 0x87, 0x1F4)
    Return()

    # Function_12_2F5E end

    def Function_13_2F7A(): pass

    label("Function_13_2F7A")

    OP_95(0xD, -5250, 1250, 25000, 4000, 0x0)
    OP_95(0xD, -5100, 1250, 21950, 4000, 0x0)
    TurnDirection(0xD, 0x8, 500)
    Return()

    # Function_13_2F7A end

    def Function_14_2FAA(): pass

    label("Function_14_2FAA")

    OP_95(0xD, -9000, 1250, 25400, 4000, 0x0)
    OP_95(0xD, -12000, 1250, 25400, 4000, 0x0)
    Return()

    # Function_14_2FAA end

    def Function_15_2FD3(): pass

    label("Function_15_2FD3")

    OP_95(0xF, -5250, 1250, 25000, 4000, 0x0)
    OP_95(0xF, -3900, 1250, 23450, 4000, 0x0)
    TurnDirection(0xF, 0x8, 500)
    Return()

    # Function_15_2FD3 end

    def Function_16_3003(): pass

    label("Function_16_3003")

    OP_95(0xF, -9000, 1250, 25400, 4000, 0x0)
    OP_95(0xF, -12000, 1250, 25400, 4000, 0x0)
    Return()

    # Function_16_3003 end

    def Function_17_302C(): pass

    label("Function_17_302C")

    OP_95(0xE, -5250, 1250, 25000, 4000, 0x0)
    OP_95(0xE, -4850, 1250, 23450, 4000, 0x0)
    TurnDirection(0xE, 0x8, 500)
    Return()

    # Function_17_302C end

    def Function_18_305C(): pass

    label("Function_18_305C")

    OP_95(0xE, -9000, 1250, 25400, 4000, 0x0)
    OP_95(0xE, -12000, 1250, 25400, 4000, 0x0)
    Return()

    # Function_18_305C end

    def Function_19_3085(): pass

    label("Function_19_3085")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30D4")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 800, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x3, 0x2)
    Jump("Function_19_3085")

    label("loc_30D4")

    Return()

    # Function_19_3085 end

    def Function_20_30D5(): pass

    label("Function_20_30D5")

    ClearChrFlags(0x11, 0x4)
    OP_95(0x11, 600, 0, 15250, 6000, 0x0)
    OP_95(0x11, 7000, 0, 17750, 6000, 0x0)
    OP_93(0x11, 0x87, 0x1F4)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 0x4C)
    OP_A1(0x11, 0x7D0, 0x2, 0x0, 0x1)
    Return()

    # Function_20_30D5 end

    def Function_21_311B(): pass

    label("Function_21_311B")

    ClearChrFlags(0x12, 0x4)
    OP_95(0x12, -600, 0, 15250, 6000, 0x0)
    OP_95(0x12, -7000, 0, 17750, 6000, 0x0)
    OP_93(0x12, 0xE1, 0x1F4)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 0x4C)
    OP_A1(0x12, 0x7D0, 0x2, 0x0, 0x1)
    Return()

    # Function_21_311B end

    def Function_22_3161(): pass

    label("Function_22_3161")

    ClearChrFlags(0x13, 0x4)
    OP_95(0x13, 600, 0, 15250, 6000, 0x0)
    OP_95(0x13, 3600, 0, 16000, 6000, 0x0)
    OP_93(0x13, 0xB4, 0x1F4)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 0x4C)
    OP_A1(0x13, 0x7D0, 0x2, 0x0, 0x1)
    Return()

    # Function_22_3161 end

    def Function_23_31A7(): pass

    label("Function_23_31A7")

    ClearChrFlags(0x14, 0x4)
    OP_95(0x14, -600, 0, 15250, 6000, 0x0)
    OP_95(0x14, -3600, 0, 16000, 6000, 0x0)
    OP_93(0x14, 0xB4, 0x1F4)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x14, 0x4C)
    OP_A1(0x14, 0x7D0, 0x2, 0x0, 0x1)
    Return()

    # Function_23_31A7 end

    def Function_24_31ED(): pass

    label("Function_24_31ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_323C")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 0, 2200, 0, 270, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x1, 0x0)
    Jump("Function_24_31ED")

    label("loc_323C")

    Return()

    # Function_24_31ED end

    def Function_25_323D(): pass

    label("Function_25_323D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_328C")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 0, 2200, 0, 270, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x5, 0x4)
    Jump("Function_25_323D")

    label("loc_328C")

    Return()

    # Function_25_323D end

    def Function_26_328D(): pass

    label("Function_26_328D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32DC")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 200, 0, 2200, 0, 270, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x3, 0x2)
    Jump("Function_26_328D")

    label("loc_32DC")

    Return()

    # Function_26_328D end

    def Function_27_32DD(): pass

    label("Function_27_32DD")

    OP_93(0xFE, 0xB4, 0x2EE)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_27_32DD end

    def Function_28_32FE(): pass

    label("Function_28_32FE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332A")
    OP_95(0xFE, 850, 2250, 3000, 4000, 0x0)
    Jump("loc_333E")

    label("loc_332A")

    OP_95(0xFE, 0, 2250, 3000, 4000, 0x0)

    label("loc_333E")

    Call(0, 27)
    Return()

    # Function_28_32FE end

    def Function_29_3342(): pass

    label("Function_29_3342")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_336E")
    OP_95(0xFE, -850, 2250, 3000, 4000, 0x0)
    Jump("loc_3382")

    label("loc_336E")

    OP_95(0xFE, 0, 2250, 3000, 4000, 0x0)

    label("loc_3382")

    Call(0, 27)
    Return()

    # Function_29_3342 end

    def Function_30_3386(): pass

    label("Function_30_3386")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33B2")
    OP_95(0xFE, 850, 1800, 5350, 4000, 0x0)
    Jump("loc_33C6")

    label("loc_33B2")

    OP_95(0xFE, 0, 1800, 5350, 4000, 0x0)

    label("loc_33C6")

    Call(0, 27)
    Return()

    # Function_30_3386 end

    def Function_31_33CA(): pass

    label("Function_31_33CA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33F6")
    OP_95(0xFE, -850, 1800, 5350, 4000, 0x0)
    Jump("loc_340A")

    label("loc_33F6")

    OP_95(0xFE, 0, 1800, 5350, 4000, 0x0)

    label("loc_340A")

    Call(0, 27)
    Return()

    # Function_31_33CA end

    def Function_32_340E(): pass

    label("Function_32_340E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343A")
    OP_95(0xFE, 850, 1350, 7600, 4000, 0x0)
    Jump("loc_344E")

    label("loc_343A")

    OP_95(0xFE, 0, 1350, 7600, 4000, 0x0)

    label("loc_344E")

    Call(0, 27)
    Return()

    # Function_32_340E end

    def Function_33_3452(): pass

    label("Function_33_3452")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_347E")
    OP_95(0xFE, -850, 1350, 7600, 4000, 0x0)
    Jump("loc_3492")

    label("loc_347E")

    OP_95(0xFE, 0, 1350, 7600, 4000, 0x0)

    label("loc_3492")

    Call(0, 27)
    Return()

    # Function_33_3452 end

    def Function_34_3496(): pass

    label("Function_34_3496")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34C2")
    OP_95(0xFE, 850, 900, 9900, 4000, 0x0)
    Jump("loc_34D6")

    label("loc_34C2")

    OP_95(0xFE, 0, 900, 9900, 4000, 0x0)

    label("loc_34D6")

    Call(0, 27)
    Return()

    # Function_34_3496 end

    def Function_35_34DA(): pass

    label("Function_35_34DA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3506")
    OP_95(0xFE, -850, 900, 9900, 4000, 0x0)
    Jump("loc_351A")

    label("loc_3506")

    OP_95(0xFE, 0, 900, 9900, 4000, 0x0)

    label("loc_351A")

    Call(0, 27)
    Return()

    # Function_35_34DA end

    def Function_36_351E(): pass

    label("Function_36_351E")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -4250, 1250, 23150)
    OP_9F(0x1, -5350, 1250, 23950)
    OP_9F(0x1, -6450, 1250, 24400)
    OP_9F(0x1, -7850, 1250, 24650)
    OP_9F(0x1, -12000, 1250, 25400)
    OP_9F(0x2, 0xFE, 1000, 0x0)
    Return()

    # Function_36_351E end

    def Function_37_3572(): pass

    label("Function_37_3572")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3589")
    OP_A0(0xFE, 6000, 0x8, 0xF)
    Jump("Function_37_3572")

    label("loc_3589")

    Return()

    # Function_37_3572 end

    def Function_38_358A(): pass

    label("Function_38_358A")

    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0xFF, 0x0, 0, 2000, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4500, 3200, 20000, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4500, 3200, 20000, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4500, 31100, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4100, 4500, 31100, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x7D0)
    SetChrPos(0xA, -2500, 1250, 25450, 225)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)
    BeginChrThread(0xA, 3, 0, 47)

    def lambda_3718():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x14B4, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3718)
    Sleep(1200)
    BeginChrThread(0xA, 0, 0, 40)
    Sleep(25000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x3)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_38_358A end

    def Function_39_376C(): pass

    label("Function_39_376C")

    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 42)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9D(0xA, 0x0, 0x4E2, 0x59D8, 0xBB8, 0x226)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x37)

    def lambda_387D():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x53C, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_387D)
    OP_49()
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 42)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x190)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x37)
    BeginChrThread(0xA, 1, 0, 42)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x190)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x37)
    BeginChrThread(0xA, 1, 0, 42)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x190)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x37)
    BeginChrThread(0xA, 1, 0, 42)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x190)
    EndChrThread(0xA, 0x3)
    SetChrChipByIndex(0xA, 0x37)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0xE1, 0x0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    Sleep(1250)
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x3E8)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)
    BeginChrThread(0xA, 3, 0, 47)

    def lambda_3CE8():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1068, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3CE8)
    Sleep(250)

    def lambda_3D06():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1450, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3D06)
    Sleep(250)

    def lambda_3D24():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3D24)
    Sleep(250)

    def lambda_3D42():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3D42)
    Return()

    # Function_39_376C end

    def Function_40_3D59(): pass

    label("Function_40_3D59")


    def lambda_3D5E():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3D5E)
    OP_49()
    SetChrFlags(0xA, 0x1020)
    Call(0, 44)
    BeginChrThread(0xA, 1, 0, 45)
    Sleep(1000)

    def lambda_3D8B():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3D8B)
    OP_49()
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xA, 0x2)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)

    def lambda_3F31():
        OP_9E(0xA, 0x0, 0x636A, 0xFFF24460, 0x2A94, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3F31)
    OP_49()
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x514)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xA, 0x3)

    def lambda_4013():
        OP_93(0xA, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4013)
    BeginChrThread(0xA, 1, 0, 42)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    EndChrThread(0xA, 0x3)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xA, 1, 0, 42)

    def lambda_40F2():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x2)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_40F2)
    OP_49()
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0xAF)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0x10E, 0x0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x37)
    OP_96(0xA, 0xBB8, 0x4E2, 0x61A8, 0x7D0, 0x0)
    Sleep(700)
    OP_68(0, 2900, 25220, 4500)
    MoveCamera(-5, 15, -1, 4500)
    SetCameraDistance(15000, 4500)
    SetChrChipByIndex(0xA, 0x38)
    OP_96(0xA, 0x7D0, 0x4E2, 0x61A8, 0x1194, 0x0)
    BeginChrThread(0xA, 1, 0, 41)
    OP_9D(0xA, 0x3E8, 0x4E2, 0x61A8, 0x3E8, 0xBB8)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 1, 0, 46)
    OP_9D(0xA, 0x0, 0x4E2, 0x61A8, 0x5DC, 0xBB8)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xA, 1, 0, 45)
    OP_9D(0xA, 0xFFFFF92A, 0x4E2, 0x61A8, 0x7D0, 0xBB8)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xA, 1, 0, 42)

    def lambda_4577():
        OP_93(0xA, 0x5A, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4577)
    OP_9D(0xA, 0xFFFFF060, 0x4E2, 0x61A8, 0xBB8, 0x578)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    Sleep(500)
    EndChrThread(0xA, 0x3)
    SetChrChip(0x0, 0xA, 0xBB8, 0x12C)
    Sleep(400)
    OP_68(0, 4900, 25220, 7000)
    MoveCamera(0, -10, 0, 7000)
    SetCameraDistance(15000, 7000)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 2, 0, 45)
    BeginChrThread(0xA, 3, 0, 47)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0x7D0, 0x8FC)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    SetChrFlags(0xA, 0x1020)
    Call(0, 44)
    BeginChrThread(0xA, 1, 0, 46)
    OP_96(0xA, 0xFFFFF830, 0x4E2, 0x6590, 0x1B58, 0x0)
    OP_9E(0xA, 0xFFFFFE0C, 0x61A8, 0x2BF20, 0x2328, 0x0)
    BeginChrThread(0xA, 1, 0, 45)
    OP_9E(0xA, 0xC8, 0x61A8, 0x2BF20, 0x2328, 0x0)
    OP_9E(0xA, 0xFFFFFF06, 0x61A8, 0x2BF20, 0x2328, 0x0)
    OP_9E(0xA, 0x32, 0x61A8, 0x7A120, 0x2328, 0x0)
    BeginChrThread(0xA, 2, 0, 54)
    OP_9D(0xA, 0x0, 0x4E2, 0x639C, 0xFA0, 0x514)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x1)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_93(0xA, 0x87, 0x0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x3)
    Return()

    # Function_40_3D59 end

    def Function_41_49BA(): pass

    label("Function_41_49BA")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_41_49BA end

    def Function_42_49DE(): pass

    label("Function_42_49DE")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_42_49DE end

    def Function_43_4A02(): pass

    label("Function_43_4A02")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x9C4, 0x2, 0x0, 0x1)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_43_4A02 end

    def Function_44_4A17(): pass

    label("Function_44_4A17")

    SetChrChipByIndex(0xFE, 0x3B)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_44_4A17 end

    def Function_45_4A25(): pass

    label("Function_45_4A25")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A43")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    Jump("Function_45_4A25")

    label("loc_4A43")

    Return()

    # Function_45_4A25 end

    def Function_46_4A44(): pass

    label("Function_46_4A44")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A62")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(60)
    Jump("Function_46_4A44")

    label("loc_4A62")

    Return()

    # Function_46_4A44 end

    def Function_47_4A63(): pass

    label("Function_47_4A63")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AAD")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_47_4A63")

    label("loc_4AAD")

    Return()

    # Function_47_4A63 end

    def Function_48_4AAE(): pass

    label("Function_48_4AAE")

    Sound(877, 2, 10, 0)
    Sleep(100)
    OP_25(0x36D, 0x14)
    Sleep(100)
    OP_25(0x36D, 0x1E)
    Sleep(100)
    OP_25(0x36D, 0x28)
    Sleep(100)
    OP_25(0x36D, 0x32)
    Sleep(100)
    OP_25(0x36D, 0x3C)
    Sleep(100)
    OP_25(0x36D, 0x46)
    Sleep(100)
    OP_25(0x36D, 0x50)
    Sleep(100)
    OP_25(0x36D, 0x5A)
    Sleep(100)
    OP_25(0x36D, 0x64)
    Return()

    # Function_48_4AAE end

    def Function_49_4AF4(): pass

    label("Function_49_4AF4")

    Sleep(500)
    Sound(818, 0, 60, 0)
    Sleep(8000)
    Sound(819, 0, 100, 0)
    Return()

    # Function_49_4AF4 end

    def Function_50_4B07(): pass

    label("Function_50_4B07")

    Sleep(1000)
    Sound(818, 0, 100, 0)
    Sleep(10000)
    Sound(819, 0, 100, 0)
    Sleep(6000)
    Sound(819, 0, 100, 0)
    Return()

    # Function_50_4B07 end

    def Function_51_4B23(): pass

    label("Function_51_4B23")

    LoadEffect(0x0, "event/ev15001.eff")
    LoadEffect(0x1, "event/ev15002.eff")
    CreatePortrait(0, 0, 0, 440, 40, 20, 217, 512, 128, 0, 0, 440, 40, 0xFFFFFF, 0x0, "c_mini00.itp")
    CreatePortrait(1, 0, 0, 20, 10, 80, 232, 512, 128, 0, 50, 20, 60, 0xFFFFFF, 0x0, "c_mini00.itp")
    CreatePortrait(2, 0, 0, 20, 10, 380, 232, 512, 128, 0, 80, 20, 90, 0xFFFFFF, 0x0, "c_mini00.itp")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrPos(0xA, 0, 1250, 25500, 225)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 3300, 24000, 0)
    MoveCamera(0, 7, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "シュリが着地するタイミングに合わせて\x01",
            "　　　　『○ボタン』を押せ！　　　　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(1000)
    OP_E5(0xA)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7576", 1)
    Sleep(3000)
    FadeToBright(6000, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1770, 0x0, 0x0)
    Sleep(6000)
    SetChrChipByIndex(0xA, 0x39)
    Fade(500)
    SetChrSubChip(0xA, 0x0)
    Sleep(1400)
    BeginChrThread(0x3, 1, 0, 55)
    BeginChrThread(0x3, 2, 0, 56)
    BeginChrThread(0xA, 0, 0, 52)
    Sleep(10000)
    BeginChrThread(0xA, 0, 0, 53)
    Sleep(25000)
    Sleep(3000)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(2500, 0, -1)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    OP_0D()
    OP_E5(0xB)
    StopEffect(0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    OP_CC(0x1, 0x2, 0x0)
    Return()

    # Function_51_4B23 end

    def Function_52_4DA2(): pass

    label("Function_52_4DA2")

    Sound(809, 0, 40, 0)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 42)
    OP_9D(0xA, 0x0, 0x4E2, 0x59D8, 0xBB8, 0x44C)
    SetChrChipByIndex(0xA, 0x37)

    def lambda_4DD3():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0xA96, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4DD3)
    OP_49()
    Sound(809, 0, 40, 0)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 42)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x4E2)
    SetChrChipByIndex(0xA, 0x37)
    Sound(809, 0, 40, 0)
    BeginChrThread(0xA, 1, 0, 42)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x4E2)
    SetChrChipByIndex(0xA, 0x37)
    Sound(809, 0, 40, 0)
    BeginChrThread(0xA, 1, 0, 42)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x4E2)
    SetChrChipByIndex(0xA, 0x37)
    Sound(809, 0, 40, 0)
    BeginChrThread(0xA, 1, 0, 42)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x4E2)
    SetChrChipByIndex(0xA, 0x37)
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0xE1, 0x0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    Sleep(1250)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)

    def lambda_4EAF():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1068, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4EAF)
    Sleep(250)

    def lambda_4ECD():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1450, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4ECD)
    Sleep(250)

    def lambda_4EEB():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4EEB)
    Sleep(250)

    def lambda_4F09():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4F09)
    Return()

    # Function_52_4DA2 end

    def Function_53_4F20(): pass

    label("Function_53_4F20")


    def lambda_4F25():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4F25)
    OP_49()
    SetChrFlags(0xA, 0x1020)
    Call(0, 44)
    BeginChrThread(0xA, 1, 0, 45)
    Sleep(1000)

    def lambda_4F52():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4F52)
    OP_49()
    Sound(844, 0, 40, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0xA, 0x2)
    Sound(809, 0, 40, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(844, 0, 40, 0)

    def lambda_4FB2():
        OP_9E(0xA, 0x0, 0x636A, 0xFFF24460, 0x2A94, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4FB2)
    OP_49()
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x514)
    Sound(809, 0, 40, 0)

    def lambda_4FEB():
        OP_93(0xA, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4FEB)
    BeginChrThread(0xA, 1, 0, 42)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(844, 0, 40, 0)
    BeginChrThread(0xA, 1, 0, 42)

    def lambda_5021():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x2)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5021)
    OP_49()
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0xAF)
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0x10E, 0x0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    Sleep(1000)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x37)
    OP_96(0xA, 0xBB8, 0x4E2, 0x61A8, 0x7D0, 0x0)
    Sleep(700)
    SetChrChipByIndex(0xA, 0x38)
    OP_96(0xA, 0x7D0, 0x4E2, 0x61A8, 0x1194, 0x0)
    BeginChrThread(0xA, 1, 0, 41)
    Sound(809, 0, 40, 0)
    OP_9D(0xA, 0x3E8, 0x4E2, 0x61A8, 0x3E8, 0xBB8)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 1, 0, 46)
    Sound(809, 0, 40, 0)
    OP_9D(0xA, 0x0, 0x4E2, 0x61A8, 0x5DC, 0xBB8)
    BeginChrThread(0xA, 1, 0, 45)
    Sound(809, 0, 40, 0)
    OP_9D(0xA, 0xFFFFF92A, 0x4E2, 0x61A8, 0x7D0, 0xBB8)
    BeginChrThread(0xA, 1, 0, 42)

    def lambda_5119():
        OP_93(0xA, 0x5A, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5119)
    Sound(809, 0, 40, 0)
    OP_9D(0xA, 0xFFFFF060, 0x4E2, 0x61A8, 0xBB8, 0x578)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    Sleep(500)
    EndChrThread(0xA, 0x3)
    SetChrChip(0x0, 0xA, 0xBB8, 0x12C)
    Sleep(400)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 2, 0, 45)
    Sound(809, 0, 40, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0x7D0, 0x8FC)
    Sleep(900)
    SetChrFlags(0xA, 0x1020)
    Call(0, 44)
    BeginChrThread(0xA, 1, 0, 46)
    OP_96(0xA, 0xFFFFF830, 0x4E2, 0x6590, 0x1B58, 0x0)
    OP_9E(0xA, 0xFFFFFE0C, 0x61A8, 0x2BF20, 0x2328, 0x0)
    BeginChrThread(0xA, 1, 0, 45)
    OP_9E(0xA, 0xC8, 0x61A8, 0x2BF20, 0x2328, 0x0)
    OP_9E(0xA, 0xFFFFFF06, 0x61A8, 0x2BF20, 0x2328, 0x0)
    OP_9E(0xA, 0x32, 0x61A8, 0x7A120, 0x2328, 0x0)
    BeginChrThread(0xA, 2, 0, 54)
    Sound(844, 0, 40, 0)
    OP_9D(0xA, 0x0, 0x4E2, 0x639C, 0xFA0, 0x514)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x1)
    OP_93(0xA, 0x87, 0x0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(1000)
    EndChrThread(0xA, 0x3)
    StopBGM(0x7D0)
    Return()

    # Function_53_4F20 end

    def Function_54_5249(): pass

    label("Function_54_5249")

    OP_D5(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D5(0xFE, 0x0, 0x0, 0xFFFA81C0, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_54_5249 end

    def Function_55_527A(): pass

    label("Function_55_527A")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58C3")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4E2), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4E3), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52E4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58B2")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58B2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58A8")
    OP_64(0xA)
    OP_63(0xA, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sound(1028, 0, 100, 0)
    Sound(3, 0, 100, 0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0xA, 0x3)
    SetChrChip(0x0, 0xA, 0xBB8, 0x12C)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5383")
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x64, 0x0, 0x0)
    Jump("loc_589B")

    label("loc_5383")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53D0")
    OP_CB(0x2, 0x1, 0x7D0, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x57E40, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x28, 0x5A)
    Jump("loc_589B")

    label("loc_53D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_541D")
    OP_CB(0x2, 0x1, 0xBB8, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x53020, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x3C, 0x5A)
    Jump("loc_589B")

    label("loc_541D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_546A")
    OP_CB(0x2, 0x1, 0xFA0, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x4E200, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x50, 0x5A)
    Jump("loc_589B")

    label("loc_546A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54B7")
    OP_CB(0x2, 0x1, 0x1388, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x493E0, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x64, 0x5A)
    Jump("loc_589B")

    label("loc_54B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5504")
    OP_CB(0x2, 0x1, 0x1770, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x445C0, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x78, 0x5A)
    Jump("loc_589B")

    label("loc_5504")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5551")
    OP_CB(0x2, 0x1, 0x1B58, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x3F7A0, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x8C, 0x5A)
    Jump("loc_589B")

    label("loc_5551")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_559E")
    OP_CB(0x2, 0x1, 0x1F40, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x3A980, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0xA0, 0x5A)
    Jump("loc_589B")

    label("loc_559E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55EB")
    OP_CB(0x2, 0x1, 0x2328, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x35B60, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0xB4, 0x5A)
    Jump("loc_589B")

    label("loc_55EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5638")
    OP_CB(0x2, 0x1, 0x2710, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x30D40, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0xC8, 0x5A)
    Jump("loc_589B")

    label("loc_5638")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5685")
    OP_CB(0x2, 0x1, 0x2AF8, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x2BF20, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0xDC, 0x5A)
    Jump("loc_589B")

    label("loc_5685")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56D2")
    OP_CB(0x2, 0x1, 0x2EE0, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x27100, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0xF0, 0x5A)
    Jump("loc_589B")

    label("loc_56D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_571F")
    OP_CB(0x2, 0x1, 0x32C8, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x222E0, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x104, 0x5A)
    Jump("loc_589B")

    label("loc_571F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_576C")
    OP_CB(0x2, 0x1, 0x36B0, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x1D4C0, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x118, 0x5A)
    Jump("loc_589B")

    label("loc_576C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B9")
    OP_CB(0x2, 0x1, 0x3A98, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x186A0, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x12C, 0x5A)
    Jump("loc_589B")

    label("loc_57B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5806")
    OP_CB(0x2, 0x1, 0x3E80, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x13880, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x140, 0x5A)
    Jump("loc_589B")

    label("loc_5806")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5853")
    OP_CB(0x2, 0x1, 0x4268, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xEA60, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x154, 0x5A)
    Jump("loc_589B")

    label("loc_5853")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589B")
    OP_CB(0x2, 0x1, 0x4650, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x9C40, 0x38A40, 0x0, 0x0)
    OP_CB(0x2, 0x8, 0x0, 0x50, 0x168, 0x5A)

    label("loc_589B")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(100)

    label("loc_58A8")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58B2")

    RunExpression(0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_52B5")

    label("loc_58C3")

    Return()

    # Function_55_527A end

    def Function_56_58C4(): pass

    label("Function_56_58C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E42")
    OP_57(0x3)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0xA), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x8), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E23")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_64(0xA)
    OP_63(0xA, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sound(1027, 0, 100, 0)
    Sound(87, 0, 50, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xA, 3, 0, 47)
    SetChrChip(0x0, 0xA, 0x12C, 0xBB8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A3C")
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    Jump("loc_5E11")

    label("loc_5A3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A76")
    OP_CB(0x1, 0x1, 0x7D0, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x28, 0x3C)
    Jump("loc_5E11")

    label("loc_5A76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AB0")
    OP_CB(0x1, 0x1, 0xBB8, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x3C, 0x3C)
    Jump("loc_5E11")

    label("loc_5AB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AEA")
    OP_CB(0x1, 0x1, 0xFA0, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x50, 0x3C)
    Jump("loc_5E11")

    label("loc_5AEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B24")
    OP_CB(0x1, 0x1, 0x1388, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x64, 0x3C)
    Jump("loc_5E11")

    label("loc_5B24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B5E")
    OP_CB(0x1, 0x1, 0x1770, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x78, 0x3C)
    Jump("loc_5E11")

    label("loc_5B5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B98")
    OP_CB(0x1, 0x1, 0x1B58, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x8C, 0x3C)
    Jump("loc_5E11")

    label("loc_5B98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BD2")
    OP_CB(0x1, 0x1, 0x1F40, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0xA0, 0x3C)
    Jump("loc_5E11")

    label("loc_5BD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C0C")
    OP_CB(0x1, 0x1, 0x2328, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0xB4, 0x3C)
    Jump("loc_5E11")

    label("loc_5C0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C46")
    OP_CB(0x1, 0x1, 0x2710, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0xC8, 0x3C)
    Jump("loc_5E11")

    label("loc_5C46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C80")
    OP_CB(0x1, 0x1, 0x2AF8, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0xDC, 0x3C)
    Jump("loc_5E11")

    label("loc_5C80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CBA")
    OP_CB(0x1, 0x1, 0x2EE0, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0xF0, 0x3C)
    Jump("loc_5E11")

    label("loc_5CBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CF4")
    OP_CB(0x1, 0x1, 0x32C8, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x104, 0x3C)
    Jump("loc_5E11")

    label("loc_5CF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D2E")
    OP_CB(0x1, 0x1, 0x36B0, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x118, 0x3C)
    Jump("loc_5E11")

    label("loc_5D2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D68")
    OP_CB(0x1, 0x1, 0x3A98, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x12C, 0x3C)
    Jump("loc_5E11")

    label("loc_5D68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DA2")
    OP_CB(0x1, 0x1, 0x3E80, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x140, 0x3C)
    Jump("loc_5E11")

    label("loc_5DA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DDC")
    OP_CB(0x1, 0x1, 0x4268, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x154, 0x3C)
    Jump("loc_5E11")

    label("loc_5DDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E11")
    OP_CB(0x1, 0x1, 0x4650, 0x3E8, 0x0, 0x0)
    OP_CB(0x1, 0x8, 0x0, 0x32, 0x168, 0x3C)

    label("loc_5E11")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(300)
    Jump("loc_5E3A")

    label("loc_5E23")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    label("loc_5E3A")

    Sleep(1)
    Jump("Function_56_58C4")

    label("loc_5E42")

    Return()

    # Function_56_58C4 end

    def Function_57_5E43(): pass

    label("Function_57_5E43")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10000.itc", 0x1E)
    LoadChrToIndex("chr/ch09700.itc", 0x1F)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -540, 1250, 24890, 225)
    OP_68(-1550, 2500, 23490, 0)
    MoveCamera(354, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetChrPos(0x101, -1800, 1250, 23000, 45)
    SetChrPos(0x102, -1280, 1250, 22120, 45)
    SetChrPos(0x103, -2680, 1250, 23520, 45)
    SetChrPos(0x104, -2700, 1250, 21400, 45)
    SetChrPos(0x109, -2180, 1250, 20520, 45)
    SetChrPos(0x105, -3580, 1250, 21920, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("chr/ch14150.itc", 0x37)
    LoadChrToIndex("chr/ch14151.itc", 0x38)
    LoadChrToIndex("chr/ch14152.itc", 0x39)
    LoadChrToIndex("chr/ch14153.itc", 0x3A)
    LoadChrToIndex("chr/ch14154.itc", 0x3B)
    LoadChrToIndex("chr/ch14100.itc", 0x3C)
    SetChrChipByIndex(0xA, 0x3C)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0050
    ChrTalk(
        0xA,
        (
            "#12203Fそれじゃ、\x01",
            "さっそく説明させてもらう。\x02\x03",

            "#12201Fまずはこれを受け取ってくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xA, 0x101, 0x4B0, 0x7D0, 0x0)
    SetChrName("")

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはホイッスルを受け取った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_96(0xA, 0xFFFFFDE4, 0x4E2, 0x613A, 0x7D0, 0x0)

    #C0052
    ChrTalk(
        0x101,
        (
            "#00005Fこれは……ホイッスル？\x01",
            "一体、何に使うんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xA,
        (
            "#12203Fああ、今からオレは\x01",
            "本番を想定して演技をするから……\x02\x03",

            "#12201F演技中、オレがジャンプする度に\x01",
            "“着地のタイミング”で\x01",
            "そのホイッスルを鳴らしてくれ。\x02\x03",

            "演技の流れを知らなくても、\x01",
            "オレの動きを目で追ってくれれば\x01",
            "できるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00001Fなるほど、着地のタイミングで……\x02\x03",

            "#00005Fって、それだけでいいのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xA,
        (
            "#12203Fああ、単純だけど大事なことだ。\x02\x03",

            "#12201Fアルカンシェルの演技で重要なのは\x01",
            "何と言ってもジャンプだ。\x02\x03",

            "中でも“着地”は全ての動きに\x01",
            "つながる大切な基本動作だからな。\x02\x03",

            "ホイッスルは、その意識を\x01",
            "高めるためのきっかけなんだ。\x02\x03",

            "#12206Fだから、間違っても\x01",
            "おかしなタイミングで鳴らすなよ。\x01",
            "むしろ混乱しちゃうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#00002F分かった、気を付けるよ。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xA,
        (
            "#12200Fで、説明は以上だけど、\x01",
            "さっそく始めて大丈夫か？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        "#00000Fああ、いつでも準備オッケーだ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    BeginChrThread(0x0, 0, 0, 51)
    WaitChrThread(0x0, 0)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x3)
    SetChrChipByIndex(0xA, 0x3C)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x1020)
    SetChrPos(0xA, 0, 1250, 25500, 225)
    SetChrPos(0x101, -1800, 1250, 23000, 45)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x103, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x105, 0x80)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x3, 0x2)
    OP_68(-1200, 2500, 24000, 0)
    MoveCamera(354, 18, 1, 0)
    OP_6E(460, 0)
    SetCameraDistance(19290, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    #C0059
    ChrTalk(
        0xA,
        "#12206Fふう、何とか形にはなったかな。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#00002Fいや、形どころか\x01",
            "大したもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        (
            "#00102Fええ、本当に。\x01",
            "自信を持っていいと思うわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65DF")
    OP_2C(0x8D, 0x2)
    OP_29(0x8D, 0x1, 0x0)

    #C0062
    ChrTalk(
        0xA,
        (
            "#12212Fあ、あんがと……\x02\x03",

            "#12202Fそれにしても、完璧に\x01",
            "合わせてくるなんてやるじゃん。\x02\x03",

            "おかげで割りとつながりを\x01",
            "意識することが出来たし、\x01",
            "かなり身のある練習になったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#00002Fはは、そこまで言ってくれるなら\x01",
            "御の字ってところかな。\x02\x03",

            "お役に立てたようで何よりだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A4")

    label("loc_65DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66A9")
    OP_2C(0x8D, 0x1)
    OP_29(0x8D, 0x1, 0x1)

    #C0064
    ChrTalk(
        0xA,
        (
            "#12212Fあ、あんがと……\x02\x03",

            "#12200Fま、ホイッスルのタイミングが\x01",
            "怪しかったりもしたけど……\x02\x03",

            "それでも十分\x01",
            "身のある練習になったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#00000Fそうか、なら良かったよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_67A4")

    label("loc_66A9")

    OP_29(0x8D, 0x1, 0x2)

    #C0066
    ChrTalk(
        0xA,
        (
            "#12212Fあ、あんがと……\x02\x03",

            "#12206Fでも、ホイッスルの方は\x01",
            "正直ダメダメだったな。\x02\x03",

            "まあ逆に、正しいタイミングが\x01",
            "自分に身に付いてるって判ったけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00006Fあ、ああ、面目ない。\x02\x03",

            "#00008F（目で動きを追うか……\x01",
            "  思ったよりも難しかったな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67A4")


    #C0068
    ChrTalk(
        0xA,
        (
            "#12203Fそれで、ここからが\x01",
            "本題なんだけど……\x02\x03",

            "#12201Fオレの演技を改めて観て\x01",
            "その、どうだった……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-1800, 2500, 23700, 0)
    MoveCamera(260, 21, 1, 0)
    OP_6E(560, 0)
    SetCameraDistance(14730, 0)
    OP_0D()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00000Fそうだな……\x02\x03",

            "いや、なんていうか\x01",
            "単純に凄いって思わされたよ。\x02\x03",

            "よくあれだけの演技を\x01",
            "ものにしたっていうか……\x02\x03",

            "#00006Fでもごめん、正直素人の\x01",
            "俺にはこれ以上気の利いたことは\x01",
            "言えそうにないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "#12203Fそうか……\x02\x03",

            "#12201Fそれじゃ、最初に言ってた\x01",
            "オレの演技に無駄がないって話……\x02\x03",

            "それについて\x01",
            "詳しく教えてくれないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0071
    ChrTalk(
        0x101,
        (
            "#00005F俺、そんな風に言ったんだっけ？\x02\x03",

            "#00006Fいや、それは別になにも\x01",
            "悪い意味で言ったんじゃなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "#12203F…………\x02\x03",

            "#12208F……実はイリアさんにも\x01",
            "同じように言われたことがある。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#00005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "#12208Fあんたの演技には無駄がない……\x02\x03",

            "あんたの演技には遊びがない……\x02\x03",

            "#12206Fそれに……もっと楽しんでやれって。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x104,
        "#00300F楽しんでやれ、か……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        "#00105Fイリアさんがそんなことを……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x105,
        (
            "#10303Fフム、でもそういう意味では\x01",
            "技術的には大きな問題はない……\x02\x03",

            "#10300Fどちらかと言うと、\x01",
            "メンタル的な問題なのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0078
    ChrTalk(
        0xA,
        (
            "#12211Fなんだよ、メンタルって！\x01",
            "ゼンゼン意味わかんねえよ！\x02\x03",

            "#12208F……………\x02\x03",

            "#12206Fでもこんなんじゃ……\x01",
            "明日の舞台もきっと\x01",
            "うまくいきっこないよな。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    #C0079
    ChrTalk(
        0x103,
        "#00201Fシュリさん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)

    #C0080
    ChrTalk(
        0x101,
        (
            "#00003F……なあ、シュリ。\x01",
            "ちょっと聞きたいんだが。\x02\x03",

            "#00001F君は演技の練習中、\x01",
            "どんなことを考えている？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "#12205Fえ、ああ……？\x02\x03",

            "#12201Fそんなのもちろん、\x01",
            "もっと上手くなりたいと\x01",
            "思ってるに決まってるだろ。\x02\x03",

            "#12208F……いや、ちょっと違うな。\x02\x03",

            "オレは……イリアさんと\x01",
            "リーシャ姉みたいな演技が\x01",
            "したいんだ。\x02\x03",

            "#12201Fオレがはじめて２人を観た時に\x01",
            "感じたような……\x02\x03",

            "なんていうか、\x01",
            "心をグッと掴まれるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        "#00102Fシュリちゃん……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x109,
        "#10100Fなんていうか、まっすぐだね。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0084
    ChrTalk(
        0xA,
        "#12211Fべ、別にそんなんじゃ……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#00003Fそうか……\x01",
            "じゃあ、こんな質問はどうだ。\x02\x03",

            "#00001Fアルカンシェルの舞台の上で\x01",
            "演技をする事についてはどう思う？\x02\x03",

            "劇場に来た観客に、\x01",
            "演技を観てもらうことについては\x01",
            "どう思ってる？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xA,
        (
            "#12201F……観客？　ああ、観客か。\x02\x03",

            "#12208F最近は都会の連中にも色んな\x01",
            "ヤツがいるって分かったけど……\x02\x03",

            "それでもやっぱり、\x01",
            "オレは自分が恵まれていることに\x01",
            "自覚のない連中は好きになれない。\x02\x03",

            "#12201F全部とは言わないけど……\x01",
            "あそこに来る客は\x01",
            "ほとんどがそんな連中だ。\x02\x03",

            "だから……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#00001Fだから……\x01",
            "観られることも良く思えないか？\x02\x03",

            "……つまり、演技を\x01",
            "純粋に楽しめないってことか？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        (
            "#12206Fん、まあ……\x01",
            "気持ち的にはそうかもな。\x02\x03",

            "考えないようにはしてるけど、\x01",
            "そんな連中のためにと思うと\x01",
            "正直虫唾が走るくらいだ。\x02\x03",

            "#12201Fでも、悪いかよ――\x01",
            "ってか、そんな気持ちなんて\x01",
            "演技とは関係ないだろう？\x02\x03",

            "オレが聞きたいのは、\x01",
            "もっと具体的にどこがどう\x01",
            "悪かったかってことで……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00003F気持ちと演技とは関係ない、か。\x02\x03",

            "#00001F……果たして、本当にそうなのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0090
    ChrTalk(
        0xA,
        (
            "#12207Fそんなこと言っても……\x01",
            "じゃあ、一体オレは\x01",
            "具体的にどうすりゃいいんだよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00008Fそれは……\x01",
            "何て言ったらいいか\x01",
            "分からないけど……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 0, 1100, 8800, 360)

    #N0092
    NpcTalk(
        0x8,
        "女性の声",
        (
            "――だったらシュリ、\x01",
            "目の前の客なんて無視しなさい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    def lambda_740B():

        label("loc_740B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_740B")

    QueueWorkItem2(0x109, 0, lambda_740B)
    Sleep(50)

    def lambda_7420():

        label("loc_7420")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7420")

    QueueWorkItem2(0x102, 0, lambda_7420)
    Sleep(50)

    def lambda_7435():

        label("loc_7435")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7435")

    QueueWorkItem2(0x104, 0, lambda_7435)
    Sleep(50)

    def lambda_744A():

        label("loc_744A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_744A")

    QueueWorkItem2(0x101, 0, lambda_744A)
    Sleep(50)

    def lambda_745F():

        label("loc_745F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_745F")

    QueueWorkItem2(0x105, 0, lambda_745F)
    Sleep(50)

    def lambda_7474():

        label("loc_7474")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7474")

    QueueWorkItem2(0x103, 0, lambda_7474)
    Sleep(50)

    def lambda_7489():

        label("loc_7489")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7489")

    QueueWorkItem2(0xA, 0, lambda_7489)
    Fade(500)
    OP_68(-250, 2000, 21140, 0)
    MoveCamera(203, 15, 1, 0)
    OP_6E(460, 0)
    SetCameraDistance(17000, 0)
    Sleep(500)

    def lambda_74D1():
        OP_97(0xFE, 0x0, 0xFFFFF830, 0x2710, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_74D1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-940, 2600, 21160, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18850, 0)
    EndChrThread(0x8, 0x1)
    SetChrPos(0x8, 1600, 1250, 21090, 270)
    SetChrPos(0xA, 1600, 1250, 23000, 180)
    SetChrPos(0x102, -1800, 1250, 22800, 45)
    SetChrPos(0x101, -1800, 1250, 21500, 45)
    SetChrPos(0x103, -1800, 1250, 20200, 45)
    SetChrPos(0x105, -3000, 1250, 22800, 45)
    SetChrPos(0x104, -3000, 1250, 21500, 45)
    SetChrPos(0x109, -3000, 1250, 20200, 45)
    FadeToBright(1000, 0)
    Sleep(500)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x103, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0xA, 0x0)
    OP_0D()

    #C0093
    ChrTalk(
        0x8,
        "#06109Fやっほー、弟君たち。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#00005Fイリアさん。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "#12207F#5P――って、\x01",
            "一体いつからいたんだよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(30, 2800, 20910, 2000)
    TurnDirection(0x8, 0xA, 500)
    OP_6F(0x79)

    #C0096
    ChrTalk(
        0x8,
        (
            "#06104Fんー、まあ今来たところだけど。\x02\x03",

            "#06100Fで、シュリ。\x01",
            "観客のことが嫌いなんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        "#12208Fフンッ、悪いかよ。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "#06104Fいいえ、悪くないわ。\x02\x03",

            "多かれ少なかれ、\x01",
            "あたしだって嫌いな客はいるし。\x02\x03",

            "#06102Fただね、そんなこと\x01",
            "いちいち気にしちゃいないわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "#12201F分かってる、だからオレだって\x01",
            "気にしないよう努力してる。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "#06106Fふう、あんたの場合\x01",
            "まずその考え方が問題アリね。\x02\x03",

            "#06102Fいい？　あんたは\x01",
            "目の前のことに囚われすぎなの。\x02\x03",

            "ねえシュリ、観客ってのは\x01",
            "誰のことを指しているか分かる？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "#12201Fああ、劇場に足を運んでくれた\x01",
            "お客さんのことだろ。\x01",
            "チケット代を出してくれる。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "#06103Fええ、それも間違いじゃないけど。\x01",
            "もっと大事なことがあるわ。\x02\x03",

            "#06100Fお客さんってのはね、何も劇場に\x01",
            "来てくれた人だけじゃないの。\x02\x03",

            "あたしたちの舞台に\x01",
            "興味を持ってくれる人、\x01",
            "その全てがお客さんなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        "#12205F興味のある人全て……？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "#06103Fそう、例えば劇団のことを\x01",
            "雑誌で見ただけの人だってそうだし、\x01",
            "話に聞いただけの人だってそう。\x02\x03",

            "どんな形でも興味を持ってくれたら\x01",
            "その時点でお客さんと言えるわ。\x02\x03",

            "#06102Fアンタにも心当りあるでしょう？\x02\x03",

            "クロスベルに来て、\x01",
            "アルカンシェルの噂を聞いて……\x02\x03",

            "劇場に忍び込んで、舞台を観て、\x01",
            "何かを感じ取ったんでしょう？\x02\x03",

            "ま、忍び込んだって所が\x01",
            "ちょっと褒められはしないけど。\x02\x03",

            "#06109Fそれでも、あの時のアンタは\x01",
            "立派なお客さんに違いないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        "#12211F忍び込んだオレが……立派な客？\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "#06100Fそう、だから何も目の前の\x01",
            "お客さんに囚われることはないの。\x02\x03",

            "#06109F何たってあたしたちは、\x01",
            "大陸中の人間を相手にしている\x01",
            "ようなものなんだから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0107
    ChrTalk(
        0xA,
        "#12207Fた、大陸中の人間！？\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "#06102Fふふ、だってそうじゃない。\x02\x03",

            "アルカンシェルの名前は\x01",
            "まだまだ大陸中に広まっているとは\x01",
            "言えないけど……\x02\x03",

            "#06104Fそれでも舞台というものを通して、\x01",
            "ノーザンブリア出身のあんたと\x01",
            "クロスベル出身の私がつながった。\x02\x03",

            "この出会いをあんたは偶然と\x01",
            "思ってるかもしれないけど……\x01",
            "あたしはそうじゃないと思ってる。\x02\x03",

            "#06109Fそう考えると舞台で表現することって、\x01",
            "凄く魅力的で楽しいことだと思わない？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        "#12205F…………………………\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "#06104Fふふ、まあいいわ。\x01",
            "またゆっくり考えなさい。\x02\x03",

            "#06101Fそれはともかくシュリ、\x01",
            "あんた今朝もご飯を\x01",
            "食べて行かなかったでしょ。\x02\x03",

            "楽屋にお弁当を用意してあるから\x01",
            "さっさと済ませてきなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "#12208Fべ、弁当って……\x01",
            "別にいいよ、そんなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "#06102Fだーめ、何度も言うけど\x01",
            "あたしらは体が資本なんだから。\x02\x03",

            "食べるまで練習はお預けよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "#12201Fちぇっ、相変わらずうるせえなぁ。\x02\x03",

            "#12207F分かったよ、\x01",
            "さっさと済ませてくらぁ！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1730, 3000, 20020, 2000)
    MoveCamera(45, 22, 0, 2000)
    OP_6E(480, 2000)
    SetCameraDistance(17010, 2000)

    def lambda_7FE0():

        label("loc_7FE0")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_7FE0")

    QueueWorkItem2(0x109, 0, lambda_7FE0)

    def lambda_7FF2():

        label("loc_7FF2")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_7FF2")

    QueueWorkItem2(0x102, 0, lambda_7FF2)

    def lambda_8004():

        label("loc_8004")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_8004")

    QueueWorkItem2(0x104, 0, lambda_8004)

    def lambda_8016():

        label("loc_8016")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_8016")

    QueueWorkItem2(0x101, 0, lambda_8016)

    def lambda_8028():

        label("loc_8028")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_8028")

    QueueWorkItem2(0x105, 0, lambda_8028)

    def lambda_803A():

        label("loc_803A")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_803A")

    QueueWorkItem2(0x103, 0, lambda_803A)

    def lambda_804C():

        label("loc_804C")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_804C")

    QueueWorkItem2(0x8, 0, lambda_804C)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)
    OP_95(0xA, -2590, 1250, 25130, 7000, 0x0)
    OP_95(0xA, -8310, 1250, 25700, 7000, 0x0)

    def lambda_808F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_808F)
    OP_95(0xA, -12090, 1250, 26230, 7000, 0x0)
    Sleep(1000)

    def lambda_80B7():

        label("loc_80B7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_80B7")

    QueueWorkItem2(0x109, 0, lambda_80B7)

    def lambda_80C9():

        label("loc_80C9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_80C9")

    QueueWorkItem2(0x102, 0, lambda_80C9)

    def lambda_80DB():

        label("loc_80DB")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_80DB")

    QueueWorkItem2(0x104, 0, lambda_80DB)

    def lambda_80ED():

        label("loc_80ED")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_80ED")

    QueueWorkItem2(0x101, 0, lambda_80ED)

    def lambda_80FF():

        label("loc_80FF")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_80FF")

    QueueWorkItem2(0x105, 0, lambda_80FF)

    def lambda_8111():

        label("loc_8111")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_8111")

    QueueWorkItem2(0x103, 0, lambda_8111)
    Sleep(1000)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x103, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x8, 0x0)

    #C0114
    ChrTalk(
        0x101,
        (
            "#00002F何というか、いい場面に\x01",
            "立ち合わせてもらいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x102,
        (
            "#00102Fええ、イリアさんのお言葉\x01",
            "とっても心に染みました。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x104,
        (
            "#00302Fそれに何つうか、\x01",
            "母親してんすねえ。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    TurnDirection(0x8, 0x101, 500)

    #C0117
    ChrTalk(
        0x8,
        (
            "#06109Fふふ、そうね。\x01",
            "おかげ様で飽きないわよ。\x02\x03",

            "#06100F弟君たちも、ありがとうね。\x02\x03",

            "何だか、あの娘の悩みを\x01",
            "聞いてもらっちゃった感じで。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0118
    ChrTalk(
        0x101,
        (
            "#00005Fもしかして……\x01",
            "最初から全部見ていたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "#06102Fええ、観客席の影からバッチリね。\x02\x03",

            "#06103Fあの娘とは普段から\x01",
            "色々話してはいるんだけど……\x02\x03",

            "実は今みたいに\x01",
            "本音を引き出す機会ってのは\x01",
            "なかなかなくてね。\x02\x03",

            "#06109Fほんと弟君には感謝してるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#00011Fいえ、そんなこと……\x02\x03",

            "#00006Fそれに肝心のアドバイスは\x01",
            "ほとんど出来ませんでしたし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_83FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_83FB)
    SetChrPos(0xA, -8310, 1250, 25700, 90)
    Sound(809, 0, 70, 0)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 41)
    OP_9D(0xA, 0xFFFFF312, 0x4E2, 0x5E10, 0x7D0, 0x1388)
    Sound(50, 0, 100, 0)
    OP_68(-1730, 3000, 20020, 2000)
    MoveCamera(33, 22, 0, 2000)
    OP_6E(480, 2000)
    SetCameraDistance(17010, 2000)

    def lambda_8479():

        label("loc_8479")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_8479")

    QueueWorkItem2(0x8, 2, lambda_8479)

    def lambda_848B():

        label("loc_848B")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_848B")

    QueueWorkItem2(0x105, 2, lambda_848B)

    def lambda_849D():

        label("loc_849D")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_849D")

    QueueWorkItem2(0x104, 2, lambda_849D)

    def lambda_84AF():

        label("loc_84AF")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_84AF")

    QueueWorkItem2(0x101, 2, lambda_84AF)

    def lambda_84C1():

        label("loc_84C1")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_84C1")

    QueueWorkItem2(0x109, 2, lambda_84C1)

    def lambda_84D3():

        label("loc_84D3")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_84D3")

    QueueWorkItem2(0x102, 2, lambda_84D3)

    def lambda_84E5():

        label("loc_84E5")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_84E5")

    QueueWorkItem2(0x103, 2, lambda_84E5)
    OP_93(0xA, 0x87, 0x0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(500)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)
    OP_95(0xA, -810, 1250, 24380, 5000, 0x0)
    OP_95(0xA, 640, 1250, 22660, 5000, 0x0)
    SetChrChipByIndex(0xA, 0x3C)
    SetChrSubChip(0xA, 0x0)
    TurnDirection(0xA, 0x8, 500)
    OP_6F(0x79)

    #C0121
    ChrTalk(
        0xA,
        "#12201F#5Pイリアさん、食い終わったぞ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0122
    ChrTalk(
        0x103,
        "#00206F#5Pシュリさん、恐るべき早さです。\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0xFF)

    #C0123
    ChrTalk(
        0x8,
        (
            "#06106Fはあ、いつもよく噛めって\x01",
            "言ってるんだけど……まあいいか。\x02\x03",

            "#06100Fよし、それじゃあ\x01",
            "さっそく稽古の続きを始めるわよ。\x02\x03",

            "場面は星の姫が登場するシーンから。\x01",
            "ビシビシ行くからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        "#12202F#5Pおう、望むところだ！\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x109,
        (
            "#10109Fあはは、何だか\x01",
            "シュリちゃん元気ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x105,
        "#10302Fフフ、少しは吹っ切れたのかな？\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x104,
        "#00302Fはは、だといいがな。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        (
            "#00000Fまあ、とりあえず\x01",
            "俺たちはこの辺で失礼するか。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#00102Fイリアさんにシュリちゃん、\x01",
            "明日の舞台、頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 500)
    TurnDirection(0x8, 0x101, 500)

    #C0130
    ChrTalk(
        0xA,
        "#12200F#2Pあ、ああ……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "#06109Fふふ、もちろんよ。\x01",
            "それじゃあね、弟君たち㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_6E(580, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0132
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【秘密の演技指導】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x8D, 0x4, 0x10)
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_57_5E43 end

    SaveToFile()

Try(main)
