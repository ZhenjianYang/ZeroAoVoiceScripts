from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0140.bin",                # FileName
        "c0140",                    # MapName
        "c0140",                    # Location
        0x0006,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 6, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0140",                  # 0
        "チャコ",                 # 1
        "ウェンディ",             # 2
        "フェルナンド",           # 3
        "ミゼット",               # 4
        "バジリオ",               # 5
        "ハース",                 # 6
        "市民",                   # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "レインズ",               # 10
    ))

    AddCharChip((
        "chr/ch26100.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch21000.itc",                   # 03
        "chr/ch20800.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch24500.itc",                   # 06
        "chr/ch32300.itc",                   # 07
        "chr/ch32200.itc",                   # 08
        "chr/ch28100.itc",                   # 09
        "chr/ch26000.itc",                   # 0A
    ))

    DeclNpc(9270,    0,       2650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(9329,    0,       -1350,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-1519,   0,       14659,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-4480,   0,       7440,    0,    261,  0x0, 0,   5,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(2299,    0,       6420,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-1519,   0,       14659,   180,  389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(11319,   4000,    8640,    90,   385,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(11470,   4000,    -1720,   90,   385,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(11300,   4000,    -2170,   90,   385,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-4679,   0,       -1820,   90,   389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)

    DeclActor(8130,    0,       3080,    1000,    9270,    1500,    2650,    0x007E, 0,  4,  0x0000)
    DeclActor(8310,    0,       -1360,   1000,    9330,    1500,    -1350,   0x007E, 0,  8,  0x0000)

    ChipFrameInfo(652, 0)                                        # 0

    ScpFunction((
        "Function_0_28C",          # 00, 0
        "Function_1_344",          # 01, 1
        "Function_2_495",          # 02, 2
        "Function_3_677",          # 03, 3
        "Function_4_6C3",          # 04, 4
        "Function_5_A90",          # 05, 5
        "Function_6_2701",         # 06, 6
        "Function_7_2F12",         # 07, 7
        "Function_8_3B19",         # 08, 8
        "Function_9_3B23",         # 09, 9
        "Function_10_3FBE",        # 0A, 10
        "Function_11_5A0B",        # 0B, 11
        "Function_12_6729",        # 0C, 12
        "Function_13_6988",        # 0D, 13
        "Function_14_7AE4",        # 0E, 14
        "Function_15_8555",        # 0F, 15
        "Function_16_90FE",        # 10, 16
        "Function_17_924A",        # 11, 17
        "Function_18_96AA",        # 12, 18
        "Function_19_9937",        # 13, 19
        "Function_20_9A8A",        # 14, 20
        "Function_21_9B8E",        # 15, 21
        "Function_22_A937",        # 16, 22
        "Function_23_B2E9",        # 17, 23
        "Function_24_C8E3",        # 18, 24
        "Function_25_D360",        # 19, 25
        "Function_26_D910",        # 1A, 26
    ))


    def Function_0_28C(): pass

    label("Function_0_28C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2CC"),
        (1, "loc_2D8"),
        (2, "loc_2E4"),
        (3, "loc_2F0"),
        (4, "loc_2FC"),
        (5, "loc_308"),
        (6, "loc_314"),
        (SWITCH_DEFAULT, "loc_320"),
    )


    label("loc_2CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_308")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_314")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_320")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_32C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_343")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_343")

    Return()

    # Function_0_28C end

    def Function_1_344(): pass

    label("Function_1_344")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_494")
    OP_95(0xFE, -4480, 0, 9380, 2000, 0x0)
    OP_95(0xFE, -1380, 0, 11120, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 6900, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 5230, 0, 1000, 2000, 0x0)
    OP_95(0xFE, 3800, 0, 930, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -1350, 0, 930, 2000, 0x0)
    OP_95(0xFE, -1310, 0, -1230, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1310, 0, 2990, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 4640, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 7440, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    Jump("Function_1_344")

    label("loc_494")

    Return()

    # Function_1_344 end

    def Function_2_495(): pass

    label("Function_2_495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4B9")
    SetChrPos(0xC, 7140, 0, 3340, 90)
    SetChrFlags(0xA, 0x80)
    Jump("loc_649")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4E7")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xA, 7390, 0, -250, 270)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_649")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4F5")
    Jump("loc_649")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_503")
    Jump("loc_649")

    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_516")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_529")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_53C")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54F")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_54F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_562")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_649")

    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_575")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_649")

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_588")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_649")

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5AC")
    SetChrPos(0xC, -3640, 0, 5020, 45)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_649")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E4")
    SetChrPos(0xC, -3640, 0, 5020, 45)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DF")
    SetChrFlags(0x11, 0x10)

    label("loc_5DF")

    Jump("loc_649")

    label("loc_5E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_619")
    SetChrPos(0xC, 11470, 4000, 8119, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2040, 0, 12670, 0)
    Jump("loc_649")

    label("loc_619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_649")
    SetChrPos(0xC, -3640, 0, 5020, 45)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 11470, 4000, 8119, 90)

    label("loc_649")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_676")
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_676")

    Return()

    # Function_2_495 end

    def Function_3_677(): pass

    label("Function_3_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68A")
    OP_1B(0x0, 0x0, 0x1A)

    label("loc_68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6AB")
    Sound(128, 1, 50, 0)

    label("loc_6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C2")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_6C2")

    Return()

    # Function_3_677 end

    def Function_4_6C3(): pass

    label("Function_4_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E3")
    SetScenarioFlags(0x0, 0)
    TalkBegin(0x8)
    Call(0, 12)
    TalkEnd(0x8)
    Return()

    label("loc_6E3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85B")

    #C0001
    ChrTalk(
        0x8,
        (
            "いらっしゃいませー☆\x01",
            "こちらはお買い上げカウンターです。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "あ、皆さんはウェンディ先輩の\x01",
            "お知り合いの方たちですね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "ふふ、こちらでは新しい\x01",
            "エニグマカバーを入荷したんですぅ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "ちなみに一度購入していただければ、\x01",
            "その後のカバー交換はいつでも\x01",
            "無料で受け付けていますので～。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "もうじゃんじゃん、チャコのことを\x01",
            "こき使っちゃってくださいですぅ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 4)

    label("loc_85B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_865")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8C")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_94B")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                            # 0
            "エニグマカバーを購入・交換する\x01",      # 1
            "マスタークオーツを購入する\x01",          # 2
            "導力車オプションを購入する\x01",          # 3
            "やめる\x01",                              # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_946")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_946")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_946")

    Jump("loc_9E0")

    label("loc_94B")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                            # 0
            "エニグマカバーを購入・交換する\x01",      # 1
            "マスタークオーツを購入する\x01",          # 2
            "やめる\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A01")
    Call(0, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A87")

    label("loc_A01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A25")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A87")

    label("loc_A25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A49")
    OP_60(0x0)
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A87")

    label("loc_A49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A87")
    OP_60(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_A6B")
    OP_AF(0xC0)
    Jump("loc_A7D")

    label("loc_A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_A7B")
    OP_AF(0xBF)
    Jump("loc_A7D")

    label("loc_A7B")

    OP_AF(0xBE)

    label("loc_A7D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A87")

    Jump("loc_865")

    label("loc_A8C")

    TalkEnd(0x8)
    Return()

    # Function_4_6C3 end

    def Function_5_A90(): pass

    label("Function_5_A90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2700")
    MenuCmd(0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0006
    ChrTalk(
        0x8,
        "どれに交換しますか～？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB6")
    MenuCmd(1, 0, "ＣＰＤ（ロイド）　　　装着中")
    Jump("loc_BD8")

    label("loc_BB6")

    MenuCmd(1, 0, "ＣＰＤ（ロイド）　　　交換する")

    label("loc_BD8")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_C1A")
    MenuCmd(1, 0, "ブルーシェリフ　　　　装着中")
    Jump("loc_C6C")

    label("loc_C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_END)), "loc_C4A")
    MenuCmd(1, 0, "ブルーシェリフ　　　　交換する")
    Jump("loc_C6C")

    label("loc_C4A")

    MenuCmd(1, 0, "ブルーシェリフ　　　　1000ミラ")

    label("loc_C6C")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_END)), "loc_CA4")
    MenuCmd(1, 0, "ハウリングウルフ　　　装着中")
    Jump("loc_CF6")

    label("loc_CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_END)), "loc_CD4")
    MenuCmd(1, 0, "ハウリングウルフ　　　交換する")
    Jump("loc_CF6")

    label("loc_CD4")

    MenuCmd(1, 0, "ハウリングウルフ　　　1000ミラ")

    label("loc_CF6")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_DA5")

    label("loc_D87")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE9")
    MenuCmd(1, 0, "ＣＰＤ（エリィ）　　　装着中")
    Jump("loc_E0B")

    label("loc_DE9")

    MenuCmd(1, 0, "ＣＰＤ（エリィ）　　　交換する")

    label("loc_E0B")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_E4D")
    MenuCmd(1, 0, "ピースグリーン　　　　装着中")
    Jump("loc_E9F")

    label("loc_E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_END)), "loc_E7D")
    MenuCmd(1, 0, "ピースグリーン　　　　交換する")
    Jump("loc_E9F")

    label("loc_E7D")

    MenuCmd(1, 0, "ピースグリーン　　　　1000ミラ")

    label("loc_E9F")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_END)), "loc_ED7")
    MenuCmd(1, 0, "スプリングバード　　　装着中")
    Jump("loc_F29")

    label("loc_ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_END)), "loc_F07")
    MenuCmd(1, 0, "スプリングバード　　　交換する")
    Jump("loc_F29")

    label("loc_F07")

    MenuCmd(1, 0, "スプリングバード　　　1000ミラ")

    label("loc_F29")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_FBA")

    label("loc_F9C")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1195")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FFE")
    MenuCmd(1, 0, "ＣＰＤ（ティオ）　　　装着中")
    Jump("loc_1020")

    label("loc_FFE")

    MenuCmd(1, 0, "ＣＰＤ（ティオ）　　　交換する")

    label("loc_1020")

    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_1064")
    MenuCmd(1, 0, "ブラックキャット　　　交換済み")
    Jump("loc_10B6")

    label("loc_1064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_END)), "loc_1094")
    MenuCmd(1, 0, "ブラックキャット　　　交換する")
    Jump("loc_10B6")

    label("loc_1094")

    MenuCmd(1, 0, "ブラックキャット　　　1000ミラ")

    label("loc_10B6")

    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_END)), "loc_10EE")
    MenuCmd(1, 0, "シャドーサークル　　　装着中")
    Jump("loc_1140")

    label("loc_10EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_END)), "loc_111E")
    MenuCmd(1, 0, "シャドーサークル　　　交換する")
    Jump("loc_1140")

    label("loc_111E")

    MenuCmd(1, 0, "シャドーサークル　　　1000ミラ")

    label("loc_1140")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_11B3")

    label("loc_1195")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_136E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11F7")
    MenuCmd(1, 0, "ＣＰＤ（ランディ）　　装着中")
    Jump("loc_1219")

    label("loc_11F7")

    MenuCmd(1, 0, "ＣＰＤ（ランディ）　　交換する")

    label("loc_1219")

    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_125B")
    MenuCmd(1, 0, "デンジャーオレンジ　　装着中")
    Jump("loc_12AD")

    label("loc_125B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_END)), "loc_128B")
    MenuCmd(1, 0, "デンジャーオレンジ　　交換する")
    Jump("loc_12AD")

    label("loc_128B")

    MenuCmd(1, 0, "デンジャーオレンジ　　1000ミラ")

    label("loc_12AD")

    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_END)), "loc_12E5")
    MenuCmd(1, 0, "ミッドナイトキス　　　装着中")
    Jump("loc_1337")

    label("loc_12E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_END)), "loc_1315")
    MenuCmd(1, 0, "ミッドナイトキス　　　交換する")
    Jump("loc_1337")

    label("loc_1315")

    MenuCmd(1, 0, "ミッドナイトキス　　　1000ミラ")

    label("loc_1337")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_138C")

    label("loc_136E")

    RunExpression(0xD, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xE, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0xF, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_138C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_149A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13CB")
    MenuCmd(1, 0, "ＣＧＦ（ノエル）　　　装着中")
    Jump("loc_13ED")

    label("loc_13CB")

    MenuCmd(1, 0, "ＣＧＦ（ノエル）　　　交換する")

    label("loc_13ED")

    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_END)), "loc_1425")
    MenuCmd(1, 0, "リバティーロード　　　装着中")
    Jump("loc_1477")

    label("loc_1425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_END)), "loc_1455")
    MenuCmd(1, 0, "リバティーロード　　　交換する")
    Jump("loc_1477")

    label("loc_1455")

    MenuCmd(1, 0, "リバティーロード　　　1000ミラ")

    label("loc_1477")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_14AE")

    label("loc_149A")

    RunExpression(0x10, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x11, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14ED")
    MenuCmd(1, 0, "ホワイトクリード　　　装着中")
    Jump("loc_150F")

    label("loc_14ED")

    MenuCmd(1, 0, "ホワイトクリード　　　交換する")

    label("loc_150F")

    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_END)), "loc_1547")
    MenuCmd(1, 0, "クレストフェイス　　　装着中")
    Jump("loc_1599")

    label("loc_1547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_END)), "loc_1577")
    MenuCmd(1, 0, "クレストフェイス　　　交換する")
    Jump("loc_1599")

    label("loc_1577")

    MenuCmd(1, 0, "クレストフェイス　　　1000ミラ")

    label("loc_1599")

    RunExpression(0x14, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_15BC")

    label("loc_15A8")

    RunExpression(0x12, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x13, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15BC")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15EF")
    Sleep(1)
    Return()

    label("loc_15EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_19CA")

    label("loc_162D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166B")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis350.itp")
    Jump("loc_19CA")

    label("loc_166B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A9")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis351.itp")
    Jump("loc_19CA")

    label("loc_16A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E7")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_19CA")

    label("loc_16E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1725")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis352.itp")
    Jump("loc_19CA")

    label("loc_1725")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1763")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis353.itp")
    Jump("loc_19CA")

    label("loc_1763")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A1")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_19CA")

    label("loc_17A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DF")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis354.itp")
    Jump("loc_19CA")

    label("loc_17DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_181D")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis355.itp")
    Jump("loc_19CA")

    label("loc_181D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185B")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis391.itp")
    Jump("loc_19CA")

    label("loc_185B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1899")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis356.itp")
    Jump("loc_19CA")

    label("loc_1899")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D7")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis357.itp")
    Jump("loc_19CA")

    label("loc_18D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1915")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis392.itp")
    Jump("loc_19CA")

    label("loc_1915")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1953")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis359.itp")
    Jump("loc_19CA")

    label("loc_1953")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1991")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis393.itp")
    Jump("loc_19CA")

    label("loc_1991")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CA")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis358.itp")

    label("loc_19CA")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A99")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはロイド専用です。\x01",
            "交換するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1A99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B3A")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはエリィ専用です。\x01",
            "交換するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1B3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BDB")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはティオ専用です。\x01",
            "交換するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1BDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C7E")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはランディ専用です。\x01",
            "交換するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1C7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D17")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはノエル専用です。\x01",
            "交換するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1D17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DA9")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはワジ専用です。\x01",
            "交換するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA9")


    #A0013
    AnonymousTalk(
        0x8,
        "はい、これでいいですか～？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【交換を頼む】\x01",      # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x3)
    OP_60(0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E3")
    ClearScenarioFlags(0x1, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E6A")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1E6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E83")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1E83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E9C")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1E9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EBB")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1EBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ED4")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1ED4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EED")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1EED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F0C")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1F0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F25")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1F25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F3E")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1F3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F5D")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1F5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F76")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1F76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F8F")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1F8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA9")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1FA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FC2")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1FC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FDC")
    SetScenarioFlags(0x1, 1)
    Jump("loc_1FF0")

    label("loc_1FDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FF0")
    SetScenarioFlags(0x1, 1)

    label("loc_1FF0")

    ClearScenarioFlags(0x1, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2008")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2008")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2021")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2021")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_203A")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_203A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_204F")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_204F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2068")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2068")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2081")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2081")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2096")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2096")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20AF")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_20AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20C8")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_20C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DD")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_20DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20F6")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_20F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_210F")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_210F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2124")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2124")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_213D")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_213D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2152")
    SetScenarioFlags(0x1, 2)
    Jump("loc_2166")

    label("loc_2152")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2166")
    SetScenarioFlags(0x1, 2)

    label("loc_2166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_21B3")

    #C0014
    ChrTalk(
        0x8,
        (
            "あれ～、すでに装着中ですよ？\x01",
            "ほかのを選んでくださいねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D4")

    label("loc_21B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2214")

    #C0015
    ChrTalk(
        0x8,
        (
            "あれ～、ミラが足りないみたいですよ？\x01",
            "それじゃ交換はできないですぅ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D4")

    label("loc_2214")


    #C0016
    ChrTalk(
        0x8,
        (
            "了解ですぅ。\x01",
            "ちょっと待っててくださいですぅ～㈱\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(71, 0, 100, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0017
    ChrTalk(
        0x8,
        "はい、お待たせですぅ。\x02",
    )

    CloseMessageWindow()
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2329")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドのエニグマカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22EC")
    ClearScenarioFlags(0xF0, 5)
    ClearScenarioFlags(0x2E, 0)
    Jump("loc_2324")

    label("loc_22EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2311")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2306")
    SetScenarioFlags(0x2C, 0)

    label("loc_2306")

    ClearScenarioFlags(0x2E, 0)
    SetScenarioFlags(0xF0, 5)
    Jump("loc_2324")

    label("loc_2311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_231E")
    SetScenarioFlags(0x2C, 1)

    label("loc_231E")

    SetScenarioFlags(0x2E, 0)
    ClearScenarioFlags(0xF0, 5)

    label("loc_2324")

    Jump("loc_261C")

    label("loc_2329")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23D9")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィのエニグマカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238A")
    ClearScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)
    Jump("loc_23D4")

    label("loc_238A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23AD")
    SetScenarioFlags(0x2C, 2)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_23AD")

    ClearScenarioFlags(0x2E, 1)
    SetScenarioFlags(0xF0, 6)
    Jump("loc_23D4")

    label("loc_23B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CE")
    SetScenarioFlags(0x2C, 3)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_23CE")

    SetScenarioFlags(0x2E, 1)
    ClearScenarioFlags(0xF0, 6)

    label("loc_23D4")

    Jump("loc_261C")

    label("loc_23D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2489")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオのエニグマカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243A")
    ClearScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)
    Jump("loc_2484")

    label("loc_243A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2468")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245D")
    SetScenarioFlags(0x2C, 4)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_245D")

    ClearScenarioFlags(0x2E, 2)
    SetScenarioFlags(0xF0, 7)
    Jump("loc_2484")

    label("loc_2468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247E")
    SetScenarioFlags(0x2C, 5)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_247E")

    SetScenarioFlags(0x2E, 2)
    ClearScenarioFlags(0xF0, 7)

    label("loc_2484")

    Jump("loc_261C")

    label("loc_2489")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_253B")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディのエニグマカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24EC")
    ClearScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)
    Jump("loc_2536")

    label("loc_24EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_251A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_250F")
    SetScenarioFlags(0x2C, 6)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_250F")

    ClearScenarioFlags(0x2E, 3)
    SetScenarioFlags(0xF1, 0)
    Jump("loc_2536")

    label("loc_251A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2530")
    SetScenarioFlags(0x2C, 7)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2530")

    SetScenarioFlags(0x2E, 3)
    ClearScenarioFlags(0xF1, 0)

    label("loc_2536")

    Jump("loc_261C")

    label("loc_253B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25AF")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ノエルのエニグマカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2591")
    ClearScenarioFlags(0x2F, 0)
    Jump("loc_25AA")

    label("loc_2591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A7")
    SetScenarioFlags(0x2D, 1)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_25A7")

    SetScenarioFlags(0x2F, 0)

    label("loc_25AA")

    Jump("loc_261C")

    label("loc_25AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_261C")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ワジのエニグマカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2603")
    ClearScenarioFlags(0x2E, 4)
    Jump("loc_261C")

    label("loc_2603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2619")
    SetScenarioFlags(0x2D, 0)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2619")

    SetScenarioFlags(0x2E, 4)

    label("loc_261C")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2693")
    OP_E0(0x16, 0x0)

    label("loc_2693")


    #C0024
    ChrTalk(
        0x8,
        (
            "ふふ、またのご利用を\x01",
            "お待ちしてま～す。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D4")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_26D4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26ED")

    label("loc_26E3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26ED")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_A9A")

    label("loc_2700")

    Return()

    # Function_5_A90 end

    def Function_6_2701(): pass

    label("Function_6_2701")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_270B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F11")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE0, 0x4)"), scpexpr(EXPR_END)), "loc_274D")
    MenuCmd(1, 0, "プラチナ　　　　購入済み")
    MenuCmd(3, 0, 0x0)
    Jump("loc_2769")

    label("loc_274D")

    MenuCmd(1, 0, "プラチナ　　　　1000ミラ")

    label("loc_2769")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE1, 0x4)"), scpexpr(EXPR_END)), "loc_2799")
    MenuCmd(1, 0, "ミラージュ　　　購入済み")
    MenuCmd(3, 0, 0x1)
    Jump("loc_27B5")

    label("loc_2799")

    MenuCmd(1, 0, "ミラージュ　　　5000ミラ")

    label("loc_27B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_285B")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE5, 0x4)"), scpexpr(EXPR_END)), "loc_27F3")
    MenuCmd(1, 0, "イージス　　　　購入済み")
    MenuCmd(3, 0, 0x2)
    Jump("loc_280F")

    label("loc_27F3")

    MenuCmd(1, 0, "イージス　　　 20000ミラ")

    label("loc_280F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xE6, 0x4)"), scpexpr(EXPR_END)), "loc_283F")
    MenuCmd(1, 0, "セプター　　　　購入済み")
    MenuCmd(3, 0, 0x3)
    Jump("loc_285B")

    label("loc_283F")

    MenuCmd(1, 0, "セプター　　　 50000ミラ")

    label("loc_285B")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_289A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_289A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28B7")
    Sleep(1)
    Return()

    label("loc_28B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28F7")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis378.itp")
    Jump("loc_29B2")

    label("loc_28F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2937")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis379.itp")
    Jump("loc_29B2")

    label("loc_2937")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2977")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis380.itp")
    Jump("loc_29B2")

    label("loc_2977")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B2")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis381.itp")

    label("loc_29B2")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A43")

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "空属性のマスタークオーツです。\x01",
            "※HP/ADF強化型・敵に止めを刺すとHP回復\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B69")

    label("loc_2A43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA6")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "幻属性のマスタークオーツです。\x01",
            "※EP/ATS強化型・敵に止めを刺すとEP回復\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B69")

    label("loc_2AA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B0E")

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "地属性のマスタークオーツです。\x01",
            "※DEF/ADF強化型・特定条件で「完全防御」効果\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B69")

    label("loc_2B0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B69")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水属性のマスタークオーツです。\x01",
            "※STR/ATS強化型・攻撃毎にセピス入手\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B69")


    #A0029
    AnonymousTalk(
        0x8,
        "はい、これでいいですか～？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【購入する】\x01",        # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x3)
    OP_60(0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CA5")

    #C0030
    ChrTalk(
        0x8,
        (
            "あれ～、ミラが足りないみたいですよ？\x01",
            "それじゃ購入はできないですぅ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EE5")

    label("loc_2CA5")


    #C0031
    ChrTalk(
        0x8,
        (
            "了解ですぅ。\x01",
            "ちょっと待っててくださいですぅ～㈱\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(71, 0, 100, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0032
    ChrTalk(
        0x8,
        "はい、お待たせですぅ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7E")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0033
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xE0, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2EB7")

    label("loc_2D7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE8")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0034
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xE1, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2EB7")

    label("loc_2DE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E52")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0035
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xE5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2EB7")

    label("loc_2E52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB7")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xE6, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2EB7")


    #C0037
    ChrTalk(
        0x8,
        (
            "ふふ、またのご利用を\x01",
            "お待ちしてま～す。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2EE5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EFE")

    label("loc_2EF4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EFE")

    OP_CC(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_270B")

    label("loc_2F11")

    Return()

    # Function_6_2701 end

    def Function_7_2F12(): pass

    label("Function_7_2F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2FA2")

    #C0038
    ChrTalk(
        0x8,
        (
            "パパがずっと見つめて来るから\x01",
            "チャコ、穴が開いちゃいそうです……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "でもこんなに心配してくれるなんて\x01",
            "ありがたいことですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_2FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_30BC")

    #C0040
    ChrTalk(
        0x8,
        (
            "戒厳令が出た時、\x01",
            "店長からチャコは帰るように\x01",
            "指示されたんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "ウェンディ先輩がもしもの時のための\x01",
            "人手として残るという話だったので、\x01",
            "チャコも留まることにしたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "パパにはちょっと悪いことを\x01",
            "しちゃった気分ですけど、\x01",
            "きっと分かってくれますよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_30BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_313A")

    #C0043
    ChrTalk(
        0x8,
        (
            "ディーター大統領の演説……\x01",
            "凄い迫力でしたねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "チャコ、聞いている最中に\x01",
            "思わず息を止めちゃいました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_313A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_31CE")

    #C0045
    ChrTalk(
        0x8,
        (
            "この１週間、出勤の時も帰宅の時も\x01",
            "ずっとパパと一緒なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "こういう時だけっていうのも\x01",
            "現金ですけど、やっぱり安心しますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_31CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3241")

    #C0047
    ChrTalk(
        0x8,
        "マインツの人たち、本当に心配ですね。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "どうして、こんなことが\x01",
            "起こっちゃったんでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_3241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3395")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3328")

    #C0049
    ChrTalk(
        0x8,
        (
            "昨日、パパがいつの間にか\x01",
            "うちのお店の面接を\x01",
            "受けたそうなんですよぅ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "パパには技師としての技術が\x01",
            "あるわけでもないし、もちろん\x01",
            "不採用だったそうなんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "うう、チャコ恥ずかしいですぅ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3390")

    label("loc_3328")


    #C0052
    ChrTalk(
        0x8,
        (
            "パパがうちのお店の\x01",
            "面接を受けたそうなんですよぅ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "うう、チャコ、\x01",
            "穴があったら入りたいですぅ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3390")

    Jump("loc_3B18")

    label("loc_3395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33DE")

    #C0054
    ChrTalk(
        0x8,
        (
            "列車が線路からはみ出ちゃうなんて\x01",
            "恐ろしいですねぇ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_33DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3455")

    #C0055
    ChrTalk(
        0x8,
        "何やらパパがソワソワしているんです。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "よく分からないですけど……\x01",
            "もの凄くイヤな予感がしますぅ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_3455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34C2")

    #C0057
    ChrTalk(
        0x8,
        (
            "パパが私を心配してくれているのは\x01",
            "わかるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        "とにかく、過剰なんですよねぇ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_34C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_350F")

    #C0059
    ChrTalk(
        0x8,
        (
            "お客様に説教をするなんて……\x01",
            "ホント信じられないですよぉ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_350F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_359C")

    #C0060
    ChrTalk(
        0x8,
        (
            "さてと、今日もそろそろ\x01",
            "店じまいの時間ですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "パパは相変わらず\x01",
            "お店にいるみたいですけど……\x01",
            "早く帰って欲しいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_359C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_364D")

    #C0062
    ChrTalk(
        0x8,
        (
            "いつも私が使ってる展示用の\x01",
            "導力カメラを、ウェンディ先輩に\x01",
            "持ってかれちゃったんですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "チャコ、クローディア姫や\x01",
            "アルバート大公を撮りたかったのになぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B18")

    label("loc_364D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3727")

    #C0064
    ChrTalk(
        0x8,
        "皆さん、いらっしゃいませー☆\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "この度、当店では導力車の\x01",
            "オプションパーツやカーペイントの\x01",
            "セット販売を開始したんですぅ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "よろしければ、ぜひぜひ\x01",
            "購入の検討をお願いしますですぅ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 1)
    Jump("loc_3860")

    label("loc_3727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37EA")

    #C0067
    ChrTalk(
        0x8,
        (
            "しかし、パパも毎日毎日、\x01",
            "よく飽きないものですね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "言っても来るのを止めないから\x01",
            "最近は放置してるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "あんまり甘やかすのも\x01",
            "良くないかもしれませんねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3860")

    label("loc_37EA")


    #C0070
    ChrTalk(
        0x8,
        (
            "来るなって言っても来るから\x01",
            "最近は放置してるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "あんまり甘やかすのも\x01",
            "良くないかもしれませんねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3860")

    Jump("loc_3B18")

    label("loc_3865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39BA")

    #C0072
    ChrTalk(
        0x8,
        (
            "このところ、店長の\x01",
            "ウェンディ先輩に対する\x01",
            "態度が明らかに変わって来たんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "以前は呼び捨てだったのに\x01",
            "突然、君付けするようになったり……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "あとは先輩に対して\x01",
            "尊敬とかいう言葉をさらっと\x01",
            "使ったりするようになったんですよぅ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "最初は先輩も面食らってましたけど、\x01",
            "今ではすっかり定着しちゃいましたねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3A5B")

    label("loc_39BA")


    #C0076
    ChrTalk(
        0x8,
        (
            "このところ、店長の\x01",
            "ウェンディ先輩に対する\x01",
            "態度が明らかに変わって来たんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "最初は先輩も面食らってましたけど、\x01",
            "今ではすっかり定着しちゃいましたねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A5B")

    Jump("loc_3B18")

    label("loc_3A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3B18")

    #C0078
    ChrTalk(
        0x8,
        (
            "こちらのカウンターでは\x01",
            "エニグマカバーの販売・交換の他に\x01",
            "マスタークオーツも販売しているんですぅ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "もうじゃんじゃん、チャコのことを\x01",
            "こき使っちゃってくださいですぅ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B18")

    Return()

    # Function_7_2F12 end

    def Function_8_3B19(): pass

    label("Function_8_3B19")

    OP_C9(0x1, 0x80)
    Call(0, 9)
    Return()

    # Function_8_3B19 end

    def Function_9_3B23(): pass

    label("Function_9_3B23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B51")
    Call(0, 25)
    Return()

    label("loc_3B51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CFC")
    TalkBegin(0x9)

    #C0080
    ChrTalk(
        0x9,
        "やっほー、ロイド。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "一体またどうしたの？\x01",
            "そんな可愛い子を連れて。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#00000Fああ、ちょっと\x01",
            "知り合いのお子さんに\x01",
            "街を案内している所でさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        "へー、そうなんだ？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "ってことは、その子はあまり\x01",
            "この辺りに来たことがないのね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    #C0085
    ChrTalk(
        0x9,
        (
            "ねえ君、このお店、\x01",
            "なかなか珍しいでしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "ゆっくり見て回って、\x01",
            "存分に愛でて行ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1A2,
        "あ、ああ……（愛でる？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DD, 0)
    TalkEnd(0x9)
    Jump("loc_3D6D")

    label("loc_3CFC")

    TalkBegin(0x9)

    #C0088
    ChrTalk(
        0x9,
        (
            "街案内かぁ、\x01",
            "何だか楽しそうでいいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "ふふ、それにしても\x01",
            "ロイドたちも色んな事を\x01",
            "するわよね～。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3D6D")

    Return()

    label("loc_3D73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D9D")
    Call(0, 21)
    Return()

    label("loc_3D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_BF(0x1, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x4, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF4")
    Call(0, 22)
    Jump("loc_3E6B")

    label("loc_3DF4")

    TalkBegin(0x9)

    #C0090
    ChrTalk(
        0x9,
        (
            "まずは全員、マスタークオーツを\x01",
            "オーブメントにセットしてもらえる？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        "話の続きは、それからさせてもらうわ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3E6B")

    Return()

    label("loc_3E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E92")
    Call(0, 23)
    Return()

    label("loc_3E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EB2")
    SetScenarioFlags(0x0, 1)
    TalkBegin(0x9)
    Call(0, 12)
    TalkEnd(0x9)
    Return()

    label("loc_3EB2")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FBA")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",            # 0
            "改造・合成する\x01",      # 1
            "質問する\x01",            # 2
            "やめる\x01",              # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F28")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3F28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F49")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_3FB5")

    label("loc_3F49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3F68")
    OP_AF(0xD)
    Jump("loc_3F8A")

    label("loc_3F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F78")
    OP_AF(0xC)
    Jump("loc_3F8A")

    label("loc_3F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F88")
    OP_AF(0xB)
    Jump("loc_3F8A")

    label("loc_3F88")

    OP_AF(0xA)

    label("loc_3F8A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FB5")

    label("loc_3F99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FB5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)

    label("loc_3FB5")

    Jump("loc_3EBF")

    label("loc_3FBA")

    TalkEnd(0x9)
    Return()

    # Function_9_3B23 end

    def Function_10_3FBE(): pass

    label("Function_10_3FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_434B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42BE")

    #C0092
    ChrTalk(
        0x9,
        (
            "ロイドに皆さん――\x01",
            "大統領の拘束、\x01",
            "本当にお疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "それからロイド、これからも\x01",
            "苦難が続くと思うけど\x01",
            "お互いに頑張って行こうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#00004Fああ、そうだな。\x02\x03",

            "#00000Fウェンディも何があっても\x01",
            "ここで自分の仕事を続けてくれよ。\x02\x03",

            "まだまだこの先、\x01",
            "オーブメントのことで\x01",
            "頼りにさせてもらうだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        "ふふ、了解よ。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "それから、本当に\x01",
            "大したものじゃないけど\x01",
            "これを持って行ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0097
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を３個受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1FA, 3)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0098
    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、ウェンディ。\x01",
            "すごく助かるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        "ふふ、どういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "とにかく、今後とも\x01",
            "危険な場所に乗り込む時は\x01",
            "くれぐれも気を付けてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "そしてまた落ち着いたら、\x01",
            "オスカーと３人で\x01",
            "食事にでも行きましょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#00002Fああ、そうだな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 6)
    Jump("loc_4346")

    label("loc_42BE")


    #C0103
    ChrTalk(
        0x9,
        (
            "これからも色々と\x01",
            "苦難が続くと思うけど、\x01",
            "お互いに頑張って行こうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "また落ち着いたら、\x01",
            "オスカーと３人で\x01",
            "食事にでも行きましょ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4346")

    Jump("loc_5A0A")

    label("loc_434B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4409")

    #C0105
    ChrTalk(
        0x9,
        (
            "無事らしいと聞いてはいたけど……\x01",
            "こうやって実際に顔を見ると\x01",
            "やっぱり安心するわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "工房に用事がある時は\x01",
            "いつでも言ってちょうだいね。\x01",
            "全力でサポートさせてもらうから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A0A")

    label("loc_4409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_458B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E7")

    #C0107
    ChrTalk(
        0x9,
        (
            "まさかこんな急展開で事が進むとは\x01",
            "思っていなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        "とにかく、これから色々と大変そうね。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "ロイド、工房に入用の時は\x01",
            "いつでも言ってちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        "#00000Fああ、ありがとう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4586")

    label("loc_44E7")


    #C0111
    ChrTalk(
        0x9,
        (
            "まさかこんな急展開で事が進むとは\x01",
            "思っていなかったけど……\x01",
            "とにかく、これから色々と大変そうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "ロイド、工房に入用の時は\x01",
            "いつでも言ってちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4586")

    Jump("loc_5A0A")

    label("loc_458B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_48CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4642")

    #C0113
    ChrTalk(
        0x9,
        (
            "街の復興も大分一区切り付いたけど、\x01",
            "流石に旧市街の方はまだまだ\x01",
            "追いついていないみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "今日も、仕事終わりにでも\x01",
            "ギヨーム親方の所に顔を出そうかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48CA")

    label("loc_4642")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4706")

    #C0115
    ChrTalk(
        0x9,
        (
            "ミスコンかあ～……\x01",
            "ま、何事も経験よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "せっかくの幼馴染の頼みだし\x01",
            "引き受けてあげるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "プログラムが始まるまでは\x01",
            "仕事してるから、必要になったら\x01",
            "連絡ちょうだいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48CA")

    label("loc_4706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4858")

    #C0118
    ChrTalk(
        0x9,
        (
            "ロイドたち、お疲れ様。\x01",
            "私もついさっきイベント会場から\x01",
            "戻ってきたところよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "……それにしてもあの\x01",
            "ロイ君っていう司会の子、\x01",
            "失礼だったわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "あんな紹介じゃ、\x01",
            "いつもわたしがスパナで客を\x01",
            "殴ってるみたいじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        "ロイドもそう思うわよね？\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#00012Fう、うん、そうだな。\x01",
            "（完全には否定できないけど……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_48CA")

    label("loc_4858")


    #C0123
    ChrTalk(
        0x9,
        (
            "ま、案外ミスコンも楽しかったわ。\x01",
            "誘ってくれてありがとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "帰ってきた事だし\x01",
            "さっさと仕事に戻らないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48CA")

    Jump("loc_5A0A")

    label("loc_48CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4A23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49AE")

    #C0125
    ChrTalk(
        0x9,
        (
            "マインツでとんでもないことが\x01",
            "起こったみたいね……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "ロイドたちも、捜査で関わるなら\x01",
            "十分に気を付けてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "エニグマⅡの調整なら\x01",
            "いつでも引き受けるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#00000Fああ、ありがとう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4A1E")

    label("loc_49AE")


    #C0129
    ChrTalk(
        0x9,
        (
            "マインツでとんでもないことが\x01",
            "起こったみたいね……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "ロイドたちも、捜査で関わるなら\x01",
            "十分に気を付けてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A1E")

    Jump("loc_5A0A")

    label("loc_4A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4AB4")

    #C0131
    ChrTalk(
        0x9,
        (
            "どうやらチャコのお父様の\x01",
            "心配性は筋金入りみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "悪いことではないと思うけど、\x01",
            "チャコの気持ちも\x01",
            "考えてあげて欲しいわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A0A")

    label("loc_4AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4B18")

    #C0133
    ChrTalk(
        0x9,
        "何でも導力列車が脱線したんだってね。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        "マシントラブルでも起こったのかな……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A0A")

    label("loc_4B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4CE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C41")

    #C0135
    ChrTalk(
        0x9,
        (
            "職人への尊敬の念を込めて、\x01",
            "昔の工房を思わせる泥臭い内装に\x01",
            "改造する、なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "せっかくお店の方も順調で\x01",
            "お得意さんも増えてきたのに、\x01",
            "それじゃお客さんが混乱するだけよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x9,
        (
            "店長が職人への認識を\x01",
            "改めてくれたことは嬉しいけど、\x01",
            "もっと別の方法を考えて欲しいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4CDC")

    label("loc_4C41")


    #C0138
    ChrTalk(
        0x9,
        (
            "今更、お店の見た目だけ変えても\x01",
            "お客さんが混乱するだけよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        (
            "店長が職人への認識を\x01",
            "改めてくれたことは嬉しいけど、\x01",
            "もっと別の方法を考えて欲しいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CDC")

    Jump("loc_5A0A")

    label("loc_4CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DF3")

    #C0140
    ChrTalk(
        0x9,
        (
            "独立か～、最初に聞いた時は\x01",
            "とにかく驚いたけど、よく聞くと\x01",
            "市長の主張はもっともなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        (
            "このまま黙ってたら\x01",
            "２大国の軍隊が国境門に\x01",
            "駐留するって話もあるくらいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x9,
        (
            "本当の平和を望むんだったら\x01",
            "今こそ声を上げるべきかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4E98")

    label("loc_4DF3")


    #C0143
    ChrTalk(
        0x9,
        (
            "独立か～、最初に聞いた時は\x01",
            "とにかく驚いたけど、よく聞くと\x01",
            "市長の主張はもっともなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        (
            "本当の平和を望むんだったら\x01",
            "今こそ声を上げるべきかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E98")

    Jump("loc_5A0A")

    label("loc_4E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F21")

    #C0145
    ChrTalk(
        0x9,
        (
            "う～ん、チャコのお父様も\x01",
            "よくやるわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        (
            "ま、営業中に従業員をナンパなんて\x01",
            "するヤツの方が悪いと思うけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A0A")

    label("loc_4F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_50C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_505F")

    #C0147
    ChrTalk(
        0x9,
        (
            "あっ、ロイドたち。\x01",
            "こんな時間に珍しいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#00000Fああ、ちょっと\x01",
            "緊急の捜査が入ってさ。\x02\x03",

            "店の方はまだ大丈夫だよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            "ああうん、基本的に８時までは\x01",
            "普通にやってるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#00000Fそうか、よかった。\x01",
            "じゃあ必要な時は調整を頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x9,
        (
            "うん、了解。\x01",
            "それじゃいつでも声掛けてね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_50BC")

    label("loc_505F")


    #C0152
    ChrTalk(
        0x9,
        (
            "エニグマⅡ関係で何かあったら\x01",
            "いつでも言ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        "さくっとバッチリ調整しちゃうから。\x02",
    )

    CloseMessageWindow()

    label("loc_50BC")

    Jump("loc_5A0A")

    label("loc_50C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_54F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_546F")

    #C0154
    ChrTalk(
        0x9,
        (
            "ふふふ、《アルセイユ号》。\x01",
            "ちょっと遠目だけど、\x01",
            "ばっちりカメラに収めたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "さっそく現像してみたんだけど、\x01",
            "良かったらロイドたちもいる？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0156
    ChrTalk(
        0x101,
        (
            "#00005Fへえ、それじゃ\x01",
            "ちょっと見せてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0157
    ChrTalk(
        0x102,
        "#00106Fえっと、これは……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x104,
        "#00306Fこいつぁ、本当に《アルセイユ》なのか？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x109,
        (
            "#10112F辛うじてシルエットで\x01",
            "判るか判らないか、くらいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x9,
        "え～、みなさんよく見てよ。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x9,
        (
            "こっちが船首でこっちが船尾。\x01",
            "辛うじてどころか、はっきり判るのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、言われてみれば\x01",
            "確かにそう見えるけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#00006Fメカ好きならではというか……\x01",
            "ウェンディはいつも見る所が違うよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x9,
        (
            "え～、そうかな。\x01",
            "いたって普通だと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        (
            "#00000Fははは……\x01",
            "（とりあえず普通でない\x01",
            "  事だけは確かだよな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 4)
    Jump("loc_54EF")

    label("loc_546F")


    #C0166
    ChrTalk(
        0x9,
        (
            "ちょっと遠目だけど、ちゃんと\x01",
            "《アルセイユ号》の姿は収めたわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        (
            "ふふふ、この写真、\x01",
            "引き伸ばして部屋の壁に貼ろうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54EF")

    Jump("loc_5A0A")

    label("loc_54F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_57C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_571B")

    #C0168
    ChrTalk(
        0x9,
        (
            "通商会議かぁ、\x01",
            "やっぱりリベールの代表者は\x01",
            "あの《アルセイユ号》で来るんだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#00000F《アルセイユ号》……\x01",
            "ああ、リベール王国の高速巡洋艦だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "その通り、ＺＣＦの技術の粋を集めた\x01",
            "まさに最高傑作と呼ぶに相応しい\x01",
            "飛行船の中の飛行船よ！\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "もし上空を横切りそうなものなら、\x01",
            "仕事を止めてでも写真を撮らなきゃね！\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#00006F気持ちは判らなくないけど……\x01",
            "ほどほどにしておけよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        "ううん、ヤよ。（キッパリ）\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        "#00011Fって、おい。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x104,
        (
            "#00309Fはは、流石はウェンディちゃん。\x01",
            "竹を割ったような見事な答えだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 3)
    Jump("loc_57BD")

    label("loc_571B")


    #C0176
    ChrTalk(
        0x9,
        (
            "通商会議かぁ、やっぱりリベールの代表者は\x01",
            "あの《アルセイユ号》で来るんだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        (
            "もし上空を横切りそうなものなら、\x01",
            "仕事を止めてでも写真を撮らなきゃね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57BD")

    Jump("loc_5A0A")

    label("loc_57C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5859")

    #C0178
    ChrTalk(
        0x9,
        (
            "ウチの店長って思ってたよりも\x01",
            "勉強熱心なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x9,
        (
            "元々デザイナーだからかな？\x01",
            "なんていうか、知識欲みたいなものは\x01",
            "相当あるようね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A0A")

    label("loc_5859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5A0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 7)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_595C")

    #C0180
    ChrTalk(
        0x9,
        (
            "とにかく、マスタークオーツを\x01",
            "セットした状態で１度でいいから\x01",
            "戦闘をこなしてきてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x9,
        (
            "それから、戦闘後はちゃんと\x01",
            "忘れずに私の所に報告に来ること。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x9,
        (
            "そうじゃないと、この講習は\x01",
            "いつまでたっても終わらないからね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A0A")

    label("loc_595C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5A0A")

    #C0183
    ChrTalk(
        0x9,
        (
            "ふふ、ということでこれから\x01",
            "マスタークオーツを\x01",
            "た～っぷり、愛でてあげてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        (
            "愛情を注げば注ぐほど、\x01",
            "マスタークオーツはかならず\x01",
            "恩返ししてくれるんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A0A")

    Return()

    # Function_10_3FBE end

    def Function_11_5A0B(): pass

    label("Function_11_5A0B")


    #C0185
    ChrTalk(
        0x9,
        (
            "オッケー。\x01",
            "何について聞きたいの？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_671B")
    FadeToDark(300, 0, 100)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "戦術オーブメントについて\x01",        # 0
            "クオーツについて\x01",                # 1
            "スロットの開封について\x01",          # 2
            "スロットの強化について\x01",          # 3
            "導力魔法（アーツ）について\x01",      # 4
            "エニグマⅡについて\x01",              # 5
            "マスタークオーツについて\x01",        # 6
            "やめる\x01",                          # 7
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B2E")
    FadeToBright(300, 0)
    OP_5A()

    label("loc_5B2E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5B62"),
        (1, "loc_5D27"),
        (2, "loc_5E56"),
        (3, "loc_5F84"),
        (4, "loc_60F7"),
        (5, "loc_62F3"),
        (6, "loc_64C1"),
        (SWITCH_DEFAULT, "loc_6707"),
    )


    label("loc_5B62")


    #C0186
    ChrTalk(
        0x9,
        (
            "《戦術オーブメント》は、\x01",
            "戦闘用に特化した\x01",
            "小型の携帯導力器のことよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x9,
        (
            "使用者の能力を強化してくれるほか\x01",
            "導力魔法#8Rア  ー  ツ#の使用もサポートしてくれるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        (
            "一般的には、単に『オーブメント』って\x01",
            "呼ばれることも多いわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x9,
        (
            "オーブメントは個人に合わせて\x01",
            "完璧に調整されてるから、\x01",
            "持ち主によって構造が異なるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        (
            "属性限定のスロットがあったり、\x01",
            "スロットを結ぶ線#2Rライン#の形が違ったりするわ。\x01",
            "一度みんなで見比べてみるといいかもね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_5D27")


    #C0191
    ChrTalk(
        0x9,
        (
            "クオーツは、セピスを精錬して作られる\x01",
            "オーブメント用の『結晶回路』のことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        (
            "必要なセピスさえ持ってきてくれれば\x01",
            "ウチで合成ができるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        (
            "クオーツによって色々な効果があるし、\x01",
            "属性値が一定以上になると\x01",
            "導力魔法#8Rア  ー  ツ#が使えるようになるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x9,
        "セピスが溜まったら色々試してみてね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_5E56")


    #C0195
    ChrTalk(
        0x9,
        (
            "オーブメントのスロットは\x01",
            "初めはほとんどが未開封の状態よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "だからクオーツをセットするには\x01",
            "まずはスロットを開封する必要があるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x9,
        (
            "スロットを開封すれば、\x01",
            "それだけクオーツも沢山付けられるし\x01",
            "最大ＥＰも上昇するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x9,
        (
            "開封にはセピスが必要になるけど、\x01",
            "早めに開封して損はないと思うわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_5F84")


    #C0199
    ChrTalk(
        0x9,
        (
            "クオーツの中には『上位クオーツ』と\x01",
            "呼ばれるものがあってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        (
            "これは強力すぎて、普通のスロットだと\x01",
            "セットすることが出来ないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x9,
        (
            "そこで必要になるのが、\x01",
            "スロット自体の強化ってわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "開封と同様にセピスが必要になるけど、\x01",
            "最大ＥＰも上昇するからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x9,
        (
            "強化を焦ることはないと思うけど、\x01",
            "オーブメントのパワーアップには\x01",
            "欠かせない要素と言えるでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_60F7")


    #C0204
    ChrTalk(
        0x9,
        (
            "戦術オーブメントを使って発動する魔法が\x01",
            "いわゆる導力魔法#8Rオーバルアーツ#ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        "単純に『アーツ』って呼ばれる事が多いわ。\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x9,
        (
            "アーツは、セットしたクオーツの\x01",
            "『ラインごとの属性値の合計』によって\x01",
            "発動できる種類が決まってくるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x9,
        (
            "つまり、セットしたクオーツの\x01",
            "属性値が高ければ高いほど、\x01",
            "使えるアーツも増えるってわけね。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x9,
        (
            "ちなみに、より強力なアーツを\x01",
            "使いたい場合は属性値の組み合わせも\x01",
            "重要になってくるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x9,
        (
            "その辺りの詳しい情報は、\x01",
            "捜査手帳にリストが載っているから\x01",
            "そちらを参照してね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_62F3")


    #C0210
    ChrTalk(
        0x9,
        (
            "エニグマの通信機能を引き継ぎ、\x01",
            "大胆な改造が施された後継機――\x01",
            "それが『エニグマⅡ』よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x9,
        (
            "唯一にして最大の変更点は、\x01",
            "新たに『マスタークオーツ』という\x01",
            "特別なクオーツに対応されたことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x9,
        (
            "ちなみに大抵そうなんだけど……\x01",
            "今回のバージョンアップによって\x01",
            "基本アーキテクチャに変更があってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x9,
        (
            "だから、互換性の問題で\x01",
            "旧エニグマで使っていたクオーツは\x01",
            "一切セットができないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x9,
        (
            "てわけで、エニグマⅡを使うには\x01",
            "新しい規格のクオーツが必要になるわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_64C1")


    #C0215
    ChrTalk(
        0x9,
        (
            "マスタークオーツは、\x01",
            "エニグマⅡの中心に嵌める\x01",
            "特別なクオーツのことよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x9,
        (
            "従来のクオーツと決定的に違うのは\x01",
            "それ自身が『成長する』ということね。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x9,
        (
            "オーブメントにセットした状態で\x01",
            "戦闘を重ねることで、レベルが上がって\x01",
            "より強力な効果を発揮してくれるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        (
            "使用者の能力強化、\x01",
            "クオーツの特殊効果、そして属性値……\x01",
            "大きな成長要素はこの３点ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x9,
        (
            "ちなみにマスタークオーツは\x01",
            "どんなものでも最後まで育てれば\x01",
            "非常に強力なものになるらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x9,
        (
            "レベルを上げるには\x01",
            "かなりの時間がかかるみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "浮気せずに、気に入ったものを\x01",
            "使い続けることが重要かもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6716")

    label("loc_6707")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6716")

    label("loc_6716")

    Jump("loc_5A3C")

    label("loc_671B")

    Sleep(150)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_5A0B end

    def Function_12_6729(): pass

    label("Function_12_6729")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    def lambda_673A():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_673A)

    def lambda_6747():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6747)
    TurnDirection(0xA, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_67A3")

    #C0222
    ChrTalk(
        0x8,
        "あ、皆さんは～……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x9,
        (
            "ロイド……\x01",
            "あなた無事だったのね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6820")

    label("loc_67A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_67D8")

    #C0224
    ChrTalk(
        0x9,
        (
            "ロイド……\x01",
            "あなた無事だったのね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6820")

    label("loc_67D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6820")

    #C0225
    ChrTalk(
        0xA,
        "おや、皆さんは……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x9,
        (
            "ロイド……\x01",
            "あなた無事だったのね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6820")


    #C0227
    ChrTalk(
        0x101,
        "#00000Fああ、何とかな。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x9,
        (
            "大体の事情は、警察の\x01",
            "お仲間さんたちから聞いてるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x9,
        (
            "あなたたち、この状況を\x01",
            "何とかしてくれるんでしょ。\x01",
            "ほんと頼んだわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        (
            "あのあの、店の方でも出来る限りの\x01",
            "サポートをさせてもらいますので～。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        (
            "どうか、先を行かれる際は\x01",
            "お気をつけ下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        "#00000Fはい、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x9, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    SetScenarioFlags(0x1BB, 5)
    Return()

    # Function_12_6729 end

    def Function_13_6988(): pass

    label("Function_13_6988")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6999")
    Jump("loc_7AE0")

    label("loc_6999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B7")
    SetScenarioFlags(0x0, 3)
    Call(0, 12)
    Jump("loc_6A2D")

    label("loc_69B7")


    #C0233
    ChrTalk(
        0xFE,
        (
            "しかし、この状況……\x01",
            "まさに混迷を極めてきましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "今後このクロスベルは一体\x01",
            "どうなってしまうのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A2D")

    Jump("loc_7AE0")

    label("loc_6A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6BA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B24")

    #C0235
    ChrTalk(
        0xFE,
        (
            "『クロスベル独立国』……\x01",
            "これで完全に２大国を\x01",
            "敵に回してしまいましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "……結果当然、ラインフォルト社と\x01",
            "ヴェルヌ社の製品は今後一切ウチの店に\x01",
            "入ってこなくなるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        "はあ、頭が痛くなってきましたよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BA4")

    label("loc_6B24")


    #C0238
    ChrTalk(
        0xFE,
        (
            "まさか経済活動を止める覚悟で\x01",
            "独立を押し切るとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "こんなことになるのであれば、\x01",
            "独立に賛成などしなかったのですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BA4")

    Jump("loc_7AE0")

    label("loc_6BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6C3B")

    #C0240
    ChrTalk(
        0xFE,
        (
            "独立の是非を巡る住民投票が、\x01",
            "いよいよ３日後に迫りましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "当日はお店を交代で留守番して、\x01",
            "従業員全員が投票する予定です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE0")

    label("loc_6C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6D6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CFC")

    #C0242
    ChrTalk(
        0xFE,
        (
            "ふむ、占拠事件とは\x01",
            "ただならぬ事態になりましたね……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "帝国が裏で手を引いているのでは\x01",
            "ないかとも言われていますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        "とにかく早く解決してほしいものです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6D69")

    label("loc_6CFC")


    #C0245
    ChrTalk(
        0xFE,
        (
            "帝国が裏で手を引いているのでは\x01",
            "ないかとも言われていますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        "とにかく早く解決してほしいものです。\x02",
    )

    CloseMessageWindow()

    label("loc_6D69")

    Jump("loc_7AE0")

    label("loc_6D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6ED9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4B")

    #C0247
    ChrTalk(
        0xFE,
        (
            "昨日、チャコのお父上が\x01",
            "当店の面接にいらしたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "娘が心配だから\x01",
            "働かせてくれという話でしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "残念ながら、ウチの採用基準に\x01",
            "当てはまらなかったので\x01",
            "遠慮させていただきました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6ED4")

    label("loc_6E4B")


    #C0250
    ChrTalk(
        0xFE,
        (
            "娘が心配だから\x01",
            "働かせてくれという話でしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "残念ながら、ウチの採用基準に\x01",
            "当てはまらなかったので\x01",
            "遠慮させていただきました。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ED4")

    Jump("loc_7AE0")

    label("loc_6ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6F50")

    #C0252
    ChrTalk(
        0xFE,
        (
            "お客さんから聞いたのですが、\x01",
            "何でも列車が脱線したそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "皆さん、無事だと良いのですが……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AE0")

    label("loc_6F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_70B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7031")

    #C0254
    ChrTalk(
        0xFE,
        (
            "店を泥臭く改装する計画について\x01",
            "ウェンディ君とチャコに\x01",
            "意見を聞いてみたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "話を全て終える前に\x01",
            "却下されてしまいましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "う～む、決して悪くない\x01",
            "アイデアだと思ったんですがね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_70AB")

    label("loc_7031")


    #C0257
    ChrTalk(
        0xFE,
        (
            "う～む、決して悪くない\x01",
            "アイデアだと思ったんですがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "やれやれ、２人にあそこまで\x01",
            "反対されては仕方ありませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70AB")

    Jump("loc_7AE0")

    label("loc_70B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7273")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71BC")

    #C0259
    ChrTalk(
        0xFE,
        (
            "かつてウチに居たギヨームさんとは、\x01",
            "経営方針に対する意見の相違で\x01",
            "道を別つことになったわけですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "今思えば、彼には\x01",
            "少し悪いことをしたと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "今さら気付かされましたが、\x01",
            "この業界は何と言っても\x01",
            "職人あってこそですからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_726E")

    label("loc_71BC")


    #C0262
    ChrTalk(
        0xFE,
        (
            "そういえば、ウェンディも\x01",
            "昔の工房の方が雰囲気が\x01",
            "好きだと言っていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "そうだ、ならせめて内装だけでも\x01",
            "昔のゲンテン工房のように\x01",
            "泥臭くしてもいいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_726E")

    Jump("loc_7AE0")

    label("loc_7273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7311")

    #C0264
    ChrTalk(
        0xFE,
        "今日が通商会議の本会議当日ですか。\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "クロスベルの、ひいては大陸全体の\x01",
            "経済の行方を占う重要な国際会議……\x01",
            "いやでも内容が気になりますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE0")

    label("loc_7311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7390")

    #C0266
    ChrTalk(
        0xFE,
        "こんばんは、《ゲンテン》へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "閉店までまだ時間はありますので、\x01",
            "焦らずにごゆっくりご覧ください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE0")

    label("loc_7390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7540")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74A6")

    #C0268
    ChrTalk(
        0xFE,
        (
            "ふう、ウェンディ君にも\x01",
            "困ったものですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "仕事を放っぽり出した挙句、\x01",
            "店のカメラを持ち出すとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "……と、以前の私なら\x01",
            "グチグチこぼしていた所ですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "特に目立った業務への\x01",
            "支障もありませんでしたし、\x01",
            "この位のことは可愛いものですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_753B")

    label("loc_74A6")


    #C0272
    ChrTalk(
        0xFE,
        (
            "展示用のカメラを使うのも、\x01",
            "機能の宣伝になると思えば\x01",
            "むしろ結構なことですしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "どれ、あとで私も撮った写真を\x01",
            "見せてもらうことにしましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_753B")

    Jump("loc_7AE0")

    label("loc_7540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7704")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7645")

    #C0274
    ChrTalk(
        0xFE,
        "お客様、何かお困り事はございませんか？\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "もし導力掃除機をお探しでしたら、\x01",
            "こちらヴェルヌ社製の\x01",
            "最新型がオススメですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "脱着可能な３つのヘッド部品を\x01",
            "使い分けることで、あらゆるシーンに\x01",
            "対応できる大変便利な優れ物なんです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_76FF")

    label("loc_7645")


    #C0277
    ChrTalk(
        0xFE,
        (
            "導力掃除機をお探しでしたら、\x01",
            "こちらヴェルヌ社製の\x01",
            "最新型がオススメですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "脱着可能な３つのヘッド部品を\x01",
            "使い分けることで、あらゆるシーンに\x01",
            "対応できる大変便利な優れ物なんです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76FF")

    Jump("loc_7AE0")

    label("loc_7704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_791C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7895")

    #C0279
    ChrTalk(
        0xFE,
        (
            "私はこれまで恥ずかしながら、\x01",
            "導力器について全くと言っていい程\x01",
            "知識を持ち合わせていませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "ですが店が軌道に乗るにつれて\x01",
            "流石にそれではいけないと気付かされ、\x01",
            "遅ればせながら勉強を始めたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "いやはや、うちのウェンディ君然り、\x01",
            "導力技師というものは凄いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "技術的な知識の習得にも挑戦したのですが、\x01",
            "あまりに複雑すぎて私にはさっぱりでしたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7917")

    label("loc_7895")


    #C0283
    ChrTalk(
        0xFE,
        (
            "いやはや、うちのウェンディ君然り、\x01",
            "導力技師というものは凄いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "私などでは、表面的な\x01",
            "知識を覚えるので精一杯ですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7917")

    Jump("loc_7AE0")

    label("loc_791C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7AE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A2B")

    #C0285
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませ。\x01",
            "オーバルストア《ゲンテン》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "当店では最先端の導力製品は勿論の事、\x01",
            "真心のこもった地域密着型の\x01",
            "アフターサービスをウリにしております。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "何かご相談事がございましたら、\x01",
            "どうぞお気軽にお申し付け下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7AE0")

    label("loc_7A2B")


    #C0288
    ChrTalk(
        0xFE,
        (
            "当店では最先端の導力製品は勿論の事、\x01",
            "真心のこもった地域密着型の\x01",
            "アフターサービスをウリにしております。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "何かご相談事がございましたら、\x01",
            "どうぞお気軽にお申し付け下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AE0")

    TalkEnd(0xFE)
    Return()

    # Function_13_6988 end

    def Function_14_7AE4(): pass

    label("Function_14_7AE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B8D")

    #C0290
    ChrTalk(
        0xFE,
        (
            "正直、買い物の気分じゃないけれど……\x01",
            "家に居ても落ち着かないからお店に来たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "はぁ……早く何もかもスッキリ\x01",
            "解決して日常を取り戻したいわねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_7B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7B9B")
    Jump("loc_8551")

    label("loc_7B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7C3C")

    #C0292
    ChrTalk(
        0xFE,
        (
            "ディーター大統領の演説、\x01",
            "迫力があったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "これからが色々と大変だろうけど、\x01",
            "おばさんも一緒になって\x01",
            "頑張らなきゃって気持ちになったわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_7C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7CEB")

    #C0294
    ChrTalk(
        0xFE,
        (
            "普段は政治に興味のないおばさんだけど、\x01",
            "流石に独立問題だけは別よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "最近の事件を踏まえて\x01",
            "色々と考えたけど、やっぱり\x01",
            "クロスベルは独立すべきだと思うわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_7CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7D5A")

    #C0296
    ChrTalk(
        0xFE,
        "占拠事件だなんて恐ろしいわよね……\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "おばさんにも何か\x01",
            "出来ることがあればいいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_7D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7EC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E23")

    #C0298
    ChrTalk(
        0xFE,
        (
            "独立すると、２大国に税金の一部を\x01",
            "納めなくて済むんですってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "そしたら、クロスベルの経済が\x01",
            "もっともっと発展するって話だし。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        "おばさん、そこは重要だと思うわよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7EC4")

    label("loc_7E23")


    #C0301
    ChrTalk(
        0xFE,
        (
            "独立すると、２大国に\x01",
            "税金を払わなくて済むんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "そしたら、クロスベルの経済が\x01",
            "もっともっと発展するって話だし。\x01",
            "おばさん、そこは重要だと思うわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EC4")

    Jump("loc_8551")

    label("loc_7EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7EFB")

    #C0303
    ChrTalk(
        0xFE,
        "あら、何だか外が騒がしいわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_7EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_806E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FDF")

    #C0304
    ChrTalk(
        0xFE,
        (
            "ラインフォルト社製の製品は\x01",
            "とにかく大容量・高出力を売りに\x01",
            "しているものが多いみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "一方、ヴェルヌ社は機能が豊富で\x01",
            "値段も手頃なものが多いのが特徴ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        "うふふ、これもお国柄なのかしら。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8069")

    label("loc_7FDF")


    #C0307
    ChrTalk(
        0xFE,
        (
            "ラインフォルト社は大容量・高出力、\x01",
            "ヴェルヌ社は利便性と経済性に\x01",
            "力を入れる傾向があるみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        "うふふ、これもお国柄なのかしら。\x02",
    )

    CloseMessageWindow()

    label("loc_8069")

    Jump("loc_8551")

    label("loc_806E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8120")

    #C0309
    ChrTalk(
        0xFE,
        (
            "最近知ったんだけど、\x01",
            "使っていて一番壊れにくいのは\x01",
            "断然ＺＣＦ製らしいわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "他と比べると割高な製品が\x01",
            "多いと思っていたけど、\x01",
            "それだけのことはあるみたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_8120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_81AC")

    #C0311
    ChrTalk(
        0xFE,
        (
            "一見、同じような製品に見えても\x01",
            "メーカーによって個性があるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "うふふ、おばさんにも\x01",
            "だんだん分かってきたわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_81AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8289")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8228")

    #C0313
    ChrTalk(
        0xFE,
        "あら、もうこんな時間なのね。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        (
            "うふふ、早く帰って自慢の\x01",
            "導力レンジでお料理しなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8284")

    label("loc_8228")


    #C0315
    ChrTalk(
        0xFE,
        (
            "それにしても、\x01",
            "導力レンジって便利よね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "随分高かったけど、\x01",
            "買ってよかったわ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8284")

    Jump("loc_8551")

    label("loc_8289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8394")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8327")

    #C0317
    ChrTalk(
        0xFE,
        (
            "通商会議？\x01",
            "う～ん、正直おばさんには\x01",
            "直接関係ないし、興味はないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "ほら、それより見て。\x01",
            "この新製品、可愛いと思わない？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_838F")

    label("loc_8327")


    #C0319
    ChrTalk(
        0xFE,
        (
            "ここに付いてるネジが\x01",
            "オメメだとするとね、\x01",
            "ほら、顔みたいに見えるでしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "うふふ、可愛いわ～。\x02",
    )

    CloseMessageWindow()

    label("loc_838F")

    Jump("loc_8551")

    label("loc_8394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_843B")

    #C0321
    ChrTalk(
        0xFE,
        (
            "ここの店長さん、この数ヶ月で\x01",
            "随分物知りになったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "頼んでもないのに説明されると\x01",
            "少しうっとうしいけど……\x01",
            "熱心さだけは伝わってくるわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_843B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_84B6")

    #C0323
    ChrTalk(
        0xFE,
        "導力製品ってつくづく魅力的よね～。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "別に買い物の予定がなくても、\x01",
            "ついお店に見に来たくなっちゃうわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8551")

    label("loc_84B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8551")

    #C0325
    ChrTalk(
        0xFE,
        (
            "あらあら、この前買った掃除機の\x01",
            "次世代モデルが早くも登場ですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        (
            "もう～、もっと早く言ってくれれば\x01",
            "おばさん、あの時買わなかったのに～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8551")

    TalkEnd(0xFE)
    Return()

    # Function_14_7AE4 end

    def Function_15_8555(): pass

    label("Function_15_8555")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_85CA")

    #C0327
    ChrTalk(
        0xFE,
        (
            "おお、チャコ……\x01",
            "まさしく私の娘のチャコだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "父さんはずっと、\x01",
            "お前のことが心配で心配で……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_85CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_85D8")
    Jump("loc_90FA")

    label("loc_85D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_867A")

    #C0329
    ChrTalk(
        0xFE,
        (
            "『国防軍』と言っても\x01",
            "本当に僕たちを守りきれるか……\x01",
            "正直不安だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "……でも大丈夫。\x01",
            "何があってもチャコのことは\x01",
            "僕が守ってみせるからねっ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_867A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_871B")

    #C0331
    ChrTalk(
        0xFE,
        (
            "チャコの許しが出たから\x01",
            "今朝も二人一緒に出勤してきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        (
            "チャコ、お前のことは\x01",
            "たとえ何に替えようとも\x01",
            "お父さんが必ず守ってやるからなっ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_871B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_87BB")

    #C0333
    ChrTalk(
        0xFE,
        (
            "鉱山町を武装集団が\x01",
            "占拠しただなんて……\x01",
            "な、なんて物騒な話なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "と、とにかく今日は\x01",
            "チャコに何を言われても\x01",
            "一緒に家に帰るつもりだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_87BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8838")

    #C0335
    ChrTalk(
        0xFE,
        (
            "う～ん、店長さんも\x01",
            "話が分からない人だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "でも、まあいい。\x01",
            "それなら、今まで通り\x01",
            "客として来るまでさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_8838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_888A")

    #C0337
    ChrTalk(
        0xFE,
        (
            "脱線事故か……\x01",
            "過去にもたまに聞いたことはあるけど、\x01",
            "珍しいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_888A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_88D8")

    #C0338
    ChrTalk(
        0xFE,
        (
            "今日、この店の面接を\x01",
            "受けることになったんだ。\x01",
            "ドキドキ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_88D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89DB")

    #C0339
    ChrTalk(
        0xFE,
        (
            "娘に何を言われようとも\x01",
            "心配なものは心配なんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "ふむ、いっそのこと\x01",
            "ここで導力技師として働くか……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "だが、私はあくまで\x01",
            "設計畑の人間だからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "簡単な調整くらいはできるんだが……\x01",
            "はたして雇ってくれるだろうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8A2D")

    label("loc_89DB")


    #C0343
    ChrTalk(
        0xFE,
        (
            "う～ん、私はあくまで\x01",
            "設計畑の人間だからなぁ。\x01",
            "はたして雇ってくれるだろうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A2D")

    Jump("loc_90FA")

    label("loc_8A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8AD3")

    #C0344
    ChrTalk(
        0xFE,
        (
            "昨日、仕事終わりを狙って\x01",
            "チャコに近づく輩がいたので\x01",
            "思わず注意してしまったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "そのことで、チャコに\x01",
            "こっぴどく怒られてしまったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_8AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8C31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BC3")

    #C0346
    ChrTalk(
        0xFE,
        (
            "さて、まだ時間はあるけど、\x01",
            "言っている間に閉店時間だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "夜道は危ないし、本当は\x01",
            "チャコと一緒に帰りたい所だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "流石にそこまですると、\x01",
            "チャコに嫌われてしまうしなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        "ふむ、どうしたものか……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8C2C")

    label("loc_8BC3")


    #C0350
    ChrTalk(
        0xFE,
        (
            "後ろからコッソリ付いていくと\x01",
            "私が不審人物になってしまうしなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        "今日も大人しく帰るとするか……\x02",
    )

    CloseMessageWindow()

    label("loc_8C2C")

    Jump("loc_90FA")

    label("loc_8C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8D03")

    #C0352
    ChrTalk(
        0xFE,
        (
            "チャコの先輩のウェンディ君だったか。\x01",
            "彼女、飛行艇のエンジン音が聞こえるなり、\x01",
            "急いで店を駆け出していったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "それからちょっとの間\x01",
            "戻って来なかったんだけど、\x01",
            "一体なんだったんだろうね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_8D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8D68")

    #C0354
    ChrTalk(
        0xFE,
        (
            "ふむ、我が娘ながら\x01",
            "チャコには華があるねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        "悪い虫が寄り付かないか心配だよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_90FA")

    label("loc_8D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EAB")

    #C0356
    ChrTalk(
        0xFE,
        (
            "導力製品の外見のデザインには\x01",
            "メーカーによってそれぞれ\x01",
            "傾向のようなものがあるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "余計な装飾や無駄がない、\x01",
            "機能美という点ではＺＣＦ製と\x01",
            "エプスタイン財団製がズバ抜けてるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "ちなみにラインフォルト社製は\x01",
            "華美なものが多くて、ヴェルヌ社製は\x01",
            "ポップなものが多い傾向にあるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8F54")

    label("loc_8EAB")


    #C0359
    ChrTalk(
        0xFE,
        (
            "僕は導力製品に余計な装飾とかは\x01",
            "一切いらないと思っているタイプなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "無駄な飾り付けのために、\x01",
            "ミラが余計にかかっていると思うと\x01",
            "イライラして仕方がないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F54")

    Jump("loc_90FA")

    label("loc_8F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_90FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_906C")

    #C0361
    ChrTalk(
        0xFE,
        (
            "私は去年まで、\x01",
            "導力製品の設計技師として\x01",
            "働いていたんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "娘が就職したこともあって、\x01",
            "家計にも一区切り付いたから\x01",
            "思い切って退職したんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "仕事に未練がないわけじゃないけど、\x01",
            "何より家族と過ごす時間が\x01",
            "増えたことの方が嬉しいんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_90FA")

    label("loc_906C")


    #C0364
    ChrTalk(
        0xFE,
        (
            "というわけで、\x01",
            "今日も娘のチャコの働きぶりを\x01",
            "見に来たんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "ふむ、いつもながら\x01",
            "よく頑張っているようだね。\x01",
            "父さんは感無量だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90FA")

    TalkEnd(0xFE)
    Return()

    # Function_15_8555 end

    def Function_16_90FE(): pass

    label("Function_16_90FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_91BC")

    #C0366
    ChrTalk(
        0xFE,
        (
            "導力車といい、導力端末といい、\x01",
            "庶民には手の届かない代物よね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "徐々に値段は下がってるらしいけど……\x01",
            "一般家庭に普及するくらいまで、\x01",
            "下がってくれるものなのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9246")

    label("loc_91BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9246")

    #C0368
    ChrTalk(
        0xFE,
        (
            "うひゃー、これが\x01",
            "噂のノート型導力端末かぁ。\x01",
            "さてお値段は……\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "………うーん、凄い０の数。\x01",
            "こんなのを買うのは到底ムリね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9246")

    TalkEnd(0xFE)
    Return()

    # Function_16_90FE end

    def Function_17_924A(): pass

    label("Function_17_924A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_933A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92F1")

    #C0370
    ChrTalk(
        0xFE,
        (
            "チャコちゃんのことがどうしても\x01",
            "忘れられずにまた来ちゃったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        "……あの親父、まだいるのか。\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        "はあ、もう諦めて帰るかな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9335")

    label("loc_92F1")


    #C0373
    ChrTalk(
        0xFE,
        "……あの親父、まだいるんだな。\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        "はあ、諦めて帰るとするか。\x02",
    )

    CloseMessageWindow()

    label("loc_9335")

    Jump("loc_96A6")

    label("loc_933A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_9418")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93BD")

    #C0375
    ChrTalk(
        0xFE,
        (
            "もうすぐ営業終了時間かぁ。\x01",
            "お客さんはまだ\x01",
            "結構いるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        "…………声、かけてみるか？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9413")

    label("loc_93BD")


    #C0377
    ChrTalk(
        0xFE,
        (
            "勇気を振り絞って\x01",
            "チャコちゃんに声を……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "ふう、ちょっと\x01",
            "落ち着いて考えるか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9413")

    Jump("loc_96A6")

    label("loc_9418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_957C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9520")

    #C0379
    ChrTalk(
        0xFE,
        (
            "特に買い物の予定はないんだけど……\x01",
            "販売の子の顔見たさに\x01",
            "またまたお店に来ちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "ちなみにネームプレートで\x01",
            "確認したんだけど、彼女\x01",
            "チャコちゃんって言うんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "あどけない外見に見合った、\x01",
            "とってもキュートな名前だよね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9577")

    label("loc_9520")


    #C0382
    ChrTalk(
        0xFE,
        "俺には除幕式なんて関係ない！\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "あの娘の笑顔を眺めていられれば\x01",
            "それでいいのさ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9577")

    Jump("loc_96A6")

    label("loc_957C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_96A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9650")

    #C0384
    ChrTalk(
        0xFE,
        "う～ん、この店は素晴らしいね。\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "導力器うんぬんじゃなく、\x01",
            "とにかく店員さんが可愛らしい！\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "むふふ、技師の人も素敵だけど、\x01",
            "僕的には販売カウンターの\x01",
            "女の子がドストライクだよ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_96A6")

    label("loc_9650")


    #C0387
    ChrTalk(
        0xFE,
        (
            "う～ん、これは\x01",
            "思わぬ旅のご褒美だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "写真とか頼んだら\x01",
            "撮らせてくれるかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96A6")

    TalkEnd(0xFE)
    Return()

    # Function_17_924A end

    def Function_18_96AA(): pass

    label("Function_18_96AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9729")

    #C0389
    ChrTalk(
        0xFE,
        (
            "ふむ、何やら不穏な事件が\x01",
            "起きているようだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "旅行の日程を早めに切り上げて\x01",
            "さっさと帰るとするか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9933")

    label("loc_9729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_97C5")

    #C0391
    ChrTalk(
        0xFE,
        (
            "昨日事故が起きたという\x01",
            "導力列車も今朝には\x01",
            "完全復旧したそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "ふむ、事故処理に当たった\x01",
            "警備隊というのも\x01",
            "なかなか優秀みたいだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9933")

    label("loc_97C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9821")

    #C0393
    ChrTalk(
        0xFE,
        (
            "ふむ、さっきの音は\x01",
            "サイレンというヤツだな。\x01",
            "あまり聞きたくない音だが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9933")

    label("loc_9821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_98AA")

    #C0394
    ChrTalk(
        0xFE,
        (
            "いや、しかし\x01",
            "導力製品というものは美しいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "同じ機能の製品でも、\x01",
            "メーカーによって形が様々なのも\x01",
            "実に興味深いよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9933")

    label("loc_98AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9933")

    #C0396
    ChrTalk(
        0xFE,
        (
            "ふむ、この店は各国メーカーの\x01",
            "導力製品がバランスよく置いてあるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "流石はクロスベル。\x01",
            "大陸有数の交易都市なだけはある。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9933")

    TalkEnd(0xFE)
    Return()

    # Function_18_96AA end

    def Function_19_9937(): pass

    label("Function_19_9937")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A15")

    #C0398
    ChrTalk(
        0xFE,
        "ほんと何なんだろうな、この状況……\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "とりあえず、家に帰ってても\x01",
            "ろくに飯すらなかったから\x01",
            "ここにいられる方がマシだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "……はぁ、やることもないし、\x01",
            "空気入れマシンの調整でもしてるかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9A86")

    label("loc_9A15")


    #C0401
    ChrTalk(
        0xFE,
        "ほんと何なんだろうな、この状況……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "とりあえず、やることもないし、\x01",
            "空気入れマシンの調整でもしてるかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A86")

    TalkEnd(0xFE)
    Return()

    # Function_19_9937 end

    def Function_20_9A8A(): pass

    label("Function_20_9A8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B15")

    #C0403
    ChrTalk(
        0xFE,
        "感光クオーツ、感光クオーツ、と……\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "お、最新の型は容量も違うなぁ。\x01",
            "これなら２、３個もあれば凌げるかな？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    Jump("loc_9B8A")

    label("loc_9B15")


    #C0405
    ChrTalk(
        0xFE,
        (
            "明日の除幕式に備えて、\x01",
            "予備の感光クオーツを\x01",
            "買い足しに来たんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "いざという時に切れたら\x01",
            "大変ですからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B8A")

    TalkEnd(0xFE)
    Return()

    # Function_20_9A8A end

    def Function_21_9B8E(): pass

    label("Function_21_9B8E")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(6960, 1500, -2230, 0)
    MoveCamera(51, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6850, 0, -790, 90)
    SetChrPos(0x102, 6820, 0, -2020, 90)
    SetChrPos(0x109, 5740, 0, -580, 90)
    SetChrPos(0x105, 5730, 0, -2460, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0407
    ChrTalk(
        0x9,
        "#11Pロイド、待ってたわよ。\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x9,
        (
            "#11Pそれに皆さんも……\x01",
            "って半分は馴染みのない顔だけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、このメンバーでは\x01",
            "活動し始めたばかりだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x109,
        (
            "#6P#10100F初めまして、\x01",
            "ノエル・シーカーと言います。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x105,
        (
            "#6P#10304Fワジ・ヘミスフィアさ、よろしく。\x02\x03",

            "#10300Fそういえば君――\x01",
            "ロイドの幼馴染なんだってね？\x02\x03",

            "よかったら、今度ぜひロイドの\x01",
            "幼き日の面白可笑しいエピソードを\x01",
            "聞かせてもらいたいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0412
    ChrTalk(
        0x9,
        (
            "#11Pふふ、いいですよ～！\x01",
            "ロイドの弱みを握りたいのね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0413
    ChrTalk(
        0x101,
        (
            "#6P#00006Fな、なんの話だよ……\x02\x03",

            "#00000F――とりあえず、\x01",
            "さっさと本題に移ってくれ。\x02\x03",

            "エニグマⅡの講習を\x01",
            "してくれるんじゃなかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x9,
        "#11Pあっと、そうだったわね。\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x9,
        "#11Pオッホン、ではさっそく……\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x9,
        (
            "#11P――ロイドたちも、\x01",
            "既にエニグマⅡを使っているから\x01",
            "知っているとは思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x9,
        (
            "#11Pエプスタイン財団が行った、\x01",
            "今回のバージョンアップの\x01",
            "唯一にして最大の変更点……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x9,
        (
            "#11Pそれは何といっても、\x01",
            "中心のスロット構造にあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x9,
        (
            "#11Pそして、その中心に嵌める\x01",
            "特別なクオーツのことを\x01",
            "『マスタークオーツ』と呼ぶの。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、この文様が刻まれた\x01",
            "クオーツのことだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x9,
        "#11Pそう、その球状のクオーツよ。\x02",
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x9,
        (
            "#11Pそして、そのマスタークオーツが\x01",
            "従来のクオーツと決定的に違う点は\x01",
            "『成長する』ということにあるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x9,
        (
            "#11Pオーブメントにセットした状態で\x01",
            "戦闘を重ねることで錬磨され、\x01",
            "段階的に強化されていくそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x109,
        (
            "#6P#10100F何ていうか……\x01",
            "少し神秘的な感じがしますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x102,
        (
            "#6P#00100Fええ、まるで\x01",
            "命を持っているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、ちなみにこれから\x01",
            "その原理やなんかを\x01",
            "講義してくれるのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x9,
        (
            "#11Pあ、ううん、そういうのは\x01",
            "残念だけど研究者じゃないから\x01",
            "私も詳しくは知らないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x9,
        (
            "#11Pそもそも本来は成長というより、\x01",
            "秘められた力を引き出して行く\x01",
            "イメージらしいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x9,
        (
            "#11Pそれはともかく、皆さんに\x01",
            "覚えて行ってもらいたいのは\x01",
            "エニグマⅡの扱い方――\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x9,
        "#11Pつまり、論より実践というヤツね。\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x9,
        (
            "#11Pというわけで、まずは\x01",
            "こちらを受け取ってくれるかしら。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0432
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "エリィは",
            scpstr(SCPSTR_CODE_ITEM, 0xDE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0xDE, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0433
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "ワジは",
            scpstr(SCPSTR_CODE_ITEM, 0xDF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0xDF, 1)

    #C0434
    ChrTalk(
        0x102,
        "#6P#00105Fこれがマスタークオーツ……\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x105,
        (
            "#6P#10303Fふむ、確かに普通のクオーツとは\x01",
            "存在感みたいなものも全然違うね。\x02\x03",

            "#10300Fでもいいのかい、もらっちゃって？\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x9,
        (
            "#11Pええ、いいもなにも\x01",
            "それは元々警察本部から\x01",
            "皆さんに支給された品だから。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x9,
        (
            "#11Pちなみに、マスタークオーツは\x01",
            "普通の工房では合成できない上に\x01",
            "量産できる物じゃないらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x9,
        (
            "#11Pウチでも財団の研究所から\x01",
            "幾つか入荷はしているけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x9,
        (
            "#11P基本的に、１種類につき\x01",
            "１個しか売ることができないから\x01",
            "くれぐれも丁重に扱ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x109,
        (
            "#6P#10100Fなるほど……\x01",
            "それだけ希少な品ということですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x101,
        (
            "#6P#00005Fそれは分かったけどウェンディ、\x01",
            "実践って一体何をすればいいんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x9,
        (
            "#11Pそうね、まずはその前に全員、\x01",
            "マスタークオーツをオーブメントに\x01",
            "セットしてもらえるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x9,
        (
            "#11P誰がどれを付けても構わないから\x01",
            "４人全員がセットしたら\x01",
            "声を掛けてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x9,
        (
            "#11Pちなみに、マスタークオーツにも\x01",
            "特定の属性はあるけど、\x01",
            "スロットに“縛り”はないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x9,
        (
            "#11Pつまり、マスタークオーツは\x01",
            "人を選ばずにセットできるって寸法よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x102,
        "#6P#00100Fなるほど、それは便利ですね。\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、それじゃさっそく\x01",
            "セットさせてもらおうか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0448
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【エニグマⅡの講習】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x132, 6)
    OP_29(0x65, 0x1, 0x0)
    OP_1B(0x0, 0x0, 0x1A)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_21_9B8E end

    def Function_22_A937(): pass

    label("Function_22_A937")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(6960, 1500, -2230, 0)
    MoveCamera(51, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6850, 0, -790, 90)
    SetChrPos(0x102, 6820, 0, -2020, 90)
    SetChrPos(0x109, 5740, 0, -580, 90)
    SetChrPos(0x105, 5730, 0, -2460, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    #C0449
    ChrTalk(
        0x9,
        (
            "#11Pオッケー、どうやら全員\x01",
            "ちゃんとマスタークオーツを\x01",
            "セットできたみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x101,
        "#6P#00000Fで、次はどうするんだ？\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x9,
        (
            "#11Pふふ、単純明快――\x01",
            "今度はマスタークオーツの効果を\x01",
            "実際に確かめて来て欲しいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x102,
        (
            "#6P#00105Fそれは……\x01",
            "戦闘を通してという事ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x9,
        "#11Pええ、そういうことです。\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x9,
        (
            "#11Pロイドとノエルさんは\x01",
            "既に経験済みみたいだけど、\x01",
            "改めて宜しくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x109,
        "#6P#10100F了解です。\x02",
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#6P#00005Fちなみに何か条件はあるのか？\x01",
            "戦う場所とか、回数とか。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x9,
        (
            "#11Pううん、特にないわ。\x01",
            "場所も相手も完全にお任せね。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x9,
        (
            "#11P戦闘の回数も１度で十分だけど、\x01",
            "ただし逃げずにちゃんと戦ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x105,
        "#6P#10300Fフフ、ごもっともだね。\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x102,
        "#6P#00100Fそれでロイド、場所はどうするの？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AD12")

    #C0461
    ChrTalk(
        0x101,
        (
            "#6P#00003Fそうだな、今のところ\x01",
            "街の外に出る予定もないし……\x02\x03",

            "#00000Fメゾン・イメルダにいる魔獣を\x01",
            "相手にするのがいいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_AD9E")

    label("loc_AD12")


    #C0462
    ChrTalk(
        0x101,
        (
            "#6P#00003Fそういえば、メゾン・イメルダに\x01",
            "手配魔獣がいるんだったな。\x02\x03",

            "#00000Fそれを片付けるついでに\x01",
            "試してみるのがいいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_AD9E")


    #C0463
    ChrTalk(
        0x109,
        (
            "#6P#10100F確かに、そこなら\x01",
            "手っ取り早く試せそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x9,
        (
            "#11Pふふ、どうやら\x01",
            "場所も決まったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x9,
        (
            "#11Pじゃあ、次はこのクオーツを\x01",
            "持って行ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0466
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x74),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x74, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0467
    ChrTalk(
        0x101,
        "#6P#00005Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x9,
        "#11Pええ、それも警察本部からの支給品よ。\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x9,
        (
            "#11P通常のスロットにそのクオーツを嵌めると、\x01",
            "エニグマⅡ用の新アーツ\x01",
            "『アナライズ』が使えるようになるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x9,
        (
            "#11P情報を制する者は\x01",
            "戦いを制するっていうしね。\x01",
            "ぜひ戦闘に役立てて。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、了解だ。\x02\x03",

            "#00003F（今はティオがいないし……\x01",
            "  しばらく魔獣の情報集めは\x01",
            "  アーツに頼る必要がありそうだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x9,
        (
            "#11Pそれじゃ、\x01",
            "気をつけて行ってらっしゃい。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x9,
        (
            "#11Pオーブメントの改造や\x01",
            "クオーツを合成したい時は、\x01",
            "いつでも言ってちょうだいね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0474
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ウェンディに話しかけ、\x01",
            "　『改造・合成する』を選択すると、\x01",
            "　新しいクオーツの合成や\x01",
            "　戦術オーブメントのスロット開封・強化が行えます。\x02\x03",

            "※新しいクオーツを合成し、セットすれば\x01",
            "　様々なアーツを使うことが出来るようになります。\x02\x03",

            "※スロットの開封・強化を行えば、\x01",
            "　セットできるクオーツの数が増えるとともに\x01",
            "　最大ＥＰを増加させることができます。\x02\x03",

            "※なお、それらの機能を利用するには、\x01",
            "  『セピス』と呼ばれる七耀石の欠片が必要です。\x01",
            "  （セピスは主に魔獣を倒すことで入手できます。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x132, 7)
    OP_29(0x65, 0x1, 0x1)
    OP_1B(0x0, 0xFF, 0xFFFF)
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_69(0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_22_A937 end

    def Function_23_B2E9(): pass

    label("Function_23_B2E9")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(6960, 1500, -2230, 0)
    MoveCamera(51, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6850, 0, -790, 90)
    SetChrPos(0x102, 6820, 0, -2020, 90)
    SetChrPos(0x109, 5740, 0, -580, 90)
    SetChrPos(0x105, 5730, 0, -2460, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    #C0475
    ChrTalk(
        0x9,
        (
            "#11Pあ、お疲れ様ー。\x01",
            "どうやらちゃんと\x01",
            "戦闘をこなしてきたみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x9,
        (
            "#11Pそれでエリィさんにワジ君、\x01",
            "マスタークオーツを実際に使ってみた\x01",
            "感想はどうでした？\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x102,
        "#6P#00100Fええ、何ていうか驚きました。\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x105,
        (
            "#6P#10304Fああ、まさかクオーツ１つで\x01",
            "あれだけのパフォーマンスを\x01",
            "発揮できるとはね。\x02\x03",

            "#10300F正直、ここまでとは思ってなかったかな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B62C")

    #C0479
    ChrTalk(
        0x9,
        "#11Pふふ、いいリアクションですね～。\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x9,
        (
            "#11Pちなみに最終段階まで成長させると、\x01",
            "あることが出来るようになるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x9,
        (
            "#11Pまあ、それは\x01",
            "実際に育ててみてのお楽しみかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x109,
        (
            "#6P#10105Fへえ～、まだサプライズが\x01",
            "用意されてるんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#6P#00009Fはは、楽しみにしておくよ。\x02\x03",

            "#00000Fそれで、講習ってのは\x01",
            "これで終わりでいいんだよな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B71C")

    label("loc_B62C")


    #C0484
    ChrTalk(
        0x9,
        "#11Pふふ、いいリアクションですね～。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x9,
        (
            "#11P何ていうか、エプスタイン財団の\x01",
            "開発関係者にも届けてあげたいかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x101,
        (
            "#6P#00009Fはは、確かに褒められて\x01",
            "悪い気はしないだろうしな。\x02\x03",

            "#00000Fそれで、講習ってのは\x01",
            "これで終わりでいいんだよな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B71C")


    #C0487
    ChrTalk(
        0x9,
        (
            "#11Pうん、警察本部にも\x01",
            "私の方から報告させてもらうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x9,
        (
            "#11Pじゃあ最後に――\x01",
            "オーブメントに関して質問があれば\x01",
            "何でも答えさせてもらうけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x9,
        "#11P改めて聞いておきたいことはある？\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        "#6P#00000Fそうだな……\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B7FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C548")

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "戦術オーブメントについて\x01",        # 0
            "クオーツについて\x01",                # 1
            "スロットの開封について\x01",          # 2
            "スロットの強化について\x01",          # 3
            "導力魔法（アーツ）について\x01",      # 4
            "エニグマⅡについて\x01",              # 5
            "マスタークオーツについて\x01",        # 6
            "やめる\x01",                          # 7
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_B8F7"),
        (1, "loc_BAD8"),
        (2, "loc_BC17"),
        (3, "loc_BD55"),
        (4, "loc_BEDC"),
        (5, "loc_C0F0"),
        (6, "loc_C2D2"),
        (SWITCH_DEFAULT, "loc_C534"),
    )


    label("loc_B8F7")


    #C0491
    ChrTalk(
        0x9,
        (
            "#11P#11P《戦術オーブメント》は、\x01",
            "戦闘用に特化した\x01",
            "小型の携帯導力器のことよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x9,
        (
            "#11P#11P使用者の能力を強化してくれるほか\x01",
            "導力魔法#8Rア  ー  ツ#の使用もサポートしてくれるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x9,
        (
            "#11P一般的には、単に『オーブメント』って\x01",
            "呼ばれることも多いわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x9,
        (
            "#11Pオーブメントは個人に合わせて\x01",
            "完璧に調整されてるから、\x01",
            "持ち主によって構造が異なるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x9,
        (
            "#11P属性限定のスロットがあったり、\x01",
            "スロットを結ぶ線#2Rライン#の形が違ったりするわ。\x01",
            "一度みんなで見比べてみるといいかもね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_BAD8")


    #C0496
    ChrTalk(
        0x9,
        (
            "#11Pクオーツは、セピスを精錬して作られる\x01",
            "オーブメント用の『結晶回路』のことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x9,
        (
            "#11P必要なセピスさえ持ってきてくれれば\x01",
            "ウチで合成ができるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x9,
        (
            "#11Pクオーツによって色々な効果があるし、\x01",
            "属性値が一定以上になると\x01",
            "導力魔法#8Rア  ー  ツ#が使えるようになるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x9,
        "#11Pセピスが溜まったら色々試してみてね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_BC17")


    #C0500
    ChrTalk(
        0x9,
        (
            "#11Pオーブメントのスロットは\x01",
            "初めはほとんどが未開封の状態よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x9,
        (
            "#11Pだからクオーツをセットするには\x01",
            "まずはスロットを開封する必要があるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x9,
        (
            "#11Pスロットを開封すれば、\x01",
            "それだけクオーツも沢山付けられるし\x01",
            "最大ＥＰも上昇するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x9,
        (
            "#11P開封にはセピスが必要になるけど、\x01",
            "早めに開封して損はないと思うわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_BD55")


    #C0504
    ChrTalk(
        0x9,
        (
            "#11Pクオーツの中には『上位クオーツ』と\x01",
            "呼ばれるものがあってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x9,
        (
            "#11Pこれは強力すぎて、普通のスロットだと\x01",
            "セットすることが出来ないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x9,
        (
            "#11Pそこで必要になるのが、\x01",
            "スロット自体の強化ってわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x9,
        (
            "#11P開封と同様にセピスが必要になるけど、\x01",
            "最大ＥＰも上昇するからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x9,
        (
            "#11P強化を焦ることはないと思うけど、\x01",
            "オーブメントのパワーアップには\x01",
            "欠かせない要素と言えるでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_BEDC")


    #C0509
    ChrTalk(
        0x9,
        (
            "#11P戦術オーブメントを使って発動する魔法が\x01",
            "いわゆる導力魔法#8Rオーバルアーツ#ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x9,
        "#11P単純に『アーツ』って呼ばれる事が多いわ。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x9,
        (
            "#11Pアーツは、セットしたクオーツの\x01",
            "『ラインごとの属性値の合計』によって\x01",
            "発動できる種類が決まってくるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x9,
        (
            "#11Pつまり、セットしたクオーツの\x01",
            "属性値が高ければ高いほど、\x01",
            "使えるアーツも増えるってわけね。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x9,
        (
            "#11Pちなみに、より強力なアーツを\x01",
            "使いたい場合は属性値の組み合わせも\x01",
            "重要になってくるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x9,
        (
            "#11Pその辺りの詳しい情報は、\x01",
            "捜査手帳にリストが載っているから\x01",
            "そちらを参照してね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_C0F0")


    #C0515
    ChrTalk(
        0x9,
        (
            "#11Pエニグマの通信機能を引き継ぎ、\x01",
            "大胆な改造が施された後継機――\x01",
            "それが『エニグマⅡ』よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x9,
        (
            "#11P唯一にして最大の変更点は、\x01",
            "新たに『マスタークオーツ』という\x01",
            "特別なクオーツに対応されたことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x9,
        (
            "#11Pちなみに大抵そうなんだけど……\x01",
            "今回のバージョンアップによって\x01",
            "基本アーキテクチャに変更があってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x9,
        (
            "#11Pだから、互換性の問題で\x01",
            "旧エニグマで使っていたクオーツは\x01",
            "一切セットができないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x9,
        (
            "#11Pてわけで、エニグマⅡを使うには\x01",
            "新しい規格のクオーツが必要になるわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_C2D2")


    #C0520
    ChrTalk(
        0x9,
        (
            "#11Pマスタークオーツは、\x01",
            "エニグマⅡの中心に嵌める\x01",
            "特別なクオーツのことよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x9,
        (
            "#11P従来のクオーツと決定的に違うのは\x01",
            "それ自身が『成長する』ということね。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x9,
        (
            "#11Pオーブメントにセットした状態で\x01",
            "戦闘を重ねることで、レベルが上がって\x01",
            "より強力な効果を発揮してくれるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x9,
        (
            "#11P使用者の能力強化、\x01",
            "クオーツの特殊効果、そして属性値……\x01",
            "大きな成長要素はこの３点ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x9,
        (
            "#11Pちなみにマスタークオーツは\x01",
            "どんなものでも最後まで育てれば\x01",
            "非常に強力なものになるらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x9,
        (
            "#11Pレベルを上げるには\x01",
            "かなりの時間がかかるみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x9,
        (
            "#11P浮気せずに、気に入ったものを\x01",
            "使い続けることが重要かもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C543")

    label("loc_C534")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C543")

    label("loc_C543")

    Jump("loc_B7FF")

    label("loc_C548")


    #C0527
    ChrTalk(
        0x101,
        (
            "#6P#00004F……これで十分かな。\x02\x03",

            "#00000Fありがとう、ウェンディ。\x01",
            "今日は勉強になったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x9,
        "#11Pふふ、なら良かった。\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x9,
        (
            "#11Pちなみにこれ、\x01",
            "エニグマⅡ用の新規格のクオーツ。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x9,
        (
            "#11P私から特務支援課に\x01",
            "再始動をお祝いしてプレゼントよ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0531
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xB7, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0532
    ChrTalk(
        0x101,
        (
            "#6P#00002F悪いな、ウェンディ。\x01",
            "必ず有効に使わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x102,
        "#6P#00102F本当に助かります。\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x9,
        "#11Pふふ、どういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x9,
        (
            "#11Pとりあえず、また何か\x01",
            "分からないことがあったら\x01",
            "いつでも聞いてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x9,
        (
            "#11P隣のカウンターでも\x01",
            "新しく色んなサービスを\x01",
            "提供していく予定だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x9,
        (
            "#11Pこれからも、\x01",
            "オーバルストア《ゲンテン》を\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x105,
        "#6P#10302Fフフ、こちらこそ。\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x109,
        (
            "#6P#10102F今日はどうも\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    Sound(9, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0540
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【エニグマⅡの講習】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_29(0x65, 0x1, 0x3)
    OP_29(0x65, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0x2)
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_69(0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_B2E9 end

    def Function_24_C8E3(): pass

    label("Function_24_C8E3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-6460, 1500, 2290, 0)
    MoveCamera(62, 32, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24150, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_CA5D")
    SetChrPos(0x1A2, -7900, 0, 2940, 90)
    SetChrPos(0x102, -7900, 0, 2090, 90)
    SetChrPos(0x101, -7900, 0, 3210, 90)
    SetChrPos(0x104, -7900, 0, 1790, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(100, 0, 100, 0)
    OP_0D()

    def lambda_C9AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_C9AE)

    def lambda_C9BF():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C9BF)

    def lambda_C9D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C9D4)

    def lambda_C9E5():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C9E5)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_CA0E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CA0E)

    def lambda_CA1F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CA1F)
    Sleep(100)

    def lambda_CA37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CA37)

    def lambda_CA48():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CA48)
    Jump("loc_CCD8")

    label("loc_CA5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_CB9D")
    SetChrPos(0x1A2, -7900, 0, 2940, 90)
    SetChrPos(0x102, -7900, 0, 2090, 90)
    SetChrPos(0x101, -7900, 0, 3210, 90)
    SetChrPos(0x109, -7900, 0, 1790, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(100, 0, 100, 0)
    OP_0D()

    def lambda_CAEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_CAEE)

    def lambda_CAFF():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_CAFF)

    def lambda_CB14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CB14)

    def lambda_CB25():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CB25)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_CB4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CB4E)

    def lambda_CB5F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CB5F)
    Sleep(100)

    def lambda_CB77():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CB77)

    def lambda_CB88():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CB88)
    Jump("loc_CCD8")

    label("loc_CB9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_CCD8")
    SetChrPos(0x1A2, -7900, 0, 2940, 90)
    SetChrPos(0x102, -7900, 0, 2090, 90)
    SetChrPos(0x101, -7900, 0, 3210, 90)
    SetChrPos(0x105, -7900, 0, 1790, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(100, 0, 100, 0)
    OP_0D()

    def lambda_CC2E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_CC2E)

    def lambda_CC3F():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_CC3F)

    def lambda_CC54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CC54)

    def lambda_CC65():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CC65)
    OP_68(-4830, 1500, 1680, 3000)
    Sleep(700)

    def lambda_CC8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CC8E)

    def lambda_CC9F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CC9F)
    Sleep(100)

    def lambda_CCB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_CCB7)

    def lambda_CCC8():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CCC8)

    label("loc_CCD8")

    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    #C0541
    ChrTalk(
        0x1A2,
        (
            "ここがいろんな雑誌でも\x01",
            "とりあげられている\x01",
            "オーバルストアというヤツか……\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x1A2,
        (
            "内装といい、置いてある製品といい、\x01",
            "まさに最先端って感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x1A2,
        (
            "共和国にもおそらく、これだけの\x01",
            "規模の店はなかったと思うが……\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、確かに各国の製品が\x01",
            "こうして一同に集まって来るのは\x01",
            "クロスベルくらいだものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x101,
        (
            "#00000Fそれに、最先端といえば\x01",
            "ここには導力ネット端末だって\x01",
            "置いてるからな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0546
    ChrTalk(
        0x1A2,
        "導力ねっと……ってなんだっけ？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_CEBB")

    def lambda_CE9E():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CE9E)
    Sleep(50)

    def lambda_CEAE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CEAE)
    Jump("loc_CF0C")

    label("loc_CEBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_CEE6")

    def lambda_CEC9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CEC9)
    Sleep(50)

    def lambda_CED9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CED9)
    Jump("loc_CF0C")

    label("loc_CEE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_CF0C")

    def lambda_CEF4():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CEF4)
    Sleep(50)

    def lambda_CF04():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CF04)

    label("loc_CF0C")


    #C0547
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、簡単に言うと従来の\x01",
            "通信器を発展させた技術さ。\x02\x03",

            "#00004Fエプスタイン財団という所が\x01",
            "中心となって、これらの計画を\x01",
            "進めているんだが……\x02\x03",

            "#00000F端末を使えば、声だけじゃなく\x01",
            "文字や画像といった情報なんかも\x01",
            "送り合うことが可能なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x1A2,
        (
            "へ、へぇ～……\x01",
            "そんなことができるのか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_93(0x1A2, 0x5A, 0x1F4)
    OP_64(0x1A2)

    #C0549
    ChrTalk(
        0x1A2,
        (
            "フ、フンッ、ボクは別に\x01",
            "驚いてなんかいないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x1A2,
        (
            "そんな知識を披露したくらいで\x01",
            "いい気になるんじゃないぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D197")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0551
    ChrTalk(
        0x101,
        (
            "#6P#00006Fいや、別にいい気に\x01",
            "なってはいないんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x104,
        "#12P#00300Fハ、素直じゃねえ小僧だな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D334")

    label("loc_D197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D271")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0553
    ChrTalk(
        0x101,
        (
            "#6P#00006Fいや、別にいい気に\x01",
            "なってはいないんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x109,
        (
            "#12P#10100F素直じゃないというか、\x01",
            "よほど悔しかったみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D334")

    label("loc_D271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D334")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0555
    ChrTalk(
        0x101,
        (
            "#6P#00006Fいや、別にいい気に\x01",
            "なってはいないんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x105,
        (
            "#12P#10300Fフフ、よほど\x01",
            "悔しかったんだろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D334")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 5)
    OP_29(0x73, 0x1, 0xA)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -4800, 0, 2530, 90)
    EventEnd(0x5)
    Return()

    # Function_24_C8E3 end

    def Function_25_D360(): pass

    label("Function_25_D360")

    EventBegin(0x0)
    Fade(500)
    OP_68(7160, 1500, -1600, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 6940, 0, -1330, 90)
    SetChrPos(0x102, 6850, 0, -320, 90)
    SetChrPos(0x103, 6730, 0, -2450, 90)
    SetChrPos(0x104, 5780, 0, -1390, 90)
    SetChrPos(0x105, 5400, 0, -2610, 90)
    SetChrPos(0x109, 5680, 0, -160, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_0D()

    #C0557
    ChrTalk(
        0x9,
        "あらロイド、何か用？\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x105,
        (
            "#10300F（ミスコンの『職人』枠……\x01",
            "  彼女なら相応しいんじゃない？）\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        (
            "#00003F（うーん、こういうことは\x01",
            "  余り興味なさそうだけど……\x01",
            "  せっかくだし頼んでみるか。）\x02\x03",

            "#00000F……ウェンディ、ちょっといいかな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0560
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "チャリティイベントの\x01",
            "ミスコンへの参加を頼んでみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0561
    ChrTalk(
        0x9,
        "みすこん……？　なにそれ。\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x9,
        (
            "新しいオーブメントの\x01",
            "部品かなにか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0563
    ChrTalk(
        0x104,
        (
            "#00306Fい、いやいやいや。\x01",
            "全然違うぜウェンディちゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x103,
        (
            "#00203Fさすが職人気質……\x01",
            "世俗に疎いのもまた然りですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x9,
        (
            "あはは、うそうそ。\x01",
            "流石に知ってるって。\x01",
            "要するに美少女コンテストのことよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x9,
        (
            "そっかー、面白そうだし……\x01",
            "参加してみてもいいわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x102,
        "#00105Fほ、本当ですか？\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x109,
        (
            "#10102Fふふ、なんだか意外です。\x01",
            "ＯＫがもらえるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x9,
        "ま、何事も経験だしね～。\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x9,
        (
            "せっかくの幼馴染の頼みだし\x01",
            "引き受けてあげるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x9,
        (
            "プログラムが始まるまでは\x01",
            "仕事してるから、必要になったら\x01",
            "連絡ちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x101,
        (
            "#00000Fああ、分かった。\x01",
            "ありがとな、ウェンディ。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8DD")

    #C0573
    ChrTalk(
        0x101,
        (
            "#00000F──さて、これでようやく\x01",
            "参加者枠が埋まったな。\x02\x03",

            "市民会館に行って\x01",
            "ロイさんたちに報告しよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_D8DD")

    SetScenarioFlags(0x199, 5)
    OP_4C(0x9, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 7330, 0, -1350, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_25_D360 end

    def Function_26_D910(): pass

    label("Function_26_D910")

    EventBegin(0x1)

    #C0574
    ChrTalk(
        0x101,
        (
            "#00000Fおっと、今は店を\x01",
            "出るわけにはいかないな。\x02\x03",

            "マスタークオーツをセットしたら\x01",
            "ウェンディに声を掛けよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 0, 2230, 90)
    EventEnd(0x4)
    Return()

    # Function_26_D910 end

    SaveToFile()

Try(main)
