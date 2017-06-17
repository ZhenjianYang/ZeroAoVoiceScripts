from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0570.bin",                # FileName
        "c0570",                    # MapName
        "c0570",                    # Location
        0x0027,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 39, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0570",                  # 0
        "エリック",               # 1
        "サンドラ",               # 2
        "セルダン支部長",         # 3
        "コパン",                 # 4
        "ペーター",               # 5
        "ダドリー捜査官",         # 6
        "アイリス",               # 7
        "客引きビッシュ",         # 8
        "オリビエ",               # 9
        "ニールセン",             # 10
    ))

    AddCharChip((
        "chr/ch32202.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch24202.itc",                   # 02
        "chr/ch22000.itc",                   # 03
        "chr/ch26802.itc",                   # 04
        "chr/ch00902.itc",                   # 05
        "chr/ch26900.itc",                   # 06
        "chr/ch26700.itc",                   # 07
    ))

    DeclNpc(0,       0,       6400,    180,  261,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4699,   79,      4449,    0,    261,  0x0, 0,   4,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(2109,    150,     4250,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-5420,   0,       1649,    90,   385,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-1090,   0,       3950,    135,  385,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       0,       5000,    1000,    0,       1500,    6400,    0x007E, 0,  4,  0x0000)
    DeclActor(-7600,   750,     5400,    1200,    -7600,   800,     5400,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(604, 0)                                        # 0

    ScpFunction((
        "Function_0_25C",          # 00, 0
        "Function_1_314",          # 01, 1
        "Function_2_52D",          # 02, 2
        "Function_3_5D6",          # 03, 3
        "Function_4_691",          # 04, 4
        "Function_5_695",          # 05, 5
        "Function_6_1EFE",         # 06, 6
        "Function_7_2F31",         # 07, 7
        "Function_8_2FDC",         # 08, 8
        "Function_9_3083",         # 09, 9
        "Function_10_312A",        # 0A, 10
        "Function_11_31AD",        # 0B, 11
        "Function_12_39B2",        # 0C, 12
        "Function_13_3A21",        # 0D, 13
        "Function_14_3A57",        # 0E, 14
        "Function_15_4C8B",        # 0F, 15
        "Function_16_5798",        # 10, 16
        "Function_17_57E8",        # 11, 17
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

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A7")
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x0)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, -8400, 100, -500, 90)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -8900, 0, 1500, 90)
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x2)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, -5800, 100, -2050, 0)

    label("loc_3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DB")
    SetScenarioFlags(0x0, 5)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_3DB")

    SetChrChipByIndex(0x9, 0x4)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3FA")
    Jump("loc_50E")

    label("loc_3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_412")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_50E")

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_420")
    Jump("loc_50E")

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_444")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jump("loc_50E")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_452")
    Jump("loc_50E")

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_465")
    SetChrFlags(0x9, 0x10)
    Jump("loc_50E")

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D")
    SetChrFlags(0x9, 0x10)

    label("loc_47D")

    Jump("loc_50E")

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_495")
    SetChrFlags(0x9, 0x10)
    Jump("loc_50E")

    label("loc_495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4A3")
    Jump("loc_50E")

    label("loc_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B6")
    SetChrFlags(0x9, 0x10)
    Jump("loc_50E")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4C4")
    Jump("loc_50E")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4D2")
    Jump("loc_50E")

    label("loc_4D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_4F7")
    SetChrFlags(0x9, 0x10)
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_50E")

    label("loc_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_505")
    Jump("loc_50E")

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_50E")

    label("loc_50E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_52C")
    ClearScenarioFlags(0x22, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_52C")
    SetScenarioFlags(0x0, 6)
    Event(0, 17)

    label("loc_52C")

    Return()

    # Function_1_314 end

    def Function_2_52D(): pass

    label("Function_2_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_549")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_594")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_565")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_594")

    label("loc_565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_57F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x243), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 5)
    Jump("loc_594")

    label("loc_57F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_594")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 6)

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B5")
    Sound(128, 1, 50, 0)

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_5CC")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    Return()

    # Function_2_52D end

    def Function_3_5D6(): pass

    label("Function_3_5D6")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『ビジネスマンのための定番メニュー』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_68D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x17)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『濃厚カプチーノ』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_68D")

    TalkEnd(0xFF)
    Return()

    # Function_3_5D6 end

    def Function_4_691(): pass

    label("Function_4_691")

    Call(0, 5)
    Return()

    # Function_4_691 end

    def Function_5_695(): pass

    label("Function_5_695")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D9")

    #C0003
    ChrTalk(
        0x8,
        "いらっしゃいませ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x8,
        (
            "おや……\x01",
            "ワジさんではありませんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "こんな時間にいらっしゃるなんて\x01",
            "珍しいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x105,
        (
            "#10303Fフフ、ちょっとした\x01",
            "パトロールの途中でね。\x02\x03",

            "#10300F今度時間がある時にでも\x01",
            "また飲みにこさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "ええ、お待ちしております。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 3)
    TalkEnd(0x8)
    Return()

    label("loc_7D9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EFA")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_841")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_841")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_861")
    OP_AF(0x42)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EF5")

    label("loc_861")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_875")
    Jump("loc_1EF5")

    label("loc_875")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A6")

    #C0008
    ChrTalk(
        0x8,
        (
            "近い内、《黒月》が裏社会で\x01",
            "実権を握ることになるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "黒月はルバーチェのような\x01",
            "目立つ行動を好まない組織ですが、\x01",
            "その存在感は圧倒的ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "この裏通りにも少なからず\x01",
            "影響が出てくるに違いありません。\x01",
            "……気をつけた方がよさそうですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A47")

    label("loc_9A6")


    #C0011
    ChrTalk(
        0x8,
        (
            "近い内、《黒月》が裏社会で\x01",
            "実権を握ることになるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "この裏通りにも少なからず\x01",
            "影響が出てくるに違いありません。\x01",
            "……気をつけた方がよさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A47")

    Jump("loc_1EF5")

    label("loc_A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AE1")

    #C0013
    ChrTalk(
        0x8,
        (
            "裏通りまではあの化物は\x01",
            "入ってきていないようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "ですが、どんな危険があるか\x01",
            "分かりません。\x01",
            "店内への避難はご自由にどうぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE5")

    #C0015
    ChrTalk(
        0x8,
        (
            "此度の独立宣言は、裏社会にも\x01",
            "大きく影響するはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "今後は国防軍によって\x01",
            "帝国、共和国系のマフィアも\x01",
            "取り締まられていくでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "かなりの急展開でしたが……\x01",
            "クロスベルにはこれくらいの\x01",
            "荒療治が必要なのかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C95")

    label("loc_BE5")


    #C0018
    ChrTalk(
        0x8,
        (
            "今後は国防軍によって\x01",
            "帝国、共和国系のマフィアも\x01",
            "取り締まられていくでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "独立宣言は急展開でしたが……\x01",
            "クロスベルにはこれくらいの\x01",
            "荒療治が必要なのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C95")

    Jump("loc_1EF5")

    label("loc_C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D89")

    #C0020
    ChrTalk(
        0x8,
        (
            "クロスベル市の襲撃……\x01",
            "『赤い星座』の連中は\x01",
            "とんでもない事をしていきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "裏の情報が入りやすいこの店でも、\x01",
            "予兆すら感じとれなかった……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "おそらく、かなり前から綿密に\x01",
            "計画されていたのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E20")

    label("loc_D89")


    #C0023
    ChrTalk(
        0x8,
        (
            "裏の情報が入りやすいこの店でも、\x01",
            "予兆すら感じとれなかった……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "クロスベル市の襲撃はおそらく、\x01",
            "かなり前から綿密に\x01",
            "計画されていたのでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E20")

    Jump("loc_1EF5")

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_FC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F28")

    #C0025
    ChrTalk(
        0x8,
        (
            "『赤い星座』の連中が\x01",
            "姿を消したのに気づいたのは、\x01",
            "警察の慌しい様子を見てからです。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "連中は地下を通って警察の監視を逃れ、\x01",
            "マインツ方面へと向かったのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "……この占拠事件が何を意味するのか\x01",
            "私には計り知れませんが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FC1")

    label("loc_F28")


    #C0028
    ChrTalk(
        0x8,
        (
            "『赤い星座』の連中が\x01",
            "姿を消したのに気づいたのは、\x01",
            "警察の慌しい様子を見てからです。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "……この占拠事件が何を意味するのか\x01",
            "私には計り知れませんが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC1")

    Jump("loc_1EF5")

    label("loc_FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1131")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A4")

    #C0030
    ChrTalk(
        0x8,
        (
            "昨日の脱線事故……\x01",
            "付近に現れた巨大な化物が\x01",
            "起こしたとの噂があるようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "しかし、住民投票が近づいてる現状では\x01",
            "ただの魔獣による事故とも思えません。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "……キナ臭いものを感じますね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_112C")

    label("loc_10A4")


    #C0033
    ChrTalk(
        0x8,
        (
            "住民投票が近づいてる現状、\x01",
            "昨日の脱線事故も噂にあるような\x01",
            "ただの魔獣による事故とも思えません。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        "……キナ臭いものを感じますね。\x02",
    )

    CloseMessageWindow()

    label("loc_112C")

    Jump("loc_1EF5")

    label("loc_1131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_118B")

    #C0035
    ChrTalk(
        0x8,
        "遠くに聞こえる救急車のサイレン……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        "……なにやら胸騒ぎがしますね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_118B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F0")

    #C0037
    ChrTalk(
        0x8,
        (
            "昨日、アルタイル市のほうで\x01",
            "共和国系テロリストの逮捕劇が\x01",
            "あったそうなのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "裏では黒月の連中も\x01",
            "追跡に動いていたという噂です。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12A7")

    #C0039
    ChrTalk(
        0x101,
        (
            "#00005F（あの場に黒月がいたのか……）\x02\x03",

            "#00003F（気づかなかったけど\x01",
            "  さすがに抜け目がない連中だな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E8")

    label("loc_12A7")


    #C0040
    ChrTalk(
        0x8,
        (
            "さすがというかなんというか……\x01",
            "やはり抜け目がありませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E8")

    SetScenarioFlags(0x0, 0)
    Jump("loc_138D")

    label("loc_12F0")


    #C0041
    ChrTalk(
        0x8,
        (
            "昨日のアルタイル市での\x01",
            "共和国系テロリストの逮捕劇には、\x01",
            "黒月も動いていたという噂です。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "さすがというかなんというか……\x01",
            "やはり抜け目がありませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138D")

    Jump("loc_1EF5")

    label("loc_1392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1540")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A7")

    #C0043
    ChrTalk(
        0x8,
        (
            "通商会議の時、『赤い星座』は\x01",
            "帝国政府の依頼でテロリストを\x01",
            "撃退したとの噂もありますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "近頃のクリムゾン商会は\x01",
            "大きなトラブルを起こす事もなく、\x01",
            "いたって静かなものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "……良くも悪くも、\x01",
            "彼らがプロの猟兵なのだと\x01",
            "実感させられますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_153B")

    label("loc_14A7")


    #C0046
    ChrTalk(
        0x8,
        (
            "通商会議で大きく動いた\x01",
            "クリムゾン商会も、近頃は\x01",
            "いたって静かなものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "……良くも悪くも、\x01",
            "彼らがプロの猟兵なのだと\x01",
            "実感させられますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153B")

    Jump("loc_1EF5")

    label("loc_1540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1638")

    #C0048
    ChrTalk(
        0x8,
        (
            "猟兵団『赤い星座』。\x01",
            "そして港湾区の『黒月』……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "本会議当日ということで、\x01",
            "警察の方々もこれらの勢力への\x01",
            "警戒を強めているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "裏通りで見かける警察官たちも\x01",
            "かなりの緊張状態に\x01",
            "なっているのを感じますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16DE")

    label("loc_1638")


    #C0051
    ChrTalk(
        0x8,
        (
            "本会議当日ということで、\x01",
            "『赤い星座』『黒月』への警戒も\x01",
            "強められているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "裏通りで見かける警察官たちも\x01",
            "かなりの緊張状態に\x01",
            "なっているのを感じますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DE")

    Jump("loc_1EF5")

    label("loc_16E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_18BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B1")

    #C0053
    ChrTalk(
        0x8,
        (
            "通商会議……\x01",
            "いよいよ始まりましたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "裏通りを警備する\x01",
            "警察の方々の緊張も\x01",
            "高まったように感じます。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "やはりクリムゾン商会への\x01",
            "警戒意識は強いようですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_182C")

    label("loc_17B1")


    #C0056
    ChrTalk(
        0x8,
        (
            "裏通りを警備する\x01",
            "警察の方々の緊張も\x01",
            "高まったように感じます。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "やはりクリムゾン商会への\x01",
            "警戒意識は強いようですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182C")

    Jump("loc_18B8")

    label("loc_1831")


    #C0058
    ChrTalk(
        0x8,
        (
            "オリビエさん、\x01",
            "なかなかに面白い方でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "できればステージの演奏家として\x01",
            "正式に契約したかったですが……\x01",
            "残念でなりませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B8")

    Jump("loc_1EF5")

    label("loc_18BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A11")

    #C0060
    ChrTalk(
        0x8,
        (
            "新たに裏路地のビルに入った\x01",
            "《クリムゾン商会》……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "何かとトラブルの絶えなかった\x01",
            "ルバーチェに比べれば、\x01",
            "弁えた連中、といった印象です。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "しかし、その実態は\x01",
            "西ゼムリア最強の猟兵団の一つ\x01",
            "『赤い星座』だという噂……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "表向きは大人しいとはいえ、\x01",
            "むしろあのルバーチェ以上の\x01",
            "存在感を感じざるを得ませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AC3")

    label("loc_1A11")


    #C0064
    ChrTalk(
        0x8,
        (
            "クリムゾン商会のその実態は\x01",
            "西ゼムリア最強の猟兵団の一つ\x01",
            "『赤い星座』だという噂……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "表向きは大人しいとはいえ、\x01",
            "むしろあのルバーチェ以上の\x01",
            "存在感を感じざるを得ませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC3")

    Jump("loc_1EF5")

    label("loc_1AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1BA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4B")

    #C0066
    ChrTalk(
        0x8,
        (
            "……雨が段々と\x01",
            "酷くなってきましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "サンドラさんもそろそろ起こして\x01",
            "帰したほうがよさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BA2")

    label("loc_1B4B")


    #C0068
    ChrTalk(
        0x8,
        "……どうかされましたか？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "今、ウチの店には\x01",
            "私とサンドラさんしかいませんが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA2")

    Jump("loc_1EF5")

    label("loc_1BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1D30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA8")

    #C0070
    ChrTalk(
        0x8,
        (
            "ルバーチェ跡の一帯は、\x01",
            "黒月が手にすると見て\x01",
            "まず間違いないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "そうなれば、黒月が\x01",
            "クロスベルの裏社会に\x01",
            "確かな足場を築くことになる……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "クロスベルの現状を考えれば、\x01",
            "ある程度仕方のないことなのかも\x01",
            "しれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D2B")

    label("loc_1CA8")


    #C0073
    ChrTalk(
        0x8,
        (
            "成立しつつある、\x01",
            "黒月による裏社会への台頭……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "クロスベルの現状を考えれば、\x01",
            "ある程度仕方のないことなのかも\x01",
            "しれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2B")

    Jump("loc_1EF5")

    label("loc_1D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E45")

    #C0075
    ChrTalk(
        0x8,
        (
            "ルバーチェが消えてから、\x01",
            "今まで身を潜めていたヤクザ者が\x01",
            "徐々に姿を現してきています。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "そういった意味では、\x01",
            "裏通りの治安はむしろ\x01",
            "悪くなっているのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "ルバーチェがどれだけの力を\x01",
            "持っていたか……消えた今でこそ\x01",
            "分かるというものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EF5")

    label("loc_1E45")


    #C0078
    ChrTalk(
        0x8,
        (
            "ルバーチェが消えてから、\x01",
            "今まで身を潜めていたヤクザ者が\x01",
            "徐々に姿を現してきています。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "ルバーチェがどれだけの力を\x01",
            "持っていたか……消えた今でこそ\x01",
            "分かるというものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF5")

    Jump("loc_7E3")

    label("loc_1EFA")

    TalkEnd(0x8)
    Return()

    # Function_5_695 end

    def Function_6_1EFE(): pass

    label("Function_6_1EFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_202F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE0")
    SetChrSubChip(0xFE, 0x2)

    #C0080
    ChrTalk(
        0xFE,
        (
            "うぃーっく……\x01",
            "エリック～、飲みましょうよ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 0xFF)

    #C0081
    ChrTalk(
        0xFE,
        (
            "あのおかしなモヤも晴れて、\x01",
            "おめでたい雰囲気でしょ～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    #C0082
    ChrTalk(
        0x8,
        (
            "サンドラさん、ジャマなので\x01",
            "いい加減帰ってください。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_202A")

    label("loc_1FE0")


    #C0083
    ChrTalk(
        0xFE,
        "うぃーっく、エリックのいけず……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "だけど、そんな所がス・テ・キ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_202A")

    Jump("loc_2F2D")

    label("loc_202F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20A9")

    #C0085
    ChrTalk(
        0xFE,
        (
            "むにゃむにゃ……\x01",
            "戒厳令で店が休みだから、\x01",
            "ここで飲んで寝てたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "なに、なにかあったのぉ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F2D")

    label("loc_20A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_21EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2180")

    #C0087
    ChrTalk(
        0xFE,
        (
            "ウチの店でも、さっそく\x01",
            "『独立記念パーティ』なんてのを\x01",
            "予約する客がいるらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "あたしには難しいことは\x01",
            "よく分かんないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "まあみんな嬉しそうだし\x01",
            "いいんじゃないの？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21E6")

    label("loc_2180")


    #C0090
    ChrTalk(
        0xFE,
        (
            "あたしには難しいことは\x01",
            "よく分かんないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "まあみんな嬉しそうだし\x01",
            "いいんじゃないの？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E6")

    Jump("loc_2F2D")

    label("loc_21EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2316")

    #C0092
    ChrTalk(
        0xFE,
        (
            "襲撃事件があって、ウチのお店も\x01",
            "営業を自粛してたんだけど、\x01",
            "今夜から再開するんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "まー、街の復旧も\x01",
            "目処がついたみたいだし、\x01",
            "いつまでも休んでられないわよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "ウチは単なるクラブだけど、\x01",
            "それでも楽しみにしてる客もいるし。\x01",
            "……いっちょがんばりますか～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23C3")

    label("loc_2316")


    #C0095
    ChrTalk(
        0xFE,
        (
            "街の復旧も目処がついたみたいだし、\x01",
            "いつまでも休んでられないわよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "ウチは単なるクラブだけど、\x01",
            "それでも楽しみにしてる客もいるし。\x01",
            "……いっちょがんばりますか～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C3")

    Jump("loc_2F2D")

    label("loc_23C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2523")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24AA")

    #C0097
    ChrTalk(
        0xFE,
        (
            "エリックが言ってたけど、\x01",
            "クリムゾン商会って\x01",
            "猟兵団の会社だったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "ひゃ～……\x01",
            "あの有名な《ノイエ＝ブラン》の\x01",
            "クリムゾン商会がねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "ヤクザ者だとは思ってたけど\x01",
            "そこまでとは驚きだわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_251E")

    label("loc_24AA")


    #C0100
    ChrTalk(
        0xFE,
        (
            "あの《ノイエ＝ブラン》の\x01",
            "クリムゾン商会が猟兵団ねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "ヤクザ者だとは思ってたけど\x01",
            "そこまでとは驚きだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_251E")

    Jump("loc_2F2D")

    label("loc_2523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_268E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2615")
    OP_4B(0x8, 0xFF)

    #C0102
    ChrTalk(
        0xFE,
        (
            "ねえ～エリックったら、\x01",
            "小難しい話ばっかりしてないで\x01",
            "飲みに付き合ってよ～……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    #C0103
    ChrTalk(
        0x8,
        (
            "サンドラさんも、\x01",
            "ウチの店でばっかり寝てないで\x01",
            "家に帰ったらどうです？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "もう、エリックのイケズ～……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2689")

    label("loc_2615")


    #C0105
    ChrTalk(
        0xFE,
        (
            "ちぇっ、エリックったら\x01",
            "出てけなんてヒドいわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "でも、そういうところもス・テ・キ。\x01",
            "……な～んちゃって㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2689")

    Jump("loc_2F2D")

    label("loc_268E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_27B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274B")

    #C0107
    ChrTalk(
        0xFE,
        (
            "むにゃむにゃ……\x01",
            "どうだ、このセクハラオヤジ～……！\x01",
            "思い知れっ、このこの～……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0108
    ChrTalk(
        0xFE,
        "……へあっ！？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "……なんだ、夢かあ。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_27AD")

    label("loc_274B")


    #C0110
    ChrTalk(
        0xFE,
        (
            "あーあ……\x01",
            "気分のいい夢を見てたのに\x01",
            "すっかり目が覚めちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        "ん……なんかあったワケ？\x02",
    )

    CloseMessageWindow()

    label("loc_27AD")

    Jump("loc_2F2D")

    label("loc_27B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_285C")

    #C0112
    ChrTalk(
        0xFE,
        (
            "むにゃむにゃ……\x01",
            "あのオヤジ、あいかわらず\x01",
            "べたべた触りやがってぇ～……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "ウチはそんな店じゃないって、\x01",
            "いつも言ってるでしょーが。\x01",
            "こんちくしょ～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F2D")

    label("loc_285C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2996")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2929")

    #C0114
    ChrTalk(
        0xFE,
        (
            "何か今度、住民投票ってヤツが\x01",
            "あるらしいじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "是非行くべきだって\x01",
            "エリックが言うんだけど、\x01",
            "正直微妙なのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "だって、投票のある時間帯は\x01",
            "寝てるもん、あたし。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2991")

    label("loc_2929")


    #C0117
    ChrTalk(
        0xFE,
        (
            "住民投票、行けるかどうか\x01",
            "正直微妙なのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "だって、投票のある時間帯は\x01",
            "寝てるもん、あたし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2991")

    Jump("loc_2F2D")

    label("loc_2996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2AC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A52")
    OP_4B(0x8, 0xFF)

    #C0119
    ChrTalk(
        0xFE,
        (
            "エリック～……\x01",
            "ラムコーラおかわり～……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    #C0120
    ChrTalk(
        0x8,
        (
            "サンドラさん、もう朝ですし\x01",
            "そろそろ帰ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "もう、エリックのイケズ～……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AC0")

    label("loc_2A52")


    #C0122
    ChrTalk(
        0xFE,
        (
            "エリックのイケズ～……\x01",
            "たまには付き合いなさいよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "久しぶりにあたし、\x01",
            "お店が休みなんだからさぁ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AC0")

    Jump("loc_2F2D")

    label("loc_2AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BCD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B58")

    #C0124
    ChrTalk(
        0xFE,
        (
            "昨日、店にタチの悪い客が来て\x01",
            "すごい飲まされちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "う～……頭がガンガンする。\x01",
            "もうやんなっちゃうわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC8")

    label("loc_2B58")


    #C0126
    ChrTalk(
        0xFE,
        (
            "あの人の演奏、\x01",
            "とっても上手だったわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "仕事疲れでぐったりしてたけど、\x01",
            "すっかり癒されちゃったわ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC8")

    Jump("loc_2F2D")

    label("loc_2BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2CA7")

    #C0128
    ChrTalk(
        0xFE,
        (
            "歓楽街の《ノイエ＝ブラン》、\x01",
            "こっちにクリムゾン商会が来てから\x01",
            "更に景気がよくなったらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "はー、やっぱり高級クラブともなると\x01",
            "払いも段違いに良いんでしょうね。\x01",
            "あたしも移らしてくれないかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F2D")

    label("loc_2CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_2CE8")
    OP_64(0x9)

    #C0130
    ChrTalk(
        0xFE,
        "こっくり……こっくり……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_2F2D")

    label("loc_2CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2E1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA0")

    #C0131
    ChrTalk(
        0xFE,
        (
            "ふぁあ～……\x01",
            "すっかり寝ちゃってたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "いつもホステスの仕事の後は\x01",
            "この店に寄っちゃうのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "だって、静かで居心地いいから\x01",
            "よく眠れるんだもの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E15")

    label("loc_2DA0")


    #C0134
    ChrTalk(
        0xFE,
        (
            "このお店、いつも静かだから\x01",
            "よく眠れるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "エリックも黙って\x01",
            "付き合ってくれるし、\x01",
            "すごい居心地いいのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E15")

    Jump("loc_2F2D")

    label("loc_2E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB3")

    #C0136
    ChrTalk(
        0xFE,
        (
            "毎日毎日、クラブで\x01",
            "営業スマイルをしながら\x01",
            "一晩中お酌しているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "はあ……\x01",
            "なんであたしったら\x01",
            "こんな仕事してんだろ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F2D")

    label("loc_2EB3")


    #C0138
    ChrTalk(
        0xFE,
        (
            "はあ……\x01",
            "最近、この仕事に\x01",
            "空しさを感じてるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "ま、払いがいいから\x01",
            "なかなか辞める気には\x01",
            "ならないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F2D")

    TalkEnd(0xFE)
    Return()

    # Function_6_1EFE end

    def Function_7_2F31(): pass

    label("Function_7_2F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F63")
    Call(0, 14)
    Return()

    label("loc_2F63")

    TalkBegin(0xFE)

    #C0140
    ChrTalk(
        0xFE,
        (
            "俺はまず、再出発に相応しい\x01",
            "新たな事務所を探すつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "ロイド団員、また何かあったら\x01",
            "情報交換をしよう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_2F31 end

    def Function_8_2FDC(): pass

    label("Function_8_2FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_300E")
    Call(0, 14)
    Return()

    label("loc_300E")

    TalkBegin(0xFE)

    #C0142
    ChrTalk(
        0xFE,
        (
            "さてと、オレはさっそく\x01",
            "釣りに出かけるとするッスかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "なに、雨なんてこれっぽっちも\x01",
            "気にしないッス！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_2FDC end

    def Function_9_3083(): pass

    label("Function_9_3083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30B5")
    Call(0, 14)
    Return()

    label("loc_30B5")

    TalkBegin(0xFE)

    #C0144
    ChrTalk(
        0xFE,
        (
            "それにしてもあの男……\x01",
            "本当に許せません。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "プロだか何だか知りませんが、\x01",
            "釣師の風上にもおけませんよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_3083 end

    def Function_10_312A(): pass

    label("Function_10_312A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_313F")
    Call(0, 11)
    Jump("loc_31A9")

    label("loc_313F")


    #C0146
    ChrTalk(
        0xD,
        (
            "#00600Fさて……\x01",
            "これを飲んだら仕事に戻るか。\x02\x03",

            "#00603F住民投票の日も近い。\x01",
            "まだまだ気は抜けんからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31A9")

    TalkEnd(0xFE)
    Return()

    # Function_10_312A end

    def Function_11_31AD(): pass

    label("Function_11_31AD")

    EventBegin(0x0)
    Fade(500)
    OP_68(1500, 1430, 2330, 0)
    MoveCamera(328, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21430, 0)
    SetChrPos(0xD, 1920, 0, 3850, 180)
    SetChrPos(0x101, 680, 0, 2770, 45)
    SetChrPos(0x102, 1730, 0, 2320, 0)
    SetChrPos(0x103, 920, 0, 1020, 0)
    SetChrPos(0x104, -160, 0, 1970, 45)
    SetChrPos(0x109, -640, 0, 3120, 90)
    SetChrPos(0x105, 2330, 0, 910, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    #C0147
    ChrTalk(
        0x101,
        "#00005Fダドリーさん。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xD,
        (
            "#00603Fお前たちか。\x01",
            "……こんな所で会うとはな。\x02\x03",

            "#00600Fどうやら、今日から\x01",
            "支援要請を再開したそうだが？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        "#00000Fええ、おかげさまで。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#6P#00100Fちなみに\x01",
            "《赤い星座》の行方について\x01",
            "新しい情報は入りましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xD,
        (
            "#00600Fフン、それが\x01",
            "情けないことに全くだ。\x02\x03",

            "帝国政府にしても、\x01",
            "新しいコメントを出すつもりは\x01",
            "一向にないようだしな。\x02\x03",

            "#00603F次に何かが起こるとしたら\x01",
            "３日後の住民投票……\x02\x03",

            "#00600F今はその日に備えるだけで\x01",
            "精一杯というところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x109,
        "#5P#10103Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x104,
        (
            "#00302Fへっ、だが何つうか\x01",
            "妙に哀愁が漂ってやがるな。\x02\x03",

            "まさか、酔っ払ってんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xD,
        (
            "#00603Fフン、酒は嗜むが\x01",
            "昼間から飲む道理はない。\x02\x03",

            "#00600Fただのソフトドリンクだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、アルコールなしで\x01",
            "ここまでの雰囲気を\x01",
            "出せるなんて見事だね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xD)

    #C0156
    ChrTalk(
        0xD,
        (
            "#00603F……バニングス。\x01",
            "お前、酒はやるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x101,
        (
            "#00005Fええまあ。\x01",
            "そんなに多くは飲みませんけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xD,
        (
            "#00602Fフン、ならば\x01",
            "ガイのヤツとは大違いだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0159
    ChrTalk(
        0x101,
        (
            "#00005Fダドリーさん、もしかして\x01",
            "兄貴とここで飲んだ事が？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xD,
        (
            "#00603Fまあ、数えるほどだがな。\x02\x03",

            "#00600Fちなみに、この店を初めに\x01",
            "知ったのはガイの紹介だ。\x02\x03",

            "#00608Fこういった店を開拓するのが\x01",
            "本当に得意なヤツだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        (
            "#00000Fはは、でしょうね。\x01",
            "何しろあの性格ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x104,
        (
            "#00300Fちなみに、あんたと\x01",
            "ロイドの兄貴はどっちが\x01",
            "酒に強かったんだ？\x02\x03",

            "あんたらのことだから、\x01",
            "対決でもしてるんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xD,
        (
            "#00603Fフン、それはノーコメントだ。\x02\x03",

            "#00602Fただ１つ言えるのは\x01",
            "オルランドにバニングス……\x01",
            "私もガイもお前たちよりは強い。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0164
    ChrTalk(
        0x104,
        (
            "#00301Fなっ、俺がどれだけ飲めるか\x01",
            "知らねえくせにヌケヌケと……\x02\x03",

            "#00304Fそこまで言うのなら\x01",
            "今度、実際に見せてもらうからな？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xD,
        "#00604Fフッ、機会があればな。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#00002Fあはは……\x02\x03",

            "（ダドリーさんって、\x01",
            "  実はこんな所でも\x01",
            "  負けず嫌いなんだな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x18F, 3)
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0xD, 2110, 150, 4250, 0)
    SetChrPos(0x0, 1210, 0, 2500, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_31AD end

    def Function_12_39B2(): pass

    label("Function_12_39B2")

    TalkBegin(0xFE)

    #C0167
    ChrTalk(
        0xFE,
        (
            "なんや、えらい事に\x01",
            "なってしもたなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "今日はお客もかからんし、\x01",
            "おとなしくしとくんやったで。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_39B2 end

    def Function_13_3A21(): pass

    label("Function_13_3A21")

    TalkBegin(0xFE)

    #C0169
    ChrTalk(
        0xFE,
        (
            "どうしよう、\x01",
            "これじゃ家にも帰れないわ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_3A21 end

    def Function_14_3A57(): pass

    label("Function_14_3A57")

    EventBegin(0x0)
    OP_4B(0xB, 0xFF)
    Fade(500)
    OP_68(-5430, 1430, 390, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -6170, 0, 1680, 180)
    SetChrPos(0x102, -5200, 0, 1810, 180)
    SetChrPos(0x109, -5400, 0, 3000, 180)
    SetChrPos(0x105, -4200, 0, 2000, 225)
    OP_0D()

    #C0170
    ChrTalk(
        0xC,
        "#6Pロイド君、来てくれましたね。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xA,
        "わざわざすまないな、ロイド団員。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "さて……これで揃ったか。\x01",
            "それじゃ早速、作戦会議と行こう。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    OP_68(-4570, 1630, -1220, 0)
    MoveCamera(318, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20220, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0xB, -8400, 0, 1500, 90)
    SetChrPos(0x101, -3100, 100, -1000, 270)
    SetChrPos(0x102, -3100, 100, 0, 270)
    SetChrPos(0x105, -4690, 0, 1380, 225)
    SetChrPos(0x109, -3190, 0, 1380, 225)
    SetChrSubChip(0xC, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)

    #C0173
    ChrTalk(
        0xA,
        (
            "#5Pまずは、ロイド団員に\x01",
            "俺たちの状況を説明しないとなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        (
            "#5P実はこの数ヶ月あまり……\x01",
            "釣公師団は活動を謹慎していたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        "#12P#00005Fき、謹慎ですか……？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xC,
        (
            "#6Pええ、何しろ我々の仲間の\x01",
            "ヨアヒム元団員があんな事件を\x01",
            "起こしてしまいましたから……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "#5Pそれで、各人で改めて\x01",
            "自己を見つめ直すことにしたんスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        "#12P#00108Fでも、それは皆さんの責任では……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xA,
        "#5P確かに事件には関係していないが……\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "#5P彼とは釣りを愛する同士として、\x01",
            "多くの時間を共に過ごしてきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xA,
        (
            "#5P……なのに俺たちは、\x01",
            "彼が心の奥底で考えていることに\x01",
            "何一つとして気付けなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        "#5P社会的にも個人的にも責任十分だよ。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#12P#00003Fセルダン支部長……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xA,
        "#5P……まあ、それは一旦置いといてだ。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "#5Pそんな中、１週間ほど前に突然\x01",
            "不動産会社から連絡があってなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        (
            "#5P謹慎の話を知ってか知らずか、\x01",
            "建物を使っていないみたいだから\x01",
            "契約を解消したと言われたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        (
            "#5Pそれも、新しく《釣皇倶楽部》と\x01",
            "契約したって報告付きでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xC,
        (
            "#6Pその後すぐ、釣皇倶楽部の代表者と\x01",
            "コンタクトを取ろうとしたんですが\x01",
            "なかなかうまくいかず……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xB,
        (
            "#5Pそれで今日、事務所を訊ねたら\x01",
            "たまたま向こうの代表がいたんスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xB,
        "#5Pそこでやっと契約の真相が聞けて……\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xB,
        (
            "#5Pそれからロイド団員たちと\x01",
            "一緒になったってわけなんス。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#12P#00005Fなるほど、そうだったんですか……\x02\x03",

            "#00003F大体、状況は把握できました。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "#5Pそれにしても……\x01",
            "レイクロード社の《釣皇倶楽部》か。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xA,
        (
            "#5P活動の拠点を広げたいってだけなら\x01",
            "別に知ったことじゃねえんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xA,
        (
            "#5Pまさか、事務所を無理やり\x01",
            "奪うような真似をするとはな……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xC,
        (
            "#6Pええ、目の敵にされる理由も\x01",
            "いまいち分かりませんし……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xB,
        (
            "#5P……とにかく、\x01",
            "これは明らかな嫌がらせッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "#5Pだからと言って、\x01",
            "何をどうこう出来るわけでも\x01",
            "ないんスけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xA,
        (
            "#5Pああ、とりあえずしばらくは\x01",
            "様子を見るしかなさそうだなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xA,
        (
            "#5P……ただ、このまま\x01",
            "支部を無くしてしまうわけにも\x01",
            "いかないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xA,
        (
            "#5Pまだ十分とはいえないが……\x01",
            "今をもって謹慎を解こうと思う。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    SetChrSubChip(0xC, 0x1)

    #C0202
    ChrTalk(
        0xC,
        (
            "#6Pふふ、それでは釣公師団・\x01",
            "クロスベル支部、活動再開ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xB,
        "#11Pおおっ、待ってましたッス！\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xA,
        (
            "#5Pただし……全員初心に帰って\x01",
            "《駆け出し釣り師》から\x01",
            "出直すことが条件だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xA,
        (
            "#5Pそれから、\x01",
            "『段位認定試験』についても\x01",
            "当分の間は中止とする。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0206
    ChrTalk(
        0xB,
        "#11Pえ……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0207
    ChrTalk(
        0xB,
        (
            "#11Pちょ、ちょっと\x01",
            "待ってくださいッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        (
            "#11Pそれはつまり……\x01",
            "オレはもう《特級釣師》\x01",
            "じゃないってことッスか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)

    #C0209
    ChrTalk(
        0xA,
        (
            "#5Pああ、残念だがそういうことだ。\x01",
            "これもケジメだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xB,
        "#11Pがくっ、オレの努力が……\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xC,
        (
            "#6Pまあまあ、コパン君。\x01",
            "また頑張ればいいじゃないですか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x87, 0x1F4)

    #C0212
    ChrTalk(
        0xB,
        (
            "#11Pうう……\x01",
            "元々が《道楽釣り師》止まりの\x01",
            "ペーターさんに言われたくないッス。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 0)), scpexpr(EXPR_END)), "loc_46CD")

    #C0213
    ChrTalk(
        0x101,
        (
            "#12P#00012Fあはは……\x02\x03",

            "#00006F（クロスベルの《釣聖》……\x01",
            "  かなり苦労したんだけどな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EF")

    label("loc_46CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 1)), scpexpr(EXPR_END)), "loc_4730")

    #C0214
    ChrTalk(
        0x101,
        (
            "#12P#00012Fあはは……\x02\x03",

            "#00006F（《特級釣師》……\x01",
            "  結構、頑張ったんだけどな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EF")

    label("loc_4730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_47A2")

    #C0215
    ChrTalk(
        0x101,
        (
            "#12P#00009Fあはは……\x02\x03",

            "#00003F（そもそも《駆け出し釣り師》の\x01",
            "  俺には関係のない話だな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EF")

    label("loc_47A2")


    #C0216
    ChrTalk(
        0x101,
        (
            "#12P#00009Fあはは……\x02\x03",

            "#00006F（ふう、これで\x01",
            "  俺の称号もリセットか。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47EF")

    SetChrSubChip(0xA, 0x0)

    #C0217
    ChrTalk(
        0xA,
        (
            "#5Pよし、それじゃ用意していた\x01",
            "新しい釣具一式を支給するぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xA,
        (
            "#5Pペーター、コパン、それにロイド団員。\x01",
            "こいつを受け取ってくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0219
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x14),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x14, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0220
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×１０\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×１０を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 10)
    AddItemNumber(0x187, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 0)), scpexpr(EXPR_END)), "loc_4A69")

    #C0222
    ChrTalk(
        0xA,
        (
            "#5P一度《釣聖》まで上り詰めた\x01",
            "ロイド団員にはこいつもサービスだ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0223
    AnonymousTalk(
        0xFF,
        (
            "さらに、",
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×２０\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×２０を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 20)
    AddItemNumber(0x187, 20)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0224
    ChrTalk(
        0x101,
        "#12P#00002Fあ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B80")

    label("loc_4A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 1)), scpexpr(EXPR_END)), "loc_4B80")

    #C0225
    ChrTalk(
        0xA,
        (
            "#5P一度《特級釣師》まで行った\x01",
            "コパンとロイド団員には\x01",
            "こいつもサービスだ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0226
    AnonymousTalk(
        0xFF,
        (
            "さらに、",
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×１０\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×１０を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 10)
    AddItemNumber(0x187, 10)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0227
    ChrTalk(
        0x101,
        "#12P#00002Fあ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xB,
        "#5Pありがたく頂いておくッス。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B80")

    label("loc_4B80")


    #C0229
    ChrTalk(
        0xA,
        (
            "#5Pよし、それじゃ後のことは\x01",
            "それぞれに任せたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xA,
        (
            "#5P俺はまず、再出発に相応しい\x01",
            "新たな事務所を探すつもりだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        (
            "#5P釣皇倶楽部の動向を含め、\x01",
            "近い内にまた情報交換をしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        "#12P#00000Fええ、分かりました。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrSubChip(0xC, 0x0)
    StopSound(128, 2000, 40)
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 4)
    NewScene("c0500", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3A57 end

    def Function_15_4C8B(): pass

    label("Function_15_4C8B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46500.itc", 0x1E)
    LoadChrToIndex("apl/ch51230.itc", 0x1F)
    LoadChrToIndex("apl/ch51270.itc", 0x20)
    OP_68(1350, 1830, 1580, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -100, 0, 1950, 270)
    SetChrPos(0x102, -100, 0, 3150, 270)
    SetChrPos(0x104, 1060, 0, 2520, 270)
    SetChrPos(0x109, 2020, 0, 1660, 270)
    SetChrPos(0x105, 1590, 0, 3440, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x10, 0x20)
    SetChrPos(0x10, -13920, 550, 4900, 45)
    BeginChrThread(0x10, 0, 0, 16)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x8, -5430, 0, 6530, 0)
    TurnDirection(0x8, 0x10, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-13000, 1830, 4650, 3000)
    MoveCamera(292, 17, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(19150, 3000)
    OP_6F(0x79)

    #C0233
    ChrTalk(
        0x101,
        "#00005F（オ、オリビエさん……？）\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x105,
        (
            "#10300F（へえ……\x01",
            "  上手いものじゃないか。）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-7750, 1830, 3690, 3000)
    MoveCamera(301, 22, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(21280, 3000)
    OP_6F(0x79)
    StopBGM(0x3E8)
    WaitBGM()
    Fade(500)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x10, 0x20)
    EndChrThread(0x10, 0x0)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x10, -11230, 400, 3690, 90)
    OP_0D()

    #C0235
    ChrTalk(
        0x10,
        (
            "#5P#13904Fフッ……\x01",
            "ご静聴、感謝する。\x02",
        )
    )

    CloseMessageWindow()
    Sound(971, 0, 50, 0)

    #C0236
    ChrTalk(
        0x9,
        "ブラボ～！\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x9,
        "お兄さん、すっごく上手いわね！\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x8,
        (
            "どうです、しばらくここで\x01",
            "演奏活動をしてみては……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x8,
        (
            "演奏料などは多少、\x01",
            "出させていただきますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x10,
        (
            "#5P#13909Fおお、なんという\x01",
            "ありがたい申し出だろう！\x02\x03",

            "#13900Fもちろん、快く\x01",
            "引き受けさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        "#00007Fちょ、ちょっと待った！！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)
    OP_68(-7500, 1630, 2280, 3000)
    MoveCamera(325, 17, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(22280, 3000)

    def lambda_50BA():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50BA)
    Sleep(50)

    def lambda_50D7():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50D7)
    Sleep(50)

    def lambda_50F4():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50F4)
    Sleep(50)

    def lambda_5111():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5111)
    Sleep(50)

    def lambda_512E():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_512E)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0242
    ChrTalk(
        0x10,
        (
            "#5P#13905Fあ、あれれ。\x01",
            "もう見つかってしまったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        (
            "#12P#00006Fな、なにのんびり仕事に\x01",
            "ありつこうとしてるんですか！\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x104,
        "#12P#00306Fったく、とんでもねえ兄さんだな……\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x10,
        (
            "#5P#13904Fフッ、よしてくれたまえ。\x01",
            "そんなに褒められたら照れてしまうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x104,
        "#12P#00301Fだれも褒めてねえっつの！\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x109,
        "#12P#10101F今度こそ、ついてきてもらいますよ。\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x10,
        (
            "#5P#13910Fやれやれ、キミたちも\x01",
            "あきらめが悪いねぇ。\x02\x03",

            "#13900F人生はもっと楽しく、\x01",
            "朗らかに生きないと。\x02\x03",

            "#13904Fそんなキミたちに、\x01",
            "今一度贈らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    OP_0D()

    #C0249
    ChrTalk(
        0x10,
        (
            "#5P#13912F荒んだ心を解きほぐす、\x01",
            "愛と真心の調べを……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x102,
        "#12P#00103Fふう……\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0251
    ChrTalk(
        0x10,
        (
            "#5P#13905Fおや……\x01",
            "どうしたんだいマドモアゼル。\x02\x03",

            "#13904F憂いを含んだ溜め息は\x01",
            "色気あっていいものだが、\x01",
            "幸せが逃げてしまうというよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        (
            "#12P#00103F……念の為に\x01",
            "言っておきますけど。\x02\x03",

            "#00100F私たち、ミュラーさんには\x01",
            "『どんなことをしてでも連れてこい』\x01",
            "と頼まれているんです。\x02\x03",

            "#00109F多少なら、痛い目に\x01",
            "あわせてもいいそうですけど……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    OP_0D()

    #C0253
    ChrTalk(
        0x10,
        (
            "#5P#13911Fわ、わかりました！\x01",
            "是非帰らせていただきます！\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#12P#00012F（エリィ、笑顔なのに\x01",
            "  目が笑ってない……）\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x10,
        (
            "#5P#13910Fやれやれ……\x01",
            "ここいらが潮時か。\x02\x03",

            "#13900Fそれじゃあ、ミュラーのところに\x01",
            "案内してくれるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x109,
        (
            "#12P#10108Fうーん、でも……\x01",
            "ミュラーさんの方からこちらに\x01",
            "来てもらうのがよさそうですね。\x02\x03",

            "#10106Fちょっとお手数はかけますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x105,
        (
            "#12P#10302Fまあ、それが無難だろうね。\x01",
            "連行中に逃げられてもなんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x10,
        "#5P#13910Fやれやれ、信用がないねえ。\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#12P#00003Fと、とにかく……\x01",
            "駅の方に連絡を入れてみるか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("c0500", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_4C8B end

    def Function_16_5798(): pass

    label("Function_16_5798")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57E7")
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x2)
    Sleep(200)
    SetChrSubChip(0xFE, 0x3)
    Sleep(200)
    SetChrSubChip(0xFE, 0x4)
    Sleep(200)
    SetChrSubChip(0xFE, 0x3)
    Sleep(200)
    SetChrSubChip(0xFE, 0x2)
    Sleep(200)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Jump("Function_16_5798")

    label("loc_57E7")

    Return()

    # Function_16_5798 end

    def Function_17_57E8(): pass

    label("Function_17_57E8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch45100.itc", 0x22)
    LoadChrToIndex("chr/ch45102.itc", 0x23)
    OP_68(-7510, 900, -380, 0)
    MoveCamera(300, 15, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20290, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -7000, 100, -2050, 0)
    SetChrPos(0x102, -5800, 100, -2050, 0)
    SetChrPos(0x103, -4600, 100, -2050, 0)
    SetChrPos(0x104, -3100, 100, -500, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x2)
    SetChrPos(0x11, -8400, 100, -500, 90)
    ClearChrFlags(0x11, 0x8000)
    PlayBGM("ed7117", 0)
    FadeToBright(2000, 0)
    OP_0D()

    #C0260
    ChrTalk(
        0x101,
        (
            "#00005F#6Pジャズ・バー《ガランテ》……\x01",
            "どうしてまたここに？\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x11,
        (
            "#5P実は３年前、ここで\x01",
            "ガイさんと情報交換をさせて頂く\x01",
            "約束をしていましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x11,
        (
            "#5P……訃報が入ったのは\x01",
            "その矢先でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x101,
        "#6P#00006Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x11,
        (
            "#5P#5P……教団事件が起こり、\x01",
            "帝国派・共和国派議員が逮捕され、\x01",
            "新市長が誕生し……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x11,
        (
            "#5P通商会議が開催され、\x01",
            "クロスベル市襲撃事件が起こり……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x11,
        (
            "#5P……そして、現在は\x01",
            "国家独立を宣言した状況にある。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x11,
        (
            "#5Pこれらは全てバラバラのようでいて、\x01",
            "相互に干渉し合って起きた出来事です。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x11,
        (
            "#5Pつまり、どれもが一連の流れの中で\x01",
            "起きた出来事と言えるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x102,
        "#6P#00101F一連の流れ……\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x11,
        (
            "#5Pそして、その流れ――\x01",
            "“大局”を掴むことができれば、\x01",
            "個々の事象がよく見える。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x11,
        (
            "#5Pそうすれば改めて\x01",
            "ガイさんの殺害事件に\x01",
            "光を当てられるのではないか――\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x11,
        (
            "#5Pそう思い、\x01",
            "事件の検証を申し出た次第です。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x11,
        (
            "#5Pロイドさんには、心苦しいことも\x01",
            "あるかと思いますが……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    #C0274
    ChrTalk(
        0x101,
        (
            "#6P#00003F………………………\x02\x03",

            "#00000Fいえ……大丈夫です。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x102,
        "#6P#00108Fロイド……\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x103,
        "#6P#00208Fロイドさん……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        (
            "#12P#00303F……ま、時間もねぇ\x02\x03",

            "#00300Fとにかく始めるとしようぜ。\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)

    #C0278
    ChrTalk(
        0x11,
        (
            "#5Pそうですね……\x01",
            "それでは早速始めましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x11,
        (
            "#5Pまずはガイさんの遺体が\x01",
            "発見された時の状況――\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x11,
        (
            "#5P時は３年前の曇天・小雨の日、\x01",
            "場所は現オルキスタワーの建設現場です。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x11,
        (
            "#5P死亡推定時刻は当日の未明、\x01",
            "発見されるまではおよそ\x01",
            "半日が経過していました。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x11,
        "#5Pそして死因は――\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x11,
        (
            "#5P背後から導力銃で\x01",
            "心臓を打ち抜かれたことによる\x01",
            "出血性ショック死です。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x11,
        "#5P……間違いありませんね？\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        "#6P#00003Fええ……その通りです。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        "#6P#00101F背後から……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x104,
        "#12P#00306Fそうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x103,
        "#6P#00208F…………………………\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x11,
        (
            "#5Pふむ……では次に遺体発見時の\x01",
            "現場の様子の整理に移りましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x11,
        (
            "#5Pまず現場周辺には激しく\x01",
            "争った形跡がありましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x11,
        (
            "#5Pガイさん以外の遺留品は\x01",
            "一切残されていない状況でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x11,
        (
            "#5Pまた現場からは\x01",
            "彼が愛用していたはずの\x01",
            "トンファーが持ち去られており……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x11,
        (
            "#5Pさらに胸に付けてあったはずの\x01",
            "警察徽章も奪われていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x11,
        "#5Pこのうち徽章の方ですが……\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x11,
        (
            "#5Pマフィア《ルバーチェ》の構成員が\x01",
            "現場から持ち去ったことが、\x01",
            "新たに判明したそうですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        (
            "#6P#00003Fはい、その情報については\x01",
            "マルコーニ会長から直接聞きました。\x02\x03",

            "#00001Fさらに、取調べで構成員本人から\x01",
            "正式な供述を得られています。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x11,
        "#5Pふむ、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x11,
        (
            "#5Pでは次は目撃者の有無、\x01",
            "これを確認しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x11,
        "#5P……結論から言うと目撃者はなし。\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x11,
        (
            "#5P当時オルキスタワーは\x01",
            "工事が一時中断された状態にあって、\x01",
            "関係者がいなかったこと。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x11,
        (
            "#5Pさらに事件発生時の未明は\x01",
            "風と小雨、雷鳴も響いていたため……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x11,
        (
            "#5P現場に近付く者は誰もおらず\x01",
            "殺害の瞬間を見た者を\x01",
            "確認することはできませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x11,
        (
            "#5Pまたガイさんは現場に\x01",
            "向かうことを周囲の誰にも\x01",
            "話していませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x11,
        (
            "#5P……と、事件の状況について\x01",
            "私が掴んでいることは以上ですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x11,
        "#5Pロイドさん、何か補足はありますか？\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#6P#00006Fいえ、特には……\x02\x03",

            "#00001F俺も把握している通りです。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        (
            "#6P#00108F（ニールセンさん……\x01",
            "  相変わらず凄い情報力ね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x103,
        (
            "#6P#00203F（ええ、ですがガイさんとは\x01",
            "  個人的にも親しく\x01",
            "  されていたようですし……）\x02\x03",

            "#00201F（この事件に関しては、\x01",
            "  だからこそなのかもしれませんね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x11,
        (
            "#5Pふむ……\x01",
            "では、事件の検証に移ります。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x11,
        (
            "#5P事件の真相――\x01",
            "ズバリ犯人の考察です。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x11,
        (
            "#5Pまず容疑者候補の筆頭として\x01",
            "考えられるのは《ルバーチェ》……\x01",
            "そして『Ｄ∴Ｇ教団』関係者ですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x11,
        "#5Pロイドさん、犯人は彼らですか？\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6779")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0313
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kガイはマフィア、もしくは\x01",
            "Ｄ∴Ｇ教団の関係者に殺された？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "犯人はマフィア関係者\x01",      # 0
            "犯人は教団関係者\x01",          # 1
            "両者ともあり得ない\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_66D9"),
        (1, "loc_670F"),
        (2, "loc_6745"),
        (SWITCH_DEFAULT, "loc_6766"),
    )


    label("loc_66D9")


    #C0314
    ChrTalk(
        0x101,
        "#6P#00006F（……違う、そうじゃない――）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6766")

    label("loc_670F")


    #C0315
    ChrTalk(
        0x101,
        "#6P#00006F（……違う、そうじゃない――）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6766")

    label("loc_6745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_675E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_675E")

    SetScenarioFlags(0x0, 2)
    Jump("loc_6766")

    label("loc_6766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6774")
    Jump("loc_6779")

    label("loc_6774")

    Jump("loc_65FA")

    label("loc_6779")


    #C0316
    ChrTalk(
        0x101,
        (
            "#6P#00003Fいえ、両者ともにあり得ません。\x02\x03",

            "#00008Fルバーチェについては、\x01",
            "マルコーニとその手下から――\x02\x03",

            "#00001F教団についてはヨアヒムから、\x01",
            "殺害を計画しながら果たせなかった\x01",
            "旨の供述を得ています。\x02\x03",

            "#00006Fまた、彼らの目の届かない所で\x01",
            "他の手下や別の関係者が\x01",
            "暴走したというのも考えにくい。\x02\x03",

            "#00013F……それに兄貴は\x01",
            "これらの勢力への警戒を\x01",
            "怠ることはなかったと聞きます。\x02\x03",

            "そんな兄貴が、自らの命を簡単に\x01",
            "奪われるような状況に誘導される……\x02\x03",

            "その可能性はかなり低いと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x104,
        (
            "#12P#00306F……だろうな。\x02\x03",

            "#00301F聞いた話じゃ、大胆不敵ながらも\x01",
            "凄まじい嗅覚の持ち主だったみてぇだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x103,
        (
            "#6P#00206F……はい。\x02\x03",

            "#00201Fマフィアや教団相手に\x01",
            "遅れを取る人とは思えません。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x11,
        (
            "#5P確かに、あらゆる要素が\x01",
            "それらの可能性を否定しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x11,
        (
            "#5P教団事件の前であればいざ知らず、\x01",
            "今、彼らを犯人とするのは\x01",
            "かなり無理があるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x11,
        (
            "#5Pふむ、では次に２大国の関係者――\x01",
            "その可能性を検証してみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x11,
        (
            "#5P利権を貪る帝国派、共和国派議員、\x01",
            "そして彼らと関係の深い両国の\x01",
            "政府高官、および諜報関係者――\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x11,
        (
            "#5Pガイさんが、\x01",
            "そんな人間の手にかかった\x01",
            "可能性は考えられないでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)

    label("loc_6BB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6DAE")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kガイは帝国か共和国の関係者に殺された？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "可能性は高い\x01",            # 0
            "可能性は低い\x01",            # 1
            "どちらとも言えない\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6C7A"),
        (1, "loc_6CF7"),
        (2, "loc_6D18"),
        (SWITCH_DEFAULT, "loc_6D9B"),
    )


    label("loc_6C7A")


    #C0325
    ChrTalk(
        0x101,
        (
            "#6P#00008F（可能性は高い――\x01",
            "  ……本当にそうなのか？）\x02\x03",

            "#00001F（改めてよく考えろ、\x01",
            "  ロイド・バニングス――）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6D9B")

    label("loc_6CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D10")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D10")

    SetScenarioFlags(0x0, 2)
    Jump("loc_6D9B")

    label("loc_6D18")


    #C0326
    ChrTalk(
        0x101,
        (
            "#6P#00008F（どちらとも言えない――\x01",
            "  ……本当にそうなのか？）\x02\x03",

            "#00001F（改めてよく考えろ、\x01",
            "  ロイド・バニングス――）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6D9B")

    label("loc_6D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6DA9")
    Jump("loc_6DAE")

    label("loc_6DA9")

    Jump("loc_6BB8")

    label("loc_6DAE")


    #C0327
    ChrTalk(
        0x101,
        (
            "#6P#00003Fいえ、おそらく\x01",
            "その可能性は低いでしょう。\x02\x03",

            "#00008F確かに、このクロスベルで\x01",
            "不正を働く２大国の関係者は多い。\x02\x03",

            "兄貴はそんな連中の不正に\x01",
            "迫ることも多々あったと聞きます。\x02\x03",

            "#00001Fそして、そんな彼らと関わりの深い\x01",
            "諜報関係者が頻繁にクロスベルに\x01",
            "出入りしていたのも事実でしょう。\x02\x03",

            "#00006Fですが、はっきり言って――\x01",
            "兄貴個人の行動なんて彼らにとっては\x01",
            "痛手でも何でもないはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x102,
        (
            "#6P#00106F確かにそうでしょうね……\x02\x03",

            "#00108F２大国がその気になれば、\x01",
            "自治州政府を通して\x01",
            "警察そのものを押さえ込む……\x02\x03",

            "#00101F以前の体制であれば、\x01",
            "そんな横暴な圧力だって\x01",
            "簡単に掛けられたでしょうから。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#6P#00003Fああ、だからいくら厄介でも\x01",
            "たった１人の捜査官を\x01",
            "わざわざ呼び出して始末する――\x02\x03",

            "#00001Fそもそも、その行為自体に\x01",
            "コストに見合うだけのメリットは\x01",
            "存在しないはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x11,
        "#5Pふむ……\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x104,
        (
            "#12P#00303Fそれに仮にそんな連中が\x01",
            "接触を図ろうとして来たって\x01",
            "ロイドの兄貴のことだ。\x02\x03",

            "#00300Fマフィアと同様、警戒して\x01",
            "不用意に近付かねえだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        "#6P#00206F――同感です。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x11,
        (
            "#5P流石は皆さんですね……\x01",
            "こちらから補足することも\x01",
            "ありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x11,
        "#5Pでは、最後の考察と参りましょう――\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x11,
        (
            "#5Pここまでは、容疑者として\x01",
            "考えられる人物像を反証によって\x01",
            "消去してきたわけですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x11,
        (
            "#5Pずばり、他に考えられる犯人像は\x01",
            "一体どういうものになるでしょう？\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)

    label("loc_7293")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74F0")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0337
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kでは、他に考えられる犯人像は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "結社《身喰らう蛇》の関係者\x01",            # 0
            "クロスベル警察の関係者\x01",                # 1
            "ガイが警戒しつつも、よく知る人物\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7373"),
        (1, "loc_73F4"),
        (2, "loc_74BC"),
        (SWITCH_DEFAULT, "loc_74DD"),
    )


    label("loc_7373")


    #C0338
    ChrTalk(
        0x101,
        (
            "#6P#00006F（確かに謎の多い組織だが――\x01",
            "  よく考えろ。）\x02\x03",

            "#00013F（もっと、自然に導き出される\x01",
            "  答えがあるはずだ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_74DD")

    label("loc_73F4")


    #C0339
    ChrTalk(
        0x101,
        (
            "#6P#00008F（恨みを持った人物による内部犯行――\x01",
            "  あり得なくはないだろうが、\x01",
            "  もっと他に答えようがあるはずだ。）\x02\x03",

            "#00013F（ここまでの流れを踏まえて\x01",
            "  自然に導き出される答え、それは――）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_74DD")

    label("loc_74BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74D5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_74D5")

    SetScenarioFlags(0x0, 2)
    Jump("loc_74DD")

    label("loc_74DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_74EB")
    Jump("loc_74F0")

    label("loc_74EB")

    Jump("loc_7293")

    label("loc_74F0")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0340
    ChrTalk(
        0x101,
        (
            "#6P#00003F兄貴が警戒しつつも、\x01",
            "よく知っていた人物――\x02\x03",

            "#00001Fそんな犯人像が\x01",
            "考えられると思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0341
    ChrTalk(
        0x103,
        "#6P#00205Fえ……\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        "#12P#00301Fそいつは……\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x11,
        "#5Pふむ、その理由は？\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#6P#00003F……まず兄貴は\x01",
            "現場に向かうことを誰にも\x01",
            "明かしていませんでした。\x02\x03",

            "#00008Fそれに状況からして、\x01",
            "単身で乗り込んだことは\x01",
            "ほぼ間違いありません。\x02\x03",

            "#00013Fこのことから考えても、\x01",
            "犯人が『知人』である可能性は\x01",
            "かなり高いと言えると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x102,
        "#6P#00106Fた、確かに……\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#6P#00006F兄貴の方から呼び出したか、\x01",
            "あるいは呼び出されたか……\x01",
            "それは分かりません。\x02\x03",

            "#00003F場所は人気のない建設現場――\x02\x03",

            "#00008Fつまり他人には決して\x01",
            "聞かれたくない、聞かれてはいけない、\x01",
            "重要な話だったんでしょう。\x02\x03",

            "#00013Fそこで何らかのやり取りがあり……\x01",
            "それが決裂した結果、命を落とすことに\x01",
            "なったのではないでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x11,
        "#5Pそのやり取りというのは……？\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#6P#00003F具体的には分かりません。\x02\x03",

            "#00008Fただ、命まで奪う必要が\x01",
            "あったことを考えると、\x01",
            "内容もそれに相当する……\x02\x03",

            "#00001F例えばそうですね……\x01",
            "『何らかの陰謀』に関わる事とか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0349
    ChrTalk(
        0x103,
        "#6P#00200F陰謀、ですか……\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x11,
        "#5Pふむ……\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#6P#00003F……ニールセンさんは、\x01",
            "『大局を掴めば光を当てられる』\x01",
            "そう仰いましたね。\x02\x03",

            "#00000Fそれを聞いた時、朧げながら\x01",
            "何かが繋がるのを感じたんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0352
    ChrTalk(
        0x11,
        "#5Pほう……\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        (
            "#6P#00006F兄貴が迫っていた可能性のある\x01",
            "何らかの陰謀……\x02\x03",

            "#00003FそれはＤ∴Ｇ教団やマフィア、\x01",
            "帝国や共和国と関係しながらも\x01",
            "それらとは別の主体――\x02\x03",

            "#00008Fそんな存在により進められていた、\x01",
            "あるいは今も進められている――\x02\x03",

            "#00001Fそういうものだと\x01",
            "推測できないでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x102,
        "#6P#00105F別の主体……\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x103,
        "#6P#00201Fそれも、現在進行形……\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        (
            "#6P#00001Fああ、兄貴の殺害犯が未だに\x01",
            "見つかっていないことからも\x01",
            "それが言えるはずだ。\x02\x03",

            "#00003Fそして、そのことこそが\x01",
            "事件がまだ終わっていないという、\x01",
            "何よりの証明のように思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x11,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0358
    ChrTalk(
        0x101,
        (
            "#6P#00005Fニールセンさん？\x02\x03",

            "#00006F……やはり、無理がありますかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x11)
    Sleep(500)

    #C0359
    ChrTalk(
        0x11,
        (
            "#5Pいえ……\x01",
            "見事な推理だと思いましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x11,
        "#5P──ずばり、ロイドさん。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x11,
        (
            "#5Pここまで検証を重ねてみて\x01",
            "思い当たる人物はいましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x11,
        (
            "#5P３年前、ガイさんを呼び出し、\x01",
            "殺害したと思われる人物は……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0363
    ChrTalk(
        0x101,
        (
            "#6P#00006Fいえ、残念ながら……\x02\x03",

            "#00003F『知人』といっても、呆れるくらい\x01",
            "顔が広かった兄貴のことです。\x02\x03",

            "#00008F……現場から持ち去られて\x01",
            "いまだ見付かっていないトンファーや\x01",
            "背後から急所を撃たれたという事実……\x02\x03",

            "#00013F個人的には、それらの要素が\x01",
            "事件解明の鍵になりそうな\x01",
            "気がしていますが……\x02\x03",

            "#00006Fそれだけで特定できるのなら\x01",
            "３年前の時点で、捜査一課が\x01",
            "とっくに突き止めていると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x11,
        "#5Pふむ、道理ですね。\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x11,
        (
            "#5P現時点で、犯人を特定できる\x01",
            "全てのピースは出揃っていません。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x11,
        (
            "#5P――ですが、これだけは\x01",
            "はっきりと言えます。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x11,
        (
            "#5P足りない最後のピースを見つけるのは\x01",
            "ロイドさん──貴方だけでしょう。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0368
    ChrTalk(
        0x102,
        "#6P#00105Fニールセンさん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0369
    ChrTalk(
        0x101,
        "#6P#00004Fええ……そのつもりです。\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)

    #C0370
    ChrTalk(
        0x11,
        "#5Pふふ、それを聞けてよかった。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x11,
        (
            "#5P……まるで３年前、\x01",
            "ガイさんとしていた情報交換の約束を\x01",
            "果たせたような気分です。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x11,
        (
            "#5P付き合って頂いて\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        (
            "#6P#00000Fいえ、こちらこそ……\x01",
            "本当にありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x11,
        (
            "#5Pでは私はこれで――\x01",
            "皆さんのご活躍に期待しています。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x11, 0x22)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -8170, 0, -500, 90)
    OP_0D()
    Sleep(500)

    def lambda_8275():
        OP_95(0xFE, -7730, 0, 1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8275)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x11, 1)

    def lambda_82A5():
        OP_95(0xFE, 690, 0, 1520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_82A5)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    WaitChrThread(0x11, 1)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)

    #C0375
    ChrTalk(
        0x103,
        (
            "#6P#00202Fニールセンさん……\x01",
            "まるでわたしたちを\x01",
            "導いてくれたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        (
            "#5P#00004Fああ……多分、兄貴との約束を\x01",
            "ずっと気に掛けてくれていたんだろう。\x02\x03",

            "#00002F話せて本当に良かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x102,
        "#6P#00109Fふふ……そうね。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        "#6P#00304Fだな。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x1)
    Sleep(300)

    #C0379
    ChrTalk(
        0x104,
        (
            "#6P#00301F#12P……よし、発破もかけられた事だし\x01",
            "そろそろ行くとするか！\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        (
            "#5P#00003Fああ……とにかく今は\x01",
            "ルバーチェ跡の会長室に急ごう。\x02\x03",

            "#00013Fレクター大尉から\x01",
            "何らかの情報を引き出せるはずだ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0381
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【ガイ・バニングス殺害事件の検証】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_853B")
    OP_2C(0x95, 0x2)
    Jump("loc_854F")

    label("loc_853B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_854F")
    OP_2C(0x95, 0x1)

    label("loc_854F")

    ClearChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x0)
    SetChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, -4660, 0, 1270, 90)
    OP_69(0xFF, 0x0)
    OP_29(0x95, 0x1, 0x0)
    OP_29(0x95, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_17_57E8 end

    SaveToFile()

Try(main)
