from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4500.bin",                # FileName
        "e4500",                    # MapName
        "e4500",                    # Location
        0x0000,                     # MapIndex
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
        "e4500",                  # 0
        "ヨナの声",               # 1
        "地形",                   # 2
        "水面",                   # 3
        "SE制御",                 # 4
    ))

    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(296, 0)                                        # 0

    ScpFunction((
        "Function_0_128",          # 00, 0
        "Function_1_160",          # 01, 1
        "Function_2_161",          # 02, 2
        "Function_3_931",          # 03, 3
        "Function_4_96F",          # 04, 4
        "Function_5_140C",         # 05, 5
        "Function_6_143F",         # 06, 6
        "Function_7_2C30",         # 07, 7
        "Function_8_2D2E",         # 08, 8
    ))


    def Function_0_128(): pass

    label("Function_0_128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_13C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_15F")

    label("loc_13C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_150")
    ClearScenarioFlags(0x22, 1)
    Event(0, 4)
    Jump("loc_15F")

    label("loc_150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_15F")
    ClearScenarioFlags(0x22, 2)
    Event(0, 6)

    label("loc_15F")

    Return()

    # Function_0_128 end

    def Function_1_160(): pass

    label("Function_1_160")

    Return()

    # Function_1_160 end

    def Function_2_161(): pass

    label("Function_2_161")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map/mprain00.eff")
    LoadChrToIndex("chr/ch02902.itc", 0x1E)
    SoundLoad(483)
    SoundLoad(126)
    SetChrPos(0x101, -950, 210, -1600, 180)
    SetChrPos(0x109, 0, 210, -1750, 180)
    SetChrPos(0x102, 950, 210, -1600, 180)
    SetChrPos(0x105, 800, 900, 0, 180)
    SetChrPos(0x103, -1130, 900, -660, 180)
    SetChrPos(0x104, -70, 900, 360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    SetChrPos(0x9, 0, 0, 0, 180)
    OP_D5(0x9, 0x0, 0x2BF20, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    SetChrPos(0xA, 0, 0, 0, 180)
    OP_D5(0xA, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x1, 0x5A)
    OP_71(0x1, 0x3E8, 0x7CF, 0x0, 0x20)
    PlayBGM("ed7151", 0)
    BeginChrThread(0xB, 1, 0, 3)
    PlayEffect(0x0, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x9C4)
    OP_11(0x95, 0xA0, 0xB5, 0x1E, 0x190, 0x9C4)
    Sound(128, 1, 50, 0)
    OP_68(-770, 3300, -4220, 0)
    MoveCamera(150, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(28820, 0)
    FadeToBright(1000, 0)
    OP_68(-1940, 4000, 9830, 6500)
    MoveCamera(172, -3, 0, 6500)
    OP_6E(650, 6500)
    SetCameraDistance(21530, 6500)
    Sleep(4500)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
    OP_11(0xB7, 0xDA, 0xDD, 0x1E, 0x190, 0x9C4)
    StopSound(128, 1000, 100)
    Sleep(500)
    StopEffect(0x7, 0x2)
    OP_6F(0x79)
    Sleep(1500)
    OP_68(-1080, 2150, -2460, 0)
    MoveCamera(44, 16, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    Fade(500)
    OP_0D()
    Sleep(300)

    #C0001
    ChrTalk(
        0x103,
        (
            "#00203F#5P……天気予報の通り、\x01",
            "午後からは晴れましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        (
            "#00306F#5Pこれも女神の\x01",
            "導きかもしれねぇな。\x02\x03",

            "#00301F正直、どんな危険が\x01",
            "待ち受けてるか判らねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x105,
        (
            "#10304F#5Pま、雨の中で探索するよりは\x01",
            "マシかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x109,
        (
            "#10108F#5P……可能性があるとしたら\x01",
            "《幻獣》でしょうか、それとも……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00106F#5P正直、今の状況だと\x01",
            "どんな可能性も考えられそうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00003F#5P……アリオスさんたちの到着が\x01",
            "何時#4Rい つ#になるか判らない。\x02\x03",

            "#00008Fなるべく俺たちが先行して\x01",
            "リンさん達の無事を確認しよう。\x02\x03",

            "#00001F場合によったら……\x01",
            "警備隊にも連絡する必要が\x01",
            "あるかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x109,
        "#10101F#5P……はい。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x104,
        (
            "#00301F#5Pお姉さんたち……\x01",
            "どうか無事でいてくれよな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0009
    ChrTalk(
        0x103,
        (
            "#00205F#5P……これは……\x02\x03",

            "#00207F湿度の急激な上昇を確認。\x01",
            "注意してください……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_6CE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6CE)
    Sleep(50)

    def lambda_6DE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6DE)
    Sleep(50)

    def lambda_6EE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6EE)
    Sleep(50)

    def lambda_6FE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6FE)
    Sleep(500)

    #C0010
    ChrTalk(
        0x101,
        "#00011F#5Pなに……！？\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1F40)
    OP_7D(0xC0, 0xE0, 0xFF, 0x0, 0xAF0)
    OP_11(0x90, 0xB0, 0xD0, 0x1, 0x32, 0xAF0)
    Sleep(500)
    OP_68(-2630, 2150, -3190, 3000)
    MoveCamera(51, 12, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(19410, 3000)
    OP_6F(0x79)
    Sleep(500)

    #C0011
    ChrTalk(
        0x105,
        "#10301F#6Pこれは……霧！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#00107F#6Pさ、さっきまで\x01",
            "あんなに晴れていたのに！？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x109,
        "#10107F#5Pロ、ロイドさん……どうします！？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00010F#5Pくっ……\x02\x03",

            "#00007F速度を落として\x01",
            "慎重に進んでみてくれ！\x02\x03",

            "ティオ、岩壁の接近を\x01",
            "感知できるか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#00201F#5Pはい、何とか……！\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00310F#5Pこうなったらもう、\x01",
            "腹を括るしかねえな……！\x02",
        )
    )

    CloseMessageWindow()
    OP_11(0x90, 0xB0, 0xD0, 0x1, 0x1E, 0xAF0)
    SetCameraDistance(20410, 2800)
    Sleep(800)
    StopSound(126, 2000, 50)
    StopSound(483, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x105, 0x4)
    WaitBGM()
    OP_24(0x7E)
    OP_24(0x1E3)
    SetScenarioFlags(0x22, 0)
    NewScene("m4200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_161 end

    def Function_3_931(): pass

    label("Function_3_931")

    Sound(126, 2, 50, 0)
    Sound(483, 2, 20, 0)
    Sleep(200)
    OP_25(0x1E3, 0x1E)
    Sleep(200)
    OP_25(0x1E3, 0x28)
    Sleep(200)
    OP_25(0x1E3, 0x32)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Sleep(200)
    OP_25(0x1E3, 0x46)
    Sleep(200)
    OP_25(0x1E3, 0x50)
    Sleep(200)
    OP_25(0x1E3, 0x5A)
    Return()

    # Function_3_931 end

    def Function_4_96F(): pass

    label("Function_4_96F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02902.itc", 0x1E)
    SoundLoad(483)
    SoundLoad(126)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis265.itp")
    SetChrPos(0x101, -800, 210, -1600, 180)
    SetChrPos(0x109, 0, 210, -1750, 180)
    SetChrPos(0x102, 950, 210, -1600, 180)
    SetChrPos(0x105, -1100, 780, 1450, 180)
    SetChrPos(0x103, 300, 780, 450, 180)
    SetChrPos(0x104, 900, 780, 1250, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x105, 0x4)
    PlayBGM("ed7560", 0)
    BeginChrThread(0xB, 1, 0, 5)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    SetChrPos(0xA, 0, 0, 0, 180)
    OP_74(0x1, 0x5A)
    OP_71(0x1, 0x7CF, 0x3E8, 0x0, 0x20)
    OP_68(250, 2150, 10000, 0)
    MoveCamera(345, 138, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(106500, 0)
    FadeToBright(1000, 0)
    OP_68(0, 2150, 5750, 3000)
    SetCameraDistance(88650, 3000)
    OP_0D()
    Sleep(1500)
    OP_68(1470, 2150, -5770, 0)
    MoveCamera(320, 175, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(34500, 0)
    Fade(1000)
    OP_68(20, 2150, -4920, 4500)
    MoveCamera(332, 175, 0, 4500)
    SetCameraDistance(22000, 4500)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-810, 2150, 460, 0)
    MoveCamera(327, 158, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(13000, 1500)
    OP_6F(0x79)

    #C0017
    ChrTalk(
        0x102,
        (
            "#00106F#5P……まさか《銀#2Rイン#》の正体が\x01",
            "リーシャさんだったなんて……\x02\x03",

            "#00108Fてっきり男の人とばかり\x01",
            "思っていたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x105,
        (
            "#10303F#6Pどうやら、あの格好の時には\x01",
            "気配を変えていたみたいだね。\x02\x03",

            "#10301Fひょっとしたら体型なんかも\x01",
            "変化させていたのかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(250)

    #C0019
    ChrTalk(
        0x109,
        (
            "#10111F#5Pそ、そんなこと\x01",
            "普通の人間にできるの？\x02\x03",

            "#10106F……って、普通じゃない人間に\x01",
            "最近何人も会ってるよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#00206F#6Pどうやら、わたしの感応力も\x01",
            "欺かれていたようですが……\x02\x03",

            "#00200Fロイドさんは、思った程には\x01",
            "驚いていませんでしたね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00003F#5P……ああ、そうだな。\x02\x03",

            "#00008Fちょっと前にリーシャと\x01",
            "話す機会があったんだけど……\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_25(0x1E3, 0x32)
    OP_25(0x7E, 0x14)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_25(0x1E3, 0x28)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "……小さい頃から……\x01",
            "そのために生きて来ました。\x02\x03",

            "気の遠くなるような昔から\x01",
            "祖先が受け継いできた道……\x02\x03",

            "今となっては何のために\x01",
            "歩んでるのか分からない道を。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    OP_25(0x1E3, 0x32)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Sleep(200)
    OP_25(0x1E3, 0x46)
    Sleep(100)

    #C0023
    ChrTalk(
        0x101,
        (
            "#00006F#5P──まさかとは思ったから\x01",
            "それ以上は考えなかったけど……\x02\x03",

            "#00001Fどこか彼女が《銀#2Rイン#》である可能性を\x01",
            "捨ててはいなかったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#00101F#5Pそんな事が……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(150)

    #C0025
    ChrTalk(
        0x104,
        (
            "#00306F#6P……考えてみりゃ、ただの素人が\x01",
            "アルカンシェルの準主役に\x01",
            "抜擢されるわけがねぇんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#00006F#5Pああ、あのイリアさんが\x01",
            "強引に誘って特訓したそうだから\x01",
            "妙な説得力があっただけだろう。\x02\x03",

            "#00008Fしかも《銀》が現れた時期と\x01",
            "リーシャがクロスベルに来た時期も\x01",
            "ちょうど一致するみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        (
            "#00201F#6P《黒月#4Rヘイユエ#》のツァオさんあたりは\x01",
            "正体を知っているんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x105,
        (
            "#10304F#6Pまあ、彼女の立場なら\x01",
            "秘密にしているのが普通だろうね。\x02\x03",

            "#10300F下手に素性なんか知られたら\x01",
            "良いように使われるだけだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#00108F#5P……そういう意味では\x01",
            "あまり正体を触れ回らない方が\x01",
            "いいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#00003F#5Pああ、課長はともかく、\x01",
            "しばらく様子を見てみよう。\x02\x03",

            "#00013Fそれに……今は《黒月》より\x01",
            "《赤い星座》の方が優先だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#00303F#6Pああ……\x02\x03",

            "#00301F──このタイミングで\x01",
            "叔父貴たちが姿を消すとしたら\x01",
            "準備をした上での行動だろう。\x02\x03",

            "多分、一気に動き始めるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#00001F#5Pそうか……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x109,
        (
            "#10101F#5P……ソーニャ司令の方にも\x01",
            "連絡する必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-180, 2150, 7610, 3500)
    MoveCamera(327, 164, 0, 3500)
    OP_6E(950, 3500)
    SetCameraDistance(13010, 3500)
    Sleep(1500)
    StopSound(126, 3000, 50)
    StopSound(483, 3000, 70)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM(-1, -1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x7E)
    OP_24(0x1E3)
    SetScenarioFlags(0x22, 0)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_96F end

    def Function_5_140C(): pass

    label("Function_5_140C")

    Sound(126, 2, 50, 0)
    Sound(483, 2, 20, 0)
    Sleep(400)
    OP_25(0x1E3, 0x1E)
    Sleep(400)
    OP_25(0x1E3, 0x28)
    Sleep(300)
    OP_25(0x1E3, 0x32)
    Sleep(300)
    OP_25(0x1E3, 0x3C)
    Sleep(300)
    OP_25(0x1E3, 0x46)
    Sleep(300)
    Return()

    # Function_5_140C end

    def Function_6_143F(): pass

    label("Function_6_143F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    LoadChrToIndex("chr/ch00302.itc", 0x1F)
    SoundLoad(483)
    SoundLoad(126)
    SoundLoad(803)
    SoundLoad(894)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    LoadEffect(0x0, "event\\ev315_00.eff")
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 800, 900, -100, 180)
    SetChrPos(0x102, -800, 900, 100, 180)
    SetChrPos(0x103, 100, 900, 1000, 180)
    SetChrPos(0x104, 0, 420, -1750, 180)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    SetChrPos(0x9, 0, 0, 0, 180)
    OP_D5(0x9, 0x0, 0x2BF20, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    SetChrPos(0xA, 0, 0, 0, 180)
    OP_D5(0xA, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x1, 0x5A)
    OP_71(0x1, 0x3E8, 0x7CF, 0x0, 0x20)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 700, 300, -100, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x104, 0, 0, 7)
    OP_F0(0x0, 0xA)
    OP_F0(0x1, 0x1F4)
    OP_68(0, 1800, -10000, 0)
    MoveCamera(25, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    BeginChrThread(0xB, 1, 0, 3)
    FadeToBright(1000, 0)
    OP_68(0, 1800, 40000, 9000)
    MoveCamera(155, 10, 0, 5000)
    SetCameraDistance(24000, 5000)
    Sleep(7000)
    OP_0D()
    Fade(1000)
    OP_68(-20, 1800, -110, 0)
    MoveCamera(126, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(18500, 2500)
    SetChrPos(0x104, 0, 420, -1450, 180)
    BeginChrThread(0x104, 1, 0, 8)
    OP_6F(0x79)
    OP_0D()

    #C0034
    ChrTalk(
        0x101,
        "#00001F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#00106F#6P何とか警察のボートを\x01",
            "確保できたのは良かったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#00203F#6P……どうやらミシュラムは\x01",
            "完全に封鎖されたそうですね。\x02\x03",

            "#00201Fテーマパークや各種ショップの\x01",
            "常駐スタッフも退去したとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#00306F#5P例の湿地帯に\x01",
            "向かった可能性もあったが……\x02\x03",

            "#00301Fこりゃ、間違いなく\x01",
            "ミシュラムが正解だろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00008F#5Pエリィ……\x01",
            "マリアベルさんとは\x01",
            "連絡が取れなかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#00106F#6P……ええ、ここ数日、\x01",
            "なかなか捕まらなくって。\x02\x03",

            "#00108FＩＢＣビル爆破の後始末で\x01",
            "忙しかったみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0040
    ChrTalk(
        0x104,
        (
            "#00303F#5Pあのお嬢さんはともかく……\x02\x03",

            "#00301Fレクターの野郎とキリカさんが\x01",
            "仄#2Rほの#めかしたアレは本当なのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#00206F#6Pクロスベル襲撃の真の黒幕が\x01",
            "エレボニア帝国ではなく……\x02\x03",

            "#00201Fディーター・クロイス市長……\x01",
            "いえ、大統領である可能性ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#00008F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    #C0043
    ChrTalk(
        0x102,
        (
            "#00106F#12P……ロイド。\x01",
            "私に気を遣う必要はないわ。\x02\x03",

            "#00108F昨日からおじいさまとの\x01",
            "連絡が取れていないのだけど……\x02\x03",

            "#00101F執事のヘルマーさんは\x01",
            "もしかしたらオルキスタワーに\x01",
            "拘束されたかもしれないって……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0044
    ChrTalk(
        0x101,
        "#00005F#5P……！？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#00208F#6P……それは……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x104,
        "#00306F#5P完全にクロじゃねぇか……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00006F#5P──ディーター市長が\x01",
            "一連の事件の黒幕……\x02\x03",

            "そう考えると、全ての辻褄#4Rつじつま#が\x01",
            "合ってくるのは確かだ。\x02\x03",

            "#00008Fその場合、《赤い星座》や《結社》は\x01",
            "彼の雇った実働部隊ないし協力者……\x02\x03",

            "#00013F魔人化したヴァルドや……\x01",
            "場合によっては《教団》すらも\x01",
            "利用されただけの可能性がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0048
    ChrTalk(
        0x102,
        "#00107F#12P《Ｄ∴Ｇ教団》も！？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#00305F#5Pヴァルドはともかく……\x01",
            "ヨアヒムまでもってことかよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        "#00208F#6Pそんな……でも……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#00003F#5P勿論、直接の繋がりが\x01",
            "あった可能性は低いだろう。\x02\x03",

            "ヨアヒムの言動から判断する限り、\x01",
            "他に黒幕がいた様子もない。\x02\x03",

            "#00001Fだが、彼自身が気付かない形で\x01",
            "利用されていた可能性はあり得る。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#00206F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#00108F#12Pそういえば、太陽の砦から\x01",
            "キーアちゃんを連れ去った人物も\x01",
            "判明していなかったわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#00303F#5Pそして《黒の競売会#10Rシュバルツオークション#》の出品物に\x01",
            "紛れ込ませたヤツか……\x02\x03",

            "#00301F考えてみりゃ、誰の仕業にしたって\x01",
            "“普通の人間”には無理な芸当だ。\x02\x03",

            "《銀#2Rイン#》や《結社》クラスの連中、\x01",
            "そうでなけりゃ──\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0055
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013Fはい……！\x01",
            "特務支援課、ロイドです！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("少年の声")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "よっしゃ、繋がったか！\x02\x03",

            "ティオにも聞かせたいから\x01",
            "スピーカーモードにしてくれよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0057
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fヨナか？\x01",
            "分かった、すぐに切り替える。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(804, 0, 100, 0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x101, 0x6)
    OP_0D()
    Sleep(300)

    #C0058
    ChrTalk(
        0x103,
        "#00201F#6Pヨナ、どうしたんですか？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2Sどうしたもこうしたもないって！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2Sクロスベルの導力ネットだけど……\x01",
            "とんでもない化物が潜んでるぞ！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x101,
        "#00011F#5P化物……？\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        "#00105F#12Pど、どういうこと？\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S最初はネットワークの周縁に\x01",
            "変なデータ構造体を見つけたんだ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S意味不明な配列だったから\x01",
            "単なるゴミかと思ってたけど……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2Sよくよく調べてみたら\x01",
            "例の《結社》が使っていたコードを\x01",
            "進化させたものが使われてたんだ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#00208F#6P《アストラルコード》……\x02\x03",

            "#00201Fつまり《結社》が仕掛けた\x01",
            "何らかのトラップですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2Sいや、日付を見る限り、\x01",
            "５年近く前からのものだ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S確か導力ネットが導入されたのも\x01",
            "そのあたりじゃなかったか！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        (
            "#00205F#6Pええ、確かに……\x02\x03",

            "#00201F……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#00103F#12P導力ネットの導入を\x01",
            "自治州政府に提案したのは\x01",
            "ＩＢＣグループ……\x02\x03",

            "#00108Fその結果、財団の技術が導入され\x01",
            "ＩＢＣも深く関わってきた……\x02\x03",

            "#00110Fそれこそネットワークの基幹部分を\x01",
            "知り尽くしているくらいに……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        "#00307F#5Pオイオイ、って事は……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0072
    ChrTalk(
        0x101,
        (
            "#00003F#5P──ヨナ。\x01",
            "その化物とは何なんだ？\x02\x03",

            "#00001Fそいつのせいで何が起きる？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2Sそ、それは解析中だけど……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2Sただ、導力ネットの\x01",
            "全領域を覆い尽くすような\x01",
            "巨大なシステムなのは確かだ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2Sしかもそれと連動するように\x01",
            "リアルなシステムも\x01",
            "用意されてるみたいだぜ！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x103,
        "#00201F#6Pリアルなシステム……？\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#00108F#12Pリアルということは\x01",
            "導力ネットの世界ではなく？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2Sああ、ジオフロントの全区画……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2Sそれとオルキスタワーを結んで\x01",
            "ミシュラム方面まで繋げる仕掛けが\x01",
            "構築されてるみたいだ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0080
    ChrTalk(
        0x101,
        "#00007F#5Pミシュラム……！？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        "#00310F#5Pその名前が出るかよ！？\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S──とにかく！\x01",
            "解析できたらまた連絡する！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S何してんのか知んねーけど\x01",
            "せいぜい気をつけろよな！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(813, 0, 70, 0)
    Sleep(200)
    Sound(894, 2, 80, 0)
    Sleep(100)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    StopSound(894, 2000, 70)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0084
    ChrTalk(
        0x104,
        (
            "#00306F#5P……おいおい。\x01",
            "繋がりすぎじゃねえか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x103,
        (
            "#00206F#6Pどんな目的のシステムかは\x01",
            "現時点では分かりませんが……\x02\x03",

            "#00208F財団や《結社》以外で\x01",
            "それだけの巨大なシステムを\x01",
            "構築できる人間がいるとすれば……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        "#00106F#12P#30W………………………………\x02",
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
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0087
    ChrTalk(
        0x101,
        (
            "#00006F#5P──今はこのまま\x01",
            "ミシュラムを目指そう。\x02\x03",

            "#00013Fキーアも、アリオスさんも……\x01",
            "全ての答えが待っているはずだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1800, -3000, 3000)

    def lambda_2B52():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B52)
    Sleep(50)

    def lambda_2B62():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2B62)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    Sleep(1000)
    EndChrThread(0x104, 0x1)
    Fade(1000)
    OP_68(0, 1800, -20000, 0)
    MoveCamera(180, 15, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(18500, 0)
    OP_68(0, 3800, 40000, 10000)
    MoveCamera(180, 0, 0, 7000)
    Sleep(5000)
    StopSound(126, 3000, 50)
    StopSound(483, 3000, 90)
    Sleep(2000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x8, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7565", "ed7561")
    ReplaceBGM("ed7160", "ed7561")
    OP_24(0x323)
    OP_24(0x37E)
    SetScenarioFlags(0x22, 1)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_143F end

    def Function_7_2C30(): pass

    label("Function_7_2C30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D2D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C89")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(333)
    Jump("loc_2D28")

    label("loc_2C89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD7")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_2D28")

    label("loc_2CD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D25")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(166)
    Jump("loc_2D28")

    label("loc_2D25")

    Sleep(233)

    label("loc_2D28")

    Jump("Function_7_2C30")

    label("loc_2D2D")

    Return()

    # Function_7_2C30 end

    def Function_8_2D2E(): pass

    label("Function_8_2D2E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D66")
    OP_82(0x0, 0xF, 0x1388, 0x3E8)
    Sleep(1000)
    OP_82(0x0, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("Function_8_2D2E")

    label("loc_2D66")

    Return()

    # Function_8_2D2E end

    SaveToFile()

Try(main)
