from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c115c.bin",                # FileName
        "c115c",                    # MapName
        "c115c",                    # Location
        0x0018,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 24, 0, 1, 0, 2],
    )

    BuildStringList((
        "c115c",                  # 0
        "受付嬢レベッカ",         # 1
        "受付嬢フラン",           # 2
        "受付嬢フラン",           # 3
        "ドノバン警部",           # 4
        "レイモンド捜査官",       # 5
        "警官",                   # 6
        "ジョーリッジ課長",       # 7
        "エマ捜査官",             # 8
        "容疑者",                 # 9
        "警官",                   # 10
        "セルゲイ課長",           # 11
        "青年",                   # 12
        "キリカ",                 # 13
        "偽ブランド商",           # 14
        "レイモンド捜査官",       # 15
        "ケイト巡査",             # 16
    ))

    AddCharChip((
        "chr/ch30400.itc",                   # 00
        "chr/ch06900.itc",                   # 01
        "chr/ch06902.itc",                   # 02
        "chr/ch30100.itc",                   # 03
        "chr/ch30100.itc",                   # 04
        "chr/ch21000.itc",                   # 05
        "chr/ch30000.itc",                   # 06
        "chr/ch30300.itc",                   # 07
        "chr/ch30200.itc",                   # 08
        "chr/ch30500.itc",                   # 09
        "chr/ch30202.itc",                   # 0A
        "chr/ch24102.itc",                   # 0B
        "chr/ch30600.itc",                   # 0C
        "chr/ch02502.itc",                   # 0D
        "chr/ch23602.itc",                   # 0E
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

    DeclNpc(-100,    0,       15399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(3000,    0,       15930,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-9600,   100,     18239,   270,  469,  0x0, 0,   2,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-125379, 0,       19520,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-125080, 150,     16309,   90,   469,  0x0, 0,   13,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(-122440, 150,     16180,   270,  469,  0x0, 0,   14,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-122300, 150,     16500,   270,  469,  0x0, 0,   11,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-125080, 150,     16500,   90,   469,  0x0, 0,   10,  0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-59229,  29,      21360,   270,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)

    DeclEvent(0x0000, 0, 31,  -12.699999809265137,   19.8700008392334,      -0.5,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    0.0,                   4.233333587646484,     -9.9350004196167,      0.1428571492433548,    1.0])

    DeclActor(-100,    0,       14400,   1100,    -100,    1500,    15400,   0x007E, 0,  3,  0x0000)
    DeclActor(2770,    0,       14280,   1000,    3000,    1500,    15930,   0x007E, 0,  7,  0x0000)
    DeclActor(-34480,  0,       20000,   1000,    -34480,  1000,    20000,   0x007C, 0,  18, 0x0000)
    DeclActor(-9850,   0,       16000,   1000,    -9850,   1500,    16000,   0x007C, 0,  32, 0x0000)
    DeclActor(-9850,   0,       13750,   1000,    -9850,   1500,    13750,   0x007C, 0,  32, 0x0000)

    ScpFunction((
        "Function_0_464",          # 00, 0
        "Function_1_51C",          # 01, 1
        "Function_2_75D",          # 02, 2
        "Function_3_7C9",          # 03, 3
        "Function_4_7CD",          # 04, 4
        "Function_5_C48",          # 05, 5
        "Function_6_13DB",         # 06, 6
        "Function_7_14C3",         # 07, 7
        "Function_8_14C7",         # 08, 8
        "Function_9_1FBF",         # 09, 9
        "Function_10_22B7",        # 0A, 10
        "Function_11_23DE",        # 0B, 11
        "Function_12_26C0",        # 0C, 12
        "Function_13_27A6",        # 0D, 13
        "Function_14_2A8C",        # 0E, 14
        "Function_15_2B8C",        # 0F, 15
        "Function_16_2C39",        # 10, 16
        "Function_17_2DD4",        # 11, 17
        "Function_18_3031",        # 12, 18
        "Function_19_30CD",        # 13, 19
        "Function_20_3270",        # 14, 20
        "Function_21_348A",        # 15, 21
        "Function_22_3533",        # 16, 22
        "Function_23_35C3",        # 17, 23
        "Function_24_481D",        # 18, 24
        "Function_25_49DB",        # 19, 25
        "Function_26_5636",        # 1A, 26
        "Function_27_6477",        # 1B, 27
        "Function_28_650B",        # 1C, 28
        "Function_29_657A",        # 1D, 29
        "Function_30_8006",        # 1E, 30
        "Function_31_9032",        # 1F, 31
        "Function_32_90CC",        # 20, 32
    ))


    def Function_0_464(): pass

    label("Function_0_464")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_4A4"),
        (1, "loc_4B0"),
        (2, "loc_4BC"),
        (3, "loc_4C8"),
        (4, "loc_4D4"),
        (5, "loc_4E0"),
        (6, "loc_4EC"),
        (SWITCH_DEFAULT, "loc_4F8"),
    )


    label("loc_4A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_504")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_51B")

    Return()

    # Function_0_464 end

    def Function_1_51C(): pass

    label("Function_1_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_52B")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 29)

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_57B")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -12850, 0, 7690, 90)
    SetChrPos(0xC, -11260, 0, 7690, 270)
    SetChrPos(0xE, -11040, 0, 13810, 90)
    Jump("loc_75C")

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_598")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_598")

    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0xB, -10370, 0, 7070, 270)
    SetChrPos(0x17, -11980, 0, 8189, 135)
    SetChrPos(0xE, -11930, 0, 7110, 90)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -58050, 0, 15900, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_75C")

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_637")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -58050, 0, 15900, 90)
    Jump("loc_75C")

    label("loc_637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6E0")
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_67B")
    SetChrPos(0xB, -124850, 0, 14920, 45)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_6B9")

    label("loc_67B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_697")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_6B9")

    label("loc_697")

    SetChrPos(0xB, -57730, 0, 16309, 180)
    SetChrPos(0xC, -57730, 0, 14480, 0)

    label("loc_6B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6DB")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -11040, 0, 13810, 90)

    label("loc_6DB")

    Jump("loc_75C")

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_75C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x10, -12850, 0, 7690, 90)
    SetChrPos(0xD, -11260, 0, 7690, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -11040, 0, 13810, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_757")
    SetChrPos(0xE, -58050, 0, 15900, 90)
    Jump("loc_75C")

    label("loc_757")

    SetChrFlags(0xE, 0x80)

    label("loc_75C")

    Return()

    # Function_1_51C end

    def Function_2_75D(): pass

    label("Function_2_75D")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_779")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    Jump("loc_7C8")

    label("loc_779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_END)), "loc_787")
    Jump("loc_7C8")

    label("loc_787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7A3")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_65(0x1, 0x1)
    Jump("loc_7C8")

    label("loc_7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7B1")
    Jump("loc_7C8")

    label("loc_7B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7BF")
    Jump("loc_7C8")

    label("loc_7BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7C8")

    label("loc_7C8")

    Return()

    # Function_2_75D end

    def Function_3_7C9(): pass

    label("Function_3_7C9")

    Call(0, 4)
    Return()

    # Function_3_7C9 end

    def Function_4_7CD(): pass

    label("Function_4_7CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_816")
    TalkBegin(0x8)
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_811")
    FadeToDark(1000, 0, -1)
    OP_0D()
    TalkEnd(0x8)
    Call(0, 25)
    Return()

    label("loc_811")

    Jump("loc_837")

    label("loc_816")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_837")
    Call(0, 23)
    Return()

    label("loc_837")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B8E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_880")

    #C0001
    ChrTalk(
        0x8,
        (
            "手配魔獣の討伐、\x01",
            "お疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_880")


    #C0002
    ChrTalk(
        0x8,
        (
            "そうそう、ご存知ですか？\x01",
            "現在クロスベル警察では\x01",
            "魔獣の情報調査を行っているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        "#0005F情報調査……ですか？\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "ええ、戦闘手帳には\x01",
            "魔獣についての項目があるのは\x01",
            "ご存知だと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "戦ったことのある魔獣は\x01",
            "戦闘手帳に記述されていくんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "もし情報がある程度溜まったら、\x01",
            "私の方に見せてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "皆さんの集めた情報を元に\x01",
            "署内で安全対策に\x01",
            "役立たせてもらいますから。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A5A")

    #C0008
    ChrTalk(
        0x102,
        (
            "#0100Fなるほど……警察も\x01",
            "色々な工夫をしているんですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF7")

    label("loc_A5A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAE")

    #C0009
    ChrTalk(
        0x103,
        (
            "#0200Fなるほど……警察も\x01",
            "色々な工夫をしているようですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF7")

    label("loc_AAE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF7")

    #C0010
    ChrTalk(
        0x104,
        (
            "#0300Fなるほど……警察も\x01",
            "色々な工夫をしてるんスね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF7")


    #C0011
    ChrTalk(
        0x8,
        (
            "ええ、これも市民の安全を\x01",
            "守るためですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "魔獣の情報を見せていただく際には\x01",
            "多少の手当ても支給しますよ。\x01",
            "気軽に立ち寄ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 2)
    SetScenarioFlags(0x1, 3)

    label("loc_B8E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C44")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",              # 0
            "戦闘手帳を見せる\x01",      # 1
            "やめる\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 4)
    Call(0, 30)
    Jump("loc_C3F")

    label("loc_C0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C23")
    Jump("loc_C3F")

    label("loc_C23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_C3F")

    Jump("loc_B98")

    label("loc_C44")

    TalkEnd(0x8)
    Return()

    # Function_4_7CD end

    def Function_5_C48(): pass

    label("Function_5_C48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2A")

    #C0013
    ChrTalk(
        0x8,
        "皆さんお疲れ様ですね。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "違法駐車の取り締まりが終わったら\x01",
            "私の方にお問い合わせ下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "また広域防犯課の方々を\x01",
            "お呼びしますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0000Fええ、その時は\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_DF5")

    #C0017
    ChrTalk(
        0x8,
        (
            "魔獣の情報がある程度溜まったら\x01",
            "私の方に見せてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "皆さんの集めた情報を元に\x01",
            "安全対策に役立たせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "多少の手当ても支給しますから\x01",
            "気軽に立ち寄ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E77")

    #C0020
    ChrTalk(
        0x8,
        "ふふ、皆さんお疲れ様でした。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "記念祭中は事件も\x01",
            "増えているみたいですけど……\x01",
            "無理せずに頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_EFF")

    #C0022
    ChrTalk(
        0x8,
        (
            "夕暮れを告げる大聖堂の鐘の後、\x01",
            "閉会式が執り行われる予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "そろそろ私たちも\x01",
            "準備を手伝わないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_END)), "loc_FFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F97")

    #C0024
    ChrTalk(
        0x8,
        (
            "毎年、記念祭では\x01",
            "迷子が何人も出ているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "今年は多かったですね……\x01",
            "２０件くらいは\x01",
            "あったんじゃないでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FF6")

    label("loc_F97")


    #C0026
    ChrTalk(
        0x8,
        (
            "どんなお子さんのご両親も\x01",
            "心配で仕方ないのは皆同じ……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "どうか力になってあげて下さい。\x02",
    )

    CloseMessageWindow()

    label("loc_FF6")

    Jump("loc_13DA")

    label("loc_FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_10ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1086")

    #C0028
    ChrTalk(
        0x8,
        (
            "ふう、ようやく\x01",
            "人の波が引きましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "フランも疲れているようだし……\x01",
            "今日は早めに上がらせようかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10E8")

    label("loc_1086")


    #C0030
    ChrTalk(
        0x8,
        (
            "フランなら自販機の近くで\x01",
            "休憩していると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "よかったら声を\x01",
            "かけてあげてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E8")

    Jump("loc_13DA")

    label("loc_10ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_11B4")

    #C0032
    ChrTalk(
        0x8,
        (
            "今日は市内で記念パレードの\x01",
            "行進が予定されています。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "問い合わせが何十件も来ていますし、\x01",
            "市民の誘導もしなくてはいけません。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "さてと……気合いを\x01",
            "入れる必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_11B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_137F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C4")

    #C0035
    ChrTalk(
        0x8,
        (
            "今日は、市庁舎の方で\x01",
            "シンポジウムが開催されるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "一般の市民や観光客が\x01",
            "集まるようなものではありませんが\x01",
            "各国の知識人が多数出席されます。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "クロスベルからは、市長を始め、\x01",
            "ＩＢＣ総裁やグリムウッド先生なども\x01",
            "参加されるそうですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_137A")

    label("loc_12C4")


    #C0038
    ChrTalk(
        0x8,
        (
            "もちろん警備は警察の担当ですが\x01",
            "あのアリオス・マクレイン氏も\x01",
            "特別に警備に参加されるとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "上層部としては複雑でしょうが\x01",
            "各国の関係者の手前、\x01",
            "反対できなかったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137A")

    Jump("loc_13DA")

    label("loc_137F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_13DA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_139C")
    Call(0, 6)
    Jump("loc_13DA")

    label("loc_139C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_END)), "loc_13D7")
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D2")
    FadeToDark(1000, 0, -1)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    TalkEnd(0x8)
    Return()

    label("loc_13D2")

    Jump("loc_13DA")

    label("loc_13D7")

    Call(0, 6)

    label("loc_13DA")

    Return()

    # Function_5_C48 end

    def Function_6_13DB(): pass

    label("Function_6_13DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1460")

    #C0040
    ChrTalk(
        0x8,
        "あら、支援課の皆さん。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "やはり今年は\x01",
            "例年になく混雑しているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        "支援要請、頑張ってくださいね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C2")

    label("loc_1460")


    #C0043
    ChrTalk(
        0x8,
        (
            "今年の記念祭は例年になく\x01",
            "混雑しているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "皆さんも支援要請、\x01",
            "頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C2")

    Return()

    # Function_6_13DB end

    def Function_7_14C3(): pass

    label("Function_7_14C3")

    Call(0, 8)
    Return()

    # Function_7_14C3 end

    def Function_8_14C7(): pass

    label("Function_8_14C7")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1760")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F1")

    #C0045
    ChrTalk(
        0x9,
        (
            "#1903F記念祭も今日で最終日……\x01",
            "何とか乗り切れそうです～。\x02\x03",

            "#1900F皆さんも\x01",
            "本当にお疲れさまです。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#0000Fはは、フランもお疲れ。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        (
            "#0203F（わたしたちの最大の山場は\x01",
            "  これからですが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#0100F（まあ、巻き込みたくないし\x01",
            "  彼女には黙っておきましょう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_175B")

    label("loc_15F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16DB")

    #C0049
    ChrTalk(
        0x9,
        (
            "#1905Fそういえば……セルゲイ警部も\x01",
            "会議で本部にいらっしゃってますよ。\x02\x03",

            "#1900Fお会いになって行きます？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#0000Fいや、今はいいよ。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#0300Fフランちゃん、\x01",
            "お互いもう一頑張りしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        "#1900Fあ、はいっ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_175B")

    label("loc_16DB")


    #C0053
    ChrTalk(
        0x9,
        (
            "#1900F最終日だけあって忙しいですけど\x01",
            "何とか頑張れそうです。\x02\x03",

            "#1906Fは～、でもやっぱり初日に\x01",
            "お休みがもらえてよかったぁ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175B")

    Jump("loc_1FBB")

    label("loc_1760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_END)), "loc_17EA")

    #C0054
    ChrTalk(
        0x9,
        (
            "#1900Fあ、皆さん。\x02\x03",

            "依頼者のハロルドさんは\x01",
            "ここを出てすぐ近くの\x01",
            "噴水前でお待ちのはずです。\x02\x03",

            "よろしくお願いしますね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FBB")

    label("loc_17EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_17F8")
    Jump("loc_1FBB")

    label("loc_17F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1919")
    OP_93(0x9, 0x5A, 0x0)
    SetChrName("")

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フランが通信器でやり取りをしている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0056
    ChrTalk(
        0x9,
        (
            "#1903Fはい、はい……\x02\x03",

            "#1901F本日のパレードは１２時からで\x01",
            "市庁舎前からスタートします。\x02\x03",

            "その後は歓楽街に出てから\x01",
            "市内をぐるっと一巡して……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1914")

    #C0057
    ChrTalk(
        0x101,
        (
            "#0000F（忙しそうだな……\x01",
            "  話しかけるのは止めておくか。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1914")

    Jump("loc_1FBB")

    label("loc_1919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1B6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAF")

    #C0058
    ChrTalk(
        0x9,
        (
            "#1900F皆さん、昨日は\x01",
            "どうもお疲れさまでした～。\x02\x03",

            "遊撃士と不良さんたち相手に\x01",
            "大活躍したそうですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#0000Fい、いや～……\x01",
            "大活躍っていうか。\x02\x03",

            "#0006F警察官としては、\x01",
            "ちょっとハシャギすぎたかと\x01",
            "反省してるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#0306Fま、それはそうかもな。\x02\x03",

            "おかげで今日は\x01",
            "微妙に筋肉痛だしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#0111Fそれは自業自得でしょう。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "#1909Fクスクス……\x01",
            "本当にお疲れさまです～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1B65")

    label("loc_1AAF")


    #C0063
    ChrTalk(
        0x9,
        (
            "#1900Fそういえば、受付の方も\x01",
            "忙しくなってきてまして～。\x02\x03",

            "今日のシンポジウムに加えて\x01",
            "明日のパレードの問い合わせが\x01",
            "増えてきているんです。\x02\x03",

            "#1906Fはあ……\x01",
            "明日は大変そうですね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B65")

    Jump("loc_1FBB")

    label("loc_1B6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_1BF7")

    #C0064
    ChrTalk(
        0x9,
        (
            "#1900Fあ、皆さん。\x01",
            "旧市街の不良さんたちは\x01",
            "港湾区で喧嘩してるみたいです。\x02\x03",

            "お手数ですけど、\x01",
            "どうかよろしくお願いします～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FBB")

    label("loc_1BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1FBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3C")

    #C0065
    ChrTalk(
        0x9,
        (
            "#1900F皆さん、お疲れ様です！\x02\x03",

            "#1909Fえへへ、実は私も昨日は\x01",
            "お休みをもらっていまして。\x02\x03",

            "お姉ちゃんと久々に\x01",
            "たくさん遊んだんですよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_1EC7")

    #C0066
    ChrTalk(
        0x9,
        (
            "#1900Fそうそう、ロイドさんとは\x01",
            "一緒にミニライブを\x01",
            "見に行ったんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#0009Fはは、楽しかったよ。\x01",
            "誘ってくれてありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        "#0111Fふーん、そうだったの……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0300Fお、そのライブなら\x01",
            "俺も見に行ってたぞ。\x02\x03",

            "#0309Fウルスラ病院の\x01",
            "看護師の子たちと一緒に\x01",
            "ノリノリで踊ってやったぜ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE9")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1DE9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E0F")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1E0F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E35")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1E35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E5B")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1E5B")

    Sleep(1000)

    #C0070
    ChrTalk(
        0x103,
        (
            "#0211Fランディさん、\x01",
            "はしゃぎすぎです。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#0000Fはは、それじゃあ\x01",
            "どこかですれ違ったかもな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F34")

    label("loc_1EC7")


    #C0072
    ChrTalk(
        0x101,
        (
            "#0000Fはは、楽しめたみたいだな。\x02\x03",

            "それじゃフラン、\x01",
            "記念祭中もよろしくな。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        "#1900Fはい、了解ですっ！\x02",
    )

    CloseMessageWindow()

    label("loc_1F34")

    SetScenarioFlags(0xB1, 3)
    Jump("loc_1FBB")

    label("loc_1F3C")


    #C0074
    ChrTalk(
        0x9,
        (
            "#1900F記念祭中は雑用が\x01",
            "たくさんあるんですよ～。\x02\x03",

            "支援要請も\x01",
            "たくさん入ると思いますけど、\x01",
            "あまり無理はしないで下さいね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FBB")

    TalkEnd(0x9)
    Return()

    # Function_8_14C7 end

    def Function_9_1FBF(): pass

    label("Function_9_1FBF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2053")
    Jump("loc_209D")

    label("loc_2053")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2073")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_209D")

    label("loc_2073")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2093")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_209D")

    label("loc_2093")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_209D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_220E")

    #C0075
    ChrTalk(
        0xFE,
        (
            "#1906Fうう、ぐったり……\x02\x03",

            "#1900Fパレードに関する問い合わせが\x01",
            "市民や観光客から殺到してて……\x02\x03",

            "#1906Fようやく一息付けました～……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#0000Fはは、お疲れさま。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#0100Fふふ、ずいぶんと\x01",
            "賑わってたみたいだものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        (
            "#0300Fせめてジュースでも\x01",
            "奢らせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "#1906Fううっ……\x01",
            "ありがとうございます～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_22AF")

    label("loc_220E")


    #C0080
    ChrTalk(
        0xFE,
        (
            "#1903Fさてと……一息入れたら\x01",
            "また頑張らなくっちゃ。\x02\x03",

            "#1901F記念祭はまだ\x01",
            "あと１日ありますし！\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0000F（頑張り屋なところは\x01",
            "  姉妹で似てるみたいだな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22AF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_1FBF end

    def Function_10_22B7(): pass

    label("Function_10_22B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_22C5")
    Jump("loc_23DD")

    label("loc_22C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2341")
    TalkBegin(0xFE)

    #C0082
    ChrTalk(
        0xFE,
        (
            "閉会式の人員は\x01",
            "強化した方がいいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "例年より人が多い。\x01",
            "気合入れねえとヤバそうだぞ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_23DD")

    label("loc_2341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_234F")
    Jump("loc_23DD")

    label("loc_234F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_23D4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_23CC")
    TalkBegin(0xFE)

    #C0084
    ChrTalk(
        0xFE,
        (
            "やれやれ、バーさん……\x01",
            "ちったあ反省してるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        "……まぁ、そんな風にはみえねぇな。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_23CF")

    label("loc_23CC")

    Call(0, 26)

    label("loc_23CF")

    Jump("loc_23DD")

    label("loc_23D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_23DD")

    label("loc_23DD")

    Return()

    # Function_10_22B7 end

    def Function_11_23DE(): pass

    label("Function_11_23DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_24CA")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247E")

    #C0086
    ChrTalk(
        0xFE,
        "やあ、君たちか～。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "警部たちなら閉会式の\x01",
            "警備体制を会議してるよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "まったく、こっちも\x01",
            "手伝って欲しいんだけどな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_24C2")

    label("loc_247E")


    #C0089
    ChrTalk(
        0xFE,
        (
            "まあ、この混雑も\x01",
            "今日で最後のはずだよ～。\x01",
            "お互い頑張ろうね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C2")

    TalkEnd(0xFE)
    Jump("loc_26BF")

    label("loc_24CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_24D8")
    Jump("loc_26BF")

    label("loc_24D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_24E6")
    Jump("loc_26BF")

    label("loc_24E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_26B6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_26AE")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_258F")
    Jump("loc_25D9")

    label("loc_258F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25AF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25D9")

    label("loc_25AF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25CF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25D9")

    label("loc_25CF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25D9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0090
    ChrTalk(
        0xFE,
        (
            "うーん……取調べって\x01",
            "どれだけやっても慣れないんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "補導少年くらいなら\x01",
            "僕でも対応できるんだけどな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        "#0006F（それは警察としてどうなんだ……？）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_26B1")

    label("loc_26AE")

    Call(0, 26)

    label("loc_26B1")

    Jump("loc_26BF")

    label("loc_26B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_26BF")

    label("loc_26BF")

    Return()

    # Function_11_23DE end

    def Function_12_26C0(): pass

    label("Function_12_26C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26D1")
    Jump("loc_27A2")

    label("loc_26D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2736")

    #C0093
    ChrTalk(
        0xFE,
        "今年は予想以上の人出だな。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "まるでクロスベルの人口が\x01",
            "２倍に増えたみたいだぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27A2")

    label("loc_2736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2744")
    Jump("loc_27A2")

    label("loc_2744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2752")
    Jump("loc_27A2")

    label("loc_2752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_27A2")

    #C0095
    ChrTalk(
        0xFE,
        "……容疑者連行！\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "まったく祭りの最中に\x01",
            "不届きなやつだよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27A2")

    TalkEnd(0xFE)
    Return()

    # Function_12_26C0 end

    def Function_13_27A6(): pass

    label("Function_13_27A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2889")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_282D")

    #C0097
    ChrTalk(
        0xFE,
        (
            "あー……今日も\x01",
            "外は賑やかだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "まあ私はコーヒーを\x01",
            "買いに来ただけだから。\x01",
            "気にせんでくれー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2884")

    label("loc_282D")


    #C0099
    ChrTalk(
        0xFE,
        "実はまだ会議中でなぁ……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "まあ、私が抜け出していた事は\x01",
            "さくっと忘れてくれー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2884")

    Jump("loc_2A88")

    label("loc_2889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_28F3")

    #C0101
    ChrTalk(
        0xFE,
        (
            "うーん、じゃあ\x01",
            "二課も手伝ってくれる？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        "広域防犯課#10Rウ　　チ#も手一杯なんだが……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A88")

    label("loc_28F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2901")
    Jump("loc_2A88")

    label("loc_2901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_29E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A6")

    #C0103
    ChrTalk(
        0xFE,
        (
            "……さっきドノバン君らが\x01",
            "何人も連行して行ったぞー。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "なんだー、あの人ごみは……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "みんなちょっと\x01",
            "張り切りすぎじゃないのかー？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_29DD")

    label("loc_29A6")


    #C0106
    ChrTalk(
        0xFE,
        (
            "あー、記念祭だからって\x01",
            "みんな張り切りすぎだろー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29DD")

    Jump("loc_2A88")

    label("loc_29E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2A88")

    #C0107
    ChrTalk(
        0xFE,
        (
            "うーむ、やはり\x01",
            "記念祭中は大忙しだなぁ……\x01",
            "ゆっくりコーヒーを飲む暇もないぞー。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "……あーともかく今日は助かったぞー。\x01",
            "またよろしくなぁ、特務支援課。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A88")

    TalkEnd(0xFE)
    Return()

    # Function_13_27A6 end

    def Function_14_2A8C(): pass

    label("Function_14_2A8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A9D")
    Jump("loc_2B88")

    label("loc_2A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2B00")

    #C0109
    ChrTalk(
        0xFE,
        "パレードが終わったようですね。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "私も港湾区の重点警備に\x01",
            "戻るとしましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B88")

    label("loc_2B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2B88")

    #C0111
    ChrTalk(
        0xFE,
        (
            "ダドリーさんは\x01",
            "帝国へ出張なさっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "このお忙しい時に\x01",
            "とんぼ返りの出張だなんて……\x01",
            "上も何を考えているのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B88")

    TalkEnd(0xFE)
    Return()

    # Function_14_2A8C end

    def Function_15_2B8C(): pass

    label("Function_15_2B8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE4")

    #C0113
    ChrTalk(
        0xFE,
        (
            "うおお……\x01",
            "わしは何もしとらん！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        "しとらんったらしとらん！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2C35")

    label("loc_2BE4")


    #C0115
    ChrTalk(
        0xFE,
        (
            "……まさかあんな所に\x01",
            "警官が来るとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        "こうなったら黙秘してやるわい！\x02",
    )

    CloseMessageWindow()

    label("loc_2C35")

    TalkEnd(0xFE)
    Return()

    # Function_15_2B8C end

    def Function_16_2C39(): pass

    label("Function_16_2C39")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2CFD")
    OP_4B(0xC, 0xFF)

    #C0117
    ChrTalk(
        0xFE,
        (
            "レイモンドさん、\x01",
            "もう取調室も一杯です！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        "どうしましょ！？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        (
            "よーし、いざとなったら\x01",
            "会議室も使っちゃうぞー！\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xC,
        (
            "でもそれより巡回だよ～。\x01",
            "駅前通り、行くぞ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    Jump("loc_2DD0")

    label("loc_2CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2DD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D97")

    #C0121
    ChrTalk(
        0xFE,
        (
            "港湾区と歓楽街から\x01",
            "応援要請が来てるんだ。\x01",
            "巡回を強化してくれってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "やれやれ……一息ついたら\x01",
            "急いで行かなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2DD0")

    label("loc_2D97")


    #C0123
    ChrTalk(
        0xFE,
        (
            "記念祭は休む暇もないよ。\x01",
            "急いで巡回に戻らないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DD0")

    TalkEnd(0xFE)
    Return()

    # Function_16_2C39 end

    def Function_17_2DD4(): pass

    label("Function_17_2DD4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E68")
    Jump("loc_2EB2")

    label("loc_2E68")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E88")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EB2")

    label("loc_2E88")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EA8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EB2")

    label("loc_2EA8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EB2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FCB")
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    OP_4B(0xB, 0xFF)

    #C0124
    ChrTalk(
        0xFE,
        (
            "#5Sア、アンタたち……\x01",
            "よくもまぁアタシの前に\x01",
            "顔を出せたもんだね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "#5Sまた来年の記念祭に\x01",
            "来てやるからねぇ！！\x01",
            "せいぜい覚えておくんだね！！\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        (
            "……ほら、バーさんこっち向け。\x01",
            "取調べ中だぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x1, 2)
    Jump("loc_3029")

    label("loc_2FCB")

    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0127
    ChrTalk(
        0xFE,
        (
            "#5Sまた来年の記念祭に\x01",
            "来てやるからねぇ！！\x01",
            "せいぜい覚えておくんだね！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3029")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_2DD4 end

    def Function_18_3031(): pass

    label("Function_18_3031")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_30C1")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "「～　取調室・使用中　～\x01",
            "　　ただ今取り調べ中です。\x01",
            "　　　　　　広域防犯課」\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_30CA")

    label("loc_30C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_30CA")

    label("loc_30CA")

    EventEnd(0x1)
    Return()

    # Function_18_3031 end

    def Function_19_30CD(): pass

    label("Function_19_30CD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3161")
    Jump("loc_31AB")

    label("loc_3161")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3181")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31AB")

    label("loc_3181")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31A1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31AB")

    label("loc_31A1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31AB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E2")
    Call(0, 20)
    Jump("loc_3268")

    label("loc_31E2")


    #C0129
    ChrTalk(
        0xFE,
        (
            "#1004Fスパー……\x01",
            "外は丁度パレードが\x01",
            "終わった頃か。\x02\x03",

            "#1000Fやれやれ、今年は\x01",
            "人出が多くていけねえな。\x01",
            "おちおち本を読む間もねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3268")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_30CD end

    def Function_20_3270(): pass

    label("Function_20_3270")


    #C0130
    ChrTalk(
        0xFE,
        (
            "#1005Fおう、お前らか。\x02\x03",

            "#1006F屋上でサボってたんだが\x01",
            "仕事を回されてな……\x02\x03",

            "捜査官資格を持ってる連中が\x01",
            "他にいねえんだと。\x01",
            "ったく、やれやれだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        "#0003F課長、仕事をしてください。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x104,
        (
            "#0306Fこっちは\x01",
            "クソ忙しいってのによ……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        "#0201Fちょっと信じられないです。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "#1000F……怒んなよ。\x01",
            "ほれ、こいつをやるからよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2CD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0136
    ChrTalk(
        0xFE,
        (
            "#1006F今日中に読破する\x01",
            "予定だったんだが、\x01",
            "シゴトが入っちまったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        (
            "#0100Fふう、サボってこれを\x01",
            "読んでいたわけですね……\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber(0x2CD, 1)
    SetScenarioFlags(0x9C, 7)
    Return()

    # Function_20_3270 end

    def Function_21_348A(): pass

    label("Function_21_348A")

    TalkBegin(0xFE)
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0138
    ChrTalk(
        0xFE,
        (
            "お、俺たち\x01",
            "《ブラックエンペラー》を\x01",
            "舐めんなよぅ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x12,
        (
            "#1006F……ああ判ったから\x01",
            "名前だ、名前。\x02\x03",

            "#1000Fほれ、とっとと言えよ\x01",
            "バカヤロウ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_348A end

    def Function_22_3533(): pass

    label("Function_22_3533")

    TalkBegin(0xFE)

    #C0140
    ChrTalk(
        0xFE,
        (
            "今年は予想以上の人出で\x01",
            "あちこち手が回ってないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "まだまだトラブルが\x01",
            "絶えないんじゃないかしら……\x01",
            "ロイド君たちも気を付けてね！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_3533 end

    def Function_23_35C3(): pass

    label("Function_23_35C3")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(-140, 1540, 13420, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    SetChrPos(0x101, 400, 0, 13450, 0)
    SetChrPos(0x102, -600, 0, 13200, 0)
    SetChrPos(0x103, 400, 0, 11950, 0)
    SetChrPos(0x104, -600, 0, 11700, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    #C0142
    ChrTalk(
        0x8,
        "#5Pあら、支援課の皆さん。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "#5P……ふう、やはり今年は\x01",
            "例年になく混雑しているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#12P#0000Fレベッカさんも\x01",
            "お忙しそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#6P#0104Fふふ、記念祭は警察も\x01",
            "たくさん仕事がありますものね。\x02\x03",

            "#0100F実は広域防犯課からの\x01",
            "支援要請で来たのですけど……\x01",
            "担当の方はいらっしゃいますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        "#5Pええ、『違法駐車取り締まり』の件ですね。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "#5P皆さん飛び回ってらっしゃいますけど……\x01",
            "今お呼びすれば、何とか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37F6():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37F6)
    Sleep(100)

    def lambda_3806():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3806)

    def lambda_3813():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3813)

    def lambda_3820():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3820)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0148
    ChrTalk(
        0x101,
        (
            "#11P#0000Fそれじゃあ……\x01",
            "……お願いしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x103,
        "#12P#0200Fそうですね。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        "#12P#0300Fおう、片付けちまおうぜ。\x02",
    )

    CloseMessageWindow()

    def lambda_38B4():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38B4)

    def lambda_38C1():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38C1)

    def lambda_38CE():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_38CE)

    def lambda_38DB():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_38DB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0151
    ChrTalk(
        0x101,
        "#12P#0000Fそれでは、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "#5P分かりました。\x01",
            "すぐにお呼びしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "#5P皆さんは会議室の方で\x01",
            "お待ちになっていて下さい。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    OP_68(-62770, 2140, 17220, 0)
    MoveCamera(40, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22390, 0)
    OP_68(-62770, 1540, 17220, 2000)
    SetChrPos(0x101, -60500, 150, 20150, 180)
    SetChrPos(0x102, -64000, 150, 20150, 180)
    SetChrPos(0x103, -60500, 150, 15850, 0)
    SetChrPos(0x104, -64000, 150, 15850, 0)
    SetChrPos(0xE, -64599, 40, 8400, 0)
    SetChrPos(0x17, -65400, 40, 8250, 0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x2)
    OP_4B(0xE, 0xFF)
    OP_4B(0x17, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0154
    ChrTalk(
        0x101,
        (
            "#5P#0003Fやっぱり……忙しいのかな。\x01",
            "まだ来ないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        (
            "#6P#0300Fま、祭りがあの様子じゃ\x01",
            "仕方ないっしょ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(103, 0, 100, 0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x1)
    OP_68(-63070, 1540, 14720, 0)
    MoveCamera(37, 13, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23450, 0)
    OP_68(-63070, 1540, 14720, 1000)

    def lambda_3B89():
        OP_97(0xE, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3B89)

    def lambda_3BA3():
        OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3BA3)
    Sleep(50)

    def lambda_3BB7():
        OP_97(0x17, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3BB7)

    def lambda_3BD1():
        OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3BD1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xE, 2)
    OP_93(0xE, 0x2D, 0x1F4)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x17, 2)
    OP_93(0x17, 0x2D, 0x1F4)
    OP_0D()

    #C0156
    ChrTalk(
        0xE,
        (
            "#12Pおー、スマンスマン。\x01",
            "立て込んでおってなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x17,
        "#6Pゴメンなさい、遅れちゃって……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        "#11P#0000Fいえ、お疲れ様です。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-61850, 1500, 18250, 0)
    MoveCamera(52, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24440, 0)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0x103, 0x2)
    SetChrSubChip(0x104, 0x2)
    SetChrPos(0xE, -57450, 0, 15000, 0)
    SetChrPos(0x17, -57200, 0, 16400, 0)

    def lambda_3CE9():
        OP_97(0xE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3CE9)
    Sleep(50)

    def lambda_3D06():
        OP_97(0x17, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3D06)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x10E, 0x1F4)
    WaitChrThread(0x17, 1)
    OP_93(0x17, 0x10E, 0x1F4)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -59750, 0, 19900, 135)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, -63250, 0, 19900, 90)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, -59750, 0, 16100, 45)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, -63250, 0, 16100, 90)
    ClearChrFlags(0x104, 0x4)
    Sound(820, 0, 100, 0)
    OP_0D()

    #C0159
    ChrTalk(
        0xE,
        (
            "#11Pあー、広域防犯課課長の\x01",
            "ジョーリッジだ。\x01",
            "よろしくなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x17,
        (
            "#5P同じく広域防犯課の\x01",
            "ケイト巡査であります。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x17,
        (
            "#5P特務支援課殿、\x01",
            "協力感謝いたします！\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#6P#0005F（そうか、一応こういった\x01",
            "  挨拶が必要なのか……）\x02\x03",

            "#0001F──特務支援課\x01",
            "バニングス捜査官、以下４名です。\x02\x03",

            "早速ですが要請内容を\x01",
            "確認させて頂けますでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xE,
        "#11Pおーし、早速説明するぞー。\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xE,
        (
            "#11P……ああ、ここからは大丈夫だー。\x01",
            "ダラけてもらって構わんぞー。\x02",
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

    #C0165
    ChrTalk(
        0x17,
        (
            "#5P……ゴメンね、うちの課長\x01",
            "ちょっとマイペースで。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xE,
        (
            "#11P支援要請にも書いたと思うがー、\x01",
            "……街の郊外に止まっとる\x01",
            "違法駐車を取り締まって欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xE,
        (
            "#11Pといっても、記念祭中は\x01",
            "どこも人手が足らんからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xE,
        (
            "#11P車両ナンバーを控えて、\x01",
            "あとは警告ステッカーを\x01",
            "貼っておく程度でいいぞー。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#6P#0005Fえっと、それだけでいいんですか？\x01",
            "撤去とかは……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xE,
        (
            "#11Pああ、構わんー。\x01",
            "どうせ罰金刑以上にはならんしなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x17,
        (
            "#5P帝国や共和国人も多いから\x01",
            "あまり厳しくできないのよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x17,
        (
            "#5Pそれより、面倒なのは\x01",
            "認可車両だと思うわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0173
    ChrTalk(
        0x103,
        "#12P#0200F認可車両……ですか？\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x17,
        (
            "#5Pええ、実は止まってる車両が\x01",
            "全て違法駐車ってわけじゃないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x17,
        (
            "#5P事前に認可を得てる人も居るから\x01",
            "注意が必要だと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        (
            "#12P#0300Fすると、無許可の駐車車両を\x01",
            "探していけばいいわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x102,
        "#6P#0100Fなるほど、手順は分かりました。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#6P#0003Fたしか街の西口と東口に\x01",
            "それぞれ４、５台\x01",
            "止まっていたはずだ……\x02\x03",

            "#0000F両方回ってみることにしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        "#12P#0200Fですね。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xE,
        (
            "#11Pよーし、それでは\x01",
            "認可車両のナンバーリストを渡すぞ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4411():
        OP_97(0x101, 0x2EE, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4411)

    def lambda_442B():
        OP_95(0xE, -58490, 30, 19160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_442B)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x87, 0x1F4)
    WaitChrThread(0xE, 1)
    Sleep(1000)
    OP_96(0xE, 0xFFFF1F96, 0x0, 0x4844, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0181
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2DB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2DB, 1)

    #C0182
    ChrTalk(
        0x17,
        (
            "#5Pあと、これが\x01",
            "車両に貼る警告ステッカー。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x17,
        (
            "#5P私たちは『違法駐車取り締まりセット』\x01",
            "って呼んでるわ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4527():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4527)
    OP_96(0x17, 0xFFFF1CA8, 0x1E, 0x4DBC, 0x7D0, 0x0)
    Sleep(1000)
    OP_96(0x17, 0xFFFF2090, 0x0, 0x4DBC, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0184
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x348),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x348, 1)

    #C0185
    ChrTalk(
        0x101,
        "#6P#0000F確かにお受け取りしました。\x02",
    )

    CloseMessageWindow()

    def lambda_45D6():
        OP_93(0xE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_45D6)

    def lambda_45E3():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45E3)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x101, 1)

    #C0186
    ChrTalk(
        0xE,
        (
            "#11P仕事が終わったら\x01",
            "またレベッカ君に声を掛けてくれー。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xE,
        (
            "#11P私もケイトも\x01",
            "あちこち飛び回っとるんでなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        (
            "#6P#0100F分かりました、報告は\x01",
            "受付のレベッカさんにですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x104,
        (
            "#12P#0300Fそんじゃ\x01",
            "街の出口に行くとするかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        "#12P#0200Fええ、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【違法駐車の取り締まり】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_4C(0xE, 0xFF)
    OP_4C(0x17, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    OP_49()
    OP_68(-65099, 1500, 14250, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x0, -65099, 0, 14250, 180)
    SetChrPos(0x1, -65099, 0, 14250, 180)
    SetChrPos(0x2, -65099, 0, 14250, 180)
    SetChrPos(0x3, -65099, 0, 14250, 180)
    OP_29(0x17, 0x1, 0x0)
    SetScenarioFlags(0x0, 1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_23_35C3 end

    def Function_24_481D(): pass

    label("Function_24_481D")


    #C0192
    ChrTalk(
        0x8,
        (
            "皆さん、違法駐車の\x01",
            "取り締まりはどうでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        (
            "報告なさるのなら広域防犯課の方々を\x01",
            "お呼びしますけれど。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【報告する】\x01",        # 0
            "【まだしない】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_497A")

    #C0194
    ChrTalk(
        0x101,
        (
            "#0000Fはい、それでは\x01",
            "お願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "分かりました。\x01",
            "申し訳ないのですけど\x01",
            "また少々お待ちくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        (
            "#0100Fええ、あまり\x01",
            "お気になさらないで下さい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49DA")

    label("loc_497A")


    #C0197
    ChrTalk(
        0x8,
        (
            "お仕事が終わったら\x01",
            "私の方にお知らせくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "広域防犯課の方々を\x01",
            "お呼びしますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49DA")

    Return()

    # Function_24_481D end

    def Function_25_49DB(): pass

    label("Function_25_49DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xE, 0xFF)
    OP_4B(0x17, 0xFF)
    OP_68(-57380, 1600, 17520, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    OP_68(-57380, 900, 17520, 3000)
    SetChrPos(0x101, -57500, 0, 17000, 0)
    SetChrPos(0x102, -56750, 0, 16500, 0)
    SetChrPos(0x103, -58250, 0, 15500, 0)
    SetChrPos(0x104, -57500, 0, 15000, 0)
    SetChrPos(0xE, -57500, 0, 19000, 180)
    SetChrPos(0x17, -58500, 0, 19250, 180)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0199
    ChrTalk(
        0x101,
        (
            "#12P#0003F……報告は以上となります。\x02\x03",

            "#0000F違法駐車の車両ナンバーは\x01",
            "こちらとなりますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(1000)
    OP_98(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)

    #C0200
    ChrTalk(
        0xE,
        "#5Pふむふむ……\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xE,
        (
            "#5Pおー、良かった。\x01",
            "調べてくれたみたいだなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x12)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D07")
    OP_2C(0x17, 0x2)
    OP_29(0x17, 0x1, 0x16)

    #C0202
    ChrTalk(
        0x102,
        (
            "#12P#0100Fええ、きちんと調べたので\x01",
            "間違いないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x103,
        (
            "#6P#0200F持ち主は帝国人や\x01",
            "共和国人も多いようですし、\x01",
            "やや神経を使いましたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xE,
        "#5Pそこまでやってくれたのか……\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xE,
        (
            "#5Pいやー、適当にパパーと\x01",
            "やってくれて構わんかったのに。\x01",
            "ウチはいつもそんなモンだぞー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E06")

    label("loc_4D07")

    OP_29(0x17, 0x1, 0x15)

    #C0206
    ChrTalk(
        0xE,
        (
            "#5Pちなみに……間違いなんかが\x01",
            "あったりはせんよな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0207
    ChrTalk(
        0x101,
        (
            "#12P#0005Fえ……えっと。\x02\x03",

            "#0006F（慌ててやったから\x01",
            "  不安になってきたな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xE,
        "#5Pふむ……まあいいか。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xE,
        (
            "#5Pこんなモンはいつも\x01",
            "パパーと適当にやっとるからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E06")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0x17, 0xE, 500)
    Sleep(500)

    #C0210
    ChrTalk(
        0x17,
        (
            "#5P課長～、私たちは\x01",
            "真面目にやってますよ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x17, 500)

    #C0211
    ChrTalk(
        0xE,
        "#11Pおー、スマンスマンー。\x02",
    )

    CloseMessageWindow()

    def lambda_4EE4():
        OP_93(0xE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4EE4)

    def lambda_4EF1():
        OP_93(0x17, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4EF1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x17, 1)

    #C0212
    ChrTalk(
        0x17,
        (
            "#5Pでも……これでなんとか\x01",
            "一仕事片付いたみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x17,
        (
            "#5Pみんなありがとう。\x01",
            "少し余裕が出来たかも！\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xE,
        (
            "#5Pおお、礼を言っとくぞー。\x01",
            "困ったときの支援課だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x104,
        (
            "#12P#0300Fハハ、本部でも\x01",
            "すっかり便利屋扱いッスね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_54B5")
    OP_2C(0x17, 0x2)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x102, 0x101, 500)
    Sleep(500)

    #C0216
    ChrTalk(
        0x102,
        (
            "#12P#0105Fそういえば……\x01",
            "ロイド、言わなくていいの？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0x102, 500)
    Sleep(500)

    #C0217
    ChrTalk(
        0x101,
        "#6P#0005Fあ、そういえば……\x02",
    )

    CloseMessageWindow()

    def lambda_5089():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5089)

    def lambda_5096():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5096)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0218
    ChrTalk(
        0x101,
        "#12P#0001Fあの、実は……\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xE,
        "#5Pうん？　なんだー。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#12P#0001F認可を受けている車両の\x01",
            "ナンバーについてなんですが……\x02\x03",

            "西口と東口に\x01",
            "同じナンバーの車両が\x01",
            "あったようなんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0221
    ChrTalk(
        0x101,
        (
            "#12P#0001F車両ナンバーは……ええと\x01",
            "『ＣＬ　１１０１』\x01",
            "ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0222
    ChrTalk(
        0x17,
        (
            "#5Pそ、そんなことが……\x01",
            "もしかしてナンバー偽造！？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x17)

    #C0223
    ChrTalk(
        0xE,
        (
            "#5Pあー……\x01",
            "……多分アレだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x17, 0xE, 500)
    Sleep(500)

    #C0224
    ChrTalk(
        0xE,
        (
            "#5P駐車認可には\x01",
            "一応料金を徴収しとるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xE,
        (
            "#5Pこれが日当でなぁ。\x01",
            "記念祭中ずっと止めとると\x01",
            "そこそこミラが掛かるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xE,
        (
            "#5P大方申請料をケチった誰かが\x01",
            "１申請で２台止めとるんだろう。\x02",
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
    OP_63(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0227
    ChrTalk(
        0x104,
        (
            "#12P#0306Fけ、けち臭い奴だな……\x01",
            "まあやばい犯罪って\x01",
            "訳じゃ無さそうだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x103,
        "#6P#0200Fですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x17, 500)

    #C0229
    ChrTalk(
        0xE,
        (
            "#5Pふむ、ケイト。\x01",
            "後で調べておいてくれるかー。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x17,
        (
            "#5Pあ、はい！\x01",
            "ケイト了解です！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54B5")


    #C0231
    ChrTalk(
        0x101,
        (
            "#12P#0001Fそれでは……\x01",
            "特務支援課、\x01",
            "これにて失礼致します。\x02\x03",

            "#0000Fまた何かあれば\x01",
            "遠慮なくお呼びください。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5529():
        OP_93(0xE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5529)

    def lambda_5536():
        OP_93(0x17, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5536)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x17, 1)

    #C0232
    ChrTalk(
        0xE,
        "#5Pおー、その時はよろしくなぁ。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x17,
        (
            "#5P記念祭はお互い忙しいけど……\x01",
            "この調子で頑張りましょ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0234
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【違法駐車の取り締まり】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, -25580, 0, 11350, 180)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    OP_29(0x17, 0x4, 0x10)
    SetScenarioFlags(0x0, 2)
    EventEnd(0x5)
    Return()

    # Function_25_49DB end

    def Function_26_5636(): pass

    label("Function_26_5636")

    EventBegin(0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-59660, 1500, 14140, 0)
    MoveCamera(38, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25010, 0)
    SetChrPos(0xB, -57730, 0, 16309, 225)
    SetChrPos(0xC, -57730, 0, 14480, 270)
    SetChrPos(0x101, -60000, 30, 14500, 45)
    SetChrPos(0x102, -60000, 0, 13000, 45)
    SetChrPos(0x103, -61500, 0, 14500, 45)
    SetChrPos(0x104, -61500, 0, 13000, 45)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0235
    ChrTalk(
        0x101,
        (
            "#6P#0000Fドノバン警部、お疲れ様です。\x02\x03",

            "特務支援課以下４名、\x01",
            "警部からの要請を受けて\x01",
            "伺いました。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xB,
        (
            "#5Pうむ、ご苦労さん。\x01",
            "よく来てくれたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xC,
        "#11Pお疲れ～。\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        (
            "#12P#0105Fそれで……\x01",
            "具体的にどういった内容の\x01",
            "依頼だったんでしょう？\x02\x03",

            "#0101F文面を見る限りでは\x01",
            "緊急度が高そうな\x01",
            "案件と見受けましたけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xB,
        (
            "#5Pああ、今から\x01",
            "簡単なミーティングをしよう。\x01",
            "各自席についてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x103,
        "#6P#0200F了解です。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x104,
        (
            "#6P#0309Fへぇ、なんだか警察の仕事っぽい\x01",
            "感じがしてきたじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-60460, 1900, 19460, 0)
    MoveCamera(48, 13, 0, 0)
    OP_6E(-3450, 0)
    SetCameraDistance(36130, 0)
    OP_68(-60460, 900, 19460, 3000)
    SetChrPos(0xB, -58000, 0, 18000, 270)
    SetChrPos(0xC, -57360, 0, 19780, 270)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -60550, 150, 15950, 0)
    SetChrPos(0x102, -60550, 150, 20000, 180)
    SetChrPos(0x103, -64050, 150, 20000, 180)
    SetChrPos(0x104, -64050, 150, 15950, 0)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0242
    ChrTalk(
        0xB,
        (
            "#11Pさて……今日、お前たちを\x01",
            "呼び出したのは他でもない。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xB,
        (
            "#11P本日、このクロスベルにやってくる\x01",
            "『偽ブランド業者』の摘発を\x01",
            "手伝ってもらうためだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        "#12P#0005F偽ブランド業者……ですか？\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x103,
        (
            "#6P#0203F有名ブランドの服飾品や導力器……\x02\x03",

            "それらに使用される\x01",
            "ロゴなどに酷似したものをつけて\x01",
            "顧客に売りつける悪徳商人のことですね。\x02\x03",

            "#0200F自治州法では軽犯罪に該当します。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xC,
        (
            "#11Pく、詳しいねぇ。\x01",
            "大体そんなところだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xC,
        (
            "#11P例年、記念祭の観光客を装って\x01",
            "多くの偽ブランド業者が\x01",
            "クロスベル入りしているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        (
            "#11Pヴェルヌ社の高級腕時計に、\x01",
            "ストレガー社のヴィンテージ物。\x01",
            "そして、七耀石細工……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xC,
        (
            "#11Pそういったものを\x01",
            "知識のない客に売りつけて、\x01",
            "不当に利益を得ているんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        (
            "#6P#0301F人様を騙して儲けようなんざ、\x01",
            "気にくわねぇヤツもいたもんだな。\x02\x03",

            "#0303F要するに、そいつらをフン捕まえるのを\x01",
            "手伝ってほしいってわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xB,
        "#11Pうむ、その通りだ。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xB,
        (
            "#11P不甲斐ねぇが……毎年、何件もの\x01",
            "被害が警察に届け出られている。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xB,
        (
            "#11Pそれに、偽ブランドの存在は\x01",
            "メーカーや流通業者の信用にも\x01",
            "繋がる大きな問題だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xB,
        (
            "#11P警察としては、今年こそ\x01",
            "奴らのクロスベル入りを食い止め、\x01",
            "市民の信頼を回復したいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#6P#0003Fなるほど……\x01",
            "事情は概ね理解しました。\x02\x03",

            "#0001F俺たち特務支援課も、\x01",
            "出来る限り協力させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xB,
        "#11Pうむ、恩に着る。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x102,
        (
            "#6P#0105Fそれで……\x01",
            "私たちは何をすればいいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xB,
        (
            "#11Pヤツらが入ってくるルートは、\x01",
            "クロスベル市の駅と空港、\x01",
            "そしてタングラム門の３つが考えられる。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xB,
        (
            "#11P駅と空港はこちらで抑えるから、\x01",
            "お前たちにはタングラム門での\x01",
            "警戒に当たってもらいたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xC,
        (
            "#11P二課も人手不足でね……\x01",
            "クロスベル市の郊外までには\x01",
            "手が回らないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xC,
        (
            "#11Pその点、君らは確か、\x01",
            "警備隊副司令のソーニャさんと\x01",
            "面識があったよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        (
            "#11P水際対策となると\x01",
            "現地での連携も必要だから、\x01",
            "君たちが適任だと思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x102,
        (
            "#6P#0103Fなるほど……確かに、\x01",
            "他の警察官より私たちの方が\x01",
            "連携がとりやすそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x104,
        (
            "#6P#0306Fやれやれ、出来るなら会わずに\x01",
            "済ませたいんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xB,
        "#11P……よし、話はまとまったな。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xB,
        (
            "#11P俺たちは今から、\x01",
            "駅・空港方面を張ってみるつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xB,
        (
            "#11Pお前たちもタングラム門に合流し、\x01",
            "警備に当たってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x101,
        (
            "#6P#0001F分かりました……\x01",
            "早速、タングラム門のほうに\x01",
            "向かいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xB,
        "#11Pよろしく頼んだぞ。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xC,
        "#11Pじゃあ、またね。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 27)
    BeginChrThread(0xC, 3, 0, 28)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    Fade(1000)
    OP_68(-61410, 900, 18100, 0)
    MoveCamera(61, 17, 0, 0)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x103, 0x1)
    SetChrSubChip(0x104, 0x2)
    OP_0D()

    #C0271
    ChrTalk(
        0x101,
        (
            "#11P#0000Fよし、それじゃあ……\x01",
            "タングラム門に向かうとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x103,
        (
            "#6P#0200Fソーニャ副司令に事情を話して\x01",
            "協力していただかないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0273
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【偽ブランド業者の摘発】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-61760, 1530, 15420, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x0, -61760, 30, 15420, 180)
    SetChrPos(0x1, -61760, 30, 15420, 180)
    SetChrPos(0x2, -61760, 30, 15420, 180)
    SetChrPos(0x3, -61760, 30, 15420, 180)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
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
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_29(0x1B, 0x1, 0x1)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_26_5636 end

    def Function_27_6477(): pass

    label("Function_27_6477")

    OP_68(-64370, 900, 15160, 6000)
    MoveCamera(59, 17, 0, 6000)

    def lambda_6498():
        OP_95(0xFE, -58000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6498)
    WaitChrThread(0xB, 1)

    def lambda_64B6():
        OP_95(0xFE, -65200, 0, 13100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_64B6)
    WaitChrThread(0xB, 1)
    Sound(103, 0, 100, 0)

    def lambda_64DA():
        OP_95(0xFE, -65200, 0, 8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_64DA)

    def lambda_64F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_64F4)
    WaitChrThread(0xB, 1)
    Sound(104, 0, 100, 0)
    Return()

    # Function_27_6477 end

    def Function_28_650B(): pass

    label("Function_28_650B")

    Sleep(500)

    def lambda_6513():
        OP_95(0xFE, -57360, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6513)
    WaitChrThread(0xC, 1)

    def lambda_6531():
        OP_95(0xFE, -65200, 0, 13100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6531)
    WaitChrThread(0xC, 1)

    def lambda_654F():
        OP_95(0xFE, -65200, 0, 9300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_654F)

    def lambda_6569():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_6569)
    WaitChrThread(0xC, 1)
    Return()

    # Function_28_650B end

    def Function_29_657A(): pass

    label("Function_29_657A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x1, 0x10)
    LoadChrToIndex("chr/ch07300.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03400.itp")
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    OP_68(-123940, 2500, 16390, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22600, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, -35500, 0, 16000, 0)
    SetChrPos(0x102, -34000, 0, 16000, 0)
    SetChrPos(0x103, -35500, 0, 14500, 0)
    SetChrPos(0x104, -34000, 0, 14500, 0)
    SetChrPos(0x14, -34750, 0, 13000, 0)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -34750, 0, 17500, 180)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x15, 0x80)
    Sleep(500)
    OP_68(-123940, 1500, 16390, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x1)

    #C0274
    ChrTalk(
        0x16,
        (
            "#6Pえ～と……\x01",
            "それじゃ、お名前をいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x15,
        (
            "#11P……フン、アンタみたいな\x01",
            "ヒョロガキに名乗る名前はないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x16,
        "#6Pヒョ、ヒョロガキって……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x16,
        (
            "#6Pあのですね～……\x01",
            "お婆さん、自分が何やったか\x01",
            "分かってないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x16,
        (
            "#6Pあなたのお仲間も、\x01",
            "すでに拘束されてるんですよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x16,
        "#6Pいい加減、諦めてくださいよ～。\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0280
    ChrTalk(
        0x15,
        (
            "#11P#5Sピーピーピーピーうるさいね！\x01",
            "それになんだい、気の利かない……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0281
    ChrTalk(
        0x15,
        (
            "#11P#5Sレデェと話そうってんだ、\x01",
            "茶の一杯でも出すのが礼儀でしょうが！\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x16,
        (
            "#6Pう、うう～……\x01",
            "後で持ってきますよ……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-35320, 1500, 15470, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23600, 0)
    SetCameraDistance(22600, 2000)
    FadeToBright(500, 0)
    OP_0D()

    #C0283
    ChrTalk(
        0x101,
        (
            "#6P#0006Fあの……\x01",
            "レイモンドさん、\x01",
            "一人で大丈夫なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xB,
        (
            "#5P手強い相手だが……\x01",
            "ま、心配はいらんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xB,
        (
            "#5Pここは警察本部だ。\x01",
            "これ以上逃げようもないさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        (
            "#11P#0106Fうーん……あのお婆さんだと\x01",
            "力ずくで逃げてしまいそうだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x103,
        "#12P#0203F……同感です。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xB,
        (
            "#5Pところで……\x01",
            "そちらの美人は何モンだ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6A55():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A55)
    Sleep(150)

    def lambda_6A65():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A65)
    Sleep(70)

    def lambda_6A75():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A75)
    Sleep(150)

    def lambda_6A85():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6A85)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0289
    ChrTalk(
        0x104,
        (
            "#11P#0305Fおお、そういやあ\x01",
            "聞いてなかったぜ！\x02\x03",

            "#0300Fお姉さん、お名前とご職業は？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("黒髪の女性")

    #A0290
    AnonymousTalk(
        0xFF,
        (
            "#12P……キリカ・ロウラン。\x02\x03",

            "共和国で芸能プロデューサーを\x01",
            "やっているわ。\x02\x03",

            "ここに来たのは……\x01",
            "まぁ、たまたまといった所ね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0291
    ChrTalk(
        0x104,
        (
            "#11P#0304Fキリカさん……いい名前だ！\x02\x03",

            "#0309Fそれに芸能プロデューサーなんて\x01",
            "華やかな仕事……いいッスね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        (
            "#6P#0000Fドノバン警部、\x01",
            "彼女には被疑者の拘束に\x01",
            "協力していただいたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xB,
        "#5Pふむ……なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xB,
        (
            "#5P……不躾な態度で申し訳ない。\x01",
            "ご協力に感謝します。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xB,
        (
            "#5Pよければ、謝礼を出させて頂きますが。\x01",
            "……大した額じゃありませんがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x14,
        (
            "#12P#3404Fいえ、気にしないで下さい。\x02\x03",

            "#3400F手伝ったと言っても、\x01",
            "お礼を言われるほどのことでは\x01",
            "ありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xB,
        (
            "#5Pはは、そう言ってもらえると\x01",
            "気が楽になりますよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6DF0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DF0)
    Sleep(150)

    def lambda_6E00():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E00)
    Sleep(70)

    def lambda_6E10():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E10)
    Sleep(150)

    def lambda_6E20():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6E20)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0298
    ChrTalk(
        0x103,
        "#12P#0211F……警部、鼻の下が伸びてます。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#6P#0000Fところで……\x01",
            "駅や空港の張り込みは\x01",
            "どうだったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xB,
        (
            "#5Pああ……\x01",
            "他のメンバーも一通り拘束できた。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xB,
        (
            "#5P搬送しようとしていた\x01",
            "偽ブランド商品も押収できたしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xB,
        (
            "#5P恐らく、今年はもう\x01",
            "奴らが動く事は不可能だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x102,
        (
            "#11P#0105F今年は、ということは……\x01",
            "彼らの処分はやはり、\x01",
            "軽い物になってしまうんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xB,
        (
            "#5P厳重注意及び\x01",
            "１ヶ月間の自治州退去命令……\x01",
            "そんなところだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        "#6P#0005Fこ、拘置すらもされないんですか……？\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#12P#0306Fなんつーか……\x01",
            "やった甲斐があんまりねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xB,
        (
            "#5P自治州法じゃ、所詮は軽犯罪だからな。\x01",
            "相手は外国人だし、\x01",
            "強く出れねぇ事情もある。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xB,
        (
            "#5Pたしかにやるせねぇが……\x01",
            "こればっかりは仕方ないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x103,
        "#12P#0203F…………………………\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xB,
        (
            "#5Pまぁ、そう気を落とすな。\x01",
            "お前たちはよくやってくれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xB,
        (
            "#5P今年の記念祭に偽ブランド品が\x01",
            "出回らないだけでも上出来ってもんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("レイモンドの声")
    SetMessageWindowPos(-50, 20, -1, -1)

    #A0312
    AnonymousTalk(
        0x16,
        (
            "#2Sけ、警部～……\x01",
            "助けてくださいよ～……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0313
    ChrTalk(
        0xB,
        (
            "#5Pおっと……\x01",
            "レイモンドのヤツを\x01",
            "助けてやらねぇとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xB,
        "#5P特務支援課、今回はご苦労だった。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        "#5Pまた何かあったらよろしく頼むぜ。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#6P#0000Fはい。\x01",
            "いつでもお待ちしてます。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xF)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73F2")

    #C0317
    ChrTalk(
        0xB,
        (
            "#5P……ああ……\x01",
            "そうだ、忘れるところだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xB,
        (
            "#5Pお前らが間違えて\x01",
            "容疑者呼ばわりした観光客だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xB,
        (
            "#5Pさっき、警察からお詫びの品を渡して\x01",
            "謝罪しておいた。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xB,
        (
            "#5P……これから軽率な判断は\x01",
            "慎むようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        (
            "#6P#0006Fす、すみませんでした。\x01",
            "以後気をつけます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73F2")

    OP_93(0xB, 0x0, 0x1F4)

    def lambda_73FE():
        OP_95(0xFE, -34750, 0, 18800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_73FE)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x1)
    Sleep(500)

    def lambda_7437():
        OP_95(0xFE, -34750, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7437)

    def lambda_7451():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_7451)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x1)

    #C0322
    ChrTalk(
        0x14,
        (
            "#12P#3401Fクロスベル自治州……\x01",
            "聞いてはいたけど、\x01",
            "やはり立場が弱い場所なのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()
    OP_68(-35070, 1500, 14300, 1000)

    def lambda_74F9():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_74F9)

    def lambda_7506():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7506)

    def lambda_7513():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7513)

    def lambda_7520():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7520)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0324
    ChrTalk(
        0x14,
        (
            "#12P#3403F法は、人々を守るために\x01",
            "作られるものだけれど……\x02\x03",

            "クロスベルではそれ以上に、\x01",
            "帝国や共和国によって\x01",
            "服従させるためのものになっている。\x02\x03",

            "#3400Fあなた達が\x01",
            "歯がゆい想いをした事も\x01",
            "１度や２度ではないでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        "#5P#0008F……………………\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x14,
        (
            "#12P#3404Fそれでも……\x01",
            "現状に立ち向かっていく\x01",
            "あなた達は敬意に値するわ。\x02\x03",

            "#3402F共和国に住む私が言うのも\x01",
            "なんだけれど……\x01",
            "これからも諦めないことね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0xB4, 0x190)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0327
    ChrTalk(
        0x101,
        "#5P#0011Fあ……\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x104,
        (
            "#11P#0305Fっと、キリカさんは\x01",
            "これからどうするんッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x14,
        (
            "#5P#3404F私は歓楽街のホテルに\x01",
            "部屋を借りているわ。\x02\x03",

            "しばらくそちらに\x01",
            "滞在するつもりよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#5P#0100Fもしよかったら\x01",
            "ご案内させていただきますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x14,
        (
            "#5P#3400Fフフ……お気遣いをどうも。\x01",
            "でも、場所は分かっているから。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        (
            "#5P#0205F歓楽街というと……\x02\x03",

            "#0200Fもしかして、キリカさんが\x01",
            "クロスベルに来たのは……？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0x0, 0x1F4)
    Sleep(300)

    #C0333
    ChrTalk(
        0x14,
        (
            "#12P#3400Fフフ……察しがいいわね。\x02\x03",

            "そう、私はアルカンシェルを\x01",
            "観るためにクロスベルに来たの。\x02\x03",

            "#3404Fあわよくば、共和国での公演を\x01",
            "取り付けられれば、と思ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#5P#0005F共和国での公演……！？\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x14,
        (
            "#12P#3404Fアルカンシェルは、\x01",
            "クロスベルに眠る魔性の宝石……\x02\x03",

            "共和国を熱狂の渦に\x01",
            "巻き込む力を持っているか……\x01",
            "まだ分からないけれど。\x02\x03",

            "#3402Fそれを見極めるのが\x01",
            "クロスベルでの私の仕事。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        (
            "#5P#0000Fあ……\x02\x03",

            "#0003F（タングラム門で言ってた\x01",
            "  “捜しに来た宝石”ってのは\x01",
            "  アルカンシェルのことか……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x14)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xF)"), scpexpr(EXPR_END)), "loc_7B86")

    #C0337
    ChrTalk(
        0x14,
        (
            "#12P#3404Fあなた達……荒削りだけど\x01",
            "真に迫るものがあったわ。\x02\x03",

            "#3402Fふふ、ピタリと真犯人を\x01",
            "言い当てた様は\x01",
            "なかなか堂に入っていた。\x02\x03",

            "お互い、これからも頑張りましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CFC")

    label("loc_7B86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_7C4D")

    #C0338
    ChrTalk(
        0x14,
        (
            "#12P#3404Fあなた達……荒削りだけど\x01",
            "真に迫るものがあったわ。\x02\x03",

            "#3400Fふふ、最後の最後で\x01",
            "私を選んだのは、まだまだ\x01",
            "未熟と言わざるを得ないけど。\x02\x03",

            "お互い、これからも頑張りましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CFC")

    label("loc_7C4D")


    #C0339
    ChrTalk(
        0x14,
        (
            "#12P#3404Fあなた達……荒削りだけど\x01",
            "真に迫るものがあったわ。\x02\x03",

            "#3400Fふふ、今一歩で\x01",
            "真実に及ばなかったのは\x01",
            "未熟と言わざるを得ないけど。\x02\x03",

            "お互い、これからも頑張りましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CFC")


    #C0340
    ChrTalk(
        0x101,
        (
            "#5P#0003Fそ、そうですね。\x02\x03",

            "#0000Fキリカさん、ご協力\x01",
            "ありがとうございました。\x02\x03",

            "そちらも何かありましたら、\x01",
            "支援課まで連絡ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x14,
        (
            "#12P#3402Fフフ……機会があれば。\x02\x03",

            "#3404Fそれでは、失礼するわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0xB4, 0x1F4)

    def lambda_7DD3():
        OP_95(0xFE, -34750, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7DD3)
    WaitChrThread(0x14, 1)

    def lambda_7DF1():
        OP_95(0xFE, -28000, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7DF1)
    WaitChrThread(0x14, 1)

    #C0342
    ChrTalk(
        0x102,
        (
            "#5P#0106Fはぁ……今回の要請も\x01",
            "大変だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        (
            "#11P#0306Fまったくだぜ。\x02\x03",

            "#0309Fま、おかげであんな美人と\x01",
            "知り合えたわけだけどな！\x02\x03",

            "#0304Fいや～、東方美人は\x01",
            "見慣れてたつもりだったけど……\x01",
            "キリカさんは格別だったな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7EEE():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7EEE)

    #C0344
    ChrTalk(
        0x103,
        "#6P#0206F……懲りない人ですね。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        (
            "#5P#0000Fはは……まあいいじゃないか。\x02\x03",

            "そろそろ行くとしよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【偽ブランド業者の摘発】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_29(0x1B, 0x4, 0x10)
    SetChrPos(0xB, -124850, 0, 14920, 45)
    SetChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    SetMapObjFlags(0x1, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_657A end

    def Function_30_8006(): pass

    label("Function_30_8006")

    ClearScenarioFlags(0x1, 4)
    ClearScenarioFlags(0x1, 5)
    ClearScenarioFlags(0x1, 6)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8019")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_823C")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8058")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_8237")

    label("loc_8058")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_808C")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_8237")

    label("loc_808C")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80C0")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_8237")

    label("loc_80C0")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80F4")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_8237")

    label("loc_80F4")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8128")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_8237")

    label("loc_8128")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_815C")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_8237")

    label("loc_815C")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8190")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_8237")

    label("loc_8190")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81C4")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_8237")

    label("loc_81C4")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81FB")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 5)
    Jump("loc_8237")

    label("loc_81FB")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xEE), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8232")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 6)
    Jump("loc_8237")

    label("loc_8232")

    Jump("loc_823C")

    label("loc_8237")

    Jump("loc_8019")

    label("loc_823C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_8EEF")
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-900, 1540, 13420, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19950, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82C6")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0xEF, 300, 40, 13000, 0)
    SetChrPos(0x153, -900, 40, 11800, 0)
    Jump("loc_83EE")

    label("loc_82C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8338")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)
    SetChrPos(0x109, -900, 40, 10600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_83EE")

    label("loc_8338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83AA")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)
    SetChrPos(0x10A, -900, 40, 10600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_83EE")

    label("loc_83AA")

    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)

    label("loc_83EE")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    #C0347
    ChrTalk(
        0x8,
        (
            "あら、皆さん……\x01",
            "戦闘手帳が\x01",
            "大分埋まってきたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x8,
        (
            "魔獣の情報を控えたいので\x01",
            "一度見せてもらっていいでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        "#0000Fええ、喜んで。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0350
    ChrTalk(
        0x8,
        (
            "ありがとうございました。\x01",
            "手帳を返却しますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x8,
        (
            "こちらは今回の手当てとなります。\x01",
            "どうぞ受け取ってください。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85A8")

    #A0352
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0353
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を1個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 1)
    Jump("loc_891F")

    label("loc_85A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_860B")

    #A0354
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１０００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(1000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0355
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 2)
    Jump("loc_891F")

    label("loc_860B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_866E")

    #A0356
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１５００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(1500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0357
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を3個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 3)
    Jump("loc_891F")

    label("loc_866E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86D1")

    #A0358
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２０００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(2000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0359
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を4個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 4)
    Jump("loc_891F")

    label("loc_86D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8734")

    #A0360
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２５００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(2500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0361
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を5個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 5)
    Jump("loc_891F")

    label("loc_8734")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8797")

    #A0362
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３０００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(3000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0363
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を6個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 6)
    Jump("loc_891F")

    label("loc_8797")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87FA")

    #A0364
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３５００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(3500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0365
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を7個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 7)
    Jump("loc_891F")

    label("loc_87FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_885D")

    #A0366
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４０００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(4000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0367
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を8個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 8)
    Jump("loc_891F")

    label("loc_885D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88C0")

    #A0368
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４５００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(4500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0369
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を9個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 9)
    Jump("loc_891F")

    label("loc_88C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_891F")

    #A0370
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５０００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(5000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0371
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を10個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 10)

    label("loc_891F")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_895B")
    Sound(17, 0, 100, 0)

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個、受け取った。\x02",
        )
    )

    AddItemNumber(0x395, 2)
    CloseMessageWindow()
    Jump("loc_898C")

    label("loc_895B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_898C")
    Sound(17, 0, 100, 0)

    #A0373
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x395, 1)
    CloseMessageWindow()

    label("loc_898C")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8AB9")

    #C0374
    ChrTalk(
        0x8,
        (
            "また魔獣の情報が集まったら\x01",
            "立ち寄ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        "#0000Fはい、宜しくお願いします。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A49")

    #C0376
    ChrTalk(
        0x102,
        "#0100Fまたお邪魔させて頂きますね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AB4")

    label("loc_8A49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A7C")

    #C0377
    ChrTalk(
        0x103,
        "#0200Fまたお邪魔します。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AB4")

    label("loc_8A7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AB4")

    #C0378
    ChrTalk(
        0x104,
        "#0300Fまたお邪魔させてもらうッス。\x02",
    )

    CloseMessageWindow()

    label("loc_8AB4")

    Jump("loc_8E6C")

    label("loc_8AB9")


    #C0379
    ChrTalk(
        0x8,
        (
            "たくさんの情報が集まって……\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        (
            "実は他の捜査官の方にも\x01",
            "お願いしているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "こんなに集めてくださったのは\x01",
            "特務支援課の皆さんだけですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BC2")

    #C0382
    ChrTalk(
        0x104,
        (
            "#0300Fハハ……まあ俺たちは\x01",
            "あちこち出かけてるしなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C63")

    label("loc_8BC2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C16")

    #C0383
    ChrTalk(
        0x102,
        (
            "#0100Fあはは……まあ私たちは\x01",
            "あちこち出かけているものね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C63")

    label("loc_8C16")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C63")

    #C0384
    ChrTalk(
        0x103,
        (
            "#0200F……まあ、わたし達は\x01",
            "あちこち出かけていますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C63")


    #C0385
    ChrTalk(
        0x101,
        (
            "#0000F戦闘も頻繁にやっていますし。\x02\x03",

            "……ともかくお役に\x01",
            "立てたみたいで何よりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x8,
        "ふふ……やっぱり頼もしいですね。\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x8,
        (
            "本部に集まった情報も\x01",
            "もう十分だと思いますので、\x01",
            "調査はここまでとさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x8,
        (
            "最後まで付き合っていただいて\x01",
            "ありがとうございました。\x01",
            "今回は特別報酬もお渡ししますね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0389
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１００００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(10000)

    #C0390
    ChrTalk(
        0x8,
        (
            "また何かお願いする事が\x01",
            "あるかもしれません。\x01",
            "その時は宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#0000Fええ、こちらこそ。\x01",
            "宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E6C")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E8A")
    Jump("loc_8EC4")

    label("loc_8E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EA7")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_8EC4")

    label("loc_8EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EC4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_8EC4")

    label("loc_8EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_8ED0")
    ClearScenarioFlags(0x1, 3)

    label("loc_8ED0")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -340, 40, 13280, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Jump("loc_9031")

    label("loc_8EEF")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FA6")

    #C0392
    ChrTalk(
        0x8,
        (
            "本部に集まった情報も\x01",
            "もう十分だと思いますので、\x01",
            "調査はここまでとさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x8,
        (
            "また何かお願いする事が\x01",
            "あるかもしれません。\x01",
            "その時は宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9031")

    label("loc_8FA6")


    #C0394
    ChrTalk(
        0x8,
        (
            "戦闘手帳の内容も\x01",
            "溜まってきているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x8,
        (
            "もう少し情報が集まったら\x01",
            "私の方に見せてください。\x01",
            "情報を控えさせてもらいますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9031")

    Return()

    # Function_30_8006 end

    def Function_31_9032(): pass

    label("Function_31_9032")

    EventBegin(0x1)

    #C0396
    ChrTalk(
        0x101,
        (
            "#0003F……上の階に用事はないな……\x02\x03",

            "#0000F用もないのに上がっていると\x01",
            "副局長に小言を言われかねない。\x01",
            "立ち入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -12810, 0, 14970, 180)
    EventEnd(0x4)
    Return()

    # Function_31_9032 end

    def Function_32_90CC(): pass

    label("Function_32_90CC")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9470")

    #C0397
    ChrTalk(
        0x101,
        (
            "#0005Fそういえば……\x01",
            "前から気になってたんだけど。\x02\x03",

            "#0001Fこれって何だ？\x01",
            "何かの装置みたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x104,
        (
            "#0305Fおお、俺も気になってたぜ。\x02\x03",

            "#0300Fいくつかジュースやらコーヒーやらが\x01",
            "並んでるみたいだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x103,
        (
            "#0202Fこれは『導力式自動販売機』です。\x01",
            "お２人は見るのは初めてですか？\x02\x03",

            "#0204Fミラ硬貨を入れると、\x01",
            "その金額に応じた飲料を\x01",
            "買うことが出来ます。\x02\x03",

            "元々エプスタイン財団で開発されたので\x01",
            "あちらの研究施設には\x01",
            "時々置かれているのですが……\x02\x03",

            "#0202Fクロスベルにも実験的に\x01",
            "設置しているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        "#0000Fへー、そうなんだ……\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x104,
        "#0305Fお嬢は知ってたかよ？\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x102,
        (
            "#0104Fううん、私も見るのは初めてね。\x02\x03",

            "#0100Fそれにしても、色々な場所に\x01",
            "エプスタイン財団の装置が\x01",
            "設置されているのね……\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x103,
        (
            "#0203F何でも、有力なスポンサーが\x01",
            "いると聞いていますが……\x02\x03",

            "#0200F……皆さん、利用するときは\x01",
            "硬貨を使ってください。\x01",
            "紙幣には対応していませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        (
            "#0000Fりょ、了解。\x01",
            "（物珍しいし……\x01",
            "  一度くらい使ってみるか。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96E2")

    label("loc_9470")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0405
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力式の自動販売機がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0406
    ChrTalk(
        0x101,
        (
            "#0005Fこれは……確か、硬貨を入れると\x01",
            "飲料が買えるんだったな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_956E")

    #C0407
    ChrTalk(
        0x103,
        (
            "#0200Fええ、エプスタイン財団が開発した\x01",
            "自動販売機です。\x02\x03",

            "クロスベルにも実験的に\x01",
            "設置している物ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96AB")

    label("loc_956E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9610")

    #C0408
    ChrTalk(
        0x102,
        (
            "#0100Fエプスタイン財団が開発した\x01",
            "自動販売機……だったかしら。\x02\x03",

            "ティオちゃんによれば、\x01",
            "財団が実験的に\x01",
            "クロスベルにも設置しているそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96AB")

    label("loc_9610")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_96AB")

    #C0409
    ChrTalk(
        0x104,
        (
            "#0300Fエプスタイン財団が開発した\x01",
            "自動販売機……だったか。\x02\x03",

            "ティオすけによりゃあ、\x01",
            "財団が実験的に\x01",
            "クロスベルにも設置しているそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96AB")


    #C0410
    ChrTalk(
        0x101,
        (
            "#0000Fさすがクロスベル……\x01",
            "色んな物があるよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96E2")

    SetScenarioFlags(0x95, 3)
    Jump("loc_9701")

    label("loc_96EA")

    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_9701")

    TalkEnd(0xFF)
    Return()

    # Function_32_90CC end

    SaveToFile()

Try(main)
