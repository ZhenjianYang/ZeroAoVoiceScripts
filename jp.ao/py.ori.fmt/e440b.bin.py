from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e440b.bin",                # FileName
        "e440b",                    # MapName
        "e440b",                    # Location
        0x0000,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e440b",                  # 0
        "リーシャ",               # 1
        "神狼ツァイト",           # 2
        "エリィ",                 # 3
        "ティオ",                 # 4
        "ランディ",               # 5
        "ノエル",                 # 6
        "ワジ",                   # 7
        "SE制御",                 # 8
    ))

    AddCharChip((
        "chr/ch03200.itc",                   # 00
        "chr/ch02708.itc",                   # 01
    ))

    DeclNpc(2589,    0,       -29,     90,   453,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-1549,   0,       -959,    180,  405,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(456, 0)                                        # 0

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_278",          # 01, 1
        "Function_2_311",          # 02, 2
        "Function_3_385",          # 03, 3
        "Function_4_A15",          # 04, 4
        "Function_5_E14",          # 05, 5
        "Function_6_1804",         # 06, 6
        "Function_7_1CDF",         # 07, 7
        "Function_8_3696",         # 08, 8
        "Function_9_36D5",         # 09, 9
        "Function_10_5653",        # 0A, 10
        "Function_11_5670",        # 0B, 11
        "Function_12_56D1",        # 0C, 12
        "Function_13_56EE",        # 0D, 13
        "Function_14_79FC",        # 0E, 14
        "Function_15_7A18",        # 0F, 15
        "Function_16_96A8",        # 10, 16
        "Function_17_B99D",        # 11, 17
        "Function_18_DA16",        # 12, 18
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_200"),
        (1, "loc_20C"),
        (2, "loc_218"),
        (3, "loc_224"),
        (4, "loc_230"),
        (5, "loc_23C"),
        (6, "loc_248"),
        (SWITCH_DEFAULT, "loc_254"),
    )


    label("loc_200")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_20C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_218")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_224")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_230")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_23C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_248")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_254")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_260")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_277")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_277")

    Return()

    # Function_0_1C8 end

    def Function_1_278(): pass

    label("Function_1_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0")
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B")
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x40)

    label("loc_29B")

    ClearChrFlags(0x9, 0x80)

    label("loc_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_310")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_2C0")
    Event(0, 7)
    Jump("loc_310")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_2D1")
    Event(0, 9)
    Jump("loc_310")

    label("loc_2D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_2E2")
    Event(0, 13)
    Jump("loc_310")

    label("loc_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_2F3")
    Event(0, 15)
    Jump("loc_310")

    label("loc_2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_304")
    Event(0, 16)
    Jump("loc_310")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_310")
    Event(0, 17)

    label("loc_310")

    Return()

    # Function_1_278 end

    def Function_2_311(): pass

    label("Function_2_311")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF0A070D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    SetMapObjFrame(0x0, "door_l1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_l2", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r2", 0x0, 0x1)
    Sound(132, 1, 70, 0)
    Sound(497, 1, 40, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_384")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_384")

    Return()

    # Function_2_311 end

    def Function_3_385(): pass

    label("Function_3_385")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6A), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_42F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A8")
    Call(0, 5)
    Jump("loc_42A")

    label("loc_3A8")


    #C0001
    ChrTalk(
        0x8,
        (
            "#10704F……私はしばらく、\x01",
            "ここで風に当たっています。\x02\x03",

            "#10702F急ぐ必要はありませんから、\x01",
            "ゆっくり準備を済ませて来てください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42A")

    Jump("loc_A11")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_954")
    TurnDirection(0x8, 0x101, 0)

    #C0002
    ChrTalk(
        0x8,
        (
            "#10708F……いよいよ、明日……\x01",
            "クロスベル市に潜入するんですね。\x02\x03",

            "#10702Fそこまで長い期間\x01",
            "離れていたわけじゃないのに、\x01",
            "なんだか随分と懐かしい気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#00000Fそうか……\x02\x03",

            "#00006F結界が消えた事で《神機》が\x01",
            "都市の防衛に集中してるって話だけど……\x02\x03",

            "#00008Fアルカンシェルの人たちは\x01",
            "今頃どうしてるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "#10704F多分……おそらく今も、\x01",
            "練習を続けているんだと思います。\x02\x03",

            "いつ、何が起ころうとも、\x01",
            "舞台の完成度を高めるために\x01",
            "前だけを向いて揺るがない……\x02\x03",

            "#10710Fそれがイリアさんの意思であり……\x01",
            "アルカンシェルの生き様ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#00004Fはは、確かにそうかもしれないな。\x02\x03",

            "#00000F……クロスベル市を解放して、\x01",
            "この事件が一通り解決したら……\x01",
            "君はどうするつもりなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#10704F……イリアさんには会いたいですし、\x01",
            "元通りアーティストとして\x01",
            "アルカンシェルで踊りつづけたい……\x02\x03",

            "その意思はありますが、\x01",
            "今はまだ分かりません。\x02\x03",

            "#10708Fイリアさんやシュリちゃんと\x01",
            "再会したとき、何を言えばいいか……\x01",
            "それすらも今は浮かびませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00006F……そうか。\x02\x03",

            "#00000Fでも、イリアさんも\x01",
            "アルカンシェルの皆さんも、\x01",
            "きっと君を受け入れてくれるさ。\x02\x03",

            "難しく考えないで、今は目の前のことに\x01",
            "集中した方がいいんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "#10704F……ふふ、確かにそうですね。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00003Fとにかく、クロスベル市を\x01",
            "解放しない事には何も始まらない。\x02\x03",

            "#00000Fお互い、明日は頑張らないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "#10702Fはい……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x1DB, 2)
    Jump("loc_A11")

    label("loc_954")

    TurnDirection(0x8, 0x101, 0)

    #C0011
    ChrTalk(
        0x8,
        (
            "#10704F今夜はここでゆっくりと月を眺めて、\x01",
            "心を落ち着けようと思います。\x02\x03",

            "#10710Fクロスベル市とアルカンシェルを\x01",
            "解放するためにも……明日は\x01",
            "精一杯頑張らないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)

    label("loc_A11")

    TalkEnd(0xFE)
    Return()

    # Function_3_385 end

    def Function_4_A15(): pass

    label("Function_4_A15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D92")

    #C0012
    ChrTalk(
        0x9,
        (
            "#01200F#3C明日のクロスベル市解放作戦……\x01",
            "私も斥候役として\x01",
            "都市に降り立つつもりだ。\x02\x03",

            "#01203Fおぬしらとは別の地点になるが、\x01",
            "何かあればすぐに駆けつけよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#00000Fああ、よろしく頼む。\x02\x03",

            "#00004Fそういえば、\x01",
            "山岳地帯にいる神狼たちも\x01",
            "手伝ってくれるんだったな？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "#01200F#3Cうむ、彼らには\x01",
            "警備隊のレジスタンスを\x01",
            "援護するよう言付けている。\x02\x03",

            "彼らが地形を味方につければ\x01",
            "《赤い星座》の猟兵相手でも\x01",
            "五分の戦いに持ち込めるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00000Fなるほど……\x01",
            "ミレイユ三尉たちの助けは\x01",
            "任せてよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "#01200F#3Cまあ、我ら神狼が出来る\x01",
            "手伝いとしてはその程度だ。\x02\x03",

            "キーアを取り戻すのは\x01",
            "あくまでおぬしらの役目となろう。\x02\x03",

            "#01203Fそこに辿り着くまでに\x01",
            "如何なる困難が待ち受けているか、\x01",
            "様々にして知れぬが……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#00004Fああ……だけど、キーアは\x01",
            "どんなことがあっても取り戻す。\x02\x03",

            "#00000Fツァイトも、どうか見守っていてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "#01200F#3Cうむ……\x01",
            "見届けさせてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 6)
    Jump("loc_E10")

    label("loc_D92")


    #C0019
    ChrTalk(
        0x9,
        (
            "#01200F#3Cキーアを取り戻すのは\x01",
            "あくまでおぬしらの役目となろう。\x02\x03",

            "その使命を達成できるか……\x01",
            "見届けさせてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E10")

    TalkEnd(0xFE)
    Return()

    # Function_4_A15 end

    def Function_5_E14(): pass

    label("Function_5_E14")

    EventBegin(0x0)
    Fade(500)
    OP_68(3230, 200, 1330, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11810, 0)
    SetChrPos(0x101, 1070, 0, 280, 90)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_END)), "loc_E6E")
    OP_93(0x8, 0x10E, 0x0)

    label("loc_E6E")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1593")

    #C0020
    ChrTalk(
        0x101,
        (
            "#6P#00005Fリーシャ……\x01",
            "こんな所でどうしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)

    #C0021
    ChrTalk(
        0x8,
        (
            "#11P#10712Fあ……ロイドさん。\x02\x03",

            "#10710F……はい、明日の準備が整ったので、\x01",
            "少し考え事をしていました。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    #C0022
    ChrTalk(
        0x8,
        (
            "#11P#10708F#5P……いよいよ、明日……\x01",
            "クロスベル市に潜入するんですね。\x02\x03",

            "#10702Fそこまで長い期間\x01",
            "離れていたわけじゃないのに、\x01",
            "なんだか随分と懐かしい気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#6P#00000Fそうか……\x02\x03",

            "#00006F結界が消えた事で《神機》が\x01",
            "都市の防衛に集中してるって話だけど……\x02\x03",

            "#00008Fアルカンシェルの人たちは\x01",
            "今頃どうしてるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#11P#10704F#5P多分……おそらく今も、\x01",
            "練習を続けているんだと思います。\x02\x03",

            "いつ、何が起ころうとも、\x01",
            "舞台の完成度を高めるために\x01",
            "前だけを向いて揺るがない……\x02\x03",

            "#10710Fそれがイリアさんの生き様であり……\x01",
            "アルカンシェルの流儀ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#6P#00004Fはは、確かにそうかもしれないな。\x02\x03",

            "#00000F……クロスベル市を解放して、\x01",
            "この事件が一通り解決したら……\x01",
            "君はどうするつもりなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#5P#10704F……イリアさんには会いたいですし、\x01",
            "元通りアーティストとして\x01",
            "アルカンシェルで踊りつづけたい……\x02\x03",

            "その意思はありますが、\x01",
            "今はまだ分かりません。\x02\x03",

            "#10708Fイリアさんやシュリちゃんと\x01",
            "再会したとき、何を言えばいいか……\x01",
            "それすらも今は浮かびませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#6P#00006F……そうか。\x02\x03",

            "#00000Fでも、イリアさんも\x01",
            "アルカンシェルの皆さんも、\x01",
            "きっと君を受け入れてくれると思う。\x02\x03",

            "難しいことは考えずに、\x01",
            "ありのままのリーシャでいれば\x01",
            "いいんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "#5P#10712F……ありのままの私……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)
    OP_93(0x8, 0x10E, 0x1F4)

    #C0029
    ChrTalk(
        0x8,
        (
            "#11P#10703F……あの、ロイドさん。\x02\x03",

            "#10701Fこの後、私に少しだけ\x01",
            "ロイドさんの時間をもらえませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#6P#00005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#11P#10704Fふふ、最近は自分でも、\x01",
            "気を張りすぎていたと思いますし……\x02\x03",

            "#10710F明日の作戦の前に、\x01",
            "ちょっとしたおしゃべりを\x01",
            "させていただきたいんです。\x02\x03",

            "一通り準備を済ませたら、\x01",
            "もう一度この甲板に来て……\x01",
            "改めて、お話をしてもらえませんか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 2)
    Jump("loc_1649")

    label("loc_1593")


    #C0032
    ChrTalk(
        0x8,
        (
            "#11P#10704F明日の作戦の前に、\x01",
            "ちょっとしたおしゃべりを\x01",
            "させていただきたいんです。\x02\x03",

            "#10710F一通り準備を済ませたら、\x01",
            "もう一度この甲板に来て……\x01",
            "改めて、お話をしてもらえませんか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1649")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "リーシャの誘いを受ける\x01",      # 0
            "やめておく\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176D")

    #C0033
    ChrTalk(
        0x101,
        "#6P#00002Fああ、俺なんかでよければ。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "#11P#10709Fふふ、ありがとうございます。\x02\x03",

            "#10704F……私はしばらく、\x01",
            "ここで風に当たっています。\x02\x03",

            "#10702F急ぐ必要はありませんから、\x01",
            "ゆっくり準備を済ませて来てください。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 6)
    SetScenarioFlags(0x1AB, 0)
    Jump("loc_17F1")

    label("loc_176D")


    #C0035
    ChrTalk(
        0x8,
        (
            "#11P#10704F……そうですか。\x02\x03",

            "#10702Fふふ、気が向いたらで結構です。\x01",
            "また声を掛けてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#6P#00000Fああ、分かったよ。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_17F1")

    ClearChrFlags(0x8, 0x10)
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_5_E14 end

    def Function_6_1804(): pass

    label("Function_6_1804")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_18C9")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0037
    AnonymousTalk(
        0x101,
        (
            "#00006F（……エリィに、行けなくなることを\x01",
            "  ちゃんと謝っておかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0038
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはエリィに、\x01",
            "約束に行けなくなったことを謝った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 3)
    Jump("loc_1CDE")

    label("loc_18C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_1983")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0039
    AnonymousTalk(
        0x101,
        (
            "#00006F（……ティオに、行けなくなることを\x01",
            "  ちゃんと謝っておかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはティオに、\x01",
            "約束に行けなくなったことを謝った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 4)
    Jump("loc_1CDE")

    label("loc_1983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_1A41")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0041
    AnonymousTalk(
        0x101,
        (
            "#00006F（……ランディに、行けなくなることを\x01",
            "  ちゃんと謝っておかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはランディに、\x01",
            "約束に行けなくなったことを謝った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 5)
    Jump("loc_1CDE")

    label("loc_1A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_1AFB")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0043
    AnonymousTalk(
        0x101,
        (
            "#00006F（……ノエルに、行けなくなることを\x01",
            "  ちゃんと謝っておかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはノエルに、\x01",
            "約束に行けなくなったことを謝った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 6)
    Jump("loc_1CDE")

    label("loc_1AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_1BB1")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0045
    AnonymousTalk(
        0x101,
        (
            "#00006F（……ワジに、行けなくなることを\x01",
            "  ちゃんと謝っておかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはワジに、\x01",
            "約束に行けなくなったことを謝った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 7)
    Jump("loc_1CDE")

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_1C6F")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0047
    AnonymousTalk(
        0x101,
        (
            "#00006F（……リーシャに、行けなくなることを\x01",
            "  ちゃんと謝っておかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはリーシャに、\x01",
            "約束に行けなくなったことを謝った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AB, 0)
    Jump("loc_1CDE")

    label("loc_1C6F")

    SetMessageWindowPos(-1, -1, -1, -1)

    #A0049
    AnonymousTalk(
        0x101,
        (
            "#00003F（……仮眠室で一通り\x01",
            "  明日の準備を済ませてから、\x01",
            "  甲板に向かうとしよう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1CDE")

    Return()

    # Function_6_1804 end

    def Function_7_1CDF(): pass

    label("Function_7_1CDF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00100.itc", 0x1E)
    LoadChrToIndex("apl/ch51800.itc", 0x1F)
    LoadChrToIndex("apl/ch5180A.itc", 0x20)
    LoadChrToIndex("apl/ch5180B.itc", 0x21)
    SoundLoad(3411)
    SoundLoad(3412)
    SoundLoad(3413)
    SoundLoad(3414)
    SoundLoad(3415)
    SoundLoad(3416)
    SoundLoad(3417)
    SoundLoad(3418)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xA, 500, 0, -3750, 180)
    OP_63(0xA, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(135, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(2000, 0)
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(135, 10, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    OP_64(0xA)
    Sleep(500)

    #C0050
    ChrTalk(
        0xA,
        "#00108F#5P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    SetChrPos(0xA, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(19500, 2000)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_1EC2():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EC2)

    def lambda_1ED7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1ED7)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)

    #C0051
    ChrTalk(
        0x101,
        (
            "#00002F#5Pあ……\x01",
            "エリィ、先に来ていたのか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F24():

        label("loc_1F24")

        TurnDirection(0xA, 0x101, 500)
        Yield()
        Jump("loc_1F24")

    QueueWorkItem2(0xA, 2, lambda_1F24)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0052
    AnonymousTalk(
        0xA,
        (
            "#3411V#30Wうん……\x01",
            "ロイド、お疲れさま。\x02\x03",

            "#3412V明日の準備、もう終わったの？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD54)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(45, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17000, 3000)
    BeginChrThread(0xF, 1, 0, 8)

    def lambda_2041():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2041)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_68(350, 1000, -3890, 50000)
    MoveCamera(44, 14, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(16880, 50000)

    #C0053
    ChrTalk(
        0x101,
        (
            "#00000F#5Pああ、一通りはね。\x02\x03",

            "#00006Fさすがに……\x01",
            "万全とは言えないけどさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2179, 255, 100, 0)    #voice#Elie

    #C0054
    ChrTalk(
        0xA,
        "#00109F#11P#30Wふふっ……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0xB4, 0x190)
    Sleep(300)

    #C0055
    ChrTalk(
        0xA,
        (
            "#00104F#5P#30W……不思議ね……\x01",
            "こんなにも危機的な状況なのに。\x02\x03",

            "なぜか不思議なくらい、\x01",
            "心が落ち着いているの。\x02\x03",

            "#00108Fベルのこと、おじさまのこと、\x01",
            "キーアちゃんのこと……\x02\x03",

            "#00102F不安なことや心配なことは\x01",
            "幾らでもあるのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#00002F#5Pそっか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    #C0057
    ChrTalk(
        0x101,
        (
            "#00004F#5P俺も……同じかな。\x02\x03",

            "#00008F肚#2Rハラ#が括れたというか\x01",
            "やるべき事が見えたというか。\x02\x03",

            "#00002Fこれも、エリィや\x01",
            "みんなのおかげだと思う。\x02\x03",

            "#00009Fありがとう、本当に。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        "#00102F#5Pふふっ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    #C0059
    ChrTalk(
        0xA,
        (
            "#00104F#11Pお礼を言うのはこちらの方よ。\x02\x03",

            "#00108F本当なら、不安と焦りで\x01",
            "潰れていてもおかしくないのに……\x02\x03",

            "#00102F貴方が居てくれたから\x01",
            "私は今、ここでこんな風に\x01",
            "立っていることが出来る……\x02\x03",

            "#00104F……ありがとう。\x01",
            "本当に貴方が居てくれてよかった。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)

    #C0060
    ChrTalk(
        0x101,
        (
            "#00005F#6Pエリィ……\x02\x03",

            "#00012Fはは……\x01",
            "お役に立てたのなら光栄かな。\x02\x03",

            "#00004F少しはリーダーとして\x01",
            "みんなの頼りになれるくらいには\x01",
            "成長できたってことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "#00104F#11Pふふ、貴方はとっくに\x01",
            "私たち全員のリーダーよ。\x02\x03",

            "でなかったら、こんな所まで\x01",
            "みんなで来られなかったと思う。\x02\x03",

            "#00108Fでも──私が言っているのは\x01",
            "そういう意味じゃないわ。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0062
    ChrTalk(
        0x101,
        "#00005F#6Pえ……\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Fade(1000)
    SetChrPos(0x101, -500, 0, -3750, 90)
    SetChrPos(0xA, 500, 0, -3750, 180)
    OP_68(250, 1000, -4400, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 1000, -3750, 50000)
    MoveCamera(135, 20, 0, 50000)
    OP_6E(800, 50000)
    SetCameraDistance(10000, 50000)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    #C0063
    ChrTalk(
        0xA,
        (
            "#00106F#5P……今回の事件。\x02\x03",

            "どう決着したとしても\x01",
            "クロスベルは大変なことになるわ。\x02\x03",

            "#00108F多分、私たち支援課も\x01",
            "今のままではいられない……\x02\x03",

            "それぞれが、それぞれの力を\x01",
            "最大限に活かせるような立場で\x01",
            "努力していく必要がある……\x02\x03",

            "#00101Fクロスベルを建て直すために。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#00006F#12P……ああ。\x02\x03",

            "#00008F俺はこのまま警察で……\x02\x03",

            "ランディは多分、\x01",
            "国防軍が警備隊に戻ったら\x01",
            "協力を要請されるかもしれない。\x02\x03",

            "#00003Fティオは財団に戻るかもしれないけど\x01",
            "もしかしたら導力ネット方面で……\x02\x03",

            "#00001F……そしてエリィは……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "#00104F#5P……有事における\x01",
            "行政・外交方面での危機管理。\x02\x03",

            "多分、私に求められるとしたら\x01",
            "そういった知識と能力だと思う。\x02\x03",

            "#00108Fそして私は、これまでの留学で\x01",
            "そうした勉強を積み重ねてきたわ。\x02\x03",

            "#00102Fまさに今回のような事態に\x01",
            "対応できる力を手に入れるために。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00008F#12P#30W……そうか……\x02\x03",

            "#00006F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        "#00104F#5Pふふっ……良かった。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#00005F#12P……え……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    #C0069
    ChrTalk(
        0xA,
        (
            "#00102F#5P少しはそんな風に\x01",
            "寂しく思ってくれたみたいで。\x02\x03",

            "#00106F『大丈夫、エリィならやれるさ』なんて\x01",
            "励まされたらどうしようかと思っちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00012F#12Pはは……\x02\x03",

            "#00006F……本当ならそんな風に\x01",
            "言えなきゃ駄目なんだろうけど……\x02\x03",

            "#00008Fそう簡単には割り切れないみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        (
            "#00104F#5Pそれは、どうして……？\x02\x03",

            "#00100Fティオちゃんやランディが\x01",
            "居なくなるのと同じ理由で……？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        "#00011F#12Pそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        (
            "#00113F#5P──答えて、ロイド。\x02\x03",

            "今、私に不安があるとしたら\x01",
            "貴方がどう答えるのかだけ……\x02\x03",

            "#00108Fもう……分かってるんでしょう？\x02\x03",

            "#00116Fどうして私が……\x01",
            "話がしたいって言ったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#00005F#12P…………エリィ………………\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    OP_93(0x101, 0xB4, 0x1F4)
    Fade(1000)
    SetChrPos(0x101, -500, 0, -4250, 180)
    SetChrPos(0xA, 500, 0, -4250, 270)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(0, 1000, -4250, 50000)
    MoveCamera(45, 15, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(15500, 50000)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Sleep(500)

    #C0075
    ChrTalk(
        0x101,
        (
            "#00006F#5P最初はさ……\x01",
            "ぼんやりとした憧れだったんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xA, 0x514, 0x5, 0x0, 0x1, 0x2, 0x1, 0x0)
    Sleep(300)

    #C0076
    ChrTalk(
        0xA,
        "#00105F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#00004F#5Pその子は可憐で、凛として\x01",
            "それでいて包容力もあって……\x02\x03",

            "#00000F出会った時から、色んな意味で\x01",
            "綺麗な女性#4Rひ と#だなって思った。\x02\x03",

            "#00002Fこれでも最初は、カッコ付けて\x01",
            "平気なフリして話していたけど……\x02\x03",

            "#00012F白状すると……\x01",
            "ずっとドキドキしていたんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0x4, 0x5, 0x6)
    Sleep(300)

    #C0078
    ChrTalk(
        0xA,
        "#00112F#11P#30Wロ、ロイド……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#00004F#5Pさすがに一ヶ月もすれば、\x01",
            "住む世界が違うお嬢様なんて風には\x01",
            "思わなくなったけど……\x02\x03",

            "それでもずっと……\x01",
            "その子の同僚であるということは\x01",
            "俺にとっての密かな誇りだった。\x02\x03",

            "#00002Fその子の相談を受けたり、\x01",
            "ささやかだけど力になれたのは\x01",
            "俺にとって何よりも嬉しかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        "#00102F#11P……………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0x6, 0x7, 0x8)
    Sleep(150)

    #C0081
    ChrTalk(
        0x101,
        (
            "#00003F#6Pそして１年近く経って、\x01",
            "楽しいことや苦しいことを全部、\x01",
            "一緒に乗り越えてきて……\x02\x03",

            "離れ離れになったけど、\x01",
            "やっとの思いでまた会えて……\x02\x03",

            "#00008F今もまた、出会った時みたいに……\x02\x03",

            "#00002Fいや、それ以上にドキドキしている。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        "#00116F#11P………ロイド……………\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#00004F#6P──好きだよ、エリィ。\x02\x03",

            "仲間として……\x01",
            "家族としてだけじゃなく。\x02\x03",

            "#00000F一人の女の子として、君が。\x02",
        )
    )

    CloseMessageWindow()
    Sound(812, 0, 70, 0)
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0xB, 0xC, 0xD)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0084
    ChrTalk(
        0xA,
        "#00106F#3413V#11Pロイド……\x02",
    )

    CloseMessageWindow()
    OP_A1(0xA, 0x640, 0x4, 0xD, 0xE, 0xF, 0x10)

    def lambda_3192():

        label("loc_3192")

        OP_A0(0xFE, 1000, 0x10, 0x12)
        Yield()
        Jump("loc_3192")

    QueueWorkItem2(0xA, 3, lambda_3192)
    Sleep(500)

    #C0085
    ChrTalk(
        0xA,
        "#00116F#3414V#11P私も──貴方が好き。\x02",
    )

    CloseMessageWindow()
    OP_24(0xD56)
    Sleep(300)
    EndChrThread(0xA, 0x3)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x1)
    OP_68(400, 1000, -4250, 1200)

    def lambda_31FA():
        OP_9B(0x1, 0xFE, 0x0, 0x190, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31FA)
    Sleep(50)

    def lambda_3212():
        OP_A0(0xFE, 1000, 0x1, 0x5)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3212)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sound(812, 0, 100, 0)

    def lambda_3248():
        OP_A0(0xFE, 1000, 0x7, 0x9)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3248)

    def lambda_3255():
        OP_A0(0xFE, 1000, 0x7, 0x9)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3255)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Fade(800)
    SetCameraDistance(15000, 1000)

    def lambda_3278():
        OP_A0(0xFE, 1000, 0x9, 0xC)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3278)
    OP_A0(0xA, 1000, 0x9, 0xC)
    Sleep(300)
    OP_A0(0xA, 1000, 0x19, 0x1E)
    Sleep(300)

    #C0086
    ChrTalk(
        0xA,
        "#3415V#11P#40W#2S……………ん…………………\x02",
    )

    CloseMessageWindow()
    OP_24(0xD57)
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    Sound(812, 0, 100, 0)

    def lambda_32DC():
        OP_A0(0xFE, 1000, 0xC, 0xF)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_32DC)

    def lambda_32E9():
        OP_A0(0xFE, 1000, 0xC, 0xF)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_32E9)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33EB")

    #C0087
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30Wはは……\x02\x03",

            "#00002F……あの時の続き、\x01",
            "やっと出来たかな……？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    #C0088
    ChrTalk(
        0xA,
        (
            "#00104F#3416V#11P#40W…………うん……………\x02\x03",

            "#00116F#3417Vずっと、ずっと待ってた……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD59)
    OP_C9(0x1, 0x80000000)

    #C0089
    ChrTalk(
        0x101,
        "#00012F#6P#40Wごめん、待たせて。\x02",
    )

    CloseMessageWindow()
    Jump("loc_344D")

    label("loc_33EB")


    #C0090
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30Wずっと……\x01",
            "こうしたいと思ってた。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        "#00104F#11P#40W…………私も………………\x02",
    )

    CloseMessageWindow()

    label("loc_344D")

    Sleep(300)

    def lambda_3455():
        OP_A0(0xFE, 1000, 0xF, 0x12)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3455)
    Sleep(50)

    def lambda_3465():
        OP_A0(0xFE, 1000, 0xF, 0x12)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3465)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Sleep(500)

    #C0092
    ChrTalk(
        0x101,
        (
            "#00006F#6P#30W──たとえ仕事で同じ道を\x01",
            "歩けなくなったとしても……\x02\x03",

            "#00004Fずっとお互いを必要とし、\x01",
            "支え合って前に進めるような……\x02\x03",

            "#00002Fそんな関係に、なってくれるか？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xA, 1300, 0x12, 0x17)
    Sleep(500)

    #C0093
    ChrTalk(
        0xA,
        "#00109F#3418V#11P#40W………はい…………！\x02",
    )

    CloseMessageWindow()
    OP_24(0xD5A)
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(16500, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x157C)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_35A5")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_35A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35B7")
    Jump("loc_3673")

    label("loc_35B7")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ロイドとエリィは\x01",
            "スターブラストⅢを習得した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとエリィのコンビクラフト、\x01",
            "《スターブラスト》が強化されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x1, 0x1AE)
    AddCraft(0x0, 0x1AE)

    label("loc_3673")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x28, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 1)
    OP_29(0xB1, 0x1, 0x1)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1CDF end

    def Function_8_3696(): pass

    label("Function_8_3696")

    OP_25(0x84, 0x41)
    OP_25(0x1F1, 0x23)
    Sleep(300)
    OP_25(0x84, 0x3C)
    OP_25(0x1F1, 0x1E)
    Sleep(300)
    OP_25(0x84, 0x37)
    OP_25(0x1F1, 0x19)
    Sleep(300)
    OP_25(0x84, 0x32)
    OP_25(0x1F1, 0x14)
    Sleep(300)
    OP_25(0x84, 0x2D)
    Sleep(300)
    OP_25(0x84, 0x28)
    Sleep(300)
    OP_25(0x84, 0x23)
    Return()

    # Function_8_3696 end

    def Function_9_36D5(): pass

    label("Function_9_36D5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00200.itc", 0x1E)
    LoadChrToIndex("apl/ch51801.itc", 0x1F)
    LoadChrToIndex("apl/ch51802.itc", 0x20)
    SoundLoad(2698)
    SoundLoad(2699)
    SoundLoad(2700)
    SoundLoad(2701)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00202.itp")
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xB, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(470, 800, 1980, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_3803():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3803)

    def lambda_3818():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3818)
    PlayBGM("ed7560", 0)
    SetCameraDistance(14000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0096
    ChrTalk(
        0x101,
        "#00005F#5P（あれ、ティオ……？）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xF, 1, 0, 8)
    Fade(1000)
    SetChrPos(0x101, 250, 0, 1250, 180)
    SetChrPos(0xB, 500, 0, -3750, 180)
    OP_68(500, 2300, -3750, 0)
    MoveCamera(125, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7500, 0)
    OP_68(500, 2300, -3750, 3000)
    MoveCamera(125, -5, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(8500, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    #C0097
    ChrTalk(
        0xB,
        "#00208F#30W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0098
    ChrTalk(
        0x101,
        "#00000F#6P#N──ティオ？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_68(320, 1000, -2950, 5000)
    MoveCamera(115, 15, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9000, 5000)

    def lambda_39B4():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF92A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39B4)
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    OP_0D()

    def lambda_39FC():

        label("loc_39FC")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_39FC")

    QueueWorkItem2(0xB, 2, lambda_39FC)
    Sleep(1500)
    OP_64(0xB)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xB, 500)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0099
    AnonymousTalk(
        0xB,
        "#2698V#40Wロイド……さん……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA8A)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    #C0100
    ChrTalk(
        0x101,
        (
            "#00012F#6Pはは、珍しいな。\x02\x03",

            "#00002F声をかけるまで\x01",
            "ティオが気付かないなんて。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0101
    ChrTalk(
        0xB,
        "#00204F#2699V#11P#40Wふふ……そうですね。\x02",
    )

    CloseMessageWindow()
    OP_24(0xA8B)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -3750, 3000)
    MoveCamera(135, 20, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(9000, 3000)
    OP_95(0x101, -500, 0, -3750, 1200, 0x0)
    TurnDirection(0x101, 0xB, 500)
    EndChrThread(0xB, 0x2)
    OP_6F(0x79)

    #C0102
    ChrTalk(
        0x101,
        (
            "#00004F#12P明日の準備、一通り済ませたよ。\x02\x03",

            "#00000F万全とは言えないけど\x01",
            "他のみんなの大変さを考えたら\x01",
            "これが精一杯だと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        (
            "#00204F#5Pはい……\x02\x03",

            "キーアや課長たちと会うためにも\x01",
            "頑張らないといけませんね。\x02\x03",

            "#00202Fそれに、コッペも心配ですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#00006F#12Pそうだな……\x02\x03",

            "#00005F……そういえば、ヨナは\x01",
            "ミシュラム送りにされたけど。\x02\x03",

            "財団のロバーツ主任は\x01",
            "今、どうしてるんだろう？\x02\x03",

            "#00008F状況が状況だし……\x01",
            "レマン自治州に帰ったのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        (
            "#00206F#5Pいえ、どうやら主任は\x01",
            "財団からの退去指示に\x01",
            "応じなかったみたいです。\x02\x03",

            "#00208Fマリアベルさんたちに奪われた\x01",
            "導力ネットの状況をチェックするため\x01",
            "市内に残っているみたいで……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    OP_A0(0xB, 1000, 0x1, 0x3)
    OP_0D()
    Sleep(200)

    #C0106
    ChrTalk(
        0xB,
        (
            "#00206F#5Pまあ、あの人のことですから\x01",
            "のらりくらりと追及を\x01",
            "免れているとは思いますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        "#00006F#12Pそっか……ちょっと心配だな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0xB, 1200, 0x3, 0x1)
    Sleep(300)

    #C0108
    ChrTalk(
        0xB,
        (
            "#00202F#5Pはい……\x01",
            "ちょっとだけですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Fade(1000)
    SetChrSubChip(0xB, 0x4)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xB, 500, 0, -4250, 270)
    OP_68(0, 1100, -4250, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_68(0, 1000, -4250, 50000)
    MoveCamera(45, 25, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(16000, 50000)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    OP_0D()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    #C0109
    ChrTalk(
        0xB,
        (
            "#00206F#11P──ロイドさん。\x02\x03",

            "#00208F相談、乗ってくれますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、もちろん。\x02\x03",

            "#00001Fひょっとして\x01",
            "さっき見ていた手紙のことか？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        "#00206F#11P気付いていましたか……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    OP_A0(0xB, 1000, 0x4, 0x6)
    Sleep(500)
    Sound(802, 0, 100, 0)
    OP_A0(0xB, 1000, 0x7, 0x8)
    OP_0D()
    Sleep(300)

    #C0112
    ChrTalk(
        0xB,
        (
            "#00203F#11P昨日、アッバスさんのルートで\x01",
            "わたしに届けられた手紙……\x02\x03",

            "#00201F共和国のアルタイル市に来ている\x01",
            "わたしの両親からのものです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0113
    ChrTalk(
        0x101,
        (
            "#00005F#6Pえ……！？\x02\x03",

            "#00002Fそれじゃあ、レミフェリアから\x01",
            "わざわざティオに会いに……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xB,
        (
            "#00206F#11Pはい、クロスベルが独立してから\x01",
            "手紙や通信による連絡も取れず……\x02\x03",

            "財団からの情報を頼りに\x01",
            "国境の町まで来ているそうです。\x02\x03",

            "#00208F現在、貨物以外の行き来は\x01",
            "完全に制限されてしまっているので\x01",
            "足止めされているみたいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00004F#6Pそうか……\x02\x03",

            "#00000F……だったら話は早い！\x01",
            "この船でアルタイル市まで──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0xB, 1300, 0x8, 0xA)
    Sleep(150)

    #C0116
    ChrTalk(
        0xB,
        (
            "#00204F#11P必要ないです。\x02\x03",

            "既にわたしが無事という情報は\x01",
            "同じルートで伝えてもらいました。\x02\x03",

            "#00208Fそれに、いま会ったら心が乱れて\x01",
            "明日に支障があるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#00011F#6P………で、でも…………\x02\x03",

            "#00006F#30W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xB, 800, 0xA, 0x8)
    Sleep(300)

    #C0118
    ChrTalk(
        0xB,
        (
            "#00209F#11Pふふ……\x01",
            "そんな顔をしないでください。\x02\x03",

            "#00202Fこの事件が解決したら\x01",
            "両親には必ず会うつもりです。\x02\x03",

            "#00204Fロイドさんのおかげで、\x01",
            "少し里心が出てきましたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        "#00005F#6Pえ……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A0(0xB, 1000, 0xD, 0xB)
    Sleep(500)

    #C0120
    ChrTalk(
        0xB,
        (
            "#00208F#5P#30W……みんな離れ離れになって……\x02\x03",

            "不安で、寂しくて、\x01",
            "ロイドさんが指名手配されたと聞いて\x01",
            "心配で胸を締め付けられて……\x02\x03",

            "#00206F……本当に、嬉しかったんです。\x02\x03",

            "ロイドさんとまた会う事が出来て。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#00008F#6P#30Wあ……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        (
            "#00204F#5P#30Wその時に、思ったんです。\x02\x03",

            "ああ──わたしは生きているって。\x02\x03",

            "#00208F誰かを大切に想うことで\x01",
            "人と人の間にちゃんと在るって。\x02\x03",

            "#00202F……どう生きたらいいのか、\x01",
            "どうして生きているのか……\x02\x03",

            "#00209F３年前、ガイさんに聞こうとした\x01",
            "質問の答えが分かった気がしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        "#00000F#6P#30W……ティオ………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xB, 1300, 0xB, 0xD)
    Sleep(300)

    #C0124
    ChrTalk(
        0xB,
        (
            "#00206F#11P#30Wそれから、エリィさんや\x01",
            "ランディさんたちとまた会えて……\x02\x03",

            "#00208Fみんなで一生懸命、\x01",
            "キーアのためにここまで来て……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(812, 0, 60, 0)
    OP_A0(0xB, 1200, 0xD, 0x10)
    Sleep(300)

    #C0125
    ChrTalk(
        0xB,
        (
            "#00212F#11P#30W……そして、この手紙を読んで\x01",
            "まるで氷が溶けるみたいに\x01",
            "素直な気持ちが湧いてきました。\x02\x03",

            "#00213F久しぶりに……\x01",
            "お父さんとお母さんに会いたいって。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#00004F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(400, 1000, -4250, 1200)
    OP_9A(0x101, 0xB, 0x258, 0x1F4, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)

    def lambda_487D():
        OP_A0(0xFE, 1000, 0x10, 0x13)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_487D)

    def lambda_488A():
        OP_A0(0xFE, 1000, 0x20, 0x23)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_488A)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sound(898, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 10)
    BeginChrThread(0x101, 3, 0, 12)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)

    #C0127
    ChrTalk(
        0xB,
        "#00216F#11P#40W#2S…………ぁ………………\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W……よかった。\x01",
            "本当によかった……\x02\x03",

            "きっかけについては\x01",
            "ちょっと照れくさいけど……\x02\x03",

            "#00002Fでも、ティオが\x01",
            "そう思えるようになったのは\x01",
            "俺にとって何よりも嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x4B0, 0x5, 0x13, 0x18, 0x19, 0x18, 0x13)
    Sleep(300)

    #C0129
    ChrTalk(
        0xB,
        "#00215F#11P#30W………ロイドさん…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    Fade(1000)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 0, 0, -3750, 90)
    SetChrPos(0xB, 500, 0, -3750, 270)
    OP_68(0, 1000, -3750, 0)
    MoveCamera(140, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    MoveCamera(140, 20, 0, 50000)
    SetCameraDistance(9000, 50000)

    def lambda_4A5A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A5A)
    OP_0D()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    OP_A1(0xB, 0x320, 0x3, 0x1, 0x2, 0x3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Sleep(500)

    #C0130
    ChrTalk(
        0xB,
        (
            "#00204F#5P#30W……２つ、お願いがあります。\x02\x03",

            "聞いていただけませんか？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0131
    ChrTalk(
        0x101,
        (
            "#00002F#12Pああ──何でも。\x02\x03",

            "#00009F遠慮なく言ってみてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    Sleep(300)

    #C0132
    ChrTalk(
        0xB,
        (
            "#00208F#5P#30Wその、１つは……\x02\x03",

            "#00208F頭を撫でてもらうのも\x01",
            "すごく好きなんですが……\x02\x03",

            "#00201Fさすがに、こんな綺麗な夜には\x01",
            "少し子供っぽすぎる気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#00011F#12Pそ、そういうもんか？\x02\x03",

            "#00012Fって、確かに俺も\x01",
            "兄貴やランディにされたら\x01",
            "子供扱いされてる気分になったな。\x02\x03",

            "#00000Fえっと、それじゃあ……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 11)
    Sleep(1500)
    OP_63(0x101, 0x0, 1900, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 1950, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    #C0134
    ChrTalk(
        0x101,
        "#00011F#12Pティ、ティオ……？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_A1(0xB, 0x3E8, 0x5, 0x1E, 0x2B, 0x2C, 0x2B, 0x1E)
    Sleep(300)

    #A0135
    AnonymousTalk(
        0xB,
        (
            "#40Wそ、その……\x02\x03",

            "再会した時、走って抱き付いたら\x01",
            "ちょっと痛そうにしていたので……\x02\x03",

            "……これなら大丈夫ですよね？\x02",
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

    #C0136
    ChrTalk(
        0x101,
        (
            "#00000F#12P#30Wあ、ああ……\x02\x03",

            "#00004F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(250, 1000, -3750, 1000)
    OP_96(0x101, 0xFFFFFF9C, 0x0, 0xFFFFF15A, 0x1F4, 0x0)
    Fade(250)
    Sound(898, 0, 100, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_4E56():
        OP_A0(0xFE, 1000, 0x1E, 0x22)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_4E56)

    def lambda_4E63():
        OP_A0(0xFE, 1000, 0x36, 0x39)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4E63)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    #C0137
    ChrTalk(
        0xB,
        (
            "#05524F#2700V#5P#40Wふふ……あったかいです……\x02\x03",

            "#05526F#2701Vエリィさんみたいに\x01",
            "抱き心地が良くないのは\x01",
            "申しわけないですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xA8D)
    OP_C9(0x1, 0x80000000)

    #C0138
    ChrTalk(
        0x101,
        (
            "#00012F#12P#30Wい、いや、これはこれで……\x02\x03",

            "#00008F（ていうか、ヤバイな……\x01",
            "  ……ティオの甘い匂いが……）\x02\x03",

            "#00011F（───じゃなくて！）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(812, 0, 60, 0)

    def lambda_4FA6():
        OP_A0(0xFE, 1000, 0x22, 0x25)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_4FA6)

    def lambda_4FB3():
        OP_A0(0xFE, 1000, 0x39, 0x3C)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4FB3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sleep(300)

    #C0139
    ChrTalk(
        0x101,
        (
            "#00012F#12Pコホン……\x01",
            "で、もう一つのお願いは？\x02\x03",

            "#00000Fこうなったらとことん、\x01",
            "付き合わせてもらうぞ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x3E8, 0x5, 0x25, 0x2E, 0x2F, 0x2E, 0x25)
    Sleep(300)

    #C0140
    ChrTalk(
        0xB,
        (
            "#05524F#5Pはい、もう一つは……\x02\x03",

            "#05522F何とか事件が一段落して\x01",
            "両親がクロスベルに来られたら\x01",
            "一緒に会って欲しいんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0141
    ChrTalk(
        0x101,
        (
            "#00009F#12Pああ、もちろんさ。\x01",
            "一度挨拶したいと思ってたし。\x02\x03",

            "#00002Fでも、そんなの言われるまでも\x01",
            "無いと思うけど……？\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        (
            "#05526F#5Pいえ、ただの挨拶ではなく……\x02\x03",

            "#05528Fわたしがクロスベルに残る理由を\x01",
            "分かりやすく説明したいんです。\x02\x03",

            "#05521Fそうでないと２人とも\x01",
            "納得してくれないでしょうから。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#00005F#12P？？？\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xB,
        (
            "#05524F#5Pみんながいて、みっしぃもいて\x01",
            "導力ネットもあるクロスベルが\x01",
            "大好きというのもありますが……\x02\x03",

            "#05528Fそれ以上に、どう生きたらいいか、\x01",
            "どうして生きているのか……\x02\x03",

            "#05522Fその答えをくれた大切な人の側で\x01",
            "これからも暮らして行きたい──\x02\x03",

            "#05529Fそう伝えようと思っています。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0145
    ChrTalk(
        0x101,
        (
            "#00007F#12P#4Sえええっ！？#3S\x02\x03",

            "#00011Fちょ、ちょっと待った！\x01",
            "それじゃあまるで……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xB, 0x2E)
    OP_0D()
    Sleep(300)

    #C0146
    ChrTalk(
        0xB,
        (
            "#05531F#5P“何でも”って、\x01",
            "言いましたよね……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0147
    ChrTalk(
        0x101,
        (
            "#00012F#12P──ああもう、分かった！\x02\x03",

            "#00002F無事、事件が一段落したら\x01",
            "一緒に挨拶させてもらうよ！\x02\x03",

            "#00006Fはあ、今から何とか\x01",
            "言い訳を考えとかなきゃな……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xB, 0x3E)
    OP_0D()
    Sleep(400)

    #C0148
    ChrTalk(
        0xB,
        (
            "#05529F#5Pふふっ……\x01",
            "頑張ってください。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(812, 0, 60, 0)
    SetChrSubChip(0xB, 0x2E)
    Sleep(50)
    SetChrSubChip(0xB, 0x25)
    Sleep(200)
    SetCameraDistance(10500, 3500)

    def lambda_550B():
        OP_A0(0xFE, 1000, 0x26, 0x29)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_550B)

    def lambda_5518():
        OP_A0(0xFE, 1000, 0x3C, 0x39)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5518)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_555C")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_555C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_556E")
    Jump("loc_5630")

    label("loc_556E")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0149
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ロイドとティオは\x01",
            "Ω#2Rオメガ#ストライクⅢを習得した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0150
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとティオのコンビクラフト、\x01",
            "《Ωストライク》が強化されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x2, 0x1AF)
    AddCraft(0x0, 0x1AF)

    label("loc_5630")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x29, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 2)
    OP_29(0xB1, 0x1, 0x2)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_36D5 end

    def Function_10_5653(): pass

    label("Function_10_5653")

    OP_A1(0xFE, 0x3E8, 0x6, 0x13, 0x14, 0x15, 0x16, 0x15, 0x14)
    OP_A1(0xFE, 0x3E8, 0x6, 0x13, 0x14, 0x15, 0x16, 0x15, 0x14)
    SetChrSubChip(0xFE, 0x13)
    Return()

    # Function_10_5653 end

    def Function_11_5670(): pass

    label("Function_11_5670")

    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    OP_A0(0xFE, 900, 0x0, 0x3)
    Sleep(300)
    Sound(898, 0, 100, 0)
    OP_A0(0xFE, 900, 0x4, 0xC)
    Sleep(300)
    OP_A0(0xFE, 1000, 0xC, 0xF)
    Sound(318, 0, 100, 0)
    Sleep(200)
    Sound(898, 0, 100, 0)
    OP_A0(0xFE, 1000, 0x10, 0x14)
    Sleep(500)
    Sound(812, 0, 100, 0)
    OP_A0(0xFE, 1000, 0x14, 0x1B)
    Sleep(300)
    OP_A0(0xFE, 1000, 0x1B, 0x1E)
    Return()

    # Function_11_5670 end

    def Function_12_56D1(): pass

    label("Function_12_56D1")

    OP_A1(0xFE, 0x3E8, 0x6, 0x23, 0x24, 0x25, 0x26, 0x25, 0x24)
    OP_A1(0xFE, 0x3E8, 0x6, 0x23, 0x24, 0x25, 0x26, 0x25, 0x24)
    SetChrSubChip(0xFE, 0x23)
    Return()

    # Function_12_56D1 end

    def Function_13_56EE(): pass

    label("Function_13_56EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00300.itc", 0x1E)
    LoadChrToIndex("apl/ch51804.itc", 0x1F)
    LoadChrToIndex("apl/ch51805.itc", 0x20)
    SoundLoad(2778)
    SoundLoad(2779)
    SoundLoad(2780)
    SoundLoad(2781)
    SoundLoad(2782)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis266.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis267.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis268.itp")
    CreatePortrait(4, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis316.itp")
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xC, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(470, 800, 1980, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_589F():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_589F)

    def lambda_58B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_58B4)
    PlayBGM("ed7560", 0)
    SetCameraDistance(14000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_C9(0x0, 0x80000000)

    #C0151
    ChrTalk(
        0xC,
        "#00300F#2778V#12P#N#30Wよ、来たか。\x02",
    )

    CloseMessageWindow()
    OP_24(0xADA)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    #C0152
    ChrTalk(
        0x101,
        "#00002F#5Pランディ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xF, 1, 0, 8)
    Fade(1000)
    SetChrPos(0x101, 500, 0, 1250, 180)
    SetChrPos(0xC, 500, 0, -3750, 0)
    OP_68(500, 2300, -3750, 0)
    MoveCamera(125, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    OP_68(500, 1600, -3750, 5000)
    MoveCamera(125, 1, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9500, 5000)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0153
    AnonymousTalk(
        0xC,
        (
            "#2779V#40Wったく、誘っといて何だが\x01",
            "こんな夜に野郎相手に\x01",
            "時間割いてんじゃねえっての。\x02\x03",

            "#2780Vちったあ色っぽい話をする\x01",
            "相手はいねぇのかよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xADC)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_68(630, 1000, -3200, 3000)
    MoveCamera(120, 10, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(10000, 3000)
    Sound(100, 0, 100, 0)

    def lambda_5B10():

        label("loc_5B10")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5B10")

    QueueWorkItem2(0xC, 2, lambda_5B10)
    OP_95(0x101, 250, 0, -1750, 1200, 0x0)
    TurnDirection(0x101, 0xC, 500)
    OP_6F(0x79)

    #C0154
    ChrTalk(
        0x101,
        (
            "#00006F#6P……余計なお世話だっての。\x02\x03",

            "#00001Fそれに作戦前だし……\x01",
            "そんな事を考える余裕は無いさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xC,
        (
            "#00306F#11Pバッカ、そういう時だからこそ\x01",
            "落とすチャンスなんじゃねぇか。\x02\x03",

            "#00308F①『ロイド、わたし不安なの……』\x02\x03",

            "#00301F②『大丈夫だ、俺が付いている』\x02\x03",

            "#00309F③『ガバーッ！』っていう\x01",
            "黄金コンボが使えるだろうが。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#00011F#6P最後のは飛躍しすぎだろ……\x02\x03",

            "#00012Fランディがモテるっていうのが\x01",
            "なんか眉唾に思えてくるんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        "#00310F#11Pなにおう～？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_68(110, 1000, -4070, 4000)
    MoveCamera(135, 15, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(10000, 30000)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(500)
    EndChrThread(0xC, 0x2)
    OP_93(0xC, 0xB4, 0x190)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    #C0158
    ChrTalk(
        0xC,
        "#00300F#5P……明日の準備は終わったか？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        (
            "#00006F#6Pああ、正直万全とは\x01",
            "とても言えないけど……\x02\x03",

            "#00001Fミレイユさんたちの事を考えたら\x01",
            "贅沢は言ってられないしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xC,
        (
            "#00306F#5Pまあな……\x02\x03",

            "#00303Fレジスタンスや黒月方面は\x01",
            "多分猟兵どもが出撃するだろう。\x02\x03",

            "#00308F叔父貴やシャーリィは\x01",
            "簡単には出てこないだろうが……\x02\x03",

            "#00301Fそれでもガレスあたりが出たら\x01",
            "相当厳しい戦いになるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        "#00008F#6Pそうか……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    EndChrThread(0xC, 0x2)
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xC)
    Sleep(500)

    #C0162
    ChrTalk(
        0x101,
        (
            "#00006F#6P《赤い星座》……\x01",
            "聞いていた以上の戦闘力だな。\x02\x03",

            "#00000F大陸西部最強と言われてるのも\x01",
            "うなずける気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xC,
        (
            "#00306F#5Pまあ、歴史だけで言うなら\x01",
            "中世の暗黒時代に遡るからなぁ。\x02\x03",

            "#00301F狂戦士#6Rベルゼルガー#オルランド……\x02\x03",

            "当時から名の知れた\x01",
            "戦士たちの一族だったらしい。\x02\x03",

            "#00308F常に最新の戦闘技術を取り入れ、\x01",
            "特殊な鍛錬法で肉体を強化する事で\x01",
            "“最強”と呼ばれ続けた戦士団……\x02\x03",

            "#00303Fそれが近代になって猟兵団となり、\x01",
            "一族の紋章だった赤いサソリを\x01",
            "名前として掲げたってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        "#00001F#6Pそうだったのか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0xC, 500)

    #C0165
    ChrTalk(
        0x101,
        (
            "#00005F#12Pひょっとして……\x02\x03",

            "#00001F前に、旧市街のレースを\x01",
            "あんな形式でやったのって？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(100)

    #C0166
    ChrTalk(
        0xC,
        (
            "#00309F#5Pハハ、よく気付いたな。\x02\x03",

            "#00300Fあれは、《赤い星座》で行われる\x01",
            "戦闘訓練をアレンジしたもんだ。\x02\x03",

            "#00306Fもっとも本来は、より実戦に近い、\x01",
            "いつ死んでもおかしくない代物でな。\x02\x03",

            "ガキの頃から、毎日のように\x01",
            "血反吐を吐くまでやらされたモンだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#00008F#12Pなるほど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    #C0168
    ChrTalk(
        0x101,
        (
            "#00000F#12P……それをランディに仕込んだのが\x01",
            "《闘神》と呼ばれた親父さんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xC,
        (
            "#00306F#5Pああ──\x01",
            "バルデル・オルランド。\x02\x03",

            "#00308Fまるで鋼鉄の獅子のように\x01",
            "厳しく容赦のない親父だった。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_93(0xC, 0xB4, 0x190)
    Fade(1000)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xC, 500, 0, -4250, 180)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16000, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    #C0170
    ChrTalk(
        0xC,
        (
            "#00303F#5P#30W──３年前。\x02\x03",

            "俺はその《闘神》から\x01",
            "一つの任務を与えられた。\x02\x03",

            "#00308F宿敵ともいえる猟兵団、\x01",
            "《西風の旅団》の２個中隊……\x02\x03",

            "#00311Fそいつらを俺の部隊で\x01",
            "殲滅しろという内容だった。\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    SetCameraDistance(15000, 2500)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0171
    AnonymousTalk(
        0xC,
        (
            "#3C#30W敵兵力はこちらの倍……\x02\x03",

            "実力が拮抗している事を考えると\x01",
            "正直、厳しすぎる戦力差だった。\x02\x03",

            "だがこちらには奇襲と\x01",
            "地形を利用できる強みがあった。\x02\x03",

            "そして俺は……\x02\x03",

            "……日頃から補給のために\x01",
            "立ち寄っていた村を利用した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(280, 145, -1, -1)

    #A0172
    AnonymousTalk(
        0xC,
        (
            "#3C#30W奇襲で陽動を行い、\x01",
            "片方の中隊を村に引き寄せて……\x02\x03",

            "崖崩れを起こすことで分断し、\x01",
            "もう片方を一気に潰した。\x02\x03",

            "そして村外れの納屋を\x01",
            "爆破することで敵の混乱を誘い……\x02\x03",

            "村から退却するルートを読んで\x01",
            "そこに全火力を集中して撃破した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0173
    AnonymousTalk(
        0xC,
        (
            "#3C#30W……村人の犠牲は\x01",
            "一人も出さないつもりだった。\x02\x03",

            "だが、戦場における見込みなんて\x01",
            "流動的で当てにならねぇもんだ。\x02\x03",

            "結局、撃破するポイントは\x01",
            "５０アージュほど村寄りになって……\x02\x03",

            "一軒の雑貨屋を巻き添えにした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x7D0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(800)
    SetMessageWindowPos(280, 145, -1, -1)

    #A0174
    AnonymousTalk(
        0xC,
        (
            "#3C#40W……多分、猟兵仲間以外で\x01",
            "初めてダチと言えるヤツだった。\x02\x03",

            "任務がない時は、たまに酒場で\x01",
            "一緒に飲んで騒いでナンパして……\x02\x03",

            "いずれ街に出て、自分の店を\x01",
            "持つのが夢だって言ってた。\x02\x03",

            "その夢も、命も、全て俺が奪った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(858, 0, 100, 0)
    Sleep(1500)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    Sleep(1300)
    SetMessageWindowPos(280, 170, -1, -1)
    SetChrName("シャーリィ")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30Wわああっ！\x01",
            "ランディ兄、やるじゃん♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("戦鬼シグムント")

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30Wクク──合格だ、ランドルフ。\x02\x03",

            "この“試し”をもって\x01",
            "お前は次の《闘神》に決まった。\x02\x03",

            "兄貴の跡を継げるよう、\x01",
            "これからも精進するがいい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    MoveCamera(40, 20, 0, 50000)
    SetCameraDistance(16540, 50000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(300)

    #C0177
    ChrTalk(
        0x101,
        "#00008F#6P#30W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xC,
        (
            "#00306F#5P#30W……しまらねぇ話だろ？\x02\x03",

            "#00308F別に、そいつが死んだショックで\x01",
            "戦場から足を洗ったわけじゃねぇ。\x02\x03",

            "猟兵としての生き方に\x01",
            "ウンザリしたわけでもねぇ。\x02\x03",

            "#00303F俺はただ……\x01",
            "分からなくなっちまったんだ。\x02\x03",

            "いつか自分の店を持ちたいっていう\x01",
            "あいつのささやかな夢と……\x02\x03",

            "いずれ《闘神》となって\x01",
            "死ぬまで戦い続ける俺の人生の……\x02\x03",

            "#00311F果たしてどちらに意味があったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        "#00001F#6P#30W……ランディ………\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xC,
        (
            "#00303F#5P#30W多分それが……\x01",
            "俺が背負った“業#2Rごう#”なんだろう。\x02\x03",

            "オルランドの一族に生まれながら\x01",
            "修羅になりきれず、中途半端に\x01",
            "戦場に生きてきた俺自身のな。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        "#00008F#6P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0182
    ChrTalk(
        0x101,
        (
            "#00006F#6Pランディは、その“業#2Rごう#”を\x01",
            "断ち切るつもりなんだな……？\x02\x03",

            "#00001Fあの叔父さんを乗り越えることで。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xC,
        (
            "#00306F#5P……まあな。\x02\x03",

            "#00308F親父が死んだ今、それ以外に\x01",
            "俺が“業”を断ち切る方法はない。\x02\x03",

            "今の俺自身の力と足場をもって\x01",
            "あの化物を乗り越えられたら……\x02\x03",

            "#00300Fその時にやっと、３年前のケリを\x01",
            "付けられそうな気がするんだ。\x02\x03",

            "#00304Fこれ以上──\x01",
            "ただ流されることなくな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F29")

    #C0184
    ChrTalk(
        0x101,
        (
            "#00004F#6P……そっか……\x02\x03",

            "#00000F当然、相棒としては\x01",
            "協力させてくれるんだろうな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F8F")

    label("loc_6F29")


    #C0185
    ChrTalk(
        0x101,
        (
            "#00004F#6P……そっか……\x02\x03",

            "#00000Fそんな風に話してくれたって事は\x01",
            "当然、協力させてくれるんだよな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F8F")

    TurnDirection(0xC, 0x101, 400)
    Sleep(250)

    #C0186
    ChrTalk(
        0xC,
        (
            "#00302F#11Pああ、よろしく頼む。\x02\x03",

            "#00306F出来れば一人でケリを付けたかったが\x01",
            "さすがに相手が悪すぎる。\x02\x03",

            "#00300F悪ぃがアテにさせてもらうぜ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_709B")

    #C0187
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、もちろんさ。\x02\x03",

            "#00002F相棒冥利に尽きるというか……\x01",
            "頼りにしてくれて嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FD")

    label("loc_709B")


    #C0188
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、もちろんさ。\x02\x03",

            "#00002F仲間冥利に尽きるというか……\x01",
            "頼りにしてくれて嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70FD")


    #C0189
    ChrTalk(
        0xC,
        (
            "#00315F#11Pクク……だからタラシなこと\x01",
            "言ってんじゃねぇっての。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0190
    ChrTalk(
        0x101,
        "#00005F#6Pへ……？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Fade(1000)
    SetChrPos(0x101, -600, 0, -3750, 90)
    SetChrPos(0xC, 600, 0, -3750, 270)
    OP_68(0, 1000, -3750, 0)
    MoveCamera(135, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    MoveCamera(140, 15, 0, 70000)
    SetCameraDistance(9000, 70000)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x1)
    OP_0D()
    Sound(802, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x4, 0x1, 0x2, 0x2, 0x2)
    Sound(854, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x4, 0x2, 0x3, 0x3, 0x3)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0xC, 0x4)
    OP_0D()
    Sleep(300)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(500)

    #A0191
    AnonymousTalk(
        0x101,
        "#00005Fそれは……酒？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0192
    AnonymousTalk(
        0xC,
        (
            "#00304F#5Pラム酒だ、結構な上物でな。\x02\x03",

            "#00300Fあいつと一緒に、村の酒場で\x01",
            "ボトルキープしていたモンさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0193
    ChrTalk(
        0x101,
        "#00000F#12P……そうか………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(812, 0, 100, 0)
    Sound(857, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x5, 0x4, 0x5, 0x6, 0x6, 0x6)

    #C0194
    ChrTalk(
        0xC,
        (
            "#00300F#5Pライフルと一緒に預けてたが\x01",
            "何となく手が付けられなくてな。\x02\x03",

            "#00304Fだが、今ならやっと\x01",
            "残りを飲み干せそうな気がする。\x02\x03",

            "#00302F決戦前夜の景気付けだ。\x01",
            "一杯だけ、付き合わねぇか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    #C0195
    ChrTalk(
        0x101,
        "#00002F#12Pああ──いただくよ。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_741E():
        OP_A0(0xFE, 1000, 0x7, 0x8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_741E)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_7434():
        OP_A0(0xFE, 1000, 0x1, 0x2)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7434)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)
    Fade(250)
    Sound(855, 0, 100, 0)
    SetChrSubChip(0xC, 0x9)
    OP_0D()
    Sleep(1000)
    Sleep(1000)
    Fade(250)
    Sound(855, 0, 100, 0)
    SetChrSubChip(0xC, 0xA)
    SetChrSubChip(0x101, 0x4)
    OP_0D()
    Sleep(1000)
    Sleep(300)

    def lambda_7479():
        OP_A0(0xFE, 800, 0xA, 0xC)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7479)
    Sleep(100)

    def lambda_7489():
        OP_A0(0xFE, 1000, 0x4, 0x6)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7489)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)
    Sleep(300)

    #C0196
    ChrTalk(
        0xC,
        (
            "#00304F#5P……ちょうど空いたか。\x02\x03",

            "#00300F無理すんなよ？\x01",
            "少しだが結構キツいぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xC, 0x8)
    SetChrSubChip(0x101, 0x4)
    OP_0D()
    Sleep(150)

    #C0197
    ChrTalk(
        0x101,
        (
            "#00004F#12Pまあ、もう成人してるし\x01",
            "このくらいなら大丈夫さ。\x02\x03",

            "#00000F乾杯しよう、ランディ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xC,
        "#00302F#5Pああ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_7581():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7581)

    def lambda_759A():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_759A)
    Fade(250)
    SetChrSubChip(0x101, 0x7)
    SetChrSubChip(0xC, 0xD)
    Sleep(50)
    Sound(856, 0, 100, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0xC, 3)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0xC, 0xE)
    SetChrSubChip(0x101, 0x8)
    OP_0D()
    Sleep(1000)

    def lambda_75E6():
        OP_A0(0xFE, 1000, 0xE, 0x10)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_75E6)
    Sound(2030, 255, 60, 0)    #voice#Lloyd
    OP_A0(0x101, 1000, 0x9, 0xB)
    OP_A0(0x101, 1000, 0x9, 0xB)
    OP_A0(0x101, 1000, 0x9, 0xB)
    WaitChrThread(0xC, 3)
    OP_A1(0xC, 0x3E8, 0x8, 0x10, 0x11, 0x12, 0x12, 0x13, 0x14, 0x13, 0x12)
    OP_A0(0x101, 1000, 0x9, 0xB)

    #C0199
    ChrTalk(
        0x101,
        (
            "#00015F#12P#40Wケホッ……\x02\x01",

            "#00008F#30W……結構くるな……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xC,
        (
            "#00309F#5Pハハ、言わんこっちゃない。\x02\x03",

            "#00302Fまあそいつが\x01",
            "大人の味ってヤツだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_76BC():
        OP_A0(0xFE, 1000, 0x15, 0x16)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_76BC)

    def lambda_76C9():
        OP_A0(0xFE, 1000, 0xC, 0xD)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_76C9)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)

    #C0201
    ChrTalk(
        0x101,
        (
            "#00013F#12Pぐっ……だから自分だけ\x01",
            "大人面するなってば。\x02\x03",

            "#00004F──なあ、ランディ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xC,
        "#00305F#5Pん、なんだ？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(802, 0, 80, 0)
    OP_A0(0x101, 1000, 0xD, 0xE)
    Sleep(300)

    #C0203
    ChrTalk(
        0x101,
        (
            "#00002F#12P事件が一段落付いたら\x01",
            "裏通りのジャズバーに行こう。\x02\x03",

            "そこで、新しい酒を\x01",
            "ボトルキープしないか？\x02\x03",

            "#00012Fできればもう少し、\x01",
            "おとなしめのヤツをさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1950, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x8, 0x16, 0x17, 0x18, 0x18, 0x19, 0x1A, 0x19, 0x18)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0204
    ChrTalk(
        0xC,
        "#00302F#2781V#5P#40Wハハ……そうだな。\x02",
    )

    CloseMessageWindow()
    OP_24(0xADD)
    OP_57(0x0)
    OP_5A()
    OP_A1(0xC, 0x3E8, 0x3, 0x18, 0x19, 0x1A)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0205
    ChrTalk(
        0xC,
        "#00315F#2782V#5P#40Wああ──繰り出すとすっか！\x02",
    )

    CloseMessageWindow()
    OP_24(0xADE)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(10500, 3000)
    FadeToDark(2000, 0, -1)
    OP_A1(0xC, 0x3E8, 0x3, 0x1A, 0x19, 0x18)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x1194)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_7907")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_7907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7919")
    Jump("loc_79D9")

    label("loc_7919")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0206
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ロイドとランディは\x01",
            "バーニングレイジⅢを習得した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0207
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとランディのコンビクラフト、\x01",
            "バーニングレイジが強化されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x3, 0x1B0)
    AddCraft(0x0, 0x1B0)

    label("loc_79D9")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x2A, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 3)
    OP_29(0xB1, 0x1, 0x3)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_56EE end

    def Function_14_79FC(): pass

    label("Function_14_79FC")

    OP_95(0x101, -500, 0, -3750, 1000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_14_79FC end

    def Function_15_7A18(): pass

    label("Function_15_7A18")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    LoadChrToIndex("apl/ch51020.itc", 0x1F)
    LoadChrToIndex("apl/ch51806.itc", 0x20)
    LoadChrToIndex("apl/ch51807.itc", 0x21)
    SoundLoad(3532)
    SoundLoad(3533)
    SoundLoad(3534)
    SoundLoad(3535)
    SoundLoad(4110)
    SoundLoad(3536)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis337.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis338.itp")
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xD, 500, 0, -3750, 180)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(135, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(135, 10, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    BeginChrThread(0xF, 1, 0, 8)
    OP_C9(0x0, 0x80000000)

    #C0208
    ChrTalk(
        0xD,
        (
            "#10106F#3532V#40W……はぁ………\x01",
            "…………どうしよう………\x02\x03",

            "#10108Fこんな時に…#800W…\x01",
            "#10101F#40Wううん、でもこれを逃がしたら……！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDCD)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0xD, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(19500, 2000)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_7CAA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7CAA)

    def lambda_7CBF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7CBF)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)

    #C0209
    ChrTalk(
        0x101,
        "#00002F#5Pノエル、先に来てたのか。\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xD, 0x0, 1850, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7D30():

        label("loc_7D30")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_7D30")

    QueueWorkItem2(0xD, 2, lambda_7D30)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0210
    ChrTalk(
        0xD,
        (
            "#10112F#3534V#12P#40Wロ、ロイドさん！\x01",
            "お疲れさまですっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDCE)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(35, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15500, 3000)

    def lambda_7DC0():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DC0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xD, 500)
    EndChrThread(0xD, 0x2)
    OP_6F(0x79)

    #C0211
    ChrTalk(
        0x101,
        (
            "#00004F#6Pはは、そっちこそお疲れ。\x02\x03",

            "#00000Fソーニャ司令との連絡も\x01",
            "済ませてくれたみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0212
    AnonymousTalk(
        0xD,
        (
            "#30Wあ、はい。\x02\x03",

            "連絡通り、明日の作戦では\x01",
            "ベルガード門・タングラム門の部隊を\x01",
            "昼過ぎまで待機させてくれるそうです。\x02\x03",

            "それを過ぎるとさすがに\x01",
            "介入せざるを得ないそうですが……\x02",
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

    #C0213
    ChrTalk(
        0x101,
        (
            "#00006F#6Pそうか……まあ一時的に\x01",
            "待機してくれるだけでも助かるよ。\x02\x03",

            "#00013Fそうなると、俺たちの役割が\x01",
            "ますます重要になりそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xD,
        (
            "#10103F#11Pはい……\x02\x03",

            "#10108F#30W…………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        (
            "#00003F#6P……たぶん市内の国防軍は\x01",
            "都市防衛に回されるはずだ。\x02\x03",

            "#00001F市街地で国防軍とやり合うのは\x01",
            "何とか避けられると思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xD,
        (
            "#10106F#11Pいえ、それについては\x01",
            "もう覚悟は済ませています。\x02\x03",

            "#10108Fただ、ちょっと自分が\x01",
            "情けないなと思って……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x101,
        "#00005F#6Pへ……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -500, 0, -3750, 90)
    SetChrPos(0xD, 500, 0, -3750, 270)
    OP_68(250, 1000, -4400, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 1000, -3750, 50000)
    MoveCamera(135, 20, 0, 50000)
    OP_6E(800, 50000)
    SetCameraDistance(10000, 50000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    #C0218
    ChrTalk(
        0xD,
        (
            "#10108F#5P#30W本当は、独立国や国防軍なんて\x01",
            "間違っていると思っていたんです。\x02\x03",

            "#10106Fでもあたしは……ミレイユ先輩のように\x01",
            "レジスタンスに身を投じる気概もなく、\x01",
            "ただ大きな流れに従うだけで……\x02\x03",

            "自分がいかに、警備隊っていう\x01",
            "狭い世界でしか生きてなかったかって\x01",
            "思い知らされました。\x02\x03",

            "#10113Fせっかく支援課に出向する機会を\x01",
            "司令がくださったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        (
            "#00006F#12Pそれは……誰だって同じさ。\x02\x03",

            "#00008F俺だって、キーアやみんなの事がなければ\x01",
            "大きな流れに逆らえなかったと思う。\x02\x03",

            "#00012F元々、大それたことが\x01",
            "出来るような性格じゃないしね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0220
    ChrTalk(
        0xD,
        (
            "#10112F#5Pえっと……\x01",
            "とてもそうは思えないんですが。\x02\x03",

            "#10114Fそうじゃなかったら\x01",
            "『君は俺がもらう』なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        "#00005F#12Pえ？\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0222
    ChrTalk(
        0xD,
        (
            "#10112F#5Pい、いえ！\x01",
            "何でもありません！\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#00000F#12P？？？\x02\x03",

            "#00004Fいずれにしても、大切なのは\x01",
            "きっかけがあるかどうかだと思う。\x02\x03",

            "そして君は、そのきっかけを掴んで\x01",
            "俺たちと共にいてくれている。\x02\x03",

            "#00008Fそれが正しい事なのかどうかは\x01",
            "俺が決めるわけにはいかないけど……\x02\x03",

            "#00002Fすごく助かっているし、\x01",
            "──何よりも嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0224
    ChrTalk(
        0xD,
        (
            "#10114F#5Pロ、ロイドさん……\x02\x03",

            "#10106F～～～っ～～～……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x258)
    Sleep(500)

    #C0225
    ChrTalk(
        0xD,
        (
            "#10108F#11P#30W（お、落ち着いて\x01",
            "  ノエル・シーカー……！）\x02\x03",

            "#10103F（演習の時みたいに\x01",
            "  迅速かつ的確な状況判断と\x01",
            "  士気のコントロールを……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0226
    ChrTalk(
        0x101,
        (
            "#00005F#12Pそういえば、何か俺に\x01",
            "頼みがあるって言ってたけど……\x02\x03",

            "#00002Fえっと、何なのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xD, 0x101, 500)

    #C0227
    ChrTalk(
        0xD,
        (
            "#10105F#5Pあ、はい！\x01",
            "それなんですけど──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    #C0228
    ChrTalk(
        0xD,
        (
            "#10106F#5P……その……えっと……\x02\x03",

            "#10108F変なことを聞きますけど\x01",
            "ロイドさんって……\x02\x03",

            "#10101Fお、お付き合いしている人が\x01",
            "いたりしますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0229
    ChrTalk(
        0x101,
        "#00005F#12Pえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xD,
        (
            "#10112F#5Pい、いえ！\x01",
            "深い意味とかじゃなくて！\x02\x03",

            "#10102Fその、そうだ、フランと\x01",
            "どうなのかなっ～て話してて！\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        (
            "#00011F#12Pあ、ああ、なるほど。\x02\x03",

            "#00012Fハハ、そういう話、\x01",
            "女の子は好きそうだもんな。\x02\x03",

            "#00006Fうーん、残念ながら今はいないよ。\x02\x03",

            "#00000F周りに良い子が一杯いるのに\x01",
            "ちょっと不甲斐ないけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xD,
        (
            "#10112F#5P#30Wあ、あはは……そんな。\x01",
            "（ワザとじゃないよね……？）\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(1200)

    #C0233
    ChrTalk(
        0xD,
        "#10103F#5P#30Wコホン……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xD, 500, 0, -4250, 270)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(30, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16500, 2000)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)
    OP_68(0, 1000, -4250, 70000)
    MoveCamera(35, 20, 0, 70000)
    OP_6E(500, 70000)
    SetCameraDistance(14500, 70000)
    OP_C9(0x0, 0x80000000)

    #C0234
    ChrTalk(
        0xD,
        "#10103F#3535V#11P#40W──あの、でしたら。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xD, 0x1)
    OP_0D()
    Sleep(300)

    #C0235
    ChrTalk(
        0xD,
        (
            "#10101F#4110V#11P#40Wこれをしばらく、\x01",
            "預かっていただけませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x100E)
    OP_C9(0x1, 0x80000000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)

    #A0236
    AnonymousTalk(
        0x101,
        (
            "#00005Fこれって……\x02\x03",

            "#00001Fクロスベル警備隊の認識タグかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0237
    AnonymousTalk(
        0xD,
        (
            "#10104F#11Pはい、国防軍に切り替わった時に\x01",
            "要らなくなったものですけど……\x02\x03",

            "#10100F何となく捨てられなくって\x01",
            "ずっと持っていたものなんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    #C0238
    ChrTalk(
        0x101,
        (
            "#00004F#6Pそっか……\x02\x03",

            "#00005Fでも、どうして俺に？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xD,
        (
            "#10106F#11P……正直、明日の作戦は\x01",
            "厳しいものになると思います。\x02\x03",

            "#10101Fもし、あたしに何かあった時に……\x02\x03",

            "#10112Fいえ──無事任務を遂行できるよう、\x01",
            "験#2Rげん#担ぎに持っていて欲しいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#00008F#6Pノエル……\x02\x03",

            "#00004F……分かった。\x01",
            "喜んで預からせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x2)
    OP_0D()
    Sleep(800)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(500)

    #C0241
    ChrTalk(
        0xD,
        (
            "#10109F#11Pほっ……\x01",
            "ありがとうございます！\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#00012F#6Pはは、別に礼を\x01",
            "言われるような事じゃないさ。\x02\x03",

            "#00008Fそれにノエルも俺たちと\x01",
            "一緒に行動するわけだし……\x02\x03",

            "#00000Fくれぐれも、ピンチの時に\x01",
            "自分一人が犠牲になろうだなんて\x01",
            "思わないでくれよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0243
    ChrTalk(
        0xD,
        "#10111F#11P#30Wど、どうして……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        (
            "#00006F#6Pそのくらい、分かるさ。\x02\x03",

            "#00001Fさっきも言ったように、\x01",
            "俺たちを捕まえた事については\x01",
            "全く気に病む必要はない。\x02\x03",

            "#00002Fあくまで支援課の仲間として\x01",
            "一緒に付いて来て欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xD,
        (
            "#10114F#11P#30W……ロイドさん……\x02\x03",

            "#10116Fぐすっ……\x01",
            "……はい、分かりました！\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        "#00009F#6Pはは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x2)
    OP_0D()
    Sleep(300)

    #C0247
    ChrTalk(
        0x101,
        (
            "#00000F#6Pしかし自分のタグを\x01",
            "誰かに預けるか……\x02\x03",

            "#00012Fハハ、何だか\x01",
            "恋人同士の習慣みたいだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0248
    ChrTalk(
        0xD,
        "#10114F#11Pっ……！\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x258)
    Sleep(300)

    def lambda_9142():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_9142)
    WaitChrThread(0xD, 2)
    Sleep(500)

    #C0249
    ChrTalk(
        0x101,
        "#00005F#6Pえ──\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xD,
        "#10106F#5P#40W……～～～っ～～～～……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        "#00001F#6Pノエル……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    Fade(250)
    Sound(812, 0, 60, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    OP_A1(0x101, 0x320, 0x7, 0x0, 0x1, 0x2, 0x1, 0x2, 0x1, 0x2)
    OP_0D()

    #C0252
    ChrTalk(
        0x101,
        (
            "#00011F#6Pえっと、その……\x02\x03",

            "#00012Fもしかしなくても、\x01",
            "そういう意味だったりする？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xD,
        "#10106F#5P#40W……………………（コクン）\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30Wそ、そっか……\x02\x03",

            "#00000F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(500)

    #C0255
    ChrTalk(
        0x101,
        (
            "#00006F#6Pその、返事になるかどうか\x01",
            "分からないけど……\x02\x03",

            "#00000Fこれを預かっててくれないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xD,
        "#10114F#5P#30Wえ……\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x10E, 0x1F4)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x3)
    OP_0D()
    Sleep(150)
    Sleep(300)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)

    #A0257
    AnonymousTalk(
        0xD,
        (
            "#10105F#11Pそれって……\x01",
            "……クロスベル警察の……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0258
    AnonymousTalk(
        0x101,
        (
            "#00002F#6P一応、現職の警察官だから\x01",
            "自分で身に付けておくべき物だけど……\x02\x03",

            "#00004Fこの事件が解決するまでは\x01",
            "ノエルに持っていて欲しいんだ。\x02\x03",

            "#00000Fその後に改めて……\x01",
            "俺の方から申し込ませて欲しい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)

    #C0259
    ChrTalk(
        0xD,
        "#10116F#11P#30W#2S……………あ…………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(500)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)
    OP_C9(0x0, 0x80000000)

    #C0260
    ChrTalk(
        0xD,
        "#10117F#3536V#11P#30Wはいっ──よろこんで！\x02",
    )

    CloseMessageWindow()
    OP_24(0xDD0)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(16000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    StopBGM(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_95B7")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_95B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95C9")
    Jump("loc_9685")

    label("loc_95C9")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0261
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ロイドとノエルは\x01",
            "ブレイブハーツⅡを習得した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0262
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとノエルのコンビクラフト、\x01",
            "《ブレイブハーツ》が強化されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x0, 0x1A0)
    AddCraft(0x8, 0x1A0)

    label("loc_9685")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x25, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 4)
    OP_29(0xB1, 0x1, 0x4)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_7A18 end

    def Function_16_96A8(): pass

    label("Function_16_96A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03100.itc", 0x1E)
    LoadChrToIndex("apl/ch51808.itc", 0x1F)
    LoadChrToIndex("apl/ch51813.itc", 0x20)
    SoundLoad(2926)
    SoundLoad(2927)
    SoundLoad(2928)
    SoundLoad(2929)
    SoundLoad(2930)
    SoundLoad(2430)
    SoundLoad(2431)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10401.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis325.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis349.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis326.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis327.itp")
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xE, 500, 0, -4250, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(18500, 2000)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_9875():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9875)

    def lambda_988A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_988A)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_C9(0x0, 0x80000000)

    #C0263
    ChrTalk(
        0xE,
        "#10402F#2926V#11P#30Wやあ、来たね。\x02",
    )

    CloseMessageWindow()
    OP_24(0xB6E)
    OP_C9(0x1, 0x80000000)

    #C0264
    ChrTalk(
        0x101,
        "#00000F#5Pああ……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xF, 1, 0, 8)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(45, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15500, 3000)

    def lambda_992A():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_992A)

    def lambda_9944():

        label("loc_9944")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9944")

    QueueWorkItem2(0xE, 2, lambda_9944)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xE, 500)
    EndChrThread(0xE, 0x2)
    OP_6F(0x79)

    #C0265
    ChrTalk(
        0x101,
        (
            "#00006F#6Pあんな風に思わせぶりに言われたら\x01",
            "来ざるを得ないと思うんだが。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0266
    AnonymousTalk(
        0xE,
        (
            "#2927V#30Wフフ、そんな風に言いながらも\x01",
            "律儀に来てくれる君が好きさ。\x02\x03",

            "#2928V愛していると言っても\x01",
            "過言じゃないくらいだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB70)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    #C0267
    ChrTalk(
        0x101,
        (
            "#00006F#6Pそういうのはいいから。\x02\x03",

            "#00001F……キーアについてだろう？\x01",
            "話を聞かせてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xE,
        "#10404F#11Pフフ、了解。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    SetChrPos(0x101, -920, 0, -3910, 90)
    SetChrPos(0xE, 500, 0, -3750, 270)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9500, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    OP_6F(0x79)
    SetCameraDistance(9000, 50000)

    #C0269
    ChrTalk(
        0xE,
        (
            "#10408F#5P本当は部外者には\x01",
            "話しちゃいけないんだけど……\x02\x03",

            "#10400F《零の至宝》の処遇については\x01",
            "どうやら教会は基本的に\x01",
            "ノータッチという形になりそうだ。\x02\x03",

            "#10403F──たとえこの事件が\x01",
            "どんな結末に終わったとしてもね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0270
    ChrTalk(
        0x101,
        "#00007F#11P本当か！？\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xE,
        (
            "#10406F#5Pああ、《蛇》の連中が撤退し、\x01",
            "オリジナルの至宝が失われている今、\x01",
            "積極的に介入できる根拠はない。\x02\x03",

            "#10400Fその意味で、僕らがキーアを\x01",
            "連れ去る選択も無くなったわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#00006F#11Pそうか……\x01",
            "知らせてくれてありがとう。\x02\x03",

            "#00005Fでも、ワジはこのまま\x01",
            "俺たちに協力して問題ないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xE,
        (
            "#10403F#5P《道化師》と第七柱は去ったけど、\x01",
            "第六柱の撤退は確認できていない。\x02\x03",

            "#10408Fそれに、あの人形たちを始め、\x01",
            "結社がクロイス家に供与した技術が\x01",
            "いまだ大きな影響を及ぼしている……\x02\x03",

            "#10400Fその影響が無くなるまでは\x01",
            "最低限の介入は続けるつもりさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x101,
        (
            "#00003F#11Pなるほど……\x02\x03",

            "#00001F……聞けば聞くほど\x01",
            "俺たちの常識から外れた争いが\x01",
            "繰り広げられているみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xE,
        (
            "#10404F#5Pフフ、君たちの住む世界とは\x01",
            "表と裏の関係にあたる世界の話さ。\x02\x03",

            "#10402Fそれと──僕にとっては\x01",
            "２年に及ぶクロスベル潜入任務の\x01",
            "締めくくりというのが大きいかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x101,
        (
            "#00011F#11Pそういえば……\x01",
            "ワジは１７歳だったよな。\x02\x03",

            "#00003F２年前ということは、\x01",
            "１５歳で任務に付いたわけで……\x02\x03",

            "#00001Fでも、《守護騎士》っていう\x01",
            "かなり重要な地位にいるんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xE,
        (
            "#10405F#5Pああ、《守護騎士》っていうのは\x01",
            "実績でなるものじゃないんだ。\x02\x03",

            "#10400F“印”が顕れた者しかなれないし、\x01",
            "なる事が運命付けられている……\x02\x03",

            "#10409Fまあ、そんなオカルティックで\x01",
            "いかがわしい立場ってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x101,
        (
            "#00006F#11P自分で言うなって……\x02\x03",

            "#00001F……でも“印”って、\x01",
            "ひょっとしてワジが戦闘中に\x01",
            "たまに見せることがある……？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xE,
        "#10404F#5Pああ……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x190)
    Fade(500)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xE, 500, 0, -4250, 180)
    OP_68(430, 1000, -4460, 0)
    OP_68(430, 1000, -4460, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    MoveCamera(40, 20, 0, 30000)
    OP_6E(500, 30000)
    SetCameraDistance(15000, 30000)
    OP_0D()
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    Sleep(500)

    #C0280
    ChrTalk(
        0xE,
        (
            "#10403F#5P#30W《聖痕#4Rスティグマ#》──\x01",
            "それがこの“印”の名前さ。\x02\x03",

            "#10408F魂に刻み込まれた刻印……\x01",
            "力の源泉にして忌むべきもの。\x02\x03",

            "#10400Fこれが僕に顕れたのは\x01",
            "今から７年くらい前のことさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        "#00005F#6P７年前……\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xE,
        (
            "#10404F#5P別にＤ∴Ｇ教団とは\x01",
            "全然関係のない話だけど……\x02\x03",

            "#10402F暇つぶしに聞くかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        (
            "#00003F#6Pそうだな……\x01",
            "差し支えなかったら、是非。\x02\x03",

            "#00000F考えてみれば、ワジの過去は\x01",
            "殆んど知らないも同然だし……\x02\x03",

            "#00012F性格や行動パターンは\x01",
            "大体分かってるつもりだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xE,
        "#10404F#5Pふふ……いいだろう。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    SetCameraDistance(15000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0285
    AnonymousTalk(
        0xE,
        (
            "#30W#3C──僕の生まれ故郷は\x01",
            "ゼムリア大陸のとある辺境でね。\x02\x03",

            "外界との接触が禁じられた\x01",
            "いわば“隠れ里”的な場所だった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7568", 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, 155, -1, -1)

    #A0286
    AnonymousTalk(
        0xE,
        (
            "#30W#3Cその里では、女神とは異なる\x01",
            "太古の《神》を祀っていてね……\x02\x03",

            "僕は幼い頃から《神》の声を聞く\x01",
            "《巫子》の役割を担ってきた。\x02\x03",

            "勿論、自発的にじゃなく、\x01",
            "物心ついた頃に勝手に選ばれてね。\x02\x03",

            "《神》の正体が、得体の知れない\x01",
            "太古の呪具であるのは知ってたから\x01",
            "正直、馬鹿馬鹿しくて仕方なかったよ。\x02\x03",

            "下らない役割から解放されて\x01",
            "自由になりたいとずっと思っていた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0287
    AnonymousTalk(
        0xE,
        (
            "#30W#3C……そのうちに里で\x01",
            "おかしな事が起こり始めてね。\x02\x03",

            "里人が一人、また一人と\x01",
            "原因不明の昏睡状態に陥ったんだ。\x02\x03",

            "僕が探ったところ、\x01",
            "《神》が暴走して、地脈を通じて\x01",
            "精気を吸い取り始めたことが判って……\x02\x03",

            "僕は封じることを主張したけど、\x01",
            "里の長老たちはそれを認めず、\x01",
            "生贄を奉げようとまで言い出したんだ。\x02\x03",

            "まあ実際、恐ろしい力を持った呪具で\x01",
            "封じることも不可能だったんだけど……\x02\x03",

            "──そんな時に外界から\x01",
            "教会の騎士たちがやってきたんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    SetMessageWindowPos(180, 160, -1, -1)

    #A0288
    AnonymousTalk(
        0xE,
        (
            "#30W#3C──彼らと接触した僕は\x01",
            "《神》が古代遺物#8Rアーティファクト#の一種だと知り……\x02\x03",

            "それが絶対的な存在でない事を知って\x01",
            "思い切った行動に出た。\x02\x03",

            "その蒼い石版状の《神》を\x01",
            "崖から落として破壊しようとしたんだ。\x02\x03",

            "太古の呪いから里を解放し、\x01",
            "自由になりたい──ただその一心で。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)
    SetMessageWindowPos(10, 150, -1, -1)

    #A0289
    AnonymousTalk(
        0xE,
        (
            "#30W#3Cしかし《神》の抵抗は凄まじく、\x01",
            "僕の力を根こそぎ奪い取ろうとした。\x02\x03",

            "騎士たちの助けも間に合わず、\x01",
            "僕の生命が尽きようとしたその時──\x02\x03",

            "その“刻印”は僕の胸に現れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    FadeToDark(2500, 16777215, -1)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_0D()
    OP_68(-360, 2100, -3950, 0)
    MoveCamera(150, -49, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(5667730, 0)
    Sleep(1500)
    FadeToBright(1500, 16777215)
    OP_0D()
    Sleep(800)
    FadeToDark(0, 0, -1)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0290
    AnonymousTalk(
        0xE,
        (
            "#30W#3C──僕の《聖痕》は\x01",
            "逆に《神》の力を根こそぎ奪い……\x02\x03",

            "《神》はただの古ぼけた石版と化し、\x01",
            "粉々に砕け散った。\x02\x03",

            "そして僕は自由を手に入れ──\x01",
            "めでたく里を追放されたわけさ。\x02\x03",

            "里人たちが崇めていた《神》を\x01",
            "“殺した”大罪人としてね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x1)
    OP_68(430, 1000, -4460, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(16000, 3000)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(150)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    OP_6F(0x79)
    MoveCamera(40, 20, 0, 50000)
    SetCameraDistance(16540, 50000)
    Sleep(300)

    #C0291
    ChrTalk(
        0x101,
        (
            "#00008F#6P#30W………そんな事が…………\x02\x03",

            "#00006F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xE,
        (
            "#10409F#5P#30Wフフ……\x01",
            "なかなか荒唐無稽な話だろ？\x02\x03",

            "#10400F都会育ちの現代っ子には\x01",
            "さすがに信じられないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        (
            "#00003F#6Pいや、ワジの力を見てると\x01",
            "現実にあったという事は判るさ。\x02\x03",

            "#00000Fツァイトなんていう生きた神話も\x01",
            "目の当たりにしてるしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xE,
        (
            "#10402F#5Pハハ、それもそうか。\x02\x03",

            "#10404Fそんな訳で、騎士たちに誘われた僕は\x01",
            "アルテリア法国へと向かい……\x02\x03",

            "１２名しかいない《聖痕》の持ち主、\x01",
            "《守護騎士#8Rド ミ ニ オ ン#》として迎えられた。\x02\x03",

            "#10400Fアッバスとは\x01",
            "その時からの付き合いかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#00008F#6Pそうか……\x02\x03",

            "#00006F……でも、そうすると、\x01",
            "故郷にずっと帰っていないのか？\x02\x03",

            "#00001F家族の人とも会わないで……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xE,
        (
            "#10405F#5P#30Wああ──当然だろう？\x02\x03",

            "#10403F里人たちの拠り所を\x01",
            "僕は粉々に砕いてしまったんだ。\x02\x03",

            "ただ自由になりたい一心で……\x01",
            "後のことを何も考えずに。\x02\x03",

            "#10400Fだからそれは、僕への罰なのさ。\x02\x03",

            "#10404F家族から憎まれるという事もね。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        "#00008F#6P#30W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xE,
        (
            "#10406F#5P#30Wまあ、聞いた話だと\x01",
            "あれから里には教会が入って\x01",
            "色々とケアをしているらしい。\x02\x03",

            "#10404F《神》の呪いもいずれは\x01",
            "過去のものとして薄れるはずだ。\x02\x03",

            "ほとぼりが冷めたくらいには\x01",
            "一度帰ろうとは思っているよ。\x02\x03",

            "#10402Fそんなに心配してくれなくてもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        "#00006F#6P#30Wワジ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    #C0300
    ChrTalk(
        0x101,
        (
            "#00008F#6Pこの事件が片付いたら……\x01",
            "ワジはクロスベルを去るんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xE,
        (
            "#10400F#5Pああ、それが僕の\x01",
            "騎士としての使命だからね。\x02\x03",

            "#10409Fフフ、何だい？\x01",
            "今から寂しくなっちゃうかい？\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    #C0302
    ChrTalk(
        0x101,
        "#00001F#6Pああ、そんなの当然だろう？\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x101, 400)
    Sleep(150)

    #C0303
    ChrTalk(
        0xE,
        "#10405F#11Pへ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    Fade(1000)
    SetChrPos(0x101, -920, 0, -3910, 90)
    SetChrPos(0xE, 500, 0, -3750, 270)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    Sleep(500)
    OP_6F(0x79)
    SetCameraDistance(9000, 30000)

    #C0304
    ChrTalk(
        0x101,
        (
            "#00003F#11P#30Wヴァルドはあんな風になったけど\x01",
            "きっと元に戻せるはずだ。\x02\x03",

            "テスタメンツのみんなだって\x01",
            "クロスベルに居るわけだし。\x02\x03",

            "#00008Fそして思惑があったとはいえ、\x01",
            "俺たちの仲間でいてくれた……\x02\x03",

            "#00000Fだから──\x01",
            "いつでも遊びにくるといい。\x02\x03",

            "#00009Fもうワジにとってクロスベルは\x01",
            "第２の故郷みたいなもんだろう？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrSubChip(0xE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    Sleep(150)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrSubChip(0xE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    Sleep(300)

    #C0305
    ChrTalk(
        0xE,
        "#10405F#5P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x2)
    OP_0D()

    def lambda_B5D4():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_B5D4)
    WaitChrThread(0xE, 2)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0306
    ChrTalk(
        0xE,
        "#10404F#2430V#5P#40W#25A……くくっ………\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetChrSubChip(0xE, 0x3)

    def lambda_B632():
        OP_A6(0xFE, 0x0, 0x1E, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_B632)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0307
    ChrTalk(
        0xE,
        "#10409F#2431V#50W#5P#4S#19Aアハハハハハハハハッ！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x2)
    OP_0D()
    Sleep(500)

    #C0308
    ChrTalk(
        0x101,
        (
            "#00006F#11P#30Wクサいのは承知してるよ。\x02\x03",

            "#00000Fでも、１００％本気だからな？\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xE,
        (
            "#10411F#5P#40W……フフ、分かった。\x01",
            "どうも君相手だと調子が狂うなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    OP_A0(0xE, 1000, 0x7, 0x5)
    OP_0D()
    Sleep(400)
    OP_C9(0x0, 0x80000000)

    #C0310
    ChrTalk(
        0xE,
        (
            "#10402F#2929V#5P#40W──里心が付いた時には\x01",
            "遠慮なく訪ねさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB71)
    Sleep(150)
    OP_A0(0xE, 1000, 0x5, 0x7)
    Sleep(400)
    OP_C9(0x0, 0x80000000)

    #C0311
    ChrTalk(
        0xE,
        (
            "#10404F#2930V#5P#40W故郷に戻れない代わりじゃなく、\x01",
            "君たちとの腐れ縁を確かめにね。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB72)
    OP_C9(0x1, 0x80000000)
    BlurSwitch(0x1770, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-360, 2100, -3950, 8000)
    MoveCamera(128, 27, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(40590, 8000)
    Sleep(500)
    OP_A0(0xE, 1000, 0x7, 0x5)
    Sleep(2500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    StopBGM(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_B8A8")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_B8A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B8BE")
    Jump("loc_B97A")

    label("loc_B8BE")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0312
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ロイドとワジは\x01",
            "ストライクヘヴンⅡを習得した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0313
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとワジのコンビクラフト、\x01",
            "《ストライクヘヴン》が強化されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x0, 0x1A1)
    AddCraft(0x4, 0x1A1)

    label("loc_B97A")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x26, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 5)
    OP_29(0xB1, 0x1, 0x5)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_96A8 end

    def Function_17_B99D(): pass

    label("Function_17_B99D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x40)
    LoadChrToIndex("chr/ch03200.itc", 0x1E)
    LoadChrToIndex("apl/ch51809.itc", 0x1F)
    LoadChrToIndex("apl/ch51810.itc", 0x20)
    SoundLoad(3265)
    SoundLoad(3266)
    SoundLoad(3267)
    SoundLoad(3268)
    SoundLoad(3269)
    SoundLoad(3270)
    SoundLoad(2634)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10701.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis321.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis322.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis323.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis324.itp")
    EndChrThread(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, -250, 120, 2750, 180)
    SetChrPos(0x8, 500, 0, -3750, 180)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(125, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8000, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(115, 15, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    Sound(100, 0, 100, 0)
    Sleep(800)

    #C0314
    ChrTalk(
        0x101,
        "#00002F#6P#30W#N……すごい満月だな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()

    def lambda_BBD5():

        label("loc_BBD5")

        TurnDirection(0xFE, 0x101, 400)
        Yield()
        Jump("loc_BBD5")

    QueueWorkItem2(0x8, 2, lambda_BBD5)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0315
    AnonymousTalk(
        0x8,
        "#3265V#11P#40Wロイドさん……\x02",
    )

    CloseMessageWindow()
    OP_24(0xCC1)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    BeginChrThread(0xF, 1, 0, 8)
    OP_68(0, 1000, -4200, 4500)
    MoveCamera(130, 20, 0, 4500)
    OP_6E(800, 4500)
    SetCameraDistance(10000, 4500)
    Sound(100, 0, 100, 0)

    def lambda_BCC9():
        OP_95(0xFE, -500, 0, -3750, 1600, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BCC9)
    WaitChrThread(0x101, 1)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)
    SetCameraDistance(9500, 30000)
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0316
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30Wなんだか、君と話す時は\x01",
            "いつも月が綺麗な気がする。\x02\x03",

            "#00002Fやっぱり《月の姫》を\x01",
            "演じているだけはあるのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0317
    ChrTalk(
        0x8,
        "#10709F#2634V#5P#30Wふふっ……\x02",
    )

    CloseMessageWindow()
    OP_24(0xA4A)
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0xB4, 0x190)
    Sleep(500)

    #C0318
    ChrTalk(
        0x8,
        (
            "#10704F#3266V#40W#5P月は、光にして影……\x02\x03",

            "#3267V多分それは、私という存在が\x01",
            "月に似ているからだと思います。\x02\x03",

            "#10708F#3268V本来は陽のあたる場所に\x01",
            "出てくるはずのなかった存在……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCC4)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0319
    ChrTalk(
        0x101,
        (
            "#00003F#12P#30Wでも君は、このクロスベルで\x01",
            "光を掴むことが出来た……\x02\x03",

            "#00001Fそれは確かだろう？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    OP_A1(0x8, 0x3E8, 0x5, 0x2, 0x25, 0x26, 0x25, 0x2)
    OP_0D()

    #C0320
    ChrTalk(
        0x8,
        (
            "#10704F#5P#30Wはい、もうその事を\x01",
            "否定するつもりはありません。\x02\x03",

            "#10708Fですが私は……\x01",
            "……私という存在を作った流れは\x01",
            "深く底知れないものがあります。\x02\x03",

            "#10711F《銀#2Rイン#》という一子相伝の流れ……\x02\x03",

            "#10703F父から受け継いだ密やかな道は。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        "#00008F#12P#30W前もそんな事を言ってたな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    #C0322
    ChrTalk(
        0x101,
        (
            "#00003F#12P#30W……差し支えなければ\x01",
            "聞かせてもらえないか？\x02\x03",

            "#00008Fクロスベルに来るまでの君を。\x02\x03",

            "#00001F俺の知らない、リーシャ・マオを。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x8,
        (
            "#10704F#5P#30W……はい。\x02\x03",

            "#10710F何となく、ロイドさんには\x01",
            "いずれ話す事になるような\x01",
            "気がしていました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()
    OP_93(0x8, 0xB4, 0x12C)
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    Sleep(800)
    OP_63(0x8, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(500)

    #C0324
    ChrTalk(
        0x8,
        (
            "#10708F#5P#30W──気付いた時には\x01",
            "私は父と共に在りました。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(9000, 2500)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0325
    AnonymousTalk(
        0x8,
        (
            "#30W#3C──母の記憶はありません。\x02\x03",

            "多分、《銀》の道を\x01",
            "私に受け継がせるために\x01",
            "父が遠ざけたのだと思います。\x02\x03",

            "ですが私にとってはそれが普通で……\x02\x03",

            "過酷な鍛錬も、暗器や符術の修練も\x01",
            "淡々とこなしていただけでした。\x02\x03",

            "各地を点々としながら、日曜学校に通い、\x01",
            "人と接する術もそこで得ました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(260, 160, -1, -1)

    #A0326
    AnonymousTalk(
        0x8,
        (
            "#30W#3C父は厳しくも優しくもなく、\x01",
            "ただひたすら教えるだけでした。\x02\x03",

            "それというのも、《銀》として\x01",
            "受け継ぐことが膨大すぎたからです。\x02\x03",

            "それは代々の《銀》の記憶……\x02\x03",

            "どのような状況でどんな工作を行い、\x01",
            "どんな標的をどのように仕留めたか……\x02\x03",

            "時代を通して同じ存在であるため、\x01",
            "その全てのあらましを\x01",
            "受け継ぐ必要があったんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0327
    AnonymousTalk(
        0x8,
        (
            "#30W#3C全てを受け継いだ時……\x01",
            "私は《銀》そのものになりました。\x02\x03",

            "といっても、父が存命である限りは\x01",
            "《銀》になることはありません。\x02\x03",

            "《銀》はただ一人……\x01",
            "それは変わる事がないからです。\x02\x03",

            "しばらくの間、父の帰りを待ちながら\x01",
            "穏やかに過ごす日々が続きました。\x02\x03",

            "そして、父が帰ってきたら\x01",
            "いつ《銀》を継いでも問題ないように\x01",
            "仕事のあらましを教えてもらう……\x02\x03",

            "既に表の顔は持っていましたが\x01",
            "それが私にとって世界の全てでした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(800)
    SetMessageWindowPos(20, 160, -1, -1)

    #A0328
    AnonymousTalk(
        0x8,
        (
            "#30W#3C──その世界が崩れたのは\x01",
            "父が不治の病に倒れてからです。\x02\x03",

            "代々の《銀》の中でも\x01",
            "卓越した力を持った父でしたが……\x01",
            "病魔からは逃れられませんでした。\x02\x03",

            "さりとて抗うこともせず、\x01",
            "延命のための手術も受けず……\x02\x03",

            "ある日、私を呼んで命じました。\x02\x03",

            "自分を殺して《銀》を継ぐようにと。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0329
    AnonymousTalk(
        0x8,
        (
            "#30W#3C──出来ませんでした。\x02\x03",

            "およそ、父の言うことに\x01",
            "逆らうことのなかった私でしたが\x01",
            "それだけは何故か出来ませんでした。\x02\x03",

            "……私は初めて恐くなりました。\x02\x03",

            "あれだけ父が丹念に仕上げた《銀#2Rわたし#》が\x01",
            "出来損ないだったのではないかと。\x02\x03",

            "死にゆく父を失望させたのではないかと。\x02\x03",

            "……懊悩#4Rおうのう#する私に\x01",
            "父はふと苦笑して言いました。\x02\x03",

            "『──それもまたお前だ』\x02\x03",

            "『お前の銀はお前が決めるがいい』\x02\x03",

            "……そして一月後、父は世を去りました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(800)
    SetMessageWindowPos(260, 160, -1, -1)

    #A0330
    AnonymousTalk(
        0x8,
        (
            "#30W#3Cそして私は《銀》となりました。\x02\x03",

            "父の持っていたコネクションを継ぎ、\x01",
            "黒衣と内功で体型を誤魔化し……\x02\x03",

            "父の腕には及びませんでしたが\x01",
            "滞りなく仕事を再開できました。\x02\x03",

            "『お前の銀はお前が決めるがいい』\x02\x03",

            "父の言葉の意味も分からぬまま、\x01",
            "ただ淡々と流されるようにして……\x02\x03",

            "──そして２年が過ぎ、\x01",
            "私は黒月と長期契約を結びました。\x02\x03",

            "カルバードの西端……\x01",
            "貿易都市クロスベルの覇権奪取に\x01",
            "協力するという契約を。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(1000)
    SetMessageWindowPos(250, 160, -1, -1)

    #A0331
    AnonymousTalk(
        0x8,
        (
            "#30W#3Cクロスベルに到着した私は\x01",
            "戦いに備え、街の下見をする最中、\x01",
            "歓楽街でとある劇場に入りました。\x02\x03",

            "そこでは丁度、公開練習というものが\x01",
            "行われていて……\x02\x03",

            "……そこから先は\x01",
            "ロイドさんもご存知の通りです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    FadeToBright(2000, 0)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    OP_6F(0x79)
    SetCameraDistance(9000, 40000)
    Sleep(300)

    #C0332
    ChrTalk(
        0x101,
        (
            "#00006F#11P#30W……そっか……\x02\x03",

            "#00000Fその時に、イリアさんに\x01",
            "目を付けられたってわけだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x8,
        (
            "#10702F#5P#30Wふふ、最初は理由を付けて\x01",
            "何とか入団を断ろうとしたんです。\x02\x03",

            "#10704Fでもイリアさんは凄く強引で……\x02\x03",

            "とうとう根負けして\x01",
            "入ることになってしまいました。\x02\x03",

            "体力と偽装には自信がありましたし、\x01",
            "いい隠れ蓑になると思ったんです。\x02\x03",

            "#10710F……予想以上に練習がハードで\x01",
            "《銀》との両立が大変でしたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#00012F#11P#30Wはは……\x02\x03",

            "#00004F──ありがとう、リーシャ。\x02\x03",

            "#00000F聞かせてくれて嬉しかった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)

    #C0335
    ChrTalk(
        0x8,
        (
            "#10704F#5P#30Wふふ、聞いていて面白い話では\x01",
            "無かったと思いますけど……\x02\x03",

            "#10703Fでもこれが──父と祖先から\x01",
            "私に受け継がれた“道”です。\x02\x03",

            "#10708Fアルカンシェルという光を\x01",
            "手に入れたとしても……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    OP_A0(0x8, 1000, 0x2, 0x5)
    OP_0D()
    Sleep(300)

    #C0336
    ChrTalk(
        0x8,
        (
            "#10704F#5P#30Wその“道”を完全に捨てることは\x01",
            "多分私には出来ないと思います。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    #C0337
    ChrTalk(
        0x101,
        (
            "#00003F#11P#30Wそうか……\x02\x03",

            "#00008F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    Fade(1000)
    SetChrSubChip(0x8, 0x6)
    SetChrPos(0x101, -1000, 0, -4250, 90)
    SetChrPos(0x8, 0, 0, -4250, 270)
    OP_68(-300, 1000, -4250, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(-300, 1000, -4250, 50000)
    MoveCamera(45, 15, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(15500, 50000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7575", 0)
    Sleep(500)

    #C0338
    ChrTalk(
        0x101,
        "#00003F#6P#30W『お前の銀はお前が決めるがいい』\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x3E8, 0x5, 0x6, 0x29, 0x2A, 0x29, 0x6)

    #C0339
    ChrTalk(
        0x8,
        "#10712F#11P#30W…………え……………\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W……《銀》は全てを受け継ぐ。\x02\x03",

            "アルカンシェルという光を\x01",
            "君が見出してしまった以上……\x02\x03",

            "#00002F《銀》もまた、光という側面を\x01",
            "受け入れざるを得ないんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x8,
        "#10717F#11P#30Wそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#00006F#6P#30Wどんなものも時代が変われば\x01",
            "在り方も変わる……\x02\x03",

            "#00003Fいや、変わらざるを得ないんだ。\x02\x03",

            "#00008Fそうして人の歴史は受け継がれ、\x01",
            "前に進んでいく……\x02\x03",

            "#00001F多分、そういう事も含めて\x01",
            "お父さんは言ったんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x8,
        "#10708F#11P#30W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W警察官として犯罪行為を\x01",
            "勧めることは出来ないけど……\x02\x03",

            "それでも君は、君の《銀》を\x01",
            "目指せばいいんだと思う。\x02\x03",

            "#00000Fあるいは、ここで《銀》という存在を\x01",
            "完全に断ち切るのも一つの道だろう。\x02\x03",

            "#00002Fそうなったとしても多分……\x01",
            "お父さんは気にしないんじゃないかな？\x02\x03",

            "#00009F『──それもまたお前だ』って苦笑して。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x8,
        "#10717F#11P#40W#2S…………ぁ………………\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W……いいお父さんじゃないか。\x02\x03",

            "#00008F普通の家族とはちょっと違うけど\x01",
            "ちゃんと娘を愛していた……\x02\x03",

            "#00002Fそんな風に俺には思えるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        "#10718F#11P#50W………お父……さん…………\x02",
    )

    CloseMessageWindow()
    OP_68(-100, 1000, -4250, 1200)
    SetChrFlags(0x8, 0x20)

    def lambda_D590():
        OP_A0(0xFE, 1000, 0x6, 0x9)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_D590)
    OP_96(0x8, 0x96, 0x0, 0xFFFFEF66, 0x1F4, 0x0)
    Sound(812, 0, 60, 0)
    ClearChrFlags(0x8, 0x20)
    OP_A0(0x8, 1000, 0x18, 0x1A)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A1(0x8, 0x3E8, 0x6, 0x1A, 0x1E, 0x1F, 0x20, 0x21, 0x22)
    OP_A0(0x8, 1000, 0x18, 0x1A)
    OP_63(0x8, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(812, 0, 60, 0)
    OP_A0(0x8, 1000, 0xA, 0xC)
    Sleep(300)

    #C0348
    ChrTalk(
        0x8,
        (
            "#10719F#11P#50Wどう……して……\x02\x03",

            "……お父さんが亡くなった時も……\x01",
            "こんな……\x02\x03",

            "#10720F………涙なんて……\x01",
            "ぜんぜん零れなかったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W多分、イリアさんたちとの日々で\x01",
            "君もまた変わっていったんだ……\x02\x03",

            "#00008Fこれから先、君がどんな道を進むか\x01",
            "分からないけれど……\x02\x03",

            "#00000Fできれば俺も、お父さんの代わりに\x01",
            "見守らせてもらうよ。\x02\x03",

            "#00002F光を掴んだ君が、\x01",
            "どう変わっていくのかをね。\x02",
        )
    )

    CloseMessageWindow()
    OP_A0(0x8, 1000, 0xC, 0xF)
    Sleep(300)

    #C0350
    ChrTalk(
        0x8,
        "#10718F#11P#50W……ロイドさん……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(1000)
    OP_68(100, 1000, -4250, 1200)
    SetCameraDistance(15000, 1200)
    OP_9A(0x101, 0x8, 0x1F4, 0x258, 0x0)
    Sleep(300)
    Fade(250)
    Sound(898, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_D81E():
        OP_A0(0xFE, 1000, 0x14, 0x16)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_D81E)

    def lambda_D82B():
        OP_A0(0xFE, 1000, 0x5, 0x7)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D82B)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x101, 3)
    OP_0D()
    MoveCamera(44, 23, 0, 15000)
    SetCameraDistance(70000, 15000)
    OP_C9(0x0, 0x80000000)

    #C0351
    ChrTalk(
        0x8,
        "#10720F#11P#3269V#70W#53A……うう……ああっ………\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(1000)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0352
    ChrTalk(
        0x8,
        "#10713F#11P#3270V#90W#30A#4S…………あああああっ…………！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x1770)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_D927")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_D927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D939")
    Jump("loc_D9F3")

    label("loc_D939")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0353
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ロイドとリーシャは\x01",
            "真・比翼双竜撃を習得した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0354
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとリーシャのコンビクラフト、\x01",
            "《比翼双竜撃》が強化されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x5, 0x1A9)
    AddCraft(0x0, 0x1A9)

    label("loc_D9F3")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x27, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 6)
    OP_29(0xB1, 0x1, 0x6)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_B99D end

    def Function_18_DA16(): pass

    label("Function_18_DA16")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DA30")
    OP_A0(0xFE, 1000, 0x10, 0x12)
    Sleep(300)
    Jump("Function_18_DA16")

    label("loc_DA30")

    Return()

    # Function_18_DA16 end

    SaveToFile()

Try(main)
