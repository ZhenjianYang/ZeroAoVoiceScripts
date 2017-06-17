from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4030.bin",                # FileName
        "t4030",                    # MapName
        "t4030",                    # Location
        0x0000,                     # MapIndex
        "ed7124",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "t4030",                  # 0
        "シスター・リース",       # 1
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(188, 0)                                        # 0

    ScpFunction((
        "Function_0_BC",           # 00, 0
        "Function_1_CF",           # 01, 1
        "Function_2_E5",           # 02, 2
    ))


    def Function_0_BC(): pass

    label("Function_0_BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_CE")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 2)

    label("loc_CE")

    Return()

    # Function_0_BC end

    def Function_1_CF(): pass

    label("Function_1_CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_E4")

    Return()

    # Function_1_CF end

    def Function_2_E5(): pass

    label("Function_2_E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch14000.itc", 0x1E)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis253.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis254.itp")
    OP_68(-1080, 3200, 2970, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23880, 0)
    SetChrPos(0x101, -1100, 0, 2650, 0)
    SetChrPos(0x102, -200, 0, 2350, 315)
    SetChrPos(0x103, -2400, 0, 2200, 45)
    SetChrPos(0x104, -950, 0, 750, 0)
    SetChrPos(0x109, -1750, 0, 1250, 0)
    SetChrPos(0x105, 200, 0, 1100, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1100, 0, 4000, 270)
    SetChrPos(0x8, -800, 0, 4030, 270)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちは\x01",
            "シスター・リースの個室に案内され……\x02\x03",

            "蒼い花を摘んだ経緯と\x01",
            "エラルダ大司教とのやり取りについて\x01",
            "彼女に一通り説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7573", 0)
    OP_68(-1080, 1200, 2970, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0002
    ChrTalk(
        0x8,
        (
            "#04406F#11P──なるほど。\x02\x03",

            "#04408F確かにこれは、大司教ならば\x01",
            "口を閉ざすのも無理ありませんね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
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

    #C0003
    ChrTalk(
        0x101,
        "#00005F#12Pえ……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93D")

    #C0004
    ChrTalk(
        0x104,
        "#00305F#12P分かるのかよ、シスターさん！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    #C0005
    ChrTalk(
        0x8,
        (
            "#04403F#5Pその前に……\x02\x03",

            "#04402F……エリィさん。\x01",
            "まだ私の身分について\x01",
            "説明していないみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        (
            "#00106F#11Pええ……\x01",
            "あまり言い回るのも\x01",
            "どうかと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "#04404F#5Pふふ……感謝します。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        "#10105F#12Pえっと……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        "#00201F#6Pその身分というのは一体……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0010
    ChrTalk(
        0x8,
        (
            "#04403F#5Pもう大司教には薄々、\x01",
            "勘付かれているようですが……\x02\x03",

            "私は教会内でも、\x01",
            "特殊な組織に所属しています。\x02\x03",

            "#04400F──『星杯騎士団』。\x01",
            "封聖省という機関に所属する\x01",
            "古代遺物#8Rアーティファクト#を回収する組織です。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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

    #C0011
    ChrTalk(
        0x101,
        "#00011F#12P星杯騎士団って……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x109,
        (
            "#10111F#12Pアルタイル・ロッジで\x01",
            "手を貸してくれた……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#04404F#5Pケビン・グラハムですね。\x02\x03",

            "#04402Fちなみに私は、彼をサポートする、\x01",
            "『従騎士』の位階にあります。\x02\x03",

            "#04406F本来ならば、様々な調査のため\x01",
            "彼自身がクロスベル入りをするのが\x01",
            "筋ではあったのですが……\x02\x03",

            "#04400F大司教の目があったので\x01",
            "代わりに私が情報収集役として\x01",
            "派遣されたというわけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00001F#12Pな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        "#00102F#11Pそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00306F#12Pなんつーか、教会ってのも\x01",
            "色々しがらみがあるみてぇだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#04403F#5Pええ、お恥ずかしながら。\x02\x03",

            "#04408F──話を戻しますが\x01",
            "皆さんが採取された花……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)
    Jump("loc_99B")

    label("loc_93D")


    #C0018
    ChrTalk(
        0x104,
        "#00305F#12P分かるのかよ、リースちゃん！？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "#04408F#11Pええ、皆さんが採取された花……\x02",
    )

    CloseMessageWindow()

    label("loc_99B")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #A0020
    AnonymousTalk(
        0x8,
        (
            "#04403F確かに、とある聖典に記されている\x01",
            "花である可能性は高そうです。\x02\x03",

            "#04401Fといっても正式な聖典ではなく\x01",
            "いわゆる“外典#4Rげてん#”にあたりますが。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0021
    AnonymousTalk(
        0x109,
        "#10105F外典……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0022
    AnonymousTalk(
        0x105,
        (
            "#10301Fつまり正式なものとは\x01",
            "認められていない異書って事だね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0023
    AnonymousTalk(
        0x8,
        (
            "#04403Fええ、教会内でも限られた者しか\x01",
            "閲覧は許されていません。\x02\x03",

            "#04400Fですが『騎士団』に所属する者は\x01",
            "そうした外典の閲覧を許されています。\x02\x03",

            "危険なアーティファクトの存在が\x01",
            "記されているものが多いからです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0024
    AnonymousTalk(
        0x101,
        "#00005Fなるほど……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0025
    ChrTalk(
        0x102,
        (
            "#00101F#11Pでは、その蒼い花は\x01",
            "一体どのように記されて……？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#04403F#11P外典の１つ『ラダー記』に\x01",
            "蒼き花についての描写があります。\x02\x03",

            "#04408F七耀脈の真上に咲く、\x01",
            "吉兆とも凶兆とも取れる神秘の花……\x02\x03",

            "#04401Fその名も『プレロマ草』の記述が。\x02",
        )
    )

    CloseMessageWindow()
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
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0027
    ChrTalk(
        0x101,
        "#00007F#4S#12Pな……！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        "#00107F#11Pその名前は……！\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    #A0029
    AnonymousTalk(
        0x109,
        "#10101Fそ、それって確か……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0030
    AnonymousTalk(
        0x105,
        (
            "#10305F『教団』の端末に残されてたっていう、\x01",
            "グノーシスの原料になった植物の名前かい？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0031
    AnonymousTalk(
        0x103,
        "#00206F………はい…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0032
    AnonymousTalk(
        0x104,
        (
            "#00301Fまさかこんな場所で\x01",
            "その名前を聞くとはな……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0033
    ChrTalk(
        0x8,
        (
            "#04403F#5P……なるほど、そうでしたか。\x02\x03",

            "#04401Fかの教団の残した謎については\x01",
            "教会でも殆んど解明されていません。\x02\x03",

            "エラルダ大司教の意向もあり、\x01",
            "ヨアヒム・ギュンターが起こした事件も\x01",
            "殆んど調査されませんでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x109,
        (
            "#10111F#12Pちょ、ちょっと待ってください。\x02\x03",

            "#10106Fその花が本当に\x01",
            "例のグノーシスという薬物の\x01",
            "原料だったとして……\x02\x03",

            "#10101Fそれが各地で発見されたことが\x01",
            "何を意味してるんでしょう……？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#00108F#11Pそ、そうね……\x01",
            "《幻獣》の出現も気になるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#00203F#6P七耀脈の真上に咲く花……\x02\x03",

            "#00201Fしかも吉兆とも凶兆とも\x01",
            "取れる花、ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        "#00306F#12Pああ、どうもイヤな符合だぜ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0038
    ChrTalk(
        0x101,
        (
            "#00003F#11P──とにかく、俺たちだけで\x01",
            "対処できる問題でも無さそうだ。\x02\x03",

            "いったん支援課に戻って\x01",
            "詳細な報告書をまとめてみよう。\x02\x03",

            "#00001Fリースさん。\x01",
            "教えていただいた情報は\x01",
            "警備隊やギルドに伝えても？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#04403F#5Pそうですね……\x02\x03",

            "#04400Fなるべく私の名前を\x01",
            "出さないで頂けるのであれば。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x105,
        (
            "#10302F#12Pフフ、大司教にとったら\x01",
            "スパイみたいな立場だろうからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#00100F#11Pもちろん、そのあたりは\x01",
            "極力配慮させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#04404F#5Pならば問題ありません。\x02\x03",

            "#04402F私の方も、騎士団に連絡してから\x01",
            "調査に入ってみるつもりです。\x02\x03",

            "お互い、何か進展があったら\x01",
            "情報交換するのは如何ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#00002F#12Pええ、喜んで。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        "#00202F#6Pよろしくお願いします。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちは支援課に戻ってから\x01",
            "幻獣と蒼き花──《プレロマ草》についての\x01",
            "詳細な報告書を大急ぎでまとめた。\x02\x03",

            "警備隊の司令部と、ギルドの受付に\x01",
            "導力ネットを通じて報告書を送った後……\x02\x03",

            "各地を回って疲れていたロイドたちは\x01",
            "課長やキーアと遅めの夕食をとってから\x01",
            "部屋に戻って早めに休むことにした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_32(0xFF, 0xFE, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("m0001", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E5 end

    SaveToFile()

Try(main)
