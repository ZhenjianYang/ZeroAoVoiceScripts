from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1310.bin",                # FileName
        "c1310",                    # MapName
        "c1310",                    # Location
        0x001C,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 300, 5000, 0, 0, 1, 28, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1310",                  # 0
        "警備員ウォング",         # 1
        "警備員ポール",           # 2
        "受付嬢ランフィ",         # 3
        "受付嬢コリンナ",         # 4
        "貿易商リゼロ",           # 5
        "研究員",                 # 6
        "ロバーツ主任",           # 7
        "市民",                   # 8
        "市民",                   # 9
        "遊撃士スコット",         # 10
        "遊撃士ヴェンツェル",     # 11
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch27900.itc",                   # 01
        "chr/ch30500.itc",                   # 02
        "chr/ch27702.itc",                   # 03
        "chr/ch32800.itc",                   # 04
        "chr/ch29300.itc",                   # 05
        "chr/ch20900.itc",                   # 06
        "chr/ch20902.itc",                   # 07
        "chr/ch27200.itc",                   # 08
        "chr/ch27300.itc",                   # 09
    ))

    DeclNpc(8500,    0,       13310,   270,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-5730,   300,     29909,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       300,     31700,   180,  257,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(7110,    300,     32759,   90,   257,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-4840,   0,       18180,   90,   341,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(5000,    0,       17850,   90,   257,  0x0, 0,   4,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(6500,    0,       17850,   270,  257,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(6570,    300,     29760,   0,    257,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(8210,    300,     28309,   270,  469,  0x0, 0,   7,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(1820,    300,     25760,   315,  389,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(3220,    300,     25959,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)

    DeclEvent(0x0000, 0, 25,  9.5,                   16.0,                  -0.5,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -4.75,                 -5.333333492279053,    0.10000000894069672,   1.0])

    DeclActor(0,       300,     30300,   1500,    0,       1800,    31700,   0x007E, 0,  6,  0x0000)
    DeclActor(6650,    300,     31080,   1500,    7110,    1800,    32759,   0x007E, 0,  9,  0x0000)

    ScpFunction((
        "Function_0_300",          # 00, 0
        "Function_1_3B8",          # 01, 1
        "Function_2_5E3",          # 02, 2
        "Function_3_5EA",          # 03, 3
        "Function_4_684",          # 04, 4
        "Function_5_1516",         # 05, 5
        "Function_6_24AB",         # 06, 6
        "Function_7_24AF",         # 07, 7
        "Function_8_2BBD",         # 08, 8
        "Function_9_4753",         # 09, 9
        "Function_10_4757",        # 0A, 10
        "Function_11_5978",        # 0B, 11
        "Function_12_6973",        # 0C, 12
        "Function_13_713F",        # 0D, 13
        "Function_14_743A",        # 0E, 14
        "Function_15_7512",        # 0F, 15
        "Function_16_7C29",        # 10, 16
        "Function_17_7CAA",        # 11, 17
        "Function_18_7DD1",        # 12, 18
        "Function_19_7F1A",        # 13, 19
        "Function_20_812E",        # 14, 20
        "Function_21_8F4B",        # 15, 21
        "Function_22_9D5D",        # 16, 22
        "Function_23_A4EF",        # 17, 23
        "Function_24_A765",        # 18, 24
        "Function_25_AB42",        # 19, 25
    ))


    def Function_0_300(): pass

    label("Function_0_300")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_340"),
        (1, "loc_34C"),
        (2, "loc_358"),
        (3, "loc_364"),
        (4, "loc_370"),
        (5, "loc_37C"),
        (6, "loc_388"),
        (SWITCH_DEFAULT, "loc_394"),
    )


    label("loc_340")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_34C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_358")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_364")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_370")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_37C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_388")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_394")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_3A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A0")

    label("loc_3B7")

    Return()

    # Function_0_300 end

    def Function_1_3B8(): pass

    label("Function_1_3B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D0")
    ClearScenarioFlags(0x5F, 1)
    Event(0, 2)

    label("loc_3D0")

    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_41E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_414")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1080, 300, 29510, 0)
    SetChrFlags(0xE, 0x10)

    label("loc_414")

    SetChrFlags(0xC, 0x80)
    Jump("loc_5C1")

    label("loc_41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_42C")
    Jump("loc_5C1")

    label("loc_42C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_43A")
    Jump("loc_5C1")

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_448")
    Jump("loc_5C1")

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_45B")
    SetChrFlags(0xC, 0x10)
    Jump("loc_5C1")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_46E")
    SetChrFlags(0xC, 0x10)
    Jump("loc_5C1")

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_486")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_5C1")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_494")
    Jump("loc_5C1")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4B8")
    SetChrPos(0xB, 7110, 300, 32759, 90)
    SetChrFlags(0xB, 0x10)
    Jump("loc_5C1")

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4C6")
    Jump("loc_5C1")

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrPos(0xB, 7110, 300, 32759, 90)
    SetChrFlags(0xB, 0x10)
    Jump("loc_5C1")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4F8")
    Jump("loc_5C1")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_53E")
    SetChrPos(0xB, 7110, 300, 32759, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 4)), scpexpr(EXPR_END)), "loc_539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)

    label("loc_539")

    Jump("loc_5C1")

    label("loc_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 4)), scpexpr(EXPR_END)), "loc_564")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)

    label("loc_564")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xB, 7110, 300, 32759, 90)
    SetChrFlags(0xB, 0x10)
    Jump("loc_5C1")

    label("loc_584")

    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 4)), scpexpr(EXPR_END)), "loc_5A1")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)

    label("loc_5A1")

    SetChrPos(0xB, 7110, 300, 32759, 90)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_5C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E2")
    Event(0, 23)

    label("loc_5E2")

    Return()

    # Function_1_3B8 end

    def Function_2_5E3(): pass

    label("Function_2_5E3")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_5E3 end

    def Function_3_5EA(): pass

    label("Function_3_5EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_603")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_609")

    label("loc_603")

    OP_10(0x0, 0x1)
    OP_10(0x2, 0x0)

    label("loc_609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_620")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63C")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_653")

    label("loc_63C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_653")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_653")

    label("loc_653")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_683")
    OP_1B(0x0, 0x0, 0xD)

    label("loc_683")

    Return()

    # Function_3_5EA end

    def Function_4_684(): pass

    label("Function_4_684")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6D6")

    #C0001
    ChrTalk(
        0xFE,
        (
            "む……今日は\x01",
            "客が少ない気がするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "気のせいだろうか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1512")

    label("loc_6D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_755")

    #C0003
    ChrTalk(
        0xFE,
        (
            "客に不安を与えないのも\x01",
            "警備員の仕事だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "発砲事件があったといっても、\x01",
            "ＩＢＣは極めて安全だぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C3")

    label("loc_755")


    #C0005
    ChrTalk(
        0xFE,
        (
            "本日は警備員を\x01",
            "２割ほど増やしている。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "……港湾公園の方で\x01",
            "事件があったと言うからな。\x01",
            "念のためだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_7C3")

    Jump("loc_1512")

    label("loc_7C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_93E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_87B")

    #C0007
    ChrTalk(
        0xFE,
        (
            "ウチの保安部は\x01",
            "世界中の主要都市に対して\x01",
            "治安レベルの格付けを行っているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "これも各地を飛び回る\x01",
            "クロイス総裁を守るためには\x01",
            "必要なことだからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_939")

    label("loc_87B")


    #C0009
    ChrTalk(
        0xFE,
        (
            "この２、３週間ほどで\x01",
            "市内の治安レベルが悪化している。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "我が保安部の格付けによると\x01",
            "Ｃ－にまで落ち込んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "人気のない裏路地などは危険だ。\x01",
            "市民も注意してくれるといいんだが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_939")

    Jump("loc_1512")

    label("loc_93E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_994")

    #C0012
    ChrTalk(
        0xFE,
        (
            "警備員たるもの油断は許されん。\x01",
            "気を引き締めておかんとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A03")

    label("loc_994")


    #C0013
    ChrTalk(
        0xFE,
        "本日が祭りの最終日だな。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "こういう時こそ\x01",
            "トラブルが起こりやすいものだ。\x01",
            "気を引き締めておかんとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_A03")

    Jump("loc_1512")

    label("loc_A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_A63")

    #C0015
    ChrTalk(
        0xFE,
        (
            "重役の方たちは\x01",
            "今日は一日中会議だそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "ふむ、同情してしまうな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1512")

    label("loc_A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_BBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AFC")

    #C0017
    ChrTalk(
        0xFE,
        (
            "祭りの影に忘れ去られそうだが、\x01",
            "クロスベルの治安は良いとは言えんのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "観光客が迷い込んで\x01",
            "事件にあわなきゃいいんだがな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBA")

    label("loc_AFC")


    #C0019
    ChrTalk(
        0xFE,
        (
            "ウチの保安部の報告によると\x01",
            "クロスベル市内の治安レベルが\x01",
            "また悪化しているそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "ふむ……警察は何をしておるのか。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "あまり悪化するようなら\x01",
            "我らも体制を強化する必要があるぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_BBA")

    Jump("loc_1512")

    label("loc_BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C24")

    #C0022
    ChrTalk(
        0xFE,
        (
            "どちらにせよ\x01",
            "セキュリティカードが無くては\x01",
            "エレベーターは動かんのだがな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA6")

    label("loc_C24")


    #C0023
    ChrTalk(
        0xFE,
        (
            "先ほど、慣れない客が\x01",
            "エレベーターに乗ろうとしたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "やれやれ、観光客め。\x01",
            "この先は立ち入り禁止だと\x01",
            "言っておるのに。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_CA6")

    Jump("loc_1512")

    label("loc_CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D13")

    #C0025
    ChrTalk(
        0xFE,
        (
            "港湾公園の方は\x01",
            "大した混雑だそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "普段より客も多い……\x01",
            "警備にも気を遣うぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1512")

    label("loc_D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_D99")

    #C0027
    ChrTalk(
        0xFE,
        (
            "このビルの\x01",
            "セキュリティシステムは\x01",
            "外部から独立している。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "ハッキングだか\x01",
            "何だかを食らっても\x01",
            "問題ないはずだぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1512")

    label("loc_D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_E70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_END)), "loc_DFD")

    #C0029
    ChrTalk(
        0xFE,
        "上の階に用事か？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "このエレベーターに乗って\x01",
            "認証カードを使うといい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6B")

    label("loc_DFD")


    #C0031
    ChrTalk(
        0xFE,
        (
            "む……この上の階は\x01",
            "関係者以外立ち入りはできないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "用事があるなら\x01",
            "総合受付で許可を貰ってからだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6B")

    Jump("loc_1512")

    label("loc_E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6F")

    #C0033
    ChrTalk(
        0xFE,
        (
            "フム、クロスベル周辺の\x01",
            "治安レベルが悪化しているようだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "現在の所、大きな問題に\x01",
            "直結しているわけではなさそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "この自治州には傭兵を取り締まる\x01",
            "法律があるわけではないのだ。\x01",
            "……どんな事でも起こりうるぞ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FF2")

    label("loc_F6F")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    #C0036
    ChrTalk(
        0xFE,
        (
            "クロスベルという土地は\x01",
            "非常に難しいのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "決して安全とは言い切れん……\x01",
            "我らも気を引き締めねばな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF2")

    Jump("loc_1512")

    label("loc_FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_112D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1069")

    #C0038
    ChrTalk(
        0xFE,
        (
            "会社が大きくなれば\x01",
            "それだけ守るものも増える。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        "どこの企業も苦労しているようだな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1128")

    label("loc_1069")


    #C0040
    ChrTalk(
        0xFE,
        (
            "最近では、うちの保安部にも\x01",
            "外国企業から引き合いが来ていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "ＶＩＰの警護依頼から\x01",
            "警備のノウハウを教えてくれ、\x01",
            "なんて話もある。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "どこの会社も\x01",
            "保安には苦労しているようだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1128")

    Jump("loc_1512")

    label("loc_112D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_129C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11C3")

    #C0043
    ChrTalk(
        0xFE,
        (
            "……知っているか？\x01",
            "ここの地下１階には\x01",
            "デカイ社員食堂があってな……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "ごほん、いや、何でもない。\x01",
            "まだ勤務時間だからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1297")

    label("loc_11C3")


    #C0045
    ChrTalk(
        0xFE,
        (
            "俺は体力を維持するため\x01",
            "毎朝１００セルジュほど走っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "いざという時のために\x01",
            "体は常に鍛えておかんとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "……だが、朝に走ると\x01",
            "腹の減り具合が早くてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "ごほん、いや、何でもないんだが……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1297")

    Jump("loc_1512")

    label("loc_129C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1426")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1319")

    #C0049
    ChrTalk(
        0xFE,
        (
            "このビルは、大陸で最も\x01",
            "セキュリティの高い場所だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "安心して商談に\x01",
            "励んでもらって構わないぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1421")

    label("loc_1319")


    #C0051
    ChrTalk(
        0xFE,
        (
            "このビルは、大陸で最も\x01",
            "セキュリティの高い場所だと\x01",
            "自負している。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "防犯機能を重視した近代ビル。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "導力技術を駆使した\x01",
            "最新のセキュリティシステム。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "そして我ら保安部の者も\x01",
            "正式な訓練を受けたプロだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "どんな悪党も\x01",
            "ここに侵入する事はできないぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1421")

    Jump("loc_1512")

    label("loc_1426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1478")

    #C0056
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ内の保安なら\x01",
            "俺たちに任せてくれ。\x01",
            "こっちもプロなんでね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1512")

    label("loc_1478")


    #C0057
    ChrTalk(
        0xFE,
        (
            "ほう、そのジャケット……\x01",
            "君達は警察の関係者か？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "俺たちはＩＢＣグループに\x01",
            "勤める保安部の者だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ内の保安なら\x01",
            "俺たちに任せてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1512")

    TalkEnd(0xFE)
    Return()

    # Function_4_684 end

    def Function_5_1516(): pass

    label("Function_5_1516")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1581")

    #C0060
    ChrTalk(
        0xFE,
        (
            "今日はクロイス総裁も\x01",
            "マリアベルさんも出張なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "少し寂しいですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_160C")

    label("loc_1581")


    #C0062
    ChrTalk(
        0xFE,
        (
            "マリアベルさんは\x01",
            "今日は外国に出張なさっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "あの方も年々\x01",
            "出張が増えていますね……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        "ますますお父上に似てきましたよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_160C")

    Jump("loc_24A7")

    label("loc_1611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1689")

    #C0065
    ChrTalk(
        0xFE,
        (
            "今日はお客様も\x01",
            "心なしか少ないようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "ふう……いくら我々でも\x01",
            "ビルの外までは警備できませんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A7")

    label("loc_1689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1803")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1707")

    #C0067
    ChrTalk(
        0xFE,
        (
            "記念祭のあおりでしょうか、\x01",
            "近頃企業進出の話が多いんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        "自分も少し気になってしまいます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_17FE")

    label("loc_1707")


    #C0069
    ChrTalk(
        0xFE,
        (
            "このビルには\x01",
            "ラインフォルト社の営業部が\x01",
            "入っているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "近頃、ライバルである\x01",
            "ヴェルヌ社も支部を設けたいという\x01",
            "打診があるそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "うーん、事あるごとに\x01",
            "対立する２社だと聞いていましたが、\x01",
            "ホント負けず嫌いな話ですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_17FE")

    Jump("loc_24A7")

    label("loc_1803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_190E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_189F")

    #C0072
    ChrTalk(
        0xFE,
        (
            "あまり報道されませんが……\x01",
            "クロスベルは過去に\x01",
            "テロ事件などにも見舞われています。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "記念祭が無事に終わりそうで\x01",
            "何よりですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1909")

    label("loc_189F")


    #C0074
    ChrTalk(
        0xFE,
        "記念祭も今日で終わりですね……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "遊べなかったのは残念ですが、\x01",
            "まあ何事もなくて良かったですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1909")

    Jump("loc_24A7")

    label("loc_190E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1997")

    #C0076
    ChrTalk(
        0xFE,
        (
            "先ほどマリアベルさんが\x01",
            "顔をお見せになったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "僕ら社員の\x01",
            "労をねぎらって下さったんですよ。\x01",
            "嬉しいものですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A7")

    label("loc_1997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1AEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A2A")

    #C0078
    ChrTalk(
        0xFE,
        (
            "ミシュラムのワンダーランドって\x01",
            "聞いた事はありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "《みっしぃ》って名前の猫が\x01",
            "マスコットキャラなんですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE9")

    label("loc_1A2A")


    #C0080
    ChrTalk(
        0xFE,
        (
            "エルム湖の対岸にある\x01",
            "《ミシュラム》には\x01",
            "テーマパークがあるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "ＩＢＣが出資して建設した物で、\x01",
            "家族連れに人気なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "きっと記念祭も\x01",
            "大いに賑わってることでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1AE9")

    Jump("loc_24A7")

    label("loc_1AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1BE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B38")

    #C0083
    ChrTalk(
        0xFE,
        (
            "街の方に較べれば\x01",
            "まだまだ静かなんですけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDF")

    label("loc_1B38")


    #C0084
    ChrTalk(
        0xFE,
        (
            "記念祭は外国からいらっしゃる\x01",
            "お客様も多いようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "昨日も何人か\x01",
            "ご案内したんですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0086
    ChrTalk(
        0xFE,
        (
            "慣れない方ばかりで\x01",
            "大変でしたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1BDF")

    Jump("loc_24A7")

    label("loc_1BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1C55")

    #C0087
    ChrTalk(
        0xFE,
        (
            "ロバーツ主任、何だか\x01",
            "楽しそうでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "お仕事でいい事でも\x01",
            "あったんですかね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE4")

    label("loc_1C55")


    #C0089
    ChrTalk(
        0xFE,
        (
            "先ほど、エプスタイン財団の\x01",
            "ロバーツ主任に挨拶をしましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "何だか嬉しそうに\x01",
            "出かけられました。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "いい事でもあったんですかね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1CE4")

    Jump("loc_24A7")

    label("loc_1CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1E72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1D77")

    #C0092
    ChrTalk(
        0xFE,
        (
            "マリアベルさんは\x01",
            "あの歳にしていくつもの事業で\x01",
            "成功を収めているそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "さすがクロイス総裁の\x01",
            "娘さんですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E6D")

    label("loc_1D77")


    #C0094
    ChrTalk(
        0xFE,
        (
            "マリアベルさんは\x01",
            "ＩＢＣグループの\x01",
            "取締役の１人なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "直接会社を経営なさってる\x01",
            "わけじゃありませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "あの歳でいくつもの事業を手がけて\x01",
            "成功を収めている方なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "自分たちも敬意を込めて\x01",
            "警護させてもらっていますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1E6D")

    Jump("loc_24A7")

    label("loc_1E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1F2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1ED4")

    #C0098
    ChrTalk(
        0xFE,
        "本日も異常無しです。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ本社ビルは万全の\x01",
            "警備体制ですからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F26")

    label("loc_1ED4")


    #C0100
    ChrTalk(
        0xFE,
        "本日も異常無しです。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ本社ビルは開業以来\x01",
            "オールグリーンですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1F26")

    Jump("loc_24A7")

    label("loc_1F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1F88")

    #C0102
    ChrTalk(
        0xFE,
        (
            "本日はＩＢＣグループの\x01",
            "重役会議の日ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        "警備にも気を遣いますよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24A7")

    label("loc_1F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_209B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2029")

    #C0104
    ChrTalk(
        0xFE,
        (
            "うちの保安部は、周辺諸国の各地域に\x01",
            "治安レベルの格付けを行っているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "クロイス総裁が出張に\x01",
            "向かわれる事もありますからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2096")

    label("loc_2029")


    #C0106
    ChrTalk(
        0xFE,
        (
            "近頃、市内の治安レベルが\x01",
            "悪化しているそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "自分たちも気を付けて\x01",
            "おかなければいけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2096")

    Jump("loc_24A7")

    label("loc_209B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_220B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_213F")

    #C0108
    ChrTalk(
        0xFE,
        (
            "受付に問い合わせれば、\x01",
            "どこの国の口座からでも\x01",
            "ミラをお引き出しできますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "……あ、自分は別に\x01",
            "窓口案内をするつもりはないんですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2206")

    label("loc_213F")


    #C0110
    ChrTalk(
        0xFE,
        (
            "当ＩＢＣ銀行は\x01",
            "世界中に支店があるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "傘下の銀行も多く、今では\x01",
            "世界一の銀行網を敷いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "ここの受付に問い合わせれば、\x01",
            "どこの国の口座からでも\x01",
            "ミラをお引き出しできますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2206")

    Jump("loc_24A7")

    label("loc_220B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2361")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_229E")

    #C0113
    ChrTalk(
        0xFE,
        (
            "この近代的なクロスベルでも\x01",
            "まだ魔獣被害が発生するんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "警備会社の者として\x01",
            "心を引き締めるべきかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235C")

    label("loc_229E")


    #C0115
    ChrTalk(
        0xFE,
        (
            "なんでも、各地に\x01",
            "魔獣が出没しているそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        "わが社の方にも連絡が来ましたよ。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "ウルスラ医大では\x01",
            "研修生が襲われたとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "さぞ怖かったろうに。\x01",
            "同情してしまいますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_235C")

    Jump("loc_24A7")

    label("loc_2361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23DF")

    #C0119
    ChrTalk(
        0xFE,
        (
            "受付の横にいると\x01",
            "よく質問されてしまうんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "あの、口座のご確認でしたら\x01",
            "受付にてお願いしますよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A7")

    label("loc_23DF")


    #C0121
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませ。\x01",
            "クロスベル国際銀行へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "……自分は配属になって２年ですが、\x01",
            "よくお客様に窓口案内を行います。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "受付の横が担当だからでしょうか。\x01",
            "よく尋ねられてしまうんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_24A7")

    TalkEnd(0xFE)
    Return()

    # Function_5_1516 end

    def Function_6_24AB(): pass

    label("Function_6_24AB")

    Call(0, 7)
    Return()

    # Function_6_24AB end

    def Function_7_24AF(): pass

    label("Function_7_24AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24C6")
    Call(0, 20)
    Return()

    label("loc_24C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24F5")
    Call(0, 24)
    Return()

    label("loc_24F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2516")
    Call(0, 21)
    Return()

    label("loc_2516")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28E0")

    #C0124
    ChrTalk(
        0xA,
        (
            "いらっしゃいませ。\x01",
            "クロスベル国際銀行へようこそ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xA, 0x102, 500)

    #C0125
    ChrTalk(
        0xA,
        "あら、そちらは……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "やはり、エリィ様でしたか！\x01",
            "お久しゅうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#0005F（え……？）\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        "#0205F（エリィさん……？）\x02",
    )

    CloseMessageWindow()

    def lambda_2607():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2607)

    def lambda_2614():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2614)

    def lambda_2621():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2621)
    Sleep(300)

    #C0129
    ChrTalk(
        0x102,
        (
            "#0100Fこんにちは、ランフィさん。\x01",
            "お久し振りですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "こうしてお会いするのは\x01",
            "留学に向かわれるとき以来ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        (
            "……そうですわ、\x01",
            "さっそくマリアベル様に\x01",
            "お知らせいたしましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "丁度ミシュラムの視察に\x01",
            "お出掛けになりましたが、きっと\x01",
            "喜んでお戻りになると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        (
            "#0104Fふふ……ベルも\x01",
            "相変わらず忙しそうね。\x02\x03",

            "#0100F構わないわ、今日はベルに\x01",
            "用事があったわけではないし。\x02\x03",

            "また日を改めて伺います。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "そうですか……\x01",
            "ではそうお伝えしておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0135
    ChrTalk(
        0x104,
        (
            "#0305F（お嬢……ＩＢＣの人と\x01",
            "  知り合いだったのかよ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#0005F（それもかなり\x01",
            "  フレンドリーだ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x103,
        (
            "#203F（ひそひそ、まさに\x01",
            "  お嬢様ですね……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    #C0138
    ChrTalk(
        0x102,
        "#0113F……あの、聞こえてるのだけど。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 4)
    Jump("loc_2BB9")

    label("loc_28E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AC8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2907")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC3")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",              # 0
            "換金をする\x01",            # 1
            "依頼について聞く\x01",      # 2
            "やめる\x01",                # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2974")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2974")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29A7")
    OP_AF(0xB5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 2)), scpexpr(EXPR_END)), "loc_29A2")
    Sleep(100)
    Call(0, 22)
    TalkEnd(0xA)
    Return()

    label("loc_29A2")

    Jump("loc_2ABE")

    label("loc_29A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A8E")

    #C0139
    ChrTalk(
        0xA,
        (
            "業務確認のため、\x01",
            "皆さんには実際に換金サービスを\x01",
            "利用して頂きたいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "全７種のセピスを\x01",
            "それぞれ３０個ずつ……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "それだけ換金していただければ\x01",
            "十分だと思います。\x01",
            "よろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2ABE")

    label("loc_2A8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AA2")
    Jump("loc_2ABE")

    label("loc_2AA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ABE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)

    label("loc_2ABE")

    Jump("loc_2907")

    label("loc_2AC3")

    Jump("loc_2BB9")

    label("loc_2AC8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BB9")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "換金をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B2E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2B2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2B60")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2B59")
    OP_AF(0xB7)
    Jump("loc_2B5B")

    label("loc_2B59")

    OP_AF(0xB6)

    label("loc_2B5B")

    Jump("loc_2B75")

    label("loc_2B60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2B73")
    OP_AF(0xB5)
    Jump("loc_2B75")

    label("loc_2B73")

    OP_AF(0xB4)

    label("loc_2B75")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BB4")

    label("loc_2B84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B98")
    Jump("loc_2BB4")

    label("loc_2B98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BB4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)

    label("loc_2BB4")

    Jump("loc_2AD2")

    label("loc_2BB9")

    TalkEnd(0xA)
    Return()

    # Function_7_24AF end

    def Function_8_2BBD(): pass

    label("Function_8_2BBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D20")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2C89")

    #C0142
    ChrTalk(
        0xA,
        (
            "カーラ様はメイドの方に\x01",
            "色々指示されていたみたいですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "グランセルのホテルを\x01",
            "予約するように……とか。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "ロビーでも大声で\x01",
            "話されていたようです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D1B")

    label("loc_2C89")


    #C0145
    ChrTalk(
        0xA,
        "先ほど会議が終わりまして……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        (
            "マリアベル様は今は総裁室に\x01",
            "いらっしゃると思いますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        (
            "そちらのエレベーターで\x01",
            "１６階へお進みください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D1B")

    Jump("loc_4752")

    label("loc_2D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2E22")

    #C0148
    ChrTalk(
        0xA,
        (
            "本日はご協力、\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xA,
        (
            "これで新サービスも\x01",
            "無事実施できそうですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "お渡ししたカードは\x01",
            "有効としておきますので、\x01",
            "ぜひご利用くださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#0000Fはは……活用させていただきます。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x104,
        "#0300F恐るべしＩＢＣ、だな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4752")

    label("loc_2E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2F74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2ECF")

    #C0153
    ChrTalk(
        0xA,
        (
            "市役所に問い合わせたところ、\x01",
            "クロスベル空港が\x01",
            "臨時閉港しているようなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        (
            "まあ今回は影響ないかと\x01",
            "思いますが……\x01",
            "突然の話で驚きましたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F6F")

    label("loc_2ECF")


    #C0155
    ChrTalk(
        0xA,
        (
            "本日はクロスベル空港が\x01",
            "臨時の検査閉港となっているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xA,
        (
            "まあ総裁もマリアベルお嬢様も\x01",
            "共和国方面の出張ですので、\x01",
            "影響はないかと思いますが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2F6F")

    Jump("loc_4752")

    label("loc_2F74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2FF3")

    #C0157
    ChrTalk(
        0xA,
        (
            "マリアベル様は重役の方たちと\x01",
            "協議を重ねておられますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xA,
        (
            "株価に影響が無ければ\x01",
            "いいのですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3134")

    label("loc_2FF3")


    #C0159
    ChrTalk(
        0xA,
        (
            "どうしましょう、\x01",
            "クロイス総裁がお留守のときに……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#0000F港湾区の事件の事ですね。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#0100Fランフィさん、こちらは\x01",
            "何ともなかったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xA,
        (
            "ええ、実害は\x01",
            "まったくありませんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "ですが株価は\x01",
            "敏感なものですから……\x01",
            "何らかの影響はあるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        (
            "今重役の方たちも\x01",
            "協議なさっているようですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3134")

    Jump("loc_4752")

    label("loc_3139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3324")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_31B2")

    #C0165
    ChrTalk(
        0xA,
        (
            "クロイス総裁は\x01",
            "何をなさっているのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xA,
        (
            "夕方からは相談もあると\x01",
            "仰ってましたのに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_331F")

    label("loc_31B2")


    #C0167
    ChrTalk(
        0xA,
        (
            "あらエリィ様、\x01",
            "いらっしゃって良かったですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "本日はクロイス総裁が\x01",
            "長期出張から戻られるはずなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "……そろそろ到着なさる\x01",
            "時間なのですが…………\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_END)), "loc_331C")

    #C0170
    ChrTalk(
        0x102,
        (
            "#0100Fあはは……\x01",
            "おじさまならさっき\x01",
            "ビルの前でお見かけしましたよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0171
    ChrTalk(
        0xA,
        "あら、そうだったのですか？\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "では何をなさっているのでしょうか。\x01",
            "よほどのご用事でも……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_331C")

    SetScenarioFlags(0x0, 2)

    label("loc_331F")

    Jump("loc_4752")

    label("loc_3324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3394")

    #C0173
    ChrTalk(
        0xA,
        (
            "総裁は本日も\x01",
            "出張なさっていますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        (
            "申し訳ございません。\x01",
            "数日で戻られると思うのですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4752")

    label("loc_3394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3501")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_342C")

    #C0175
    ChrTalk(
        0xA,
        (
            "クロイス総裁は今晩から\x01",
            "祝賀会への出席と出張の予定が\x01",
            "立て込んでおります。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xA,
        (
            "しばらくはお会いに\x01",
            "なれないかもしませんわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34FC")

    label("loc_342C")


    #C0177
    ChrTalk(
        0xA,
        (
            "先ほどマリアベル様が\x01",
            "いらっしゃったのです。\x01",
            "重役会議も終わったそうですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "ですが総裁は今晩から\x01",
            "祝賀会への出席と出張が\x01",
            "立て込んでおりますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xA,
        (
            "しばらくはお会いに\x01",
            "なれないかもしませんわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_34FC")

    Jump("loc_4752")

    label("loc_3501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_358E")

    #C0180
    ChrTalk(
        0xA,
        (
            "そういえば……本日は\x01",
            "早朝から会議があるようですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xA,
        (
            "記念祭だというのに忙しいと\x01",
            "総裁がこぼしておられました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_358E")


    #C0182
    ChrTalk(
        0xA,
        (
            "本日もお客様が多めなのですが、\x01",
            "コリンナが仕事の\x01",
            "速い子なので助かりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        (
            "ただ……忙しくても\x01",
            "休憩時間を削らないのが\x01",
            "ポリシーらしくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xA,
        (
            "ふう、時間になるといつの間にか\x01",
            "消えてしまうのですけれど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3662")

    Jump("loc_4752")

    label("loc_3667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_37DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3707")

    #C0185
    ChrTalk(
        0xA,
        (
            "総裁もマリアベル様も\x01",
            "本日は留守になさっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        (
            "エリィ様、ご用でしたら\x01",
            "ウルスラ医科大学に向かわれると\x01",
            "いいかもしれませんわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37D8")

    label("loc_3707")


    #C0187
    ChrTalk(
        0xA,
        (
            "いらっしゃいませ。\x01",
            "ようこそクロスベル国際銀行へ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        (
            "総裁もマリアベル様も\x01",
            "本日は留守になさっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        (
            "ウルスラ医科大学に\x01",
            "向かわれるといいかもしれませんわ。\x01",
            "今ごろお着きになっている頃でしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_37D8")

    Jump("loc_4752")

    label("loc_37DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3A4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 2)), scpexpr(EXPR_END)), "loc_3857")

    #C0190
    ChrTalk(
        0xA,
        (
            "そうそう、マリアベル様なら\x01",
            "お部屋にいらっしゃいますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xA,
        "今ならお会いになれると思います。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A47")

    label("loc_3857")


    #C0192
    ChrTalk(
        0xA,
        (
            "いらっしゃいませ。\x01",
            "クロスベル国際銀行へようこそ──\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        "これは、皆様でしたか。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xA,
        (
            "クロスベル創立７０周年、\x01",
            "おめでとうございますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x102,
        (
            "#0100Fありがとうございます。\x02\x03",

            "ランフィさんの方も\x01",
            "お忙しそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xA,
        (
            "ええ、創立記念祭は\x01",
            "クロスベル内だけの祭典ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xA,
        (
            "国際銀行としては\x01",
            "業務を止めるわけには参りません。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xA,
        "全日平常営業ですわ。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        "#0006Fそ、それは大変ですね。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xA,
        (
            "ふふ、記念祭の後に\x01",
            "代休を頂けますからご心配なく。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xA,
        (
            "銀行をご利用の際は\x01",
            "遠慮なく申し付けてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 2)

    label("loc_3A47")

    Jump("loc_4752")

    label("loc_3A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3C01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3AE4")

    #C0202
    ChrTalk(
        0xA,
        (
            "総裁は出張に\x01",
            "出てしまわれまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xA,
        (
            "マリアベル様なら\x01",
            "自室にいらっしゃると思いますわ。\x01",
            "どうかお会いになって行って下さい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BFC")

    label("loc_3AE4")


    #C0204
    ChrTalk(
        0xA,
        (
            "総裁は出張に\x01",
            "出てしまわれまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xA,
        (
            "お帰りは２週間ほど\x01",
            "先になるかと思いますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        "#0100Fやっぱりお忙しいみたいですね……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xA,
        (
            "ええ、ここ数年は\x01",
            "外国の銀行との提携を\x01",
            "精力的に行っておられるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xA,
        (
            "一度に何カ国もお回りになって\x01",
            "たまに戻られるような生活なんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3BFC")

    Jump("loc_4752")

    label("loc_3C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_3DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3C70")

    #C0209
    ChrTalk(
        0xA,
        (
            "エリィ様、\x01",
            "どうかまたいらしてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xA,
        (
            "マリアベル様も\x01",
            "お喜びになるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D9C")

    label("loc_3C70")


    #C0211
    ChrTalk(
        0xA,
        (
            "よかったですわ、\x01",
            "マリアベル様にも\x01",
            "お会いになられたようで。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xA,
        (
            "エリィ様、認証カードは\x01",
            "このまま有効ですから\x01",
            "どうかまたいらしてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xA,
        (
            "マリアベル様も\x01",
            "お喜びになるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        (
            "#0006Fあの様子じゃ、会うたびに\x01",
            "絡まれそうだけどな……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        (
            "#0106Fう、うーん……\x01",
            "（ベルは強引なのよね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3D9C")

    Jump("loc_4752")

    label("loc_3DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3E27")

    #C0216
    ChrTalk(
        0xA,
        (
            "総裁がお会いになるそうです。\x01",
            "最上階の総裁室へお通り下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xA,
        (
            "エレベーターは、\x01",
            "当フロア右手となっておりますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4752")

    label("loc_3E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3FA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3ECB")

    #C0218
    ChrTalk(
        0xA,
        (
            "コリンナは休憩時間になると\x01",
            "すばやく消えてしまうのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xA,
        (
            "お客様に対しても\x01",
            "思い切りが良すぎる気がしますね。\x01",
            "優秀ではあるのですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F9D")

    label("loc_3ECB")


    #C0220
    ChrTalk(
        0xA,
        (
            "去年から入ったコリンナは\x01",
            "とても優秀な子なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xA,
        (
            "でも……休憩時間になると\x01",
            "すばやく消えてしまうところが\x01",
            "少し問題ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xA,
        (
            "優秀ではあるのだけど……\x01",
            "どこか思い切りが\x01",
            "良すぎるんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3F9D")

    Jump("loc_4752")

    label("loc_3FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4348")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_40A8")

    #C0223
    ChrTalk(
        0xA,
        (
            "最近の投資相場は\x01",
            "エリィ様がいらっしゃった頃より\x01",
            "さらに拡大しておりますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xA,
        (
            "様々な投資スタイルも\x01",
            "日々生み出され、ディーラーの方々も\x01",
            "工夫を競っておられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xA,
        (
            "お気が向いたらお越しくださいませ。\x01",
            "詳しく案内させていただきますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4343")

    label("loc_40A8")


    #C0226
    ChrTalk(
        0xA,
        (
            "最近は投資話にいらっしゃる\x01",
            "お客様が多いようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xA,
        (
            "ＩＢＣ証券への問い合わせが\x01",
            "増えているように思います。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_417E")

    #C0228
    ChrTalk(
        0xA,
        (
            "皆さんにご協力いただいた\x01",
            "新サービスも大変好評ですし。\x01",
            "その影響もあるようですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_417E")


    #C0229
    ChrTalk(
        0xA,
        (
            "そういえば……\x01",
            "エリィ様も久々にいかがですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xA,
        (
            "以前お使いになっていた口座が\x01",
            "まだ残っておりますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        (
            "#0000Fエリィ、\x01",
            "投資とかやってたのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x104,
        "#0309Fヒュー、そりゃ凄えな！\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x102,
        (
            "#0103Fその、昔勉強のためにね。\x01",
            "投資は政治的な動きも反映するから\x01",
            "とても勉強になるのよ。\x02\x03",

            "#0100Fでも今は仕事があるから\x01",
            "学生の頃のようにはいかないわ。\x01",
            "……ごめんなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xA,
        (
            "いえいえ。\x01",
            "またよろしいときにお越しください。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xA,
        "改めて案内をさせて頂きますから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4343")

    Jump("loc_4752")

    label("loc_4348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_44E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_43B9")

    #C0236
    ChrTalk(
        0xA,
        (
            "マリアベル様も\x01",
            "大変心配しておられました。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xA,
        (
            "どうかご無理は\x01",
            "なさらないで下さいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44DC")

    label("loc_43B9")


    #C0238
    ChrTalk(
        0xA,
        (
            "エリィ様のご活躍、\x01",
            "わたくしも聞き及んでおりますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x102,
        (
            "#0100Fあはは……\x01",
            "クロスベルタイムズ、ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xA,
        (
            "ええ、先日の記事は\x01",
            "目を引きましたもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xA,
        (
            "……マリアベル様も\x01",
            "エリィ様の事を\x01",
            "大変心配しておられました。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xA,
        (
            "仕事なのは分かりますが、\x01",
            "どうかご無理をなさらないで下さいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_44DC")

    Jump("loc_4752")

    label("loc_44E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4607")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_454E")

    #C0243
    ChrTalk(
        0xA,
        (
            "こちらではビル内の\x01",
            "企業案内も行っておりますわ。\x01",
            "何なりとお申し付けくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4602")

    label("loc_454E")


    #C0244
    ChrTalk(
        0xA,
        (
            "当受付ではビル内の\x01",
            "企業案内も行っておりますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xA,
        (
            "なにせグループ各社を含め\x01",
            "２０数社が存在しますから……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xA,
        (
            "どなたかのお呼び出しの際は\x01",
            "こちらにお申し付けくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4602")

    Jump("loc_4752")

    label("loc_4607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4694")

    #C0247
    ChrTalk(
        0xA,
        (
            "マリアベル様には\x01",
            "必ずお伝えしておきましょう。\x01",
            "きっとお喜びになりますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xA,
        (
            "エリィ様、また\x01",
            "いつでもお越しくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4752")

    label("loc_4694")


    #C0249
    ChrTalk(
        0xA,
        (
            "いらっしゃいませ。\x01",
            "クロスベル国際銀行へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "生憎マリアベル様は\x01",
            "朝から視察に出ておられまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xA,
        "大変申し訳ございませんわ。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xA,
        (
            "本日の事は\x01",
            "必ずお伝えしておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4752")

    Return()

    # Function_8_2BBD end

    def Function_9_4753(): pass

    label("Function_9_4753")

    Call(0, 10)
    Return()

    # Function_9_4753 end

    def Function_10_4757(): pass

    label("Function_10_4757")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4852")

    #C0253
    ChrTalk(
        0xB,
        (
            "あれ、今日はリゼロさんは\x01",
            "いらっしゃってないようですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xB,
        (
            "昨日までは毎日いらっしゃる\x01",
            "常連さんでございましたがー。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_484D")

    #C0255
    ChrTalk(
        0x101,
        "#0001F（……例の行方不明者、か……）\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x102,
        (
            "#0101F（ＩＢＣにもよく来ている\x01",
            "  人だったみたいね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_484D")

    Jump("loc_5974")

    label("loc_4852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_494A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_48B6")

    #C0257
    ChrTalk(
        0xB,
        (
            "ビル内はしごく\x01",
            "安全でございますー。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xB,
        "株価の方は存じ上げませんがー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4945")

    label("loc_48B6")


    #C0259
    ChrTalk(
        0xB,
        (
            "襲撃事件ですか。\x01",
            "やれやれでございますねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xB,
        (
            "まあこのビルは保安部が\x01",
            "万全の警備を敷いてますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xB,
        "何の心配もございませんがー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4945")

    Jump("loc_5974")

    label("loc_494A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4A82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_49DD")

    #C0262
    ChrTalk(
        0xB,
        (
            "……リゼロさん、最近かなり\x01",
            "ツイてらっしゃるようですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xB,
        (
            "まあ、こういうときは\x01",
            "しっぺ返しが怖い物でございますが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A7D")

    label("loc_49DD")


    #C0264
    ChrTalk(
        0xB,
        (
            "……リゼロさん、最近かなり\x01",
            "ツイてらっしゃるようですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xB,
        (
            "今朝も投資話を\x01",
            "一山当てられました。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xB,
        (
            "これで２週連続のＷＩＮ……\x01",
            "中々やられますねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4A7D")

    Jump("loc_5974")

    label("loc_4A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4B09")

    #C0267
    ChrTalk(
        0xB,
        (
            "ＩＢＣは明日は\x01",
            "お休みとなっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xB,
        (
            "……本日を乗り切れば\x01",
            "休暇でございますねー。\x01",
            "待ち遠しいでございますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5974")

    label("loc_4B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4BED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4B57")

    #C0269
    ChrTalk(
        0xB,
        (
            "マリアベル様はあれで\x01",
            "心お優しい方でございますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE8")

    label("loc_4B57")


    #C0270
    ChrTalk(
        0xB,
        (
            "マリアベル様は\x01",
            "祭りを遊べない私達を\x01",
            "ねぎらってくださいましたー。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xB,
        (
            "トップがああいう方ですと、\x01",
            "こちらもやる気が\x01",
            "沸いてまいりますねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4BE8")

    Jump("loc_5974")

    label("loc_4BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4D38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4C60")

    #C0272
    ChrTalk(
        0xB,
        (
            "記念祭は困った方が\x01",
            "多いですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xB,
        (
            "申込書類など３０秒で\x01",
            "書きやがれでございますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D33")

    label("loc_4C60")


    #C0274
    ChrTalk(
        0xB,
        (
            "先ほどは、記念に\x01",
            "ＩＢＣ口座開設したいという\x01",
            "お客様がいらっしゃいましてー。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xB,
        (
            "ご自分から言い出したくせに\x01",
            "パレードまで時間が無い、などと焦って\x01",
            "書類を書き損じられましたー。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xB,
        "やれやれでございますー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4D33")

    Jump("loc_5974")

    label("loc_4D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4E55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4D91")

    #C0277
    ChrTalk(
        0xB,
        (
            "記念祭は困った方が\x01",
            "多いですねー。\x01",
            "案内も大変でございますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E50")

    label("loc_4D91")


    #C0278
    ChrTalk(
        0xB,
        (
            "昨日のお客様は\x01",
            "てこずらせて頂きましたねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xB,
        (
            "銀行や預貯金の概念が\x01",
            "全くご理解いただけていない\x01",
            "方でしてー。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xB,
        (
            "ミラを貸せだの口座とはなんじゃだの、\x01",
            "小うるさい方でございましたー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4E50")

    Jump("loc_5974")

    label("loc_4E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4F35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4EC0")

    #C0281
    ChrTalk(
        0xB,
        (
            "ＩＢＣは国際グループですから\x01",
            "お休みとはなりません。\x01",
            "やれやれでございますねー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F30")

    label("loc_4EC0")


    #C0282
    ChrTalk(
        0xB,
        (
            "記念祭の間は\x01",
            "自治州内の会社は\x01",
            "大抵お休みでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xB,
        (
            "……その点だけは\x01",
            "羨ましいでございますねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4F30")

    Jump("loc_5974")

    label("loc_4F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5046")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4FAF")

    #C0284
    ChrTalk(
        0xB,
        (
            "万が一のため、社内の端末は\x01",
            "全て使用停止となってございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xB,
        "やれやれでございますねー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5041")

    label("loc_4FAF")


    #C0286
    ChrTalk(
        0xB,
        (
            "保安部より連絡、\x01",
            "ハッキングの穴は封鎖済み……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xB,
        "……ようやく端末が使えますね。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xB,
        (
            "やれやれ、勘弁して\x01",
            "ほしいものでございますー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)

    label("loc_5041")

    Jump("loc_5974")

    label("loc_5046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_50DF")

    #C0289
    ChrTalk(
        0xB,
        (
            "ランフィ先輩は、元は秘書部に\x01",
            "いらっしゃったそうでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xB,
        (
            "とても字がお綺麗でして。\x01",
            "サインなどは\x01",
            "惚れ惚れしてしまいますねー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5974")

    label("loc_50DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_52A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5170")

    #C0291
    ChrTalk(
        0xB,
        (
            "ＩＢＣの受付業務は\x01",
            "大変やりがいのある仕事でございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xB,
        (
            "時間にも厳格ですし、\x01",
            "楽しく働かせてもらっておりますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_529C")

    label("loc_5170")


    #C0293
    ChrTalk(
        0xB,
        "（カタカタ、カタタッ……！）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 300)

    #C0294
    ChrTalk(
        0xB,
        (
            "私は以前冴えない中小企業に\x01",
            "勤めておりましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xB,
        (
            "端末操作の腕を買われ、\x01",
            "ＩＢＣに転職させて頂きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xB,
        (
            "こちらはやりがいのある仕事ですし\x01",
            "時間にも厳格ですからー。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xB,
        (
            "お陰様で大変楽しく\x01",
            "働かせてもらっておりますー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_9E(0xB, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    ClearChrFlags(0xB, 0x10)

    label("loc_529C")

    Jump("loc_5974")

    label("loc_52A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_54AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_533F")

    #C0298
    ChrTalk(
        0xB,
        (
            "いらっしゃいませー。\x01",
            "ＩＢＣ本店受付へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xB,
        (
            "こちら窓口では\x01",
            "各種ご案内も致しております。\x01",
            "何なりとお申し付け下さいませー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54A9")

    label("loc_533F")


    #C0300
    ChrTalk(
        0xB,
        (
            "いらっしゃいませー。\x01",
            "ＩＢＣ本店窓口へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xB,
        (
            "ご口座の開設やお預け、お引き出し、\x01",
            "各種証券のお取引……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xB,
        (
            "投資や融資のご紹介から\x01",
            "ご資産、不動産の運用相談も\x01",
            "承っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xB,
        "ぜひご活用くださいませー。\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        (
            "#0005F（ＩＢＣに行けば\x01",
            "  何でも出来そうなノリだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x102,
        (
            "#0100F（実際……ミラに\x01",
            "  関することならほとんど\x01",
            "  網羅しているらしいけど。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_54A9")

    Jump("loc_5974")

    label("loc_54AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5673")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_554F")

    #C0306
    ChrTalk(
        0xB,
        (
            "導力ネットも試験段階ですし、\x01",
            "銀行業務は全て書類作業でございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xB,
        (
            "早急に全面導力化していただけると\x01",
            "業務効率も上がるのですがー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_566E")

    label("loc_554F")


    #C0308
    ChrTalk(
        0xB,
        (
            "当ビルは数年前から\x01",
            "完全導力化されておりますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xB,
        (
            "この端末も、現在の所\x01",
            "社内連絡程度にしか\x01",
            "使われてございません。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xB,
        (
            "業務部での利用も\x01",
            "まだ始まったばかりでございますー。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xB,
        (
            "それも社内ネットワークのみの接続……\x01",
            "裏方の銀行業務にいたっては\x01",
            "いまだ書類作業となっておりますー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_566E")

    Jump("loc_5974")

    label("loc_5673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5808")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_56EA")

    #C0312
    ChrTalk(
        0xB,
        (
            "ＩＢＣの口座をお持ちですと\x01",
            "世界各国の支店でお取引が可能ですよ。\x01",
            "是非ご利用くださいませー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5803")

    label("loc_56EA")


    #C0313
    ChrTalk(
        0xB,
        "（カタカタカタ、カタタタッ……！）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 300)

    #C0314
    ChrTalk(
        0xB,
        (
            "これはお客様、\x01",
            "口座をご利用ですかー？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        (
            "ＩＢＣの口座をお持ちですと\x01",
            "世界各国の支店でお取引が可能です。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xB,
        (
            "提携銀行からのご利用も\x01",
            "できますから大変便利となりますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xB,
        "是非ご利用くださいませー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_9E(0xB, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    ClearChrFlags(0xB, 0x10)

    label("loc_5803")

    Jump("loc_5974")

    label("loc_5808")

    OP_4B(0xF, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_58DD")
    TurnDirection(0xF, 0x0, 0)
    TurnDirection(0xB, 0x0, 0)

    #C0318
    ChrTalk(
        0xF,
        (
            "あら……ごめんなさいね。\x01",
            "まだ手続きをしてもらっているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xB,
        (
            "申し訳ございません、\x01",
            "左手のソファーで\x01",
            "順番をお待ちくださいませー。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xB, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    OP_9E(0xF, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_596C")

    label("loc_58DD")


    #C0320
    ChrTalk(
        0xB,
        (
            "少々お待ちくださいませー。\x01",
            "（カタカタ、カタタッ……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xB,
        (
            "ただいま口座を\x01",
            "確認いたしますのでー。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xF,
        "ええ、よろしくお願いするわね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_596C")

    OP_4C(0xF, 0xFF)
    OP_4C(0xB, 0xFF)

    label("loc_5974")

    TalkEnd(0xB)
    Return()

    # Function_10_4757 end

    def Function_11_5978(): pass

    label("Function_11_5978")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A0C")
    Jump("loc_5A56")

    label("loc_5A0C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A2C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A56")

    label("loc_5A2C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A4C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A56")

    label("loc_5A4C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A56")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5ADF")

    #C0323
    ChrTalk(
        0xFE,
        (
            "信じられん、\x01",
            "こんな事は人生初めてだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        "まるで侮辱された気分だぞ！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B70")

    label("loc_5ADF")


    #C0325
    ChrTalk(
        0xFE,
        (
            "むう、クロスベルタイムズが\x01",
            "臨時休刊だと……？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "信じられん、何たることだ！\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "経済面のあのコラムが\x01",
            "毎回楽しみだったというのに……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5B70")

    Jump("loc_696B")

    label("loc_5B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5C7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5BF2")

    #C0328
    ChrTalk(
        0xFE,
        (
            "投資話なら\x01",
            "この私に任せてくれたまえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "記念祭の後からこちら、\x01",
            "山を当てまくりなものでねぇ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C75")

    label("loc_5BF2")


    #C0330
    ChrTalk(
        0xFE,
        "ふはは、また儲かったよ！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "記念祭の頃の損失など\x01",
            "またたく間に埋め合わせたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        (
            "ははははは……！\x01",
            "投資はいいなぁ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5C75")

    Jump("loc_696B")

    label("loc_5C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5CF5")

    #C0333
    ChrTalk(
        0xFE,
        (
            "祭りだというのに\x01",
            "仕事をしているから悪いのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "うむ、この大損失は\x01",
            "そういう啓示に違いない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DBE")

    label("loc_5CF5")

    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0335
    ChrTalk(
        0xFE,
        (
            "わ、分かったぞ……！\x01",
            "なぜ投資が外れてばかりなのか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "……きっと記念祭なのに\x01",
            "仕事をしてばかりなのが悪いのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "うむ、今日はどこかへ\x01",
            "遊びに行くとしようか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5DBE")

    Jump("loc_696B")

    label("loc_5DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5EBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5E4B")

    #C0338
    ChrTalk(
        0xFE,
        (
            "ゼロが３つほど\x01",
            "少ないなど考えられん。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "うむ、きっと必ず\x01",
            "見間違いであろう。\x01",
            "……………………（ごしごし）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EB7")

    label("loc_5E4B")


    #C0340
    ChrTalk(
        0xFE,
        (
            "ば、馬鹿な……\x01",
            "こんなはずでは……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        "……………………（ごしごし）\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        "……見間違いではないかな？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5EB7")

    Jump("loc_696B")

    label("loc_5EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5F1B")

    #C0343
    ChrTalk(
        0xFE,
        "今日こそは必ず儲けてやる……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "残り資産の３分の一。\x01",
            "これでどうだっ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_696B")

    label("loc_5F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_601E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5F65")

    #C0345
    ChrTalk(
        0xFE,
        (
            "むむむ、値動きが激しい……\x01",
            "これは難しいぞ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6019")

    label("loc_5F65")


    #C0346
    ChrTalk(
        0xFE,
        (
            "記念祭でどこも\x01",
            "値を上げているのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "逆を言うと、買いである投資株を\x01",
            "見つけるのが難しいという事なのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "こほん、つまりだ……\x01",
            "失敗しても仕方ないということだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6019")

    Jump("loc_696B")

    label("loc_601E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_60F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_606A")

    #C0349
    ChrTalk(
        0xFE,
        (
            "これだから観光客は……\x01",
            "まったくイライラするぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60F0")

    label("loc_606A")


    #C0350
    ChrTalk(
        0xFE,
        (
            "やれやれ……君たちも\x01",
            "ミラを下ろしに来た観光客かね？\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        (
            "遊ぶミラくらい、\x01",
            "事前に整えておきたまえ！\x01",
            "資産運用がなっていないぞ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_60F0")

    Jump("loc_696B")

    label("loc_60F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_620E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6178")

    #C0352
    ChrTalk(
        0xFE,
        (
            "なぜ端末が止まっているのだ。\x01",
            "誰か説明したまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "遅れたせいで損失が出たら\x01",
            "どうしてくれるのだ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6209")

    label("loc_6178")


    #C0354
    ChrTalk(
        0xFE,
        (
            "さっき受付に出向いたのだが、\x01",
            "端末が止まっており\x01",
            "決算が遅れるというのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        "む……一体どういう事だ。\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        "これはどこの誰の仕業だ……？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6209")

    Jump("loc_696B")

    label("loc_620E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_632C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_62A8")

    #C0357
    ChrTalk(
        0xFE,
        (
            "投資において大切なのは\x01",
            "若い頃に培われる感性だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "……投資や金融などは\x01",
            "日曜学校の必須教科に\x01",
            "取り入れても良いくらいだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6327")

    label("loc_62A8")


    #C0359
    ChrTalk(
        0xFE,
        (
            "おや……君たちも\x01",
            "ＩＢＣに用事かね。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        "若いのに感心感心。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        (
            "その調子で金融に対する\x01",
            "感性を磨いていくといいだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6327")

    Jump("loc_696B")

    label("loc_632C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6445")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6396")

    #C0362
    ChrTalk(
        0xFE,
        "ふはは、まあ驚かないでくれたまえ。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "これでも私は\x01",
            "資産運用のプロなのでね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6440")

    label("loc_6396")


    #C0364
    ChrTalk(
        0xFE,
        "私は貿易会社を経営していてね。\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "こちらの投資活動は、\x01",
            "まあ余暇のようなものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "くふふ、だがこれが儲かるのだよ。\x01",
            "先月はざっと\x01",
            "１００万ミラほど儲けたかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6440")

    Jump("loc_696B")

    label("loc_6445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6570")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_64DA")

    #C0367
    ChrTalk(
        0xFE,
        "記念祭はクロスベル最大の祭りなのだ。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "周辺諸国からも\x01",
            "膨大な人とミラが流れ込んでくる……\x01",
            "投資家としても見過ごせんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_656B")

    label("loc_64DA")


    #C0369
    ChrTalk(
        0xFE,
        "おっほん、本日の経済面は、と。\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "ふむやはり記念祭関連の\x01",
            "銘柄が動いているな……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "一投資家としても\x01",
            "記念祭という行事は見過ごせんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_656B")

    Jump("loc_696B")

    label("loc_6570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_671A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6612")

    #C0372
    ChrTalk(
        0xFE,
        (
            "ＩＢＣの起源は\x01",
            "中世末期に興った\x01",
            "一つの国際銀行だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "そこから発展し、時には苦汁を舐め……\x01",
            "そして今日の繁栄があるというわけだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6715")

    label("loc_6612")


    #C0374
    ChrTalk(
        0xFE,
        (
            "International Bank of Crossbell……\x01",
            "ここＩＢＣには\x01",
            "最新の導力設備が揃っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "だがＩＢＣとは\x01",
            "実はとても古い銀行なのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "その起源は中世まで遡り、\x01",
            "創業３００年近くになるという。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "まさに由緒正しい\x01",
            "『クロスベル国際銀行』と言えるだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6715")

    Jump("loc_696B")

    label("loc_671A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6864")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6787")

    #C0378
    ChrTalk(
        0xFE,
        (
            "クロスベルにもまだまだ\x01",
            "頭の固い連中は多い……\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        "まったく嘆かわしい事だな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_685F")

    label("loc_6787")


    #C0380
    ChrTalk(
        0xFE,
        (
            "クロスベルは中世より\x01",
            "貿易と七耀石#6Rセプチウム#の取引によって\x01",
            "繁栄してきた。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "しかしこの導力化の時代において\x01",
            "それでは通用しない……\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "これからの時代は金融と投資だよ。\x01",
            "ちまちました取引などやってられんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_685F")

    Jump("loc_696B")

    label("loc_6864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_68D3")

    #C0383
    ChrTalk(
        0xFE,
        "おや……私に何か用事かね？\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "特に無いなら静かにしたまえ。\x01",
            "ロビーには他の客もいるのだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_696B")

    label("loc_68D3")


    #C0385
    ChrTalk(
        0xFE,
        "おっほん、どれ経済面は、と。\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "ふむ、ＩＢＣが\x01",
            "新サービスを始めるのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "これはまた株価が動きそうだな。\x01",
            "ふはは、チェックしておくか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xC, 0x10)

    label("loc_696B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_5978 end

    def Function_12_6973(): pass

    label("Function_12_6973")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6E1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 3)), scpexpr(EXPR_END)), "loc_6A82")

    #C0388
    ChrTalk(
        0xFE,
        (
            "一応決まりもあるから、\x01",
            "財団からのミラは\x01",
            "今までどおり振り込んでおくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "だが……うん、\x01",
            "ティオ君の気持ちはよく分かった。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "何かのために使うか、\x01",
            "財団に返却するか……\x01",
            "いつかティオ君が決めてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x103,
        "#0200Fはい、考えておきます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E15")

    label("loc_6A82")


    #C0392
    ChrTalk(
        0xFE,
        "ギクギクッ……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 0)

    #C0393
    ChrTalk(
        0xFE,
        (
            "や、やあ、ティオ君……\x01",
            "ＩＢＣに用事かい……？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x103,
        (
            "#0203Fいえ別に。\x02\x03",

            "#0205F主任は一体何を……？\x01",
            "（挙動が怪しい……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0395
    ChrTalk(
        0xFE,
        "その、少しミラの振込みをね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0396
    ChrTalk(
        0xFE,
        (
            "ティオ君の生活費は\x01",
            "一応エプスタイン財団の方で\x01",
            "用意しているんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "……ティオ君、一度も\x01",
            "使ってくれないんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x103,
        (
            "#0200F今は警察のお給料がありますから。\x02\x03",

            "#0208Fそれに……今は支援課という場所で、\x01",
            "自分の力で生きていきたいもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x101,
        "#0000F……ティオ………\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        "そ、そうか……\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "うん、それもまた\x01",
            "ティオ君らしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "分かったよ、しばらく\x01",
            "お節介はよす事にしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "……だからティオ君、そのぅ、\x01",
            "今日の事は怒らないでね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0404
    ChrTalk(
        0x103,
        (
            "#0211F主任のそういう所が\x01",
            "ついイラッと来るのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 3)
    ClearChrFlags(0xE, 0x10)

    label("loc_6E15")

    Jump("loc_713B")

    label("loc_6E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E35")
    Call(0, 15)
    Jump("loc_6FDB")

    label("loc_6E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F50")

    #C0405
    ChrTalk(
        0xFE,
        (
            "そうだね、理論的には可能なんだが\x01",
            "演算能力が追いついていないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "エプスタイン財団製の\x01",
            "最新装置をもってしても\x01",
            "限界はある、ということだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#0005F（難しい話を\x01",
            "  してるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x103,
        (
            "#0203F（……一応、クロスベルでは\x01",
            "  最も詳しい専門家ですから。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6FDB")

    label("loc_6F50")


    #C0409
    ChrTalk(
        0xFE,
        (
            "理論的には可能なんだが\x01",
            "演算能力が追いついていないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "だがしかし、そこに\x01",
            "アルゴリズムの進化と発展の可能性が\x01",
            "あるわけだから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FDB")

    Jump("loc_713B")

    label("loc_6FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FF2")
    Call(0, 15)
    Jump("loc_713B")

    label("loc_6FF2")

    TurnDirection(0xFE, 0x103, 0)

    #C0411
    ChrTalk(
        0xFE,
        "ティ、ティオ君、お仕事頑張ってね。\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "それと……たまには\x01",
            "支部にも顔を出してくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "ティオ君あまり報告をくれないし……\x01",
            "僕は心配だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x103,
        "#0203F余計なお世話です。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0415
    ChrTalk(
        0xFE,
        (
            "や、やっぱり僕って\x01",
            "嫌われているのかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_713B")

    TalkEnd(0xFE)
    Return()

    # Function_12_6973 end

    def Function_13_713F(): pass

    label("Function_13_713F")

    EventBegin(0x1)
    Sound(160, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_7197():
        OP_92(0x101, 0x251C, 0x3E80, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7197)
    Sleep(50)

    def lambda_71AD():
        OP_92(0x102, 0x251C, 0x3E80, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_71AD)
    Sleep(50)

    def lambda_71C3():
        OP_92(0x103, 0x251C, 0x3E80, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_71C3)
    Sleep(50)

    def lambda_71D9():
        OP_92(0x104, 0x251C, 0x3E80, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_71D9)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    EventBegin(0x0)
    Fade(500)
    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(9500, 1500, 16000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0xE, 11000, 0, 16500, 270)
    SetChrPos(0xD, 11500, 0, 15600, 270)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_0D()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_68(5750, 1500, 17850, 4000)
    MoveCamera(44, 15, 0, 4000)
    BeginChrThread(0xE, 3, 0, 14)

    #N0416
    NpcTalk(
        0xE,
        "初老の男性",
        "うんうん、お役に立ったようだね。\x02",
    )

    CloseMessageWindow()

    #N0417
    NpcTalk(
        0xD,
        "研究員",
        "またお世話になってしまって。\x02",
    )

    CloseMessageWindow()

    #N0418
    NpcTalk(
        0xD,
        "研究員",
        "しかし助かりましたよ、主任。\x02",
    )

    CloseMessageWindow()

    #N0419
    NpcTalk(
        0xD,
        "研究員",
        (
            "あのアルゴリズムは\x01",
            "どうにも難しくて……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(0, 1900, 9000, 0)
    MoveCamera(35, 11, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 250, 300, 7750, 45)
    SetChrPos(0x102, 600, 300, 9100, 45)
    SetChrPos(0x104, -350, 300, 8750, 45)
    SetChrPos(0x103, 0, 300, 10150, 45)
    OP_0D()

    #C0420
    ChrTalk(
        0x103,
        "#0205F（……あれは………）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    WaitChrThread(0xE, 3)
    SetChrPos(0x0, 0, 300, 7750, 0)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x6F, 4)
    EventEnd(0x5)
    Return()

    # Function_13_713F end

    def Function_14_743A(): pass

    label("Function_14_743A")


    def lambda_743F():
        OP_97(0xE, 0xFFFFEE6C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_743F)

    def lambda_7459():
        OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_7459)
    Sleep(50)

    def lambda_746D():
        OP_97(0xD, 0xFFFFE69C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_746D)

    def lambda_7487():
        OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_7487)
    Sleep(1250)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    WaitChrThread(0xE, 1)

    def lambda_74B4():
        OP_97(0xE, 0x0, 0x0, 0x546, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_74B4)
    WaitChrThread(0xE, 1)

    def lambda_74D2():
        OP_93(0xE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_74D2)
    WaitChrThread(0xD, 1)

    def lambda_74E3():
        OP_97(0xD, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_74E3)
    WaitChrThread(0xD, 1)

    def lambda_7501():
        OP_93(0xD, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7501)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xD, 1)
    Return()

    # Function_14_743A end

    def Function_15_7512(): pass

    label("Function_15_7512")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(6500, 1200, 17000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x103, 6500, 0, 16350, 0)
    SetChrPos(0x102, 5900, 0, 15150, 0)
    SetChrPos(0x101, 7100, 0, 15350, 0)
    SetChrPos(0x104, 6500, 0, 14150, 0)
    OP_93(0xE, 0x10E, 0x0)
    OP_0D()

    #C0421
    ChrTalk(
        0x103,
        "#0205F主任、お久し振りですね。\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0422
    ChrTalk(
        0xE,
        "その声は……！？\x02",
    )

    CloseMessageWindow()

    def lambda_75EF():
        TurnDirection(0xD, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_75EF)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    TurnDirection(0xE, 0x103, 500)

    #C0423
    ChrTalk(
        0xE,
        (
            "や、や、やあ……\x01",
            "……ティオ君じゃないかぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xE,
        "げ、元気か～い？\x02",
    )

    CloseMessageWindow()
    OP_64(0xE)
    TurnDirection(0x101, 0x103, 500)

    #C0425
    ChrTalk(
        0x101,
        (
            "#0000F主任って……もしかして\x01",
            "この人がティオの上司……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0426
    ChrTalk(
        0x103,
        (
            "#0203Fええ、直接の上司──\x01",
            "魔導杖開発チームの主任では\x01",
            "ないんですが。\x02\x03",

            "#0200F導力ネットワークの専門家で\x01",
            "一応、クロスベルにある\x01",
            "エプスタイン財団支部の責任者です。\x02\x03",

            "……わたしの\x01",
            "現場監督という所ですね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_777A():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_777A)
    Sleep(50)
    OP_93(0x101, 0x0, 0x1F4)

    #C0427
    ChrTalk(
        0xE,
        (
            "警察の例の部署でも\x01",
            "何とかやっているようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xE,
        "うんうん、良かったよ～。\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xE,
        (
            "ティオ君はその、あまり\x01",
            "報告もくれないし……\x01",
            "僕ったら心配してしまってさぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x103,
        (
            "#0205Fこっそり武器屋に\x01",
            "魔導杖を置いたりしてましたよね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0431
    ChrTalk(
        0xE,
        "ギクッ……\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x101,
        (
            "#0000Fそういえばウェンディも\x01",
            "財団の人が\x01",
            "よく来るとか言っていたな……\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xE,
        "ギクギクッ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0434
    ChrTalk(
        0xE,
        "そ、そ、それはその……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    #C0435
    ChrTalk(
        0xE,
        (
            "マズイ、ティオ君を\x01",
            "怒らせてしまっただろうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xE,
        (
            "いやしかし、子供をたった一人で\x01",
            "この巨大な街に放り出すというのも……\x01",
            "ブツブツ……\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x103,
        "#0211F……主任、挙動不審です。\x02",
    )

    CloseMessageWindow()
    OP_9C(0xE, 0x0, 0x0, 0x0, 0x190, 0x2EE0)

    #C0438
    ChrTalk(
        0xE,
        "はうっ……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xE, 0x103, 500)

    #C0439
    ChrTalk(
        0x103,
        (
            "#0206Fふう……\x02\x03",

            "#0205Fともかく、市内のあちこちに\x01",
            "装備を仕込むのはやめて下さい。\x02\x03",

            "オリエンテーリングではないので。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xE,
        "ぐさっ……\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xE,
        (
            "ハハ、わ、分かったよ。\x01",
            "ゴメンねティオ君、機嫌なおして？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x103,
        (
            "#0211F……主任の\x01",
            "そういう所が嫌いです。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xE,
        (
            "ぐさぐさっ……\x01",
            "ハハ、そうだよね、うん分かるよ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0444
    ChrTalk(
        0x102,
        "#0106F（ティオちゃん、容赦ないわね……）\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x103,
        (
            "#0203F（……なんとなく\x01",
            "  イラッと来てしまうもので。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 6500, 0, 16350, 0)
    OP_93(0xD, 0x5A, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x6C, 5)
    EventEnd(0x5)
    Return()

    # Function_15_7512 end

    def Function_16_7C29(): pass

    label("Function_16_7C29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7C6D")

    #C0446
    ChrTalk(
        0xFE,
        (
            "な、なるほど……\x01",
            "まだまだ研究が必要ですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CA6")

    label("loc_7C6D")


    #C0447
    ChrTalk(
        0xFE,
        (
            "ふむふむ、なるほど……\x01",
            "主任のご意見はさすがですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CA6")

    TalkEnd(0xFE)
    Return()

    # Function_16_7C29 end

    def Function_17_7CAA(): pass

    label("Function_17_7CAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D80")

    #C0448
    ChrTalk(
        0xFE,
        (
            "今日はＩＢＣビル内の会社から\x01",
            "仕事の依頼が来ていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        (
            "こういうハイテクな場所は\x01",
            "どうにも落ち着かないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x103,
        (
            "#0203F（はいてく……\x01",
            "  なんだかおじさんくさい\x01",
            "  言い方ですね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7DCD")

    label("loc_7D80")


    #C0451
    ChrTalk(
        0xFE,
        (
            "……依頼主の会社は\x01",
            "何階に入ってるんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        "受付に聞いてみるかな。\x02",
    )

    CloseMessageWindow()

    label("loc_7DCD")

    TalkEnd(0xFE)
    Return()

    # Function_17_7CAA end

    def Function_18_7DD1(): pass

    label("Function_18_7DD1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EA2")

    #C0453
    ChrTalk(
        0xFE,
        (
            "世の中には株の取り引きのみで\x01",
            "生計を立てる者もいるという……\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "ふむ……そんな方法で\x01",
            "ミラを稼いで達成感のようなものが\x01",
            "得られるのだろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xFE,
        "……俺には縁のない世界だな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7F16")

    label("loc_7EA2")


    #C0456
    ChrTalk(
        0xFE,
        (
            "あるいは……株の値が上下する\x01",
            "ギャンブル性を楽しんでいるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "……どちらにしろ、\x01",
            "俺には縁のない世界だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F16")

    TalkEnd(0xFE)
    Return()

    # Function_18_7DD1 end

    def Function_19_7F1A(): pass

    label("Function_19_7F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8124")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7FB7")
    Jump("loc_8001")

    label("loc_7FB7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7FD7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8001")

    label("loc_7FD7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FF7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8001")

    label("loc_7FF7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8001")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_809F")

    #C0458
    ChrTalk(
        0xFE,
        (
            "ＩＢＣに預金を\x01",
            "下ろしに来たのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xFE,
        (
            "クロスベル市民なら\x01",
            "みんなＩＢＣよね。\x01",
            "利回りも一番だもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8118")

    label("loc_809F")


    #C0460
    ChrTalk(
        0xFE,
        (
            "孫の誕生日でね。\x01",
            "少し大きな買い物をしようと思って。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xFE,
        (
            "ひい、ふう、みい……\x01",
            "ええ、きちんと全額揃っているわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_8118")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_812D")

    label("loc_8124")

    TalkBegin(0xFE)
    Call(0, 10)
    TalkEnd(0xFE)

    label("loc_812D")

    Return()

    # Function_19_7F1A end

    def Function_20_812E(): pass

    label("Function_20_812E")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(1000)
    OP_68(0, 1300, 30100, 0)
    MoveCamera(37, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 0, 300, 28600, 0)
    SetChrPos(0x102, -1400, 300, 27300, 0)
    SetChrPos(0x103, -500, 300, 27000, 0)
    SetChrPos(0x104, 600, 300, 27600, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8592")

    #C0462
    ChrTalk(
        0xA,
        (
            "#5Pいらっしゃいませ。\x01",
            "クロスベル国際銀行へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xA,
        (
            "#5P……あらエリィ様、\x01",
            "それに特務支援課の方々も。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xA,
        (
            "#5P先日は新サービスのテストに\x01",
            "協力いただいて\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xA,
        (
            "#5Pお陰様で大変好評を\x01",
            "博しておりますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x101,
        "#0002F#12Pはは、そうなんですか。\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x103,
        "#12P#0202Fお力になれたみたいですね。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xA,
        (
            "#5Pええ、また何かあれば\x01",
            "よろしくお願いいたします。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xA,
        (
            "#5Pそれで……本日は\x01",
            "どのようなご用件でしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#0001F#12Pあ、えっと……\x02",
    )

    CloseMessageWindow()

    def lambda_8380():
        OP_96(0xFE, 0xFFFFFDA8, 0x12C, 0x7274, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8380)
    WaitChrThread(0x102, 1)

    #C0471
    ChrTalk(
        0x102,
        (
            "#6P#0104Fランフィさん、実は\x01",
            "問い合わせたい事があって。\x02\x03",

            "#0100Fディーター総裁は\x01",
            "いらっしゃるでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0472
    ChrTalk(
        0xA,
        (
            "#5Pあら……マリアベル様ではなく\x01",
            "クロイス総裁にご用件ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#6P#0103Fええ、アポイント無しなので\x01",
            "申しわけないんですけど……\x02\x03",

            "#0101Fそれとも……\x01",
            "やはりご不在でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xA,
        (
            "#5Pいえ、今日は珍しく\x01",
            "いらっしゃっていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0xA,
        (
            "#5P面会は同僚の方々も\x01",
            "ご一緒に……？\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x102,
        (
            "#6P#0102Fええ……とある事件について\x01",
            "少々、総裁に相談に乗って\x01",
            "いただきたい事がありまして……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B4F")

    label("loc_8592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_END)), "loc_888B")

    #C0477
    ChrTalk(
        0xA,
        (
            "#5Pいらっしゃいませ。\x01",
            "クロスベル国際銀行へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xA,
        (
            "#5P……あらエリィ様、\x01",
            "それに特務支援課の方々も。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xA,
        "#5P本日はどのようなご用件でしょう？\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x101,
        (
            "#12P#0012Fはは、どうも。\x02\x03",

            "#0001Fえっとその……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_866D():
        OP_96(0xFE, 0xFFFFFDA8, 0x12C, 0x7274, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_866D)
    WaitChrThread(0x102, 1)

    #C0481
    ChrTalk(
        0x102,
        (
            "#6P#0104Fこんにちは、ランフィさん。\x01",
            "実は問い合わせたい事があって。\x02\x03",

            "#0100Fディーター総裁は\x01",
            "いらっしゃるでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0482
    ChrTalk(
        0xA,
        (
            "#5Pあら……マリアベル様ではなく\x01",
            "クロイス総裁にご用件ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x102,
        (
            "#6P#0104Fええ、アポイント無しなので\x01",
            "申しわけないんですけど……\x02\x03",

            "#0101Fそれとも……\x01",
            "やはりご不在でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xA,
        (
            "#5Pいえ、今日は珍しく\x01",
            "いらっしゃっていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xA,
        (
            "#5P面会は同僚の方々も\x01",
            "ご一緒に……？\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x102,
        (
            "#6P#0102Fええ……とある事件について\x01",
            "少々、総裁に相談に乗って\x01",
            "いただきたい事がありまして……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B4F")

    label("loc_888B")


    #C0487
    ChrTalk(
        0xA,
        (
            "#5Pいらっしゃいませ。\x01",
            "クロスベル国際銀行へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xA,
        "#5P本日はどのようなご用件でしょう？\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x101,
        "#0001F#12Pえっと……\x02",
    )

    CloseMessageWindow()

    def lambda_890D():
        OP_96(0xFE, 0xFFFFFDA8, 0x12C, 0x7274, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_890D)
    WaitChrThread(0x102, 1)

    #C0490
    ChrTalk(
        0x102,
        (
            "#6P#0104Fこんにちは、ランフィさん。\x02\x03",

            "#0100Fディーター総裁は\x01",
            "いらっしゃるでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0491
    ChrTalk(
        0xA,
        (
            "#5Pまあ、エリィ様！\x01",
            "ようこそいらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xA,
        (
            "#5Pマリアベル様ではなく、\x01",
            "クロイス総裁にご用件ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x102,
        (
            "#6P#0103Fええ、アポイント無しなので\x01",
            "申しわけないんですけど……\x02\x03",

            "#0101Fそれとも……\x01",
            "やはりご不在でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xA,
        (
            "#5Pいえ、今日は珍しく\x01",
            "いらっしゃっていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xA,
        "#5Pえっと、そちらの方々は……\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        (
            "#6P#0102F私の同僚で、\x01",
            "クロスベル警察の者です。\x02\x03",

            "とある事件について\x01",
            "少々、総裁に相談に乗って\x01",
            "いただきたい事がありまして……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B4F")


    #C0497
    ChrTalk(
        0xA,
        "#5Pまあ、そうなんですか。\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xA,
        (
            "#5P分かりました。\x01",
            "少々お待ちください。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0xA, 0x258, 0x7D00, 0x190)

    def lambda_8BAC():
        OP_95(0xFE, 600, 300, 32000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8BAC)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x190)
    Sleep(300)

    #C0499
    ChrTalk(
        0x104,
        (
            "#12P#0302F（さすがお嬢……\x01",
            "  ほぼ顔パスじゃねえか。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_END)), "loc_8C53")

    #C0500
    ChrTalk(
        0x101,
        (
            "#0002F（はは……やっぱり\x01",
            "  世界が違うって感じだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C88")

    label("loc_8C53")


    #C0501
    ChrTalk(
        0x101,
        (
            "#0012F（確かに……\x01",
            "  世界が違うって感じだな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C88")


    #C0502
    ChrTalk(
        0xA,
        "#5Pはい……はい……\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xA,
        (
            "#5Pかしこまりました。\x01",
            "そのままお通しします。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x190)

    def lambda_8CDF():
        OP_95(0xFE, 0, 300, 31700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8CDF)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0xB4, 0x190)

    #C0504
    ChrTalk(
        0xA,
        (
            "#5P──エリィ様。\x01",
            "総裁がお会いになるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xA,
        (
            "#5Pカードを発行しますので\x01",
            "そのまま最上階の総裁室まで\x01",
            "直接お行きになってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x102,
        "#6P#0109Fええ、ありがとう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0507
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x320),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x320, 1)
    OP_93(0x102, 0xB4, 0x1F4)

    #C0508
    ChrTalk(
        0x102,
        (
            "#0100F#5Pそれじゃあ、みんな。\x01",
            "エレベーターに乗りましょう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8E45():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8E45)
    Sleep(50)
    TurnDirection(0x104, 0x102, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_END)), "loc_8ED5")

    #C0509
    ChrTalk(
        0x101,
        (
            "#0002Fああ、そうしよう。\x01",
            "……助かったよ、エリィ。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x104,
        (
            "#0300Fそんじゃま、早いこと\x01",
            "お邪魔するとしようかね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F22")

    label("loc_8ED5")


    #C0511
    ChrTalk(
        0x101,
        "#0002Fあ、ああ……\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x104,
        (
            "#0300F……そんじゃま、\x01",
            "お邪魔するとしようかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F22")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 300, 28800, 180)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x82, 2)
    OP_29(0x43, 0x1, 0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_20_812E end

    def Function_21_8F4B(): pass

    label("Function_21_8F4B")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(1000)
    OP_68(0, 1000, 30100, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 300, 28600, 0)
    SetChrPos(0x102, -1400, 300, 27300, 0)
    SetChrPos(0x103, -500, 300, 27000, 0)
    SetChrPos(0x104, 600, 300, 27600, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9572")

    #C0513
    ChrTalk(
        0xA,
        (
            "#5Pいらっしゃいませ。\x01",
            "クロスベル国際銀行へようこそ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0514
    ChrTalk(
        0xA,
        "#5Pあら、そちらは……\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xA,
        (
            "#5Pやはり、エリィ様でしたか！\x01",
            "お久しゅうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x101,
        "#11P#0005F（え……？）\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x103,
        "#12P#0205F（エリィさん……？）\x02",
    )

    CloseMessageWindow()

    def lambda_90BC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_90BC)

    def lambda_90C9():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_90C9)

    def lambda_90D6():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_90D6)
    Sleep(300)

    #C0518
    ChrTalk(
        0x102,
        (
            "#12P#0100Fこんにちは、ランフィさん。\x01",
            "お久し振りですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xA,
        (
            "#5Pこうしてお会いするのは\x01",
            "留学に向かわれるとき以来ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xA,
        (
            "#5P……そうですわ、\x01",
            "さっそくマリアベル様に\x01",
            "お知らせいたしましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xA,
        (
            "#5P丁度ミシュラムの視察に\x01",
            "お出掛けになりましたが、きっと\x01",
            "喜んでお戻りになると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x102,
        (
            "#12P#0104Fふふ……ベルも\x01",
            "相変わらず忙しそうね。\x02\x03",

            "#0100F構わないわ、今日はベルに\x01",
            "用事があったわけではないし。\x02\x03",

            "また日を改めて伺います。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xA,
        (
            "#5Pそうですか……\x01",
            "ではそうお伝えしておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_92D0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92D0)

    def lambda_92DD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_92DD)
    Sleep(300)

    #C0524
    ChrTalk(
        0x104,
        (
            "#12P#0305F（お嬢……ＩＢＣの人と\x01",
            "  知り合いだったのかよ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        (
            "#11P#0005F（それもかなり\x01",
            "  フレンドリーだ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x103,
        (
            "#12P#203F（ひそひそ、まさに\x01",
            "  お嬢様ですね……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    #C0527
    ChrTalk(
        0x102,
        "#6P#0113F……あの、聞こえてるのだけど。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0528
    ChrTalk(
        0x102,
        (
            "#6P#0100Fロイド、今日は\x01",
            "仕事で来たんじゃなかったの？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0529
    ChrTalk(
        0x101,
        (
            "#11P#0012Fあ、ああ、そうだった。\x01",
            "（ついうっかり……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9470():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9470)

    def lambda_947D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_947D)

    def lambda_948A():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_948A)

    def lambda_9497():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9497)
    Sleep(300)

    #C0530
    ChrTalk(
        0x101,
        (
            "#11P#0000F改めまして……\x01",
            "クロスベル警察、\x01",
            "特務支援課といいます。\x02\x03",

            "確かＩＢＣの方から\x01",
            "依頼をされたいとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xA,
        "#5Pあら、そちらのお話でしたか。\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xA,
        (
            "#5P申し訳ありません、\x01",
            "すぐにご説明致しますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 4)
    Jump("loc_96BC")

    label("loc_9572")


    #C0533
    ChrTalk(
        0xA,
        (
            "#5Pいらっしゃいませ。\x01",
            "クロスベル国際銀行へようこそ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0534
    ChrTalk(
        0xA,
        (
            "#5Pあらエリィ様、\x01",
            "それに特務支援課の方々も。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x102,
        (
            "#12P#0100Fランフィさん、\x01",
            "依頼を見てきたのだけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x101,
        (
            "#11P#0000Fえっと、ＩＢＣの方から\x01",
            "依頼をされたいとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xA,
        "#5Pあら、そちらのお話でしたか。\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xA,
        (
            "#5Pでは早速\x01",
            "ご説明させていただきますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96BC")


    #C0539
    ChrTalk(
        0x102,
        "#12P#0100Fええ、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xA,
        (
            "#5Pすでに経済誌などで\x01",
            "ご存知かもしれませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xA,
        (
            "#5PＩＢＣではこのたび\x01",
            "セピス換金に関する新サービスを\x01",
            "実施する予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xA,
        (
            "#5P具体的には、通常より高い換金率で\x01",
            "セピスをミラに換えさせていただく\x01",
            "サービスとなります。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x104,
        (
            "#12P#0300Fなるほど……\x01",
            "普通の店よりお得ってわけか。\x01",
            "そりゃ確かに便利そうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        (
            "#12P#0100F限りある七耀石資源に配慮し、\x01",
            "セピス貯蔵を積極的に行うのが\x01",
            "目的だそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x103,
        (
            "#12P#0204FさすがＩＢＣ……\x01",
            "地味ですが効果的なサービスかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xA,
        "#5Pふふ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xA,
        (
            "#5P──ただ、偽造セピスや\x01",
            "盗難などの問題があるため\x01",
            "会員限定にするつもりでして……\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xA,
        (
            "#5Pさらに導力端末を利用した\x01",
            "セピス貯蔵の管理も行う予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xA,
        (
            "#5Pそのテスト運用に\x01",
            "協力していただくというのが\x01",
            "今回お願いしたい内容となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        (
            "#11P#0000F判りました。\x01",
            "具体的にはどうすれば……？\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xA,
        (
            "#5Pはい、それではこちらの\x01",
            "カードをお受け取り下さい。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0552
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x35B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x35B, 1)

    #C0553
    ChrTalk(
        0xA,
        (
            "#5Pこちらを私の方に提示して\x01",
            "新サービスをご利用になってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xA,
        (
            "#5Pその上で、一定以上のセピスを\x01",
            "換金していただければと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xA,
        (
            "#5P具体的には、７種のセピスを各３０個、\x01",
            "それだけ試していただければ十分です。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x101,
        (
            "#11P#0002F各３０個ずつですね。\x01",
            "分かりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x104,
        "#12P#0309Fうっし、んじゃあ早速試してみるか。\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x102,
        (
            "#12P#0104Fええ、一度に換金する必要は\x01",
            "無いでしょうし……\x02\x03",

            "#0100F他の仕事の合間に\x01",
            "少しずつ試してみましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0559
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【新サービスの運用協力】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)

    #A0560
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＩＢＣの換金サービスが利用可能になりました。\x02",
        )
    )

    CloseMessageWindow()

    #A0561
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランフィに話しかけ、\x01",
            "『セピス換金』を選んだ後\x01",
            "<EXCHANGE>を選ぶと換金を行う事ができます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 300, 28800, 0)
    OP_4C(0xA, 0xFF)
    Sleep(500)
    OP_29(0x7, 0x1, 0x0)
    ClearScenarioFlags(0x49, 2)
    EventEnd(0x5)
    Return()

    # Function_21_8F4B end

    def Function_22_9D5D(): pass

    label("Function_22_9D5D")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(1000)
    OP_68(0, 1000, 30100, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 300, 28600, 0)
    SetChrPos(0x102, -1400, 300, 27300, 0)
    SetChrPos(0x103, -500, 300, 27000, 0)
    SetChrPos(0x104, 600, 300, 27600, 0)
    OP_0D()

    #C0562
    ChrTalk(
        0xA,
        "#5Pあら……\x02",
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xA,
        (
            "#5Pこれで７種のセピスを\x01",
            "３０個ずつ換金して\x01",
            "頂けたことになりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xA,
        "#5Pそれでは、少々お待ち下さい。\x02",
    )

    CloseMessageWindow()
    OP_92(0xA, 0x258, 0x7D00, 0x190)

    def lambda_9E6C():
        OP_95(0xFE, 600, 300, 32000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9E6C)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x190)
    Sleep(300)

    #C0565
    ChrTalk(
        0xA,
        (
            "#5Pこちら受付……\x01",
            "ただいまの換金で各３０ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xA,
        (
            "#5Pええ、ええ……\x01",
            "……はい、そうでしたか……\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xA,
        "#5P……はい、分かりました。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x190)

    def lambda_9F26():
        OP_95(0xFE, 0, 300, 31700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9F26)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0xB4, 0x190)

    #C0568
    ChrTalk(
        0xA,
        "#5P業務の方も確認が出来ました。\x02",
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xA,
        (
            "#5P一時、空のセピスと地のセピスを\x01",
            "間違えかけた社員がいたそうですが……\x01",
            "すぐに取り消しができたとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xA,
        (
            "#5P以降はある程度スムーズに\x01",
            "処理できたそうですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x104,
        (
            "#12P#0300Fはは、少しは\x01",
            "慣れたみたいッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x102,
        (
            "#12P#0104Fお役に立てたみたいで\x01",
            "良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xA,
        (
            "#5Pいえいえ、本当に\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xA,
        (
            "#5Pそうですわ、粗品ですが\x01",
            "どうかこちらをお受け取り下さい。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0575
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×３を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0576
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×２を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0577
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×２を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1F5, 3)
    AddItemNumber(0x1FB, 2)
    AddItemNumber(0x1F8, 2)

    #C0578
    ChrTalk(
        0x103,
        "#12P#0205Fさすが、太っ腹ですね。\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0xA,
        "#5Pふふ、それと……\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0xA,
        (
            "#5P皆さんにお渡ししたカードは\x01",
            "そのままお持ちになって結構ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xA,
        (
            "#5P皆さんには特別に\x01",
            "今後も換金サービスを\x01",
            "実施させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xA,
        (
            "#5Pご協力いただいた\x01",
            "謝礼の１つとお考え下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0583
    ChrTalk(
        0x101,
        (
            "#11P#0011Fいいんですか！？\x01",
            "それはさすがに太っ腹すぎな気が。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x104,
        (
            "#12P#0305F会員限定サービスが\x01",
            "こうも簡単に使えるとは……\x02\x03",

            "#0309Fお嬢のセレブパワーが\x01",
            "影響してるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x102,
        (
            "#12P#0109Fあはははは……\x01",
            "そ、それはないと思うけど。\x02\x03",

            "#0105F……ないですよね、ランフィさん？\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xA,
        "#5Pええ、もちろんです。\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xA,
        (
            "#5P皆さん、また必要なときは\x01",
            "いつでもいらしてくださいね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0588
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【新サービスの運用協力】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 300, 28800, 180)
    OP_4C(0xA, 0xFF)
    OP_29(0x7, 0x4, 0x10)
    OP_29(0x7, 0x1, 0x1)
    SetScenarioFlags(0x1, 1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_22_9D5D end

    def Function_23_A4EF(): pass

    label("Function_23_A4EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(220, 5800, 11750, 0)
    MoveCamera(16, 14, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 700, 300, 1650, 0)
    SetChrPos(0x102, -700, 300, 1650, 0)
    SetChrPos(0x103, -700, 300, 0, 0)
    SetChrPos(0x104, 700, 300, 0, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0x9, 0x8000)

    def lambda_A586():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A586)

    def lambda_A59B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A59B)

    def lambda_A5B0():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A5B0)

    def lambda_A5C5():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A5C5)
    OP_68(220, 1800, 11750, 4000)
    MoveCamera(16, 10, 0, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x3, 1)
    Sleep(300)
    Fade(800)
    OP_68(-90, 1800, 6110, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(16850, 0)
    OP_0D()

    #C0589
    ChrTalk(
        0x101,
        (
            "#11P#0000Fさてと……\x01",
            "ＩＢＣまで来たけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x104,
        (
            "#11P#0300F相変わらずすげー設備が\x01",
            "稼動中って感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x103,
        (
            "#11P#0200F家出した議員令嬢さんが\x01",
            "立ち寄っているはずですが……\x02\x03",

            "受付で聞いてみましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x102,
        (
            "#5P#0100Fええ、ランフィさんに\x01",
            "聞いてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 300, 4570, 0)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    OP_29(0x2D, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_23_A4EF end

    def Function_24_A765(): pass

    label("Function_24_A765")

    EventBegin(0x0)
    Fade(800)
    OP_4B(0xA, 0xFF)
    OP_68(0, 1200, 30100, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 300, 28600, 0)
    SetChrPos(0x102, -1400, 300, 27300, 0)
    SetChrPos(0x103, -500, 300, 27000, 0)
    SetChrPos(0x104, 600, 300, 27600, 0)
    OP_0D()

    #C0593
    ChrTalk(
        0xA,
        (
            "#5Pあらエリィ様、\x01",
            "何か御用でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x102,
        (
            "#12P#0100Fええ、ランフィさん。\x01",
            "問い合わせたいのだけれど……\x02\x03",

            "今日こちらに\x01",
            "カーラさんという方が\x01",
            "来なかったかしら。\x02\x03",

            "#0103Fメイドさんと\x01",
            "一緒だと思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xA,
        (
            "#5Pカーラ様……\x01",
            "ええ、先ほど来られましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xA,
        (
            "#5P急ぎの用件とかで、\x01",
            "マリアベル様にお会いになりたいと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0597
    ChrTalk(
        0x102,
        "#12P#0105Fベルに……？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xA,
        (
            "#5Pマリアベル様も\x01",
            "承諾なさいましたので\x01",
            "上の階へお通ししたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xA,
        (
            "#5P１時間ほど前に\x01",
            "帰られたようですけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそれでは……マリアベルさんに\x01",
            "詳しい話を伺ってもいいでしょうか。\x02\x03",

            "#0001F実は少し、捜査がらみの話でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xA,
        (
            "#5Pええ、今の時間なら\x01",
            "大丈夫だと思いますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0xA,
        (
            "#5P総裁室の方に\x01",
            "いらっしゃると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x103,
        "#12P#0200Fありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x104,
        "#12P#0300Fよし、行ってみようぜ。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -370, 300, 28210, 180)
    OP_4C(0xA, 0xFF)
    OP_29(0x2D, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_24_A765 end

    def Function_25_AB42(): pass

    label("Function_25_AB42")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 500)

    #C0605
    ChrTalk(
        0x8,
        (
            "おっと、ここから先は\x01",
            "スタッフ専用のフロアだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x8,
        (
            "許可がない者を\x01",
            "入れるわけにはいかないぞ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 6280, 0, 15970, 270)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_25_AB42 end

    SaveToFile()

Try(main)
