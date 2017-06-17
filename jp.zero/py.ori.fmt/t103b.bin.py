from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t103b.bin",                # FileName
        "t103b",                    # MapName
        "t103b",                    # Location
        0x0041,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t103b",                  # 0
        "係員",                   # 1
        "係員",                   # 2
        "男の子",                 # 3
        "男性",                   # 4
        "女性",                   # 5
        "男の子",                 # 6
        "男性",                   # 7
        "ホテル・デルフィニア方面",# 8
        "テーマパーク方面",       # 9
    ))

    AddCharChip((
        "chr/ch28300.itc",                   # 00
        "chr/ch20600.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch24600.itc",                   # 04
        "chr/ch24200.itc",                   # 05
    ))

    DeclNpc(4750,    4400,    0,       180,  257,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-4000,   4400,    0,       180,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-200,    4219,    -15479,  90,   257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-9,      4250,    -14289,  0,    273,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(980,     4219,    -15399,  270,  257,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-3829,   0,       -55380,  90,   273,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-3650,   0,       -54209,  180,  257,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)

    DeclEvent(0x0000, 0, 12,  0.0,                   4.150000095367432,     3.0,                   81.0,                  [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.6666666865348816,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -2.766666889190674,    -0.6000000238418579,   1.0])

    DeclActor(-14170,  4000,    -6040,   1200,    -14170,  5500,    -6040,   0x007C, 0,  10, 0x0000)
    DeclActor(-6650,   4000,    1550,    1200,    -6650,   5500,    1550,    0x007C, 0,  11, 0x0000)

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "ホテル・デルフィニア方面")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "テーマパーク方面")

    ScpFunction((
        "Function_0_278",          # 00, 0
        "Function_1_330",          # 01, 1
        "Function_2_340",          # 02, 2
        "Function_3_37D",          # 03, 3
        "Function_4_3E7",          # 04, 4
        "Function_5_4AC",          # 05, 5
        "Function_6_584",          # 06, 6
        "Function_7_5B1",          # 07, 7
        "Function_8_6BC",          # 08, 8
        "Function_9_701",          # 09, 9
        "Function_10_7A1",         # 0A, 10
        "Function_11_81E",         # 0B, 11
        "Function_12_902",         # 0C, 12
        "Function_13_B0B",         # 0D, 13
    ))


    def Function_0_278(): pass

    label("Function_0_278")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2B8"),
        (1, "loc_2C4"),
        (2, "loc_2D0"),
        (3, "loc_2DC"),
        (4, "loc_2E8"),
        (5, "loc_2F4"),
        (6, "loc_300"),
        (SWITCH_DEFAULT, "loc_30C"),
    )


    label("loc_2B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_2F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_300")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_30C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_318")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_318")

    label("loc_32F")

    Return()

    # Function_0_278 end

    def Function_1_330(): pass

    label("Function_1_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_33F")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_33F")

    Return()

    # Function_1_330 end

    def Function_2_340(): pass

    label("Function_2_340")

    SoundDistance(0x375, 0x92E0, 0xFA0, 0x44D4, 0x15F90, 0xEA60, 0x64, 0x0)
    OP_E1(0xFFFFF646, 0xFA0, 0x2800)
    OP_E1(0xFFFED040, 0xFA0, 0x466E)
    Sound(918, 1, 100, 0)
    Return()

    # Function_2_340 end

    def Function_3_37D(): pass

    label("Function_3_37D")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        "花火はご覧になられましたか？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "ミシュラム全域から見られるよう\x01",
            "高く高く上げているのですよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_37D end

    def Function_4_3E7(): pass

    label("Function_4_3E7")

    TalkBegin(0xFE)

    #C0003
    ChrTalk(
        0xFE,
        (
            "現在、中ではナイトパレードが\x01",
            "執り行われております。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "みっしぃを代表する\x01",
            "テーマパークのマスコットたちが\x01",
            "賑やかに園内を回るのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "こちらは入場者様だけの\x01",
            "お楽しみということで。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_3E7 end

    def Function_5_4AC(): pass

    label("Function_5_4AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_534")

    #C0006
    ChrTalk(
        0xFE,
        (
            "ジェットコースターが\x01",
            "すっごく楽しかったんだぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "#4Sンビューーーーン！！！！#3S\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "……って感じだった！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_580")

    label("loc_534")


    #C0009
    ChrTalk(
        0xFE,
        (
            "ジェットコースターって凄いね！\x01",
            "景色がぜーんぶ後ろに\x01",
            "流れちゃってさー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_580")

    TalkEnd(0xFE)
    Return()

    # Function_5_4AC end

    def Function_6_584(): pass

    label("Function_6_584")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "うぷぅ……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_584 end

    def Function_7_5B1(): pass

    label("Function_7_5B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_679")

    #C0012
    ChrTalk(
        0xFE,
        (
            "この人ったら\x01",
            "絶叫系の乗り物がダメなのに\x01",
            "ムリしちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "でも久しぶりの一家団欒は\x01",
            "凄く楽しかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "忙しい仕事の合間に\x01",
            "時間を作ってくれた夫には\x01",
            "感謝しなきゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6B8")

    label("loc_679")


    #C0015
    ChrTalk(
        0xFE,
        (
            "子供も随分楽しんだみたい。\x01",
            "ふふ、夫には感謝しなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B8")

    TalkEnd(0xFE)
    Return()

    # Function_7_5B1 end

    def Function_8_6BC(): pass

    label("Function_8_6BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E7")

    #C0016
    ChrTalk(
        0xFE,
        "うつらうつら……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6FD")

    label("loc_6E7")


    #C0017
    ChrTalk(
        0xFE,
        "むにゃむにゃ……\x02",
    )

    CloseMessageWindow()

    label("loc_6FD")

    TalkEnd(0xFE)
    Return()

    # Function_8_6BC end

    def Function_9_701(): pass

    label("Function_9_701")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_755")

    #C0018
    ChrTalk(
        0xFE,
        (
            "やれやれ、息子は全力で遊んで\x01",
            "完全燃焼しちゃったみたいだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_79D")

    label("loc_755")

    TurnDirection(0xFE, 0xD, 0)

    #C0019
    ChrTalk(
        0xFE,
        (
            "おーい、もうちょっとがんばれ。\x01",
            "水上バスがそろそろ来てるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79D")

    TalkEnd(0xFE)
    Return()

    # Function_9_701 end

    def Function_10_7A1(): pass

    label("Function_10_7A1")

    TalkBegin(0xFF)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "テーマパークの\x01",
            "見取り図が描かれている。\x02\x03",

            "広大な敷地に\x01",
            "さまざまなアミューズメント施設が\x01",
            "並んでいるようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_10_7A1 end

    def Function_11_81E(): pass

    label("Function_11_81E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   ～こ来園のみなさまへ～\x01\x01",
            "当テーマパーク内での\x01",
            "暴走行為や危険物の持ち込みは\x01",
            "固くお断り申し上げます。\x01\x01",
            "また、お子様には必ず\x01",
            "保護者の方が同伴なさるよう\x01",
            "お願い申し上げます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_81E end

    def Function_12_902(): pass

    label("Function_12_902")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A92")

    #C0022
    ChrTalk(
        0x101,
        (
            "#5003Fテーマパークの方は\x01",
            "盛り上がってるみたいだな……\x02\x03",

            "#5000Fまあ今回は遊んでる暇は無い。\x01",
            "準備も整ったし\x01",
            "オークション会場へ向かおう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C8")

    #C0023
    ChrTalk(
        0x103,
        "#0203F……そうしましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E8")

    label("loc_9C8")


    #C0024
    ChrTalk(
        0x103,
        "#5403F……そうしましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_9E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1D")

    #C0025
    ChrTalk(
        0x102,
        "#0100F時間に遅れても事だものね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A43")

    label("loc_A1D")


    #C0026
    ChrTalk(
        0x102,
        "#5300F時間に遅れても事だものね。\x02",
    )

    CloseMessageWindow()

    label("loc_A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6E")

    #C0027
    ChrTalk(
        0x104,
        "#0300Fうっし、行くか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A8A")

    label("loc_A6E")


    #C0028
    ChrTalk(
        0x104,
        "#5600Fうっし、行くか。\x02",
    )

    CloseMessageWindow()

    label("loc_A8A")

    SetScenarioFlags(0x0, 4)
    Jump("loc_AF4")

    label("loc_A92")


    #C0029
    ChrTalk(
        0x101,
        (
            "#5000F今回はテーマパークで\x01",
            "遊んでる暇は無い……\x02\x03",

            "準備も整ったし\x01",
            "オークション会場へ向かおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF4")

    Sleep(50)
    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x4)
    Return()

    # Function_12_902 end

    def Function_13_B0B(): pass

    label("Function_13_B0B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t105B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_B0B end

    SaveToFile()

Try(main)
