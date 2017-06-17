from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c047b.bin",                # FileName
        "c047b",                    # MapName
        "c047b",                    # Location
        0x0025,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c047b",                  # 0
        "ドレイク・オーナー",     # 1
        "チェリー",               # 2
        "ガレッティ",             # 3
        "エリンデ",               # 4
        "レイタロッサ",           # 5
        "リッケ爺さん",           # 6
    ))

    AddCharChip((
        "chr/ch20002.itc",                   # 00
        "chr/ch25800.itc",                   # 01
        "chr/ch25900.itc",                   # 02
        "chr/ch27000.itc",                   # 03
        "chr/ch27100.itc",                   # 04
        "chr/ch33302.itc",                   # 05
    ))

    DeclNpc(-899,    4000,    21299,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(6199,    -1000,   8000,    270,  261,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       -1000,   13649,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-6500,   -1000,   6000,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(1350,    -949,    11500,   0,    261,  0x0, 0,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(6699,    4269,    15750,   90,   261,  0x0, 0,   0,   0,   255, 255, 0,   12,  255,  0)

    DeclActor(-900,    4000,    20000,   2000,    -900,    5500,    21300,   0x007E, 0,  3,  0x0000)
    DeclActor(5240,    -1000,   8000,    1200,    6200,    500,     8000,    0x007E, 0,  5,  0x0000)
    DeclActor(-920,    -1000,   12050,   1700,    0,       500,     13650,   0x007E, 0,  7,  0x0000)
    DeclActor(-4500,   -1000,   6000,    1500,    -6500,   500,     6000,    0x007E, 0,  9,  0x0000)

    ScpFunction((
        "Function_0_218",          # 00, 0
        "Function_1_2D0",          # 01, 1
        "Function_2_2D1",          # 02, 2
        "Function_3_2FB",          # 03, 3
        "Function_4_2FF",          # 04, 4
        "Function_5_5B4",          # 05, 5
        "Function_6_5B8",          # 06, 6
        "Function_7_77C",          # 07, 7
        "Function_8_780",          # 08, 8
        "Function_9_89C",          # 09, 9
        "Function_10_8A0",         # 0A, 10
        "Function_11_90F",         # 0B, 11
        "Function_12_AFF",         # 0C, 12
    ))


    def Function_0_218(): pass

    label("Function_0_218")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_258"),
        (1, "loc_264"),
        (2, "loc_270"),
        (3, "loc_27C"),
        (4, "loc_288"),
        (5, "loc_294"),
        (6, "loc_2A0"),
        (SWITCH_DEFAULT, "loc_2AC"),
    )


    label("loc_258")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_264")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_270")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_27C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_288")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_294")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_2A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_2AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_2B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_2CF")

    Return()

    # Function_0_218 end

    def Function_1_2D0(): pass

    label("Function_1_2D0")

    Return()

    # Function_1_2D0 end

    def Function_2_2D1(): pass

    label("Function_2_2D1")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -6000, -1000, 16000, 5000, 5000, 0)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    Return()

    # Function_2_2D1 end

    def Function_3_2FB(): pass

    label("Function_3_2FB")

    Call(0, 4)
    Return()

    # Function_3_2FB end

    def Function_4_2FF(): pass

    label("Function_4_2FF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_397")

    #C0001
    ChrTalk(
        0x8,
        (
            "ガンツさんの話を聞きましたか……\x01",
            "確かにあれは異常な冴えですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "まったく……どこでどうやって\x01",
            "カンを鍛えたものやら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F8")

    label("loc_397")


    #C0003
    ChrTalk(
        0x8,
        (
            "おや皆さん、いかがでしたか？\x01",
            "ガンツさんには会えましたかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0003Fええ、まあ……\x01",
            "大分予想とは違いましたが、何とか。\x02\x03",

            "#0000Fご協力ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#0301Fしっかし謎なのは\x01",
            "奴の異常なギャンブル能力だぜ。\x02\x03",

            "#0306Fなんでその力が\x01",
            "俺に目覚めないんだっつーの！\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        "#0106Fふう、まだ拘ってるのね。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x103,
        "#0211F……………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_4F8")

    Jump("loc_5B0")

    label("loc_4FD")


    #C0008
    ChrTalk(
        0x8,
        (
            "ガンツさんならウチの常連ですよ。\x01",
            "間違えるはずはありませんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "ホテル・ミレニアムの\x01",
            "最上階デラックスルームに\x01",
            "ご滞在なさってる筈ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "ご用ならお会いになられては？\x02",
    )

    CloseMessageWindow()

    label("loc_5B0")

    TalkEnd(0x8)
    Return()

    # Function_4_2FF end

    def Function_5_5B4(): pass

    label("Function_5_5B4")

    Call(0, 6)
    Return()

    # Function_5_5B4 end

    def Function_6_5B8(): pass

    label("Function_6_5B8")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_778")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "交換をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_621")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_621")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_654")
    SetScenarioFlags(0x6D, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_643")
    OP_AF(0x3F)
    Jump("loc_645")

    label("loc_643")

    OP_AF(0x3E)

    label("loc_645")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_773")

    label("loc_654")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_668")
    Jump("loc_773")

    label("loc_668")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_773")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6E6")

    #C0011
    ChrTalk(
        0x9,
        (
            "ガンツさん、最近\x01",
            "アタリが来ちゃってるのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x9,
        "なんだか前とは別人みた～い。\x02",
    )

    CloseMessageWindow()
    Jump("loc_773")

    label("loc_6E6")


    #C0013
    ChrTalk(
        0x9,
        (
            "でもガンツさん、\x01",
            "最近様子が変かも～。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "スッゴク偉そうになったし～\x01",
            "バカみたいに当てまくるし～。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        "なんだか前とは別人みた～い。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_773")

    Jump("loc_5C5")

    label("loc_778")

    TalkEnd(0x9)
    Return()

    # Function_6_5B8 end

    def Function_7_77C(): pass

    label("Function_7_77C")

    Call(0, 8)
    Return()

    # Function_7_77C end

    def Function_8_780(): pass

    label("Function_8_780")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7DA")

    #C0016
    ChrTalk(
        0xA,
        (
            "以前はフルハウスが精々だった方が\x01",
            "はて、どうしてあれほどのツキを……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_898")

    label("loc_7DA")


    #C0017
    ChrTalk(
        0xA,
        (
            "ガンツ様はカード勝負となると\x01",
            "素晴らしい手ばかりお引きになります。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "絶対にイカサマは無いと\x01",
            "言い切れるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xA,
        (
            "どうしてあれほど運がよいのか、\x01",
            "はてどうしても判らぬのです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_898")

    TalkEnd(0xA)
    Return()

    # Function_8_780 end

    def Function_9_89C(): pass

    label("Function_9_89C")

    Call(0, 10)
    Return()

    # Function_9_89C end

    def Function_10_8A0(): pass

    label("Function_10_8A0")

    TalkBegin(0xB)

    #C0020
    ChrTalk(
        0xB,
        (
            "ガンツさんのツキとカンは\x01",
            "異常ですわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xB,
        (
            "わたくしもあそこまで\x01",
            "負けが続いたのは初めてですわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_10_8A0 end

    def Function_11_90F(): pass

    label("Function_11_90F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A3")
    Jump("loc_9ED")

    label("loc_9A3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9C3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9ED")

    label("loc_9C3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9ED")

    label("loc_9E3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9ED")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A7F")

    #C0022
    ChrTalk(
        0xC,
        "私も一度勝負してみたのだけど。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xC,
        (
            "とても冴えないギャンブラー\x01",
            "って感じじゃなかったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF7")

    label("loc_A7F")


    #C0024
    ChrTalk(
        0xC,
        (
            "あのガンツっていう男、\x01",
            "元は冴えないギャンブラー\x01",
            "だったそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xC,
        (
            "本当かしら。\x01",
            "とても想像できないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_AF7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_90F end

    def Function_12_AFF(): pass

    label("Function_12_AFF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B93")
    Jump("loc_BDD")

    label("loc_B93")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BB3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDD")

    label("loc_BB3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BD3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDD")

    label("loc_BD3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BDD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0026
    ChrTalk(
        0xD,
        (
            "うむむ、いい所なのに\x01",
            "日が暮れてしもうたわい……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xD,
        (
            "嫌じゃ、帰りたくない。\x01",
            "今が丁度ノリノリなんじゃ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_AFF end

    SaveToFile()

Try(main)
