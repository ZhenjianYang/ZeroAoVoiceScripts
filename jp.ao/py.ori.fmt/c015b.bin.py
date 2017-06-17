from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c015b.bin",                # FileName
        "c015b",                    # MapName
        "c015b",                    # Location
        0x0000,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c015b",                  # 0
        "ホイストフ",             # 1
        "ブラウン",               # 2
        "セルテオ",               # 3
        "ノンノ",                 # 4
        "フロテ",                 # 5
        "市民",                   # 6
        "市民",                   # 7
        "ホステス",               # 8
        "ビジネスマン",           # 9
        "ジロンド",               # 10
    ))

    AddCharChip((
        "chr/ch25200.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch25600.itc",                   # 03
        "chr/ch20200.itc",                   # 04
        "chr/ch34302.itc",                   # 05
        "chr/ch21902.itc",                   # 06
        "chr/ch20302.itc",                   # 07
        "chr/ch43402.itc",                   # 08
        "chr/ch27802.itc",                   # 09
    ))

    DeclNpc(-509,    0,       12449,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-42889,  0,       5699,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-52029,  0,       3650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-8880,   0,       3240,    45,   261,  0x0, 0,   3,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(-7449,   150,     8510,    270,  325,  0x0, 0,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(4460,    150,     5829,    180,  453,  0x0, 0,   6,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(6679,    150,     3630,    270,  453,  0x0, 0,   7,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-1649,   5150,    17649,   180,  453,  0x0, 0,   8,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-1649,   5150,    13439,   0,    453,  0x0, 0,   9,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(60580,   -1000,   -8600,   270,  261,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)

    DeclActor(59140,   -1000,   -8880,   1500,    60580,   500,     -8600,   0x007E, 0,  4,  0x0000)
    DeclActor(-510,    0,       10640,   1000,    -510,    1500,    12450,   0x007E, 0,  6,  0x0000)

    ChipFrameInfo(604, 0)                                        # 0

    ScpFunction((
        "Function_0_25C",          # 00, 0
        "Function_1_314",          # 01, 1
        "Function_2_3B1",          # 02, 2
        "Function_3_453",          # 03, 3
        "Function_4_454",          # 04, 4
        "Function_5_458",          # 05, 5
        "Function_6_6E9",          # 06, 6
        "Function_7_6ED",          # 07, 7
        "Function_8_904",          # 08, 8
        "Function_9_953",          # 09, 9
        "Function_10_9FD",         # 0A, 10
        "Function_11_A70",         # 0B, 11
        "Function_12_B0D",         # 0C, 12
        "Function_13_B90",         # 0D, 13
        "Function_14_C06",         # 0E, 14
        "Function_15_C66",         # 0F, 15
    ))


    def Function_0_25C(): pass

    label("Function_0_25C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_29C"),
        (1, "loc_2A8"),
        (2, "loc_2B4"),
        (3, "loc_2C0"),
        (4, "loc_2CC"),
        (5, "loc_2D8"),
        (6, "loc_2E4"),
        (SWITCH_DEFAULT, "loc_2F0"),
    )


    label("loc_29C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2A8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2B4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2C0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2CC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2D8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_313")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_313")

    Return()

    # Function_0_25C end

    def Function_1_314(): pass

    label("Function_1_314")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B0")
    OP_95(0xFE, -4260, 0, 8920, 2000, 0x0)
    OP_95(0xFE, 720, 0, 6870, 2000, 0x0)
    OP_95(0xFE, 780, 0, 1070, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -2090, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -6010, 2000, 0x0)
    OP_95(0xFE, 3280, 0, -8790, 2000, 0x0)
    OP_95(0xFE, -8880, 0, 3240, 2000, 0x0)
    Jump("Function_1_314")

    label("loc_3B0")

    Return()

    # Function_1_314 end

    def Function_2_3B1(): pass

    label("Function_2_3B1")

    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0x9)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    Return()

    # Function_2_3B1 end

    def Function_3_453(): pass

    label("Function_3_453")

    Return()

    # Function_3_453 end

    def Function_4_454(): pass

    label("Function_4_454")

    Call(0, 5)
    Return()

    # Function_4_454 end

    def Function_5_458(): pass

    label("Function_5_458")

    TalkBegin(0x11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_465")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_523")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E2")
    OP_AF(0x4)
    Jump("loc_514")

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4F2")
    OP_AF(0x3)
    Jump("loc_514")

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_502")
    OP_AF(0x2)
    Jump("loc_514")

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_512")
    OP_AF(0x1)
    Jump("loc_514")

    label("loc_512")

    OP_AF(0x0)

    label("loc_514")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E0")

    label("loc_523")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_537")
    Jump("loc_6E0")

    label("loc_537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_673")

    #C0001
    ChrTalk(
        0x11,
        (
            "よう、ダドリーじゃねえか。\x01",
            "支援課と仲良くお散歩かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x10A,
        (
            "#00603Fいえ、少々気になる事がありまして。\x02\x03",

            "#00600Fこいつらだけでは\x01",
            "頼りないので同行しているだけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x11,
        "へっ、お前も相変わらずだな。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x11,
        (
            "まあいい、そろそろ店仕舞いなもんで\x01",
            "見るならチャッチャと見てくれや。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6E0")

    label("loc_673")


    #C0005
    ChrTalk(
        0x11,
        (
            "そろそろ店仕舞いなモンだからよ。\x01",
            "見るならチャッチャと見てくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x11,
        "早く上がって、一杯やりてえんだ。\x02",
    )

    CloseMessageWindow()

    label("loc_6E0")

    Jump("loc_465")

    label("loc_6E5")

    TalkEnd(0x11)
    Return()

    # Function_5_458 end

    def Function_6_6E9(): pass

    label("Function_6_6E9")

    Call(0, 7)
    Return()

    # Function_6_6E9 end

    def Function_7_6ED(): pass

    label("Function_7_6ED")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_900")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_758")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_758")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_788")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_777")
    OP_AF(0x9)
    Jump("loc_779")

    label("loc_777")

    OP_AF(0x8)

    label("loc_779")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8FB")

    label("loc_788")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79C")
    Jump("loc_8FB")

    label("loc_79C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88B")

    #C0007
    ChrTalk(
        0x8,
        (
            "ブラウンから聞いたのですが、\x01",
            "どうやらノンノには料理人の\x01",
            "センスがあるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "当初は簡単な手伝いを\x01",
            "してもらうだけのつもりでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "ふむ、これは\x01",
            "思わぬ収穫かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_8FB")

    label("loc_88B")


    #C0010
    ChrTalk(
        0x8,
        (
            "ノンノには簡単な手伝いを\x01",
            "してもらうだけのつもりでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "ふむ、これは\x01",
            "思わぬ収穫かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FB")

    Jump("loc_6FA")

    label("loc_900")

    TalkEnd(0x8)
    Return()

    # Function_7_6ED end

    def Function_8_904(): pass

    label("Function_8_904")

    TalkBegin(0xFE)

    #C0012
    ChrTalk(
        0xFE,
        (
            "よしっ、いっそのこと\x01",
            "明日は思い切って\x01",
            "ノンノに調理を任せてみるか。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_904 end

    def Function_9_953(): pass

    label("Function_9_953")

    TalkBegin(0xFE)

    #C0013
    ChrTalk(
        0xFE,
        (
            "全然気にしてなかったけど、\x01",
            "ノンノの奴、いつの間にか仕込みまで\x01",
            "任されるようになってたんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "まさか、このままコックに\x01",
            "なっちまうってことはねえよなぁ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_953 end

    def Function_10_9FD(): pass

    label("Function_10_9FD")

    TalkBegin(0xFE)

    #C0015
    ChrTalk(
        0xFE,
        (
            "この仕込みを終えたら\x01",
            "次はお皿を洗って、と。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "ふう……やっぱりウチの\x01",
            "ディナータイムは忙しいですね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_9FD end

    def Function_11_A70(): pass

    label("Function_11_A70")

    TalkBegin(0xFE)

    #C0017
    ChrTalk(
        0xFE,
        (
            "ふう、今日はついつい読書に熱中して\x01",
            "久しぶりに日が暮れるまで居ちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "流石にお店の人にも悪いから、\x01",
            "このまま夕飯でも食べて行こうかしら。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_A70 end

    def Function_12_B0D(): pass

    label("Function_12_B0D")

    TalkBegin(0xFE)

    #C0019
    ChrTalk(
        0xFE,
        (
            "今日はお互い、家族を放って\x01",
            "女２人でディナーに来ているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "たまにはこういう日もないとねー。\x01",
            "主婦も色々大変なのよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_B0D end

    def Function_13_B90(): pass

    label("Function_13_B90")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        (
            "好きな物を沢山食べて喋りまくる……\x01",
            "これが私たちのストレス解消法よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "さぁ、今日は目一杯楽しむわよ～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_B90 end

    def Function_14_C06(): pass

    label("Function_14_C06")

    TalkBegin(0xFE)

    #C0023
    ChrTalk(
        0xFE,
        (
            "うふふ、そういうベタな台詞、\x01",
            "嫌いじゃないわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "何だかもう、酔っちゃったかも㈱\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_C06 end

    def Function_15_C66(): pass

    label("Function_15_C66")

    TalkBegin(0xFE)

    #C0025
    ChrTalk(
        0xFE,
        (
            "――君の瞳に乾杯。\x01",
            "今夜は特別な夜になりそうだね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_C66 end

    SaveToFile()

Try(main)
