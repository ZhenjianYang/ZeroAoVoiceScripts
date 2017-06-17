from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c022b.bin",                # FileName
        "c022b",                    # MapName
        "c022b",                    # Location
        0x000D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c022b",                  # 0
        "イアン弁護士",           # 1
        "ピート",                 # 2
    ))

    AddCharChip((
        "chr/ch05900.itc",                   # 00
        "chr/ch05902.itc",                   # 01
        "chr/ch22200.itc",                   # 02
    ))

    DeclNpc(4510,    1169,    15779,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(12869,   1000,    4809,    90,   261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)

    DeclActor(14350,   1000,    -70,     2000,    14350,   2500,    -70,     0x007C, 0,  5,  0x0000)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_1C4",          # 01, 1
        "Function_2_1E4",          # 02, 2
        "Function_3_1EB",          # 03, 3
        "Function_4_3EF",          # 04, 4
        "Function_5_5E9",          # 05, 5
    ))


    def Function_0_114(): pass

    label("Function_0_114")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_14C"),
        (1, "loc_158"),
        (2, "loc_164"),
        (3, "loc_170"),
        (4, "loc_17C"),
        (5, "loc_188"),
        (6, "loc_194"),
        (SWITCH_DEFAULT, "loc_1A0"),
    )


    label("loc_14C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_158")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_164")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_170")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_17C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_188")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_194")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1C3")

    Return()

    # Function_0_114 end

    def Function_1_1C4(): pass

    label("Function_1_1C4")

    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 3)), scpexpr(EXPR_END)), "loc_1E3")
    SetChrFlags(0x9, 0x10)

    label("loc_1E3")

    Return()

    # Function_1_1C4 end

    def Function_2_1E4(): pass

    label("Function_2_1E4")

    ClearMapObjFlags(0x0, 0x10)
    Return()

    # Function_2_1E4 end

    def Function_3_1EB(): pass

    label("Function_3_1EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384")

    #C0001
    ChrTalk(
        0xFE,
        (
            "#02200Fおや、君たち。\x01",
            "こんな夜に来るとは珍しいね。\x02\x03",

            "ダドリー君も一緒とは……\x01",
            "明日の会議本番に関わるような\x01",
            "問題でも発生したかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x10A,
        (
            "#00603F今から、それを確かめに\x01",
            "行くところです。\x02\x03",

            "#00600F万全を期すためには、\x01",
            "不確定な要素は潰しておくに\x01",
            "越した事はありませんからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "#02200Fうむ、用心しすぎるという\x01",
            "ことはないだろうな。\x02\x03",

            "詳しい事情は知らないが……\x01",
            "是非ともがんばってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3EB")

    label("loc_384")


    #C0004
    ChrTalk(
        0xFE,
        (
            "#02200Fさて……\x01",
            "準備はこのあたりで充分だな。\x02\x03",

            "ひとまず明日に備えて、\x01",
            "今日は早めに休むとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EB")

    TalkEnd(0xFE)
    Return()

    # Function_3_1EB end

    def Function_4_3EF(): pass

    label("Function_4_3EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_569")

    #C0005
    ChrTalk(
        0xFE,
        (
            "書類整理をしていたら\x01",
            "僕が以前、留守番している時に\x01",
            "読んでいた本が出てきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "この本に出てくる『カゲマル』……\x01",
            "僕、みっしぃよりも気に入ってるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "僕は一度読んだ本って、\x01",
            "あまり読み返さない性分ですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "せっかくですから\x01",
            "皆さんも読んでみませんか？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2F1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F1, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 3)
    TalkEnd(0xFE)
    SetChrFlags(0x9, 0x10)
    Return()

    label("loc_569")


    #C0010
    ChrTalk(
        0xFE,
        (
            "あれ、このファイル……\x01",
            "収納する場所が間違ってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "まったくイアン先生ったら、\x01",
            "こういうところはズボラなんだから……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_3EF end

    def Function_5_5E9(): pass

    label("Function_5_5E9")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_5_5E9 end

    SaveToFile()

Try(main)
