from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c020b.bin",                # FileName
        "c020b",                    # MapName
        "c020b",                    # Location
        0x000A,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 10, 0, 3, 0, 4],
    )

    BuildStringList((
        "c020b",                  # 0
        "隆",                     # 1
        "庞斯",                   # 2
        "布利克",                 # 3
        "车",                     # 4
        "SE控制",                 # 5
        "警官",                   # 6
        "中央广场",               # 7
        "西街",                   # 8
        "行政区",                 # 9
        "住宅街",                 # 10
        "欢乐街",                 # 11
        "东街",                   # 12
        "旧城区",                 # 13
        "港湾区",                 # 14
        "ＩＢＣ",                 # 15
        "站前街道",               # 16
        "后巷",                   # 17
        "乌尔斯拉间道",           # 18
        "东克洛斯贝尔街道",       # 19
        "西克洛斯贝尔街道",       # 20
        "玛因兹山道",             # 21
        "兰花塔",                 # 22
    ))

    AddCharChip((
        "chr/ch20600.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20402.itc",                   # 03
        "chr/ch30000.itc",                   # 04
    ))

    DeclNpc(-1000,   0,       610,     90,   257,  0x0, 0,   0,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(-15119,  0,       5829,    270,  261,  0x0, 0,   2,   0,   0,   2,   0,   7,   255,  0)
    DeclNpc(6570,    -150,    5119,    90,   341,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-30459,  0,       7500,    180,  385,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(14500,   -6500,   -13500,  1200,    14500,   -5500,   -13500,  0x007C, 0,  5,  0x0000)
    DeclActor(33490,   -4000,   -16740,  1500,    33490,   -2000,   -16740,  0x007C, 0,  10, 0x0000)
    DeclActor(-34530,  0,       4350,    1500,    -34530,  1500,    4350,    0x007C, 0,  19, 0x0000)

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "中央广场")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "西街")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "行政区")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "住宅街")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "欢乐街")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "东街")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "旧城区")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "港湾区")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "站前街道")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "后巷")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(91.0, 0.0, 213.0, 0x0000, 0x0000, "兰花塔")
    PlaceName(48.75, 0.0, -21.0, 0x0000, 0x0051, "")
    PlaceName(102.5, 0.0, 5.0, 0x0000, 0x0054, "")
    PlaceName(73.25, 0.0, -29.0, 0x0000, 0x0057, "")
    PlaceName(48.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(68.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(17.75, 0.0, 3.0, 0x0000, 0x0053, "")
    PlaceName(8.0, 0.0, 24.0, 0x0000, 0x0053, "")
    PlaceName(32.0, 0.0, 56.0, 0x0000, 0x0052, "")
    PlaceName(36.75, 0.0, 43.0, 0x0000, 0x0053, "")
    PlaceName(45.5, 0.0, 34.5, 0x0000, 0x0053, "")
    PlaceName(74.0, 0.0, 105.5, 0x0000, 0x0051, "")
    PlaceName(186.0, 0.0, -30.0, 0x0000, 0x0052, "")
    PlaceName(169.0, 0.0, -120.5, 0x0000, 0x0053, "")
    PlaceName(156.0, 0.0, -102.0, 0x0000, 0x0053, "")

    ChipFrameInfo(1124, 0)                                       # 0

    ScpFunction((
        "Function_0_464",          # 00, 0
        "Function_1_514",          # 01, 1
        "Function_2_575",          # 02, 2
        "Function_3_5D6",          # 03, 3
        "Function_4_5F4",          # 04, 4
        "Function_5_67D",          # 05, 5
        "Function_6_7B8",          # 06, 6
        "Function_7_8C4",          # 07, 7
        "Function_8_995",          # 08, 8
        "Function_9_A0D",          # 09, 9
        "Function_10_B6C",         # 0A, 10
        "Function_11_BAF",         # 0B, 11
        "Function_12_1088",        # 0C, 12
        "Function_13_1109",        # 0D, 13
        "Function_14_113A",        # 0E, 14
        "Function_15_116B",        # 0F, 15
        "Function_16_119C",        # 10, 16
        "Function_17_11F2",        # 11, 17
        "Function_18_1223",        # 12, 18
        "Function_19_1251",        # 13, 19
    ))


    def Function_0_464(): pass

    label("Function_0_464")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_49C"),
        (1, "loc_4A8"),
        (2, "loc_4B4"),
        (3, "loc_4C0"),
        (4, "loc_4CC"),
        (5, "loc_4D8"),
        (6, "loc_4E4"),
        (SWITCH_DEFAULT, "loc_4F0"),
    )


    label("loc_49C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4A8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4B4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4C0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4CC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4D8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_513")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_513")

    Return()

    # Function_0_464 end

    def Function_1_514(): pass

    label("Function_1_514")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_574")
    OP_95(0xFE, 7000, -300, 610, 6000, 0x0)
    OP_95(0xFE, 7000, 0, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, -10, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, 0, 610, 6000, 0x0)
    Jump("Function_1_514")

    label("loc_574")

    Return()

    # Function_1_514 end

    def Function_2_575(): pass

    label("Function_2_575")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D5")
    OP_95(0xFE, -10000, 0, 5750, 800, 0x0)
    OP_95(0xFE, -10000, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 5750, 800, 0x0)
    Jump("Function_2_575")

    label("loc_5D5")

    Return()

    # Function_2_575 end

    def Function_3_5D6(): pass

    label("Function_3_5D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_5E5")
    ClearScenarioFlags(0x22, 0)
    Event(0, 11)

    label("loc_5E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5F3")
    ClearChrFlags(0xD, 0x80)

    label("loc_5F3")

    Return()

    # Function_3_5D6 end

    def Function_4_5F4(): pass

    label("Function_4_5F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_607")
    OP_70(0xF, 0x0)
    Jump("loc_60B")

    label("loc_607")

    OP_70(0xF, 0x1E)

    label("loc_60B")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_61D")
    Jump("loc_676")

    label("loc_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_676")
    ClearChrFlags(0xB, 0x80)
    OP_78(0xE, 0xB)
    SetChrPos(0xB, 34510, -4000, -15670, 270)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFlags(0xE, 0x2)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_676")

    ClearMapObjFlags(0x7, 0x10)
    Return()

    # Function_4_5F4 end

    def Function_5_67D(): pass

    label("Function_5_67D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76F")
    Sound(14, 0, 100, 0)
    OP_74(0xF, 0x1E)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x358, 1)"), scpexpr(EXPR_END)), "loc_700")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_76A")

    label("loc_700")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x0)

    label("loc_76A")

    Jump("loc_7AC")

    label("loc_76F")

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

    label("loc_7AC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_67D end

    def Function_6_7B8(): pass

    label("Function_6_7B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_879")

    #C0004
    ChrTalk(
        0xFE,
        (
            "明天好像要在兰花塔\x01",
            "举行一个叫做\x01",
            "通商什么的活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "虽然不太了解，\x01",
            "但机会难得，\x01",
            "我准备和亨利他们一起去参观。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "嘿嘿，那肯定是一场\x01",
            "有趣的宴会吧，\x01",
            "好期待明天啊～¤\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8C0")

    label("loc_879")


    #C0007
    ChrTalk(
        0xFE,
        (
            "那个叫通商什么的活动\x01",
            "多半是一场宴会吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "嘿嘿，好期待明天啊～\x02",
    )

    CloseMessageWindow()

    label("loc_8C0")

    TalkEnd(0xFE)
    Return()

    # Function_6_7B8 end

    def Function_7_8C4(): pass

    label("Function_7_8C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95B")

    #C0009
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "感光回路\x01",
            "已经用完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "看来是在白天的揭幕式上\x01",
            "拍了太多照片。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "在导力商店关门之前，\x01",
            "得赶快去买个新的感光回路。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_991")

    label("loc_95B")


    #C0012
    ChrTalk(
        0xFE,
        (
            "在导力商店关门之前，\x01",
            "得赶快去买个\x01",
            "新的感光回路。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_991")

    TalkEnd(0xFE)
    Return()

    # Function_7_8C4 end

    def Function_8_995(): pass

    label("Function_8_995")

    TalkBegin(0xFE)

    #C0013
    ChrTalk(
        0xFE,
        (
            "在这里边喝咖啡边看书，\x01",
            "不知不觉就已经这么晚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "（抖）……\x01",
            "晚上果然很冷啊，\x01",
            "趁着还没感冒，赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_995 end

    def Function_9_A0D(): pass

    label("Function_9_A0D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_B68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2D")

    #C0015
    ChrTalk(
        0xFE,
        "各位辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "在通商会议期间，将会强化警备力度，\x01",
            "限制车辆在晚间出行。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "如想驾车前往市外，\x01",
            "请在这里申请。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x10A,
        (
            "#00604F警备工作辛苦了，\x01",
            "保持这种状态，继续努力吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0019
    ChrTalk(
        0xFE,
        "达德利搜查官！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "您正在执行任务吗？\x01",
            "真是辛苦了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B68")

    label("loc_B2D")


    #C0021
    ChrTalk(
        0xFE,
        (
            "目前并没有发现\x01",
            "可疑车辆。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "这里的工作就交给我吧。\x02",
    )

    CloseMessageWindow()

    label("loc_B68")

    TalkEnd(0xFE)
    Return()

    # Function_9_A0D end

    def Function_10_B6C(): pass

    label("Function_10_B6C")

    TalkBegin(0xFF)

    #C0023
    ChrTalk(
        0x101,
        (
            "#00000F地下空间离这里不远，步行就可以了，\x01",
            "没必要开车。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_10_B6C end

    def Function_11_BAF(): pass

    label("Function_11_BAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x153, 0x8)
    SoundLoad(468)
    ClearChrFlags(0xB, 0x80)
    OP_78(0xE, 0xB)
    OP_49()
    SetChrPos(0xB, 40500, 2080, -8000, 270)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    OP_74(0xE, 0x1E)
    OP_71(0xE, 0x79, 0xB4, 0x1, 0x20)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C60")
    EndChrThread(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 12500, 0, -6000, 270)

    def lambda_C50():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C50)

    label("loc_C60")

    FadeToBright(1000, 0)
    BeginChrThread(0xB, 3, 0, 12)
    BeginChrThread(0xC, 1, 0, 18)
    OP_68(15900, 2550, -18000, 0)
    MoveCamera(24, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19500, 0)
    OP_68(19700, -150, -19350, 10000)
    MoveCamera(60, 21, 0, 10000)
    Sleep(8000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xB, 0x3)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    ClearChrFlags(0x153, 0x8)
    SetChrPos(0x101, 34500, -4000, -17900, 180)
    SetChrPos(0x102, 34500, -4000, -17900, 180)
    SetChrPos(0x109, 34500, -4000, -17900, 180)
    SetChrPos(0x105, 34500, -4000, -17900, 180)
    SetChrPos(0x153, 34500, -4000, -17900, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 34550, -4000, -15850, 270)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    OP_70(0xE, 0x78)
    OP_68(34650, -3250, -16450, 0)
    MoveCamera(30, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16650, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(462, 0, 100, 0)
    OP_71(0xE, 0x12D, 0x14A, 0x1, 0x8)
    Sleep(1000)
    Sleep(250)
    OP_68(34650, -3250, -18450, 7000)
    VolumeBGM(0x46, 0x1770)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(1000)
    BeginChrThread(0x153, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 14)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 15)
    Sleep(1000)
    BeginChrThread(0x109, 3, 0, 16)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x153, 3)
    OP_6F(0x79)
    OP_93(0x101, 0x10E, 0x1F4)

    #C0024
    ChrTalk(
        0x101,
        (
            "#00002F#11P呼……这么大的城市，\x01",
            "一旦开车，却可以轻松绕一大圈呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EA5():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EA5)
    Sleep(100)

    def lambda_EB5():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_EB5)
    Sleep(100)

    def lambda_EC5():
        TurnDirection(0x153, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_EC5)
    Sleep(100)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x153, 0)

    #C0025
    ChrTalk(
        0x105,
        "#10309F#6P呵呵，感觉真不错啊。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x153,
        (
            "#01109F#6P嘿嘿，好开心！\x02\x03",

            "#01110F虽然街景和平时一样，\x01",
            "但看上去的感觉完全不同了！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#00109F#6P呵呵，确实如此。\x02\x03",

            "#00100F简直就像在城市的灯海中\x01",
            "遨游一般。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    #C0028
    ChrTalk(
        0x101,
        (
            "#00000F#11P今后如果需要出远门，\x01",
            "就可以开车出行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x109,
        (
            "#10109F#5P嗯，这辆车的耐久性很高，\x01",
            "各种路况应该都没问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#00102F#6P呵呵……\x01",
            "真要好好感谢迪塔叔叔啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    VolumeBGM(0x64, 0x32)
    Sleep(50)
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_BAF end

    def Function_12_1088(): pass

    label("Function_12_1088")

    SetChrPos(0xFE, 40500, 2080, -8000, 270)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 28850, 300, -8000)
    OP_9F(0x1, 21700, 150, -8000)
    OP_9F(0x1, 19600, 150, -8850)
    OP_9F(0x1, 18650, 150, -11150)
    OP_9F(0x1, 18350, -1850, -19050)
    OP_9F(0x1, 20700, -1850, -20250)
    OP_9F(0x1, 26850, -3850, -20250)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_12_1088 end

    def Function_13_1109(): pass

    label("Function_13_1109")


    def lambda_110E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_110E)
    OP_95(0xFE, 36480, -4000, -19100, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_1109 end

    def Function_14_113A(): pass

    label("Function_14_113A")


    def lambda_113F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_113F)
    OP_95(0xFE, 33950, -4000, -20400, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_14_113A end

    def Function_15_116B(): pass

    label("Function_15_116B")


    def lambda_1170():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1170)
    OP_95(0xFE, 32850, -4000, -19600, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_15_116B end

    def Function_16_119C(): pass

    label("Function_16_119C")


    def lambda_11A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11A1)
    OP_95(0xFE, 34450, -4000, -18500, 2000, 0x0)
    Sleep(100)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    Sound(461, 0, 100, 0)
    OP_71(0xE, 0x14B, 0x168, 0x0, 0x8)
    Sleep(1000)
    Sleep(200)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_119C end

    def Function_17_11F2(): pass

    label("Function_17_11F2")


    def lambda_11F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11F7)
    OP_95(0xFE, 35050, -4000, -19950, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_11F2 end

    def Function_18_1223(): pass

    label("Function_18_1223")

    Sound(468, 2, 100, 0)
    Sound(458, 0, 80, 0)
    Sleep(4000)
    Sound(493, 0, 100, 0)
    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(3000)
    Sound(492, 0, 60, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_18_1223 end

    def Function_19_1251(): pass

    label("Function_19_1251")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    #A0031
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

    # Function_19_1251 end

    SaveToFile()

Try(main)
