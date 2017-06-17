from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t154b.bin",                # FileName
        "t154b",                    # MapName
        "t154b",                    # Location
        0x0051,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 81, 0, 2, 0, 3],
    )

    BuildStringList((
        "t154b",                  # 0
        "マフィア",               # 1
        "マフィア",               # 2
        "マフィア",               # 3
        "マフィア",               # 4
        "研修医グェン",           # 5
        "看護師ラン",             # 6
        "入院患者",               # 7
        "入院患者",               # 8
        "入院患者",               # 9
        "看護師エイダ",           # 10
        "診察医ベルダイン",       # 11
        "入院患者",               # 12
        "入院患者",               # 13
        "入院患者",               # 14
        "bt154b",                 # 15
    ))

    ATBonus("ATBonus_328", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_408", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 5, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_418", 11, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_41C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_400", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 5, 5, 45)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_428", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt154b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31103.dat", "ms67101.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_408", "MonsterBattlePostion_3E8", "ed7402", "ed7403", "ATBonus_328"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50362.itc",                   # 00
        "apl/ch50363.itc",                   # 01
        "chr/ch29500.itc",                   # 02
        "chr/ch29700.itc",                   # 03
        "chr/ch29800.itc",                   # 04
        "chr/ch29300.itc",                   # 05
        "apl/ch50133.itc",                   # 06
        "apl/ch50137.itc",                   # 07
        "apl/ch50141.itc",                   # 08
        "apl/ch50135.itc",                   # 09
        "apl/ch50139.itc",                   # 0A
        "apl/ch50143.itc",                   # 0B
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-1000,   0,       55279,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-4309,   0,       55029,   0,    261,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4000,   699,     57029,   270,  341,  0x0, 0,   6,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(4949,    699,     57029,   270,  341,  0x0, 0,   7,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(4949,    699,     52029,   270,  341,  0x0, 0,   8,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(4940,    0,       -54380,  0,    261,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4269,    0,       -53810,  0,    261,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-4150,   699,     -52060,  270,  341,  0x0, 0,   9,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-4150,   699,     -56970,  270,  341,  0x0, 0,   10,  0,   255, 255, 0,   13,  255,  0)
    DeclNpc(4849,    699,     -52060,  270,  341,  0x0, 0,   11,  0,   255, 255, 0,   14,  255,  0)

    DeclEvent(0x0000, 0, 18,  26.5,                  -11.0,                 -1.0,                  110.25,                [0.1428571492433548,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.7857143878936768,   3.6666667461395264,    0.20000000298023224,   1.0])

    DeclActor(29820,   0,       -12440,  1200,    29820,   1500,    -12440,  0x007C, 0,  21, 0x0000)

    ScpFunction((
        "Function_0_4C4",          # 00, 0
        "Function_1_57C",          # 01, 1
        "Function_2_5A7",          # 02, 2
        "Function_3_5FD",          # 03, 3
        "Function_4_69A",          # 04, 4
        "Function_5_6CA",          # 05, 5
        "Function_6_746",          # 06, 6
        "Function_7_87B",          # 07, 7
        "Function_8_9DA",          # 08, 8
        "Function_9_B46",          # 09, 9
        "Function_10_C9D",         # 0A, 10
        "Function_11_D52",         # 0B, 11
        "Function_12_E48",         # 0C, 12
        "Function_13_F7E",         # 0D, 13
        "Function_14_1106",        # 0E, 14
        "Function_15_12B0",        # 0F, 15
        "Function_16_15C2",        # 10, 16
        "Function_17_163D",        # 11, 17
        "Function_18_1BF3",        # 12, 18
        "Function_19_1ECB",        # 13, 19
        "Function_20_1F46",        # 14, 20
        "Function_21_25A9",        # 15, 21
    ))


    def Function_0_4C4(): pass

    label("Function_0_4C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_504"),
        (1, "loc_510"),
        (2, "loc_51C"),
        (3, "loc_528"),
        (4, "loc_534"),
        (5, "loc_540"),
        (6, "loc_54C"),
        (SWITCH_DEFAULT, "loc_558"),
    )


    label("loc_504")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_510")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_51C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_528")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_534")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_540")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_54C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_558")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_564")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_564")

    label("loc_57B")

    Return()

    # Function_0_4C4 end

    def Function_1_57C(): pass

    label("Function_1_57C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A6")
    OP_94(0xFE, 0xFFFFFAF6, 0xCFEE, 0x4D8, 0xD99E, 0x3E8)
    Sleep(400)
    Jump("Function_1_57C")

    label("loc_5A6")

    Return()

    # Function_1_57C end

    def Function_2_5A7(): pass

    label("Function_2_5A7")

    BeginChrThread(0xC, 0, 0, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC")
    Event(0, 20)
    Jump("loc_5FC")

    label("loc_5CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EB")
    Event(0, 17)
    Jump("loc_5FC")

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FC")
    Event(0, 15)

    label("loc_5FC")

    Return()

    # Function_2_5A7 end

    def Function_3_5FD(): pass

    label("Function_3_5FD")

    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66A")
    Call(0, 16)

    label("loc_66A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67B")
    Call(0, 19)

    label("loc_67B")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_693")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_693")

    ClearMapObjFlags(0x0, 0x10)
    Return()

    # Function_3_5FD end

    def Function_4_69A(): pass

    label("Function_4_69A")

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

    # Function_4_69A end

    def Function_5_6CA(): pass

    label("Function_5_6CA")

    TalkBegin(0xFE)

    #C0002
    ChrTalk(
        0xFE,
        (
            "私たちは患者さんに\x01",
            "悪い影響がでないように\x01",
            "ここに詰めているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "弟君、みんな。\x01",
            "病院の人たちを助けてあげて！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_6CA end

    def Function_6_746(): pass

    label("Function_6_746")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E0")

    #C0004
    ChrTalk(
        0xFE,
        (
            "そ、そうよ……\x01",
            "こういうときこそ、技術よりも\x01",
            "精神力が問われるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "患者さんを安心させるためにも\x01",
            "せめて私は笑顔でいないと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_877")

    label("loc_7E0")


    #C0006
    ChrTalk(
        0xFE,
        (
            "落ち着かないと……落ち着かないと……\x01",
            "落ち着かないと……落ち着かないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "……あぁっ、ダメ！\x01",
            "考えれば考えるほど\x01",
            "平静じゃいられなくなる……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_877")

    TalkEnd(0xFE)
    Return()

    # Function_6_746 end

    def Function_7_87B(): pass

    label("Function_7_87B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90F")
    Jump("loc_959")

    label("loc_90F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_92F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_959")

    label("loc_92F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_959")

    label("loc_94F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_959")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0008
    ChrTalk(
        0xFE,
        (
            "わしゃあとっくに\x01",
            "寝ておる時間なんじゃが……\x01",
            "すっかり目が覚めてしもうたわい……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_87B end

    def Function_8_9DA(): pass

    label("Function_8_9DA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A6E")
    Jump("loc_AB8")

    label("loc_A6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A8E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB8")

    label("loc_A8E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB8")

    label("loc_AAE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AB8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0009
    ChrTalk(
        0xFE,
        (
            "……さっき、銃声らしき音が\x01",
            "聞こえた気がするんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "まさかね……聞き間違いだよね。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_9DA end

    def Function_9_B46(): pass

    label("Function_9_B46")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BDA")
    Jump("loc_C24")

    label("loc_BDA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BFA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C24")

    label("loc_BFA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C24")

    label("loc_C1A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C24")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0011
    ChrTalk(
        0xFE,
        "なぁおい……何の騒ぎなんだ！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "どう考えても普通じゃないぞ、これ！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_B46 end

    def Function_10_C9D(): pass

    label("Function_10_C9D")

    TalkBegin(0xFE)

    #C0013
    ChrTalk(
        0xFE,
        (
            "ベルダイン先生がいてよかったわ。\x01",
            "どうしても看護師だけじゃ\x01",
            "患者さんは安心できないもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "本当なら他の病室の様子も\x01",
            "確かめにいきたいけど……\x01",
            "今は我慢するしかないわね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_C9D end

    def Function_11_D52(): pass

    label("Function_11_D52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCC")

    #C0015
    ChrTalk(
        0xFE,
        (
            "事態が収束するまで、\x01",
            "私は患者を元気づけることに専念しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "君たちも気を付けて行きたまえ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E44")

    label("loc_DCC")

    TurnDirection(0xFE, 0x15, 0)

    #C0017
    ChrTalk(
        0xFE,
        (
            "……いいから落ち着きなさい。\x01",
            "動いては縫合が外れてしまいますぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "大丈夫、じっとしていれば安全でしょう。\x02",
    )

    CloseMessageWindow()

    label("loc_E44")

    TalkEnd(0xFE)
    Return()

    # Function_11_D52 end

    def Function_12_E48(): pass

    label("Function_12_E48")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EDC")
    Jump("loc_F26")

    label("loc_EDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EFC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F26")

    label("loc_EFC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F1C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F26")

    label("loc_F1C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F26")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0019
    ChrTalk(
        0xFE,
        (
            "あわわわ……\x01",
            "病院は大丈夫なんですか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_E48 end

    def Function_13_F7E(): pass

    label("Function_13_F7E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1012")
    Jump("loc_105C")

    label("loc_1012")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1032")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_105C")

    label("loc_1032")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1052")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_105C")

    label("loc_1052")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_105C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0020
    ChrTalk(
        0xFE,
        (
            "お義母さまが\x01",
            "見舞いに来ているときでなくて\x01",
            "本当によかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "……もしかして、相当に\x01",
            "危険な状態なんじゃないの？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_F7E end

    def Function_14_1106(): pass

    label("Function_14_1106")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_119A")
    Jump("loc_11E4")

    label("loc_119A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_11BA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11E4")

    label("loc_11BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11DA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11E4")

    label("loc_11DA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11E4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0022
    ChrTalk(
        0xFE,
        (
            "ちょっ……ちょっとちょっと！\x01",
            "こちとらまだ病み上がりで、\x01",
            "ロクに歩けもしないってのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "いたた……ど、どうしよう。\x01",
            "こんなんじゃ逃げられないじゃない！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_1106 end

    def Function_15_12B0(): pass

    label("Function_15_12B0")

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
    OP_68(3750, 1000, 2800, 0)
    MoveCamera(35, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 2800, 0, 3450, 90)
    SetChrPos(0x102, 2800, 0, 2150, 90)
    SetChrPos(0x103, 1500, 0, 3450, 90)
    SetChrPos(0x104, 1500, 0, 2150, 90)
    SetChrPos(0x106, 200, 0, 2800, 90)
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
    SetChrPos(0x8, 9600, 0, 3440, 270)
    SetChrPos(0x9, 9450, 0, 1840, 270)
    FadeToBright(1000, 0)
    OP_68(4750, 1000, 2800, 1000)
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

    #C0024
    ChrTalk(
        0x103,
        "#0201F#1Pいきなりですか……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        "#0307F#5P片付けるぞ……！\x02",
    )

    CloseMessageWindow()
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
    OP_68(4250, 1000, 2800, 850)
    SetCameraDistance(17500, 850)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)

    def lambda_1512():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1512)

    def lambda_1527():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1527)
    Sleep(350)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(400)
    Battle("BattleInfo_428", 0x0, 0x0, 0x0, 0x0, 0xFF)
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
    SetChrPos(0x0, 4000, 0, 3000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE1, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_12B0 end

    def Function_16_15C2(): pass

    label("Function_16_15C2")

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
    SetChrPos(0x8, 6570, 0, 1270, 90)
    SetChrPos(0x9, 5480, 0, 3900, 270)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_16_15C2 end

    def Function_17_163D(): pass

    label("Function_17_163D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-100, 1000, 54020, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -600, 0, 49400, 0)
    SetChrPos(0x102, 600, 0, 49400, 0)
    SetChrPos(0x103, -600, 0, 48100, 0)
    SetChrPos(0x104, 600, 0, 48100, 0)
    SetChrPos(0x106, 0, 0, 46800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xD, -2500, 0, 55150, 180)
    SetChrPos(0xC, -2500, 0, 53950, 0)
    FadeToBright(1000, 0)
    OP_68(-870, 1000, 54870, 3000)

    def lambda_1754():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1754)
    Sleep(50)

    def lambda_176C():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_176C)
    Sleep(50)

    def lambda_1784():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1784)
    Sleep(50)

    def lambda_179C():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_179C)
    Sleep(50)

    def lambda_17B4():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_17B4)
    Sleep(200)

    def lambda_17CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17CC)
    Sleep(50)

    def lambda_17E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_17E0)
    Sleep(500)

    def lambda_17F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_17F4)
    Sleep(50)

    def lambda_1808():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1808)
    Sleep(500)

    def lambda_181C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_181C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_1835():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1835)

    def lambda_1842():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1842)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_1857():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1857)

    def lambda_1864():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1864)
    WaitChrThread(0x106, 1)

    def lambda_1875():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1875)
    OP_4B(0xD, 0xFF)
    EndChrThread(0xC, 0xFF)
    SetChrSubChip(0xC, 0x0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_18C4():
        OP_93(0xFE, 0x5A, 0x258)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_18C4)
    Sleep(50)

    def lambda_18D4():
        OP_93(0xFE, 0x5A, 0x258)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_18D4)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xC, 1)

    #C0026
    ChrTalk(
        0xC,
        "#6Pあ、あなた達は……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xD,
        "#6Pランディさん、弟君！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        (
            "#0302F#11Pおお！\x01",
            "ランちゃん、無事だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0000F#11Pよかった……\x01",
            "患者さんは全員いますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xD,
        (
            "#6Pこの部屋にいた人だったら\x01",
            "全員揃っているけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xC,
        (
            "#6Pねえ、あの黒服たちは\x01",
            "もう居なくなっちゃったの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        "#0206F#11Pいえ、残念ながらまだです。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#0103F#11P今は侵入者を制圧しながら\x01",
            "皆さんの安全を確認しています。\x02\x03",

            "#0101F危険かもしれませんから\x01",
            "ここで待っていてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xC,
        "#6Pわ、分かったわ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4B")

    #C0035
    ChrTalk(
        0xD,
        (
            "#6P多分、エイダやフィリア、\x01",
            "セシル先輩も残ってると思う……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xD,
        "#6P絶対に助けてあげて！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        "#0013F#11Pええ、もちろんです！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B8D")

    label("loc_1B4B")


    #C0038
    ChrTalk(
        0xD,
        (
            "#6Pみんな……\x01",
            "くれぐれも気をつけてね！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#0000F#11Pはい！\x02",
    )

    CloseMessageWindow()

    label("loc_1B8D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    SetChrPos(0x0, 10, 0, 50670, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xD, -4310, 0, 55030, 0)
    SetChrPos(0xC, -1000, 0, 55280, 180)
    OP_4C(0xD, 0xFF)
    BeginChrThread(0xC, 0, 0, 1)
    SetScenarioFlags(0xE2, 0)
    OP_29(0x4D, 0x1, 0x8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_163D end

    def Function_18_1BF3(): pass

    label("Function_18_1BF3")

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
    OP_68(26750, 1200, -11250, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 27250, 0, -11320, 180)
    SetChrPos(0x102, 26090, 0, -11300, 180)
    SetChrPos(0x103, 27290, 0, -9930, 180)
    SetChrPos(0x104, 26110, 0, -9930, 180)
    SetChrPos(0x106, 26710, 0, -8580, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xA, 26550, 0, -17660, 0)
    SetChrPos(0xB, 27830, 0, -18140, 0)
    FadeToBright(1000, 0)
    OP_68(26750, 1200, -13750, 1500)
    Sleep(1300)
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
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)

    def lambda_1DFC():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1DFC)

    def lambda_1E11():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E11)
    OP_68(26750, 1200, -12500, 800)
    SetCameraDistance(18000, 800)
    Sleep(300)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(500)
    Battle("BattleInfo_428", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    Call(0, 19)
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
    SetChrPos(0x0, 26650, 0, -14270, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE2, 1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_1BF3 end

    def Function_19_1ECB(): pass

    label("Function_19_1ECB")

    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xA, 26350, 0, -17110, 0)
    SetChrPos(0xB, 27830, 0, -18140, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Return()

    # Function_19_1ECB end

    def Function_20_1F46(): pass

    label("Function_20_1F46")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1710, 1100, -53910, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -550, 0, -49650, 180)
    SetChrPos(0x102, 550, 0, -49650, 180)
    SetChrPos(0x103, -550, 0, -48450, 180)
    SetChrPos(0x104, 550, 0, -48450, 180)
    SetChrPos(0x106, 0, 0, -47250, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, -2700, 0, -53930, 180)
    SetChrPos(0x12, -2700, 0, -55100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x3)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    OP_68(-890, 1100, -55040, 3000)

    def lambda_20B1():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20B1)
    Sleep(50)

    def lambda_20C9():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20C9)
    Sleep(50)

    def lambda_20E1():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20E1)
    Sleep(50)

    def lambda_20F9():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20F9)
    Sleep(50)

    def lambda_2111():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2111)
    Sleep(200)

    def lambda_2129():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2129)

    def lambda_213A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_213A)
    Sleep(100)

    def lambda_214E():

        label("loc_214E")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_214E")

    QueueWorkItem2(0x11, 1, lambda_214E)

    def lambda_2160():

        label("loc_2160")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2160")

    QueueWorkItem2(0x12, 1, lambda_2160)
    Sleep(400)

    def lambda_2175():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2175)

    def lambda_2186():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2186)
    Sleep(500)

    def lambda_219A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_219A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_21B3():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21B3)

    def lambda_21C0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_21C0)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_21D5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21D5)

    def lambda_21E2():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_21E2)
    WaitChrThread(0x106, 1)

    def lambda_21F3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_21F3)
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
    Sound(107, 0, 100, 0)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)

    #C0040
    ChrTalk(
        0x12,
        "#6Pおお、君たちは……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x11,
        "#6Pロイド君にランディさん！？\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#0002F#11Pエイダさん、無事でしたか。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        (
            "#0304F#11Pやれやれ……\x01",
            "患者も揃ってるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x12,
        (
            "#6P君たちが来たということは\x01",
            "マフィアたちは去ったのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#0003F#11Pいえ……まだです。\x02\x03",

            "#0001F現在、彼らを制圧しながら\x01",
            "皆さんの安全を確認している所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x11,
        (
            "#6Pそうなると……\x01",
            "私たちは下手にここから\x01",
            "動かない方がいいのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        "#0202F#11Pええ、そうしていただけると。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#0100F#11P病院内が完全に安全になるまで\x01",
            "私たちに任せてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x12,
        "#6P分かった、よろしく頼む。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F1")

    #C0050
    ChrTalk(
        0x11,
        (
            "#6P３階には個室の患者さんが\x01",
            "残っていると思うわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x11,
        (
            "#6Pセシルさんと\x01",
            "フィリアもいるはずだから\x01",
            "よろしくお願いするわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252B")

    label("loc_24F1")


    #C0052
    ChrTalk(
        0x11,
        (
            "#6Pこちらの心配はいらないわ。\x01",
            "くれぐれも気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252B")


    #C0053
    ChrTalk(
        0x101,
        "#0000F#11Pはい……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    SetChrPos(0x0, 0, 0, -54000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x11, 4940, 0, -54380, 0)
    SetChrPos(0x12, 4270, 0, -53810, 0)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    SetScenarioFlags(0xE2, 2)
    OP_29(0x4D, 0x1, 0x9)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_1F46 end

    def Function_21_25A9(): pass

    label("Function_21_25A9")

    TalkBegin(0xFF)
    SetChrName("")

    #A0054
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

    # Function_21_25A9 end

    SaveToFile()

Try(main)
