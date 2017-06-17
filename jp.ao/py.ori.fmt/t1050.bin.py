from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1050.bin",                # FileName
        "t1050",                    # MapName
        "t1050",                    # Location
        0x0042,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 3, 0, 4],
    )

    BuildStringList((
        "t1050",                  # 0
        "ハガー支配人",           # 1
        "ロッチー",               # 2
        "シトラス",               # 3
        "技師",                   # 4
        "占い師",                 # 5
        "キーア",                 # 6
        "フラン",                 # 7
        "セシル",                 # 8
        "イリア",                 # 9
        "リーシャ",               # 10
        "シュリ",                 # 11
        "マリアベル",             # 12
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch25600.itc",                   # 02
        "chr/ch26000.itc",                   # 03
        "chr/ch14202.itc",                   # 04
    ))

    DeclNpc(-479,    0,       10050,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-93959,  0,       8260,    0,    385,  0x0, 0,   1,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(-101819, 0,       8859,    90,   389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(1059,    0,       10489,   177,  389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-13359,  150,     15430,   90,   453,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(5500,    0,       13500,   1200,    5500,    1500,    13500,   0x007C, 0,  30, 0x0000)
    DeclActor(-20,     0,       8270,    1500,    -480,    1500,    10050,   0x007E, 0,  6,  0x0000)
    DeclActor(12010,   0,       15830,   1200,    12010,   450,     15830,   0x007C, 0,  5,  0x0000)
    DeclActor(1260,    0,       9210,    1500,    1060,    1500,    10490,   0x007E, 0,  11, 0x0000)

    ChipFrameInfo(772, 0)                                        # 0

    ScpFunction((
        "Function_0_304",          # 00, 0
        "Function_1_3BC",          # 01, 1
        "Function_2_41D",          # 02, 2
        "Function_3_47E",          # 03, 3
        "Function_4_586",          # 04, 4
        "Function_5_5D3",          # 05, 5
        "Function_6_688",          # 06, 6
        "Function_7_68C",          # 07, 7
        "Function_8_1035",         # 08, 8
        "Function_9_159F",         # 09, 9
        "Function_10_16EE",        # 0A, 10
        "Function_11_19D3",        # 0B, 11
        "Function_12_19D7",        # 0C, 12
        "Function_13_1BCC",        # 0D, 13
        "Function_14_28F3",        # 0E, 14
        "Function_15_2953",        # 0F, 15
        "Function_16_2EC1",        # 10, 16
        "Function_17_317E",        # 11, 17
        "Function_18_31FA",        # 12, 18
        "Function_19_327B",        # 13, 19
        "Function_20_32FC",        # 14, 20
        "Function_21_337D",        # 15, 21
        "Function_22_33FE",        # 16, 22
        "Function_23_347F",        # 17, 23
        "Function_24_3500",        # 18, 24
        "Function_25_3581",        # 19, 25
        "Function_26_3602",        # 1A, 26
        "Function_27_3683",        # 1B, 27
        "Function_28_3704",        # 1C, 28
        "Function_29_3785",        # 1D, 29
        "Function_30_3806",        # 1E, 30
    ))


    def Function_0_304(): pass

    label("Function_0_304")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_344"),
        (1, "loc_350"),
        (2, "loc_35C"),
        (3, "loc_368"),
        (4, "loc_374"),
        (5, "loc_380"),
        (6, "loc_38C"),
        (SWITCH_DEFAULT, "loc_398"),
    )


    label("loc_344")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_350")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_35C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_368")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_374")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_380")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_38C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_398")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3BB")

    Return()

    # Function_0_304 end

    def Function_1_3BC(): pass

    label("Function_1_3BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41C")
    OP_95(0xFE, -106030, 0, 8260, 2000, 0x0)
    OP_95(0xFE, -106030, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 8260, 2000, 0x0)
    Jump("Function_1_3BC")

    label("loc_41C")

    Return()

    # Function_1_3BC end

    def Function_2_41D(): pass

    label("Function_2_41D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47D")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_2_41D")

    label("loc_47D")

    Return()

    # Function_2_41D end

    def Function_3_47E(): pass

    label("Function_3_47E")

    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4C8")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 106130, 0, 11580, 0)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_576")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_521")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 4270, 0, 7670, 90)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 5450, 0, 7670, 270)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51C")
    SetChrFlags(0xC, 0x10)

    label("loc_51C")

    Jump("loc_576")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_52F")
    Jump("loc_576")

    label("loc_52F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_568")
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0x9, -100710, 0, 8860, 270)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_576")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_576")
    ClearChrFlags(0x9, 0x80)

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_585")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)

    label("loc_585")

    Return()

    # Function_3_47E end

    def Function_4_586(): pass

    label("Function_4_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_598")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_598")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_5AF")
    ClearMapObjFlags(0x0, 0x10)
    OP_66(0x0, 0x1)

    label("loc_5AF")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C5")
    OP_66(0x3, 0x1)
    Jump("loc_5D2")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5D2")
    OP_66(0x3, 0x1)

    label("loc_5D2")

    Return()

    # Function_4_586 end

    def Function_5_5D3(): pass

    label("Function_5_5D3")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『恋する休日　厳選レシピ集』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_684")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x15)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_684")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『こだわり抹茶ラテ』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_684")

    TalkEnd(0xFF)
    Return()

    # Function_5_5D3 end

    def Function_6_688(): pass

    label("Function_6_688")

    Call(0, 7)
    Return()

    # Function_6_688 end

    def Function_7_68C(): pass

    label("Function_7_68C")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_699")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1031")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "休憩をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_715")
    OP_AF(0x64)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_102C")

    label("loc_715")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_89F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81E")

    #C0003
    ChrTalk(
        0x8,
        (
            "街での騒ぎも収まったので、\x01",
            "皆でホテルの様子を見に伺った所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "しかし、あの不可解な青白い大樹……\x01",
            "近くで見るとさらに不気味ですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "分かっていたことですが、当面、\x01",
            "ミシュラムの再開は難しいでしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_89A")

    label("loc_81E")


    #C0006
    ChrTalk(
        0x8,
        (
            "ミシュラムの再開はまだ先でしょうが……\x01",
            "折角こうして来ていることです。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "ご休憩の際は、\x01",
            "お気軽にお申し付けください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89A")

    Jump("loc_102C")

    label("loc_89F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_978")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0008
    ChrTalk(
        0x8,
        (
            "おや、ロイド様……\x01",
            "よくお越しくださいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "当ホテルは休業中ですが、\x01",
            "お客様を受け入れる準備は\x01",
            "いつでも整っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "ご休憩の際はお申し付けください。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9EA")

    label("loc_978")


    #C0011
    ChrTalk(
        0x8,
        (
            "ふむ、それにしても、\x01",
            "なぜあのような鐘の音が……？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "ＭＷＬも休業中のはずですが……\x01",
            "どうもおかしいですな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EA")

    Jump("loc_102C")

    label("loc_9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_9FD")
    Jump("loc_102C")

    label("loc_9FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_D3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0A")

    #C0013
    ChrTalk(
        0x8,
        (
            "おお、ロイド様にキーア様。\x01",
            "これはお帰りなさいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        "お会いできたようでなによりです。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x153,
        "#01110Fえへへ、ただいまー。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#00002Fはは、心配かけてすみませんでした。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "いえいえ、滅相もない……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "ああ、先ほどお連れ様方が\x01",
            "お出かけになられたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "各々、用事を済ませてから\x01",
            "待ち合わせ場所へ行くとの事……\x01",
            "急がれた方がいいのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00004Fそうですね、\x01",
            "ありがとうございます。\x02\x03",

            "#00000Fそれじゃあ、\x01",
            "俺たちも用事がすんだら\x01",
            "テーマパークに行こうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x153,
        "#01109Fうん、レッツゴー！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 7)
    Jump("loc_D37")

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC7")

    #C0022
    ChrTalk(
        0x8,
        (
            "先ほどお連れ様方が\x01",
            "お出かけになられたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "各々、用事を済ませてから\x01",
            "待ち合わせ場所へ行くとの事。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "ロイド様たちも、そろそろ\x01",
            "向かわれたほうがいいのでは？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D37")

    label("loc_CC7")


    #C0025
    ChrTalk(
        0x8,
        (
            "先ほどお連れ様方が\x01",
            "お出かけになられたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "ロイド様たちも、そろそろ\x01",
            "向かわれたほうがいいのでは？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D37")

    Jump("loc_102C")

    label("loc_D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_EA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E30")

    #C0027
    ChrTalk(
        0x8,
        (
            "先ほどキーア様がお一人で\x01",
            "お出かけになられたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "念のためお声をおかけしたのですが、\x01",
            "心配なさらぬようにと言われまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#00003F（キーア……\x01",
            "  やっぱりホテルの外を\x01",
            "  探した方がいいかもしれないな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EA0")

    label("loc_E30")


    #C0030
    ChrTalk(
        0x8,
        (
            "先ほどキーア様がお一人で\x01",
            "お出かけになられたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "ふむ、一体どこに\x01",
            "行ってしまわれたのでしょうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA0")

    Jump("loc_102C")

    label("loc_EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_102C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9F")

    #C0032
    ChrTalk(
        0x8,
        (
            "これはこれは皆様……\x01",
            "３階ＶＩＰフロアの使い心地は\x01",
            "いかがですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#00000Fええ、とても快適ですよ。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        "それは何よりです。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "もし至らぬ点がありましたら\x01",
            "すぐにお知らせください。\x01",
            "至急対応させていただきますので。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_102C")

    label("loc_F9F")


    #C0036
    ChrTalk(
        0x8,
        (
            "３階ＶＩＰフロアの使い心地は\x01",
            "いかがですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "もし至らぬ点がありましたら\x01",
            "すぐにお知らせください。\x01",
            "至急対応させていただきますので。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102C")

    Jump("loc_699")

    label("loc_1031")

    TalkEnd(0x8)
    Return()

    # Function_7_68C end

    def Function_8_1035(): pass

    label("Function_8_1035")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_115F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D3")

    #C0038
    ChrTalk(
        0x9,
        (
            "しばらく放っておかれたせいか、\x01",
            "結構ホコリが溜まってるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "はあ……青白い木は不安だけど、\x01",
            "ちゃんと掃除しないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_115A")

    label("loc_10D3")


    #C0040
    ChrTalk(
        0x9,
        (
            "いつでも再開できるように、\x01",
            "定期的に掃除に来てるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "あんな青白い木が\x01",
            "あんな近くにあるんですもの、\x01",
            "どうにも不安よね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115A")

    Jump("loc_159B")

    label("loc_115F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1302")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1268")

    #C0042
    ChrTalk(
        0x9,
        (
            "さっき、国防長官になった\x01",
            "あのアリオスさんが、\x01",
            "アーケードを通ってったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "可愛い小さな女の子を\x01",
            "連れてたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00001F（アリオスさんとキーア……\x01",
            "  やっぱり来てたみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        "#00101F（早く追いかけましょう。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12FD")

    label("loc_1268")


    #C0046
    ChrTalk(
        0x9,
        (
            "さっき、国防長官のアリオスさんが\x01",
            "アーケードを通ってったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "小さな女の子を連れて\x01",
            "テーマパークへ行ったみたいだけど……\x01",
            "一体なんなのかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FD")

    Jump("loc_159B")

    label("loc_1302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1310")
    Jump("loc_159B")

    label("loc_1310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1389")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132B")
    Call(0, 9)
    Jump("loc_1384")

    label("loc_132B")


    #C0048
    ChrTalk(
        0xFE,
        (
            "お願～い、\x01",
            "ワジ様のお世話は私がしたいの～！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "今度ジェラートとかおごるからさ～！\x02",
    )

    CloseMessageWindow()

    label("loc_1384")

    Jump("loc_159B")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_159B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1516")
    TurnDirection(0xFE, 0x105, 0)

    #C0050
    ChrTalk(
        0xFE,
        "あれっ、お客様は……ワジ様！？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "も、もしかして、\x01",
            "今日ＶＩＰフロアに宿泊する\x01",
            "お客様って……？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x105,
        (
            "#10300Fああ、それなら\x01",
            "僕たちだと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "！！！！！！\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "（あ、あたしったら……\x01",
            "  何でこんな日に限って一般フロアの\x01",
            "  担当になっちゃったのよ！！）\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#00005Fな、なんか知らないけど\x01",
            "ショックを受けてるみたいだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        "#10302Fフフ、おかしな子だね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_159B")

    label("loc_1516")


    #C0057
    ChrTalk(
        0xFE,
        (
            "あ、あたしったら……\x01",
            "こんな日に限って一般フロアの\x01",
            "担当になっちゃうなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "ワジ様のお世話ができる\x01",
            "チャンスだったのに～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_159B")

    TalkEnd(0xFE)
    Return()

    # Function_8_1035 end

    def Function_9_159F(): pass

    label("Function_9_159F")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0059
    ChrTalk(
        0x9,
        "ねっ、シトラスお願いっ！\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "今日はあたしにワジ様のいる\x01",
            "ＶＩＰフロアの当番させて～！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "わざわざ仕事中に呼び出して\x01",
            "何かと思えば……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        (
            "だいたい、もとはといえばあんたが\x01",
            "『ＶＩＰフロアのお世話は面倒そう』\x01",
            "とか言って、私に押し付けたんじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "そ、そこをなんとか～。\x01",
            "今度ジェラートとかおごるからさ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_159F end

    def Function_10_16EE(): pass

    label("Function_10_16EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1852")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CA")

    #C0064
    ChrTalk(
        0xA,
        (
            "迎賓館のほうには、\x01",
            "マクダエル議長たちが\x01",
            "監禁されてたらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "しかも、街を襲った猟兵たちに\x01",
            "見張らせてたそうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xA,
        (
            "独立のためとはいえ、\x01",
            "大統領もひどい事をするわよね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_184D")

    label("loc_17CA")


    #C0067
    ChrTalk(
        0xA,
        (
            "迎賓館のほうには、\x01",
            "マクダエル議長たちが\x01",
            "監禁されてたらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "大統領もひどい事をするわよね……\x01",
            "捕まってよかったけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184D")

    Jump("loc_19CF")

    label("loc_1852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_193F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FD")

    #C0069
    ChrTalk(
        0xA,
        (
            "あっちの方に座ってるのって、\x01",
            "テーマパークで働いてる占い師さんよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "いつの間にか現れたみたいだけど……\x01",
            "普段、どこに住んでるのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_193A")

    label("loc_18FD")


    #C0071
    ChrTalk(
        0xA,
        (
            "……おっと、話してないで\x01",
            "さっさと掃除を済ませないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_193A")

    Jump("loc_19CF")

    label("loc_193F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_194D")
    Jump("loc_19CF")

    label("loc_194D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_19C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1968")
    Call(0, 9)
    Jump("loc_19C1")

    label("loc_1968")


    #C0072
    ChrTalk(
        0xFE,
        (
            "もう、そこまで言うなら\x01",
            "代わってあげてもいいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "まったく、勝手なんだから。\x02",
    )

    CloseMessageWindow()

    label("loc_19C1")

    Jump("loc_19CF")

    label("loc_19C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_19CF")

    label("loc_19CF")

    TalkEnd(0xFE)
    Return()

    # Function_10_16EE end

    def Function_11_19D3(): pass

    label("Function_11_19D3")

    Call(0, 12)
    Return()

    # Function_11_19D3 end

    def Function_12_19D7(): pass

    label("Function_12_19D7")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC8")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",            # 0
            "改造・合成する\x01",      # 1
            "やめる\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A44")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1A44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A64")
    OP_AF(0x65)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC3")

    label("loc_1A64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1B1E")

    #C0074
    ChrTalk(
        0xB,
        (
            "あんな得体の知れないもんが\x01",
            "現れてるのに、ここの職員は\x01",
            "なかなかキモが座ってるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        (
            "……メンテを早く済ませて\x01",
            "さっさとここから離れたいぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC3")

    label("loc_1B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1BC3")

    #C0076
    ChrTalk(
        0xB,
        (
            "ちょうどホテルの人たちと、\x01",
            "休業中の設備のメンテナンスに\x01",
            "来てた所でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xB,
        (
            "あんたらも何か用事があったら\x01",
            "遠慮なく言ってくれ。\x01",
            "片手間に手伝ってやるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC3")

    Jump("loc_19E4")

    label("loc_1BC8")

    TalkEnd(0xB)
    Return()

    # Function_12_19D7 end

    def Function_13_1BCC(): pass

    label("Function_13_1BCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_228E")
    Call(0, 14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F11")
    EventBegin(0x0)
    Fade(500)
    OP_68(-13160, 1200, 13150, 0)
    MoveCamera(320, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17640, 0)
    SetChrPos(0x101, -12560, 0, 13000, 0)
    SetChrPos(0x102, -13820, 0, 12710, 45)
    SetChrPos(0x103, -12700, 0, 11800, 0)
    SetChrPos(0x104, -13690, 0, 13610, 45)
    SetChrPos(0xF4, -14000, 0, 11480, 45)
    SetChrPos(0xF5, -14760, 0, 12870, 50)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xC, 0x2)
    OP_0D()

    #C0078
    ChrTalk(
        0xC,
        "#11Pあら、その本は……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xC,
        (
            "#11Pクロスベル市で時々見かける\x01",
            "『陽溜りのアニエス』ではないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#6P#00005Fえっと、この小説のことですか？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        "#6P#00100F一応、全巻集まってるのよね。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xC,
        "#11Pフフ、素晴らしいわね。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xC,
        (
            "#11P以前、私もその小説を\x01",
            "手に取る機会があってね。\x01",
            "とても楽しんで読ませてもらったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xC,
        (
            "#11P作り話ではあるようだけど……\x01",
            "主人公の少女にどこか通じるものが\x01",
            "あったのかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xC,
        (
            "#11Pクロスベルの事件の結末、\x01",
            "ここから傍観させてもらう\x01",
            "つもりだったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xC,
        (
            "#11Pそんな本を読みながら、\x01",
            "というのもいいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#6P#00004F（折角だから、この人に\x01",
            "  差し上げようかな……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18A, 5)
    Call(0, 15)
    Jump("loc_2289")

    label("loc_1F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20B9")
    EventBegin(0x0)
    Fade(500)
    OP_68(-13160, 1200, 13150, 0)
    MoveCamera(320, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17640, 0)
    SetChrPos(0x101, -12560, 0, 13000, 0)
    SetChrPos(0x102, -13820, 0, 12710, 45)
    SetChrPos(0x103, -12700, 0, 11800, 0)
    SetChrPos(0x104, -13690, 0, 13610, 45)
    SetChrPos(0xF4, -14000, 0, 11480, 45)
    SetChrPos(0xF5, -11330, 0, 11290, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xC, 0x2)
    OP_0D()

    #C0088
    ChrTalk(
        0xC,
        (
            "#11Pそれは、クロスベル市で時々見かける\x01",
            "『陽溜りのアニエス』という本ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        (
            "#11Pクロスベルの事件の結末、\x01",
            "ここから傍観させてもらう\x01",
            "つもりだったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xC,
        (
            "#11Pそんな本を読みながら、\x01",
            "というのもいいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 15)
    Jump("loc_2289")

    label("loc_20B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E5")

    #C0091
    ChrTalk(
        0xC,
        (
            "あの碧き大樹……\x01",
            "これほどのものが出現するとはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        (
            "タロット、水晶、星見……\x01",
            "私の持つあらゆる方法を用いても、\x01",
            "この先の運命を占うことができない。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xC,
        (
            "フフ、面白い……\x01",
            "こんな事は初めてだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xC,
        (
            "この先クロスベルが\x01",
            "どんな未来を掴むのか……\x01",
            "ここで見届けさせてもらいましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2289")

    label("loc_21E5")


    #C0095
    ChrTalk(
        0xC,
        (
            "フフ……“彼ら”も\x01",
            "ここまでの事態になるとは\x01",
            "思いも寄らなかったでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xC,
        (
            "この先クロスベルが\x01",
            "どんな未来を掴むのか……\x01",
            "ここで見届けさせてもらいましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2289")

    Jump("loc_28EF")

    label("loc_228E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_28EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279E")

    #C0097
    ChrTalk(
        0xC,
        "ふむ…………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_235C")

    #C0098
    ChrTalk(
        0x101,
        (
            "#00005F（この人は……\x01",
            "  テーマパークの占い師さんか？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_237B")

    label("loc_235C")


    #C0099
    ChrTalk(
        0x101,
        "#00005F（この人は……？）\x02",
    )

    CloseMessageWindow()

    label("loc_237B")


    #C0100
    ChrTalk(
        0x102,
        (
            "#00105F（タロットカードを\x01",
            "  広げているみたいだけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_244A")
    Jump("loc_2494")

    label("loc_244A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_246A")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2494")

    label("loc_246A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_248A")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2494")

    label("loc_248A")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2494")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    #C0101
    ChrTalk(
        0xC,
        "……気をつけなさい。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xC,
        (
            "この先に進むつもりなら……\x01",
            "恐らくあなたたちは、壮絶なる\x01",
            "困難の道を歩む事になるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0103
    ChrTalk(
        0x103,
        "#00201F………………！？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x104,
        "#00305Fど、どういう意味ッスか……？\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xC,
        (
            "さて……この難解な配置を\x01",
            "どう読み解いたものか……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xC,
        (
            "ただ、この先に進むのなら\x01",
            "覚悟を決めたほうがいいでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xC,
        (
            "あらゆる困難と相対しても\x01",
            "大切な物を護り抜いていけるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xC,
        (
            "それはあなたたち自身に\x01",
            "かかっているでしょうから。\x02",
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

    #C0109
    ChrTalk(
        0x101,
        (
            "#00003F……よく分かりませんが……\x01",
            "心に留めておきたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xC,
        "フフ、健闘を祈らせていただくわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x191, 7)
    SetChrSubChip(0xC, 0x0)
    Jump("loc_28EF")

    label("loc_279E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288A")

    #C0111
    ChrTalk(
        0xC,
        (
            "この先に進むのなら\x01",
            "覚悟を決めたほうがいいでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xC,
        (
            "あらゆる困難と相対しても\x01",
            "大切な物を護り抜いていけるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xC,
        (
            "それはあなたたち自身に\x01",
            "かかっているでしょうから。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xC,
        "フフ、健闘を祈らせていただくわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_28EF")

    label("loc_288A")


    #C0115
    ChrTalk(
        0xC,
        (
            "あらゆる困難と相対しても\x01",
            "大切な物を護り抜いていけるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xC,
        "フフ、健闘を祈らせていただくわ。\x02",
    )

    CloseMessageWindow()

    label("loc_28EF")

    TalkEnd(0xFE)
    Return()

    # Function_13_1BCC end

    def Function_14_28F3(): pass

    label("Function_14_28F3")

    ClearScenarioFlags(0x0, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2EE, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2EF, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F0, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F2, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F3, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F4, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F5, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F6, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F8, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2F9, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2FA, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2FB, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2952")
    SetScenarioFlags(0x0, 5)

    label("loc_2952")

    Return()

    # Function_14_28F3 end

    def Function_15_2953(): pass

    label("Function_15_2953")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "小説を渡す\x01",      # 0
            "渡さない\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E5E")

    #C0117
    ChrTalk(
        0x101,
        (
            "#6P#00000Fよろしければ……\x01",
            "この本、お譲りしましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xC,
        "#11Pあら……いいのかしら。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x103,
        (
            "#6P#00200Fロイドさんがそういうなら……\x01",
            "もともと殆どが貰い物ですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x104,
        "#6P#00300F遠慮せずに受け取ってくださいッス。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xC,
        (
            "#11Pフフ、それじゃあありがたく\x01",
            "受け取らせていただくわね。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0122
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "陽溜りのアニエスを全て渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SubItemNumber(0x2EE, 1)
    SubItemNumber(0x2EF, 1)
    SubItemNumber(0x2F0, 1)
    SubItemNumber(0x2F1, 1)
    SubItemNumber(0x2F2, 1)
    SubItemNumber(0x2F3, 1)
    SubItemNumber(0x2F4, 1)
    SubItemNumber(0x2F5, 1)
    SubItemNumber(0x2F6, 1)
    SubItemNumber(0x2F7, 1)
    SubItemNumber(0x2F8, 1)
    SubItemNumber(0x2F9, 1)
    SubItemNumber(0x2FA, 1)
    SubItemNumber(0x2FB, 1)

    #C0123
    ChrTalk(
        0xC,
        "#11P……そうね。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xC,
        (
            "#11P代わりと言っては何だけど、\x01",
            "あなたたちにこれを差し上げましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0125
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x396),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x396, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0126
    ChrTalk(
        0x101,
        "#6P#00005Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xC,
        (
            "#11P以前、あるツテから\x01",
            "手に入れたものなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xC,
        (
            "#11Pあなたたちに扱えるかは\x01",
            "分からないけれど……\x01",
            "よければ持っておきなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#6P#00105Fえっと、いいんですか？\x01",
            "こんな貴重そうなものを……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xC,
        "#11Pフフ、構わないわ。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xC,
        (
            "#11Pクロスベルに事件が渦巻く中で、\x01",
            "今回の私は、あくまで傍観者……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xC,
        (
            "#11Pこの程度の介入なら\x01",
            "誰にも文句は言われないでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0133
    ChrTalk(
        0xC,
        "#11Pフフ……こちらの話よ。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xC,
        "#11Pよかったら大事にしてちょうだい。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#6P#00000Fえっと、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x18A, 6)
    Jump("loc_2E91")

    label("loc_2E5E")


    #C0136
    ChrTalk(
        0x101,
        "#6P#00000F（うーん、やっぱりやめておくか。）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2E91")

    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -12560, 0, 13000, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_15_2953 end

    def Function_16_2EC1(): pass

    label("Function_16_2EC1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08500.itc", 0x1F)
    LoadChrToIndex("chr/ch05200.itc", 0x20)
    LoadChrToIndex("chr/ch05100.itc", 0x21)
    LoadChrToIndex("chr/ch07500.itc", 0x22)
    LoadChrToIndex("chr/ch10000.itc", 0x23)
    LoadChrToIndex("chr/ch05500.itc", 0x24)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x102, 0, 0, 0, 0)
    SetChrPos(0x103, 0, 0, 0, 0)
    SetChrPos(0x104, 0, 0, 0, 0)
    SetChrPos(0x109, 0, 0, 0, 0)
    SetChrPos(0x105, 0, 0, 0, 0)
    SetChrPos(0xD, 0, 0, 0, 0)
    SetChrPos(0xE, 0, 0, 0, 0)
    SetChrPos(0x10, 0, 0, 0, 0)
    SetChrPos(0xF, 0, 0, 0, 0)
    SetChrPos(0x11, 0, 0, 0, 0)
    SetChrPos(0x12, 0, 0, 0, 0)
    SetChrPos(0x13, 0, 0, 0, 0)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    ClearMapObjFlags(0x0, 0x10)
    OP_68(4140, 1000, 8840, 0)
    MoveCamera(315, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23500, 0)
    FadeToBright(1000, 0)
    OP_68(5450, 1000, 10150, 6000)
    BeginChrThread(0x13, 3, 0, 17)
    BeginChrThread(0x10, 3, 0, 18)
    BeginChrThread(0xF, 3, 0, 19)
    BeginChrThread(0xE, 3, 0, 20)
    BeginChrThread(0x11, 3, 0, 22)
    BeginChrThread(0x12, 3, 0, 23)
    BeginChrThread(0xD, 3, 0, 24)
    BeginChrThread(0x102, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 26)
    BeginChrThread(0x109, 3, 0, 21)
    BeginChrThread(0x105, 3, 0, 29)
    BeginChrThread(0x101, 3, 0, 27)
    BeginChrThread(0x104, 3, 0, 28)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0x10, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    SetMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t1080", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2EC1 end

    def Function_17_317E(): pass

    label("Function_17_317E")

    SetChrPos(0xFE, 3500, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0xFFD3, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x10CC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x3E8, 0x7D0, 0x1)
    Sound(121, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x0)

    def lambda_31DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31DA)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_317E end

    def Function_18_31FA(): pass

    label("Function_18_31FA")

    SetChrPos(0xFE, 1300, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_325B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_325B)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_31FA end

    def Function_19_327B(): pass

    label("Function_19_327B")

    SetChrPos(0xFE, 1300, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_32DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32DC)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_19_327B end

    def Function_20_32FC(): pass

    label("Function_20_32FC")

    SetChrPos(0xFE, -600, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1518, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_335D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_335D)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_20_32FC end

    def Function_21_337D(): pass

    label("Function_21_337D")

    SetChrPos(0xFE, -600, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1518, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_33DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33DE)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_21_337D end

    def Function_22_33FE(): pass

    label("Function_22_33FE")

    SetChrPos(0xFE, -2500, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_345F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_345F)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_33FE end

    def Function_23_347F(): pass

    label("Function_23_347F")

    SetChrPos(0xFE, -2500, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_34E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_34E0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_347F end

    def Function_24_3500(): pass

    label("Function_24_3500")

    SetChrPos(0xFE, -4400, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3561():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3561)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_24_3500 end

    def Function_25_3581(): pass

    label("Function_25_3581")

    SetChrPos(0xFE, -6300, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2C88, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_35E2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_35E2)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_25_3581 end

    def Function_26_3602(): pass

    label("Function_26_3602")

    SetChrPos(0xFE, -6300, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2C88, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3663():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3663)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_26_3602 end

    def Function_27_3683(): pass

    label("Function_27_3683")

    SetChrPos(0xFE, -8200, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x33F4, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_36E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36E4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_27_3683 end

    def Function_28_3704(): pass

    label("Function_28_3704")

    SetChrPos(0xFE, -10100, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x3B60, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_3765():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3765)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_28_3704 end

    def Function_29_3785(): pass

    label("Function_29_3785")

    SetChrPos(0xFE, -10100, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x3B60, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_37E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_37E6)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_29_3785 end

    def Function_30_3806(): pass

    label("Function_30_3806")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0137
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　 ～階段室～\x01",
            "３階のＶＩＰフロアは\x01",
            "貸し切りとなっております。\x01",
            "立ち入りはご遠慮下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_30_3806 end

    SaveToFile()

Try(main)
