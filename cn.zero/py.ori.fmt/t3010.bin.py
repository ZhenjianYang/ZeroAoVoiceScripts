from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t3010.bin",                # FileName
        "t3010",                    # MapName
        "t3010",                    # Location
        0x005B,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "t3010",                  # 0
        "玲",                     # 1
        "约鲁古老人",             # 2
        "帕蒂尔·玛蒂尔",         # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_F8",           # 00, 0
        "Function_1_108",          # 01, 1
        "Function_2_109",          # 02, 2
        "Function_3_1021",         # 03, 3
    ))


    def Function_0_F8(): pass

    label("Function_0_F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_107")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)

    label("loc_107")

    Return()

    # Function_0_F8 end

    def Function_1_108(): pass

    label("Function_1_108")

    Return()

    # Function_1_108 end

    def Function_2_109(): pass

    label("Function_2_109")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09500.itc", 0x1E)
    LoadChrToIndex("chr/ch06600.itc", 0x1F)
    LoadChrToIndex("apl/ch50500.itc", 0x20)
    LoadChrToIndex("chr/ch09502.itc", 0x21)
    LoadEffect(0x0, "event\\ev622_00.eff")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis162.itp")
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -5800, 200, 6000, 0)
    SetChrFlags(0x8, 0x8000)
    BeginChrThread(0x8, 0, 0, 3)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, 0, 7100, 180)
    SetChrFlags(0x9, 0x8000)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_78(0x1, 0xA)
    OP_49()
    OP_74(0x1, 0xF)
    OP_70(0x1, 0x65)
    SetChrPos(0xA, 8930, 750, -140, 270)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03900.itp")
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K同日，１４：４０──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    Sound(850, 0, 90, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("少女的声音")

    #A0002
    AnonymousTalk(
        0xFF,
        "──呵呵，原来如此。\x02",
    )

    CloseMessageWindow()

    #A0003
    AnonymousTalk(
        0xFF,
        (
            "看来哥哥们\x01",
            "终于到达那里了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7304", 0)
    FadeToBright(1000, 0)
    OP_68(-960, 2500, 1000, 0)
    MoveCamera(30, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21390, 0)
    OP_68(-5320, 2500, 3850, 8000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-7120, 1700, 5020, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    SetCameraDistance(12000, 2500)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    #C0004
    ChrTalk(
        0x8,
        (
            "#3302F#11P出席者已经到齐了，\x01",
            "邀请函也已经送出……\x02\x03",

            "这样一来，晚宴的准备工作\x01",
            "便全部完成了吧？\x02\x03",

            "#3304F先找到『鬼』的，\x01",
            "是艾丝蒂尔他们？还是哥哥他们呢？\x02\x03",

            "#3308F亦或是──\x02",
        )
    )

    CloseMessageWindow()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    Sleep(250)

    #N0005
    NpcTalk(
        0x9,
        "老人的声音",
        (
            "#4P……你好像依然\x01",
            "可以看透一切呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-6020, 1700, 4270, 4000)
    MoveCamera(46, 15, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(14300, 4000)

    def lambda_4E7():
        OP_9B(0x0, 0xFE, 0x0, 0x708, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4E7)

    def lambda_4FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4FC)
    Sleep(500)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)

    def lambda_533():
        OP_95(0xFE, -4200, 0, 5300, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_533)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    Sleep(300)

    #C0006
    ChrTalk(
        0x8,
        (
            "#3309F#5P呵呵，玲才没有\x01",
            "自信过剩到那种程度呢。\x02\x03",

            "#3300F玲所看清的，只不过是\x01",
            "纠缠在一起的因果报应而已。\x02\x03",

            "各自的行动所招致的后果，\x01",
            "会在克洛斯贝尔这片土地上\x01",
            "交织出怎样的命运呢……\x02\x03",

            "#3304F我能看到的，只不过是这个罢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0007
    AnonymousTalk(
        0x9,
        (
            "嗯……原来如此。\x02\x03",

            "黑手党与那个教团\x01",
            "有何企图，目前还不得而知，\x01",
            "看样子，似乎会稍微发生一些骚乱呢。\x02\x03",

            "不过，这也是他们自作自受──\x01",
            "不，该说是因果报应吗。\x02",
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

    #C0008
    ChrTalk(
        0x8,
        (
            "#3306F#5P是啊，在这座灰色的城市，\x01",
            "将其称之为不断累积的因果报应，\x01",
            "或许也并不为过。\x02\x03",

            "#3300F──其实我之前还一度认为\x01",
            "和『结社』有关呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "#3903F#11P这片土地毕竟是\x01",
            "『结社』和『教会』之间的缓冲地带。\x02\x03",

            "法王禁止骑士活动，\x01",
            "盟主也不派遣执行者。\x02\x03",

            "#3900F哼，不过，终究也只是表面上的承诺而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "#3309F#5P呵呵呵，但爷爷的工房却坐落于此，\x01",
            "实在是有些古怪呢……\x02\x03",

            "#3302F没想到，还装设了能够\x01",
            "干涉克洛斯贝尔导力网络\x01",
            "的远程操控系统啊。\x02\x03",

            "多亏有这个东西，\x01",
            "玲才不会感到无聊。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "#3903F#11P只要能帮得上你，\x01",
            "准备这些东西就是值得的。\x02\x03",

            "#3901F那家伙将这些东西推给我时，\x01",
            "本以为已经接近报废了……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "#3302F#5P呵呵……\x01",
            "你和『博士』的关系依然很不好啊。\x02\x03",

            "#3304F『十三工房』的管理者，\x01",
            "使徒第六柱──诺华提斯博士。\x02\x03",

            "#3300F明明已经有了『星辰』网络，\x01",
            "但好像却依然对爱普斯泰恩的网络试验\x01",
            "有着浓厚兴趣，这是为什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "#3901F#11P哼，那家伙就是这样。\x02\x03",

            "大概是为了自己的某种危险企图，\x01",
            "而想要利用那个网络吧。\x02\x03",

            "#3903F真受不了，竟然随意散播\x01",
            "还在开发过程中的试验品……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#3304F#5P呵呵，是指和哥哥们战斗过的\x01",
            "那台红色武者吗？\x02\x03",

            "#3300F从监控记录上看来，\x01",
            "性能还是很优秀的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        (
            "#3903F#11P自我调节、状况判断和\x01",
            "灵活选择行动等方面始终是个难点。\x02\x03",

            "#3900F跟你的『伙伴』比起来，\x01",
            "还有相当的差距呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#3304F#5P呵呵……\x02\x03",

            "#3305F不过，玲在这里的事情，\x01",
            "博士应该也已经发觉了吧？\x02\x03",

            "先不说玲，关于『他』，\x01",
            "博士难道没有任何表示吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "#3903F#11P目前是无动于衷。\x02\x03",

            "看样子，他正在埋头\x01",
            "开发新机体呢……\x02\x03",

            "#3900F──对了，作为课题的姿势控制与\x01",
            "关节部分的强化改造已经完成了。\x02\x03",

            "我不会让那个家伙\x01",
            "挑出任何毛病。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#3304F#5P呵呵，谢谢了。\x02\x03",

            "#3308F这样一来……\x01",
            "终于可以开始最后的赌局了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        "#3900F#11P……嗯………\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    Fade(250)
    EndChrThread(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x8, 0x11)
    Sleep(300)

    #C0020
    ChrTalk(
        0x8,
        (
            "#3300F#5P呵呵，别露出那副表情嘛。\x02\x03",

            "爷爷教会我操控人偶的技术，\x01",
            "又为我制造了那两个傀儡人偶，\x01",
            "而且还给我提供藏身之处……\x02\x03",

            "#3304F我十分感谢爷爷哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "#3903F#11P哪里，这不算什么。\x02\x03",

            "#3900F说起来──\x01",
            "今天会变得很忙吧？\x02\x03",

            "虽然时间尚早……\x01",
            "不过，就让我们开始今天的下午茶吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "#3309F#5P呵呵，好啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x12C)
    Sleep(100)
    Fade(1000)
    OP_68(4730, 4900, -140, 7000)
    MoveCamera(69, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13000, 7000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)

    #C0023
    ChrTalk(
        0x8,
        (
            "#3300F『帕蒂尔·玛蒂尔』──\x01",
            "一起来喝茶吧。\x02\x03",

            "#3304F今天将会是很漫长的一天哦。\x02\x03",

            "#3302F或许会是……自治州有史以来\x01",
            "最漫长的一天呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_87(0x0, 0xFF, 0x1, "pm_head:Layer1(4)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(300)
    Sound(943, 0, 100, 0)
    Sleep(1500)
    FadeToDark(3000, 0, -1)
    SetCameraDistance(12000, 4000)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_E3(0xB)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_109 end

    def Function_3_1021(): pass

    label("Function_3_1021")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1070")
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(1000)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(1000)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(1000)
    Jump("Function_3_1021")

    label("loc_1070")

    Return()

    # Function_3_1021 end

    SaveToFile()

Try(main)
