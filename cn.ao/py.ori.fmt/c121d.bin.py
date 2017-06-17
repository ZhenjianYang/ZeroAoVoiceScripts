from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c121d.bin",                # FileName
        "c121d",                    # MapName
        "c121d",                    # Location
        0x0021,                     # MapIndex
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
        "c121d",                  # 0
        "猎兵",                   # 1
        "猎兵",                   # 2
        "战鬼西格蒙德",           # 3
        "黑月成员",               # 4
        "黑月成员",               # 5
        "曹",                     # 6
        "偃月轮",                 # 7
        "SE控制",                 # 8
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(436, 0)                                        # 0

    ScpFunction((
        "Function_0_1B4",          # 00, 0
        "Function_1_1C4",          # 01, 1
        "Function_2_1C5",          # 02, 2
        "Function_3_12C5",         # 03, 3
        "Function_4_12DD",         # 04, 4
        "Function_5_13A4",         # 05, 5
        "Function_6_1543",         # 06, 6
        "Function_7_156C",         # 07, 7
        "Function_8_162E",         # 08, 8
        "Function_9_165A",         # 09, 9
        "Function_10_1710",        # 0A, 10
        "Function_11_1768",        # 0B, 11
        "Function_12_18B5",        # 0C, 12
        "Function_13_1A1C",        # 0D, 13
        "Function_14_1A64",        # 0E, 14
        "Function_15_1AAC",        # 0F, 15
    ))


    def Function_0_1B4(): pass

    label("Function_0_1B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1C3")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_1C3")

    Return()

    # Function_0_1B4 end

    def Function_1_1C4(): pass

    label("Function_1_1C4")

    Return()

    # Function_1_1C4 end

    def Function_2_1C5(): pass

    label("Function_2_1C5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    LoadChrToIndex("apl/ch51535.itc", 0x23)
    LoadChrToIndex("chr/ch03350.itc", 0x24)
    LoadChrToIndex("chr/ch03352.itc", 0x25)
    LoadChrToIndex("chr/ch03356.itc", 0x26)
    LoadChrToIndex("chr/ch41950.itc", 0x28)
    LoadChrToIndex("chr/ch41951.itc", 0x29)
    LoadChrToIndex("chr/ch06300.itc", 0x2D)
    LoadChrToIndex("apl/ch51515.itc", 0x2E)
    LoadChrToIndex("chr/ch31500.itc", 0x32)
    LoadChrToIndex("chr/ch31551.itc", 0x33)
    LoadChrToIndex("chr/ch31552.itc", 0x34)
    LoadChrToIndex("chr/ch31553.itc", 0x35)
    LoadChrToIndex("chr/ch31556.itc", 0x36)
    LoadChrToIndex("chr/ch12500.itc", 0x37)
    LoadChrToIndex("chr/ch12551.itc", 0x38)
    LoadChrToIndex("chr/ch12552.itc", 0x39)
    LoadChrToIndex("chr/ch12553.itc", 0x3A)
    LoadChrToIndex("chr/ch12556.itc", 0x3B)
    LoadEffect(0x0, "event/ev15036.eff")
    LoadEffect(0x1, "event/ev15040.eff")
    LoadEffect(0x2, "event/eva01_01.eff")
    LoadEffect(0x3, "event/ev15037.eff")
    LoadEffect(0x4, "battle/ms00001.eff")
    LoadEffect(0x5, "battle/cr033000.eff")
    LoadEffect(0x6, "event/ev15038.eff")
    LoadEffect(0x7, "event/ev15039.eff")
    LoadEffect(0x8, "event\\ev307_00.eff")
    SoundLoad(868)
    SoundLoad(926)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x29)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xB, 0x36)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x39)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xE, 0x20)
    SetChrChipByIndex(0xE, 0x36)
    SetChrSubChip(0xE, 0x10)
    SetMapObjFrame(0xFF, "ato_yuka01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_yuka02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_yuka03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_mado", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_tukue", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_nuki03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage04", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0xB, -73500, 0, 600, 180)
    SetChrPos(0xC, -74350, 0, 1750, 180)
    SetChrPos(0xE, -74350, 0, 1750, 180)
    SetChrPos(0xA, -74150, -4000, -9450, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4A3():
        OP_95(0xFE, -74000, -4000, -6450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4A3)

    def lambda_4BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_4BD)
    OP_68(-74150, -3000, -9450, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    OP_68(-74150, -3000, -6450, 1750)
    SetCameraDistance(22000, 1750)
    Sound(868, 2, 20, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0xBB8)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 3)
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x5)
    Sound(531, 0, 80, 0)
    Sound(538, 0, 80, 0)
    BeginChrThread(0xE, 1, 0, 4)
    BeginChrThread(0xB, 1, 0, 5)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xB, 1)

    #C0001
    ChrTalk(
        0xA,
        "#04512F#12P没用的。\x02",
    )

    CloseMessageWindow()
    OP_68(-74150, -500, -2390, 500)
    MoveCamera(51, 12, 5, 500)
    OP_6E(300, 500)
    SetCameraDistance(37250, 500)
    OP_6F(0x79)
    Sound(4132, 255, 100, 0)    #voice#Sigmund
    Sound(893, 0, 100, 0)
    Sound(538, 0, 100, 0)
    Sound(926, 2, 100, 0)
    OP_A1(0xA, 0x9C4, 0x4, 0x0, 0x0, 0x0, 0x1)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    PlayEffect(0x3, 0xFF, 0xA, 0x0, 0, -700, 0, 0, -45, 180, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrSubChip(0xA, 0x1)
    Sleep(50)
    PlayEffect(0x3, 0xFF, 0xA, 0x0, 0, 700, 0, 0, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrChipByIndex(0xB, 0x35)
    Sound(501, 0, 100, 0)
    BeginChrThread(0xB, 0, 0, 10)
    Sound(809, 0, 100, 0)

    def lambda_669():
        OP_9D(0xFE, 0xFFFEE0E4, 0x0, 0x640, 0xFA, 0xFA0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_669)

    #C0002
    ChrTalk(
        0xB,
        "#5P#10A哇……\x02",
    )
    #Auto

    Sleep(100)
    SetChrChipByIndex(0xC, 0x3A)
    Sound(501, 0, 100, 0)
    BeginChrThread(0xC, 0, 0, 10)

    def lambda_6AB():
        OP_9D(0xFE, 0xFFFEDD92, 0x0, 0xABE, 0xFA, 0xFA0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6AB)

    #C0003
    ChrTalk(
        0xC,
        "#6P#10A……呜……\x02",
    )
    #Auto

    Sleep(1900)
    SetChrSubChip(0xA, 0x3)
    OP_24(0x39E)
    Sound(308, 0, 100, 0)
    Sound(538, 0, 100, 0)
    Sleep(500)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x23)
    ClearChrFlags(0xA, 0x4)

    def lambda_70C():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_70C)
    MoveCamera(40, 7, 5, 3000)
    SetCameraDistance(34250, 3000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xA, 0x1)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x34)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x39)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xB, -38800, 0, 5500, 180)
    SetChrPos(0xC, -35600, 0, 3900, 225)
    SetChrPos(0xA, -38800, -1550, -1700, 0)
    ClearChrFlags(0xA, 0x4)

    def lambda_794():
        OP_95(0xFE, -38800, 0, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_794)
    OP_68(-38800, -1000, -1500, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(26300, 0)
    OP_68(-38800, 800, 1000, 1000)
    MoveCamera(45, 25, 0, 1000)
    SetCameraDistance(24300, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0xB, 0, 0, 6)
    BeginChrThread(0xC, 0, 0, 8)
    WaitChrThread(0xA, 1)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x3)
    Sleep(200)
    SetChrSubChip(0xA, 0x4)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(893, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xA, 0x5, 0, 750, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-37350, 800, 4900, 500)
    MoveCamera(45, 23, -5, 500)
    SetCameraDistance(26500, 500)
    EndChrThread(0xB, 0x0)
    BeginChrThread(0xB, 0, 0, 7)

    #C0004
    ChrTalk(
        0xB,
        "#5P#10A啊啊……！\x02",
    )
    #Auto

    Sleep(100)
    EndChrThread(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 9)
    WaitChrThread(0xC, 0)

    #C0005
    ChrTalk(
        0xC,
        "#5P真、真是不甘……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    Sleep(500)
    OP_68(-34500, 1000, 0, 2500)
    MoveCamera(45, 30, -5, 2500)
    SetCameraDistance(24000, 2500)
    SetChrChipByIndex(0xA, 0x23)
    OP_95(0xA, -36150, 0, 1000, 2000, 0x0)
    OP_95(0xA, -34950, 0, 0, 2000, 0x0)
    OP_93(0xA, 0x5A, 0x1F4)
    Sound(893, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x25)
    OP_A1(0xA, 0x7D0, 0x4, 0x0, 0x0, 0x0, 0x1)
    Sleep(50)
    SetChrSubChip(0xA, 0x2)
    PlayEffect(0x5, 0xFF, 0xA, 0x5, -1500, 0, 500, 0, 10, 270, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(880, 0, 100, 0)
    Sound(165, 0, 100, 0)
    Sound(196, 0, 80, 0)
    SetMapObjFrame(0x0, "c12dor52:Layer1(1)", 0x2, "アニメ")
    SetMapObjFrame(0x0, "c12dor52:Layer2(2)", 0x2, "アニメ")
    SetMapObjFrame(0x0, "c12dor52:Layer3(3)", 0x2, "アニメ")
    SetMapObjFrame(0x0, "c12dor52:Layer4(4)", 0x2, "アニメ")
    Sleep(1000)
    SetCameraDistance(23000, 2000)
    SetChrChipByIndex(0xA, 0x23)

    def lambda_A4F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A4F)

    def lambda_A64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_A64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xA, 0x1)
    EndChrThread(0xA, 0x3)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, -5000, 0, 0, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 5500, 0, 0, 270)
    ClearChrFlags(0xD, 0x80)
    OP_68(-5000, 1000, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23000, 0)

    def lambda_AF2():
        OP_95(0xFE, 1750, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_AF2)

    def lambda_B0C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_B0C)
    OP_68(4250, 1000, 0, 4000)
    SetCameraDistance(25000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 3)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0006
    AnonymousTalk(
        0xD,
        (
            "哎呀呀，真希望你们的\x01",
            "拜访能稍微安静一些啊。\x02",
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

    #C0007
    ChrTalk(
        0xA,
        (
            "#04504F#6P呵呵，没办法，毕竟还有\x01",
            "一些着急的工作在等着处理。\x02\x03",

            "#04500F话说回来，『白兰龙』，\x01",
            "确实该赞你一声名不虚传。\x02\x03",

            "只留下这么少的成员……\x01",
            "看来你已经预料到我们会来袭击了？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xD,
        (
            "#03203F#11P嗯，算是吧。\x02\x03",

            "#03200F我还没有愚蠢到\x01",
            "与你们这种战争狂人\x01",
            "正面冲突的程度。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xA,
        (
            "#04502F#6P哼哼，话虽如此，但你却\x01",
            "没有逃走，而是在这里等待……\x02\x03",

            "莫非是想与我\x01",
            "『战鬼』一战吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xD,
        (
            "#03204F#11P哈哈，怎么可能。\x02\x03",

            "不得不承认，在你面前，\x01",
            "即使是『银』大人也要甘拜下风。\x02\x03",

            "#03210F我只是想确认一件事情，\x01",
            "所以才会在这里等你。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xA,
        "#04505F#6P哦？想确认事情？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xD,
        (
            "#03209F#11P嗯，很简单。\x02\x03",

            "#03202F如今和你签署契约的人\x01",
            "究竟是谁？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "#04504F#6P哼哼……哈哈哈……\x02\x03",

            "#04512F看来你这家伙\x01",
            "确实有些能耐呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 3, 0, 11)
    BeginChrThread(0xD, 1, 0, 13)
    OP_68(4750, 1000, 0, 500)
    MoveCamera(35, 30, 0, 500)
    SetCameraDistance(22500, 500)
    Sleep(500)
    OP_82(0x190, 0x0, 0xBB8, 0x190)
    #Sound(4133, 255, 100, 0)    #voice#Sigmund

    #C0014
    ChrTalk(
        0xA,
        "#04507F#6P#5S#10A喝啊啊啊！\x02",
    )
    #Auto

    CloseMessageWindow()
    WaitChrThread(0xA, 3)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)
    BeginChrThread(0xA, 3, 0, 12)
    BeginChrThread(0xD, 1, 0, 14)
    OP_68(7250, 1000, 0, 500)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0015
    ChrTalk(
        0xD,
        "#03201F#7A哈……！\x02",
    )
    #Auto

    WaitChrThread(0xA, 3)
    WaitChrThread(0xD, 1)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x2E)
    SetChrSubChip(0xD, 0x0)
    SetChrChip(0x0, 0xD, 0x32, 0x12C)
    Sound(844, 0, 100, 0)

    def lambda_F86():
        OP_9D(0xFE, 0x2710, 0xFFFFEC78, 0xFFFFFF9C, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F86)
    Sleep(50)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)
    Sound(991, 0, 100, 0)
    Sound(833, 0, 50, 0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, 7900, 900, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMapObjFrame(0xFF, "mae_mado", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_mado", 0x1, 0x1)
    WaitChrThread(0xD, 1)
    SetChrChip(0x1, 0xD, 0x0, 0x0)
    SetChrFlags(0xD, 0x80)
    OP_6F(0x79)
    BeginChrThread(0xF, 1, 0, 15)
    OP_68(7450, 1000, -100, 1000)
    SetChrChipByIndex(0xA, 0x23)
    OP_95(0xA, 7450, 0, -100, 2000, 0x0)
    OP_93(0xA, 0x5A, 0x1F4)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    OP_6F(0x79)
    Sleep(500)

    #C0016
    ChrTalk(
        0xA,
        "#04504F#5P哼，逃走了啊。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, -3750, 0, 500, 90)
    SetChrPos(0x9, -3000, 0, -500, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    #N0017
    NpcTalk(
        0x8,
        "声音",
        "西格蒙德大人！\x02",
    )

    CloseMessageWindow()
    OP_68(5000, 1000, 0, 2000)
    MoveCamera(45, 18, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(23500, 2000)

    def lambda_1112():
        OP_95(0xFE, 1750, 0, -500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1112)
    Sleep(100)

    def lambda_112F():
        OP_95(0xFE, 1000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_112F)
    WaitChrThread(0x8, 1)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    OP_6F(0x79)

    #C0018
    ChrTalk(
        0xA,
        "#04500F#5P曹的部下怎么样了？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "#6P实在对不起，\x01",
            "虽然把他们打伤了，但是……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xA,
        (
            "#04504F#5P呵呵，跑掉了吗？\x02\x03",

            "#04500F算了，就让他们潜藏在黑暗中，\x01",
            "慢慢磨尖牙齿吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x10E, 0x1F4)
    Sleep(300)

    #C0021
    ChrTalk(
        0xA,
        (
            "#04502F#11P好，接下来就要\x01",
            "进入最终阶段了。\x02\x03",

            "将此处爆破，\x01",
            "然后向ＩＢＣ大楼进发。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("众猎兵")

    #A0022
    AnonymousTalk(
        0xFF,
        "#4S是！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopSound(868, 1000, 20)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c030B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1C5 end

    def Function_3_12C5(): pass

    label("Function_3_12C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12DC")
    OP_A0(0xFE, 5000, 0x10, 0x17)
    Jump("Function_3_12C5")

    label("loc_12DC")

    Return()

    # Function_3_12C5 end

    def Function_4_12DD(): pass

    label("Function_4_12DD")

    BeginChrThread(0xE, 0, 0, 3)
    Sound(637, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_9A(0xFE, 0xA, 0x1F4, 0x3A98, 0x0)
    StopEffect(0x0, 0x0)
    EndChrThread(0xE, 0x0)
    Sound(532, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(566, 0, 60, 0)
    Sound(196, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xA, 0x4, 0, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_96(0xFE, 0xFFFEDD60, 0xFFFFEE6C, 0xFFFFEED0, 0x3A98, 0x0)
    Return()

    # Function_4_12DD end

    def Function_5_13A4(): pass

    label("Function_5_13A4")

    Sound(241, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -73850, -1800, -2000, 180, 0, 0, 1000, 1000, 1000, 0xA, 0, 1000, 0, 0)
    Sleep(100)
    Sound(241, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -73850, -1800, -2000, 180, 0, 0, 1000, 1000, 1000, 0xA, 0, 1000, 0, 0)
    Sleep(100)
    Sound(241, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -73850, -1800, -2000, 180, 0, 0, 1000, 1000, 1000, 0xA, 0, 1000, 0, 0)
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xA, 0x4, 1000, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xA, 0x4, 0, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xA, 0x4, -1000, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_5_13A4 end

    def Function_6_1543(): pass

    label("Function_6_1543")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x2)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF6870, 0x1F4, 0x3E8, 0x2EE, 0xBB8)
    Return()

    # Function_6_1543 end

    def Function_7_156C(): pass

    label("Function_7_156C")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_15BB():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_15BB)
    OP_9D(0xFE, 0xFFFF66E0, 0x3E8, 0x1B58, 0x4B0, 0x1388)
    EndChrThread(0xFE, 0x3)
    Sound(196, 0, 80, 0)
    Sound(815, 0, 100, 0)

    def lambda_15FB():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_15FB)
    OP_96(0xFE, 0xFFFF66E0, 0x0, 0x1B58, 0xBB8, 0x0)
    SetChrSubChip(0xFE, 0x1)
    Sound(514, 0, 100, 0)
    Return()

    # Function_7_156C end

    def Function_8_162E(): pass

    label("Function_8_162E")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x38)
    OP_96(0xFE, 0xFFFF6870, 0x0, 0x3E8, 0x1388, 0x0)
    Sound(533, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_162E end

    def Function_9_165A(): pass

    label("Function_9_165A")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_16A3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_16A3)
    OP_9D(0xFE, 0xFFFF79D2, 0x3E8, 0x12C0, 0x4B0, 0x1388)
    EndChrThread(0xFE, 0x3)
    Sound(501, 0, 100, 0)

    def lambda_16DD():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_16DD)
    OP_96(0xFE, 0xFFFF79D2, 0x0, 0x12C0, 0xBB8, 0x0)
    SetChrSubChip(0xFE, 0x1)
    Sound(514, 0, 100, 0)
    Return()

    # Function_9_165A end

    def Function_10_1710(): pass

    label("Function_10_1710")

    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_10_1710 end

    def Function_11_1768(): pass

    label("Function_11_1768")

    SetChrFlags(0xFE, 0x20)
    Sound(893, 0, 100, 0)

    def lambda_1778():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1778)
    SetChrChipByIndex(0xA, 0x25)
    OP_A1(0xA, 0x7D0, 0x2, 0x0, 0x1)
    PlayEffect(0x5, 0xFF, 0xA, 0x5, -1500, 0, 500, 0, 10, 270, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 80, 0)
    Sound(165, 0, 100, 0)
    Sound(992, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x4, 0, 0, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    SetChrSubChip(0xA, 0x2)
    SetMapObjFrame(0xFF, "ato_yuka01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato_yuka02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kage03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato_tukue", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hane", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae_tukue", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage02", 0x0, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    WaitChrThread(0xA, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_11_1768 end

    def Function_12_18B5(): pass

    label("Function_12_18B5")

    SetChrFlags(0xFE, 0x20)

    def lambda_18BF():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_18BF)
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x3)
    Sound(538, 0, 100, 0)
    Sound(4134, 255, 100, 0)    #voice#Sigmund
    PlayEffect(0x5, 0xFF, 0xA, 0x5, 0, 750, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(833, 0, 100, 0)
    Sound(196, 0, 80, 0)
    Sound(165, 0, 100, 0)
    Sound(992, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x4, 0, 0, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    SetChrSubChip(0xA, 0x4)
    SetMapObjFrame(0xFF, "ato_yuka03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato_nuki03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kage04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato_yuka02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_tukue", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae_isu", 0x0, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    WaitChrThread(0xA, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_12_18B5 end

    def Function_13_1A1C(): pass

    label("Function_13_1A1C")

    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x2E)
    SetChrSubChip(0xD, 0x0)
    SetChrChip(0x0, 0xD, 0x32, 0x12C)
    Sound(250, 0, 100, 0)
    OP_9D(0xFE, 0x1996, 0x0, 0xFFFFFDA8, 0x1F4, 0xFA0)
    SetChrChip(0x1, 0xD, 0x0, 0x0)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    Return()

    # Function_13_1A1C end

    def Function_14_1A64(): pass

    label("Function_14_1A64")

    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x2E)
    SetChrSubChip(0xD, 0x0)
    SetChrChip(0x0, 0xD, 0x32, 0x12C)
    Sound(250, 0, 100, 0)
    OP_9D(0xFE, 0x1D1A, 0x0, 0xFFFFFF9C, 0x1F4, 0xFA0)
    SetChrChip(0x1, 0xD, 0x0, 0x0)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    Return()

    # Function_14_1A64 end

    def Function_15_1AAC(): pass

    label("Function_15_1AAC")

    Sleep(700)
    Sound(976, 0, 70, 0)
    Return()

    # Function_15_1AAC end

    SaveToFile()

Try(main)
