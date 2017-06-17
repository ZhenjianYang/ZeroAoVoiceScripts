from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t121b.bin",                # FileName
        "t121b",                    # MapName
        "t121b",                    # Location
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
        "t121b",                  # 0
        "執事コーエン",           # 1
        "黒服",                   # 2
        "マフィア",               # 3
        "マフィア",               # 4
        "マフィア",               # 5
        "マフィア",               # 6
        "マフィア",               # 7
        "マフィア",               # 8
        "レクター",               # 9
        "エリザベート",           # 10
        "声",                     # 11
        "銀",                     # 12
        "bt113b",                 # 13
    ))

    ATBonus("ATBonus_3B8", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_3F8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_45C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_460", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_464", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_468", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_46C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_470", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_478", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt113b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31002.dat", "ms31102.dat", "ms31102.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F8", "MonsterBattlePostion_458", "ed7509", "ed7000", "ATBonus_3B8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch25900.itc",                   # 00
        "chr/ch36000.itc",                   # 01
        "apl/ch50362.itc",                   # 02
        "apl/ch50363.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch07400.itc",                   # 05
        "chr/ch39100.itc",                   # 06
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

    DeclNpc(-58000,  0,       -49500,  180,  261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(58000,   0,       -49500,  180,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(60700,   0,       2400,    0,    389,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(63099,   0,       4000,    315,  389,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(63099,   0,       4000,    315,  389,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(58000,   0,       -55500,  0,    389,  0x0, 3,   2,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(58000,   0,       -56500,  0,    389,  0x0, 3,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(58000,   0,       -57500,  0,    389,  0x0, 3,   4,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-54029,  0,       6579,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-52930,  0,       6579,    270,  389,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 13,  58.0,                  -57.5,                 -1.0,                  56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -11.600000381469727,   19.166667938232422,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 14,  58.0,                  -57.5,                 -1.0,                  56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -11.600000381469727,   19.166667938232422,    0.20000000298023224,   1.0])

    DeclActor(55540,   0,       6000,    2500,    55540,   1500,    6000,    0x007C, 0,  8,  0x0000)
    DeclActor(-57850,  0,       4860,    2500,    -57850,  1500,    4860,    0x007C, 0,  8,  0x0000)
    DeclActor(55540,   0,       1500,    2500,    55540,   1500,    1500,    0x007C, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_540",          # 00, 0
        "Function_1_5F8",          # 01, 1
        "Function_2_68C",          # 02, 2
        "Function_3_7C6",          # 03, 3
        "Function_4_A3C",          # 04, 4
        "Function_5_A8C",          # 05, 5
        "Function_6_C8A",          # 06, 6
        "Function_7_E17",          # 07, 7
        "Function_8_E32",          # 08, 8
        "Function_9_ED7",          # 09, 9
        "Function_10_F14",         # 0A, 10
        "Function_11_FCC",         # 0B, 11
        "Function_12_1084",        # 0C, 12
        "Function_13_13AF",        # 0D, 13
        "Function_14_1B5C",        # 0E, 14
        "Function_15_21DB",        # 0F, 15
        "Function_16_2EFC",        # 10, 16
        "Function_17_2F5D",        # 11, 17
        "Function_18_2FBE",        # 12, 18
        "Function_19_301F",        # 13, 19
        "Function_20_348E",        # 14, 20
        "Function_21_3834",        # 15, 21
        "Function_22_3878",        # 16, 22
        "Function_23_389E",        # 17, 23
        "Function_24_51F5",        # 18, 24
        "Function_25_524A",        # 19, 25
        "Function_26_528F",        # 1A, 26
        "Function_27_52D4",        # 1B, 27
        "Function_28_530B",        # 1C, 28
        "Function_29_5349",        # 1D, 29
        "Function_30_538D",        # 1E, 30
        "Function_31_53D1",        # 1F, 31
        "Function_32_5415",        # 20, 32
    ))


    def Function_0_540(): pass

    label("Function_0_540")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_580"),
        (1, "loc_58C"),
        (2, "loc_598"),
        (3, "loc_5A4"),
        (4, "loc_5B0"),
        (5, "loc_5BC"),
        (6, "loc_5C8"),
        (SWITCH_DEFAULT, "loc_5D4"),
    )


    label("loc_580")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_58C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_598")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5A4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5B0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5BC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5F7")

    Return()

    # Function_0_540 end

    def Function_1_5F8(): pass

    label("Function_1_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_END)), "loc_61A")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_657")

    label("loc_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_632")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_657")

    label("loc_632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_640")
    Jump("loc_657")

    label("loc_640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_64E")
    Jump("loc_657")

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_657")

    label("loc_657")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_671")
    Event(0, 19)

    label("loc_671")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68B")
    Event(0, 23)

    label("loc_68B")

    Return()

    # Function_1_5F8 end

    def Function_2_68C(): pass

    label("Function_2_68C")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A9")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BC")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E4")
    Call(0, 9)

    label("loc_6E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_END)), "loc_707")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_707")
    Call(0, 10)

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_72A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_72A")
    Call(0, 11)

    label("loc_72A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_END)), "loc_754")
    SetMapObjFrame(0xFF, "mado_a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mado_b", 0x1, 0x1)
    Jump("loc_770")

    label("loc_754")

    SetMapObjFrame(0xFF, "mado_a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mado_b", 0x0, 0x1)

    label("loc_770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_779")

    label("loc_779")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_791")
    OP_1B(0x2, 0x0, 0x20)

    label("loc_791")

    SetMapObjFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AB")
    ClearMapObjFlags(0x8, 0x10)

    label("loc_7AB")

    SetMapObjFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C5")
    ClearMapObjFlags(0x9, 0x10)

    label("loc_7C5")

    Return()

    # Function_2_68C end

    def Function_3_7C6(): pass

    label("Function_3_7C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DC")
    Call(0, 12)
    Jump("loc_A3B")

    label("loc_7DC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_7ED")
    Jump("loc_A38")

    label("loc_7ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_867")

    #C0001
    ChrTalk(
        0xFE,
        (
            "主人はマルコーニ会長と\x01",
            "競売会の段取りについて\x01",
            "最終確認をしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "どうかお静かにお願いします。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A38")

    label("loc_867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_8FE")

    #C0003
    ChrTalk(
        0xFE,
        (
            "こちらは当館の主人、\x01",
            "ハルトマン議長閣下の\x01",
            "居室になっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "オークション開始はもうすぐです。\x01",
            "会場のほうにお急ぎください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A38")

    label("loc_8FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_A38")

    #C0005
    ChrTalk(
        0xFE,
        (
            "こちらは当館の主人、\x01",
            "ハルトマン議長閣下の\x01",
            "居室になっております。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_9CA")

    #C0006
    ChrTalk(
        0xFE,
        (
            "只今でしたら、\x01",
            "主人は１階左手にある\x01",
            "サロンにいるかと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "御用がおありでしたら\x01",
            "どうぞそちらへ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A38")

    label("loc_9CA")


    #C0008
    ChrTalk(
        0xFE,
        (
            "主人は１階左手にある\x01",
            "サロンに向かう準備をしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "御用がおありでしたら\x01",
            "そちらでお待ちください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A38")

    TalkEnd(0x8)

    label("loc_A3B")

    Return()

    # Function_3_7C6 end

    def Function_4_A3C(): pass

    label("Function_4_A3C")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "完全に気を失っているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_4_A3C end

    def Function_5_A8C(): pass

    label("Function_5_A8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_A9D")
    Jump("loc_C86")

    label("loc_A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_AAB")
    Jump("loc_C86")

    label("loc_AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_B23")

    #C0012
    ChrTalk(
        0xFE,
        (
            "失礼ですが……\x01",
            "こちらにおられると\x01",
            "商品の運搬の妨げになります。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "どうか会場で静かにお待ち下さい。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C86")

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_C86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2C")

    #C0014
    ChrTalk(
        0xFE,
        "……お客様、まだ何か？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#5100Fああ、いや……\x01",
            "なんでもないんだ。\x02\x03",

            "#5108F（……さっきの声は一体……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0016
    ChrTalk(
        0xFE,
        (
            "……出品物は開場まで\x01",
            "非公開となっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "オークションで出品されるのを\x01",
            "お待ちください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C86")

    label("loc_C2C")


    #C0018
    ChrTalk(
        0xFE,
        (
            "出品物は開場まで非公開となっています。\x01",
            "オークションで出品されるのを\x01",
            "お待ちください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C86")

    TalkEnd(0xFE)
    Return()

    # Function_5_A8C end

    def Function_6_C8A(): pass

    label("Function_6_C8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8D")

    #C0019
    ChrTalk(
        0x10,
        (
            "#3505Fおおっと、\x01",
            "裏庭に行ったはずの連中が\x01",
            "まだこんなトコにいやがるぜェ。\x02\x03",

            "#3502Fモタモタしてていいのかなァ～？\x02",
        )
    )

    CloseMessageWindow()

    #N0020
    NpcTalk(
        0x101,
        "キーア",
        "#5810F#Nヘンなヒト、またね！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x10,
        (
            "#3504Fはいはい、あ～ばよ。\x02\x03",

            "#3501F……って、ヘンなヒトは\x01",
            "流石にヒドくない？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E13")

    label("loc_D8D")

    OP_4B(0x11, 0xFF)
    TurnDirection(0xFE, 0x11, 0)

    #C0022
    ChrTalk(
        0x10,
        (
            "#3509F部屋の主はいねぇみたいだし、\x01",
            "存分に遊べるなぁ、クロ。\x02\x03",

            "#3507Fよっしゃ、缶蹴りでもするか！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x11,
        "にゃおおん？\x02",
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)

    label("loc_E13")

    TalkEnd(0xFE)
    Return()

    # Function_6_C8A end

    def Function_7_E17(): pass

    label("Function_7_E17")

    TalkBegin(0xFE)

    #C0024
    ChrTalk(
        0xFE,
        "ごろにゃーん。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_E17 end

    def Function_8_E32(): pass

    label("Function_8_E32")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB9")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_EB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED5")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_ED5")

    Return()

    # Function_8_E32 end

    def Function_9_ED7(): pass

    label("Function_9_ED7")

    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 58930, 0, -51280, 0)
    Return()

    # Function_9_ED7 end

    def Function_10_F14(): pass

    label("Function_10_F14")

    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, 59800, 0, 1810, 0)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xB, 58650, 0, 3490, 45)
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, 64230, 0, 4180, 315)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xC, 0x10)
    Return()

    # Function_10_F14 end

    def Function_11_FCC(): pass

    label("Function_11_FCC")

    SetChrChipByIndex(0xD, 0x3)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xD, 58290, 0, -55060, 45)
    SetChrChipByIndex(0xE, 0x3)
    SetChrSubChip(0xE, 0x1)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x1)
    SetChrPos(0xE, 59250, 0, -56490, 180)
    SetChrChipByIndex(0xF, 0x3)
    SetChrSubChip(0xF, 0x1)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0xF, 0x1)
    SetChrPos(0xF, 56290, 0, -58070, 135)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xF, 0x10)
    Return()

    # Function_11_FCC end

    def Function_12_1084(): pass

    label("Function_12_1084")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(-57790, 1200, -50440, 0)
    MoveCamera(315, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18290, 0)
    SetChrPos(0x101, -57400, 0, -51000, 0)
    SetChrPos(0xEF, -58600, 0, -51000, 0)
    OP_0D()

    #C0025
    ChrTalk(
        0x8,
        "#11Pお客様、申し訳ありません。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#11Pこちらは当館の主人の\x01",
            "居室になっておりまして。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0027
    ChrTalk(
        0x101,
        (
            "#5105F#6Pという事は……\x01",
            "ハルトマン議長閣下の？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "#11Pはい、その通りでございます。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_125A")

    #C0029
    ChrTalk(
        0x8,
        "#11Pただ生憎、主人は不在でして。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#11P今でしたら、１階左手にある\x01",
            "サロンにいるかと思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#5100F#6Pああ、さっき見かけたよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12FF")

    label("loc_125A")


    #C0032
    ChrTalk(
        0x8,
        (
            "#11Pそろそろ１階左手にある\x01",
            "サロンに向かうかと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#11P主人に御用がおありでしたら、\x01",
            "そちらでお待ちいただけると……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#5100F#6Pそうか、分かったよ。\x02",
    )

    CloseMessageWindow()

    label("loc_12FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1332")

    #C0035
    ChrTalk(
        0x102,
        "#5302F#6Pふふ、お邪魔しました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1391")

    label("loc_1332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1363")

    #C0036
    ChrTalk(
        0x103,
        "#5404F#6P……お邪魔しました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1391")

    label("loc_1363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1391")

    #C0037
    ChrTalk(
        0x104,
        "#5609F#6Pそんじゃ、邪魔したな。\x02",
    )

    CloseMessageWindow()

    label("loc_1391")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -58000, 0, -51500, 180)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xA5, 7)
    EventEnd(0x5)
    Return()

    # Function_12_1084 end

    def Function_13_13AF(): pass

    label("Function_13_13AF")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(1000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, 58000, 0, -48500, 0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(58220, 1100, -52980, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19200, 0)
    SetChrPos(0x101, 57410, 0, -62690, 0)
    SetChrPos(0xEF, 58150, 0, -63610, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis064.itp")

    def lambda_1461():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1461)

    def lambda_1476():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1476)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(58220, 1100, -53580, 1800)

    def lambda_14B2():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_14B2)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x9,
        (
            "#5P──お客様。\x01",
            "申しわけありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "#5Pこちらはスタッフ専用の\x01",
            "部屋になっておりまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#5106F#12Pああ、それは失礼。\x01",
            "広すぎて迷ったみたいだ。\x02\x03",

            "#5108F（マフィアが詰めている\x01",
            "  待機場所って所か……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(58220, 1100, -51980, 1800)
    OP_6F(0x1)

    #N0041
    NpcTalk(
        0x12,
        "男の声",
        (
            "#2P#2Sおい、ちゃんとリスト通りに\x01",
            "揃っているんだろうな！？\x02",
        )
    )

    CloseMessageWindow()

    #N0042
    NpcTalk(
        0x12,
        "男の声",
        (
            "#5P#2Sああ、前半の出品物は\x01",
            "そろそろ会場に運び出すぞ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x9,
        "#11Pちっ、アイツら……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#5105F#12Pひょっとして……\x01",
            "出品物はそちらの方に？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(58220, 1100, -53580, 1200)
    OP_93(0x9, 0xB4, 0x190)
    OP_6F(0x1)

    #C0045
    ChrTalk(
        0x9,
        (
            "#5Pえ、ええ。\x01",
            "万が一のことが無いよう\x01",
            "我々で保管をしております。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "#5Pオークションで出品されるのを\x01",
            "楽しみにして頂けると。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#5104F#12P……ああ。\x01",
            "もちろん期待しているよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    #C0048
    ChrTalk(
        0x101,
        "#5100F#5P──それじゃあ戻ろうか。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1847")

    #C0049
    ChrTalk(
        0x102,
        "#5302F#11Pええ、判ったわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A4")

    label("loc_1847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1877")

    #C0050
    ChrTalk(
        0x103,
        "#5402F#11P……はい、兄さま。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A4")

    label("loc_1877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_18A4")

    #C0051
    ChrTalk(
        0x104,
        "#5602F#11Pおお、行くとするか。\x02",
    )

    CloseMessageWindow()

    label("loc_18A4")


    def lambda_18A9():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18A9)

    def lambda_18B6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_18B6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    Fade(1000)
    OP_68(58390, 1100, -58100, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18240, 0)
    OP_68(58390, 1100, -60100, 3000)

    def lambda_190F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_190F)

    def lambda_1924():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1924)
    Sleep(2000)
    OP_0D()
    OP_C7(0x0, 0x800)
    VolumeBGM(0x28, 0x1F4)
    FadeToDark(500, 0, -1)
    Sound(915, 0, 100, 0)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(200)
    Sound(2179, 255, 75, 0)    #voice#KeA
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    FadeToBright(500, 0)
    SetChrSubChip(0x101, 0x0)

    def lambda_19A1():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_19A1)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    OP_C7(0x1, 0x800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    OP_4B(0xEF, 0xFF)
    Sleep(500)
    OP_93(0xEF, 0x0, 0x1F4)

    #C0052
    ChrTalk(
        0x101,
        "#5111F#5Pえ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    OP_63(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1A4C")

    #C0053
    ChrTalk(
        0x102,
        "#5305F#12P（……ロイド？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AB1")

    label("loc_1A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1A7E")

    #C0054
    ChrTalk(
        0x103,
        "#5405F#12P（……ロイドさん？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AB1")

    label("loc_1A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1AB1")

    #C0055
    ChrTalk(
        0x104,
        "#5605F#12P（……なんだ、どうした？）\x02",
    )

    CloseMessageWindow()

    label("loc_1AB1")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0056
    ChrTalk(
        0x101,
        (
            "#5106F#5P（いや……\x01",
            "  ゴメン、何でもない。）\x02\x03",

            "#5101F（早くここを離れよう。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    OP_4C(0x9, 0xFF)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetScenarioFlags(0xA6, 0)
    OP_29(0x47, 0x1, 0xA)
    EventEnd(0x5)
    NewScene("t119B", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_13_13AF end

    def Function_14_1B5C(): pass

    label("Function_14_1B5C")

    EventBegin(0x2)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch31150.itc", 0x1E)
    LoadChrToIndex("chr/ch31151.itc", 0x1F)
    LoadChrToIndex("chr/ch31050.itc", 0x21)
    LoadChrToIndex("chr/ch31051.itc", 0x22)
    LoadChrToIndex("chr/ch00500.itc", 0x24)
    LoadChrToIndex("apl/ch50364.itc", 0x25)
    LoadChrToIndex("chr/ch31100.itc", 0x26)
    LoadChrToIndex("chr/ch31000.itc", 0x27)
    LoadChrToIndex("chr/ch00550.itc", 0x28)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 58810, 0, -53260, 0)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 61240, 0, 1290, 0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 63510, 0, 4260, 315)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 60110, 0, 2400, 0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 60800, 0, 6500, 180)
    SetChrPos(0x101, 58000, 0, -59000, 0)
    SetChrPos(0xEF, 58700, 0, -60000, 0)
    SetChrPos(0x151, 57300, 0, -60500, 0)
    SetChrPos(0x9, 58930, 0, -51280, 0)
    OP_68(57900, 1500, -60140, 0)
    MoveCamera(60, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18330, 0)
    FadeToBright(1000, 0)
    OP_68(57900, 1500, -58090, 1200)
    OP_6F(0x1)
    OP_0D()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(57900, 1300, -52450, 2000)
    SetCameraDistance(17330, 2000)

    def lambda_1D5B():
        OP_95(0xFE, 58340, 0, -52690, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D5B)
    Sleep(100)

    def lambda_1D78():
        OP_95(0xFE, 59000, 0, -53630, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1D78)
    Sleep(100)

    def lambda_1D95():
        OP_95(0xFE, 57030, 0, -53980, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1D95)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x151, 1)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    #C0057
    ChrTalk(
        0x101,
        "#5110F#11P駄目だ、気絶している……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x151,
        (
            "#5700F#12Pへえ、どうやら一撃で\x01",
            "昏倒させられたみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1E6A")

    #C0059
    ChrTalk(
        0x102,
        "#5301F#12Pこ、こんな事ができるのは……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EDB")

    label("loc_1E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1EA4")

    #C0060
    ChrTalk(
        0x103,
        "#5401F#12P……こんな事ができるのは……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EDB")

    label("loc_1EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1EDB")

    #C0061
    ChrTalk(
        0x104,
        "#5601F#12Pチッ、こんな事ができんのは……\x02",
    )

    CloseMessageWindow()

    label("loc_1EDB")


    #C0062
    ChrTalk(
        0x101,
        "#5113F#11P……とにかく中に入ろう！\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00700.itp")
    OP_68(61440, 1200, 3040, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19300, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0x13, 0x28)
    SetChrSubChip(0x13, 0x0)
    FadeToBright(1000, 0)
    OP_68(61440, 1200, 5040, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0063
    ChrTalk(
        0xA,
        "#12Pて、てめえ……！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        "#2Pいつの間に現れやがった……！\x02",
    )

    CloseMessageWindow()
    #Sound(1628, 255, 100, 0)    #voice#Yin
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0065
    AnonymousTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "フフ……我が名は《銀#2Rイン#》。\x02\x03",

            "月の光さす所ならば\x01",
            "どこへでも現れよう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0066
    ChrTalk(
        0xA,
        "#4Pふ、ふざけろ……！\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xC,
        "#6Pくたばりやがれ……！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5Pぬるい──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14300, 400)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)

    def lambda_2136():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2136)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x0)

    def lambda_2153():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2153)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)

    def lambda_2170():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2170)
    Sleep(300)
    Battle(0xFFFFFFFF, 0x30200004, "", 0x30000500, 0x0, 0x0, 0x0, 0x30031100, 0x30031000, 0x30031000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x200, 0x8)
    FadeToDark(0, 0, -1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    Call(0, 15)
    Return()

    # Function_14_1B5C end

    def Function_15_21DB(): pass

    label("Function_15_21DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31151.itc", 0x1F)
    LoadChrToIndex("chr/ch31153.itc", 0x20)
    LoadChrToIndex("chr/ch31051.itc", 0x22)
    LoadChrToIndex("chr/ch31053.itc", 0x23)
    LoadChrToIndex("chr/ch00500.itc", 0x24)
    LoadChrToIndex("chr/ch00501.itc", 0x25)
    LoadChrToIndex("chr/ch00550.itc", 0x26)
    LoadChrToIndex("chr/ch00551.itc", 0x27)
    LoadEffect(0x0, "event\\ev307_00.eff")
    LoadEffect(0x1, "battle\\ms00001.eff")
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xA, 60780, 0, 4520, 0)
    SetChrPos(0xB, 60140, 0, 5260, 45)
    SetChrPos(0xC, 61710, 0, 5140, 315)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, 61000, 0, 6300, 180)
    FadeToBright(0, 0)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    Sound(834, 0, 100, 0)
    OP_68(61000, 700, 5300, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14530, 0)
    SetCameraDistance(17660, 500)
    BeginChrThread(0xA, 3, 0, 16)
    BeginChrThread(0xB, 3, 0, 17)
    BeginChrThread(0xC, 3, 0, 18)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    OP_6F(0x79)
    CancelBlur(0)

    #C0069
    ChrTalk(
        0xC,
        "#12Pがっ……\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        "#6P馬鹿な……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    Sound(514, 0, 100, 0)
    Call(0, 10)
    OP_0D()
    Sleep(750)
    SetChrPos(0x101, 58160, 0, -4030, 0)
    SetChrPos(0xEF, 58160, 0, -4030, 0)
    SetChrPos(0x151, 58160, 0, -4030, 0)
    OP_68(61500, 1000, 4019, 2000)
    MoveCamera(42, 16, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(18540, 2000)
    Sleep(200)

    def lambda_23D4():
        OP_95(0xFE, 61080, 0, 1250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23D4)
    Sleep(200)

    def lambda_23F1():
        OP_95(0xFE, 61590, 0, 160, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_23F1)
    Sleep(200)

    def lambda_240E():
        OP_95(0xFE, 60490, 0, 60, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_240E)
    WaitChrThread(0x101, 1)

    def lambda_242C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_242C)
    WaitChrThread(0xEF, 1)

    def lambda_243D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_243D)
    WaitChrThread(0x151, 1)

    def lambda_244E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_244E)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0071
    ChrTalk(
        0x101,
        "#5107F#12Pなっ……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_24F9")

    #C0072
    ChrTalk(
        0x102,
        "#5307F#12Pや、やっぱり……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_254E")

    label("loc_24F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2523")

    #C0073
    ChrTalk(
        0x103,
        "#5401F#12Pやはり……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_254E")

    label("loc_2523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_254E")

    #C0074
    ChrTalk(
        0x104,
        "#5607F#12P出やがったか……！\x02",
    )

    CloseMessageWindow()

    label("loc_254E")

    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x13)
    Sleep(300)
    Sound(1609, 255, 100, 0)    #voice#Yin
    Sleep(800)

    #C0075
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5P……妙な気配がするかと思えば\x01",
            "お前たちも入り込んでいたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5113F#12Pあんた……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x151,
        (
            "#5705F#12Pへえ……\x01",
            "随分とヤバそうな人だね。\x02\x03",

            "#5702F察するに、巷#2Rちまた#で噂されてる\x01",
            "《銀#2Rイン#》殿なのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5Pいかにも……\x01",
            "《テスタメンツ》リーダー、\x01",
            "ワジ・ヘミスフィア。\x02\x03",

            "妙な気配の一つは\x01",
            "お前のものだったようだな。\x02\x03",

            "それ以外にもいるようだが……\x01",
            "クク、まさに伏魔殿だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x151,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5704F#12Pふぅん、面白いことを言うね。\x02\x03",

            "#5700Fそれで……\x01",
            "僕たちも彼らのように\x01",
            "実力で排除するつもりかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x13)
    Fade(250)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_93(0x13, 0x0, 0x1F4)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0080
    ChrTalk(
        0x101,
        "#5111F#12Pお、おい……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0081
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#11Pフフ、お前たちを\x01",
            "始末するのは簡単だが……\x02\x03",

            "この場を任せても\x01",
            "面白いことになりそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0082
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5105F#12Pえ……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x13, 0x10E, 0x1F4)
    Sleep(300)

    #C0083
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#11Pそちらの奥の部屋には\x01",
            "競売会後半の出品物がある……\x02\x03",

            "《黒月》に流れた情報によると\x01",
            "面白い“爆弾”があるらしいぞ？\x02\x03",

            "その目で確かめてみるといい。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1614, 255, 100, 0)    #voice#Yin
    OP_93(0x13, 0x0, 0x190)
    Sleep(1200)
    Fade(500)
    OP_68(61000, 1000, 4500, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18540, 0)
    SetCameraDistance(17540, 1000)
    OP_0D()
    OP_6F(0x79)
    OP_68(61000, 1500, 8000, 1500)
    MoveCamera(0, 7, 0, 1500)
    OP_6E(800, 1500)
    SetCameraDistance(7250, 1500)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    SetChrChip(0x0, 0x13, 0x1E, 0x12C)

    def lambda_29BE():
        OP_95(0xFE, 61000, 0, 7500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_29BE)
    WaitChrThread(0x13, 1)
    SetChrSubChip(0x13, 0x2)
    SetChrFlags(0x13, 0x4)
    Sleep(200)
    Sound(854, 0, 100, 0)

    def lambda_29EE():
        OP_9D(0xFE, 0xEE48, 0xFFFFD8F0, 0x2AF8, 0x5DC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_29EE)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 60800, 0, 9000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x0, 0x1770, 0x1F4)
    Sound(921, 0, 100, 0)
    Sound(812, 0, 100, 0)
    SetMapObjFrame(0xFF, "mado_a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mado_b", 0x1, 0x1)
    WaitChrThread(0x13, 1)
    SetChrChip(0x1, 0x13, 0x0, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    OP_6F(0x79)
    Sleep(750)
    StopBGM(0x1F40)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(61020, 1000, 7200, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19540, 0)
    SetCameraDistance(16540, 2000)

    def lambda_2AEA():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AEA)
    Sleep(300)

    def lambda_2B02():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2B02)
    Sleep(300)

    def lambda_2B1A():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2B1A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x151, 1)
    OP_6F(0x79)
    OP_0D()

    #C0084
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5107F#11Pお、おい……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2B8D")

    #C0085
    ChrTalk(
        0x102,
        "#5301F#11Pなんて身のこなし……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BF0")

    label("loc_2B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2BBF")

    #C0086
    ChrTalk(
        0x103,
        "#5401F#11P……なんて速い……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BF0")

    label("loc_2BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2BF0")

    #C0087
    ChrTalk(
        0x104,
        "#5607F#11Pなんて身のこなしだ……！\x02",
    )

    CloseMessageWindow()

    label("loc_2BF0")


    #C0088
    ChrTalk(
        0x151,
        (
            "#5706F#12Pやれやれ……\x01",
            "噂に違わぬ化物みたいだね。\x02\x03",

            "#5703Fやり合う羽目にならなくて\x01",
            "ラッキーだったけど……\x02\x03",

            "#5701Fどうするんだい、ロイド？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0089
    ChrTalk(
        0x101,
        (
            "#5103F#5P……時間がない。\x01",
            "奥の部屋を調べてみよう。\x02\x03",

            "#5101Fあいつが言っていた“爆弾”……\x01",
            "本当にあるなら確かめてみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x151,
        (
            "#5702F#12Pフフ……\x01",
            "そう言うと思ったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2DB1")

    #C0091
    ChrTalk(
        0x102,
        (
            "#5306F#12Pふう、仕方ないわね。\x02\x03",

            "#5300F出来るだけ急いで\x01",
            "調べるだけ調べてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7E")

    label("loc_2DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2E1E")

    #C0092
    ChrTalk(
        0x103,
        (
            "#5406F#12P……はぁ、仕方ありませんね。\x02\x03",

            "#5402F可及的速やかに\x01",
            "調べるだけ調べてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E7E")

    label("loc_2E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2E7E")

    #C0093
    ChrTalk(
        0x104,
        (
            "#5606F#12Pったく、仕方ねぇな……\x02\x03",

            "#5600F出来るだけ急いで\x01",
            "調べるだけ調べちまうぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E7E")


    #C0094
    ChrTalk(
        0x101,
        "#5100F#5Pああ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    SetChrPos(0x0, 60190, 0, -200, 180)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xA6, 3)
    OP_29(0x47, 0x1, 0xD)
    OP_1B(0x2, 0x0, 0x20)
    WaitBGM()
    Sleep(500)
    PlayBGM("ed7302", 0)
    ReplaceBGM("ed7125", "ed7302")
    EventEnd(0x5)
    Return()

    # Function_15_21DB end

    def Function_16_2EFC(): pass

    label("Function_16_2EFC")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 60780, 800, 4520, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2F38():
        OP_9D(0xFE, 0xE998, 0x0, 0x712, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F38)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_16_2EFC end

    def Function_17_2F5D(): pass

    label("Function_17_2F5D")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 60140, 800, 5260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2F99():
        OP_9D(0xFE, 0xE51A, 0x0, 0xDA2, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F99)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_17_2F5D end

    def Function_18_2FBE(): pass

    label("Function_18_2FBE")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 61710, 800, 5140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2FFA():
        OP_9D(0xFE, 0xFAE6, 0x0, 0x1054, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FFA)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_18_2FBE end

    def Function_19_301F(): pass

    label("Function_19_301F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("chr/ch31050.itc", 0x23)
    LoadChrToIndex("chr/ch31051.itc", 0x24)
    LoadChrToIndex("chr/ch31150.itc", 0x25)
    LoadChrToIndex("chr/ch31151.itc", 0x26)
    LoadChrToIndex("chr/ch00000.itc", 0x29)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xD, 58100, 0, -73510, 0)
    SetChrPos(0xE, 58900, 0, -74710, 0)
    SetChrPos(0xF, 57170, 0, -75310, 0)
    SetChrPos(0x101, 57950, 0, -52700, 180)
    SetChrPos(0xEF, 58860, 0, -52240, 180)
    SetChrPos(0x105, 57560, 0, -50980, 180)
    SetChrPos(0x133, 57250, 0, -52700, 90)
    OP_68(58000, 1200, -51840, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(58100, 1200, -68860, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(58100, 1200, -73860, 1500)
    OP_6F(0x1)
    OP_0D()

    #C0095
    ChrTalk(
        0xD,
        "#11Pいたぞ……！\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xE,
        "#11P侵入者だ……！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(58000, 1200, -51840, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    #C0097
    ChrTalk(
        0x101,
        "#0010F#5Pくっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0098
    ChrTalk(
        0x101,
        (
            "#0007F#11P……キーア！\x01",
            "下がっていてくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x133,
        "#5801F#6Pうんっ……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x133, 3, 0, 21)
    Sleep(200)
    OP_93(0x101, 0xB4, 0x12C)
    WaitChrThread(0x133, 3)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_331A")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    Jump("loc_3341")

    label("loc_331A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3330")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_3341")

    label("loc_3330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3341")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_3341")

    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3373")

    #C0100
    ChrTalk(
        0x102,
        "#0107F#5P来るわ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_33C0")

    label("loc_3373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_339C")

    #C0101
    ChrTalk(
        0x103,
        "#0201F#5P来ます……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_33C0")

    label("loc_339C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_33C0")

    #C0102
    ChrTalk(
        0x104,
        "#0307F#5P来るぞ……！\x02",
    )

    CloseMessageWindow()

    label("loc_33C0")

    OP_68(57960, 1200, -53640, 1300)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xD, 58100, 0, -60510, 0)
    SetChrPos(0xE, 58900, 0, -61710, 0)
    SetChrPos(0xF, 57170, 0, -62310, 0)

    def lambda_3421():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3421)
    Sleep(100)

    def lambda_3439():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3439)
    Sleep(100)

    def lambda_3451():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3451)
    Sleep(800)
    Battle("BattleInfo_478", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    Call(0, 20)
    Return()

    # Function_19_301F end

    def Function_20_348E(): pass

    label("Function_20_348E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("chr/ch00000.itc", 0x23)
    LoadChrToIndex("apl/ch50364.itc", 0x24)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 57950, 0, -52700, 180)
    SetChrPos(0xEF, 58860, 0, -52240, 180)
    SetChrPos(0x105, 57560, 0, -50980, 180)
    SetChrPos(0x133, 56620, 0, -49950, 180)
    Call(0, 11)
    OP_68(57960, 1200, -53640, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(18290, 2500)
    OP_6F(0x10)
    OP_0D()

    #C0103
    ChrTalk(
        0x101,
        "#0010F#5Pくっ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    OP_68(58380, 1200, -50320, 1500)
    MoveCamera(38, 19, 0, 1500)

    def lambda_35B3():
        TurnDirection(0xFE, 0x133, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35B3)

    def lambda_35C0():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_35C0)
    Sleep(100)

    def lambda_35D0():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_35D0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    #C0104
    ChrTalk(
        0x101,
        "#0001F#11Pキーア、大丈夫か！？\x02",
    )

    CloseMessageWindow()

    def lambda_360F():

        label("loc_360F")

        TurnDirection(0x101, 0x133, 500)
        Yield()
        Jump("loc_360F")

    QueueWorkItem2(0x101, 1, lambda_360F)

    def lambda_3621():

        label("loc_3621")

        TurnDirection(0xEF, 0x133, 500)
        Yield()
        Jump("loc_3621")

    QueueWorkItem2(0xEF, 1, lambda_3621)

    def lambda_3633():

        label("loc_3633")

        TurnDirection(0x105, 0x133, 500)
        Yield()
        Jump("loc_3633")

    QueueWorkItem2(0x105, 1, lambda_3633)
    OP_68(58380, 1200, -51450, 1000)
    BeginChrThread(0x133, 3, 0, 22)
    WaitChrThread(0x133, 3)
    OP_6F(0x1)
    Sleep(300)

    #C0105
    ChrTalk(
        0x133,
        (
            "#5810F#6Pうん、だいじょーぶ。\x02\x03",

            "#5809Fキーア、へいきだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#0002F#11Pそっか……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x5)
    Sound(910, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Sleep(250)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x133, 0x80)
    SetChrBattleFlags(0x133, 0x8000)
    OP_0D()
    Sleep(300)

    #C0107
    ChrTalk(
        0x105,
        (
            "#0404F#5Pフフ、随分と\x01",
            "度胸のある子じゃないか。\x02\x03",

            "#0400Fこの調子で何とか\x01",
            "逃げ切れるといいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_37AA")

    #C0108
    ChrTalk(
        0x102,
        "#0101F#11Pとにかく急ぎましょう……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_380B")

    label("loc_37AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_37DE")

    #C0109
    ChrTalk(
        0x103,
        "#0201F#11P……急ぎましょう……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_380B")

    label("loc_37DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_380B")

    #C0110
    ChrTalk(
        0x104,
        "#0301F#11Pとにかく急ぐぞ……！\x02",
    )

    CloseMessageWindow()

    label("loc_380B")

    Sleep(150)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    SetChrPos(0x0, 57210, 0, -54060, 180)
    SetScenarioFlags(0xA6, 6)
    EventEnd(0x5)
    Return()

    # Function_20_348E end

    def Function_21_3834(): pass

    label("Function_21_3834")


    def lambda_3839():
        OP_95(0xFE, 56620, 0, -52700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3839)
    WaitChrThread(0xFE, 1)

    def lambda_3857():
        OP_95(0xFE, 56620, 0, -49950, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3857)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_3834 end

    def Function_22_3878(): pass

    label("Function_22_3878")


    def lambda_387D():
        OP_95(0xFE, 57250, 0, -52700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_387D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_22_3878 end

    def Function_23_389E(): pass

    label("Function_23_389E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("apl/ch50371.itc", 0x20)
    OP_68(-58000, 1200, 3580, 0)
    MoveCamera(322, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -58000, 0, -4970, 0)
    SetChrPos(0xEF, -58350, 0, -4920, 0)
    SetChrPos(0x105, -57990, 0, -6140, 0)
    SetChrPos(0x133, -52560, 0, -2430, 0)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, -59700, 0, 8000, 180)
    SetChrFlags(0x10, 0x8000)
    VolumeBGM(0x32, 0x7D0)
    FadeToBright(1000, 0)
    OP_68(-58000, 1200, -1480, 4000)

    def lambda_397B():
        OP_95(0xFE, -58000, 0, -1860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_397B)
    Sleep(800)

    def lambda_3998():
        OP_95(0xFE, -58680, 0, -2920, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3998)
    Sleep(300)

    def lambda_39B5():
        OP_95(0xFE, -57580, 0, -3520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_39B5)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_458C")

    #C0111
    ChrTalk(
        0x101,
        "#0005F#6Pここは……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3A49")

    #C0112
    ChrTalk(
        0x102,
        (
            "#0101F#6P確かハルトマン議長の\x01",
            "部屋じゃなかったかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD6")

    label("loc_3A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3A91")

    #C0113
    ChrTalk(
        0x103,
        (
            "#0201F#6P……確か議長さんの\x01",
            "部屋という話でしたが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD6")

    label("loc_3A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3AD6")

    #C0114
    ChrTalk(
        0x104,
        (
            "#0305F#1P確か議長ってヤツの\x01",
            "部屋とか言ってなかったか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD6")


    #C0115
    ChrTalk(
        0x105,
        (
            "#0402F#6Pへえ、さすがに\x01",
            "豪華そうな部屋だね──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0x105,
        (
            "#0404F#6P……どうやら\x01",
            "先客がいるみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        "#0005F#6Pえ……\x02",
    )

    CloseMessageWindow()
    OP_68(-57830, 1200, 4080, 2000)
    OP_6F(0x1)

    #N0118
    NpcTalk(
        0x10,
        "軽そうな声",
        "#11Pおいおい、先に気付くなよな。\x02",
    )

    CloseMessageWindow()

    #N0119
    NpcTalk(
        0x10,
        "軽そうな声",
        (
            "#11Pせっかく驚かせてやろうと\x01",
            "準備してたのによ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3C2F():

        label("loc_3C2F")

        TurnDirection(0x101, 0x10, 500)
        Yield()
        Jump("loc_3C2F")

    QueueWorkItem2(0x101, 1, lambda_3C2F)

    def lambda_3C41():

        label("loc_3C41")

        TurnDirection(0xEF, 0x10, 500)
        Yield()
        Jump("loc_3C41")

    QueueWorkItem2(0xEF, 1, lambda_3C41)

    def lambda_3C53():

        label("loc_3C53")

        TurnDirection(0x105, 0x10, 500)
        Yield()
        Jump("loc_3C53")

    QueueWorkItem2(0x105, 1, lambda_3C53)

    def lambda_3C65():
        OP_95(0xFE, -61300, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3C65)
    WaitChrThread(0x10, 1)
    OP_68(-58780, 1200, -1460, 4000)
    OP_93(0x10, 0x87, 0x1F4)

    def lambda_3C9B():
        OP_96(0xFE, 0xFFFF138E, 0x0, 0x2DA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3C9B)
    WaitChrThread(0x10, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x1)

    #C0120
    ChrTalk(
        0x101,
        "#0011F#6Pレクターさん……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3D18")

    #C0121
    ChrTalk(
        0x102,
        "#0105F#6Pど、どうしてここに……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D84")

    label("loc_3D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3D4B")

    #C0122
    ChrTalk(
        0x103,
        "#0205F#6P……どうしてここに……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D84")

    label("loc_3D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3D84")

    #C0123
    ChrTalk(
        0x104,
        (
            "#0301F#6Pチッ……\x01",
            "気配を消してやがったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D84")

    OP_68(-58540, 1200, -1840, 1500)

    def lambda_3D9A():
        OP_95(0xFE, -59360, 0, -570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3D9A)
    WaitChrThread(0x10, 1)
    OP_6F(0x1)

    #C0124
    ChrTalk(
        0x10,
        (
            "#3505F#5Pほう、これはなかなか……\x02\x03",

            "#3504Fフッ……アンタらも随分と\x01",
            "面白い魚を釣り上げたもんだなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#0005F#6Pえ……\x02",
    )

    CloseMessageWindow()

    #N0126
    NpcTalk(
        0x101,
        "キーア",
        (
            "#5805F#12Pお魚ってキーアのこと？\x02\x03",

            "#5801Fキーア、食べられちゃうの？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x10,
        (
            "#3502F#5Pおお、頭っから\x01",
            "ガブリとひと呑みにな！\x02\x03",

            "#3509Fがお～ッ！　バクバク！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A6(0x10, 0x14, 0x14, 0x190, 0x7D0)
    Sleep(300)
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x10, 0x0, 0x3E8)
    Sleep(500)
    OP_93(0x10, 0x10E, 0x3E8)
    OP_64(0x10)

    #C0128
    ChrTalk(
        0x10,
        (
            "#3507F#11Pんぐぐ、しまったぁ！\x01",
            "ノドに詰まらせちまったぜェ～！\x02",
        )
    )

    CloseMessageWindow()

    #N0129
    NpcTalk(
        0x101,
        "キーア",
        (
            "#5809F#12Pあはは！\x01",
            "このヒト、ヘンなヒトだね！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#0006F#6Pそれは十分すぎるくらい\x01",
            "分かってるよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x105,
        (
            "#0404F#6Pフフ、《銀#2Rイン#》といい、\x01",
            "ＩＢＣのお嬢様といい、\x01",
            "ヘンな知り合いが多いなぁ。\x02\x03",

            "#0402Fこれも君たちの人徳かい？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4047():
        TurnDirection(0xFE, 0x105, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4047)
    Sleep(50)

    def lambda_4057():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4057)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    #C0132
    ChrTalk(
        0x101,
        "#0013F#11Pそんな人徳、嫌すぎるんだが……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_40E5")

    #C0133
    ChrTalk(
        0x102,
        (
            "#0111F#5Pというか、あなたも十分、\x01",
            "ヘンな知り合いでしょう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4178")

    label("loc_40E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4135")

    #C0134
    ChrTalk(
        0x103,
        (
            "#0211F#5Pというか、ワジさんも十分、\x01",
            "ヘンな知り合いですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4178")

    label("loc_4135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4178")

    #C0135
    ChrTalk(
        0x104,
        (
            "#0306F#5Pつーか、お前も十分\x01",
            "ヘンな知り合いだろうが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4178")

    OP_93(0x10, 0x87, 0x1F4)
    Sleep(300)

    #C0136
    ChrTalk(
        0x10,
        (
            "#3506F#5Pおいおい、アンタら、\x01",
            "ちょっと和みすぎだろ～？\x02\x03",

            "#3501Fもうちょい脱出者としての\x01",
            "緊張感を持ってくれないとな！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_4233():
        TurnDirection(0xFE, 0x10, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4233)

    def lambda_4240():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4240)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    #C0137
    ChrTalk(
        0x101,
        (
            "#0012F#6Pいや、いきなり\x01",
            "そんな正論を言われても……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-58780, 1200, -2750, 1500)
    OP_6F(0x1)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, -57500, -1000, -8000, 0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    #N0138
    NpcTalk(
        0x12,
        "男の声",
        "#2P#2Sおい、いたか……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_433E():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_433E)

    def lambda_434B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_434B)
    Sleep(100)

    def lambda_435B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_435B)

    def lambda_4368():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4368)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x10, 1)

    #N0139
    NpcTalk(
        0x12,
        "男の声",
        (
            "#2P#2S右翼は調べた！\x01",
            "あとは左翼だけだ！\x02",
        )
    )

    CloseMessageWindow()

    #N0140
    NpcTalk(
        0x12,
        "男の声",
        "#2P#2S議長の部屋も確認しろ！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_68(-58780, 1200, -1840, 1000)

    def lambda_43FD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_43FD)
    Sleep(100)

    def lambda_440D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_440D)

    def lambda_441A():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_441A)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x10, 1)
    OP_6F(0x1)

    #C0141
    ChrTalk(
        0x101,
        "#0010F#11Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x10,
        (
            "#3505F#5P……なにグズグズしてんだ？\x02\x03",

            "#3504Fオレがいた場所があるだろうが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x10, 500)

    #C0143
    ChrTalk(
        0x101,
        "#0005F#6Pあ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4523")

    #C0144
    ChrTalk(
        0x102,
        "#0101F#6P迷っている暇は無いわ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_458C")

    label("loc_4523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_455E")

    #C0145
    ChrTalk(
        0x103,
        "#0201F#6P迷ってる暇は無さそうです……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_458C")

    label("loc_455E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_458C")

    #C0146
    ChrTalk(
        0x104,
        "#0301F#6P迷ってる暇はねぇ……！\x02",
    )

    CloseMessageWindow()

    label("loc_458C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x101, -57000, 0, 8000, 180)
    SetChrPos(0xEF, -58000, 0, 8000, 180)
    SetChrPos(0x105, -59000, 0, 8000, 180)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xD, -58000, 0, -5900, 0)
    SetChrPos(0xE, -58000, 0, -5900, 0)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, -61000, 0, 4000, 180)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    OP_68(-58000, 1200, 3580, 0)
    MoveCamera(322, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(-58000, 1200, -280, 4000)
    BeginChrThread(0x10, 3, 0, 24)
    Sleep(2000)
    Sound(103, 0, 100, 0)
    BeginChrThread(0xD, 3, 0, 25)
    Sleep(1000)
    BeginChrThread(0xE, 3, 0, 26)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x10, 3)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0147
    ChrTalk(
        0xD,
        "#6Pこれはレクター様……\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x10,
        (
            "#3504F#11Pおう、見回りご苦労。\x02\x03",

            "#3500Fクセ者が出たらしいが\x01",
            "そろそろ捕まったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xD,
        (
            "#6Pいえ……\x01",
            "ですが時間の問題です。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xE,
        (
            "#6Pところでレクター様は\x01",
            "どうしてここに……？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x10,
        (
            "#3503F#11Pああ、このあたりで\x01",
            "変な物音が聞こえてなァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xE,
        "#6P変な物音……？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xD,
        "#6Pまさか侵入者……！？\x02",
    )

    CloseMessageWindow()
    OP_68(-58000, 1200, 3280, 1500)
    OP_93(0x10, 0x0, 0x12C)
    OP_6F(0x1)

    #C0154
    ChrTalk(
        0x10,
        (
            "#3509F#6Pおーい、出て来いよ。\x02\x03",

            "恐がることないんだぜ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#0013F#11P（くっ……何を……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_48E5")

    #C0156
    ChrTalk(
        0x102,
        (
            "#0108F#11P（最初から私たちを\x01",
            "  突き出すつもりで……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4980")

    label("loc_48E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4934")

    #C0157
    ChrTalk(
        0x103,
        (
            "#0208F#11P（最初からわたしたちを\x01",
            "  突き出すつもりで……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4980")

    label("loc_4934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4980")

    #C0158
    ChrTalk(
        0x104,
        (
            "#0310F#11P（チッ、最初から俺たちを\x01",
            "  突き出すつもりか……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4980")


    #C0159
    ChrTalk(
        0x105,
        "#0404F#5P（いや……）\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(823, 0, 100, 0)
    Sleep(300)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x11, -57150, 0, 2300, 180)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    OP_68(-58000, 1200, 1000, 3500)

    def lambda_4A0A():

        label("loc_4A0A")

        TurnDirection(0x10, 0x11, 500)
        Yield()
        Jump("loc_4A0A")

    QueueWorkItem2(0x10, 1, lambda_4A0A)

    def lambda_4A1C():
        OP_95(0xFE, -57000, 0, 1000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4A1C)

    def lambda_4A36():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4A36)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x11, 2)
    OP_93(0x11, 0x10E, 0x1F4)
    EndChrThread(0x10, 0x1)
    OP_6F(0x1)

    #C0160
    ChrTalk(
        0xD,
        "#6Pね、猫……？\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x10,
        (
            "#3500F#5Pおう、クロ。\x01",
            "そんなに恐がるなって。\x02\x03",

            "ほ～らほら。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x10)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x11, -57200, 0, 1000, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrSubChip(0x10, 0x1)
    Sleep(500)

    #C0162
    ChrTalk(
        0x10,
        (
            "#3509F#5Pうりうり……\x01",
            "犬に追いかけられて\x01",
            "怖い思いをしちまったか。\x02\x03",

            "#3507Fよし、この黒い連中に\x01",
            "一言文句を言ってやれ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    OP_68(-58000, 1200, 0, 1200)
    OP_93(0x11, 0xB4, 0x1F4)
    OP_6F(0x1)
    Sound(823, 0, 100, 0)
    Sleep(1000)

    #C0163
    ChrTalk(
        0xD,
        "#6Pくっ、人騒がせな……\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xE,
        "#6P失礼する……！\x02",
    )

    CloseMessageWindow()

    def lambda_4BBF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4BBF)
    Sleep(100)

    def lambda_4BCF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4BCF)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)

    #C0165
    ChrTalk(
        0x10,
        (
            "#3505F#11Pあ、そうそう。\x01",
            "今思い出したぜ。\x02\x03",

            "#3510Fさっき、そこの窓から\x01",
            "妙な連中を見かけたんだが……\x02\x03",

            "うーん、あれが\x01",
            "クセ者ってやつだったのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4CAD():
        OP_93(0xFE, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4CAD)
    Sleep(50)

    def lambda_4CBD():
        OP_93(0xFE, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4CBD)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)

    #C0166
    ChrTalk(
        0xD,
        "#6P妙な連中！？\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xE,
        "#6Pどういう連中ですか！？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x10,
        (
            "#3503F#11Pなんかちっこい女の子を\x01",
            "連れてたみたいだが……\x02\x03",

            "#3501F裏庭の方に逃げていったぜェ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D67():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4D67)
    Sleep(100)

    def lambda_4D77():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4D77)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)

    #C0169
    ChrTalk(
        0xD,
        (
            "#11P間違いない……\x01",
            "目撃情報と一致するぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xE,
        (
            "#6Pクッ……\x01",
            "いつの間に屋敷の外に！？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xE,
        "#6P若頭に報告するぞ！\x02",
    )

    CloseMessageWindow()
    OP_68(-58000, 1200, -1500, 2000)
    BeginChrThread(0xE, 3, 0, 28)
    Sleep(500)
    BeginChrThread(0xD, 3, 0, 27)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)
    Fade(250)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x10)
    SetChrChipByIndex(0x10, 0x5)
    SetChrSubChip(0x10, 0x0)
    Sound(820, 0, 100, 0)
    OP_93(0x10, 0xB4, 0x0)
    OP_0D()
    Sleep(1000)
    OP_68(-56670, 1200, 1310, 5000)

    def lambda_4E7D():

        label("loc_4E7D")

        TurnDirection(0x10, 0x101, 500)
        Yield()
        Jump("loc_4E7D")

    QueueWorkItem2(0x10, 1, lambda_4E7D)

    def lambda_4E8F():

        label("loc_4E8F")

        TurnDirection(0x11, 0x101, 500)
        Yield()
        Jump("loc_4E8F")

    QueueWorkItem2(0x11, 1, lambda_4E8F)
    BeginChrThread(0x101, 3, 0, 29)
    Sleep(500)
    BeginChrThread(0xEF, 3, 0, 30)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 31)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x105, 3)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    OP_6F(0x1)

    #C0172
    ChrTalk(
        0x105,
        "#0402F#12Pフフ、見事な手並みだね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4F39")

    #C0173
    ChrTalk(
        0x102,
        (
            "#0111F#12Pその猫、最初から\x01",
            "用意してたんですか……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB5")

    label("loc_4F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4F73")

    #C0174
    ChrTalk(
        0x103,
        "#0211F#12Pその猫、最初から用意を……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FB5")

    label("loc_4F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4FB5")

    #C0175
    ChrTalk(
        0x104,
        (
            "#0302F#12Pったく、最初から\x01",
            "仕込んでやがったのかよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FB5")


    #C0176
    ChrTalk(
        0x10,
        (
            "#3504F#5Pん～……何のことだ？\x02\x03",

            "#3505Fおや、裏庭に逃げたはずの連中が\x01",
            "何故ここに……？\x02\x03",

            "#3509F世の中不思議で一杯だなァ～。\x02",
        )
    )

    CloseMessageWindow()

    #N0177
    NpcTalk(
        0x101,
        "キーア",
        (
            "#5809F#11Pあはは！\x01",
            "やっぱりヘンなヒトだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#0012F#12Pはは……本当に助かりました。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    #C0179
    ChrTalk(
        0x101,
        (
            "#0000F#5P──みんな、一か八か、\x01",
            "玄関の方に行ってみよう……！\x02\x03",

            "さっきの誘導で\x01",
            "手薄になってるかもしれない！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5136")

    #C0180
    ChrTalk(
        0x102,
        "#0100F#12Pええ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5189")

    label("loc_5136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5162")

    #C0181
    ChrTalk(
        0x103,
        "#0202F#12P了解です……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5189")

    label("loc_5162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5189")

    #C0182
    ChrTalk(
        0x104,
        "#0300F#12P合点承知だぜ！\x02",
    )

    CloseMessageWindow()

    label("loc_5189")

    OP_57(0x0)
    SetCameraDistance(18750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetChrPos(0x0, -58000, 0, 0, 180)
    SetChrPos(0x10, -54030, 0, 6580, 90)
    SetChrPos(0x11, -52930, 0, 6580, 270)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0xA7, 2)
    OP_29(0x47, 0x1, 0x11)
    VolumeBGM(0x64, 0xBB8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_23_389E end

    def Function_24_51F5(): pass

    label("Function_24_51F5")

    SetChrPos(0x10, -61000, 0, 4000, 180)

    def lambda_520B():
        OP_95(0xFE, -61000, 0, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_520B)
    WaitChrThread(0xFE, 1)

    def lambda_5229():
        OP_95(0xFE, -58000, 0, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5229)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_24_51F5 end

    def Function_25_524A(): pass

    label("Function_25_524A")


    def lambda_524F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_524F)
    OP_95(0xFE, -57980, 0, -4080, 4000, 0x1)
    OP_95(0xFE, -58000, 0, -2240, 4000, 0x0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_25_524A end

    def Function_26_528F(): pass

    label("Function_26_528F")


    def lambda_5294():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5294)
    OP_95(0xFE, -57980, 0, -4080, 4000, 0x1)
    OP_95(0xFE, -58360, 0, -3500, 4000, 0x0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_26_528F end

    def Function_27_52D4(): pass

    label("Function_27_52D4")


    def lambda_52D9():
        OP_95(0xFE, -58000, 0, -5900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_52D9)
    Sleep(500)

    def lambda_52F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_52F6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_27_52D4 end

    def Function_28_530B(): pass

    label("Function_28_530B")

    OP_93(0xFE, 0xB4, 0x320)

    def lambda_5317():
        OP_95(0xFE, -58000, 0, -5900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5317)
    Sleep(300)

    def lambda_5334():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5334)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_28_530B end

    def Function_29_5349(): pass

    label("Function_29_5349")


    def lambda_534E():
        OP_95(0xFE, -54690, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_534E)
    WaitChrThread(0xFE, 1)

    def lambda_536C():
        OP_95(0xFE, -55680, 0, 1190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_536C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_29_5349 end

    def Function_30_538D(): pass

    label("Function_30_538D")


    def lambda_5392():
        OP_95(0xFE, -54690, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5392)
    WaitChrThread(0xFE, 1)

    def lambda_53B0():
        OP_95(0xFE, -54290, 0, 200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53B0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_30_538D end

    def Function_31_53D1(): pass

    label("Function_31_53D1")


    def lambda_53D6():
        OP_95(0xFE, -54690, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53D6)
    WaitChrThread(0xFE, 1)

    def lambda_53F4():
        OP_95(0xFE, -54730, 0, 2230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53F4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_31_53D1 end

    def Function_32_5415(): pass

    label("Function_32_5415")

    EventBegin(0x1)

    #C0183
    ChrTalk(
        0x101,
        (
            "#5103F奥の部屋が気になる……\x02\x03",

            "#5101F時間もないし、\x01",
            "手早く調べてしまおう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 58000, 0, -4000, 0)
    EventEnd(0x4)
    Return()

    # Function_32_5415 end

    SaveToFile()

Try(main)
