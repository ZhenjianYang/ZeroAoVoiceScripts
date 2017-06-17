from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c017c.bin",                # FileName
        "c017c",                    # MapName
        "c017c",                    # Location
        0x0005,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 5, 0, 2, 0, 3],
    )

    BuildStringList((
        "c017c",                  # 0
        "受付嬢パール",           # 1
        "受付嬢シンシア",         # 2
        "ハンソン",               # 3
        "リジョン",               # 4
        "プラダ",                 # 5
        "ベイカー",               # 6
        "サザーク",               # 7
        "ダドリー捜査官",         # 8
        "ネストン支配人",         # 9
        "ジャネッタ",             # 10
        "バッジョ",               # 11
        "ドロテ",                 # 12
        "ケン",                   # 13
        "オネスト老人",           # 14
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
        "chr/ch00900.itc",                   # 0A
        "chr/ch34600.itc",                   # 0B
        "chr/ch25900.itc",                   # 0C
    ))

    DeclNpc(7480,    0,       10079,   225,  257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5880,    0,       11680,   225,  257,  0x0, 0,   11,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(59,      8000,    30040,   180,  257,  0x0, 0,   12,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(15979,   0,       9520,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(18110,   8000,    12220,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-11529,  8000,    8510,    225,  257,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-15989,  0,       25739,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-5250,   8000,    5360,    360,  385,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-2660,   0,       9829,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-6659,   8000,    28870,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(14930,   0,       2589,    90,   257,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(13800,   8000,    6199,    225,  257,  0x0, 0,   6,   0,   0,   1,   0,   22,  255,  0)
    DeclNpc(8020,    8000,    17270,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-14449,  8000,    14420,   90,   257,  0x0, 0,   9,   0,   0,   0,   0,   24,  255,  0)

    DeclActor(6250,    0,       9040,    1000,    7480,    1500,    10080,   0x007E, 0,  4,  0x0000)
    DeclActor(4440,    0,       10280,   1000,    5880,    1500,    11680,   0x007E, 0,  6,  0x0000)
    DeclActor(-480,    8000,    28360,   1000,    60,      9500,    30040,   0x007E, 0,  8,  0x0000)
    DeclActor(15980,   0,       7760,    1000,    15980,   1500,    9520,    0x007E, 0,  10, 0x0000)
    DeclActor(16480,   8000,    11730,   1000,    18110,   9500,    12220,   0x007E, 0,  12, 0x0000)
    DeclActor(-12390,  8000,    7660,    1000,    -11530,  9500,    8510,    0x007E, 0,  14, 0x0000)
    DeclActor(-16030,  0,       23800,   1000,    -15990,  1500,    25740,   0x007E, 0,  16, 0x0000)
    DeclActor(1670,    0,       13270,   800,     1670,    1500,    13270,   0x007C, 0,  26, 0x0000)

    ScpFunction((
        "Function_0_3E0",          # 00, 0
        "Function_1_498",          # 01, 1
        "Function_2_571",          # 02, 2
        "Function_3_60F",          # 03, 3
        "Function_4_63F",          # 04, 4
        "Function_5_643",          # 05, 5
        "Function_6_EEC",          # 06, 6
        "Function_7_EF0",          # 07, 7
        "Function_8_18C2",         # 08, 8
        "Function_9_18C6",         # 09, 9
        "Function_10_1E9F",        # 0A, 10
        "Function_11_1EA3",        # 0B, 11
        "Function_12_2345",        # 0C, 12
        "Function_13_2349",        # 0D, 13
        "Function_14_28EB",        # 0E, 14
        "Function_15_28EF",        # 0F, 15
        "Function_16_308E",        # 10, 16
        "Function_17_3092",        # 11, 17
        "Function_18_363D",        # 12, 18
        "Function_19_39E5",        # 13, 19
        "Function_20_434C",        # 14, 20
        "Function_21_47C5",        # 15, 21
        "Function_22_4BDC",        # 16, 22
        "Function_23_4ED6",        # 17, 23
        "Function_24_549E",        # 18, 24
        "Function_25_5802",        # 19, 25
        "Function_26_58AB",        # 1A, 26
        "Function_27_59C3",        # 1B, 27
    ))


    def Function_0_3E0(): pass

    label("Function_0_3E0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_420"),
        (1, "loc_42C"),
        (2, "loc_438"),
        (3, "loc_444"),
        (4, "loc_450"),
        (5, "loc_45C"),
        (6, "loc_468"),
        (SWITCH_DEFAULT, "loc_474"),
    )


    label("loc_420")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_42C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_438")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_444")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_450")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_45C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_468")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_474")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_480")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_497")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_497")

    Return()

    # Function_0_3E0 end

    def Function_1_498(): pass

    label("Function_1_498")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_570")
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
    Jump("Function_1_498")

    label("loc_570")

    Return()

    # Function_1_498 end

    def Function_2_571(): pass

    label("Function_2_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_590")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_5F8")

    label("loc_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_59E")
    Jump("loc_5F8")

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5AC")
    Jump("loc_5F8")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_5CB")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_5F8")

    label("loc_5CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5EA")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_5F8")

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5F8")
    ClearChrFlags(0xF, 0x80)

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60E")
    SetMapFlags(0x10000000)
    Event(0, 27)

    label("loc_60E")

    Return()

    # Function_2_571 end

    def Function_3_60F(): pass

    label("Function_3_60F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_630")
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    Jump("loc_63E")

    label("loc_630")

    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)

    label("loc_63E")

    Return()

    # Function_3_60F end

    def Function_4_63F(): pass

    label("Function_4_63F")

    Call(0, 5)
    Return()

    # Function_4_63F end

    def Function_5_643(): pass

    label("Function_5_643")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6A5")

    #C0001
    ChrTalk(
        0x8,
        (
            "スコットさん、来週もなんだか\x01",
            "出張が入っているらしいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "……はぁ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EE8")

    label("loc_6A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_7F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77D")
    OP_4B(0x9, 0xFF)

    #C0003
    ChrTalk(
        0x8,
        (
            "……先輩のため息つくところ、\x01",
            "みちゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "う～ん、先輩みたいな大人の女性は\x01",
            "セクシーさが違いますね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0005
    ChrTalk(
        0x9,
        (
            "お、お客様になに言ってるんですか\x01",
            "パールさん……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_7F3")

    label("loc_77D")


    #C0006
    ChrTalk(
        0x8,
        (
            "先輩みたいな大人の女性は\x01",
            "ため息ひとつとっても\x01",
            "セクシーさが違いますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "なんで男の人は先輩をほっとくかな～。\x02",
    )

    CloseMessageWindow()

    label("loc_7F3")

    Jump("loc_EE8")

    label("loc_7F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_B23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA4")
    OP_4B(0x9, 0xFF)

    #C0008
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人たちなら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0010
    ChrTalk(
        0x8,
        "迷子、ですか……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    #C0011
    ChrTalk(
        0x9,
        (
            "あら、迷子なんて……\x01",
            "それは心配ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x9,
        (
            "でも私は\x01",
            "心当たりが無いようです。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_927():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_927)

    def lambda_934():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_934)
    WaitChrThread(0x8, 2)

    #C0013
    ChrTalk(
        0x9,
        "パール、あなたは見かけなかった？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "ええ……私も\x01",
            "覚えはないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "パレードが通過する頃に\x01",
            "何人かお子さんもいましたけど……\x01",
            "みんな親御さん連れでしたし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9EE():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9EE)

    def lambda_9FB():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9FB)
    WaitChrThread(0x8, 2)

    #C0016
    ChrTalk(
        0x9,
        (
            "申し訳ありません、\x01",
            "当百貨店にはいらっしゃって\x01",
            "いないかと存じます。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#0000Fそうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    OP_93(0x9, 0xE1, 0x0)
    OP_4C(0x9, 0xFF)
    Jump("loc_B1E")

    label("loc_AA4")


    #C0018
    ChrTalk(
        0x8,
        (
            "当百貨店にいらっしゃったお子様は\x01",
            "皆さん親御さん連れだったはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "お探しのお子様は\x01",
            "見かけてないと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1E")

    Jump("loc_EE8")

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_C76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFB")
    OP_4B(0x9, 0xFF)

    #C0020
    ChrTalk(
        0x8,
        (
            "……先輩のため息つくところ、\x01",
            "みちゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "う～ん、先輩みたいな大人の女性は\x01",
            "セクシーさが違いますね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0022
    ChrTalk(
        0x9,
        (
            "お、お客様になに言ってるんですか\x01",
            "パールさん……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_C71")

    label("loc_BFB")


    #C0023
    ChrTalk(
        0x8,
        (
            "先輩みたいな大人の女性は\x01",
            "ため息ひとつとっても\x01",
            "セクシーさが違いますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "なんで男の人は先輩をほっとくかな～。\x02",
    )

    CloseMessageWindow()

    label("loc_C71")

    Jump("loc_EE8")

    label("loc_C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D26")

    #C0025
    ChrTalk(
        0x8,
        (
            "支配人の企画は、\x01",
            "従業員にとっては結構厳しいものも\x01",
            "多いんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "それでもついていけるのは、\x01",
            "支配人の企画なら結果が出るっていう\x01",
            "確信があるからなんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE8")

    label("loc_D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_DA0")

    #C0027
    ChrTalk(
        0x8,
        (
            "昨日、迷子の子供がいて\x01",
            "大変だったんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "やっぱり、人が多いと\x01",
            "トラブルが起きやすいですねぇ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE8")

    label("loc_DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E35")

    #C0029
    ChrTalk(
        0x8,
        (
            "先輩は女の子に憧れられる\x01",
            "タイプですから、\x01",
            "女友達が結構多いんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "……男の人とのいい話も\x01",
            "聞いてみたいんですけどねぇ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE8")

    label("loc_E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_EE8")

    #C0031
    ChrTalk(
        0x8,
        (
            "私、以前スコットさんと\x01",
            "ミシュラムでデートしたときに\x01",
            "みっしぃを見たことがあるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "みっしぃって、\x01",
            "とても可愛らしいんですよ。\x01",
            "ふふ、いつか会ってみてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE8")

    TalkEnd(0x8)
    Return()

    # Function_5_643 end

    def Function_6_EEC(): pass

    label("Function_6_EEC")

    Call(0, 7)
    Return()

    # Function_6_EEC end

    def Function_7_EF0(): pass

    label("Function_7_EF0")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F88")

    #C0033
    ChrTalk(
        0x9,
        "ようこそ、百貨店《タイムズ》へ。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        "本日は夜の２３時まで開店しております。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "どうぞごゆっくり、\x01",
            "買い物をお楽しみ下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BE")

    label("loc_F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_10DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1048")

    #C0036
    ChrTalk(
        0x9,
        "ふぅ……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "あら、失礼しました。\x01",
            "お客様の前でため息だなんて\x01",
            "私も疲労が溜まっているんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "こんなときこそ息抜きに\x01",
            "ジョギングでもしたいところです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_10D7")

    label("loc_1048")


    #C0039
    ChrTalk(
        0x9,
        (
            "記念祭が終わって休みがとれたら、\x01",
            "市内をぐるっとジョギングして\x01",
            "過ごしたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "休日の使い方なんてそんなものですよ。\x01",
            "独身ですし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D7")

    Jump("loc_18BE")

    label("loc_10DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1398")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132D")
    OP_4B(0x8, 0xFF)

    #C0041
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人たちなら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0043
    ChrTalk(
        0x9,
        (
            "あら、迷子なんて……\x01",
            "それは心配ですね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11B0():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_11B0)

    def lambda_11BD():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11BD)
    WaitChrThread(0x8, 2)

    #C0044
    ChrTalk(
        0x9,
        "パール、あなたは見かけなかった？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "ええ……私も\x01",
            "覚えはないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "パレードが通過する頃に\x01",
            "何人かお子さんもいましたけど……\x01",
            "みんな親御さん連れでしたし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1277():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1277)

    def lambda_1284():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1284)
    WaitChrThread(0x8, 2)

    #C0047
    ChrTalk(
        0x9,
        (
            "申し訳ありません、\x01",
            "当百貨店にはいらっしゃって\x01",
            "いないかと存じます。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#0000Fそうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    OP_93(0x8, 0xE1, 0x0)
    OP_4C(0x8, 0xFF)
    Jump("loc_1393")

    label("loc_132D")


    #C0049
    ChrTalk(
        0x9,
        "私も覚えはないですね……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "申し訳ありません、\x01",
            "当百貨店にはいらっしゃって\x01",
            "いないかと存じます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1393")

    Jump("loc_18BE")

    label("loc_1398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_14EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1458")

    #C0051
    ChrTalk(
        0x9,
        "ふぅ……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "あら、失礼しました。\x01",
            "お客様の前でため息だなんて\x01",
            "私も疲労が溜まっているんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "こんなときこそ息抜きに\x01",
            "ジョギングでもしたいところです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_14E7")

    label("loc_1458")


    #C0054
    ChrTalk(
        0x9,
        (
            "記念祭が終わって休みがとれたら、\x01",
            "市内をぐるっとジョギングして\x01",
            "過ごしたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "休日の使い方なんてそんなものですよ。\x01",
            "独身ですし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E7")

    Jump("loc_18BE")

    label("loc_14EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_15A3")

    #C0056
    ChrTalk(
        0x9,
        (
            "記念祭最終日に向けて、支配人は\x01",
            "新しい企画を用意しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "支配人の企画はいつも\x01",
            "お客様に支持される素敵なものばかりです。\x01",
            "今回も期待していていいと思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BE")

    label("loc_15A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1648")

    #C0058
    ChrTalk(
        0x9,
        (
            "旅行中の不足品などがありましたら\x01",
            "是非当店にお越しください。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "百貨店《タイムズ》は、\x01",
            "必ずお客様のご希望の品を\x01",
            "取り揃えてお待ちしておりますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BE")

    label("loc_1648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1829")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1760")

    #C0060
    ChrTalk(
        0x9,
        (
            "以前からクロスベルに来ている\x01",
            "遊撃士のエステルさんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "彼女もストレガー社の\x01",
            "スニーカーのファンなんだそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "私も、ジョギングが趣味で\x01",
            "スニーカーには目がなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "ふふ、私とした事が\x01",
            "すっかりお客様と意気投合して\x01",
            "しまいました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1824")

    label("loc_1760")


    #C0064
    ChrTalk(
        0x9,
        (
            "遊撃士のエステルさんも\x01",
            "ストレガー社のファンだそうで、\x01",
            "すっかり意気投合してしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "公私混同は気を付けたいところですが……\x01",
            "ふふ、同じ趣味の方を見つけられて\x01",
            "とても嬉しい気持ちです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1824")

    Jump("loc_18BE")

    label("loc_1829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_18BE")

    #C0066
    ChrTalk(
        0x9,
        (
            "昨日のイベントには、\x01",
            "多くの家族連れのお客様も\x01",
            "いらっしゃっていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "みっしいの登場には、\x01",
            "子供さんたちが\x01",
            "大変喜んでいましたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BE")

    TalkEnd(0x9)
    Return()

    # Function_7_EF0 end

    def Function_8_18C2(): pass

    label("Function_8_18C2")

    Call(0, 9)
    Return()

    # Function_8_18C2 end

    def Function_9_18C6(): pass

    label("Function_9_18C6")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E9B")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1931")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1931")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1961")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1950")
    OP_AF(0x22)
    Jump("loc_1952")

    label("loc_1950")

    OP_AF(0x21)

    label("loc_1952")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E96")

    label("loc_1961")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1975")
    Jump("loc_1E96")

    label("loc_1975")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E96")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A35")

    #C0068
    ChrTalk(
        0xA,
        (
            "プラダさんに売り上げ勝負を\x01",
            "持ち掛けられていたことを\x01",
            "すっかり忘れていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        (
            "いやはや、商売に熱中すると\x01",
            "勝敗などはどうでも良くなるものですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E96")

    label("loc_1A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1AC2")

    #C0070
    ChrTalk(
        0xA,
        (
            "ハイヒールは女性らしさを\x01",
            "際立たせる靴です。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        (
            "運動には向きませんが、\x01",
            "社交パーティなどの場には\x01",
            "必ず用いられるのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E96")

    label("loc_1AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1BAE")

    #C0072
    ChrTalk(
        0xA,
        (
            "ストレガー社製の靴は\x01",
            "マニアの間で大人気なのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        (
            "運動性とスタイリッシュさを併せ持ち、\x01",
            "頑丈で長持ちとくれば\x01",
            "人気が出るのも当然でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "ちなみに、遊撃士のエステルさんも\x01",
            "ストレガー社のファンらしいですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E96")

    label("loc_1BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1C6E")

    #C0075
    ChrTalk(
        0xA,
        (
            "クロスベルについてから、\x01",
            "動きやすいサンダルなどを\x01",
            "購入する方を見かけます。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xA,
        (
            "こちらで取り扱っている靴は\x01",
            "ほとんどがクロスベルの地形に適した\x01",
            "性能ですから、おすすめですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E96")

    label("loc_1C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D17")

    #C0077
    ChrTalk(
        0xA,
        (
            "たまに休み時間などに、\x01",
            "シンシアさんがジョギング用のシューズを\x01",
            "のぞきにくるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "ジョギングは若い女性にとって\x01",
            "大変健康的でよろしいことですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E96")

    label("loc_1D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1E96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E07")

    #C0079
    ChrTalk(
        0xA,
        (
            "プラダさんから、\x01",
            "記念祭中の売り上げ競争を\x01",
            "持ち掛けられましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        (
            "平常時の売り上げから\x01",
            "何％増できるかといったものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "個人経営時代、プラダさんとはよく\x01",
            "そんな争いをして\x01",
            "互いを高めあったものですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E96")

    label("loc_1E07")


    #C0082
    ChrTalk(
        0xA,
        (
            "プラダさんから、\x01",
            "記念祭中の売り上げ競争を\x01",
            "持ち掛けられましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "もちろん、受けて立つ予定です。\x01",
            "ふふ、個人経営時代を思い出しますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E96")

    Jump("loc_18D3")

    label("loc_1E9B")

    TalkEnd(0xA)
    Return()

    # Function_9_18C6 end

    def Function_10_1E9F(): pass

    label("Function_10_1E9F")

    Call(0, 11)
    Return()

    # Function_10_1E9F end

    def Function_11_1EA3(): pass

    label("Function_11_1EA3")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2341")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1F0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F2E")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_233C")

    label("loc_1F2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F42")
    Jump("loc_233C")

    label("loc_1F42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_233C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1FC3")

    #C0084
    ChrTalk(
        0xB,
        (
            "さあ、今日も\x01",
            "気合入れて行きましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xB,
        (
            "まだまだ娘には\x01",
            "負けてられませんからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233C")

    label("loc_1FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_201A")

    #C0086
    ChrTalk(
        0xB,
        "いらっしゃいませ～！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xB,
        (
            "やれやれ、お客さんが\x01",
            "どっと増えましたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233C")

    label("loc_201A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_20D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208A")

    #C0088
    ChrTalk(
        0xB,
        (
            "ジャネッタちゃん、\x01",
            "今日は上の空みたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        "何をしているのかしらねえ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_20CC")

    label("loc_208A")


    #C0090
    ChrTalk(
        0xB,
        (
            "ジャネッタちゃんは\x01",
            "変わった子ねえ。\x01",
            "時々心配になっちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CC")

    Jump("loc_233C")

    label("loc_20D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_21F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2175")

    #C0091
    ChrTalk(
        0xB,
        (
            "さっきのお客さんときたら\x01",
            "ワインを半ダースも\x01",
            "買っていかれたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xB,
        (
            "ふう……お祭りだからって。\x01",
            "みんな飲みすぎじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_21EC")

    label("loc_2175")


    #C0093
    ChrTalk(
        0xB,
        (
            "お祭りだからって\x01",
            "皆さんお酒を\x01",
            "買い込んでいかれるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xB,
        (
            "ふう、飲みすぎじゃないかって\x01",
            "心配してしまいますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21EC")

    Jump("loc_233C")

    label("loc_21F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_226D")

    #C0095
    ChrTalk(
        0xB,
        (
            "こちらのフルーツの詰め合わせは\x01",
            "ご家庭のパーティに使えますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xB,
        (
            "どうぞどうぞ、\x01",
            "見ていってくださ～い。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233C")

    label("loc_226D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_233C")

    #C0097
    ChrTalk(
        0xB,
        (
            "《リジョンフード》の\x01",
            "コーナーへようこそ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xB,
        (
            "こちら帝国産の燻製肉は\x01",
            "ハムサンドに最適ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xB,
        (
            "アルモリカ産のレタスを使えば\x01",
            "しゃきしゃきサンドができあがりです。\x01",
            "記念祭の軽食にいかが～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_233C")

    Jump("loc_1EB0")

    label("loc_2341")

    TalkEnd(0xB)
    Return()

    # Function_11_1EA3 end

    def Function_12_2345(): pass

    label("Function_12_2345")

    Call(0, 13)
    Return()

    # Function_12_2345 end

    def Function_13_2349(): pass

    label("Function_13_2349")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2356")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E7")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_23B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_23D3")
    OP_AF(0x1F)
    Jump("loc_23D5")

    label("loc_23D3")

    OP_AF(0x1E)

    label("loc_23D5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28E2")

    label("loc_23E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23F8")
    Jump("loc_28E2")

    label("loc_23F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_253E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A6")

    #C0100
    ChrTalk(
        0xC,
        (
            "ハンソンさんったら、\x01",
            "売り上げ勝負のことを\x01",
            "すっかり忘れていましたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xC,
        "もう、昔と変わらずマイペースなんだから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2539")

    label("loc_24A6")


    #C0102
    ChrTalk(
        0xC,
        (
            "でも、まぁ……形式的にも\x01",
            "勝負という形にしたおかげで\x01",
            "大分楽しかったですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xC,
        (
            "勝負を受けてくれたハンソンさんには\x01",
            "感謝しないとけませんわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2539")

    Jump("loc_28E2")

    label("loc_253E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_25D9")

    #C0104
    ChrTalk(
        0xC,
        (
            "クロスベルの方々は\x01",
            "なかなかのセンスをして\x01",
            "いらっしゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xC,
        (
            "どんどん最先端の流行をとりいれて\x01",
            "お客様を飽きさせないようにしないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E2")

    label("loc_25D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_26AF")

    #C0106
    ChrTalk(
        0xC,
        (
            "帝国の富裕層の服装は\x01",
            "余り好きになれませんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xC,
        (
            "たしかに質の良い立派な服ですけど、\x01",
            "どの方もなんだか\x01",
            "似たり寄ったりなんですもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xC,
        (
            "やはり、多少はオリジナリティを\x01",
            "追求して欲しいものですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E2")

    label("loc_26AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2781")

    #C0109
    ChrTalk(
        0xC,
        (
            "ファッションとは、\x01",
            "ただ高価なもので着飾れば\x01",
            "いいというわけではありませんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xC,
        (
            "大事なのは全体の調和……\x01",
            "バランスなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xC,
        (
            "ふふ、お客様はそれをよく\x01",
            "分かっていらっしゃるようですわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E2")

    label("loc_2781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_280D")

    #C0112
    ChrTalk(
        0xC,
        (
            "外国の方は、やはり個性的な\x01",
            "ファッションが多いですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xC,
        (
            "ブティックを営むものとして\x01",
            "観光客から学ぶことも多いですわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28E2")

    label("loc_280D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_28E2")

    #C0114
    ChrTalk(
        0xC,
        (
            "ハンソンさんとの売り上げ勝負、\x01",
            "結果が楽しみですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        (
            "思えば、ハンソンさんの店が\x01",
            "ブティックだったころは\x01",
            "ついに勝てませんでした……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xC,
        (
            "勝ち逃げされてしまった屈辱、\x01",
            "今度こそ返して差し上げますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E2")

    Jump("loc_2356")

    label("loc_28E7")

    TalkEnd(0xC)
    Return()

    # Function_13_2349 end

    def Function_14_28EB(): pass

    label("Function_14_28EB")

    Call(0, 15)
    Return()

    # Function_14_28EB end

    def Function_15_28EF(): pass

    label("Function_15_28EF")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_308A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_295A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_295A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_298A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2979")
    OP_AF(0x25)
    Jump("loc_297B")

    label("loc_2979")

    OP_AF(0x24)

    label("loc_297B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3085")

    label("loc_298A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_299E")
    Jump("loc_3085")

    label("loc_299E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3085")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2B37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ABA")

    #C0117
    ChrTalk(
        0xD,
        (
            "記念祭の最終日は特別な日ですから、\x01",
            "この日に想いを伝えようとする方も\x01",
            "多分におられるようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xD,
        (
            "給料の３ヵ月分の指輪を用意して\x01",
            "プロポーズの機会を待つ男性……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xD,
        (
            "いつの時代になっても、\x01",
            "こういう風習は変わらないのでしょうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2B32")

    label("loc_2ABA")


    #C0120
    ChrTalk(
        0xD,
        (
            "給料の３ヵ月分の指輪を用意して\x01",
            "プロポーズの機会を待つ男性……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xD,
        (
            "前時代的な風習ですが、\x01",
            "やはり、いいものですな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B32")

    Jump("loc_3085")

    label("loc_2B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2CF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C4D")

    #C0122
    ChrTalk(
        0xD,
        (
            "以前“怪盗Ｂ”なる泥棒が\x01",
            "帝国に現れた時、不謹慎にも民衆には\x01",
            "彼を応援する声もあったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xD,
        (
            "一部の熱狂的なファンが\x01",
            "かの怪盗への応援メッセージを\x01",
            "通信社に送る始末だったそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xD,
        (
            "盗みの対象となる宝石商にとっては\x01",
            "たまったものではないですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2CEE")

    label("loc_2C4D")


    #C0125
    ChrTalk(
        0xD,
        (
            "以前“怪盗Ｂ”なる泥棒が\x01",
            "帝国に現れた時、不謹慎にも民衆には\x01",
            "彼を応援する声もあったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xD,
        (
            "泥棒風情を英雄視する気持ちなど\x01",
            "私には分かりませんでしたがね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CEE")

    Jump("loc_3085")

    label("loc_2CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2E87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE1")

    #C0127
    ChrTalk(
        0xD,
        (
            "“怪盗Ｂ”なる怪人物を\x01",
            "知っていますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xD,
        (
            "以前帝国で流行った、\x01",
            "曰くつきの美術品だけを狙う\x01",
            "少し変わった泥棒なのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xD,
        (
            "美術商だった頃、\x01",
            "知人も被害にあいましてね。\x01",
            "いやはや、迷惑なヤツもいたものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2E82")

    label("loc_2DE1")


    #C0130
    ChrTalk(
        0xD,
        (
            "“怪盗Ｂ”という怪人物……\x01",
            "噂では、２年前からリベールでも\x01",
            "被害の目撃談が出ているとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xD,
        (
            "……あるいは、このクロスベル市にも\x01",
            "やってくるかもしれませんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E82")

    Jump("loc_3085")

    label("loc_2E87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2F30")

    #C0132
    ChrTalk(
        0xD,
        (
            "最近のクロスベルタイムズは\x01",
            "本当にゴシップっぽいというか、\x01",
            "なんというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        (
            "……それでも読んでしまうのは\x01",
            "なんらかの魅力があるからなんでしょうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3085")

    label("loc_2F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2FA1")

    #C0134
    ChrTalk(
        0xD,
        "旧市街で乱闘騒ぎがあったそうですな。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xD,
        (
            "いやはや、少しは住民の迷惑も\x01",
            "考えて欲しいものです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3085")

    label("loc_2FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3085")

    #C0136
    ChrTalk(
        0xD,
        (
            "毎年この時期は\x01",
            "売り上げがぐんとアップしますな。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xD,
        (
            "当店は中々高価な\x01",
            "装飾品も扱っておりますが、\x01",
            "そこはサイフの紐が緩むと申しますか。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xD,
        (
            "大変結構なことですが、\x01",
            "浮かれすぎて贅を尽くすような真似は\x01",
            "感心しませんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3085")

    Jump("loc_28FC")

    label("loc_308A")

    TalkEnd(0xD)
    Return()

    # Function_15_28EF end

    def Function_16_308E(): pass

    label("Function_16_308E")

    Call(0, 17)
    Return()

    # Function_16_308E end

    def Function_17_3092(): pass

    label("Function_17_3092")

    TalkBegin(0xE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_309F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3639")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30FD")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_30FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_318D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_311C")
    OP_AF(0x1B)
    Jump("loc_317E")

    label("loc_311C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_312C")
    OP_AF(0x1A)
    Jump("loc_317E")

    label("loc_312C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_313C")
    OP_AF(0x19)
    Jump("loc_317E")

    label("loc_313C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_314C")
    OP_AF(0x18)
    Jump("loc_317E")

    label("loc_314C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_315C")
    OP_AF(0x17)
    Jump("loc_317E")

    label("loc_315C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_316C")
    OP_AF(0x16)
    Jump("loc_317E")

    label("loc_316C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_317C")
    OP_AF(0x15)
    Jump("loc_317E")

    label("loc_317C")

    OP_AF(0x14)

    label("loc_317E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3634")

    label("loc_318D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31A1")
    Jump("loc_3634")

    label("loc_31A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3634")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3295")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322D")

    #C0139
    ChrTalk(
        0xE,
        (
            "やあ、今朝は\x01",
            "書籍の新刊が入ってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xE,
        (
            "入荷少数だから\x01",
            "お買い上げはお早めにね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3290")

    label("loc_322D")


    #C0141
    ChrTalk(
        0xE,
        "この本、結構人気なんだよね。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xE,
        (
            "お昼には売り切れそうだから\x01",
            "お買い上げは早めにお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3290")

    Jump("loc_3634")

    label("loc_3295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_32F4")

    #C0143
    ChrTalk(
        0xE,
        (
            "記念祭の間は\x01",
            "立ち読みする人が多いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xE,
        "とほほ……買ってくれないかなぁ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3634")

    label("loc_32F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A0")

    #C0145
    ChrTalk(
        0xE,
        (
            "クロスベルタイムズ、\x01",
            "どうやら記念祭の最終日にも\x01",
            "最新号を出すつもりらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xE,
        (
            "うーん、記者さんも頑張るなぁ。\x01",
            "こっちまで感心しちゃうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3414")

    label("loc_33A0")


    #C0147
    ChrTalk(
        0xE,
        (
            "クロスベルタイムズの最新号が\x01",
            "記念祭最終日にも出るらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xE,
        (
            "君たちも愛読しているなら\x01",
            "気を付けた方がいいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3414")

    Jump("loc_3634")

    label("loc_3419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_34A4")

    #C0149
    ChrTalk(
        0xE,
        (
            "いらっしゃいませ。\x01",
            "何かお求めですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xE,
        (
            "お薬くらいは\x01",
            "常備していた方がいいですよ。\x01",
            "人生、何があるか判りませんからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3634")

    label("loc_34A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_35B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3533")

    #C0151
    ChrTalk(
        0xE,
        (
            "昨日からクロスベルの地図や\x01",
            "バスの時刻表が売れてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xE,
        (
            "クロスベル市以外の地方に\x01",
            "出かける人もいるのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_35AC")

    label("loc_3533")


    #C0153
    ChrTalk(
        0xE,
        (
            "外国の人なんかは\x01",
            "記念祭の間に遊びつくす\x01",
            "つもりらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xE,
        (
            "クロスベル市以外の地方に\x01",
            "出かける人もいるみたいだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35AC")

    Jump("loc_3634")

    label("loc_35B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3634")

    #C0155
    ChrTalk(
        0xE,
        (
            "アルカンシェルのパンフレット、\x01",
            "ようやく再入荷したよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xE,
        (
            "この前から売り切れ続出なんだよね。\x01",
            "ホント、凄い人気だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3634")

    Jump("loc_309F")

    label("loc_3639")

    TalkEnd(0xE)
    Return()

    # Function_17_3092 end

    def Function_18_363D(): pass

    label("Function_18_363D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38FF")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0157
    ChrTalk(
        0xFE,
        "#0600F……またお前たちか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0158
    ChrTalk(
        0x101,
        "#0005Fダ、ダドリー捜査官！？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x102,
        "#0100Fその……奇遇ですね。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x104,
        "#0305F買物かなんかッスか？\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "#0601F……そんな訳が無いだろう！\x01",
            "クロスベル市内の重点警備だ。\x02\x03",

            "#0603F中央広場や大通り、\x01",
            "港湾区など人の集まる場所には\x01",
            "定期的に人を割り振っている。\x02\x03",

            "犯罪者やテロリストなどが\x01",
            "記念祭に紛れ込んでいないか\x01",
            "見極めるためにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#0001Fそ、そうなんですか……\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#0200F意外と地味なところで\x01",
            "働いているんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "#0603Fふう……まあお前たちに\x01",
            "言っても始まらんか。\x02\x03",

            "#0600Fさっさと仕事に戻れ。\x01",
            "色々と雑用を\x01",
            "言い付かっているのだろう？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 6)
    Jump("loc_39E1")

    label("loc_38FF")


    #C0165
    ChrTalk(
        0xFE,
        (
            "#0606F……しかし今年は\x01",
            "バカみたいに人が多いな。\x02\x03",

            "#0608Fテロリストや猟兵団が見たら\x01",
            "狂喜しそうな光景だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#0005F（さすがに心配しすぎだと\x01",
            "  思うけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#0103F（そうね、外国の要人が\x01",
            "  来ているならともかく……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39E1")

    TalkEnd(0xFE)
    Return()

    # Function_18_363D end

    def Function_19_39E5(): pass

    label("Function_19_39E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3C78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE4")

    #C0168
    ChrTalk(
        0xFE,
        (
            "記念祭終了セールといたしまして、\x01",
            "本日はいつもの営業時間より\x01",
            "２時間ほど延長する予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "深夜の百貨店では、\x01",
            "全店舗が感謝を込めたお値段で\x01",
            "商品を提供する予定なのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        "#0100Fう……とても魅力的だけど……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#0000F今日はミシュラム保養地に\x01",
            "外せない用がある……\x02\x03",

            "#0003F……ホント、\x01",
            "付き合わせて悪いな、みんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        (
            "#0300Fなーにセールを逃す程度のことで\x01",
            "深刻になってんだよ。\x02\x03",

            "はは、しっかし……\x01",
            "タイミングの悪さだけは\x01",
            "ピカイチだな、俺ら。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        "#0211F……笑えないです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3C73")

    label("loc_3BE4")


    #C0174
    ChrTalk(
        0xFE,
        (
            "深夜の百貨店では、\x01",
            "全店舗が感謝を込めたお値段で\x01",
            "商品を提供する予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "どうか更けゆく記念祭の夜は、\x01",
            "当百貨店でお楽しみ下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C73")

    Jump("loc_4348")

    label("loc_3C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_3D29")

    #C0176
    ChrTalk(
        0xFE,
        (
            "ときたま同業者らしき観光客の方が\x01",
            "店内を見て回っている事があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "この店を見た結果、\x01",
            "お客様第一の百貨店が生まれるなら\x01",
            "私としては、視察は大歓迎ですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4348")

    label("loc_3D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3E72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DEC")

    #C0178
    ChrTalk(
        0xFE,
        (
            "おや……どなたか\x01",
            "お探しのようですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "よろしければ\x01",
            "総合インフォメーションまで\x01",
            "お問い合わせ下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "当百貨店の受付でしたら\x01",
            "心当たりがあるかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3E6D")

    label("loc_3DEC")


    #C0181
    ChrTalk(
        0xFE,
        (
            "ふむ、あの２人でも\x01",
            "見ていないとなると……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "当百貨店には\x01",
            "いらっしゃっていないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "お力になれず\x01",
            "申し訳ありません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E6D")

    Jump("loc_4348")

    label("loc_3E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3F23")

    #C0184
    ChrTalk(
        0xFE,
        (
            "ときたま同業者らしき観光客の方が\x01",
            "店内を見て回っている事があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "この店を見た結果、\x01",
            "お客様第一の百貨店が生まれるなら\x01",
            "私としては、視察は大歓迎ですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4348")

    label("loc_3F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3FDF")

    #C0186
    ChrTalk(
        0xFE,
        (
            "当百貨店の商品・店舗の質は、\x01",
            "この支配人自らの目で\x01",
            "責任を持って監査しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "万が一にも、\x01",
            "不良品・対応の不備などがございましたら\x01",
            "いつでもお申し付け下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4348")

    label("loc_3FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4067")

    #C0188
    ChrTalk(
        0xFE,
        (
            "観光の方の入りもよく、\x01",
            "近年のうちでも大繁盛しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "お客様も、もしよろしければ\x01",
            "ご覧になってくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4348")

    label("loc_4067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_410B")

    #C0190
    ChrTalk(
        0xFE,
        (
            "当百貨店では、\x01",
            "クロスベルの純国産品も\x01",
            "多数取り扱っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "観光のお土産にもぴったりです。\x01",
            "よろしければ是非、\x01",
            "覗いていってくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4348")

    label("loc_410B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4348")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A1")

    #C0192
    ChrTalk(
        0xFE,
        (
            "昨日、ミシュラム保養地から\x01",
            "《みっしぃ》を呼んで\x01",
            "イベントを行っていたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "観光客さまにも大好評で、\x01",
            "百貨店の売り上げも前年度の１２％増。\x01",
            "企画は大成功となりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x103,
        (
            "#0205F……そ、そんなものが\x01",
            "開催されていたなんて……\x02\x03",

            "#0201F（ヨナとゲームなんかしてなければ、\x01",
            "  こんなことには……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        "#0000Fティ、ティオ？\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x103,
        (
            "#0203F……なんでもありません。\x01",
            "お気になさらず。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4348")

    label("loc_42A1")


    #C0197
    ChrTalk(
        0xFE,
        (
            "昨日の《みっしぃ》との\x01",
            "コラボレーション・イベントは\x01",
            "大成功のままに終わりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "やはりキャラクターの力は偉大ですね。\x01",
            "企画した甲斐があったというものですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4348")

    TalkEnd(0xFE)
    Return()

    # Function_19_39E5 end

    def Function_20_434C(): pass

    label("Function_20_434C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43F0")

    #C0199
    ChrTalk(
        0xFE,
        (
            "パール先輩はいいなぁ、\x01",
            "遊撃士の婚約者なんて\x01",
            "羨ましいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "わたしも、わたしの魅力に\x01",
            "気付いてくれる\x01",
            "婚約者が欲しいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4462")

    label("loc_43F0")


    #C0201
    ChrTalk(
        0xFE,
        (
            "記念祭のお客さんも\x01",
            "がんばって物色したんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "はあ、気付いてくれるヒト、\x01",
            "中々いないんですよねー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4462")

    Jump("loc_47C1")

    label("loc_4467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_44CA")

    #C0203
    ChrTalk(
        0xFE,
        "みっしぃ、可愛かったですよね！？\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "はぁ、わたしも\x01",
            "モフモフしたかったなぁ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47C1")

    label("loc_44CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_452A")
    OP_93(0xFE, 0x0, 0x0)

    #C0205
    ChrTalk(
        0xFE,
        "パレード、パレードぉ……♪\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "今日はお仕事\x01",
            "抜け出しちゃおうかなぁ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47C1")

    label("loc_452A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_457D")

    #C0207
    ChrTalk(
        0xFE,
        "はあ、お腹減っちゃったなー。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "早くお仕事\x01",
            "終わらないかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47C1")

    label("loc_457D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F3")

    #C0209
    ChrTalk(
        0xFE,
        "あ、いらっしゃいませー。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "お客様も記念祭の見物ですかー？\x01",
            "いいなー、羨ましいなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_463C")

    label("loc_45F3")


    #C0211
    ChrTalk(
        0xFE,
        (
            "わたしも遊びに行きたいですけど……\x01",
            "残念、お仕事があるんですよねー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_463C")

    Jump("loc_47C1")

    label("loc_4641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_47C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4745")

    #C0212
    ChrTalk(
        0xFE,
        "#4S記念祭、ばんざーい！\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "……でもえっと、\x01",
            "実は気になってるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "昨日からずっと店内に\x01",
            "怪しい人が居るんですよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "メガネでスーツ着た\x01",
            "男の人なんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "怪しいです。\x01",
            "もしかして、テロリストとか……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_47C1")

    label("loc_4745")


    #C0217
    ChrTalk(
        0xFE,
        (
            "メガネでスーツ着た怪しい男……\x01",
            "今は２階の売り場にいるみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "警察に通報した方が\x01",
            "いいのかなぁ……ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47C1")

    TalkEnd(0xFE)
    Return()

    # Function_20_434C end

    def Function_21_47C5(): pass

    label("Function_21_47C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4861")

    #C0219
    ChrTalk(
        0xFE,
        (
            "ふー、結局今年の記念祭も\x01",
            "自宅で勉強、百貨店にパシリの\x01",
            "往復だったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "早いトコ研修医の試験に合格して\x01",
            "ウルスラ病院で働きたいぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD8")

    label("loc_4861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_48F9")

    #C0221
    ChrTalk(
        0xFE,
        (
            "……おっとぉ！\x01",
            "これ、両親に頼まれてたのより\x01",
            "１０ミラ安いじゃないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "やりぃ、お釣りでお駄賃ゲット～！\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "……１０ミラだけど。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BD8")

    label("loc_48F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4989")

    #C0224
    ChrTalk(
        0xFE,
        (
            "輸入食品って言っても、\x01",
            "やっぱり随分安いんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "鉄道一本で輸入できるんだから、\x01",
            "輸送費はタダみたいなもんだろうしなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD8")

    label("loc_4989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_49EC")

    #C0226
    ChrTalk(
        0xFE,
        "参考書、参考書……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "はぁ、記念祭も折り返しだってのに、\x01",
            "浪人生はつらいよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD8")

    label("loc_49EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4A7A")

    #C0228
    ChrTalk(
        0xFE,
        (
            "シロン姉ちゃん、\x01",
            "昨日ウチについたのが\x01",
            "もう夕方でさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "久しぶりの休みだってのに\x01",
            "夕飯くらいしか\x01",
            "一緒に過ごせなかったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD8")

    label("loc_4A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4BD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B32")

    #C0230
    ChrTalk(
        0xFE,
        (
            "んだよ、シロン姉ちゃん\x01",
            "全然来ないじゃないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "今日は休暇だから\x01",
            "迎えに来いっつってたのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "ま、またメイファさんに\x01",
            "面倒かけてないだろうな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4BD8")

    label("loc_4B32")


    #C0233
    ChrTalk(
        0xFE,
        (
            "シロン姉ちゃん、\x01",
            "幼馴染のメイファさんに\x01",
            "昔っから迷惑かけっぱなしなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "まったく……\x01",
            "待ち合わせのことなんか忘れて、\x01",
            "記念祭で遊んでるんじゃないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BD8")

    TalkEnd(0xFE)
    Return()

    # Function_21_47C5 end

    def Function_22_4BDC(): pass

    label("Function_22_4BDC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4C73")

    #C0235
    ChrTalk(
        0xFE,
        (
            "朝入ってたチラシを見てビックリよ！\x01",
            "今日は深夜までやってるんですって！\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "ああん、どれだけ私の心を\x01",
            "くすぐれば気が済むというの！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ED2")

    label("loc_4C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4CEF")

    #C0237
    ChrTalk(
        0xFE,
        (
            "さーて、一通り\x01",
            "ウィンドウショッピングもおわったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "そろそろ１階で\x01",
            "夕飯の買い物を済まそうかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ED2")

    label("loc_4CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4D7D")

    #C0239
    ChrTalk(
        0xFE,
        (
            "ま・ず・は……\x01",
            "今日もブティック《ルッカ》をチェ～ック！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "毎日新商品が出てるわけないけど、\x01",
            "なんだか覗いちゃうのよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ED2")

    label("loc_4D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4DE2")

    #C0241
    ChrTalk(
        0xFE,
        "あれとこれとそれと……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "キャッ、どうしましょ！\x01",
            "買いたいものが決められなーい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ED2")

    label("loc_4DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4E5D")

    #C0243
    ChrTalk(
        0xFE,
        (
            "ケンったら、私の買い物に\x01",
            "イヤな顔ひとつせず付き合ってくれるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        "ううん、いい息子を持ったものだわ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_4ED2")

    label("loc_4E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4ED2")

    #C0245
    ChrTalk(
        0xFE,
        (
            "日頃頑張っている自分へのご褒美に、\x01",
            "へそくりを解禁よ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "もう、思う様に\x01",
            "買い物してあげるんだから！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ED2")

    TalkEnd(0xFE)
    Return()

    # Function_22_4BDC end

    def Function_23_4ED6(): pass

    label("Function_23_4ED6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4F51")

    #C0247
    ChrTalk(
        0xFE,
        (
            "はぁ……\x01",
            "今日は深夜までママのお守り……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "ママや他のお客にとっては\x01",
            "喜ばしいことなんでしょうね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_549A")

    label("loc_4F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_4FDC")

    #C0249
    ChrTalk(
        0xFE,
        (
            "ふう、ようやくママの\x01",
            "ウィンドウショッピングが\x01",
            "おわりそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "飽きたときの顔って\x01",
            "なんだか分かりやすいんですよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_549A")

    label("loc_4FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5189")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5109")

    #C0251
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この子なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()

    #A0252
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0253
    ChrTalk(
        0xFE,
        "え？　えっと……\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "うーん、見たことは無いです。\x01",
            "知らない子だなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#0000Fそうか……\x01",
            "ありがとう、助かったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Jump("loc_5184")

    label("loc_5109")


    #C0256
    ChrTalk(
        0xFE,
        (
            "ごめんなさい、\x01",
            "見たことの無い子みたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "今日は子供もたくさん\x01",
            "来てましたけど、\x01",
            "それらしい子は覚えがないです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5184")

    Jump("loc_549A")

    label("loc_5189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5214")

    #C0258
    ChrTalk(
        0xFE,
        (
            "ふう、ようやくママの\x01",
            "ウィンドウショッピングが\x01",
            "おわりそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "飽きたときの顔って\x01",
            "なんだか分かりやすいんですよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_549A")

    label("loc_5214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_52AC")

    #C0260
    ChrTalk(
        0xFE,
        (
            "ママは人一倍ブティックの商品に　\x01",
            "興味津々なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "……ママが若い気持ちを保っているのは\x01",
            "この場合、喜ぶべきことなんでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_549A")

    label("loc_52AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_5326")

    #C0262
    ChrTalk(
        0xFE,
        (
            "ママの買いたい物が決まらないのは\x01",
            "日常茶飯事です。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "やれやれ、あと何時間くらいで\x01",
            "家に帰れるかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_549A")

    label("loc_5326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_540C")

    #C0264
    ChrTalk(
        0xFE,
        (
            "ママが買い物に行くと、\x01",
            "放っておいたら一日中百貨店を\x01",
            "ブラブラしていることでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "だからパパに、ママのお守りを\x01",
            "任されてるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "こればっかりは家庭の存亡に関わる\x01",
            "大問題なので、やるしかないんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_549A")

    label("loc_540C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_549A")

    #C0267
    ChrTalk(
        0xFE,
        (
            "ママはよく自分へのご褒美にって\x01",
            "言っていますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "その面倒を見る僕にもなにか\x01",
            "ご褒美をくれても\x01",
            "いいんじゃないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_549A")

    TalkEnd(0xFE)
    Return()

    # Function_23_4ED6 end

    def Function_24_549E(): pass

    label("Function_24_549E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_558A")

    #C0269
    ChrTalk(
        0xFE,
        (
            "婆さんに、昨日ここで選んだ\x01",
            "ブローチをプレゼントしたら、\x01",
            "随分喜んでくれての。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "今までかっこつけて\x01",
            "亭主関白を気取っていた自分が\x01",
            "恥ずかしいわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "これからもちょくちょく、\x01",
            "プレゼントさせてもらうとするかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57FE")

    label("loc_558A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_55EA")

    #C0272
    ChrTalk(
        0xFE,
        (
            "ううむ……困った。\x01",
            "贈り物などは今までしてこなかったから\x01",
            "勝手が分からんわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57FE")

    label("loc_55EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5635")

    #C0273
    ChrTalk(
        0xFE,
        (
            "はて……婆さんは一体\x01",
            "何を贈れば喜んでくれるじゃろうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57FE")

    label("loc_5635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_56C9")

    #C0274
    ChrTalk(
        0xFE,
        "やはり、スタンダードに指輪じゃろうか。\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "ただこれを婆さんに贈るとなると、\x01",
            "プロポーズのときを思い出して\x01",
            "こっ恥ずかしいのう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57FE")

    label("loc_56C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5755")

    #C0276
    ChrTalk(
        0xFE,
        (
            "せっかくの記念祭じゃから、\x01",
            "前々から計画していた婆さんへの\x01",
            "プレゼントを選んでいるんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        "ふむ……何がいいかのう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_57FE")

    label("loc_5755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_57FE")

    #C0278
    ChrTalk(
        0xFE,
        (
            "昨日の式典では、\x01",
            "マクダエル市長の素晴らしい演説を\x01",
            "聴くことができた。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "あのハルトマン議長とは\x01",
            "対立があるじゃろうが、\x01",
            "これからも頑張って欲しいもんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57FE")

    TalkEnd(0xFE)
    Return()

    # Function_24_549E end

    def Function_25_5802(): pass

    label("Function_25_5802")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58AA")

    #C0280
    ChrTalk(
        0x160,
        (
            "#3300F（中央広場の聞き込みは\x01",
            "  こんな所かしら？）\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        (
            "#0000F（ああ、十分だと思う。）\x02\x03",

            "（次は駅前通りで\x01",
            "  聞き込みをしてみよう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 5)
    OP_29(0x46, 0x1, 0x7)

    label("loc_58AA")

    Return()

    # Function_25_5802 end

    def Function_26_58AB(): pass

    label("Function_26_58AB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0282
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

    #A0283
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

    # Function_26_58AB end

    def Function_27_59C3(): pass

    label("Function_27_59C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 3300, 19500, 0)
    MoveCamera(57, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44000, 0)
    SetChrPos(0x101, 600, 30, -2000, 0)
    SetChrPos(0x160, -600, 30, -2200, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x160, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    OP_68(0, 1300, 7500, 7000)
    MoveCamera(40, 25, 0, 7000)
    SetCameraDistance(29000, 7000)
    FadeToBright(2000, 0)
    Sleep(5000)

    def lambda_5AAC():
        OP_96(0xFE, 0x258, 0x1E, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AAC)

    def lambda_5AC6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5AC6)
    Sleep(100)

    def lambda_5ADA():
        OP_96(0xFE, 0xFFFFFDA8, 0x1E, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_5ADA)

    def lambda_5AF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_5AF4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x160, 1)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1200, 2500, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    OP_0D()

    #C0284
    ChrTalk(
        0x101,
        (
            "#0006Fさすがに人が多いな……\x02\x03",

            "#0000Fでも、ここは一応\x01",
            "聞き込みをした方がよさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x160,
        (
            "#12P#3300Fレンも賛成よ。\x02\x03",

            "#3304Fまあ、受付のお姉さんたちと\x01",
            "子供客くらいでいいと思うけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x160, 500)

    #C0286
    ChrTalk(
        0x101,
        (
            "#0012F#11Pああ、俺もそう思ったけど……\x02\x03",

            "#0000F……レンちゃん、頭いいんだな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x160, 0x101, 500)
    Sleep(150)

    #C0287
    ChrTalk(
        0x160,
        (
            "#6P#3309Fうふふ。\x01",
            "ちょっと自信はあるわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 2500, 0)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA2, 3)
    EventEnd(0x5)
    Return()

    # Function_27_59C3 end

    SaveToFile()

Try(main)
