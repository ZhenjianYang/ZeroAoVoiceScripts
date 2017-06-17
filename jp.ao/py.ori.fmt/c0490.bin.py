from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "シグムント",             # 1
        "シャーリィ",             # 2
        "猟兵ガレス",             # 3
        "支配人",                 # 4
        "食器",                   # 5
        "食器",                   # 6
        "食器",                   # 7
        "食器",                   # 8
        "食器",                   # 9
        "クライド",               # 10
        "マーガレット夫人",       # 11
        "ピエール副局長",         # 12
        "猟兵ザックス",           # 13
        "店員",                   # 14
        "店員",                   # 15
        "ホステス",               # 16
        "ホステス",               # 17
        "客",                     # 18
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
        "Function_12_2C34",        # 0C, 12
        "Function_13_541B",        # 0D, 13
        "Function_14_543F",        # 0E, 14
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
        "#12P#00001Fこんな場所があったのか……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        (
            "#6P#00301Fフン……\x01",
            "繁華街でも超一等地だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、僕が顔を出してる\x01",
            "ホストクラブも近くにあるよ。\x02\x03",

            "#10300Fそういえば、この店……\x01",
            "前は議員先生の御用達だったけど\x01",
            "最近は外国の賓客が多いんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "#11P#04605Fあー、そうみたいだね。\x02\x03",

            "#04609Fちなみに今日は貸し切りだから\x01",
            "遠慮なくくつろいじゃっていいよ。\x02\x03",

            "#04602Fさ、入った入った♪\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 8)
    Sleep(1000)

    #C0005
    ChrTalk(
        0x101,
        "#12P#00011Fお、おい……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)

    #C0006
    ChrTalk(
        0x105,
        "#6P#10302F自由気ままな子だねぇ。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#6P#00306F……ガレス。\x01",
            "お守り、ご苦労さんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xA,
        "#5Pハハ、とんでもない。\x02",
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

    def lambda_BBA():
        OP_97(0xA, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_BBA)
    Sleep(100)

    def lambda_BD7():
        OP_97(0x104, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BD7)
    Sleep(100)

    def lambda_BF4():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BF4)
    Sleep(100)

    def lambda_C11():
        OP_97(0x105, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C11)
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
        "逞しい声",
        "#3835V#30W──来たか、ランドルフ。\x02",
    )

    CloseMessageWindow()
    OP_24(0xEFB)
    OP_C9(0x1, 0x80000000)
    OP_68(-600, 1000, 23500, 2500)
    MoveCamera(321, 17, 0, 2500)
    SetCameraDistance(18000, 2500)
    OP_6F(0x79)
    SetChrFlags(0xA, 0x80)

    def lambda_CEC():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x4F4C, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CEC)
    Sleep(100)

    def lambda_D09():
        OP_96(0xFE, 0x1F4, 0x0, 0x4A38, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D09)
    Sleep(50)

    def lambda_D26():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x4A38, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D26)
    WaitChrThread(0x105, 1)

    #C0010
    ChrTalk(
        0x104,
        (
            "#6P#00303F叔父貴……\x01",
            "ずいぶん唐突じゃねえか？\x02\x03",

            "#00301F前に会ってから２週間……\x01",
            "何の音沙汰もなかったクセによ。\x02",
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
            "フフ、こちらも\x01",
            "色々やることがあってな。\x02\x03",

            "しかしお前がこの場に\x01",
            "ツレを連れてくるとは……\x02\x03",

            "２年前のお前じゃ考えられんな。\x02",
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
            "#6P#00306Fフン……\x01",
            "うちのリーダーは義理堅いんでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#6P#N#00003F──初めまして。\x02\x03",

            "#00001Fクロスベル警察、特務支援課、\x01",
            "ロイド・バニングスといいます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x105,
        (
            "#6P#10304F同じく支援課の準メンバー、\x01",
            "ワジ・へミスフィアだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#04504F#11P《クリムゾン商会》代表、\x01",
            "シグムント・オルランドだ。\x02\x03",

            "#04500F迷惑を掛けた貸しもある。\x01",
            "ゆっくりと飲んでいくがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#6P#N#00003F……では、お言葉に甘えて。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0017
    ChrTalk(
        0x105,
        (
            "#6P#10302Fところで迷惑を掛けたっていうのは\x01",
            "旧鉱山の一件でいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#04502F#11Pクク、さてな。\x02\x03",

            "#04504F腹も減ってるんだろう？\x01",
            "すぐに料理を持ってこさせよう。\x02",
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
            "#04609Fもぐもぐ……\x01",
            "あ、パフェもう１つ追加ね！\x02",
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
            "#04503F#11Pさて……積もる話もあるが。\x02\x03",

            "#04500Fまずは客人。\x01",
            "お前らからの質問に答えよう。\x02\x03",

            "それが目当ての一つだろうが？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00006F……はい。\x01",
            "話が早くて助かります。\x02\x03",

            "#00008F率直に言って、クロスベル警察は\x01",
            "あなた方の動向に注目しています。\x02\x03",

            "#00013F特に──どのような目的で\x01",
            "クロスベルに滞在しているかを。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "#04502F#11Pフフ、直球だな。\x02\x03",

            "#04504F俺たちがここにいる理由は\x01",
            "幾つかあるが……\x02\x03",

            "#04500Fもちろん最大の目的は\x01",
            "“契約”を結んだからだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00001Fそれは……\x01",
            "帝国政府との契約ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#04504F#11Pフフ、ノーコメントだ。\x02\x03",

            "ウチの業界にとっちゃあ\x01",
            "守秘義務に抵触するんでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#00006F……なるほど。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x105,
        (
            "#6P#10300Fそれじゃ、エレボニアの\x01",
            "レクター大尉との関係は？\x02\x03",

            "ルバーチェ跡地の買収で\x01",
            "お世話になったそうじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#04504F#11Pクク、あの戯言#4Rざれごと#使いか。\x02\x03",

            "《鉄血》の懐刀だけあって\x01",
            "なかなか面白い小僧だ。\x02\x03",

            "#04500F案外、ツァオあたりとも\x01",
            "良い勝負をするかもしれんな。\x02",
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
        "#00011Fえ！？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#5P#00301F叔父貴……\x01",
            "あの眼鏡野郎も知ってんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#04500F#11P去年、“連中”の縄張りを\x01",
            "かき回した時にやり合った。\x02\x03",

            "正直、ぬるい仕事だったが\x01",
            "ヤツの手勢には食い下がられてな。\x02\x03",

            "#04504Fフフ、まさかこの街でも\x01",
            "顔を合わせるとは思わなかったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "#12P#04606Fモグモグ……\x01",
            "ウワサの《銀#2Rイン#》ってのには\x01",
            "結局会えなかったんだよねー。\x02\x03",

            "別の仕事をしてたらしくて\x01",
            "ニアミスだったみたいでさー。\x02\x03",

            "#04600F確かちょっと前まで\x01",
            "クロスベルにいたんでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#5P#00306Fああ、ルバーチェが消えてから\x01",
            "音沙汰はねぇらしいが……\x02\x03",

            "#00301F──って、誤魔化すな。\x01",
            "あのレクターってヤツとの\x01",
            "関係を聞いてんだろうが。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#04502F#11Pクク、つまりは\x01",
            "ノーコメントというわけだ。\x02\x03",

            "それ以上は察しろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        "#5P#00301Fチッ……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00006Fいいさ、ランディ。\x02\x03",

            "#00008Fちなみに差し支えなければで\x01",
            "いいんですが……\x02\x03",

            "#00001F今回の“契約”というのは\x01",
            "どのくらいの額なんですか？\x02",
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
        "#04505F#11Pほう……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#12P#04602Fあはは、お兄さん。\x01",
            "目の付けどころがイイね～。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 9)

    #C0038
    ChrTalk(
        0x105,
        (
            "#6P#10306Fなるほど、そんな反応が\x01",
            "出てくるくらいの額なんだ。\x02\x03",

            "#10302F１億ミラくらい出てるのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#04504F#11Pノーコメントだ──\x01",
            "とはぐらかしてもいいが。\x02\x03",

            "#04502Fま、今回の契約に関しては\x01",
            "そのくらいの額と言っておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00011Fい、１億ミラ相当の契約……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x105,
        "#6P#10304Fフフ、豪気だねぇ。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#5P#00306F……ロクでもねぇことを\x01",
            "やろうとしてるみてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#04500F#11Pフフ、サービスはここまでだ。\x02\x03",

            "#04503Fそれじゃあ……\x01",
            "そろそろ本題に入るとしよう。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(1000)

    #C0044
    ChrTalk(
        0x8,
        (
            "#04503F#11P──ランドルフ。\x01",
            "前も言ったが休暇は終わりだ。\x02\x03",

            "#04501F貴様には近いうちに\x01",
            "次の《闘神#4Rとうしん#》を継いでもらう。\x02",
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
        "#5P#00310F#4Sッ……！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#00011Fな……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x105,
        (
            "#6P#10301F《闘神》……\x01",
            "親父さんの異名だっけ？\x02",
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
            "#5P#00307F──ざけんな！\x01",
            "何を口走ってやがる！\x02\x03",

            "まさか酒に酔ったとか\x01",
            "抜かすんじゃねえだろうな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#04504F#11Pフフ、簡単な話だ。\x02\x03",

            "《赤い星座》を率いるのは\x01",
            "《闘神》でなくてはならん。\x02\x03",

            "#04500Fそして、それを継ぐのは\x01",
            "兄貴の息子である貴様の義務だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        (
            "#5P#00306Fな、何で俺が……\x02\x03",

            "#00307F《闘神》が必要ってんなら\x01",
            "アンタが継ぎゃあいいだろう！？\x02\x03",

            "何ならシャーリィでもいい！\x01",
            "女じゃいけない理由はねえはずだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#04503F#11P俺はあくまで《戦鬼》……\x01",
            "戦場を蹂躙するだけの存在#4Rモ ノ#。\x02\x03",

            "兄貴みたいにはなれんし、\x01",
            "また、なりたいとも思わん。\x02\x03",

            "#04500Fそれは娘#2Rコイツ#も同じ……\x01",
            "いや、ある意味俺以上だろう。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x3)
    SetChrSubChip(0x9, 0x2)

    #C0052
    ChrTalk(
        0x9,
        (
            "#12P#04604Fうんうん、シャーリィも\x01",
            "《闘神》なんて柄#2Rガラ#じゃないなぁ。\x02",
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
        "#5P#00310Fぐっ……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#04503F#11P──ランドルフ。\x01",
            "貴様には分かっているはずだ。\x02\x03",

            "兄貴が何故、長年の宿敵と\x01",
            "決着を付ける気になったのかを。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_2153():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2153)
    WaitChrThread(0x104, 2)
    Sleep(500)

    #C0055
    ChrTalk(
        0x104,
        "#5P#00308F#40W#2S……あ………\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "#04501F#11Pかつて兄貴は\x01",
            "貴様に“試練”を与えた。\x02\x03",

            "そして貴様はそれを乗り越え、\x01",
            "見事《闘神》を継ぐ器を示した。\x02\x03",

            "#04504F──お前も気付いているはずだ。\x01",
            "もう“他のもの”にはなれん事を。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#5P#00311F……ッ……！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        "#00011F《闘神》を継ぐ試練……\x02",
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
            "#12P#04609Fえへへ、今はヘタレてるけど\x01",
            "昔のランディ兄は凄かったよね。\x02\x03",

            "#04602Fなにせ《西風》の大部隊を\x01",
            "撃破するために、あの村を──\x02",
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
            "#5P#00313F#30W#4S──黙れ。\x02\x03",

            "#50W#3S頼むから……それ以上喋るな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)

    def lambda_23C9():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_23C9)
    WaitChrThread(0x104, 2)
    Sleep(500)

    def lambda_23E9():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_23E9)
    WaitChrThread(0x104, 2)
    Sleep(500)

    #C0061
    ChrTalk(
        0x101,
        "#00005F……ランディ……\x02",
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
            "#12P#04601Fダサ……\x01",
            "ちょっとショックだなぁ。\x02\x03",

            "#04606Fこれでも昔はランディ兄に\x01",
            "憧れてたこともあったのにさー。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "#04504F#11P……クク。\x01",
            "そのくらいにしておけ。\x02\x03",

            "#04500F今夜は帰るぞ、シャーリィ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        "#12P#04600Fん、分かった。\x02",
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

    def lambda_259C():
        OP_95(0xFE, -2200, 0, 24800, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_259C)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_6F(0x1)
    SetCameraDistance(13500, 15000)
    OP_C9(0x0, 0x80000000)

    #C0066
    ChrTalk(
        0x8,
        (
            "#11P#04503F#3836V#30Wその姿、兄貴が見たら\x01",
            "どう思うかよく考えてみろ。\x02\x03",

            "#3837Vそれ以上無様をさらす前に\x01",
            "従うか、逃げるか、\x01",
            "抗うか決めるがいい。\x02\x03",

            "#04502F#3838V#40W───さもなくば、死ね。\x02",
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
            "#04609F#12P#N#3947V#30Wふふっ、おやすみランディ兄♪\x02\x03",

            "#04602F#3948Vお兄さんたちもまたね～！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF6C)
    OP_C9(0x1, 0x80000000)
    OP_68(-700, 1300, 20300, 4000)
    SetCameraDistance(17500, 4000)
    OP_93(0x9, 0x2, 0xBE)

    def lambda_277E():
        OP_95(0xFE, 2500, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_277E)
    Sleep(300)

    def lambda_279B():
        OP_95(0xFE, -2300, 0, 10400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_279B)
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
            "#11P#00316F#40Wったく、お嬢たちを\x01",
            "連れて来なくてよかったぜ……\x02\x03",

            "#00315F……さすがにカッコ悪すぎだろ……\x02",
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
        "#6P#00008Fランディ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(150)

    #C0072
    ChrTalk(
        0x104,
        (
            "#11P#00306F#30W……すまねえな。\x02\x03",

            "#00308F無様なところを\x01",
            "見せちまったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#6P#00006F……そんな風に言うなよ。\x02\x03",

            "#00013Fどう考えても……\x01",
            "おかしいのは彼らの方だろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、でもそこまで\x01",
            "ヘコんでるところを見ると──\x02\x03",

            "#10300F意外と図星だったみたいだね？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0075
    ChrTalk(
        0x101,
        "#11P#00007Fワジ……！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    #Sound(2375, 255, 100, 0)    #voice#Randy

    #C0076
    ChrTalk(
        0x104,
        "#11P#00312F#40Wクク……イヤな野郎だ。\x02",
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
            "#11P#00313F#40W#25Aああ……そうだ。\x02\x03",

            "#50W#42Aこの上もなく図星で……\x01",
            "痛いところを突かれちまった。\x02",
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
            "──その後、ロイドたちは\x01",
            "車を手配しようとする支配人の\x01",
            "申し出を断ってから帰途についた。\x02\x03",

            "心配そうに待っていた女性陣と\x01",
            "セルゲイに無事な姿を見せ……\x02\x03",

            "眠そうなキーアを寝かしつけてから\x01",
            "ロイドたちは事の顛末#4Rてんまつ#を報告した。\x07\x00\x02",
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

    def Function_12_2C34(): pass

    label("Function_12_2C34")

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
            "#1P#00303F……ってことでな。\x01",
            "俺たちの立ち入りを\x01",
            "許可してもらいたい。\x02\x03",

            "#00301Fもちろん、叔父貴や\x01",
            "シャーリィには内緒でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x14,
        (
            "……久々に顔を合わせたと思えば\x01",
            "そんな野暮用を頼まれるとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x14,
        (
            "クク、ランドルフ隊長……\x01",
            "あんた、お嬢が言ってた通り\x01",
            "腑抜けちまったんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        "#1P#00303F……その呼び方は止めろ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_END)), "loc_2F3C")

    #C0083
    ChrTalk(
        0x101,
        (
            "#00001F（『赤い星座』の猟兵……\x01",
            "　以前クリムゾン商会前で会ったのと\x01",
            "　同じ人物みたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F82")

    label("loc_2F3C")


    #C0084
    ChrTalk(
        0x101,
        (
            "#00001F（赤い星座の猟兵……\x01",
            "　ランディの知ってる顔みたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F82")


    #C0085
    ChrTalk(
        0x13,
        "（ゴ、ゴクリ……）\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x14,
        (
            "……クク、まあ\x01",
            "他ならぬあんたの頼みだ。\x01",
            "協力はさせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x14,
        (
            "とは言っても、店内で起こる\x01",
            "ちょっとしたトラブルに\x01",
            "目を瞑るって程度だがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x14,
        (
            "あんたが来たってことも、\x01",
            "副団長やお嬢には黙っとく。\x01",
            "……それでいいんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        "#1P#00303F……十分だ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x10E, 0x1F4)
    Sleep(100)

    #C0090
    ChrTalk(
        0x104,
        (
            "#1P#00300Fつーわけで、お膳立ては整った。\x02\x03",

            "#00300F夫人たちはまだ来てねえみてえだが、\x01",
            "待ち伏せするつもりなら\x01",
            "先に入っといたほうがいいだろう。\x02\x03",

            "#00303F流石に俺は遠慮させてもらうが。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00000Fああ、人数は最低限に\x01",
            "絞ったほうがよさそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x13,
        (
            "わ、私はもちろん入るから、\x01",
            "残りは君たちで決めたまえ！\x02",
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

    def lambda_326F():
        TurnDirection(0x101, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_326F)
    Sleep(50)

    def lambda_327F():
        TurnDirection(0x102, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_327F)
    Sleep(50)

    def lambda_328F():
        TurnDirection(0x103, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_328F)
    Sleep(50)

    def lambda_329F():
        TurnDirection(0x109, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_329F)
    Sleep(50)

    def lambda_32AF():
        TurnDirection(0x105, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_32AF)

    #C0093
    ChrTalk(
        0x109,
        "#10111F（すごく張り切ってますね……）\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        (
            "#00206F（正直、ここまで来てしまって\x01",
            "  後に引けなくなってるんでしょうが……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(50)

    #C0095
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、それじゃあ僕も入ろうかな。\x02\x03",

            "#10300F副局長さんとロイドと僕。\x01",
            "この３人で大丈夫じゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        "#1P#00300Fああ、まあそんな所だろう。\x02",
    )

    CloseMessageWindow()

    def lambda_33D6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_33D6)
    Sleep(50)

    def lambda_33E6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_33E6)
    Sleep(50)

    def lambda_33F6():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_33F6)

    #C0097
    ChrTalk(
        0x102,
        (
            "#00100Fそれじゃあ、\x01",
            "私たちは待機しているわね。\x02\x03",

            "万が一のことがあったら\x01",
            "エニグマで呼んでちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#00004Fああ、分かった。\x02\x03",

            "#00000Fそれじゃあさっそく\x01",
            "入るとしましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x13,
        "うむっ……い、行くぞ諸君！！\x02",
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
            "#00000F一応、夫人たちが来たら\x01",
            "すぐそこの席に案内してもらう\x01",
            "手筈になっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x13,
        (
            "う、うむ。\x01",
            "結構じゃないかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x13,
        (
            "悪徳不動産業者め……\x01",
            "私が絶対捕まえてくれる！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1194)

    #C0103
    ChrTalk(
        0x105,
        (
            "#10309Fフフ、なんだか\x01",
            "ワクワクしてきたね。\x02\x03",

            "#10305F……っと。\x01",
            "そうこうしているうちに\x01",
            "きたみたいだよ。\x02",
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

    def lambda_3821():
        OP_9B(0x0, 0x11, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3821)
    Sleep(300)

    def lambda_3839():
        OP_9B(0x0, 0x12, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3839)
    WaitChrThread(0x11, 1)

    def lambda_3852():
        OP_95(0x11, -2000, 0, -5940, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3852)
    WaitChrThread(0x12, 1)

    def lambda_3870():
        OP_93(0x12, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3870)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0x10E, 0x1F4)
    OP_6F(0x1)
    OP_0D()
    Sleep(500)

    #C0104
    ChrTalk(
        0x11,
        (
            "あの、予約していた\x01",
            "クライドですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x16,
        "どうぞ、あちらへ。\x02",
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
        "フフ、なかなかいいお店ね。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x11,
        (
            "おや、マーガレットさん……\x01",
            "こういった場所は始めてですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x11,
        (
            "てっきり警察キャリアの旦那様と\x01",
            "色々な場所に顔を出しているのかと。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x1)

    #C0109
    ChrTalk(
        0x12,
        "オホホ、冗談はやめて頂戴。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x12,
        (
            "たかが警察の副局長ごときじゃ\x01",
            "給料なんてたかが知れてるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x12,
        (
            "私とお洒落な店に行くよりも、\x01",
            "場末のバーでホステスと飲むほうが\x01",
            "あの人の性に合ってるのよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    #C0112
    ChrTalk(
        0x11,
        "はは、これは失礼しました。\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0113
    ChrTalk(
        0x11,
        (
            "それじゃあ、昼間ですが\x01",
            "景気付けにカクテルでも\x01",
            "おごらせていただきますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x12,
        "フフ……いただくわね。\x02",
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
            "#00012F（ふ、副局長。\x01",
            "  気にしないほうが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x13,
        (
            "（う、うるさいっ……\x01",
            "  気を使わないでくれたまえ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x13,
        (
            "（フン、ああそうさ。\x01",
            "  どうせ私の薄給じゃ\x01",
            "  こんな高級な店には来れない。）\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x13,
        (
            "（私には場末のバーがお似合いさ。\x01",
            "  それの何が悪いと言うんだ……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0119
    ChrTalk(
        0x105,
        "#10300F（すっかりイジケちゃったね。）\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        "#00006F（だ、大丈夫かホント……）\x02",
    )

    CloseMessageWindow()
    OP_68(-5840, 1500, 14140, 2000)
    OP_6F(0x1)
    Sleep(500)

    #C0121
    ChrTalk(
        0x11,
        "それでは、早速ですがこちらを。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0122
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クライドは契約書らしき書類を\x01",
            "アタッシュケースから取り出した。\x07\x00\x02",
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
            "奥様がご所望されている、\x01",
            "ミシュラムの一等地にある\x01",
            "別荘の契約書です。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x11,
        (
            "あとはこちらに\x01",
            "サインしていただければ、\x01",
            "あの屋敷は貴女のものですよ。\x02",
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
            "ホホ……\x01",
            "ついにこのときが来たのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x12,
        "もちろんサインさせていただくわ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(100)

    #C0127
    ChrTalk(
        0x101,
        (
            "#00001F（やっぱり、ミシュラムの\x01",
            "  別荘の取引きだったみたいだな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x105,
        (
            "#10300F（さて、ここからどうする？）\x02\x03",

            "#10304F（踏み込むにしても、\x01",
            "  もう少し話を聞いてからでも……）\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x13)

    #C0129
    ChrTalk(
        0x13,
        "……わ……わ……\x02",
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
            "#4S私のワイフを騙すのは\x01",
            "やめてもらおうかっ！！\x02",
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
        "えっ……！？\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x12,
        "……あなた……！？\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#00011F（わわっ……！？）\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x105,
        "#10306F（あちゃー。）\x02",
    )

    CloseMessageWindow()

    def lambda_4122():
        OP_95(0x101, -820, 0, 18700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4122)
    Sleep(200)

    def lambda_413F():
        OP_95(0x105, -820, 0, 18700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_413F)
    WaitChrThread(0x101, 1)

    def lambda_415D():
        OP_95(0x101, -1590, 0, 11760, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_415D)
    WaitChrThread(0x105, 1)

    def lambda_417B():
        OP_95(0x105, -1710, 0, 13690, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_417B)
    WaitChrThread(0x105, 1)

    def lambda_4199():
        TurnDirection(0x105, 0x12, 1000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4199)
    Sleep(100)
    WaitChrThread(0x101, 1)

    def lambda_41AD():
        TurnDirection(0x101, 0x12, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41AD)
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
        "あなた……これはどういうこと？\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0136
    ChrTalk(
        0x13,
        (
            "#4Sマーガレット！！\x01",
            "こんな取引きは止めなさい！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0137
    ChrTalk(
        0x13,
        (
            "#4Sこの悪徳不動産業者は、\x01",
            "お前を騙そうとしているんだっ！\x02",
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
            "ええええっ！？\x01",
            "ちょ、ちょっと待って下さい！！\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x11,
        (
            "悪徳……って、\x01",
            "わ、私が一体何をしたと……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0140
    ChrTalk(
        0x13,
        (
            "#4Sええい、黙りたまえ！\x01",
            "ネタは上がっているんだっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x12,
        "……あなた……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0142
    ChrTalk(
        0x13,
        (
            "#4S私のワイフを口先三寸で騙して、\x01",
            "ムチャなローンを組まそうと\x01",
            "していたんだろう！？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x12,
        "……あなた……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0144
    ChrTalk(
        0x13,
        (
            "#4Sだが、そうは問屋が卸さんぞっ！\x01",
            "この私の目が黒いうちは……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x12,
        "……あなたったら……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0146
    ChrTalk(
        0x13,
        (
            "#4Sええい、お前はだまっていなさい！\x01",
            "私は警察の副局長として……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x1450)

    #C0147
    ChrTalk(
        0x12,
        "#800W#5Sお　黙　り　な　さ　い　。\x02",
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
        "#2S……ごめんなさい。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 500)
    Sleep(50)

    #C0149
    ChrTalk(
        0x101,
        "#00011F（よ、弱っ！？）\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x105,
        "#10309F（アハハ、完全に黙らされちゃったね。）\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x12,
        (
            "まったく……\x01",
            "あなたと言う人は本当に\x01",
            "どうしようもない人ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x12,
        (
            "警察の副局長ともあろう者が、\x01",
            "早とちりして罪もない人を\x01",
            "犯罪者扱いなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0153
    ChrTalk(
        0x12,
        "#4S恥ずかしいとは思わないのっ！？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x13,
        (
            "ひいっ！！\x01",
            "すみません、もうしません！\x02",
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
        "って、勘違い……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12, 500)
    Sleep(50)

    #C0156
    ChrTalk(
        0x101,
        "#00011Fええええっ！！？？\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x105,
        (
            "#10300Fマダム、できれば詳しく\x01",
            "事情を聞かせてもらえるかな？\x02",
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
        "#3Pふう……まあ、いいでしょう。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x12,
        (
            "#3Pまず断っておくけれど、\x01",
            "このクライドさんは高級物件を扱う\x01",
            "真っ当な不動産業者さんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x12,
        (
            "#3Pあなたのいうような、\x01",
            "悪徳商人なんかでは決してないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x13,
        (
            "だ、だが、そうだとしても……\x01",
            "ウチに高級物件を買う資金なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x12,
        (
            "#3P実は私、先日暇つぶしに始めた株で\x01",
            "かなりの儲けを出したのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x12,
        (
            "#3Pそれこそ、あなたが何年もかかって\x01",
            "やっと貯めるようなミラをね。\x02",
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
        "カ、カブ……！？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x12,
        (
            "#3P正直に言って……\x01",
            "……あなたという人には、\x01",
            "ほとほと愛想が尽きてたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x12,
        (
            "#3Pコネと運でたまたま手に入れた\x01",
            "地位に踏ん反りかえってるくせに、\x01",
            "家では私に頭が上がらない情けなさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x12,
        (
            "#3P家にいづらくなったか知らないけど、\x01",
            "スキあらば一晩中飲みにいって\x01",
            "家計を圧迫する無計画さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x13,
        "ううっ……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x12,
        (
            "#3P局長が失脚した時には\x01",
            "あなた、自分が次期局長になるなんて\x01",
            "しばらく上機嫌だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x12,
        (
            "#3Pだけど結局、もう１人の副局長に\x01",
            "そのポストを取られてしまう体たらく。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x12,
        (
            "#3Pしかもその事で不機嫌になって\x01",
            "グチグチグチグチ文句ばかり……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#00012Fお、奥さん、その辺で……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x12,
        (
            "#3P……それで正直、\x01",
            "これ以上一緒に住むのは\x01",
            "無理だと感じていたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x12,
        (
            "#3Pだから、株で手に入れたミラで\x01",
            "別居用の屋敷を買おうと、\x01",
            "クライドさんに相談していたわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x12,
        (
            "#3Pしばらくはそっちで暮らして、\x01",
            "ゆくゆくは離婚届けに\x01",
            "判を押してもらうつもりだったわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0176
    ChrTalk(
        0x13,
        "#4Sガーン！！\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        "#10309Fアハハ、容赦ないなあ。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#00006F（さ、さすがに可哀想すぎる……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0179
    ChrTalk(
        0x101,
        (
            "#00005Fあれ、でも……\x01",
            "『だった』ってことは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x13,
        "……え……\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x12,
        (
            "#3P……ふふ、そうね。\x01",
            "まあ、私を心配してここまで\x01",
            "やってきたことは買いましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x12,
        (
            "#3P私にビクビクしてばかりで\x01",
            "家に帰るのを避けていた、\x01",
            "あなたにしては上出来だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x12,
        (
            "#3P今日のところは家に帰って、\x01",
            "改めて話し合うことにしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x13,
        "マ、マーガレット……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 500)
    Sleep(50)

    #C0185
    ChrTalk(
        0x12,
        (
            "#3P……と、言うわけでクライドさん。\x01",
            "今回の別荘購入の件は\x01",
            "一旦保留にしていただけるかしら。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 500)
    Sleep(50)

    #C0186
    ChrTalk(
        0x11,
        (
            "#3Pそ、そんなマーガレットさん！\x01",
            "ここまで交渉を進めておいて……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x12,
        "#3Pあくまで“保留”よ。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x12,
        (
            "#3P私も１人で勝手に\x01",
            "進めていたのは悪かったし、\x01",
            "改めて話し合おうと思って。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x12,
        (
            "#3P大丈夫、別居はしないけど\x01",
            "物件を気に入ったのは本当だから\x01",
            "きっと買わせていただくわ。\x02",
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
            "#3Pふう、できれば今日中に\x01",
            "いい返事を頂きたかったですが……\x01",
            "仕方ありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x11,
        "#3Pそれでは私は失礼します……\x02",
    )

    CloseMessageWindow()
    OP_68(-5570, -600, 15480, 2000)

    def lambda_5123():
        OP_95(0x11, -2680, 0, 14150, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5123)
    Sleep(500)

    def lambda_5140():
        OP_93(0x12, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5140)

    def lambda_514D():
        OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_514D)
    Sleep(100)

    def lambda_5165():
        OP_9B(0x1, 0x105, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5165)
    Sleep(100)

    def lambda_517D():
        OP_9B(0x1, 0x13, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_517D)
    WaitChrThread(0x11, 1)
    OP_6F(0x1)
    Sleep(50)

    def lambda_519B():
        OP_9B(0x0, 0x11, 0x5A, 0x2710, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_519B)
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
            "#00001Fうーん、結局あの人は\x01",
            "無実だったんだよな……\x02\x03",

            "#00006Fなんだか悪い事しちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、まあいいじゃない。\x01",
            "副局長と奥さんについては\x01",
            "ひとまず一件落着みたいだしさ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 500)
    Sleep(50)

    #C0194
    ChrTalk(
        0x12,
        (
            "#3P……それじゃ、あなた。\x01",
            "私も今日は家に帰るとするわ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5313():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5313)
    Sleep(50)

    def lambda_5323():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5323)
    Sleep(50)

    def lambda_5333():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5333)

    #C0195
    ChrTalk(
        0x12,
        (
            "#3P色々と話をしたいから、\x01",
            "今夜はまっすぐ家に帰ってくること。\x01",
            "……分かったわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0196
    ChrTalk(
        0x13,
        "……は、はいっ！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0197
    ChrTalk(
        0x101,
        "#00006F（……大丈夫かなあ……）\x02",
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

    # Function_12_2C34 end

    def Function_13_541B(): pass

    label("Function_13_541B")

    Fade(500)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -7060, 0, 13990, 90)
    Return()

    # Function_13_541B end

    def Function_14_543F(): pass

    label("Function_14_543F")

    Fade(500)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -7490, 0, 13110, 90)
    Return()

    # Function_14_543F end

    SaveToFile()

Try(main)
