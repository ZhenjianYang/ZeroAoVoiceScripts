from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t130b.bin",                # FileName
        "t130b",                    # MapName
        "t130b",                    # Location
        0x00B6,                     # MapIndex
        "ed7564",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 182, 0, 0, 0, 1],
    )

    BuildStringList((
        "t130b",                  # 0
        "小丑肯帕雷拉",           # 1
        "剧情用魔兽",             # 2
        "剧情用魔兽",             # 3
        "bt130b",                 # 4
        "镜之城方向",             # 5
        "摩天轮方向",             # 6
        "恐怖过山车方向",         # 7
        "翠雀酒店方向",           # 8
    ))

    ATBonus("ATBonus_208", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_2E8", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_308", 0x0052, 3, 6, 45, 3, 3, 30, 0, "bt130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms84400.dat", "ms85900.dat", 0, 0, 0, 0, "ms86600.dat", 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_2C8", "ed7590", "ed7453", "ATBonus_208"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 2,   0.0,                   -15.0,                 -1.0,                  625.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  3.0,                   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 11,  0.0,                   -18.5,                 -1.0,                  25.0,                  [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  1.0,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  18.5,                  0.19999998807907104,   1.0])

    PlaceName(0.0, 0.0, 30.0, 0x0000, 0x0000, "镜之城方向")
    PlaceName(-40.0, 0.0, 10.0, 0x0000, 0x0000, "摩天轮方向")
    PlaceName(60.0, 0.0, 10.0, 0x0000, 0x0000, "恐怖过山车方向")
    PlaceName(0.0, 0.0, -80.0, 0x0000, 0x0000, "翠雀酒店方向")

    ChipFrameInfo(892, 0)                                        # 0

    ScpFunction((
        "Function_0_37C",          # 00, 0
        "Function_1_38C",          # 01, 1
        "Function_2_4C5",          # 02, 2
        "Function_3_AA6",          # 03, 3
        "Function_4_AC5",          # 04, 4
        "Function_5_B05",          # 05, 5
        "Function_6_B3F",          # 06, 6
        "Function_7_B75",          # 07, 7
        "Function_8_C90",          # 08, 8
        "Function_9_2AF7",         # 09, 9
        "Function_10_2B40",        # 0A, 10
        "Function_11_2B89",        # 0B, 11
    ))


    def Function_0_37C(): pass

    label("Function_0_37C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_38B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)

    label("loc_38B")

    Return()

    # Function_0_37C end

    def Function_1_38C(): pass

    label("Function_1_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3A1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_3A1")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B9")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_3B9")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E1")
    ModifyEventFlags(1, 1, 0x80)
    OP_10(0x2, 0x1)
    OP_10(0x3, 0x1)
    OP_1B(0x2, 0x0, 0x9)
    OP_1B(0x3, 0x0, 0xA)

    label("loc_3E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_447")
    SetMapObjFrame(0xFF, "face00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "obj11", 0x0, 0x1)
    SetMapObjFrame(0x9, "face00", 0x0, 0x1)
    SetMapObjFrame(0xA, "face00", 0x0, 0x1)
    SetMapObjFrame(0xB, "face00", 0x0, 0x1)
    SetMapObjFrame(0xC, "face00", 0x0, 0x1)
    Jump("loc_49B")

    label("loc_447")

    SetMapObjFrame(0xFF, "face01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fool11", 0x0, 0x1)
    SetMapObjFrame(0x9, "face01", 0x0, 0x1)
    SetMapObjFrame(0xA, "face01", 0x0, 0x1)
    SetMapObjFrame(0xB, "face01", 0x0, 0x1)
    SetMapObjFrame(0xC, "face01", 0x0, 0x1)

    label("loc_49B")

    SoundDistance(0x7E, 0xFFFFB5D2, 0xBB8, 0xFFFF26F8, 0x13880, 0xC350, 0x50, 0x0)
    OP_E3(0x639C, 0xBB8, 0xFFFF26F8)
    Return()

    # Function_1_38C end

    def Function_2_4C5(): pass

    label("Function_2_4C5")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("monster/ch84450.itc", 0x1E)
    LoadChrToIndex("monster/ch84452.itc", 0x1F)
    LoadChrToIndex("monster/ch85950.itc", 0x20)
    LoadChrToIndex("monster/ch85952.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch03050.itc", 0x27)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 0, -10000, 0)
    SetChrPos(0x102, -650, 0, -11100, 0)
    SetChrPos(0x103, 750, 0, -10800, 0)
    SetChrPos(0x104, 150, 0, -12000, 0)
    SetChrPos(0x109, -1100, 0, -12300, 0)
    SetChrPos(0x105, 1200, 0, -12500, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -2500, 1500, -7300, 135)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x20)
    BeginChrThread(0x9, 0, 0, 3)
    SetChrChip(0x0, 0x9, 0x64, 0x1F4)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 2500, 1500, -7300, 225)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x20)
    BeginChrThread(0xA, 0, 0, 3)
    SetChrChip(0x0, 0xA, 0x64, 0x1F4)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, 0, 0)
    MoveCamera(30, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    FadeToBright(1000, 0)
    MoveCamera(0, 20, 0, 8000)
    SetCameraDistance(18000, 8000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(0, 1000, -8000, 0)
    OP_68(0, 1000, -10000, 3000)
    MoveCamera(0, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0001
    ChrTalk(
        0x105,
        (
            "#10302F#12P哎呀呀……\x01",
            "这种品位真让人不敢恭维啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        (
            "#00306F#6P竟然准备得如此细致，\x01",
            "倒也不得不拜服了……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x109,
        (
            "#10108F#6P话、话说回来……\x01",
            "这个形象好诡异啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x103,
        (
            "#00206F#12P……竟然把咪西\x01",
            "换成了这种东西……\x02\x03",

            "#00201F……绝对不能饶恕……！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00109F#6P缇、缇欧，\x01",
            "冷静些……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00008F#6P话说回来，琪雅究竟\x01",
            "在什么地方——\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0007
    ChrTalk(
        0x103,
        "#00207F#12P左前方与右前方……有东西在靠近！\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#00005F#6P什么……！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7590", 0)
    OP_68(0, 1400, -8500, 3000)
    MoveCamera(0, 10, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15500, 3000)
    OP_6F(0x79)
    Sound(212, 0, 100, 0)
    Sound(223, 0, 100, 0)
    Sound(817, 0, 70, 0)
    BlurSwitch(0x1F4, 0x77FFFFFF, 0x4, 0x1, 0xF)
    SetCameraDistance(15000, 3000)
    BeginChrThread(0x9, 3, 0, 4)
    BeginChrThread(0xA, 3, 0, 4)
    Sleep(500)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x79)
    MoveCamera(0, 7, 0, 20000)
    SetCameraDistance(15000, 20000)
    #Sound(2182, 255, 100, 0)    #voice#Elie
    OP_82(0x64, 0x0, 0xBB8, 0x320)

    #C0009
    ChrTalk(
        0x102,
        "#00115F#6P#4S#13A呀啊啊啊啊啊啊……！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(300)

    #C0010
    ChrTalk(
        0x109,
        "#10111F#6P#N这、这是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0011
    ChrTalk(
        0x104,
        (
            "#00310F#6P#N难道是恐怖过山车那里的怪物？\x01",
            "但这未免也太逼真了吧……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00007F#6P唔……\x01",
            "总之，准备迎击吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x105,
        "#10307F#12P#N它们来了！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14000, 800)
    Sleep(700)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    SetScenarioFlags(0x0, 0)
    Battle("BattleInfo_308", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 8)
    Return()

    # Function_2_4C5 end

    def Function_3_AA6(): pass

    label("Function_3_AA6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC4")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_3_AA6")

    label("loc_AC4")

    Return()

    # Function_3_AA6 end

    def Function_4_AC5(): pass

    label("Function_4_AC5")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_AD5():
        OP_98(0xFE, 0x0, 0xFFFFFA24, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD5)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_AC5 end

    def Function_5_B05(): pass

    label("Function_5_B05")

    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)

    def lambda_B1F():
        OP_9B(0x0, 0xFE, 0xFFEC, 0xBB8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1F)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_5_B05 end

    def Function_6_B3F(): pass

    label("Function_6_B3F")

    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Sleep(500)

    def lambda_B55():
        OP_9B(0x0, 0xFE, 0x14, 0xBB8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B55)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_B3F end

    def Function_7_B75(): pass

    label("Function_7_B75")


    def lambda_B7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B7A)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x898), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0xA28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    Return()

    # Function_7_B75 end

    def Function_8_C90(): pass

    label("Function_8_C90")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("monster/ch84450.itc", 0x1E)
    LoadChrToIndex("monster/ch85950.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch03050.itc", 0x27)
    LoadChrToIndex("apl/ch51326.itc", 0x28)
    LoadChrToIndex("apl/ch51416.itc", 0x29)
    SoundLoad(3716)
    SoundLoad(3717)
    SoundLoad(3718)
    SoundLoad(959)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04800.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis234.itp")
    LoadEffect(0x0, "event\\ev10002.eff")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 0, -10000, 0)
    SetChrPos(0x102, -650, 0, -11100, 0)
    SetChrPos(0x103, 750, 0, -10800, 0)
    SetChrPos(0x104, 150, 0, -12000, 0)
    SetChrPos(0x109, -1100, 0, -12300, 0)
    SetChrPos(0x105, 1200, 0, -12500, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -2500, 0, -7300, 135)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 0, 0, 3)
    SetChrChip(0x0, 0x9, 0x64, 0x1F4)
    SetChrFlags(0x9, 0x20)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 2500, 0, -7300, 225)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 3)
    SetChrChip(0x0, 0xA, 0x64, 0x1F4)
    SetChrFlags(0xA, 0x20)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -14350, 5950, 1450, 135)
    SetChrFlags(0x8, 0x8)
    BlurSwitch(0x0, 0x77FFFFFF, 0x4, 0x1, 0xF)
    OP_68(0, 1400, -8500, 30)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15500, 3000)
    Sleep(2000)
    Sound(212, 0, 100, 0)
    Sound(223, 0, 100, 0)
    Sound(817, 0, 70, 0)
    SetCameraDistance(16000, 1000)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    BeginChrThread(0x9, 0, 0, 7)
    BeginChrThread(0xA, 0, 0, 7)
    Sleep(500)
    CancelBlur(1500)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    OP_6F(0x79)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Sleep(300)
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(500)

    #C0014
    ChrTalk(
        0x102,
        "#00106F#6P#30W呼……呼……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        "#00311F#6P可恶，那是什么鬼东西……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#00201F#12P那种打击感究竟是……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#00010F#6P啧……\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1400, -8200, 1000)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x4B0, 0x0)
    Sound(33, 0, 100, 0)
    Sound(48, 0, 50, 0)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0018
    ChrTalk(
        0x101,
        (
            "#00007F#4S#5P你到底想躲藏到\x01",
            "什么时候！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0019
    ChrTalk(
        0x101,
        "#00007F#4S#5P赶快出来吧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0020
    ChrTalk(
        0x109,
        "#10105F#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x105,
        "#10301F#12P哦……？\x02",
    )

    CloseMessageWindow()
    Sound(1008, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x8, 0x8)
    OP_C9(0x0, 0x80000000)

    #N0022
    NpcTalk(
        0x8,
        "少年的声音",
        "#3716V#30A#40W呵呵，你竟然知道我在这里。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    PlayBGM("ed7584", 0)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x6)
    ClearChrFlags(0x8, 0x100)
    OP_D5(0x8, 0x0, 0x20F58, 0x0, 0x0)
    OP_68(-14350, 6950, 1450, 3000)
    MoveCamera(330, -13, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13250, 3000)

    def lambda_123A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_123A)
    Sleep(50)

    def lambda_124A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_124A)
    Sleep(50)

    def lambda_125A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_125A)
    Sleep(50)

    def lambda_126A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_126A)
    Sleep(50)

    def lambda_127A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_127A)
    Sleep(50)

    def lambda_128A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_128A)
    OP_6F(0x79)
    Sleep(300)

    #C0023
    ChrTalk(
        0x109,
        "#10111F#12P#N什么……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0024
    ChrTalk(
        0x102,
        "#00105F#12P#N小、小男孩……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0025
    ChrTalk(
        0x103,
        "#00201F#12P#N完全没感觉到他的气息……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0026
    ChrTalk(
        0x104,
        "#00311F#12P#N你小子……是什么人？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_13D0")

    #N0027
    NpcTalk(
        0x8,
        "少年",
        (
            "#04804F#5P呵呵，好薄情啊。\x02\x03",

            "咱们明明有过一面之缘，\x01",
            "并不是素不相识的陌生人啊。\x02\x03",

            "#04802F对吧？特别任务支援科的诸位。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1456")

    label("loc_13D0")


    #N0028
    NpcTalk(
        0x8,
        "少年",
        (
            "#04804F#5P呵呵，好薄情啊。\x02\x03",

            "严格来说，我们确实是初次见面，\x01",
            "但也不能算是素不相识啊。\x02\x03",

            "#04802F对吧？特别任务支援科的诸位。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1456")

    Fade(500)
    OP_68(0, 1000, -9500, 0)
    MoveCamera(130, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15400, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0029
    ChrTalk(
        0x102,
        "#00101F#11P你……难道是……！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        (
            "#00201F#5P在约纳的房间里给大家\x01",
            "布下机关的黑客……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_163E")

    #C0031
    ChrTalk(
        0x101,
        (
            "#00003F#5P……同时也是把兰花塔的资料\x01",
            "交给那些恐怖分子的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    #C0032
    ChrTalk(
        0x101,
        (
            "#00013F#5P上次见面，是在人偶工房前\x01",
            "擦身而过的那次吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1682")

    label("loc_163E")


    #C0033
    ChrTalk(
        0x101,
        (
            "#00003F#5P……同时也是把兰花塔的资料\x01",
            "交给那些恐怖分子的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1682")

    Fade(500)
    OP_68(-14350, 6950, 1450, 0)
    MoveCamera(330, -13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13250, 0)
    OP_0D()

    #N0034
    NpcTalk(
        0x8,
        "少年",
        "#04809F#5P呵呵，没错。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    SetChrName("少年")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            "#30W『#3717V噬身之蛇』的执行者，\x01",
            "Ｎｏ．０──『小丑』肯帕雷拉。\x02\x03",

            "#3718V今后请多指教。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE86)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(0, 1000, -9500, 0)
    MoveCamera(130, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15400, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0036
    ChrTalk(
        0x101,
        "#00010F#5P啧……！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        (
            "#00107F#11P是那个使利贝尔\x01",
            "陷入混乱的神秘结社……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_1978")
    OP_29(0xA5, 0x1, 0xB)

    #C0038
    ChrTalk(
        0x104,
        (
            "#00311F#11P#N听说你曾出现在那间工房的门前时，\x01",
            "就觉得你可能与『结社』存在某种关系……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0039
    ChrTalk(
        0x105,
        (
            "#10306F#11P#N没想到你竟然还会\x01",
            "与恐怖分子合作。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_19D2")

    label("loc_1978")

    OP_29(0xA5, 0x1, 0xC)

    #C0040
    ChrTalk(
        0x104,
        (
            "#00311F#11P#N看到那些恐怖分子\x01",
            "使用机械智能兵器的时候，\x01",
            "我就觉得很可疑了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_19D2")

    Fade(500)
    OP_68(-8730, 4700, -4270, 0)
    MoveCamera(127, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24200, 0)
    SetCameraDistance(26200, 1500)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x100)
    OP_D5(0x8, 0x4E20, 0x0, 0x0, 0x0)
    OP_6F(0x79)
    OP_0D()

    #C0041
    ChrTalk(
        0x8,
        (
            "#04804F#6P#N呵呵呵，他们可真是不幸啊。\x02\x03",

            "#04802F『黑月』和『赤色星座』……\x01",
            "竟然会遇到那么危险的敌人。\x02\x03",

            "#04806F特别是帝国的那些家伙，\x01",
            "实在是太悲惨啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0042
    ChrTalk(
        0x109,
        (
            "#10107F#11P这、这叫什么话！\x02\x03",

            "再怎么说，你们也是\x01",
            "互相协助的同伴吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#04809F#6P#N啊哈哈，他们只不过是\x01",
            "被我利用的棋子之一罢了。\x02\x03",

            "#04802F只是觉得他们的\x01",
            "行动方式挺有趣，\x01",
            "才随便提供些帮助。\x02\x03",

            "#04804F至于他们的理念与思想，\x01",
            "我连半点兴趣都没有呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0044
    ChrTalk(
        0x109,
        "#10110F#11P唔……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        (
            "#10301F#11P#N哼，这小子的性格\x01",
            "可真够恶劣啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0046
    ChrTalk(
        0x103,
        (
            "#00211F#5P……也许可以与\x01",
            "瓦吉先生一较高低。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1000, -9500, 0)
    MoveCamera(130, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15400, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00003F#5P玩笑就开到这里吧。\x02\x03",

            "#00001F你来克洛斯贝尔\x01",
            "究竟有何企图……？\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    Fade(500)
    SetCameraDistance(15000, 500)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sound(805, 0, 100, 0)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0048
    ChrTalk(
        0x101,
        (
            "#00007F#4S#5P更重要的是……\x01",
            "你把琪雅带到什么地方了！？\x02\x03",

            "#4S就算动用武力，我也要让你说出来！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(500)
    Fade(500)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x6)
    ClearChrFlags(0x8, 0x100)
    OP_D5(0x8, 0x0, 0x20F58, 0x0, 0x0)
    OP_68(-14350, 6950, 1450, 0)
    MoveCamera(330, -13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13250, 0)
    OP_0D()

    #C0049
    ChrTalk(
        0x8,
        (
            "#04804F#5P呵呵呵，气势真不错呢。\x02\x03",

            "#04800F不过，我并没有对你们的\x01",
            "小公主做任何事情哦。\x02\x03",

            "只是看到她刚才摇摇晃晃地\x01",
            "从这里走过而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#00011F#12P#N什么……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0051
    ChrTalk(
        0x104,
        (
            "#00307F#12P#N你这家伙……\x01",
            "想抵赖到底吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0052
    ChrTalk(
        0x8,
        (
            "#04804F#5P呵呵，事实就是事实嘛。\x02\x03",

            "#04802F信或不信，\x01",
            "都是你们的自由……\x02\x03",

            "我今天只是来和\x01",
            "你们打个招呼而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetCameraDistance(12750, 500)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x6)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Sound(325, 0, 100, 0)
    SetChrSubChip(0x8, 0xE)
    Sleep(300)
    Fade(500)
    OP_68(0, 800, -20000, 0)
    OP_68(0, 2600, -20000, 6000)
    MoveCamera(0, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(41550, 0)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x100)
    OP_D5(0x8, 0x4E20, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(1000)
    Sound(212, 0, 100, 0)
    Sound(223, 0, 100, 0)
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x4, 0x1, 0xF)
    Sleep(1000)
    CancelBlur(1000)
    Fade(100)
    SetMapObjFrame(0xFF, "obj11", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fool11", 0x0, 0x1)
    SetMapObjFrame(0x9, "face00", 0x1, 0x1)
    SetMapObjFrame(0xA, "face00", 0x1, 0x1)
    SetMapObjFrame(0xB, "face00", 0x1, 0x1)
    SetMapObjFrame(0xC, "face00", 0x1, 0x1)
    SetMapObjFrame(0x9, "face01", 0x0, 0x1)
    SetMapObjFrame(0xA, "face01", 0x0, 0x1)
    SetMapObjFrame(0xB, "face01", 0x0, 0x1)
    SetMapObjFrame(0xC, "face01", 0x0, 0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x101,
        "#00007F#5P什么……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x109,
        "#10108F#6P这、这是……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(0, 1000, 0, 0)
    MoveCamera(30, 35, 0, 0)
    MoveCamera(0, 20, 0, 6000)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(18000, 6000)
    OP_0D()
    Sleep(1500)
    Sound(212, 0, 100, 0)
    Sound(223, 0, 100, 0)
    BlurSwitch(0x7D0, 0xFFFFFFFF, 0x4, 0x1, 0xF)
    Sleep(700)
    Sound(829, 0, 100, 0)
    Sleep(1300)
    CancelBlur(1500)
    Fade(250)
    SetMapObjFrame(0xFF, "face01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "face00", 0x1, 0x1)
    OP_0D()
    OP_6F(0x79)
    OP_68(0, 1000, -9500, 2000)
    MoveCamera(0, 20, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(18000, 2000)
    Sleep(500)

    def lambda_2259():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2259)
    Sleep(50)

    def lambda_2269():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2269)
    Sleep(50)

    def lambda_2279():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2279)
    Sleep(50)

    def lambda_2289():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2289)
    Sleep(50)

    def lambda_2299():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2299)
    Sleep(50)

    def lambda_22A9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_22A9)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    #C0055
    ChrTalk(
        0x102,
        "#00101F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        "#00301F#6P恢复原状了……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x105,
        (
            "#10306F#12P……真是排场十足的\x01",
            "魔术表演啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        "#00208F#12P难道是幻术吗……？\x02",
    )

    CloseMessageWindow()
    Sound(325, 0, 80, 0)
    Sleep(300)
    Sound(959, 2, 60, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-14350, 6950, 1450, 2000)
    MoveCamera(330, -13, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(13250, 2000)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x6)
    ClearChrFlags(0x8, 0x100)
    OP_D5(0x8, 0x0, 0x20F58, 0x0, 0x0)
    SetChrPos(0x8, -14350, 5950, 1450, 145)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, -700, -1000, 0, 0, 0, 800, 1000, 800, 0xFF, 0, 0, 0, 0)

    def lambda_249D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_249D)
    Sleep(50)

    def lambda_24AD():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_24AD)
    Sleep(50)

    def lambda_24BD():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_24BD)
    Sleep(50)

    def lambda_24CD():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_24CD)
    Sleep(50)

    def lambda_24DD():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_24DD)
    Sleep(50)

    def lambda_24ED():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_24ED)
    OP_6F(0x79)

    #C0059
    ChrTalk(
        0x8,
        (
            "#04809F#5P呵呵，好啦，\x01",
            "我就此失陪。\x02\x03",

            "#04802F希望能在不久之后\x01",
            "与各位再次相会。\x02\x03",

            "#04805F哦，对了，\x01",
            "你们的小公主走向里面的城堡了。\x02\x03",

            "#04804F赶快去把她接回去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-14350, 6950, 1450, 0)
    MoveCamera(0, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    MoveCamera(315, 5, 0, 3000)
    SetCameraDistance(10000, 3000)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x100)
    OP_D5(0x8, 0x4E20, 0x0, 0x0, 0x0)
    SetChrPos(0x8, -14350, 5900, 1450, 135)
    ClearChrFlags(0x8, 0x1)
    StopEffect(0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_25(0x3BF, 0x46)
    Sound(3703, 255, 100, 0)    #voice#Companella
    OP_6F(0x79)
    OP_0D()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(10750, 500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_6F(0x79)
    CancelBlur(1000)
    StopEffect(0x0, 0x2)
    StopSound(959, 1000, 60)
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    StopBGM(0x1770)
    Fade(500)
    OP_68(0, 1000, -9500, 0)
    MoveCamera(130, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15400, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0060
    ChrTalk(
        0x101,
        "#00006F#40W#5P……那就是……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0061
    ChrTalk(
        0x101,
        "#00010F#5P#4S那就是『噬身之蛇』啊！\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#00108F#11P虽然听艾丝蒂尔他们\x01",
            "和玲说起过，但实在是……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        (
            "#00206F#5P……包括黑客方面的技术，\x01",
            "真是个相当惊人的集团呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#00310F#11P喂喂，竟然连那种家伙\x01",
            "都来到克洛斯贝尔了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x109,
        (
            "#10106F#11P怎、怎么会……\x01",
            "克洛斯贝尔为何总是遭遇灾难……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x105,
        (
            "#10306F#11P#N看样子，存在着很多不为我们所知的内情呢。\x02\x03",

            "#10303F算啦，不管怎么说……\x02\x03",

            "#10301F我们现在还是\x01",
            "先去找琪雅吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00011F#5P没错……！\x01",
            "他说琪雅走向里面的城堡了！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        "#00107F#11P我们赶快过去看看吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    PlayBGM("ed7564", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x234), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x20)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    SetChrPos(0x0, 0, 0, -10000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x146, 2)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    OP_10(0x2, 0x1)
    OP_10(0x3, 0x1)
    OP_1B(0x2, 0x0, 0x9)
    OP_1B(0x3, 0x0, 0xA)
    EventEnd(0x5)
    Return()

    # Function_8_C90 end

    def Function_9_2AF7(): pass

    label("Function_9_2AF7")

    EventBegin(0x1)

    #C0069
    ChrTalk(
        0x101,
        (
            "#00001F琪雅在里面的城堡，\x01",
            "我们赶快追过去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -10940, 0, 3960, 135)
    EventEnd(0x4)
    Return()

    # Function_9_2AF7 end

    def Function_10_2B40(): pass

    label("Function_10_2B40")

    EventBegin(0x1)

    #C0070
    ChrTalk(
        0x101,
        (
            "#00001F琪雅在里面的城堡，\x01",
            "我们赶快追过去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 10740, 0, 4720, 225)
    EventEnd(0x4)
    Return()

    # Function_10_2B40 end

    def Function_11_2B89(): pass

    label("Function_11_2B89")

    EventBegin(0x1)

    #C0071
    ChrTalk(
        0x101,
        (
            "#00001F琪雅在里面的城堡，\x01",
            "我们赶快追过去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, -14500, 0)
    EventEnd(0x4)
    Return()

    # Function_11_2B89 end

    SaveToFile()

Try(main)
