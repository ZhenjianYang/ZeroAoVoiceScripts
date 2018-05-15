from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1650.bin",                # FileName
        "t1650",                    # MapName
        "t1650",                    # Location
        0x0058,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 50500, 0, 50000, 90, 0, 1, 88, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1650",                  # 0
        "ヨアヒム准教授",         # 1
        "丸イス",                 # 2
        "パイプイス",             # 3
        "パイプイス",             # 4
        "パイプイス",             # 5
        "パイプイス",             # 6
        "教授イス",               # 7
    ))

    AddCharChip((
        "chr/ch07102.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
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

    DeclNpc(110690,  150,     57000,   270,  469,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(109380,  0,       57000,   1500,    110690,  1500,    57000,   0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_258",          # 00, 0
        "Function_1_310",          # 01, 1
        "Function_2_371",          # 02, 2
        "Function_3_3E9",          # 03, 3
        "Function_4_3ED",          # 04, 4
        "Function_5_9E3",          # 05, 5
        "Function_6_B33",          # 06, 6
        "Function_7_B8C",          # 07, 7
        "Function_8_BE5",          # 08, 8
        "Function_9_C3E",          # 09, 9
        "Function_10_C7B",         # 0A, 10
        "Function_11_CD0",         # 0B, 11
        "Function_12_E2B",         # 0C, 12
        "Function_13_10DC",        # 0D, 13
        "Function_14_34E0",        # 0E, 14
        "Function_15_3517",        # 0F, 15
        "Function_16_3582",        # 10, 16
        "Function_17_3824",        # 11, 17
        "Function_18_385F",        # 12, 18
        "Function_19_3893",        # 13, 19
        "Function_20_5792",        # 14, 20
        "Function_21_5793",        # 15, 21
        "Function_22_57CE",        # 16, 22
        "Function_23_5809",        # 17, 23
        "Function_24_5844",        # 18, 24
    ))


    def Function_0_258(): pass

    label("Function_0_258")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_298"),
        (1, "loc_2A4"),
        (2, "loc_2B0"),
        (3, "loc_2BC"),
        (4, "loc_2C8"),
        (5, "loc_2D4"),
        (6, "loc_2E0"),
        (SWITCH_DEFAULT, "loc_2EC"),
    )


    label("loc_298")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2A4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2B0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2BC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2C8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2D4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_2F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F8")

    label("loc_30F")

    Return()

    # Function_0_258 end

    def Function_1_310(): pass

    label("Function_1_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_31E")
    Jump("loc_34D")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_331")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_34D")

    label("loc_331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_33F")
    Jump("loc_34D")

    label("loc_33F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_34D")
    ClearChrFlags(0x8, 0x80)

    label("loc_34D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_361")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)
    Jump("loc_370")

    label("loc_361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_370")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 19)

    label("loc_370")

    Return()

    # Function_1_310 end

    def Function_2_371(): pass

    label("Function_2_371")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_383")
    Jump("loc_3B0")

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_395")
    OP_66(0x0, 0x1)
    Jump("loc_3B0")

    label("loc_395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3A3")
    Jump("loc_3B0")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_3B0")
    OP_66(0x0, 0x1)

    label("loc_3B0")

    OP_1B(0x1, 0x0, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D1")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_3E8")

    label("loc_3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E8")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_3E8")

    Return()

    # Function_2_371 end

    def Function_3_3E9(): pass

    label("Function_3_3E9")

    Call(0, 4)
    Return()

    # Function_3_3E9 end

    def Function_4_3ED(): pass

    label("Function_4_3ED")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_481")
    Jump("loc_4CB")

    label("loc_481")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A1")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB")

    label("loc_4A1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C1")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB")

    label("loc_4C1")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CB")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4FE")
    Jump("loc_9DB")

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_6D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D")

    #C0001
    ChrTalk(
        0x8,
        (
            "#2410Fこの錠剤が噂の《グノーシス》か、\x01",
            "はたまた全く別の薬なのか……\x02\x03",

            "#2400F不謹慎かもしれないが\x01",
            "薬学の研究者としても\x01",
            "非常に興味が沸いたよ。\x02\x03",

            "#2401Fとにかく、この蒼い錠剤については\x01",
            "最善を尽くして調べさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x103,
        "#0208F……………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6D2")

    label("loc_61D")


    #C0003
    ChrTalk(
        0x8,
        (
            "#2403F悪魔の力を借りる謎の秘薬……\x01",
            "この薬が本当に《グノーシス》かどうかは\x01",
            "調べてみないと分からない。\x02\x03",

            "#2401Fとにかく、この蒼い錠剤については\x01",
            "最善を尽くして調べさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D2")

    Jump("loc_9DB")

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6E5")
    Jump("loc_9DB")

    label("loc_6E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_END)), "loc_9DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_948")

    #C0004
    ChrTalk(
        0x8,
        (
            "#2400Fキーア君も嫌がっているようだし\x01",
            "検査入院は見送った方がよさそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0006Fすみませんでした……\x01",
            "せっかく相談に乗って頂いたのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#2404Fハハ、気にする事はない。\x02\x03",

            "#2405Fそんなことより、\x01",
            "早くキーア君を追いかけた方が\x01",
            "いいんじゃないかな？\x02\x03",

            "このウルスラ病院は結構広いから\x01",
            "迷子になると大変だよ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_88C")

    #C0007
    ChrTalk(
        0x102,
        (
            "#0108Fそうね……急いだほうがいいかも。\x01",
            "キーアちゃん、怒ってたみたいだし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91C")

    label("loc_88C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_8E2")

    #C0008
    ChrTalk(
        0x103,
        (
            "#0203F確かに……\x01",
            "病院の人に迷惑をかける前に\x01",
            "探した方がいいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91C")

    label("loc_8E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_91C")

    #C0009
    ChrTalk(
        0x104,
        (
            "#0300Fちゃっちゃと見つけて\x01",
            "謝っちまおうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91C")


    #C0010
    ChrTalk(
        0x101,
        "#0000Fああ、それじゃあ行くか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9DB")

    label("loc_948")


    #C0011
    ChrTalk(
        0x8,
        (
            "#2400F今後、キーアくんの気が\x01",
            "変わらないとも限らないし、\x01",
            "検査の準備だけはしておこう。\x02\x03",

            "何かあったら相談に乗るから\x01",
            "いつでも連絡してくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DB")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_4_3ED end

    def Function_5_9E3(): pass

    label("Function_5_9E3")

    EventBegin(0x2)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(0, 0)
    MenuCmd(1, 0, "【研究棟から出る】")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A51"),
        (1, "loc_A60"),
        (2, "loc_A8D"),
        (SWITCH_DEFAULT, "loc_A9C"),
    )


    label("loc_A51")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A9C")

    label("loc_A60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A88")

    label("loc_A7E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A88")

    Jump("loc_A9C")

    label("loc_A8D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A9C")

    label("loc_A9C")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_AB8"),
        (1, "loc_AFF"),
        (2, "loc_B1A"),
        (SWITCH_DEFAULT, "loc_B32"),
    )


    label("loc_AB8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD9")
    Call(0, 16)
    Jump("loc_AFA")

    label("loc_AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEF")
    Call(0, 20)
    Jump("loc_AFA")

    label("loc_AEF")

    EventEnd(0x5)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()

    label("loc_AFA")

    Jump("loc_B32")

    label("loc_AFF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("t1620", 114, 0, 0)
    IdleLoop()
    Jump("loc_B32")

    label("loc_B1A")

    SetChrPos(0x0, 100500, 0, 50000, 90)
    EventEnd(0x5)
    Jump("loc_B32")

    label("loc_B32")

    Return()

    # Function_5_9E3 end

    def Function_6_B33(): pass

    label("Function_6_B33")


    def lambda_B38():
        OP_95(0xFE, -4460, 0, 90610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B38)

    def lambda_B52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B52)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_B6B():
        OP_95(0xFE, -7820, 0, 90540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_6_B33 end

    def Function_7_B8C(): pass

    label("Function_7_B8C")


    def lambda_B91():
        OP_95(0xFE, -4460, 0, 90610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B91)

    def lambda_BAB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BAB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_BC4():
        OP_95(0xFE, -5900, 0, 89580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_7_B8C end

    def Function_8_BE5(): pass

    label("Function_8_BE5")


    def lambda_BEA():
        OP_95(0xFE, -4460, 0, 90610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BEA)

    def lambda_C04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C04)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_C1D():
        OP_95(0xFE, -6530, 0, 90480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C1D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_8_BE5 end

    def Function_9_C3E(): pass

    label("Function_9_C3E")


    def lambda_C43():
        OP_95(0xFE, -6720, 0, 95640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C43)
    WaitChrThread(0xFE, 1)

    def lambda_C61():
        OP_95(0xFE, -1680, 0, 99810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C61)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_C3E end

    def Function_10_C7B(): pass

    label("Function_10_C7B")


    def lambda_C80():
        OP_95(0xFE, 57520, 0, 58790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C80)
    WaitChrThread(0xFE, 1)

    def lambda_C9E():
        OP_95(0xFE, 59520, 0, 58790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C9E)
    Sleep(500)

    def lambda_CBB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CBB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_10_C7B end

    def Function_11_CD0(): pass

    label("Function_11_CD0")

    OP_68(-5980, 1700, 90160, 0)
    MoveCamera(55, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -2320, 0, 90910, 270)
    SetChrPos(0xEF, -2320, 0, 90910, 270)
    SetChrPos(0x153, -2320, 0, 90910, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(160, 0, 100, 0)
    Sleep(500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    Sleep(500)
    OP_68(-6980, 1700, 90160, 3000)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(1000)
    BeginChrThread(0x153, 3, 0, 8)
    Sleep(1000)
    BeginChrThread(0xEF, 3, 0, 7)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x153, 3)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    OP_6F(0x1)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 9)
    Sleep(750)
    OP_68(-6980, 2700, 90160, 6000)
    BeginChrThread(0x153, 3, 0, 9)
    Sleep(325)
    BeginChrThread(0xEF, 3, 0, 9)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x153, 0x1)
    EndChrThread(0x101, 0x3)
    EndChrThread(0xEF, 0x3)
    EndChrThread(0x153, 0x3)
    Sleep(1000)
    Return()

    # Function_11_CD0 end

    def Function_12_E2B(): pass

    label("Function_12_E2B")

    FadeToBright(1000, 0)
    OP_68(56390, 1400, 57940, 0)
    MoveCamera(47, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21940, 0)
    SetCameraDistance(20900, 3000)
    SetChrPos(0x101, 57020, 0, 58790, 90)
    SetChrPos(0xEF, 56370, 0, 60220, 135)
    SetChrPos(0x153, 55430, 0, 58580, 90)
    OP_6F(0x10)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   薬学・神経科研究室\x01",
            "ヨアヒム・ギュンター准教授\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)

    #C0013
    ChrTalk(
        0x101,
        (
            "#0005F（ここがそうみたいだな……）\x02\x03",

            "#0003F──失礼します。\x01",
            "支援課のロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 59520, 0, 59900, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    #N0014
    NpcTalk(
        0x8,
        "男性の声",
        "#11P#2Sああ、待っていたよ。\x02",
    )

    CloseMessageWindow()

    #N0015
    NpcTalk(
        0x8,
        "男性の声",
        "#11P#2Sどうぞ、入ってきたまえ。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#0000Fはい。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 110690, 150, 57000, 270)
    TurnDirection(0x101, 0x153, 500)

    #C0017
    ChrTalk(
        0x101,
        "#0000F#11Pキーア、中に入るよ。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x153,
        "#1110F#6Pうんっ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x190)
    Sleep(100)

    def lambda_1057():
        OP_95(0xFE, 57520, 0, 58790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1057)
    WaitChrThread(0x101, 1)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    Sleep(200)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(750)
    BeginChrThread(0x153, 3, 0, 10)
    Sleep(1000)
    BeginChrThread(0xEF, 3, 0, 10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x153, 3)
    Sleep(500)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_12_E2B end

    def Function_13_10DC(): pass

    label("Function_13_10DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 11)
    Call(0, 12)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch08202.itc", 0x22)
    LoadChrToIndex("apl/ch50383.itc", 0x23)
    OP_68(113550, 1250, 51110, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23130, 0)
    SetChrPos(0x101, 108030, 0, 49200, 270)
    SetChrPos(0xEF, 108030, 0, 48000, 270)
    SetChrPos(0x153, 106810, 0, 48600, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02400.itp")
    FadeToBright(1000, 0)
    OP_68(108440, 1250, 57200, 7000)
    OP_6F(0x1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    #C0019
    ChrTalk(
        0x101,
        "#0000F──失礼します。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    def lambda_1237():
        OP_95(0xFE, 108030, 0, 57600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1237)
    Sleep(150)

    def lambda_1254():
        OP_95(0xFE, 106810, 0, 57000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_1254)
    Sleep(50)

    def lambda_1271():
        OP_95(0xFE, 108030, 0, 56400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1271)
    Sleep(3000)
    SetChrSubChip(0x8, 0x0)
    WaitChrThread(0x101, 1)

    def lambda_1296():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1296)
    WaitChrThread(0x153, 1)

    def lambda_12A7():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_12A7)
    WaitChrThread(0xEF, 1)

    def lambda_12B8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_12B8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_13D6")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0020
    AnonymousTalk(
        0x8,
        (
            "やあ、ロイド君。\x01",
            "それにエリィさんだったかな。\x02\x03",

            "記念祭中はどうも。\x01",
            "おかげで中々楽しかったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0021
    ChrTalk(
        0x102,
        (
            "#0102F#6Pふふっ……\x01",
            "先生も相変わらずみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C9")

    label("loc_13D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_14D0")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0022
    AnonymousTalk(
        0x8,
        (
            "やあ、ロイド君。\x01",
            "それにティオ君だったかな。\x02\x03",

            "記念祭中はどうも。\x01",
            "おかげで中々楽しかったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0023
    ChrTalk(
        0x103,
        "#0202F#6P……先生も相変わらずですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15C9")

    label("loc_14D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_15C9")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0024
    AnonymousTalk(
        0x8,
        (
            "やあ、ロイド君。\x01",
            "それにランディ君だったかな。\x02\x03",

            "記念祭中はどうも。\x01",
            "おかげで中々楽しかったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0025
    ChrTalk(
        0x104,
        "#0302F#6Pハハ、先生も相変わらずッスね。\x02",
    )

    CloseMessageWindow()

    label("loc_15C9")


    #C0026
    ChrTalk(
        0x101,
        (
            "#0003F#6Pその、すみません。\x02\x03",

            "#0000Fアポイント無しに\x01",
            "押しかけてしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#2404F#11Pいやいや、ちょうど仕事が\x01",
            "一区切り付いた所だったからね。\x02\x03",

            "#2401Fそれで、記憶喪失の子を\x01",
            "預かったそうだけど……その子が？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0001F#6Pはい……\x01",
            "キーアといいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x153,
        (
            "#1110F#6Pねえねえ、ロイド。\x02\x03",

            "このメガネのおじさんが\x01",
            "キオクを戻してくれるのー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0030
    ChrTalk(
        0x8,
        (
            "#2405F#11Pオ、オジサン！？\x02\x03",

            "#2406F……はは、これでも\x01",
            "若作りなつもりだったが……\x01",
            "やっぱりオジサンだよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#0011F#6Pい、いや、先生はお若いですよ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x153, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1855")

    #C0032
    ChrTalk(
        0x102,
        (
            "#0106F#11P（……キーアちゃん。）\x02\x03",

            "#0100F（こういう時はお世辞にでも\x01",
            "  お兄さんって呼んだ方がいいわ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1936")

    label("loc_1855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_18C6")

    #C0033
    ChrTalk(
        0x103,
        (
            "#0203F#11P（……キーア。）\x02\x03",

            "#0202F（こういう時はお世辞でも\x01",
            "  お兄さんと呼んだ方がいいです。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1936")

    label("loc_18C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1936")

    #C0034
    ChrTalk(
        0x104,
        (
            "#0306F#11P（おーい、キー坊。）\x02\x03",

            "#0300F（こういう時はお世辞でも\x01",
            "  お兄さんとか呼んだ方がいいぜ？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1936")


    #C0035
    ChrTalk(
        0x153,
        "#1105F#6P（そうなのー？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0036
    ChrTalk(
        0x8,
        (
            "#2406F#11Pいや、そういうフォローは\x01",
            "余計に切なくなるんだけど……\x02\x03",

            "#2400F……まあいい、とりあえず、\x01",
            "こちらの方に座ってくれたまえ。\x02\x03",

            "詳しい事情と経緯を\x01",
            "聞かせてもらおうじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1A6D")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_1A94")

    label("loc_1A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1A83")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_1A94")

    label("loc_1A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1A94")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_1A94")

    SetChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0x153, 0x22)
    SetChrSubChip(0x153, 0x0)
    SetChrFlags(0x153, 0x4)
    SetChrSubChip(0x8, 0x1)
    OP_68(111390, 2150, 55630, 0)
    MoveCamera(50, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20870, 0)
    SetChrPos(0x8, 111000, 150, 56700, 180)
    SetChrPos(0x153, 111000, 150, 55300, 0)
    SetChrPos(0x101, 112700, 0, 56600, 270)
    SetChrPos(0xEF, 112700, 0, 55500, 270)
    OP_78(0xA, 0xE)
    SetChrPos(0xE, 111000, 0, 57000, 0)
    OP_D3(0xE, 0x0, 0x0, 0x0, 0x0)
    OP_78(0x5, 0xA)
    SetChrPos(0xA, 111000, 0, 55000, 0)
    OP_78(0x6, 0xB)
    SetChrPos(0xB, 113000, 0, 56600, 0)
    OP_D3(0xB, 0x0, 0x15F90, 0x0, 0x0)
    OP_78(0x7, 0xC)
    SetChrPos(0xC, 113000, 0, 55500, 90)
    OP_D3(0xC, 0x0, 0x15F90, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(111390, 1150, 55630, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(300)

    #C0037
    ChrTalk(
        0x8,
        (
            "#2403F#6P……なるほど。\x01",
            "大体の状況は了解したよ。\x02\x03",

            "#2401Fふむ、七耀教会の法術でも\x01",
            "取り戻せない記憶か……\x02\x03",

            "となると、そのシスターの指摘通り\x01",
            "神経系の問題である可能性は高いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#0006F#11Pそうですか……\x02\x03",

            "#0013F何とか回復する手段は\x01",
            "あるものなんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#2406F#6P正直、脳神経や脳細胞の研究は\x01",
            "まだまだ始まったばかりでね。\x02\x03",

            "記憶喪失になる原因は\x01",
            "それこそ無数にあり得るから\x01",
            "対処療法が存在しないんだよ。\x02\x03",

            "#2400Fただまあ……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "准教授は医療用ルーペを取り出した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetChrSubChip(0x8, 0x0)
    Sound(882, 0, 100, 0)
    Sleep(300)

    #C0041
    ChrTalk(
        0x8,
        (
            "#2401F#5P──キーア君。\x01",
            "僕の目を見てくれるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x153,
        (
            "#1110F#12Pいいよー。\x02\x03",

            "#1101Fじー……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    #C0043
    ChrTalk(
        0x8,
        (
            "#2403F#5Pふむ……瞳孔に異常ナシ。\x02\x03",

            "#2401Fここ数日、頭痛がしたり、\x01",
            "吐き気がしたりしたことは？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x153,
        "#1105F#12Pズツウ？　ハキケ？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0045
    ChrTalk(
        0x101,
        (
            "#0000F#5P頭が痛かったり、\x01",
            "気持ち悪かったりってことさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x153,
        "#1104F#12Pううん、キーア元気だよ？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0047
    ChrTalk(
        0x8,
        (
            "#2401F#5Pふむ……脳にダメージが\x01",
            "あるような感じでもなさそうだ。\x02\x03",

            "#2403Fとなると……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2019")

    #C0048
    ChrTalk(
        0x102,
        "#0101F#11Pな、何か見当が付きました？\x02",
    )

    CloseMessageWindow()
    Jump("loc_207C")

    label("loc_2019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2049")

    #C0049
    ChrTalk(
        0x103,
        "#0201F#11P……何か見当でも？\x02",
    )

    CloseMessageWindow()
    Jump("loc_207C")

    label("loc_2049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_207C")

    #C0050
    ChrTalk(
        0x104,
        "#0301F#11P何か見当でも付いたッスか？\x02",
    )

    CloseMessageWindow()

    label("loc_207C")

    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0051
    ChrTalk(
        0x8,
        (
            "#2403F#6P……これは僕のカンなんだが。\x02\x03",

            "#2401F何らかの薬物が影響している\x01",
            "可能性は高いかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x101,
        "#0007F#11P薬物……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2188")

    #C0053
    ChrTalk(
        0x102,
        (
            "#0105F#11P薬で記憶喪失が起きる\x01",
            "可能性があるんですか！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2209")

    label("loc_2188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_21CB")

    #C0054
    ChrTalk(
        0x103,
        (
            "#0205F#11P薬で記憶喪失が\x01",
            "起きる可能性が……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2209")

    label("loc_21CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2209")

    #C0055
    ChrTalk(
        0x104,
        (
            "#0305F#11P薬で記憶喪失が\x01",
            "起きるもんなんスか！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2209")


    #C0056
    ChrTalk(
        0x8,
        (
            "#2403F#6Pああ、そういう症例も\x01",
            "数少ないが過去に存在する。\x02\x03",

            "#2401F薬の成分が、神経系の伝達を\x01",
            "副次的に阻害してしまうんだが……\x02\x03",

            "#2406Fただ多くの場合、心神喪失を\x01",
            "伴うことが殆んどみたいでねぇ。\x02\x03",

            "キーア君にはそのまま\x01",
            "当てはまらないかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#0008F#11P確かに……\x01",
            "心神喪失には程遠いですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_237C")

    #C0058
    ChrTalk(
        0x102,
        (
            "#0108F#11Pそうね、見ての通り\x01",
            "明るくて元気一杯だし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23F4")

    label("loc_237C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_23B2")

    #C0059
    ChrTalk(
        0x103,
        "#0208F#11P…………はい………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_23F4")

    label("loc_23B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_23F4")

    #C0060
    ChrTalk(
        0x104,
        (
            "#0308F#11Pだな、見ての通り\x01",
            "メチャメチャ元気だし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F4")

    SetChrSubChip(0x153, 0x2)
    Sleep(300)

    #C0061
    ChrTalk(
        0x153,
        "#1100F#6Pんー？\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#2403F#6Pただまあ、薬学の分野も\x01",
            "まだまだ発展途中と言える。\x02\x03",

            "未知の効果を及ぼす薬物が\x01",
            "開発された可能性は否定できない。\x02\x03",

            "#2401Fその意味では、神経系の異常と\x01",
            "薬物の副作用の両方の可能性から\x01",
            "探ってみるべきかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#0003F#11Pなるほど……\x02\x03",

            "#0001Fあの、こちらで検査を\x01",
            "依頼することは可能ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "#2405F#6Pああ、もちろん可能だよ。\x02\x03",

            "#2406Fただし、時間がかかる上に\x01",
            "記憶が取り戻せる保証もない。\x02\x03",

            "#2400Fそれで良ければになるけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#0006F#11Pそ、そうですか……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2639")

    #C0066
    ChrTalk(
        0x102,
        (
            "#0108F#11Pあの、検査をするとなると\x01",
            "どのくらいの期間が……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D4")

    label("loc_2639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_268A")

    #C0067
    ChrTalk(
        0x103,
        (
            "#0201F#11P……検査をするとなると\x01",
            "具体的にはどの程度の期間が？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D4")

    label("loc_268A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_26D4")

    #C0068
    ChrTalk(
        0x104,
        (
            "#0301F#11Pで、検査をするとなると\x01",
            "期間はどのくらいなんスか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D4")


    #C0069
    ChrTalk(
        0x8,
        (
            "#2403F#6P──最低でも３日間。\x02\x03",

            "#2401Fできれば１週間ほどは\x01",
            "検査入院して欲しい所だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        "#0003F#11P最低でも３日ですか……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "#2406F#6P薬物に関する検査は\x01",
            "それなりに時間がかかるんだ。\x02\x03",

            "体内から排出される成分を\x01",
            "化学的方法で調べたりするからね。\x02\x03",

            "#2400F入院と検査費用に関しては……\x01",
            "珍しい症例みたいだから\x01",
            "ある程度お安くはしておこう。\x02\x03",

            "……どうする？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0072
    ChrTalk(
        0x101,
        (
            "#0002F#5P──なあ、キーア。\x02\x03",

            "３日くらいの間……\x01",
            "この病院に泊まらないか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    #C0073
    ChrTalk(
        0x153,
        (
            "#1100F#6Pん～？\x02\x03",

            "べつにいいけどー。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#0012F#5Pほっ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2914")

    #C0075
    ChrTalk(
        0x102,
        "#0109F#11Pふふ、一安心ね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_296F")

    label("loc_2914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2944")

    #C0076
    ChrTalk(
        0x103,
        "#0204F#11P……一安心ですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_296F")

    label("loc_2944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_296F")

    #C0077
    ChrTalk(
        0x104,
        "#0309F#11Pはは、一安心だな。\x02",
    )

    CloseMessageWindow()

    label("loc_296F")

    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0078
    ChrTalk(
        0x8,
        (
            "#2404F#6Pふむ、それなら早速、\x01",
            "検査入院の手続きをしようか。\x02\x03",

            "#2400F着替えや私物などがあるなら\x01",
            "改めて持ってきてもらった方が\x01",
            "いいかもしれないね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0079
    ChrTalk(
        0x101,
        (
            "#0000F#11Pええ、それは後ほど\x01",
            "改めて用意して持って来ます。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x153,
        (
            "#1111F#6Pねえねえ、ロイド。\x02\x03",

            "ここに泊まるのはいいけど\x01",
            "またいっしょに寝てもいい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)

    #C0081
    ChrTalk(
        0x101,
        "#0011F#5Pえっと……それは……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x153,
        (
            "#1106F#6Pんー、ダメだったら\x01",
            "ガマンするけどー……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#0006F#5Pい、いや……\x01",
            "そうじゃないんだ。\x02\x03",

            "#0002Fこの病院に泊まるのは\x01",
            "キーアだけなんだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0084
    ChrTalk(
        0x153,
        (
            "#1105F#6Pそーなの？\x02\x03",

            "#1110Fそれじゃあロイドたちは\x01",
            "どこに泊まるのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#0004F#5P俺たちはいつも通り、\x01",
            "支援課のオンボロビルだよ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0086
    ChrTalk(
        0x101,
        (
            "#0000F#5P#1K#38Aでも、毎日ちゃんと\x01",
            "キーアの顔は見に来るから──\x02",
        )
    )

    Sleep(3800)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0087
    ChrTalk(
        0x153,
        "#1103F#6P#1Kヤダ。\x02",
    )

    OP_57(0x1)
    OP_5A()

    #C0088
    ChrTalk(
        0x101,
        "#0005F#5P……え。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    SetChrPos(0x153, 111510, 0, 55700, 45)
    Sound(820, 0, 100, 0)
    ClearChrFlags(0x153, 0x4)
    SetChrSubChip(0x8, 0x1)
    OP_0D()
    Sleep(300)

    #C0089
    ChrTalk(
        0x153,
        (
            "#1101F#6P……ロイドたち、キーアのことを\x01",
            "ヨソのコにしちゃうつもりなんだ。\x02\x03",

            "#1107Fキーア、いらないコなんだ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0090
    ChrTalk(
        0x101,
        "#0013F#5Pそ、そんな訳ないだろ！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_2E1B")

    #C0091
    ChrTalk(
        0x102,
        (
            "#0106F#11Pちょ、ちょっとのあいだ\x01",
            "ここで泊まるだけだから……\x02\x03",

            "#0102Fその後は、今まで通り\x01",
            "みんなで一緒に暮らせるわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F0A")

    label("loc_2E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2E93")

    #C0092
    ChrTalk(
        0x103,
        (
            "#0206F#11P少しの間だけ\x01",
            "ここで泊まるだけです。\x02\x03",

            "#0202Fその後は、今まで通り\x01",
            "みんなで一緒に暮らせます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F0A")

    label("loc_2E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_2F0A")

    #C0093
    ChrTalk(
        0x104,
        (
            "#0306F#11Pちょっとの間、\x01",
            "ここで泊まるだけだって。\x02\x03",

            "#0300Fその後は、今まで通り\x01",
            "みんなで一緒に暮らせるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F0A")


    #C0094
    ChrTalk(
        0x153,
        (
            "#1101F#6Pそんなの知らないモン！\x02\x03",

            "ぎるども、びょーいんも\x01",
            "キーア泊まりたくないモン！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(110240, 1150, 54670, 1000)
    BeginChrThread(0x153, 3, 0, 14)
    Sleep(300)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0xEF, 0x1)
    Sleep(600)
    SetChrSubChip(0x8, 0x2)
    WaitChrThread(0x153, 3)

    #C0095
    ChrTalk(
        0x101,
        "#0011F#5P#Nキ、キーア？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0096
    ChrTalk(
        0x153,
        "#1107F#4S#6Pロイドのばか！\x02",
    )

    CloseMessageWindow()
    OP_68(100850, 1150, 50000, 3000)
    BeginChrThread(0x153, 3, 0, 15)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_6F(0x79)

    #C0097
    ChrTalk(
        0x101,
        "#0007F#12Pちょっ、キーア！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(112060, 1150, 56390, 0)
    MoveCamera(50, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20870, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_30BE")

    #C0098
    ChrTalk(
        0x102,
        (
            "#0106F#11Pふう……\x01",
            "怒らせちゃったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3133")

    label("loc_30BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_30FB")

    #C0099
    ChrTalk(
        0x103,
        (
            "#0206F#11Pはぁ……\x01",
            "怒らせてしまいました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3133")

    label("loc_30FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3133")

    #C0100
    ChrTalk(
        0x104,
        (
            "#0306F#11Pやれやれ……\x01",
            "怒らせちまったか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3133")


    #C0101
    ChrTalk(
        0x101,
        "#0006F#5Pああもう……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0xEF, 0x0)
    Sleep(200)

    #C0102
    ChrTalk(
        0x101,
        (
            "#0001F#11Pすみません先生。\x01",
            "せっかくの話でしたけど……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    #C0103
    ChrTalk(
        0x8,
        (
            "#2409F#6Pハハ、あの調子だと\x01",
            "無理強いはかえって逆効果だね。\x02\x03",

            "#2400Fまあ、結果が出るかどうかも\x01",
            "分からない検査入院だ。\x02\x03",

            "キーア君が落ち着いてから\x01",
            "改めて検討してみたらどうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#0006F#11Pはい……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#2404F#6Pまあ、記憶が戻るのを\x01",
            "気長に待つのもいいだろう。\x02\x03",

            "#2400F何かあったら相談に乗るから\x01",
            "いつでも連絡してくれたまえ。\x02\x03",

            "こちらも記憶障害について\x01",
            "幾つか症例を調べておくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#0002F#11P……ありがとうございます。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_338E")

    #C0107
    ChrTalk(
        0x102,
        (
            "#0104F#11Pその時はどうか\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FC")

    label("loc_338E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_33CF")

    #C0108
    ChrTalk(
        0x103,
        (
            "#0204F#11P……その時は\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FC")

    label("loc_33CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_33FC")

    #C0109
    ChrTalk(
        0x104,
        "#0304F#11Pその時は宜しくッス。\x02",
    )

    CloseMessageWindow()

    label("loc_33FC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x52, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0xA, 0, 0, 0, 0)
    SetChrPos(0xB, 0, 0, 0, 0)
    SetChrPos(0xC, 0, 0, 0, 0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_D3(0xE, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    SetChrPos(0x0, 107040, 0, 52930, 180)
    SetChrPos(0x8, 110690, 150, 57000, 270)
    OP_4C(0x8, 0xFF)
    OP_66(0x0, 0x1)
    SetScenarioFlags(0xA8, 6)
    OP_29(0x48, 0x1, 0x8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_10DC end

    def Function_14_34E0(): pass

    label("Function_14_34E0")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, 111670, 0, 54050, 5000, 0x1)
    OP_95(0xFE, 109780, 0, 53980, 5000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_14_34E0 end

    def Function_15_3517(): pass

    label("Function_15_3517")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_95(0xFE, 105220, 0, 50000, 5000, 0x1)
    OP_95(0xFE, 100910, 0, 50000, 5000, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)

    def lambda_3554():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3554)
    OP_95(0xFE, 98450, 0, 50000, 5000, 0x0)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    Sound(107, 0, 100, 0)
    Return()

    # Function_15_3517 end

    def Function_16_3582(): pass

    label("Function_16_3582")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(56390, 1400, 57940, 0)
    MoveCamera(47, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21440, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 60040, 0, 59000, 270)
    SetChrPos(0xEF, 60040, 0, 59000, 270)
    FadeToBright(1000, 0)
    SetCameraDistance(20900, 2000)
    OP_6F(0x10)
    OP_0D()
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    OP_68(55390, 1400, 57940, 3000)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0xEF, 3, 0, 18)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    OP_6F(0x1)

    #C0110
    ChrTalk(
        0x101,
        (
            "#0006F#6P参ったな……\x01",
            "あんなに嫌がるなんて。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_36E4")

    #C0111
    ChrTalk(
        0x102,
        (
            "#0102F#11Pふふ、それはそれで\x01",
            "嬉しいとか思っていない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_376F")

    label("loc_36E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_372B")

    #C0112
    ChrTalk(
        0x103,
        (
            "#0202F#11P……それはそれで\x01",
            "嬉しいと思ってませんか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_376F")

    label("loc_372B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_376F")

    #C0113
    ChrTalk(
        0x104,
        (
            "#0302F#11Pハハ、それはそれで\x01",
            "嬉しいとか思ってねぇか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376F")


    #C0114
    ChrTalk(
        0x101,
        (
            "#0011F#6Pうっ……\x01",
            "まあ、否定はしないけどさ。\x02\x03",

            "#0003Fとにかくキーアを追いかけよう。\x02\x03",

            "#0008Fハア、変なところに\x01",
            "行ってないといいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19940, 2000)
    FadeToDark(1000, 0, -1)
    OP_6F(0x10)
    OP_0D()
    SetScenarioFlags(0xA8, 7)
    SetScenarioFlags(0x5C, 2)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3582 end

    def Function_17_3824(): pass

    label("Function_17_3824")


    def lambda_3829():
        OP_95(0xFE, 55540, 0, 59000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3829)

    def lambda_3843():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3843)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x190)
    Return()

    # Function_17_3824 end

    def Function_18_385F(): pass

    label("Function_18_385F")


    def lambda_3864():
        OP_95(0xFE, 57040, 0, 59000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3864)

    def lambda_387E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_387E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_385F end

    def Function_19_3893(): pass

    label("Function_19_3893")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis087.itp")
    OP_68(113550, 1250, 51110, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23130, 0)
    SetChrPos(0x101, 108030, 0, 49200, 270)
    SetChrPos(0x102, 108030, 0, 48000, 270)
    SetChrPos(0x103, 106810, 0, 48000, 270)
    SetChrPos(0x104, 106810, 0, 49200, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    FadeToBright(1000, 0)
    OP_68(108440, 1250, 57200, 8000)
    OP_6F(0x1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    #C0115
    ChrTalk(
        0x101,
        "#0000F──失礼します。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    def lambda_3A04():
        OP_95(0xFE, 108030, 0, 57600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A04)
    Sleep(150)

    def lambda_3A21():
        OP_95(0xFE, 106810, 0, 57600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A21)
    Sleep(50)

    def lambda_3A3E():
        OP_95(0xFE, 108030, 0, 56400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A3E)
    Sleep(100)

    def lambda_3A5B():
        OP_95(0xFE, 106810, 0, 56400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A5B)
    Sleep(3000)
    SetChrSubChip(0x8, 0x0)
    WaitChrThread(0x101, 1)

    def lambda_3A80():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A80)
    WaitChrThread(0x104, 1)

    def lambda_3A91():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A91)
    WaitChrThread(0x102, 1)

    def lambda_3AA2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3AA2)
    WaitChrThread(0x103, 1)

    def lambda_3AB3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AB3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0116
    ChrTalk(
        0x8,
        (
            "#2406F#11Pはは……ようこそ。\x01",
            "よく訪ねてきてくれたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0012F#6Pえっと……\x01",
            "突然お邪魔してすみません。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#0106F#6P何だかご趣味の邪魔を\x01",
            "してしまったようで……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "#2406F#11Pいや～、午後のこの時間は\x01",
            "ノーブルカルプを釣り上げる\x01",
            "絶好の時間帯なんだけど……\x02\x03",

            "#2401Fでも、来客ならば仕方ない。\x02\x03",

            "#2403F君たちを逆恨みする気なんて\x01",
            "これっぽっちもないさ、うん。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x103,
        (
            "#0206F#6P（なんだか思いっきり\x01",
            "  恨まれてるような気が……）\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x104,
        (
            "#0306F#6P（筋金入りの\x01",
            "  釣りバカみてぇだな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "#2409F#11Pまあ、軽いイヤミは\x01",
            "このくらいにして……\x02\x03",

            "#2400F今日は一体どうしたんだい？\x02\x03",

            "てっきりキーア君を連れて\x01",
            "相談に来たと思ったんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#0000F#6Pいえ、実は別件なんです。\x02\x03",

            "#0006Fその……\x01",
            "相変わらずキーアの記憶は\x01",
            "戻っていないんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "#2410F#11Pふむ、そうか……\x02\x03",

            "#2400F個人的には一度、検査入院を\x01",
            "してもらった方がいいと思うが。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        (
            "#0108F#6Pその、本人にもそれとなく\x01",
            "勧めているんですが、\x01",
            "その気になれないみたいで……\x02\x03",

            "#0106F……すみません。\x01",
            "問題を先送りにしていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "#2404F#11Pまあ焦らずに\x01",
            "ゆっくりと考えるといい。\x02\x03",

            "#2400Fそれで、別件というのは？\x02\x03",

            "僕の専門に関わる話かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#0003F#6Pええ、まさにそうなんです。\x02\x03",

            "#0001F──こちらの薬を\x01",
            "ご覧になっていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        "#2405F#11Pほう……？\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)

    #A0129
    AnonymousTalk(
        0x8,
        (
            "#2405F……これは……\x02\x03",

            "#2401Fなんだこの蒼色は……\x01",
            "着色料にしては様子が……\x02",
        )
    )

    CloseMessageWindow()

    #A0130
    AnonymousTalk(
        0x101,
        (
            "#0006Fこの錠剤は、とある人物が\x01",
            "持っていた物なんですが……\x02\x03",

            "#0013F俺たちは、違法性のある\x01",
            "薬物ではないかと睨んでいます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #C0131
    ChrTalk(
        0x8,
        (
            "#2403F#11P……なるほど。\x02\x03",

            "#2401F詳しい話を聞かせて\x01",
            "もらおうじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 102150, 150, 55850, 0)
    SetChrPos(0x101, 103000, 150, 55880, 0)
    SetChrPos(0x102, 103850, 150, 55890, 0)
    SetChrPos(0x104, 105270, 0, 56100, 315)
    SetChrPos(0x8, 102990, 150, 58690, 180)
    SetChrSubChip(0x8, 0x0)
    OP_68(103000, 1950, 57370, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_68(103000, 950, 57370, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0132
    ChrTalk(
        0x8,
        (
            "#2403F#5Pなるほど……\x01",
            "そんな事になっているのか。\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#0008F#12Pそれで、ヨアヒム先生。\x02\x03",

            "#0001Fこの蒼い錠剤について\x01",
            "何かご存知ではありませんか？\x02\x03",

            "どこかで開発された新薬とか……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "#2406F#5P……残念ながら、\x01",
            "見たことのないタイプの薬だ。\x02\x03",

            "#2401F僕は専門柄、各国にある\x01",
            "製薬会社と付き合いがあってね。\x02\x03",

            "開発された新薬のサンプルは\x01",
            "大抵回してもらっているんだが……\x02\x03",

            "こんな色の錠剤は見たことがない。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#0006F#12Pそ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        (
            "#2403F#5Pしかも聞く限りにおいて\x01",
            "効能についても尋常ではない。\x02\x03",

            "筋力、集中力、反射神経、\x01",
            "そして判断力と直感力……\x02\x03",

            "#2401Fそれら全てを高めるというのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        (
            "#0106F#12Pその、まだマフィアたちが\x01",
            "この薬を服用していたかどうかは\x01",
            "確かではないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x104,
        (
            "#0301F#11P実際、確認できてんのは\x01",
            "あの鉱員だけだしなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x103,
        (
            "#0206F#6P……イアン先生から聞いた話も\x01",
            "まだ噂の域を出ていませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "#2410F#5Pふむ、いずれにせよ、\x01",
            "得体の知れない薬物であるのは\x01",
            "確かのようだな。\x02\x03",

            "#2400F──分かった。\x01",
            "３錠ほど預からせてもらうよ。\x02\x03",

            "早速、成分調査をしてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0004F#12Pありがとうございます。\x02\x03",

            "#0000Fその……成分を突き止めるのに\x01",
            "どのくらいかかりそうですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#2400F#5P薬の現物もあるし、\x01",
            "症状などの手がかりもある。\x02\x03",

            "今日中には、主成分くらいは\x01",
            "突き止められるとは思うが……\x02\x03",

            "#2406F逆にそれで突き止められなければ\x01",
            "結構、長引くかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#0006F#12Pそうですか……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "#2400F#5Pまあ、明日の午後くらいに\x01",
            "通信で連絡させてもらうよ。\x02\x03",

            "それで構わないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            "#0002F#12Pそれで結構です。\x01",
            "どうか宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        (
            "#0109F#12Pふふ、これで一安心ね。\x02\x03",

            "#0105Fそういえば、副作用や中毒症状の\x01",
            "可能性はどうなんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "#2403F#5Pふむ、それも調べてみないと\x01",
            "何とも言えないんだが……\x02\x03",

            "#2401F念のため、その鉱員の関係者には\x01",
            "何かあったらこちらに相談するよう\x01",
            "伝えておいてもらえるかな？\x02\x03",

            "他の服用者が見つかったら\x01",
            "同じ手配をしておいて欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        "#0100F#12P承知しました。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        (
            "#0306F#11Pやれやれ……\x01",
            "どんだけ出回ってる事やら。\x02\x03",

            "#0301F街でそれっぽい噂も\x01",
            "チラホラ聞いたくらいだし。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(200)

    #C0150
    ChrTalk(
        0x103,
        (
            "#0206F#6Pさすがにルバーチェに\x01",
            "連絡するのは無理そうですが……\x02\x03",

            "#0201F本当に構成員が服用していたら\x01",
            "副作用などが心配ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#0006F#12Pうーん、確かに……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        "#2403F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x103, 0x0)

    #C0153
    ChrTalk(
        0x101,
        "#0005F#12P……先生？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        "#0101F#12Pやはり副作用の危険が？\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "#2405F#5Pああ、いや……\x01",
            "そうじゃないんだ。\x02\x03",

            "#2410Fふと、前に聞いた噂を\x01",
            "思い出してしまってね……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        "#0005F#12P前に聞いた噂……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        "#0301F#11Pどんな噂ッスか？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7526", 0)
    SetCameraDistance(25000, 50000)

    #C0158
    ChrTalk(
        0x8,
        (
            "#2409F#5Pハハ、参ったな。\x01",
            "改めて説明するほどの\x01",
            "話でもないと思うんだが……\x02\x03",

            "#2410F──数年前、製薬業界の方面で\x01",
            "奇妙な噂が流れた事があったんだ。\x02\x03",

            "#2401Fとある狂信的な宗教団体が\x01",
            "不思議な薬を造りだしたとね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0159
    ChrTalk(
        0x101,
        "#0011F#12Pきょ、狂信的な宗教団体……？\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#0105F#12P七耀教会の異端的な一派……\x01",
            "ということでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "#2403F#5Pいやいや、そんな生易しい\x01",
            "連中じゃなかったらしいよ。\x02\x03",

            "#2401F何でも女神の存在を否定し、\x01",
            "悪魔を崇拝する……\x02\x03",

            "そんな教団だったらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0162
    ChrTalk(
        0x101,
        "#0005F#12Pあ、悪魔を崇拝……！？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        (
            "#0301F#11Pなんかいきなり\x01",
            "胡散臭い話になったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x103,
        "#0205F#12P………………………………\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        (
            "#2400F#5Pはは、確かに僕も\x01",
            "突拍子もない話だと思ったが。\x02\x03",

            "#2410Fただ、その薬の効能というのが\x01",
            "ちょっと気になってね……\x02\x03",

            "#2401F──何でも悪魔の力を借りる事で\x01",
            "人間の潜在能力を開花させ、\x01",
            "運すら呼び込むものだったらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0166
    ChrTalk(
        0x102,
        "#0107F#12Pそ、それって……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#0013F#12P今回の薬物の症状と同じ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0168
    ChrTalk(
        0x103,
        (
            "#0208F#6P#40Wあの……ヨアヒム先生……\x02\x03",

            "#0201F#40Wその薬の名前は……\x01",
            "何か聞いていませんか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x8,
        (
            "#2405F#5Pああ、何だったかな……\x02\x03",

            "#2403F……そうそう、思い出した。\x02\x03",

            "#2401F《真なる叡智#10Rグ ノ ー シ ス#》──\x01",
            "そんな風に噂されていたかな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0170
    ChrTalk(
        0x103,
        "#0210F#6P…………っ……………\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#0005F#12P《真なる叡智#10Rグ ノ ー シ ス#》……\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        (
            "#0101F#12Pな、何だかとても\x01",
            "思わせぶりな名前ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "#2403F#5Pまあ、余りに荒唐無稽だから\x01",
            "すぐに消えた噂話だったけどね。\x02\x03",

            "#2401Fただ、去年リベールの異変で\x01",
            "奇妙な組織が暗躍していたという\x01",
            "噂話もあっただろう？\x02\x03",

            "今更ながら気になってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#0013F#12P（エステルたちが言っていた\x01",
            "  《結社》のことか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        (
            "#0108F#12P（悪魔崇拝の教団……\x01",
            "  何か関係があるのかしら？）\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "#2410F#5P──いずれにせよ、\x01",
            "蒼い錠剤の正体を突き止めるため、\x01",
            "同業者には当たってみるつもりだ。\x02\x03",

            "#2400Fついでに、その噂についても\x01",
            "何か続報がないか確かめてみるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        "#0001F#12Pお、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x104,
        "#0301F#11P悪魔の力を借りる薬ねぇ……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        "#0206F#6P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
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
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 110690, 150, 57000, 270)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetChrPos(0x0, 106850, 0, 52690, 180)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xC3, 4)
    OP_29(0x4C, 0x1, 0x3)
    OP_68(57830, 1200, 58960, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21440, 0)
    SetChrPos(0x101, 60040, 0, 59000, 270)
    SetChrPos(0x102, 60040, 0, 59000, 270)
    SetChrPos(0x103, 60040, 0, 59000, 270)
    SetChrPos(0x104, 60040, 0, 59000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    SetCameraDistance(20900, 2000)
    OP_6F(0x10)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)
    OP_68(55830, 1200, 58960, 3000)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 22)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 23)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 24)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    Sound(107, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    OP_6F(0x1)

    #C0180
    ChrTalk(
        0x101,
        (
            "#0006F#6Pな、何だか最後に\x01",
            "奇妙な話を聞いたけど……\x02\x03",

            "#0000Fとりあえず薬の成分調査は\x01",
            "先生に任せておけばよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x102,
        (
            "#0100F#5Pええ、そろそろ夕方だし、\x01",
            "クロスベル市に戻りましょう。\x02\x03",

            "一課からの捜査報告書が\x01",
            "届いているかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x104,
        (
            "#0306F#11Pやれやれ、今夜は書類と\x01",
            "にらめっこになりそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        "#0208F#12P#40W…………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21400, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0xC3, 5)
    OP_29(0x4C, 0x1, 0x4)
    EventEnd(0x5)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_19_3893 end

    def Function_20_5792(): pass

    label("Function_20_5792")

    Return()

    # Function_20_5792 end

    def Function_21_5793(): pass

    label("Function_21_5793")


    def lambda_5798():
        OP_95(0xFE, 54500, 0, 59000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5798)

    def lambda_57B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_57B2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_21_5793 end

    def Function_22_57CE(): pass

    label("Function_22_57CE")


    def lambda_57D3():
        OP_95(0xFE, 56000, 0, 59800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57D3)

    def lambda_57ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_57ED)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xE1, 0x12C)
    Return()

    # Function_22_57CE end

    def Function_23_5809(): pass

    label("Function_23_5809")


    def lambda_580E():
        OP_95(0xFE, 56000, 0, 58000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_580E)

    def lambda_5828():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5828)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x13B, 0x12C)
    Return()

    # Function_23_5809 end

    def Function_24_5844(): pass

    label("Function_24_5844")


    def lambda_5849():
        OP_95(0xFE, 57000, 0, 59000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5849)

    def lambda_5863():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5863)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x10E, 0x12C)
    Return()

    # Function_24_5844 end

    SaveToFile()

Try(main)
