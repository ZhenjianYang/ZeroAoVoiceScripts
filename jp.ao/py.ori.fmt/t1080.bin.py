from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1080.bin",                # FileName
        "t1080",                    # MapName
        "t1080",                    # Location
        0x0042,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1080",                  # 0
        "シトラス",               # 1
        "ゾルク",                 # 2
        "キーア",                 # 3
        "フラン",                 # 4
        "セシル",                 # 5
        "イリア",                 # 6
        "リーシャ",               # 7
        "シュリ",                 # 8
        "エリィ",                 # 9
        "ティオ",                 # 10
        "ノエル",                 # 11
        "ツァイト",               # 12
        "マリアベル",             # 13
    ))

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch08500.itc",                   # 01
        "chr/ch05200.itc",                   # 02
        "chr/ch05100.itc",                   # 03
        "chr/ch07500.itc",                   # 04
        "chr/ch10000.itc",                   # 05
        "chr/ch00100.itc",                   # 06
        "chr/ch00200.itc",                   # 07
        "chr/ch02900.itc",                   # 08
        "chr/ch25600.itc",                   # 09
        "chr/ch25900.itc",                   # 0A
        "chr/ch02707.itc",                   # 0B
        "chr/ch05202.itc",                   # 0C
        "chr/ch10002.itc",                   # 0D
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

    DeclNpc(106129,  0,       11579,   0,    385,  0x0, 0,   9,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(-14840,  0,       6570,    90,   385,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   6,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(569,     0,       1809,    135,  389,  0x0, 0,   11,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-13250,  0,       6540,    1500,    -14840,  1500,    6570,    0x007E, 0,  17, 0x0000)

    ChipFrameInfo(804, 0)                                        # 0

    ScpFunction((
        "Function_0_324",          # 00, 0
        "Function_1_3DC",          # 01, 1
        "Function_2_43D",          # 02, 2
        "Function_3_62A",          # 03, 3
        "Function_4_661",          # 04, 4
        "Function_5_899",          # 05, 5
        "Function_6_D2B",          # 06, 6
        "Function_7_129C",         # 07, 7
        "Function_8_151F",         # 08, 8
        "Function_9_16F6",         # 09, 9
        "Function_10_19D7",        # 0A, 10
        "Function_11_1AC7",        # 0B, 11
        "Function_12_1E50",        # 0C, 12
        "Function_13_2025",        # 0D, 13
        "Function_14_21EC",        # 0E, 14
        "Function_15_2319",        # 0F, 15
        "Function_16_24D7",        # 10, 16
        "Function_17_2658",        # 11, 17
        "Function_18_265C",        # 12, 18
        "Function_19_2833",        # 13, 19
        "Function_20_3A24",        # 14, 20
        "Function_21_3A34",        # 15, 21
        "Function_22_3A44",        # 16, 22
        "Function_23_3A54",        # 17, 23
        "Function_24_3A64",        # 18, 24
        "Function_25_3A92",        # 19, 25
        "Function_26_3ACF",        # 1A, 26
        "Function_27_3B0C",        # 1B, 27
        "Function_28_3B49",        # 1C, 28
        "Function_29_3B86",        # 1D, 29
        "Function_30_3BC3",        # 1E, 30
        "Function_31_3C0F",        # 1F, 31
        "Function_32_3C5B",        # 20, 32
        "Function_33_3CA7",        # 21, 33
    ))


    def Function_0_324(): pass

    label("Function_0_324")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_364"),
        (1, "loc_370"),
        (2, "loc_37C"),
        (3, "loc_388"),
        (4, "loc_394"),
        (5, "loc_3A0"),
        (6, "loc_3AC"),
        (SWITCH_DEFAULT, "loc_3B8"),
    )


    label("loc_364")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_370")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_37C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_388")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_394")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3A0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3DB")

    Return()

    # Function_0_324 end

    def Function_1_3DC(): pass

    label("Function_1_3DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43C")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_1_3DC")

    label("loc_43C")

    Return()

    # Function_1_3DC end

    def Function_2_43D(): pass

    label("Function_2_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_44B")
    Jump("loc_5F1")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_45E")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_5F1")

    label("loc_45E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4F8")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 5850, 0, 4400, 45)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 6560, 0, 5100, 225)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7")
    SetChrFlags(0x11, 0x10)

    label("loc_4A7")

    SetChrChipByIndex(0xE, 0xC)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 97700, 150, 124100, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 4800, 0, 6050, 135)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_5F1")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_506")
    Jump("loc_5F1")

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5F1")
    SetChrChipByIndex(0xF, 0xD)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 104060, 500, 118180, 0)
    SetChrChipByIndex(0xE, 0xC)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 104060, 500, 119880, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 99230, 0, -80380, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 100220, 0, -80390, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59D")
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_59D")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -100940, 0, 121230, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -99810, 0, 121220, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x12, 0x10)

    label("loc_5DD")

    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_605")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)
    Jump("loc_617")

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_617")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 33)

    label("loc_617")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_629")
    OP_66(0x0, 0x1)

    label("loc_629")

    Return()

    # Function_2_43D end

    def Function_3_62A(): pass

    label("Function_3_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_63F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_63F")

    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_62A end

    def Function_4_661(): pass

    label("Function_4_661")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_672")
    Jump("loc_895")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_680")
    Jump("loc_895")

    label("loc_680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_68E")
    Jump("loc_895")

    label("loc_68E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_69C")
    Jump("loc_895")

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_706")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B7")
    Call(0, 15)
    Jump("loc_701")

    label("loc_6B7")


    #C0001
    ChrTalk(
        0xF,
        (
            "#04205Fな、なんだよいきなり……\x02\x03",

            "#04206Fオレ、何か悪いこと言ったか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_701")

    Jump("loc_895")

    label("loc_706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_714")
    Jump("loc_895")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_895")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72F")
    Call(0, 6)
    Jump("loc_895")

    label("loc_72F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_845")

    #C0002
    ChrTalk(
        0xF,
        (
            "#04206Fはあ、泳ぐなんて\x01",
            "生まれて初めてだよ。\x02\x03",

            "#04208Fリーシャ姉が教えてくれるけど、\x01",
            "溺れちゃったらどうしよう……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x104,
        (
            "#00309Fはは、んなことで悩むなんて\x01",
            "可愛いとこがあるじゃねえか、\x01",
            "シュリぞう。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xF,
        (
            "#04201Fああ、もう！\x01",
            "シュリぞうでいいから\x01",
            "あっちいけっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_895")

    label("loc_845")


    #C0005
    ChrTalk(
        0xF,
        (
            "#04206F泳ぐなんて生まれて初めてだよ。\x02\x03",

            "#04208F溺れちゃったらどうしよう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_895")

    TalkEnd(0xFE)
    Return()

    # Function_4_661 end

    def Function_5_899(): pass

    label("Function_5_899")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_8AA")
    Jump("loc_D27")

    label("loc_8AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8B8")
    Jump("loc_D27")

    label("loc_8B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_8C6")
    Jump("loc_D27")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_8E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DE")
    Jump("loc_8DE")

    label("loc_8DE")

    Jump("loc_D27")

    label("loc_8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9F")

    #C0006
    ChrTalk(
        0xE,
        "#01802Fあ……ロイドさん。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00005Fあれ、リーシャ。\x01",
            "まだ部屋にいたのか？\x02\x03",

            "#00000Fエリィたちと一緒に\x01",
            "ブティックに行ったと\x01",
            "思っていたんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xE,
        (
            "#01809Fあはは、なんだかビーチで\x01",
            "遊び疲れちゃったみたいで。\x02\x03",

            "#01802F少し休んだら\x01",
            "私も行ってみるつもりですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00005Fそうか……\x02\x03",

            "#00002Fまあ、テーマパークでの\x01",
            "待ち合わせまでは時間があるし、\x01",
            "無理はしないでくれよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xE,
        "#01809Fはい、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B12")

    label("loc_A9F")


    #C0011
    ChrTalk(
        0xE,
        (
            "#01800Fキーアちゃんなら、\x01",
            "こちらには来ていませんよ。\x02\x03",

            "もしかしたら、ホテルから\x01",
            "出ちゃったのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B12")

    Jump("loc_D27")

    label("loc_B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_B25")
    Jump("loc_D27")

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_D27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B40")
    Call(0, 6)
    Jump("loc_D27")

    label("loc_B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9A")

    #C0012
    ChrTalk(
        0xE,
        (
            "#01803F本当は、私みたいな未熟者が\x01",
            "遊んでるヒマなんてないんですけど……\x02\x03",

            "#01802Fアーティストには休むのも大事だって、\x01",
            "イリアさんに説得されてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#00004Fイリアさんの言うことももっともだよ。\x02\x03",

            "#00000Fせっかくの機会だし、リーシャも\x01",
            "目一杯気分転換したらいいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xE,
        "#01800Fふふ……ええ、そうさせてもらいます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D27")

    label("loc_C9A")


    #C0015
    ChrTalk(
        0xE,
        (
            "#01804Fまずは基本の泳法から\x01",
            "順番に教えた方がいいですね。\x02\x03",

            "#01803Fそれさえ覚えれば、後は\x01",
            "シュリちゃんのセンスで\x01",
            "何とかなると思いますし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D27")

    TalkEnd(0xFE)
    Return()

    # Function_5_899 end

    def Function_6_D2B(): pass

    label("Function_6_D2B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DBC")
    Jump("loc_E06")

    label("loc_DBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DDC")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E06")

    label("loc_DDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFC")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E06")

    label("loc_DFC")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E06")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EBC")
    Jump("loc_F06")

    label("loc_EBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EDC")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F06")

    label("loc_EDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EFC")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F06")

    label("loc_EFC")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F06")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0016
    ChrTalk(
        0xE,
        "#01802Fあ、みなさん。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#00000Fこっちは荷解きが\x01",
            "終わったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xE,
        (
            "#01802Fええ、そうなんですけど……\x02\x03",

            "#01809Fシュリちゃんが今日、\x01",
            "初めて水遊びをするらしくて\x01",
            "ちょっと緊張しているみたいで。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    #C0019
    ChrTalk(
        0xF,
        "#04211Fちょ、ちょっとリーシャ姉っ！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        (
            "#00302Fハハ、隠したからって\x01",
            "どうなるもんでもねえだろ、\x01",
            "シュリぞう。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xF,
        (
            "#04205Fシュ、シュリぞうって……\x01",
            "いきなりヘンな呼び方すんなよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#00309Fハハ、いいじゃねえか。\x01",
            "ティオすけ、ヨナ公、キー坊ときたら\x01",
            "次はやっぱりシュリぞうだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xF,
        (
            "#04206Fし、知るかっ！\x01",
            "だろ？　じゃねーよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、まあ泳げないなら\x01",
            "彼女に手取り足取り\x01",
            "教えてもらえばいいじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xE,
        (
            "#01802Fうん、それにシュリちゃんなら\x01",
            "きっと覚えるのも早いと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xF,
        (
            "#04203Fフ、フン、分かってるって。\x02\x03",

            "#04208Fただその、色々と心の準備がさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#00009Fはは、まあ覚悟ができたら\x01",
            "リーシャと一緒に来るといいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x15A, 4)
    Return()

    # Function_6_D2B end

    def Function_7_129C(): pass

    label("Function_7_129C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_12AD")
    Jump("loc_151B")

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_12BB")
    Jump("loc_151B")

    label("loc_12BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_12C9")
    Jump("loc_151B")

    label("loc_12C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_12D7")
    Jump("loc_151B")

    label("loc_12D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12E5")
    Jump("loc_151B")

    label("loc_12E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_12F3")
    Jump("loc_151B")

    label("loc_12F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_151B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130E")
    Call(0, 9)
    Jump("loc_151B")

    label("loc_130E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1480")

    #C0028
    ChrTalk(
        0xD,
        (
            "#01704F以前、外国の雑誌で見てから\x01",
            "ビーチで思いっきり遊ぶのが\x01",
            "夢だったのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#00309F個人的には、イリアさんたちの\x01",
            "水着姿が楽しみッス！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xD,
        (
            "#01705Fああ、湖水浴場の受付で\x01",
            "水着を貸し出してるのよね。\x02\x03",

            "#01709Fよーし、こうなったら\x01",
            "超ド派手でセクシーなのを\x01",
            "選んじゃおうかしら！\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 0xFF)

    #C0031
    ChrTalk(
        0xC,
        (
            "#05909Fふふ、イリアったら。\x01",
            "ほどほどなのにしなさいよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1, 0)
    Jump("loc_151B")

    label("loc_1480")


    #C0032
    ChrTalk(
        0xD,
        (
            "#01709Fフフ、楽しみにしてなさい。\x01",
            "超ド派手でセクシーな水着を\x01",
            "選んじゃうから！\x02\x03",

            "#01702Fそんじゃ、さっさと準備を済ませて\x01",
            "念願のビーチへレッツらゴーね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151B")

    TalkEnd(0xFE)
    Return()

    # Function_7_129C end

    def Function_8_151F(): pass

    label("Function_8_151F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1530")
    Jump("loc_16F2")

    label("loc_1530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_153E")
    Jump("loc_16F2")

    label("loc_153E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_154C")
    Jump("loc_16F2")

    label("loc_154C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_155A")
    Jump("loc_16F2")

    label("loc_155A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1568")
    Jump("loc_16F2")

    label("loc_1568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1576")
    Jump("loc_16F2")

    label("loc_1576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_16F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1591")
    Call(0, 9)
    Jump("loc_16F2")

    label("loc_1591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167A")

    #C0033
    ChrTalk(
        0xC,
        (
            "#05900Fあ、ロイド。\x01",
            "そろそろ準備は済んだかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#00000Fああ、一応ね。\x02\x03",

            "#00004F先に行ってるから、セシル姉たちは\x01",
            "後からゆっくり来るといいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xC,
        (
            "#05902Fふふ、分かった。\x01",
            "なるべく遅すぎないように行くわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_16F2")

    label("loc_167A")


    #C0036
    ChrTalk(
        0xC,
        (
            "#05904Fイリアったら本当に\x01",
            "相変わらずなんだから。\x02\x03",

            "#05902Fふふ、アルカンシェルの人たちも\x01",
            "さぞ苦労してるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F2")

    TalkEnd(0xFE)
    Return()

    # Function_8_151F end

    def Function_9_16F6(): pass

    label("Function_9_16F6")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0037
    ChrTalk(
        0xC,
        (
            "#05909Fそれにしても、\x01",
            "イリアとお泊りなんて\x01",
            "子供の頃以来ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xD,
        (
            "#01705Fあ～、そういえばそうね。\x02\x03",

            "#01704Fあたしも練習が忙しくなってから\x01",
            "なかなか会いに行けなかったし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0039
    ChrTalk(
        0xD,
        (
            "#01709Fそうだ、今日は久しぶりに\x01",
            "一緒にお風呂にでも入ろっか？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        (
            "#05905Fええ、別にいいけど……\x02\x03",

            "#05903F部屋についてるバスだと\x01",
            "大人２人は狭くないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xD,
        (
            "#01703Fえー、それがいいんじゃない。\x02\x03",

            "#01709F数年分の成長、しっかりこの手で\x01",
            "確かめさせてもらわないとねっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "#05909Fふふ、イリアったら\x01",
            "相変わらずなんだから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)
    Sleep(50)
    OP_64(0x101)

    #C0043
    ChrTalk(
        0x104,
        (
            "#00306F（むう……\x01",
            "  イリアさんのポジションが\x01",
            "  滅茶苦茶羨ましいんだが。）\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00006F（う、うーん……\x01",
            "  セシル姉は無防備だしなあ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 3)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_16F6 end

    def Function_10_19D7(): pass

    label("Function_10_19D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_19E8")
    Jump("loc_1AC3")

    label("loc_19E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_19F6")
    Jump("loc_1AC3")

    label("loc_19F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1A04")
    Jump("loc_1AC3")

    label("loc_1A04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_1A14")
    Jump("loc_1AC3")

    label("loc_1A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1A22")
    Jump("loc_1AC3")

    label("loc_1A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1A30")
    Jump("loc_1AC3")

    label("loc_1A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1A3E")
    Jump("loc_1AC3")

    label("loc_1A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1AC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A59")
    Call(0, 12)
    Jump("loc_1AC3")

    label("loc_1A59")


    #C0045
    ChrTalk(
        0xB,
        (
            "#06401Fお姉ちゃんったら、\x01",
            "ひどい言い草ですよね～。\x02\x03",

            "#06406Fあたしだって、これでも\x01",
            "警察官なのになあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC3")

    TalkEnd(0xFE)
    Return()

    # Function_10_19D7 end

    def Function_11_1AC7(): pass

    label("Function_11_1AC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1AD8")
    Jump("loc_1E4C")

    label("loc_1AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1AE6")
    Jump("loc_1E4C")

    label("loc_1AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1AF4")
    Jump("loc_1E4C")

    label("loc_1AF4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_1B04")
    Jump("loc_1E4C")

    label("loc_1B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1B12")
    Jump("loc_1E4C")

    label("loc_1B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D06")

    #C0046
    ChrTalk(
        0x12,
        (
            "#10103Fう～ん、あたしは\x01",
            "待ち合わせ時間までどうしてましょう。\x02\x03",

            "#10108Fフランと一緒にブティックに行っても\x01",
            "良かったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#00005Fん、何か問題でもあるのか？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x12,
        (
            "#10111Fえ、えっと実は、その……\x02\x03",

            "#10109Fビーチで見たセシルさんたちの\x01",
            "プロポーションに、ちょっと\x01",
            "敗北感を感じちゃったっていうか。\x02\x03",

            "#10106F彼女たちの前で服を選んだり\x01",
            "試着したりするのは、\x01",
            "どうも気が進まなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#00003F（う、う～ん、\x01",
            "  考えすぎだと思うけど……\x01",
            "  女性同士だとあり得るのかな？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1DAD")

    label("loc_1D06")


    #C0050
    ChrTalk(
        0x12,
        (
            "#10106Fセシルさんたちの前で\x01",
            "服を選んだり試着したりするのは、\x01",
            "どうも気が進まないというか……\x02\x03",

            "#10100Fあたしはあとで、ランディ先輩のいる\x01",
            "宝飾店にでも行ってみます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAD")

    Jump("loc_1E4C")

    label("loc_1DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1DC0")
    Jump("loc_1E4C")

    label("loc_1DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DDB")
    Call(0, 12)
    Jump("loc_1E3E")

    label("loc_1DDB")


    #C0051
    ChrTalk(
        0x12,
        (
            "#10106Fはあ、一杯食わされた感じです。\x02\x03",

            "#10101Fこのあたしがフランなんかに\x01",
            "騙されるなんてっ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E3E")

    Jump("loc_1E4C")

    label("loc_1E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1E4C")

    label("loc_1E4C")

    TalkEnd(0xFE)
    Return()

    # Function_11_1AC7 end

    def Function_12_1E50(): pass

    label("Function_12_1E50")

    OP_4B(0x12, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0052
    ChrTalk(
        0x12,
        (
            "#10101Fもう、フランったら……\x01",
            "昨日は来る気配なんて\x01",
            "全然見せてなかったじゃない。\x02\x03",

            "#10106F『仕事がなければ行くのに』とか\x01",
            "『お姉ちゃんが羨ましい～』とか\x01",
            "言っちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "#06402Fえへっ、ごめんね～。\x01",
            "招待自体はお姉ちゃんと\x01",
            "同じ頃に受けたんだけど……\x02\x03",

            "#06409Fマリアベルさんから\x01",
            "当日まで黙っているように\x01",
            "口止めされちゃってたんだ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x12,
        (
            "#10106Fはあ、このあたしが\x01",
            "フランなんかに騙されるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        "#06405Fあっ、ひど～いお姉ちゃん！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0x12, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_12_1E50 end

    def Function_13_2025(): pass

    label("Function_13_2025")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_2036")
    Jump("loc_21E8")

    label("loc_2036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2044")
    Jump("loc_21E8")

    label("loc_2044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2052")
    Jump("loc_21E8")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2060")
    Jump("loc_21E8")

    label("loc_2060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_208F")

    #C0056
    ChrTalk(
        0x13,
        "#01200Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21E8")

    label("loc_208F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_209D")
    Jump("loc_21E8")

    label("loc_209D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_21DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B9")

    #C0057
    ChrTalk(
        0x13,
        "#01200F……グルルル…………\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        "#00000Fツァイト、ここにいたのか。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#00302Fはは、水上バスの旅が\x01",
            "ちょっと疲れたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x13,
        "#01203F……ウォン。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x105,
        "#10304Fってわけでもなさそうだね。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00000Fまあ、ツァイトも後で\x01",
            "ビーチに来るだろうし\x01",
            "放っておくか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_21DA")

    label("loc_21B9")


    #C0063
    ChrTalk(
        0x13,
        "#01200F……グルルル…………\x02",
    )

    CloseMessageWindow()

    label("loc_21DA")

    Jump("loc_21E8")

    label("loc_21DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_21E8")

    label("loc_21E8")

    TalkEnd(0xFE)
    Return()

    # Function_13_2025 end

    def Function_14_21EC(): pass

    label("Function_14_21EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_21FD")
    Jump("loc_2315")

    label("loc_21FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_220B")
    Jump("loc_2315")

    label("loc_220B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2219")
    Jump("loc_2315")

    label("loc_2219")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2229")
    Jump("loc_2315")

    label("loc_2229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_2237")
    Jump("loc_2315")

    label("loc_2237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_22F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2252")
    Call(0, 15)
    Jump("loc_22EB")

    label("loc_2252")


    #C0064
    ChrTalk(
        0x11,
        (
            "#00203Fみっしぃを知らずに\x01",
            "テーマパークに行こうなんて、\x01",
            "命知らずもいいところです。\x02\x03",

            "#00201Fどうやらシュリさんには\x01",
            "徹底的な教育が必要みたいですね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22EB")

    Jump("loc_2315")

    label("loc_22F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_22FE")
    Jump("loc_2315")

    label("loc_22FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_230C")
    Jump("loc_2315")

    label("loc_230C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_2315")

    label("loc_2315")

    TalkEnd(0xFE)
    Return()

    # Function_14_21EC end

    def Function_15_2319(): pass

    label("Function_15_2319")

    OP_4B(0x11, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0065
    ChrTalk(
        0xF,
        "#04205Fん、その機械についてるのは……？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x11,
        "#00204Fええ、みっしぃのストラップですが。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xF,
        (
            "#04202Fへー、これが話で聞いた\x01",
            "『みっしぃ』ってヤツかあ。\x02\x03",

            "#04204Fそういえば初めて見たかも。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0068
    ChrTalk(
        0x11,
        "#00205F……初めて見た？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xF,
        (
            "#04202Fああ、名前はよく聞いてたんだけど\x01",
            "こういうモンだとは知らなかったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    #C0070
    ChrTalk(
        0x11,
        (
            "#00203F……どうやらシュリさんには\x01",
            "徹底的な教育が必要みたいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0x11, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_15_2319 end

    def Function_16_24D7(): pass

    label("Function_16_24D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_24E8")
    Jump("loc_2654")

    label("loc_24E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_24F6")
    Jump("loc_2654")

    label("loc_24F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D1")

    #C0071
    ChrTalk(
        0xFE,
        (
            "本日、ＶＩＰフロアは\x01",
            "皆様の貸切になっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "また、各種ルームサービスは\x01",
            "マリアベル様のご厚意で\x01",
            "無償で提供されています。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "どうぞ、何なりと気兼ねなく\x01",
            "お申し付けくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2654")

    label("loc_25D1")


    #C0074
    ChrTalk(
        0xFE,
        (
            "各種ルームサービスは\x01",
            "マリアベル様のご厚意で\x01",
            "無償で提供されています。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "どうぞ、何なりと気兼ねなく\x01",
            "お申し付けくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2654")

    TalkEnd(0xFE)
    Return()

    # Function_16_24D7 end

    def Function_17_2658(): pass

    label("Function_17_2658")

    Call(0, 18)
    Return()

    # Function_17_2658 end

    def Function_18_265C(): pass

    label("Function_18_265C")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_266D")
    Jump("loc_282F")

    label("loc_266D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_2798")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2726")

    #C0076
    ChrTalk(
        0x9,
        (
            "皆様、ビーチでは\x01",
            "いかがお過ごしでしたかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "私もオフの日には、\x01",
            "ビーチで日光浴などを\x01",
            "楽しんでいるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "ふふ、近いうちに\x01",
            "また行きませんとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2793")

    label("loc_2726")


    #C0079
    ChrTalk(
        0x9,
        (
            "私もオフの日には、\x01",
            "ビーチで日光浴などを\x01",
            "楽しんでいるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "ふふ、近いうちに\x01",
            "また行きませんとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2793")

    Jump("loc_282F")

    label("loc_2798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_282F")

    #C0081
    ChrTalk(
        0x9,
        (
            "こちらは、ＶＩＰフロア専用の\x01",
            "バーカウンターとなっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "各種カクテル、ソフトドリンクなども\x01",
            "ご用意してますのでお気軽にどうぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_282F")

    TalkEnd(0x9)
    Return()

    # Function_18_265C end

    def Function_19_2833(): pass

    label("Function_19_2833")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05500.itc", 0x24)
    SoundLoad(3801)
    SoundLoad(3771)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0xD, 9970, 0, 11960, 90)
    SetChrPos(0xC, 8910, 0, 12550, 90)
    SetChrPos(0xE, 8960, 0, 11180, 90)
    SetChrPos(0xF, 7880, 0, 11840, 90)
    SetChrPos(0x14, 1690, 0, 5920, 270)
    SetChrPos(0x109, 2590, 0, 7310, 225)
    SetChrPos(0xB, 3500, 0, 5840, 225)
    SetChrPos(0x102, 4019, 0, 7340, 225)
    SetChrPos(0x103, 4150, 0, 8660, 225)
    SetChrPos(0xA, 5460, 0, 7210, 225)
    SetChrPos(0x101, 5510, 0, 8830, 180)
    SetChrPos(0x104, 6640, 0, 9950, 180)
    SetChrPos(0x105, 5200, 0, 10210, 180)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0xA)
    OP_68(7450, 1700, 8400, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(27000, 5000)
    FadeToBright(1000, 0)
    BeginChrThread(0xD, 3, 0, 20)
    BeginChrThread(0xC, 3, 0, 21)
    BeginChrThread(0xE, 3, 0, 22)
    BeginChrThread(0xF, 3, 0, 23)
    BeginChrThread(0x14, 3, 0, 24)
    BeginChrThread(0x109, 3, 0, 25)
    BeginChrThread(0xB, 3, 0, 26)
    BeginChrThread(0x102, 3, 0, 27)
    BeginChrThread(0x103, 3, 0, 28)
    BeginChrThread(0xA, 3, 0, 29)
    BeginChrThread(0x101, 3, 0, 30)
    BeginChrThread(0x105, 3, 0, 31)
    BeginChrThread(0x104, 3, 0, 32)
    Sleep(200)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sleep(4000)
    OP_0D()
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0xD, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x14, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0xA, 0x3)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0x104, 0x3)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x14, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    Sound(121, 0, 100, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_2B2D")
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0083
    AnonymousTalk(
        0x14,
        "#02902F#3801V#30Wここが皆さんのお部屋ですわ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xED9)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Jump("loc_2B6B")

    label("loc_2B2D")

    SetMessageWindowPos(-1, -1, -1, -1)

    #A0084
    AnonymousTalk(
        0x14,
        "#02902Fここが皆さんのお部屋ですわ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_2B6B")

    OP_68(-100000, 1000, -81500, 0)
    MoveCamera(318, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x14, -100000, 0, -78000, 180)
    SetChrPos(0x101, -100000, 0, -80300, 180)
    SetChrPos(0x104, -99000, 0, -80000, 180)
    SetChrPos(0x105, -101000, 0, -80100, 180)
    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x5)
    FadeToBright(1000, 0)
    OP_68(-100000, 1000, -79000, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0085
    ChrTalk(
        0x101,
        "#00011F#11Pこれは凄いな……\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x87, 0x1F4)
    Sleep(100)

    #C0086
    ChrTalk(
        0x104,
        "#00309F#5Pは～、豪勢すぎんだろ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0xE1, 0x1F4)
    Sleep(100)

    #C0087
    ChrTalk(
        0x105,
        (
            "#10302F#11P僕たちに合わせてベッドの数も\x01",
            "調整してくれたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x14,
        (
            "#02904F#11Pうふふ、高級ホテルならば\x01",
            "当然のサービスですわ。\x02\x03",

            "#02901Fまあ、この部屋に関しては\x01",
            "外からも鍵がかかるように\x01",
            "しておきたかったのですけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_2D76():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D76)
    Sleep(50)

    def lambda_2D86():
        TurnDirection(0x104, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2D86)
    Sleep(50)

    def lambda_2D96():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2D96)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0089
    ChrTalk(
        0x101,
        "#00012F#6Pそ、それって……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        "#00306F#6Pそんな信用ないッスかねぇ。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x105,
        (
            "#10304F#6Pフフ、心外だなぁ。\x02\x03",

            "#10302Fいくら僕たち以外は全員、\x01",
            "麗しい女性たちだからってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x14,
        (
            "#02906F#11Pまあ、ワジさんに関しては\x01",
            "何となく信用できそうですけど。\x02\x03",

            "#02913Fロイドさんとランディさんは\x01",
            "正直、信用しきれませんから。\x02\x03",

            "#02901F……特にロイドさんは\x01",
            "要注意・危険人物ですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00011F#6Pええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x105,
        (
            "#10309F#6Pフフ、どうせ君のことだから\x01",
            "ふと夜中にラウンジに出てみたら\x01",
            "眠れない女の子がいて……\x02\x03",

            "#10302Fそれで話しているうちに\x01",
            "イイ雰囲気になりそうだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        "#00309F#6Pおお、いかにもありそうだなー。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0096
    ChrTalk(
        0x14,
        (
            "#02909F#11P……ロイドさん。\x01",
            "従業員用の仮眠室あたりに\x01",
            "泊まっていただけるかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)

    #C0097
    ChrTalk(
        0x101,
        "#00012F#6Pいや、ありませんから！\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x14,
        (
            "#02906F#11Pフン、まったく。\x02\x03",

            "#02904Fちなみにわたくしは\x01",
            "この後、取締役会がありますから\x01",
            "いったん街へ戻りますけど……\x02\x03",

            "くれぐれも、水着姿のエリィたちに\x01",
            "劣情を催さないよう注意なさい。\x02\x03",

            "#02901F……悪さをしたら保安部を呼んで\x01",
            "湖の真ん中に叩き込みますわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00006F#6Pだからしませんって……\x02\x03",

            "#00001F……でも、マリアベルさん、\x01",
            "やっぱり相当お忙しいんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x14,
        (
            "#02904F#11Pフフ、お父様があんな事を\x01",
            "言い出してしまいましたから。\x02\x03",

            "#02902FさすがにＩＢＣの業務を\x01",
            "並行する事が難しくなったようで\x01",
            "全て取締役会で引き取りました。\x02\x03",

            "当然わたくしにも\x01",
            "シワ寄せが回ってきてる訳ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#00003F#6Pそうですか……\x01",
            "本当にお疲れさまです。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#00302F#6Pま、適当に\x01",
            "息抜きもしてくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x105,
        (
            "#10300F#6P休息とストレス解消は\x01",
            "美容と健康にもいいしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x14,
        (
            "#02904F#11Pフフ、お気遣い感謝しますわ。\x02\x03",

            "#02900Fお伝えしたように、湖水浴場の受付は\x01",
            "１Ｆアーケードの右翼方面にあります。\x02\x03",

            "そこで水着もレンタルできるので\x01",
            "更衣室で着替えてくださいな。\x02\x03",

            "#02901F……もちろん男子の方ですわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        "#00012F#6Pいや、念を押さなくても。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        "#00309F#6Pとにかく了解ッス。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x14,
        (
            "#02904F#11P湖水浴場は皆さんのために\x01",
            "昼まで貸し切りにしています。\x02\x03",

            "午後からはテーマパークで\x01",
            "存分に楽しむといいでしょう。\x02\x03",

            "#02902Fそちらは行ったことがある人も\x01",
            "多いでしょうからお任せしますわ。\x02\x03",

            "#02909Fそれと夜は、迎賓館の方に\x01",
            "ディナーの席を用意しています。\x02\x03",

            "正装の必要はありませんから\x01",
            "時間までに来てください。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00000F#6P分かりました。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x105,
        (
            "#10304F#6P至れり尽くせりで\x01",
            "申しわけないくらいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x14,
        "#02904F#11Pフフ、どう致しまして。\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x0, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_36F2")
    OP_C9(0x0, 0x80000000)

    #C0111
    ChrTalk(
        0x14,
        (
            "#02911F#3771V#5P#40W──よき滞在を#10R㈲　㈲　㈲　㈲　㈲#。\x01",
            "存分に羽を伸ばして下さいな。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEBB)
    OP_C9(0x1, 0x80000000)
    Jump("loc_372F")

    label("loc_36F2")


    #C0112
    ChrTalk(
        0x14,
        (
            "#02902F#5P──よき滞在を。\x01",
            "存分に羽を伸ばして下さいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_372F")

    OP_57(0x0)
    OP_5A()

    def lambda_3737():

        label("loc_3737")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3737")

    QueueWorkItem2(0x101, 2, lambda_3737)

    def lambda_3749():

        label("loc_3749")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_3749")

    QueueWorkItem2(0x104, 2, lambda_3749)

    def lambda_375B():

        label("loc_375B")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_375B")

    QueueWorkItem2(0x105, 2, lambda_375B)

    def lambda_376D():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_376D)
    Sleep(1000)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x14, 1)
    Sleep(300)
    Sound(890, 0, 100, 0)
    OP_74(0x7, 0xF)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_74(0x7, 0x1E)
    SetMapObjFlags(0x7, 0x10)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    OP_68(-100000, 1000, -80000, 2000)
    OP_6F(0x79)

    #C0113
    ChrTalk(
        0x101,
        (
            "#00002F#6P……何だかんだ言って\x01",
            "すごく親切な人なんだよな。\x02\x03",

            "#00006F妙に敵視してくるのは\x01",
            "勘弁して欲しいけど……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_384C():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_384C)
    Sleep(50)

    def lambda_385C():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_385C)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    Sleep(100)

    #C0114
    ChrTalk(
        0x104,
        (
            "#00304F#12Pま、運命と思って諦めろ。\x02\x03",

            "#00302Fそれじゃあ早速、\x01",
            "ビーチに行ってみるかね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x105,
        (
            "#10304F#5Pフフ、そうだね。\x02\x03",

            "#10300F女性陣はどうしても準備に\x01",
            "時間がかかるだろうし……\x02\x03",

            "先に行ってもいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        (
            "#00004F#6Pそうだな……\x02\x03",

            "#00000Fそれじゃあ一応、\x01",
            "声をかけて行くとするか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_49()
    OP_D7(0x24)
    SetMapObjFlags(0x0, 0x10)
    SetChrPos(0x0, -100000, 0, -80000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x8, 0xFF)
    SetScenarioFlags(0x144, 5)
    OP_29(0xA5, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_19_2833 end

    def Function_20_3A24(): pass

    label("Function_20_3A24")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_20_3A24 end

    def Function_21_3A34(): pass

    label("Function_21_3A34")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_21_3A34 end

    def Function_22_3A44(): pass

    label("Function_22_3A44")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_22_3A44 end

    def Function_23_3A54(): pass

    label("Function_23_3A54")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_23_3A54 end

    def Function_24_3A64(): pass

    label("Function_24_3A64")

    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1F40, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_24_3A64 end

    def Function_25_3A92(): pass

    label("Function_25_3A92")

    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2134, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_25_3A92 end

    def Function_26_3ACF(): pass

    label("Function_26_3ACF")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1194, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1F40, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_26_3ACF end

    def Function_27_3B0C(): pass

    label("Function_27_3B0C")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xED8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_27_3B0C end

    def Function_28_3B49(): pass

    label("Function_28_3B49")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_28_3B49 end

    def Function_29_3B86(): pass

    label("Function_29_3B86")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_29_3B86 end

    def Function_30_3BC3(): pass

    label("Function_30_3BC3")

    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x14B4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_30_3BC3 end

    def Function_31_3C0F(): pass

    label("Function_31_3C0F")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_31_3C0F end

    def Function_32_3C5B(): pass

    label("Function_32_3C5B")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2134, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_32_3C5B end

    def Function_33_3CA7(): pass

    label("Function_33_3CA7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(3396)
    SetChrPos(0x101, -100500, 0, -80500, 90)
    SetChrPos(0x104, -99000, 0, -81000, 270)
    SetChrPos(0x105, -101000, 0, -85000, 0)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -100000, 0, -74900, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("エリィの声")

    #A0117
    AnonymousTalk(
        0xFF,
        "#3396V#30Wごめんなさい、ちょっといい？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD44)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    PlayBGM("ed7111", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7565", "ed7111")
    OP_68(-100000, 1000, -78300, 0)
    MoveCamera(320, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(22000, 1500)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_6F(0x79)
    OP_0D()
    Sound(121, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)

    def lambda_3E15():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E15)
    Sleep(50)

    def lambda_3E25():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3E25)
    OP_79(0x7)
    OP_68(-100000, 1000, -79300, 2000)

    def lambda_3E46():
        OP_9B(0x0, 0xFE, 0x0, 0xC1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3E46)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)

    #C0118
    ChrTalk(
        0x101,
        "#00002F#6Pああ、エリィか。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x104,
        "#00302F#6Pもう出んのか？\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x10,
        (
            "#00102F#11Pええ、イリアさんたちに誘われて\x01",
            "ショップを覗いてからテーマパークに\x01",
            "行くつもりだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x87, 0x1F4)
    Sleep(600)
    OP_93(0x10, 0xE1, 0x1F4)
    Sleep(600)
    OP_93(0x10, 0xB4, 0x1F4)

    #C0121
    ChrTalk(
        0x10,
        (
            "#00105F#11Pその、キーアちゃん、\x01",
            "こっちに訪ねて来なかった？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#00005F#6Pキーアが？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        "#00305F#6Pなんだ、キー坊がどうした？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x10,
        (
            "#00106F#11Pそれが、ついさっき\x01",
            "『ロイドの所に行ってくる』って\x01",
            "部屋を出ていったんだけど……\x02\x03",

            "#00108Fうーん、どこに行ったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#00001F#6Pそうなのか……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#00300F#6Pティオすけかツァイトと\x01",
            "一緒にいるんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x10,
        (
            "#00104F#11Pええ、そうかもしれないわ。\x02\x03",

            "#00102Fごめんなさい。\x01",
            "もうちょっと探してみるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        (
            "#00005F#6Pああ、ちょっと待った。\x02\x03",

            "#00000Fイリアさんたちを\x01",
            "待たせているんだろう？\x02\x03",

            "キーアは俺が探しておくから\x01",
            "エリィはそっちに行ってくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x10,
        "#00105F#11Pえ、でも……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#00004F#6Pずっとエリィたちに\x01",
            "任せきりなのも悪いしさ。\x02\x03",

            "#00002Fちゃんと見つけて\x01",
            "テーマパークに連れて行くよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x10,
        (
            "#00106F#11Pうーん。\x01",
            "それじゃあお願いするわね。\x02\x03",

            "#00108F……はぁ。\x01",
            "キーアちゃんにも新しい服を\x01",
            "見てあげたかったんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x1F4)

    def lambda_4299():
        OP_9B(0x0, 0xFE, 0x0, 0xC1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4299)
    Sleep(1000)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x10, 1)
    SetChrFlags(0x10, 0x80)
    Sound(890, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_68(-100000, 1000, -80000, 1500)
    OP_6F(0x79)
    OP_93(0x104, 0x10E, 0x1F4)

    #C0132
    ChrTalk(
        0x104,
        (
            "#00309F#12Pはは、キー坊も\x01",
            "相変わらずモテモテだな。\x02\x03",

            "#00300Fそんじゃ早速、捜してみるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0133
    ChrTalk(
        0x101,
        (
            "#00000F#5Pああ、俺一人で十分だよ。\x02\x03",

            "ランディもショップを\x01",
            "覗きたいって言ってただろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#00305F#12Pそうか？\x02\x03",

            "#00304Fそんじゃ、下の宝飾店にいるから\x01",
            "何かあったら声をかけてくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 0)), scpexpr(EXPR_END)), "loc_443B")

    #C0135
    ChrTalk(
        0x101,
        "#00002F#5Pああ、分かった。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4675")

    label("loc_443B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_455D")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0136
    ChrTalk(
        0x101,
        (
            "#00005F#5P宝飾店って……\x01",
            "たしか会員限定の？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        (
            "#00302F#12Pああ、何でも\x01",
            "マリアベルお嬢さんの口利きで\x01",
            "俺たちでも入れるらしいぜ？\x02\x03",

            "#00304F店員は微妙にムカつくが\x01",
            "品揃えには興味あるしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#00002F#5Pそっか、分かった。\x01",
            "（ちょっと覗いてみようかな？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4675")

    label("loc_455D")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0139
    ChrTalk(
        0x101,
        (
            "#00005F#5P宝飾店って……\x01",
            "下のアーケードにある？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x104,
        (
            "#00302F#12Pああ、何でも\x01",
            "マリアベルお嬢さんの口利きで\x01",
            "俺たちでも入れるらしいぜ？\x02\x03",

            "#00304Fお高く止まってやがるが\x01",
            "品揃えには興味あるしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#00002F#5Pそっか、分かった。\x01",
            "（ちょっと覗いてみようかな？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4675")

    OP_68(-100000, 1000, -78500, 5000)

    def lambda_468B():

        label("loc_468B")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_468B")

    QueueWorkItem2(0x101, 2, lambda_468B)
    OP_93(0x104, 0x0, 0x1F4)

    def lambda_46A4():
        OP_95(0xFE, -100000, 0, -76900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_46A4)
    WaitChrThread(0x104, 1)
    Sound(121, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    OP_93(0x104, 0x0, 0x0)

    def lambda_46E2():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_46E2)
    Sleep(500)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x104, 1)
    Sound(890, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    EndChrThread(0x101, 0x2)
    OP_6F(0x79)

    #C0142
    ChrTalk(
        0x101,
        (
            "#00004F#6Pさてと、キーアを探すか。\x02\x03",

            "#00008F多分、ホテルの中からは\x01",
            "出てないと思うんだけど……\x02\x03",

            "#00001Fもし見つからなかったら、\x01",
            "他の場所も捜す必要があるな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_74(0x7, 0x1E)
    SetMapObjFlags(0x7, 0x10)
    ClearChrFlags(0x105, 0x8)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    SetChrPos(0x0, -100000, 0, -80000, 0)
    SetScenarioFlags(0x145, 1)
    OP_29(0xA5, 0x1, 0x4)
    SubItemNumber(0x329, 10)
    SubItemNumber(0x32B, 10)
    SubItemNumber(0x32C, 10)
    EventEnd(0x5)
    Return()

    # Function_33_3CA7 end

    SaveToFile()

Try(main)
