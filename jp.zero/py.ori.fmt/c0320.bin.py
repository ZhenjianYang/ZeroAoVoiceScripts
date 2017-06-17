from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0320.bin",                # FileName
        "c0320",                    # MapName
        "c0320",                    # Location
        0x002D,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 45, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0320",                  # 0
        "キャンベル議員",         # 1
        "共和国派議員",           # 2
        "共和国派議員",           # 3
        "カーラ",                 # 4
        "マーシャ",               # 5
    ))

    AddCharChip((
        "chr/ch27702.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch27802.itc",                   # 02
        "chr/ch33200.itc",                   # 03
        "chr/ch34500.itc",                   # 04
    ))

    DeclNpc(0,       250,     46110,   180,  469,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(-2490,   0,       48869,   45,   389,  0x0, 0,   1,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(2299,    250,     43630,   270,  341,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(43490,   59,      3440,    135,  389,  0x0, 0,   3,   0,   0,   2,   0,   8,   255,  0)
    DeclNpc(-44409,  0,       10199,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(45950,   60,      1790,    1500,    46410,   1000,    1270,    0x007C, 0,  13, 0x0000)

    ScpFunction((
        "Function_0_190",          # 00, 0
        "Function_1_248",          # 01, 1
        "Function_2_273",          # 02, 2
        "Function_3_29E",          # 03, 3
        "Function_4_311",          # 04, 4
        "Function_5_383",          # 05, 5
        "Function_6_88D",          # 06, 6
        "Function_7_9F0",          # 07, 7
        "Function_8_1343",         # 08, 8
        "Function_9_1717",         # 09, 9
        "Function_10_1A13",        # 0A, 10
        "Function_11_298F",        # 0B, 11
        "Function_12_3185",        # 0C, 12
        "Function_13_3A7E",        # 0D, 13
    ))


    def Function_0_190(): pass

    label("Function_0_190")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1D0"),
        (1, "loc_1DC"),
        (2, "loc_1E8"),
        (3, "loc_1F4"),
        (4, "loc_200"),
        (5, "loc_20C"),
        (6, "loc_218"),
        (SWITCH_DEFAULT, "loc_224"),
    )


    label("loc_1D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_1DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_1E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_1F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_200")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_20C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_218")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_224")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_230")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_247")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_247")

    Return()

    # Function_0_190 end

    def Function_1_248(): pass

    label("Function_1_248")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_272")
    OP_94(0xFE, 0xFFFFF57E, 0xC1DE, 0xFFFFEFFC, 0xB4AA, 0x3E8)
    Sleep(300)
    Jump("Function_1_248")

    label("loc_272")

    Return()

    # Function_1_248 end

    def Function_2_273(): pass

    label("Function_2_273")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29D")
    OP_94(0xFE, 0xAE56, 0xD70, 0xA320, 0x67C, 0x3E8)
    Sleep(300)
    Jump("Function_2_273")

    label("loc_29D")

    Return()

    # Function_2_273 end

    def Function_3_29E(): pass

    label("Function_3_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_2B9")
    ClearChrFlags(0xC, 0x80)

    label("loc_2B9")

    Jump("loc_2FE")

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2DB")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_2FE")

    label("loc_2DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2FE")
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0xA, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2FE")
    ClearChrFlags(0xC, 0x80)

    label("loc_2FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_310")
    ClearChrFlags(0xB, 0x80)

    label("loc_310")

    Return()

    # Function_3_29E end

    def Function_4_311(): pass

    label("Function_4_311")

    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34C")
    OP_66(0x0, 0x1)

    label("loc_34C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_365")
    OP_10(0x0, 0x0)
    OP_10(0x7, 0x1)
    Jump("loc_36B")

    label("loc_365")

    OP_10(0x0, 0x1)
    OP_10(0x7, 0x0)

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_382")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_382")

    label("loc_382")

    Return()

    # Function_4_311 end

    def Function_5_383(): pass

    label("Function_5_383")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AD")
    Call(0, 10)
    Return()

    label("loc_3AD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_441")
    Jump("loc_48B")

    label("loc_441")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_461")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48B")

    label("loc_461")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_481")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48B")

    label("loc_481")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_534")

    #C0001
    ChrTalk(
        0xFE,
        (
            "……娘を連れ戻してくれたこと、\x01",
            "一応礼を言っておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "フン、それだけだ。\x01",
            "もう下がりたまえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AF")

    label("loc_534")


    #C0003
    ChrTalk(
        0xFE,
        (
            "フン……やはり警察は\x01",
            "当てにならんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "まあいい、連絡先さえ判っていれば\x01",
            "力づくでも連れ戻せよう。\x01",
            "何とでもなる……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AF")

    Jump("loc_885")

    label("loc_5B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C5")

    #C0005
    ChrTalk(
        0xFE,
        (
            "今日は議会だの黒月の一件だので\x01",
            "朝からごたごたしていたのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "昼過ぎに所用があってな、\x01",
            "一度戻ってきたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "しかし何度呼んでも\x01",
            "娘もメイドも出てこぬ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "不審に思っていると\x01",
            "書き置きがあった、というわけだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BD")

    #C0009
    ChrTalk(
        0x104,
        "#0301F（普段から傍若無人っぽいな。）\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#0006F（この分では\x01",
            "  お嬢さんの行き先にも\x01",
            "  心当たりは無さそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x2D, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BD")

    #C0011
    ChrTalk(
        0x103,
        (
            "#0200F（情報が揃いましたね……\x01",
            "　一度カーラさんの部屋に戻って\x01",
            "　推理を再開しましょう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#0000F（ああ、そうしよう。）\x02",
    )

    CloseMessageWindow()

    label("loc_7BD")

    SetScenarioFlags(0x0, 0)
    Jump("loc_885")

    label("loc_7C5")


    #C0013
    ChrTalk(
        0xFE,
        (
            "昼過ぎに所用で戻ると\x01",
            "娘もメイドもいなかったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "……娘の事はよろしく頼むぞ。\x01",
            "このままでは帝国派に\x01",
            "攻撃材料を与えかねん。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#0108F（カーラさんの事、\x01",
            "  心配じゃないのかしら……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_885")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_383 end

    def Function_6_88D(): pass

    label("Function_6_88D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_976")

    #C0016
    ChrTalk(
        0xFE,
        (
            "議員秘書の収賄疑惑に\x01",
            "あの議長邸を発端とする不可解な事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "ふむ、帝国派を攻撃するには\x01",
            "どれが一番効果的だろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "予算議会もそろそろ佳境だし、\x01",
            "早くまとめてキャンベル議員の加勢に\x01",
            "向かわなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_9EC")

    label("loc_976")


    #C0019
    ChrTalk(
        0xFE,
        (
            "キャンベル議員が\x01",
            "議会に乗り込んでいる間、\x01",
            "僕が戦うための情報を集めているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "議会は情報の戦いだからねぇ。\x02",
    )

    CloseMessageWindow()

    label("loc_9EC")

    TalkEnd(0xFE)
    Return()

    # Function_6_88D end

    def Function_7_9F0(): pass

    label("Function_7_9F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A1A")
    Call(0, 10)
    Return()

    label("loc_A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_CDE")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB7")
    Jump("loc_B01")

    label("loc_AB7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AD7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B01")

    label("loc_AD7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B01")

    label("loc_AF7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B01")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD8")

    #C0021
    ChrTalk(
        0xFE,
        (
            "ついさっき\x01",
            "自治州議会が終わったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "……うーん、\x01",
            "今年はやけに長かったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "それだけ我々共和国派が\x01",
            "食い下がったという事だろうね。\x01",
            "うふふふ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CD2")

    label("loc_BD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_C65")

    #C0024
    ChrTalk(
        0xFE,
        (
            "コホン……にしても\x01",
            "やっぱりお嬢さんが\x01",
            "戻ってきて良かったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "メイドさんがいなくちゃ、\x01",
            "お茶も出てこないんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD2")

    label("loc_C65")


    #C0026
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "お茶はまだかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "ここのメイド、\x01",
            "さっきから見かけないが\x01",
            "一体何をしているんだ……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1342")

    label("loc_CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1342")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D7E")
    Jump("loc_DC8")

    label("loc_D7E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D9E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DC8")

    label("loc_D9E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DBE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DC8")

    label("loc_DBE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DC8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1012")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8B")

    #C0028
    ChrTalk(
        0xFE,
        (
            "いや、良かった。\x01",
            "これで帝国派に嗅ぎ付かれる事も\x01",
            "ないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "ふふふ……安心して\x01",
            "議会対策に精を出せるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EF9")

    label("loc_E8B")


    #C0030
    ChrTalk(
        0xFE,
        (
            "それにしても議員、\x01",
            "珍しく動揺していたな……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "まさか本気でお嬢さんの心配を\x01",
            "……なわけないか、ははは！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF9")

    Jump("loc_100D")

    label("loc_EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC7")

    #C0032
    ChrTalk(
        0xFE,
        (
            "え、お嬢さんを\x01",
            "連れ戻せなかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "まあ帝国派に嗅ぎ付かれなきゃ\x01",
            "何だっていいんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "こっちは黒月や\x01",
            "議会対策に忙しいんだ、\x01",
            "もう顔を出さないでくれるか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_100D")

    label("loc_FC7")


    #C0035
    ChrTalk(
        0xFE,
        (
            "こっちは黒月や\x01",
            "議会対策に忙しいんだ。\x01",
            "もう顔を出さないでくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100D")

    Jump("loc_133B")

    label("loc_1012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B2")

    #C0036
    ChrTalk(
        0xFE,
        (
            "議員は決まりごとに\x01",
            "厳格な方でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "例えば、朝食は必ず\x01",
            "一緒にとるように、という風だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "お嬢さんにも\x01",
            "それを守るよう言うわけだが、\x01",
            "彼女はそれが気に入らないらしくてね。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AA")

    #C0039
    ChrTalk(
        0x103,
        "#0203F……そうですか。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "お２人が不仲なのは\x01",
            "その辺りが原因かもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "……ともあれ、今朝の朝食には\x01",
            "お嬢さんも顔を出していたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "私もご一緒させて\x01",
            "もらったからねえ。\x01",
            "間違いはないとも。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A4")

    #C0043
    ChrTalk(
        0x103,
        (
            "#0200F（情報が揃いましたね……\x01",
            "　一度カーラさんの部屋に戻って\x01",
            "　推理を再開しましょう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0000F（ああ、そうしよう。）\x02",
    )

    CloseMessageWindow()

    label("loc_12A4")

    OP_29(0x2D, 0x1, 0x3)

    label("loc_12AA")

    SetScenarioFlags(0x0, 1)
    Jump("loc_133B")

    label("loc_12B2")


    #C0045
    ChrTalk(
        0xFE,
        (
            "ともかく議会対策と\x01",
            "黒月の件でこっちは手一杯なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "君たち、なるべく内密に、\x01",
            "帝国派に気取られないよう\x01",
            "捜索を進めてくれたまえ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133B")

    SetChrSubChip(0xFE, 0x2)
    TalkEnd(0xFE)

    label("loc_1342")

    Return()

    # Function_7_9F0 end

    def Function_8_1343(): pass

    label("Function_8_1343")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1473")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E9")

    #C0047
    ChrTalk(
        0xFE,
        (
            "予算議会が終わったそうですね。\x01",
            "お父様も早めに帰ってくるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "……仕方がありませんわ……\x01",
            "私が晩餐に付き合ってあげますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_146E")

    label("loc_13E9")


    #C0049
    ChrTalk(
        0xFE,
        (
            "……今日は\x01",
            "指図されたからじゃないんです。\x01",
            "気が向いたからなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "私だって、お父様を心底\x01",
            "嫌っているわけではないですもの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_146E")

    Jump("loc_1713")

    label("loc_1473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_15B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_152F")

    #C0051
    ChrTalk(
        0xFE,
        (
            "今日はマーシャと\x01",
            "お買い物にいく予定なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "ふふ……お父様も\x01",
            "小言を言わなくなりましたし。\x01",
            "とても自由な気分ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "これも皆さんのお陰ですわね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_15AE")

    label("loc_152F")


    #C0054
    ChrTalk(
        0xFE,
        (
            "今日はマーシャと\x01",
            "お買い物にいく予定なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "ふふ……お父様も\x01",
            "小言を言わなくなりましたし。\x01",
            "とても自由な気分ですわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AE")

    Jump("loc_1713")

    label("loc_15B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1713")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B6")

    #C0056
    ChrTalk(
        0xFE,
        "やっぱり我が家が一番ですわ。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "……エリィさん、皆さん。\x01",
            "今日はお世話になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#0100F気にしないで下さい。\x01",
            "それより……お父様と\x01",
            "もう少し話し合われて下さいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "ええ、もう大丈夫ですわ。\x01",
            "私も自信が付きましたから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1713")

    label("loc_16B6")


    #C0060
    ChrTalk(
        0xFE,
        (
            "……エリィさん、皆さん。\x01",
            "今日はお世話になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "また遊びにいらしてくださいね。\x02",
    )

    CloseMessageWindow()

    label("loc_1713")

    TalkEnd(0xFE)
    Return()

    # Function_8_1343 end

    def Function_9_1717(): pass

    label("Function_9_1717")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1792")

    #C0062
    ChrTalk(
        0xFE,
        (
            "今晩は豪華なご馳走を\x01",
            "用意しているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "ふふ……お嬢様も旦那様も\x01",
            "喜んでくれるといいのですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0F")

    label("loc_1792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_185D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_180D")

    #C0064
    ChrTalk(
        0xFE,
        (
            "お嬢様、とっても\x01",
            "笑顔になられました。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "ふふ……今日のお買い物は\x01",
            "私もとても楽しみです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1858")

    label("loc_180D")


    #C0066
    ChrTalk(
        0xFE,
        "……お嬢様…………\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "家出したきりお一人で……\x01",
            "大丈夫でしょうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1858")

    Jump("loc_1A0F")

    label("loc_185D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1A0F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_19A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195F")

    #C0068
    ChrTalk(
        0xFE,
        (
            "皆さん、本当になんと\x01",
            "お礼を言っていいのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "やっぱり相談してよかったです。\x01",
            "あのままお嬢様に従うよりも……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#0000Fまた何かあれば相談してくれ。\x01",
            "俺たち『特務支援課』にさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "は、はい。\x01",
            "ぜひそうします！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_19A4")

    label("loc_195F")


    #C0072
    ChrTalk(
        0xFE,
        (
            "皆さん、ありがとうございました。\x01",
            "私、勇気を出してよかったです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A4")

    Jump("loc_1A0F")

    label("loc_19A9")


    #C0073
    ChrTalk(
        0xFE,
        (
            "今日はお仕事を\x01",
            "放り出してしまいました……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "……すぐに支度しないと\x01",
            "お食事が間に合いません……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0F")

    TalkEnd(0xFE)
    Return()

    # Function_9_1717 end

    def Function_10_1A13(): pass

    label("Function_10_1A13")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(440, 1000, 42830, 0)
    MoveCamera(54, 20, 0, 0)
    OP_6E(390, 0)
    SetCameraDistance(22640, 0)
    SetChrPos(0x101, 500, 0, 40660, 0)
    SetChrPos(0x102, -500, 0, 40660, 0)
    SetChrPos(0x103, -500, 60, 39200, 0)
    SetChrPos(0x104, 500, 60, 39200, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0075
    ChrTalk(
        0x8,
        "#5Pまったく面倒な事をしおって……！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xA,
        (
            "#11Pですが議員、何とか\x01",
            "手を打たないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#12P#0000Fあの、すみません。\x01",
            "支援要請を見て伺ったのですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    SetChrSubChip(0xA, 0x1)
    Fade(300)
    SetChrPos(0xA, 1900, 60, 43630, 270)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_95(0xA, 2029, 60, 42410, 1000, 0x0)
    OP_93(0xA, 0xE1, 0x190)

    #C0078
    ChrTalk(
        0xA,
        "#5P警察のなんとか課だね？\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "#5Pよかった、藁にもすがる\x01",
            "想いだったものでね！\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        "#5Pおや、いや待て……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "#5Pそちらはマクダエル市長の所の\x01",
            "エリィ君ではないか。\x01",
            "何故君が同席しているのかね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        (
            "#12P#0103Fご無沙汰しています、議員。\x02\x03",

            "#0100Fあの、私は現在は\x01",
            "警察に勤務していまして。\x01",
            "今日は一警察官として伺いました。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        "#5Pそ、そうだったか。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "#5Pむむ、まあ中立派の市長のことだ。\x01",
            "大事は無かろうが……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)
    Sleep(300)

    #C0085
    ChrTalk(
        0xA,
        (
            "#11Pでも議員、帝国派の連中は\x01",
            "姑息ですからねぇ。\x01",
            "どこから嗅ぎ付けてくるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#12P#0300F（……お嬢って政治的に\x01",
            "  問題になるような立場なんだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        (
            "#12P#0106F（議員の先生達と話すのは\x01",
            "  肩が凝るわ……）\x02\x03",

            "#0101Fあの議員、話せる範囲でいいので\x01",
            "話していただけませんか？\x02\x03",

            "何かとても\x01",
            "お困りだったようですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        (
            "#12P#0200F確か支援要請では\x01",
            "『要人の捜索依頼』とありましたが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    #C0089
    ChrTalk(
        0x8,
        (
            "#5Pそ、そうだった。\x01",
            "実は厄介な事になっていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "#5P……この際、仕方がない。\x01",
            "全て説明してしまおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "#5Pだが断っておくぞ。\x01",
            "これは政治的判断が絡む重要案件だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "#5P我が共和国派も\x01",
            "難しい局面であるし……\x01",
            "この件、絶対に他言せぬように！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#12P#0001F分かりました。\x01",
            "お約束しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        (
            "#12P#0100F議員の不利になる事にしないと\x01",
            "誓います。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        "#5Pよし、では話そう。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "#5P……実はわが共和国派から\x01",
            "とある人物が消えてしまってな。\x02",
        )
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

    #C0097
    ChrTalk(
        0x103,
        "#12P#0205F消えた……？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        "#5P私の娘だ。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "#5Pメイドと一緒に\x01",
            "家出してしまったらしいのだ。\x02",
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
    Sleep(1200)

    #C0100
    ChrTalk(
        0x104,
        (
            "#12P#0306F（もったいぶっといて\x01",
            "  娘の家出かよ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        (
            "#12P#0101F娘さん……カーラさんですね。\x01",
            "私は日曜学校で\x01",
            "一緒だった事があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xA,
        (
            "#5Pおやそうだったか。\x01",
            "……議員はお嬢さんと\x01",
            "あまり仲がよろしくないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "#5P普段から口論の\x01",
            "絶えない仲、というかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        "#5Pだが今は時期が悪くて……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "#5P我々の後ろ盾である黒月が\x01",
            "今朝方襲撃されたらしくてね。\x01",
            "こちらも対応に手一杯なんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "#5Pフン、馬鹿娘め。\x01",
            "この忙しい時だ、放っておきたい\x01",
            "所なのだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "#5P近頃はマフィア同士の抗争も\x01",
            "激しくなっておるようだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "#5Pメイドと２人でさまよっていては\x01",
            "危険も少なくは無かろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#12P#0003Fなるほど、やはり\x01",
            "お嬢さんの身の上が心配だと。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "#5P……それにこの事が公になれば\x01",
            "帝国派の連中が\x01",
            "攻撃材料にしてくるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "#5P議会もまだまだ混戦中、\x01",
            "不祥事は避けたいのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "#5P君たち、何としても\x01",
            "内密に連れ戻してくれたまえ。\x02",
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
    Sleep(1200)

    #C0113
    ChrTalk(
        0x103,
        "#12P#0203F（結局世間体のようですね……）\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        "#12P#0306F（お偉いさんらしい考え方だぜ。）\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x102,
        "#12P#0103F（予想はしていたけれど……）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_25EE():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_25EE)
    Sleep(50)

    def lambda_25FE():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25FE)

    def lambda_260B():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_260B)

    def lambda_2618():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2618)
    Sleep(400)

    #C0116
    ChrTalk(
        0x102,
        (
            "#6P#0101Fでも心配なのは確かだし……\x01",
            "事件に巻き込まれる可能性も\x01",
            "低くないと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        "#12P#0003Fそうだな……\x02",
    )

    CloseMessageWindow()

    def lambda_269B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_269B)

    def lambda_26A8():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_26A8)

    def lambda_26B5():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_26B5)

    def lambda_26C2():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26C2)
    Sleep(400)

    #C0118
    ChrTalk(
        0x101,
        (
            "#12P#0001F分かりました、\x01",
            "お嬢様をお探ししましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        "#5Pおお、よかった！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        "#5Pすぐに連れ戻してくれたまえ。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそこまでは確約できかねますが……\x02\x03",

            "#0001Fお嬢様の行き先を突き止めて\x01",
            "身の安全を図れるように\x01",
            "したいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "#5Pまあ、仕方ないか。\x01",
            "後はなんとでもなる……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        "#5Pその方針で進めてくれたまえ。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "#5Pお嬢さんの部屋に\x01",
            "書き置きが残されているようなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xA,
        (
            "#5P捜査するのなら\x01",
            "手がかりにするといい。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2886():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2886)

    def lambda_2893():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2893)

    def lambda_28A0():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_28A0)

    def lambda_28AD():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_28AD)
    Sleep(300)

    #C0126
    ChrTalk(
        0x102,
        (
            "#12P#0101F分かりました、\x01",
            "拝見させていただきます。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【要人の捜索依頼】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 30, 0, 40130, 180)
    SetChrPos(0xA, 2300, 250, 43630, 270)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x2)
    OP_29(0x2D, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_1A13 end

    def Function_11_298F(): pass

    label("Function_11_298F")

    EventBegin(0x0)
    Fade(800)
    OP_68(44280, 1560, 2580, 0)
    MoveCamera(56, 25, 0, 0)
    OP_6E(390, 0)
    SetCameraDistance(21530, 0)
    SetChrPos(0x101, 44280, 60, 2500, 135)
    SetChrPos(0x102, 45340, 60, 3250, 135)
    SetChrPos(0x103, 43820, 60, 3620, 135)
    SetChrPos(0x104, 44820, 60, 4220, 135)
    OP_0D()

    #C0128
    ChrTalk(
        0x101,
        (
            "#12P#0005F手帳に書き置きが\x01",
            "残されてるみたいだな……\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x102, 45710, 60, 2120, 1000, 0x0)
    OP_93(0x102, 0x5A, 0x190)

    #C0129
    ChrTalk(
        0x102,
        (
            "#11P#0103Fええと……\x02\x03",

            "『もういいです、\x01",
            "  お父様だけ好きにやればいいのですわ。』\x02\x03",

            "『私は私で好きにやらせてもらいます！\x01",
            "  ……カーラ』。\x02\x03",

            "『ＰＳ：メイドも連れて行きますから。\x01",
            "  食事の支度ができずに\x01",
            "  困ればいいのですわ！』\x02",
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
    Sleep(1200)

    #C0130
    ChrTalk(
        0x101,
        "#12P#0006Fなんと言うか……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#5P#0306F父親も父親だが、\x01",
            "娘の方も身勝手みてえだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x190)
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    #C0132
    ChrTalk(
        0x102,
        (
            "#11P#0108Fキャンベル議員は\x01",
            "家庭を顧みないタイプなのよ。\x02\x03",

            "そういえば昔から\x01",
            "よく父親の事を愚痴っていたし……\x02\x03",

            "#0103F何かきっかけさえあれば\x01",
            "家出してもおかしくないと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        (
            "#6P#0203Fしかしきっかけについては\x01",
            "書かれてないようですね。\x02\x03",

            "#0200F本人の意思で家出したという事しか\x01",
            "分からないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそうだな……\x01",
            "この文面から分かるとすれば……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【突発的な家出】\x01",      # 0
            "【計画的な家出】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EE2")
    TurnDirection(0x101, 0x104, 400)
    TurnDirection(0x104, 0x101, 400)
    Sleep(300)

    #C0135
    ChrTalk(
        0x101,
        (
            "#12P#0003F割と突発的かもしれないな。\x02\x03",

            "エリィの言うとおり\x01",
            "何かきっかけがあって……\x02\x03",

            "#0001Fそれにカチンときて\x01",
            "飛び出してしまったんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x103,
        "#6P#0200Fなるほど、そんな感じです。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        (
            "#5P#0300F計画的なら、もっと\x01",
            "ウラミツラミを\x01",
            "書き連ねるだろうしな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 1)
    Jump("loc_300C")

    label("loc_2EE2")


    #C0138
    ChrTalk(
        0x101,
        "#12P#0003F計画的な家出、なのかな……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)
    Sleep(300)

    #C0139
    ChrTalk(
        0x104,
        (
            "#5P#0305F計画的なら、もっと\x01",
            "ウラミツラミを書くんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x103,
        (
            "#6P#0200F自分の反抗の意志を伝えるために\x01",
            "しっかりとした文面が\x01",
            "起こされそうですね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    Sleep(300)

    #C0141
    ChrTalk(
        0x101,
        (
            "#12P#0006Fそ、そうか。\x02\x03",

            "この走り書きだと、むしろ\x01",
            "突発的な家出かもしれない……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_300C")


    #C0142
    ChrTalk(
        0x102,
        (
            "#11P#0101F家出してしまったのは\x01",
            "いつ頃なのかしら。\x02\x03",

            "#0108Fまだ遠くへ行っていないと\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3176")
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    #C0143
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそれは文脈からじゃ\x01",
            "分からないな。\x02\x03",

            "#0001F一度議員たち２人に\x01",
            "聞いてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        "#5P#0300Fうっし、確認してくるか。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x103,
        (
            "#6P#0200Fですね、終わったらもう一度\x01",
            "ここに戻ってきましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 45270, 60, 2680, 152)
    OP_29(0x2D, 0x1, 0x4)
    EventEnd(0x5)
    Jump("loc_3184")

    label("loc_3176")

    TurnDirection(0x101, 0x102, 400)
    Sleep(300)
    Call(0, 12)
    Return()

    label("loc_3184")

    Return()

    # Function_11_298F end

    def Function_12_3185(): pass

    label("Function_12_3185")


    #C0146
    ChrTalk(
        0x101,
        (
            "#12P#0003F……そうだな。\x01",
            "さっき議員たちが\x01",
            "話していた内容からすると……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【昨日のうち】\x01",        # 0
            "【今日の午前中】\x01",      # 1
            "【ついさっき】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32BA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0147
    ChrTalk(
        0x102,
        (
            "#11P#0103F朝食にはいたけれど\x01",
            "お昼過ぎにはいなかった……\x02\x03",

            "#0101F今日の午前中で\x01",
            "間違い無さそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3400")

    label("loc_32BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3367")

    #C0148
    ChrTalk(
        0x102,
        (
            "#11P#0105Fあら、今朝の朝食には\x01",
            "顔を出していたそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#12P#0006F間違えた……\x01",
            "お昼過ぎに気付いたらしいし、\x01",
            "今日の午前中ってことになるな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3400")

    label("loc_3367")


    #C0150
    ChrTalk(
        0x102,
        (
            "#11P#0105Fあら、議員たちは\x01",
            "お昼過ぎに気付いたらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#12P#0006F間違えた……\x01",
            "今朝の朝食にはいたそうだし、\x01",
            "今日の午前中ってことになるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3400")


    #C0152
    ChrTalk(
        0x103,
        "#6P#0200Fまだ追いつけそうですね。\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x104,
        (
            "#5P#0301F問題はどこへ行ったかだぜ。\x02\x03",

            "#0303F家出娘の交友関係を\x01",
            "当たってみるか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    #C0154
    ChrTalk(
        0x101,
        (
            "#12P#0003Fいや、時間が掛かりすぎる。\x02\x03",

            "#0001Fそれに状況を考えると\x01",
            "もっと確実に、立ち寄りそうな場所が\x01",
            "あると思うんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0155
    ChrTalk(
        0x101,
        (
            "#12P#0000F突発的に思い立ち\x01",
            "今日の午前中に出たばかり。\x02\x03",

            "立ち寄りそうな場所は……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【大聖堂】\x01",      # 0
            "【市庁舎】\x01",      # 1
            "【ＩＢＣ】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_375C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0156
    ChrTalk(
        0x101,
        "#12P#0000FＩＢＣじゃないかな。\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#5P#0300Fなるほど……当座の家出資金を\x01",
            "確保しに行ったってわけか。\x02\x03",

            "ある意味\x01",
            "家出の常套ルートだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#11P#0100F突発的な家出なら\x01",
            "手持ちも乏しかったでしょうし。\x01",
            "十分可能性はあるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        (
            "#6P#0200FではＩＢＣに行ってみましょう。\x01",
            "まだそこに居るかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#12P#0000Fああ、なるべく急ごう！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A3E")

    label("loc_375C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3804")

    #C0161
    ChrTalk(
        0x101,
        (
            "#12P#0000F大聖堂、かな？\x02\x03",

            "信仰に篤い人なら\x01",
            "ありうると思うんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        (
            "#11P#0108Fそうね……カーラさんは特に\x01",
            "信仰に篤くはなかったと思うけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_389E")

    label("loc_3804")


    #C0163
    ChrTalk(
        0x101,
        (
            "#12P#0000F市庁舎、かな？\x02\x03",

            "思い切って引越し届けを\x01",
            "出してしまったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x102,
        (
            "#11P#0108Fそうね……飛び出したカーラさんが\x01",
            "そこまで冷静になれるかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389E")

    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    #C0165
    ChrTalk(
        0x103,
        (
            "#6P#0203F突発的な家出、ということは。\x02\x03",

            "#0200F手持ちのミラが乏しかった\x01",
            "可能性が高いですよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_3953():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3953)

    def lambda_3960():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3960)

    def lambda_396D():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_396D)
    Sleep(300)

    #C0166
    ChrTalk(
        0x101,
        (
            "#12P#0005Fそうか、ＩＢＣに\x01",
            "家出資金を下ろしに行った……！\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x104,
        (
            "#5P#0303F考えてみりゃあ\x01",
            "家出の常套ルートだな。\x02\x03",

            "#0300Fよし、ＩＢＣに行ってみようぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x102,
        (
            "#11P#0100Fええ、なるべく\x01",
            "急ぎましょう！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A56")
    OP_2C(0x2D, 0x2)

    label("loc_3A56")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 45270, 60, 2680, 152)
    OP_29(0x2D, 0x1, 0x5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_3185 end

    def Function_13_3A7E(): pass

    label("Function_13_3A7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CDF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BD7")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『もういいです、\x01",
            "　お父様だけ好きにやればいいのですわ。\x01",
            "　私は私で好きにやらせてもらいます！\x01",
            "  　　　　　　　　　　　　カーラ　　』\x02",
        )
    )

    CloseMessageWindow()

    #A0170
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『ＰＳ：メイドも連れて行きますから。\x01",
            "  食事の支度ができずに\x01",
            "  困ればいいのですわ！』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_3CDE")

    label("loc_3BD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_3CDB")
    EventBegin(0x0)
    Fade(800)
    OP_68(44280, 1560, 2580, 0)
    MoveCamera(56, 25, 0, 0)
    OP_6E(390, 0)
    SetCameraDistance(21530, 0)
    SetChrPos(0x101, 44280, 60, 2500, 0)
    SetChrPos(0x102, 45340, 60, 3250, 270)
    SetChrPos(0x103, 43820, 60, 3620, 90)
    SetChrPos(0x104, 44820, 60, 4220, 180)
    OP_0D()

    #C0171
    ChrTalk(
        0x102,
        (
            "#11P#0108Fカーラさん、\x01",
            "家出してしまったのは\x01",
            "いつ頃なのかしら。\x02\x03",

            "#0103Fまだ遠くへ行っていないと\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_3CDE")

    label("loc_3CDB")

    Call(0, 11)

    label("loc_3CDE")

    Return()

    label("loc_3CDF")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0172
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『もういいです、\x01",
            "　お父様だけ好きにやればいいのですわ。\x01",
            "　私は私で好きにやらせてもらいます！\x01",
            "  　　　　　　　　　　　　カーラ　　』\x02",
        )
    )

    CloseMessageWindow()

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『ＰＳ：メイドも連れて行きますから。\x01",
            "  食事の支度ができずに\x01",
            "  困ればいいのですわ！』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_13_3A7E end

    SaveToFile()

Try(main)
