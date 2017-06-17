from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1390.bin",                # FileName
        "t1390",                    # MapName
        "t1390",                    # Location
        0x0000,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1390",                  # 0
        "職員ハンクス",           # 1
        "中年男性",               # 2
        "みーしぇ頭",             # 3
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(256, 0)                                        # 0

    ScpFunction((
        "Function_0_100",          # 00, 0
        "Function_1_127",          # 01, 1
        "Function_2_13A",          # 02, 2
        "Function_3_1437",         # 03, 3
        "Function_4_1482",         # 04, 4
        "Function_5_14CD",         # 05, 5
    ))


    def Function_0_100(): pass

    label("Function_0_100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_114")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_126")

    label("loc_114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_126")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 5)

    label("loc_126")

    Return()

    # Function_0_100 end

    def Function_1_127(): pass

    label("Function_1_127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_139")
    VolumeBGM(0x50, 0x32)
    ClearScenarioFlags(0x0, 0)

    label("loc_139")

    Return()

    # Function_1_127 end

    def Function_2_13A(): pass

    label("Function_2_13A")

    EventBegin(0x0)
    VolumeBGM(0x50, 0x3E8)
    FadeToDark(0, 0, -1)
    OP_68(-3080, 2600, -370, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19020, 0)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch28100.itc", 0x20)
    SoundLoad(2679)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x101, -4170, 0, 610, 90)
    SetChrPos(0x102, -2300, 0, 570, 270)
    SetChrPos(0x104, -2550, 0, 1990, 225)
    SetChrPos(0x109, -3870, 0, 2290, 180)
    SetChrPos(0x105, -3280, 0, -1000, 315)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x103, 210, 0, -4420, 0)
    SetChrPos(0x8, 210, 0, -4420, 0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-3080, 1600, -370, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0001
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F……ど、どうかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        "#00100Fうふ、かわいいわよ。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x109,
        "#10109Fええ、とっても似合ってます！\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F（全身覆ってるんだから\x01",
            "  似合うもなにもないような……）\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、着心地はどうだい？\x01",
            "なんだか暑そうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201Fああ……\x01",
            "けっこう中に熱気が\x01",
            "こもる感じかな。\x02\x03",

            "#05203Fあと、タテは合ってるけど\x01",
            "けっこうブカブカで\x01",
            "動きにくいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#00300F細かいことは\x01",
            "いーじゃねぇか。\x02\x03",

            "#00306Fちぇっ、うらやましいぜ。\x01",
            "ファンの女の子とさりげなく\x01",
            "ふれ合えるなんてよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211Fへ、変な言い方をするなって！\x01",
            "まったく……\x02\x03",

            "#05205F……あれ？\x01",
            "そういえば、ティオは？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#00105Fそういえば、さっき\x01",
            "職員さんに声をかけて\x01",
            "どこかに行ってしまったけど……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("ティオの声")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──ここです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-910, 1600, -2190, 3000)
    MoveCamera(289, 20, 0, 3000)

    def lambda_5C7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C7)
    Sleep(50)

    def lambda_5D7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D7)
    Sleep(50)

    def lambda_5E7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E7)
    Sleep(50)

    def lambda_5F7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5F7)
    Sleep(50)

    def lambda_607():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_607)
    OP_6F(0x79)
    Sound(121, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 3)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 4)

    def lambda_62E():

        label("loc_62E")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_62E")

    QueueWorkItem2(0x101, 1, lambda_62E)

    def lambda_640():

        label("loc_640")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_640")

    QueueWorkItem2(0x102, 1, lambda_640)

    def lambda_652():

        label("loc_652")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_652")

    QueueWorkItem2(0x104, 1, lambda_652)

    def lambda_664():

        label("loc_664")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_664")

    QueueWorkItem2(0x109, 1, lambda_664)

    def lambda_676():

        label("loc_676")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_676")

    QueueWorkItem2(0x105, 1, lambda_676)
    OP_68(-1670, 1600, -1050, 3000)
    MoveCamera(305, 23, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17980, 3000)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x8, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x79)

    #C0011
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205Fえ……\x01",
            "ティ、ティオなのか？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    #C0012
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#2679Vみししっ、みーしぇだヨ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xA77)
    OP_C9(0x1, 0x80000000)

    #C0013
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "お兄ちゃんったら、\x01",
            "あたしの顔を忘れたの？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        "#00305Fは～、こりゃまた……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_812")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆幕間でみーしぇに？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【会えた】\x01",          # 0
            "【会ってない】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_812")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_970")

    #C0016
    ChrTalk(
        0x102,
        (
            "#00102Fかわいい……\x01",
            "かわいいわ、ティオちゃん！\x02\x03",

            "#00105Fそれに、\x01",
            "そのキャラクターって確か……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522Fええ、みっしぃの妹の\x01",
            "『みーしぇ』です。\x02\x03",

            "#05524Fドジばかりの兄を\x01",
            "いつも生暖かく見守っている\x01",
            "健気な女の子なんです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F（な、生暖かく……）\x02\x03",

            "#05203Fそういえば、\x01",
            "前にＭＷＬに来たときにも\x01",
            "会ったんだったな……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABB")

    label("loc_970")


    #C0019
    ChrTalk(
        0x102,
        (
            "#00102Fかわいい……\x01",
            "かわいいわ、ティオちゃん！\x02\x03",

            "#00105Fでも、このキャラクターは\x01",
            "一体……？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522Fええ、みっしぃの妹の\x01",
            "『みーしぇ』です。\x02\x03",

            "#05524Fドジばかりの兄を\x01",
            "いつも生暖かく見守っている\x01",
            "健気な女の子なんです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F（な、生暖かく……）\x02\x03",

            "#05203Fそういえば、\x01",
            "みっしぃの妹がいるって\x01",
            "前にも聞いてたっけ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABB")


    #C0022
    ChrTalk(
        0x8,
        (
            "いやあ、さっき突然\x01",
            "貸してくれって\x01",
            "頼まれちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "みーしぇの方は\x01",
            "シフトに余裕があったから\x01",
            "ＯＫしたってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x109,
        (
            "#10105Fな、なるほど……\x02\x03",

            "でも、突然そんなものを\x01",
            "着て現れたってことは……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524Fロイドさんのみっしぃぶりを、\x01",
            "わたしが陰ながらサポートします。\x02\x03",

            "#05521Fなにかポカをやらかしたら、\x01",
            "容赦なく蹴りをいれますので。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0026
    ChrTalk(
        0x105,
        (
            "#10309Fあはは、妹の愛のムチか。\x01",
            "愛されてるねえ、お兄ちゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F勘弁してほしいんですけど……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0028
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201F……っていうか、演技指導とかは\x01",
            "していただけないんですか？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CF6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CF6)
    Sleep(50)

    def lambda_D06():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D06)
    Sleep(50)

    def lambda_D16():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D16)
    Sleep(50)

    def lambda_D26():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D26)
    Sleep(50)

    def lambda_D36():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D36)
    Sleep(300)

    #C0029
    ChrTalk(
        0x8,
        (
            "悪いけど、\x01",
            "とてもそんなヒマはないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "そろそろみっしぃの\x01",
            "巡回時間が近いしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "なあに、それっぽい言動を\x01",
            "心がければ何とかなるさ、多分！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F（ふ、不安だ……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "あと、午前は巡回の後、\x01",
            "テーマパーク内の広場で\x01",
            "みっしぃダンスショウがあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "そこだけは、僕なりに\x01",
            "演技マニュアルをしたためておいた。\x01",
            "……パッと読んで覚えてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダンスマニュアルを\x01",
            "見せてもらった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "情熱的に、それでいて\x01",
            "ファンシーに踊るべし。\x01\x01",
            "※最後のキメゼリフに、\x01",
            "　『エンジョイみっしぃ☆』と\x01",
            "　叫ぶのを忘れないこと。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x104,
        "#00306Fこ、これはまた……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        (
            "#10112Fありえないくらい\x01",
            "アバウトですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "実を言うと、\x01",
            "みっしぃのキャラづけは\x01",
            "役者の人に任せきりでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "テーマパーク創設以来、\x01",
            "ロクなマニュアルは\x01",
            "何一つ作ってないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "まあ、ミスしたら\x01",
            "そのときはそのときってことで。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0042
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524Fわたしが監督する以上\x01",
            "ミスは許しませんけどね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206Fど、どうしろってんだよ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0044
    ChrTalk(
        0x8,
        (
            "おっと……時間だ。\x01",
            "そろそろ準備を頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11EC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11EC)
    Sleep(50)

    def lambda_11FC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11FC)
    Sleep(50)

    def lambda_120C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_120C)
    Sleep(50)

    def lambda_121C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_121C)
    Sleep(300)

    #C0045
    ChrTalk(
        0x102,
        (
            "#00100Fそれじゃあ、私たちは\x01",
            "園内の見回りでもしながら\x01",
            "時間を潰しているわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x105,
        "#10300Fフフ、幸運を祈るよ。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520Fでは、行きましょうロイドさん。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205Fあ、ああ……\x02\x03",

            "#05203F（とにかく……今までに得た\x01",
            "  みっしぃのイメージを\x01",
            "  搾り出してみるしかないか。）\x02\x03",

            "#05200F（それと……ダンスの合言葉は\x01",
            "  『エンジョイみっしぃ☆』、か。\x01",
            "  覚えていた方がよさそうだな。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "それじゃ、\x01",
            "子供たちの夢のために\x01",
            "がんばってくれ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "よろしく頼むよ！\x01",
            "みっしぃ、みーしぇ！！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x0)
    OP_29(0x86, 0x1, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("t1030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_13A end

    def Function_3_1437(): pass

    label("Function_3_1437")


    def lambda_143C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_143C)

    def lambda_144D():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_144D)
    WaitChrThread(0x103, 1)
    OP_95(0x103, -1210, 0, -1620, 2000, 0x0)
    TurnDirection(0x103, 0x101, 500)
    Return()

    # Function_3_1437 end

    def Function_4_1482(): pass

    label("Function_4_1482")


    def lambda_1487():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1487)

    def lambda_1498():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1498)
    WaitChrThread(0x8, 1)
    OP_95(0x8, -10, 0, -300, 2000, 0x0)
    OP_93(0x8, 0x10E, 0x1F4)
    Return()

    # Function_4_1482 end

    def Function_5_14CD(): pass

    label("Function_5_14CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("apl/ch51403.itc", 0x20)
    LoadChrToIndex("chr/ch47300.itc", 0x22)
    SoundLoad(802)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x1)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x9, 0x22)
    SetChrFlags(0x9, 0x8000)
    OP_68(1860, 2600, 260, 0)
    MoveCamera(320, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15130, 0)
    SetChrPos(0x101, 380, 0, 1140, 90)
    SetChrPos(0x103, 2500, 0, 1020, 270)
    SetChrPos(0x9, 210, 0, -4420, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_68(1860, 1600, 260, 3000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()

    #C0051
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F……よいしょ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x20)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1370, 200, 310, 180)
    Sound(802, 0, 100, 0)
    OP_0D()

    #C0052
    ChrTalk(
        0x103,
        "#05526Fふう……汗だくです。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00009Fはは……\x01",
            "すごくがんばったみたいだな。\x02\x03",

            "#00000Fお疲れ様、ティオ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17C8")

    #C0054
    ChrTalk(
        0x103,
        (
            "#05522Fいえ、ロイドさんのみっしぃぶりも\x01",
            "申し分ない出来でした。\x02\x03",

            "#05524F……その、最後のダンスも\x01",
            "一緒に踊れて楽しかったですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#00009Fえっと、はは……\x01",
            "なんだか照れるな。\x02\x03",

            "#00003F……さて、と。\x01",
            "そろそろみんなとも\x01",
            "合流したいところだけど。\x02\x03",

            "#00005F本物のみっしぃの役者さんは\x01",
            "まだなのかな……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E2")

    label("loc_17C8")


    #C0056
    ChrTalk(
        0x103,
        (
            "#05522Fロイドさんも。\x01",
            "荒削りですがよく\x01",
            "成し遂げたと思います。\x02\x03",

            "#05524Fわたしも監督した甲斐が\x01",
            "あったというものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00000Fはは……\x01",
            "本当、助かったよ。\x02\x03",

            "#00003F……さて、と。\x01",
            "そろそろみんなとも\x01",
            "合流したいところだけど。\x02\x03",

            "#00005F本物のみっしぃの役者さんは\x01",
            "まだなのかな……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E2")


    #C0058
    ChrTalk(
        0x103,
        "#05520Fそういえば、遅いような──\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("中年男性の声")

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S──ガ～ッハッハッハ！\x01",
            "待たせちまったな！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(1590, 1600, -1210, 3000)

    def lambda_19A0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19A0)
    Sleep(50)

    def lambda_19B0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19B0)
    OP_6F(0x1)
    Sound(121, 0, 100, 0)
    ClearChrFlags(0x9, 0x80)

    def lambda_19CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_19CA)

    def lambda_19DB():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_19DB)
    WaitChrThread(0x9, 1)
    Sleep(300)

    #C0060
    ChrTalk(
        0x101,
        "#00011Fへ…………？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        "#05521F…………！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(300)

    #C0062
    ChrTalk(
        0x9,
        "げっぷ……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    #C0063
    ChrTalk(
        0x9,
        "ガッハッハ、悪い悪い！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "もらってきた薬が食後じゃないと\x01",
            "飲めないヤツらしくてな！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "朝飯も抜いてたから、\x01",
            "ついついガッツリ\x01",
            "食っちまったのよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "……で、オレっちの着ぐるみは\x01",
            "そこのロッカーかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x103)

    #C0067
    ChrTalk(
        0x9,
        (
            "……あん？\x01",
            "目を真ん丸にしてどうしたんでぇ？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "そういや、どっかで見た\x01",
            "顔みてえだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "ま、何にしろ恩に着るぜ。\x01",
            "ワンダーランドにみっしぃは\x01",
            "必要不可欠だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "俺のいない穴を\x01",
            "よく埋めてくれたぜ。\x01",
            "ガッハッハ……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "おっと、ダベってる暇はねえ。\x01",
            "さっさと着替えて\x01",
            "午後の準備をしなきゃあな。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-720, 1600, -10, 3000)

    def lambda_1C92():

        label("loc_1C92")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1C92")

    QueueWorkItem2(0x101, 1, lambda_1C92)

    def lambda_1CA4():

        label("loc_1CA4")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1CA4")

    QueueWorkItem2(0x103, 1, lambda_1CA4)
    OP_95(0x9, -2860, 0, -1350, 2000, 0x0)
    OP_95(0x9, -4080, 0, 260, 2000, 0x0)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(1000)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x103)
    VolumeBGM(0x46, 0x3E8)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Sound(898, 0, 100, 0)
    Sleep(1000)
    Sound(1000, 0, 100, 0)
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()
    VolumeBGM(0x50, 0x3E8)
    OP_93(0x9, 0x5A, 0x1F4)

    #N0072
    NpcTalk(
        0x9,
        "みっしぃ",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "──変身完了～☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0073
    NpcTalk(
        0x9,
        "みっしぃ",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "お兄さんにお嬢ちゃん、\x01",
            "本当にありがとうね！\x01",
            "ボク、助かっちゃったヨ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0074
    NpcTalk(
        0x9,
        "みっしぃ",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "あとは任せてネ～！\x01",
            "みししっ、それじゃっ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1590, 1600, -1210, 3000)
    OP_95(0x9, -2860, 0, -1350, 2000, 0x0)
    OP_95(0x9, 370, 0, -2050, 2000, 0x0)

    def lambda_1E53():
        OP_95(0xFE, 210, 0, -4420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E53)
    Sound(121, 0, 100, 0)
    Sleep(500)

    def lambda_1E76():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1E76)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    OP_93(0x103, 0xB4, 0x1F4)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    Sound(890, 0, 100, 0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x103)

    #C0075
    ChrTalk(
        0x101,
        (
            "#00005F（プ、プロだ……\x01",
            "  声色まで全然違う……）\x02\x03",

            "#00006F（あまりにも完璧なほどに\x01",
            "  みっしぃだ……けど……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0076
    ChrTalk(
        0x101,
        (
            "#00011F#4S（イメージと\x01",
            "  全然違うじゃないかッ！！）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0077
    ChrTalk(
        0x101,
        "#00006F……コホン、えーっと……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0078
    ChrTalk(
        0x101,
        (
            "#00012Fと、とにかく\x01",
            "みんなのところに帰ろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        "#05520F………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(1000)
    SetScenarioFlags(0x22, 3)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_14CD end

    SaveToFile()

Try(main)
