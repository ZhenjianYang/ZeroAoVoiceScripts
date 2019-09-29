from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1650.bin",                # FileName
        "t1650",                    # MapName
        "t1650",                    # Location
        0x0058,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 88, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1650",                  # 0
        "赛兰德教授",             # 1
    ))

    AddCharChip((
        "chr/ch44802.itc",                   # 00
    ))

    DeclNpc(110690,  150,     57000,   270,  453,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)

    DeclActor(109380,  0,       57000,   1500,    110690,  1500,    57000,   0x007E, 0,  2,  0x0000)

    ChipFrameInfo(264, 0)                                        # 0

    ScpFunction((
        "Function_0_108",          # 00, 0
        "Function_1_14E",          # 01, 1
        "Function_2_1CA",          # 02, 2
        "Function_3_1CE",          # 03, 3
        "Function_4_421",          # 04, 4
        "Function_5_FD1",          # 05, 5
        "Function_6_101C",         # 06, 6
        "Function_7_1067",         # 07, 7
        "Function_8_10B2",         # 08, 8
        "Function_9_1103",         # 09, 9
        "Function_10_114E",        # 0A, 10
        "Function_11_2ADB",        # 0B, 11
    ))


    def Function_0_108(): pass

    label("Function_0_108")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)

    label("loc_13E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_14D")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)

    label("loc_14D")

    Return()

    # Function_0_108 end

    def Function_1_14E(): pass

    label("Function_1_14E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_160")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_160")

    OP_1B(0x1, 0x0, 0xB)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18D")
    OP_66(0x0, 0x1)

    label("loc_18D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C9")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 30, 0)

    label("loc_1C9")

    Return()

    # Function_1_14E end

    def Function_2_1CA(): pass

    label("Function_2_1CA")

    Call(0, 3)
    Return()

    # Function_2_1CA end

    def Function_3_1CE(): pass

    label("Function_3_1CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA")
    Call(0, 10)
    Return()

    label("loc_1FA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355")

    #C0001
    ChrTalk(
        0x8,
        (
            "服用过那种药物的患者\x01",
            "所需接受的治疗已经基本结束，\x01",
            "但有些人还没交回问诊表。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "首先是住在克洛斯贝尔市\x01",
            "旧城区的少年迪诺。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "然后是彩虹剧团\x01",
            "的演员尼克鲁。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "还有在贝尔加德门执勤的\x01",
            "克洛斯贝尔警备队队员库雷斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "请向他们说明情况，\x01",
            "并将问诊表收回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "全部收齐之后，\x01",
            "再回我这里报告吧。\x01",
            "那么，事情就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_41D")

    label("loc_355")


    #C0007
    ChrTalk(
        0x8,
        (
            "住在克洛斯贝尔市\x01",
            "旧城区的少年迪诺。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "彩虹剧团的\x01",
            "演员尼克鲁。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "还有在贝尔加德门执勤的\x01",
            "克洛斯贝尔警备队队员库雷斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "请向他们说明情况，\x01",
            "并将问诊表收回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "那么，事情就拜托你们了。\x02",
    )

    CloseMessageWindow()

    label("loc_41D")

    TalkEnd(0x8)
    Return()

    # Function_3_1CE end

    def Function_4_421(): pass

    label("Function_4_421")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x8, 59520, 0, 59900, 0)
    OP_68(57330, 1000, 58820, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 57250, 0, 59010, 90)
    SetChrPos(0x102, 56500, 0, 57980, 90)
    SetChrPos(0x109, 56600, 0, 59920, 135)
    SetChrPos(0x105, 54680, 0, 57620, 90)
    SetChrPos(0x104, 55270, 0, 59030, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0012
    ChrTalk(
        0x101,
        (
            "#6P#00000F抱歉，打扰了，\x01",
            "我们是特别任务支援科的成员……\x02",
        )
    )

    CloseMessageWindow()

    #N0013
    NpcTalk(
        0x8,
        "女性的声音",
        "进来吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x8, 110690, 150, 57000, 270)
    SetChrSubChip(0x8, 0x1)
    OP_68(100830, 1250, 48810, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 98390, 0, 49590, 90)
    SetChrPos(0x102, 98390, 0, 49590, 90)
    SetChrPos(0x104, 98390, 0, 49590, 90)
    SetChrPos(0x109, 98390, 0, 49590, 90)
    SetChrPos(0x105, 98390, 0, 49590, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 5)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 6)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 7)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 8)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 9)
    OP_68(105790, 1250, 52080, 3000)
    MoveCamera(62, 24, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(19000, 3000)
    OP_6F(0x79)

    #N0014
    NpcTalk(
        0x8,
        "女医生",
        "嗯，你们总算来了。\x02",
    )

    CloseMessageWindow()

    #N0015
    NpcTalk(
        0x8,
        "女医生",
        (
            "比我预想的时间\x01",
            "晚了大约两分钟……\x01",
            "不过，也还算是优秀吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0016
    ChrTalk(
        0x104,
        (
            "#12P#00306F（总、总觉得有点可怕啊……\x01",
            "　虽然确实是位美女。）\x02",
        )
    )

    CloseMessageWindow()

    #N0017
    NpcTalk(
        0x8,
        "女医生",
        (
            "好了，你们先过来吧。\x01",
            "隔这么远，不方便说话啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#12P#00000F是、是的。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    OP_68(108640, 950, 57250, 5000)
    MoveCamera(45, 28, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(20000, 5000)

    def lambda_81C():
        OP_95(0xFE, 107920, 0, 57770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81C)
    Sleep(500)

    def lambda_839():
        OP_95(0xFE, 107840, 0, 56600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_839)
    Sleep(500)

    def lambda_856():
        OP_95(0xFE, 106710, 0, 58390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_856)
    Sleep(700)

    def lambda_873():
        OP_95(0xFE, 106120, 0, 57330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_873)
    Sleep(500)

    def lambda_890():
        OP_95(0xFE, 106680, 0, 56190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_890)
    WaitChrThread(0x101, 1)

    def lambda_8AE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8AE)
    WaitChrThread(0x102, 1)

    def lambda_8BF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8BF)
    WaitChrThread(0x109, 1)

    def lambda_8D0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8D0)
    WaitChrThread(0x104, 1)

    def lambda_8E1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8E1)
    WaitChrThread(0x105, 1)

    def lambda_8F2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8F2)
    OP_6F(0x79)
    OP_0D()

    #C0019
    ChrTalk(
        0x102,
        (
            "#6P#00100F那个……您就是\x01",
            "赛兰德教授吧？\x02\x03",

            "#00103F听说您已经分析出了\x01",
            "『真知』的成分……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#11P不好意思，在此之前，\x01",
            "我有件事情想要拜托你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#11P希望你们先把\x01",
            "这件事解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x105,
        (
            "#6P#10303F就是向我们提出的那件委托吧？\x02\x03",

            "#10301F不能先把『真知』的\x01",
            "分析结果告诉\x01",
            "我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#11P此事与分析结果存在一定关联，\x01",
            "所以我希望你们优先处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#11P而且，这件事情和那些\x01",
            "『真知』的受害者也有一定关系。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0025
    ChrTalk(
        0x109,
        "#6P#10105F原来如此，是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#6P#00003F……我明白了，\x01",
            "我们会尽快处理这件事的。\x02\x03",

            "#00000F可以告诉我们委托的内容吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#11P嗯，我想要拜托你们\x01",
            "的事情是『回收问诊表』。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#11P……教团事件结束之后，\x01",
            "医院在『真知』受害者的疗后调养\x01",
            "方面倾注了相当多的精力。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#11P对患者们的治疗工作\x01",
            "已经基本结束……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#11P最后请他们填了一份问诊表，\x01",
            "但有几名患者至今还没有交回。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#6P#00003F这样啊……\x01",
            "这确实关系到了\x01",
            "分析结果呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "#11P嗯，所以希望你们迅速完成这项工作。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#11P……没有交回问诊表的\x01",
            "患者共有三名。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "#11P首先是住在克洛斯贝尔市\x01",
            "旧城区的少年迪诺。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#11P然后是彩虹剧团\x01",
            "的演员尼克鲁。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "#11P还有在贝尔加德门执勤的\x01",
            "克洛斯贝尔警备队队员库雷斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#11P请你们向以上患者说明情况，\x01",
            "并将问诊表收回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        (
            "#6P#00300F哦，都是我们熟悉的名字呢。\x02\x03",

            "#00303F旧城区和彩虹剧团的那两个人很简单，\x01",
            "我们回市里找找，应该马上就能找到。\x02\x03",

            "#00302F至于库雷斯前辈，现在大概在\x01",
            "贝尔加德门的食堂吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#6P#00000F嗯，我们赶快去找他们吧。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        "#11P那么，这件事就拜托你们了。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "#11P回收完毕之后，\x01",
            "就再到这里向我报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#11P那时候，我会向你们详细\x01",
            "说明『真知』的分析结果。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【新教授的委托】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x152, 2)
    OP_29(0x70, 0x1, 0x1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 107500, 0, 57000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_4_421 end

    def Function_5_FD1(): pass

    label("Function_5_FD1")


    def lambda_FD6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FD6)

    def lambda_FE7():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FE7)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 105730, 0, 50340, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_5_FD1 end

    def Function_6_101C(): pass

    label("Function_6_101C")


    def lambda_1021():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1021)

    def lambda_1032():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1032)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 104600, 0, 50890, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_6_101C end

    def Function_7_1067(): pass

    label("Function_7_1067")


    def lambda_106C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_106C)

    def lambda_107D():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_107D)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 105690, 0, 48970, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_7_1067 end

    def Function_8_10B2(): pass

    label("Function_8_10B2")


    def lambda_10B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10B7)

    def lambda_10C8():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10C8)
    WaitChrThread(0x109, 1)
    Sound(107, 0, 100, 0)
    OP_95(0x109, 104810, 0, 49520, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_8_10B2 end

    def Function_9_1103(): pass

    label("Function_9_1103")


    def lambda_1108():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1108)

    def lambda_1119():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1119)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 103660, 0, 49780, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_9_1103 end

    def Function_10_114E(): pass

    label("Function_10_114E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(108640, 950, 57250, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 107920, 0, 57770, 90)
    SetChrPos(0x102, 107840, 0, 56600, 90)
    SetChrPos(0x109, 106120, 0, 57330, 90)
    SetChrPos(0x105, 106680, 0, 56190, 90)
    SetChrPos(0x104, 106710, 0, 58390, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0044
    ChrTalk(
        0x8,
        "#11P……回来了啊。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "#11P比我预想的时间慢了大约五分钟……\x01",
            "不过还算及格吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0046
    ChrTalk(
        0x104,
        "#6P#00306F（果、果然很可怕……）\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#6P#00000F那个……问诊表已经\x01",
            "收回来了……就是这些。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将问诊表交给了赛兰德教授。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x32D, 1)
    SubItemNumber(0x32E, 1)
    SubItemNumber(0x32F, 1)

    #C0049
    ChrTalk(
        0x8,
        "#11P……唔……………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    #C0050
    ChrTalk(
        0x102,
        (
            "#6P#00101F请、请问……\x01",
            "是不是有什么问题呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    Sleep(500)

    #C0051
    ChrTalk(
        0x8,
        "#11P……不，正好相反。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#11P单从问诊表来看，\x01",
            "似乎没有任何后遗症。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#11P如此一来，\x01",
            "所有服用过『真知』的人\x01",
            "都已经顺利结束了治疗。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        "#11P辛苦你们了。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#6P#00002F是、是吗……！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x109,
        "#6P#10109F呵呵，太好了。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x105,
        (
            "#6P#10300F虽然费了不少工夫，\x01",
            "但能帮上您的忙，我深感荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#11P那么，虽然有些仓促，但我现在\x01",
            "就向你们说明『真知』的分析结果吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        "#11P可以稍微占用你们一些时间吗？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    #C0060
    ChrTalk(
        0x101,
        (
            "#6P#00001F啊……\x01",
            "好的，拜托您了！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    OP_68(103000, 1050, 57370, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22900, 0)
    SetChrPos(0x8, 103000, 150, 58690, 180)
    SetChrPos(0x109, 102150, 150, 58690, 180)
    SetChrPos(0x102, 103850, 150, 58690, 180)
    SetChrPos(0x105, 102150, 150, 55850, 0)
    SetChrPos(0x101, 103000, 150, 55880, 0)
    SetChrPos(0x104, 103850, 150, 55890, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0061
    ChrTalk(
        0x8,
        (
            "#5P我们对『真知』做了彻底分析之后，\x01",
            "得到了如下结果……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#5P首先，『真知』具有\x01",
            "强行解除『大脑抑制功能』\x01",
            "的效果。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#12P#00005F大脑抑制功能……\x01",
            "是指什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "#5P据研究，人类这种生物\x01",
            "所能运用的身体能力\x01",
            "还不到自身潜能的一半。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "#5P这是因为大脑为了减轻身体的负担，\x01",
            "无意识地限制了\x01",
            "能够使用的能力。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "#5P如果可以\x01",
            "有意识地解除\x01",
            "这种限制……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#5P从理论上来说，\x01",
            "便可以发挥出\x01",
            "达到个人极限的能力。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x105,
        (
            "#12P#10303F也就是说，『真知』这种药物\x01",
            "并非单纯强化肌肉力量……\x02\x03",

            "#10301F而是强行激发出平时无法\x01",
            "使用的潜在能力？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        "#5P正是如此。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "#5P当然，如果解除了\x01",
            "无意识的限制，\x01",
            "会对身体造成相当大的负担。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#12P#00301F的确，在教团事件结束之后，\x01",
            "警备队的那些家伙\x01",
            "似乎相当疲惫。\x02\x03",

            "#00303F连一根手指\x01",
            "都很难活动……\x02\x03",

            "#00302F不过，在经过充分的\x01",
            "复健训练之后，\x01",
            "他们总算找回感觉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x109,
        "#5P#10104F嗯……确实是呢。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        (
            "#11P#00103F……说起感觉。\x02\x03",

            "#00101F当时有一名受害者，\x01",
            "在服用过『真知』之后，得到了惊人的\x01",
            "运气与直觉，在赌局中连战连胜。\x02\x03",

            "#00108F但与此同时，他的性格与举止\x01",
            "却发生了巨大的改变……\x02\x03",

            "#00101F像这种情况，\x01",
            "也可以解释为是『真知』解除了\x01",
            "大脑的抑制功能所致吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        "#5P嗯，可以这样理解。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "#5P目前已经确认，\x01",
            "这种药物同时具有令五感的\x01",
            "敏锐性飞跃提升的作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "#5P但副作用也很明显，\x01",
            "它会使服用者变得很神经质，\x01",
            "处于情绪不安定的焦躁状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "#5P那名服用者的性格变得狂躁，\x01",
            "恐怕就是由于这个原因。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#12P#00003F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x109,
        (
            "#5P#10100F这样的话，确实可以\x01",
            "将大部分问题都解释清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "#5P单从生物化学的方面来解释，\x01",
            "也只能说明到这种程度了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x101,
        "#12P#00005F咦……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "#5P这种药物所具有的某些效果，\x01",
            "实在无法从科学角度来说明。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "#5P具体来说，就像刚才提到过的\x01",
            "那种招来好运的效果……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "#5P以及你们曾经多次目击过的那种\x01",
            "名为『魔人化』的肉体变异现象。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#11P#00105F……的、的确……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        "#12P#00303F倒把那件事给忘了……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#12P#00003F……引起魔人化的药物\x01",
            "是红色的『真知』……\x02\x03",

            "#00001F它的成分和\x01",
            "蓝色的『真知』是不是有所不同？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        "#5P这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "#5P其实蓝色『真知』和\x01",
            "红色『真知』的成分\x01",
            "并没有任何不同。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        "#5P至少从生物化学的角度来说是这样。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0091
    ChrTalk(
        0x101,
        "#12P#00005F是、是这样吗！？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "#5P是的，颜色的差异只是由于\x01",
            "提炼时的处理工序有所不同。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "#5P主要成分并没有任何区别，\x01",
            "二者的分子构造也几乎相同……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "#5P话虽如此，但按照你们的说法，\x01",
            "红色『真知』却可以引发肉体变异\x01",
            "这种无法解释的现象……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "#5P老实说，最合理的解释就是──\x01",
            "所谓的魔人化只是由于你们\x01",
            "过于恐惧而看到了幻觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0096
    ChrTalk(
        0x104,
        "#12P#00306F不，那绝不是幻觉……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x109,
        (
            "#5P#10108F连我也亲眼目睹了\x01",
            "阿奈斯特秘书的魔人化……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "#5P我明白。\x01",
            "所以，我们的研究至此已是极限。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "#5P仅靠生物化学方面的知识，\x01",
            "恐怕无法解开『真知』这种药物\x01",
            "的全部谜团。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#12P#00003F……原来如此……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x105,
        (
            "#12P#10302F身为最尖端现代医学界的领军人物，\x01",
            "能坦然发表这种意见，还真是令人佩服呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "#5P现代医学并不是万能的，尤其是在\x01",
            "心理、灵魂等领域，还存在很大空白。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#5P『真知』或许还隐含着\x01",
            "某些不为人知的特殊作用，\x01",
            "可以让心灵与肉体产生共鸣。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "#5P恐怕连约亚西姆都没有\x01",
            "掌握『真知』的全貌。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#5P他大概只是以教团流传下来的秘密仪式\x01",
            "为基础，通过反复试验而将其完善，\x01",
            "最终成功实现了量产化而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        (
            "#11P#00101F他本人好像\x01",
            "也承认过这一点……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#12P#00001F嗯，他当时确实说过，\x01",
            "以各地的仪式资料为基础，\x01",
            "经过反复试验之后才将『真知』完成……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        "#5P唔，果然如此啊。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "#5P他虽然有能力，而且也很有热情，\x01",
            "但缺乏过人的灵感与想象力，\x01",
            "并不是那种可以被称之为天才的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        "#5P没想到他竟会走向邪路……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0111
    ChrTalk(
        0x101,
        "#12P#00005F难道……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#12P#00305F您认识\x01",
            "约亚西姆吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "#5P是的，他是我在雷米菲利亚医科大学\x01",
            "读书时的同届校友。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "#5P虽然毕业之后就没再见过面，\x01",
            "但偶尔也会有书信往来，\x01",
            "交流彼此的最新研究成果。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "#5P但是，真没想到他会以那种\x01",
            "方式将医学技术用于恶途，\x01",
            "最终还导致玩火自焚……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#11P#00108F教授……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x109,
        "#5P#10103F……我可以理解您的心情。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        "#5P呼，和你们说了些无谓的事情。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "#5P总之，\x01",
            "我能告诉你们的也只有这些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "#5P你们如果想进一步查明『真知』的真相，\x01",
            "恐怕还需要其它的方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        "#5P这只是我的直觉而已……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "#5P我总觉得『真知』的原料──\x01",
            "『灵智之草』这种植物的特性\x01",
            "是解开谜团的关键所在。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        "#12P#00001F『灵智之草』……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#11P#00103F是我们在教团的终端中\x01",
            "看到过的名字呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        (
            "#12P#00306F但直到最后也没有查明\x01",
            "那到底是怎样的植物，\x01",
            "也不知道它生长在什么地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "#5P嗯，我曾向植物学方面\x01",
            "的学者咨询过，但对方并没有\x01",
            "想到特性相符的植物。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "#5P究竟是仅在教团内部流传的新品种，\x01",
            "还是……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "#5P不管怎么说，从药效来推测，\x01",
            "那种植物可能也具有某些\x01",
            "匪夷所思的特性。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        "#11P#00101F匪夷所思的特性吗……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x105,
        (
            "#12P#10309F呵呵，听起来有种超自然的感觉，\x01",
            "事情似乎越来越有趣了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0131
    ChrTalk(
        0x101,
        (
            "#12P#00003F赛兰德教授，\x01",
            "非常感谢您。\x02\x03",

            "#00000F多亏您的帮助，之前一直都毫无头绪\x01",
            "的问题，如今似乎已经渐渐理清了。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        "#5P是吗，那就好。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "#5P我们对『真知』的调查工作，\x01",
            "至此就要告一段落了……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "#5P不过，如果你们今后查到了什么新线索，\x01",
            "可以随时来找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "#5P虽然我只能从医学角度发表观点，\x01",
            "但应该可以给你们提供一些意见。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_10_114E end

    def Function_11_2ADB(): pass

    label("Function_11_2ADB")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【离开研究楼】\x01",      # 0
            "【放弃】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B3A"),
        (1, "loc_2B53"),
        (SWITCH_DEFAULT, "loc_2B6B"),
    )


    label("loc_2B3A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Jump("loc_2B6B")

    label("loc_2B53")

    SetChrPos(0x0, 100500, 0, 50000, 90)
    EventEnd(0x5)
    Jump("loc_2B6B")

    label("loc_2B6B")

    Return()

    # Function_11_2ADB end

    SaveToFile()

Try(main)
