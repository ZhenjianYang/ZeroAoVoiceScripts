from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t5000.bin",                # FileName
        "t5000",                    # MapName
        "t5000",                    # Location
        0x0000,                     # MapIndex
        "ed7102",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x27,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "t5000",                  # 0
        "ケビン神父",             # 1
        "シスター服の娘",         # 2
        "ダドリーの車",           # 3
        "車",                     # 4
        "車",                     # 5
        "市民",                   # 6
        "市民",                   # 7
        "市民",                   # 8
        "市民",                   # 9
        "市民",                   # 10
        "市民",                   # 11
        "市民",                   # 12
        "市民",                   # 13
        "市民",                   # 14
        "共和国バス",             # 15
        "護送車",                 # 16
        "偽ブランド商",           # 17
        "共和国軍人",             # 18
        "共和国軍人",             # 19
        "黒月構成員",             # 20
        "黒月構成員",             # 21
        "SE制御",                 # 22
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(836, 0)                                        # 0

    ScpFunction((
        "Function_0_344",          # 00, 0
        "Function_1_3F4",          # 01, 1
        "Function_2_418",          # 02, 2
        "Function_3_419",          # 03, 3
        "Function_4_2753",         # 04, 4
        "Function_5_27E3",         # 05, 5
        "Function_6_2817",         # 06, 6
        "Function_7_286F",         # 07, 7
        "Function_8_28EF",         # 08, 8
        "Function_9_2929",         # 09, 9
        "Function_10_2970",        # 0A, 10
        "Function_11_29CB",        # 0B, 11
        "Function_12_2A2C",        # 0C, 12
        "Function_13_2A48",        # 0D, 13
        "Function_14_3B58",        # 0E, 14
        "Function_15_3C71",        # 0F, 15
        "Function_16_3C9E",        # 10, 16
        "Function_17_3CD8",        # 11, 17
    ))


    def Function_0_344(): pass

    label("Function_0_344")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_37C"),
        (1, "loc_388"),
        (2, "loc_394"),
        (3, "loc_3A0"),
        (4, "loc_3AC"),
        (5, "loc_3B8"),
        (6, "loc_3C4"),
        (SWITCH_DEFAULT, "loc_3D0"),
    )


    label("loc_37C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_388")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_394")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3F3")

    Return()

    # Function_0_344 end

    def Function_1_3F4(): pass

    label("Function_1_3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_408")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)
    Jump("loc_417")

    label("loc_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_417")
    ClearScenarioFlags(0x22, 1)
    Event(0, 13)

    label("loc_417")

    Return()

    # Function_1_3F4 end

    def Function_2_418(): pass

    label("Function_2_418")

    Return()

    # Function_2_418 end

    def Function_3_419(): pass

    label("Function_3_419")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11400.itc", 0x1E)
    LoadChrToIndex("apl/ch51026.itc", 0x1F)
    LoadChrToIndex("chr/ch25600.itc", 0x20)
    LoadChrToIndex("chr/ch21102.itc", 0x21)
    LoadChrToIndex("chr/ch21302.itc", 0x22)
    LoadChrToIndex("chr/ch26000.itc", 0x23)
    LoadChrToIndex("chr/ch25000.itc", 0x24)
    LoadChrToIndex("chr/ch44200.itc", 0x25)
    LoadChrToIndex("chr/ch44100.itc", 0x26)
    LoadChrToIndex("chr/ch44000.itc", 0x27)
    LoadChrToIndex("chr/ch44400.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13800.itp")
    SetChrPos(0x101, 0, 0, 8400, 0)
    SetChrPos(0x109, -1300, 0, 8200, 0)
    SetChrPos(0x10A, -700, 0, 10900, 180)
    SetChrPos(0x108, 700, 0, 11200, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 1500, 0, 8200, 315)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    ClearChrFlags(0xA, 0x80)
    OP_78(0xA, 0xA)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 0, 0, 13500, 0)
    OP_D5(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x6, 0xB)
    OP_49()
    SetChrPos(0xB, 5000, 0, -3500, 0)
    OP_D5(0xB, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x6, 0x1000)
    ClearChrFlags(0xC, 0x80)
    OP_78(0x7, 0xC)
    OP_49()
    SetChrPos(0xC, -19000, 0, 2200, 0)
    OP_D5(0xC, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x9, 0x16)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x16, -35000, 0, 17500, 0)
    OP_D5(0x16, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x20)
    SetChrPos(0xD, 5800, 0, -5400, 225)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x2)
    SetChrPos(0xE, -2300, 50, -2750, 225)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x1)
    SetChrPos(0xF, -2950, 50, -2200, 225)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x23)
    SetChrPos(0x10, 14700, 0, -6400, 270)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x24)
    SetChrPos(0x11, -22200, 0, 900, 270)
    BeginChrThread(0x11, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x25)
    SetChrPos(0x12, 0, 0, -23000, 0)
    BeginChrThread(0x12, 1, 0, 6)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x26)
    SetChrPos(0x13, 21500, 180, 6000, 270)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x27)
    SetChrPos(0x14, 12000, 0, 9000, 0)
    BeginChrThread(0x14, 0, 0, 8)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x28)
    SetChrPos(0x15, -23500, 0, 900, 90)
    BeginChrThread(0x15, 0, 0, 0)
    OP_68(0, 1900, -21500, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(18000, 0)
    OP_68(0, 2000, 0, 8000)
    MoveCamera(30, 17, 0, 8000)
    SetCameraDistance(41000, 8000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    PlaceName2(100, 200, "c_plac35", 0x0, 0)
    Sleep(500)
    Sleep(1000)
    BeginChrThread(0x16, 0, 0, 4)
    BeginChrThread(0x16, 1, 0, 5)
    BeginChrThread(0x1D, 1, 0, 12)
    Sleep(2000)
    BeginChrThread(0x13, 0, 0, 7)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-11500, 1900, 7700, 0)
    MoveCamera(23, 27, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    WaitChrThread(0x16, 1)
    Sleep(1000)
    Fade(500)
    OP_68(0, 11000, 17800, 0)
    MoveCamera(31, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(26000, 0)
    OP_68(0, 5000, 17800, 7000)
    MoveCamera(39, 10, 0, 7000)
    SetCameraDistance(29000, 7000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1100, 9600, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x101,
        (
            "#12P#00004F──それではダドリーさん。\x01",
            "２人の護送はよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x10A,
        "#00600F#5Pああ、任せておけ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x8, 500)
    Sleep(300)

    #C0003
    ChrTalk(
        0x10A,
        (
            "#00603F#5P──ケビン神父。\x01",
            "礼を言わせてもらおう。\x02\x03",

            "#00600Fまあ、本当なら事前に、\x01",
            "警察#4Rこちら#に連絡して欲しかったが。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9BF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9BF)
    Sleep(50)

    def lambda_9CF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9CF)
    Sleep(100)

    #C0004
    ChrTalk(
        0x8,
        (
            "#04306F#11Pいや～、そうしたいのは\x01",
            "山々やったんですけど。\x02\x03",

            "#04300F何分、騎士団#6Rウ チ ら#にとっては\x01",
            "クロスベルは鬼門でして……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x10A,
        (
            "#00606F#5Pクロスベル教区の責任者、\x01",
            "エラルダ大司教の意向か。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#6P#00005Fそうか、前にマーブル先生が言ってた\x01",
            "法術の専門家って……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(150)

    #C0007
    ChrTalk(
        0x8,
        (
            "#04303F#11Pああ、オレらの事やろね。\x02\x03",

            "#04300Fまあ色々あって、大司教さんには\x01",
            "えらい嫌われてしまっててな。\x02\x03",

            "クロスベルでの\x01",
            "星杯騎士団の活動については\x01",
            "一切禁じられてしまってるんや。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            "#6P#10108Fエラルダ大司教ですか……\x02\x03",

            "#10106F私も会ったことがありますけど\x01",
            "すごく厳格そうな人ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#04306F#11P厳格も厳格。\x01",
            "あんなガンコな人見たことないわ。\x02\x03",

            "#04308Fま、オレらも色々やっとるから\x01",
            "彼みたいな真っ当な人から見たら\x01",
            "我慢ならんのかもしれへんけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#6P#00011Fい、色々って……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x108,
        (
            "#5P#01403Fまあ、《古代遺物》に関わる事件は\x01",
            "奇麗事だけでは済まないという事だ。\x02\x03",

            "#01402F──ケビン神父。\x01",
            "とにかく今回は助けられた。\x02\x03",

            "改めて礼を言わせてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(150)

    #C0012
    ChrTalk(
        0x8,
        (
            "#04302F#12Pはは、アリオスさんには\x01",
            "前にデカイ借りがありますしな。\x02\x03",

            "#04304F本当なら、例の教団の件も含めて\x01",
            "オレも付いて行きたいトコですけど。\x02\x03",

            "#04311Fま、大司教を刺激したくないですし\x01",
            "何か分かったら教えてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x108,
        (
            "#5P#01404Fああ、ギルドを通じて\x01",
            "そちらに連絡させてもらおう。\x02\x03",

            "#01402F──ロイド、ノエル曹長も。\x01",
            "今回は本当によくやってくれた。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EDD():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EDD)
    Sleep(50)

    def lambda_EED():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_EED)
    Sleep(50)
    TurnDirection(0x109, 0x10A, 500)
    Sleep(200)

    #C0014
    ChrTalk(
        0x109,
        (
            "#6P#10112Fあはは、正直あんまり\x01",
            "お役に立てませんでしたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#12P#00002Fいや、曹長は本当に\x01",
            "助けになってくれたよ。\x02\x03",

            "#00006F……俺の方こそ\x01",
            "やっぱりまだまだ未熟ですね。\x02\x03",

            "#00008F本当なら、逮捕まできちんと\x01",
            "皆さんを引っ張らなくては\x01",
            "ならなかったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x108,
        "#5P#01405Fふむ……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x10A,
        (
            "#00606F#5Pフン、自惚#4Rうぬぼ#れるな。\x02\x03",

            "#00601F支援課による逮捕というのが\x01",
            "あくまで建前であるというのは\x01",
            "お前も弁#2Rわきま#えていたはずだ。\x02\x03",

            "その上で、自分が本当に\x01",
            "役に立たなかったと思うのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#12P#00005Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x10A,
        (
            "#00603F#5P自戒もいいが、客観的な自己評価と\x01",
            "状況判断は上級捜査官に必須だ。\x02\x03",

            "#00600F研修とはいえ、一課に居たからには\x01",
            "その辺りは弁えておくがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#12P#00002Fダドリーさん……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x109,
        (
            "#6P#10112Fふふっ……\x01",
            "本当に素直じゃないですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x108,
        (
            "#5P#01404Fフッ、よくやったの一言くらい\x01",
            "言ってやればいいものを。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x10A,
        (
            "#00610F#5Pええい、うるさい。\x02\x03",

            "#00606F──とにかくバニングス。\x01",
            "これで一課の研修も終了だ。\x02\x03",

            "#00602F今回の事件で学んだ事と合わせて\x01",
            "新たなスタートに活かすがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#12P#00002Fはい……\x01",
            "ありがとうございます！\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x108,
        (
            "#5P#01404Fそれでは俺たちは\x01",
            "一足先に行かせてもらおう。\x02\x03",

            "#01402Fまた協力するような事があれば\x01",
            "よろしく頼むぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#12P#00000Fええ、こちらこそ！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x109,
        "#6P#10109Fお疲れさまです！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "#04309F#12Pそんじゃ、お元気で～！\x02",
    )

    CloseMessageWindow()
    OP_71(0xA, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0xA)
    BeginChrThread(0x10A, 3, 0, 9)
    Sleep(1000)
    BeginChrThread(0x108, 3, 0, 9)
    WaitChrThread(0x108, 3)

    def lambda_1409():

        label("loc_1409")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_1409")

    QueueWorkItem2(0x101, 2, lambda_1409)

    def lambda_141B():

        label("loc_141B")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_141B")

    QueueWorkItem2(0x109, 2, lambda_141B)

    def lambda_142D():

        label("loc_142D")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_142D")

    QueueWorkItem2(0x8, 2, lambda_142D)
    OP_71(0xA, 0x14B, 0x168, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0xA)
    Sound(470, 0, 80, 0)
    OP_71(0xA, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0xA)
    Sound(494, 0, 90, 0)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-2000, 1100, 9600, 2000)

    def lambda_148C():
        OP_96(0xFE, 0xFFFFD6FC, 0x0, 0x34BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_148C)
    Sleep(2000)
    Sound(457, 0, 100, 0)
    Fade(500)
    EndChrThread(0xA, 0x1)
    SetChrPos(0xA, -15000, 0, 18000, 0)

    def lambda_14C9():
        OP_96(0xFE, 0xFFFF3CB0, 0x0, 0x4650, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14C9)
    OP_68(-18000, 900, 18000, 0)
    MoveCamera(60, 27, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    OP_68(-30000, 900, 18000, 4000)
    MoveCamera(60, 21, 0, 4000)
    SetCameraDistance(23500, 4000)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x8, 0x2)
    Fade(500)
    StopSound(457, 500, 90)
    OP_68(500, 1000, 8500, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -800, 0, 8900, 270)
    SetChrPos(0x109, -900, 0, 7600, 270)
    SetChrPos(0x8, 1500, 0, 8500, 270)
    OP_0D()

    #C0029
    ChrTalk(
        0x8,
        (
            "#04309F#11Pいや～、君らも幸運やね。\x02\x03",

            "#04311F所属は違っても、いい先輩に\x01",
            "恵まれてるみたいやないか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1618():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1618)
    Sleep(50)
    TurnDirection(0x109, 0x8, 500)

    #C0030
    ChrTalk(
        0x101,
        "#00002F#6Pええ、本当にそう思います。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x109,
        (
            "#6P#10104Fそうですね……\x01",
            "セルゲイ課長もそうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "#04300F#11Pそれで、君らはどうするん？\x02\x03",

            "このまま列車で\x01",
            "クロスベルに戻るつもりか？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00004F#6Pええ、そうするつもりです。\x02\x03",

            "#00005Fそうだ……\x01",
            "ケビン神父、この後のご予定は？\x02\x03",

            "#00000Fクロスベルまで一駅ですし……\x01",
            "よかったら寄っていただいて\x01",
            "お礼をさせて欲しいんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "#04306F#11Pいや～、ありがたいけど\x01",
            "これから待ち合わせがあってな。\x02\x03",

            "#04308F本当なら、例の教団についても\x01",
            "詳しい話を聞きたいんやけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x101,
        "#00013F#6PＤ∴Ｇ教団、ですか……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x109,
        (
            "#6P#10101Fやっぱり教会の方でも\x01",
            "何か掴んでいるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#04306F#11Pいや～、それが全く。\x02\x03",

            "#04300Fオレらが教団と関わったのは\x01",
            "４年くらい前の事件が最後やね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        "#6P#10105F４年前……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#00005F#6P各国の軍やギルドが協力した\x01",
            "一斉制圧・摘発作戦の後ですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#04303F#11Pああ、あれから取りこぼされた\x01",
            "ロッジの一つを制圧したんや。\x02\x03",

            "#04308F……ここだけの話、教団の中でも\x01",
            "最悪と言えるようなロッジでな。\x02\x03",

            "#04301F正直、人体実験がマシに思えるほど\x01",
            "イカれた儀式をしてた連中やった。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#00006F#6P……そうですか。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        (
            "#6P#10106F本当に……\x01",
            "最低の連中だったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#04304F#11Pま、実はそん時にアリオスさんに\x01",
            "えらい助けられてしまってな。\x02\x03",

            "#04311Fデカイ借りを作ったままやったから\x01",
            "今回、お手伝いできて助かったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00002F#6Pそうだったんですか……\x02\x03",

            "#00004Fでも、お陰で犯人を生かしたまま\x01",
            "捕まえることができました。\x02\x03",

            "#00000Fありがとうございます。\x01",
            "……本当に助かりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "#04304F#11Pいやいや。\x02\x03",

            "#04302Fさっきの眼鏡の人も言ってたけど\x01",
            "何とかなったのは君のお陰やで。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0046
    ChrTalk(
        0x101,
        "#00005F#6P俺の、ですか？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#04304F#11Pああ、あの兄さんが\x01",
            "ギリギリのところで保ったのは\x01",
            "君の言葉があったからやろ。\x02\x03",

            "#04300Fそうでなかったらオレが処置しても\x01",
            "たぶん助けられへんかったはずや。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00002F#6Pそう、でしょうか……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(200)

    #C0049
    ChrTalk(
        0x109,
        (
            "#12P#10109Fええ、きっとそうですよ！\x02\x03",

            "#10102Fロイドさんが必死に語りかけたから\x01",
            "彼も自分を取り戻せたみたいだし！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(150)

    #C0050
    ChrTalk(
        0x101,
        "#00005F#5P曹長……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#04309F#11Pハハ……\x01",
            "『特務支援課』やったっけ？\x02\x03",

            "#04302Fまた機会があったら\x01",
            "詳しい話でも聞かせてや。\x02\x03",

            "これで教団の件も\x01",
            "一通りケリが付いたはずやけど\x01",
            "また何かあるかもしれへんしな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E9B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E9B)
    Sleep(50)
    TurnDirection(0x109, 0x8, 500)

    #C0052
    ChrTalk(
        0x101,
        (
            "#00004F#6Pはは、分かりました。\x02\x03",

            "#00000F……それじゃあ俺たちは\x01",
            "このあたりで失礼します。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x109,
        "#6P#10109Fお疲れ様でした！\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#04311F#11Pああ！\x01",
            "そちらこそお疲れさん！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(500, 1000, 11400, 4000)

    def lambda_1F6D():

        label("loc_1F6D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1F6D")

    QueueWorkItem2(0x8, 2, lambda_1F6D)
    BeginChrThread(0x101, 3, 0, 10)
    BeginChrThread(0x109, 3, 0, 11)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x109, 3)
    EndChrThread(0x8, 0x2)
    Sleep(500)

    #C0055
    ChrTalk(
        0x8,
        (
            "#04300F#11Pロイド君か……\x01",
            "なかなか見込みがありそうやな。\x02\x03",

            "#04304Fエステルちゃんたちの力にも\x01",
            "なってくれたみたいやし。\x02\x03",

            "#04308Fせやけど……今回ばかりは\x01",
            "どうも分が悪いかもしれへんな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 7100, 0, 2300, 315)
    ClearChrFlags(0x9, 0x80)

    #N0056
    NpcTalk(
        0x9,
        "娘の声",
        "──ケビン。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(5300, 1000, 3800, 0)
    MoveCamera(83, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_68(2300, 1000, 7800, 3500)
    SetCameraDistance(16500, 3500)

    def lambda_20E5():
        OP_95(0xFE, 3100, 0, 7300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20E5)
    OP_0D()
    TurnDirection(0x8, 0x9, 500)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x8, 500)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)

    #C0057
    ChrTalk(
        0x8,
        (
            "#6P#04302Fおお、遅かったやないか。\x02\x03",

            "#04305F……って、なんやその紙袋は？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0058
    AnonymousTalk(
        0x9,
        (
            "そこの屋台で売ってた\x01",
            "アルタイル名物の焼き栗。\x02\x03",

            "ホクホクしてて絶妙な甘さで\x01",
            "いい仕事してる。\x02",
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

    #C0059
    ChrTalk(
        0x8,
        (
            "#6P#04306Fだからって紙袋いっぱい\x01",
            "買うことないやろ……\x02\x03",

            "#04301Fまったく、そんな調子で\x01",
            "これから大丈夫か？\x02\x03",

            "やっぱりオレも付いて……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "#13806F#11P……だめ。\x01",
            "ケビンの悪名は知られすぎている。\x02\x03",

            "#13811Fエラルダ大司教に潜入がバレたら\x01",
            "火あぶりにされるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "#6P#04305Fい、いくらなんでも\x01",
            "そこまではされへんやろ！？\x02\x03",

            "#04308Fいや、でも典礼省の\x01",
            "オーウェンの件があったか……\x02\x03",

            "#04306Fあの一件で封聖省への態度を\x01",
            "ますます硬化させたみたいやし。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "#13803F#11Pその点、私一人なら\x01",
            "目くらましにはもってこい。\x02\x03",

            "#13801Fそれはケビンにも\x01",
            "分かっているでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#6P#04306Fああもう……分かったわ！\x02\x03",

            "#04308Fまったく総長も\x01",
            "よりによって何でコイツを……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "#13804F#11P的確な人選。\x02\x03",

            "#13802Fケビンこそ、私がいない間、\x01",
            "無茶はしないように。\x02\x03",

            "セサルさんとマーカスさんに\x01",
            "あまり心配はかけないこと。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "#6P#04303Fへーへー、分かったわ。\x02\x03",

            "#04301F……しかしリース。\x01",
            "ホンマ、気をつけろや？\x02\x03",

            "お前がこれから向かう場所は\x01",
            "正直、何が起きてもおかしくない。\x02\x03",

            "いざとなったらオレを呼ぶなり、\x01",
            "切り札に頼るんやで？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "#13805F#11Pそれは心得てるけど……\x02\x03",

            "#13801F……そんなに悪い状況？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#6P#04306Fああ……\x01",
            "聖俗双方の意味合いでな。\x02\x03",

            "#04301Fどうやら“連中”も\x01",
            "密かに動き出しとるらしい。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0068
    AnonymousTalk(
        0x8,
        (
            "#30W魔都クロスベル──\x01",
            "その名の通りになるかもしれん。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    RemoveParty(0x9, 0xFF)
    RemoveParty(0x7, 0xFF)
    SetScenarioFlags(0x25, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1500)
    SetScenarioFlags(0x22, 2)
    NewScene("e4800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_419 end

    def Function_4_2753(): pass

    label("Function_4_2753")

    OP_96(0x16, 0xFFFFBF8C, 0x0, 0x445C, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFFBF8C, 0x30D4, 0x15F90, 0x1388, 0x1)
    OP_96(0x16, 0xFFFFD314, 0x0, 0x5DC, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFFBBA4, 0x5DC, 0x15F90, 0x1388, 0x1)
    OP_96(0x16, 0xFFFF9A70, 0x0, 0xFFFFEE6C, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFF9A70, 0xFFFFDAE4, 0xFFFEA070, 0x1388, 0x1)
    OP_96(0x16, 0xFFFF86E8, 0x0, 0xFFFF88DC, 0x1770, 0x0)
    Return()

    # Function_4_2753 end

    def Function_5_27E3(): pass

    label("Function_5_27E3")

    Sleep(5500)
    OP_68(-24960, 1900, -3590, 6000)
    MoveCamera(24, 19, 0, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(24000, 6000)
    OP_6F(0x79)
    Return()

    # Function_5_27E3 end

    def Function_6_2817(): pass

    label("Function_6_2817")

    OP_95(0x12, 0, 0, -10500, 2000, 0x0)
    OP_95(0x12, 4700, 0, -5400, 2000, 0x0)

    def lambda_2844():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2844)
    TurnDirection(0x12, 0xD, 500)
    BeginChrThread(0x12, 0, 0, 0)
    Sleep(1000)
    OP_63(0x12, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Return()

    # Function_6_2817 end

    def Function_7_286F(): pass

    label("Function_7_286F")

    ClearMapObjFlags(0x0, 0x10)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_288D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_288D)
    OP_95(0x13, 10500, 0, 6000, 2000, 0x0)
    OP_95(0x13, 10500, 0, -5000, 2000, 0x0)
    OP_9E(0x13, 0x7D0, 0xFFFFEC78, 0x15F90, 0x7D0, 0x1)
    OP_95(0x13, 2000, 0, -30000, 2000, 0x0)
    OP_70(0x0, 0x0)
    Return()

    # Function_7_286F end

    def Function_8_28EF(): pass

    label("Function_8_28EF")

    OP_95(0x14, 12000, 0, 15500, 2000, 0x0)
    OP_95(0x14, 30000, 0, 15500, 2000, 0x0)

    def lambda_291C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_291C)
    Return()

    # Function_8_28EF end

    def Function_9_2929(): pass

    label("Function_9_2929")

    OP_92(0xFE, 0xFFFFFE70, 0x2EE0, 0x1F4)
    OP_95(0xFE, -400, 0, 12000, 2000, 0x0)

    def lambda_294F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_294F)
    OP_95(0xFE, -400, 150, 13500, 1500, 0x0)
    Return()

    # Function_9_2929 end

    def Function_10_2970(): pass

    label("Function_10_2970")

    OP_92(0xFE, 0xFFFFFE70, 0x4074, 0x1F4)
    OP_95(0xFE, -400, 0, 16500, 2500, 0x0)
    OP_95(0xFE, -400, 1100, 20500, 2500, 0x0)

    def lambda_29AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_29AA)
    OP_95(0xFE, -400, 1100, 22500, 2500, 0x0)
    Return()

    # Function_10_2970 end

    def Function_11_29CB(): pass

    label("Function_11_29CB")

    Sleep(100)
    OP_92(0xFE, 0xFFFFFDA8, 0x4074, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -600, 0, 16500, 2500, 0x0)
    OP_95(0xFE, -600, 1100, 20500, 2500, 0x0)

    def lambda_2A0B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A0B)
    OP_95(0xFE, -600, 1100, 22500, 2500, 0x0)
    Return()

    # Function_11_29CB end

    def Function_12_2A2C(): pass

    label("Function_12_2A2C")

    Sleep(2000)
    Sound(467, 0, 80, 0)
    Sleep(200)
    Sound(465, 0, 100, 0)
    Sleep(5300)
    Sound(471, 0, 100, 0)
    Return()

    # Function_12_2A2C end

    def Function_13_2A48(): pass

    label("Function_13_2A48")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1960, 5600, 11900, 0)
    MoveCamera(40, 14, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(13600, 0)
    SetChrPos(0x101, 80, 0, 15350, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AB9")
    SetChrPos(0x102, -1100, 0, 15350, 180)
    Jump("loc_2B4C")

    label("loc_2AB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ADF")
    SetChrPos(0x103, -1100, 0, 15350, 180)
    Jump("loc_2B4C")

    label("loc_2ADF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B05")
    SetChrPos(0x104, -1100, 0, 15350, 180)
    Jump("loc_2B4C")

    label("loc_2B05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B2B")
    SetChrPos(0x109, -1100, 0, 15350, 180)
    Jump("loc_2B4C")

    label("loc_2B2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B4C")
    SetChrPos(0x105, -1100, 0, 15350, 180)

    label("loc_2B4C")

    SetChrPos(0x1A1, 1150, 0, 15350, 180)
    LoadChrToIndex("chr/ch24100.itc", 0x1E)
    LoadChrToIndex("chr/ch41200.itc", 0x1F)
    LoadChrToIndex("chr/ch31400.itc", 0x20)
    LoadChrToIndex("chr/ch31500.itc", 0x21)
    SetChrChipByIndex(0x18, 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -50, 0, 11950, 0)
    SetChrChipByIndex(0x19, 0x1F)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -840, 0, 11950, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 720, 0, 11950, 0)
    SetChrChipByIndex(0x1B, 0x20)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -20430, 0, 2990, 45)
    SetChrChipByIndex(0x1C, 0x21)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -21600, 0, 2950, 45)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xA, 0x17)
    OP_49()
    SetChrPos(0x17, -500, 0, 8940, 0)
    OP_D5(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x0)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    OP_68(-1960, 1900, 11900, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0069
    ChrTalk(
        0x19,
        (
            "クロスベル警察の諸君、\x01",
            "ご苦労だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x19,
        (
            "彼らは我々が責任を持って、\x01",
            "連行させていただく。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#00000Fありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x1A1,
        "よ、よろしくおねがいします～。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x1A,
        "ほら、キビキビ歩け。\x02",
    )

    CloseMessageWindow()

    def lambda_2D53():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2D53)

    def lambda_2D60():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2D60)
    Sleep(300)
    OP_93(0x18, 0xB4, 0x1F4)

    def lambda_2D77():
        OP_95(0xFE, -840, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2D77)

    def lambda_2D91():
        OP_95(0xFE, 720, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2D91)

    def lambda_2DAB():
        OP_95(0xFE, -50, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2DAB)
    WaitChrThread(0x18, 1)
    Sleep(500)
    OP_93(0x18, 0x0, 0x1F4)

    #C0074
    ChrTalk(
        0x18,
        "ア、アンタたち……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0075
    ChrTalk(
        0x18,
        (
            "#5Sこの借りは必ず返すから、\x01",
            "楽しみにしておくんだね！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x1A, 0x10E, 0x1F4)

    #C0076
    ChrTalk(
        0x1A,
        "ほら、私語は慎め！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1A, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0077
    ChrTalk(
        0x18,
        (
            "#5Sうるさいよッ！\x01",
            "このポンコツ軍人が！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0078
    ChrTalk(
        0x18,
        (
            "#5Sレデエはもっと\x01",
            "丁重に扱うんだねっ！#3S\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x1A,
        "ポ、ポンコツ！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x19, 0x5A, 0x1F4)

    #C0080
    ChrTalk(
        0x19,
        "……いいから、連れて行け。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Sound(462, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x169, 0x186, 0x1, 0x8)
    Sleep(1500)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1A, 0x4)
    BeginChrThread(0x18, 1, 0, 15)
    BeginChrThread(0x1A, 1, 0, 16)
    WaitChrThread(0x1A, 1)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x1A, 0x80)
    Sound(461, 0, 100, 0)
    OP_71(0xA, 0x187, 0x1A4, 0x1, 0x8)
    Sleep(1500)

    #C0081
    ChrTalk(
        0x101,
        (
            "#00006Fな、なんというか……\x01",
            "本当にまた現れそうで嫌だな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3045")

    #C0082
    ChrTalk(
        0x102,
        "#00106F同感だわ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F6")

    label("loc_3045")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3071")

    #C0083
    ChrTalk(
        0x103,
        "#00206F同感です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F6")

    label("loc_3071")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_309B")

    #C0084
    ChrTalk(
        0x104,
        "#00306F同感だ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F6")

    label("loc_309B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30C9")

    #C0085
    ChrTalk(
        0x109,
        "#10106F同感です……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F6")

    label("loc_30C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30F6")

    #C0086
    ChrTalk(
        0x105,
        "#10302Fフフ、同感だよ。\x02",
    )

    CloseMessageWindow()

    label("loc_30F6")

    OP_93(0x19, 0x0, 0x1F4)

    #C0087
    ChrTalk(
        0x19,
        (
            "……そんなことがないよう、\x01",
            "善処させてもらうつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x19,
        (
            "とにかく、ご苦労だった。\x01",
            "君たちも気をつけて帰りたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        "#00000Fあ……はい、お疲れ様でした。\x02",
    )

    CloseMessageWindow()
    OP_93(0x19, 0xB4, 0x1F4)
    Sound(462, 0, 100, 0)
    OP_71(0xA, 0xF1, 0x10E, 0x1, 0x8)
    Sleep(1500)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x19, 0x4)

    def lambda_31C9():
        OP_95(0xFE, -840, 150, 9610, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_31C9)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Sound(461, 0, 100, 0)
    OP_71(0xA, 0x10F, 0x12C, 0x1, 0x8)
    Sleep(1500)
    Sound(470, 0, 50, 0)
    OP_71(0xA, 0x3C, 0x5A, 0x1, 0x8)
    Sleep(1000)
    Sound(457, 0, 100, 0)
    OP_71(0xA, 0x79, 0xB4, 0x1, 0x20)
    OP_68(-8150, 1900, 6710, 2500)
    MoveCamera(35, 31, 0, 2500)
    OP_6E(580, 2500)
    SetCameraDistance(18500, 2500)
    BeginChrThread(0x17, 1, 0, 17)
    OP_6F(0x79)
    Sleep(2000)
    StopSound(457, 1000, 90)
    Fade(500)
    EndChrThread(0x17, 0x1)
    SetMapObjFlags(0xA, 0x4)
    OP_68(-810, 1900, 13320, 0)
    MoveCamera(27, 23, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(13600, 0)
    SetChrPos(0x101, -200, 0, 15570, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32D8")
    SetChrPos(0x102, -1040, 0, 14270, 45)
    Jump("loc_336B")

    label("loc_32D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32FE")
    SetChrPos(0x103, -1040, 0, 14270, 45)
    Jump("loc_336B")

    label("loc_32FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3324")
    SetChrPos(0x104, -1040, 0, 14270, 45)
    Jump("loc_336B")

    label("loc_3324")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_334A")
    SetChrPos(0x109, -1040, 0, 14270, 45)
    Jump("loc_336B")

    label("loc_334A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_336B")
    SetChrPos(0x105, -1040, 0, 14270, 45)

    label("loc_336B")

    SetChrPos(0x1A1, 750, 0, 14180, 315)
    OP_0D()

    #C0090
    ChrTalk(
        0x101,
        (
            "#00003Fふう……\x01",
            "結局はこうするしかなかったか。\x02\x03",

            "#00001F何とかして自分たちの手で\x01",
            "捕まえたかったところだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3464")

    #C0091
    ChrTalk(
        0x102,
        (
            "#00100Fううん、でも……\x01",
            "仕方がないわよね。\x02\x03",

            "#00104F逃がさなかっただけでも\x01",
            "よしとしないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3669")

    label("loc_3464")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34E1")

    #C0092
    ChrTalk(
        0x103,
        (
            "#00200F気持ちは分かりますが……\x01",
            "仕方がないかと。\x02\x03",

            "#00204F逃がさなかっただけでも\x01",
            "よしとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3669")

    label("loc_34E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_355A")

    #C0093
    ChrTalk(
        0x104,
        (
            "#00306Fそう言われると\x01",
            "そうなんだけどな……\x02\x03",

            "#00300Fま、逃がさなかっただけでも\x01",
            "よしとしようや。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3669")

    label("loc_355A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35DE")

    #C0094
    ChrTalk(
        0x109,
        (
            "#10106Fそうですね……\x01",
            "ちょっと悔しいです。\x02\x03",

            "#10100F……でも、\x01",
            "逃がさずに済みましたし\x01",
            "結果オーライですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3669")

    label("loc_35DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3669")

    #C0095
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、捕まえたのには\x01",
            "変わりないんだし、\x01",
            "別にいいんじゃない？\x02\x03",

            "#10304F逃がさなかっただけでも\x01",
            "よしとしないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3669")


    #C0096
    ChrTalk(
        0x1A1,
        (
            "そうそう！\x01",
            "僕も随分助かっちゃったよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x1A1,
        (
            "いや～、よかったよかった。\x01",
            "これでドノバン警部に\x01",
            "いい報告ができそうだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#00000Fはは……\x01",
            "それもそうですね。\x02\x03",

            "さて……\x01",
            "それじゃ、クロスベル市に\x01",
            "戻るとするか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_379E")

    #C0099
    ChrTalk(
        0x102,
        (
            "#00100Fええ、そうね。\x01",
            "あまりこちらに長居するのも\x01",
            "よくないでしょうし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D9")

    label("loc_379E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37F0")

    #C0100
    ChrTalk(
        0x103,
        (
            "#00200Fそうですね。\x01",
            "あまりこちらに長居は\x01",
            "できませんし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D9")

    label("loc_37F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_383E")

    #C0101
    ChrTalk(
        0x104,
        (
            "#00300Fだな。\x01",
            "あんまし長居してる暇は\x01",
            "なさそうだし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D9")

    label("loc_383E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_388E")

    #C0102
    ChrTalk(
        0x109,
        (
            "#10100Fですね。\x01",
            "あまり長居してる暇は\x01",
            "なさそうですし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D9")

    label("loc_388E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38D9")

    #C0103
    ChrTalk(
        0x105,
        (
            "#10300Fそうだね。\x01",
            "あまり長居するのも\x01",
            "どうかと思うし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D9")


    #C0104
    ChrTalk(
        0x1A1,
        (
            "う～ん、でもせっかく\x01",
            "共和国まで来たんだし……。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x1A1,
        (
            "ついでにどこかに\x01",
            "観光でも行きたいところだな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#00006Fこ、今度にしてください……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x0, 1, 0, 14)
    Sleep(50)
    BeginChrThread(0x1, 1, 0, 14)
    Sleep(50)
    BeginChrThread(0x1A1, 1, 0, 14)
    Sleep(1000)
    OP_68(-18880, 1900, 2270, 5000)
    MoveCamera(41, 24, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(15100, 5000)
    OP_6F(0x79)

    #C0107
    ChrTalk(
        0x1B,
        (
            "こういう結末になるとは\x01",
            "予想外だったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x1C,
        (
            "……まぁ、\x01",
            "残党を逃がさないという\x01",
            "最低限の目的は達したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x1C,
        (
            "ひとまずツァオ様のところに\x01",
            "報告に戻るぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x1B,
        "ああ、そうだな……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1A1, 0x1)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x1A1)
    SetChrName("")

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちはそのまま\x01",
            "クロスベル行きの列車を待ち……\x02\x03",

            "お土産屋に後ろ髪を引かれるレイモンドを\x01",
            "たしなめながら、共和国を後にするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 6)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_13_2A48 end

    def Function_14_3B58(): pass

    label("Function_14_3B58")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C70")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3B9B"),
        (1, "loc_3BB5"),
        (2, "loc_3BCF"),
        (3, "loc_3BE9"),
        (4, "loc_3C03"),
        (5, "loc_3C1D"),
        (6, "loc_3C37"),
        (SWITCH_DEFAULT, "loc_3C51"),
    )


    label("loc_3B9B")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_3C6B")

    label("loc_3BB5")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_3C6B")

    label("loc_3BCF")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_3C6B")

    label("loc_3BE9")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_3C6B")

    label("loc_3C03")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_3C6B")

    label("loc_3C1D")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_3C6B")

    label("loc_3C37")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_3C6B")

    label("loc_3C51")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_3C6B")

    label("loc_3C6B")

    Jump("Function_14_3B58")

    label("loc_3C70")

    Return()

    # Function_14_3B58 end

    def Function_15_3C71(): pass

    label("Function_15_3C71")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_3C7D():
        OP_96(0xFE, 0xFFFFFFCE, 0x96, 0x258A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C7D)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_15_3C71 end

    def Function_16_3C9E(): pass

    label("Function_16_3C9E")

    OP_95(0xFE, -50, 0, 10950, 1000, 0x0)

    def lambda_3CB7():
        OP_95(0xFE, -50, 150, 9610, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3CB7)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_16_3C9E end

    def Function_17_3CD8(): pass

    label("Function_17_3CD8")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -500, 0, 8940)
    OP_9F(0x1, -6550, 0, 8940)
    OP_9F(0x1, -7500, 0, 8400)
    OP_9F(0x1, -8100, 0, 7000)
    OP_9F(0x1, -8200, 0, 4200)
    OP_9F(0x1, -8360, 0, -4860)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_17_3CD8 end

    SaveToFile()

Try(main)
