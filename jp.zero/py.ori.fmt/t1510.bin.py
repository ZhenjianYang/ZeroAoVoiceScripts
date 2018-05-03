from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1510.bin",                # FileName
        "t1510",                    # MapName
        "t1510",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1510",                  # 0
        "キルシュ寮長",           # 1
        "研修医フローラ",         # 2
        "研修医リットン",         # 3
        "セシル",                 # 4
        "遊撃士リン",             # 5
        "遊撃士エオリア",         # 6
        "観光客テュイエ",         # 7
        "観光客パステル",         # 8
    ))

    AddCharChip((
        "chr/ch24300.itc",                   # 00
        "chr/ch29502.itc",                   # 01
        "chr/ch29402.itc",                   # 02
        "chr/ch32002.itc",                   # 03
        "chr/ch32102.itc",                   # 04
        "chr/ch34302.itc",                   # 05
        "chr/ch23900.itc",                   # 06
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

    DeclNpc(-4809,   0,       11600,   225,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-12069,  150,     14399,   180,  341,  0x0, 0,   1,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-12069,  150,     11050,   0,    469,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-12479,  150,     6900,    180,  469,  0x0, 0,   3,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-12319,  150,     3630,    0,    469,  0x0, 0,   4,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-12479,  150,     6900,    180,  469,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(4690,    3750,    15430,   0,    385,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)

    DeclEvent(0x0000, 0, 17,  9.0,                   11.0,                  3.25,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -3.0,                  -5.5,                  -0.6500000357627869,   1.0])

    DeclActor(-6100,   0,       10440,   1000,    -4810,   1500,    11600,   0x007E, 0,  3,  0x0000)
    DeclActor(4390,    3750,    16900,   1000,    4390,    5000,    16900,   0x007C, 0,  11, 0x0000)
    DeclActor(5830,    0,       11730,   1200,    5830,    1500,    11730,   0x007C, 0,  18, 0x0000)

    ScpFunction((
        "Function_0_304",          # 00, 0
        "Function_1_3BC",          # 01, 1
        "Function_2_42C",          # 02, 2
        "Function_3_4D1",          # 03, 3
        "Function_4_4D5",          # 04, 4
        "Function_5_1721",         # 05, 5
        "Function_6_1853",         # 06, 6
        "Function_7_2B01",         # 07, 7
        "Function_8_2C5F",         # 08, 8
        "Function_9_2D5D",         # 09, 9
        "Function_10_3067",        # 0A, 10
        "Function_11_3685",        # 0B, 11
        "Function_12_36E5",        # 0C, 12
        "Function_13_38ED",        # 0D, 13
        "Function_14_39E6",        # 0E, 14
        "Function_15_4C1B",        # 0F, 15
        "Function_16_591C",        # 10, 16
        "Function_17_5EE4",        # 11, 17
        "Function_18_5F85",        # 12, 18
    ))


    def Function_0_304(): pass

    label("Function_0_304")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_344"),
        (1, "loc_350"),
        (2, "loc_35C"),
        (3, "loc_368"),
        (4, "loc_374"),
        (5, "loc_380"),
        (6, "loc_38C"),
        (SWITCH_DEFAULT, "loc_398"),
    )


    label("loc_344")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_350")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_35C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_368")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_374")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_380")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_38C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_398")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3BB")

    Return()

    # Function_0_304 end

    def Function_1_3BC(): pass

    label("Function_1_3BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3CA")
    Jump("loc_3D8")

    label("loc_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3D8")
    ClearChrFlags(0xA, 0x80)

    label("loc_3D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F0")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_404")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 14)
    Jump("loc_413")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_413")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 15)

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42B")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)

    label("loc_42B")

    Return()

    # Function_1_3BC end

    def Function_2_42C(): pass

    label("Function_2_42C")

    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x2, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_481")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49D")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_4D0")

    label("loc_49D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B9")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_4D0")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D0")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_4D0")

    Return()

    # Function_2_42C end

    def Function_3_4D1(): pass

    label("Function_3_4D1")

    Call(0, 4)
    Return()

    # Function_3_4D1 end

    def Function_4_4D5(): pass

    label("Function_4_4D5")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_171D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "休憩をする\x01",        # 2
            "やめる\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_555")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_555")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_585")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_574")
    OP_AF(0x5D)
    Jump("loc_576")

    label("loc_574")

    OP_AF(0x5C)

    label("loc_576")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1718")

    label("loc_585")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A5")
    OP_AF(0x5A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1718")

    label("loc_5A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B9")
    Jump("loc_1718")

    label("loc_5B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1718")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_635")

    #C0001
    ChrTalk(
        0x8,
        "あいよ、いらっしゃい！\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "病院もついさっき、今日の業務が\x01",
            "始まったばかりだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1718")

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_7E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76E")

    #C0003
    ChrTalk(
        0x8,
        (
            "そろそろ看護師の子が\x01",
            "病院食をとりにくる頃だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "最近の食事はなかなか\x01",
            "入院患者さんたちに好評なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "以前ゲバル議員さんに\x01",
            "『もっと豪華にしろ』だのワガママを\x01",
            "言われたときは腹が立ったもんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "アレのおかげでメニューを\x01",
            "工夫するようになったんだから\x01",
            "結果オーライさね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7E2")

    label("loc_76E")


    #C0007
    ChrTalk(
        0x8,
        (
            "最近の食事はなかなか\x01",
            "入院患者さんたちに好評なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "ゲバルさんがワガママ言ってくれた\x01",
            "おかげとも言えるね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E2")

    Jump("loc_1718")

    label("loc_7E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_878")

    #C0009
    ChrTalk(
        0x8,
        (
            "今朝運び込まれた患者は\x01",
            "なんでも撃たれた傷があったそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "やぁねぇ……\x01",
            "病院まで危ないことに\x01",
            "巻き込まれなけりゃいいけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1718")

    label("loc_878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_902")

    #C0011
    ChrTalk(
        0x8,
        (
            "あの遊撃士さんは病院関係の仕事を\x01",
            "よく手伝ってくれてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "いつもお世話になってるし、\x01",
            "今日は私がご馳走しようかねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1718")

    label("loc_902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_97E")

    #C0013
    ChrTalk(
        0x8,
        (
            "ん、さっき一緒にいた女の子は\x01",
            "どうしたんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "……なに、はぐれたのかい！？\x01",
            "はぁ、なにやってんだい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1718")

    label("loc_97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAA")

    #C0015
    ChrTalk(
        0x8,
        (
            "ふーん、話が聞こえてきたけど……\x01",
            "あんたがセシルさんの弟さんの\x01",
            "娘なんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x153,
        "#1105Fえ、キーアはやっぱりそーなんだ？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#0011Fち、違っ……！\x01",
            "だからそれは誤解ですってば！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "あはは、からかってみただけだよ。\x01",
            "本気にしない、しない。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x153,
        "#1111Fふーん？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0005Fはぁ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_AFA")

    #C0021
    ChrTalk(
        0x102,
        (
            "#0102F（ふふ、からかいやすい体質だとは\x01",
            "思っていたけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA2")

    label("loc_AFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B50")

    #C0022
    ChrTalk(
        0x103,
        (
            "#0202F（ロイドさんは、\x01",
            "いわゆるいじられキャラという\x01",
            "ヤツですね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA2")

    label("loc_B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_BA2")

    #C0023
    ChrTalk(
        0x104,
        (
            "#0309F（はっはっは、愛#2Rう#い奴だぜ。\x01",
            "ロイドはこうでなくちゃな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA2")

    SetScenarioFlags(0x0, 0)
    Jump("loc_C0F")

    label("loc_BAA")


    #C0024
    ChrTalk(
        0x8,
        "あはは、からかって悪かったよ。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "まぁ、お詫びといっちゃなんだが\x01",
            "好きにくつろいでいっとくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0F")

    Jump("loc_1718")

    label("loc_C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_C71")

    #C0026
    ChrTalk(
        0x8,
        "おやいらっしゃい。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "記念祭もやってるだろうに\x01",
            "こんな所によく来たねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1718")

    label("loc_C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2A")

    #C0028
    ChrTalk(
        0x8,
        (
            "食堂や病院食の食材は\x01",
            "ハロルドさんっていう商人さんから\x01",
            "買い付けてるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "新鮮で体に良い食材を\x01",
            "あんなに安く譲ってくれるところは\x01",
            "他にないからねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D6B")

    label("loc_D2A")


    #C0030
    ChrTalk(
        0x8,
        (
            "病院で出す料理の食材は\x01",
            "ハロルドさんから買い付けてるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6B")

    Jump("loc_1718")

    label("loc_D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E32")

    #C0031
    ChrTalk(
        0x8,
        (
            "寮で働いているマローネは\x01",
            "私の姪っ子でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "家事手伝いで暇そうにしてたのを\x01",
            "拾ってやったのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "あのコ、綺麗好きなだけが\x01",
            "取り柄だから、掃除するのは\x01",
            "かなり向いてるのよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1718")

    label("loc_E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_FC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F29")

    #C0034
    ChrTalk(
        0x8,
        (
            "せっかくの記念祭なのに\x01",
            "入院してベッドの上なんて\x01",
            "気の毒だろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "だから記念祭中くらいは\x01",
            "病院食を豪華にしてあげようと\x01",
            "思ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "かといって、\x01",
            "あまり偏った食事は出せないからね。\x01",
            "アイデアで勝負しないと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FBB")

    label("loc_F29")


    #C0037
    ChrTalk(
        0x8,
        (
            "記念祭中くらいは\x01",
            "病院食を豪華にしてあげようと\x01",
            "思ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "昨日からメニューに入れた\x01",
            "豆腐で作ったハンバーグ……\x01",
            "ヘルシーでいいだろう？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBB")

    Jump("loc_1718")

    label("loc_FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_10ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1070")

    #C0039
    ChrTalk(
        0x8,
        (
            "ここの研修医さんは\x01",
            "食事の時間も勉強してるほど\x01",
            "みんな熱心なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "うんうん、若いうちは勉強しなきゃね。\x01",
            "それが楽しい将来に繋がるってもんさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10E8")

    label("loc_1070")


    #C0041
    ChrTalk(
        0x8,
        (
            "どれ、勉強熱心な研修医さんの為に\x01",
            "アタマの良くなる特別メニューでも\x01",
            "考えてみるかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        "魚の目玉なんてどうかねぇ？\x02",
    )

    CloseMessageWindow()

    label("loc_10E8")

    Jump("loc_1718")

    label("loc_10ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_117C")

    #C0043
    ChrTalk(
        0x8,
        (
            "食堂に来るお客さんが\x01",
            "アルカンシェルの話をしてたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "新しい演目……\x01",
            "『金の太陽、銀の月』だっけ？\x01",
            "ぜひ見てみたいわ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1718")

    label("loc_117C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1330")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1198")
    Call(0, 5)
    Jump("loc_132B")

    label("loc_1198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_127D")

    #C0045
    ChrTalk(
        0x8,
        (
            "入院患者の食事も\x01",
            "あたしが作ってるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "昨日、個室に入院してるゲバルさんが\x01",
            "『ステーキを出せ』なんて\x01",
            "寝言を言い出してね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "つい、んなもん食いたきゃ\x01",
            "レストランにでも行けって\x01",
            "突っぱねちまったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_132B")

    label("loc_127D")


    #C0048
    ChrTalk(
        0x8,
        (
            "昨日、個室に入院してるゲバルさんが\x01",
            "『ステーキを出せ』なんて\x01",
            "寝言を言い出してね。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "こっちも栄養バランスに気をつけて\x01",
            "作ってるんだから\x01",
            "ああいう手合いには困っちまうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_132B")

    Jump("loc_1718")

    label("loc_1330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1403")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134C")
    Call(0, 5)
    Jump("loc_13FE")

    label("loc_134C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D1")

    #C0050
    ChrTalk(
        0x8,
        (
            "昼休みも終わって、\x01",
            "寮の中もようやく静かになったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "あとであたしも\x01",
            "マローネを手伝って\x01",
            "掃除するとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FE")

    label("loc_13D1")


    #C0052
    ChrTalk(
        0x8,
        (
            "あ……注文があるなら\x01",
            "遠慮なく言いなよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FE")

    Jump("loc_1718")

    label("loc_1403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_15EF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141F")
    Call(0, 5)
    Jump("loc_15EA")

    label("loc_141F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_158C")

    #C0053
    ChrTalk(
        0x8,
        (
            "おやセシルさん、\x01",
            "まだ休憩時間は残ってるだろう？\x01",
            "もう戻るのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "ただでさえ看護師は忙しいんだ。\x01",
            "休める時に休んどかないとだめだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x136,
        (
            "#1302Fふふ、大丈夫ですよ。\x01",
            "ロイドに会えたおかげで\x01",
            "疲れなんて吹っ飛んじゃいました。\x02\x03",

            "#1300F寮長、場所を借りさせてもらって\x01",
            "ありがとうございますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "はは、いいってことよ。\x01",
            "あんたはうちの寮生だしね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15EA")

    label("loc_158C")


    #C0057
    ChrTalk(
        0x8,
        (
            "あんたたち、セシルさんを\x01",
            "あんまり連れまわしちゃダメよ。\x01",
            "これで結構忙しい子なんだからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15EA")

    Jump("loc_1718")

    label("loc_15EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1718")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160B")
    Call(0, 5)
    Jump("loc_1718")

    label("loc_160B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169D")

    #C0058
    ChrTalk(
        0x8,
        (
            "ほいほい、いらっしゃい。\x01",
            "ここは病院職員たちの寮だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "夜勤疲れで寝てる先生もいるから\x01",
            "無理に起こしたりしないようにね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1718")

    label("loc_169D")


    #C0060
    ChrTalk(
        0x8,
        (
            "宿泊スペースと食堂は\x01",
            "外来用に設けてあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "何か食いたきゃ言っとくれ。\x01",
            "ウデによりをかけて\x01",
            "作らせてもらうからさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1718")

    Jump("loc_4E2")

    label("loc_171D")

    TalkEnd(0x8)
    Return()

    # Function_4_4D5 end

    def Function_5_1721(): pass

    label("Function_5_1721")


    #C0062
    ChrTalk(
        0x8,
        (
            "この病院では食事の栄養バランスも\x01",
            "しっかりと考えられていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "とくにあたしが得意なのは\x01",
            "手作りのビーフシチューさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "作り方を教えるから、\x01",
            "よかったらあんたたちも\x01",
            "試してごらん。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x5)
    Return()

    # Function_5_1721 end

    def Function_6_1853(): pass

    label("Function_6_1853")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18E7")
    Jump("loc_1931")

    label("loc_18E7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1907")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1931")

    label("loc_1907")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1927")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1931")

    label("loc_1927")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1931")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19DD")

    #C0067
    ChrTalk(
        0xFE,
        "あっ……その本！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "本が無事見つかったみたいで\x01",
            "なによりだわ。\x01",
            "面倒かけてごめんなさいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A66")

    label("loc_19DD")


    #C0069
    ChrTalk(
        0xFE,
        (
            "しかしまぁ、あの膨大な\x01",
            "本棚から見つけ出すなんて\x01",
            "なかなか大変だったでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "よく見つけられたわよねー。\x01",
            "人海戦術ってヤツかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A66")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_1A73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B90")

    #C0071
    ChrTalk(
        0xFE,
        (
            "私、よく研究棟の資料室にある\x01",
            "医学書を持ち出して、\x01",
            "ここで勉強しているんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "資料室の本棚に本を戻した時に\x01",
            "一緒に図書館の本も\x01",
            "本棚に入れちゃったみたいなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "申し訳ないけど、\x01",
            "病棟屋上にある研究棟の資料室を\x01",
            "探してみてもらえるかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_1B90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BB1")
    Call(0, 16)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C45")

    #C0074
    ChrTalk(
        0xFE,
        (
            "さーてと……\x01",
            "そろそろ勉強始めますか。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "お昼ご飯には……まだ早いわね。\x01",
            "ま、本を読んでたら\x01",
            "すぐ時間もたつでしょ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C80")

    label("loc_1C45")


    #C0076
    ChrTalk(
        0xFE,
        (
            "この食堂は私にとって\x01",
            "すっごく勉強しやすい空間なのよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C80")

    Jump("loc_2AF9")

    label("loc_1C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1D15")

    #C0077
    ChrTalk(
        0xFE,
        (
            "ん、今日の授業もバッチリ理解。\x01",
            "肌身離さず医学書を持ち歩いてる成果ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "同級生のリットンは\x01",
            "授業についていけてんのかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF9")

    label("loc_1D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1D9F")

    #C0079
    ChrTalk(
        0xFE,
        (
            "今度の筆記試験の予習してるの。\x01",
            "邪魔しないでくれる？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "まだ試験日はずっと先だけど\x01",
            "予習するに越したことはないからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF9")

    label("loc_1D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1E12")

    #C0081
    ChrTalk(
        0xFE,
        "はー、やっぱり外科はおもしろいわ。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "未知の技術がいっぱいだから\x01",
            "すっごくわくわくするのよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF9")

    label("loc_1E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1E8B")

    #C0083
    ChrTalk(
        0xFE,
        (
            "へ、小さい女の子？\x01",
            "見てないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "食堂に入ってきてたら\x01",
            "多分気づくし、\x01",
            "ここには居ないんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF9")

    label("loc_1E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_20E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A5")
    SetChrSubChip(0xFE, 0x0)

    #C0085
    ChrTalk(
        0xFE,
        "…………………………♪\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x153,
        (
            "#1110Fあ、なんだか難しそうな本を\x01",
            "よんでるねー？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0005Fなになに、死体解剖学……\x02\x03",

            "#0011Fって、キーアにはまだ早い！！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x153,
        "#1106Fえー？　つまんないの。\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FF1")
    Jump("loc_203B")

    label("loc_1FF1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2011")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_203B")

    label("loc_2011")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2031")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_203B")

    label("loc_2031")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_203B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0089
    ChrTalk(
        0xFE,
        (
            "……っていうか……\x01",
            "あなたたちうるさいんですけど……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x0, 1)
    Jump("loc_20E3")

    label("loc_20A5")


    #C0090
    ChrTalk(
        0xFE,
        (
            "まったく……\x01",
            "こっちは勉強してんだから\x01",
            "邪魔しないでよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E3")

    Jump("loc_2AF9")

    label("loc_20E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2142")

    #C0091
    ChrTalk(
        0xFE,
        (
            "私はいつも本で勉強してるから\x01",
            "こういう実地研修は\x01",
            "大事にしてかないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF9")

    label("loc_2142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_21C8")

    #C0092
    ChrTalk(
        0xFE,
        (
            "あ……そういや明日は、\x01",
            "教授会で教授たちがいないんだっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "うーん、質問があるから\x01",
            "早めに聞きにいかないとなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF9")

    label("loc_21C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_227B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E3")
    Call(0, 8)
    Jump("loc_2276")

    label("loc_21E3")


    #C0094
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "いちいちご飯時なんて気にしてたら\x01",
            "何も食べられなくなるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "手術に参加するようになったら\x01",
            "こんな光景は日常茶飯事なんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2276")

    Jump("loc_2AF9")

    label("loc_227B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_23A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2338")

    #C0096
    ChrTalk(
        0xFE,
        (
            "……創立記念祭？\x01",
            "うーん……特に興味ないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "私、これでも勉強しに\x01",
            "クロスベルに来たのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "他の人みたいに、\x01",
            "休みがないからって\x01",
            "嘆いたりはしないわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23A4")

    label("loc_2338")


    #C0099
    ChrTalk(
        0xFE,
        (
            "そもそも“クロスベルの”\x01",
            "創立記念祭でしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "レミフェリア出身の私には\x01",
            "あんまり関係ないと思うわ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A4")

    Jump("loc_2AF9")

    label("loc_23A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2454")

    #C0101
    ChrTalk(
        0xFE,
        (
            "外科の講義の時間がまだだから\x01",
            "ご飯を食べながら勉強してるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "……お行儀悪いってよく言われるけど、\x01",
            "ご飯食べてる時間って\x01",
            "何だかもったいないのよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF9")

    label("loc_2454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_260C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2585")

    #C0103
    ChrTalk(
        0xFE,
        (
            "私、結構この生物の解剖本を\x01",
            "持ち歩いてるんだけど……\x01",
            "これって変？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "リットンとご飯たべてたら、\x01",
            "『メシ時にそんなの読むな』って\x01",
            "怒られちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x103,
        (
            "#0203F……お肉とか食べてる時に\x01",
            "その本の図説が見えたら\x01",
            "食欲がなくなりそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "うーん、私は全然平気なんだけどなー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2607")

    label("loc_2585")


    #C0107
    ChrTalk(
        0xFE,
        (
            "生物の解剖本を持ち歩いてるのって\x01",
            "やっぱ変なのかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "私的にはどこでも勉強できて\x01",
            "便利でいいなぁーと思ってるんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2607")

    Jump("loc_2AF9")

    label("loc_260C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_266B")

    #C0109
    ChrTalk(
        0xFE,
        "あー、もうこんな時間かぁ。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "研究棟の資料室で\x01",
            "予習でもしてようかしらね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF9")

    label("loc_266B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_27FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2763")

    #C0111
    ChrTalk(
        0xFE,
        (
            "リットンは、わたしと同じ\x01",
            "レミフェリアの出なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "あいつ、学力は並だったけど\x01",
            "この病院に入るために\x01",
            "死に物狂いで勉強したのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "けど、やっぱどっか抜けてるのよね。\x01",
            "魔獣に襲われたのに\x01",
            "緊迫感がないっていうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27F8")

    label("loc_2763")


    #C0114
    ChrTalk(
        0xFE,
        (
            "リットンってば抜けてるわよね。\x01",
            "魔獣に襲われたのに\x01",
            "緊迫感がないっていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "ま、悪運が強くてよかったってとこね。\x01",
            "空の女神に感謝しなきゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F8")

    Jump("loc_2AF9")

    label("loc_27FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2935")

    #C0116
    ChrTalk(
        0xFE,
        (
            "ここ、居心地いいから\x01",
            "つい居座っちゃうんですよね。\x01",
            "勉強もはかどるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x136,
        (
            "#1302Fフローラさんは\x01",
            "本を読むのがホント好きよね。\x01",
            "熱心でいいことだわ。\x02\x03",

            "#1304Fでも、熱中しすぎて\x01",
            "講義に遅れたりしないように\x01",
            "気をつけるのよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "……時々お母さんみたいなこと\x01",
            "言いますよね、セシルさんって。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_297E")

    label("loc_2935")


    #C0119
    ChrTalk(
        0xFE,
        (
            "そういえば、もうすぐ講義の時間だし……\x01",
            "そろそろ研究棟に戻ろうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_297E")

    Jump("loc_2AF9")

    label("loc_2983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2AF9")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AC0")

    #C0120
    ChrTalk(
        0xFE,
        "ふんふん、ここがこうなって……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "……なーるほど！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#0005F（食事をとりながら\x01",
            "  本を読んでるみたいだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        (
            "#0105F（生物学の本みたいね。\x01",
            "  解剖写真の図説つきの……）\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        "#0306F（グ、グロい……）\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x103,
        (
            "#0203F（……少なくとも\x01",
            "  ご飯時に読むものでは\x01",
            "  なさそうですね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AF9")

    label("loc_2AC0")


    #C0126
    ChrTalk(
        0xFE,
        (
            "ご飯の時間も勉強勉強！\x01",
            "いや～、外科って面白いわ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AF9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_1853 end

    def Function_7_2B01(): pass

    label("Function_7_2B01")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B95")
    Jump("loc_2BDF")

    label("loc_2B95")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BB5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BDF")

    label("loc_2BB5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BD5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BDF")

    label("loc_2BD5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BDF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C16")
    Call(0, 8)
    Jump("loc_2C57")

    label("loc_2C16")


    #C0127
    ChrTalk(
        0xFE,
        (
            "はぁ……よくもまぁ食事中に\x01",
            "あんなものを読む気分になれるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C57")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_2B01 end

    def Function_8_2C5F(): pass

    label("Function_8_2C5F")

    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)

    #C0128
    ChrTalk(
        0xA,
        (
            "なぁフローラ、\x01",
            "さっきの講義の要点って……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "……ってうわっ！？\x01",
            "食事中にそんなもの読むなよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "ご飯を食べてる時間に\x01",
            "勉強しないのは勿体無いでしょうが。\x01",
            "もぐもぐ……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        (
            "それにしたって、\x01",
            "なにも解剖図なんて見ながら……\x01",
            "……おえっぷ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_8_2C5F end

    def Function_9_2D5D(): pass

    label("Function_9_2D5D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DF1")
    Jump("loc_2E3B")

    label("loc_2DF1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E11")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E3B")

    label("loc_2E11")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E31")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E3B")

    label("loc_2E31")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E3B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2ECA")

    #C0132
    ChrTalk(
        0xFE,
        "いいプレゼントは作れたか？\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "あとで私もエオリアと一緒に\x01",
            "見舞いに行ってみるかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_305F")

    label("loc_2ECA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2FE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F90")

    #C0134
    ChrTalk(
        0xFE,
        (
            "えっ……\x01",
            "シズクちゃんのプレゼントの\x01",
            "材料集めをしているって？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "そうか、うーん……\x01",
            "何か手伝えればよかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "生憎、役に立ちそうなものは\x01",
            "持ってないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 4)
    Jump("loc_2FDD")

    label("loc_2F90")


    #C0137
    ChrTalk(
        0xFE,
        (
            "生憎、よさそうなものは\x01",
            "持ってないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        "すまないな、役に立てなくて。\x02",
    )

    CloseMessageWindow()

    label("loc_2FDD")

    Jump("loc_305F")

    label("loc_2FE2")


    #C0139
    ChrTalk(
        0xFE,
        (
            "急患があってね、\x01",
            "エオリアと一緒にこちらまで\x01",
            "運んできたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "やれやれ、記念祭が終わっても\x01",
            "忙しいのは変わらないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_305F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_2D5D end

    def Function_10_3067(): pass

    label("Function_10_3067")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30FB")
    Jump("loc_3145")

    label("loc_30FB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_311B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3145")

    label("loc_311B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_313B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3145")

    label("loc_313B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3145")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3213")

    #C0141
    ChrTalk(
        0xFE,
        (
            "シズクちゃん、ずっとこの病院に\x01",
            "入院してるのよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "……よーし、アリオスさんのよしみで\x01",
            "久しぶりにスリスリさせてもらおう㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xC,
        "……やめとけ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_367D")

    label("loc_3213")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3565")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C8")

    #C0144
    ChrTalk(
        0xFE,
        (
            "え、プレゼントの材料になりそうなものを\x01",
            "シズクちゃんが探してる？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "うーん……そうねぇ。\x01",
            "何かあったかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0146
    ChrTalk(
        0xFE,
        (
            "……そうだ！\x01",
            "こんなのがあったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0147
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エオリアは蒼耀石の結晶を取り出した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0148
    ChrTalk(
        0xFE,
        (
            "どうこれ！\x01",
            "ちょっと前に帝国の交易商さんに\x01",
            "仕事の報酬としてもらったものなんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "これなら絶対シズクちゃんも\x01",
            "喜んでくれるでしょう！\x01",
            "……はい、持っていってちょうだい㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#0011Fさ、さすがにこんなのもらえません！\x02\x03",

            "シズクちゃんも困ると思いますし……！\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x103,
        (
            "#0203Fというか、材料集めという\x01",
            "趣旨が変わってしまっているかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "うー、そう？\x01",
            "でも他によさそうなものもないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "あーあ、シズクちゃんの力に\x01",
            "なりたかったなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 5)
    Jump("loc_3560")

    label("loc_34C8")


    #C0154
    ChrTalk(
        0xFE,
        (
            "あーあ、シズクちゃんの力に\x01",
            "なりたかったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "あ、そうだ。\x01",
            "だったらこっちの金耀石の……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        "#0006Fだ、だからそんなのもらえませんってば……！\x02",
    )

    CloseMessageWindow()

    label("loc_3560")

    Jump("loc_367D")

    label("loc_3565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361C")

    #C0157
    ChrTalk(
        0xFE,
        (
            "さっき運び込んだ患者さん、\x01",
            "街道で魔獣に襲われたらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "どうも、前よりも魔獣が\x01",
            "強くなっているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "なんとか一命をとりとめたのは\x01",
            "よかったけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_367D")

    label("loc_361C")


    #C0160
    ChrTalk(
        0xFE,
        "実は、私も手術を手伝ったのよ。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "こういうとき医師の免許を持っていて\x01",
            "よかったって思うわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_3067 end

    def Function_11_3685(): pass

    label("Function_11_3685")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "３階：女性職員寮→\x01\x01",
            "←２階：男性職員寮\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_3685 end

    def Function_12_36E5(): pass

    label("Function_12_36E5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3779")
    Jump("loc_37C3")

    label("loc_3779")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3799")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37C3")

    label("loc_3799")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37B9")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37C3")

    label("loc_37B9")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37C3")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385A")

    #C0163
    ChrTalk(
        0xE,
        "もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xE,
        (
            "うーん、あっさりしてて\x01",
            "物足りないかと思ったけど……\x01",
            "なかなかいけるわー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38E5")

    label("loc_385A")


    #C0165
    ChrTalk(
        0xE,
        (
            "ウムム……病院のご飯も\x01",
            "なかなかバカにできないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xE,
        (
            "あたしが普段食べてる\x01",
            "ジャンクフードみたいなのより\x01",
            "１００倍は美味しいかも……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E5")

    SetChrSubChip(0xE, 0x0)
    TalkEnd(0xE)
    Return()

    # Function_12_36E5 end

    def Function_13_38ED(): pass

    label("Function_13_38ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3970")

    #C0167
    ChrTalk(
        0xFE,
        (
            "こっちは看護師さんや\x01",
            "お医者さんたちのお部屋なんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "みんなで暮らすのって、\x01",
            "楽しそうでいいなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_39E2")

    label("loc_3970")


    #C0169
    ChrTalk(
        0xFE,
        (
            "こっちは看護師さんや\x01",
            "お医者さんたちのお部屋なんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "知らない人同士で暮らすのって\x01",
            "きっと楽しいよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39E2")

    TalkEnd(0xFE)
    Return()

    # Function_13_38ED end

    def Function_14_39E6(): pass

    label("Function_14_39E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch05302.itc", 0x22)
    LoadChrToIndex("chr/ch05300.itc", 0x23)
    OP_68(-6830, 1000, 10260, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -13400, 200, 6850, 180)
    SetChrPos(0x102, -13700, 200, 3600, 0)
    SetChrPos(0x103, -12800, 200, 3600, 0)
    SetChrPos(0x104, -11900, 200, 3600, 0)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -12300, 200, 6850, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01300.itp")
    FadeToBright(1000, 0)
    OP_68(-12750, 1000, 5380, 6000)
    OP_0D()
    OP_6F(0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0171
    AnonymousTalk(
        0xB,
        (
            "──初めまして。\x01",
            "セシル・ノイエスといいます。\x02\x03",

            "ふふ、どちら様かと思ったけど\x01",
            "ロイドの同僚さんだったんですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0172
    ChrTalk(
        0x102,
        (
            "#0102F#6Pは、はい……\x01",
            "エリィ・マクダエルです。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        (
            "#0203F#12Pどうも……\x01",
            "ティオ・プラトーです。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#0309F#2Pランディ・オルランドっス！\x01",
            "どうぞお見知りおきを！\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "#1302F#5Pふふ、よろしくね。\x02\x03",

            "#1306Fはあ……\x01",
            "でも、私ったら慌てんぼうね。\x02\x03",

            "てっきりロイドが彼女を連れて\x01",
            "遊びに来たかと思っちゃったわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(500)

    #C0176
    ChrTalk(
        0x101,
        "#0011F#1Pちょ、何を言い出すのさ！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    #C0177
    ChrTalk(
        0xB,
        (
            "#1309F#11Pだって３年ぶりでしょう？\x02\x03",

            "彼女の１人か２人くらい作って\x01",
            "お姉ちゃんに\x01",
            "紹介してくれるのかな～って。\x02\x03",

            "#1305Fはっ、ひょっとして\x01",
            "本当に付き合っているけど\x01",
            "仕事だから隠しているとか……\x02\x03",

            "#1308Fご、ごめんなさい。\x01",
            "悪いことをしちゃったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#0006F#1Pあ、あのねぇ……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xB,
        (
            "#1309F#11Pそれで……\x01",
            "どっちと付き合ってるの？\x02\x03",

            "エリィさん？　ティオちゃん？\x01",
            "それとも２人いっぺんにとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        "#0001F#1Pだから違うってば！\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xB,
        (
            "#1305F#11Pはっ……\x01",
            "も、もしかしてそこの彼と……\x02\x03",

            "#1306Fううん、私もそういうのには\x01",
            "理解のある姉でいたいから……\x02\x03",

            "#1301F全力で応援させてもらうわっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#0012F#1Pいや！\x01",
            "そこは反対するとこだから！？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x102,
        "#0109F#6Pクスクス……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x103,
        (
            "#0202F#12Pなんだか……\x01",
            "ユニークなお姉さんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x104,
        "#0309F#2Pは～、天然なところも素敵だ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)

    #C0186
    ChrTalk(
        0x101,
        (
            "#0003F#1P──コホン。\x02\x03",

            "#0001Fそれで、セシル姉。\x01",
            "魔獣騒ぎのことなんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xB,
        (
            "#1303F#11Pうん、そうだったわね。\x02\x03",

            "#1300F師長から許可は貰ったから\x01",
            "私が説明させてもらうけど……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(200)
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0188
    ChrTalk(
        0xB,
        (
            "#1303F#5P……１週間前の夜のことよ。\x02\x03",

            "うちで研修医をしている人が\x01",
            "魔獣に襲われてしまったの。\x02\x03",

            "#1301Fただ、おかしな事があって……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        (
            "#0201F#12P警備隊の調書によると\x01",
            "被害者の勘違いの可能性もあると\x01",
            "書かれていましたが……？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xB,
        (
            "#1306F#5P……そう。\x01",
            "やっぱり半信半疑みたいね。\x02\x03",

            "#1301F私も詳しくは知らないけど……\x01",
            "病棟の屋上で襲われたらしいの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0191
    ChrTalk(
        0x101,
        "#0005F#1P屋上……！？\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x102,
        "#0101F#6Pどういう事でしょう……？\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "#1300F#5Pえっと、病棟の屋上は\x01",
            "庭園みたいなテラスになってるの。\x02\x03",

            "奥には先生方が詰めている\x01",
            "研究棟なんてのも建っていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x104,
        (
            "#0301F#2Pなるほど……\x01",
            "要するに魔獣が出るような場所じゃ\x01",
            "あり得ないってことッスね？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        (
            "#1306F#5Pええ……警備隊の人たちも\x01",
            "最終的にそう判断したみたい。\x02\x03",

            "#1308Fでも、やっぱりどこか\x01",
            "納得行かなかったんでしょうね。\x02\x03",

            "#1301Fあなた達に調査を\x01",
            "お願いしているところを見ると。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        (
            "#0006F#1Pい、いや～……どうかな。\x02\x03",

            "#0008F正直そんなに期待されては\x01",
            "いないと思ってるけど……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    #C0197
    ChrTalk(
        0xB,
        (
            "#1302F#11Pふふ、謙遜しないで。\x02\x03",

            "クロスベルタイムズを読んだけど\x01",
            "すごく頑張ってるみたいじゃない？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0198
    ChrTalk(
        0x101,
        (
            "#0005F#1Pあ……\x01",
            "そうか、あの旧市街の事件か。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 1)), scpexpr(EXPR_END)), "loc_469A")

    #C0199
    ChrTalk(
        0x102,
        (
            "#0105F#6Pですが、最新の記事には\x01",
            "私たちが解決したとまでは……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46E5")

    label("loc_469A")


    #C0200
    ChrTalk(
        0x104,
        (
            "#0302F#12Pひょっとして、俺たちのこと\x01",
            "カッコよく書かれちゃってます！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E5")

    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(200)

    #C0201
    ChrTalk(
        0xB,
        (
            "#1304F#5Pふふ、そうは書かれてないけど\x01",
            "頑張ってることは伝わってきたわ。\x02\x03",

            "#1302Fそれに、ちょっと前まで\x01",
            "うちに怪我をしていた男の子たちが\x01",
            "入院していたんだけど……\x02\x03",

            "お見舞いに来た仲間の子たちから\x01",
            "ちょっとだけ話を聞いちゃったの。\x02\x03",

            "#1309Fあなたたちに\x01",
            "大きな借りを作っちゃったって。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#0000F#1Pそ、そうだったんだ……\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        "#0102F#6Pふふ、面白い偶然ですね。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x104,
        "#0309F#2Pいや～、照れちゃうなぁ。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#0203F#12Pランディさんはそれほど\x01",
            "活躍してないと思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xB,
        (
            "#1303F#5Pでも、そうね……\x02\x03",

            "#1300Fこの先は、実際に被害にあった人から\x01",
            "直接聞いた方がいいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        (
            "#0003F#1Pうん、できれば紹介してほしい。\x02\x03",

            "#0001Fそれと……\x01",
            "実際の現場を調べておきたいかな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    #C0208
    ChrTalk(
        0xB,
        (
            "#1302F#11P分かった。\x01",
            "どちらも案内するから任せて。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -12300, 0, 6400, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0209
    ChrTalk(
        0x101,
        (
            "#0005F#1Pあっと……\x01",
            "セシル姉、時間の方は大丈夫？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x1F4)

    #C0210
    ChrTalk(
        0xB,
        (
            "#1300F#11Pうん、ちょうど今は\x01",
            "休憩時間になっているから。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    #C0211
    ChrTalk(
        0xB,
        (
            "#1309F#5Pそれじゃあまずは、\x01",
            "病院棟の２階に行きましょう。\x02\x03",

            "みんな、私に付いてきて。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x102,
        "#0102F#6Pはいっ。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        "#0204F#12P……了解です。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x104,
        "#0309F#2Pお供しまッス！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0215
    ChrTalk(
        0x101,
        (
            "#0012F#5P（……みんないきなり\x01",
            "  セシル姉に馴染んでるなぁ。）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7123", 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0xB, 0x80)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    AddParty(0x35, 0xFF, 0xFF)
    SetChrPos(0x0, -10400, 0, 6500, 90)
    SetScenarioFlags(0x62, 0)
    OP_29(0x3F, 0x1, 0x9)
    EventEnd(0x5)
    Return()

    # Function_14_39E6 end

    def Function_15_4C1B(): pass

    label("Function_15_4C1B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch05302.itc", 0x22)
    LoadChrToIndex("chr/ch08202.itc", 0x23)
    OP_68(-9140, 1000, 9070, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23610, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4C9C")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_4CC3")

    label("loc_4C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4CB2")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_4CC3")

    label("loc_4CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4CC3")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_4CC3")

    SetChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0x153, 0x23)
    SetChrSubChip(0x153, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x153, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xEF, 0x4)
    SetChrPos(0x153, -13350, 300, 3500, 0)
    SetChrPos(0x101, -12350, 200, 3500, 0)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -12350, 200, 6850, 180)
    SetChrPos(0xEF, -13350, 200, 6850, 180)
    FadeToBright(1000, 0)
    OP_68(-12880, 1200, 5390, 5000)
    OP_6F(0x1)
    OP_0D()

    #C0216
    ChrTalk(
        0xB,
        (
            "#1309F#5Pふふっ、私ったら\x01",
            "ちょっとあわてんぼうね。\x02\x03",

            "#1302F１８歳のロイドが、\x01",
            "９歳くらいのキーアちゃんの\x01",
            "パパであるはずないのにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#0006F#12Pはあ……当たり前だろ。\x02\x03",

            "#0001Fそもそも、なんで親子なんて\x01",
            "突拍子もない考えになるのさ？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        (
            "#1306F#5Pだって、何だかすごく\x01",
            "家族って感じがしたから……\x02\x03",

            "#1300F直感的に、キーアちゃんのパパが\x01",
            "ロイドって思い込んじゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        "#0011F#12Pへっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x153, 0x2)

    #C0220
    ChrTalk(
        0x153,
        (
            "#1105F#6Pキーアのパパって\x01",
            "ロイドだったのー！？\x02\x03",

            "#1110Fキーア、知らなかったー！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x101, 0x1)

    #C0221
    ChrTalk(
        0x101,
        "#0012F#11Pいやいや、違うから！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(150)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_5074")

    #C0222
    ChrTalk(
        0xB,
        (
            "#1302F#11Pふふっ……\x01",
            "ねえ、エリィちゃん。\x02\x03",

            "そうやって２人が並んでると\x01",
            "そんな風に見えないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x102,
        (
            "#0105F#5Pああ……！\x01",
            "言われてみれば確かに。\x02\x03",

            "#0104F顔は似てませんけど\x01",
            "雰囲気が親子っていうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_520D")

    label("loc_5074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_514A")

    #C0224
    ChrTalk(
        0xB,
        (
            "#1302F#11Pふふっ……\x01",
            "ねえ、ティオちゃん。\x02\x03",

            "そうやって２人が並んでると\x01",
            "そんな風に見えないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x103,
        (
            "#0205F#5P……言われてみれば確かに。\x02\x03",

            "#0204F顔の造形は似ていませんが\x01",
            "親子という感じがします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_520D")

    label("loc_514A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_520D")

    #C0226
    ChrTalk(
        0xB,
        (
            "#1302F#11Pふふっ……\x01",
            "ねえ、ランディ君。\x02\x03",

            "そうやって２人が並んでると\x01",
            "そんな風に見えないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x104,
        (
            "#0305F#5Pいや～、確かに。\x02\x03",

            "#0309Fぜんぜん似てないけど\x01",
            "確かに親子っぽい感じッス。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_520D")


    #C0228
    ChrTalk(
        0x101,
        "#0011F#12Pそ、そうなのか……？\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x153,
        (
            "#1104F#6Pえへへ～……\x01",
            "ロイドがパパかぁ。\x02\x03",

            "#1100F……ロイドじゃなくって\x01",
            "パパって呼んだほうがいい？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        (
            "#0012F#11Pうっ……\x01",
            "今まで通りでいいから！\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x153,
        "#1103F#6Pんー、そっか。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x153, 0x0)
    Sleep(300)

    #C0232
    ChrTalk(
        0x153,
        (
            "#1110F#12Pでもでも、\x01",
            "セシルっていいヒトだね！\x02\x03",

            "#1109Fキーア、セシル大好き！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    Sleep(150)

    #C0233
    ChrTalk(
        0xB,
        (
            "#1309F#5Pふふっ……\x01",
            "私もキーアちゃんが大好きよ。\x02\x03",

            "気が合うわね、私たち。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x153,
        "#1109F#12Pうんっ！\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0xB, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_542E")

    #C0235
    ChrTalk(
        0x102,
        (
            "#0102F#5P（ふふっ、あっという間に\x01",
            "  仲良くなっちゃったわね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54BF")

    label("loc_542E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_547A")

    #C0236
    ChrTalk(
        0x103,
        (
            "#0202F#5P（くす、あっという間に\x01",
            "  仲良くなりましたね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54BF")

    label("loc_547A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_54BF")

    #C0237
    ChrTalk(
        0x104,
        (
            "#0300F#5P（ハハ、あっという間に\x01",
            "  馴染んじまったな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54BF")


    #C0238
    ChrTalk(
        0x101,
        (
            "#0006F#12P（ハア、それはいいけど\x01",
            "  なんかどっと疲れたよ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xB,
        (
            "#1303F#5P……それで……\x01",
            "キーアちゃんの記憶だったわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0xEF, 0x1)

    #C0240
    ChrTalk(
        0x101,
        (
            "#0003F#12Pあ、ああ……\x01",
            "大体の事情は話した通りさ。\x02\x03",

            "#0001Fこの病院にある『神経科』に\x01",
            "キーアを見て欲しいんだけど……\x02\x03",

            "どの先生に頼めばいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xB,
        (
            "#1304F#5Pふふ、あなた達も面識が\x01",
            "あったんじゃないかしら？\x02\x03",

            "#1300Fヨアヒム・ギュンター先生よ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0242
    ChrTalk(
        0x101,
        (
            "#0005F#12Pええっ……\x01",
            "あの人が『神経科』の！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_570C")
    SetChrSubChip(0x102, 0x1)

    #C0243
    ChrTalk(
        0x102,
        "#0105F#6Pそ、そうだったんですか……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5771")

    label("loc_570C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_5743")
    SetChrSubChip(0x103, 0x1)

    #C0244
    ChrTalk(
        0x103,
        "#0205F#6Pそうだったんですか……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5771")

    label("loc_5743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_5771")
    SetChrSubChip(0x104, 0x1)

    #C0245
    ChrTalk(
        0x104,
        "#0305F#6Pそうだったのか……\x02",
    )

    CloseMessageWindow()

    label("loc_5771")


    #C0246
    ChrTalk(
        0xB,
        (
            "#1302F#5Pふふっ、普段は釣り好きで\x01",
            "呑気そうな人に見えるけど……\x02\x03",

            "ああ見えて、外国の医療機関で\x01",
            "凄い研究成果を上げた人らしいの。\x02\x03",

            "この病院では『薬学』『神経科』の\x01",
            "２部門を取り仕切っているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#0000F#12Pそ、そうなんだ……\x02\x03",

            "それじゃあ、キーアの事は\x01",
            "あの先生に相談すれば……？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xB,
        (
            "#1304F#5Pええ、きっと\x01",
            "力になってくださるはずよ。\x02\x03",

            "#1302Fさっそく受付に行って\x01",
            "問い合わせてもらいましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(21610, 3000)
    OP_6F(0x10)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_4C1B end

    def Function_16_591C(): pass

    label("Function_16_591C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-10080, 1000, 14190, 0)
    MoveCamera(53, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19140, 0)
    SetChrPos(0x101, -10300, 0, 13500, 270)
    SetChrPos(0x102, -10300, 0, 14700, 270)
    SetChrPos(0x103, -9100, 0, 13500, 270)
    SetChrPos(0x104, -9100, 0, 14700, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59C5")
    SetChrPos(0x109, -9750, 0, 12300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_59F0")

    label("loc_59C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59F0")
    SetChrPos(0x10A, -9750, 0, 12300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_59F0")

    SetChrSubChip(0x9, 0x1)
    OP_0D()

    #C0249
    ChrTalk(
        0x101,
        (
            "#11P#0000Fえっと、あなたが\x01",
            "フローラさんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x9,
        (
            "#6P……あら、\x01",
            "私に何か用かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#11P#0000Fクロスベル警察・\x01",
            "特務支援課のものです。\x02\x03",

            "図書館の依頼で、\x01",
            "延滞している本の回収を\x01",
            "しているのですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0252
    ChrTalk(
        0x9,
        "#6Pあっ、そういうことか。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x9,
        (
            "#6Pう、うーん、\x01",
            "返したいのは山々なんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0254
    ChrTalk(
        0x102,
        (
            "#11P#0105F何か返却できない\x01",
            "理由があったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x9,
        "#6Pえぇ、まぁ……\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x9,
        (
            "#6P私、よく研究棟の資料室にある\x01",
            "医学書を持ち出して、\x01",
            "ここで勉強しているんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x9,
        (
            "#6P資料室の本棚に本を戻した時に\x01",
            "一緒に図書館の本も\x01",
            "本棚に入れちゃったみたいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x9,
        (
            "#6P気づいた時には、\x01",
            "どこにやったかわからなく\x01",
            "なっちゃってたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x103,
        "#11P#0203F……うっかり屋さんですね。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x104,
        (
            "#11P#0306Fま、そういうことなら\x01",
            "仕方ねぇか。\x02\x03",

            "#0300F俺もよく、グラビア本を\x01",
            "どこにやったかわからなく\x01",
            "なることがあるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        (
            "#11P#0211F……ランディさんのそれとは\x01",
            "毛色が違う気がしますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        (
            "#11P#0006Fと、ともかく……\x01",
            "延滞本は資料室の本棚に\x01",
            "あるんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x9,
        (
            "#6Pええ、間違いないわ。\x01",
            "申し訳ないけど、\x01",
            "探してみてもらえるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x9,
        (
            "#6P資料室は、病棟屋上にある\x01",
            "研究棟の中にあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        (
            "#11P#0003F研究棟は行ったことが\x01",
            "あるし……場所は分かるな。\x02\x03",

            "#0000Fよし、それじゃあ\x01",
            "探しに行ってみようか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5ECA")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_5ECA")

    SetChrPos(0x0, -10220, 0, 13340, 270)
    OP_29(0x28, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_16_591C end

    def Function_17_5EE4(): pass

    label("Function_17_5EE4")

    EventBegin(0x1)

    #C0266
    ChrTalk(
        0x103,
        (
            "#0205Fロイドさん、\x01",
            "この下は食堂ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#0005Fおっと、こっちじゃないな。\x02\x03",

            "#0001F……さっき積んであった\x01",
            "木箱やコンテナは……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9230, 3750, 13010, 0)
    EventEnd(0x4)
    Return()

    # Function_17_5EE4 end

    def Function_18_5F85(): pass

    label("Function_18_5F85")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　お見舞い・外来患者用宿泊施設　　\x01",
            "※ご利用の際は寮長にお申し付け下さい\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_5F85 end

    SaveToFile()

Try(main)
