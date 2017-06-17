from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4090.bin",                # FileName
        "m4090",                    # MapName
        "m4090",                    # Location
        0x007E,                     # MapIndex
        "ed7350",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x27,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 126, 0, 0, 0, 1],
    )

    BuildStringList((
        "m4090",                  # 0
        "阿奈斯特",               # 1
        "哈尔特曼前议长",         # 2
        "假哈尔特曼",             # 3
        "魔人阿奈斯特",           # 4
        "身穿法衣的青年",         # 5
        "效果",                   # 6
        "效果",                   # 7
        "效果",                   # 8
        "效果",                   # 9
        "SE制御",                 # 10
        "bm4030",                 # 11
        "bm4040",                 # 12
    ))

    ATBonus("ATBonus_1DC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_29C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_280", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_284", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_288", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_28C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_290", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_294", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 8, 16, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 0, 0, 180)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_2DC", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bm4030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_29C", "MonsterBattlePostion_27C", "ed7451", "ed7000", "ATBonus_1DC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_320", 0x004A, 3, 6, 45, 3, 3, 30, 0, "bm4040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2BC", "MonsterBattlePostion_27C", "ed7454", "ed7000", "ATBonus_1DC"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    254,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    254,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    254,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    254,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1020, 0)                                       # 0

    ScpFunction((
        "Function_0_3FC",          # 00, 0
        "Function_1_437",          # 01, 1
        "Function_2_474",          # 02, 2
        "Function_3_493",          # 03, 3
        "Function_4_1A35",         # 04, 4
        "Function_5_1A70",         # 05, 5
        "Function_6_1A83",         # 06, 6
        "Function_7_374A",         # 07, 7
        "Function_8_37AA",         # 08, 8
        "Function_9_37CE",         # 09, 9
        "Function_10_37F2",        # 0A, 10
        "Function_11_381C",        # 0B, 11
        "Function_12_383E",        # 0C, 12
        "Function_13_3863",        # 0D, 13
        "Function_14_3A59",        # 0E, 14
        "Function_15_3AD6",        # 0F, 15
        "Function_16_3B32",        # 10, 16
        "Function_17_3C99",        # 11, 17
        "Function_18_3EED",        # 12, 18
        "Function_19_3F3A",        # 13, 19
        "Function_20_65C6",        # 14, 20
        "Function_21_65F3",        # 15, 21
        "Function_22_6618",        # 16, 22
        "Function_23_663D",        # 17, 23
        "Function_24_6675",        # 18, 24
        "Function_25_6A4F",        # 19, 25
        "Function_26_6BB8",        # 1A, 26
        "Function_27_6D09",        # 1B, 27
        "Function_28_6D5E",        # 1C, 28
        "Function_29_6D78",        # 1D, 29
        "Function_30_6DE4",        # 1E, 30
        "Function_31_6E24",        # 1F, 31
        "Function_32_6E64",        # 20, 32
        "Function_33_6E7E",        # 21, 33
        "Function_34_6E98",        # 22, 34
        "Function_35_6EB2",        # 23, 35
        "Function_36_6F20",        # 24, 36
        "Function_37_6F8E",        # 25, 37
    ))


    def Function_0_3FC(): pass

    label("Function_0_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40D")
    Event(0, 3)

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_424")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 6)
    Jump("loc_436")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_436")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 1)
    Event(0, 19)

    label("loc_436")

    Return()

    # Function_0_3FC end

    def Function_1_437(): pass

    label("Function_1_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_44C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1FE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_461")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1C6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)

    label("loc_461")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    Sound(129, 1, 100, 0)
    Return()

    # Function_1_437 end

    def Function_2_474(): pass

    label("Function_2_474")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_492")
    OP_A1(0xFE, 0x708, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_474")

    label("loc_492")

    Return()

    # Function_2_474 end

    def Function_3_493(): pass

    label("Function_3_493")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch02950.itc", 0x20)
    LoadChrToIndex("chr/ch02951.itc", 0x21)
    LoadChrToIndex("chr/ch02300.itc", 0x22)
    LoadChrToIndex("chr/ch06500.itc", 0x23)
    LoadChrToIndex("monster/ch67450.itc", 0x24)
    LoadChrToIndex("chr/ch02952.itc", 0x25)
    LoadChrToIndex("chr/ch02350.itc", 0x26)
    LoadChrToIndex("monster/ch67452.itc", 0x27)
    LoadChrToIndex("chr/ch02357.itc", 0x28)
    LoadEffect(0x0, "event\\ev602_01.eff")
    LoadEffect(0x1, "event\\ev602_02.eff")
    LoadEffect(0x2, "event\\ev602_00.eff")
    SoundLoad(832)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06600.itp")
    OP_68(0, -400, -20400, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 50, -1400, -24400, 0)
    SetChrPos(0x109, -100, -1400, -26400, 0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 200, 30500, 0)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -1500, 200, 29800, 45)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 0, 200, 28500, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFrame(0xFF, "bl_ato00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_ato01", 0x0, 0x1)
    OP_68(0, -400, -17400, 3000)
    SetCameraDistance(18500, 3000)

    def lambda_685():
        OP_97(0x101, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_685)
    Sleep(30)

    def lambda_6A2():
        OP_97(0x109, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6A2)
    FadeToBright(2000, 0)
    OP_0D()
    StopBGM(0xBB8)
    WaitChrThread(0x101, 0)

    #C0001
    ChrTalk(
        0x101,
        "#00007F（啊……！）\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0)

    #C0002
    ChrTalk(
        0x109,
        "#6P#10101F（找到了……！）\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7510", 0)
    OP_68(0, 6000, 37500, 5000)
    MoveCamera(0, -3, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(29500, 5000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1300, 32000, 0)
    MoveCamera(329, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(17500, 1500)
    OP_0D()
    OP_95(0x8, 0, 200, 32000, 1500, 0x0)
    OP_6F(0x79)

    #C0003
    ChrTalk(
        0x8,
        (
            "#02613F呵呵……\x01",
            "正如约亚西姆老师说的一样。\x02\x03",

            "#02610F在这里，必然可以\x01",
            "轻松达成我的目的。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "#6P#02703F啧……你给我适可而止吧！\x02\x03",

            "#02701F约亚西姆和你\x01",
            "全都是疯子……！\x02\x03",

            "别、别把我卷进\x01",
            "你们的妄想中！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0005
    ChrTalk(
        0x8,
        (
            "#11P#02613F哈哈，您有资格\x01",
            "如此指责别人吗？\x02\x03",

            "#02610F是叫『乐园』吧……？\x01",
            "曾经光顾过那种地方的您，\x01",
            "竟然还好意思装出一副清高自傲的样子。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    #C0006
    ChrTalk(
        0x9,
        (
            "#6P#02705F我、我只是被教团的人\x01",
            "连蒙带骗地带去的……\x02\x03",

            "#02703F如果早知道是那种低劣的地方，\x01",
            "我绝对不会涉足的！\x02\x03",

            "#02701F而且他们还给我服下了奇怪的药物……\x01",
            "我、我完全是个受害者啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    #C0007
    ChrTalk(
        0x8,
        (
            "#11P#02613F哎呀呀，您觉得这种说辞\x01",
            "能得到社会的认可吗？\x02\x03",

            "#02610F要是克洛斯贝尔时代周刊刊登一篇独家报道，\x01",
            "想必会引起巨大轰动吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        "#6P#02701F唔……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2090, 255, 100, 0)    #voice#Lloyd

    #N0009
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "#30W#12A到此为止了……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_ADB():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_ADB)
    Sleep(50)

    def lambda_AEB():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_AEB)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    SetChrPos(0x101, -600, 200, 12600, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x109, 800, 200, 11900, 0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    OP_68(-500, 1200, 25870, 3000)
    MoveCamera(329, 14, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18000, 3000)
    Sleep(1000)
    BeginChrThread(0x11, 1, 0, 5)

    def lambda_B6C():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B6C)
    Sleep(100)

    def lambda_B89():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B89)
    Sleep(500)

    def lambda_BA6():
        OP_95(0xFE, 0, 200, 28500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BA6)
    OP_6F(0x79)

    #C0010
    ChrTalk(
        0x9,
        "#11P#02705F哦哦，你们是……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)

    #C0011
    ChrTalk(
        0x8,
        (
            "#02605F#11P哎呀呀，是你们啊。\x02\x03",

            "#02613F好不容易才搞定了那两个麻烦的家伙，\x01",
            "没想到又混进来两只小喽啰。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#6P#00013F好巨大的祭坛……\x01",
            "这里就是据点的最深处吧。\x02\x03",

            "#00007F你把亚里欧斯先生他们怎么样了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#02610F#11P哦，你是说『风之剑圣』\x01",
            "和搜查一科的王牌吗？\x02\x03",

            "#02613F那两个人实在很麻烦，\x01",
            "所以我只能设法困住了他们。\x02\x03",

            "他们现在大概正在被我那\x01",
            "十架魔导智能兵器蹂躏吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0014
    ChrTalk(
        0x101,
        "#6P#00010F什么……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x109,
        "#6P#10110F竟然一下放出十架那样的怪物……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#02613F#11P拜他们所赐，我已经把\x01",
            "从老师那里继承的棋子全部用光了。\x02\x03",

            "#02610F不过，这样至少可以\x01",
            "确保干掉那两个家伙。\x02\x03",

            "接下来，我就在这个神圣的地方\x01",
            "不慌不忙地达成目的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#6P#00007F休想得逞……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x4)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0018
    ChrTalk(
        0x109,
        "#6P#10107F举手投降吧！\x02",
    )

    CloseMessageWindow()
    OP_68(-340, 1200, 26670, 1500)
    OP_6F(0x79)
    Sound(832, 2, 70, 0)
    Sound(934, 0, 50, 0)
    Sound(829, 0, 50, 0)
    PlayEffect(0x2, 0x1, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetCameraDistance(16000, 30000)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0019
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "哎呀呀……\x01",
            "你们似乎没有搞清现在的状况呢。\x02\x03",

            "话说回来，我原本还在想，\x01",
            "为什么没看见艾莉……\x02\x03",

            "原来如此，她暂时离开支援科，\x01",
            "去给麦克道尔先生帮忙了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0020
    ChrTalk(
        0x101,
        "#6P#00010F唔……！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x109,
        (
            "#6P#10101F难、难道他能窥视到\x01",
            "罗伊德警官的记忆……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06613F#11P哦，而且还协助新市长和新议长\x01",
            "建立新的体制与法案……\x02\x03",

            "#06610F原来如此，想通过这种方式\x01",
            "为支援科制造政治立足点，\x01",
            "以便使今后的行动更加方便啊。\x02\x03",

            "#06613F哼，新市长的这项提案倒是很符合他的风格，\x01",
            "可以算是一次有趣的尝试。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#6P#00013F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06606F#11P不过，让艾莉这样的人才\x01",
            "埋没在小小的警察局，\x01",
            "真是只能用愚蠢来形容啊。\x02\x03",

            "#06600F唔，等我当上市长之后，\x01",
            "马上就解散特别任务支援科。\x02\x03",

            "然后让艾莉担任我的私人秘书，\x01",
            "充分发挥她的才能……\x02\x03",

            "#06604F嗯嗯，这才是最好的选择，\x01",
            "就这么决定了！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138E")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆得到了前作的成就：与艾莉的羁绊\x01",      # 0
            "◆未得到前作的成就：与艾莉的羁绊\x01",      # 1
            "◆不做变更\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1379"),
        (1, "loc_1381"),
        (2, "loc_1389"),
        (SWITCH_DEFAULT, "loc_1389"),
    )


    label("loc_1379")

    SetScenarioFlags(0x25, 3)
    Jump("loc_138E")

    label("loc_1381")

    ClearScenarioFlags(0x25, 3)
    Jump("loc_138E")

    label("loc_1389")

    Jump("loc_138E")

    label("loc_138E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_149C")
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0025
    ChrTalk(
        0x101,
        (
            "#6P#00007F#4S别开玩笑了……！\x02\x03",

            "#3S#00010F休想把艾莉牵扯到\x01",
            "你那荒谬的妄想中！\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x109,
        "#6P#10105F（罗伊德警官的气势好惊人……）\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06603F#11P哼……\x01",
            "你这种小鬼根本\x01",
            "就配不上艾莉。\x02\x03",

            "#06611F为了让她醒悟，\x01",
            "我要把隐患消灭在萌芽状态。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_156A")

    label("loc_149C")


    #C0028
    ChrTalk(
        0x101,
        "#6P#00013F这家伙……！\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x109,
        (
            "#6P#10106F如果他这些话是认真的，\x01",
            "总觉得相当那个呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06613F#11P哼哼……\x01",
            "约亚西姆老师的大仇还没报。\x02\x03",

            "#06610F另外，为了斩断艾莉的留恋，\x01",
            "我要把隐患消灭在萌芽状态。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_156A")

    StopBGM(0x7D0)
    Fade(250)
    OP_68(0, 1200, 28500, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 3000)
    Sound(540, 0, 50, 0)
    Sound(531, 0, 20, 0)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_82(0x32, 0x32, 0xBB8, 0xDAC)
    OP_25(0x340, 0x64)
    Sound(357, 0, 100, 0)
    StopEffect(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x2)

    def lambda_1636():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1636)
    Sleep(100)
    SetChrSubChip(0x8, 0x3)
    Sleep(2000)
    BeginChrThread(0x9, 3, 0, 4)
    Sound(831, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x3)
    SetChrFlags(0xB, 0x800)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)

    def lambda_1698():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1698)

    def lambda_16A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_16A9)
    Sleep(500)
    Sound(817, 0, 100, 0)
    Sleep(500)
    StopEffect(0x0, 0x2)
    Sound(202, 0, 100, 0)
    StopSound(832, 1000, 100)
    PlayEffect(0x1, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 1300, 28500, 1000)
    MoveCamera(0, 21, 10, 1000)
    SetCameraDistance(17000, 1000)
    OP_82(0x12C, 0x12C, 0xBB8, 0x5DC)
    SetChrSubChip(0xB, 0x4)
    Sleep(150)
    SetChrSubChip(0xB, 0x5)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xB, 2)
    SetChrFlags(0x8, 0x80)
    Sleep(500)
    CancelBlur(500)
    Sleep(500)
    OP_6F(0x79)
    EndChrThread(0x8, 0xFF)
    ClearChrFlags(0xB, 0x800)
    Fade(250)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 3, 0, 2)
    OP_0D()
    OP_68(330, 1300, 26300, 1500)
    MoveCamera(36, 13, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(18000, 1500)
    OP_6F(0x79)
    WaitChrThread(0x9, 3)

    #C0031
    ChrTalk(
        0x9,
        "#6P#02705F哇哇哇哇……！？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x109,
        "#12P#10110F这、这是……！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#6P#00010F嗯，这就是红色『真知』\x01",
            "所带来的魔人化效果！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 80, -1, -1)
    Sleep(300)

    #A0034
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "呵呵，在这神圣的地方，\x01",
            "连觉醒时的感觉都比平时更加畅快……\x02",
        )
    )

    CloseMessageWindow()

    #A0035
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "你们只是我在实现宏大愿望之前\x01",
            "所享用的小小供品……\x02",
        )
    )

    CloseMessageWindow()

    #A0036
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "尽管翻滚挣扎，\x01",
            "体会痛苦的滋味吧！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0037
    ChrTalk(
        0x101,
        "#6P#00007F做梦……！\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        "#12P#10107F目标一名，开始压制！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xB, 0x3)
    BlurSwitch(0x190, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(16000, 400)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x6)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xB, 0x32, 0xC8)
    Sound(251, 0, 100, 0)

    def lambda_19E0():
        OP_9D(0xFE, 0x0, 0xC8, 0x53FC, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_19E0)
    Sleep(250)
    SetChrSubChip(0xB, 0x7)
    Sleep(150)
    EndChrThread(0xB, 0x1)
    SetScenarioFlags(0x0, 0)
    Battle("BattleInfo_2DC", 0x0, 0x0, 0x100, 0x27, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    Call(0, 6)
    Return()

    # Function_3_493 end

    def Function_4_1A35(): pass

    label("Function_4_1A35")

    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x9, 0x87, 0x1F4)
    Sleep(500)

    def lambda_1A56():
        OP_96(0xFE, 0xFFFFF31C, 0xC8, 0x79E0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1A56)
    WaitChrThread(0x9, 1)
    Return()

    # Function_4_1A35 end

    def Function_5_1A70(): pass

    label("Function_5_1A70")

    Sleep(2500)
    Sound(805, 0, 100, 0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    Return()

    # Function_5_1A70 end

    def Function_6_1A83(): pass

    label("Function_6_1A83")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x9, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    OP_32(0x9, 0xFF, 0x0)
    OP_32(0x7, 0xFF, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch02950.itc", 0x20)
    LoadChrToIndex("chr/ch02951.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch00951.itc", 0x23)
    LoadChrToIndex("chr/ch02450.itc", 0x24)
    LoadChrToIndex("chr/ch02451.itc", 0x25)
    LoadChrToIndex("chr/ch06500.itc", 0x26)
    LoadChrToIndex("monster/ch67450.itc", 0x27)
    LoadChrToIndex("chr/ch00056.itc", 0x28)
    LoadChrToIndex("chr/ch02953.itc", 0x29)
    LoadChrToIndex("chr/ch00952.itc", 0x2A)
    LoadChrToIndex("chr/ch02452.itc", 0x2B)
    LoadChrToIndex("monster/ch67453.itc", 0x2C)
    LoadChrToIndex("monster/ch67456.itc", 0x2D)
    LoadChrToIndex("monster/ch67457.itc", 0x2E)
    LoadChrToIndex("apl/ch51022.itc", 0x2F)
    LoadChrToIndex("chr/ch0295F.itc", 0x30)
    LoadEffect(0x0, "event\\ev602_01.eff")
    LoadEffect(0x1, "event\\ev10020.eff")
    LoadEffect(0x2, "event\\ev10022.eff")
    LoadEffect(0x3, "battle\\cr313000.eff")
    LoadEffect(0x4, "event\\ev10018.eff")
    LoadEffect(0x5, "event/ev17034.eff")
    LoadEffect(0x6, "battle\\ms00001.eff")
    LoadEffect(0x7, "event/eva01_01.eff")
    LoadEffect(0x8, "event/ev10023.eff")
    LoadEffect(0x9, "event/eva04_00.eff")
    SoundLoad(832)
    SoundLoad(825)
    SoundLoad(889)
    OP_68(50, 1400, 25050, 0)
    MoveCamera(27, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, -600, 200, 22600, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x109, 800, 200, 21900, 0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x10A, 0, -1400, -33000, 0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x108, 0, -1400, -34000, 0)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -3300, 200, 31200, 135)
    SetChrChipByIndex(0xB, 0x2C)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 0, 200, 29500, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFrame(0xFF, "bl_ato00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_ato01", 0x0, 0x1)
    PlayEffect(0x0, 0x0, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(832, 2, 100, 0)
    OP_68(50, 1400, 25050, 30000)
    MoveCamera(38, 11, 0, 30000)
    OP_6E(600, 30000)
    SetCameraDistance(15500, 30000)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(60, 80, -1, -1)
    Sleep(300)

    #A0039
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#N#30A呵呵呵……\x02",
        )
    )
    #Auto
    Sleep(2600)

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(100)
    SetChrSubChip(0xB, 0x1)
    OP_0D()
    Sleep(500)
    OP_82(0xC8, 0xC8, 0xBB8, 0x2BC)
    SetMessageWindowPos(60, 80, -1, -1)

    #A0040
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#N#5S#35A哈哈哈哈哈哈！\x07\x00\x02",
        )
    )
    #Auto
    Sleep(4600)

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    #C0041
    ChrTalk(
        0x101,
        "#6P#00010F啧，这是……！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        "#12P#10110F完全不起作用……！？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        "#6P#02705F哇、哇哇……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x9, 3, 0, 7)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0044
    ChrTalk(
        0x9,
        "#20A#5P#4S#10A哇啊啊啊啊啊啊啊……！\x02",
    )
    #Auto

    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1000, 14000, 0)
    MoveCamera(131, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(3000)
    OP_68(0, 1400, 26500, 2000)
    OP_6F(0x79)
    SetMessageWindowPos(40, 130, -1, -1)

    #A0045
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#N哎呀呀……\x01",
            "您擅自退场，会让我很难办哦。\x02",
        )
    )

    CloseMessageWindow()

    #A0046
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#N这里可不是能让您\x01",
            "为所欲为的自治州议会。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetCameraDistance(15500, 800)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    SetChrPos(0xA, 0, -1400, -3000, 0)
    Sound(258, 0, 100, 0)
    PlayEffect(0x2, 0x2, 0xB, 0x5, 0, 2000, 1500, 0, 0, 0, 1000, 1000, 1000, 0xA, 0, 0, 0, 0)
    Sleep(1000)
    Sound(321, 0, 100, 0)
    OP_68(0, -400, -5000, 2000)
    MoveCamera(143, 29, 0, 2000)
    SetCameraDistance(17000, 2000)
    WaitChrThread(0x9, 3)
    OP_90(0x9, 0, 200, 2500, 180)

    def lambda_20FE():
        OP_95(0xFE, 0, -1400, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20FE)
    WaitChrThread(0x9, 1)
    OP_64(0x9)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    OP_82(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sound(204, 0, 100, 0)
    Sound(833, 0, 100, 0)

    def lambda_214F():
        OP_A6(0xFE, 0x32, 0x32, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_214F)

    def lambda_2168():
        OP_9D(0xFE, 0x514, 0xFFFFFA88, 0xFFFFE4A8, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2168)

    #C0047
    ChrTalk(
        0x9,
        "#4S#11P#12A呜啊……！\x02",
    )
    #Auto

    WaitChrThread(0x9, 1)
    Sound(514, 0, 100, 0)
    SetChrSubChip(0x9, 0x1)
    Sleep(2000)
    Fade(500)
    OP_68(50, 1400, 25050, 0)
    MoveCamera(27, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)

    def lambda_21E3():
        OP_93(0x101, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21E3)
    Sleep(0)

    def lambda_21F3():
        OP_93(0x109, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_21F3)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    OP_0D()

    #C0048
    ChrTalk(
        0x109,
        "#5P#10107F啊……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0049
    ChrTalk(
        0x101,
        "#6P#00010F阿奈斯特，你……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    def lambda_22A8():
        OP_93(0xFE, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_22A8)
    SetMessageWindowPos(60, 80, -1, -1)

    #A0050
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#N呵呵，他还有利用价值，\x01",
            "我只是让他暂时昏迷而已。\x02",
        )
    )

    CloseMessageWindow()

    #A0051
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#N话说回来，你们现在\x01",
            "还有空担心别人吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x101, 3, 0, 12)
    BeginChrThread(0x11, 1, 0, 18)
    Sound(195, 0, 100, 0)
    Sound(212, 0, 100, 0)
    PlayEffect(0x1, 0x0, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    #C0052
    ChrTalk(
        0x101,
        "#6P#00010F唔……！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x109,
        "#12P#10107F这、这是……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 80, -1, -1)

    #A0054
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#N呵呵，教团的所有据点\x01",
            "都建设于七耀脉的正上方……\x02",
        )
    )

    CloseMessageWindow()

    #A0055
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#N在这种场所觉醒，\x01",
            "便可以开启\x01",
            "通往『Ｄ』的大门……\x02",
        )
    )

    CloseMessageWindow()

    #A0056
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#N哈哈哈，正如老师所说啊！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    SetScenarioFlags(0x0, 1)
    EndChrThread(0x101, 0x3)
    OP_82(0x32, 0x32, 0xBB8, 0x157C)
    Fade(500)
    OP_68(0, 1700, 29500, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(14500, 0)
    MoveCamera(0, 27, -25, 7000)
    SetCameraDistance(11500, 7000)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xB, 0x2E)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(620)
    SetChrSubChip(0xB, 0x1)
    Sleep(120)
    SetChrSubChip(0xB, 0x5)
    Sleep(120)
    SetChrSubChip(0xB, 0x6)
    Sleep(120)
    SetChrSubChip(0xB, 0x7)
    Sleep(120)
    SetChrSubChip(0xB, 0xA)
    Sound(308, 0, 50, 0)
    Sound(531, 0, 50, 0)
    Sound(540, 0, 50, 0)
    Sleep(1400)
    Sound(534, 0, 60, 0)
    SetChrSubChip(0xB, 0xB)
    Sleep(100)
    SetChrSubChip(0xB, 0xC)
    Sleep(100)
    SetChrSubChip(0xB, 0xD)
    Sleep(100)
    SetChrSubChip(0xB, 0xE)
    Sleep(2500)
    Sound(532, 0, 100, 0)
    Sleep(200)
    Sound(288, 0, 100, 0)
    Sound(308, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Sound(889, 0, 100, 0)
    SetChrSubChip(0xB, 0x16)
    BeginChrThread(0xB, 3, 0, 13)
    OP_82(0x12C, 0x12C, 0xBB8, 0x5DC)
    StopSound(832, 2000, 90)
    StopSound(825, 2000, 90)
    FadeToDark(1500, 16777215, -1)
    OP_0D()
    Sound(817, 0, 100, 0)
    StopEffect(0x0, 0x2)
    SetMapObjFrame(0xFF, "hasiraR", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasiraL", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_mae00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_mae01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_mae02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_ato00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bl_ato01", 0x1, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    ClearChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x8)
    OP_78(0x0, 0xB)
    OP_49()
    SetChrPos(0xB, 0, 0, 33000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x334)
    SetChrPos(0x101, -700, 200, 25200, 0)
    SetChrFlags(0x101, 0x8)
    SetChrPos(0x109, 700, 200, 24500, 0)
    SetChrFlags(0x109, 0x8)
    Sound(829, 0, 100, 0)
    Sleep(1000)
    StopSound(889, 2000, 100)
    OP_68(0, 4000, 32000, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8500, 0)
    PlayEffect(0x1, 0x0, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_68(0, 1500, 32000, 5000)
    FadeToBright(2000, 16777215)
    Sleep(500)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 2800, 32000, 0)
    MoveCamera(330, -20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8500, 0)
    OP_68(0, 3000, 32000, 6000)
    MoveCamera(30, -13, 0, 6000)
    SetCameraDistance(11500, 6000)
    BlurSwitch(0xBB8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(1005, 0, 100, 0)
    Sound(889, 0, 50, 0)
    OP_74(0x0, 0x14)
    OP_71(0x0, 0x334, 0x38E, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x38F, 0x3B6, 0x0, 0x20)
    OP_6F(0x79)
    Sleep(500)
    Fade(250)
    Sound(833, 0, 100, 0)
    OP_68(0, 4500, 33500, 0)
    MoveCamera(0, 45, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(7500, 0)
    OP_68(0, 3000, 33500, 1500)
    MoveCamera(0, 50, 0, 1500)
    SetCameraDistance(12500, 1500)
    OP_6F(0x79)
    Sleep(500)

    #C0057
    ChrTalk(
        0x109,
        "#N#10105F怎、怎么会……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0058
    ChrTalk(
        0x101,
        (
            "#N#00010F啧……\x01",
            "和那时的约亚西姆一样！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    CancelBlur(0)
    OP_68(0, 1700, 29200, 0)
    MoveCamera(33, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x109, 0x8)
    MoveCamera(33, 9, 5, 20000)
    SetCameraDistance(15500, 20000)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x3B7, 0x3C0, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x1E1, 0x208, 0x0, 0x20)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(1005, 0, 100, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W哼哼……这就是老师所达到的境界……\x02",
        )
    )

    CloseMessageWindow()

    #A0060
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W如此一来，我便可掌握万物之真实……\x02",
        )
    )

    CloseMessageWindow()
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x28B, 0x294, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x294, 0x2BC, 0x0, 0x20)

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W……………？………………\x02",
        )
    )

    CloseMessageWindow()

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W…………为何…………\x01",
            "……为何什么都看不到……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)

    #C0063
    ChrTalk(
        0x101,
        "#00005F#12P……？\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        "#10101F#12P他、他的样子似乎有些奇怪……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(1005, 0, 100, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W……我为何……！\x01",
            "为何看不到『Ｄ』……！？\x02",
        )
    )

    CloseMessageWindow()

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W我为何感受不到\x01",
            "真神的气息！？\x02",
        )
    )

    CloseMessageWindow()

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W这和老师说的不一样啊！！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_95(0x101, -700, 200, 26200, 4000, 0x0)
    Sound(30, 0, 100, 0)

    #C0068
    ChrTalk(
        0x101,
        (
            "#12P#00010F啧……你清醒点！\x02\x03",

            "#00007F约亚西姆告诉你的\x01",
            "未必就是真话吧！？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(1005, 0, 100, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W#4S闭、闭嘴！\x01",
            "闭嘴闭嘴闭嘴！！\x02",
        )
    )

    CloseMessageWindow()
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x2BC, 0x2C6, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x1E1, 0x208, 0x0, 0x20)

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W也罢……先把你们\x01",
            "两个血祭……\x02",
        )
    )

    CloseMessageWindow()

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W再回克洛斯贝尔，\x01",
            "夺回圣子和艾莉！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)

    #C0072
    ChrTalk(
        0x101,
        "#12P#00010F可、可恶……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0073
    ChrTalk(
        0x109,
        "#10107F罗伊德警官，危险！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(1000)
    Sound(834, 0, 100, 0)
    OP_68(0, 10000, 27900, 0)
    MoveCamera(330, 50, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    OP_68(0, 1000, 27900, 650)
    MoveCamera(0, 35, 0, 650)
    BeginChrThread(0xB, 3, 0, 8)
    OP_6F(0x79)
    Sound(833, 0, 100, 0)
    Sound(288, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 0, 200, 28000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 0, 200, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x7, 0xFF, 0x0, 0, 200, 28000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x5DC)
    BeginChrThread(0x109, 3, 0, 15)
    SetCameraDistance(19500, 1500)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)

    #C0074
    ChrTalk(
        0x101,
        "#00010F唔……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x109,
        "#10110F好可怕的怪物……\x02",
    )

    CloseMessageWindow()
    OP_68(0, 2600, 29000, 3000)
    MoveCamera(0, -3, 0, 3000)
    SetCameraDistance(14000, 3000)
    Sound(892, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x259, 0x280, 0x0, 0x0)
    Sleep(800)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, -500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, -500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, -500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, -500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, -500, 0, 28000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sound(288, 0, 70, 0)
    Sound(210, 0, 40, 0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x32, 0x0, 0x20)
    OP_6F(0x79)
    SetCameraDistance(15500, 10000)
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(1005, 0, 100, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W哼哼哼，永别了……\x02",
        )
    )

    CloseMessageWindow()

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W哀叹着自己的渺小，\x01",
            "化为尘埃吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sound(892, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_71(0x0, 0x411, 0x438, 0x0, 0x0)
    OP_79(0x0)
    Sound(833, 0, 100, 0)
    Sound(892, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x438, 0x441, 0x0, 0x0)
    Sleep(200)
    Sound(893, 0, 100, 0)
    OP_79(0x0)
    OP_68(0, 700, 16000, 0)
    MoveCamera(315, 25, -5, 0)
    OP_6E(700, 0)
    SetCameraDistance(15000, 0)
    CancelBlur(0)
    BeginChrThread(0xB, 3, 0, 11)
    OP_68(0, 1100, 18500, 1600)
    MoveCamera(323, 15, -5, 1600)
    SetCameraDistance(13500, 1600)
    BeginChrThread(0x108, 3, 0, 16)
    OP_6F(0x79)
    OP_68(1000, 1100, 27000, 0)
    MoveCamera(300, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_68(1000, 2100, 27000, 1000)
    MoveCamera(313, 5, 0, 1000)
    SetCameraDistance(13000, 1000)
    OP_0D()
    #Sound(3997, 255, 100, 0)    #voice#Arios

    #C0078
    ChrTalk(
        0x108,
        "#4S#8A#6P喝啊！\x02",
    )
    #Auto

    Sleep(600)
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x108, 3)
    SetMessageWindowPos(300, 70, -1, -1)

    #A0079
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#4S什么……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0xB, 3)
    Sound(2514, 255, 100, 0)    #voice#Dudley
    Sleep(300)
    OP_68(0, 3100, 32000, 1500)
    MoveCamera(327, -1, 0, 1500)
    SetCameraDistance(13500, 1500)
    Sleep(300)
    BeginChrThread(0x10A, 3, 0, 17)
    Sleep(300)
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(-1, 120, -1, -1)

    #A0080
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#4S#15A喔啊啊啊啊……！？\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0x10A, 3)
    Fade(500)
    OP_68(0, 2100, 27400, 0)
    MoveCamera(323, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 2000)
    BeginChrThread(0xB, 3, 0, 9)
    SetChrPos(0x101, -700, 200, 23000, 0)
    SetChrPos(0x109, 700, 200, 22500, 0)
    SetChrPos(0x108, -300, 200, 26700, 0)
    SetChrPos(0x10A, 2100, 200, 16400, 0)

    def lambda_33FA():
        OP_95(0xFE, 2100, 200, 23400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_33FA)
    OP_0D()
    SetChrChipByIndex(0x108, 0x25)
    SetChrSubChip(0x108, 0x1)
    Sound(809, 0, 50, 0)

    def lambda_3423():
        OP_9D(0xFE, 0xFFFFFED4, 0xC8, 0x607C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3423)
    WaitChrThread(0x108, 1)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x108, 0x2B)
    SetChrSubChip(0x108, 0x1)
    WaitChrThread(0x10A, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x10A, 0x2A)
    SetChrSubChip(0x10A, 0x0)

    #C0081
    ChrTalk(
        0x109,
        "#5P#10102F啊……！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00002F达德利警官、亚里欧斯先生！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(0, 1300, 24700, 0)
    MoveCamera(230, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    OP_0D()

    #C0083
    ChrTalk(
        0x10A,
        (
            "#6P#00604F哎呀呀……\x01",
            "总算赶上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x108,
        (
            "#01402F罗伊德、诺艾尔上士，\x01",
            "多亏你们一直坚持到现在。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#00002F#5P二位才是，\x01",
            "幸好你们平安无事……！\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x10A,
        (
            "#6P#00606F哼，对手多达十架，\x01",
            "确实花了一番工夫。\x02\x03",

            "#00601F有话稍后再说！\x01",
            "先制服这家伙！\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x108,
        (
            "#01407F对手非同寻常！\x01",
            "我们要全力以赴！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_35F3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35F3)

    def lambda_360C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_360C)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0088
    ChrTalk(
        0x101,
        "#00007F#5P#4S是！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0089
    ChrTalk(
        0x109,
        "#10107F#5P#4S遵命！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 2100, 27400, 2000)
    MoveCamera(323, 9, 0, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    Sound(892, 0, 100, 0)
    OP_71(0x0, 0x410, 0x438, 0x0, 0x0)
    OP_79(0x0)
    MoveCamera(323, 9, -10, 500)
    SetCameraDistance(14500, 500)
    Sound(893, 0, 100, 0)
    Sound(833, 0, 60, 0)
    OP_74(0x0, 0x14)
    OP_71(0x0, 0x438, 0x442, 0x0, 0x0)
    OP_79(0x0)
    SetScenarioFlags(0x0, 0)
    Battle("BattleInfo_320", 0x30200011, 0x0, 0x100, 0x23, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xB, 0x80)
    StopEffect(0x7, 0x0)
    Call(0, 19)
    Return()

    # Function_6_1A83 end

    def Function_7_374A(): pass

    label("Function_7_374A")

    ClearChrFlags(0x9, 0x4)

    def lambda_3754():
        OP_95(0xFE, -3300, 200, 18500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3754)
    WaitChrThread(0x9, 1)

    def lambda_3772():
        OP_95(0xFE, 0, 200, 13500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3772)
    WaitChrThread(0x9, 1)

    def lambda_3790():
        OP_95(0xFE, 0, -1400, -5500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3790)
    WaitChrThread(0x9, 1)
    Return()

    # Function_7_374A end

    def Function_8_37AA(): pass

    label("Function_8_37AA")

    OP_74(0x0, 0xA)
    OP_71(0x0, 0x209, 0x230, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x231, 0x258, 0x0, 0x20)
    Return()

    # Function_8_37AA end

    def Function_9_37CE(): pass

    label("Function_9_37CE")

    OP_74(0x0, 0x14)
    OP_71(0x0, 0x4BA, 0x4CE, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x31, 0x0, 0x20)
    Return()

    # Function_9_37CE end

    def Function_10_37F2(): pass

    label("Function_10_37F2")

    Sound(831, 0, 100, 0)
    OP_70(0x0, 0x44D)
    OP_71(0x0, 0x44D, 0x460, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x460, 0x488, 0x0, 0x20)
    Return()

    # Function_10_37F2 end

    def Function_11_381C(): pass

    label("Function_11_381C")

    OP_70(0x0, 0x438)
    OP_74(0x0, 0xA)
    ClearMapObjFlags(0x0, 0x20)
    OP_71(0x0, 0x42A, 0x441, 0x0, 0x0)
    OP_79(0x0)
    OP_70(0x0, 0x441)
    Return()

    # Function_11_381C end

    def Function_12_383E(): pass

    label("Function_12_383E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3862")
    OP_82(0x32, 0x32, 0xBB8, 0x2710)
    Sleep(10000)
    Jump("Function_12_383E")

    label("loc_3862")

    Return()

    # Function_12_383E end

    def Function_13_3863(): pass

    label("Function_13_3863")

    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4CE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4CE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4CE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4EC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4EC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4EC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x50A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x50A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x50A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x528), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x528), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x528), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x546), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x546), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x546), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x564), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x564), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x564), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x582), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x582), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x582), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x5A0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x5A0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x5A0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x5BE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x5BE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x5BE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x5FA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x5FA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x5FA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x618), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x618), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x618), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x636), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x636), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x636), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x654), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x654), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x654), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_3863 end

    def Function_14_3A59(): pass

    label("Function_14_3A59")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(700)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x2)
    Sound(809, 0, 80, 0)

    def lambda_3A87():
        OP_9D(0xFE, 0xFFFFFD44, 0xC8, 0x5DC0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A87)
    WaitChrThread(0x101, 1)
    Sound(326, 0, 40, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sleep(700)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)

    def lambda_3AC1():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AC1)
    Return()

    # Function_14_3A59 end

    def Function_15_3AD6(): pass

    label("Function_15_3AD6")

    SetChrChipByIndex(0x109, 0x29)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x1000)

    def lambda_3AED():
        OP_96(0xFE, 0x2BC, 0xC8, 0x5BCC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3AED)

    def lambda_3B07():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3B07)
    WaitChrThread(0x109, 1)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 0x30)
    SetChrSubChip(0x109, 0x0)
    Return()

    # Function_15_3AD6 end

    def Function_16_3B32(): pass

    label("Function_16_3B32")

    SetChrPos(0x108, 0, 200, 8000, 0)
    SetChrFlags(0x108, 0x1000)
    SetChrChipByIndex(0x108, 0x25)
    SetChrSubChip(0x108, 0x0)
    SetChrChip(0x0, 0x108, 0x32, 0x12C)
    Sound(250, 0, 100, 0)

    def lambda_3B63():
        OP_95(0xFE, 0, 200, 19500, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3B63)
    WaitChrThread(0x108, 1)
    Sound(251, 0, 100, 0)

    def lambda_3B87():
        OP_9D(0xFE, 0xFA0, 0xC8, 0x6338, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3B87)
    WaitChrThread(0x108, 1)
    Sound(326, 0, 100, 0)
    SetChrChipByIndex(0x108, 0x2B)
    SetChrSubChip(0x108, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_3BBC():
        OP_9D(0xFE, 0xFFFFFE0C, 0xC8, 0x68B0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3BBC)
    Sleep(300)
    Sound(534, 0, 100, 0)
    Sound(540, 0, 100, 0)
    Sleep(200)
    Sound(288, 0, 100, 0)
    Sound(859, 0, 100, 0)
    Sound(196, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0x108, 0x0, 0, 1000, 1200, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x108, 0x0, 0, 1000, 1200, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x108, 0x3)
    OP_82(0x12C, 0x12C, 0xBB8, 0x1F4)
    BeginChrThread(0xB, 3, 0, 10)
    WaitChrThread(0x108, 1)
    Sound(326, 0, 100, 0)
    ClearChrFlags(0x108, 0x1000)
    SetChrChip(0x1, 0x108, 0x0, 0x0)
    Return()

    # Function_16_3B32 end

    def Function_17_3C99(): pass

    label("Function_17_3C99")

    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -2000, 3500, 18000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 70, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -2000, 3500, 32000, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_71(0x0, 0x489, 0x4BA, 0x0, 0x0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xC8)
    Sleep(300)
    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 2000, 3000, 18000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 70, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 2000, 3000, 32000, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xC8)
    Sleep(300)
    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1500, 17500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 70, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1500, 31500, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xC8)
    Sleep(300)
    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 4000, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 70, 0)
    Sound(353, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 4000, 32500, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xC8)
    Return()

    # Function_17_3C99 end

    def Function_18_3EED(): pass

    label("Function_18_3EED")

    Sound(825, 2, 0, 0)
    Sleep(200)
    OP_25(0x339, 0xA)
    Sleep(200)
    OP_25(0x339, 0x14)
    Sleep(200)
    OP_25(0x339, 0x1E)
    Sleep(200)
    OP_25(0x339, 0x28)
    Sleep(200)
    OP_25(0x339, 0x32)
    Sleep(200)
    OP_25(0x339, 0x3C)
    Sleep(200)
    OP_25(0x339, 0x46)
    Sleep(200)
    OP_25(0x339, 0x50)
    Sleep(200)
    OP_25(0x339, 0x5A)
    Sleep(200)
    OP_25(0x339, 0x64)
    Return()

    # Function_18_3EED end

    def Function_19_3F3A(): pass

    label("Function_19_3F3A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xFE, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch02950.itc", 0x20)
    LoadChrToIndex("chr/ch02951.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch00951.itc", 0x23)
    LoadChrToIndex("chr/ch02450.itc", 0x24)
    LoadChrToIndex("chr/ch02451.itc", 0x25)
    LoadChrToIndex("apl/ch51022.itc", 0x26)
    LoadChrToIndex("apl/ch50523.itc", 0x27)
    LoadChrToIndex("chr/ch11400.itc", 0x28)
    LoadChrToIndex("chr/ch00056.itc", 0x29)
    LoadChrToIndex("chr/ch02452.itc", 0x2A)
    LoadChrToIndex("chr/ch02456.itc", 0x2B)
    LoadChrToIndex("chr/ch02952.itc", 0x2C)
    LoadChrToIndex("chr/ch00952.itc", 0x2D)
    LoadChrToIndex("apl/ch51024.itc", 0x2E)
    LoadChrToIndex("apl/ch51025.itc", 0x2F)
    LoadChrToIndex("apl/ch51028.itc", 0x30)
    LoadChrToIndex("chr/ch0295F.itc", 0x31)
    LoadChrToIndex("apl/ch51021.itc", 0x32)
    SoundLoad(3314)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis223.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04300.itp")
    LoadEffect(0x9, "event\\ev620_00.eff")
    LoadEffect(0x0, "event\\ev614_01.eff")
    LoadEffect(0x1, "event\\ev614_02.eff")
    LoadEffect(0x2, "battle\\cr024200.eff")
    LoadEffect(0x3, "battle\\cr024201.eff")
    LoadEffect(0x4, "battle\\cr024102.eff")
    LoadEffect(0x5, "battle\\btgun00.eff")
    LoadEffect(0x6, "battle\\ms00001.eff")
    LoadEffect(0x7, "event\\ev10032.eff")
    LoadEffect(0x8, "event\\ev10033.eff")
    SoundLoad(825)
    SoundLoad(1004)
    SetChrPos(0x101, -200, 200, 24000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x109, 200, 200, 22400, 0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x10A, 1600, 200, 22800, 0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x108, -1600, 200, 23100, 0)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    SetChrPos(0xD, -200, 200, 24000, 0)
    SetChrPos(0xE, 200, 200, 22400, 0)
    SetChrPos(0xF, 1600, 200, 22800, 0)
    SetChrPos(0x10, -1600, 200, 23100, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x9, -1000, -1400, -4000, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x8, 0, 200, 30000, 270)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_78(0x1, 0xB)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    OP_49()
    SetChrPos(0xB, 0, 0, 33000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x1, 0x1E)
    OP_70(0x1, 0x65)
    OP_71(0x1, 0x65, 0x78, 0x0, 0x20)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 0, -1400, -3000, 0)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFrame(0xFF, "hasiraR", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasiraL", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_mae00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_mae01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_mae02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bl_ato00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bl_ato01", 0x1, 0x1)
    OP_7D(0xFF, 0xC8, 0xBE, 0x0, 0x1770)
    OP_11(0xA0, 0x0, 0x2D, 0xF, 0x64, 0x1770)
    OP_68(0, 2700, 34000, 0)
    MoveCamera(319, 35, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(12500, 0)
    MoveCamera(329, 25, 0, 6000)
    SetCameraDistance(15500, 6000)
    Sound(825, 2, 100, 0)
    BeginChrThread(0x11, 1, 0, 28)
    BeginChrThread(0xB, 3, 0, 21)
    FadeToBright(1000, 0)
    Sound(1005, 0, 100, 0)
    Sound(1031, 0, 100, 0)
    Sound(833, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    SetMessageWindowPos(-1, 120, -1, -1)

    #A0090
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S#30A#60W哦哦哦哦哦哦……！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(2000)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1900, 28300, 0)
    MoveCamera(329, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    CancelBlur(0)
    OP_0D()

    #C0091
    ChrTalk(
        0x108,
        "#01401F#5P唔……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)

    #C0092
    ChrTalk(
        0x101,
        (
            "#00007F#3314V#30W#5P#4S#19A来了！\x01",
            "大家小心！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0093
    ChrTalk(
        0x109,
        "#10110F#5P#6A！\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x10A,
        "#00610F#5P#6A啧！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_71(0x1, 0xC8, 0xF0, 0x0, 0x0)
    Sleep(1100)
    Sound(1033, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    PlayEffect(0x9, 0x6, 0xB, 0x0, 3000, 200, -2400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0x7, 0xB, 0x0, -3000, 200, -2400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_79(0x1)
    OP_71(0x1, 0xF1, 0x118, 0x0, 0x20)
    Sleep(100)
    OP_68(0, 1000, 21700, 1000)
    MoveCamera(300, 25, 0, 1000)
    OP_6F(0x79)
    MoveCamera(285, 23, 0, 4500)
    SetCameraDistance(13500, 4500)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Sound(1006, 0, 100, 0)
    Sound(607, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 23)
    Sleep(100)
    PlayEffect(0x0, 0x0, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x109, 3, 0, 24)
    Sleep(100)
    PlayEffect(0x0, 0x1, 0xE, 0x0, 0, 0, 0, 30, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x10A, 3, 0, 25)
    Sleep(100)
    PlayEffect(0x0, 0x2, 0xF, 0x0, 0, 0, 0, 70, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x108, 3, 0, 26)
    Sleep(100)
    PlayEffect(0x0, 0x3, 0x10, 0x0, 0, 0, 0, 130, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x6, 0xFF, 0xD, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xE, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xF, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0x10, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xD, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xE, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xF, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0x10, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xD, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xE, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0xF, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x6, 0xFF, 0x10, 0x5, 0, 900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(514, 0, 100, 0)
    Sound(253, 0, 100, 0)
    Sound(248, 0, 100, 0)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    PlayEffect(0x1, 0xFF, 0xD, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xE, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xF, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x10, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x6, 0x2)
    StopEffect(0x7, 0x2)
    BeginChrThread(0xB, 3, 0, 37)
    Sleep(1000)
    OP_6F(0x79)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    LoadEffect(0x2, "event\\ev10030.eff")
    LoadEffect(0x3, "event\\ev10031.eff")
    LoadEffect(0x4, "event\\ev10034.eff")
    LoadEffect(0x5, "event\\ev10035.eff")
    LoadEffect(0x6, "event\\ev10036.eff")
    OP_68(0, 2700, 33000, 2000)
    MoveCamera(321, 4, 0, 2000)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    Sound(1004, 2, 100, 0)
    PlayEffect(0x7, 0x0, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(-1, 120, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #A0095
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S#60W#20A哦哦哦哦哦哦哦……！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(800)

    #C0096
    ChrTalk(
        0x101,
        "#00010F#N#6P这是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0097
    ChrTalk(
        0x109,
        "#10110F#N#6P在、在融化……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0098
    ChrTalk(
        0x10A,
        (
            "#00610F#N#6P就是在约亚西姆的死亡情况\x01",
            "报告中提到的那种现象吗……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(-1, 120, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #A0099
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#30A啊啊啊啊啊啊啊……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #A0100
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#45A……不要……\x01",
            "#4S不要啊！！！！！！\x02",
        )
    )
    #Auto

    Sleep(800)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    CloseMessageWindow()
    Sleep(300)

    #A0101
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#60A我不想死……\x01",
            "#4S……我不想死啊……！！！\x07\x00\x02",
        )
    )
    #Auto

    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_4DDE():
        OP_93(0x101, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4DDE)
    Sleep(0)

    def lambda_4DEE():
        OP_93(0x109, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4DEE)
    Sleep(0)

    def lambda_4DFE():
        OP_93(0x10A, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_4DFE)
    Sleep(0)

    def lambda_4E0E():
        OP_93(0x108, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_4E0E)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x108, 0)
    Fade(500)
    OP_68(0, 1900, 25300, 0)
    MoveCamera(330, 7, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    #C0102
    ChrTalk(
        0x109,
        "#10108F……这………\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x108,
        "#01403F……真可悲啊。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#00010F唔……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_4EB3():
        OP_95(0xFE, 0, 200, 27500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4EB3)
    OP_68(0, 2000, 32299, 2000)
    MoveCamera(0, 3, 0, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    SetCameraDistance(14890, 30000)

    #C0105
    ChrTalk(
        0x109,
        "#10105F#N#12P罗伊德警官！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0106
    ChrTalk(
        0x10A,
        "#00607F#N#12P喂，你干什么……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x101, 1)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x2E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0107
    ChrTalk(
        0x101,
        (
            "#6P#00007F阿奈斯特！\x01",
            "保持清醒！\x02\x03",

            "不要迷失自我！\x01",
            "你就是你啊！\x02",
        )
    )

    CloseMessageWindow()
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(-1, 70, -1, -1)

    #A0108
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#40A……咕咕咕……咯咯咯……？\x07\x00\x02",
        )
    )
    Sleep(500)
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    #C0109
    ChrTalk(
        0x101,
        (
            "#6P#00010F你和约亚西姆不同，\x01",
            "并没有服下\x01",
            "大量的红色『真知』！\x02\x03",

            "#00007F所以你还有救的！\x01",
            "绝对不要放弃！\x02",
        )
    )

    CloseMessageWindow()
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(-1, 70, -1, -1)

    #A0110
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#35A咕咕……嘎嘎嘎……\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    #C0111
    ChrTalk(
        0x10A,
        "#00600F#N#12P班宁斯，你……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0112
    ChrTalk(
        0x109,
        "#10108F#N#12P……罗伊德警官………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(1004, 1000, 100)
    OP_25(0x339, 0x28)
    Fade(500)
    OP_68(0, 2300, 31000, 0)
    MoveCamera(213, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    SetChrPos(0x109, 0, 200, 20400, 0)
    SetChrPos(0x10A, 2500, 200, 21200, 0)
    SetChrPos(0x108, -2500, 200, 21200, 0)
    BeginChrThread(0x109, 3, 0, 27)
    BeginChrThread(0xB, 2, 0, 35)
    StopEffect(0x0, 0x2)
    PlayEffect(0x8, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    MoveCamera(223, 29, 0, 15000)
    SetCameraDistance(15500, 15000)
    OP_0D()
    EndChrThread(0xB, 0x3)
    StopEffect(0x0, 0x2)
    Sleep(300)
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(250, 140, -1, -1)

    #A0113
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W呜呜呜……啊啊……\x02",
        )
    )

    CloseMessageWindow()

    #A0114
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W……为……为什么……\x02",
        )
    )

    CloseMessageWindow()

    #A0115
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W我已经如此……\x01",
            "………你为何还要………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    #C0116
    ChrTalk(
        0x101,
        (
            "#00006F……这是两回事。\x02\x03",

            "#00008F你的确犯了罪。\x02\x03",

            "但我认为你的罪行\x01",
            "并没有深重到应该\x01",
            "死在这种地方的程度。\x02\x03",

            "#00013F更何况，如果你死了，\x01",
            "艾莉和麦克道尔议长\x01",
            "肯定都会很伤心的。\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x101, 0x4)
    Sleep(90)
    SetChrSubChip(0x101, 0x5)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0117
    ChrTalk(
        0x101,
        (
            "#00007F所以……\x01",
            "你一定要找回自我！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1005, 0, 100, 0)
    SetMessageWindowPos(250, 140, -1, -1)

    #A0118
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W……艾莉……麦克道尔先生……\x02",
        )
    )

    CloseMessageWindow()

    #A0119
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W……对不起……我为何要……\x02",
        )
    )

    CloseMessageWindow()

    #A0120
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#40A……唔……！\x01",
            "……啊啊啊啊啊啊啊啊啊！\x07\x00\x02",
        )
    )
    #Auto

    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1004, 2, 100, 0)
    OP_25(0x339, 0x64)
    BeginChrThread(0xB, 3, 0, 21)
    BeginChrThread(0xB, 2, 0, 36)
    StopEffect(0x1, 0x2)
    PlayEffect(0x7, 0x0, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
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
    Sleep(1000)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x101, 0x6)

    #C0121
    ChrTalk(
        0x101,
        "#00010F#5P唔，不行吗……！？\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x109,
        (
            "#10113F#5P#N没、没有任何\x01",
            "办法了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0123
    ChrTalk(
        0x10A,
        (
            "#00610F啧，这种情况完全超出了\x01",
            "我们的专业范畴啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x108,
        (
            "#01400F#5P#N不用慌……\x02\x03",

            "#01404F看样子，『专家』已经\x01",
            "及时赶到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1388)
    TurnDirection(0x10A, 0x108, 500)

    #C0125
    ChrTalk(
        0x10A,
        "#00605F#6P什么……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x80)
    Sleep(300)

    #N0126
    NpcTalk(
        0xC,
        "青年的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#40W#24A『端坐于天国的吾主啊』。\x02",
        )
    )
    Sleep(300)
    #Auto

    CloseMessageWindow()

    #N0127
    NpcTalk(
        0xC,
        "青年的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#40W#50A『请用您的光芒，\x01",
            "  唤回被魔鬼诱惑的迷途羔羊吧……』\x02",
        )
    )
    Sleep(900)
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xB, 0x3)
    BeginChrThread(0xB, 2, 0, 35)
    StopEffect(0x0, 0x2)
    Sound(1002, 0, 100, 0)
    BeginChrThread(0x11, 2, 0, 33)
    PlayEffect(0x8, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x7, 0xB, 0x1, 0, 2000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(300)
    Sound(692, 0, 80, 0)
    Sleep(700)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)

    def lambda_5779():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5779)
    Sleep(50)

    def lambda_5789():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5789)
    Sleep(50)

    def lambda_5799():
        OP_93(0x10A, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_5799)
    Sleep(50)

    def lambda_57A9():
        OP_93(0x108, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_57A9)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x108, 0)

    #C0128
    ChrTalk(
        0x101,
        "#12P#00005F咦……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x109,
        "#10105F教会的圣言……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x11, 1, 0, 29)
    EndChrThread(0x11, 0x2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    BeginChrThread(0x11, 2, 0, 34)
    Fade(500)
    OP_68(0, 1000, 0, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10500, 0)

    def lambda_584B():
        OP_95(0xFE, 0, 200, 16000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_584B)

    def lambda_5865():

        label("loc_5865")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5865")

    QueueWorkItem2(0x101, 2, lambda_5865)

    def lambda_5877():

        label("loc_5877")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5877")

    QueueWorkItem2(0x109, 2, lambda_5877)

    def lambda_5889():

        label("loc_5889")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5889")

    QueueWorkItem2(0x10A, 2, lambda_5889)

    def lambda_589B():

        label("loc_589B")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_589B")

    QueueWorkItem2(0x108, 2, lambda_589B)
    OP_68(0, 1000, 2000, 3500)
    MoveCamera(0, 17, 0, 3500)
    SetCameraDistance(15500, 3500)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1300, 16000, 0)
    MoveCamera(221, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x10A, 0x8)
    SetChrFlags(0x108, 0x8)
    MoveCamera(213, 21, 0, 3000)
    SetCameraDistance(14500, 3000)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0xC, 1)

    #C0130
    ChrTalk(
        0x10A,
        "#00605F你是……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xC,
        (
            "#04303F抱歉，没时间了，\x01",
            "请让我立刻处理吧。\x02\x03",

            "#04300F你可以稍微退后些吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#00005F哎？啊……是！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 1500)

    def lambda_59BF():
        OP_95(0xFE, 0, 200, 27600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_59BF)
    Sleep(1500)
    EndChrThread(0x11, 0x2)
    BeginChrThread(0x11, 1, 0, 30)
    BeginChrThread(0x11, 2, 0, 33)
    Fade(500)
    OP_68(0, 1500, 29500, 0)
    MoveCamera(310, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16000, 2500)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x10A, 0x8)
    ClearChrFlags(0x108, 0x8)
    SetChrPos(0x101, -1300, 200, 25500, 180)
    SetChrPos(0x109, 1300, 200, 23000, 180)
    SetChrPos(0x10A, 2200, 200, 24000, 180)
    SetChrPos(0x108, -2200, 200, 24000, 180)
    OP_0D()
    Sleep(1500)

    def lambda_5A84():
        OP_96(0xFE, 0x1F4, 0xC8, 0x5BCC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A84)
    Sleep(300)

    def lambda_5AA1():
        OP_96(0xFE, 0xFFFFFE0C, 0xC8, 0x61A8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AA1)
    WaitChrThread(0xC, 1)
    SetMessageWindowPos(250, 70, -1, -1)

    #A0133
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "呜呜呜呜……\x01",
            "……啊啊啊啊啊啊……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0134
    ChrTalk(
        0xC,
        (
            "#6P#04308F唔，已经到崩溃边缘了。\x02\x03",

            "#04304F……不过，总算是\x01",
            "控制住了。\x02\x03",

            "#04301F接下来──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 2300, 27600, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_68(0, 1300, 27600, 2000)
    Sleep(1000)
    BeginChrThread(0x11, 1, 0, 31)
    Sound(531, 0, 100, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x2F)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 3, 0, 20)
    Sound(357, 0, 100, 0)
    PlayEffect(0x2, 0x2, 0xFF, 0x0, 0, 250, 27600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    Sleep(300)

    #C0135
    ChrTalk(
        0xC,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#04303F#50W#30A『于深渊中闪耀光芒的苍之刻印啊！』\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    MoveCamera(315, 17, 0, 1500)
    OP_6F(0x79)
    SetCameraDistance(13500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sound(895, 0, 100, 0)
    Sound(222, 0, 100, 0)
    PlayEffect(0x3, 0x3, 0xFF, 0x0, 0, 500, 27600, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xC8, 0xDC, 0x0, 0x5DC)
    Sleep(1500)
    CancelBlur(0)
    Sleep(500)

    #C0136
    ChrTalk(
        0xC,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#04301F#50W#61A『化作光明，驱散昏暗的邪气，\x01",
            "  为迷途之人指明道路吧！』\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sound(1002, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 500, 27600, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xC, 0x3)
    SetChrSubChip(0xC, 0x4)
    Sleep(90)
    SetChrSubChip(0xC, 0x5)
    BeginChrThread(0xB, 3, 0, 22)
    OP_68(0, 2300, 31600, 1500)
    MoveCamera(327, 3, 0, 1500)
    SetCameraDistance(16500, 1500)
    BeginChrThread(0x11, 3, 0, 32)
    Sound(222, 0, 100, 0)
    PlayEffect(0x5, 0x6, 0xB, 0x1, 0, 2000, 0, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x10A, 0x2)
    EndChrThread(0x108, 0x2)

    def lambda_5DDA():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5DDA)
    Sleep(30)

    def lambda_5DEA():
        OP_93(0x10A, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_5DEA)
    Sleep(30)

    def lambda_5DFA():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5DFA)
    Sleep(30)

    def lambda_5E0A():
        OP_93(0x108, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_5E0A)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x108, 0)
    OP_6F(0x79)
    Sleep(500)

    #C0137
    ChrTalk(
        0x101,
        "#00005F#30W#N#6P#20A这、这是……\x02",
    )
    #Auto

    Sleep(2500)

    #C0138
    ChrTalk(
        0x10A,
        "#00605F#30W#N#6P#15A那道光到底是……\x02",
    )
    #Auto

    Sleep(1500)
    SetCameraDistance(19500, 2000)
    Sound(829, 0, 100, 0)
    Sound(1002, 0, 100, 0)
    Sound(833, 0, 80, 0)
    StopSound(825, 2000, 30)
    StopSound(1004, 2000, 30)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x11, 0x3)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    Sleep(1000)
    OP_68(0, 1100, 28800, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetMapObjFlags(0x1, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    EndChrThread(0xB, 0xFF)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xB3, 0x35, 0x5E, 0xA, 0xC8, 0x0)

    def lambda_5F36():
        TurnDirection(0x101, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5F36)
    Sleep(0)

    def lambda_5F46():
        TurnDirection(0x109, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5F46)
    Sleep(0)

    def lambda_5F56():
        TurnDirection(0x10A, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_5F56)
    Sleep(0)

    def lambda_5F66():
        TurnDirection(0x108, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_5F66)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x108, 0)
    SetCameraDistance(17000, 2000)
    FadeToBright(2000, 16777215)
    OP_0D()

    #C0139
    ChrTalk(
        0x109,
        "#10102F#30W#N#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0140
    ChrTalk(
        0x101,
        "#00002F#30W#N#6P恢、恢复了……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0141
    ChrTalk(
        0xC,
        "#04306F#30W#5P呼……总算成功了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_600A():
        OP_95(0xFE, 0, 200, 29300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_600A)
    WaitChrThread(0xC, 1)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x30)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    OP_0D()
    SetCameraDistance(16500, 1500)

    def lambda_6054():
        OP_96(0xFE, 0xFFFFFF38, 0xC8, 0x6A40, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6054)
    Sleep(200)

    def lambda_6071():
        OP_96(0xFE, 0xC8, 0xC8, 0x6464, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6071)
    Sleep(200)

    def lambda_608E():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_608E)

    def lambda_609B():
        OP_96(0xFE, 0x76C, 0xC8, 0x6720, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_609B)
    Sleep(200)

    def lambda_60B8():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_60B8)

    def lambda_60C5():
        OP_96(0xFE, 0xFFFFF894, 0xC8, 0x6590, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_60C5)
    WaitChrThread(0x101, 1)
    Sleep(800)

    #C0142
    ChrTalk(
        0x101,
        "#00013F#6P他、他的情况如何？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xC,
        (
            "#04304F嗯，只是昏过去了。\x02\x03",

            "#04300F虽然还要昏迷好几天，\x01",
            "但已经没有生命危险了。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        "#00006F#6P太、太好了……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 1)
    WaitChrThread(0x10A, 1)
    WaitChrThread(0x108, 1)

    #C0145
    ChrTalk(
        0x109,
        "#6P#10112F呼……终于松了一口气。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x10A,
        (
            "#6P#00607F先、先不说这些，\x01",
            "你到底是什么人！？\x02\x03",

            "看起来倒像是教会的神父……\x01",
            "但你为何会来这种地方！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0xC8, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x20)
    OP_0D()
    TurnDirection(0xC, 0x108, 500)

    #C0147
    ChrTalk(
        0xC,
        (
            "#11P#04305F咦，亚里欧斯先生。\x02\x03",

            "您没有把我的事情\x01",
            "告诉这几位吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x108,
        (
            "#01404F呵呵，因为你说过，\x01",
            "不知能否及时赶到啊。\x02\x03",

            "#01402F考虑到你的身份，\x01",
            "我就谨慎起见，没有多说。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xC,
        (
            "#11P#04304F原来如此，那可多谢啦。\x02\x03",

            "#04311F哎呀～您还是\x01",
            "如此心细呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x108,
        (
            "#01404F呵呵，彼此彼此。\x02\x03",

            "#01402F你能前来，\x01",
            "真是帮了大忙，谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#00011F#6P那个……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x10A,
        (
            "#6P#00606F哼，有人自作主张，\x01",
            "暗中为我们上了一道保险啊。\x02\x03",

            "#00600F看样子，阁下应该是隶属于\x01",
            "七耀教会封圣省的『星杯骑士』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x109,
        "#3P#10105F封圣省、星杯骑士……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        (
            "#00005F#6P莫非就是负责回收\x01",
            "『古代遗物』的那个……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(150)

    #C0155
    ChrTalk(
        0xC,
        "#11P#04304F哈哈，瞒不过您的眼睛呢。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0156
    AnonymousTalk(
        0xC,
        (
            "初次见面，\x01",
            "我是七耀教会·星杯骑士团的\x01",
            "凯文·格拉汉姆。\x02\x03",

            "之前接到亚里欧斯先生的联络，\x01",
            "特此前来协助。\x02\x03",

            "请多多指教……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(17000, 2000)
    StopSound(129, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t5000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_3F3A end

    def Function_20_65C6(): pass

    label("Function_20_65C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65F2")
    SetChrSubChip(0xC, 0x0)
    Sleep(100)
    SetChrSubChip(0xC, 0x1)
    Sleep(100)
    SetChrSubChip(0xC, 0x2)
    Sleep(100)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    Jump("Function_20_65C6")

    label("loc_65F2")

    Return()

    # Function_20_65C6 end

    def Function_21_65F3(): pass

    label("Function_21_65F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6617")
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_21_65F3")

    label("loc_6617")

    Return()

    # Function_21_65F3 end

    def Function_22_6618(): pass

    label("Function_22_6618")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_663C")
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_22_6618")

    label("loc_663C")

    Return()

    # Function_22_6618 end

    def Function_23_663D(): pass

    label("Function_23_663D")

    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_6650():
        OP_9D(0xFE, 0xFFFFFC18, 0xC8, 0x5014, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6650)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Return()

    # Function_23_663D end

    def Function_24_6675(): pass

    label("Function_24_6675")

    SetChrChipByIndex(0x109, 0x31)
    SetChrSubChip(0x109, 0x2)
    Sound(809, 0, 100, 0)

    def lambda_6688():
        OP_9D(0xFE, 0x5DC, 0xC8, 0x4A38, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6688)
    WaitChrThread(0x109, 1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    Sleep(1500)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrSubChip(0x109, 0x0)
    Sound(531, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x3)
    Sleep(50)
    Sound(2450, 255, 100, 0)    #voice#Noel
    Sound(539, 0, 100, 0)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    Sound(539, 0, 100, 0)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x109, 0x5)
    Sleep(30)
    SetChrSubChip(0x109, 0x4)
    Sleep(50)
    SetChrSubChip(0x109, 0x3)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    Return()

    # Function_24_6675 end

    def Function_25_6A4F(): pass

    label("Function_25_6A4F")

    SetChrFlags(0x10A, 0x20)

    def lambda_6A59():
        OP_93(0xFE, 0x13B, 0x2BC)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_6A59)
    SetChrChipByIndex(0x10A, 0x32)
    SetChrSubChip(0x10A, 0x0)

    def lambda_6A6E():
        OP_9D(0xFE, 0xDAC, 0xC8, 0x4F4C, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_6A6E)
    WaitChrThread(0x10A, 1)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    Sleep(1500)
    SetChrChipByIndex(0x10A, 0x2D)
    SetChrSubChip(0x10A, 0x0)
    Sleep(100)
    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1100, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(300)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(100)
    Sound(2512, 255, 100, 0)    #voice#Dudley
    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1100, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(300)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(100)
    Sound(567, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 1100, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(300)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    ClearChrFlags(0x10A, 0x20)
    Return()

    # Function_25_6A4F end

    def Function_26_6BB8(): pass

    label("Function_26_6BB8")

    SetChrFlags(0x108, 0x20)

    def lambda_6BC2():
        OP_93(0xFE, 0x3C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_6BC2)
    SetChrChipByIndex(0x108, 0x25)
    SetChrSubChip(0x108, 0x3)

    def lambda_6BD7():
        OP_9D(0xFE, 0xFFFFF060, 0xC8, 0x526C, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_6BD7)
    WaitChrThread(0x108, 1)
    Sound(540, 0, 100, 0)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    Sleep(100)
    Sound(881, 0, 100, 0)
    PlayEffect(0x4, 0x1, 0x108, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_6C46():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_6C46)
    SetChrChipByIndex(0x108, 0x2A)
    SetChrSubChip(0x108, 0x3)
    Sleep(1000)
    StopEffect(0x1, 0x2)
    Sound(259, 0, 100, 0)
    Sound(3988, 255, 100, 0)    #voice#Arios
    PlayEffect(0x2, 0xFF, 0x108, 0x5, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x108, 0x5, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x108, 0x2B)
    SetChrSubChip(0x108, 0x0)
    Sleep(100)
    SetChrSubChip(0x108, 0x1)
    Sleep(2500)
    SetChrSubChip(0x108, 0x2)
    Sleep(100)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    ClearChrFlags(0x108, 0x20)
    Return()

    # Function_26_6BB8 end

    def Function_27_6D09(): pass

    label("Function_27_6D09")


    def lambda_6D0E():
        OP_96(0xFE, 0x0, 0xC8, 0x5B68, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6D0E)
    Sleep(100)

    def lambda_6D2B():
        OP_96(0xFE, 0x7D0, 0xC8, 0x5E88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_6D2B)
    Sleep(100)

    def lambda_6D48():
        OP_96(0xFE, 0xFFFFF830, 0xC8, 0x5E88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_6D48)
    Return()

    # Function_27_6D09 end

    def Function_28_6D5E(): pass

    label("Function_28_6D5E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D77")
    Sound(892, 0, 50, 0)
    Sleep(1150)
    Jump("Function_28_6D5E")

    label("loc_6D77")

    Return()

    # Function_28_6D5E end

    def Function_29_6D78(): pass

    label("Function_29_6D78")

    OP_25(0x339, 0x5F)
    OP_25(0x3EC, 0x5F)
    Sleep(100)
    OP_25(0x339, 0x5A)
    OP_25(0x3EC, 0x5A)
    Sleep(100)
    OP_25(0x339, 0x55)
    OP_25(0x3EC, 0x55)
    Sleep(100)
    OP_25(0x339, 0x50)
    OP_25(0x3EC, 0x50)
    Sleep(100)
    OP_25(0x339, 0x4B)
    OP_25(0x3EC, 0x4B)
    Sleep(100)
    OP_25(0x339, 0x46)
    OP_25(0x3EC, 0x46)
    Sleep(100)
    OP_25(0x339, 0x41)
    OP_25(0x3EC, 0x41)
    Sleep(100)
    OP_25(0x339, 0x3C)
    OP_25(0x3EC, 0x3C)
    Sleep(100)
    OP_25(0x339, 0x32)
    OP_25(0x3EC, 0x32)
    Sleep(100)
    OP_25(0x339, 0x28)
    OP_25(0x3EC, 0x28)
    Return()

    # Function_29_6D78 end

    def Function_30_6DE4(): pass

    label("Function_30_6DE4")

    OP_25(0x339, 0x32)
    OP_25(0x3EC, 0x32)
    Sleep(100)
    OP_25(0x339, 0x3C)
    OP_25(0x3EC, 0x3C)
    Sleep(100)
    OP_25(0x339, 0x41)
    OP_25(0x3EC, 0x41)
    Sleep(100)
    OP_25(0x339, 0x46)
    OP_25(0x3EC, 0x46)
    Sleep(100)
    OP_25(0x339, 0x4B)
    OP_25(0x3EC, 0x4B)
    Sleep(100)
    OP_25(0x339, 0x50)
    OP_25(0x3EC, 0x50)
    Return()

    # Function_30_6DE4 end

    def Function_31_6E24(): pass

    label("Function_31_6E24")

    OP_25(0x339, 0x4B)
    OP_25(0x3EC, 0x4B)
    Sleep(100)
    OP_25(0x339, 0x46)
    OP_25(0x3EC, 0x46)
    Sleep(100)
    OP_25(0x339, 0x41)
    OP_25(0x3EC, 0x41)
    Sleep(100)
    OP_25(0x339, 0x3C)
    OP_25(0x3EC, 0x3C)
    Sleep(100)
    OP_25(0x339, 0x32)
    OP_25(0x3EC, 0x32)
    Sleep(100)
    OP_25(0x339, 0x28)
    OP_25(0x3EC, 0x28)
    Return()

    # Function_31_6E24 end

    def Function_32_6E64(): pass

    label("Function_32_6E64")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E7D")
    Sound(934, 0, 60, 0)
    Sleep(1500)
    Jump("Function_32_6E64")

    label("loc_6E7D")

    Return()

    # Function_32_6E64 end

    def Function_33_6E7E(): pass

    label("Function_33_6E7E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E97")
    Sound(1034, 0, 100, 0)
    Sleep(1000)
    Jump("Function_33_6E7E")

    label("loc_6E97")

    Return()

    # Function_33_6E7E end

    def Function_34_6E98(): pass

    label("Function_34_6E98")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EB1")
    Sound(1034, 0, 50, 0)
    Sleep(1000)
    Jump("Function_34_6E98")

    label("loc_6EB1")

    Return()

    # Function_34_6E98 end

    def Function_35_6EB2(): pass

    label("Function_35_6EB2")

    OP_74(0x1, 0x1E)
    Sleep(300)
    OP_74(0x1, 0x1D)
    Sleep(300)
    OP_74(0x1, 0x1C)
    Sleep(300)
    OP_74(0x1, 0x1B)
    Sleep(300)
    OP_74(0x1, 0x1A)
    Sleep(300)
    OP_74(0x1, 0x19)
    Sleep(300)
    OP_74(0x1, 0x18)
    Sleep(300)
    OP_74(0x1, 0x17)
    Sleep(300)
    OP_74(0x1, 0x16)
    Sleep(300)
    OP_74(0x1, 0x15)
    Sleep(300)
    OP_74(0x1, 0x14)
    Sleep(300)
    OP_74(0x1, 0x13)
    Sleep(300)
    OP_74(0x1, 0x12)
    Sleep(300)
    OP_74(0x1, 0x11)
    Sleep(300)
    OP_74(0x1, 0x10)
    Sleep(300)
    OP_74(0x1, 0xF)
    Return()

    # Function_35_6EB2 end

    def Function_36_6F20(): pass

    label("Function_36_6F20")

    OP_74(0x1, 0xF)
    Sleep(300)
    OP_74(0x1, 0x10)
    Sleep(300)
    OP_74(0x1, 0x11)
    Sleep(300)
    OP_74(0x1, 0x12)
    Sleep(300)
    OP_74(0x1, 0x13)
    Sleep(300)
    OP_74(0x1, 0x14)
    Sleep(300)
    OP_74(0x1, 0x15)
    Sleep(300)
    OP_74(0x1, 0x16)
    Sleep(300)
    OP_74(0x1, 0x17)
    Sleep(300)
    OP_74(0x1, 0x18)
    Sleep(300)
    OP_74(0x1, 0x19)
    Sleep(300)
    OP_74(0x1, 0x1A)
    Sleep(300)
    OP_74(0x1, 0x1B)
    Sleep(300)
    OP_74(0x1, 0x1C)
    Sleep(300)
    OP_74(0x1, 0x1D)
    Sleep(300)
    OP_74(0x1, 0x1E)
    Return()

    # Function_36_6F20 end

    def Function_37_6F8E(): pass

    label("Function_37_6F8E")

    OP_71(0x1, 0x119, 0x136, 0x0, 0x0)
    OP_79(0x1)
    Sound(831, 0, 100, 0)
    Sound(830, 0, 50, 0)
    OP_71(0x1, 0x384, 0x38E, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x38F, 0x3B6, 0x0, 0x20)
    Return()

    # Function_37_6F8E end

    SaveToFile()

Try(main)
