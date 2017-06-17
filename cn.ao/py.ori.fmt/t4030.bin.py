from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t4030.bin",                # FileName
        "t4030",                    # MapName
        "t4030",                    # Location
        0x0000,                     # MapIndex
        "ed7124",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "t4030",                  # 0
        "莉丝修女",               # 1
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(188, 0)                                        # 0

    ScpFunction((
        "Function_0_BC",           # 00, 0
        "Function_1_CF",           # 01, 1
        "Function_2_E5",           # 02, 2
    ))


    def Function_0_BC(): pass

    label("Function_0_BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_CE")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 2)

    label("loc_CE")

    Return()

    # Function_0_BC end

    def Function_1_CF(): pass

    label("Function_1_CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_E4")

    Return()

    # Function_1_CF end

    def Function_2_E5(): pass

    label("Function_2_E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch14000.itc", 0x1E)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis253.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis254.itp")
    OP_68(-1080, 3200, 2970, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23880, 0)
    SetChrPos(0x101, -1100, 0, 2650, 0)
    SetChrPos(0x102, -200, 0, 2350, 315)
    SetChrPos(0x103, -2400, 0, 2200, 45)
    SetChrPos(0x104, -950, 0, 750, 0)
    SetChrPos(0x109, -1750, 0, 1250, 0)
    SetChrPos(0x105, 200, 0, 1100, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1100, 0, 4000, 270)
    SetChrPos(0x8, -800, 0, 4030, 270)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人在莉丝修女的\x01",
            "引领下来到她的房间……\x02\x03",

            "随即向其说明了\x01",
            "摘取蓝花的经过，以及与\x01",
            "艾拉尔达大主教交涉的过程。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7573", 0)
    OP_68(-1080, 1200, 2970, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0002
    ChrTalk(
        0x8,
        (
            "#04406F#11P原来如此。\x02\x03",

            "#04408F站在大主教的立场来说，\x01",
            "坚持不肯开口也是很正常的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0003
    ChrTalk(
        0x101,
        "#00005F#12P哎……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_851")

    #C0004
    ChrTalk(
        0x104,
        "#00305F#12P修女小姐，你知道些什么吗！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    #C0005
    ChrTalk(
        0x8,
        (
            "#04403F#5P在说明之前，先问一句……\x02\x03",

            "#04402F……艾莉小姐，\x01",
            "你还没有把我的\x01",
            "真实身份告诉大家吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        (
            "#00106F#11P嗯……\x01",
            "我觉得不能擅自把\x01",
            "你的身份透露出去。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "#04404F#5P呵呵……非常感谢。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        "#10105F#12P那个……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        "#00201F#6P你的身份究竟是……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0010
    ChrTalk(
        0x8,
        (
            "#04403F#5P我想大主教已经\x01",
            "隐隐察觉到了……\x02\x03",

            "我隶属于教会内的一个\x01",
            "特殊组织──『星杯骑士团』。\x02\x03",

            "#04400F这个组织从属于\x01",
            "名为封圣省的机关，\x01",
            "主要职责为回收古代遗物。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0011
    ChrTalk(
        0x101,
        "#00011F#12P星杯骑士团……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x109,
        (
            "#10111F#12P不就是在阿尔泰尔据点\x01",
            "出手帮助我们的那位……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#04404F#5P是指凯文·格拉汉姆吧？\x02\x03",

            "#04402F顺便一说，我的级别为『随从骑士』，\x01",
            "职责就是协助他完成任务。\x02\x03",

            "#04406F原本应该由他亲自\x01",
            "来克洛斯贝尔\x01",
            "展开各种调查……\x02\x03",

            "#04400F但碍于大主教，\x01",
            "因此只得派遣我\x01",
            "来这里收集情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00001F#12P原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        "#00102F#11P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00306F#12P呼，看来教会里\x01",
            "也有很多复杂的内幕啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#04403F#5P嗯，让各位见笑了。\x02\x03",

            "#04408F言归正传吧，\x01",
            "各位采摘的花……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)
    Jump("loc_8A3")

    label("loc_851")


    #C0018
    ChrTalk(
        0x104,
        "#00305F#12P莉丝小姐，你知道些什么吗！？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "#04408F#11P嗯，各位采摘的花……\x02",
    )

    CloseMessageWindow()

    label("loc_8A3")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #A0020
    AnonymousTalk(
        0x8,
        (
            "#04403F很可能是某部圣典中\x01",
            "所记载的一种。\x02\x03",

            "#04401F话虽如此，但那并非正式圣典，\x01",
            "而是所谓的『外典』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0021
    AnonymousTalk(
        0x109,
        "#10105F外典……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0022
    AnonymousTalk(
        0x105,
        (
            "#10301F也就是不被认可\x01",
            "的禁书吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0023
    AnonymousTalk(
        0x8,
        (
            "#04403F嗯，即使在教会之中，\x01",
            "也只有特定人员才有权阅览那些书。\x02\x03",

            "#04400F而『骑士团』的成员\x01",
            "便拥有阅览外典的权限。\x02\x03",

            "因为其中往往记载着\x01",
            "很多危险的古代遗物。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0024
    AnonymousTalk(
        0x101,
        "#00005F原来如此……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0025
    ChrTalk(
        0x102,
        (
            "#00101F#11P那么，外典中究竟是\x01",
            "如何描述那种蓝花的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#04403F#11P外典之一《拉达记》\x01",
            "对那种蓝花有过如下描写——\x02\x03",

            "#04408F盛开在七耀脉的正上方，\x01",
            "同时象征吉兆与凶兆的神秘植物……\x02\x03",

            "#04401F其名为『灵智之草』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0027
    ChrTalk(
        0x101,
        "#00007F#4S#12P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        "#00107F#11P那名字是……！\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    #A0029
    AnonymousTalk(
        0x109,
        "#10101F我、我记得是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0030
    AnonymousTalk(
        0x105,
        (
            "#10305F『教团』终端中所记载的植物名称，\x01",
            "似乎是制造『真知』的原材料吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0031
    AnonymousTalk(
        0x103,
        "#00206F………是的…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0032
    AnonymousTalk(
        0x104,
        (
            "#00301F竟然会在这种地方\x01",
            "再次听到它的名字……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0033
    ChrTalk(
        0x8,
        (
            "#04403F#5P……原来如此，是这样啊。\x02\x03",

            "#04401F那个教团留下了很多谜团，\x01",
            "连教会都未能完全解明。\x02\x03",

            "再加上艾拉尔达大主教固执己见，\x01",
            "因此基本没有对约亚西姆·琼塔\x01",
            "引发的那起事件进行调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x109,
        (
            "#10111F#12P请、请稍等一下。\x02\x03",

            "#10106F假如那种花\x01",
            "真的是制造『真知』\x01",
            "的原材料……\x02\x03",

            "#10101F它如今在各地盛开，\x01",
            "究竟有何含义呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#00108F#11P是、是啊……\x01",
            "突然出现的『幻兽』也很让人在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#00203F#6P盛开在七耀脉的正上方……\x02\x03",

            "#00201F同时象征吉兆与凶兆\x01",
            "的神秘植物……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        "#00306F#12P嗯，真是相当吻合呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0038
    ChrTalk(
        0x101,
        (
            "#00003F#11P总之，这似乎不是\x01",
            "单凭我们几个就能解决的问题。\x02\x03",

            "还是先回支援科，\x01",
            "整理出一份详细报告书吧。\x02\x03",

            "#00001F莉丝小姐，\x01",
            "我们能把你提供的这些情报\x01",
            "转达给警备队和协会吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#04403F#5P这个嘛……\x02\x03",

            "#04400F如果可以，请尽量不要\x01",
            "提到我的名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x105,
        (
            "#10302F#12P呵呵，如果让大主教知道了，\x01",
            "肯定会把你当成间谍呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#00100F#11P放心，我们肯定会\x01",
            "极力注意的。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#04404F#5P那就没有问题了。\x02\x03",

            "#04402F我准备联络骑士团，\x01",
            "并展开正式调查。\x02\x03",

            "如果我们今后取得了进展，\x01",
            "可以交换情报吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#00002F#12P嗯，非常愿意。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        "#00202F#6P一起加油吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人返回支援科，\x01",
            "十万火急地整理出了关于幻兽\x01",
            "及蓝花──『灵智之草』的报告书。\x02\x03",

            "通过导力网络，将报告书发送到\x01",
            "警备队的司令部和协会的接待处之后……\x02\x03",

            "整日奔波于各地，早已筋疲力尽的罗伊德等人\x01",
            "与科长、琪雅一起享用了迟来的晚餐，\x01",
            "随后便立刻返回房间休息了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_32(0xFF, 0xFE, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("m0001", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E5 end

    SaveToFile()

Try(main)
