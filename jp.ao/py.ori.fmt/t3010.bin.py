from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t3010.bin",                # FileName
        "t3010",                    # MapName
        "t3010",                    # Location
        0x005B,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1E,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 91, 0, 0, 0, 1],
    )

    BuildStringList((
        "t3010",                  # 0
        "案内人形",               # 1
        "ヨルグ老人",             # 2
        "パテマテ",               # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(332, 0)                                        # 0

    ScpFunction((
        "Function_0_14C",          # 00, 0
        "Function_1_17A",          # 01, 1
        "Function_2_1AA",          # 02, 2
        "Function_3_2EC8",         # 03, 3
        "Function_4_2F07",         # 04, 4
        "Function_5_2F6A",         # 05, 5
        "Function_6_2FF7",         # 06, 6
        "Function_7_3083",         # 07, 7
        "Function_8_30CD",         # 08, 8
        "Function_9_3107",         # 09, 9
        "Function_10_3147",        # 0A, 10
        "Function_11_3191",        # 0B, 11
        "Function_12_31CB",        # 0C, 12
        "Function_13_320B",        # 0D, 13
        "Function_14_3255",        # 0E, 14
        "Function_15_328F",        # 0F, 15
        "Function_16_32CF",        # 10, 16
        "Function_17_3319",        # 11, 17
        "Function_18_3353",        # 12, 18
        "Function_19_3393",        # 13, 19
        "Function_20_33DD",        # 14, 20
        "Function_21_3417",        # 15, 21
        "Function_22_3457",        # 16, 22
        "Function_23_34A1",        # 17, 23
        "Function_24_34DB",        # 18, 24
    ))


    def Function_0_14C(): pass

    label("Function_0_14C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_165")
    SetScenarioFlags(0x0, 4)
    Event(0, 2)
    Jump("loc_179")

    label("loc_165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_179")
    SetScenarioFlags(0x0, 5)
    Event(0, 24)

    label("loc_179")

    Return()

    # Function_0_14C end

    def Function_1_17A(): pass

    label("Function_1_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_194")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)
    Jump("loc_1A9")

    label("loc_194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1A9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 5)

    label("loc_1A9")

    Return()

    # Function_1_17A end

    def Function_2_1AA(): pass

    label("Function_2_1AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06600.itc", 0x1E)
    LoadChrToIndex("chr/ch47400.itc", 0x1F)
    SoundLoad(957)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis256.itp")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1F)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    OP_74(0x1, 0xF)
    OP_70(0x1, 0x65)
    SetChrPos(0xA, 8730, 250, 0, 270)
    OP_D5(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetChrPos(0x101, 0, 0, 87500, 0)
    SetChrPos(0x102, 500, 0, 87000, 0)
    SetChrPos(0x103, -750, 0, 86000, 0)
    SetChrPos(0x104, 0, 0, 85500, 0)
    SetChrPos(0x109, 750, 0, 84750, 0)
    SetChrPos(0x105, 1250, 0, 86000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 0, 0, 90000, 0)
    OP_68(0, 600, 88000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    BeginChrThread(0x8, 1, 0, 3)
    Sleep(50)
    BeginChrThread(0x101, 1, 0, 6)
    Sleep(30)
    BeginChrThread(0x102, 1, 0, 9)
    Sleep(50)
    BeginChrThread(0x103, 1, 0, 12)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 15)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 21)
    Sleep(50)
    BeginChrThread(0x109, 1, 0, 18)
    Sound(957, 2, 40, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(14000)
    StopSound(957, 1000, 30)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こうして、ロイドたちは\x01",
            "案内役の自動人形に導かれ……\x02\x03",

            "迷宮のように入り組んだ\x01",
            "地下工房の一角へと案内された。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x8, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x109, 0x1)
    SetChrPos(0x101, 0, 0, 7000, 180)
    SetChrPos(0x102, 250, 0, 7000, 180)
    SetChrPos(0x103, -250, 0, 7000, 180)
    SetChrPos(0x104, 0, 0, 7000, 180)
    SetChrPos(0x109, 250, 0, 7000, 180)
    SetChrPos(0x105, -500, 0, 7000, 180)
    SetChrPos(0x8, 0, 0, 7000, 180)
    SetChrPos(0x9, -2000, 0, -4700, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayBGM("ed7304", 0)
    OP_68(0, 600, 7000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(0, 600, 4000, 4000)
    BeginChrThread(0x8, 1, 0, 4)
    Sleep(3000)
    BeginChrThread(0x101, 1, 0, 7)
    Sleep(500)
    BeginChrThread(0x103, 1, 0, 13)
    Sleep(500)
    BeginChrThread(0x102, 1, 0, 10)
    Sleep(500)
    BeginChrThread(0x104, 1, 0, 16)
    Sleep(500)
    BeginChrThread(0x105, 1, 0, 22)
    Sleep(500)
    BeginChrThread(0x109, 1, 0, 19)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x101, 0x1)

    def lambda_65D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_65D)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)

    def lambda_672():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_672)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x109, 0x1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)

    #C0002
    ChrTalk(
        0x101,
        "#00013F#5Pこ、ここは……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        "#00205F#5P……凄いです……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    BeginChrThread(0x9, 1, 0, 5)
    OP_68(-2000, 600, -4700, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(4250, 1000, 2300, 10000)
    MoveCamera(75, 15, 0, 10000)
    OP_6E(500, 10000)
    SetCameraDistance(28000, 10000)
    PlaceName2(340, 200, "c_plac16", 0x0, 3000)
    OP_0D()
    OP_6F(0x79)

    def lambda_74C():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_74C)
    Sleep(50)

    def lambda_75C():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_75C)
    Sleep(50)

    def lambda_76C():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_76C)
    Sleep(50)

    def lambda_77C():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_77C)
    Sleep(50)

    def lambda_78C():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_78C)
    Sleep(50)

    def lambda_79C():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_79C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0004
    ChrTalk(
        0x109,
        "#10111F#6P#4Sなあっ……！？\x02",
    )

    CloseMessageWindow()
    OP_68(8730, 4000, 0, 3000)
    MoveCamera(72, 20, 0, 3000)
    SetCameraDistance(20000, 3000)
    OP_6F(0x79)
    Sleep(300)

    #C0005
    ChrTalk(
        0x105,
        (
            "#10301F#6P#Nひょっとして……\x01",
            "君らが言ってた巨大人形かい？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00006F#6P#Nああ……\x01",
            "レンっていう子が使っていた\x01",
            "《パテル＝マテル》だけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0007
    ChrTalk(
        0x102,
        "#00108F#6P#Nここに保管されていたのね……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0008
    ChrTalk(
        0x104,
        (
            "#00306F#6P#Nしかしまさか、この屋敷の地下に\x01",
            "こんな場所があったとは……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(4250, 1000, 2300, 0)
    MoveCamera(75, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(28000, 0)
    OP_0D()
    OP_93(0x103, 0x13B, 0x1F4)
    Sleep(300)

    #C0009
    ChrTalk(
        0x103,
        (
            "#00208F#11P何気に導力ネットの\x01",
            "端末らしきものもありますし……\x02\x03",

            "#00201F……まさか《仔猫》はここから\x01",
            "無線でネットに介入して……？\x02",
        )
    )

    CloseMessageWindow()

    #N0010
    NpcTalk(
        0x9,
        "老人の声",
        "──それで、何の用だ？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_ABF():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ABF)
    Sleep(50)

    def lambda_ACF():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ACF)
    Sleep(50)

    def lambda_ADF():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_ADF)
    Sleep(50)

    def lambda_AEF():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AEF)
    Sleep(50)

    def lambda_AFF():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AFF)
    Sleep(50)

    def lambda_B0F():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B0F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_68(-6000, 700, -650, 5000)
    MoveCamera(23, 17, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(20580, 5000)
    BeginChrThread(0x101, 1, 0, 8)
    BeginChrThread(0x103, 1, 0, 14)
    BeginChrThread(0x102, 1, 0, 11)
    BeginChrThread(0x104, 1, 0, 17)
    BeginChrThread(0x109, 1, 0, 20)
    BeginChrThread(0x105, 1, 0, 23)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_C29")

    #C0011
    ChrTalk(
        0x101,
        (
            "#00003F#5Pその……\x01",
            "時間を割いていただいて\x01",
            "ありがとうございました。\x02\x03",

            "#00001F実は、幾つか貴方に\x01",
            "お聞きしたい事がありまして。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D04")

    label("loc_C29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CA1")

    #C0012
    ChrTalk(
        0x101,
        (
            "#00003F#5Pその……\x01",
            "どうもお久しぶりです。\x02\x03",

            "#00001F実は、幾つか貴方に\x01",
            "お聞きしたい事がありまして。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D04")

    label("loc_CA1")


    #C0013
    ChrTalk(
        0x101,
        (
            "#00006F#5Pその……\x01",
            "どうも初めまして。\x02\x03",

            "#00001F実は、幾つか貴方に\x01",
            "お聞きしたい事がありまして。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D04")


    #C0014
    ChrTalk(
        0x9,
        (
            "#03903F#12Pフン……\x02\x03",

            "#03900F大方、カンパネルラが\x01",
            "ちょっかいをかけたという所か。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0015
    ChrTalk(
        0x101,
        "#00013F#5P……！\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        "#00301F#5P爺さん、あんた……\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x1E, 0x1F4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EEB")

    #C0017
    ChrTalk(
        0x9,
        (
            "#03903F#6P──カン違いするな。\x02\x03",

            "#03900F確かにわしは《結社》の関係者だが\x01",
            "あくまで一介の人形師に過ぎぬ。\x02\x03",

            "《結社》の計画そのものに\x01",
            "直接関わっているわけでもない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA9")

    label("loc_EEB")


    #C0018
    ChrTalk(
        0x9,
        (
            "#03903F#6P──カン違いするな。\x02\x03",

            "#03900Fレンから聞いておるように\x01",
            "確かにわしは《結社》の関係者だが\x01",
            "あくまで一介の人形師に過ぎぬ。\x02\x03",

            "《結社》の計画そのものに\x01",
            "直接関わっているわけでもない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA9")


    #C0019
    ChrTalk(
        0x101,
        (
            "#00006F#5Pそ、それじゃあ……\x02\x03",

            "#00001Fあのカンパネルラという少年が\x01",
            "何をしようとしているのか\x01",
            "貴方はご存知ないと……？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            "#03900F#6P知らぬし、知る立場にもない。\x02\x03",

            "#03903Fただ……\x01",
            "彼は《使徒》ではなく《執行者》だ。\x02\x03",

            "実際に《結社》が進めようとする\x01",
            "『計画』を提案する立場にはない。\x02\x03",

            "#03901Fそれを企画・立案しているのは\x01",
            "あくまで《使徒》という事になる。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        "#00101F#11Pちょ、ちょっと待って下さい……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x109,
        (
            "#10106F#11Pな、何だか話が急すぎて\x01",
            "理解が追いつかないというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x105,
        (
            "#10305F#11P重要な内部情報みたいだけど\x01",
            "簡単に喋っちゃってもいいわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        (
            "#03903F#6Pフフ……\x01",
            "別に禁ぜられてはおらぬからな。\x02\x03",

            "#03900Fそれに、この程度の情報ならば\x01",
            "知る者はそれなりにおるだろう。\x02\x03",

            "教会やギルド、大国の諜報機関ならば\x01",
            "とっくの昔に掴んでいるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#00001F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        (
            "#00201F#5Pにも関わらず、貴方はここで\x01",
            "人形を作り続けていられる……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "#03903F#6Pそもそも《結社》の全貌を\x01",
            "知る立場にはないからな。\x02\x03",

            "#03900F例えば人形兵器#8Rオーバーマペット#ですら\x01",
            "ここ以外の複数の工房の技術からも\x01",
            "成り立っている代物だ。\x02\x03",

            "言うならば、ここは無数にある\x01",
            "巨大な《蛇》の尻尾の一つ……\x02\x03",

            "#03903Fギルドや教会あたりが\x01",
            "簡単に乗り込んでこないのは\x01",
            "そういった理由もあるのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#00006F#5Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#00303F#5Pただ摘発するよりは\x01",
            "必要に応じて情報を引き出す……\x02\x03",

            "#00300Fその方が利用価値があるってか。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        (
            "#03903F#6Pそう、それに加えて\x01",
            "この工房にも“備え”がある。\x02\x03",

            "#03901Fもし、お前たちが逮捕令状を取って\x01",
            "ここに踏み込んできた場合……\x02\x03",

            "発見できるのはおそらく\x01",
            "がらんどうの工房だけだろう。\x02\x03",

            "その《パテル＝マテル》も含めてな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0031
    ChrTalk(
        0x9,
        (
            "#03903F#6Pフフ、何なら今この場で\x01",
            "わしの身柄を拘束してみるか？\x02\x03",

            "#03900Fまたとない機会かもしれんぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00006F#5P──いえ、遠慮しておきます。\x02\x03",

            "#00001F確かに貴方からは……\x01",
            "話を伺うだけの方がよさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#00108F#11P……ロイド……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x109,
        (
            "#10106Fち#11Pょ、ちょっと\x01",
            "納得はできませんけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "#03903F#6Pふふ、賢明だな。\x02\x03",

            "#03900Fどうやら具体的に色々と\x01",
            "聞きたいことがあるようだが……\x02\x03",

            "３つに絞るがいい。\x01",
            "答えられる内容ならば答えよう。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0036
    ChrTalk(
        0x101,
        (
            "#00003F#5P……分かりました。\x02\x03",

            "#00008F（この老人から聞きたい事、\x01",
            "  それは……）\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    SetCameraDistance(18000, 120000)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)

    label("loc_1842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B33")
    FadeToDark(300, 0, 100)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18E0")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【結社の《使徒》について】\x01",        # 0
            "【結社の『計画』について】\x01",        # 1
            "【結社と教団の関係について】\x01",      # 2
            "【質問をやめる】\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_1942")

    label("loc_18E0")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【結社の《使徒》について】\x01",        # 0
            "【結社の『計画』について】\x01",        # 1
            "【結社と教団の関係について】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)

    label("loc_1942")

    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_196E"),
        (0, "loc_1D0F"),
        (2, "loc_2698"),
        (3, "loc_2B26"),
        (SWITCH_DEFAULT, "loc_2B2E"),
    )


    label("loc_196E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C84")

    #C0037
    ChrTalk(
        0x9,
        (
            "#03903F#6P先ほども言ったように\x01",
            "わしも詳細は知らぬ。\x02\x03",

            "ただ、伝え聞く話によると\x01",
            "こんな風に呼ばれているらしい。\x02\x03",

            "#03901F──『幻焔#4Rげんえん#計画』と。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#00005F#5P『幻焔#4Rげんえん#計画』……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x105,
        "#10301F#11P……意味深な名前だね……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#00101F#11P……その計画は……\x01",
            "１年前のリベールのような異変を\x01",
            "クロスベルにもたらすものですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        (
            "#10107F#11Pも、もしそうなら……\x01",
            "絶対に認められません！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            "#03903F#6P繰り返すが、わしも詳細は知らぬ。\x02\x03",

            "#03900Fただ、一つ言えるとしたら\x01",
            "リベールほど《結社》の介入が\x01",
            "大規模ではないというくらいだ。\x02\x03",

            "そもそも《結社》は闇の存在……\x01",
            "本来あまり表舞台には出ぬからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        "#00101F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#00306F#5Pなんつーか、\x01",
            "全然安心できねぇんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#00211F#5Pむしろ名前だけというのが\x01",
            "逆に不安を煽っているような……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D0A")

    label("loc_1C84")


    #C0046
    ChrTalk(
        0x9,
        (
            "#03903F#6Pわしも概要は知らぬ。\x02\x03",

            "ただ、伝え聞く話によると\x01",
            "こんな風に呼ばれているらしい。\x02\x03",

            "#03901F──『幻焔#4Rげんえん#計画』と。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0A")

    Jump("loc_2B2E")

    label("loc_1D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2560")
    Sleep(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(280, 170, -1, -1)

    #A0047
    AnonymousTalk(
        0x9,
        (
            "#3C#30W《蛇の使徒#8Rア ン ギ ス#》──\x02\x03",

            "大いなる《盟主#4Rマスター#》の意を受け、\x01",
            "計画を実現する七人の幹部のことだ。\x02\x03",

            "わしも全員について\x01",
            "詳しく知っているわけではないが……\x02\x03",

            "近々、このクロスベルを訪れるという\x01",
            "使徒たちならば知らぬでもない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0048
    ChrTalk(
        0x101,
        (
            "#00013F#5Pそ、それは……\x01",
            "一体どういう人物ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "#03900F#6P……………………………………\x02\x03",

            "#03903F一人は《第六柱》にして\x01",
            "結社の技術ネットワークである\x01",
            "《十三工房》を統括する男だ。\x02\x03",

            "結社きっての理論家にして\x01",
            "貪欲きわまる技術者#6Rエンジニア#……\x02\x03",

            "#03901Fまあ、タチの悪い男だとだけ\x01",
            "言っておこう。\x02",
        )
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

    #C0050
    ChrTalk(
        0x103,
        "#00206F#5P……そんな風に言われましても。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x109,
        "#10101F#11Pど、どうタチが悪いんですか？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "#03903F#6P良くも悪くも、自分の知的好奇心を\x01",
            "満たすことしか考えていない男だ。\x02\x03",

            "どのような目的でこの地を\x01",
            "訪れるつもりなのかは知らぬが……\x02\x03",

            "#03901F少なくともクロスベルにとって\x01",
            "良い予兆とはとても言えぬだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        "#00108F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00006F#5P……確かに聞いた限り、\x01",
            "タチが悪そうではありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "#03903F#6P……そしてもう一人……\x02\x03",

            "#03900F《鋼#2Rはがね#》の名を冠する《第七柱》が\x01",
            "クロスベル入りするという情報がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0056
    ChrTalk(
        0x101,
        "#00005F#5P《鋼#2Rはがね#》……？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#00301F#5Pなんつーか……\x01",
            "ちょいとヤバそうな響きだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "#03903F#6Pフフ……少々謎めいた人物でな。\x02\x03",

            "#03900F一つ、言えるとしたら\x01",
            "お前たち全員が束になって挑んでも\x01",
            "敵わぬほどの達人というくらいか。\x02",
        )
    )

    CloseMessageWindow()
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0059
    ChrTalk(
        0x101,
        "#00011F#5P俺たち全員でも……！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x105,
        (
            "#10302F#11Pへえ……\x01",
            "ずいぶん自信満々だねぇ？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "#03903F#6Pまあ、忠告程度に思っておけ。\x02\x03",

            "《第六柱》と違い、\x01",
            "高潔な人物とは聞いているが……\x02\x03",

            "#03901F下手に挑んだりしたら\x01",
            "間違いなく返り討ちに遭うだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#00013F#5P………………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2693")

    label("loc_2560")


    #C0063
    ChrTalk(
        0x9,
        (
            "#03903F#6P詳細は知らぬが、クロスベルに\x01",
            "来ると言われる《使徒》は２人だ。\x02\x03",

            "#03900F一人は《第六柱》──\x01",
            "《十三工房》を統括している\x01",
            "タチの悪い技術者#6Rエンジニア#だ。\x02\x03",

            "そしても一人は《第七柱》──\x01",
            "《鋼#2Rはがね#》の名を冠する最強の使い手だ。\x02\x03",

            "#03903Fまあ、どちらもお前たちの\x01",
            "手に負える相手ではないだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2693")

    Jump("loc_2B2E")

    label("loc_2698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A23")

    #C0064
    ChrTalk(
        0x9,
        (
            "#03903F#6P《Ｄ∴Ｇ教団》か。\x02\x03",

            "#03901Fわしの知る限り、直接の繋がりが\x01",
            "あった事はないようだな。\x02\x03",

            "レンがいた連中の拠点#4Rロッジ#を\x01",
            "《結社》が潰した事実はあったが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0065
    ChrTalk(
        0x101,
        "#00011F#5Pええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        "#00101F#11Pそれって《楽園》っていう……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "#03900F#6Pうむ、各地の有力者を\x01",
            "取り込むための場所だったらしいな。\x02\x03",

            "大方、《結社》の息がかかった\x01",
            "有力者をターゲットにしたため、\x01",
            "殲滅の対象となったのだろう。\x02\x03",

            "#03903Fレンが生き延びたのは\x01",
            "僥倖#4Rぎょうこう#と言うより他にはないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        "#00208F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#00306F#5Pだからといって《結社》ってのが\x01",
            "マトモとはとても思えねぇがな……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x105,
        (
            "#10301F#11P正直、そんな説明だけじゃ\x01",
            "納得できそうもないんだけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "#03903F#6Pフフ、言っただろう。\x01",
            "わしの知る限りと。\x02\x03",

            "#03900Fどう判断するかはお前たち次第だ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B21")

    label("loc_2A23")


    #C0072
    ChrTalk(
        0x9,
        (
            "#03903F#6P《Ｄ∴Ｇ教団》──\x01",
            "わしの知る限り、《結社》と直接の\x01",
            "繋がりがあった事はないようだな。\x02\x03",

            "#03900Fレンがいた連中の拠点#4Rロッジ#を\x01",
            "《結社》が潰した事実はあったが……\x02\x03",

            "《結社》の息が掛かった\x01",
            "有力者に手を出されたため\x01",
            "殲滅の対象になったにすぎん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B21")

    Jump("loc_2B2E")

    label("loc_2B26")

    SetScenarioFlags(0x0, 3)
    Jump("loc_2B2E")

    label("loc_2B2E")

    Jump("loc_1842")

    label("loc_2B33")


    #C0073
    ChrTalk(
        0x9,
        (
            "#03900F#6Pふむ、これで３つか。\x02\x03",

            "#03903F──時間を取られた。\x01",
            "そろそろお引取り願おうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#00013F#5Pっ……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        "#00107F#11Pで、でも……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x109,
        "#10108F#11Pロ、ロイドさん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0077
    ChrTalk(
        0x101,
        (
            "#00006F#5P──そういう約束だ。\x01",
            "今回はこれで引き上げよう。\x02\x03",

            "#00000Fまた、機会があれば\x01",
            "話を伺いに来ても構いませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#03903F#6Pまあ、気が向けばな。\x02\x03",

            "#03901Fそもそも、お前たちにとって\x01",
            "気がかりは我々だけではあるまい。\x02\x03",

            "『国家独立』とやらを前にして、\x01",
            "警戒しなくてはならぬ勢力は\x01",
            "他に幾らでもあるのではないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#00011F#5Pそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        "#00303F#5P……ま、確かにな。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#10302F#11Pそういった勢力の動きも\x01",
            "全部知っていそうだけどね？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        "#03903F#6Pフフ、さてな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x8, 0x9, 500)
    OP_68(-6150, 700, -850, 1500)
    MoveCamera(25, 25, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(19000, 1500)
    Sound(957, 2, 40, 0)
    OP_95(0x8, -3750, 0, 4000, 2000, 0x0)
    StopSound(957, 300, 30)
    OP_6F(0x79)

    #C0083
    ChrTalk(
        0x9,
        (
            "#03900F#6P──さあ、帰りも\x01",
            "その子に付いて行くがいい。\x02\x03",

            "はぐれたりしたら\x01",
            "身の安全は保障できんぞ？\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x3BD)
    SetScenarioFlags(0x22, 0)
    NewScene("t3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1AA end

    def Function_3_2EC8(): pass

    label("Function_3_2EC8")

    OP_95(0xFE, 0, 0, 102000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    StopSound(957, 300, 30)
    Sleep(1000)
    Sound(957, 2, 40, 0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_3_2EC8 end

    def Function_4_2F07(): pass

    label("Function_4_2F07")

    Sound(957, 2, 40, 0)

    def lambda_2F12():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2F12)
    OP_95(0xFE, 0, 0, 5000, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    StopSound(957, 300, 30)
    Sleep(1000)
    Sound(957, 2, 40, 0)
    OP_95(0xFE, -2750, 0, 6300, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    StopSound(957, 300, 30)
    Return()

    # Function_4_2F07 end

    def Function_5_2F6A(): pass

    label("Function_5_2F6A")

    Sleep(1000)
    OP_95(0xFE, 500, 0, -4700, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -2000, 0, -4700, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -3450, 0, -500, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -7500, -250, -500, 2000, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_95(0xFE, -7500, -250, -3350, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_5_2F6A end

    def Function_6_2FF7(): pass

    label("Function_6_2FF7")

    OP_68(0, 600, 101000, 7000)
    SetCameraDistance(22000, 7000)
    OP_95(0xFE, 0, 0, 100000, 2000, 0x0)

    def lambda_302A():

        label("loc_302A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_302A")

    QueueWorkItem2(0xFE, 2, lambda_302A)
    Sleep(2000)
    EndChrThread(0xFE, 0x2)
    OP_68(-10000, 600, 102000, 8000)
    MoveCamera(40, 20, 0, 8000)
    OP_95(0xFE, -2000, 0, 102000, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_6_2FF7 end

    def Function_7_3083(): pass

    label("Function_7_3083")


    def lambda_3088():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3088)
    OP_95(0xFE, 0, 0, 2500, 2000, 0x0)

    label("loc_30A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30CC")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_30A8")

    label("loc_30CC")

    Return()

    # Function_7_3083 end

    def Function_8_30CD(): pass

    label("Function_8_30CD")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(100)
    OP_95(0xFE, -3450, 0, -500, 2000, 0x0)
    OP_95(0xFE, -6500, -250, -1500, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_8_30CD end

    def Function_9_3107(): pass

    label("Function_9_3107")

    OP_95(0xFE, 500, 0, 99500, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102500, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102500, 2000, 0x0)
    Return()

    # Function_9_3107 end

    def Function_10_3147(): pass

    label("Function_10_3147")


    def lambda_314C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_314C)
    OP_95(0xFE, 750, 0, 3500, 2000, 0x0)

    label("loc_316C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3190")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    Jump("loc_316C")

    label("loc_3190")

    Return()

    # Function_10_3147 end

    def Function_11_3191(): pass

    label("Function_11_3191")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(200)
    OP_95(0xFE, -3450, 0, -1000, 2000, 0x0)
    OP_95(0xFE, -5500, -250, -1150, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_11_3191 end

    def Function_12_31CB(): pass

    label("Function_12_31CB")

    OP_95(0xFE, -750, 0, 99000, 2000, 0x0)
    Sleep(2100)
    OP_95(0xFE, -2000, 0, 101250, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 101250, 2000, 0x0)
    Return()

    # Function_12_31CB end

    def Function_13_320B(): pass

    label("Function_13_320B")


    def lambda_3210():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3210)
    OP_95(0xFE, -1000, 0, 3000, 2000, 0x0)

    label("loc_3230")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3254")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_3230")

    label("loc_3254")

    Return()

    # Function_13_320B end

    def Function_14_3255(): pass

    label("Function_14_3255")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    OP_95(0xFE, -3450, 0, 500, 2000, 0x0)
    OP_95(0xFE, -6650, -250, -300, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_14_3255 end

    def Function_15_328F(): pass

    label("Function_15_328F")

    OP_95(0xFE, 0, 0, 98000, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102000, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_15_328F end

    def Function_16_32CF(): pass

    label("Function_16_32CF")


    def lambda_32D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_32D4)
    OP_95(0xFE, -250, 0, 4000, 2000, 0x0)

    label("loc_32F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3318")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    Jump("loc_32F4")

    label("loc_3318")

    Return()

    # Function_16_32CF end

    def Function_17_3319(): pass

    label("Function_17_3319")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(400)
    OP_95(0xFE, -3450, 0, -500, 2000, 0x0)
    OP_95(0xFE, -5450, -250, 300, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_17_3319 end

    def Function_18_3353(): pass

    label("Function_18_3353")

    OP_95(0xFE, 750, 0, 97250, 2000, 0x0)
    Sleep(2100)
    OP_95(0xFE, -2000, 0, 102250, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102250, 2000, 0x0)
    Return()

    # Function_18_3353 end

    def Function_19_3393(): pass

    label("Function_19_3393")


    def lambda_3398():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3398)
    OP_95(0xFE, 500, 0, 5500, 2000, 0x0)

    label("loc_33B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33DC")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_33B8")

    label("loc_33DC")

    Return()

    # Function_19_3393 end

    def Function_20_33DD(): pass

    label("Function_20_33DD")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    OP_95(0xFE, -3450, 0, -1000, 2000, 0x0)
    OP_95(0xFE, -4250, 0, -850, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_20_33DD end

    def Function_21_3417(): pass

    label("Function_21_3417")

    OP_95(0xFE, 1250, 0, 98500, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102750, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102750, 2000, 0x0)
    Return()

    # Function_21_3417 end

    def Function_22_3457(): pass

    label("Function_22_3457")


    def lambda_345C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_345C)
    OP_95(0xFE, -1000, 0, 4500, 2000, 0x0)

    label("loc_347C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34A0")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(1500)
    Jump("loc_347C")

    label("loc_34A0")

    Return()

    # Function_22_3457 end

    def Function_23_34A1(): pass

    label("Function_23_34A1")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(1000)
    OP_95(0xFE, -3450, 0, 500, 2000, 0x0)
    OP_95(0xFE, -4300, 0, 500, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_23_34A1 end

    def Function_24_34DB(): pass

    label("Function_24_34DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06600.itc", 0x1E)
    LoadChrToIndex("chr/ch47400.itc", 0x1F)
    LoadEffect(0x0, "event/ev622_00.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03900.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01200.itp")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1F)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    OP_74(0x1, 0xF)
    OP_70(0x1, 0x65)
    SetChrPos(0xA, 8730, -2400, 0, 270)
    OP_D5(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFrame(0x1, "pm_body:Layer1(5)", 0x0, 0x1)
    SetMapObjFrame(0x1, "pm_head:Layer1(4)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_body:Layer3(7)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_body:Layer3(8)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_backpack:Layer1(9)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_arm:Layer1(20)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_arm:Layer1(29)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_giar:Layer1(38)", 0x1, 0x1)
    SetMapObjFrame(0x1, "pm_giar:Layer1(39)", 0x1, 0x1)
    SetMapObjFrame(0x1, "Null_chest_ball(71)", 0x1, 0x1)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    SetChrPos(0x9, 6100, 500, -50, 270)
    SetChrPos(0x8, -2750, 0, 6300, 180)
    SetChrPos(0x101, 3300, 0, -50, 90)
    SetChrPos(0x107, 2750, 0, 900, 90)
    SetChrPos(0x103, 1750, 0, 300, 90)
    SetChrPos(0x105, 3500, 0, -1750, 45)
    SetChrPos(0x106, 2750, 0, -1000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x107, 0x5)
    OP_68(4740, 1400, -130, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    MoveCamera(55, 20, 0, 3000)
    SetCameraDistance(20000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0084
    AnonymousTalk(
        0x9,
        (
            "──ふむ。\x01",
            "珍しい客人もあったものだ。\x02\x03",

            "久しいな、神狼よ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0085
    AnonymousTalk(
        0x107,
        (
            "#3Cそうだな、人の子よ。\x02\x03",

            "さすがのおぬしも\x01",
            "随分と老けたようだ。\x02\x03",

            "相変わらず《蛇》どもに\x01",
            "関わっているようだが。\x02",
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

    #C0086
    ChrTalk(
        0x9,
        (
            "#03903F#11Pフフ、しがらみというのは\x01",
            "俗世でなくとも付きまとうもの。\x02\x03",

            "#03900Fおぬしを縛っていた《盟約》とて\x01",
            "同じようなものであろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x107,
        "#01201F#6P#3Cハハ、違いない。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0088
    ChrTalk(
        0x103,
        (
            "#00211F#6P（なんだかとんでもなく\x01",
            "  遠い話をしてるような……）\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00006F#6P（ああ、同じ世界の\x01",
            "  会話とは思えないな……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    #C0090
    ChrTalk(
        0x9,
        (
            "#03903F#5Pしかし星杯の守護騎士に、\x01",
            "ここに侵入しようとしていた\x01",
            "東方人街の魔人か……\x02\x03",

            "#03900Fなかなか個性的な顔触れが\x01",
            "集まっているではないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x105,
        "#10402F#12Pフフ、確かに。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x106,
        "#10710F#6P……その節は失礼しました。\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    #C0093
    ChrTalk(
        0x101,
        (
            "#00006F#6P──ヨルグ・マイスター。\x02\x03",

            "#00001Fお話した通り、俺たちは今、\x01",
            "この状況を何とかするために\x01",
            "動いている最中です。\x02\x03",

            "特に《結社》の動きについて……\x01",
            "何かご存知ではないでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(150)

    #C0094
    ChrTalk(
        0x9,
        (
            "#03900F#11Pふむ……\x02\x03",

            "#03903F──既に知っているかもしれんが\x01",
            "《結社》は今回、クロイス家の目的に\x01",
            "協力しているだけの立場にすぎん。\x02\x03",

            "《結社》の計画──『幻焔#4Rげんえん#計画』は\x01",
            "既に次の舞台へ移行しているようだ。\x02\x03",

            "#03901Fすなわちエレボニア帝国にな。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#00011F#6Pえ……！？\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x105,
        (
            "#10406F#12P実際、他の使徒や執行者が\x01",
            "そちらの方で動き始めていてね。\x02\x03",

            "#10401F騎士団#6Rボ ク ら#がクロスベルに\x01",
            "そこまで戦力を割けないのも\x01",
            "その辺りが理由だったりするのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#00008F#6Pそうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        (
            "#00206F#6P……大陸全土で色々なことが\x01",
            "起こりすぎているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "#03903F#11Pだが、非常に厄介な三名が\x01",
            "未だクロスベルに残っている。\x02\x03",

            "#03901Fそれも結社の中でも\x01",
            "指折りの実力者たちだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#00003F#6P《道化師》カンパネルラ……\x02\x03",

            "#00013Fそして《使徒》と呼ばれる\x01",
            "ノバルティスという博士と\x01",
            "アリアンロードという女性ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x106,
        (
            "#10708F#6P………………………………\x02\x03",

            "#10706Fあの女性は一体、何者ですか？\x02\x03",

            "#10701Fあの動きと反応──\x01",
            "とても人の業#2Rわざ#とは思えません。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "#03903F#11Pわしも詳しくは知らぬ。\x02\x03",

            "ただ、凄まじい槍技を使い、\x01",
            "仁義にも篤#2Rあつ#い人物として\x01",
            "《結社》では知られている。\x02\x03",

            "#03900F付き従う戦乙女たちは皆、\x01",
            "彼女が何処#4Rいずこ#からか見出した上で\x01",
            "稽古を付けているらしくてな。\x02\x03",

            "一人一人が《執行者》に\x01",
            "迫るほどの実力を持つらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x103,
        "#00205F#6Pあのレンさんと同じくらい……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x105,
        (
            "#10403F#12Pまあ、《執行者》の能力は\x01",
            "戦闘だけじゃないみたいだけど……\x02\x03",

            "#10408Fそれにしても計６人も\x01",
            "厄介な相手が協力してるわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00005F#6P……でも、\x01",
            "協力しているだけという事は。\x02\x03",

            "#00001F場合によったら、\x01",
            "クロスベルの今後の状況には\x01",
            "深入りしない可能性が？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "#03900F#11Pふむ、そうかもしれぬな。\x02\x03",

            "#03903Fもっともノバルティスの若造は\x01",
            "《至宝》の力を受けた人形どもに\x01",
            "興味津々なようだ。\x02\x03",

            "#03901Fいずれにせよ、わしの情報では\x01",
            "彼らの今後の予定は分からぬ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        "#00006F#6Pそうですか……\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x103,
        (
            "#00206F#6Pなかなか一筋縄では\x01",
            "行かなさそうですね。\x02\x03",

            "#00200F……ところで、先ほどから\x01",
            "少し気になっているんですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6200, 1200, -50, 2000)
    MoveCamera(90, 10, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(20600, 2000)
    OP_6F(0x79)
    Sleep(300)

    #C0109
    ChrTalk(
        0x103,
        (
            "#00200F#6P《パテル＝マテル》を\x01",
            "修理している最中なんですか？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(859, 0, 70, 0)
    OP_87(0x0, 0xFF, 0x1, "pm_head:Layer1(4)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(500)
    Sound(903, 0, 100, 0)
    Sleep(1500)

    #C0110
    ChrTalk(
        0x101,
        "#00011F#6Pわっ……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x106,
        "#10712F#12Pしゃ、喋った……？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "#03903F#5Pまあ、ちょっとした\x01",
            "メンテナンスのようなものだ。\x02\x03",

            "ノバルティスの若造は\x01",
            "この機体に随分執心#4Rしゅうしん#していた。\x02\x03",

            "#03901F今は新しい人形に夢中なようだから\x01",
            "心配ないとは思うが……\x02\x03",

            "もし奪いに来たら逃がせるよう\x01",
            "備えだけはしておこうと思ってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        "#00001F#6Pな、なるほど。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x105,
        (
            "#10404F#12Pいざという時は《殲滅天使》がいる\x01",
            "リベールまで行かせるわけか。\x02\x03",

            "#10400Fしかし聞いてる限りだと\x01",
            "あの博士と随分仲が悪そうだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "#03903F#5Pフン、否定はせん。\x02\x03",

            "元々この《ゴルディアス級》は\x01",
            "わしの全てを掛けて開発したものだ。\x02\x03",

            "#03900Fそれを途中で奪い去り、\x01",
            "非道な接続試験までした挙句に\x01",
            "レンのような幼子に宛#2Rあて#がったこと……\x02\x03",

            "何とか接続が成功したとはいえ、\x01",
            "その試み自体は許されざる所業だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#00008F#6P確かに……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        (
            "#00206F#6P……教団のした実験と\x01",
            "大差ないかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "#03903F#5Pおまけに、至宝なしでは\x01",
            "満足に稼動することも出来ぬ\x01",
            "後継機どもを勝手に開発して……\x02\x03",

            "それを《ゴルディアス級》の\x01",
            "“最終型”などと臆面もなく言う\x01",
            "厚かましさ……！\x02\x03",

            "#03901Fこの場にいたら、あの細首を\x01",
            "締め上げてくれるところだ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        "#00012F#6Pそ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x107,
        (
            "#01203F#6P#3Cまあ、落ち着け。\x02\x03",

            "#01200F相変わらず作品の事になると\x01",
            "冷静ではいられないようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "#03903F#5Pコホン……\x01",
            "まあ、それはともかく。\x02\x03",

            "#03900Fいかに厚顔無恥とはいえ、\x01",
            "応用・強化する技術にかけては\x01",
            "天才的な頭脳を持つのは確かだ。\x02\x03",

            "わしが開発した人形兵器も\x01",
            "あやつに改造・強化された上で\x01",
            "量産されていると聞いている。\x02\x03",

            "噂では、それらの機体が\x01",
            "《塔》や《僧院》などにも\x01",
            "配備されているらしいぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_END)), "loc_4B66")

    #C0122
    ChrTalk(
        0x105,
        "#10401F#12Pあの塔の前にいたヤツか……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#00006F#6P……確かにやたらと\x01",
            "強そうな人形だったけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BAD")

    label("loc_4B66")


    #C0124
    ChrTalk(
        0x101,
        "#00001F#6Pそうなんですか……\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x105,
        "#10403F#12P……それは初耳だな。\x02",
    )

    CloseMessageWindow()

    label("loc_4BAD")


    #C0126
    ChrTalk(
        0x103,
        (
            "#00208F#6Pしかし、それらの場所に\x01",
            "配備されているという事は……\x02\x03",

            "#00201Fやはり例の《大鐘》を\x01",
            "守っているのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "#03903F#5Pその可能性は高いだろう。\x02\x03",

            "#03900Fあのアーティファクトらしき\x01",
            "《大鐘》については\x01",
            "わしも個人的に調べていてな。\x02\x03",

            "何か分かったらお前たちにも\x01",
            "教えてやってもよい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0128
    ChrTalk(
        0x101,
        "#00011F#6Pほ、本当ですか！？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x105,
        (
            "#10402F#12Pへえ……？\x01",
            "さすがに気前が良すぎない？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "#03903F#5Pフン……此度#4R こ たび#の顛末については\x01",
            "わしも少々頭に来ているからな。\x02\x03",

            "#03901Fノバルティスの若造もそうだが……\x02\x03",

            "わしが協力していた《劇団#4Rアルカンシェル#》を\x01",
            "無茶苦茶にされた事もある。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x106,
        "#10708F#12Pあ……\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x103,
        (
            "#00206F#6Pそういえば……\x01",
            "舞台装置や自動人形#8Rオ ー ト マ タ#も\x01",
            "全て破壊されたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "#03903F#5Pうむ、全て作り直しだろう。\x02\x03",

            "#03901Fその意味で、《赤い星座》とやらも\x01",
            "それを雇ったクロイス家の当主も\x01",
            "個人的には許しがたい。\x02\x03",

            "#03903F娘の方は、わしの人形の\x01",
            "熱心な蒐集家#6Rコレクター#のようだが……\x01",
            "それとこれとは話は別だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x105,
        "#10404F#12Pフフ、なるほどね。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#00003F#6P……分かりました。\x01",
            "正直、とても助かります。\x02\x03",

            "#00000F《大鐘》について何か分かったら\x01",
            "是非、ご連絡をいただけると。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21600, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_34DB end

    SaveToFile()

Try(main)
