from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1020.bin",                # FileName
        "t1020",                    # MapName
        "t1020",                    # Location
        0x0095,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 149, 0, 3, 0, 4],
    )

    BuildStringList((
        "t1020",                  # 0
        "エリーゼ",               # 1
        "青年",                   # 2
        "観光客",                 # 3
        "観光客",                 # 4
        "女性",                   # 5
        "女の子",                 # 6
        "店員",                   # 7
    ))

    AddCharChip((
        "chr/ch23600.itc",                   # 00
        "chr/ch26700.itc",                   # 01
        "chr/ch21600.itc",                   # 02
        "chr/ch21100.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch33200.itc",                   # 05
        "chr/ch25900.itc",                   # 06
    ))

    DeclNpc(-24909,  0,       5570,    90,   257,  0x0, 0,   5,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(100139,  0,       18219,   0,    385,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4190,    0,       13079,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(97510,   0,       5429,    270,  385,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-23930,  0,       11470,   0,    385,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-22840,  0,       10689,   315,  401,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-18940,  0,       12609,   180,  385,  0x0, 0,   6,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 14,  26.5,                  8.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -8.833333969116211,    -0.800000011920929,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 15,  8.5,                   8.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.8333334922790527,   -0.800000011920929,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 15,  -11.0,                 8.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.6666667461395264,    -0.800000011920929,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 13,  -19.030000686645508,   11.899999618530273,    -1.0,                  2.4964001178741455,    [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.6329113841056824,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   9.515000343322754,     -7.53164529800415,     0.20000000298023224,   1.0])

    DeclActor(27660,   0,       10070,   1200,    27660,   1500,    10070,   0x007C, 0,  18, 0x0000)
    DeclActor(19000,   0,       11850,   2000,    19000,   1000,    11850,   0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_388",          # 00, 0
        "Function_1_440",          # 01, 1
        "Function_2_46B",          # 02, 2
        "Function_3_496",          # 03, 3
        "Function_4_566",          # 04, 4
        "Function_5_5CB",          # 05, 5
        "Function_6_6DE",          # 06, 6
        "Function_7_71E",          # 07, 7
        "Function_8_851",          # 08, 8
        "Function_9_982",          # 09, 9
        "Function_10_A7D",         # 0A, 10
        "Function_11_AE8",         # 0B, 11
        "Function_12_B31",         # 0C, 12
        "Function_13_C3C",         # 0D, 13
        "Function_14_10DE",        # 0E, 14
        "Function_15_14A8",        # 0F, 15
        "Function_16_18D5",        # 10, 16
        "Function_17_1B10",        # 11, 17
        "Function_18_1B5B",        # 12, 18
    ))


    def Function_0_388(): pass

    label("Function_0_388")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3C8"),
        (1, "loc_3D4"),
        (2, "loc_3E0"),
        (3, "loc_3EC"),
        (4, "loc_3F8"),
        (5, "loc_404"),
        (6, "loc_410"),
        (SWITCH_DEFAULT, "loc_41C"),
    )


    label("loc_3C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_3F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_404")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_410")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_41C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_428")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_428")

    label("loc_43F")

    Return()

    # Function_0_388 end

    def Function_1_440(): pass

    label("Function_1_440")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46A")
    OP_94(0xFE, 0x17D0E, 0x3F0C, 0x19154, 0x47A4, 0x3E8)
    Sleep(150)
    Jump("Function_1_440")

    label("loc_46A")

    Return()

    # Function_1_440 end

    def Function_2_46B(): pass

    label("Function_2_46B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_495")
    OP_94(0xFE, 0x3AC, 0x28D2, 0x12FC, 0x37E6, 0x3E8)
    Sleep(300)
    Jump("Function_2_46B")

    label("loc_495")

    Return()

    # Function_2_46B end

    def Function_3_496(): pass

    label("Function_3_496")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B8")
    Event(0, 15)

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4C6")
    Jump("loc_565")

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4D4")
    Jump("loc_565")

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_4E2")
    Jump("loc_565")

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4F0")
    Jump("loc_565")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_4FE")
    Jump("loc_565")

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_52E")
    SetChrPos(0x8, -13780, 0, 6020, 90)
    SetChrPos(0xA, -12240, 0, 6020, 270)
    Jump("loc_565")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_55C")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_565")

    label("loc_55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_565")

    label("loc_565")

    Return()

    # Function_3_496 end

    def Function_4_566(): pass

    label("Function_4_566")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_588")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A8")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_5A8")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C4")
    ClearMapObjFlags(0x3, 0x10)
    OP_66(0x1, 0x1)

    label("loc_5C4")

    ClearMapObjFlags(0x2, 0x10)
    Return()

    # Function_4_566 end

    def Function_5_5CB(): pass

    label("Function_5_5CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_5DC")
    Jump("loc_6DA")

    label("loc_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_5EA")
    Jump("loc_6DA")

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_5F8")
    Jump("loc_6DA")

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_606")
    Jump("loc_6DA")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_614")
    Jump("loc_6DA")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_65E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F")
    Call(0, 8)
    Jump("loc_659")

    label("loc_62F")


    #C0001
    ChrTalk(
        0xFE,
        "……まったく、品のない観光客だこと。\x02",
    )

    CloseMessageWindow()

    label("loc_659")

    Jump("loc_6DA")

    label("loc_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_6D1")

    #C0002
    ChrTalk(
        0xFE,
        (
            "ふぅ……まったく。\x01",
            "ここはいつ来ても混んでますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "普通に買い物に来るだけで一苦労ですわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DA")

    label("loc_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6DA")

    label("loc_6DA")

    TalkEnd(0xFE)
    Return()

    # Function_5_5CB end

    def Function_6_6DE(): pass

    label("Function_6_6DE")

    TalkBegin(0xFE)

    #C0004
    ChrTalk(
        0xFE,
        (
            "うおおおー！！！\x01",
            "待ってろよみっしぃぃぃぃぃぃい！！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_6DE end

    def Function_7_71E(): pass

    label("Function_7_71E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_72F")
    Jump("loc_84D")

    label("loc_72F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_73D")
    Jump("loc_84D")

    label("loc_73D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_74B")
    Jump("loc_84D")

    label("loc_74B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_759")
    Jump("loc_84D")

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_767")
    Jump("loc_84D")

    label("loc_767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_7C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_782")
    Call(0, 8)
    Jump("loc_7C4")

    label("loc_782")


    #C0005
    ChrTalk(
        0xFE,
        (
            "なんてこった……\x01",
            "金持ちアピールじゃ\x01",
            "ここの娘はなびかねぇ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C4")

    Jump("loc_84D")

    label("loc_7C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_844")

    #C0006
    ChrTalk(
        0xFE,
        (
            "さすが高級保養地……\x01",
            "お嬢様タイプの女の子が\x01",
            "わんさかいらぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "よぉし……いっちょ\x01",
            "声をかけてみるか！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84D")

    label("loc_844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_84D")

    label("loc_84D")

    TalkEnd(0xFE)
    Return()

    # Function_7_71E end

    def Function_8_851(): pass

    label("Function_8_851")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0xA, 0x8, 0)

    #C0008
    ChrTalk(
        0xA,
        (
            "よう、彼女……\x01",
            "よかったらそこのレストランで\x01",
            "食事でもどうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xA,
        (
            "大丈夫、ミラならたっぷり\x01",
            "持ってきてるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "……結構です。\x01",
            "あなたにご馳走になる筋合いは\x01",
            "ありませんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "たぶん、ミラなら\x01",
            "あなたより私の方が\x01",
            "持っていると思いますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        "#4Sズガーン！#3S\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_8_851 end

    def Function_9_982(): pass

    label("Function_9_982")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2D")

    #C0013
    ChrTalk(
        0xFE,
        (
            "ここが《フォルトゥナ》……\x01",
            "ふむ、さすがに豪華な\x01",
            "店構えをしておるのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "……だが問題は料理の味じゃ！\x01",
            "美食家のわしは\x01",
            "見た目じゃ惑わされんぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A79")

    label("loc_A2D")


    #C0015
    ChrTalk(
        0xFE,
        (
            "さぁ、名高き保養地の\x01",
            "レストランの味……\x01",
            "この舌で確かめさせてもらおう！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A79")

    TalkEnd(0xFE)
    Return()

    # Function_9_982 end

    def Function_10_A7D(): pass

    label("Function_10_A7D")

    TalkBegin(0xFE)

    #C0016
    ChrTalk(
        0xFE,
        (
            "この宝飾店……\x01",
            "私みたいな普通の観光客は\x01",
            "入店すらさせてくれないのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "きーっ！　くやしい！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_A7D end

    def Function_11_AE8(): pass

    label("Function_11_AE8")

    TalkBegin(0xFE)

    #C0018
    ChrTalk(
        0xFE,
        (
            "ママー……\x01",
            "宝石なんかいいから、\x01",
            "テーマパークであそぼうよう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_AE8 end

    def Function_12_B31(): pass

    label("Function_12_B31")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0019
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1E")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x7, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x7, 0x0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x7, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_C1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3A")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_C3A")

    Return()

    # Function_12_B31 end

    def Function_13_C3C(): pass

    label("Function_13_C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1089")
    EventBegin(0x0)
    Fade(1000)
    OP_68(-19000, 1000, 11800, 0)
    SetChrPos(0x101, -19330, 0, 8810, 0)
    SetChrPos(0x102, -17960, 0, 8810, 0)
    SetChrPos(0x103, -20760, 0, 10150, 45)
    SetChrPos(0x104, -16940, 0, 9380, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC1")
    SetChrPos(0x151, -18610, 0, 7180, 0)

    label("loc_CC1")

    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -19000, 0, 12900, 180)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)

    def lambda_D01():
        OP_96(0xFE, 0xFFFFB5C8, 0x0, 0x2C2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_D01)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
    WaitChrThread(0xE, 1)

    #C0020
    ChrTalk(
        0x101,
        "#0005Fうわっと……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "#11P宝飾店《ディアマンテ》へ\x01",
            "ようこそいらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xE,
        (
            "#11P……失礼ですがお客様。\x01",
            "どなたかからの紹介状は\x01",
            "お持ちでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#0105Fええっと……\x01",
            "紹介が必要なのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xE,
        "#11P左様。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xE,
        (
            "#11P当店は会員専用になっておりますので\x01",
            "入店はお控えくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xE,
        "#11Pそれでは……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)
    Sleep(100)

    def lambda_E71():
        OP_96(0xFE, 0xFFFFB5C8, 0x0, 0x3264, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E71)
    Sleep(300)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    WaitChrThread(0xE, 1)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0xE, 0x80)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    #C0027
    ChrTalk(
        0x103,
        "#0211F……一見様お断り、というヤツですか。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        "#0310Fか、感じ悪ィ～……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103A")

    #C0029
    ChrTalk(
        0x151,
        (
            "#5704Fこういう場所の店では\x01",
            "よくあることさ。\x02\x03",

            "高級な装飾品があれば\x01",
            "コーディネートの完成度は\x01",
            "増すだろうけど……\x02\x03",

            "#5702Fま、今回は諦めなよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#0006Fそ、そうだな……\x01",
            "今はとにかく、ブティックに行こう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107E")

    label("loc_103A")


    #C0031
    ChrTalk(
        0x101,
        (
            "#0006Fと、とにかく……\x01",
            "入れないなら仕方ないな。\x01",
            "今は諦めよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107E")

    OP_5A()
    SetScenarioFlags(0xAE, 1)
    EventEnd(0x5)
    Jump("loc_10DD")

    label("loc_1089")

    EventBegin(0x1)

    #C0032
    ChrTalk(
        0x101,
        (
            "#0001Fここは会員制の\x01",
            "宝飾店みたいだな。\x01",
            "今回は諦めよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -18610, 0, 9950, 180)
    EventEnd(0x4)

    label("loc_10DD")

    Return()

    # Function_13_C3C end

    def Function_14_10DE(): pass

    label("Function_14_10DE")

    EventBegin(0x0)
    Fade(1000)
    OP_68(27100, 1600, 7920, 0)
    MoveCamera(315, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, 25000, 0, 7600, 90)
    SetChrPos(0x102, 23800, 0, 8900, 90)
    SetChrPos(0x103, 23800, 0, 7600, 90)
    SetChrPos(0x104, 25000, 0, 8900, 90)
    OP_68(25100, 1600, 7920, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0033
    ChrTalk(
        0x101,
        "#0001F#5Pこの先は……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#0105F#5Pどうやら封鎖されて\x01",
            "いるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x104,
        "#0305F#5Pお、何か書いてあるぜ。\x02",
    )

    CloseMessageWindow()
    OP_68(26500, 1600, 7920, 3000)

    def lambda_120C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_120C)
    Sleep(300)

    def lambda_1224():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1224)
    Sleep(100)

    def lambda_123C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_123C)
    Sleep(50)

    def lambda_1254():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1254)
    WaitChrThread(0x104, 1)

    def lambda_126D():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_126D)
    WaitChrThread(0x101, 1)

    def lambda_127E():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_127E)
    WaitChrThread(0x102, 1)

    def lambda_128F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_128F)
    WaitChrThread(0x103, 1)

    def lambda_12A0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12A0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この先は開発中の区画となります。\x01",
            "立ち入りはご遠慮ください。\x01",
            "　　　　──ミシュラム開発事業部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_0D()

    #C0037
    ChrTalk(
        0x103,
        (
            "#0200F#6P……どうやらこの先は\x01",
            "まだ開発中みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        (
            "#0103F#5Pええ、ミシュラムの開発計画は\x01",
            "まだ途中みたいだから……\x02\x03",

            "#0100F今後、こちらの方にも\x01",
            "何か造られるのかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#0306F#5Pやれやれ、豪勢なこった。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#0000F#6Pともかく、今は用はなさそうだ。\x01",
            "他を回ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 25630, 0, 8109, 270)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xA4, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A5")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_14A5")

    EventEnd(0x5)
    Return()

    # Function_14_10DE end

    def Function_15_14A8(): pass

    label("Function_15_14A8")

    EventBegin(0x0)
    Fade(1000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_68(-50, 1100, 8000, 0)
    MoveCamera(335, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20090, 0)
    SetCameraDistance(18590, 2000)
    SetChrPos(0x101, 0, 0, 9300, 180)
    SetChrPos(0x102, 0, 0, 6700, 0)
    SetChrPos(0x103, 1200, 0, 8000, 270)
    SetChrPos(0x104, -1200, 0, 8000, 90)
    OP_6F(0x10)
    OP_0D()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0003F#11P一通り回ってみたけど……\x02\x03",

            "#0001Fやっぱりオークション会場に入る\x01",
            "手立てを考える必要がありそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#0301F#5P確かに、チェックしてるのが\x01",
            "あのマフィアどもみたいだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#0205F#12Pそもそも、その招待カードは\x01",
            "そのまま使えるんでしょうか？\x02\x03",

            "#0201F身元を照合される可能性が\x01",
            "高そうな気もしますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#0103F#6P……確かにそうね。\x02\x03",

            "#0108Fその辺り、レンちゃんから話を\x01",
            "聞ければよかったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#0000F#11Pまあ、招待カードを\x01",
            "譲ってくれただけでも\x01",
            "ありがたいと思っておこう。\x02\x03",

            "#0006Fいずれにしても……\x01",
            "どこか落ち着ける場所が欲しいな。\x02\x03",

            "#0008Fレストランは……\x01",
            "ちょっと人目がありすぎるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#0200F#12Pなら、上のホテルに\x01",
            "空室はないんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#0106F#6Pうーん、この時期だから\x01",
            "さすがに満室だと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0300F#5Pま、ひょっとしたら\x01",
            "キャンセル空きがあるかもしれねぇ。\x02\x03",

            "フロントで聞くだけ聞いてみようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#0000F#11Pそうだな、行ってみよう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 400, 0, 7770, 0)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    SetScenarioFlags(0xA4, 4)
    OP_29(0x47, 0x1, 0x3)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_15_14A8 end

    def Function_16_18D5(): pass

    label("Function_16_18D5")

    EventBegin(0x0)
    Fade(1000)
    OP_68(19000, 1000, 10600, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 19000, 0, 10600, 0)
    SetChrPos(0x102, 18350, 0, 9300, 0)
    SetChrPos(0x103, 19650, 0, 9300, 0)
    SetChrPos(0x104, 18350, 0, 8000, 0)
    SetChrPos(0x151, 19650, 0, 8000, 0)
    SetCameraDistance(19500, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0003F#5P（……ドレスアップしたら\x01",
            "  もう周辺の聞き込みは出来ないな。）\x02\x03",

            "#0001F（誰を連れて行くかも決める必要があるし、\x01",
            "  どうしようか……？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【周辺で聞き込みを続ける】\x01",            # 0
            "【ブティックでドレスアップする】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A74"),
        (1, "loc_1A8C"),
        (SWITCH_DEFAULT, "loc_1B0F"),
    )


    label("loc_1A74")

    SetChrPos(0x0, 19000, 0, 9300, 180)
    EventEnd(0x5)
    Jump("loc_1B0F")

    label("loc_1A8C")

    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_68(19000, 1000, 11600, 5000)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(300)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x103, 3, 0, 17)
    Sleep(300)
    BeginChrThread(0x104, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x151, 3, 0, 17)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x151, 0x3)
    NewScene("t1040", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B0F")

    label("loc_1B0F")

    Return()

    # Function_16_18D5 end

    def Function_17_1B10(): pass

    label("Function_17_1B10")

    OP_95(0xFE, 19000, 0, 10600, 2000, 0x1)

    def lambda_1B29():
        OP_95(0xFE, 19000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B29)
    Sleep(400)

    def lambda_1B46():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B46)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_1B10 end

    def Function_18_1B5B(): pass

    label("Function_18_1B5B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この先は開発中の区画となります。\x01",
            "立ち入りはご遠慮ください。\x01",
            "　　　　──ミシュラム開発事業部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_1B5B end

    SaveToFile()

Try(main)
