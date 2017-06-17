from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t140b.bin",                # FileName
        "t140b",                    # MapName
        "t140b",                    # Location
        0x00BB,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 187, 0, 0, 0, 1],
    )

    BuildStringList((
        "t140b",                  # 0
        "琪雅",                   # 1
    ))

    AddCharChip((
        "chr/ch13600.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 2,   0.0,                   -75.0,                 2.0,                   225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  25.0,                  -0.4000000059604645,   1.0])

    ChipFrameInfo(404, 0)                                        # 0

    ScpFunction((
        "Function_0_194",          # 00, 0
        "Function_1_195",          # 01, 1
        "Function_2_1B4",          # 02, 2
    ))


    def Function_0_194(): pass

    label("Function_0_194")

    Return()

    # Function_0_194 end

    def Function_1_195(): pass

    label("Function_1_195")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AD")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1AD")

    Sound(126, 1, 50, 0)
    Return()

    # Function_1_195 end

    def Function_2_1B4(): pass

    label("Function_2_1B4")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SoundLoad(852)
    SoundLoad(3616)
    SoundLoad(3617)
    SoundLoad(3618)
    SoundLoad(4109)
    SoundLoad(3330)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 0, 5000, -68000, 0)
    OP_90(0x102, -800, 5000, -69000, 0)
    OP_90(0x103, 900, 5000, -68800, 0)
    OP_90(0x104, 200, 5000, -70000, 0)
    OP_90(0x109, -1000, 5000, -71000, 0)
    OP_90(0x105, 1100, 5000, -71000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, 0, 5000, -45000, 0)
    SetChrFlags(0x8, 0x4)
    PlayEffect(0x0, 0x0, 0x8, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopBGM(0xFA0)
    FadeToBright(1000, 0)
    OP_68(0, 4500, -57000, 0)
    OP_68(0, 3000, -57000, 3000)
    MoveCamera(0, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)

    def lambda_323():
        OP_9B(0x0, 0x101, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_323)
    Sleep(50)

    def lambda_33B():
        OP_9B(0x0, 0x102, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_33B)
    Sleep(50)

    def lambda_353():
        OP_9B(0x0, 0x103, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_353)
    Sleep(50)

    def lambda_36B():
        OP_9B(0x0, 0x104, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_36B)
    Sleep(50)

    def lambda_383():
        OP_9B(0x0, 0x109, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_383)
    Sleep(50)

    def lambda_39B():
        OP_9B(0x0, 0x105, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_39B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()

    #C0001
    ChrTalk(
        0x101,
        "#00002F#6P（……在这里……！）\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        "#00106F#6P（太、太好了……！）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    Sound(852, 2, 60, 0)
    Fade(1000)
    OP_68(0, 1000, -45000, 0)
    MoveCamera(180, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(14000, 4000)
    OP_6F(0x79)
    OP_25(0x354, 0x28)
    Fade(1000)
    OP_68(0, 32000, -7500, 0)
    MoveCamera(0, -39, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(48400, 0)
    SetCameraDistance(47900, 3000)
    OP_6F(0x79)
    SetCameraDistance(46900, 20000)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0003
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#05815F#3616V#60W#12P#N…………为什么……………\x02\x03",

            "#3617V#60W……为…………什么……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE21)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(1, 180, -1, -1)

    #A0004
    AnonymousTalk(
        0x101,
        "#00007F#4S琪雅#3330V……！\x02",
    )

    CloseMessageWindow()
    OP_24(0xD02)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_25(0x354, 0x3C)
    Fade(500)
    OP_90(0x101, -100, 5000, -58300, 0)
    OP_90(0x102, -1500, 5000, -57500, 0)
    OP_90(0x103, 1500, 5000, -57800, 0)
    OP_90(0x104, 200, 5000, -60100, 0)
    OP_90(0x109, -1000, 5000, -59800, 0)
    OP_90(0x105, 1200, 5000, -59900, 0)
    OP_68(0, 1100, -45000, 0)
    OP_68(0, 1100, -48800, 3500)
    MoveCamera(180, 22, 0, 0)
    MoveCamera(180, 12, 0, 3500)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)

    def lambda_621():
        OP_9B(0x0, 0x101, 0x0, 0x2CEC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_621)
    Sleep(50)

    def lambda_639():
        OP_9B(0x0, 0x102, 0x0, 0x2CEC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_639)
    Sleep(50)

    def lambda_651():
        OP_9B(0x0, 0x103, 0x0, 0x2CEC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_651)
    Sleep(50)

    def lambda_669():
        OP_9B(0x0, 0x104, 0x0, 0x2CEC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_669)
    Sleep(50)

    def lambda_681():
        OP_9B(0x0, 0x109, 0x0, 0x2CEC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_681)
    Sleep(50)

    def lambda_699():
        OP_9B(0x0, 0x105, 0x0, 0x2CEC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_699)
    WaitChrThread(0x102, 0)

    def lambda_6B2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B2)
    WaitChrThread(0x103, 0)

    def lambda_6C3():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C3)
    OP_6F(0x79)

    #C0005
    ChrTalk(
        0x101,
        "#00013F#5P琪雅！没事吧！？\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        (
            "#00101F#11P太好了……\x01",
            "你没受伤吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#05815F#40W#5P…………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    Fade(500)
    StopSound(852, 700, 60)
    StopEffect(0x0, 0x0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_63(0x8, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_C9(0x0, 0x80000000)

    #C0008
    ChrTalk(
        0x8,
        (
            "#05805F#3618V#6P#30W哎……？\x02\x03",

            "#05810F#4109V罗伊德，你们怎么了？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x100D)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0009
    ChrTalk(
        0x101,
        (
            "#00006F#5P唉……\x02\x03",

            "#00011F你……你还问我们怎么了……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#00206F#5P琪雅，你为什么要跑到这里？\x02\x03",

            "#00200F你是从罗伊德前辈他们\x01",
            "的房间中走来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "#05805F#6P#30W？？？\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x8, 0x13B, 0x1F4)
    Sleep(400)
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(400)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0012
    ChrTalk(
        0x8,
        (
            "#05811F#6P#30W这里是白天那座城堡……？\x02\x03",

            "#05805F琪雅为什么会在这里？\x02",
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

    #C0013
    ChrTalk(
        0x105,
        (
            "#10306F#5P哎呀呀……\x01",
            "看来她完全不记得了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x109,
        (
            "#10108F#11P难、难道是梦游\x01",
            "走到这里的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#00306F#5P不，梦游到这种程度，\x01",
            "未免也太过夸张了……\x02\x03",

            "#00301F阿琪，你什么都不记得了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#05803F#6P#30W嗯……\x02\x03",

            "#05808F……在梦里，好像有个\x01",
            "声音在呼唤琪雅……\x02\x03",

            "#05805F…………哎？\x01",
            "是那个声音把琪雅叫来的吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        "#00303F#5P唔……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        (
            "#00109F#11P呵呵……\x01",
            "梦这种东西，真是让人没办法啊。\x02\x03",

            "#00102F不管怎么说，你没事就好……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00004F#5P是啊……\x02\x03",

            "#00002F好，我们这就\x01",
            "回酒店吧。\x02\x03",

            "琪雅，回房间以后，\x01",
            "可要乖乖睡觉哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x32, 0x0, 0x7D0, 0xC8)
    #Sound(3659, 255, 80, 0)    #voice#KeA

    #C0020
    ChrTalk(
        0x8,
        "#05809F#6P嗯。\x02",
    )

    CloseMessageWindow()
    OP_24(0xE4B)
    StopSound(126, 2000, 50)
    FadeToDark(1500, 0, -1)
    SetCameraDistance(15750, 1500)
    OP_6F(0x79)
    OP_0D()
    WaitBGM()
    Sleep(500)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人返回酒店，\x01",
            "将琪雅哄睡之后，\x01",
            "联络了米修拉姆的保安部门……\x02\x03",

            "向保安人员说明了事情经过之后，众人再次\x01",
            "前往现场，但之前的异常现象却已全部消失了。\x02\x03",

            "拂晓时分，大家才返回酒店安睡，\x01",
            "一直休息到临近中午……\x02\x03",

            "之后，罗伊德等人与前来迎接大家的\x01",
            "玛丽亚贝尔一起离开了米修拉姆。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ReplaceBGM(-1, -1)
    OP_24(0x354)
    SetScenarioFlags(0x22, 1)
    NewScene("e3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1B4 end

    SaveToFile()

Try(main)
