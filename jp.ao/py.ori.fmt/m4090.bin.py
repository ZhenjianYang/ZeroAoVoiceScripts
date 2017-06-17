from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "アーネスト",             # 1
        "ハルトマン元議長",       # 2
        "ダミーハルトマン",       # 3
        "魔人アーネスト",         # 4
        "法衣姿の青年",           # 5
        "ダミーエフェクト",       # 6
        "ダミーエフェクト",       # 7
        "ダミーエフェクト",       # 8
        "ダミーエフェクト",       # 9
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
        "Function_4_1BB5",         # 04, 4
        "Function_5_1BF0",         # 05, 5
        "Function_6_1C03",         # 06, 6
        "Function_7_3A06",         # 07, 7
        "Function_8_3A66",         # 08, 8
        "Function_9_3A8A",         # 09, 9
        "Function_10_3AAE",        # 0A, 10
        "Function_11_3AD8",        # 0B, 11
        "Function_12_3AFA",        # 0C, 12
        "Function_13_3B1F",        # 0D, 13
        "Function_14_3D15",        # 0E, 14
        "Function_15_3D92",        # 0F, 15
        "Function_16_3DEE",        # 10, 16
        "Function_17_3F55",        # 11, 17
        "Function_18_41A9",        # 12, 18
        "Function_19_41F6",        # 13, 19
        "Function_20_6A4C",        # 14, 20
        "Function_21_6A79",        # 15, 21
        "Function_22_6A9E",        # 16, 22
        "Function_23_6AC3",        # 17, 23
        "Function_24_6AFB",        # 18, 24
        "Function_25_6ED5",        # 19, 25
        "Function_26_703E",        # 1A, 26
        "Function_27_718F",        # 1B, 27
        "Function_28_71E4",        # 1C, 28
        "Function_29_71FE",        # 1D, 29
        "Function_30_726A",        # 1E, 30
        "Function_31_72AA",        # 1F, 31
        "Function_32_72EA",        # 20, 32
        "Function_33_7304",        # 21, 33
        "Function_34_731E",        # 22, 34
        "Function_35_7338",        # 23, 35
        "Function_36_73A6",        # 24, 36
        "Function_37_7414",        # 25, 37
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
        "#00007F（あ……！）\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0)

    #C0002
    ChrTalk(
        0x109,
        "#6P#10101F（いた……！）\x02",
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
            "#02613Fクク……\x01",
            "ヨアヒム師から聞いた通りだ。\x02\x03",

            "#02610Fこの場所ならば私の目的も\x01",
            "万事滞りなく達せられるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "#6P#02703Fクッ……いい加減にしないか！\x02\x03",

            "#02701Fヨアヒムといい貴様といい、\x01",
            "気が触れたようなことを……！\x02\x03",

            "き、貴様らの妄想に\x01",
            "私を巻き込むんじゃない！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0005
    ChrTalk(
        0x8,
        (
            "#11P#02613Fハハ、あなたこそ人の事を\x01",
            "とやかく言えるような立場かな？\x02\x03",

            "#02610F《楽園》でしたか……\x01",
            "あんな場所を利用していた割には\x01",
            "ずいぶんと偉そうな物言いですね？\x02",
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
            "#6P#02705Fあ、あれは教団の手先に\x01",
            "騙されて連れて行かれただけで……\x02\x03",

            "#02703Fあんな悪趣味な場所と知っていれば\x01",
            "断じて首を突っ込んだりしたものか！\x02\x03",

            "#02701Fおまけに妙な薬まで盛られて……\x01",
            "わ、私の方こそ完全な被害者だ！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    #C0007
    ChrTalk(
        0x8,
        (
            "#11P#02613Fやれやれ、そのような釈明が\x01",
            "世間に通用するとお思いですか？\x02\x03",

            "#02610Fクロスベルタイムズが独占取材したら\x01",
            "さぞ盛り上がってくれるでしょうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        "#6P#02701Fぐっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2090, 255, 100, 0)    #voice#Lloyd

    #N0009
    NpcTalk(
        0x101,
        "ロイドの声",
        "#30W#12Aそこまでだ……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B6D():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_B6D)
    Sleep(50)

    def lambda_B7D():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_B7D)
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

    def lambda_BFE():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BFE)
    Sleep(100)

    def lambda_C1B():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C1B)
    Sleep(500)

    def lambda_C38():
        OP_95(0xFE, 0, 200, 28500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C38)
    OP_6F(0x79)

    #C0010
    ChrTalk(
        0x9,
        "#11P#02705Fおお、お前たちは……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)

    #C0011
    ChrTalk(
        0x8,
        (
            "#02605F#11Pおやおや、君たちか。\x02\x03",

            "#02613F面倒な連中を撒いたと思ったら\x01",
            "とんだザコが紛れ込んで来たものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#6P#00013Fその巨大な祭壇……\x01",
            "ここがロッジの最奥か。\x02\x03",

            "#00007Fアリオスさんたちはどうした！？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#02610F#11Pああ、《風の剣聖》と\x01",
            "捜査一課のエースどのか。\x02\x03",

            "#02613Fさすがに厄介だったので\x01",
            "足止めさせてもらったよ。\x02\x03",

            "今頃、魔導人形１０体相手に\x01",
            "翻弄されている頃だろう。\x02",
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
        "#6P#00010Fなっ……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x109,
        "#6P#10110Fあの化物を１０体も……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#02613F#11Pおかげで師から受け継いだ\x01",
            "コマを使いきってしまったがね。\x02\x03",

            "#02610Fだが、これであの連中も\x01",
            "確実に始末できるだろう。\x02\x03",

            "私はゆっくりと、この聖なる場所で\x01",
            "目的を果たさせてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#6P#00007Fさせるか……！\x02",
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
        "#6P#10107F手を上げて投降しなさい！\x02",
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
            "やれやれ……\x01",
            "状況が判っていないようだな。\x02\x03",

            "それにしても、エリィの姿が\x01",
            "なぜ見えないのかと思っていたが……\x02\x03",

            "なるほど、一時的に支援課を離れて\x01",
            "マクダエル先生の手伝いをしているのか。\x02",
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
        "#6P#00010Fくっ……！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x109,
        (
            "#6P#10101Fま、まさか\x01",
            "ロイドさんの記憶を……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06613F#11Pさらに新市長と新議長による\x01",
            "新たな体制・法案作りへの協力……\x02\x03",

            "#06610Fなるほど、そうする事で\x01",
            "これまで以上に支援課が動きやすい\x01",
            "政治的な足場を作るつもりか。\x02\x03",

            "#06613Fフン、新市長の提案らしいが\x01",
            "なかなか興味深い試みじゃないか。\x02",
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
            "#06606F#11Pだが、エリィのような人材を\x01",
            "警察ごときに埋もれさせておくのは\x01",
            "愚かとしか言いようがないな。\x02\x03",

            "#06600Fふむ、私が市長となった暁には\x01",
            "特務支援課は解体させてもらおう。\x02\x03",

            "そして彼女は私の専属秘書として\x01",
            "存分に才能を発揮してもらう……\x02\x03",

            "#06604Fうんうん、それがいい。\x01",
            "そうしよう！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148E")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆前編実績エリィとの絆達成済\x01",      # 0
            "◆前編実績エリィとの絆未達成\x01",      # 1
            "◆変更しない\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1479"),
        (1, "loc_1481"),
        (2, "loc_1489"),
        (SWITCH_DEFAULT, "loc_1489"),
    )


    label("loc_1479")

    SetScenarioFlags(0x25, 3)
    Jump("loc_148E")

    label("loc_1481")

    ClearScenarioFlags(0x25, 3)
    Jump("loc_148E")

    label("loc_1489")

    Jump("loc_148E")

    label("loc_148E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_15D4")
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0025
    ChrTalk(
        0x101,
        (
            "#6P#00007F#4Sふざけるな……！\x02\x03",

            "#3S#00010Fあんたのふざけた妄想に\x01",
            "エリィを巻き込ませるものか！\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x109,
        "#6P#10105F（ロイドさん、凄い迫力……）\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06603F#11Pフン……\x01",
            "そもそも、君のような小僧が\x01",
            "エリィと釣り合うものか。\x02\x03",

            "#06611F彼女の目を覚まさせるためにも\x01",
            "悪い芽は摘み取らせてもらおう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_16B4")

    label("loc_15D4")


    #C0028
    ChrTalk(
        0x101,
        "#6P#00013Fこいつ……！\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x109,
        (
            "#6P#10106F本気で言ってるんだとしたら\x01",
            "相当アレな感じですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#06613F#11Pクク……\x01",
            "君にはヨアヒム師の仇もある。\x02\x03",

            "#06610Fエリィの未練を断ち切るためにも\x01",
            "悪い芽は摘み取らせてもらおう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_16B4")

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

    def lambda_1780():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1780)
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

    def lambda_17E2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_17E2)

    def lambda_17F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_17F3)
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
        "#6P#02705Fひいいいっ……！？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x109,
        "#12P#10110Fこ、これが……！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#6P#00010Fああ、紅いグノーシスによる\x01",
            "魔人化#6Rデモナイズ#だ！\x02",
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
            "フフ、この聖なる場所では\x01",
            "いつもの覚醒も殊更#4Rことさら#心地よい……\x02",
        )
    )

    CloseMessageWindow()

    #A0035
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "大いなる望みを叶える前の\x01",
            "ささやかなる供物……\x02",
        )
    )

    CloseMessageWindow()

    #A0036
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "せいぜい足掻いて、もがいて、\x01",
            "のた打ち回ってもらうぞ！\x07\x00\x02",
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
        "#6P#00007Fそうはいくか……！\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        "#12P#10107F対象一名、制圧を開始します！\x02",
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

    def lambda_1B60():
        OP_9D(0xFE, 0x0, 0xC8, 0x53FC, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1B60)
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

    def Function_4_1BB5(): pass

    label("Function_4_1BB5")

    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x9, 0x87, 0x1F4)
    Sleep(500)

    def lambda_1BD6():
        OP_96(0xFE, 0xFFFFF31C, 0xC8, 0x79E0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BD6)
    WaitChrThread(0x9, 1)
    Return()

    # Function_4_1BB5 end

    def Function_5_1BF0(): pass

    label("Function_5_1BF0")

    Sleep(2500)
    Sound(805, 0, 100, 0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    Return()

    # Function_5_1BF0 end

    def Function_6_1C03(): pass

    label("Function_6_1C03")

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
            "#5P#N#30Aククク……\x02",
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
            "#5P#N#5S#35Aハーッハッハッハッハッ！\x07\x00\x02",
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
        "#6P#00010Fくっ、これは……！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        "#12P#10110Fぜんぜん効いてない……！？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        "#6P#02705Fひ、ひいいいっ……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x9, 3, 0, 7)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0044
    ChrTalk(
        0x9,
        "#20A#5P#4S#10Aわあああああああっ……！\x02",
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
            "#5P#Nおやおや……\x01",
            "勝手な退場は困りますねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #A0046
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#Nあなたが好き勝手していた\x01",
            "自治州議会ではないのだから。\x07\x00\x02",
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

    def lambda_22A8():
        OP_95(0xFE, 0, -1400, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_22A8)
    WaitChrThread(0x9, 1)
    OP_64(0x9)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    OP_82(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sound(204, 0, 100, 0)
    Sound(833, 0, 100, 0)

    def lambda_22F9():
        OP_A6(0xFE, 0x32, 0x32, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_22F9)

    def lambda_2312():
        OP_9D(0xFE, 0x514, 0xFFFFFA88, 0xFFFFE4A8, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2312)

    #C0047
    ChrTalk(
        0x9,
        "#4S#11P#12Aぐぎゃっ……！\x02",
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

    def lambda_2391():
        OP_93(0x101, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2391)
    Sleep(0)

    def lambda_23A1():
        OP_93(0x109, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_23A1)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    OP_0D()

    #C0048
    ChrTalk(
        0x109,
        "#5P#10107Fああっ……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0049
    ChrTalk(
        0x101,
        "#6P#00010Fアーネスト、貴様……！\x02",
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

    def lambda_245E():
        OP_93(0xFE, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_245E)
    SetMessageWindowPos(60, 80, -1, -1)

    #A0050
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#Nフフ、まだ利用価値はあるから\x01",
            "軽く気絶させただけさ。\x02",
        )
    )

    CloseMessageWindow()

    #A0051
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#Nそれより、他人のことを\x01",
            "心配している余裕はあるのかな？\x07\x00\x02",
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
        "#6P#00010Fくっ……！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x109,
        "#12P#10107Fこ、これは……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 80, -1, -1)

    #A0054
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#Nクク、教団のロッジはすべて\x01",
            "七耀脈の真上に作られている……\x02",
        )
    )

    CloseMessageWindow()

    #A0055
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#Nその真上で覚醒することで\x01",
            "《Ｄ》へと至る扉を\x01",
            "開くことが可能になる……\x02",
        )
    )

    CloseMessageWindow()

    #A0056
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#Nフハハ、師から聞いた通りだな！\x07\x00\x02",
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
        "#N#10105Fそ、そんな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0058
    ChrTalk(
        0x101,
        (
            "#N#00010Fくっ……\x01",
            "あの時のヨアヒムと同じか！\x02",
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
            "#60Wクク……コレゾ師ノ至ッタ境地……\x02",
        )
    )

    CloseMessageWindow()

    #A0060
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60Wコレデ総テノ真実ハ我ノモノニ……\x02",
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
            "#60W…………ナゼダ…………\x01",
            "……ナゼ何モ視エナイ……？\x02",
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
        "#10101F#12Pな、何だか様子が変です……\x02",
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
            "#60W……ナゼダ……！\x01",
            "ナゼ《Ｄ》ガ視エナイ……！？\x02",
        )
    )

    CloseMessageWindow()

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W真ナル神ノ息吹ガ\x01",
            "ドウシテ感ジラレナイノダ！？\x02",
        )
    )

    CloseMessageWindow()

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60Wコレデハ話ガ違ウデハナイカ！！\x02",
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
            "#12P#00010Fクッ……しっかりしろ！\x02\x03",

            "#00007Fヨアヒムが真実を語っていたとは\x01",
            "限らないだろう！？\x02",
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
            "#60W#4Sダ、ダマレ！\x01",
            "ダマレダマレダマレエエッ！\x02",
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
            "#60Wマアイイ……マズハ手始メニ\x01",
            "貴様ラヲ贄トシテクレル……\x02",
        )
    )

    CloseMessageWindow()

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60Wソノ上デくろすべるヘ帰還シ、\x01",
            "御子トえりぃヲ奪ッテクレルワ！\x02",
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
        "#12P#00010Fこ、このっ……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0073
    ChrTalk(
        0x109,
        "#10107Fロイドさん、危ない！\x02",
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
        "#00010Fクッ……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x109,
        "#10110Fなんて化物……\x02",
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
            "#60Wククク、ソレデハサラバダ……\x02",
        )
    )

    CloseMessageWindow()

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W矮小ナル己ノ身ヲ嘆イテ\x01",
            "塵ト化スガイイ──！\x02",
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
        "#4S#8A#6Pはあああああッ！\x02",
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
            "#4Sナ……！\x02",
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
            "#4S#15Aグオオオオッ……！？\x02",
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

    def lambda_367E():
        OP_95(0xFE, 2100, 200, 23400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_367E)
    OP_0D()
    SetChrChipByIndex(0x108, 0x25)
    SetChrSubChip(0x108, 0x1)
    Sound(809, 0, 50, 0)

    def lambda_36A7():
        OP_9D(0xFE, 0xFFFFFED4, 0xC8, 0x607C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_36A7)
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
        "#5P#10102Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00002Fダドリーさん、アリオスさん！\x02",
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
            "#6P#00604Fやれやれ……\x01",
            "何とか間に合ったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x108,
        (
            "#01402Fロイド、ノエル曹長。\x01",
            "よく持ちこたえてくれた。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#00002F#5Pお２人の方こそ\x01",
            "よくご無事で……！\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x10A,
        (
            "#6P#00606Fフン、さすがに１０体は\x01",
            "手こずらせてもらったがな。\x02\x03",

            "#00601F話は後だ！\x01",
            "まずはコイツを無力化する！\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x108,
        (
            "#01407F尋常な相手ではない！\x01",
            "我々の全力をぶつけるぞ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38A5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38A5)

    def lambda_38BE():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_38BE)
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
        "#00007F#5P#4Sはい！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0089
    ChrTalk(
        0x109,
        "#10107F#5P#4Sイエス・サー！\x02",
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

    # Function_6_1C03 end

    def Function_7_3A06(): pass

    label("Function_7_3A06")

    ClearChrFlags(0x9, 0x4)

    def lambda_3A10():
        OP_95(0xFE, -3300, 200, 18500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A10)
    WaitChrThread(0x9, 1)

    def lambda_3A2E():
        OP_95(0xFE, 0, 200, 13500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A2E)
    WaitChrThread(0x9, 1)

    def lambda_3A4C():
        OP_95(0xFE, 0, -1400, -5500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A4C)
    WaitChrThread(0x9, 1)
    Return()

    # Function_7_3A06 end

    def Function_8_3A66(): pass

    label("Function_8_3A66")

    OP_74(0x0, 0xA)
    OP_71(0x0, 0x209, 0x230, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x231, 0x258, 0x0, 0x20)
    Return()

    # Function_8_3A66 end

    def Function_9_3A8A(): pass

    label("Function_9_3A8A")

    OP_74(0x0, 0x14)
    OP_71(0x0, 0x4BA, 0x4CE, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x31, 0x0, 0x20)
    Return()

    # Function_9_3A8A end

    def Function_10_3AAE(): pass

    label("Function_10_3AAE")

    Sound(831, 0, 100, 0)
    OP_70(0x0, 0x44D)
    OP_71(0x0, 0x44D, 0x460, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x460, 0x488, 0x0, 0x20)
    Return()

    # Function_10_3AAE end

    def Function_11_3AD8(): pass

    label("Function_11_3AD8")

    OP_70(0x0, 0x438)
    OP_74(0x0, 0xA)
    ClearMapObjFlags(0x0, 0x20)
    OP_71(0x0, 0x42A, 0x441, 0x0, 0x0)
    OP_79(0x0)
    OP_70(0x0, 0x441)
    Return()

    # Function_11_3AD8 end

    def Function_12_3AFA(): pass

    label("Function_12_3AFA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B1E")
    OP_82(0x32, 0x32, 0xBB8, 0x2710)
    Sleep(10000)
    Jump("Function_12_3AFA")

    label("loc_3B1E")

    Return()

    # Function_12_3AFA end

    def Function_13_3B1F(): pass

    label("Function_13_3B1F")

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

    # Function_13_3B1F end

    def Function_14_3D15(): pass

    label("Function_14_3D15")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(700)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x2)
    Sound(809, 0, 80, 0)

    def lambda_3D43():
        OP_9D(0xFE, 0xFFFFFD44, 0xC8, 0x5DC0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D43)
    WaitChrThread(0x101, 1)
    Sound(326, 0, 40, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sleep(700)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)

    def lambda_3D7D():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D7D)
    Return()

    # Function_14_3D15 end

    def Function_15_3D92(): pass

    label("Function_15_3D92")

    SetChrChipByIndex(0x109, 0x29)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x1000)

    def lambda_3DA9():
        OP_96(0xFE, 0x2BC, 0xC8, 0x5BCC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3DA9)

    def lambda_3DC3():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3DC3)
    WaitChrThread(0x109, 1)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 0x30)
    SetChrSubChip(0x109, 0x0)
    Return()

    # Function_15_3D92 end

    def Function_16_3DEE(): pass

    label("Function_16_3DEE")

    SetChrPos(0x108, 0, 200, 8000, 0)
    SetChrFlags(0x108, 0x1000)
    SetChrChipByIndex(0x108, 0x25)
    SetChrSubChip(0x108, 0x0)
    SetChrChip(0x0, 0x108, 0x32, 0x12C)
    Sound(250, 0, 100, 0)

    def lambda_3E1F():
        OP_95(0xFE, 0, 200, 19500, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3E1F)
    WaitChrThread(0x108, 1)
    Sound(251, 0, 100, 0)

    def lambda_3E43():
        OP_9D(0xFE, 0xFA0, 0xC8, 0x6338, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3E43)
    WaitChrThread(0x108, 1)
    Sound(326, 0, 100, 0)
    SetChrChipByIndex(0x108, 0x2B)
    SetChrSubChip(0x108, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_3E78():
        OP_9D(0xFE, 0xFFFFFE0C, 0xC8, 0x68B0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3E78)
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

    # Function_16_3DEE end

    def Function_17_3F55(): pass

    label("Function_17_3F55")

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

    # Function_17_3F55 end

    def Function_18_41A9(): pass

    label("Function_18_41A9")

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

    # Function_18_41A9 end

    def Function_19_41F6(): pass

    label("Function_19_41F6")

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
            "#4S#30A#60Wオオオオオオッ……！\x07\x00\x02",
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
        "#01401F#5Pむっ……！\x02",
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
            "#00007F#3314V#30W#5P#4S#19A──来る！\x01",
            "気を付けてください！\x02",
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
        "#10110F#5P#6Aっ！\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x10A,
        "#00610F#5P#6Aチッ！\x02",
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
            "#4S#60W#20Aオオオオオンン……！\x07\x00\x02",
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
        "#00010F#N#6Pこれは……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0097
    ChrTalk(
        0x109,
        "#10110F#N#6Pと、溶けてる……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0098
    ChrTalk(
        0x10A,
        (
            "#00610F#N#6Pヨアヒム死亡時の報告に\x01",
            "あったやつか……！\x02",
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
            "#60W#30Aアアアアアアア……\x02",
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
            "#60W#45A……イヤダ……\x01",
            "#4Sイヤダアアアアアアッ！！\x02",
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
            "#60W#60A死ニタクナイ……\x01",
            "#4S……死ニタクナイヨオオオッ……！\x07\x00\x02",
        )
    )
    #Auto

    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_50BC():
        OP_93(0x101, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_50BC)
    Sleep(0)

    def lambda_50CC():
        OP_93(0x109, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_50CC)
    Sleep(0)

    def lambda_50DC():
        OP_93(0x10A, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_50DC)
    Sleep(0)

    def lambda_50EC():
        OP_93(0x108, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_50EC)
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
        "#10108F……っ………\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x108,
        "#01403F……哀れな。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#00010Fくっ……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_5191():
        OP_95(0xFE, 0, 200, 27500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5191)
    OP_68(0, 2000, 32299, 2000)
    MoveCamera(0, 3, 0, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    SetCameraDistance(14890, 30000)

    #C0105
    ChrTalk(
        0x109,
        "#10105F#N#12Pロイドさん！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0106
    ChrTalk(
        0x10A,
        "#00607F#N#12Pおい、何を……！？\x02",
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
            "#6P#00007Fアーネスト！\x01",
            "気をしっかり持て！\x02\x03",

            "自分を見失うな！\x01",
            "あんたは、あんただろう！\x02",
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
            "#60W#40A……グググ……ギギギッ……？\x07\x00\x02",
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
            "#6P#00010Fヨアヒムと違ってあんたは\x01",
            "紅いグノーシスを\x01",
            "大量に飲んだわけじゃない！\x02\x03",

            "#00007Fだったら助かる！\x01",
            "絶対に諦めるんじゃない！\x02",
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
            "#60W#35Aググ……ガガガ……\x07\x00\x02",
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
        "#00600F#N#12Pバニングス、お前……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0112
    ChrTalk(
        0x109,
        "#10108F#N#12P……ロイドさん………\x02",
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
            "#60Wウウウ……アア……\x02",
        )
    )

    CloseMessageWindow()

    #A0114
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W……ド……ドウシテ……\x02",
        )
    )

    CloseMessageWindow()

    #A0115
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60Wココマデシタ私ニ……\x01",
            "………ドウシテ貴様ハ………\x07\x00\x02",
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
            "#00006F……それとこれとは話が別だ。\x02\x03",

            "#00008Fあんたは確かに罪を犯した。\x02\x03",

            "でも、だからといって\x01",
            "こんな場所で死んでいいほど\x01",
            "罪深かったとは思えない。\x02\x03",

            "#00013Fそれに、あんたが死んだら\x01",
            "エリィやマクダエル議長だって\x01",
            "きっと哀しむだろう。\x02",
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
            "#00007Fだから……\x01",
            "絶対に自分を取り戻してくれ！\x02",
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
            "#60W……えりぃ……まくだえる先生……\x02",
        )
    )

    CloseMessageWindow()

    #A0119
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W……スマナイ……ドウシテ私ハ……\x02",
        )
    )

    CloseMessageWindow()

    #A0120
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#40A……クッ……！\x01",
            "……アアアアアアアアアッ！\x07\x00\x02",
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
        "#00010F#5Pクッ、駄目か……！？\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x109,
        (
            "#10113F#5P#Nな、何とか\x01",
            "ならないんでしょうか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0123
    ChrTalk(
        0x10A,
        (
            "#00610Fくっ、こんなケース、\x01",
            "さすがに専門外だぞ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x108,
        (
            "#01400F#5P#Nいや……\x02\x03",

            "#01404F──どうやら“専門家”が\x01",
            "間に合ってくれたようだ。\x02",
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
        "#00605F#6Pなに……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x80)
    Sleep(300)

    #N0126
    NpcTalk(
        0xC,
        "青年の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#40W#24A『天に坐#2Rいま#す我らが主よ』\x02",
        )
    )
    Sleep(300)
    #Auto

    CloseMessageWindow()

    #N0127
    NpcTalk(
        0xC,
        "青年の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#40W#50A『魔に引かれし哀れな迷い子を\x01",
            "  御身の光で呼び戻さんことを……』\x02",
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

    def lambda_5B1B():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5B1B)
    Sleep(50)

    def lambda_5B2B():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5B2B)
    Sleep(50)

    def lambda_5B3B():
        OP_93(0x10A, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_5B3B)
    Sleep(50)

    def lambda_5B4B():
        OP_93(0x108, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_5B4B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x108, 0)

    #C0128
    ChrTalk(
        0x101,
        "#12P#00005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x109,
        "#10105F教会の聖句……？\x02",
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

    def lambda_5BED():
        OP_95(0xFE, 0, 200, 16000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5BED)

    def lambda_5C07():

        label("loc_5C07")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5C07")

    QueueWorkItem2(0x101, 2, lambda_5C07)

    def lambda_5C19():

        label("loc_5C19")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5C19")

    QueueWorkItem2(0x109, 2, lambda_5C19)

    def lambda_5C2B():

        label("loc_5C2B")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5C2B")

    QueueWorkItem2(0x10A, 2, lambda_5C2B)

    def lambda_5C3D():

        label("loc_5C3D")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5C3D")

    QueueWorkItem2(0x108, 2, lambda_5C3D)
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
        "#00605Fあんたは……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xC,
        (
            "#04303Fスンマセン、時間がないんで\x01",
            "すぐに処置させてもらいますわ。\x02\x03",

            "#04300F君、ちょっと退#2Rど#いてもらえるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#00005Fえ、あ……はい！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 1500)

    def lambda_5D8D():
        OP_95(0xFE, 0, 200, 27600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5D8D)
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

    def lambda_5E52():
        OP_96(0xFE, 0x1F4, 0xC8, 0x5BCC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5E52)
    Sleep(300)

    def lambda_5E6F():
        OP_96(0xFE, 0xFFFFFE0C, 0xC8, 0x61A8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E6F)
    WaitChrThread(0xC, 1)
    SetMessageWindowPos(250, 70, -1, -1)

    #A0133
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ググググ……\x01",
            "……アアアアアアッ……！\x07\x00\x02",
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
            "#6P#04308Fふむ、崩壊一歩手前やね。\x02\x03",

            "#04304F……けど、何とか\x01",
            "踏みとどまってくれたか。\x02\x03",

            "#04301Fこれなら──\x02",
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
            "#5P#04303F#50W#30A『我が深淵にて煌く蒼の刻印よ』\x02",
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
            "#5P#04301F#50W#61A『光となって昏き瘴気を払い、\x01",
            "  迷い子の道を指し示せ──！』\x02",
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

    def lambda_61BC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_61BC)
    Sleep(30)

    def lambda_61CC():
        OP_93(0x10A, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_61CC)
    Sleep(30)

    def lambda_61DC():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_61DC)
    Sleep(30)

    def lambda_61EC():
        OP_93(0x108, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_61EC)
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
        "#00005F#30W#N#6P#20Aこ、これは……\x02",
    )
    #Auto

    Sleep(2500)

    #C0138
    ChrTalk(
        0x10A,
        "#00605F#30W#N#6P#15Aあの光は一体……\x02",
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

    def lambda_631A():
        TurnDirection(0x101, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_631A)
    Sleep(0)

    def lambda_632A():
        TurnDirection(0x109, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_632A)
    Sleep(0)

    def lambda_633A():
        TurnDirection(0x10A, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_633A)
    Sleep(0)

    def lambda_634A():
        TurnDirection(0x108, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_634A)
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
        "#10102F#30W#N#6Pあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0140
    ChrTalk(
        0x101,
        "#00002F#30W#N#6Pも、戻った……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0141
    ChrTalk(
        0xC,
        "#04306F#30W#5Pふう……何とかなったか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_63F4():
        OP_95(0xFE, 0, 200, 29300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_63F4)
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

    def lambda_643E():
        OP_96(0xFE, 0xFFFFFF38, 0xC8, 0x6A40, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_643E)
    Sleep(200)

    def lambda_645B():
        OP_96(0xFE, 0xC8, 0xC8, 0x6464, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_645B)
    Sleep(200)

    def lambda_6478():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_6478)

    def lambda_6485():
        OP_96(0xFE, 0x76C, 0xC8, 0x6720, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_6485)
    Sleep(200)

    def lambda_64A2():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_64A2)

    def lambda_64AF():
        OP_96(0xFE, 0xFFFFF894, 0xC8, 0x6590, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_64AF)
    WaitChrThread(0x101, 1)
    Sleep(800)

    #C0142
    ChrTalk(
        0x101,
        "#00013F#6Pど、どうですか？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xC,
        (
            "#04304Fうん、気絶しとるだけや。\x02\x03",

            "#04300F数日は起きられへんけど\x01",
            "命に別状はないやろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        "#00006F#6Pよ、良かった……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 1)
    WaitChrThread(0x10A, 1)
    WaitChrThread(0x108, 1)

    #C0145
    ChrTalk(
        0x109,
        "#6P#10112Fはぁ……ひと安心ですね。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x10A,
        (
            "#6P#00607Fそ、それはともかく\x01",
            "あんたは一体何者なんだ！？\x02\x03",

            "教会の神父のようだが……\x01",
            "一体どうしてこんな場所に！？\x02",
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
            "#11P#04305Fあれ、アリオスさん。\x02\x03",

            "オレのこと、こちらの皆さんには\x01",
            "話してへんのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x108,
        (
            "#01404Fフフ、間に合うかどうか\x01",
            "分からないと言われたからな。\x02\x03",

            "#01402F立場が立場だろうし、\x01",
            "念のため伏せさせてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xC,
        (
            "#11P#04304Fなるほど、助かりますわ。\x02\x03",

            "#04311Fいや～、相変わらず\x01",
            "気が利いてはるお人やなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x108,
        (
            "#01404Fフッ、君の方こそな。\x02\x03",

            "#01402Fありがとう。\x01",
            "来てくれて本当に助かった。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#00011F#6Pえっと……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x10A,
        (
            "#6P#00606Fフン、どうやら勝手に\x01",
            "保険を掛けられたようだな。\x02\x03",

            "#00600F七耀教会、封聖省に所属する\x01",
            "《星杯騎士》どのと見受けるが？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x109,
        "#3P#10105F封聖省、星杯騎士……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        (
            "#00005F#6P確か《古代遺物#8Rアーティファクト#》を\x01",
            "回収するっていう……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(150)

    #C0155
    ChrTalk(
        0xC,
        "#11P#04304Fハハ、お見通しでしたか。\x02",
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
            "初めまして──\x01",
            "七耀教会、星杯騎士団に所属する\x01",
            "ケビン・グラハムいいます。\x02\x03",

            "アリオスさんの連絡を受けて\x01",
            "参上させてもらいましたわ。\x02\x03",

            "どうかお見知りおきを──\x02",
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

    # Function_19_41F6 end

    def Function_20_6A4C(): pass

    label("Function_20_6A4C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A78")
    SetChrSubChip(0xC, 0x0)
    Sleep(100)
    SetChrSubChip(0xC, 0x1)
    Sleep(100)
    SetChrSubChip(0xC, 0x2)
    Sleep(100)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    Jump("Function_20_6A4C")

    label("loc_6A78")

    Return()

    # Function_20_6A4C end

    def Function_21_6A79(): pass

    label("Function_21_6A79")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A9D")
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_21_6A79")

    label("loc_6A9D")

    Return()

    # Function_21_6A79 end

    def Function_22_6A9E(): pass

    label("Function_22_6A9E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AC2")
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_22_6A9E")

    label("loc_6AC2")

    Return()

    # Function_22_6A9E end

    def Function_23_6AC3(): pass

    label("Function_23_6AC3")

    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_6AD6():
        OP_9D(0xFE, 0xFFFFFC18, 0xC8, 0x5014, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AD6)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Return()

    # Function_23_6AC3 end

    def Function_24_6AFB(): pass

    label("Function_24_6AFB")

    SetChrChipByIndex(0x109, 0x31)
    SetChrSubChip(0x109, 0x2)
    Sound(809, 0, 100, 0)

    def lambda_6B0E():
        OP_9D(0xFE, 0x5DC, 0xC8, 0x4A38, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6B0E)
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

    # Function_24_6AFB end

    def Function_25_6ED5(): pass

    label("Function_25_6ED5")

    SetChrFlags(0x10A, 0x20)

    def lambda_6EDF():
        OP_93(0xFE, 0x13B, 0x2BC)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_6EDF)
    SetChrChipByIndex(0x10A, 0x32)
    SetChrSubChip(0x10A, 0x0)

    def lambda_6EF4():
        OP_9D(0xFE, 0xDAC, 0xC8, 0x4F4C, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_6EF4)
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

    # Function_25_6ED5 end

    def Function_26_703E(): pass

    label("Function_26_703E")

    SetChrFlags(0x108, 0x20)

    def lambda_7048():
        OP_93(0xFE, 0x3C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_7048)
    SetChrChipByIndex(0x108, 0x25)
    SetChrSubChip(0x108, 0x3)

    def lambda_705D():
        OP_9D(0xFE, 0xFFFFF060, 0xC8, 0x526C, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_705D)
    WaitChrThread(0x108, 1)
    Sound(540, 0, 100, 0)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    Sleep(100)
    Sound(881, 0, 100, 0)
    PlayEffect(0x4, 0x1, 0x108, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_70CC():
        OP_A6(0xFE, 0x32, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_70CC)
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

    # Function_26_703E end

    def Function_27_718F(): pass

    label("Function_27_718F")


    def lambda_7194():
        OP_96(0xFE, 0x0, 0xC8, 0x5B68, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7194)
    Sleep(100)

    def lambda_71B1():
        OP_96(0xFE, 0x7D0, 0xC8, 0x5E88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_71B1)
    Sleep(100)

    def lambda_71CE():
        OP_96(0xFE, 0xFFFFF830, 0xC8, 0x5E88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_71CE)
    Return()

    # Function_27_718F end

    def Function_28_71E4(): pass

    label("Function_28_71E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_71FD")
    Sound(892, 0, 50, 0)
    Sleep(1150)
    Jump("Function_28_71E4")

    label("loc_71FD")

    Return()

    # Function_28_71E4 end

    def Function_29_71FE(): pass

    label("Function_29_71FE")

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

    # Function_29_71FE end

    def Function_30_726A(): pass

    label("Function_30_726A")

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

    # Function_30_726A end

    def Function_31_72AA(): pass

    label("Function_31_72AA")

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

    # Function_31_72AA end

    def Function_32_72EA(): pass

    label("Function_32_72EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7303")
    Sound(934, 0, 60, 0)
    Sleep(1500)
    Jump("Function_32_72EA")

    label("loc_7303")

    Return()

    # Function_32_72EA end

    def Function_33_7304(): pass

    label("Function_33_7304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_731D")
    Sound(1034, 0, 100, 0)
    Sleep(1000)
    Jump("Function_33_7304")

    label("loc_731D")

    Return()

    # Function_33_7304 end

    def Function_34_731E(): pass

    label("Function_34_731E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7337")
    Sound(1034, 0, 50, 0)
    Sleep(1000)
    Jump("Function_34_731E")

    label("loc_7337")

    Return()

    # Function_34_731E end

    def Function_35_7338(): pass

    label("Function_35_7338")

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

    # Function_35_7338 end

    def Function_36_73A6(): pass

    label("Function_36_73A6")

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

    # Function_36_73A6 end

    def Function_37_7414(): pass

    label("Function_37_7414")

    OP_71(0x1, 0x119, 0x136, 0x0, 0x0)
    OP_79(0x1)
    Sound(831, 0, 100, 0)
    Sound(830, 0, 50, 0)
    OP_71(0x1, 0x384, 0x38E, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x38F, 0x3B6, 0x0, 0x20)
    Return()

    # Function_37_7414 end

    SaveToFile()

Try(main)
