from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c045b.bin",                # FileName
        "c045b",                    # MapName
        "c045b",                    # Location
        0x0024,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "c045b",                  # 0
        "受付カイル",             # 1
        "ドリス",                 # 2
        "アーロン",               # 3
        "レティシア支配人",       # 4
        "宿泊客",                 # 5
        "宿泊客",                 # 6
        "宿泊客",                 # 7
        "宿泊客",                 # 8
        "宿泊客",                 # 9
        "ガンツ",                 # 10
        "ホステス",               # 11
        "ホステス",               # 12
        "食器",                   # 13
        "食器",                   # 14
        "食器",                   # 15
        "酒",                     # 16
        "酒",                     # 17
        "酒",                     # 18
        "酒",                     # 19
        "酒",                     # 20
    ))

    AddCharChip((
        "apl/ch50403.itc",                   # 00
        "chr/ch26802.itc",                   # 01
        "chr/ch26902.itc",                   # 02
        "apl/ch50090.itc",                   # 03
        "apl/ch50091.itc",                   # 04
        "chr/ch22000.itc",                   # 05
        "chr/ch25700.itc",                   # 06
        "chr/ch27500.itc",                   # 07
        "chr/ch27900.itc",                   # 08
        "chr/ch20200.itc",                   # 09
        "chr/ch34300.itc",                   # 0A
        "chr/ch21800.itc",                   # 0B
        "chr/ch33000.itc",                   # 0C
        "chr/ch32400.itc",                   # 0D
    ))

    DeclNpc(65440,   0,       59970,   270,  261,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4909,    0,       59669,   270,  277,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3529,    0,       59669,   90,   277,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-3990,   0,       7000,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(115110,  0,       62319,   0,    277,  0x0, 0,   9,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(112750,  0,       57849,   270,  261,  0x0, 0,   10,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(153279,  0,       61220,   180,  261,  0x0, 0,   11,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(1769,    0,       7150,    270,  261,  0x0, 0,   12,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2640,    0,       7760,    270,  261,  0x0, 0,   13,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(168500,  150,     6300,    180,  311,  0x0, 0,   0,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(167699,  150,     6300,    180,  261,  0x0, 1,   2,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(169300,  150,     6300,    180,  261,  0x0, 2,   1,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(168500,  349,     4599,    0,    374,  0x0, 0,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(167800,  349,     4599,    0,    374,  0x0, 1,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(169199,  349,     4599,    0,    374,  0x0, 5,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168500,  449,     4199,    0,    374,  0x0, 28,  3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168899,  449,     4199,    0,    374,  0x0, 28,  3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168100,  449,     4199,    0,    374,  0x0, 28,  3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168300,  449,     3799,    0,    374,  0x0, 29,  3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(168699,  449,     3799,    0,    374,  0x0, 30,  3,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(168500,  0,       4000,    1500,    168500,  1650,    6300,    0x007E, 0,  16, 0x0000)
    DeclActor(-3500,   0,       7000,    1500,    -3990,   1500,    7000,    0x007E, 0,  5,  0x0000)
    DeclActor(64300,   0,       59970,   1500,    65440,   1500,    59970,   0x007E, 0,  7,  0x0000)
    DeclActor(68050,   0,       11560,   1200,    68050,   1500,    11560,   0x007C, 0,  18, 0x0000)

    ScpFunction((
        "Function_0_3DC",          # 00, 0
        "Function_1_494",          # 01, 1
        "Function_2_4F5",          # 02, 2
        "Function_3_520",          # 03, 3
        "Function_4_521",          # 04, 4
        "Function_5_539",          # 05, 5
        "Function_6_53D",          # 06, 6
        "Function_7_7E2",          # 07, 7
        "Function_8_7E6",          # 08, 8
        "Function_9_A6A",          # 09, 9
        "Function_10_B09",         # 0A, 10
        "Function_11_BBB",         # 0B, 11
        "Function_12_C1B",         # 0C, 12
        "Function_13_C4B",         # 0D, 13
        "Function_14_CCC",         # 0E, 14
        "Function_15_DCC",         # 0F, 15
        "Function_16_E47",         # 10, 16
        "Function_17_E4B",         # 11, 17
        "Function_18_E62",         # 12, 18
        "Function_19_F79",         # 13, 19
    ))


    def Function_0_3DC(): pass

    label("Function_0_3DC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_41C"),
        (1, "loc_428"),
        (2, "loc_434"),
        (3, "loc_440"),
        (4, "loc_44C"),
        (5, "loc_458"),
        (6, "loc_464"),
        (SWITCH_DEFAULT, "loc_470"),
    )


    label("loc_41C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_428")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_434")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_440")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_44C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_458")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_464")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_470")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_47C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_493")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_47C")

    label("loc_493")

    Return()

    # Function_0_3DC end

    def Function_1_494(): pass

    label("Function_1_494")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F4")
    OP_95(0xFE, 72280, 0, 9750, 1000, 0x0)
    OP_95(0xFE, 72280, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 9750, 1000, 0x0)
    Jump("Function_1_494")

    label("loc_4F4")

    Return()

    # Function_1_494 end

    def Function_2_4F5(): pass

    label("Function_2_4F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51F")
    OP_94(0xFE, 0x604, 0xD714, 0x17C0, 0xFB9A, 0x3E8)
    Sleep(300)
    Jump("Function_2_4F5")

    label("loc_51F")

    Return()

    # Function_2_4F5 end

    def Function_3_520(): pass

    label("Function_3_520")

    Return()

    # Function_3_520 end

    def Function_4_521(): pass

    label("Function_4_521")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_538")
    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_538")

    Return()

    # Function_4_521 end

    def Function_5_539(): pass

    label("Function_5_539")

    Call(0, 6)
    Return()

    # Function_5_539 end

    def Function_6_53D(): pass

    label("Function_6_53D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A8")

    #C0001
    ChrTalk(
        0xB,
        "《ホテル・ミレニアム》へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xB,
        (
            "うふふ、当ホテルでは\x01",
            "様々なサービスをご用意しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xB,
        (
            "歓楽の都クロスベルでの\x01",
            "極上の一日を約束致しますわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ホテルや宿酒場に宿泊すると\x01",
            "ＣＰを回復する事ができます。\x02",
        )
    )

    CloseMessageWindow()

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "通常の宿酒場ではＣＰ１００、\x01",
            "高級ホテルではＣＰ２００が回復します。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x4B, 4)

    label("loc_6A8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DE")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_70E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72E")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D9")

    label("loc_72E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_742")
    Jump("loc_7D9")

    label("loc_742")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0006
    ChrTalk(
        0xB,
        "あら、ご宿泊でしょうか？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xB,
        (
            "本日ご予約のない部屋は\x01",
            "１室のみとなっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xB,
        (
            "お早めの決断を\x01",
            "お願いいたしますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D9")

    Jump("loc_6B2")

    label("loc_7DE")

    TalkEnd(0xB)
    Return()

    # Function_6_53D end

    def Function_7_7E2(): pass

    label("Function_7_7E2")

    Call(0, 8)
    Return()

    # Function_7_7E2 end

    def Function_8_7E6(): pass

    label("Function_8_7E6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_921")

    #C0009
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "《ホテル・ミレニアム》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "お部屋のご予約なら\x01",
            "当フロントをご利用ください。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ホテルや宿酒場に宿泊すると\x01",
            "ＣＰを回復する事ができます。\x02",
        )
    )

    CloseMessageWindow()

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "通常の宿酒場ではＣＰ１００、\x01",
            "高級ホテルではＣＰ２００が回復します。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x4B, 4)

    label("loc_921")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_92B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A66")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_987")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_987")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A7")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A61")

    label("loc_9A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9BB")
    Jump("loc_A61")

    label("loc_9BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A61")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0013
    ChrTalk(
        0x8,
        (
            "当ホテルのデラックスルームは\x01",
            "最上階になります。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "こちらは別館フロントですが、\x01",
            "階段を上ればデラックスルームまで\x01",
            "行く事が出来ますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A61")

    Jump("loc_92B")

    label("loc_A66")

    TalkEnd(0x8)
    Return()

    # Function_8_7E6 end

    def Function_9_A6A(): pass

    label("Function_9_A6A")

    TalkBegin(0xFE)
    OP_4B(0x9, 0xFF)

    #C0015
    ChrTalk(
        0xA,
        (
            "チップはお客様のご好意……\x01",
            "ドリスさんが納めておきなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "それよりも、他のお客様が見ている前で\x01",
            "そういう相談をするものではないですよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_9_A6A end

    def Function_10_B09(): pass

    label("Function_10_B09")

    TalkBegin(0xFE)
    OP_4B(0xA, 0xFF)

    #C0017
    ChrTalk(
        0x9,
        (
            "最上階に宿泊しているお客様から、\x01",
            "びっくりするくらいのチップを\x01",
            "頂いてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "ど、どうしましょうこんな大金……\x01",
            "支配人に報告した方がいいでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_10_B09 end

    def Function_11_BBB(): pass

    label("Function_11_BBB")

    TalkBegin(0xFE)

    #C0019
    ChrTalk(
        0xFE,
        (
            "う～む、いい夜だ。\x01",
            "極上のワインが欲しくなってきたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "ふはは、ふはははは……！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_BBB end

    def Function_12_C1B(): pass

    label("Function_12_C1B")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        (
            "パパったら\x01",
            "何を気取ってんのかしら。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_C1B end

    def Function_13_C4B(): pass

    label("Function_13_C4B")

    TalkBegin(0xFE)

    #C0022
    ChrTalk(
        0xFE,
        (
            "取引先にホテルを取ってもらったら\x01",
            "とんだ高級ホテルだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "こりゃあ半分接待が入ってるな。\x01",
            "とほほ、後が怖いよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_C4B end

    def Function_14_CCC(): pass

    label("Function_14_CCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D47")

    #C0024
    ChrTalk(
        0xFE,
        (
            "妻と最上階の一室を\x01",
            "予約しているのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "クロスベルに滞在する際はここと\x01",
            "決めているものでね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_DC8")

    label("loc_D47")


    #C0026
    ChrTalk(
        0xFE,
        (
            "そういえば……\x01",
            "ここのデラックスルームを\x01",
            "借り切っている男がいるそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "フフ、どこぞの御曹司かね？\x01",
            "少々興味があるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC8")

    TalkEnd(0xFE)
    Return()

    # Function_14_CCC end

    def Function_15_DCC(): pass

    label("Function_15_DCC")

    TalkBegin(0xFE)

    #C0028
    ChrTalk(
        0xFE,
        (
            "ホテル・ミレニアムといえば\x01",
            "昔から格式高いことで有名ですもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "やはり宿泊先は\x01",
            "信頼できる所を選ぶべきよね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_DCC end

    def Function_16_E47(): pass

    label("Function_16_E47")

    Call(0, 17)
    Return()

    # Function_16_E47 end

    def Function_17_E4B(): pass

    label("Function_17_E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E61")
    Call(0, 19)
    Jump("loc_E61")

    label("loc_E61")

    Return()

    # Function_17_E4B end

    def Function_18_E62(): pass

    label("Function_18_E62")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0030
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "鍵が掛かっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ガンツの声")

    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……んが～……ごが～……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F75")

    #C0032
    ChrTalk(
        0x101,
        (
            "#0001Fガンツさん、\x01",
            "酔いつぶれて寝ちゃったみたいだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#0106Fそろそろ支援課に帰りましょう。\x01",
            "キーアちゃんも待っている事だし。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#6P#0000Fああ、そうだな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_F75")

    TalkEnd(0xFF)
    Return()

    # Function_18_E62 end

    def Function_19_F79(): pass

    label("Function_19_F79")

    EventBegin(0x0)
    Fade(1000)
    OP_68(168500, 1000, 4800, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 169000, 0, 2900, 0)
    SetChrPos(0x103, 169300, 0, 1800, 0)
    SetChrPos(0x102, 167700, 0, 2100, 0)
    SetChrPos(0x104, 168000, 0, 2900, 0)
    SetChrPos(0x11, 168500, 150, 6300, 180)
    SetChrPos(0x12, 167700, 150, 6300, 180)
    SetChrPos(0x13, 169300, 150, 6300, 180)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis083.itp")
    OP_0D()
    SetChrSubChip(0x12, 0x0)
    Sleep(50)
    SetChrSubChip(0x13, 0x0)
    Sleep(300)

    #C0035
    ChrTalk(
        0x12,
        "#11Pあ～、ランディさん？\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x13,
        "#11Pあら、お久しぶりね。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        "#0309F#5Pはは、ご無沙汰してるぜ。\x02",
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0x11,
        "酔っ払った男",
        "#11Pああん、なんだオメーらは……？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#6P#0003F──失礼します。\x01",
            "クロスベル警察の者です。\x02\x03",

            "#0000Fマインツのガンツさんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x11,
        "#11Pヒック、そうだが……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x11,
        (
            "#11Pオメーら、どこかで\x01",
            "見たことがあるような……？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#6P#0211F……というか、この人。\x02\x03",

            "軍用犬騒ぎの時に\x01",
            "襲われそうになっていた\x01",
            "鉱員さんの片方では……？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#6P#0011Fあ……！\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x3C, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)

    #A0045
    AnonymousTalk(
        0x102,
        "#0105Fあの時の……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    VolumeBGM(0x64, 0x1F4)

    #C0046
    ChrTalk(
        0x11,
        "#11Pハ、そんな事もありやがったな。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x11,
        (
            "#11P思い出したぜ……\x01",
            "確かに警察のガキどもだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x11,
        "#11Pこのオレ様に何の用だよ、ヒック？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#6P#0006Fその、実はマインツの\x01",
            "町長さんに頼まれまして……\x02\x03",

            "#0000Fあなたの行方を捜していたんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0050
    ChrTalk(
        0x11,
        "#11P町長がオレのことを……？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x11,
        (
            "#11Pヒック……\x01",
            "いったい何の用だってんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#0301F#5Pアンタ、こっちに来たまま\x01",
            "２週間も連絡取ってねえんだろ？\x02\x03",

            "失踪したんじゃないかって\x01",
            "えらく心配されてたぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#6P#0100Fそれで私たちが\x01",
            "捜索を引き受けたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x11,
        "#11Pヒック、なるほどなぁ。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x11,
        (
            "#11Pよかったじゃねーか。\x01",
            "ちゃんと見つかってよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x11,
        (
            "#11Pクク、と言っても\x01",
            "もうオレはマインツなんざ\x01",
            "帰るつもりはねぇんだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0057
    ChrTalk(
        0x101,
        "#6P#0005Fそ、そうなんですか？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        "#6P#0205F一体どうして……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x96, 0x0, 0xBB8, 0x190)

    #C0059
    ChrTalk(
        0x11,
        "#11Pガハハ、決まってんだろ！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x11,
        (
            "#11Pオレは手に入れたんだ！\x01",
            "天才的なギャンブルの腕をな！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x11,
        (
            "#11P腕やカンだけじゃねえ！\x01",
            "女神の幸運もオレ様のもんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x11,
        (
            "#11P誰があんな田舎町に戻って\x01",
            "セコイ穴掘りなんぞやるかっての！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        "#6P#0106Fそんな……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        "#0301F#5Pおいおい……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#6P#0006Fその、いいんですか？\x02\x03",

            "#0001Fみんな心配しているんですから\x01",
            "せめて町長さんには連絡を……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0066
    ChrTalk(
        0x11,
        (
            "#11P#4Sるせえ！\x01",
            "オレに指図すんじゃねえ！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x11,
        (
            "#11Pクク、もう一儲けしたら\x01",
            "ミシュラムにでも行くか……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0x1)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0068
    ChrTalk(
        0x11,
        (
            "#5Pおい女ども！\x01",
            "週末あたりにテーマパークに\x01",
            "連れて行ってやるぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x11,
        (
            "#5P宝石店とブティックで、\x01",
            "何でも好きな物を買ってやる！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x13, 0x2)
    Sleep(300)

    #C0070
    ChrTalk(
        0x12,
        "#5Pわ～、ホントですかァ！？\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x13,
        (
            "#11Pふふっ……\x01",
            "楽しみにさせてもらうわ。\x02",
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
    Sleep(1200)
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    LoadChrToIndex("chr/ch26800.itc", 0x1E)
    LoadChrToIndex("chr/ch26900.itc", 0x1F)
    LoadChrToIndex("apl/ch50011.itc", 0x20)
    OP_68(68000, 1000, 10700, 0)
    MoveCamera(300, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 68000, 0, 13000, 180)
    SetChrPos(0x102, 68000, 0, 13000, 180)
    SetChrPos(0x103, 68000, 0, 13000, 180)
    SetChrPos(0x104, 68000, 0, 13000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x12, 68000, 0, 13000, 180)
    SetChrPos(0x13, 68000, 0, 13000, 180)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(2000, 0)
    Sleep(1000)
    ClearMapObjFlags(0x1, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    OP_68(68000, 1000, 7700, 3000)

    def lambda_1AB8():
        OP_96(0xFE, 0x109A0, 0x0, 0x1A2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AB8)

    def lambda_1AD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AD2)
    Sleep(500)

    def lambda_1AE6():
        OP_96(0xFE, 0x105B8, 0x0, 0x1E14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1AE6)

    def lambda_1B00():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1B00)
    Sleep(300)

    def lambda_1B14():
        OP_96(0xFE, 0x10D88, 0x0, 0x1E14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B14)

    def lambda_1B2E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1B2E)
    Sleep(500)

    def lambda_1B42():
        OP_96(0xFE, 0x109A0, 0x0, 0x21FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B42)

    def lambda_1B5C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1B5C)
    WaitChrThread(0x101, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)

    def lambda_1B83():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B83)
    WaitChrThread(0x102, 1)

    def lambda_1B94():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1B94)
    WaitChrThread(0x103, 1)

    def lambda_1BA5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1BA5)
    WaitChrThread(0x104, 1)

    def lambda_1BB6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1BB6)
    WaitChrThread(0x104, 2)
    OP_79(0x1)
    OP_6F(0x1)

    #C0072
    ChrTalk(
        0x104,
        (
            "#0303F#11P……駄目だな、あれは。\x02\x03",

            "#0301F完璧に舞い上がってやがるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#6P#0006Fああ……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        (
            "#0106F#5P残念だけど、町長さんに\x01",
            "状況を伝えるしかなさそうね。\x02\x03",

            "#0101F私たちが説得するというのも\x01",
            "筋違いでしょうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#12P#0206Fそうですね……\x01",
            "本人の意志もありますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#6P#0008F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C0077
    ChrTalk(
        0x102,
        (
            "#0105F#5P……ロイド？\x01",
            "何か気になることでもあるの？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D58():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1D58)

    #C0078
    ChrTalk(
        0x101,
        (
            "#6P#0006Fいや……ちょっとね。\x02\x03",

            "元々、ツキもカンもない、\x01",
            "下手の横好きでしかなかった\x01",
            "週末ギャンブラー……\x02\x03",

            "#0001Fどうしてこんなに\x01",
            "勝ち続けることが出来るように\x01",
            "なったのかと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        "#0105F#5Pそれは……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#0301F#11Pふむ、確かに気になるな。\x02\x03",

            "#0306Fつーか、是非ともコツを\x01",
            "伝授してもらいたいくらいだぜ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(150)

    #C0081
    ChrTalk(
        0x103,
        (
            "#6P#0205Fランディさんもギャンブルは\x01",
            "そこそこ強いと聞いてますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#0300F#11P調子がいい時はな。\x02\x03",

            "#0306Fだが、２週間連続で勝ち続けて\x01",
            "５０万ミラ稼ぐなんてのは無理だ。\x02\x03",

            "#0302Fま、ジャックみたいな凄腕の\x01",
            "賭博師ならあり得るかもしれんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        "#0106F#5Pあれは小説の話でしょう……\x02",
    )

    CloseMessageWindow()
    OP_68(68000, 1000, 9700, 2000)
    MoveCamera(310, 23, 0, 2000)
    SetCameraDistance(23500, 2000)
    Sound(103, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)

    def lambda_1FFD():
        OP_96(0xFE, 0x10B94, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1FFD)

    def lambda_2017():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2017)

    def lambda_2028():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2028)
    Sleep(50)

    def lambda_2038():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2038)
    Sleep(50)

    def lambda_2048():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2048)
    Sleep(400)

    def lambda_2058():
        OP_96(0xFE, 0x107AC, 0x0, 0x2904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2058)

    def lambda_2072():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2072)

    def lambda_2083():
        OP_96(0xFE, 0x109A0, 0x0, 0x2008, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2083)
    WaitChrThread(0x13, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    WaitChrThread(0x12, 1)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0084
    ChrTalk(
        0x13,
        "#11Pあら……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x12,
        "#5Pなんだ、まだいたんだァ？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#0306F#6Pおいおい、ご挨拶だな。\x02\x03",

            "#0300Fそうだ２人とも……\x01",
            "少し話を聞かせてくれねぇか？\x02\x03",

            "あのガンツって\x01",
            "兄さんについてなんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x13,
        "#11Pふふ、別にいいわよ。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x12,
        (
            "#5Pなになに？\x01",
            "ひょっとして犯罪がらみぃ？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        (
            "#0303F#6Pいや、そうじゃねえが……\x02\x03",

            "#0301Fあの兄さん、\x01",
            "いつもあんな調子なのかよ？\x02\x03",

            "いくら酒が入ってるからって\x01",
            "あまりに横柄すぎやしねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x13,
        "#11Pうーん、そうね……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x13,
        (
            "#11P確かに最初の頃は、\x01",
            "あそこまで威張り散らしたりは\x01",
            "していなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x12,
        (
            "#5Pそのうちどんどん、\x01",
            "エラソーになってったかなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x12,
        (
            "#5Pま、ウチらは客商売だから\x01",
            "あんまり気にはしてないけどー。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        "#0303F#6Pふむ、そうか……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#6P#0008Fあの態度は、酒が入っているから\x01",
            "だけじゃ無いってことか……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x13,
        (
            "#11Pそれにしても\x01",
            "彼、ホント凄いのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x13,
        (
            "#11Pまるで伏せられたカードが\x01",
            "見えているみたいに\x01",
            "カンが冴えてるんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x12,
        (
            "#5Pうんうん！\x01",
            "ルーレットなんて数字を\x01",
            "ピタリと当てちゃうしィ！\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x12,
        (
            "#5Pディーラーの人たちの考えも\x01",
            "見抜いちゃってるみたいだもん！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        "#0105F#6Pそれは凄いですね……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#6P#0006Fは～、そこまで行くと\x01",
            "カンと言うより超能力だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#0310F#6Pクッ、なんでその力が\x01",
            "俺に目覚めないんだっつーの！\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x103,
        "#6P#0208F………………………………\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x13,
        (
            "#11Pえっと、ガンツさんについては\x01",
            "知っているのはその位だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x12,
        "#5Pそんなんでもいいワケ？\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#0309F#6Pおお、サンクス。\x02\x03",

            "#0302Fまた暇な時にでも\x01",
            "店に寄らせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x13,
        (
            "#11Pふふ……\x01",
            "期待しないで待ってるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x12,
        "#5Pそれじゃ、まったねェ～。\x02",
    )

    CloseMessageWindow()

    def lambda_266C():

        label("loc_266C")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_266C")

    QueueWorkItem2(0x101, 2, lambda_266C)

    def lambda_267E():

        label("loc_267E")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_267E")

    QueueWorkItem2(0x102, 2, lambda_267E)

    def lambda_2690():

        label("loc_2690")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_2690")

    QueueWorkItem2(0x103, 2, lambda_2690)

    def lambda_26A2():

        label("loc_26A2")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_26A2")

    QueueWorkItem2(0x104, 2, lambda_26A2)

    def lambda_26B4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_26B4)
    Sleep(50)

    def lambda_26C4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_26C4)
    WaitChrThread(0x12, 2)
    OP_68(65000, 1000, 7700, 5000)

    def lambda_26E6():
        OP_96(0xFE, 0x9E34, 0x0, 0x157C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_26E6)
    WaitChrThread(0x13, 2)

    def lambda_2704():
        OP_96(0xFE, 0x9E34, 0x0, 0x157C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2704)
    OP_6F(0x79)
    Fade(500)
    OP_68(68000, 1000, 7700, 0)
    MoveCamera(300, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x104, 68000, 0, 8700, 270)
    OP_93(0x103, 0x10E, 0x0)
    OP_93(0x104, 0x10E, 0x0)
    OP_0D()
    TurnDirection(0x102, 0x101, 500)

    #C0109
    ChrTalk(
        0x102,
        (
            "#0101F#5P……とりあえず、\x01",
            "町長さんに連絡を入れた方が\x01",
            "いいんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_27F3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_27F3)

    def lambda_2800():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2800)
    TurnDirection(0x101, 0x102, 500)

    #C0110
    ChrTalk(
        0x101,
        "#6P#0006Fああ、そうだな……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは教えてもらっていた\x01",
            "ビクセン町長宅の番号にコールした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetChrSubChip(0x101, 0x5)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(902, 0, 100, 0)
    Sleep(2800)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もしもし。\x01",
            "こちらビクセンだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0113
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000Fどうも、特務支援課の\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おお、君か。\x02\x03",

            "ひょっとして何か\x01",
            "情報でもあったのかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0115
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003Fいえ、それが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはビクセン町長に一通りの事情を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A0117
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なんと……\x01",
            "そんな事になっていたのか。\x02\x03",

            "まさかあのガンツが\x01",
            "ギャンブルで大勝ちをして\x01",
            "高級ホテルに泊まっているとは……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0118
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006Fさすがに連れ戻す説得までは\x01",
            "出来なかったんですが……\x02\x03",

            "#0000F一応、報告だけでもと思いまして。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A0119
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いやいや、それで十分だ。\x02\x03",

            "そういう事であれば\x01",
            "明日にでも私が街に出て\x01",
            "彼と直接話をしてみるつもりだ。\x02\x03",

            "ありがとう、本当に助かったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0120
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0004Fいえ、お気になさらずに。\x02\x03",

            "#0000Fまた何かあったら遠慮なく\x01",
            "こちらに連絡してきてください。\x02\x03",

            "出来る限りのお手伝いを\x01",
            "させてもらいますから。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A0121
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ありがとう……\x01",
            "その時はよろしく頼むよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0122
    ChrTalk(
        0x102,
        "#0101F#5P町長さんはなんて？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0123
    ChrTalk(
        0x101,
        (
            "#6P#0006Fああ、さすがに\x01",
            "驚いたみたいだった。\x02\x03",

            "#0000F明日、クロスベル市に来て\x01",
            "直接話してみるってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0300F#11Pま、身内が話すのが\x01",
            "一番いいかもしれねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x103,
        "#12P#0203F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 500)

    #C0126
    ChrTalk(
        0x101,
        (
            "#5P#0005F……ティオ？\x02\x03",

            "#0001Fさっきから静かだけど\x01",
            "何か気になる事でもあるのか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E78():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2E78)
    Sleep(50)

    def lambda_2E88():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2E88)

    #C0127
    ChrTalk(
        0x103,
        (
            "#12P#0203Fいえ……\x02\x03",

            "#0200Fただ、今日は色々あったので\x01",
            "疲れてしまったみたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        (
            "#5P#0002Fそうか……\x01",
            "遺跡の調査もあったしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#0104F#5Pもう日も暮れているし、\x01",
            "そろそろ支援課に帰りましょう。\x02\x03",

            "#0102Fキーアちゃんも待っている事だし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    #C0130
    ChrTalk(
        0x103,
        (
            "#12P#0204Fふふ、そうですね……\x02\x03",

            "#0202Fキーアの笑顔が見られれば\x01",
            "疲れも吹き飛びそうな気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#5P#0009Fはは、大げさだな。\x02\x03",

            "#0002Fま、気持ちは分かるけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x104,
        (
            "#0304F#11Pやれやれ、揃いも揃って\x01",
            "親バカというか何というか……\x02\x03",

            "#0302Fそんじゃ、とっとと\x01",
            "キー坊の顔を見に帰るとすっか！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_68(68000, 1500, 9000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 68000, 0, 9000, 180)
    SetChrPos(0x1, 68000, 0, 9000, 180)
    SetChrPos(0x2, 68000, 0, 9000, 180)
    SetChrPos(0x3, 68000, 0, 9000, 180)
    SetScenarioFlags(0xC2, 0)
    OP_29(0x4A, 0x1, 0x5)
    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_19_F79 end

    SaveToFile()

Try(main)
