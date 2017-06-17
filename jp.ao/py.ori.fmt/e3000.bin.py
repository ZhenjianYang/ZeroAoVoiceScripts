from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3000.bin",                # FileName
        "e3000",                    # MapName
        "e3000",                    # Location
        0x00A1,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 1, 0, 2],
    )

    BuildStringList((
        "e3000",                  # 0
        "ティオ",                 # 1
        "ツァイト",               # 2
        "ワジ",                   # 3
        "キーア",                 # 4
        "観光客",                 # 5
        "観光客",                 # 6
        "マリアベル",             # 7
    ))

    AddCharChip((
        "chr/ch00200.itc",                   # 00
        "chr/ch02707.itc",                   # 01
        "chr/ch03002.itc",                   # 02
        "chr/ch08200.itc",                   # 03
        "chr/ch24502.itc",                   # 04
        "chr/ch21302.itc",                   # 05
        "chr/ch00000.itc",                   # 06
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    404,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    388,  0x0, 0,   2,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2210,    4250,    899,     180,  453,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(1029,    4250,    899,     180,  453,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(580, 0)                                        # 0

    ScpFunction((
        "Function_0_244",          # 00, 0
        "Function_1_2F4",          # 01, 1
        "Function_2_408",          # 02, 2
        "Function_3_475",          # 03, 3
        "Function_4_AA2",          # 04, 4
        "Function_5_D10",          # 05, 5
        "Function_6_D2E",          # 06, 6
        "Function_7_103E",         # 07, 7
        "Function_8_115D",         # 08, 8
        "Function_9_11CA",         # 09, 9
        "Function_10_2719",        # 0A, 10
        "Function_11_2739",        # 0B, 11
        "Function_12_2759",        # 0C, 12
        "Function_13_2F59",        # 0D, 13
        "Function_14_30FE",        # 0E, 14
        "Function_15_3DCC",        # 0F, 15
        "Function_16_3DE3",        # 10, 16
        "Function_17_3E67",        # 11, 17
        "Function_18_3E8D",        # 12, 18
        "Function_19_3EA4",        # 13, 19
        "Function_20_3ECA",        # 14, 20
        "Function_21_3EF7",        # 15, 21
        "Function_22_3F09",        # 16, 22
        "Function_23_3F14",        # 17, 23
        "Function_24_3F33",        # 18, 24
        "Function_25_3F52",        # 19, 25
        "Function_26_4065",        # 1A, 26
        "Function_27_4FE5",        # 1B, 27
        "Function_28_500B",        # 1C, 28
    ))


    def Function_0_244(): pass

    label("Function_0_244")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_27C"),
        (1, "loc_288"),
        (2, "loc_294"),
        (3, "loc_2A0"),
        (4, "loc_2AC"),
        (5, "loc_2B8"),
        (6, "loc_2C4"),
        (SWITCH_DEFAULT, "loc_2D0"),
    )


    label("loc_27C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_288")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_294")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2DC")

    label("loc_2F3")

    Return()

    # Function_0_244 end

    def Function_1_2F4(): pass

    label("Function_1_2F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38A")
    SetChrPos(0x8, -500, 4100, 11000, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 1000, 4100, 11000, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -2250, 4250, -2100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x1)

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AE")
    SetChrPos(0xB, 3000, 4100, -8000, 180)
    ClearChrFlags(0xB, 0x80)

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3C8")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 9)
    Jump("loc_3EE")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3DF")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 1)
    Event(0, 25)
    Jump("loc_3EE")

    label("loc_3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_3EE")
    ClearScenarioFlags(0x22, 2)
    Event(0, 26)

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_407")
    Event(0, 13)

    label("loc_407")

    Return()

    # Function_1_2F4 end

    def Function_2_408(): pass

    label("Function_2_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_422")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_43A")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_43A")
    SetScenarioFlags(0x0, 1)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_44E")
    OP_24(0x1DF)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_454")

    label("loc_44E")

    Sound(479, 1, 100, 0)

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_474")
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_474")

    Return()

    # Function_2_408 end

    def Function_3_475(): pass

    label("Function_3_475")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_486")
    Jump("loc_A9E")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_494")
    Jump("loc_A9E")

    label("loc_494")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_A9E")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4B2")
    Jump("loc_A9E")

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4C0")
    Jump("loc_A9E")

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4CE")
    Jump("loc_A9E")

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4DC")
    Jump("loc_A9E")

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4EA")
    Jump("loc_A9E")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_A9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0D")

    #C0001
    ChrTalk(
        0x8,
        (
            "#00204Fこほん、とにかく……\x01",
            "今日は久しぶりの休暇を\x01",
            "楽しめるといいですね。\x02\x03",

            "#00200F前は『競売会』の調査もあって、\x01",
            "楽しんでいる時間はほとんど\x01",
            "ありませんでしたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#00004F確かに、ミシュラムに\x01",
            "ちゃんと遊びに行くのは\x01",
            "今回が初めてだったな。\x02\x03",

            "#00009Fはは、やっぱり\x01",
            "ティオのお目当ては\x01",
            "テーマパークなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#00204Fモチのロンです。\x02\x03",

            "《ミシュラム・ワンダーランド》\x01",
            "（MICHLLAM WONDER LAND）……\x02\x03",

            "――略してＭ・Ｗ・Ｌ。\x02\x03",

            "#00202Fみっしぃに会えるのが楽しみです。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_8F2")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0004
    ChrTalk(
        0x101,
        (
            "#00004F……そういえば、その。\x01",
            "例の『約束』の話、覚えてるか？\x02\x03",

            "#00002F教団事件が終わった後、\x01",
            "折を見てテーマパークに\x01",
            "遊びに行くって話だったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#00204F……もちろん、覚えています。\x02\x03",

            "『まずは支援課のみんなで……\x01",
            "  その後、ロイドさんとわたしで。』\x02\x03",

            "#00200Fそういう意味では、今回の招待で\x01",
            "ようやく第１フェイズに移行した、\x01",
            "と言っていいでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00009Fはは、言い回しの意味は\x01",
            "よくわかんないけど……\x02\x03",

            "#00000F今度は近いうちに、\x01",
            "絶対に２人で来なくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#00209Fふふっ……\x01",
            "ええ、楽しみにしています。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A05")

    label("loc_8F2")


    #C0008
    ChrTalk(
        0x101,
        (
            "#00004Fティオはみっしぃについて\x01",
            "特別詳しいんだよな。\x02\x03",

            "#00002Fテーマパークについたら、\x01",
            "色々と教えてくれよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#00204F……了解しました。\x02\x03",

            "#00202Fでは、まずはロイドさんに\x01",
            "みっしぃ誕生秘話、家族構成などを\x01",
            "徹底的に叩き込んで……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00006Fい、いや、そこまではいいから。\x02",
    )

    CloseMessageWindow()

    label("loc_A05")

    SetScenarioFlags(0x15A, 0)
    Jump("loc_A9E")

    label("loc_A0D")


    #C0011
    ChrTalk(
        0x8,
        (
            "#00202Fみっしぃのことなら、\x01",
            "テーマパークに着いてから\x01",
            "色々と教えて差し上げます。\x02\x03",

            "#00204F今は、皆さんの所に行って\x01",
            "話をしてくるのがいいかと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9E")

    TalkEnd(0xFE)
    Return()

    # Function_3_475 end

    def Function_4_AA2(): pass

    label("Function_4_AA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_AB3")
    Jump("loc_D0C")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_AC1")
    Jump("loc_D0C")

    label("loc_AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_ACF")
    Jump("loc_D0C")

    label("loc_ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_ADD")
    Jump("loc_D0C")

    label("loc_ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_AEB")
    Jump("loc_D0C")

    label("loc_AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_AF9")
    Jump("loc_D0C")

    label("loc_AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B07")
    Jump("loc_D0C")

    label("loc_B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_D0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAD")
    OP_4B(0x8, 0xFF)

    #C0012
    ChrTalk(
        0x9,
        "#01203Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0013
    ChrTalk(
        0x8,
        (
            "#00204F『やれやれ、手がかかるリーダーだ』と\x01",
            "言っているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00012Fはは、ツァイトに言われると\x01",
            "立つ瀬がないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#00211Fあと、『にぶちんすぎる』\x01",
            "『もう少し気が利く男になれ』\x01",
            "とも言っているようです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    #C0016
    ChrTalk(
        0x101,
        (
            "#00006F……それ、なんだか\x01",
            "主観が入ってないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "#00203Fさて、何のことやら。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x0, 4)
    OP_4C(0x8, 0xFF)
    Jump("loc_D0C")

    label("loc_CAD")


    #C0018
    ChrTalk(
        0x9,
        "#01203F……グルルル……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00002F（ツァイトもミシュラムを\x01",
            "  楽しみにしてるのかな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0C")

    TalkEnd(0xFE)
    Return()

    # Function_4_AA2 end

    def Function_5_D10(): pass

    label("Function_5_D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D27")
    Call(0, 14)
    Return()

    label("loc_D27")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_5_D10 end

    def Function_6_D2E(): pass

    label("Function_6_D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D45")
    Call(0, 12)
    Return()

    label("loc_D45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_D56")
    Jump("loc_103A")

    label("loc_D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D64")
    Jump("loc_103A")

    label("loc_D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_D72")
    Jump("loc_103A")

    label("loc_D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_D80")
    Jump("loc_103A")

    label("loc_D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D8E")
    Jump("loc_103A")

    label("loc_D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_D9C")
    Jump("loc_103A")

    label("loc_D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_DAA")
    Jump("loc_103A")

    label("loc_DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_103A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC2")
    Jump("loc_103A")

    label("loc_DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6E")

    #C0020
    ChrTalk(
        0xA,
        (
            "#10304Fさて、ホストの仕事以外で\x01",
            "ミシュラムに来るのも久しぶりだし、\x01",
            "今日は羽を休めさせてもらおうかな。\x02\x03",

            "#10300Fどこかのタイミングで\x01",
            "レストランにでも行くつもりだけど、\x01",
            "君も一杯付き合うかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00003F……あのな、何度も言うようだけど\x01",
            "未成年の飲酒は認められないからな？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xA,
        (
            "#10309Fフフ、カタいことは言いっこなしさ。\x01",
            "もっとハメを外しなよ、君。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00006Fカタいとかヤワいとか、\x01",
            "そういうことじゃないから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_103A")

    label("loc_F6E")


    #C0024
    ChrTalk(
        0xA,
        (
            "#10309Fカタいことは言いっこなしさ。\x01",
            "もっとハメを外しなよ、君。\x02\x03",

            "#10302F何だったら、女の子を落とすための\x01",
            "ホストの基本テクニックを\x01",
            "伝授してあげてもいいんだよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#00006Fば、買収しようとするなよ……\x02",
    )

    CloseMessageWindow()

    label("loc_103A")

    TalkEnd(0xFE)
    Return()

    # Function_6_D2E end

    def Function_7_103E(): pass

    label("Function_7_103E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1159")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10ED")

    #C0026
    ChrTalk(
        0xC,
        (
            "なんか、街じゃみんな\x01",
            "ドクリツがどうとか話してたよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xC,
        (
            "あたしたち、外国からきたから\x01",
            "よくわかんないんだけど……\x01",
            "なんか大変なことなわけ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1159")

    label("loc_10ED")


    #C0028
    ChrTalk(
        0xC,
        (
            "街の人が話してた\x01",
            "ドクリツってなんなのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        (
            "よくわかんないんだけど……\x01",
            "なんか大変なことなわけ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1159")

    TalkEnd(0xFE)
    Return()

    # Function_7_103E end

    def Function_8_115D(): pass

    label("Function_8_115D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_11C6")

    #C0030
    ChrTalk(
        0xD,
        (
            "ねーねー、そんなことより\x01",
            "前の席のあのコ、可愛くない？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xD,
        "逆ナンしちゃう？　しちゃう？\x02",
    )

    CloseMessageWindow()

    label("loc_11C6")

    TalkEnd(0xFE)
    Return()

    # Function_8_115D end

    def Function_9_11CA(): pass

    label("Function_9_11CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    LoadChrToIndex("apl/ch51300.itc", 0x1E)
    LoadChrToIndex("apl/ch51301.itc", 0x1F)
    SoundLoad(479)
    SoundLoad(2674)
    SoundLoad(2675)
    SoundLoad(2676)
    SoundLoad(4108)
    SoundLoad(3054)
    SoundLoad(3060)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis245.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis091.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01200.itp")
    SetChrPos(0x101, -750, 4100, 12500, 0)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1000, 4100, 11000, 0)
    BeginChrThread(0x9, 3, 0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -2250, 4250, -2100, 180)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 4100, 5000, 0)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W通商会議から２週間後──\x01",
            "クロスベル市は静かな熱気に包まれていた。\x02\x03",

            "他の自治州──\x01",
            "レマン、オレド、ノーザンブリアは\x01",
            "アルテリア法国の承認を受けた上で、\x01",
            "国家と同等の主権が認められている。\x02\x03",

            "しかしクロスベル自治州には\x01",
            "帝国・共和国から、緩衝地帯としての\x01",
            "自治権のみが承認されている状態だった。\x02\x03",

            "（ちなみに税収の１０％は、\x01",
            "  “委任統治費”という名目で\x01",
            "  帝国・共和国双方に納められている。）\x02\x03",

            "貿易・金融センターとしての発展と、\x01",
            "それに反比例する政治基盤の脆弱さ──\x02\x03",

            "それは結果的に、外国からの干渉と\x01",
            "マフィアなどの台頭をもたらした。\x02\x03",

            "その歪んだ状況を打破するため\x01",
            "『主権国家として独立する』という\x01",
            "ディーター市長の思い切った提唱に、\x01",
            "多くの市民は共感を覚えたが……\x02\x03",

            "２大国の意向を気にする者も多く、\x01",
            "『独立』の是非についての議論が\x01",
            "あちこちで行われるようになっていた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7515", 0)
    OP_68(0, 4100, -15000, 0)
    MoveCamera(340, 6, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(45000, 0)
    OP_68(0, 4100, 45000, 12000)
    Sound(479, 2, 20, 0)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(200)
    FadeToBright(2000, 0)
    Sleep(10500)
    OP_0D()
    Fade(1000)
    OP_68(-750, 5100, 12500, 0)
    MoveCamera(225, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    SetCameraDistance(21000, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0033
    ChrTalk(
        0x101,
        "#00008F#5P#30W……………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0034
    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W…………はあ……………\x02\x03",

            "#00008F駄目だな、あれから\x01",
            "半月近くも経つのに……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(3052, 255, 80, 0)    #voice#Zeit

    #C0035
    ChrTalk(
        0x9,
        "#01200F#6P#30Wウォン？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    Sleep(100)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    #C0036
    ChrTalk(
        0x101,
        (
            "#00012F#11P#30Wゴメン、溜息なんかついて。\x02\x03",

            "#00008F……なあ、ツァイト。\x02\x03",

            "こんな時にリーダーって\x01",
            "何をしてやればいいのかな？\x02\x03",

            "ランディはもちろん、\x01",
            "エリィやノエルも考えごとを\x01",
            "しているみたいだし……\x02\x03",

            "#00006F……キーアにも気を\x01",
            "遣わせてるみたいなんだよな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0037
    AnonymousTalk(
        0x9,
        (
            "#3054V#30Wウォン。\x02\x03",

            "#3060V#40Wグルルルルル……ウォン。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xBF4)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    #C0038
    ChrTalk(
        0x101,
        (
            "#00005F#11P#30Wえっと……\x01",
            "何て言ってるんだ？\x02\x03",

            "#00012Fハハ、ゴメンな。\x01",
            "こちらから振っといて……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x8, 0x8)
    OP_C9(0x0, 0x80000000)

    #N0039
    NpcTalk(
        0xA,
        "少女の声",
        (
            "#2674V#5P#N#30W#35A『こういう時は\x01",
            "  理屈で考えるな。』\x02\x03",

            "#2675V#25A『自分から動いて\x01",
            "  話してみるがいい。』\x02\x03",

            "#4108V#N#15A──だそうです。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_68(-350, 5100, 11350, 2500)
    OP_9B(0x0, 0x8, 0x0, 0x1194, 0x7D0, 0x0)
    OP_6F(0x79)

    #C0040
    ChrTalk(
        0x101,
        "#00005F#12Pティオ……\x02",
    )

    CloseMessageWindow()
    OP_68(-1350, 5100, 12250, 2500)
    MoveCamera(210, 23, 0, 2500)
    SetCameraDistance(19330, 2500)

    def lambda_1BAF():

        label("loc_1BAF")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1BAF")

    QueueWorkItem2(0x101, 2, lambda_1BAF)
    OP_96(0x8, 0xFFFFF894, 0x1004, 0x2F76, 0x7D0, 0x0)
    EndChrThread(0x101, 0x2)
    OP_6F(0x79)
    SetCameraDistance(18360, 20000)
    Sound(2676, 255, 80, 0)    #voice#Tio
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0041
    AnonymousTalk(
        0x8,
        (
            "#30W……いい風ですね。\x02\x03",

            "せっかくの休暇#4Rバカンス#ですし\x01",
            "晴れて本当によかったです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0042
    ChrTalk(
        0x101,
        (
            "#00004F#5Pそうだな……\x02\x03",

            "#00000Fマリアベルさんに招待された時は\x01",
            "何事かと思ったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#00202F#5Pふふ、何かの罠と思ったとか？\x02\x03",

            "いまだにちょっと\x01",
            "敵視されているみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#00012F#5Pハハ、実はちょっと思った。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0045
    ChrTalk(
        0x101,
        (
            "#00006F#5P……ゴメンな、ティオも。\x02\x03",

            "#00008F帰ってきたばかりなのに\x01",
            "こんな情けない所を見せて。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#00206F#5P……無理もないと思います。\x02\x03",

            "#00208F目の前であれだけの人が\x01",
            "亡くなったんですから……\x02\x03",

            "#00200F普通ならショックだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#00003F#5Pいや、捜査官になった以上、\x01",
            "どこかで覚悟していたことだ。\x02\x03",

            "#00001F……ヨアヒムの件もあったから\x01",
            "何とか慣れたつもりだったけど……\x02\x03",

            "#00006F捜査官としても、リーダーとしても\x01",
            "まだまだ覚悟が足りなかったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        "#00203F#5P#40Wふう……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0049
    ChrTalk(
        0x8,
        (
            "#00200F#11P──慣れるというのは\x01",
            "覚悟にあまり関係ないのでは？\x02\x03",

            "それを言うなら、わたしなんて\x01",
            "覚悟完了している事になります。\x02\x03",

            "#00203F多分、ランディさんの次くらいに\x01",
            "人の死に“慣れて”いますから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    SetCameraDistance(18360, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)

    #C0050
    ChrTalk(
        0x101,
        "#00008F#6P……そうか………\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#00206F#11Pですが、わたしがロイドさんより\x01",
            "捜査官に向いているとは\x01",
            "とても思えませんし……\x02\x03",

            "リーダーをやれるくらいの\x01",
            "覚悟があるとも当然思いません。\x02\x03",

            "#00201F──みんながロイドさんに\x01",
            "求めているのは多分違うと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#00005F#6Pティオ……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0053
    ChrTalk(
        0x101,
        (
            "#00006F#6P……そうだな。\x01",
            "確かにそうかもしれない。\x02\x03",

            "#00008F受けたショックを、覚悟の不足と\x01",
            "取り違えて動けなくなってたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#00204F#11Pなら、どうか動いてください。\x02\x03",

            "#00202F滅多にない全員での休暇#4Rバカンス#……\x02\x03",

            "みんなに楽しんでもらえるよう、\x01",
            "配慮するのはリーダーの役目では？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00002F#6Pああ、そうだな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18060, 1000)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_6F(0x79)
    Fade(250)
    BeginChrThread(0x101, 3, 0, 10)
    BeginChrThread(0x8, 3, 0, 11)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x8, 3)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)

    #C0056
    ChrTalk(
        0x8,
        "#00205F#11P……！？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00009F#6Pサンキュー、ティオ。\x02\x03",

            "#00000Fちょっとみんなと\x01",
            "軽く話してくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#00206F#11Pえ、ええ。\x01",
            "それがいいかと。\x02\x03",

            "#00208F#30W……でも……あの……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0059
    ChrTalk(
        0x101,
        "#00011F#6Pああ、悪い悪い。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_A1(0x101, 0x4E2, 0x2, 0x1, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_9B(0x1, 0x101, 0x0, 0xFFFFFF38, 0x3E8, 0x0)
    OP_0D()
    #Sound(2274, 255, 60, 0)    #voice#Tio

    #C0060
    ChrTalk(
        0x8,
        "#00205F#11P#40W……ぁ………\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00012F#6Pはは、子供扱いしたわけじゃなくて、\x01",
            "感謝のつもりっていうか……\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x3, 0x7, 0x8, 0x9)

    #C0062
    ChrTalk(
        0x8,
        (
            "#00206F#11Pいえ、気にしてません。\x02\x03",

            "#00208F#30Wその……むしろもう少し……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00005F#6Pえ？\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x2, 0xA, 0xB)
    Sleep(150)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0064
    ChrTalk(
        0x8,
        "#00201F#11Pっ……何でもありません！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x5DC, 0x2, 0xC, 0xD)

    #C0065
    ChrTalk(
        0x8,
        (
            "#00203F#11P早くみんなの所に\x01",
            "行ってきてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#00000F#6Pあ、ああ……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    #Sound(3053, 255, 60, 0)    #voice#Zeit

    #C0067
    ChrTalk(
        0x9,
        "#01203F#6P#30Wグルルルル……（やれやれ）\x02",
    )

    CloseMessageWindow()
    OP_24(0xBED)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x8, -500, 4100, 11000, 90)
    ClearChrFlags(0x8, 0x8000)
    OP_4C(0x8, 0xFF)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 1000, 4100, 11000, 180)
    ClearChrFlags(0x9, 0x8000)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -2250, 4250, -2100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0x0, 0, 4100, 8000, 180)
    SetScenarioFlags(0x144, 0)
    OP_29(0xA5, 0x4, 0x2)
    OP_29(0xA5, 0x1, 0x0)
    ClearChrFlags(0xA, 0x8)
    OP_25(0x1DF, 0x64)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_11CA end

    def Function_10_2719(): pass

    label("Function_10_2719")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x3E8, 0x7, 0x2, 0x3, 0x4, 0x5, 0x4, 0x3, 0x2)
    Return()

    # Function_10_2719 end

    def Function_11_2739(): pass

    label("Function_11_2739")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0x3E8, 0x7, 0x2, 0x3, 0x4, 0x5, 0x4, 0x3, 0x2)
    Return()

    # Function_11_2739 end

    def Function_12_2759(): pass

    label("Function_12_2759")

    EventBegin(0x0)
    Fade(500)
    OP_68(-2250, 5100, -2100, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16450, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10301.itp")
    SetChrPos(0x101, -1050, 4100, -2900, 315)
    SetChrSubChip(0xA, 0x1)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    #Sound(2911, 255, 100, 0)    #voice#Lazy

    #A0068
    AnonymousTalk(
        0xA,
        (
            "#30W──やあ、ロイド。\x02\x03",

            "どうやら活を\x01",
            "入れてもらったみたいだね？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB5F)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0069
    ChrTalk(
        0x101,
        (
            "#00012F#6Pハハ、まあね。\x02\x03",

            "#00000F……ワジの方は\x01",
            "けっこう平気みたいだな？\x02\x03",

            "いつも通りの\x01",
            "クールさっていうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "#10304F#5Pま、僕はそれが売りだから。\x02\x03",

            "#10308Fそれに、今までにも\x01",
            "理不尽な死に立ち会った\x01",
            "経験が無いわけじゃない。\x02\x03",

            "#10303Fクロスベルに来る前だけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#00008F#6Pそうなのか……\x02\x03",

            "#00005F……って、ワジの口から\x01",
            "初めて昔のことを聞いたな。\x02\x03",

            "#00000Fクロスベルの出身じゃないのは\x01",
            "何となく聞いてたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "#10309F#5Pフフ、それは企業秘密かな。\x02\x03",

            "#10300Fでも……\x01",
            "スラムで暮らしてた事もあるよ。\x02\x03",

            "旧市街なんかよりも遥かに\x01",
            "救われないようなゴミ溜めにさ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6F), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B3B")

    #C0073
    ChrTalk(
        0x101,
        (
            "#00006F#6P……そうか……\x02\x03",

            "#00008Fアルカンシェルのシュリも\x01",
            "辺境のスラム出身らしいけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9B")

    label("loc_2B3B")


    #C0074
    ChrTalk(
        0x101,
        (
            "#00006F#6P……そうか……\x02\x03",

            "#00008Fアルカンシェルの新人の子も\x01",
            "辺境のスラム出身らしいけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B9B")


    #C0075
    ChrTalk(
        0xA,
        (
            "#10305F#5Pああ、ノーザンブリアの子だね。\x02\x03",

            "#10306Fあそこは酷いからな……\x01",
            "外で猟兵をしている連中の送金で\x01",
            "何とか糊口#4R こ こう#をしのいでるくらいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00003F#6Pああ、噂は聞いたけど……\x02\x03",

            "#00005F……って、まるで行った事が\x01",
            "あるような口ぶりだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "#10304F#5Pフフ、さてね。\x02\x03",

            "#10308F#30W………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00005F#6P？？\x02\x03",

            "#00003F平気そうって言ったけど\x01",
            "少しキレがないっていうか……\x02\x03",

            "#00001F……何かあったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "#10304F#5P僕の方は別に。\x02\x03",

            "#10300Fただ、バイパーの方では\x01",
            "色々とあるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#00001F#6Pバイパー……\x01",
            "ヴァルドたちのことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "#10304F#5Pま、あんな別れ方だったから\x01",
            "さすがにちょっと気になるのさ。\x02\x03",

            "#10302F神秘的なカリスマが売りらしい\x01",
            "クールビューティな僕でもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#00006F#6P自分で言うなって……\x02\x03",

            "#00008F……でも、ヴァルドのことは\x01",
            "俺も少し気になってたんだ。\x02\x03",

            "#00000F時間が空いている時にでも\x01",
            "ちょっと様子を見に行こうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "#10304F#5Pフフ、そうしてくれると\x01",
            "こちらも助かるかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -1050, 4100, -3100, 180)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xD, 0x1)
    SetScenarioFlags(0x144, 1)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_2759 end

    def Function_13_2F59(): pass

    label("Function_13_2F59")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 2640, 4100, 4150, 180)
    SetChrPos(0xB, 3000, 4100, -8000, 180)
    ClearChrFlags(0xB, 0x80)
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x5)
    OP_68(2700, 5100, 3350, 0)
    MoveCamera(52, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18200, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17700, 2000)
    Sleep(500)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x8)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_6F(0x79)
    OP_68(3000, 5100, -8000, 3000)
    SetCameraDistance(18000, 3000)
    OP_6F(0x79)
    Sleep(1500)
    Fade(500)
    OP_68(2700, 5100, 3350, 0)
    MoveCamera(52, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    #C0084
    ChrTalk(
        0x101,
        (
            "#00002F#5P（キーア……\x01",
            "  どこにいるかと思ったら。）\x02\x03",

            "#00006F（……やっぱり少し\x01",
            "  心配させてたみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, 2640, 4100, 4150, 180)
    SetMapObjFlags(0x0, 0x10)
    SetScenarioFlags(0x144, 4)
    EventEnd(0x5)
    Return()

    # Function_13_2F59 end

    def Function_14_30FE(): pass

    label("Function_14_30FE")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_64(0xB)
    LoadChrToIndex("chr/ch02710.itc", 0x1E)
    LoadChrToIndex("chr/ch02702.itc", 0x1F)
    LoadChrToIndex("apl/ch51302.itc", 0x20)
    LoadChrToIndex("apl/ch51355.itc", 0x21)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01103.itp")
    SoundLoad(3611)
    SoundLoad(3612)
    OP_4B(0xB, 0xFF)
    SetChrPos(0x101, 3000, 4100, -6800, 180)
    SetChrPos(0x102, 0, 4100, 2000, 180)
    SetChrPos(0x103, 3550, 4100, 0, 180)
    SetChrPos(0x104, 3550, 4100, 4000, 180)
    SetChrPos(0x109, 0, 4100, 3200, 180)
    SetChrPos(0x105, 0, 4100, 4400, 180)
    SetChrPos(0x9, 0, 4100, 0, 180)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x1)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x8, 0x8)
    OP_68(3000, 5100, -7400, 0)
    MoveCamera(135, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17500, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0085
    ChrTalk(
        0xB,
        "#01108F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#00002F#6Pキーア、ここにいたのか。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0xB, 0x0, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0087
    AnonymousTalk(
        0xB,
        (
            "#3611V#40Wあ……ロイド……\x02\x03",

            "#3612V#30Wえへへ……\x01",
            "そろそろ到着かなー？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE1C)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0088
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、あと少しだよ。\x02\x03",

            "#00000Fテーマパークもあるから\x01",
            "着いたら目いっぱい遊ぼうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        (
            "#01102F#11Pうんっ！\x02\x03",

            "#01122F……えへへ………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0090
    ChrTalk(
        0x101,
        (
            "#00006F#6P……ごめんな、キーア。\x02\x03",

            "#00008F最近、ずっと寂しい思いを\x01",
            "させちゃってたみたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xB,
        (
            "#01121F#11P……ううん。\x01",
            "ぜんぜんヘーキだよ。\x02\x03",

            "#01106F詳しくは知らないけど……\x01",
            "みんなが落ち込んでるのは\x01",
            "なんとなく分かったから……\x02\x03",

            "#01108Fキーアの方こそみんなを\x01",
            "元気付けてあげたかったのに……\x02\x03",

            "けっきょく何もできなくって……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(17200, 750)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_6F(0x79)
    Fade(250)
    BeginChrThread(0x101, 3, 0, 23)
    BeginChrThread(0xB, 3, 0, 24)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xB, 3)
    OP_0D()

    #C0092
    ChrTalk(
        0xB,
        "#01105F#11Pあ……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#00004F#6P十分、元気をもらってるよ。\x02\x03",

            "#00002Fキーアが側に居てくれること……\x02\x03",

            "それがどれだけ、俺たち全員に\x01",
            "力と元気をくれていると思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xB,
        (
            "#01105F#11Pそーなの……？\x02\x03",

            "#01108F……本当にそうなのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#00005F#6P……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0x101, 0x514, 0x2, 0x2, 0x1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_9B(0x1, 0x101, 0x0, 0xFFFFFF06, 0x1F4, 0x0)

    #C0096
    ChrTalk(
        0xB,
        (
            "#01109F#11P……えへへ。\x01",
            "なんか分かんなくなっちゃった。\x02\x03",

            "#01105Fあ、でも、みんなちょっと\x01",
            "元気になったみたいだねー？\x02\x03",

            "#01104Fえへへ。\x01",
            "やっぱりロイドはすごいなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00012F#6Pいや、俺のせいってわけじゃ\x01",
            "ないと思うんだけど……\x02\x03",

            "#00002Fでも、せっかくだから\x01",
            "みんなで目いっぱい楽しもう。\x02\x03",

            "テーマパーク、\x01",
            "すごく楽しみにしてただろう？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x4B0, 0x4, 0x8, 0x9, 0x8, 0x3)

    #C0098
    ChrTalk(
        0xB,
        "#01109F#11Pうんっ！\x02",
    )

    CloseMessageWindow()
    OP_A1(0xB, 0x4B0, 0x6, 0xB, 0xC, 0xD, 0xE, 0xD, 0xC)

    #C0099
    ChrTalk(
        0xB,
        (
            "#01110F#11Pキーア、観覧車に乗りたいー！\x02\x03",

            "あと、ティオといっしょに\x01",
            "『みっしぃにキック』もしたいかな～！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#00011F#6P『みっしぃにキック』って……\x01",
            "子供の間で流行ってるんだっけ？\x02\x03",

            "#00012Fうーん、ティオはちょっと\x01",
            "年齢制限に引っかかりそうだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0101
    ChrTalk(
        0x103,
        (
            "#00211F#6P#N──そのあたりのマナーは\x01",
            "わきまえているつもりですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0xB, 0x5DC, 0x2, 0xC, 0xF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(3000, 4800, -5400, 0)
    OP_68(3000, 4800, -7400, 6000)
    MoveCamera(150, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20350, 0)
    ClearChrFlags(0x9, 0x800)
    BeginChrThread(0x101, 3, 0, 21)
    BeginChrThread(0xB, 3, 0, 22)
    BeginChrThread(0x103, 3, 0, 15)
    BeginChrThread(0x9, 3, 0, 16)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 18)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 19)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 20)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0x102, 3)

    #C0102
    ChrTalk(
        0x101,
        "#00005F#5Pティオ、それにみんな……\x02",
    )

    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        "#01105F#11Pあれー、どうしたのー？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        "#01200F#11Pウォン。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        (
            "#00109F#12Pふふ、何となくみんなで\x01",
            "集まっちゃったというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x105,
        (
            "#10302F#12Pそれに、そろそろ\x01",
            "到着するみたいだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        "#00002F#5Pああ、そうか。\x02",
    )

    CloseMessageWindow()

    def lambda_3BA7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3BA7)
    Sleep(50)

    def lambda_3BB7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3BB7)
    Sleep(50)

    def lambda_3BC7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3BC7)
    Sleep(50)

    def lambda_3BD7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3BD7)
    Sleep(50)

    def lambda_3BE7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3BE7)
    Sleep(50)

    def lambda_3BF7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3BF7)
    Sleep(50)

    def lambda_3C07():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3C07)
    Sleep(50)
    SetChrFlags(0x9, 0x20)

    def lambda_3C1C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3C1C)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0x9, 2)
    Sleep(200)
    Fade(500)
    OP_68(3000, 4800, -7400, 0)
    MoveCamera(159, 0, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(47500, 0)
    OP_93(0x101, 0xE1, 0x0)
    OP_93(0x102, 0xE1, 0x0)
    OP_93(0x103, 0xE1, 0x0)
    OP_93(0x104, 0xE1, 0x0)
    OP_93(0x109, 0xE1, 0x0)
    OP_93(0x105, 0xE1, 0x0)
    OP_93(0xB, 0xE1, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    OP_68(0, 7800, -25000, 6000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    #Sound(3029, 255, 100, 0)    #voice#KeA
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0108
    ChrTalk(
        0xB,
        "#01109F#6P#N#4Sわあ～っ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xBD9)

    #C0109
    ChrTalk(
        0x102,
        "#00102F#6P#N綺麗ね……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0110
    ChrTalk(
        0x109,
        "#10109F#6P#N本日晴天、行楽日和ですね！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0111
    ChrTalk(
        0x104,
        (
            "#00309F#6P#Nよーし、ガンガン、\x01",
            "テンション上がってきたぜ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(479, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_68(0, 7800, -26000, 2000)
    OP_6F(0x79)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_30FE end

    def Function_15_3DCC(): pass

    label("Function_15_3DCC")

    OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_15_3DCC end

    def Function_16_3DE3(): pass

    label("Function_16_3DE3")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x898, 0x1)
    SetChrFlags(0xFE, 0x800)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x898, 0x1)
    ClearChrFlags(0xFE, 0x800)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x898, 0x1)
    SetChrFlags(0xFE, 0x800)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x898, 0x1)
    ClearChrFlags(0xFE, 0x800)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x7D0, 0x898, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 1, 0, 0)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_16_3DE3 end

    def Function_17_3E67(): pass

    label("Function_17_3E67")

    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x7D0, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_17_3E67 end

    def Function_18_3E8D(): pass

    label("Function_18_3E8D")

    OP_9B(0x0, 0xFE, 0x0, 0x2008, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_18_3E8D end

    def Function_19_3EA4(): pass

    label("Function_19_3EA4")

    OP_9B(0x0, 0xFE, 0x0, 0x21FC, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x320, 0x898, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_19_3EA4 end

    def Function_20_3ECA(): pass

    label("Function_20_3ECA")

    OP_9B(0x0, 0xFE, 0x0, 0x238C, 0x898, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x640, 0x898, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_20_3ECA end

    def Function_21_3EF7(): pass

    label("Function_21_3EF7")

    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_21_3EF7 end

    def Function_22_3F09(): pass

    label("Function_22_3F09")

    Sleep(1000)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_22_3F09 end

    def Function_23_3F14(): pass

    label("Function_23_3F14")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x20)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_A1(0xFE, 0x3E8, 0x6, 0x4, 0x5, 0x6, 0x5, 0x4, 0x3)
    Return()

    # Function_23_3F14 end

    def Function_24_3F33(): pass

    label("Function_24_3F33")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x21)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_A1(0xFE, 0x3E8, 0x6, 0x4, 0x5, 0x6, 0x5, 0x4, 0x3)
    Return()

    # Function_24_3F33 end

    def Function_25_3F52(): pass

    label("Function_25_3F52")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0x101, 2500, 4100, -8000, 180)
    SetChrPos(0xB, 3500, 4100, -8000, 180)
    OP_68(0, 5100, -18500, 0)
    MoveCamera(35, 3, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 2100, 18000, 15000)
    MoveCamera(40, 30, 0, 15000)
    SetCameraDistance(25000, 15000)
    FadeToBright(1000, 0)
    Sound(479, 2, 10, 0)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x64)
    OP_0D()
    Sleep(8000)
    StopSound(479, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e0510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_3F52 end

    def Function_26_4065(): pass

    label("Function_26_4065")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    SoundLoad(3802)
    SoundLoad(3775)
    SoundLoad(3776)
    SoundLoad(3777)
    SoundLoad(3778)
    SoundLoad(3779)
    SoundLoad(3619)
    SoundLoad(3620)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis407.itp")
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0x101, 2500, 4100, -8000, 180)
    SetChrPos(0xB, 3500, 4100, -8000, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 0, 4100, 1000, 180)
    SetChrFlags(0xE, 0x8)
    ClearMapObjFlags(0x0, 0x10)
    OP_68(3160, 5100, -6140, 0)
    MoveCamera(145, 29, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    FadeToBright(1000, 0)
    OP_68(3160, 5100, -8140, 3000)
    Sleep(2500)
    OP_63(0xB, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #C0112
    ChrTalk(
        0xB,
        "#01104F#3619V#5P#30W#15Aふんふふーん♪\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    TurnDirection(0x101, 0xB, 500)
    Sleep(150)

    #C0113
    ChrTalk(
        0x101,
        (
            "#00012F#12Pはは……\x01",
            "キーア、ご機嫌だな。\x02\x03",

            "#00002Fなんか色々あったけど……\x01",
            "ちゃんと楽しめたか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0114
    ChrTalk(
        0xB,
        (
            "#01109F#5Pうんっ！\x02\x03",

            "#01110Fまたみんなで一緒に\x01",
            "おでかけしたいねー！\x02\x03",

            "今度はアルモリカ村とかー。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00002F#12Pはは、いいかもしれないな。\x02\x03",

            "#00004F（……昨日の様子からすると\x01",
            "  何かあるのかと思ったけど……）\x02\x03",

            "（すっかり元気そうだし、\x01",
            "  そんなに心配はいらないかな？）\x02\x03",

            "#00008F（むしろ心配すべきは\x01",
            "  《結社》の動きの方か……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0xB,
        (
            "#01105F#5Pんー？\x01",
            "ロイド、どうしたのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#00012F#12Pいや、何でもないよ。\x02\x03",

            "#00008F……それよりキーア。\x01",
            "本当に昨日の夜、変なヤツを\x01",
            "見かけたりしてないんだよな？\x02\x03",

            "#00001Fピンク色の服を着たヤツとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xB,
        (
            "#01112F#5Pんー……\x01",
            "見かけてないと思うけど。\x02\x03",

            "#01106Fキーア、寝ぼけてたみたいだから\x01",
            "ちょっと自信ないかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#00000F#12Pそっか……\x01",
            "いや、それならいいんだ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_4570")
    OP_C9(0x0, 0x80000000)

    #N0120
    NpcTalk(
        0xE,
        "マリアベルの声",
        "#3802V#2P#30Wあら、こちらにいましたか。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Jump("loc_459A")

    label("loc_4570")


    #N0121
    NpcTalk(
        0xE,
        "娘の声",
        "#2Pあら、こちらにいましたか。\x02",
    )

    CloseMessageWindow()

    label("loc_459A")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(2000, 5100, -7500, 4000)
    MoveCamera(147, 22, 0, 4000)

    def lambda_45E2():

        label("loc_45E2")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_45E2")

    QueueWorkItem2(0x101, 2, lambda_45E2)

    def lambda_45F4():

        label("loc_45F4")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_45F4")

    QueueWorkItem2(0xB, 2, lambda_45F4)
    BeginChrThread(0xE, 3, 0, 27)
    WaitChrThread(0xE, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0xB, 0x2)
    OP_6F(0x79)

    #C0122
    ChrTalk(
        0xB,
        "#01110F#5Pあ、ベルだー。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#00002F#5Pマリアベルさん。\x01",
            "どうも、お疲れ様です。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4783")

    #C0124
    ChrTalk(
        0xE,
        (
            "#02902F#12Pふふ、お疲れ様は\x01",
            "あなたたちの方でしょう。\x02\x03",

            "#02906Fしかし《結社》といったかしら。\x01",
            "ふざけた連中もいたものね。\x02\x03",

            "#02903Fわたくしの人形を攫#2Rさら#ったのも\x01",
            "そいつらの一員という話ですし！\x02\x03",

            "#02910Fこれは保安部の警備体制を\x01",
            "徹底する必要がありますわね……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4841")

    label("loc_4783")


    #C0125
    ChrTalk(
        0xE,
        (
            "#02902F#12Pふふ、お疲れ様は\x01",
            "あなたたちの方でしょう。\x02\x03",

            "#02906Fしかし《結社》といったかしら。\x01",
            "ふざけた連中もいたものね。\x02\x03",

            "#02901Fこれは保安部の警備体制を\x01",
            "徹底する必要がありますわね……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4841")


    #C0126
    ChrTalk(
        0x101,
        (
            "#00012F#5Pそ、そうですね……\x02\x03",

            "#00008F（民間の警備員の手に負える\x01",
            "  ヤツじゃないと思うけど……）\x02\x03",

            "#00013F（……やっぱり俺たちの方で\x01",
            "  気をつけておく必要があるな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xE,
        (
            "#02904F#12P──まあ、それはともかく。\x02\x03",

            "#02900Fロイドさん、キーアさん。\x02\x03",

            "ふと思ったのですけど、\x01",
            "皆で記念写真を撮らないこと？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0128
    ChrTalk(
        0x101,
        "#00002F#5Pああ、いいですね！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)
    Sleep(100)

    #C0129
    ChrTalk(
        0xB,
        (
            "#01105F#5Pえっと、記念写真って、\x01",
            "前にみんなでいっしょに撮った？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)
    Sleep(100)

    #C0130
    ChrTalk(
        0x101,
        (
            "#00004F#11Pああ、みんなと一緒の思い出を\x01",
            "写真に残しておくものさ。\x02\x03",

            "#00000Fそれを見れば今回のバカンスを\x01",
            "いつでも思い出せるってわけだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0131
    ChrTalk(
        0xB,
        "#01107F#4S#5Pうんっ、撮りたいー！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xE,
        (
            "#02909F#12P決まりですわね。\x02\x03",

            "#02905Fそうなると……\x01",
            "船内より甲板#4Rこちら#の方がいいかしら？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)

    #C0133
    ChrTalk(
        0x101,
        (
            "#00009F#5Pそうですね。\x01",
            "せっかくのいい天気ですし。\x02\x03",

            "#00002F俺、みんなを呼んできますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xE,
        (
            "#02904F#12Pええ、お願いします。\x02\x03",

            "#02902Fそれと船内にいる\x01",
            "添乗員に声をかけてください。\x02\x03",

            "記念写真のサービスなら\x01",
            "すぐに受け付けてくれますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#00000F#5P分かりました。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x19, 0x1F4)
    OP_68(3000, 5100, 0, 5000)
    MoveCamera(30, 25, 0, 5000)
    OP_6E(400, 5000)
    SetCameraDistance(22000, 5000)
    BeginChrThread(0x101, 3, 0, 28)

    def lambda_4C9B():

        label("loc_4C9B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4C9B")

    QueueWorkItem2(0xB, 2, lambda_4C9B)

    def lambda_4CAD():
        OP_93(0xFE, 0xA, 0x12C)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4CAD)
    Sleep(1500)
    SetMessageWindowPos(250, 180, -1, -1)
    OP_C9(0x0, 0x80000000)

    #C0136
    ChrTalk(
        0xB,
        "#01105F#3620V#30W#10A#11P#Nあ──\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    WaitChrThread(0x101, 3)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xE, 0x2)
    OP_6F(0x79)
    StopBGM(0x1770)

    #C0137
    ChrTalk(
        0xB,
        "#01112F#40W#12P#N…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0138
    ChrTalk(
        0xE,
        (
            "#02913F#3775V#12P#30W#Nふふっ……\x02\x03",

            "#3776V──大切な人たちに\x01",
            "余計な心配をかけたくない。\x02\x03",

            "#02902F#3777Vいい女は大変ですわね？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEC1)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    #C0139
    ChrTalk(
        0xB,
        "#01105F#12P#N！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    TurnDirection(0xB, 0xE, 0)
    OP_68(2000, 5100, -7500, 0)
    MoveCamera(300, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetCameraDistance(22000, 1500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    TurnDirection(0xE, 0xB, 350)
    OP_6F(0x79)
    CancelBlur(0)
    SetCameraDistance(21000, 20000)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0140
    ChrTalk(
        0xE,
        (
            "#02913F#3778V#5P#40W#30A何か悩みがあるのでしょう？\x02\x03",

            "#02912F#3779V#35A──わたくしならば\x01",
            "力になれるかもしれませんわ。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_24(0xEC3)
    OP_C9(0x1, 0x80000000)
    StopSound(479, 3000, 80)
    FadeToDark(2000, 0, -1)
    SetCameraDistance(20700, 2000)
    OP_6F(0x79)
    OP_0D()
    WaitBGM()
    Sleep(2500)
    OP_29(0xA5, 0x1, 0xD)
    OP_29(0xA5, 0x4, 0x10)
    OP_32(0xFF, 0xFE, 0x0)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("e4600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_4065 end

    def Function_27_4FE5(): pass

    label("Function_27_4FE5")

    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x5DC, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 0)
    Return()

    # Function_27_4FE5 end

    def Function_28_500B(): pass

    label("Function_28_500B")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFE7, 0x1F40, 0x7D0, 0x1)
    OP_96(0xFE, 0xA50, 0x1004, 0x11C6, 0x7D0, 0x0)
    Sound(100, 0, 100, 0)
    OP_70(0x0, 0x5)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x0)

    def lambda_505B():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_505B)
    Sleep(300)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0xFE, 1)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x0)
    SetChrPos(0x101, 0, 0, 0, 0)
    Return()

    # Function_28_500B end

    SaveToFile()

Try(main)
