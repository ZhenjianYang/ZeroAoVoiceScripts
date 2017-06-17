from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0490.bin",                # FileName
        "c0490",                    # MapName
        "c0490",                    # Location
        0x0036,                     # MapIndex
        "ed7151",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 54, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0490",                  # 0
        "西格蒙德",               # 1
        "谢莉",                   # 2
        "猎兵加雷斯",             # 3
        "经理",                   # 4
        "餐具",                   # 5
        "餐具",                   # 6
        "餐具",                   # 7
        "餐具",                   # 8
        "餐具",                   # 9
        "克莱德",                 # 10
        "玛格丽特夫人",           # 11
        "皮埃尔副局长",           # 12
        "猎兵扎克斯",             # 13
        "店员",                   # 14
        "店员",                   # 15
        "女公关",                 # 16
        "女公关",                 # 17
        "客人",                   # 18
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(712, 0)                                        # 0

    ScpFunction((
        "Function_0_2C8",          # 00, 0
        "Function_1_378",          # 01, 1
        "Function_2_3A2",          # 02, 2
        "Function_3_3D2",          # 03, 3
        "Function_4_409",          # 04, 4
        "Function_5_440",          # 05, 5
        "Function_6_470",          # 06, 6
        "Function_7_4A0",          # 07, 7
        "Function_8_4D0",          # 08, 8
        "Function_9_558",          # 09, 9
        "Function_10_577",         # 0A, 10
        "Function_11_5EF",         # 0B, 11
        "Function_12_2958",        # 0C, 12
        "Function_13_4CCF",        # 0D, 13
        "Function_14_4CF3",        # 0E, 14
    ))


    def Function_0_2C8(): pass

    label("Function_0_2C8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_300"),
        (1, "loc_30C"),
        (2, "loc_318"),
        (3, "loc_324"),
        (4, "loc_330"),
        (5, "loc_33C"),
        (6, "loc_348"),
        (SWITCH_DEFAULT, "loc_354"),
    )


    label("loc_300")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_30C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_318")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_324")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_330")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_33C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_348")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_354")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_360")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_377")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_377")

    Return()

    # Function_0_2C8 end

    def Function_1_378(): pass

    label("Function_1_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_38F")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 11)
    Jump("loc_3A1")

    label("loc_38F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3A1")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 12)

    label("loc_3A1")

    Return()

    # Function_1_378 end

    def Function_2_3A2(): pass

    label("Function_2_3A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3BC")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x162), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    Jump("loc_3D1")

    label("loc_3BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_3D1")

    Return()

    # Function_2_3A2 end

    def Function_3_3D2(): pass

    label("Function_3_3D2")


    def lambda_3D7():
        OP_95(0xFE, 99300, 0, -2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D7)

    def lambda_3F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_3_3D2 end

    def Function_4_409(): pass

    label("Function_4_409")


    def lambda_40E():
        OP_95(0xFE, 100700, 0, -2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40E)

    def lambda_428():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_428)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_4_409 end

    def Function_5_440(): pass

    label("Function_5_440")


    def lambda_445():
        OP_95(0xFE, 101000, 0, -6100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_445)

    def lambda_45F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_45F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_5_440 end

    def Function_6_470(): pass

    label("Function_6_470")


    def lambda_475():
        OP_95(0xFE, 100000, 0, -5700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_475)

    def lambda_48F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_470 end

    def Function_7_4A0(): pass

    label("Function_7_4A0")


    def lambda_4A5():
        OP_95(0xFE, 99000, 0, -6100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A5)

    def lambda_4BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_7_4A0 end

    def Function_8_4D0(): pass

    label("Function_8_4D0")

    OP_92(0x9, 0x186A0, 0x14B4, 0x1F4)

    def lambda_4E2():
        OP_95(0xFE, 100000, 0, 5300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4E2)
    WaitChrThread(0x9, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)

    def lambda_51B():
        OP_95(0xFE, 100000, 0, 7300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_51B)

    def lambda_535():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_535)
    WaitChrThread(0x9, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Return()

    # Function_8_4D0 end

    def Function_9_558(): pass

    label("Function_9_558")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_576")
    SetChrSubChip(0x9, 0x0)
    Sleep(250)
    SetChrSubChip(0x9, 0x1)
    Sleep(250)
    Jump("Function_9_558")

    label("loc_576")

    Return()

    # Function_9_558 end

    def Function_10_577(): pass

    label("Function_10_577")

    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x20)
    SetChrPos(0x9, 900, 0, 25200, 180)
    OP_0D()

    def lambda_5B0():
        OP_95(0xFE, 2500, 0, 25200, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5B0)
    WaitChrThread(0x9, 1)

    def lambda_5CE():
        OP_95(0xFE, 2500, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5CE)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0x13B, 0x1F4)
    Return()

    # Function_10_577 end

    def Function_11_5EF(): pass

    label("Function_11_5EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    LoadChrToIndex("chr/ch42900.itc", 0x1F)
    LoadChrToIndex("chr/ch03300.itc", 0x20)
    LoadChrToIndex("chr/ch00002.itc", 0x22)
    LoadChrToIndex("chr/ch00302.itc", 0x23)
    LoadChrToIndex("chr/ch03002.itc", 0x24)
    LoadChrToIndex("apl/ch51201.itc", 0x25)
    LoadChrToIndex("apl/ch51202.itc", 0x26)
    LoadChrToIndex("apl/ch51203.itc", 0x27)
    LoadChrToIndex("apl/ch51204.itc", 0x28)
    LoadChrToIndex("chr/ch25800.itc", 0x29)
    LoadChrToIndex("apl/ch50091.itc", 0x2A)
    LoadChrToIndex("apl/ch50092.itc", 0x2B)
    SoundLoad(3835)
    SoundLoad(3836)
    SoundLoad(3837)
    SoundLoad(3838)
    SoundLoad(3947)
    SoundLoad(3948)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04500.itp")
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 100500, 0, -9000, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 99500, 0, -9000, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x29)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 107600, 0, -1000, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0x0, -10000, 0, -7000, 0)
    SetChrPos(0x1, -10000, 0, -7000, 0)
    SetChrPos(0x2, -10000, 0, -7000, 0)
    SetChrPos(0x3, -10000, 0, -7000, 0)
    SetChrPos(0x4, -10000, 0, -7000, 0)
    SetChrPos(0x101, 100500, 0, -9000, 0)
    SetChrPos(0x104, 100000, 0, -9000, 0)
    SetChrPos(0x105, 99500, 0, -9000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(101420, 1300, -1100, 0)
    MoveCamera(40, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26240, 0)
    SetCameraDistance(22440, 6000)
    FadeToBright(1500, 0)
    OP_0D()
    PlaceName2(340, 50, "c_plac67", 0x0, 0)
    BeginChrThread(0xA, 3, 0, 3)
    Sleep(600)
    BeginChrThread(0x9, 3, 0, 4)
    Sleep(1200)
    BeginChrThread(0x104, 3, 0, 6)
    Sleep(600)
    BeginChrThread(0x101, 3, 0, 5)
    Sleep(600)
    BeginChrThread(0x105, 3, 0, 7)
    OP_6F(0x79)
    Fade(500)
    OP_68(100000, 2600, -3500, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16149, 0)
    OP_68(100000, 1600, -3500, 3000)
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x101,
        "#12P#00001F还有这样的地方啊……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        (
            "#6P#00301F哼……\x01",
            "在繁华市区中也算是超一流的地段呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，我工作的那家\x01",
            "男公关俱乐部也在这附近。\x02\x03",

            "#10300F说起来，这家店……\x01",
            "听说以前是议员先生们的专用店，\x01",
            "最近则多是外国宾客光顾了？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "#11P#04605F啊，确实。\x02\x03",

            "#04609F不过我们今天已经包了场，\x01",
            "不用拘束，尽情放松吧。\x02\x03",

            "#04602F好啦，快进去吧¤\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 8)
    Sleep(1000)

    #C0005
    ChrTalk(
        0x101,
        "#12P#00011F喂、喂……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)

    #C0006
    ChrTalk(
        0x105,
        "#6P#10302F真是个自由散漫的孩子啊。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#6P#00306F……加雷斯，\x01",
            "你平时跟着她可真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xA,
        "#5P哈哈，还好。\x02",
    )

    CloseMessageWindow()
    OP_68(100000, 1300, -2500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0x101, 500, 0, -8100, 0)
    SetChrPos(0x104, -500, 0, -6800, 0)
    SetChrPos(0x105, -1000, 0, -8100, 0)
    SetChrPos(0xA, -500, 0, -5000, 0)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x9, 900, 50, 25800, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x9, 3, 0, 9)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -700, 50, 25800, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1500, -4000, 0)
    MoveCamera(305, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24500, 0)

    def lambda_B99():
        OP_97(0xA, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_B99)
    Sleep(100)

    def lambda_BB6():
        OP_97(0x104, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BB6)
    Sleep(100)

    def lambda_BD3():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BD3)
    Sleep(100)

    def lambda_BF0():
        OP_97(0x105, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BF0)
    OP_68(0, 1500, 6000, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(100, 1500, 13380, 0)
    MoveCamera(305, 29, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    WaitChrThread(0xA, 0)
    OP_C9(0x0, 0x80000000)

    #N0009
    NpcTalk(
        0x8,
        "豪气的声音",
        "#3835V#30W你来了啊，兰道夫。\x02",
    )

    CloseMessageWindow()
    OP_24(0xEFB)
    OP_C9(0x1, 0x80000000)
    OP_68(-600, 1000, 23500, 2500)
    MoveCamera(321, 17, 0, 2500)
    SetCameraDistance(18000, 2500)
    OP_6F(0x79)
    SetChrFlags(0xA, 0x80)

    def lambda_CC7():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x4F4C, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CC7)
    Sleep(100)

    def lambda_CE4():
        OP_96(0xFE, 0x1F4, 0x0, 0x4A38, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CE4)
    Sleep(50)

    def lambda_D01():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x4A38, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D01)
    WaitChrThread(0x105, 1)

    #C0010
    ChrTalk(
        0x104,
        (
            "#6P#00303F叔叔……\x01",
            "这未免太唐突了吧？\x02\x03",

            "#00301F自从上次见面之后，两周时间内\x01",
            "没有任何音讯，这次却突然……\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0011
    AnonymousTalk(
        0x8,
        (
            "呵呵，我们也有\x01",
            "很多事情要做啊。\x02\x03",

            "话说回来，竟然会有\x01",
            "同伴跟着你到这种地方来……\x02\x03",

            "如果是两年前的你，这可真是无法想象呢。\x02",
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

    #C0012
    ChrTalk(
        0x104,
        (
            "#6P#00306F哼……\x01",
            "我们的队长是个很讲义气的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#6P#N#00003F初次见面。\x02\x03",

            "#00001F我是克洛斯贝尔警察局\x01",
            "特别任务支援科的罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x105,
        (
            "#6P#10304F同属支援科的准成员\x01",
            "瓦吉·赫米斯菲亚。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#04504F#11P我是『深红商会』的代表\x01",
            "西格蒙德·奥兰多。\x02\x03",

            "#04500F之前曾给你们添过麻烦，\x01",
            "这次不必客气，尽情畅饮吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#6P#N#00003F……那就恭敬不如从命了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0017
    ChrTalk(
        0x105,
        (
            "#6P#10302F话说回来，所谓的添麻烦，\x01",
            "是指旧矿山的那件事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#04502F#11P呵呵，先不说这些了。\x02\x03",

            "#04504F你们有点饿了吧？\x01",
            "我马上让他们上菜。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    EndChrThread(0x9, 0x3)
    SetChrSubChip(0x9, 0x3)
    Sleep(300)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0019
    ChrTalk(
        0x9,
        (
            "#04609F（津津有味）……\x01",
            "啊，再加一份冰激凌！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x104, -2900, 50, 24950, 135)
    SetChrPos(0x101, -3100, 50, 23300, 90)
    SetChrPos(0x105, -3100, 50, 21800, 90)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -1400, 200, 23900, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x2A)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -1400, 200, 22800, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x2A)
    SetChrSubChip(0xE, 0x5)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1400, 200, 21700, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x2B)
    SetChrSubChip(0xF, 0x8)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -600, 300, 21700, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x5)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 900, 200, 24100, 0)
    BeginChrThread(0x9, 3, 0, 9)
    OP_68(-700, 1400, 24300, 0)
    MoveCamera(319, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15100, 0)
    SetCameraDistance(15600, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0020
    ChrTalk(
        0x8,
        (
            "#04503F#11P好了……你们想必有很多话想说吧？\x02\x03",

            "#04500F几位远来是客，\x01",
            "就由你们先提问好了。\x02\x03",

            "这也是你们来此的目的之一吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00006F……是的，\x01",
            "多谢您的理解。\x02\x03",

            "#00008F老实说，克洛斯贝尔警察局\x01",
            "很关注你们的动向。\x02\x03",

            "#00013F特别是──你们滞留在\x01",
            "克洛斯贝尔究竟有何目的。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "#04502F#11P呵呵，真直接啊。\x02\x03",

            "#04504F我们来此的理由\x01",
            "有好几个……\x02\x03",

            "#04500F至于最大的目的，\x01",
            "自然还是因为签署了『契约』。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00001F这……\x01",
            "是与帝国政府签署的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#04504F#11P呵呵，无可奉告。\x02\x03",

            "这已经触及到我们\x01",
            "这个行业的保密义务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#00006F……这样啊。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x105,
        (
            "#6P#10300F那么，你们与埃雷波尼亚帝国\x01",
            "的雷克特大尉有什么关系？\x02\x03",

            "在收购鲁巴彻旧址时，\x01",
            "他好像帮了你们不少忙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#04504F#11P哼哼，那个满嘴胡话的小子吗？\x02\x03",

            "他不愧是『铁血』的亲信，\x01",
            "真是个很有趣的小鬼啊。\x02\x03",

            "#04500F这次说不定还可以和曹他们\x01",
            "好好较量一番呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0028
    ChrTalk(
        0x101,
        "#00011F哎！？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#5P#00301F叔叔……\x01",
            "你连那个戴眼镜的家伙都知道吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#04500F#11P去年在『那些家伙』的地盘上闹事时，\x01",
            "曾经和他交锋过一次。\x02\x03",

            "本来只是个简单到无聊的工作，\x01",
            "没想到会被他的手下咬住不放。\x02\x03",

            "#04504F呵呵，真没想到在这座城市里\x01",
            "也能遇到他。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "#12P#04606F（津津有味）……\x01",
            "最后还是没能见到\x01",
            "那个传说中的『银』啊。\x02\x03",

            "听说正在做其它的工作，\x01",
            "所以错失了见面的良机。\x02\x03",

            "#04600F『银』之前好像一直\x01",
            "都在克洛斯贝尔吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#5P#00306F嗯，但自从鲁巴彻覆灭之后，\x01",
            "就杳无音信了……\x02\x03",

            "#00301F喂，不要东拉西扯啊。\x01",
            "我们在问你们与雷克特\x01",
            "那家伙之间的关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#04502F#11P哼哼，岔开话题的意思\x01",
            "就是无可奉告。\x02\x03",

            "还望多加理解。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        "#5P#00301F啧……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00006F算了，兰迪。\x02\x03",

            "#00008F再问一个问题，\x01",
            "不愿回答也可以……\x02\x03",

            "#00001F你们这次的『契约』……\x01",
            "签约金是多少？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    EndChrThread(0x9, 0x3)
    SetChrSubChip(0x9, 0x2)

    #C0036
    ChrTalk(
        0x8,
        "#04505F#11P嘿……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#12P#04602F啊哈哈，小哥，\x01",
            "你的着眼点很不错嘛～\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 9)

    #C0038
    ChrTalk(
        0x105,
        (
            "#6P#10306F原来如此，从这种反应来看，\x01",
            "似乎是相当可观的金额。\x02\x03",

            "#10302F大概会有一亿米拉左右吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#04504F#11P无可奉告──\x01",
            "原本可以这样敷衍过去。\x02\x03",

            "#04502F不过，告诉你们也无妨，\x01",
            "这次的签约金差不多就是那个数字。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00011F一、一亿米拉的契约……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x105,
        "#6P#10304F呵呵，真是豪爽啊。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#5P#00306F……看来委托内容\x01",
            "不简单呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#04500F#11P呵呵，特别服务就到此为止了。\x02\x03",

            "#04503F接下来……\x01",
            "我们差不多也该进入正题了。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(1000)

    #C0044
    ChrTalk(
        0x8,
        (
            "#04503F#11P──兰道夫，\x01",
            "之前也说过，你的休假结束了。\x02\x03",

            "#04501F你要在近期\x01",
            "继承『斗神』之位。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0045
    ChrTalk(
        0x104,
        "#5P#00310F#4S……！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#00011F什么……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x105,
        (
            "#6P#10301F『斗神』……\x01",
            "不是兰迪父亲的称号吗？\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    SetCameraDistance(14000, 50000)
    SetChrChipByIndex(0x104, 0x28)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    Sound(802, 0, 100, 0)
    Sleep(300)
    SetChrSubChip(0x104, 0x1)
    Sound(811, 0, 100, 0)
    Sound(886, 0, 50, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0048
    ChrTalk(
        0x104,
        (
            "#5P#00307F别开玩笑了！\x01",
            "你在胡扯些什么！？\x02\x03",

            "该不会是喝多了酒，\x01",
            "在说醉话吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#04504F#11P呵呵，我的意思很简单。\x02\x03",

            "能率领『赤色星座』\x01",
            "的人只有『斗神』。\x02\x03",

            "#04500F而你身为大哥之子，\x01",
            "继承此位正是应尽的义务。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        (
            "#5P#00306F为、为何要我……\x02\x03",

            "#00307F如果必须要有『斗神』的话，\x01",
            "由你来继承不就好了吗！？\x02\x03",

            "或者谢莉也可以！\x01",
            "并没有女人不能继承之类的规矩吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#04503F#11P我终究是『战鬼』……\x01",
            "只能蹂躏战场。\x02\x03",

            "我无法变成大哥那样的人，\x01",
            "也不想变成那样的人。\x02\x03",

            "#04500F我女儿也一样……\x01",
            "不，从某种意义上说，也许比我更甚吧。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x3)
    SetChrSubChip(0x9, 0x2)

    #C0052
    ChrTalk(
        0x9,
        (
            "#12P#04604F嗯嗯，我也完全\x01",
            "当不了什么『斗神』哦。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 9)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x1)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)

    #C0053
    ChrTalk(
        0x104,
        "#5P#00310F唔……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#04503F#11P──兰道夫，\x01",
            "你应该很清楚。\x02\x03",

            "大哥为何会与\x01",
            "多年的宿敌决战。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_1F1B():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1F1B)
    WaitChrThread(0x104, 2)
    Sleep(500)

    #C0055
    ChrTalk(
        0x104,
        "#5P#00308F#40W#2S……啊………\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "#04501F#11P大哥当年\x01",
            "曾给予你『试炼』。\x02\x03",

            "而你也成功跨越了试炼，\x01",
            "出色地展现了继承『斗神』之位的素质。\x02\x03",

            "#04504F你应该早就察觉到了吧？\x01",
            "你已经无法再成为『其它存在』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#5P#00311F……呜……！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        "#00011F继承『斗神』之位的试炼……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x1)
    Sound(857, 0, 100, 0)
    Sound(856, 0, 50, 0)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_0D()
    Sleep(300)

    #C0059
    ChrTalk(
        0x9,
        (
            "#12P#04609F嘿嘿，别看兰迪哥现在一脸呆样，\x01",
            "但以前可是非常厉害的哦。\x02\x03",

            "#04602F当年为了击破『西风』的大部队，\x01",
            "把那个村子──\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x104, 0x28)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x96)

    #C0060
    ChrTalk(
        0x104,
        (
            "#5P#00313F#30W#4S──住口。\x02\x03",

            "#50W#3S算我求你……别再继续说了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)

    def lambda_2177():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2177)
    WaitChrThread(0x104, 2)
    Sleep(500)

    def lambda_2197():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2197)
    WaitChrThread(0x104, 2)
    Sleep(500)

    #C0061
    ChrTalk(
        0x101,
        "#00005F……兰迪……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        "#6P#10308F………………………………\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "#12P#04601F好无聊……\x01",
            "真有点失望呢。\x02\x03",

            "#04606F不过我还是很崇拜\x01",
            "当年的兰迪哥哟。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "#04504F#11P……哼哼，\x01",
            "就到此为止吧。\x02\x03",

            "#04500F我们回去了，谢莉。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        "#12P#04600F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x9, 3, 0, 10)
    Sleep(500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)
    SetChrPos(0x8, -700, 0, 25200, 180)
    OP_0D()
    Sleep(300)
    OP_68(-1560, 1400, 24280, 2500)
    MoveCamera(323, 15, 0, 2500)
    OP_6E(550, 2500)

    def lambda_2316():
        OP_95(0xFE, -2200, 0, 24800, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2316)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_6F(0x1)
    SetCameraDistance(13500, 15000)
    OP_C9(0x0, 0x80000000)

    #C0066
    ChrTalk(
        0x8,
        (
            "#11P#04503F#3836V#30W大哥要是看到你现在这副德性，\x01",
            "心里会怎么想？自己好好想想吧。\x02\x03",

            "#3837V在进一步丢人现眼之前，\x01",
            "尽快做出选择吧。\x01",
            "是服从？逃跑？还是抵抗？\x02\x03",

            "#04502F#3838V#40W……不然的话，就去死吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEFE)
    OP_C9(0x1, 0x80000000)
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    #C0067
    ChrTalk(
        0x101,
        "#00013F……！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        "#5P#00314F#40W………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_C9(0x0, 0x80000000)

    #C0069
    ChrTalk(
        0x9,
        (
            "#04609F#12P#N#3947V#30W呵呵，晚安啦，兰迪哥¤\x02\x03",

            "#04602F#3948V两位小哥，再见啦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF6C)
    OP_C9(0x1, 0x80000000)
    OP_68(-700, 1300, 20300, 4000)
    SetCameraDistance(17500, 4000)
    OP_93(0x9, 0x2, 0xBE)

    def lambda_24FA():
        OP_95(0xFE, 2500, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_24FA)
    Sleep(300)

    def lambda_2517():
        OP_95(0xFE, -2300, 0, 10400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2517)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x105, 0x0)
    Sleep(700)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x105, 0x2)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    Fade(500)
    SetCameraDistance(15300, 0)
    OP_68(-2900, 1100, 24950, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)
    OP_6F(0x79)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    OP_0D()
    Sound(2374, 255, 100, 0)    #voice#Randy
    Sleep(1000)

    #C0070
    ChrTalk(
        0x104,
        (
            "#11P#00316F#40W真是的，没带大小姐她们\x01",
            "一起来，真是万幸啊……\x02\x03",

            "#00315F……我实在太丢人了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(250)

    #C0071
    ChrTalk(
        0x101,
        "#6P#00008F兰迪……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(150)

    #C0072
    ChrTalk(
        0x104,
        (
            "#11P#00306F#30W……抱歉。\x02\x03",

            "#00308F让你们看到了\x01",
            "我如此丢脸的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#6P#00006F……不要这么说啊。\x02\x03",

            "#00013F无论怎么想……\x01",
            "都是他们不好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，但竟然能让你\x01",
            "沮丧成这样，由此来看──\x02\x03",

            "#10300F他们的话似乎戳中了你的要害吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0075
    ChrTalk(
        0x101,
        "#11P#00007F瓦吉……！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    #Sound(2375, 255, 100, 0)    #voice#Randy

    #C0076
    ChrTalk(
        0x104,
        "#11P#00312F#40W呵呵……真是个讨厌的家伙。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetCameraDistance(13800, 12500)
    Fade(250)
    SetChrChipByIndex(0x104, 0x28)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    OP_0D()
    Sleep(800)

    #C0077
    ChrTalk(
        0x104,
        (
            "#11P#00313F#40W#25A嗯……正是如此。\x02\x03",

            "#50W#42A完全戳中了要害……\x01",
            "戳到了我最大的痛处。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──之后，罗伊德等人谢绝了\x01",
            "经理为他们准备车辆的好意，\x01",
            "步行踏上了归途。\x02\x03",

            "平安无事地回到了忧心等待大家的\x01",
            "女性同伴与赛尔盖的面前……\x02\x03",

            "将已经睡眼朦胧的琪雅哄睡之后，\x01",
            "罗伊德等人将事情的经过做了报告。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 3)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_5EF end

    def Function_12_2958(): pass

    label("Function_12_2958")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch47500.itc", 0x1E)
    LoadChrToIndex("chr/ch44000.itc", 0x1F)
    LoadChrToIndex("chr/ch06400.itc", 0x20)
    LoadChrToIndex("chr/ch42800.itc", 0x21)
    LoadChrToIndex("chr/ch25800.itc", 0x22)
    LoadChrToIndex("chr/ch25900.itc", 0x23)
    LoadChrToIndex("chr/ch26802.itc", 0x24)
    LoadChrToIndex("chr/ch43402.itc", 0x25)
    LoadChrToIndex("chr/ch27702.itc", 0x26)
    LoadChrToIndex("chr/ch47502.itc", 0x27)
    LoadChrToIndex("chr/ch44002.itc", 0x28)
    SoundLoad(812)
    SoundLoad(896)
    OP_68(104870, 3100, -2210, 0)
    MoveCamera(46, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    SetChrPos(0x101, 103450, 0, -1770, 90)
    SetChrPos(0x102, 103840, 0, -3240, 45)
    SetChrPos(0x103, 103720, 0, 140, 135)
    SetChrPos(0x104, 105010, 0, -1570, 90)
    SetChrPos(0x109, 102060, 0, -780, 90)
    SetChrPos(0x105, 104660, 0, -4160, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 101610, 0, -2300, 90)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 107620, 0, -1610, 270)
    OP_68(104870, 1500, -2210, 3000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()

    #C0079
    ChrTalk(
        0x104,
        (
            "#1P#00303F……事情就是这样。\x01",
            "希望能允许\x01",
            "我们进入。\x02\x03",

            "#00301F另外，还要对\x01",
            "叔叔和谢莉保密哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x14,
        (
            "……久别重逢，你竟会\x01",
            "因为这种杂事拜托我。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x14,
        (
            "哼哼，兰道夫队长……\x01",
            "莫非正如大小姐所说，\x01",
            "你已经沦落成一个窝囊废了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        "#1P#00303F……不要再这样叫我。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_END)), "loc_2C18")

    #C0083
    ChrTalk(
        0x101,
        (
            "#00001F（『赤色星座』的猎兵……\x01",
            "　好像就是以前曾在深红商会门前\x01",
            "　遇到的那个人呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C56")

    label("loc_2C18")


    #C0084
    ChrTalk(
        0x101,
        (
            "#00001F（『赤色星座』的猎兵……\x01",
            "　似乎是兰迪的旧识呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C56")


    #C0085
    ChrTalk(
        0x13,
        "（紧张……）\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x14,
        (
            "……哼哼，也罢。\x01",
            "毕竟是你的请求，\x01",
            "我就帮个忙好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x14,
        (
            "话说在先，我能做的顶多也就是\x01",
            "在你们没惹出太大乱子的情况下，\x01",
            "当作什么都没看见。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x14,
        (
            "另外，不把你来此的事情\x01",
            "告诉副团长和小姐。\x01",
            "……这样可以吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        "#1P#00303F……这就足够了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x10E, 0x1F4)
    Sleep(100)

    #C0090
    ChrTalk(
        0x104,
        (
            "#1P#00300F好，已经交代好了。\x02\x03",

            "#00300F夫人他们好像还没来，\x01",
            "如果想埋伏起来的话，\x01",
            "还是先进去为好。\x02\x03",

            "#00303F不过我就不进去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00000F嗯，人数还是\x01",
            "越少越好……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x13,
        (
            "我、我是一定要进去的，\x01",
            "剩下的人选就由你们自己决定！\x02",
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

    def lambda_2ED5():
        TurnDirection(0x101, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ED5)
    Sleep(50)

    def lambda_2EE5():
        TurnDirection(0x102, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2EE5)
    Sleep(50)

    def lambda_2EF5():
        TurnDirection(0x103, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2EF5)
    Sleep(50)

    def lambda_2F05():
        TurnDirection(0x109, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2F05)
    Sleep(50)

    def lambda_2F15():
        TurnDirection(0x105, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2F15)

    #C0093
    ChrTalk(
        0x109,
        "#10111F（他好激动啊……）\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        (
            "#00206F（已经走到了这一步，\x01",
            "  他自然不可能让步的……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(50)

    #C0095
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，那就让我也进去吧。\x02\x03",

            "#10300F副局长先生、罗伊德和我，\x01",
            "由我们三人进去如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        "#1P#00300F嗯，这样挺好。\x02",
    )

    CloseMessageWindow()

    def lambda_3000():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3000)
    Sleep(50)

    def lambda_3010():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3010)
    Sleep(50)

    def lambda_3020():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3020)

    #C0097
    ChrTalk(
        0x102,
        (
            "#00100F那我们就在\x01",
            "外面等你们啦。\x02\x03",

            "万一遇到什么情况，\x01",
            "就用艾尼格玛来联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#00004F嗯，知道了。\x02\x03",

            "#00000F那我们就\x01",
            "赶快去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x13,
        "嗯……走、走吧，诸位！！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -7010, 0, -3490, 90)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -3410, 0, -5940, 90)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -4740, 0, -2140, 225)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x2)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 7220, 0, -990, 225)
    SetChrChipByIndex(0x19, 0x26)
    SetChrSubChip(0x19, 0x1)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 6220, 0, -1000, 180)
    SetChrPos(0x101, -3560, 0, 18530, 180)
    SetChrPos(0x105, -4460, 0, 18910, 180)
    SetChrPos(0x13, -3870, 0, 19520, 180)
    OP_68(-2710, 1500, -5230, 0)
    MoveCamera(307, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19130, 0)
    OP_68(3930, 1500, -3640, 6000)
    MoveCamera(307, 18, 0, 6000)
    OP_6E(440, 6000)
    SetCameraDistance(19130, 6000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()
    OP_68(-4560, 1500, 16460, 8000)
    MoveCamera(305, 17, 0, 8000)
    OP_6E(440, 8000)
    SetCameraDistance(17710, 8000)
    OP_6F(0x1)
    Sleep(500)

    #C0100
    ChrTalk(
        0x101,
        (
            "#00000F已经和他们打过招呼了，\x01",
            "夫人他们来了以后，\x01",
            "会被立刻引领到这个席位。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x13,
        (
            "嗯、嗯……\x01",
            "很好。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x13,
        (
            "可恶的无德房产商……\x01",
            "我一定会抓住你！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1194)

    #C0103
    ChrTalk(
        0x105,
        (
            "#10309F呵呵，开始\x01",
            "期待起来了呢。\x02\x03",

            "#10305F……哦，\x01",
            "说着说着\x01",
            "就来了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 0x1E)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x11, -480, 0, -8690, 0)
    SetChrPos(0x12, 790, 0, -8960, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(360, 1500, -6110, 0)
    MoveCamera(315, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20150, 0)
    Sleep(100)
    OP_68(780, 1500, -8090, 2500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)

    def lambda_33DB():
        OP_9B(0x0, 0x11, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_33DB)
    Sleep(300)

    def lambda_33F3():
        OP_9B(0x0, 0x12, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_33F3)
    WaitChrThread(0x11, 1)

    def lambda_340C():
        OP_95(0x11, -2000, 0, -5940, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_340C)
    WaitChrThread(0x12, 1)

    def lambda_342A():
        OP_93(0x12, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_342A)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0x10E, 0x1F4)
    OP_6F(0x1)
    OP_0D()
    Sleep(500)

    #C0104
    ChrTalk(
        0x11,
        (
            "那个，我是之前预约\x01",
            "过的克莱德……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x16,
        "请到这边坐。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5840, 1500, 14140, 0)
    MoveCamera(298, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20470, 0)
    SetChrChipByIndex(0x11, 0x27)
    SetChrChipByIndex(0x12, 0x28)
    SetChrSubChip(0x11, 0x2)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -7450, 100, 14400, 135)
    SetChrPos(0x12, -8000, 100, 13110, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0106
    ChrTalk(
        0x12,
        "呵呵，真是家不错的店呢。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x11,
        (
            "呀，玛格丽特夫人……\x01",
            "莫非您是第一次来这种地方吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x11,
        (
            "本以为您那在警察局担任要职的先生\x01",
            "一定会带您去各种地方享受的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x1)

    #C0109
    ChrTalk(
        0x12,
        "哦呵呵，别开玩笑啦。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x12,
        (
            "不过就是个警察局的副局长而已，\x01",
            "那点薪水够干什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x12,
        (
            "比起和我一起光顾高档的店，\x01",
            "在破旧的小酒吧里与女公关\x01",
            "一起喝酒才与那个人的品性相符。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    #C0112
    ChrTalk(
        0x11,
        "哈哈，真是失礼了。\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0113
    ChrTalk(
        0x11,
        (
            "那么……虽然现在还是白天，\x01",
            "但让我先请夫人喝一杯\x01",
            "振奋精神的鸡尾酒吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x12,
        "呵呵……那就不客气啦。\x02",
    )

    CloseMessageWindow()
    OP_68(-5050, 1500, 16160, 2000)
    OP_6F(0x1)
    Sleep(500)
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x13)

    #C0115
    ChrTalk(
        0x101,
        (
            "#00012F（副、副局长，\x01",
            "  请不必太在意……）\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x13,
        (
            "（烦、烦死了……\x01",
            "  不用管我。）\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x13,
        (
            "（哼，说的没错。\x01",
            "  反正凭我那点可怜的薪水，\x01",
            "  确实无法来这种高级的店里消费。）\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x13,
        (
            "（街边的破旧小酒馆才与我相符。\x01",
            "  但那又有什么不好……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0119
    ChrTalk(
        0x105,
        "#10300F（好像彻底消沉了呢。）\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        "#00006F（不、不要紧吧……）\x02",
    )

    CloseMessageWindow()
    OP_68(-5840, 1500, 14140, 2000)
    OP_6F(0x1)
    Sleep(500)

    #C0121
    ChrTalk(
        0x11,
        "那么，虽然有些急促，但请您在这里签个字……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0122
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "克莱德从公文包中取出\x01",
            "一份看似合同的文件。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(18, 0, 50, 0)
    Sleep(200)

    #C0123
    ChrTalk(
        0x11,
        (
            "这就是夫人想要的那栋\x01",
            "位于米修拉姆一流地段\x01",
            "的别墅的购买合同。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x11,
        (
            "您只要在这里\x01",
            "签上名字，\x01",
            "那栋别墅就归您所有啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0125
    ChrTalk(
        0x12,
        (
            "呵呵……\x01",
            "终于迎来这个时刻了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x12,
        "我当然会签。\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(100)

    #C0127
    ChrTalk(
        0x101,
        (
            "#00001F（果然是在销售\x01",
            "  米修拉姆的别墅啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x105,
        (
            "#10300F（那么，接下来该怎么办呢？）\x02\x03",

            "#10304F（就算想出面介入，\x01",
            "  是不是也应该再听一下……）\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x13)

    #C0129
    ChrTalk(
        0x13,
        "……你……你……\x02",
    )

    CloseMessageWindow()
    OP_68(-6600, 0, 15210, 500)
    MoveCamera(305, 18, 1, 500)
    OP_6E(500, 500)
    SetCameraDistance(20950, 500)
    OP_95(0x13, -2060, 0, 19090, 5000, 0x0)
    OP_95(0x13, -2360, 0, 12830, 5000, 0x0)
    TurnDirection(0x13, 0x12, 1000)
    Sleep(50)
    OP_6F(0x1)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0130
    ChrTalk(
        0x13,
        (
            "#4S你不要再欺骗\x01",
            "我的太太了！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)

    #C0131
    ChrTalk(
        0x11,
        "哎……！？\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x12,
        "……老公……！？\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#00011F（哇哇……！？）\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x105,
        "#10306F（哎呀呀。）\x02",
    )

    CloseMessageWindow()

    def lambda_3C04():
        OP_95(0x101, -820, 0, 18700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C04)
    Sleep(200)

    def lambda_3C21():
        OP_95(0x105, -820, 0, 18700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C21)
    WaitChrThread(0x101, 1)

    def lambda_3C3F():
        OP_95(0x101, -1590, 0, 11760, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C3F)
    WaitChrThread(0x105, 1)

    def lambda_3C5D():
        OP_95(0x105, -1710, 0, 13690, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C5D)
    WaitChrThread(0x105, 1)

    def lambda_3C7B():
        TurnDirection(0x105, 0x12, 1000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C7B)
    Sleep(100)
    WaitChrThread(0x101, 1)

    def lambda_3C8F():
        TurnDirection(0x101, 0x12, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C8F)
    WaitChrThread(0x101, 1)
    Sound(812, 0, 100, 0)
    BeginChrThread(0x12, 1, 0, 14)
    Sleep(300)
    Sound(812, 0, 100, 0)
    BeginChrThread(0x11, 1, 0, 13)
    Sleep(1000)
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x13)

    #C0135
    ChrTalk(
        0x12,
        "老公……这是怎么回事？\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0136
    ChrTalk(
        0x13,
        (
            "#4S玛格丽特！！\x01",
            "请赶快停止这种交易！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0137
    ChrTalk(
        0x13,
        (
            "#4S这个无德的房产商\x01",
            "只是想欺骗你而已！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x11)

    #C0138
    ChrTalk(
        0x11,
        (
            "什么！？\x01",
            "请、请等一下！！\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x11,
        (
            "无、无德……\x01",
            "我、我究竟做了什么……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0140
    ChrTalk(
        0x13,
        (
            "#4S住嘴！你不许说话！\x01",
            "我已经找到证据了，你别想再狡辩！\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x12,
        "……老公……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0142
    ChrTalk(
        0x13,
        (
            "#4S你油嘴滑舌地哄骗我太太，\x01",
            "是想让她背负\x01",
            "巨额贷款吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x12,
        "……老公……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0144
    ChrTalk(
        0x13,
        (
            "#4S但你想得未免也太美了！\x01",
            "我是不会让你得逞的……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x12,
        "……喂，老公……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0146
    ChrTalk(
        0x13,
        (
            "#4S烦死了，你不要说话！\x01",
            "我身为警察局的副局长……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x1450)

    #C0147
    ChrTalk(
        0x12,
        "#800W#5S你　给　我　立　刻　住　嘴　。\x02",
    )

    Sleep(4800)
    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(896, 0, 60, 0)
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0148
    ChrTalk(
        0x13,
        "#2S……对不起。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 500)
    Sleep(50)

    #C0149
    ChrTalk(
        0x101,
        "#00011F（气势弱、弱了！？）\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x105,
        "#10309F（啊哈哈，完全不敢出声了呢。）\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x12,
        (
            "真是的……\x01",
            "你实在是个\x01",
            "无药可救的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x12,
        (
            "身为警察局的副局长，\x01",
            "竟然在毫无根据的情况下\x01",
            "将无辜人士视为犯罪分子……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0153
    ChrTalk(
        0x12,
        "#4S难道就不觉得可耻吗！？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x13,
        (
            "哇哇！！\x01",
            "对不起，我再也不敢了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x13)
    OP_64(0x101)
    OP_64(0x105)

    #C0155
    ChrTalk(
        0x13,
        "嗯？难道搞错了吗……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12, 500)
    Sleep(50)

    #C0156
    ChrTalk(
        0x101,
        "#00011F什么！？\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x105,
        (
            "#10300F夫人，如果可以，\x01",
            "能否将事情的详情告诉我们呢？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-6950, -600, 15800, 0)
    MoveCamera(328, 22, 1, 0)
    OP_6E(500, 0)
    SetCameraDistance(20840, 0)
    SetChrPos(0x11, -6060, 0, 13990, 90)
    OP_0D()
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)

    #C0158
    ChrTalk(
        0x12,
        "#3P呼……算了，告诉你们也无妨。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x12,
        (
            "#3P话说在先，\x01",
            "克莱德确实是一位销售\x01",
            "高级房地产的房产商。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x12,
        (
            "#3P绝不是你刚才说的\x01",
            "什么无德商人。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x13,
        (
            "可、可是，就算是这样……\x01",
            "咱们哪有购买高级房产的资金……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x12,
        (
            "#3P其实，我为了打发时间，从不久前\x01",
            "开始炒股，结果赚到了不少钱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x12,
        (
            "#3P金额相当于你需要花费\x01",
            "多年时间才能攒下的钱。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0164
    ChrTalk(
        0x13,
        "炒、炒股……！？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x12,
        (
            "#3P说心里话……\x01",
            "……我对你这个人\x01",
            "早就失望透顶了。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x12,
        (
            "#3P靠着后门和运气才得到现在的地位，\x01",
            "在外面飞扬跋扈，回到家里却一副窝囊样，\x01",
            "在我面前连头都抬不起来……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x12,
        (
            "#3P不知道你是不是在家里待得很痛苦，\x01",
            "只要一有点机会就跑出去通宵酗酒，\x01",
            "毫无节制地浪费家中积蓄。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x13,
        "呜呜……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x12,
        (
            "#3P在前局长刚刚下台的时候，\x01",
            "你曾以为自己会成为新局长，\x01",
            "高兴了好一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x12,
        (
            "#3P但最后却输给了另一位\x01",
            "副局长，实在是狼狈万分。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x12,
        (
            "#3P而且你还因此而烦闷不堪，\x01",
            "整天唠唠叨叨地发牢骚……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#00012F夫、夫人，这些事情就不必……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x12,
        (
            "#3P……说实话，\x01",
            "我觉得已经很难\x01",
            "继续与你一起生活了。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x12,
        (
            "#3P所以我才会和克莱德先生商谈，\x01",
            "准备用炒股赚来的钱买一座房子，\x01",
            "用于分居生活。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x12,
        (
            "#3P我原本打算先在那边\x01",
            "生活一段时间，等到时机\x01",
            "成熟后再向你递交离婚协议书。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0176
    ChrTalk(
        0x13,
        "#4S（巨大打击！！）\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        "#10309F啊哈哈，真无情呢。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#00006F（实、实在太可怜了……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0179
    ChrTalk(
        0x101,
        (
            "#00005F哎，不过……\x01",
            "您刚才说『原本打算』，也就是说……？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x13,
        "……哎……\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x12,
        (
            "#3P……呵呵，不错。\x01",
            "他因为担心我，竟能一直追到这里。\x01",
            "这份心意，我便接受好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x12,
        (
            "#3P对于这个平时怕我\x01",
            "怕到不敢回家的人来说，\x01",
            "这次的表现实在是很不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x12,
        (
            "#3P今天就先回家，\x01",
            "再和他谈一谈好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x13,
        "玛、玛格丽特……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 500)
    Sleep(50)

    #C0185
    ChrTalk(
        0x12,
        (
            "#3P……事情就是这样，克莱德先生。\x01",
            "购买别墅的事情\x01",
            "就暂缓一阵子吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 500)
    Sleep(50)

    #C0186
    ChrTalk(
        0x11,
        (
            "#3P怎、怎么可以这样，玛格丽特夫人！\x01",
            "都已经谈到这个地步了，您却……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x12,
        "#3P只是『暂缓』而已啦。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x12,
        (
            "#3P我一个人擅自\x01",
            "做出这种决定也不太好，\x01",
            "还是应该再和他商量一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x12,
        (
            "#3P别担心，虽然不准备分居了，\x01",
            "但我确实看中了那套房子，\x01",
            "一定会买的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0190
    ChrTalk(
        0x11,
        (
            "#3P呼，本想在今天\x01",
            "就得到您的好消息呢……\x01",
            "真是没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x11,
        "#3P那我就先告辞了……\x02",
    )

    CloseMessageWindow()
    OP_68(-5570, -600, 15480, 2000)

    def lambda_4A2F():
        OP_95(0x11, -2680, 0, 14150, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4A2F)
    Sleep(500)

    def lambda_4A4C():
        OP_93(0x12, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4A4C)

    def lambda_4A59():
        OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A59)
    Sleep(100)

    def lambda_4A71():
        OP_9B(0x1, 0x105, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4A71)
    Sleep(100)

    def lambda_4A89():
        OP_9B(0x1, 0x13, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4A89)
    WaitChrThread(0x11, 1)
    OP_6F(0x1)
    Sleep(50)

    def lambda_4AA7():
        OP_9B(0x0, 0x11, 0x5A, 0x2710, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4AA7)
    Sleep(1000)
    OP_93(0x12, 0x5A, 0x1F4)
    Sleep(100)
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(100)
    TurnDirection(0x105, 0x11, 500)
    Sleep(100)
    TurnDirection(0x13, 0x11, 500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0x12, 0x87, 0x1F4)
    Sleep(100)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)
    OP_93(0x13, 0xB4, 0x1F4)
    Sleep(100)
    OP_93(0x105, 0xB4, 0x1F4)
    WaitChrThread(0x11, 1)
    SetChrFlags(0x11, 0x80)
    Sleep(100)

    #C0192
    ChrTalk(
        0x101,
        (
            "#00001F嗯……看来那个人\x01",
            "确实是无辜的……\x02\x03",

            "#00006F真是对不住他啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，算啦。\x01",
            "至少副局长和他夫人的事情\x01",
            "总算是告一段落了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 500)
    Sleep(50)

    #C0194
    ChrTalk(
        0x12,
        (
            "#3P……那好，老公，\x01",
            "我今天会回家的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BDF():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4BDF)
    Sleep(50)

    def lambda_4BEF():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BEF)
    Sleep(50)

    def lambda_4BFF():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4BFF)

    #C0195
    ChrTalk(
        0x12,
        (
            "#3P有很多话想和你说，\x01",
            "今晚下班后可要立刻回家哦。\x01",
            "……知道了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0196
    ChrTalk(
        0x13,
        "……是、是！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0197
    ChrTalk(
        0x101,
        "#00006F（……不要紧吧……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("c1160", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2958 end

    def Function_13_4CCF(): pass

    label("Function_13_4CCF")

    Fade(500)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -7060, 0, 13990, 90)
    Return()

    # Function_13_4CCF end

    def Function_14_4CF3(): pass

    label("Function_14_4CF3")

    Fade(500)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -7490, 0, 13110, 90)
    Return()

    # Function_14_4CF3 end

    SaveToFile()

Try(main)
