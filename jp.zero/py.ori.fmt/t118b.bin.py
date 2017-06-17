from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "招待客",                 # 1
        "招待客",                 # 2
        "招待客",                 # 3
        "招待客",                 # 4
        "招待客",                 # 5
        "ドーベンカイザーその１", # 6
        "ドーベンカイザーその２", # 7
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
        "Function_7_722",          # 07, 7
        "Function_8_88C",          # 08, 8
        "Function_9_A01",          # 09, 9
        "Function_10_BA3",         # 0A, 10
        "Function_11_C31",         # 0B, 11
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694")

    #C0001
    ChrTalk(
        0xFE,
        (
            "本日出品されるらしい目玉商品は\x01",
            "とても精巧な人形だという噂なのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "精巧な人形というので思いつくのは\x01",
            "やはりローゼンベルク工房製だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "いやぁ、オークションの開場が楽しみだ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_71A")

    label("loc_694")


    #C0004
    ChrTalk(
        0xFE,
        (
            "ローゼンベルク工房製の人形は\x01",
            "まさに生きているかのような\x01",
            "とてつもない魅力を放つのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "いやぁ、オークションの開場が楽しみだ。\x02",
    )

    CloseMessageWindow()

    label("loc_71A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_4C5 end

    def Function_7_722(): pass

    label("Function_7_722")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E4")

    #C0006
    ChrTalk(
        0xFE,
        (
            "主人はこと人形に関しては\x01",
            "本当に目がないんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "人形など、と初めは\x01",
            "思っていたものでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "あの魅力を知ってからは\x01",
            "私にとっても素敵な趣味になりましたわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_888")

    label("loc_7E4")


    #C0009
    ChrTalk(
        0xFE,
        (
            "人形の魅力を知ってからは、\x01",
            "夫婦２人で収集に\x01",
            "精を出すようになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "どれだけのミラを使っても\x01",
            "手元に置いておきたい……\x01",
            "そんな魅力が人形にはあるのです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_888")

    TalkEnd(0xFE)
    Return()

    # Function_7_722 end

    def Function_8_88C(): pass

    label("Function_8_88C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_920")
    Jump("loc_96A")

    label("loc_920")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_940")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96A")

    label("loc_940")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_960")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96A")

    label("loc_960")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0011
    ChrTalk(
        0xFE,
        (
            "立食会などにはどうも、\x01",
            "参加する気が起きなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "やはり食事はメイドに\x01",
            "運びに来させるにかぎる。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_88C end

    def Function_9_A01(): pass

    label("Function_9_A01")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A95")
    Jump("loc_ADF")

    label("loc_A95")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AB5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADF")

    label("loc_AB5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADF")

    label("loc_AD5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ADF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0013
    ChrTalk(
        0xFE,
        (
            "知り合いのツテで\x01",
            "偶然招待状をいただいたけど……\x01",
            "なんだか雰囲気に合ってないみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "オークションが始まるまでは\x01",
            "ここで待っているとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_A01 end

    def Function_10_BA3(): pass

    label("Function_10_BA3")

    TalkBegin(0xFE)

    #C0015
    ChrTalk(
        0xFE,
        (
            "……うむ……\x01",
            "屋敷を見物していたのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "どうやら迷ってしまったらしい。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "困ったな……\x01",
            "オークションが\x01",
            "始まってしまうぞ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_BA3 end

    def Function_11_C31(): pass

    label("Function_11_C31")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C6E")
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    Jump("loc_C8F")

    label("loc_C6E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C89")
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    Jump("loc_C8F")

    label("loc_C89")

    LoadChrToIndex("chr/ch00350.itc", 0x1F)

    label("loc_C8F")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB8")
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
    Jump("loc_E4C")

    label("loc_DB8")

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

    label("loc_E4C")


    def lambda_E51():
        OP_98(0xD, 0x0, 0x0, 0xFFFFEE6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_E51)
    Sleep(50)

    def lambda_E6E():
        OP_98(0xE, 0x0, 0x0, 0xFFFFEE6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_E6E)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F68")
    OP_68(0, 1200, -6000, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -6000, 0)
    SetChrPos(0xEF, 0, 0, -6000, 0)
    SetChrPos(0x105, 0, 0, -6000, 0)
    Jump("loc_FC9")

    label("loc_F68")

    OP_68(0, 1200, -16000, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -16000, 0)
    SetChrPos(0xEF, 0, 0, -16000, 0)
    SetChrPos(0x105, 0, 0, -16000, 0)

    label("loc_FC9")

    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_11_C31 end

    SaveToFile()

Try(main)
