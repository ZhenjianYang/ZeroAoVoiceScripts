from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t117b.bin",                # FileName
        "t117b",                    # MapName
        "t117b",                    # Location
        0x004A,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 74, 0, 1, 0, 2],
    )

    BuildStringList((
        "t117b",                  # 0
        "招待客",                 # 1
        "招待客",                 # 2
        "招待客",                 # 3
        "エヴェリン夫人",         # 4
        "ジェイムズ",             # 5
        "案内人",                 # 6
        "マフィアその１",         # 7
        "マフィアその２",         # 8
        "bt113b",                 # 9
    ))

    ATBonus("ATBonus_1FC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_2DC", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2FC", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt113b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31002.dat", "ms31102.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2DC", "MonsterBattlePostion_2BC", "ed7509", "ed7000", "ATBonus_1FC"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch22000.itc",                   # 00
        "chr/ch33002.itc",                   # 01
        "chr/ch26902.itc",                   # 02
        "chr/ch33302.itc",                   # 03
        "chr/ch27802.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
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
        "chr/ch31051.itc",                   # 1C
        "chr/ch31151.itc",                   # 1D
    ))

    DeclNpc(-310,    0,       -71709,  180,  385,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(44860,   150,     -13789,  270,  469,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(40840,   150,     -13789,  90,   469,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(44860,   150,     26239,   270,  469,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(40840,   150,     26290,   90,   469,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   28,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   29,  0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_36C",          # 00, 0
        "Function_1_424",          # 01, 1
        "Function_2_4AB",          # 02, 2
        "Function_3_502",          # 03, 3
        "Function_4_5CA",          # 04, 4
        "Function_5_7BB",          # 05, 5
        "Function_6_7F7",          # 06, 6
        "Function_7_AD9",          # 07, 7
        "Function_8_D35",          # 08, 8
        "Function_9_1DD4",         # 09, 9
        "Function_10_3179",        # 0A, 10
    ))


    def Function_0_36C(): pass

    label("Function_0_36C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3AC"),
        (1, "loc_3B8"),
        (2, "loc_3C4"),
        (3, "loc_3D0"),
        (4, "loc_3DC"),
        (5, "loc_3E8"),
        (6, "loc_3F4"),
        (SWITCH_DEFAULT, "loc_400"),
    )


    label("loc_3AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_400")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_40C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_423")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_423")

    Return()

    # Function_0_36C end

    def Function_1_424(): pass

    label("Function_1_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_45E")
    ClearScenarioFlags(0x5C, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_441")
    Event(0, 8)
    Jump("loc_45E")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_452")
    Event(0, 9)
    Jump("loc_45E")

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_45E")
    Event(0, 9)

    label("loc_45E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_46C")
    Jump("loc_4AA")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_47A")
    Jump("loc_4AA")

    label("loc_47A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_492")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4AA")

    label("loc_492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4AA")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_4AA")

    Return()

    # Function_1_424 end

    def Function_2_4AB(): pass

    label("Function_2_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4B4")

    label("loc_4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4C2")
    Jump("loc_501")

    label("loc_4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_501")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_501")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_501")
    Event(0, 10)

    label("loc_501")

    Return()

    # Function_2_4AB end

    def Function_3_502(): pass

    label("Function_3_502")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "今回招待された客層……\x01",
            "名前は伏せられてはいるが\x01",
            "帝国や共和国の要人ばかりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "政治家や貴族といった連中は\x01",
            "裏表の顔を使い分けるのが\x01",
            "本当に上手いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "……僕も含めて、ね。\x01",
            "ふふふ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_502 end

    def Function_4_5CA(): pass

    label("Function_4_5CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_727")

    #C0004
    ChrTalk(
        0xFE,
        (
            "この競売会は各国の要人と\x01",
            "コネクションを結ぶ\x01",
            "絶好の機会じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "ふふふ……娘よ。\x01",
            "ついでにいい婿を\x01",
            "見つけてきてはどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xA,
        (
            "オホホ……お父様ったら。\x01",
            "それではまるで政略結婚だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xA,
        (
            "お父様が婿養子として\x01",
            "お母様の家に入ってきた理由も\x01",
            "実のところはそういうことかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "がっはっはっは。\x01",
            "これは一本とられてしまったな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7B7")

    label("loc_727")


    #C0009
    ChrTalk(
        0xFE,
        (
            "ふふふ……\x01",
            "実際、結婚ほど強力な\x01",
            "結びつきは無いからのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "あわよくば……と思ったが\x01",
            "さすがに分別のできる歳であったか。\x01",
            "がっはっはっは。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B7")

    TalkEnd(0xFE)
    Return()

    # Function_4_5CA end

    def Function_5_7BB(): pass

    label("Function_5_7BB")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xFE,
        (
            "オホホ……お父様ったら\x01",
            "冗談がお上手なんだから。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_7BB end

    def Function_6_7F7(): pass

    label("Function_6_7F7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_88B")
    Jump("loc_8D5")

    label("loc_88B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8AB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D5")

    label("loc_8AB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D5")

    label("loc_8CB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A36")

    #C0012
    ChrTalk(
        0xFE,
        (
            "もう夫とは金輪際、縁を切ってしまおう……\x01",
            "そう考えていた私に、\x01",
            "ワジ君が言ってくれましたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "『旦那さんを許せないのは\x01",
            "  彼を本当に愛しているからさ。』って……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "私、大事なことを忘れていましたわ。\x01",
            "ワジ君には感謝しないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "夫も反省していることですし\x01",
            "今回だけは許そうと思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 2)
    SetScenarioFlags(0x0, 1)
    Jump("loc_AD1")

    label("loc_A36")

    SetChrSubChip(0xB, 0x0)

    #C0016
    ChrTalk(
        0xFE,
        (
            "ワジ君にはとても感謝していますわ。\x01",
            "結果的に夫婦の仲を\x01",
            "取り持ってくれたのですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "……さ、あなた行きましょう。\x01",
            "そろそろ競売が始まりますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_7F7 end

    def Function_7_AD9(): pass

    label("Function_7_AD9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B6D")
    Jump("loc_BB7")

    label("loc_B6D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B8D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BB7")

    label("loc_B8D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BAD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BB7")

    label("loc_BAD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BB7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD0")

    #C0018
    ChrTalk(
        0xFE,
        (
            "エヴェリンがあんなに\x01",
            "怒っているのを見たのは初めてだよ。\x01",
            "……正直、怖かった。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "普段の彼女は大人しいから\x01",
            "それにつけ上がって\x01",
            "女遊びなどをしてしまったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "実際はこんな激しい性格だったんだな。\x01",
            "知らなかったよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 2)
    SetScenarioFlags(0x0, 2)
    Jump("loc_D2D")

    label("loc_CD0")


    #C0021
    ChrTalk(
        0xFE,
        (
            "ともあれ、なんとかエヴェリンと\x01",
            "和解できてよかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "……もう女遊びはこりごりだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_D2D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_AD9 end

    def Function_8_D35(): pass

    label("Function_8_D35")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(47070, 2000, -52070, 0)
    MoveCamera(48, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18250, 0)
    SetChrPos(0x101, 46200, 0, -52600, 90)
    SetChrPos(0x102, 46200, 0, -51400, 90)
    SetChrPos(0x138, 48700, 0, -52000, 270)
    FadeToBright(1000, 0)
    OP_68(47070, 1200, -52070, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0023
    ChrTalk(
        0x138,
        (
            "#2904F#11Pフフ、なるほど。\x01",
            "そういう事情でしたの。\x02\x03",

            "#2902Fなかなか大胆な事をしてますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#5106F#6P……ええ、まあ。\x02\x03",

            "#5108F実際には見ているだけですから\x01",
            "ただの自己満足かもしれませんけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x138,
        (
            "#2902F#11Pフフ、でも気に入りましたわ。\x02\x03",

            "#2909Fエリィの同僚なら\x01",
            "そのくらいの思い切りがないと\x01",
            "相応#4Rふさわ#しくありませんものね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0026
    ChrTalk(
        0x102,
        (
            "#5313F#6Pも、もう、何を言ってるのよ。\x02\x03",

            "#5301F……それにしても。\x01",
            "ベル、どうしてこんな所に？\x02\x03",

            "さっきの話を聞く限り\x01",
            "来るのは初めてみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x138,
        (
            "#2902F#11Pハルトマン議長からは\x01",
            "毎年熱心に誘われていますの。\x02\x03",

            "#2903Fただまあ、怪しい方々との\x01",
            "付き合いがある人でしょう？\x02\x03",

            "お父様は色々と理由をつけて\x01",
            "断っているんですけど……\x02\x03",

            "#2901Fわたくしの方は\x01",
            "中々そうもいかなくって。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#5306F#6Pなるほど……\x01",
            "確かにそうかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0029
    ChrTalk(
        0x101,
        "#5105F#6P何か事情があるんですか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0030
    ChrTalk(
        0x102,
        (
            "#5300F#5P前にも言ったけど\x01",
            "彼女はＩＢＣの事業の幾つかを\x01",
            "おじさまから任されているのよ。\x02\x03",

            "このミシュラムの開発計画も\x01",
            "担当しているそうだから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x101,
        "#5111F#6Pええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x138,
        (
            "#2902F#11Pふふ、と言っても\x01",
            "ホテルとテーマパークの運営に\x01",
            "関わっているだけですけど。\x02\x03",

            "#2906Fただ、その関係でどうしても\x01",
            "昔から住んでいる議長のお誘いは\x01",
            "なかなか無下にできなくって。\x02\x03",

            "#2900F今年はこうして\x01",
            "出席することにしたわけですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#5101F#6Pな、なるほど……\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x190)
    Sleep(300)

    #C0034
    ChrTalk(
        0x102,
        "#5311F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x138,
        (
            "#2905F#11Pあら、エリィ？\x02\x03",

            "何か言いたいことが\x01",
            "ありそうな顔ですわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#5303F#6P……まあ、ね。\x02\x03",

            "#5300Fベルって自分が気に入らない事は\x01",
            "絶対にやらないタイプでしょう？\x02\x03",

            "なのに、事情があるからといって\x01",
            "わざわざ足を運んだりして……\x02\x03",

            "何か他に狙いがあるのではないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x138,
        (
            "#2904F#11Pふふっ……流石はエリィ。\x02\x03",

            "#2902F──実は、今回の出品物に\x01",
            "面白い品があるそうなんですの。\x02\x03",

            "それに興味があったので\x01",
            "出席することにしたのですわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x101,
        "#5105F#6Pそれって……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#5301F#6Pどういう品なの？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x138,
        (
            "#2904F#11Pローゼンベルク工房製の\x01",
            "初期のアンティークドール……\x02\x03",

            "#2902F好事家の間で破格の値段が付いた\x01",
            "幻の作品という触れ込みですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#5105F#6Pアンティークドール……\x01",
            "あの人形工房のですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#5301F#6P……やっぱりそれも\x01",
            "曰#2Rいわ#くつきの作品なのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x138,
        (
            "#2904F#11P盗品か、どこぞの資産家が\x01",
            "後ろ暗い理由で手放したものか……\x02\x03",

            "#2902F詳細は分かりませんけど\x01",
            "噂では素晴らしい逸品らしくて。\x02\x03",

            "コレクターの一人として\x01",
            "これは見逃せないないでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#5306F#6Pなるほど、あなた昔から\x01",
            "あそこの人形のファンだものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#5101F#6P……ちなみに、そういう人形、\x01",
            "幾らくらいの値が付くんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x138,
        (
            "#2905F#11Pそうですわね……\x02\x03",

            "#2906F初期の作品は、最近のものより\x01",
            "一回り以上大きかったらしくて\x01",
            "ほとんど出回っていませんの。\x02\x03",

            "マイスターもそのサイズは\x01",
            "もう作るつもりがないそうで\x01",
            "必然的にプレミアがついて……\x02\x03",

            "#2900F以前、帝都で開かれた競売会では\x01",
            "５００万ミラで落札された作品も\x01",
            "あったそうですわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0047
    ChrTalk(
        0x101,
        "#5111F#6Pに、人形一体にそんな値が！？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#5309F#6Pまあ、熱心なファンがいる\x01",
            "芸術品みたいなものだから……\x02\x03",

            "#5300Fしかしその様子だと\x01",
            "手に入れる気満々みたいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x138,
        (
            "#2904F#11Pフフ、由来がどうあれ、\x01",
            "人形には罪はありませんから。\x02\x03",

            "#2902Fもちろん、盗品であった場合は\x01",
            "しかるべき対応をいたしますわ。\x02\x03",

            "#2909Fその上で、前の所有者と交渉して\x01",
            "正式に手に入れるつもりですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#5106F#6P……参りました。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        "#5306F#6Pふう、敵わないわね。\x02",
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x138,
        "#2905F#11Pあら……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, 38000, 0, -52000, 0)
    OP_68(45720, 1200, -52070, 1500)

    def lambda_1ADD():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1ADD)
    Sleep(50)

    def lambda_1AED():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1AED)
    OP_6F(0x1)

    #N0053
    NpcTalk(
        0xD,
        "案内人の声",
        "#2S失礼します、マリアベル様。\x02",
    )

    CloseMessageWindow()

    #N0054
    NpcTalk(
        0xD,
        "案内人の声",
        (
            "#2Sオークションの開催時刻が\x01",
            "そろそろ近づいて参りましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x138,
        (
            "#2904F#11Pそう、ありがとう。\x02\x03",

            "#2900Fすぐに参りますから\x01",
            "後ろの方に３人分の席を\x01",
            "用意してもらえるかしら？\x02",
        )
    )

    CloseMessageWindow()

    #N0056
    NpcTalk(
        0xD,
        "案内人の声",
        (
            "#2S──かしこまりました。\x01",
            "それでは手配しておきます。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(47070, 1200, -52070, 1200)

    def lambda_1C39():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C39)
    Sleep(50)

    def lambda_1C49():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C49)
    OP_6F(0x1)

    #C0057
    ChrTalk(
        0x102,
        "#5308F#6Pえっと、ベル……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x138,
        (
            "#2902F#11Pふふっ、心配いりませんわ。\x02\x03",

            "わたくしが議長と挨拶するのは\x01",
            "オークションが終わった後ですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        (
            "#5306F#6Pう、うーん……\x02\x03",

            "#5300F構わないかしら、ロイド？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#5104F#6Pああ、せっかくだから\x01",
            "一緒に出席させてもらおう。\x02\x03",

            "#5100Fマリアベルさん。\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x138,
        "#2909F#11Pええ、こちらこそ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 44770, 0, -52070, 270)
    SetScenarioFlags(0xA6, 1)
    OP_29(0x47, 0x1, 0xB)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_8_D35 end

    def Function_9_1DD4(): pass

    label("Function_9_1DD4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(47070, 2000, -52070, 0)
    MoveCamera(48, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18250, 0)
    SetChrPos(0x101, 46200, 0, -52600, 90)
    SetChrPos(0xEF, 46200, 0, -51400, 90)
    SetChrPos(0x138, 48700, 0, -52000, 270)
    FadeToBright(1000, 0)
    OP_68(47070, 1200, -52070, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0062
    ChrTalk(
        0x138,
        (
            "#2904F#11Pフフ、なるほど。\x01",
            "そういう事情でしたの。\x02\x03",

            "#2902Fなかなか大胆な事をしてますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#5106F#6P……ええ、まあ。\x02\x03",

            "#5108F実際には見ているだけですから\x01",
            "ただの自己満足かもしれませんけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x138,
        (
            "#2902F#11Pフフ、でも気に入りましたわ。\x02\x03",

            "#2909Fエリィの同僚なら\x01",
            "そのくらいの思い切りがないと\x01",
            "相応#4Rふさわ#しくありませんものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#5112F#6Pそ、そういうもんですか……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2018")

    #C0066
    ChrTalk(
        0x103,
        (
            "#5402F#6Pよっぽどエリィさんが\x01",
            "大事みたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_205D")

    label("loc_2018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_205D")

    #C0067
    ChrTalk(
        0x104,
        (
            "#5602F#6Pはは、よっぽどお嬢のことが\x01",
            "大事みたいッスね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_205D")


    #C0068
    ChrTalk(
        0x138,
        (
            "#2904F#11Pええ、愛していると言っても\x01",
            "過言ではありませんわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0069
    ChrTalk(
        0x101,
        "#5111F#6Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x138,
        (
            "#2902F#11Pだってあの子、可愛いでしょう？\x02\x03",

            "まっすぐで意志が強くて\x01",
            "とても凛としているけれど\x01",
            "落ち着いた気品と優しさがあって。\x02\x03",

            "#2909Fわたくしの自慢の友人ですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#5100F#6P確かに……\x02\x03",

            "#5104F俺たちにとっても\x01",
            "自慢の同僚ですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2223")

    #C0072
    ChrTalk(
        0x103,
        (
            "#5404F#6Pふふ、本人が聞いたら\x01",
            "真っ赤になりそうですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_226A")

    label("loc_2223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_226A")

    #C0073
    ChrTalk(
        0x104,
        (
            "#5609F#6Pはは、本人が聞いたら\x01",
            "真っ赤になりそうだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_226A")


    #C0074
    ChrTalk(
        0x138,
        (
            "#2906F#11Pただまあ、エリィとここで\x01",
            "会えなかったのは残念ですわね。\x02\x03",

            "#2900F一緒にオークションでも\x01",
            "鑑賞しようと思ったのですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#5101F#6Pそういえば……\x01",
            "どういう事情でこんな所に？\x02\x03",

            "先ほどの話を聞く限り\x01",
            "来るのは初めてみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x138,
        (
            "#2902F#11Pハルトマン議長からは\x01",
            "毎年熱心に誘われていますの。\x02\x03",

            "#2903Fただまあ、怪しい方々との\x01",
            "付き合いがある人でしょう？\x02\x03",

            "お父様は色々と理由をつけて\x01",
            "断っているんですけど……\x02\x03",

            "#2901Fわたくしの方は\x01",
            "中々そうもいかなくって。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_246C")

    #C0077
    ChrTalk(
        0x103,
        "#5400F#6P……何か事情でも？\x02",
    )

    CloseMessageWindow()
    Jump("loc_249A")

    label("loc_246C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_249A")

    #C0078
    ChrTalk(
        0x104,
        "#5605F#6P何か事情があるんスか？\x02",
    )

    CloseMessageWindow()

    label("loc_249A")


    #C0079
    ChrTalk(
        0x138,
        (
            "#2904F#11Pミシュラムの開発計画は\x01",
            "わたくしが担当してますから。\x02\x03",

            "#2900Fその関係でどうしても\x01",
            "昔から住んでいる議長のお誘いは\x01",
            "なかなか無下にできなくって。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2594")

    #C0080
    ChrTalk(
        0x103,
        "#5401F#6Pえっ……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_25BA")

    label("loc_2594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_25BA")

    #C0081
    ChrTalk(
        0x104,
        "#5607F#6Pマジっすか！？\x02",
    )

    CloseMessageWindow()

    label("loc_25BA")


    #C0082
    ChrTalk(
        0x101,
        (
            "#5111F#6Pそ、そういえば……\x01",
            "前にＩＢＣの事業の幾つかを\x01",
            "任されていると聞きましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x138,
        (
            "#2904F#11Pふふ、と言っても\x01",
            "ホテルとテーマパークの運営に\x01",
            "関わっているだけですわ。\x02\x03",

            "#2902F──それと、今年の競売会は\x01",
            "面白い出品物があるらしくて。\x02\x03",

            "それに興味があったので\x01",
            "出席することにしたんですの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0084
    ChrTalk(
        0x101,
        "#5101F#6Pそれって……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2756")

    #C0085
    ChrTalk(
        0x103,
        "#5401F#6Pどういう品ですか……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2786")

    label("loc_2756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2786")

    #C0086
    ChrTalk(
        0x104,
        "#5602F#6P……どういう品なんスか？\x02",
    )

    CloseMessageWindow()

    label("loc_2786")


    #C0087
    ChrTalk(
        0x138,
        (
            "#2904F#11Pローゼンベルク工房製の\x01",
            "初期のアンティークドール……\x02\x03",

            "#2902F好事家の間で破格の値段が付いた\x01",
            "幻の作品という触れ込みですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#5105F#6Pアンティークドール……\x01",
            "あの人形工房のですか。\x02\x03",

            "#5101F……やっぱりそれも\x01",
            "曰くつきの作品なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x138,
        (
            "#2904F#11P盗品か、どこぞの資産家が\x01",
            "後ろ暗い理由で手放したものか……\x02\x03",

            "詳細は分かりませんけど\x01",
            "噂では素晴らしい逸品らしくて。\x02\x03",

            "#2902Fコレクターの一人として\x01",
            "これは見逃せないないでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#5112F#6Pな、なるほど……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_29B7")

    #C0091
    ChrTalk(
        0x103,
        (
            "#5400F#6Pちなみに、そういう人形……\x01",
            "幾らくらいの値が付くんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A0A")

    label("loc_29B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2A0A")

    #C0092
    ChrTalk(
        0x104,
        (
            "#5609F#6Pちなみに、そういう人形って\x01",
            "幾らくらいの値が付くんですかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A0A")


    #C0093
    ChrTalk(
        0x138,
        (
            "#2905F#11Pそうですわね……\x02\x03",

            "#2906F初期の作品は、最近のものより\x01",
            "一回り以上大きかったらしくて\x01",
            "ほとんど出回っていませんの。\x02\x03",

            "マイスターもそのサイズは\x01",
            "もう作るつもりがないそうで\x01",
            "必然的にプレミアがついて……\x02\x03",

            "#2900F以前、帝都で開かれた競売会では\x01",
            "５００万ミラで落札された作品も\x01",
            "あったそうですわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0094
    ChrTalk(
        0x101,
        "#5111F#6Pに、人形一体にそんな値が！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2C1C")

    #C0095
    ChrTalk(
        0x103,
        (
            "#5406F#6Pメインクラスの導力演算器が\x01",
            "買えそうな値段ですね……\x02\x03",

            "#5400Fもしかして、その人形を\x01",
            "落札するつもりですか……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C9A")

    label("loc_2C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2C9A")

    #C0096
    ChrTalk(
        0x104,
        (
            "#5606F#6P旧式の戦車だったら\x01",
            "買えちまいそうな値段だな……\x02\x03",

            "#5605Fもしかして、その人形\x01",
            "競り落とすつもりなんスか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C9A")


    #C0097
    ChrTalk(
        0x138,
        (
            "#2904F#11Pフフ、由来がどうあれ、\x01",
            "人形には罪はありませんから。\x02\x03",

            "#2902Fもちろん、盗品であった場合は\x01",
            "しかるべき対応をいたしますわ。\x02\x03",

            "#2909Fその上で、前の所有者と交渉して\x01",
            "正式に手に入れるつもりですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#5106F#6P……参りました。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2DB5")

    #C0099
    ChrTalk(
        0x103,
        "#5406F#6P太っ腹すぎです……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DDF")

    label("loc_2DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2DDF")

    #C0100
    ChrTalk(
        0x104,
        "#5606F#6P太っ腹すぎるぜ……\x02",
    )

    CloseMessageWindow()

    label("loc_2DDF")

    Sound(811, 0, 100, 0)
    Sleep(500)

    #C0101
    ChrTalk(
        0x138,
        "#2905F#11Pあら……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, 38000, 0, -52000, 0)
    OP_68(45720, 1200, -52070, 1200)

    def lambda_2E27():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E27)
    Sleep(50)

    def lambda_2E37():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2E37)
    OP_6F(0x1)

    #N0102
    NpcTalk(
        0xD,
        "案内人の声",
        "#2S失礼します、マリアベル様。\x02",
    )

    CloseMessageWindow()

    #N0103
    NpcTalk(
        0xD,
        "案内人の声",
        (
            "#2Sオークションの開催時刻が\x01",
            "そろそろ近づいて参りましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x138,
        (
            "#2909F#11Pそう、ありがとう。\x02\x03",

            "#2900Fすぐに参りますから\x01",
            "後ろの方に３人分の席を\x01",
            "用意してもらえるかしら？\x02",
        )
    )

    CloseMessageWindow()

    #N0105
    NpcTalk(
        0xD,
        "案内人の声",
        (
            "#2S──かしこまりました。\x01",
            "それでは手配しておきます。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(47070, 1200, -52070, 1200)

    def lambda_2F83():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F83)
    Sleep(50)

    def lambda_2F93():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2F93)
    OP_6F(0x1)

    #C0106
    ChrTalk(
        0x101,
        "#5108F#6Pその、マリアベルさん……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x138,
        (
            "#2902F#11Pふふっ、心配いりませんわ。\x02\x03",

            "わたくしが議長と挨拶するのは\x01",
            "オークションが終わった後ですし。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3073")

    #C0108
    ChrTalk(
        0x103,
        (
            "#5402F#6Pまあ、それなら\x01",
            "問題はなさそうですけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B2")

    label("loc_3073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_30B2")

    #C0109
    ChrTalk(
        0x104,
        (
            "#5600F#6Pま、そういう事なら\x01",
            "問題はなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B2")


    #C0110
    ChrTalk(
        0x101,
        (
            "#5103F#6P……分かりました。\x01",
            "せっかくなので\x01",
            "ご一緒させてもらいます。\x02\x03",

            "#5100Fマリアベルさん。\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x138,
        "#2909F#11Pええ、こちらこそ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 44770, 0, -52070, 270)
    SetScenarioFlags(0xA6, 1)
    OP_29(0x47, 0x1, 0xB)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_1DD4 end

    def Function_10_3179(): pass

    label("Function_10_3179")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31B6")
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    Jump("loc_31D7")

    label("loc_31B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31D1")
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    Jump("loc_31D7")

    label("loc_31D1")

    LoadChrToIndex("chr/ch00350.itc", 0x1F)

    label("loc_31D7")

    LoadChrToIndex("chr/ch00450.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0xEF, 0x1F)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0xEF, 0x0)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CD")
    OP_68(0, 1200, -11000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -11000, 0)
    SetChrPos(0xEF, -750, 0, -12500, 0)
    SetChrPos(0x105, 750, 0, -12250, 0)
    SetChrPos(0x133, 0, 0, -14000, 0)
    SetChrPos(0xE, 0, 0, -5000, 180)
    SetChrPos(0xF, -750, 0, -4250, 180)
    Jump("loc_3409")

    label("loc_32CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3375")
    OP_68(0, 1200, -19000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -19000, 0)
    SetChrPos(0xEF, -750, 0, -20500, 0)
    SetChrPos(0x105, 750, 0, -20250, 0)
    SetChrPos(0x133, 0, 0, -22000, 0)
    SetChrPos(0xE, 0, 0, -13000, 180)
    SetChrPos(0xF, -750, 0, -12250, 180)
    Jump("loc_3409")

    label("loc_3375")

    OP_68(0, 1200, -22000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -22000, 0)
    SetChrPos(0xEF, -750, 0, -23500, 0)
    SetChrPos(0x105, 750, 0, -23250, 0)
    SetChrPos(0x133, 0, 0, -25000, 0)
    SetChrPos(0xE, 0, 0, -16000, 180)
    SetChrPos(0xF, -750, 0, -15250, 180)

    label("loc_3409")


    def lambda_340E():
        OP_97(0xE, 0x0, 0x0, 0xFFFFEE6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_340E)
    Sleep(50)

    def lambda_342B():
        OP_97(0xF, 0x0, 0x0, 0xFFFFEE6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_342B)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0xE, 1)
    Battle("BattleInfo_2FC", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0xEF, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x133, 0x80)
    SetChrBattleFlags(0x133, 0x8000)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_351D")
    OP_68(0, 1200, -11000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -11000, 0)
    SetChrPos(0xEF, 0, 0, -11000, 0)
    SetChrPos(0x105, 0, 0, -11000, 0)
    Jump("loc_35F3")

    label("loc_351D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3592")
    OP_68(0, 1200, -19000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -19000, 0)
    SetChrPos(0xEF, 0, 0, -19000, 0)
    SetChrPos(0x105, 0, 0, -19000, 0)
    Jump("loc_35F3")

    label("loc_3592")

    OP_68(0, 1200, -23250, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -23250, 0)
    SetChrPos(0xEF, 0, 0, -23250, 0)
    SetChrPos(0x105, 0, 0, -23250, 0)

    label("loc_35F3")

    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_10_3179 end

    SaveToFile()

Try(main)
