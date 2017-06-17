from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0520.bin",                # FileName
        "t0520",                    # MapName
        "t0520",                    # Location
        0x003F,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 63, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0520",                  # 0
        "ノーマ",                 # 1
        "リュッカ",               # 2
        "鉱員ロージー",           # 3
        "フリージア",             # 4
        "レティナ",               # 5
        "エステル",               # 6
        "ヨシュア",               # 7
        "遊撃士スコット",         # 8
        "遊撃士ヴェンツェル",     # 9
        "観光客ウォレンス",       # 10
    ))

    AddCharChip((
        "chr/ch23500.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "apl/ch50130.itc",                   # 04
        "chr/ch33300.itc",                   # 05
        "chr/ch34500.itc",                   # 06
        "chr/ch00602.itc",                   # 07
        "chr/ch00702.itc",                   # 08
        "chr/ch27202.itc",                   # 09
        "chr/ch27302.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch24402.itc",                   # 0C
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
    DeclNpc(147360,  500,     4599,    0,    469,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(204809,  0,       560,     270,  261,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(203350,  0,       560,     90,   261,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-7530,   -600,    -3140,   270,  469,  0x0, 0,   7,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-8640,   -600,    -4380,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-6199,   -600,    4199,    270,  469,  0x0, 0,   9,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-9289,   -600,    3869,    90,   469,  0x0, 0,   10,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-9510,   -600,    -1200,   180,  405,  0x0, 0,   12,  0,   255, 255, 0,   15,  255,  0)

    DeclActor(3700,    0,       2920,    1000,    3700,    1500,    4290,    0x007E, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_290",          # 00, 0
        "Function_1_348",          # 01, 1
        "Function_2_373",          # 02, 2
        "Function_3_573",          # 03, 3
        "Function_4_5B2",          # 04, 4
        "Function_5_5B6",          # 05, 5
        "Function_6_1453",         # 06, 6
        "Function_7_1E45",         # 07, 7
        "Function_8_1EC7",         # 08, 8
        "Function_9_27D5",         # 09, 9
        "Function_10_301C",        # 0A, 10
        "Function_11_323E",        # 0B, 11
        "Function_12_34FD",        # 0C, 12
        "Function_13_368C",        # 0D, 13
        "Function_14_3917",        # 0E, 14
        "Function_15_3B6A",        # 0F, 15
        "Function_16_3D33",        # 10, 16
        "Function_17_4002",        # 11, 17
    ))


    def Function_0_290(): pass

    label("Function_0_290")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2D0"),
        (1, "loc_2DC"),
        (2, "loc_2E8"),
        (3, "loc_2F4"),
        (4, "loc_300"),
        (5, "loc_30C"),
        (6, "loc_318"),
        (SWITCH_DEFAULT, "loc_324"),
    )


    label("loc_2D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_2DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_2E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_2F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_300")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_30C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_318")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_324")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_330")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_347")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_330")

    label("loc_347")

    Return()

    # Function_0_290 end

    def Function_1_348(): pass

    label("Function_1_348")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_372")
    OP_94(0xFE, 0x31678, 0xFFFFFF1A, 0x321B8, 0x3DE, 0x3E8)
    Sleep(300)
    Jump("Function_1_348")

    label("loc_372")

    Return()

    # Function_1_348 end

    def Function_2_373(): pass

    label("Function_2_373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_38B")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_38B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A3")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_3BB")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3D3")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3EB")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_55F")

    label("loc_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_421")
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    Jump("loc_55F")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_457")
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    Jump("loc_55F")

    label("loc_457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_48D")
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    Jump("loc_55F")

    label("loc_48D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4C8")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    Jump("loc_55F")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4F5")
    SetChrPos(0x9, 10680, 0, -830, 90)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)

    label("loc_4F5")

    Jump("loc_55F")

    label("loc_4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_53A")
    SetChrPos(0xB, 204010, 0, 560, 270)
    BeginChrThread(0xB, 0, 0, 1)
    SetChrPos(0xC, 199530, 0, 3160, 225)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_55F")

    label("loc_53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_548")
    Jump("loc_55F")

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_556")
    Jump("loc_55F")

    label("loc_556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_55F")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_572")
    ClearChrFlags(0x11, 0x80)

    label("loc_572")

    Return()

    # Function_2_373 end

    def Function_3_573(): pass

    label("Function_3_573")

    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59A")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5B1")

    label("loc_59A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B1")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_5B1")

    Return()

    # Function_3_573 end

    def Function_4_5B2(): pass

    label("Function_4_5B2")

    Call(0, 5)
    Return()

    # Function_4_5B2 end

    def Function_5_5B6(): pass

    label("Function_5_5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC")
    Call(0, 17)
    Jump("loc_1452")

    label("loc_5CC")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_64C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66C")
    OP_AF(0x52)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_144A")

    label("loc_66C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68C")
    OP_AF(0x50)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_144A")

    label("loc_68C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A0")
    Jump("loc_144A")

    label("loc_6A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_745")

    #C0001
    ChrTalk(
        0x8,
        (
            "結局ガンツさんがいなくなった理由も、\x01",
            "村長が帰ってこない理由も\x01",
            "未だに私らには伏せられたままさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "ああ、心配だねぇ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_144A")

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7CB")

    #C0003
    ChrTalk(
        0x8,
        (
            "バスに乗ろうとしてた町長を\x01",
            "見かけたんだが、\x01",
            "なんだか浮かない顔をしていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "ガンツさんに何かあったのかねぇ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_144A")

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_87A")

    #C0005
    ChrTalk(
        0x8,
        (
            "数ヶ月前の魔獣騒動といい\x01",
            "今回の鉱員の失踪といい……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "なんだか短い間に\x01",
            "色々なことが起こってるねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "悪いことの予兆だったり\x01",
            "しなきゃあいいんだが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144A")

    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_8C7")

    #C0008
    ChrTalk(
        0x8,
        (
            "なんだかお疲れのようだね。\x01",
            "なんだったら宿をとってくかい？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144A")

    label("loc_8C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_92A")

    #C0009
    ChrTalk(
        0x8,
        "なんだか最近締まらないねぇ……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "一番飲みっぷりのいいのが\x01",
            "来ないからかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144A")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A39")

    #C0011
    ChrTalk(
        0x8,
        (
            "うちに置いてある酒は、\x01",
            "ハロルドっていう商人さんに\x01",
            "頼んでるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "流石、身なりがいいだけあって\x01",
            "なかなかいい酒を\x01",
            "選んで持ってきてくれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "最近鉱員どもに麦酒を\x01",
            "あらかた開けられちまったし……\x01",
            "また来た時に頼んでおかないとねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AA6")

    label("loc_A39")


    #C0014
    ChrTalk(
        0x8,
        (
            "ハロルドさんが仕入れてくれる酒は\x01",
            "なかなかいいものが多くてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "ウチとしては重宝させてもらってるよ。\x02",
    )

    CloseMessageWindow()

    label("loc_AA6")

    Jump("loc_144A")

    label("loc_AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_CA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1E")

    #C0016
    ChrTalk(
        0x8,
        (
            "ウェイトレスのリュッカ、\x01",
            "いつもはブアイソでね。\x01",
            "憎まれ口ばかり叩いちゃうのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "……今度、お酒を盛ってやろうかねぇ。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "あの子、めちゃくちゃ酒に弱いからね。\x01",
            "酔っ払ったときの顔は見ものなんだよ。\x02",
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

    #C0019
    ChrTalk(
        0x102,
        "#0106F軽犯罪にならないのかしら……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CA1")

    label("loc_C1E")


    #C0020
    ChrTalk(
        0x8,
        "……今度、リュッカにお酒を盛ってやろうかねぇ。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "あの子、めちゃくちゃ酒に弱いからね。\x01",
            "酔っ払ったときの顔は見ものなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA1")

    Jump("loc_144A")

    label("loc_CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D49")

    #C0022
    ChrTalk(
        0x8,
        (
            "創立７０周年だからかねぇ。\x01",
            "今年は去年より観光客が多くて\x01",
            "大助かりだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "この時期は、いつも鉱員たちは\x01",
            "街に行っちまうから儲からないんだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144A")

    label("loc_D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_E7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE4")

    #C0024
    ChrTalk(
        0x8,
        "昨日は鉱員全員で宴会をやってたのさ。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "忙しかったけど、\x01",
            "あれだけ楽しそうにしてもらえると\x01",
            "酒場冥利に尽きるというものさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E75")

    label("loc_DE4")


    #C0026
    ChrTalk(
        0x8,
        (
            "そういえば、鉱員のロージーが\x01",
            "完全に潰れちゃってね。\x01",
            "仕方なく店で休ませてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "まったく、若いってのに\x01",
            "情けないったらありゃしないね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E75")

    Jump("loc_144A")

    label("loc_E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_EFC")

    #C0028
    ChrTalk(
        0x8,
        (
            "今日来てるお客さん、\x01",
            "随分若いけど遊撃士だそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "……なんだか重い雰囲気だけど\x01",
            "何かあったのかしらねぇ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144A")

    label("loc_EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1084")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1000")

    #C0030
    ChrTalk(
        0x8,
        (
            "ほんと、昼間のこの店は\x01",
            "ヒマなもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "……よし、ヒマだから\x01",
            "いいことを教えてあげよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "ウェイトレスやってるリュッカは\x01",
            "いつもブアイソなんだけどね……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "笑うと超絶に可愛いのさ。\x01",
            "あたしが男だったら\x01",
            "絶対惚れちまうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_107F")

    label("loc_1000")


    #C0034
    ChrTalk(
        0x8,
        (
            "リュッカはいつもブアイソだけど、\x01",
            "笑顔は超絶に可愛いんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "ま、その笑顔に\x01",
            "なかなかならないのが\x01",
            "残念なんだけどねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107F")

    Jump("loc_144A")

    label("loc_1084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_11D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115A")

    #C0036
    ChrTalk(
        0x8,
        (
            "魔獣騒ぎも収まって、\x01",
            "この町もいつも通りさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "鉱員連中は\x01",
            "『早く帰れなくなった』なんて\x01",
            "寝ぼけたことをぬかしてたけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "とにかく、\x01",
            "危険な目に遭わなくなって\x01",
            "本当によかったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11CF")

    label("loc_115A")


    #C0039
    ChrTalk(
        0x8,
        (
            "魔獣騒ぎも収まって、\x01",
            "鉱員や町の人間が\x01",
            "襲われることもなくなった。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "アンタたちのお陰さ。\x01",
            "本当にありがとうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CF")

    Jump("loc_144A")

    label("loc_11D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_128C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123C")

    #C0041
    ChrTalk(
        0x8,
        "ん、出かけるのかい？\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "最近物騒だし、\x01",
            "遅くならないうちに帰るんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1287")

    label("loc_123C")


    #C0043
    ChrTalk(
        0x8,
        (
            "なんだったら飲んで\x01",
            "暖まってくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        "……席埋まっちゃってるけど。\x02",
    )

    CloseMessageWindow()

    label("loc_1287")

    Jump("loc_144A")

    label("loc_128C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_144A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AE")
    SetScenarioFlags(0x66, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A4")

    #C0045
    ChrTalk(
        0x8,
        (
            "おや、見かけない顔だねぇ。\x01",
            "クロスベル市から来たのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "しかし、\x01",
            "タイミングの悪い時に来たねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "最近、狼型の魔獣が\x01",
            "この辺を荒らしまわっててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "うちも前に食糧庫を荒らされてねぇ。\x01",
            "まったく、迷惑ったらないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_144A")

    label("loc_13A4")


    #C0049
    ChrTalk(
        0x8,
        (
            "そうそう、\x01",
            "良かったら何か食べてくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "ゆっくり休もうと思ったら\x01",
            "今が休み時だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "夜になったら、\x01",
            "帰ってきた鉱員どもで\x01",
            "席がいっぱいになっちまうからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144A")

    Jump("loc_5D9")

    label("loc_144F")

    TalkEnd(0x8)

    label("loc_1452")

    Return()

    # Function_5_5B6 end

    def Function_6_1453(): pass

    label("Function_6_1453")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_14E3")

    #C0052
    ChrTalk(
        0xFE,
        (
            "ガンツさん失踪には\x01",
            "とんでもなく大きな謎が……\x01",
            "隠されているような気がするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "……ミステリー小説の\x01",
            "読みすぎかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E41")

    label("loc_14E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1570")

    #C0054
    ChrTalk(
        0xFE,
        (
            "ガンツさんが見つかったってことは……\x01",
            "またお祝いの宴会が開かれる可能性は大ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "はぁ……また片付けが大変なんだろうな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E41")

    label("loc_1570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_15FC")

    #C0056
    ChrTalk(
        0xFE,
        (
            "ガンツさんってほんと、\x01",
            "賭け事はへたくそみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "ここで酔っ払ってるときの話題は\x01",
            "大抵賭け事に負けた愚痴だったもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E41")

    label("loc_15FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_165F")

    #C0058
    ChrTalk(
        0xFE,
        "ん、掃除はこんなとこかな。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "ガンツさん１人いないだけで\x01",
            "掃除もえらく簡単ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E41")

    label("loc_165F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1721")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E9")

    #C0060
    ChrTalk(
        0xFE,
        "さーて、客の居ぬ間に掃除しなきゃ。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "って言っても、最近はなんだか\x01",
            "あんまり宴会をしてないみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_171C")

    label("loc_16E9")


    #C0062
    ChrTalk(
        0xFE,
        (
            "最近はあまり宴会がないから\x01",
            "掃除が楽でいいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171C")

    Jump("loc_1E41")

    label("loc_1721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_17BA")

    #C0063
    ChrTalk(
        0xFE,
        "今日で記念祭も終わりかぁ。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "観光客はいなくなるかもしれないけど、\x01",
            "入れ替わりに鉱員が帰ってくるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        "あーあ、忙しい忙しい。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E41")

    label("loc_17BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_182D")

    #C0066
    ChrTalk(
        0xFE,
        (
            "まぁまぁ忙しいけど……\x01",
            "あなたたちもなんか飲んでく？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "……仕事中だとしても責任持たないけど。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E41")

    label("loc_182D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_18BA")

    #C0068
    ChrTalk(
        0xFE,
        (
            "記念祭やってる最中に\x01",
            "わざわざこんな寂れたトコにくる\x01",
            "観光客ねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "……ま、気持ちはわかるかな。\x01",
            "私も人ごみ嫌いだし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E41")

    label("loc_18BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19AE")

    #C0070
    ChrTalk(
        0xFE,
        "ったく、毎日毎日ホント大変ね。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "……酒なんかどこがいいのかしら。\x01",
            "私全然飲めないから魅力が分からないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#0006Fや、宿酒場のウェイトレスとは\x01",
            "思えない発言だね……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "うっさいよお客さん。\x01",
            "私の勝手でしょ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A36")

    label("loc_19AE")


    #C0074
    ChrTalk(
        0xFE,
        "ほんと、酒なんかどこがいいのかしら。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "……前に興味本位で飲んだときは\x01",
            "記憶が無くなっちゃったから、\x01",
            "いまいち魅力が分からないわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A36")

    Jump("loc_1E41")

    label("loc_1A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1B4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF0")

    #C0076
    ChrTalk(
        0xFE,
        (
            "……何よ。\x01",
            "じろじろ見てんじゃないわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "注文なら女将さんが受けてるわ。\x01",
            "私は運ぶだけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "……以上。\x01",
            "分かったら私のことは\x01",
            "ほっといてくれない？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B47")

    label("loc_1AF0")


    #C0079
    ChrTalk(
        0xFE,
        (
            "毎晩毎晩、酔った鉱員の\x01",
            "相手をして疲れてんの。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        "私のことはほっといてくれない？\x02",
    )

    CloseMessageWindow()

    label("loc_1B47")

    Jump("loc_1E41")

    label("loc_1B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1CB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C20")

    #C0081
    ChrTalk(
        0xFE,
        (
            "くぁ……\x01",
            "あーもう、眠い眠い。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "鉱員たちが仕事帰りに\x01",
            "宴会してくもんだから、\x01",
            "私も女将さんも寝不足なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "ったく、いつまで\x01",
            "『魔獣撃退記念パーティ』を\x01",
            "やるつもりなのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CAE")

    label("loc_1C20")


    #C0084
    ChrTalk(
        0xFE,
        (
            "鉱員たちったら、未だに\x01",
            "『魔獣撃退記念パーティ』を\x01",
            "毎晩やってんのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "とにかく理由をかこつけて\x01",
            "飲みたいだけなのよね。\x01",
            "ったくもう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAE")

    Jump("loc_1E41")

    label("loc_1CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1CC1")
    Jump("loc_1E41")

    label("loc_1CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1D7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3E")

    #C0086
    ChrTalk(
        0xFE,
        (
            "ふきふき……\x01",
            "よし、これでオッケーね。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "さ、これから忙しくなるし……\x01",
            "ちょっと休憩しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D75")

    label("loc_1D3E")


    #C0088
    ChrTalk(
        0xFE,
        (
            "さ、これから忙しくなるし……\x01",
            "ちょっと休憩しよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D75")

    Jump("loc_1E41")

    label("loc_1D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1E41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9C")
    SetScenarioFlags(0x66, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E06")

    #C0089
    ChrTalk(
        0xFE,
        (
            "……いらっしゃい。\x01",
            "注文ならカウンターね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "……何よ、\x01",
            "あたしになんか用なワケ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E41")

    label("loc_1E06")


    #C0091
    ChrTalk(
        0xFE,
        (
            "注文ならカウンターにしてくれる？\x01",
            "夜の準備で忙しいの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E41")

    TalkEnd(0xFE)
    Return()

    # Function_6_1453 end

    def Function_7_1E45(): pass

    label("Function_7_1E45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA3")

    #C0092
    ChrTalk(
        0xFE,
        (
            "うぇ…………\x01",
            "も……う飲めません……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        "ひ、一人にしてくれ…………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1EC3")

    label("loc_1EA3")


    #C0094
    ChrTalk(
        0xFE,
        "ひ、一人にしてくれ…………\x02",
    )

    CloseMessageWindow()

    label("loc_1EC3")

    TalkEnd(0xFE)
    Return()

    # Function_7_1E45 end

    def Function_8_1EC7(): pass

    label("Function_8_1EC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE3")

    #C0095
    ChrTalk(
        0xFE,
        "おほほほほほ！\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "ついに、ついに……\x01",
            "七耀石の結晶を買い付けることに\x01",
            "成功しましたわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "それにしても\x01",
            "こんな大きな紅耀石#6Rカーネリア#……\x01",
            "初めて見ましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "ふふ、これで帝国のお父様には\x01",
            "いい報告が出来そう！\x01",
            "大商人にまた一歩近づきましたわ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2072")

    label("loc_1FE3")


    #C0099
    ChrTalk(
        0xFE,
        (
            "こんな大きな紅耀石#6Rカーネリア#が\x01",
            "採掘できるなんて……\x01",
            "さすがは七耀石の産地ですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "ふふ、帝国のお父様には\x01",
            "いい報告が出来そうね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2072")

    Jump("loc_27D1")

    label("loc_2077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_20E5")

    #C0101
    ChrTalk(
        0xFE,
        (
            "今夜は町長の家で\x01",
            "七耀石の取り引き交渉よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "手に入れるまで……\x01",
            "絶対に諦めないんだから！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D1")

    label("loc_20E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_226E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FF")

    #C0103
    ChrTalk(
        0xFE,
        (
            "七耀石の結晶を\x01",
            "なんとか買い付けようと、\x01",
            "前から町長と交渉しているのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "あの町長も手強いわね。\x01",
            "なかなかＹＥＳと言ってくれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "ううん、腐ってばかりは\x01",
            "いられないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "大商人のお父様の血を引く私ですもの、\x01",
            "きっと手に入れて見せるわ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2269")

    label("loc_21FF")


    #C0107
    ChrTalk(
        0xFE,
        (
            "そうと決まれば早速、\x01",
            "交渉の手立てを考えないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "まずは提示額を思いっきり\x01",
            "引き上げちゃって……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2269")

    Jump("loc_27D1")

    label("loc_226E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_22E2")

    #C0109
    ChrTalk(
        0xFE,
        (
            "うう……昨日は１階がうるさくて\x01",
            "眠れなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "すごくだるい……\x01",
            "今日は寝てることにします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D1")

    label("loc_22E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_24B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2414")

    #C0111
    ChrTalk(
        0xFE,
        (
            "私がこのマインツで狙っている\x01",
            "七耀石の結晶は\x01",
            "それはそれは貴重なものなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "まぁ、発掘量が少ないから\x01",
            "本当に運が良くないと\x01",
            "手に入らないらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "昨日の交渉では\x01",
            "残念ながら断られてしまったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "……なぁに、\x01",
            "滞在資金ならたっぷりあるし、\x01",
            "とことん粘ってみせるわ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_24AC")

    label("loc_2414")


    #C0115
    ChrTalk(
        0xFE,
        (
            "滞在資金はたっぷりあるし、\x01",
            "身の回りの世話兼ヒマ潰し用に\x01",
            "レティナも連れてきたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "おほほほほ、\x01",
            "結晶を手に入れるまでは\x01",
            "とことん粘って見せるわ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AC")

    Jump("loc_27D1")

    label("loc_24B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2698")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F5")

    #C0117
    ChrTalk(
        0xFE,
        (
            "貴重な七耀石の結晶……\x01",
            "私はそれを狙って\x01",
            "ここに滞在してるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "結晶は、魔獣が落とすセピスみたいな\x01",
            "ちゃちなモノじゃないわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "どれも妖艶な輝きを秘めていて、\x01",
            "帝国の貴族層は\x01",
            "アクセサリになんかしてるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "手に入れて帝国に持ち帰れば、\x01",
            "かなりの値で売れるに違いないわ。\x01",
            "おほほほほ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2693")

    label("loc_25F5")


    #C0121
    ChrTalk(
        0xFE,
        (
            "七耀石の結晶は、\x01",
            "魔獣が落とすみたいな\x01",
            "ちゃちなセピスじゃないのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "手に入れて帝国に持ち帰れば、\x01",
            "かなりの高さで売れるに違いないわ。\x01",
            "おほほほほ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2693")

    Jump("loc_27D1")

    label("loc_2698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_26A6")
    Jump("loc_27D1")

    label("loc_26A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_2743")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C1")
    Call(0, 10)
    Jump("loc_273E")

    label("loc_26C1")


    #C0123
    ChrTalk(
        0xFE,
        (
            "大体、そろそろ鉱員の方たちが\x01",
            "戻ってくる頃でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "昨日みたいな\x01",
            "どんちゃん騒ぎの中で\x01",
            "ご飯なんか食べてらんないわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_273E")

    Jump("loc_27D1")

    label("loc_2743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_27D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275E")
    Call(0, 10)
    Jump("loc_27D1")

    label("loc_275E")


    #C0125
    ChrTalk(
        0xFE,
        (
            "あら……あなたも\x01",
            "七耀石の買い付けに来たのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "おーほっほ！\x01",
            "果たして私の取引テクに\x01",
            "勝てるかしらね！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D1")

    TalkEnd(0xFE)
    Return()

    # Function_8_1EC7 end

    def Function_9_27D5(): pass

    label("Function_9_27D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2946")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28CB")

    #C0127
    ChrTalk(
        0xFE,
        (
            "お嬢様が七耀石の結晶を……\x01",
            "はぁ……長かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "たしかにスゴくいいものみたいですけど……\x01",
            "４ヶ月近い滞在費を使ったこと、\x01",
            "ちゃんと分かってるんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "…………\x01",
            "あまり考えない方がよさそうですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2941")

    label("loc_28CB")


    #C0130
    ChrTalk(
        0xFE,
        (
            "……とにかくこれで、\x01",
            "やっと帝国に帰れます。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "４ヶ月近くも出奔したままで\x01",
            "お屋敷は今頃どうしてるでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2941")

    Jump("loc_3018")

    label("loc_2946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29CB")

    #C0132
    ChrTalk(
        0xFE,
        (
            "（お嬢様も\x01",
            "  お取り引きの話の時だけは\x01",
            "  こんなに真剣に……）\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "（い、一体どうなるんでしょう……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2A13")

    label("loc_29CB")


    #C0134
    ChrTalk(
        0xFE,
        (
            "（どきどき……\x01",
            "  今夜のお取り引き、\x01",
            "  一体どうなるんでしょう……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A13")

    Jump("loc_3018")

    label("loc_2A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2ADE")

    #C0135
    ChrTalk(
        0xFE,
        (
            "お嬢様は持ち前の押しの強さと\x01",
            "潤沢な資金で交渉してるんですが……\x01",
            "なかなか難しいみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "……もう、ここまできたらヤケです。\x01",
            "お嬢様にはとことん\x01",
            "頑張ってもらおうと思います！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3018")

    label("loc_2ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2C07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B80")

    #C0137
    ChrTalk(
        0xFE,
        (
            "昨日は鉱員さんたちが\x01",
            "遅くまで宴会をしていたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "……私も遅くまで\x01",
            "お嬢様が眠れるように\x01",
            "努力していたのでキツいです……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2C02")

    label("loc_2B80")


    #C0139
    ChrTalk(
        0xFE,
        (
            "今日は町長様も疲れてるでしょうし……\x01",
            "買い付け交渉は諦めるしかないですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "……いつになったら\x01",
            "帝国に帰れるんでしょう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C02")

    Jump("loc_3018")

    label("loc_2C07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2D65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CE8")

    #C0141
    ChrTalk(
        0xFE,
        (
            "お嬢様の滞在資金……\x01",
            "なんでも、屋敷の金庫から\x01",
            "ちょろまかしてきたらしいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "１年間は余裕で滞在できる……\x01",
            "お嬢様はそう言ってましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "ううっ、いったい\x01",
            "どれだけのミラを……！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2D60")

    label("loc_2CE8")


    #C0144
    ChrTalk(
        0xFE,
        (
            "１年間は滞在できるミラと\x01",
            "鉄道のチケットが往復二人分……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "ううっ、今頃お屋敷は\x01",
            "大騒ぎになっているのでは……！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D60")

    Jump("loc_3018")

    label("loc_2D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2EDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5D")

    #C0146
    ChrTalk(
        0xFE,
        (
            "お嬢様はエレボニア帝国有数の\x01",
            "大商人の一人娘なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "ゆくゆくはご自分も\x01",
            "大女商人になるために、と\x01",
            "私を引っ張ってこの自治州に……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "はぁ、黙ってお屋敷を出てきたので\x01",
            "帰ったら旦那さまに\x01",
            "大目玉を喰らいそうです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2ED5")

    label("loc_2E5D")


    #C0149
    ChrTalk(
        0xFE,
        (
            "とにかくお屋敷に早く戻らないと\x01",
            "私などは１００％クビです。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "七耀石の結晶、\x01",
            "早く手に入ってくれないでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED5")

    Jump("loc_3018")

    label("loc_2EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_2EE8")
    Jump("loc_3018")

    label("loc_2EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_2F75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F03")
    Call(0, 10)
    Jump("loc_2F70")

    label("loc_2F03")


    #C0151
    ChrTalk(
        0xFE,
        (
            "とほほ……\x01",
            "夕食を受け取りに行かないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "私、ドジですから……\x01",
            "階段で転んでしまわないか\x01",
            "心配です……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F70")

    Jump("loc_3018")

    label("loc_2F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3018")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F90")
    Call(0, 10)
    Jump("loc_3018")

    label("loc_2F90")


    #C0153
    ChrTalk(
        0xFE,
        (
            "お嬢様と私は、\x01",
            "帝国から七耀石の\x01",
            "買い付けに来たんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "でも、最近町の近くで\x01",
            "魔獣が出没するとかで、\x01",
            "ちょっと怖いんですよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3018")

    TalkEnd(0xFE)
    Return()

    # Function_9_27D5 end

    def Function_10_301C(): pass

    label("Function_10_301C")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_312D")

    #C0155
    ChrTalk(
        0xB,
        (
            "あら、もうこんな時間ね。\x01",
            "おなかが空いたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "レティナ、女将の所に行って\x01",
            "晩御飯をもらって来なさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        (
            "あ、あのう……\x01",
            "折角なので上のテーブルで\x01",
            "召し上がられては……？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        (
            "めんどくさい。\x01",
            "いいから行ってきなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xC,
        "とほほ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_322F")

    label("loc_312D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_322F")

    #C0160
    ChrTalk(
        0xB,
        (
            "おーほっほ。\x01",
            "さすがは大陸有数の\x01",
            "七耀石の産地ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xC,
        (
            "そ、そうですねお嬢様。\x01",
            "昨日はビクセン町長といい取引も\x01",
            "出来ましたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        (
            "この分だと、\x01",
            "七耀石の結晶を手に入れるのも\x01",
            "時間の問題だわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "うん、迷っていたけど、\x01",
            "暫く滞在することに決定！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_322F")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_10_301C end

    def Function_11_323E(): pass

    label("Function_11_323E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32D2")
    Jump("loc_331C")

    label("loc_32D2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32F2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_331C")

    label("loc_32F2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3312")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_331C")

    label("loc_3312")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_331C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_34F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_335C")
    Call(0, 16)
    Jump("loc_34F5")

    label("loc_335C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_349C")

    #C0164
    ChrTalk(
        0xD,
        (
            "#0805Fあ、ロイド君たち……\x02\x03",

            "#0809Fあはは……\x01",
            "ぜんぜん気付かなかった。\x01",
            "仕事で来てるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        (
            "#0002Fあ、ああ。\x01",
            "まあそんな所かな。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#0108F（エステルさん……\x01",
            "  何だか無理してるわね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x104,
        (
            "#0303F（ああ……\x01",
            "  ちょいと気になるが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        (
            "#0208F（……これは困惑……？\x01",
            "  それとも深い哀しみ……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_34F5")

    label("loc_349C")


    #C0169
    ChrTalk(
        0xD,
        (
            "#0809Fさ、さーてと！\x01",
            "一休みしたら街に戻らないと！\x02\x03",

            "#0802Fロイド君たちも頑張ってね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_323E end

    def Function_12_34FD(): pass

    label("Function_12_34FD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3591")
    Jump("loc_35DB")

    label("loc_3591")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_35B1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35DB")

    label("loc_35B1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35D1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35DB")

    label("loc_35D1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_35DB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3684")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361B")
    Call(0, 16)
    Jump("loc_3684")

    label("loc_361B")


    #C0170
    ChrTalk(
        0xE,
        (
            "#0903F（ごめん、色々あってさ……）\x02\x03",

            "#0900F（今はエステルのことを\x01",
            "  そっとしてあげてくれないかな？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3684")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_34FD end

    def Function_13_368C(): pass

    label("Function_13_368C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3720")
    Jump("loc_376A")

    label("loc_3720")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3740")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_376A")

    label("loc_3740")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3760")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_376A")

    label("loc_3760")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_376A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_390F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_388E")

    #C0171
    ChrTalk(
        0xFE,
        (
            "警察の子たちか。\x01",
            "お疲れさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "例のマフィア、\x01",
            "何とか立件できたそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        (
            "#0200F……ルバーチェですね。\x01",
            "２日で釈放されてしまいましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        "はは、そう落ち込むなよ。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "遊撃士やってても\x01",
            "そういう事はよくあるさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_390F")

    label("loc_388E")


    #C0176
    ChrTalk(
        0xFE,
        (
            "あの魔獣事件以来、\x01",
            "各地の依頼のついでに\x01",
            "見回りすることになってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "さらに忙しくなったけど……\x01",
            "まぁ、必要なことだしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_390F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_368C end

    def Function_14_3917(): pass

    label("Function_14_3917")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39AB")
    Jump("loc_39F5")

    label("loc_39AB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39CB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39F5")

    label("loc_39CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39EB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39F5")

    label("loc_39EB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39F5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3B62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AEF")

    #C0178
    ChrTalk(
        0xFE,
        (
            "あの事件の解決……\x01",
            "お前たちにしてはよくやったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "だが、慢心はするんじゃないぞ。\x01",
            "常に向上心を持って\x01",
            "精進していくことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0003F（ちょっとは認めて\x01",
            "  もらえたのかな……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3B62")

    label("loc_3AEF")


    #C0181
    ChrTalk(
        0xFE,
        (
            "成功は慢心を呼ぶ。\x01",
            "それに溺れてしまうと\x01",
            "次の成功はやってこない。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "常に向上心を持って\x01",
            "精進していくことだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B62")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_3917 end

    def Function_15_3B6A(): pass

    label("Function_15_3B6A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BFE")
    Jump("loc_3C48")

    label("loc_3BFE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C1E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C48")

    label("loc_3C1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C3E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C48")

    label("loc_3C3E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C48")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF5")

    #C0183
    ChrTalk(
        0xFE,
        "ぐびっぐびっ……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "くぅ～……\x01",
            "昼間から１人で飲むなんて\x01",
            "贅沢もいいところだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        "まあアイスティーだけどね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3D2B")

    label("loc_3CF5")


    #C0186
    ChrTalk(
        0xFE,
        "ぐびっぐびっぐびっ……\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "ぷはぁー、うめぇー！\x02",
    )

    CloseMessageWindow()

    label("loc_3D2B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_3B6A end

    def Function_16_3D33(): pass

    label("Function_16_3D33")

    EventBegin(0x0)
    Fade(500)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_68(-8200, 750, -3800, 0)
    MoveCamera(55, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, -6100, -750, -4050, 270)
    SetChrPos(0x102, -5950, -750, -5050, 270)
    SetChrPos(0x103, -5100, -750, -4050, 270)
    SetChrPos(0x104, -4950, -750, -5050, 270)
    OP_0D()

    #C0188
    ChrTalk(
        0xD,
        "#0808F#11P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xE,
        (
            "#0906F#12Pどうやら調査した通り、\x01",
            "かなり真っ当な人みたいだね。\x02\x03",

            "#0908Fやっぱりあの子の勘違い……\x01",
            "いや、そう思い込もうとしたのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xD,
        (
            "#0808F#11P……わかってるよ……\x01",
            "あの人が悪いわけじゃないって。\x02\x03",

            "もちろんあの子が\x01",
            "悪かったわけじゃ絶対ない……\x02\x03",

            "#0811Fねえヨシュア……\x01",
            "あたし……どうしたらいいの？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xE,
        (
            "#0903F#12P……落ち着いて、エステル。\x01",
            "簡単に解決する問題じゃない。\x02\x03",

            "#0900F焦らずじっくり取り組もうって\x01",
            "ここに来る前に決めただろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xD,
        "#0806F#11P……うん。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        (
            "#0001F#11P（何だか深刻な話を\x01",
            "  しているみたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -6100, -750, -4550, 270)
    SetScenarioFlags(0x94, 4)
    EventEnd(0x5)
    Return()

    # Function_16_3D33 end

    def Function_17_4002(): pass

    label("Function_17_4002")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(3040, 1500, 1600, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    SetChrPos(0x101, 2900, 0, 1900, 0)
    SetChrPos(0x102, 4100, 0, 1900, 0)
    SetChrPos(0x103, 2900, 0, 700, 0)
    SetChrPos(0x104, 4100, 0, 700, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0194
    ChrTalk(
        0x8,
        (
            "#1Pおや、アンタたち……\x01",
            "もう夕方だよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "#1Pバスの最終は８時くらいだけど\x01",
            "大丈夫なのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        (
            "#0100F#2Pいえ……今日はこちらに\x01",
            "泊めていただこうと思いまして。\x02\x03",

            "その、テーブルのある\x01",
            "大きな部屋は空いていますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        "#1Pああ、空いてるよ。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "#1Pふふ、嬉しいねぇ。\x01",
            "アンタたちみたいな若いのが\x01",
            "ウチに泊まってってくれるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x8,
        "#1P夕食もウチで取るのかい？\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#0000F#2Pええ、お願いできれば。\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "#1Pよしきた、腕によりをかけて\x01",
            "美味しいのを作ってやるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "#1P部屋は降りて左手の奥さ。\x01",
            "夕食までゆっくりしておいき。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x104,
        "#0300F#4Pサンクス、おばちゃん。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x103,
        "#0200F#4P……失礼します。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("t052B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_4002 end

    SaveToFile()

Try(main)
