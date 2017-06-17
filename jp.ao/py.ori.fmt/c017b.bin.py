from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c017b.bin",                # FileName
        "c017b",                    # MapName
        "c017b",                    # Location
        0x0005,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c017b",                  # 0
        "受付嬢パール",           # 1
        "受付嬢シンシア",         # 2
        "ハンソン",               # 3
        "リジョン",               # 4
        "プラダ",                 # 5
        "ベイカー",               # 6
        "サザーク",               # 7
        "ネストン支配人",         # 8
        "ジャネッタ",             # 9
        "ドロテ",                 # 10
        "ケン",                   # 11
        "オネスト老人",           # 12
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
        "chr/ch21600.itc",                   # 08
        "chr/ch34600.itc",                   # 09
        "chr/ch25900.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch20500.itc",                   # 0C
    ))

    DeclNpc(7480,    0,       10079,   225,  257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5880,    0,       11680,   225,  257,  0x0, 0,   9,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(59,      8000,    30040,   180,  257,  0x0, 0,   10,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(15979,   0,       9520,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(18110,   8000,    12220,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-11529,  8000,    8510,    225,  257,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-15989,  0,       25739,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-2660,   0,       9829,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-6659,   8000,    28870,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(13800,   8000,    6199,    225,  257,  0x0, 0,   6,   0,   0,   1,   0,   20,  255,  0)
    DeclNpc(8020,    8000,    17270,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-14449,  8000,    14420,   90,   257,  0x0, 0,   8,   0,   0,   0,   0,   22,  255,  0)

    DeclActor(6250,    0,       9040,    1000,    7480,    1500,    10080,   0x007E, 0,  4,  0x0000)
    DeclActor(4440,    0,       10280,   1000,    5880,    1500,    11680,   0x007E, 0,  6,  0x0000)
    DeclActor(-480,    8000,    28360,   1000,    60,      9500,    30040,   0x007E, 0,  8,  0x0000)
    DeclActor(15980,   0,       7760,    1000,    15980,   1500,    9520,    0x007E, 0,  10, 0x0000)
    DeclActor(16480,   8000,    11730,   1000,    18110,   9500,    12220,   0x007E, 0,  12, 0x0000)
    DeclActor(-12390,  8000,    7660,    1000,    -11530,  9500,    8510,    0x007E, 0,  14, 0x0000)
    DeclActor(-16030,  0,       23800,   1000,    -15990,  1500,    25740,   0x007E, 0,  16, 0x0000)
    DeclActor(1670,    0,       13270,   800,     1670,    1500,    13270,   0x007C, 0,  23, 0x0000)

    ChipFrameInfo(920, 0)                                        # 0

    ScpFunction((
        "Function_0_398",          # 00, 0
        "Function_1_448",          # 01, 1
        "Function_2_521",          # 02, 2
        "Function_3_54F",          # 03, 3
        "Function_4_57F",          # 04, 4
        "Function_5_583",          # 05, 5
        "Function_6_64C",          # 06, 6
        "Function_7_650",          # 07, 7
        "Function_8_74B",          # 08, 8
        "Function_9_74F",          # 09, 9
        "Function_10_A23",         # 0A, 10
        "Function_11_A27",         # 0B, 11
        "Function_12_B65",         # 0C, 12
        "Function_13_B69",         # 0D, 13
        "Function_14_C9C",         # 0E, 14
        "Function_15_CA0",         # 0F, 15
        "Function_16_EBD",         # 10, 16
        "Function_17_EC1",         # 11, 17
        "Function_18_10B2",        # 12, 18
        "Function_19_1138",        # 13, 19
        "Function_20_11A4",        # 14, 20
        "Function_21_1237",        # 15, 21
        "Function_22_1296",        # 16, 22
        "Function_23_12E9",        # 17, 23
    ))


    def Function_0_398(): pass

    label("Function_0_398")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3D0"),
        (1, "loc_3DC"),
        (2, "loc_3E8"),
        (3, "loc_3F4"),
        (4, "loc_400"),
        (5, "loc_40C"),
        (6, "loc_418"),
        (SWITCH_DEFAULT, "loc_424"),
    )


    label("loc_3D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_3DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_3E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_3F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_400")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_40C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_418")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_424")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_430")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_447")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_447")

    Return()

    # Function_0_398 end

    def Function_1_448(): pass

    label("Function_1_448")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_520")
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
    Jump("Function_1_448")

    label("loc_520")

    Return()

    # Function_1_448 end

    def Function_2_521(): pass

    label("Function_2_521")

    SetChrPos(0x12, 8020, 8000, 17270, 90)
    SetChrPos(0x11, 9070, 8000, 17290, 270)
    BeginChrThread(0x11, 0, 0, 0)
    SetChrFlags(0x11, 0x10)
    Return()

    # Function_2_521 end

    def Function_3_54F(): pass

    label("Function_3_54F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_570")
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    Jump("loc_57E")

    label("loc_570")

    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)

    label("loc_57E")

    Return()

    # Function_3_54F end

    def Function_4_57F(): pass

    label("Function_4_57F")

    Call(0, 5)
    Return()

    # Function_4_57F end

    def Function_5_583(): pass

    label("Function_5_583")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61B")

    #C0001
    ChrTalk(
        0x8,
        (
            "今日は仕事終わりに、\x01",
            "シンシア先輩とジャネッタちゃんの\x01",
            "３人でお食事に行くんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "久しぶりのお食事会、\x01",
            "ふふ、楽しみだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_648")

    label("loc_61B")


    #C0003
    ChrTalk(
        0x8,
        (
            "久しぶりのお食事会、\x01",
            "ふふ、楽しみだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_648")

    TalkEnd(0x8)
    Return()

    # Function_5_583 end

    def Function_6_64C(): pass

    label("Function_6_64C")

    Call(0, 7)
    Return()

    # Function_6_64C end

    def Function_7_650(): pass

    label("Function_7_650")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F9")

    #C0004
    ChrTalk(
        0x9,
        (
            "ジャネッタさん、\x01",
            "今日はやけに張り切って\x01",
            "何かあったんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        (
            "３人で食事に行くのは別に\x01",
            "初めてではないんですけど……\x01",
            "気にしすぎかしら？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_747")

    label("loc_6F9")


    #C0006
    ChrTalk(
        0x9,
        (
            "３人で食事に行くのは別に\x01",
            "初めてではないんですけど……\x01",
            "気にしすぎかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_747")

    TalkEnd(0x9)
    Return()

    # Function_7_650 end

    def Function_8_74B(): pass

    label("Function_8_74B")

    Call(0, 9)
    Return()

    # Function_8_74B end

    def Function_9_74F(): pass

    label("Function_9_74F")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_75C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_7BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7D9")
    OP_AF(0x26)
    Jump("loc_7FB")

    label("loc_7D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7E9")
    OP_AF(0x25)
    Jump("loc_7FB")

    label("loc_7E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7F9")
    OP_AF(0x24)
    Jump("loc_7FB")

    label("loc_7F9")

    OP_AF(0x23)

    label("loc_7FB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A1A")

    label("loc_80A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81E")
    Jump("loc_A1A")

    label("loc_81E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_957")

    #C0007
    ChrTalk(
        0xA,
        (
            "靴選びは夕方以降に行った方が良い事を\x01",
            "皆さんはご存知でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xA,
        (
            "というのも、人の足は朝起きてから\x01",
            "徐々にむくんでいき、夕方頃にもなると\x01",
            "最大で約１リジュほども大きくなるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xA,
        (
            "なので、足が最も大きくなる夕方以降に\x01",
            "サイズを選ぶのが良いとされているのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A1A")

    label("loc_957")


    #C0010
    ChrTalk(
        0xA,
        (
            "実は、人の足は朝起きてから\x01",
            "徐々にむくんでいき、夕方頃にもなると\x01",
            "最大で約１リジュほども大きくなるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xA,
        (
            "なので、足が最も大きくなる夕方以降に\x01",
            "サイズを選ぶのが良いとされているのですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1A")

    Jump("loc_75C")

    label("loc_A1F")

    TalkEnd(0xA)
    Return()

    # Function_9_74F end

    def Function_10_A23(): pass

    label("Function_10_A23")

    Call(0, 11)
    Return()

    # Function_10_A23 end

    def Function_11_A27(): pass

    label("Function_11_A27")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B61")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A92")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_A92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB2")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B5C")

    label("loc_AB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC6")
    Jump("loc_B5C")

    label("loc_AC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0012
    ChrTalk(
        0xB,
        (
            "こんばんは。\x01",
            "《リジョンフード》へようこそ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        (
            "晩御飯の支度がまだなら、\x01",
            "ぜひウチで材料を\x01",
            "買い揃えて行って下さいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5C")

    Jump("loc_A34")

    label("loc_B61")

    TalkEnd(0xB)
    Return()

    # Function_11_A27 end

    def Function_12_B65(): pass

    label("Function_12_B65")

    Call(0, 13)
    Return()

    # Function_12_B65 end

    def Function_13_B69(): pass

    label("Function_13_B69")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C98")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_BD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BF3")
    OP_AF(0x21)
    Jump("loc_C15")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C03")
    OP_AF(0x20)
    Jump("loc_C15")

    label("loc_C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C13")
    OP_AF(0x1F)
    Jump("loc_C15")

    label("loc_C13")

    OP_AF(0x1E)

    label("loc_C15")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C93")

    label("loc_C24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C38")
    Jump("loc_C93")

    label("loc_C38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C93")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0014
    ChrTalk(
        0xC,
        (
            "いらっしゃいませ。\x01",
            "どうぞ夜のショッピングを\x01",
            "お楽しみ下さい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C93")

    Jump("loc_B76")

    label("loc_C98")

    TalkEnd(0xC)
    Return()

    # Function_13_B69 end

    def Function_14_C9C(): pass

    label("Function_14_C9C")

    Call(0, 15)
    Return()

    # Function_14_C9C end

    def Function_15_CA0(): pass

    label("Function_15_CA0")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB9")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_D0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D2A")
    OP_AF(0x11)
    Jump("loc_D3C")

    label("loc_D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D3A")
    OP_AF(0x10)
    Jump("loc_D3C")

    label("loc_D3A")

    OP_AF(0xF)

    label("loc_D3C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EB4")

    label("loc_D4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D5F")
    Jump("loc_EB4")

    label("loc_D5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2F")

    #C0015
    ChrTalk(
        0xD,
        "すっかり日も暮れましたね。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xD,
        (
            "そういえば、首脳たちによる\x01",
            "アルカンシェルの観劇は\x01",
            "もうそろそろ終わる頃でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xD,
        (
            "ふむ、楽しんで\x01",
            "くれているといいのですが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_EB4")

    label("loc_E2F")


    #C0018
    ChrTalk(
        0xD,
        (
            "そういえば、首脳たちによる\x01",
            "アルカンシェルの観劇は\x01",
            "もうそろそろ終わる頃でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xD,
        (
            "ふむ、楽しんで\x01",
            "くれているといいのですが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB4")

    Jump("loc_CAD")

    label("loc_EB9")

    TalkEnd(0xD)
    Return()

    # Function_15_CA0 end

    def Function_16_EBD(): pass

    label("Function_16_EBD")

    Call(0, 17)
    Return()

    # Function_16_EBD end

    def Function_17_EC1(): pass

    label("Function_17_EC1")

    TalkBegin(0xE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ECE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AE")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F2C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_F2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4C")
    OP_AF(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10A9")

    label("loc_F4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F60")
    Jump("loc_10A9")

    label("loc_F60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1048")

    #C0020
    ChrTalk(
        0xE,
        (
            "ジャネッタちゃんが、\x01",
            "今朝からやけに楽しそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "明日にはスーパージャネッタに\x01",
            "生まれ変わってるとか、\x01",
            "よく分からない事を言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xE,
        "何だろう、何故だか凄く気になるぞ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_10A9")

    label("loc_1048")


    #C0023
    ChrTalk(
        0xE,
        (
            "ジャネッタちゃんが、\x01",
            "今朝からやけに楽しそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xE,
        "何だろう、何故だか凄く気になるぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_10A9")

    Jump("loc_ECE")

    label("loc_10AE")

    TalkEnd(0xE)
    Return()

    # Function_17_EC1 end

    def Function_18_10B2(): pass

    label("Function_18_10B2")

    TalkBegin(0xFE)

    #C0025
    ChrTalk(
        0xFE,
        (
            "本日の営業は通常通り\x01",
            "２０：００をもって\x01",
            "終了とさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "お買い忘れやお忘れ物のないよう\x01",
            "お気を付け下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_10B2 end

    def Function_19_1138(): pass

    label("Function_19_1138")

    TalkBegin(0xFE)

    #C0027
    ChrTalk(
        0xFE,
        (
            "お洋服は準備オッケーだし、\x01",
            "お化粧のノリもバッチリです。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "うふふ、今夜の私は一味違いますよ㈱\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_1138 end

    def Function_20_11A4(): pass

    label("Function_20_11A4")

    TalkBegin(0xFE)

    #C0029
    ChrTalk(
        0xFE,
        "いい、ケン。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "帰ったらまずパパにゴメンなさい。\x01",
            "それから、すかさずにハグよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "大丈夫、２人で挟み込めば\x01",
            "怖いものナシなんだから。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_11A4 end

    def Function_21_1237(): pass

    label("Function_21_1237")

    TalkBegin(0xFE)

    #C0032
    ChrTalk(
        0xFE,
        (
            "ママが買い物に夢中で\x01",
            "こんな時間まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "さすがのパパも\x01",
            "怒っていると思います。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_1237 end

    def Function_22_1296(): pass

    label("Function_22_1296")

    TalkBegin(0xFE)

    #C0034
    ChrTalk(
        0xFE,
        "さて、そろそろ家に帰らんとのう。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "婆さんに怒られては敵わんからな。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_1296 end

    def Function_23_12E9(): pass

    label("Function_23_12E9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0036
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

    #A0037
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

    # Function_23_12E9 end

    SaveToFile()

Try(main)
