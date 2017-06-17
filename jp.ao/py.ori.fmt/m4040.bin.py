from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "アーネスト",             # 1
        "ハルトマン元議長",       # 2
        "イベント用モンスター",   # 3
        "イベント用モンスター",   # 4
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
        "Function_4_1A70",         # 04, 4
        "Function_5_1B1E",         # 05, 5
        "Function_6_1B61",         # 06, 6
        "Function_7_1BB6",         # 07, 7
        "Function_8_1C0B",         # 08, 8
        "Function_9_1C60",         # 09, 9
        "Function_10_1CB5",        # 0A, 10
        "Function_11_1D2E",        # 0B, 11
        "Function_12_1D94",        # 0C, 12
        "Function_13_2E86",        # 0D, 13
        "Function_14_2ED5",        # 0E, 14
        "Function_15_2F06",        # 0F, 15
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
        "#00007F（いた……！）\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x10A,
        "#00601F#6P（追い付いたか……！）\x02",
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
            "#30Wア、アーネスト君……\x01",
            "いいかげんに解放してくれ……！\x02\x03",

            "も、もう私は付き合いきれん！\x02",
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
            "#6P#02604Fやれやれ、困りますねぇ議長。\x02\x03",

            "#02610F貴方にはクロスベルの政界に\x01",
            "ちゃんと返り咲いて頂かないと……\x02\x03",

            "この私が次期市長となるためにもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        (
            "#02701F#11Pい、いいかげんにするがいい！\x02\x03",

            "クロスベルの政界に返り咲く！？\x01",
            "今更そんな事が\x01",
            "可能だと思っているのか！？\x02\x03",

            "ましてや貴様ごときが\x01",
            "あのディーター・クロイスから\x01",
            "市長の座を奪えるはずがなかろう！？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#6P#02613Fクク、簡単なことですよ。\x02\x03",

            "人の身では叶わなくとも\x01",
            "真なる“神”に近付けばたやすい……\x02\x03",

            "#02610Fあらゆる因果を見通す叡智#4Rえい ち #があれば\x01",
            "どんな現実も思いのままになる……\x02\x03",

            "#02614Fそう、かの偉大なる\x01",
            "ヨアヒム・ギュンター師のようにね！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        "#02705F#11Pく、狂ってる……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2091, 255, 100, 0)    #voice#Lloyd

    #N0008
    NpcTalk(
        0x101,
        "ロイドの声",
        "#30Wさせるか……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_AC7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AC7)
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
        "#02700Fお、お前たちは！？\x02",
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
            "フフ、追いついてきたか。\x02\x03",

            "お久しぶりと言っておこうか。\x01",
            "ロイド君、それにダドリー君。\x02\x03",

            "アルタイル市での捜査は\x01",
            "ご苦労だったね。\x02",
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
        "#00013F#6Pアーネスト、あんた……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x108, 3)

    #C0012
    ChrTalk(
        0x10A,
        (
            "#6P#00601F我々が追っているのに\x01",
            "気付いていたというのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#02613F#11Pクク、全ては偉大なる\x01",
            "『グノーシス』の力によるもの。\x02\x03",

            "君たちが我々の行方を追って\x01",
            "アルタイル市を訪れたこと……\x02\x03",

            "そして我々の動向を突き止めて\x01",
            "共和国軍の許可を得てから\x01",
            "ここまで追って来たこと……\x02\x03",

            "#02610F全てお見通しなのだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00010F#6Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x109,
        "#6P#10113Fどうしてそこまで……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x108,
        (
            "#01408F#6Pどうやら不可思議な知覚によって\x01",
            "我々の動向を察知したようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "#02705Fつ、つまりお前たちは\x01",
            "クロスベル警察の人間というわけか。\x02\x03",

            "#02703F……ええい、背に腹はかえられん！\x02\x03",

            "#02701F頼む、素直に投降するから\x01",
            "この狂人を取り押さえてくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "#02613F#11Pおやおや、狂人とは失礼ですな。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#00003F#6P言われるまでもない……\x02",
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
            "#00007F#6P──ハルトマン元議長、\x01",
            "およびアーネスト・ライズ！\x02\x03",

            "自治州法改正項目に基づき、\x01",
            "拘置所脱走、および多数の余罪で\x01",
            "あなたたちの身柄を拘束する。\x02\x03",

            "大人しく投降してもらおう！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#02610F#11Pクク、そう焦るものじゃない。\x02\x03",

            "#02613F今日、私はヨアヒム師の跡を継いで\x01",
            "《Ｄ》への扉を開く事になる……\x02\x03",

            "#02614F余興はそれからでも遅くなかろう！？\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0022
    ChrTalk(
        0x108,
        "#01401F#6Pむ……！\x02",
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

    def lambda_123A():
        OP_96(0xFE, 0xA8C, 0xC8, 0x7D0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_123A)

    def lambda_1254():
        OP_96(0xFE, 0xFFFFF574, 0xC8, 0x7D0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1254)

    def lambda_126E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_126E)

    def lambda_127F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_127F)
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

    def lambda_131F():
        OP_96(0xFE, 0xFFFFFF38, 0xBE, 0xFFFFF380, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_131F)
    Sleep(300)

    def lambda_133C():
        OP_96(0xFE, 0xC8, 0xBE, 0xFFFFEC78, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_133C)
    Sleep(100)

    def lambda_1359():
        OP_96(0xFE, 0x5DC, 0xBE, 0xFFFFEDA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1359)
    Sleep(100)

    def lambda_1376():
        OP_96(0xFE, 0xFFFFFA24, 0xBE, 0xFFFFEF34, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1376)
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
        "#02705Fひ、ひいいっ！？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x109,
        "#3P#10110F#6Pこ、これって……！\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x10A,
        "#6P#00607F#6P人形兵器の一種か！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1532")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆前編２周目クエストクリア\x01",        # 0
            "◆前編２周目クエスト未クリア\x01",      # 1
            "◆変更しない\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1519"),
        (1, "loc_1523"),
        (2, "loc_152D"),
        (SWITCH_DEFAULT, "loc_152D"),
    )


    label("loc_1519")

    OP_29(0x34, 0x4, 0x10)
    Jump("loc_1532")

    label("loc_1523")

    OP_29(0x34, 0x3, 0x10)
    Jump("loc_1532")

    label("loc_152D")

    Jump("loc_1532")

    label("loc_1532")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1640")

    #C0026
    ChrTalk(
        0x101,
        (
            "#00010F#6PジオフロントＢ２区画を\x01",
            "凍りつかせた魔導人形……！\x02\x03",

            "#00007F気をつけてください！\x01",
            "途轍もなく強力な相手です！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#02613F#11Pクク、それでは諸君。\x01",
            "我々は先に行かせてもらうよ。\x02\x03",

            "#02614Fヨアヒム師が遺した守護者の力、\x01",
            "とくと味わってくれたまえ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_172F")

    label("loc_1640")


    #C0028
    ChrTalk(
        0x101,
        (
            "#00005F#6Pヨアヒムが従えていた\x01",
            "中世の魔導人形……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#02613F#11Pクク、あれよりも\x01",
            "遥かに強力な性能だがね。\x02\x03",

            "#02610F──それでは諸君。\x01",
            "我々は先に行かせてもらうよ。\x02\x03",

            "#02614Fヨアヒム師が遺した守護者の力、\x01",
            "とくと味わってくれたまえ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_172F")

    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x0, 0x1F4)
    OP_68(1000, 1200, 3700, 4000)

    def lambda_1754():
        OP_96(0xFE, 0x12C, 0xC8, 0x13EC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1754)
    WaitChrThread(0x8, 1)
    OP_64(0x9)
    Sound(802, 0, 100, 0)
    BeginChrThread(0x8, 3, 0, 10)
    BeginChrThread(0x9, 3, 0, 11)
    Sleep(3500)

    #C0030
    ChrTalk(
        0x109,
        "#10107Fああっ！？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x10A,
        "#00610Fクッ、逃がすか……！\x02",
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

    def lambda_1829():
        OP_A6(0xFE, 0x32, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1829)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2, 0x1, 0xFF, 0x0, 3000, 2000, 2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(881, 0, 50, 0)
    EndChrThread(0xB, 0x0)
    SetChrChipByIndex(0xB, 0x2C)
    SetChrSubChip(0xB, 0x0)

    def lambda_18AC():
        OP_A6(0xFE, 0x32, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_18AC)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2, 0x2, 0xFF, 0x0, -1000, 2000, 2500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    #C0032
    ChrTalk(
        0x108,
        (
            "#01403F#6Pどうやら尋常な相手では\x01",
            "無さそうだな……\x02\x03",

            "#01407F全力で撃破するぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#00007F#6Pはいっ！\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15000, 500)
    OP_68(0, 1200, 1000, 500)

    def lambda_19AD():
        OP_97(0x101, 0x1, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19AD)
    Sleep(30)

    def lambda_19CA():
        OP_97(0x108, 0x1, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_19CA)
    Sleep(30)

    def lambda_19E7():
        OP_97(0x10A, 0x1, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_19E7)
    Sleep(30)

    def lambda_1A04():
        OP_97(0x109, 0x1, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A04)
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

    def Function_4_1A70(): pass

    label("Function_4_1A70")

    Sleep(1000)

    def lambda_1A78():
        OP_95(0xFE, 0, 190, 600, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1A78)
    WaitChrThread(0x9, 1)
    Sleep(500)

    def lambda_1A99():
        OP_95(0xFE, 0, 190, 2600, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1A99)
    WaitChrThread(0x9, 1)
    Sleep(500)

    def lambda_1ABA():
        OP_95(0xFE, 0, 190, 4600, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1ABA)
    WaitChrThread(0x9, 1)
    OP_A6(0x9, 0x0, 0x32, 0x12C, 0x7D0)
    Sleep(200)

    def lambda_1AEE():
        OP_95(0xFE, 0, 190, 5600, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1AEE)
    WaitChrThread(0x9, 1)
    OP_A6(0x9, 0x0, 0x32, 0x12C, 0x7D0)
    Sleep(200)
    Return()

    # Function_4_1A70 end

    def Function_5_1B1E(): pass

    label("Function_5_1B1E")

    Sleep(3000)

    def lambda_1B26():
        OP_95(0xFE, 0, 190, 700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B26)
    WaitChrThread(0x8, 1)
    Sleep(1500)

    def lambda_1B47():
        OP_95(0xFE, 0, 190, 3300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B47)
    WaitChrThread(0x8, 1)
    Return()

    # Function_5_1B1E end

    def Function_6_1B61(): pass

    label("Function_6_1B61")

    SetChrPos(0xFE, 700, 0, -30000, 0)
    OP_96(0xFE, 0x2BC, 0x0, 0xFFFFB5C8, 0x1388, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFDC10, 0x1388, 0x1)
    OP_96(0xFE, 0xFFFFFF38, 0xBE, 0xFFFFF63C, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_6_1B61 end

    def Function_7_1BB6(): pass

    label("Function_7_1BB6")

    SetChrPos(0xFE, 700, 0, -30000, 0)
    OP_96(0xFE, 0x2BC, 0x0, 0xFFFFB5C8, 0x1388, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFDC10, 0x1388, 0x1)
    OP_96(0xFE, 0xC8, 0xBE, 0xFFFFF060, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_7_1BB6 end

    def Function_8_1C0B(): pass

    label("Function_8_1C0B")

    SetChrPos(0xFE, 700, 0, -30000, 0)
    OP_96(0xFE, 0x2BC, 0x0, 0xFFFFB5C8, 0x1388, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFDC10, 0x1388, 0x1)
    OP_96(0xFE, 0x5DC, 0xBE, 0xFFFFF18C, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_8_1C0B end

    def Function_9_1C60(): pass

    label("Function_9_1C60")

    SetChrPos(0xFE, 700, 0, -30000, 0)
    OP_96(0xFE, 0x2BC, 0x0, 0xFFFFB5C8, 0x1388, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFDC10, 0x1388, 0x1)
    OP_96(0xFE, 0xFFFFFA24, 0xBE, 0xFFFFF31C, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_9_1C60 end

    def Function_10_1CB5(): pass

    label("Function_10_1CB5")


    def lambda_1CBA():
        OP_96(0xFE, 0x1004, 0x0, 0x39D0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1CBA)

    def lambda_1CD4():
        OP_96(0xFE, 0x1194, 0x0, 0x37DC, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1CD4)
    WaitChrThread(0x8, 1)

    def lambda_1CF2():
        OP_96(0xFE, 0x19C8, 0x60E, 0x6C98, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1CF2)
    WaitChrThread(0x9, 1)

    def lambda_1D10():
        OP_96(0xFE, 0x1B58, 0x60E, 0x6AA4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D10)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    Return()

    # Function_10_1CB5 end

    def Function_11_1D2E(): pass

    label("Function_11_1D2E")


    #C0034
    ChrTalk(
        0x9,
        "#12P#18A#02700Fは、放せ……\x02",
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
        "#6P#18A#4S放してくれええええっ！\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    Return()

    # Function_11_1D2E end

    def Function_12_1D94(): pass

    label("Function_12_1D94")

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

    def lambda_1F0C():
        OP_A6(0xFE, 0x32, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1F0C)
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

    def lambda_1F7D():
        OP_A6(0xFE, 0x32, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1F7D)
    PlayEffect(0x0, 0x0, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetCameraDistance(18000, 3000)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_2017():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2017)

    def lambda_2028():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2028)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_6F(0x79)

    def lambda_20B8():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20B8)
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
        "#6P#00015F#30W……ぐうっ……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x109,
        "#3P#10106F#30Wな、なんて強さ……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x10A,
        (
            "#6P#00610Fチッ……\x01",
            "時間を取られたか！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x108,
        "#01407Fよし、追いかけるぞ！\x02",
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
            "#00607F#11Pどうした！\x01",
            "動けないのか！？\x02",
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

    def lambda_2292():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2292)
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
        "#6P#00007Fだ、大丈夫です……！\x02",
    )

    CloseMessageWindow()

    def lambda_22FA():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_22FA)
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
        "#6P#10101Fこちらも何とか……！\x02",
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
        "#01407Fダドリー、上だ！\x02",
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

    def lambda_242C():
        OP_9D(0xFE, 0x1C20, 0x1194, 0xA21C, 0x708, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_242C)
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
        "#00610Fクッ……！？\x02",
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

    def lambda_2564():
        OP_96(0xFE, 0x16A8, 0x64, 0x59D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2564)
    Sleep(200)

    def lambda_2581():
        OP_96(0xFE, 0x1004, 0x64, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2581)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)

    #C0045
    ChrTalk(
        0x101,
        "#00005Fみ、道が……！？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x109,
        "#10110Fそ、そんな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    OP_0D()

    def lambda_25EE():
        OP_96(0xFE, 0x1F40, 0x1194, 0xA604, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_25EE)
    WaitChrThread(0x108, 1)

    #C0047
    ChrTalk(
        0x108,
        (
            "#01403F先ほどの戦闘の衝撃で\x01",
            "脆#2Rもろ#くなった地盤が崩落したか……\x02\x03",

            "#01400Fこの距離を飛び越えるのは\x01",
            "少々、難しそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00006F#5Pはい……さすがに。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        "#10106F#5Pす、すみません……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x10A,
        (
            "#00606Fチッ……\x01",
            "こうなったら仕方ない。\x02\x03",

            "#00607Fそこで待っていろ！\x01",
            "我々だけでケリを付けてくる！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#00007Fそ、そんな！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x109,
        (
            "#10101Fいくらお２人でも\x01",
            "サポート無しじゃ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x108,
        (
            "#01400Fいや──\x01",
            "ここは別行動としよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_27E4():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_27E4)

    #C0054
    ChrTalk(
        0x101,
        "#00005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x10A,
        "#6P#00605Fどういうことだ？\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x108,
        (
            "#01403Fここから最奥に至るルートは\x01",
            "２つある。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x108, 0x5A, 0x1F4)
    Sleep(300)

    #C0057
    ChrTalk(
        0x108,
        "#01400F#6Pもう１つはあちらだ。\x02",
    )

    CloseMessageWindow()
    OP_68(26000, -9000, 29000, 4000)
    MoveCamera(340, 15, 0, 4000)
    OP_6E(650, 4000)
    SetCameraDistance(45500, 4000)

    def lambda_28B2():
        OP_93(0x10A, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_28B2)
    Sleep(100)

    def lambda_28C2():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28C2)
    Sleep(100)

    def lambda_28D2():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_28D2)
    Sleep(100)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)

    #C0058
    ChrTalk(
        0x101,
        "#00005F#N#5P別の道が……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0059
    ChrTalk(
        0x109,
        "#10100F#N#5Pもしかしてあの先が？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0060
    ChrTalk(
        0x108,
        (
            "#01404F#12P#N#5Pああ、遠回りになるが\x01",
            "最奥で合流できるはずだ。\x02",
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
        "#00603F#5Pならば話は早い！\x02",
    )

    CloseMessageWindow()
    OP_93(0x10A, 0xB4, 0x1F4)
    Sleep(300)

    #C0062
    ChrTalk(
        0x10A,
        (
            "#00607F#11Pバニングス、シーカー曹長！\x01",
            "我々はこのまま連中を追う！\x02\x03",

            "何とか合流するがいい！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A3C():
        OP_93(0x101, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A3C)
    Sleep(0)

    def lambda_2A4C():
        OP_93(0x109, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A4C)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)

    def lambda_2A64():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2A64)
    Sleep(150)

    #C0063
    ChrTalk(
        0x101,
        "#00007F了解です！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        "#10107Fイエス・サー！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0065
    ChrTalk(
        0x108,
        (
            "#01404F#4039V#11P#30W武運を──\x01",
            "気をつけて行くがいい。\x02",
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
            "#12P#00003Fよし……俺たちも急ごう！\x02\x03",

            "#00001F曹長、すぐに動けるか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0067
    ChrTalk(
        0x109,
        "#10101F#5Pええ、大丈夫です！\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0068
    ChrTalk(
        0x109,
        (
            "#10105F#5Pそうだ、ロイドさん……\x02\x03",

            "#10100Fせっかくの機会ですから\x01",
            "コンビネーションを使った戦技#4Rクラフト#を\x01",
            "試してみませんか？\x02",
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
            "#00002F#12Pそうか、いいかもしれないな。\x02\x03",

            "#00004Fお互いのクセも判ってきたし、\x01",
            "何とかなりそうだ。\x02\x03",

            "#00000F上手く使いこなして\x01",
            "慎重に、確実に進んでいこう！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2442, 255, 100, 0)    #voice#Noel

    #C0070
    ChrTalk(
        0x109,
        "#10109F#5P#30Wはいっ！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(300)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D78")
    AddCraft(0x0, 0x1A0)
    AddCraft(0x8, 0x1A0)
    Jump("loc_2D80")

    label("loc_2D78")

    AddCraft(0x0, 0x18C)
    AddCraft(0x8, 0x18C)

    label("loc_2D80")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとノエルがコンビクラフト\x01\x07\x02",

            "『ブレイブハーツ』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＣＰを１００ずつ消費することで\x01",
            "強力なコンビネーション攻撃が繰り出せます。\x07\x00\x02",
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

    # Function_12_1D94 end

    def Function_13_2E86(): pass

    label("Function_13_2E86")

    OP_96(0xFE, 0x1324, 0x0, 0x3A98, 0x1388, 0x1)

    def lambda_2E9F():
        OP_95(0xFE, 7000, 3200, 33300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E9F)
    Sleep(3000)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_13_2E86 end

    def Function_14_2ED5(): pass

    label("Function_14_2ED5")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0x1324, 0x0, 0x3A98, 0x157C, 0x1)
    OP_95(0xFE, 7200, 4500, 43800, 5500, 0x0)
    Return()

    # Function_14_2ED5 end

    def Function_15_2F06(): pass

    label("Function_15_2F06")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_96(0xFE, 0x1D4C, 0x1194, 0xE678, 0x1388, 0x0)
    Return()

    # Function_15_2F06 end

    SaveToFile()

Try(main)
