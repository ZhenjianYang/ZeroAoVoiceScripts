from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t210d.bin",                # FileName
        "t210d",                    # MapName
        "t210d",                    # Location
        0x0059,                     # MapIndex
        "ed7151",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "t210d",                  # 0
        "ソーニャ司令",           # 1
        "兵士ブルード",           # 2
        "兵士ダリア",             # 3
        "観光客",                 # 4
    ))

    AddCharChip((
        "chr/ch12200.itc",                   # 00
        "chr/ch41400.itc",                   # 01
        "chr/ch41800.itc",                   # 02
        "chr/ch33000.itc",                   # 03
    ))

    DeclNpc(-10000,  10000,   0,       270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-13829,  10000,   -2960,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-14060,  10000,   2900,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-18600,  5000,    -17170,  270,  389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(1500,    5050,    -20000,  1200,    1500,    6050,    -20000,  0x007C, 0,  3,  0x0000)

    ChipFrameInfo(348, 0)                                        # 0

    ScpFunction((
        "Function_0_15C",          # 00, 0
        "Function_1_20C",          # 01, 1
        "Function_2_21B",          # 02, 2
        "Function_3_25C",          # 03, 3
        "Function_4_3AD",          # 04, 4
        "Function_5_593",          # 05, 5
        "Function_6_732",          # 06, 6
        "Function_7_862",          # 07, 7
        "Function_8_9C3",          # 08, 8
    ))


    def Function_0_15C(): pass

    label("Function_0_15C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_194"),
        (1, "loc_1A0"),
        (2, "loc_1AC"),
        (3, "loc_1B8"),
        (4, "loc_1C4"),
        (5, "loc_1D0"),
        (6, "loc_1DC"),
        (SWITCH_DEFAULT, "loc_1E8"),
    )


    label("loc_194")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_1F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F4")

    label("loc_20B")

    Return()

    # Function_0_15C end

    def Function_1_20C(): pass

    label("Function_1_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21A")
    ClearChrFlags(0xB, 0x80)

    label("loc_21A")

    Return()

    # Function_1_20C end

    def Function_2_21B(): pass

    label("Function_2_21B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_22D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_244")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_244")

    label("loc_244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257")
    OP_70(0x2, 0x0)
    Jump("loc_25B")

    label("loc_257")

    OP_70(0x2, 0x1E)

    label("loc_25B")

    Return()

    # Function_2_21B end

    def Function_3_25C(): pass

    label("Function_3_25C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F4, 1)"), scpexpr(EXPR_END)), "loc_2E5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_357")

    label("loc_2E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_357")

    Jump("loc_3A1")

    label("loc_35C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_3A1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_25C end

    def Function_4_3AD(): pass

    label("Function_4_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB")
    Call(0, 8)
    Return()

    label("loc_3BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_509")

    #C0004
    ChrTalk(
        0x8,
        (
            "#10600F今後の対応については、\x01",
            "ダグラス副司令がマクダエル議長に\x01",
            "相談しに行っているわ。\x02\x03",

            "私は正規軍の司令官として、\x01",
            "帝国・共和国方面への警戒態勢を\x01",
            "万全にしておかなくてはならない。\x02\x03",

            "#10603F全てが終わった後、どうするかは\x01",
            "まだ分からないけれど……\x02\x03",

            "#10600F今はとにかく、司令官として\x01",
            "出来る限りのことをするのみよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_58F")

    label("loc_509")


    #C0005
    ChrTalk(
        0x8,
        (
            "#10603F全てが終わった後、どうするかは\x01",
            "まだ分からないけれど……\x02\x03",

            "#10600F今はとにかく、司令官として\x01",
            "出来る限りのことをするのみよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58F")

    TalkEnd(0xFE)
    Return()

    # Function_4_3AD end

    def Function_5_593(): pass

    label("Function_5_593")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694")

    #C0006
    ChrTalk(
        0x9,
        (
            "なんでも帝国では、内戦の最中\x01",
            "『飛行軍艦』のようなものが\x01",
            "開発されているらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            "そんなものが帝国軍の\x01",
            "機甲師団に加わったら、\x01",
            "正直手がつけられない……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "あの《神機》があれば……\x01",
            "そう考えてしまうのは\x01",
            "僕だけなんだろうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_72E")

    label("loc_694")


    #C0009
    ChrTalk(
        0x9,
        (
            "『飛行軍艦』なんかが\x01",
            "機甲師団に加わったら、\x01",
            "帝国軍は手がつけられなくなる。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "あの《神機》があれば……\x01",
            "そう考えてしまうのは\x01",
            "僕だけなんだろうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72E")

    TalkEnd(0xFE)
    Return()

    # Function_5_593 end

    def Function_6_732(): pass

    label("Function_6_732")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D6")

    #C0011
    ChrTalk(
        0xA,
        (
            "私は、《神機》が失われて\x01",
            "良かったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "あれほどの力をもった兵器を、\x01",
            "私たちなんかがが扱っていいとは\x01",
            "どうしても思えませんから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_85E")

    label("loc_7D6")


    #C0013
    ChrTalk(
        0xA,
        (
            "《神機》……あんなものが、\x01",
            "私たちの手に負えたとは思えません。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xA,
        (
            "……ガレリア要塞の有様を見ると、\x01",
            "今でも背筋が凍ってしまいます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85E")

    TalkEnd(0xFE)
    Return()

    # Function_6_732 end

    def Function_7_862(): pass

    label("Function_7_862")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93F")

    #C0015
    ChrTalk(
        0xB,
        (
            "なんとか帝国に帰ろうと思って\x01",
            "ベルガード門にきたのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "ま、まさか《ガレリア要塞》が\x01",
            "あんなことになっていたとは……！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        (
            "こ、これじゃあどうあっても\x01",
            "帰るなんて無理じゃないか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9BF")

    label("loc_93F")


    #C0018
    ChrTalk(
        0xB,
        (
            "ま、まさか《ガレリア要塞》が\x01",
            "あんなことになっていたとは……！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "こ、これじゃあどうあっても\x01",
            "帰るなんて無理じゃないか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BF")

    TalkEnd(0xFE)
    Return()

    # Function_7_862 end

    def Function_8_9C3(): pass

    label("Function_8_9C3")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-6780, 12170, -1160, 0)
    MoveCamera(303, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12280, 0)
    SetChrPos(0x101, -8000, 10000, 500, 270)
    SetChrPos(0x102, -7900, 10000, -500, 270)
    SetChrPos(0x103, -7000, 10000, 1400, 270)
    SetChrPos(0x104, -6800, 10000, -1500, 270)
    SetChrPos(0xF4, -6000, 10000, 500, 270)
    SetChrPos(0xF5, -5800, 10000, -500, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    #C0020
    ChrTalk(
        0x101,
        (
            "#12P#00002Fソーニャ司令……\x01",
            "こんな所にいたんですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    #C0021
    ChrTalk(
        0x8,
        "#10605F#5Pあなたたち……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-68290, 12670, -3030, 0)
    MoveCamera(239, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(127990, 0)
    OP_0D()
    MoveCamera(303, 17, 0, 40000)
    Sleep(1000)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0022
    AnonymousTalk(
        0x104,
        (
            "#00301F……すげえ有様ッスね。\x02\x03",

            "#00303Fあの白い人形が列車砲を\x01",
            "跡形もなく消しちまったのは\x01",
            "映像で見ていたが……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #A0023
    AnonymousTalk(
        0x101,
        (
            "#00008F……間接的にだけど、\x01",
            "キーアの力でこんなことに\x01",
            "なってしまったんだよな……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #A0024
    AnonymousTalk(
        0x8,
        (
            "#10603F……これは、帝国側から\x01",
            "入ってきた不確定な\x01",
            "情報なのだけれど……\x02\x03",

            "#10600Fあの《神機》の攻撃では、\x01",
            "帝国軍に人的被害は\x01",
            "ほとんどなかったそうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #A0025
    AnonymousTalk(
        0x101,
        "#12P#00005Fほ、本当ですか！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #A0026
    AnonymousTalk(
        0x102,
        (
            "#12P#00105Fあ、あの状況じゃ奇跡としか\x01",
            "言いようがないですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #A0027
    AnonymousTalk(
        0x8,
        (
            "#10600F事実確認のしようはないから\x01",
            "実際の所は分からないけど……\x02\x03",

            "#10604F人間を巻き込まずに\x01",
            "無機物だけを消し去るという\x01",
            "力だったのかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #A0028
    AnonymousTalk(
        0x103,
        (
            "#12P#00202Fそれが本当だとすると、\x01",
            "キーアが無意識に《奇蹟》に\x01",
            "干渉したのかもしれません。\x02\x03",

            "#00204F帝国が甚大な被害を受けたのは\x01",
            "間違いないでしょうが……\x01",
            "少しだけホッとしました。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-6780, 12170, -1160, 0)
    MoveCamera(303, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12280, 0)
    OP_0D()

    #C0029
    ChrTalk(
        0x8,
        (
            "#10604F#5P……あなたたち、話は聞いたわ。\x02\x03",

            "#10602Fクロスベル市の解放作戦、\x01",
            "上手くいったようでなによりね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        "#12P#00309Fハハ、正直出来すぎッスけどね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FC8")

    #C0031
    ChrTalk(
        0x109,
        (
            "#12P#10104Fソーニャ司令のおかげです！\x02\x03",

            "#10102Fあの助言があったからこそ、\x01",
            "独立の無効宣言という道を\x01",
            "見出すことができましたし！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FB")

    label("loc_FC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1065")

    #C0032
    ChrTalk(
        0x105,
        (
            "#12P#10400Fフフ、それも司令のおかげかな。\x02\x03",

            "#10404Fあの助言があったからこそ、\x01",
            "独立の無効宣言という道を\x01",
            "見出すことができたわけだし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FB")

    label("loc_1065")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10FB")

    #C0033
    ChrTalk(
        0x106,
        (
            "#12P#10704F貴女のおかげだと思います。\x02\x03",

            "#10702Fあの助言があったからこそ、\x01",
            "独立の無効宣言という道を\x01",
            "見出すことができたわけですし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FB")


    #C0034
    ChrTalk(
        0x8,
        (
            "#10602F#5Pふふ、私は何もしていないわ。\x01",
            "すべてはあなた達の成した事……\x02\x03",

            "#10603F……私のしたことと言えば、\x01",
            "大統領の方針に流されるまま\x01",
            "国防軍を運用したというだけ。\x02\x03",

            "#10608F独立国の正当性が挫かれた今、\x01",
            "私という人間に司令官としての\x01",
            "資格はないのかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x101,
        "#12P#00011Fそ、それって……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12EC")

    #C0036
    ChrTalk(
        0x10A,
        (
            "#12P#00606F……そこまで思い込むことは\x01",
            "ないかと思いますが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138F")

    label("loc_12EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1341")

    #C0037
    ChrTalk(
        0x105,
        (
            "#12P#10406F……そこまで思い込む事は\x01",
            "ないんじゃないのかい？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138F")

    label("loc_1341")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_138F")

    #C0038
    ChrTalk(
        0x109,
        (
            "#12P#10113Fそ、そこまで思い込むことは\x01",
            "ないんじゃ……！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138F")


    #C0039
    ChrTalk(
        0x8,
        (
            "#10602F#5Pふふ、もちろん今やるべき事は\x01",
            "分かっているつもりよ。\x02\x03",

            "#10604F全てが終わった後、どうするかは\x01",
            "まだ分からないけれど……\x02\x03",

            "#10600F今はとにかく、司令官として\x01",
            "出来る限りのことをするのみよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1AC, 0)
    EventEnd(0x5)
    Return()

    # Function_8_9C3 end

    SaveToFile()

Try(main)
