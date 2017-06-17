from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c011b.bin",                # FileName
        "c011b",                    # MapName
        "c011b",                    # Location
        0x0009,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 2, 0, 3],
    )

    BuildStringList((
        "c011b",                  # 0
        "セルゲイ課長",           # 1
        "ツァイト",               # 2
        "キーア",                 # 3
        "シャーリィ",             # 4
        "ダドリー捜査官",         # 5
        "市民",                   # 6
        "市民",                   # 7
        "市民",                   # 8
        "市民",                   # 9
        "市民",                   # 10
        "警官",                   # 11
        "食器",                   # 12
        "食器",                   # 13
        "食器",                   # 14
        "食器",                   # 15
        "食器",                   # 16
        "食器",                   # 17
        "食器",                   # 18
        "食器",                   # 19
        "食器",                   # 20
        "食器",                   # 21
        "食器",                   # 22
        "食器",                   # 23
        "食器",                   # 24
        "食器",                   # 25
        "食器",                   # 26
        "食器",                   # 27
        "食器",                   # 28
        "食器",                   # 29
        "食器",                   # 30
        "椅子",                   # 31
        "椅子",                   # 32
        "椅子",                   # 33
        "椅子",                   # 34
        "椅子",                   # 35
        "椅子",                   # 36
        "椅子",                   # 37
        "椅子",                   # 38
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch02502.itc",                   # 01
        "chr/ch08200.itc",                   # 02
        "chr/ch08202.itc",                   # 03
        "chr/ch02707.itc",                   # 04
        "chr/ch02708.itc",                   # 05
        "chr/ch02702.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  7,  0x0000)
    DeclActor(16960,   850,     10840,   2000,    16960,   1300,    10840,   0x007C, 0,  25, 0x0000)

    ChipFrameInfo(1512, 0)                                       # 0

    ScpFunction((
        "Function_0_5E8",          # 00, 0
        "Function_1_698",          # 01, 1
        "Function_2_6B4",          # 02, 2
        "Function_3_7DE",          # 03, 3
        "Function_4_83F",          # 04, 4
        "Function_5_994",          # 05, 5
        "Function_6_B4A",          # 06, 6
        "Function_7_DCF",          # 07, 7
        "Function_8_E10",          # 08, 8
        "Function_9_2E85",         # 09, 9
        "Function_10_2F14",        # 0A, 10
        "Function_11_4986",        # 0B, 11
        "Function_12_49B4",        # 0C, 12
        "Function_13_4A05",        # 0D, 13
        "Function_14_4A56",        # 0E, 14
        "Function_15_4AAE",        # 0F, 15
        "Function_16_4AF8",        # 10, 16
        "Function_17_4B1E",        # 11, 17
        "Function_18_5426",        # 12, 18
        "Function_19_5463",        # 13, 19
        "Function_20_673B",        # 14, 20
        "Function_21_8A44",        # 15, 21
        "Function_22_8AB4",        # 16, 22
        "Function_23_9DA3",        # 17, 23
        "Function_24_ADCA",        # 18, 24
        "Function_25_B8DB",        # 19, 25
        "Function_26_BFC4",        # 1A, 26
    ))


    def Function_0_5E8(): pass

    label("Function_0_5E8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_620"),
        (1, "loc_62C"),
        (2, "loc_638"),
        (3, "loc_644"),
        (4, "loc_650"),
        (5, "loc_65C"),
        (6, "loc_668"),
        (SWITCH_DEFAULT, "loc_674"),
    )


    label("loc_620")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_62C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_638")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_644")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_650")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_65C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_668")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_674")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_680")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_697")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_697")

    Return()

    # Function_0_5E8 end

    def Function_1_698(): pass

    label("Function_1_698")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B3")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_698")

    label("loc_6B3")

    Return()

    # Function_1_698 end

    def Function_2_6B4(): pass

    label("Function_2_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72E")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 14400, 850, 12500, 0)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 5570, 150, 6230, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x5)
    SetChrPos(0x9, 2880, 0, 1750, 225)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x40)

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_742")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)
    Jump("loc_7DD")

    label("loc_742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_756")
    ClearScenarioFlags(0x22, 1)
    Event(0, 10)
    Jump("loc_7DD")

    label("loc_756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_76A")
    ClearScenarioFlags(0x22, 2)
    Event(0, 17)
    Jump("loc_7DD")

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_77E")
    ClearScenarioFlags(0x22, 3)
    Event(0, 19)
    Jump("loc_7DD")

    label("loc_77E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_792")
    ClearScenarioFlags(0x22, 4)
    Event(0, 20)
    Jump("loc_7DD")

    label("loc_792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_7A9")
    ClearScenarioFlags(0x22, 5)
    SetScenarioFlags(0x0, 4)
    Event(0, 22)
    Jump("loc_7DD")

    label("loc_7A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_7BD")
    ClearScenarioFlags(0x22, 6)
    Event(0, 23)
    Jump("loc_7DD")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_7CE")
    ClearScenarioFlags(0x22, 7)
    Jump("loc_7DD")

    label("loc_7CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_7DD")
    ClearScenarioFlags(0x23, 0)
    Event(0, 24)

    label("loc_7DD")

    Return()

    # Function_2_6B4 end

    def Function_3_7DE(): pass

    label("Function_3_7DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7F3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)

    label("loc_7F3")

    SetMapObjFlags(0x19, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_816")
    SetMapObjFrame(0xFF, "asihuki", 0x0, 0x1)
    Jump("loc_825")

    label("loc_816")

    SetMapObjFrame(0xFF, "asihuki", 0x1, 0x1)

    label("loc_825")

    ClearMapObjFlags(0x6, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_83E")
    SetMapObjFlags(0x6, 0x10)
    OP_65(0x0, 0x1)

    label("loc_83E")

    Return()

    # Function_3_7DE end

    def Function_4_83F(): pass

    label("Function_4_83F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91C")

    #C0001
    ChrTalk(
        0x8,
        (
            "#01000F俺はテロリストの情報を\x01",
            "市長や警備隊方面に連絡しておく。\x02\x03",

            "ダドリー、うちの奴らの\x01",
            "お守りを頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x10A,
        (
            "#00603Fええ、任せてください。\x02\x03",

            "#00601F……さあ、行くぞお前たち。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        "#00000Fはい！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_990")

    label("loc_91C")


    #C0004
    ChrTalk(
        0x8,
        (
            "#01000Fジオフロントで\x01",
            "何があったか分からんが、\x01",
            "せいぜい気をつけろ。\x02\x03",

            "ダドリー、うちの奴らの\x01",
            "お守りを頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_990")

    TalkEnd(0xFE)
    Return()

    # Function_4_83F end

    def Function_5_994(): pass

    label("Function_5_994")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADC")

    #C0005
    ChrTalk(
        0xA,
        (
            "#01100Fみんな、いってらっしゃーい。\x02\x03",

            "#01109Fえへへ、ダドリーも気をつけてねー？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x10A,
        "#00603Fだから呼び捨ては止めろと……！\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xA,
        "#01105Fんー？\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0008
    ChrTalk(
        0x10A,
        (
            "#00606F……ええい、もういい！\x01",
            "お前たち、さっさと行くぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00012F（うーん、さすがのダドリーさんも\x01",
            "  キーアには敵わないか。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B46")

    label("loc_ADC")


    #C0010
    ChrTalk(
        0xA,
        (
            "#01109Fみんな、いってらっしゃーい。\x02\x03",

            "えへへ、ダドリーも気をつけてねー？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x10A,
        "#00603F（まったく……）\x02",
    )

    CloseMessageWindow()

    label("loc_B46")

    TalkEnd(0xFE)
    Return()

    # Function_5_994 end

    def Function_6_B4A(): pass

    label("Function_6_B4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAA")

    #C0012
    ChrTalk(
        0x9,
        "#01200Fグルルルル……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x10A,
        (
            "#00603Fフン、相変わらず偉そうな狼だ。\x02\x03",

            "#00600Fだが警察犬である以上は\x01",
            "その力を借りることもあるだろう。\x01",
            "いつでも出られる準備をしておけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        "#01200F……ウォン。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4B")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_C4B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C7F")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_C7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB3")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_CB3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE7")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_CE7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1B")
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_D1B")

    Sleep(1000)

    #C0015
    ChrTalk(
        0x104,
        (
            "#00306F（偉そうったって、\x01",
            "  他人のこと言えねーだろ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#00100F（ふふ、ダドリーさんなりの\x01",
            "  激励の仕方なんだろうけど。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_DCB")

    label("loc_DAA")


    #C0017
    ChrTalk(
        0x9,
        "#01200Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_DCB")

    TalkEnd(0xFE)
    Return()

    # Function_6_B4A end

    def Function_7_DCF(): pass

    label("Function_7_DCF")

    TalkBegin(0xFF)

    #C0018
    ChrTalk(
        0x101,
        (
            "#00000Fここはティオの部屋だ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_7_DCF end

    def Function_8_E10(): pass

    label("Function_8_E10")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis120.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis124.itp")
    CreatePortrait(3, 176, 36, 304, 164, 0, 0, 512, 256, 0, 0, 128, 128, 0xFFFFFF, 0x0, "c_vis239.itp")
    OP_68(14100, 1750, 12300, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22000, 0)
    OP_90(0x101, 1700, 850, 14100, 180)
    OP_90(0x102, 600, 4850, 14400, 180)
    OP_90(0x153, 1700, 4850, 15400, 180)
    OP_90(0x109, 600, 4850, 15700, 180)
    OP_90(0x105, 1700, 4850, 16700, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 14100, 850, 12300, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x5)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 13100, 850, 9300, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SoundLoad(98)
    SoundLoad(2668)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x1000)
    OP_70(0x19, 0x32)
    SetCameraDistance(24000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0019
    ChrTalk(
        0x8,
        (
            "#01003F#11Pふむ、ふむ……\x02\x03",

            "#01000Fそうだな。\x01",
            "そろそろ戻ってくると──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(3054, 255, 80, 0)    #voice#Zeit

    #C0020
    ChrTalk(
        0x9,
        "#01200F#12Pウォン。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)

    #C0021
    ChrTalk(
        0x8,
        (
            "#01005F#11P……おっと。\x01",
            "ちょうど戻ってきやがった。\x02",
        )
    )

    CloseMessageWindow()

    #N0022
    NpcTalk(
        0x101,
        "ロイドの声",
        "ただいま帰りました。\x02",
    )

    CloseMessageWindow()
    OP_68(4100, 1750, 10400, 2500)
    SetCameraDistance(25000, 2500)
    Sleep(1000)
    OP_90(0x101, 1700, 4850, 14100, 180)
    BeginChrThread(0x101, 3, 0, 9)

    def lambda_1141():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1141)
    Sleep(400)

    def lambda_1155():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1155)
    Sleep(600)

    def lambda_1169():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_1169)
    Sleep(400)

    def lambda_117D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_117D)
    Sleep(600)

    def lambda_1191():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1191)
    WaitChrThread(0x101, 0)

    def lambda_11A6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11A6)
    WaitChrThread(0x102, 0)

    def lambda_11B7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11B7)
    WaitChrThread(0x153, 0)

    def lambda_11C8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_11C8)
    WaitChrThread(0x109, 0)

    def lambda_11D9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11D9)
    WaitChrThread(0x105, 0)

    def lambda_11EA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11EA)

    #C0023
    ChrTalk(
        0x153,
        "#5P#01110Fかちょー、ただいまー。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#6P#00105Fあら、通信中ですか？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        "#01004F#12Pいや、もう問題ない。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(300)
    Sound(838, 0, 100, 0)
    SetMapObjFlags(0x19, 0x4)
    Sleep(500)
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    #C0026
    ChrTalk(
        0x8,
        (
            "#01002F#6Pそら、とっとと\x01",
            "そこの端末を起動してみろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        "#6P#00005Fえ、はい……？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#6P#00100F警察本部から\x01",
            "連絡が入っているんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#01003F#6P起動すれば分かる。\x02\x03",

            "#01001Fほら、新人どもと\x01",
            "キーアもこっちに来い。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x153,
        "#5P#01100Fんー？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x109,
        "#6P#10105Fは、はい。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x105,
        "#10300F何かあるみたいだね。\x02",
    )

    CloseMessageWindow()

    def lambda_13BA():
        OP_97(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13BA)
    Sleep(250)

    def lambda_13D7():
        OP_97(0x153, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_13D7)
    Sleep(250)

    def lambda_13F4():
        OP_97(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_13F4)
    Sleep(250)

    def lambda_1411():
        OP_97(0x109, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1411)
    Sleep(100)
    Fade(1000)
    OP_68(16300, 1750, 10200, 0)
    MoveCamera(13, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    EndChrThread(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    EndChrThread(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    EndChrThread(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x101, 16300, 850, 10200, 45)
    SetChrPos(0x102, 14800, 850, 9500, 45)
    SetChrPos(0x153, 15250, 850, 8500, 45)
    SetChrPos(0x109, 16200, 850, 7400, 0)
    SetChrPos(0x105, 17200, 850, 7800, 0)
    SetChrPos(0x8, 14200, 850, 11900, 135)
    SetChrPos(0x9, 13100, 850, 8900, 45)
    OP_68(16800, 1750, 10700, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0033
    ChrTalk(
        0x101,
        "#5P#00001Fえっと……\x02",
    )

    CloseMessageWindow()
    Sound(836, 0, 100, 0)
    Sleep(1200)
    StopBGM(0xBB8)
    Sound(72, 0, 100, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    OP_CB(0x3, 0x1, 0x3E8, 0x0, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x17700, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sound(1021, 0, 100, 0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0xFA, 0x0)
    OP_CB(0x3, 0x1, 0x3E8, 0x3E8, 0xFA, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(300)

    #A0034
    AnonymousTalk(
        0x101,
        "#00005F！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0035
    AnonymousTalk(
        0x102,
        "#00105Fティオちゃん！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0036
    AnonymousTalk(
        0x153,
        "#01109Fあー、ティオだぁ！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)
    Sleep(500)
    SetMessageWindowPos(-1, 150, -1, -1)
    OP_C9(0x0, 0x80000000)
    SetChrName("ティオ")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2668V#40W……こんばんは。\x01",
            "どうもお久しぶりです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA6C)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)

    #A0038
    AnonymousTalk(
        0x101,
        (
            "#00002Fティオ……！\x01",
            "いったいどうして……\x02\x03",

            "ひょっとしてクロスベルに\x01",
            "帰ってきているのか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    #Sound(2273, 255, 100, 0)    #voice#Tio
    Sleep(800)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W……まだレマン自治州の\x01",
            "エプスタイン財団の研究所にいます。\x02\x03",

            "予定よりも帰るのが\x01",
            "少し遅くなりそうなので……\x02\x03",

            "わがままを言って回線を\x01",
            "使わせてもらいました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0040
    AnonymousTalk(
        0x101,
        "#00000Fそっか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0041
    AnonymousTalk(
        0x102,
        (
            "#00109Fティオちゃん……\x01",
            "顔を見られて嬉しいわ。\x02\x03",

            "#00105Fあら、でも導力ネットって\x01",
            "自治州外のネットワークには\x01",
            "繋げられないんじゃ……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x80, 0x0, 0x100, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、本来なら有線で繋がないと\x01",
            "膨大な情報量を処理できません。\x02\x03",

            "ですが今、財団とＩＢＣとの間で\x01",
            "遠隔接続の実験が進められています。\x02\x03",

            "まあ、強力な無線ブースターが\x01",
            "レマン自治州とクロスベル自治州の間に\x01",
            "１０基ほど設置されているんですが……\x02\x03",

            "それで一応、映像と音声も\x01",
            "こうして送れているわけです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0043
    AnonymousTalk(
        0x102,
        "#00102Fそうだったの……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0044
    AnonymousTalk(
        0x101,
        "#00004F技術の進歩は凄いんだな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0045
    AnonymousTalk(
        0x153,
        (
            "#01110Fねえねえ、ティオ！\x02\x03",

            "遅くなるって言ってたけど\x01",
            "いつ帰ってくるのー？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "月末か、来月の始めには\x01",
            "そちらに戻れると思います。\x02\x03",

            "それまでの間は、\x01",
            "この通信で溜めたキーア分で\x01",
            "しのがせてもらおうかと。\x02\x03",

            "だからキーア、\x01",
            "もっとよく顔を見せてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0047
    AnonymousTalk(
        0x153,
        (
            "#01109Fえへへ……うんっ！\x02\x03",

            "#01110Fほらほら、ツァイトも\x01",
            "ティオに顔を見せてあげてー。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0048
    AnonymousTalk(
        0x9,
        "#01200Fウルルル……ウォン。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ、大丈夫。\x01",
            "元気でやってますから。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0050
    AnonymousTalk(
        0x101,
        "#00002Fはは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0051
    AnonymousTalk(
        0x102,
        (
            "#00104Fふふ……導力ネットには\x01",
            "こんな恩恵もあるのね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x180, 0x0, 0x200, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そういえばランディさんも\x01",
            "まだ戻ってないそうですが……\x02\x03",

            "ノエルさんとワジさんは\x01",
            "もう、参加したみたいですね？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0053
    AnonymousTalk(
        0x101,
        (
            "#00000Fああ、ちょうど今日から\x01",
            "仕事を始めてもらってるんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0054
    AnonymousTalk(
        0x109,
        (
            "#10102Fふふっ……\x01",
            "ティオちゃん、お久しぶり！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0055
    AnonymousTalk(
        0x105,
        (
            "#10302Fやあ。\x01",
            "お邪魔させてもらってるよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x80, 0x0, 0x100, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふふ……\x01",
            "お２人ともお久しぶりです。\x02\x03",

            "それにしても、ノエルさんが\x01",
            "出向してきたのは納得ですが……\x02\x03",

            "ワジさんがそこにいるのは\x01",
            "ちょっと不思議な光景ですね。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0057
    AnonymousTalk(
        0x105,
        "#10309Fアハハ、僕もそう思うよ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0058
    AnonymousTalk(
        0x109,
        (
            "#10106Fもう……\x01",
            "笑い事じゃないでしょ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0059
    AnonymousTalk(
        0x101,
        (
            "#00004Fはは、まあ当面は何とか\x01",
            "このメンツでやっていくよ。\x02\x03",

            "#00002Fだけどティオ……\x01",
            "早く戻ってきてくれよな！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0060
    AnonymousTalk(
        0x102,
        (
            "#00102Fええ、ティオちゃんがいないと\x01",
            "本当の支援課じゃないものね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0061
    AnonymousTalk(
        0x153,
        "#01109Fうんうん！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クス……では早めに戻れるよう\x01",
            "わたしの方も頑張ってみます。\x02\x03",

            "本当はヨナも、この通信に\x01",
            "呼ぼうと思ったんですけど……\x02\x03",

            "徹夜続きだったみたいで\x01",
            "コールしても起きて来なくて。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0063
    AnonymousTalk(
        0x101,
        (
            "#00000Fそうか……\x01",
            "あいつも頑張ってるみたいだな。\x02\x03",

            "#00006Fまあ、財団に与えた損害を\x01",
            "取り戻しているらしいからなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0064
    AnonymousTalk(
        0x102,
        (
            "#00104Fあんまり無理をしないように\x01",
            "気を配ってあげて。\x02\x03",

            "#00100Fもちろんティオちゃんも\x01",
            "無理はしないようにね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x80, 0x0, 0x100, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、分かりました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(839, 0, 90, 0)
    Sleep(400)
    Sound(839, 0, 90, 0)
    Sleep(600)
    Sound(2274, 255, 50, 0)    #voice#Tio
    Fade(250)
    OP_CB(0x3, 0x8, 0x180, 0x0, 0x200, 0x80)
    OP_0D()
    Sleep(1500)
    Sound(2676, 255, 100, 0)    #voice#Tio
    Fade(250)
    OP_CB(0x3, 0x8, 0x0, 0x80, 0x80, 0x100)
    OP_0D()
    Sleep(1200)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……すみません。\x01",
            "そろそろ時間みたいです。\x02\x03",

            "無理を言って実験用の回線を\x01",
            "使わせてもらっているので……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0067
    AnonymousTalk(
        0x101,
        "#00001Fそっか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0068
    AnonymousTalk(
        0x102,
        (
            "#00106Fもっと話していたいのに\x01",
            "残念ね……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0069
    AnonymousTalk(
        0x8,
        (
            "#01004Fまあ、また機会はあるだろ。\x02\x03",

            "#01002Fティオ、そちらの予定が付いたら\x01",
            "また連絡してくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x80, 0x0, 0x100, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "了解しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_2571")

    #A0071
    AnonymousTalk(
        0x101,
        (
            "#00004F……じゃあな、ティオ。\x02\x03",

            "#00002F戻ってきたら今度こそ\x01",
            "あの時の約束を守るから。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x80, 0x80, 0x100, 0x100)
    OP_0D()
    Sound(2275, 255, 100, 0)    #voice#Tio
    Sleep(1000)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい……\x01",
            "楽しみにしています。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0073
    AnonymousTalk(
        0x153,
        "#01111Fヤクソク～？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0074
    AnonymousTalk(
        0x102,
        (
            "#00104F何だか気になるけど……\x01",
            "まあ、いいでしょう。\x02\x03",

            "#00102Fティオちゃん。\x01",
            "また連絡してちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x80, 0x0, 0x100, 0x80)
    OP_0D()

    #A0075
    AnonymousTalk(
        0x109,
        (
            "#10109F元気でね！\x01",
            "身体には気を付けて！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2607")

    label("loc_2571")


    #A0076
    AnonymousTalk(
        0x101,
        (
            "#00002Fじゃあな、ティオ。\x01",
            "身体には気を付けてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0077
    AnonymousTalk(
        0x102,
        (
            "#00102Fよかったら\x01",
            "また連絡してちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0078
    AnonymousTalk(
        0x109,
        "#10109Fティオちゃん、元気でね！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2607")


    #A0079
    AnonymousTalk(
        0x105,
        "#10302Fアディオス、よい夜を。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0080
    AnonymousTalk(
        0x9,
        "#01200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0081
    AnonymousTalk(
        0x153,
        "#01110Fまたね～、ティオ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    Sound(2276, 255, 100, 0)    #voice#Tio
    Sleep(1000)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ、それではまた。\x01",
            "おやすみなさい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1021, 0, 50, 0)
    Sound(939, 0, 50, 0)
    OP_CB(0x3, 0x0, 0x0, 0x17700, 0xFA, 0x0)
    OP_CB(0x3, 0x1, 0x3E8, 0x0, 0xFA, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(500)
    OP_24(0x3AB)
    Sound(73, 0, 100, 0)
    OP_68(16300, 1750, 10200, 2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_6F(0x79)
    Sleep(500)

    #C0083
    ChrTalk(
        0x153,
        "#6P#01106F消えちゃった……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#00008Fああ……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#6P#00104F……何だか顔を見たら\x01",
            "ますます会いたくなったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x105,
        "#12P#10302Fフフ、青春だねぇ。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x109,
        (
            "#6P#10109Fふふっ、支援課って\x01",
            "本当に仲がいいんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00004Fはは、最初は縁もゆかりもない\x01",
            "関係だったんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0089
    ChrTalk(
        0x101,
        (
            "#11P#00000Fそうだ、課長。\x01",
            "遅くなってすみませんでした。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28C0():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_28C0)
    Sleep(50)

    def lambda_28D0():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_28D0)
    Sleep(50)

    def lambda_28E0():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_28E0)
    Sleep(50)

    def lambda_28F0():
        TurnDirection(0x153, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_28F0)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x153, 0)

    #C0090
    ChrTalk(
        0x8,
        (
            "#01004Fま、いいだろ。\x02\x03",

            "#01000F今日の報告については\x01",
            "後で聞かせてもらうとして……\x02\x03",

            "晩飯はどうなってるんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0091
    ChrTalk(
        0x101,
        "#11P#00011Fそ、そうだ、忘れてた！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0092
    ChrTalk(
        0x102,
        (
            "#6P#00108Fそういえば、このメンバーで\x01",
            "まだ当番は決めてなかったわね……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A2E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2A2E)
    Sleep(100)

    def lambda_2A3E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_2A3E)
    WaitChrThread(0x109, 2)

    #C0093
    ChrTalk(
        0x109,
        (
            "#6P#10105Fそっか、特務支援課って\x01",
            "食事が当番制なんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x105,
        (
            "#12P#10305Fなんだ、そうなのか。\x02\x03",

            "#10306F……ふむ。\x01",
            "ちょっとメンドクサイねぇ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 3)), scpexpr(EXPR_END)), "loc_2BCF")

    #C0095
    ChrTalk(
        0x101,
        (
            "#00003Fワジも支援課に入ったからには\x01",
            "ちゃんと分担してもらうからな。\x02\x03",

            "#00000F意外と料理もできるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x105,
        (
            "#12P#10304Fまあね、そこそこ出来るよ。\x02\x03",

            "#10300F面倒だからアッバスあたりに\x01",
            "作ってもらう事が多かったけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CDB")

    label("loc_2BCF")


    #C0097
    ChrTalk(
        0x101,
        (
            "#00003Fワジも支援課に入ったからには\x01",
            "ちゃんと分担してもらうからな。\x02\x03",

            "#00000F新しい料理手帳も手に入れたし、\x01",
            "苦手だったら教えるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x105,
        (
            "#12P#10302Fそれは嬉しいけど、\x01",
            "僕、そこそこ料理は出来るよ。\x02\x03",

            "#10309F面倒だからアッバスあたりに\x01",
            "作ってもらう事が多かったけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CDB")


    #C0099
    ChrTalk(
        0x101,
        (
            "#00013Fええい、だったら\x01",
            "文句を言うんじゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#6P#00109Fふふ、まあ今日のところは\x01",
            "みんなで手分けしましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x109,
        (
            "#6P#10102Fそれじゃあ、手っ取り早く\x01",
            "作れるものがよさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x153,
        "#6P#01109Fキーアも手伝うー！\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#01006F……やれやれ。\x01",
            "一服しながら待つとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        "#6P#01203Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    RemoveParty(0x52, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c0120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_E10 end

    def Function_9_2E85(): pass

    label("Function_9_2E85")


    def lambda_2E8A():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E8A)
    Sleep(200)

    def lambda_2EA7():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2EA7)
    Sleep(200)

    def lambda_2EC4():
        OP_97(0x153, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_2EC4)
    Sleep(200)

    def lambda_2EE1():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2EE1)
    Sleep(200)

    def lambda_2EFE():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2EFE)
    Return()

    # Function_9_2E85 end

    def Function_10_2F14(): pass

    label("Function_10_2F14")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    LoadChrToIndex("apl/ch51201.itc", 0x1F)
    LoadChrToIndex("apl/ch50091.itc", 0x20)
    LoadChrToIndex("chr/ch02710.itc", 0x21)
    SoundLoad(3942)
    SoundLoad(3943)
    SoundLoad(3944)
    SoundLoad(3945)
    SoundLoad(3946)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    SetChrPos(0x101, 1200, 0, -2000, 0)
    SetChrPos(0x102, 300, 0, -1800, 0)
    SetChrPos(0x104, 2700, 0, 5000, 90)
    SetChrPos(0x109, 1200, 0, -2300, 0)
    SetChrPos(0x105, 300, 0, -2100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x20)
    SetChrPos(0xB, 5300, 150, 6250, 180)
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 900, 0, -3000, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 700, 0, -2500, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x1D)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 5300, 330, 4600, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_68(5300, 900, 6250, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(24000, 3000)
    StopBGM(0xFA0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(4000, 1000, 5250, 2500)
    MoveCamera(40, 19, 0, 2500)
    BeginChrThread(0x104, 3, 0, 11)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0105
    ChrTalk(
        0x101,
        "#12P#00011Fな……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    #C0106
    ChrTalk(
        0x102,
        "#6P#00105Fランディの従妹#4Rいとこ#の……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)
    SetChrSubChip(0xB, 0x4)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0107
    ChrTalk(
        0xB,
        (
            "#11P#04609F#3942V#30Wえへへ、どもども。\x01",
            "シャーリィ・オルランドでーす。\x02\x03",

            "#04602F#3943V遅かったねー。\x01",
            "待ちくたびれちゃったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF67)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    #C0108
    ChrTalk(
        0x104,
        (
            "#6P#00301F#30W……お前……\x02\x03",

            "一体、何しに来やがった……？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "#11P#04605Fあ、つれないなー、ランディ兄は。\x02\x03",

            "#04606F２年ぶりの可愛いイトコに\x01",
            "素っ気なさすぎるんじゃないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x104,
        (
            "#6P#00303F#30Wいいから答えろ……\x01",
            "何しに来やがった。\x02\x03",

            "#00311Fいや──ここで何をしていた？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        "#11P#04604Fふふっ……\x02",
    )

    CloseMessageWindow()
    Fade(800)
    SetCameraDistance(22800, 800)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    #A0112
    AnonymousTalk(
        0xB,
        (
            "#3944V#40W──ぬるいね、ランディ兄#2Rにい#。\x02\x03",

            "#3945V#30W対人トラップを仕掛けてたら\x01",
            "入った瞬間に挽肉になってたよ？\x02\x03",

            "#3946Vいつからそんなに\x01",
            "腑抜けになっちゃったのさー？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xF6A)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    #C0113
    ChrTalk(
        0x104,
        "#6P#00311F#30W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x102,
        "#6P#00101Fあ、貴女……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x109,
        "#12P#N#10107Fいきなり何を……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0116
    ChrTalk(
        0xB,
        (
            "#11P#04612Fふふっ、心配しなくても\x01",
            "トラップとかは仕掛けてないよ。\x02\x03",

            "#04602Fランディ兄一人だったら\x01",
            "そんなお遊びもアリだったけど。\x02\x03",

            "#04604F“戦争中”でもない限り\x01",
            "一般人は巻き込みたくないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        "#6P#00110Fっ……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        "#01105F#6P#Nほえ～……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0119
    ChrTalk(
        0x105,
        (
            "#6P#N#10306Fふう……\x01",
            "こりゃまた過激な子だねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0120
    ChrTalk(
        0x101,
        (
            "#12P#00003F──君。\x01",
            "シャーリィといったか。\x02\x03",

            "#00001F改めて……\x01",
            "支援課のロイド・バニングスだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xB,
        (
            "#11P#04602Fあ、どもども。\x02\x03",

            "#04609Fこないだはゴメンねー？\x01",
            "つい耳たぶ噛んじゃってさ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#12P#00006F……それはともかく。\x02\x03",

            "#00013Fここはクロスベル警察の分室で\x01",
            "君の座っているそのソファーも\x01",
            "公費で賄#2Rまかな#われたものだ。\x02\x03",

            "トラップだの巻き込むだの……\x01",
            "子供の前で不用意な発言は\x01",
            "控えてもらおうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "#11P#04612Fあはは、ゴメンゴメン。\x02\x03",

            "#04611Fつい懐かしかったから\x01",
            "お兄#2Rにい#にジャレつきたくってさ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#6P#00306F……フン。\x01",
            "お前が俺になつくタマか。\x02\x03",

            "#00301F大方、叔父貴の使いで\x01",
            "俺を呼びに来たんだろうが？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3994():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3994)
    Sleep(50)

    def lambda_39A4():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_39A4)
    Sleep(50)

    def lambda_39B4():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_39B4)
    Sleep(50)

    def lambda_39C4():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_39C4)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0125
    ChrTalk(
        0x101,
        "#12P#00005Fえ……！\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#6P#00101Fそれって……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        "#11P#04604Fふふっ、正解。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(4000, 800, 5250, 800)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xB, 0x2)
    ClearChrFlags(0xB, 0x20)
    Sound(802, 0, 100, 0)
    OP_9D(0xB, 0x14B4, 0x1E, 0x157C, 0x1F4, 0xBB8)
    OP_93(0xB, 0x10E, 0x1F4)
    Sleep(300)

    #C0128
    ChrTalk(
        0xB,
        (
            "#04602F#11Pパパが言ってたでしょ？\x01",
            "いずれ話があるって。\x02\x03",

            "明日から忙しくなりそうだし、\x01",
            "今晩あたりはどうかだってさ。\x02\x03",

            "#04605Fあ、別に断ってもいいけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        (
            "#6P#00306Fハッ、断った場合は\x01",
            "手段#4R㈲　㈲#を選ばねぇってんだろ？\x02\x03",

            "#00311Fお見通しなんだよ。\x01",
            "……お前らのやり方はな。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "#04609F#11Pふふっ。\x01",
            "調子が戻ってきたみたいだね。\x02\x03",

            "#04602Fパパは《ノイエ＝ブラン》で\x01",
            "先にやってるけど、どうする？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        "#6P#00304Fフン、いいだろう。\x02",
    )

    CloseMessageWindow()
    OP_68(4100, 800, 5360, 1000)
    BeginChrThread(0xA, 3, 0, 16)
    Sleep(150)
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0132
    ChrTalk(
        0x104,
        (
            "#5P#00300Fみんな、悪いが\x01",
            "夕食は俺抜きで──\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0xA, 3)

    #C0133
    ChrTalk(
        0xA,
        (
            "#6P#01101Fねえねえ、ランディ。\x02\x03",

            "このお姉ちゃん、\x01",
            "ひょっとして悪いヒトー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3D4A():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3D4A)
    Sleep(50)

    def lambda_3D5A():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D5A)
    Sleep(50)

    def lambda_3D6A():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3D6A)
    Sleep(50)

    def lambda_3D7A():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D7A)
    Sleep(50)

    def lambda_3D8A():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3D8A)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0134
    ChrTalk(
        0x101,
        "#11P#00011Fちょ、キーア……！\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        "#6P#00107Fキーアちゃん、下がって……！\x02",
    )

    CloseMessageWindow()
    OP_68(3920, 800, 5320, 1000)
    MoveCamera(42, 20, 0, 1000)
    OP_6E(400, 1000)
    SetCameraDistance(24000, 1000)

    def lambda_3E2B():
        OP_95(0xFE, 1400, 0, 5500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E2B)
    Sleep(300)

    def lambda_3E48():
        OP_95(0xFE, 1800, 0, 4300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E48)
    WaitChrThread(0x102, 1)

    def lambda_3E66():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3E66)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xA, 500)

    def lambda_3E7E():
        OP_96(0xFE, 0x1F4, 0x0, 0x13EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E7E)

    def lambda_3E98():
        OP_96(0xFE, 0x384, 0x0, 0xF3C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E98)

    def lambda_3EB2():
        OP_96(0xFE, 0x3E8, 0x0, 0x12C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3EB2)
    Sleep(300)

    def lambda_3ECF():
        OP_95(0xFE, 1300, 0, 2700, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3ECF)
    Sleep(300)

    def lambda_3EEC():
        OP_95(0xFE, 2200, 0, 2500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3EEC)
    WaitChrThread(0x101, 1)

    def lambda_3F0A():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F0A)

    #C0136
    ChrTalk(
        0xB,
        (
            "#04606F#11P悪いヒトは酷いなぁ。\x02\x03",

            "#04605Fていうか何その子！？\x01",
            "メチャクチャ可愛くない！？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        "#6P#01105Fんー？\x02",
    )

    CloseMessageWindow()

    def lambda_3F8A():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3F8A)
    Sleep(100)

    def lambda_3F9A():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3F9A)

    def lambda_3FA7():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3FA7)
    WaitChrThread(0x104, 2)
    Sleep(150)

    #C0138
    ChrTalk(
        0x104,
        (
            "#6P#00303Fウチで預かってる子でな。\x02\x03",

            "#00312F#30W──手を出したら殺すぞ？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    #C0139
    ChrTalk(
        0x101,
        "#6P#00013F……！\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        "#6P#00108Fっ……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        (
            "#04612F#11Pあはは、わかった。\x02\x03",

            "#04602F少なくともこのビルを\x01",
            "爆破するのは止めておくよ。\x02\x03",

            "#04609Fあ、モチロン冗談だからね？\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x109,
        "#12P#10106F（な、なんて会話……）\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x105,
        "#6P#10308F（こりゃ、心臓に悪いね。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0144
    ChrTalk(
        0x104,
        (
            "#5P#00304F──ま、そういう事だから\x01",
            "叔父貴んトコに顔を出してくる。\x02\x03",

            "#00300F今夜中には戻るから\x01",
            "あんま心配しないでくれや。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_419E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_419E)

    #C0145
    ChrTalk(
        0x102,
        "#6P#00108Fで、でも……！\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x109,
        "#12P#10101Fさすがに危ないんじゃ……！\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#00006F──なあ、ランディ。\x02\x03",

            "#00000Fだったら俺も\x01",
            "挨拶に伺っていいかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(800)

    def lambda_42C8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_42C8)
    Sleep(50)

    def lambda_42D8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_42D8)
    Sleep(50)

    def lambda_42E8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_42E8)
    Sleep(50)

    def lambda_42F8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_42F8)
    Sleep(50)

    def lambda_4308():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4308)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0148
    ChrTalk(
        0x104,
        "#5P#00305F！？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x102,
        "#5P#00107Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x109,
        "#11P#10111Fロ、ロイドさん……！？\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#6P#00004F一応、支援課のリーダーとして\x01",
            "同僚の身内に挨拶するのは\x01",
            "礼儀だろうからな。\x02\x03",

            "#00000Fそれに高級クラブなんて\x01",
            "いい社会勉強になりそうだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "#04611F#11Pへぇ……面白いね、お兄さん。\x02\x03",

            "#04609Fいいじゃんいいじゃん、\x01",
            "せっかくだから付いてきなよ♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xB, 500)
    Sleep(150)

    #C0153
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、だったら僕も\x01",
            "ご一緒させてもらおうかな。\x02\x03",

            "#10302F高級クラブ《ノイエ＝ブラン》……\x01",
            "一度遊んでみたかったんだよね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x105, 500)

    #C0154
    ChrTalk(
        0xB,
        (
            "#04612F#11Pキレイなお兄さんもどうぞ！\x02\x03",

            "#04605Fあれ……\x01",
            "ひょっとしてお姉さん？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x105,
        (
            "#6P#10309Fフフ、一応お兄さんってことに\x01",
            "なっているみたいだけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x104,
        (
            "#5P#00306Fだあああっ！\x01",
            "なに考えてんだお前ら！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xB, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0157
    ChrTalk(
        0x104,
        (
            "#6P#00307Fシャーリィ、お前も\x01",
            "勝手に話を進めんじゃねえ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 500)
    Sleep(150)

    #C0158
    ChrTalk(
        0xB,
        (
            "#04604F#11Pまあまあ、\x01",
            "車で送り迎えするからさ。\x02\x03",

            "#04602Fそうだ、お姉さんたちも来る？\x02\x03",

            "#04606Fあ、でもその子と狼は\x01",
            "さすがに連れていけないなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        (
            "#6P#00003F──エリィ、ノエル。\x01",
            "夕食はキーアと済ませてくれ。\x02\x03",

            "#00008Fそれと課長に一応、連絡を。\x02\x03",

            "#00013Fツァイトは課長が戻るまで\x01",
            "ここの守りをよろしく頼む。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(100)

    #C0160
    ChrTalk(
        0x9,
        "#01201F#12P#Nウォン。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0161
    ChrTalk(
        0x102,
        (
            "#5P#00101Fで、でも……！\x02\x03",

            "#00106F………分かった。\x01",
            "留守の方は任せて。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x109,
        "#11P#10101F……気を付けてください！\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "#5P#01110Fねえねえ、ロイド。\x01",
            "どこかに出かけるのー？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Sleep(150)

    #C0164
    ChrTalk(
        0x101,
        (
            "#12P#00004Fああ、ランディたちと\x01",
            "ちょっと出かけてくるよ。\x02\x03",

            "#00000F遅くなるかもしれないから\x01",
            "夜更かししないで寝るんだぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        (
            "#5P#01109Fうんっ！\x01",
            "行ってらっしゃーい！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0166
    ChrTalk(
        0x104,
        "#5P#00306Fクソ、どうしてこんな事に……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x105,
        "#6P#10302Fま、腹を括るしかないんじゃない？\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_2F14 end

    def Function_11_4986(): pass

    label("Function_11_4986")

    BeginChrThread(0x101, 3, 0, 12)
    Sleep(300)
    BeginChrThread(0x102, 3, 0, 12)
    Sleep(300)
    BeginChrThread(0x109, 3, 0, 13)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 13)
    BeginChrThread(0xA, 3, 0, 14)
    BeginChrThread(0x9, 3, 0, 15)
    Return()

    # Function_11_4986 end

    def Function_12_49B4(): pass

    label("Function_12_49B4")


    def lambda_49B9():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49B9)
    Sleep(300)

    def lambda_49D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_49D6)
    WaitChrThread(0xFE, 1)

    def lambda_49EB():
        OP_97(0xFE, 0x5DC, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49EB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_49B4 end

    def Function_13_4A05(): pass

    label("Function_13_4A05")


    def lambda_4A0A():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A0A)
    Sleep(300)

    def lambda_4A27():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A27)
    WaitChrThread(0xFE, 1)

    def lambda_4A3C():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A3C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_4A05 end

    def Function_14_4A56(): pass

    label("Function_14_4A56")

    Sleep(500)

    def lambda_4A5E():
        OP_96(0xFE, 0x2BC, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A5E)

    def lambda_4A78():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A78)
    WaitChrThread(0xFE, 1)

    def lambda_4A8D():
        OP_96(0xFE, 0x190, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A8D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_14_4A56 end

    def Function_15_4AAE(): pass

    label("Function_15_4AAE")

    Sleep(1500)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_4ABE():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4ABE)

    def lambda_4AD8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4AD8)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x2D, 0x1F4)
    Return()

    # Function_15_4AAE end

    def Function_16_4AF8(): pass

    label("Function_16_4AF8")


    def lambda_4AFD():
        OP_95(0xFE, 1900, 0, 5200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4AFD)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0xB, 500)
    Return()

    # Function_16_4AF8 end

    def Function_17_4B1E(): pass

    label("Function_17_4B1E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis120.itp")
    CreatePortrait(1, 176, 36, 304, 164, 0, 0, 512, 256, 0, 128, 128, 256, 0xFFFFFF, 0x0, "c_vis239.itp")
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 4000, 850, 15000, 0)
    SetChrPos(0x104, 4000, 850, 15000, 0)
    SetChrPos(0x105, 4000, 850, 15000, 0)
    SetChrPos(0x102, 16300, 850, 10200, 45)
    SetChrPos(0x109, 14500, 850, 9100, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x9, 0x5)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 2500, 0, 5000, 225)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 3, 0, 1)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 14900, 850, 8100, 45)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetCameraDistance(22500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そうですか……そんな事に。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0169
    AnonymousTalk(
        0x102,
        (
            "#00106Fええ……ごめんなさい。\x02\x03",

            "#00108Fせっかくティオちゃんが\x01",
            "また連絡してくれたのに。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x1, 0x8, 0x100, 0x80, 0x180, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0170
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……いえ。\x01",
            "話が聞けてよかったです。\x02\x03",

            "とりあえず、今日はこれで。\x01",
            "また連絡させてもらいます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0171
    AnonymousTalk(
        0x102,
        "#00100Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0172
    AnonymousTalk(
        0xA,
        "#01102Fティオ、またねー！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0173
    AnonymousTalk(
        0x109,
        (
            "#10100Fその……\x01",
            "あんまり心配しないでね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x1, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ティオ")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、失礼します。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1021, 0, 50, 0)
    Sound(939, 0, 50, 0)
    OP_CB(0x1, 0x0, 0x0, 0x17700, 0xFA, 0x0)
    OP_CB(0x1, 0x1, 0x3E8, 0x0, 0xFA, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_24(0x3AB)
    Sound(73, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    SetCameraDistance(23000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_93(0x102, 0xE1, 0x1F4)

    #C0175
    ChrTalk(
        0x102,
        (
            "#00106Fふう……\x02\x03",

            "#00108Fロイドたち……\x01",
            "本当に大丈夫なのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x109,
        (
            "#6P#10106F相手が相手だけに\x01",
            "さすがに心配ですね……\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1000, 0, -1500, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    #N0177
    NpcTalk(
        0x8,
        "セルゲイの声",
        "おー、帰ったぞ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5077():

        label("loc_5077")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5077")

    QueueWorkItem2(0xA, 2, lambda_5077)
    Sleep(50)

    def lambda_508C():

        label("loc_508C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_508C")

    QueueWorkItem2(0x109, 2, lambda_508C)
    Sleep(50)

    def lambda_50A1():

        label("loc_50A1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_50A1")

    QueueWorkItem2(0x102, 2, lambda_50A1)

    #C0178
    ChrTalk(
        0xA,
        "#01110F#11Pあ、かちょーだ！\x02",
    )

    CloseMessageWindow()
    OP_68(1960, 1750, 2650, 2500)
    MoveCamera(40, 17, 0, 2500)
    OP_6E(380, 2500)
    SetCameraDistance(24000, 2500)
    Sleep(2000)

    def lambda_5105():
        OP_95(0xFE, 1000, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5105)

    def lambda_511F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_511F)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x102, 500)
    OP_6F(0x79)
    Sound(104, 0, 100, 0)

    #C0179
    ChrTalk(
        0x102,
        "#00102F課長……！\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x109,
        "#10102F#6Pお、お疲れさまです。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(1000)
    Fade(1000)
    OP_68(14300, 1850, 9700, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    EndChrThread(0x8, 0xFF)
    SetChrPos(0x8, 6300, 850, 9700, 90)

    def lambda_51CF():
        OP_95(0xFE, 12300, 850, 9700, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_51CF)
    SetCameraDistance(22500, 2500)
    OP_0D()
    WaitChrThread(0x8, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0xA, 0x2)
    OP_6F(0x79)

    #C0181
    ChrTalk(
        0x8,
        (
            "#6P#01000F遅くなった。\x01",
            "状況は変わっていないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x102,
        (
            "#11P#00106Fええ、先ほど\x01",
            "連絡した時のままで……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x109,
        (
            "#12P#10101F……あたしたちも店の近くで\x01",
            "待機した方がいいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x8,
        (
            "#6P#01004Fま、そう心配すんな。\x02\x03",

            "#01002F《ノイエ＝ブラン》周辺には\x01",
            "一課の監視も入ってるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x109,
        "#12P#10105Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        "#11P#00102Fそ、そうだったんですか。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x8,
        (
            "#6P#01006Fただ、連中がその気になれば\x01",
            "監視の目も潰されるかもしれん。\x02\x03",

            "#01000F……とにかく今夜は\x01",
            "連中#4Rあいつら#の帰りを待つしかねぇだろ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(14300, 2350, 9700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c0490", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_4B1E end

    def Function_18_5426(): pass

    label("Function_18_5426")


    def lambda_542B():
        OP_95(0xFE, 1000, 850, 10000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_542B)
    WaitChrThread(0x8, 1)

    def lambda_5449():
        OP_95(0xFE, 10000, 850, 10000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5449)
    WaitChrThread(0x8, 1)
    Return()

    # Function_18_5426 end

    def Function_19_5463(): pass

    label("Function_19_5463")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 63100, 0, 6900, 0)
    SetChrPos(0x102, 64000, 0, 5500, 0)
    SetChrPos(0x109, 65099, 0, 5100, 0)
    SetChrPos(0x104, 64400, 0, 6900, 0)
    SetChrPos(0x105, 62700, 0, 5500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0188
    ChrTalk(
        0x102,
        "#12P#00108F……そんな事が……\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x109,
        (
            "#10106F本当に……\x01",
            "とんでもない連中みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x8,
        (
            "#01003Fまあ、お前が《闘神》ってのを\x01",
            "継ぐって話はともかく……\x02\x03",

            "#01000F色々収穫はあったみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        (
            "#00306Fああ……\x02\x03",

            "#00308F連中が今、受けてるのは\x01",
            "１億ミラ相当の契約……\x02\x03",

            "#00301F契約相手は、流れからして\x01",
            "帝国政府なのは間違いねぇだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x105,
        (
            "#12P#10304Fそれと、明日から忙しく\x01",
            "なりそうとか言ってたから……\x02\x03",

            "#10300Fやっぱり通商会議の期間中に\x01",
            "何かしでかすつもりみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        (
            "#01003Fフム、そうなると\x01",
            "その１億の契約の内容だが……\x02\x03",

            "#01001F──ロイド、どう思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        "#12P#00005F……あ、はい。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K１億ミラの契約の内容とは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "共和国大統領の暗殺\x01",      # 0
            "鉄血宰相の安全確保\x01",      # 1
            "黒月の掃討\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_583B"),
        (1, "loc_5A66"),
        (2, "loc_5C46"),
        (SWITCH_DEFAULT, "loc_5E42"),
    )


    label("loc_583B")


    #C0196
    ChrTalk(
        0x101,
        (
            "#12P#00008Fカルバード共和国、\x01",
            "ロックスミス大統領の暗殺……\x02\x03",

            "#00006F……いや、違うな。\x02\x03",

            "仮にそうだった場合、\x01",
            "１億ミラというのは少なすぎる。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        (
            "#01004Fクク、その通りだ。\x02\x03",

            "#01002Fこの時点で考えられるとすれば\x01",
            "鉄血宰相の安全確保くらいだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0198
    ChrTalk(
        0x101,
        "#12P#00011Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#12P#00101Fな、なるほど。\x02\x03",

            "オズボーン宰相は帝国内に\x01",
            "かなりの敵対勢力を持っていると\x01",
            "言われていますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x104,
        "#00301F……そいつはアリそうだな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E42")

    label("loc_5A66")

    OP_2C(0xA3, 0x1)

    #C0201
    ChrTalk(
        0x101,
        (
            "#12P#00003F……これはカンですが……\x02\x03",

            "#00001F鉄血宰相は帝国内に、かなりの\x01",
            "敵対勢力を持つと言われています。\x02\x03",

            "このクロスベルで、そうした勢力から\x01",
            "宰相を守るというのはあり得るかと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5B8F():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5B8F)
    Sleep(50)

    def lambda_5B9F():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5B9F)
    Sleep(50)

    def lambda_5BAF():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5BAF)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    #C0202
    ChrTalk(
        0x102,
        "#12P#00105Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x104,
        (
            "#00301F……なるほど……\x01",
            "そいつはアリそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x8,
        (
            "#01004Fクク……\x01",
            "いい目の付けどころだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E42")

    label("loc_5C46")


    #C0205
    ChrTalk(
        0x101,
        (
            "#12P#00008F《黒月》の掃討……\x02\x03",

            "#00006Fいや、通商会議の期間中は\x01",
            "さすがにタイミングが悪いか。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x8,
        (
            "#01004Fクク、その通りだ。\x02\x03",

            "#01002Fこの時点で考えられるとすれば\x01",
            "鉄血宰相の安全確保くらいだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0207
    ChrTalk(
        0x101,
        "#12P#00011Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        (
            "#12P#00101Fな、なるほど。\x02\x03",

            "オズボーン宰相は帝国内に\x01",
            "かなりの敵対勢力を持っていると\x01",
            "言われていますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x104,
        "#00301F……そいつはアリそうだな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E42")

    label("loc_5E42")


    #C0210
    ChrTalk(
        0x105,
        (
            "#12P#10303Fんー、でもそれだと逆に\x01",
            "１億ミラは少し多すぎないかい？\x02\x03",

            "#10301F宰相だって自分の護衛は\x01",
            "引き連れてくるんだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x109,
        (
            "#10106F確かに……\x02\x03",

            "#10101F帝国にしても共和国にしても\x01",
            "かなりの護衛将校を\x01",
            "同行させるそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_613D")
    OP_2C(0xA3, 0x2)

    #C0212
    ChrTalk(
        0x101,
        (
            "#5P#00003F……もちろん、そういう\x01",
            "表向きの護衛とは違うだろう。\x02\x03",

            "#00008Fただ、彼らの動向を見る限り\x01",
            "様々な形でクロスベルという土地を\x01",
            "把握しようとしているのは確かだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x105,
        (
            "#12P#10300Fアルモリカ村、マインツ、\x01",
            "そしてベルガード門での目撃情報が\x01",
            "それを物語っているかもしれないね。\x02\x03",

            "#10304F食料調達や七耀石の売買という\x01",
            "もっともらしい理由があったみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        (
            "#5P#00003Fああ、各地を訪れていた\x01",
            "本当の目的は別にあったんだと思う。\x02\x03",

            "#00001Fそれこそ俺たちや遊撃士と同じく、\x01",
            "何かあっても即座に対応できるように。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_624C")

    label("loc_613D")


    #C0215
    ChrTalk(
        0x101,
        (
            "#5P#00003F……もちろん、そういう\x01",
            "表向きの護衛とは違うだろう。\x02\x03",

            "#00008Fただ、彼らの動向を見る限り\x01",
            "様々な形でクロスベルという土地を\x01",
            "把握しようとしているのは確かだ。\x02\x03",

            "#00001Fそれこそ俺たちや遊撃士と同じく、\x01",
            "何かあっても即座に対応できるように。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x105,
        "#12P#10300Fふむ……\x02",
    )

    CloseMessageWindow()

    label("loc_624C")


    #C0217
    ChrTalk(
        0x102,
        (
            "#12P#00106F確かに……\x01",
            "そんな風には感じられたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x104,
        "#00308F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        (
            "#01000F──ま、現時点で\x01",
            "推測できるのはここまでだろう。\x02\x03",

            "#01003F明日は各国首脳が来訪し、\x01",
            "オルキスタワーの除幕式がある。\x02\x03",

            "#01002Fああ、ちなみに\x01",
            "お前らにも現場に出てもらうぞ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_63E5():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_63E5)
    Sleep(50)

    def lambda_63F5():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_63F5)
    Sleep(50)

    def lambda_6405():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6405)
    Sleep(50)

    def lambda_6415():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6415)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    #C0220
    ChrTalk(
        0x101,
        "#12P#00005Fえっ……\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x102,
        "#12P#00105F現場ということは……除幕式へ？\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "#01004Fどうやら《赤い星座》の方に\x01",
            "目を奪われているみたいだからな。\x02\x03",

            "#01000F──防諜#4Rぼうちょう#やテロ対策なんてのは\x01",
            "本来、お前らの仕事じゃない。\x02\x03",

            "ここらで気分を切り替えて\x01",
            "もうちょっと状況を俯瞰#4Rふかん#してみろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        "#12P#00000F……なるほど……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x104,
        (
            "#00304Fハハ……\x01",
            "耳に痛ぇ突っ込みだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x109,
        (
            "#10105Fえっと、除幕式ということは\x01",
            "警備に参加するという事ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        (
            "#01003Fま、名目上はそうだが、\x01",
            "それよりも除幕式の様子を\x01",
            "観察することに専念しておけ。\x02\x03",

            "#01002F通商会議が始まる時の空気……\x01",
            "首脳どものオーラなんかをな。\x02\x03",

            "また違った視野が持てるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        "#12P#00000F……了解しました。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、それじゃあ特等席から\x01",
            "鑑賞させてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(64000, 1600, 8600, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 0)
    NewScene("e4010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_5463 end

    def Function_20_673B(): pass

    label("Function_20_673B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x9, 0xFF, 0xFF)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis120.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    CreatePortrait(2, 176, 36, 304, 164, 0, 0, 512, 256, 128, 0, 256, 128, 0xFFFFFF, 0x0, "c_vis240.itp")
    SoundLoad(3452)
    SoundLoad(4106)
    SoundLoad(3609)
    SoundLoad(3610)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 63100, 0, 6700, 0)
    SetChrPos(0x102, 64400, 0, 6700, 0)
    SetChrPos(0x109, 62700, 0, 5300, 0)
    SetChrPos(0x104, 64000, 0, 5300, 0)
    SetChrPos(0x105, 65099, 0, 4900, 0)
    SetChrPos(0x10A, 65099, 0, 8600, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0229
    AnonymousTalk(
        0x8,
        (
            "#01001F──なるほど。\x01",
            "両首脳を狙うテロリストか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0230
    ChrTalk(
        0x10A,
        (
            "#00606F#5Pクッ、可能性はあったが\x01",
            "そこまで具体的だったとは……\x02\x03",

            "#00610F帝国にしても共和国にしても\x01",
            "いったい何を考えている……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x8,
        (
            "#1P#01003Fま、当然何かの狙いが\x01",
            "あると見ていいだろう。\x02\x03",

            "#01000F市長や警備隊方面にも\x01",
            "伝えた方が良さそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x10A,
        (
            "#00603F#5Pええ、そちらはお任せします。\x02\x03",

            "#00601F──それにしても。\x01",
            "お前たちがあの《アルセイユ》に\x01",
            "乗ったと聞いた時には耳を疑ったぞ。\x02\x03",

            "しかも国賓クラスの２人から\x01",
            "そこまでの話を聞いてくるとは……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6AC6():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6AC6)
    Sleep(100)

    def lambda_6AD6():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6AD6)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)

    #C0233
    ChrTalk(
        0x101,
        (
            "#6P#00012Fはは、一課の方でも\x01",
            "当然チェックしていましたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        (
            "#12P#00302Fま、こっちも突然だったんだから\x01",
            "目くじら立てないで欲しいッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x10A,
        (
            "#00607F#5Pええい、突然だろうが、\x01",
            "そういう時は上に相談してから\x01",
            "招待を受けるかどうかをだな……！\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "#1P#01004Fクク、ありきたりの対応を\x01",
            "コイツらにやらせてどうすんだ？\x02\x03",

            "#01002F呼びつけた相手も規格外みたいだし、\x01",
            "ちょうど良いってところだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x10A,
        "#00606F#5Pぐっ……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x104,
        (
            "#12P#00309Fいや～、でも確かに変わった\x01",
            "お姫様と皇子だったよな。\x02\x03",

            "#00300F特にオリヴァルト皇子ってのが\x01",
            "あんな変人だとは思わなかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D12():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6D12)
    Sleep(100)

    def lambda_6D22():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6D22)
    Sleep(100)

    def lambda_6D32():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6D32)
    Sleep(100)

    def lambda_6D42():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6D42)
    Sleep(100)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0239
    ChrTalk(
        0x102,
        (
            "#5P#00106F失礼よ、ランディ。\x02\x03",

            "#00100F確かに愉快というか……\x01",
            "とても軽妙な方ではあったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#5P#00004Fでも、色々なことを\x01",
            "よく考えてる人だとは思う。\x02\x03",

            "#00000Fあの護衛をしてた少佐も\x01",
            "かなりの腕前だったみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x109,
        (
            "#6P#10102Fそれに、クローディア姫と\x01",
            "ユリア准佐は素敵でしたね……！\x02\x03",

            "#10112F姫殿下は気さくだけど気品があって\x01",
            "ユリア准佐はもう凛としてて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x105,
        (
            "#10302F#11Pふふ、ちゃんと妹さんの分まで\x01",
            "サインを貰えたみたいじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x109,
        "#6P#10111Fど、どうしてそれを……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x10A,
        (
            "#00606F#5P……まったく。\x02\x03",

            "#00600Fまあいい──テロリストの存在が\x01",
            "分かっただけでも収穫というものだ。\x02\x03",

            "少々、明日の警備シフトを\x01",
            "調整した方がいいかもしれんな……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6FE3():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6FE3)
    Sleep(100)

    def lambda_6FF3():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6FF3)
    Sleep(100)

    def lambda_7003():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7003)
    Sleep(100)

    def lambda_7013():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7013)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0245
    ChrTalk(
        0x101,
        (
            "#6P#00001Fやはり正念場は明日……\x01",
            "『通商会議』の本番ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x8,
        (
            "#1P#01003Fああ、明後日の午後には\x01",
            "首脳たちも帰国する……\x02\x03",

            "#01001F何かあるとしたら\x01",
            "明日の可能性が高いだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x102,
        (
            "#00101Fたしか……\x01",
            "会議は昼からでしたね？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x10A,
        (
            "#00600F#5Pああ、午後１時から\x01",
            "オルキスタワー３５Ｆにある\x01",
            "『国際会議場』で行われる。\x02\x03",

            "それから一度休憩を挟んで\x01",
            "夕方くらいまで続く予定だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x104,
        (
            "#12P#00305Fとなると、その会議中、\x01",
            "首脳連中を守りぬけばいいのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x10A,
        (
            "#00604F#5Pいや、オルキスタワー内部には\x01",
            "万全の警備体制が敷かれている。\x02\x03",

            "ビル自体のセキュリティもあるし、\x01",
            "会議中はむしろ安全だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "#1P#01003F加えて会場警備には\x01",
            "アリオスも参加する予定だ。\x02\x03",

            "#01002Fそれもギルドの立会いとして\x01",
            "通商会議の場にもいるそうだから\x01",
            "安心といえば安心だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        "#00102Fそうなんですか……\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x109,
        (
            "#12P#10108Fとなると、会議の前後が\x01",
            "一番危ないかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x105,
        (
            "#10304F#12Pタワーから出てきたところで\x01",
            "遠くからターンって狙撃とかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#6P#00006F正直、それが一番、\x01",
            "恐いパターンではあるよな……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(103, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 59000, -3000, 3300, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    #Sound(3609, 255, 70, 0)    #voice#KeA

    #N0256
    NpcTalk(
        0xA,
        "キーアの声",
        "#11P#13Aねえねえ、ロイドー。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_68(64000, 1000, 6300, 2000)
    MoveCamera(62, 15, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(24000, 2000)
    OP_5A()
    SetChrPos(0xA, 61500, 0, 3800, 90)

    def lambda_74A3():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_74A3)
    Sleep(50)

    def lambda_74B3():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_74B3)
    Sleep(50)

    def lambda_74C3():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_74C3)
    Sleep(50)

    def lambda_74D3():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_74D3)
    Sleep(50)

    def lambda_74E3():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_74E3)
    Sleep(50)

    def lambda_74F3():
        TurnDirection(0x10A, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_74F3)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10A, 0)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 59000, 0, 3300, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7546():
        OP_96(0xFE, 0xEE48, 0x0, 0xCE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7546)

    def lambda_7560():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7560)
    WaitChrThread(0xA, 1)

    def lambda_7575():
        OP_95(0xFE, 61500, 0, 3800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7575)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0x10A, 500)
    OP_6F(0x79)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #C0257
    ChrTalk(
        0xA,
        "#12P#01105F#3610V#30Wあ、ぶすっとしたオジサンだ！\x02",
    )

    CloseMessageWindow()
    OP_24(0xE1A)
    OP_C9(0x1, 0x80000000)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0258
    ChrTalk(
        0x10A,
        (
            "#5P#00603F……相変わらず\x01",
            "躾がなっていないようだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        "#5P#00011Fす、すみません。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        (
            "#00112F#5Pキーアちゃん、この人は\x01",
            "ダドリーさんといって……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xA,
        (
            "#12P#01109Fうんっ、ダドリー！\x02\x03",

            "#01110Fひさしぶりだねー。\x01",
            "元気だったー？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x10A,
        (
            "#5P#00604Fフン、一課の捜査官たる者、\x01",
            "体調は常に万全にしている。\x02\x03",

            "#00607F──じゃなくて！\x01",
            "呼び捨ては止めるがいい！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xA,
        (
            "#12P#01106Fえー、ダメなのー？\x02\x03",

            "#01111Fじゃあ、ダドリーおじさん？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0264
    ChrTalk(
        0x10A,
        "#5P#00610F誰がオジサンだ、誰がっ！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x109,
        "#5P#10112Fま、まあまあ。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        (
            "#5P#00309Fはは、子供にしてみりゃ、\x01",
            "十分オジサンだよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x105,
        (
            "#10302F#11Pそれでキーア。\x01",
            "なんの用なんだい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0268
    ChrTalk(
        0xA,
        (
            "#12P#01106Fあ、そうだった。\x02\x03",

            "#01100Fえっとね、ロイドたちに\x01",
            "通信が入ってるよー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0269
    ChrTalk(
        0x101,
        "#00005F#5P通信が？\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x102,
        (
            "#00105F#5Pあら、通信器のベルは\x01",
            "鳴ってなかったみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xA,
        (
            "#12P#01109Fあ、フツーのじゃなくて\x01",
            "カオが出てくるほう。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#00011F#5P端末の方か……\x01",
            "キーア、よく操作が分かったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x104,
        (
            "#00305F#5Pでも、それならティオすけか？\x01",
            "夕方連絡してきたみてぇだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        (
            "#12P#01104Fううん、ソバカスのヒト。\x02\x03",

            "#01100F何だかカオが赤くなったり\x01",
            "青くなったりしてるけどー。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(63000, 1000, 6300, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    OP_68(17800, 1750, 10700, 0)
    MoveCamera(13, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 16300, 850, 10200, 45)
    SetChrPos(0x102, 15250, 850, 8300, 45)
    SetChrPos(0x104, 14600, 850, 9400, 45)
    SetChrPos(0x109, 16200, 850, 7400, 0)
    SetChrPos(0x105, 17200, 850, 7800, 0)
    SetChrPos(0x10A, 14100, 850, 11900, 135)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 13000, 850, 10400, 90)
    SetChrPos(0xA, 13300, 850, 9300, 90)
    OP_68(16800, 1750, 10700, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Sound(72, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 21)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ヨナの声")

    #A0275
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S──遅いっての！\x02\x03",

            "#3Sまったく、\x01",
            "いつまで待たせんだよ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x101, 3)
    SetMessageWindowPos(14, 280, 60, 3)

    #A0276
    AnonymousTalk(
        0x101,
        (
            "#00012Fはは、悪い。\x02\x03",

            "#00002Fそれにしても久しぶりだな\x01",
            "元気でやっているの──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x180, 0x0, 0x200, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ヨナの声")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あーもう、\x01",
            "そんな挨拶はいいっての！\x02\x03",

            "アンタらに至急、\x01",
            "頼みたいコトがあるんだ！\x02\x03",

            "今からボクのベースを\x01",
            "見てきてくんねーか！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0278
    AnonymousTalk(
        0x101,
        "#00011Fえ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0279
    AnonymousTalk(
        0x102,
        (
            "#00105Fベースって……\x01",
            "あなたが寝泊りしていた？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ヨナの声")

    #A0280
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、ジオフロントＢ区画の\x01",
            "第８制御端末のある場所さ！\x02\x03",

            "昨日から今日にかけて\x01",
            "あの端末を勝手に使っている\x01",
            "ヤツがいるみたいなんだ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0281
    AnonymousTalk(
        0x101,
        "#00001F勝手に使ってるって……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0282
    AnonymousTalk(
        0x109,
        (
            "#10105F一体どうして\x01",
            "そんなことが判ったの？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0283
    AnonymousTalk(
        0x104,
        (
            "#00301Fつーか、ヨナ公。\x01",
            "勝手に使ってるのは\x01",
            "お前だって同じじゃねーか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x180, 0x0, 0x200, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ヨナの声")

    #A0284
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そ、それはともかく！\x02\x03",

            "ボクの留守中、あの端末には\x01",
            "強力なプロテクトをかけたんだ！\x02\x03",

            "それで、万が一それが破られたら\x01",
            "導力ネットの遠隔接続実験の時に\x01",
            "アラートを送るようにしてて……\x02\x03",

            "そのアラートが今日来てたんだよ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0285
    AnonymousTalk(
        0x101,
        "#00013Fそれは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0286
    AnonymousTalk(
        0x105,
        (
            "#10303F……君がプロテクトをかけた端末を\x01",
            "ハッキングした者がいる。\x02\x03",

            "#10301Fつまりそういうことだね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x0, 0x80, 0x80, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ヨナの声")

    #A0287
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、そういうことさ！\x01",
            "かなりのハッカーなのは間違いない！\x02\x03",

            "とにかくとっ捕まえて\x01",
            "２度と触らせないで欲しいんだ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0288
    AnonymousTalk(
        0x104,
        (
            "#00306Fったく、自分の事は棚に上げて\x01",
            "勝手なことを言ってやがるな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0289
    AnonymousTalk(
        0x102,
        (
            "#00108Fでも、かなりのハッカーって……\x01",
            "ちょっと心配ね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0290
    AnonymousTalk(
        0x101,
        (
            "#00003Fああ、レンはもう帰ったはずだし、\x01",
            "ロバーツ主任とも思えない。\x02\x03",

            "#00001Fとりあえず見てくるから\x01",
            "また後で連絡してきてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x100, 0x0, 0x180, 0x80)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("ヨナの声")

    #A0291
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、頼んだぜ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1021, 0, 50, 0)
    Sound(939, 0, 50, 0)
    OP_CB(0x2, 0x0, 0x0, 0x17700, 0xFA, 0x0)
    OP_CB(0x2, 0x1, 0x3E8, 0x0, 0xFA, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    OP_24(0x3AB)
    OP_68(16300, 1750, 10200, 0)
    MoveCamera(13, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    Sound(73, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0292
    ChrTalk(
        0x8,
        "#01000F#5Pなんだ、行くのか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0293
    ChrTalk(
        0x101,
        (
            "#11P#00003Fええ、念のため。\x02\x03",

            "#00000F何だったら俺一人で\x01",
            "見に行ってきてもいいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        "#6P#00301Fおいおい、無茶言うなよ。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x102,
        (
            "#6P#00103Fそうね……\x01",
            "いるのがハッカーだけとは\x01",
            "限らないでしょうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x109,
        "#12P#10101Fご一緒します！\x02",
    )

    CloseMessageWindow()
    OP_68(15300, 1750, 10700, 2000)
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10A)
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0297
    AnonymousTalk(
        0x10A,
        (
            "#3452V#30W──待て。\x02\x03",

            "#4106V私も同行しておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x100A)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_865A():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_865A)
    Sleep(50)

    def lambda_866A():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_866A)
    Sleep(50)

    def lambda_867A():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_867A)
    Sleep(50)

    def lambda_868A():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_868A)
    Sleep(50)

    def lambda_869A():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_869A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    #C0298
    ChrTalk(
        0x101,
        "#11P#00005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x105,
        "#12P#10302Fへえ、どんな風の吹き回しだい？\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x10A,
        (
            "#00603F#5Pフン、通商会議を前にして\x01",
            "イレギュラーな要素は少しでも\x01",
            "把握しておきたいというだけだ。\x02\x03",

            "#00601F時間が惜しい、とっとと行くぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#11P#00011Fわ、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、それじゃあ軽く、\x01",
            "食後の運動と行きますか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)
    Sleep(100)

    #C0303
    ChrTalk(
        0x102,
        (
            "#12P#00100F課長、キーアちゃん、\x01",
            "それでは行ってきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x8,
        "#01002F#5Pおお、せいぜい気をつけろ。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xA,
        "#6P#01109Fいってらっしゃーい。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0306
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダドリー捜査官がパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0307
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キャンプメニューの[TACTICS]で\x01",
            "アタックメンバーに加える事が出来ます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0x9, 0x0, 0x42)
    OP_32(0x9, 0x5, 0xC8)
    OP_42(0x9, 0x466, 0xFF)
    OP_42(0x9, 0x5E1, 0xFF)
    OP_42(0x9, 0x645, 0xFF)
    OP_42(0x9, 0x4E, 0x3)
    OP_42(0x9, 0x49, 0x4)
    OP_38(0x9, 0x80, 0x2)
    OP_38(0x9, 0x81, 0x1)
    OP_38(0x9, 0x82, 0x2)
    OP_38(0x9, 0x83, 0x2)
    OP_38(0x9, 0x84, 0x1)
    OP_38(0x9, 0x85, 0x1)
    OP_38(0x9, 0x86, 0x1)
    OP_42(0x9, 0x6D, 0x1)
    OP_42(0x9, 0xAE, 0x2)
    OP_42(0x9, 0xB8, 0x3)
    OP_42(0x9, 0x8D, 0x4)
    OP_42(0x9, 0x84, 0x5)
    OP_42(0x9, 0x7D, 0x6)
    AddCraft(0x9, 0x179)
    OP_CC(0x1, 0xFF, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 14400, 850, 12500, 0)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 5570, 150, 6230, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x5)
    SetChrPos(0x9, 2880, 0, 1750, 225)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x40)
    SetChrPos(0x0, 8790, 850, 10000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x141, 0)
    OP_29(0xA3, 0x1, 0x12)
    OP_29(0xA3, 0x1, 0x13)
    ReplaceBGM("ed7150", "ed7513")
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_673B end

    def Function_21_8A44(): pass

    label("Function_21_8A44")

    OP_CB(0x2, 0x0, 0x4B0, 0xFFFFFBB4, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x2, 0x0, 0xFFFFFAEC, 0x4B0, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x2, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x2, 0x0, 0x640, 0xFFFFFB50, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1, 0x0)
    OP_CC(0x0, 0xFF, 0x0)
    Return()

    # Function_21_8A44 end

    def Function_22_8AB4(): pass

    label("Function_22_8AB4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("apl/ch50380.itc", 0x1F)
    LoadChrToIndex("apl/ch51225.itc", 0x20)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_68(700, 1100, 4100, 0)
    MoveCamera(53, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 500, 0, 2100, 0)
    SetChrPos(0x102, -1500, 0, 1400, 45)
    SetChrPos(0x109, -2200, 0, 2200, 45)
    SetChrPos(0x105, -1900, 0, 3400, 90)
    SetChrPos(0x104, 900, 0, 900, 0)
    SetChrPos(0x103, 700, 0, 3600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 2700, 0, 5200, 225)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 700, 0, 4100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -900, 0, 5300, 135)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 2200, 0, 2400, 315)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetCameraDistance(24000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0308
    ChrTalk(
        0xA,
        (
            "#01109Fえへへ、ティオだー！\x02\x03",

            "#01110Fねえねえ、ツァイト！\x01",
            "ティオが戻ってきたよー！\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x9,
        "#01200F#5Pウォン。\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x103,
        (
            "#12P#00202Fただいまです。\x01",
            "キーア、ツァイト。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)

    def lambda_8CF9():
        OP_96(0xFE, 0x2BC, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8CF9)
    WaitChrThread(0xA, 1)
    TurnDirection(0x103, 0x8, 500)
    Sleep(300)

    #C0311
    ChrTalk(
        0x103,
        (
            "#6P#00204Fセルゲイ課長。\x01",
            "ただいま戻りました。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        (
            "#5P#01004Fああ、よく戻った。\x02\x03",

            "#01002Fフッ、いきなり仲間の\x01",
            "ピンチを救ったみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        "#12P#00004Fええ、本当に助かりました。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        (
            "#12P#00106Fあそこでティオちゃんが\x01",
            "来てくれなかったら\x01",
            "どうなっていたことか……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x109,
        "#6P#10112Fうんうん、ゾッとしますね。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xC,
        (
            "#00604F……今回ばかりは礼を\x01",
            "言わざるを得ないようだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x103, 0x101, 500)

    #C0317
    ChrTalk(
        0x103,
        "#5P#00205Fその、別に大した事は。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x104,
        "#12P#00309Fはは、照れるなって。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x105,
        (
            "#6P#10304Fまあ実際、いいタイミングで\x01",
            "戻ってきてくれたと思うよ。\x02\x03",

            "#10300Fあんなハッカーが絡んできたら\x01",
            "僕たちだけじゃお手上げだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        "#12P#00006Fそうだな……\x02",
    )

    CloseMessageWindow()
    OP_68(1300, 1100, 2800, 2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    Sleep(300)

    #C0321
    ChrTalk(
        0x101,
        (
            "#6P#00003F──課長、ダドリーさん。\x02\x03",

            "#00001F明日の通商会議ですが……\x01",
            "俺たちもオルキスタワーの警備に\x01",
            "参加させてもらえませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_90DE():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_90DE)
    Sleep(50)

    def lambda_90EE():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_90EE)
    Sleep(50)

    def lambda_90FE():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_90FE)
    Sleep(50)

    def lambda_910E():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_910E)
    Sleep(50)

    def lambda_911E():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_911E)
    Sleep(50)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x8, 0)

    #C0322
    ChrTalk(
        0x102,
        "#6P#00105Fロイド、それは……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x104,
        (
            "#12P#00305Fおいおい。\x01",
            "いきなりどうしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x8,
        "#5P#01000Fふむ……\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xC,
        (
            "#00600F#11P……会場の警備体制は\x01",
            "万全だと言ったはずだが？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#6P#00006Fですが、今日のハッカーは\x01",
            "タワーの図面らしきものを\x01",
            "何処かから入手していました。\x02\x03",

            "#00008F《銀》の言葉ではありませんが\x01",
            "何か仕掛けてくる可能性がある──\x02\x03",

            "#00001Fいや、むしろその情報を“誰か”に\x01",
            "渡した可能性が高いと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x109,
        "#6P#10101F誰か……\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x105,
        "#6P#10301Fふむ、それは誰だい？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)

    label("loc_9323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_946D")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0329
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K謎のハッカーはどこに情報を渡した？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "《黒月》\x01",            # 0
            "《赤い星座》\x01",        # 1
            "それ以外の勢力\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_93CF"),
        (1, "loc_93CF"),
        (2, "loc_944C"),
        (SWITCH_DEFAULT, "loc_9468"),
    )


    label("loc_93CF")


    #C0330
    ChrTalk(
        0x101,
        (
            "#11P#00006F（いや……それよりも\x01",
            "  欲しがる連中がいるはずだ。）\x02\x03",

            "#00001F（それは……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9447")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9447")

    Jump("loc_9468")

    label("loc_944C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9460")
    OP_2C(0xA3, 0x1)

    label("loc_9460")

    SetScenarioFlags(0x0, 3)
    Jump("loc_9468")

    label("loc_9468")

    Jump("loc_9323")

    label("loc_946D")


    #C0331
    ChrTalk(
        0x101,
        (
            "#11P#00003F《赤い星座》か《黒月》、\x01",
            "または帝国政府か共和国政府……\x02\x03",

            "どれもありえそうだけど\x01",
            "より現実味のありそうな連中がいる。\x02\x03",

            "#00013F帝国と共和国のテロリストたちさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0332
    ChrTalk(
        0x102,
        (
            "#6P#00101Fクローディア殿下と\x01",
            "オリヴァルト皇子から聞いた……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x104,
        (
            "#12P#00301Fそれぞれの国のトップを狙う\x01",
            "２グループのテロリストどもか。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x109,
        (
            "#6P#10108F確かにビルの構成図があれば\x01",
            "死角を狙えるかもしれませんね……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0335
    ChrTalk(
        0x101,
        (
            "#6P#00006Fもちろん、偽装情報の\x01",
            "可能性もあるでしょうが……\x02\x03",

            "#00001Fやはり明日、オルキスタワーで\x01",
            "何かが起きる可能性は\x01",
            "高くなったと言えると思います。\x02\x03",

            "タワー周辺の警備でもいいので\x01",
            "参加させてもらえないでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x8,
        (
            "#5P#01004Fクク、なるほどな。\x02\x03",

            "#01002Fダドリー、どうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xC,
        (
            "#00606F#11Pふう……\x01",
            "まあ、いいでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    Sleep(100)
    SetChrSubChip(0xC, 0x1)
    Sleep(100)
    SetChrSubChip(0xC, 0x2)
    Sleep(100)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    SetChrSubChip(0xC, 0x4)
    Sleep(100)
    SetChrSubChip(0xC, 0x3)
    Sound(318, 0, 100, 0)
    Sleep(500)

    #C0338
    ChrTalk(
        0xC,
        (
            "#00611F#11P──明日の正午ちょうどに、\x01",
            "オルキスタワー１Ｆに来るがいい。\x02\x03",

            "予備の警備要員として\x01",
            "通商会議の現場に入れてやる。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_991A():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_991A)
    Sleep(50)

    def lambda_992A():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_992A)
    Sleep(50)

    def lambda_993A():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_993A)
    Sleep(50)

    def lambda_994A():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_994A)
    Sleep(50)

    def lambda_995A():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_995A)
    Sleep(50)

    def lambda_996A():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_996A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0339
    ChrTalk(
        0x101,
        "#6P#00005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x104,
        "#12P#00305Fおっと、会場の方かよ。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x105,
        (
            "#6P#10302Fへえ……\x01",
            "気前がいいじゃない？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0x1)
    Sleep(80)
    SetChrSubChip(0xC, 0x0)
    Sleep(80)
    ClearChrFlags(0xC, 0x20)
    ClearChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    Sleep(300)

    #C0342
    ChrTalk(
        0xC,
        (
            "#00603F#11Pカン違いをするな。\x01",
            "あくまで予備の要員としてだ。\x02\x03",

            "市長暗殺未遂事件でも\x01",
            "偶然とはいえ役には立ったし、\x01",
            "導力ネットに詳しい人間もいる。\x02\x03",

            "#00601F万が一の保険程度だから\x01",
            "せいぜい弁#2Rわきま#えておくがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#6P#00000Fりょ、了解しました！\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x109,
        "#6P#10102F謹んで拝命します！\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x103,
        (
            "#5P#00204Fしかし、やっぱり照れ隠しの\x01",
            "一種ではないかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x104,
        (
            "#12P#00309Fハハ、いつになったら\x01",
            "デレてくれるのかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xA,
        "#01111F#5Pデレる～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 500)
    Sleep(150)

    #C0348
    ChrTalk(
        0xA,
        (
            "#01110F#5Pねえねえエリィ。\x01",
            "デレるってなにー？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        (
            "#6P#00109Fう、うーん。\x01",
            "キーアちゃんと話している時の\x01",
            "みんなの態度というか……\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x105,
        (
            "#6P#10309Fフフ、この調子じゃ\x01",
            "近いうちかもしれないね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0351
    ChrTalk(
        0xC,
        "#00610F#11Pき、貴様ら……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x8,
        (
            "#5P#01004Fクク、どうやら明日は\x01",
            "死ぬほど忙しくなりそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x9,
        "#01203Fウォン。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7150", "ed7125")
    ReplaceBGM("ed7101", "ed7125")
    SetScenarioFlags(0x22, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_8AB4 end

    def Function_23_9DA3(): pass

    label("Function_23_9DA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    LoadChrToIndex("apl/ch50092.itc", 0x25)
    LoadChrToIndex("apl/ch51090.itc", 0x26)
    LoadEffect(0x0, "event/ev12002.eff")
    OP_68(12600, 2550, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 13900, 900, 5400, 270)
    SetChrPos(0x102, 11300, 900, 7000, 90)
    SetChrPos(0x103, 11300, 900, 3800, 90)
    SetChrPos(0x104, 13900, 900, 3800, 270)
    SetChrPos(0x109, 11300, 900, 2200, 90)
    SetChrPos(0x105, 13900, 900, 2200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 11300, 900, 5400, 90)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 16300, 850, 6400, 270)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xA, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0xB, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0xC, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0xD, 0x29)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0xE, 0x2A)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0xF, 0x2B)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0x1A, 0x2C)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x1B, 0x2D)
    OP_49()
    SetChrPos(0x26, 14000, 0, 7000, 0)
    OP_D5(0x26, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x27, 14000, 0, 5400, 0)
    OP_D5(0x27, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x28, 14000, 0, 3800, 0)
    OP_D5(0x28, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x29, 14000, 0, 2200, 0)
    OP_D5(0x29, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x2A, 11200, 0, 7000, 0)
    OP_D5(0x2A, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x2B, 11200, 0, 5400, 0)
    OP_D5(0x2B, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x2C, 11200, 0, 3800, 0)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x2D, 11200, 0, 2200, 0)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x5)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1350, 7100, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x14)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13100, 1350, 6800, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x5)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12200, 1350, 7100, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x11)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12300, 1300, 6800, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x5)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1350, 5200, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x14)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13100, 1350, 4900, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x26)
    SetChrSubChip(0x19, 0x5)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 12200, 1350, 5200, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x11)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 12300, 1300, 4900, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x5)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 13000, 1350, 3800, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x14)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 13100, 1350, 3500, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x26)
    SetChrSubChip(0x1D, 0x5)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13000, 1350, 2000, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x14)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13100, 1350, 1700, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x26)
    SetChrSubChip(0x1F, 0x5)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 12200, 1350, 2000, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x24)
    SetChrSubChip(0x20, 0x11)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12300, 1300, 1700, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x26)
    SetChrSubChip(0x21, 0x5)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 12200, 1350, 3800, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x24)
    SetChrSubChip(0x22, 0x11)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12300, 1300, 3500, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x25)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 16300, 750, 5500, 0)
    SetChrChipByIndex(0x24, 0x26)
    SetChrSubChip(0x24, 0x6)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 12650, 1450, 5900, 0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x26)
    SetChrSubChip(0x25, 0x6)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 12650, 1450, 2750, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12650, 1550, 5900, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12650, 1550, 2750, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    OP_68(12600, 2050, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0354
    ChrTalk(
        0x101,
        (
            "#00008F#11P……遅いな、課長。\x02\x03",

            "#00006Fあんな事があったからには\x01",
            "無理もないと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x109,
        "#12P#10108Fはい……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0356
    ChrTalk(
        0x102,
        (
            "#5P#00106F……今ごろオルキスタワーで\x01",
            "今後の対策について\x01",
            "話し合われているんでしょうね。\x02\x03",

            "#00108F政治的にも難しい問題だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x105,
        (
            "#10306F#11Pヴァルドもそうだけど……\x02\x03",

            "#10301F難しい時期にとんでもない事を\x01",
            "しでかしてくれたもんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xA,
        (
            "#6P#01106F……ねえねえ、みんな。\x02\x03",

            "#01112Fかちょーが帰って来ないんだったら\x01",
            "やっぱりお鍋はやめとくー？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    #C0359
    ChrTalk(
        0x104,
        (
            "#00304F#11P……いや、遅くなったら\x01",
            "先に始めてろって言ってたしな。\x02\x03",

            "#00300Fせっかくキー坊が用意してくれたし、\x01",
            "俺たちだけでも先に頂いとこうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xA,
        "#6P#01108Fで、でも……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    #C0361
    ChrTalk(
        0x103,
        "#6P#00208Fランディさん……\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x101,
        (
            "#00006F#5P鍋のことはともかく……\x01",
            "ランディ、無理してないか？\x02\x03",

            "#00008Fこういう時だからこそ\x01",
            "俺たちを頼ってくれたら──\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    #C0363
    ChrTalk(
        0x104,
        (
            "#00302F#11Pハハ、もちろん頼ってるっての。\x02\x03",

            "#00303F前にも言ったが……\x01",
            "叔父貴たちとの縁は切れている。\x02\x03",

            "今さら古巣が何をしたところで\x01",
            "そこまで堪えるってことはねぇさ。\x02\x03",

            "#00304Fそれよりも今はメシを喰って\x01",
            "休めるうちに休んで……\x02\x03",

            "#00300F──明日に備えるのが先決だろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x101,
        "#00005F#5Pそれは……\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x109,
        (
            "#6P#10112Fそ、そうですね……！\x02\x03",

            "#10100Fお腹が空いては\x01",
            "戦はできないって言いますし！\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x102,
        (
            "#5P#00109Fふふ、貴方#4Rランディ#のそういうタフさには\x01",
            "いつも助けられているわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x103,
        "#6P#00202F……ですね。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x105,
        (
            "#10304F#11Pま、今日は湖の方でも\x01",
            "とんでもない連中と出くわしたし。\x02\x03",

            "#10302F早めに食事を済ませて休んだ方が\x01",
            "明日のためになるかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        "#00004F#5Pそうだな……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0370
    ChrTalk(
        0x101,
        (
            "#00002F#11P──よし。\x01",
            "それじゃあ鍋を始めよう。\x02\x03",

            "#00004Fキーアが準備してくれたから\x01",
            "肉、魚、野菜──タップリある。\x02\x03",

            "#00000Fたくさん食べて、早めに休んで……\x01",
            "明日に備えよう！\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x104,
        "#00309F#11Pおお！\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x109,
        "#12P#10109Fいただきます！\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x102,
        (
            "#5P#00102Fキーアちゃん、後は私たちに任せて\x01",
            "お腹いっぱい食べてね？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(100)

    #C0374
    ChrTalk(
        0xA,
        "#6P#01109F……うんっ！\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x103,
        (
            "#6P#00202Fツァイトはお肉とお魚を\x01",
            "後で冷ましてあげます。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x9,
        "#01200F#11Pグルルル……ウォン。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetChrPos(0x29, 22900, 0, 12700, 0)
    SetChrPos(0x2A, 22900, 0, 12700, 0)
    SetChrPos(0x2B, 22900, 0, 12700, 0)
    SetChrPos(0x2C, 22900, 0, 12700, 0)
    SetChrPos(0x2D, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    VolumeBGM(0x3C, 0x7D0)
    Sleep(2000)
    SetScenarioFlags(0x22, 4)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_9DA3 end

    def Function_24_ADCA(): pass

    label("Function_24_ADCA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50006.itc", 0x1F)
    LoadChrToIndex("apl/ch51517.itc", 0x20)
    LoadChrToIndex("chr/ch30000.itc", 0x21)
    LoadChrToIndex("chr/ch20400.itc", 0x22)
    LoadChrToIndex("chr/ch21100.itc", 0x23)
    LoadChrToIndex("chr/ch20100.itc", 0x24)
    LoadChrToIndex("chr/ch21000.itc", 0x25)
    LoadChrToIndex("chr/ch21400.itc", 0x26)
    LoadChrToIndex("chr/ch08201.itc", 0x27)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SoundLoad(803)
    SoundLoad(852)
    SoundLoad(3621)
    SoundLoad(3622)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrPos(0x0, 4000, 850, 15000, 0)
    SetChrPos(0x1, 4000, 850, 15000, 0)
    SetChrPos(0x2, 4000, 850, 15000, 0)
    SetChrPos(0x3, 4000, 850, 15000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 200, 0, 1600, 180)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2200, 0, 2300, 225)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -1300, 0, 4400, 180)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 400, 0, 4000, 180)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 1700, 0, 4400, 180)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 900, 0, 5600, 180)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 3700, 0, 5400, 180)
    SetChrChipByIndex(0x11, 0x26)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 4700, 0, 5400, 180)
    OP_7D(0xFF, 0xE6, 0xDC, 0x0, 0x0)
    OP_68(1000, 1000, 0, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20400, 0)
    OP_68(1020, 1000, 3180, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0377
    ChrTalk(
        0xD,
        (
            "#5Pい、一体外は\x01",
            "どうなっているんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xE,
        (
            "#5P……夫は……\x01",
            "あの人は無事なのかしら……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(100)

    #C0379
    ChrTalk(
        0x8,
        (
            "#12P#01003Fあー、皆さん落ち着いて。\x02\x03",

            "#01002F今入った連絡によると\x01",
            "謎の武装集団が\x01",
            "撤退を開始したそうです。\x02\x03",

            "安全が確認されしだい、\x01",
            "ちゃんと家に戻れますよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B11E():
        TurnDirection(0xE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_B11E)
    Sleep(30)

    def lambda_B12E():
        TurnDirection(0x10, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B12E)
    Sleep(30)

    def lambda_B13E():
        TurnDirection(0x11, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_B13E)
    Sleep(30)
    WaitChrThread(0xE, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x11, 0)

    #C0380
    ChrTalk(
        0xE,
        "#5Pそ、そうなの！？\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xD,
        (
            "#5Pおお、女神#4Rエイドス#よ……\x01",
            "ご加護に感謝します……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 1000)

    def lambda_B1BA():
        OP_9A(0xFE, 0x8, 0x4B0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B1BA)
    WaitChrThread(0xA, 1)

    #C0382
    ChrTalk(
        0xA,
        (
            "#5P#01112F#30Wかちょー……\x01",
            "もう、だいじょうぶなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x8,
        (
            "#11P#01006Fああ、ひとまずはな。\x02\x03",

            "#01001Fロイドたちのヤツ……\x01",
            "無事でいるといいんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xA,
        (
            "#5P#01104F#30W──うん、大丈夫。\x02\x03",

            "#01121Fロイドたちなら平気だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x8,
        (
            "#11P#01005Fん、ああ……そうだな。\x02\x03",

            "#01002F何だかんだ言って\x01",
            "奴等も成長しているからな。\x02\x03",

            "#01004Fひょっとしたら\x01",
            "かつてのセルゲイ班より──\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(300)
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(150)
    Fade(250)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x2)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x8, 0x3)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0386
    ChrTalk(
        0x8,
        (
            "#11P#01003Fはい、こちら支援課──\x02\x03",

            "#01005F……おお、ダドリーか。\x01",
            "そっちの様子はどうだ？\x02\x03",

            "#01001F…………なに？\x01",
            "猟兵どもの飛行艇だと……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)
    Sleep(500)

    def lambda_B46B():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xCE4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B46B)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)

    def lambda_B498():
        OP_96(0xFE, 0x190, 0x0, 0x1A90, 0xDAC, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B498)
    WaitChrThread(0xA, 1)
    OP_68(1000, 2000, 3000, 3000)

    def lambda_B4C7():
        OP_96(0xFE, 0x514, 0x352, 0x2BC0, 0xDAC, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B4C7)
    WaitChrThread(0xA, 1)

    def lambda_B4E5():
        OP_96(0xFE, 0x514, 0xFA0, 0x3B60, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B4E5)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_6F(0x79)
    Sleep(1000)
    OP_68(-300, 800, 72310, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0xA, 1400, 0, 70000, 0)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(-260, 1300, 72270, 2500)

    def lambda_B574():
        OP_96(0xFE, 0xFFFFFED4, 0x0, 0x11A6C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B574)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    OP_6F(0x79)
    Sleep(300)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)
    Sleep(500)
    Fade(500)
    SetCameraDistance(19500, 800)
    Sound(928, 0, 60, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    SetCameraDistance(18500, 30000)
    Sleep(500)

    #C0387
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#01119F#40W#11P………………………………\x02\x03",

            "#01118F#40W………やっぱり…………\x02\x03",

            "#01120F#40Wやっぱりどうやっても\x01",
            "……これが一番マシみたい……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopEffect(0x0, 0x2)
    StopSound(852, 1000, 100)
    Sleep(1300)

    #C0388
    ChrTalk(
        0xA,
        "#01123F#40W#11P……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x20)
    Sleep(500)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    SetChrSubChip(0xA, 0x1)
    Sleep(500)
    SetCameraDistance(18000, 20000)

    #C0389
    ChrTalk(
        0xA,
        (
            "#01112F#30W#11P#15A………もしもし………？\x02\x03",

            "#01108F#40W#25A………………うん………\x01",
            "…………うん…………………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0390
    ChrTalk(
        0xA,
        "#01121F#3621V#40W#11P#20A──だいじょうぶ。\x02",
    )
    #Auto

    CloseMessageWindow()
    SetCameraDistance(18000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0391
    AnonymousTalk(
        0xA,
        (
            "#3622V#30W#40Aもう……\x01",
            "ちゃんと決心できたから。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_24(0x323)
    OP_24(0x354)
    Sleep(500)
    SetScenarioFlags(0x22, 0)
    NewScene("c110D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_ADCA end

    def Function_25_B8DB(): pass

    label("Function_25_B8DB")

    TalkBegin(0xFF)
    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B8F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFA6")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_B930"),
        (1, "loc_BAE2"),
        (2, "loc_BF8A"),
        (3, "loc_BF92"),
        (SWITCH_DEFAULT, "loc_BFA1"),
    )


    label("loc_B930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B943")
    OP_2B(0x94, 0xFFFF)
    Jump("loc_BADD")

    label("loc_B943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B95E")
    OP_2B(0x8E, 0x8F, 0x90, 0x91, 0x92, 0xFFFF)
    Jump("loc_BADD")

    label("loc_B95E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B9B7")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("自動アナウンス")

    #A0392
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "現在、支援要請はありません。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_BADD")

    label("loc_B9B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B9D2")
    OP_2B(0x8B, 0x8C, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_BADD")

    label("loc_B9D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BA0D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B9FB")
    OP_2B(0x85, 0x86, 0x87, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_BA08")

    label("loc_B9FB")

    OP_2B(0x85, 0x86, 0x88, 0x80, 0x83, 0xFFFF)

    label("loc_BA08")

    Jump("loc_BADD")

    label("loc_BA0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BA26")
    OP_2B(0x80, 0x81, 0x82, 0x83, 0xFFFF)
    Jump("loc_BADD")

    label("loc_BA26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_BA34")
    Jump("loc_BADD")

    label("loc_BA34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BA51")
    OP_2B(0x79, 0x7A, 0x7B, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_BADD")

    label("loc_BA51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_BA6E")
    OP_2B(0x74, 0x75, 0x76, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_BADD")

    label("loc_BA6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BA87")
    OP_2B(0x6F, 0x70, 0x71, 0x72, 0xFFFF)
    Jump("loc_BADD")

    label("loc_BA87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_BABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_BAAB")
    OP_2B(0x6A, 0x6B, 0x6C, 0x6D, 0x67, 0xFFFF)
    Jump("loc_BAB6")

    label("loc_BAAB")

    OP_2B(0x6A, 0x6B, 0x6C, 0x67, 0xFFFF)

    label("loc_BAB6")

    Jump("loc_BADD")

    label("loc_BABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_BAD2")
    OP_2B(0x65, 0x66, 0x67, 0xFFFF)
    Jump("loc_BADD")

    label("loc_BAD2")

    OP_2B(0x65, 0x66, 0x67, 0x68, 0xFFFF)

    label("loc_BADD")

    Jump("loc_BFA1")

    label("loc_BAE2")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BBBF")
    SetChrName("自動アナウンス")

    #A0393
    AnonymousTalk(
        0xFF,
        "こちらはクロスベル警察です。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_BB98")

    #A0394
    AnonymousTalk(
        0xFF,
        "報告を承ります。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("自動アナウンス")

    #A0395
    AnonymousTalk(
        0xFF,
        (
            "報告処理を終了します。\x01",
            "お疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBBA")

    label("loc_BB98")


    #A0396
    AnonymousTalk(
        0xFF,
        "報告可能な依頼はありません。\x02",
    )

    CloseMessageWindow()

    label("loc_BBBA")

    Jump("loc_BF7C")

    label("loc_BBBF")

    SetChrName("受付嬢フラン")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BC13")
    Sound(3062, 255, 100, 0)    #voice#Fran

    #A0397
    AnonymousTalk(
        0xFF,
        "#26Aはい、こちらクロスベル警察です～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC3F")

    label("loc_BC13")

    Sound(3061, 255, 100, 0)    #voice#Fran

    #A0398
    AnonymousTalk(
        0xFF,
        "#29A皆さん、どうもお疲れさまですー。\x02",
    )

    CloseMessageWindow()

    label("loc_BC3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_BE88")
    Sound(3067, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0399
    AnonymousTalk(
        0xFF,
        "#27Aそれでは報告を承りますね～。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE13")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_BCB0"),
        (13, "loc_BCFA"),
        (12, "loc_BD42"),
        (SWITCH_DEFAULT, "loc_BD8C"),
    )


    label("loc_BCB0")

    Sound(3075, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0400
    AnonymousTalk(
        0xFF,
        (
            "#39Aクラス１ｓｔ――\x01",
            "ロイドさん、スゴすぎです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD8C")

    label("loc_BCFA")

    Sound(3074, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0401
    AnonymousTalk(
        0xFF,
        (
            "#38Aクラス２ｎｄ──\x01",
            "ロイドさん、すごいです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD8C")

    label("loc_BD42")

    Sound(3073, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0402
    AnonymousTalk(
        0xFF,
        (
            "#33Aクラス３ｒｄ──\x01",
            "ロイドさん、やりましたね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD8C")

    label("loc_BD8C")

    Sound(3076, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0403
    AnonymousTalk(
        0xFF,
        (
            "#33A特典の品もすぐに\x01",
            "そちらにお届けしますね～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)    #voice#Fran

    #A0404
    AnonymousTalk(
        0xFF,
        (
            "#33Aお疲れさまでした～！\x01",
            "またよろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE80")

    label("loc_BE13")

    Sound(3078, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0405
    AnonymousTalk(
        0xFF,
        "#17A報告は以上ですね～。\x02",
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)    #voice#Fran

    #A0406
    AnonymousTalk(
        0xFF,
        (
            "#38Aでは、また依頼を達成したら\x01",
            "よろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE80")

    SetScenarioFlags(0x0, 6)
    Jump("loc_BF7C")

    label("loc_BE88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_BF0D")
    Sound(3063, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0407
    AnonymousTalk(
        0xFF,
        (
            "#31Aあれっ……\x01",
            "先ほど報告されたばかりですよ？\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)    #voice#Fran

    #A0408
    AnonymousTalk(
        0xFF,
        "#35Aまた依頼を達成されたらお願いしますね～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF7C")

    label("loc_BF0D")

    Sound(3065, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0409
    AnonymousTalk(
        0xFF,
        (
            "#38Aあれっ、報告可能な\x01",
            "依頼は無いみたいですね～。\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)    #voice#Fran

    #A0410
    AnonymousTalk(
        0xFF,
        "#20Aまたよろしくお願いしますー。\x02",
    )

    CloseMessageWindow()

    label("loc_BF7C")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_BFA1")

    label("loc_BF8A")

    Call(0, 26)
    Jump("loc_BFA1")

    label("loc_BF92")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BFA1")

    label("loc_BFA1")

    Jump("loc_B8F7")

    label("loc_BFA6")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_25_B8DB end

    def Function_26_BFC4(): pass

    label("Function_26_BFC4")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_BFE6")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFE6")
    ClearScenarioFlags(0x2A, 0)

    label("loc_BFE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_C003")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C003")
    ClearScenarioFlags(0x2A, 1)

    label("loc_C003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_C020")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C020")
    ClearScenarioFlags(0x2A, 2)

    label("loc_C020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_C03D")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C03D")
    ClearScenarioFlags(0x2A, 3)

    label("loc_C03D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_C05A")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C05A")
    ClearScenarioFlags(0x2A, 4)

    label("loc_C05A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_C077")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C077")
    ClearScenarioFlags(0x2A, 5)

    label("loc_C077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_C083")
    SetScenarioFlags(0x2A, 6)

    label("loc_C083")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0D5")
    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0x0)
    Jump("loc_C150")

    label("loc_C0D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C127")
    OP_24(0x80)
    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Sound(128, 1, 50, 0)
    Jump("loc_C150")

    label("loc_C127")

    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()

    label("loc_C150")

    Return()

    # Function_26_BFC4 end

    SaveToFile()

Try(main)
