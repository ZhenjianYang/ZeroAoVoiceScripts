from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t052b.bin",                # FileName
        "t052b",                    # MapName
        "t052b",                    # Location
        0x003F,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 63, 0, 2, 0, 3],
    )

    BuildStringList((
        "t052b",                  # 0
        "ノーマ",                 # 1
        "リュッカ",               # 2
        "カルロス",               # 3
        "鉱員マルロ",             # 4
        "鉱員ガンツ",             # 5
        "フリージア",             # 6
        "レティナ",               # 7
    ))

    AddCharChip((
        "chr/ch23500.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch23602.itc",                   # 02
        "chr/ch26202.itc",                   # 03
        "chr/ch33300.itc",                   # 04
        "chr/ch34500.itc",                   # 05
        "chr/ch30702.itc",                   # 06
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

    DeclNpc(3700,    0,       4289,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4880,   -750,    -860,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-6130,   -600,    4219,    270,  469,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-9359,   -600,    -1110,   180,  469,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-8659,   -600,    -4480,   0,    469,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(204009,  0,       560,     270,  389,  0x0, 0,   4,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(199529,  0,       3160,    225,  389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)

    DeclActor(3700,    0,       2920,    1000,    3700,    1500,    4290,    0x007E, 0,  4,  0x0000)
    DeclActor(102600,  2000,    1500,    2000,    102600,  3200,    1500,    0x007C, 0,  12, 0x0000)

    ScpFunction((
        "Function_0_250",          # 00, 0
        "Function_1_308",          # 01, 1
        "Function_2_333",          # 02, 2
        "Function_3_41B",          # 03, 3
        "Function_4_432",          # 04, 4
        "Function_5_436",          # 05, 5
        "Function_6_71B",          # 06, 6
        "Function_7_7DA",          # 07, 7
        "Function_8_9F2",          # 08, 8
        "Function_9_B3D",          # 09, 9
        "Function_10_C9C",         # 0A, 10
        "Function_11_E1D",         # 0B, 11
        "Function_12_F03",         # 0C, 12
        "Function_13_11C3",        # 0D, 13
    ))


    def Function_0_250(): pass

    label("Function_0_250")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_290"),
        (1, "loc_29C"),
        (2, "loc_2A8"),
        (3, "loc_2B4"),
        (4, "loc_2C0"),
        (5, "loc_2CC"),
        (6, "loc_2D8"),
        (SWITCH_DEFAULT, "loc_2E4"),
    )


    label("loc_290")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_29C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2A8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2B4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2C0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2CC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_307")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_307")

    Return()

    # Function_0_250 end

    def Function_1_308(): pass

    label("Function_1_308")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_332")
    OP_94(0xFE, 0x31678, 0xFFFFFF1A, 0x321B8, 0x3DE, 0x3E8)
    Sleep(300)
    Jump("Function_1_308")

    label("loc_332")

    Return()

    # Function_1_308 end

    def Function_2_333(): pass

    label("Function_2_333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_341")
    Jump("loc_40B")

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_34F")
    Jump("loc_40B")

    label("loc_34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_35D")
    Jump("loc_40B")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_36B")
    Jump("loc_40B")

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_379")
    Jump("loc_40B")

    label("loc_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_387")
    Jump("loc_40B")

    label("loc_387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_395")
    Jump("loc_40B")

    label("loc_395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3A3")
    Jump("loc_40B")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3B1")
    Jump("loc_40B")

    label("loc_3B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3BF")
    Jump("loc_40B")

    label("loc_3BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3CD")
    Jump("loc_40B")

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_3F4")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_40B")

    label("loc_3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_402")
    Jump("loc_40B")

    label("loc_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_40B")

    label("loc_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_41A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_41A")

    Return()

    # Function_2_333 end

    def Function_3_41B(): pass

    label("Function_3_41B")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_431")
    OP_66(0x1, 0x1)

    label("loc_431")

    Return()

    # Function_3_41B end

    def Function_4_432(): pass

    label("Function_4_432")

    Call(0, 5)
    Return()

    # Function_4_432 end

    def Function_5_436(): pass

    label("Function_5_436")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_443")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_717")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "休憩をする\x01",        # 2
            "やめる\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D6")
    OP_AF(0x52)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_712")

    label("loc_4D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F6")
    OP_AF(0x50)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_712")

    label("loc_4F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50A")
    Jump("loc_712")

    label("loc_50A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_712")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D")

    #C0001
    ChrTalk(
        0x8,
        (
            "ふふ、どうだいあの部屋は。\x01",
            "広くてなかなかいいだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "あんたたちみたいな若い子が\x01",
            "ウチに泊まってくれるなんてことは\x01",
            "なかなか無いからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        "……おっと、出かける所かい？\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "最近物騒だし、\x01",
            "遅くならないうちに帰るんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_712")

    label("loc_61D")


    #C0005
    ChrTalk(
        0x8,
        (
            "いつも酒場は鉱員たちで\x01",
            "騒がしいくらいなんだけど、\x01",
            "今日はお客が少ないほうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "やれやれ、とんだとばっちりだよ。\x01",
            "マックスさんが怪我したばかりだから\x01",
            "しょうがないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "狼型魔獣だかなんだか知らないが、\x01",
            "いい加減にしてほしいもんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_712")

    Jump("loc_443")

    label("loc_717")

    TalkEnd(0x8)
    Return()

    # Function_5_436 end

    def Function_6_71B(): pass

    label("Function_6_71B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79F")

    #C0008
    ChrTalk(
        0xFE,
        (
            "……やれやれ、\x01",
            "毎日毎日酒盛りなんて\x01",
            "懲りないもんだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "仕事が終わったんなら\x01",
            "さっさと帰ればいいのに。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_7D6")

    label("loc_79F")


    #C0010
    ChrTalk(
        0xFE,
        (
            "しかし、ガンツさんは\x01",
            "いつもながら酒癖悪いわね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D6")

    TalkEnd(0xFE)
    Return()

    # Function_6_71B end

    def Function_7_7DA(): pass

    label("Function_7_7DA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_86E")
    Jump("loc_8B8")

    label("loc_86E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_88E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8")

    label("loc_88E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8")

    label("loc_8AE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97A")

    #C0011
    ChrTalk(
        0xFE,
        (
            "うーん……\x01",
            "やっぱりお酒はいいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "一日の疲れが\x01",
            "どっと抜けていくようだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "ただ、あまり飲みすぎるのは\x01",
            "良くないと思うけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_9EA")

    label("loc_97A")


    #C0014
    ChrTalk(
        0xFE,
        (
            "鉱員の彼らも\x01",
            "うっ憤がたまってるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "おいしくお酒を飲んで、\x01",
            "明日への活力としてほしいものだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_7DA end

    def Function_8_9F2(): pass

    label("Function_8_9F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB2")

    #C0016
    ChrTalk(
        0xB,
        "ぐびぐび……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        (
            "……くぅ～！\x01",
            "仕事終わりの一杯は格別だな！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xB,
        (
            "っと、あまり飲みすぎないように\x01",
            "気をつけないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "ガンツのやつは\x01",
            "すぐベロベロになっちまうからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_B39")

    label("loc_AB2")


    #C0020
    ChrTalk(
        0xB,
        (
            "ガンツのやつは\x01",
            "すぐベロベロになっちまうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xB,
        (
            "俺まで酔っ払っちまったら\x01",
            "こいつ家に帰れなくなるし……\x01",
            "はぁ、損な役回りだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B39")

    TalkEnd(0xFE)
    Return()

    # Function_8_9F2 end

    def Function_9_B3D(): pass

    label("Function_9_B3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C16")

    #C0022
    ChrTalk(
        0xC,
        (
            "俺はよぉ……\x01",
            "カジノで一山あててよぉ……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xC,
        "この先の人生をラクにだなぁ……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xC,
        (
            "うぃ～ッ……\x01",
            "……おい、聞いてんのかぁ、マルロ？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xB,
        "聞いてる聞いてる。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        "ったく、何回同じこと言ってんだ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_C98")

    label("loc_C16")


    #C0027
    ChrTalk(
        0xC,
        "うぃ～ッ……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xC,
        (
            "俺はよぉ……\x01",
            "今週こそカジノで一山あててよぉ……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xB,
        (
            "……はぁ、帰る前に\x01",
            "ちっと酔いを冷ましてやんないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C98")

    TalkEnd(0xFE)
    Return()

    # Function_9_B3D end

    def Function_10_C9C(): pass

    label("Function_10_C9C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7A")

    #C0030
    ChrTalk(
        0xFE,
        (
            "お向かいの部屋、\x01",
            "あなた達が借りたのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "私も広い部屋がよかったけど\x01",
            "２人で４人部屋は\x01",
            "ダメって言われちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "あの女将、なかなかやるわね。\x01",
            "ワガママが通らなかったのは\x01",
            "久しぶりだわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_E19")

    label("loc_D7A")


    #C0033
    ChrTalk(
        0xFE,
        (
            "ま、こっちは二人だし……\x01",
            "当分この部屋で我慢するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "それより、明日はまた\x01",
            "町長と交渉しなければね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "七耀石の結晶……\x01",
            "明日こそ手に入れてみせるわ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E19")

    TalkEnd(0xFE)
    Return()

    # Function_10_C9C end

    def Function_11_E1D(): pass

    label("Function_11_E1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAB")

    #C0036
    ChrTalk(
        0xFE,
        (
            "あ……食器をお店の方に\x01",
            "返しに行かないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "ふぅ……\x01",
            "お嬢様が部屋で食べたいなんて\x01",
            "わがままを言ったばっかりに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_EFF")

    label("loc_EAB")


    #C0038
    ChrTalk(
        0xFE,
        (
            "食事を部屋まで持ってくるのは\x01",
            "大丈夫でしたけど……\x01",
            "返す時に転ばないか心配です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFF")

    TalkEnd(0xFE)
    Return()

    # Function_11_E1D end

    def Function_12_F03(): pass

    label("Function_12_F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11C2")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【深夜まで待機する】\x01",        # 0
            "【まだ他に用事がある】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F79"),
        (1, "loc_10EC"),
        (SWITCH_DEFAULT, "loc_11C0"),
    )


    label("loc_F79")


    #C0039
    ChrTalk(
        0x101,
        (
            "#0003Fそれじゃあ一旦、\x01",
            "ここで真夜中まで待機しよう。\x02\x03",

            "#0001F魔獣が現れた時の\x01",
            "段取りと配置も決めないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x103,
        (
            "#0201Fただ魔獣を撃退するだけでは\x01",
            "駄目ということですね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#0103Fええ、魔獣を操っている\x01",
            "マフィアたちの方も抑えないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#0302Fヘッ、なかなか難易度の高い\x01",
            "ミッションになりそうだぜ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_65(0x2, 0x1)
    SetScenarioFlags(0x5C, 0)
    NewScene("t050B", 0, 0, 0)
    IdleLoop()
    Jump("loc_11C0")

    label("loc_10EC")


    #C0043
    ChrTalk(
        0x104,
        (
            "#0300Fそんじゃ、準備を済ませたら\x01",
            "ここに戻ってくるとすっか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "部屋で深夜まで待機する場合は\x01",
            "テーブルの上に！マークが出た状態で\x01",
            "○ボタンを押してください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_11C0")

    label("loc_11C0")

    EventEnd(0x3)

    label("loc_11C2")

    Return()

    # Function_12_F03 end

    def Function_13_11C3(): pass

    label("Function_13_11C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50111.itc", 0x22)
    OP_68(102070, 4500, 1190, 0)
    MoveCamera(58, 19, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(32299, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 102700, 2200, 3100, 180)
    SetChrPos(0x102, 102500, 2200, -300, 0)
    SetChrPos(0x103, 101200, 2200, 1700, 90)
    SetChrPos(0x104, 104400, 2200, 1300, 270)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis021.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis022.itp")
    FadeToBright(1000, 0)
    OP_68(102370, 3300, 1380, 4000)
    OP_6F(0x1)
    OP_0D()

    #C0045
    ChrTalk(
        0x101,
        (
            "#0003F#5P──さて。\x01",
            "状況の整理を始めよう。\x02\x03",

            "#0001F今回の一連の魔獣被害だけど……\x01",
            "最初の警備隊の調書には\x01",
            "幾つもの不明点があった。\x02\x03",

            "俺たちの調査で、その不明点の\x01",
            "幾つかが明らかになったけど……\x02\x03",

            "#0003F本当なら判明しているはずの\x01",
            "ある情報がまだ判っていないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0105F#12P判明しているはずの情報……？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        "#0305F#11Pなんだ、そいつは？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K本来判明しているはずの情報とは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【魔獣の正体】\x01",      # 0
            "【魔獣の住処】\x01",      # 1
            "【魔獣の目的】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1504"),
        (1, "loc_161A"),
        (2, "loc_1752"),
        (SWITCH_DEFAULT, "loc_17C9"),
    )


    label("loc_1504")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0049
    ChrTalk(
        0x101,
        (
            "#0006F#5P魔獣の正体……\x01",
            "って言いたいところだけど。\x02\x03",

            "#0008F相手が神出鬼没な以上、\x01",
            "さすがに無理があるんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        (
            "#0206F#6Pまあ、それが判れば\x01",
            "苦労はしませんよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#0003F#5P……そうだな。\x01",
            "あえて言うとしたら。\x02\x03",

            "#0001F魔獣の目的、じゃないかと思う。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C9")

    label("loc_161A")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0052
    ChrTalk(
        0x101,
        (
            "#0006F#5P魔獣の住処……\x01",
            "って言いたいところだけど。\x02\x03",

            "#0008F警備隊の山狩りで見つかってないのに\x01",
            "俺たちが見つけられる訳がないんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        (
            "#0206F#6Pまあ、本格的に山狩りができる\x01",
            "人数でもありませんし……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#0003F#5P……そうだな。\x01",
            "あえて言うとしたら。\x02\x03",

            "#0001F魔獣の目的、じゃないかと思う。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C9")

    label("loc_1752")

    OP_2C(0x3F, 0x3)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0055
    ChrTalk(
        0x101,
        (
            "#0003F#5Pそう、一連の調査で\x01",
            "本来判明しているはずの情報……\x02\x03",

            "#0001Fそれは魔獣の目的、だと思う。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C9")

    label("loc_17C9")


    #C0056
    ChrTalk(
        0x104,
        (
            "#0303F#11Pそういや……\x02\x03",

            "#0301F病院の被害を考えると\x01",
            "飢えて各地を襲ったって訳じゃ\x01",
            "なさそうなんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#0108F#12Pアルモリカ村の村長さんによれば\x01",
            "伝承にある《神狼》が警告している\x01",
            "可能性もあるという事だけど……\x02\x03",

            "#0101Fでも、実際に各地を襲ったのは\x01",
            "黒い狼たちの可能性が高いのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#0203F#6Pはい……そうだと思います。\x02\x03",

            "#0201Fそうなると、確かに目的が\x01",
            "まったく判らなくなりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#0003F#5Pああ……\x02\x03",

            "#0001Fだが、ここで黒い狼たちの\x01",
            "気まぐれと判断するのは早すぎる。\x02\x03",

            "病院での一件を考えれば判るけど\x01",
            "彼らは非常に巧妙なルートを使って\x01",
            "病棟の屋上に侵入している。\x02\x03",

            "#0003Fそして被害者を必要以上に\x01",
            "害することなく去っていった……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#0103F#12P確かに……\x02\x03",

            "#0101Fただの気まぐれというには\x01",
            "周到すぎるかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#0303F#11P本来見えてくるべき\x01",
            "目的がまったく見えて来ない……\x02\x03",

            "#0300Fつまりそこに\x01",
            "何か意味があるってわけだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#0000F#5Pそういう事。\x02\x03",

            "#0003Fこんな場合、\x01",
            "人は大抵、一つの《枠組み》に\x01",
            "囚われている場合が多いんだ。\x02\x03",

            "黒い狼たちによる各地の襲撃……\x02\x03",

            "#0001Fそこに納得のいく目的を見出せる\x01",
            "別の《枠組み》を考えるべきだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        "#0208F#6P別の《枠組み》……ですか。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0064
    ChrTalk(
        0x101,
        (
            "#0000F#5P難しく考えることはないよ。\x02\x03",

            "#0004Fおよそ犯罪事件と呼べるものは\x01",
            "『犯人』『目的』『手段』『結果』が\x01",
            "あるものだけど……\x02\x03",

            "#0000Fそのうちの幾つかが、\x01",
            "ズレていると考えたらどうだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        "#0205F#6Pえ……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#0101F#12Pちょ、ちょっと待って。\x01",
            "簡単にまとめてみるから。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "犯人　＝　黒い狼たち\x01",
            "目的　＝　？\x01",
            "手段　＝　狼の身体能力\x01",
            "結果　＝　各地の被害\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    #C0068
    ChrTalk(
        0x101,
        "#0000F#5Pうん、そんな所だろうな。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0301F#11Pそれで……\x01",
            "こいつがどうズレてるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#0001F#5Pああ……\x01",
            "こうしてみたらどうだ？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 5)

    label("loc_1E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2208")
    SetScenarioFlags(0x0, 5)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K『犯人』に相当するのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "黒い狼たち\x01",        # 0
            "？\x01",                # 1
            "狼の身体能力\x01",      # 2
            "各地の被害\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ED9")
    ClearScenarioFlags(0x0, 5)

    label("loc_1ED9")

    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K『目的』に相当するのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "黒い狼たち\x01",        # 0
            "？\x01",                # 1
            "狼の身体能力\x01",      # 2
            "各地の被害\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F54")
    ClearScenarioFlags(0x0, 5)

    label("loc_1F54")

    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K『手段』に相当するのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "黒い狼たち\x01",        # 0
            "？\x01",                # 1
            "狼の身体能力\x01",      # 2
            "各地の被害\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FCF")
    ClearScenarioFlags(0x0, 5)

    label("loc_1FCF")

    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K『結果』に相当するのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "黒い狼たち\x01",        # 0
            "？\x01",                # 1
            "狼の身体能力\x01",      # 2
            "各地の被害\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_204A")
    ClearScenarioFlags(0x0, 5)

    label("loc_204A")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_210E")
    OP_63(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0075
    ChrTalk(
        0x101,
        (
            "#0006F#5P（うーん……\x01",
            "  やっぱり辻褄が合わない。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)

    #C0076
    ChrTalk(
        0x101,
        "#0005F#5P（もしかして、これか……？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2178")

    label("loc_210E")


    #C0077
    ChrTalk(
        0x101,
        (
            "#0003F#5P（いや……\x01",
            "  これだと辻褄が合わない。）\x02\x03",

            "#0001F（もう一度選び直してみよう。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2178")

    Jump("loc_2203")

    label("loc_217D")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_218D"),
        (SWITCH_DEFAULT, "loc_21C9"),
    )


    label("loc_218D")

    OP_2C(0x3F, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0078
    ChrTalk(
        0x101,
        "#0000F#5P（間違いない……これだ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2203")

    label("loc_21C9")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0079
    ChrTalk(
        0x101,
        "#0003F#5P（……多分、これだな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2203")

    label("loc_2203")

    Jump("loc_1E46")

    label("loc_2208")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0080
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "犯人　＝　？\x01",
            "目的　＝　狼の身体能力\x01",
            "手段　＝　黒い狼たち\x01",
            "結果　＝　各地の被害\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x102,
        "#0105F#12Pこれは……！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        (
            "#0201F#6P仮にこうした場合……\x02\x03",

            "犯人は別にいて、黒い狼たちが手段で\x01",
            "彼らの身体能力が目的になる……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0305F#11Pおいおい……\x01",
            "完全に見方が変わったな！\x02\x03",

            "#0301Fって事は、狼どもの背後に\x01",
            "人間がいる可能性があるわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#0003F#5P魔獣を操ることが出来るなら\x01",
            "そう考えるのがむしろ自然だろう。\x02\x03",

            "#0008F問題は、複数の狼型魔獣を連れて\x01",
            "コントロールする方法だけど……\x02\x03",

            "#0000Fこのうち、コントロールする方法は\x01",
            "ある人物の証言から推測できると思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#0101F#12Pある人物の証言……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0086
    ChrTalk(
        0x104,
        "#0300F#11P……なるほど、あれだな？\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0004F#5Pさすがにランディは気付くか。\x02\x03",

            "#0000Fうん、その証言者は……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K証言者の名前は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【ハロルド・ヘイワース】\x01",      # 0
            "【リットン研修医】\x01",            # 1
            "【シズク・マクレイン】\x01",        # 2
            "【ノエル・シーカー】\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2625"),
        (1, "loc_26D3"),
        (2, "loc_2781"),
        (3, "loc_27E8"),
        (SWITCH_DEFAULT, "loc_2896"),
    )


    label("loc_2625")


    #C0089
    ChrTalk(
        0x104,
        (
            "#0303F#11Pいや……違うだろ？\x02\x03",

            "#0301Fあの目が見えない\x01",
            "シズクって子じゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#0011F#5Pあ……そうだった。\x02\x03",

            "#0006F具体的な証言をしてくれたのは\x01",
            "あの子だったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2896")

    label("loc_26D3")


    #C0091
    ChrTalk(
        0x104,
        (
            "#0303F#11Pいや……違うだろ？\x02\x03",

            "#0301Fあの目が見えない\x01",
            "シズクって子じゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#0011F#5Pあ……そうだった。\x02\x03",

            "#0006F具体的な証言をしてくれたのは\x01",
            "あの子だったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2896")

    label("loc_2781")

    OP_2C(0x3F, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0093
    ChrTalk(
        0x101,
        (
            "#0003F#5Pシズク・マクレイン……\x02\x03",

            "#0001Fあの遊撃士アリオスの\x01",
            "娘さんの証言だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2896")

    label("loc_27E8")


    #C0094
    ChrTalk(
        0x104,
        (
            "#0303F#11Pいや……違うだろ？\x02\x03",

            "#0301Fあの目が見えない\x01",
            "シズクって子じゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#0011F#5Pあ……そうだった。\x02\x03",

            "#0006F具体的な証言をしてくれたのは\x01",
            "あの子だったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2896")

    label("loc_2896")


    #C0096
    ChrTalk(
        0x103,
        "#0205F#6Pシズクさんの証言……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(40, 120, -1, -1)
    SetChrName("シズクの証言")

    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "その、気になったので\x01",
            "そこの窓を開けて\x01",
            "耳を澄ませたんですけど……\x02\x03",

            "それ以上、悲鳴は聞こえなくて\x01",
            "代わりにハッハッハッって\x01",
            "息づかいみたいな音が聞こえて……\x02\x03",

            "しばらくしたらタンタンって\x01",
            "何かはねるような音が聞こえて……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetMessageWindowPos(190, 140, -1, -1)
    SetChrName("シズクの証言")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "そ、それと……\x02\x03",

            "その……さっき話した音が\x01",
            "聞こえてる最中なんですけど……\x02\x03",

            "なにか……\x01",
            "キーンってかすれた音が\x01",
            "聞こえたような気がしたんです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis023.itp")

    #C0099
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0105F#12Pも、もしかして……\x01",
            "その音で魔獣を操っていたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#0001F#5Pああ、その可能性が高いだろう。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#0203F#6P……狼や犬のような獣は\x01",
            "人には聞こえない周波数の音を\x01",
            "聞き取ることができるそうです。\x02\x03",

            "#0201Fそれを利用した特殊な笛が\x01",
            "昔からあるらしいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#0304F#11Pいわゆる『犬笛』だな。\x02\x03",

            "#0300F今でも軍用犬なんかを\x01",
            "犬笛で操る技術は残っているぜ。\x02\x03",

            "#0306Fまあ、まともな正規軍よりは\x01",
            "猟兵どもがよく使うんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#0005F#5Pそうなのか……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        (
            "#0108F#12P……なるほど。\x01",
            "かなり輪郭が見えて来たかも。\x02\x03",

            "#0101Fそうなると、魔獣を連れて\x01",
            "移動する手段が必要になるわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0105
    ChrTalk(
        0x102,
        "#0105F#12P……もしかして。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 3)), scpexpr(EXPR_END)), "loc_3411")
    OP_2C(0x3F, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x40, 0x1, 0xB)

    #C0106
    ChrTalk(
        0x101,
        (
            "#0004F#5Pああ、多分エリィの想像通りだ。\x02\x03",

            "#0000Fそれを裏付けることも\x01",
            "ひょっとしたら出来ると思う。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0107
    ChrTalk(
        0x101,
        (
            "#0000F#5P──ティオ、エニグマの\x01",
            "通信機能はこの町でも使えるかな？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(200)

    #C0108
    ChrTalk(
        0x103,
        (
            "#0205F#6Pええ、自治州内なら\x01",
            "何とかぎりぎり通じるかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        "#0305F#11Pなんだ、どこに連絡するんだ？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0110
    ChrTalk(
        0x101,
        "#0000F#5Pああ……医科大学の受付さ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x10)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 101060, 2000, -560, 180)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x103, 0x2)
    SetChrSubChip(0x104, 0x1)
    Sleep(1000)
    OP_68(102370, 4500, 1380, 0)
    OP_68(102370, 3300, 1380, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0111
    ChrTalk(
        0x102,
        (
            "#0101F#5Pはい……はい……\x02\x03",

            "#0105F！！\x02\x03",

            "#0103Fそうでしたか……\x01",
            "ええ、ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x102, 0x10)
    Sound(807, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0112
    ChrTalk(
        0x101,
        "#0001F#5Pどうだった？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0113
    ChrTalk(
        0x102,
        (
            "#0106F#11P……貴方の読み通りよ。\x02\x03",

            "#0101F魔獣が屋上に現れた夜、\x01",
            "《ルバーチェ商会》の運搬車が\x01",
            "駐車場に停まっていたらしいわ。\x02\x03",

            "どうやら病院で使う備品なんかを\x01",
            "高値で押し売りに来てたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        "#0306F#5Pさすがにタイミング良すぎだな。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    #C0115
    ChrTalk(
        0x104,
        (
            "#0301F#11Pしかしロイド……\x01",
            "何で連中の運搬車が駐車場に\x01",
            "停まってたって分かったんだ？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)

    #C0116
    ChrTalk(
        0x103,
        (
            "#0205F#6P深夜、病院の手前に車で来て\x01",
            "襲撃させた可能性もありますよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0003F#5Pいや、それだとシズクちゃんが\x01",
            "車の音を聞いているはずだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)

    #A0118
    AnonymousTalk(
        0x101,
        (
            "#0000Fそれに最初は\x01",
            "魔獣たちが入ってきたのが\x01",
            "草むらの方かと思ったんだけど……\x02\x03",

            "あそこにあった木箱の上に\x01",
            "魔獣の足跡が付いてなくてね。\x02\x03",

            "#0003F逆に、駐車場に面した\x01",
            "手すりの上が擦れていたんだ。\x02\x03",

            "#0001Fそこから入ってきた可能性が\x01",
            "高いんじゃないかと思ってさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0119
    AnonymousTalk(
        0x102,
        (
            "#0106Fなるほど……\x02\x03",

            "#0101F駐車場の方向は高さがあったから\x01",
            "入って来られないと思ってたけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(500)

    #A0120
    AnonymousTalk(
        0x104,
        (
            "#0300Fこう、運搬車の上を行かせれば\x01",
            "余裕で侵入できるってわけだな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0121
    AnonymousTalk(
        0x103,
        "#0206F……用意周到ですね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 102500, 2200, -300, 0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Jump("loc_348E")

    label("loc_3411")

    OP_29(0x40, 0x1, 0xC)

    #C0122
    ChrTalk(
        0x101,
        (
            "#0003F#5Pああ……\x01",
            "さっき見かけた黒い運搬車。\x02\x03",

            "#0001F断定は出来ないけど、あれなんか、\x01",
            "まさに打ってつけじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_348E")

    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x102)

    #C0123
    ChrTalk(
        0x103,
        "#0203F#6P……繋がりましたね、色々と。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#0108F#12Pええ、目的は\x01",
            "七耀石#6Rセプチウム#の取引の独占……\x02\x03",

            "#0101Fいえ、むしろそれはオマケね？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#0006F#5Pああ、多分ね。\x02\x03",

            "#0008Fマフィアが今力を入れているのは\x01",
            "対抗組織である《黒月#4Rヘイユエ#》を\x01",
            "圧倒できる戦力を手に入れること。\x02\x03",

            "#0001Fそのための戦力として\x01",
            "狼たちを使うつもりだとすれば……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#0303F#11P暴れるしか出来ない魔獣は\x01",
            "戦力としては全く使えない……\x02\x03",

            "十分、コントロールできるかを\x01",
            "実際にテストする必要がある……\x02\x03",

            "#0301Fそれが各地で起きていた\x01",
            "被害の真相だったってわけか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#0003F#5Pああ……間違いない。\x02\x03",

            "#0001Fそもそも警備隊が引き上げた直後に\x01",
            "マフィアの手下が訪れたこと自体、\x01",
            "不自然極まりないだろう。\x02\x03",

            "引き上げを命じた警備隊司令は\x01",
            "有力議員と繋がっているらしいし……\x02\x03",

            "多分、その議員を通じて\x01",
            "根回しが行われたんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x102,
        (
            "#0106F#12P多分……そうでしょうね。\x02\x03",

            "#0108F……腐っているとは思ってたけど\x01",
            "そこまでだったなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    #C0129
    ChrTalk(
        0x102,
        (
            "#0101F#12P……それで……\x01",
            "彼らはこれ以上、続けると思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#0006F#5P魔獣の実戦テストという意味では\x01",
            "もう十分なんだろう。\x02\x03",

            "警備隊を引き上げさせたということは\x01",
            "これ以上、騒ぎを起こす気がないという\x01",
            "裏返しでもある気がする。\x02\x03",

            "#0001Fただ……\x01",
            "どうやら今回動いている連中は\x01",
            "余計な色気を出しているみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        (
            "#0201F#6P七耀石の独占取引ですね……\x02\x03",

            "すると……\x01",
            "最後にもう一度だけ動くと？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x104,
        (
            "#0301F#11P連中の態度を見る限り\x01",
            "その可能性は高そうだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        "#0101F#12P襲撃があるとすれば、いつ？\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#0003F#5Pそうだな……\x02\x03",

            "#0008F……明日になれば町長が\x01",
            "ギルドに相談する可能性もある。\x02\x03",

            "#0001F最後の脅しをかけるとしたら\x01",
            "多分、今夜以外にはありえない。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x102)

    #C0135
    ChrTalk(
        0x104,
        "#0300F#11P──よし、やるか。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x103,
        (
            "#0201F#6P黒い狼たちの撃退と\x01",
            "マフィアたちの拘束ですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        (
            "#0103F#12Pええ……\x01",
            "さすがに見過ごせないわ。\x02\x03",

            "#0101F警備隊の方には\x01",
            "連絡した方がいいのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#0006F#5P……いや。\x01",
            "警備隊が動けば議員を通じて\x01",
            "マフィアに感付かれる恐れがある。\x02\x03",

            "#0001F俺たちだけで何とかしてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x102,
        (
            "#0103F#12P……分かった。\x02\x03",

            "#0101F魔獣が現れるとしたら\x01",
            "多分、深夜になってからよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x103,
        (
            "#0203F#6Pはい……今までの事件も\x01",
            "全て深夜に起こっていました。\x02\x03",

            "#0200Fまだ時間がありますが……\x01",
            "一通り、準備を整えますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0000F#5Pそうだな……\x01",
            "足りないものがあったら\x01",
            "補充くらいはしておこう。\x02\x03",

            "準備が済みしだい、\x01",
            "この部屋で真夜中まで待機だ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(32800, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(500)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0142
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "部屋で深夜まで待機する場合は\x01",
            "テーブルの上に！マークが出た状態で\x01",
            "○ボタンを押してください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    SetChrPos(0x0, 101300, 2000, 3700, 180)
    OP_66(0x1, 0x1)
    SetScenarioFlags(0x65, 5)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayBGM("ed7513", 0)
    EventEnd(0x5)
    Return()

    # Function_13_11C3 end

    SaveToFile()

Try(main)
