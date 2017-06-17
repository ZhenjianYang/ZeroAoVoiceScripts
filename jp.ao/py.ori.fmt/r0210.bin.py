from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0210.bin",                # FileName
        "r0210",                    # MapName
        "r0210",                    # Location
        0x00A5,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x04,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0210",                  # 0
        "セルダン支部長",         # 1
        "ペーター",               # 2
        "フィッシャー",           # 3
        "レイクロードⅢ世",       # 4
        "竜宮カグヤ",             # 5
    ))

    AddCharChip((
        "chr/ch32200.itc",                   # 00
        "chr/ch24200.itc",                   # 01
        "chr/ch46100.itc",                   # 02
        "chr/ch45600.itc",                   # 03
        "chr/ch45800.itc",                   # 04
    ))

    DeclNpc(-389,    0,       -1149,   188,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(1080,    0,       -1110,   270,  389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(6010,    0,       -8220,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(529,     0,       -1149,   270,  389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-449,    0,       -1190,   90,   389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(1510,    0,       3420,    1200,    1510,    750,     3420,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(384, 0)                                        # 0

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_230",          # 01, 1
        "Function_2_39C",          # 02, 2
        "Function_3_3E7",          # 03, 3
        "Function_4_498",          # 04, 4
        "Function_5_162E",         # 05, 5
        "Function_6_1B9C",         # 06, 6
        "Function_7_1C53",         # 07, 7
        "Function_8_1D96",         # 08, 8
        "Function_9_2532",         # 09, 9
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1B8"),
        (1, "loc_1C4"),
        (2, "loc_1D0"),
        (3, "loc_1DC"),
        (4, "loc_1E8"),
        (5, "loc_1F4"),
        (6, "loc_200"),
        (SWITCH_DEFAULT, "loc_20C"),
    )


    label("loc_1B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_200")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_20C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_22F")

    Return()

    # Function_0_180 end

    def Function_1_230(): pass

    label("Function_1_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_243")
    SetChrFlags(0x8, 0x80)
    Jump("loc_39B")

    label("loc_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_274")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_26A")

    SetChrFlags(0x8, 0x80)
    Jump("loc_39B")

    label("loc_274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_287")
    SetChrFlags(0x8, 0x80)
    Jump("loc_39B")

    label("loc_287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2B6")
    SetChrPos(0xA, 1080, 0, -1110, 270)
    ClearChrFlags(0xA, 0x80)
    TurnDirection(0x8, 0xA, 0)

    label("loc_2B6")

    Jump("loc_39B")

    label("loc_2BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2C9")
    Jump("loc_39B")

    label("loc_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_308")
    SetChrPos(0x8, -390, 0, -1150, 90)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x9, 1080, 0, -1110, 270)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_39B")

    label("loc_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_316")
    Jump("loc_39B")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_324")
    Jump("loc_39B")

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_341")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C")
    SetChrFlags(0x8, 0x80)

    label("loc_33C")

    Jump("loc_39B")

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34F")
    Jump("loc_39B")

    label("loc_34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_35D")
    Jump("loc_39B")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_37A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_375")
    SetChrFlags(0x8, 0x80)

    label("loc_375")

    Jump("loc_39B")

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_38D")
    SetChrFlags(0x8, 0x80)
    Jump("loc_39B")

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_39B")
    SetChrFlags(0x8, 0x80)

    label("loc_39B")

    Return()

    # Function_1_230 end

    def Function_2_39C(): pass

    label("Function_2_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_3AE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E6")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_3E6")

    Return()

    # Function_2_39C end

    def Function_3_3E7(): pass

    label("Function_3_3E7")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『お菓子の王国　第二巻』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_494")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x12)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_494")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『つるつる杏仁豆腐』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_494")

    TalkEnd(0xFF)
    Return()

    # Function_3_3E7 end

    def Function_4_498(): pass

    label("Function_4_498")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C7")
    TurnDirection(0xFE, 0x101, 0)

    #C0003
    ChrTalk(
        0xFE,
        (
            "おお、ロイド団員。\x01",
            "やっと顔を出してくれたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#00005Fセルダン支部長、ここは……\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "ああ、この建物は元々\x01",
            "貸しボート小屋だったんだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "数年前に廃業して以来、\x01",
            "ずっと放置されてたみたいなんで\x01",
            "格安で借りることが出来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "まあ、再出発する俺たちに\x01",
            "あつらえ向きの新支部ってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "それよりロイド団員、君にも\x01",
            "釣皇倶楽部との《爆釣#4Rばくちょう#勝負》について\x01",
            "説明しておきたいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#00005Fば、《爆釣勝負》ですか……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00003Fなるほど、釣皇倶楽部の\x01",
            "メンバー５人と《爆釣勝負》ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "ああ、そういうわけだ。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "勝負の方は一応、\x01",
            "俺たちの方で何とかする\x01",
            "つもりではいるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "出来れば、ロイド団員にも\x01",
            "協力をお願いするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00004Fはい、俺も好きな場所で\x01",
            "釣りが出来なくなるのは\x01",
            "御免ですからね。\x02\x03",

            "#00000F出来る限り、努力してみます。\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣皇倶楽部のメンバーに、\x01",
            "《爆釣勝負》を挑めるようになりました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "勝負についての詳しい内容は、\x01",
            "『東通りの釣皇倶楽部』にいる\x01",
            "受付嬢セイラームから聞く事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x1C0, 0)

    label("loc_8C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D4")
    TurnDirection(0xFE, 0x101, 0)

    #C0017
    ChrTalk(
        0xFE,
        (
            "おお、ロイド団員。\x01",
            "さっそく来てくれたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "見ての通り何もない所だが、\x01",
            "ま、どうか寛いで行ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "それと、材料不足のために\x01",
            "値段は張るんだが、ちょっとした\x01",
            "売り物も用意してあるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "よければ、気軽に見て行ってくれ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 7)

    label("loc_9D4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A41")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_A56")

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A56")
    TurnDirection(0xFE, 0x0, 0)

    label("loc_A56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_END)), "loc_A85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A7E")
    OP_AF(0x37)
    Jump("loc_A80")

    label("loc_A7E")

    OP_AF(0x3B)

    label("loc_A80")

    Jump("loc_A97")

    label("loc_A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A95")
    OP_AF(0x36)
    Jump("loc_A97")

    label("loc_A95")

    OP_AF(0x3A)

    label("loc_A97")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AB6")
    TurnDirection(0xFE, 0x9, 0)

    label("loc_AB6")

    Jump("loc_1625")

    label("loc_ABB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1625")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B71")
    TurnDirection(0xFE, 0x101, 0)

    #C0021
    ChrTalk(
        0xFE,
        (
            "釣皇倶楽部との爆釣勝負……\x01",
            "ロイド団員にも協力をお願いするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "何といっても、この勝負には\x01",
            "釣公師団の未来が懸かってるからなァ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1625")

    label("loc_B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B7F")
    Jump("loc_1625")

    label("loc_B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1040")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_C1C")
    TurnDirection(0xFE, 0x101, 0)

    #C0023
    ChrTalk(
        0xFE,
        (
            "ふむ、ロイド師には\x01",
            "本当に感謝の言葉もないぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "この調子で、今後も更なる\x01",
            "伝説を生み出してくれることを\x01",
            "期待しているぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_103B")

    label("loc_C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C8B")

    #C0025
    ChrTalk(
        0xFE,
        (
            "ふむ、あと少しすれば\x01",
            "あのお方に来ていただける……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        "そうすれば必ず……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_103B")

    label("loc_C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB1")
    TurnDirection(0xFE, 0x101, 0)

    #C0027
    ChrTalk(
        0xFE,
        (
            "ロイド団員、そのメダルは……\x01",
            "まさか、四天王を全員倒したのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#00000Fええ……何とかやりました。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "フハハ、流石はロイド団員だ！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "ふむ、ロイド団員になら\x01",
            "安心してこいつを託せるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "どうか、俺たちの\x01",
            "“魂”を受け取ってくれ！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0032
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x18B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x18B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0033
    ChrTalk(
        0x101,
        "#00005Fこ、これは……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "それは、対釣皇倶楽部のために\x01",
            "俺たちが血反吐を吐きながら\x01",
            "開発に漕ぎ着けた究極の釣りエサだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "セピスを材料にしているので値は張るが……\x01",
            "言ってくれればいくらでも生産可能だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00004Fなるほど……皆さんの\x01",
            "血と汗の結晶というわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "ああ、その通りだ。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "どうかロイド団員……\x01",
            "そいつで、あのレイクロードの\x01",
            "鼻っ柱を折ってくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "ロイド団員になら、\x01",
            "きっとそれが出来るはずだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00001Fは、はい……やってみます！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 5)
    Jump("loc_103B")

    label("loc_FB1")

    TurnDirection(0xFE, 0x101, 0)

    #C0041
    ChrTalk(
        0xFE,
        (
            "ロイド団員……俺たちの\x01",
            "想いと共に、あのレイクロードの\x01",
            "鼻っ柱を折ってくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "ロイド団員になら、\x01",
            "きっとそれが出来るはずだ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_103B")

    Jump("loc_1625")

    label("loc_1040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_104E")
    Jump("loc_1625")

    label("loc_104E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_108F")

    #C0043
    ChrTalk(
        0xFE,
        (
            "う～む、しかし\x01",
            "最終兵器は最終兵器だからなァ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1625")

    label("loc_108F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_109D")
    Jump("loc_1625")

    label("loc_109D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1140")

    #C0044
    ChrTalk(
        0xFE,
        "くそっ、次でもう何度目だ！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "《銀鯱》トリトン……\x01",
            "ヤツは本当に恐ろしい男だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "流石に四天王筆頭は\x01",
            "ワケが違うというわけか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11C0")

    label("loc_1140")


    #C0047
    ChrTalk(
        0xFE,
        (
            "《銀鯱》トリトン……\x01",
            "ヤツは本当に恐ろしい男だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "あのアタリを確実に乗せるなんて……\x01",
            "ヤツには水面の下が見えてるのか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C0")

    Jump("loc_1625")

    label("loc_11C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1241")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DD")
    Jump("loc_123C")

    label("loc_11DD")

    TurnDirection(0xFE, 0x101, 0)

    #C0049
    ChrTalk(
        0xFE,
        (
            "ロイド団員、\x01",
            "今日は本当にありがとうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "おかげで今夜は\x01",
            "ぐっすり眠れそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123C")

    Jump("loc_1625")

    label("loc_1241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1362")
    TurnDirection(0xFE, 0x101, 0)

    #C0051
    ChrTalk(
        0xFE,
        "ロイド団員は知ってるか？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "釣皇倶楽部を倒すと、\x01",
            "なんか変テコな称号が\x01",
            "もらえるみたいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "ちなみに俺は、昨日さっそく\x01",
            "ナルセスって野郎を倒してな。\x01",
            "『水狂ハンター』の称号を得たぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "ふはは、敵が用意した趣向ながら\x01",
            "こいつはちょっと楽しいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13F7")

    label("loc_1362")


    #C0055
    ChrTalk(
        0xFE,
        (
            "俺は昨日、さっそく\x01",
            "ナルセスって野郎を倒してな。\x01",
            "『水狂ハンター』の称号を得たぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "ふはは、敵が用意した趣向ながら\x01",
            "こいつはちょっと楽しいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F7")

    Jump("loc_1625")

    label("loc_13FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1582")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F0")

    #C0057
    ChrTalk(
        0xFE,
        (
            "しかし、こんな気持ちで\x01",
            "釣りに取り組むのは\x01",
            "一体いつぶりだろうなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "若い頃は向こう見ずに\x01",
            "釣具を賭けて爆釣勝負を\x01",
            "挑んだこともあったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "何ていうか、困ったことだが妙に\x01",
            "ワクワクしている自分がいやがるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_157D")

    label("loc_14F0")


    #C0060
    ChrTalk(
        0xFE,
        (
            "ふむ、こんな気持ちで\x01",
            "釣りに取り組むのは\x01",
            "一体いつぶりだろうなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "何ていうか、困ったことだが妙に\x01",
            "ワクワクしている自分がいやがるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157D")

    Jump("loc_1625")

    label("loc_1582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_160E")
    TurnDirection(0xFE, 0x101, 0)

    #C0062
    ChrTalk(
        0xFE,
        (
            "とにもかくにも、\x01",
            "釣公師団・クロスベル支部は\x01",
            "ここから再出発だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "ロイド団員、お互いに\x01",
            "頑張って行くとしようぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1625")

    label("loc_160E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_161C")
    Jump("loc_1625")

    label("loc_161C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1625")

    label("loc_1625")

    Jump("loc_9DE")

    label("loc_162A")

    TalkEnd(0xFE)
    Return()

    # Function_4_498 end

    def Function_5_162E(): pass

    label("Function_5_162E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19F6")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1662")
    Jump("loc_19F6")

    label("loc_1662")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19F6")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 500)

    #C0064
    ChrTalk(
        0xFE,
        "ロイド君、それは……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00003Fええ、間違いなく釣具の\x01",
            "パーツだと思うんですけど、\x01",
            "すごく綺麗ですよね。\x02\x03",

            "#00000F四天王から取り返した釣り場で\x01",
            "珍しい魚を釣ったんですけど……\x01",
            "その魚が吐き出したんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        "……間違いありません。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "それはかつて、旅の凄腕釣師が\x01",
            "使っていた伝説の釣具のパーツです。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "彼がクロスベルを去る時、\x01",
            "この地に封印されたと\x01",
            "聞いていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "まさか、\x01",
            "このような形で見つかるとは！\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00005Fそ、そんなに\x01",
            "凄いものだったんですか……\x02\x03",

            "#00003Fでもどうしましょう。\x01",
            "なら、その人に返した方が……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "いえ、その必要はありません。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……なぜなら彼は言いました。\x01",
            "その釣具は見つけた者が使えと。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "ロイド君、\x01",
            "パーツは全部で４つあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "その全てを手に入れたら\x01",
            "どうか私のところへ来て下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "私ならそのパーツを\x01",
            "組み上げることができます。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00005Fな、なるほど……\x01",
            "分かりました、覚えておきます。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x8, 0)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x1C0, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_19F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1A84")
    TurnDirection(0xFE, 0x101, 0)

    #C0077
    ChrTalk(
        0xFE,
        (
            "かつて封印された伝説の釣具が\x01",
            "このような時に現れるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "ふむ、ロイド君。\x01",
            "これは運命かもしれませんよ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x8, 0)
    Jump("loc_1B98")

    label("loc_1A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1A92")
    Jump("loc_1B98")

    label("loc_1A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1AA0")
    Jump("loc_1B98")

    label("loc_1AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1AAE")
    Jump("loc_1B98")

    label("loc_1AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1B2D")

    #C0079
    ChrTalk(
        0xFE,
        (
            "コパン君も\x01",
            "壁にぶち当たっている\x01",
            "みたいですしねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "やはり、我々の力だけでは\x01",
            "これ以上はどうしようも……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B98")

    label("loc_1B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B3B")
    Jump("loc_1B98")

    label("loc_1B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B49")
    Jump("loc_1B98")

    label("loc_1B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B57")
    Jump("loc_1B98")

    label("loc_1B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1B65")
    Jump("loc_1B98")

    label("loc_1B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B73")
    Jump("loc_1B98")

    label("loc_1B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B81")
    Jump("loc_1B98")

    label("loc_1B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1B8F")
    Jump("loc_1B98")

    label("loc_1B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B98")

    label("loc_1B98")

    TalkEnd(0xFE)
    Return()

    # Function_5_162E end

    def Function_6_1B9C(): pass

    label("Function_6_1B9C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1BAD")
    Jump("loc_1C4F")

    label("loc_1BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C4F")
    TurnDirection(0xFE, 0x101, 0)

    #N0081
    NpcTalk(
        0xFE,
        "フィッシャー団長",
        (
            "ロイド師、君は我が\x01",
            "釣公師団の誇りなのである。\x02",
        )
    )

    CloseMessageWindow()

    #N0082
    NpcTalk(
        0xFE,
        "フィッシャー団長",
        (
            "機会があれば、是非リベールで\x01",
            "共に釣りをしたいものだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4F")

    TalkEnd(0xFE)
    Return()

    # Function_6_1B9C end

    def Function_7_1C53(): pass

    label("Function_7_1C53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C70")
    Call(0, 8)
    TalkEnd(0xFE)
    Return()

    label("loc_1C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CFF")

    #C0083
    ChrTalk(
        0xB,
        (
            "俺たちには、サバイバル術の\x01",
            "心得がある上にエニグマもある。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xB,
        (
            "分かったら、心配などいらんから\x01",
            "さっさと出て行くがいい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D0D")
    Jump("loc_1D92")

    label("loc_1D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1D7B")

    #C0085
    ChrTalk(
        0xB,
        (
            "ふむ、それにしても\x01",
            "独立無効宣言か……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xB,
        (
            "これはますます波乱を含んだ\x01",
            "展開になってきたな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1D89")
    Jump("loc_1D92")

    label("loc_1D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1D92")

    label("loc_1D92")

    TalkEnd(0xFE)
    Return()

    # Function_7_1C53 end

    def Function_8_1D96(): pass

    label("Function_8_1D96")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5E")

    #C0087
    ChrTalk(
        0xB,
        (
            "『大陸諸国連合』の提唱に\x01",
            "祖国エレボニアの内戦……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xB,
        (
            "まさか、この一月ほどで\x01",
            "世俗がここまで動こうとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        (
            "はい……青天のへきれきとは\x01",
            "まさにこのことでございますわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F46")

    label("loc_1E5E")


    #C0090
    ChrTalk(
        0xB,
        (
            "『大陸諸国連合』の提唱に\x01",
            "祖国エレボニアの内戦……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xB,
        (
            "まさか、この一月ほどで\x01",
            "世俗がここまで動こうとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xB,
        (
            "……さらに、ここへ来て\x01",
            "独立無効宣言と来たものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xC,
        (
            "はい……青天のへきれきとは\x01",
            "まさにこのことでございますわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F46")

    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 500)
    Sleep(500)
    TurnDirection(0xC, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2008")
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
            "【変更しない】\x01",        # 0
            "【倒している】\x01",        # 1
            "【倒していない】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FF6")
    SetScenarioFlags(0x191, 1)
    Jump("loc_2008")

    label("loc_1FF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2008")
    ClearScenarioFlags(0x191, 1)

    label("loc_2008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2049")

    #C0094
    ChrTalk(
        0xB,
        (
            "ふむ、貴公は釣公師団の\x01",
            "ロイド・バニングスか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207C")

    label("loc_2049")


    #C0095
    ChrTalk(
        0xB,
        (
            "ふむ、貴様は釣公師団の\x01",
            "ロイド・バニングスか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_207C")


    #C0096
    ChrTalk(
        0x101,
        (
            "#00005Fあなたは釣皇倶楽部の\x01",
            "レイクロードさん……\x01",
            "どうしてこんな所に？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xB,
        (
            "フンッ、どうしても何も\x01",
            "釣りの修行をするためだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xB,
        (
            "なにせ俺は倶楽部の長……\x01",
            "勝負に負けたまま、おめおめと\x01",
            "帰るワケにもいかんのでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00006Fな、なるほど……\x02\x03",

            "#00001Fですが、こんな所に\x01",
            "ずっといるわけには……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        (
            "#00200Fええ、わたしたちが\x01",
            "アルモリカ村に送り届けますので\x01",
            "すぐに避難の準備を……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xC,
        (
            "ふんっ、私たちのことは\x01",
            "放っておいて頂けないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xC,
        (
            "釣師たる者、日頃から\x01",
            "外の危険には慣れていますし、\x01",
            "飢える心配もありませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        (
            "ああ、それに危険と言うなら\x01",
            "どこにいても同じだと思うがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#00005Fで、ですが……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        (
            "とにかく、俺たちにはエニグマもあるし\x01",
            "はっきり言って心配など余計なお世話だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xB,
        "分かったら、さっさと出て行くがいい。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        "#00006Fは、はあ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_250B")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0108
    ChrTalk(
        0xB,
        (
            "ああ……だがせっかく来たのだ。\x01",
            "貴公には手土産をくれてやろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "少々釣りすぎてしまってな。\x01",
            "俺たちだけでは食べきれんのだ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0110
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x168),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を１０匹受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x168, 10)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0111
    ChrTalk(
        0xB,
        (
            "ついでに、こいつは\x01",
            "魚たちが吐き出したものだ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0112
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1FE, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0113
    ChrTalk(
        0x101,
        "#00005Fあ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    label("loc_250B")

    SetScenarioFlags(0x1BD, 2)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)
    Return()

    # Function_8_1D96 end

    def Function_9_2532(): pass

    label("Function_9_2532")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_254F")
    Call(0, 8)
    TalkEnd(0xFE)
    Return()

    label("loc_254F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25C9")

    #C0114
    ChrTalk(
        0xC,
        "……話はもう十分ではなくて？\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        (
            "私たちも色々と忙しいのです。\x01",
            "邪魔をしないで頂きたいものですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267F")

    label("loc_25C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_25D7")
    Jump("loc_267F")

    label("loc_25D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2668")

    #C0116
    ChrTalk(
        0xC,
        (
            "私は、例えどんな困難でも\x01",
            "レイクロード様とご一緒に\x01",
            "乗り越えて行く覚悟ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xC,
        (
            "というより、むしろ\x01",
            "このまま２人きりで……㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267F")

    label("loc_2668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_2676")
    Jump("loc_267F")

    label("loc_2676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_267F")

    label("loc_267F")

    TalkEnd(0xFE)
    Return()

    # Function_9_2532 end

    SaveToFile()

Try(main)
