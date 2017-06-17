from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t153b.bin",                # FileName
        "t153b",                    # MapName
        "t153b",                    # Location
        0x004F,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 79, 0, 1, 0, 2],
    )

    BuildStringList((
        "t153b",                  # 0
        "マフィア",               # 1
        "マフィア",               # 2
        "受付嬢セラ",             # 3
        "クラーク事務長",         # 4
        "診察医ダスター（未使用）",# 5
        "研修医リゼル（未使用）", # 6
        "研修医シャルール",       # 7
        "研修医フローラ",         # 8
        "bt154b",                 # 9
    ))

    ATBonus("ATBonus_220", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_300", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 5, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_310", 11, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_314", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_31C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_320", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt154b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31103.dat", "ms67101.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_300", "MonsterBattlePostion_2E0", "ed7402", "ed7403", "ATBonus_220"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50362.itc",                   # 00
        "apl/ch50363.itc",                   # 01
        "chr/ch28202.itc",                   # 02
        "chr/ch28000.itc",                   # 03
        "chr/ch29302.itc",                   # 04
        "chr/ch29400.itc",                   # 05
        "chr/ch32800.itc",                   # 06
        "chr/ch29502.itc",                   # 07
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(48319,   150,     52389,   90,   341,  0x0, 0,   2,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(53840,   0,       52029,   135,  261,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(50979,   150,     59069,   300,  469,  0x0, 0,   4,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(48700,   0,       59700,   90,   389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(48700,   0,       59700,   90,   261,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(59159,   400,     55750,   0,    341,  0x0, 0,   7,   0,   255, 255, 0,   9,   255,  0)

    DeclActor(58800,   0,       5460,    1200,    58800,   1500,    5460,    0x007C, 0,  14, 0x0000)

    ScpFunction((
        "Function_0_3A0",          # 00, 0
        "Function_1_458",          # 01, 1
        "Function_2_4AD",          # 02, 2
        "Function_3_4C5",          # 03, 3
        "Function_4_4F5",          # 04, 4
        "Function_5_67B",          # 05, 5
        "Function_6_7D3",          # 06, 6
        "Function_7_A2A",          # 07, 7
        "Function_8_B8C",          # 08, 8
        "Function_9_CF1",          # 09, 9
        "Function_10_ECC",         # 0A, 10
        "Function_11_12B7",        # 0B, 11
        "Function_12_15C3",        # 0C, 12
        "Function_13_163E",        # 0D, 13
        "Function_14_1BF2",        # 0E, 14
    ))


    def Function_0_3A0(): pass

    label("Function_0_3A0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3E0"),
        (1, "loc_3EC"),
        (2, "loc_3F8"),
        (3, "loc_404"),
        (4, "loc_410"),
        (5, "loc_41C"),
        (6, "loc_428"),
        (SWITCH_DEFAULT, "loc_434"),
    )


    label("loc_3E0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_440")

    label("loc_3EC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_440")

    label("loc_3F8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_440")

    label("loc_404")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_440")

    label("loc_410")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_440")

    label("loc_41C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_440")

    label("loc_428")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_440")

    label("loc_434")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_440")

    label("loc_440")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_457")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_440")

    label("loc_457")

    Return()

    # Function_0_3A0 end

    def Function_1_458(): pass

    label("Function_1_458")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_477")
    Event(0, 13)
    Jump("loc_4AC")

    label("loc_477")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_496")
    Event(0, 11)
    Jump("loc_4AC")

    label("loc_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AC")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_4AC")

    Return()

    # Function_1_458 end

    def Function_2_4AD(): pass

    label("Function_2_4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BE")
    Call(0, 12)

    label("loc_4BE")

    ClearMapObjFlags(0x0, 0x10)
    Return()

    # Function_2_4AD end

    def Function_3_4C5(): pass

    label("Function_3_4C5")

    TalkBegin(0xFE)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "マフィアは気を失っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_3_4C5 end

    def Function_4_4F5(): pass

    label("Function_4_4F5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_589")
    Jump("loc_5D3")

    label("loc_589")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D3")

    label("loc_5A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D3")

    label("loc_5C9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0002
    ChrTalk(
        0xFE,
        (
            "まだ上の階に、\x01",
            "病院職員や患者の皆さんが\x01",
            "大勢残っているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "どうか皆さんのことを\x01",
            "よろしくおねがいします……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_4F5 end

    def Function_5_67B(): pass

    label("Function_5_67B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B")

    #C0004
    ChrTalk(
        0xFE,
        (
            "以前の魔獣騒ぎで魔獣よけのフェンスも\x01",
            "つけたので安心しきっていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "ま、まさかマフィアが病院に\x01",
            "乗り込んでくるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "大陸中から支援を受けている以上、\x01",
            "下手をすると国際問題ですよ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7CF")

    label("loc_75B")


    #C0007
    ChrTalk(
        0xFE,
        (
            "マフィアはもう少し統率された組織だと\x01",
            "思っていたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "こんな状況……\x01",
            "下手をすると国際問題です……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CF")

    TalkEnd(0xFE)
    Return()

    # Function_5_67B end

    def Function_6_7D3(): pass

    label("Function_6_7D3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_867")
    Jump("loc_8B1")

    label("loc_867")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_887")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B1")

    label("loc_887")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B1")

    label("loc_8A7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A3")

    #C0009
    ChrTalk(
        0xFE,
        (
            "そ、そうだ。\x01",
            "今日は夕方から患者の診察が\x01",
            "入っていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "この騒ぎでは発作が起きていても\x01",
            "おかしくはない……\x01",
            "どうすれば……っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "と、とにかく私たち医師が\x01",
            "落ち着かなければな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A22")

    label("loc_9A3")


    #C0012
    ChrTalk(
        0xFE,
        (
            "そういえば今日は\x01",
            "夕方に軽い発作のある患者を\x01",
            "診察する予定だったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "うぅむ……発作が\x01",
            "酷くなっていなければいいが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A22")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_7D3 end

    def Function_7_A2A(): pass

    label("Function_7_A2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEB")

    #C0014
    ChrTalk(
        0xFE,
        (
            "この異常事態ですが、\x01",
            "僕は意外と平静でいられています。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "冷静沈着なベルダイン先生のもとで\x01",
            "勉強してきたおかげかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "……先生も無事だといいですが……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B88")

    label("loc_AEB")


    #C0017
    ChrTalk(
        0xFE,
        (
            "……時間が時間ですから、\x01",
            "外来の患者が巻き込まれた可能性は……\x01",
            "確かに高いかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "……銃声も聞こえましたし、\x01",
            "宿泊施設のほうも心配ですね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B88")

    TalkEnd(0xFE)
    Return()

    # Function_7_A2A end

    def Function_8_B8C(): pass

    label("Function_8_B8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C72")

    #C0019
    ChrTalk(
        0xFE,
        (
            "最新医療技術の集結する\x01",
            "ウルスラ病院を襲うなんて、\x01",
            "愚かな連中だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "しかも彼ら……\x01",
            "あろうことか病院内に\x01",
            "武器なんて持ち込んでいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "まだ試験途中の機器を壊されでもしたら\x01",
            "医療の未来に大きな損失だよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_CED")

    label("loc_C72")


    #C0022
    ChrTalk(
        0xFE,
        (
            "まったく、彼らの狙いが\x01",
            "さっぱり分からない……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "とにかく、\x01",
            "病院内の機器が壊されないように\x01",
            "女神様に祈らなければ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CED")

    TalkEnd(0xFE)
    Return()

    # Function_8_B8C end

    def Function_9_CF1(): pass

    label("Function_9_CF1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D85")
    Jump("loc_DCF")

    label("loc_D85")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DA5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCF")

    label("loc_DA5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCF")

    label("loc_DC5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DCF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E73")
    SetChrSubChip(0xFE, 0x0)

    #C0024
    ChrTalk(
        0xFE,
        "……ダメ、落ち着きなさいフローラ。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "こ、これくらいで動じてちゃ、\x01",
            "医者になんかなれっこないわ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_EC4")

    label("loc_E73")


    #C0026
    ChrTalk(
        0xFE,
        "……気持ちを落ち着けたいの。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "ごめん、悪いけど……\x01",
            "放っておいてくれる？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_CF1 end

    def Function_10_ECC(): pass

    label("Function_10_ECC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(17480, 600, -4610, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22180, 0)
    SetChrPos(0x101, -600, 0, 600, 90)
    SetChrPos(0x102, -600, 0, -600, 90)
    SetChrPos(0x103, -1900, 0, -600, 90)
    SetChrPos(0x104, -1900, 0, 600, 90)
    SetChrPos(0x106, -3200, 0, 0, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(12880, 600, 6580, 7000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(4870, 2400, -280, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19020, 0)
    OP_68(4870, 900, -280, 3000)
    Sleep(1000)

    def lambda_1005():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1005)
    Sleep(50)

    def lambda_101D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_101D)
    Sleep(50)

    def lambda_1035():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1035)
    Sleep(50)

    def lambda_104D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_104D)
    Sleep(50)

    def lambda_1065():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1065)
    Sleep(200)

    def lambda_107D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_107D)
    Sleep(50)

    def lambda_1091():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1091)
    Sleep(500)

    def lambda_10A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10A5)
    Sleep(50)

    def lambda_10B9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10B9)
    Sleep(500)

    def lambda_10CD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_10CD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_6F(0x1)
    OP_0D()

    #C0028
    ChrTalk(
        0x101,
        "#0001F#5P人気#4Rひとけ#は無し、か……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#0108F#6P……マフィアの姿も無いわね。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6Pいや、建物のあちこちから\x01",
            "気の巡りが伝わってくる……\x02\x03",

            "おそらく病院関係者は\x01",
            "各所に避難しているのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        (
            "#0203F#6Pええ、かなりの人数が\x01",
            "残っている気配がします。\x02\x03",

            "#0201Fマフィアの人たちの気配も……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#0301F#5Pなるほど……\x01",
            "ここからが本番って訳かよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#0013F#5Pよし……\x01",
            "慎重に回って行こう！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 3190, 0, -210, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE1, 4)
    EventEnd(0x5)
    Return()

    # Function_10_ECC end

    def Function_11_12B7(): pass

    label("Function_11_12B7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("chr/ch31000.itc", 0x23)
    LoadChrToIndex("chr/ch31050.itc", 0x24)
    LoadChrToIndex("chr/ch31051.itc", 0x25)
    LoadChrToIndex("chr/ch31100.itc", 0x26)
    LoadChrToIndex("chr/ch31150.itc", 0x27)
    LoadChrToIndex("chr/ch31151.itc", 0x28)
    OP_68(47500, 1000, 0, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 47400, 0, 600, 90)
    SetChrPos(0x102, 47400, 0, -600, 90)
    SetChrPos(0x103, 46100, 0, -600, 90)
    SetChrPos(0x104, 46100, 0, 600, 90)
    SetChrPos(0x106, 44800, 0, 0, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, 55000, 0, 580, 270)
    SetChrPos(0x9, 54750, 0, -800, 270)
    FadeToBright(1000, 0)
    OP_68(49500, 1000, 0, 1200)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x102,
        "#0105F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#0013F#6P待ち伏せか……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(48500, 1000, 0, 1000)
    SetCameraDistance(17500, 1000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)

    def lambda_14DC():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14DC)

    def lambda_14F1():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_14F1)
    Sleep(300)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sleep(100)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(500)
    Battle("BattleInfo_320", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Call(0, 12)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    SetChrPos(0x0, 51690, 0, -10, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE1, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_12B7 end

    def Function_12_15C3(): pass

    label("Function_12_15C3")

    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x8, 54860, 0, 580, 315)
    SetChrPos(0x9, 55500, 0, -1070, 225)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_12_15C3 end

    def Function_13_163E(): pass

    label("Function_13_163E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28200.itc", 0x1E)
    LoadChrToIndex("chr/ch29300.itc", 0x1F)
    LoadChrToIndex("chr/ch29500.itc", 0x20)
    OP_68(54490, 1000, 57780, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 49490, 0, 49500, 0)
    SetChrPos(0x102, 50490, 0, 49500, 0)
    SetChrPos(0x103, 49490, 0, 48300, 0)
    SetChrPos(0x104, 50490, 0, 48300, 0)
    SetChrPos(0x106, 49990, 0, 47100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xA, 54390, 0, 55860, 180)
    SetChrPos(0xE, 54520, 0, 54400, 0)
    SetChrPos(0xF, 58520, 0, 57440, 90)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xF, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(51800, 1000, 55090, 3000)
    Sleep(500)

    def lambda_179A():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_179A)
    Sleep(50)

    def lambda_17B2():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17B2)
    Sleep(50)

    def lambda_17CA():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_17CA)
    Sleep(50)

    def lambda_17E2():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17E2)
    Sleep(50)

    def lambda_17FA():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_17FA)
    Sleep(200)

    def lambda_1812():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1812)
    Sleep(50)

    def lambda_1826():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1826)
    Sleep(500)

    def lambda_183A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_183A)
    Sleep(50)

    def lambda_184E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_184E)
    Sleep(500)

    def lambda_1862():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1862)
    WaitChrThread(0x101, 1)

    def lambda_1877():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1877)
    WaitChrThread(0x102, 1)

    def lambda_1888():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1888)
    WaitChrThread(0x103, 1)

    def lambda_1899():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1899)
    WaitChrThread(0x104, 1)

    def lambda_18AA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18AA)
    WaitChrThread(0x106, 1)

    def lambda_18BB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_18BB)
    EndChrThread(0xA, 0xFF)
    SetChrSubChip(0xA, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)
    EndChrThread(0xF, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_194C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_194C)
    Sleep(50)

    def lambda_195C():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_195C)
    Sleep(50)

    def lambda_196C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_196C)
    Sleep(50)

    def lambda_197C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_197C)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)

    #C0036
    ChrTalk(
        0xA,
        "#5Pロイドさん……！？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#0002F#6Pセラさん……\x01",
            "よかった、ご無事でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        "#11Pみ、皆さんは警察の……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xE,
        (
            "#5Pひょ、ひょっとして\x01",
            "助けに来てくれたのかい！？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#0300F#6Pああ、侵入者を制圧しながら\x01",
            "全員の安全を確認してる所だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#0201F#6P#N危険なので、しばらく\x01",
            "こちらで待っていてください。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0042
    ChrTalk(
        0xA,
        "#5Pわ、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xA,
        (
            "#5P上の階には他のスタッフと\x01",
            "入院患者もいると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xE,
        "#5Pか、彼らの方もよろしく頼むよ！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        "#6P#0001F了解しました！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    SetChrPos(0x0, 50090, 0, 51200, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xA, 48320, 150, 52390, 90)
    SetChrPos(0xF, 59160, 400, 55750, 0)
    OP_93(0xB, 0x87, 0x0)
    SetChrPos(0xE, 48700, 0, 59700, 90)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetScenarioFlags(0xE1, 6)
    OP_29(0x4D, 0x1, 0x7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_163E end

    def Function_14_1BF2(): pass

    label("Function_14_1BF2")

    TalkBegin(0xFF)
    SetChrName("")

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力は完全に落ちているようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_1BF2 end

    SaveToFile()

Try(main)
