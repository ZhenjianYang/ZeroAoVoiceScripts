from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4290.bin",                # FileName
        "m4290",                    # MapName
        "m4290",                    # Location
        0x007F,                     # MapIndex
        "ed7573",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x29,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 127, 0, 0, 0, 1],
    )

    BuildStringList((
        "m4290",                  # 0
        "ノバルティス博士",       # 1
        "道化師カンパネルラ",     # 2
        "アリアンロード",         # 3
        "銀",                     # 4
        "リーシャ",               # 5
        "遊撃士スコット",         # 6
        "遊撃士ヴェンツェル",     # 7
        "アリオス",               # 8
        "騎士装束の娘",           # 9
        "騎士装束の娘",           # 10
        "騎士装束の娘",           # 11
        "スフィンキマイラ",       # 12
        "SE制御",                 # 13
        "APL表示用",              # 14
        "bm4210",                 # 15
    ))

    ATBonus("ATBonus_24C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_30C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_31C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_300", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_304", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_32C", 0x0042, 72, 6, 45, 3, 3, 30, 0, "bm4210", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_30C", "MonsterBattlePostion_2EC", "ed7454", "ed7453", "ATBonus_24C"),
            (),
            (),
            (),
        )
    )

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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1052, 0)                                       # 0

    ScpFunction((
        "Function_0_41C",          # 00, 0
        "Function_1_43D",          # 01, 1
        "Function_2_480",          # 02, 2
        "Function_3_254B",         # 03, 3
        "Function_4_2587",         # 04, 4
        "Function_5_25C3",         # 05, 5
        "Function_6_25FF",         # 06, 6
        "Function_7_263B",         # 07, 7
        "Function_8_2677",         # 08, 8
        "Function_9_26A9",         # 09, 9
        "Function_10_29B0",        # 0A, 10
        "Function_11_2A37",        # 0B, 11
        "Function_12_2B00",        # 0C, 12
        "Function_13_2B09",        # 0D, 13
        "Function_14_2B12",        # 0E, 14
        "Function_15_2B1B",        # 0F, 15
        "Function_16_2B24",        # 10, 16
        "Function_17_2B2D",        # 11, 17
        "Function_18_2B36",        # 12, 18
        "Function_19_6A7E",        # 13, 19
        "Function_20_6AA0",        # 14, 20
        "Function_21_6BEC",        # 15, 21
        "Function_22_6BFF",        # 16, 22
        "Function_23_6CF4",        # 17, 23
        "Function_24_6D5E",        # 18, 24
        "Function_25_6D7D",        # 19, 25
        "Function_26_6E8E",        # 1A, 26
        "Function_27_6EFA",        # 1B, 27
        "Function_28_6FA6",        # 1C, 28
        "Function_29_7046",        # 1D, 29
        "Function_30_70E6",        # 1E, 30
        "Function_31_718C",        # 1F, 31
        "Function_32_722C",        # 20, 32
        "Function_33_72C5",        # 21, 33
        "Function_34_73FD",        # 22, 34
        "Function_35_7520",        # 23, 35
        "Function_36_7533",        # 24, 36
        "Function_37_7568",        # 25, 37
        "Function_38_765A",        # 26, 38
        "Function_39_7675",        # 27, 39
        "Function_40_76B5",        # 28, 40
        "Function_41_76F3",        # 29, 41
        "Function_42_770C",        # 2A, 42
    ))


    def Function_0_41C(): pass

    label("Function_0_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42D")
    Event(0, 2)

    label("loc_42D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_43C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)

    label("loc_43C")

    Return()

    # Function_0_41C end

    def Function_1_43D(): pass

    label("Function_1_43D")

    SoundDistance(0x7A, 0xFFFFB06E, 0xBC2, 0xFFFFD008, 0x4E20, 0x186A0, 0x64, 0x0)
    OP_E3(0x24E, 0xFFFFFD12, 0x6004)
    OP_E3(0x7DBD, 0xFFFFFD12, 0x14DC)
    Sound(123, 1, 80, 0)
    SetMapObjFlags(0x0, 0x4)
    Return()

    # Function_1_43D end

    def Function_2_480(): pass

    label("Function_2_480")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13400.itc", 0x1E)
    LoadChrToIndex("chr/ch03600.itc", 0x1F)
    LoadChrToIndex("chr/ch03500.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00550.itc", 0x26)
    SoundLoad(3887)
    SoundLoad(3888)
    SoundLoad(3889)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E0")
    LoadChrToIndex("chr/ch02950.itc", 0x25)
    Jump("loc_4E6")

    label("loc_4E0")

    LoadChrToIndex("chr/ch03050.itc", 0x25)

    label("loc_4E6")

    LoadEffect(0x7, "event/ev10008.eff")
    LoadEffect(0x0, "event/ev10017.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04700.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    SetChrPos(0x101, -800, -750, -26000, 0)
    SetChrPos(0x102, 600, -750, -26000, 0)
    SetChrPos(0x103, -1100, -750, -27400, 0)
    SetChrPos(0x104, 900, -750, -27400, 0)
    SetChrPos(0x106, -800, -750, -28800, 0)
    SetChrPos(0xF4, 600, -750, -28800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, -2300, 250, 7600, 315)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrPos(0x9, -900, 250, 7400, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x20)
    SetChrPos(0xA, 600, 250, 7600, 45)
    SetChrFlags(0xA, 0x8000)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x0, 0x1000)
    OP_78(0x0, 0x13)
    OP_68(-290, 750, -25000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(17000, 0)
    FadeToBright(1000, 0)
    OP_68(-720, 2250, -20050, 3000)
    MoveCamera(52, 18, 0, 3000)
    OP_6E(750, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_6DF():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6DF)
    Sleep(100)

    def lambda_6F7():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6F7)
    Sleep(50)

    def lambda_70F():
        OP_9B(0x0, 0x103, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_70F)
    Sleep(50)

    def lambda_727():
        OP_9B(0x0, 0x104, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_727)
    Sleep(50)

    def lambda_73F():
        OP_9B(0x0, 0xF4, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_73F)
    Sleep(50)

    def lambda_757():
        OP_9B(0x0, 0x106, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_757)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x101, 2)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0001
    ChrTalk(
        0x101,
        "#00011F#6P（こ、ここは……！）\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x103,
        (
            "#00205F#12P#N（凄い……膨大なエネルギーが\x01",
            "  集まっているみたいです……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0003
    ChrTalk(
        0x104,
        (
            "#00311F#12P（それに……\x01",
            "  やっぱり居やがったみたいだぜ。）\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    SetCameraDistance(12000, 4000)
    OP_68(-800, 2250, 1500, 4000)
    MoveCamera(0, 14, 0, 4000)
    OP_6E(810, 4000)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    Fade(500)
    OP_68(-800, 12550, 2650, 0)
    MoveCamera(0, 14, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(5000, 0)
    OP_68(-800, 2750, 1500, 5000)
    OP_6F(0x79)
    Sleep(500)

    #C0004
    ChrTalk(
        0x9,
        (
            "#04809F#6Pウフフ……\x01",
            "これは物凄い場所だね。\x02\x03",

            "#04800Fここまで活性化しているのなら\x01",
            "そろそろ準備は出来ているのかな？\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "白衣の男",
        "#04704F#11Pフフ、そういう事なんだろう。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x86, 0x1F4)
    Sleep(200)

    #N0006
    NpcTalk(
        0x8,
        "白衣の男",
        (
            "#04702F#5Pうんうん、さぞかし面白い\x01",
            "見世物になってくれそうだ。\x02\x03",

            "《白面》殿が生きていれば\x01",
            "さぞ愉しんでくれただろうに。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(100)

    #C0007
    ChrTalk(
        0x9,
        (
            "#04809F#11Pアハハ、間違いないだろうね。\x02\x03",

            "#04805Fでも、博士に加えて\x01",
            "教授までクロスベルに来てたら\x01",
            "収拾が付かなくならないかな？\x02\x03",

            "#04802F《方舟#4Rグロリアス#》まで持ち出して\x01",
            "２大国に喧嘩を売ったりして。\x02",
        )
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x8,
        "白衣の男",
        (
            "#04709F#5Pハハ、それはそれで\x01",
            "なかなか面白そうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #N0009
    NpcTalk(
        0xA,
        "甲冑の人物",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P……………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BE7():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE7)

    def lambda_BFC():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BFC)

    def lambda_C11():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C11)

    def lambda_C26():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C26)

    def lambda_C3B():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_C3B)

    def lambda_C50():
        OP_9B(0x0, 0xFE, 0x166, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C50)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x9, 0x87, 0x1F4)

    #C0010
    ChrTalk(
        0x9,
        (
            "#04805F#5Pあれ、どうしたの？\x02\x03",

            "#04800Fやっぱりこの程度の使命、\x01",
            "簡単すぎて気乗りがしない？\x02",
        )
    )

    CloseMessageWindow()

    #N0011
    NpcTalk(
        0xA,
        "甲冑の人物",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P──全てはあの方の意志。\x01",
            "異存などあるはずもありません。\x02\x03",

            "それよりも博士、カンパネルラ。\x01",
            "お喋りはそのくらいで。\x02\x03",

            "どうやら客人のようです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-800, 2250, -4500, 2500)
    MoveCamera(0, 25, 0, 2500)
    SetCameraDistance(16000, 2500)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(50)

    def lambda_DD5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_DD5)
    Sleep(50)

    def lambda_DE5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_DE5)
    WaitChrThread(0x101, 1)

    def lambda_DF6():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF6)
    Sleep(50)

    def lambda_E0E():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E0E)
    Sleep(50)

    def lambda_E26():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E26)
    Sleep(50)

    def lambda_E3E():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E3E)
    Sleep(50)

    def lambda_E56():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_E56)
    Sleep(50)

    def lambda_E6E():
        OP_9B(0x0, 0xFE, 0x166, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_E6E)
    OP_6F(0x79)
    Fade(500)
    OP_68(-6700, 2150, -2690, 0)
    MoveCamera(47, 8, -1, 0)
    OP_6E(630, 0)
    SetCameraDistance(10290, 0)
    SetCameraDistance(9290, 2000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xF4, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)

    #C0012
    ChrTalk(
        0x101,
        "#00013F#12P………………………………\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        "#00107F#12P……あ、貴方たちは……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#12P#N……どうやら予想以上の\x01",
            "化物どもが揃っていたようだな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0015
    ChrTalk(
        0x9,
        (
            "#04805F#5Pああ、君たちか。\x02\x03",

            "#04804F遊撃士のお姉さんたちは\x01",
            "身動きを取れなくした筈だけど……\x02\x03",

            "#04802Fウフフ、どうやって\x01",
            "この場所を突き止めたんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#00203F……#12P#N一応、企業秘密という事で。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0017
    ChrTalk(
        0x104,
        (
            "#00301F#12P#Nしかし、何だか面白ぇことを\x01",
            "ペラペラ抜かしてたじゃねぇか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E9")

    #C0018
    ChrTalk(
        0x109,
        (
            "#10107F#12P#Nあなた達の企て……\x01",
            "見過ごすわけにはいきません！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_112D")

    label("loc_10E9")


    #C0019
    ChrTalk(
        0x105,
        (
            "#10302F#12P#Nさすがに見過ごすわけには\x01",
            "行かなくなってきたかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112D")

    OP_57(0x0)
    OP_5A()

    #N0020
    NpcTalk(
        0x8,
        "白衣の男",
        (
            "#04703F#5Pふむ……\x02\x03",

            "#04701F察するにクロスベル警察の\x01",
            "新人諸君といったところかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00003F……#12Pクロスベル警察、\x01",
            "《特務支援課》の者だ。\x02\x03",

            "#00008F結社《身喰らう蛇#10Rウ ロ ボ ロ ス#》の\x01",
            "関係者と見受けるが……\x02\x03",

            "#00001Fまずは身分を証明できるものを\x01",
            "提示してもらいましょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0022
    NpcTalk(
        0x8,
        "白衣の男",
        (
            "#04705F#5P身分の証明……？\x01",
            "彼は何を言ってるんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "#04806F#5Pうーん、警察としての手続きを\x01",
            "踏んでいるんじゃないの？\x02\x03",

            "#04802Fウフフ、ボクたち相手に身分証明って\x01",
            "悪い冗談にしか思えないけど。\x02",
        )
    )

    CloseMessageWindow()

    #N0024
    NpcTalk(
        0xA,
        "甲冑の人物",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P真っ直ぐな若者ですね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0025
    NpcTalk(
        0xA,
        "甲冑の人物",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P要求に応えられないのは\x01",
            "心苦しくはありますが……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        (
            "#00306F……#11P駄目だ、ロイド。\x02\x03",

            "#00301F常識が通用する連中じゃ\x01",
            "なさそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P#N《教団》の連中あたりと\x01",
            "同じだと考えるべきだろう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0028
    NpcTalk(
        0x8,
        "白衣の男",
        (
            "#04703F#5Pフム、彼らと一緒にされるのは\x01",
            "さすがに面白くないねぇ。\x02\x03",

            "#04702Fフフ……いいだろう。\x01",
            "自己紹介くらいはしようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x8, 0x0, 0x190, 0x320, 0x0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("白衣の男")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            "Ｆ・ノバルティスだ。\x02\x03",

            "《身喰らう蛇#10Rウ ロ ボ ロ ス#》の第六柱にして、\x01",
            "《十三工房》を任されている。\x02\x03",

            "フフ、どうか気軽に\x01",
            "“博士”とでも呼んでくれたまえ。\x02",
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

    #C0030
    ChrTalk(
        0x103,
        (
            "#00203F#12P#N……なるほど。\x01",
            "貴方の仕業だったんですね。\x02\x03",

            "#00201F導力ネットのハッキングに使われた\x01",
            "不可解なコードを開発したのは。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x8,
        (
            "#04705F#1Pほお……！？\x01",
            "あのコードが分かるのかね！？\x02\x03",

            "#04709Fあれは《星辰#4Rアストラル#のコード》と言ってね！\x01",
            "結社のネットワークで使われている──\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        "#04801F#5P博士、博士。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#04703F#5Pそういえば教団の被験者で\x01",
            "エプスタインの連中が拾った\x01",
            "娘というのがいたか……\x02\x03",

            "#04702F──どうだね君！？\x01",
            "その才能を《結社》のために\x01",
            "活かすつもりはないかね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        "#00211F#12P#Nお断りします。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x190)

    #C0035
    ChrTalk(
        0x8,
        "#04705F#5P#4Sガーン！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0036
    ChrTalk(
        0x9,
        (
            "#04806F#5Pまったく……\x01",
            "レンに逃げられたからといって\x01",
            "さすがに必死すぎないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#04701F#5Pべ、別にレンの話は\x01",
            "ここでは関係ないだろう？\x02",
        )
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0xA,
        "甲冑の人物",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P──さて、次は私ですか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xA, 0x0, 0x190, 0x320, 0x0)
    Fade(500)
    OP_68(-3520, 2450, 2610, 0)
    MoveCamera(53, 7, -1, 0)
    OP_6E(630, 0)
    SetCameraDistance(7100, 0)
    OP_0D()
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetChrName("甲冑の人物")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3887V#40W我が名はアリアンロード。\x02\x03",

            "#3888V《身喰らう蛇#10Rウ ロ ボ ロ ス#》の第七柱にして、\x01",
            "《鋼》の名を冠されています。\x02\x03",

            "#3889Vどうか見知りおきを。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF31)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0040
    ChrTalk(
        0x101,
        "#00011F#12P#Nっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0041
    ChrTalk(
        0x102,
        "#00108F#12P#Nなんて澄んだ声……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0042
    ChrTalk(
        0x104,
        (
            "#00301F#12P#Nゴツイ鎧を着ているが、\x01",
            "女みてぇだな……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE1")

    #C0043
    ChrTalk(
        0x109,
        (
            "#10108F#12P#Nし、信じられないほどの\x01",
            "威圧感ですけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C1F")

    label("loc_1BE1")


    #C0044
    ChrTalk(
        0x105,
        (
            "#10301F#12P#N……信じられないほどの\x01",
            "威圧感だけどねぇ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1F")

    OP_57(0x0)
    OP_5A()

    #C0045
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P#N……貴様が《結社》の\x01",
            "最強の使い手というわけか。\x02\x03",

            "確かに身震いするほどの\x01",
            "闘気の持ち主のようだが──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2330, 1950, -5470, 2000)
    MoveCamera(14, 13, -1, 2000)
    OP_6E(630, 2000)
    SetCameraDistance(9290, 2000)
    Sound(540, 0, 70, 0)
    SetChrChipByIndex(0x106, 0x26)
    SetChrSubChip(0x106, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0xF4, 3, 0, 7)
    BeginChrThread(0x103, 3, 0, 5)
    BeginChrThread(0x104, 3, 0, 6)
    BeginChrThread(0x101, 3, 0, 3)
    BeginChrThread(0x102, 3, 0, 4)
    WaitChrThread(0xF4, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x106, 3)
    Sleep(150)

    #C0046
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#6P──この《銀#2Rイン#》を前にして\x01",
            "その余裕、どれだけ保てるかな？\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#11P#N…………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0048
    ChrTalk(
        0x101,
        "#00011F#5Pお、おい《銀》……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#00108F#11Pどうしてそんな……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "#04804F#5P#Nウフフ、なかなか興味深い\x01",
            "対戦カードだとは思うけど……\x02\x03",

            "#04800Fその前に、ここのヌシが\x01",
            "戻ってきたみたいだねぇ。\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    def lambda_1EF0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EF0)
    Sleep(50)

    def lambda_1F00():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F00)
    Sleep(50)

    def lambda_1F10():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F10)
    Sleep(50)

    def lambda_1F20():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F20)
    Sleep(50)

    def lambda_1F30():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1F30)
    Sleep(100)

    #C0051
    ChrTalk(
        0x101,
        "#00005F#6Pなに……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F87")

    #C0052
    ChrTalk(
        0x109,
        "#10105F#12P“ヌシ”……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FA6")

    label("loc_1F87")


    #C0053
    ChrTalk(
        0x105,
        "#10305F#12P“ヌシ”……？\x02",
    )

    CloseMessageWindow()

    label("loc_1FA6")

    Sleep(100)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xFA0)

    #C0054
    ChrTalk(
        0x103,
        (
            "#00208F#6P巨大なオーラの接近を確認……\x02\x03",

            "#00207F大型の幻獣が来ます！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetCameraDistance(11290, 5000)

    def lambda_20A1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20A1)
    Sleep(50)

    def lambda_20B1():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20B1)
    Sleep(50)

    def lambda_20C1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20C1)
    Sleep(50)

    def lambda_20D1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20D1)
    Sleep(50)

    def lambda_20E1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_20E1)
    Sleep(50)

    def lambda_20F1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_20F1)
    Sleep(150)

    #C0055
    ChrTalk(
        0x104,
        "#00307F#5Pなんだと……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2155")

    #C0056
    ChrTalk(
        0x109,
        "#10101F#5Pど、どこから……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2179")

    label("loc_2155")


    #C0057
    ChrTalk(
        0x105,
        "#10308F#5P一体どこから……！？\x02",
    )

    CloseMessageWindow()

    label("loc_2179")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 35000, 7000, -1870, 270)
    OP_93(0x13, 0x10E, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x5A)
    SetChrFlags(0x13, 0x1)
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x0, 0x4)
    OP_70(0x0, 0xE5)
    OP_68(8260, 2850, -1360, 0)
    MoveCamera(72, 16, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(11450, 0)
    Fade(500)
    BeginChrThread(0x13, 0, 0, 9)
    WaitChrThread(0x13, 0)

    def lambda_2210():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2210)
    Sleep(50)

    def lambda_2220():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2220)
    Sleep(50)

    def lambda_2230():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2230)
    Sleep(50)

    def lambda_2240():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2240)
    Sleep(50)

    def lambda_2250():
        OP_93(0x106, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2250)
    Sleep(50)

    def lambda_2260():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2260)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0xF4, 0)
    OP_6F(0x79)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x106, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0xF4, 2)
    BeginChrThread(0x103, 3, 0, 14)
    Sleep(50)
    BeginChrThread(0x106, 3, 0, 17)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 12)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(50)
    BeginChrThread(0xF4, 3, 0, 16)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 13)
    Sleep(50)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    Sleep(500)
    SetChrPos(0x101, -1040, -750, -890, 90)
    SetChrPos(0x102, -2590, -750, 20, 90)

    #C0058
    ChrTalk(
        0x101,
        "#00007F#6P#Nなっ……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0059
    ChrTalk(
        0x102,
        "#00110F#6P#Nこ、この魔獣は……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0060
    ChrTalk(
        0x9,
        (
            "#04804F#6P#N幻獣《スフィンキマイラ》……\x02\x03",

            "#04802F古の幻想が作り出した\x01",
            "聖なる花園の番人といった所かな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0061
    ChrTalk(
        0x8,
        (
            "#04704F#6P#Nいやはや、こんなものまで\x01",
            "実体化しているとは……\x02\x03",

            "#04702Fフフ、これは計画の精度にも\x01",
            "期待が持てるというものだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    BeginChrThread(0x13, 0, 0, 10)
    WaitChrThread(0x13, 0)
    OP_68(-830, 2050, -5110, 2000)
    MoveCamera(52, 7, -1, 2000)
    OP_6E(530, 2000)
    SetCameraDistance(14680, 2000)
    OP_6F(0x79)
    Sleep(500)

    #C0062
    ChrTalk(
        0x101,
        "#00010F#6P#Nくっ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0063
    ChrTalk(
        0x104,
        (
            "#00310F#6P#Nチッ……！\x01",
            "狙うなら連中を狙いやがれ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0064
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00707F#6P#N──話は後だ！\x01",
            "速やかに調伏#4Rちょうぶく#する！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x13, 0, 0, 11)
    WaitChrThread(0x13, 0)
    Battle("BattleInfo_32C", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 18)
    Return()

    # Function_2_480 end

    def Function_3_254B(): pass

    label("Function_3_254B")


    def lambda_2550():
        OP_9B(0x1, 0xFE, 0x66, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2550)

    def lambda_2565():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2565)
    WaitChrThread(0xFE, 2)

    def lambda_2576():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2576)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_3_254B end

    def Function_4_2587(): pass

    label("Function_4_2587")


    def lambda_258C():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFD12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_258C)

    def lambda_25A1():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25A1)
    WaitChrThread(0xFE, 2)

    def lambda_25B2():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25B2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_4_2587 end

    def Function_5_25C3(): pass

    label("Function_5_25C3")


    def lambda_25C8():
        OP_9B(0x1, 0xFE, 0x66, 0xFFFFFEA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25C8)

    def lambda_25DD():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25DD)
    WaitChrThread(0xFE, 2)

    def lambda_25EE():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25EE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_5_25C3 end

    def Function_6_25FF(): pass

    label("Function_6_25FF")


    def lambda_2604():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFEA2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2604)

    def lambda_2619():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2619)
    WaitChrThread(0xFE, 2)

    def lambda_262A():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_262A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_6_25FF end

    def Function_7_263B(): pass

    label("Function_7_263B")


    def lambda_2640():
        OP_9B(0x1, 0xFE, 0x126, 0xFFFFFF6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2640)

    def lambda_2655():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2655)
    WaitChrThread(0xFE, 2)

    def lambda_2666():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2666)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0x13, 2)
    Return()

    # Function_7_263B end

    def Function_8_2677(): pass

    label("Function_8_2677")

    OP_68(-4000, 1950, -6700, 800)
    MoveCamera(21, 12, -1, 800)
    OP_6F(0x79)
    OP_68(-4650, 1950, -8700, 800)
    OP_6F(0x79)
    Return()

    # Function_8_2677 end

    def Function_9_26A9(): pass

    label("Function_9_26A9")

    OP_68(17070, 10650, -6540, 0)
    MoveCamera(48, 5, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(7630, 0)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(1300)
    OP_68(17070, 10650, -6540, 1650)
    MoveCamera(312, 24, 0, 1650)
    OP_6E(810, 1650)
    SetCameraDistance(7630, 1650)
    Sound(914, 0, 100, 0)
    Sound(251, 0, 100, 0)
    Sound(834, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xE5, 0xEF, 0x0, 0x0)
    CloseMessageWindow()
    OP_96(0xFE, 0x3A98, 0x1B58, 0xFFFFF8B2, 0x4268, 0x0)
    OP_74(0x0, 0x1E)
    OP_68(9820, 9950, -1820, 0)
    MoveCamera(82, 49, 0, 0)
    OP_6E(810, 0)
    SetCameraDistance(12750, 0)
    Fade(500)
    PlayEffect(0x0, 0x0, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(990, 0, 100, 0)
    OP_68(9820, 1350, -1820, 1500)
    MoveCamera(67, 7, 0, 1500)
    OP_6E(810, 1500)
    SetCameraDistance(10570, 1500)

    def lambda_27F9():
        OP_9D(0xFE, 0x29F4, 0xFFFFFE0C, 0xFFFFF8B2, 0x96, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27F9)
    Sleep(1100)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    WaitChrThread(0xFE, 2)
    OP_0D()
    Sound(833, 0, 100, 0)
    StopEffect(0x0, 0x2)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    OP_82(0x96, 0x12C, 0x1388, 0x320)
    OP_71(0x0, 0xF0, 0xF8, 0x0, 0x0)
    Sleep(300)
    CancelBlur(900)
    OP_79(0x0)
    Sleep(900)
    OP_68(9820, 2750, -1820, 600)
    MoveCamera(67, -3, 0, 600)
    OP_6E(810, 600)
    SetCameraDistance(10570, 600)
    OP_74(0x0, 0xF)
    Sound(251, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    OP_71(0x0, 0xF9, 0x104, 0x0, 0x0)

    def lambda_2921():
        OP_9C(0xFE, 0x32, 0x0, 0x0, 0x546, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2921)
    WaitChrThread(0xFE, 2)
    Sound(893, 0, 50, 0)
    OP_68(8900, 2000, -1790, 700)
    MoveCamera(61, -2, 0, 700)
    OP_6E(810, 700)
    SetCameraDistance(10360, 700)
    OP_79(0x0)
    OP_71(0x0, 0x105, 0x118, 0x0, 0x0)
    Sleep(200)
    Sound(833, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0x1F4)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    OP_6F(0x79)
    Return()

    # Function_9_26A9 end

    def Function_10_29B0(): pass

    label("Function_10_29B0")

    Fade(100)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x40, 0x4C, 0x0, 0x0)
    OP_79(0x0)
    OP_0D()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(11950, 500)
    Sound(913, 0, 100, 0)
    OP_71(0x0, 0x4D, 0x55, 0x0, 0x20)
    Sleep(300)
    OP_82(0xC8, 0xC8, 0xBB8, 0x5DC)
    Sleep(1800)
    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    OP_6F(0x79)
    CancelBlur(0)
    OP_71(0x0, 0x56, 0x63, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    Return()

    # Function_10_29B0 end

    def Function_11_2A37(): pass

    label("Function_11_2A37")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0xD4, 0xE4, 0x0, 0x0)
    Sleep(300)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(400)
    CancelBlur(300)
    OP_79(0x0)
    SetChrFlags(0xFE, 0x4)
    OP_71(0x0, 0xE5, 0xED, 0x0, 0x20)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_82(0x32, 0x64, 0xBB8, 0x1F4)
    Sound(251, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_68(-2700, 2550, -4100, 700)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_9C(0xFE, 0xFFFFE890, 0x1F4, 0x0, 0x226, 0x640)
    CancelBlur(0)
    Return()

    # Function_11_2A37 end

    def Function_12_2B00(): pass

    label("Function_12_2B00")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_2B00 end

    def Function_13_2B09(): pass

    label("Function_13_2B09")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_2B09 end

    def Function_14_2B12(): pass

    label("Function_14_2B12")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_2B12 end

    def Function_15_2B1B(): pass

    label("Function_15_2B1B")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_2B1B end

    def Function_16_2B24(): pass

    label("Function_16_2B24")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_2B24 end

    def Function_17_2B2D(): pass

    label("Function_17_2B2D")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_2B2D end

    def Function_18_2B36(): pass

    label("Function_18_2B36")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13400.itc", 0x1E)
    LoadChrToIndex("chr/ch03600.itc", 0x1F)
    LoadChrToIndex("chr/ch03500.itc", 0x20)
    LoadChrToIndex("chr/ch00500.itc", 0x21)
    LoadChrToIndex("chr/ch13700.itc", 0x22)
    LoadChrToIndex("chr/ch27200.itc", 0x23)
    LoadChrToIndex("chr/ch27300.itc", 0x24)
    LoadChrToIndex("chr/ch02400.itc", 0x25)
    LoadChrToIndex("chr/ch43150.itc", 0x26)
    LoadChrToIndex("chr/ch43250.itc", 0x27)
    LoadChrToIndex("chr/ch43350.itc", 0x28)
    LoadChrToIndex("apl/ch50011.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00150.itc", 0x2B)
    LoadChrToIndex("chr/ch00250.itc", 0x2C)
    LoadChrToIndex("chr/ch00350.itc", 0x2D)
    LoadChrToIndex("chr/ch00550.itc", 0x2E)
    LoadChrToIndex("chr/ch03550.itc", 0x30)
    LoadChrToIndex("chr/ch03552.itc", 0x31)
    LoadChrToIndex("apl/ch51408.itc", 0x32)
    LoadChrToIndex("chr/ch00053.itc", 0x33)
    LoadChrToIndex("chr/ch00153.itc", 0x34)
    LoadChrToIndex("chr/ch00253.itc", 0x35)
    LoadChrToIndex("chr/ch00353.itc", 0x36)
    LoadChrToIndex("chr/ch00056.itc", 0x39)
    LoadChrToIndex("chr/ch00156.itc", 0x3A)
    LoadChrToIndex("chr/ch00256.itc", 0x3B)
    LoadChrToIndex("chr/ch00356.itc", 0x3C)
    LoadChrToIndex("chr/ch00556.itc", 0x3D)
    LoadChrToIndex("chr/ch43100.itc", 0x3F)
    LoadChrToIndex("chr/ch43200.itc", 0x40)
    LoadChrToIndex("chr/ch43300.itc", 0x41)
    LoadChrToIndex("apl/ch51415.itc", 0x42)
    LoadChrToIndex("apl/ch51416.itc", 0x37)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00701.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    LoadEffect(0x1, "battle/bs000001.eff")
    LoadEffect(0x2, "eff/cutin35.eff")
    LoadEffect(0x3, "event/eva01_01.eff")
    LoadEffect(0x4, "event/ev14016.eff")
    LoadEffect(0x5, "event/ev10007.eff")
    LoadEffect(0x6, "event/ev10002.eff")
    LoadEffect(0x7, "battle/ms00001.eff")
    LoadEffect(0x8, "event/ev10006.eff")
    LoadEffect(0x9, "event/ev14015.eff")
    SoundLoad(3890)
    SoundLoad(3891)
    SoundLoad(3892)
    SoundLoad(4053)
    SoundLoad(4054)
    SoundLoad(4068)
    SoundLoad(3459)
    SoundLoad(3460)
    SoundLoad(2915)
    SoundLoad(3519)
    SoundLoad(3248)
    SoundLoad(3249)
    SoundLoad(4135)
    SoundLoad(959)
    SoundLoad(803)
    SoundLoad(825)
    RemoveParty(0x5, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DD2")
    LoadChrToIndex("chr/ch02950.itc", 0x2F)
    LoadChrToIndex("chr/ch02953.itc", 0x38)
    LoadChrToIndex("chr/ch0295F.itc", 0x3E)
    SetScenarioFlags(0x0, 0)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_2DEB")

    label("loc_2DD2")

    LoadChrToIndex("chr/ch03050.itc", 0x2F)
    LoadChrToIndex("chr/ch03053.itc", 0x38)
    LoadChrToIndex("chr/ch0305F.itc", 0x3E)
    ClearScenarioFlags(0x0, 0)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_2DEB")

    OP_68(-1820, 1450, 3350, 0)
    MoveCamera(153, 15, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(17390, 0)
    SetChrPos(0x101, -2190, -750, -670, 270)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x102, -210, -750, -3260, 270)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x103, -1200, -750, -2190, 270)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x104, -2960, -750, -2640, 270)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0xF4, 960, -750, -1430, 270)
    SetChrChipByIndex(0xF4, 0x2F)
    SetChrSubChip(0xF4, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x5, 10000, 12000, -7000, 0)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x2E)
    SetChrPos(0xB, 200, -750, 0, 270)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 200, -750, -3000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, -2300, 250, 7600, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrPos(0x9, -900, 250, 7400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x20)
    SetChrPos(0xA, 600, 250, 7600, 180)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x25)
    SetChrPos(0xF, 900, -750, -23000, 0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x23)
    SetChrPos(0xD, -900, -750, -25000, 0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x24)
    SetChrPos(0xE, 900, -750, -25000, 0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x26)
    SetChrPos(0x10, 0, -750, -13600, 0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x27)
    SetChrPos(0x11, 3850, -750, -7000, 250)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x28)
    SetChrPos(0x12, -4180, -750, -8370, 117)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0x13)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -9950, -750, 880, 0)
    OP_93(0x13, 0x64, 0x0)
    OP_74(0x0, 0x1E)
    SetChrFlags(0x13, 0x1)
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 0x32)
    SetChrSubChip(0x15, 0x8)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 600, 750, 5200, 180)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x15, 0x1000)
    SetChrFlags(0x15, 0x4)
    ClearChrFlags(0x15, 0x1)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetScenarioFlags(0x0, 1)
    OP_68(-5390, 2150, 1420, 0)
    MoveCamera(246, 16, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(14170, 0)
    SetCameraDistance(19170, 3000)
    FadeToBright(1000, 0)
    OP_82(0x0, 0x32, 0x5DC, 0x1388)
    BeginChrThread(0x13, 3, 0, 19)
    OP_0D()
    Sleep(500)
    Sound(843, 0, 100, 0)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    PlayEffect(0x1, 0x0, 0x13, 0x1, 500, -750, 500, 0, 0, 0, 1350, 1350, 1350, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_6F(0x79)
    OP_75(0x0, 0x1, 0x5DC)

    def lambda_315E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_315E)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    CancelBlur(2000)
    OP_6F(0x79)
    Sleep(500)
    OP_68(1240, 2150, 1060, 2000)
    MoveCamera(246, 16, -1, 2000)
    OP_6E(530, 2000)
    SetCameraDistance(15170, 2000)
    OP_6F(0x79)
    Sleep(300)

    #C0065
    ChrTalk(
        0x101,
        "#00006F#6Pくっ……はあはあ……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        "#00108F#6Pな、何とか倒せた……\x02",
    )

    CloseMessageWindow()
    Sound(971, 0, 100, 0)
    Sleep(1000)
    #Sound(4124, 255, 100, 0)    #voice#Companella
    Sleep(500)

    #C0067
    ChrTalk(
        0x9,
        "#04809F#5Pウフフ、結構やるじゃない㈱\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(1140, 2150, 4290, 2000)
    MoveCamera(313, 15, -1, 2000)
    OP_6E(630, 2000)
    SetCameraDistance(9710, 2000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_326F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_326F)
    Sleep(50)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_3287():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3287)
    Sleep(50)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    def lambda_329F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_329F)
    Sleep(50)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    def lambda_32B7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_32B7)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)

    def lambda_32CF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_32CF)
    Sleep(50)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)

    def lambda_32E7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_32E7)
    Sleep(50)
    OP_6F(0x79)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0xB, 2)

    #C0068
    ChrTalk(
        0x8,
        (
            "#04704F#5Pフム、素人にしては\x01",
            "なかなかといったところかな。\x02\x03",

            "#04700Fその魔導杖とやらも\x01",
            "財団の連中が作ったにしては\x01",
            "そこそこ完成度も高そうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        "#00201F#6P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0070
    ChrTalk(
        0x104,
        "#00311F#6P#Nてめぇら……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-6700, 2150, -2690, 0)
    MoveCamera(47, 8, -1, 0)
    OP_6E(630, 0)
    SetCameraDistance(9290, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    OP_9B(0x1, 0x101, 0x0, 0x190, 0x3E8, 0x0)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    #C0071
    ChrTalk(
        0x101,
        (
            "#00003F#12P《身喰らう蛇》──\x01",
            "そろそろ答えてもらおう！\x02\x03",

            "#00013Fクロスベルの地で\x01",
            "何をしようとしている！？\x02\x03",

            "#00007Fまさかとは思うが……\x01",
            "《グノーシス》を新たに製造したのも\x01",
            "アンタたちじゃないだろうな！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0072
    ChrTalk(
        0x102,
        "#00105F#11Pえっ！？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        "#00208F#11Pあ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3604")

    #C0074
    ChrTalk(
        0x109,
        "#10110F#11Pま、まさか……\x02",
    )

    CloseMessageWindow()

    label("loc_3604")


    #C0075
    ChrTalk(
        0x9,
        (
            "#04809F#5Pはは、魔人化しちゃった\x01",
            "不良のリーダー君か。\x02\x03",

            "ボクも見物させてもらったけど\x01",
            "なかなかの弾けっぷりだったよね。\x02\x03",

            "#04802Fウフフ、もう少し突き抜けたら\x01",
            "《結社》に迎えてもいいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F7")

    #C0076
    ChrTalk(
        0x105,
        "#10301F#11P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_36F7")


    #C0077
    ChrTalk(
        0x101,
        (
            "#00007F#12Pはぐらかすな！\x01",
            "質問に答えてもらおう！\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "#04709F#1Pハハ、君たちがそう思うのは\x01",
            "無理もないとは思うが……\x02\x03",

            "#04702F私たちはあくまで『計画』の\x01",
            "進行度を確かめに来ただけさ。\x02\x03",

            "七耀脈の活性化の度合いと……\x01",
            "『約束の日』のタイミングをね。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        "#00205F#12P#N『約束の日』……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0080
    ChrTalk(
        0x104,
        (
            "#00301F#12P#Nチッ、どこまで\x01",
            "思わせぶりなんだっつーの。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0081
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P……………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetCameraDistance(8000, 1500)

    def lambda_3894():
        OP_9B(0x1, 0xFE, 0x0, 0x190, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3894)
    WaitChrThread(0xB, 1)
    Sleep(300)
    Sound(540, 0, 70, 0)
    SetChrChipByIndex(0xB, 0x2E)
    SetChrSubChip(0xB, 0x0)
    OP_6F(0x79)
    Sleep(300)

    #C0082
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#12P──もはや言葉は尽くした。\x02\x03",

            "ここから先は力をもって\x01",
            "口を開いてもらうことにしよう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0083
    ChrTalk(
        0x101,
        "#00008F#6P銀#2Rイン#……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_398F")

    #C0084
    ChrTalk(
        0x109,
        (
            "#10107F#12P……そうするしか\x01",
            "方法はないみたいですね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C5")

    label("loc_398F")


    #C0085
    ChrTalk(
        0x105,
        (
            "#10303F#12P……そうするしか\x01",
            "道はないみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39C5")

    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xF4, 0x2F)
    SetChrSubChip(0xF4, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7584", 0)
    Fade(500)
    OP_68(-970, 1050, 4590, 0)
    MoveCamera(150, 17, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(18630, 0)
    SetCameraDistance(18130, 1000)
    OP_0D()
    Sleep(300)

    #C0086
    ChrTalk(
        0x8,
        "#04704F#6Pやれやれ。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "#04804F#6Pフフ、さすがにボクじゃ\x01",
            "君たち全員の相手は無理か。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    #C0088
    ChrTalk(
        0x9,
        (
            "#04802F#12Pここは貴女に\x01",
            "お任せしちゃっていいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P仕方ありませんね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B0D():
        OP_9B(0x1, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3B0D)
    Sleep(50)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_9B(0x1, 0x9, 0x0, 0xFFFFFCE0, 0x3E8, 0x0)
    Sleep(300)
    Fade(500)
    OP_68(130, 1950, 4130, 0)
    MoveCamera(11, 10, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 1000)
    OP_6F(0x79)
    BeginChrThread(0xA, 0, 0, 22)
    Sleep(300)
    SetCameraDistance(13000, 500)
    BlurSwitch(0xA, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(400)
    CancelBlur(0)
    WaitChrThread(0xA, 0)
    OP_6F(0x79)
    OP_68(-740, 2050, -670, 1200)
    SetCameraDistance(16550, 1200)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0090
    ChrTalk(
        0x101,
        "#00011F#6P#Nや、槍……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0091
    ChrTalk(
        0x102,
        (
            "#00105F#12P#N中世の騎士が使っていた\x01",
            "騎兵槍#6Rラ ン ス#みたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0092
    ChrTalk(
        0x104,
        (
            "#00306F#6P#Nおいおい……\x01",
            "そんな骨董品を持ち出して\x01",
            "どうしようってんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0093
    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3890V#5P#30W──問答は無用。\x02\x03",

            "#3891V互いに得物を取ったからには\x01",
            "全力をもって当たるがいい。\x02\x03",

            "#3892Vさもなくば命はないぞ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF34)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0094
    ChrTalk(
        0x101,
        "#00005F#6P#Nっ……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0095
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00707F#12P#N来る──！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(800)
    BeginChrThread(0xA, 3, 0, 24)
    Sleep(700)
    EndChrThread(0xA, 0x3)
    BeginChrThread(0xA, 3, 0, 25)
    BeginChrThread(0x14, 1, 0, 39)
    Fade(500)
    OP_68(-4770, 1950, -2610, 0)
    OP_68(-5000, 1850, -2610, 3000)
    MoveCamera(51, 8, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(9500, 0)
    SetCameraDistance(11000, 3000)
    Fade(500)
    CancelBlur(0)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x32, 0x5DC, 0x7D0)
    SetCameraDistance(12000, 3000)
    BeginChrThread(0xB, 3, 0, 32)
    BeginChrThread(0xB, 2, 0, 33)
    Sound(815, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 27)
    BeginChrThread(0x101, 2, 0, 34)
    BeginChrThread(0x102, 3, 0, 28)
    BeginChrThread(0x103, 3, 0, 29)
    BeginChrThread(0x104, 3, 0, 30)
    BeginChrThread(0xF4, 3, 0, 31)

    #C0096
    ChrTalk(
        0x102,
        "#00105F#11P#7Aえ──\x02",
    )
    #Auto

    Sleep(800)

    #C0097
    ChrTalk(
        0x101,
        "#00010F#4P#N#7A……な………\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0xA, 3)
    Sleep(300)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-3210, 1650, -4260, 1000)
    MoveCamera(36, 5, -1, 1000)
    OP_6E(530, 1000)
    SetCameraDistance(17220, 1000)
    OP_82(0x1F4, 0x0, 0xBB8, 0x3E8)
    Sound(369, 0, 100, 0)
    Sound(196, 0, 80, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(2031, 255, 100, 0)    #voice#Lloyd
    Sound(2129, 255, 70, 1)    #voice#Elie
    Sound(2223, 255, 100, 2)    #voice#Tio
    Sound(2318, 255, 100, 3)    #voice#Randy
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4043")
    Sound(2464, 255, 100, 4)    #voice#Noel
    Jump("loc_4049")

    label("loc_4043")

    Sound(2404, 255, 100, 4)    #voice#Lazy

    label("loc_4049")

    WaitChrThread(0xB, 2)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0xF4, 3)
    CancelBlur(0)
    Sleep(500)
    BeginChrThread(0xA, 3, 0, 26)
    WaitChrThread(0xA, 3)

    #C0098
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_412B")

    #C0099
    ChrTalk(
        0x109,
        "#10108F#12P#30W#Nそ、そんな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0100
    ChrTalk(
        0x104,
        (
            "#00310F#12P#30W#Nちょ、超高速の突きを\x01",
            "一瞬で何十も放ったのか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_41A4")

    label("loc_412B")


    #C0101
    ChrTalk(
        0x104,
        "#00310F#12P#30W#Nグッ……まさか今のは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0102
    ChrTalk(
        0x105,
        (
            "#10310F#12P#30W#N……超高速の突きを\x01",
            "一呼吸で数十放ったのか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_41A4")


    #C0103
    ChrTalk(
        0x103,
        (
            "#00206F#12P#30W#N……ありえません……\x01",
            "人間の出来ることでは……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0104
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00710F#11P#30W…………くっ……………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#04702F#5Pほう、《鋼#2Rはがね#の聖女》の槍を\x01",
            "凌げる人間がいるとはねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "#04809F#5Pウフフ、東方人街の魔人なんて\x01",
            "呼ばれるだけはあるみたいだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5Pなかなかの反応です。\x02\x03",

            "ですが“先代”と比べると\x01",
            "いまだ迷いがあるようですね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    #Sound(2617, 255, 100, 0)    #voice#Yin

    #C0108
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00705F#11P#30W#10A………なに…………\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(972, 0, 100, 0)
    Sleep(800)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-90, 550, -3200, 0)
    MoveCamera(168, 27, -1, 0)
    MoveCamera(168, 23, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 1000)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 0x39)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    ClearChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 0x3A)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0x3C)
    SetChrSubChip(0x104, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    ClearChrFlags(0x103, 0x20)
    SetChrChipByIndex(0x103, 0x3B)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0xF4, 0x20)
    SetChrChipByIndex(0xF4, 0x3E)
    SetChrSubChip(0xF4, 0x0)
    Sleep(300)
    OP_6F(0x79)
    OP_FD(0xC, 0xB)
    BeginChrThread(0xB, 0, 0, 40)
    WaitChrThread(0xB, 0)
    SetChrChipByIndex(0xC, 0x42)
    SetChrSubChip(0xC, 0x1)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_0D()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0109
    AnonymousTalk(
        0xC,
        "#30W────────────\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0110
    ChrTalk(
        0x101,
        "#00011F#12P……！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        "#00105F#5Pえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        "#00307F#11Pなあっ……！？\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#00205F#11Pリーシャ……さん……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4602")

    #C0114
    ChrTalk(
        0x109,
        "#10111F#5Pえ、ええっ……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_4602")


    #C0115
    ChrTalk(
        0x105,
        (
            "#10301F#5P凄いな……\x01",
            "気配を変えてたのか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4633")

    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0116
    ChrTalk(
        0x9,
        (
            "#04809F#5Pアハハ、こりゃ傑作だ！\x02\x03",

            "《銀#2Rイン#》の正体が\x01",
            "アルカンシェルの準ヒロイン、\x01",
            "リーシャ・マオだったなんてね！\x02\x03",

            "#04802Fウフフ、さぞ面白い\x01",
            "ドラマがありそうじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xC,
        "#00711F#5P…………くっ……………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x5, -900, -750, -23000, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_47B4")

    #N0118
    NpcTalk(
        0x105,
        "少年の声",
        (
            "#2915V#6P#29A──いやはや。\x01",
            "凄い場面に来たみたいだね。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Jump("loc_47EC")

    label("loc_47B4")


    #N0119
    NpcTalk(
        0x109,
        "娘の声",
        "#3519V#6P#20A皆さん、大丈夫ですか！？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    label("loc_47EC")

    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0xC, 0x2)
    SetChrSubChip(0xC, 0x5)
    OP_68(-2330, 1950, -1820, 1500)
    MoveCamera(158, 16, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(14070, 1500)
    Sleep(500)

    def lambda_48C4():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_48C4)
    Sleep(100)

    def lambda_48DC():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_48DC)
    Sleep(50)

    def lambda_48F4():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_48F4)
    Sleep(50)

    def lambda_490C():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_490C)

    def lambda_4921():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4921)
    Sleep(50)

    def lambda_4931():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4931)
    Sleep(50)

    def lambda_4941():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_4941)
    Sleep(50)

    def lambda_4951():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4951)
    Sleep(50)

    def lambda_4961():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4961)
    Sleep(150)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0x5, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_49DB")

    #C0120
    ChrTalk(
        0x101,
        (
            "#00008F#6P#Nワジ……\x01",
            "それにアリオスさんたちも……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A14")

    label("loc_49DB")


    #C0121
    ChrTalk(
        0x101,
        (
            "#00008F#6P#Nノエル……\x01",
            "それにアリオスさんたちも……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A14")

    OP_57(0x0)
    OP_5A()

    #C0122
    ChrTalk(
        0x102,
        "#00106F#6P来てくれたんですね……\x02",
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_4A45():
        OP_9B(0x0, 0xFE, 0x163, 0x1A90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_4A45)
    Sleep(100)

    def lambda_4A5D():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4A5D)
    Sleep(150)

    def lambda_4A75():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4A75)
    Sleep(50)

    def lambda_4A8D():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4A8D)
    Sleep(400)
    Fade(500)
    SetChrChipByIndex(0xC, 0x42)
    SetChrFlags(0xC, 0x1000)
    ClearChrFlags(0xC, 0x2)
    SetChrSubChip(0xC, 0x1)
    OP_68(-3310, 1950, -11270, 0)
    MoveCamera(24, 9, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(13150, 0)
    WaitChrThread(0x5, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0123
    ChrTalk(
        0xE,
        "#12Pあの者たちは……！\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xD,
        "#12P《蛇》の連中か……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0125
    AnonymousTalk(
        0xF,
        (
            "#4053V#11P#40W《道化師》カンパネルラ……\x02\x03",

            "#4054Vそれに《十三工房》の管理者に\x01",
            "《鋼の聖女》か……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFD6)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    #C0126
    ChrTalk(
        0x8,
        (
            "#04705F#5P#Nほほう……\x01",
            "あれが《風の剣聖》かな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0127
    ChrTalk(
        0x9,
        (
            "#04802F#5P#Nウフフ、レーヴェに匹敵する\x01",
            "腕前らしいけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0128
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#N──《風の剣聖》。\x01",
            "見#2Rまみ#えるのは初めてですか。\x02\x03",

            "なるほど、噂に違わず\x01",
            "素晴らしい腕前のようですね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0129
    ChrTalk(
        0xF,
        (
            "#01403F#11P……世辞は結構。\x02\x03",

            "貴女のように“人の域”を\x01",
            "超えるまでは到底至っていない。\x02\x03",

            "#01401F特に“その槍”の前では\x01",
            "一軍すら退かざるを得ないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#Nフフ、それが見抜けるだけでも\x01",
            "大したものです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0131
    ChrTalk(
        0xD,
        "#6Pアリオスさん……！？\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xE,
        (
            "#12Pよもや……\x01",
            "このまま見逃すのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xF,
        (
            "#01403F#11Pまさか……\x01",
            "だが、状況はこちらが不利だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xE,
        "#12P！？\x02",
    )

    CloseMessageWindow()
    OP_68(30, 150, -9540, 1500)
    MoveCamera(24, 25, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(21930, 1500)
    OP_6F(0x79)
    Fade(500)
    OP_68(30, 150, -9540, 0)
    MoveCamera(345, 34, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(21930, 0)
    OP_68(970, 150, -9750, 3000)
    MoveCamera(64, 29, -1, 3000)
    OP_6E(530, 3000)
    SetCameraDistance(21930, 3000)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(977, 0, 100, 0)
    BeginChrThread(0x14, 1, 0, 42)
    PlayEffect(0x5, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4FF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_4FF6)
    Sleep(400)
    PlayEffect(0x5, 0xFF, 0x11, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_5041():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5041)
    Sleep(400)
    PlayEffect(0x5, 0xFF, 0x12, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_508C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x2EE)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_508C)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_516C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_516C)
    Sleep(150)

    def lambda_517C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_517C)
    Sleep(150)

    def lambda_518C():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_518C)
    Sleep(250)

    #C0135
    ChrTalk(
        0x10,
        "#11P…………………………\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xD,
        (
            "#5Pくっ……\x01",
            "リンたちがやり合った？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5231")

    #C0137
    ChrTalk(
        0x105,
        (
            "#10301F#11Pどうやらこのお姉さんたちも\x01",
            "タダ者じゃなさそうだね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5267")

    label("loc_5231")


    #C0138
    ChrTalk(
        0x109,
        (
            "#10108F#11Pくっ……\x01",
            "（ぜんぜん隙が無い……！？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5267")

    OP_68(240, 1000, -7460, 1500)
    MoveCamera(25, 10, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(20910, 1500)
    OP_6F(0x79)

    #C0139
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P#N──良い。\x01",
            "ここで嬲#2Rなぶ#る必要はない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0140
    ChrTalk(
        0x11,
        "#11Pは。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x12,
        "#5Pフフ、承知しましたわ。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x10,
        "#11Pマスターの仰せのままに。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    Sound(805, 0, 70, 0)
    Sound(540, 0, 50, 0)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0x10, 0x3F)
    SetChrChipByIndex(0x11, 0x40)
    SetChrChipByIndex(0x12, 0x41)
    OP_0D()
    Sleep(300)

    def lambda_5355():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5355)
    Sleep(100)

    def lambda_536D():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_536D)
    Sleep(100)

    def lambda_5385():
        OP_9B(0x1, 0xFE, 0x13B, 0xFFFFFD44, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5385)
    Sleep(500)

    #C0143
    ChrTalk(
        0x101,
        "#00010F#1Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xC,
        "#00712F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        "#04804F#5P#Nウフフ、潮時みたいだね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(440, 1150, 7910, 0)
    MoveCamera(30, 11, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(19660, 0)
    SetCameraDistance(18660, 1000)
    OP_6F(0x79)

    def lambda_5449():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_5449)

    def lambda_5456():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5456)

    def lambda_5463():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5463)

    def lambda_5470():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5470)

    def lambda_547D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_547D)

    def lambda_548A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_548A)

    def lambda_5497():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_5497)

    def lambda_54A4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_54A4)

    def lambda_54B1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_54B1)

    #C0146
    ChrTalk(
        0x8,
        (
            "#04704F#5P『計画』の進行度と\x01",
            "七耀脈の状態も確認できた。\x02\x03",

            "#04702Fフフ、そろそろ私も\x01",
            "“仕上げ”に戻るとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x9, 0, 0, 41)
    WaitChrThread(0x9, 0)
    Sound(959, 2, 100, 0)
    PlayEffect(0x6, 0x0, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x6, 0x2, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    Sleep(100)
    OP_93(0x101, 0x0, 0x1F4)

    #C0147
    ChrTalk(
        0x101,
        "#00007F#12P#Nま、待て……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0148
    ChrTalk(
        0xF,
        (
            "#01407F#12P#N……さすがにこのまま\x01",
            "見逃すわけにはいかん……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0149
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5P一つ、忠告しておきましょう。\x02\x03",

            "此度の『計画』において\x01",
            "我らはあくまで脇役にすぎません。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#00005F#12P#Nえ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0151
    ChrTalk(
        0xF,
        "#01405Fなに#12P#N……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0152
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F#5Pじきに獣たちが放たれ、\x01",
            "この地に混乱が招かれるでしょう。\x02\x03",

            "されど、目の前で起きる悲劇に\x01",
            "囚われすぎぬよう心得なさい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        (
            "#04802F#5Pウフフ……\x01",
            "それでは御機嫌よう。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        (
            "#04709F#5Pハハ、またの再会を\x01",
            "楽しみにしててくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 35)
    BeginChrThread(0x102, 1, 0, 35)
    BeginChrThread(0x103, 1, 0, 35)
    BeginChrThread(0x104, 1, 0, 35)
    BeginChrThread(0xF4, 1, 0, 35)
    ClearChrFlags(0xC, 0x1000)
    ClearChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    Sound(4135, 255, 100, 0)    #voice#Companella
    OP_68(-160, 750, 1070, 8000)
    MoveCamera(31, 15, -1, 8000)
    OP_6E(530, 8000)
    SetCameraDistance(25510, 8000)
    StopEffect(0x0, 0x2)

    def lambda_586E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_586E)
    Sound(1035, 0, 100, 0)
    Sound(977, 0, 100, 0)
    Sleep(400)
    StopEffect(0x1, 0x2)

    def lambda_5891():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5891)
    Sound(1035, 0, 100, 0)
    Sleep(400)
    StopEffect(0x2, 0x2)

    def lambda_58AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_58AE)
    Sound(1035, 0, 100, 0)
    Sleep(400)
    StopSound(959, 1000, 100)
    Sleep(600)

    def lambda_58D1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_58D1)
    Sleep(400)

    def lambda_58E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_58E5)
    Sleep(400)

    def lambda_58F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_58F9)
    Sleep(400)
    StopBGM(0x1F40)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xC)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0xD)
    OP_64(0xE)
    OP_64(0xF)
    OP_6F(0x79)
    Fade(500)
    OP_68(-860, 750, -6060, 0)
    MoveCamera(137, 16, -1, 0)
    OP_6E(530, 0)
    SetCameraDistance(17680, 0)
    OP_0D()
    Sleep(300)

    #C0155
    ChrTalk(
        0xE,
        "#11Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xD,
        (
            "#11P《身喰らう蛇》……\x01",
            "とんでもない連中だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        "#00713F#11P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 3, 0, 36)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 38)
    BeginChrThread(0x102, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 38)
    BeginChrThread(0x104, 3, 0, 38)
    BeginChrThread(0x109, 3, 0, 38)
    BeginChrThread(0x105, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 38)
    BeginChrThread(0xE, 3, 0, 38)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xE, 2)
    Sleep(100)

    #C0158
    ChrTalk(
        0x101,
        "#00011F#12Pリーシャ……！？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x102,
        "#00108F#11Pリーシャさん……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0160
    ChrTalk(
        0xC,
        (
            "#00714F#3248V#5P#30W……そろそろ稽古に\x01",
            "戻らなくてはいけませんから。\x02\x03",

            "#00713F#3249V…………失礼します……………\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCB1)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0xC, 3, 0, 37)
    Sleep(500)
    OP_68(2660, 750, -9640, 2000)
    MoveCamera(140, 15, -1, 2000)
    OP_6E(530, 2000)
    SetCameraDistance(23490, 2000)
    WaitChrThread(0xC, 3)
    SetChrFlags(0xC, 0x80)
    OP_6F(0x79)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_68(-960, 750, -5650, 1500)
    MoveCamera(140, 17, -1, 1500)
    OP_6E(530, 1500)
    SetCameraDistance(18220, 1500)
    OP_6F(0x79)

    #C0161
    ChrTalk(
        0x101,
        "#00008F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        (
            "#00108F#6P信じられない事ばかり起きて\x01",
            "ちょっと現実感がないわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        "#00306F#12P………ああ………………\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x103,
        (
            "#00208F#6Pまるで夢の中にいるような\x01",
            "気分です……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x109,
        "#10106F#6Pた、確かにそうかも……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x105,
        (
            "#10308F#12Pヴァルドの事といい……\x01",
            "悪夢の類いだとは思うけどね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0167
    ChrTalk(
        0xF,
        "#01403F#4068V#5P#40Wだが──紛れもなく現実だ。\x02",
    )

    CloseMessageWindow()
    OP_24(0xFE4)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5FA6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5FA6)
    Sleep(50)

    def lambda_5FB6():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FB6)

    def lambda_5FC3():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FC3)
    Sleep(50)

    def lambda_5FD3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5FD3)

    def lambda_5FE0():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5FE0)

    def lambda_5FED():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5FED)
    Sleep(50)

    def lambda_5FFD():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FFD)

    def lambda_600A():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_600A)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)

    #C0168
    ChrTalk(
        0x101,
        "#00001F#6Pアリオスさん……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    #C0169
    ChrTalk(
        0xF,
        (
            "#01401F#5P《結社》の連中は予想以上の\x01",
            "手がかりを残してくれた。\x02\x03",

            "この場所の意味、そして\x01",
            "『じきに放たれる獣たち』……\x02\x03",

            "#01403F呆然としている暇は無さそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        "#00013F#6Pは、はい。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x104,
        "#00311F#12P（『獣たち』……まさか……）\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_61D1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_61D1)

    def lambda_61DE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_61DE)
    Sleep(50)

    def lambda_61EE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_61EE)

    def lambda_61FB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_61FB)
    Sleep(50)

    def lambda_620B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_620B)

    def lambda_6218():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6218)
    Sleep(50)

    def lambda_6228():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6228)

    def lambda_6235():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6235)
    Sleep(700)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)

    #C0172
    ChrTalk(
        0x101,
        (
            "#00011F#6Pそ、そうか。\x01",
            "導力波が届くんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        "#00200F#11Pええ、ギリギリ大丈夫かと。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x5)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0174
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F──はい！\x01",
            "特務支援課、バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3459V#30W……ダドリーだ。\x02\x03",

            "#3460V湖の南岸へ向かったと聞いたが\x01",
            "今、そちらにいるのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD84)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0176
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fあ、はい。\x02\x03",

            "#00001Fその……色々あって\x01",
            "アリオスさんたちも一緒ですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0177
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ならば丁度いい。\x01",
            "ついでに連中にも伝えておけ。\x02\x03",

            "──《赤い星座》のメンバーが\x01",
            "一人残らず市内から消えうせた。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0178
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F#4Sな……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0179
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "できればオルランドから\x01",
            "話を聞きたい。\x02\x03",

            "すぐに戻ってこられるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0180
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00010Fわ、分かりました！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 60, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0181
    ChrTalk(
        0x102,
        "#00101F#5Pど、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x109,
        "#10113F#5P随分慌ててましたけど……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0183
    ChrTalk(
        0x101,
        "#00003F#6Pああ……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0184
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダドリーからの情報を手短に説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0185
    ChrTalk(
        0x104,
        "#00310F#4S#11P！！\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x103,
        "#00205F#11Pそれは……\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xD,
        "#11P《赤い星座》が……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xE,
        (
            "#5Pクッ……\x01",
            "我々も気にはしていたが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xF)

    #C0189
    ChrTalk(
        0xF,
        (
            "#01403F#5P──ロイド。\x01",
            "お前たちは急いで街に戻れ。\x02\x03",

            "#01400F俺たちは、この場所を\x01",
            "調べてから戻るとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_6856():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6856)
    Sleep(50)

    def lambda_6866():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6866)

    def lambda_6873():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6873)
    Sleep(50)

    def lambda_6883():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6883)

    def lambda_6890():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6890)

    def lambda_689D():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_689D)
    Sleep(250)

    #C0190
    ChrTalk(
        0x101,
        (
            "#00011F#6Pあ……\x02\x03",

            "#00003F……すみません。\x01",
            "そうして頂けると助かります。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        "#00306F#12P……すまねぇな。\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xD,
        "#11Pこういう時はお互い様さ。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xE,
        (
            "#5Pそれに、リンとエオリアとて\x01",
            "すぐには動かせないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xF,
        (
            "#01403F#5P《赤い星座》が動いたとすれば\x01",
            "《黒月》の動きもあるはずだ……\x02\x03",

            "#01401F俺たちもすぐに戻るが\x01",
            "くれぐれも気を付けるがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        "#00007F#6Pはい……！\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x109,
        "#10107F#6Pそれでは失礼します！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20180, 2000)
    StopSound(122, 2000, 50)
    StopSound(123, 2000, 70)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x0, 0x10000)
    OP_24(0x323)
    SoundLoad(959)
    SoundLoad(825)
    SetScenarioFlags(0x22, 1)
    NewScene("e4500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2B36 end

    def Function_19_6A7E(): pass

    label("Function_19_6A7E")

    OP_71(0x0, 0x157, 0x16C, 0x0, 0x0)
    OP_79(0x0)
    Sound(913, 0, 100, 0)
    OP_71(0x0, 0x16D, 0x17E, 0x0, 0x20)
    Return()

    # Function_19_6A7E end

    def Function_20_6AA0(): pass

    label("Function_20_6AA0")

    Sound(970, 0, 100, 0)
    Sound(920, 0, 100, 0)
    Sound(202, 0, 100, 0)
    PlayEffect(0x9, 0xFF, 0xFE, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    Sound(893, 0, 70, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(156)
    SetChrSubChip(0xFE, 0x9)
    Sleep(144)
    SetChrSubChip(0xFE, 0xA)
    Sleep(132)
    SetChrSubChip(0xFE, 0xB)
    Sleep(120)
    SetChrSubChip(0xFE, 0xC)
    Sleep(108)
    SetChrSubChip(0xFE, 0xD)
    Sleep(96)
    SetChrSubChip(0xFE, 0xE)
    Sleep(84)
    SetChrSubChip(0xFE, 0xF)
    Sleep(72)

    label("loc_6B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B8C")
    Sound(893, 0, 50, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(60)
    SetChrSubChip(0xFE, 0x9)
    Sleep(60)
    SetChrSubChip(0xFE, 0xA)
    Sleep(60)
    SetChrSubChip(0xFE, 0xB)
    Sleep(60)
    SetChrSubChip(0xFE, 0xC)
    Sleep(60)
    SetChrSubChip(0xFE, 0xD)
    Sleep(60)
    SetChrSubChip(0xFE, 0xE)
    Sleep(60)
    SetChrSubChip(0xFE, 0xF)
    Sleep(60)
    Jump("loc_6B3A")

    label("loc_6B8C")

    Sound(893, 0, 60, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(72)
    SetChrSubChip(0xFE, 0x9)
    Sleep(84)
    SetChrSubChip(0xFE, 0xA)
    Sleep(96)
    SetChrSubChip(0xFE, 0xB)
    Sleep(108)
    SetChrSubChip(0xFE, 0xC)
    Sleep(120)
    SetChrSubChip(0xFE, 0xD)
    Sleep(132)
    SetChrSubChip(0xFE, 0xE)
    Sleep(144)
    SetChrSubChip(0xFE, 0xF)
    Sleep(156)
    Sound(531, 0, 80, 0)
    Sound(358, 0, 50, 0)
    Sound(308, 0, 100, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(400)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_6AA0 end

    def Function_21_6BEC(): pass

    label("Function_21_6BEC")

    Sleep(2000)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x1F4, 0x1)
    Return()

    # Function_21_6BEC end

    def Function_22_6BFF(): pass

    label("Function_22_6BFF")

    SetChrChipByIndex(0xFE, 0x32)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    Sound(531, 0, 80, 0)
    Sound(358, 0, 60, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(500)
    BeginChrThread(0x15, 3, 0, 20)
    BeginChrThread(0x15, 2, 0, 21)
    Sleep(2500)
    ClearScenarioFlags(0x0, 1)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x15, 3)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(3000)
    OP_82(0x0, 0x64, 0x1388, 0x320)
    SetCameraDistance(11000, 250)

    def lambda_6C9E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_6C9E)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(300)
    Sound(288, 0, 70, 0)
    Sound(308, 0, 100, 0)
    Sound(358, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(100)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Return()

    # Function_22_6BFF end

    def Function_23_6CF4(): pass

    label("Function_23_6CF4")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(150)
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x8)
    Sleep(800)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(100)
    Return()

    # Function_23_6CF4 end

    def Function_24_6D5E(): pass

    label("Function_24_6D5E")

    SetChrChipByIndex(0xFE, 0x31)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 70, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Return()

    # Function_24_6D5E end

    def Function_25_6D7D(): pass

    label("Function_25_6D7D")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_6D95():
        OP_9D(0xFE, 0xFFFFFF06, 0xFFFFFD12, 0x726, 0x96, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6D95)
    WaitChrThread(0xFE, 2)
    PlayEffect(0x4, 0x0, 0xFE, 0x4, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    StopEffect(0x0, 0x2)
    Return()

    # Function_25_6D7D end

    def Function_26_6E8E(): pass

    label("Function_26_6E8E")

    SetChrSubChip(0xFE, 0x5)
    Sleep(200)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(844, 0, 60, 0)
    Sound(250, 0, 80, 0)

    def lambda_6EAE():
        OP_9D(0xFE, 0x258, 0xFA, 0x1900, 0x60E, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6EAE)
    WaitChrThread(0xFE, 2)
    Sound(326, 0, 50, 0)
    Sleep(300)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sound(531, 0, 60, 0)
    Sound(358, 0, 60, 0)
    SetChrChipByIndex(0xA, 0x30)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    Return()

    # Function_26_6E8E end

    def Function_27_6EFA(): pass

    label("Function_27_6EFA")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)

    label("loc_6F02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F29")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_6F02")

    label("loc_6F29")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    Sound(251, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0xFFFFFE70, 0xFFFFF34E, 0x2EE, 0x3AB6)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Sleep(150)
    Return()

    # Function_27_6EFA end

    def Function_28_6FA6(): pass

    label("Function_28_6FA6")

    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)

    label("loc_6FAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FD5")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_6FAE")

    label("loc_6FD5")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0xFA, 0x0, 0xFFFFF34E, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Return()

    # Function_28_6FA6 end

    def Function_29_7046(): pass

    label("Function_29_7046")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    label("loc_704E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7075")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_704E")

    label("loc_7075")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFEF66, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Return()

    # Function_29_7046 end

    def Function_30_70E6(): pass

    label("Function_30_70E6")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)

    label("loc_70EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7115")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_70EE")

    label("loc_7115")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0xFFFFFF06, 0x0, 0xFFFFF15A, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Sleep(150)
    Return()

    # Function_30_70E6 end

    def Function_31_718C(): pass

    label("Function_31_718C")

    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)

    label("loc_7194")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71BB")
    OP_A6(0xFE, 0x1E, 0x1E, 0xFA, 0xBB8)
    Jump("loc_7194")

    label("loc_71BB")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_9C(0xFE, 0x190, 0x0, 0xFFFFF34E, 0x2EE, 0x5DC)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    Return()

    # Function_31_718C end

    def Function_32_722C(): pass

    label("Function_32_722C")

    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0xDAC, 0x0, 0xFFFFFE0C, 0x3E8, 0xBB8)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0xFFFFF060, 0x0, 0x0, 0x5DC, 0xBB8)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0xC8, 0xBB8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)

    label("loc_7293")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72AA")
    Sleep(1)
    Jump("loc_7293")

    label("loc_72AA")

    Sleep(200)
    OP_9D(0xFE, 0xC8, 0xFFFFFD12, 0xFFFFF3E4, 0x2EE, 0x5DC)
    Return()

    # Function_32_722C end

    def Function_33_72C5(): pass

    label("Function_33_72C5")

    Sleep(50)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sound(540, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sleep(50)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    Sound(540, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    Sound(540, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_33_72C5 end

    def Function_34_73FD(): pass

    label("Function_34_73FD")

    Sleep(50)
    PlayEffect(0x7, 0xFF, 0x101, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x7, 0xFF, 0x102, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x7, 0xFF, 0x103, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x7, 0xFF, 0x104, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x7, 0xFF, 0xF4, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_34_73FD end

    def Function_35_7520(): pass

    label("Function_35_7520")

    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_7520 end

    def Function_36_7533(): pass

    label("Function_36_7533")

    OP_93(0xFE, 0xB3, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x514, 0x4B0, 0x0)
    OP_95(0xFE, 470, -750, -5220, 1200, 0x0)
    OP_93(0xFE, 0x87, 0x0)
    Return()

    # Function_36_7533 end

    def Function_37_7568(): pass

    label("Function_37_7568")

    SetChrFlags(0xFE, 0x40)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x5, 0x3E8, 0x1B58, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x3E8, 0x1B58, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x3E8, 0x1B58, 0x1)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_9B(0x0, 0xFE, 0x5, 0x9C4, 0x1B58, 0x1)
    SetChrFlags(0xFE, 0x20)
    Sound(844, 0, 50, 0)
    OP_9C(0xFE, 0xDAC, 0x6D6, 0xFFFFDECC, 0x7D0, 0xDAC)
    ClearChrFlags(0xFE, 0x20)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x1B58, 0x1)
    SetChrFlags(0xFE, 0x20)
    Sound(844, 0, 50, 0)
    OP_9C(0xFE, 0x3E8, 0xFA0, 0xFFFFF768, 0x1388, 0x9C4)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_37_7568 end

    def Function_38_765A(): pass

    label("Function_38_765A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7674")
    TurnDirection(0xFE, 0xC, 500)
    Sleep(300)
    Jump("Function_38_765A")

    label("loc_7674")

    Return()

    # Function_38_765A end

    def Function_39_7675(): pass

    label("Function_39_7675")

    Sleep(200)
    Sound(287, 0, 100, 0)
    Sound(270, 0, 80, 0)
    Sound(225, 0, 70, 0)
    Sound(833, 0, 70, 0)
    Sound(825, 2, 100, 0)
    Sleep(1000)
    Sound(271, 0, 80, 0)
    Sound(287, 0, 60, 0)
    Sleep(1000)
    StopSound(225, 1000, 40)
    StopSound(825, 1000, 90)
    Return()

    # Function_39_7675 end

    def Function_40_76B5(): pass

    label("Function_40_76B5")

    SetChrChipByIndex(0xFE, 0x42)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    Sound(1037, 0, 100, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(400)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)
    SetChrSubChip(0xFE, 0x2)
    Sleep(400)
    Sound(1037, 0, 70, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(400)
    SetChrSubChip(0xFE, 0x4)
    Sleep(400)
    Return()

    # Function_40_76B5 end

    def Function_41_76F3(): pass

    label("Function_41_76F3")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Sound(325, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    Return()

    # Function_41_76F3 end

    def Function_42_770C(): pass

    label("Function_42_770C")

    Sleep(1500)
    Sound(936, 0, 100, 0)
    Sleep(400)
    Sound(936, 0, 80, 0)
    Sleep(400)
    Sound(936, 0, 80, 0)
    Return()

    # Function_42_770C end

    SaveToFile()

Try(main)
