from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t118b.bin",                # FileName
        "t118b",                    # MapName
        "t118b",                    # Location
        0x004A,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 74, 0, 4, 0, 5],
    )

    BuildStringList((
        "t118b",                  # 0
        "客人",                   # 1
        "客人",                   # 2
        "客人",                   # 3
        "客人",                   # 4
        "客人",                   # 5
        "猎犬帝王之１",           # 6
        "猎犬帝王之２",           # 7
        "bt113b",                 # 8
    ))

    ATBonus("ATBonus_180", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_260", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_268", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_26C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_270", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_274", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_240", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_244", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_248", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_24C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_250", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_254", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_258", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_25C", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_280", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt113b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67100.dat", "ms67100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_260", "MonsterBattlePostion_240", "ed7509", "ed7000", "ATBonus_180"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch21802.itc",                   # 00
        "chr/ch21900.itc",                   # 01
        "chr/ch33002.itc",                   # 02
        "chr/ch21702.itc",                   # 03
        "chr/ch33100.itc",                   # 04
        "monster/ch67151.itc",               # 05
    ))

    DeclNpc(3829,    150,     -64919,  180,  469,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(70,      0,       -69059,  180,  385,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-46529,  150,     32020,   180,  469,  0x0, 0,   2,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-46529,  150,     27889,   0,    469,  0x0, 0,   3,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-19,     0,       -11449,  180,  385,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_2F4",          # 00, 0
        "Function_1_3AC",          # 01, 1
        "Function_2_3D7",          # 02, 2
        "Function_3_402",          # 03, 3
        "Function_4_41E",          # 04, 4
        "Function_5_477",          # 05, 5
        "Function_6_4C5",          # 06, 6
        "Function_7_6DC",          # 07, 7
        "Function_8_81E",          # 08, 8
        "Function_9_993",          # 09, 9
        "Function_10_B0B",         # 0A, 10
        "Function_11_B83",         # 0B, 11
    ))


    def Function_0_2F4(): pass

    label("Function_0_2F4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_334"),
        (1, "loc_340"),
        (2, "loc_34C"),
        (3, "loc_358"),
        (4, "loc_364"),
        (5, "loc_370"),
        (6, "loc_37C"),
        (SWITCH_DEFAULT, "loc_388"),
    )


    label("loc_334")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_394")

    label("loc_340")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_394")

    label("loc_34C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_394")

    label("loc_358")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_394")

    label("loc_364")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_394")

    label("loc_370")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_394")

    label("loc_37C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_394")

    label("loc_388")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_394")

    label("loc_394")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_394")

    label("loc_3AB")

    Return()

    # Function_0_2F4 end

    def Function_1_3AC(): pass

    label("Function_1_3AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D6")
    OP_94(0xFE, 0xFFFFF9CA, 0xFFFEEAE4, 0x456, 0xFFFEFC6E, 0x3E8)
    Sleep(300)
    Jump("Function_1_3AC")

    label("loc_3D6")

    Return()

    # Function_1_3AC end

    def Function_2_3D7(): pass

    label("Function_2_3D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_401")
    OP_94(0xFE, 0xFFFFFB82, 0xFFFFBE42, 0x3DE, 0xFFFFF16E, 0x3E8)
    Sleep(300)
    Jump("Function_2_3D7")

    label("loc_401")

    Return()

    # Function_2_3D7 end

    def Function_3_402(): pass

    label("Function_3_402")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41D")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_3_402")

    label("loc_41D")

    Return()

    # Function_3_402 end

    def Function_4_41E(): pass

    label("Function_4_41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_42C")
    Jump("loc_476")

    label("loc_42C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_445")
    ClearChrFlags(0xC, 0x80)
    BeginChrThread(0xC, 0, 0, 2)
    Jump("loc_476")

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_453")
    Jump("loc_476")

    label("loc_453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_476")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_476")

    Return()

    # Function_4_41E end

    def Function_5_477(): pass

    label("Function_5_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_480")

    label("loc_480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_48E")
    Jump("loc_4C4")

    label("loc_48E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_END)), "loc_4C4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C4")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C4")
    Event(0, 11)

    label("loc_4C4")

    Return()

    # Function_5_477 end

    def Function_6_4C5(): pass

    label("Function_6_4C5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_559")
    Jump("loc_5A3")

    label("loc_559")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_579")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A3")

    label("loc_579")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_599")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A3")

    label("loc_599")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66C")

    #C0001
    ChrTalk(
        0xFE,
        (
            "据说，今天展出的重头商品\x01",
            "是一个做工非常精巧的人偶。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "说到做工精巧，\x01",
            "当然首推罗赞贝尔克工房制造的人偶啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "哎呀，好期待拍卖会开场啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6D4")

    label("loc_66C")


    #C0004
    ChrTalk(
        0xFE,
        (
            "罗赞贝尔克工房制造的人偶\x01",
            "仿佛拥有生命一样，\x01",
            "散发着难以言喻的魅力。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "哎呀，好期待拍卖会开场啊。\x02",
    )

    CloseMessageWindow()

    label("loc_6D4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_4C5 end

    def Function_7_6DC(): pass

    label("Function_7_6DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_788")

    #C0006
    ChrTalk(
        0xFE,
        (
            "我老公一提到关于人偶的事情，\x01",
            "就会变得非常激动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "一开始，我还觉得人偶\x01",
            "这种东西很平常……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "不过，一旦感受到了它的魅力，\x01",
            "我也产生兴趣了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_81A")

    label("loc_788")


    #C0009
    ChrTalk(
        0xFE,
        (
            "感受到人偶的魅力之后，\x01",
            "我们夫妇二人便开始\x01",
            "齐心协力地收集了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "花费多少米拉都无所谓，\x01",
            "就想让它们陪在自己的身边……\x01",
            "人偶就是有这样的魅力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81A")

    TalkEnd(0xFE)
    Return()

    # Function_7_6DC end

    def Function_8_81E(): pass

    label("Function_8_81E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B2")
    Jump("loc_8FC")

    label("loc_8B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8FC")

    label("loc_8D2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8FC")

    label("loc_8F2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8FC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0011
    ChrTalk(
        0xFE,
        (
            "连座位都没有的餐会吗，\x01",
            "那种活动实在是没兴趣参加。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "用餐的时候，一定要有女仆\x01",
            "把料理送到面前才行。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_81E end

    def Function_9_993(): pass

    label("Function_9_993")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A27")
    Jump("loc_A71")

    label("loc_A27")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A47")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A71")

    label("loc_A47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A67")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A71")

    label("loc_A67")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A71")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0013
    ChrTalk(
        0xFE,
        (
            "偶然从朋友那里\x01",
            "得到了邀请函……\x01",
            "但我好像不太适合这种环境啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "在拍卖会开始之前，\x01",
            "还是在这里等着吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_993 end

    def Function_10_B0B(): pass

    label("Function_10_B0B")

    TalkBegin(0xFE)

    #C0015
    ChrTalk(
        0xFE,
        (
            "……嗯……\x01",
            "本来想参观一下宅邸的……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "看样子，好像是迷路了呢。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "真头疼啊……\x01",
            "拍卖会\x01",
            "马上就要开始了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_B0B end

    def Function_11_B83(): pass

    label("Function_11_B83")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC0")
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    Jump("loc_BE1")

    label("loc_BC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BDB")
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    Jump("loc_BE1")

    label("loc_BDB")

    LoadChrToIndex("chr/ch00350.itc", 0x1F)

    label("loc_BE1")

    LoadChrToIndex("chr/ch00450.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0xEF, 0x1F)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0xEF, 0x0)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 1, 0, 3)
    Sleep(50)
    BeginChrThread(0xE, 1, 0, 3)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0A")
    OP_68(0, 1200, -6000, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -6000, 0)
    SetChrPos(0xEF, -750, 0, -7000, 0)
    SetChrPos(0x105, 750, 0, -7750, 0)
    SetChrPos(0x133, 0, 0, -9000, 0)
    SetChrPos(0xD, 0, 0, 0, 180)
    SetChrPos(0xE, 1250, 0, 1000, 180)
    Jump("loc_D9E")

    label("loc_D0A")

    OP_68(0, 1200, -16000, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -16000, 0)
    SetChrPos(0xEF, -750, 0, -17000, 0)
    SetChrPos(0x105, 750, 0, -17750, 0)
    SetChrPos(0x133, 0, 0, -19000, 0)
    SetChrPos(0xD, 0, 0, -10000, 180)
    SetChrPos(0xE, 1250, 0, -9000, 180)

    label("loc_D9E")


    def lambda_DA3():
        OP_98(0xD, 0x0, 0x0, 0xFFFFEE6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_DA3)
    Sleep(50)

    def lambda_DC0():
        OP_98(0xE, 0x0, 0x0, 0xFFFFEE6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_DC0)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0xD, 2)
    Battle("BattleInfo_280", 0x0, 0x0, 0x0, 0x10, 0xFF)
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
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xE, 0x2)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBA")
    OP_68(0, 1200, -6000, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -6000, 0)
    SetChrPos(0xEF, 0, 0, -6000, 0)
    SetChrPos(0x105, 0, 0, -6000, 0)
    Jump("loc_F1B")

    label("loc_EBA")

    OP_68(0, 1200, -16000, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -16000, 0)
    SetChrPos(0xEF, 0, 0, -16000, 0)
    SetChrPos(0x105, 0, 0, -16000, 0)

    label("loc_F1B")

    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_11_B83 end

    SaveToFile()

Try(main)
