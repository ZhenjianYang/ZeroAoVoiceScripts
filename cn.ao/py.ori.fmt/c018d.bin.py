from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c018d.bin",                # FileName
        "c018d",                    # MapName
        "c018d",                    # Location
        0x0005,                     # MapIndex
        "ed7571",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "c018d",                  # 0
        "小丑肯帕雷拉",           # 1
        "阿瑞安赫德",             # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(216, 0)                                        # 0

    ScpFunction((
        "Function_0_D8",           # 00, 0
        "Function_1_E8",           # 01, 1
        "Function_2_E9",           # 02, 2
    ))


    def Function_0_D8(): pass

    label("Function_0_D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_E7")

    Return()

    # Function_0_D8 end

    def Function_1_E8(): pass

    label("Function_1_E8")

    Return()

    # Function_1_E8 end

    def Function_2_E9(): pass

    label("Function_2_E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadChrToIndex("chr/ch04200.itc", 0x1F)
    LoadChrToIndex("apl/ch51516.itc", 0x20)
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 350000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundLoad(3882)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04901.itp")
    SoundLoad(868)
    SoundLoad(900)
    SetChrPos(0x0, 10000, 0, 1000, 0)
    SetChrPos(0x1, 10000, 0, 1000, 0)
    SetChrPos(0x2, 10000, 0, 1000, 0)
    SetChrPos(0x3, 10000, 0, 1000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -5200, -200, 7100, 45)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -3500, -200, 7100, 0)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-2080, 1500, 32950, 0)
    MoveCamera(17, 2, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(20610, 0)
    Sound(868, 2, 50, 0)
    OP_68(-4410, 1500, 15860, 6000)
    MoveCamera(37, 16, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(22870, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-4470, 4500, 9330, 0)
    OP_68(-4470, 1500, 9330, 4000)
    MoveCamera(51, 5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x8,
        (
            "#6P#04809F啊哈哈，好漂亮。\x02\x03",

            "金融都市克洛斯贝尔的象征\x01",
            "就这样付之一炬了。\x02\x03",

            "#04802F话说回来，『赤色星座』……\x02\x03",

            "就算是我们的强化猎兵，\x01",
            "恐怕也无法和他们抗衡。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x9,
        "#11P#04920F#30W………………………………\x07\x00\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    Sleep(300)

    #C0003
    ChrTalk(
        0x8,
        (
            "#04804F#6P呵呵……\x02\x03",

            "#04800F这种行为，终究有些\x01",
            "违背你的原则吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "#11P#04923F#30W……是啊。\x02\x03",

            "#04920F但战争原本就是无情的。\x02\x03",

            "他们也只是遵循着自己的原则，\x01",
            "驰骋于战场而已。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "#04804F#6P呵呵，原来如此。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(900, 2, 100, 0)
    Sleep(300)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(150)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    Sound(901, 0, 100, 0)
    OP_24(0x384)
    Sleep(300)
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0006
    ChrTalk(
        0x8,
        (
            "#5P#04800F啊，博士，\x01",
            "突然联络，有什么事吗？\x02\x03",

            "#04805F……哎？\x01",
            "已经完成一台机体了？\x02\x03",

            "#04806F好的好的，明白了，\x01",
            "我这就回去帮忙。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sound(901, 0, 100, 0)
    Sleep(300)
    Sound(802, 0, 100, 0)
    Fade(250)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    TurnDirection(0x8, 0x9, 500)
    Sleep(150)

    #C0007
    ChrTalk(
        0x8,
        (
            "#04804F#6P……情况就是这样，\x01",
            "我就暂时失陪啦。\x02\x03",

            "#04802F在『约定之日』到来之前，\x01",
            "就由你来负责见证了？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        "#11P#04923F#30W嗯，没有问题。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0009
    AnonymousTalk(
        0x9,
        (
            "#3882V#40W降临于此地的命运……\x01",
            "就让我来亲眼见证吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF2A)
    OP_C9(0x1, 0x80000000)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    StopSound(868, 2000, 50)
    SetCameraDistance(11500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x23B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x364)
    OP_24(0x384)
    SetScenarioFlags(0x22, 6)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E9 end

    SaveToFile()

Try(main)
