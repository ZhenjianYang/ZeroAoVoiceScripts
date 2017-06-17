from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1160.bin",                # FileName
        "c1160",                    # MapName
        "c1160",                    # Location
        0x0018,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 24, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1160",                  # 0
        "皮埃尔副局长",           # 1
    ))

    AddCharChip((
        "chr/ch06402.itc",                   # 00
        "chr/ch06400.itc",                   # 01
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(204, 0)                                        # 0

    ScpFunction((
        "Function_0_CC",           # 00, 0
        "Function_1_104",          # 01, 1
        "Function_2_161",          # 02, 2
        "Function_3_CCB",          # 03, 3
        "Function_4_23B0",         # 04, 4
    ))


    def Function_0_CC(): pass

    label("Function_0_CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E0")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_103")

    label("loc_E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F4")
    ClearScenarioFlags(0x22, 1)
    Event(0, 3)
    Jump("loc_103")

    label("loc_F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_103")
    ClearScenarioFlags(0x22, 2)
    Event(0, 4)

    label("loc_103")

    Return()

    # Function_0_CC end

    def Function_1_104(): pass

    label("Function_1_104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_137")
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_160")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_160")

    Return()

    # Function_1_104 end

    def Function_2_161(): pass

    label("Function_2_161")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(40930, 1200, -590, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24070, 0)
    SetChrPos(0x101, 40570, 0, -1240, 0)
    SetChrPos(0x102, 42040, 0, -1210, 0)
    SetChrPos(0x103, 40600, 0, -2730, 0)
    SetChrPos(0x104, 42020, 0, -2750, 0)
    SetChrPos(0x109, 40570, 0, -4150, 0)
    SetChrPos(0x105, 42000, 0, -4170, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(1500)

    #C0001
    ChrTalk(
        0x101,
        "#1P#N#00005F您的夫人与男公关秘密私会……？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0002
    ChrTalk(
        0x8,
        "#3P嗯……是的……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#3P她最近似乎经常去\x01",
            "那种俱乐部。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "#3P应该是在与某个\x01",
            "男公关秘密私会。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00101F不、不过，\x01",
            "也未必是去见男公关吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x109,
        "#10101F是啊，您还是应该信任夫人……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#3P我抱着必死的决心，\x01",
            "偷偷翻了妻子的皮包，\x01",
            "结果发现了确凿证据！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "#3P她的日程记录本里\x01",
            "满满地记着好多条与一个叫\x01",
            "『克莱德』的男人见面的预定。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#3P她身为一名家庭主妇，\x01",
            "除了男公关俱乐部之外，\x01",
            "还能在哪里结识那种男人呢！？\x02",
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

    #C0010
    ChrTalk(
        0x103,
        "#00206F（原来如此，所以才会那样想……）\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        "#00303F（呼，确实能感觉到他已经豁出去了。）\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x105,
        (
            "#10303F……嗯，不过……\x01",
            "名叫『克莱德』的男公关吗？\x02\x03",

            "#10300F真不凑巧，\x01",
            "我从没听说过这个名字呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5E2():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E2)
    Sleep(50)

    def lambda_5F2():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F2)
    Sleep(50)

    def lambda_602():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_602)
    Sleep(50)

    def lambda_612():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_612)
    Sleep(50)

    def lambda_622():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_622)

    #C0013
    ChrTalk(
        0x8,
        "#3P什、什么……？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00005F是这样吗？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x105,
        (
            "#10302F嗯，只要是在欢乐街的俱乐部\x01",
            "登记在册的男公关，\x01",
            "我基本都知道。\x02\x03",

            "当然了，也有可能是个新人，\x01",
            "所以我还没了解到他的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#3P等、等一下，\x01",
            "你好像很熟悉那个行业啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#3P难道传闻中的那个\x01",
            "临时加入支援科的\x01",
            "现役男公关就是……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x105,
        "#10309F哦，正是本人。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0019
    ChrTalk(
        0x8,
        "#3P你、你！！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#3P你再怎么说也是个警察！\x01",
            "竟然从事男公关这种\x01",
            "不三不四的工作……！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7DC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DC)

    #C0021
    ChrTalk(
        0x101,
        (
            "#00006F好、好啦好啦……\x01",
            "您先冷静一点。\x02\x03",

            "#00001F总之，现在的首要任务\x01",
            "就是尽快搞清楚\x01",
            "夫人目前的状况。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_852():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_852)
    Sleep(50)

    def lambda_862():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_862)
    Sleep(50)

    def lambda_872():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_872)
    Sleep(50)

    def lambda_882():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_882)

    #C0022
    ChrTalk(
        0x109,
        (
            "#10101F就、就是说啊……\x02\x03",

            "#10106F就算您在这里\x01",
            "训斥瓦吉，\x01",
            "他也不会有任何改变的。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x105,
        "#10304F呵呵，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "#3P唔……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#00100F您刚才说，\x01",
            "偷偷翻看了夫人的皮包……\x02\x03",

            "有没有在里面发现\x01",
            "什么有助于调查的\x01",
            "线索呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        "#3P唔，这个嘛……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0027
    ChrTalk(
        0x8,
        "#3P对、对了！我想起来了！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#3P在翻阅日程记录本的时候，\x01",
            "发现她记录了去过的场所……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#3P她最近经常\x01",
            "在白天去\x01",
            "中央广场的西餐厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        (
            "#00203F中央广场的西餐厅，\x01",
            "就是『温赛特』吧……\x02\x03",

            "#00200F但如果对方是男公关的话，\x01",
            "选择在白天见面\x01",
            "不是很奇怪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x105,
        (
            "#10304F也许是特地挑选\x01",
            "丈夫工作的时间段，\x01",
            "以便偷偷会面呢……\x02\x03",

            "#10302F呵呵，男公关与客人\x01",
            "私下会面的时候，\x01",
            "一般都会选在白天呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "#3P果、果然是这样吗……！？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00006F您、您先冷静点。\x01",
            "……还有瓦吉，你也不要再煽风点火了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x105,
        "#10304F呵呵，真不好意思。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00003F咳，总之，\x01",
            "我们已经明白事情的状况了。\x02\x03",

            "#00000F接下来的调查\x01",
            "就交给我们吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "#3P嗯、嗯，\x01",
            "一切都拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#3P无论如何，\x01",
            "一定要给我找出真相！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#3P另外，此事一定要保密。\x01",
            "……明白了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#00006F明、明白了。\x01",
            "……那我们就先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1150", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_2_161 end

    def Function_3_CCB(): pass

    label("Function_3_CCB")

    EventBegin(0x0)
    SoundLoad(812)
    FadeToDark(0, 0, -1)
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在此之后，罗伊德一行与\x01",
            "跟踪夫人的艾莉一行\x01",
            "取得了联系……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "经过一番商量，决定去皮埃尔副局长\x01",
            "所在的警察总部整理情报。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(40930, 1200, -590, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24070, 0)
    SetChrPos(0x101, 40570, 0, -1240, 0)
    SetChrPos(0x102, 42040, 0, -1210, 0)
    SetChrPos(0x103, 40600, 0, -2730, 0)
    SetChrPos(0x104, 42020, 0, -2750, 0)
    SetChrPos(0x109, 40570, 0, -4150, 0)
    SetChrPos(0x105, 42000, 0, -4170, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(1500)
    Sleep(10)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0042
    ChrTalk(
        0x8,
        (
            "#3P那、那么……\x01",
            "调查得怎么样了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#3P我的妻子果然在和\x01",
            "男公关私会吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00003F那个，副局长……\x01",
            "您冷静一点。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(50)

    #C0045
    ChrTalk(
        0x101,
        (
            "#00000F艾莉……你们先说吧，\x01",
            "跟踪夫人时有什么发现吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    #C0046
    ChrTalk(
        0x102,
        (
            "#00100F嗯，虽然用心地监视了她……\x01",
            "但并没有发现什么异常。\x02\x03",

            "她现在应该已经返回\x01",
            "位于住宅街的家中了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(50)

    #C0047
    ChrTalk(
        0x109,
        (
            "#10100F在我们跟踪期间，\x01",
            "她并没有和任何人会面。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        (
            "#00200F但稍后好像会去『诺艾·布朗』，\x01",
            "和那个名叫克莱德的\x01",
            "男人见面……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#3P你、你说什么！？\x02",
    )

    CloseMessageWindow()

    def lambda_1028():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1028)
    Sleep(100)

    def lambda_1038():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1038)
    Sleep(100)

    #C0050
    ChrTalk(
        0x8,
        (
            "#3P可恶，竟敢把我妻子\x01",
            "约到那种可疑的地方，\x01",
            "到底想干什么！？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#3P既、既然如此，我就组编一个警队，\x01",
            "连同『诺艾·布朗』一起查缴……！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00006F都、都说过让您\x01",
            "冷静一点了！\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00303F而且警队根本就不是\x01",
            "那些家伙的对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#3P你、你们说得倒轻松……\x01",
            "但我能冷静得下来吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#3P如果再在这里拖延下去，\x01",
            "男公关就要对我妻子伸出魔爪了……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，您不必担心。\x02\x03",

            "#10302F至少不必担心那位女士\x01",
            "被『男公关』的魔爪侵害。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0057
    ChrTalk(
        0x8,
        "#3P什、什么意思……？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00003F其实瓦吉在一开始\x01",
            "就说过了……\x02\x03",

            "#00001F而我现在也基本确定了，\x01",
            "那位名叫克莱德的男人并不是什么男公关。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        "#3P什、什么……！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "#3P那……\x01",
            "那他是什么人！？\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_132B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1529")
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K克莱德的真实身份是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【男公关】\x01",      # 0
            "【 骗子 】\x01",      # 1
            "【推销员】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13B7"),
        (1, "loc_1449"),
        (2, "loc_14C7"),
        (SWITCH_DEFAULT, "loc_1524"),
    )


    label("loc_13B7")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0062
    ChrTalk(
        0x101,
        (
            "#00006F（……刚才不是已经\x01",
            "  说过他不是\x01",
            "  男公关了吗！）\x02\x03",

            "#00001F（再冷静思考一下吧，\x01",
            "  那位名叫克莱德的男人的真正身份是……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1524")

    label("loc_1449")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0063
    ChrTalk(
        0x101,
        (
            "#00003F（不……严格来说，并不正确。）\x02\x03",

            "#00001F（再冷静思考一下吧，\x01",
            "  那位叫克莱德的男人的真正身份是……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1524")

    label("loc_14C7")


    #C0064
    ChrTalk(
        0x101,
        (
            "#00001F那位叫克莱德的男人，\x01",
            "真实身份应该是……\x01",
            "『推销员』。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_151F")
    OP_2C(0x84, 0x1)

    label("loc_151F")

    Jump("loc_1524")

    label("loc_1524")

    Jump("loc_132B")

    label("loc_1529")


    #C0065
    ChrTalk(
        0x109,
        "#10105F推销员吗？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#00300F确实，他的言行举止很有礼貌，\x01",
            "与其说是男公关，\x01",
            "倒更像是个生意人……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，这也可以更加清楚地\x01",
            "证明他不是男公关。\x02\x03",

            "#10302F我们的职责是为寂寞的女士\x01",
            "带来短暂的美好幻梦……\x02\x03",

            "一流的男公关\x01",
            "虽然会用心陪伴女士，\x01",
            "但并不会过分谦逊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0068
    ChrTalk(
        0x101,
        (
            "#00006F从瓦吉的角度来看，\x01",
            "还会有这种意见啊……\x01",
            "总之，我的推测与他一致。\x02\x03",

            "#00001F那位名叫克莱德的男人与夫人之间的关系，\x01",
            "看上去并不像是\x01",
            "『秘密私会的男公关与客人』。\x02\x03",

            "相对而言，倒更像是\x01",
            "『生意人与顾客』\x01",
            "这样的关系……\x02\x03",

            "他们多次见面，\x01",
            "应该也是为了达成\x01",
            "某项交易而反复交涉。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "#3P如、如果真如你所说……\x01",
            "那他到底在向我妻子\x01",
            "推销什么！？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00003F关于这个问题，只要推理一下\x01",
            "那位名叫克莱德的男人是哪个\x01",
            "行业的推销员，就可以得出答案了。\x02\x03",

            "#00001F那个男人，应该是……\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_182E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A1C")
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K克莱德是哪个行业的推销员？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【宝石店】\x01",          # 0
            "【房地产公司】\x01",      # 1
            "【证券公司】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18C6"),
        (1, "loc_1949"),
        (2, "loc_1994"),
        (SWITCH_DEFAULT, "loc_1A17"),
    )


    label("loc_18C6")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0072
    ChrTalk(
        0x101,
        (
            "#00003F（不……这不太可能。）\x02\x03",

            "#00001F（结合他们在餐厅中的对话，\x01",
            "  还有我们在跟踪时\x01",
            "  所看到的场面来推测……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A17")

    label("loc_1949")


    #C0073
    ChrTalk(
        0x101,
        (
            "#00001F他应该是……\x01",
            "推销房地产的\x01",
            "推销员。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_198F")
    OP_2C(0x84, 0x1)

    label("loc_198F")

    Jump("loc_1A17")

    label("loc_1994")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0074
    ChrTalk(
        0x101,
        (
            "#00003F（不……这不太可能。）\x02\x03",

            "#00001F（结合他们在餐厅中的对话，\x01",
            "  还有我们在跟踪时\x01",
            "  所看到的场面来推测……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A17")

    label("loc_1A17")

    Jump("loc_182E")

    label("loc_1A1C")

    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    #C0075
    ChrTalk(
        0x102,
        (
            "#00103F房地产……\x02\x03",

            "#00100F说起来，他们在餐厅谈话时，\x01",
            "确实提到过有关米修拉姆的话题呢。\x02\x03",

            "一开始还以为是在讨论旅游计划，\x01",
            "但他们还提到了『宣传册』……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    #C0076
    ChrTalk(
        0x101,
        (
            "#00000F那大概是米修拉姆高级别墅区的\x01",
            "住宅信息宣传册。\x02\x03",

            "之后，我们跟踪到港湾区时，\x01",
            "发现一个穿西装的男人\x01",
            "把一件东西交给了克莱德。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x105,
        (
            "#10304F从他们的谈话口气来判断，\x01",
            "那个穿西装的男人应该是克莱德的上司。\x02\x03",

            "#10300F大概是向他转交了购房合同\x01",
            "之类的重要文件。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(50)
    TurnDirection(0x102, 0x8, 500)
    Sleep(100)

    #C0078
    ChrTalk(
        0x101,
        (
            "#00000F那个名叫克莱德的男人\x01",
            "是房地产公司的职员，\x01",
            "他向夫人推销了房地产。\x02\x03",

            "而夫人也接受了他的推荐，\x01",
            "去米修拉姆看了房子，\x01",
            "交涉过程十分顺利。\x02\x03",

            "这应该就是夫人去见\x01",
            "那名男子的原因了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        (
            "#00302F原来如此……\x01",
            "听起来很合乎情理呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x105,
        (
            "#10302F另外，他们的交易\x01",
            "已经在今天大致谈妥了……\x02\x03",

            "稍后就要去『诺艾·布朗』\x01",
            "进行最后的商谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        "#3P唔……原来是这样……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0082
    ChrTalk(
        0x8,
        "#3P不、不对！慢着！\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "#3P玛格丽特想瞒着我，\x01",
            "去买米修拉姆的房子。\x01",
            "……你们是这个意思吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "#3P但、但是……我家根本就没有\x01",
            "可以在那里买房子的钱啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "#3P她到底想从哪里\x01",
            "筹集那么多米拉！？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        (
            "#10108F难、难道说……\x01",
            "夫人准备去借钱……？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x103,
        (
            "#00203F……很有可能。\x02\x03",

            "#00200F对方的目的也许是\x01",
            "诱骗她借贷数额庞大的贷款。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        "#3P怎、怎么会这样……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_0D()
    Fade(500)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sound(812, 0, 100, 0)
    SetChrPos(0x8, 42100, 0, 1700, 90)
    OP_0D()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)
    TurnDirection(0x8, 0x101, 500)
    Sleep(100)

    #C0089
    ChrTalk(
        0x8,
        (
            "#3P我、我决定了……果然还是要\x01",
            "去一趟『诺艾·布朗』！\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "#3P既然已经了解到了这么多情况，\x01",
            "我绝不能眼睁睁地看着\x01",
            "妻子被骗！！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "#3P我要去骂走那个叫克莱德的小子，\x01",
            "然后……就算抽她几个耳光，也要把她拽回家去！！\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#00205F（……妻管严竟然敢吹这么大的牛。）\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#00006F（我们好像给他按下了\x01",
            "  奇怪的开关呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，机会难得，\x01",
            "就帮他一下吧。\x02\x03",

            "#10309F如果放任不管，\x01",
            "任由他独自冲进『诺艾·布朗』\x01",
            "也不太好呢。\x02",
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
    Sleep(1000)

    def lambda_2133():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2133)
    Sleep(50)

    def lambda_2143():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2143)
    Sleep(50)

    def lambda_2153():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2153)
    Sleep(50)

    def lambda_2163():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2163)
    Sleep(50)

    def lambda_2173():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2173)

    #C0095
    ChrTalk(
        0x101,
        (
            "#00006F也许正如你\x01",
            "所说……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x109,
        (
            "#10106F……瓦吉，\x01",
            "你好像越来越开心了？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x105,
        "#10304F呵呵，你在说什么啊。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#00108F总之，能够防止场面失控的人\x01",
            "好像也只有我们了……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#00306F真没办法，虽然不太情愿……\x01",
            "但到了『诺艾·布朗』之后，\x01",
            "就由我出面交涉吧。\x02\x03",

            "#00300F我的熟人扎克斯应该\x01",
            "会在那里担任保安。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "#3P喂！你们在那里嘀嘀咕咕地\x01",
            "说些什么！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22DA():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22DA)
    Sleep(50)

    def lambda_22EA():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22EA)
    Sleep(50)

    def lambda_22FA():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_22FA)
    Sleep(50)

    def lambda_230A():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_230A)
    Sleep(50)

    def lambda_231A():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_231A)

    #C0101
    ChrTalk(
        0x8,
        (
            "#3P别磨磨蹭蹭了，马上出发，\x01",
            "去『诺艾·布朗』吧！！\x01",
            "你们也跟我来！\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#00005F明、明白了……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c0490", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_CCB end

    def Function_4_23B0(): pass

    label("Function_4_23B0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(40930, 1200, -590, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24070, 0)
    SetChrPos(0x101, 40570, 0, -1240, 0)
    SetChrPos(0x102, 42040, 0, -1210, 0)
    SetChrPos(0x103, 40600, 0, -2730, 0)
    SetChrPos(0x104, 42020, 0, -2750, 0)
    SetChrPos(0x109, 40570, 0, -4150, 0)
    SetChrPos(0x105, 42000, 0, -4170, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0103
    ChrTalk(
        0x8,
        (
            "#3P……咳咳，\x01",
            "这次真是辛苦你们了，\x01",
            "特别任务支援科的诸位。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        (
            "#00102F我们已经听说了事情的经过，\x01",
            "暂且算是安心了。\x02\x03",

            "夫人没有被人欺骗，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#3P还、还好吧，但她最后\x01",
            "还是没有放弃\x01",
            "购买别墅的想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "#3P不过，她已经不再提分居的事了，\x01",
            "大概是想把那幢别墅当作\x01",
            "夫妻二人在周末度假的住所吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x109,
        (
            "#10100F哈哈……\x01",
            "夫人好像很喜欢\x01",
            "那幢别墅呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#00309F好啦，这点小事\x01",
            "就别再和夫人\x01",
            "计较啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，反正买别墅的资金\x01",
            "本来就是夫人炒股赚来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "#3P唔……\x01",
            "这也是一个让我头痛的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "#3P唉，经过这件事情之后，\x01",
            "我今后在家里就更加抬不起头了……\x02",
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

    #C0112
    ChrTalk(
        0x103,
        "#00211F（……基本算是自作自受。）\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "#3P唔，不管怎么说……\x01",
            "总算避免了离婚这种\x01",
            "最糟糕的结局。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "#3P这次就向你们\x01",
            "坦率地说声谢谢吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，如果今后再遇到什么事情，\x01",
            "请随时找我们商量。\x02\x03",

            "#00004F……那么，我们这就告辞了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【副局长的委托】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x84, 0x1, 0x1)
    OP_29(0x84, 0x1, 0x2)
    OP_29(0x84, 0x4, 0x10)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    SetScenarioFlags(0x22, 4)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_23B0 end

    SaveToFile()

Try(main)
