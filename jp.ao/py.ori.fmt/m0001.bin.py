from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0001.bin",                # FileName
        "m0001",                    # MapName
        "m0001",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0001",                  # 0
        "声",                     # 1
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(188, 0)                                        # 0

    ScpFunction((
        "Function_0_BC",           # 00, 0
        "Function_1_CC",           # 01, 1
        "Function_2_CD",           # 02, 2
    ))


    def Function_0_BC(): pass

    label("Function_0_BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_CB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_CB")

    Return()

    # Function_0_BC end

    def Function_1_CC(): pass

    label("Function_1_CC")

    Return()

    # Function_1_CC end

    def Function_2_CD(): pass

    label("Function_2_CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    LoadChrToIndex("apl/ch51400.itc", 0x1E)
    LoadChrToIndex("apl/ch51401.itc", 0x1F)
    LoadEffect(0x0, "map/mpcave2.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SoundLoad(803)
    OP_68(199890, 1100, 199470, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, 199500, 150, 199500, 270)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x8, 0x5A, 0x5A, 0x5A, 0xFF, 0x0)
    OP_7D(0xEB, 0xD2, 0xD2, 0x0, 0x0)
    PlayEffect(0x0, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(945, 0, 50, 0)
    Sleep(1600)
    Sound(945, 0, 30, 0)
    Sleep(1200)
    PlayBGM("ed7571", 0)
    SetCameraDistance(15000, 7000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    #Sound(3577, 255, 50, 0)    #voice#Wald
    OP_6F(0x79)
    SetCameraDistance(13000, 50000)

    #C0001
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#50W#11P……こりゃあいい…………\x01",
            "…………コイツは最高だ…………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0002
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#50W#11Pクク……これなら絶対に……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0003
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#50W#11P絶対に“ヤツ”を──！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(803, 2, 100, 0)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11Pチッ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_68(199050, 1000, 199350, 800)
    SetChrSubChip(0x8, 0x1)
    SetChrPos(0x8, 199000, 0, 199500, 270)
    OP_0D()
    SetChrSubChip(0x8, 0x2)
    Sound(812, 0, 100, 0)
    Sleep(300)
    SetChrSubChip(0x8, 0x3)
    Sleep(500)

    #C0005
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#11Pああ……アンタか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0006
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#11P……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0007
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#11P……ああ……ああ………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0008
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#11P問題ねぇ……\x01",
            "クク……いつでも行ける……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(199000, 1500, 199500, 7000)
    OP_82(0x14, 0x14, 0xBB8, 0x1B58)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_42C():
        OP_A0(0xFE, 900, 0x0, 0x1F)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_42C)
    Sound(889, 0, 40, 0)
    Sleep(3000)
    FadeToDark(4000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声")

    #A0009
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#11P……ただし……\x01",
            "やり方は俺に任せてもらうぜ？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x323)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    ReplaceBGM(-1, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x23, 0)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_CD end

    SaveToFile()

Try(main)
