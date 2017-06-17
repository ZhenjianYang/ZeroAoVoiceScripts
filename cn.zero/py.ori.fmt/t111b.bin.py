from ZeroScenarioHelper import *

def main():
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
        "向导巴克雷",             # 1
        "尼基塔",                 # 2
        "艾维琳夫人",             # 3
        "詹姆斯",                 # 4
        "黑衣人",                 # 5
        "黑衣人",                 # 6
        "客人",                   # 7
        "客人",                   # 8
        "客人",                   # 9
        "客人",                   # 10
        "客人",                   # 11
        "客人",                   # 12
        "黑衣人",                 # 13
        "黑衣人",                 # 14
        "黑衣人",                 # 15
        "黑手党",                 # 16
        "黑手党",                 # 17
        "黑手党",                 # 18
        "加尔西亚",               # 19
        "玛丽亚贝尔",             # 20
        "马尔克尼会长",           # 21
        "哈尔特曼议长",           # 22
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
        "Function_5_89F",          # 05, 5
        "Function_6_900",          # 06, 6
        "Function_7_961",          # 07, 7
        "Function_8_A3F",          # 08, 8
        "Function_9_C25",          # 09, 9
        "Function_10_DEA",         # 0A, 10
        "Function_11_E47",         # 0B, 11
        "Function_12_ED4",         # 0C, 12
        "Function_13_FAB",         # 0D, 13
        "Function_14_111F",        # 0E, 14
        "Function_15_1190",        # 0F, 15
        "Function_16_122D",        # 10, 16
        "Function_17_1A84",        # 11, 17
        "Function_18_2C8D",        # 12, 18
        "Function_19_3EA7",        # 13, 19
        "Function_20_4419",        # 14, 20
        "Function_21_468D",        # 15, 21
        "Function_22_4900",        # 16, 22
        "Function_23_4E92",        # 17, 23
        "Function_24_5691",        # 18, 24
        "Function_25_56B2",        # 19, 25
        "Function_26_56E1",        # 1A, 26
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
    Jump("loc_89B")

    label("loc_76D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_7BA")

    #C0001
    ChrTalk(
        0xFE,
        "哎呀……二位有事吗？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "拍卖即将开始，\x01",
            "请尽快入座等待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89B")

    label("loc_7BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_7C8")
    Jump("loc_89B")

    label("loc_7C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_89B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_853")

    #C0003
    ChrTalk(
        0xFE,
        (
            "竞拍会将于晚上九点\x01",
            "在那边正面的大厅里\x01",
            "举行。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "在此之前，左手边的客厅里\x01",
            "设有宴席，\x01",
            "请尽情享用美酒佳肴。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_89B")

    label("loc_853")


    #C0005
    ChrTalk(
        0xFE,
        (
            "如果您需要在客房休息，\x01",
            "请尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "我会立即\x01",
            "为您准备好房间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89B")

    TalkEnd(0xFE)
    Return()

    # Function_4_75C end

    def Function_5_89F(): pass

    label("Function_5_89F")

    TalkBegin(0xFE)

    #C0007
    ChrTalk(
        0xFE,
        (
            "正好有\x01",
            "单独来的客人，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "詹姆斯先生\x01",
            "声名显赫……\x01",
            "现在这个人又如何呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_89F end

    def Function_6_900(): pass

    label("Function_6_900")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        (
            "我先生说，作为和好的证明，\x01",
            "要特别给我拍个\x01",
            "漂亮的珠宝首饰。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "呵呵……真是期待呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_900 end

    def Function_7_961(): pass

    label("Function_7_961")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A19")
    OP_4B(0xA, 0xFF)

    #C0011
    ChrTalk(
        0xB,
        (
            "……刚才向导过来的时候，\x01",
            "要是让他帮我占个位置就好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0012
    ChrTalk(
        0xA,
        "哎呀，为什么呢？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        (
            "（因为万一和尼基塔\x01",
            "  坐得很近，\x01",
            "  那可就尴尬了啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_A3B")

    label("loc_A19")


    #C0014
    ChrTalk(
        0xB,
        (
            "算、算了，\x01",
            "总之先进\x01",
            "会场吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3B")

    TalkEnd(0xFE)
    Return()

    # Function_7_961 end

    def Function_8_A3F(): pass

    label("Function_8_A3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_A50")
    Jump("loc_C21")

    label("loc_A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_BAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5C")

    #C0015
    ChrTalk(
        0xFE,
        (
            "客人……\x01",
            "您怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "这样随便走动可不太好啊。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#5101F（黑衣人们似乎\x01",
            "  还没注意到异常啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x151,
        (
            "#5703F（呵呵，这不是正好吗？\x01",
            "  要调查的话，还是在出现骚动\x01",
            "  之前进行为好哦。）\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#5101F（是啊……趁现在\x01",
            "  把宅邸都转一遍吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BA8")

    label("loc_B5C")


    #C0020
    ChrTalk(
        0xFE,
        "……您忘了什么在房间里吗？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "竞拍会的开场\x01",
            "是不等人的，\x01",
            "请您尽快吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA8")

    Jump("loc_C21")

    label("loc_BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_BDC")

    #C0022
    ChrTalk(
        0xFE,
        (
            "竞拍会即将开始，\x01",
            "请进会场。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C21")

    label("loc_BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_C21")

    #C0023
    ChrTalk(
        0xFE,
        (
            "宅邸内的安全，\x01",
            "我们会负责保卫的。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "请放心\x01",
            "享受吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C21")

    TalkEnd(0xFE)
    Return()

    # Function_8_A3F end

    def Function_9_C25(): pass

    label("Function_9_C25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_C36")
    Jump("loc_DE6")

    label("loc_C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_CA5")
    OP_93(0xFE, 0xB4, 0x0)

    #C0025
    ChrTalk(
        0xFE,
        (
            "我们准备了足够的座位，\x01",
            "请您随意寻找空位就坐。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "虽然是站席，\x01",
            "但二楼也可以使用哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE6")

    label("loc_CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_D9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D56")

    #C0027
    ChrTalk(
        0xFE,
        (
            "二位是玛丽亚贝尔小姐的友人吗？\x01",
            "向导吩咐过我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "已经为各位准备了\x01",
            "最后一排的席位，\x01",
            "请入内跟随向导就坐。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x138,
        (
            "#2900F别客气。\x01",
            "……来，进去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_D99")

    label("loc_D56")


    #C0030
    ChrTalk(
        0xFE,
        (
            "二位是玛丽亚贝尔小姐的友人吗？\x01",
            "已经为各位准备了最后排的席位。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D99")

    Jump("loc_DE6")

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_DE6")

    #C0031
    ChrTalk(
        0xFE,
        (
            "会场内正在进行\x01",
            "竞拍会的准备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "请您耐心等候开场。\x02",
    )

    CloseMessageWindow()

    label("loc_DE6")

    TalkEnd(0xFE)
    Return()

    # Function_9_C25 end

    def Function_10_DEA(): pass

    label("Function_10_DEA")

    TalkBegin(0xFE)

    #C0033
    ChrTalk(
        0xFE,
        (
            "我这是第一次跟我先生\x01",
            "来议长宅邸。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "一想到即将举行的竞拍会，\x01",
            "我就期待万分呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_DEA end

    def Function_11_E47(): pass

    label("Function_11_E47")

    TalkBegin(0xFE)

    #C0035
    ChrTalk(
        0xFE,
        (
            "我太太平时很娴静。\x01",
            "我想让她感受点刺激的场面，\x01",
            "所以就带她来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "为了在社交界生存，\x01",
            "必须学学与贵妇人\x01",
            "的身份相符合的言行举止。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_E47 end

    def Function_12_ED4(): pass

    label("Function_12_ED4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F53")

    #C0037
    ChrTalk(
        0xFE,
        (
            "虽然我在帝国也有宅邸，\x01",
            "但和这幢大宅比起来\x01",
            "可就逊色多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "豪华绚烂这种词汇，形容的就是这里啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_FA7")

    label("loc_F53")


    #C0039
    ChrTalk(
        0xFE,
        (
            "我在帝国的宅邸\x01",
            "虽然也很大……\x01",
            "不过和这幢大宅就不能比了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "真是让人羡慕啊。\x02",
    )

    CloseMessageWindow()

    label("loc_FA7")

    TalkEnd(0xFE)
    Return()

    # Function_12_ED4 end

    def Function_13_FAB(): pass

    label("Function_13_FAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AE")

    #C0041
    ChrTalk(
        0xFE,
        "竞拍会终于快开始了啊……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "我一定要拍下\x01",
            "罗赞贝尔克工房的人偶。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x138,
        (
            "#2905F哎呀……\x01",
            "出现竞争对手了呢。\x02\x03",

            "#2900F我的目标也是那个哦，\x01",
            "呵呵……我可不会输的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x138, 500)

    #C0044
    ChrTalk(
        0xFE,
        (
            "哦哦……真是好胆量啊，小姐。\x01",
            "请手下留情哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_111B")

    label("loc_10AE")


    #C0045
    ChrTalk(
        0xFE,
        (
            "想要的东西近在眼前，\x01",
            "我也不能退让啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x138, 500)

    #C0046
    ChrTalk(
        0xFE,
        (
            "小姐，\x01",
            "还请手下留情哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x138,
        "#2900F呵呵……彼此彼此。\x02",
    )

    CloseMessageWindow()

    label("loc_111B")

    TalkEnd(0xFE)
    Return()

    # Function_13_FAB end

    def Function_14_111F(): pass

    label("Function_14_111F")

    TalkBegin(0xFE)

    #C0048
    ChrTalk(
        0xFE,
        (
            "我先生真是的，随着开始时间的临近，\x01",
            "好像越来越兴奋了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "等到入席之后，\x01",
            "必须得让他冷静一下才行啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_111F end

    def Function_15_1190(): pass

    label("Function_15_1190")

    TalkBegin(0xFE)

    #C0050
    ChrTalk(
        0xFE,
        (
            "（这位女性刚才\x01",
            "　向我搭讪，\x01",
            "　所以就决定一起参加竞拍会了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "（如果没有同伴，\x01",
            "　还是有点没面子呢。\x01",
            "　呵呵，有个正合适的女人，真是得救了。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1190 end

    def Function_16_122D(): pass

    label("Function_16_122D")

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

    def lambda_1334():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1334)
    Sleep(200)

    def lambda_134C():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_134C)

    def lambda_1361():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1361)

    def lambda_1372():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_1372)
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
        "#5105F#12P这、这里可真是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_141C")

    #C0053
    ChrTalk(
        0x102,
        (
            "#5301F#6P哈尔特曼议长宅邸……\x02\x03",

            "虽然听过传闻，\x01",
            "但没想到竟是如此宏伟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EF")

    label("loc_141C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1485")

    #C0054
    ChrTalk(
        0x103,
        (
            "#5406F#6P与其说是宅邸，\x01",
            "感觉倒更像是城堡呢……\x02\x03",

            "#5401F光是维护，似乎\x01",
            "就要花很多钱吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EF")

    label("loc_1485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_14EF")

    #C0055
    ChrTalk(
        0x104,
        (
            "#5605F#6P咻～！\x01",
            "这宅子可真是不得了啊。\x02\x03",

            "#5601F像这种宅子，就连帝国\x01",
            "的大贵族也要望而兴叹吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EF")


    #C0056
    ChrTalk(
        0x101,
        (
            "#5106F#12P嗯……这种豪华程度真是超乎预想啊。\x02\x03",

            "#5108F（哈尔特曼议长……\x01",
            "  还有『鲁巴彻』……）\x02\x03",

            "#5113F（竟然拥有如此强大的财力吗……）\x02",
        )
    )

    CloseMessageWindow()

    #N0057
    NpcTalk(
        0x8,
        "男性的声音",
        "#11P──欢迎，两位客人。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_15CF():
        OP_95(0xFE, 0, 500, 14060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_15CF)
    WaitChrThread(0x8, 1)

    #C0058
    ChrTalk(
        0x8,
        "#5P欢迎参加『黑之竞拍会』。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#5P二位是……\x01",
            "第一次参加吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#5100F#12P嗯，是的。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "#5P竞拍会将于晚上九点\x01",
            "在那边正面的会场里\x01",
            "举行。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#5P在此之前，左手边的客厅里\x01",
            "设有宴席，\x01",
            "请尽情享用美酒佳肴。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#5P顺便问一下，二位今夜\x01",
            "打算在本馆留宿吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#5105F#12P啊，不……\x02\x03",

            "#5104F我们在酒店订了房间，\x01",
            "而且还有朋友在等我们。\x02\x03",

            "#5100F这次就不麻烦您啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        "#5P好的。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "#5P如果您改变主意的话，\x01",
            "我们可以马上为您准备房间，\x01",
            "请不必客气，尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#5P此外，您可以在宅邸内\x01",
            "随意参观……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "#5P不过有几个区域\x01",
            "谢绝入内，\x01",
            "敬请理解。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#5100F#12P嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_185F")

    #C0070
    ChrTalk(
        0x102,
        (
            "#5302F#6P呵呵……\x01",
            "谢谢您耐心细致的指引。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C4")

    label("loc_185F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1894")

    #C0071
    ChrTalk(
        0x103,
        "#5402F#6P……多谢指引，辛苦您了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18C4")

    label("loc_1894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_18C4")

    #C0072
    ChrTalk(
        0x104,
        "#5609F#6P真是细致的指引，辛苦啦。\x02",
    )

    CloseMessageWindow()

    label("loc_18C4")


    #C0073
    ChrTalk(
        0x8,
        (
            "#5P哪里，如果有什么需要，\x01",
            "请尽管吩咐\x01",
            "我或者其他佣人。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        "#5P那么，我先失陪了……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_1928():
        OP_95(0xFE, 1910, 500, 19610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1928)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    TurnDirection(0x101, 0xEF, 500)

    #C0075
    ChrTalk(
        0x101,
        (
            "#5103F#2P（离竞拍会开始\x01",
            "  还有两个小时左右……）\x02\x03",

            "#5101F（在宅邸里转一圈看看吧。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_19DB")

    #C0076
    ChrTalk(
        0x102,
        "#5301F#1P（嗯，明白了。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A3D")

    label("loc_19DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1A06")

    #C0077
    ChrTalk(
        0x103,
        "#5401F#1P（……明白。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A3D")

    label("loc_1A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1A3D")

    #C0078
    ChrTalk(
        0x104,
        (
            "#5600F#1P（哦，随便吃点什么\x01",
            "  再去吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A3D")

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

    # Function_16_122D end

    def Function_17_1A84(): pass

    label("Function_17_1A84")

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

    def lambda_1C20():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1C20)

    def lambda_1C35():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1C35)
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
            "……哼，真奇怪啊。\x02\x03",

            "本以为他们一定会\x01",
            "有所动作的……\x02",
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
        "#6P不过，到现在还没发生异常情况呢。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x15,
        (
            "#6P就算是『黑月』，\x01",
            "也不会做出有损\x01",
            "哈尔特曼议长脸面的事情吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x1A,
        (
            "#3103F#11P蠢货，不要小看他们。\x02\x03",

            "#3101F『银』就不用说了，传闻那个曹\x01",
            "也是个聪明绝顶之人，连组织的长老\x01",
            "都要敬他三分呢。\x02\x03",

            "松懈大意的话，\x01",
            "当心性命不保。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x15,
        "#6P是、是……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x1A,
        (
            "#3103F#11P话说回来，总觉得这次的\x01",
            "竞拍会有点诡异……\x02\x03",

            "除了『黑月』以外，\x01",
            "好像还有其他什么人\x01",
            "偷偷混了进来似的……\x02\x03",

            "#3101F我总有这种感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x15,
        "#6P哎，那个……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x15,
        (
            "#6P这也是在战场上训练出来的\x01",
            "猎兵的直觉吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1A,
        (
            "#3104F#11P……算是吧。\x02\x03",

            "#3102F呵呵……\x01",
            "我也上年纪了啊。\x02\x03",

            "如果就这样平安无事地顺利结束，\x01",
            "自然是再好不过了……\x01",
            "但总觉得躁动不安。\x02\x03",

            "久违的『狩猎』欲望好像又涌现出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x15,
        "#6P哈、哈哈……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-12460, 1600, 21220, 0)
    MoveCamera(325, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(-1910, 1600, 19760, 4500)

    def lambda_1FE5():
        OP_95(0xFE, -4000, 500, 20600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FE5)
    Sleep(100)

    def lambda_2002():
        OP_95(0xFE, -4000, 500, 19400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2002)
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
        "#5105F#5P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_209F")

    #C0090
    ChrTalk(
        0x102,
        "#5301F#5P（黑手党的副头目……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2102")

    label("loc_209F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_20D4")

    #C0091
    ChrTalk(
        0x103,
        "#5401F#5P（黑手党的副头目……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2102")

    label("loc_20D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2102")

    #C0092
    ChrTalk(
        0x104,
        "#5607F#5P（『杀戮之熊』吗……）\x02",
    )

    CloseMessageWindow()

    label("loc_2102")

    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_213F")

    def lambda_2137():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2137)

    label("loc_213F")


    def lambda_2144():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2144)
    Sleep(50)

    def lambda_2154():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2154)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)

    #C0093
    ChrTalk(
        0x1A,
        (
            "#3104F#12P哦，真是失礼了。\x02\x03",

            "#3100F我是负责本会场保安工作的\x01",
            "加尔西亚·罗西。\x02\x03",

            "为了确保场内安全，正在进行巡逻，\x01",
            "如有不敬之处，还请见谅。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#5112F#5P……哪里，\x01",
            "您巡逻辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_224D")

    #C0095
    ChrTalk(
        0x102,
        "#5308F#5P（得想办法蒙混过去……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B4")

    label("loc_224D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2286")

    #C0096
    ChrTalk(
        0x103,
        "#5408F#5P（必须得想个办法脱身呢……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B4")

    label("loc_2286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_22B4")

    #C0097
    ChrTalk(
        0x104,
        "#5608F#5P（能瞒得过去吗……？）\x02",
    )

    CloseMessageWindow()

    label("loc_22B4")

    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-3300, 1600, 20000, 2500)

    def lambda_22DF():
        OP_95(0xFE, -2500, 500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_22DF)
    Sleep(300)
    Sound(1856, 255, 100, 0)    #voice#Garcia
    WaitChrThread(0x1A, 1)
    OP_6F(0x1)

    #C0098
    ChrTalk(
        0x1A,
        (
            "#3105F#12P客人，我感觉好像\x01",
            "以前在哪里见过您……\x02\x03",

            "#3101F……嗯～……？\x02",
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
            "#5104F#5P……那只是您的心理作用吧？\x02\x03",

            "#5100F像您这样高大魁梧的人，\x01",
            "只要见过一次，我应该就不会忘记的。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x1A,
        (
            "#3109F#12P哈哈，说得也是啊。\x02\x03",

            "#3100F唔……保险起见，\x01",
            "能请教一下尊姓大名吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#5103F#5P……嗯，可以啊。\x02\x03",

            "#5100F──初次见面，幸会。\x01",
            "我是盖伊·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0102
    ChrTalk(
        0x1A,
        (
            "#3105F#12P盖伊……？\x02\x03",

            "慢着，这名字\x01",
            "我好像曾在哪里听过……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2518")
    TurnDirection(0x1A, 0x104, 500)
    Sleep(300)

    #C0103
    ChrTalk(
        0x1A,
        "#3101F#12P还有，另一位客人……\x02",
    )

    CloseMessageWindow()

    label("loc_2518")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0xEF)

    #C0104
    ChrTalk(
        0x101,
        "#5110F#5P（呜……搞砸了吗……！？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_259F")

    #C0105
    ChrTalk(
        0x102,
        "#5301F#5P（该、该怎么办……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_25FE")

    label("loc_259F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_25CE")

    #C0106
    ChrTalk(
        0x103,
        "#5401F#5P（穷途末路了……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_25FE")

    label("loc_25CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_25FE")

    #C0107
    ChrTalk(
        0x104,
        "#5610F#5P（嘁，既然这样的话……）\x02",
    )

    CloseMessageWindow()

    label("loc_25FE")


    #N0108
    NpcTalk(
        0x1B,
        "女性的声音",
        (
            "#11P──呵呵，\x01",
            "我迟到了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_267A():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_267A)

    def lambda_2687():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2687)
    Sleep(100)

    def lambda_2697():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2697)

    def lambda_26A4():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_26A4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)

    def lambda_26C1():

        label("loc_26C1")

        TurnDirection(0x15, 0x1B, 500)
        Yield()
        Jump("loc_26C1")

    QueueWorkItem2(0x15, 1, lambda_26C1)
    OP_68(-2700, 1600, 19140, 3000)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_26EF():
        OP_95(0xFE, -1820, 500, 17630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_26EF)
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
        "#5105F#5P哎……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2786")

    #C0110
    ChrTalk(
        0x102,
        "#5305F#5P贝、贝尔……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_27E9")

    label("loc_2786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_27B9")

    #C0111
    ChrTalk(
        0x103,
        "#5405F#5P玛丽亚贝尔小姐……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_27E9")

    label("loc_27B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_27E9")

    #C0112
    ChrTalk(
        0x104,
        "#5605F#5P玛丽亚贝尔大小姐……！？\x02",
    )

    CloseMessageWindow()

    label("loc_27E9")

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
            "呵呵……\x01",
            "晚上好，『盖伊』先生。\x02\x03",

            "竟然会在这里碰到你，\x01",
            "真是好巧呢。\x02",
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
        "#5112F#5P嗯、是啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_28E1")

    #C0115
    ChrTalk(
        0x102,
        "#5306F#5P真是……预料之外啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_293A")

    label("loc_28E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2910")

    #C0116
    ChrTalk(
        0x103,
        "#5406F#5P的确是预料之外……\x02",
    )

    CloseMessageWindow()
    Jump("loc_293A")

    label("loc_2910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_293A")

    #C0117
    ChrTalk(
        0x104,
        "#5606F#5P……的确是好巧呢。\x02",
    )

    CloseMessageWindow()

    label("loc_293A")


    #C0118
    ChrTalk(
        0x1A,
        (
            "#3100F#11P唔……\x01",
            "这位小姐，请问您是哪位？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x1B,
        (
            "#2904F#6P我的名字是\x01",
            "玛丽亚贝尔·库罗伊斯。\x02\x03",

            "#2902F请多关照。\x02",
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
        "#11PＩＢＣ的……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x1A,
        (
            "#3104F#11P这可真是失敬……\x01",
            "上头交代过您的事。\x02\x03",

            "#3100F您今年总算\x01",
            "接受邀请了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x1B,
        (
            "#2904F#6P呵呵，拒绝了那么多次，\x01",
            "我也觉得太失礼了。\x02\x03",

            "#2900F这两位\x01",
            "是我的朋友……\x02\x03",

            "有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x1A,
        (
            "#3104F#11P不不，当然没有。\x02\x03",

            "#3100F重新打个招呼──\x01",
            "欢迎参加『黑之竞拍会』。\x02\x03",

            "要不要先带您去见\x01",
            "哈尔特曼议长呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x1B,
        (
            "#2904F#6P呵呵，我稍后\x01",
            "再自行去拜会议长阁下吧。\x02\x03",

            "#2902F话说回来，\x01",
            "能不能帮我准备个房间？\x02\x03",

            "之前一直在谈生意，\x01",
            "想稍微休息一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x1A,
        "#3104F#11P遵命。\x02",
    )

    CloseMessageWindow()
    OP_68(-3030, 1600, 20130, 1200)
    OP_93(0x1A, 0x0, 0x190)
    OP_6F(0x1)

    #C0126
    ChrTalk(
        0x1A,
        (
            "#3100F#6P──喂，\x01",
            "玛丽亚贝尔小姐需要一个房间。\x02\x03",

            "好好带路，切记不可失礼。\x02",
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
            "#11P是、是。\x01",
            "那么，就由我来为您带路。\x02",
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

    # Function_17_1A84 end

    def Function_18_2C8D(): pass

    label("Function_18_2C8D")

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

    def lambda_2E29():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2E29)

    def lambda_2E3E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2E3E)
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
            "……哼，真奇怪啊。\x02\x03",

            "本以为他们一定会\x01",
            "有所动作的……\x02",
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
        "#12P不过，到现在还没发生异常情况呢。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x15,
        (
            "#12P就算是『黑月』，\x01",
            "也不会做出有损\x01",
            "哈尔特曼议长脸面的事情吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x1A,
        (
            "#3103F#5P蠢货，不要小看他们。\x02\x03",

            "#3101F『银』就不用说了，传闻那个曹\x01",
            "也是个聪明绝顶之人，连组织的长老\x01",
            "都要敬他三分呢。\x02\x03",

            "松懈大意的话，\x01",
            "当心性命不保。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x15,
        "#12P是、是……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x1A,
        (
            "#3103F#5P话说回来，总觉得这次的\x01",
            "竞拍会有点诡异……\x02\x03",

            "除了『黑月』以外，\x01",
            "好像还有其他什么人\x01",
            "偷偷混了进来似的……\x02\x03",

            "#3101F我总有这种感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x15,
        "#12P哎，那个……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x15,
        (
            "#12P这也是在战场上训练出来的\x01",
            "猎兵的直觉吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x1A,
        (
            "#3104F#5P……算是吧。\x02\x03",

            "#3102F呵呵……\x01",
            "我也上年纪了啊。\x02\x03",

            "如果就这样平安无事地顺利结束，\x01",
            "自然是再好不过了……\x01",
            "但总觉得躁动不安。\x02\x03",

            "久违的『狩猎』欲望好像又涌现出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x15,
        "#12P哈、哈哈……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(12460, 1600, 21220, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(1910, 1600, 19760, 4500)

    def lambda_31F1():
        OP_95(0xFE, 4000, 500, 20600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31F1)
    Sleep(100)

    def lambda_320E():
        OP_95(0xFE, 4000, 500, 19400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_320E)
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
        "#5105F#11P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_32AD")

    #C0139
    ChrTalk(
        0x102,
        "#5301F#11P（黑手党的副头目……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3312")

    label("loc_32AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_32E3")

    #C0140
    ChrTalk(
        0x103,
        "#5401F#11P（黑手党的副头目……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3312")

    label("loc_32E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3312")

    #C0141
    ChrTalk(
        0x104,
        "#5607F#11P（『杀戮之熊』吗……）\x02",
    )

    CloseMessageWindow()

    label("loc_3312")

    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_334F")

    def lambda_3347():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3347)

    label("loc_334F")


    def lambda_3354():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3354)
    Sleep(50)

    def lambda_3364():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3364)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)

    #C0142
    ChrTalk(
        0x1A,
        (
            "#3104F#6P哦，真是失礼了。\x02\x03",

            "#3100F我是负责本会场保安工作的\x01",
            "加尔西亚·罗西。\x02\x03",

            "为了确保场内安全，正在进行巡逻，\x01",
            "如有不敬之处，还请见谅。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#5112F#11P……哪里，\x01",
            "您巡逻辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_345E")

    #C0144
    ChrTalk(
        0x102,
        "#5308F#11P（得想办法蒙混过去……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_34C7")

    label("loc_345E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3498")

    #C0145
    ChrTalk(
        0x103,
        "#5408F#11P（必须得个想办法脱身呢……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_34C7")

    label("loc_3498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_34C7")

    #C0146
    ChrTalk(
        0x104,
        "#5608F#11P（能瞒得过去吗……？）\x02",
    )

    CloseMessageWindow()

    label("loc_34C7")

    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(3300, 1600, 20000, 2500)

    def lambda_34F2():
        OP_95(0xFE, 2500, 500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_34F2)
    Sleep(300)
    Sound(1856, 255, 100, 0)    #voice#Garcia
    WaitChrThread(0x1A, 1)
    OP_6F(0x1)

    #C0147
    ChrTalk(
        0x1A,
        (
            "#3105F#6P客人，我感觉好像\x01",
            "以前在哪里见过您……\x02\x03",

            "#3101F……嗯～……？\x02",
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
            "#5104F#11P……那只是您的心理作用吧？\x02\x03",

            "#5100F像您这样高大魁梧的人，\x01",
            "只要见过一次，我应该就不会忘记的。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x1A,
        (
            "#3109F#6P哈哈，说得也是啊。\x02\x03",

            "#3100F唔……保险起见，\x01",
            "能请教一下尊姓大名吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#5103F#11P……嗯，可以啊。\x02\x03",

            "#5100F──初次见面，幸会。\x01",
            "我是盖伊·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x1A,
        (
            "#3105F#6P盖伊……？\x02\x03",

            "慢着，这名字\x01",
            "我好像曾在哪里听过……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3729")
    TurnDirection(0x1A, 0x104, 500)
    Sleep(300)

    #C0152
    ChrTalk(
        0x1A,
        "#3101F#6P还有，另一位客人……\x02",
    )

    CloseMessageWindow()

    label("loc_3729")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0xEF)

    #C0153
    ChrTalk(
        0x101,
        "#5110F#11P（呜……搞砸了吗……！？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_37B2")

    #C0154
    ChrTalk(
        0x102,
        "#5301F#11P（该、该怎么办……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3813")

    label("loc_37B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_37E2")

    #C0155
    ChrTalk(
        0x103,
        "#5401F#11P（穷途末路了……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3813")

    label("loc_37E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3813")

    #C0156
    ChrTalk(
        0x104,
        "#5610F#11P（嘁，既然这样的话……）\x02",
    )

    CloseMessageWindow()

    label("loc_3813")


    #N0157
    NpcTalk(
        0x1B,
        "女性的声音",
        (
            "#5P──呵呵，\x01",
            "我迟到了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_388E():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_388E)

    def lambda_389B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_389B)
    Sleep(100)

    def lambda_38AB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_38AB)

    def lambda_38B8():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_38B8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)

    def lambda_38D5():

        label("loc_38D5")

        TurnDirection(0x15, 0x1B, 500)
        Yield()
        Jump("loc_38D5")

    QueueWorkItem2(0x15, 1, lambda_38D5)
    OP_68(2700, 1600, 19140, 3000)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_3903():
        OP_95(0xFE, 1820, 500, 17630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3903)
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
        "#5105F#11P哎……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_399C")

    #C0159
    ChrTalk(
        0x102,
        "#5305F#11P贝、贝尔……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A01")

    label("loc_399C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_39D0")

    #C0160
    ChrTalk(
        0x103,
        "#5405F#11P玛丽亚贝尔小姐……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A01")

    label("loc_39D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3A01")

    #C0161
    ChrTalk(
        0x104,
        "#5605F#11P玛丽亚贝尔大小姐……！？\x02",
    )

    CloseMessageWindow()

    label("loc_3A01")

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
            "呵呵……\x01",
            "晚上好，『盖伊』先生。\x02\x03",

            "竟然会在这里碰到你，\x01",
            "真是好巧呢。\x02",
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
        "#5112F#11P嗯、是啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3AFB")

    #C0164
    ChrTalk(
        0x102,
        "#5306F#11P真是……预料之外啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B56")

    label("loc_3AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3B2B")

    #C0165
    ChrTalk(
        0x103,
        "#5406F#11P的确是预料之外……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B56")

    label("loc_3B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3B56")

    #C0166
    ChrTalk(
        0x104,
        "#5606F#11P……的确是好巧呢。\x02",
    )

    CloseMessageWindow()

    label("loc_3B56")


    #C0167
    ChrTalk(
        0x1A,
        (
            "#3105F#5P唔……\x01",
            "这位小姐，请问您是哪位？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x1B,
        (
            "#2904F#12P我的名字是\x01",
            "玛丽亚贝尔·库罗伊斯。\x02\x03",

            "#2902F请多关照。\x02",
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
        "#5PＩＢＣ的……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x1A,
        (
            "#3104F#5P这可真是失敬……\x01",
            "上头交代过您的事。\x02\x03",

            "#3100F您今年总算\x01",
            "接受邀请了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x1B,
        (
            "#2904F#12P呵呵，拒绝了那么多次，\x01",
            "我也觉得太失礼了。\x02\x03",

            "#2900F这两位\x01",
            "是我的朋友……\x02\x03",

            "有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x1A,
        (
            "#3104F#5P不不，当然没有。\x02\x03",

            "#3100F重新打个招呼──\x01",
            "欢迎参加『黑之竞拍会』。\x02\x03",

            "要不要先带您去见\x01",
            "哈尔特曼议长呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x1B,
        (
            "#2904F#12P呵呵，我稍后\x01",
            "再自行去拜会议长阁下吧。\x02\x03",

            "#2902F话说回来，\x01",
            "能不能帮我准备个房间？\x02\x03",

            "之前一直在谈生意，\x01",
            "想稍微休息一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x1A,
        "#3104F#5P遵命。\x02",
    )

    CloseMessageWindow()
    OP_68(3030, 1600, 20130, 1200)
    OP_93(0x1A, 0x0, 0x190)
    OP_6F(0x1)

    #C0175
    ChrTalk(
        0x1A,
        (
            "#3100F#12P──喂，\x01",
            "玛丽亚贝尔小姐需要一个房间。\x02\x03",

            "好好带路，切记不可失礼。\x02",
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
            "#5P是、是。\x01",
            "那么，就由我来为您带路。\x02",
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

    # Function_18_2C8D end

    def Function_19_3EA7(): pass

    label("Function_19_3EA7")

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

    def lambda_3F49():
        OP_95(0xFE, 0, 500, 19000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3F49)
    Sleep(100)

    def lambda_3F66():
        OP_95(0xFE, -600, 500, 20200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F66)
    Sleep(50)

    def lambda_3F83():
        OP_95(0xFE, 600, 500, 20200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3F83)

    def lambda_3F9D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F9D)

    def lambda_3FAE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_3FAE)

    def lambda_3FBF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_3FBF)
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
            "#5703F#12P（安排在后院里的看门狗\x01",
            "  有好几条都睡着了……）\x02\x03",

            "#5702F（呵呵，这意味着什么呢？）\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#5103F#5P（嗯，能想到的就是──）\x02",
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
            "#1K这意味着什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【出现了入侵者】\x01",            # 0
            "【是黑手党设下的圈套】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_40F4"),
        (1, "loc_422F"),
        (SWITCH_DEFAULT, "loc_42ED"),
    )


    label("loc_40F4")

    OP_2C(0x47, 0x1)

    #C0180
    ChrTalk(
        0x101,
        (
            "#5113F#5P（出现了入侵者……\x01",
            "  这种可能性或许很高。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xEF, 0xE1, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4170")

    #C0181
    ChrTalk(
        0x102,
        "#5301F#5P（原来如此……确实。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_41C7")

    label("loc_4170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_419F")

    #C0182
    ChrTalk(
        0x103,
        "#5401F#5P（……原来如此。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_41C7")

    label("loc_419F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_41C7")

    #C0183
    ChrTalk(
        0x104,
        "#5601F#5P（嗯，有同感。）\x02",
    )

    CloseMessageWindow()

    label("loc_41C7")


    #C0184
    ChrTalk(
        0x151,
        (
            "#5704F#12P（不管怎么说，\x01",
            "  恐怕是有什么事情要发生了……）\x02\x03",

            "#5702F（只有这点是可以肯定的呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42ED")

    label("loc_422F")


    #C0185
    ChrTalk(
        0x101,
        (
            "#5108F#5P（黑手党设下的圈套……\x01",
            "  这似乎也有可能。）\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x151,
        (
            "#5706F#12P（我倒觉得\x01",
            "  你实在是想多了。）\x02\x03",

            "#5702F（不管怎么说，\x01",
            "  恐怕是有什么事情要发生了。\x01",
            "  只有这点是可以肯定的呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42ED")

    label("loc_42ED")


    #C0187
    ChrTalk(
        0x101,
        (
            "#5101F#5P（嗯，保险起见，\x01",
            "  先在宅邸里转一圈看看吧。）\x02\x03",

            "（可能会发现什么异常情况呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xEF, 0xE1, 0x1F4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4379")

    #C0188
    ChrTalk(
        0x102,
        "#5301F#5P（嗯……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_43CA")

    label("loc_4379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_43A6")

    #C0189
    ChrTalk(
        0x103,
        "#5401F#5P（……明白了。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_43CA")

    label("loc_43A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_43CA")

    #C0190
    ChrTalk(
        0x104,
        "#5601F#5P（明白啦。）\x02",
    )

    CloseMessageWindow()

    label("loc_43CA")


    #C0191
    ChrTalk(
        0x151,
        (
            "#5709F#12P（呵呵……\x01",
            "  我也陪你们去吧。）\x02",
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

    # Function_19_3EA7 end

    def Function_20_4419(): pass

    label("Function_20_4419")

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
            "#3104F#11P哼哼……\x01",
            "果然有小老鼠出现了吗？\x02\x03",

            "#3107F──你们几个，要开始狩猎了！\x02\x03",

            "把客人隔离在竞拍会场，\x01",
            "完全封锁宅邸出口！\x02\x03",

            "连一只老鼠都不能放跑！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(80, 140, -1, -1)
    SetChrName("黑手党们")
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)

    #A0193
    AnonymousTalk(
        0xFF,
        "#4S遵命！\x02",
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

    # Function_20_4419 end

    def Function_21_468D(): pass

    label("Function_21_468D")

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
            "#3007F#11P──可恶！\x01",
            "还没找到入侵者吗！\x02\x03",

            "宾客们快要\x01",
            "开始骚乱了！\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x1A,
        (
            "#3103F#6P……请您稍等。\x02\x03",

            "#3100F宅邸已经完全封锁了，\x01",
            "现在正所谓是瓮中捉鳖。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x1C,
        (
            "#3003F#11P呜……\x01",
            "这样下去的话，议长一定会很恼火……\x02\x03",

            "#3007F别管那么多了，快点抓住他们啊！\x02\x03",

            "形势需要的话，杀掉也无所谓！\x02",
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

    # Function_21_468D end

    def Function_22_4900(): pass

    label("Function_22_4900")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4972")
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_4999")

    label("loc_4972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4988")
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_4999")

    label("loc_4988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4999")
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    label("loc_4999")

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
        "#0000F#2P（好，这点人数的话……！）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4B06")

    #C0198
    ChrTalk(
        0x102,
        "#0100F#2P（强行突破吧……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B65")

    label("loc_4B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4B3B")

    #C0199
    ChrTalk(
        0x103,
        "#0202F#2P（要强行突破了吧……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B65")

    label("loc_4B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4B65")

    #C0200
    ChrTalk(
        0x104,
        "#0300F#2P（强行突破……！）\x02",
    )

    CloseMessageWindow()

    label("loc_4B65")


    #C0201
    ChrTalk(
        0x105,
        "#0400F#2P（上吧……！）\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4BAE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4BAE)
    Sleep(50)

    def lambda_4BBE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4BBE)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x18, 1)

    #C0202
    ChrTalk(
        0x17,
        "#11P嗯……？\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x18,
        "#11P哎……\x02",
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

    def lambda_4CA1():
        OP_95(0xFE, -4740, 500, 18820, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CA1)
    Sleep(50)

    def lambda_4CBE():
        OP_95(0xFE, -6480, 500, 18040, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4CBE)
    Sleep(50)

    def lambda_4CDB():
        OP_95(0xFE, -6140, 500, 19670, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4CDB)
    Sleep(100)

    def lambda_4CF8():
        OP_95(0xFE, -7980, 500, 18940, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_4CF8)
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
        "#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x18,
        "#11P不是出去了吗！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4DAF")

    #C0206
    ChrTalk(
        0x102,
        "#0107F#6P太慢了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DFC")

    label("loc_4DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4DD8")

    #C0207
    ChrTalk(
        0x103,
        "#0207F#6P太慢了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DFC")

    label("loc_4DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4DFC")

    #C0208
    ChrTalk(
        0x104,
        "#0307F#3P太慢啦……！\x02",
    )

    CloseMessageWindow()

    label("loc_4DFC")

    SetCameraDistance(15800, 300)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_4E1C():
        OP_95(0xFE, -740, 500, 18820, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E1C)

    def lambda_4E36():
        OP_95(0xFE, -2480, 500, 18040, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4E36)

    def lambda_4E50():
        OP_95(0xFE, -2980, 500, 19260, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4E50)
    Sleep(300)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x105, 0x1)
    Battle("BattleInfo_464", 0x0, 0x0, 0x0, 0x11, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 23)
    Return()

    # Function_22_4900 end

    def Function_23_4E92(): pass

    label("Function_23_4E92")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4FEF")
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_5016")

    label("loc_4FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5005")
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_5016")

    label("loc_5005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5016")
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    label("loc_5016")

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

    def lambda_50DB():
        TurnDirection(0xFE, 0x133, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50DB)

    def lambda_50E8():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_50E8)
    Sleep(100)

    def lambda_50F8():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_50F8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    Sleep(100)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)

    #N0209
    NpcTalk(
        0x1C,
        "男人的声音",
        (
            "#4P可恶，吵死了！\x01",
            "还没找到吗──\x02",
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

    def lambda_51B2():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51B2)

    def lambda_51BF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_51BF)
    Sleep(100)

    def lambda_51CF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_51CF)

    def lambda_51DC():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_51DC)
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

    def lambda_5255():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5255)
    WaitChrThread(0x1C, 1)
    OP_0D()
    OP_63(0x1C, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0210
    ChrTalk(
        0x1C,
        (
            "#3005F#5P什么……\x01",
            "你、你们是！？\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x133,
        "#5805F#12P#N啊，圆滚滚的人！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_52FE")

    #C0212
    ChrTalk(
        0x102,
        "#0101F#12P马尔克尼会长……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_535B")

    label("loc_52FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_532E")

    #C0213
    ChrTalk(
        0x103,
        "#0201F#12P黑手党的会长……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_535B")

    label("loc_532E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_535B")

    #C0214
    ChrTalk(
        0x104,
        "#0307F#12P黑手党的老大吗……！\x02",
    )

    CloseMessageWindow()

    label("loc_535B")

    OP_93(0x101, 0x10E, 0x1F4)

    #C0215
    ChrTalk(
        0x101,
        (
            "#0007F#11P没有问题！\x01",
            "直接冲出去！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_538E():
        OP_95(0xFE, -800, 500, 18640, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_538E)
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
        "#0402F#12PArrivederci（再见啦）！\x02",
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
        "#3001F#5P你、你、你……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0218
    ChrTalk(
        0x1C,
        "#3007F#5P#4S你们在干什么啊！\x02",
    )

    CloseMessageWindow()
    OP_68(1030, 1600, 20870, 1500)
    SetCameraDistance(16780, 1500)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_5504():
        OP_95(0xFE, 690, 500, 21650, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5504)
    WaitChrThread(0x1C, 1)
    OP_93(0x1C, 0x87, 0x1F4)
    OP_6F(0x1)

    #C0219
    ChrTalk(
        0x1C,
        (
            "#3007F#5P快起来，还不起来！\x02\x03",

            "#3001F可恶……\x01",
            "加尔西亚到底在干什么！？\x02",
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
            "#2902F#5P（呵呵……\x01",
            "  情况变得有趣起来了呢。）\x02\x03",

            "#2905F（不过，罗伊德\x01",
            "  抱着的那个孩子是……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_565D")
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_5684")

    label("loc_565D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5673")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_5684")

    label("loc_5673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5684")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_5684")

    SetScenarioFlags(0x5C, 0)
    NewScene("t110B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_4E92 end

    def Function_24_5691(): pass

    label("Function_24_5691")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_569D():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_569D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_5691 end

    def Function_25_56B2(): pass

    label("Function_25_56B2")


    def lambda_56B7():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56B7)

    def lambda_56CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_56CC)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_25_56B2 end

    def Function_26_56E1(): pass

    label("Function_26_56E1")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5741")

    #C0221
    ChrTalk(
        0x101,
        (
            "#5101F（难得潜入进来了……\x01",
            "  在竞拍会开始之前，\x01",
            "  先在宅邸里四处转转吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5822")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57DC")

    #C0222
    ChrTalk(
        0x138,
        (
            "#2905F哎呀，不去会场吗？\x01",
            "竞拍会场\x01",
            "是那边的大堂哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#5105F啊，说得也是。\x02\x03",

            "#5100F机会难得，\x01",
            "就让我们跟您一起去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5822")

    label("loc_57DC")


    #C0224
    ChrTalk(
        0x101,
        (
            "#5101F会场是正面的大堂。\x01",
            "……行动时要注意一点，\x01",
            "不要引人生疑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_5864")

    #C0225
    ChrTalk(
        0x101,
        (
            "#5101F情况很令人在意呢……\x01",
            "在宅邸里面再四处转转吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5864")

    Sleep(50)
    SetChrPos(0x0, 0, 0, -1030, 360)
    EventEnd(0x4)
    Return()

    # Function_26_56E1 end

    SaveToFile()

Try(main)
