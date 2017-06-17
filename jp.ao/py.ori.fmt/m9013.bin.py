from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9013.bin",                # FileName
        "m9013",                    # MapName
        "m9013",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 100000, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9013",                  # 0
        "ガイ",                   # 1
        "SE制御",                 # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_124",          # 01, 1
        "Function_2_129",          # 02, 2
        "Function_3_2AA9",         # 03, 3
        "Function_4_2ABC",         # 04, 4
        "Function_5_2B03",         # 05, 5
        "Function_6_2B27",         # 06, 6
        "Function_7_2B4B",         # 07, 7
        "Function_8_2BE4",         # 08, 8
        "Function_9_2C05",         # 09, 9
        "Function_10_2C30",        # 0A, 10
        "Function_11_2C97",        # 0B, 11
        "Function_12_2CC8",        # 0C, 12
        "Function_13_2CF3",        # 0D, 13
        "Function_14_2D14",        # 0E, 14
        "Function_15_2D3F",        # 0F, 15
        "Function_16_2D63",        # 10, 16
        "Function_17_2D9F",        # 11, 17
    ))


    def Function_0_114(): pass

    label("Function_0_114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_123")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_123")

    Return()

    # Function_0_114 end

    def Function_1_124(): pass

    label("Function_1_124")

    OP_F0(0x1, 0x320)
    Return()

    # Function_1_124 end

    def Function_2_129(): pass

    label("Function_2_129")

    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    Call(0, 17)
    LoadChrToIndex("chr/ch12100.itc", 0x1E)
    LoadChrToIndex("apl/ch51751.itc", 0x1F)
    SoundLoad(111)
    SoundLoad(125)
    SoundLoad(109)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07801.itp")
    OP_68(0, 2500, 0, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27000, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    SetChrPos(0x101, 0, -750, 750, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -750, -2750, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(111, 2, 80, 0)
    Sound(125, 2, 40, 0)
    Sound(109, 2, 30, 0)
    OP_68(40000, 150, -50000, 0)
    MoveCamera(306, 14, 8, 0)
    OP_6E(700, 0)
    SetCameraDistance(35000, 0)
    OP_68(-20000, 150, 25000, 16000)
    MoveCamera(306, 14, 6, 16000)
    OP_6E(700, 16000)
    SetCameraDistance(35000, 16000)
    PlaceName2(340, 200, "c_plac63", 0x0, 6000)
    FadeToBright(3000, 16777215)
    Sleep(15600)
    Fade(500)
    OP_68(0, 750, 250, 0)
    MoveCamera(210, 8, -5, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_68(0, 750, 750, 7500)
    MoveCamera(135, 14, 5, 7500)
    OP_6E(700, 7500)
    SetCameraDistance(18500, 7500)
    OP_6F(0x79)
    SetCameraDistance(13600, 100000)
    Sleep(500)

    #C0001
    ChrTalk(
        0x101,
        (
            "#00005F#11P#30Wここは……\x02\x03",

            "#00008F……みんなは……\x01",
            "キーアはどこに行ったんだ？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_93(0x101, 0x59, 0x190)
    Sleep(800)
    OP_93(0x101, 0x10F, 0x190)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0002
    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W……どう考えても\x01",
            "普通の場所じゃなさそうだ。\x02\x03",

            "#00008F無闇に動き回るわけにも\x01",
            "行かなさそうだけど……\x02\x03",

            "#00003F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    MoveCamera(135, 14, 4, 2000)
    SetCameraDistance(13600, 10000)
    Sleep(200)
    OP_93(0x101, 0x0, 0x190)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    #C0003
    ChrTalk(
        0x101,
        (
            "#00003F#11P#30W……どうしてだろう。\x01",
            "こんなに何もない場所なのに……\x02\x03",

            "#00000Fなぜか……不安や恐れは\x01",
            "不思議なほど感じない……\x02\x03",

            "#00008F……いったいこの場所は……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 10, -1, -1)
    SetChrName("声")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            "#3C──どんな状況でも\x01",
            "慌てずに踏みとどまって\x01",
            "現場の把握に努める……\x02\x03",

            "だいぶ捜査官として\x01",
            "板に付いてきたじゃないか。\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(223, 0, 50, 0)
    Sound(920, 0, 50, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 750, 0, 1500)
    MoveCamera(135, 14, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(13600, 1500)

    def lambda_60B():
        OP_95(0xFE, 0, -750, -1400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_60B)

    def lambda_625():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_625)

    def lambda_636():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_636)
    OP_6F(0x79)
    CancelBlur(0)
    SetCameraDistance(13000, 3000)
    Sleep(500)

    #C0005
    ChrTalk(
        0x101,
        "#00005F#6P#30W────────────\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)

    #N0006
    NpcTalk(
        0x8,
        "？？？",
        "#11P#30Wなんだ、どうしたロイド？\x02",
    )

    CloseMessageWindow()

    #N0007
    NpcTalk(
        0x8,
        "？？？",
        (
            "#11P#30W久しぶりの再会に\x01",
            "口も利けないくらい驚いたのか？\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7534", 0)
    SetCameraDistance(11000, 100000)
    Sleep(500)
    BeginChrThread(0x9, 1, 0, 16)

    #C0008
    ChrTalk(
        0x101,
        (
            "#00011F#6P#40Wあ、兄貴……\x02\x03",

            "#00002F兄貴なの……か……？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0009
    AnonymousTalk(
        0x8,
        (
            "#30W#0Cハハ、“兄貴”だなんて\x01",
            "カッコ付けてんじゃねえっての。\x02\x03",

            "前みたいに“兄ちゃん”って\x01",
            "呼べばいいだろうが？\x02\x03",

            "２人しかいないんだから\x01",
            "遠慮なく甘えていいんだぜ？\x02",
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

    #C0010
    ChrTalk(
        0x101,
        (
            "#00006F#6P#30W……～～～～っ……\x01",
            "放っておいてくれよっ！\x02\x03",

            "#00002Fでも、その減らず口……\x01",
            "間違いなく兄貴みたいだな……\x02\x03",

            "夢でもないみたいだし……\x01",
            "一体どういうことなんだ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wああ、どうやらここは\x01",
            "あの子の内面の一部らしいな。\x02\x03",

            "#07808Fあらゆる可能性を内包しつつ、\x01",
            "世界を再構成できる“零”の世界……\x02\x03",

            "#07800Fどうやらそんな場所らしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00005F#6P#30W“零”の世界……\x02\x03",

            "#00013F兄ちゃんが……\x01",
            "……兄貴が現れているのも\x01",
            "関係があるのか？\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 5)
    WaitChrThread(0x8, 1)

    #C0013
    ChrTalk(
        0x8,
        (
            "#07803F#11P#30Wああ、恐らくあの子は、\x01",
            "過去の時空間に干渉することで\x01",
            "俺という存在を識#2Rし#ったんだろう。\x02\x03",

            "#07808Fそしてお前やセシル……\x01",
            "アリオスやティオたちのためにも\x01",
            "俺を甦らせようとしたのかもしれん。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x101,
        "#00011F#6P#30W兄貴を……甦らせる！？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 6)
    WaitChrThread(0x8, 1)

    #C0015
    ChrTalk(
        0x8,
        (
            "#07800F#11P#30Wまあ正確には、今の世界を\x01",
            "『俺が死ななかった世界』に\x01",
            "紡ぎ直すって事だろうけどな。\x02\x03",

            "#07802F──どうだロイド？\x02\x03",

            "#07809Fお兄様が戻って来たら嬉しいか？\x01",
            "それともウザったいか？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00002F#6P#40W…………はは……………\x02\x03",

            "#00004Fそんなの……嬉しいに\x01",
            "……決まってるだろう……？\x02\x03",

            "#00008F………でも………それは…………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0017
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W──俺が死んだ後の時間を、\x01",
            "そこで頑張ってきた人々の努力を\x01",
            "否定することにもなる……\x02\x03",

            "#07810Fまあ、当然そうなるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#00008F#6P#40W………………………………………\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "#07803F#11P#30W《特務支援課》だったか……\x02\x03",

            "#07802F俺も参加して、お前らと一緒に\x01",
            "色んな事件を解決している世界も\x01",
            "あり得たのかもしれねぇが……\x02\x03",

            "#07804Fそれは今のお前らの世界じゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00002F#6P#40W…………ああ………………\x02\x03",

            "#00006F本当にそんな世界があったら、\x01",
            "どんなに楽しくて、嬉しくて……\x01",
            "……幸せだろうと思うけど……\x02\x03",

            "#00008F#50W……それでも……僕は………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    def lambda_EE1():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EE1)
    WaitChrThread(0x101, 2)
    Sleep(750)

    #C0021
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wああ──それでいい。\x02\x03",

            "#07800Fお前がそう言えるようになったのを\x01",
            "俺は誇りに思うぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 750, 500, 1500)
    MoveCamera(135, 14, 3, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(11000, 1500)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1000)
    OP_9B(0x1, 0x8, 0x0, 0x60E, 0x3E8, 0x0)
    OP_6F(0x79)
    BeginChrThread(0x8, 1, 0, 7)
    WaitChrThread(0x8, 1)
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 8)
    WaitChrThread(0x8, 1)
    Sleep(300)

    #C0022
    ChrTalk(
        0x8,
        (
            "#07809F#11P#40W本当に……あの甘えん坊が\x01",
            "よくここまでデカくなったもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00015F#6P#50Wに、兄ちゃんなんかに\x01",
            "甘えた記憶はないっての……\x02\x03",

            "#00008F……セシル姉にならともかく……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "#07804F#11P#40Wはは……そうだったな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    #C0025
    ChrTalk(
        0x8,
        (
            "#07803F#11P#30W……セシルも自分のために\x01",
            "歩き始めてもいい頃合いだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(120)
    SetChrSubChip(0x8, 0x10)
    Sleep(120)
    SetChrSubChip(0x8, 0x9)
    Sleep(300)

    #C0026
    ChrTalk(
        0x8,
        (
            "#07802F#11P#30W何だったらお前、思い切って\x01",
            "アタックしてみたらどうだ？\x02\x03",

            "#07809F天然ボケだから、なかなか\x01",
            "気付いてくれなさそうだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#00006F#6P#30Wうるさい……\x01",
            "セシル姉を馬鹿にするな。\x02\x03",

            "#00013F兄ちゃんなんかには勿体ない、\x01",
            "最高の女性なんだからな……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1499")

    #C0028
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wハハ、違いない。\x02\x03",

            "#07800Fまあお前も、自分の相手は\x01",
            "ちゃんと見つけたみてぇだから\x01",
            "余計なお世話ってもんか。\x02\x03",

            "#07809Fエリィって言ったか？\x01",
            "お前には勿体ないような\x01",
            "才色兼備のいい子じゃないか。\x02\x03",

            "#07802Fお嬢様なのに芯が通ってて\x01",
            "行動力も包容力もあるみてぇだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#00002F#6P#30Wはは……俺もそう思うよ。\x02\x03",

            "#00006Fできれば兄貴にも……\x01",
            "エリィに会って欲しかった。\x02\x03",

            "#00008Fそれにティオやランディにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wティオか……色々あったみてぇだが\x01",
            "いい子に育ってくれて何よりだぜ。\x02\x03",

            "#07800Fランディってのも馬鹿っぽくて\x01",
            "なかなか楽しそうなヤツみてぇだし。\x02\x03",

            "#07809Fいい仲間に恵まれたみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2521")

    label("loc_1499")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C2")

    #C0031
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wハハ、違いない。\x02\x03",

            "#07800Fまあお前も、自分の相手は\x01",
            "ちゃんと見つけたみてぇだから\x01",
            "余計なお世話ってもんか。\x02\x03",

            "#07809Fまさかお前とティオが\x01",
            "くっつくとは思わなかったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00011F#6P#30Wべ、別にそういう\x01",
            "関係ってわけじゃないけど……\x02\x03",

            "#00004Fでも、見守ってあげたい、\x01",
            "大切な子であるのは間違いないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wそうか……すごく良い顔で\x01",
            "笑うようになったみたいだし。\x02\x03",

            "#07802Fま、将来有望なのは間違いないから\x01",
            "ちゃんと繋ぎ止めておくんだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#00002F#6P#30Wはは……先走りすぎだって。\x02\x03",

            "#00006F……できれば兄貴にも\x01",
            "ティオに会って欲しかった。\x02\x03",

            "#00008Fそれにエリィやランディにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wエリィってのは、才色兼備で\x01",
            "行動力もあるお嬢様だったか。\x02\x03",

            "#07800Fランディってのも馬鹿っぽくて\x01",
            "なかなか楽しそうなヤツみてぇだし。\x02\x03",

            "#07809Fいい仲間に恵まれたみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2521")

    label("loc_17C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6D")

    #C0036
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wハハ、違いない。\x02\x03",

            "#07800Fまあお前も、自分の相手は\x01",
            "ちゃんと見つけたみてぇだから\x01",
            "余計なお世話ってもんか。\x02\x03",

            "#07809Fノエルって言ったか？\x01",
            "お前には勿体ないような\x01",
            "真っ直ぐでいい子じゃないか。\x02\x03",

            "#07802F一本気なところも\x01",
            "お前に合ってるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#00002F#6P#30Wはは……俺もそう思うよ。\x02\x03",

            "#00006Fできれば兄貴にも……\x01",
            "ノエルに会って欲しかった。\x02\x03",

            "#00008Fエリィやランディ、\x01",
            "それに勿論ティオにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wティオか……色々あったみてぇだが\x01",
            "いい子に育ってくれて何よりだぜ。\x02\x03",

            "#07800Fエリィってのは、才色兼備で\x01",
            "行動力もあるお嬢様だったか。\x02\x03",

            "ランディってのも馬鹿っぽくて\x01",
            "なかなか楽しそうなヤツみてぇだし。\x02\x03",

            "#07809Fいい仲間に恵まれたみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2521")

    label("loc_1A6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D57")

    #C0039
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wハハ、違いない。\x02\x03",

            "#07800Fまあお前も、自分の相手は\x01",
            "ちゃんと見つけたみてぇだから\x01",
            "余計なお世話ってもんか。\x02\x03",

            "#07809F──リーシャって言ったか？\x02\x03",

            "#07802F色々抱えてるみてぇだが、\x01",
            "お前には勿体ないような\x01",
            "健気でいい子じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00011F#6P#30Wべ、別にそういう\x01",
            "関係ってわけじゃないけど……\x02\x03",

            "#00004Fでも……見守ってあげたい\x01",
            "存在であるのは間違いないかな。\x02\x03",

            "#00008Fできれば兄貴にも……\x01",
            "リーシャに会って欲しかった。\x02\x03",

            "エリィやランディ、\x01",
            "それに勿論ティオにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wティオか……色々あったみてぇだが\x01",
            "いい子に育ってくれて何よりだぜ。\x02\x03",

            "#07800Fエリィってのは、才色兼備で\x01",
            "行動力もあるお嬢様だったか。\x02\x03",

            "ランディってのも馬鹿っぽくて\x01",
            "なかなか楽しそうなヤツみてぇだし。\x02\x03",

            "#07809Fいい仲間に恵まれたみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2521")

    label("loc_1D57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2005")

    #C0042
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wハハ、違いない。\x02\x03",

            "#07802Fまあお前も、自分の相手は\x01",
            "ちゃんと見つけておけよ？\x02\x03",

            "相棒同士でつるむのが\x01",
            "楽しいってのも分かるけどよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#00005F#6P#30Wああ、ランディの事か？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wなかなか馬鹿っぽくて、\x01",
            "芯の通ったヤツみてえだな。\x02\x03",

            "#07800F真面目なお前とは\x01",
            "息も合ってるみてぇだし……\x02\x03",

            "#07809Fいい相棒みたいじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30Wああ……俺もそう思うよ。\x02\x03",

            "#00008Fできれば兄貴にも……\x01",
            "ランディに会って欲しかった。\x02\x03",

            "それにティオやエリィにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wティオか……色々あったみてぇだが\x01",
            "いい子に育ってくれて何よりだぜ。\x02\x03",

            "#07800Fエリィってのは、才色兼備で\x01",
            "行動力もあるお嬢様だったか。\x02\x03",

            "#07809Fいい仲間に恵まれたみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2521")

    label("loc_2005")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22F9")

    #C0047
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wハハ、違いない。\x02\x03",

            "#07802Fまあお前も、自分の相手は\x01",
            "ちゃんと見つけておけよ？\x02\x03",

            "野郎同士でつるむのが\x01",
            "楽しいってのも分かるけどよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00005F#6P#30Wああ、ワジの事か？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wミステリアスなヤツだが\x01",
            "信頼はできるみてぇだな。\x02\x03",

            "#07800F真面目なお前とも\x01",
            "逆に合ってるみてぇだし……\x02\x03",

            "#07809Fこれも何かの縁ってやつか。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30Wああ……俺もそう思うよ。\x02\x03",

            "#00008Fできれば兄貴にも……\x01",
            "ワジに会って欲しかった。\x02\x03",

            "エリィやランディ、\x01",
            "それに勿論ティオにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wティオか……色々あったみてぇだが\x01",
            "いい子に育ってくれて何よりだぜ。\x02\x03",

            "#07800Fエリィってのは、才色兼備で\x01",
            "行動力もあるお嬢様だったか。\x02\x03",

            "ランディってのも馬鹿っぽくて\x01",
            "なかなか楽しそうなヤツみてぇだし。\x02\x03",

            "#07809Fいい仲間に恵まれたみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2521")

    label("loc_22F9")


    #C0052
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wハハ、違いない。\x02\x03",

            "#07803Fまあお前も、自分の相手は\x01",
            "ちゃんと見つけておけよ？\x02\x03",

            "#07802F仲間同士でつるむのが\x01",
            "楽しいってのも分かるけどよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00012F#6P#30Wはは……否定できないな。\x02\x03",

            "#00008Fできれば兄貴にも……\x01",
            "みんなに会って欲しかった。\x02\x03",

            "エリィやランディ、\x01",
            "それに勿論ティオにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wティオか……色々あったみてぇだが\x01",
            "いい子に育ってくれて何よりだぜ。\x02\x03",

            "#07800Fエリィってのは、才色兼備で\x01",
            "行動力もあるお嬢様だったか。\x02\x03",

            "ランディってのも馬鹿っぽくて\x01",
            "なかなか楽しそうなヤツみてぇだし。\x02\x03",

            "#07809Fいい仲間に恵まれたみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2521")


    #C0055
    ChrTalk(
        0x101,
        "#00002F#6P#30Wああ……最高の仲間たちさ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 11)
    BeginChrThread(0x101, 1, 0, 12)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x1000)
    SetChrSubChip(0x101, 0xE)
    BeginChrThread(0x101, 0, 0, 3)
    OP_68(0, 750, 800, 1500)
    MoveCamera(135, 14, 3, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(12000, 1500)
    WaitChrThread(0x101, 0)
    OP_6F(0x79)

    #C0056
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W……兄貴、そろそろ行くよ。\x02\x03",

            "大切なものを取り戻して\x01",
            "みんなの所に帰るためにも。\x02\x03",

            "#00000Fまた……いつか会えるよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30Wああ、もちろんだ。\x02\x03",

            "#07810F俺はお前たちの近くにいる。\x02\x03",

            "泣きたくなったら、甘えたくなったら\x01",
            "いつでも呼んでくれりゃあいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00012F#6P#30Wはは……分かった。\x02\x03",

            "#00002Fでも、どんなに苦しくても\x01",
            "《壁》は乗り越えられると思う。\x02\x03",

            "#00004Fみんながいて、その向こうにある\x01",
            "明日を掴むためだったら……\x02\x03",

            "#00000F──だから大丈夫。\x01",
            "安心して見守っていてくれよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#07809F#11P#30Wハハ、生意気言いやがって。\x02\x03",

            "#07804F──今のお前なら、あの子を\x01",
            "本当の意味で見付けられるはずだ。\x02\x03",

            "#07800F#30W#11P殻の中に閉じこもったお姫様を\x01",
            "見つけ出して抱きしめてやれ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0060
    ChrTalk(
        0x101,
        (
            "#00000F#6P#30W#4Sああ……！\x02\x03",

            "#00014F#3Sさよなら───兄貴！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(480, 350, 5260, 3500)
    MoveCamera(34, 8, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(13230, 3500)
    BeginChrThread(0x101, 0, 0, 4)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 350, 400, 0)
    MoveCamera(135, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(10500, 3000)
    Sleep(1500)
    BeginChrThread(0x8, 1, 0, 13)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    SetCameraDistance(10000, 15000)

    #C0061
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W……そう、生きている限り、\x01",
            "《壁》はいつだって現れるもんだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    BeginChrThread(0x8, 1, 0, 14)
    WaitChrThread(0x8, 1)
    Sleep(200)

    #C0062
    ChrTalk(
        0x8,
        (
            "#07810F#11P#30W大切なのは、乗り越える意志と\x01",
            "その先にどんな光を見出すか……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 15)
    WaitChrThread(0x8, 1)

    #C0063
    ChrTalk(
        0x8,
        "#07804F#11P#30W気張れよ──ロイド・バニングス。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(12000, 3000)
    FadeToDark(2000, 0, -1)
    Sleep(300)
    SetChrSubChip(0x8, 0x16)
    Sleep(143)
    SetChrSubChip(0x8, 0x15)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    StopSound(111, 2000, 30)
    StopSound(125, 2000, 20)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("m9014", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_129 end

    def Function_3_2AA9(): pass

    label("Function_3_2AA9")

    OP_9B(0x1, 0x101, 0x0, 0xFFFFFD12, 0x320, 0x0)
    Sleep(400)
    Return()

    # Function_3_2AA9 end

    def Function_4_2ABC(): pass

    label("Function_4_2ABC")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x1)

    def lambda_2AD7():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AD7)
    Sleep(3000)

    def lambda_2AEF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2AEF)
    Sleep(1500)
    EndChrThread(0xFE, 0x1)
    Return()

    # Function_4_2ABC end

    def Function_5_2B03(): pass

    label("Function_5_2B03")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xE)
    Sleep(500)
    Return()

    # Function_5_2B03 end

    def Function_6_2B27(): pass

    label("Function_6_2B27")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xE)
    Sleep(150)
    SetChrSubChip(0xFE, 0xD)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    Return()

    # Function_6_2B27 end

    def Function_7_2B4B(): pass

    label("Function_7_2B4B")

    Sound(812, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    BeginChrThread(0x101, 1, 0, 10)
    Sound(898, 0, 50, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    WaitChrThread(0x101, 1)
    Return()

    # Function_7_2B4B end

    def Function_8_2BE4(): pass

    label("Function_8_2BE4")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0x10)
    Sleep(120)
    SetChrSubChip(0xFE, 0x11)
    Return()

    # Function_8_2BE4 end

    def Function_9_2C05(): pass

    label("Function_9_2C05")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x18)
    Sleep(120)
    SetChrSubChip(0xFE, 0x19)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(120)
    Return()

    # Function_9_2C05 end

    def Function_10_2C30(): pass

    label("Function_10_2C30")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(143)
    SetChrSubChip(0xFE, 0x19)
    Sleep(143)
    SetChrSubChip(0xFE, 0x18)
    Sleep(143)
    SetChrSubChip(0xFE, 0x19)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(143)
    SetChrSubChip(0xFE, 0x19)
    Sleep(143)
    SetChrSubChip(0xFE, 0x18)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1F)
    Return()

    # Function_10_2C30 end

    def Function_11_2C97(): pass

    label("Function_11_2C97")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(898, 0, 30, 0)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0x0)
    Sleep(429)
    Return()

    # Function_11_2C97 end

    def Function_12_2CC8(): pass

    label("Function_12_2CC8")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1F)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(143)
    SetChrSubChip(0xFE, 0x18)
    Sleep(429)
    Return()

    # Function_12_2CC8 end

    def Function_13_2CF3(): pass

    label("Function_13_2CF3")

    Fade(250)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(812, 0, 30, 0)
    SetChrSubChip(0xFE, 0x12)
    Sleep(300)
    Return()

    # Function_13_2CF3 end

    def Function_14_2D14(): pass

    label("Function_14_2D14")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x12)
    Sleep(120)
    SetChrSubChip(0xFE, 0x13)
    Sleep(120)
    SetChrSubChip(0xFE, 0x14)
    Sleep(120)
    SetChrSubChip(0xFE, 0x15)
    Sleep(300)
    Return()

    # Function_14_2D14 end

    def Function_15_2D3F(): pass

    label("Function_15_2D3F")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x15)
    Sleep(150)
    SetChrSubChip(0xFE, 0x16)
    Sleep(150)
    SetChrSubChip(0xFE, 0x17)
    Sleep(500)
    Return()

    # Function_15_2D3F end

    def Function_16_2D63(): pass

    label("Function_16_2D63")

    StopSound(109, 1000, 20)
    OP_25(0x6F, 0x4B)
    Sleep(100)
    OP_25(0x6F, 0x46)
    Sleep(100)
    OP_25(0x6F, 0x41)
    Sleep(100)
    OP_25(0x6F, 0x3C)
    Sleep(100)
    OP_25(0x6F, 0x37)
    Sleep(100)
    OP_25(0x6F, 0x32)
    Sleep(100)
    OP_25(0x6F, 0x2D)
    Sleep(100)
    OP_25(0x6F, 0x28)
    Return()

    # Function_16_2D63 end

    def Function_17_2D9F(): pass

    label("Function_17_2D9F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_2DC1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_2DD9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_2DF1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_END)), "loc_2E09")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_END)), "loc_2E21")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_END)), "loc_2E39")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2E39")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E43")

    Return()

    # Function_17_2D9F end

    SaveToFile()

Try(main)
