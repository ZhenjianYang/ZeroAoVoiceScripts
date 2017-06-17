from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e3800.bin",                # FileName
        "e3800",                    # MapName
        "e3800",                    # Location
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
        "e3800",                  # 0
        "亚修莉",                 # 1
        "金格",                   # 2
        "魔人瓦鲁多",             # 3
        "阿巴斯",                 # 4
        "琴兹",                   # 5
        "贝赛",                   # 6
        "诺加诺夫",               # 7
        "杰德",                   # 8
        "修伊",                   # 9
        "斯拉修",                 # 10
        "寇奇",                   # 11
        "迪诺",                   # 12
        "魔人瓦鲁多",             # 13
        "SE控制",                 # 14
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(600, 0)                                        # 0

    ScpFunction((
        "Function_0_258",          # 00, 0
        "Function_1_268",          # 01, 1
        "Function_2_269",          # 02, 2
        "Function_3_1AA4",         # 03, 3
        "Function_4_1AD7",         # 04, 4
        "Function_5_1B3E",         # 05, 5
        "Function_6_1BF0",         # 06, 6
        "Function_7_1CA2",         # 07, 7
        "Function_8_1D4E",         # 08, 8
        "Function_9_1DF9",         # 09, 9
        "Function_10_1EAB",        # 0A, 10
        "Function_11_1ED4",        # 0B, 11
        "Function_12_1EFD",        # 0C, 12
        "Function_13_1F26",        # 0D, 13
        "Function_14_1F4B",        # 0E, 14
    ))


    def Function_0_258(): pass

    label("Function_0_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_267")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_267")

    Return()

    # Function_0_258 end

    def Function_1_268(): pass

    label("Function_1_268")

    Return()

    # Function_1_268 end

    def Function_2_269(): pass

    label("Function_2_269")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    LoadChrToIndex("chr/ch23900.itc", 0x1E)
    LoadChrToIndex("chr/ch30900.itc", 0x1F)
    LoadChrToIndex("chr/ch31800.itc", 0x20)
    LoadChrToIndex("chr/ch06800.itc", 0x21)
    LoadChrToIndex("chr/ch09200.itc", 0x23)
    LoadChrToIndex("apl/ch51512.itc", 0x24)
    LoadChrToIndex("chr/ch06700.itc", 0x28)
    LoadChrToIndex("apl/ch51511.itc", 0x29)
    LoadChrToIndex("chr/ch30800.itc", 0x2D)
    LoadChrToIndex("chr/ch31700.itc", 0x2E)
    LoadChrToIndex("apl/ch51510.itc", 0x2F)
    LoadEffect(0x0, "battle/ms00000.eff")
    LoadEffect(0x1, "event/ev15030.eff")
    LoadEffect(0x2, "battle/bs880000.eff")
    LoadEffect(0x3, "event/ev14006.eff")
    LoadEffect(0x4, "battle/ms00064.eff")
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundLoad(868)
    SoundLoad(825)
    SoundLoad(3576)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0x11, 0x2D)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x2D)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0xF, 0x2E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x2E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    OP_A7(0x14, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_78(0xA, 0xA)
    OP_49()
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_68(32970, -4310, -31970, 0)
    MoveCamera(32, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29000, 0)
    MoveCamera(35, 35, 0, 5000)
    SetCameraDistance(33000, 5000)
    Sound(868, 2, 80, 0)
    BeginChrThread(0x15, 1, 0, 14)
    BeginChrThread(0xA, 0, 0, 13)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-13550, 1000, -13650, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(34500, 0)
    OP_68(-13550, 1000, -13650, 5000)
    MoveCamera(40, 30, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(36500, 5000)
    OP_0D()
    OP_6F(0x79)
    Sound(834, 0, 100, 0)
    EndChrThread(0xA, 0x0)
    Fade(500)
    OP_68(4000, 6500, -26500, 0)
    MoveCamera(45, -5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(4000, 3250, -26500, 500)
    MoveCamera(45, 30, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(21000, 500)
    SetChrPos(0xA, 4470, 5400, -26160, 225)
    OP_D5(0xA, 0x0, 0x36EE8, 0x0, 0x0)
    SetChrPos(0x14, 4470, 4900, -26160, 0)
    OP_71(0xA, 0x145, 0x154, 0x1, 0x8)
    OP_9D(0xA, 0x1176, 0x578, 0xFFFF99D0, 0x3E8, 0x2710)
    OP_82(0xC8, 0x0, 0xBB8, 0x5DC)
    Sound(833, 0, 100, 0)
    Sound(196, 0, 100, 0)
    Sound(880, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(1000)
    OP_79(0xA)
    OP_6F(0x79)
    Sleep(1000)
    OP_68(4000, 5250, -26500, 1000)
    MoveCamera(45, 25, 0, 1000)
    OP_71(0xA, 0x155, 0x168, 0x1, 0x8)
    OP_79(0xA)
    OP_0D()
    OP_6F(0x79)
    OP_74(0xA, 0x14)
    OP_71(0xA, 0x4B0, 0x500, 0x1, 0x8)
    SetCameraDistance(19000, 3500)
    OP_68(4000, 5450, -26500, 3500)
    MoveCamera(65, 25, 0, 1500)
    OP_6F(0x40)
    MoveCamera(25, 20, 5, 2000)
    OP_6F(0x79)
    OP_79(0xA)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    #Sound(3573, 255, 100, 0)    #voice#Wald

    #C0001
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#30W#N哼哼……\x01",
            "……真是不错的景象啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0002
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#30W#N将这个地方作为『祭品』，\x01",
            "以便使我今后继续变强……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0003
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#4S#N哈哈哈……\x01",
            "这建议真是不坏呢……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18000, 1300)
    OP_68(4000, 4250, -26500, 1300)
    MoveCamera(25, 30, 5, 1300)
    Sound(892, 0, 100, 0)
    OP_71(0xA, 0x104, 0x122, 0x1, 0x8)
    OP_79(0xA)
    OP_6F(0x79)
    Sound(833, 0, 100, 0)
    Sound(251, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    MoveCamera(25, -10, 5, 300)
    OP_68(4000, 5250, -26500, 300)
    OP_71(0xA, 0x123, 0x12C, 0x1, 0x8)
    OP_9D(0xA, 0x1176, 0x3C28, 0xFFFF99D0, 0x3A98, 0x1F40)
    Fade(500)
    OP_68(50000, 72500, 50000, 0)
    MoveCamera(45, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(110000, 0)
    OP_F0(0x0, 0x1)
    OP_68(50000, 82500, 50000, 1500)
    MoveCamera(45, -10, 0, 1500)
    Sound(834, 0, 100, 0)
    SetChrPos(0xA, 45000, 20000, 45000, 225)
    OP_D5(0xA, 0x0, 0x36EE8, 0x0, 0x0)
    OP_9D(0xA, 0x2710, 0x11170, 0x2710, 0xC544, 0x1388)
    OP_71(0xA, 0x140, 0x145, 0x1, 0x8)

    def lambda_93A():
        OP_96(0xFE, 0xFFFF3CB0, 0xAFC8, 0xFFFF3CB0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_93A)
    Sound(990, 0, 100, 0)
    Sleep(800)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sleep(500)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0xA, 0x1)
    SetChrPos(0xA, 12450, 20500, -23000, 70)
    OP_D5(0xA, 0x0, 0x11170, 0x0, 0x0)
    OP_68(12450, 26700, -23000, 0)
    MoveCamera(60, 40, -10, 0)
    OP_6E(500, 0)
    SetCameraDistance(15500, 0)
    OP_68(26730, 8700, -18670, 500)
    MoveCamera(30, 30, -10, 500)
    SetCameraDistance(28000, 500)
    SetChrPos(0xA, 12450, 20500, -23000, 70)
    OP_96(0xA, 0x55F0, 0x157C, 0xFFFFB3D4, 0x9C40, 0x0)
    Sound(196, 0, 100, 0)
    Sound(876, 0, 100, 0)
    Sound(3549, 255, 100, 0)    #voice#Wald
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x4, 0xFF, 0xA, 0x5, 0, 4500, 1500, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_6F(0x79)
    OP_68(31150, 2500, -15500, 500)
    MoveCamera(45, 20, 0, 500)
    SetCameraDistance(23000, 500)
    Sound(200, 0, 100, 0)
    Sound(880, 0, 100, 0)

    def lambda_ACB():
        OP_96(0xFE, 0x79AE, 0xFFFFFE0C, 0xFFFFC374, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_ACB)
    OP_71(0xA, 0x145, 0x154, 0x1, 0x8)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x5DC)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sound(833, 0, 100, 0)
    OP_71(0x9, 0x0, 0x3C, 0x0, 0x8)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 30000, 0, -14500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_79(0x9)
    OP_0D()
    OP_6F(0x79)
    OP_68(31150, 3500, -15500, 1500)
    MoveCamera(30, 30, 10, 1500)
    SetCameraDistance(20000, 1500)
    SetChrPos(0x14, 31150, 3500, -15500, 0)
    Sound(892, 0, 100, 0)

    def lambda_B9E():
        OP_D5(0xFE, 0x0, 0x2BF20, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B9E)
    OP_71(0xA, 0x154, 0x168, 0x1, 0x8)
    OP_79(0xA)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    WaitChrThread(0xA, 2)
    OP_6F(0x79)
    Sleep(500)
    BeginChrThread(0xA, 0, 0, 4)
    OP_C9(0x0, 0x80000000)

    #C0004
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3576V#5P#N#4S#40A哼哼哼……\x01",
            "#5S哇哈哈哈哈哈哈哈哈哈！！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDF8)
    OP_C9(0x1, 0x80000000)
    WaitChrThread(0xA, 0)
    SetChrPos(0xE, 41750, -2500, -22700, 270)
    SetChrPos(0x11, 40100, -2500, -24600, 315)
    SetChrPos(0x10, 41450, -2500, -24450, 315)
    SetChrPos(0xF, 40950, -2500, -21550, 270)
    SetChrPos(0x12, 43350, -2500, -22000, 270)
    SetChrPos(0x13, 49950, -2100, -22500, 270)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    #N0005
    NpcTalk(
        0x11,
        "声音",
        "这、这是怎么回事！？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(41000, 0, -22050, 0)
    MoveCamera(22, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(39150, -700, -22050, 2000)
    MoveCamera(13, 15, 0, 2000)
    SetCameraDistance(16000, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0006
    ChrTalk(
        0x11,
        "#12P那、那栋破旧公寓……！？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xE,
        "完全化为废墟瓦砾了！？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xF,
        "那只怪物究竟是……！？\x02",
    )

    CloseMessageWindow()
    OP_68(37000, 1000, -22150, 2000)
    MoveCamera(345, 5, 0, 2000)
    SetCameraDistance(17500, 2000)
    Sleep(1000)
    Fade(250)

    def lambda_DAB():
        OP_D5(0xFE, 0x0, 0x20F58, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_DAB)
    OP_71(0xA, 0x277, 0x280, 0x1, 0x8)
    OP_79(0xA)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    WaitChrThread(0xA, 2)
    OP_6F(0x79)

    #C0009
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#30W#N哈哈……\x01",
            "你们来得正好。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_71(0xA, 0x104, 0x122, 0x1, 0x8)
    OP_79(0xA)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    OP_68(38750, 700, -23450, 3000)
    MoveCamera(50, 35, 0, 3000)
    SetCameraDistance(11000, 3000)

    def lambda_E68():

        label("loc_E68")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_E68")

    QueueWorkItem2(0xE, 2, lambda_E68)

    def lambda_E7A():

        label("loc_E7A")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_E7A")

    QueueWorkItem2(0x11, 2, lambda_E7A)

    def lambda_E8C():

        label("loc_E8C")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_E8C")

    QueueWorkItem2(0x10, 2, lambda_E8C)

    def lambda_E9E():

        label("loc_E9E")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_E9E")

    QueueWorkItem2(0xF, 2, lambda_E9E)

    def lambda_EB0():

        label("loc_EB0")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_EB0")

    QueueWorkItem2(0x12, 2, lambda_EB0)
    Sound(833, 0, 70, 0)
    Sound(251, 0, 100, 0)

    def lambda_ECE():
        OP_9D(0xFE, 0x8D68, 0xFFFFF63C, 0xFFFFA81C, 0x2710, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_ECE)
    OP_71(0xA, 0x122, 0x154, 0x1, 0x8)
    WaitChrThread(0xA, 1)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Sound(833, 0, 100, 0)
    Sound(196, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    EndChrThread(0xE, 0x2)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x10, 0x2)
    EndChrThread(0xF, 0x2)
    EndChrThread(0x12, 0x2)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x12, 0x20)

    def lambda_F56():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_F56)
    Sleep(50)

    def lambda_F6E():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F6E)
    Sleep(50)

    def lambda_F86():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F86)
    Sleep(50)

    def lambda_F9E():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_F9E)
    Sleep(50)

    def lambda_FB6():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_FB6)
    OP_79(0xA)
    Sleep(500)
    SetChrPos(0x14, 36200, -2500, -22500, 0)

    def lambda_FE2():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_FE2)
    OP_71(0xA, 0x154, 0x168, 0x1, 0x8)
    OP_79(0xA)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    WaitChrThread(0xA, 2)
    OP_6F(0x79)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x12, 1)

    #C0010
    ChrTalk(
        0x10,
        "哇哇哇……！！\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x12,
        "呜哇哇哇！！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#30W#N哼哼……你们就\x01",
            "葬身于此吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0013
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#30W#N作为我与自己的过去和软弱……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#30W#N以及始终无法舍弃的『多余存在』\x01",
            "彻底诀别的见证……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0015
    ChrTalk(
        0xE,
        "哎……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xF,
        (
            "难、难道是……\x01",
            "瓦鲁多大哥……\x02",
        )
    )

    CloseMessageWindow()
    Sound(892, 0, 100, 0)
    OP_71(0xA, 0x82, 0x8C, 0x1, 0x8)
    OP_79(0xA)
    Sleep(500)
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)

    #C0017
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#5S#N#20A喝啊啊啊啊啊啊啊啊啊啊！！！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(253, 0, 100, 0)
    Sound(893, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_74(0xA, 0xF)
    OP_71(0xA, 0x96, 0x9B, 0x1, 0x8)
    PlayEffect(0x2, 0xFF, 0xA, 0x5, 0, -6000, 0, 180, 160, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    #C0018
    ChrTalk(
        0xE,
        "#11P#10A不……！！\x02",
    )
    #Auto

    OP_68(41120, 800, -23590, 1000)
    MoveCamera(52, 23, 0, 1000)
    SetCameraDistance(19000, 1000)
    Sound(833, 0, 100, 0)
    Sound(545, 0, 100, 0)
    BeginChrThread(0x11, 3, 0, 5)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 6)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 7)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 8)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 9)
    Sleep(300)
    Sound(880, 0, 100, 0)
    Sound(288, 0, 100, 0)
    Sound(876, 0, 100, 0)
    Sound(116, 0, 100, 0)
    OP_71(0x3, 0x0, 0x14, 0x1, 0x8)
    OP_79(0xA)
    CancelBlur(500)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x12, 3)
    Sleep(300)

    #C0019
    ChrTalk(
        0xF,
        "#15A#60W#2S……呜……啊………\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #C0020
    ChrTalk(
        0x10,
        "#28A#60W#2S………………………（颤抖）\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #N0021
    NpcTalk(
        0x13,
        "少年的声音",
        "#1P各、各位前辈！？\x02",
    )

    CloseMessageWindow()
    OP_68(47600, -1100, -22500, 1000)
    MoveCamera(55, 30, 0, 1000)
    OP_6E(500, 1000)
    SetCameraDistance(20000, 1000)

    def lambda_133C():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_133C)

    def lambda_1351():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_1351)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x13, 3)
    TurnDirection(0x13, 0xF, 500)
    Sleep(300)
    TurnDirection(0x13, 0xE, 500)
    Sleep(300)
    TurnDirection(0x13, 0x11, 500)
    Sleep(300)
    TurnDirection(0x13, 0x10, 500)
    Sleep(300)
    TurnDirection(0x13, 0x12, 500)

    #C0022
    ChrTalk(
        0x13,
        "各位！？寇奇前辈！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x13,
        "请、请振作一点啊！\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x12,
        (
            "#12P#60W#2S……我不行……了……\x01",
            "你一个人……逃吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W#N哼哼……你也在啊……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    OP_68(43180, -600, -22820, 1500)
    MoveCamera(65, 24, 0, 1500)
    SetCameraDistance(19750, 1500)

    def lambda_1486():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_1486)
    OP_93(0x13, 0x10E, 0x64)
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_6F(0x79)

    #C0026
    ChrTalk(
        0x13,
        (
            "哇哇哇哇！？\x01",
            "怪、怪物！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#30W#N正好……\x01",
            "……也把你这小子亲手给……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0028
    NpcTalk(
        0xB,
        "低沉的声音",
        "到此为止吧。\x02",
    )

    CloseMessageWindow()
    OP_64(0x13)
    Fade(500)
    SetChrPos(0xB, 24800, -2500, -22000, 90)
    SetChrPos(0x8, 24200, -2500, -23850, 90)
    SetChrPos(0x9, 23000, -2500, -23450, 90)
    SetChrPos(0xC, 23450, -2500, -21500, 90)
    SetChrPos(0xD, 22100, -2500, -22150, 90)
    OP_68(25350, -400, -23090, 0)
    MoveCamera(50, 3, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(14000, 1000)
    OP_D5(0xA, 0x0, 0x33450, 0x0, 0x0)

    def lambda_15D7():
        OP_D5(0xFE, 0x0, 0x41EB0, 0x0, 0x2EE)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15D7)
    OP_74(0xA, 0x14)
    OP_71(0xA, 0x277, 0x280, 0x1, 0x8)
    OP_79(0xA)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    WaitChrThread(0xA, 2)
    OP_0D()
    OP_6F(0x79)

    #C0029
    ChrTalk(
        0x9,
        "#6P哇，好巨大啊！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xC,
        "#6P那、那是什么！？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xD,
        "#6P鬼……！？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        (
            "#5P#04100F……你们几个\x01",
            "去周围灭火。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xC,
        "#6P明、明白了……！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "#5P金格，\x01",
            "你带附近的人去避难。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        "#6P嗯，知道啦。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 10)
    BeginChrThread(0xC, 3, 0, 11)
    BeginChrThread(0xD, 3, 0, 12)
    Sleep(300)
    OP_68(31950, -100, -23600, 3000)
    MoveCamera(320, 23, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18500, 3000)

    def lambda_171B():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_171B)
    Sleep(200)

    def lambda_1733():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1733)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    SetMessageWindowPos(300, 140, -1, -1)

    #A0036
    AnonymousTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W#N秃子和武器商人吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0037
    AnonymousTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#12P#30W#N哼哼……你们也想给我\x01",
            "展示一下『力量』吗……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0038
    ChrTalk(
        0xB,
        "#04100F#5P既然你有此意，自不吝啬。\x02",
    )

    CloseMessageWindow()
    OP_68(25250, -1500, -21850, 1500)
    MoveCamera(315, 25, 0, 1500)
    SetCameraDistance(15500, 1500)
    Sleep(1000)
    Sound(534, 0, 50, 0)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x29)
    OP_A0(0xB, 1500, 0x0, 0x1)
    Sleep(300)

    #C0039
    ChrTalk(
        0xB,
        (
            "#04100F#5P我已经得到了瓦吉的批准，\x01",
            "这次就尽情一战吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#5P哎呀呀，我并不喜欢\x01",
            "直接交火呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(24580, -1500, -22730, 800)
    MoveCamera(315, 25, 0, 800)
    OP_6E(600, 800)
    SetCameraDistance(15500, 800)
    Sleep(300)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x24)
    OP_A0(0x8, 1500, 0x0, 0x2)
    Sound(531, 0, 70, 0)
    Sound(358, 0, 70, 0)
    Sleep(300)

    #C0041
    ChrTalk(
        0x8,
        (
            "#5P但这家伙在我的店附近闹事，\x01",
            "在搞出太大麻烦之前，\x01",
            "不如趁早解决了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 140, -1, -1)

    #A0042
    AnonymousTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#12P#30W#N哈哈哈……好胆量。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(32500, 0, -22700, 2500)
    MoveCamera(315, 20, 0, 2500)
    SetCameraDistance(14000, 2500)
    Sleep(2000)
    Sound(893, 0, 100, 0)
    Sound(892, 0, 100, 0)
    Sound(825, 2, 100, 0)
    Sound(195, 0, 100, 0)
    Sound(212, 0, 100, 0)
    OP_71(0xA, 0xD3, 0xE1, 0x1, 0x8)
    PlayEffect(0x3, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_79(0xA)
    BeginChrThread(0xA, 3, 0, 3)
    SetMessageWindowPos(300, 150, -1, -1)

    #A0043
    AnonymousTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#12P#30W#N就让你们彻底\x01",
            "体会一下……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0044
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#12P#5S#N我瓦鲁多·瓦雷斯\x01",
            "的『力量』吧！！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopSound(825, 1000, 90)
    StopSound(868, 1000, 70)
    SetCameraDistance(16500, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_269 end

    def Function_3_1AA4(): pass

    label("Function_3_1AA4")

    OP_74(0xA, 0x5)

    label("loc_1AA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1AD6")
    OP_71(0xA, 0xE1, 0xDF, 0x1, 0x8)
    OP_79(0xA)
    OP_71(0xA, 0xDF, 0xE1, 0x1, 0x8)
    OP_79(0xA)
    Jump("loc_1AA8")

    label("loc_1AD6")

    Return()

    # Function_3_1AA4 end

    def Function_4_1AD7(): pass

    label("Function_4_1AD7")

    OP_82(0x14, 0x14, 0xBB8, 0x7D0)
    Sleep(1500)
    OP_74(0xA, 0x14)
    OP_71(0xA, 0x5B, 0x64, 0x1, 0x8)
    OP_79(0xA)
    OP_71(0xA, 0x65, 0x78, 0x1, 0x20)
    OP_82(0x64, 0x64, 0xBB8, 0xCE4)
    Sleep(3000)
    OP_71(0xA, 0x79, 0x82, 0x1, 0x8)
    OP_79(0xA)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    Return()

    # Function_4_1AD7 end

    def Function_5_1B3E(): pass

    label("Function_5_1B3E")

    OP_93(0x11, 0x0, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0x11, 0xA122, 0xFFFFFB1E, 0xFFFF8EEA, 0x9C4, 0x1D4C)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(501, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    OP_A6(0x11, 0x0, 0x32, 0x12C, 0xBB8)
    OP_96(0x11, 0xA122, 0xFFFFFA24, 0xFFFF8EEA, 0x1D4C, 0x0)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0x11, 0x2F)
    SetChrSubChip(0x11, 0x2)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_1B3E end

    def Function_6_1BF0(): pass

    label("Function_6_1BF0")

    OP_93(0x10, 0x13B, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0x10, 0xBD42, 0x0, 0xFFFF98AE, 0xDAC, 0x1D4C)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(815, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    OP_A6(0x10, 0x0, 0x32, 0x12C, 0xBB8)
    OP_96(0x10, 0xB7CA, 0xFFFFFBE6, 0xFFFF9494, 0x1D4C, 0x0)
    SetChrChipByIndex(0x10, 0x2F)
    SetChrSubChip(0x10, 0x3)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    Return()

    # Function_6_1BF0 end

    def Function_7_1CA2(): pass

    label("Function_7_1CA2")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0x12, 0xBDD8, 0xFFFFFA24, 0xFFFFA4FC, 0x7D0, 0x1D4C)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(501, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    OP_A6(0x12, 0x0, 0x32, 0x12C, 0xBB8)
    OP_96(0x12, 0xB95A, 0xFFFFF7CC, 0xFFFFA402, 0x1D4C, 0x0)
    OP_93(0x12, 0x5A, 0x0)
    SetChrChipByIndex(0x12, 0x2F)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_1CA2 end

    def Function_8_1D4E(): pass

    label("Function_8_1D4E")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xE, 0xB9F0, 0x1F4, 0xFFFFBC08, 0xFA0, 0x1D4C)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(815, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    OP_A6(0xE, 0x0, 0x32, 0x12C, 0xBB8)
    OP_96(0xE, 0xB734, 0xFFFFFF38, 0xFFFFB758, 0x1D4C, 0x0)
    SetChrChipByIndex(0xE, 0x2F)
    SetChrSubChip(0xE, 0x2)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    Return()

    # Function_8_1D4E end

    def Function_9_1DF9(): pass

    label("Function_9_1DF9")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xF, 0xAB18, 0xFFFFFE0C, 0xFFFFBD02, 0xBB8, 0x1D4C)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(196, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    OP_A6(0xF, 0x0, 0x32, 0x12C, 0xBB8)
    OP_96(0xF, 0xA8F2, 0xFFFFF63C, 0xFFFFB820, 0x1D4C, 0x0)
    OP_93(0xF, 0x2D, 0x0)
    SetChrChipByIndex(0xF, 0x2F)
    SetChrSubChip(0xF, 0x1)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    Return()

    # Function_9_1DF9 end

    def Function_10_1EAB(): pass

    label("Function_10_1EAB")

    OP_95(0x9, 21960, -2500, -25110, 4000, 0x0)
    OP_95(0x9, 21890, -6130, -34350, 4000, 0x0)
    Return()

    # Function_10_1EAB end

    def Function_11_1ED4(): pass

    label("Function_11_1ED4")

    OP_95(0xC, 21870, -2500, -25020, 4000, 0x0)
    OP_95(0xC, 21270, -6030, -34120, 4000, 0x0)
    Return()

    # Function_11_1ED4 end

    def Function_12_1EFD(): pass

    label("Function_12_1EFD")

    OP_95(0xD, 19770, -2500, -21590, 4000, 0x0)
    OP_95(0xD, 13770, -1130, -16129, 4000, 0x0)
    Return()

    # Function_12_1EFD end

    def Function_13_1F26(): pass

    label("Function_13_1F26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F4A")
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(1000)
    Jump("Function_13_1F26")

    label("loc_1F4A")

    Return()

    # Function_13_1F26 end

    def Function_14_1F4B(): pass

    label("Function_14_1F4B")

    Sleep(500)
    Sound(891, 0, 100, 0)
    Sleep(2000)
    Sound(880, 0, 100, 0)
    Sound(200, 0, 60, 0)
    Sleep(2000)
    Sound(880, 0, 100, 0)
    Sound(200, 0, 50, 0)
    Sleep(1500)
    Sound(880, 0, 100, 0)
    Sound(833, 0, 60, 0)
    Sleep(2000)
    Sound(880, 0, 100, 0)
    Sound(200, 0, 60, 0)
    Return()

    # Function_14_1F4B end

    SaveToFile()

Try(main)
