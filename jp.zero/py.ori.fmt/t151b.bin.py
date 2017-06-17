from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t151b.bin",                # FileName
        "t151b",                    # MapName
        "t151b",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 1, 0, 2],
    )

    BuildStringList((
        "t151b",                  # 0
        "マフィア",               # 1
        "マフィア",               # 2
        "マローネ",               # 3
        "バスの乗客",             # 4
        "バスの乗客",             # 5
        "バスの乗客",             # 6
        "バスの乗客",             # 7
        "バスの乗客",             # 8
        "マーサ師長",             # 9
        "キルシュ寮長",           # 10
        "警備員トニー",           # 11
        "バスの運転手",           # 12
        "外来患者",               # 13
        "外来患者",               # 14
        "bt152b",                 # 15
    ))

    ATBonus("ATBonus_328", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_368", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_400", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_408", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt152b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31103.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_368", "MonsterBattlePostion_3E8", "ed7402", "ed7403", "ATBonus_328"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "apl/ch50362.itc",                   # 02
        "apl/ch50363.itc",                   # 03
        "chr/ch25600.itc",                   # 04
        "chr/ch20400.itc",                   # 05
        "chr/ch22102.itc",                   # 06
        "chr/ch21000.itc",                   # 07
        "chr/ch27600.itc",                   # 08
        "chr/ch20300.itc",                   # 09
        "chr/ch29600.itc",                   # 0A
        "chr/ch24300.itc",                   # 0B
        "apl/ch50155.itc",                   # 0C
        "apl/ch50154.itc",                   # 0D
        "chr/ch20000.itc",                   # 0E
        "chr/ch22802.itc",                   # 0F
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(55459,   0,       -2079,   270,  261,  0x0, 0,   4,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(55909,   0,       1330,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(59330,   449,     -3049,   180,  341,  0x0, 0,   6,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(59130,   0,       -5159,   225,  261,  0x0, 0,   7,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(57900,   0,       -6389,   45,   261,  0x0, 0,   8,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(52869,   0,       -4570,   0,    261,  0x0, 0,   9,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(52490,   0,       51650,   0,    261,  0x0, 0,   10,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(60090,   0,       55479,   180,  261,  0x0, 0,   11,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(59909,   449,     53849,   90,   343,  0x0, 1,   12,  0,   255, 255, 0,   12,  255,  0)
    DeclNpc(52569,   449,     53849,   90,   343,  0x0, 1,   13,  0,   255, 255, 0,   13,  255,  0)
    DeclNpc(58209,   0,       50250,   270,  261,  0x0, 0,   14,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(52270,   449,     56560,   180,  341,  0x0, 0,   15,  0,   255, 255, 0,   15,  255,  0)

    DeclEvent(0x0000, 0, 22,  6.0,                   4.0,                   -0.5,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -3.0,                  -1.3333333730697632,   0.10000000894069672,   1.0])

    DeclActor(4390,    3750,    16900,   1000,    4390,    5000,    16900,   0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_4A8",          # 00, 0
        "Function_1_560",          # 01, 1
        "Function_2_5B5",          # 02, 2
        "Function_3_648",          # 03, 3
        "Function_4_678",          # 04, 4
        "Function_5_74E",          # 05, 5
        "Function_6_78A",          # 06, 6
        "Function_7_8F0",          # 07, 7
        "Function_8_975",          # 08, 8
        "Function_9_9C4",          # 09, 9
        "Function_10_A21",         # 0A, 10
        "Function_11_E72",         # 0B, 11
        "Function_12_FD4",         # 0C, 12
        "Function_13_1109",        # 0D, 13
        "Function_14_1178",        # 0E, 14
        "Function_15_11C8",        # 0F, 15
        "Function_16_12F1",        # 10, 16
        "Function_17_1351",        # 11, 17
        "Function_18_1851",        # 12, 18
        "Function_19_1D11",        # 13, 19
        "Function_20_1D8C",        # 14, 20
        "Function_21_2516",        # 15, 21
        "Function_22_2C68",        # 16, 22
    ))


    def Function_0_4A8(): pass

    label("Function_0_4A8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4E8"),
        (1, "loc_4F4"),
        (2, "loc_500"),
        (3, "loc_50C"),
        (4, "loc_518"),
        (5, "loc_524"),
        (6, "loc_530"),
        (SWITCH_DEFAULT, "loc_53C"),
    )


    label("loc_4E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_4F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_500")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_50C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_518")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_524")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_530")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_53C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_548")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_55F")

    Return()

    # Function_0_4A8 end

    def Function_1_560(): pass

    label("Function_1_560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57B")
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_5B4")

    label("loc_57B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59A")
    Event(0, 20)
    Jump("loc_5B4")

    label("loc_59A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B4")
    Event(0, 21)

    label("loc_5B4")

    Return()

    # Function_1_560 end

    def Function_2_5B5(): pass

    label("Function_2_5B5")

    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62A")
    Call(0, 19)

    label("loc_62A")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_647")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_647")

    Return()

    # Function_2_5B5 end

    def Function_3_648(): pass

    label("Function_3_648")

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

    # Function_3_648 end

    def Function_4_678(): pass

    label("Function_4_678")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F5")

    #C0002
    ChrTalk(
        0xFE,
        (
            "病棟側とは\x01",
            "全然連絡がつかない状態なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "事務長さんやセラさんたちは\x01",
            "無事なんでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_74A")

    label("loc_6F5")


    #C0004
    ChrTalk(
        0xFE,
        (
            "病棟側とは\x01",
            "全然連絡がつかない状態なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "事務長たちは無事でしょうか……\x02",
    )

    CloseMessageWindow()

    label("loc_74A")

    TalkEnd(0xFE)
    Return()

    # Function_4_678 end

    def Function_5_74E(): pass

    label("Function_5_74E")

    TalkBegin(0xFE)

    #C0006
    ChrTalk(
        0xFE,
        (
            "ちくしょう、\x01",
            "入院してる俺のダチは大丈夫かな……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_74E end

    def Function_6_78A(): pass

    label("Function_6_78A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81E")
    Jump("loc_868")

    label("loc_81E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_83E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_868")

    label("loc_83E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_868")

    label("loc_85E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_868")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0007
    ChrTalk(
        0xFE,
        "あなた達が来てくれて良かったわ……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "こんな所に押し込められて、\x01",
            "何をされるかと……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_78A end

    def Function_7_8F0(): pass

    label("Function_7_8F0")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        (
            "あ、あの黒服の連中……\x01",
            "目が普通じゃなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "まるで生気を感じないというか……\x01",
            "静かな恐ろしさというものを感じたよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_8F0 end

    def Function_8_975(): pass

    label("Function_8_975")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xFE,
        "くそっ……なんでこんな目に。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "僕が一体何をしたって言うんだ！？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_975 end

    def Function_9_9C4(): pass

    label("Function_9_9C4")

    TalkBegin(0xFE)

    #C0013
    ChrTalk(
        0xFE,
        "バスの運転手さん、大丈夫かしら……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "隣の部屋で治療を受けてるみたいだけど……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_9C4 end

    def Function_10_A21(): pass

    label("Function_10_A21")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 0)), scpexpr(EXPR_END)), "loc_B6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF1")

    #C0015
    ChrTalk(
        0xFE,
        (
            "おお、それはあたしが\x01",
            "黒服にふんだくられた鍵じゃないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "そいつがあれば\x01",
            "病棟に入ることができるはずさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "そっちは任せたよ。\x01",
            "セシルや患者さんたちを\x01",
            "助けてやってくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B66")

    label("loc_AF1")


    #C0018
    ChrTalk(
        0xFE,
        (
            "その鍵があれば\x01",
            "病棟に入ることができるはずさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "そっちは任せたよ。\x01",
            "セシルや患者さんたちを\x01",
            "助けてやってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B66")

    Jump("loc_E6E")

    label("loc_B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 5)), scpexpr(EXPR_END)), "loc_D43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7A")

    #C0020
    ChrTalk(
        0xFE,
        (
            "なに、病棟の入り口に\x01",
            "鍵がかかってた……？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "ちっ、あの黒服ども、\x01",
            "さては内側から閉めたね……！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "……病棟の鍵なら\x01",
            "あたしが持っていたんだが……\x01",
            "黒服に奪われちまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "鍵を持っている奴を探し出して\x01",
            "奪い返すしかないだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 1)
    SetScenarioFlags(0x0, 1)
    Jump("loc_D3E")

    label("loc_C7A")


    #C0024
    ChrTalk(
        0xFE,
        (
            "あたしの持っていた病棟の鍵は\x01",
            "黒服に奪われちまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "黒服はそのまま寮の階段を\x01",
            "上がっていったから、\x01",
            "多分まだ建物の中にいると思う……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "何とか探し出して\x01",
            "鍵を奪い返すしかないだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3E")

    Jump("loc_E6E")

    label("loc_D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2A")

    #C0027
    ChrTalk(
        0xFE,
        (
            "あの黒服ども……\x01",
            "うちの職員と患者にヒドいことを\x01",
            "してくれたもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "あたしも必死で抵抗したんだが、\x01",
            "あっけなくぶっ倒されちまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "……病棟の方は任せたよ。\x01",
            "セシルや患者さんたちを\x01",
            "助けてやっとくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E6E")

    label("loc_E2A")


    #C0030
    ChrTalk(
        0xFE,
        (
            "病棟の方は任せたよ。\x01",
            "セシルや患者さんたちを\x01",
            "助けてやっとくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6E")

    TalkEnd(0xFE)
    Return()

    # Function_10_A21 end

    def Function_11_E72(): pass

    label("Function_11_E72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3F")
    TurnDirection(0xFE, 0x12, 0)

    #C0031
    ChrTalk(
        0xFE,
        "ほれ、トニーさんしっかりおし！\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "あんたがいたおかげで\x01",
            "運転手さんが２発撃たれずに\x01",
            "済んだと思いなさいな！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "幸い２人とも命に別状は無いんだ、\x01",
            "心を強く持たなきゃダメよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_FD0")

    label("loc_F3F")


    #C0034
    ChrTalk(
        0xFE,
        (
            "ああ、困ったねぇ。\x01",
            "ここじゃ設備が足りないから\x01",
            "応急処置程度しかできないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "他の患者さんも熱を出しちゃったし、\x01",
            "人手も全然足りないわ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD0")

    TalkEnd(0xFE)
    Return()

    # Function_11_E72 end

    def Function_12_FD4(): pass

    label("Function_12_FD4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AC")

    #C0036
    ChrTalk(
        0xFE,
        (
            "……や、やぁ……\x01",
            "こんな時に病院に来ちゃうなんて\x01",
            "君たちもついてないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "そっちの運転手さんは\x01",
            "僕と一緒に奴らに抵抗して\x01",
            "撃たれてしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "……くそっ！\x01",
            "何のための警備員だよ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1105")

    label("loc_10AC")


    #C0039
    ChrTalk(
        0xFE,
        (
            "僕は警備員なのに……\x01",
            "簡単に奴らの侵入を許してしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "自分が不甲斐ないよ……\x02",
    )

    CloseMessageWindow()

    label("loc_1105")

    TalkEnd(0xFE)
    Return()

    # Function_12_FD4 end

    def Function_13_1109(): pass

    label("Function_13_1109")

    TalkBegin(0xFE)

    #C0041
    ChrTalk(
        0xFE,
        (
            "痛つっ！　……\x01",
            "……うぅ、まさか撃たれるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "銃口を向けられた時は\x01",
            "もう駄目かと思った……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1109 end

    def Function_14_1178(): pass

    label("Function_14_1178")

    TalkBegin(0xFE)

    #C0043
    ChrTalk(
        0xFE,
        (
            "……夕方に診察を予約したばっかりに\x01",
            "こんなことに巻き込まれるとは……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1178 end

    def Function_15_11C8(): pass

    label("Function_15_11C8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_125C")
    Jump("loc_12A6")

    label("loc_125C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_127C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12A6")

    label("loc_127C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_129C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12A6")

    label("loc_129C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12A6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0044
    ChrTalk(
        0xFE,
        "これは夢だ、夢なんだ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_11C8 end

    def Function_16_12F1(): pass

    label("Function_16_12F1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "３階：女性職員寮→\x01\x01",
            "←２階：男性職員寮\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_12F1 end

    def Function_17_1351(): pass

    label("Function_17_1351")

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
    OP_68(-7450, 1000, 12750, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 0, 0, -1300, 0)
    SetChrPos(0x102, 600, 50, -2800, 0)
    SetChrPos(0x103, -600, 50, -2800, 0)
    SetChrPos(0x104, -600, 0, -4300, 0)
    SetChrPos(0x106, 600, 0, -4300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, 6500, 0, 9500, 180)
    SetChrPos(0x9, 4500, 0, 9500, 180)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_68(1750, 1000, 4550, 7000)
    Sleep(3000)

    def lambda_14D5():
        OP_95(0xFE, 0, 0, 3700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14D5)

    def lambda_14EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14EF)
    Sleep(50)

    def lambda_1503():
        OP_95(0xFE, 600, 50, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1503)

    def lambda_151D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_151D)
    Sleep(50)

    def lambda_1531():
        OP_95(0xFE, -600, 50, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1531)

    def lambda_154B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_154B)
    Sleep(50)

    def lambda_155F():
        OP_95(0xFE, -600, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_155F)

    def lambda_1579():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1579)
    Sleep(50)

    def lambda_158D():
        OP_95(0xFE, 600, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_158D)

    def lambda_15A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_15A7)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_15F1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_15F1)
    Sleep(50)

    def lambda_1601():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_1601)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    def lambda_162A():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_162A)

    def lambda_1637():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1637)

    def lambda_1644():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_1644)
    Sleep(100)

    def lambda_1654():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_1654)

    def lambda_1661():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_1661)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x106, 3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_6F(0x79)
    OP_0D()

    #C0046
    ChrTalk(
        0x101,
        "#0013F#6Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        "#0301F#6P早速いやがったか……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0050
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#12Pフ……問答無用か。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
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
    Sleep(300)

    #C0051
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0107F#6P来るわ……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)

    def lambda_17E7():
        OP_95(0xFE, 3650, 0, 6040, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17E7)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)

    def lambda_1809():
        OP_95(0xFE, 2009, 0, 6190, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1809)
    Sleep(500)
    Battle("BattleInfo_408", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    Call(0, 18)
    Return()

    # Function_17_1351 end

    def Function_18_1851(): pass

    label("Function_18_1851")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    OP_68(-280, 1100, 3650, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, -440, 0, 5250, 90)
    SetChrPos(0x102, -1750, 0, 5720, 90)
    SetChrPos(0x103, -2900, 0, 3020, 90)
    SetChrPos(0x104, -1020, 0, 3310, 90)
    SetChrPos(0x106, -3540, 0, 4380, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
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
    Call(0, 19)
    FadeToBright(1000, 0)
    SetCameraDistance(26500, 2000)
    OP_6F(0x10)
    OP_0D()
    Fade(250)
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
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0052
    ChrTalk(
        0x104,
        (
            "#0303F#6Pチッ……\x01",
            "手こずらせやがって。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        (
            "#0203F#6Pやはり感情のゆらぎが\x01",
            "殆んど感じられませんでした……\x02\x03",

            "#0208Fひょっとしたら自分の意志で\x01",
            "動いていないのかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1A72():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A72)
    Sleep(50)

    def lambda_1A82():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1A82)
    Sleep(50)

    def lambda_1A92():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A92)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0054
    ChrTalk(
        0x102,
        (
            "#0105F#5Pじ、自分の意志で\x01",
            "動いていない……？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#0013F#5Pそれは……\x01",
            "操られているという事か？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(150)

    #C0056
    ChrTalk(
        0x103,
        "#0206F#6Pはい……断言はできませんが。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P東方には薬物と暗示を利用した\x01",
            "“傀儡の術”なども存在する。\x02\x03",

            "その可能性はあり得るだろう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        "#0106F#5Pし、信じられない……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#0306F#11Pけったくそ悪ぃ話だな……\x02\x03",

            "#0301Fしかしこりゃあ、どう考えても\x01",
            "ガルシアのオッサンの流儀じゃねえぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0003F#5Pああ……分かってる。\x02\x03",

            "#0013Fとにかく今は、病院関係者の\x01",
            "安全を確認する方が先決だ。\x02\x03",

            "まずはこの宿泊施設の\x01",
            "内部を調べてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#0101F#5Pええ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    SetChrPos(0x0, 0, 0, 4000, 0)
    SetScenarioFlags(0xE0, 4)
    EventEnd(0x5)
    Return()

    # Function_18_1851 end

    def Function_19_1D11(): pass

    label("Function_19_1D11")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
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
    SetChrPos(0x8, 2940, 0, 3630, 225)
    SetChrPos(0x9, 2480, 0, 5210, 315)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_19_1D11 end

    def Function_20_1D8C(): pass

    label("Function_20_1D8C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(57230, 1100, -1820, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19870, 0)
    OP_93(0xA, 0x5A, 0x0)
    SetChrPos(0x101, 47720, 0, 0, 90)
    SetChrPos(0x102, 46520, 0, 600, 90)
    SetChrPos(0x103, 46520, 0, -600, 90)
    SetChrPos(0x104, 45320, 0, -600, 90)
    SetChrPos(0x106, 45320, 0, 600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(55230, 1100, -1820, 4000)

    def lambda_1E82():
        OP_95(0xFE, 52720, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E82)

    def lambda_1E9C():
        OP_95(0xFE, 51520, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E9C)

    def lambda_1EB6():
        OP_95(0xFE, 51520, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1EB6)

    def lambda_1ED0():
        OP_95(0xFE, 50320, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1ED0)

    def lambda_1EEA():
        OP_95(0xFE, 50320, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1EEA)
    Sleep(1000)

    def lambda_1F07():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F07)
    Sleep(500)

    def lambda_1F1B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1F1B)

    def lambda_1F2C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1F2C)
    Sleep(500)

    def lambda_1F40():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1F40)

    def lambda_1F51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1F51)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xA, 500)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2031():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2031)
    SetChrSubChip(0xC, 0x2)
    Sleep(50)

    def lambda_2045():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2045)

    def lambda_2052():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2052)
    Sleep(50)

    def lambda_2062():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2062)

    def lambda_206F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_206F)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xA, 1)

    #N0062
    NpcTalk(
        0xB,
        "若い男性",
        "#5Pひっ……！？\x02",
    )

    CloseMessageWindow()

    #N0063
    NpcTalk(
        0xD,
        "中年男性",
        "#11Pな、なんだアンタら……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2102")

    #C0064
    ChrTalk(
        0x101,
        "#0005F#6Pあなた方は……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2134")

    label("loc_2102")


    #C0065
    ChrTalk(
        0x101,
        (
            "#0002F#6Pよかった……\x01",
            "そちらも無事でしたか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2134")

    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0066
    ChrTalk(
        0xA,
        (
            "#11Pあなたたち……\x01",
            "たしか警察の人じゃ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#0003F#6Pええ、クロスベル警察の者です。\x02\x03",

            "#0000Fこちらの異変に気づいて\x01",
            "皆さんの安全を確認しに来ました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0068
    NpcTalk(
        0xC,
        "若い女性",
        "#5Pた、助かったわ！\x02",
    )

    CloseMessageWindow()

    #N0069
    NpcTalk(
        0xE,
        "スーツの男性",
        (
            "#11Pバスから引きずり出された時は\x01",
            "どうなることかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#0301F#6P#Nあんたら、途中で停まってた\x01",
            "バスに乗っていたのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0071
    ChrTalk(
        0xD,
        "#11Pああ……\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xD,
        (
            "#11P道の途中で、いきなりあの\x01",
            "黒服たちが立ち塞がったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xB,
        (
            "#5Pむ、無言で銃を突きつけられて\x01",
            "ここまで歩かされて……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "#5P抵抗しようとした運転手さんは\x01",
            "い、いきなり撃たれて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        "#0106F#6Pそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#0003F#6P……しばらくの間、\x01",
            "ここで待っていてください。\x02\x03",

            "#0001F皆さんの安全は\x01",
            "自分たちが必ず確保します。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xB,
        "#5Pわ、分かった！\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xC,
        "#5Pよろしく頼んだわよ！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 50500, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_93(0xB, 0x0, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_93(0xD, 0xE1, 0x0)
    OP_93(0xE, 0x2D, 0x0)
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0xE0, 5)
    OP_29(0x4D, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_20_1D8C end

    def Function_21_2516(): pass

    label("Function_21_2516")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(56470, 700, 54520, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(23870, 0)
    SetChrPos(0x101, 48100, 0, 50000, 90)
    SetChrPos(0x102, 46900, 0, 50600, 90)
    SetChrPos(0x103, 46900, 0, 49400, 90)
    SetChrPos(0x104, 45700, 0, 50600, 90)
    SetChrPos(0x106, 45700, 0, 49400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 56000, 0, 54040, 180)
    SetChrPos(0x11, 56000, 0, 52770, 0)
    FadeToBright(1000, 0)
    OP_68(54450, 700, 52500, 3000)
    Sleep(150)

    def lambda_262A():
        OP_95(0xFE, 53100, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_262A)

    def lambda_2644():
        OP_95(0xFE, 51900, 0, 50600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2644)

    def lambda_265E():
        OP_95(0xFE, 51900, 0, 49400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_265E)

    def lambda_2678():
        OP_95(0xFE, 50700, 0, 50600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2678)

    def lambda_2692():
        OP_95(0xFE, 50700, 0, 49400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2692)
    Sleep(1000)

    def lambda_26AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26AF)
    Sleep(500)

    def lambda_26C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_26C3)

    def lambda_26D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_26D4)
    Sleep(500)

    def lambda_26E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_26E8)

    def lambda_26F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_26F9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    def lambda_271E():
        TurnDirection(0xFE, 0x10, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_271E)

    def lambda_272B():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_272B)

    def lambda_2738():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_2738)
    Sleep(100)

    def lambda_2748():
        TurnDirection(0xFE, 0x10, 300)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_2748)

    def lambda_2755():
        TurnDirection(0xFE, 0x10, 300)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_2755)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x106, 3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_6F(0x1)
    OP_0D()
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2805():
        TurnDirection(0xFE, 0x101, 600)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2805)
    Sleep(30)

    def lambda_2815():
        TurnDirection(0xFE, 0x101, 600)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2815)
    Sleep(300)

    #C0079
    ChrTalk(
        0x10,
        "#5Pあんたたち……！？\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x11,
        "#11Pたしか警察の……！\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0002F#12P師長さん……\x01",
            "ご無事でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        "#0202F#12P……よかった……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x10,
        "#5Pどうしてここに……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x10,
        (
            "#5Pひょっとして、\x01",
            "もう安全なのかい！？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#0106F#6Pいえ……私たちも\x01",
            "先ほど来たばかりなんです。\x02\x03",

            "#0101F現在、安全を確認しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x10,
        "#5Pそうかい……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#0301F#6Pどうやらケガをしてる人が\x01",
            "いるみたいッスね？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x10,
        (
            "#5Pああ……\x01",
            "ウチの警備員とバスの運転手さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x10,
        (
            "#5Pあの黒服たちに撃たれて……\x01",
            "一応、応急手当ては済ませたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#0006F#12Pそうですか……\x02\x03",

            "#0001Fセシル姉や他の人たちは\x01",
            "やはり病棟の方でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x10,
        (
            "#5Pああ、ちょうど仕事中だったし、\x01",
            "かなりの人間が病棟にいるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x10,
        (
            "#5Pあたしは丁度休憩中で\x01",
            "こっちに来ていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x10,
        (
            "#5Pくっ、こんな大変な時に\x01",
            "病棟から離れちまうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        "#0208F#12P師長さん……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#0003F#12P……安心してください。\x02\x03",

            "#0013Fセシル姉や患者さんたちは\x01",
            "俺たちが絶対に助けます！\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        (
            "#0101F#6P師長さんたちは\x01",
            "どうかケガをされた方を\x01",
            "診ていてあげてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x10,
        "#5P判った……よろしく頼むよ！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 50500, 0, 50000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10, 52490, 0, 51650, 0)
    SetChrPos(0x11, 60090, 0, 55480, 180)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x14, 0xFF)
    SetScenarioFlags(0xE0, 6)
    OP_29(0x4D, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_21_2516 end

    def Function_22_2C68(): pass

    label("Function_22_2C68")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CE8")

    #C0098
    ChrTalk(
        0x101,
        (
            "#0001Fさっきのマフィアたちは\x01",
            "１階の宿泊施設を\x01",
            "守っていたみたいだ。\x02\x03",

            "まずはそっちを調べてみよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D32")

    label("loc_2CE8")


    #C0099
    ChrTalk(
        0x101,
        (
            "#0001F……宿泊施設は\x01",
            "もう一部屋あったはずだ。\x01",
            "そっちも調べてみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D32")

    Sleep(50)
    SetChrPos(0x0, 4059, 0, 3600, 270)
    EventEnd(0x4)
    Return()

    # Function_22_2C68 end

    SaveToFile()

Try(main)
