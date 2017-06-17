from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1370.bin",                # FileName
        "t1370",                    # MapName
        "t1370",                    # Location
        0x00B9,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 185, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1370",                  # 0
        "ランディ",               # 1
        "ノエル",                 # 2
        "ワジ",                   # 3
        "キーア",                 # 4
        "ツァイト",               # 5
        "セシル",                 # 6
        "イリア",                 # 7
        "リーシャ",               # 8
        "シュリ",                 # 9
        "みーしぇ",               # 10
        "メルスン",               # 11
        "コロナ",                 # 12
        "リマ",                   # 13
        "ＭＷＬスタッフ",         # 14
        "観光客",                 # 15
        "観光客",                 # 16
        "観光客",                 # 17
        "観光客",                 # 18
        "観光客",                 # 19
        "観光客",                 # 20
        "観光客",                 # 21
        "職員ハンクス",           # 22
        "ワンダーランド入口広場方面",# 23
    ))

    AddCharChip((
        "chr/ch00302.itc",                   # 00
        "chr/ch02902.itc",                   # 01
        "chr/ch03002.itc",                   # 02
        "chr/ch08200.itc",                   # 03
        "chr/ch02707.itc",                   # 04
        "chr/ch07502.itc",                   # 05
        "chr/ch05102.itc",                   # 06
        "chr/ch05202.itc",                   # 07
        "chr/ch10100.itc",                   # 08
        "chr/ch45400.itc",                   # 09
        "chr/ch26202.itc",                   # 0A
        "chr/ch22702.itc",                   # 0B
        "chr/ch20702.itc",                   # 0C
        "chr/ch44600.itc",                   # 0D
        "chr/ch23500.itc",                   # 0E
        "chr/ch23800.itc",                   # 0F
        "chr/ch23900.itc",                   # 10
        "chr/ch33102.itc",                   # 11
        "chr/ch34302.itc",                   # 12
        "chr/ch21602.itc",                   # 13
        "chr/ch21702.itc",                   # 14
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

    DeclNpc(-2750,   200,     13850,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-2750,   200,     10949,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4250,   200,     12250,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(769,     0,       8899,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(270,     0,       10720,   225,  389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-1250,   200,     12250,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-1250,   200,     12250,   270,  389,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-4250,   200,     12250,   90,   389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-230,    0,       8899,    0,    389,  0x0, 0,   8,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(18000,   0,       -469,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-8600,   200,     2400,    270,  389,  0x0, 0,   10,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-10100,  200,     3900,    180,  389,  0x0, 0,   11,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-11600,  200,     2400,    90,   389,  0x0, 0,   12,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(17700,   0,       4750,    270,  389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(10250,   0,       7349,    180,  389,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(10750,   0,       6250,    270,  389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(9750,    0,       6250,    90,   389,  0x0, 0,   16,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-250,    200,     899,     0,    389,  0x0, 0,   17,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-250,    200,     3900,    180,  389,  0x0, 0,   18,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-17100,  200,     2400,    270,  389,  0x0, 0,   19,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-20100,  200,     2400,    90,   389,  0x0, 0,   20,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(16700,   0,       4750,    1000,    17700,   1500,    4750,    0x007E, 0,  18, 0x0000)
    DeclActor(-22000,  500,     9250,    1200,    -22000,  750,     9250,    0x007C, 0,  3,  0x0000)
    DeclActor(15870,   0,       -630,    1200,    18000,   1500,    -470,    0x007C, 0,  13, 0x0000)
    DeclActor(8450,    0,       9280,    1200,    8450,    2000,    9280,    0x007C, 0,  34, 0x0000)

    PlaceName(10.0, 0.0, -45.0, 0x0000, 0x0000, "ワンダーランド入口広場方面")
    PlaceName(17.68000030517578, 0.0, 4.739999771118164, 0x0000, 0x0053, "")

    ChipFrameInfo(1208, 0)                                       # 0

    ScpFunction((
        "Function_0_4B8",          # 00, 0
        "Function_1_570",          # 01, 1
        "Function_2_5FC",          # 02, 2
        "Function_3_715",          # 03, 3
        "Function_4_7C2",          # 04, 4
        "Function_5_97E",          # 05, 5
        "Function_6_AEF",          # 06, 6
        "Function_7_D42",          # 07, 7
        "Function_8_DF8",          # 08, 8
        "Function_9_F17",          # 09, 9
        "Function_10_1193",        # 0A, 10
        "Function_11_1373",        # 0B, 11
        "Function_12_1440",        # 0C, 12
        "Function_13_1507",        # 0D, 13
        "Function_14_150B",        # 0E, 14
        "Function_15_150F",        # 0F, 15
        "Function_16_159D",        # 10, 16
        "Function_17_1640",        # 11, 17
        "Function_18_16D0",        # 12, 18
        "Function_19_16D4",        # 13, 19
        "Function_20_1860",        # 14, 20
        "Function_21_18DE",        # 15, 21
        "Function_22_1950",        # 16, 22
        "Function_23_19D5",        # 17, 23
        "Function_24_1A98",        # 18, 24
        "Function_25_1B27",        # 19, 25
        "Function_26_1BD2",        # 1A, 26
        "Function_27_1C7A",        # 1B, 27
        "Function_28_1D30",        # 1C, 28
        "Function_29_1FAF",        # 1D, 29
        "Function_30_262C",        # 1E, 30
        "Function_31_276D",        # 1F, 31
        "Function_32_2934",        # 20, 32
        "Function_33_3742",        # 21, 33
        "Function_34_3DFC",        # 22, 34
    ))


    def Function_0_4B8(): pass

    label("Function_0_4B8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4F8"),
        (1, "loc_504"),
        (2, "loc_510"),
        (3, "loc_51C"),
        (4, "loc_528"),
        (5, "loc_534"),
        (6, "loc_540"),
        (SWITCH_DEFAULT, "loc_54C"),
    )


    label("loc_4F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_504")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_510")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_51C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_528")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_534")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_540")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_54C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_558")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_558")

    label("loc_56F")

    Return()

    # Function_0_4B8 end

    def Function_1_570(): pass

    label("Function_1_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_57E")
    Jump("loc_5EC")

    label("loc_57E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_58C")
    Jump("loc_5EC")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_59A")
    Jump("loc_5EC")

    label("loc_59A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_5AB")
    Call(0, 28)
    Jump("loc_5EC")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_5B9")
    Jump("loc_5EC")

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5C7")
    Jump("loc_5EC")

    label("loc_5C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_5D5")
    Jump("loc_5EC")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5E3")
    Jump("loc_5EC")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_5EC")

    label("loc_5EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_5FB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 33)

    label("loc_5FB")

    Return()

    # Function_1_570 end

    def Function_2_5FC(): pass

    label("Function_2_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62F")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x78, 0x0)

    label("loc_62F")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_641")
    Jump("loc_6B0")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_64F")
    Jump("loc_6B0")

    label("loc_64F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_65D")
    Jump("loc_6B0")

    label("loc_65D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_66F")
    OP_66(0x0, 0x1)
    Jump("loc_6B0")

    label("loc_66F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_67D")
    Jump("loc_6B0")

    label("loc_67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_68B")
    Jump("loc_6B0")

    label("loc_68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_699")
    Jump("loc_6B0")

    label("loc_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_6A7")
    Jump("loc_6B0")

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_6B0")

    label("loc_6B0")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D6")
    OP_66(0x2, 0x1)

    label("loc_6D6")

    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_708")
    OP_24(0x335)
    Jump("loc_70E")

    label("loc_708")

    Sound(821, 1, 50, 0)

    label("loc_70E")

    Sound(126, 1, 80, 0)
    Return()

    # Function_2_5FC end

    def Function_3_715(): pass

    label("Function_3_715")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『お菓子の王国　第三巻』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_7BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『七色わたあめ』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7BE")

    TalkEnd(0xFF)
    Return()

    # Function_3_715 end

    def Function_4_7C2(): pass

    label("Function_4_7C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DB")
    Jump("loc_97A")

    label("loc_7DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    Jump("loc_97A")

    label("loc_7F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D7")

    #C0003
    ChrTalk(
        0x8,
        (
            "#00306Fぬう……セシルさんと\x01",
            "楽しくお茶でもしようと\x01",
            "思って来たんだがな。\x02\x03",

            "#00309Fまあ、ここはノエルで\x01",
            "我慢するとするか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x9,
        "#10106Fず、随分な言い様ですね先輩……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_94E")

    label("loc_8D7")


    #C0005
    ChrTalk(
        0x8,
        (
            "#00306Fセシルさんと\x01",
            "楽しくお茶でもしようと\x01",
            "思って来たんだがな。\x02\x03",

            "#00309Fまあ、ノエルに\x01",
            "付き合ってもらうとするか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94E")

    Jump("loc_97A")

    label("loc_953")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_969")
    Jump("loc_97A")

    label("loc_969")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97A")

    label("loc_97A")

    TalkEnd(0xFE)
    Return()

    # Function_4_7C2 end

    def Function_5_97E(): pass

    label("Function_5_97E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_997")
    Jump("loc_AEB")

    label("loc_997")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AD")
    Jump("loc_AEB")

    label("loc_9AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3A")

    #C0006
    ChrTalk(
        0x9,
        (
            "#10100Fセシルさんは遊びに\x01",
            "出ているみたいです。\x02\x03",

            "#10109Fふふ、ランディ先輩も\x01",
            "タイミングが悪いですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_ABF")

    label("loc_A3A")


    #C0007
    ChrTalk(
        0x9,
        (
            "#10105Fところで……\x01",
            "ツァイト君はずっとここで\x01",
            "昼寝してるつもりなんですかね。\x02\x03",

            "#10104Fうーん、売店で何か\x01",
            "買ってあげようかなあ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABF")

    Jump("loc_AEB")

    label("loc_AC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADA")
    Jump("loc_AEB")

    label("loc_ADA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEB")

    label("loc_AEB")

    TalkEnd(0xFE)
    Return()

    # Function_5_97E end

    def Function_6_AEF(): pass

    label("Function_6_AEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B08")
    Jump("loc_D3E")

    label("loc_B08")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1E")
    Jump("loc_D3E")

    label("loc_B1E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B34")
    Jump("loc_D3E")

    label("loc_B34")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4A")
    Jump("loc_D3E")

    label("loc_B4A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB2")

    #C0008
    ChrTalk(
        0x101,
        (
            "#00005Fワジ、なにしてるんだ？\x02\x03",

            "#00003Fまさか、セシル姉に\x01",
            "ちょっかいをかけてるんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xA,
        (
            "#10306Fフフ、やれやれ。\x01",
            "少しは信用して欲しいな。\x02\x03",

            "#10302F僕の行ってるクラブには\x01",
            "彼女くらいの妙齢の女性も来るけど……\x01",
            "今日はオフだし手出しはしないさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0010
    ChrTalk(
        0x101,
        (
            "#00006Fそんなのだから\x01",
            "信用ならないんだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_D3E")

    label("loc_CB2")


    #C0011
    ChrTalk(
        0xA,
        (
            "#10305Fうちの店にはセシルさんくらいの\x01",
            "妙齢の女性が来る事もあるけど……\x02\x03",

            "#10300Fフフ、君の素敵なお姉さんに\x01",
            "手を出したりなんかしないさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3E")

    TalkEnd(0xFE)
    Return()

    # Function_6_AEF end

    def Function_7_D42(): pass

    label("Function_7_D42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5B")
    Jump("loc_DF4")

    label("loc_D5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7E")
    Call(0, 27)
    Jump("loc_DB2")

    label("loc_D7E")


    #C0012
    ChrTalk(
        0xB,
        (
            "#01105Fえー、だってこんなに\x01",
            "かわいいんだよー？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB2")

    Jump("loc_DF4")

    label("loc_DB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCD")
    Jump("loc_DF4")

    label("loc_DCD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE3")
    Jump("loc_DF4")

    label("loc_DE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF4")

    label("loc_DF4")

    TalkEnd(0xFE)
    Return()

    # Function_7_D42 end

    def Function_8_DF8(): pass

    label("Function_8_DF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E32")

    #C0013
    ChrTalk(
        0xC,
        "#01200Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_E32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E55")
    Call(0, 27)
    Jump("loc_E6E")

    label("loc_E55")


    #C0014
    ChrTalk(
        0xC,
        "#01200F……ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_E6E")

    Jump("loc_F13")

    label("loc_E73")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA6")

    #C0015
    ChrTalk(
        0xC,
        "#01200F……グルルル……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_EA6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE1")

    #C0016
    ChrTalk(
        0xC,
        "#01200F……グルルル……ウォン。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_EE1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F13")

    #C0017
    ChrTalk(
        0xC,
        "#01200Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_F13")

    TalkEnd(0xFE)
    Return()

    # Function_8_DF8 end

    def Function_9_F17(): pass

    label("Function_9_F17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1028")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAB")

    #C0018
    ChrTalk(
        0xD,
        (
            "#05900Fなるべく私は\x01",
            "ここに居るようにするわね。\x02\x03",

            "#05909Fふふ、ロイドたちは\x01",
            "気兼ねなく楽しんでらっしゃい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1023")

    label("loc_FAB")


    #C0019
    ChrTalk(
        0xD,
        (
            "#05904Fしばらくはツァイトくんと\x01",
            "のんびりしてようかな。\x02\x03",

            "#05909Fふふ、でも誘ってくれるなら\x01",
            "ご一緒させてもらうわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1023")

    Jump("loc_118F")

    label("loc_1028")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103E")
    Jump("loc_118F")

    label("loc_103E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1054")
    Jump("loc_118F")

    label("loc_1054")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106A")
    Jump("loc_118F")

    label("loc_106A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1112")

    #C0020
    ChrTalk(
        0xD,
        (
            "#05900Fふふ、そろそろ\x01",
            "昼の部も終わりそうだから\x01",
            "ここで皆を待ってるの。\x02\x03",

            "#05904Fロイドも遊び終わったら、\x01",
            "一度ここに戻ってきてね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_118F")

    label("loc_1112")


    #C0021
    ChrTalk(
        0xD,
        (
            "#05900Fロイドも遊び終わったら、\x01",
            "一度ここに戻ってきてね。\x02\x03",

            "#05909Fふふ、もちろん\x01",
            "誘ってくれるなら\x01",
            "ご一緒させてもらうわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118F")

    TalkEnd(0xFE)
    Return()

    # Function_9_F17 end

    def Function_10_1193(): pass

    label("Function_10_1193")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AC")
    Jump("loc_136F")

    label("loc_11AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C2")
    Jump("loc_136F")

    label("loc_11C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D8")
    Jump("loc_136F")

    label("loc_11D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E5")

    #C0022
    ChrTalk(
        0xE,
        (
            "#01700Fこの子、ツァイト君だっけ？\x01",
            "普段はおとなしいし、\x01",
            "かなり賢いみたいねー。\x02\x03",

            "#01704F前にクロスベルタイムズでも\x01",
            "紹介されてたみたいだし……\x01",
            "なかなかのスター性を感じるわ。\x02\x03",

            "#01709Fフフ、アルカンシェルに\x01",
            "スカウトしちゃおうかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1359")

    label("loc_12E5")


    #C0023
    ChrTalk(
        0xE,
        (
            "#01704Fツァイト君には\x01",
            "なかなかのスター性を感じるわ。\x02\x03",

            "#01709Fフフ、アルカンシェルに\x01",
            "スカウトしちゃおうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1359")

    Jump("loc_136F")

    label("loc_135E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136F")

    label("loc_136F")

    TalkEnd(0xFE)
    Return()

    # Function_10_1193 end

    def Function_11_1373(): pass

    label("Function_11_1373")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_138C")
    Jump("loc_143C")

    label("loc_138C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A2")
    Jump("loc_143C")

    label("loc_13A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B8")
    Jump("loc_143C")

    label("loc_13B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142B")

    #C0024
    ChrTalk(
        0xF,
        (
            "#01803Fそこの売店のわたあめが\x01",
            "なかなか美味しかったですよ。\x02\x03",

            "#01809Fもう食べてみました？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143C")

    label("loc_142B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143C")

    label("loc_143C")

    TalkEnd(0xFE)
    Return()

    # Function_11_1373 end

    def Function_12_1440(): pass

    label("Function_12_1440")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1459")
    Jump("loc_1503")

    label("loc_1459")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_147C")
    Call(0, 27)
    Jump("loc_14C1")

    label("loc_147C")


    #C0025
    ChrTalk(
        0x10,
        (
            "#14006Fかわいかろうが\x01",
            "かっこよかろうが\x01",
            "ダメなもんはダメだろ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C1")

    Jump("loc_1503")

    label("loc_14C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DC")
    Jump("loc_1503")

    label("loc_14DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F2")
    Jump("loc_1503")

    label("loc_14F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1503")

    label("loc_1503")

    TalkEnd(0xFE)
    Return()

    # Function_12_1440 end

    def Function_13_1507(): pass

    label("Function_13_1507")

    Call(0, 29)
    Return()

    # Function_13_1507 end

    def Function_14_150B(): pass

    label("Function_14_150B")

    Call(0, 30)
    Return()

    # Function_14_150B end

    def Function_15_150F(): pass

    label("Function_15_150F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1546")

    #C0026
    ChrTalk(
        0x12,
        "さあ、次は何に乗ろうか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1599")

    label("loc_1546")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155C")
    Jump("loc_1599")

    label("loc_155C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1572")
    Jump("loc_1599")

    label("loc_1572")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1588")
    Jump("loc_1599")

    label("loc_1588")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1599")

    label("loc_1599")

    TalkEnd(0xFE)
    Return()

    # Function_15_150F end

    def Function_16_159D(): pass

    label("Function_16_159D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E9")

    #C0027
    ChrTalk(
        0x13,
        (
            "ふふ、いいわね。\x01",
            "高い所でのんびりしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_163C")

    label("loc_15E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15FF")
    Jump("loc_163C")

    label("loc_15FF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1615")
    Jump("loc_163C")

    label("loc_1615")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162B")
    Jump("loc_163C")

    label("loc_162B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_163C")

    label("loc_163C")

    TalkEnd(0xFE)
    Return()

    # Function_16_159D end

    def Function_17_1640(): pass

    label("Function_17_1640")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1679")

    #C0028
    ChrTalk(
        0x14,
        "リマ、観覧車に乗りたーい！\x02",
    )

    CloseMessageWindow()
    Jump("loc_16CC")

    label("loc_1679")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_168F")
    Jump("loc_16CC")

    label("loc_168F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A5")
    Jump("loc_16CC")

    label("loc_16A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BB")
    Jump("loc_16CC")

    label("loc_16BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16CC")

    label("loc_16CC")

    TalkEnd(0xFE)
    Return()

    # Function_17_1640 end

    def Function_18_16D0(): pass

    label("Function_18_16D0")

    Call(0, 19)
    Return()

    # Function_18_16D0 end

    def Function_19_16D4(): pass

    label("Function_19_16D4")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話す\x01",              # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_173B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_173B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_175B")
    OP_AF(0x6B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1857")

    label("loc_175B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176F")
    Jump("loc_1857")

    label("loc_176F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1787")
    TalkEnd(0x15)
    Return()

    label("loc_1787")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1857")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F8")

    #C0029
    ChrTalk(
        0x15,
        "いらっしゃいませ～！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x15,
        "おいしいわたあめはいかがですか～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1857")

    label("loc_17F8")


    #C0031
    ChrTalk(
        0x15,
        (
            "そろそろお腹が空いてきた頃じゃ\x01",
            "ありませんか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x15,
        "甘～いわたあめなんていかがですか～？\x02",
    )

    CloseMessageWindow()

    label("loc_1857")

    Jump("loc_16E1")

    label("loc_185C")

    TalkEnd(0x15)
    Return()

    # Function_19_16D4 end

    def Function_20_1860(): pass

    label("Function_20_1860")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B4")

    #C0033
    ChrTalk(
        0x16,
        (
            "ああもう、こんなとこまできて\x01",
            "ケンカなんかやめなさい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18DA")

    label("loc_18B4")


    #C0034
    ChrTalk(
        0x16,
        "ああもう、今回はガマンしなさい！\x02",
    )

    CloseMessageWindow()

    label("loc_18DA")

    TalkEnd(0xFE)
    Return()

    # Function_20_1860 end

    def Function_21_18DE(): pass

    label("Function_21_18DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1926")

    #C0035
    ChrTalk(
        0x17,
        (
            "へへっ、たった一口くらい\x01",
            "いいじゃんか～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_194C")

    label("loc_1926")


    #C0036
    ChrTalk(
        0x17,
        "もう帰るなんて絶対早すぎだよ～！\x02",
    )

    CloseMessageWindow()

    label("loc_194C")

    TalkEnd(0xFE)
    Return()

    # Function_21_18DE end

    def Function_22_1950(): pass

    label("Function_22_1950")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_199E")

    #C0037
    ChrTalk(
        0x18,
        (
            "あーん、お兄ちゃんが\x01",
            "あたしのわたあめ食べた～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D1")

    label("loc_199E")


    #C0038
    ChrTalk(
        0x18,
        (
            "あーん、やだやだ～！\x01",
            "夜のパレードも見るの～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D1")

    TalkEnd(0xFE)
    Return()

    # Function_22_1950 end

    def Function_23_19D5(): pass

    label("Function_23_19D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A54")

    #C0039
    ChrTalk(
        0x19,
        (
            "お待たせ、ハニー。\x01",
            "ジュースを買ってきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x19,
        (
            "このラブラブストローで\x01",
            "一緒に飲もうじゃないか！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A94")

    label("loc_1A54")


    #C0041
    ChrTalk(
        0x19,
        "夕日が綺麗だね、ハニー。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x19,
        "でも君の方がもっと綺麗だよ。\x02",
    )

    CloseMessageWindow()

    label("loc_1A94")

    TalkEnd(0xFE)
    Return()

    # Function_23_19D5 end

    def Function_24_1A98(): pass

    label("Function_24_1A98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AEC")

    #C0043
    ChrTalk(
        0x1A,
        (
            "いや、そういうのいいから\x01",
            "２つ買ってきてちょうだいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B23")

    label("loc_1AEC")


    #C0044
    ChrTalk(
        0x1A,
        (
            "いや、そういうのいいから\x01",
            "そろそろ帰りましょうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B23")

    TalkEnd(0xFE)
    Return()

    # Function_24_1A98 end

    def Function_25_1B27(): pass

    label("Function_25_1B27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BCE")

    #C0045
    ChrTalk(
        0x1B,
        (
            "静かで美しい保養地だったのに、\x01",
            "ミシュラムも変わったもんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x1B,
        (
            "なんでもかんでも若者向けにしおって。\x01",
            "年寄りのことも考えて欲しいわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BCE")

    label("loc_1BCE")

    TalkEnd(0xFE)
    Return()

    # Function_25_1B27 end

    def Function_26_1BD2(): pass

    label("Function_26_1BD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C76")

    #C0047
    ChrTalk(
        0x1C,
        (
            "ふふ、おじいさんは\x01",
            "あんなこと言ってるけど、\x01",
            "内心相当楽しんでるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x1C,
        (
            "今日だって、ホラーコースターに\x01",
            "もう４回も乗ってるんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C76")

    label("loc_1C76")

    TalkEnd(0xFE)
    Return()

    # Function_26_1BD2 end

    def Function_27_1C7A(): pass

    label("Function_27_1C7A")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0049
    ChrTalk(
        0xB,
        (
            "#01109Fよーし、それじゃあ\x01",
            "次のアトラクションは\x01",
            "ツァイトも一緒に乗ろー！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xC,
        "#01200F……ウォン？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x10,
        (
            "#14006Fいやいや……無理だろ、\x01",
            "常識的に考えて。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_27_1C7A end

    def Function_28_1D30(): pass

    label("Function_28_1D30")

    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x19, 0x11)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x1A, 0x12)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x13)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x14)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    SetChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E41")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x10)
    Jump("loc_1FAE")

    label("loc_1E41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6B")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    Jump("loc_1FAE")

    label("loc_1E6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EAD")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_1FAE")

    label("loc_1EAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F59")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 6)), scpexpr(EXPR_END)), "loc_1F09")
    SetChrPos(0x11, 14920, 0, -450, 270)

    label("loc_1F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 2)), scpexpr(EXPR_END)), "loc_1F17")
    SetChrFlags(0x11, 0x80)

    label("loc_1F17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_1F46")
    SetChrFlags(0xE, 0x80)
    Jump("loc_1F54")

    label("loc_1F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_1F54")
    SetChrFlags(0xF, 0x80)

    label("loc_1F54")

    Jump("loc_1FAE")

    label("loc_1F59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FAE")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    TurnDirection(0x17, 0x16, 0)
    TurnDirection(0x18, 0x16, 0)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)

    label("loc_1FAE")

    Return()

    # Function_28_1D30 end

    def Function_29_1FAF(): pass

    label("Function_29_1FAF")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(17030, 400, 460, 0)
    MoveCamera(43, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0x101, 13520, 0, -380, 90)
    OP_65(0x2, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x101,
        (
            "#00005Fあれ、何かピンク色のものが\x01",
            "隠れてるぞ……？\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x11, 0xFF)
    OP_9C(0x11, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    TurnDirection(0x11, 0x101, 500)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "きゃっ、見つかっちゃった☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(15090, 0, 480, 0)
    MoveCamera(43, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0x101, 11950, 0, -590, 90)
    SetChrPos(0x11, 14500, 0, -450, 270)
    Sound(1025, 0, 100, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0054
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "はじめまして、おにーさん㈱\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "あたしは『みーしぇ』だヨっ♪\x01",
            "みししっ、よろしくね～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0056
    ChrTalk(
        0x101,
        (
            "#00000Fああ、もしかして\x01",
            "みっしぃの妹っていう？\x02\x03",

            "#00004Fティオは、運がよければ\x01",
            "会えるって言ってけど……\x01",
            "はは、ラッキーだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "あっ、知ってたんだ～！\x01",
            "みししっ、うれしいナ～☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0058
    ChrTalk(
        0x101,
        (
            "#00005Fそういえば……\x01",
            "なんであんなところに\x01",
            "隠れてたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "みししっ、あたしってば\x01",
            "かくれんぼが大好きなのよね～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "いつもワンダーランドの\x01",
            "どこかに隠れて、白馬の王子様が\x01",
            "見つけてくれるのを待ってるの㈱\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x101,
        (
            "#00006F（運がよくなきゃ\x01",
            "  会えないわけだな……）\x02\x03",

            "#00012Fはは、ってことは今回は\x01",
            "俺が白馬の王子様ってことかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "みししっ、そうだヨ～。\x01",
            "見つけてくれて\x01",
            "とっても嬉しいんだから！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "しょんぼり顔のお兄ちゃんの\x01",
            "百倍はイケメンだし、\x01",
            "王子様の資格もばっちりヨ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#00006F（み、みっしぃが微妙に\x01",
            "  ひどい言われ様だな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "と、いうわけで……\x01",
            "おにーさん、あたしと一緒に\x01",
            "かくれんぼして遊ばない？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0066
    ChrTalk(
        0x101,
        "#00005Fえっ……？\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "あたしを見つけてくれた\x01",
            "王子様だけが参加できる、\x01",
            "スペシャルなゲームなんだヨ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "おにーさんがお友達と一緒に、\x01",
            "ワンダーランド内に隠れてる\x01",
            "あたしを５回見つけ出すの！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "豪華な景品もあるんだヨ☆\x01",
            "どう、やってみない？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Return()

    # Function_29_1FAF end

    def Function_30_262C(): pass

    label("Function_30_262C")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x11, 0xFF)
    OP_68(15090, 0, 480, 0)
    MoveCamera(43, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0x101, 11950, 0, -590, 90)
    SetChrPos(0x11, 14500, 0, -450, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0070
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "あっ、おにーさん！\x01",
            "やっぱりあたしとかくれんぼする～？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "おにーさんがお友達と一緒に、\x01",
            "ワンダーランド内に隠れてる\x01",
            "あたしを５回見つけ出すの！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "豪華な景品もあるんだヨ☆\x01",
            "どう、やってみない？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 31)
    Return()

    # Function_30_262C end

    def Function_31_276D(): pass

    label("Function_31_276D")


    #C0073
    ChrTalk(
        0x101,
        (
            "#00003F（一度始めると、\x01",
            "  終わるまでは他のアトラクションで\x01",
            "  遊んでる暇はなさそうだな……）\x02",
        )
    )

    CloseMessageWindow()
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
            "【受けて立つ】\x01",      # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283D")
    Call(0, 32)
    Jump("loc_28FC")

    label("loc_283D")


    #C0074
    ChrTalk(
        0x101,
        (
            "#00000Fえっと、ごめん。\x01",
            "今はアトラクションを\x01",
            "回ってる最中でさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "えーっ、そうなの～？\x01",
            "しょんぼり……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "でも、やりたくなったら\x01",
            "いつでも言ってね！\x01",
            "あたし、待ってるから。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C7, 6)

    label("loc_28FC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x11, 14920, 0, -450, 270)
    OP_4C(0x11, 0xFF)
    SetChrPos(0x0, 12800, 0, -380, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_31_276D end

    def Function_32_2934(): pass

    label("Function_32_2934")


    #C0077
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ……\x01",
            "やってみようかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0078
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "みししっ、そうこなくっちゃ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "それじゃ、さっそく隠れるから\x01",
            "おにーさんはパートナーを\x01",
            "探しといてネ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "ギブアップするときは\x01",
            "広場にいるみっしぃお兄ちゃんに\x01",
            "言ってくれればいいから。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "みししっ、それじゃネ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(12510, 0, 1310, 3000)

    def lambda_2A79():

        label("loc_2A79")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_2A79")

    QueueWorkItem2(0x101, 1, lambda_2A79)
    SetChrFlags(0x11, 0x1000)
    OP_95(0x11, 13790, 0, 1620, 5000, 0x0)
    OP_95(0x11, 2640, 0, 1210, 5000, 0x0)
    EndChrThread(0x101, 0x1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0082
    ChrTalk(
        0x101,
        (
            "#00003Fと、とにかく……\x01",
            "一緒にみーしぇを探す\x01",
            "パートナーが必要みたいだ。\x02\x03",

            "#00000F誰を誘おうかな……？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【エリィ】\x01",        # 0
            "【ティオ】\x01",        # 1
            "【ランディ】\x01",      # 2
            "【ノエル】\x01",        # 3
            "【ワジ】\x01",          # 4
            "【キーア】\x01",        # 5
            "【フラン】\x01",        # 6
            "【セシル】\x01",        # 7
            "【イリア】\x01",        # 8
            "【リーシャ】\x01",      # 9
            "【シュリ】\x01",        # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C3D"),
        (1, "loc_2C83"),
        (2, "loc_2CC9"),
        (3, "loc_2D11"),
        (4, "loc_2D57"),
        (5, "loc_2D9B"),
        (6, "loc_2DE1"),
        (7, "loc_2E27"),
        (8, "loc_2E6F"),
        (9, "loc_2EB9"),
        (10, "loc_2F01"),
        (SWITCH_DEFAULT, "loc_2F47"),
    )


    label("loc_2C3D")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C7, 7)

    #C0083
    ChrTalk(
        0x101,
        "#00000F（よし……エリィを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x0)
    Jump("loc_2F47")

    label("loc_2C83")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 0)

    #C0084
    ChrTalk(
        0x101,
        "#00000F（よし……ティオを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x1)
    Jump("loc_2F47")

    label("loc_2CC9")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 1)

    #C0085
    ChrTalk(
        0x101,
        "#00000F（よし……ランディを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x2)
    Jump("loc_2F47")

    label("loc_2D11")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 2)

    #C0086
    ChrTalk(
        0x101,
        "#00000F（よし……ノエルを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x3)
    Jump("loc_2F47")

    label("loc_2D57")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 3)

    #C0087
    ChrTalk(
        0x101,
        "#00000F（よし……ワジを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x4)
    Jump("loc_2F47")

    label("loc_2D9B")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 4)

    #C0088
    ChrTalk(
        0x101,
        "#00000F（よし……キーアを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x5)
    Jump("loc_2F47")

    label("loc_2DE1")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 5)

    #C0089
    ChrTalk(
        0x101,
        "#00000F（よし……フランを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x6)
    Jump("loc_2F47")

    label("loc_2E27")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 6)

    #C0090
    ChrTalk(
        0x101,
        "#00000F（よし……セシル姉を誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x7)
    Jump("loc_2F47")

    label("loc_2E6F")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C8, 7)

    #C0091
    ChrTalk(
        0x101,
        "#00000F（よし……イリアさんを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x8)
    Jump("loc_2F47")

    label("loc_2EB9")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C9, 0)

    #C0092
    ChrTalk(
        0x101,
        "#00000F（よし……リーシャを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0x9)
    Jump("loc_2F47")

    label("loc_2F01")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C9, 1)

    #C0093
    ChrTalk(
        0x101,
        "#00000F（よし……シュリを誘ってみよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x7F, 0x1, 0xA)
    Jump("loc_2F47")

    label("loc_2F47")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_2F64")
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_2F76")
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_2F88")
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_2F9A")
    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_2FAC")
    AddParty(0x4, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_2FBE")
    AddParty(0x52, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_2FD0")
    AddParty(0x55, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_2FE2")
    AddParty(0x4B, 0xEF, 0xFF)
    Jump("loc_3014")

    label("loc_2FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_2FF9")
    AddParty(0x33, 0xEF, 0xFF)
    SetChrFlags(0xE, 0x80)
    Jump("loc_3014")

    label("loc_2FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_3010")
    AddParty(0x34, 0xEF, 0xFF)
    SetChrFlags(0xF, 0x80)
    Jump("loc_3014")

    label("loc_3010")

    AddParty(0x65, 0xEF, 0xFF)

    label("loc_3014")

    OP_68(14480, 0, 520, 0)
    MoveCamera(44, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19900, 0)
    SetChrPos(0xEF, 13000, 0, 200, 180)
    SetChrPos(0x101, 13000, 0, -1690, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_30DF")

    #C0094
    ChrTalk(
        0x102,
        (
            "#00100Fうん、事情は分かったわ。\x02\x03",

            "#00109Fふふ、結構楽しそうだし、\x01",
            "頑張って探してみましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_30DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_3168")

    #C0095
    ChrTalk(
        0x103,
        (
            "#00200Fなるほど……\x01",
            "事情は分かりました。\x02\x03",

            "#00204Fあのみーしぇとかくれんぼ……\x01",
            "気合を入れて臨まなくては\x01",
            "いけませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_3168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_31DD")

    #C0096
    ChrTalk(
        0x104,
        (
            "#00300Fなるほど、事情は分かったぜ。\x02\x03",

            "#00304Fま、アトラクションのつなぎに\x01",
            "ちょっくら遊んでみるか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_31DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_324E")

    #C0097
    ChrTalk(
        0x109,
        (
            "#10105Fはあ、そんなことが……\x02\x03",

            "#10109Fでも、面白そうですね。\x01",
            "やるからには本気で探しましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_324E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_32D6")

    #C0098
    ChrTalk(
        0x105,
        (
            "#10300Fふむ、なるほど。\x01",
            "なかなか楽しそうなことになったね。\x02\x03",

            "#10309Fフフ、せっかくだから\x01",
            "気合を入れて探してみようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_32D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_333A")

    #C0099
    ChrTalk(
        0x153,
        (
            "#01100Fかくれんぼなんて、たのしそー！！\x02\x03",

            "#01109Fロイド、がんばってさがそーね！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_333A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_33BA")

    #C0100
    ChrTalk(
        0x156,
        (
            "#06405Fへえ、あのみーしぇと\x01",
            "かくれんぼですか～。\x02\x03",

            "#06409Fふふっ、ロイドさん！\x01",
            "こうなったらがんばりましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_33BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_3433")

    #C0101
    ChrTalk(
        0x14C,
        (
            "#05905Fまあ、そんな事があったのね。\x02\x03",

            "#05909Fふふ、それじゃあその\x01",
            "みーしぇって子を探してみましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_3433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_34DA")

    #C0102
    ChrTalk(
        0x134,
        (
            "#01700Fふんふん、事情は分かったわ。\x01",
            "なんだか面白そうじゃない。\x02\x03",

            "#01709Fたかがかくれんぼだけど、\x01",
            "本気でいく必要がありそうね！\x01",
            "がんばりましょ、弟君！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_34DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_355D")

    #C0103
    ChrTalk(
        0x135,
        (
            "#01802Fなるほど……事情は分かりました。\x02\x03",

            "#01809Fふふ、私もかくれんぼは得意ですし、\x01",
            "ご一緒させていただきますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EB")

    label("loc_355D")


    #C0104
    ChrTalk(
        0x166,
        (
            "#14000Fふーん、かくれんぼねえ。\x01",
            "なんかヘンな話になってるなあ。\x02\x03",

            "#14004Fま、ヒマだし付き合ってやるよ。\x01",
            "……ほら、さっさと探しに行こうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_3662")

    #C0105
    ChrTalk(
        0x101,
        (
            "#00009Fはは、よろしくお願いします。\x02\x03",

            "#00000Fそれじゃあさっそく\x01",
            "テーマパークの中を探してみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C1")

    label("loc_3662")


    #C0106
    ChrTalk(
        0x101,
        (
            "#00009Fはは、よろしく頼むよ。\x02\x03",

            "#00000Fそれじゃあさっそく\x01",
            "テーマパークの中を探してみるか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0107
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【みーしぇの挑戦】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1C9, 2)
    OP_29(0x7F, 0x4, 0x2)
    SetChrFlags(0x11, 0x80)
    OP_65(0x2, 0x1)
    SetChrPos(0x0, 12800, 0, -380, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_32_2934 end

    def Function_33_3742(): pass

    label("Function_33_3742")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch28100.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrFlags(0x1D, 0x8000)
    OP_68(12380, 0, 8690, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18770, 0)
    SetChrPos(0x101, 10510, 0, 7810, 90)
    SetChrPos(0x103, 11970, 0, 7490, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    #C0108
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200Fふう、なんとかやりきったな……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F……お疲れさまです。\x02\x03",

            "#05526F着ぐるみのままダンスは\x01",
            "なかなか大変でしたね……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206Fそうだな……\x01",
            "めちゃくちゃ暑いし。\x02\x03",

            "#05209Fこれを毎日やるんだから\x01",
            "本物の役者さんは\x01",
            "たいしたものだよな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522Fふふ……そうですね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 6440, 0, 1530, 45)

    #N0112
    NpcTalk(
        0x1D,
        "男性の声",
        (
            "おーい！\x01",
            "みっしぃ、みーしぇ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(11850, 0, 8160, 3000)
    SetCameraDistance(20690, 3000)

    def lambda_39AE():

        label("loc_39AE")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_39AE")

    QueueWorkItem2(0x101, 1, lambda_39AE)

    def lambda_39C0():

        label("loc_39C0")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_39C0")

    QueueWorkItem2(0x103, 1, lambda_39C0)
    OP_95(0x1D, 10760, 0, 5250, 2000, 0x0)
    OP_93(0x1D, 0x0, 0x1F4)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    OP_6F(0x79)

    #C0113
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200Fあ……\x01",
            "お疲れ様です。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x1D,
        (
            "ああ、お疲れ様。\x01",
            "本当にごくろうだったね！\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x1D,
        (
            "なあ、聞いてくれよ。\x01",
            "今日の『みーしぇ』がなんだか\x01",
            "結構話題になってるみたいでね！\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F話題……ですか？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x1D,
        (
            "ああ、みっしぃに付き添って\x01",
            "時折みせていたクールな素振りが\x01",
            "たまらないってね！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x1D,
        (
            "うーん、これは\x01",
            "『みーしぇ』のキャラの方向性を\x01",
            "考えなおしたほうがいいかもなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212Fそ、そうですか……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2300, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x103)

    #C0120
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524F……こほん……\x01",
            "まあ、お役に立てたなら幸いです。\x02\x03",

            "#05520Fところで……\x01",
            "本物の役者さんは、まだ……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x1D,
        (
            "……ああ、そうだ忘れてた！\x01",
            "ついさっき到着したよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x1D,
        (
            "あとで向かうそうだから、\x01",
            "先にロッカールームに行って\x01",
            "待っててくれってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x1D,
        (
            "本当にお疲れ様。\x01",
            "よかったら、バイト代に\x01",
            "これを受け取ってくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x1D, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0124
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x34D, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0125
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202Fありがとうございます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0126
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200Fそれじゃ、ティオ……\x01",
            "上がるとするか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0127
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522Fええ、そうですね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    StopSound(821, 4000, 50)
    StopSound(126, 4000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1390", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_3742 end

    def Function_34_3DFC(): pass

    label("Function_34_3DFC")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "テーマパークの\x01",
            "見取り図が描かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_34_3DFC end

    SaveToFile()

Try(main)
