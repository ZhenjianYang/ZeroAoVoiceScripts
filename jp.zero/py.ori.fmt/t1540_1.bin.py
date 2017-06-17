from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1540_1.bin",                # FileName
        "t1540",                    # MapName
        "t1540",                    # Location
        0x0051,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 81, 0, 1, 0, 3],
    )

    BuildStringList((
        "t1540_1",                # 0
    ))

    ScpFunction((
        "Function_0_15C",          # 00, 0
        "Function_1_739",          # 01, 1
        "Function_2_A70",          # 02, 2
        "Function_3_FD9",          # 03, 3
        "Function_4_1214",         # 04, 4
        "Function_5_1218",         # 05, 5
        "Function_6_21C9",         # 06, 6
        "Function_7_33B6",         # 07, 7
        "Function_8_4076",         # 08, 8
        "Function_9_4936",         # 09, 9
        "Function_10_519B",        # 0A, 10
        "Function_11_5272",        # 0B, 11
        "Function_12_5314",        # 0C, 12
        "Function_13_5527",        # 0D, 13
        "Function_14_5703",        # 0E, 14
        "Function_15_574F",        # 0F, 15
        "Function_16_5A66",        # 10, 16
        "Function_17_5CF4",        # 11, 17
        "Function_18_6010",        # 12, 18
        "Function_19_61E7",        # 13, 19
        "Function_20_62F6",        # 14, 20
        "Function_21_6344",        # 15, 21
        "Function_22_64B0",        # 16, 22
        "Function_23_66A5",        # 17, 23
        "Function_24_671D",        # 18, 24
        "Function_25_6938",        # 19, 25
        "Function_26_6B2C",        # 1A, 26
        "Function_27_6E0A",        # 1B, 27
        "Function_28_719B",        # 1C, 28
        "Function_29_7479",        # 1D, 29
        "Function_30_7743",        # 1E, 30
        "Function_31_79C6",        # 1F, 31
        "Function_32_7C39",        # 20, 32
        "Function_33_7E4D",        # 21, 33
        "Function_34_8074",        # 22, 34
        "Function_35_82C0",        # 23, 35
        "Function_36_841C",        # 24, 36
        "Function_37_854A",        # 25, 37
        "Function_38_87D3",        # 26, 38
        "Function_39_883B",        # 27, 39
        "Function_40_8AFF",        # 28, 40
        "Function_41_8C9B",        # 29, 41
        "Function_42_8F47",        # 2A, 42
        "Function_43_925D",        # 2B, 43
        "Function_44_941E",        # 2C, 44
        "Function_45_9579",        # 2D, 45
        "Function_46_98B0",        # 2E, 46
        "Function_47_9CA1",        # 2F, 47
        "Function_48_9E23",        # 30, 48
        "Function_49_9F3E",        # 31, 49
    ))


    def Function_0_15C(): pass

    label("Function_0_15C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F0")
    Jump("loc_23A")

    label("loc_1F0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_210")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A")

    label("loc_210")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_230")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23A")

    label("loc_230")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_26D")
    Jump("loc_731")

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_27B")
    Jump("loc_731")

    label("loc_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_289")
    Jump("loc_731")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_297")
    Jump("loc_731")

    label("loc_297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2A5")
    Jump("loc_731")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2B3")
    Jump("loc_731")

    label("loc_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C1")
    Jump("loc_731")

    label("loc_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2CF")
    Jump("loc_731")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2DD")
    Jump("loc_731")

    label("loc_2DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2EB")
    Jump("loc_731")

    label("loc_2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2F9")
    Jump("loc_731")

    label("loc_2F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_307")
    Jump("loc_731")

    label("loc_307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_3DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A7")

    #C0001
    ChrTalk(
        0xFE,
        (
            "そういえば、\x01",
            "ヨアヒム先生によると\x01",
            "明日退院らしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "うあ～、仕事が溜まってんだろうなぁ。\x01",
            "もうちょっと寝てたいかも……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3D6")

    label("loc_3A7")


    #C0003
    ChrTalk(
        0xFE,
        (
            "はぁ、折角明日退院だってのに\x01",
            "憂鬱だよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D6")

    Jump("loc_731")

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_638")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D")

    #C0004
    ChrTalk(
        0xFE,
        (
            "お、君たち。\x01",
            "屋上の調査はどうだった？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0001Fはい、まだ謎は残っていますが……\x01",
            "獣がいた形跡は見つかりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "ほ、ほんとかい！？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "うーん、やっぱり夢じゃ\x01",
            "なかったのかな………………\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "……うん、どうもありがとう。\x01",
            "それが分かっただけでも\x01",
            "僕にとっちゃ収穫だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        "#0100Fどういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#0200Fそれでは……\x01",
            "セシルさんにも\x01",
            "報告に行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_5B5")

    #C0011
    ChrTalk(
        0x104,
        (
            "#0300F病棟の３階奥の個室に\x01",
            "行ってるって話だな。\x01",
            "早速行ってみようぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_605")

    label("loc_5B5")


    #C0012
    ChrTalk(
        0x104,
        (
            "#0300Fナースセンターで聞けば\x01",
            "どこにいるか分かるだろ。\x01",
            "早速行ってみようぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_605")

    SetScenarioFlags(0x0, 0)
    Jump("loc_633")

    label("loc_60D")


    #C0013
    ChrTalk(
        0xFE,
        "やっぱり夢じゃなかったのかな……\x02",
    )

    CloseMessageWindow()

    label("loc_633")

    Jump("loc_731")

    label("loc_638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D1")

    #C0014
    ChrTalk(
        0xFE,
        (
            "うーん……やっぱり\x01",
            "気のせいだったのかなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "実際ただの夢だったらいいんだけど、\x01",
            "こうして全身ケガしてるわけだし……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_723")

    label("loc_6D1")


    #C0016
    ChrTalk(
        0xFE,
        (
            "……とにかく調査の方は頼むよ。\x01",
            "夢にしろ現実にしろ、\x01",
            "原因は知っておきたいし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_723")

    Jump("loc_731")

    label("loc_728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_731")

    label("loc_731")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_0_15C end

    def Function_1_739(): pass

    label("Function_1_739")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_80B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_757")
    Call(1, 2)
    Jump("loc_806")

    label("loc_757")

    TurnDirection(0xC, 0x9, 0)
    OP_4B(0xC, 0xFF)

    #C0017
    ChrTalk(
        0xFE,
        "えへへ、また失敗しちゃいました。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "どんまいどんまい、わたし。\x01",
            "人間、生きていればだれにでも\x01",
            "間違いはありますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xC,
        "あんたは間違いありすぎだっつの。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_806")

    Jump("loc_A6C")

    label("loc_80B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_819")
    Jump("loc_A6C")

    label("loc_819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_827")
    Jump("loc_A6C")

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_835")
    Jump("loc_A6C")

    label("loc_835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_843")
    Jump("loc_A6C")

    label("loc_843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_851")
    Jump("loc_A6C")

    label("loc_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_85F")
    Jump("loc_A6C")

    label("loc_85F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87A")
    Call(1, 2)
    Jump("loc_8D7")

    label("loc_87A")


    #C0020
    ChrTalk(
        0xFE,
        (
            "ミハイル君ならエイダちゃんと\x01",
            "散歩にでてるよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "たぶん、水辺のところじゃないかな？\x02",
    )

    CloseMessageWindow()

    label("loc_8D7")

    Jump("loc_A6C")

    label("loc_8DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8EA")
    Jump("loc_A6C")

    label("loc_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8F8")
    Jump("loc_A6C")

    label("loc_8F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_960")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_913")
    Call(1, 3)
    Jump("loc_95B")

    label("loc_913")


    #C0022
    ChrTalk(
        0xFE,
        (
            "うふふ……\x01",
            "体温計がこれだけあれば\x01",
            "どんなに失敗しても大丈夫ですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95B")

    Jump("loc_A6C")

    label("loc_960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97B")
    Call(1, 3)
    Jump("loc_9BD")

    label("loc_97B")


    #C0023
    ChrTalk(
        0xFE,
        (
            "ふふ、失敗失敗。\x01",
            "体温計はこっちのポッケに\x01",
            "入ってたんでした。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BD")

    Jump("loc_A6C")

    label("loc_9C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_9D0")
    Jump("loc_A6C")

    label("loc_9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_9DE")
    Jump("loc_A6C")

    label("loc_9DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_A63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F9")
    Call(1, 2)
    Jump("loc_A5E")

    label("loc_9F9")


    #C0024
    ChrTalk(
        0xFE,
        (
            "ふぅ……\x01",
            "メイファちゃんったら\x01",
            "怒りっぽいんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "あとでゲバルさんのとこに\x01",
            "行かなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5E")

    Jump("loc_A6C")

    label("loc_A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A6C")

    label("loc_A6C")

    TalkEnd(0xFE)
    Return()

    # Function_1_739 end

    def Function_2_A70(): pass

    label("Function_2_A70")

    TurnDirection(0x9, 0xC, 0)
    TurnDirection(0xC, 0x9, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BB5")

    #C0026
    ChrTalk(
        0xC,
        (
            "シロン、あんたねぇ……\x01",
            "コーヒー淹れるのもロクにできないわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xC,
        (
            "なんでコーヒーから\x01",
            "紅茶の香りがするのよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "うーん、多分だけど……\x01",
            "コーヒーとお紅茶を\x01",
            "一緒に淹れちゃったのかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        (
            "そんなの分かってるわよ！\x01",
            "だから、なんでそーなるんだって……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xC,
        "……はぁ、正直疲れてきたわ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_FCA")

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_BC3")
    Jump("loc_FCA")

    label("loc_BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BD1")
    Jump("loc_FCA")

    label("loc_BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BDF")
    Jump("loc_FCA")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_BED")
    Jump("loc_FCA")

    label("loc_BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_BFB")
    Jump("loc_FCA")

    label("loc_BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_C09")
    Jump("loc_FCA")

    label("loc_C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_DB8")

    #C0031
    ChrTalk(
        0x9,
        (
            "ねーメイファちゃん。\x01",
            "ミハイルくんって、結局なんの病気なの？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xC,
        (
            "んー……結構難しい病気で、\x01",
            "完治するには手術が必要らしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xC,
        (
            "でも、外科ってなんだか怖いじゃない？\x01",
            "ミハイル君もご多分に漏れず\x01",
            "手術に踏み切れずにいるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        "ふぅん、そうなんだぁ……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "手術する勇気が芽生えたら\x01",
            "ミハイル君も治るのにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            "なにかいいキッカケが\x01",
            "あればいいのにな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xC,
        (
            "あんた……ごくたまに\x01",
            "マトモなこと言うわよね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FCA")

    label("loc_DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_DC6")
    Jump("loc_FCA")

    label("loc_DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_DD4")
    Jump("loc_FCA")

    label("loc_DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_DE2")
    Jump("loc_FCA")

    label("loc_DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_DF0")
    Jump("loc_FCA")

    label("loc_DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_DFE")
    Jump("loc_FCA")

    label("loc_DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_E0C")
    Jump("loc_FCA")

    label("loc_E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_FC1")

    #C0038
    ChrTalk(
        0xC,
        (
            "あんた昨日……ゲバルさんのシーツに\x01",
            "トマトソースぶちまけたんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "そーなの。\x01",
            "あれはびっくりしちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "たまたま回診に来た先生が\x01",
            "大出血と勘違いして倒れちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xC,
        "あ、あんたねぇ……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "とにかく、シーツはなんとか\x01",
            "洗えたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xC,
        (
            "あんたはちゃんと\x01",
            "新しいシーツを持って\x01",
            "ゲバルさんに謝りなさいよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "えぇ～……私、あのおじさん\x01",
            "あんまり好きじゃないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xC,
        "不満そうに言うな！\x02",
    )

    CloseMessageWindow()
    Jump("loc_FCA")

    label("loc_FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_FCA")

    label("loc_FCA")

    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_2_A70 end

    def Function_3_FD9(): pass

    label("Function_3_FD9")

    TurnDirection(0x9, 0x1B, 0)
    SetChrSubChip(0x1B, 0x2)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_FF6")
    Jump("loc_1208")

    label("loc_FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1100")

    #C0046
    ChrTalk(
        0x9,
        (
            "はーい、今日も検温の時間ですよ。\x01",
            "体温計入れましょうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x1B,
        (
            "……か、看護師さん。\x01",
            "それは良いんだけど……\x01",
            "なんで１０本も体温計を持ってるんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "これだけあれば計ってる最中に折れても\x01",
            "一本くらいは正常に計測できますから！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x1B,
        "（ふ、不安……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1208")

    label("loc_1100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1208")

    #C0050
    ChrTalk(
        0x9,
        (
            "はーい、検温の時間ですよ。\x01",
            "体温計入れましょうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x1B,
        (
            "……か、看護師さん。\x01",
            "昨日みたいに間違えて\x01",
            "注射針を持ってきてないでしょうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "やだぁ、大丈夫ですよ。\x01",
            "さすがの私でも二度も同じ\x01",
            "間違いなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        "…………あっ。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x1B,
        "…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_1208")

    SetScenarioFlags(0x0, 1)
    SetChrSubChip(0x1B, 0x0)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_3_FD9 end

    def Function_4_1214(): pass

    label("Function_4_1214")

    Call(1, 5)
    Return()

    # Function_4_1214 end

    def Function_5_1218(): pass

    label("Function_5_1218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_122E")
    Call(0, 11)
    Jump("loc_21C8")

    label("loc_122E")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_13F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1388")

    #C0055
    ChrTalk(
        0xA,
        "あと何日かで久しぶりの休日です。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        (
            "うふふ、ランディさん……\x01",
            "またみんなで遊びに行きましょうね！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#0300Fおう、待ってるぜ！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1380")

    #C0058
    ChrTalk(
        0x10A,
        (
            "#0603F……この私の前で勤務中に\x01",
            "遊びの約束とはいい度胸だな。\x02\x03",

            "#0600Fお前が一課の人間なら、\x01",
            "あとで死ぬほどの始末書を\x01",
            "書かせてやるところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        "#0305Fげっ……！？\x02",
    )

    CloseMessageWindow()

    label("loc_1380")

    SetScenarioFlags(0x0, 3)
    Jump("loc_13F0")

    label("loc_1388")


    #C0060
    ChrTalk(
        0xA,
        (
            "記念祭以来、ようやく\x01",
            "休みがとれそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "ランとエイダも誘ってるので、\x01",
            "また遊びましょうね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F0")

    Jump("loc_21C5")

    label("loc_13F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1468")

    #C0062
    ChrTalk(
        0xA,
        "そろそろ夕食の時間ですね～。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        (
            "キルシュ寮長のところに\x01",
            "患者さん用の食事を取りに行かないと～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C5")

    label("loc_1468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_14C8")

    #C0064
    ChrTalk(
        0xA,
        (
            "今日運び込まれた患者さん、\x01",
            "怪我の軽い方は２０１号室で\x01",
            "寝てもらってますよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C5")

    label("loc_14C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_16C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1612")

    #C0065
    ChrTalk(
        0xA,
        (
            "ゲバル議員っていうオジサンが\x01",
            "３階の個室に入院してるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xA,
        (
            "この間酔っ払って\x01",
            "ナースステーションに入ってきて、\x01",
            "酌をしろなんて言ってきたんですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        (
            "その後すぐに師長が戻ってきて\x01",
            "追い出されちゃいましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "まったく、看護師をホステスか何かと\x01",
            "勘違いしてるんじゃないですかね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_16C0")

    label("loc_1612")


    #C0069
    ChrTalk(
        0xA,
        (
            "ゲバル議員さんみたいに、\x01",
            "たま～に迷惑な人がいるんですよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "居心地がいいから退院しないとか、\x01",
            "看護師にセクハラしたりだとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        "まったく、イヤになりますね～。\x02",
    )

    CloseMessageWindow()

    label("loc_16C0")

    Jump("loc_21C5")

    label("loc_16C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_175D")

    #C0072
    ChrTalk(
        0xA,
        (
            "ほっぺた膨らました女の子が\x01",
            "下の階に向かって走って行きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        (
            "なんだか怒ってたみたいですけど……\x01",
            "それにしても可愛かったなぁ～㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C5")

    label("loc_175D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_17B8")

    #C0074
    ChrTalk(
        0xA,
        "あ、弟君じゃない。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        (
            "セシル先輩なら\x01",
            "３０１号室の方に行ってるわよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C5")

    label("loc_17B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1844")

    #C0076
    ChrTalk(
        0xA,
        (
            "先生方がいないと\x01",
            "なんだか不安ですね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "研修医の皆さんも優秀とは聞きますけど、\x01",
            "やっぱり教授の方には適いませんよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C5")

    label("loc_1844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1906")

    #C0078
    ChrTalk(
        0xA,
        "お腹空きました～……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "看護師の昼休憩は交代制なので\x01",
            "よく昼ごはんどきを\x01",
            "逃しちゃうんですよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        (
            "検温の時にお腹が鳴ったりすると\x01",
            "結構恥ずかしいんですよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1942")

    label("loc_1906")


    #C0081
    ChrTalk(
        0xA,
        "（くぅ～……）\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        "はぁ……早く昼休憩に行きたいです。\x02",
    )

    CloseMessageWindow()

    label("loc_1942")

    Jump("loc_21C5")

    label("loc_1947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1ACE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7E")

    #C0083
    ChrTalk(
        0xA,
        (
            "本当は明日もう１日だけ\x01",
            "休みがほしいんですよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "だって、明日はパレードですよ？\x01",
            "これを見なきゃ\x01",
            "記念祭じゃないですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "警察の皆さんがうらやましいです。\x01",
            "仕事にかこつけてパレードを\x01",
            "見ることもできるんじゃないですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#0006Fさ、さすがに\x01",
            "そんなことはしない……かな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1AC9")

    label("loc_1A7E")


    #C0087
    ChrTalk(
        0xA,
        (
            "明日のパレードも見たいですけど……\x01",
            "まぁ、仕事だし仕方ありませんね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC9")

    Jump("loc_21C5")

    label("loc_1ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B6E")

    #C0088
    ChrTalk(
        0xA,
        (
            "今日は、昨日仕事に出てくれてた\x01",
            "メイファとシロンが休みなんです～。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xA,
        (
            "わたし達は昨日充分楽しんだし、\x01",
            "今日一日がんばらないといけませんね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C5")

    label("loc_1B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C59")

    #C0090
    ChrTalk(
        0xA,
        (
            "あのイリア・プラティエの知り合いが\x01",
            "こんな近い所にいたなんて驚きです～。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        (
            "……セシル先輩に\x01",
            "イリアのサインとか頼んじゃ\x01",
            "だめでしょうかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#0000F（イリアさんのファン……\x01",
            "  こんなに多いんだなあ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1CD2")

    label("loc_1C59")


    #C0093
    ChrTalk(
        0xA,
        (
            "……セシル先輩に\x01",
            "イリアのサインとか頼んじゃ\x01",
            "だめでしょうかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        (
            "今度タイミングを見計らって\x01",
            "頼んでみようかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD2")

    Jump("loc_21C5")

    label("loc_1CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1D84")

    #C0095
    ChrTalk(
        0xA,
        (
            "あーあ、アルカンシェルのチケットは\x01",
            "結局取れませんでした～。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xA,
        (
            "師長は見た事あるって自慢してたけど、\x01",
            "きっと今のアルカンシェルの方が\x01",
            "すごいはずですよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C5")

    label("loc_1D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1DD6")

    #C0097
    ChrTalk(
        0xA,
        "３６度６分……異常なしですね～。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        "次はリットンさんかな～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21C5")

    label("loc_1DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1E56")

    #C0099
    ChrTalk(
        0xA,
        (
            "……マーサ師長は地獄耳だから\x01",
            "ちょっと怖いですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        (
            "どこで聞かれてるか分からないから\x01",
            "気をつけないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C5")

    label("loc_1E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_21BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_215C")

    #C0101
    ChrTalk(
        0xA,
        (
            "あ、セシル先輩。\x01",
            "お疲れさまでーす。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xA,
        (
            "もうすぐ休憩時間が\x01",
            "終わっちゃいますけど……\x01",
            "どうかしたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x136,
        (
            "#1300Fこの子たちのお手伝いをしてるのよ。\x01",
            "ごめんね、急いで戻るから。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "あ、いえいえ～\x01",
            "少しくらいなら大丈夫だと思います。\x01",
            "……えっと、そちらの方達は？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        (
            "#0304Fいきなりごめん。\x01",
            "俺はランディっていうんだ。\x02\x03",

            "#0300F……君の名前は？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        "えっと、フィリアですけど～……？\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#0006Fあぁもう、ランディはちょっと\x01",
            "静かにしててくれ……\x02\x03",

            "#0000F……コホン、申し遅れました。\x01",
            "警察・特務支援課のロイドといいます。\x02\x03",

            "研修医のリットンさんが襲われた件で\x01",
            "捜査に来ていまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        "はぁ、あの事件ですか～。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        (
            "（もしかして、この人が\x01",
            "  セシル先輩の言ってた……）\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        "……ふふ、がんばってくださいね～。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#0003F（な、なんだろう今の間は……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 1)
    Jump("loc_21B7")

    label("loc_215C")


    #C0112
    ChrTalk(
        0xA,
        "調査の方、頑張ってくださいね～。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#0003F（何だかいやに\x01",
            "  ニコニコしてるなぁ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B7")

    Jump("loc_21C5")

    label("loc_21BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_21C5")

    label("loc_21C5")

    TalkEnd(0xA)

    label("loc_21C8")

    Return()

    # Function_5_1218 end

    def Function_6_21C9(): pass

    label("Function_6_21C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21F0")
    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_21EB")
    SetScenarioFlags(0x0, 5)

    label("loc_21EB")

    Jump("loc_33B5")

    label("loc_21F0")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2270")

    #C0114
    ChrTalk(
        0xB,
        "さて、今日も一日がんばって働くかね。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xB,
        (
            "私たち看護師は患者のために\x01",
            "精一杯やれることをやっていかないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B2")

    label("loc_2270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_237A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2324")
    TurnDirection(0xB, 0x103, 0)

    #C0116
    ChrTalk(
        0xB,
        (
            "……おや、ティオちゃん。\x01",
            "なんだか顔色が悪くないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        (
            "#0203F……そんな事はありません。\x01",
            "お気になさらず……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xB,
        "んん……気のせいかねぇ？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2375")

    label("loc_2324")


    #C0119
    ChrTalk(
        0xB,
        "気のせいかねぇ……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xB,
        (
            "……まあ、そろそろ暗くなるし\x01",
            "気をつけて帰るんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2375")

    Jump("loc_33B2")

    label("loc_237A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_240A")

    #C0121
    ChrTalk(
        0xB,
        (
            "朝っぱらからてんやわんやだったけど\x01",
            "さっきようやく落ち着いたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        (
            "まぁなんにせよ、\x01",
            "患者が命を落とさずに済んでよかったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B2")

    label("loc_240A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2561")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24DC")

    #C0123
    ChrTalk(
        0xB,
        (
            "シズクちゃんは、この間から\x01",
            "随分明るくなった気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xB,
        (
            "なんでも、友達が出来たらしくって\x01",
            "嬉しそうに話してくれるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xB,
        (
            "ふふ、よかったよ。\x01",
            "友達は人生の宝だって言うしね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_255C")

    label("loc_24DC")


    #C0126
    ChrTalk(
        0xB,
        (
            "シズクちゃんは、この間から\x01",
            "随分明るくなった気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        (
            "これも友達が出来たおかげかね。\x01",
            "あたしたちもなんだか嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_255C")

    Jump("loc_33B2")

    label("loc_2561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2677")

    #C0128
    ChrTalk(
        0xB,
        "セシルはほんと、よく働く娘だよ。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xB,
        (
            "おまけに他の看護師や医師、\x01",
            "患者さんたちからの信頼も厚いときてる。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "師長の座は是非ともセシルに\x01",
            "引き継ぎたいもんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#0006Fな、なんかいきなり\x01",
            "すごい話を聞いたような……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xB,
        "はは、まだまだ先の話さ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_270C")

    label("loc_2677")


    #C0133
    ChrTalk(
        0xB,
        (
            "師長の座は是非ともセシルに\x01",
            "引き継ぎたいもんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        (
            "まァ、あたしゃあと２０年は\x01",
            "現役でやってくつもりだから、\x01",
            "先の長い話になっちまうけどねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_270C")

    Jump("loc_33B2")

    label("loc_2711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_283B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C9")

    #C0135
    ChrTalk(
        0xB,
        (
            "３０２号室に入院してるゲバルさん、\x01",
            "早く退院してくれないかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "看護師たちにも他の仕事があるんだ、\x01",
            "仮病の相手してやってるほど\x01",
            "暇じゃないんだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2836")

    label("loc_27C9")


    #C0137
    ChrTalk(
        0xB,
        (
            "……まあ、患者さんである限りは\x01",
            "無理に追い出したりも出来ないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        "飽きるまで待つしかないのかねぇ……\x02",
    )

    CloseMessageWindow()

    label("loc_2836")

    Jump("loc_33B2")

    label("loc_283B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_293E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28DB")

    #C0139
    ChrTalk(
        0xB,
        (
            "……ふぅ。\x01",
            "看護師たちをまとめあげるってのも\x01",
            "なかなか大変だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xB,
        (
            "ま、セシルが入ってからは\x01",
            "少しずつ楽させてもらってるけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2939")

    label("loc_28DB")


    #C0141
    ChrTalk(
        0xB,
        (
            "セシルには\x01",
            "看護主任みたいなことを\x01",
            "やってもらってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        "お陰で随分助けられてるよ。\x02",
    )

    CloseMessageWindow()

    label("loc_2939")

    Jump("loc_33B2")

    label("loc_293E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A10")

    #C0143
    ChrTalk(
        0xB,
        "フィリアもまだまだだねぇ。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xB,
        (
            "お腹が空くのは仕方ないけど、\x01",
            "なにも真面目に\x01",
            "昼休憩を待つ事はないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "移動中やあたしが見ていない隙に、\x01",
            "バババっと食べる！\x01",
            "それくらいの度胸が欲しいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B2")

    label("loc_2A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2B87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF5")

    #C0146
    ChrTalk(
        0xB,
        (
            "セシルならシズクちゃんの病室に\x01",
            "行ってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xB,
        (
            "……シズクちゃんも難しい子でね。\x01",
            "お母さんを早くに亡くしたせいか\x01",
            "妙に大人びてしまっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xB,
        (
            "もっと子供らしく振舞っても\x01",
            "いいと思うんだけどねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2B82")

    label("loc_2AF5")


    #C0149
    ChrTalk(
        0xB,
        (
            "シズクちゃんは、\x01",
            "お母さんを早くに亡くしたせいか\x01",
            "妙に大人びてしまっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        (
            "もっと子供らしく振舞っても\x01",
            "いいと思うんだけどねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B82")

    Jump("loc_33B2")

    label("loc_2B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2C9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C1E")

    #C0151
    ChrTalk(
        0xB,
        (
            "あたしかい？\x01",
            "もちろん、昨日も出勤してたさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "患者さんは待ってくれないからね。\x01",
            "基本的にあたしたちに休みはないのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2C9A")

    label("loc_2C1E")


    #C0153
    ChrTalk(
        0xB,
        (
            "いざ患者さんが来た時の為に\x01",
            "病院が休むわけにはいかないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        (
            "ヨアヒム先生なんかは\x01",
            "サボリ癖がついてて困るんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C9A")

    Jump("loc_33B2")

    label("loc_2C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2D4E")

    #C0155
    ChrTalk(
        0xB,
        (
            "セシルがあのイリア・プラティエの\x01",
            "友達だって聞いて、若い子たちが\x01",
            "浮き足立ってるみたいだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "まったく、少しはセシルの\x01",
            "働きぶりを見習って欲しいんだが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B2")

    label("loc_2D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E66")

    #C0157
    ChrTalk(
        0xB,
        (
            "アルカンシェルの公演のチラシが\x01",
            "この病院にも届いたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        (
            "私が若い頃のアルカンシェルは\x01",
            "イリア・プラティエもいなかったし\x01",
            "劇団も今ほど有名じゃなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "今となってはクロスベル中に名が轟く\x01",
            "超有名な実力派劇団……\x01",
            "なんだか遠くに行っちまったねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2EBA")

    label("loc_2E66")


    #C0160
    ChrTalk(
        0xB,
        (
            "アルカンシェル……\x01",
            "私も若い頃はよく見に行ったものさ。\x01",
            "あぁ、なつかしいねぇ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EBA")

    Jump("loc_33B2")

    label("loc_2EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2FE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_2F5B")

    #C0161
    ChrTalk(
        0xB,
        (
            "しかしまぁ……\x01",
            "あのティオちゃんが\x01",
            "すっかり大きくなっちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        (
            "今日はもう、帰っちゃうんだろう？\x01",
            "時間が出来たらまたおいで。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE0")

    label("loc_2F5B")


    #C0163
    ChrTalk(
        0xB,
        (
            "あんたたちのおかげで\x01",
            "これ以上の魔獣の被害は\x01",
            "何とか喰いとめられそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xB,
        (
            "スタッフや患者たちの代わりに\x01",
            "礼を言わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FE0")

    Jump("loc_33B2")

    label("loc_2FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_31EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_3161")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B9")

    #C0165
    ChrTalk(
        0xB,
        (
            "一度会った患者さんのことは\x01",
            "絶対忘れないようにしてるんだが……\x01",
            "いや、それでも見違えたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xB,
        (
            "ティオちゃん、またおいで。\x01",
            "機会があったら、\x01",
            "ゆっくり話でもしようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_315C")

    label("loc_30B9")


    #C0167
    ChrTalk(
        0xB,
        (
            "そうそう、セシルがいるのは\x01",
            "３階の一番奥の病室だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "ちょっと訳アリだが\x01",
            "とってもイイ子がいてねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xB,
        (
            "できればアンタたちにも\x01",
            "見舞ってあげて欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_315C")

    Jump("loc_31EA")

    label("loc_3161")


    #C0170
    ChrTalk(
        0xB,
        (
            "ああ、すまないねぇ。\x01",
            "今ちょっと帳簿をつけていて\x01",
            "手が離せないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xB,
        (
            "悪いけど、用があるなら\x01",
            "外にいるフィリアに聞いてくれるかい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31EA")

    Jump("loc_33B2")

    label("loc_31EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_33A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3344")

    #C0172
    ChrTalk(
        0xB,
        (
            "おや、セシル。\x01",
            "お客さんの案内をしてるのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x136,
        "#1300Fはい、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セシルは師長に経緯を伝えた。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "なるほど、そういう事なら\x01",
            "案内してあげるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xB,
        (
            "支援課とかいったかい？\x01",
            "調査の方はよろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#0005Fは、はい。\x01",
            "（何だか迫力のある人だな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x103,
        "#0208F………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_33A4")

    label("loc_3344")


    #C0179
    ChrTalk(
        0xB,
        (
            "本当に魔獣が出たんなら\x01",
            "えらい事だからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xB,
        (
            "あんたたち、\x01",
            "調査の方はよろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33A4")

    Jump("loc_33B2")

    label("loc_33A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_33B2")

    label("loc_33B2")

    TalkEnd(0xB)

    label("loc_33B5")

    Return()

    # Function_6_21C9 end

    def Function_7_33B6(): pass

    label("Function_7_33B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_344D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D4")
    Call(1, 2)
    Jump("loc_3448")

    label("loc_33D4")


    #C0181
    ChrTalk(
        0xFE,
        (
            "はーっ、この子ってば\x01",
            "ほんと理解できないわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "シロンにモノを頼む私こそが\x01",
            "根本的な間違いな気がしてきた……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3448")

    Jump("loc_4072")

    label("loc_344D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_345B")
    Jump("loc_4072")

    label("loc_345B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3637")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35AB")

    #C0183
    ChrTalk(
        0xFE,
        (
            "うちの病院で使ってるシーツは\x01",
            "貿易商のハロルドさんから買ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "この間、その発注書をシロンに任せたら……\x01",
            "５０枚って言っておいたのに、\x01",
            "５００枚で注文しちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "５００枚よ、５００枚！\x01",
            "ハロルドさんが間違いに気づいて\x01",
            "教えてくれたから良かったものの……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "まったくシロンには困ったもんだわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3632")

    label("loc_35AB")


    #C0187
    ChrTalk(
        0xFE,
        (
            "ハロルドさん以外の業者だったら\x01",
            "絶対に５００枚のシーツを\x01",
            "買わされてたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "まったく、シロンったら\x01",
            "悪運だけは強いんだから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3632")

    Jump("loc_4072")

    label("loc_3637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3904")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_36D5")

    #C0189
    ChrTalk(
        0xFE,
        (
            "実はあのリボン、\x01",
            "シロンに乗せられて\x01",
            "買っちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "まったくシロンったら、\x01",
            "どれだけ私を翻弄すれば\x01",
            "気が済むのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_36D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3761")

    #C0191
    ChrTalk(
        0xFE,
        (
            "リボンを捨てずに済んで\x01",
            "良かったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "そこそこ長いし、\x01",
            "包装用にもなると思うわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "材料集め、頑張って頂戴ね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_3761")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3775")
    Call(1, 49)
    Jump("loc_38FF")

    label("loc_3775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3863")

    #C0194
    ChrTalk(
        0xFE,
        (
            "……最近はおとなしくしてたのに\x01",
            "シロンったら、またやらかしたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "レミフェリアから届いたばかりの\x01",
            "輸血用血液のパックを、\x01",
            "家庭用の冷凍庫に入れてたのよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "知らずに開けた時は\x01",
            "ほんと、心臓が飛び出るかと思ったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38FF")

    label("loc_3863")


    #C0197
    ChrTalk(
        0xFE,
        (
            "シロンのミスは、\x01",
            "よく“天然”とか言われるような\x01",
            "可愛いもんじゃないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "輸血用血液のパックを\x01",
            "家庭用冷凍庫に保存しとくなんて……\x01",
            "もう、テロよテロ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38FF")

    Jump("loc_4072")

    label("loc_3904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_3912")
    Jump("loc_4072")

    label("loc_3912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_3920")
    Jump("loc_4072")

    label("loc_3920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3A13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39D9")

    #C0199
    ChrTalk(
        0xFE,
        (
            "シロンのやつ……\x01",
            "わたしの部屋着を\x01",
            "勝手にどこかにもちだしたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "あれがないと部屋の中でまで\x01",
            "看護服を着るハメに……\x01",
            "さっさとシロンを問い詰めないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A0E")

    label("loc_39D9")


    #C0201
    ChrTalk(
        0xFE,
        (
            "シロンめ……どこ行ったのかしら。\x01",
            "私の服返せ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0E")

    Jump("loc_4072")

    label("loc_3A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3A85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A2E")
    Call(1, 2)
    Jump("loc_3A80")

    label("loc_3A2E")


    #C0202
    ChrTalk(
        0xFE,
        (
            "シズクちゃんといい\x01",
            "ミハイル君といい……\x01",
            "子供なのによくがんばってるのよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A80")

    Jump("loc_4072")

    label("loc_3A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3A93")
    Jump("loc_4072")

    label("loc_3A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3AA1")
    Jump("loc_4072")

    label("loc_3AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3BB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B4C")

    #C0203
    ChrTalk(
        0xFE,
        (
            "……むむっ……\x01",
            "シロンの奴がまたどこかで\x01",
            "へんてこな事をしてる気がする……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "……やだなぁ。\x01",
            "付き合い長いからって\x01",
            "妙なカンが働いちゃうわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BAF")

    label("loc_3B4C")


    #C0205
    ChrTalk(
        0xFE,
        (
            "はぁ……いくらシロンでも、\x01",
            "検温くらいは出来ると思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        "念の為、後で様子見に行こ……\x02",
    )

    CloseMessageWindow()

    label("loc_3BAF")

    Jump("loc_4072")

    label("loc_3BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3D96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF0")

    #C0207
    ChrTalk(
        0xFE,
        (
            "同僚のシロンのドジぶりは\x01",
            "それはもう半端じゃないわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "医療ミスすれすれの器具の間違いとか\x01",
            "アレな薬品を床にこぼしたりとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "ただ、大事になる前に\x01",
            "周りのみんながフォローするから\x01",
            "今のところ人的被害はゼロだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "はぁ、セシル先輩の爪のアカを\x01",
            "煎じて飲ませてやりたいわ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D91")

    label("loc_3CF0")


    #C0211
    ChrTalk(
        0xFE,
        (
            "シロンのドジぶりは半端じゃないのよ。\x01",
            "今まで人的被害が出てないのが\x01",
            "本当に不思議でならないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "はぁ、セシル先輩の爪のアカを\x01",
            "煎じて飲ませてやりたいわ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D91")

    Jump("loc_4072")

    label("loc_3D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_3E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E5D")

    #C0213
    ChrTalk(
        0xFE,
        "んがー、遅い！\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "シロンのやつ、\x01",
            "たかがシーツ干すくらいで\x01",
            "どんだけ時間かかってんの！\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "ああ、イヤな予感……\x01",
            "折角綺麗に洗ったシーツを\x01",
            "また汚してそうな気がするわ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E98")

    label("loc_3E5D")


    #C0216
    ChrTalk(
        0xFE,
        (
            "シロンのやつ……\x01",
            "またシーツを汚してないでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E98")

    Jump("loc_4072")

    label("loc_3E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_3F2E")

    #C0217
    ChrTalk(
        0xFE,
        (
            "シロンのやつ、\x01",
            "ちゃんとゲバル議員に\x01",
            "謝ってるでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "あの子、ほんとドジだから\x01",
            "なにがあってもおかしくないのよね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4072")

    label("loc_3F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_3FC8")

    #C0219
    ChrTalk(
        0xFE,
        "え、セシル先輩？\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "うーん、ナースステーションには\x01",
            "戻ってきてないと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "そのまま他の仕事をしに\x01",
            "行ったんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4072")

    label("loc_3FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_4069")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE3")
    Call(1, 2)
    Jump("loc_4064")

    label("loc_3FE3")


    #C0222
    ChrTalk(
        0xFE,
        (
            "シロンったら、\x01",
            "いっつもとんでもないミスを\x01",
            "やらかしちゃうのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "そのくせ患者さんには妙に人気だし……\x01",
            "意味わかんないわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4064")

    Jump("loc_4072")

    label("loc_4069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4072")

    label("loc_4072")

    TalkEnd(0xFE)
    Return()

    # Function_7_33B6 end

    def Function_8_4076(): pass

    label("Function_8_4076")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4087")
    Jump("loc_4932")

    label("loc_4087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_4095")
    Jump("loc_4932")

    label("loc_4095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_40A3")
    Jump("loc_4932")

    label("loc_40A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_40B1")
    Jump("loc_4932")

    label("loc_40B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_40BF")
    Jump("loc_4932")

    label("loc_40BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_40CD")
    Jump("loc_4932")

    label("loc_40CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_40DB")
    Jump("loc_4932")

    label("loc_40DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_40E9")
    Jump("loc_4932")

    label("loc_40E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_40F7")
    Jump("loc_4932")

    label("loc_40F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_43C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A4")

    #C0224
    ChrTalk(
        0xD,
        (
            "#1302Fあら、ロイド。\x01",
            "早速仕事を始めているのね。\x02\x03",

            "#1309Fふふ……\x01",
            "みんなも休みは有意義に過ごせた？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#0102Fそうですね……\x01",
            "久しぶりに実家で過ごせましたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x103,
        "#0202F……まあ、ノンビリとは出来ましたね。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x104,
        (
            "#0306Fいやでも、一日だけって\x01",
            "マジ休みが少なすぎッスよ。\x02\x03",

            "#0300F本当ならセシルさんとも\x01",
            "一緒に遊びたかったのになぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        (
            "#0004F（うーん、何だかんだいって\x01",
            "  充実した一日だったかな……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 5)
    Jump("loc_43BB")

    label("loc_42A4")


    #C0229
    ChrTalk(
        0xD,
        (
            "#1304F昨日は有意義にお休みを使えたわ。\x01",
            "リーシャさんのことも\x01",
            "イリアに紹介してもらったし……\x02\x03",

            "#1302Fそうそう、イリアったら\x01",
            "ロイドも誘ってくればいいのにって\x01",
            "残念そうだったわよ。\x02\x03",

            "#1309Fふふ、ロイドったら人気者ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        (
            "#0012Fオモチャ扱いされてる\x01",
            "だけのような気もするけどね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43BB")

    Jump("loc_4932")

    label("loc_43C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4717")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_466F")

    #C0231
    ChrTalk(
        0xD,
        (
            "#1300Fあっ、ロイド。\x01",
            "丁度よかったわ。\x02\x03",

            "実はね、イリアに\x01",
            "来月のアルカンシェル公演の\x01",
            "チケットを２枚もらってるのよ。\x02\x03",

            "#1309Fもしスケジュールが空いてたら\x01",
            "一緒に行かない？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#0009Fああ、ありがとう！\x01",
            "願ってもないことだよ。\x02\x03",

            "#0004F仕事が忙しいだろうから\x01",
            "日程が空くかはわからないけど……\x01",
            "ぜひ行ってみたいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xD,
        (
            "#1309Fうふふ、わかった。\x01",
            "じゃあ、キープしておくわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#0004F（あの練習風景だと……\x01",
            "  本番はきっと物凄いんだろうな。\x01",
            "  ……………………？）\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x103,
        "#0211F（じとー…………）\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x102,
        (
            "#0111F（仕事中にデートの約束、ね。\x01",
            "  ……良いご身分だこと。）\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x104,
        (
            "#0301F（この弟野郎……\x01",
            "  なんでお前だけっ……！！）\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        "#0006F（うっ……仲間の視線が痛い……！）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 4)
    Jump("loc_4712")

    label("loc_466F")


    #C0239
    ChrTalk(
        0xD,
        (
            "#1300Fアルカンシェルの公演……\x01",
            "一緒に見に行けるといいわね。\x02\x03",

            "#1309Fふふ、休みが取れるのを期待しておくわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        "#0011Fそ、そうだね……\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x103,
        "#0211F（じー……）\x02",
    )

    CloseMessageWindow()

    label("loc_4712")

    Jump("loc_4932")

    label("loc_4717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4725")
    Jump("loc_4932")

    label("loc_4725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_490D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4856")

    #C0242
    ChrTalk(
        0xD,
        "#1305Fあら？　ロイド、忘れ物？\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        (
            "#0000Fいや、そういうわけじゃ\x01",
            "ないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xD,
        (
            "#1305Fあっ、もしかして……\x01",
            "もう報告に来てくれたのかしら！？\x02\x03",

            "#1309Fエリィちゃんとティオちゃんと\x01",
            "ランディ君……\x02\x03",

            "結局誰と\x01",
            "付き合うことにしたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        "#0006F……そういうわけでもないから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4908")

    label("loc_4856")


    #C0246
    ChrTalk(
        0xD,
        (
            "#1300Fふふっ、冗談よ。\x02\x03",

            "また何かあったら……\x01",
            "いえ、何にもなくてもいいから\x01",
            "会いに来てちょうだいね。\x02\x03",

            "#1304F……さて。\x01",
            "シズクちゃんのところに\x01",
            "夕飯を持っていってあげないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4908")

    Jump("loc_4932")

    label("loc_490D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_491B")
    Jump("loc_4932")

    label("loc_491B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_4929")
    Jump("loc_4932")

    label("loc_4929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4932")

    label("loc_4932")

    TalkEnd(0xFE)
    Return()

    # Function_8_4076 end

    def Function_9_4936(): pass

    label("Function_9_4936")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_499E")
    OP_93(0xFE, 0x0, 0x0)

    #C0247
    ChrTalk(
        0xFE,
        (
            "簡単な手術だとて\x01",
            "なめてはいけない。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "安静にしていなさい。\x01",
            "……いいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5197")

    label("loc_499E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_4A27")

    #C0249
    ChrTalk(
        0xFE,
        (
            "あの患者……\x01",
            "特に暴れるようなそぶりを\x01",
            "見せることはないようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "……とりあえず、分別を弁えた\x01",
            "連中ではあるらしい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5197")

    label("loc_4A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B23")

    #C0251
    ChrTalk(
        0xFE,
        (
            "今朝、黒月とか言う組織の人間が\x01",
            "運び込まれてきてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "とりあえず、１人は話ができるまでに\x01",
            "回復したからこちらに移してきたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "しかし、明らかに負傷のしかたが\x01",
            "一般人のそれとは違う……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        "どうにも怪しい連中だよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4BDA")

    label("loc_4B23")


    #C0255
    ChrTalk(
        0xFE,
        (
            "今朝運ばれてきた、\x01",
            "黒月とか言う組織の人間だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "この部屋に移してきた者以外は\x01",
            "まだ安静が必要でな。\x01",
            "ＩＣＵの病室で眠っているだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        "しかし……どうにも怪しい連中だよ。\x02",
    )

    CloseMessageWindow()

    label("loc_4BDA")

    Jump("loc_5197")

    label("loc_4BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4BED")
    Jump("loc_5197")

    label("loc_4BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_4DF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D8D")

    #C0258
    ChrTalk(
        0xFE,
        (
            "さっきまで、シズクくんを\x01",
            "診察していたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "……彼女の症例は、\x01",
            "現在の医療技術では完治が難しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "外科・内科・神経科……\x01",
            "各々の分野の問題が複雑に干渉しあい、\x01",
            "治療への道を妨げているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "完全な失明には至っていないから\x01",
            "治癒の可能性は僅かにあるのだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFE)

    #C0262
    ChrTalk(
        0xFE,
        (
            "……私としたことが、\x01",
            "患者の事情を話すなど\x01",
            "軽率だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        "……今の話は忘れるように。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4DEF")

    label("loc_4D8D")


    #C0264
    ChrTalk(
        0xFE,
        (
            "……私としたことが、\x01",
            "患者の事情を話すなど\x01",
            "軽率だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        "……さっきの話は忘れるように。\x02",
    )

    CloseMessageWindow()

    label("loc_4DEF")

    Jump("loc_5197")

    label("loc_4DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_4E02")
    Jump("loc_5197")

    label("loc_4E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4E10")
    Jump("loc_5197")

    label("loc_4E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4E8C")

    #C0266
    ChrTalk(
        0xFE,
        "……健康体を診る趣味はないぞ。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "いまから回診だ。\x01",
            "他の患者の邪魔にならないうちに\x01",
            "出て行ってもらおう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5197")

    label("loc_4E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4E9A")
    Jump("loc_5197")

    label("loc_4E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F5C")

    #C0268
    ChrTalk(
        0xFE,
        "記念祭も２日目か……\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "浮かれて周囲が見えない時にこそ\x01",
            "怪我の危険は潜んでいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "また明日あたり、\x01",
            "クロスベル市の不良グループが\x01",
            "運ばれて来なければいいがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4FB2")

    label("loc_4F5C")


    #C0271
    ChrTalk(
        0xFE,
        (
            "浮かれて周囲が見えない時にこそ\x01",
            "怪我の危険は潜んでいる。\x01",
            "君たちも気をつけたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FB2")

    Jump("loc_5197")

    label("loc_4FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_503C")

    #C0272
    ChrTalk(
        0xFE,
        (
            "今回のは小さい手術だが……\x01",
            "手を抜くことは絶対にしない。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "それが外科医として\x01",
            "手術に臨む者の\x01",
            "最低限のルールだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5197")

    label("loc_503C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5105")
    OP_93(0xFE, 0xB4, 0x0)

    #C0274
    ChrTalk(
        0xFE,
        (
            "外科手術を怖がるのは\x01",
            "無理はないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "だが、今回の手術の危険度は\x01",
            "かなり低いと言えます。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "気に病む方が体に悪い。\x01",
            "どうか心を落ち着けて、\x01",
            "今日は早めに寝てください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5197")

    label("loc_5105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_5172")

    #C0277
    ChrTalk(
        0xFE,
        "これから２０２号室の回診だ。\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "君は入院患者ではないな？\x01",
            "暗くなるまえに家に帰りなさい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5197")

    label("loc_5172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_5180")
    Jump("loc_5197")

    label("loc_5180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_518E")
    Jump("loc_5197")

    label("loc_518E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5197")

    label("loc_5197")

    TalkEnd(0xFE)
    Return()

    # Function_9_4936 end

    def Function_10_519B(): pass

    label("Function_10_519B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51B0")
    Call(1, 12)
    Jump("loc_526E")

    label("loc_51B0")


    #C0279
    ChrTalk(
        0xFE,
        (
            "朝から粘ってたんだが……\x01",
            "そろそろ引き上げるとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "……にしても黒月ってのは\x01",
            "相当手強い相手みてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "ハナシすんのは初めてだが\x01",
            "構成員の末端まで\x01",
            "統率が取れている感じだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_526E")

    TalkEnd(0xFE)
    Return()

    # Function_10_519B end

    def Function_11_5272(): pass

    label("Function_11_5272")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5287")
    Call(1, 12)
    Jump("loc_5310")

    label("loc_5287")


    #C0282
    ChrTalk(
        0xFE,
        (
            "くそっ、捜査一課め。\x01",
            "前から気に入らなかったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "こっちの事件は\x01",
            "平気で横取りするくせに\x01",
            "こんな時だけこき使いやがってえ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5310")

    TalkEnd(0xFE)
    Return()

    # Function_11_5272 end

    def Function_12_5314(): pass

    label("Function_12_5314")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    TurnDirection(0xF, 0x0, 0)
    TurnDirection(0x10, 0x0, 0)

    #C0284
    ChrTalk(
        0xF,
        "ちっ、あれが黒月か。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xF,
        (
            "そろって口裏合わせやがって\x01",
            "可愛くねえ連中だぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0286
    ChrTalk(
        0x102,
        (
            "#0105F警部たちは\x01",
            "黒月の事情聴取ですか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x10,
        (
            "捜査一課の要請でね～。\x01",
            "入院組から調書取って来いってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x10,
        (
            "あんな口の固い連中が\x01",
            "ボロを出すわけ無いのにな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x10,
        (
            "くそう、捜査一課め。\x01",
            "絶対分かってて回したな～！\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#0011Fはは……\x01",
            "（形式だけの調書を取りに\x01",
            "  使われたみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x104,
        "#0306F（捜査二課も大変だなぁ。）\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x0)
    OP_93(0x10, 0x5A, 0x0)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Return()

    # Function_12_5314 end

    def Function_13_5527(): pass

    label("Function_13_5527")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_55BB")
    Jump("loc_5605")

    label("loc_55BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_55DB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5605")

    label("loc_55DB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55FB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5605")

    label("loc_55FB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5605")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5638")
    Jump("loc_56FB")

    label("loc_5638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_567B")

    #C0292
    ChrTalk(
        0xFE,
        (
            "もう夕方か……\x01",
            "ずっと寝ていると一日が短いわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56FB")

    label("loc_567B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_5689")
    Jump("loc_56FB")

    label("loc_5689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_56F2")

    #C0293
    ChrTalk(
        0xFE,
        (
            "研修医とはいえ、\x01",
            "医者が入院しておるとはのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        "医者の不養生というやつじゃろうか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_56FB")

    label("loc_56F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_56FB")

    label("loc_56FB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_5527 end

    def Function_14_5703(): pass

    label("Function_14_5703")

    TalkBegin(0xFE)

    #C0295
    ChrTalk(
        0xFE,
        (
            "さっきからドタバタうるさいのう。\x01",
            "もうちょい静かにしてくれんか。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_5703 end

    def Function_15_574F(): pass

    label("Function_15_574F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_57E3")
    Jump("loc_582D")

    label("loc_57E3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5803")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_582D")

    label("loc_5803")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5823")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_582D")

    label("loc_5823")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_582D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5860")
    Jump("loc_5A5E")

    label("loc_5860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_5894")

    #C0296
    ChrTalk(
        0xFE,
        "入院生活ってほんとヒマだなぁ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A5E")

    label("loc_5894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_58D5")

    #C0297
    ChrTalk(
        0xFE,
        (
            "あの美人の看護師さんなら\x01",
            "ここには来てないぞ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A5E")

    label("loc_58D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_5A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59D8")

    #C0298
    ChrTalk(
        0xFE,
        (
            "な、なんなんだ……\x01",
            "さっきのメガネの先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "治療の話をしてるかと思ったら\x01",
            "エスだのエムだの……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x136,
        (
            "#1306Fすいません、\x01",
            "あんまり気にしないで下さい。\x01",
            "ヨアヒム先生はああいう人なので……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x103,
        "#0200F……それで済ますのもどうかと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5A50")

    label("loc_59D8")


    #C0302
    ChrTalk(
        0xFE,
        (
            "さっきのメガネの先生……\x01",
            "とても医者には見えないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "でも准教授っていえば、\x01",
            "教授の次に偉い人なんだろうしな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A50")

    Jump("loc_5A5E")

    label("loc_5A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5A5E")

    label("loc_5A5E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_574F end

    def Function_16_5A66(): pass

    label("Function_16_5A66")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5AFA")
    Jump("loc_5B44")

    label("loc_5AFA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B1A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B44")

    label("loc_5B1A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B3A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B44")

    label("loc_5B3A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5B44")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5B77")
    Jump("loc_5CEC")

    label("loc_5B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_5BDA")

    #C0304
    ChrTalk(
        0xFE,
        "あのお婆さん、幸せそうね。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "うーん、私もちゃんと\x01",
            "退院できるようにがんばろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CEC")

    label("loc_5BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_5C5C")

    #C0306
    ChrTalk(
        0xFE,
        (
            "あのお婆さん……\x01",
            "お孫さんが見舞いに来てるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "いつもグチグチうるさかったけど\x01",
            "まぁよかったじゃない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CEC")

    label("loc_5C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_5CE3")

    #C0308
    ChrTalk(
        0xFE,
        (
            "はぁ、あのお婆さん……\x01",
            "見舞いが来ないって\x01",
            "前から愚痴ってんのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "こっちまで気が滅入っちゃうわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CEC")

    label("loc_5CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5CEC")

    label("loc_5CEC")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_5A66 end

    def Function_17_5CF4(): pass

    label("Function_17_5CF4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D88")
    Jump("loc_5DD2")

    label("loc_5D88")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5DA8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DD2")

    label("loc_5DA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DC8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DD2")

    label("loc_5DC8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DD2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5E05")
    Jump("loc_6008")

    label("loc_5E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_5E81")

    #C0310
    ChrTalk(
        0xFE,
        (
            "孫が見舞いに来てくれとったが\x01",
            "暗くならんうちに帰したわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "うむ……お陰で元気が出た。\x01",
            "頑張らねばな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6008")

    label("loc_5E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_5F4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E9C")
    Call(1, 19)
    Jump("loc_5F48")

    label("loc_5E9C")


    #C0312
    ChrTalk(
        0xFE,
        (
            "孫がわざわざ一人で\x01",
            "見舞いに来てくれてのう……\x01",
            "これほど嬉しいことはないのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "聞けば、息子夫婦も\x01",
            "相当に忙しかったようだし……\x01",
            "当たり散らした自分が恥ずかしいわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F48")

    Jump("loc_6008")

    label("loc_5F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_5FFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_END)), "loc_5F71")
    Call(1, 18)
    Jump("loc_5FD1")

    label("loc_5F71")


    #C0314
    ChrTalk(
        0xFE,
        (
            "ここに入院してから\x01",
            "家族の誰も迎えに来てくれんでな……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        "はぁ、孫娘に会いたいのう……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_5FD1")

    Jump("loc_5FFA")

    label("loc_5FD6")


    #C0316
    ChrTalk(
        0xFE,
        "はぁ……孫娘に会いたいのう……\x02",
    )

    CloseMessageWindow()

    label("loc_5FFA")

    Jump("loc_6008")

    label("loc_5FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6008")

    label("loc_6008")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_5CF4 end

    def Function_18_6010(): pass

    label("Function_18_6010")

    OP_93(0x30, 0xB4, 0x0)
    SetChrSubChip(0x15, 0x2)
    OP_4B(0x30, 0xFF)

    #C0317
    ChrTalk(
        0x15,
        (
            "ここに入院してから\x01",
            "家族の誰も迎えに来てくれんでな……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x15,
        "はぁ、孫娘に会いたいわい……\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x15,
        (
            "忙しいかなんか知らんが\x01",
            "息子夫婦には思いやりが欠けとる！\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x30,
        (
            "#2406Fそうですねぇ……\x01",
            "うん、それは嘆かわしい。\x02\x03",

            "#2400Fまぁ、それだけ元気があれば\x01",
            "退院もすぐでしょう。\x01",
            "お孫さんにもすぐ会えますよ。\x02\x03",

            "#2409Fそうだ、お菓子でもどうです？\x01",
            "気分が落ち着きますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x15,
        (
            "はぁ、優しくしてくれるのは\x01",
            "先生だけじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x101,
        "#0005F（な、なんか変な先生だな……）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    OP_4C(0x30, 0xFF)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 5)
    Return()

    # Function_18_6010 end

    def Function_19_61E7(): pass

    label("Function_19_61E7")

    TurnDirection(0x16, 0x15, 0)
    SetChrSubChip(0x15, 0x2)
    OP_4B(0x16, 0xFF)

    #C0323
    ChrTalk(
        0x16,
        (
            "おばあちゃん、聞いて！\x01",
            "あたし、初めて定期バスに\x01",
            "一人で乗ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x16,
        (
            "お父さんたちと乗るより\x01",
            "ずっとわくわくして楽しかった！\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x15,
        "そうかそうか、偉いのう。\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x15,
        (
            "どれ、さっきヨアヒム先生にもらった\x01",
            "飴玉をあげるかの。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x16,
        "わーい、ありがと！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_19_61E7 end

    def Function_20_62F6(): pass

    label("Function_20_62F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_630B")
    Call(1, 19)
    Jump("loc_6340")

    label("loc_630B")


    #C0328
    ChrTalk(
        0xFE,
        (
            "おばあちゃん、\x01",
            "思ったより元気そうでよかったっ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6340")

    TalkEnd(0xFE)
    Return()

    # Function_20_62F6 end

    def Function_21_6344(): pass

    label("Function_21_6344")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_63D8")
    Jump("loc_6422")

    label("loc_63D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_63F8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6422")

    label("loc_63F8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6418")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6422")

    label("loc_6418")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6422")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0329
    ChrTalk(
        0xFE,
        (
            "ヒザを痛めておったのじゃが\x01",
            "今日の様子だと退院も近いそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        "ほほ、たのしみじゃわい。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_6344 end

    def Function_22_64B0(): pass

    label("Function_22_64B0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6544")
    Jump("loc_658E")

    label("loc_6544")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6564")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_658E")

    label("loc_6564")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6584")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_658E")

    label("loc_6584")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_658E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_65C1")
    Jump("loc_669D")

    label("loc_65C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_663D")

    #C0331
    ChrTalk(
        0xFE,
        (
            "い、いよいよ今日は手術だ。\x01",
            "執刀医はこのベルダイン先生が\x01",
            "やるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        "……はぁ、どうにも緊張するよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_669D")

    label("loc_663D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_669D")

    #C0333
    ChrTalk(
        0xFE,
        "はぁ……憂鬱だなぁ。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "先生は簡単な手術だから\x01",
            "心配ないって言ってくれるけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_669D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_64B0 end

    def Function_23_66A5(): pass

    label("Function_23_66A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_66B6")
    Jump("loc_6719")

    label("loc_66B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_66F6")

    #C0335
    ChrTalk(
        0xFE,
        "んごー……んごー……\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        "ふがが、んごー……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6719")

    label("loc_66F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6719")

    #C0337
    ChrTalk(
        0xFE,
        "んごー……んごー……\x02",
    )

    CloseMessageWindow()

    label("loc_6719")

    TalkEnd(0xFE)
    Return()

    # Function_23_66A5 end

    def Function_24_671D(): pass

    label("Function_24_671D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_67B1")
    Jump("loc_67FB")

    label("loc_67B1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_67D1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67FB")

    label("loc_67D1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67F1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67FB")

    label("loc_67F1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67FB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_682E")
    Jump("loc_6930")

    label("loc_682E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_68CF")

    #C0338
    ChrTalk(
        0xFE,
        (
            "この病院、居心地がいいから\x01",
            "いついちゃうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "先生も看護師さんたちも優しいし……\x01",
            "うふふ、退院したくなくなっちゃったら\x01",
            "どうしようかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6930")

    label("loc_68CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6930")

    #C0340
    ChrTalk(
        0xFE,
        (
            "病院のベッドはラクでいいわね。\x01",
            "黙っていても料理が出てくるのなんて\x01",
            "何年ぶりかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6930")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_671D end

    def Function_25_6938(): pass

    label("Function_25_6938")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_69CC")
    Jump("loc_6A16")

    label("loc_69CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_69EC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A16")

    label("loc_69EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A0C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A16")

    label("loc_6A0C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A16")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6A49")
    Jump("loc_6B24")

    label("loc_6A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A64")
    Call(1, 3)
    Jump("loc_6A95")

    label("loc_6A64")


    #C0341
    ChrTalk(
        0xFE,
        (
            "一体何をしたら\x01",
            "体温計なんか折れるんだ……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A95")

    Jump("loc_6B24")

    label("loc_6A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6B24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AB5")
    Call(1, 3)
    Jump("loc_6B24")

    label("loc_6AB5")


    #C0342
    ChrTalk(
        0xFE,
        (
            "……この看護師さんのドジ相手じゃ\x01",
            "命が何個あっても足りないなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        "でもまぁ……カワイイからいいかなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_6B24")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_6938 end

    def Function_26_6B2C(): pass

    label("Function_26_6B2C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x1C)
    ClearChrFlags(0x1C, 0x10)
    TurnDirection(0x1C, 0x0, 0)
    OP_52(0x1C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6BC0")
    Jump("loc_6C0A")

    label("loc_6BC0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6BE0")
    OP_52(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C0A")

    label("loc_6BE0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C00")
    OP_52(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C0A")

    label("loc_6C00")

    OP_52(0x1C, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1C, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C0A")

    OP_52(0x1C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1C, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6C3D")
    Jump("loc_6E02")

    label("loc_6C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6CE0")

    #C0344
    ChrTalk(
        0x1C,
        (
            "隠してたグラビア雑誌が見つかってから\x01",
            "なんか看護師さん達の目が\x01",
            "冷たい気がする……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x1C,
        (
            "あんな雑誌押し付けてきた\x01",
            "向かいのおっさんが悪いんだ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E02")

    label("loc_6CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6D6C")

    #C0346
    ChrTalk(
        0x1C,
        (
            "昨日、向こうのおっさんに\x01",
            "もらったグラビア雑誌……\x01",
            "検温の時に見つかっちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x1C,
        "あの恥ずかしさったらなかったぜ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E02")

    label("loc_6D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6DAD")

    #C0348
    ChrTalk(
        0x1C,
        (
            "（……この人、マジで\x01",
            "  偉い先生なのか……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E02")

    label("loc_6DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6E02")

    #C0349
    ChrTalk(
        0x1C,
        (
            "あーあ……\x01",
            "こんな怪我なんてしてなきゃ\x01",
            "今頃はお祭り気分だったのになぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E02")

    SetChrSubChip(0x1C, 0x0)
    TalkEnd(0x1C)
    Return()

    # Function_26_6B2C end

    def Function_27_6E0A(): pass

    label("Function_27_6E0A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E9E")
    Jump("loc_6EE8")

    label("loc_6E9E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6EBE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EE8")

    label("loc_6EBE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EDE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EE8")

    label("loc_6EDE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6EE8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6F1B")
    Jump("loc_7193")

    label("loc_6F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6FD4")

    #C0350
    ChrTalk(
        0xFE,
        (
            "こないだグラビア雑誌をあげてから\x01",
            "向かいの子がよくこっちを睨んで来るんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        (
            "うーん、まだ欲しいのかな？\x01",
            "仕方ない、友好の証にもう一冊\x01",
            "とっておきをプレゼントするか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7193")

    label("loc_6FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7063")

    #C0352
    ChrTalk(
        0xFE,
        (
            "向かいのベッドの子に\x01",
            "昨日グラビア雑誌をあげたのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "検温の時の彼の\x01",
            "慌てた様子を見るに、\x01",
            "元気になってくれたみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7193")

    label("loc_7063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7115")

    #C0354
    ChrTalk(
        0xFE,
        (
            "おじさんは、挨拶代わりに\x01",
            "コレクションしている\x01",
            "グラビア雑誌をプレゼントするんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "ヨアヒム先生も\x01",
            "結構快く受け取ってくれてね。\x01",
            "いや、親しみやすいお方だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7193")

    label("loc_7115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7193")

    #C0356
    ChrTalk(
        0xFE,
        (
            "向かいのベッドの子、\x01",
            "何だか元気がないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "仕方ない、おじさん秘蔵の\x01",
            "グラビア雑誌を\x01",
            "こっそりあげるとするか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7193")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_6E0A end

    def Function_28_719B(): pass

    label("Function_28_719B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_722F")
    Jump("loc_7279")

    label("loc_722F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_724F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7279")

    label("loc_724F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_726F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7279")

    label("loc_726F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7279")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_72AC")
    Jump("loc_7471")

    label("loc_72AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_732D")

    #C0358
    ChrTalk(
        0xFE,
        (
            "今日回診に来る先生のこと\x01",
            "調べたんだけど……\x01",
            "ゲイリー教授ってダレ？\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "ヨアヒム先生に\x01",
            "診てもらいたいのにぃ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7471")

    label("loc_732D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_737E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7348")
    Call(1, 47)
    Jump("loc_7379")

    label("loc_7348")


    #C0360
    ChrTalk(
        0xFE,
        (
            "ヨアヒム先生ったら\x01",
            "照れ屋なんだから、もう㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7379")

    Jump("loc_7471")

    label("loc_737E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_73F6")

    #C0361
    ChrTalk(
        0xFE,
        "ヨアヒム先生って独身らしいわねー。\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "ふふふ、このあたしが\x01",
            "先生の心の隙間を\x01",
            "埋めてあげようかしら㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7471")

    label("loc_73F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7471")

    #C0363
    ChrTalk(
        0xFE,
        (
            "あぁん、ヨアヒム先生は\x01",
            "まだ回診に来てくれないのかしら㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "あの飄々とした感じ……\x01",
            "おばさんのタイプだわ～㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7471")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_28_719B end

    def Function_29_7479(): pass

    label("Function_29_7479")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_750D")
    Jump("loc_7557")

    label("loc_750D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_752D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7557")

    label("loc_752D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_754D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7557")

    label("loc_754D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7557")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_758A")
    Jump("loc_773B")

    label("loc_758A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_75F3")

    #C0365
    ChrTalk(
        0xFE,
        (
            "今日は外科のセンセが\x01",
            "回診に来てくれる予定なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        "私の足腰、良くなってるといいわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_773B")

    label("loc_75F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7642")

    #C0367
    ChrTalk(
        0xFE,
        (
            "あらあら、かわいい先生だこと。\x01",
            "さぞ人気が高いのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_773B")

    label("loc_7642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_76CC")

    #C0368
    ChrTalk(
        0xFE,
        (
            "看護師さん達が\x01",
            "本当によくしてくれるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "ふふ、何人か変わった子もいるけど……\x01",
            "みんな思いやりが合って良い子たちね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_773B")

    label("loc_76CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_773B")

    #C0370
    ChrTalk(
        0xFE,
        (
            "この病院はほんと、\x01",
            "快適でいいところねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "足腰がよくなるまで\x01",
            "ゆっくりさせてもらいましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_773B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_7479 end

    def Function_30_7743(): pass

    label("Function_30_7743")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_77D7")
    Jump("loc_7821")

    label("loc_77D7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_77F7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7821")

    label("loc_77F7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7817")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7821")

    label("loc_7817")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7821")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7854")
    Jump("loc_79BE")

    label("loc_7854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_794B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78FA")

    #C0372
    ChrTalk(
        0xFE,
        (
            "さっき検温されてる時に、\x01",
            "看護師さんにグラビア雑誌が\x01",
            "見つかっちゃってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "微笑ましく笑われちゃったけど、\x01",
            "それはそれでツラいぜ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7946")

    label("loc_78FA")


    #C0374
    ChrTalk(
        0xFE,
        (
            "はぁ、やっぱ隣のおっさんから\x01",
            "グラビア雑誌なんて\x01",
            "貰うんじゃなかった……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7946")

    Jump("loc_79BE")

    label("loc_794B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_79BE")

    #C0375
    ChrTalk(
        0xFE,
        (
            "えへへ……\x01",
            "この病院、看護師さん、美人だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "やっぱりグラビアの中の美人より\x01",
            "実在する美人だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79BE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_7743 end

    def Function_31_79C6(): pass

    label("Function_31_79C6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A5A")
    Jump("loc_7AA4")

    label("loc_7A5A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A7A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AA4")

    label("loc_7A7A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A9A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AA4")

    label("loc_7A9A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AA4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7AD7")
    Jump("loc_7C31")

    label("loc_7AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_7B9B")

    #C0377
    ChrTalk(
        0xFE,
        "実は僕、そろそろ退院なんだ。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "気の合う病室の仲間と別れるのは寂しいけど……\x01",
            "こればっかりは仕方ないよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "よし……餞別に、隣の子に\x01",
            "秘蔵のグラビアをプレゼントしようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C31")

    label("loc_7B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7C31")

    #C0380
    ChrTalk(
        0xFE,
        (
            "隣のベッドの子に\x01",
            "友好の証にグラビア雑誌を\x01",
            "何冊かあげたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "回診の時に見つかりそうになったけど……\x01",
            "あはは、スリリングだったねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C31")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_79C6 end

    def Function_32_7C39(): pass

    label("Function_32_7C39")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7CCD")
    Jump("loc_7D17")

    label("loc_7CCD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D17")

    label("loc_7CED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D0D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D17")

    label("loc_7D0D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7D17")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7D4A")
    Jump("loc_7E45")

    label("loc_7D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_7DAE")

    #C0382
    ChrTalk(
        0xFE,
        "さっき、廊下を子供が走っておったのう。\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        "まったく、親はなにを教育しとるんだ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E45")

    label("loc_7DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7E45")

    #C0384
    ChrTalk(
        0xFE,
        (
            "先週、ラゴー教授に診てもらったんじゃ。\x01",
            "どうやら今週中には退院できるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "食あたりはやはり怖いのう。\x01",
            "おまえさんも気をつけなされ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E45")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_7C39 end

    def Function_33_7E4D(): pass

    label("Function_33_7E4D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7EE1")
    Jump("loc_7F2B")

    label("loc_7EE1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7F01")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F2B")

    label("loc_7F01")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F21")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F2B")

    label("loc_7F21")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F2B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7F5E")
    Jump("loc_806C")

    label("loc_7F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_7FE2")

    #C0386
    ChrTalk(
        0xFE,
        "えっ……ヨアヒム先生と会ってきたの？\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "ムキーッ！\x01",
            "こんな子たちに会うくらいなら\x01",
            "回診に来てくれればいいのにっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_806C")

    label("loc_7FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_806C")

    #C0388
    ChrTalk(
        0xFE,
        (
            "最近ヨアヒム先生が\x01",
            "回診に来てくれないと思ったら……\x01",
            "いつの間にか担当が替わってたの！\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "ムキーッ！\x01",
            "ヨアヒム先生のいけず！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_806C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_7E4D end

    def Function_34_8074(): pass

    label("Function_34_8074")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8108")
    Jump("loc_8152")

    label("loc_8108")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8128")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8152")

    label("loc_8128")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8148")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8152")

    label("loc_8148")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8152")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8185")
    Jump("loc_82B8")

    label("loc_8185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_81DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81A0")
    Call(1, 36)
    Jump("loc_81D7")

    label("loc_81A0")


    #C0390
    ChrTalk(
        0xFE,
        (
            "ま、まぁとにかく。\x01",
            "見舞いに来てくれてうれしいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81D7")

    Jump("loc_82B8")

    label("loc_81DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_82B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8289")

    #C0391
    ChrTalk(
        0xFE,
        (
            "昨日、ダチが見舞いに来るって\x01",
            "連絡があったんだけど\x01",
            "結局来なかったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "……心配だな。\x01",
            "あいつ、ありえないほど\x01",
            "方向音痴なんだよな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_82B8")

    label("loc_8289")


    #C0393
    ChrTalk(
        0xFE,
        (
            "あいつ、ちゃんと病室に\x01",
            "来れるのかな……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82B8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_8074 end

    def Function_35_82C0(): pass

    label("Function_35_82C0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8354")
    Jump("loc_839E")

    label("loc_8354")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8374")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_839E")

    label("loc_8374")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8394")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_839E")

    label("loc_8394")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_839E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83D5")
    Call(1, 36)
    Jump("loc_8414")

    label("loc_83D5")


    #C0394
    ChrTalk(
        0xFE,
        (
            "いやぁ、まいったまいった。\x01",
            "病室の場所が分からなくてねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8414")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_82C0 end

    def Function_36_841C(): pass

    label("Function_36_841C")

    TurnDirection(0x2D, 0x24, 0)
    SetChrSubChip(0x24, 0x1)
    OP_4B(0x2D, 0xFF)

    #C0395
    ChrTalk(
        0x2D,
        (
            "よっ。\x01",
            "入院生活満喫してるかぁ？\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x24,
        "はは、よく来たな。\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x24,
        (
            "ところでお前、\x01",
            "導力通信じゃ昨日来る予定だって\x01",
            "言ってなかったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x2D,
        (
            "一応来てたんだけど、\x01",
            "なかなか病室にたどり着けなくてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x2D,
        (
            "しかたないから宿泊施設で\x01",
            "宿をとってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x24,
        "相変わらずの方向音痴だな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetChrSubChip(0x24, 0x0)
    OP_4C(0x2D, 0xFF)
    Return()

    # Function_36_841C end

    def Function_37_854A(): pass

    label("Function_37_854A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_85DE")
    Jump("loc_8628")

    label("loc_85DE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_85FE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8628")

    label("loc_85FE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_861E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8628")

    label("loc_861E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8628")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_86D1")

    #C0401
    ChrTalk(
        0xFE,
        (
            "昨日入院してきたもんが\x01",
            "今朝、いつのまにか退院しておった。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "ありゃあ、相当やましい事を\x01",
            "しとるにちがいないぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87CB")

    label("loc_86D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_86DF")
    Jump("loc_87CB")

    label("loc_86DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_874E")

    #C0403
    ChrTalk(
        0xFE,
        (
            "あの新入り……\x01",
            "なんでも抗争で大怪我したそうじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        "そんな奴と同室で大丈夫かのう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_87CB")

    label("loc_874E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_87CB")

    #C0405
    ChrTalk(
        0xFE,
        (
            "この間、ラゴー教授に\x01",
            "回診に来ていただいたのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "偉い先生に診てもらえるのは\x01",
            "本当にありがたいことだのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87CB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_37_854A end

    def Function_38_87D3(): pass

    label("Function_38_87D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_87E4")
    Jump("loc_8837")

    label("loc_87E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_8820")

    #C0407
    ChrTalk(
        0xFE,
        "にゃむ……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        "ぐう…………ぐう…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_8837")

    label("loc_8820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_882E")
    Jump("loc_8837")

    label("loc_882E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8837")

    label("loc_8837")

    TalkEnd(0xFE)
    Return()

    # Function_38_87D3 end

    def Function_39_883B(): pass

    label("Function_39_883B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_88CF")
    Jump("loc_8919")

    label("loc_88CF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_88EF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8919")

    label("loc_88EF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_890F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8919")

    label("loc_890F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8919")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_89B2")

    #C0409
    ChrTalk(
        0xFE,
        (
            "昨日は彼女が見舞いにきて、\x01",
            "とんだ恥をかいちまったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "まったくよう……\x01",
            "照れるじゃねーか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AF7")

    label("loc_89B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_8A34")

    #C0411
    ChrTalk(
        0xFE,
        (
            "バッ……そんなこと言う為だけに\x01",
            "見舞いなんかに来るんじゃねーよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "迷惑なんてかけてねーよ。\x01",
            "……本当だって！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AF7")

    label("loc_8A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8A9F")

    #C0413
    ChrTalk(
        0xFE,
        "今日は彼女が見舞いに来るんだ。\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        (
            "来なくていいっつったのに……\x01",
            "照れちゃうじゃねーか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AF7")

    label("loc_8A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8AF7")

    #C0415
    ChrTalk(
        0xFE,
        (
            "ケッ、病院ってのは\x01",
            "かったるくてやだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        "さっさと退院させろっつーの。\x02",
    )

    CloseMessageWindow()

    label("loc_8AF7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_39_883B end

    def Function_40_8AFF(): pass

    label("Function_40_8AFF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B93")
    Jump("loc_8BDD")

    label("loc_8B93")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8BB3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8BDD")

    label("loc_8BB3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BD3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8BDD")

    label("loc_8BD3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8BDD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8C10")
    Jump("loc_8C93")

    label("loc_8C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_8C7C")
    TurnDirection(0xFE, 0x27, 0)

    #C0417
    ChrTalk(
        0xFE,
        (
            "ふふ、安心した。\x01",
            "結構元気そうなんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        "皆さんに迷惑かけてないでしょうね？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C93")

    label("loc_8C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8C8A")
    Jump("loc_8C93")

    label("loc_8C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8C93")

    label("loc_8C93")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_40_8AFF end

    def Function_41_8C9B(): pass

    label("Function_41_8C9B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D2F")
    Jump("loc_8D79")

    label("loc_8D2F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D4F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D79")

    label("loc_8D4F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D6F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D79")

    label("loc_8D6F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D79")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8E27")

    #C0419
    ChrTalk(
        0xFE,
        (
            "同室のおじいさんなら\x01",
            "看護師さんと散歩に出かけてるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "うん、いいわね。\x01",
            "私も看護師さんに\x01",
            "お願いしてみようかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F3F")

    label("loc_8E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_8E6E")

    #C0421
    ChrTalk(
        0xFE,
        (
            "うふふ、部屋の皆さんは\x01",
            "個性的でなかなか楽しいわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F3F")

    label("loc_8E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8EB8")

    #C0422
    ChrTalk(
        0xFE,
        "おやおや、大所帯で病室に……\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        "誰かのお見舞いかい？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F3F")

    label("loc_8EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8F3F")

    #C0424
    ChrTalk(
        0xFE,
        (
            "お家に一人で住んでいたから、\x01",
            "こういう共同生活みたいなのは楽しいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "みんな良い人そうだし、\x01",
            "仲良くして頂かないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F3F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_41_8C9B end

    def Function_42_8F47(): pass

    label("Function_42_8F47")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FDB")
    Jump("loc_9025")

    label("loc_8FDB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8FFB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9025")

    label("loc_8FFB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_901B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9025")

    label("loc_901B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9025")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_90E3")

    #C0426
    ChrTalk(
        0xFE,
        (
            "明日当たりに息子とお義母さまが\x01",
            "お見舞いに来てくれるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        (
            "お義母さまには今回、\x01",
            "色々よくしてもらったし\x01",
            "きちんとお礼を言わないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9255")

    label("loc_90E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_9142")

    #C0428
    ChrTalk(
        0xFE,
        (
            "なんでも、この病院は\x01",
            "食事もレベル高いそうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        "うふふ、楽しみね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9255")

    label("loc_9142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_91D6")

    #C0430
    ChrTalk(
        0xFE,
        (
            "今度、息子を連れてお見舞いに来るって\x01",
            "お義母さまから連絡があったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        (
            "わわー、どうしよう。\x01",
            "なんかすっごく申し訳ないかも……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9255")

    label("loc_91D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9255")

    #C0432
    ChrTalk(
        0xFE,
        (
            "息子をお義母さまに預けて\x01",
            "入院してきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "普段は嫁・姑であまり仲良くないけど、\x01",
            "意外と協力しあえるものねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9255")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_42_8F47 end

    def Function_43_925D(): pass

    label("Function_43_925D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_92F1")
    Jump("loc_933B")

    label("loc_92F1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9311")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_933B")

    label("loc_9311")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9331")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_933B")

    label("loc_9331")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_933B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_936E")
    Jump("loc_9416")

    label("loc_936E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_937C")
    Jump("loc_9416")

    label("loc_937C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_938A")
    Jump("loc_9416")

    label("loc_938A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9416")

    #C0434
    ChrTalk(
        0xFE,
        (
            "妙におなか痛いと思って来たら\x01",
            "チュウスイエン……？　だとかで\x01",
            "いきなり入院させられたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "あーもう！\x01",
            "早く家に帰りたーい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9416")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_43_925D end

    def Function_44_941E(): pass

    label("Function_44_941E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_94A5")

    #C0436
    ChrTalk(
        0xFE,
        (
            "うー、まだなんかお腹が\x01",
            "ズキズキする気がする……\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "手術って、終わってもしばらくは\x01",
            "休んでないといけないのね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9575")

    label("loc_94A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_94EE")

    #C0438
    ChrTalk(
        0xFE,
        (
            "……朝、手術したから寝てるの。\x01",
            "起こさないでくんない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9575")

    label("loc_94EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_956C")

    #C0439
    ChrTalk(
        0xFE,
        (
            "うー……朝のうちに\x01",
            "虫垂炎の手術があったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "痛い……何にもしたくない……\x01",
            "寝たい……おなかすいた……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9575")

    label("loc_956C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9575")

    label("loc_9575")

    TalkEnd(0xFE)
    Return()

    # Function_44_941E end

    def Function_45_9579(): pass

    label("Function_45_9579")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_960D")
    Jump("loc_9657")

    label("loc_960D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_962D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9657")

    label("loc_962D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_964D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9657")

    label("loc_964D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9657")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_968A")
    Jump("loc_98A8")

    label("loc_968A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_9739")
    SetChrSubChip(0xFE, 0x0)

    #C0441
    ChrTalk(
        0xFE,
        (
            "（……あまり長居して\x01",
            "  周囲に不安を与えるのは\x01",
            "  公社にとって不利益ですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "（明日、仲間が目覚めたら\x01",
            "  すぐにでも退院させてもらうとしましょう。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98A8")

    label("loc_9739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_989F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_980B")

    #C0443
    ChrTalk(
        0xFE,
        "やれやれ、警察にも困ったものです。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "根掘り葉掘り聞かれても\x01",
            "答えられることなんて\x01",
            "何もないのですがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xFE,
        (
            "これでも入院している身なのだから、\x01",
            "少しは気を遣って欲しいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_989A")

    label("loc_980B")


    #C0446
    ChrTalk(
        0xFE,
        (
            "一緒に運ばれた同僚たちは\x01",
            "まだＩＣＵにいるようですが……\x01",
            "明日には目覚めるとのことです。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        (
            "ふふ、さすがは噂に名高い\x01",
            "ウルスラ病院ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_989A")

    Jump("loc_98A8")

    label("loc_989F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_98A8")

    label("loc_98A8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_45_9579 end

    def Function_46_98B0(): pass

    label("Function_46_98B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_98C1")
    Jump("loc_9C9D")

    label("loc_98C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_98CF")
    Jump("loc_9C9D")

    label("loc_98CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_98DD")
    Jump("loc_9C9D")

    label("loc_98DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_98EB")
    Jump("loc_9C9D")

    label("loc_98EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_98F9")
    Jump("loc_9C9D")

    label("loc_98F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_9907")
    Jump("loc_9C9D")

    label("loc_9907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9915")
    Jump("loc_9C9D")

    label("loc_9915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_998F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9930")
    Call(1, 47)
    Jump("loc_998A")

    label("loc_9930")


    #C0448
    ChrTalk(
        0x30,
        (
            "#2406Fふぅ……たまにモテるとこれだよ。\x01",
            "早く回診を終わらせて\x01",
            "帰りたいんだけどねぇ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_998A")

    Jump("loc_9C9D")

    label("loc_998F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9BA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AD2")

    #C0449
    ChrTalk(
        0x30,
        (
            "#2400F記念祭は満喫してるかな？\x02\x03",

            "#2409F僕も昨日、新しい釣り場を見つけてね。\x01",
            "この後行くところなのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x101,
        "#0005Fあの……仕事は？\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x30,
        (
            "#2409Fはっはっは……\x01",
            "他の先生方には内緒で頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x1, 5)
    Jump("loc_9B9B")

    label("loc_9AD2")


    #C0452
    ChrTalk(
        0x30,
        (
            "#2405Fあ、一応言っておくが\x01",
            "今日やっておくべきことはキチンと\x01",
            "済ませたんだからね？\x02\x03",

            "#2400F自分で作った休憩時間だ、\x01",
            "文句を言われる筋合いはないだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        "#0006F（だったら堂々と行けばいいのに……）\x02",
    )

    CloseMessageWindow()

    label("loc_9B9B")

    Jump("loc_9C9D")

    label("loc_9BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9BAE")
    Jump("loc_9C9D")

    label("loc_9BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9BBC")
    Jump("loc_9C9D")

    label("loc_9BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9BCA")
    Jump("loc_9C9D")

    label("loc_9BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_9BD8")
    Jump("loc_9C9D")

    label("loc_9BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_9BE6")
    Jump("loc_9C9D")

    label("loc_9BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_9C94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C01")
    Call(1, 18)
    Jump("loc_9C8F")

    label("loc_9C01")


    #C0454
    ChrTalk(
        0x30,
        (
            "#2403F病は気から、なんて言うらしいしね。\x01",
            "これだけ元気があれば退院もすぐだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x136,
        (
            "#1306F……もう少し医者らしいことを\x01",
            "言ってください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C8F")

    Jump("loc_9C9D")

    label("loc_9C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9C9D")

    label("loc_9C9D")

    TalkEnd(0xFE)
    Return()

    # Function_46_98B0 end

    def Function_47_9CA1(): pass

    label("Function_47_9CA1")

    TurnDirection(0x30, 0x1E, 0)
    SetChrSubChip(0x1E, 0x2)
    OP_4B(0x30, 0xFF)

    #C0456
    ChrTalk(
        0x1E,
        (
            "ヨアヒム先生は\x01",
            "彼女とかいないのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x30,
        (
            "#2409Fはっはっは、これでも僕は\x01",
            "独身貴族を気取っていましてね。\x01",
            "なかなか女性が寄り付かないんですよ。\x02\x03",

            "#2400Fまぁそんなことはともかく\x01",
            "診察をですね──\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x1E,
        (
            "あっらぁ、そうなんですか？\x01",
            "もったいないわぁ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x1E,
        (
            "うふ、そ・れ・な・ら……\x01",
            "私が立候補しちゃおうかしら㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x30,
        (
            "#2406Fえ、え～と……\x01",
            "ははは、参ったねぇ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    SetChrSubChip(0x1E, 0x0)
    OP_4C(0x30, 0xFF)
    Return()

    # Function_47_9CA1 end

    def Function_48_9E23(): pass

    label("Function_48_9E23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EBA")

    #C0461
    ChrTalk(
        0xFE,
        (
            "後学のために、病院の医師たちの\x01",
            "働きぶりを見学させてもらってるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        (
            "てきぱきと働く姿を見ると\x01",
            "彼らの優秀さが伺えるね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_9F3A")

    label("loc_9EBA")


    #C0463
    ChrTalk(
        0xFE,
        (
            "後学のために、病院の医師たちの\x01",
            "働きぶりを見学させてもらってるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xFE,
        (
            "……さすがに、\x01",
            "ここに居座るのは邪魔だろうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F3A")

    TalkEnd(0xFE)
    Return()

    # Function_48_9E23 end

    def Function_49_9F3E(): pass

    label("Function_49_9F3E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(110090, 1000, -5610, 0)
    MoveCamera(68, 34, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20480, 0)
    SetChrPos(0x101, 110500, 0, -6000, 0)
    SetChrPos(0x102, 109200, 0, -6000, 45)
    SetChrPos(0x103, 110500, 0, -7300, 0)
    SetChrPos(0x104, 109200, 0, -7300, 45)
    SetChrPos(0x109, 109200, 0, -4700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    TurnDirection(0xC, 0x101, 0)
    SetChrSubChip(0xC, 0x0)
    FadeToBright(500, 0)
    OP_0D()

    #C0465
    ChrTalk(
        0xC,
        (
            "#5Pうーん……やっぱりアレ、\x01",
            "お店に買い取ってもらおうかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあの……\x01",
            "何かお困りですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xC,
        (
            "#5Pん？　いや、\x01",
            "困ってるってわけじゃ\x01",
            "無いんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xC,
        (
            "#5Pこの間、記念祭でクロスベル市に\x01",
            "行った時に、ちょっとした\x01",
            "リボンを買ったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xC,
        (
            "#5P買ったときはカワイイなんて\x01",
            "思ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xC,
        (
            "#5Pよくよく考えたら\x01",
            "可愛すぎて、ちょっと\x01",
            "私にはあわないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x101,
        (
            "#12P#0003F（リボンか……）\x02\x03",

            "（プレゼントの包装用に\x01",
            "  あるといいかもしれないな。）\x02\x03",

            "#0000Fあの、相談なんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xC,
        "#5Pへ、なに？\x02",
    )

    CloseMessageWindow()

    #A0473
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは、プレゼントの材料集めを\x01",
            "していることを説明した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0474
    ChrTalk(
        0x101,
        (
            "#12P#0000Fと、いうわけで……\x01",
            "そのリボン、よかったら\x01",
            "譲っていただけませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0xC,
        "#5Pへぇ、シズクちゃんが……\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x104,
        (
            "#12P#0304F別にいかがわしい目的で\x01",
            "使うんじゃないし、心配はいらないぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x109,
        "#6P#0506Fラ、ランディ先輩……\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x103,
        (
            "#12P#0200F……そういうことを言ったら\x01",
            "逆に疑われそうですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xC,
        "#5Pあは……まぁ、いいわ。\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xC,
        (
            "#5Pそういうことなら是非とも\x01",
            "有効活用してよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0481
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x344),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x344, 1)

    #C0482
    ChrTalk(
        0x102,
        (
            "#12P#0100Fすみません、\x01",
            "無理を言ってしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xC,
        (
            "#5Pいえいえ、いいのよ。\x01",
            "このリボンも捨てずにすむし。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xC,
        "#5P材料集め、頑張って頂戴ね。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x101,
        "#12P#0000Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_29(0x2C, 0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A581")
    OP_29(0x2C, 0x1, 0x5)

    #C0486
    ChrTalk(
        0x101,
        (
            "#12P#0000F（プレゼントの材料になりそうな物も揃ったし\x01",
            "  包装用の箱とリボンも手に入ったな……）\x02\x03",

            "（よし、そろそろシズクちゃんの所に\x01",
            "  持っていってあげよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A581")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(110500, 1000, -6000, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_93(0xC, 0x5A, 0x0)
    SetChrPos(0x0, 110500, 0, -6000, 0)
    SetChrPos(0x1, 110500, 0, -6000, 0)
    SetChrPos(0x2, 110500, 0, -6000, 0)
    SetChrPos(0x3, 110500, 0, -6000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_49_9F3E end

    SaveToFile()

Try(main)
