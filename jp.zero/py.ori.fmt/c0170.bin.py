from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0170.bin",                # FileName
        "c0170",                    # MapName
        "c0170",                    # Location
        0x0005,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 5, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0170",                  # 0
        "受付嬢パール",           # 1
        "受付嬢シンシア",         # 2
        "ハンソン",               # 3
        "リジョン",               # 4
        "プラダ",                 # 5
        "ベイカー",               # 6
        "サザーク",               # 7
        "セルゲイ課長",           # 8
        "ネストン支配人",         # 9
        "ジャネッタ",             # 10
        "バッジョ",               # 11
        "ドロテ",                 # 12
        "ケン",                   # 13
        "オネスト老人",           # 14
        "サンサン",               # 15
        "リーシャ",               # 16
        "プリエ",                 # 17
    ))

    AddCharChip((
        "chr/ch27400.itc",                   # 00
        "chr/ch26600.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch24300.itc",                   # 03
        "chr/ch27000.itc",                   # 04
        "chr/ch20000.itc",                   # 05
        "chr/ch10400.itc",                   # 06
        "chr/ch34200.itc",                   # 07
        "chr/ch20400.itc",                   # 08
        "chr/ch21600.itc",                   # 09
        "chr/ch02500.itc",                   # 0A
        "chr/ch32500.itc",                   # 0B
        "chr/ch05200.itc",                   # 0C
        "chr/ch29000.itc",                   # 0D
        "chr/ch34600.itc",                   # 0E
        "chr/ch25900.itc",                   # 0F
    ))

    DeclNpc(7480,    0,       10079,   225,  257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5880,    0,       11680,   225,  257,  0x0, 0,   14,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(59,      8000,    30040,   180,  257,  0x0, 0,   15,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(15979,   0,       9520,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(18110,   8000,    12220,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-11529,  8000,    8510,    225,  257,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-15989,  0,       25739,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(8289,    0,       2460,    90,   385,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-2660,   0,       9829,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-6659,   8000,    28870,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(14930,   0,       2589,    90,   257,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(13800,   8000,    6199,    225,  257,  0x0, 0,   6,   0,   0,   1,   0,   22,  255,  0)
    DeclNpc(8020,    8000,    17270,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-14449,  8000,    14420,   90,   257,  0x0, 0,   9,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(14220,   8000,    21190,   90,   405,  0x0, 0,   11,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(14220,   8000,    22209,   90,   405,  0x0, 0,   12,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(8750,    0,       1879,    90,   389,  0x0, 0,   13,  0,   0,   0,   0,   28,  255,  0)

    DeclActor(6250,    0,       9040,    1000,    7480,    1500,    10080,   0x007E, 0,  4,  0x0000)
    DeclActor(4440,    0,       10280,   1000,    5880,    1500,    11680,   0x007E, 0,  6,  0x0000)
    DeclActor(-480,    8000,    28360,   1000,    60,      9500,    30040,   0x007E, 0,  8,  0x0000)
    DeclActor(15980,   0,       7760,    1000,    15980,   1500,    9520,    0x007E, 0,  10, 0x0000)
    DeclActor(16480,   8000,    11730,   1000,    18110,   9500,    12220,   0x007E, 0,  12, 0x0000)
    DeclActor(-12390,  8000,    7660,    1000,    -11530,  9500,    8510,    0x007E, 0,  14, 0x0000)
    DeclActor(-16030,  0,       23800,   1000,    -15990,  1500,    25740,   0x007E, 0,  16, 0x0000)
    DeclActor(1670,    0,       13270,   800,     1670,    1500,    13270,   0x007C, 0,  37, 0x0000)
    DeclActor(5790,    0,       9800,    1000,    6620,    1500,    10670,   0x007E, 0,  6,  0x0000)

    ScpFunction((
        "Function_0_48C",          # 00, 0
        "Function_1_544",          # 01, 1
        "Function_2_61D",          # 02, 2
        "Function_3_839",          # 03, 3
        "Function_4_8FD",          # 04, 4
        "Function_5_901",          # 05, 5
        "Function_6_1683",         # 06, 6
        "Function_7_1687",         # 07, 7
        "Function_8_2364",         # 08, 8
        "Function_9_2368",         # 09, 9
        "Function_10_30B2",        # 0A, 10
        "Function_11_30B6",        # 0B, 11
        "Function_12_41C5",        # 0C, 12
        "Function_13_41C9",        # 0D, 13
        "Function_14_4F78",        # 0E, 14
        "Function_15_4F7C",        # 0F, 15
        "Function_16_6168",        # 10, 16
        "Function_17_616C",        # 11, 17
        "Function_18_7261",        # 12, 18
        "Function_19_7400",        # 13, 19
        "Function_20_8C30",        # 14, 20
        "Function_21_9A36",        # 15, 21
        "Function_22_A5EF",        # 16, 22
        "Function_23_AD13",        # 17, 23
        "Function_24_B43F",        # 18, 24
        "Function_25_BFF2",        # 19, 25
        "Function_26_BFFC",        # 1A, 26
        "Function_27_C006",        # 1B, 27
        "Function_28_C2E8",        # 1C, 28
        "Function_29_C342",        # 1D, 29
        "Function_30_C96A",        # 1E, 30
        "Function_31_CF82",        # 1F, 31
        "Function_32_D600",        # 20, 32
        "Function_33_DC55",        # 21, 33
        "Function_34_E28E",        # 22, 34
        "Function_35_E4B1",        # 23, 35
        "Function_36_E616",        # 24, 36
        "Function_37_EEAA",        # 25, 37
    ))


    def Function_0_48C(): pass

    label("Function_0_48C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4CC"),
        (1, "loc_4D8"),
        (2, "loc_4E4"),
        (3, "loc_4F0"),
        (4, "loc_4FC"),
        (5, "loc_508"),
        (6, "loc_514"),
        (SWITCH_DEFAULT, "loc_520"),
    )


    label("loc_4CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_4D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_4E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_4F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_4FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_508")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_514")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_520")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_52C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_543")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_52C")

    label("loc_543")

    Return()

    # Function_0_48C end

    def Function_1_544(): pass

    label("Function_1_544")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61C")
    OP_95(0xFE, 13800, 8000, 6200, 2000, 0x0)
    OP_95(0xFE, 14520, 8000, 20050, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8530, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -14240, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 23430, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 7560, 2000, 0x0)
    OP_95(0xFE, -11380, 8000, 2990, 2000, 0x0)
    OP_95(0xFE, 14040, 8000, 2490, 2000, 0x0)
    Jump("Function_1_544")

    label("loc_61C")

    Return()

    # Function_1_544 end

    def Function_2_61D(): pass

    label("Function_2_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_64D")
    SetChrPos(0x11, 14240, 0, 2440, 270)
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_64D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_66C")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_67A")
    Jump("loc_838")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_688")
    Jump("loc_838")

    label("loc_688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6A7")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6E3")
    SetChrPos(0x9, 6620, 0, 10670, 225)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 2)), scpexpr(EXPR_END)), "loc_6DE")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_6DE")

    Jump("loc_838")

    label("loc_6E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_70C")
    SetChrPos(0x9, 6620, 0, 10670, 225)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_838")

    label("loc_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_730")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_760")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    SetChrPos(0x11, -17370, 30, 22740, 45)
    Jump("loc_838")

    label("loc_760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_784")
    SetChrPos(0x11, 14240, 0, 2440, 270)
    SetChrFlags(0x12, 0x80)
    Jump("loc_838")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7B6")
    TurnDirection(0x8, 0x9, 0)
    TurnDirection(0x9, 0x8, 0)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x11, 14040, 8000, 21830, 90)
    Jump("loc_838")

    label("loc_7B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7D5")
    SetChrPos(0x11, -17370, 30, 22740, 45)
    Jump("loc_838")

    label("loc_7D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7F4")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_838")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_813")
    SetChrPos(0x11, -5240, 8000, 5490, 0)
    Jump("loc_838")

    label("loc_813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_821")
    Jump("loc_838")

    label("loc_821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_82F")
    Jump("loc_838")

    label("loc_82F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_838")

    label("loc_838")

    Return()

    # Function_2_61D end

    def Function_3_839(): pass

    label("Function_3_839")

    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_84B")
    Jump("loc_860")

    label("loc_84B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_860")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_66(0x8, 0x1)

    label("loc_860")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_881")
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    Jump("loc_88F")

    label("loc_881")

    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)

    label("loc_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AB")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8C2")

    label("loc_8AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8C2")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_8C2")

    label("loc_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8D0")
    Jump("loc_8FC")

    label("loc_8D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8EA")
    Jump("loc_8FC")

    label("loc_8EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_8FC")
    OP_1B(0x0, 0x0, 0x23)

    label("loc_8FC")

    Return()

    # Function_3_839 end

    def Function_4_8FD(): pass

    label("Function_4_8FD")

    Call(0, 5)
    Return()

    # Function_4_8FD end

    def Function_5_901(): pass

    label("Function_5_901")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_932")
    TurnDirection(0x0, 0x8, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    Call(0, 36)
    Return()

    label("loc_932")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_998")

    #C0001
    ChrTalk(
        0x8,
        "ふふ、見つかって良かったですね。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "また百貨店タイムズを\x01",
            "ご利用くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167F")

    label("loc_998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1B")

    #C0003
    ChrTalk(
        0x8,
        (
            "はぁ……スコットさんは\x01",
            "いつごろゆっくりできるように\x01",
            "なるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "……結婚はまだ遠いなぁ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AA4")

    label("loc_A1B")


    #C0005
    ChrTalk(
        0x8,
        (
            "……あっ、すみません！\x01",
            "ぼーっとしちゃっていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "何かありましたら\x01",
            "遠慮なく仰ってください。\x01",
            "丁寧にご案内させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA4")

    Jump("loc_167F")

    label("loc_AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B34")

    #C0007
    ChrTalk(
        0x8,
        (
            "仕事が始まって間もない\x01",
            "この時間はなんだか、\x01",
            "気だるくて心地いいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "今日も一日、お仕事を\x01",
            "頑張ってくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167F")

    label("loc_B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C07")

    #C0009
    ChrTalk(
        0x8,
        (
            "百貨店《タイムズ》へ\x01",
            "ようこそいらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "当店ではお客様の心をくすぐる\x01",
            "さまざまな催しが行われています。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "『心をくすぐると笑顔がこぼれる』……\x01",
            "それが支配人の座右の銘なのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167F")

    label("loc_C07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E17")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CB3")

    #C0012
    ChrTalk(
        0x8,
        (
            "恋人へのプレゼントを選んでいると\x01",
            "とても楽しい一時を過ごせますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "ふふ、どうかお買い物を\x01",
            "楽しんでいってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8E")

    label("loc_CB3")


    #C0014
    ChrTalk(
        0x8,
        (
            "お客様……もしかして\x01",
            "恋人へのプレゼントを\x01",
            "お選びですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "ふふ、とても恋人想いなんですね。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x19F,
        (
            "えっ……\x01",
            "い、いやいや、俺とフランさんは\x01",
            "まだそんな仲じゃあ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#0006F（本当に違うあたり、切ないな……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D8E")

    Jump("loc_E12")

    label("loc_D93")


    #C0018
    ChrTalk(
        0x8,
        (
            "マクダエル市長も御用達の\x01",
            "百貨店《タイムズ》へ\x01",
            "ようこそいらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "……なんて、ちょっと\x01",
            "あざとすぎますかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E12")

    Jump("loc_167F")

    label("loc_E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_E25")
    Jump("loc_167F")

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE4")

    #C0020
    ChrTalk(
        0x8,
        (
            "シンシア先輩みたいな美人の方は\x01",
            "ヒールでキチッとキメてる\x01",
            "イメージなんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "朝、スニーカーで\x01",
            "通勤しているのを見たときは\x01",
            "ちょっぴり驚いちゃいました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F7D")

    label("loc_EE4")


    #C0022
    ChrTalk(
        0x8,
        (
            "シンシア先輩みたいな美人の方は\x01",
            "ヒールでキチッとキメてる\x01",
            "イメージなんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "実はスニーカー姿が似合っているって、\x01",
            "ギャップがいいですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F7D")

    Jump("loc_167F")

    label("loc_F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1054")

    #C0024
    ChrTalk(
        0x8,
        (
            "ネストン支配人は、\x01",
            "色々な企画に携わってきた\x01",
            "すごい方なんだそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "昔は創立記念祭の行事進行にも\x01",
            "関わっていたとかいないとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "うーん、私が言うのもなんですが\x01",
            "只者じゃないですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167F")

    label("loc_1054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_10F7")

    #C0027
    ChrTalk(
        0x8,
        (
            "……あら、ジャネッタさんったら\x01",
            "食品売り場を眺めて\x01",
            "よだれをたらしているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "ふふ、ああいう子供っぽいところが\x01",
            "私たちを癒してくれるんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167F")

    label("loc_10F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_11B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1112")
    Call(0, 7)
    Jump("loc_11B3")

    label("loc_1112")

    TurnDirection(0x8, 0x0, 0)

    #C0029
    ChrTalk(
        0x8,
        (
            "実は私、ギルドの遊撃士に\x01",
            "婚約者がいるんですよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "あ、忙しくてなかなか会えないけど\x01",
            "私のことを大事に想ってくれる\x01",
            "とてもいい人なんですよ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 0)

    label("loc_11B3")

    Jump("loc_167F")

    label("loc_11B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_12D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1273")

    #C0031
    ChrTalk(
        0x8,
        (
            "こちらでは、駅やバス、飛行船の\x01",
            "時刻案内も行っていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "帝国や共和国からも\x01",
            "お客様が沢山いらっしゃるものですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        "皆様もぜひご利用くださいね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12CF")

    label("loc_1273")


    #C0034
    ChrTalk(
        0x8,
        (
            "こちらでは、駅やバス、飛行船の\x01",
            "時刻案内も行っていますよ。\x01",
            "皆様もぜひご利用くださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CF")

    Jump("loc_167F")

    label("loc_12D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_139A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1364")

    #C0035
    ChrTalk(
        0x8,
        (
            "……はぁ……スコットさん、\x01",
            "今頃何してるのかな……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0036
    ChrTalk(
        0x8,
        (
            "し、失礼しました。\x01",
            "お客様の前で……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1395")

    label("loc_1364")


    #C0037
    ChrTalk(
        0x8,
        (
            "失礼しました。\x01",
            "お客様の前でため息なんて……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1395")

    Jump("loc_167F")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1410")

    #C0038
    ChrTalk(
        0x8,
        (
            "支配人が何か\x01",
            "考え込んでらっしゃいますね……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "また新しい企画でも\x01",
            "練ってらっしゃるんでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167F")

    label("loc_1410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_146D")

    #C0040
    ChrTalk(
        0x8,
        "皆様、お早うございます。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "どうか本日も\x01",
            "一日元気にお過ごしくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167F")

    label("loc_146D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1500")

    #C0042
    ChrTalk(
        0x8,
        (
            "シンシア先輩はこの百貨店の\x01",
            "看板娘なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "とても女性らしくて素敵ですから、\x01",
            "街の女の子の憧れの的なんです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_157F")

    label("loc_1500")


    #C0044
    ChrTalk(
        0x8,
        (
            "シンシア先輩はこの百貨店の\x01",
            "看板娘なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "うふふ……かくいう私も、\x01",
            "シンシア先輩に憧れて\x01",
            "この仕事に就いたんです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157F")

    Jump("loc_167F")

    label("loc_1584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_167F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1621")

    #C0046
    ChrTalk(
        0x8,
        (
            "輸入食材や洋服、\x01",
            "靴に雑貨、アクセサリ……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "当百貨店にはいくつもの専門店があります。\x01",
            "ふふ、一度覗いてみてはいかがですか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_167F")

    label("loc_1621")


    #C0048
    ChrTalk(
        0x8,
        (
            "当百貨店には\x01",
            "いくつもの専門店があるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "ふふ、皆様も\x01",
            "覗いてみてはいかがですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167F")

    TalkEnd(0x8)
    Return()

    # Function_5_901 end

    def Function_6_1683(): pass

    label("Function_6_1683")

    Call(0, 7)
    Return()

    # Function_6_1683 end

    def Function_7_1687(): pass

    label("Function_7_1687")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16B8")
    TurnDirection(0x0, 0x9, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    Call(0, 36)
    Return()

    label("loc_16B8")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1785")

    #C0050
    ChrTalk(
        0x9,
        (
            "当百貨店では\x01",
            "遺失物の届けが多いんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "発見後１週間以上経つと\x01",
            "警察に届ける決まりなのですが……\x01",
            "常時十数点はお預かりしているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "皆様も落し物には\x01",
            "ご注意くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_1785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_182C")

    #C0053
    ChrTalk(
        0x9,
        (
            "夕暮れのあたるクロスベル市……\x01",
            "とても美しいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "美しい自然も良いですけど、\x01",
            "近代文化の中をジョギングするのも\x01",
            "なかなか悪くはないですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_182C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_18F3")

    #C0055
    ChrTalk(
        0x9,
        (
            "おはようございます、\x01",
            "ようこそ百貨店《タイムズ》へ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "開店時間から間もないですが、\x01",
            "すでにお客様にご利用いただいています。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "どうぞご遠慮なく、\x01",
            "お買い物をお楽しみ下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_18F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_19B6")

    #C0058
    ChrTalk(
        0x9,
        (
            "支配人のお顔、とても楽しそうです。\x01",
            "まるで新しいおもちゃを見つけた\x01",
            "子供みたい……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "ああいう顔をしているときは\x01",
            "とてもいい企画を思いついたときです。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        "ふふ、楽しみですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_19B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B03")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A8B")

    #C0061
    ChrTalk(
        0x9,
        (
            "１階には雑貨店、輸入食品店、\x01",
            "２階にはブティック、靴屋、\x01",
            "アクセサリ店が出店しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "各店、お客様のニーズに合う商品が\x01",
            "必ずございます。\x01",
            "どうかご覧になって下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_1A8B")


    #C0063
    ChrTalk(
        0x9,
        (
            "支配人は昔から、\x01",
            "業種を問わず色々な企画を\x01",
            "任されていたそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "財界、政界にも\x01",
            "とても顔が広いんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AFE")

    Jump("loc_2360")

    label("loc_1B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1BCA")

    #C0065
    ChrTalk(
        0x9,
        (
            "記念祭後の休みは\x01",
            "充実したものになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "まっ青な空の下のジョギングは、\x01",
            "爽やかで、とても気持ちよかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "ふふ、今度はパールさんも誘って\x01",
            "２人で走ってみましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_1BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1CFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C62")

    #C0068
    ChrTalk(
        0x9,
        (
            "意外に思われるのですが、\x01",
            "私、ジョギングが趣味なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "休みの日などは、\x01",
            "よくクロスベル市内を\x01",
            "走っているんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CF5")

    label("loc_1C62")


    #C0070
    ChrTalk(
        0x9,
        (
            "意外に思われるのですが、\x01",
            "私、ジョギングが趣味なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "スニーカーは\x01",
            "２階の靴屋で見繕っていただきました。\x01",
            "お客様にもお勧めいたしますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF5")

    Jump("loc_2360")

    label("loc_1CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1DD2")

    #C0072
    ChrTalk(
        0x9,
        (
            "私は元々、レミフェリアの百貨店で\x01",
            "働いていたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "そこで支配人にスカウトされて、\x01",
            "クロスベルに引っ越してきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "ネストン支配人という\x01",
            "一流の方に見出されて、\x01",
            "とても光栄な気持ちですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_1DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1E4A")

    #C0075
    ChrTalk(
        0x9,
        "日も落ちてきましたね。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "閉店時間が近づくと、\x01",
            "クロスベル市の市歌が\x01",
            "百貨店内に放送されるんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_1E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1FB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F36")
    TurnDirection(0x9, 0x8, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0077
    ChrTalk(
        0x9,
        (
            "ふふ……パールさんは\x01",
            "丁度悩みが多い頃なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "何だかんだと言っても、\x01",
            "やっぱり寂しいんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x8,
        (
            "そ、そうなんです……\x01",
            "もう婚約して丸１年なのに……！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FB4")

    label("loc_1F36")


    #C0080
    ChrTalk(
        0x9,
        (
            "あら……失礼致しました。\x01",
            "私とした事がお客様の前で……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "ご用がおありでしょうか？\x01",
            "誠心誠意ご案内させていただきますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB4")

    Jump("loc_2360")

    label("loc_1FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_202A")

    #C0082
    ChrTalk(
        0x9,
        "ようこそ、百貨店《タイムズ》へ。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "何かお探しでしょうか？\x01",
            "各店舗のご案内はお任せください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_202A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_20AA")

    #C0084
    ChrTalk(
        0x9,
        (
            "本日も百貨店《タイムズ》の\x01",
            "ご利用、ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "お忘れ物などないよう\x01",
            "お気をつけくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_20AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2136")

    #C0086
    ChrTalk(
        0x9,
        (
            "『百貨店の経営とは、すなわち\x01",
            "  お客様を飽きさせない事。』\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "……これが支配人の口癖なんです。\x01",
            "次の企画が楽しみですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_2136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_21BA")

    #C0088
    ChrTalk(
        0x9,
        (
            "当百貨店はお客様の声に\x01",
            "応えるべく尽力してまいります。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "ご不満の点などございましたら\x01",
            "お気軽に仰ってください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_21BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2243")

    #C0090
    ChrTalk(
        0x9,
        (
            "本日もご来店\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "当百貨店に関するご意見、\x01",
            "ご要望がありましたら\x01",
            "どうぞお申し付けくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_2243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2360")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F4")

    #C0092
    ChrTalk(
        0x9,
        "ようこそ、百貨店《タイムズ》へ。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "こちらは\x01",
            "総合インフォメーションとなります。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "店内で何かございましたら\x01",
            "遠慮なくお申し付けくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2360")

    label("loc_22F4")


    #C0095
    ChrTalk(
        0x9,
        (
            "こちらは\x01",
            "総合インフォメーションです。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "当店内で何かございましたら\x01",
            "遠慮なくお申し付けくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2360")

    TalkEnd(0x9)
    Return()

    # Function_7_1687 end

    def Function_8_2364(): pass

    label("Function_8_2364")

    Call(0, 9)
    Return()

    # Function_8_2364 end

    def Function_9_2368(): pass

    label("Function_9_2368")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2379")
    Jump("loc_23A7")

    label("loc_2379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_23A7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2393")
    Jump("loc_23A7")

    label("loc_2393")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_23A7")
    Call(0, 32)
    TalkEnd(0xA)
    Return()

    label("loc_23A7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30AE")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_240F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_240F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_242E")
    OP_AF(0x22)
    Jump("loc_2430")

    label("loc_242E")

    OP_AF(0x21)

    label("loc_2430")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30A9")

    label("loc_243F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2453")
    Jump("loc_30A9")

    label("loc_2453")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_254F")

    #C0097
    ChrTalk(
        0xA,
        (
            "プラダさんにまた\x01",
            "勝負を持ち掛けられましたよ。\x01",
            "やれやれ、本当に競争好きな方です。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        (
            "ですが、競うことで新たな\x01",
            "境地が拓けるのもまた事実……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "互いを高めあう為にも\x01",
            "この勝負、乗らせていただく\x01",
            "つもりですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_254F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_25DF")

    #C0100
    ChrTalk(
        0xA,
        (
            "履きなれない靴をなじませるには\x01",
            "とにかく歩くしかありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "新品の靴だからといって\x01",
            "大事にしすぎると、機能が泣きますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_25DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_26AE")

    #C0102
    ChrTalk(
        0xA,
        "当店では靴の修理も承っております。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "古い靴などは部品をそろえる為に\x01",
            "費用がかさむこともありますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "思い入れのある靴を\x01",
            "履き続けたいというお客様に\x01",
            "なかなか好評のサービスなのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_26AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2784")

    #C0105
    ChrTalk(
        0xA,
        (
            "靴の中にエアが入ったものが\x01",
            "最近の若者の流行です。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        (
            "衝撃を吸収するので\x01",
            "長時間の運動にも最適なのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "かのストレガー社の近年のモデルも、\x01",
            "ほとんどがエアを採用したものに\x01",
            "なっていますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_2784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2A44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_280D")

    #C0108
    ChrTalk(
        0xA,
        (
            "おや、お客様……\x01",
            "先ほど選ばれた靴は\x01",
            "そちらのお子様のものでしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        "#0100Fええ、そうなんです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28F7")

    label("loc_280D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_287F")

    #C0110
    ChrTalk(
        0xA,
        (
            "おや、お客様……\x01",
            "先ほど選ばれた靴は\x01",
            "そちらのお子様のものでしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        "#0200F先ほどはどうも。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28F7")

    label("loc_287F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_28F7")

    #C0112
    ChrTalk(
        0xA,
        (
            "おや、そちらのお子様の靴は\x01",
            "先ほど２人組の女性が買われていった……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x104,
        "#0300Fああ、そりゃうちの連れだな。\x02",
    )

    CloseMessageWindow()

    label("loc_28F7")


    #C0114
    ChrTalk(
        0xA,
        (
            "ふふ、履き心地はどうですか？\x01",
            "多少大きめの靴を選ばせて頂きましたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x153,
        "#1110Fゆったりしてていいよ～！\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "それはよかった。\x01",
            "また何かありましたらお申し付けくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A3F")

    label("loc_29AD")


    #C0117
    ChrTalk(
        0xA,
        (
            "子供の足はすぐに大きくなりますからね。\x01",
            "ピッタリより多少大きめの方がいいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "次回ご来店の際も、是非とも\x01",
            "当店にお立ち寄りくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3F")

    Jump("loc_30A9")

    label("loc_2A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2ACA")

    #C0119
    ChrTalk(
        0xA,
        (
            "小さい靴はお子様の成長を\x01",
            "妨げる可能性があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xA,
        (
            "ぴったりより、少し爪先が余るサイズを\x01",
            "おすすめいたしますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_2ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2B31")

    #C0121
    ChrTalk(
        0xA,
        (
            "靴のサイズも\x01",
            "豊富にとりそろえております。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        "気兼ねせず、私に声をかけてください。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_2B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2B90")

    #C0123
    ChrTalk(
        0xA,
        (
            "おや、このような時間まで\x01",
            "お疲れ様です。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        "靴をお急ぎでお探しでしょうか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_2B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2C37")

    #C0125
    ChrTalk(
        0xA,
        (
            "最近人気を博しているのが\x01",
            "革靴に見えるスニーカーです。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "職場でも遜色なく使えるということで\x01",
            "ビジネスマンの間で\x01",
            "密かなブームになっているのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_2C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2CD5")

    #C0127
    ChrTalk(
        0xA,
        (
            "お客さまのように歩き回る職業の方は、\x01",
            "よい靴を選ばれる事をおすすめします。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xA,
        (
            "靴によって、長時間歩いた後の\x01",
            "疲れ方などは全然違うのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_2CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2D60")

    #C0129
    ChrTalk(
        0xA,
        (
            "クロスベル自治州には\x01",
            "創立記念祭という\x01",
            "ビッグイベントがあるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "どの店も、期間中が\x01",
            "最大のかきいれ時なのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_2D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2DD2")

    #C0131
    ChrTalk(
        0xA,
        (
            "近頃、またマフィア絡みの\x01",
            "黒い噂を聞きますねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "観光客の足に\x01",
            "影響しなければいいんですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_2DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2E82")

    #C0133
    ChrTalk(
        0xA,
        (
            "靴のデザインには、\x01",
            "職人の性格が良く表れています。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "同じ靴というカテゴリに属するものが\x01",
            "こうまで形の違うものになるのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        "そう考えると胸が躍ります。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_2E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2F59")

    #C0136
    ChrTalk(
        0xA,
        (
            "ウチも昔は服も扱っていたのですが、\x01",
            "店舗に入る際に靴専門になったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "ブティックのプラダさんは\x01",
            "その個人経営時代のライバルなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "今でもときどき、\x01",
            "こっちにつっかかってくるんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A9")

    label("loc_2F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_30A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3029")

    #C0139
    ChrTalk(
        0xA,
        (
            "いらっしゃいませ。\x01",
            "当店では靴を取り扱っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "運動靴・革靴・ブーツ……\x01",
            "お客様のニーズに合わせた品揃えを\x01",
            "取り揃えております。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        "どうぞお気軽に覗いていってください。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30A9")

    label("loc_3029")


    #C0142
    ChrTalk(
        0xA,
        (
            "人気スニーカーメーカーである\x01",
            "ストレガー社製品なども\x01",
            "順次取り扱っていく予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        "どうぞお気軽に覗いていってください。\x02",
    )

    CloseMessageWindow()

    label("loc_30A9")

    Jump("loc_23B1")

    label("loc_30AE")

    TalkEnd(0xA)
    Return()

    # Function_9_2368 end

    def Function_10_30B2(): pass

    label("Function_10_30B2")

    Call(0, 11)
    Return()

    # Function_10_30B2 end

    def Function_11_30B6(): pass

    label("Function_11_30B6")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_30C7")
    Jump("loc_30F5")

    label("loc_30C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_30F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_30E1")
    Jump("loc_30F5")

    label("loc_30E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_30F5")
    Call(0, 30)
    TalkEnd(0xB)
    Return()

    label("loc_30F5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C1")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_315D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_315D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_317D")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41BC")

    label("loc_317D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3191")
    Jump("loc_41BC")

    label("loc_3191")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41BC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3235")

    #C0144
    ChrTalk(
        0xB,
        (
            "アルモリカ村から\x01",
            "新鮮なお野菜が届いたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "なんだかんだ言っても、\x01",
            "採れたての食材が\x01",
            "一番美味しいですからねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41BC")

    label("loc_3235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_32B3")

    #C0146
    ChrTalk(
        0xB,
        (
            "店にない商品があったら\x01",
            "気兼ねなく言ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xB,
        (
            "この私がどんな手を使ってでも\x01",
            "仕入れてみせますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41BC")

    label("loc_32B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3423")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A0")

    #C0148
    ChrTalk(
        0xB,
        (
            "最近お天気がいいですね。\x01",
            "お陰で娘のやっているジュース屋も\x01",
            "順調みたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "何人かお得意さんもいるらしくて\x01",
            "家でもよく自慢するんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        (
            "ふふ……楽しそうで何よりだわ。\x01",
            "母としても嬉しく思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_341E")

    label("loc_33A0")


    #C0151
    ChrTalk(
        0xB,
        (
            "娘は自分の力でお商売がしたいと\x01",
            "ジュース屋を始めたんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "ふふ……どうやらお商売が\x01",
            "板についてきたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_341E")

    Jump("loc_41BC")

    label("loc_3423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_347F")

    #C0153
    ChrTalk(
        0xB,
        "良質な食材を一斉入荷したんですよ。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        "豊かな食卓を楽しんでくださいな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_41BC")

    label("loc_347F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_35CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_356B")

    #C0155
    ChrTalk(
        0xB,
        (
            "料理の出来を決めるのは、\x01",
            "料理人の腕、良質な食材……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "でも一番大事なのは、\x01",
            "やっぱり食べる人のことを想って\x01",
            "作ることだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "ささ、皆さんもいかが～？\x01",
            "食材が無くちゃ\x01",
            "お料理は作れませんからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_35C5")

    label("loc_356B")


    #C0158
    ChrTalk(
        0xB,
        (
            "今晩の料理に\x01",
            "王様ポテトなんていかが～？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "今日は特別立派なものを\x01",
            "仕入れてますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35C5")

    Jump("loc_41BC")

    label("loc_35CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_36CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_367D")

    #C0160
    ChrTalk(
        0xB,
        (
            "やっぱり記念祭が近いと\x01",
            "お客さんが増えますねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        (
            "……ふふっ、うちの娘も\x01",
            "今ごろ頑張っているのかしらね。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        "お母さんも負けていられませんね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36C9")

    label("loc_367D")


    #C0163
    ChrTalk(
        0xB,
        (
            "娘もジュース屋を開いて\x01",
            "頑張っているんですもの。\x01",
            "負けていられませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C9")

    Jump("loc_41BC")

    label("loc_36CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_37E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3788")

    #C0164
    ChrTalk(
        0xB,
        (
            "今朝は鉄道便が\x01",
            "貨物検査で遅れたらしくって。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xB,
        (
            "お野菜を運んで並べるので\x01",
            "色々と慌しかったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xB,
        (
            "あいたた……腰にきちゃったわ。\x01",
            "私ももう歳かしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37DB")

    label("loc_3788")


    #C0167
    ChrTalk(
        0xB,
        (
            "今朝は鉄道便が\x01",
            "貨物検査で遅れていたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        "鉄道便って時々遅れるんですよね。\x02",
    )

    CloseMessageWindow()

    label("loc_37DB")

    Jump("loc_41BC")

    label("loc_37E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_385F")

    #C0169
    ChrTalk(
        0xB,
        (
            "そろそろ仕事帰りの\x01",
            "お客さんが増える時間ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "百貨店の営業は\x01",
            "まだまだこれから。\x01",
            "もう一頑張りですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41BC")

    label("loc_385F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3989")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3925")

    #C0171
    ChrTalk(
        0xB,
        (
            "んー、共和国産の最高級ワインは\x01",
            "今週は３０ってトコかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xB,
        (
            "記念祭前はパーティ用の\x01",
            "高級食材の需要も上がるんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "早めに発注して\x01",
            "おいた方がよさそうだわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3984")

    label("loc_3925")


    #C0174
    ChrTalk(
        0xB,
        (
            "記念祭前はパーティ用の\x01",
            "食材の需要が上がるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        "高級食材もばんばん売れるんですよ。\x02",
    )

    CloseMessageWindow()

    label("loc_3984")

    Jump("loc_41BC")

    label("loc_3989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3AF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A61")

    #C0176
    ChrTalk(
        0xB,
        (
            "うちの娘は行政区で\x01",
            "ジュース屋をやっているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "大分商売に慣れてきたみたいで\x01",
            "家では何かと自慢するんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xB,
        (
            "ふふ、私から見ればまだまだね。\x01",
            "商人の道は険しいんですから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3AEB")

    label("loc_3A61")


    #C0179
    ChrTalk(
        0xB,
        (
            "私も以前は店を持っていましたからね。\x01",
            "商売の事はよく判っているつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xB,
        (
            "娘も頑張っているようだけど\x01",
            "まだまだといった所ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AEB")

    Jump("loc_41BC")

    label("loc_3AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3B9B")

    #C0181
    ChrTalk(
        0xB,
        (
            "いらっしゃ～い！\x01",
            "《リジョンフード》へようこそ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xB,
        (
            "今日はリベール産の\x01",
            "にがトマトが入荷していますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xB,
        (
            "とっても健康にいいとか。\x01",
            "お一ついかが～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41BC")

    label("loc_3B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3D99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D12")

    #C0184
    ChrTalk(
        0xB,
        (
            "最近、高級紅茶を買っていく\x01",
            "常連さんがいるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        "セルゲイさんって方なんだけど……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xB,
        (
            "ふふ、お話が面白くって。\x01",
            "今日は小一時間雑談してしまったわ㈱\x02",
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

    #C0187
    ChrTalk(
        0x102,
        (
            "#0106F（課長……私たちが\x01",
            "  苦労している間に……）\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x103,
        "#0200F（……さいてーです……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D94")

    label("loc_3D12")


    #C0189
    ChrTalk(
        0xB,
        (
            "セルゲイさん、よく高級紅茶を\x01",
            "買っていく常連さんなんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xB,
        (
            "ふふ、お話が面白くって。\x01",
            "今日は小一時間雑談してしまったわ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D94")

    Jump("loc_41BC")

    label("loc_3D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EA7")

    #C0191
    ChrTalk(
        0xB,
        (
            "最近、共和国の穀倉地帯は\x01",
            "雨続きらしいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xB,
        (
            "んー、来週辺りから\x01",
            "共和国産のお野菜は値上がりするから\x01",
            "帝国産を２割増やして……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "……うん、仕入れの\x01",
            "調整で何とかなりそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xB,
        (
            "できればお客さんには\x01",
            "迷惑を掛けたくないですもの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F13")

    label("loc_3EA7")


    #C0195
    ChrTalk(
        0xB,
        (
            "輸入食材を扱っていると\x01",
            "外国の情勢にも気を遣います。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "ふふ、それがこの仕事の\x01",
            "醍醐味なんですけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F13")

    Jump("loc_41BC")

    label("loc_3F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_40A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4033")

    #C0197
    ChrTalk(
        0xB,
        (
            "うちは天下のタイムズ百貨店、\x01",
            "食材の品揃えもクロスベル一ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "帝国産、共和国産から\x01",
            "リベール産にレミフェリア産……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        (
            "さらにはオレド自治州産の香辛料まで、\x01",
            "世界中から取り寄せています。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xB,
        (
            "ふふ、ちなみに今も\x01",
            "取扱品を増やしている所なんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40A1")

    label("loc_4033")


    #C0201
    ChrTalk(
        0xB,
        (
            "実は私、以前は\x01",
            "貿易商をやっていたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xB,
        (
            "ふふ、輸入食材の仕入れには\x01",
            "つい熱が入ってしまいますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40A1")

    Jump("loc_41BC")

    label("loc_40A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_41BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_414E")

    #C0203
    ChrTalk(
        0xB,
        (
            "《リジョンフード》の\x01",
            "コーナーにようこそ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xB,
        (
            "うちは輸入食材なんかも\x01",
            "豊富に扱ってますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xB,
        (
            "どうぞどうぞ、\x01",
            "見ていってくださ～い。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41BC")

    label("loc_414E")


    #C0206
    ChrTalk(
        0xB,
        (
            "うちは鉄道便や飛行船を使って\x01",
            "輸入食材も取り寄せてるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xB,
        (
            "どうぞどうぞ、\x01",
            "見ていってくださ～い。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41BC")

    Jump("loc_30FF")

    label("loc_41C1")

    TalkEnd(0xB)
    Return()

    # Function_11_30B6 end

    def Function_12_41C5(): pass

    label("Function_12_41C5")

    Call(0, 13)
    Return()

    # Function_12_41C5 end

    def Function_13_41C9(): pass

    label("Function_13_41C9")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_41DA")
    Jump("loc_4208")

    label("loc_41DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4208")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_41F4")
    Jump("loc_4208")

    label("loc_41F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_4208")
    Call(0, 31)
    TalkEnd(0xC)
    Return()

    label("loc_4208")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4212")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F74")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4270")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4270")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_428F")
    OP_AF(0x1F)
    Jump("loc_4291")

    label("loc_428F")

    OP_AF(0x1E)

    label("loc_4291")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F6F")

    label("loc_42A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42B4")
    Jump("loc_4F6F")

    label("loc_42B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F6F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4355")

    #C0208
    ChrTalk(
        0xC,
        (
            "自分に革命を起こすような\x01",
            "ファッションとの出会い……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xC,
        (
            "それは服を捜し求める者にしか\x01",
            "訪れない貴重な出会いなのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_4355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_43FC")

    #C0210
    ChrTalk(
        0xC,
        (
            "大人びた服装、子供らしい服装……\x01",
            "いろいろなファッションが\x01",
            "あると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xC,
        (
            "背伸びして分不相応の物を着るより、\x01",
            "似合うものを着るのが一番ですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_43FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_44CE")

    #C0212
    ChrTalk(
        0xC,
        "制服って美しいですよね。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xC,
        (
            "その仕事をまっとうするために\x01",
            "最適化された服装には、\x01",
            "目には見えない美しさがありますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        (
            "警察官や警備隊の制服も\x01",
            "私はファッションとして\x01",
            "高く買っていますのよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_44CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4584")

    #C0215
    ChrTalk(
        0xC,
        (
            "ほんの少しのアクセントが\x01",
            "ファッション全体の印象を変える\x01",
            "ということもありますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xC,
        (
            "ベイカーさんのところで\x01",
            "アクセサリを見繕ってみるのも\x01",
            "よいかもしれませんわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_4584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4846")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4615")

    #C0217
    ChrTalk(
        0xC,
        "あら、お客様は先ほどの……\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x102,
        (
            "#0100Fどうも、さっきは服選びを\x01",
            "手伝っていただいて\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_470F")

    label("loc_4615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_468D")

    #C0219
    ChrTalk(
        0xC,
        "あら、お客様は先ほどの……\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#0200Fどうも。\x01",
            "先ほどは服を見立てていただいて\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_470F")

    label("loc_468D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_470F")

    #C0221
    ChrTalk(
        0xC,
        "あら、そのお子様の服はさっきの……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x104,
        (
            "#0300Fそういや、お嬢とティオすけは\x01",
            "ここでキー坊の服を買ってきたんだったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_470F")


    #C0223
    ChrTalk(
        0xC,
        (
            "なるほど、そちらのお子様の\x01",
            "お洋服だったのですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x153,
        "#1109Fえへへ、似合う？\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        (
            "うふふ、よく似合っていますわ。\x01",
            "私も手伝った甲斐がありました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4841")

    label("loc_47AD")


    #C0226
    ChrTalk(
        0xC,
        (
            "お子様に喜んでいただけているようで、\x01",
            "私も手伝った甲斐がありました。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xC,
        (
            "子供用の服も沢山取り揃えてますから、\x01",
            "何度でも足を運んでくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4841")

    Jump("loc_4F6F")

    label("loc_4846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_492A")

    #C0228
    ChrTalk(
        0xC,
        (
            "ミシュラム保養地のほうには\x01",
            "高級ブティックが\x01",
            "出店されているようですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xC,
        (
            "でも、品揃えではきっと負けません。\x01",
            "立地の差は言わずもがな……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xC,
        (
            "私はもっとお客様に近い形で\x01",
            "ファッションを提供していきたいのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_492A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_49AA")

    #C0231
    ChrTalk(
        0xC,
        (
            "当店ではフォーマルウェアの\x01",
            "取り扱いも多数ございますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xC,
        (
            "冠婚葬祭には是非とも当店を\x01",
            "ごひいきくださいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_49AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4A50")

    #C0233
    ChrTalk(
        0xC,
        "ふぅ……もうすぐ閉店時間ですわね。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xC,
        (
            "個人経営のときは、\x01",
            "それこそがむしゃらに深夜まで\x01",
            "やっていたものですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xC,
        "私もトシということかしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_4A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4AE1")

    #C0236
    ChrTalk(
        0xC,
        (
            "ハンソンさんとは\x01",
            "以前、商売敵だったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xC,
        (
            "彼が靴屋に鞍替えしてからは\x01",
            "なんだか張り合いが\x01",
            "なくなってしまいましたわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_4AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4BAC")

    #C0238
    ChrTalk(
        0xC,
        (
            "動きやすさや耐久性を重視するか、\x01",
            "組み合わせやデザインを重視するか……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xC,
        (
            "ファッションに何を求めるかは\x01",
            "お客様によって千差万別ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xC,
        (
            "どうか、思うままに\x01",
            "服を選んでくださいまし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_4BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4C42")

    #C0241
    ChrTalk(
        0xC,
        (
            "いらっしゃいませ。\x01",
            "ブティック《ルッカ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xC,
        (
            "うふふ、当店は本日も大好調ですわ。\x01",
            "どうかごゆっくり楽しんでくださいまし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_4C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4D26")

    #C0243
    ChrTalk(
        0xC,
        (
            "私も店を立ち上げたばかりの頃は\x01",
            "ブランドの買い付けに\x01",
            "外国を飛び回ったものですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xC,
        (
            "今では仕入れルートも確立しましたし\x01",
            "注文ひとつで済んでしまいますけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xC,
        (
            "たまにあの頃が\x01",
            "懐かしく思えてしまいますわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_4D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4DEB")

    #C0246
    ChrTalk(
        0xC,
        (
            "クロスベルには当店のような\x01",
            "ブティックが沢山ありますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xC,
        (
            "特に当店はマイナーなブランドまで\x01",
            "ほぼ網羅しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        (
            "決して他店に引けは取らない\x01",
            "品揃えをお楽しみ下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_4DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4E5D")

    #C0249
    ChrTalk(
        0xC,
        (
            "クロスベルには世界中の\x01",
            "ブランド品が集まっていますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xC,
        (
            "皆様もどうか\x01",
            "お楽しみくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F6F")

    label("loc_4E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4F6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EFB")

    #C0251
    ChrTalk(
        0xC,
        "ブティック《ルッカ》へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xC,
        (
            "キッズ物から紳士服、\x01",
            "各種ブランド品も扱っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        "ご用があれば何なりとどうぞ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F6F")

    label("loc_4EFB")


    #C0254
    ChrTalk(
        0xC,
        (
            "キッズ物から紳士服、\x01",
            "各種ブランド品も扱っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xC,
        (
            "どうぞブティック《ルッカ》を\x01",
            "お楽しみくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F6F")

    Jump("loc_4212")

    label("loc_4F74")

    TalkEnd(0xC)
    Return()

    # Function_13_41C9 end

    def Function_14_4F78(): pass

    label("Function_14_4F78")

    Call(0, 15)
    Return()

    # Function_14_4F78 end

    def Function_15_4F7C(): pass

    label("Function_15_4F7C")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4F8D")
    Jump("loc_4FBB")

    label("loc_4F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4FBB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4FA7")
    Jump("loc_4FBB")

    label("loc_4FA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_4FBB")
    Call(0, 33)
    TalkEnd(0xD)
    Return()

    label("loc_4FBB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6164")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5023")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5023")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5042")
    OP_AF(0x25)
    Jump("loc_5044")

    label("loc_5042")

    OP_AF(0x24)

    label("loc_5044")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_615F")

    label("loc_5053")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5067")
    Jump("loc_615F")

    label("loc_5067")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_615F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5137")

    #C0256
    ChrTalk(
        0xD,
        (
            "そういえば……\x01",
            "委託していた七耀石の加工が\x01",
            "済んだと業者から連絡がきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xD,
        (
            "あとは帝国から送られてくるのを\x01",
            "待つだけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xD,
        "ふふ、どうにも待ち遠しいですな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_615F")

    label("loc_5137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5237")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51DB")

    #C0259
    ChrTalk(
        0xD,
        (
            "……ガンツ？\x01",
            "ああ、あの羽振りのいい鉱員ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xD,
        (
            "最近のお得意さまなのですが\x01",
            "ここ２日ほど顔を見せないので\x01",
            "心配していたのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5232")

    label("loc_51DB")


    #C0261
    ChrTalk(
        0xD,
        (
            "ガンツさんというと、\x01",
            "あの羽振りのいい鉱員の……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xD,
        "彼、どうかなさったのですか？\x02",
    )

    CloseMessageWindow()

    label("loc_5232")

    Jump("loc_615F")

    label("loc_5237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_52E8")

    #C0263
    ChrTalk(
        0xD,
        (
            "昨日から、あのガンツという鉱員は\x01",
            "来ていないのです。\x01",
            "最近のお得意様だったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xD,
        (
            "まぁ、カジノ稼ぎだったようですし\x01",
            "運が尽きたというところでしょうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_615F")

    label("loc_52E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_53D8")

    #C0265
    ChrTalk(
        0xD,
        (
            "少し前から、えらく羽振りの良い\x01",
            "客が来るようになりましてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xD,
        (
            "いつも女性をはべらせて、\x01",
            "アクセサリーを５、６個買って\x01",
            "贈っているようなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xD,
        (
            "カジノで稼いだといっていましたが……\x01",
            "いやはや、うらやましい限りですな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_615F")

    label("loc_53D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5825")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57AF")

    #C0268
    ChrTalk(
        0xD,
        (
            "記念祭中にミシュラムに向かわれた\x01",
            "旅行者のトマさん、という方がいるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xD,
        (
            "彼は記念祭中にプロポーズするため、\x01",
            "こちらで結婚指輪を買って行かれたんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_55E9")

    #C0270
    ChrTalk(
        0xD,
        (
            "トマさんは先日、帰国前に\x01",
            "うちに顔を出しに来ましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xD,
        (
            "当店で仕上げた婚約指輪のおかげで\x01",
            "見事プロポーズが成ったと喜んでおられました。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xD,
        (
            "いやはや、喜ばしいことです。\x01",
            "一晩で指輪に名前を彫れなどという\x01",
            "無茶をやり遂げた甲斐がありましたなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#0004F（プロポーズ、成功したのか……\x01",
            "  俺たちも頑張った甲斐があったな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57A7")

    label("loc_55E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_576C")

    #C0274
    ChrTalk(
        0xD,
        (
            "トマさんは先日、帰国前に\x01",
            "うちに顔を出しに来ましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xD,
        (
            "当店で仕上げた婚約指輪は\x01",
            "不注意で失くされてしまったそうですが、\x01",
            "一応プロポーズは成ったと喜んでおられました。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xD,
        (
            "……いやはや、喜ばしいことですが……\x01",
            "一晩で指輪に名前を彫れなどという\x01",
            "無茶をやり遂げた甲斐がありませんでしたなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        (
            "#0004F（プロポーズ、成功したのか……\x01",
            "  指輪、見つけてあげたかったな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57A7")

    label("loc_576C")


    #C0278
    ChrTalk(
        0xD,
        (
            "さて、彼の大勝負は一体\x01",
            "どうなったんでしょうかねぇ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57A7")

    SetScenarioFlags(0x0, 5)
    Jump("loc_5820")

    label("loc_57AF")


    #C0279
    ChrTalk(
        0xD,
        (
            "しかし、プロポーズというのは\x01",
            "どんな形であれよいものですなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xD,
        "つい若かりし頃を思い出してしまいますよ。\x02",
    )

    CloseMessageWindow()

    label("loc_5820")

    Jump("loc_615F")

    label("loc_5825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5950")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D5")

    #C0281
    ChrTalk(
        0xD,
        (
            "なんとか記念祭に向けた新商品を\x01",
            "仕入れることができそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xD,
        (
            "……今年もあの忌まわしい\x01",
            "偽ブランド業者どもが\x01",
            "入ってこなければいいのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_594B")

    label("loc_58D5")


    #C0283
    ChrTalk(
        0xD,
        (
            "記念祭の時期になると\x01",
            "偽ブランド業者なる不届き者が\x01",
            "クロスベルに現れるのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xD,
        "お客様もお気をつけください。\x02",
    )

    CloseMessageWindow()

    label("loc_594B")

    Jump("loc_615F")

    label("loc_5950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_59F4")

    #C0285
    ChrTalk(
        0xD,
        (
            "記念祭に向けて、\x01",
            "そろそろ新しい商品を\x01",
            "仕入れたいところです。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xD,
        (
            "ただ、装飾品や宝石は密輸の対象に\x01",
            "なりやすいものだから、\x01",
            "輸入が大変なんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_615F")

    label("loc_59F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5A83")

    #C0287
    ChrTalk(
        0xD,
        (
            "そういえば、\x01",
            "クロスベルタイムズの新刊を\x01",
            "まだ読んでいなかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xD,
        (
            "あとでサザーク君の所に行って\x01",
            "買ってくるとしようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_615F")

    label("loc_5A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5B2D")

    #C0289
    ChrTalk(
        0xD,
        (
            "……おっと失礼。\x01",
            "クロスベル通信社の\x01",
            "経済誌を読んでいたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xD,
        (
            "本日の七耀石の取引価格が\x01",
            "載っているものでしてね。\x01",
            "まぁ、職業病のようなものですな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_615F")

    label("loc_5B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C19")

    #C0291
    ChrTalk(
        0xD,
        (
            "先ほど美術品の卸しをしたいと仰る\x01",
            "業者様がいらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xD,
        (
            "……ですが、どうも質が良くないため\x01",
            "謹んでお断りいたしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xD,
        (
            "ふむ、金儲け目当てで取引なさる方は\x01",
            "どうも審美眼に欠ける気が致します。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5CA2")

    label("loc_5C19")


    #C0294
    ChrTalk(
        0xD,
        (
            "最近の商人は儲けにかまけて、\x01",
            "商品の質を見極める目が\x01",
            "鍛えられていないようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xD,
        (
            "是非とも審美眼を\x01",
            "磨いていただきたいものですな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA2")

    Jump("loc_615F")

    label("loc_5CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5D40")

    #C0296
    ChrTalk(
        0xD,
        (
            "鉱山町マインツで採掘される\x01",
            "七耀石は、それは美しい宝石です。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xD,
        (
            "特に希少価値の高い結晶は\x01",
            "かなりの高値で取り引き\x01",
            "されているのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_615F")

    label("loc_5D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E3A")

    #C0298
    ChrTalk(
        0xD,
        (
            "近頃、闇市場の問題に\x01",
            "心を痛めているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xD,
        (
            "事業に失敗した資産家の\x01",
            "保有する美術品などが\x01",
            "流れていってしまう領域でしてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xD,
        (
            "そこではどんなに美しい美術品も\x01",
            "裏の世界のものとなってしまう……\x01",
            "嘆かわしいことですな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5E9C")

    label("loc_5E3A")


    #C0301
    ChrTalk(
        0xD,
        (
            "闇市場の問題には\x01",
            "心を痛めております。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xD,
        (
            "クロスベル警察も\x01",
            "何とかしてくださればよいものを。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E9C")

    Jump("loc_615F")

    label("loc_5EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5FF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F7E")

    #C0303
    ChrTalk(
        0xD,
        (
            "よい美術品の噂を聞くと、\x01",
            "居てもたってもいられなくなる\x01",
            "タチでしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xD,
        (
            "先日はレマン自治州の美術館へ\x01",
            "青磁の壷を拝観しにいきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xD,
        (
            "叶うことならお客様にも\x01",
            "お見せしたかった所ですな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5FEE")

    label("loc_5F7E")


    #C0306
    ChrTalk(
        0xD,
        (
            "レマン自治州で見た\x01",
            "青磁の壷は良い物でございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xD,
        (
            "叶うことならお客様にも\x01",
            "お見せしたかった所ですな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FEE")

    Jump("loc_615F")

    label("loc_5FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_60EA")

    #C0308
    ChrTalk(
        0xD,
        (
            "私は元々帝国で美術商を\x01",
            "やっていたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xD,
        (
            "ですが、一部の富豪たちの中だけで\x01",
            "美術品が扱われる現状に\x01",
            "嫌気が差して、装飾品店を開いたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xD,
        (
            "装飾品という形で\x01",
            "一般に広く美術品を広められる。\x01",
            "とてもやりがいを感じていますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_615F")

    label("loc_60EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_615F")

    #C0311
    ChrTalk(
        0xD,
        (
            "当店では主に装飾品・小物などを\x01",
            "取り扱っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xD,
        (
            "少々値は張りますが\x01",
            "どれも良い品ばかりですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_615F")

    Jump("loc_4FC5")

    label("loc_6164")

    TalkEnd(0xD)
    Return()

    # Function_15_4F7C end

    def Function_16_6168(): pass

    label("Function_16_6168")

    Call(0, 17)
    Return()

    # Function_16_6168 end

    def Function_17_616C(): pass

    label("Function_17_616C")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_617D")
    Jump("loc_61AB")

    label("loc_617D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_61AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6197")
    Jump("loc_61AB")

    label("loc_6197")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_61AB")
    Call(0, 29)
    TalkEnd(0xE)
    Return()

    label("loc_61AB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_725D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6213")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6213")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6232")
    OP_AF(0x1B)
    Jump("loc_6294")

    label("loc_6232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6242")
    OP_AF(0x1A)
    Jump("loc_6294")

    label("loc_6242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6252")
    OP_AF(0x19)
    Jump("loc_6294")

    label("loc_6252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6262")
    OP_AF(0x18)
    Jump("loc_6294")

    label("loc_6262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6272")
    OP_AF(0x17)
    Jump("loc_6294")

    label("loc_6272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6282")
    OP_AF(0x16)
    Jump("loc_6294")

    label("loc_6282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6292")
    OP_AF(0x15)
    Jump("loc_6294")

    label("loc_6292")

    OP_AF(0x14)

    label("loc_6294")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7258")

    label("loc_62A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62B7")
    Jump("loc_7258")

    label("loc_62B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7258")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6372")

    #C0313
    ChrTalk(
        0xE,
        (
            "今度久しぶりに休みがとれてね。\x01",
            "共和国のほうへ里帰りする予定なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xE,
        (
            "クロスベルの店が繁盛してると知ったら、\x01",
            "商売仲間がみんな悔しがるぞ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7258")

    label("loc_6372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_63D5")

    #C0315
    ChrTalk(
        0xE,
        "え？　居なくなった人がいるって？\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xE,
        (
            "うーん、心配だねぇ。\x01",
            "何があったんだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7258")

    label("loc_63D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_647E")

    #C0317
    ChrTalk(
        0xE,
        (
            "商品のディスプレーは\x01",
            "ただ置けばいいというものじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xE,
        (
            "お客さんに買いたいと思わせるよう、\x01",
            "綿密に計算され尽くした物でなければ\x01",
            "意味がないんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7258")

    label("loc_647E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_64F5")

    #C0319
    ChrTalk(
        0xE,
        "だんだんウチも品揃えが整ってきたな。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xE,
        (
            "不自由なくお客さんに商品を\x01",
            "提供できるのはいいことだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7258")

    label("loc_64F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6562")

    #C0321
    ChrTalk(
        0xE,
        "記念祭の売り上げは極めて上々だったよ。\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xE,
        (
            "ふふふ……\x01",
            "今年のボーナスが楽しみになるねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7258")

    label("loc_6562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_661D")

    #C0323
    ChrTalk(
        0xE,
        (
            "記念祭に向けてウチのコーナーも\x01",
            "仕入れを増やしてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xE,
        (
            "観光客向けのパンフレットとかは\x01",
            "毎年かなり売れるしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xE,
        (
            "普段は地味な雑貨コーナーも\x01",
            "忙しくなるんだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7258")

    label("loc_661D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_675F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66F2")

    #C0326
    ChrTalk(
        0xE,
        (
            "ジャネッタちゃん、\x01",
            "今朝大柄な遊撃士の人と\x01",
            "すれ違ったらしくてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xE,
        "朝からずっとこの調子なんだよね。\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x11, 500)
    Sleep(300)

    #C0328
    ChrTalk(
        0xE,
        "あのジャネッタちゃん、仕事は……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x0, 0)
    SetScenarioFlags(0x0, 6)
    Jump("loc_675A")

    label("loc_66F2")


    #C0329
    ChrTalk(
        0xE,
        (
            "まあ確かに、遊撃士の人は\x01",
            "頼りになるよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xE,
        (
            "……勤務時間中にお喋りに来るのは\x01",
            "どうかと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_675A")

    Jump("loc_7258")

    label("loc_675F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_67C1")

    #C0331
    ChrTalk(
        0xE,
        (
            "いらっしゃい。\x01",
            "何か見ていくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xE,
        (
            "今月の新刊なら\x01",
            "ばっちり入荷しているよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7258")

    label("loc_67C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_682E")

    #C0333
    ChrTalk(
        0xE,
        (
            "ジャネッタちゃんは……３歩歩けば\x01",
            "大抵の事は忘れるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xE,
        "ある意味才能だと思うよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7258")

    label("loc_682E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6966")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68F3")

    #C0335
    ChrTalk(
        0xE,
        (
            "アルカンシェルの\x01",
            "新作公演が発表になったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xE,
        "演目は『金の太陽、銀の月』……\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xE,
        (
            "うちでもチケットを販売したけど\x01",
            "即日完売しちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xE,
        "さすがの大人気だね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6961")

    label("loc_68F3")


    #C0339
    ChrTalk(
        0xE,
        (
            "ジャネッタちゃんには悪いけど\x01",
            "我慢してもらうしかないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xE,
        (
            "ほんと言うと\x01",
            "僕もすごーく欲しかった位だし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6961")

    Jump("loc_7258")

    label("loc_6966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6BC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6ACC")

    #C0341
    ChrTalk(
        0xE,
        (
            "最近大企業向けに\x01",
            "導力ネットとかいうのが\x01",
            "整備されてるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xE,
        (
            "ときどき解説本は無いかって\x01",
            "真剣に相談される事があるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x103,
        (
            "#0200F導力ネットは\x01",
            "まだ研究段階の技術ですから。\x01",
            "論文くらいしか存在しないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xE,
        "や、やっぱりそうだよね。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xE,
        (
            "困ってるお客さんには悪いけど、\x01",
            "いくら何でも発刊してない本は\x01",
            "仕入れられないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6BBF")

    label("loc_6ACC")


    #C0346
    ChrTalk(
        0xE,
        (
            "相談に来る人は、\x01",
            "身なりのいいビジネスマンとか\x01",
            "市役所の人みたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xE,
        (
            "『便利らしいがサッパリ判らん！』\x01",
            "って口々に言っているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#0000Fはは……支援課#6Rウ  チ#でも\x01",
            "使いこなせてるのは\x01",
            "ティオだけだもんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x104,
        "#0300Fだよなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_6BBF")

    Jump("loc_7258")

    label("loc_6BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6D14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CAA")

    #C0350
    ChrTalk(
        0xE,
        (
            "うーん、やっぱり\x01",
            "書籍の売れ行きが一番だなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xE,
        (
            "うちは雑貨コーナーといっても\x01",
            "薬や日用品より\x01",
            "本を買いに来る人が多いんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xE,
        (
            "新刊の注文も多いし……\x01",
            "もう少し書籍のスペースを\x01",
            "増やしたい所だね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6D0F")

    label("loc_6CAA")


    #C0353
    ChrTalk(
        0xE,
        (
            "ここは雑貨コーナーだけど\x01",
            "本を買いに来る人が多いんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xE,
        "一度支配人に相談してみようかな。\x02",
    )

    CloseMessageWindow()

    label("loc_6D0F")

    Jump("loc_7258")

    label("loc_6D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_700C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FA6")
    TurnDirection(0xE, 0x104, 0)

    #C0355
    ChrTalk(
        0xE,
        (
            "やあ、最近よくグラビア雑誌を\x01",
            "買いに来る人じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xE,
        (
            "いや、君も好きだよね。\x01",
            "毎週の欠かさず品揃えをチェックしに来るんだものな。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x104,
        (
            "#0300Fへへ、あたぼうよ。\x01",
            "それが俺のライフワークだからな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x102)
    OP_64(0x103)

    #C0358
    ChrTalk(
        0x102,
        "#0111Fグラビア雑誌ねえ……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#0006Fランディ、女性陣の前で\x01",
            "そういうのはちょっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x104,
        (
            "#0305Fん……なんだロイド、\x01",
            "お前も見たかったのか？\x02\x03",

            "#0300Fはっはー、遠慮すんなって。\x01",
            "後で回してやるからよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0361
    ChrTalk(
        0x101,
        (
            "#0011Fいやいや、そうじゃないから！\x01",
            "誤解を招くような事を\x01",
            "言わないでくれよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x103,
        "#0211Fじー……\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xE,
        (
            "あ、あはは……\x01",
            "まずい話題を振っちゃったかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 6)
    Jump("loc_7007")

    label("loc_6FA6")


    #C0364
    ChrTalk(
        0xE,
        (
            "そういえば、うちの百貨店って\x01",
            "忘れ物をする人が多いんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xE,
        "君たちも気を付けてくれよ。\x02",
    )

    CloseMessageWindow()

    label("loc_7007")

    Jump("loc_7258")

    label("loc_700C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_716F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70E2")

    #C0366
    ChrTalk(
        0xE,
        (
            "数年前、クロスベルタイムズのビルが\x01",
            "中央広場にあったことは知ってるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xE,
        (
            "この百貨店の名前《タイムズ》は、\x01",
            "その頃の中央広場が“タイムズ広場”なんて\x01",
            "呼ばれてたことに由来するのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_716A")

    label("loc_70E2")


    #C0368
    ChrTalk(
        0xE,
        (
            "この百貨店の名前《タイムズ》は、\x01",
            "クロスベルタイムズが\x01",
            "中央広場にあったことに由来してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xE,
        "いや～、さすが影響力があるよね。\x02",
    )

    CloseMessageWindow()

    label("loc_716A")

    Jump("loc_7258")

    label("loc_716F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7258")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71F4")

    #C0370
    ChrTalk(
        0xE,
        (
            "やあいらっしゃい。\x01",
            "こっちは雑貨コーナーだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xE,
        (
            "クロスベルタイムズも\x01",
            "扱っているから、ぜひどうぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7258")

    label("loc_71F4")


    #C0372
    ChrTalk(
        0xE,
        (
            "一番の売れ筋は\x01",
            "やっぱりクロスベルタイムズだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xE,
        (
            "クロスベルには\x01",
            "商売に携わる人が多いしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7258")

    Jump("loc_61B5")

    label("loc_725D")

    TalkEnd(0xE)
    Return()

    # Function_17_616C end

    def Function_18_7261(): pass

    label("Function_18_7261")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_737B")

    #C0374
    ChrTalk(
        0x104,
        "#0300Fあ、課長じゃねえか。\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        (
            "#0000Fあの課長、仕事の方は……？\x02\x03",

            "上層部や捜査一課を\x01",
            "誤魔化しておく方法とか……\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xF,
        (
            "#1000Fああ、心配すんな。\x01",
            "頭ン中でばっちり考えてるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x102,
        "#0100Fそ、そうなんですか……？\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x103,
        (
            "#0200Fあまり説得力が\x01",
            "無さそうですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_73FC")

    label("loc_737B")


    #C0379
    ChrTalk(
        0xF,
        (
            "#1003F捜査の方はお前らの判断だ。\x01",
            "好きにやればいい。\x02\x03",

            "#1000Fただしロイド、後で報告しろよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        "#0000Fはい、分かっています。\x02",
    )

    CloseMessageWindow()

    label("loc_73FC")

    TalkEnd(0xFE)
    Return()

    # Function_18_7261 end

    def Function_19_7400(): pass

    label("Function_19_7400")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7892")

    #C0381
    ChrTalk(
        0x10,
        (
            "いらしゃいませ。\x01",
            "百貨店《タイムズ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74A0")

    #C0382
    ChrTalk(
        0x10,
        (
            "おや……これはこれは\x01",
            "エリィお嬢様でしたか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74E7")

    label("loc_74A0")

    TurnDirection(0x10, 0x102, 500)

    #C0383
    ChrTalk(
        0x10,
        "おや、そちらの方は……\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x10,
        "やはり、エリィお嬢様でしたか。\x02",
    )

    CloseMessageWindow()

    label("loc_74E7")


    #C0385
    ChrTalk(
        0x10,
        (
            "本日はご来店、\x01",
            "誠にありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7536")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_7536")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7556")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_7556")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7576")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_7576")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7596")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_7596")

    Sleep(1000)

    #C0386
    ChrTalk(
        0x101,
        "#0005Fエ、エリィお嬢様……？\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        (
            "#0100Fあ、あはははは……\x02\x03",

            "そのう、私の祖父が\x01",
            "支配人と知り合いなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x10,
        (
            "エリィお嬢様は\x01",
            "幼少の頃から当店の大切な\x01",
            "お得意様なのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x103,
        (
            "#0200Fこんな立派な百貨店で\x01",
            "ＶＩＰ扱いですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x104,
        (
            "#0305Fはー、やっぱり\x01",
            "“お嬢”だったんだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x102,
        "#0112Fもう、みんなして……\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x10,
        "……そういえば、お嬢様。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x10,
        (
            "留学先から戻られてから\x01",
            "警察への就職を希望なさったと\x01",
            "お聞きしましたが……？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x102,
        (
            "#0100Fええ、今は一警察官という身分になるわね。\x02\x03",

            "#0108Fだから……できれば店内でも\x01",
            "特別扱いは控えてもらえるかしら。\x02\x03",

            "#0106Fごめんなさいね、\x01",
            "我が侭ばかり言って。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x10,
        (
            "おっと、これは失礼致しました。\x01",
            "ではそのように……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x10,
        (
            "しかし、大切なお客様であることに\x01",
            "変わりはありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x10,
        (
            "困った事があれば\x01",
            "何なりとお申し付けくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 2)
    TalkEnd(0xFE)
    Return()

    label("loc_7892")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_790F")

    #C0398
    ChrTalk(
        0x101,
        (
            "#0000F（百貨店……\x01",
            "  落し物をしたトロントさんが\x01",
            "  立ち寄っていた場所だな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)

    label("loc_790F")


    #C0399
    ChrTalk(
        0x101,
        (
            "#0000Fすみません、この辺りで\x01",
            "落し物を見かけませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "遺失物の\x01",
            "お問い合わせでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "それでしたら中央の\x01",
            "総合インフォメーションへどうぞ。\x01",
            "すぐに照会させて頂きますので。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_79D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_7A5F")

    #C0402
    ChrTalk(
        0xFE,
        (
            "どうやらお探しの物は\x01",
            "見つかったようですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        "何よりでございます。\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "また百貨店タイムズを\x01",
            "ご利用くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_7A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7B64")

    #C0405
    ChrTalk(
        0xFE,
        (
            "近頃は売り上げも安定し、\x01",
            "どこか落ち着いてきている気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "……ですが百貨店であるからには、\x01",
            "常日頃からお客様の心をくすぐる\x01",
            "企画を提供し続けなければなりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        (
            "今、進行中のプランは\x01",
            "なかなかの自信作なのですよ。\x01",
            "今後をお楽しみに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C2C")

    label("loc_7B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7C2F")

    #C0408
    ChrTalk(
        0xFE,
        (
            "お客様の満足・安心が\x01",
            "当百貨店《タイムズ》のモットーです。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "職員一同、私が経験から培った\x01",
            "徹底的な教育をなされております。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "どうか気持ちのよいお買い物を\x01",
            "していってくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C2C")

    label("loc_7C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7CCF")

    #C0411
    ChrTalk(
        0xFE,
        (
            "今朝起きたら、ふとした事がきっかけで\x01",
            "新しいイベントの企画を思いつきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "いやはや、企画のタネとは\x01",
            "どこにでも転がっているものですな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C2C")

    label("loc_7CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7FF1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D93")

    #C0413
    ChrTalk(
        0xFE,
        (
            "いらしゃいませ。\x01",
            "百貨店《タイムズ》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        (
            "なにか商品を見繕う際は\x01",
            "お気軽に店員にお問い合わせ下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "懇切丁寧にご案内させて\x01",
            "いただきますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FEC")

    label("loc_7D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F35")

    #C0416
    ChrTalk(
        0xFE,
        (
            "先日、マクダエル市長から\x01",
            "労いの言葉を頂いたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "地域に根付いた老舗百貨店として、\x01",
            "今後とも市民に近しい存在で\x01",
            "あって欲しい、とのことでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x102,
        (
            "#0100F大企業であることを鼻にかけず、\x01",
            "常にお客の事を考えている\x01",
            "ネストンさんですもの。\x02\x03",

            "私も祖父と同じ気持ちです。\x01",
            "これからも頑張ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        (
            "勿体無いお言葉です、\x01",
            "エリィお嬢様……\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "是非ともご期待に添える\x01",
            "百貨店でありたいと思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7FEC")

    label("loc_7F35")


    #C0421
    ChrTalk(
        0xFE,
        (
            "マクダエル市長とは\x01",
            "以前から親交はありましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "改めてあのような言葉をいただけると\x01",
            "身も引き締まるというものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        (
            "今後ともご期待に添える\x01",
            "百貨店でありたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FEC")

    Jump("loc_8C2C")

    label("loc_7FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_81C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_812A")

    #C0424
    ChrTalk(
        0xFE,
        (
            "私もこの業界に入って\x01",
            "随分と経ちます。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "日々、この百貨店を盛り上げる\x01",
            "よい企画がないか思案していますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        (
            "若い頃のほんの少しの経験が、\x01",
            "未だにプランニングに\x01",
            "生きてくることも多いのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        (
            "がむしゃらに色々なものに\x01",
            "手を出していたあの時代は、\x01",
            "私にとっては宝物のようですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_81BF")

    label("loc_812A")


    #C0428
    ChrTalk(
        0xFE,
        (
            "若い頃のほんの少しの経験が、\x01",
            "未だにプランニングに\x01",
            "生きてくることも多いのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        (
            "若い頃、色々な経験をしておいて\x01",
            "本当によかったと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81BF")

    Jump("loc_8C2C")

    label("loc_81C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_83D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8358")

    #C0430
    ChrTalk(
        0xFE,
        (
            "ミシュラムの由緒正しいマスコット、\x01",
            "《みっしぃ》をご存知でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        (
            "元々保養地だったミシュラムで\x01",
            "売り出されたご当地キャラクターですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        (
            "２年前にテーマパークが併設され、\x01",
            "一躍人気を博すこととなったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "当百貨店でも\x01",
            "コラボレーション・イベントなどを\x01",
            "企画しているのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x103,
        "#0205F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x101,
        "#0000F（ティオの目が輝いている……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_83D4")

    label("loc_8358")


    #C0436
    ChrTalk(
        0xFE,
        (
            "我が百貨店は《みっしぃ》との\x01",
            "コラボイベントを企画しているのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "開催しましたらば\x01",
            "是非ともお越しくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83D4")

    Jump("loc_8C2C")

    label("loc_83D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_849C")

    #C0438
    ChrTalk(
        0xFE,
        (
            "百貨店の新しいイベントの企画を\x01",
            "着々と進めています。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        (
            "後はスポンサーの方に\x01",
            "連絡差し上げ、了解を頂くのみ……\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "お客様、今後の百貨店の動向から\x01",
            "どうか目を離されませんよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C2C")

    label("loc_849C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_8501")

    #C0441
    ChrTalk(
        0xFE,
        "当店は８時まで開いております。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "どうぞごゆっくり買い物を\x01",
            "お楽しみ下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C2C")

    label("loc_8501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_85C5")

    #C0443
    ChrTalk(
        0xFE,
        (
            "我が百貨店の出店店舗は、\x01",
            "私がクロスベルと周辺諸国を回り\x01",
            "見出した優良店ばかりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "日々、買い物に来られる\x01",
            "お客様の笑顔を見るたびに、\x01",
            "私の目に狂いはなかったと思うのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C2C")

    label("loc_85C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_867A")

    #C0445
    ChrTalk(
        0xFE,
        "百貨店《タイムズ》へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "何かご入用でしたら\x01",
            "正面インフォメーションで\x01",
            "係の者が承らせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        (
            "どうぞごゆるりと\x01",
            "買い物をお楽しみ下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C2C")

    label("loc_867A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_86D1")

    #C0448
    ChrTalk(
        0xFE,
        "……いらっしゃいませ。\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        (
            "どうかごゆっくり\x01",
            "お楽しみくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C2C")

    label("loc_86D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_87CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8779")

    #C0450
    ChrTalk(
        0xFE,
        (
            "ふむ、新装開店フェアからも\x01",
            "日にちが開きましたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        (
            "そろそろお客様も\x01",
            "退屈なさっている頃……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        (
            "何か良い企画が\x01",
            "あれば良いのですが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_87C7")

    label("loc_8779")


    #C0453
    ChrTalk(
        0xFE,
        (
            "新装開店フェアからも\x01",
            "日にちが開きました。\x01",
            "何か妙案はないものでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87C7")

    Jump("loc_8C2C")

    label("loc_87CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_89A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8930")

    #C0454
    ChrTalk(
        0x102,
        (
            "#0100Fネストンさん、\x01",
            "お早うございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xFE,
        "これは皆様、お早うございます。\x02",
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xFE,
        (
            "おや……どちらかに\x01",
            "お出掛けのようですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x102,
        (
            "#0100Fええ……\x01",
            "よくお分かりになりましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xFE,
        "はは、客商売が長いものですから。\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xFE,
        (
            "皆様、出先で持ち物が足りないと\x01",
            "つい焦ってしまうものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xFE,
        (
            "どうぞお忘れ物のないよう\x01",
            "お仕度くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 7)
    Jump("loc_899C")

    label("loc_8930")


    #C0461
    ChrTalk(
        0xFE,
        (
            "皆様、どうかお忘れ物の\x01",
            "ないようお仕度くださいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        (
            "そしてお気をつけて\x01",
            "行ってらっしゃいますよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_899C")

    Jump("loc_8C2C")

    label("loc_89A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8AF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A82")

    #C0463
    ChrTalk(
        0xFE,
        (
            "ご存知かと思いますが、昨年\x01",
            "当百貨店は全面改装を行いました。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xFE,
        (
            "この数年で街並みも\x01",
            "随分と様変わり致しましたので、\x01",
            "それに倣いましてございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        (
            "ますますご利用の程\x01",
            "よろしくお願い致します。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8AEC")

    label("loc_8A82")


    #C0466
    ChrTalk(
        0xFE,
        (
            "街並みに倣いまして、\x01",
            "当百貨店も全面改装致しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "ますますご利用の程\x01",
            "よろしくお願い致します。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AEC")

    Jump("loc_8C2C")

    label("loc_8AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8C2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BAD")

    #C0468
    ChrTalk(
        0xFE,
        (
            "当百貨店には\x01",
            "様々な売り場を用意しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xFE,
        (
            "いずれも品質・品揃えともに\x01",
            "申し分のない店舗ばかり……\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xFE,
        (
            "皆様、どうぞごゆっくり\x01",
            "お楽しみくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8C2C")

    label("loc_8BAD")


    #C0471
    ChrTalk(
        0xFE,
        (
            "当百貨店の売り場は、\x01",
            "品質・品揃えともに最高のものと\x01",
            "自負しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xFE,
        (
            "皆様、どうぞごゆっくり\x01",
            "お楽しみくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C2C")

    TalkEnd(0xFE)
    Return()

    # Function_19_7400 end

    def Function_20_8C30(): pass

    label("Function_20_8C30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8CAD")

    #C0473
    ChrTalk(
        0xFE,
        (
            "最近夕方になると\x01",
            "勤務中なのにここにきちゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xFE,
        (
            "うー、いい匂い……\x01",
            "おなか減っちゃったなぁ～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A32")

    label("loc_8CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8DBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D60")
    OP_93(0xFE, 0x0, 0x0)

    #C0475
    ChrTalk(
        0xFE,
        "お掃除、お掃除……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0476
    ChrTalk(
        0xFE,
        (
            "はあ、昨日寝坊した罰に\x01",
            "大掃除を言いつけられたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xFE,
        (
            "このあと倉庫のお掃除もあって\x01",
            "はあ、大変ですよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8DBA")

    label("loc_8D60")


    #C0478
    ChrTalk(
        0xFE,
        (
            "あれは目覚ましが\x01",
            "止まってただけなのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xFE,
        (
            "はあ、誰か\x01",
            "代わってくれないかなぁ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DBA")

    Jump("loc_9A32")

    label("loc_8DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8EA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E79")

    #C0480
    ChrTalk(
        0xFE,
        (
            "ふぁ～ああ、今日は\x01",
            "寝坊しちゃったんですよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xFE,
        (
            "あ、でもわたしの\x01",
            "せいじゃないんですよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xFE,
        (
            "目覚まし時計がいつの間にか\x01",
            "止まっちゃってただけですもん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8EA4")

    label("loc_8E79")


    #C0483
    ChrTalk(
        0xFE,
        (
            "ふぁ～ああ、\x01",
            "何だかまだ眠いですよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EA4")

    Jump("loc_9A32")

    label("loc_8EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_900F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F2C")

    #C0484
    ChrTalk(
        0xFE,
        (
            "商品は自由に\x01",
            "見ていってくださいね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xFE,
        (
            "ウチはウィンドウショッピング\x01",
            "大歓迎ですからっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_900A")

    label("loc_8F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FD5")

    #C0486
    ChrTalk(
        0xFE,
        "ささっ……お仕事は素早く！\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0xFE,
        (
            "わたし、最近\x01",
            "とっても頑張ってるんですよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xFE,
        (
            "これもシンシア先輩や\x01",
            "パール先輩に追いつくため。\x01",
            "ファイト、おー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_900A")

    label("loc_8FD5")


    #C0489
    ChrTalk(
        0xFE,
        (
            "ファイト、おー！\x01",
            "わたし、今日も頑張りますよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_900A")

    Jump("loc_9A32")

    label("loc_900F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_90A7")

    #C0490
    ChrTalk(
        0xFE,
        (
            "記念祭が終わって\x01",
            "おヒマになっちゃいましたねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xFE,
        (
            "でもわたし、\x01",
            "おヒマなのは大好きですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xFE,
        "のんびりしてていいですもんね～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A32")

    label("loc_90A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_912F")

    #C0493
    ChrTalk(
        0xFE,
        (
            "わたしって、記念祭が近づくと\x01",
            "うきうきしちゃうんですよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        (
            "うふふ、楽しみだな～。\x01",
            "今年は何をして遊ぼうかなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A32")

    label("loc_912F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9264")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9203")

    #C0495
    ChrTalk(
        0xFE,
        (
            "遊撃士のヒトって\x01",
            "かっこいいですよねー……\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xFE,
        (
            "この前も百貨店に\x01",
            "迷子の子供を引き取りに\x01",
            "来てくれたんですよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xFE,
        (
            "あの、わたしも\x01",
            "連れてってくれませんか？\x01",
            "……な、なーんちゃって。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_925F")

    label("loc_9203")


    #C0498
    ChrTalk(
        0xFE,
        (
            "遊撃士のヒトって\x01",
            "かっこいいですよねー……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xFE,
        (
            "わたしも今度\x01",
            "迷子になってみようかなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_925F")

    Jump("loc_9A32")

    label("loc_9264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_92C1")

    #C0500
    ChrTalk(
        0xFE,
        "はあ、お腹減っちゃったなー。\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xFE,
        (
            "今日は早く帰って\x01",
            "ゴハン食べたいですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A32")

    label("loc_92C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_935B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_931B")
    OP_93(0xFE, 0x5A, 0x0)

    #C0502
    ChrTalk(
        0xFE,
        "あ、このお洋服いいなー。\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xFE,
        "わたしも欲しいなー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9356")

    label("loc_931B")


    #C0504
    ChrTalk(
        0xFE,
        (
            "これ、今年の新作ですよねー。\x01",
            "わたしも欲しいですよー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9356")

    Jump("loc_9A32")

    label("loc_935B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9628")
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_958D")

    #C0505
    ChrTalk(
        0xFE,
        "う～、聞いてくださいよ～！\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xFE,
        (
            "アルカンシェルのチケット、\x01",
            "確保しておいてくださいって\x01",
            "サザークさんに頼んでたのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xFE,
        "全部売っちゃったって言うんです！\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xFE,
        (
            "ううっ、百貨店勤めなら\x01",
            "手に入ると思ったのにぃ～……\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xE,
        (
            "はは……悪いけど\x01",
            "チケット販売にも規則があるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xE,
        (
            "僕だって自分の分は\x01",
            "買えなかったんだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xE,
        (
            "ジャネッタちゃん、機嫌直してよ。\x01",
            "今度埋め合わせするからさぁ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xE, 500)
    Sleep(300)

    #C0512
    ChrTalk(
        0xFE,
        (
            "……ほんとですか？\x01",
            "じゃあ今度デートしてください。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0513
    ChrTalk(
        0xE,
        (
            "べ、別にいいけど……\x01",
            "本当にそんなのでいいの？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_961F")

    label("loc_958D")

    OP_93(0xFE, 0x2D, 0x0)

    #C0514
    ChrTalk(
        0xFE,
        (
            "ぐすん、チケット\x01",
            "絶対欲しかったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xFE,
        (
            "サザークさんのバカー！\x01",
            "今度デートしてください！\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xE,
        (
            "ジャネッタちゃん、\x01",
            "やけくそだね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_961F")

    OP_4C(0xE, 0xFF)
    Jump("loc_9A32")

    label("loc_9628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9724")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96F0")

    #C0517
    ChrTalk(
        0xFE,
        (
            "シンシア先輩とパール先輩って\x01",
            "いつも息ピッタリなんですよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xFE,
        (
            "お互い何も言わないのに\x01",
            "考えてる事が分かるみたいな……\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        (
            "はあ、２人とも\x01",
            "ベテランだからなのかな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_971F")

    label("loc_96F0")


    #C0520
    ChrTalk(
        0xFE,
        (
            "わたしも早く\x01",
            "お２人みたいになりたいな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_971F")

    Jump("loc_9A32")

    label("loc_9724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9806")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97C4")

    #C0521
    ChrTalk(
        0xFE,
        (
            "ここのコーナーの担当さん、\x01",
            "いつも休み時間に\x01",
            "お皿を拭いてるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "それもニコニコしながら。\x01",
            "……ヘンな人だと思いません？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9801")

    label("loc_97C4")


    #C0523
    ChrTalk(
        0xFE,
        (
            "ここのコーナーの担当さん、\x01",
            "ちょっとヘンな人ですよねー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9801")

    Jump("loc_9A32")

    label("loc_9806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_98D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98AF")

    #C0524
    ChrTalk(
        0xFE,
        (
            "この前、遊撃士の\x01",
            "お客さんを案内したんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        (
            "青年と若い娘さんで、\x01",
            "何だかカップルみたいな雰囲気でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xFE,
        "はあ、羨ましいなぁ～……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_98D1")

    label("loc_98AF")


    #C0527
    ChrTalk(
        0xFE,
        "わたしも彼氏欲しいですよ～。\x02",
    )

    CloseMessageWindow()

    label("loc_98D1")

    Jump("loc_9A32")

    label("loc_98D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_9950")

    #C0528
    ChrTalk(
        0xFE,
        (
            "シンシア先輩は素敵だし、\x01",
            "パール先輩は美人だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xFE,
        (
            "はあ、わたしも早く\x01",
            "お２人みたいになりたいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A32")

    label("loc_9950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99DF")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x104, 500)

    #C0530
    ChrTalk(
        0xFE,
        "あ、かっこいい人……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0531
    ChrTalk(
        0xFE,
        (
            "あ、いえ、何でもないんです。\x01",
            "どうぞごゆっくり～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9A32")

    label("loc_99DF")


    #C0532
    ChrTalk(
        0xFE,
        (
            "わ、わたしはここの販売を\x01",
            "手伝っているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xFE,
        "ど、どうぞごゆっくり～。\x02",
    )

    CloseMessageWindow()

    label("loc_9A32")

    TalkEnd(0xFE)
    Return()

    # Function_20_8C30 end

    def Function_21_9A36(): pass

    label("Function_21_9A36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9AA5")

    #C0534
    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xFE,
        (
            "……おーっと危ない！\x01",
            "買う本を立ち読みで読破しちまう\x01",
            "ところだった！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5EB")

    label("loc_9AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9BDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B67")

    #C0536
    ChrTalk(
        0xFE,
        "お、あったあった……\x02",
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xFE,
        (
            "お高い参考書だけど、\x01",
            "親に頼んだらミラを出してくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xFE,
        (
            "浪人生だから\x01",
            "肩身が狭い気がしてたけど、\x01",
            "ちゃんと応援してくれてんだなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_9BD5")

    label("loc_9B67")


    #C0539
    ChrTalk(
        0xFE,
        (
            "よーし、この参考書を読んで、\x01",
            "リッパな医者になれたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xFE,
        (
            "まずは親に本の代金を\x01",
            "返さなきゃな、ははっ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BD5")

    Jump("loc_A5EB")

    label("loc_9BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9C9D")

    #C0541
    ChrTalk(
        0xFE,
        (
            "今日も親の言いつけで\x01",
            "家の買い物に来たけど……\x01",
            "どうしても雑貨屋がきになるなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xFE,
        (
            "昨日見つけた参考書、\x01",
            "どうしても欲しいんだよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xFE,
        "ダメ元で親にねだってみようかなぁ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A5EB")

    label("loc_9C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9DE8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D19")

    #C0544
    ChrTalk(
        0xFE,
        (
            "俺はいっつも親の言いつけで\x01",
            "買い物に来てるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xFE,
        "浪人生は肩身が狭いんだよな～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9DE3")

    label("loc_9D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D82")

    #C0546
    ChrTalk(
        0xFE,
        "おっ、新しい参考書が出てら。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xFE,
        (
            "なになに……\x01",
            "おお、よさそうな参考書じゃないか！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_9DE3")

    label("loc_9D82")


    #C0548
    ChrTalk(
        0xFE,
        "……うー、欲しいなこの参考書……\x02",
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xFE,
        (
            "だが、浪人生のこの俺に\x01",
            "この値段は余りにも高いッ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DE3")

    Jump("loc_A5EB")

    label("loc_9DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9F14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9ED6")

    #C0550
    ChrTalk(
        0xFE,
        "さーて、今日頼まれてるのはと……\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x153,
        (
            "#1110Fおにーちゃん、お使い？\x01",
            "えらいねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xFE,
        (
            "……おにーちゃんは浪人生だからね。\x01",
            "お使いでもしなきゃ肩身が狭いんだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xFE,
        (
            "……自分で言ってて\x01",
            "悲しくなってきたな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_9F0F")

    label("loc_9ED6")


    #C0554
    ChrTalk(
        0xFE,
        (
            "浪人生だからお使いでもしなきゃ\x01",
            "肩身が狭いんだよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F0F")

    Jump("loc_A5EB")

    label("loc_9F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9F5D")

    #C0555
    ChrTalk(
        0xFE,
        (
            "んー、今日は真新しい参考書は\x01",
            "置いてないみたいだなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5EB")

    label("loc_9F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A055")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FF3")

    #C0556
    ChrTalk(
        0xFE,
        (
            "俺、医者になろうと思って\x01",
            "ウルスラ病院の試験を\x01",
            "何度も受けてるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xFE,
        (
            "……相当難しいから\x01",
            "未だ浪人の身分だけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A050")

    label("loc_9FF3")


    #C0558
    ChrTalk(
        0xFE,
        "はぁ、浪人はつらいよ。\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xFE,
        (
            "家族に頭があがらないから\x01",
            "こういうパシリにも使われ放題だし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A050")

    Jump("loc_A5EB")

    label("loc_A055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_A179")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A108")

    #C0560
    ChrTalk(
        0xFE,
        (
            "シロン姉ちゃん、\x01",
            "看護師としてウルスラ病院で\x01",
            "働いてるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xFE,
        (
            "どうしてあのおっちょこちょいが\x01",
            "あんな立派な病院に\x01",
            "就けたのか未だに疑問だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A174")

    label("loc_A108")


    #C0562
    ChrTalk(
        0xFE,
        (
            "……まぁ、シロン姉ちゃんは\x01",
            "昔から悪運が強いからなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xFE,
        (
            "……っと、そんな事より\x01",
            "買い物買い物っと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A174")

    Jump("loc_A5EB")

    label("loc_A179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A24A")

    #C0564
    ChrTalk(
        0xFE,
        (
            "ウチの親はさ、\x01",
            "子供に買い物任せるくせに\x01",
            "駄賃を１ミラもくれねぇんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xFE,
        (
            "ピッタリ買ってくるものの分しか\x01",
            "ミラを渡してくれないから\x01",
            "おつりも出ないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        (
            "計算高い親ってのは\x01",
            "やなもんだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5EB")

    label("loc_A24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A28B")

    #C0567
    ChrTalk(
        0xFE,
        (
            "お、新刊が入ってる。\x01",
            "チェックチェック～っと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5EB")

    label("loc_A28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A3DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A354")

    #C0568
    ChrTalk(
        0xFE,
        (
            "俺の姉ちゃん、看護師として\x01",
            "ウルスラ病院で働いてるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xFE,
        (
            "シロンっていうんだけど\x01",
            "見かけたことある？\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xFE,
        (
            "これから家族命令で\x01",
            "会いに行ってきます。\x01",
            "……面倒臭いけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A3D9")

    label("loc_A354")


    #C0571
    ChrTalk(
        0xFE,
        (
            "俺の姉ちゃん、\x01",
            "ウルスラ病院で働いてるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        (
            "シロン姉ちゃんは\x01",
            "おっちょこちょいだからな……\x01",
            "家族全員の心配のタネなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3D9")

    Jump("loc_A5EB")

    label("loc_A3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A46C")

    #C0573
    ChrTalk(
        0xFE,
        "また買い物を頼まれちゃってさー。\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xFE,
        (
            "ほんとは宿題のレポートで使う\x01",
            "資料本を探しに来たのに……\x01",
            "ウチの家族は人使いが荒いぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5EB")

    label("loc_A46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A500")

    #C0575
    ChrTalk(
        0xFE,
        (
            "百貨店って何でも揃うからさ、\x01",
            "ついつい立ち寄っちゃうんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xFE,
        (
            "去年に新装オープンしてから\x01",
            "客入りもますます増えたらしいぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5EB")

    label("loc_A500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A5EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5A8")

    #C0577
    ChrTalk(
        0xFE,
        (
            "砂糖に小麦粉、\x01",
            "オニオンソースっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xFE,
        (
            "ほんとにこの店は\x01",
            "品揃えがいいよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0xFE,
        (
            "砂糖だけでも、産地別に\x01",
            "３６種類も扱ってるんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A5EB")

    label("loc_A5A8")


    #C0580
    ChrTalk(
        0xFE,
        (
            "でも料理人ならともかく……\x01",
            "どれを買ったらいいか分かんないぞ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5EB")

    TalkEnd(0xFE)
    Return()

    # Function_21_9A36 end

    def Function_22_A5EF(): pass

    label("Function_22_A5EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A65F")

    #C0581
    ChrTalk(
        0xFE,
        "あらやだ、すっかり夕方ねぇ。\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        (
            "夕飯のレシピ、まだ全然決めてないわ。\x01",
            "どうしよっかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_A65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A6AE")

    #C0583
    ChrTalk(
        0xFE,
        (
            "今日も開店時間から並んでいたの。\x01",
            "朝の買い物は清々しいわ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_A6AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A705")

    #C0584
    ChrTalk(
        0xFE,
        "おほほ、買い物三昧よ～！\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xFE,
        (
            "今日は好きなだけ\x01",
            "買い物してやるわ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_A705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A7E4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A786")

    #C0586
    ChrTalk(
        0xFE,
        (
            "百貨店って歩いているだけでも\x01",
            "楽しいのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xFE,
        (
            "何時間だって\x01",
            "こうしていられちゃうっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7DF")

    label("loc_A786")


    #C0588
    ChrTalk(
        0xFE,
        "おほほ、明日は旦那の給料日なの。\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xFE,
        (
            "今から下見して\x01",
            "好きなだけ買い物してやるわ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7DF")

    Jump("loc_AD0F")

    label("loc_A7E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A82A")

    #C0590
    ChrTalk(
        0xFE,
        "うろうろうろうろ～。\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xFE,
        "……はぁ、全然飽きない！\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_A82A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A871")

    #C0592
    ChrTalk(
        0xFE,
        (
            "あなたもウィンドウショッピングを\x01",
            "楽しみましょうよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_A871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A8C0")

    #C0593
    ChrTalk(
        0xFE,
        (
            "今日も開店時間から並んでいたの。\x01",
            "朝の買い物は清々しいわ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_A8C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_A934")

    #C0594
    ChrTalk(
        0xFE,
        (
            "まぁ……\x01",
            "もうこんな時間になっていたのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xFE,
        (
            "久しぶりに閉店時間ギリギリまで\x01",
            "遊んでしまったわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_A934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_A971")

    #C0596
    ChrTalk(
        0xFE,
        (
            "ごめんなさいねぇ！\x01",
            "今、買い物で忙しいの！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_A971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A9FB")

    #C0597
    ChrTalk(
        0xFE,
        (
            "クロスベルには大陸中の\x01",
            "ブランドショップが集まってるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xFE,
        (
            "でも、私のへそくりで\x01",
            "買える値段じゃないのよね、はあ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_A9FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_AB50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAEA")

    #C0599
    ChrTalk(
        0xFE,
        (
            "待ちに待った\x01",
            "アルカンシェルの新作チケットが、\x01",
            "発売になるんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0xFE,
        (
            "はあ、私も欲しいけど\x01",
            "ちょっと高いのよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        (
            "それに確かこの前は\x01",
            "発売から１日で売り切れたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0xFE,
        "今回も争奪戦なんだろうな～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_AB4B")

    label("loc_AAEA")


    #C0603
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの新作公演は\x01",
            "ずっと楽しみにしていたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xFE,
        "……徹夜で並んだら買えるかしら。\x02",
    )

    CloseMessageWindow()

    label("loc_AB4B")

    Jump("loc_AD0F")

    label("loc_AB50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_ABD3")

    #C0605
    ChrTalk(
        0xFE,
        (
            "さて、お料理の食材は買ったし\x01",
            "プラダさんのトコの新商品は\x01",
            "チェックしたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xFE,
        (
            "えーっと、\x01",
            "それからそれから……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_ABD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_AC4B")

    #C0607
    ChrTalk(
        0xFE,
        (
            "ね、ね、洋服店の新商品は見た？\x01",
            "欲しいわよねー！\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0xFE,
        (
            "でも主人に言ったって\x01",
            "反対されるわよね、はあ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_AC4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_AC90")

    #C0609
    ChrTalk(
        0xFE,
        (
            "あら、ケンったらあんなところで\x01",
            "何してるのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_AC90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_AD0F")

    #C0610
    ChrTalk(
        0xFE,
        (
            "あらあら、あっちの店もこっちの店も\x01",
            "新商品がいっぱいよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0xFE,
        (
            "やっぱり百貨店は\x01",
            "ちょくちょくチェックしなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD0F")

    TalkEnd(0xFE)
    Return()

    # Function_22_A5EF end

    def Function_23_AD13(): pass

    label("Function_23_AD13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_AD7F")

    #C0612
    ChrTalk(
        0xFE,
        "はぁ……ママも相変わらずです。\x02",
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xFE,
        (
            "せめて何を買うか決めてから\x01",
            "家を出て欲しいですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_AD7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_ADDD")

    #C0614
    ChrTalk(
        0xFE,
        (
            "今日もママにつきあって\x01",
            "朝から百貨店です。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xFE,
        (
            "ふああ……\x01",
            "まだ眠いですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_ADDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_AE44")

    #C0616
    ChrTalk(
        0xFE,
        "今日はパパのお給料日なんです。\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        (
            "……つまり、ママの\x01",
            "歯止めが利かなくなる日です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_AE44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_AF67")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AED1")

    #C0618
    ChrTalk(
        0xFE,
        (
            "ママ……\x01",
            "百貨店に何度も来てるのに\x01",
            "買い物の量はそんなでもないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        "冷やかしの常連なんですよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF62")

    label("loc_AED1")


    #C0620
    ChrTalk(
        0xFE,
        (
            "うちのパパは、\x01",
            "ママにお財布の全権を\x01",
            "握られているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xFE,
        (
            "……ただ、あれで家計が破綻しないのは\x01",
            "ちゃんと考えられてるってことですよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF62")

    Jump("loc_B43B")

    label("loc_AF67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_AFC0")

    #C0622
    ChrTalk(
        0xFE,
        (
            "ママはいつも百貨店の中を歩き回って……\x01",
            "いい加減飽きないんでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_AFC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_B052")

    #C0623
    ChrTalk(
        0xFE,
        (
            "ママは買わずに満足できる\x01",
            "なかなか稀有な人種なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0xFE,
        (
            "それにつき合わされていると\x01",
            "すごく時間を無駄にした気持ちになります。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_B052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B0D1")

    #C0625
    ChrTalk(
        0xFE,
        (
            "朝からママの買い物に\x01",
            "付き合わされてるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xFE,
        (
            "……はあ。\x01",
            "今日は友達と遊びに行く\x01",
            "約束をしてたのになぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_B0D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_B167")

    #C0627
    ChrTalk(
        0xFE,
        (
            "パパもそろそろ家に帰る頃なのに、\x01",
            "夕飯もお風呂も準備できていません。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xFE,
        (
            "……パパはよく、\x01",
            "ママに愛想を尽かさずにいられますよね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_B167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_B1A4")

    #C0629
    ChrTalk(
        0xFE,
        (
            "すみません。\x01",
            "ママのお守りで忙しいんです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_B1A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B1F7")

    #C0630
    ChrTalk(
        0xFE,
        (
            "ママもいい歳なんだから、\x01",
            "ブランドブランド言わないでほしいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_B1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_B284")

    #C0631
    ChrTalk(
        0xFE,
        (
            "アルカンシェル……\x01",
            "僕も見に行きたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xFE,
        (
            "……ママのことだから、\x01",
            "当日も百貨店で買い物してて\x01",
            "公演を忘れそうですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_B284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B2F2")

    #C0633
    ChrTalk(
        0xFE,
        (
            "ママは午前中の半分を\x01",
            "買い物に費やします。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xFE,
        (
            "そして午後からも\x01",
            "買い物に出かけるんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_B2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B362")

    #C0635
    ChrTalk(
        0xFE,
        (
            "今日もママの\x01",
            "買い物に付き合ってるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xFE,
        (
            "一人でお留守番を\x01",
            "している方が楽なんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_B362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_B3CD")

    #C0637
    ChrTalk(
        0xFE,
        (
            "ママは買う気もないのに\x01",
            "お店の隅々まで見て回るんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0xFE,
        "……なんだか恥ずかしいです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B43B")

    label("loc_B3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_B43B")

    #C0639
    ChrTalk(
        0xFE,
        (
            "ママの買い物は長いんです。\x01",
            "とっても待たされちゃう……\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0xFE,
        "……でもいいんです、慣れてますから。\x02",
    )

    CloseMessageWindow()

    label("loc_B43B")

    TalkEnd(0xFE)
    Return()

    # Function_23_AD13 end

    def Function_24_B43F(): pass

    label("Function_24_B43F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B533")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4EF")

    #C0641
    ChrTalk(
        0xFE,
        (
            "思い余って、結局婆さんと\x01",
            "まったく同じブローチを買ってしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0xFE,
        (
            "婆さんには笑われるかもしれんが……\x01",
            "そんな顔をされるのもまた一興じゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_B52E")

    label("loc_B4EF")


    #C0643
    ChrTalk(
        0xFE,
        (
            "婆さんとおそろいのブローチというのも\x01",
            "悪くないじゃろうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B52E")

    Jump("loc_BFEE")

    label("loc_B533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B5A4")

    #C0644
    ChrTalk(
        0xFE,
        (
            "街でルバーチェの構成員を\x01",
            "見かけなくなってるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0xFE,
        "いないならいないで、不気味じゃな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BFEE")

    label("loc_B5A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B634")

    #C0646
    ChrTalk(
        0xFE,
        "ついにマフィアが事を起こしおったか。\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xFE,
        (
            "いくらルバーチェでも、\x01",
            "あれだけ大きくやってしまっては\x01",
            "さすがに言い逃れはできまい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFEE")

    label("loc_B634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B752")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6B8")

    #C0648
    ChrTalk(
        0xFE,
        (
            "昔は、結婚指輪と言ったら\x01",
            "給料の３ヶ月分がザラじゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xFE,
        "……若かりし頃を思い出すのう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B74D")

    label("loc_B6B8")


    #C0650
    ChrTalk(
        0xFE,
        (
            "婆さんにブローチを贈ったら、\x01",
            "自分用にもなにか欲しくなってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0xFE,
        (
            "足繁く通っていたら、\x01",
            "乙女のようでみっともないと\x01",
            "婆さんに笑われてしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B74D")

    Jump("loc_BFEE")

    label("loc_B752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_B81F")

    #C0652
    ChrTalk(
        0xFE,
        (
            "記念祭の最終日、市長の閉会の挨拶も\x01",
            "素晴らしいものじゃったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xFE,
        "おまえさんは、聞かなかったのか？\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0xFE,
        (
            "……まったく嘆かわしいわい。\x01",
            "クロスベルの未来を担う若者が\x01",
            "そんなことでどうする？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFEE")

    label("loc_B81F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_B860")

    #C0655
    ChrTalk(
        0xFE,
        (
            "ネックレスか……\x01",
            "婆さんにはちと若すぎるかの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFEE")

    label("loc_B860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B9CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B94D")

    #C0656
    ChrTalk(
        0xFE,
        (
            "大分前、脱税疑惑で\x01",
            "クロスベルタイムズに曝しあげられた\x01",
            "自治州議員がおったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xFE,
        (
            "突然の体調不良で入院したあと、\x01",
            "ぱったりと話題が止んでしまったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0xFE,
        (
            "また汚いやり口で\x01",
            "もみ消されたのじゃろうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_B9C9")

    label("loc_B94D")


    #C0659
    ChrTalk(
        0xFE,
        (
            "脱税疑惑が上がっておった議員……\x01",
            "確か名前は……\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0xFE,
        (
            "ゲ……ゲビル？　ゴバラ……？\x01",
            "う、うむ、確かそんな名前だったかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9C9")

    Jump("loc_BFEE")

    label("loc_B9CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_BA2C")

    #C0661
    ChrTalk(
        0xFE,
        (
            "うーむ、決まらんのう。\x01",
            "婆さんはどんな贈り物を\x01",
            "喜んでくれるのじゃろうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFEE")

    label("loc_BA2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_BA6F")

    #C0662
    ChrTalk(
        0xFE,
        (
            "ふむ……この帽子は\x01",
            "なかなか品があっていいのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFEE")

    label("loc_BA6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BBC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB3F")

    #C0663
    ChrTalk(
        0xFE,
        (
            "クロスベル警備隊は\x01",
            "ベルガード門に本司令部を\x01",
            "構えておるのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0xFE,
        (
            "最新の装備をそろえた\x01",
            "精鋭と聞くが……\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0xFE,
        (
            "活躍する機会には恵まれず、\x01",
            "地味な活動ばかり\x01",
            "しておるらしいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_BBBE")

    label("loc_BB3F")


    #C0666
    ChrTalk(
        0xFE,
        (
            "クロスベル警備隊は\x01",
            "最新の装備をそろえた精鋭と聞く。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0xFE,
        (
            "活躍する機会には恵まれず、\x01",
            "地味な活動ばかり\x01",
            "しておるらしいがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBBE")

    Jump("loc_BFEE")

    label("loc_BBC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_BC38")
    OP_93(0xFE, 0x5A, 0x0)

    #C0668
    ChrTalk(
        0xFE,
        (
            "むう、ここにあった指輪は\x01",
            "売れてしもうたのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0xFE,
        (
            "婆さんにぴったりじゃと\x01",
            "思うたがの……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFEE")

    label("loc_BC38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_BD3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCE7")

    #C0670
    ChrTalk(
        0xFE,
        (
            "噂で聞いたが、マインツで\x01",
            "魔獣被害があったそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0xFE,
        "ふむ、珍しい事もあるものじゃな。\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0xFE,
        (
            "魔獣避けの導力灯は\x01",
            "壊れておったんじゃろうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_BD35")

    label("loc_BCE7")


    #C0673
    ChrTalk(
        0xFE,
        (
            "今は昔とは違い魔獣避けの\x01",
            "導力灯が普及しておる。\x01",
            "魔獣被害など珍しいのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD35")

    Jump("loc_BFEE")

    label("loc_BD3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_BE2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDF8")

    #C0674
    ChrTalk(
        0xFE,
        (
            "今の自治州議会は\x01",
            "腑抜けどものあつまりじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0xFE,
        (
            "派閥争いばかりで\x01",
            "法案一つ決められんとは……\x01",
            "やれやれ、悲しい話じゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x102,
        "#0108F………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_BE27")

    label("loc_BDF8")


    #C0677
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "世の中は悲しい話ばかりじゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE27")

    Jump("loc_BFEE")

    label("loc_BE2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_BEA0")

    #C0678
    ChrTalk(
        0xFE,
        (
            "いつも世話になっとる婆さんに\x01",
            "なにか贈り物をしたいんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0xFE,
        (
            "ふむ……\x01",
            "これはいいものじゃなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFEE")

    label("loc_BEA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_BFEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF72")

    #C0680
    ChrTalk(
        0xFE,
        (
            "クロスベルでは毎年何件もの\x01",
            "不審事件が起きているんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0xFE,
        (
            "先日も裏路地で\x01",
            "発砲事件があったという……\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0xFE,
        (
            "この国は、きっと外から見えるほど\x01",
            "素晴らしい国ではないんじゃろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_BFEE")

    label("loc_BF72")


    #C0683
    ChrTalk(
        0xFE,
        (
            "クロスベルでは毎年何件もの\x01",
            "不審事件が起きているんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0xFE,
        (
            "……犯人が薄々判っておっても\x01",
            "捕まらぬことも多いしのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFEE")

    TalkEnd(0xFE)
    Return()

    # Function_24_B43F end

    def Function_25_BFF2(): pass

    label("Function_25_BFF2")

    TalkBegin(0xFE)
    Call(0, 27)
    TalkEnd(0xFE)
    Return()

    # Function_25_BFF2 end

    def Function_26_BFFC(): pass

    label("Function_26_BFFC")

    TalkBegin(0xFE)
    Call(0, 27)
    TalkEnd(0xFE)
    Return()

    # Function_26_BFFC end

    def Function_27_C006(): pass

    label("Function_27_C006")

    OP_4B(0x17, 0xFF)
    OP_4B(0x16, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_C107")

    #C0685
    ChrTalk(
        0x16,
        (
            "リーシャは胸がビッグだから\x01",
            "スレンダー系は難しいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x16,
        (
            "むむ、ここは組み合わせる\x01",
            "という工夫が必要かも……\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x17,
        (
            "#1806F#5P（はあ……\x01",
            "  それが一番の問題なのよね。）\x02\x03",

            "#1808F（“あの格好”の時は内功で\x01",
            "  体型を変えられるんだけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2DF")

    label("loc_C107")


    #C0688
    ChrTalk(
        0x16,
        (
            "んー、そっちもいいけど\x01",
            "さっきのも捨てがたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x16,
        (
            "あ、この花柄入ったのは\x01",
            "リーシャにピッタリかも♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 750)

    #C0690
    ChrTalk(
        0x17,
        (
            "#1810F#5Pサンサン……\x01",
            "気持ちは嬉しいけど。\x02\x03",

            "せっかくの休みなんだから\x01",
            "私の服選びなんてしなくても。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x17, 750)

    #C0691
    ChrTalk(
        0x16,
        (
            "ダメダメ！\x01",
            "リーシャ、そんなに可愛いのに\x01",
            "あんまり服持ってないみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x16,
        (
            "こうなったらサンサンが\x01",
            "可愛いのを選んであげないとね！\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x16,
        (
            "話題の大型新人なんだから\x01",
            "もっとオシャレにも\x01",
            "気を遣わないとダメだよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x17,
        "#1809F#5Pう、うん、そうだね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_C2DF")

    OP_4C(0x17, 0xFF)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_27_C006 end

    def Function_28_C2E8(): pass

    label("Function_28_C2E8")

    TalkBegin(0xFE)

    #C0695
    ChrTalk(
        0x18,
        (
            "今日は買い物よ。\x01",
            "お菓子を買いに来たの㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x18,
        "甘い物はお稽古の原動力だもの～。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_C2E8 end

    def Function_29_C342(): pass

    label("Function_29_C342")

    EventBegin(0x0)
    Fade(500)
    OP_68(-16810, 1500, 23180, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x19F, -16000, 0, 22500, 0)
    SetChrPos(0x109, -15250, 0, 22000, 0)
    SetChrPos(0x101, -16750, 0, 21250, 0)
    OP_93(0xE, 0xB4, 0x0)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 3)), scpexpr(EXPR_END)), "loc_C4D5")

    #C0697
    ChrTalk(
        0xE,
        (
            "#5P女性が喜びそうな\x01",
            "プレゼントといえば\x01",
            "『みっしぃのぬいぐるみ』だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0xE,
        (
            "#5P女の子で、ぬいぐるみが\x01",
            "嫌いな子なんていないだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x109,
        (
            "#12P#0500Fフランは可愛いものが大好きですし、\x01",
            "ぬいぐるみという選択はありかと。\x02\x03",

            "#0503Fみっしぃが好きかどうかは\x01",
            "ちょっと分かりませんが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C788")

    label("loc_C4D5")


    #C0700
    ChrTalk(
        0xE,
        (
            "#5Pいらっしゃい、\x01",
            "こちらは雑貨コーナーだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0xE,
        "#5P何かお探しかな？\x02",
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        (
            "#12P#0000Fあの……女性が喜びそうな\x01",
            "プレゼントを探しているんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0xE,
        (
            "#5P女性が喜びそうな\x01",
            "プレゼント、ねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0xE,
        (
            "#5Pそうだねぇ、それじゃあ……\x01",
            "この『みっしぃのぬいぐるみ』\x01",
            "はどうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0xE,
        (
            "#5P女の子で、ぬいぐるみが\x01",
            "嫌いな子なんていないだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x19F,
        (
            "#12Pおお、これは……\x01",
            "なんだかよさそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x109,
        (
            "#12P#0503Fそうですね……\x02\x03",

            "#0500Fフランは可愛いものが大好きですし、\x01",
            "ぬいぐるみという選択はありかと。\x02\x03",

            "#0503Fみっしぃが好きかどうかは\x01",
            "ちょっと分かりませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x19F,
        (
            "#12Pどうしようか……\x01",
            "こういうのを決めるのは\x01",
            "苦手なんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x19F,
        (
            "#12Pフランさんへのプレゼントは\x01",
            "『みっしぃのぬいぐるみ』で\x01",
            "大丈夫かな？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 3)

    label("loc_C788")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【このプレゼントを薦める】\x01",      # 0
            "【まだ考える】\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8E0")

    #C0710
    ChrTalk(
        0x101,
        (
            "#12P#0000Fこのプレゼントが\x01",
            "いいんじゃないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x19F,
        (
            "#12P……そういわれると\x01",
            "なんだかよさそうに見えてきた。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x19F,
        (
            "#12Pそれじゃ、それください。\x01",
            "あっ、ちゃんと包んでくださいね！\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0xE,
        (
            "#5Pはい、お買い上げ\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x4)
    Call(0, 34)
    Jump("loc_C969")

    label("loc_C8E0")


    #C0714
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそうですね……\x01",
            "もっと検討してましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x19F,
        (
            "#12P……うん、そうだな。\x01",
            "色々な店を見た方がよさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -16000, 0, 22500, 0)
    EventEnd(0x5)

    label("loc_C969")

    Return()

    # Function_29_C342 end

    def Function_30_C96A(): pass

    label("Function_30_C96A")

    EventBegin(0x0)
    Fade(500)
    OP_68(15120, 1500, 7250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x19F, 16000, 0, 6500, 0)
    SetChrPos(0x109, 16750, 0, 6000, 0)
    SetChrPos(0x101, 15250, 0, 5250, 0)
    OP_93(0xB, 0xB4, 0x0)
    SetChrSubChip(0xB, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 4)), scpexpr(EXPR_END)), "loc_CAF0")

    #C0716
    ChrTalk(
        0xB,
        (
            "#5Pこちらのレミフェリア産\x01",
            "『アイスジャム』はいかがかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0xB,
        (
            "#5Pひんやり食感がたまらないと\x01",
            "ひそかにブームですのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x109,
        (
            "#12P#0500Fフランは昔からパン食でしたし\x01",
            "珍しいジャムは喜びそうです。\x02\x03",

            "#0503Fただ、プレゼントとなると\x01",
            "形に残るものがいいのかも……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CDA4")

    label("loc_CAF0")


    #C0719
    ChrTalk(
        0xB,
        (
            "#5P《リジョンフード》の\x01",
            "コーナーにようこそ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0xB,
        (
            "#5Pうちは輸入食材なんかも\x01",
            "豊富に扱ってますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x101,
        (
            "#12P#0000Fあの……女性が喜びそうな\x01",
            "プレゼントを探しているんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0xB,
        (
            "#5Pあら、プレゼント？\x01",
            "ううん、そうね、だったら……\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0xB,
        (
            "#5Pこちらのレミフェリア産\x01",
            "『アイスジャム』はいかがかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0xB,
        (
            "#5Pひんやり食感がたまらないと\x01",
            "ひそかにブームですのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x19F,
        (
            "#11Pジャムか……\x01",
            "案外こういうものの方が\x01",
            "喜ばれるのかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x109,
        (
            "#12P#0500Fそうですね……\x01",
            "フランは昔からパン食でしたし\x01",
            "珍しいジャムは喜びそうです。\x02\x03",

            "#0503Fただ、プレゼントとなると\x01",
            "形に残るものがいいのかも……？\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x19F,
        (
            "#11Pうーん、どうしよう……\x01",
            "迷ってしまうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x19F,
        (
            "#11Pフランさんへのプレゼントは\x01",
            "『アイスジャム』で\x01",
            "大丈夫かな？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 4)

    label("loc_CDA4")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【このプレゼントを薦める】\x01",      # 0
            "【まだ考える】\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEFE")

    #C0729
    ChrTalk(
        0x101,
        (
            "#12P#0000Fこのプレゼントが\x01",
            "いいんじゃないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x19F,
        (
            "#11P……そういわれると\x01",
            "なんだかよさそうに見えてきた。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x19F,
        (
            "#11Pそれじゃ、それください。\x01",
            "あっ、ちゃんと包んでくださいね！\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0xB,
        (
            "#5Pはいよ、お買い上げ\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x5)
    Call(0, 34)
    Jump("loc_CF81")

    label("loc_CEFE")


    #C0733
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそうですね……\x01",
            "もっと検討してましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x19F,
        (
            "#11P……う、そうかい？\x01",
            "じゃあ他の店も見てみようか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 16000, 0, 6500, 0)
    EventEnd(0x5)

    label("loc_CF81")

    Return()

    # Function_30_C96A end

    def Function_31_CF82(): pass

    label("Function_31_CF82")

    EventBegin(0x0)
    Fade(500)
    OP_68(16149, 9530, 11470, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x19F, 15500, 8029, 12250, 90)
    SetChrPos(0x109, 14500, 8029, 11500, 90)
    SetChrPos(0x101, 14750, 8029, 13000, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 5)), scpexpr(EXPR_END)), "loc_D11C")

    #C0735
    ChrTalk(
        0xC,
        (
            "#11Pこちらの新作、\x01",
            "『ぽむぽむニット』はいかが？\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0xC,
        (
            "#11P白いポムをあしらった\x01",
            "もこふわな手触りは\x01",
            "病み付きになりますわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x109,
        (
            "#12P#0500Fそうですね……\x01",
            "フランの私服にも\x01",
            "マッチしている気がします。\x02\x03",

            "#0503Fただ、フランはあの髪型ですから\x01",
            "帽子は苦手かもしれませんけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3FB")

    label("loc_D11C")


    #C0738
    ChrTalk(
        0xC,
        "#11Pブティック《ルッカ》へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xC,
        (
            "#11Pキッズ物から紳士服、\x01",
            "各種ブランド品も扱っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0xC,
        "#11Pご用があれば何なりとどうぞ。\x02",
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあの……女性が喜びそうな\x01",
            "プレゼントを探しているんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0xC,
        (
            "#11P女性へのプレゼントですか？\x01",
            "そうですわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xC,
        (
            "#11Pこちらの新作、\x01",
            "『ぽむぽむニット』はいかが？\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0xC,
        (
            "#11P白いポムをあしらった\x01",
            "もこふわな手触りは\x01",
            "病み付きになりますわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x19F,
        (
            "#5Pニット帽か……\x01",
            "かわいくて、彼女のイメージに\x01",
            "ぴったりかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x109,
        (
            "#12P#0500Fそうですね……\x01",
            "フランの私服にも\x01",
            "マッチしている気がします。\x02\x03",

            "#0503Fただ、フランはあの髪型ですから\x01",
            "帽子は苦手かもしれませんけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x19F,
        (
            "#5Pう、うーん……\x01",
            "なかなか危険な賭けだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x19F,
        (
            "#5Pフランさんへのプレゼントは\x01",
            "『ぽむぽむニット』で\x01",
            "大丈夫かな？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 5)

    label("loc_D3FB")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【このプレゼントを薦める】\x01",      # 0
            "【まだ考える】\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D55D")

    #C0749
    ChrTalk(
        0x101,
        (
            "#6P#0000Fこのプレゼントが\x01",
            "いいんじゃないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x19F,
        (
            "#5P……そういわれると\x01",
            "なんだかよさそうに見えてきた。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x19F,
        (
            "#5Pそれじゃ、それください。\x01",
            "あっ、ちゃんと包んでくださいね！\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0xC,
        (
            "#11Pふふ、ありがとうございます。\x01",
            "少々お待ちくださいね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x6)
    Call(0, 34)
    Jump("loc_D5FF")

    label("loc_D55D")


    #C0753
    ChrTalk(
        0x101,
        (
            "#6P#0000F難しいところですけど……\x01",
            "他のところを見てからでも\x01",
            "遅くないんじゃ？\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x19F,
        (
            "#5Pそ、そうだね。\x01",
            "じゃあ、よそも見てみようか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 15500, 8029, 12250, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    EventEnd(0x5)

    label("loc_D5FF")

    Return()

    # Function_31_CF82 end

    def Function_32_D600(): pass

    label("Function_32_D600")

    EventBegin(0x0)
    Fade(500)
    OP_68(-460, 9520, 27870, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x19F, 0, 8029, 27750, 0)
    SetChrPos(0x109, 750, 8029, 27250, 0)
    SetChrPos(0x101, -750, 8029, 26500, 0)
    OP_93(0xA, 0xB4, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 6)), scpexpr(EXPR_END)), "loc_D7A1")

    #C0755
    ChrTalk(
        0xA,
        (
            "#5Pこちらの\x01",
            "『ストレガー・ブーツ』は\x01",
            "いかがでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0xA,
        (
            "#5P安心のストレガー社製で、\x01",
            "今女性に最も人気の\x01",
            "モデルになっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x109,
        (
            "#12P#0500Fブーツは最近、注目している\x01",
            "ようなことを言っていました。\x02\x03",

            "#0503Fただ、流行しているモデルを\x01",
            "気に入るかどうかは\x01",
            "別ですけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA54")

    label("loc_D7A1")


    #C0758
    ChrTalk(
        0xA,
        (
            "#5Pいらっしゃいませ。\x01",
            "当店では靴を取り扱っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0xA,
        (
            "#5P運動靴・革靴・ブーツ……\x01",
            "お客様のニーズに合わせた品揃えを\x01",
            "取り揃えておりますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x101,
        (
            "#12P#0000F女性が喜びそうな\x01",
            "プレゼントを探しているんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0xA,
        "#5Pふむ、そうですね……\x02",
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0xA,
        (
            "#5Pではこちらの\x01",
            "『ストレガー・ブーツ』は\x01",
            "いかがでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0xA,
        (
            "#5P安心のストレガー社製で、\x01",
            "今女性に最も人気の\x01",
            "モデルになっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x19F,
        (
            "#11Pブーツか……\x01",
            "お姉さん、フランさんは\x01",
            "ブーツ履くんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x109,
        (
            "#12P#0500Fブーツは最近、注目している\x01",
            "ようなことを言っていました。\x02\x03",

            "#0503Fただ、流行しているモデルを\x01",
            "気に入るかどうかは\x01",
            "別ですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x19F,
        "#11Pま、迷うなあ……\x02",
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x19F,
        (
            "#11Pフランさんへのプレゼントは\x01",
            "『ストレガー・ブーツ』で\x01",
            "大丈夫かな？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 6)

    label("loc_DA54")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【このプレゼントを薦める】\x01",      # 0
            "【まだ考える】\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBAC")

    #C0768
    ChrTalk(
        0x101,
        (
            "#12P#0000Fこのプレゼントが\x01",
            "いいんじゃないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x19F,
        (
            "#11P……そういわれると\x01",
            "なんだかよさそうに見えてきた。\x02",
        )
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0x19F,
        (
            "#11Pそれじゃ、それください。\x01",
            "あっ、ちゃんと包んでくださいね！\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0xA,
        (
            "#5Pどうもお買い上げ\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x7)
    Call(0, 34)
    Jump("loc_DC54")

    label("loc_DBAC")


    #C0772
    ChrTalk(
        0x101,
        (
            "#12P#0000F……他の店も見てみましょう。\x01",
            "それからでも遅くないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x19F,
        (
            "#11Pそうだなぁ……\x01",
            "それじゃ、もう少し\x01",
            "回ってみようかな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 8029, 27700, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    EventEnd(0x5)

    label("loc_DC54")

    Return()

    # Function_32_D600 end

    def Function_33_DC55(): pass

    label("Function_33_DC55")

    EventBegin(0x0)
    Fade(500)
    OP_68(-12820, 9330, 7150, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x19F, -13400, 8029, 6600, 45)
    SetChrPos(0x109, -13160, 8029, 5720, 45)
    SetChrPos(0x101, -14580, 8029, 6580, 45)
    OP_93(0xD, 0xE1, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 7)), scpexpr(EXPR_END)), "loc_DE08")

    #C0774
    ChrTalk(
        0xD,
        (
            "#11Pこちらのネックレス\x01",
            "『ピンキームーン』は\x01",
            "どうでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0xD,
        (
            "#11Pピンクの宝石をあしらった\x01",
            "可愛らしいネックレスですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x109,
        (
            "#12P#0500Fそうですね……\x01",
            "フランはピンクが好きですし、\x01",
            "かなりいいかと思います。\x02\x03",

            "#0503Fただ、初めてのプレゼントが\x01",
            "ネックレスって言うのは\x01",
            "ちょっと、重いかも……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0B0")

    label("loc_DE08")


    #C0777
    ChrTalk(
        0xD,
        (
            "#11P当店では主に装飾品・小物などを\x01",
            "取り扱っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0xD,
        (
            "#11P少々値は張りますが\x01",
            "どれも良い品ばかりですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x101,
        (
            "#6P#0000F女性が喜びそうな\x01",
            "プレゼントって、\x01",
            "何かないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0xD,
        "#11Pそうですねぇ……\x02",
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0xD,
        (
            "#11Pこちらのネックレス\x01",
            "『ピンキームーン』は\x01",
            "どうでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0xD,
        (
            "#11Pピンクの宝石をあしらった\x01",
            "可愛らしいネックレスですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x19F,
        (
            "#6Pこ、これは……\x01",
            "なかなかよさそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x109,
        (
            "#12P#0500Fそうですね……\x01",
            "フランはピンクが好きですし、\x01",
            "かなりいいかと思います。\x02\x03",

            "#0503Fただ、初めてのプレゼントが\x01",
            "ネックレスって言うのは\x01",
            "ちょっと、重いかも……？\x02",
        )
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x19F,
        (
            "#6Pた、確かに……\x01",
            "ちょっと意味深すぎるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x19F,
        (
            "#6Pフランさんへのプレゼントは\x01",
            "『ピンキームーン』で\x01",
            "大丈夫かな？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 7)

    label("loc_E0B0")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【このプレゼントを薦める】\x01",      # 0
            "【まだ考える】\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E217")

    #C0787
    ChrTalk(
        0x101,
        (
            "#6P#0000Fこのプレゼントが\x01",
            "いいんじゃないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x19F,
        (
            "#6P……そういわれると\x01",
            "なんだかよさそうに見えてきた。\x02",
        )
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x19F,
        (
            "#6Pそれじゃ、それください。\x01",
            "あっ、ちゃんと包んでくださいね！\x02",
        )
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0xD,
        (
            "#11Pほっほ、分かりました。\x01",
            "丁寧に包装させて\x01",
            "いただきますよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2A, 0x1, 0x8)
    Call(0, 34)
    Jump("loc_E28D")

    label("loc_E217")


    #C0791
    ChrTalk(
        0x101,
        "#6P#0000Fもう少し検討してみましょう。\x02",
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x19F,
        (
            "#6Pううん……\x01",
            "プレゼント選びも難しいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -13400, 8029, 6600, 45)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    EventEnd(0x5)

    label("loc_E28D")

    Return()

    # Function_33_DC55 end

    def Function_34_E28E(): pass

    label("Function_34_E28E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x10, 0xFF)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    OP_68(0, 1500, 3750, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19400, 0)
    SetChrPos(0x101, 0, 30, 4750, 180)
    SetChrPos(0x109, -750, 30, 3250, 45)
    SetChrPos(0x19F, 750, 30, 3250, 315)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0x10, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0793
    ChrTalk(
        0x19F,
        (
            "#11Pおかげでよさそうなものが\x01",
            "手に入ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x19F,
        (
            "#11Pフランさん、喜んでくれると\x01",
            "いいんだけどなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x109,
        (
            "#6P#0503Fうーん、こればっかりは\x01",
            "渡してみないことには……\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x101,
        (
            "#5P#0005Fおっと……\x01",
            "そろそろレストランに\x01",
            "向かいましょう。\x02\x03",

            "#0000F今頃フランも待っていると\x01",
            "おもいますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x19F,
        (
            "#11Pよ、よし……\x01",
            "それじゃあ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x109,
        "#6P#0508F（…………………………）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_E28E end

    def Function_35_E4B1(): pass

    label("Function_35_E4B1")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_E53E")

    #C0799
    ChrTalk(
        0x101,
        (
            "#0000Fまだアントンさんの\x01",
            "プレゼント選びが終わってない。\x02\x03",

            "フランもそんなに\x01",
            "時間がとれないだろうし、\x01",
            "早く決めてしまおう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5FF")

    label("loc_E53E")


    #C0800
    ChrTalk(
        0x19F,
        "どこに行くつもりなんだ？\x02",
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x19F,
        (
            "プレゼント選び、\x01",
            "手伝ってくれるんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0x109,
        (
            "#0500F早くしないと\x01",
            "フランの休憩時間が\x01",
            "終わってしまいますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x101,
        (
            "#0000Fそ、そうだな。\x01",
            "早く選んでしまおう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_E5FF")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 0, 0)
    EventEnd(0x4)
    Return()

    # Function_35_E4B1 end

    def Function_36_E616(): pass

    label("Function_36_E616")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(3660, 2029, 7210, 0)
    MoveCamera(17, 21, 1, 0)
    OP_6E(500, 0)
    SetCameraDistance(16100, 0)
    SetChrPos(0x101, 3750, 30, 9040, 45)
    SetChrPos(0x102, 4920, 30, 7850, 45)
    SetChrPos(0x103, 2550, 0, 7830, 45)
    SetChrPos(0x104, 3730, 0, 6660, 45)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E743")

    #C0804
    ChrTalk(
        0x101,
        (
            "#6P#0003F（百貨店……\x01",
            "  落し物をしたトロントさんが\x01",
            "  立ち寄っていた場所だな。）\x02\x03",

            "#0000Fすみません、この辺りで\x01",
            "落し物を見かけませんでしたか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_E787")

    label("loc_E743")


    #C0805
    ChrTalk(
        0x101,
        (
            "#6P#0000Fすみません、この辺りで\x01",
            "落し物を見かけませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E787")


    #C0806
    ChrTalk(
        0x9,
        "#5P落し物のお問い合わせですね。\x02",
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x8,
        (
            "#11Pええ、こちらの窓口で\x01",
            "何点かお預かりしていますよ。\x01",
            "どのような物をお探しでしょう。\x02",
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

    #C0808
    ChrTalk(
        0x104,
        (
            "#12P#0305Fおいおい、何点かお預かりって……\x01",
            "そいつはもしかして……\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x101,
        (
            "#6P#0006Fああ……\x01",
            "よく考えれば百貨店には\x01",
            "忘れ物や落し物が多そうだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x102,
        (
            "#12P#0100Fトロントさんが落としたのは、\x01",
            "お財布と土産物と……\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x103,
        (
            "#6P#0200F……もう少し詳しく\x01",
            "落し物の特徴を\x01",
            "聞いておくべきだったでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0812
    ChrTalk(
        0x8,
        "#11Pあ、もしかして……\x02",
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x8,
        (
            "#11Pカバンに穴が開いていて\x01",
            "財布を落された方ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x101,
        "#6P#0005Fええ、その人です！\x02",
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x102,
        (
            "#12P#0100Fよかった、目撃された方が\x01",
            "いらっしゃったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x8,
        "あ、いえ、そうではないんですが……\x02",
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x8,
        (
            "当店のお客様の中でも\x01",
            "とても目立つ方だったもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x9,
        (
            "#5Pとてもニコニコした方で、\x01",
            "会う人会う人に\x01",
            "冗談を飛ばしてらっしゃいましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x9,
        (
            "#5Pそれに、帰りがけに\x01",
            "ショーケースにカバンを\x01",
            "引っ掛けてしまわれて。\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x9,
        (
            "#5P後片付けは私達でしたのですが、\x01",
            "その際に見つけたお財布なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x102,
        "#12P#0100Fそ、そうでしたか。\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x103,
        "#6P#0203F（何という分かりやすい……）\x02",
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0x101,
        (
            "#6P#0003Fトロントさん、百貨店には\x01",
            "探しに来なかったんだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0824
    ChrTalk(
        0x104,
        (
            "#12P#0300F途中で力尽きたっぽいなぁ。\x02\x03",

            "ま、だからこそ支援課#6Rオ レ ら#に\x01",
            "依頼を出したんだろうが。\x02",
        )
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x9,
        (
            "#5P遺失物はすぐにお持ちいたします。\x01",
            "少々お待ちくださいね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0826
    ChrTalk(
        0x9,
        "#5Pこちらになります。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0827
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x337),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を預かった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x337, 1)

    #C0828
    ChrTalk(
        0x101,
        (
            "#6P#0000F助かりました、\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x9,
        (
            "#5Pふふ、どうかあの方に\x01",
            "届けてあげて下さいね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x337, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x338, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x339, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE28")

    #C0830
    ChrTalk(
        0x104,
        (
            "#12P#0300Fうっし、これで\x01",
            "全部見つかったみてえだし\x01",
            "戻って知らせてやるとするか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE28")

    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2, 0x1, 0x1)
    SetScenarioFlags(0x1, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE60")
    OP_29(0x2, 0x1, 0x1F)

    label("loc_EE60")

    SetChrPos(0x0, 3740, 0, 7840, 45)
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_68(3740, 1800, 7840, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    EventEnd(0x5)
    Return()

    # Function_36_E616 end

    def Function_37_EEAA(): pass

    label("Function_37_EEAA")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0831
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "２Ｆ　ブティック《ルッカ》\x01",
            "２Ｆ　ハンソンシューズ\x01",
            "２Ｆ　アクセサリ《ベイカー》\x01",
            "１Ｆ　《リジョンフード》\x01",
            "１Ｆ　雑貨コーナー《サザーク》\x02",
        )
    )

    CloseMessageWindow()

    #A0832
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ご不明な点がありましたら\x01",
            "  正面総合インフォメーションにて\x01",
            "  お気軽にお尋ねくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_37_EEAA end

    SaveToFile()

Try(main)
