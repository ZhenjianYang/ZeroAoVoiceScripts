from ZeroScenarioHelper import *

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
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 24, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1160",                  # 0
        "ピエール副局長",         # 1
        "ソーニャ副司令",         # 2
        "ノエル",                 # 3
    ))

    AddCharChip((
        "chr/ch06402.itc",                   # 00
        "chr/ch06400.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_1B8",          # 01, 1
        "Function_2_1D0",          # 02, 2
        "Function_3_A6E",          # 03, 3
        "Function_4_AA7",          # 04, 4
        "Function_5_11DA",         # 05, 5
        "Function_6_3CD6",         # 06, 6
        "Function_7_3D1A",         # 07, 7
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_194")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_1B7")

    label("loc_194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1A8")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 5)
    Jump("loc_1B7")

    label("loc_1A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_1B7")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 2)

    label("loc_1B7")

    Return()

    # Function_0_180 end

    def Function_1_1B8(): pass

    label("Function_1_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CF")

    Return()

    # Function_1_1B8 end

    def Function_2_1D0(): pass

    label("Function_2_1D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x1B, 0x0)
    ClearScenarioFlags(0x93, 6)
    OP_C7(0x1, 0x1000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_68(40710, 1200, -390, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20840, 0)
    SetChrPos(0x101, 41600, 0, -2500, 0)
    SetChrPos(0x103, 40600, 0, -2750, 0)
    SetChrPos(0x102, 41600, 0, -4000, 0)
    SetChrPos(0x104, 40600, 0, -4250, 0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x8,
        "#5P……それで？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "#5P見つかったというのは\x01",
            "本当だろうね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        "#12P#0000Fええ、勿論です。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#12P#0106F副局長、どうか\x01",
            "気を確かに持ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "#5Pなんだ、何が言いたい。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#5P#5Pたかだか指輪一つ……\x01",
            "私が妻を恐れている事が\x01",
            "そんなに滑稽かね、ええ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#12P#0006Fいえ、あの……\x01",
            "とりあえずご報告しますね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(2000, 0)
    OP_0D()

    #C0008
    ChrTalk(
        0x101,
        (
            "#12P#0003F……というわけでして。\x02\x03",

            "#0001F最終的にはホステスの方から\x01",
            "返却していただき……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        "#5Pな、な、な……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41320, 30, 1710, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_68(40720, 1200, -2260, 3000)
    OP_95(0x8, 43880, 30, 1710, 2000, 0x0)
    OP_95(0x8, 43880, 30, -870, 2000, 0x0)
    OP_95(0x8, 41100, 30, -870, 2000, 0x0)
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 3)

    #C0010
    ChrTalk(
        0x8,
        (
            "#5Pな、何かの\x01",
            "間違いじゃないのかね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "#5P私が、私がそんな……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#12P#0300F仰ってた紅耀石の指輪みてえだし\x01",
            "間違いないんじゃないスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#12P#0203Fツァイトの嗅覚も\x01",
            "間違いないと確認しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#12P#0000Fええと、こちらがその\x01",
            "発見した指輪となります。\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x1F4, 0x3E8, 0x0)
    EndChrThread(0x8, 0x1)
    OP_95(0x8, 41600, 30, -870, 3000, 0x0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0x8, 0xB4, 0x2EE)
    Sleep(750)
    OP_95(0x8, 41600, 30, -1250, 1000, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#800M紅耀石の結婚指輪\x07\x00",
            "を渡した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_98(0x101, 0x0, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_93(0x8, 0x0, 0x1F4)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0016
    ChrTalk(
        0x8,
        "#5Pえー、ゴホンゴホン！\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    #C0017
    ChrTalk(
        0x8,
        (
            "#5Pよくやった。\x01",
            "下がってよし。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#5Pただしいいかね、今回の事は\x01",
            "絶対に内密にしたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "#5Pあのセルゲイにもだぞ。\x01",
            "絶対に誰にも話すんじゃない！\x01",
            "──判ったかね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#12P#0205Fはあ、ですが\x01",
            "まだツァイトの功績を……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 750)

    #C0021
    ChrTalk(
        0x8,
        "#5Pギロッ……！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#12P#0211F了解です……\x01",
            "（後で骨付き肉がもらえるように\x01",
            "　申請しよう。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_85D():

        label("loc_85D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_85D")

    QueueWorkItem2(0x0, 1, lambda_85D)

    def lambda_86F():

        label("loc_86F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_86F")

    QueueWorkItem2(0x1, 1, lambda_86F)

    def lambda_881():

        label("loc_881")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_881")

    QueueWorkItem2(0x2, 1, lambda_881)

    def lambda_893():

        label("loc_893")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_893")

    QueueWorkItem2(0x3, 1, lambda_893)
    OP_95(0x8, 43880, 30, -1250, 2000, 0x0)
    OP_95(0x8, 43880, 30, 0, 2000, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    #C0023
    ChrTalk(
        0x8,
        (
            "#5Pフウゥ……これでクビが繋がった。\x01",
            "繋がったとも……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(2000)

    #C0024
    ChrTalk(
        0x104,
        "#12P#0300F（妙に爽やかそうだな。）\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        "#12P#0100F（まさに一件落着ね。）\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#12P#0000F（ハハ……邪魔しちゃ悪いし\x01",
            "  そろそろ仕事に戻ろうか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        "#6P#0200F（ええ、そうしましょう。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【失くした結婚指輪】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SubItemNumber(0x33D, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x15, 0x1, 0x9)
    OP_29(0x15, 0x4, 0x10)
    SetScenarioFlags(0x5C, 2)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1D0 end

    def Function_3_A6E(): pass

    label("Function_3_A6E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA6")
    OP_95(0x8, 42500, 30, -870, 3000, 0x0)
    OP_95(0x8, 40500, 30, -870, 3000, 0x0)
    Jump("Function_3_A6E")

    label("loc_AA6")

    Return()

    # Function_3_A6E end

    def Function_4_AA7(): pass

    label("Function_4_AA7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(41000, 1900, -500, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 41100, 0, -2500, 0)
    SetChrPos(0x102, 40100, 0, -2500, 0)
    SetChrPos(0x103, 39100, 0, -2500, 0)
    SetChrPos(0x104, 42100, 0, -2500, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    Sound(818, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("神経質そうな声")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            "#4S──まったく！\x01",
            "いったい何のつもりだね！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    OP_68(41000, 900, -500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0030
    ChrTalk(
        0x8,
        (
            "#5P任務に関係ないことに\x01",
            "首を突っ込んだあげく……！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#5Pあのアリオス・マクレインに\x01",
            "手柄を持っていかれて……っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "#5Pお、おまけにそれを\x01",
            "《クロスベルタイムズ》に\x01",
            "すっぱ抜かれてしまうとは！！！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#12P#0011Fいや、ですが……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x190)

    #C0034
    ChrTalk(
        0x8,
        "#5P#4Sうるさい、言い訳無用だ！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#5P#3Sまったく、だから私は\x01",
            "新部署設立など反対だったのだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "#5Pあの忌々しいセルゲイのヤツが\x01",
            "交換条件を持ちかけなければ\x01",
            "こんな事には……！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#12P#0105Fあの、それはどういう……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0038
    ChrTalk(
        0x8,
        "#5P#4Sええい、君たちには関係ない！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0039
    ChrTalk(
        0x8,
        (
            "#1P#2Sい、いや……\x01",
            "……そう、そうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#1P#2S部下が一人も居なくなれば\x01",
            "あの疫病神だって動きようが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0041
    ChrTalk(
        0x8,
        "#5P君たち、悪いことは言わない。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#5P『特務支援課』への配属を\x01",
            "一両日中に辞退したまえ。\x02",
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

    #C0043
    ChrTalk(
        0x101,
        "#12P#0005Fえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#2P#0301Fおいおい……\x01",
            "どういうことっスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#6P#0211F……意味不明です。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "#5Pどういう事も、そのままの意味だ。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#5Pどうせ半年も保たない部署だ。\x01",
            "絶対に出世の役には立たないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#5Pそれどころか、問題に巻き込まれて\x01",
            "経歴を汚す可能性もある……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#5Pバカバカしいとは思わないかね？\x02",
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

    #C0050
    ChrTalk(
        0x8,
        (
            "#5Pロイド君は捜査官志望だったか？\x01",
            "ならば捜査課のどこかに回そう。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#5P他の者も、それぞれ適性に合った\x01",
            "新しい配属先を用意しておく。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#5Pなに、悪いようにはしない。\x01",
            "一晩じっくり考えてみたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_AA7 end

    def Function_5_11DA(): pass

    label("Function_5_11DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05700.itc", 0x1E)
    LoadChrToIndex("chr/ch00800.itc", 0x1F)
    LoadChrToIndex("apl/ch50109.itc", 0x20)
    OP_68(-2000, 1100, 15900, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, -2300, 0, 16500, 180)
    SetChrPos(0x102, -1700, 0, 16500, 180)
    SetChrPos(0x103, -2300, 0, 16500, 180)
    SetChrPos(0x104, -1700, 0, 16500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02000.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00500.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0053
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "警察本部、３階フロア──\x07\x00\x02",
        )
    )

    Sleep(2500)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_68(-2000, 1100, 12900, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(160, 0, 100, 0)
    Sleep(1000)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)

    def lambda_139F():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x300C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_139F)

    def lambda_13B9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13B9)
    Sleep(350)

    def lambda_13CD():
        OP_96(0xFE, 0xFFFFFA88, 0x0, 0x300C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13CD)

    def lambda_13E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_13E7)
    Sleep(350)

    def lambda_13FB():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13FB)

    def lambda_1415():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1415)
    Sleep(350)

    def lambda_1429():
        OP_96(0xFE, 0xFFFFFA88, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1429)

    def lambda_1443():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1443)
    WaitChrThread(0x101, 1)

    def lambda_1458():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1458)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    WaitChrThread(0x102, 1)

    def lambda_147E():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_147E)
    WaitChrThread(0x103, 1)

    def lambda_148F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_148F)
    WaitChrThread(0x104, 1)

    def lambda_14A0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_14A0)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    #C0054
    ChrTalk(
        0x104,
        (
            "#0306Fまたあの嫌味な副局長に\x01",
            "呼び出される事になるとはな……\x02\x03",

            "#0301F一体、何の用だってんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#6P#0003Fうーん……\x01",
            "客が待ってるって言ってたし。\x02\x03",

            "#0000Fただ嫌味や小言を言うために\x01",
            "呼び出したんじゃないと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        (
            "#0203F……どのみち嫌味は\x01",
            "聞かされそうな気がしますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#0106Fそうね……\x01",
            "まあ、流しておきましょう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15F9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15F9)
    Sleep(100)

    def lambda_1609():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1609)
    Sleep(50)

    def lambda_1619():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1619)
    Sleep(50)

    def lambda_1629():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1629)
    WaitChrThread(0x101, 2)
    OP_68(-2000, 1100, 9900, 3000)

    def lambda_164B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_164B)
    Sleep(100)
    WaitChrThread(0x102, 2)

    def lambda_166C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_166C)
    Sleep(50)
    WaitChrThread(0x103, 2)

    def lambda_168D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_168D)
    Sleep(100)
    WaitChrThread(0x104, 2)

    def lambda_16AE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16AE)
    Sleep(2500)
    Fade(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_68(700, 1100, 2300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 700, 30, 2300, 90)
    SetChrPos(0x102, 700, 30, 900, 90)
    SetChrPos(0x103, -500, 30, 2300, 90)
    SetChrPos(0x104, -500, 30, 900, 90)
    OP_68(3700, 1100, 2300, 2000)

    def lambda_1763():
        OP_96(0xFE, 0xE74, 0x1E, 0x8FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1763)
    Sleep(50)

    def lambda_1780():
        OP_96(0xFE, 0xE74, 0x1E, 0x384, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1780)
    Sleep(50)

    def lambda_179D():
        OP_96(0xFE, 0x9C4, 0x1E, 0x8FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_179D)
    Sleep(50)

    def lambda_17BA():
        OP_96(0xFE, 0x9C4, 0x1E, 0x384, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17BA)
    WaitChrThread(0x101, 1)

    def lambda_17D8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17D8)
    WaitChrThread(0x102, 1)

    def lambda_17E9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_17E9)
    WaitChrThread(0x103, 1)

    def lambda_17FA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_17FA)
    WaitChrThread(0x104, 1)

    def lambda_180B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_180B)
    WaitChrThread(0x104, 2)

    def lambda_181C():
        OP_95(0xFE, 3700, 0, 3200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_181C)
    WaitChrThread(0x101, 1)
    Sleep(300)
    Sound(811, 0, 100, 0)
    Sleep(800)

    #C0058
    ChrTalk(
        0x101,
        (
            "#2P#0001F──特務支援課所属、\x01",
            "バニングス以下４名、参りました。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 3500, 0, 5200, 0)

    #N0059
    NpcTalk(
        0x8,
        "神経質そうな声",
        "#2S#5Pフン……入りたまえ。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#2P#0003F失礼します。\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_79(0x0)
    Sleep(300)

    def lambda_1922():
        OP_95(0xFE, 3700, 0, 4500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1922)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_68(41270, 1000, -4180, 0)
    MoveCamera(55, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x8, 42100, 30, 1900, 180)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 42100, 30, -900, 180)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 43000, 0, -1400, 180)
    SetChrPos(0x101, 41000, 0, -7000, 0)
    SetChrPos(0x102, 41000, 0, -7000, 0)
    SetChrPos(0x103, 41000, 0, -7000, 0)
    SetChrPos(0x104, 41000, 0, -7000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(41840, 1000, -2380, 2500)
    SetCameraDistance(22000, 2500)

    def lambda_1A76():
        OP_96(0xFE, 0x9EFC, 0x0, 0xFFFFF0C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A76)

    def lambda_1A90():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A90)
    Sleep(350)

    def lambda_1AA4():
        OP_96(0xFE, 0xA348, 0x0, 0xFFFFF0C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1AA4)

    def lambda_1ABE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1ABE)
    Sleep(350)

    def lambda_1AD2():
        OP_96(0xFE, 0x9EFC, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AD2)

    def lambda_1AEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1AEC)
    Sleep(350)

    def lambda_1B00():
        OP_96(0xFE, 0xA348, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B00)

    def lambda_1B1A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1B1A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)

    #C0061
    ChrTalk(
        0x101,
        "#6P#0005F（あれ、あの制服は……）\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        "#6P#0105F（警備隊……だったかしら？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_1BBC():
        OP_96(0xFE, 0xA348, 0x0, 0xFFFFEAE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1BBC)
    #Sound(1365, 255, 100, 0)    #voice#Randy
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0063
    ChrTalk(
        0x104,
        "#11P#0307F#4Sげげっ……！？#3S\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #N0064
    NpcTalk(
        0x9,
        "眼鏡の女性",
        (
            "#2004F#5Pあら、ご挨拶ね。\x01",
            "ランディ・オルランド。\x02\x03",

            "#2002Fなにが『げげっ』なのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#12P#0309Fい、いや～……\x01",
            "少し意表を突かれたっていうか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1CB6():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CB6)
    Sleep(50)

    def lambda_1CC6():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CC6)
    Sleep(50)
    TurnDirection(0x103, 0x104, 500)

    #C0066
    ChrTalk(
        0x101,
        "#5P#0005Fなんだ、知ってるのか？\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x103,
        (
            "#6P#0211Fやましい事が\x01",
            "ありそうな反応ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        "#5Pえー、ゴホンゴホン！\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        "#5P君たち、敬礼したまえ！\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "#5Pこちらは警備隊の副司令を\x01",
            "務めておられるソーニャ二佐だ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1DE8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DE8)
    Sleep(50)

    def lambda_1DF8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1DF8)
    Sleep(50)
    OP_93(0x103, 0x0, 0x1F4)

    #C0071
    ChrTalk(
        0x101,
        "#6P#0005F警備隊の副司令……！\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        "#12P#0101Fし、失礼しました。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0073
    ChrTalk(
        0x103,
        (
            "#6P#0208F（二佐というと、普通の軍隊では\x01",
            "  中佐に相当するはずですが……）\x02\x03",

            "（そんなに偉い人なんですか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#0306F#12P（偉いもなにも……\x01",
            "  実質、警備隊のナンバー２だぞ。）\x02\x03",

            "#0300F（指揮官としてのカリスマなら\x01",
            "  間違いなくナンバー１だけどな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "#2004F#5Pふふ……\x01",
            "堅苦しくしないでちょうだい。\x02\x03",

            "#2000Fあなたたちが『特務支援課』ね？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#6P#0000Fは、はい。\x02\x03",

            "本日は、自分たち特務支援課に\x01",
            "何かお話があるとか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        "#5Pフフン、光栄に思うがいい。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "#5P君たちごとき役立たずの新米を\x01",
            "この場に呼んでやったのだからな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_93(0x9, 0x15E, 0x1F4)

    #C0079
    ChrTalk(
        0x9,
        (
            "#12P#2003F……副局長。\x01",
            "この場はどうか、わたくしに。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        "#5Pで、ですが……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "#5P……わかりました。\x01",
            "全て貴女にお任せしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        "#12P#2000Fありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0083
    AnonymousTalk(
        0x9,
        (
            "──改めて。\x01",
            "クロスベル警備隊の副司令、\x01",
            "ソーニャ・ベルツよ。\x02\x03",

            "今日は貴方たち『特務支援課』の\x01",
            "力を借りに参上したわ。\x02\x03",

            "まずは一通り、\x01",
            "話を聞いてくれないかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    SetCameraDistance(21500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    OP_68(41300, 900, -2100, 0)
    MoveCamera(47, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x9, 42200, 0, -2100, 270)
    SetChrPos(0xA, 42500, 0, -3000, 270)
    SetChrPos(0x101, 39700, 0, -2600, 90)
    SetChrPos(0x102, 39700, 0, -1600, 90)
    SetChrPos(0x104, 38400, 0, -2500, 90)
    SetChrPos(0x103, 38400, 0, -1500, 90)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0084
    AnonymousTalk(
        0x101,
        "#0001F魔獣の被害調査……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(22500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0085
    ChrTalk(
        0x9,
        (
            "#2003F#11Pええ、そうよ。\x02\x03",

            "#2000Fここ一月あまり、自治州各地で\x01",
            "特定の魔獣被害が相次いでいるの。\x02\x03",

            "その調査の手伝いを\x01",
            "あなた達にお願いしたくってね。\x02",
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

    #C0086
    ChrTalk(
        0x101,
        (
            "#6P#0011Fちょ、ちょっと待ってください。\x02\x03",

            "クロスベル市内ではなく……\x01",
            "市外での魔獣被害の調査ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        "#2000F#11Pあら、不服かしら？\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#6P#0003Fい、いえ……そんな事は。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#0101F#6Pその、警備隊の方でも\x01",
            "既に調査されているのですよね？\x02\x03",

            "その上で、私たちが\x01",
            "手伝う余地などあるのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "#2006F#11Pうーん、それが大アリなのよ。\x02\x03",

            "#2001F普通の魔獣被害というには\x01",
            "どうも不可解なことが多すぎてね。\x02\x03",

            "ウチの調査だけでは\x01",
            "手詰まりになってきているのよ。\x02\x03",

            "だから別の視点を\x01",
            "入れておきたいって所かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#6P#0005F別の視点、ですか。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "#2003F#11Pそう、警備のプロではなく\x01",
            "捜査のプロとしての視点をね。\x02\x03",

            "#2000Fその意味では、別に貴方たち\x01",
            "支援課でなくてもいいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(300)

    #C0093
    ChrTalk(
        0x9,
        (
            "#2002F#2Pたとえばエリートと名高い\x01",
            "『捜査一課』とか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    #C0094
    ChrTalk(
        0x8,
        (
            "#5Pい、いや……ハハ。\x01",
            "紹介したいのは山々なんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        "#5P何分、忙しい連中でして、ハイ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    #C0096
    ChrTalk(
        0x9,
        (
            "#2004F#11P──とまあ、\x01",
            "色々事情がおありのようだから\x01",
            "あなた達を指名させてもらったの。\x02\x03",

            "#2000F迷惑だったかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#6P#0002Fい、いえ……\x02\x03",

            "#0004F──判りました。\x01",
            "そういう事情があるなら喜んで。\x02\x03",

            "#0001Fそれで、魔獣被害の調査というと\x01",
            "具体的には何をすればいいんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    #C0098
    ChrTalk(
        0x9,
        "#5P#2000F──ノエル、例のものを。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    #Sound(1491, 255, 100, 0)    #voice#Noel

    #N0099
    NpcTalk(
        0xA,
        "女性隊員",
        "#11P#0500Fはっ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(40840, 900, -2120, 1000)

    def lambda_2947():

        label("loc_2947")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_2947")

    QueueWorkItem2(0x102, 2, lambda_2947)

    def lambda_2959():

        label("loc_2959")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_2959")

    QueueWorkItem2(0x103, 2, lambda_2959)

    def lambda_296B():
        OP_95(0xFE, 40500, 0, -2800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_296B)
    WaitChrThread(0xA, 1)

    def lambda_2989():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2989)
    EndChrThread(0x102, 0x2)

    def lambda_299A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_299A)
    EndChrThread(0x103, 0x2)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    #Sound(1492, 255, 100, 0)    #voice#Noel
    SetChrName("女性隊員")

    #A0100
    AnonymousTalk(
        0xFF,
        "──どうぞ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(60, 180, -1, -1)

    #A0101
    AnonymousTalk(
        0x101,
        "#0000Fあ、どうも。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0102
    ChrTalk(
        0x101,
        "#6P#0005F（あれ、この人……？）\x02",
    )

    CloseMessageWindow()

    #N0103
    NpcTalk(
        0xA,
        "女性隊員",
        "#11P#0505F？　どうしましたか？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#6P#0003Fい、いえ……すみません。\x02\x03",

            "#0008F（うーん……\x01",
            "  どこかで見た気がしたけど。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0105
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D4, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(41300, 900, -2100, 1000)

    def lambda_2B90():
        OP_96(0xFE, 0xA604, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2B90)
    WaitChrThread(0xA, 1)
    Sleep(500)
    OP_64(0x101)
    Sleep(300)

    #C0106
    ChrTalk(
        0x101,
        "#6P#0001Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x102,
        "#0101F#5P警備隊の調査報告書ですね。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "#2003F#11Pこちらの調査で判明したことは\x01",
            "一通りそれに書かれてあるわ。\x02\x03",

            "#2000Fまずは、その調書だけを見て\x01",
            "あなた達には捜査に入って欲しいの。\x02\x03",

            "余計な先入観を与えないためにもね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2CAB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2CAB)
    Sleep(100)
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(200)

    #C0109
    ChrTalk(
        0x102,
        "#0100F#6Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそういう事であれば\x01",
            "後ほど拝見させてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "#2004F#11Pふふ、お願いするわね。\x02\x03",

            "#2002Fそれでは申しわけないけど\x01",
            "我々はこれで失礼させてもらうわ。\x02\x03",

            "今後は支援課と直接やり取りするから\x01",
            "なにか判ったら報告をちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#6P#0000F了解しました。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(300)

    #C0113
    ChrTalk(
        0x9,
        (
            "#2000F#12P──副局長。\x01",
            "どうもお邪魔しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "#5Pい、いえいえ。\x01",
            "また遠慮なくどうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    def lambda_2E57():

        label("loc_2E57")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2E57")

    QueueWorkItem2(0x101, 2, lambda_2E57)

    def lambda_2E69():

        label("loc_2E69")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2E69")

    QueueWorkItem2(0x102, 2, lambda_2E69)

    def lambda_2E7B():

        label("loc_2E7B")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2E7B")

    QueueWorkItem2(0x103, 2, lambda_2E7B)

    def lambda_2E8D():

        label("loc_2E8D")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2E8D")

    QueueWorkItem2(0x104, 2, lambda_2E8D)

    def lambda_2E9F():
        OP_95(0xFE, 40500, 0, -3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2E9F)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x104, 500)
    Sleep(300)

    #C0115
    ChrTalk(
        0x9,
        (
            "#2002F#11Pふふ……\x02\x03",

            "どうやら結構、\x01",
            "馴染めてるみたいじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x104,
        (
            "#0302F#6Pいやあ、ハハ……\x02\x03",

            "#0304Fまあ、国境監視や演習よりは\x01",
            "楽しく過ごさせてもらってますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "#2004F#11Pそれは結構……\x01",
            "私も紹介した甲斐があったわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(300)

    #C0118
    ChrTalk(
        0x9,
        "#6P#2000Fノエル、行くわよ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)
    #Sound(1478, 255, 100, 0)    #voice#Noel

    #N0119
    NpcTalk(
        0xA,
        "女性隊員",
        "#0500F#5Pはいっ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sound(1498, 255, 100, 0)    #voice#Noel
    Sleep(1000)
    OP_68(41300, 1000, -3600, 2000)
    BeginChrThread(0x9, 3, 0, 6)
    BeginChrThread(0xA, 3, 0, 7)
    WaitChrThread(0x9, 3)
    EndChrThread(0x104, 0x2)

    def lambda_3060():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3060)
    WaitChrThread(0xA, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(39100, 1000, -2100, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21850, 0)
    OP_93(0x8, 0xE1, 0x0)
    SetChrPos(0x102, 39700, 0, -1500, 180)
    SetChrPos(0x103, 38400, 0, -1400, 180)
    OP_0D()

    #C0120
    ChrTalk(
        0x104,
        "#6P#0300Fは～……やれやれだぜ。\x02",
    )

    CloseMessageWindow()

    def lambda_311E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_311E)
    Sleep(100)
    TurnDirection(0x102, 0x104, 500)
    Sleep(200)

    #C0121
    ChrTalk(
        0x101,
        (
            "#11P#0000Fひょっとして\x01",
            "警備隊での上官だったのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0122
    ChrTalk(
        0x104,
        (
            "#6P#0300Fいや……\x01",
            "直接の上官じゃないけどな。\x02\x03",

            "訓練や軍事演習で\x01",
            "何度か指導を受けているんだ。\x02\x03",

            "#0306F美人なのに、怒らせると\x01",
            "メチャクチャ恐いんだよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#0200F#5Pランディさんの場合は、\x01",
            "生活態度が原因なのでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#5P#0104Fふふ、そうね。\x02\x03",

            "#0100F何だか女性問題で色々と\x01",
            "トラブルを起こしてたらしいし。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#11P#0005Fそういえば……\x02\x03",

            "#0001F副司令に付き添っていた\x01",
            "女性隊員も知り合いなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#6P#0300Fいや……\x01",
            "見たことのない顔だったな。\x02\x03",

            "多分、副司令が任されている\x01",
            "タングラム門詰めの隊員だろ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0127
    ChrTalk(
        0x104,
        (
            "#6P#0305Fん、そういやお前、\x01",
            "なんか気にしてたみたいだな？\x02\x03",

            "#0309Fなんだなんだ、\x01",
            "ひょっとして一目ボレかぁ～？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_33F6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_33F6)
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0128
    ChrTalk(
        0x102,
        "#5P#0111Fあら……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        "#0211F#5P………………………（じー）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0130
    ChrTalk(
        0x101,
        (
            "#11P#0011Fい、いや。\x01",
            "そんなんじゃないってば。\x02\x03",

            "ただ、どこかで\x01",
            "見かけたような気がして……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0131
    ChrTalk(
        0x8,
        "#4Sオッホン！#3S\x02",
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
    OP_68(40800, 800, 0, 1200)
    SetCameraDistance(22800, 1200)

    def lambda_3570():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3570)
    Sleep(50)

    def lambda_3580():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3580)
    Sleep(50)

    def lambda_3590():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3590)
    Sleep(50)

    def lambda_35A0():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_35A0)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x79)

    #C0132
    ChrTalk(
        0x101,
        "#0005F#12Pあ……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "#5P……君たちはいつまで\x01",
            "下らない話をしてるのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        "#5Pひょっとして……あれか？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "#5Pセルゲイあたりに言われて\x01",
            "私を馬鹿にしに来たのかね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        "#12P#0011Fい、いや、そんな！\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        "#0103F#6Pその……失礼しました。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "#5Pフン……\x01",
            "ならばとっとと出て行きたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "#5Pまったく、揃いも揃って\x01",
            "私の忠告を無視しおって……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "#5Pそれが何を意味するのかは\x01",
            "当然分かっているのだろうね？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#12P#0001Fっ……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        "#6P#0301Fおいおい……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "#5Pフフ、まあせいぜい野山で\x01",
            "魔獣探しにでも明け暮れるんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "#5P何だったら全員、そのまま\x01",
            "警備隊に移ったらどうかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        "#5Pあの忌々しいセルゲイと一緒にな。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x103,
        "#6P#0211F………………………………\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        "#0103F#6P……失礼します。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23300, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(3700, 1000, 3500, 0)
    MoveCamera(55, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 3700, 0, 4000, 180)
    SetChrPos(0x102, 3700, 0, 4000, 180)
    SetChrPos(0x103, 3700, 0, 4000, 180)
    SetChrPos(0x104, 3700, 0, 4000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    OP_68(3700, 1100, 1400, 2500)

    def lambda_3969():
        OP_96(0xFE, 0xE74, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3969)

    def lambda_3983():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3983)
    Sleep(500)

    def lambda_3997():
        OP_96(0xFE, 0x125C, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3997)

    def lambda_39B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_39B1)
    Sleep(500)

    def lambda_39C5():
        OP_96(0xFE, 0xA8C, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_39C5)

    def lambda_39DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_39DF)
    Sleep(500)

    def lambda_39F3():
        OP_96(0xFE, 0xE74, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39F3)

    def lambda_3A0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A0D)
    Sleep(500)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)
    WaitChrThread(0x101, 1)

    def lambda_3A3A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A3A)
    WaitChrThread(0x102, 1)

    def lambda_3A4B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3A4B)
    WaitChrThread(0x103, 1)

    def lambda_3A5C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3A5C)
    WaitChrThread(0x104, 1)

    def lambda_3A6D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A6D)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    #C0148
    ChrTalk(
        0x104,
        (
            "#0306F#5Pったく……\x01",
            "嫌味ったらしい野郎だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x103,
        "#0203F#6P……耳栓が欲しかったです。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#11P#0106Fまあ、今のは私たちにも\x01",
            "少しは非があったわけだから。\x02\x03",

            "#0101F……さすがに少し、\x01",
            "暴言が過ぎると思ったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#12P#0003F──まあいい。\x01",
            "目くじら立てても仕方ない。\x02\x03",

            "#0001Fとにかく一旦戻って\x01",
            "調書に目を通してみよう。\x02\x03",

            "その上で、捜査方針を決めて\x01",
            "動く必要がありそうだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BF2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3BF2)
    Sleep(50)
    TurnDirection(0x103, 0x101, 500)
    Sleep(200)

    #C0152
    ChrTalk(
        0x102,
        (
            "#5P#0100Fそうね、どうやら普通の\x01",
            "魔獣被害じゃなさそうだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x103,
        (
            "#6P#0200F不可解な事……\x01",
            "いったい何なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_11DA end

    def Function_6_3CD6(): pass

    label("Function_6_3CD6")

    OP_93(0x9, 0xB4, 0x1F4)

    def lambda_3CE2():
        OP_95(0xFE, 40500, 0, -7500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3CE2)
    Sleep(1000)

    def lambda_3CFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3CFF)
    Sound(103, 0, 100, 0)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Return()

    # Function_6_3CD6 end

    def Function_7_3D1A(): pass

    label("Function_7_3D1A")

    Sleep(600)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)

    def lambda_3D2A():
        OP_95(0xFE, 40500, 0, -5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3D2A)
    WaitChrThread(0xA, 1)

    def lambda_3D48():
        OP_95(0xFE, 40500, 0, -7500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3D48)
    Sleep(500)

    def lambda_3D65():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3D65)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    Return()

    # Function_7_3D1A end

    SaveToFile()

Try(main)
