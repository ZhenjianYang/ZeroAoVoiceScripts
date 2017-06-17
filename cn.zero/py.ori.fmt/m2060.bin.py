from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m2060.bin",                # FileName
        "M2060",                    # MapName
        "M2060",                    # Location
        0x0079,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 121, 0, 0, 0, 1],
    )

    BuildStringList((
        "m2060",                  # 0
        "SE控制",                 # 1
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 2,   16.799999237060547,    0.0,                   6.75,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.599999904632568,    -0.0,                  -1.350000023841858,    1.0])

    ScpFunction((
        "Function_0_134",          # 00, 0
        "Function_1_135",          # 01, 1
        "Function_2_1CE",          # 02, 2
        "Function_3_A7B",          # 03, 3
        "Function_4_AA2",          # 04, 4
        "Function_5_AC7",          # 05, 5
        "Function_6_AE8",          # 06, 6
        "Function_7_B08",          # 07, 7
        "Function_8_B32",          # 08, 8
    ))


    def Function_0_134(): pass

    label("Function_0_134")

    Return()

    # Function_0_134 end

    def Function_1_135(): pass

    label("Function_1_135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_147")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_147")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_15F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_1A6")
    StopEffect(0x80, 0x0)
    StopEffect(0x81, 0x0)
    StopEffect(0x82, 0x0)
    SetMapObjFrame(0xFF, "model07_cloudanime", 0x2, "off")
    SetMapObjFrame(0x0, "root", 0x2, "off")
    SetMapObjFrame(0x0, "model02", 0x0, 0x1)

    label("loc_1A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB")
    Sound(936, 1, 100, 0)
    Jump("loc_1CD")

    label("loc_1BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_1CD")
    OP_24(0x3A8)
    Sound(132, 1, 70, 0)

    label("loc_1CD")

    Return()

    # Function_1_135 end

    def Function_2_1CE(): pass

    label("Function_2_1CE")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00001.itc", 0x1E)
    LoadChrToIndex("chr/ch00301.itc", 0x1F)
    LoadChrToIndex("chr/ch00801.itc", 0x20)
    SoundLoad(132)
    SoundLoad(930)
    OP_68(19800, 9550, 0, 0)
    MoveCamera(90, 6, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20270, 0)
    FadeToBright(1000, 0)
    OP_68(21850, 9550, 0, 3000)
    SetChrPos(0x101, 18960, 7750, 100, 90)
    SetChrPos(0x109, 18120, 7750, 1600, 90)
    SetChrPos(0x103, 17720, 7750, -1450, 90)
    SetChrPos(0x102, 16670, 7750, 800, 90)
    SetChrPos(0x104, 16110, 7750, -510, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_6F(0x1)
    OP_0D()
    VolumeBGM(0x3C, 0x3E8)

    #C0001
    ChrTalk(
        0x101,
        "#0005F#6P#N这声音是……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0002
    ChrTalk(
        0x102,
        "#0105F#6P#N钟在共鸣……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0003
    ChrTalk(
        0x103,
        (
            "#0205F#12P#N……难道……\x02\x03",

            "#0201F或许这个共鸣声就是\x01",
            "制造出『力场』的源头。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_381():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_381)
    Sleep(50)

    def lambda_391():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_391)
    Sleep(50)

    def lambda_3A1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A1)
    Sleep(50)

    def lambda_3B1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3B1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0004
    ChrTalk(
        0x101,
        "#0013F#5P什么……？\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        "#0101F#5P怎、怎么回事？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x109, 500)

    #C0006
    ChrTalk(
        0x103,
        (
            "#0203F#12P#N我也不知道详细原理……\x02\x03",

            "#0208F不过能感觉得到，\x01",
            "以钟为中心，产生了某种『力场』，\x01",
            "把整个遗迹都笼罩了起来。\x02\x03",

            "#0201F所以，只要能停止钟的共鸣，\x01",
            "也许就……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0007
    ChrTalk(
        0x104,
        (
            "#0301F#5P……或许就能\x01",
            "抑制住某些『现象』吧……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0008
    ChrTalk(
        0x101,
        (
            "#0001F#11P怎么办，上士？\x02\x03",

            "要尝试停止钟声的共鸣吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    def lambda_530():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_530)
    Sleep(50)

    def lambda_540():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_540)
    Sleep(50)

    def lambda_550():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_550)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x109)

    #C0009
    ChrTalk(
        0x109,
        (
            "#0503F#6P……嗯，试试看吧。\x02\x03",

            "#0501F罗伊德警官、兰迪前辈，\x01",
            "请来帮个忙。\x02\x03",

            "我们同时把钟压住。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#0000F#11P没问题。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        "#0300F#11P明白。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    BeginChrThread(0x8, 0, 0, 5)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x1)
    SetChrPos(0x101, 21840, 7750, 2140, 180)
    SetChrPos(0x104, 21920, 7750, -1930, 0)
    SetChrPos(0x109, 20010, 7750, 30, 90)
    SetChrPos(0x102, 17770, 7750, -2330, 45)
    SetChrPos(0x103, 19210, 7750, -3260, 45)
    OP_82(0x64, 0x64, 0x3E8, 0x1770)
    BeginChrThread(0x8, 1, 0, 7)
    BeginChrThread(0x101, 3, 0, 3)
    BeginChrThread(0x104, 3, 0, 3)
    BeginChrThread(0x109, 3, 0, 3)
    OP_68(22400, 9450, 80, 0)
    MoveCamera(108, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21090, 0)
    MoveCamera(75, 14, 0, 6000)
    OP_6F(0x40)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    Fade(1000)
    BeginChrThread(0x102, 3, 0, 4)
    OP_68(22400, 10250, 80, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(11970, 0)
    SetCameraDistance(18800, 5000)
    OP_6F(0x10)

    #C0012
    ChrTalk(
        0x102,
        "#0105F啊……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    StopBGM(0xFA0)
    Sound(937, 0, 100, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    SetCameraDistance(39080, 1000)
    FadeToDark(1000, 16777215, -1)
    BeginChrThread(0x8, 1, 0, 8)
    Sleep(1000)
    BeginChrThread(0x8, 0, 0, 6)
    OP_6F(0x1)
    CancelBlur(100)
    OP_0D()
    EndChrThread(0x102, 0x3)
    Sleep(2000)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    PlayBGM("ed7304", 0)
    Sound(132, 2, 70, 0)
    FadeToBright(2000, 16777215)
    StopEffect(0x80, 0x0)
    StopEffect(0x81, 0x0)
    StopEffect(0x82, 0x0)
    SetMapObjFrame(0xFF, "model07_cloudanime", 0x2, "off")
    SetMapObjFrame(0x0, "root", 0x2, "off")
    SetMapObjFrame(0x0, "model02", 0x0, 0x1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_68(22400, 11650, 80, 0)
    MoveCamera(67, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(37180, 0)
    OP_68(22400, 9150, 80, 6000)
    OP_6F(0x1)
    OP_0D()
    EndChrThread(0x8, 0x0)
    Fade(1000)
    OP_68(25000, 9550, 590, 0)
    MoveCamera(83, 4, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(24140, 0)
    SetCameraDistance(23140, 2000)
    SetChrPos(0x101, 21840, 7750, 2140, 315)
    SetChrPos(0x104, 21920, 7750, -2140, 135)
    SetChrPos(0x109, 19960, 7750, -200, 225)
    SetChrPos(0x102, 17660, 7750, -2450, 45)
    SetChrPos(0x103, 18870, 7750, -3570, 45)
    OP_6F(0x79)

    #C0013
    ChrTalk(
        0x102,
        "#0102F#11P雾、雾气消失了……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0014
    ChrTalk(
        0x104,
        (
            "#0302F#6P哦哦……\x01",
            "天空恢复晴朗了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0015
    ChrTalk(
        0x103,
        (
            "#0204F#12P#N笼罩着整个遗迹的\x01",
            "某种『力场』似乎也消失了。\x02\x03",

            "#0202F难道说，内部也……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_994():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_994)
    Sleep(50)

    def lambda_9A4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A4)
    Sleep(50)

    def lambda_9B4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9B4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0016
    ChrTalk(
        0x101,
        (
            "#0004F#5P发生了某种变化吗……\x02\x03",

            "#0000F好──\x01",
            "返回内部，确认一下吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0017
    ChrTalk(
        0x109,
        "#0502F#11P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetCameraDistance(23410, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 17720, 7750, 260, 283)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_37()
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xC0, 6)
    OP_29(0x49, 0x1, 0x4)
    OP_24(0x3A2)
    OP_24(0x3A8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_2_1CE end

    def Function_3_A7B(): pass

    label("Function_3_A7B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA1")
    OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(500)
    Jump("Function_3_A7B")

    label("loc_AA1")

    Return()

    # Function_3_A7B end

    def Function_4_AA2(): pass

    label("Function_4_AA2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC6")
    OP_82(0x64, 0x64, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_4_AA2")

    label("loc_AC6")

    Return()

    # Function_4_AA2 end

    def Function_5_AC7(): pass

    label("Function_5_AC7")

    OP_25(0x3A8, 0x5A)
    Sleep(500)
    OP_25(0x3A8, 0x50)
    Sleep(500)
    OP_25(0x3A8, 0x46)
    Sleep(500)
    OP_25(0x3A8, 0x3C)
    Sleep(500)
    OP_25(0x3A8, 0x32)
    Return()

    # Function_5_AC7 end

    def Function_6_AE8(): pass

    label("Function_6_AE8")

    OP_25(0x3A8, 0x28)
    Sleep(800)
    OP_25(0x3A8, 0x1E)
    Sleep(800)
    OP_25(0x3A8, 0x14)
    Sleep(800)
    OP_25(0x3A8, 0xA)
    Sleep(800)
    OP_24(0x3A8)
    Return()

    # Function_6_AE8 end

    def Function_7_B08(): pass

    label("Function_7_B08")

    Sound(930, 2, 0, 0)
    Sleep(500)
    OP_25(0x3A2, 0xA)
    Sleep(500)
    OP_25(0x3A2, 0x14)
    Sleep(500)
    OP_25(0x3A2, 0x1E)
    Sleep(500)
    OP_25(0x3A2, 0x28)
    Sleep(4000)
    OP_25(0x3A2, 0x32)
    Return()

    # Function_7_B08 end

    def Function_8_B32(): pass

    label("Function_8_B32")

    OP_25(0x3A2, 0x28)
    Sleep(200)
    OP_25(0x3A2, 0x1E)
    Sleep(200)
    OP_25(0x3A2, 0x14)
    Sleep(200)
    OP_25(0x3A2, 0xA)
    Sleep(200)
    OP_24(0x3A2)
    Return()

    # Function_8_B32 end

    SaveToFile()

Try(main)
