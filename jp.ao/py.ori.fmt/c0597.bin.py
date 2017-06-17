from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0597.bin",                # FileName
        "c0597",                    # MapName
        "c0597",                    # Location
        0x0029,                     # MapIndex
        "ed7302",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 0, 0, 1],
    )

    BuildStringList((
        "c0597",                  # 0
        "キリカ",                 # 1
        "レクター",               # 2
        "ダミー",                 # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       0,       64000,   1200,    0,       1500,    64000,   0x007C, 0,  2,  0x0000)

    ChipFrameInfo(288, 0)                                        # 0

    ScpFunction((
        "Function_0_120",          # 00, 0
        "Function_1_121",          # 01, 1
        "Function_2_13E",          # 02, 2
        "Function_3_43A",          # 03, 3
        "Function_4_2AF1",         # 04, 4
    ))


    def Function_0_120(): pass

    label("Function_0_120")

    Return()

    # Function_0_120 end

    def Function_1_121(): pass

    label("Function_1_121")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137")
    OP_66(0x0, 0x1)

    label("loc_137")

    ClearMapObjFlags(0x10, 0x10)
    Return()

    # Function_1_121 end

    def Function_2_13E(): pass

    label("Function_2_13E")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1150, 63000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 0, 30, 62300, 0)
    SetChrPos(0x102, -900, 30, 60400, 0)
    SetChrPos(0x104, 900, 30, 60400, 0)
    SetChrPos(0x103, -300, 30, 59700, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x101,
        (
            "#00003F#11P（帝国軍情報局所属、\x01",
            "  レクター・アランドールか。）\x02\x03",

            "#00013F（油断できる相手じゃない……\x01",
            "  入るなら覚悟を固めよう。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "一度、部屋に入ったら\x01",
            "しばらく装備やアイテム、オーブメントを\x01",
            "整えることができなくなります。\x02\x03",

            "また、残ったクエストなども\x01",
            "全て終了するので注意してください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ他に用事がある】\x01",            # 0
            "【扉を開けて部屋の中に入る】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_36E"),
        (0, "loc_41D"),
        (SWITCH_DEFAULT, "loc_439"),
    )


    label("loc_36E")

    Sound(103, 0, 100, 0)
    OP_71(0x10, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x10)
    StopBGM(0xFA0)
    FadeToDark(1000, 0, -1)

    def lambda_397():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_397)
    Sleep(300)

    def lambda_3B4():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B4)
    Sleep(300)

    def lambda_3D1():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3D1)
    Sleep(300)

    def lambda_3EE():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3EE)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x103, 0xFF)
    WaitBGM()
    Call(0, 3)
    Jump("loc_439")

    label("loc_41D")

    SetChrPos(0x0, 0, 30, 61800, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_439")

    label("loc_439")

    Return()

    # Function_2_13E end

    def Function_3_43A(): pass

    label("Function_3_43A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    LoadChrToIndex("chr/ch07300.itc", 0x1F)
    LoadChrToIndex("apl/ch51526.itc", 0x20)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03500.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03400.itp")
    SetChrPos(0x101, -700, 30, 101500, 0)
    SetChrPos(0x102, 300, 30, 101500, 0)
    SetChrPos(0x104, 500, 30, 100400, 0)
    SetChrPos(0x103, -900, 30, 100400, 0)
    SetChrPos(0xA, -200, 0, 107950, 0)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -100, 100, 112500, 180)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 98000, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, 112500, 0)
    MoveCamera(27, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)

    def lambda_5C0():
        OP_97(0x101, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5C0)
    Sleep(100)

    def lambda_5DD():
        OP_97(0x102, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5DD)
    Sleep(100)

    def lambda_5FA():
        OP_97(0x104, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5FA)
    Sleep(100)

    def lambda_617():
        OP_97(0x103, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_617)
    OP_68(0, 1100, 110500, 3000)
    MoveCamera(33, 17, 0, 3000)
    SetCameraDistance(18000, 3000)
    Sound(104, 0, 60, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x103, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0003
    AnonymousTalk(
        0x9,
        (
            "よ、ゴクローさん。\x02\x03",

            "どうやら国防軍の連中は\x01",
            "引き連れてないみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    PlayBGM("ed7564", 0)
    Sleep(500)

    #C0004
    ChrTalk(
        0x101,
        (
            "#12P#00001F……だからといって\x01",
            "あなたを捕まえるつもりが\x01",
            "無いと思わない方がいいですよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00101F《赤い星座》の所業……\x01",
            "貴方にも関係がないとは\x01",
            "言わせません。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        "#5P#03504F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#00306F#12P単刀直入に聞くぜ。\x01",
            "なんでクロスベルに現れた？\x02\x03",

            "#00311Fそれと叔父貴たち……\x01",
            "《赤い星座》は何処に行った？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        (
            "#12P#00201Fクライアントならば\x01",
            "もちろんご存知ですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "#5P#03506Fんー、まずは最初の質問に\x01",
            "答えさせてもらおうか。\x02\x03",

            "#03508Fオレが来たのは今日……\x01",
            "帝都からの始発でな。\x02\x03",

            "#03501Fもちろんギリアスのオッサンの\x01",
            "指示によるものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        "#00108F《鉄血宰相》の……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#12P#00001F……どういう目的で？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x9,
        (
            "#5P#03504Fその前に、アンタらに\x01",
            "耳寄りな情報を教えてやろう。\x02\x03",

            "#03501F──今日の午後くらいに\x01",
            "帝国軍が侵攻してくるぞ。\x02",
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0013
    ChrTalk(
        0x101,
        "#12P#00007F！！！\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#00105Fな……！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#12P#00211F……冗談きついです。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00303F#12Pいや……この状況じゃ、\x01",
            "本当だとしてもおかしくねぇ。\x02\x03",

            "#00301Fもちろんベルガード門からだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "#5P#03504Fああ、既にガレリア要塞に\x01",
            "機甲師団が集結している。\x02\x03",

            "#03508Fま、たかだか一個師団だが……\x02\x03",

            "#03501F最新の重戦車が揃ってるから\x01",
            "クロスベルの装甲車くらいは\x01",
            "余裕で蹴散らすだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#12P#00010Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#00107Fす、すぐに警備隊に──\x01",
            "ううん国防軍に伝えないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            "#5P#03508Fいや？\x01",
            "とっくに伝わってるぜ。\x02\x03",

            "#03503F一応、事前の通達は\x01",
            "自治州政府に行ってるしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#12P#00011F！？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            "#5P#03506Fなのにディーターのオッサンは\x01",
            "ＩＢＣの資産凍結を撤回せず、\x01",
            "大統領なんかに就任しやがった。\x02\x03",

            "侵攻してくる帝国軍を防ぐのが\x01",
            "不可能なのは判っているはずなのに。\x02\x03",

            "#03502F──それがオレが改めて\x01",
            "クロスベル入りした理由ってわけだ。\x02",
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

    def lambda_E1F():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E1F)
    Sleep(30)

    def lambda_E2F():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E2F)
    Sleep(30)

    def lambda_E3F():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E3F)
    Sleep(30)

    def lambda_E4F():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E4F)
    Sleep(30)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)

    #C0023
    ChrTalk(
        0x104,
        (
            "#00301F#11Pおい……どういうことだ？\x02\x03",

            "その状況で、アリオスのオッサンを\x01",
            "国防軍の長官に任命してどうなる？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#5P#00006F……分からない。\x02\x03",

            "いくらアリオスさんでも\x01",
            "戦車相手に戦えるわけがないし。\x02\x03",

            "#00008Fどう考えても、何か切り札が\x01",
            "あるとしか思えない判断だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#6P#00200Fもしかして共和国と和解して\x01",
            "帝国軍への牽制を……？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#11P#00106Fううん、もしそうだったら\x01",
            "大統領演説で共和国の事まで\x01",
            "あんな風に非難する筈がないわ……\x02\x03",

            "#00108Fあくまでカルバードとも\x01",
            "本気で対決するつもりのはずよ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)

    #N0027
    NpcTalk(
        0x8,
        "女性の声",
        "──ええ、そうでしょうね。\x02",
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
    OP_68(0, 1100, 102500, 2000)
    SetCameraDistance(17500, 2000)

    def lambda_110E():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_110E)
    Sleep(50)

    def lambda_111E():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_111E)
    Sleep(50)

    def lambda_112E():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_112E)
    Sleep(50)

    def lambda_113E():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_113E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)

    def lambda_1167():
        OP_96(0xFE, 0x0, 0x0, 0x18C7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1167)

    def lambda_1181():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1181)
    WaitChrThread(0x8, 1)
    Sound(104, 0, 60, 0)
    OP_6F(0x79)

    #C0028
    ChrTalk(
        0x101,
        "#00005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        "#00205Fあなたは……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        "#5P#N#00305Fキリカさんじゃないッスか！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0031
    AnonymousTalk(
        0x8,
        (
            "──お久しぶり。\x02\x03",

            "アランドール大尉も。\x01",
            "遅れて済まなかったわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    def lambda_12B4():
        OP_96(0xFE, 0xFFFFFE70, 0x0, 0x1A5E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12B4)
    Sleep(1000)
    Fade(500)
    OP_68(760, 1100, 109730, 0)
    MoveCamera(37, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 800, 30, 108500, 270)
    SetChrPos(0x102, 1800, 30, 108300, 270)
    SetChrPos(0x104, 2300, 30, 107100, 270)
    SetChrPos(0x103, 1000, 30, 107100, 270)

    def lambda_1348():

        label("loc_1348")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1348")

    QueueWorkItem2(0x101, 2, lambda_1348)

    def lambda_135A():

        label("loc_135A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_135A")

    QueueWorkItem2(0x102, 2, lambda_135A)

    def lambda_136C():

        label("loc_136C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_136C")

    QueueWorkItem2(0x103, 2, lambda_136C)

    def lambda_137E():

        label("loc_137E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_137E")

    QueueWorkItem2(0x104, 2, lambda_137E)

    def lambda_1390():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1390)
    Sleep(100)

    def lambda_13AD():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13AD)
    Sleep(100)

    def lambda_13CA():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13CA)
    Sleep(100)

    def lambda_13E7():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13E7)
    Sleep(1100)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    #C0032
    ChrTalk(
        0x9,
        (
            "#5P#03504Fま、オレも来たばかりだし\x01",
            "気にしないでくれ。\x02\x03",

            "#03500Fそっちの様子はどうよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#12P#03403Fおおむね予想通りの進行ね。\x02\x03",

            "#03401F現在、アルタイル市の郊外に\x01",
            "空挺機甲師団が展開しているわ。\x02",
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

    #C0034
    ChrTalk(
        0x101,
        "#11P#00010F！！！？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        "#00108Fきょ、共和国軍も……！？\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#12P#00310F空挺機甲師団ってことは……\x01",
            "戦車と飛行艇の混成部隊かよ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)

    #C0037
    ChrTalk(
        0x8,
        (
            "#6P#03403Fええ、機動力のある新型戦車と\x01",
            "軍用艇#6Rガンシップ#の組み合わせね。\x02\x03",

            "#03400Fカルバード軍の中でも\x01",
            "最高の機動力を誇っているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#11P#00013Fそんな……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x103,
        "#12P#00208F挟み撃ち……という事ですか？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#6P#03400Fええ、貴方たちにとっては\x01",
            "不本意な事態でしょうけど。\x02\x03",

            "#03403F──でも、この状況になるのは\x01",
            "少し考えれば分かるはずよ。\x02\x03",

            "にもかかわらず\x01",
            "ディーター・クロイスは\x01",
            "一切の妥協なく強硬姿勢に出た。\x02\x03",

            "#03402Fこれは一体、どういう事かしら？\x02",
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

    #C0041
    ChrTalk(
        0x9,
        (
            "#5P#03504Fそれともう一つ……\x02\x03",

            "#03502F２番目の質問について\x01",
            "大サービスで答えてやろう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_185A():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_185A)
    Sleep(50)

    def lambda_186A():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_186A)
    Sleep(50)

    def lambda_187A():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_187A)
    Sleep(50)

    def lambda_188A():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_188A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    #C0042
    ChrTalk(
        0x101,
        "#11P#00008F２番目……？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        "#12P#00301F……《赤い星座》の行方か？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "#5P#03505Fああ、答えはカンタン。\x02\x03",

            "#03506F──帝国政府#8Rオ レ た ち#だって\x01",
            "全然知らないんだな、これが。\x02",
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0045
    ChrTalk(
        0x102,
        "#00107Fそ、そんな……！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#12P#00211Fここまでぶっちゃけておいて\x01",
            "それは無いのでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#12P#00310Fハッ、クロスベルで暴れた後、\x01",
            "契約は終了したってことか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#11P#00011Fい、いや──待ってくれ。\x02\x03",

            "#00003F《赤い星座》は、通商会議の時、\x01",
            "帝国政府と契約を結んでいた……\x02\x03",

            "契約内容は、宰相の命を狙う\x01",
            "テロリストたちの殲滅……\x02\x03",

            "#00013Fそれは間違いないですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        "#5P#03504Fああ、連中もそう言ってたろ？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#11P#00008F……でも、ひょっとして……\x02\x03",

            "#00010F帝国政府との契約は\x01",
            "その時に#8R㈲　㈲　㈲　㈲#切れていたんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1C24():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C24)
    Sleep(50)

    def lambda_1C34():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C34)
    Sleep(50)

    def lambda_1C44():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C44)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0051
    ChrTalk(
        0x102,
        "#00105Fえ────\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#12P#00205Fそれって……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        "#12P#00301F……まさか………\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "#5P#03504F……クックックッ。\x02\x03",

            "#03502Fロイド、やっぱりアンタ、\x01",
            "わりと諜報に向いてるかもなァ。\x02\x03",

            "#03509Fもう少し性格が悪ければだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#11P#00007Fそ、それじゃあ……！\x02",
    )

    CloseMessageWindow()

    def lambda_1D61():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D61)
    Sleep(50)

    def lambda_1D71():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D71)
    Sleep(50)

    def lambda_1D81():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D81)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0056
    ChrTalk(
        0x9,
        (
            "#5P#03503F──答えはイエスだ。\x02\x03",

            "通商会議以降、帝国政府は\x01",
            "《赤い星座》と関わりはない。\x02\x03",

            "#03508Fにも関わらず、\x01",
            "連中がクロスベルに残ってたのは\x01",
            "こちらも妙だと思っていたが……\x02\x03",

            "#03501Fまさかあんなことを\x01",
            "いきなりブチかますとはなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#00106Fそんな……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        (
            "#12P#00308Fじゃあ、どうして\x01",
            "叔父貴たちはあんな真似を……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        (
            "#12P#00201F……まさか《結社》と\x01",
            "新たな契約を結んだとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "#6P#03403Fいえ、それもおかしな話ね。\x02\x03",

            "#03401Fかつてリベールの異変では\x01",
            "彼らは『強化猟兵』という\x01",
            "独自の戦闘部隊を運用していた。\x02\x03",

            "もしクロスベルを襲撃するなら\x01",
            "そういった部隊にさせたでしょう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FDA():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1FDA)
    Sleep(50)

    def lambda_1FEA():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1FEA)
    Sleep(50)

    def lambda_1FFA():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FFA)
    Sleep(50)

    def lambda_200A():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_200A)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    #C0061
    ChrTalk(
        0x103,
        "#12P#00200F……なるほど。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#00108Fわざわざ外部の猟兵団を\x01",
            "雇う必要はないわけですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#11P#00008F#30W……そうなると……\x01",
            "他の候補は絞られてくる。\x02\x03",

            "#00003Fいかにも帝国政府が\x01",
            "黒幕と思われるような状況で……\x02\x03",

            "クロスベル市を襲撃させて\x01",
            "何らかの“得”をした勢力……\x02\x03",

            "そして最高ランクの猟兵団と\x01",
            "長期契約を結べるほどの\x01",
            "莫大な資金力を持っている勢力……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0064
    ChrTalk(
        0x101,
        "#11P#00011F──────え。\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7203", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0065
    ChrTalk(
        0x9,
        "#5P#03504Fま、そういう事かね？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "#6P#03401F……信じがたい可能性にこそ\x01",
            "往々にして真実は潜むものよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        "#00105Fちょ、ちょっと待って！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        "#12P#00208Fい、今の話の流れだと……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#00307F該当しそうなのは\x01",
            "一つしかねえだろうが！？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00002F#11Pい、いや……\x01",
            "さすがに決め付けはまずい。\x02\x03",

            "#00006F──レクター大尉、キリカさん。\x02\x03",

            "情報提供には感謝しますが\x01",
            "あなた方の立場も立場です。\x02\x03",

            "#00013Fここから先は、自分たちで──\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_23A7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_23A7)
    Sleep(50)

    def lambda_23B7():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_23B7)
    Sleep(50)

    def lambda_23C7():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_23C7)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0071
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013Fはい！\x01",
            "特務支援課、バニングスで──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("女性の声")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "よ、よかった！\x01",
            "ちゃんと繋がって……\x02\x03",

            "ロイド、セシルよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0073
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011Fセシル姉？\x02\x03",

            "#00001Fそんな慌てて……\x01",
            "何かあったのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セシルの声")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そ、それが……\x02\x03",

            "さっき、アリオスさんが\x01",
            "このビルにやって来たの。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0075
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fアリオスさんが！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セシルの声")

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そ、それで……\x02\x03",

            "キーアちゃんを連れて\x01",
            "そのまま出ていってしまって……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0077
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F#4S！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セシルの声")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "私も止めようとしたんだけど\x01",
            "キーアちゃんが……\x02\x03",

            "とにかく戻って来れる？\x01",
            "詳しい状況を説明するから！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0079
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00010Fわ、分かった！\x01",
            "そのまま待っててくれ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 40, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x1)
    Sound(804, 0, 100, 0)

    #C0080
    ChrTalk(
        0x102,
        "#00101Fど、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        "#12P#00301Fお前、スゲェ血相だぞ？\x02",
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
    OP_0D()
    TurnDirection(0x101, 0x104, 500)

    #C0082
    ChrTalk(
        0x101,
        (
            "#5P#00013Fアリオスさんが支援課に来て\x01",
            "キーアを連れて行った……！\x02",
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

    #C0083
    ChrTalk(
        0x102,
        "#00105F#4S！？\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0084
    ChrTalk(
        0x104,
        "#12P#00307F#4Sなんだとッ！？\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x103,
        "#12P#00201F一体どうして……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#5P#00010Fとにかく支援課に戻ろう！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    #C0087
    ChrTalk(
        0x101,
        (
            "#11P#00007Fキリカさん、レクターさん！\x01",
            "俺たちはこれで失礼します！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        "#6P#03400Fええ、気をつけて。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        "#5P#03509Fま、頑張れよな～。\x02",
    )

    CloseMessageWindow()

    def lambda_2964():

        label("loc_2964")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2964")

    QueueWorkItem2(0x8, 2, lambda_2964)
    OP_68(400, 1100, 103800, 3000)
    MoveCamera(30, 15, 0, 3000)
    SetCameraDistance(19500, 3000)
    BeginChrThread(0x103, 3, 0, 4)
    Sleep(250)
    BeginChrThread(0x104, 3, 0, 4)
    Sleep(250)
    BeginChrThread(0x101, 3, 0, 4)
    Sleep(250)
    BeginChrThread(0x102, 3, 0, 4)
    Sleep(600)
    Sound(103, 0, 100, 0)
    WaitChrThread(0x102, 3)
    Sound(104, 0, 100, 0)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1100, 110450, 0)
    MoveCamera(30, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrSubChip(0x9, 0x1)
    OP_0D()
    Sleep(300)

    #C0090
    ChrTalk(
        0x9,
        (
            "#03506F#5Pやっぱあの嬢ちゃんが\x01",
            "全ての“鍵”だったか。\x02\x03",

            "#03508Fなあ、間に合うと思うか？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        "#03401F#5Pそうね……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    #C0092
    ChrTalk(
        0x8,
        "#03403F#5P──多分、難しいでしょう。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    SetScenarioFlags(0x23, 6)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_43A end

    def Function_4_2AF1(): pass

    label("Function_4_2AF1")

    OP_92(0xFE, 0x0, 0x18894, 0x1F4)

    def lambda_2B03():
        OP_95(0xFE, 0, 0, 101000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B03)
    WaitChrThread(0xFE, 1)

    def lambda_2B21():
        OP_95(0xFE, 0, 0, 98000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B21)

    def lambda_2B3B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B3B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_4_2AF1 end

    SaveToFile()

Try(main)
