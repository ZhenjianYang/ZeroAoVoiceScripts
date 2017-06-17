from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1070.bin",                # FileName
        "t1070",                    # MapName
        "t1070",                    # Location
        0x0000,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1070",                  # 0
        "マライア",               # 1
        "タイラー",               # 2
        "観光客",                 # 3
        "観光客",                 # 4
        "観光客",                 # 5
        "観光客",                 # 6
        "ワジ",                   # 7
        "ランディ",               # 8
        "ノエル",                 # 9
        "フラン",                 # 10
    ))

    AddCharChip((
        "chr/ch32400.itc",                   # 00
        "chr/ch25900.itc",                   # 01
        "chr/ch33000.itc",                   # 02
        "chr/ch22000.itc",                   # 03
        "chr/ch33300.itc",                   # 04
        "chr/ch33200.itc",                   # 05
        "chr/ch03000.itc",                   # 06
        "chr/ch00300.itc",                   # 07
        "chr/ch02900.itc",                   # 08
        "chr/ch08500.itc",                   # 09
    ))

    DeclNpc(-6500,   0,       5000,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-6300,   0,       9500,    90,   261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       5000,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(6119,    0,       3660,    90,   389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(6119,    0,       2240,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       5000,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(6119,    0,       3660,    90,   389,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(5550,    0,       10000,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(500,     0,       9000,    0,    389,  0x0, 0,   8,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-500,    0,       9000,    0,    389,  0x0, 0,   9,   0,   0,   0,   0,   3,   255,  0)

    DeclActor(-4700,   0,       5000,    1000,    -6500,   1500,    5000,    0x007E, 0,  8,  0x0000)

    ChipFrameInfo(636, 0)                                        # 0

    ScpFunction((
        "Function_0_27C",          # 00, 0
        "Function_1_334",          # 01, 1
        "Function_2_4FB",          # 02, 2
        "Function_3_532",          # 03, 3
        "Function_4_73D",          # 04, 4
        "Function_5_AAA",          # 05, 5
        "Function_6_C0E",          # 06, 6
        "Function_7_1113",         # 07, 7
        "Function_8_11F0",         # 08, 8
        "Function_9_11F4",         # 09, 9
        "Function_10_1835",        # 0A, 10
        "Function_11_1B92",        # 0B, 11
        "Function_12_1D13",        # 0C, 12
        "Function_13_1D9B",        # 0D, 13
        "Function_14_1F15",        # 0E, 14
        "Function_15_2098",        # 0F, 15
        "Function_16_2AB5",        # 10, 16
        "Function_17_2B0E",        # 11, 17
        "Function_18_2B67",        # 12, 18
        "Function_19_2BC0",        # 13, 19
        "Function_20_2C0B",        # 14, 20
        "Function_21_2C5D",        # 15, 21
        "Function_22_3E58",        # 16, 22
        "Function_23_3EAA",        # 17, 23
        "Function_24_3F2E",        # 18, 24
        "Function_25_3F87",        # 19, 25
        "Function_26_3FD9",        # 1A, 26
        "Function_27_4024",        # 1B, 27
        "Function_28_4050",        # 1C, 28
        "Function_29_409B",        # 1D, 29
        "Function_30_50F5",        # 1E, 30
        "Function_31_5E76",        # 1F, 31
        "Function_32_6DB2",        # 20, 32
    ))


    def Function_0_27C(): pass

    label("Function_0_27C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2BC"),
        (1, "loc_2C8"),
        (2, "loc_2D4"),
        (3, "loc_2E0"),
        (4, "loc_2EC"),
        (5, "loc_2F8"),
        (6, "loc_304"),
        (SWITCH_DEFAULT, "loc_310"),
    )


    label("loc_2BC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2C8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2D4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2E0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2EC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_2F8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_304")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_310")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_31C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_333")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_31C")

    label("loc_333")

    Return()

    # Function_0_27C end

    def Function_1_334(): pass

    label("Function_1_334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_342")
    Jump("loc_47C")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_350")
    Jump("loc_47C")

    label("loc_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_3B0")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 100, 0, 5000, 90)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1200, 0, 5000, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A1")
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_3AB")

    label("loc_3A1")

    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_3AB")

    Jump("loc_47C")

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_3BE")
    Jump("loc_47C")

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_421")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_3FC")
    TurnDirection(0x10, 0x11, 0)
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x11, 0x10, 0)
    ClearChrFlags(0x11, 0x10)

    label("loc_3FC")

    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -5340, 0, 1100, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    Jump("loc_47C")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_43E")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_47C")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_44C")
    Jump("loc_47C")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_473")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_47C")

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_47C")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_497")
    Event(0, 15)
    Jump("loc_4FA")

    label("loc_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_4BB")
    Event(0, 21)
    Jump("loc_4FA")

    label("loc_4BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_4CC")
    Event(0, 29)
    Jump("loc_4FA")

    label("loc_4CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_4DD")
    Event(0, 30)
    Jump("loc_4FA")

    label("loc_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_4EE")
    Event(0, 31)
    Jump("loc_4FA")

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_4FA")
    Event(0, 32)

    label("loc_4FA")

    Return()

    # Function_1_334 end

    def Function_2_4FB(): pass

    label("Function_2_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_514")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_51A")

    label("loc_514")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_531")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_531")

    Return()

    # Function_2_4FB end

    def Function_3_532(): pass

    label("Function_3_532")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_543")
    Jump("loc_739")

    label("loc_543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_551")
    Jump("loc_739")

    label("loc_551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_55F")
    Jump("loc_739")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_67B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A")

    #C0001
    ChrTalk(
        0x11,
        (
            "#06406Fお姉ちゃん、さっきから\x01",
            "様子が変なんですよね～。\x02\x03",

            "#06402Fビーチでなにかあったんですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#00012Fい、いや～……\x01",
            "それはちょっと、俺からは\x01",
            "説明しにくいというか。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x11,
        "#06405F？？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_676")

    label("loc_63A")


    #C0004
    ChrTalk(
        0x11,
        (
            "#06406Fお姉ちゃん、さっきから\x01",
            "様子が変なんですよね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_676")

    Jump("loc_739")

    label("loc_67B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_696")
    Call(0, 5)
    Jump("loc_70F")

    label("loc_696")


    #C0005
    ChrTalk(
        0x11,
        (
            "#06409Fロイドさん、このネックレスを\x01",
            "プレゼントしてくださいよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#00006Fい、いやいや、さすがに手が出ないから。\x02",
    )

    CloseMessageWindow()

    label("loc_70F")

    Jump("loc_739")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_722")
    Jump("loc_739")

    label("loc_722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_730")
    Jump("loc_739")

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_739")

    label("loc_739")

    TalkEnd(0xFE)
    Return()

    # Function_3_532 end

    def Function_4_73D(): pass

    label("Function_4_73D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_74E")
    Jump("loc_AA6")

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_75C")
    Jump("loc_AA6")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_76A")
    Jump("loc_AA6")

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_9E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_937")

    #C0007
    ChrTalk(
        0x10,
        (
            "#10106Fはあ……危険はあったとはいえ、\x01",
            "まさか本当に水着を切られるなんて……\x02\x03",

            "#10101Fあの程度の攻撃を防げないなんて、\x01",
            "まだまだ修行が足りませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00006F……ゴ、ゴメン。\x01",
            "俺も、もう少し気づくのが早ければ\x01",
            "なんとかできたかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x10,
        (
            "#10114Fあ、い、いえ！\x01",
            "幸い怪我もありませんでしたし！\x02\x03",

            "#10103Fは、恥ずかしかったのは確かですけど……\x01",
            "これをバネに、精進したいと思います！\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00012F（な、何を精進するんだろう……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_9DE")

    label("loc_937")


    #C0011
    ChrTalk(
        0x10,
        (
            "#10106Fはあ……あの程度の魔獣の\x01",
            "攻撃を防げないなんて、\x01",
            "まだまだ修行が足りませんね。\x02\x03",

            "#10101Fおかげで恥ずかしい思いをしちゃったし……\x01",
            "これをバネに、精進しないと！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DE")

    Jump("loc_AA6")

    label("loc_9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_A73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FE")
    Call(0, 5)
    Jump("loc_A6E")

    label("loc_9FE")


    #C0012
    ChrTalk(
        0x10,
        (
            "#10106Fこ、こんな凄いネックレス、\x01",
            "だれが買えるんでしょう。\x02\x03",

            "#10101F下手すると国宝レベルの\x01",
            "値段ですよ……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6E")

    Jump("loc_AA6")

    label("loc_A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A81")
    Jump("loc_AA6")

    label("loc_A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_A8F")
    Jump("loc_AA6")

    label("loc_A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A9D")
    Jump("loc_AA6")

    label("loc_A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_AA6")

    label("loc_AA6")

    TalkEnd(0xFE)
    Return()

    # Function_4_73D end

    def Function_5_AAA(): pass

    label("Function_5_AAA")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0013
    ChrTalk(
        0x10,
        "#10109Fはあ～、すごく綺麗なネックレス……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x11,
        (
            "#06402Fこのお店の目玉商品みたいだよ～。\x02\x03",

            "#06405Fえ～と、気になるお値段は……\x01",
            "……ゼロが、ひぃ、ふう、みぃ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)
    OP_64(0x11)

    #C0015
    ChrTalk(
        0x10,
        (
            "#10106F……こ、このネックレス一つで\x01",
            "導力車が何台も買えちゃうんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x11,
        "#06406Fさ、さすがに世界が違うね～。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_5_AAA end

    def Function_6_C0E(): pass

    label("Function_6_C0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_C1F")
    Jump("loc_110F")

    label("loc_C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C2D")
    Jump("loc_110F")

    label("loc_C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_C3B")
    Jump("loc_110F")

    label("loc_C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_FB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F27")

    #C0017
    ChrTalk(
        0xF,
        (
            "#00300Fよう、ロイド。\x01",
            "キー坊は見つかったみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x153,
        "#01109Fえへへ、勝手にうろついてゴメンね。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xF,
        (
            "#00303F……よし、許す！\x01",
            "許さないわけがねえ！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00009Fはは……\x02\x03",

            "#00005F……あれ、そういえばランディ、\x01",
            "ここで何か買ってたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xF,
        (
            "#00302Fああ、ミレイユのやつに\x01",
            "ちょっとした土産でもと思ってな。\x02\x03",

            "#00304Fアイツも昇進が近いらしいし、\x01",
            "その祝いも込めてって感じだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00005Fへえ～、なるほど……\x02\x03",

            "#00012Fあのさ、もしかしてランディって\x01",
            "ミレイユ准尉のこと……？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xF,
        (
            "#00304Fはは、なに寝ぼけたことを\x01",
            "言ってんだっつの。\x02\x03",

            "#00300F警備隊時代には世話になってたし、\x01",
            "この位は礼儀のうちだろうが？\x02\x03",

            "#00309Fそれに、俺のストライクは\x01",
            "セシルさんだしな！！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#00006F聞き捨てならない発言だけど……\x01",
            "まあでも、そういうものか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 1)
    Jump("loc_FAD")

    label("loc_F27")


    #C0025
    ChrTalk(
        0xF,
        (
            "#00300F俺ももうちょいしたら、\x01",
            "ノエルたちと集合場所に向かうぜ。\x02\x03",

            "#00304Fそれまではウィンドウショッピングに\x01",
            "勤しんでるとするかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAD")

    Jump("loc_110F")

    label("loc_FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_10EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1075")

    #C0026
    ChrTalk(
        0xF,
        (
            "#00301Fん～、ネックレスか……\x02\x03",

            "#00306Fアイツのことだから、\x01",
            "こういうのは演習のジャマだとか\x01",
            "言いそうだなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#00005F（なんだか真剣に選んでる\x01",
            "  みたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_10E5")

    label("loc_1075")


    #C0028
    ChrTalk(
        0xF,
        (
            "#00303Fあんまりジャマにならねえ\x01",
            "小物のほうがいいのかもな。\x02\x03",

            "#00300F向こうのブローチとかを\x01",
            "見てみるかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E5")

    Jump("loc_110F")

    label("loc_10EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_10F8")
    Jump("loc_110F")

    label("loc_10F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1106")
    Jump("loc_110F")

    label("loc_1106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_110F")

    label("loc_110F")

    TalkEnd(0xFE)
    Return()

    # Function_6_C0E end

    def Function_7_1113(): pass

    label("Function_7_1113")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1124")
    Jump("loc_11EC")

    label("loc_1124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1132")
    Jump("loc_11EC")

    label("loc_1132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1140")
    Jump("loc_11EC")

    label("loc_1140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_11B9")

    #C0029
    ChrTalk(
        0xE,
        (
            "#10305F……おや、この宝石はこの間\x01",
            "あの婦人にもらった物に似てるな。\x02\x03",

            "#10302Fフフ、ここで買ったのかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11EC")

    label("loc_11B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_11C7")
    Jump("loc_11EC")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_11D5")
    Jump("loc_11EC")

    label("loc_11D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11E3")
    Jump("loc_11EC")

    label("loc_11E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_11EC")

    label("loc_11EC")

    TalkEnd(0xFE)
    Return()

    # Function_7_1113 end

    def Function_8_11F0(): pass

    label("Function_8_11F0")

    Call(0, 9)
    Return()

    # Function_8_11F0 end

    def Function_9_11F4(): pass

    label("Function_9_11F4")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_14AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 7)), scpexpr(EXPR_END)), "loc_1327")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C3")

    #C0030
    ChrTalk(
        0x8,
        (
            "ホホホ……\x01",
            "お買い上げありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "宝飾品とはまさに\x01",
            "万感の思いを込められし\x01",
            "人生の贈り物……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "さぞ大切にされることを\x01",
            "女神にお祈りしておきますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1322")

    label("loc_12C3")


    #C0033
    ChrTalk(
        0x8,
        "宝飾品とはまさに人生の贈り物……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "さぞ大切にされることを\x01",
            "女神にお祈りしておきますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1322")

    Jump("loc_14A6")

    label("loc_1327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FE")

    #C0035
    ChrTalk(
        0x8,
        (
            "宝飾品とはまさに\x01",
            "万感の思いを込められし\x01",
            "人生の贈り物……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "贈るチャンスを掴めるかも\x01",
            "また、その人次第なのですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "ホホホ……\x01",
            "今度来るときは懐をぬくぬくと\x01",
            "暖めてからいらっしゃることね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14A6")

    label("loc_13FE")


    #C0038
    ChrTalk(
        0x8,
        (
            "宝飾品とはまさに人生の贈り物……\x01",
            "贈るチャンスを掴めるかも\x01",
            "また、その人次第なのですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "ホホホ……\x01",
            "今度来るときは懐をぬくぬくと\x01",
            "暖めてからいらっしゃることね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A6")

    Jump("loc_1831")

    label("loc_14AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_16AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DB")

    #C0040
    ChrTalk(
        0x8,
        (
            "ウチが会員制度をとるのは、\x01",
            "信頼の置けるお得意様に向けて\x01",
            "最高のサービスを提供するためですのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "お客様が増えれば、どうしても\x01",
            "サービスの質は低下してしまいますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "ただ無制限に集客をするのだけが\x01",
            "商売のやり方ではない、ということ。\x01",
            "ホホホ、勉強になりましたかしら？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16A7")

    label("loc_15DB")


    #C0043
    ChrTalk(
        0x8,
        (
            "ウチが会員制度をとるのは、\x01",
            "信頼の置けるお得意様に向けて\x01",
            "最高のサービスを提供するためですのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "ただ無制限に集客をするのだけが\x01",
            "商売のやり方ではない、ということ。\x01",
            "ホホホ、勉強になりましたかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A7")

    Jump("loc_1831")

    label("loc_16AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1793")

    #C0045
    ChrTalk(
        0x8,
        (
            "ホホホ……\x01",
            "アタクシの《ディアマンテ》に\x01",
            "よくぞいらっしゃったわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "ここでは、最高級の宝飾品ばかりを\x01",
            "取り揃えてございましてよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "この永遠の輝きを手にする資格、\x01",
            "アナタはお持ちなのかしらね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1831")

    label("loc_1793")


    #C0048
    ChrTalk(
        0x8,
        (
            "この《ディアマンテ》では、\x01",
            "最高級の宝飾品ばかりを\x01",
            "取り揃えてございましてよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "ホホホ……\x01",
            "この永遠の輝きを手にする資格、\x01",
            "アナタはお持ちなのかしらね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1831")

    TalkEnd(0x8)
    Return()

    # Function_9_11F4 end

    def Function_10_1835(): pass

    label("Function_10_1835")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1873")

    #C0050
    ChrTalk(
        0x9,
        (
            "……またのご来店を\x01",
            "お待ちしております。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8E")

    label("loc_1873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19AE")

    #C0051
    ChrTalk(
        0x9,
        (
            "あちらのショーウィンドウに\x01",
            "展示されているのは『聖女の涙』と\x01",
            "呼ばれるネックレスです。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "中世の時代の遺跡から発掘された\x01",
            "当時のクロスベル領主の持ち物を、\x01",
            "特別に展示させていただいています。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "便宜上値段をつけてはいますが、\x01",
            "販売することはできません。\x01",
            "念のため、ご承知くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A66")

    label("loc_19AE")


    #C0054
    ChrTalk(
        0x9,
        (
            "あちらのショーウィンドウに\x01",
            "展示されているのは『聖女の涙』と\x01",
            "呼ばれるネックレスです。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "便宜上値段をつけてはいますが、\x01",
            "販売することはできません。\x01",
            "念のため、ご承知くださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A66")

    Jump("loc_1B8E")

    label("loc_1A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1B8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1C")

    #C0056
    ChrTalk(
        0x9,
        "先ほどは大変失礼いたしました。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "今後は特別会員として\x01",
            "丁重におもてなしさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "何かありましたらご遠慮なく\x01",
            "お申し付け下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B8E")

    label("loc_1B1C")


    #C0059
    ChrTalk(
        0x9,
        (
            "今後は特別会員として\x01",
            "丁重におもてなしさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "何かありましたらご遠慮なく\x01",
            "お申し付け下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8E")

    TalkEnd(0xFE)
    Return()

    # Function_10_1835 end

    def Function_11_1B92(): pass

    label("Function_11_1B92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1BA3")
    Jump("loc_1D0F")

    label("loc_1BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1BB1")
    Jump("loc_1D0F")

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1D0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C91")

    #C0061
    ChrTalk(
        0xA,
        (
            "多くの七耀石が発掘される、\x01",
            "マインツ鉱山を擁するクロスベル……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        (
            "この店においてある宝飾品……\x01",
            "特に七耀石細工においては\x01",
            "高品質なものが並んでいるようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        "ふむ、さすがと言ったところだな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D0F")

    label("loc_1C91")


    #C0064
    ChrTalk(
        0xA,
        (
            "この店の七耀石細工は\x01",
            "高品質なものが並んでいるようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "さすがはマインツ鉱山を擁する\x01",
            "クロスベル、と言ったところだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0F")

    TalkEnd(0xFE)
    Return()

    # Function_11_1B92 end

    def Function_12_1D13(): pass

    label("Function_12_1D13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1D24")
    Jump("loc_1D97")

    label("loc_1D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1D32")
    Jump("loc_1D97")

    label("loc_1D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1D97")

    #C0066
    ChrTalk(
        0xB,
        "フフ、しかたないなあ。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xB,
        (
            "君のためなら\x01",
            "ネックレスの一つや二つ、\x01",
            "造作もないことだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D97")

    TalkEnd(0xFE)
    Return()

    # Function_12_1D13 end

    def Function_13_1D9B(): pass

    label("Function_13_1D9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1E9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E10")

    #C0068
    ChrTalk(
        0xC,
        "ふふ、先程はごめんあそばせ。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        (
            "私たち、これでも\x01",
            "愛するダーリンがおりますので。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E95")

    label("loc_1E10")


    #C0070
    ChrTalk(
        0xC,
        (
            "ええ、最近は帝国方面にも\x01",
            "よく顔を出していますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "この店ほど良質な宝飾を\x01",
            "多数取り揃えている店は\x01",
            "なかなかありませんわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E95")

    Jump("loc_1F11")

    label("loc_1E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1EA8")
    Jump("loc_1F11")

    label("loc_1EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1F11")

    #C0072
    ChrTalk(
        0xC,
        (
            "このネックレス、\x01",
            "なかなかステキじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        (
            "ねえダーリン、\x01",
            "私にプレゼントしてくれない？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F11")

    TalkEnd(0xFE)
    Return()

    # Function_13_1D9B end

    def Function_14_1F15(): pass

    label("Function_14_1F15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2005")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F90")

    #C0074
    ChrTalk(
        0xD,
        "多少の火遊びは魅力的ですけど……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xD,
        (
            "やはり、淑女たるもの貞淑さが\x01",
            "大事だと思いますの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2000")

    label("loc_1F90")


    #C0076
    ChrTalk(
        0xD,
        (
            "ふふ、確かに\x01",
            "それは言えていますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xD,
        (
            "やはりクロスベル産の七耀石細工は、\x01",
            "他国にも引けをとりませんの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2000")

    Jump("loc_2094")

    label("loc_2005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_208B")

    #C0078
    ChrTalk(
        0xD,
        (
            "アタシに相応しい宝飾品、\x01",
            "なかなか見つからないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xD,
        (
            "ま、宝石との出会いは一期一会……\x01",
            "気長に探すとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2094")

    label("loc_208B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2094")

    label("loc_2094")

    TalkEnd(0xFE)
    Return()

    # Function_14_1F15 end

    def Function_15_2098(): pass

    label("Function_15_2098")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 0, 0, -3000, 0)
    SetChrPos(0x104, 0, 0, -3000, 0)
    SetChrPos(0x105, 0, 0, -3000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(2140, 400, 4920, 0)
    MoveCamera(312, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25520, 0)
    FadeToBright(1000, 0)
    OP_68(-380, 400, 2640, 5000)
    BeginChrThread(0x101, 3, 0, 16)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 18)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x1)
    OP_0D()

    #C0080
    ChrTalk(
        0x101,
        "#00005Fここは……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#6P#10300F確か、会員制の宝飾店だね。\x02\x03",

            "#10304F僕はクラブのお客さんと一緒に\x01",
            "何度か入ったことがあるかな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_22B7")

    #C0082
    ChrTalk(
        0x104,
        (
            "#6P#00306F確か、俺たちが前に来たときは\x01",
            "店の前で追い返されたんだよな。\x02\x03",

            "#00301Fあの店員の態度が\x01",
            "微妙にムカついたっつーか。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#11P#00000Fああ、そういえば今回は\x01",
            "止められなかったけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2340")

    label("loc_22B7")


    #C0084
    ChrTalk(
        0x104,
        (
            "#6P#00306F一見さんお断りってワケか……\x01",
            "なんか感じ悪ィ話だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#11P#00005Fあれ、ということは俺たちって\x01",
            "入っちゃマズいんじゃ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2340")

    OP_68(-3330, 400, 5840, 2500)
    OP_6F(0x1)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0x87, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)

    #N0086
    NpcTalk(
        0x9,
        "店員",
        "お客様。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 19)
    Sleep(50)
    OP_68(-2610, 600, 2290, 3000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(2000)

    def lambda_23E4():

        label("loc_23E4")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_23E4")

    QueueWorkItem2(0x101, 2, lambda_23E4)

    def lambda_23F6():

        label("loc_23F6")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_23F6")

    QueueWorkItem2(0x104, 2, lambda_23F6)

    def lambda_2408():

        label("loc_2408")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2408")

    QueueWorkItem2(0x105, 2, lambda_2408)
    WaitChrThread(0x9, 3)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x105, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_2462")

    #C0087
    ChrTalk(
        0x105,
        "#12P#10300Fフフ、噂をすれば何とやらだね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_247F")

    label("loc_2462")


    #C0088
    ChrTalk(
        0x101,
        "#12P#00011Fうわっと……\x02",
    )

    CloseMessageWindow()

    label("loc_247F")


    #C0089
    ChrTalk(
        0x9,
        (
            "#5P宝飾店《ディアマンテ》へ\x01",
            "ようこそいらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "#5P……失礼ですがお客様。\x01",
            "どなたかからの紹介状は\x01",
            "お持ちでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#12P#00005Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x105,
        "#12P#10300F残念ながら、紹介状はないねえ。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        "#5Pでは入店はお控えくださいませ。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "#5P当店は選ばれたお客さま限定の\x01",
            "会員制となっておりますので。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0095
    ChrTalk(
        0x104,
        (
            "#00306Fチッ、しゃあねえ……\x01",
            "出直すとしようぜ、ロイド。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0096
    ChrTalk(
        0x101,
        (
            "#12P#00012Fそうだな、ビーチで\x01",
            "待ち合わせもしてることだし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0097
    ChrTalk(
        0x9,
        "#5Pロイド様……？\x02",
    )

    CloseMessageWindow()

    def lambda_2680():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2680)
    Sleep(50)

    def lambda_2690():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2690)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    #C0098
    ChrTalk(
        0x9,
        (
            "#5P……お客様。\x01",
            "もしや『特務支援課』の方々で\x01",
            "いらっしゃいますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0099
    ChrTalk(
        0x101,
        "#12P#00005Fええ、そうですけど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0100
    ChrTalk(
        0x9,
        "#5P#4Sしっ、失礼しました！#3S\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        "#6P#00305Fな、なんだあ？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "#5Pコ、コホン……\x01",
            "先ほどマリアベル様から、\x01",
            "連絡がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "#5P本日は特別に、皆様方の入店を\x01",
            "許可するようにとのことです。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        "#5Pどうかご無礼をお許しください。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#12P#00000Fえっと、ということは……\x01",
            "俺たちも利用できるってことですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "#5P左様、今後は特別会員として\x01",
            "丁重におもてなしさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "#5Pそれでは、何かありましたら\x01",
            "お申し付け下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 3)
    OP_4C(0x9, 0xFF)

    def lambda_2955():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2955)

    def lambda_2962():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2962)

    def lambda_296F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_296F)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_93(0x105, 0x13B, 0x1F4)

    #C0108
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、どうやらあのお嬢さんが\x01",
            "気を利かせてくれたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x104,
        (
            "#5P#00306Fそれにしたって\x01",
            "変わり身の早え店員だなあ。\x02\x03",

            "#00300Fま、そうと決まれば\x01",
            "ガンガン利用させてもらうとすっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#11P#00012Fはは、どれも高価そうだから\x01",
            "手が出ないかもしれないけどな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x15B, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 800, 0)
    EventEnd(0x5)
    Return()

    # Function_15_2098 end

    def Function_16_2AB5(): pass

    label("Function_16_2AB5")


    def lambda_2ABA():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2ABA)

    def lambda_2AD4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2AD4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2AED():
        OP_95(0xFE, 0, 0, 800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AED)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_2AB5 end

    def Function_17_2B0E(): pass

    label("Function_17_2B0E")


    def lambda_2B13():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B13)

    def lambda_2B2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B2D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2B46():
        OP_95(0xFE, -790, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B46)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_2B0E end

    def Function_18_2B67(): pass

    label("Function_18_2B67")


    def lambda_2B6C():
        OP_95(0xFE, 0, 0, -1440, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B6C)

    def lambda_2B86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B86)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2B9F():
        OP_95(0xFE, 870, 0, -900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B9F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_18_2B67 end

    def Function_19_2BC0(): pass

    label("Function_19_2BC0")


    def lambda_2BC5():
        OP_95(0xFE, -3560, 0, 6930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BC5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x0)

    def lambda_2BEA():
        OP_95(0xFE, -3560, 0, 2870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BEA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_19_2BC0 end

    def Function_20_2C0B(): pass

    label("Function_20_2C0B")

    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_2C17():
        OP_95(0xFE, -3560, 0, 6930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C17)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x0)

    def lambda_2C3C():
        OP_95(0xFE, -6300, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C3C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_20_2C0B end

    def Function_21_2C5D(): pass

    label("Function_21_2C5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x102, -200, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x102, 3, 0, 23)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)

    #C0111
    ChrTalk(
        0x102,
        (
            "#00105Fここが《ディアマンテ》……\x02\x03",

            "#00104Fさすがに綺麗な宝飾品を\x01",
            "たくさん扱ってるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#12P#00000Fああ、エリィは昼間は\x01",
            "ブティックに行ってたんだったな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0113
    ChrTalk(
        0x101,
        (
            "#12P#00005Fあれ、そういえば……\x01",
            "エリィはここの会員じゃないんだな？\x02\x03",

            "#00000Fマリアベルさんの幼馴染だし、\x01",
            "てっきりＶＩＰ扱いかと思ってたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x102,
        (
            "#00106Fうーん、前にベルと来たときは\x01",
            "宝飾店には入らなかったのよね。\x02\x03",

            "#00100Fブティックで服を見ている方が\x01",
            "性に合っている気がするし。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#12P#00009Fはは、なるほど。\x02\x03",

            "#00000Fそれじゃあ、せっかくだし\x01",
            "一緒に色々と見てみようか？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#00102Fええ、そうしましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4810, 1400, 4230, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 4100, 0, 4500, 270)
    SetChrPos(0x102, 4000, 0, 5500, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0117
    ChrTalk(
        0x101,
        (
            "#6P#00000Fネックレスに指輪にブローチ……\x02\x03",

            "#00003F宝飾品といっても色々あるよなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#11P#00100Fふふ、そうね。\x01",
            "どれもなかなか手が出ない\x01",
            "高価な品だけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0119
    ChrTalk(
        0x102,
        (
            "#11P#00102F見て、ロイド。\x01",
            "この指輪なんか素敵だと思わない？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#6P#00005Fどれどれ……\x02\x03",

            "#00000Fうん、確かに……\x01",
            "エリィに似合いそうな気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x102,
        (
            "#11P#00109Fふふ、お世辞なんて\x01",
            "言ってくれなくてもいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#6P#00012Fいやいや、本当だって。\x02\x03",

            "#00003F（値段は俺の給料の\x01",
            "  ３ヶ月分くらいか……\x01",
            "  やっぱり結構するよな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0123
    ChrTalk(
        0x101,
        "#6P#00011F（って、このコーナーって……！）\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    BeginChrThread(0x9, 3, 0, 24)
    WaitChrThread(0x9, 3)

    #C0124
    ChrTalk(
        0x9,
        "お客様、婚約指輪をお探しでしょうか。\x02",
    )

    CloseMessageWindow()

    def lambda_3230():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3230)
    Sleep(50)

    def lambda_3240():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3240)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    #C0125
    ChrTalk(
        0x9,
        (
            "よろしければ、\x01",
            "お見繕いいたしますが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0126
    ChrTalk(
        0x102,
        "#6P#00105F#4Sえ゛。#3S\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#6P#00012Fはは、いや、え～っと……\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x9,
        (
            "おや、お２人は\x01",
            "ご結婚されるのでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "失礼しました、エンゲージリングの\x01",
            "一角を見てらしたので、つい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    #C0130
    ChrTalk(
        0x102,
        (
            "#6P#00112Fえ、あ……！\x02\x03",

            "#00112Fそ、そのっ……ち、違いますから！\x01",
            "私たちはまだそういうんじゃ……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0131
    ChrTalk(
        0x102,
        (
            "#11P#00112Fロ、ロイド、違うからね！？\x02\x03",

            "#00113F別にそういうアピールとかを\x01",
            "しようとしたんじゃなくって……！\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#6P#00012Fわ、分かったから、\x01",
            "そんなに慌てなくても……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "……ふむ、それでは\x01",
            "そういった話はこれから、\x01",
            "と言ったところでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    #C0134
    ChrTalk(
        0x102,
        "#6P#00112Fで、ですからっ……！\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#6P#00012F（はは、あそこまで\x01",
            "  必死に弁明されると、\x01",
            "  それはそれで残念だけど……）\x02\x03",

            "#00004F（……でも、そうだな。\x01",
            "  エリィには色々と助けられてるし。）\x02\x03",

            "#00000F（結婚指輪じゃないにしろ、\x01",
            "  贈り物は充分アリかもしれない。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0136
    ChrTalk(
        0x101,
        (
            "#12P#00000F（この翠耀石のブローチ……\x01",
            "  エリィに似合いそうだな。）\x02\x03",

            "#00003F（値段は……１００００ミラか。\x01",
            "  結構するけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3C9E")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ブローチを購入する\x01",      # 0
            "やめておく\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B19")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    #C0137
    ChrTalk(
        0x101,
        (
            "#6P#00000Fすみません、このブローチを\x01",
            "包んで欲しいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        "おや……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0139
    ChrTalk(
        0x102,
        "#11P#00112Fロ、ロイド……！？\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#6P#00009Fはは、エリィには\x01",
            "日頃から助けてもらってるしさ。\x02\x03",

            "#00000F特別な意味ってわけじゃないけど、\x01",
            "良ければプレゼントさせてくれないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        (
            "#11P#00113F（そ、それって充分に\x01",
            "  特別な意味がありそうな\x01",
            "  感じなんだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        (
            "#6P#00005Fや、やっぱりダメかな？\x01",
            "俺なんかのプレゼントじゃ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    #C0143
    ChrTalk(
        0x102,
        (
            "#11P#00112Fい、いえ、ダメってわけじゃ……\x02\x03",

            "#00104F……コホン。\x01",
            "ありがとう、嬉しいわロイド。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0144
    ChrTalk(
        0x102,
        (
            "#11P#00100Fそうじゃあ、お返しに……\x01",
            "私からもあなたに似合いそうなものを\x01",
            "見繕わせてもらおうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#6P#00005Fえっ、いいのか？\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        (
            "#11P#00100Fふふ、せっかくだし。\x02\x03",

            "#00109Fそれじゃあ、良い物を探してみるから\x01",
            "少し待っててちょうだいね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0147
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドとエリィはそれぞれ\x01",
            "買った宝飾品を店員に包んでもらい、\x01",
            "互いにプレゼントしあうのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x398),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x398, 1)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_3C99")

    label("loc_3B19")


    #C0149
    ChrTalk(
        0x101,
        (
            "#6P#00006F（……さすがにちょっと重いかな。\x01",
            "  今回はやめておくか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#6P#00112F……だ、だから私たちはまだ\x01",
            "恋人同士でもなくって……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x9,
        "は、はあ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0152
    ChrTalk(
        0x102,
        (
            "#11P#00113Fちょ、ちょっとロイド！\x01",
            "あなたも釈明してちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0153
    ChrTalk(
        0x101,
        "#6P#00012Fあ、ああ……分かったよ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドとエリィは\x01",
            "若干気まずさを感じつつも\x01",
            "宝飾店を後にするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3C99")

    Jump("loc_3E48")

    label("loc_3C9E")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0155
    ChrTalk(
        0x101,
        (
            "#12P#00006F（……って、そもそもミラが足りないな。\x01",
            "  残念だけど諦めるしかないか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        (
            "#6P#00112F……だ、だから私たちはまだ\x01",
            "恋人同士でもなくって……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        "は、はあ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0158
    ChrTalk(
        0x102,
        (
            "#11P#00113Fちょ、ちょっとロイド！\x01",
            "あなたも釈明してちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0159
    ChrTalk(
        0x101,
        "#6P#00012Fあ、ああ……分かったよ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドとエリィは\x01",
            "若干気まずさを感じつつも\x01",
            "宝飾店を後にするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3E48")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_2C5D end

    def Function_22_3E58(): pass

    label("Function_22_3E58")


    def lambda_3E5D():
        OP_95(0xFE, 800, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E5D)

    def lambda_3E77():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E77)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3E90():
        OP_95(0xFE, 800, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E90)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_3E58 end

    def Function_23_3EAA(): pass

    label("Function_23_3EAA")


    def lambda_3EAF():
        OP_95(0xFE, -200, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EAF)

    def lambda_3EC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3EC9)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)

    def lambda_3F14():
        OP_95(0xFE, -200, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F14)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_3EAA end

    def Function_24_3F2E(): pass

    label("Function_24_3F2E")


    def lambda_3F33():
        OP_95(0xFE, 4120, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F33)

    def lambda_3F4D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F4D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_3F6D():
        OP_95(0xFE, 4120, 0, 7340, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F6D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_3F2E end

    def Function_25_3F87(): pass

    label("Function_25_3F87")


    def lambda_3F8C():
        OP_95(0xFE, -500, 0, -1500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F8C)

    def lambda_3FA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3FA6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3FBF():
        OP_95(0xFE, -500, 0, -500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FBF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_3F87 end

    def Function_26_3FD9(): pass

    label("Function_26_3FD9")

    OP_93(0xFE, 0xE1, 0x1F4)

    def lambda_3FE5():
        OP_95(0xFE, 650, 0, 8150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FE5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_400A():
        OP_95(0xFE, 650, 0, 6000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_400A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_3FD9 end

    def Function_27_4024(): pass

    label("Function_27_4024")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_404F")
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    Jump("Function_27_4024")

    label("loc_404F")

    Return()

    # Function_27_4024 end

    def Function_28_4050(): pass

    label("Function_28_4050")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_405C():
        OP_95(0xFE, -3800, 0, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_405C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_4081():
        OP_95(0xFE, -3800, 0, 5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4081)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_4050 end

    def Function_29_409B(): pass

    label("Function_29_409B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x103, -200, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x103, 3, 0, 23)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x103, 3)

    #C0161
    ChrTalk(
        0x103,
        (
            "#00205Fここが宝飾店……\x02\x03",

            "#00202Fロイドさん、\x01",
            "見ていってもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#12P#00000Fああ、まだ時間もあるし\x01",
            "大丈夫だと思うよ。\x02\x03",

            "#00012Fそれにしても……\x01",
            "そんなに来たかったんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#00203Fえ、ええまあ……\x01",
            "綺麗なアクセサリなどが\x01",
            "沢山あると聞きましたので。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#12P#00009Fはは、そっか。\x02\x03",

            "#00000Fそれじゃ、一緒に色々と見てみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        "#00209F……はいっ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(70, 1400, 8900, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 500, 0, 8900, 0)
    SetChrPos(0x103, -500, 0, 9000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0166
    ChrTalk(
        0x101,
        (
            "#12P#00005Fこれはまた、\x01",
            "すごいネックレスだな。\x02\x03",

            "#00004F中世の時代の宝飾か……\x01",
            "なんだか歴史を感じるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        "#6P#00205F………………………………\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        "#12P#00005F……えっと、ティオ？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0169
    ChrTalk(
        0x103,
        (
            "#00205F……あ、い、いえ。\x02\x03",

            "#00204Fあまりにも綺麗だったので、\x01",
            "言葉を失ってしまって……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0170
    ChrTalk(
        0x101,
        "#12P#00005F………………………………\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        (
            "#00205F……なんですか？\x01",
            "目がお皿みたいですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#12P#00012Fい、いや……\x01",
            "意外だなと思ってさ。\x02\x03",

            "#00003Fさっきも思ったけど、\x01",
            "ティオがこういう俗っぽいものに\x01",
            "興味を示すなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        (
            "#00211Fわ、私だって、こういうものを\x01",
            "素直に綺麗と思うことはあります。\x02\x03",

            "#00204F……まあ、そうなったのは\x01",
            "ある意味ロイドさんたちのおかげですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#12P#00005Fあ……\x02\x03",

            "#00004F（そうか……考えてみれば\x01",
            "  ティオも年頃の女の子なんだよな。）\x02\x03",

            "（俺たちと最初会った頃は\x01",
            "  ひたすら大人びてる印象だったけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x103,
        "#00205F……ロイドさん？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#12P#00002Fいや、なんでもないよ。\x02\x03",

            "#00004F（そうだな、機嫌をとるって\x01",
            "  わけじゃないけど……）\x02\x03",

            "（ティオに何かプレゼントするのも\x01",
            "  いいかもしれない。）\x02\x03",

            "#00000F（喜んでくれそうなものはと……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0177
    ChrTalk(
        0x101,
        (
            "#5P#00000F（この蒼耀石の髪飾り……\x01",
            "  ティオにぴったり似合いそうだな。）\x02\x03",

            "#00003F（値段は……１００００ミラか。\x01",
            "  結構するけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4F6B")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "髪飾りを購入する\x01",      # 0
            "やめておく\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E19")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x103, 500)

    #C0178
    ChrTalk(
        0x101,
        (
            "#12P#00000Fティオ、そこにある髪飾りを\x01",
            "プレゼントさせてくれないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x103, 0x101, 500)
    Sleep(1000)
    OP_64(0x103)

    #C0179
    ChrTalk(
        0x103,
        "#00205Fえっ……？\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#12P#00012Fはは、さすがに\x01",
            "そこにあるほどのネックレスは\x01",
            "買ってあげられないけど……\x02\x03",

            "#00000Fティオにも女の子らしい\x01",
            "お洒落をして欲しいと思ってさ。\x02\x03",

            "もちろん、特別な意味って\x01",
            "訳じゃないんだけど……どうかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0181
    ChrTalk(
        0x103,
        (
            "#00204F……嬉しいです。\x02\x03",

            "#00200Fですが、一点だけ\x01",
            "言わせてもらっても？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0182
    ChrTalk(
        0x103,
        (
            "#00203F『もちろん、特別な意味じゃない』……\x02\x03",

            "#00211Fそう言い切ってしまうのも、\x01",
            "女性に対してある意味失礼では？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#12P#00005Fえっ、そ、そういうもんかな？\x02\x03",

            "#00002F兄妹の間でプレゼントするくらいに\x01",
            "受けとめてくれればって事なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x103,
        (
            "#00206F……ふう。\x02\x03",

            "#00211Fまあ、今はそのあたりが\x01",
            "落とし所ですかね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0185
    ChrTalk(
        0x101,
        (
            "#12P#00003Fう、うーん……\x01",
            "何がそんなに納得いかないんだ？\x02\x03",

            "#00012Fやっぱり髪飾りじゃなくて\x01",
            "みっしぃグッズがよかったとか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0186
    ChrTalk(
        0x103,
        (
            "#00206F（この人は、本当にもう……）\x02\x03",

            "#00202F……でも、そうですね。\x01",
            "もしよろしければ、わたしからも\x01",
            "ロイドさんにプレゼントさせてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        "#12P#00005Fえっ、いいのか？\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x103,
        (
            "#00202Fええ、せっかくですし。\x02\x03",

            "#00204Fそれでは良さげなものを探してみますので、\x01",
            "少し待っていてください。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドとティオはそれぞれ\x01",
            "買った宝飾品を店員に包んでもらい、\x01",
            "互いにプレゼントしあうのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0190
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x399),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x399, 1)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_4F66")

    label("loc_4E19")


    #C0191
    ChrTalk(
        0x101,
        (
            "#5P#00006F（……やっぱりやめておくか。\x01",
            "  迷惑かもしれないし……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0192
    ChrTalk(
        0x103,
        (
            "#00202F……ロイドさん、\x01",
            "あちらの方も見てみませんか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0193
    ChrTalk(
        0x101,
        (
            "#12P#00012Fあ、ああ分かった。\x01",
            "気の済むまで付き合わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドとティオはひとしきり\x01",
            "ウィンドウショッピングを楽しみ、\x01",
            "宝飾店を後にするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4F66")

    Jump("loc_50E5")

    label("loc_4F6B")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0195
    ChrTalk(
        0x101,
        (
            "#5P#00006F（……って、そもそもミラが足りないな。\x01",
            "  残念だけど諦めるしかないか……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0196
    ChrTalk(
        0x103,
        (
            "#00202F……ロイドさん、\x01",
            "あちらの方も見てみませんか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0197
    ChrTalk(
        0x101,
        (
            "#12P#00012Fあ、ああ分かった。\x01",
            "気の済むまで付き合わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドとティオはひとしきり\x01",
            "ウィンドウショッピングを楽しみ、\x01",
            "宝飾店を後にするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_50E5")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_409B end

    def Function_30_50F5(): pass

    label("Function_30_50F5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x104, -500, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x104, 3, 0, 25)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)

    #C0199
    ChrTalk(
        0x101,
        "#12P#00000F宝飾店に着いたな。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x104,
        (
            "#00300Fよーし、そんじゃさっそく\x01",
            "ロイドのプレゼント探しにでも\x01",
            "付き合うとすっかね。\x02\x03",

            "#00309Fんで、狙いは誰なんだ？\x01",
            "お兄さんに教えてみな。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#12P#00012Fい、いやいや。\x01",
            "だからそんなんじゃないってば。\x02\x03",

            "#00000Fとにかく、少し時間があるし\x01",
            "ブラブラ店内を見てみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x104,
        "#00302Fおう、了解だぜ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(5520, 1400, 8900, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24620, 0)
    SetChrPos(0x101, 5350, 0, 9700, 270)
    SetChrPos(0x104, 4150, 0, 9700, 90)
    SetChrPos(0x9, -900, 0, 9680, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0203
    ChrTalk(
        0x101,
        (
            "#12P#00001Fなんというか……\x02\x03",

            "#00006F見れば見るほど\x01",
            "夜中に男２人で入るような店じゃ\x01",
            "ない気がしてきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x104,
        (
            "#00306Fおいおい、ンな事言ったら\x01",
            "真っ昼間に１人で入った\x01",
            "俺の立場はどうなんだっつの。\x02\x03",

            "#00300Fまあしかし、その意見には同意だぜ。\x01",
            "どうせならテーマパークに行って\x01",
            "ナンパの一つでもしねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        "#12P#00011Fだ、だからそんな時間はないってば。\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x104,
        (
            "#00306Fつーか、水上バスではもともと\x01",
            "そういう話だったじゃねえかよ～。\x02\x03",

            "#00301Fお前って奴は草食っつーかなんつーか……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0207
    ChrTalk(
        0x104,
        (
            "#00302Fよっしゃ、せっかくだからそんなお前に\x01",
            "男前が上がりそうなアクセサリを\x01",
            "プレゼントしてやろうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#12P#00005Fえっ……い、いいのか？\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x104,
        (
            "#00300Fああ、さっき\x01",
            "向こうのショーウィンドウに\x01",
            "お前に似合いそうなのを見かけてよ。\x02\x03",

            "#00309Fハハ、まあお遊びみたいなもんだし\x01",
            "そう気後れするこたぁねえさ。\x02\x03",

            "#00304Fもちろん特別な意味が\x01",
            "あるってわけでもねえしよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0210
    ChrTalk(
        0x101,
        (
            "#12P#00006Fいやいや……\x01",
            "そんなのあっても困るから。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x104,
        (
            "#00302Fハハ、冗談だっつの。\x02\x03",

            "#00304Fそんじゃ、ちょっくら\x01",
            "店員に包んでもらってくるとすっかね。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4210, 1400, 7590, 2000)
    OP_6F(0x79)
    TurnDirection(0x104, 0xC, 500)

    #C0212
    ChrTalk(
        0x104,
        (
            "#11P#00309Fちょうどあそこにいる\x01",
            "セレブのお姉さんたちに、\x01",
            "今夜の約束を取り付けてからな！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 2, 0, 27)
    BeginChrThread(0x104, 3, 0, 26)

    def lambda_57DE():

        label("loc_57DE")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_57DE")

    QueueWorkItem2(0x101, 2, lambda_57DE)
    WaitChrThread(0x104, 3)
    EndChrThread(0x104, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    def lambda_5800():
        TurnDirection(0xC, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5800)
    TurnDirection(0xD, 0x104, 500)
    EndChrThread(0x101, 0xFF)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0213
    ChrTalk(
        0x101,
        (
            "#12P#00012Fはは、やれやれ……\x02\x03",

            "#00004F（でも、あの面倒見のよさには\x01",
            "  俺たち全員が助けられてるよな。）\x02\x03",

            "（支援課のリーダーとして、\x01",
            "  感謝の気持ちを表したいし……）\x02\x03",

            "#00000F（せっかく宝飾店に来たんだし、\x01",
            "  俺も思い切ってなにか探してみるか。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0214
    ChrTalk(
        0x101,
        (
            "#5P#00000F（この紅耀石のついたブレスレット……\x01",
            "  ランディに似合うかもな。）\x02\x03",

            "#00003F（値段は……１００００ミラか。\x01",
            "  結構するけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5CE6")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ブレスレットを購入する\x01",      # 0
            "やめておく\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BA6")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    #C0215
    ChrTalk(
        0x101,
        (
            "#12P#00000Fあの、すみません。\x01",
            "このブレスレットが欲しいんですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4B(0x9, 0xFF)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    #C0216
    ChrTalk(
        0x9,
        "#5Pは、ただいま。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0217
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドはナンパに失敗して\x01",
            "肩をすくめているランディを冗談交じりに慰め……\x02\x03",

            "買った宝飾品を店員に包んでもらい、\x01",
            "互いにプレゼントしあうのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_5CE1")

    label("loc_5BA6")


    #C0218
    ChrTalk(
        0x101,
        (
            "#5P#00006F（……なんだか気恥ずかしいし\x01",
            "  やっぱりやめておこう。）\x02\x03",

            "#00000F（ランディへの感謝の気持ちは\x01",
            "  後日改めて、別の形で示さないとな。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドはナンパに失敗して\x01",
            "肩をすくめているランディを冗談交じりに慰め……\x02\x03",

            "ランディから宝飾品を贈られてから、\x01",
            "宝飾店を後にするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5CE1")

    Jump("loc_5E2B")

    label("loc_5CE6")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0220
    ChrTalk(
        0x101,
        (
            "#5P#00006F（……って、そもそもミラが足りないな。）\x02\x03",

            "#00008F（申し訳ないけどこっちから贈るのは\x01",
            "  諦めたほうがよさそうだ……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドはナンパに失敗して\x01",
            "肩をすくめているランディを冗談交じりに慰め……\x02\x03",

            "ランディから宝飾品を贈られてから、\x01",
            "宝飾店を後にするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5E2B")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0222
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x39A, 1)
    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_50F5 end

    def Function_31_5E76(): pass

    label("Function_31_5E76")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x109, -200, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x109, 3, 0, 23)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x109, 3)

    #C0223
    ChrTalk(
        0x109,
        (
            "#10108Fうーん、昼間フランと一緒に\x01",
            "一通り見て回りましたけど……\x02\x03",

            "#10106Fはあ、やっぱり\x01",
            "場違いな気がするなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#12P#00012Fそもそもマリアベルさんの\x01",
            "口利きがなかったら、\x01",
            "入れないような店だしな。\x02\x03",

            "#00000Fまあ、せっかくだし\x01",
            "今度は俺と一緒に回ってみないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x109,
        "#10100Fええ、お付き合いさせていただきます！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6510, 1400, 6990, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 6000, 0, 8500, 90)
    SetChrPos(0x109, 6000, 0, 7200, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0226
    ChrTalk(
        0x109,
        "#5P#10103Fう～ん……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    #C0227
    ChrTalk(
        0x101,
        "#00005Fどうした、ノエル？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0228
    ChrTalk(
        0x109,
        (
            "#6P#10101Fいえ、さっきから色々と\x01",
            "見て思ったんですけど……\x02\x03",

            "#10106Fなんだか宝飾品って\x01",
            "ムダが多くありませんか？\x02\x03",

            "#10108Fつけてるとやたらと\x01",
            "動きにくそうですし、\x01",
            "仕事にも支障が……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    #C0229
    ChrTalk(
        0x109,
        (
            "#6P#10111Fあっ、す、すみません！\x01",
            "せっかく楽しく見ていたのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        (
            "#00012Fはは……いや、なんだか\x01",
            "ノエルらしい意見だな。\x02\x03",

            "#00000Fそういえばノエルの私服って\x01",
            "動きやすそうだもんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x109,
        (
            "#6P#10109Fあはは……\x01",
            "その点は結構重視して\x01",
            "選んでいる気がします。\x02\x03",

            "#10106F１人で選ぶとどうも\x01",
            "マニッシュになりがちで\x01",
            "困っちゃうんですけどね。\x02\x03",

            "#10100Fだからいつもはフランに頼んで、\x01",
            "コーディネートしてもらったり……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00009Fはは、なるほど。\x02\x03",

            "#00000Fそれじゃあ、この店だと\x01",
            "気に入りそうなものはないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x109,
        "#6P#10100Fそうですねえ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x109, 0x87, 0x1F4)
    Sleep(500)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0234
    ChrTalk(
        0x109,
        (
            "#5P#10102Fあ、この琥耀石の\x01",
            "はまったチョーカー……\x02\x03",

            "#10109F昼間、フランと一緒に見てから\x01",
            "ちょっといいなって\x01",
            "思ってたんですよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#00002Fはは、確かにノエルに似合いそうだな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0236
    ChrTalk(
        0x101,
        (
            "#00000F（そうだな、せっかく一緒に来たんだし、\x01",
            "  プレゼントしてもいいかもしれない。）\x02\x03",

            "#00003F（値段は……１００００ミラか。\x01",
            "  結構するけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6BFF")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "チョーカーを購入する\x01",      # 0
            "やめておく\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A70")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0237
    ChrTalk(
        0x101,
        (
            "#00000Fノエル、このチョーカー……\x01",
            "君にプレゼントさせてくれないか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0238
    ChrTalk(
        0x109,
        "#6P#10105Fえ…………\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0239
    ChrTalk(
        0x109,
        "#6P#10111Fえええええええっ！？\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#00005Fあ、もしかして迷惑だったかな？\x02\x03",

            "#00004F君は支援課の出向を頑張ってるし、\x01",
            "その労いを込めてだから\x01",
            "特別な意味とかじゃないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x109,
        (
            "#6P#10111Fえ、えーっと……いえその！！\x01",
            "嬉しいのは嬉しいんですけどっ……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        "#00005Fな、何か問題でもあるのか？\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x109,
        (
            "#6P#10112F……い、いえ！！\x01",
            "そういうわけでは……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x109)

    #C0244
    ChrTalk(
        0x109,
        (
            "#6P#10101F……で、では！\x01",
            "せっかくの申し出ですし、\x01",
            "謹んでお受けさせて頂きます！\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        "#00012Fはは、そんなに畏まらなくても……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x109,
        (
            "#6P#10106Fい、いえ……\x01",
            "やっぱり申し訳ないですし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0247
    ChrTalk(
        0x109,
        (
            "#6P#10103Fそうだ、それなら……\x02\x03",

            "#10100Fあたしからもロイドさんに\x01",
            "何かプレゼントさせてもらえませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x101,
        "#00005Fえっ、いいのか？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x109,
        (
            "#6P#10109Fはい、せっかくですし。\x02\x03",

            "#10100F良さそうなものを探してみますから、\x01",
            "ちょっとだけ待っててください。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0250
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドとノエルはそれぞれ\x01",
            "買った宝飾品を店員に包んでもらい、\x01",
            "互いにプレゼントしあうのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0251
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x39B, 1)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_6BFA")

    label("loc_6A70")


    #C0252
    ChrTalk(
        0x101,
        (
            "#00006F（……うーん、やっぱりやめとくか。\x01",
            "  フランとかにも誤解を生みそうだし……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0253
    ChrTalk(
        0x109,
        "#6P#10105Fロイドさん、どうかしました？\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00004Fああいや、なんでもないよ。\x02\x03",

            "#00000F他にも気に入りそうなものがないか\x01",
            "色々と見てみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x109,
        "#6P#10102Fええ、そうですね！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0256
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドはノエルとひとしきり\x01",
            "ウィンドウショッピングを楽しみ、\x01",
            "宝飾店を後にするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6BFA")

    Jump("loc_6DA2")

    label("loc_6BFF")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0257
    ChrTalk(
        0x101,
        (
            "#00006F（……って、そもそもミラが足りないな。\x01",
            "  残念だけど諦めるしかないか……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0258
    ChrTalk(
        0x109,
        "#6P#10105Fロイドさん、どうかしました？\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#00004Fああいや、なんでもないよ。\x02\x03",

            "#00000F他にも気に入りそうなものがないか\x01",
            "色々と見てみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x109,
        "#6P#10102Fええ、そうですね！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0261
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドはノエルとひとしきり\x01",
            "ウィンドウショッピングを楽しみ、\x01",
            "宝飾店を後にするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6DA2")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_5E76 end

    def Function_32_6DB2(): pass

    label("Function_32_6DB2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(990, 1400, -1000, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 800, 0, -4000, 0)
    SetChrPos(0x105, -500, 0, -4000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x105, 3, 0, 25)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x105, 3)

    #C0262
    ChrTalk(
        0x101,
        "#12P#00000Fさてと、宝飾店に来てみたけど。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x105,
        (
            "#10300F晩餐会までは時間があるし、\x01",
            "一緒に見ていくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#12P#00002Fああ、せっかくだし\x01",
            "それもいいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、決まりだ。\x01",
            "それじゃあ一通り回ってみようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6510, 1400, 6990, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 6000, 0, 8100, 90)
    SetChrPos(0x105, 6000, 0, 6900, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0266
    ChrTalk(
        0x101,
        (
            "#00003Fうーん、会員制なだけあって\x01",
            "やっぱり高価なものが揃ってるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、せっかくだし、\x01",
            "あとでキーアに指輪でも\x01",
            "贈ってみるといいかもしれないね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0268
    ChrTalk(
        0x101,
        (
            "#00006Fこらこら、\x01",
            "子供に与えるものじゃないだろ。\x02\x03",

            "#00005F……そういえばワジって、\x01",
            "支援課に入る前から\x01",
            "随分と羽振りがいいよな。\x02\x03",

            "#00003F戦術オーブメントなんかも\x01",
            "会った時から持ってたみたいだし……\x02\x03",

            "#00000F下世話な話だけど、\x01",
            "ホストクラブってやっぱり\x01",
            "かなり儲かるのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0269
    ChrTalk(
        0x105,
        (
            "#6P#10300Fいや？　僕は所詮バイトだし、\x01",
            "たまに手伝うくらいだから\x01",
            "実際の給料は大したことないよ。\x02\x03",

            "#10304Fクラブではどちらかというと、\x01",
            "給料とは別の臨時収入#8R㈲　㈲　㈲　㈲#が多くなるかな。\x02\x03",

            "#10302Fセレブなマダムから\x01",
            "お小遣い代わりに宝石を渡される、\x01",
            "なんてことがたまにあるしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#00003F……な、なるほど。\x01",
            "あまり感心できないけど、\x01",
            "そういうのが資金源になって……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、いやいや。\x01",
            "お客さんにもらったものを\x01",
            "換金するなんてことはしないよ？\x02\x03",

            "#10304F前に持ってたエニグマも、\x01",
            "アシュリーさんの店から\x01",
            "自分のミラで仕入れたものだしね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0272
    ChrTalk(
        0x101,
        (
            "#00005F……じゃあ、結局そのミラは\x01",
            "どこから出てるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x105,
        "#6P#10309Fフフ、それは企業秘密。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0274
    ChrTalk(
        0x101,
        "#00006Fな、なんじゃそりゃ……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、まあそんな\x01",
            "どうでもいいことは置いといて……\x02\x03",

            "#10302Fロイド、よかったらこれを\x01",
            "受け取ってくれるかい？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0276
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x39C, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0277
    ChrTalk(
        0x101,
        "#00005Fこれって……\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x105,
        (
            "#6P#10300Fついさっき\x01",
            "向こうのショーケースで\x01",
            "見つけたアクセサリでね。\x02\x03",

            "#10304F君に似合いそうだと思ったから\x01",
            "せっかくだし買っておいたってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#00006Fい、いつの間に……\x02\x03",

            "#00005Fでも、こんな高価そうなものを\x01",
            "本当にもらっていいのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、単なる気まぐれだし\x01",
            "そう難しく考えなくていいよ。\x02\x03",

            "#10309Fこの程度で君に恩が売れるなら\x01",
            "安いものだしね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0281
    ChrTalk(
        0x101,
        (
            "#00006Fこ、こらこら……\x02\x03",

            "#00000Fでもまあ、ありがとな。\x01",
            "お礼を言わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x105,
        "#6P#10300Fフフ、どういたしまして。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x101,
        (
            "#00000F（……そうだな、\x01",
            "　もらってばかりもなんだし……）\x02\x03",

            "#00004F（こっちからも何かお返しするのも\x01",
            "  いいかもしれないな。）\x02\x03",

            "#00000F（ワジが来たおかげで、\x01",
            "  支援課の柔軟性もある意味増したし、\x01",
            "　そのお礼の意味も込めて……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0284
    ChrTalk(
        0x101,
        (
            "#00000F（この金耀石のペンダントなら、\x01",
            "  ワジに似合うかもしれない。）\x02\x03",

            "#00003F（値段は……１００００ミラか。\x01",
            "  結構するけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7CE6")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ペンダントを購入する\x01",      # 0
            "やめておく\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B6F")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0285
    ChrTalk(
        0x101,
        (
            "#00000Fそれなら、お返しに\x01",
            "このペンダントを贈らせてくれないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x2D, 0x1F4)

    #C0286
    ChrTalk(
        0x105,
        (
            "#6P#10305Fへえ、いいのかい？\x02\x03",

            "#10300Fフフ、君のセンスも\x01",
            "なかなか悪くないじゃない。\x02\x03",

            "#10302F贈り物としてはチープだけど、\x01",
            "まあ及第点じゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#00006Fあのな……\x01",
            "いらないなら買わないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x105,
        (
            "#6P#10309Fアハハ、とんでもない。\x02\x03",

            "#10302F君が一所懸命に選んでくれたものだし、\x01",
            "ありがたく受け取らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        (
            "#00002F……はは、まあいいや。\x01",
            "店員さんを呼んでこよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0290
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドは\x01",
            "買った宝飾品を店員に包んでもらい、\x01",
            "ワジにプレゼントするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x158, 7)
    Jump("loc_7CE1")

    label("loc_7B6F")


    #C0291
    ChrTalk(
        0x101,
        (
            "#00006F（……やっぱり今回はやめとくかな。\x01",
            "　別の機会に埋め合わせをしよう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x105,
        "#6P#10305Fおや、どうしたんだい？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0293
    ChrTalk(
        0x101,
        (
            "#00004Fいや、なんでもないさ。\x02\x03",

            "#00000F待ち合わせまで少し時間があるし、\x01",
            "店内を見ていようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x105,
        "#6P#10302Fフフ、了解。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドはワジとひとしきり\x01",
            "ウィンドウショッピングを楽しみ、\x01",
            "宝飾店を後にするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7CE1")

    Jump("loc_7E77")

    label("loc_7CE6")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0296
    ChrTalk(
        0x101,
        (
            "#00006F（……って、そもそもミラが足りないな。\x01",
            "  残念だけど諦めるしかないか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        "#6P#10305Fおや、どうしたんだい？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0298
    ChrTalk(
        0x101,
        (
            "#00004Fいや、なんでもないさ。\x02\x03",

            "#00000F待ち合わせまで少し時間があるし、\x01",
            "店内を見ていようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x105,
        "#6P#10302Fフフ、了解。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0300
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドはワジとひとしきり\x01",
            "ウィンドウショッピングを楽しみ、\x01",
            "宝飾店を後にするのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7E77")

    SetScenarioFlags(0x15B, 3)
    SetScenarioFlags(0x22, 1)
    NewScene("t102B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_32_6DB2 end

    SaveToFile()

Try(main)
