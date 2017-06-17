from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t111b.bin",                # FileName
        "t111b",                    # MapName
        "t111b",                    # Location
        0x0047,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 71, 0, 2, 0, 3],
    )

    BuildStringList((
        "t111b",                  # 0
        "案内人バークレイ",       # 1
        "ニキータ",               # 2
        "エヴェリン夫人",         # 3
        "ジェイムズ",             # 4
        "黒服",                   # 5
        "黒服",                   # 6
        "招待客",                 # 7
        "招待客",                 # 8
        "招待客",                 # 9
        "招待客",                 # 10
        "招待客",                 # 11
        "招待客",                 # 12
        "黒服",                   # 13
        "黒服",                   # 14
        "黒服",                   # 15
        "マフィア",               # 16
        "マフィア",               # 17
        "マフィア",               # 18
        "ガルシア",               # 19
        "マリアベル",             # 20
        "マルコーニ会長",         # 21
        "ハルトマン議長",         # 22
        "bt111b",                 # 23
    ))

    ATBonus("ATBonus_3A4", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_3C4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_448", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_44C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_450", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_454", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_458", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_45C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_464", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt111b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31002.dat", "ms31102.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C4", "MonsterBattlePostion_444", "ed7509", "ed7000", "ATBonus_3A4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch36000.itc",                   # 01
        "chr/ch36100.itc",                   # 02
        "chr/ch33300.itc",                   # 03
        "chr/ch33000.itc",                   # 04
        "chr/ch33100.itc",                   # 05
        "chr/ch26800.itc",                   # 06
        "chr/ch21800.itc",                   # 07
        "chr/ch21900.itc",                   # 08
        "chr/ch22000.itc",                   # 09
        "chr/ch27800.itc",                   # 0A
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

    DeclNpc(1909,    500,     19610,   180,  385,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(10149,   500,     22780,   270,  385,  0x0, 0,   6,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2789,    500,     25229,   0,    385,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(2019,    500,     25690,   0,    401,  0x0, 0,   10,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-2240,   500,     27729,   180,  385,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(2009,    500,     27729,   180,  385,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-6530,   500,     16040,   135,  385,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-5719,   500,     15300,   315,  385,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(6449,    500,     24350,   45,   385,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-5719,   500,     15300,   315,  385,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-6530,   500,     16040,   135,  385,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(9100,    500,     22780,   90,   385,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_514",          # 00, 0
        "Function_1_5CC",          # 01, 1
        "Function_2_5CD",          # 02, 2
        "Function_3_713",          # 03, 3
        "Function_4_75C",          # 04, 4
        "Function_5_93F",          # 05, 5
        "Function_6_9BC",          # 06, 6
        "Function_7_A27",          # 07, 7
        "Function_8_B37",          # 08, 8
        "Function_9_D7F",          # 09, 9
        "Function_10_F9E",         # 0A, 10
        "Function_11_1017",        # 0B, 11
        "Function_12_10BA",        # 0C, 12
        "Function_13_11C5",        # 0D, 13
        "Function_14_138D",        # 0E, 14
        "Function_15_1400",        # 0F, 15
        "Function_16_14BF",        # 10, 16
        "Function_17_1E93",        # 11, 17
        "Function_18_329D",        # 12, 18
        "Function_19_46B8",        # 13, 19
        "Function_20_4CA2",        # 14, 20
        "Function_21_4F48",        # 15, 21
        "Function_22_51E9",        # 16, 22
        "Function_23_578B",        # 17, 23
        "Function_24_5FE0",        # 18, 24
        "Function_25_6001",        # 19, 25
        "Function_26_6030",        # 1A, 26
    ))


    def Function_0_514(): pass

    label("Function_0_514")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_554"),
        (1, "loc_560"),
        (2, "loc_56C"),
        (3, "loc_578"),
        (4, "loc_584"),
        (5, "loc_590"),
        (6, "loc_59C"),
        (SWITCH_DEFAULT, "loc_5A8"),
    )


    label("loc_554")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_560")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_56C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_578")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_584")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_590")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_59C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5CB")

    Return()

    # Function_0_514 end

    def Function_1_5CC(): pass

    label("Function_1_5CC")

    Return()

    # Function_1_5CC end

    def Function_2_5CD(): pass

    label("Function_2_5CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_5DB")
    Jump("loc_650")

    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_5FD")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_650")

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_629")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_650")

    label("loc_629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_650")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_650")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A2")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69A")
    Event(0, 18)
    Jump("loc_69D")

    label("loc_69A")

    Event(0, 17)

    label("loc_69D")

    Jump("loc_6B3")

    label("loc_6A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B3")
    Event(0, 22)

    label("loc_6B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_6C7")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 16)
    Jump("loc_712")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_6DB")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 19)
    Jump("loc_712")

    label("loc_6DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_6EF")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 20)
    Jump("loc_712")

    label("loc_6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_703")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 21)
    Jump("loc_712")

    label("loc_703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_712")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 23)

    label("loc_712")

    Return()

    # Function_2_5CD end

    def Function_3_713(): pass

    label("Function_3_713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_71C")

    label("loc_71C")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_734")
    OP_1B(0x0, 0x0, 0x1A)

    label("loc_734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_747")
    OP_1B(0x0, 0x0, 0x1A)

    label("loc_747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_755")
    OP_1B(0x0, 0x0, 0x1A)

    label("loc_755")

    Sound(124, 1, 80, 0)
    Return()

    # Function_3_713 end

    def Function_4_75C(): pass

    label("Function_4_75C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_76D")
    Jump("loc_93B")

    label("loc_76D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_7E0")

    #C0001
    ChrTalk(
        0xFE,
        "おや……いかがなさいましたか？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "間もなく競売が始まります。\x01",
            "早めに席についてお待ちください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93B")

    label("loc_7E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_7EE")
    Jump("loc_93B")

    label("loc_7EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_93B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D1")

    #C0003
    ChrTalk(
        0xFE,
        (
            "オークションは午後９時から、\x01",
            "そちらの正面にあるホールにて\x01",
            "開催を予定しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "それまでの間、左手にあるサロンで\x01",
            "饗応の用意をさせて頂いておりますので\x01",
            "お酒やお食事などをお楽しみください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_93B")

    label("loc_8D1")


    #C0005
    ChrTalk(
        0xFE,
        (
            "お部屋が必要になりましたら\x01",
            "声をおかけになって下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "すぐに部屋を用意させて\x01",
            "いただきますので。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93B")

    TalkEnd(0xFE)
    Return()

    # Function_4_75C end

    def Function_5_93F(): pass

    label("Function_5_93F")

    TalkBegin(0xFE)

    #C0007
    ChrTalk(
        0xFE,
        (
            "丁度良く\x01",
            "フリーの招待客がいて\x01",
            "よかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "ジェイムズさんは\x01",
            "羽振りがよかったけど……\x01",
            "この人はどうかしらね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_93F end

    def Function_6_9BC(): pass

    label("Function_6_9BC")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        (
            "主人が仲直りの印に、\x01",
            "特別綺麗な宝飾品を\x01",
            "落札してくれるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "うふふ……楽しみですわ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_9BC end

    def Function_7_A27(): pass

    label("Function_7_A27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFD")
    OP_4B(0xA, 0xFF)

    #C0011
    ChrTalk(
        0xB,
        (
            "……さっき案内人が来た時に\x01",
            "席をとっておいて貰えばよかったな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0012
    ChrTalk(
        0xA,
        "あら、どうしてですの？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        (
            "（万が一ニキータ君と\x01",
            "  近い席になってしまったら\x01",
            "  気まずいからね……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_B33")

    label("loc_AFD")


    #C0014
    ChrTalk(
        0xB,
        (
            "ま、まぁいい。\x01",
            "とにかく会場に\x01",
            "入ろうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B33")

    TalkEnd(0xFE)
    Return()

    # Function_7_A27 end

    def Function_8_B37(): pass

    label("Function_8_B37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_B48")
    Jump("loc_D7B")

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C76")

    #C0015
    ChrTalk(
        0xFE,
        (
            "お客様……\x01",
            "どうしました？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "あまり出歩かれては困ります。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#5101F（黒服たちはまだ異変に\x01",
            "  気づいてないらしいな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x151,
        (
            "#5703F（フフ、好都合じゃないか。\x01",
            "  調べるなら騒ぎになる\x01",
            "  前の方がいいよ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#5101F（そうだな……今のうちに\x01",
            "  屋敷を歩き回ってみよう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CDA")

    label("loc_C76")


    #C0020
    ChrTalk(
        0xFE,
        "……部屋に忘れ物ですか？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "オークションの開始を\x01",
            "遅らせることはできません。\x01",
            "お急ぎください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDA")

    Jump("loc_D7B")

    label("loc_CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_D26")

    #C0022
    ChrTalk(
        0xFE,
        (
            "間もなくオークションが開催します。\x01",
            "会場内へどうぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7B")

    label("loc_D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_D7B")

    #C0023
    ChrTalk(
        0xFE,
        (
            "邸内の安全は\x01",
            "我々が保証します。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "どうか安心して\x01",
            "お過ごしください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7B")

    TalkEnd(0xFE)
    Return()

    # Function_8_B37 end

    def Function_9_D7F(): pass

    label("Function_9_D7F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_D90")
    Jump("loc_F9A")

    label("loc_D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_E13")
    OP_93(0xFE, 0xB4, 0x0)

    #C0025
    ChrTalk(
        0xFE,
        (
            "席は充分に用意しております。\x01",
            "空いた席へお座り下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "立ち見になりますが２階席も\x01",
            "ご利用できますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9A")

    label("loc_E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_F40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF2")

    #C0027
    ChrTalk(
        0xFE,
        (
            "マリアベル様とご友人の方々ですね？\x01",
            "案内人より言付かっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "最後列に席を\x01",
            "ご用意しておりますので\x01",
            "中で案内を受けてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x138,
        (
            "#2900Fどういたしまして。\x01",
            "……さ、中に入りましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_F3B")

    label("loc_EF2")


    #C0030
    ChrTalk(
        0xFE,
        (
            "マリアベル様とご友人の方々ですね？\x01",
            "最後列に席をご用意しております。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3B")

    Jump("loc_F9A")

    label("loc_F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_F9A")

    #C0031
    ChrTalk(
        0xFE,
        (
            "会場は現在、\x01",
            "オークションの準備中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "開場までしばらくお待ち下さい。\x02",
    )

    CloseMessageWindow()

    label("loc_F9A")

    TalkEnd(0xFE)
    Return()

    # Function_9_D7F end

    def Function_10_F9E(): pass

    label("Function_10_F9E")

    TalkBegin(0xFE)

    #C0033
    ChrTalk(
        0xFE,
        (
            "夫に連れられて\x01",
            "初めて議長邸に来ましたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "これから行われる競売会のことを考えると\x01",
            "楽しみで仕方がないわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_F9E end

    def Function_11_1017(): pass

    label("Function_11_1017")

    TalkBegin(0xFE)

    #C0035
    ChrTalk(
        0xFE,
        (
            "妻は普段から大人しくてね。\x01",
            "刺激を与えたいと思って\x01",
            "連れてきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "社交界を生き抜く為に\x01",
            "夫人として相応しい振る舞いを\x01",
            "身に付けてもらわなくてはな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1017 end

    def Function_12_10BA(): pass

    label("Function_12_10BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1149")

    #C0037
    ChrTalk(
        0xFE,
        (
            "帝国にある我が屋敷を持ってしても\x01",
            "この屋敷と比べると\x01",
            "数段見劣りしてしまう。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "豪華絢爛とはこのことを言うのだな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_11C1")

    label("loc_1149")


    #C0039
    ChrTalk(
        0xFE,
        (
            "帝国にある我が屋敷も\x01",
            "それなりに広くはあるのだが……\x01",
            "この屋敷と比べてしまうとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "是非ともあやかりたいものだ。\x02",
    )

    CloseMessageWindow()

    label("loc_11C1")

    TalkEnd(0xFE)
    Return()

    # Function_12_10BA end

    def Function_13_11C5(): pass

    label("Function_13_11C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FC")

    #C0041
    ChrTalk(
        0xFE,
        "いよいよオークションが始まるな……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "ローゼンベルク工房の人形は\x01",
            "きっと私が落札してみせるぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x138,
        (
            "#2905Fあら……\x01",
            "ライバル出現ですわね。\x02\x03",

            "#2900F私もあれを狙っていますの。\x01",
            "ふふふ……負けませんわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x138, 500)

    #C0044
    ChrTalk(
        0xFE,
        (
            "ほほう……いい度胸だなお嬢さん。\x01",
            "お手柔らかに頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1389")

    label("loc_12FC")


    #C0045
    ChrTalk(
        0xFE,
        (
            "欲しい物がすぐそこにあるのだ、\x01",
            "私も引くわけにはいかないな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x138, 500)

    #C0046
    ChrTalk(
        0xFE,
        (
            "お嬢さん。\x01",
            "お手柔らかに頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x138,
        "#2900Fふふ……こちらこそ。\x02",
    )

    CloseMessageWindow()

    label("loc_1389")

    TalkEnd(0xFE)
    Return()

    # Function_13_11C5 end

    def Function_14_138D(): pass

    label("Function_14_138D")

    TalkBegin(0xFE)

    #C0048
    ChrTalk(
        0xFE,
        (
            "主人ったら開始時間が近づいて\x01",
            "舞い上がっているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "席に着いたら一旦\x01",
            "頭を冷やしてやらないとね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_138D end

    def Function_15_1400(): pass

    label("Function_15_1400")

    TalkBegin(0xFE)

    #C0050
    ChrTalk(
        0xFE,
        (
            "（先程こちらの女性に\x01",
            "　声をかけられてね。\x01",
            "　一緒に競売に行くことにしたよ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "（同伴者がいないとなると\x01",
            "　やはり格好がつかないからね。\x01",
            "　ふふ、都合のいい女がいて助かったよ。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1400 end

    def Function_16_14BF(): pass

    label("Function_16_14BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 500, 500, 6800, 0)
    SetChrPos(0xEF, -500, 500, 6800, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    FadeToBright(1000, 0)
    OP_68(-4530, 2300, 17580, 0)
    MoveCamera(326, 9, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19400, 0)
    OP_68(5540, 2300, 24020, 10000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(0, 2300, 11200, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16760, 0)
    OP_4B(0x8, 0xFF)

    def lambda_15C6():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15C6)
    Sleep(200)

    def lambda_15DE():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_15DE)

    def lambda_15F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15F3)

    def lambda_1604():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_1604)
    OP_68(0, 2300, 12950, 4000)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xEF, 2)
    OP_0D()

    #C0052
    ChrTalk(
        0x101,
        "#5105F#12Pな、なんだここは……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_16BE")

    #C0053
    ChrTalk(
        0x102,
        (
            "#5301F#6Pハルトマン議長邸……\x02\x03",

            "噂には聞いていたけど\x01",
            "こんな壮麗な建物だったなんて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B5")

    label("loc_16BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1741")

    #C0054
    ChrTalk(
        0x103,
        (
            "#5406F#6P何だかお屋敷というより\x01",
            "お城という雰囲気ですね……\x02\x03",

            "#5401F維持するだけでも\x01",
            "大変なミラがかかりそうです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B5")

    label("loc_1741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_17B5")

    #C0055
    ChrTalk(
        0x104,
        (
            "#5605F#6Pひゅーっ！\x01",
            "とんでもない屋敷だな。\x02\x03",

            "#5601Fこりゃ、帝国の大貴族も\x01",
            "顔負けの屋敷なんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B5")


    #C0056
    ChrTalk(
        0x101,
        (
            "#5106F#12Pああ……想像以上だったな。\x02\x03",

            "#5108F（ハルトマン議長……\x01",
            "  それに《ルバーチェ》……）\x02\x03",

            "#5113F（ここまで大物だったのか……）\x02",
        )
    )

    CloseMessageWindow()

    #N0057
    NpcTalk(
        0x8,
        "男性の声",
        "#11P──ようこそ、お客様。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1893():
        OP_95(0xFE, 0, 500, 14060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1893)
    WaitChrThread(0x8, 1)

    #C0058
    ChrTalk(
        0x8,
        "#5P《黒の競売会#10Rシュバルツオークション#》へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#5Pお客様は……\x01",
            "初めてのご来場でございますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#5100F#12Pああ、そうだけど。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "#5Pオークションは午後９時から、\x01",
            "正面にあるホールにて\x01",
            "開催を予定しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#5Pそれまでの間、左手にあるサロンで\x01",
            "饗応の用意をさせて頂いておりますので\x01",
            "お酒やお食事などをお楽しみください。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#5Pちなみに今宵、当館に\x01",
            "お泊りになるつもりはございますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#5105F#12Pあ、いや……\x02\x03",

            "#5104Fホテルに部屋を取っているし\x01",
            "知り合いも待たせているからね。\x02\x03",

            "#5100F今回は遠慮させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        "#5Pかしこまりました。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "#5Pもし気が変わられた場合、\x01",
            "すぐにお部屋を用意いたしますので\x01",
            "遠慮なくお申し付けになってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#5Pなお、邸内はご自由に\x01",
            "ご観覧いただいて結構ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "#5P幾つかの区画は\x01",
            "立入りをご遠慮願っておりますので\x01",
            "どうかご容赦くださいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#5100F#12Pああ、分かったよ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1C36")

    #C0070
    ChrTalk(
        0x102,
        (
            "#5302F#6Pふふ……\x01",
            "丁寧な案内、ありがとう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9B")

    label("loc_1C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1C6B")

    #C0071
    ChrTalk(
        0x103,
        "#5402F#6P……案内、お疲れ様です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C9B")

    label("loc_1C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1C9B")

    #C0072
    ChrTalk(
        0x104,
        "#5609F#6P丁寧な案内、ご苦労さん。\x02",
    )

    CloseMessageWindow()

    label("loc_1C9B")


    #C0073
    ChrTalk(
        0x8,
        (
            "#5Pいえ、何かあったら\x01",
            "わたくしや他の使用人に\x01",
            "遠慮なくお申し付けください。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        "#5Pそれでは……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_1D0B():
        OP_95(0xFE, 1910, 500, 19610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1D0B)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    TurnDirection(0x101, 0xEF, 500)

    #C0075
    ChrTalk(
        0x101,
        (
            "#5103F#2P（オークション開催まで\x01",
            "  ２時間くらいはある……）\x02\x03",

            "#5101F（一通り屋敷の中を回ってみよう。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1DD6")

    #C0076
    ChrTalk(
        0x102,
        "#5301F#1P（ええ、分かったわ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E4C")

    label("loc_1DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1E05")

    #C0077
    ChrTalk(
        0x103,
        "#5401F#1P（……了解です。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E4C")

    label("loc_1E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1E4C")

    #C0078
    ChrTalk(
        0x104,
        (
            "#5600F#1P（おお、適当にメシでも\x01",
            "  摘みながら行こうぜ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4C")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 500, 12000, 0)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xA5, 0)
    OP_29(0x47, 0x1, 0x9)
    OP_1B(0x0, 0x0, 0x1A)
    EventEnd(0x5)
    Return()

    # Function_16_14BF end

    def Function_17_1E93(): pass

    label("Function_17_1E93")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch36100.itc", 0x1E)
    LoadChrToIndex("chr/ch02200.itc", 0x1F)
    LoadChrToIndex("chr/ch05500.itc", 0x20)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -4010, 500, 25720, 180)
    OP_68(0, 1600, 19000, 0)
    MoveCamera(325, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x1A, 0, 500, 15000, 0)
    SetChrPos(0x15, 0, 500, 13500, 0)
    OP_52(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x1B, 0, 500, 12000, 0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -14500, 500, 20600, 90)
    SetChrPos(0xEF, -14500, 500, 19400, 90)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02900.itp")
    FadeToBright(1000, 0)
    SetCameraDistance(19000, 2500)

    def lambda_202F():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_202F)

    def lambda_2044():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2044)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)
    OP_6F(0x10)
    OP_0D()
    OP_93(0x1A, 0xB4, 0x1F4)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0079
    AnonymousTalk(
        0x1A,
        (
            "……フン、妙だな。\x02\x03",

            "てっきり何か仕掛けてくると\x01",
            "思ったんだが……\x02",
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

    #C0080
    ChrTalk(
        0x15,
        "#6P今の所は異常ナシですね。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x15,
        (
            "#6Pさすがの《黒月#4Rヘイユエ#》も、\x01",
            "ハルトマン議長の顔を潰すような\x01",
            "真似はしないんじゃないですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x1A,
        (
            "#3103F#11P馬鹿野郎、連中を甘く見るな。\x02\x03",

            "#3101F《銀#2Rイン#》はもちろん、あのツァオも\x01",
            "有能すぎて組織の長老どもから\x01",
            "疎まれてるって噂の切れ者だ。\x02\x03",

            "気を抜いていると\x01",
            "喉笛に喰い付かれるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x15,
        "#6Pは、はい……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x1A,
        (
            "#3103F#11Pしかし、今回の競売会は\x01",
            "妙な感じがしやがるな……\x02\x03",

            "《黒月》以外にも、\x01",
            "どこぞの連中がチョロチョロと\x01",
            "紛れ込んでいるような……\x02\x03",

            "#3101Fそんな気配がしやがるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x15,
        "#6Pえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x15,
        (
            "#6Pそれも戦場で培#2Rつちか#った\x01",
            "猟兵としてのカンですかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1A,
        (
            "#3104F#11P……まあな。\x02\x03",

            "#3102Fクク……\x01",
            "俺もヤキが回っちまったか。\x02\x03",

            "このまま何も起こらずに\x01",
            "終わるに越した事はねえんだが……\x01",
            "どうにも血が疼#2Rウズ#きやがる。\x02\x03",

            "久々に“狩り”がしたい気分だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x15,
        "#6Pは、はは……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-12460, 1600, 21220, 0)
    MoveCamera(325, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(-1910, 1600, 19760, 4500)

    def lambda_2488():
        OP_95(0xFE, -4000, 500, 20600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2488)
    Sleep(100)

    def lambda_24A5():
        OP_95(0xFE, -4000, 500, 19400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_24A5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0089
    ChrTalk(
        0x101,
        "#5105F#5Pあ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2542")

    #C0090
    ChrTalk(
        0x102,
        "#5301F#5P（マフィアの若頭……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_25AD")

    label("loc_2542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_257B")

    #C0091
    ChrTalk(
        0x103,
        "#5401F#5P（マフィアの若頭さん……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_25AD")

    label("loc_257B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_25AD")

    #C0092
    ChrTalk(
        0x104,
        "#5607F#5P（《キリングベア》か……）\x02",
    )

    CloseMessageWindow()

    label("loc_25AD")

    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_25EA")

    def lambda_25E2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_25E2)

    label("loc_25EA")


    def lambda_25EF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_25EF)
    Sleep(50)

    def lambda_25FF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_25FF)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)

    #C0093
    ChrTalk(
        0x1A,
        (
            "#3104F#12Pおっと、こいつは失礼。\x02\x03",

            "#3100F当会場の警備を担当している\x01",
            "ガルシア・ロッシといいます。\x02\x03",

            "防犯のため見回ってる最中でして、\x01",
            "お見苦しいでしょうがご容赦を。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#5112F#5P……いや。\x01",
            "見回り、ご苦労さまだね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2724")

    #C0095
    ChrTalk(
        0x102,
        "#5308F#5P（何とか凌#2Rしの#がないと……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2793")

    label("loc_2724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_275B")

    #C0096
    ChrTalk(
        0x103,
        "#5408F#5P（何とか離脱しないと……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2793")

    label("loc_275B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2793")

    #C0097
    ChrTalk(
        0x104,
        "#5608F#5P（何とか躱#2Rかわ#せるか……？）\x02",
    )

    CloseMessageWindow()

    label("loc_2793")

    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-3300, 1600, 20000, 2500)

    def lambda_27BE():
        OP_95(0xFE, -2500, 500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_27BE)
    Sleep(300)
    Sound(1856, 255, 100, 0)    #voice#Garcia
    WaitChrThread(0x1A, 1)
    OP_6F(0x1)

    #C0098
    ChrTalk(
        0x1A,
        (
            "#3105F#12Pお客さん、どこかで\x01",
            "見かけた事があるような……\x02\x03",

            "#3101F……ん～……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0099
    ChrTalk(
        0x101,
        (
            "#5104F#5P……気のせいじゃないかな？\x02\x03",

            "#5100Fあなたみたいな大柄な人、\x01",
            "一度見たら忘れないだろうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x1A,
        (
            "#3109F#12Pはは、そうかもしれませんな。\x02\x03",

            "#3100Fふむ……念のため\x01",
            "名前を伺ってもいいですかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#5103F#5P……ああ、構わないよ。\x02\x03",

            "#5100F──初めまして。\x01",
            "ガイ・バニングスという。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0102
    ChrTalk(
        0x1A,
        (
            "#3105F#12Pガイ……？\x02\x03",

            "はて、その名前も\x01",
            "どこかで聞いたような……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2A21")
    TurnDirection(0x1A, 0x104, 500)
    Sleep(300)

    #C0103
    ChrTalk(
        0x1A,
        "#3101F#12Pそれに、そちらの御仁は……\x02",
    )

    CloseMessageWindow()

    label("loc_2A21")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0xEF)

    #C0104
    ChrTalk(
        0x101,
        "#5110F#5P（くっ……マズったか……！？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2AAE")

    #C0105
    ChrTalk(
        0x102,
        "#5301F#5P（ど、どうしたら……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B11")

    label("loc_2AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2ADF")

    #C0106
    ChrTalk(
        0x103,
        "#5401F#5P（絶体絶命です……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B11")

    label("loc_2ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2B11")

    #C0107
    ChrTalk(
        0x104,
        "#5610F#5P（チッ、こうなったら……）\x02",
    )

    CloseMessageWindow()

    label("loc_2B11")


    #N0108
    NpcTalk(
        0x1B,
        "女性の声",
        (
            "#11P──ふふ。\x01",
            "遅れてしまいましたわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2B97():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B97)

    def lambda_2BA4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2BA4)
    Sleep(100)

    def lambda_2BB4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2BB4)

    def lambda_2BC1():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2BC1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)

    def lambda_2BDE():

        label("loc_2BDE")

        TurnDirection(0x15, 0x1B, 500)
        Yield()
        Jump("loc_2BDE")

    QueueWorkItem2(0x15, 1, lambda_2BDE)
    OP_68(-2700, 1600, 19140, 3000)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_2C0C():
        OP_95(0xFE, -1820, 500, 17630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2C0C)
    WaitChrThread(0x1B, 1)
    OP_6F(0x1)
    EndChrThread(0x15, 0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0109
    ChrTalk(
        0x101,
        "#5105F#5Pへ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2CA3")

    #C0110
    ChrTalk(
        0x102,
        "#5305F#5Pベ、ベル……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D0A")

    label("loc_2CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2CD6")

    #C0111
    ChrTalk(
        0x103,
        "#5405F#5Pマリアベルさん……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D0A")

    label("loc_2CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2D0A")

    #C0112
    ChrTalk(
        0x104,
        "#5605F#5Pマリアベルのお嬢さん……！？\x02",
    )

    CloseMessageWindow()

    label("loc_2D0A")

    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0113
    AnonymousTalk(
        0x1B,
        (
            "ふふ……\x01",
            "こんばんは、“ガイ”さん。\x02\x03",

            "こんな場所で会えるなんて\x01",
            "本当に奇遇ですわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0114
    ChrTalk(
        0x101,
        "#5112F#5Pえ、ええ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2E14")

    #C0115
    ChrTalk(
        0x102,
        "#5306F#5P本当に……予想外だわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E73")

    label("loc_2E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2E45")

    #C0116
    ChrTalk(
        0x103,
        "#5406F#5P確かに予想外です……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E73")

    label("loc_2E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2E73")

    #C0117
    ChrTalk(
        0x104,
        "#5606F#5P……確かに奇遇ッスね。\x02",
    )

    CloseMessageWindow()

    label("loc_2E73")


    #C0118
    ChrTalk(
        0x1A,
        (
            "#3100F#11Pふむ……\x01",
            "お嬢さんはどちらさまで？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x1B,
        (
            "#2904F#6Pわたくしの名は\x01",
            "マリアベル・クロイス。\x02\x03",

            "#2902Fお見知りおき願いますわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x15,
        "#11PＩＢＣの……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x1A,
        (
            "#3104F#11Pこれはこれは……\x01",
            "上から話は聞いておりましたよ。\x02\x03",

            "#3100F今年はついに招待に\x01",
            "応じてくださったわけですな？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x1B,
        (
            "#2904F#6Pふふ、何度も断るのも\x01",
            "さすがに失礼かと思いまして。\x02\x03",

            "#2900Fこちらの方々は\x01",
            "わたくしの友人ですけど……\x02\x03",

            "何か問題でもありまして？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x1A,
        (
            "#3104F#11Pいやいや、とんでもない。\x02\x03",

            "#3100F改めまして──\x01",
            "ようこそ《黒の競売会#10Rシュバルツオークション#》へ。\x02\x03",

            "まずはハルトマン議長に\x01",
            "ご案内いたしましょうかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x1B,
        (
            "#2904F#6Pふふ、議長閣下には\x01",
            "後ほど改めて挨拶しますわ。\x02\x03",

            "#2902Fそれより出来れば\x01",
            "お部屋をご用意してくださる？\x02\x03",

            "先ほどまで商談をしていたので\x01",
            "少し休憩したいのですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x1A,
        "#3104F#11Pかしこまりました。\x02",
    )

    CloseMessageWindow()
    OP_68(-3030, 1600, 20130, 1200)
    OP_93(0x1A, 0x0, 0x190)
    OP_6F(0x1)

    #C0126
    ChrTalk(
        0x1A,
        (
            "#3100F#6P──おい。\x01",
            "マリアベルお嬢様が部屋をご所望だ。\x02\x03",

            "くれぐれも粗相の無いようにな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x8, 0x1A, 500)
    Sleep(500)

    #C0127
    ChrTalk(
        0x8,
        (
            "#11Pは、はい。\x01",
            "それでは案内させて頂きます。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    AddParty(0x37, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    NewScene("t117B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_1E93 end

    def Function_18_329D(): pass

    label("Function_18_329D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch36100.itc", 0x1E)
    LoadChrToIndex("chr/ch02200.itc", 0x1F)
    LoadChrToIndex("chr/ch05500.itc", 0x20)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, 4010, 500, 25720, 180)
    OP_68(0, 1600, 19000, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x1A, 0, 500, 15000, 0)
    SetChrPos(0x15, 0, 500, 13500, 0)
    OP_52(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x1B, 0, 500, 12000, 0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 14500, 500, 20600, 90)
    SetChrPos(0xEF, 14500, 500, 19400, 90)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02900.itp")
    FadeToBright(1000, 0)
    SetCameraDistance(19000, 2500)

    def lambda_3439():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3439)

    def lambda_344E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_344E)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)
    OP_6F(0x10)
    OP_0D()
    OP_93(0x1A, 0xB4, 0x1F4)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0128
    AnonymousTalk(
        0x1A,
        (
            "……フン、妙だな。\x02\x03",

            "てっきり何か仕掛けてくると\x01",
            "思ったんだが……\x02",
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

    #C0129
    ChrTalk(
        0x15,
        "#12P今の所は異常ナシですね。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x15,
        (
            "#12Pさすがの《黒月#4Rヘイユエ#》も、\x01",
            "ハルトマン議長の顔を潰すような\x01",
            "真似はしないんじゃないですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x1A,
        (
            "#3103F#5P馬鹿野郎、連中を甘く見るな。\x02\x03",

            "#3101F《銀#2Rイン#》はもちろん、あのツァオも\x01",
            "有能すぎて組織の長老どもから\x01",
            "疎まれてるって噂の切れ者だ。\x02\x03",

            "気を抜いていると\x01",
            "喉笛に喰い付かれるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x15,
        "#12Pは、はい……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x1A,
        (
            "#3103F#5Pしかし、今回の競売会は\x01",
            "妙な感じがしやがるな……\x02\x03",

            "《黒月》以外にも、\x01",
            "どこぞの連中がチョロチョロと\x01",
            "紛れ込んでいるような……\x02\x03",

            "#3101Fそんな気配がしやがるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x15,
        "#12Pえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x15,
        (
            "#12Pそれも戦場で培#2Rつちか#った\x01",
            "猟兵としてのカンですかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x1A,
        (
            "#3104F#5P……まあな。\x02\x03",

            "#3102Fクク……\x01",
            "俺もヤキが回っちまったか。\x02\x03",

            "このまま何も起こらずに\x01",
            "終わるに越した事はねえんだが……\x01",
            "どうにも血が疼#2Rウズ#きやがる。\x02\x03",

            "久々に“狩り”がしたい気分だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x15,
        "#12Pは、はは……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(12460, 1600, 21220, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(1910, 1600, 19760, 4500)

    def lambda_3895():
        OP_95(0xFE, 4000, 500, 20600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3895)
    Sleep(100)

    def lambda_38B2():
        OP_95(0xFE, 4000, 500, 19400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_38B2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0138
    ChrTalk(
        0x101,
        "#5105F#11Pあ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3951")

    #C0139
    ChrTalk(
        0x102,
        "#5301F#11P（マフィアの若頭……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_39BE")

    label("loc_3951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_398B")

    #C0140
    ChrTalk(
        0x103,
        "#5401F#11P（マフィアの若頭さん……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_39BE")

    label("loc_398B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_39BE")

    #C0141
    ChrTalk(
        0x104,
        "#5607F#11P（《キリングベア》か……）\x02",
    )

    CloseMessageWindow()

    label("loc_39BE")

    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_39FB")

    def lambda_39F3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39F3)

    label("loc_39FB")


    def lambda_3A00():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3A00)
    Sleep(50)

    def lambda_3A10():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3A10)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)

    #C0142
    ChrTalk(
        0x1A,
        (
            "#3104F#6Pおっと、こいつは失礼。\x02\x03",

            "#3100F当会場の警備を担当している\x01",
            "ガルシア・ロッシといいます。\x02\x03",

            "防犯のため見回ってる最中でして、\x01",
            "お見苦しいでしょうがご容赦を。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#5112F#11P……いや。\x01",
            "見回り、ご苦労さまだね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3B36")

    #C0144
    ChrTalk(
        0x102,
        "#5308F#11P（何とか凌#2Rしの#がないと……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_3B36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3B6E")

    #C0145
    ChrTalk(
        0x103,
        "#5408F#11P（何とか離脱しないと……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_3B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3BA7")

    #C0146
    ChrTalk(
        0x104,
        "#5608F#11P（何とか躱#2Rかわ#せるか……？）\x02",
    )

    CloseMessageWindow()

    label("loc_3BA7")

    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(3300, 1600, 20000, 2500)

    def lambda_3BD2():
        OP_95(0xFE, 2500, 500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3BD2)
    Sleep(300)
    Sound(1856, 255, 100, 0)    #voice#Garcia
    WaitChrThread(0x1A, 1)
    OP_6F(0x1)

    #C0147
    ChrTalk(
        0x1A,
        (
            "#3105F#6Pお客さん、どこかで\x01",
            "見かけた事があるような……\x02\x03",

            "#3101F……ん～……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0148
    ChrTalk(
        0x101,
        (
            "#5104F#11P……気のせいじゃないかな？\x02\x03",

            "#5100Fあなたみたいな大柄な人、\x01",
            "一度見たら忘れないだろうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x1A,
        (
            "#3109F#6Pはは、そうかもしれませんな。\x02\x03",

            "#3100Fふむ……念のため\x01",
            "名前を伺ってもいいですかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#5103F#11P……ああ、構わないよ。\x02\x03",

            "#5100F──初めまして。\x01",
            "ガイ・バニングスという。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x1A,
        (
            "#3105F#6Pガイ……？\x02\x03",

            "はて、その名前も\x01",
            "どこかで聞いたような……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3E33")
    TurnDirection(0x1A, 0x104, 500)
    Sleep(300)

    #C0152
    ChrTalk(
        0x1A,
        "#3101F#6Pそれに、そちらの御仁は……\x02",
    )

    CloseMessageWindow()

    label("loc_3E33")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0xEF)

    #C0153
    ChrTalk(
        0x101,
        "#5110F#11P（くっ……マズったか……！？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3EC2")

    #C0154
    ChrTalk(
        0x102,
        "#5301F#11P（ど、どうしたら……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F27")

    label("loc_3EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3EF4")

    #C0155
    ChrTalk(
        0x103,
        "#5401F#11P（絶体絶命です……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F27")

    label("loc_3EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3F27")

    #C0156
    ChrTalk(
        0x104,
        "#5610F#11P（チッ、こうなったら……）\x02",
    )

    CloseMessageWindow()

    label("loc_3F27")


    #N0157
    NpcTalk(
        0x1B,
        "女性の声",
        (
            "#5P──ふふ。\x01",
            "遅れてしまいましたわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3FAC():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FAC)

    def lambda_3FB9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3FB9)
    Sleep(100)

    def lambda_3FC9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3FC9)

    def lambda_3FD6():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3FD6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)

    def lambda_3FF3():

        label("loc_3FF3")

        TurnDirection(0x15, 0x1B, 500)
        Yield()
        Jump("loc_3FF3")

    QueueWorkItem2(0x15, 1, lambda_3FF3)
    OP_68(2700, 1600, 19140, 3000)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_4021():
        OP_95(0xFE, 1820, 500, 17630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4021)
    WaitChrThread(0x1B, 1)
    OP_6F(0x1)
    EndChrThread(0x15, 0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0158
    ChrTalk(
        0x101,
        "#5105F#11Pへ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_40BA")

    #C0159
    ChrTalk(
        0x102,
        "#5305F#11Pベ、ベル……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4123")

    label("loc_40BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_40EE")

    #C0160
    ChrTalk(
        0x103,
        "#5405F#11Pマリアベルさん……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4123")

    label("loc_40EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4123")

    #C0161
    ChrTalk(
        0x104,
        "#5605F#11Pマリアベルのお嬢さん……！？\x02",
    )

    CloseMessageWindow()

    label("loc_4123")

    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0162
    AnonymousTalk(
        0x1B,
        (
            "ふふ……\x01",
            "こんばんは、“ガイ”さん。\x02\x03",

            "こんな場所で会えるなんて\x01",
            "本当に奇遇ですわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0163
    ChrTalk(
        0x101,
        "#5112F#11Pえ、ええ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_422F")

    #C0164
    ChrTalk(
        0x102,
        "#5306F#11P本当に……予想外だわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4290")

    label("loc_422F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4261")

    #C0165
    ChrTalk(
        0x103,
        "#5406F#11P確かに予想外です……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4290")

    label("loc_4261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4290")

    #C0166
    ChrTalk(
        0x104,
        "#5606F#11P……確かに奇遇ッスね。\x02",
    )

    CloseMessageWindow()

    label("loc_4290")


    #C0167
    ChrTalk(
        0x1A,
        (
            "#3105F#5Pふむ……\x01",
            "お嬢さんはどちらさまで？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x1B,
        (
            "#2904F#12Pわたくしの名は\x01",
            "マリアベル・クロイス。\x02\x03",

            "#2902Fお見知りおき願いますわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0169
    ChrTalk(
        0x15,
        "#5PＩＢＣの……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x1A,
        (
            "#3104F#5Pこれはこれは……\x01",
            "上から話は聞いておりましたよ。\x02\x03",

            "#3100F今年はついに招待に\x01",
            "応じてくださったわけですな？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x1B,
        (
            "#2904F#12Pふふ、何度も断るのも\x01",
            "さすがに失礼かと思いまして。\x02\x03",

            "#2900Fこちらの方々は\x01",
            "わたくしの友人ですけど……\x02\x03",

            "何か問題でもありまして？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x1A,
        (
            "#3104F#5Pいやいや、とんでもない。\x02\x03",

            "#3100F改めまして──\x01",
            "ようこそ《黒の競売会#10Rシュバルツオークション#》へ。\x02\x03",

            "まずはハルトマン議長に\x01",
            "ご案内いたしましょうかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x1B,
        (
            "#2904F#12Pふふ、議長閣下には\x01",
            "後ほど改めて挨拶しますわ。\x02\x03",

            "#2902Fそれより出来れば\x01",
            "お部屋をご用意してくださる？\x02\x03",

            "先ほどまで商談をしていたので\x01",
            "少し休憩したいのですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x1A,
        "#3104F#5Pかしこまりました。\x02",
    )

    CloseMessageWindow()
    OP_68(3030, 1600, 20130, 1200)
    OP_93(0x1A, 0x0, 0x190)
    OP_6F(0x1)

    #C0175
    ChrTalk(
        0x1A,
        (
            "#3100F#12P──おい。\x01",
            "マリアベルお嬢様が部屋をご所望だ。\x02\x03",

            "くれぐれも粗相の無いようにな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x8, 0x1A, 500)
    Sleep(500)

    #C0176
    ChrTalk(
        0x8,
        (
            "#5Pは、はい。\x01",
            "それでは案内させて頂きます。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    AddParty(0x37, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    NewScene("t117B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_329D end

    def Function_19_46B8(): pass

    label("Function_19_46B8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-80, 1800, 19610, 0)
    MoveCamera(52, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -600, 500, 25200, 180)
    SetChrPos(0xEF, 600, 500, 25200, 180)
    SetChrPos(0x151, 0, 500, 24000, 180)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    FadeToBright(1000, 0)
    SetCameraDistance(17000, 3000)

    def lambda_475A():
        OP_95(0xFE, 0, 500, 19000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_475A)
    Sleep(100)

    def lambda_4777():
        OP_95(0xFE, -600, 500, 20200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4777)
    Sleep(50)

    def lambda_4794():
        OP_95(0xFE, 600, 500, 20200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4794)

    def lambda_47AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_47AE)

    def lambda_47BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_47BF)

    def lambda_47D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_47D0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x151, 1)
    OP_6F(0x10)
    OP_0D()
    OP_93(0x151, 0x0, 0x1F4)

    #C0177
    ChrTalk(
        0x151,
        (
            "#5703F#12P（庭に放たれていた番犬が\x01",
            "  何匹も眠っていた……）\x02\x03",

            "#5702F（フフ、何を意味してるのかな？）\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#5103F#5P（ああ、考えられるとすれば──）\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0179
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K何を意味している？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【侵入者が現れた】\x01",            # 0
            "【マフィアの仕掛けた罠】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_491D"),
        (1, "loc_4A7E"),
        (SWITCH_DEFAULT, "loc_4B58"),
    )


    label("loc_491D")

    OP_2C(0x47, 0x1)

    #C0180
    ChrTalk(
        0x101,
        (
            "#5113F#5P（何らかの侵入者が現れた……\x01",
            "  その可能性が高いかもしれない。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xEF, 0xE1, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_49AF")

    #C0181
    ChrTalk(
        0x102,
        "#5301F#5P（なるほど……確かに。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A12")

    label("loc_49AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_49E6")

    #C0182
    ChrTalk(
        0x103,
        "#5401F#5P（……そういう事ですか。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A12")

    label("loc_49E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4A12")

    #C0183
    ChrTalk(
        0x104,
        "#5601F#5P（ああ、同感だぜ。）\x02",
    )

    CloseMessageWindow()

    label("loc_4A12")


    #C0184
    ChrTalk(
        0x151,
        (
            "#5704F#12P（いずれにしても\x01",
            "  何かが起ころうとしている……）\x02\x03",

            "#5702F（それだけは確かみたいだね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B58")

    label("loc_4A7E")


    #C0185
    ChrTalk(
        0x101,
        (
            "#5108F#5P（マフィアの仕掛けた罠……\x01",
            "  って線もありそうだけど。）\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x151,
        (
            "#5706F#12P（さすがにそれは\x01",
            "  深読みしすぎだと思うけど。）\x02\x03",

            "#5702F（いずれにしても\x01",
            "  何かが起ころうとしているのだけは\x01",
            "  確かみたいだね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B58")

    label("loc_4B58")


    #C0187
    ChrTalk(
        0x101,
        (
            "#5101F#5P（ああ、念のため\x01",
            "  屋敷の中を一通り回ってみよう。\x02\x03",

            "（異変に気付けるかもしれない。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xEF, 0xE1, 0x1F4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4BEC")

    #C0188
    ChrTalk(
        0x102,
        "#5301F#5P（ええ……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C49")

    label("loc_4BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4C1F")

    #C0189
    ChrTalk(
        0x103,
        "#5401F#5P（……了解しました。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C49")

    label("loc_4C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4C49")

    #C0190
    ChrTalk(
        0x104,
        "#5601F#5P（合点承知だぜ。）\x02",
    )

    CloseMessageWindow()

    label("loc_4C49")


    #C0191
    ChrTalk(
        0x151,
        (
            "#5709F#12P（フフ……\x01",
            "  僕も付き合わせてもらうよ。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 500, 18770, 180)
    SetScenarioFlags(0xA6, 2)
    OP_29(0x47, 0x1, 0xC)
    EventEnd(0x5)
    Return()

    # Function_19_46B8 end

    def Function_20_4CA2(): pass

    label("Function_20_4CA2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("chr/ch31900.itc", 0x20)
    LoadChrToIndex("chr/ch02200.itc", 0x21)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 2000, 500, 18000, 270)
    SetChrPos(0x14, -1000, 500, 19600, 90)
    SetChrPos(0x15, -1000, 500, 18000, 90)
    SetChrPos(0x16, -1000, 500, 16400, 90)
    SetChrPos(0x17, -2400, 500, 19600, 90)
    SetChrPos(0x18, -2400, 500, 18000, 90)
    SetChrPos(0x19, -2400, 500, 16400, 90)
    OP_52(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(4059, 1700, 17050, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(1000, 0)
    OP_68(60, 1700, 18000, 2500)
    OP_6F(0x1)
    OP_0D()

    #C0192
    ChrTalk(
        0x1A,
        (
            "#3104F#11Pクク……\x01",
            "やはりネズミが出やがったか。\x02\x03",

            "#3107F──てめえら、狩りを始めるぞ！\x02\x03",

            "客はオークション会場に隔離して、\x01",
            "屋敷の出口は完全に封鎖しろ！\x02\x03",

            "ネズミ一匹、逃がすんじゃねえぞ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(80, 140, -1, -1)
    SetChrName("マフィアたち")
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)

    #A0193
    AnonymousTalk(
        0xFF,
        "#4S承知しました！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0xA6, 7)
    OP_29(0x47, 0x1, 0x10)
    SetScenarioFlags(0x5C, 0)
    NewScene("t119B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_4CA2 end

    def Function_21_4F48(): pass

    label("Function_21_4F48")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("chr/ch31900.itc", 0x20)
    LoadChrToIndex("chr/ch02200.itc", 0x21)
    LoadChrToIndex("chr/ch06200.itc", 0x22)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 0, 500, 19500, 180)
    SetChrPos(0x1A, 0, 500, 17500, 0)
    SetChrPos(0x14, 0, 500, 16000, 0)
    SetChrPos(0x15, 1500, 500, 16000, 0)
    SetChrPos(0x16, -1500, 500, 16000, 0)
    OP_52(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-4990, 1700, 17500, 0)
    MoveCamera(325, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1700, 17500, 2500)
    OP_6F(0x1)
    OP_0D()

    #C0194
    ChrTalk(
        0x1C,
        (
            "#3007F#11P──ええい！\x01",
            "まだ侵入者は見つからんのか！\x02\x03",

            "そろそろ招待客が\x01",
            "騒ぎ始めておるのだぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x1A,
        (
            "#3103F#6P……どうかしばしお待ちを。\x02\x03",

            "#3100F屋敷は完全に封鎖しました。\x01",
            "袋のネズミってやつです。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x1C,
        (
            "#3003F#11Pクッ……\x01",
            "このままでは議長の機嫌が……\x02\x03",

            "#3007Fいいからとっとと捕まえるのだ！\x02\x03",

            "場合によっては殺しても構わん！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0xA7, 1)
    SetScenarioFlags(0x5C, 1)
    NewScene("t119B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_4F48 end

    def Function_22_51E9(): pass

    label("Function_22_51E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00450.itc", 0x26)
    LoadChrToIndex("chr/ch00451.itc", 0x27)
    LoadChrToIndex("chr/ch31000.itc", 0x28)
    LoadChrToIndex("chr/ch31100.itc", 0x29)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_525B")
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_5282")

    label("loc_525B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5271")
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_5282")

    label("loc_5271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5282")
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    label("loc_5282")

    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    SetChrChipByIndex(0x17, 0x28)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x29)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x17, 0, 500, 19600, 180)
    SetChrPos(0x18, 0, 500, 18000, 0)
    SetChrPos(0x101, -10780, 500, 16940, 90)
    SetChrPos(0xEF, -10780, 500, 16940, 90)
    SetChrPos(0x105, -10780, 500, 16940, 90)
    SetChrPos(0x133, -10780, 500, 16940, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x133, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-1500, 1600, 19000, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1600, 19000, 2500)
    OP_6F(0x1)
    OP_0D()

    #C0197
    ChrTalk(
        0x101,
        "#0000F#2P（よし、あの数なら……！）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_53F7")

    #C0198
    ChrTalk(
        0x102,
        "#0100F#2P（強行突破しましょう……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_545A")

    label("loc_53F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_542C")

    #C0199
    ChrTalk(
        0x103,
        "#0202F#2P（強行突破ですね……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_545A")

    label("loc_542C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_545A")

    #C0200
    ChrTalk(
        0x104,
        "#0300F#2P（強行突破だな……！）\x02",
    )

    CloseMessageWindow()

    label("loc_545A")


    #C0201
    ChrTalk(
        0x105,
        "#0400F#2P（行こうか……！）\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_54A7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_54A7)
    Sleep(50)

    def lambda_54B7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_54B7)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x18, 1)

    #C0202
    ChrTalk(
        0x17,
        "#11Pん……？\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x18,
        "#11Pえ……\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_68(-2130, 1400, 19140, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22800, 0)
    SetCameraDistance(19800, 2000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x133, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, -9740, 500, 18820, 90)
    SetChrPos(0xEF, -11480, 500, 18040, 90)
    SetChrPos(0x105, -11140, 500, 19670, 90)
    SetChrPos(0x133, -12980, 500, 18940, 90)

    def lambda_559A():
        OP_95(0xFE, -4740, 500, 18820, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_559A)
    Sleep(50)

    def lambda_55B7():
        OP_95(0xFE, -6480, 500, 18040, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_55B7)
    Sleep(50)

    def lambda_55D4():
        OP_95(0xFE, -6140, 500, 19670, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_55D4)
    Sleep(100)

    def lambda_55F1():
        OP_95(0xFE, -7980, 500, 18940, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_55F1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x133, 1)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0204
    ChrTalk(
        0x17,
        "#11Pなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x18,
        "#11P外に出たんじゃ！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_56A8")

    #C0206
    ChrTalk(
        0x102,
        "#0107F#6P遅い……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_56F5")

    label("loc_56A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_56D3")

    #C0207
    ChrTalk(
        0x103,
        "#0207F#6P遅いです……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_56F5")

    label("loc_56D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_56F5")

    #C0208
    ChrTalk(
        0x104,
        "#0307F#3P遅ぇ……！\x02",
    )

    CloseMessageWindow()

    label("loc_56F5")

    SetCameraDistance(15800, 300)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_5715():
        OP_95(0xFE, -740, 500, 18820, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5715)

    def lambda_572F():
        OP_95(0xFE, -2480, 500, 18040, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_572F)

    def lambda_5749():
        OP_95(0xFE, -2980, 500, 19260, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5749)
    Sleep(300)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x105, 0x1)
    Battle("BattleInfo_464", 0x0, 0x0, 0x0, 0x11, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 23)
    Return()

    # Function_22_51E9 end

    def Function_23_578B(): pass

    label("Function_23_578B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00450.itc", 0x26)
    LoadChrToIndex("chr/ch00451.itc", 0x27)
    LoadChrToIndex("chr/ch31000.itc", 0x28)
    LoadChrToIndex("chr/ch31100.itc", 0x29)
    LoadChrToIndex("chr/ch31053.itc", 0x2A)
    LoadChrToIndex("chr/ch31153.itc", 0x2B)
    LoadChrToIndex("chr/ch06200.itc", 0x2C)
    LoadChrToIndex("chr/ch06500.itc", 0x2D)
    LoadChrToIndex("chr/ch05500.itc", 0x2E)
    LoadChrToIndex("chr/ch00000.itc", 0x2F)
    LoadChrToIndex("apl/ch50364.itc", 0x30)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrSubChip(0x17, 0x3)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x2B)
    SetChrSubChip(0x18, 0x3)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x17, 3470, 500, 19830, 270)
    SetChrPos(0x18, 2770, 500, 17960, 270)
    SetChrChipByIndex(0x1C, 0x2C)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x2D)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1B, 0x2E)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1C, 0x8000)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1D, 0x8000)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1B, 0x8000)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1C, 0, 4000, 33000, 180)
    SetChrPos(0x1D, 600, 500, 28500, 180)
    SetChrPos(0x1B, 0, 1500, 32500, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_58E8")
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_590F")

    label("loc_58E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_58FE")
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_590F")

    label("loc_58FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_590F")
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    label("loc_590F")

    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, -50, 500, 18760, 90)
    SetChrPos(0xEF, -950, 500, 19580, 90)
    SetChrPos(0x105, -1080, 500, 17400, 90)
    SetChrPos(0x133, -2650, 500, 18280, 90)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    OP_68(0, 1400, 19000, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18750, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(18000, 1500)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x101, 0x2F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(100)

    def lambda_59D4():
        TurnDirection(0xFE, 0x133, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59D4)

    def lambda_59E1():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_59E1)
    Sleep(100)

    def lambda_59F1():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_59F1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    Sleep(100)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)

    #N0209
    NpcTalk(
        0x1C,
        "男の声",
        (
            "#4Pええい、騒がしいぞ！\x01",
            "まだ見つからんのか──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x133, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5AB5():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AB5)

    def lambda_5AC2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5AC2)
    Sleep(100)

    def lambda_5AD2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5AD2)

    def lambda_5ADF():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_5ADF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x133, 1)
    Sleep(100)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrPos(0x1C, -600, 500, 28500, 180)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Fade(500)
    OP_68(-560, 1600, 22180, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18650, 0)

    def lambda_5B58():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5B58)
    WaitChrThread(0x1C, 1)
    OP_0D()
    OP_63(0x1C, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0210
    ChrTalk(
        0x1C,
        (
            "#3005F#5Pな……\x01",
            "お、お前たちは！？\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x133,
        "#5805F#12P#Nあ、まるっこいヒト！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5C09")

    #C0212
    ChrTalk(
        0x102,
        "#0101F#12Pマルコーニ会長……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C6E")

    label("loc_5C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5C3F")

    #C0213
    ChrTalk(
        0x103,
        "#0201F#12Pマフィアの会長さん……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C6E")

    label("loc_5C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5C6E")

    #C0214
    ChrTalk(
        0x104,
        "#0307F#12Pマフィアのボスか……！\x02",
    )

    CloseMessageWindow()

    label("loc_5C6E")

    OP_93(0x101, 0x10E, 0x1F4)

    #C0215
    ChrTalk(
        0x101,
        (
            "#0007F#11P問題ない！\x01",
            "このまま脱出するぞ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CA9():
        OP_95(0xFE, -800, 500, 18640, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_5CA9)
    WaitChrThread(0x133, 1)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x30)
    SetChrSubChip(0x101, 0x5)
    Sound(910, 0, 100, 0)
    Sleep(250)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x133, 0x80)
    SetChrBattleFlags(0x133, 0x8000)
    OP_0D()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0216
    ChrTalk(
        0x105,
        "#0402F#12Pアリヴェデルチ#14Rさ　よ　う　な　ら#！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20650, 2000)
    BeginChrThread(0x105, 3, 0, 24)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 24)
    Sleep(100)
    BeginChrThread(0xEF, 3, 0, 24)
    OP_63(0x1C, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x1C)
    Sleep(300)
    OP_63(0x1C, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    OP_6F(0x10)

    #C0217
    ChrTalk(
        0x1C,
        "#3001F#5Pな、な、な……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0218
    ChrTalk(
        0x1C,
        "#3007F#5P#4S何をやっておる、お前たち！\x02",
    )

    CloseMessageWindow()
    OP_68(1030, 1600, 20870, 1500)
    SetCameraDistance(16780, 1500)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_5E39():
        OP_95(0xFE, 690, 500, 21650, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5E39)
    WaitChrThread(0x1C, 1)
    OP_93(0x1C, 0x87, 0x1F4)
    OP_6F(0x1)

    #C0219
    ChrTalk(
        0x1C,
        (
            "#3007F#5P起きろ、起きんか！\x02\x03",

            "#3001Fええい……\x01",
            "ガルシアは何をやっておる！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-940, 2500, 27990, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18500, 0)
    OP_68(-940, 2500, 29990, 4000)
    Sleep(1500)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    BeginChrThread(0x1B, 3, 0, 25)
    WaitChrThread(0x1B, 3)
    SetChrFlags(0x1B, 0x4)
    OP_6F(0x1)
    OP_0D()

    #C0220
    ChrTalk(
        0x1B,
        (
            "#2902F#5P（フフ……\x01",
            "  面白い事になってますわね。）\x02\x03",

            "#2905F（しかし、ロイドさんが\x01",
            "  抱きかかえていたあの子は……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5FAC")
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_5FD3")

    label("loc_5FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5FC2")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_5FD3")

    label("loc_5FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5FD3")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_5FD3")

    SetScenarioFlags(0x5C, 0)
    NewScene("t110B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_578B end

    def Function_24_5FE0(): pass

    label("Function_24_5FE0")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_5FEC():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FEC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_5FE0 end

    def Function_25_6001(): pass

    label("Function_25_6001")


    def lambda_6006():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6006)

    def lambda_601B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_601B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_25_6001 end

    def Function_26_6030(): pass

    label("Function_26_6030")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60A4")

    #C0221
    ChrTalk(
        0x101,
        (
            "#5101F（せっかく潜入できたんだ……\x01",
            "  オークション開催まで、\x01",
            "  もう少し屋敷の中を見て回ろう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6161")

    #C0222
    ChrTalk(
        0x138,
        (
            "#2905Fあら、会場に行きませんの？\x01",
            "オークション会場は\x01",
            "そこの広間ですわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#5105Fおっと、そうですね。\x02\x03",

            "#5100Fせっかくなので\x01",
            "ご一緒させてもらいます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_61A9")

    label("loc_6161")


    #C0224
    ChrTalk(
        0x101,
        (
            "#5101F会場は正面の広間だ。\x01",
            "……怪しまれないように\x01",
            "行動しないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_61F7")

    #C0225
    ChrTalk(
        0x101,
        (
            "#5101Fどうも様子が気になる……\x01",
            "もう少し屋敷の中を回ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61F7")

    Sleep(50)
    SetChrPos(0x0, 0, 0, -1030, 360)
    EventEnd(0x4)
    Return()

    # Function_26_6030 end

    SaveToFile()

Try(main)
