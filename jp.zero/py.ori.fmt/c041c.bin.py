from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c041c.bin",                # FileName
        "c041c",                    # MapName
        "c041c",                    # Location
        0x0023,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 1, 0, 2],
    )

    BuildStringList((
        "c041c",                  # 0
        "イリア",                 # 1
        "リーシャ",               # 2
        "支配人バルサモ",         # 3
        "受付ローランド",         # 4
        "ユージーン",             # 5
        "テオドール",             # 6
        "プリエ",                 # 7
        "セリーヌ",               # 8
        "カレリア",               # 9
        "アバン劇団長",           # 10
        "客",                     # 11
        "客",                     # 12
        "客",                     # 13
        "客",                     # 14
        "客",                     # 15
    ))

    AddCharChip((
        "chr/ch05100.itc",                   # 00
        "chr/ch05200.itc",                   # 01
        "chr/ch21900.itc",                   # 02
        "chr/ch25800.itc",                   # 03
        "chr/ch25900.itc",                   # 04
        "chr/ch28700.itc",                   # 05
        "chr/ch28800.itc",                   # 06
        "chr/ch36900.itc",                   # 07
        "chr/ch37000.itc",                   # 08
        "chr/ch27500.itc",                   # 09
    ))

    DeclNpc(-91550,  0,       1679,    180,  405,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-90209,  0,       1070,    225,  389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-2250,   2500,    15000,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(6969,    0,       3480,    270,  261,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-91199,  0,       -870,    0,    405,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-121580, 0,       1669,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-121709, 0,       3109,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-91300,  0,       4960,    90,   389,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-121709, 0,       3109,    90,   277,  0x0, 0,   2,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-3240,   0,       4179,    180,  389,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 25,  9.0,                   14.0,                  2.5,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -4.5,                  -2.799999713897705,    -0.4999999701976776,   1.0])

    DeclActor(6500,    0,       3480,    1200,    6970,    1500,    3480,    0x007E, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_34C",          # 00, 0
        "Function_1_404",          # 01, 1
        "Function_2_4EE",          # 02, 2
        "Function_3_511",          # 03, 3
        "Function_4_9C2",          # 04, 4
        "Function_5_9C6",          # 05, 5
        "Function_6_CCB",          # 06, 6
        "Function_7_D7F",          # 07, 7
        "Function_8_10EF",         # 08, 8
        "Function_9_133D",         # 09, 9
        "Function_10_1475",        # 0A, 10
        "Function_11_1598",        # 0B, 11
        "Function_12_1636",        # 0C, 12
        "Function_13_16D4",        # 0D, 13
        "Function_14_180E",        # 0E, 14
        "Function_15_1A72",        # 0F, 15
        "Function_16_1CE0",        # 10, 16
        "Function_17_1F57",        # 11, 17
        "Function_18_2144",        # 12, 18
        "Function_19_23C1",        # 13, 19
        "Function_20_25AE",        # 14, 20
        "Function_21_31E4",        # 15, 21
        "Function_22_322A",        # 16, 22
        "Function_23_3270",        # 17, 23
        "Function_24_329C",        # 18, 24
        "Function_25_3320",        # 19, 25
    ))


    def Function_0_34C(): pass

    label("Function_0_34C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_38C"),
        (1, "loc_398"),
        (2, "loc_3A4"),
        (3, "loc_3B0"),
        (4, "loc_3BC"),
        (5, "loc_3C8"),
        (6, "loc_3D4"),
        (SWITCH_DEFAULT, "loc_3E0"),
    )


    label("loc_38C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_398")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_403")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_403")

    Return()

    # Function_0_34C end

    def Function_1_404(): pass

    label("Function_1_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41A")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_430")
    Event(0, 19)
    Jump("loc_4A7")

    label("loc_430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_43E")
    Jump("loc_4A7")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_454")
    Event(0, 18)
    Jump("loc_4A7")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46A")
    Event(0, 17)
    Jump("loc_4A7")

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_49A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_495")
    SetChrPos(0xA, -3460, 0, 2440, 0)
    ClearChrFlags(0x11, 0x80)

    label("loc_495")

    Jump("loc_4A7")

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7")
    Event(0, 16)

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4ED")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, -90300, 0, 4960, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 4)), scpexpr(EXPR_END)), "loc_4ED")
    SetChrFlags(0x9, 0x10)

    label("loc_4ED")

    Return()

    # Function_1_404 end

    def Function_2_4EE(): pass

    label("Function_2_4EE")

    OP_1B(0x3, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_510")
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x3, 0x0, 0x18)

    label("loc_510")

    Return()

    # Function_2_4EE end

    def Function_3_511(): pass

    label("Function_3_511")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_669")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_59B")

    #C0001
    ChrTalk(
        0xA,
        (
            "どうやら劇場内には\x01",
            "いらっしゃらないようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xA,
        (
            "もし見かけたらすぐに\x01",
            "警察の方に連絡いたしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_664")

    label("loc_59B")


    #C0003
    ChrTalk(
        0xA,
        (
            "ロイド様、話はお聞きしましたよ。\x01",
            "男の子を捜してらっしゃるとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xA,
        (
            "どうやら劇場内には\x01",
            "いらっしゃらないようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xA,
        (
            "ご安心ください。\x01",
            "もし見かけたらすぐに\x01",
            "警察の方に連絡いたしましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_664")

    Jump("loc_9BE")

    label("loc_669")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_840")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_773")

    #C0006
    ChrTalk(
        0xFE,
        (
            "ストーカーと思われたのは\x01",
            "歳若い少女だったとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "ともかく、イリアさんの要請で\x01",
            "受け入れ手続きを進めている所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "なに、イリアさんが仰るのなら\x01",
            "入団したって構わないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "あのリーシャさんも\x01",
            "そうだったのですから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_83B")

    label("loc_773")


    #C0010
    ChrTalk(
        0xFE,
        (
            "リーシャさんは元々\x01",
            "イリアさんが引っ張ってきたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "劇団長も最初は\x01",
            "首を捻っていたんですが、\x01",
            "実際素晴らしい才能の持ち主で。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "イリアさんの目に間違いはありません。\x01",
            "むしろ大歓迎ですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83B")

    Jump("loc_9BE")

    label("loc_840")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_927")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F1")

    #C0013
    ChrTalk(
        0xFE,
        "お話はお聞きになりましたか……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "そうなのです、イリアさんに\x01",
            "今度はストーカーが……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "ふう、どうか皆様、\x01",
            "お力添えを願えないでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_922")

    label("loc_8F1")


    #C0016
    ChrTalk(
        0xFE,
        (
            "どうか皆様、\x01",
            "お力添えを願えないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_922")

    Jump("loc_9BE")

    label("loc_927")


    #C0017
    ChrTalk(
        0xA,
        (
            "おや……これは皆様。\x01",
            "ようこそいらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "イリアさんに御用でしょうか？\x01",
            "劇団長やリーシャさんと一緒に\x01",
            "ホールの方にいらっしゃいますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BE")

    TalkEnd(0xFE)
    Return()

    # Function_3_511 end

    def Function_4_9C2(): pass

    label("Function_4_9C2")

    Call(0, 5)
    Return()

    # Function_4_9C2 end

    def Function_5_9C6(): pass

    label("Function_5_9C6")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_AF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A52")

    #C0019
    ChrTalk(
        0xB,
        (
            "お探しの男の子は\x01",
            "劇場内にはいないようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xB,
        (
            "また夜の公演が始まりましたら\x01",
            "自分も気を付けておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF1")

    label("loc_A52")


    #C0021
    ChrTalk(
        0xB,
        (
            "受付を通られるお客様は\x01",
            "一通り見ているつもりなんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        (
            "お子様は全員保護者の方が\x01",
            "付いておられたと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xB,
        "お力になれず申し訳ありません。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_AF1")

    Jump("loc_CC7")

    label("loc_AF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B9B")

    #C0024
    ChrTalk(
        0xB,
        (
            "はあ、何だか\x01",
            "よく分かりませんが……\x01",
            "新しい団員さんが増えるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xB,
        (
            "イリアさんの目に適うなんて\x01",
            "よほどの天才なのでしょう。\x01",
            "楽しみですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC7")

    label("loc_B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C27")

    #C0026
    ChrTalk(
        0xB,
        (
            "そういえば、昨晩の公演の後\x01",
            "イリアさんとリーシャさん、劇団長で\x01",
            "話しこんでいましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        "何の話だったんでしょうかね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC7")

    label("loc_C27")


    #C0028
    ChrTalk(
        0xB,
        (
            "本日は劇団アルカンシェルは\x01",
            "休演日となっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xB,
        (
            "ですが……\x01",
            "イリアさんとリーシャさんは\x01",
            "顔を出しておられますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        "２人とも熱心ですからねえ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_CC7")

    TalkEnd(0xB)
    Return()

    # Function_5_9C6 end

    def Function_6_CCB(): pass

    label("Function_6_CCB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D78")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0031
    ChrTalk(
        0x8,
        (
            "#1700Fリーシャも公演のテンポってものに\x01",
            "慣れてきたみたいね。\x02\x03",

            "#1709Fうんうん、いい感じだわ。\x01",
            "今日の残りも張り切って行くわよ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Jump("loc_D7B")

    label("loc_D78")

    Call(0, 7)

    label("loc_D7B")

    TalkEnd(0xFE)
    Return()

    # Function_6_CCB end

    def Function_7_D7F(): pass

    label("Function_7_D7F")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0032
    ChrTalk(
        0xC,
        (
            "ハハ、しかしリーシャも\x01",
            "ここまでやってくれるとはなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#1709Fそうね、今日の舞台は\x01",
            "今までで一番良かったし。\x02\x03",

            "#1702Fま、メンバー全員の演技が\x01",
            "こなれてきたのもあるだろうけど……\x02\x03",

            "リーシャも公演のテンポってものが\x01",
            "掴めて来たんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        (
            "#1809Fあはは……１日２舞台って\x01",
            "思っていた以上に大変ですけど……\x02\x03",

            "#1802Fでも、さっきの舞台は\x01",
            "とっても気持ちよかったです。\x01",
            "途中からスッと体が軽くなって……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#1709Fそうそう、それそれ。\x01",
            "その感覚を大事にしなさい！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_10DF")

    #C0036
    ChrTalk(
        0x160,
        (
            "#3305F（これがイリア・プラティエ……？\x01",
            "  ふーん、普通の気配しかしないけど。）\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#0012F（普通の気配って……）\x02\x03",

            "#0000F（イリアさんは《天才》だよ。\x01",
            "  ただし、舞台の上だけらしいけどね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x160,
        (
            "#3304F（クスクス……なるほど。\x01",
            "  それは面白い《天才》だわ。）\x02\x03",

            "#3302F（そっちの東方系のお姉さんも\x01",
            "  ちょっと面白そうだし……）\x02\x03",

            "（レンも一度、アルカンシェルの\x01",
            "  舞台を見てみようかしら。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10DF")

    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_7_D7F end

    def Function_8_10EF(): pass

    label("Function_8_10EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 4)), scpexpr(EXPR_END)), "loc_11B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_11A8")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0039
    ChrTalk(
        0x9,
        (
            "#1810F記念祭は明日が最終日ですよね。\x02\x03",

            "#1804F……さてと。\x01",
            "体調を整えて頑張らないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#0001F（さすがに疲れてるのかな……？）\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Jump("loc_11AB")

    label("loc_11A8")

    Call(0, 7)

    label("loc_11AB")

    Jump("loc_1339")

    label("loc_11B0")


    #C0041
    ChrTalk(
        0x9,
        (
            "#1805Fあ、ロイドさん。\x02\x03",

            "例の男の子、まだ\x01",
            "見つからないんですか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_END)), "loc_1273")

    #C0042
    ChrTalk(
        0x101,
        (
            "#0006Fああ、今の所は……\x02\x03",

            "#0000Fでも目撃情報も入ってるし、\x01",
            "じきに見つかると思う。\x01",
            "あまり心配しないでくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D2")

    label("loc_1273")


    #C0043
    ChrTalk(
        0x101,
        (
            "#0006Fああ、今の所は……\x02\x03",

            "#0000Fでも、まだ探し始めたばかりだし、\x01",
            "あまり心配しないでくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D2")


    #C0044
    ChrTalk(
        0x9,
        (
            "#1806F……はい。\x02\x03",

            "#1810Fすみません、\x01",
            "私も公演が無かったら\x01",
            "お手伝いするんですけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x0)
    SetChrFlags(0x9, 0x10)
    SetScenarioFlags(0xB2, 4)

    label("loc_1339")

    TalkEnd(0xFE)
    Return()

    # Function_8_10EF end

    def Function_9_133D(): pass

    label("Function_9_133D")

    TalkBegin(0xFE)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_139A")

    #C0045
    ChrTalk(
        0xC,
        (
            "共和国の渋茶って\x01",
            "なかなかイケルな。\x01",
            "疲れに効く気がするぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1465")

    label("loc_139A")


    #C0046
    ChrTalk(
        0xC,
        "ずず～っ……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xC,
        (
            "おっ、本当だ。\x01",
            "確かに疲れにきく気がするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        (
            "さすが東方出身者。\x01",
            "リーシャはいい物持ってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#1704Fうんうん、これはイケルわ。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        "#1809Fあはは、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1465")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_9_133D end

    def Function_10_1475(): pass

    label("Function_10_1475")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 6)), scpexpr(EXPR_END)), "loc_14D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_14C8")

    #C0051
    ChrTalk(
        0xD,
        (
            "………………………………\x01",
            "劇団は年功序列制だからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14CB")

    label("loc_14C8")

    Call(0, 12)

    label("loc_14CB")

    Jump("loc_1594")

    label("loc_14D0")


    #C0052
    ChrTalk(
        0xD,
        "……子供を捜しているらしいな。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xD,
        "俺も探そうか？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#0001Fあ、いえ……\x01",
            "すみません、お気持ちだけで。\x02\x03",

            "時間が掛かると思いますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xD,
        "……そうか。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xD,
        "その子、早く見つかるといいな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 6)

    label("loc_1594")

    TalkEnd(0xFE)
    Return()

    # Function_10_1475 end

    def Function_11_1598(): pass

    label("Function_11_1598")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 7)), scpexpr(EXPR_END)), "loc_15E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_15D9")

    #C0057
    ChrTalk(
        0xE,
        (
            "ぽりぽり……\x01",
            "甘い物は正義よね～㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15DC")

    label("loc_15D9")

    Call(0, 12)

    label("loc_15DC")

    Jump("loc_1632")

    label("loc_15E1")


    #C0058
    ChrTalk(
        0xE,
        (
            "あら、イリアが\x01",
            "言ってた男の子の話？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xE,
        (
            "見てないのよ、\x01",
            "ごめんなさいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 7)

    label("loc_1632")

    TalkEnd(0xFE)
    Return()

    # Function_11_1598 end

    def Function_12_1636(): pass

    label("Function_12_1636")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0xD, 0xE, 0)
    TurnDirection(0xE, 0xD, 0)

    #C0060
    ChrTalk(
        0xD,
        (
            "プリエさん、菓子食うのは\x01",
            "着替えてからの方が……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xE,
        (
            "……テオドール君、\x01",
            "キミちょっと生意気だぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xD,
        "……すみません。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_12_1636 end

    def Function_13_16D4(): pass

    label("Function_13_16D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_173C")

    #C0063
    ChrTalk(
        0xF,
        (
            "イリアさんに褒められるなんて……\x01",
            "う、嬉しいですわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xF,
        "…………………………㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_180A")

    label("loc_173C")


    #C0065
    ChrTalk(
        0xF,
        "……あの、聞いてくださいます？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xF,
        (
            "実は今日の演技、\x01",
            "イリアさんに褒めてもらえたのです！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xF)

    #C0067
    ChrTalk(
        0xF,
        (
            "イ、イリア様……\x01",
            "コホン、イリアさんに褒められるなんて\x01",
            "入団以来初めてですわ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_180A")

    TalkEnd(0xFE)
    Return()

    # Function_13_16D4 end

    def Function_14_180E(): pass

    label("Function_14_180E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_19C9")
    OP_4B(0x10, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_188B")

    #C0068
    ChrTalk(
        0x10,
        (
            "ともかく、夜の部は\x01",
            "こちらを使ってくださいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x10,
        "いつもの衣装は直しておきますから。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19BC")

    label("loc_188B")


    #C0070
    ChrTalk(
        0x10,
        (
            "さっさっさっ……\x01",
            "ええ、大分いいようですね。\x01",
            "丈も苦しくはありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xF,
        "はい、平気ですわ。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xF,
        (
            "それに元々\x01",
            "だぶっとした衣装ですもの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0073
    ChrTalk(
        0x10,
        (
            "そ、そうですね。\x01",
            "確かにだぶっと作ってしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xF,
        (
            "だ、だぶっとしてて\x01",
            "最高の衣装だと思いますわ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_19BC")

    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    Jump("loc_1A6E")

    label("loc_19C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1A1D")

    #C0075
    ChrTalk(
        0x10,
        (
            "休演日の間に\x01",
            "掃除をしておかなくちゃいけません。\x01",
            "まったくもう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6E")

    label("loc_1A1D")


    #C0076
    ChrTalk(
        0x10,
        (
            "あらプリエさんたら\x01",
            "またこんな所にお菓子を……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x10,
        "没収です、没収！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x0, 6)

    label("loc_1A6E")

    TalkEnd(0xFE)
    Return()

    # Function_14_180E end

    def Function_15_1A72(): pass

    label("Function_15_1A72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1CDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BFA")

    #C0078
    ChrTalk(
        0xFE,
        (
            "話は聞いたよ。\x01",
            "無事解決してくれたそうだね！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#0000Fええ、何とか……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x103,
        (
            "#0200F思わぬ方向へ\x01",
            "転がってしまいましたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "はは、そうなんだよな。\x01",
            "イリア君はいつも強引で……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "そうだ、リーシャ君を\x01",
            "劇団に入れる時だって……\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0305Fありゃ、回想モードに\x01",
            "入っちまったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x102,
        (
            "#0100F劇団長はイリアさんに\x01",
            "随分困らされてるみたいだものね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 2)
    Jump("loc_1CDC")

    label("loc_1BFA")


    #C0085
    ChrTalk(
        0xFE,
        (
            "と、ともかく、感謝するよ。\x01",
            "これで心配なく\x01",
            "公演も進められそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "君たちにはお礼をしなくてはな……\x01",
            "あとでもう一枚チケットを送ろうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#0309F超うれしいッス。\x01",
            "有り難く受け取らせてもらいます！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#0000Fははは……\x02",
    )

    CloseMessageWindow()

    label("loc_1CDC")

    TalkEnd(0xFE)
    Return()

    # Function_15_1A72 end

    def Function_16_1CE0(): pass

    label("Function_16_1CE0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xA, 0x80)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    SetChrPos(0xA, 0, 0, -1760, 180)
    FadeToBright(500, 0)
    OP_0D()

    #C0089
    ChrTalk(
        0xA,
        (
            "おや皆様、ようこそ\x01",
            "お越しくださいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xA,
        (
            "……プレ公演の一件、\x01",
            "本当にありがとうございました。\x01",
            "改めて御礼を言わせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#0012Fはは、その件はもう。\x02\x03",

            "#0000Fそれより、舞台の方は\x01",
            "ちょうど公演中みたいですね。\x01",
            "連日大好評みたいで何よりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xA,
        "はい、これも皆様のお陰です。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "そうそう……明日は\x01",
            "休演日となっておりますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        (
            "宜しければ\x01",
            "いらっしゃってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        (
            "#0100Fありがとう、また\x01",
            "お邪魔させてもらいますね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xB8, 7)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_1CE0 end

    def Function_17_1F57(): pass

    label("Function_17_1F57")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xA, 0x80)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    SetChrPos(0xA, 0, 0, -1760, 180)
    FadeToBright(500, 0)
    OP_0D()

    #C0096
    ChrTalk(
        0xA,
        (
            "これは皆様、ようこそ\x01",
            "お越しくださいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        (
            "ですが、申し訳ありません。\x01",
            "ただ今イリアさんやリーシャさんは……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#0000Fすみません、\x01",
            "皆さん準備中なんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#0300Fまあ用事があったわけじゃねえし、\x01",
            "また別の機会に訪ねてみるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        "#0100Fええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        "#0200Fどうもお邪魔しました。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xB9, 0)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_1F57 end

    def Function_18_2144(): pass

    label("Function_18_2144")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    LoadChrToIndex("chr/ch21800.itc", 0x1E)
    LoadChrToIndex("chr/ch21900.itc", 0x1F)
    LoadChrToIndex("chr/ch20800.itc", 0x20)
    LoadChrToIndex("chr/ch21200.itc", 0x21)
    LoadChrToIndex("chr/ch21300.itc", 0x22)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrChipByIndex(0x14, 0x20)
    SetChrChipByIndex(0x15, 0x21)
    SetChrChipByIndex(0x16, 0x22)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0x12, 3540, 0, -2890, 315)
    SetChrPos(0x13, 2540, 0, -1890, 135)
    SetChrPos(0x14, 5100, 0, 3030, 89)
    SetChrPos(0x15, -1210, 0, -1120, 225)
    SetChrPos(0x16, -2410, 0, -2320, 45)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0102
    ChrTalk(
        0x101,
        (
            "#0005Fあれ、賑わってるな。\x01",
            "公演はパレードの前に\x01",
            "終わったはずだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x102,
        (
            "#0100F公演の余熱が冷めないまま\x01",
            "残っている人が多かったみたいね。\x02\x03",

            "まだしばらくは\x01",
            "混雑するんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x103,
        (
            "#0200Fお邪魔するのは\x01",
            "やめておいた方が良さそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        "#0300Fやれやれ、そうすっか。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xB9, 1)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2144 end

    def Function_19_23C1(): pass

    label("Function_19_23C1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xA, 0x80)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    SetChrPos(0xA, 0, 0, -1760, 180)
    FadeToBright(500, 0)
    OP_0D()

    #C0106
    ChrTalk(
        0xA,
        (
            "これは皆様、ようこそ\x01",
            "お越しくださいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "ですが、申し訳ありません。\x01",
            "ただ今イリアさんやリーシャさんは……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#0000Fすみません、\x01",
            "皆さん準備中なんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        (
            "#0300Fまあ用事があったわけじゃねえし、\x01",
            "また別の機会に訪ねてみるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x102,
        "#0100Fええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        "#0200Fどうもお邪魔しました。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xB9, 2)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_23C1 end

    def Function_20_25AE(): pass

    label("Function_20_25AE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1100, -2000, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 0, 0, -7000, 0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, -5100, 0, 3000, 135)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, -6000, 0, 2400, 135)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10000000)
    MoveCamera(45, 21, 0, 3000)
    SetCameraDistance(19000, 3000)

    def lambda_2675():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2675)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(500)
    OP_6F(0x50)

    #C0112
    ChrTalk(
        0x101,
        (
            "#0005Fあれ、お客さんがいない……\x02\x03",

            "#0000Fそうか、午後のステージは\x01",
            "もう終わっているのか。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    #N0113
    NpcTalk(
        0x9,
        "娘の声",
        "#2P……ロイドさん？\x02",
    )

    CloseMessageWindow()

    #N0114
    NpcTalk(
        0x8,
        "女性の声",
        "#2Pあら、どうかしたの？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-860, 1100, -1110, 2500)
    MoveCamera(10, 21, 0, 2500)
    SetCameraDistance(18000, 2500)

    def lambda_27A9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27A9)

    def lambda_27B6():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27B6)
    Sleep(100)

    def lambda_27D3():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_27D3)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28A1")

    #C0115
    ChrTalk(
        0x101,
        "#12P#0005Fイリアさん、リーシャ。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "#5P#1702Fなになに？\x01",
            "あたしたちに会いに来たの？\x02\x03",

            "#1709F夜のステージまで時間があるから\x01",
            "一緒にお茶でも飲む？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC5")

    label("loc_28A1")


    #C0117
    ChrTalk(
        0x101,
        (
            "#12P#0005Fイリアさん、リーシャ。\x02\x03",

            "#0002Fお久しぶりです。\x01",
            "新作、大好評みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        (
            "#5P#1702Fフフン。\x01",
            "ま、当然だけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "#1809F#5Pロイドさんも初日に\x01",
            "見にきてくれたんですよね。\x02\x03",

            "#1802Fふふっ、ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#12P#0012Fいやあ……\x01",
            "セシル姉のオマケだから。\x02\x03",

            "#0002Fでも、ステージは本当に凄かった！\x02\x03",

            "#0009Fイリアさんはもちろんだけど\x01",
            "リーシャも改めて大ファンになったよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        "#1810F#5Pそ、そんな……恥ずかしいです。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "#1705F#5Pあらら、お安くないわねぇ。\x02\x03",

            "#1709F弟君がナンパしてたって\x01",
            "セシルに言いつけてやろうかな～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0123
    ChrTalk(
        0x101,
        (
            "#12P#0011Fいっ……\x01",
            "ナンパじゃないですってば！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0124
    ChrTalk(
        0x9,
        "#1801F#6Pも、もう、イリアさんったら。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "#5P#1702Fまあそれは置いといて……\x01",
            "なに、あたしたちに会いに来たの？\x02\x03",

            "夜のステージまで時間があるから\x01",
            "一緒にお茶でも飲む？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2BBD():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2BBD)

    label("loc_2BC5")


    #C0126
    ChrTalk(
        0x101,
        (
            "#12P#0008Fあ、いや……\x01",
            "仕事で立ち寄ったんです。\x02\x03",

            "#0001F実は……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "イリアたちに迷子の男の子を\x01",
            "捜している事情を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    #C0128
    ChrTalk(
        0x9,
        "#1801F#5Pそれは……心配ですね。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#5P#1706Fうーん、確かにここって\x01",
            "子供も楽しめる場所ではあるし……\x02\x03",

            "公演中に紛れ込んじゃった可能性は\x01",
            "あるかもしれないわね。\x02\x03",

            "#1702F──よし、ちょっと待ってなさい。\x02\x03",

            "休憩中のメンバーにも声を掛けて\x01",
            "入り込んでないか確かめてみるわ。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 21)
    Sleep(100)

    def lambda_2D7B():

        label("loc_2D7B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_2D7B")

    QueueWorkItem2(0x9, 2, lambda_2D7B)
    Sleep(500)

    #C0130
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあっ……\x02\x03",

            "#0006Fうーん、そこまでお願いする\x01",
            "つもりじゃ無かったんだけど……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x2)
    TurnDirection(0x9, 0x101, 500)

    #C0131
    ChrTalk(
        0x9,
        (
            "#1804F#5Pふふっ、イリアさんって\x01",
            "思い立ったら一直線ですから。\x02\x03",

            "#1802F私も見回って来ますから\x01",
            "ロイドさんはここで待っていてください。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 3)
    BeginChrThread(0x9, 3, 0, 22)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x9, 0x2)
    EndChrThread(0x9, 0x3)
    SetChrPos(0x8, -1100, 0, 600, 135)
    SetChrPos(0x9, -2000, 0, 0, 135)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrSubChip(0x9, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0132
    ChrTalk(
        0x8,
        (
            "#5P#1706Fうーん、とりあえず\x01",
            "劇場の中にはいないみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "#1806F#5Pすみません……\x01",
            "お力になれなくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#12P#0002Fいや、そんな……\x01",
            "こちらこそ、お手数かけました。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        "#5P#1702Fふふっ、そのくらいいいわよ。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "#1800F#5P一応、劇団長と支配人にも\x01",
            "男の子の事は伝えておきます。\x02\x03",

            "もし保護したら警察の方に\x01",
            "連絡すればいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#12P#0004Fああ、それが確実だと思う。\x02\x03",

            "#0002F──ありがとうございました。\x01",
            "夜の公演も頑張ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        "#5P#1709F弟君の方もね～♪\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        (
            "#1802F#5Pロイドさん。\x01",
            "またいらしてください。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_30F8():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30F8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31AF")
    StopBGM(0x7D0)
    WaitBGM()

    #A0140
    AnonymousTalk(
        0x101,
        (
            "#0003F（よし、歓楽街の聞き込みは\x01",
            "  これで十分だな。）\x02\x03",

            "#0001F（次は裏通りだ……\x01",
            "  同じように聞き込みを進めていこう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_31AF")

    SetScenarioFlags(0xA1, 7)
    OP_29(0x46, 0x1, 0x1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31D8")
    OP_29(0x46, 0x1, 0x2)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 3)

    label("loc_31D8")

    EventEnd(0x5)
    NewScene("c040C", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_20_25AE end

    def Function_21_31E4(): pass

    label("Function_21_31E4")

    OP_92(0xFE, 0xFFFFE69C, 0xBB8, 0x1F4)

    def lambda_31F6():
        OP_95(0xFE, -5500, 0, 5000, 3500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31F6)
    WaitChrThread(0xFE, 1)

    def lambda_3214():
        OP_95(0xFE, -10500, 0, 5000, 3500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3214)
    Return()

    # Function_21_31E4 end

    def Function_22_322A(): pass

    label("Function_22_322A")

    OP_92(0xFE, 0xFFFFE69C, 0xBB8, 0x1F4)

    def lambda_323C():
        OP_95(0xFE, -5500, 0, 5000, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_323C)
    WaitChrThread(0xFE, 1)

    def lambda_325A():
        OP_95(0xFE, -10500, 0, 5000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_325A)
    Return()

    # Function_22_322A end

    def Function_23_3270(): pass

    label("Function_23_3270")

    OP_92(0xFE, 0xFFFFE69C, 0xBB8, 0x1F4)

    def lambda_3282():
        OP_95(0xFE, -6500, 0, 5000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3282)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_3270 end

    def Function_24_329C(): pass

    label("Function_24_329C")

    EventBegin(0x1)
    Sleep(50)

    #C0141
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは２階の観客席みたいだな。\x02\x03",

            "あまりうろうろすると迷惑になるし、\x01",
            "立ち入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -8260, 2500, 14010, 90)
    EventEnd(0x4)
    Return()

    # Function_24_329C end

    def Function_25_3320(): pass

    label("Function_25_3320")

    EventBegin(0x1)
    Sleep(50)

    #C0142
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは２階の観客席みたいだな。\x02\x03",

            "あまりうろうろすると迷惑になるし、\x01",
            "立ち入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 5760, 2500, 13790, 270)
    EventEnd(0x4)
    Return()

    # Function_25_3320 end

    SaveToFile()

Try(main)
