from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1430.bin",                # FileName
        "c1430",                    # MapName
        "c1430",                    # Location
        0x0032,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 50, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1430",                  # 0
        "ギヨーム親方",           # 1
        "遊撃士スコット",         # 2
        "遊撃士ヴェンツェル",     # 3
        "ロバーツ主任",           # 4
    ))

    AddCharChip((
        "chr/ch26400.itc",                   # 00
        "chr/ch27200.itc",                   # 01
        "chr/ch27300.itc",                   # 02
        "chr/ch29300.itc",                   # 03
    ))

    DeclNpc(5619,    0,       5329,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(550,     0,       4179,    90,   389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(709,     0,       5539,    135,  389,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-51279,  0,       15350,   270,  389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)

    DeclActor(4150,    0,       4740,    1000,    5620,    1500,    5330,    0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_170",          # 00, 0
        "Function_1_228",          # 01, 1
        "Function_2_425",          # 02, 2
        "Function_3_5A5",          # 03, 3
        "Function_4_5C2",          # 04, 4
        "Function_5_DC4",          # 05, 5
        "Function_6_293B",         # 06, 6
        "Function_7_2CC9",         # 07, 7
        "Function_8_2E4B",         # 08, 8
        "Function_9_302A",         # 09, 9
        "Function_10_3082",        # 0A, 10
        "Function_11_34AE",        # 0B, 11
        "Function_12_4D2F",        # 0C, 12
        "Function_13_69C5",        # 0D, 13
    ))


    def Function_0_170(): pass

    label("Function_0_170")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1B0"),
        (1, "loc_1BC"),
        (2, "loc_1C8"),
        (3, "loc_1D4"),
        (4, "loc_1E0"),
        (5, "loc_1EC"),
        (6, "loc_1F8"),
        (SWITCH_DEFAULT, "loc_204"),
    )


    label("loc_1B0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1BC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1C8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1D4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1E0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1EC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_204")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_210")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_227")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_227")

    Return()

    # Function_0_170 end

    def Function_1_228(): pass

    label("Function_1_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_253")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_2B8")

    label("loc_253")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_28C")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    SetChrPos(0xB, 5620, 0, 5330, 270)
    Jump("loc_2B8")

    label("loc_28C")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 1040, 0, 7000, 270)
    SetChrPos(0xB, -490, 0, 7000, 90)
    SetChrFlags(0xB, 0x10)

    label("loc_2B8")

    Jump("loc_424")

    label("loc_2BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2CB")
    Jump("loc_424")

    label("loc_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2E3")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_424")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2F1")
    Jump("loc_424")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_310")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_424")

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_31E")
    Jump("loc_424")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_32C")
    Jump("loc_424")

    label("loc_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33A")
    Jump("loc_424")

    label("loc_33A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_348")
    Jump("loc_424")

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_356")
    Jump("loc_424")

    label("loc_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_364")
    Jump("loc_424")

    label("loc_364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_383")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_424")

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_391")
    Jump("loc_424")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_END)), "loc_3CA")
    SetChrPos(0x8, 14820, 1000, 8970, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14820, 1000, 7170, 0)

    label("loc_3CA")

    Jump("loc_424")

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3DD")
    Jump("loc_424")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3EB")
    Jump("loc_424")

    label("loc_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_40A")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_424")

    label("loc_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_424")
    SetChrPos(0x8, 15240, 1000, 7610, 90)

    label("loc_424")

    Return()

    # Function_1_228 end

    def Function_2_425(): pass

    label("Function_2_425")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43E")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_444")

    label("loc_43E")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_444")

    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    ClearMapObjFlags(0x0, 0x4)

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_49E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_483")
    OP_65(0x0, 0x1)
    Jump("loc_499")

    label("loc_483")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_495")
    Jump("loc_499")

    label("loc_495")

    OP_65(0x0, 0x1)

    label("loc_499")

    Jump("loc_5A4")

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4AC")
    Jump("loc_5A4")

    label("loc_4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4BA")
    Jump("loc_5A4")

    label("loc_4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4C8")
    Jump("loc_5A4")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4DA")
    OP_65(0x0, 0x1)
    Jump("loc_5A4")

    label("loc_4DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4E8")
    Jump("loc_5A4")

    label("loc_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4F6")
    Jump("loc_5A4")

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_504")
    Jump("loc_5A4")

    label("loc_504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_512")
    Jump("loc_5A4")

    label("loc_512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_520")
    Jump("loc_5A4")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_52E")
    Jump("loc_5A4")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_540")
    OP_65(0x0, 0x1)
    Jump("loc_5A4")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_54E")
    Jump("loc_5A4")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_569")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_END)), "loc_564")
    OP_65(0x0, 0x1)

    label("loc_564")

    Jump("loc_5A4")

    label("loc_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_577")
    Jump("loc_5A4")

    label("loc_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_585")
    Jump("loc_5A4")

    label("loc_585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_597")
    OP_65(0x0, 0x1)
    Jump("loc_5A4")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5A4")
    OP_65(0x0, 0x1)

    label("loc_5A4")

    Return()

    # Function_2_425 end

    def Function_3_5A5(): pass

    label("Function_3_5A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BE")
    Call(0, 10)
    Return()

    label("loc_5BE")

    Call(0, 4)
    Return()

    # Function_3_5A5 end

    def Function_4_5C2(): pass

    label("Function_4_5C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E3")
    Call(0, 11)
    Return()

    label("loc_5E3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62E")

    #C0001
    ChrTalk(
        0x8,
        (
            "よう、お前ぇらか。\x01",
            "……何か改造するかよ？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 7)
    SetScenarioFlags(0x4E, 4)
    Jump("loc_91A")

    label("loc_62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_904")

    #C0002
    ChrTalk(
        0x8,
        (
            "おう、いらっしゃい。\x01",
            "今日は何にしやしょうかい？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_END)), "loc_6B8")

    #C0003
    ChrTalk(
        0x8,
        (
            "……ってお前ぇらかい。\x01",
            "確か警察の『特務支援課』の。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FE")

    label("loc_6B8")


    #C0004
    ChrTalk(
        0x8,
        (
            "……ってお前ぇらかい。\x01",
            "確かクロスベルタイムズに\x01",
            "載ってた警察の。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FE")


    #C0005
    ChrTalk(
        0x8,
        (
            "まあいいや、\x01",
            "何か注文してってくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "俺んとこは導力製品の修理が\x01",
            "メインだが、武器の強化改造なんかも\x01",
            "請け負ってるぜい！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0005F強化改造、ですか……？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "おう、色んな『素材』を使って\x01",
            "武器の構造を強化したりするワケだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "こんなナリだが\x01",
            "俺は昔エプスタイン財団で\x01",
            "材料工学を専門にしてた事があってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "腕は信用してもらって構わねえぜ？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        (
            "#0200F財団の人でしたか……\x01",
            "それはちょっと凄そうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#0300Fああ、他にはねえ強力な武器が\x01",
            "手に入りそうだよな。\x02\x03",

            "材料があれば\x01",
            "頼んでみたい所だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 7)
    SetScenarioFlags(0x4E, 4)
    Jump("loc_91A")

    label("loc_904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91A")
    Call(0, 6)
    TalkEnd(0x8)
    Return()

    label("loc_91A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D6")

    #C0013
    ChrTalk(
        0x8,
        (
            "おう、『Ｔマテリアル』を\x01",
            "手に入れてきたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "魔導杖をアップデートすんなら\x01",
            "そう言ってくれ。\x01",
            "大体の準備はできてるからよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D6")

    SetScenarioFlags(0x0, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAF")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                # 0
            "改造を頼む\x01",              # 1
            "アップデートを頼む\x01",      # 2
            "やめる\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A52")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_A52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A71")
    OP_AF(0xAE)
    Jump("loc_AA3")

    label("loc_A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A81")
    OP_AF(0xAD)
    Jump("loc_AA3")

    label("loc_A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A91")
    OP_AF(0xAC)
    Jump("loc_AA3")

    label("loc_A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_AA1")
    OP_AF(0xAB)
    Jump("loc_AA3")

    label("loc_AA1")

    OP_AF(0xAA)

    label("loc_AA3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CAA")

    label("loc_AB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7A")

    #C0015
    ChrTalk(
        0x8,
        (
            "魔導杖をアップデートすると\x01",
            "手持ちの材料を使うことになるが……\x01",
            "今やっちまうかよ？\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【頼む】\x01",            # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0C")

    #C0016
    ChrTalk(
        0x101,
        "#0000Fええ、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "うっし、なら始めるとするか。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 500)
    Sleep(300)

    #C0018
    ChrTalk(
        0x8,
        (
            "ロバーツ、\x01",
            "そっちの準備はいいかよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        "おっ、材料が手に入ったようだね。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xB,
        "今そっちに行くよ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 12)
    Return()

    label("loc_C0C")


    #C0021
    ChrTalk(
        0x8,
        (
            "そうかい、またアップデートを\x01",
            "したくなったら言ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "準備だけは整えておくからよ。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CAA")

    label("loc_C7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C8E")
    Jump("loc_CAA")

    label("loc_C8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_CAA")

    Jump("loc_9E3")

    label("loc_CAF")

    Jump("loc_DC0")

    label("loc_CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_DBD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB8")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "改造を頼む\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D23")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_D23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D42")
    OP_AF(0xAE)
    Jump("loc_D74")

    label("loc_D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D52")
    OP_AF(0xAD)
    Jump("loc_D74")

    label("loc_D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D62")
    OP_AF(0xAC)
    Jump("loc_D74")

    label("loc_D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_D72")
    OP_AF(0xAB)
    Jump("loc_D74")

    label("loc_D72")

    OP_AF(0xAA)

    label("loc_D74")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DB3")

    label("loc_D83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D97")
    Jump("loc_DB3")

    label("loc_D97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_DB3")

    Jump("loc_CC7")

    label("loc_DB8")

    Jump("loc_DC0")

    label("loc_DBD")

    Call(0, 5)

    label("loc_DC0")

    TalkEnd(0x8)
    Return()

    # Function_4_5C2 end

    def Function_5_DC4(): pass

    label("Function_5_DC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E6A")

    #C0023
    ChrTalk(
        0x8,
        (
            "必要な材料は『Ｔマテリアル』っつー\x01",
            "特別な素材が１個だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "俺たちは準備を進めておくからよ。\x01",
            "素材が揃ったら声を掛けてくんな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293A")

    label("loc_E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_F51")

    #C0025
    ChrTalk(
        0x8,
        (
            "今回の改造、\x01",
            "俺は大した事はしてねえんだ。\x01",
            "設計図どおり作っただけだからよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "へへっ、気にせずお前ぇらで\x01",
            "活用してやってくんな！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        "#0200Fええ、早速試してみようかと。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0000F本当にありがとうございました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_293A")

    label("loc_F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_115D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_111E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FDC")

    #C0029
    ChrTalk(
        0x8,
        "参ったな、すっかり忘れてたぜ。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "警備員の兄ちゃん、\x01",
            "関係者だって言ったら\x01",
            "通してくれんのかねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1119")

    label("loc_FDC")


    #C0031
    ChrTalk(
        0x8,
        "おっと、夕方か……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "今日は財団支部に\x01",
            "顔を出そうと思ってたんだが。\x01",
            "すっかり忘れちまってたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        "#0205Fエプスタイン財団の支部にですか？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "おう、向こうでロバーツの奴と\x01",
            "語り合おうかと思ってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "いやだが参ったな。\x01",
            "支部はＩＢＣビルにあるから……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "今の時間、閉まっちまってるかも\x01",
            "しれねえなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 4)
    SetScenarioFlags(0x0, 0)

    label("loc_1119")

    Jump("loc_1158")

    label("loc_111E")


    #C0037
    ChrTalk(
        0x8,
        "よ、よう、お前ぇらか。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        "……なんか改造するかよ？\x02",
    )

    CloseMessageWindow()

    label("loc_1158")

    Jump("loc_293A")

    label("loc_115D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_121E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11DF")

    #C0039
    ChrTalk(
        0x8,
        (
            "今朝は街の様子が\x01",
            "どっかおかしかった気がすんなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "うーむ、徹夜明けだった\x01",
            "せいかもしんねえが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1219")

    label("loc_11DF")


    #C0041
    ChrTalk(
        0x8,
        "よ、よう、お前ぇらか。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        "……なんか改造するかよ？\x02",
    )

    CloseMessageWindow()

    label("loc_1219")

    Jump("loc_293A")

    label("loc_121E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_132D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1295")

    #C0043
    ChrTalk(
        0x8,
        (
            "俺はもう歳だ、\x01",
            "生き方は変えられねえや。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "ま、ここで死ぬまで\x01",
            "修理屋をやらせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1328")

    label("loc_1295")


    #C0045
    ChrTalk(
        0x8,
        (
            "昨日久々に\x01",
            "ウェンディの奴に会ったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "仕事にも慣れたって言ってやがった。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "へっ……若いってのはいいねぇ。\x01",
            "何にでも柔軟になれらぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1328")

    Jump("loc_293A")

    label("loc_132D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_14EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 2)), scpexpr(EXPR_END)), "loc_1410")

    #C0048
    ChrTalk(
        0x8,
        (
            "エプスタイン財団のロバーツは\x01",
            "向こうに居た頃の仕事仲間なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "当時のエプスタイン財団には\x01",
            "導力技術を学びに\x01",
            "各国から若いのが集まっててよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "俺やロバーツみてえのが\x01",
            "その一員だったってぇわけよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E7")

    label("loc_1410")


    #C0051
    ChrTalk(
        0x8,
        (
            "改造武器のアイデアに\x01",
            "煮詰まってたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "ロバーツの奴に相談してな。\x01",
            "まずは納得の行く設計図が出来たぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "まだまだ改良の余地はあるが、\x01",
            "ラインナップにも挙げておいたぜ。\x01",
            "良かったら試してみてくれや。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 2)

    label("loc_14E7")

    Jump("loc_293A")

    label("loc_14EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_167B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1565")

    #C0054
    ChrTalk(
        0x8,
        (
            "何か困った事があれば\x01",
            "遠慮なく声をかけてくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "俺にできる事なら\x01",
            "何でもしてやっからよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1676")

    label("loc_1565")


    #C0056
    ChrTalk(
        0x8,
        (
            "特務支援課の\x01",
            "お出ましとは光栄だねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "活躍の噂は聞いたぜ？\x01",
            "ヤバイ事になってた\x01",
            "らしいじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#0003Fはは……そうなんですよね。\x01",
            "ようやく一段落したんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "何か困った事があれば\x01",
            "俺に声をかけな。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "へへっ、匿ってやるくらいの事は\x01",
            "できっからなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1676")

    Jump("loc_293A")

    label("loc_167B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_17A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16F3")

    #C0061
    ChrTalk(
        0x8,
        (
            "凝り性なのはいけねえなぁ……\x01",
            "つい高みを目指しちまうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        "……ま、それが楽しいんだがよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_17A2")

    label("loc_16F3")


    #C0063
    ChrTalk(
        0x8,
        (
            "新しい改造武器の\x01",
            "設計図を引いてる所だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "うーむ、ああでもねえ、\x01",
            "こうでもねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "俺ぁつい最高傑作を\x01",
            "作ろうとしちまうからな。\x01",
            "中々思うように纏まらねえのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_17A2")

    Jump("loc_293A")

    label("loc_17A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1827")

    #C0066
    ChrTalk(
        0x8,
        (
            "どっかに出掛けんなら気を付けな！\x01",
            "外はすげえ人出らしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "ま、パレードの後は\x01",
            "毎年混雑しまくるからなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293A")

    label("loc_1827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_193A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FA")

    #C0068
    ChrTalk(
        0x8,
        (
            "今日は導力おもちゃの修理が\x01",
            "１件にぃ……っと。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "記念祭の間も\x01",
            "ちらほら仕事が入っててな、\x01",
            "これで意外と忙しいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "試したいマテリアルの\x01",
            "強度テストなんかも溜まってるしなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1935")

    label("loc_18FA")


    #C0071
    ChrTalk(
        0x8,
        (
            "記念祭の間も休業の予定はねえぜ。\x01",
            "遠慮なく来てくれや。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1935")

    Jump("loc_293A")

    label("loc_193A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19BF")

    #C0072
    ChrTalk(
        0x8,
        (
            "導力ネットっていやあ\x01",
            "飛行船と並んで導力技術の粋だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "俺もちっとは興味あるんだが、\x01",
            "旧市街じゃなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A7B")

    label("loc_19BF")


    #C0074
    ChrTalk(
        0x8,
        (
            "この旧市街で、どんなに\x01",
            "頑張っても手に入らねえもの……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "そりゃあ導力ネットだな。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "なにせ旧市街だ。\x01",
            "ケーブルが敷設されてねえんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "俺もちっとは\x01",
            "興味あるんだがなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A7B")

    Jump("loc_293A")

    label("loc_1A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 4)), scpexpr(EXPR_END)), "loc_1B0F")

    #C0078
    ChrTalk(
        0x8,
        (
            "おりゃあ、お前ぇらみてえな\x01",
            "威勢のいい連中が大好きだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "これからも職務に励んでくれよ！\x01",
            "活躍、期待してるいぜぃ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5B")

    label("loc_1B0F")


    #C0080
    ChrTalk(
        0x8,
        (
            "ハッピー・アニバーサリー＆\x01",
            "ハッピー・クロスベール！\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "いよう、市長暗殺を\x01",
            "食い止めた英雄たち！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0006F……すごくハズい\x01",
            "言い方なんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        "俺はハズい言い方が大好きだ。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "これからも職務に励んでくれよ！\x01",
            "活躍、期待してるいぜぃ！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        "#0300Fういーっす。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        (
            "#0100Fまあ、好意はありがたく\x01",
            "受け取っておくものよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 4)

    label("loc_1C5B")

    Jump("loc_293A")

    label("loc_1C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1D50")

    #C0087
    ChrTalk(
        0x8,
        (
            "改造に使う『Ｕマテリアル』は\x01",
            "魔獣が落とす事があるらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "それ以外にも、思わぬ所から\x01",
            "入手できる事もあるらしいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "まあ、見慣れねえ素材が手に入ったら\x01",
            "大切に持ってるといいぜ。\x01",
            "何かの改造に使えるかもしれねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293A")

    label("loc_1D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1E9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DF4")

    #C0090
    ChrTalk(
        0x8,
        (
            "クロスベルには\x01",
            "導力鉄道も飛行船も通ってっから\x01",
            "錯覚に陥んのかもしれねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "ったく、こんなに恵まれてるのは\x01",
            "クロスベルだけなんだぜ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E9A")

    label("loc_1DF4")


    #C0092
    ChrTalk(
        0x8,
        (
            "クロスベル人は\x01",
            "新しい導力製品を買って\x01",
            "古いものは捨てちまうらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        "やれやれ贅沢な話だぜ。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "世界には導力化が進んでねえ\x01",
            "地域もたくさんあるってのによ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E9A")

    Jump("loc_293A")

    label("loc_1E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F24")

    #C0095
    ChrTalk(
        0x8,
        (
            "いま新しい改造武器の\x01",
            "試作品を作ってんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "完成を楽しみにしててくれや。\x01",
            "そのうち見せてやっからよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_204D")

    label("loc_1F24")


    #C0097
    ChrTalk(
        0x8,
        (
            "いま新しい改造武器の\x01",
            "試作品を仕上げてんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "へっへ、こいつはすげえぜ？\x01",
            "この俺がイチから設計図を引いた\x01",
            "オリジナル武器だあ！\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "……いやな、色々手がけてるうちに\x01",
            "自分でも作りたくなっちまったわけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "まだ試作品だが……\x01",
            "完成を楽しみにしててくれや。\x01",
            "お前ぇらにも見せてやっからよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_204D")

    Jump("loc_293A")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_21E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20E5")

    #C0101
    ChrTalk(
        0x8,
        "ウェンディの奴は元気にしてっかねえ。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "手が空いてんなら\x01",
            "うちに来てほしいくらいなんだが。\x01",
            "……ま、そうはいかねえか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E0")

    label("loc_20E5")


    #C0103
    ChrTalk(
        0x8,
        "ウェンディの奴は元気にしてるかい？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "あいつは俺が工房に勤めてた頃の\x01",
            "弟子でな、中々腕のいい奴だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "オーバルストアに嫌気が差したら\x01",
            "うちに来て手伝ってくんねえかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "近頃、修理の依頼と\x01",
            "改造に懲りだしちまって……\x01",
            "手が足りねえんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_21E0")

    Jump("loc_293A")

    label("loc_21E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_22C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_END)), "loc_2262")

    #C0107
    ChrTalk(
        0x8,
        (
            "ロバーツとは\x01",
            "財団に居た頃からの親友なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "にしても、こいつは\x01",
            "２０年前から変わんねえなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C1")

    label("loc_2262")


    #C0109
    ChrTalk(
        0x8,
        "おう、朝からお出掛けかい？\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "どこに行くんだか知らねえが\x01",
            "バッチリ準備だけはしときなよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C1")

    Jump("loc_293A")

    label("loc_22C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_234A")

    #C0111
    ChrTalk(
        0x8,
        (
            "今日は修理の依頼が\x01",
            "３件も入っちまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "チィ、まったく手が足りねえや。\x01",
            "助手みてえなのがいりゃいいんだが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293A")

    label("loc_234A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2545")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_END)), "loc_2419")

    #C0113
    ChrTalk(
        0x8,
        (
            "俺ぁ昔から\x01",
            "導力製品いじりが好きでねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "最近は修理屋の他に\x01",
            "武器の強化改造なんかも手がけてるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "へへっ、お前ぇらも\x01",
            "利用して行ってくれや。\x01",
            "これでも腕利きのつもりだしよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2540")

    label("loc_2419")


    #C0116
    ChrTalk(
        0x8,
        (
            "そういやお前ぇら、\x01",
            "なんだかご活躍だったみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "あのクロスベルタイムズに載ってた\x01",
            "『警察』ってのは\x01",
            "お前ぇらの事だろ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 5)), scpexpr(EXPR_END)), "loc_2502")

    #C0118
    ChrTalk(
        0x8,
        (
            "へへ、さすがは\x01",
            "ウェンディの幼馴染だ。\x01",
            "頼りにならぁな。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        "#0000Fはは、どうも……\x02",
    )

    CloseMessageWindow()
    Jump("loc_253D")

    label("loc_2502")


    #C0120
    ChrTalk(
        0x8,
        (
            "へへ、お陰で表が静かになった。\x01",
            "礼を言わせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253D")

    SetScenarioFlags(0x6B, 4)

    label("loc_2540")

    Jump("loc_293A")

    label("loc_2545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_265F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_25D5")

    #C0121
    ChrTalk(
        0x8,
        (
            "お前ぇらも\x01",
            "また今度寄ってくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "今日はパーツを切らしちまってるが、\x01",
            "いつもは修理なんかを\x01",
            "請け負ってるからよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265A")

    label("loc_25D5")


    #C0123
    ChrTalk(
        0x8,
        (
            "旧市街暮らしも意外と悪くねえぜ。\x01",
            "ジャンクパーツも結構手に入るしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "うっし、これから早速\x01",
            "パーツの発掘に向かうとするか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_265A")

    Jump("loc_293A")

    label("loc_265F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B9")

    #C0125
    ChrTalk(
        0x8,
        (
            "俺は元々市街の\x01",
            "工房に勤めてたんだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "だが去年、オーバルストアとかいう\x01",
            "意味の判んねえ店に変わっちまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "てやんでぃってなわけで、\x01",
            "自分の工房を持つ事にしたわけよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28B1")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0128
    ChrTalk(
        0x101,
        (
            "#0005Fあれ、それじゃあ\x01",
            "ウェンディの言ってた\x01",
            "師匠ってのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "ん……？\x01",
            "ウェンディの奴を知ってるのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0130
    ChrTalk(
        0x8,
        (
            "そうか、お前ぇ\x01",
            "ウェンディの言ってた幼馴染だな？\x01",
            "……警察の方の！\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#0000Fははは……\x01",
            "色々聞かれてたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "おうよ、ウェンディは前の工房時代\x01",
            "俺の弟子だったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "へへ、その分だと\x01",
            "元気にしてるみてえだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 5)

    label("loc_28B1")

    SetScenarioFlags(0x0, 0)
    Jump("loc_293A")

    label("loc_28B9")


    #C0134
    ChrTalk(
        0x8,
        (
            "お前ぇらも\x01",
            "また何かあったら寄ってくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "今日はパーツを切らしちまってるが、\x01",
            "いつもは修理なんかを\x01",
            "請け負ってるからよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_293A")

    Return()

    # Function_5_DC4 end

    def Function_6_293B(): pass

    label("Function_6_293B")

    EventBegin(0x0)
    Fade(500)
    OP_68(14750, 2250, 7600, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 13750, 1000, 7200, 90)
    SetChrPos(0x102, 13650, 1000, 8000, 90)
    SetChrPos(0x103, 12500, 1000, 7200, 90)
    SetChrPos(0x104, 12400, 1000, 8000, 90)
    OP_93(0x8, 0x10E, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    #C0136
    ChrTalk(
        0x8,
        "おう、お客さんか。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "すいやせんねえ、\x01",
            "今日はパーツを切らしちまっててよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "仕事の依頼なら\x01",
            "また今度にしてくれねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0005Fえっと……\x01",
            "ここは工房店ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x103,
        (
            "#0203F（カチャカチャ……）\x02\x03",

            "#0200Fデータベースには\x01",
            "載っていませんね……\x01",
            "営業許可もないようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "はっはっは、確かに\x01",
            "届けは出してねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "ここは俺の個人的な工房で\x01",
            "正式な店ってわけじゃねえんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "ただ、時々ぶっ壊れた導力製品の\x01",
            "修理なんかも請け負ってるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        "#0200F修理屋、というわけですか。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        (
            "#0300Fはー、さすがクロスベルだ。\x01",
            "色んな店があるねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        (
            "#0103Fでも……やっぱり営業許可は\x01",
            "貰った方がいいと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        "はは、違いねえ。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        (
            "まあ今日は店じまいしてるが、\x01",
            "また何かあったら立ち寄ってくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "導力灯が切れた程度なら\x01",
            "格安で直してやるぜい！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 13750, 1000, 7600, 90)
    SetScenarioFlags(0x4A, 3)
    EventEnd(0x5)
    Return()

    # Function_6_293B end

    def Function_7_2CC9(): pass

    label("Function_7_2CC9")

    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)

    #A0150
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ギヨーム親方に話しかけて『改造を頼む』を選択すると、\x01",
            "  改造可能な商品が一覧表示されます。\x01",
            "  必要な素材を持っていれば、改造を行えます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0151
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※改造によってできた武器・防具は\x01",
            "  武器商会などでは入手出来ない強力なもので、\x01",
            "  特に武器には特殊な効果がついていることがあります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※改造に必要な『素材』は、\x01",
            "  主に魔獣が落とすことがあります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Return()

    # Function_7_2CC9 end

    def Function_8_2E4B(): pass

    label("Function_8_2E4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3026")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F9B")

    #C0153
    ChrTalk(
        0xFE,
        (
            "……うん、新品同様だ。\x01",
            "さすがこの店は腕がいいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        (
            "#0000Fスコットさんは\x01",
            "この店の常連なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        (
            "#0100Fい、一応この店って\x01",
            "違法営業みたいなんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "はは、固いこと言うなよ。\x01",
            "君たちも来てるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "いいものは活用してかないと\x01",
            "とてもクロスベルで遊撃士なんて\x01",
            "やってらんないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3026")

    label("loc_2F9B")


    #C0158
    ChrTalk(
        0xFE,
        (
            "今日は修理に出してたライフルを\x01",
            "受け取りに来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "どうも最近、強い魔獣が\x01",
            "増えてきたみたいだからな。\x01",
            "装備は万全にしとかないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3026")

    TalkEnd(0xFE)
    Return()

    # Function_8_2E4B end

    def Function_9_302A(): pass

    label("Function_9_302A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_307E")

    #C0160
    ChrTalk(
        0xFE,
        (
            "ふむ……\x01",
            "俺も今度、エニグマが壊れたら\x01",
            "ここに持ってくるとするか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_307E")

    TalkEnd(0xFE)
    Return()

    # Function_9_302A end

    def Function_10_3082(): pass

    label("Function_10_3082")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30A3")
    Call(0, 11)
    Return()

    label("loc_30A3")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3319")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326E")

    #C0161
    ChrTalk(
        0xB,
        (
            "僕は追加プログラムの\x01",
            "準備を進めておくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        (
            "大規模なアップデートになるからね。\x01",
            "コンポーネントの解凍だけで\x01",
            "結構時間かかっちゃうんだよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#0200F主任、カウンターに居ると\x01",
            "お店の人に見えて\x01",
            "紛らわしいです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xB, 0x103, 500)
    Sleep(500)

    #C0164
    ChrTalk(
        0xB,
        (
            "ご、ごめんよティオ君！\x01",
            "だってこの店、暗いんだもの！\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        (
            "#0106F（ティオちゃん……あまり\x01",
            "  主任さんをいじめないようにね？）\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x103,
        "#0203F（すみません、つい……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3314")

    label("loc_326E")


    #C0167
    ChrTalk(
        0xB,
        (
            "追加プログラムの準備は\x01",
            "こっちでやっておくからね。\x01",
            "心配は要らないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "素材が手に入ったら\x01",
            "ギヨームに声を掛けてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xB,
        (
            "改造の準備を\x01",
            "しているはずだからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3314")

    Jump("loc_34AA")

    label("loc_3319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3376")

    #C0170
    ChrTalk(
        0xB,
        "うふふ、準備はバッチリだよ。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xB,
        (
            "必要なツールは\x01",
            "一通り持ってきてるしね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AA")

    label("loc_3376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_33FE")

    #C0172
    ChrTalk(
        0xB,
        (
            "ギヨームとは古い友人でね。\x01",
            "時々連絡を取り合っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "ハハハ、彼が修理屋を始めたなんて\x01",
            "知らなかったなぁ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AA")

    label("loc_33FE")


    #C0174
    ChrTalk(
        0xB,
        (
            "やあティオ君、\x01",
            "アナライザーの調子はどう？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        "よかったら調整してあげようか……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x103,
        (
            "#0200F結構です。\x01",
            "自分でやった方が早いので。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "がーん……\x01",
            "そ、そうだよね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_34AA")

    TalkEnd(0xB)
    Return()

    # Function_10_3082 end

    def Function_11_34AE(): pass

    label("Function_11_34AE")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(510, 1000, 6090, 0)
    MoveCamera(42, 23, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(28680, 0)
    SetChrPos(0x101, 380, 0, 4670, 0)
    SetChrPos(0x102, -230, 0, 3500, 0)
    SetChrPos(0x103, -830, 0, 4330, 0)
    SetChrPos(0x104, 1200, 0, 4160, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3560")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, 780, 0, 2600, 0)

    label("loc_3560")

    SetChrPos(0x8, 1000, 0, 7430, 270)
    SetChrPos(0xB, -400, 0, 7430, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    #C0178
    ChrTalk(
        0x8,
        (
            "#11Pおう来たか。\x01",
            "特務支援課の面々！\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#12P#0000Fどうも、支援要請を\x01",
            "伺って参りました。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x104,
        (
            "#12P#0300Fちゃーす、修理屋のオッサン。\x01",
            "いつも世話になってるぜ。\x02\x03",

            "#0305Fつーか、えっと……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x13B, 0x1F4)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(700)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    def lambda_3685():
        OP_95(0xFE, -870, 0, 5820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3685)

    #C0181
    ChrTalk(
        0xB,
        "#5Pやあティオ君、久し振りだねぇ～！\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xB,
        (
            "#5P最近調子はどう？\x01",
            "風邪なんて引いてないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#6P#0205F主任、ここに来ていたんですか。\x02\x03",

            "#0211Fというか\x01",
            "そう久しくもない訳ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        (
            "#12P#0109Fあはは……\x01",
            "（ティオちゃんは主任さんと\x01",
            "  ちょっと微妙な関係なのよね。）\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AA2")

    #C0185
    ChrTalk(
        0x10A,
        (
            "#12P#0603Fエプスタイン財団のロバーツ氏……\x01",
            "それに元財団技師のギヨーム氏か。\x02\x03",

            "#0600Fフム、話は大体読めた。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_387D():
        TurnDirection(0xFE, 0x10A, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_387D)

    def lambda_388A():
        TurnDirection(0xFE, 0x10A, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_388A)

    def lambda_3897():
        TurnDirection(0xFE, 0x10A, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3897)

    def lambda_38A4():
        TurnDirection(0xFE, 0x10A, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_38A4)
    Sleep(300)

    #C0186
    ChrTalk(
        0x101,
        "#11P#0005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x10A,
        (
            "#12P#0600F私は外で待っている。\x01",
            "お前たちは用事を済ませてから来い。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x10A, 300, 0, -1400, 2000, 0x0)
    OP_95(0x10A, 300, 0, -3210, 2000, 0x0)

    #C0188
    ChrTalk(
        0xB,
        (
            "#5Pあれはティオ君の上司の人かい？\x01",
            "随分と切れ者みたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        (
            "#6P#0203Fはあ、ダドリーさんと言って\x01",
            "捜査一課の方です。\x01",
            "今は少々事情がありまして。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_39D6():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39D6)

    def lambda_39E3():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39E3)

    def lambda_39F0():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_39F0)

    def lambda_39FD():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39FD)
    Sleep(500)

    #C0190
    ChrTalk(
        0x102,
        (
            "#12P#0105Fそれで……お２人は\x01",
            "お話中だったみたいですけど、\x01",
            "もしかしてお邪魔だったでしょうか。\x02\x03",

            "#0100F私たちなら出直してきても\x01",
            "構いませんけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B33")

    label("loc_3AA2")

    OP_93(0x101, 0x0, 0x1F4)
    OP_93(0x104, 0x0, 0x1F4)
    Sleep(300)

    #C0191
    ChrTalk(
        0x102,
        (
            "#12P#0105Fお話中だったみたいですけど\x01",
            "もしかしてお邪魔だったでしょうか。\x02\x03",

            "#0100F私たちなら出直してきても\x01",
            "構いませんけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B33")


    #C0192
    ChrTalk(
        0x8,
        (
            "#11Pいやいや、それには及ばねえ。\x01",
            "実は今回の依頼はロバーツの奴が\x01",
            "言い出したことでなぁ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0xB, 0x8, 500)
    Sleep(500)
    OP_95(0xB, -210, 0, 6430, 5000, 0x0)

    #C0193
    ChrTalk(
        0xB,
        (
            "#5Pわああ、ギヨーム！？\x01",
            "それは黙っててくれと……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x103,
        "#6P#0211Fじ～～～……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xB, 0x103, 500)
    Sleep(300)

    #C0195
    ChrTalk(
        0xB,
        (
            "#5Pち、違うんだよ？\x01",
            "別にやましい事が\x01",
            "あるわけじゃなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "#5Pその、これには\x01",
            "深い事情があってね！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#12P#0005F深い事情……ですか。\x02\x03",

            "#0001Fご依頼に関係のある事みたいですね。\x01",
            "話していただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        "#5Pそ、そうだね、お話ししよう。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        "#5P実は財団がらみの話なんだが。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0200
    ChrTalk(
        0xB,
        (
            "#5Pティオ君がクロスベルで\x01",
            "魔導杖の実戦データ収集をしていた事は\x01",
            "知っていると思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xB,
        (
            "#5Pティオ君が提出してくれている\x01",
            "使用記録を参考に\x01",
            "魔導杖は改良を重ねていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xB,
        (
            "#5Pこのたび、ついに\x01",
            "魔導杖の新機能解放に\x01",
            "メドが立ったらしいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#12P#0005F新機能の解放……\x01",
            "って、どういうことですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x104,
        (
            "#12P#0305Fティオすけに\x01",
            "新しい便利機能でも付くのかよ！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(200)

    #C0205
    ChrTalk(
        0x103,
        (
            "#6P#0203Fランディさん、別にわたしには\x01",
            "便利機能なんて付いていませんが……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3FC3():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3FC3)

    def lambda_3FD0():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FD0)

    def lambda_3FDD():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FDD)
    Sleep(400)

    #C0206
    ChrTalk(
        0x103,
        (
            "#6P#0200F魔導杖にはまだいくつか\x01",
            "開封されていない機能があります。\x02\x03",

            "#0203F安定して発動させるプログラムが\x01",
            "無いためですが……\x02\x03",

            "#0200Fそのプログラム完成の\x01",
            "見込みがたった、\x01",
            "ということだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x102,
        "#12P#0105F一体どういった機能なのかしら。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        (
            "#5Pそうだね、一言で言うと\x01",
            "新しい戦技#4Rクラフト#に関するものだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4126():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4126)

    def lambda_4133():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4133)

    def lambda_4140():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4140)

    def lambda_414D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_414D)
    Sleep(300)

    #C0209
    ChrTalk(
        0xB,
        (
            "#5P新プログラムの適用によって\x01",
            "高出力の技が使えるようになるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x8,
        (
            "#11Pま、俺も資料を見せてもらったが\x01",
            "かなり強力らしくてなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x8,
        (
            "#11P今のままじゃ、\x01",
            "危なくて発動できねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "#11Pハンドグリップの改良なんかが\x01",
            "必要になりそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#12P#0003Fな、なんだか凄そうですね……\x02\x03",

            "#0005Fそれをティオが\x01",
            "使えるようになるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        (
            "#11Pいや、そこで一つ\x01",
            "トラブルがあってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x8,
        (
            "#11P財団側で用意した\x01",
            "追加プログラムとアタッチパーツの\x01",
            "到着が遅れてんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "#11P向こう側の手違いとかで、\x01",
            "一週間くらい掛かっちまうそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xB,
        "#5P依頼というのはその事なんだよね。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        (
            "#5Pこのままじゃ\x01",
            "ティオ君も困っちゃうだろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "#5P僕たちで何とかしてあげよう\x01",
            "という事になったわけさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x104,
        (
            "#12P#0300Fああ、それで依頼が\x01",
            "『新機能の開発』だったわけッスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x102,
        "#12P#0100Fようやく納得がいきました。\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x103,
        (
            "#6P#0203F……別に一週間くらい\x01",
            "遅れて困る事はないですが……\x02\x03",

            "#0200F確かに、早く見てみたい気もします。\x01",
            "わたしが一時期手がけていた\x01",
            "プログラムでもあるので。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそうだな……\x01",
            "ティオが戦力アップしてくれれば\x01",
            "探索も楽になりそうだし。\x02\x03",

            "#0005Fでも主任さん、財団からの発送が\x01",
            "遅れているのでは仕方ないのでは？\x01",
            "他に方法でもあるんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)
    OP_63(0xB, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    #C0224
    ChrTalk(
        0xB,
        (
            "#5Pふふ、よくぞ聞いてくれたね。\x01",
            "それがあるんだよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)

    #C0225
    ChrTalk(
        0xB,
        (
            "#5P実は、追加プログラムの方は\x01",
            "事前に受け取っていた資料を元に\x01",
            "こちらで再現する事ができたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xB,
        (
            "#5P後は魔導杖の\x01",
            "アタッチパーツだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        "#11Pそこで俺の出番ってわけだ。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x8,
        (
            "#11P修理や改造ならお手のモンだぜ。\x01",
            "資料は受け取ったから、\x01",
            "材料さえありゃあすぐに作ってやるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#12P#0000Fなるほど……素材さえあれば\x01",
            "何とかなるってことですね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4795():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4795)

    def lambda_47A2():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_47A2)

    def lambda_47AF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47AF)

    def lambda_47BC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_47BC)
    Sleep(500)

    #C0230
    ChrTalk(
        0x101,
        (
            "#11P#0000Fみんな、ここは一つ\x01",
            "ティオのために協力しようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x102,
        "#12P#0100Fええ、私もそれがいいと思う。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x104,
        "#12P#0300F異議なしだぜ。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        (
            "#6P#0205Fいいんですか……？\x01",
            "捜査の方に\x01",
            "遅れが出るかもしれませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        (
            "#12P#0309Fはは、材料を探してくるだけだろ？\x01",
            "大したことねえって。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x102,
        (
            "#12P#0100Fそうそう、ロイドも言っていたけど\x01",
            "戦力がアップすれば\x01",
            "探索も楽になるはずだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        (
            "#11P#0000Fああ、やらない手はないと思うよ。\x02\x03",

            "……ティオ、どうかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x103,
        (
            "#6P#0203F判りました、では\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x104,
        "#12P#0300Fよし、決まりだな！\x02",
    )

    CloseMessageWindow()

    def lambda_49E1():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49E1)

    def lambda_49EE():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_49EE)

    def lambda_49FB():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_49FB)

    def lambda_4A08():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4A08)
    Sleep(300)

    #C0239
    ChrTalk(
        0x103,
        (
            "#6P#0200F親方さん、必要な材料は\x01",
            "具体的にはどのようなものが？\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        (
            "#11Pああ、『Ｔマテリアル』っつー\x01",
            "特別な素材なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        (
            "#11Pこいつはクロスベルじゃ\x01",
            "手に入りにくいかもしれねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそうですか……\x01",
            "まあ何とか探してみます。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xB,
        (
            "#5Pああ、必要なのは１個だけだし\x01",
            "どうにかお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xB,
        (
            "#5P材料が揃ったら\x01",
            "ギヨームに声を掛けてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xB,
        (
            "#5P僕たちは改造の準備を\x01",
            "進めておくからね！\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x103,
        "#6P#0200Fよろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x102,
        "#12P#0100Fそれじゃあ行きましょうか。\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x104,
        "#12P#0300Fおう、張り切っていこうぜ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0249
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【魔導杖の新機能開発】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(115090, 1500, 58830, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -200, 0, 3820, 0)
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    SetChrPos(0xB, 5620, 0, 5330, 270)
    ClearChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D0E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_4D0E")

    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_29(0x31, 0x1, 0x0)
    SetScenarioFlags(0x4E, 4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_34AE end

    def Function_12_4D2F(): pass

    label("Function_12_4D2F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    TalkEnd(0x8)
    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(13800, 2300, 7800, 0)
    MoveCamera(61, 26, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(24880, 0)
    SetChrPos(0x101, 12800, 1000, 7200, 90)
    SetChrPos(0x102, 12800, 1000, 8100, 90)
    SetChrPos(0x103, 12800, 1000, 9000, 90)
    SetChrPos(0x104, 12800, 1000, 6300, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DE4")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, 12110, 1000, 9870, 90)

    label("loc_4DE4")

    SetChrPos(0x8, 15200, 1000, 8900, 225)
    SetChrPos(0xB, 15240, 1000, 7610, 270)
    OP_65(0x0, 0x1)
    SetMapObjFlags(0x0, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    #C0250
    ChrTalk(
        0x8,
        (
            "#5P材料は確認したぜ。\x01",
            "こっちは問題なしだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53D8")

    #C0251
    ChrTalk(
        0x10A,
        (
            "#6P#0604F武器の改造ですか……\x01",
            "これは珍しい物が見れそうですな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_4EB8():

        label("loc_4EB8")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_4EB8")

    QueueWorkItem2(0x104, 1, lambda_4EB8)
    Sleep(50)

    def lambda_4ECD():

        label("loc_4ECD")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_4ECD")

    QueueWorkItem2(0x101, 1, lambda_4ECD)

    def lambda_4EDF():

        label("loc_4EDF")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_4EDF")

    QueueWorkItem2(0x102, 1, lambda_4EDF)

    def lambda_4EF1():

        label("loc_4EF1")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_4EF1")

    QueueWorkItem2(0x103, 1, lambda_4EF1)

    def lambda_4F03():

        label("loc_4F03")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_4F03")

    QueueWorkItem2(0xB, 1, lambda_4F03)

    def lambda_4F15():

        label("loc_4F15")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_4F15")

    QueueWorkItem2(0x8, 1, lambda_4F15)
    Sleep(400)

    #C0252
    ChrTalk(
        0x104,
        (
            "#12P#0300Fお、ダドリーのオッサンも\x01",
            "やっぱ興味あんのかよ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x104, 500)
    Sleep(300)

    #C0253
    ChrTalk(
        0x10A,
        (
            "#6P#0601F……馬鹿者、皮肉だ！\x01",
            "この忙しい時に何を悠長な事を、\x01",
            "と言っている！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0254
    ChrTalk(
        0x102,
        (
            "#12P#0103Fす、すみません。\x01",
            "そうですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x103,
        (
            "#6P#0200F気付かなくて\x01",
            "申し訳ないです。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x5A, 0x1F4)
    Sleep(500)

    #C0256
    ChrTalk(
        0x10A,
        (
            "#6P#0603Fフン……\x01",
            "だが、お前達にはお前達の\x01",
            "事情があることは理解している。\x02\x03",

            "#0601F……私は席を外してる。\x01",
            "なるべく早く片付けて\x01",
            "捜査に戻れよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x101,
        "#12P#0005Fは、はい、分かりました。\x02",
    )

    CloseMessageWindow()
    OP_95(0x10A, 7200, 0, 9870, 2000, 0x0)
    Sleep(500)

    #C0258
    ChrTalk(
        0xB,
        "#11Pあれが捜査一課の人かぁ……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0x8, 0x1)

    def lambda_519A():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_519A)

    def lambda_51A7():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_51A7)

    def lambda_51B4():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51B4)

    def lambda_51C1():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_51C1)
    OP_93(0x8, 0xE1, 0x190)
    Sleep(400)

    #C0259
    ChrTalk(
        0xB,
        (
            "#11Pティオ君、やっぱり止めておくかい？\x01",
            "今は忙しいみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x103,
        (
            "#6P#0203Fいえ、気にしないで下さい。\x01",
            "ダドリーさんは\x01",
            "いつもあんな感じなので。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x102,
        (
            "#6P#0100F了解はしてくれたみたいですし。\x01",
            "今は早く改造してしまった方が\x01",
            "いいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        (
            "#5Pみてえだな。\x01",
            "ちゃちゃっと始めちまうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xB,
        (
            "#11Pよし、ここは一つ全速力で\x01",
            "仕上げさせてもらおうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    #C0264
    ChrTalk(
        0xB,
        (
            "#11Pそう考えると\x01",
            "俄然やる気が出てきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xB,
        (
            "#11Pうふふ、楽しみだね～。\x01",
            "新しい魔導杖を颯爽と構える\x01",
            "ティオ君が目に浮かぶようだな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_546F")

    label("loc_53D8")


    #C0266
    ChrTalk(
        0xB,
        "#11Pよし、準備は万全だね。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    #C0267
    ChrTalk(
        0xB,
        (
            "#11Pうふふ、楽しみだね～。\x01",
            "新しい魔導杖を颯爽と構える\x01",
            "ティオ君が目に浮かぶようだよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_546F")


    #C0268
    ChrTalk(
        0x103,
        (
            "#6P#0211F……主任。\x02\x03",

            "魔導杖がバグって\x01",
            "使い物にならなくなったら\x01",
            "恨みますよ？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    #C0269
    ChrTalk(
        0xB,
        (
            "#11Pそ、そんな……\x01",
            "ティオ君に一生嫌われちゃう……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xB,
        (
            "#11Pうわーん……！\x01",
            "僕は、僕は何て酷い事を……！\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        (
            "#12P#0006F主任さん、まだ何も\x01",
            "起きてませんよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 500)
    Sleep(300)

    #C0272
    ChrTalk(
        0x8,
        "#5Pロバーツよう、正気に戻れ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0273
    ChrTalk(
        0xB,
        "#11Pハッ……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x190)
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(300)

    #C0274
    ChrTalk(
        0xB,
        (
            "#11Pす、すまない。\x01",
            "早速始めるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xB,
        (
            "#11P支援課のみんなは\x01",
            "少しの間待っていてくれるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x102,
        (
            "#6P#0100Fええ、それでは\x01",
            "見学させていただきますね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(800)
    SetChrName("")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイド達はそのまま\x01",
            "３０分ほどの時間を過ごした。\x02",
        )
    )

    CloseMessageWindow()

    #A0278
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "詳しくは判らないが、\x01",
            "魔導杖の改造は\x01",
            "手際よく進められているようだった。\x02",
        )
    )

    CloseMessageWindow()

    #A0279
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そして──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x103, 250, 0, 6400, 255)
    SetChrPos(0x8, -820, 0, 8210, 166)
    SetChrPos(0xB, 1100, 0, 8510, 211)
    SetChrPos(0x101, -2090, 0, 2600, 31)
    SetChrPos(0x102, -880, 0, 2190, 346)
    SetChrPos(0x104, -2730, 0, 3880, 31)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57C4")
    SetChrPos(0x10A, 230, 0, -1850, 38)
    SetChrFlags(0x10A, 0x80)

    label("loc_57C4")

    OP_68(-520, 1600, 5910, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16770, 0)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00257.itc", 0x1F)
    LoadChrToIndex("chr/ch0025A.itc", 0x20)
    LoadEffect(0x0, "battle\\cr002403.eff")
    LoadEffect(0x1, "battle\\cr002401.eff")
    SetChrChipByIndex(0x103, 0x1E)
    BeginChrThread(0x103, 0, 0, 13)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    EndChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    OP_A0(0x103, 1500, 0x0, 0x2)
    Sleep(300)
    OP_A0(0x103, 1500, 0x2, 0x3)
    Sound(279, 0, 100, 0)
    SetChrSubChip(0x103, 0x4)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x103, 0xC0, 200, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(363, 0, 100, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0x103, 0xC0, 200, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(274, 0, 100, 0)
    Sleep(100)
    Fade(300)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    Sleep(2500)
    PlayEffect(0x1, 0xFF, 0x103, 0xC0, 200, 550, 850, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sound(280, 0, 90, 0)
    Sound(323, 0, 90, 0)
    Sleep(4500)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x103)
    Sleep(1000)
    Fade(300)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 0, 0, 13)
    OP_0D()
    Sleep(1000)

    #C0280
    ChrTalk(
        0x8,
        (
            "#5Pどうだい、具合の方は。\x01",
            "調整はこんなトコだと思うんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        (
            "#12P#0203Fそうですね……\x02\x03",

            "#0200F基本プログラムが書き換わったので\x01",
            "やや違和感がありますが、\x01",
            "悪くない感じです。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xB,
        (
            "#11Pきっと重心制御だね。\x01",
            "ティオ君ならすぐに慣れると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xB,
        (
            "#11P他の魔導杖に持ち替えるときは\x01",
            "エイオンシステムを使って\x01",
            "プログラムをコピーして使ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xB,
        (
            "#11P脱着式のアタッチパーツも\x01",
            "付けるのを忘れないようにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x103,
        "#12P#0200F了解です。\x02",
    )

    CloseMessageWindow()
    OP_68(-630, 1000, 5470, 2200)
    MoveCamera(67, 26, 0, 2200)
    SetCameraDistance(20230, 2200)
    OP_6F(0x79)

    #C0286
    ChrTalk(
        0x104,
        (
            "#6P#0305Fおいロイド……\x01",
            "なんか上手く行ったみたいだぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#12P#0005Fはぁ……魔導杖があんな風に\x01",
            "パカッと開くとは知らなかったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x102,
        (
            "#12P#0100F見た目以上に\x01",
            "色んな機能が入ってるのねぇ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0289
    ChrTalk(
        0x102,
        (
            "#12P#0105F……ってそうだ。\x01",
            "ティオちゃん、どんな具合なの？\x02\x03",

            "#0100F新しいクラフトというのは\x01",
            "上手く行ったのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Fade(300)
    EndChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    OP_0D()
    Sleep(300)

    def lambda_5CB0():
        OP_95(0xFE, -990, 0, 4810, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5CB0)
    Sleep(300)

    def lambda_5CCD():
        OP_95(0xFE, -1390, 0, 6630, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5CCD)

    def lambda_5CE7():
        OP_95(0xFE, 250, 0, 6400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5CE7)
    Sleep(2000)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0290
    ChrTalk(
        0x103,
        (
            "#11P#0200Fええ、改造は一通り終了しました。\x01",
            "性能も期待通りの値を\x01",
            "発揮しているようです。\x02\x03",

            "#0203F絶対零度の反エネルギー弾を打ち出す\x01",
            "『アブソリュート・ゼロ』──\x02\x03",

            "#0200F乱発は出来ませんが\x01",
            "重要な戦闘では\x01",
            "役に立ってくれそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        "#12P#0000Fそうか……それは心強いな。\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x104,
        (
            "#6P#0300Fはは、聞くからに凄そうな技だしな。\x01",
            "実戦が楽しみだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        (
            "#12P#0100Fそうね、今回はこちらが\x01",
            "お世話になってしまったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x103,
        "#11P#0200Fですね。\x02",
    )

    CloseMessageWindow()

    def lambda_5EB9():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5EB9)

    def lambda_5EC6():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EC6)
    Sleep(300)

    #C0295
    ChrTalk(
        0x103,
        (
            "#11P#0200F主任、親方さん、\x01",
            "どうもありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        "#12P#0000Fお世話になりました。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x8,
        (
            "#5Pへへっ、大した事はしてねえぜ。\x01",
            "気にしねえでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xB,
        (
            "#11Pああ、お礼なんていいんだよ。\x01",
            "こちらから言い出したことなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xB,
        (
            "#11Pそれに……無事に\x01",
            "改造ができて本当に良かったよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xB,
        (
            "#11P初めは断られるかと覚悟してたけど……\x01",
            "うんうん、やっぱりギヨームの名前で\x01",
            "要請を出したのが良かったのかな～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(14)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x103, 0xB, 500)
    TurnDirection(0x101, 0xB, 500)
    Sleep(200)

    #C0301
    ChrTalk(
        0x103,
        "#6P#0211F……じとー…………\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0302
    ChrTalk(
        0xB,
        (
            "#11Pいや、何でもないんだ。\x01",
            "何でもないよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x1F4)
    Sleep(200)

    #C0303
    ChrTalk(
        0xB,
        (
            "#11Pおおっとぉ、もうこんな時間だ……\x01",
            "僕はこれで失礼しないとね！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xE1, 0x1F4)
    Sleep(200)

    #C0304
    ChrTalk(
        0xB,
        (
            "#11Pティオ君、魔導杖は実戦で役立ててね？\x01",
            "じゃ、じゃあね～！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_61E8():

        label("loc_61E8")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_61E8")

    QueueWorkItem2(0x101, 1, lambda_61E8)

    def lambda_61FA():

        label("loc_61FA")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_61FA")

    QueueWorkItem2(0x102, 1, lambda_61FA)

    def lambda_620C():

        label("loc_620C")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_620C")

    QueueWorkItem2(0x104, 1, lambda_620C)

    def lambda_621E():

        label("loc_621E")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_621E")

    QueueWorkItem2(0x103, 1, lambda_621E)

    def lambda_6230():

        label("loc_6230")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_6230")

    QueueWorkItem2(0x8, 1, lambda_6230)

    def lambda_6242():
        OP_95(0xFE, 1200, 0, 1500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6242)
    WaitChrThread(0xB, 1)

    def lambda_6260():
        OP_95(0xFE, 0, 0, 1500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6260)
    WaitChrThread(0xB, 1)

    def lambda_627E():
        OP_95(0xFE, 0, 0, -2000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_627E)
    Sound(105, 0, 100, 0)

    def lambda_629E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_629E)
    WaitChrThread(0xB, 1)
    SetChrFlags(0xB, 0x80)
    Sleep(1100)

    #C0305
    ChrTalk(
        0x103,
        (
            "#6P#0206Fふう……\x01",
            "悪い人間ではないのですが。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x1)

    #C0306
    ChrTalk(
        0x101,
        (
            "#12P#0000Fまあ、ティオの事を\x01",
            "真剣に心配してくれてるのは\x01",
            "判るんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x8,
        (
            "#5Pあいつの過保護癖も\x01",
            "治んねえなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67B8")
    ClearChrFlags(0x10A, 0x80)

    #N0308
    NpcTalk(
        0x10A,
        "男の声",
        "#3P終わったようですな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_68(-380, 1000, 4920, 3000)
    MoveCamera(14, 20, 0, 3000)

    def lambda_642D():

        label("loc_642D")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_642D")

    QueueWorkItem2(0x101, 1, lambda_642D)

    def lambda_643F():

        label("loc_643F")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_643F")

    QueueWorkItem2(0x102, 1, lambda_643F)

    def lambda_6451():

        label("loc_6451")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_6451")

    QueueWorkItem2(0x104, 1, lambda_6451)

    def lambda_6463():

        label("loc_6463")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_6463")

    QueueWorkItem2(0x103, 1, lambda_6463)

    def lambda_6475():

        label("loc_6475")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_6475")

    QueueWorkItem2(0x8, 1, lambda_6475)
    OP_95(0x10A, 730, 0, 2370, 2000, 0x0)
    OP_93(0x10A, 0x13B, 0x1F4)
    Sleep(200)
    OP_6F(0x79)

    #C0309
    ChrTalk(
        0x10A,
        (
            "#12P#0600Fお前たち、魔導杖の\x01",
            "改造とやらは成功したのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x103,
        "#11P#0200Fええ、もちろんです。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#6P#0000Fお時間を取ってしまって\x01",
            "申し訳ありませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x10A,
        (
            "#12P#0603Fフン、全くだ。\x01",
            "この緊急を要するタイミングで\x01",
            "武器の手入れとは……\x02\x03",

            "#0601Fまあいい、終わったのなら\x01",
            "探索に戻るぞ。\x02\x03",

            "あちらをこれ以上\x01",
            "放置しておくわけにはいかん。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#6P#0000F分かりました、\x01",
            "すぐに行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x1)

    def lambda_663A():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_663A)

    def lambda_6647():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6647)

    def lambda_6654():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6654)

    def lambda_6661():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6661)
    Sleep(400)

    #C0314
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれでは親方さん、\x01",
            "これにて失礼します。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        (
            "#12P#0100Fお世話になりました。\x01",
            "また何かあれば\x01",
            "よろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x8,
        (
            "#5Pおう、何だか知ねえが\x01",
            "しっかりやんなよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x8,
        (
            "#5Pダドリーさんだっけか？\x01",
            "あんたも気が向いたら\x01",
            "訪ねに来てくれや！\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x10A,
        (
            "#12P#0604Fフ……まあ\x01",
            "考えておきましょう。\x02\x03",

            "#0600Fそれではまたの機会に。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68E3")

    label("loc_67B8")


    #C0319
    ChrTalk(
        0x8,
        (
            "#5Pまあいいさ、これでしばらくは\x01",
            "大人しくなんだろうしな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_67FE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67FE)

    def lambda_680B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_680B)

    def lambda_6818():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6818)

    def lambda_6825():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6825)
    Sleep(300)

    #C0320
    ChrTalk(
        0x8,
        (
            "#5Pんじゃ、俺はそろそろ\x01",
            "仕事に戻るぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x8,
        (
            "#5Pその魔導杖、\x01",
            "活用してやってくれよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x103,
        "#12P#0200Fええ、もちろんです。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x102,
        (
            "#12P#0100Fまた何かあれば\x01",
            "よろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68E3")

    AddCraft(0x2, 0xAE)
    SubItemNumber(0x397, 1)
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【魔導杖の新機能開発】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 0, 4190, 180)
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    OP_4C(0x8, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69B1")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_69B1")

    OP_29(0x31, 0x4, 0x10)
    OP_29(0x31, 0x1, 0x1)
    SetScenarioFlags(0x0, 4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_4D2F end

    def Function_13_69C5(): pass

    label("Function_13_69C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69DC")
    OP_A0(0x103, 1200, 0x0, 0x4)
    Jump("Function_13_69C5")

    label("loc_69DC")

    Return()

    # Function_13_69C5 end

    SaveToFile()

Try(main)
