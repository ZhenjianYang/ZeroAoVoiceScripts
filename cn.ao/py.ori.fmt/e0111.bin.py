from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e0111.bin",                # FileName
        "e0111",                    # MapName
        "e0111",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e0111",                  # 0
        "谢莉",                   # 1
        "猎兵加雷斯",             # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(220, 0)                                        # 0

    ScpFunction((
        "Function_0_DC",           # 00, 0
        "Function_1_EC",           # 01, 1
        "Function_2_ED",           # 02, 2
        "Function_3_112",          # 03, 3
    ))


    def Function_0_DC(): pass

    label("Function_0_DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_EB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)

    label("loc_EB")

    Return()

    # Function_0_DC end

    def Function_1_EC(): pass

    label("Function_1_EC")

    Return()

    # Function_1_EC end

    def Function_2_ED(): pass

    label("Function_2_ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_111")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_2_ED")

    label("loc_111")

    Return()

    # Function_2_ED end

    def Function_3_112(): pass

    label("Function_3_112")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51201.itc", 0x1E)
    LoadChrToIndex("apl/ch51261.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    SoundLoad(460)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 52800, 100, -200, 270)
    SetChrPos(0x104, 52100, 200, 350, 180)
    SetChrPos(0x105, 52800, 100, -1100, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 50400, 150, 350, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 47800, 100, 700, 0)
    BeginChrThread(0x101, 3, 0, 2)
    OP_68(44700, 1100, 0, 0)
    MoveCamera(319, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17100, 0)
    Sound(460, 2, 100, 0)
    OP_68(50700, 1100, 0, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    #Sound(2428, 255, 100, 0)    #voice#Lazy
    Sleep(800)

    #C0001
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，真是相当豪华。\x02\x03",

            "猎兵生意竟然\x01",
            "这么赚钱啊？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    Sleep(300)

    #C0002
    ChrTalk(
        0x8,
        (
            "#04600F#5P嗯……我们比较特别吧。\x02\x03",

            "#04604F我们的主顾中有很多资产家和大贵族，\x01",
            "经常能接到一千万米拉左右的生意呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x105,
        "#12P#10305F哟¤\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#12P#00011F竟然如此……\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00303F……不过要想笼络住数量众多的顶级猎兵，\x01",
            "也需要相当高的费用。\x02\x03",

            "#00301F武装方面，自然也要采购最新型的用品──\x01",
            "说不定现在连飞艇都买了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#04604F#5P啊哈哈，那倒是还没有。\x02\x03",

            "#04602F要论坚固程度，\x01",
            "首选自然还是利贝尔的军用飞艇，\x01",
            "但那种飞艇都不会流通到黑市呢。\x02\x03",

            "#04609F算啦，万一遇到什么紧急情况，\x01",
            "去抢几架就是了¤\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0007
    ChrTalk(
        0x101,
        "#12P#00008F（……是在开玩笑吧？）\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x104,
        "#00306F（你就当做是吧。）\x02",
    )

    CloseMessageWindow()
    StopSound(460, 2000, 100)
    OP_68(53000, 1100, 0, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetScenarioFlags(0x22, 2)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_112 end

    SaveToFile()

Try(main)
