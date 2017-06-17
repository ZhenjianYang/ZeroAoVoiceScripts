from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c033b.bin",                # FileName
        "c033b",                    # MapName
        "c033b",                    # Location
        0x002C,                     # MapIndex
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
        "c033b",                  # 0
        "ハロルド",               # 1
        "ソフィア",               # 2
        "コリン",                 # 3
    ))

    AddCharChip((
        "chr/ch09300.itc",                   # 00
        "chr/ch09302.itc",                   # 01
        "chr/ch09400.itc",                   # 02
        "chr/ch09402.itc",                   # 03
        "chr/ch07200.itc",                   # 04
        "chr/ch07202.itc",                   # 05
    ))

    DeclNpc(-340,    0,       4409,    315,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(550,     0,       2039,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(37479,   0,       3799,    180,  261,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)

    DeclActor(34620,   0,       7280,    1200,    34620,   1750,    7280,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(320, 0)                                        # 0

    ScpFunction((
        "Function_0_140",          # 00, 0
        "Function_1_1F0",          # 01, 1
        "Function_2_23A",          # 02, 2
        "Function_3_23B",          # 03, 3
        "Function_4_2E3",          # 04, 4
        "Function_5_4A8",          # 05, 5
        "Function_6_51E",          # 06, 6
    ))


    def Function_0_140(): pass

    label("Function_0_140")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_178"),
        (1, "loc_184"),
        (2, "loc_190"),
        (3, "loc_19C"),
        (4, "loc_1A8"),
        (5, "loc_1B4"),
        (6, "loc_1C0"),
        (SWITCH_DEFAULT, "loc_1CC"),
    )


    label("loc_178")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_184")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_190")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_19C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1EF")

    Return()

    # Function_0_140 end

    def Function_1_1F0(): pass

    label("Function_1_1F0")

    SetChrPos(0x8, 1940, 200, 6910, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 40940, 0, -550, 180)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, 40930, 0, -1640, 90)
    Return()

    # Function_1_1F0 end

    def Function_2_23A(): pass

    label("Function_2_23A")

    Return()

    # Function_2_23A end

    def Function_3_23B(): pass

    label("Function_3_23B")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "車雑誌『月間カーマニアvol.1』がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36C, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DF")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "ペイントパターン\x01\x07\x02",

            "『スカイカラー』\x07\x00",
            "を覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36C, 1)

    label("loc_2DF")

    TalkEnd(0xFF)
    Return()

    # Function_3_23B end

    def Function_4_2E3(): pass

    label("Function_4_2E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_427")

    #C0003
    ChrTalk(
        0x8,
        "#03605Fおや、みなさん。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#00000Fこんばんは、ハロルドさん。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00104F２階からいい匂い……\x01",
            "奥様が夕食の準備を\x01",
            "されてるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#03600Fええ、そうなんですよ。\x01",
            "それに今日はコリンも\x01",
            "手伝っているみたいでして。\x02\x03",

            "#03609Fいやあ、私も出先から\x01",
            "戻ってきたところなので、\x01",
            "お腹がペコペコですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 6)
    Jump("loc_4A4")

    label("loc_427")


    #C0007
    ChrTalk(
        0x8,
        (
            "#03600Fどうやら今日は、\x01",
            "コリンが料理を手伝っている\x01",
            "みたいでしてね。\x02\x03",

            "#03609Fふふ、どんな料理が\x01",
            "出てくるか楽しみですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A4")

    TalkEnd(0xFE)
    Return()

    # Function_4_2E3 end

    def Function_5_4A8(): pass

    label("Function_5_4A8")

    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0x9,
        (
            "#03700Fさ、あとは煮立つのを待つだけよ。\x02\x03",

            "#03709Fふふ、よく出来たわねコリン。\x01",
            "きっとパパも喜んでくれるわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_4A8 end

    def Function_6_51E(): pass

    label("Function_6_51E")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xA,
        (
            "#03802Fきょうのばんごはんは\x01",
            "カレーなんだよ～。\x02\x03",

            "#03809Fえへへ、ぼくが\x01",
            "おやさいを切ったんだ～。\x01",
            "すごいでしょ～？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_51E end

    SaveToFile()

Try(main)
