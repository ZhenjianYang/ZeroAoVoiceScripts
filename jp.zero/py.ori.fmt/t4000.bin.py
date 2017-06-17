from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4000.bin",                # FileName
        "t4000",                    # MapName
        "t4000",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 3, 0, 4],
    )

    BuildStringList((
        "t4000",                  # 0
        "ロランド司祭",           # 1
        "シスター・ジュジュ",     # 2
        "タミル",                 # 3
        "ハミル",                 # 4
        "エステル",               # 5
        "ヨシュア",               # 6
        "遊撃士リン",             # 7
        "遊撃士エオリア",         # 8
        "観光客フォンティアーヌ", # 9
        "マインツ山道",           # 10
    ))

    AddCharChip((
        "chr/ch25400.itc",                   # 00
        "chr/ch25500.itc",                   # 01
        "chr/ch23800.itc",                   # 02
        "chr/ch00600.itc",                   # 03
        "chr/ch00700.itc",                   # 04
        "chr/ch32000.itc",                   # 05
        "chr/ch32100.itc",                   # 06
        "chr/ch32400.itc",                   # 07
    ))

    DeclNpc(-2630,   0,       9369,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2299,    0,       14270,   180,  257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-5780,   0,       14529,   180,  385,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-5780,   0,       13680,   0,    385,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(21059,   0,       40569,   90,   405,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(20940,   0,       44159,   180,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-9,      0,       5010,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(1200,    0,       4199,    315,  389,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-1940,   9,       19950,   0,    385,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(-10390,  500,     13820,   1200,    -10390,  2000,    13820,   0x007C, 0,  18, 0x0000)

    PlaceName(5.0, -0.0, -35.0, 0x0000, 0x0000, "マインツ山道")

    ScpFunction((
        "Function_0_234",          # 00, 0
        "Function_1_2EC",          # 01, 1
        "Function_2_43D",          # 02, 2
        "Function_3_49E",          # 03, 3
        "Function_4_621",          # 04, 4
        "Function_5_634",          # 05, 5
        "Function_6_10D3",         # 06, 6
        "Function_7_2473",         # 07, 7
        "Function_8_2756",         # 08, 8
        "Function_9_2A65",         # 09, 9
        "Function_10_2B14",        # 0A, 10
        "Function_11_2E53",        # 0B, 11
        "Function_12_2FEA",        # 0C, 12
        "Function_13_3393",        # 0D, 13
        "Function_14_3456",        # 0E, 14
        "Function_15_34D8",        # 0F, 15
        "Function_16_35FC",        # 10, 16
        "Function_17_3FE0",        # 11, 17
        "Function_18_4433",        # 12, 18
    ))


    def Function_0_234(): pass

    label("Function_0_234")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_274"),
        (1, "loc_280"),
        (2, "loc_28C"),
        (3, "loc_298"),
        (4, "loc_2A4"),
        (5, "loc_2B0"),
        (6, "loc_2BC"),
        (SWITCH_DEFAULT, "loc_2C8"),
    )


    label("loc_274")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_280")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_28C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_298")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2A4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2B0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2EB")

    Return()

    # Function_0_234 end

    def Function_1_2EC(): pass

    label("Function_1_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43C")
    OP_95(0xFE, -2510, 0, 14270, 2000, 0x0)
    OP_95(0xFE, -2510, 0, 12920, 2000, 0x0)
    OP_95(0xFE, 11020, 0, 12920, 2000, 0x0)
    OP_95(0xFE, 18830, 0, 20000, 2000, 0x0)
    OP_95(0xFE, 18830, 0, 24520, 2000, 0x0)
    OP_95(0xFE, 26350, 0, 31740, 2000, 0x0)
    OP_95(0xFE, 26350, 0, 46780, 2000, 0x0)
    OP_95(0xFE, 23030, 0, 51110, 2000, 0x0)
    OP_95(0xFE, 23030, 0, 54060, 2000, 0x0)
    OP_95(0xFE, 21080, 0, 54060, 2000, 0x0)
    OP_95(0xFE, 21080, 0, 48950, 2000, 0x0)
    OP_95(0xFE, 25050, 0, 44720, 2000, 0x0)
    OP_95(0xFE, 25050, 0, 34580, 2000, 0x0)
    OP_95(0xFE, 17430, 0, 27090, 2000, 0x0)
    OP_95(0xFE, 17430, 0, 21180, 2000, 0x0)
    OP_95(0xFE, 9240, 0, 14270, 2000, 0x0)
    Jump("Function_1_2EC")

    label("loc_43C")

    Return()

    # Function_1_2EC end

    def Function_2_43D(): pass

    label("Function_2_43D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49D")
    OP_95(0xFE, 23000, 0, 42000, 6000, 0x0)
    OP_95(0xFE, 19000, 0, 42000, 6000, 0x0)
    OP_95(0xFE, 19000, 0, 39000, 6000, 0x0)
    OP_95(0xFE, 23000, 0, 39000, 6000, 0x0)
    Jump("Function_2_43D")

    label("loc_49D")

    Return()

    # Function_2_43D end

    def Function_3_49E(): pass

    label("Function_3_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4B6")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5DB")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4C4")
    Jump("loc_5DB")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4DC")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5DB")

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4EA")
    Jump("loc_5DB")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_4F8")
    Jump("loc_5DB")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_510")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5DB")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_528")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5DB")

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_578")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, 23000, 0, 41500, 0)
    SetChrPos(0xB, 23000, 0, 39000, 0)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_5DB")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_586")
    Jump("loc_5DB")

    label("loc_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_59E")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_5DB")

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5AC")
    Jump("loc_5DB")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5BA")
    Jump("loc_5DB")

    label("loc_5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5C8")
    Jump("loc_5DB")

    label("loc_5C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5DB")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_5DB")

    BeginChrThread(0x9, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FC")
    SetMapFlags(0x10000000)
    Event(0, 16)
    Jump("loc_60D")

    label("loc_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60D")
    Event(0, 17)

    label("loc_60D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_620")
    ClearChrFlags(0x10, 0x80)

    label("loc_620")

    Return()

    # Function_3_49E end

    def Function_4_621(): pass

    label("Function_4_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_633")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)

    label("loc_633")

    Return()

    # Function_4_621 end

    def Function_5_634(): pass

    label("Function_5_634")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6BC")

    #C0001
    ChrTalk(
        0xFE,
        (
            "日が落ちてきました……\x01",
            "視界の悪い夕方は\x01",
            "魔獣の危険度も増します。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "街道を歩くおつもりなら\x01",
            "どうかお気をつけて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CF")

    label("loc_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_72F")

    #C0003
    ChrTalk(
        0xFE,
        (
            "本日は警備隊の方から\x01",
            "曹長殿がいらっしゃっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "一体どのようなご用なのでしょうか……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_10CF")

    label("loc_72F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7C7")

    #C0005
    ChrTalk(
        0xFE,
        (
            "近頃、クロスベルがまた\x01",
            "物騒になってきている気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "日曜学校で子供たちを預かる大聖堂も、\x01",
            "しかと用心しなければなりませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CF")

    label("loc_7C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_854")

    #C0007
    ChrTalk(
        0xFE,
        (
            "こんにちは、\x01",
            "クロスベル大聖堂へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "本日は日曜学校が開かれています。\x01",
            "授業の妨げにならないよう\x01",
            "ご注意ください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CF")

    label("loc_854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_8CB")

    #C0009
    ChrTalk(
        0xFE,
        "おや……もうお帰りでしょうか。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "またいつでもお越しください。\x01",
            "皆様に女神の加護があらんことを……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CF")

    label("loc_8CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B89")

    #C0011
    ChrTalk(
        0xFE,
        (
            "こんにちは、\x01",
            "クロスベル大聖堂へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x153,
        "#1110Fこんにちはっ！　キーアだよ！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "はは……元気がよくて何よりです。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_END)), "loc_B81")

    #C0014
    ChrTalk(
        0x101,
        (
            "#0000Fえっと……マーブル先生は\x01",
            "いらっしゃいますか？\x02\x03",

            "この子のことについて\x01",
            "相談したいことがありまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "おや、そうでしたか。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "シスター・マーブルなら\x01",
            "日曜学校の教室で\x01",
            "雑務を行っておられますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#0000Fあ、そうですか……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_AB0")

    #C0018
    ChrTalk(
        0x102,
        (
            "#0104Fほっ、良かった。\x01",
            "先生はいらっしゃるみたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B26")

    label("loc_AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_AE4")

    #C0019
    ChrTalk(
        0x103,
        "#0200F随分と熱心な方なんですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B26")

    label("loc_AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B26")

    #C0020
    ChrTalk(
        0x104,
        (
            "#0300Fどうやら行き違いには\x01",
            "ならなかったみてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B26")


    #C0021
    ChrTalk(
        0x101,
        (
            "#0000F……よし、じゃあさっそく\x01",
            "マーブル先生に会いに行くとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x153,
        "#1109Fごーっ！\x02",
    )

    CloseMessageWindow()

    label("loc_B81")

    SetScenarioFlags(0x0, 0)
    Jump("loc_C03")

    label("loc_B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_END)), "loc_BDF")

    #C0023
    ChrTalk(
        0xFE,
        (
            "シスター・マーブルなら\x01",
            "日曜学校の教室で\x01",
            "雑務を行っておられますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C03")

    label("loc_BDF")


    #C0024
    ChrTalk(
        0xFE,
        "ふふ……子供は元気が一番です。\x02",
    )

    CloseMessageWindow()

    label("loc_C03")

    Jump("loc_10CF")

    label("loc_C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C91")

    #C0025
    ChrTalk(
        0xFE,
        (
            "記念祭中は大聖堂内で\x01",
            "ミサを執り行っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "今日で記念祭も終わり……\x01",
            "気を引き締めておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CDB")

    label("loc_C91")


    #C0027
    ChrTalk(
        0xFE,
        (
            "今日で記念祭も終わり……\x01",
            "気を引き締めて\x01",
            "守衛にあたりたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDB")

    Jump("loc_10CF")

    label("loc_CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D40")

    #C0028
    ChrTalk(
        0xFE,
        (
            "連日、記念祭は\x01",
            "大盛況のようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "これだけ人が多いと\x01",
            "守衛も大変です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CF")

    label("loc_D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_DB4")

    #C0030
    ChrTalk(
        0xFE,
        (
            "記念祭中は大聖堂内で\x01",
            "ミサを執り行っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "外国の方などもぽつぽつと\x01",
            "訪れているようです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CF")

    label("loc_DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_E6E")

    #C0032
    ChrTalk(
        0xFE,
        (
            "記念祭中は大聖堂内で\x01",
            "ミサを執り行っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "参加を希望されるなら\x01",
            "ご自由にお通りください。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "児童の方には\x01",
            "お菓子の配布などもしてますので\x01",
            "よろしければどうぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CF")

    label("loc_E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_EDC")

    #C0035
    ChrTalk(
        0xFE,
        (
            "本日もお日柄良く、\x01",
            "何事もなく終わりそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "こんな日がいつまでも\x01",
            "続くといいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CF")

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1010")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9F")

    #C0037
    ChrTalk(
        0xFE,
        (
            "今日は講堂の方で\x01",
            "日曜学校が開かれています。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "不審者が入らないよう\x01",
            "注意しているのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "あなた達は……\x01",
            "警察の方のようですね。\x01",
            "どうぞ、お通りください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_100B")

    label("loc_F9F")


    #C0040
    ChrTalk(
        0xFE,
        (
            "子供たちを預かる身として\x01",
            "守衛役は気を遣います。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "先日の狼騒動といい、\x01",
            "物騒な事件が多いですからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100B")

    Jump("loc_10CF")

    label("loc_1010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_10CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A9")

    #C0042
    ChrTalk(
        0xFE,
        (
            "このクロスベル大聖堂では、\x01",
            "教区長であるエラルダ大司教が\x01",
            "七耀の教えを施しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        "敷地内ではお静かにお願いします。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10CF")

    label("loc_10A9")


    #C0044
    ChrTalk(
        0xFE,
        "敷地内ではお静かにお願いします。\x02",
    )

    CloseMessageWindow()

    label("loc_10CF")

    TalkEnd(0xFE)
    Return()

    # Function_5_634 end

    def Function_6_10D3(): pass

    label("Function_6_10D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EB")

    #C0045
    ChrTalk(
        0xFE,
        (
            "私がシスターとしてここに就任して\x01",
            "そろそろ半年近くがたちます。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "多くの市民や子供たちと\x01",
            "出会えましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "シスター・マーブルと比べると\x01",
            "どうしても未熟さがでてしまいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "いつか私も彼女のような\x01",
            "立派なシスターになれるといいなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_127D")

    label("loc_11EB")


    #C0049
    ChrTalk(
        0xFE,
        (
            "私がシスターとしてここに就任して\x01",
            "そろそろ半年近くがたちます。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "いつか私もシスター・マーブルのような\x01",
            "立派なシスターになれるといいなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_127D")

    Jump("loc_246F")

    label("loc_1282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1372")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1330")

    #C0051
    ChrTalk(
        0xFE,
        (
            "今日来ている警備隊の方は\x01",
            "プライベートでもよく\x01",
            "お祈りに来られています。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "ノエルさんといいましたか……\x01",
            "礼儀正しく心優しい方だと思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_136D")

    label("loc_1330")


    #C0053
    ChrTalk(
        0xFE,
        (
            "ノエルさんはプライベートでも\x01",
            "よくお祈りに来られますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136D")

    Jump("loc_246F")

    label("loc_1372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_13EE")

    #C0054
    ChrTalk(
        0xFE,
        (
            "タミル君とハミル君は\x01",
            "よくここに遊びに来るんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "ええっと……\x01",
            "あれ、どっちがどっちだったかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246F")

    label("loc_13EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_158E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1508")

    #C0056
    ChrTalk(
        0xFE,
        (
            "今日は東通りの\x01",
            "子供たちが来ているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "……それにしても、今時の子たちは\x01",
            "しっかりしていますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "クータ君なんかはあの歳で、\x01",
            "色んな店の安売り情報なんかに\x01",
            "詳しいんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "安いお店を教えてもらいましたし\x01",
            "あとで買出しに行こうかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1589")

    label("loc_1508")


    #C0060
    ChrTalk(
        0xFE,
        (
            "今日は東通りの\x01",
            "子供たちが来ているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "今時の子はしっかりしていて、\x01",
            "大人としての私の立場が\x01",
            "危うい気がしますね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1589")

    Jump("loc_246F")

    label("loc_158E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1859")
    TurnDirection(0xFE, 0x153, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F1")

    #C0062
    ChrTalk(
        0xFE,
        (
            "そういえば……\x01",
            "あなたは日曜学校には\x01",
            "通っていないのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x153,
        (
            "#1111Fガッコー？\x01",
            "キーアもそこにいくの？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#0003Fえ、えっと……\x01",
            "説明が難しいんですが、\x01",
            "この子には色々ありまして、今は……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "あ、いえ……\x01",
            "立ち入った事を聞いてしまって\x01",
            "すみません。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "でももし来れるようになったら……\x01",
            "そのときは日曜学校においで下さいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "他の子供たちも、\x01",
            "友達が増えたら喜ぶだろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x153,
        "#1110Fうん、気がむいたらね～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1787")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_17CE")

    label("loc_1787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_17AD")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_17CE")

    label("loc_17AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_17CE")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_17CE")

    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1854")

    label("loc_17F1")


    #C0069
    ChrTalk(
        0xFE,
        (
            "えっと……キーアちゃん。\x01",
            "いつか日曜学校においで下さいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "私たち、歓迎しちゃいますから。\x02",
    )

    CloseMessageWindow()

    label("loc_1854")

    Jump("loc_246F")

    label("loc_1859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A5")
    TurnDirection(0xFE, 0x153, 0)

    #C0071
    ChrTalk(
        0xFE,
        (
            "……あら可愛らしい！\x01",
            "ふふ、お名前はなんです？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x153,
        (
            "#1110Fキーアの名前はキーアだよ！\x02\x03",

            "#1109F……あ、おねえさん、\x01",
            "おもしろいかっこうしてるね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "そ、そう？\x01",
            "一般的な修道女の服なのだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x153,
        "#1111Fシュードー……ジョー？\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#0003F（うーん、七耀教会の事は\x01",
            "  ほとんど知らないのか……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AEF")

    label("loc_19A5")


    #C0076
    ChrTalk(
        0xFE,
        (
            "面白い格好……面白い格好……\x01",
            "そうなのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "もしかして……\x01",
            "子どもになめられる要因は\x01",
            "この、服に……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1A56")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_1A9D")

    label("loc_1A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1A7C")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_1A9D")

    label("loc_1A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1A9D")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1A9D")

    Sleep(1000)

    #C0078
    ChrTalk(
        0x101,
        (
            "#0006Fあ、あの……子どもの言う事ですし\x01",
            "深く考えない方がいいと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AEF")

    Jump("loc_246F")

    label("loc_1AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1C13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BBA")

    #C0079
    ChrTalk(
        0xFE,
        (
            "噂で聞きました。\x01",
            "街で小さい子供が迷子になっていたとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "皆さんがそれを助ける為に\x01",
            "動き回っているのを\x01",
            "沢山の人が見ていたらしくって。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "ふふ、お手柄でしたね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C0E")

    label("loc_1BBA")


    #C0082
    ChrTalk(
        0xFE,
        (
            "昨日はお手柄でしたね。\x01",
            "こんな広い自治州から\x01",
            "迷子の子供を見つけてしまうなんて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0E")

    Jump("loc_246F")

    label("loc_1C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1E3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D74")

    #C0083
    ChrTalk(
        0xFE,
        (
            "私、子供になめられやすくて。\x01",
            "シスター・マーブルにそのことを\x01",
            "相談してみたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "そしたら、『それはあなたが子供に\x01",
            "好かれやすいということなのよ』って\x01",
            "言われました。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        "……どういうことなんでしょう？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "突然スカートをめくられたりするのが\x01",
            "好かれてるってこと……？？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "うーん……\x01",
            "まだ新米なのでよくわかりません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E36")

    label("loc_1D74")


    #C0088
    ChrTalk(
        0xFE,
        (
            "子供にはよくスカートをめくられたり\x01",
            "突然攻撃されたりするんですけど……\x01",
            "それが好かれているってこと……？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "シスター・マーブルのような\x01",
            "ベテランのシスターになれば\x01",
            "意味が分かるんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E36")

    Jump("loc_246F")

    label("loc_1E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1FED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F74")

    #C0090
    ChrTalk(
        0xFE,
        (
            "わたし、なんだか\x01",
            "子供になめられやすい気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "今日なんかミサに来てた男の子に\x01",
            "いきなりおしりを蹴られちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "怒って追い掛け回してたら\x01",
            "なんだか楽しくなっちゃって、\x01",
            "結局２人で笑ってたんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "もっとシスターとして、\x01",
            "清楚でビシッとした態度を\x01",
            "とりたいです……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FE8")

    label("loc_1F74")


    #C0094
    ChrTalk(
        0xFE,
        (
            "わたし、なんだか\x01",
            "子供になめられやすい気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "はぁ……今度シスター・マーブルに\x01",
            "相談してみようかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE8")

    Jump("loc_246F")

    label("loc_1FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2135")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20EA")

    #C0096
    ChrTalk(
        0xFE,
        (
            "昨日は、思った以上に\x01",
            "子供連れの参拝客が多くて\x01",
            "大変でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "あらかじめ焼いていたクッキーが\x01",
            "足りなくなっちゃって、\x01",
            "泣き出す子までいて……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "うう、悪いことをしました。\x01",
            "今日は夜までに沢山クッキーを\x01",
            "焼いておかないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2130")

    label("loc_20EA")


    #C0099
    ChrTalk(
        0xFE,
        (
            "今日はクッキーが\x01",
            "足らなくならないように、\x01",
            "沢山焼いておかないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2130")

    Jump("loc_246F")

    label("loc_2135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_21A5")

    #C0100
    ChrTalk(
        0xFE,
        (
            "今日は日曜学校は休みで、\x01",
            "ミサが開かれるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "もしよかったら\x01",
            "参加なさってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246F")

    label("loc_21A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2361")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_231C")

    #C0102
    ChrTalk(
        0xFE,
        (
            "わたしお料理が得意で、\x01",
            "日曜学校に子供たちが来た時は\x01",
            "昼ごはんを振舞うんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "最近は好き嫌いの多い子が\x01",
            "増えてきてるんですけど……\x01",
            "そこはウデの見せ所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "その子の好物の中にさりげなく\x01",
            "嫌いなモノを混ぜたりして、\x01",
            "徐々に慣らしていくんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "あとで嫌いなモノが入ってたって\x01",
            "教えた時の子供の顔ときたら……\x01",
            "これはもう、見ものですよ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_235C")

    label("loc_231C")


    #C0106
    ChrTalk(
        0xFE,
        (
            "子供の好き嫌いを無くすのは\x01",
            "なかなか楽しいですよ。\x01",
            "ふふふ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235C")

    Jump("loc_246F")

    label("loc_2361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_246F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2401")

    #C0107
    ChrTalk(
        0xFE,
        (
            "あら……\x01",
            "大聖堂に何か御用です？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "それとも、もしかして\x01",
            "お墓参りに来た方かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "脇道を真っ直ぐ歩けば\x01",
            "墓地がありますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_246F")

    label("loc_2401")


    #C0110
    ChrTalk(
        0xFE,
        (
            "お墓参りに来たのでしたら、\x01",
            "脇道を真っ直ぐ歩いてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "この地に眠る魂たちも\x01",
            "きっと喜ぶでしょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246F")

    TalkEnd(0xFE)
    Return()

    # Function_6_10D3 end

    def Function_7_2473(): pass

    label("Function_7_2473")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_24CB")

    #C0112
    ChrTalk(
        0xA,
        (
            "あっ、もうこんな時間……\x01",
            "早く帰らないと母ちゃんに怒られちゃうぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2752")

    label("loc_24CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_24D9")
    Jump("loc_2752")

    label("loc_24D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2565")

    #C0113
    ChrTalk(
        0xA,
        (
            "おいらたち、日曜学校がない日だけ\x01",
            "ここで遊ばせてもらってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "こんなに広いのに遊び場所に\x01",
            "使わないのは勿体無いよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2752")

    label("loc_2565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2573")
    Jump("loc_2752")

    label("loc_2573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_264D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_258E")
    Call(0, 10)
    Jump("loc_2648")

    label("loc_258E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_25F8")
    TurnDirection(0xA, 0x153, 0)

    #C0115
    ChrTalk(
        0xA,
        (
            "あ、もう帰っちゃうんだ。\x01",
            "……今度会ったら遊ぼうぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x153,
        "#1100Fうん、いいよ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2648")

    label("loc_25F8")


    #C0117
    ChrTalk(
        0xA,
        (
            "（ハミルめ……\x01",
            "  この子がいくらかわいいからって\x01",
            "  張り切りやがって～……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2648")

    Jump("loc_2752")

    label("loc_264D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_269F")

    #C0118
    ChrTalk(
        0xA,
        "このお姉さん、遊撃士なんだって。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        "あはは、見えないよな～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2752")

    label("loc_269F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_26AD")
    Jump("loc_2752")

    label("loc_26AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_26BB")
    Jump("loc_2752")

    label("loc_26BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_26C9")
    Jump("loc_2752")

    label("loc_26C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_26D7")
    Jump("loc_2752")

    label("loc_26D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_26E5")
    Jump("loc_2752")

    label("loc_26E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2752")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2700")
    Call(0, 9)
    Jump("loc_2752")

    label("loc_2700")


    #C0120
    ChrTalk(
        0xA,
        (
            "おいらとハミルは双子なんだけど、\x01",
            "こいつってば運動神経が\x01",
            "からきしなんだよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2752")

    TalkEnd(0xFE)
    Return()

    # Function_7_2473 end

    def Function_8_2756(): pass

    label("Function_8_2756")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_27B2")

    #C0121
    ChrTalk(
        0xB,
        (
            "門限があるのが子供の辛いところだね。\x01",
            "おなかもすいたし早く帰ろうっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A61")

    label("loc_27B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_27C0")
    Jump("loc_2A61")

    label("loc_27C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2837")

    #C0122
    ChrTalk(
        0xB,
        "ねぇタミル、今日はなにをする？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "外で走り回ってたら疲れるし、\x01",
            "シスターとおしゃべりしてようよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A61")

    label("loc_2837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2845")
    Jump("loc_2A61")

    label("loc_2845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_295B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2860")
    Call(0, 10)
    Jump("loc_2956")

    label("loc_2860")

    TurnDirection(0xB, 0x153, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2903")

    #C0124
    ChrTalk(
        0xB,
        (
            "あ、帰っちゃうんだ……\x01",
            "……ねぇ今度、一緒に本でも……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x153,
        (
            "#1109Fえへへ、いいよ～。\x01",
            "キーア本読むのスキだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        "（か、可愛いなぁ……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2956")

    label("loc_2903")


    #C0127
    ChrTalk(
        0xB,
        "（はぁ……かわいいなぁ……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0128
    ChrTalk(
        0x153,
        "#1105Fんー……？\x02",
    )

    CloseMessageWindow()

    label("loc_2956")

    Jump("loc_2A61")

    label("loc_295B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_29CF")

    #C0129
    ChrTalk(
        0xB,
        (
            "はぁ、はぁ……\x01",
            "……遊び疲れてきちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "タミル、お姉さんたちも\x01",
            "迷惑してるから帰ろうよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A61")

    label("loc_29CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_29DD")
    Jump("loc_2A61")

    label("loc_29DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_29EB")
    Jump("loc_2A61")

    label("loc_29EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_29F9")
    Jump("loc_2A61")

    label("loc_29F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2A07")
    Jump("loc_2A61")

    label("loc_2A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A15")
    Jump("loc_2A61")

    label("loc_2A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2A61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A30")
    Call(0, 9)
    Jump("loc_2A61")

    label("loc_2A30")


    #C0131
    ChrTalk(
        0xB,
        (
            "ぜぇぜぇ……\x01",
            "まったく、体力バカなんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A61")

    TalkEnd(0xFE)
    Return()

    # Function_8_2756 end

    def Function_9_2A65(): pass

    label("Function_9_2A65")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    #C0132
    ChrTalk(
        0xA,
        (
            "よーしハミル！\x01",
            "次は何して遊ぶ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xB,
        (
            "はぁ、はぁ……\x01",
            "ちょ、ちょっと待ってタミル。\x01",
            "少し休憩しようよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        "なんだよ、だらしないなぁ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_9_2A65 end

    def Function_10_2B14(): pass

    label("Function_10_2B14")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    #C0135
    ChrTalk(
        0xA,
        "よしハミル、今日は何して遊ぼうか？\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        "うーん、僕は家で遊んでたいんだけど……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x153,
        (
            "#1105Fわー、同じカオだ！\x01",
            "すごいねー！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x153, 400)
    TurnDirection(0xB, 0x153, 400)
    Sleep(400)

    #C0138
    ChrTalk(
        0xA,
        "えっ……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        "（か、かわいい……）\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x153,
        "#1110Fねーねー、なんで同じカオなの？\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "え、えっと……\x01",
            "おいらとハミルは双子なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        (
            "そ、そうなんだよ、不思議でしょ！？\x01",
            "一卵性双生児って言ってね……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x153,
        "#1111F……ソーセージ？\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#0004F（うーん、さすが子供同士……\x01",
            "  あっというまに馴染んじゃったな。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2D50")

    #C0145
    ChrTalk(
        0x102,
        "#0100F（ふふ、なんだか微笑ましいわね。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E39")

    label("loc_2D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2D9D")

    #C0146
    ChrTalk(
        0x103,
        (
            "#0203F（この人当たりの良さは\x01",
            "  キーアならではですよね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E39")

    label("loc_2D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2E39")

    #C0147
    ChrTalk(
        0x104,
        (
            "#0300F（コゾーどもめ……\x01",
            "  うちの愛娘に色目を使ったら\x01",
            "  ロイドが黙っちゃいないぜ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#0006F（な、なんでそこで\x01",
            "  俺が出て来るんだよ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E39")

    SetScenarioFlags(0xAE, 0)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_10_2B14 end

    def Function_11_2E53(): pass

    label("Function_11_2E53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2FE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F91")

    #C0149
    ChrTalk(
        0xC,
        (
            "#0802Fはいはい、子供たちー！\x01",
            "大人しく並んでね～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)

    #C0150
    ChrTalk(
        0xC,
        (
            "#0801F……んもう、ちっとも言う事\x01",
            "聞いてくれないんだから……\x02\x03",

            "#0809Fそっちがそのつもりなら、\x01",
            "お姉さんも遊んじゃうわよ～っ？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        "#0109F（エ、エステルさん……）\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x104,
        "#0309F（う～ん、楽しそうだなぁ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FE6")

    label("loc_2F91")


    #C0153
    ChrTalk(
        0xC,
        (
            "#0809Fいい加減にしないと\x01",
            "くすぐっちゃうぞっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        "あははは！\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        "きゃははは！\x02",
    )

    CloseMessageWindow()

    label("loc_2FE6")

    TalkEnd(0xFE)
    Return()

    # Function_11_2E53 end

    def Function_12_2FEA(): pass

    label("Function_12_2FEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_338F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C3")

    #C0156
    ChrTalk(
        0x101,
        (
            "#0002Fやあ、ヨシュア。\x01",
            "何だか楽しそうだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xD,
        (
            "#0902Fはは、ここの大司教さんに\x01",
            "届け物に来たんだけど……\x02\x03",

            "予想通りエステルが\x01",
            "子供たちに捕まっちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x103,
        "#0202Fノリノリですね。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x102,
        (
            "#0102Fふふ、エステルさん、\x01",
            "子供に好かれそうだものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xD,
        (
            "#0904Fそれはもう……\x01",
            "昔からモテモテなんだ。\x02\x03",

            "#0900F何ていうか、一つの才能と\x01",
            "言ってもいいくらいにね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFE)

    #C0161
    ChrTalk(
        0xD,
        (
            "#0903F……昨日は本当にありがとう。\x02\x03",

            "僕も、エステルも、\x01",
            "ずっと抱えてきた胸のつかえが\x01",
            "取れた気分なんだ。\x02\x03",

            "#0902F改めて礼を言わせて欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#0011Fい、いや……\x01",
            "大した事はしていないって。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        (
            "#0304Fま、礼を言うんだったら\x01",
            "あのとんでもない嬢ちゃんを\x01",
            "無事捕まえてからにしてくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xD,
        "#0909Fはは……それもそうですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 0)
    Jump("loc_338F")

    label("loc_32C3")


    #C0165
    ChrTalk(
        0xD,
        (
            "#0904F記念祭も最終日だね。\x02\x03",

            "#0900Fさすがに昨日ほど\x01",
            "忙しくはなさそうだけど\x01",
            "お互い気を抜かずに頑張ろう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338C")

    #C0166
    ChrTalk(
        0x101,
        (
            "#0002Fあ、ああ。\x02\x03",

            "#0003F（競売会の事はちょっと\x01",
            "  話せる雰囲気じゃないな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_338C")

    SetScenarioFlags(0x0, 4)

    label("loc_338F")

    TalkEnd(0xFE)
    Return()

    # Function_12_2FEA end

    def Function_13_3393(): pass

    label("Function_13_3393")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3452")

    #C0167
    ChrTalk(
        0xFE,
        (
            "エラルダ大司教の依頼で、\x01",
            "薬品の材料を届けに来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "エオリアが見繕ってくれたお陰で\x01",
            "実にスムーズに仕事が運んだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "流石、医師免許を持っている\x01",
            "だけのことはあるね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3452")

    TalkEnd(0xFE)
    Return()

    # Function_13_3393 end

    def Function_14_3456(): pass

    label("Function_14_3456")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_34D4")

    #C0170
    ChrTalk(
        0xFE,
        (
            "えーっと、この薬草に、\x01",
            "滋養効果のある木の実に……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "……うん、漏れはないみたい。\x01",
            "さっそく届けましょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D4")

    TalkEnd(0xFE)
    Return()

    # Function_14_3456 end

    def Function_15_34D8(): pass

    label("Function_15_34D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3573")

    #C0172
    ChrTalk(
        0xFE,
        (
            "まぁ、クロスベルの教会は\x01",
            "大変立派な造りをしていますのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "私が今まで行ったどの教区のものより\x01",
            "一回りも二回りも大きいですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_35F8")

    label("loc_3573")


    #C0174
    ChrTalk(
        0xFE,
        (
            "クロスベルの教会は\x01",
            "大変立派に造られていますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "七耀教会の総本山、\x01",
            "アルテリア法国の聖堂にも\x01",
            "ひけをとらないと思いますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35F8")

    TalkEnd(0xFE)
    Return()

    # Function_15_34D8 end

    def Function_16_35FC(): pass

    label("Function_16_35FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_11(0xA0, 0xDC, 0xDC, 0x3C, 0x64, 0x0)
    OP_68(13460, 3600, 9960, 0)
    MoveCamera(310, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31000, 0)
    SetChrPos(0x101, 600, 0, -6100, 0)
    SetChrPos(0x153, 0, 0, -4500, 0)
    SetChrPos(0xEF, -600, 0, -6100, 0)
    FadeToBright(1000, 0)
    OP_68(13460, 10600, 9960, 10000)
    PlaceName2(100, 40, "c_plac33", 0x0, 4000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_11(0xA0, 0xDC, 0xDC, 0x3C, 0x64, 0x0)
    OP_68(0, 900, -4500, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(17900, 0)
    OP_0D()

    #C0176
    ChrTalk(
        0x153,
        (
            "#1105F#5Pほえ～っ……\x02\x03",

            "#1110Fおっきな建物だけど\x01",
            "ここがキョウカイなの～？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#0004F#6Pああ……\x01",
            "クロスベル大聖堂だよ。\x02\x03",

            "#0001F当然キーアも、どこかの教会に\x01",
            "礼拝には行ってるはずだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x153, 0xB4, 0x1F4)

    #C0178
    ChrTalk(
        0x153,
        "#1100F#11P？？？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3861")

    #C0179
    ChrTalk(
        0x102,
        (
            "#0106F#5P普通の町にある礼拝堂は\x01",
            "ここまで大きくないと思うし……\x02\x03",

            "#0100Fキーアちゃんの記憶を取り戻す\x01",
            "きっかけにはならなさそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3980")

    label("loc_3861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_38F2")

    #C0180
    ChrTalk(
        0x103,
        (
            "#0206F#5P普通の町にある礼拝堂は\x01",
            "ここまで大きくはないですし……\x02\x03",

            "#0200Fキーアの記憶を取り戻す\x01",
            "きっかけにはならなさそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3980")

    label("loc_38F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3980")

    #C0181
    ChrTalk(
        0x104,
        (
            "#0306F#5Pま、普通の町にある礼拝堂は\x01",
            "ここまで大きくないだろうし……\x02\x03",

            "#0300Fキー坊の記憶を取り戻す\x01",
            "きっかけにはならなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3980")

    TurnDirection(0x101, 0xEF, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_END)), "loc_3BD4")

    #C0182
    ChrTalk(
        0x101,
        (
            "#0006F#12P……みたいだな。\x02\x03",

            "#0000Fまあいいや、まずは\x01",
            "マーブル先生に相談してみよう。\x02\x03",

            "教会にいる専門家を\x01",
            "紹介してくれるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3A9F")

    #C0183
    ChrTalk(
        0x102,
        (
            "#0104F#5Pそうね、マーブル先生なら\x01",
            "間違いはないでしょうし……\x02\x03",

            "#0102Fそれじゃ、日曜学校の\x01",
            "教室に行ってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BCC")

    label("loc_3A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3B37")

    #C0184
    ChrTalk(
        0x103,
        (
            "#0202F#5Pマーブル先生というと、\x01",
            "前にロイドさんたちが話していた\x01",
            "日曜学校のシスターの方ですね。\x02\x03",

            "では、日曜学校の\x01",
            "教室に行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BCC")

    label("loc_3B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3BCC")

    #C0185
    ChrTalk(
        0x104,
        (
            "#0302F#5Pマーブル先生っていうと、\x01",
            "前にロイドとお嬢が話していた\x01",
            "日曜学校のシスターだよな。\x02\x03",

            "そんじゃ、日曜学校の\x01",
            "教室に行ってみようぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BCC")

    OP_57(0x0)
    OP_5A()
    Jump("loc_3FC3")

    label("loc_3BD4")


    #C0186
    ChrTalk(
        0x101,
        (
            "#0006F#12P……みたいだな。\x02\x03",

            "#0000Fまあいいや、まずは\x01",
            "知り合いの人に相談してみるよ。\x02\x03",

            "昔、お世話になった\x01",
            "日曜学校の先生がいるんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3E97")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0187
    ChrTalk(
        0x102,
        (
            "#0105F#5Pあら、それって……\x01",
            "シスターのマーブル先生かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#0005F#12Pああ、そうだけど……\x02\x03",

            "#0004Fそっか、エリィも当然、\x01",
            "ここの日曜学校に行ってたんだよな。\x02\x03",

            "#0000Fお互い違う授業日だったから\x01",
            "会ったことはなかったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x102,
        (
            "#0102F#5Pふふ、そうね……\x01",
            "私はその後、留学もしちゃってるし。\x02\x03",

            "#0106Fうーん、小さな頃に会っていたら\x01",
            "もう少し進展があったのかしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        "#0005F#12Pへ……？\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x102,
        (
            "#0112F#5Pな、何でもない。\x02\x03",

            "#0104Fそれより、マーブル先生なら\x01",
            "間違いないと思うわ。\x02\x03",

            "#0100F早速、聖堂の中にある\x01",
            "日曜学校を訪ねてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FC0")

    label("loc_3E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3F2A")

    #C0192
    ChrTalk(
        0x103,
        (
            "#0202F#5Pなるほど。\x01",
            "それは打ってつけですね。\x02\x03",

            "では、日曜学校の\x01",
            "教室に行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        "#0000F#12Pああ、正面にある聖堂の中だ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FC0")

    label("loc_3F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3FC0")

    #C0194
    ChrTalk(
        0x104,
        (
            "#0300F#5Pなるほど。\x01",
            "そいつは打ってつけかもな。\x02\x03",

            "そんじゃ、日曜学校の\x01",
            "教室に行ってみようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        "#0000F#12Pああ、正面にある聖堂の中だ。\x02",
    )

    CloseMessageWindow()

    label("loc_3FC0")

    OP_57(0x0)
    OP_5A()

    label("loc_3FC3")

    SetChrPos(0x0, 0, 0, -4500, 0)
    SetScenarioFlags(0xA8, 1)
    OP_29(0x48, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_16_35FC end

    def Function_17_3FE0(): pass

    label("Function_17_3FE0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_68(-200, 2950, 35510, 0)
    MoveCamera(325, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24530, 0)
    SetChrPos(0x101, -500, 2000, 37440, 180)
    SetChrPos(0x153, 870, 2000, 38370, 180)
    SetChrPos(0xEF, -370, 2000, 39460, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_79(0x0)
    OP_68(-200, 2950, 31510, 4500)

    def lambda_40B6():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40B6)

    def lambda_40CB():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_40CB)

    def lambda_40E0():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_40E0)

    def lambda_40F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_40F5)
    Sleep(300)

    def lambda_4109():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_4109)
    Sleep(300)

    def lambda_411D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_411D)
    Sleep(1500)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    Sound(890, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)

    def lambda_4150():
        TurnDirection(0xFE, 0xEF, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4150)
    WaitChrThread(0x153, 1)

    def lambda_4161():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_4161)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xEF, 2)
    WaitChrThread(0x153, 2)
    OP_6F(0x1)

    #C0196
    ChrTalk(
        0x101,
        "#0000F#6Pさてと、次はウルスラ病院か。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    Sleep(100)
    TurnDirection(0xEF, 0x153, 500)

    #C0197
    ChrTalk(
        0x101,
        (
            "#0001F#5Pかなりの寄り道になるけど、\x01",
            "……なあキーア、疲れてないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x153,
        (
            "#1110F#12Pぜんぜんヘイキー！\x02\x03",

            "#1109Fさんぽって楽しいね！\x01",
            "キーア、歩くのダイスキ！\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        "#0012F#5Pはは、元気だなぁ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_42FC")

    #C0200
    ChrTalk(
        0x102,
        (
            "#0109F#5Pふふ、それじゃあ\x01",
            "南口に行きましょうか。\x02\x03",

            "#0102Fバスに乗ればそれほど\x01",
            "時間は取られないでしょうし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43E3")

    label("loc_42FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4375")

    #C0201
    ChrTalk(
        0x103,
        (
            "#0202F#5Pクス……それでは\x01",
            "南口に行くとしましょう。\x02\x03",

            "#0204Fバスに乗ればそれほど\x01",
            "時間は取られないかと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43E3")

    label("loc_4375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_43E3")

    #C0202
    ChrTalk(
        0x104,
        (
            "#0304F#5Pハハ、そんじゃあ\x01",
            "南口に行くとしようぜ。\x02\x03",

            "#0302Fバスに乗りゃあ\x01",
            "あっという間に着くだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43E3")

    OP_93(0x153, 0x10E, 0x1F4)
    Sleep(300)

    #C0203
    ChrTalk(
        0x153,
        "#1110F#12Pおー、れっつごー！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 2000, 32200, 180)
    SetScenarioFlags(0xA8, 3)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_17_3FE0 end

    def Function_18_4433(): pass

    label("Function_18_4433")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0204
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～クロスベル大聖堂寄宿舎～\x01",
            "　　参拝の方は礼拝堂へ\x01",
            "　    お回り下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_4433 end

    SaveToFile()

Try(main)
