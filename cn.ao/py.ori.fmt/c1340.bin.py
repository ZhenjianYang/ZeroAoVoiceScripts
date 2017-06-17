from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1340.bin",                # FileName
        "c1340",                    # MapName
        "c1340",                    # Location
        0x001D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 53000, 0, 20000, 0, 0, 1, 29, 0, 0, 0, 2],
    )

    BuildStringList((
        "c1340",                  # 0
        "玛丽亚贝尔",             # 1
    ))

    AddCharChip((
        "chr/ch05502.itc",                   # 00
    ))

    DeclNpc(55029,   180,     128820,  180,  389,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)

    DeclActor(47960,   0,       123700,  1200,    47960,   800,     123700,  0x007C, 0,  3,  0x0000)
    DeclActor(53000,   0,       45600,   1200,    53000,   800,     45600,   0x007C, 0,  6,  0x0000)
    DeclActor(55000,   150,     128800,  2500,    55000,   1800,    128800,  0x007E, 0,  4,  0x0000)

    ChipFrameInfo(324, 0)                                        # 0

    ScpFunction((
        "Function_0_144",          # 00, 0
        "Function_1_19E",          # 01, 1
        "Function_2_1A5",          # 02, 2
        "Function_3_1C2",          # 03, 3
        "Function_4_26D",          # 04, 4
        "Function_5_271",          # 05, 5
        "Function_6_37C",          # 06, 6
        "Function_7_1936",         # 07, 7
        "Function_8_253D",         # 08, 8
    ))


    def Function_0_144(): pass

    label("Function_0_144")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15C")
    ClearScenarioFlags(0x25, 1)
    Call(0, 1)

    label("loc_15C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18E")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)

    label("loc_18E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_19D")
    ClearScenarioFlags(0x22, 1)
    Event(0, 7)

    label("loc_19D")

    Return()

    # Function_0_144 end

    def Function_1_19E(): pass

    label("Function_1_19E")

    Sound(160, 0, 100, 0)
    Return()

    # Function_1_19E end

    def Function_2_1A5(): pass

    label("Function_2_1A5")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1")
    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x1, 0x1)

    label("loc_1C1")

    Return()

    # Function_2_1A5 end

    def Function_3_1C2(): pass

    label("Function_3_1C2")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着车辆杂志《导力车爱好者月刊 vol.2》。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('狂野色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_269")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "导力车喷漆式样\x01\x07\x02",

            "『狂野色彩』\x07\x00",
            "已经记下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('狂野色彩', 1)

    label("loc_269")

    TalkEnd(0xFF)
    Return()

    # Function_3_1C2 end

    def Function_4_26D(): pass

    label("Function_4_26D")

    Call(0, 5)
    Return()

    # Function_4_26D end

    def Function_5_271(): pass

    label("Function_5_271")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B")

    #C0003
    ChrTalk(
        0x8,
        (
            "#02901F那个可恨的怪盗Ｂ一共\x01",
            "偷走了五个罗赞贝尔克人偶。\x02\x03",

            "#02903F竟敢把我最心爱的\x01",
            "孩子们拐走……\x01",
            "绝对不能原谅。\x02\x03",

            "#02900F各位，一切都\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_378")

    label("loc_31B")


    #C0004
    ChrTalk(
        0x8,
        (
            "#02903F竟敢把我最心爱的\x01",
            "孩子们拐走……\x01",
            "绝对不能原谅。\x02\x03",

            "#02901F各位，一切都\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_378")

    TalkEnd(0x8)
    Return()

    # Function_5_271 end

    def Function_6_37C(): pass

    label("Function_6_37C")

    EventBegin(0x0)
    Fade(1000)
    OP_68(53250, 1500, 45110, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18430, 0)
    SetChrPos(0x102, 52950, 0, 44240, 0)
    SetChrPos(0x101, 52220, 0, 43070, 0)
    SetChrPos(0x104, 53710, 0, 43070, 0)
    SetChrPos(0x109, 51640, 0, 42010, 0)
    SetChrPos(0x103, 52930, 0, 42010, 0)
    SetChrPos(0x105, 54450, 0, 42010, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    OP_9B(0x0, 0x102, 0x0, 0x3E8, 0x5DC, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(500)

    #C0005
    ChrTalk(
        0x102,
        "#12P#00100F──贝尔，是我。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("玛丽亚贝尔的声音")

    #A0006
    AnonymousTalk(
        0xFF,
        "嗯，请进吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0007
    ChrTalk(
        0x102,
        "#12P#00100F打扰啦。\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    Sleep(300)

    def lambda_4DA():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4DA)
    Sleep(100)

    def lambda_4F7():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F7)

    def lambda_511():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_511)

    def lambda_52B():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_52B)

    def lambda_545():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_545)

    def lambda_55F():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_55F)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_68(54290, 1230, 126800, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    SetChrPos(0x101, 54960, 30, 125480, 0)
    SetChrPos(0x102, 53750, 30, 125480, 0)
    SetChrPos(0x104, 56190, 30, 125480, 0)
    SetChrPos(0x109, 54960, 30, 124330, 0)
    SetChrPos(0x103, 53750, 30, 124330, 0)
    SetChrPos(0x105, 56190, 30, 124330, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    SetMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x0, 0x0, 0x0)
    OP_65(0x1, 0x1)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x105, 0x0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0008
    ChrTalk(
        0x102,
        "#12P#00102F呵呵，好久不见了，贝尔。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#5P#02904F艾莉……\x01",
            "还有特别任务支援科的诸位，\x01",
            "真是好久不见了。\x02\x03",

            "#02900F听说缇欧\x01",
            "昨晚刚刚回来，\x01",
            "最近还好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        "#12P#00200F是的，托你的福。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#5P#02909F呵呵，那就好。\x02\x03",

            "#02900F今天是正式会议的召开日，\x01",
            "自然会非常繁忙，\x01",
            "请大家多多加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x109,
        "#12P#10109F呵呵，谢谢了。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x105,
        (
            "#12P#10300F对了，玛丽亚贝尔小姐\x01",
            "今天你不去兰花塔\x01",
            "露个面吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#5P#02900F嗯，我身为\x01",
            "父亲的代理人，\x01",
            "还要处理银行的工作……\x02\x03",

            "通商会议那边的事情\x01",
            "就全部交给父亲了。\x02\x03",

            "#02906F说起来……这次真是不得\x01",
            "不向各位致歉呢。\x02\x03",

            "在如此繁忙的时期，我却为了\x01",
            "这种事情突然把你们叫过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#12P#00000F哪里的话……\x01",
            "玛丽亚贝尔小姐平时总是关照我们，\x01",
            "我们很愿意接受你的委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00303F听说你的古董人偶\x01",
            "被盗走了……\x02\x03",

            "#00301F可以把事情的详情告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#5P#02903F……好的。\x02\x03",

            "#02900F我想大家应该都知道，\x01",
            "我非常喜爱罗赞贝尔克\x01",
            "工房制作的人偶……\x02\x03",

            "#02900F在我位于ＩＢＣ的私人房间中，\x01",
            "存放着五个\x01",
            "我最心爱的人偶。\x02\x03",

            "#02903F但就在昨晚，有人趁我出去办事，\x01",
            "房间中空无一人的时候，\x01",
            "将五个人偶全部偷走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        (
            "#12P#00205F五个罗赞贝尔克工房\x01",
            "制造的古董人偶……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x109,
        (
            "#12P#10105F价、价值应该\x01",
            "相当高昂呢。\x02\x03",

            "#10106F如果是大号人偶，\x01",
            "恐怕最少值数百万米拉……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#5P#02903F钱倒不是什么大问题。\x02\x03",

            "最重要的是，原本应该有那些孩子的地方，\x01",
            "如今变得空荡荡的那种失落感……\x02\x03",

            "#02910F啊啊，我真想亲手把那个\x01",
            "可恨的毛贼大卸八块！！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#12P#00006F请、请冷静一点。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#12P#00105F贝尔的私室……\x01",
            "就是这间办公室旁边的房间吧？\x02\x03",

            "#00103F犯人竟能穿越ＩＢＣ的\x01",
            "安全系统，侵入你的房间，\x01",
            "究竟是如何做到的……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#5P#02903F……咳咳。\x01",
            "嗯，其实我本来也觉得\x01",
            "很不可思议……\x02\x03",

            "#02901F但看到遗留在现场的物品之后，\x01",
            "马上就可以理解了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        "#12P#00205F遗留在现场的物品……？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "#5P#02901F还是请你们\x01",
            "亲眼看看吧。\x01",
            "……就是这个。\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FE9")

    #A0026
    AnonymousTalk(
        0x101,
        "#00011F这、这是……！\x02",
    )

    CloseMessageWindow()

    #A0027
    AnonymousTalk(
        0x102,
        "#00105F『怪盗Ｂ』的犯罪卡片……！？\x02",
    )

    CloseMessageWindow()

    #A0028
    AnonymousTalk(
        0x8,
        (
            "#02901F神出鬼没的怪人，曾在大陆各地\x01",
            "盗取过无数美术品的传奇大盗──\x01",
            "人称『怪盗Ｂ』。\x02\x03",

            "#02903F听说他会使用多种不可思议的奇术，\x01",
            "轻而易举地将目标完美盗走，\x01",
            "作案之后必定会在犯罪现场留下一张卡片……\x02\x03",

            "#02901F对他来说，潜入ＩＢＣ\x01",
            "恐怕也是易如反掌吧。\x02\x03",

            "#02902F另外，听说各位曾经\x01",
            "解决过同其相关的案件？\x02",
        )
    )

    CloseMessageWindow()

    #A0029
    AnonymousTalk(
        0x109,
        "#10105F还、还有这种事吗！？\x02",
    )

    CloseMessageWindow()

    #A0030
    AnonymousTalk(
        0x103,
        (
            "#00200F嗯，记得他以前还盗窃过\x01",
            "原市政厅中的雕像呢。\x02\x03",

            "#00203F但我们最后也没能将他逮捕……\x02",
        )
    )

    CloseMessageWindow()

    #A0031
    AnonymousTalk(
        0x104,
        (
            "#00310F啧，没想到他竟然\x01",
            "再次来到克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #A0032
    AnonymousTalk(
        0x105,
        (
            "#10304F呵呵，你们似乎也经历过\x01",
            "各种各样的事件呢。\x02\x03",

            "#10305F那么……卡片上\x01",
            "写着什么吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1252")

    label("loc_FE9")


    #A0033
    AnonymousTalk(
        0x101,
        "#00011F这是……！\x02",
    )

    CloseMessageWindow()

    #A0034
    AnonymousTalk(
        0x102,
        (
            "#00101F莫非是……\x01",
            "『怪盗Ｂ』的犯罪卡片……！？\x02",
        )
    )

    CloseMessageWindow()

    #A0035
    AnonymousTalk(
        0x109,
        (
            "#10105F怪盗Ｂ……？\x01",
            "好像曾在什么地方听到过这个名字。\x02",
        )
    )

    CloseMessageWindow()

    #A0036
    AnonymousTalk(
        0x8,
        (
            "#02900F艾莉和罗伊德警官\x01",
            "应该听说过他的名字吧。\x02\x03",

            "#02901F神出鬼没的怪人，曾在大陆各地\x01",
            "盗取过无数美术品的传奇大盗──\x01",
            "人称『怪盗Ｂ』。\x02\x03",

            "#02903F听说他会使用多种不可思议的奇术，\x01",
            "轻而易举地将目标完美盗走，\x01",
            "作案之后必定会在犯罪现场留下一张卡片……\x02\x03",

            "#02901F在他的活动中心──帝国，\x01",
            "他的名字可以说是无人不知。\x02\x03",

            "#02906F对他来说，潜入ＩＢＣ\x01",
            "恐怕也是易如反掌吧。\x02",
        )
    )

    CloseMessageWindow()

    #A0037
    AnonymousTalk(
        0x103,
        (
            "#00200F我也听说过\x01",
            "这个名字呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0038
    AnonymousTalk(
        0x104,
        (
            "#00301F啧，没想到那家伙竟然\x01",
            "来到克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #A0039
    AnonymousTalk(
        0x105,
        (
            "#10305F那么……\x01",
            "卡片上写着什么吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1252")


    #A0040
    AnonymousTalk(
        0x8,
        "#02903F……内容是这些。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "致特别任务支援科的诸位年轻人。\x01",
            "深受大小姐宠爱的五名幼女\x01",
            "如今都在我的手中。\x02\x03",

            "如希望她们重获自由，\x01",
            "就请使用名为真实的钥匙，\x01",
            "将幽禁她们的五处牢笼开启吧。\x02\x03",

            "第一个牢笼在市内。\x01",
            "请寻找『见缝插针的\x01",
            "指挥官所坐的椅子』。\x01",
            "  　　　　　　　　──怪盗Ｂ\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0042
    ChrTalk(
        0x8,
        (
            "#5P#02901F……你们明白了吧？\x01",
            "这就是我把各位\x01",
            "叫来的最大理由。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#12P#00001F怪盗Ｂ向我们特别任务支援科\x01",
            "发出了挑战书……\x02\x03",

            "就是这么一回事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x105,
        (
            "#12P#10306F难道他为此\x01",
            "才特意盗窃\x01",
            "五个人偶吗？\x02\x03",

            "#10302F呵呵，真是个\x01",
            "相当奇怪的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        (
            "#00301F不管怎么说……\x01",
            "既然已经出现了受害者，\x01",
            "我们便不能坐视不管。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#12P#00103F是啊……\x01",
            "而且被盗走的东西可是贝尔\x01",
            "最珍爱的罗赞贝尔克人偶。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#5P#02902F呵呵，谢谢了，艾莉。\x01",
            "一切都靠你们啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#12P#00000F那么，在调查开始之前，\x01",
            "我们再来分析一下\x01",
            "卡片上的文字吧。\x02\x03",

            "#00003F首先是『五名幼女』……\x02\x03",

            "这应该是指\x01",
            "被盗走的五个人偶。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        (
            "#12P#00203F那么，『五处牢笼』……\x02\x03",

            "#00200F恐怕表示\x01",
            "人偶被分别藏在了\x01",
            "五个场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x109,
        (
            "#12P#10105F也就是说，\x01",
            "我们必须要去\x01",
            "五个地方寻找吗……\x02\x03",

            "#10106F呜呜，好像很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x105,
        (
            "#12P#10302F接下来，最重要的内容\x01",
            "恐怕就是『市内』和『见缝插针的\x01",
            "指挥官所坐的椅子』这两处文字了。\x02\x03",

            "#10304F这应该是提示人偶\x01",
            "所在之处的线索……\x01",
            "唔，究竟在比喻什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#00303F『见缝插针』……\x01",
            "最近好像在什么地方\x01",
            "听到过这句话呢……\x02\x03",

            "#00300F总之，在这里苦想也无济于事，\x01",
            "我们赶快开始调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#5P#02904F呵呵，我很期待你们的表现哦，\x01",
            "特别任务支援科的各位。\x02\x03",

            "#02900F请一定要把我最珍爱的\x01",
            "孩子们平安接回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        "#12P#00000F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        (
            "#12P#00104F我先把卡片上的内容\x01",
            "记录到调查手册里。\x02\x03",

            "#00100F接下来就以此为线索，开始调查吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找消失的收藏品】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 54990, 30, 124960, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x7A, 0x1, 0x1)
    SetScenarioFlags(0x1C6, 3)
    EventEnd(0x5)
    Return()

    # Function_6_37C end

    def Function_7_1936(): pass

    label("Function_7_1936")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(54970, 1230, 123580, 0)
    MoveCamera(46, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    SetChrPos(0x101, 54960, 30, 123480, 0)
    SetChrPos(0x102, 53750, 30, 123480, 0)
    SetChrPos(0x104, 56190, 30, 123480, 0)
    SetChrPos(0x109, 54960, 30, 122330, 0)
    SetChrPos(0x103, 53750, 30, 122330, 0)
    SetChrPos(0x105, 56190, 30, 122330, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    SetChrChipByIndex(0x8, 0x1E)
    ClearChrBattleFlags(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 54960, 30, 125480, 180)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0057
    ChrTalk(
        0x8,
        (
            "#02903F我已经了解事情的大致情况了。\x02\x03",

            "#02901F没想到怪盗Ｂ是『结社』的成员，\x01",
            "真是让我吃了一惊……\x02\x03",

            "#02906F既然如此，那也就没办法啦。\x02\x03",

            "#02910F但以后要是把他抓到，\x01",
            "我一定会让他后悔\x01",
            "出生到这个世界上。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0058
    ChrTalk(
        0x104,
        "#00306F（好、好可怕的发言……）\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#12P#00006F对、对不起，\x01",
            "我们也很想抓住他的……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#12P#00100F总之，先把找回来的人偶\x01",
            "还给贝尔吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(500)
    SetChrName("")

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把五个装有罗赞贝尔克人偶的\x01",
            "箱子交给了贝尔。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x7D0, 0x0)

    #C0062
    ChrTalk(
        0x8,
        (
            "#02909F呵呵，你们终于回来了。\x01",
            "爱丽丝、卡楠、莉埃缇、\x01",
            "米丝蒂尔、夏伦……\x02\x03",

            "#02904F……算啦，这样就好，\x01",
            "我就不抱怨什么了。\x02\x03",

            "#02900F反正我这些可爱的\x01",
            "罗赞贝尔克人偶\x01",
            "已经毫发无伤地回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        (
            "#10304F嗯，怪盗在这方面\x01",
            "似乎也相当用心呢。\x02\x03",

            "#10300F他把人偶装在了十分坚固的箱子里，\x01",
            "而且并没有把任何一个箱子\x01",
            "放在会有危险的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        "#12P#10105F啊，如此说来，还真是这样呢。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#12P#00206F话虽如此，但他当初要是没把人偶偷走，\x01",
            "不就什么事都没有了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#12P#00009F哈哈，说的没错呢。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#02903F总之，今后我会彻底\x01",
            "加强安保力度，\x01",
            "避免这样的事情再度发生。\x02\x03",

            "#02900F必须要让保安部门\x01",
            "比以往更加用心地工作才行。\x02\x03",

            "#02909F呵呵，这次真是\x01",
            "多亏你们帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#12P#00109F不用客气啦，贝尔，\x01",
            "遇到困难的时候就应该互相帮助。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2356")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0069
    ChrTalk(
        0x101,
        "#12P#00005F（对了，上次曾经……）\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 54960, 30, 124080, 2000, 0x0)

    #C0070
    ChrTalk(
        0x101,
        "#12P#00001F（盯视……）\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x109,
        "#12P#10105F罗、罗伊德警官？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "#02905F……你要干什么？\x01",
            "为什么突然瞪着我？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#12P#00003F没、没什么。\x02\x03",

            "#00001F在以前那起事件刚刚解决的时候，\x01",
            "怪盗Ｂ曾易容成委托人的样子，\x01",
            "出现在我们的面前……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#00305F哦哦，说起来，\x01",
            "确实发生过那种事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        "#12P#00205F哎，可是这次……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#12P#00003F……所以，我就开门见山地直接问了。\x02\x03",

            "#00001F你真的是玛丽亚贝尔小姐──\x02",
        )
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)

    def lambda_2121():
        OP_99(0xFE, 0x101, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2121)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_214E():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_214E)

    def lambda_2167():
        OP_98(0xFE, 0x0, 0xC8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2167)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    #C0077
    ChrTalk(
        0x101,
        "#12P#00011F呜啊……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0078
    ChrTalk(
        0x8,
        (
            "#02902F呵呵呵，罗伊德警官可真是的。\x02\x03",

            "#02909F人家如此诚恳地向你道谢，\x01",
            "你却说出这样的话，\x01",
            "难道不觉得很失礼吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0079
    ChrTalk(
        0x101,
        (
            "#12P#00011F对、对不起……唔啊……！\x02\x03",

            "#00006F（没、没错，确实是\x01",
            "  玛丽亚贝尔小姐呢……呜。）\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        "#12P#00106F罗伊德，你可真是的……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        "#10309F哎呀呀，被抓住不放呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_244F")

    label("loc_2356")


    #C0082
    ChrTalk(
        0x101,
        (
            "#12P#00000F那么，我们这就\x01",
            "告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "#02909F呵呵，今天真是\x01",
            "谢谢各位了。\x02\x03",

            "#02900F听说你们也会以\x01",
            "警卫人员的身份\x01",
            "参加今天的通商会议吧？\x02\x03",

            "#02904F请大家在我父亲的\x01",
            "背后尽力协助他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#12P#00000F嗯，放心吧。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#12P#00100F那我们走啦，贝尔。\x02",
    )

    CloseMessageWindow()

    label("loc_244F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_2466")
    Call(0, 8)

    label("loc_2466")


    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人\x01",
            "退还了在一层接待处\x01",
            "领取的ＩＢＣ认证卡片。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找消失的收藏品】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7A, 0x1, 0x6)
    OP_29(0x7A, 0x1, 0x7)
    OP_29(0x7A, 0x4, 0x10)
    SubItemNumber('ＩＢＣ认证卡片', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｃ', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｒ', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｍ', 1)
    SubItemNumber('罗赞贝尔克人偶·Ｓ', 1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("c1310", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1936 end

    def Function_8_253D(): pass

    label("Function_8_253D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    OP_68(54590, 1500, 13640, 0)
    MoveCamera(55, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20420, 0)
    SetChrPos(0x101, 53930, 0, 14020, 90)
    SetChrPos(0x102, 53440, 0, 15190, 90)
    SetChrPos(0x104, 53440, 0, 12670, 90)
    SetChrPos(0x109, 52520, 0, 13810, 90)
    SetChrPos(0x103, 52020, 0, 15160, 90)
    SetChrPos(0x105, 52020, 0, 12580, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0xA, 0x1, 0x8)
    Sleep(1000)

    def lambda_2608():
        OP_95(0xFE, 56930, 0, 14020, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2608)

    def lambda_2622():
        OP_95(0xFE, 56440, 0, 15190, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2622)

    def lambda_263C():
        OP_95(0xFE, 56440, 0, 12670, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_263C)

    def lambda_2656():
        OP_95(0xFE, 55520, 0, 13810, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2656)

    def lambda_2670():
        OP_95(0xFE, 55020, 0, 15160, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2670)

    def lambda_268A():
        OP_95(0xFE, 55020, 0, 12580, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_268A)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x105, 0x1)
    LoadChrToIndex("apl/ch51274.itc", 0x1F)
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(55700, 1400, 130699, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x8, 56030, 0, 130930, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    Sound(802, 0, 100, 0)
    Sleep(500)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x1, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0088
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02904F喂？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    Sleep(500)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("声音")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──呀，美丽的玛丽亚贝尔小姐，\x01",
            "你的心情还好吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0090
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02912F好的不得了哦。\x02\x03",

            "#02913F你的『余兴节目』\x01",
            "也让我十分享受。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("声音")

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，那就好。\x02\x03",

            "感谢你把珍爱的\x01",
            "收藏品借给我。\x02\x03",

            "我虽然认识大师，\x01",
            "但同时欣赏这么多作品的机会，\x01",
            "之前真是连一次都没有过呢。\x02\x03",

            "这简直是美的极致──\x01",
            "请容我再次表达谢意。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0092
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02909F呵呵呵……你似乎\x01",
            "保管得相当细致用心，\x01",
            "真是让我松了一口气。\x02\x03",

            "#02911F要是你在它们身上留下了\x01",
            "哪怕只有一处的损伤，我都会招待\x01",
            "你去我的『城堡』里好好享受一番。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("声音")

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈哈哈……\x01",
            "错失良机，还真是遗憾呢。\x02\x03",

            "嗯，说起来，也要感谢迅速将它们\x01",
            "找回的诸位支援科成员啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0094
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02913F呵呵……\x01",
            "你接下来\x01",
            "有什么安排？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("声音")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，我马上就要动身\x01",
            "离开克洛斯贝尔了。\x02\x03",

            "帝国即将发生\x01",
            "很有趣的事情，\x01",
            "我准备去那里看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0096
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02912F是吗……\x01",
            "那可真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("声音")

    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "到了帝国之后，\x01",
            "我也会继续关注\x01",
            "你们的『计划』。\x02\x03",

            "呵呵，自然也会关注你这位\x01",
            "『结社』新成员的动向哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0098
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02902F呵呵……我还没有决定\x01",
            "是否要加入呢。\x02\x03",

            "#02913F那么，我们就在\x01",
            "不久之后再见吧──\x02",

            "#02911F『怪盗绅士』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("怪盗布卢布兰")

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈哈，我期待着\x01",
            "那一天的到来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Return()

    # Function_8_253D end

    SaveToFile()

Try(main)
