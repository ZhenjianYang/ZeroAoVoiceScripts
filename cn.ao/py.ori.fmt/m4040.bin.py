from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4040.bin",                # FileName
        "m4040",                    # MapName
        "m4040",                    # Location
        0x007C,                     # MapIndex
        "ed7350",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x27,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 124, 0, 1, 0, 2],
    )

    BuildStringList((
        "m4040",                  # 0
        "阿奈斯特",               # 1
        "哈尔特曼前议长",         # 2
        "剧情用魔兽",             # 3
        "剧情用魔兽",             # 4
        "bm4020",                 # 5
    ))

    ATBonus("ATBonus_134", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_1F4", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_200", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_204", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_20C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_210", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1D8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_1DC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_1E0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_1E4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_214", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bm4020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms71800.dat", "ms71800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1F4", "MonsterBattlePostion_1D4", "ed7451", "ed7000", "ATBonus_134"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)

    ChipFrameInfo(664, 0)                                        # 0

    ScpFunction((
        "Function_0_298",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_2DA",          # 02, 2
        "Function_3_2F7",          # 03, 3
        "Function_4_1946",         # 04, 4
        "Function_5_19F4",         # 05, 5
        "Function_6_1A37",         # 06, 6
        "Function_7_1A8C",         # 07, 7
        "Function_8_1AE1",         # 08, 8
        "Function_9_1B36",         # 09, 9
        "Function_10_1B8B",        # 0A, 10
        "Function_11_1C04",        # 0B, 11
        "Function_12_1C68",        # 0C, 12
        "Function_13_2C9C",        # 0D, 13
        "Function_14_2CEB",        # 0E, 14
        "Function_15_2D1C",        # 0F, 15
    ))


    def Function_0_298(): pass

    label("Function_0_298")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_298")

    label("loc_2B3")

    Return()

    # Function_0_298 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CA")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2D9")
    ClearScenarioFlags(0x22, 0)
    Event(0, 12)

    label("loc_2D9")

    Return()

    # Function_1_2B4 end

    def Function_2_2DA(): pass

    label("Function_2_2DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 6)), scpexpr(EXPR_END)), "loc_2EC")
    OP_70(0x0, 0x3C)
    Jump("loc_2F0")

    label("loc_2EC")

    OP_70(0x0, 0x0)

    label("loc_2F0")

    Sound(129, 1, 100, 0)
    Return()

    # Function_2_2DA end

    def Function_3_2F7(): pass

    label("Function_3_2F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch02950.itc", 0x20)
    LoadChrToIndex("chr/ch02951.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch00951.itc", 0x23)
    LoadChrToIndex("chr/ch02450.itc", 0x24)
    LoadChrToIndex("chr/ch02451.itc", 0x25)
    LoadChrToIndex("chr/ch02300.itc", 0x26)
    LoadChrToIndex("chr/ch06500.itc", 0x27)
    LoadChrToIndex("monster/ch71850.itc", 0x28)
    LoadChrToIndex("chr/ch02350.itc", 0x29)
    LoadChrToIndex("chr/ch02356.itc", 0x2A)
    LoadChrToIndex("apl/ch50014.itc", 0x2B)
    LoadChrToIndex("monster/ch71852.itc", 0x2C)
    LoadEffect(0x0, "event\\ev618_01.eff")
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\ms00002.eff")
    SoundLoad(832)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02700.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02600.itp")
    OP_68(900, 1400, -40800, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 1400, 0, -45800, 0)
    SetChrPos(0x109, 600, 0, -46900, 0)
    SetChrPos(0x10A, 2300, 0, -47800, 0)
    SetChrPos(0x108, 1500, 0, -48900, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 0, 190, -2400, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, 190, -1400, 0)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 2700, -800, 2000, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -2700, -800, 2000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10000000)
    SetCameraDistance(17500, 3000)

    def lambda_56A():
        OP_97(0x101, 0xFFFFFE0C, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_56A)
    Sleep(50)

    def lambda_587():
        OP_97(0x109, 0xFFFFFE0C, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_587)
    Sleep(50)

    def lambda_5A4():
        OP_97(0x10A, 0xFFFFFE0C, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_5A4)
    Sleep(50)

    def lambda_5C1():
        OP_97(0x108, 0xFFFFFE0C, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_5C1)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x109, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x10A, 0)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x108, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x101,
        "#00007F（在那里……！）\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x10A,
        "#00601F#6P（终于追上了……！）\x02",
    )

    CloseMessageWindow()
    OP_68(0, 500, 1800, 4500)
    MoveCamera(315, 30, 0, 4500)
    OP_6E(650, 4500)
    SetCameraDistance(45000, 4500)
    BeginChrThread(0x9, 3, 0, 4)
    BeginChrThread(0x8, 3, 0, 5)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1200, 4500, 0)
    MoveCamera(315, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(16500, 2000)
    OP_0D()
    WaitChrThread(0x9, 3)
    TurnDirection(0x9, 0x8, 500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0003
    AnonymousTalk(
        0x9,
        (
            "#30W阿、阿奈斯特……\x01",
            "你差不多也该放过我了吧……！\x02\x03",

            "我、我已经不想再和你纠缠不清了！\x02",
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
    WaitChrThread(0x8, 3)

    #C0004
    ChrTalk(
        0x8,
        (
            "#6P#02604F哎呀呀，议长，您这样说可让我太为难了。\x02\x03",

            "#02610F我必须要把您重新推上\x01",
            "克洛斯贝尔的政坛……\x02\x03",

            "这也是为了让我成为下一任的市长。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        (
            "#02701F#11P你、你适可而止吧！\x02\x03",

            "重返克洛斯贝尔政坛！？\x01",
            "事到如今还在痴心妄想，\x01",
            "你觉得有可能成功吗！？\x02\x03",

            "就凭你，难道还想从\x01",
            "迪塔·库罗伊斯的手中\x01",
            "夺走市长的宝座！？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#6P#02613F呵呵，那种事情简单得很。\x02\x03",

            "身为平凡的人类，的确很难成功。\x01",
            "但如果能接近『真神』，那便容易至极了……\x02\x03",

            "#02610F只要拥有可以看透一切因果的睿智，\x01",
            "任何事情都会如我所愿……\x02\x03",

            "#02614F没错，就如同我那伟大的老师──\x01",
            "约亚西姆·琼塔一般！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        "#02705F#11P你、你疯了……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2091, 255, 100, 0)    #voice#Lloyd

    #N0008
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "#30W白日做梦……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_A8B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A8B)
    Fade(500)
    OP_68(700, 900, -18500, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25500, 0)
    OP_68(0, 1200, 500, 6000)
    MoveCamera(323, 15, 0, 6000)
    SetCameraDistance(17500, 6000)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 7)
    Sleep(500)
    BeginChrThread(0x10A, 3, 0, 8)
    Sleep(500)
    BeginChrThread(0x108, 3, 0, 9)
    OP_6F(0x79)
    OP_96(0x9, 0x2BC, 0xBE, 0x11F8, 0x7D0, 0x0)

    #C0009
    ChrTalk(
        0x9,
        "#02700F你、你们是……！？\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0010
    AnonymousTalk(
        0x8,
        (
            "呵呵，追上来了啊。\x02\x03",

            "是不是该说一句好久不见呢？\x01",
            "罗伊德、达德利。\x02\x03",

            "你们在阿尔泰尔市努力搜查，\x01",
            "真是辛苦了。\x02",
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
    WaitChrThread(0x101, 3)

    #C0011
    ChrTalk(
        0x101,
        "#00013F#6P阿奈斯特，你……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x108, 3)

    #C0012
    ChrTalk(
        0x10A,
        (
            "#6P#00601F你早就发现我们\x01",
            "正在追捕你了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#02613F#11P哼哼，这都是凭借\x01",
            "伟大的『真知』之力。\x02\x03",

            "各位追寻我们的踪迹，\x01",
            "来到阿尔泰尔市……\x02\x03",

            "随后察觉到了我们的动向，\x01",
            "在得到共和国军的许可之后，\x01",
            "一直追到了此地……\x02\x03",

            "#02610F这一切都在我的掌握之中！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00010F#6P唔……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x109,
        "#6P#10113F为何连这些都……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x108,
        (
            "#01408F#6P看来他是通过某种不可思议的知觉\x01",
            "而了解到我们的动向的。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "#02705F如、如此说来，你们是\x01",
            "克洛斯贝尔的警察吧？\x02\x03",

            "#02703F……罢了！还是保命要紧！\x02\x03",

            "#02701F我愿意老老实实地投降！\x01",
            "拜托你们！请把这疯子逮捕吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "#02613F#11P哎呀呀，竟然说我是疯子，真是失礼啊。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#00003F#6P不用你说，我们也会这么做的……\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, -200, 190, -1300, 1500, 0x0)
    SetChrChipByIndex(0x101, 0x2B)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0020
    ChrTalk(
        0x101,
        (
            "#00007F#6P哈尔特曼前议长，\x01",
            "以及阿奈斯特·莱兹！\x02\x03",

            "根据自治州法的修订条目，\x01",
            "我们将以逃离拘留所等\x01",
            "多项罪名将你们逮捕。\x02\x03",

            "老老实实地投降吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#02610F#11P哼哼，不必如此着急。\x02\x03",

            "#02613F我今天将要追寻约亚西姆老师的脚步，\x01",
            "开启通往『Ｄ』的大门……\x02\x03",

            "#02614F余兴节目留到那之后再享受也不迟吧！？\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0022
    ChrTalk(
        0x108,
        "#01401F#6P唔……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(0, 1200, 3300, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(16500, 3000)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    Sound(540, 0, 70, 0)
    Sound(531, 0, 50, 0)
    Sleep(500)
    PlayEffect(0x1, 0x3, 0xFF, 0x0, 0, 200, 3300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(832, 2, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    Sound(817, 0, 100, 0)
    OP_82(0xC8, 0xC8, 0xBB8, 0xBB8)
    PlayEffect(0x0, 0x1, 0xFF, 0x0, 2700, 200, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 0x0, -2700, 200, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    def lambda_1166():
        OP_96(0xFE, 0xA8C, 0xC8, 0x7D0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1166)

    def lambda_1180():
        OP_96(0xFE, 0xFFFFF574, 0xC8, 0x7D0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1180)

    def lambda_119A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_119A)

    def lambda_11AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_11AB)
    Sleep(300)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_124B():
        OP_96(0xFE, 0xFFFFFF38, 0xBE, 0xFFFFF380, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_124B)
    Sleep(300)

    def lambda_1268():
        OP_96(0xFE, 0xC8, 0xBE, 0xFFFFEC78, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1268)
    Sleep(100)

    def lambda_1285():
        OP_96(0xFE, 0x5DC, 0xBE, 0xFFFFEDA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1285)
    Sleep(100)

    def lambda_12A2():
        OP_96(0xFE, 0xFFFFFA24, 0xBE, 0xFFFFEF34, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_12A2)
    WaitChrThread(0x109, 1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    WaitChrThread(0x10A, 1)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    WaitChrThread(0x108, 1)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(932, 0, 100, 0)
    Sound(805, 0, 100, 0)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    OP_68(0, 1200, -300, 2500)
    MoveCamera(327, 15, 0, 2500)
    SetCameraDistance(17000, 2500)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    Fade(250)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    OP_24(0x340)
    OP_0D()
    OP_6F(0x79)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    #C0023
    ChrTalk(
        0x9,
        "#02705F哇、哇啊啊啊！？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x109,
        "#3P#10110F#6P这、这是……！\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x10A,
        "#6P#00607F#6P智能兵器的一种吗！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1452")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆完成了前作的二周目任务\x01",      # 0
            "◆未完成前作的二周目任务\x01",      # 1
            "◆不做变更\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1439"),
        (1, "loc_1443"),
        (2, "loc_144D"),
        (SWITCH_DEFAULT, "loc_144D"),
    )


    label("loc_1439")

    OP_29(0x34, 0x4, 0x10)
    Jump("loc_1452")

    label("loc_1443")

    OP_29(0x34, 0x3, 0x10)
    Jump("loc_1452")

    label("loc_144D")

    Jump("loc_1452")

    label("loc_1452")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_153E")

    #C0026
    ChrTalk(
        0x101,
        (
            "#00010F#6P是将地下空间Ｂ２区域\x01",
            "冻结住的魔导智能兵器……！\x02\x03",

            "#00007F大家小心！\x01",
            "它们相当难对付！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#02613F#11P呵呵，好了，诸位，\x01",
            "我们先走一步啦。\x02\x03",

            "#06614F约亚西姆老师留下的守护者有多么强大，\x01",
            "你们就好好体验一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161D")

    label("loc_153E")


    #C0028
    ChrTalk(
        0x101,
        (
            "#00005F#6P是约亚西姆当时操控的那种\x01",
            "中世纪魔导智能兵器……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#02613F#11P哼哼，性能可比\x01",
            "那种还要强得多。\x02\x03",

            "#02610F好了，诸位，\x01",
            "我们就先走一步啦。\x02\x03",

            "#06614F约亚西姆老师留下的守护者有多么强大，\x01",
            "你们就好好体验一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_161D")

    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x0, 0x1F4)
    OP_68(1000, 1200, 3700, 4000)

    def lambda_1642():
        OP_96(0xFE, 0x12C, 0xC8, 0x13EC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1642)
    WaitChrThread(0x8, 1)
    OP_64(0x9)
    Sound(802, 0, 100, 0)
    BeginChrThread(0x8, 3, 0, 10)
    BeginChrThread(0x9, 3, 0, 11)
    Sleep(3500)

    #C0030
    ChrTalk(
        0x109,
        "#10107F啊啊！？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x10A,
        "#00610F可恶，逃走了……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1200, -300, 0)
    MoveCamera(327, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0xA, 3000, 200, 2500, 180)
    SetChrPos(0xB, -1000, 200, 2500, 180)
    OP_0D()
    EndChrThread(0xA, 0x0)
    SetChrChipByIndex(0xA, 0x2C)
    SetChrSubChip(0xA, 0x0)

    def lambda_1713():
        OP_A6(0xFE, 0x32, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1713)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2, 0x1, 0xFF, 0x0, 3000, 2000, 2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(881, 0, 50, 0)
    EndChrThread(0xB, 0x0)
    SetChrChipByIndex(0xB, 0x2C)
    SetChrSubChip(0xB, 0x0)

    def lambda_1796():
        OP_A6(0xFE, 0x32, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1796)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2, 0x2, 0xFF, 0x0, -1000, 2000, 2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    #C0032
    ChrTalk(
        0x108,
        (
            "#01403F#6P看来并不是\x01",
            "寻常的家伙呢……\x02\x03",

            "#01407F全力消灭它们！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#00007F#6P是！\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15000, 500)
    OP_68(0, 1200, 1000, 500)

    def lambda_1883():
        OP_97(0x101, 0x1, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1883)
    Sleep(30)

    def lambda_18A0():
        OP_97(0x108, 0x1, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_18A0)
    Sleep(30)

    def lambda_18BD():
        OP_97(0x10A, 0x1, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_18BD)
    Sleep(30)

    def lambda_18DA():
        OP_97(0x109, 0x1, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_18DA)
    Sleep(500)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x108, 0xFF)
    EndChrThread(0x10A, 0xFF)
    EndChrThread(0x109, 0xFF)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    Battle("BattleInfo_214", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Call(0, 12)
    Return()

    # Function_3_2F7 end

    def Function_4_1946(): pass

    label("Function_4_1946")

    Sleep(1000)

    def lambda_194E():
        OP_95(0xFE, 0, 190, 600, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_194E)
    WaitChrThread(0x9, 1)
    Sleep(500)

    def lambda_196F():
        OP_95(0xFE, 0, 190, 2600, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_196F)
    WaitChrThread(0x9, 1)
    Sleep(500)

    def lambda_1990():
        OP_95(0xFE, 0, 190, 4600, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1990)
    WaitChrThread(0x9, 1)
    OP_A6(0x9, 0x0, 0x32, 0x12C, 0x7D0)
    Sleep(200)

    def lambda_19C4():
        OP_95(0xFE, 0, 190, 5600, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_19C4)
    WaitChrThread(0x9, 1)
    OP_A6(0x9, 0x0, 0x32, 0x12C, 0x7D0)
    Sleep(200)
    Return()

    # Function_4_1946 end

    def Function_5_19F4(): pass

    label("Function_5_19F4")

    Sleep(3000)

    def lambda_19FC():
        OP_95(0xFE, 0, 190, 700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_19FC)
    WaitChrThread(0x8, 1)
    Sleep(1500)

    def lambda_1A1D():
        OP_95(0xFE, 0, 190, 3300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A1D)
    WaitChrThread(0x8, 1)
    Return()

    # Function_5_19F4 end

    def Function_6_1A37(): pass

    label("Function_6_1A37")

    SetChrPos(0xFE, 700, 0, -30000, 0)
    OP_96(0xFE, 0x2BC, 0x0, 0xFFFFB5C8, 0x1388, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFDC10, 0x1388, 0x1)
    OP_96(0xFE, 0xFFFFFF38, 0xBE, 0xFFFFF63C, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_6_1A37 end

    def Function_7_1A8C(): pass

    label("Function_7_1A8C")

    SetChrPos(0xFE, 700, 0, -30000, 0)
    OP_96(0xFE, 0x2BC, 0x0, 0xFFFFB5C8, 0x1388, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFDC10, 0x1388, 0x1)
    OP_96(0xFE, 0xC8, 0xBE, 0xFFFFF060, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_7_1A8C end

    def Function_8_1AE1(): pass

    label("Function_8_1AE1")

    SetChrPos(0xFE, 700, 0, -30000, 0)
    OP_96(0xFE, 0x2BC, 0x0, 0xFFFFB5C8, 0x1388, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFDC10, 0x1388, 0x1)
    OP_96(0xFE, 0x5DC, 0xBE, 0xFFFFF18C, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_8_1AE1 end

    def Function_9_1B36(): pass

    label("Function_9_1B36")

    SetChrPos(0xFE, 700, 0, -30000, 0)
    OP_96(0xFE, 0x2BC, 0x0, 0xFFFFB5C8, 0x1388, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFDC10, 0x1388, 0x1)
    OP_96(0xFE, 0xFFFFFA24, 0xBE, 0xFFFFF31C, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_9_1B36 end

    def Function_10_1B8B(): pass

    label("Function_10_1B8B")


    def lambda_1B90():
        OP_96(0xFE, 0x1004, 0x0, 0x39D0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B90)

    def lambda_1BAA():
        OP_96(0xFE, 0x1194, 0x0, 0x37DC, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BAA)
    WaitChrThread(0x8, 1)

    def lambda_1BC8():
        OP_96(0xFE, 0x19C8, 0x60E, 0x6C98, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BC8)
    WaitChrThread(0x9, 1)

    def lambda_1BE6():
        OP_96(0xFE, 0x1B58, 0x60E, 0x6AA4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BE6)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    Return()

    # Function_10_1B8B end

    def Function_11_1C04(): pass

    label("Function_11_1C04")


    #C0034
    ChrTalk(
        0x9,
        "#12P#18A#02700F放、放开我……\x02",
    )
    #Auto

    Sleep(1100)
    OP_57(0x0)
    OP_5A()
    Sleep(400)
    OP_82(0xC8, 0x0, 0xBB8, 0x4B0)

    #C0035
    ChrTalk(
        0x9,
        "#6P#18A#4S放开我啊！！！！！\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    Return()

    # Function_11_1C04 end

    def Function_12_1C68(): pass

    label("Function_12_1C68")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch02950.itc", 0x20)
    LoadChrToIndex("chr/ch02951.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch00951.itc", 0x23)
    LoadChrToIndex("chr/ch02450.itc", 0x24)
    LoadChrToIndex("chr/ch02451.itc", 0x25)
    LoadChrToIndex("chr/ch00053.itc", 0x26)
    LoadChrToIndex("chr/ch02953.itc", 0x27)
    LoadChrToIndex("monster/ch71850.itc", 0x28)
    LoadChrToIndex("chr/ch00953.itc", 0x29)
    LoadChrToIndex("apl/ch51021.itc", 0x2A)
    SoundLoad(4039)
    LoadEffect(0x0, "event\\ev602_00.eff")
    LoadEffect(0x1, "event\\ev602_03.eff")
    OP_68(2000, 1300, 2000, 0)
    MoveCamera(320, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 1400, 190, -500, 0)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x3)
    SetChrPos(0x109, 400, 190, -1400, 0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x3)
    SetChrPos(0x10A, 3500, 190, -700, 0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x3)
    SetChrPos(0x108, -500, 190, 700, 0)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x3)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 3000, 200, 5000, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1DE0():
        OP_A6(0xFE, 0x32, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1DE0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, 0, 200, 5000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0xB, 0x0)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1E51():
        OP_A6(0xFE, 0x32, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1E51)
    PlayEffect(0x0, 0x0, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetCameraDistance(18000, 3000)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_1EEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1EEB)

    def lambda_1EFC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1EFC)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_6F(0x79)

    def lambda_1F8C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F8C)
    WaitChrThread(0x101, 2)
    Sleep(300)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    #C0036
    ChrTalk(
        0x101,
        "#6P#00015F#30W……唔……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x109,
        "#3P#10106F#30W竟、竟然这么强……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x10A,
        (
            "#6P#00610F啧……\x01",
            "浪费了这么多时间！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x108,
        "#01407F好，赶快追！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(531, 0, 80, 0)
    Sound(540, 0, 60, 0)
    BeginChrThread(0x108, 3, 0, 14)
    Sleep(300)
    BeginChrThread(0x10A, 3, 0, 13)
    Sleep(1000)
    Fade(500)
    OP_68(4900, 900, 13000, 0)
    MoveCamera(300, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(7000, 4100, 33300, 6500)
    MoveCamera(327, 15, 0, 6500)
    SetCameraDistance(16500, 6500)
    WaitChrThread(0x10A, 3)
    OP_6F(0x79)

    #C0040
    ChrTalk(
        0x10A,
        (
            "#00607F#11P怎么了？\x01",
            "已经动不了了吗！？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x108, 3)
    OP_93(0x108, 0xB4, 0x1F4)
    Fade(500)
    OP_68(2700, 1200, -500, 0)
    MoveCamera(320, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 2700, 190, -500, 0)
    SetChrPos(0x109, 1500, 190, -1400, 0)
    OP_0D()

    def lambda_2158():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2158)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)
    SetChrSubChip(0x101, 0x1)
    Sound(2030, 255, 60, 0)    #voice#Lloyd
    Sleep(200)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    #C0041
    ChrTalk(
        0x101,
        "#6P#00007F不、不要紧……！\x02",
    )

    CloseMessageWindow()

    def lambda_21BC():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_21BC)
    SetChrSubChip(0x109, 0x2)
    Sleep(120)
    SetChrSubChip(0x109, 0x1)
    Sound(2463, 255, 60, 0)    #voice#Noel
    Sleep(120)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Sleep(300)

    #C0042
    ChrTalk(
        0x109,
        "#6P#10101F我也可以坚持……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(7000, 4100, 33300, 0)
    MoveCamera(327, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0043
    ChrTalk(
        0x108,
        "#01407F达德利！上面！\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(809, 0, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x5DC)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    SetChrChip(0x0, 0x10A, 0x1E, 0x12C)
    SetChrChipByIndex(0x10A, 0x2A)
    SetChrSubChip(0x10A, 0x0)

    def lambda_22EA():
        OP_9D(0xFE, 0x1C20, 0x1194, 0xA21C, 0x708, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_22EA)
    Sound(3447, 255, 100, 0)    #voice#Dudley
    Sound(834, 0, 100, 0)
    WaitChrThread(0x10A, 1)
    SetChrChipByIndex(0x10A, 0x29)
    SetChrSubChip(0x10A, 0x3)
    SetChrChip(0x1, 0x10A, 0x0, 0x0)
    OP_82(0xC8, 0xC8, 0xBB8, 0x7D0)
    OP_71(0x0, 0x0, 0x3C, 0x0, 0x0)
    Sleep(300)
    Sound(166, 0, 90, 0)
    Sound(189, 0, 90, 0)
    OP_79(0x0)
    Sound(189, 0, 90, 0)
    Sound(833, 0, 90, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x5DC)
    Sleep(1000)
    #Sound(2563, 255, 100, 0)    #voice#Dudley

    #C0044
    ChrTalk(
        0x10A,
        "#00610F啧……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(5000, 1100, 23200, 0)
    MoveCamera(317, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 4700, 0, 15000, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x109, 3000, 0, 15300, 0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_68(9800, 3700, 24500, 2000)
    MoveCamera(327, 13, 0, 2000)
    SetCameraDistance(19000, 2000)

    def lambda_2420():
        OP_96(0xFE, 0x16A8, 0x64, 0x59D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2420)
    Sleep(200)

    def lambda_243D():
        OP_96(0xFE, 0x1004, 0x64, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_243D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)

    #C0045
    ChrTalk(
        0x101,
        "#00005F路、路被……！？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x109,
        "#10110F怎、怎么会这样……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    OP_0D()

    def lambda_24AE():
        OP_96(0xFE, 0x1F40, 0x1194, 0xA604, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_24AE)
    WaitChrThread(0x108, 1)

    #C0047
    ChrTalk(
        0x108,
        (
            "#01403F刚才那场战斗所造成的冲击，\x01",
            "使本身就已很脆弱的地面崩塌了……\x02\x03",

            "#01400F要想跨越这种距离，\x01",
            "恐怕有些难度呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00006F#5P是的……实在是太勉强了。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        "#10106F#5P对、对不起……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x10A,
        (
            "#00606F啧……\x01",
            "既然如此，那也没办法了。\x02\x03",

            "#00607F你们在那里等着吧！\x01",
            "剩下的事情就交给我们两个！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#00007F那、那怎么可以！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x109,
        (
            "#10101F无论你们二位有多强，\x01",
            "在没有支援的情况下也……！\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x108,
        (
            "#01400F不，\x01",
            "接下来就分头行动吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_26A0():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_26A0)

    #C0054
    ChrTalk(
        0x101,
        "#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x10A,
        "#6P#00605F什么意思？\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x108,
        (
            "#01403F通向最深处的路\x01",
            "共有两条。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x108, 0x5A, 0x1F4)
    Sleep(300)

    #C0057
    ChrTalk(
        0x108,
        "#01400F#6P另一条在那边。\x02",
    )

    CloseMessageWindow()
    OP_68(26000, -9000, 29000, 4000)
    MoveCamera(340, 15, 0, 4000)
    OP_6E(650, 4000)
    SetCameraDistance(45500, 4000)

    def lambda_2758():
        OP_93(0x10A, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_2758)
    Sleep(100)

    def lambda_2768():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2768)
    Sleep(100)

    def lambda_2778():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2778)
    Sleep(100)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)

    #C0058
    ChrTalk(
        0x101,
        "#00005F#N#5P还有别的路……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0059
    ChrTalk(
        0x109,
        "#10100F#N#5P莫非在那前方吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0060
    ChrTalk(
        0x108,
        (
            "#01404F#12P#N#5P嗯，虽然会绕些远路，\x01",
            "但应该可以在最深处与我们会合。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(7600, 5400, 42100, 0)
    MoveCamera(317, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    #C0061
    ChrTalk(
        0x10A,
        "#00603F#5P那就好办了！\x02",
    )

    CloseMessageWindow()
    OP_93(0x10A, 0xB4, 0x1F4)
    Sleep(300)

    #C0062
    ChrTalk(
        0x10A,
        (
            "#00607F#11P班宁斯、希卡上士！\x01",
            "我们继续追捕他们！\x02\x03",

            "你们两个就努力与我们会合！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28D6():
        OP_93(0x101, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28D6)
    Sleep(0)

    def lambda_28E6():
        OP_93(0x109, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_28E6)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)

    def lambda_28FE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_28FE)
    Sleep(150)

    #C0063
    ChrTalk(
        0x101,
        "#00007F明白！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        "#10107F是！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0065
    ChrTalk(
        0x108,
        (
            "#01404F#4039V#11P#30W祝你们一路顺利，\x01",
            "一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFC7)
    OP_C9(0x1, 0x80000000)
    OP_68(7600, 5400, 46100, 2500)
    SetCameraDistance(19500, 2500)
    BeginChrThread(0x108, 3, 0, 15)
    Sleep(300)
    BeginChrThread(0x10A, 3, 0, 15)
    WaitChrThread(0x108, 3)
    OP_6F(0x79)
    Fade(500)
    OP_68(5000, 1000, 23200, 0)
    MoveCamera(317, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    EndChrThread(0x108, 0x3)
    EndChrThread(0x10A, 0x3)
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0066
    ChrTalk(
        0x101,
        (
            "#12P#00003F好……我们也赶快吧！\x02\x03",

            "#00001F上士，你可以立即出发吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0067
    ChrTalk(
        0x109,
        "#10101F#5P嗯，没问题！\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0068
    ChrTalk(
        0x109,
        (
            "#10105F#5P对了，罗伊德警官……\x02\x03",

            "#10100F机会难得，\x01",
            "我们要不要试试\x01",
            "组合战技呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0069
    ChrTalk(
        0x101,
        (
            "#00002F#12P哦，这主意不错呢。\x02\x03",

            "#00004F我们已经很熟悉对方的战斗特点了，\x01",
            "应该可以顺利使用。\x02\x03",

            "#00000F熟练掌握之后，\x01",
            "小心慎重地前进吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2442, 255, 100, 0)    #voice#Noel

    #C0070
    ChrTalk(
        0x109,
        "#10109F#5P#30W是！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(300)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BB4")
    AddCraft(0x0, 0x1A0)
    AddCraft(0x8, 0x1A0)
    Jump("loc_2BBC")

    label("loc_2BB4")

    AddCraft(0x0, 0x18C)
    AddCraft(0x8, 0x18C)

    label("loc_2BBC")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德与诺艾尔习得组合战技\x01\x07\x02",

            "『勇猛之心』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人各自消耗１００点ＣＰ，\x01",
            "便可以施展威力强大的组合技攻击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0xFF, 0xF9, 0x0)
    RemoveParty(0x9, 0x0)
    RemoveParty(0x7, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    OP_37()
    SetChrPos(0x0, 5270, 100, 23060, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x120, 6)
    OP_29(0xA0, 0x1, 0x2)
    ClearScenarioFlags(0x21, 0)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_1C68 end

    def Function_13_2C9C(): pass

    label("Function_13_2C9C")

    OP_96(0xFE, 0x1324, 0x0, 0x3A98, 0x1388, 0x1)

    def lambda_2CB5():
        OP_95(0xFE, 7000, 3200, 33300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CB5)
    Sleep(3000)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_13_2C9C end

    def Function_14_2CEB(): pass

    label("Function_14_2CEB")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0x1324, 0x0, 0x3A98, 0x157C, 0x1)
    OP_95(0xFE, 7200, 4500, 43800, 5500, 0x0)
    Return()

    # Function_14_2CEB end

    def Function_15_2D1C(): pass

    label("Function_15_2D1C")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_96(0xFE, 0x1D4C, 0x1194, 0xE678, 0x1388, 0x0)
    Return()

    # Function_15_2D1C end

    SaveToFile()

Try(main)
