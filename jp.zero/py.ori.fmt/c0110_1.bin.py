from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0110_1.bin",                # FileName
        "c0110",                    # MapName
        "c0110",                    # Location
        0x0009,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1000, 0, 2000, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0110_1",                # 0
    ))

    DeclEvent(0x0000, 0, 17,  10.0,                  10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -5.0,                  -2.0999999046325684,   -0.0,                  1.0])

    ScpFunction((
        "Function_0_194",          # 00, 0
        "Function_1_3A4",          # 01, 1
        "Function_2_3A8",          # 02, 2
        "Function_3_981",          # 03, 3
        "Function_4_1CEB",         # 04, 4
        "Function_5_1FFA",         # 05, 5
        "Function_6_2183",         # 06, 6
        "Function_7_281A",         # 07, 7
        "Function_8_2DCF",         # 08, 8
        "Function_9_3136",         # 09, 9
        "Function_10_32CA",        # 0A, 10
        "Function_11_3500",        # 0B, 11
        "Function_12_37E7",        # 0C, 12
        "Function_13_3B68",        # 0D, 13
        "Function_14_4019",        # 0E, 14
        "Function_15_4994",        # 0F, 15
        "Function_16_49D1",        # 10, 16
        "Function_17_5084",        # 11, 17
        "Function_18_5291",        # 12, 18
        "Function_19_5330",        # 13, 19
        "Function_20_54A0",        # 14, 20
        "Function_21_5B37",        # 15, 21
        "Function_22_6052",        # 16, 22
        "Function_23_621F",        # 17, 23
        "Function_24_63EC",        # 18, 24
        "Function_25_65BB",        # 19, 25
        "Function_26_6795",        # 1A, 26
        "Function_27_6966",        # 1B, 27
        "Function_28_6B37",        # 1C, 28
        "Function_29_6D04",        # 1D, 29
        "Function_30_6EDC",        # 1E, 30
        "Function_31_6F33",        # 1F, 31
        "Function_32_6FDE",        # 20, 32
        "Function_33_7120",        # 21, 33
        "Function_34_71C3",        # 22, 34
        "Function_35_726E",        # 23, 35
        "Function_36_7315",        # 24, 36
        "Function_37_73BE",        # 25, 37
        "Function_38_746D",        # 26, 38
        "Function_39_751A",        # 27, 39
    ))


    def Function_0_194(): pass

    label("Function_0_194")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_25B")
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伝言板にメッセージがある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『キツネに呼び出されたんで行ってくる。\x01",
            "  適当にあしらうから夕方には戻る。\x01",
            "                        セルゲイ』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3A0")

    label("loc_25B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2FA")
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伝言板にメッセージがある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『本部に行ってくる。\x01",
            "  夕方には戻るつもりだ。\x01",
            "               セルゲイ』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3A0")

    label("loc_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_3A0")
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伝言板にメッセージがある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『ヤボ用で出かけてくる。\x01",
            "  例の件は好きにやってみろ。\x01",
            "                   セルゲイ』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3A0")

    TalkEnd(0xFF)
    Return()

    # Function_0_194 end

    def Function_1_3A4(): pass

    label("Function_1_3A4")

    Call(1, 3)
    Return()

    # Function_1_3A4 end

    def Function_2_3A8(): pass

    label("Function_2_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C3")
    Call(0, 48)
    Jump("loc_980")

    label("loc_3C3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3D4")
    Jump("loc_97D")

    label("loc_3D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3E2")
    Jump("loc_97D")

    label("loc_3E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3F0")
    Jump("loc_97D")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DA")
    OP_93(0xFE, 0x5A, 0x0)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セルゲイは台所で\x01",
            "朝食の後片付けをしている。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0008
    ChrTalk(
        0x8,
        (
            "#1003Fマフィア絡みとなると\x01",
            "捜査一課が動いてるだろうが……\x02\x03",

            "#1000F確かに無視できない事件だな。\x02\x03",

            "後で俺も本部に\x01",
            "顔を出してみるつもりだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_52B")

    label("loc_4DA")


    #C0009
    ChrTalk(
        0x8,
        (
            "#1000Fいいからとっとと行って来い。\x02\x03",

            "後で俺も本部に\x01",
            "顔を出してみるつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52B")

    Jump("loc_97D")

    label("loc_530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_53E")
    Jump("loc_97D")

    label("loc_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_54C")
    Jump("loc_97D")

    label("loc_54C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_55A")
    Jump("loc_97D")

    label("loc_55A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_568")
    Jump("loc_97D")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_576")
    Jump("loc_97D")

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_584")
    Jump("loc_97D")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_592")
    Jump("loc_97D")

    label("loc_592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82E")

    #C0010
    ChrTalk(
        0x8,
        "#1005Fなんだ、全員戻ってたか。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#0000F課長……\x01",
            "自室にいるなんて珍しいですね。\x02\x03",

            "何か調べ物ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "#1002F……いや？\x01",
            "タバコが切れちまってな。\x02\x03",

            "へそくりに隠しておいた\x01",
            "ミラ札を捜しているところだ。\x02",
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

    #C0013
    ChrTalk(
        0x103,
        (
            "#0206Fまあ、そんな事だろうと\x01",
            "思いましたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#1003Fそうそう、ツァイトのやつは\x01",
            "裏口の辺りにいやがったぞ。\x02\x03",

            "#1000Fお前ら、ちゃんと\x01",
            "責任持って面倒みとけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#0302Fういーっす。\x02\x03",

            "#0309Fま、ティオすけとお嬢が\x01",
            "毎日撫でてやってるから十分だろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#0113F……コホン、その、\x01",
            "スキンシップは重要だものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        "#0202Fもちろんです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8C7")

    label("loc_82E")


    #C0018
    ChrTalk(
        0x8,
        (
            "#1003Fツァイトのやつは\x01",
            "裏口の辺りにいやがったぞ。\x02\x03",

            "#1000Fお前ら、ちゃんと\x01",
            "責任持って面倒みとけよ。\x02\x03",

            "俺もエサくらいはやってやるが\x01",
            "後は知らんからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C7")

    Jump("loc_97D")

    label("loc_8CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8DA")
    Jump("loc_97D")

    label("loc_8DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8E8")
    Jump("loc_97D")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8F6")
    Jump("loc_97D")

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_904")
    Jump("loc_97D")

    label("loc_904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_912")
    Jump("loc_97D")

    label("loc_912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_END)), "loc_97D")

    #C0019
    ChrTalk(
        0x8,
        (
            "#1000Fどうした、さっさと\x01",
            "支援要請を確認しろ。\x02\x03",

            "そこの端末を調べれば\x01",
            "情報が引き出せるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97D")

    TalkEnd(0x8)

    label("loc_980")

    Return()

    # Function_2_3A8 end

    def Function_3_981(): pass

    label("Function_3_981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_99C")
    Call(0, 48)
    Jump("loc_1CEA")

    label("loc_99C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A30")
    Jump("loc_A7A")

    label("loc_A30")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A50")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A7A")

    label("loc_A50")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A70")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A7A")

    label("loc_A70")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A7A")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_EAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 2)), scpexpr(EXPR_END)), "loc_B46")

    #C0020
    ChrTalk(
        0x9,
        (
            "#1005Fなんだ、また戻ってきたのか？\x02\x03",

            "#1003Fソーニャの所には\x01",
            "俺の方から連絡しておく。\x02\x03",

            "#1001Fとにかくお前らは\x01",
            "大急ぎでウルスラ病院へ向かえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA9")

    label("loc_B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_D10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAB")

    #C0021
    ChrTalk(
        0x9,
        (
            "#1005F……？\x01",
            "どうした、病院に行かないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0003Fいえ、それが……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダドリーからの情報と\x01",
            "病院と連絡が付かなくなっている事を説明した。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        (
            "#1010F………………………………\x02\x03",

            "チッ……キナ臭すぎるな。\x02\x03",

            "#1003F俺の方からも\x01",
            "各方面に連絡しておく。\x02\x03",

            "#1001Fとにかくお前らは\x01",
            "大急ぎでウルスラ病院へ向かえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#0013Fはい！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 5)
    Jump("loc_D0B")

    label("loc_CAB")


    #C0026
    ChrTalk(
        0x9,
        (
            "#1001F俺の方からも\x01",
            "各方面に連絡しておく。\x02\x03",

            "とにかくお前らは\x01",
            "大急ぎでウルスラ病院へ向かえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0B")

    Jump("loc_EA9")

    label("loc_D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E02")

    #C0027
    ChrTalk(
        0x9,
        (
            "#1000Fギルドからの連絡は\x01",
            "俺に任せておけ。\x02\x03",

            "ウルスラのナントカ先生んとこに\x01",
            "急いで行ってくるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0100Fシズクちゃんは\x01",
            "キーアちゃんと一緒みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "#1002Fああ、ツァイトも一緒だ。\x01",
            "こっちの事は心配すんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_EA9")

    label("loc_E02")


    #C0030
    ChrTalk(
        0x9,
        (
            "#1003Fこっちの事は心配すんな。\x01",
            "俺が万事引き受けておく。\x02\x03",

            "#1000Fお前らはウルスラ病院に\x01",
            "急いで行ってくるといい。\x02\x03",

            "薬の成分、今日中には\x01",
            "確認しておいた方がいいだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA9")

    Jump("loc_1CE3")

    label("loc_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_10A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_F4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED2")
    Call(1, 13)
    Jump("loc_F46")

    label("loc_ED2")


    #C0031
    ChrTalk(
        0x9,
        (
            "#1003F上層部の方は\x01",
            "こっちで誤魔化しておいてやる。\x02\x03",

            "#1001F……捜索に入るなら急げ。\x01",
            "そう長く持つもんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F46")

    Jump("loc_10A4")

    label("loc_F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1036")

    #C0032
    ChrTalk(
        0x9,
        (
            "#1003F重要参考人が消えたか……\x02\x03",

            "#1001F思ってたより\x01",
            "事態の進行が早いかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#0003Fええ……まずは\x01",
            "状況を掴まない事には……\x02\x03",

            "#0000Fすみません、課長は\x01",
            "こっちの方を頼みます。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        "#1000Fああ、任せておけ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_10A4")

    label("loc_1036")


    #C0035
    ChrTalk(
        0x9,
        (
            "#1000Fもしこの件に\x01",
            "『教団』が絡んでるなら……\x01",
            "必ず捜査の延長線上にいるはずだ。\x02\x03",

            "お前たち、油断すんなよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A4")

    Jump("loc_1CE3")

    label("loc_10A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1181")

    #C0036
    ChrTalk(
        0x9,
        (
            "#1003Fま、その薬物はウルスラ大の\x01",
            "先生に見てもらうとして……\x02\x03",

            "#1002F一課の方は放っておけばいい。\x01",
            "あれで優秀な連中だ、\x01",
            "必ず何か成果を上げるはずだ。\x02\x03",

            "お前たちはお前たちで\x01",
            "いつも通り自由に動いてみろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE3")

    label("loc_1181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_1298")
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x9,
        (
            "#1005Fなんだ、遅かったな。\x02\x03",

            "#1000F《黒月》の方の聞き込みは\x01",
            "そんなに時間がかかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#0003Fいえ……実はそれとは別に\x01",
            "気になる事件に出くわしまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#0101F《黒月》襲撃事件と合わせて\x01",
            "一通り報告させていただきます。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 47)
    Return()

    label("loc_1298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_12A6")
    Jump("loc_1CE3")

    label("loc_12A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_12B4")
    Jump("loc_1CE3")

    label("loc_12B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_12C2")
    Jump("loc_1CE3")

    label("loc_12C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1371")

    #C0040
    ChrTalk(
        0x9,
        (
            "#1004Fキーアについては\x01",
            "ロイド、しばらくお前に任せる。\x02\x03",

            "#1000Fただし何か分かれば\x01",
            "すぐに報告しろ。\x01",
            "警察全体にも関わる事だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#0000Fはい、了解です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CE3")

    label("loc_1371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_137F")
    Jump("loc_1CE3")

    label("loc_137F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1533")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B6")

    #C0042
    ChrTalk(
        0x9,
        (
            "#1000Fフン、どうやら\x01",
            "腹を括ったみたいだな。\x02\x03",

            "#1004F──ま、好きにやれ。\x01",
            "上には適当に\x01",
            "誤魔化しておいてやる。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#0000Fすみません、課長。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#0100F……どうか\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "#1002Fクク、気にするな。\x01",
            "こういう時ための\x01",
            "『特務支援課』だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0105Fは、はあ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_152E")

    label("loc_14B6")


    #C0047
    ChrTalk(
        0x9,
        (
            "#1004Fさて、紅茶でも淹れながら\x01",
            "上への誤魔化し方を考えるか。\x02\x03",

            "#1002Fクク……心配すんな。\x01",
            "こういうのは俺の十八番だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152E")

    Jump("loc_1CE3")

    label("loc_1533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1541")
    Jump("loc_1CE3")

    label("loc_1541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_154F")
    Jump("loc_1CE3")

    label("loc_154F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_155D")
    Jump("loc_1CE3")

    label("loc_155D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1701")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1693")

    #C0048
    ChrTalk(
        0x9,
        (
            "#1003Fエステル・ブライトと\x01",
            "ヨシュア・ブライトか……\x02\x03",

            "#1002F──お前らが昨日会った２人は\x01",
            "どうやら大した経歴らしいぜ。\x02\x03",

            "今回の件も、長引かせたら\x01",
            "間違いなくギルドが出張るだろう。\x02\x03",

            "#1004Fそれが嫌なら\x01",
            "きりきり働くしかねえよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        (
            "#0111F（……励ましている\x01",
            "  つもりなのかしら。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_16FC")

    label("loc_1693")


    #C0050
    ChrTalk(
        0x9,
        (
            "#1004F今回の件も、長引かせたら\x01",
            "間違いなくギルドが出張るだろう。\x02\x03",

            "#1002Fま、せいぜい気張っておけよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FC")

    Jump("loc_1CE3")

    label("loc_1701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_170F")
    Jump("loc_1CE3")

    label("loc_170F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1975")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FC")
    SetChrSubChip(0x9, 0x0)

    #C0051
    ChrTalk(
        0x9,
        "#1003Fふう、朝の煙草は美味ぇな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17F7")
    Jump("loc_1841")

    label("loc_17F7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1817")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1841")

    label("loc_1817")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1837")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1841")

    label("loc_1837")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1841")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    #C0052
    ChrTalk(
        0x9,
        (
            "#1005Fおー、話は聞いてきたか？\x02\x03",

            "#1004Fなら適当に頑張ってこい。\x01",
            "副局長のやつに\x01",
            "小言を言われねえ程度にな。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#0006Fはいはい、了解です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1970")

    label("loc_18FC")


    #C0054
    ChrTalk(
        0x9,
        (
            "#1002F詳しい話は知らんが\x01",
            "警備隊絡みだそうじゃねえか。\x02\x03",

            "ある程度成果が出せなきゃ\x01",
            "副局長に小言を言われちまうぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1970")

    Jump("loc_1CE3")

    label("loc_1975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1AC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7E")

    #C0055
    ChrTalk(
        0x9,
        (
            "#1000F西通りにある\x01",
            "法律事務所に行ってこい。\x02\x03",

            "そこの弁護士先生に\x01",
            "支援課#6Rウ　チ#のことは伝えてあるから\x01",
            "話ぐらいは聞いてくれるだろう。\x02\x03",

            "#1003F有意義な情報が聞けるよう\x01",
            "お前たちで頑張れ──以上だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        "#0306Fやる気ないッスね、課長～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1ABF")

    label("loc_1A7E")


    #C0057
    ChrTalk(
        0x9,
        (
            "#1003F有意義な情報が聞けるよう\x01",
            "お前たちで頑張れ──以上だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ABF")

    Jump("loc_1CE3")

    label("loc_1AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_END)), "loc_1BD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B92")

    #C0058
    ChrTalk(
        0x9,
        (
            "#1005Fなんだお前ら、\x01",
            "旧市街に行けと言ったろう。\x02\x03",

            "#1003Fウチは便利屋みてえなモンだからな。\x01",
            "支援要請の他に緊急の\x01",
            "捜査任務が入ることもあるんだ。\x02\x03",

            "#1000Fそっちを優先して当たれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1BD0")

    label("loc_1B92")


    #C0059
    ChrTalk(
        0x9,
        (
            "#1003Fとっとと旧市街に行け。\x02\x03",

            "#1000F内容は知らん、以上。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD0")

    Jump("loc_1CE3")

    label("loc_1BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1CE3")

    #C0060
    ChrTalk(
        0x9,
        (
            "#1003F細かい支援要請を片付けるのが\x01",
            "特務支援課のお仕事だ。\x02\x03",

            "#1000Fやるかやらんかは任せるが、\x01",
            "警察の受付だけは行っておけ。\x02\x03",

            "それと、エニグマの調整については\x01",
            "オーバルストアに依頼してるから\x01",
            "そっちの方を訪ねてみるんだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE3")

    #C0061
    ChrTalk(
        0x101,
        "#0000F了解しました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_1CE3")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)

    label("loc_1CEA")

    Return()

    # Function_3_981 end

    def Function_4_1CEB(): pass

    label("Function_4_1CEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_1CFF")
    Call(1, 5)
    Jump("loc_1FF6")

    label("loc_1CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1E7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2A")

    #C0062
    ChrTalk(
        0xA,
        "#1110Fあ、みんなー！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#0002Fはは、さっそく\x01",
            "仲良く遊んでるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        (
            "#1109Fえへへー。\x02\x03",

            "#1110Fロイドたちは\x01",
            "これからお仕事なのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        (
            "#0102Fええ、でも\x01",
            "すぐに戻ってくるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#0202F晩ゴハンはシズクさんも一緒に\x01",
            "にぎやかに食べましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        "#1109Fうんっ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1E78")

    label("loc_1E2A")

    OP_93(0xFE, 0xB4, 0x0)

    #C0068
    ChrTalk(
        0xA,
        (
            "#1100Fそれでねー、こうやってなでると\x01",
            "しっぽフリフリするんだよー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E78")

    Jump("loc_1FF6")

    label("loc_1E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_1EEE")

    #C0069
    ChrTalk(
        0xFE,
        (
            "#1104Fせっせのせー♪\x01",
            "お皿をきれーに並べないとー！\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        "#0000F（何だか熱中してるみたいだな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FF6")

    label("loc_1EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA1")
    OP_93(0xFE, 0x0, 0x0)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キーアは台所で\x01",
            "朝食の後片付けをしている。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0072
    ChrTalk(
        0xA,
        (
            "#1100Fロイドー、何か分かったら\x01",
            "キーアにも教えてねー？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#0002Fはは、了解だよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1FF6")

    label("loc_1FA1")


    #C0074
    ChrTalk(
        0xA,
        (
            "#1104Fおかたづけー、おかたづけー♪\x02\x03",

            "#1110F何か分かったら\x01",
            "キーアにも教えてねー？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF6")

    TalkEnd(0xFE)
    Return()

    # Function_4_1CEB end

    def Function_5_1FFA(): pass

    label("Function_5_1FFA")

    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xF, 0xE1, 0x0)
    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0075
    ChrTalk(
        0xF,
        (
            "#6005Fわっ、ホントだ。\x01",
            "フカフカの毛並み……\x02\x03",

            "#6000Fわたしシズクっていいます。\x01",
            "よろしくね、ツァイトさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xD,
        "#1200Fグルル、グルルルル……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "#1110Fえーとねぇ……\x02\x03",

            "#1109F『れーぎ正しいコは\x01",
            "  キライじゃない』だってー。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217A")

    #C0078
    ChrTalk(
        0x102,
        (
            "#0108F（キーアちゃんたちには\x01",
            "  何も伝えない方がいいわね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#0003F（ああ……\x01",
            "  ツァイトに任せて病院に急ごう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_217A")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_5_1FFA end

    def Function_6_2183(): pass

    label("Function_6_2183")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2217")
    Jump("loc_2261")

    label("loc_2217")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2237")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2261")

    label("loc_2237")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2257")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2261")

    label("loc_2257")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2261")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2294")
    Jump("loc_2812")

    label("loc_2294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_24DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249C")

    #C0080
    ChrTalk(
        0xB,
        (
            "#1105Fあれー？\x01",
            "ぶすっとしたオジサン？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2316")
    OP_63(0x10A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_2316")


    #C0081
    ChrTalk(
        0x10A,
        (
            "#0603Fだ、誰がオジサンだ。\x02\x03",

            "#0600F私の名はダドリーだ。\x01",
            "覚えておいてもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xB,
        (
            "#1109Fうんっ！\x01",
            "よろしくね、ダドリー！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23BC")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_23BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23E2")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_23E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2408")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2408")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_242E")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_242E")

    Sleep(1000)

    #C0083
    ChrTalk(
        0x10A,
        (
            "#0603F（……お前たち。\x01",
            "  年長者への礼儀はいずれ教えておけ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#0006F（りょ、了解です。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_24D5")

    label("loc_249C")


    #C0085
    ChrTalk(
        0xB,
        (
            "#1110Fロイドたちにダドリー！\x01",
            "お仕事がんばってねー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D5")

    Jump("loc_2812")

    label("loc_24DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2613")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E3")

    #C0086
    ChrTalk(
        0x103,
        (
            "#0202Fキーア……\x01",
            "ここにいたんですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#0302Fお、そいつも\x01",
            "図書館の本みたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xB,
        (
            "#1100Fうん、まだ１さつ残ってたから\x01",
            "読んじゃおうと思ってー。\x02\x03",

            "#1109Fみんな、お仕事がんばってねー！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#0000Fああ、なるべく\x01",
            "早く戻ってくるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_260E")

    label("loc_25E3")


    #C0090
    ChrTalk(
        0xB,
        (
            "#1110Fえへへ。\x01",
            "お仕事がんばってねー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260E")

    Jump("loc_2812")

    label("loc_2613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_2812")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D9")

    #C0091
    ChrTalk(
        0xB,
        (
            "#1105Fあれー、みんな。\x01",
            "また出かけるのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#0002Fああ、行って来るよ。\x01",
            "夜までには戻るからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#0102Fふふっ、何か\x01",
            "おみやげでも買ってくる？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xB,
        (
            "#1111Fんー、別にいいや。\x02\x03",

            "#1109Fロイドたちが元気に\x01",
            "帰ってきてくれるだけでいい！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(892, 0, 100, 0)
    Sleep(1000)

    #C0095
    ChrTalk(
        0x101,
        "#0012Fうっ……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        "#0109Fはぁぁ～……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x103,
        "#0204F笑顔が沁#2Rし#みます……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        (
            "#0302Fはは、殺伐とした雰囲気が\x01",
            "一気に消し飛んじまったな。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)

    #C0099
    ChrTalk(
        0xB,
        "#1100Fんー？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 6)
    Jump("loc_2812")

    label("loc_27D9")


    #C0100
    ChrTalk(
        0xB,
        (
            "#1110Fいってらっしゃ～い！\x01",
            "みんな、気をつけてねー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2812")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_2183 end

    def Function_7_281A(): pass

    label("Function_7_281A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_282E")
    Call(1, 5)
    Jump("loc_2DCB")

    label("loc_282E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2858")

    #C0101
    ChrTalk(
        0xFE,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCB")

    label("loc_2858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_293C")

    #C0102
    ChrTalk(
        0xFE,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28C1")
    OP_63(0x10A, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_28C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2937")

    #C0103
    ChrTalk(
        0x10A,
        (
            "#0606F（ふう、これが警察犬扱いか……）\x02\x03",

            "#0610F（セルゲイさん……\x01",
            "  さすがに無理がありすぎだろう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_2937")

    Jump("loc_2DCB")

    label("loc_293C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_29E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C4")

    #C0104
    ChrTalk(
        0xFE,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x103,
        (
            "#0202Fええ、こちらは\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xC,
        "#1203Fグルルル……ウォン！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_29E0")

    label("loc_29C4")


    #C0107
    ChrTalk(
        0xFE,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()

    label("loc_29E0")

    Jump("loc_2DCB")

    label("loc_29E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_2ADF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ABE")

    #C0108
    ChrTalk(
        0xFE,
        "#1203Fグルルルルル……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            "#0202F『自分がいるかぎり\x01",
            "  ここの守りは万全だ』と言ってます。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        "#0000Fはは……本当に助かるよ。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x104,
        (
            "#0304Fこりゃ、たまには\x01",
            "骨付き肉でも差し入れねぇとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2ADA")

    label("loc_2ABE")


    #C0112
    ChrTalk(
        0xFE,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()

    label("loc_2ADA")

    Jump("loc_2DCB")

    label("loc_2ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2BC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BA8")

    #C0113
    ChrTalk(
        0xFE,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#0000F（相変わらず偉そうだけど……\x01",
            "  支援課を守ってくれてるんだよな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#0202F（ええ、不審者が入ってきたら\x01",
            "  噛み付いてくれそうです。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2BC4")

    label("loc_2BA8")


    #C0116
    ChrTalk(
        0xFE,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()

    label("loc_2BC4")

    Jump("loc_2DCB")

    label("loc_2BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_2BD7")
    Jump("loc_2DCB")

    label("loc_2BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2BE5")
    Jump("loc_2DCB")

    label("loc_2BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CE8")

    #C0117
    ChrTalk(
        0x153,
        (
            "#1110Fツァイトー、それじゃ\x01",
            "お出掛けしてくるね。\x02\x03",

            "#1109Fおるすばんをおねがいー！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        "#1200Fグルルルルルル……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_2CAD")

    #C0119
    ChrTalk(
        0x103,
        (
            "#0202Fさっさと行ってくるがいい……\x01",
            "と言っています。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CAD")


    #C0120
    ChrTalk(
        0x101,
        (
            "#0012Fははは……\x01",
            "了解してくれてるみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2D06")

    label("loc_2CE8")


    #C0121
    ChrTalk(
        0xFE,
        "#1200Fグルルルルルル……\x02",
    )

    CloseMessageWindow()

    label("loc_2D06")

    Jump("loc_2DCB")

    label("loc_2D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2D6A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 5)), scpexpr(EXPR_END)), "loc_2D31")
    Call(1, 8)
    Jump("loc_2D34")

    label("loc_2D31")

    Call(1, 19)

    label("loc_2D34")

    Jump("loc_2D65")

    label("loc_2D39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_2D4E")
    Call(1, 17)
    Jump("loc_2D65")

    label("loc_2D4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2D62")
    Call(1, 16)
    Jump("loc_2D65")

    label("loc_2D62")

    Call(1, 8)

    label("loc_2D65")

    Jump("loc_2DCB")

    label("loc_2D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2DCB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2DB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 5)), scpexpr(EXPR_END)), "loc_2DAB")

    #C0122
    ChrTalk(
        0xFE,
        "#1200Fグルルルルルル……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DAE")

    label("loc_2DAB")

    Call(1, 19)

    label("loc_2DAE")

    Jump("loc_2DCB")

    label("loc_2DB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_2DC8")
    Call(1, 17)
    Jump("loc_2DCB")

    label("loc_2DC8")

    Call(1, 16)

    label("loc_2DCB")

    TalkEnd(0xFE)
    Return()

    # Function_7_281A end

    def Function_8_2DCF(): pass

    label("Function_8_2DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_305C")
    EventBegin(0x0)
    Fade(500)
    OP_68(3640, 1000, 5390, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(23630, 0)
    SetChrPos(0x101, 2060, 0, 5360, 90)
    SetChrPos(0x102, 2250, 0, 6760, 135)
    SetChrPos(0x103, 3500, 30, 4350, 0)
    SetChrPos(0x104, 4770, 30, 6030, 270)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    BeginChrThread(0xD, 1, 0, 0)
    OP_0D()

    #C0123
    ChrTalk(
        0xD,
        "#1200F#5Pグルル……？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        (
            "#0204F#12Pええ、少し出かけて来ます。\x02\x03",

            "#0202Fちょっと危ない事に\x01",
            "なるかもしれませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xD,
        (
            "#1203F#5Pグルルル……\x01",
            "……グルル……ウォン。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#0005F#6Pえっとティオ、\x01",
            "なんて言ってるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x103,
        (
            "#0202F#12Pええ、わたし達が\x01",
            "何かを調べている事は\x01",
            "判っていたようです。\x02\x03",

            "#0204F『適当に助けてやるから\x01",
            "  心配は無用だ』と言っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        (
            "#0309F#11Pはは……そいつは\x01",
            "頼りになるお言葉だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#0102F#5Pええ、今みたいな時には\x01",
            "心強い助っ人よね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 3500, 30, 4350, 0)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    SetScenarioFlags(0x8E, 4)
    EventEnd(0x5)
    Jump("loc_3135")

    label("loc_305C")


    #C0130
    ChrTalk(
        0xFE,
        "#1203Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        (
            "#0206F『さっさと行け……\x01",
            "  たまに行動力に欠けるのが\x01",
            "  お前たちの欠点だ……』\x02\x03",

            "#0200F……と言っています。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_3135")

    Return()

    # Function_8_2DCF end

    def Function_9_3136(): pass

    label("Function_9_3136")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_314A")
    Call(1, 5)
    Jump("loc_32C6")

    label("loc_314A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_32C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3293")
    TurnDirection(0xF, 0x0, 0)

    #C0132
    ChrTalk(
        0xF,
        "#6005Fあ、皆さん……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#0000F悪い、少し出かけてくるよ。\x02\x03",

            "キーアとツァイトのこと、\x01",
            "頼めるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xF,
        (
            "#6000Fはい、大丈夫です。\x02\x03",

            "わたしの方こそ\x01",
            "遊んでもらっちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        (
            "#0309Fま、たまの外出日なんだろ？\x01",
            "好きなだけ遊んでいきな。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xF,
        (
            "#6002Fふふ……はい。\x01",
            "そうさせてもらいますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xF, 0xE1, 0x0)
    Jump("loc_32C6")

    label("loc_3293")


    #C0137
    ChrTalk(
        0xF,
        (
            "#6001F本当になでてもいいの……？\x01",
            "ドキドキ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C6")

    TalkEnd(0xF)
    Return()

    # Function_9_3136 end

    def Function_10_32CA(): pass

    label("Function_10_32CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33E6")

    #C0138
    ChrTalk(
        0x10,
        (
            "#0100Fあらキーアちゃん。\x01",
            "初めてのお出掛けはどう？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x153,
        (
            "#1109Fうん、すっごくたのしいよ！\x01",
            "エリィも来ればよかったのにー。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x10,
        (
            "#0109Fふふっ、私は今日は\x01",
            "お留守番だから……\x02\x03",

            "#0102Fまた今度一緒に\x01",
            "お出掛けしましょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x153,
        (
            "#1110Fうん、わかった。\x01",
            "やくそくだよー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_34FC")

    label("loc_33E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_345D")

    #C0142
    ChrTalk(
        0x10,
        (
            "#0100Fロイド、ティオちゃん。\x01",
            "気をつけてね。\x02\x03",

            "間違っても\x01",
            "ルバーチェ商会なんかに\x01",
            "顔を出しちゃ駄目よ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34CB")

    label("loc_345D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_34CB")

    #C0143
    ChrTalk(
        0x10,
        (
            "#0100Fロイド、ランディ。\x01",
            "気をつけてね。\x02\x03",

            "間違っても\x01",
            "ルバーチェ商会なんかに\x01",
            "顔を出しちゃ駄目よ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34CB")


    #C0144
    ChrTalk(
        0x101,
        (
            "#0000Fそうだな……\x01",
            "十分に気をつけておくよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34FC")

    TalkEnd(0xFE)
    Return()

    # Function_10_32CA end

    def Function_11_3500(): pass

    label("Function_11_3500")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3594")
    Jump("loc_35DE")

    label("loc_3594")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_35B4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35DE")

    label("loc_35B4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35D4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35DE")

    label("loc_35D4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_35DE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3776")

    #C0145
    ChrTalk(
        0x11,
        "#0200Fキーア、出掛けたのでは……？\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x153,
        (
            "#1110Fうん、ティオに会いに\x01",
            "もどってきたよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x11,
        (
            "#0205F………………………………\x02\x03",

            "#0204Fキーアは可愛いです。\x01",
            "少しだけ撫でさせてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        "#0012F（はははは……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3722")

    #C0149
    ChrTalk(
        0x102,
        (
            "#0102F（ティオちゃん。\x01",
            "  気持ちは分かるわ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_376E")

    label("loc_3722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_376E")

    #C0150
    ChrTalk(
        0x104,
        (
            "#0309F（クールなティオすけが\x01",
            "  この可愛がりようだもんなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376E")

    SetScenarioFlags(0x1, 1)
    Jump("loc_37DF")

    label("loc_3776")


    #C0151
    ChrTalk(
        0x11,
        (
            "#0202Fキーア、車に気をつけてください。\x01",
            "２人から絶対に離れないように。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x153,
        "#1109Fうん、わかったー！\x02",
    )

    CloseMessageWindow()

    label("loc_37DF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_3500 end

    def Function_12_37E7(): pass

    label("Function_12_37E7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_387B")
    Jump("loc_38C5")

    label("loc_387B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_389B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38C5")

    label("loc_389B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38BB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38C5")

    label("loc_38BB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38C5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A87")

    #C0153
    ChrTalk(
        0x153,
        (
            "#1110Fランディ、それじゃあ\x01",
            "お出掛けしてくるねー！\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x12,
        "#0302Fおう、元気に行ってこいや！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_39E6")

    #C0155
    ChrTalk(
        0x12,
        (
            "#0300F……ロイド、お嬢。\x01",
            "キー坊のことは頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        "#0000Fああ、任せておいてくれ。\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        (
            "#0100Fなるべく早く\x01",
            "帰ってくるわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A7F")

    label("loc_39E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3A7F")

    #C0158
    ChrTalk(
        0x12,
        (
            "#0300F……ロイド、ティオすけ。\x01",
            "キー坊のことは頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#0000Fああ、任せておいてくれ。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x103,
        (
            "#0202Fなるべく早く\x01",
            "帰ってくるつもりです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A7F")

    SetScenarioFlags(0x1, 2)
    Jump("loc_3B60")

    label("loc_3A87")


    #C0161
    ChrTalk(
        0x12,
        (
            "#0303Fさてと、今のうちに\x01",
            "『ホットショット』でも読んどくか。\x02\x03",

            "#0309Fここ一週間はピリピリして\x01",
            "ロクに寛#3Rくつろ#げなかったからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#0006F（ランディ、子供の前で\x01",
            "  グラビア誌はちょっと……）\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x153,
        "#1105F？？？\x02",
    )

    CloseMessageWindow()

    label("loc_3B60")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_37E7 end

    def Function_13_3B68(): pass

    label("Function_13_3B68")

    EventBegin(0x0)
    Fade(500)
    OP_68(63930, 1330, 8550, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, 65489, 0, 8029, 315)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0164
    ChrTalk(
        0x9,
        (
            "#1005Fダドリー……？\x01",
            "何してるんだお前。\x02\x03",

            "#1001F……何かあったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x10A,
        (
            "#0601Fフン、どうもこうもありません。\x01",
            "何者かに出し抜かれましてね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダドリーは手短に\x01",
            "ルバーチェ商会の状況を伝えた。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        (
            "#1001F………………………………\x02\x03",

            "#1003Fマズイな、そりゃあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x10A,
        (
            "#0603Fともかくこのヒヨッ子どもと\x01",
            "ルバーチェ商会を捜索してみます。\x02\x03",

            "#0600Fセルゲイさんは上層部の方を……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        (
            "#0306Fま、おそらく上層部は\x01",
            "機能してねえ可能性が高いだろ。\x02\x03",

            "#0301F空港に爆破予告なんざ\x01",
            "タイミング良すぎだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#0000Fというわけで課長には\x01",
            "いつものように上層部を\x01",
            "押さえておいて欲しいんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "#1004F分かった、何とかしてやる。\x02\x03",

            "#1002Fだがこの状況で\x01",
            "突っついてみるのはヤブ蛇だ。\x01",
            "本当に誤魔化すくらいしかできんぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        (
            "#0102Fええ、時間を\x01",
            "稼いでいただければ十分です。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0xE1, 0x1F4)

    #C0173
    ChrTalk(
        0x10A,
        (
            "#0610Fお、お前たち……\x01",
            "私の指揮下に入ると\x01",
            "言っておきながら勝手を……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        "#0204Fまあ、そんなのは今更かと。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x9,
        (
            "#1004Fクク、悪いなダドリー。\x01",
            "これが支援課#6Rウ　チ#のやり方だ。\x02\x03",

            "#1000F……ともかく、急げよ。\x01",
            "この状況はかなりマズイぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 64000, 30, 7000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xCC, 4)
    EventEnd(0x5)
    Return()

    # Function_13_3B68 end

    def Function_14_4019(): pass

    label("Function_14_4019")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(254990, 1300, 67290, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x101, 251150, 0, 65900, 90)
    SetChrPos(0xEF, 249150, 0, 65900, 90)
    SetChrPos(0x153, 250150, 0, 65500, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetCameraDistance(25000, 3000)
    FadeToBright(500, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 1, 15)
    Sleep(500)
    BeginChrThread(0x153, 3, 1, 15)
    Sleep(500)
    BeginChrThread(0xEF, 3, 1, 15)
    Sleep(500)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x153, 3)

    #C0176
    ChrTalk(
        0x101,
        (
            "#0005Fあれ、なんだかキーアの部屋に\x01",
            "戻ってきちゃったな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_41AC")

    #C0177
    ChrTalk(
        0x153,
        (
            "#1109F#6Pえへへ～、ロイドたちに\x01",
            "他の服も見せてあげよーか。\x02\x03",

            "#1110Fエリィとティオが\x01",
            "いろいろ買ってきてくれたんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4221")

    label("loc_41AC")


    #C0178
    ChrTalk(
        0x153,
        (
            "#1109F#6Pえへへ～、ロイドに\x01",
            "他の服も見せてあげよーか。\x02\x03",

            "#1110Fエリィとティオが\x01",
            "いろいろ買ってきてくれたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4221")


    def lambda_4226():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4226)
    Sleep(50)

    def lambda_4236():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4236)
    Sleep(250)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4355")

    #C0179
    ChrTalk(
        0x102,
        (
            "#0105F#6Pあ、それはいいわね。\x02\x03",

            "#0109Fもうちょっとコーディネートを\x01",
            "楽しみたかったし……\x01",
            "……ほら、あのブラウスとか！\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0011Fい、いや、それはまた\x01",
            "次の機会にお願いするよ。\x01",
            "今日は用事があるわけだしさ。\x02\x03",

            "#0012F（放っておくと２時間くらい\x01",
            "  掛かりそうだ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4528")

    label("loc_4355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4477")

    #C0181
    ChrTalk(
        0x103,
        (
            "#0205F#6Pあ、それはいい考えです。\x02\x03",

            "#0204Fもう少しコーディネートを\x01",
            "楽しみたかった所ですし……\x01",
            "あのニット帽も捨てがたいと言うか……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#0011Fい、いや、それはまた\x01",
            "次の機会にお願いするよ。\x01",
            "今日は用事があるわけだしさ。\x02\x03",

            "#0012F（放っておくと２時間くらい\x01",
            "  掛かりそうだ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4528")

    label("loc_4477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4528")

    #C0183
    ChrTalk(
        0x104,
        (
            "#0309F#6Pおー、そりゃ楽しみだな。\x02\x03",

            "#0300Fでもま、また今度にしねえか？\x02\x03",

            "#0306Fお嬢とティオすけがやってきて\x01",
            "きゃいきゃい楽しく始めそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        "#0012Fはははは……\x02",
    )

    CloseMessageWindow()

    label("loc_4528")

    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)

    #C0185
    ChrTalk(
        0x101,
        (
            "#0000Fうん、でも何とかなったよな。\x02\x03",

            "空き部屋だったけど掃除もしたし、\x01",
            "家具も最低限は\x01",
            "エリィに揃えてもらったし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_45BF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_45BF)
    Sleep(200)

    def lambda_45CF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_45CF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4714")

    #C0186
    ChrTalk(
        0x102,
        (
            "#0102F#12Pああ……これは実家の古い物を\x01",
            "届けてもらっただけよ。\x02\x03",

            "#0106F両親の使っていた物だから\x01",
            "大人向けばかりで悪いけど。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4663():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4663)
    Sleep(250)

    #C0187
    ChrTalk(
        0x101,
        (
            "#0002Fいや、十分だよ。\x02\x03",

            "#0004F（キーアの身元が判ったら\x01",
            "  ご両親の所へ返すことに\x01",
            "  なるだろうけど……）\x02\x03",

            "（それまではできる限りの事は\x01",
            "  してあげたいよな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_497D")

    label("loc_4714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_484D")

    #C0188
    ChrTalk(
        0x103,
        (
            "#0202F#12Pエリィさんの実家にあった\x01",
            "お古だそうですね。\x02\x03",

            "#0204Fキーアには少し大きい物ばかりですが\x01",
            "特に支障は無いかと。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_479C():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_479C)
    Sleep(250)

    #C0189
    ChrTalk(
        0x101,
        (
            "#0002Fああ、十分だよ。\x02\x03",

            "#0004F（キーアの身元が判ったら\x01",
            "  ご両親の所へ返すことに\x01",
            "  なるだろうけど……）\x02\x03",

            "（それまではできる限りの事は\x01",
            "  してあげたいよな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_497D")

    label("loc_484D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_497D")

    #C0190
    ChrTalk(
        0x104,
        (
            "#0300F#12Pお嬢の実家にあったお古らしいな。\x02\x03",

            "#0309Fキー坊にはちょいと大きい\x01",
            "大人サイズだが、\x01",
            "ま、支障はねえだろ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_48D1():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48D1)
    Sleep(250)

    #C0191
    ChrTalk(
        0x101,
        (
            "#0002Fああ、十分だよ。\x02\x03",

            "#0004F（キーアの身元が判ったら\x01",
            "  ご両親の所へ返すことに\x01",
            "  なるだろうけど……）\x02\x03",

            "（それまではできる限りの事は\x01",
            "  してあげたいよな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_497D")

    SetChrPos(0x0, 255350, 0, 64650, 0)
    SetScenarioFlags(0xD8, 6)
    EventEnd(0x5)
    Return()

    # Function_14_4019 end

    def Function_15_4994(): pass

    label("Function_15_4994")


    def lambda_4999():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4999)

    def lambda_49B3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_49B3)
    WaitChrThread(0xFE, 1)

    def lambda_49C8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49C8)
    Return()

    # Function_15_4994 end

    def Function_16_49D1(): pass

    label("Function_16_49D1")


    #C0192
    ChrTalk(
        0x101,
        (
            "#0000Fあ、いたいた。\x02\x03",

            "副局長の件、\x01",
            "ツァイトに頼んでみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x103,
        (
            "#0200Fそうですね、ツァイトの嗅覚なら\x01",
            "副局長の歩いたルートを\x01",
            "正確に辿れると思います。\x02\x03",

            "一通り説明して\x01",
            "協力を求めてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("apl/ch50116.itc", 0x1E)
    OP_68(2940, 1200, 4980, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(24570, 0)
    SetChrPos(0x101, 2250, 30, 5500, 90)
    SetChrPos(0x102, 2500, 30, 6850, 135)
    SetChrPos(0x103, 3500, 30, 4500, 0)
    SetChrPos(0x104, 3000, 30, 3150, 0)
    OP_93(0xD, 0xB4, 0x0)
    SetChrName("")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイド達はツァイトに\x01",
            "事のあらましを伝え、協力を求めた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(2000, 0)
    OP_0D()

    #C0195
    ChrTalk(
        0x101,
        (
            "#6P#0003Fというわけで\x01",
            "力を借りたいんだが……\x02\x03",

            "#0012F……えっとツァイト、\x01",
            "ちゃんと聞いてるよな？\x02",
        )
    )

    CloseMessageWindow()
    Sound(848, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_A1(0xD, 0x4E2, 0x8, 0x0, 0x1, 0x1, 0x1, 0x1, 0x2, 0x3, 0x4)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    #C0196
    ChrTalk(
        0xD,
        (
            "#11P#1200Fグルルルル……\x02\x03",

            "グルルルル……ウォン！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 1, 0, 0)

    #C0197
    ChrTalk(
        0x104,
        "#12P#0305Fあれ、何か反応悪いぜ？\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x102,
        "#6P#0100F乗り気じゃないのかしら……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0199
    ChrTalk(
        0x103,
        (
            "#12P#0200Fいえ、大丈夫です。\x02\x03",

            "#0203F相変わらず不甲斐ない連中だ……\x01",
            "そう言いつつも\x01",
            "協力はしてくれそうです。\x02\x03",

            "#0200Fロイドさん、副局長の\x01",
            "ハンカチを渡してもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#6P#0000Fああ、これだ。\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 2900, 850, 5000, 2000, 0x0)
    Sleep(500)
    OP_96(0x101, 0x8CA, 0x0, 0x157C, 0x7D0, 0x0)

    def lambda_4D85():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D85)

    def lambda_4D92():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4D92)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    #C0201
    ChrTalk(
        0x103,
        (
            "#12P#0200Fツァイト、\x01",
            "これが目標#4Rターゲット#の匂いです。\x02\x03",

            "覚えてもらえますか？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 0x2)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xC, 0x1)
    OP_0D()

    #C0202
    ChrTalk(
        0xD,
        (
            "#5P#1203Fフンフン………\x02\x03",

            "#1200F……ウウ、グルルルル……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x103,
        "#12P#0200F『小物臭い匂いだ』。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xD,
        "#5P#1200Fグルルルル……ウォン！\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#12P#0200F『仕方がないから手を貸してやる……\x01",
            "  行きたくなったら声を掛けろ』\x01",
            "だそうです。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xC, 0x1)
    OP_0D()

    #C0206
    ChrTalk(
        0x104,
        (
            "#12P#0306Fやれやれ、相変わらず\x01",
            "尊大というかなんというか。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x102,
        (
            "#6P#0100Fふふ、でも警察犬と捜索なんて\x01",
            "警察らしくなってきたんじゃない？\x02\x03",

            "ロイド、今回は時間も掛かりそうだし\x01",
            "一応準備してから行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#6P#0000Fああ、そうだな。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_68(3500, 1030, 4500, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 3500, 0, 4500, 0)
    SetChrPos(0x1, 3500, 0, 4500, 0)
    SetChrPos(0x2, 3500, 0, 4500, 0)
    SetChrPos(0x3, 3500, 0, 4500, 0)
    OP_29(0x15, 0x1, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_16_49D1 end

    def Function_17_5084(): pass

    label("Function_17_5084")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_508E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5290")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "同行を求める\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_50F2"),
        (1, "loc_51A0"),
        (SWITCH_DEFAULT, "loc_528B"),
    )


    label("loc_50F2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0209
    ChrTalk(
        0xD,
        (
            "#1200Fグルルル……\x01",
            "グルルルルルル……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x103,
        (
            "#0200F『結婚指輪とやらを探したいなら\x01",
            "  私に同行を求めろ。』\x02\x03",

            "『しばらく付き合ってやる。』\x01",
            "……と言っています。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_528B")

    label("loc_51A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_51E1")

    #C0211
    ChrTalk(
        0x101,
        (
            "#0000Fよし、じゃあ\x01",
            "歓楽街に行ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_525C")

    label("loc_51E1")


    #C0212
    ChrTalk(
        0x101,
        (
            "#0000Fよし、じゃあ\x01",
            "歓楽街に行ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x102,
        (
            "#0100Fカジノを出たときは\x01",
            "身に付けていたそうだし……\x01",
            "まずはそこからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_525C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    AddParty(0x1B, 0xFF, 0xFF)
    SetScenarioFlags(0x93, 6)
    OP_C7(0x0, 0x1000)
    SetScenarioFlags(0x5C, 5)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Jump("loc_528B")

    label("loc_528B")

    Jump("loc_508E")

    label("loc_5290")

    Return()

    # Function_17_5084 end

    def Function_18_5291(): pass

    label("Function_18_5291")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    RemoveParty(0x1B, 0x0)
    ClearScenarioFlags(0x93, 6)
    OP_C7(0x1, 0x1000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_68(3500, 1030, 4500, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 3500, 0, 4500, 0)
    SetChrPos(0x1, 3500, 0, 4500, 0)
    SetChrPos(0x2, 3500, 0, 4500, 0)
    SetChrPos(0x3, 3500, 0, 4500, 0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x4)
    Return()

    # Function_18_5291 end

    def Function_19_5330(): pass

    label("Function_19_5330")


    #C0214
    ChrTalk(
        0x101,
        (
            "#0000Fツァイト、今日は助かったよ。\x01",
            "嗅覚の鋭さはさすがだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x103,
        (
            "#0200Fええ、予想以上です。\x02\x03",

            "物的証拠系の捜査には\x01",
            "今後も役に立ちそうかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xD,
        "#1200Fフン、グルルル……\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x103,
        (
            "#0200F『次はもう少し\x01",
            "  マシな仕事を請けてこい』\x01",
            "……だそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x104,
        "#0300Fハハ、言われちまったか。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#0100F今回は私たちよりも\x01",
            "活躍したものね。\x02\x03",

            "今後もお世話になるわね、\x01",
            "ツァイト。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 5)
    Return()

    # Function_19_5330 end

    def Function_20_54A0(): pass

    label("Function_20_54A0")

    EventBegin(0x0)
    Fade(500)
    OP_68(15900, 1550, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 14100, 850, 9500, 45)
    SetChrPos(0x104, 15600, 850, 8000, 45)
    OP_0D()

    #C0220
    ChrTalk(
        0x101,
        (
            "#0000F#6Pさてと……\x01",
            "この端末から警察本部に\x01",
            "報告を送ればいいんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x103,
        (
            "#0202F#6Pはい。\x01",
            "早速やってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_E3(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()

    label("loc_55AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B11")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E3(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_55DE"),
        (1, "loc_5604"),
        (255, "loc_5A72"),
        (SWITCH_DEFAULT, "loc_5B0C"),
    )


    label("loc_55DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_55FA")
    OP_2B(0x1, 0x2, 0x3, 0x35, 0xFFFF)
    Jump("loc_55FF")

    label("loc_55FA")

    OP_2B(0x1, 0xFFFF)

    label("loc_55FF")

    Jump("loc_5B0C")

    label("loc_5604")

    SetMapFlags(0x40000000)
    OP_E3(0x7)
    Sleep(500)
    SetChrName("受付嬢フラン")
    Sound(2062, 255, 100, 0)    #voice#Fran

    #A0222
    AnonymousTalk(
        0xFF,
        "#28Aはい、こちらクロスベル警察です～！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E3(0x4)"), scpexpr(EXPR_END)), "loc_5887")
    Sound(2067, 255, 100, 0)    #voice#Fran

    #A0223
    AnonymousTalk(
        0xFF,
        "#27Aそれでは報告を承りますね～。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_581E")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_56AD"),
        (13, "loc_56E9"),
        (12, "loc_5723"),
        (SWITCH_DEFAULT, "loc_575F"),
    )


    label("loc_56AD")

    Sound(2075, 255, 100, 0)    #voice#Fran

    #A0224
    AnonymousTalk(
        0xFF,
        (
            "#36Aクラス１ｓｔ――\x01",
            "ロイドさん、スゴすぎです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57A3")

    label("loc_56E9")

    Sound(2074, 255, 100, 0)    #voice#Fran

    #A0225
    AnonymousTalk(
        0xFF,
        (
            "#35Aクラス２ｎｄ──\x01",
            "ロイドさん、すごいです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57A3")

    label("loc_5723")

    Sound(2073, 255, 100, 0)    #voice#Fran

    #A0226
    AnonymousTalk(
        0xFF,
        (
            "#32Aクラス３ｒｄ──\x01",
            "ロイドさん、やりましたね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57A3")

    label("loc_575F")

    Sound(2073, 255, 100, 0)    #voice#Fran

    #A0227
    AnonymousTalk(
        0xFF,
        (
            "#32Aクラス３ｒｄ──(テスト)\x01",
            "ロイドさん、やりましたね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57A3")

    label("loc_57A3")

    Sound(2076, 255, 100, 0)    #voice#Fran

    #A0228
    AnonymousTalk(
        0xFF,
        (
            "#31A特典の品もすぐに\x01",
            "そちらにお届けしますね～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(2077, 255, 100, 0)    #voice#Fran

    #A0229
    AnonymousTalk(
        0xFF,
        (
            "#34Aお疲れさまでした～！\x01",
            "またよろしくお願いしますー。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_587F")

    label("loc_581E")

    Sound(2078, 255, 100, 0)    #voice#Fran

    #A0230
    AnonymousTalk(
        0xFF,
        "#16A報告は以上ですね～。\x02",
    )

    CloseMessageWindow()
    Sound(2079, 255, 100, 0)    #voice#Fran

    #A0231
    AnonymousTalk(
        0xFF,
        (
            "#37Aでは、また依頼を達成したら\x01",
            "よろしくお願いしますー。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_587F")

    SetScenarioFlags(0x1, 5)
    Jump("loc_5963")

    label("loc_5887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_5900")
    Sound(2063, 255, 100, 0)    #voice#Fran

    #A0232
    AnonymousTalk(
        0xFF,
        (
            "#32Aあれっ……\x01",
            "先ほど報告されたばかりですよ？\x02",
        )
    )

    CloseMessageWindow()
    Sound(2064, 255, 100, 0)    #voice#Fran

    #A0233
    AnonymousTalk(
        0xFF,
        "#32Aまた依頼を達成されたらお願いしますね～。\x07\x00\x02",
    )

    CloseMessageWindow()
    Jump("loc_5963")

    label("loc_5900")

    Sound(2065, 255, 100, 0)    #voice#Fran

    #A0234
    AnonymousTalk(
        0xFF,
        (
            "#37Aあれっ、報告可能な\x01",
            "依頼は無いみたいですね～。\x02",
        )
    )

    CloseMessageWindow()
    Sound(2066, 255, 100, 0)    #voice#Fran

    #A0235
    AnonymousTalk(
        0xFF,
        "#16Aまたよろしくお願いしますー。\x07\x00\x02",
    )

    CloseMessageWindow()

    label("loc_5963")

    OP_57(0x0)
    OP_E3(0x8)
    ClearMapFlags(0x40000000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A6D")
    Sleep(1000)

    #A0236
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0002Fなるほど……\x01",
            "確かにあっという間だな。\x02",
        )
    )

    CloseMessageWindow()

    #A0237
    AnonymousTalk(
        0x102,
        (
            "#0109F今後は、依頼を達成したら\x01",
            "同じように報告すればいいわけね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(824, 0, 100, 0)
    Sleep(1000)

    #A0238
    AnonymousTalk(
        0x103,
        (
            "#0205Fあ……\x01",
            "早速、新しい支援要請が\x01",
            "送られてきたみたいです。\x02\x03",

            "#0202F念のため確認してみましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1, 0x1, 0x2)

    label("loc_5A6D")

    Jump("loc_5B0C")

    label("loc_5A72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x1, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B07")

    #A0239
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0203F早速、新しい支援要請が\x01",
            "送られてきたみたいです。\x02\x03",

            "#0200F念のため確認してみましょう。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5B07")

    Jump("loc_5B0C")

    label("loc_5B0C")

    Jump("loc_55AB")

    label("loc_5B11")

    OP_E3(0x6)
    FadeToBright(300, 0)
    OP_0D()
    OP_E3(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_5B34")
    Call(1, 21)
    Jump("loc_5B36")

    label("loc_5B34")

    EventEnd(0x5)

    label("loc_5B36")

    Return()

    # Function_20_54A0 end

    def Function_21_5B37(): pass

    label("Function_21_5B37")

    Sleep(500)

    #C0240
    ChrTalk(
        0x104,
        (
            "#0301F#12P色々と来たみてぇだが……\x01",
            "また地下に魔獣が出たのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        (
            "#0101Fいわゆる『手配魔獣』ね。\x02\x03",

            "ギルドの遊撃士が退治する事が\x01",
            "多いそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0242
    ChrTalk(
        0x101,
        (
            "#0003F#5P……なあ、みんな。\x02\x03",

            "#0001Fこの『手配魔獣』、\x01",
            "俺たちで何とかしてみないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5C8C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C8C)
    Sleep(50)

    def lambda_5C9C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C9C)
    Sleep(50)

    def lambda_5CAC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5CAC)
    Sleep(300)

    #C0243
    ChrTalk(
        0x102,
        "#0105Fそれって……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x104,
        "#0305F#12P一昨日のリベンジってやつか？\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#0006F#5Pああ、あの時は\x01",
            "アリオス・マクレインに\x01",
            "助けられちゃったけど……\x02\x03",

            "#0001F前もって備えていれば\x01",
            "何とか撃退できたと思うんだ。\x02\x03",

            "せっかくの仕事初日なんだし、\x01",
            "景気付けにもなるんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        "#0103Fうーん、確かに……\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x103,
        (
            "#0204F#6Pめんどくさいですけど\x01",
            "一理ありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x104,
        (
            "#0304F#12Pいいんじゃね？\x01",
            "借りを返すって意味でもな。\x02\x03",

            "#0300Fそんじゃ、準備が出来しだい、\x01",
            "駅前の入口に行ってみようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#0000F#5Pああ！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0250
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "支援要請の中には、緊急度が高く、\x01",
            "必ず行う必要があるものが存在します。\x02",
        )
    )

    CloseMessageWindow()

    #A0251
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こうしたものは『緊急』マークが付き、\x01",
            "達成するとメインストーリーが進行します。\x02",
        )
    )

    CloseMessageWindow()

    #A0252
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それ以外の支援要請は、\x01",
            "必ずしも達成する必要はありませんが\x01",
            "期限を過ぎると消滅するので注意してください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(15730, 1850, 9350, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 15730, 850, 9350, 225)
    SetChrPos(0x1, 15730, 850, 9350, 225)
    SetChrPos(0x2, 15730, 850, 9350, 225)
    SetChrPos(0x3, 15730, 850, 9350, 225)
    OP_29(0x3D, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_21_5B37 end

    def Function_22_6052(): pass

    label("Function_22_6052")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    OP_68(-1560, 1330, 122920, 0)
    MoveCamera(38, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60AA")
    SetChrFlags(0x0, 0x8)

    label("loc_60AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60BD")
    SetChrFlags(0x1, 0x8)

    label("loc_60BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60D0")
    SetChrFlags(0x2, 0x8)

    label("loc_60D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60E3")
    SetChrFlags(0x3, 0x8)

    label("loc_60E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60F6")
    SetChrFlags(0x4, 0x8)

    label("loc_60F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6109")
    SetChrFlags(0x5, 0x8)

    label("loc_6109")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1830, 30, 122400, 270)
    FadeToBright(500, 0)
    OP_0D()

    #C0253
    ChrTalk(
        0x101,
        "#0000Fここでいいかな。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0254
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x350, 1)
    SetScenarioFlags(0x50, 6)
    OP_66(0x7, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61A9")
    ClearChrFlags(0x0, 0x8)

    label("loc_61A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61BC")
    ClearChrFlags(0x1, 0x8)

    label("loc_61BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61CF")
    ClearChrFlags(0x2, 0x8)

    label("loc_61CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61E2")
    ClearChrFlags(0x3, 0x8)

    label("loc_61E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61F5")
    ClearChrFlags(0x4, 0x8)

    label("loc_61F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6208")
    ClearChrFlags(0x5, 0x8)

    label("loc_6208")

    Call(1, 39)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_22_6052 end

    def Function_23_621F(): pass

    label("Function_23_621F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    OP_68(-2440, 1300, 129810, 0)
    MoveCamera(36, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(20500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6277")
    SetChrFlags(0x0, 0x8)

    label("loc_6277")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_628A")
    SetChrFlags(0x1, 0x8)

    label("loc_628A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_629D")
    SetChrFlags(0x2, 0x8)

    label("loc_629D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62B0")
    SetChrFlags(0x3, 0x8)

    label("loc_62B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62C3")
    SetChrFlags(0x4, 0x8)

    label("loc_62C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62D6")
    SetChrFlags(0x5, 0x8)

    label("loc_62D6")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1940, 0, 128820, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0255
    ChrTalk(
        0x101,
        "#0000Fここでいいかな。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0256
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x351, 1)
    SetScenarioFlags(0x50, 7)
    OP_66(0x8, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6376")
    ClearChrFlags(0x0, 0x8)

    label("loc_6376")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6389")
    ClearChrFlags(0x1, 0x8)

    label("loc_6389")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_639C")
    ClearChrFlags(0x2, 0x8)

    label("loc_639C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63AF")
    ClearChrFlags(0x3, 0x8)

    label("loc_63AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63C2")
    ClearChrFlags(0x4, 0x8)

    label("loc_63C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63D5")
    ClearChrFlags(0x5, 0x8)

    label("loc_63D5")

    Call(1, 39)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_23_621F end

    def Function_24_63EC(): pass

    label("Function_24_63EC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "05", 0x1, 0x1)
    OP_68(153830, 1330, 130810, 0)
    MoveCamera(29, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6444")
    SetChrFlags(0x0, 0x8)

    label("loc_6444")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6457")
    SetChrFlags(0x1, 0x8)

    label("loc_6457")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_646A")
    SetChrFlags(0x2, 0x8)

    label("loc_646A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_647D")
    SetChrFlags(0x3, 0x8)

    label("loc_647D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6490")
    SetChrFlags(0x4, 0x8)

    label("loc_6490")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_64A3")
    SetChrFlags(0x5, 0x8)

    label("loc_64A3")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 155090, 30, 129770, 344)
    FadeToBright(500, 0)
    OP_0D()

    #C0257
    ChrTalk(
        0x102,
        "#0100Fここでいいかしら。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0258
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x352, 1)
    SetScenarioFlags(0x51, 0)
    OP_66(0x9, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6545")
    ClearChrFlags(0x0, 0x8)

    label("loc_6545")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6558")
    ClearChrFlags(0x1, 0x8)

    label("loc_6558")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_656B")
    ClearChrFlags(0x2, 0x8)

    label("loc_656B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_657E")
    ClearChrFlags(0x3, 0x8)

    label("loc_657E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6591")
    ClearChrFlags(0x4, 0x8)

    label("loc_6591")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65A4")
    ClearChrFlags(0x5, 0x8)

    label("loc_65A4")

    Call(1, 39)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_24_63EC end

    def Function_25_65BB(): pass

    label("Function_25_65BB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x1, 0x1)
    OP_68(154150, 1330, 121920, 0)
    MoveCamera(53, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_661E")
    SetChrFlags(0x0, 0x8)

    label("loc_661E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6631")
    SetChrFlags(0x1, 0x8)

    label("loc_6631")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6644")
    SetChrFlags(0x2, 0x8)

    label("loc_6644")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6657")
    SetChrFlags(0x3, 0x8)

    label("loc_6657")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_666A")
    SetChrFlags(0x4, 0x8)

    label("loc_666A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_667D")
    SetChrFlags(0x5, 0x8)

    label("loc_667D")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154150, 30, 121920, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0259
    ChrTalk(
        0x102,
        "#0100Fここでいいかしら。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0260
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x353, 1)
    SetScenarioFlags(0x51, 1)
    OP_66(0xA, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_671F")
    ClearChrFlags(0x0, 0x8)

    label("loc_671F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6732")
    ClearChrFlags(0x1, 0x8)

    label("loc_6732")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6745")
    ClearChrFlags(0x2, 0x8)

    label("loc_6745")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6758")
    ClearChrFlags(0x3, 0x8)

    label("loc_6758")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_676B")
    ClearChrFlags(0x4, 0x8)

    label("loc_676B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_677E")
    ClearChrFlags(0x5, 0x8)

    label("loc_677E")

    Call(1, 39)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_25_65BB end

    def Function_26_6795(): pass

    label("Function_26_6795")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "07", 0x1, 0x1)
    OP_68(208030, 1330, 127590, 0)
    MoveCamera(25, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67ED")
    SetChrFlags(0x0, 0x8)

    label("loc_67ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6800")
    SetChrFlags(0x1, 0x8)

    label("loc_6800")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6813")
    SetChrFlags(0x2, 0x8)

    label("loc_6813")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6826")
    SetChrFlags(0x3, 0x8)

    label("loc_6826")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6839")
    SetChrFlags(0x4, 0x8)

    label("loc_6839")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_684C")
    SetChrFlags(0x5, 0x8)

    label("loc_684C")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208030, 30, 127590, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0261
    ChrTalk(
        0x103,
        "#0200Fここでいいでしょう。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0262
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x354, 1)
    SetScenarioFlags(0x51, 2)
    OP_66(0xB, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68F0")
    ClearChrFlags(0x0, 0x8)

    label("loc_68F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6903")
    ClearChrFlags(0x1, 0x8)

    label("loc_6903")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6916")
    ClearChrFlags(0x2, 0x8)

    label("loc_6916")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6929")
    ClearChrFlags(0x3, 0x8)

    label("loc_6929")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_693C")
    ClearChrFlags(0x4, 0x8)

    label("loc_693C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_694F")
    ClearChrFlags(0x5, 0x8)

    label("loc_694F")

    Call(1, 39)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_26_6795 end

    def Function_27_6966(): pass

    label("Function_27_6966")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "08", 0x1, 0x1)
    OP_68(207830, 1330, 127120, 0)
    MoveCamera(56, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69BE")
    SetChrFlags(0x0, 0x8)

    label("loc_69BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69D1")
    SetChrFlags(0x1, 0x8)

    label("loc_69D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69E4")
    SetChrFlags(0x2, 0x8)

    label("loc_69E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69F7")
    SetChrFlags(0x3, 0x8)

    label("loc_69F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A0A")
    SetChrFlags(0x4, 0x8)

    label("loc_6A0A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A1D")
    SetChrFlags(0x5, 0x8)

    label("loc_6A1D")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 207830, 30, 127120, 107)
    FadeToBright(500, 0)
    OP_0D()

    #C0263
    ChrTalk(
        0x103,
        "#0200Fここでいいでしょう。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0264
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x355, 1)
    SetScenarioFlags(0x51, 3)
    OP_66(0xC, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AC1")
    ClearChrFlags(0x0, 0x8)

    label("loc_6AC1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AD4")
    ClearChrFlags(0x1, 0x8)

    label("loc_6AD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AE7")
    ClearChrFlags(0x2, 0x8)

    label("loc_6AE7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AFA")
    ClearChrFlags(0x3, 0x8)

    label("loc_6AFA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B0D")
    ClearChrFlags(0x4, 0x8)

    label("loc_6B0D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B20")
    ClearChrFlags(0x5, 0x8)

    label("loc_6B20")

    Call(1, 39)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_27_6966 end

    def Function_28_6B37(): pass

    label("Function_28_6B37")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "03", 0x1, 0x1)
    OP_68(51760, 1300, 129800, 0)
    MoveCamera(29, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B8F")
    SetChrFlags(0x0, 0x8)

    label("loc_6B8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BA2")
    SetChrFlags(0x1, 0x8)

    label("loc_6BA2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BB5")
    SetChrFlags(0x2, 0x8)

    label("loc_6BB5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BC8")
    SetChrFlags(0x3, 0x8)

    label("loc_6BC8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BDB")
    SetChrFlags(0x4, 0x8)

    label("loc_6BDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BEE")
    SetChrFlags(0x5, 0x8)

    label("loc_6BEE")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 51760, 0, 129800, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0265
    ChrTalk(
        0x104,
        "#0300Fここでいいか。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0266
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x356, 1)
    SetScenarioFlags(0x51, 4)
    OP_66(0xD, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C8E")
    ClearChrFlags(0x0, 0x8)

    label("loc_6C8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CA1")
    ClearChrFlags(0x1, 0x8)

    label("loc_6CA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CB4")
    ClearChrFlags(0x2, 0x8)

    label("loc_6CB4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CC7")
    ClearChrFlags(0x3, 0x8)

    label("loc_6CC7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CDA")
    ClearChrFlags(0x4, 0x8)

    label("loc_6CDA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CED")
    ClearChrFlags(0x5, 0x8)

    label("loc_6CED")

    Call(1, 39)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_28_6B37 end

    def Function_29_6D04(): pass

    label("Function_29_6D04")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x1, 0x1)
    OP_68(52520, 1300, 124040, 0)
    MoveCamera(70, 13, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D67")
    SetChrFlags(0x0, 0x8)

    label("loc_6D67")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D7A")
    SetChrFlags(0x1, 0x8)

    label("loc_6D7A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D8D")
    SetChrFlags(0x2, 0x8)

    label("loc_6D8D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DA0")
    SetChrFlags(0x3, 0x8)

    label("loc_6DA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DB3")
    SetChrFlags(0x4, 0x8)

    label("loc_6DB3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DC6")
    SetChrFlags(0x5, 0x8)

    label("loc_6DC6")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52520, 0, 124040, 25)
    FadeToBright(500, 0)
    OP_0D()

    #C0267
    ChrTalk(
        0x104,
        "#0300Fここでいいか。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x357, 1)
    SetScenarioFlags(0x51, 5)
    OP_66(0xE, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E66")
    ClearChrFlags(0x0, 0x8)

    label("loc_6E66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E79")
    ClearChrFlags(0x1, 0x8)

    label("loc_6E79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E8C")
    ClearChrFlags(0x2, 0x8)

    label("loc_6E8C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E9F")
    ClearChrFlags(0x3, 0x8)

    label("loc_6E9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EB2")
    ClearChrFlags(0x4, 0x8)

    label("loc_6EB2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EC5")
    ClearChrFlags(0x5, 0x8)

    label("loc_6EC5")

    Call(1, 39)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_29_6D04 end

    def Function_30_6EDC(): pass

    label("Function_30_6EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F32")
    SetChrName("")

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "家具アイテムを入手すると\x01",
            "主人公達の部屋に置く事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x51, 6)

    label("loc_6F32")

    Return()

    # Function_30_6EDC end

    def Function_31_6F33(): pass

    label("Function_31_6F33")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis164.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力車模型が置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_31_6F33 end

    def Function_32_6FDE(): pass

    label("Function_32_6FDE")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis165.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0271
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力コンポが置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_70A9"),
        (1, "loc_70B2"),
        (2, "loc_70BB"),
        (3, "loc_70C4"),
        (4, "loc_70CD"),
        (5, "loc_70D6"),
        (6, "loc_70DF"),
        (7, "loc_70E8"),
        (SWITCH_DEFAULT, "loc_70F1"),
    )


    label("loc_70A9")

    PlayBGM("ed7400", 0)
    Jump("loc_70F1")

    label("loc_70B2")

    PlayBGM("ed7401", 0)
    Jump("loc_70F1")

    label("loc_70BB")

    PlayBGM("ed7402", 0)
    Jump("loc_70F1")

    label("loc_70C4")

    PlayBGM("ed7204", 0)
    Jump("loc_70F1")

    label("loc_70CD")

    PlayBGM("ed7205", 0)
    Jump("loc_70F1")

    label("loc_70D6")

    PlayBGM("ed7201", 0)
    Jump("loc_70F1")

    label("loc_70DF")

    PlayBGM("ed7200", 0)
    Jump("loc_70F1")

    label("loc_70E8")

    PlayBGM("ed7202", 0)
    Jump("loc_70F1")

    label("loc_70F1")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_32_6FDE end

    def Function_33_7120(): pass

    label("Function_33_7120")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis167.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0272
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "壁掛け時計がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_33_7120 end

    def Function_34_71C3(): pass

    label("Function_34_71C3")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis166.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0273
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "上品な花瓶が置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_34_71C3 end

    def Function_35_726E(): pass

    label("Function_35_726E")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis168.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0274
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "壁かけみっしぃがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_35_726E end

    def Function_36_7315(): pass

    label("Function_36_7315")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis057.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0275
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おすわりみっしぃがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_36_7315 end

    def Function_37_73BE(): pass

    label("Function_37_73BE")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis171.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0276
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "イリアポスターが飾られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_37_73BE end

    def Function_38_746D(): pass

    label("Function_38_746D")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis170.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダーツセットが置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_38_746D end

    def Function_39_751A(): pass

    label("Function_39_751A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7552")
    OP_DE(0x16, 0x0)

    label("loc_7552")

    Return()

    # Function_39_751A end

    SaveToFile()

Try(main)
