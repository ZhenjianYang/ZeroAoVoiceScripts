from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c045c.bin",                # FileName
        "c045c",                    # MapName
        "c045c",                    # Location
        0x0024,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 36, 0, 4, 0, 5],
    )

    BuildStringList((
        "c045c",                  # 0
        "受付カイル",             # 1
        "ドリス",                 # 2
        "アーロン",               # 3
        "レティシア支配人",       # 4
        "見物客",                 # 5
        "見物客",                 # 6
        "見物客",                 # 7
        "キリカ",                 # 8
    ))

    AddCharChip((
        "chr/ch07300.itc",                   # 00
        "chr/ch21800.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch22300.itc",                   # 03
        "chr/ch25700.itc",                   # 04
        "chr/ch27500.itc",                   # 05
        "chr/ch27900.itc",                   # 06
        "chr/ch33200.itc",                   # 07
    ))

    DeclNpc(65440,   0,       59970,   270,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4090,    9,       59900,   225,  261,  0x0, 0,   4,   0,   0,   2,   0,   11,  255,  0)
    DeclNpc(50740,   0,       9750,    90,   261,  0x0, 0,   5,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(-3990,   0,       7000,    90,   261,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(112779,  0,       57889,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(116599,  0,       58169,   225,  261,  0x0, 0,   3,   0,   0,   3,   0,   13,  255,  0)
    DeclNpc(155360,  0,       59509,   135,  261,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(114040,  0,       5860,    270,  389,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(-3500,   0,       7000,    1500,    -3990,   1500,    7000,    0x007E, 0,  6,  0x0000)
    DeclActor(64300,   0,       59970,   1500,    65440,   1500,    59970,   0x007E, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_220",          # 00, 0
        "Function_1_2D8",          # 01, 1
        "Function_2_339",          # 02, 2
        "Function_3_364",          # 03, 3
        "Function_4_38F",          # 04, 4
        "Function_5_3F4",          # 05, 5
        "Function_6_3F5",          # 06, 6
        "Function_7_3F9",          # 07, 7
        "Function_8_C25",          # 08, 8
        "Function_9_C29",          # 09, 9
        "Function_10_14E2",        # 0A, 10
        "Function_11_1883",        # 0B, 11
        "Function_12_1BBF",        # 0C, 12
        "Function_13_1E42",        # 0D, 13
        "Function_14_1FBE",        # 0E, 14
        "Function_15_2195",        # 0F, 15
        "Function_16_25FA",        # 10, 16
    ))


    def Function_0_220(): pass

    label("Function_0_220")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_260"),
        (1, "loc_26C"),
        (2, "loc_278"),
        (3, "loc_284"),
        (4, "loc_290"),
        (5, "loc_29C"),
        (6, "loc_2A8"),
        (SWITCH_DEFAULT, "loc_2B4"),
    )


    label("loc_260")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_26C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_278")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_284")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_290")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_29C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2D7")

    Return()

    # Function_0_220 end

    def Function_1_2D8(): pass

    label("Function_1_2D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_338")
    OP_95(0xFE, 72280, 0, 9750, 1000, 0x0)
    OP_95(0xFE, 72280, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 9750, 1000, 0x0)
    Jump("Function_1_2D8")

    label("loc_338")

    Return()

    # Function_1_2D8 end

    def Function_2_339(): pass

    label("Function_2_339")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_363")
    OP_94(0xFE, 0x604, 0xD714, 0x17C0, 0xFB9A, 0x3E8)
    Sleep(300)
    Jump("Function_2_339")

    label("loc_363")

    Return()

    # Function_2_339 end

    def Function_3_364(): pass

    label("Function_3_364")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38E")
    OP_94(0xFE, 0x1C200, 0xDFAC, 0x1CB9C, 0xE8B2, 0x3E8)
    Sleep(300)
    Jump("Function_3_364")

    label("loc_38E")

    Return()

    # Function_3_364 end

    def Function_4_38F(): pass

    label("Function_4_38F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_39D")
    Jump("loc_3F3")

    label("loc_39D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C6")
    SetChrPos(0xF, 63400, 0, 59930, 90)
    ClearChrFlags(0xF, 0x80)

    label("loc_3C6")

    Jump("loc_3F3")

    label("loc_3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3D9")
    Jump("loc_3F3")

    label("loc_3D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3F3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3F3")
    ClearChrFlags(0xF, 0x80)

    label("loc_3F3")

    Return()

    # Function_4_38F end

    def Function_5_3F4(): pass

    label("Function_5_3F4")

    Return()

    # Function_5_3F4 end

    def Function_6_3F5(): pass

    label("Function_6_3F5")

    Call(0, 7)
    Return()

    # Function_6_3F5 end

    def Function_7_3F9(): pass

    label("Function_7_3F9")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_564")

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

    label("loc_564")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C21")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EA")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C1C")

    label("loc_5EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FE")
    Jump("loc_C1C")

    label("loc_5FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6C7")

    #C0006
    ChrTalk(
        0xB,
        (
            "いよいよ最終日……\x01",
            "チェックアウトなさるお客様は\x01",
            "最大の笑顔でお送り致しますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xB,
        (
            "また来年、再びこの地を\x01",
            "訪れてくださることを\x01",
            "心からお待ちしているのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1C")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_7C4")

    #C0008
    ChrTalk(
        0xB,
        (
            "パレードが通り過ぎるのが\x01",
            "聞こえてきましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xB,
        (
            "子供の頃から聞き馴染んだ音ですが、\x01",
            "実際に聞くと、こう……\x01",
            "ウキウキしてしまいますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xB,
        (
            "支配人として取り繕っていても、\x01",
            "私にもクロスベル市民の血が\x01",
            "流れているということでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1C")

    label("loc_7C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_985")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 4)), scpexpr(EXPR_END)), "loc_85A")

    #C0011
    ChrTalk(
        0xB,
        (
            "申し訳ございません。\x01",
            "当ロビーには来ていないと思いますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            "お客様はすべて\x01",
            "チェックしていますし\x01",
            "間違いは無いはずです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_980")

    label("loc_85A")


    #C0013
    ChrTalk(
        0x101,
        (
            "#0000F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0014
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

    #C0015
    ChrTalk(
        0xB,
        (
            "あら、可愛らしい\x01",
            "男の子ですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "ですが当ロビーには\x01",
            "来ていないと思いますわ。\x02",
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
    SetScenarioFlags(0xAA, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)

    label("loc_980")

    Jump("loc_C1C")

    label("loc_985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_A82")

    #C0018
    ChrTalk(
        0xB,
        (
            "パレードが通り過ぎるのが\x01",
            "聞こえてきましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "子供の頃から聞き馴染んだ音ですが、\x01",
            "実際に聞くと、こう……\x01",
            "ウキウキしてしまいますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xB,
        (
            "支配人として取り繕っていても、\x01",
            "私にもクロスベル市民の血が\x01",
            "流れているということでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1C")

    label("loc_A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B1A")

    #C0021
    ChrTalk(
        0xB,
        (
            "今日のパレードは\x01",
            "最上階・デラックスルームの\x01",
            "真下を通りますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        (
            "この時期はいつも、\x01",
            "他の部屋に先んじて\x01",
            "満室になってしまいますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1C")

    label("loc_B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B93")

    #C0023
    ChrTalk(
        0xB,
        (
            "本日は市庁舎の方で\x01",
            "催し物があるそうですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        (
            "当ホテルにも\x01",
            "出席者の方がご予約を\x01",
            "なさっていますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1C")

    label("loc_B93")


    #C0025
    ChrTalk(
        0xB,
        (
            "記念祭初日から\x01",
            "多くのご利用を頂いておりますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        (
            "観光客の皆様にとっても、\x01",
            "この歓楽街が注目のスポットに\x01",
            "なっているようですわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1C")

    Jump("loc_56E")

    label("loc_C21")

    TalkEnd(0xB)
    Return()

    # Function_7_3F9 end

    def Function_8_C25(): pass

    label("Function_8_C25")

    Call(0, 9)
    Return()

    # Function_8_C25 end

    def Function_9_C29(): pass

    label("Function_9_C29")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D64")

    #C0027
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "《ホテル・ミレニアム》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
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

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ホテルや宿酒場に宿泊すると\x01",
            "ＣＰを回復する事ができます。\x02",
        )
    )

    CloseMessageWindow()

    #A0030
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

    label("loc_D64")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DE")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DCA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_DCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEA")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14D9")

    label("loc_DEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DFE")
    Jump("loc_14D9")

    label("loc_DFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E99")

    #C0031
    ChrTalk(
        0x8,
        (
            "最終日とあってお部屋にも\x01",
            "空きが目立つようになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "当日宿泊も可能ですので\x01",
            "どうぞご利用くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D9")

    label("loc_E99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_EEA")

    #C0033
    ChrTalk(
        0x8,
        (
            "迷子のお子様とは心配ですね。\x01",
            "……私も気を付けておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D9")

    label("loc_EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_10D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 5)), scpexpr(EXPR_END)), "loc_F7B")

    #C0034
    ChrTalk(
        0x8,
        (
            "表は見物客で一杯でしたし\x01",
            "見かけたかどうかは判りませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "当ホテルのお客様でないことだけは\x01",
            "断言できるのですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D0")

    label("loc_F7B")


    #C0036
    ChrTalk(
        0x101,
        (
            "#0000F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0037
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

    #C0038
    ChrTalk(
        0x8,
        (
            "迷子のお子さんですか……\x01",
            "それは心配ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "ふむ、しかし\x01",
            "見かけたかどうかまでは……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "なにせ表は\x01",
            "見物客で一杯でしたので。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0000Fそうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)

    label("loc_10D0")

    Jump("loc_14D9")

    label("loc_10D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_11F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_115D")

    #C0042
    ChrTalk(
        0x8,
        (
            "記念祭最終日、または\x01",
            "その翌日に帰国なさる\x01",
            "お客様が多いのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "……またのご利用を\x01",
            "お待ちしております。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F3")

    label("loc_115D")


    #C0044
    ChrTalk(
        0x8,
        (
            "キリカ様はあと２日滞在の上\x01",
            "帰国なさるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "記念祭が終わった翌日に\x01",
            "帰られる計算ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "……またのご利用を\x01",
            "お待ちしております。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_11F3")

    Jump("loc_14D9")

    label("loc_11F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_12E1")

    #C0047
    ChrTalk(
        0x8,
        (
            "当ホテルにキリカ様という方が\x01",
            "滞在なさっているのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "アルカンシェルのチケットを\x01",
            "お持ちだそうで、\x01",
            "本日は劇場観賞に出ておられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "芸能関係の方だそうですが、\x01",
            "さすが、と思わせる\x01",
            "颯爽とした方でしたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D9")

    label("loc_12E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_137B")

    #C0050
    ChrTalk(
        0x8,
        (
            "当ホテルは、行き届いたサービスで\x01",
            "他所の国にも名を知られています。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "噂を聞きつけた政界の要人から\x01",
            "ご利用いただくことも多いのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D9")

    label("loc_137B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1423")

    #C0052
    ChrTalk(
        0x8,
        (
            "宿泊客の方と\x01",
            "間違えてしまいましたこと……\x01",
            "どうか支配人にはご内密に。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "昨日から大勢の方が出入りして\x01",
            "いらっしゃいますから……\x01",
            "私もまだまだですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D9")

    label("loc_1423")


    #C0054
    ChrTalk(
        0x8,
        "お客様、お忘れ物でしょうか？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "……失礼、私とした事が、\x01",
            "宿泊客の方と間違えてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "昨日から大勢の方が出入りして\x01",
            "いらっしゃいますから……\x01",
            "私もまだまだですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_14D9")

    Jump("loc_D6E")

    label("loc_14DE")

    TalkEnd(0x8)
    Return()

    # Function_9_C29 end

    def Function_10_14E2(): pass

    label("Function_10_14E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1590")

    #C0057
    ChrTalk(
        0xA,
        (
            "お客様がチェックアウトされた後は\x01",
            "可及的速やかに部屋を整えなければ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        (
            "次のお客様を待たせないためにも、\x01",
            "私たち従業員には\x01",
            "常に速さが求められるのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187F")

    label("loc_1590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_15F2")

    #C0059
    ChrTalk(
        0xA,
        (
            "……うむ、ドリスさんの掃除は\x01",
            "きちんとやり直されたようですな。\x01",
            "上出来、上出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187F")

    label("loc_15F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1753")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_169D")

    #C0060
    ChrTalk(
        0xA,
        (
            "お客様に気持ちよく\x01",
            "過ごしていただく為には\x01",
            "美しい空間が必要不可欠です。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "記念祭だとてたるまないよう、\x01",
            "ドリスさんには\x01",
            "しかと注意しなければ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174E")

    label("loc_169D")


    #C0062
    ChrTalk(
        0xA,
        (
            "……廊下の掃除が\x01",
            "少々甘いようですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        (
            "お客様に気持ちよく\x01",
            "過ごしていただく為には\x01",
            "美しい空間が必要不可欠です。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        (
            "ドリスさんに\x01",
            "しかと言っておかないといけませんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_174E")

    Jump("loc_187F")

    label("loc_1753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_17F7")

    #C0065
    ChrTalk(
        0xA,
        (
            "ミラに余裕のある方々は、\x01",
            "記念祭の間中ミシュラムのホテルで\x01",
            "過ごすそうですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xA,
        (
            "一般市民たるわたくしには\x01",
            "到底真似できませんな。\x01",
            "はっはっは……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187F")

    label("loc_17F7")


    #C0067
    ChrTalk(
        0xA,
        (
            "デラックスルームは\x01",
            "記念祭の間は満室になっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "普段埋まるような部屋ではないのですが、\x01",
            "さすが記念祭ともなると違いますな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187F")

    TalkEnd(0xFE)
    Return()

    # Function_10_14E2 end

    def Function_11_1883(): pass

    label("Function_11_1883")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_18CB")

    #C0069
    ChrTalk(
        0x9,
        (
            "えっと、バスセットの補充と、\x01",
            "それからそれから……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBB")

    label("loc_18CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1968")

    #C0070
    ChrTalk(
        0x9,
        (
            "アーロンさんに掃除の甘さを\x01",
            "指摘されてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "何とかやり直したんですが……\x01",
            "やっぱり忙しいからって\x01",
            "手を抜いちゃいけませんよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBB")

    label("loc_1968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_19E0")

    #C0072
    ChrTalk(
        0x9,
        (
            "ふぅ……なんだか疲れが\x01",
            "出ている気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "記念祭も明日までですし、\x01",
            "なんとかがんばらないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBB")

    label("loc_19E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A85")

    #C0074
    ChrTalk(
        0x9,
        (
            "あっちの部屋のシーツを\x01",
            "たたんでリネン室に持っていって、\x01",
            "こっちの部屋のベッドメイクをして……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "ああ、急がなきゃ\x01",
            "お客様が帰ってきてしまいます！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBB")

    label("loc_1A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1AFD")

    #C0076
    ChrTalk(
        0x9,
        (
            "この階のベッドメイクは\x01",
            "一通り済みました。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "チップを入れてくださる方もいて、\x01",
            "なんだか嬉しいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBB")

    label("loc_1AFD")


    #C0078
    ChrTalk(
        0x9,
        (
            "この階のベッドメイクは\x01",
            "一通り済みました。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "最近の流行で、枕の下に\x01",
            "チップを置いてくださる方も\x01",
            "いるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "……し、失礼しました。\x01",
            "私ったらお客様の前で\x01",
            "はしたないお話を……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1BBB")

    TalkEnd(0xFE)
    Return()

    # Function_11_1883 end

    def Function_12_1BBF(): pass

    label("Function_12_1BBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1C28")

    #C0081
    ChrTalk(
        0xC,
        (
            "予定していたアルカンシェルも\x01",
            "終わりましたし、今日は娘と\x01",
            "ゆっくりする予定なのです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3E")

    label("loc_1C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1CA2")

    #C0082
    ChrTalk(
        0xC,
        (
            "娘とアルカンシェルの\x01",
            "公演を観たのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xC,
        (
            "その素晴らしさに触れて、\x01",
            "娘は今朝から放心状態なのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3E")

    label("loc_1CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D31")

    #C0084
    ChrTalk(
        0xC,
        (
            "明日はアルカンシェルの\x01",
            "公演を観に行くのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xC,
        (
            "娘は興味ないようですが……\x01",
            "一度観れば、きっと\x01",
            "素晴らしさが分かりますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3E")

    label("loc_1D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1D8D")

    #C0086
    ChrTalk(
        0xC,
        (
            "アルカンシェルの舞台は最高です。\x01",
            "娘にもあの衝撃を\x01",
            "味わって欲しいですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3E")

    label("loc_1D8D")


    #C0087
    ChrTalk(
        0xC,
        (
            "私達は記念祭に合わせ、\x01",
            "アルカンシェルの公演を\x01",
            "見に来たのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xC,
        (
            "私が以前見たのは\x01",
            "もう３年も前のこと……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        (
            "新作が公開されるというので、\x01",
            "娘と観る事にしたのです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1E3E")

    TalkEnd(0xFE)
    Return()

    # Function_12_1BBF end

    def Function_13_1E42(): pass

    label("Function_13_1E42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1EA1")

    #C0090
    ChrTalk(
        0xD,
        "お父さんと一緒に歓楽街を回るわ。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xD,
        "イリアのグッズとかないのかなぁ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FBA")

    label("loc_1EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1EE7")

    #C0092
    ChrTalk(
        0xD,
        "イリア様……！\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xD,
        "はあ、素晴らしかったわ……ッ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FBA")

    label("loc_1EE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1F65")

    #C0094
    ChrTalk(
        0xD,
        (
            "クロスベルの歓楽街って凄いわね。\x01",
            "遊ぶ所が盛りだくさんだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xD,
        (
            "ちょっと休憩したら\x01",
            "また遊びに行こうっと！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FBA")

    label("loc_1F65")


    #C0096
    ChrTalk(
        0xD,
        "お父さんが凄い凄いって言うのよ。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xD,
        (
            "たかが舞台でしょ？\x01",
            "そんなに凄いのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FBA")

    TalkEnd(0xFE)
    Return()

    # Function_13_1E42 end

    def Function_14_1FBE(): pass

    label("Function_14_1FBE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_203B")

    #C0098
    ChrTalk(
        0xE,
        (
            "私、気づいたの。\x01",
            "いつの間にかカジノで\x01",
            "相当なミラをすっていたことに。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xE,
        "……危険すぎるわ、あの場所。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2191")

    label("loc_203B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_20AF")

    #C0100
    ChrTalk(
        0xE,
        "昨日カジノに行ってきたわ。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xE,
        (
            "あのスリル……\x01",
            "ファンが多い理由が\x01",
            "なんとなく分かった気がするわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2191")

    label("loc_20AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_212A")

    #C0102
    ChrTalk(
        0xE,
        (
            "せっかくクロスベルに来たのだし、\x01",
            "普段できないことをしてみようと思うの。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xE,
        "カジノって面白いのかしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2191")

    label("loc_212A")


    #C0104
    ChrTalk(
        0xE,
        (
            "綺麗なホテルが\x01",
            "見つかってよかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xE,
        (
            "東通りの宿みたいな\x01",
            "ボロっちい場所は\x01",
            "性に合わないもの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2191")

    TalkEnd(0xFE)
    Return()

    # Function_14_1FBE end

    def Function_15_2195(): pass

    label("Function_15_2195")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_234A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_224E")

    #C0106
    ChrTalk(
        0xF,
        (
            "#3400Fアルカンシェルの\x01",
            "共和国公演……か。\x02\x03",

            "確かに実現すれば\x01",
            "素晴らしい人気でしょうね。\x02\x03",

            "先方には打診だけはしておいたわ。\x01",
            "後は向こうの出方次第でしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2345")

    label("loc_224E")


    #C0107
    ChrTalk(
        0xF,
        (
            "#3400Fアルカンシェルの公演は\x01",
            "素晴らしいものだったわ。\x02\x03",

            "さすがの私も\x01",
            "魂を抜かれかけた……\x01",
            "とでも言いましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#0000Fははは……\x01",
            "それで、お話の方は\x01",
            "ついたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xF,
        (
            "#3400F提案だけはしてきた所よ。\x01",
            "後は向こうの出方次第でしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2345")

    Jump("loc_25F6")

    label("loc_234A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_25F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 5)), scpexpr(EXPR_END)), "loc_2425")

    #C0110
    ChrTalk(
        0xF,
        (
            "#3400Fさて、仕事に向けて\x01",
            "色々と把握しておく\x01",
            "必要がありそうね。\x02\x03",

            "……最終的には\x01",
            "向こうの出方次第でしょうけど……\x02\x03",

            "準備をしておくに\x01",
            "越したことはないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#0000F（随分と真剣そうだな……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_25F6")

    label("loc_2425")


    #C0112
    ChrTalk(
        0xF,
        "#3400Fあら、先ほどはどうも。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#0000Fキリカさん……\x01",
            "このホテルにご滞在だったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        (
            "#0300F高級ホテルのスイートとは、\x01",
            "さすがっすね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        "#0200F芸能プロはランクが違うかと。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xF,
        (
            "#3400Fフフ、ホテルのランクは\x01",
            "どうでも良かったのだけど。\x02\x03",

            "ここが立地的に\x01",
            "都合が良かったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        (
            "#0100Fあ……アルカンシェルの\x01",
            "目の前ですものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xF,
        (
            "#3400Fええ、おまけに\x01",
            "見晴らしは最高……\x02\x03",

            "明日の公演は\x01",
            "楽しませてもらうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#0000Fははは……\x01",
            "ごゆっくりどうぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB7, 5)

    label("loc_25F6")

    TalkEnd(0xFE)
    Return()

    # Function_15_2195 end

    def Function_16_25FA(): pass

    label("Function_16_25FA")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2690")
    OP_29(0x46, 0x1, 0x2)

    #C0120
    ChrTalk(
        0x101,
        (
            "#0000F（よし、歓楽街の聞き込みは\x01",
            "  これで十分だな。）\x02\x03",

            "（次は裏通りだ……\x01",
            "  同じように聞き込みを進めていこう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 3)

    label("loc_2690")

    Return()

    # Function_16_25FA end

    SaveToFile()

Try(main)
