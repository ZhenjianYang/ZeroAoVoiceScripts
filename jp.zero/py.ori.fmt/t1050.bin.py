from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1050.bin",                # FileName
        "t1050",                    # MapName
        "t1050",                    # Location
        0x0043,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 67, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1050",                  # 0
        "ハガー支配人",           # 1
        "ロッチー",               # 2
        "シトラス",               # 3
        "観光客",                 # 4
        "観光客",                 # 5
        "ワジ",                   # 6
        "トマ",                   # 7
        "アルビナ",               # 8
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25600.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch20400.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch20200.itc",                   # 05
        "chr/ch20300.itc",                   # 06
        "chr/ch08000.itc",                   # 07
    ))

    DeclNpc(-479,    0,       10050,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-100709, 0,       8859,    270,  257,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-101819, 0,       8859,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(8970,    0,       6630,    225,  385,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(8250,    0,       5920,    45,   385,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   7,   0,   0,   3,   255, 255, 255,  0)
    DeclNpc(96220,   0,       121949,  270,  261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(103230,  0,       124330,  0,    261,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(-20,     0,       8270,    1500,    -480,    1500,    10050,   0x007E, 0,  7,  0x0000)
    DeclActor(5500,    0,       13500,   1200,    5500,    1500,    13500,   0x007C, 0,  28, 0x0000)
    DeclActor(-99830,  0,       13590,   1200,    -99830,  1500,    13590,   0x007C, 0,  29, 0x0000)
    DeclActor(-96600,  0,       120560,  1500,    -96600,  1000,    120560,  0x007C, 0,  6,  0x0000)

    ScpFunction((
        "Function_0_29C",          # 00, 0
        "Function_1_354",          # 01, 1
        "Function_2_3B5",          # 02, 2
        "Function_3_416",          # 03, 3
        "Function_4_495",          # 04, 4
        "Function_5_549",          # 05, 5
        "Function_6_583",          # 06, 6
        "Function_7_628",          # 07, 7
        "Function_8_62C",          # 08, 8
        "Function_9_98E",          # 09, 9
        "Function_10_BF6",         # 0A, 10
        "Function_11_D57",         # 0B, 11
        "Function_12_E3B",         # 0C, 12
        "Function_13_1386",        # 0D, 13
        "Function_14_1627",        # 0E, 14
        "Function_15_16B4",        # 0F, 15
        "Function_16_16F5",        # 10, 16
        "Function_17_1F9D",        # 11, 17
        "Function_18_1FB2",        # 12, 18
        "Function_19_2035",        # 13, 19
        "Function_20_39D5",        # 14, 20
        "Function_21_3A1A",        # 15, 21
        "Function_22_3A7D",        # 16, 22
        "Function_23_3AE0",        # 17, 23
        "Function_24_3B25",        # 18, 24
        "Function_25_3B6A",        # 19, 25
        "Function_26_45EC",        # 1A, 26
        "Function_27_56A3",        # 1B, 27
        "Function_28_5D6A",        # 1C, 28
        "Function_29_5E05",        # 1D, 29
    ))


    def Function_0_29C(): pass

    label("Function_0_29C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2DC"),
        (1, "loc_2E8"),
        (2, "loc_2F4"),
        (3, "loc_300"),
        (4, "loc_30C"),
        (5, "loc_318"),
        (6, "loc_324"),
        (SWITCH_DEFAULT, "loc_330"),
    )


    label("loc_2DC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_2E8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_2F4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_300")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_30C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_318")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_324")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_330")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_33C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_353")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_33C")

    label("loc_353")

    Return()

    # Function_0_29C end

    def Function_1_354(): pass

    label("Function_1_354")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B4")
    OP_95(0xFE, -106030, 0, 8260, 2000, 0x0)
    OP_95(0xFE, -106030, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 8260, 2000, 0x0)
    Jump("Function_1_354")

    label("loc_3B4")

    Return()

    # Function_1_354 end

    def Function_2_3B5(): pass

    label("Function_2_3B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_415")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_2_3B5")

    label("loc_415")

    Return()

    # Function_2_3B5 end

    def Function_3_416(): pass

    label("Function_3_416")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_494")
    SetScenarioFlags(0xAA, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0xA)
    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -100040, 0, 13630, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(890, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)

    label("loc_494")

    Return()

    # Function_3_416 end

    def Function_4_495(): pass

    label("Function_4_495")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AF")
    Event(0, 19)

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4BD")
    Jump("loc_548")

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4CB")
    Jump("loc_548")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_4D9")
    Jump("loc_548")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4E7")
    Jump("loc_548")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_4F5")
    Jump("loc_548")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_531")
    SetChrPos(0x9, -93960, 0, 8260, 0)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 94190, 0, 11580, 0)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_548")

    label("loc_531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_53F")
    Jump("loc_548")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_548")

    label("loc_548")

    Return()

    # Function_4_495 end

    def Function_5_549(): pass

    label("Function_5_549")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56B")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_582")
    EndChrThread(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    label("loc_582")

    Return()

    # Function_5_549 end

    def Function_6_583(): pass

    label("Function_6_583")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60A")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_60A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_626")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_626")

    Return()

    # Function_6_583 end

    def Function_7_628(): pass

    label("Function_7_628")

    Call(0, 8)
    Return()

    # Function_7_628 end

    def Function_8_62C(): pass

    label("Function_8_62C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_642")
    Call(0, 16)
    Jump("loc_98D")

    label("loc_642")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_653")
    Jump("loc_98A")

    label("loc_653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_661")
    Jump("loc_98A")

    label("loc_661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_66F")
    Jump("loc_98A")

    label("loc_66F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_67D")
    Jump("loc_98A")

    label("loc_67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_68B")
    Jump("loc_98A")

    label("loc_68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_7CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_768")
    TurnDirection(0x8, 0x151, 0)

    #C0001
    ChrTalk(
        0x8,
        "ワジ様、お出かけでしょうか？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "でしたらその間、\x01",
            "ベッドメイクを\x01",
            "させていただきますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x151,
        (
            "#5700Fそうだね、少し時間がかかると思うし……\x01",
            "じゃあよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "承知しました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7C6")

    label("loc_768")


    #C0005
    ChrTalk(
        0x8,
        (
            "それでは、\x01",
            "お出かけの間にベッドメイクを\x01",
            "させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        "いってらっしゃいませ。\x02",
    )

    CloseMessageWindow()

    label("loc_7C6")

    Jump("loc_98A")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_83A")

    #C0007
    ChrTalk(
        0x8,
        "お客様はワジ様のお知り合いでしたか。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "ワジ様の部屋は左の扉を入って\x01",
            "右手でございますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98A")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_981")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_905")

    #C0009
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "ホテル・デルフィニアへようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "本日は実に多くのお客様に\x01",
            "ご利用頂いております。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "部屋にいないお客様は\x01",
            "各々観光を楽しんでおられる\x01",
            "ようですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_97C")

    label("loc_905")


    #C0012
    ChrTalk(
        0x8,
        (
            "本日は実に多くのお客様に\x01",
            "ご利用頂いております。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "部屋にいないお客様は\x01",
            "各々観光を楽しんでおられる\x01",
            "ようですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97C")

    Jump("loc_98A")

    label("loc_981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_98A")

    label("loc_98A")

    TalkEnd(0x8)

    label("loc_98D")

    Return()

    # Function_8_62C end

    def Function_9_98E(): pass

    label("Function_9_98E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_99F")
    Jump("loc_BF2")

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_9AD")
    Jump("loc_BF2")

    label("loc_9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_9BB")
    Jump("loc_BF2")

    label("loc_9BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_9C9")
    Jump("loc_BF2")

    label("loc_9C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_9D7")
    Jump("loc_BF2")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_AF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9F")
    TurnDirection(0xFE, 0x151, 0)

    #C0014
    ChrTalk(
        0xFE,
        (
            "あっ、お客様…………\x01",
            "………………\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x151,
        "#5705F……ん？　僕に何か用かい？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "（はぁあ……やっぱり\x01",
            "  綺麗な顔してるわ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x151,
        "#5702F……ふふ、おかしな子だね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_AF0")

    label("loc_A9F")


    #C0018
    ChrTalk(
        0xFE,
        "あっ……お出かけですか？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "気をつけて行ってらっしゃいませ。\x01",
            "おほほほ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF0")

    Jump("loc_BF2")

    label("loc_AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_B65")
    TurnDirection(0xFE, 0xA, 0)
    OP_4B(0xA, 0xFF)

    #C0020
    ChrTalk(
        0xFE,
        (
            "キャー、どうしましょ！\x01",
            "お顔を拝見しちゃった！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        "いいから落ち着きなさいっ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_BF2")

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_BE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B80")
    Call(0, 11)
    Jump("loc_BE4")

    label("loc_B80")


    #C0022
    ChrTalk(
        0xFE,
        (
            "チェックインだけ済ませて\x01",
            "どこかへ行っちゃったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "さっきのお客様、\x01",
            "かわいかったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE4")

    Jump("loc_BF2")

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BF2")

    label("loc_BF2")

    TalkEnd(0xFE)
    Return()

    # Function_9_98E end

    def Function_10_BF6(): pass

    label("Function_10_BF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_C07")
    Jump("loc_D53")

    label("loc_C07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_C15")
    Jump("loc_D53")

    label("loc_C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_C23")
    Jump("loc_D53")

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_C31")
    Jump("loc_D53")

    label("loc_C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_C3F")
    Jump("loc_D53")

    label("loc_C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_CAA")

    #C0024
    ChrTalk(
        0xFE,
        (
            "何かお困りでしたら\x01",
            "遠慮なくお申し付けください。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "誠心誠意尽くさせていただきますわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D53")

    label("loc_CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_CEB")

    #C0026
    ChrTalk(
        0xFE,
        (
            "もう、この子ったら\x01",
            "お客様の前ではしたない……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D53")

    label("loc_CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_D4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D06")
    Call(0, 11)
    Jump("loc_D45")

    label("loc_D06")


    #C0027
    ChrTalk(
        0xFE,
        (
            "ほらほら、そんな暇があったら\x01",
            "さっさと廊下の掃除をするっ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D45")

    Jump("loc_D53")

    label("loc_D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D53")

    label("loc_D53")

    TalkEnd(0xFE)
    Return()

    # Function_10_BF6 end

    def Function_11_D57(): pass

    label("Function_11_D57")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)

    #C0028
    ChrTalk(
        0x9,
        (
            "ねぇ、見た？\x01",
            "さっきのお客様……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "すっごくカワイイ顔してたけど\x01",
            "あれって男の子よね？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        (
            "まーたあんたは……\x01",
            "そんなこと言ってないで\x01",
            "さっさと掃除済ませるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        "あ～ん、気になるぅ……\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_D57 end

    def Function_12_E3B(): pass

    label("Function_12_E3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1180")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_F12")

    #C0032
    ChrTalk(
        0xFE,
        (
            "これで、予定していた\x01",
            "花火の中でのプロポーズ、\x01",
            "決行することができそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "ありがとう、君たちには\x01",
            "どれだけ礼をしても足りないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "さぁ……夜に向けて\x01",
            "心の準備を始めないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117B")

    label("loc_F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_10D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1054")

    #C0035
    ChrTalk(
        0xFE,
        (
            "さ、さぁ……今から\x01",
            "テーマパークに向かうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "キチンと計画したとはいえ、\x01",
            "ちゃんとプロポーズできるかな。\x01",
            "なんだか緊張してきた……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "い、いや……せっかく君たちに\x01",
            "指輪を見つけてもらったんだ。\x01",
            "弱気になっちゃいけないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "とにかく、\x01",
            "脳内シミュレーションだけは\x01",
            "繰り返しやっておこう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_10D1")

    label("loc_1054")


    #C0039
    ChrTalk(
        0xFE,
        (
            "結婚してください！\x01",
            "……うん。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "結婚しよう！\x01",
            "……これもいいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "結婚しやがれこんにゃろう！\x01",
            "……これはナシだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D1")

    Jump("loc_117B")

    label("loc_10D6")


    #C0042
    ChrTalk(
        0xFE,
        (
            "さぁ……夜に向けて\x01",
            "心の準備を始めないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "アルビナがプロポーズに\x01",
            "ＯＫしてくれるか否かで……\x01",
            "僕の生死も決まる気がする……！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0006Fそれは言い過ぎ……\x02",
    )

    CloseMessageWindow()

    label("loc_117B")

    Jump("loc_1382")

    label("loc_1180")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_1195")
    Call(0, 27)
    Jump("loc_1382")

    label("loc_1195")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_1237")

    #C0045
    ChrTalk(
        0xFE,
        (
            "と、とにかく、君たち！\x01",
            "一度高級住宅街の方を\x01",
            "見に行ってくれないか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "もしかしたら、指輪はまだ\x01",
            "あのベンチのあたりに\x01",
            "落ちてるかも……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1382")

    label("loc_1237")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1255")
    Call(0, 26)
    Jump("loc_1382")

    label("loc_1255")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1273")
    Call(0, 26)
    Jump("loc_1382")

    label("loc_1273")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1291")
    Call(0, 26)
    Jump("loc_1382")

    label("loc_1291")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_137F")

    #C0047
    ChrTalk(
        0xFE,
        (
            "どこで指輪を落としたか\x01",
            "まったく身に覚えが無いんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "ただ言えるのは……\x01",
            "僕とアルビナはここに着いてから\x01",
            "一通りの場所を回ったというだけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "と、とにかく……\x01",
            "それらしいものを拾ったら\x01",
            "片っ端から見せに来てくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1382")

    label("loc_137F")

    Call(0, 25)

    label("loc_1382")

    TalkEnd(0xFE)
    Return()

    # Function_12_E3B end

    def Function_13_1386(): pass

    label("Function_13_1386")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_14F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_13EC")

    #C0050
    ChrTalk(
        0xFE,
        "トマ、なんだか嬉しそうね。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "なにかいいことでも\x01",
            "あったのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EE")

    label("loc_13EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1468")

    #C0052
    ChrTalk(
        0xFE,
        (
            "トマ、テーマパークで\x01",
            "何かしてくれるつもりみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "ふふ、彼ってすぐ顔に出るから\x01",
            "分かりやすいのよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EE")

    label("loc_1468")


    #C0054
    ChrTalk(
        0xFE,
        (
            "なんでトマと\x01",
            "付き合ってるのかって\x01",
            "よく言われるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "トマって見てると\x01",
            "なんだかおかしいじゃない？\x01",
            "そこが魅力的なのよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EE")

    Jump("loc_1623")

    label("loc_14F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_1580")

    #C0056
    ChrTalk(
        0xFE,
        (
            "トマったら……\x01",
            "落ち込んだり大声出したり、\x01",
            "今日はなんだか変よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "まぁ、いっか。\x01",
            "トマも何でもないって言ってるし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1623")

    label("loc_1580")


    #C0058
    ChrTalk(
        0xFE,
        (
            "今晩、トマと２人で\x01",
            "テーマパークの夜の部に行くのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "なんでも、沢山の花火が上がって\x01",
            "すっごくロマンチックな夜を\x01",
            "過ごせるんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "ふふ、楽しみね。\x02",
    )

    CloseMessageWindow()

    label("loc_1623")

    TalkEnd(0xFE)
    Return()

    # Function_13_1386 end

    def Function_14_1627(): pass

    label("Function_14_1627")

    TalkBegin(0xFE)

    #C0061
    ChrTalk(
        0xFE,
        (
            "日も落ちてきたし、\x01",
            "今日は妻と休んでいることにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "部屋からテーマパークの花火を肴に\x01",
            "ワインを飲むというのもオツだろう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1627 end

    def Function_15_16B4(): pass

    label("Function_15_16B4")

    TalkBegin(0xFE)

    #C0063
    ChrTalk(
        0xFE,
        (
            "ホテルの予約、\x01",
            "事前にとっておいて\x01",
            "本当によかったわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_16B4 end

    def Function_16_16F5(): pass

    label("Function_16_16F5")

    EventBegin(0x0)
    Fade(1000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -16950, 0, 11920, 45)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xD, 0x8000)
    OP_68(-240, 1100, 7180, 0)
    MoveCamera(327, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16470, 0)
    SetChrPos(0x101, -500, 0, 6400, 0)
    SetChrPos(0x102, 500, 0, 6400, 0)
    SetChrPos(0x103, 500, 0, 5000, 0)
    SetChrPos(0x104, -500, 0, 5000, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05700.itp")
    OP_0D()

    #C0064
    ChrTalk(
        0x8,
        (
            "#11Pいらっしゃいませ。\x01",
            "ホテル・デルフィニアへようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "#11Pひょっとして……\x01",
            "当ホテルのご利用でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#0100F#6Pええ、そうなんですけど、\x01",
            "やはり満室でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        "#11P大変申し訳ありません。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "#11P実は先ほど、\x01",
            "一件キャンセルがあったのですが\x01",
            "すぐに予約が入ってしまいまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#0106F#6Pそうですか……\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x103,
        "#0206F#6P……惜しかったです。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0306F#6P仕方ねぇから、\x01",
            "レストランあたりに行こうぜ。\x02\x03",

            "#0300F話をするくらいは出来るだろ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1998():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1998)
    Sleep(50)

    def lambda_19A8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19A8)
    Sleep(300)

    #C0072
    ChrTalk(
        0x101,
        "#0006F#11Pそうだな……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1437, 255, 100, 0)    #voice#Lazy
    Sleep(700)

    #N0073
    NpcTalk(
        0xD,
        "涼しげな声",
        (
            "#4P#17Aフフッ……\x01",
            "お困りみたいだね。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-1880, 1100, 6720, 5100)
    MoveCamera(307, 16, 0, 5100)

    def lambda_1A7C():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A7C)

    def lambda_1A89():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A89)
    Sleep(50)

    def lambda_1A99():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A99)

    def lambda_1AA6():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1AA6)
    Sleep(50)

    def lambda_1AB6():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1AB6)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0xA)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0xD, 3, 0, 17)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x8, 1)
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

    #C0074
    ChrTalk(
        0x101,
        "#0005F#12Pへ……？\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        "#0105F#12Pワ、ワジ君……？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        "#2Pこれはワジ様……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    #Sound(1435, 255, 100, 0)    #voice#Lazy
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(700)

    #A0077
    AnonymousTalk(
        0xD,
        (
            "何だか部屋が取れなくて\x01",
            "困っているみたいだけど……\x02\x03",

            "ゆっくり話ができる場所が\x01",
            "欲しいってところかな？\x02",
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

    #C0078
    ChrTalk(
        0x101,
        (
            "#0000F#12Pあ、ああ。\x01",
            "そうなんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xD,
        (
            "#5704F#5P#Nだったら話は早い。\x02\x03",

            "僕の部屋を提供してあげるよ。\x02",
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

    #C0080
    ChrTalk(
        0x101,
        "#0011F#12Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        "#0305F#6Pおいおい、いきなりだな。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xD,
        "#5702F#5P#Nフフ、こっちだよ。\x02",
    )

    CloseMessageWindow()
    OP_68(-3940, 1200, 6960, 5000)
    BeginChrThread(0xD, 3, 0, 18)
    WaitChrThread(0xD, 3)
    OP_6F(0x1)
    OP_68(-1350, 1100, 6510, 1200)

    def lambda_1E09():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E09)

    def lambda_1E16():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E16)
    Sleep(100)

    def lambda_1E26():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E26)

    def lambda_1E33():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E33)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0083
    ChrTalk(
        0x102,
        "#0101F#12Pど、どうするの……？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#0211F#6Pあからさまに怪しげな\x01",
            "格好をしてましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#0301F#6Pつうかどうして、\x01",
            "不良グループのリーダーが\x01",
            "こんな場所にいるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#0006F#5Pま、まあ、\x01",
            "知らない相手じゃないし……\x02\x03",

            "#0000Fとにかく行ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 40, 0, 6580, 270)
    SetChrPos(0x8, -480, 0, 10050, 180)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 0, 0, 0, 0)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0xA4, 5)
    OP_29(0x47, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_16_16F5 end

    def Function_17_1F9D(): pass

    label("Function_17_1F9D")

    OP_95(0xFE, -4000, 0, 8400, 3000, 0x0)
    Return()

    # Function_17_1F9D end

    def Function_18_1FB2(): pass

    label("Function_18_1FB2")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_96(0xFE, 0xFFFFC037, 0x0, 0x2EEA, 0x9C4, 0x0)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_79(0x5)

    def lambda_1FED():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1FED)
    Sleep(200)

    def lambda_2005():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2005)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)
    Sound(890, 0, 100, 0)
    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    Return()

    # Function_18_1FB2 end

    def Function_19_2035(): pass

    label("Function_19_2035")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50353.itc", 0x1E)
    OP_68(-99800, 1100, 124250, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xD, -102200, 150, 124000, 90)
    SetChrPos(0x101, -101400, 0, 121700, 0)
    SetChrPos(0x102, -100300, 0, 121700, 315)
    SetChrPos(0x103, -100300, 0, 120400, 315)
    SetChrPos(0x104, -101400, 0, 120400, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis063.itp")
    FadeToBright(1000, 0)
    OP_68(-101070, 1100, 122980, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0087
    ChrTalk(
        0xD,
        (
            "#5709F#11Pフフ、しかし君たちも\x01",
            "なかなか優雅じゃないか。\x02\x03",

            "#5702F記念祭の最終日に休みをもらって\x01",
            "ミシュラムで豪遊とはねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#0012F#6Pあー……\x01",
            "まあ、骨休みって所さ。\x02\x03",

            "#0001Fそれより、ワジ。\x01",
            "君のその格好は……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xD,
        (
            "#5704F#11Pフフ、イカスだろう？\x02\x03",

            "#5700F僕の副業の\x01",
            "制服みたいなもんさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#0005F#6Pふ、副業……？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#0101F#6Pそれってどういう……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xD,
        (
            "#5703F#11P上流階級という冷たい世界で\x01",
            "愛を見失ってしまった\x01",
            "麗しくも寂しいご婦人たち……\x02\x03",

            "#5702Fそんな彼女たちに\x01",
            "一時の夢を見せてあげる仕事さ。\x02",
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

    #C0093
    ChrTalk(
        0x101,
        "#0011F#6Pなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        "#0105F#6Pそ、それってもしかして……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x103,
        "#0211F#6Pいわゆる『ホスト』さんですか。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        (
            "#0307F#6Pおいおい！\x01",
            "なんてうらやましい──\x01",
            "もとい、ケシカランことを！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xD,
        (
            "#5702F#11Pフフ、別にミラに困って\x01",
            "やってるわけじゃないけどね。\x02\x03",

            "いつもしつこく誘われるから\x01",
            "仕方なく付き合ってあげてるんだ。\x02\x03",

            "#5709Fまあ、慈善事業ってやつ？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#0006F#6Pなんて言い草だ……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#0306F#6Pそういうすげない所に\x01",
            "コロッといっちまうマダムが\x01",
            "多いってことかよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#0103F#6Pはあ……\x01",
            "正直、感心はできないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#0200F#6Pそれではワジさんは\x01",
            "ホストのお仕事でここに？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xD,
        (
            "#5702F#11Pああ、いわゆる\x01",
            "エスコート役ってやつさ。\x02\x03",

            "とあるご婦人に同伴して\x01",
            "ちょっとワケありのパーティに\x01",
            "出るつもりなんだけどね。\x02",
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

    #C0103
    ChrTalk(
        0x101,
        "#0005F#6Pえ……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        "#0101F#6Pそれって……\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    #Sound(1436, 255, 90, 0)    #voice#Lazy
    Sleep(1000)

    #C0105
    ChrTalk(
        0xD,
        "#5704F#11Pふふ……成程ね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0106
    ChrTalk(
        0x101,
        (
            "#0012F#6P成程って……\x01",
            "その、なんの話だ？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xD,
        (
            "#5702F#11P《黒の競売会#10Rシュバルツオークション#》……\x02\x03",

            "#5702F大方、その名前を知って\x01",
            "調べに来たって所だろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#0001F#6Pっ……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        (
            "#0306F#6Pはあ……\x01",
            "バレバレみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x102,
        (
            "#0101F#6Pという事は、あなたが出る\x01",
            "訳ありのパーティーというのも……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xD,
        (
            "#5700F#11Pああ、その競売会さ。\x02\x03",

            "#5704F去年も別のマダムの付き添いで\x01",
            "行ったから、２回目になるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#0006F#6Pそうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        (
            "#0206F#6Pこんな身近に知っている人がいたとは\x01",
            "思いませんでしたね……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xD,
        (
            "#5705F#11Pでも君たち、その競売会を\x01",
            "摘発するつもりなのかい？\x02\x03",

            "さすがに無茶だと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#0006F#6Pいや……悔しいけど\x01",
            "元より摘発するつもりはないさ。\x02\x03",

            "#0008Fただ、知っておきたかったんだ。\x02\x03",

            "クロスベルの歪みを象徴したような\x01",
            "豪華絢爛な裏の社交パーティー……\x02\x03",

            "#0013F俺たちが乗り越えるべき《壁》が\x01",
            "どの程度のものであるのかを。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#0105F#6Pロイド……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xD,
        (
            "#5702F#11Pフフ……なるほどね。\x02\x03",

            "#5704Fその意気込みは買うけど\x01",
            "あいにく《競売会》には\x01",
            "招待カードがないと入れないよ。\x02\x03",

            "毎年、違った薔薇のデザインで\x01",
            "通しナンバーも入っているから\x01",
            "偽造することも難しい……\x02\x03",

            "#5702Fどうしようもないと思うけどねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0000F#6Pそれなんだけど……\x01",
            "実は、カードは持っているんだ。\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)

    #A0119
    AnonymousTalk(
        0xD,
        (
            "#5705Fへえ……\x02\x03",

            "#5709Fどうやって手に入れたかを\x01",
            "聞くのは野暮ってもんかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0120
    AnonymousTalk(
        0x101,
        "#0004Fああ、事情があってね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #C0121
    ChrTalk(
        0x102,
        (
            "#0108F#6Pこの招待カードだけど……\x01",
            "身元の特定はされないのかしら？\x02\x03",

            "#0101F会員限定で、登録されている人しか\x01",
            "入ることはできないとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xD,
        (
            "#5705F#11Pいや、それはないと思うよ。\x02\x03",

            "#5704F裏の社交界的な側面があるから\x01",
            "新規の客を歓迎してるみたいなんだ。\x02\x03",

            "#5702F盗品を扱っている以上、\x01",
            "あえて身元を特定されたくない\x01",
            "有力者も多いみたいだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        (
            "#0300F#6Pふむ、だったら\x01",
            "何とかなるかもしれねぇな。\x02\x03",

            "#0305Fそういや、１枚の招待カードで\x01",
            "何人まで入れるもんなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xD,
        (
            "#5703F#11P特に決まりはないみたいだけど……\x01",
            "ただまあ、大抵は２人連れだね。\x02\x03",

            "#5700F４人連れで入るのは\x01",
            "目立つからお勧めはできないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x103,
        "#0201F#6Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#0106F#6P……確かにそれは\x01",
            "言えてるかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "#5704F#11Pそれと、一応パーティーだから\x01",
            "フォーマルな格好をした方がいいね。\x02\x03",

            "#5702Fま、僕みたいな格好をして\x01",
            "悪目立ちするってのもアリだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#0006F#6Pさすがにそれは遠慮しとくよ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    #C0129
    ChrTalk(
        0x101,
        (
            "#0001F#5P──なあ、エリィ。\x02\x03",

            "パーティー向けの服装だけど\x01",
            "どこかで調達できる場所はないかな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(150)

    #C0130
    ChrTalk(
        0x102,
        (
            "#0102F#12Pそれなら、下のブティックが\x01",
            "丁度いいと思うわ。\x02\x03",

            "前に来た時に使った事があるし、\x01",
            "私が立て替えておくから。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        "#0011F#5Pいや、それは……\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        (
            "#0104F#12Pそのくらいさせて頂戴。\x02\x03",

            "#0100Fそれより問題は、\x01",
            "潜入するメンバーでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#0006F#5Pああ……そうだな。\x02\x03",

            "#0008Fクジ引きかジャンケンで\x01",
            "決めるってのもアレだしな……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#0306F#6Pおいおい、何言ってんだ。\x02\x03",

            "#0300F少なくともお前は確定だろうが。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#0005F#5Pえっ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    #C0136
    ChrTalk(
        0x103,
        (
            "#0204F#6P今回の件、一番拘っていたのは\x01",
            "ロイドさんですし……\x02\x03",

            "#0202Fわたしたちのリーダーですから\x01",
            "行くのは当然ではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#0005F#5Pで、でも……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        (
            "#0103F#12Pもう、ここは素直に\x01",
            "引き受けておきなさい。\x02\x03",

            "#0102F見てみたいんでしょう？\x01",
            "クロスベルの“歪み”の実態を。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0139
    ChrTalk(
        0x101,
        (
            "#0004F#5P──分かった。\x01",
            "引き受けさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xD,
        (
            "#5704F#11Pフフ、だったらもう一人、\x01",
            "同伴する人間を決めるといい。\x02\x03",

            "#5702F一人で参加するっていうのは\x01",
            "かえって目立つだろうからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#0006F#5Pそうだな……うーん。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#0103F#12P私か、ティオちゃんか、ランディ。\x02\x03",

            "#0100Fマフィアがいる事を踏まえて\x01",
            "選んだ方がいいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        (
            "#0204F#6P残る２人は、会場の外で\x01",
            "いざという時に備えて待機する。\x02\x03",

            "#0202Fそんな役割分担でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        (
            "#0302F#6Pま、どんな分担にするにしても\x01",
            "まずは下のブティックに行こうぜ。\x02\x03",

            "ドレスアップする時までに\x01",
            "誰を連れていくか決めとけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            "#0000F#5P……ああ。\x01",
            "そうさせてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17500, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetChrChipByIndex(0xD, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    AddParty(0x50, 0xFF, 0xFF)
    OP_68(-100000, 1250, 12500, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18600, 0)
    SetChrPos(0x101, -100030, 0, 14990, 180)
    SetChrPos(0x102, -100030, 0, 14990, 180)
    SetChrPos(0x103, -100030, 0, 14990, 180)
    SetChrPos(0x104, -100030, 0, 14990, 180)
    SetChrPos(0x151, -100030, 0, 14990, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(17600, 2500)
    OP_6F(0x10)
    OP_0D()
    Sound(121, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)
    OP_68(-100000, 1250, 10500, 4000)
    BeginChrThread(0x101, 3, 0, 20)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 22)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 23)
    Sleep(1000)
    BeginChrThread(0x151, 3, 0, 24)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x151, 3)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sleep(100)
    Sound(890, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    OP_6F(0x1)
    TurnDirection(0x101, 0x151, 400)

    #C0146
    ChrTalk(
        0x101,
        (
            "#0011F#6P──ちょっと待て。\x02\x03",

            "#0001Fどうしてワジまで\x01",
            "一緒に付いてくるんだ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37D8():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37D8)
    Sleep(100)

    def lambda_37E8():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_37E8)

    def lambda_37F5():
        TurnDirection(0xFE, 0x151, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_37F5)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0147
    ChrTalk(
        0x151,
        (
            "#5709F#11Pフフ、せっかくだから\x01",
            "コーディネイトの指南でも\x01",
            "してあげようと思ってね。\x02\x03",

            "#5702Fマフィアのチェックを\x01",
            "誤魔化すコツを教えてあげるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#0006F#6Pうーん……\x01",
            "まあ、そういう事なら。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x103,
        (
            "#0211F#6P何かあからさまに\x01",
            "興味本位っぽいですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        "#0302F#5Pま、聞くだけ聞いてみようぜ。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        (
            "#0100F#5Pそれじゃあ下にある\x01",
            "ブティックに行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -99720, 0, 10000, 90)
    SetScenarioFlags(0xA4, 6)
    OP_29(0x47, 0x1, 0x5)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -93960, 0, 8260, 0)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 94190, 0, 11580, 0)
    BeginChrThread(0xA, 0, 0, 2)
    EventEnd(0x5)
    Return()

    # Function_19_2035 end

    def Function_20_39D5(): pass

    label("Function_20_39D5")


    def lambda_39DA():
        OP_95(0xFE, -100000, 0, 9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39DA)

    def lambda_39F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39F4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3A0D():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A0D)
    WaitChrThread(0x101, 1)
    Return()

    # Function_20_39D5 end

    def Function_21_3A1A(): pass

    label("Function_21_3A1A")


    def lambda_3A1F():
        OP_95(0xFE, -100000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A1F)

    def lambda_3A39():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A39)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3A52():
        OP_95(0xFE, -101200, 0, 10800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A52)
    WaitChrThread(0xFE, 1)

    def lambda_3A70():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A70)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_3A1A end

    def Function_22_3A7D(): pass

    label("Function_22_3A7D")


    def lambda_3A82():
        OP_95(0xFE, -100000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A82)

    def lambda_3A9C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A9C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3AB5():
        OP_95(0xFE, -98800, 0, 10200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AB5)
    WaitChrThread(0xFE, 1)

    def lambda_3AD3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AD3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_3A7D end

    def Function_23_3AE0(): pass

    label("Function_23_3AE0")


    def lambda_3AE5():
        OP_95(0xFE, -100000, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AE5)

    def lambda_3AFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3AFF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3B18():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B18)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_3AE0 end

    def Function_24_3B25(): pass

    label("Function_24_3B25")


    def lambda_3B2A():
        OP_95(0xFE, -98610, 0, 11590, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B2A)

    def lambda_3B44():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B44)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3B5D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B5D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_3B25 end

    def Function_25_3B6A(): pass

    label("Function_25_3B6A")

    EventBegin(0x0)
    Fade(500)
    OP_68(97820, 900, 122220, 0)
    MoveCamera(313, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20810, 0)
    SetChrPos(0x101, 98200, 0, 121000, 270)
    SetChrPos(0x102, 98200, 0, 122200, 270)
    SetChrPos(0x103, 99400, 0, 121000, 270)
    SetChrPos(0x104, 99400, 0, 122200, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_3BFD")
    SetChrPos(0x151, 100600, 0, 121600, 270)

    label("loc_3BFD")

    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0x10E, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_4B(0xF, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_0D()

    #C0152
    ChrTalk(
        0xE,
        (
            "#5P何でなんだよ……\x01",
            "僕が何したって言うんだよ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0x5A, 0x1F4)

    #C0153
    ChrTalk(
        0xE,
        (
            "#5P君たち……\x01",
            "このミシュラム保養地で\x01",
            "なにか拾わなかった？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xE,
        (
            "#5Pなんていうか、その……\x01",
            "婚約指輪的な輪っかとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        (
            "#12P#0005Fいえ、何も拾ってませんが……\x02\x03",

            "#0001F……婚約指輪を\x01",
            "落としちゃったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xE,
        "#5P#5Sわー、声がデカい！\x02",
    )

    CloseMessageWindow()
    OP_68(99540, 1200, 123070, 2000)
    OP_6F(0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0x10E, 0x1F4)

    #C0157
    ChrTalk(
        0xF,
        (
            "#12Pトマ？　どうしたの、\x01",
            "そんな大きな声を出して。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0158
    ChrTalk(
        0xE,
        (
            "#5Pえ、あ、や……\x01",
            "な、なんでもないよ、\x01",
            "アルビナ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xF,
        (
            "#12P……そう？\x01",
            "ふふっ、おかしなトマ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x1F4)
    OP_68(97820, 900, 122220, 2000)
    OP_6F(0x1)

    #C0160
    ChrTalk(
        0xE,
        (
            "#5P……ア、 アルビナに\x01",
            "バレる所だったじゃないか。\x01",
            "まったくもう……！\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        (
            "#12P#0006Fは、はぁ……すみません。\x01",
            "（俺が悪いのか、今の……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xE,
        (
            "#5Pとにかく……\x01",
            "お詫びに手伝いたまえ。\x01",
            "指輪を探すの。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        (
            "#12P#0303Fおいおい……\x01",
            "何がお詫びなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x103,
        (
            "#12P#0203F全くもって義理はないかと。\x01",
            "無視して行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xE,
        (
            "#5Pし、失礼、言い方が悪かった。\x01",
            "お願いします助けてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xE,
        (
            "#5P今夜、テーマパークの夜の部で\x01",
            "花火が上がるのは知ってるだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xE,
        (
            "#5Pあの指輪は、どうしても\x01",
            "その最高のムードの中で\x01",
            "彼女に渡したいんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4116")

    #C0168
    ChrTalk(
        0x151,
        "#5700F#12Pフフ、なかなかロマンチストだね。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x102,
        (
            "#12P#0102Fええ、ほんと。\x02\x03",

            "#0100F私たちもそんなに時間に\x01",
            "余裕があるわけではないけど……\x01",
            "気にかけておきましょうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4192")

    label("loc_4116")


    #C0170
    ChrTalk(
        0x102,
        (
            "#12P#0102Fふふ……素敵ですね。\x02\x03",

            "#0100F私たちもそんなに時間に\x01",
            "余裕があるわけではないけど……\x01",
            "気にかけておきましょうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4192")


    #C0171
    ChrTalk(
        0xE,
        "#5Pおお……本当かい！？\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#12P#0011F……エ、エリィ？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#12P#0104Fふふ、いいじゃない。\x02\x03",

            "彼女のためを考えて\x01",
            "一生懸命彼が考えた\x01",
            "シチュエーションよ。\x02\x03",

            "#0100F叶わなかったら、\x01",
            "彼女もかわいそうだもの。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4335")

    #C0174
    ChrTalk(
        0x101,
        (
            "#12P#006Fって言っても、\x01",
            "さすがに一般人のワジまで\x01",
            "連れ回すわけにはいかないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x151,
        (
            "#5704F#12P僕は全然構わないけどね。\x02\x03",

            "#5700Fま、自分たちが\x01",
            "ここに来た目的さえ忘れなければ\x01",
            "別にいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4375")

    label("loc_4335")


    #C0176
    ChrTalk(
        0x101,
        (
            "#12P#0003Fう、うーん……\x01",
            "確かにかわいそうでは\x01",
            "あるけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4375")


    #C0177
    ChrTalk(
        0x102,
        (
            "#12P#0100Fふふ、決まりね。\x02\x03",

            "#0105Fそれで……落とした場所に\x01",
            "心当たりはないんですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xE,
        (
            "#5P残念だが、無い。\x01",
            "まったく身に覚えが無いんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xE,
        (
            "#5Pただ言えるのは……\x01",
            "僕とアルビナはここに着いてから\x01",
            "一通りの場所を回った。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xE,
        "#5P宝石店は門前払いだったけどね。\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        (
            "#12P#0203F……流石にヒントが\x01",
            "アバウトすぎます。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xE,
        (
            "#5Pと、とにかく……\x01",
            "それらしいものを拾ったら\x01",
            "片っ端から見せに来てくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xE,
        (
            "#5P夜になったら僕たちは\x01",
            "テーマパークに入ってしまう。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xE,
        "#5Pいいね、よろしく頼んだよ！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0185
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【婚約指輪は今いずこ】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0xE, 0x10E, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 97960, 0, 122140, 270)
    OP_29(0x24, 0x4, 0x2)
    OP_29(0x24, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_3B6A end

    def Function_26_45EC(): pass

    label("Function_26_45EC")

    EventBegin(0x0)
    Fade(500)
    OP_68(97820, 900, 122220, 0)
    MoveCamera(313, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20810, 0)
    SetChrPos(0x101, 98200, 0, 121000, 270)
    SetChrPos(0x102, 98200, 0, 122200, 270)
    SetChrPos(0x103, 99400, 0, 121000, 270)
    SetChrPos(0x104, 99400, 0, 122200, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_467F")
    SetChrPos(0x151, 100600, 0, 121600, 270)

    label("loc_467F")

    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0x5A, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_4B(0xF, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_0D()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0186
    ChrTalk(
        0xE,
        (
            "#5Pもしかして……\x01",
            "指輪を見つけてきて\x01",
            "くれたのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#12P#0000Fええ、ミシュラム保有地内で\x01",
            "拾いました。\x02\x03",

            "トマさんのものか、\x01",
            "確認をお願いします。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4793")
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0188
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_4793")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C8")
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_47C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47FD")
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0190
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_47FD")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0191
    ChrTalk(
        0xE,
        "#5Pふむ、どれどれ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48D2")

    #C0192
    ChrTalk(
        0xE,
        "#5P……この金の指輪は……\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xE,
        (
            "#5P……ちがうな。\x01",
            "この指輪じゃないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xE,
        (
            "#5P形状は近いけど、\x01",
            "色が全然違う。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x2)

    label("loc_48D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4976")

    #C0195
    ChrTalk(
        0xE,
        "#5P……この真珠の指輪は……\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xE,
        (
            "#5P……ちがう。\x01",
            "これじゃないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xE,
        (
            "#5P確かに美しいけど……\x01",
            "僕の買った物とは\x01",
            "似ても似つかない。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x4)

    label("loc_4976")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A11")

    #C0198
    ChrTalk(
        0xE,
        "#5P……この白金の指輪は……\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xE,
        (
            "#5P……ちがう。\x01",
            "こんなのじゃないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xE,
        (
            "#5Pこんな悪趣味なの、\x01",
            "彼女に渡すわけないだろ？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x24, 0x1, 0x6)

    label("loc_4A11")

    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0201
    ChrTalk(
        0x101,
        "#12P#0006Fそ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xE,
        (
            "#5Pこの指輪は返すよ。\x01",
            "好きにしたらいい。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "トマに渡した指輪を返してもらった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55FE")
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0204
    ChrTalk(
        0xE,
        (
            "#5P……これだけ指輪が\x01",
            "見つかってるのに、\x01",
            "僕の指輪が無いなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xE,
        (
            "#5Pハァ……\x01",
            "一体どこに落として\x01",
            "しまったんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        (
            "#12P#0100Fあの……\x01",
            "気を落とさないでください。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4D3F")

    #C0207
    ChrTalk(
        0x151,
        (
            "#5706F#12Pそうだねぇ……これ以上、\x01",
            "どこを探せばいいんだろうね。\x02\x03",

            "#5702Fあるいは、もう誰かに\x01",
            "拾われちゃってたりしてね？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#6P#0011Fワ、ワジッ……！\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xE,
        "#5P……や、やっぱりそうなのかな……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0210
    ChrTalk(
        0x104,
        "#12P#0306Fおいおい、落ち込んじまったぞ。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x151,
        (
            "#5709F#12Pあはは、\x01",
            "軽いジョークってヤツだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E6B")

    label("loc_4D3F")


    #C0212
    ChrTalk(
        0x104,
        (
            "#12P#0306Fつか、こんだけ探して\x01",
            "無いんだから、もう誰かに\x01",
            "拾われてるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        "#6P#0011Fラ、ランディッ……！\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xE,
        "#5P……や、やっぱりそうなのかな……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0215
    ChrTalk(
        0x103,
        (
            "#12P#0203F……すっかり落ち込んで\x01",
            "しまいましたね、\x01",
            "ランディさんのせいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        "#12P#0306Fお、俺のせいかよ……\x02",
    )

    CloseMessageWindow()

    label("loc_4E6B")

    OP_68(99540, 1200, 123070, 2000)
    OP_6F(0x1)
    OP_93(0xF, 0x10E, 0x1F4)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(99270, 1200, 122850, 2000)
    OP_95(0xF, 102010, 0, 123530, 2000, 0x0)
    TurnDirection(0xF, 0xE, 500)
    OP_6F(0x1)

    #C0217
    ChrTalk(
        0xF,
        (
            "#12P……トマ？　どうしたの、\x01",
            "元気がないみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F08():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4F08)
    Sleep(100)

    def lambda_4F18():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F18)
    Sleep(50)

    def lambda_4F28():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F28)
    Sleep(100)

    def lambda_4F38():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F38)
    Sleep(50)

    def lambda_4F48():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4F48)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4F69")

    def lambda_4F61():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4F61)

    label("loc_4F69")


    #C0218
    ChrTalk(
        0xE,
        (
            "#5Pえっ！？\x01",
            "いや、えっとそのあの……\x01",
            "なんでもないんだ、うん。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xF,
        (
            "#12P……そう？\x01",
            "そうは見えないんだけどな……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xF,
        (
            "#12Pねぇトマ。\x01",
            "もし気分が悪いなら、\x01",
            "高級住宅街の方に行ってみない？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xF,
        (
            "#12P午前中に散策した時、\x01",
            "湖のほとりのベンチで\x01",
            "一緒に休んだじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xE,
        "#5Pああ、そうだったね……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xE,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xE)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0224
    ChrTalk(
        0xE,
        "#5P#5Sあ……あああああああああっ！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5174():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5174)
    Sleep(100)

    def lambda_5184():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5184)
    Sleep(50)

    def lambda_5194():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5194)
    Sleep(100)

    def lambda_51A4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_51A4)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_51C5")

    def lambda_51BD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_51BD)

    label("loc_51C5")


    #C0225
    ChrTalk(
        0x101,
        "#12P#0005Fト、トマさん？\x02",
    )

    CloseMessageWindow()

    def lambda_51E8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_51E8)

    #C0226
    ChrTalk(
        0xE,
        (
            "#5P思い出した、思い出したんだよ！\x01",
            "きっとあの時だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xE,
        (
            "#5Pアルビナと２人で\x01",
            "ベンチに座っているとき……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xE,
        (
            "#5P一度ポッケの中の\x01",
            "アレの存在を確かめたんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xE,
        (
            "#5Pその後、ホテルに戻って\x01",
            "またポッケを確かめた時には\x01",
            "もう無くって……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xE,
        (
            "#5P落としたとしたら、\x01",
            "あの時、あの場所しか\x01",
            "考えられないっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        "#12P#0005Fほ、本当ですか？\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x103,
        (
            "#12P#0200Fいきなり有力な手がかりが\x01",
            "出てきましたね……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xF,
        (
            "#12P……ねぇ、トマ。\x01",
            "さっきから何の話をしてるの？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_53B7():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_53B7)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0234
    ChrTalk(
        0xE,
        (
            "#5Pい、いや、本当に\x01",
            "なんでもないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xE,
        (
            "#5Pほら、アルビナ。\x01",
            "ミシュラムの美しい町並みを\x01",
            "眺めていてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xF,
        (
            "#12P……そう？\x01",
            "なんだか変ねぇ……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(97670, 1200, 121980, 2000)
    OP_95(0xF, 103230, 0, 124330, 2000, 0x0)
    OP_93(0xF, 0x0, 0x1F4)
    OP_6F(0x1)

    #C0237
    ChrTalk(
        0xE,
        "#5Pあ、危なかった……\x02",
    )

    CloseMessageWindow()

    def lambda_54BF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_54BF)

    #C0238
    ChrTalk(
        0xE,
        (
            "#5Pと、とにかく、君たち！\x01",
            "一度高級住宅街の方を\x01",
            "見に行ってくれないか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xE,
        (
            "#5Pもしかしたら、\x01",
            "まだあのベンチのあたりに\x01",
            "落ちてるかも……！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x102,
        (
            "#12P#0100Fそうね……\x01",
            "ロイド、一度確認して\x01",
            "みましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        "#12P#0000Fそうだな……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_55F3")

    #C0242
    ChrTalk(
        0x151,
        (
            "#5709F#12Pハハ、君たちといると\x01",
            "ホント飽きないよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55F3")

    OP_29(0x24, 0x1, 0x7)
    Jump("loc_5680")

    label("loc_55FE")


    #C0243
    ChrTalk(
        0xE,
        (
            "#5Pハァ……\x01",
            "一体どこに落として\x01",
            "しまったんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xE,
        (
            "#5Pとにかく……\x01",
            "それらしい指輪を見つけたら\x01",
            "また持ってきて見せてくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5680")

    OP_93(0xE, 0x10E, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 97960, 0, 122140, 270)
    EventEnd(0x5)
    Return()

    # Function_26_45EC end

    def Function_27_56A3(): pass

    label("Function_27_56A3")

    EventBegin(0x0)
    Fade(500)
    OP_68(97820, 900, 122220, 0)
    MoveCamera(313, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20810, 0)
    SetChrPos(0x101, 98200, 0, 121000, 270)
    SetChrPos(0x102, 98200, 0, 122200, 270)
    SetChrPos(0x103, 99400, 0, 121000, 270)
    SetChrPos(0x104, 99400, 0, 122200, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_5736")
    SetChrPos(0x151, 100600, 0, 121600, 270)

    label("loc_5736")

    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0x5A, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_4B(0xF, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_0D()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0245
    ChrTalk(
        0xE,
        "#5Pあ、君たち……！\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xE,
        (
            "#5Pもしかして……\x01",
            "ついに指輪を見つけてきて\x01",
            "くれたのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#12P#0000Fええ、それらしいものが。\x01",
            "一度確認をお願いします。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0248
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x34F, 1)

    #C0249
    ChrTalk(
        0xE,
        "#5Pふむ、どれどれ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)

    #C0250
    ChrTalk(
        0xE,
        "#5P……こ、これだ……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xE,
        "#5Pこの指輪だよ、間違いない！\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xE,
        (
            "#5P銀耀石で出来たリングに彫られた\x01",
            "僕とアルビナの名前……\x01",
            "確かに僕のものにちがいないよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        (
            "#12P#0012Fそ、そうですか。\x01",
            "それは良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x104,
        (
            "#12P#0306Fやれやれ、\x01",
            "また違うなんて言われたら\x01",
            "どうしようかと思ったぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_5A10")

    #C0255
    ChrTalk(
        0x151,
        (
            "#5702F#12Pフフ、そのときはまた\x01",
            "どこかに探しにいけばいいじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x103,
        "#12P#0206F冗談きついです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A2E")

    label("loc_5A10")


    #C0257
    ChrTalk(
        0x103,
        "#12P#0206Fまったくです。\x02",
    )

    CloseMessageWindow()

    label("loc_5A2E")


    #C0258
    ChrTalk(
        0x102,
        (
            "#12P#0100Fふふ、よかったですね、\x01",
            "無事指輪が見つかって。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xE,
        "#5Pああ、ありがとう……！\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xE,
        (
            "#5Pテーマパークに入る前に\x01",
            "見つかって本当によかった！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xE,
        (
            "#5Pこれで、予定していた\x01",
            "花火の中でのプロポーズ、\x01",
            "決行することができそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xE,
        (
            "#5Pありがとう、君たちには\x01",
            "どれだけ礼をしても足りないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xE,
        (
            "#5Pそうだ、よければコイツを\x01",
            "受け取ってくれないか？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0264
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x9A, 1)

    #C0265
    ChrTalk(
        0x101,
        (
            "#12P#0005Fえ……い、いいんですか？\x01",
            "こんなよさそうなものを……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xE,
        (
            "#5Pああ、気にしないでくれたまえ。\x01",
            "君たちへの感謝の気持ちだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xE,
        (
            "#5Pさぁ……夜に向けて\x01",
            "心の準備を始めないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xE,
        (
            "#5Pまたどこかで会うことがあったら\x01",
            "そのときはよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【婚約指輪は今いずこ】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0xE, 0x10E, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 97960, 0, 122140, 270)
    OP_29(0x24, 0x1, 0xA)
    OP_29(0x24, 0x4, 0x10)
    SetScenarioFlags(0x0, 3)
    EventEnd(0x5)
    Return()

    # Function_27_56A3 end

    def Function_28_5D6A(): pass

    label("Function_28_5D6A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "        ～階段室～\x01",
            "現在、３階のＶＩＰフロアは\x01",
            "貸し切りとなっております。\x01",
            "立ち入りはご遠慮下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_28_5D6A end

    def Function_29_5E05(): pass

    label("Function_29_5E05")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0271
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっているようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_29_5E05 end

    SaveToFile()

Try(main)
