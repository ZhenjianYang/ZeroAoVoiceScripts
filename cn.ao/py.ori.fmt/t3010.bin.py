from ScenarioHelper import *

def main():
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
        "领路人偶",               # 1
        "约鲁古老人",             # 2
        "帕蒂尔·玛蒂尔",         # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(332, 0)                                        # 0

    ScpFunction((
        "Function_0_14C",          # 00, 0
        "Function_1_17A",          # 01, 1
        "Function_2_1AA",          # 02, 2
        "Function_3_2A0D",         # 03, 3
        "Function_4_2A4C",         # 04, 4
        "Function_5_2AAF",         # 05, 5
        "Function_6_2B3C",         # 06, 6
        "Function_7_2BC8",         # 07, 7
        "Function_8_2C12",         # 08, 8
        "Function_9_2C4C",         # 09, 9
        "Function_10_2C8C",        # 0A, 10
        "Function_11_2CD6",        # 0B, 11
        "Function_12_2D10",        # 0C, 12
        "Function_13_2D50",        # 0D, 13
        "Function_14_2D9A",        # 0E, 14
        "Function_15_2DD4",        # 0F, 15
        "Function_16_2E14",        # 10, 16
        "Function_17_2E5E",        # 11, 17
        "Function_18_2E98",        # 12, 18
        "Function_19_2ED8",        # 13, 19
        "Function_20_2F22",        # 14, 20
        "Function_21_2F5C",        # 15, 21
        "Function_22_2F9C",        # 16, 22
        "Function_23_2FE6",        # 17, 23
        "Function_24_3020",        # 18, 24
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
            "就这样，罗伊德等人\x01",
            "在自动领路人偶的引领之下……\x02\x03",

            "经由构造如迷宫般复杂的通路，\x01",
            "来到了地下工房的一角。\x07\x00\x02",
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

    def lambda_657():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_657)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)

    def lambda_66C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_66C)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x109, 0x1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)

    #C0002
    ChrTalk(
        0x101,
        "#00013F#5P这、这里是……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        "#00205F#5P……好惊人……\x02",
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

    def lambda_744():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_744)
    Sleep(50)

    def lambda_754():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_754)
    Sleep(50)

    def lambda_764():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_764)
    Sleep(50)

    def lambda_774():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_774)
    Sleep(50)

    def lambda_784():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_784)
    Sleep(50)

    def lambda_794():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_794)
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
        "#10111F#6P#4S那是……！？\x02",
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
            "#10301F#6P#N莫非……\x01",
            "是你们说过的那个巨大智能兵器吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00006F#6P#N嗯……\x01",
            "是那个名叫玲的女孩\x01",
            "所操控的『帕蒂尔·玛蒂尔』……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0007
    ChrTalk(
        0x102,
        "#00108F#6P#N原来存放在这里啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0008
    ChrTalk(
        0x104,
        (
            "#00306F#6P#N话说回来，没想到这座建筑\x01",
            "的地下竟然存在这种地方……\x02",
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
            "#00208F#11P还有看上去像是\x01",
            "导力网络终端的设备……\x02\x03",

            "#00201F……难道『小猫』当时就是在这里\x01",
            "以无线的方式接入导力网络的……？\x02",
        )
    )

    CloseMessageWindow()

    #N0010
    NpcTalk(
        0x9,
        "老人的声音",
        "你们有什么事情？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A91():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A91)
    Sleep(50)

    def lambda_AA1():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AA1)
    Sleep(50)

    def lambda_AB1():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AB1)
    Sleep(50)

    def lambda_AC1():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AC1)
    Sleep(50)

    def lambda_AD1():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AD1)
    Sleep(50)

    def lambda_AE1():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AE1)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_BD5")

    #C0011
    ChrTalk(
        0x101,
        (
            "#00003F#5P那个……\x01",
            "感谢您花费宝贵的时间\x01",
            "接待我们。\x02\x03",

            "#00001F我们有几件事情\x01",
            "想请教您。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C72")

    label("loc_BD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C2D")

    #C0012
    ChrTalk(
        0x101,
        (
            "#00003F#5P那个……\x01",
            "好久不见了。\x02\x03",

            "#00001F我们有几件事情\x01",
            "想请教您。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C72")

    label("loc_C2D")


    #C0013
    ChrTalk(
        0x101,
        (
            "#00006F#5P那个……\x01",
            "初次见面。\x02\x03",

            "#00001F我们有几件事情\x01",
            "想请教您。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C72")


    #C0014
    ChrTalk(
        0x9,
        (
            "#03903F#12P哼……\x02\x03",

            "#03900F多半是肯帕雷拉\x01",
            "又做了些多余的事情吧？\x02",
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
        "#00301F#5P老爷爷，您……\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x1E, 0x1F4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E1B")

    #C0017
    ChrTalk(
        0x9,
        (
            "#03903F#6P不要搞错。\x02\x03",

            "#03900F虽然我的确是『结社』的成员，\x01",
            "但终究只是一介人偶师而已。\x02\x03",

            "与『结社』的计划\x01",
            "并无直接关系。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAD")

    label("loc_E1B")


    #C0018
    ChrTalk(
        0x9,
        (
            "#03903F#6P不要搞错。\x02\x03",

            "#03900F正如玲对你们说的一样，\x01",
            "虽然我的确是『结社』的成员，\x01",
            "但终究只是一介人偶师而已。\x02\x03",

            "与『结社』的计划\x01",
            "并无直接关系。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EAD")


    #C0019
    ChrTalk(
        0x101,
        (
            "#00006F#5P那、那就是说……\x02\x03",

            "#00001F您并不知道\x01",
            "那个名叫肯帕雷拉\x01",
            "的少年打算做些什么……？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            "#03900F#6P不知道，也没有知道的理由。\x02\x03",

            "#03903F只有一点可以确定……\x01",
            "他不是『使徒』，而是『执行者』。\x02\x03",

            "并无权力提案『结社』\x01",
            "将要进行的『计划』。\x02\x03",

            "#03901F制订计划的工作\x01",
            "终究还是要由『使徒』来负责。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        "#00101F#11P请、请稍等一下……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x109,
        (
            "#10106F#11P您、您说得太快了，\x01",
            "我们一时无法理解……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x105,
        (
            "#10305F#11P听起来似乎是很重要的内部情报，\x01",
            "如此轻易地透露给我们，没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        (
            "#03903F#6P呵呵……\x01",
            "并没有人要求我保密啊。\x02\x03",

            "#03900F而且，像这种程度的情报，\x01",
            "了解的人并不在少数。\x02\x03",

            "教会、协会，还有大国的谍报机关\x01",
            "应该在很早之前就掌握了。\x02",
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
            "#00201F#5P尽管如此，您却能一直\x01",
            "在这里制作人偶……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "#03903F#6P我原本就没有\x01",
            "了解『结社』全貌的资格。\x02\x03",

            "#03900F就算是智能兵器，\x01",
            "也完全可以利用除此处之外的\x01",
            "多处工房的技术来制造。\x02\x03",

            "简要来说，这里只是巨大之『蛇』\x01",
            "的无数尾巴之一……\x02\x03",

            "#03903F游击士协会与教会等组织\x01",
            "之所以不会轻易侵犯这里，\x01",
            "也有这方面的因素在内。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#00006F#5P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#00303F#5P与其揭发取缔，不如\x01",
            "根据具体需要而从中探查情报……\x02\x03",

            "#00300F这样才更有利用价值啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        (
            "#03903F#6P不错，而且这所工房\x01",
            "还拥有『防备手段』。\x02\x03",

            "#03901F如果你们带着逮捕令\x01",
            "闯入这里……\x02\x03",

            "也只能看到一座\x01",
            "空荡荡的工房而已。\x02\x03",

            "『帕蒂尔·玛蒂尔』自然也不会还留在这里。\x02",
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
            "#03903F#6P呵呵，不然干脆试试\x01",
            "将我当场抓捕如何？\x02\x03",

            "#03900F以后恐怕再也没有这么好的机会了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00006F#5P不，还是不必了。\x02\x03",

            "#00001F我看……老老实实地向您\x01",
            "打听些消息才是最好的选择。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#00108F#11P……罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x109,
        (
            "#10106F#11P虽、虽然有些\x01",
            "无法接受，不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "#03903F#6P呵呵，很明智的决定。\x02\x03",

            "#03900F看样子，你们似乎有\x01",
            "不少问题想问……\x02\x03",

            "不过尽量归结为三个问题吧。\x01",
            "只要是我能回答的，我就会回答你们。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0036
    ChrTalk(
        0x101,
        (
            "#00003F#5P……明白了。\x02\x03",

            "#00008F（想询问这位老人\x01",
            "  什么问题呢……）\x02",
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

    label("loc_1624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D4")
    FadeToDark(300, 0, 100)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16A6")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【结社的『使徒』】\x01",        # 0
            "【结社的『计划』】\x01",        # 1
            "【结社与教团的关系】\x01",      # 2
            "【结束询问】\x01",              # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_16F0")

    label("loc_16A6")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【结社的『使徒』】\x01",        # 0
            "【结社的『计划』】\x01",        # 1
            "【结社与教团的关系】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)

    label("loc_16F0")

    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_171C"),
        (0, "loc_1A4B"),
        (2, "loc_22C7"),
        (3, "loc_26C7"),
        (SWITCH_DEFAULT, "loc_26CF"),
    )


    label("loc_171C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19DE")

    #C0037
    ChrTalk(
        0x9,
        (
            "#03903F#6P正如刚才所说，\x01",
            "我也不了解详情。\x02\x03",

            "不过，据我所闻，\x01",
            "他们是这样命名此项计划的。\x02\x03",

            "#03901F──『幻焰计划』。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#00005F#5P『幻焰计划』……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x105,
        "#10301F#11P……真是个意味深长的名字呢……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        (
            "#00101F#11P……那项计划……\x01",
            "也会给克洛斯贝尔带来\x01",
            "利贝尔一年半前遭遇的那种异变吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        (
            "#10107F#11P如、如果真是如此……\x01",
            "我绝对不能饶恕！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            "#03903F#6P再说一遍，我也不了解详情。\x02\x03",

            "#03900F不过有一件事情倒是可以确定，\x01",
            "那就是『结社』此次的介入规模\x01",
            "并不像利贝尔那次那样庞大。\x02\x03",

            "『结社』原本就处于黑暗之中……\x01",
            "一般情况下是不会现身于人前的。\x02",
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
            "#00306F#5P怎么说呢，\x01",
            "完全不能让人放心啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#00211F#5P不如说，只知道了名字\x01",
            "反而更让人感到不安啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A46")

    label("loc_19DE")


    #C0046
    ChrTalk(
        0x9,
        (
            "#03903F#6P我也不了解详情。\x02\x03",

            "不过，据我所闻，\x01",
            "他们是这样命名此项计划的。\x02\x03",

            "#03901F──『幻焰计划』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A46")

    Jump("loc_26CF")

    label("loc_1A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C3")
    Sleep(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(280, 170, -1, -1)

    #A0047
    AnonymousTalk(
        0x9,
        (
            "#3C#30W『蛇之使徒』──\x02\x03",

            "是遵照伟大『盟主』的授意，\x01",
            "将计划实现的七名干部。\x02\x03",

            "我并不了解\x01",
            "所有使徒的详细信息……\x02\x03",

            "不过，说起最近来访克洛斯贝尔的\x01",
            "两名使徒，倒也算是了解一二。\x02",
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
            "#00013F#5P那、那么……\x01",
            "他们究竟是怎样的人物呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "#03900F#6P……………………………………\x02\x03",

            "#03903F其中一人是『第六柱』，\x01",
            "统管着结社技术网络\x01",
            "『十三工房』的男人。\x02\x03",

            "他是结社中首屈一指的理论家，\x01",
            "极度贪婪的技术者。\x02\x03",

            "#03901F简单来说，\x01",
            "就是个品格低劣的男人。\x02",
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
        "#00206F#5P……光是这样说也无法了解啊。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x109,
        "#10101F#11P到、到底是怎样的品格低劣呢？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "#03903F#6P他是个不顾善恶，一心只为\x01",
            "满足自己的求知欲与好奇心的男人。\x02\x03",

            "虽然我并不知道他来访此地\x01",
            "究竟有何目的……\x02\x03",

            "#03901F但至少可以确定，他的到来\x01",
            "对克洛斯贝尔而言绝不是什么好兆头。\x02",
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
            "#00006F#5P……听您所说，\x01",
            "的确是个品格低劣的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "#03903F#6P……至于另外一人……\x02\x03",

            "#03900F根据我收到的情报，被冠以『钢』\x01",
            "之名的『第七柱』也来到克洛斯贝尔了。\x02",
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
        "#00005F#5P『钢』……？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#00301F#5P这……\x01",
            "听起来似乎是个很危险的家伙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "#03903F#6P呵呵……是个充满谜团的人物。\x02\x03",

            "#03900F唯一确定的是，\x01",
            "那是一位你们即使全员联手\x01",
            "也无法匹敌的达人。\x02",
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
        "#00011F#5P我们全员联手也……！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x105,
        (
            "#10302F#11P嘿……\x01",
            "真是自信满满啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "#03903F#6P总之，你们就把这些话当作我的忠告吧。\x02\x03",

            "与『第六柱』不同，据说『第七柱』\x01",
            "是一位性情高洁的人物……\x02\x03",

            "#03901F但你们要是莽撞挑战，\x01",
            "肯定会反遭击溃。\x02",
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
    Jump("loc_22C2")

    label("loc_21C3")


    #C0063
    ChrTalk(
        0x9,
        (
            "#03903F#6P我并不了解详情，不过据说来到\x01",
            "克洛斯贝尔的『使徒』共有两人。\x02\x03",

            "#03900F其中一人是『第六柱』──\x01",
            "统管着『十三工房』，\x01",
            "品格低劣的技术者。\x02\x03",

            "另一人则是『第七柱』──\x01",
            "被冠以『钢』之名的最强达人。\x02\x03",

            "#03903F总之，这两人恐怕都不是\x01",
            "你们可以应付的对手。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C2")

    Jump("loc_26CF")

    label("loc_22C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F2")

    #C0064
    ChrTalk(
        0x9,
        (
            "#03903F#6P『Ｄ∴Ｇ教团』吗？\x02\x03",

            "#03901F据我所知，结社与其\x01",
            "并无直接联系。\x02\x03",

            "不过，他们曾经囚禁玲的据点\x01",
            "当年正是被『结社』所击溃的……\x02",
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
        "#00011F#5P哎哎……！？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        "#00101F#11P就是那个名为『乐园』的……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "#03900F#6P嗯，据说那是用于\x01",
            "笼络各地权势人物的场所。\x02\x03",

            "多半是因为对与『结社』密切相关\x01",
            "的权势人物图谋不轨，\x01",
            "才会成为歼灭对象吧。\x02\x03",

            "#03903F玲能因此而存活下来，\x01",
            "实属侥幸啊。\x02",
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
            "#00306F#5P就算『结社』偶尔做了件好事，\x01",
            "我也不认为那是个正派的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x105,
        (
            "#10301F#11P老实说，只有这种程度的说明，\x01",
            "实在是让人难以接受啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "#03903F#6P呵呵，我不是说过吗，\x01",
            "我只能回答我了解的内容。\x02\x03",

            "#03900F至于如何判断，就要看你们自己了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26C2")

    label("loc_25F2")


    #C0072
    ChrTalk(
        0x9,
        (
            "#03903F#6P『Ｄ∴Ｇ教团』──\x01",
            "据我所知，结社与其\x01",
            "并无直接联系。\x02\x03",

            "#03900F不过，他们曾经囚禁玲的据点\x01",
            "当年正是被『结社』所击溃的……\x02\x03",

            "大概是因为对与『结社』密切相关\x01",
            "的权势人物图谋不轨，\x01",
            "才会成为歼灭对象吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26C2")

    Jump("loc_26CF")

    label("loc_26C7")

    SetScenarioFlags(0x0, 3)
    Jump("loc_26CF")

    label("loc_26CF")

    Jump("loc_1624")

    label("loc_26D4")


    #C0073
    ChrTalk(
        0x9,
        (
            "#03900F#6P嗯，三个问题回答完毕。\x02\x03",

            "#03903F已经耗去了不少时间，\x01",
            "请各位就此离开吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#00013F#5P……！\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        "#00107F#11P可、可是……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x109,
        "#10108F#11P罗、罗伊德警官……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0077
    ChrTalk(
        0x101,
        (
            "#00006F#5P我们毕竟有约在先，\x01",
            "这次就到此为止吧。\x02\x03",

            "#00000F如果今后有机会，\x01",
            "还可以再来向您咨询吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#03903F#6P嗯，如果我心情好的话。\x02\x03",

            "#03901F反正令你们担心的\x01",
            "也并非只有我们结社。\x02\x03",

            "在『独立』问题面前，\x01",
            "必须要全力警戒的势力\x01",
            "恐怕还有很多个吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#00011F#5P这……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        "#00303F#5P……确实如此。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#10302F#11P言下之意，那些势力的动向\x01",
            "似乎也全在您的掌握之中？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        "#03903F#6P呵呵，随你怎么想。\x02",
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
            "#03900F#6P好了，回去的路上\x01",
            "也跟着那孩子走吧。\x02\x03",

            "如果跟丢了，\x01",
            "我可无法保证你们的人身安全。\x02",
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

    def Function_3_2A0D(): pass

    label("Function_3_2A0D")

    OP_95(0xFE, 0, 0, 102000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    StopSound(957, 300, 30)
    Sleep(1000)
    Sound(957, 2, 40, 0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_3_2A0D end

    def Function_4_2A4C(): pass

    label("Function_4_2A4C")

    Sound(957, 2, 40, 0)

    def lambda_2A57():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2A57)
    OP_95(0xFE, 0, 0, 5000, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    StopSound(957, 300, 30)
    Sleep(1000)
    Sound(957, 2, 40, 0)
    OP_95(0xFE, -2750, 0, 6300, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    StopSound(957, 300, 30)
    Return()

    # Function_4_2A4C end

    def Function_5_2AAF(): pass

    label("Function_5_2AAF")

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

    # Function_5_2AAF end

    def Function_6_2B3C(): pass

    label("Function_6_2B3C")

    OP_68(0, 600, 101000, 7000)
    SetCameraDistance(22000, 7000)
    OP_95(0xFE, 0, 0, 100000, 2000, 0x0)

    def lambda_2B6F():

        label("loc_2B6F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_2B6F")

    QueueWorkItem2(0xFE, 2, lambda_2B6F)
    Sleep(2000)
    EndChrThread(0xFE, 0x2)
    OP_68(-10000, 600, 102000, 8000)
    MoveCamera(40, 20, 0, 8000)
    OP_95(0xFE, -2000, 0, 102000, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_6_2B3C end

    def Function_7_2BC8(): pass

    label("Function_7_2BC8")


    def lambda_2BCD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2BCD)
    OP_95(0xFE, 0, 0, 2500, 2000, 0x0)

    label("loc_2BED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C11")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_2BED")

    label("loc_2C11")

    Return()

    # Function_7_2BC8 end

    def Function_8_2C12(): pass

    label("Function_8_2C12")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(100)
    OP_95(0xFE, -3450, 0, -500, 2000, 0x0)
    OP_95(0xFE, -6500, -250, -1500, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_8_2C12 end

    def Function_9_2C4C(): pass

    label("Function_9_2C4C")

    OP_95(0xFE, 500, 0, 99500, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102500, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102500, 2000, 0x0)
    Return()

    # Function_9_2C4C end

    def Function_10_2C8C(): pass

    label("Function_10_2C8C")


    def lambda_2C91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2C91)
    OP_95(0xFE, 750, 0, 3500, 2000, 0x0)

    label("loc_2CB1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CD5")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    Jump("loc_2CB1")

    label("loc_2CD5")

    Return()

    # Function_10_2C8C end

    def Function_11_2CD6(): pass

    label("Function_11_2CD6")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(200)
    OP_95(0xFE, -3450, 0, -1000, 2000, 0x0)
    OP_95(0xFE, -5500, -250, -1150, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_11_2CD6 end

    def Function_12_2D10(): pass

    label("Function_12_2D10")

    OP_95(0xFE, -750, 0, 99000, 2000, 0x0)
    Sleep(2100)
    OP_95(0xFE, -2000, 0, 101250, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 101250, 2000, 0x0)
    Return()

    # Function_12_2D10 end

    def Function_13_2D50(): pass

    label("Function_13_2D50")


    def lambda_2D55():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2D55)
    OP_95(0xFE, -1000, 0, 3000, 2000, 0x0)

    label("loc_2D75")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D99")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_2D75")

    label("loc_2D99")

    Return()

    # Function_13_2D50 end

    def Function_14_2D9A(): pass

    label("Function_14_2D9A")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    OP_95(0xFE, -3450, 0, 500, 2000, 0x0)
    OP_95(0xFE, -6650, -250, -300, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_14_2D9A end

    def Function_15_2DD4(): pass

    label("Function_15_2DD4")

    OP_95(0xFE, 0, 0, 98000, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102000, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102000, 2000, 0x0)
    Return()

    # Function_15_2DD4 end

    def Function_16_2E14(): pass

    label("Function_16_2E14")


    def lambda_2E19():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2E19)
    OP_95(0xFE, -250, 0, 4000, 2000, 0x0)

    label("loc_2E39")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E5D")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1500)
    Jump("loc_2E39")

    label("loc_2E5D")

    Return()

    # Function_16_2E14 end

    def Function_17_2E5E(): pass

    label("Function_17_2E5E")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(400)
    OP_95(0xFE, -3450, 0, -500, 2000, 0x0)
    OP_95(0xFE, -5450, -250, 300, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_17_2E5E end

    def Function_18_2E98(): pass

    label("Function_18_2E98")

    OP_95(0xFE, 750, 0, 97250, 2000, 0x0)
    Sleep(2100)
    OP_95(0xFE, -2000, 0, 102250, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102250, 2000, 0x0)
    Return()

    # Function_18_2E98 end

    def Function_19_2ED8(): pass

    label("Function_19_2ED8")


    def lambda_2EDD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2EDD)
    OP_95(0xFE, 500, 0, 5500, 2000, 0x0)

    label("loc_2EFD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F21")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1500)
    Jump("loc_2EFD")

    label("loc_2F21")

    Return()

    # Function_19_2ED8 end

    def Function_20_2F22(): pass

    label("Function_20_2F22")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    OP_95(0xFE, -3450, 0, -1000, 2000, 0x0)
    OP_95(0xFE, -4250, 0, -850, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_20_2F22 end

    def Function_21_2F5C(): pass

    label("Function_21_2F5C")

    OP_95(0xFE, 1250, 0, 98500, 2000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2000, 0, 102750, 2000, 0x0)
    OP_95(0xFE, -21450, 0, 102750, 2000, 0x0)
    Return()

    # Function_21_2F5C end

    def Function_22_2F9C(): pass

    label("Function_22_2F9C")


    def lambda_2FA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2FA1)
    OP_95(0xFE, -1000, 0, 4500, 2000, 0x0)

    label("loc_2FC1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FE5")
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(1500)
    Jump("loc_2FC1")

    label("loc_2FE5")

    Return()

    # Function_22_2F9C end

    def Function_23_2FE6(): pass

    label("Function_23_2FE6")

    TurnDirection(0xFE, 0x9, 500)
    Sleep(1000)
    OP_95(0xFE, -3450, 0, 500, 2000, 0x0)
    OP_95(0xFE, -4300, 0, 500, 2000, 0x0)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_23_2FE6 end

    def Function_24_3020(): pass

    label("Function_24_3020")

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
            "嗯，\x01",
            "有稀客来访啊。\x02\x03",

            "好久不见了，神狼。\x02",
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
            "#3C是啊，人类之子。\x02\x03",

            "连你都已经\x01",
            "这么老了啊。\x02\x03",

            "看来你还在和『蛇』的\x01",
            "那些家伙牵扯不断。\x02",
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
            "#03903F#11P呵呵，情面这种东西，\x01",
            "就算远离世俗也难以摆脱啊。\x02\x03",

            "#03900F束缚着你的『盟约』\x01",
            "不也和这类似吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x107,
        "#01201F#6P#3C哈哈，说的没错。\x02",
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
            "#00211F#6P（他们讨论的话题\x01",
            "  似乎离我们很遥远啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00006F#6P（嗯，感觉不是\x01",
            "  同一个世界的对话……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    #C0090
    ChrTalk(
        0x9,
        (
            "#03903F#5P话说回来，\x01",
            "星杯骑士与曾经试图侵入此地的\x01",
            "东方人街的魔人也来了啊……\x02\x03",

            "#03900F真是汇集了不少\x01",
            "奇妙的面孔呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x105,
        "#10402F#12P呵呵，确实。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x106,
        "#10710F#6P……关于当时那件事，真是失礼了。\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    #C0093
    ChrTalk(
        0x101,
        (
            "#00006F#6P约鲁古大师。\x02\x03",

            "#00001F正如刚才所说，\x01",
            "我们正在设法\x01",
            "打破现在这种局面。\x02\x03",

            "您了解什么情况吗？\x01",
            "特别是有关『结社』动向方面的信息……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(150)

    #C0094
    ChrTalk(
        0x9,
        (
            "#03900F#11P唔……\x02\x03",

            "#03903F你们或许已经知道了，\x01",
            "『结社』此次的立场仅仅是\x01",
            "协助库罗伊斯家族达成目的而已。\x02\x03",

            "至于『结社』的计划──『幻焰计划』，\x01",
            "似乎已经转移到下一个舞台了。\x02\x03",

            "#03901F也就是埃雷波尼亚帝国。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#00011F#6P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x105,
        (
            "#10406F#12P其他使徒与执行者\x01",
            "已经开始在那边行动了。\x02\x03",

            "#10401F我们骑士团在克洛斯贝尔\x01",
            "只留下了这么少的战力，\x01",
            "似乎也是因为那个原因。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#00008F#6P是吗……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        (
            "#00206F#6P……看来他们在整个大陆\x01",
            "引发着各种麻烦的事件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "#03903F#11P虽然主要舞台已经转移，\x01",
            "但仍有三名非常棘手的人留在克洛斯贝尔。\x02\x03",

            "#03901F他们均是在结社中也\x01",
            "分量十足的强大人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#00003F#6P『小丑』肯帕雷拉……\x02\x03",

            "#00013F以及被称为『使徒』\x01",
            "的诺华提斯博士\x01",
            "与名为阿瑞安赫德的女性。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x106,
        (
            "#10708F#6P………………………………\x02\x03",

            "#10706F那位女性究竟是什么人？\x02\x03",

            "#10701F她的动作与反应……\x01",
            "怎么看都不像是人类可以拥有的。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "#03903F#11P我也不清楚她的详细身份。\x02\x03",

            "不过，整个『结社』都知道\x01",
            "她是一位充满仁义之心，\x01",
            "拥有惊人枪技的人物。\x02\x03",

            "#03900F而陪伴在她身边的那三名女战士\x01",
            "都是她从各地选拔，\x01",
            "并亲自训练的。\x02\x03",

            "据说每人都有着\x01",
            "接近『执行者』的实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x103,
        "#00205F#6P和玲相当的实力吗……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x105,
        (
            "#10403F#12P『执行者』的能力应该\x01",
            "并不是只有战斗……\x02\x03",

            "#10408F话虽如此，共有六名\x01",
            "棘手的敌人在协助总统他们吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00005F#6P……不过，\x01",
            "如果只是『正在协助』而已的话……\x02\x03",

            "#00001F根据具体情况的变化，\x01",
            "他们今后也未必就会继续深入\x01",
            "过问克洛斯贝尔的状况吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "#03900F#11P嗯，也许吧。\x02\x03",

            "#03903F诺华提斯那小子\x01",
            "所感兴趣的，只是那些\x01",
            "容纳了『至宝』之力的智能兵器而已。\x02\x03",

            "#03901F不管怎么说，凭我现在掌握到的情报，\x01",
            "无法预测他们今后的行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        "#00006F#6P是吗……\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x103,
        (
            "#00206F#6P看来事情\x01",
            "没那么容易解决呢。\x02\x03",

            "#00200F……说起来，我从刚才开始\x01",
            "就很想问了。\x02",
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
            "#00200F#6P您正在修理\x01",
            "『帕蒂尔·玛蒂尔』吗？\x02",
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
        "#00011F#6P哇……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x106,
        "#10712F#12P说、说话了……？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "#03903F#5P嗯，稍微做了一些\x01",
            "维护而已。\x02\x03",

            "诺华提斯那小子一直\x01",
            "都对这台机体非常执著。\x02\x03",

            "#03901F他现在还沉迷于新机体之中，\x01",
            "暂时不必担心……\x02\x03",

            "但为防止他今后前来夺取，仍然要做好准备，\x01",
            "以保证『帕蒂尔·玛蒂尔』随时能够逃脱。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        "#00001F#6P原、原来如此。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x105,
        (
            "#10404F#12P是打算在情况紧急时，让它逃往\x01",
            "『歼灭天使』所在的利贝尔吗……\x02\x03",

            "#10400F看来您与那位博士\x01",
            "之间的关系非常恶劣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "#03903F#5P哼，我不否认。\x02\x03",

            "这台『极限级』的智能兵器\x01",
            "本是我全力开发出来的。\x02\x03",

            "#03900F但那家伙却半途插手，将它夺去，\x01",
            "并挑选了很多像玲那样的幼童，\x01",
            "进行各种不人道的接续实验……\x02\x03",

            "虽然最后总算是接续成功了，\x01",
            "但那种实验本身就是不可宽恕的罪孽。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#00008F#6P的确……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        (
            "#00206F#6P……与教团的所作所为\x01",
            "并没有多少差别呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "#03903F#5P而且他竟然还擅自开发\x01",
            "那种没有至宝的支持\x01",
            "就无法正常运转的后续机体……\x02\x03",

            "并恬不知耻地将其称为『极限级』\x01",
            "智能兵器的『最终型』，\x01",
            "脸皮真是厚到了极点……！\x02\x03",

            "#03901F要是那家伙敢出现在我的面前，\x01",
            "我一定会掐紧他那根细脖子……！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        "#00012F#6P是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x107,
        (
            "#01203F#6P#3C好了，先冷静一下。\x02\x03",

            "#01200F你还是老样子啊，只要一提到\x01",
            "作品的事情就控制不住情绪。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "#03903F#5P咳咳……\x01",
            "当然，抛开这一点不谈。\x02\x03",

            "#03900F那家伙虽然厚颜无耻，\x01",
            "但在应用以及强化技术方面\x01",
            "确实拥有天才般的头脑。\x02\x03",

            "听说我开发的智能兵器\x01",
            "经过他的改造和强化之后，\x01",
            "已经正式投入量产了。\x02\x03",

            "据说，『塔』和\x01",
            "『僧院』中都配备着\x01",
            "那些机体。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_END)), "loc_444B")

    #C0122
    ChrTalk(
        0x105,
        "#10401F#12P阻挡在塔前的那种东西吗……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#00006F#6P……看起来的确像是\x01",
            "很强的智能兵器呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_448A")

    label("loc_444B")


    #C0124
    ChrTalk(
        0x101,
        "#00001F#6P是吗……\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x105,
        "#10403F#12P……这还是第一次听说。\x02",
    )

    CloseMessageWindow()

    label("loc_448A")


    #C0126
    ChrTalk(
        0x103,
        (
            "#00208F#6P话说回来，既然将它们\x01",
            "配备在那种场所，也就是说……\x02\x03",

            "#00201F目的是看守\x01",
            "『大钟』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "#03903F#5P这种可能性很高。\x02\x03",

            "#03900F那些『大钟』\x01",
            "似乎是古代遗物，\x01",
            "我个人也正在调查。\x02\x03",

            "如果今后有了什么发现，\x01",
            "也会告诉你们的。\x02",
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
        "#00011F#6P真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x105,
        (
            "#10402F#12P嘿……？\x01",
            "这未免也太慷慨了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "#03903F#5P哼……他们这次的行动\x01",
            "实在是有点惹火我了。\x02\x03",

            "#03901F诺华提斯那小子自不必提……\x02\x03",

            "竟然还把我经常协助的\x01",
            "『彩虹剧团』搞得一片狼籍。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x106,
        "#10708F#12P啊……\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x103,
        (
            "#00206F#6P说起来……\x01",
            "舞台装置和自动人偶\x01",
            "好像也都被破坏了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "#03903F#5P嗯，全都要重做了。\x02\x03",

            "#03901F由于此事，我绝对无法原谅\x01",
            "『赤色星座』的那些家伙，\x01",
            "还有雇佣他们的库罗伊斯家族的当家。\x02\x03",

            "#03903F虽然他女儿很喜欢我做的人偶，\x01",
            "是个非常热心的收藏家……\x01",
            "但两件事可不能混为一谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x105,
        "#10404F#12P呵呵，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#00003F#6P……明白了，\x01",
            "您真是帮了我们的大忙。\x02\x03",

            "#00000F如果对『大钟』的调查取得了什么进展，\x01",
            "请您一定和我们联络。\x02",
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

    # Function_24_3020 end

    SaveToFile()

Try(main)
