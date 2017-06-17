from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t155b.bin",                # FileName
        "t155b",                    # MapName
        "t155b",                    # Location
        0x0052,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 82, 0, 1, 0, 2],
    )

    BuildStringList((
        "t155b",                  # 0
        "マフィア",               # 1
        "マフィア",               # 2
        "看護師フィリア",         # 3
        "研修医リットン",         # 4
        "用務員ダイソン",         # 5
        "ゲバル議員",             # 6
        "ゲバル議員",             # 7
        "セシル",                 # 8
        "ミハイル",               # 9
        "ラゴー教授",             # 10
        "ゲイリー教授",           # 11
        "アーシュラ主任",         # 12
        "bt154b",                 # 13
    ))

    ATBonus("ATBonus_374", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_454", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 11, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_468", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_46C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_470", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_438", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_43C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_440", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_444", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_448", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_44C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_474", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt154b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31103.dat", "ms31003.dat", "ms31003.dat", "ms67101.dat", 0, 0, 0, 0, "MonsterBattlePostion_454", "MonsterBattlePostion_434", "ed7402", "ed7403", "ATBonus_374"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50362.itc",                   # 00
        "apl/ch50363.itc",                   # 01
        "chr/ch29900.itc",                   # 02
        "chr/ch29400.itc",                   # 03
        "apl/ch50153.itc",                   # 04
        "chr/ch33602.itc",                   # 05
        "chr/ch05300.itc",                   # 06
        "apl/ch50144.itc",                   # 07
        "chr/ch29202.itc",                   # 08
        "chr/ch32702.itc",                   # 09
        "chr/ch32900.itc",                   # 0A
        "chr/ch33600.itc",                   # 0B
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
    DeclNpc(-55169,  0,       -50069,  0,    261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-55930,  0,       -49529,  0,    261,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-55549,  379,     -47700,  90,   342,  0x0, 1,   4,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(54200,   -300,    -2799,   270,  389,  0x0, 0,   11,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-54500,  250,     -52330,  270,  468,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(6519,    0,       -48889,  0,    389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6150,    400,     -47400,  0,    468,  0x0, 0,   7,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-102150, 250,     -4730,   180,  469,  0x0, 0,   8,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-102150, 250,     -7550,   0,    469,  0x0, 0,   9,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-100489, 0,       -6130,   270,  389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)

    DeclEvent(0x0000, 0, 15,  -1.5,                  9.0,                   -1.0,                  110.25,                [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.5,                   -1.2857143878936768,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 29,  -9.0,                  21.0,                  0.0,                   110.25,                [0.1428571492433548,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.2857143878936768,    -7.0,                  -0.0,                  1.0])

    DeclActor(-6230,   0,       14490,   1200,    -6230,   1500,    14490,   0x007C, 0,  28, 0x0000)
    DeclActor(5240,    0,       -48080,  1200,    6340,    1500,    -47750,  0x007E, 0,  11, 0x0000)

    ScpFunction((
        "Function_0_530",          # 00, 0
        "Function_1_5E8",          # 01, 1
        "Function_2_699",          # 02, 2
        "Function_3_73E",          # 03, 3
        "Function_4_76E",          # 04, 4
        "Function_5_8FF",          # 05, 5
        "Function_6_A03",          # 06, 6
        "Function_7_A28",          # 07, 7
        "Function_8_A3A",          # 08, 8
        "Function_9_D33",          # 09, 9
        "Function_10_1027",        # 0A, 10
        "Function_11_12EA",        # 0B, 11
        "Function_12_1331",        # 0C, 12
        "Function_13_159B",        # 0D, 13
        "Function_14_17C7",        # 0E, 14
        "Function_15_192D",        # 0F, 15
        "Function_16_1D13",        # 10, 16
        "Function_17_1D8E",        # 11, 17
        "Function_18_2878",        # 12, 18
        "Function_19_2C95",        # 13, 19
        "Function_20_2CF3",        # 14, 20
        "Function_21_2D51",        # 15, 21
        "Function_22_2DAF",        # 16, 22
        "Function_23_2E0D",        # 17, 23
        "Function_24_2E6B",        # 18, 24
        "Function_25_2EB9",        # 19, 25
        "Function_26_3915",        # 1A, 26
        "Function_27_39BD",        # 1B, 27
        "Function_28_3E5F",        # 1C, 28
        "Function_29_3E91",        # 1D, 29
    ))


    def Function_0_530(): pass

    label("Function_0_530")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_570"),
        (1, "loc_57C"),
        (2, "loc_588"),
        (3, "loc_594"),
        (4, "loc_5A0"),
        (5, "loc_5AC"),
        (6, "loc_5B8"),
        (SWITCH_DEFAULT, "loc_5C4"),
    )


    label("loc_570")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_57C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_588")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_594")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_5A0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_5AC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_5B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_5C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_5D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_5E7")

    Return()

    # Function_0_530 end

    def Function_1_5E8(): pass

    label("Function_1_5E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 6)), scpexpr(EXPR_END)), "loc_5FB")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_600")

    label("loc_5FB")

    ClearChrFlags(0xD, 0x80)

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_END)), "loc_613")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 2)), scpexpr(EXPR_END)), "loc_62B")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)

    label("loc_62B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64B")
    SetScenarioFlags(0xE6, 6)
    Jump("loc_689")

    label("loc_64B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66F")
    Event(0, 18)
    Jump("loc_689")

    label("loc_66F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_689")
    Event(0, 17)

    label("loc_689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_698")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 27)

    label("loc_698")

    Return()

    # Function_1_5E8 end

    def Function_2_699(): pass

    label("Function_2_699")

    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C6")
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)

    label("loc_6C6")

    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_6F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_709")
    Call(0, 16)

    label("loc_709")

    ClearMapObjFlags(0x0, 0x10)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_END)), "loc_720")
    OP_66(0x1, 0x1)

    label("loc_720")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73D")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_73D")

    Return()

    # Function_2_699 end

    def Function_3_73E(): pass

    label("Function_3_73E")

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

    # Function_3_73E end

    def Function_4_76E(): pass

    label("Function_4_76E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 6)), scpexpr(EXPR_END)), "loc_8C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_847")

    #C0002
    ChrTalk(
        0xFE,
        "ゲバルさんが先程戻ってきました～。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "てっきりベッドを占領していることを\x01",
            "怒られるかと思ったんですが、\x01",
            "なんだか落ち込んでて……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "ああ塞ぎ込んでるのをみると\x01",
            "少し可哀想ですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8BB")

    label("loc_847")


    #C0005
    ChrTalk(
        0xFE,
        (
            "ゲバルさん、病室に戻ってから\x01",
            "ずっとああして塞ぎ込んでます。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "そんなに怖い目に\x01",
            "あっちゃったんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BB")

    Jump("loc_8FB")

    label("loc_8C0")


    #C0007
    ChrTalk(
        0xFE,
        (
            "ゲバルさん、こんなときに\x01",
            "どこ行っちゃったんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FB")

    TalkEnd(0xFE)
    Return()

    # Function_4_76E end

    def Function_5_8FF(): pass

    label("Function_5_8FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 6)), scpexpr(EXPR_END)), "loc_991")

    #C0008
    ChrTalk(
        0xFE,
        (
            "はやくダイソンさんに\x01",
            "ちゃんとした治療を\x01",
            "してあげたいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "さすがにこの病室じゃ\x01",
            "設備もなにも足りなさ過ぎるな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FF")

    label("loc_991")


    #C0010
    ChrTalk(
        0xFE,
        (
            "とりあえず落ち着いてきたけど……\x01",
            "熱が出だしたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "しばらくは苦しいだろうな。\x01",
            "かわいそうに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FF")

    TalkEnd(0xFE)
    Return()

    # Function_5_8FF end

    def Function_6_A03(): pass

    label("Function_6_A03")

    TalkBegin(0xFE)

    #C0012
    ChrTalk(
        0xFE,
        "……う、うう………………\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_A03 end

    def Function_7_A28(): pass

    label("Function_7_A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A39")
    Call(0, 25)

    label("loc_A39")

    Return()

    # Function_7_A28 end

    def Function_8_A3A(): pass

    label("Function_8_A3A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ACE")
    Jump("loc_B18")

    label("loc_ACE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AEE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B18")

    label("loc_AEE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B18")

    label("loc_B0E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B18")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C59")

    #C0013
    ChrTalk(
        0xFE,
        (
            "あぁ……\x01",
            "わしは一体どうすればいい……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "ここまで大胆な暗殺を決行するんじゃ、\x01",
            "きっとどこへ逃げても……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#0200F（妄想と戦ってますね……）\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#0103F（ハルトマン議長の\x01",
            "  裏の顔を知っているなら\x01",
            "  分からなくもない反応だけど……）\x02\x03",

            "#0108F（……不憫な人……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_D2B")

    label("loc_C59")


    #C0017
    ChrTalk(
        0xFE,
        (
            "……ええい、こうなったら\x01",
            "ハルトマン議長に反旗を翻すか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "この暗殺事件を公表すれば\x01",
            "世論はわしの味方を………………\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "…………だめじゃ。\x01",
            "ハルトマン議長ならこのくらい\x01",
            "もみ消してしまうじゃろうな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_A3A end

    def Function_9_D33(): pass

    label("Function_9_D33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D48")
    Call(0, 10)
    Jump("loc_1023")

    label("loc_D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EAA")

    #C0020
    ChrTalk(
        0xF,
        (
            "#1302Fあの……あなたもロイドたちに\x01",
            "協力して下さってるんですよね。\x02\x03",

            "#1309F先ほどはありがとうございます。\x01",
            "おかげで助かりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F……フ……\x01",
            "私は成り行きで手を貸したに過ぎん。\x02\x03",

            "礼ならこの者たちにでもするがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xF,
        (
            "#1305F（……あら、\x01",
            "  この人、どこかで……？）\x02\x03",

            "#1300F（……ううん、\x01",
            "  さすがに気のせいよね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 0)
    Jump("loc_1023")

    label("loc_EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA1")

    #C0023
    ChrTalk(
        0xF,
        (
            "#1301Fそれにしても……\x01",
            "ロイドの話を聞いても\x01",
            "いまだに信じられないわ。\x02\x03",

            "まさかあのヨアヒム先生が\x01",
            "こんな大それた事をするなんて……\x02\x03",

            "#1303F趣味人でサボリ好きだけど、\x01",
            "患者さんたちにも慕われている\x01",
            "優しい先生だと思っていたのに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1023")

    label("loc_FA1")


    #C0024
    ChrTalk(
        0xF,
        (
            "#1303Fまさかあのヨアヒム先生が\x01",
            "こんな大それた事をするなんて……\x02\x03",

            "#1308F病院での先生の振る舞いは\x01",
            "すべて演技だったのかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1023")

    TalkEnd(0xFE)
    Return()

    # Function_9_D33 end

    def Function_10_1027(): pass

    label("Function_10_1027")

    EventBegin(0x0)
    Fade(500)
    OP_68(5950, 1000, -48900, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 5000, 0, -48900, 45)
    SetChrPos(0x102, 4130, 0, -49060, 45)
    SetChrPos(0x103, 3790, 0, -48130, 90)
    SetChrPos(0x104, 3320, 0, -47550, 90)
    SetChrPos(0x106, 5890, 0, -50380, 0)
    OP_93(0xF, 0x0, 0x0)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0025
    ChrTalk(
        0xF,
        (
            "#1302F……ほっ……\x01",
            "ミハイル君、薬が効いて来たみたい。\x01",
            "よく寝ているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#0000Fそうか、よかった……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0xF, 400)

    #C0027
    ChrTalk(
        0x101,
        (
            "#0005F（そうだ、この兄貴のバッジ……）\x02\x03",

            "#0008F（兄貴の形見を取り戻したことを\x01",
            "  セシル姉にも……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0028
    ChrTalk(
        0x101,
        (
            "#0006F（……何を考えてるんだ、俺。）\x02\x03",

            "（今はみんな手一杯なのに\x01",
            "  これ以上の負担はかけられない。）\x02\x03",

            "#0008F（セシル姉にはこの事件が終わってから\x01",
            "  ゆっくり話そう……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    #C0029
    ChrTalk(
        0xF,
        "#1305F……ロイド、どうかした？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#0000F……いや、なんでもないよ。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 5000, 0, -48900, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xEC, 7)
    EventEnd(0x5)
    Return()

    # Function_10_1027 end

    def Function_11_12EA(): pass

    label("Function_11_12EA")

    TalkBegin(0x10)

    #C0031
    ChrTalk(
        0x10,
        "すー……すー……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "薬が効いてよく眠っているようだ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_11_12EA end

    def Function_12_1331(): pass

    label("Function_12_1331")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13C5")
    Jump("loc_140F")

    label("loc_13C5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13E5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_140F")

    label("loc_13E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1405")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_140F")

    label("loc_1405")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_140F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1532")

    #C0033
    ChrTalk(
        0xFE,
        (
            "……確かに、ヨアヒム君の経歴には\x01",
            "不透明な部分が幾つかあった。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "レミフェリア公国の出身者で\x01",
            "薬学・神経科の研究で大きな成果を成し……\x01",
            "……それから……？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……考えてみればわしらは彼のことを\x01",
            "何も分かっていなかったのかもしれん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1593")

    label("loc_1532")


    #C0036
    ChrTalk(
        0xFE,
        "ヨアヒム君の有能さ、人柄……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "わしらはそれを表面的にしか\x01",
            "捉えてなかったのかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1593")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_1331 end

    def Function_13_159B(): pass

    label("Function_13_159B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_162F")
    Jump("loc_1679")

    label("loc_162F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_164F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1679")

    label("loc_164F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_166F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1679")

    label("loc_166F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1679")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1747")

    #C0038
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "研究棟の中に満ちていた\x01",
            "あの淀んだ空気はなんだったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "病棟の中まで入ってきていたら\x01",
            "患者たちの病状が悪化しかねんところだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_17BF")

    label("loc_1747")


    #C0040
    ChrTalk(
        0xFE,
        (
            "研究棟の中に満ちていた\x01",
            "淀んだ空気は一体……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "日々研究に明け暮れてきたが、\x01",
            "まだまだ理解に苦しむことが多いな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_159B end

    def Function_14_17C7(): pass

    label("Function_14_17C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189D")

    #C0042
    ChrTalk(
        0xFE,
        (
            "魔獣を連れていた人は、\x01",
            "研究棟の４階まで上がっていきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "黒い服ではなかったですし、\x01",
            "多分、マフィアではないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "平然と魔獣を連れている姿は\x01",
            "あまりにも異様でしたけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1929")

    label("loc_189D")


    #C0045
    ChrTalk(
        0xFE,
        (
            "研究棟の４階に上がっていったあの人……\x01",
            "多分、マフィアではないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "平然と魔獣を連れている姿は\x01",
            "あまりにも異様でしたけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1929")

    TalkEnd(0xFE)
    Return()

    # Function_14_17C7 end

    def Function_15_192D(): pass

    label("Function_15_192D")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
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
    OP_68(-9000, 1000, 9000, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, -4800, 0, 9600, 270)
    SetChrPos(0x102, -4800, 0, 8300, 270)
    SetChrPos(0x103, -3500, 0, 8300, 270)
    SetChrPos(0x104, -3500, 0, 9600, 270)
    SetChrPos(0x106, -2200, 0, 8950, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -8430, 0, 21350, 180)
    SetChrPos(0x9, -9590, 0, 21100, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    SetCameraDistance(23500, 3000)

    def lambda_1A7C():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A7C)
    Sleep(50)

    def lambda_1A94():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A94)
    Sleep(50)

    def lambda_1AAC():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AAC)
    Sleep(50)

    def lambda_1AC4():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1AC4)
    Sleep(50)

    def lambda_1ADC():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1ADC)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1B76():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B76)
    Sleep(50)

    def lambda_1B86():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1B86)
    Sleep(50)

    def lambda_1B96():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B96)
    Sleep(50)

    def lambda_1BA6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BA6)
    Sleep(50)

    def lambda_1BB6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1BB6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    Fade(500)
    OP_68(-8850, 1000, 16000, 0)
    OP_68(-8850, 1000, 10500, 1500)
    SetCameraDistance(25500, 0)
    SetCameraDistance(19500, 1500)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_1C26():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C26)

    def lambda_1C3B():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C3B)
    Sleep(500)
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
    OP_0D()
    Sleep(500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(400)
    Battle("BattleInfo_474", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Call(0, 16)
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
    SetChrPos(0x0, -8500, 0, 8500, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE2, 3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_192D end

    def Function_16_1D13(): pass

    label("Function_16_1D13")

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
    SetChrPos(0x8, -8580, 0, 14110, 315)
    SetChrPos(0x9, -11600, 0, 11420, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_16_1D13 end

    def Function_17_1D8E(): pass

    label("Function_17_1D8E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-52500, 1000, -50000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -49550, 50, -49660, 270)
    SetChrPos(0x102, -49550, 50, -50640, 270)
    SetChrPos(0x103, -48250, 50, -50640, 270)
    SetChrPos(0x104, -48250, 50, -49660, 270)
    SetChrPos(0x106, -46950, 50, -50160, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, -56730, 0, -50110, 0)
    SetChrPos(0xB, -55580, 0, -49500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x4)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    OP_68(-54000, 1000, -50000, 3000)

    def lambda_1EF9():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EF9)
    Sleep(50)

    def lambda_1F11():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F11)
    Sleep(50)

    def lambda_1F29():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F29)
    Sleep(50)

    def lambda_1F41():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F41)
    Sleep(50)

    def lambda_1F59():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1F59)
    Sleep(200)

    def lambda_1F71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F71)

    def lambda_1F82():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1F82)
    Sleep(100)

    def lambda_1F96():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1F96)
    Sleep(50)

    def lambda_1FA6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1FA6)
    Sleep(350)

    def lambda_1FB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1FB6)

    def lambda_1FC7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1FC7)
    Sleep(500)

    def lambda_1FDB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1FDB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x4, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)

    #C0047
    ChrTalk(
        0xA,
        (
            "#3Pああ～っ！\x01",
            "弟君にランディさん！？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0302F#11Pはは……\x01",
            "フィリアちゃん、無事だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        (
            "#6Pたしかクロスベル警察の……\x01",
            "もしかして、もう安全なのかい！？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0003F#11Pいえ、まだ侵入者は\x01",
            "病院内に残っている状況です。\x02\x03",

            "#0013Fそれより、そちらの人は……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        (
            "#3Pうん……\x01",
            "用務員のダイソンさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xA,
        (
            "#3Pあいつらに斬りつけられて\x01",
            "大ケガをしちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "#6P一応、応急処置はしたから\x01",
            "命に別状はないと思うが……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        "#6Pまだちょっと目が離せないかな。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#0006F#11P……そうですか……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        (
            "#0105F#11Pそういえば……\x01",
            "この部屋の患者さんはどちらに？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xA,
        (
            "#3Pゲバルっていう議員のオジサンが\x01",
            "使っている部屋なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        (
            "#3Pうーん、こんな時に\x01",
            "どこに行っちゃったのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xA,
        (
            "#3Pま、ずっと仮病で\x01",
            "入院してるだけのヒトだから\x01",
            "心配はいらないと思うけど～。\x02",
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
    Sleep(1000)

    #C0060
    ChrTalk(
        0x101,
        (
            "#0003F#11Pと、とりあえずこちらでも\x01",
            "安否は確認しておきます。\x02\x03",

            "#0005F……ところでフィリアさん。\x02\x03",

            "#0001Fセシル姉がどこにいるか\x01",
            "ご存知じゃありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        "#3Pセシル先輩～？\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        (
            "#3Pあれれ、ナースセンターに\x01",
            "戻ってると思ったけど……？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xB,
        (
            "#6Pいや、確かセシルさん、\x01",
            "３０１号室のミハイル君の所に\x01",
            "行ってるんじゃなかったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        (
            "#6P今日はシズクちゃんが外出して\x01",
            "寂しがってるから、絵本を読んで\x01",
            "あげるって言ってたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 6)), scpexpr(EXPR_END)), "loc_2729")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0065
    ChrTalk(
        0x103,
        (
            "#0205F#11P３０１号室って、\x01",
            "ここに来る途中に入った\x01",
            "個室の事ですよね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        "#0301F#11Pああ、誰も居なかったが……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0067
    ChrTalk(
        0xA,
        "#3Pほ、本当～！？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        "#6Pそ、それじゃあどこへ……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#0008F#11P……セシル姉とミハイル君は\x01",
            "こちらの方で捜してみます。\x02\x03",

            "#0013Fお２人は怪我人の治療に\x01",
            "専念してあげてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        "#6Pあ、ああ……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        "#3Pよろしくお願いね～！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2819")

    label("loc_2729")


    #C0072
    ChrTalk(
        0x103,
        (
            "#0205F#11P３０１号室というのは\x01",
            "途中にあった個室の事ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#0006F#11Pああ、ちょうど\x01",
            "通り過ぎてしまったな。\x02\x03",

            "#0000Fこちらで確認しますから\x01",
            "お２人は怪我人の治療に\x01",
            "専念してあげてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        "#6Pああ……！\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        "#3Pうん、任せて～！\x02",
    )

    CloseMessageWindow()

    label("loc_2819")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -53190, 0, -50010, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xA, -55170, 0, -50070, 0)
    SetChrPos(0xB, -55930, 0, -49530, 0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0xE2, 4)
    OP_29(0x4D, 0x1, 0xA)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_1D8E end

    def Function_18_2878(): pass

    label("Function_18_2878")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3300, 1000, -50000, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -800, 0, -50000, 90)
    SetChrPos(0x102, -800, 0, -50000, 90)
    SetChrPos(0x103, -800, 0, -50000, 90)
    SetChrPos(0x104, -800, 0, -50000, 90)
    SetChrPos(0x106, -800, 0, -50000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(4700, 1000, -50000, 3000)
    BeginChrThread(0x101, 3, 0, 19)
    Sleep(600)
    BeginChrThread(0x102, 3, 0, 20)
    Sleep(600)
    BeginChrThread(0x103, 3, 0, 21)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 22)
    Sleep(600)
    BeginChrThread(0x106, 3, 0, 23)
    WaitChrThread(0x101, 3)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 6)), scpexpr(EXPR_END)), "loc_2A0A")

    #C0076
    ChrTalk(
        0x101,
        "#0001F#6Pやっぱり誰もいないか……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#0106F#6Pベッドの下に隠れてるとか\x01",
            "そんな事はないわよね……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACE")

    label("loc_2A0A")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0078
    ChrTalk(
        0x101,
        "#0005F#6Pあ、あれ……？\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        (
            "#0301F#6P誰も居ないが……\x01",
            "ここが３０１号室だよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        (
            "#0101F#6Pその筈だけど……\x02\x03",

            "#0108Fベッドの下に隠れてるとか\x01",
            "そんな事はないわよね……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ACE")


    #C0081
    ChrTalk(
        0x103,
        (
            "#0201F#6Pそうでしたら\x01",
            "わたしが気付きますし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x106)
    OP_68(5790, 1000, -49750, 2500)
    BeginChrThread(0x106, 3, 0, 24)
    WaitChrThread(0x106, 3)
    OP_6F(0x1)
    Sound(820, 0, 100, 0)
    Sleep(1000)

    #C0082
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#11P……まだ暖かい。\x02\x03",

            "どうやらこの部屋の主は\x01",
            "先程までここにいたようだ。\x02\x03",

            "そのセシルという看護師と共に。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0013F#6Pくっ……\x01",
            "とにかく捜さないと……！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        "#0307F#6Pおお……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    OP_68(3000, 1000, -50000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 3000, 0, -50000, 90)
    SetChrPos(0x1, 3000, 0, -50000, 90)
    SetChrPos(0x2, 3000, 0, -50000, 90)
    SetChrPos(0x3, 3000, 0, -50000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE2, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_2878 end

    def Function_19_2C95(): pass

    label("Function_19_2C95")


    def lambda_2C9A():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C9A)

    def lambda_2CAF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CAF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2CC8():
        OP_95(0xFE, 3090, 0, -49370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CC8)
    WaitChrThread(0x101, 1)

    def lambda_2CE6():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CE6)
    WaitChrThread(0x101, 1)
    Return()

    # Function_19_2C95 end

    def Function_20_2CF3(): pass

    label("Function_20_2CF3")


    def lambda_2CF8():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CF8)

    def lambda_2D0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D0D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2D26():
        OP_95(0xFE, 2350, 0, -51300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D26)
    WaitChrThread(0xFE, 1)

    def lambda_2D44():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D44)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_2CF3 end

    def Function_21_2D51(): pass

    label("Function_21_2D51")


    def lambda_2D56():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D56)

    def lambda_2D6B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D6B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2D84():
        OP_95(0xFE, 2420, 0, -48520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D84)
    WaitChrThread(0xFE, 1)

    def lambda_2DA2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DA2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_2D51 end

    def Function_22_2DAF(): pass

    label("Function_22_2DAF")


    def lambda_2DB4():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DB4)

    def lambda_2DC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DC9)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2DE2():
        OP_95(0xFE, 1330, 0, -48080, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DE2)
    WaitChrThread(0xFE, 1)

    def lambda_2E00():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E00)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_2DAF end

    def Function_23_2E0D(): pass

    label("Function_23_2E0D")


    def lambda_2E12():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E12)

    def lambda_2E27():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E27)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2E40():
        OP_95(0xFE, 1320, 50, -50150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E40)
    WaitChrThread(0xFE, 1)

    def lambda_2E5E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E5E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_2E0D end

    def Function_24_2E6B(): pass

    label("Function_24_2E6B")


    def lambda_2E70():
        OP_95(0xFE, 4950, 0, -50540, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E70)
    WaitChrThread(0xFE, 1)

    def lambda_2E8E():
        OP_95(0xFE, 5950, 0, -48890, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E8E)
    WaitChrThread(0xFE, 1)

    def lambda_2EAC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EAC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_2E6B end

    def Function_25_2EB9(): pass

    label("Function_25_2EB9")

    EventBegin(0x0)
    OP_4B(0xD, 0xFF)
    Fade(1000)
    OP_68(54550, 1300, -1040, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 54580, 0, -1490, 180)
    SetChrPos(0x102, 54860, 0, -360, 180)
    SetChrPos(0x103, 54100, 0, 400, 180)
    SetChrPos(0x104, 54810, 0, 1280, 180)
    SetChrPos(0x106, 54100, 0, 2190, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xD, 54620, 0, -2970, 0)
    OP_0D()

    #C0085
    ChrTalk(
        0x101,
        "#0005F#5Pあれっ……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_9C(0xD, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0086
    ChrTalk(
        0xD,
        "#2Pひ、ひいいっ……！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xD,
        (
            "#2P頼む、頼むから\x01",
            "命だけはお助けを～っ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        "#0301F#5Pなんだ、このオッサンは……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#0106F#5P帝国派のゲバル議員……\x01",
            "フィリアさんに聞いた人物ね。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xD)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0090
    ChrTalk(
        0xD,
        "#2Pな、なんだお前たちは……！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xD,
        "#2Pマフィアどもではないのか！？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#0003F#5Pクロスベル警察、\x01",
            "特務支援課の者です。\x02\x03",

            "#0001Fゲバル議員、ここで何を？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xD,
        (
            "#2Pか、隠れていたに\x01",
            "決まっておるだろう！？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xD,
        (
            "#2Pおそらく、マフィアどもは\x01",
            "わしを始末しに来たに違いない！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xD,
        (
            "#2Pハルトマン議長……\x01",
            "まさかこんな形でわしを\x01",
            "切り捨てようとするとは……！\x02",
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

    #C0096
    ChrTalk(
        0x101,
        "#0008F#5P（エリィ、どう思う……？）\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x102,
        (
            "#0106F#5P（……完全に被害妄想だと思う。）\x02\x03",

            "#0111F（たぶん議長はこの人を\x01",
            "  全く重要視していないはずよ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        "#0206F#5P（まあ、そんな感じですよね。）\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xD,
        (
            "#2Pそ、そうだお前たち！\x01",
            "わしを連れてこのまま脱出しろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xD,
        "#2Pわしはまだ死にたくはない！\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#0003F#5P……生憎、まだ安否が\x01",
            "確認できない人たちがいます。\x02\x03",

            "#0001F自分たちはその確認を\x01",
            "しなくてはなりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#0100F#5Pいったんお部屋に戻って\x01",
            "待っていていただけませんか？\x02\x03",

            "この辺りのマフィアは制圧したので\x01",
            "安全に移動できると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xD,
        (
            "#2Pき、き、貴様ら……\x01",
            "わしを誰だと思っている！？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xD,
        (
            "#2Pクロスベル自治州を代表する\x01",
            "大物議員の一人なのだぞ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5P……うるさい男だ。\x01",
            "軽く眠らせておくか？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0106
    ChrTalk(
        0xD,
        "#2Pな、なんだお前は……！？\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xD,
        (
            "#2Pそ、その格好……\x01",
            "どこかで聞いたような……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5Pフフ……どこで聞いたのかな？\x02\x03",

            "よもや《黒月》に関する\x01",
            "妖しげな噂ではあるまいな？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0109
    ChrTalk(
        0xD,
        "#2Pひっ、まさか……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0006F#5P……からかうのは\x01",
            "そのくらいにしてくれ。\x02\x03",

            "#0013F──議員。\x01",
            "とにかく今は緊急事態です。\x02\x03",

            "どうか協力して、\x01",
            "お部屋に避難してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xD,
        "#2Pわ、わ、分かった……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xD,
        (
            "#2P一刻も早くマフィアどもを\x01",
            "追い払うのだぞ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(56620, 500, 2080, 0)
    MoveCamera(70, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28000, 0)
    SetCameraDistance(27000, 2500)
    SetChrPos(0x101, 54770, 0, 2600, 270)
    SetChrPos(0x102, 55470, 0, 3170, 270)
    SetChrPos(0x103, 55830, 0, 2100, 270)
    SetChrPos(0x104, 56450, 0, 2800, 270)
    SetChrPos(0x106, 57130, 0, 2110, 270)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    BeginChrThread(0xD, 3, 0, 26)
    WaitChrThread(0xD, 3)
    OP_6F(0x1)
    Sound(107, 0, 100, 0)
    Sleep(500)

    #C0113
    ChrTalk(
        0x104,
        (
            "#0300F#5Pやれやれ、入院患者とは\x01",
            "思えねぇ足の早さだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        (
            "#0211F#11Pまあ、仮病で入院していた\x01",
            "だけのようですし。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3876")

    #C0115
    ChrTalk(
        0x101,
        (
            "#0006F#5P──時間を取られた。\x01",
            "セシル姉たちを捜しに行こう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B4")

    label("loc_3876")


    #C0116
    ChrTalk(
        0x101,
        (
            "#0006F#5P──時間を取られた。\x01",
            "早く研究棟の方に向かおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B4")


    #C0117
    ChrTalk(
        0x102,
        "#0101F#5Pええ……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    SetChrPos(0x0, 50910, 0, 110, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetScenarioFlags(0xE2, 6)
    OP_29(0x4D, 0x1, 0xB)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_25_2EB9 end

    def Function_26_3915(): pass

    label("Function_26_3915")

    SetChrPos(0xFE, 54490, 0, 1290, 225)

    def lambda_392B():
        OP_95(0xFE, 53490, 0, 2450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_392B)
    WaitChrThread(0xFE, 1)

    def lambda_3949():
        OP_95(0xFE, 51600, 0, 2360, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3949)
    WaitChrThread(0xFE, 1)

    def lambda_3967():
        OP_95(0xFE, 51080, 0, 40, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3967)
    WaitChrThread(0xFE, 1)

    def lambda_3985():
        OP_95(0xFE, 48880, 0, 20, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3985)
    Sound(107, 0, 100, 0)
    Sleep(200)

    def lambda_39A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39A8)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_26_3915 end

    def Function_27_39BD(): pass

    label("Function_27_39BD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(5290, 2000, -50030, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21610, 0)
    SetChrPos(0x101, 4600, 0, -50000, 90)
    SetChrPos(0x102, 3600, 0, -49400, 90)
    SetChrPos(0x103, 3600, 0, -50600, 90)
    SetChrPos(0x104, 2200, 0, -49400, 90)
    SetChrPos(0x106, 2200, 0, -50600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetChrPos(0xF, 6200, 0, -50000, 270)
    FadeToBright(1000, 0)
    OP_68(5290, 1000, -50030, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(300)

    #C0118
    ChrTalk(
        0xF,
        (
            "#1306F#11Pそう……\x01",
            "そんな事情で病院に。\x02\x03",

            "#1308Fまさかヨアヒム先生が……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#0006F#6P……まだ怪しいと\x01",
            "決まったわけじゃないけどね。\x02\x03",

            "#0001F彼はまだ研究棟に？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xF,
        (
            "#1303F#11Pそれは判らないけれど……\x02\x03",

            "#1301F他の教授の方々は研究棟に\x01",
            "取り残されているかもしれないわ。\x02\x03",

            "黒服の人たちが連れ出したのは\x01",
            "研修医の人たちばかりだったから。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#0003F#6Pそうか……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x104,
        (
            "#0301F#6Pところで、さっきの魔獣は\x01",
            "いったい何だったんスか？\x02\x03",

            "不気味っつーか……\x01",
            "得体が知れない感じだったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#0208F#6P……そうですね。\x02\x03",

            "まるで何かのバランスが\x01",
            "欠けてしまってるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#0101F#6Pやはりマフィアたちが\x01",
            "連れ込んできたんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xF,
        (
            "#1306F#11P分からないけれど……\x01",
            "研究棟からいきなり現れたの。\x02\x03",

            "#1301Fそれでそのまま\x01",
            "取り囲まれてしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6Pどうやら研究棟とやらに\x01",
            "何かが隠されているらしいな。\x02\x03",

            "時間が惜しい──\x01",
            "早速、向かうとするぞ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    #C0127
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0013F#11Pああ……！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3670, 0, -50220, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xF, 6520, 0, -48890, 0)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0xE2, 7)
    OP_29(0x4D, 0x1, 0xC)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_27_39BD end

    def Function_28_3E5F(): pass

    label("Function_28_3E5F")

    TalkBegin(0xFF)
    SetChrName("")

    #A0128
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

    # Function_28_3E5F end

    def Function_29_3E91(): pass

    label("Function_29_3E91")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4118")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CE")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3ED1")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_3ED1")


    #C0129
    ChrTalk(
        0x103,
        (
            "#0200F……待ってください。\x01",
            "さっきの左の部屋から人の気配が。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F33")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_3F33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F54")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_3F54")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F75")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_3F75")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F96")
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_3F96")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3FBB")

    def lambda_3FAD():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FAD)

    label("loc_3FBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3FDD")

    def lambda_3FCF():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3FCF)

    label("loc_3FDD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3FFF")

    def lambda_3FF1():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3FF1)

    label("loc_3FFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4021")

    def lambda_4013():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4013)

    label("loc_4021")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4043")

    def lambda_4035():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_4035)

    label("loc_4043")

    Sleep(1000)
    Fade(500)
    OP_68(-16780, 1000, 8490, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    OP_0D()

    #C0130
    ChrTalk(
        0x101,
        "#0005F左の部屋……あの部屋か。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        "#0101Fロイド、早く確認しましょう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4113")

    label("loc_40CE")


    #C0132
    ChrTalk(
        0x101,
        (
            "#0001F３０２号室に誰かいるみたいだ……\x01",
            "先にそちらを確認しよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4113")

    Jump("loc_4160")

    label("loc_4118")


    #C0133
    ChrTalk(
        0x101,
        (
            "#0001F……セシル姉は\x01",
            "３０１号室にいるみたいだ。\x01",
            "早く行ってみよう！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4160")

    Sleep(50)
    SetChrPos(0x0, -8930, 0, 17770, 180)
    EventEnd(0x4)
    Return()

    # Function_29_3E91 end

    SaveToFile()

Try(main)
