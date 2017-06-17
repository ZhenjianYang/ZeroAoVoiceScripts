from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1160.bin",                # FileName
        "c1160",                    # MapName
        "c1160",                    # Location
        0x0018,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 24, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1160",                  # 0
        "ピエール副局長",         # 1
    ))

    AddCharChip((
        "chr/ch06402.itc",                   # 00
        "chr/ch06400.itc",                   # 01
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(204, 0)                                        # 0

    ScpFunction((
        "Function_0_CC",           # 00, 0
        "Function_1_104",          # 01, 1
        "Function_2_161",          # 02, 2
        "Function_3_E85",          # 03, 3
        "Function_4_2928",         # 04, 4
    ))


    def Function_0_CC(): pass

    label("Function_0_CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E0")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_103")

    label("loc_E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F4")
    ClearScenarioFlags(0x22, 1)
    Event(0, 3)
    Jump("loc_103")

    label("loc_F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_103")
    ClearScenarioFlags(0x22, 2)
    Event(0, 4)

    label("loc_103")

    Return()

    # Function_0_CC end

    def Function_1_104(): pass

    label("Function_1_104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_137")
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_160")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_160")

    Return()

    # Function_1_104 end

    def Function_2_161(): pass

    label("Function_2_161")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(40930, 1200, -590, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24070, 0)
    SetChrPos(0x101, 40570, 0, -1240, 0)
    SetChrPos(0x102, 42040, 0, -1210, 0)
    SetChrPos(0x103, 40600, 0, -2730, 0)
    SetChrPos(0x104, 42020, 0, -2750, 0)
    SetChrPos(0x109, 40570, 0, -4150, 0)
    SetChrPos(0x105, 42000, 0, -4170, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(1500)

    #C0001
    ChrTalk(
        0x101,
        "#1P#N#00005F奥さんがホストと密会している……？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0002
    ChrTalk(
        0x8,
        "#3Pう、うむ……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#3P近頃、何度もそういったクラブに\x01",
            "足を運んでいるようでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "#3Pどうやら、どこぞのホストと\x01",
            "密会しているようなのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00101Fで、でも、それがホストとは\x01",
            "限らないんじゃないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x109,
        "#10101Fそうですよ、奥様を信じてあげた方が……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#3P決死の覚悟で目を盗んで\x01",
            "ワイフの鞄を調べて、\x01",
            "確かな証拠を見つけたんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "#3P彼女のスケジュール帳に\x01",
            "『クライド』とかいう男に会う約束が、\x01",
            "ビッシリと書かれていたのをね！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#3P主婦である彼女がそんな男に出会うなど、\x01",
            "ホストクラブ以外には\x01",
            "考えられないんじゃないのかねっ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0010
    ChrTalk(
        0x103,
        "#00206F（言い分は分かりますけど……）\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        "#00303F（まあ、必死なのは伝わってきたぜ。）\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x105,
        (
            "#10303F……ふむ、しかし……\x01",
            "ホストの『クライド』か。\x02\x03",

            "#10300F生憎だけど、そんな名前は\x01",
            "一度も聞いた事はないなあ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_678():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_678)
    Sleep(50)

    def lambda_688():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_688)
    Sleep(50)

    def lambda_698():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_698)
    Sleep(50)

    def lambda_6A8():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A8)
    Sleep(50)

    def lambda_6B8():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6B8)

    #C0013
    ChrTalk(
        0x8,
        "#3Pな、何……？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00005Fそうなのか？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x105,
        (
            "#10302Fま、歓楽街のクラブに在籍する\x01",
            "ホストの名前くらいは\x01",
            "一通り把握しているからね。\x02\x03",

            "新入りだから情報がないって\x01",
            "可能性もないわけじゃないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#3Pま、待ちたまえ。\x01",
            "やたら詳しいようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#3Pまさか、支援課に入った\x01",
            "現役ホストの臨時メンバー、\x01",
            "と噂されているのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x105,
        "#10309Fあ、それは僕だね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0019
    ChrTalk(
        0x8,
        "#3Pき、君ッ！！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#3P仮にも警察ともあろう者が、\x01",
            "ホストなどという\x01",
            "いかがわしい商売に……！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A8():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A8)

    #C0021
    ChrTalk(
        0x101,
        (
            "#00006Fま、まあまあ……\x01",
            "落ち着いてください。\x02\x03",

            "#00001Fとにかく今は、奥さんが\x01",
            "現在置かれている状況を\x01",
            "確かめることが先決です。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_936():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_936)
    Sleep(50)

    def lambda_946():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_946)
    Sleep(50)

    def lambda_956():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_956)
    Sleep(50)

    def lambda_966():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_966)

    #C0022
    ChrTalk(
        0x109,
        (
            "#10101Fで、ですよね……\x02\x03",

            "#10106Fワジ君については\x01",
            "この場で言っても\x01",
            "仕方ないとは思いますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x105,
        "#10304Fフフ、そういうことさ。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "#3Pぐっ……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#00100Fさっき、奥様の鞄を覗いたと\x01",
            "言っていましたけど……\x02\x03",

            "なにか捜査の\x01",
            "手がかりになるものは\x01",
            "ありませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        "#3Pう、うむ、そうだな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0027
    ChrTalk(
        0x8,
        "#3Pそ、そうだ、思い出したよ！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#3Pスケジュール帳を見たとき、\x01",
            "行き先のメモも書いてあったのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#3P最近は中央広場のレストランに\x01",
            "昼間から行っていることが\x01",
            "多いようだったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        (
            "#00203F中央広場のレストラン、\x01",
            "《ヴァンセット》ですか……\x02\x03",

            "#00200Fしかし、相手がホストなら\x01",
            "昼間から会ったりしているのは\x01",
            "おかしくありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x105,
        (
            "#10304F旦那が働いている時間帯に\x01",
            "目を盗んで逢引きを……\x01",
            "ってことかもしれないね。\x02\x03",

            "#10302Fフフ、ホストと客が\x01",
            "プライベートで会うときは、\x01",
            "昼の方が多いだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "#3Pや、やはりッ……！？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00006Fお、落ち着いてください。\x01",
            "……っていうか、ワジも煽るなよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x105,
        "#10304Fフフ、これは失敬。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00003Fコホン、とにかく\x01",
            "事情はわかりました。\x02\x03",

            "#00000F捜査はこちらに\x01",
            "任せていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "#3Pう、うむ。\x01",
            "すべて君達に任せよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#3Pなんとしても真相を\x01",
            "暴いてくれたまえっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#3Pただし、くれぐれも内密にだ。\x01",
            "……分かったね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#00006Fりょ、了解しました。\x01",
            "……それでは失礼します。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1150", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_2_161 end

    def Function_3_E85(): pass

    label("Function_3_E85")

    EventBegin(0x0)
    SoundLoad(812)
    FadeToDark(0, 0, -1)
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちは\x01",
            "夫人を尾行していたエリィたちと\x01",
            "連絡をとり合い……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ピエール副局長が待つ警察本部で、\x01",
            "情報を整理することになった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(40930, 1200, -590, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24070, 0)
    SetChrPos(0x101, 40570, 0, -1240, 0)
    SetChrPos(0x102, 42040, 0, -1210, 0)
    SetChrPos(0x103, 40600, 0, -2730, 0)
    SetChrPos(0x104, 42020, 0, -2750, 0)
    SetChrPos(0x109, 40570, 0, -4150, 0)
    SetChrPos(0x105, 42000, 0, -4170, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(1500)
    Sleep(10)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0042
    ChrTalk(
        0x8,
        (
            "#3Pそ、それで……\x01",
            "調査のほうはどうなったのかね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#3Pやはり、わたしのワイフは\x01",
            "ホストと密会して……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00003Fえっと、副局長……\x01",
            "落ち着いてください。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(50)

    #C0045
    ChrTalk(
        0x101,
        (
            "#00000Fその前に……エリィたち、\x01",
            "夫人の尾行はどうだった？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    #C0046
    ChrTalk(
        0x102,
        (
            "#00100Fええ、注意深く見ていたけど……\x01",
            "変わったことはしていなかったわ。\x02\x03",

            "住宅街方面にある、ご自宅に\x01",
            "お戻りになっていたみたい。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(50)

    #C0047
    ChrTalk(
        0x109,
        (
            "#10100F特に誰かに会った、ということも\x01",
            "ありませんでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        (
            "#00200Fこの後、《ノイエ＝ブラン》で\x01",
            "あのクライドという男と\x01",
            "待ち合わせているみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#3Pな、なんだとっ！？\x02",
    )

    CloseMessageWindow()

    def lambda_1260():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1260)
    Sleep(100)

    def lambda_1270():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1270)
    Sleep(100)

    #C0050
    ChrTalk(
        0x8,
        (
            "#3Pええい、私のワイフを\x01",
            "あんな如何わしい場所に連れ込んで\x01",
            "何をするつもりなのだねっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#3Pこ、こうなったら警官隊を編成して、\x01",
            "《ノイエ＝ブラン》ごと制圧を……！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00006Fだ、だから\x01",
            "落ち着いてくださいってば！\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00303Fあの連中相手じゃ、\x01",
            "返り討ちにあうのが関の山ッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#3Pだ、だからといって……\x01",
            "これが落ち着いていられるかね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#3Pこうしている間にも、\x01",
            "私のワイフがホストの毒牙に……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、その心配はないと思うよ。\x02\x03",

            "#10302F少なくとも、あのマダムが\x01",
            "『ホスト』の毒牙にかかる心配はね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0057
    ChrTalk(
        0x8,
        "#3Pど、どういうことだね……？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00003Fワジが最初から\x01",
            "言っていたことですが……\x02\x03",

            "#00001Fやはり、クライドという男は\x01",
            "ホストではないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        "#3Pな、なに……！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "#3Pだとしたら……\x01",
            "何者だというのかねっ！？\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1805")
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kクライドの正体は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【ホスト】\x01",            # 0
            "【詐欺師】\x01",            # 1
            "【セールスマン】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1665"),
        (1, "loc_1715"),
        (2, "loc_1795"),
        (SWITCH_DEFAULT, "loc_1800"),
    )


    label("loc_1665")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0062
    ChrTalk(
        0x101,
        (
            "#00006F（……って、たった今、\x01",
            "  自分でホストじゃないって\x01",
            "  言ったばかりじゃないか。）\x02\x03",

            "#00001F（冷静になって考えよう。\x01",
            "  あのクライドという男の正体は……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1800")

    label("loc_1715")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0063
    ChrTalk(
        0x101,
        (
            "#00003F（いや……厳密に言えば違う。）\x02\x03",

            "#00001F（冷静になって考えよう。\x01",
            "  あのクライドという男の正体は……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1800")

    label("loc_1795")


    #C0064
    ChrTalk(
        0x101,
        (
            "#00001Fクライドという男の正体、\x01",
            "それはおそらく……\x01",
            "『セールスマン』です。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FB")
    OP_2C(0x84, 0x1)

    label("loc_17FB")

    Jump("loc_1800")

    label("loc_1800")

    Jump("loc_15D5")

    label("loc_1805")


    #C0065
    ChrTalk(
        0x109,
        "#10105Fセールスマン、ですか？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#00300F確かに、あの丁寧な喋りは\x01",
            "ホストっていうより\x01",
            "商売人って感じはしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、でもそれは明らかに\x01",
            "ホストじゃないと言える証拠でもある。\x02\x03",

            "#10302F僕たちは寂しいマダムたちに\x01",
            "一時の夢を見せてあげるための存在……\x02\x03",

            "一流のホストなら、\x01",
            "丁寧にエスコートする事はあっても\x01",
            "必要以上にへりくだることはしないさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0068
    ChrTalk(
        0x101,
        (
            "#00006Fワジにしてみれば\x01",
            "そういう観点もあるだろうけど……\x01",
            "まあ、似たような推測です。\x02\x03",

            "#00001Fクライドという男と奥さんは、\x01",
            "『密会しているホストと客』には\x01",
            "どうしても見えませんでした。\x02\x03",

            "どちらかといえば、\x01",
            "『商売人』と『その客』……\x01",
            "その方がしっくり来る印象です。\x02\x03",

            "何度も会っていたのも、\x01",
            "なんらかの取引きをするための\x01",
            "交渉だと考えるのが自然でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "#3Pし、しかし仮にそうだとして……\x01",
            "ワイフは一体何を買わされようと\x01",
            "しているのかね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00003Fそれも、クライドという男が\x01",
            "どこに所属するセールスマンかを\x01",
            "推理すれば分かります。\x02\x03",

            "#00001Fあの男は、おそらく……\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E00")
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kクライドはどこのセールスマン？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【宝石店】\x01",          # 0
            "【不動産業者】\x01",      # 1
            "【証券会社】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C5E"),
        (1, "loc_1CF7"),
        (2, "loc_1D62"),
        (SWITCH_DEFAULT, "loc_1DFB"),
    )


    label("loc_1C5E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0072
    ChrTalk(
        0x101,
        (
            "#00003F（いや……それは考えにくい。）\x02\x03",

            "#00001F（レストランでの会話、\x01",
            "  そして尾行した先での光景……\x01",
            "  それらを総合的に考えれば……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DFB")

    label("loc_1CF7")


    #C0073
    ChrTalk(
        0x101,
        (
            "#00001Fおそらく……\x01",
            "不動産を取り扱うセールスマン\x01",
            "ではないかと思われます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D5D")
    OP_2C(0x84, 0x1)

    label("loc_1D5D")

    Jump("loc_1DFB")

    label("loc_1D62")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0074
    ChrTalk(
        0x101,
        (
            "#00003F（いや……それは考えにくい。）\x02\x03",

            "#00001F（レストランでの会話、\x01",
            "  そして尾行した先での光景……\x01",
            "  それらを総合的に考えれば……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DFB")

    label("loc_1DFB")

    Jump("loc_1BC2")

    label("loc_1E00")

    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    #C0075
    ChrTalk(
        0x102,
        (
            "#00103F不動産……\x02\x03",

            "#00100Fそういえば、レストランの会話では\x01",
            "ミシュラムの話題が出ていたわね。\x02\x03",

            "最初は旅行の話かと思ったけど、\x01",
            "話に出た『パンフレット』というのは……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    #C0076
    ChrTalk(
        0x101,
        (
            "#00000F多分、ミシュラムの高級別荘地にある\x01",
            "住宅情報のパンフレットだろう。\x02\x03",

            "そして、港湾区まで尾行した先で、\x01",
            "クライドという男はスーツ姿の男から\x01",
            "何かを受け取っていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x105,
        (
            "#10304F口ぶりからすれば、\x01",
            "あのスーツの男はクライドの上司だろう。\x02\x03",

            "#10300Fおそらく契約書などの重要な書類を\x01",
            "受け取っていたんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(50)
    TurnDirection(0x102, 0x8, 500)
    Sleep(100)

    #C0078
    ChrTalk(
        0x101,
        (
            "#00000Fクライドという男は\x01",
            "不動産屋のサラリーマンで、\x01",
            "夫人に物件を売る交渉をしていた。\x02\x03",

            "夫人もそれを好意的に受け、\x01",
            "ミシュラムへの下見などにも行って\x01",
            "順調に交渉を進めていた。\x02\x03",

            "夫人があの男と会っていたのは、\x01",
            "そのためだと考えると自然です。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        (
            "#00302Fなるほど……\x01",
            "つじつまは合いそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x105,
        (
            "#10302Fそして、今日の交渉で\x01",
            "話は大方まとまり……\x02\x03",

            "もうすぐ《ノイエ＝ブラン》で\x01",
            "最後の交渉が行われるわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        "#3Pふ、ふむ、なるほど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0082
    ChrTalk(
        0x8,
        "#3Pい、いや、待ってくれたまえ！\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "#3Pマーガレットは、私に黙って\x01",
            "ミシュラムの物件を買おうとしている。\x01",
            "……そういうことかね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "#3Pだ、だが……そんな資産は\x01",
            "我が家には全くないぞ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "#3P一体どうやってそんなミラを\x01",
            "工面するつもりだというのだね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        (
            "#10108Fも、もしかして……\x01",
            "借金とかでしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x103,
        (
            "#00203F……十分考えられそうですね。\x02\x03",

            "#00200F無理なローンを組ませるよう\x01",
            "誘導したのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        "#3Pそ、そんな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_0D()
    Fade(500)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sound(812, 0, 100, 0)
    SetChrPos(0x8, 42100, 0, 1700, 90)
    OP_0D()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    #C0089
    ChrTalk(
        0x8,
        (
            "#3Pき、決めたぞ……私はやはり、\x01",
            "《ノイエ＝ブラン》に乗り込むっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "#3Pここまで聞かされて、\x01",
            "ワイフがみすみす騙されるのを\x01",
            "見過ごすわけにはいかん！！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "#3Pそこでクライドとかいう若造を一喝し、\x01",
            "ワイフの頬をはたいてでも連れ帰る！！\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#00205F（……恐妻家が大きく出ましたね。）\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#00006F（というか、ヘンなスイッチを\x01",
            "  入れちゃった気がするな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、せっかくだし\x01",
            "手伝ってあげるとしようよ。\x02\x03",

            "#10309Fこのまま放っておいて、\x01",
            "１人で《ノイエ＝ブラン》に\x01",
            "突入されても困るだろうし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_2651():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2651)
    Sleep(50)

    def lambda_2661():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2661)
    Sleep(50)

    def lambda_2671():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2671)
    Sleep(50)

    def lambda_2681():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2681)
    Sleep(50)

    def lambda_2691():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2691)

    #C0095
    ChrTalk(
        0x101,
        (
            "#00006Fそれは確かに言えてるかも\x01",
            "しれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x109,
        (
            "#10106F……ワジ君、なんだか\x01",
            "ますます楽しんでない？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x105,
        "#10304Fフフ、何のことやら。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#00108Fまあでも、ブレーキになれるのは\x01",
            "私たちだけみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#00306Fしゃあねえ、気は進まねえが\x01",
            "《ノイエ＝ブラン》には\x01",
            "俺から話をつけてみるか。\x02\x03",

            "#00300F多分、ザックスって顔なじみが\x01",
            "番犬をやってるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "#3Pええい、なにをゴチャゴチャ\x01",
            "話し合っているのかね！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2840():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2840)
    Sleep(50)

    def lambda_2850():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2850)
    Sleep(50)

    def lambda_2860():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2860)
    Sleep(50)

    def lambda_2870():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2870)
    Sleep(50)

    def lambda_2880():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2880)

    #C0101
    ChrTalk(
        0x8,
        (
            "#3Pさあ、すぐにでも\x01",
            "《ノイエ＝ブラン》へ行くぞ！！\x01",
            "君たちもついてきたまえ！\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#00005Fりょ、了解しました……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c0490", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_E85 end

    def Function_4_2928(): pass

    label("Function_4_2928")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(40930, 1200, -590, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24070, 0)
    SetChrPos(0x101, 40570, 0, -1240, 0)
    SetChrPos(0x102, 42040, 0, -1210, 0)
    SetChrPos(0x103, 40600, 0, -2730, 0)
    SetChrPos(0x104, 42020, 0, -2750, 0)
    SetChrPos(0x109, 40570, 0, -4150, 0)
    SetChrPos(0x105, 42000, 0, -4170, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0103
    ChrTalk(
        0x8,
        (
            "#3P……コホン。\x01",
            "ひとまずご苦労だった、\x01",
            "特務支援課の諸君。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        (
            "#00102F私たちも顛末を聞いて、\x01",
            "ひとまず安心しました。\x02\x03",

            "奥様が騙されていたわけじゃなくて\x01",
            "本当によかったですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#3Pま、まあ、結局別荘は\x01",
            "購入することになって\x01",
            "しまいそうだがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "#3Pただ、別居の話は無くなったから、\x01",
            "おそらく週末あたりに\x01",
            "夫婦で使う事になるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x109,
        (
            "#10100Fあはは……\x01",
            "奥さんも別荘をかなり\x01",
            "気に入っていたみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#00309Fま、その程度は\x01",
            "大目にみてやっても\x01",
            "いいんじゃないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、もともと購入資金も\x01",
            "奥さんが株で稼いだって話だし。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "#3Pう、うむ……\x01",
            "その点も頭が痛い話なのだがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "#3Pはあ、今回の件でますます\x01",
            "頭が上がらなくなってしまった……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0112
    ChrTalk(
        0x103,
        "#00211F（……割と自業自得かと。）\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "#3Pまあ、なにはともあれ……\x01",
            "離婚という最悪の事態は\x01",
            "免れることができた。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "#3Pここは素直に\x01",
            "礼を言わせてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00002Fはは、また何かありましたら\x01",
            "いつでもご相談ください。\x02\x03",

            "#00004F……それでは失礼します。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【副局長の依頼】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x84, 0x1, 0x1)
    OP_29(0x84, 0x1, 0x2)
    OP_29(0x84, 0x4, 0x10)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    SetScenarioFlags(0x22, 4)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_2928 end

    SaveToFile()

Try(main)
