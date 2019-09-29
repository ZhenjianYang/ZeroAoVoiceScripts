from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c030b.bin",                # FileName
        "c030b",                    # MapName
        "c030b",                    # Location
        0x002A,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 42, 0, 1, 0, 2],
    )

    BuildStringList((
        "c030b",                  # 0
        "雷兹老人",               # 1
        "本特斯",                 # 2
        "警官",                   # 3
        "警官",                   # 4
        "车",                     # 5
        "车",                     # 6
        "车",                     # 7
        "警官",                   # 8
        "中央广场",               # 9
        "西街",                   # 10
        "行政区",                 # 11
        "住宅街",                 # 12
        "欢乐街",                 # 13
        "东街",                   # 14
        "旧城区",                 # 15
        "港湾区",                 # 16
        "ＩＢＣ",                 # 17
        "站前街道",               # 18
        "后巷",                   # 19
        "乌尔斯拉间道",           # 20
        "东克洛斯贝尔街道",       # 21
        "西克洛斯贝尔街道",       # 22
        "玛因兹山道",             # 23
        "兰花塔",                 # 24
    ))

    AddCharChip((
        "chr/ch21602.itc",                   # 00
        "chr/ch33000.itc",                   # 01
        "chr/ch30000.itc",                   # 02
    ))

    DeclNpc(-12850,  -5900,   -31489,  315,  261,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(32279,   0,       -4369,   270,  257,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(22500,   0,       -2569,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(22500,   0,       -6449,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-14159,  300,     14789,   270,  385,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)

    DeclEvent(0x0000, 0, 13,  25.1200008392334,      -4.449999809265137,    -1.0,                  306.25,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571343421936,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.02400016784668,     0.6357142329216003,    0.20000000298023224,   1.0])

    DeclActor(-2700,   -6500,   -38000,  2000,    -2700,   -5500,   -38000,  0x007C, 0,  10, 0x0000)
    DeclActor(-35330,  -4950,   -41950,  1200,    -35330,  -3950,   -41950,  0x007C, 0,  3,  0x0000)
    DeclActor(17650,   0,       -800,    2000,    17650,   1500,    -800,    0x007C, 0,  15, 0x0000)
    DeclActor(0,       0,       -770,    2000,    0,       1500,    -770,    0x007C, 0,  14, 0x0000)
    DeclActor(-16210,  300,     18010,   1500,    -16210,  1800,    18010,   0x007C, 0,  16, 0x0000)

    PlaceName(167.6699981689453, 0.0, -124.73999786376953, 0x0000, 0x0000, "中央广场")
    PlaceName(61.15999984741211, 0.0, -117.44999694824219, 0x0000, 0x0000, "西街")
    PlaceName(211.41000366210938, 0.0, 19.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-37.66999816894531, 0.0, 3.240000009536743, 0x0000, 0x0000, "住宅街")
    PlaceName(80.5999984741211, 0.0, -9.720000267028809, 0x0000, 0x0000, "欢乐街")
    PlaceName(299.29998779296875, 0.0, -162.0, 0x0000, 0x0000, "东街")
    PlaceName(356.80999755859375, 0.0, -251.10000610351562, 0x0000, 0x0000, "旧城区")
    PlaceName(344.6600036621094, 0.0, -55.08000183105469, 0x0000, 0x0000, "港湾区")
    PlaceName(302.5400085449219, 0.0, 97.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(185.89999389648438, 0.0, -236.52000427246094, 0x0000, 0x0000, "站前街道")
    PlaceName(109.76000213623047, 0.0, -68.04000091552734, 0x0000, 0x0000, "后巷")
    PlaceName(181.0399932861328, 0.0, -286.739990234375, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(386.7799987792969, 0.0, -139.32000732421875, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-21.469999313354492, 0.0, -119.87999725341797, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-11.75, 0.0, 42.119998931884766, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(200.0, 0.0, 231.5, 0x0000, 0x0000, "兰花塔")
    PlaceName(132.02999877929688, 0.0, -147.4199981689453, 0x0000, 0x0051, "")
    PlaceName(219.11000061035156, 0.0, -105.30000305175781, 0x0000, 0x0054, "")
    PlaceName(171.72000122070312, 0.0, -160.3800048828125, 0x0000, 0x0057, "")
    PlaceName(130.82000732421875, 0.0, -100.44000244140625, 0x0000, 0x0053, "")
    PlaceName(164.02999877929688, 0.0, -61.560001373291016, 0x0000, 0x0053, "")
    PlaceName(81.80999755859375, 0.0, -108.54000091552734, 0x0000, 0x0053, "")
    PlaceName(66.0199966430664, 0.0, -74.5199966430664, 0x0000, 0x0053, "")
    PlaceName(104.9000015258789, 0.0, -22.68000030517578, 0x0000, 0x0052, "")
    PlaceName(112.58999633789062, 0.0, -43.7400016784668, 0x0000, 0x0053, "")
    PlaceName(126.7699966430664, 0.0, -57.5099983215332, 0x0000, 0x0053, "")
    PlaceName(172.94000244140625, 0.0, 57.5099983215332, 0x0000, 0x0051, "")
    PlaceName(354.3800048828125, 0.0, -162.0, 0x0000, 0x0052, "")
    PlaceName(326.8399963378906, 0.0, -308.6099853515625, 0x0000, 0x0053, "")
    PlaceName(305.7799987792969, 0.0, -278.6400146484375, 0x0000, 0x0053, "")

    ChipFrameInfo(1328, 0)                                       # 0

    ScpFunction((
        "Function_0_530",          # 00, 0
        "Function_1_5E0",          # 01, 1
        "Function_2_627",          # 02, 2
        "Function_3_6B7",          # 03, 3
        "Function_4_7F2",          # 04, 4
        "Function_5_839",          # 05, 5
        "Function_6_93A",          # 06, 6
        "Function_7_A9E",          # 07, 7
        "Function_8_AE4",          # 08, 8
        "Function_9_BA2",          # 09, 9
        "Function_10_C12",         # 0A, 10
        "Function_11_E93",         # 0B, 11
        "Function_12_1197",        # 0C, 12
        "Function_13_11FD",        # 0D, 13
        "Function_14_12AB",        # 0E, 14
        "Function_15_12D4",        # 0F, 15
        "Function_16_12FD",        # 10, 16
    ))


    def Function_0_530(): pass

    label("Function_0_530")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_568"),
        (1, "loc_574"),
        (2, "loc_580"),
        (3, "loc_58C"),
        (4, "loc_598"),
        (5, "loc_5A4"),
        (6, "loc_5B0"),
        (SWITCH_DEFAULT, "loc_5BC"),
    )


    label("loc_568")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5C8")

    label("loc_574")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5C8")

    label("loc_580")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5C8")

    label("loc_58C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5C8")

    label("loc_598")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5C8")

    label("loc_5A4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5C8")

    label("loc_5B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5C8")

    label("loc_5BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5C8")

    label("loc_5C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5DF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5C8")

    label("loc_5DF")

    Return()

    # Function_0_530 end

    def Function_1_5E0(): pass

    label("Function_1_5E0")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 13450, 0, -4760, 45)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_626")
    ClearScenarioFlags(0x22, 0)
    Event(0, 11)

    label("loc_626")

    Return()

    # Function_1_5E0 end

    def Function_2_627(): pass

    label("Function_2_627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63C")
    ClearMapObjFlags(0x2, 0x10)
    Jump("loc_640")

    label("loc_63C")

    OP_65(0x0, 0x1)

    label("loc_640")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0x14, 0x10)
    OP_70(0x0, 0x0)
    OP_70(0x1, 0xA)
    OP_70(0x3, 0xA)
    OP_70(0x4, 0xA)
    OP_70(0x5, 0x0)
    OP_70(0x6, 0xA)
    OP_70(0x14, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_699")
    OP_70(0x18, 0x0)
    Jump("loc_69D")

    label("loc_699")

    OP_70(0x18, 0x1E)

    label("loc_69D")

    ClearMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1C, 0x1000)
    SetMapObjFrame(0x1C, "light", 0x0, 0x1)
    Return()

    # Function_2_627 end

    def Function_3_6B7(): pass

    label("Function_3_6B7")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A9")
    Sound(14, 0, 100, 0)
    OP_74(0x18, 0x1E)
    OP_71(0x18, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5DE, 1)"), scpexpr(EXPR_END)), "loc_73A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5DE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_7A4")

    label("loc_73A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x5DE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x5DE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x18, 0x1E, 0x0, 0x0, 0x0)

    label("loc_7A4")

    Jump("loc_7E6")

    label("loc_7A9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_7E6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_6B7 end

    def Function_4_7F2(): pass

    label("Function_4_7F2")

    TalkBegin(0xFE)

    #C0004
    ChrTalk(
        0xFE,
        (
            "哦哦，天都已经\x01",
            "这么黑了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "我差不多也该\x01",
            "动身回家了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_7F2 end

    def Function_5_839(): pass

    label("Function_5_839")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CF")

    #C0006
    ChrTalk(
        0xFE,
        (
            "我好像听到\x01",
            "有小女孩的声音\x01",
            "从那所房屋中传出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "嗯？可那所房屋\x01",
            "一直都是无人居住的……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "唔，算了，大概只是我幻听吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_936")

    label("loc_8CF")


    #C0009
    ChrTalk(
        0xFE,
        (
            "说起来，大约在十年前，\x01",
            "还曾流传过那所房屋\x01",
            "有幽灵出现的传闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "呼，但也只是个\x01",
            "无聊的传闻而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_936")

    TalkEnd(0xFE)
    Return()

    # Function_5_839 end

    def Function_6_93A(): pass

    label("Function_6_93A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A36")

    #C0011
    ChrTalk(
        0xFE,
        (
            "不好意思，在会议期间，\x01",
            "晚间出行是要受到限制的。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "如想从这里经过，\x01",
            "请提交您的身份证明材料。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#00008F（只要说明我们的身份，\x01",
            "  对方应该就会放行了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x10A,
        (
            "#00603F（并没有这个必要，\x01",
            "  还是尽快前往地下空间吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A9A")

    label("loc_A36")


    #C0015
    ChrTalk(
        0xFE,
        (
            "不好意思，在会议期间，\x01",
            "晚间出行是要受到限制的。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "如想从这里经过，\x01",
            "请提交您的身份证明材料。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9A")

    TalkEnd(0xFE)
    Return()

    # Function_6_93A end

    def Function_7_A9E(): pass

    label("Function_7_A9E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB3")
    Call(0, 8)
    Jump("loc_AE0")

    label("loc_AB3")


    #C0017
    ChrTalk(
        0xFE,
        "大家辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "这一带目前\x01",
            "并无异常。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE0")

    TalkEnd(0xFE)
    Return()

    # Function_7_A9E end

    def Function_8_AE4(): pass

    label("Function_8_AE4")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0x0, 0)

    #C0019
    ChrTalk(
        0xA,
        "大家辛苦了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 500)

    #C0020
    ChrTalk(
        0xB,
        (
            "首脑们的观剧活动\x01",
            "即将结束，\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x10A,
        (
            "#00603F不，没什么。\x01",
            "封锁方面的工作就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xA,
        "明白！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xB,
        "明白！\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x10E, 0x0)
    OP_93(0xB, 0x10E, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x149, 2)
    Return()

    # Function_8_AE4 end

    def Function_9_BA2(): pass

    label("Function_9_BA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB7")
    Call(0, 8)
    Jump("loc_C0E")

    label("loc_BB7")


    #C0024
    ChrTalk(
        0xFE,
        (
            "首脑们的观剧活动\x01",
            "即将结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "在首脑们离开之前，\x01",
            "这里将会完全封锁，\x01",
            "敬请谅解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0E")

    TalkEnd(0xFE)
    Return()

    # Function_9_BA2 end

    def Function_10_C12(): pass

    label("Function_10_C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C49")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Jump("loc_E92")

    label("loc_C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E92")
    EventBegin(0x0)
    Fade(500)
    OP_68(-3600, -4900, -38500, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -4600, -6000, -39000, 90)
    SetChrPos(0x102, -4600, -6000, -38000, 90)
    SetChrPos(0x104, -5700, -6000, -39000, 90)
    SetChrPos(0x109, -5700, -6000, -38000, 90)
    SetChrPos(0x105, -5400, -6000, -36600, 135)
    SetChrPos(0x10A, -4500, -6000, -36200, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0028
    ChrTalk(
        0x104,
        (
            "#6P#00305F对了，还带着\x01",
            "这扇门的钥匙吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#5P#00004F嗯，之前已经从\x01",
            "储物柜中取出来了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D85():
        OP_96(0xFE, 0xFFFFF31C, 0xFFFFE764, 0xFFFF6B2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D85)
    WaitChrThread(0x101, 1)
    Sound(802, 0, 100, 0)
    SetChrName("")

    #A0030
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德从怀中取出了地下空间的钥匙。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(806, 0, 100, 0)
    Sleep(300)
    Sound(102, 0, 100, 0)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)
    TurnDirection(0x10A, 0x101, 500)

    #C0031
    ChrTalk(
        0x10A,
        (
            "#00603F那个小鬼的房间\x01",
            "好像就在管道的出口附近。\x02\x03",

            "#00600F立刻出发吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 500)

    #C0032
    ChrTalk(
        0x101,
        "#11P#00000F明白。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -5000, -6000, -38000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x141, 1)
    EventEnd(0x5)

    label("loc_E92")

    Return()

    # Function_10_C12 end

    def Function_11_E93(): pass

    label("Function_11_E93")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xD2, 0xD7, 0x0, 0x0)
    SoundLoad(868)
    SoundLoad(469)
    SetChrPos(0x0, -1500, -6000, -21000, 0)
    SetChrPos(0x1, -1500, -6000, -21000, 0)
    SetChrPos(0x2, -1500, -6000, -21000, 0)
    SetChrPos(0x3, -1500, -6000, -21000, 0)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x1C, 0x4)
    ClearChrFlags(0xC, 0x80)
    OP_78(0x19, 0xC)
    OP_49()
    OP_90(0xC, -16000, 300, 20000, 180)
    OP_D5(0xC, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x1000)
    OP_74(0x19, 0x1E)
    OP_71(0x19, 0x79, 0xB4, 0x1, 0x20)
    ClearChrFlags(0xD, 0x80)
    OP_78(0x1A, 0xD)
    OP_49()
    OP_90(0xD, -16000, 300, 30000, 180)
    OP_D5(0xD, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1A, 0x1000)
    SetMapObjFrame(0x1A, "mark01", 0x0, 0x1)
    SetMapObjFrame(0x1A, "mark00", 0x1, 0x1)
    OP_74(0x1A, 0x1E)
    OP_71(0x1A, 0x79, 0xB4, 0x1, 0x20)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x1B, 0xE)
    OP_49()
    OP_90(0xE, -16000, 300, 40000, 180)
    OP_D5(0xE, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1B, 0x1000)
    SetMapObjFrame(0x1B, "mark01", 0x0, 0x1)
    SetMapObjFrame(0x1B, "mark00", 0x1, 0x1)
    OP_74(0x1B, 0x1E)
    OP_71(0x1B, 0x79, 0xB4, 0x1, 0x20)
    ClearMapObjFlags(0x14, 0x10)
    OP_70(0x14, 0x1E)
    OP_68(17500, -1500, -6700, 0)
    MoveCamera(30, 7, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(55000, 0)
    Sound(868, 2, 40, 0)
    OP_68(17500, -2500, -6700, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(458, 0, 100, 0)
    Sound(469, 2, 100, 0)
    Fade(500)
    OP_68(-16000, 2300, 20000, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(17500, 0)
    MoveCamera(45, 23, 0, 11000)
    SetCameraDistance(23500, 11000)
    OP_6B(0xC)
    BeginChrThread(0xC, 3, 0, 12)
    Sleep(300)
    BeginChrThread(0xD, 3, 0, 12)
    Sleep(300)
    BeginChrThread(0xE, 3, 0, 12)
    Sleep(3000)
    Sound(457, 0, 100, 0)
    Sleep(2000)
    Sound(465, 0, 100, 0)
    Sleep(1400)
    OP_6B(0xFF)
    Sleep(2000)
    StopSound(868, 2000, 30)
    StopSound(469, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x364)
    OP_24(0x1D5)
    SetScenarioFlags(0x23, 0)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_E93 end

    def Function_12_1197(): pass

    label("Function_12_1197")

    OP_96(0xFE, 0xFFFFC180, 0x12C, 0x4650, 0x1B58, 0x0)
    OP_96(0xFE, 0xFFFFC180, 0x0, 0x0, 0x1B58, 0x0)
    OP_9E(0xFE, 0xFFFFD314, 0x0, 0xFFFEA070, 0x1B58, 0x1)
    OP_96(0xFE, 0xFFFFD314, 0x0, 0xFFFFEE6C, 0x1B58, 0x0)
    OP_96(0xFE, 0xC350, 0x0, 0xFFFFEE6C, 0x1B58, 0x0)
    Return()

    # Function_12_1197 end

    def Function_13_11FD(): pass

    label("Function_13_11FD")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1211")
    Call(0, 8)
    Jump("loc_1294")

    label("loc_1211")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0x0, 0)
    TurnDirection(0xB, 0x0, 0)

    #C0033
    ChrTalk(
        0xB,
        (
            "首脑们的观剧活动\x01",
            "即将结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "在首脑们离开之前，\x01",
            "这里将会完全封锁，\x01",
            "敬请谅解。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x10E, 0x0)
    OP_93(0xB, 0x10E, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)

    label("loc_1294")

    Sleep(50)
    SetChrPos(0x0, 21370, 0, -4360, 270)
    EventEnd(0x4)
    Return()

    # Function_13_11FD end

    def Function_14_12AB(): pass

    label("Function_14_12AB")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_14_12AB end

    def Function_15_12D4(): pass

    label("Function_15_12D4")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_15_12D4 end

    def Function_16_12FD(): pass

    label("Function_16_12FD")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门牢固地关闭着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_16_12FD end

    SaveToFile()

Try(main)
