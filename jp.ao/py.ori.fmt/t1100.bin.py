from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1100.bin",                # FileName
        "t1100",                    # MapName
        "t1100",                    # Location
        0x0046,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 70, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1100",                  # 0
        "猟兵ザックス",           # 1
        "猟兵",                   # 2
        "猟兵",                   # 3
        "猟兵",                   # 4
        "猟兵",                   # 5
        "軍用犬",                 # 6
        "軍用犬",                 # 7
        "SE制御",                 # 8
        "bt1010",                 # 9
        "ホテル・デルフィニア方面",# 10
    ))

    ATBonus("ATBonus_280", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_340", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 10, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_324", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_328", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_32C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_330", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_334", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_338", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_360", 0x004A, 255, 6, 45, 3, 3, 30, 0, "bt1010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42002.dat", "ms41902.dat", "ms41902.dat", "ms86100.dat", "ms86100.dat", 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_320", "ed7540", "ed7453", "ATBonus_280"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51706.itc",                   # 00
        "chr/ch00000.itc",                   # 01
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   0.0,                   1.5,                   -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -0.5,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 18,  0.0,                   0.0,                   -1.0,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -0.0,                  0.19999998807907104,   1.0])

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "ホテル・デルフィニア方面")

    ChipFrameInfo(1008, 0)                                       # 0

    ScpFunction((
        "Function_0_3F0",          # 00, 0
        "Function_1_411",          # 01, 1
        "Function_2_4C6",          # 02, 2
        "Function_3_16BE",         # 03, 3
        "Function_4_16D1",         # 04, 4
        "Function_5_16E4",         # 05, 5
        "Function_6_16EE",         # 06, 6
        "Function_7_1709",         # 07, 7
        "Function_8_172A",         # 08, 8
        "Function_9_174B",         # 09, 9
        "Function_10_1DB1",        # 0A, 10
        "Function_11_1DCE",        # 0B, 11
        "Function_12_1DEB",        # 0C, 12
        "Function_13_1E03",        # 0D, 13
        "Function_14_1E1B",        # 0E, 14
        "Function_15_1E44",        # 0F, 15
        "Function_16_1E5A",        # 10, 16
        "Function_17_243E",        # 11, 17
        "Function_18_24D8",        # 12, 18
    ))


    def Function_0_3F0(): pass

    label("Function_0_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_401")
    Event(0, 2)

    label("loc_401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_410")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)

    label("loc_410")

    Return()

    # Function_0_3F0 end

    def Function_1_411(): pass

    label("Function_1_411")

    SetMapObjFrame(0xFF, "t1100_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1100_sky_y", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_44D")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_476")
    Call(0, 17)

    label("loc_476")

    Sound(126, 1, 80, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4A3")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_4C5")

    label("loc_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_4C5")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)

    label("loc_4C5")

    Return()

    # Function_1_411 end

    def Function_2_4C6(): pass

    label("Function_2_4C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x52, 0xFF, 0xFF)
    LoadChrToIndex("apl/ch51323.itc", 0x1E)
    SetChrPos(0x101, 0, 0, -32000, 0)
    SetChrPos(0x153, 0, 0, -17000, 0)
    OP_68(0, 1000, -17000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1000, -21500, 6000)
    MoveCamera(0, 20, 0, 6000)
    SetCameraDistance(28000, 6000)
    Sleep(3500)

    def lambda_562():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_562)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xFA0)
    BeginChrThread(0xF, 1, 0, 7)

    #C0001
    ChrTalk(
        0x101,
        "#00001F#6P#N（こんな所に……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1000, -16500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    #C0002
    ChrTalk(
        0x153,
        "#01108F#40W#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        "#00002F#12P#Nキーア、ここにいたのか。\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x153, 0xB4, 0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    #C0004
    ChrTalk(
        0x153,
        "#01102F#5Pロイド……\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, -17000, 5000)
    SetCameraDistance(21000, 5000)

    def lambda_6AC():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFBD98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AC)

    def lambda_6C6():

        label("loc_6C6")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6C6")

    QueueWorkItem2(0x153, 2, lambda_6C6)
    Sleep(4000)

    def lambda_6DB():
        OP_96(0xFE, 0x1F4, 0x0, 0xFFFFBD98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_6DB)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 1)
    EndChrThread(0x153, 0x2)
    OP_6F(0x79)
    Fade(1000)
    OP_68(3790, 500, 33620, 0)
    MoveCamera(26, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(80770, 0)
    PlaceName2(340, 40, "c_plac73", 0x0, 3000)
    MoveCamera(37, 23, 0, 8000)
    OP_6F(0x40)
    Sleep(500)

    #C0005
    ChrTalk(
        0x101,
        (
            "#00004F#12P#Nはは、懐かしいな。\x02\x03",

            "#00000F……覚えてるか？\x01",
            "ここから一緒に逃げた事を。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0006
    ChrTalk(
        0x153,
        (
            "#01104F#12P#Nえへへ……\x01",
            "忘れるわけないよー。\x02\x03",

            "#01121Fだってキーアの記憶は\x01",
            "ここから始まったんだよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00002F#12P#N……だよな。\x02\x03",

            "#00008F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0008
    ChrTalk(
        0x153,
        (
            "#01103F#12P#Nねえ、ロイド。\x02\x03",

            "#01101Fキーアはここにいたけど……\x01",
            "ずっと居た場所は違うんだよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00003F#12P#Nああ……\x02\x03",

            "#00001F……やっぱり気になるか？\x01",
            "自分がどういう生まれなのか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0010
    ChrTalk(
        0x153,
        (
            "#01106F#12P#N……うん。\x02\x03",

            "なんだか最近、すこしずつ\x01",
            "気になってきちゃって……\x02\x03",

            "#01108Fずっと昔に生まれたっていうのは\x01",
            "ロイドたちから聞いたけど……\x02\x03",

            "#01112Fそれがどういう意味なのか\x01",
            "最近やっと分かった気がする……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0011
    ChrTalk(
        0x101,
        "#00008F#12P#Nそっか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1000, -17000, 0)
    MoveCamera(42, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(19000, 50000)
    OP_0D()
    OP_93(0x153, 0x0, 0x1F4)
    Sleep(300)

    #C0012
    ChrTalk(
        0x153,
        (
            "#01122F#11Pえへへ……\x02\x03",

            "#01121Fロイドがいて、エリィがいて……\x01",
            "ティオやランディやみんながいて……\x02\x03",

            "シズクや、リュウたちや\x01",
            "マーブルせんせーも仲良くしてくれて……\x02\x03",

            "#01108F毎日楽しいのはホントだけど……\x02\x03",

            "#01106F#30Wたまにね……ほんのたまに\x01",
            "ひとりぼっちになった気がする……\x02\x03",

            "#30W……あの真っ黒な空洞に\x01",
            "とり残されちゃったような……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x190)
    Sleep(150)

    #C0013
    ChrTalk(
        0x101,
        "#00001F#6P──キーア。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(670, 1000, -16940, 1500)
    Sleep(400)

    def lambda_BE8():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE8)
    OP_93(0x153, 0x10E, 0x190)
    WaitChrThread(0x101, 1)
    Fade(250)
    Sound(898, 0, 70, 0)
    BeginChrThread(0x101, 3, 0, 3)
    BeginChrThread(0x153, 3, 0, 4)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x153, 3)
    OP_0D()
    OP_6F(0x1)

    #C0014
    ChrTalk(
        0x153,
        (
            "#01123F#40W#11Pごめんね……ごめんなさい。\x02\x03",

            "ホントはこんなこと\x01",
            "言うつもりなかったのにぃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00006F#6Pバカ、遠慮するなって。\x02\x03",

            "#00008Fまた……言えなかったんだな？\x02\x03",

            "#00001Fヘコんでる俺たちに\x01",
            "余計な心配をかけたくなくって。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x153,
        "#01114F#40W#11P…………（コクン）\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#00000F#6Pあのな……逆だよキーア。\x02\x03",

            "#00004Fキーアが頼ってくれたら\x01",
            "それだけで俺たちは元気になれる。\x02\x03",

            "負けてられるか、なにくそって\x01",
            "お腹の底から頑張れるんだ。\x02\x03",

            "#00002Fだから、遠慮なんてするな。\x02\x03",

            "#00009F俺は──少なくとも俺だけは\x01",
            "ずっとキーアのそばにいるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x153,
        (
            "#01102F#30W#11P…………ぁ………………\x02\x03",

            "#30W#01104F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x153)
    Fade(250)
    Sound(812, 0, 70, 0)
    BeginChrThread(0x101, 3, 0, 5)
    BeginChrThread(0x153, 3, 0, 6)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x153, 3)
    OP_0D()
    Sleep(150)

    #C0019
    ChrTalk(
        0x153,
        "#01109F#11Pえへへ、ありがとー。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A1(0x153, 0x4B0, 0x6, 0x7, 0x8, 0x7, 0x6, 0x7, 0x8)
    Sleep(150)

    #C0020
    ChrTalk(
        0x153,
        (
            "#01101F#11Pでも、そんなこと言ってたら\x01",
            "おヨメさんが来てくれないよー？\x02\x03",

            "こんなコブがついてたら\x01",
            "出会いがなくなっちゃうかも。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0021
    ChrTalk(
        0x101,
        (
            "#00012F#6Pあのな……\x01",
            "どこで覚えたんだそんなの。\x02\x03",

            "#00011Fって、ひょっとして\x01",
            "図書館の本で読んだりしたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x153,
        (
            "#01111F#11Pんー、それもあるけど。\x02\x03",

            "#01100F街でいろんな人と\x01",
            "話してたらなんとなく？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00006F#6P勉強のしすぎも程々にな……\x02\x03",

            "#00000F──いずれにせよ、\x01",
            "俺の結婚なんて相当先だよ。\x02\x03",

            "兄貴だって結婚しようとしてたのは\x01",
            "２５歳くらいだったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x153,
        (
            "#01105F#11Pロイドのおにーさん？\x02\x03",

            "#01106F……そっか。\x01",
            "居なくなっちゃったんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、でも昔の話さ。\x02\x03",

            "#00000F兄貴の歳まであと７年……\x01",
            "ちゃんと一人前になるまでは\x01",
            "結婚なんて考えられないさ。\x02\x03",

            "#00012Fというか、そもそも\x01",
            "相手がいないと駄目だしなー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x153)
    Sleep(100)
    OP_A1(0x153, 0x5DC, 0x4, 0x7, 0x6, 0x7, 0x8)
    Sleep(200)

    #C0026
    ChrTalk(
        0x153,
        (
            "#01105F#11P７年後ってことは……\x02\x03",

            "キーア、幾つくらいになるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#00005F#6Pああ、今が９歳くらいだから……\x02\x03",

            "#00004F１６歳くらい──\x01",
            "はは、今のティオより年上か。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x153,
        (
            "#01103F#11Pんー……\x02\x03",

            "#01101Fそれくらいのトシになったら\x01",
            "キーアもケッコンできるー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0029
    ChrTalk(
        0x101,
        (
            "#00011F#6P#4Sええっ！？\x02\x03",

            "#00006Fいや、幾らなんでも\x01",
            "１６で結婚は早過ぎだろう！？\x02\x03",

            "#00008Fそりゃ、たしか保護者が認めれば\x01",
            "１６から結婚できたはずだけど……\x02\x03",

            "#00007Fで、でも駄目！\x01",
            "俺は絶対に認めないからなっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x153,
        (
            "#01111F#11Pんー、そういうイミじゃ\x01",
            "ないんだけどー。\x02\x03",

            "#01104F……えへへ、でもそっか。\x02\x03",

            "#01121F心配することなんて……\x01",
            "なんにもないんだよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、何もないさ。\x02\x03",

            "#00000F──さあ、そろそろ\x01",
            "テーマパークの方に行こう。\x02\x03",

            "ずっと楽しみにしてたんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x153,
        (
            "#01109F#11Pえへへ……\x02\x03",

            "#01110Fあのね、シズクに\x01",
            "テーマパークがどんな場所か\x01",
            "教えてって頼まれてるんだー。\x02\x03",

            "それで、シズクの目が治ったら\x01",
            "いっしょに遊びに行こうって。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00004F#6Pそっか……\x02\x03",

            "#00002Fよし、だったら尚更、\x01",
            "目いっぱい楽しまなくちゃな？\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x153, 0x5DC, 0x6, 0x9, 0xA, 0xB, 0xA, 0x9, 0x8)
    Sleep(100)

    #C0034
    ChrTalk(
        0x153,
        "#01109F#11Pうんっ！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    ClearChrFlags(0x153, 0x2)
    OP_49()
    OP_D7(0x1E)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    BeginChrThread(0xF, 1, 0, 8)
    SetChrPos(0x0, 0, 0, -12000, 180)
    SetScenarioFlags(0x145, 2)
    OP_29(0xA5, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_2_4C6 end

    def Function_3_16BE(): pass

    label("Function_3_16BE")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x10, 0x11, 0x12)
    Return()

    # Function_3_16BE end

    def Function_4_16D1(): pass

    label("Function_4_16D1")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_4_16D1 end

    def Function_5_16E4(): pass

    label("Function_5_16E4")

    OP_A1(0xFE, 0x3E8, 0x3, 0x13, 0x14, 0x15)
    Return()

    # Function_5_16E4 end

    def Function_6_16EE(): pass

    label("Function_6_16EE")

    SetChrPos(0xFE, 750, 0, -17000, 270)
    OP_A1(0xFE, 0x3E8, 0x3, 0x3, 0x4, 0x5)
    Return()

    # Function_6_16EE end

    def Function_7_1709(): pass

    label("Function_7_1709")

    OP_25(0x7E, 0x46)
    Sleep(200)
    OP_25(0x7E, 0x3C)
    Sleep(200)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x7E, 0x28)
    Sleep(200)
    OP_25(0x7E, 0x1E)
    Return()

    # Function_7_1709 end

    def Function_8_172A(): pass

    label("Function_8_172A")

    OP_25(0x7E, 0x28)
    Sleep(200)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x7E, 0x3C)
    Sleep(200)
    OP_25(0x7E, 0x46)
    Sleep(200)
    OP_25(0x7E, 0x50)
    Return()

    # Function_8_172A end

    def Function_9_174B(): pass

    label("Function_9_174B")

    EventBegin(0x0)
    FadeToDark(300, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00251.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch00351.itc", 0x23)
    LoadChrToIndex("chr/ch02950.itc", 0x24)
    LoadChrToIndex("chr/ch02951.itc", 0x25)
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch03151.itc", 0x27)
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch03251.itc", 0x29)
    LoadChrToIndex("chr/ch41950.itc", 0x2A)
    LoadChrToIndex("chr/ch41951.itc", 0x2B)
    LoadChrToIndex("chr/ch41952.itc", 0x2C)
    LoadChrToIndex("chr/ch42050.itc", 0x2D)
    LoadChrToIndex("chr/ch42051.itc", 0x2E)
    LoadChrToIndex("monster/ch86150.itc", 0x2F)
    LoadChrToIndex("monster/ch86151.itc", 0x30)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 600, 0, 5100, 0)
    OP_90(0x103, 500, 0, 3300, 0)
    OP_90(0x104, -700, 0, 5200, 0)
    OP_90(0x105, -500, 0, 3500, 0)
    OP_90(0x106, 1500, 0, 4350, 0)
    OP_90(0x109, -1500, 0, 4050, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x24)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x28)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 0x2F)
    SetChrChipByIndex(0xE, 0x2F)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 10)
    BeginChrThread(0xE, 0, 0, 10)
    SetChrPos(0x8, 0, 0, 20000, 180)
    SetChrPos(0x9, -2000, 0, 19500, 180)
    SetChrPos(0xC, 2000, 0, 19500, 180)
    SetChrPos(0xD, -1300, 0, 23000, 180)
    SetChrPos(0xE, 1300, 0, 23000, 180)
    OP_68(0, 1000, 17000, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(18500, 3000)
    FadeToBright(1000, 0)
    BeginChrThread(0xF, 1, 0, 15)

    def lambda_19A1():
        OP_9B(0x0, 0x101, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19A1)
    Sleep(50)

    def lambda_19B9():
        OP_9B(0x0, 0x103, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_19B9)
    Sleep(50)

    def lambda_19D1():
        OP_9B(0x0, 0x104, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_19D1)
    Sleep(50)

    def lambda_19E9():
        OP_9B(0x0, 0x109, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_19E9)
    Sleep(50)

    def lambda_1A01():
        OP_9B(0x0, 0x105, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1A01)
    Sleep(50)

    def lambda_1A19():
        OP_9B(0x0, 0x106, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1A19)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(0, 1000, 16000, 0)
    OP_68(350, 1000, 17640, 1500)
    MoveCamera(41, 16, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0035
    ChrTalk(
        0x8,
        (
            "#5Pチッ、まさか力ずくで\x01",
            "急襲してくるとはな……！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#00312F#12Pザックス。\x01",
            "お前がそこにいるって事は\x01",
            "ラストみてぇだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        "#5P……ああ、ランドルフ隊長。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#5Pだが俺たちも\x01",
            "《赤い星座》の一員として\x01",
            "ここを通すわけにはいかねぇ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0039
    ChrTalk(
        0x8,
        "#5P#4Sてめえら、気合いを入れろ！\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    #C0040
    ChrTalk(
        0x8,
        (
            "#5Pここを守りきれなかったら\x01",
            "副団長とお嬢にブッ殺されっぞ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0x9C4, 0xFA)

    #C0041
    ChrTalk(
        0x9,
        "#5P了解#4Rヤ ー#！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0x9C4, 0xFA)

    #C0042
    ChrTalk(
        0xC,
        "#5P全力で撃破する！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#00007F#12P望むところだ！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x106,
        (
            "#10707F#12Pアルカンシェルでの借り、\x01",
            "返してもらいます……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(11000, 500)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    BeginChrThread(0x8, 3, 0, 13)
    BeginChrThread(0x9, 3, 0, 12)
    BeginChrThread(0xC, 3, 0, 12)
    BeginChrThread(0xD, 3, 0, 14)
    BeginChrThread(0xE, 3, 0, 14)

    def lambda_1CE3():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CE3)

    def lambda_1CF8():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CF8)

    def lambda_1D0D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D0D)

    def lambda_1D22():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D22)

    def lambda_1D37():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D37)

    def lambda_1D4C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1D4C)
    Sleep(200)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x106, 0x1)
    Battle("BattleInfo_360", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 16)
    Return()

    # Function_9_174B end

    def Function_10_1DB1(): pass

    label("Function_10_1DB1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DCD")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_10_1DB1")

    label("loc_1DCD")

    Return()

    # Function_10_1DB1 end

    def Function_11_1DCE(): pass

    label("Function_11_1DCE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DEA")
    OP_A1(0xFE, 0x960, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_11_1DCE")

    label("loc_1DEA")

    Return()

    # Function_11_1DCE end

    def Function_12_1DEB(): pass

    label("Function_12_1DEB")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
    Return()

    # Function_12_1DEB end

    def Function_13_1E03(): pass

    label("Function_13_1E03")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
    Return()

    # Function_13_1E03 end

    def Function_14_1E1B(): pass

    label("Function_14_1E1B")

    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 11)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
    Return()

    # Function_14_1E1B end

    def Function_15_1E44(): pass

    label("Function_15_1E44")

    Sleep(2200)
    Sound(805, 0, 70, 0)
    Sound(531, 0, 70, 0)
    Sound(540, 0, 20, 0)
    Return()

    # Function_15_1E44 end

    def Function_16_1E5A(): pass

    label("Function_16_1E5A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("chr/ch42053.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00356.itc", 0x26)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 600, 0, 16100, 0)
    OP_90(0x103, 500, 0, 14300, 0)
    OP_90(0x104, -700, 0, 16200, 0)
    OP_90(0x105, -500, 0, 14500, 0)
    OP_90(0x106, 1500, 0, 15350, 0)
    OP_90(0x109, -1500, 0, 15050, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    Call(0, 17)
    SetChrPos(0x9, -2500, 0, 21000, 0)
    SetChrPos(0xC, 2000, 0, 22500, 45)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x3)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 200, 0, 19100, 180)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    VolumeBGM(0x32, 0x7D0)
    OP_68(-360, 1000, 18310, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15250, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14250, 2000)
    OP_6F(0x79)
    OP_0D()

    def lambda_201B():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_201B)
    WaitChrThread(0x8, 2)
    Sleep(500)

    #C0045
    ChrTalk(
        0x8,
        (
            "#5P#40W……ちっ……\x01",
            "ランドルフ隊長……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#5P#40Wあんた……団にいた頃より\x01",
            "はるかに強ぇじゃねえか……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#00306F#12Pま、今の職場で色々と\x01",
            "鍛えられてるからな。\x02\x03",

            "#00300F場数の違いだろ、場数の。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#5P#40Wハッ……\x01",
            "毎日が戦闘漬けの俺たちより\x01",
            "場数が上たぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#5P#40Wどんな職場だっての……\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_2169():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2169)
    WaitChrThread(0x8, 2)
    Sleep(500)
    Fade(500)
    Sound(514, 0, 100, 0)
    OP_68(-230, 1000, 18600, 500)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, -500, 0, 18250, 0)
    OP_0D()
    Sleep(300)

    #C0050
    ChrTalk(
        0x8,
        "#60W#5P#2S……気ぃ……つけろ………\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#60W#5P#2Sその中には………\x01",
            "………連中#4R㈲　㈲#の………\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        "#60W#5P#2S………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #C0053
    ChrTalk(
        0x101,
        "#00008F#12P……気絶したか？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#00306F#11Pああ……\x01",
            "完全に落ちてやがる。\x02\x03",

            "#00311F“連中の”……\x01",
            "いったい何のことだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#00208F#12Pトラップの可能性、\x01",
            "もしくは別の“敵”……？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        (
            "#10403F#12Pふむ、分からないけど\x01",
            "用心した方が良さそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x109,
        (
            "#10101F#12P……回復が必要なら\x01",
            "今の内に処置しましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14500, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x64, 0x7D0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    Call(0, 17)
    SetChrPos(0x0, 0, 0, 11900, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 0)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_1E5A end

    def Function_17_243E(): pass

    label("Function_17_243E")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, 1100, 0, 15000, 0)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, -2500, 0, 18000, 0)
    SetChrChipByIndex(0xC, 0x0)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, 2000, 0, 19500, 45)
    Return()

    # Function_17_243E end

    def Function_18_24D8(): pass

    label("Function_18_24D8")

    EventBegin(0x1)

    #C0058
    ChrTalk(
        0x101,
        (
            "#00000Fこっちは迎賓館だ。\x02\x03",

            "今夜の晩餐会までは\x01",
            "特に用はないな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 200, -1700, 180)
    OP_68(0, 700, -1700, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(37000, 0)
    EventEnd(0x4)
    Return()

    # Function_18_24D8 end

    SaveToFile()

Try(main)
