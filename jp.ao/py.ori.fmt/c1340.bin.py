from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1340.bin",                # FileName
        "c1340",                    # MapName
        "c1340",                    # Location
        0x001D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 53000, 0, 20000, 0, 0, 1, 29, 0, 0, 0, 2],
    )

    BuildStringList((
        "c1340",                  # 0
        "マリアベル",             # 1
    ))

    AddCharChip((
        "chr/ch05502.itc",                   # 00
    ))

    DeclNpc(55029,   180,     128820,  180,  389,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)

    DeclActor(47960,   0,       123700,  1200,    47960,   800,     123700,  0x007C, 0,  3,  0x0000)
    DeclActor(53000,   0,       45600,   1200,    53000,   800,     45600,   0x007C, 0,  6,  0x0000)
    DeclActor(55000,   150,     128800,  2500,    55000,   1800,    128800,  0x007E, 0,  4,  0x0000)

    ChipFrameInfo(324, 0)                                        # 0

    ScpFunction((
        "Function_0_144",          # 00, 0
        "Function_1_19E",          # 01, 1
        "Function_2_1A5",          # 02, 2
        "Function_3_1C2",          # 03, 3
        "Function_4_26C",          # 04, 4
        "Function_5_270",          # 05, 5
        "Function_6_3DF",          # 06, 6
        "Function_7_1D53",         # 07, 7
        "Function_8_2AF8",         # 08, 8
    ))


    def Function_0_144(): pass

    label("Function_0_144")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15C")
    ClearScenarioFlags(0x25, 1)
    Call(0, 1)

    label("loc_15C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18E")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)

    label("loc_18E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_19D")
    ClearScenarioFlags(0x22, 1)
    Event(0, 7)

    label("loc_19D")

    Return()

    # Function_0_144 end

    def Function_1_19E(): pass

    label("Function_1_19E")

    Sound(160, 0, 100, 0)
    Return()

    # Function_1_19E end

    def Function_2_1A5(): pass

    label("Function_2_1A5")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1")
    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x1, 0x1)

    label("loc_1C1")

    Return()

    # Function_2_1A5 end

    def Function_3_1C2(): pass

    label("Function_3_1C2")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "車雑誌『月間カーマニアvol.2』がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36F, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_268")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "ペイントパターン\x01\x07\x02",

            "『ワイルドカラー』\x07\x00",
            "を覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36F, 1)

    label("loc_268")

    TalkEnd(0xFF)
    Return()

    # Function_3_1C2 end

    def Function_4_26C(): pass

    label("Function_4_26C")

    Call(0, 5)
    Return()

    # Function_4_26C end

    def Function_5_270(): pass

    label("Function_5_270")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E")

    #C0003
    ChrTalk(
        0x8,
        (
            "#02901F憎き怪盗Ｂに盗まれた\x01",
            "ローゼンベルク人形は５体です。\x02\x03",

            "#02903Fわたくしの大切なあの子達を\x01",
            "かどわかすなんて……\x01",
            "到底許す事の出来ない所業ですわ。\x02\x03",

            "#02900F皆さん、どうか\x01",
            "よろしく頼みましたわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3DB")

    label("loc_34E")


    #C0004
    ChrTalk(
        0x8,
        (
            "#02903Fわたくしの大切なあの子達を\x01",
            "かどわかすなんて……\x01",
            "到底許す事の出来ない所業ですわ。\x02\x03",

            "#02901F皆さん、どうか\x01",
            "よろしく頼みましたわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DB")

    TalkEnd(0x8)
    Return()

    # Function_5_270 end

    def Function_6_3DF(): pass

    label("Function_6_3DF")

    EventBegin(0x0)
    Fade(1000)
    OP_68(53250, 1500, 45110, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18430, 0)
    SetChrPos(0x102, 52950, 0, 44240, 0)
    SetChrPos(0x101, 52220, 0, 43070, 0)
    SetChrPos(0x104, 53710, 0, 43070, 0)
    SetChrPos(0x109, 51640, 0, 42010, 0)
    SetChrPos(0x103, 52930, 0, 42010, 0)
    SetChrPos(0x105, 54450, 0, 42010, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    OP_9B(0x0, 0x102, 0x0, 0x3E8, 0x5DC, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(500)

    #C0005
    ChrTalk(
        0x102,
        "#12P#00100F──ベル、私よ。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("マリアベルの声")

    #A0006
    AnonymousTalk(
        0xFF,
        "ええ、お入りなさいな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0007
    ChrTalk(
        0x102,
        "#12P#00100F失礼するわね。\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    Sleep(300)

    def lambda_54B():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54B)
    Sleep(100)

    def lambda_568():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_568)

    def lambda_582():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_582)

    def lambda_59C():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_59C)

    def lambda_5B6():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B6)

    def lambda_5D0():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_68(54290, 1230, 126800, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    SetChrPos(0x101, 54960, 30, 125480, 0)
    SetChrPos(0x102, 53750, 30, 125480, 0)
    SetChrPos(0x104, 56190, 30, 125480, 0)
    SetChrPos(0x109, 54960, 30, 124330, 0)
    SetChrPos(0x103, 53750, 30, 124330, 0)
    SetChrPos(0x105, 56190, 30, 124330, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    SetMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x0, 0x0, 0x0)
    OP_65(0x1, 0x1)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x105, 0x0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0008
    ChrTalk(
        0x102,
        "#12P#00102Fふふ、久しぶりベル。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#5P#02904Fエリィ……\x01",
            "それに特務支援課の皆さんも\x01",
            "お久しぶりですわね。\x02\x03",

            "#02900Fティオさんも昨夜\x01",
            "お戻りになったようですが、\x01",
            "お変わりありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        "#12P#00200Fはい、おかげさまで。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#5P#02909Fうふふ、それはよかった。\x02\x03",

            "#02900F今日は本会議の日ですし\x01",
            "色々忙しいとは思いますが、\x01",
            "皆さんどうか頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x109,
        "#12P#10109Fふふっ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x105,
        (
            "#12P#10300Fそういえば、マリアベルさんは\x01",
            "今日はタワーの方に\x01",
            "顔を出さないのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#5P#02900Fええ、わたくしには\x01",
            "お父様の代理として\x01",
            "銀行の仕事もありますし……\x02\x03",

            "通商会議の仕切りはお父様に\x01",
            "全てお任せしていますわ。\x02\x03",

            "#02906Fそれと……皆さんにはお詫びして\x01",
            "おかなければいけませんわね。\x02\x03",

            "お忙しい中こんな事で\x01",
            "突然お呼び立てしてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#12P#00000Fいえ、そんな事は……\x01",
            "お世話になっている\x01",
            "マリアベルさんの依頼ですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00303Fなんでも、アンティークドールが\x01",
            "盗難にあったっつう話だが……\x02\x03",

            "#00301F詳しく話を聞かせてもらえるッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#5P#02903F……分かりましたわ。\x02\x03",

            "#02900Fわたくしがローゼンベルク製の\x01",
            "人形を愛してやまないことは、\x01",
            "皆さんもご存知かと思いますが……\x02\x03",

            "#02900FＩＢＣ内にある私室には、\x01",
            "特にお気に入りの５体の人形を\x01",
            "保管していましたの。\x02\x03",

            "#02903Fですが昨晩、所用で部屋を空けた隙に\x01",
            "何者かが侵入し、それら全てを\x01",
            "盗んでいってしまったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        (
            "#12P#00205Fローゼンベルク製の\x01",
            "アンティークドールを５体も……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x109,
        (
            "#12P#10105Fた、たしかそれって\x01",
            "相当高額だったはずですよね。\x02\x03",

            "#10106F大きいものになると\x01",
            "数百万ミラは下らないとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#5P#02903F金額は大した問題ではありませんわ。\x02\x03",

            "何よりも、あるべき場所に\x01",
            "大切なあの子たちがいない喪失感……\x02\x03",

            "#02910Fああっ、忌々しい賊をこの手で\x01",
            "八つ裂きにしてやりたいですわ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#12P#00006Fお、落ち着いてください。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#12P#00105Fベルの私室って……\x01",
            "ここの隣の部屋のことよね？\x02\x03",

            "#00103FＩＢＣのセキュリティを\x01",
            "掻い潜って侵入するなんて、\x01",
            "一体どうやって……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#5P#02903F……コホン。\x01",
            "ええ、わたくしも不思議に\x01",
            "思っていたのですが……\x02\x03",

            "#02901F現場に残されていた遺留品を見て、\x01",
            "すぐに合点が行きましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        "#12P#00205F遺留品……？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "#5P#02901Fそれに関しては\x01",
            "見てもらったほうが早いでしょう。\x01",
            "……これですわ。\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_123C")

    #A0026
    AnonymousTalk(
        0x101,
        "#00011Fこ、これは……！\x02",
    )

    CloseMessageWindow()

    #A0027
    AnonymousTalk(
        0x102,
        "#00105F『怪盗Ｂ』の犯行カード……！？\x02",
    )

    CloseMessageWindow()

    #A0028
    AnonymousTalk(
        0x8,
        (
            "#02901F大陸各地で数々の美術品を\x01",
            "盗み出した神出鬼没の怪人にして\x01",
            "稀代の盗人──人呼んで『怪盗Ｂ』。\x02\x03",

            "#02903F数々の摩訶不思議な奇術を操り\x01",
            "鮮やかに獲物を盗み出すと言われ、\x01",
            "犯行現場には必ずカードが残される……\x02\x03",

            "#02901F彼ならばおそらく、ＩＢＣへの潜入も\x01",
            "お手の物だったでしょう。\x02\x03",

            "#02902Fそれに皆さんは、彼の事件を\x01",
            "扱ったことがあったそうですわね？\x02",
        )
    )

    CloseMessageWindow()

    #A0029
    AnonymousTalk(
        0x109,
        "#10105Fそ、そうだったんですか！？\x02",
    )

    CloseMessageWindow()

    #A0030
    AnonymousTalk(
        0x103,
        (
            "#00200F確か以前、今の市民会館にあった\x01",
            "彫像が盗まれたんでしたよね。\x02\x03",

            "#00203F結局逮捕はできませんでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #A0031
    AnonymousTalk(
        0x104,
        (
            "#00310Fちっ、またクロスベルに\x01",
            "現れやがったとはな。\x02",
        )
    )

    CloseMessageWindow()

    #A0032
    AnonymousTalk(
        0x105,
        (
            "#10304Fフフ、君たちも色々な事件に\x01",
            "巻き込まれてるみたいだね。\x02\x03",

            "#10305Fそれで……カードには何て\x01",
            "書かれてたんだい？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FF")

    label("loc_123C")


    #A0033
    AnonymousTalk(
        0x101,
        "#00011Fこれは……！\x02",
    )

    CloseMessageWindow()

    #A0034
    AnonymousTalk(
        0x102,
        (
            "#00101Fもしかして……\x01",
            "『怪盗Ｂ』の犯行カード……！？\x02",
        )
    )

    CloseMessageWindow()

    #A0035
    AnonymousTalk(
        0x109,
        (
            "#10105F怪盗Ｂ……？\x01",
            "どこかで聞いたような。\x02",
        )
    )

    CloseMessageWindow()

    #A0036
    AnonymousTalk(
        0x8,
        (
            "#02900Fエリィとロイドさんは\x01",
            "ご存知のようですわね。\x02\x03",

            "#02901F大陸各地で数々の美術品を\x01",
            "盗み出した神出鬼没の怪人にして\x01",
            "稀代の盗人──人呼んで『怪盗Ｂ』。\x02\x03",

            "#02903F数々の摩訶不思議な奇術を操り\x01",
            "鮮やかに獲物を盗み出すと言われ、\x01",
            "犯行現場には必ずカードが残される……\x02\x03",

            "#02901F活動の中心となっている帝国では\x01",
            "彼の名を知らぬ者はいませんわ。\x02\x03",

            "#02906F彼ならばおそらく、ＩＢＣへの潜入も\x01",
            "お手の物だったでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #A0037
    AnonymousTalk(
        0x103,
        (
            "#00200Fわたしも名前くらいは\x01",
            "耳にしたことがありますね。\x02",
        )
    )

    CloseMessageWindow()

    #A0038
    AnonymousTalk(
        0x104,
        (
            "#00301Fちっ、そいつがクロスベルに\x01",
            "現れやがったとはな。\x02",
        )
    )

    CloseMessageWindow()

    #A0039
    AnonymousTalk(
        0x105,
        (
            "#10305Fそれで……\x01",
            "カードには何て書かれてたんだい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14FF")


    #A0040
    AnonymousTalk(
        0x8,
        "#02903F……内容はこうですわ。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特務支援課の若者たちよ。\x01",
            "令嬢の寵愛受けし五人の童女は\x01",
            "わが手中にあり。\x02\x03",

            "彼女らの自由を望むならば\x01",
            "閉じ込めし五つの檻を\x01",
            "真実の鍵にて開け放つがよい。\x02\x03",

            "第一の檻は市中に。\x01",
            "『搦め手の指揮官が\x01",
            "  座する椅子』を探せ。\x01",
            "  　　　　　　　　──怪盗Ｂ\x07\x00\x02",
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

    #C0042
    ChrTalk(
        0x8,
        (
            "#5P#02901F……お分かり頂けましたわね？\x01",
            "わたくしが皆さんを\x01",
            "お呼び立てした最大の理由が。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#12P#00001F怪盗Ｂが俺たち特務支援課に\x01",
            "挑戦状を叩きつけている……\x02\x03",

            "つまりはそういうことですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x105,
        (
            "#12P#10306Fそのために\x01",
            "わざわざ５体もの人形を\x01",
            "盗み出したってわけかい？\x02\x03",

            "#10302Fフフ、相当な変人なのは\x01",
            "間違いなさそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        (
            "#00301Fともかく……\x01",
            "現実に被害が出てんだし、\x01",
            "見過ごすわけにもいかねえだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#12P#00103Fそうね……盗まれたのは\x01",
            "ベルの大事にしている\x01",
            "ローゼンベルクドールなんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#5P#02902Fふふ、ありがとうエリィ。\x01",
            "どうかよろしくお願いしますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#12P#00000Fそれじゃあ、調査を始める前に\x01",
            "改めてカードの文章について\x01",
            "検証してみよう。\x02\x03",

            "#00003Fまず『五人の童女』という言葉……\x02\x03",

            "これは盗まれた５体の人形のことを\x01",
            "指しているんだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        (
            "#12P#00203Fとなると、『五つの檻』は……\x02\x03",

            "#00200Fおそらく、それらの人形が\x01",
            "計５ヶ所に隠されている事を\x01",
            "示しているんでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x109,
        (
            "#12P#10105Fということは、\x01",
            "計５ヶ所もの場所を探さなきゃ\x01",
            "いけないわけですか……\x02\x03",

            "#10106Fうう、大変そうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x105,
        (
            "#12P#10302Fそして、おそらく重要なのは\x01",
            "『市中』と『搦め手の指揮官が\x01",
            "座する椅子』という言葉だ。\x02\x03",

            "#10304Fおそらくは隠し場所の\x01",
            "ヒントなんだろうけど……\x01",
            "ふむ、なにかの例えなのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#00303F『搦め手』……\x01",
            "最近、なんだかそういう言葉を\x01",
            "聞いたような気がするが……\x02\x03",

            "#00300Fとにかく、悩んでいても始まらねえか。\x01",
            "早速調査を始めるとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#5P#02904Fうふふ、期待していますわ、\x01",
            "特務支援課の皆さん。\x02\x03",

            "#02900Fわたくしの大切なあの子たちを、\x01",
            "どうか取り戻してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        "#12P#00000Fええ、お任せ下さい。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        (
            "#12P#00104Fひとまずカードの内容については\x01",
            "捜査手帳にメモをしておいたわ。\x02\x03",

            "#00100Fこれを手がかりに調査を始めましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【消えたコレクションの捜索】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 54990, 30, 124960, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x7A, 0x1, 0x1)
    SetScenarioFlags(0x1C6, 3)
    EventEnd(0x5)
    Return()

    # Function_6_3DF end

    def Function_7_1D53(): pass

    label("Function_7_1D53")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(54970, 1230, 123580, 0)
    MoveCamera(46, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    SetChrPos(0x101, 54960, 30, 123480, 0)
    SetChrPos(0x102, 53750, 30, 123480, 0)
    SetChrPos(0x104, 56190, 30, 123480, 0)
    SetChrPos(0x109, 54960, 30, 122330, 0)
    SetChrPos(0x103, 53750, 30, 122330, 0)
    SetChrPos(0x105, 56190, 30, 122330, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    SetChrChipByIndex(0x8, 0x1E)
    ClearChrBattleFlags(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 54960, 30, 125480, 180)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0057
    ChrTalk(
        0x8,
        (
            "#02903F──事情は概ね分かりましたわ。\x02\x03",

            "#02901F怪盗Ｂが《結社》の一味というのは\x01",
            "たしかに驚きましたけど……\x02\x03",

            "#02906Fそういうことなら仕方ありませんわね。\x02\x03",

            "#02910F捕まえた暁には、生きている事を\x01",
            "後悔するほどのお仕置きをして\x01",
            "差し上げる予定でしたのに。\x02",
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

    #C0058
    ChrTalk(
        0x104,
        "#00306F（お、恐ろしいことを言うなあ……）\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#12P#00006Fす、すみません、\x01",
            "俺たちも逮捕したい所でしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#12P#00100Fひとまず、回収した人形たちを\x01",
            "ベルに返させてもらうわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(500)
    SetChrName("")

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "５体のローゼンベルク人形のトランクを\x01",
            "マリアベルに渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x7D0, 0x0)

    #C0062
    ChrTalk(
        0x8,
        (
            "#02909Fうふふ、お帰りなさい。\x01",
            "アリス、カナン、リエーテ、\x01",
            "ミステル、シャロン……\x02\x03",

            "#02904F……まあいいでしょう。\x01",
            "この際文句は言いませんわ。\x02\x03",

            "#02900Fこうしてわたくしのかわいい\x01",
            "ローゼンベルク人形たちが\x01",
            "無傷で戻ってきたことですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        (
            "#10304Fまあ、その点は怪盗Ｂも\x01",
            "徹底していたみたいだしね。\x02\x03",

            "#10300Fそんな頑丈なトランクに入れて、\x01",
            "野ざらしにするような場所には\x01",
            "置いてなかったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        "#12P#10105Fああ、そういえばそうだったね。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#12P#00206Fまあ、そもそも盗まなければ\x01",
            "いいだけの話なのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#12P#00009Fはは、確かにそうだな。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#02903Fとにかく、今後は\x01",
            "このような事がないように\x01",
            "セキュリティを徹底強化しますわ。\x02\x03",

            "#02900F保安部にも今まで以上に\x01",
            "しっかり働いてもらわないと。\x02\x03",

            "#02909Fフフ、皆さんには本当に\x01",
            "お世話になってしまいましたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#12P#00109Fふふ、気にしないでベル。\x01",
            "困ったときはお互いさまだし。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2897")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0069
    ChrTalk(
        0x101,
        "#12P#00005F（そうだ、前回の時は確か……）\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 54960, 30, 124080, 2000, 0x0)

    #C0070
    ChrTalk(
        0x101,
        "#12P#00001F（まじっ……）\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x109,
        "#12P#10105Fロ、ロイドさん？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "#02905F……何のおつもりですか？\x01",
            "突然ジロジロと。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#12P#00003Fい、いえ。\x02\x03",

            "#00001F以前、事件を解決した時は\x01",
            "怪盗Ｂが依頼者の姿に変装して\x01",
            "現れたということがあったので……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#00305Fああ、そういや\x01",
            "そんなこともあったっけなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        "#12P#00205Fいや、でも今回は……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#12P#00003F……その、単刀直入に聞きます。\x02\x03",

            "#00001Fあなたは、マリアベルさんですよね──\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)

    def lambda_263C():
        OP_99(0xFE, 0x101, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_263C)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2669():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2669)

    def lambda_2682():
        OP_98(0xFE, 0x0, 0xC8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2682)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    #C0077
    ChrTalk(
        0x101,
        "#12P#00011Fぐふっ……！？\x02",
    )

    CloseMessageWindow()
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

    #C0078
    ChrTalk(
        0x8,
        (
            "#02902Fうふふ、ロイドさんったら。\x02\x03",

            "#02909F人がせっかく素直に\x01",
            "感謝しているというのに、\x01",
            "さすがに失礼じゃありませんこと？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0079
    ChrTalk(
        0x101,
        (
            "#12P#00011Fす、すみませっ……ぐうっ……！\x02\x03",

            "#00006F（た、確かにこれは間違いなく\x01",
            "  マリアベルさん、だ……ガクッ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        "#12P#00106Fもう、ロイドったら……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        "#10309Fやれやれ、締まらないねえ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29DE")

    label("loc_2897")


    #C0082
    ChrTalk(
        0x101,
        (
            "#12P#00000Fそれじゃあ、俺たちは\x01",
            "そろそろ失礼しますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "#02909Fふふ、今日は本当に\x01",
            "ありがとうございました。\x02\x03",

            "#02900Fあなたたちも、\x01",
            "今日の通商会議に警備として\x01",
            "参加されるそうですわね。\x02\x03",

            "#02904Fせいぜい、お父様を陰ながら\x01",
            "助けてあげてくださいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#12P#00000Fええ、お任せください。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#12P#00100Fそれじゃあね、ベル。\x02",
    )

    CloseMessageWindow()

    label("loc_29DE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_29F5")
    Call(0, 8)

    label("loc_29F5")


    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちは\x01",
            "１Ｆの受付で発行されていた\x01",
            "ＩＢＣ認証カードを返却するのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【消えたコレクションの捜索】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7A, 0x1, 0x6)
    OP_29(0x7A, 0x1, 0x7)
    OP_29(0x7A, 0x4, 0x10)
    SubItemNumber(0x324, 1)
    SubItemNumber(0x335, 1)
    SubItemNumber(0x336, 1)
    SubItemNumber(0x337, 1)
    SubItemNumber(0x338, 1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("c1310", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1D53 end

    def Function_8_2AF8(): pass

    label("Function_8_2AF8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    OP_68(54590, 1500, 13640, 0)
    MoveCamera(55, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20420, 0)
    SetChrPos(0x101, 53930, 0, 14020, 90)
    SetChrPos(0x102, 53440, 0, 15190, 90)
    SetChrPos(0x104, 53440, 0, 12670, 90)
    SetChrPos(0x109, 52520, 0, 13810, 90)
    SetChrPos(0x103, 52020, 0, 15160, 90)
    SetChrPos(0x105, 52020, 0, 12580, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0xA, 0x1, 0x8)
    Sleep(1000)

    def lambda_2BC3():
        OP_95(0xFE, 56930, 0, 14020, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BC3)

    def lambda_2BDD():
        OP_95(0xFE, 56440, 0, 15190, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BDD)

    def lambda_2BF7():
        OP_95(0xFE, 56440, 0, 12670, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BF7)

    def lambda_2C11():
        OP_95(0xFE, 55520, 0, 13810, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C11)

    def lambda_2C2B():
        OP_95(0xFE, 55020, 0, 15160, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C2B)

    def lambda_2C45():
        OP_95(0xFE, 55020, 0, 12580, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2C45)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x105, 0x1)
    LoadChrToIndex("apl/ch51274.itc", 0x1F)
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(55700, 1400, 130699, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x8, 56030, 0, 130930, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    Sound(802, 0, 100, 0)
    Sleep(500)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x1, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0088
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02904Fもしもし。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    Sleep(500)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("声")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──やあ、麗しのマリアベル嬢。\x01",
            "ご機嫌はいかがかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0090
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02912F上々と言った所ですわ。\x02\x03",

            "#02913F貴方の“余興”とやらも、\x01",
            "十分に楽しめましたし。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("声")

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、それは良かった。\x02\x03",

            "大切なコレクションを\x01",
            "貸して頂いて感謝している。\x02\x03",

            "マイスターとは面識もあるが、\x01",
            "あれだけの数の作品を\x01",
            "一度に見る機会はそう無くてね。\x02\x03",

            "まさに美の至極──\x01",
            "改めて礼を言わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0092
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02909Fうふふ……丁重に扱って\x01",
            "いただけたようですし、\x01",
            "その点は安心しましたわ。\x02\x03",

            "#02911F傷の一つでも付いていたら、\x01",
            "それこそわたくしの“お城”に\x01",
            "招待させていただく所でしたけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("声")

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハハハ……\x01",
            "それはそれで残念だったかな。\x02\x03",

            "まあ、手早く回収してくれた\x01",
            "支援課の諸君には感謝しておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0094
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02913Fフフ……\x01",
            "それで貴方はこれから\x01",
            "どうされるつもりですの？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("声")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、クロスベルは\x01",
            "すぐにでも発つつもりだよ。\x02\x03",

            "帝国方面が面白いことに\x01",
            "なっているようなのでね。\x01",
            "そちらに行かせてもらうつもりだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0096
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02912Fそうでしたわね……\x01",
            "それではお疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("声")

    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そちらの《計画》については、\x01",
            "私も帝国から見守らせて\x01",
            "もらうとしよう。\x02\x03",

            "フフ、《結社》における\x01",
            "貴女の今後についてもね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0098
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02902Fうふふ……まだどうするか\x01",
            "決めたわけではありませんけど。\x02\x03",

            "#02913Fそれでは、また近い内に\x01",
            "お会いしましょう──\x02",

            "#02911F《怪盗紳士》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("怪盗ブルブラン")

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハハ、その時を\x01",
            "楽しみにさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Return()

    # Function_8_2AF8 end

    SaveToFile()

Try(main)
