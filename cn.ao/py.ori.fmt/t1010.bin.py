from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1010.bin",                # FileName
        "t1010",                    # MapName
        "t1010",                    # Location
        0x0045,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 69, 0, 3, 0, 4],
    )

    BuildStringList((
        "t1010",                  # 0
        "艾米",                   # 1
        "泽鲁",                   # 2
        "卡比兰",                 # 3
        "卢古曼",                 # 4
        "玛格丽特夫人",           # 5
        "剧情用魔兽",             # 6
        "剧情用魔兽",             # 7
        "剧情用魔兽",             # 8
        "剧情用魔兽",             # 9
        "剧情用魔兽",             # 10
        "剧情用魔兽",             # 11
        "剧情用魔兽",             # 12
        "剧情用魔兽",             # 13
        "bt1010",                 # 14
        "迎宾馆方向",             # 15
        "翠雀酒店方向",           # 16
    ))

    ATBonus("ATBonus_2CC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_38C", 8, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_370", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_374", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_378", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_37C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_380", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_384", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_3AC", 0x004A, 255, 6, 45, 3, 3, 30, 0, "bt1010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms86100.dat", "ms82002.dat", "ms82002.dat", "ms82002.dat", 0, 0, 0, 0, "MonsterBattlePostion_38C", "MonsterBattlePostion_36C", "ed7540", "ed7453", "ATBonus_2CC"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch22302.itc",                   # 00
        "chr/ch22202.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch33000.itc",                   # 03
        "chr/ch44000.itc",                   # 04
    ))

    DeclNpc(2279,    -3700,   -12430,  180,  325,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(3660,    -3700,   -12430,  180,  325,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(26860,   -2000,   2200,    270,  257,  0x0, 0,   2,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(-1970,   -2000,   34720,   180,  257,  0x0, 0,   3,   0,   0,   2,   0,   9,   255,  0)
    DeclNpc(-6230,   -1799,   0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  5.5,                   0.0,                   -3.0,                  400.0,                 [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.09999999403953552,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -1.375,                -0.0,                  0.5999999642372131,    1.0])

    PlaceName(-5.0, 0.0, 81.0, 0x0000, 0x0000, "迎宾馆方向")
    PlaceName(65.0, 0.0, 0.0, 0x0000, 0x0000, "翠雀酒店方向")

    ChipFrameInfo(1072, 0)                                       # 0

    ScpFunction((
        "Function_0_430",          # 00, 0
        "Function_1_4E8",          # 01, 1
        "Function_2_549",          # 02, 2
        "Function_3_5AA",          # 03, 3
        "Function_4_614",          # 04, 4
        "Function_5_6B2",          # 05, 5
        "Function_6_7B6",          # 06, 6
        "Function_7_9CE",          # 07, 7
        "Function_8_ACA",          # 08, 8
        "Function_9_DBA",          # 09, 9
        "Function_10_FFE",         # 0A, 10
        "Function_11_10DA",        # 0B, 11
        "Function_12_17B1",        # 0C, 12
        "Function_13_17D0",        # 0D, 13
        "Function_14_17EF",        # 0E, 14
        "Function_15_180C",        # 0F, 15
    ))


    def Function_0_430(): pass

    label("Function_0_430")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_470"),
        (1, "loc_47C"),
        (2, "loc_488"),
        (3, "loc_494"),
        (4, "loc_4A0"),
        (5, "loc_4AC"),
        (6, "loc_4B8"),
        (SWITCH_DEFAULT, "loc_4C4"),
    )


    label("loc_470")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_47C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_488")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_494")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4A0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4AC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D0")

    label("loc_4E7")

    Return()

    # Function_0_430 end

    def Function_1_4E8(): pass

    label("Function_1_4E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_548")
    OP_95(0xFE, 26860, -2000, 2200, 2000, 0x0)
    OP_95(0xFE, -4019, -1800, 2200, 2000, 0x0)
    OP_95(0xFE, -3510, -1800, -1500, 2000, 0x0)
    OP_95(0xFE, 26860, -2000, -2060, 2000, 0x0)
    Jump("Function_1_4E8")

    label("loc_548")

    Return()

    # Function_1_4E8 end

    def Function_2_549(): pass

    label("Function_2_549")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A9")
    OP_95(0xFE, -1970, -2000, 34720, 2000, 0x0)
    OP_95(0xFE, -1970, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 34720, 2000, 0x0)
    Jump("Function_2_549")

    label("loc_5A9")

    Return()

    # Function_2_549 end

    def Function_3_5AA(): pass

    label("Function_3_5AA")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrSubChip(0x8, 0x1)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrSubChip(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5FB")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_613")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)

    label("loc_613")

    Return()

    # Function_3_5AA end

    def Function_4_614(): pass

    label("Function_4_614")

    SetMapObjFrame(0xFF, "t1010_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1010_sky_y", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_64A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_64A")

    Sound(126, 1, 80, 0)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_668")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_68F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_6B1")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_6B1")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)

    label("loc_6B1")

    Return()

    # Function_4_614 end

    def Function_5_6B2(): pass

    label("Function_5_6B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_6C3")
    Jump("loc_7AE")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_738")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DE")
    Call(0, 6)
    Jump("loc_733")

    label("loc_6DE")


    #C0001
    ChrTalk(
        0x8,
        "泽鲁真不像话，太不像话了。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "竟然让淑女丢脸，\x01",
            "这实在不是一名绅士该有的行为。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_733")

    Jump("loc_7AE")

    label("loc_738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_7AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_753")
    Call(0, 6)
    Jump("loc_7AE")

    label("loc_753")


    #C0003
    ChrTalk(
        0x8,
        "泽鲁真不像话，太不像话了。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "为了将来能成为我的好老公，\x01",
            "你必须要做到那种程度才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AE")

    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x1)
    Return()

    # Function_5_6B2 end

    def Function_6_7B6(): pass

    label("Function_6_7B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_895")

    #C0005
    ChrTalk(
        0x8,
        (
            "听好哦，泽鲁。\x01",
            "你可是我的未婚夫，\x01",
            "必须要放眼未来才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "『最理想的结果还是头生女二生男』……\x01",
            "妈妈曾经这样说过……你觉得呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        "头生二生……？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        "你、你在说什么？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        "……没、没什么。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        "？？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C0")

    label("loc_895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9C0")

    #C0011
    ChrTalk(
        0x8,
        (
            "听好哦，泽鲁。\x01",
            "你可是我的未婚夫，\x01",
            "一定要成为一个帅气的人才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "你要成为一个头脑聪明，擅长运动，\x01",
            "而且还对我温柔体贴的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "说、说是这么说……\x01",
            "但具体要怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "首先，你每天都要做一百次\x01",
            "俯卧撑和仰卧起坐。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "还有，主日学校的考试一定\x01",
            "要得满分。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        "这、这是不可能的……\x02",
    )

    CloseMessageWindow()

    label("loc_9C0")

    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_6_7B6 end

    def Function_7_9CE(): pass

    label("Function_7_9CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_9DF")
    Jump("loc_AC2")

    label("loc_9DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FA")
    Call(0, 6)
    Jump("loc_A50")

    label("loc_9FA")


    #C0017
    ChrTalk(
        0x9,
        (
            "有时候，我真的搞不懂\x01",
            "艾米在说什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "什么头生二生的……\x01",
            "那到底是什么意思啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A50")

    Jump("loc_AC2")

    label("loc_A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_AC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A70")
    Call(0, 6)
    Jump("loc_AC2")

    label("loc_A70")


    #C0019
    ChrTalk(
        0x9,
        "艾米的目标实在是太高了。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            "人生只能顺其自然，\x01",
            "把目标定得那么高\x01",
            "也没用啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC2")

    TalkEnd(0xFE)
    SetChrSubChip(0x9, 0x2)
    Return()

    # Function_7_9CE end

    def Function_8_ACA(): pass

    label("Function_8_ACA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_ADB")
    Jump("loc_DB6")

    label("loc_ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF2")

    #C0021
    ChrTalk(
        0xA,
        (
            "哼，你们这些庶民，\x01",
            "来这种地方做什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x153,
        "#01105F嗯？\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(822, 0, 100, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x153)

    #C0023
    ChrTalk(
        0xA,
        "……不……没什么。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xA,
        (
            "真的没什么啦，\x01",
            "拜托你别再带着那种\x01",
            "纯真无邪的笑容看我了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#00012F（哈哈……琪雅真是天下无敌啊。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C45")

    label("loc_BF2")


    #C0026
    ChrTalk(
        0xA,
        "……拜托你，快走开吧。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        (
            "我竟然用那么刻薄的话向你挑衅，\x01",
            "实在是太差劲了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C45")

    Jump("loc_DB6")

    label("loc_C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CBE")

    #C0028
    ChrTalk(
        0xA,
        (
            "刚才往迎宾馆那边走去的\x01",
            "那个绿发女孩……\x01",
            "总觉得以前曾经见过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xA,
        "唔……到底是什么时候的事呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB6")

    label("loc_CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_DB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D70")

    #C0030
    ChrTalk(
        0xA,
        "哎呀呀，你来这里做什么？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        (
            "这里是高级别墅区哦，\x01",
            "和庶民可是完全无关的……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        (
            "……哼，算了。\x01",
            "你就好好瞧瞧我们有钱人\x01",
            "住的房子是多么富丽堂皇吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DB6")

    label("loc_D70")


    #C0033
    ChrTalk(
        0xA,
        (
            "……哼，算了。\x01",
            "你就好好瞧瞧我们有钱人\x01",
            "住的房子是多么富丽堂皇吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB6")

    TalkEnd(0xFE)
    Return()

    # Function_8_ACA end

    def Function_9_DBA(): pass

    label("Function_9_DBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_DCB")
    Jump("loc_FFA")

    label("loc_DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_E71")

    #C0034
    ChrTalk(
        0xB,
        (
            "自从哈尔特曼前议长下台之后，\x01",
            "附近那群危险的家伙\x01",
            "也不见踪影了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xB,
        (
            "那栋宅邸变成迎宾馆之后，\x01",
            "警备力度加强了不少，\x01",
            "治安状况也因此得到了明显改善。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FFA")

    label("loc_E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_FFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F61")

    #C0036
    ChrTalk(
        0xB,
        (
            "哈尔特曼前议长的宅邸在不久前\x01",
            "成为了迎宾馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        (
            "在前一段时间的通商会议时，\x01",
            "还让各国首脑入住\x01",
            "其中了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        (
            "那个地方以前经常用来举办危险的宴会。\x01",
            "与那时相比，现在真是变成一个\x01",
            "很有意义，也非常正规的好地方了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_FFA")

    label("loc_F61")


    #C0039
    ChrTalk(
        0xB,
        (
            "哈尔特曼前议长的宅邸在不久前\x01",
            "成为了迎宾馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        (
            "那个地方以前经常用来举办危险的聚会。\x01",
            "与那时相比，现在真是变成一个\x01",
            "很有意义，也非常正规的好地方了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFA")

    TalkEnd(0xFE)
    Return()

    # Function_9_DBA end

    def Function_10_FFE(): pass

    label("Function_10_FFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_107B")

    #C0041
    ChrTalk(
        0xFE,
        (
            "宣传册上登载的那栋房子……\x01",
            "应该就在这里了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "地理位置得天独厚，湖光尽收眼底……\x01",
            "的确不错呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_10D6")

    label("loc_107B")


    #C0043
    ChrTalk(
        0xFE,
        (
            "地理位置得天独厚，湖光尽收眼底……\x01",
            "的确不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        "干脆就下定决心，买下这栋房子吧。\x02",
    )

    CloseMessageWindow()

    label("loc_10D6")

    TalkEnd(0xFE)
    Return()

    # Function_10_FFE end

    def Function_11_10DA(): pass

    label("Function_11_10DA")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("monster/ch82050.itc", 0x24)
    LoadChrToIndex("monster/ch82051.itc", 0x25)
    LoadChrToIndex("monster/ch86150.itc", 0x26)
    LoadChrToIndex("monster/ch86151.itc", 0x27)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 5500, 0, 2000, 315)
    OP_90(0x104, 6500, 0, 2000, 315)
    OP_90(0x103, 6500, 0, 500, 315)
    OP_90(0x109, 5500, 0, 500, 315)
    OP_90(0x105, 7500, 0, 1250, 315)
    OP_90(0x106, 4500, 0, 1250, 315)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0xD, 0x24)
    SetChrChipByIndex(0xE, 0x24)
    SetChrChipByIndex(0xF, 0x24)
    SetChrChipByIndex(0x10, 0x24)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 12)
    BeginChrThread(0xE, 0, 0, 12)
    BeginChrThread(0xF, 0, 0, 12)
    BeginChrThread(0x10, 0, 0, 12)
    BeginChrThread(0x12, 0, 0, 14)
    SetChrPos(0xE, -1800, -2000, 19500, 180)
    SetChrPos(0xF, 0, -2000, 18500, 180)
    SetChrPos(0x10, 1800, -2000, 19500, 180)
    SetChrPos(0x12, 0, -2000, 22500, 180)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    FadeToBright(1000, 0)
    OP_68(2700, -500, 1500, 0)
    OP_68(0, -500, 4500, 2500)
    MoveCamera(315, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)

    def lambda_138B():
        OP_95(0xFE, -1500, 0, 4250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_138B)
    Sleep(50)

    def lambda_13A8():
        OP_95(0xFE, -500, 0, 5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13A8)
    Sleep(50)

    def lambda_13C5():
        OP_95(0xFE, 500, 0, 5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13C5)
    Sleep(50)

    def lambda_13E2():
        OP_95(0xFE, -500, 0, 3500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13E2)
    Sleep(50)

    def lambda_13FF():
        OP_95(0xFE, 500, 0, 3500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13FF)
    Sleep(50)

    def lambda_141C():
        OP_95(0xFE, 1500, 0, 4250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_141C)
    Sleep(800)
    Sound(948, 0, 30, 0)
    Sound(911, 0, 100, 0)
    WaitChrThread(0x106, 1)

    def lambda_1449():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1449)
    WaitChrThread(0x101, 1)

    def lambda_145A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_145A)
    WaitChrThread(0x104, 1)

    def lambda_146B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_146B)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x109, 1)

    def lambda_1512():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1512)
    WaitChrThread(0x103, 1)

    def lambda_1523():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1523)
    WaitChrThread(0x105, 1)

    def lambda_1534():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1534)
    OP_6F(0x79)
    OP_0D()
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x12, 0x8)
    OP_68(150, -500, 18040, 2000)
    MoveCamera(321, 21, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(25000, 2000)
    OP_6F(0x79)

    #C0045
    ChrTalk(
        0x101,
        "#00010F#2P啧，这是新的军用魔兽吗！？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x104,
        "#00307F#2P是赤狮！大家小心！\x02",
    )

    CloseMessageWindow()
    OP_68(0, -500, 8000, 1100)
    SetCameraDistance(18000, 1100)
    Sound(911, 0, 80, 0)
    Sound(948, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x25)
    BeginChrThread(0xE, 0, 0, 13)

    def lambda_1604():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1604)
    Sleep(50)
    SetChrChipByIndex(0xF, 0x25)
    BeginChrThread(0xF, 0, 0, 13)

    def lambda_1626():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1626)
    Sleep(50)
    SetChrChipByIndex(0x10, 0x25)
    BeginChrThread(0x10, 0, 0, 13)

    def lambda_1648():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1648)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x27)
    BeginChrThread(0x12, 0, 0, 15)

    def lambda_166A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_166A)
    Sleep(50)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    Sleep(700)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(18000, 300)
    Sleep(300)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xF, 0x0)
    EndChrThread(0x10, 0x0)
    EndChrThread(0x11, 0x0)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x14, 0x0)
    Battle("BattleInfo_3AC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrPos(0x0, 0, -1800, 6000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A3, 7)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_10DA end

    def Function_12_17B1(): pass

    label("Function_12_17B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17CF")
    OP_A1(0xFE, 0x6A4, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_12_17B1")

    label("loc_17CF")

    Return()

    # Function_12_17B1 end

    def Function_13_17D0(): pass

    label("Function_13_17D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17EE")
    OP_A1(0xFE, 0xBB8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_13_17D0")

    label("loc_17EE")

    Return()

    # Function_13_17D0 end

    def Function_14_17EF(): pass

    label("Function_14_17EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_180B")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_14_17EF")

    label("loc_180B")

    Return()

    # Function_14_17EF end

    def Function_15_180C(): pass

    label("Function_15_180C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1828")
    OP_A1(0xFE, 0x960, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_15_180C")

    label("loc_1828")

    Return()

    # Function_15_180C end

    SaveToFile()

Try(main)
