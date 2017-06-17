from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c034b.bin",                # FileName
        "c034b",                    # MapName
        "c034b",                    # Location
        0x002D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "c034b",                  # 0
        "イズリ夫人",             # 1
        "フェリック",             # 2
        "シンディ",               # 3
        "アンリ",                 # 4
        "ユンクス",               # 5
    ))

    AddCharChip((
        "chr/ch21700.itc",                   # 00
        "chr/ch21702.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch22200.itc",                   # 04
        "chr/ch27600.itc",                   # 05
        "chr/ch21900.itc",                   # 06
        "chr/ch22102.itc",                   # 07
        "chr/ch22202.itc",                   # 08
        "chr/ch27602.itc",                   # 09
    ))

    DeclNpc(40669,   0,       9600,    360,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(32659,   0,       5679,    180,  261,  0x0, 0,   2,   0,   0,   2,   0,   7,   255,  0)
    DeclNpc(4980,    0,       8989,    89,   261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(5329,    0,       3990,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(689,     0,       990,     225,  389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)

    ChipFrameInfo(372, 0)                                        # 0

    ScpFunction((
        "Function_0_174",          # 00, 0
        "Function_1_224",          # 01, 1
        "Function_2_24C",          # 02, 2
        "Function_3_277",          # 03, 3
        "Function_4_33E",          # 04, 4
        "Function_5_33F",          # 05, 5
        "Function_6_3C0",          # 06, 6
        "Function_7_4A3",          # 07, 7
        "Function_8_58A",          # 08, 8
        "Function_9_6B2",          # 09, 9
        "Function_10_7B0",         # 0A, 10
    ))


    def Function_0_174(): pass

    label("Function_0_174")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1AC"),
        (1, "loc_1B8"),
        (2, "loc_1C4"),
        (3, "loc_1D0"),
        (4, "loc_1DC"),
        (5, "loc_1E8"),
        (6, "loc_1F4"),
        (SWITCH_DEFAULT, "loc_200"),
    )


    label("loc_1AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_1F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_200")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_20C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_223")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_20C")

    label("loc_223")

    Return()

    # Function_0_174 end

    def Function_1_224(): pass

    label("Function_1_224")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24B")
    OP_94(0xFE, 0x14D2, 0xFFFFFCAE, 0xFFFFF6B4, 0x94C, 0x3E8)
    Jump("Function_1_224")

    label("loc_24B")

    Return()

    # Function_1_224 end

    def Function_2_24C(): pass

    label("Function_2_24C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_276")
    OP_94(0xFE, 0x7738, 0x1126, 0x852A, 0x1D38, 0x3E8)
    Sleep(300)
    Jump("Function_2_24C")

    label("loc_276")

    Return()

    # Function_2_24C end

    def Function_3_277(): pass

    label("Function_3_277")

    SetChrPos(0x8, 2560, 350, 6660, 225)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -630, 200, 6750, 135)
    SetChrChipByIndex(0xC, 0x9)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D4")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_2D4")

    SetChrPos(0xA, 2380, 200, 3690, 315)
    SetChrChipByIndex(0xA, 0x7)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrSubChip(0xA, 0x1)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -380, 200, 3780, 45)
    SetChrChipByIndex(0xB, 0x8)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0x9, 700, 0, 0, 270)
    BeginChrThread(0x9, 0, 0, 1)
    Return()

    # Function_3_277 end

    def Function_4_33E(): pass

    label("Function_4_33E")

    Return()

    # Function_4_33E end

    def Function_5_33F(): pass

    label("Function_5_33F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354")
    Call(0, 6)
    Jump("loc_3BC")

    label("loc_354")


    #C0001
    ChrTalk(
        0xFE,
        (
            "マリエッタさんも\x01",
            "忙しいみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "家族全員で食事をするのは\x01",
            "しばらく先のことになりそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BC")

    TalkEnd(0xFE)
    Return()

    # Function_5_33F end

    def Function_6_3C0(): pass

    label("Function_6_3C0")


    #C0003
    ChrTalk(
        0x8,
        (
            "そういえばユンクス、\x01",
            "マリエッタさんは帰国の目処は\x01",
            "ついているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xC,
        (
            "うーん、しばらく難しいかもな。\x01",
            "結構忙しくしてるみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "そう……\x01",
            "家族全員で食事をするのは\x01",
            "しばらく先のことになりそうね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_6_3C0 end

    def Function_7_4A3(): pass

    label("Function_7_4A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_540")

    #C0006
    ChrTalk(
        0xFE,
        (
            "仕事で忙しい親父が、\x01",
            "久しぶりに夕飯の時間に\x01",
            "帰ってきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "ありゃ、そういえば\x01",
            "イスが足りないな。\x01",
            "物置から出してこないと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_586")

    label("loc_540")


    #C0008
    ChrTalk(
        0xFE,
        (
            "ありゃ、そういえば\x01",
            "イスが足りないな。\x01",
            "物置から出してこないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_586")

    TalkEnd(0xFE)
    Return()

    # Function_7_4A3 end

    def Function_8_58A(): pass

    label("Function_8_58A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67F")

    #C0009
    ChrTalk(
        0xFE,
        (
            "アンリ、オルキスタワーを\x01",
            "近くで見てきたんでしょ。\x01",
            "どんな感じだった？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "やっぱり大っきかった？\x01",
            "ミラがかかってそうだった？\x01",
            "いっぱい人いた？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xB,
        (
            "ちょ、ちょっと姉さん。\x01",
            "一度にそんなに質問されても\x01",
            "答えられないってば～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6AE")

    label("loc_67F")


    #C0012
    ChrTalk(
        0xFE,
        (
            "いいじゃない、\x01",
            "ケチケチしないで教えてよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AE")

    TalkEnd(0xFE)
    Return()

    # Function_8_58A end

    def Function_9_6B2(): pass

    label("Function_9_6B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_737")

    #C0013
    ChrTalk(
        0xFE,
        "もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "あ、支援課の皆さん。\x01",
            "ウチになにか用ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "よかったら一緒に\x01",
            "夕飯を食べていきます？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7AC")

    label("loc_737")


    #C0016
    ChrTalk(
        0xFE,
        (
            "それにしても昼の除幕式は\x01",
            "すごかったですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "警察のみなさんは\x01",
            "忙しいでしょうけど、\x01",
            "がんばってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AC")

    TalkEnd(0xFE)
    Return()

    # Function_9_6B2 end

    def Function_10_7B0(): pass

    label("Function_10_7B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C5")
    Call(0, 6)
    Jump("loc_845")

    label("loc_7C5")


    #C0018
    ChrTalk(
        0xFE,
        (
            "妻のマリエッタは\x01",
            "外国のＩＢＣ支社で働いてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "あっちはあっちで忙しそうだし、\x01",
            "帰ってくるのはまだまだ先だろうな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_845")

    TalkEnd(0xFE)
    Return()

    # Function_10_7B0 end

    SaveToFile()

Try(main)
