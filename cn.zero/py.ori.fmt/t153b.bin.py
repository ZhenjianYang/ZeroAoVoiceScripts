from ZeroScenarioHelper import *

def main():
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
        "黑手党",                 # 1
        "黑手党",                 # 2
        "接待小姐塞拉",           # 3
        "克拉克事务长",           # 4
        "诊断医生达斯塔（未使用）",# 5
        "实习医生利泽尔（未使用）",# 6
        "实习医生夏鲁鲁",         # 7
        "实习医生芙萝拉",         # 8
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
        "Function_4_4F1",          # 04, 4
        "Function_5_647",          # 05, 5
        "Function_6_783",          # 06, 6
        "Function_7_9B4",          # 07, 7
        "Function_8_AE2",          # 08, 8
        "Function_9_C23",          # 09, 9
        "Function_10_DF2",         # 0A, 10
        "Function_11_11A7",        # 0B, 11
        "Function_12_14AF",        # 0C, 12
        "Function_13_152A",        # 0D, 13
        "Function_14_1A90",        # 0E, 14
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
            "黑手党成员失去了意识。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_3_4C5 end

    def Function_4_4F1(): pass

    label("Function_4_4F1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_585")
    Jump("loc_5CF")

    label("loc_585")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CF")

    label("loc_5A5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CF")

    label("loc_5C5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0002
    ChrTalk(
        0xFE,
        (
            "楼上还有不少\x01",
            "医院的工作人员\x01",
            "以及患者。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "那些人就\x01",
            "拜托你们了……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_4F1 end

    def Function_5_647(): pass

    label("Function_5_647")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_713")

    #C0004
    ChrTalk(
        0xFE,
        (
            "以前魔兽作乱时建造的防护栏还在，\x01",
            "所以我一直都很放心。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "但、但没想到黑手党\x01",
            "竟然会入侵到医院里……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "这里的医生和学员来自大陆各国，\x01",
            "如果不妥善处理，会演变成国际问题的……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_77F")

    label("loc_713")


    #C0007
    ChrTalk(
        0xFE,
        (
            "本以为黑手党应该稍微\x01",
            "有些组织性的……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "在这种情况下……\x01",
            "不妥善处理的话，就会演变成国际问题的……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77F")

    TalkEnd(0xFE)
    Return()

    # Function_5_647 end

    def Function_6_783(): pass

    label("Function_6_783")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_817")
    Jump("loc_861")

    label("loc_817")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_837")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_861")

    label("loc_837")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_857")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_861")

    label("loc_857")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_861")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_941")

    #C0009
    ChrTalk(
        0xFE,
        (
            "对、对了。\x01",
            "从今天傍晚开始，\x01",
            "就要给病人看病……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "在这样的骚乱中，就算有人\x01",
            "突然发病也不足为奇……\x01",
            "该怎么办呢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "总、总之，我们作为医生，\x01",
            "要先冷静下来……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_9AC")

    label("loc_941")


    #C0012
    ChrTalk(
        0xFE,
        (
            "说起来，今天的安排是傍晚\x01",
            "给轻微发病的患者\x01",
            "诊断病情。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "唔……希望病人的发病\x01",
            "不要变得更加严重啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AC")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_783 end

    def Function_7_9B4(): pass

    label("Function_7_9B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A59")

    #C0014
    ChrTalk(
        0xFE,
        (
            "面对这种异常事态，\x01",
            "我的心情却意外地平静。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "这或许要归功于一直在冷静沉着的\x01",
            "贝尔达因医生手下学习吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "……希望医生也能平安无事啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_ADE")

    label("loc_A59")


    #C0017
    ChrTalk(
        0xFE,
        (
            "……要是拖到天亮的话，\x01",
            "那些前来医院就诊的患者们\x01",
            "很可能也会被卷进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "……连枪声都能听得到，\x01",
            "住宿设施那边也很让人担心啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADE")

    TalkEnd(0xFE)
    Return()

    # Function_7_9B4 end

    def Function_8_AE2(): pass

    label("Function_8_AE2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAC")

    #C0019
    ChrTalk(
        0xFE,
        (
            "竟然袭击拥有最新医疗技术的\x01",
            "乌尔斯拉医院，\x01",
            "真是群愚蠢的家伙们！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "而且他们……\x01",
            "竟然携带着武器\x01",
            "闯入医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "如果把正在进行试验的机器弄坏，\x01",
            "会给医疗事业的未来造成巨大损失！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_C1F")

    label("loc_BAC")


    #C0022
    ChrTalk(
        0xFE,
        (
            "真是完全搞不懂他们的目的，\x01",
            "为什么要袭击这里呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "总而言之，\x01",
            "只能希望女神保佑\x01",
            "院内的机器不要被破坏了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1F")

    TalkEnd(0xFE)
    Return()

    # Function_8_AE2 end

    def Function_9_C23(): pass

    label("Function_9_C23")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CB7")
    Jump("loc_D01")

    label("loc_CB7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CD7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D01")

    label("loc_CD7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D01")

    label("loc_CF7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D01")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA5")
    SetChrSubChip(0xFE, 0x0)

    #C0024
    ChrTalk(
        0xFE,
        "……别慌，要冷静下来，芙萝拉。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "因、因为这点小事就方寸大乱的话，\x01",
            "是没法成为一名合格的医生的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_DEA")

    label("loc_DA5")


    #C0026
    ChrTalk(
        0xFE,
        "……我想冷静下来。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "抱歉，不好意思……\x01",
            "能让我一个人待会吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_C23 end

    def Function_10_DF2(): pass

    label("Function_10_DF2")

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

    def lambda_F2B():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F2B)
    Sleep(50)

    def lambda_F43():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F43)
    Sleep(50)

    def lambda_F5B():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F5B)
    Sleep(50)

    def lambda_F73():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F73)
    Sleep(50)

    def lambda_F8B():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_F8B)
    Sleep(200)

    def lambda_FA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FA3)
    Sleep(50)

    def lambda_FB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FB7)
    Sleep(500)

    def lambda_FCB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FCB)
    Sleep(50)

    def lambda_FDF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FDF)
    Sleep(500)

    def lambda_FF3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_FF3)
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
        "#0001F#5P没有人的气息吗……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#0108F#6P……也没有黑手党的踪影。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P不，建筑物内的多个地方\x01",
            "都有流动的气息传来……\x02\x03",

            "想必是医院里的人\x01",
            "躲在各个房间避难吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        (
            "#0203F#6P嗯，能感觉得到，\x01",
            "好像还有不少人呢。\x02\x03",

            "#0201F其中也包括黑手党的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#0301F#5P原来如此……\x01",
            "也就是说，好戏才刚刚开始啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#0013F#5P好……\x01",
            "谨慎前进吧！\x02",
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

    # Function_10_DF2 end

    def Function_11_11A7(): pass

    label("Function_11_11A7")

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
        "#0105F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#0013F#6P埋伏吗……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(48500, 1000, 0, 1000)
    SetCameraDistance(17500, 1000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)

    def lambda_13C8():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13C8)

    def lambda_13DD():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13DD)
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

    # Function_11_11A7 end

    def Function_12_14AF(): pass

    label("Function_12_14AF")

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

    # Function_12_14AF end

    def Function_13_152A(): pass

    label("Function_13_152A")

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

    def lambda_1686():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1686)
    Sleep(50)

    def lambda_169E():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_169E)
    Sleep(50)

    def lambda_16B6():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16B6)
    Sleep(50)

    def lambda_16CE():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16CE)
    Sleep(50)

    def lambda_16E6():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_16E6)
    Sleep(200)

    def lambda_16FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16FE)
    Sleep(50)

    def lambda_1712():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1712)
    Sleep(500)

    def lambda_1726():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1726)
    Sleep(50)

    def lambda_173A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_173A)
    Sleep(500)

    def lambda_174E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_174E)
    WaitChrThread(0x101, 1)

    def lambda_1763():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1763)
    WaitChrThread(0x102, 1)

    def lambda_1774():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1774)
    WaitChrThread(0x103, 1)

    def lambda_1785():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1785)
    WaitChrThread(0x104, 1)

    def lambda_1796():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1796)
    WaitChrThread(0x106, 1)

    def lambda_17A7():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_17A7)
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

    def lambda_1838():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1838)
    Sleep(50)

    def lambda_1848():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1848)
    Sleep(50)

    def lambda_1858():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1858)
    Sleep(50)

    def lambda_1868():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1868)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)

    #C0036
    ChrTalk(
        0xA,
        "#5P罗伊德警官……！？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#0002F#6P塞拉小姐……\x01",
            "太好了，你没事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        "#11P各、各位是警察局的……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xE,
        (
            "#5P难、难道\x01",
            "是来救我们的吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#0300F#6P嗯，我们会在制服入侵者的同时，\x01",
            "确保大家的安全。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#0201F#6P#N目前的情况还很危险，\x01",
            "请暂时留在这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0042
    ChrTalk(
        0xA,
        "#5P我、我知道了。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xA,
        (
            "#5P楼上应该还有\x01",
            "其他工作人员与患者。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xE,
        "#5P他、他们的安全也拜托各位了！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        "#6P#0001F明白！\x02",
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

    # Function_13_152A end

    def Function_14_1A90(): pass

    label("Function_14_1A90")

    TalkBegin(0xFF)
    SetChrName("")

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力似乎完全停止了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_1A90 end

    SaveToFile()

Try(main)
