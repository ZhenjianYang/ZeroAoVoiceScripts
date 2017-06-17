from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0597.bin",                # FileName
        "c0597",                    # MapName
        "c0597",                    # Location
        0x0029,                     # MapIndex
        "ed7302",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 0, 0, 1],
    )

    BuildStringList((
        "c0597",                  # 0
        "雾香",                   # 1
        "雷克特",                 # 2
        "模型",                   # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       0,       64000,   1200,    0,       1500,    64000,   0x007C, 0,  2,  0x0000)

    ChipFrameInfo(288, 0)                                        # 0

    ScpFunction((
        "Function_0_120",          # 00, 0
        "Function_1_121",          # 01, 1
        "Function_2_13E",          # 02, 2
        "Function_3_3F2",          # 03, 3
        "Function_4_27A6",         # 04, 4
    ))


    def Function_0_120(): pass

    label("Function_0_120")

    Return()

    # Function_0_120 end

    def Function_1_121(): pass

    label("Function_1_121")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137")
    OP_66(0x0, 0x1)

    label("loc_137")

    ClearMapObjFlags(0x10, 0x10)
    Return()

    # Function_1_121 end

    def Function_2_13E(): pass

    label("Function_2_13E")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1150, 63000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 0, 30, 62300, 0)
    SetChrPos(0x102, -900, 30, 60400, 0)
    SetChrPos(0x104, 900, 30, 60400, 0)
    SetChrPos(0x103, -300, 30, 59700, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x101,
        (
            "#00003F#11P（对方是帝国军情报局的\x01",
            "  雷克特·亚兰德尔。）\x02\x03",

            "#00013F（在他面前，绝不能掉以轻心……\x01",
            "  进去之前一定要做好准备。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "一旦进入房内，\x01",
            "就暂时无法调整装备、道具\x01",
            "和导力器了。\x02\x03",

            "此外，未完成的任务也将全部\x01",
            "强制结束，请多加注意。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还有其它事情】\x01",      # 0
            "【开门进入房间】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_326"),
        (0, "loc_3D5"),
        (SWITCH_DEFAULT, "loc_3F1"),
    )


    label("loc_326")

    Sound(103, 0, 100, 0)
    OP_71(0x10, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x10)
    StopBGM(0xFA0)
    FadeToDark(1000, 0, -1)

    def lambda_34F():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34F)
    Sleep(300)

    def lambda_36C():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36C)
    Sleep(300)

    def lambda_389():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_389)
    Sleep(300)

    def lambda_3A6():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A6)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x103, 0xFF)
    WaitBGM()
    Call(0, 3)
    Jump("loc_3F1")

    label("loc_3D5")

    SetChrPos(0x0, 0, 30, 61800, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_3F1")

    label("loc_3F1")

    Return()

    # Function_2_13E end

    def Function_3_3F2(): pass

    label("Function_3_3F2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    LoadChrToIndex("chr/ch07300.itc", 0x1F)
    LoadChrToIndex("apl/ch51526.itc", 0x20)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03500.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03400.itp")
    SetChrPos(0x101, -700, 30, 101500, 0)
    SetChrPos(0x102, 300, 30, 101500, 0)
    SetChrPos(0x104, 500, 30, 100400, 0)
    SetChrPos(0x103, -900, 30, 100400, 0)
    SetChrPos(0xA, -200, 0, 107950, 0)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -100, 100, 112500, 180)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 98000, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, 112500, 0)
    MoveCamera(27, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)

    def lambda_578():
        OP_97(0x101, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_578)
    Sleep(100)

    def lambda_595():
        OP_97(0x102, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_595)
    Sleep(100)

    def lambda_5B2():
        OP_97(0x104, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5B2)
    Sleep(100)

    def lambda_5CF():
        OP_97(0x103, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5CF)
    OP_68(0, 1100, 110500, 3000)
    MoveCamera(33, 17, 0, 3000)
    SetCameraDistance(18000, 3000)
    Sound(104, 0, 60, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x103, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0003
    AnonymousTalk(
        0x9,
        (
            "嗨，辛苦了。\x02\x03",

            "看样子，你们没把\x01",
            "国防军的家伙带来呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    PlayBGM("ed7564", 0)
    Sleep(500)

    #C0004
    ChrTalk(
        0x101,
        (
            "#12P#00001F……话虽如此，\x01",
            "但请不要因此就断定\x01",
            "我们会轻易放走你。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00101F『赤色星座』的所作所为……\x01",
            "与你并非\x01",
            "毫无干系。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        "#5P#03504F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#00306F#12P我就直截了当地问吧，\x01",
            "你为什么会出现在克洛斯贝尔？\x02\x03",

            "#00311F还有叔叔他们……\x01",
            "『赤色星座』到哪里去了？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        (
            "#12P#00201F既然你是雇主，\x01",
            "显然应该知道吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "#5P#03506F嗯～那我就先从\x01",
            "第一个问题开始回答吧。\x02\x03",

            "#03508F我是今天来的……\x01",
            "坐的是发自帝都的首班车。\x02\x03",

            "#03501F这些行动自然是遵照着\x01",
            "吉利亚斯大叔的指示进行的。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        "#00108F『铁血宰相』……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#12P#00001F……有什么目的？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x9,
        (
            "#5P#03504F在此之前，让我\x01",
            "告诉你们一条有价值的情报吧。\x02\x03",

            "#03501F今天下午，\x01",
            "帝国军将会大举入侵哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0013
    ChrTalk(
        0x101,
        "#12P#00007F！！！\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#00105F什么……！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#12P#00211F……这玩笑太过分了。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00303F#12P不……在这种情况下，\x01",
            "就算是真的也不奇怪。\x02\x03",

            "#00301F是要从贝尔加德门方向入侵吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "#5P#03504F嗯，装甲师团已经\x01",
            "集合在卡雷利亚要塞了。\x02\x03",

            "#03508F虽说只有区区一个师团……\x02\x03",

            "#03501F但配备了最新的重型战车，\x01",
            "应该可以很轻松地击溃\x01",
            "克洛斯贝尔的装甲车呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#12P#00010F唔……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#00107F必、必须要赶快向警备队……\x01",
            "不，是国防军报告！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            "#5P#03508F不用啊，\x01",
            "早就已经通知他们了。\x02\x03",

            "#03503F帝国军事先就向\x01",
            "自治州政府发出了通告。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#12P#00011F！？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            "#5P#03506F但是迪塔大叔并没有\x01",
            "收回ＩＢＣ冻结帝国资产的宣言，\x01",
            "仍然就任为总统。\x02\x03",

            "他应该很清楚才对，想阻止\x01",
            "帝国军的入侵是不可能的。\x02\x03",

            "#03502F这就是我再次来到\x01",
            "克洛斯贝尔的原因。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    def lambda_CFF():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CFF)
    Sleep(30)

    def lambda_D0F():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D0F)
    Sleep(30)

    def lambda_D1F():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D1F)
    Sleep(30)

    def lambda_D2F():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D2F)
    Sleep(30)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)

    #C0023
    ChrTalk(
        0x104,
        (
            "#00301F#11P喂……到底是怎么一回事？\x02\x03",

            "在这种情况下，他任命亚里欧斯大叔\x01",
            "为国防军长官，打的是什么主意？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#5P#00006F……不知道。\x02\x03",

            "就算是亚里欧斯先生，\x01",
            "也不可能与战车抗衡。\x02\x03",

            "#00008F不管怎么想，都只能理解为\x01",
            "他还有尚未亮出的杀手锏……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#6P#00200F难道说……他想与共和国和解，\x01",
            "从而牵制住帝国军……？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#11P#00106F不对，如果是那样的话，\x01",
            "迪塔叔叔就不会在总统演讲中\x01",
            "那样斥责共和国了……\x02\x03",

            "#00108F他恐怕是打算与共和国\x01",
            "也展开正面对决。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)

    #N0027
    NpcTalk(
        0x8,
        "女性的声音",
        "嗯，应该没错。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1100, 102500, 2000)
    SetCameraDistance(17500, 2000)

    def lambda_FAE():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FAE)
    Sleep(50)

    def lambda_FBE():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FBE)
    Sleep(50)

    def lambda_FCE():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FCE)
    Sleep(50)

    def lambda_FDE():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FDE)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)

    def lambda_1007():
        OP_96(0xFE, 0x0, 0x0, 0x18C7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1007)

    def lambda_1021():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1021)
    WaitChrThread(0x8, 1)
    Sound(104, 0, 60, 0)
    OP_6F(0x79)

    #C0028
    ChrTalk(
        0x101,
        "#00005F咦……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        "#00205F你是……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        "#5P#N#00305F这不是雾香小姐吗！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0031
    AnonymousTalk(
        0x8,
        (
            "好久不见了，各位。\x02\x03",

            "亚兰德尔大尉，\x01",
            "不好意思，我来晚了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    def lambda_1140():
        OP_96(0xFE, 0xFFFFFE70, 0x0, 0x1A5E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1140)
    Sleep(1000)
    Fade(500)
    OP_68(760, 1100, 109730, 0)
    MoveCamera(37, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 800, 30, 108500, 270)
    SetChrPos(0x102, 1800, 30, 108300, 270)
    SetChrPos(0x104, 2300, 30, 107100, 270)
    SetChrPos(0x103, 1000, 30, 107100, 270)

    def lambda_11D4():

        label("loc_11D4")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_11D4")

    QueueWorkItem2(0x101, 2, lambda_11D4)

    def lambda_11E6():

        label("loc_11E6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_11E6")

    QueueWorkItem2(0x102, 2, lambda_11E6)

    def lambda_11F8():

        label("loc_11F8")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_11F8")

    QueueWorkItem2(0x103, 2, lambda_11F8)

    def lambda_120A():

        label("loc_120A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_120A")

    QueueWorkItem2(0x104, 2, lambda_120A)

    def lambda_121C():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_121C)
    Sleep(100)

    def lambda_1239():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1239)
    Sleep(100)

    def lambda_1256():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1256)
    Sleep(100)

    def lambda_1273():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1273)
    Sleep(1100)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)

    #C0032
    ChrTalk(
        0x9,
        (
            "#5P#03504F哪里，我也刚来，\x01",
            "不用在意。\x02\x03",

            "#03500F你那边的情况如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#12P#03403F事态的进展和预想中差不多。\x02\x03",

            "#03401F飞艇机甲师团已经\x01",
            "在阿尔泰尔市的郊外散开了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x101,
        "#11P#00010F！？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        "#00108F共、共和国军也……！？\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#12P#00310F飞艇机甲师团……\x01",
            "难道是战车和飞艇的混编部队吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)

    #C0037
    ChrTalk(
        0x8,
        (
            "#6P#03403F嗯，是高机动力的新型战车\x01",
            "和军用飞艇的组合。\x02\x03",

            "#03400F在卡尔瓦德的军队中，\x01",
            "是以最高机动力著称的。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#11P#00013F怎么会这样……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x103,
        "#12P#00208F也就是……两面夹击吗？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#6P#03400F是啊，这种事态显然\x01",
            "不是你们愿意看到的吧。\x02\x03",

            "#03403F只要稍加思考，\x01",
            "就能料想到情况会发展到这种局面。\x02\x03",

            "但是，迪塔·库罗伊斯\x01",
            "却摆出了一副\x01",
            "毫不妥协的强硬态度。\x02\x03",

            "#03402F这到底是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0041
    ChrTalk(
        0x9,
        (
            "#5P#03504F至于另一个问题……\x02\x03",

            "#03502F也就是第二个问题，\x01",
            "我就当作是特别奉送，回答你们吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1672():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1672)
    Sleep(50)

    def lambda_1682():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1682)
    Sleep(50)

    def lambda_1692():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1692)
    Sleep(50)

    def lambda_16A2():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_16A2)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    #C0042
    ChrTalk(
        0x101,
        "#11P#00008F第二个问题……？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        "#12P#00301F……『赤色星座』的去向吗？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "#5P#03505F嗯，答案很简单。\x02\x03",

            "#03506F帝国政府完全不清楚\x01",
            "这件事情呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0045
    ChrTalk(
        0x102,
        "#00107F怎、怎么会……！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#12P#00211F二者的关系已经完全暴露了，\x01",
            "怎么可能会……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#12P#00310F你难道想说，雇他们在克洛斯贝尔\x01",
            "大闹一场之后，契约就结束了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#11P#00011F不……等一下。\x02\x03",

            "#00003F在通商会议召开时，『赤色星座』\x01",
            "与帝国政府签订了契约……\x02\x03",

            "契约内容是歼灭威胁到\x01",
            "宰相生命安全的恐怖分子……\x02\x03",

            "#00013F这没错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        "#5P#03504F嗯，他们也是这么说的吧？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#11P#00008F……莫非……\x02\x03",

            "#00010F他们与帝国政府签订的契约，\x01",
            "在那个时候就已经结束了？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_19D7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_19D7)
    Sleep(50)

    def lambda_19E7():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_19E7)
    Sleep(50)

    def lambda_19F7():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_19F7)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0051
    ChrTalk(
        0x102,
        "#00105F哎……？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#12P#00205F这……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        "#12P#00301F……不会吧………\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "#5P#03504F……呵呵呵。\x02\x03",

            "#03502F罗伊德，你果然\x01",
            "很适合做谍报工作呢。\x02\x03",

            "#03509F不过，性格也许还需要再邪恶一些。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#11P#00007F那、那就是说……！\x02",
    )

    CloseMessageWindow()

    def lambda_1AF4():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1AF4)
    Sleep(50)

    def lambda_1B04():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B04)
    Sleep(50)

    def lambda_1B14():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B14)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0056
    ChrTalk(
        0x9,
        (
            "#5P#03503F答案是ＹＥＳ。\x02\x03",

            "通商会议结束之后，帝国政府和\x01",
            "『赤色星座』就再无瓜葛了。\x02\x03",

            "#03508F尽管如此，\x01",
            "他们却仍然留在克洛斯贝尔，\x01",
            "我们也觉得很可疑呢……\x02\x03",

            "#03501F但真是没想到，\x01",
            "他们竟会突然做出那种事。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#00106F怎么会……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        (
            "#12P#00308F既然如此，叔叔他们\x01",
            "为何会做出那种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        (
            "#12P#00201F……难道说，\x01",
            "他们和『结社』签署了新的契约？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "#6P#03403F不，那也不太说得通。\x02\x03",

            "#03401F在当时发生于利贝尔的那场异变中，\x01",
            "『结社』调用了名为『强化猎兵』\x01",
            "的私有战斗部队。\x02\x03",

            "如果他们要袭击克洛斯贝尔，\x01",
            "应该会派那个部队来执行。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D39():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D39)
    Sleep(50)

    def lambda_1D49():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D49)
    Sleep(50)

    def lambda_1D59():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D59)
    Sleep(50)

    def lambda_1D69():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D69)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    #C0061
    ChrTalk(
        0x103,
        "#12P#00200F……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#00108F也就是说，他们没有必要\x01",
            "特意雇用其它的猎兵团吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#11P#00008F#30W……这样一来……\x01",
            "怀疑对象的范围也就缩小了。\x02\x03",

            "#00003F如今，帝国政府几乎已经\x01",
            "被认定为幕后黑手……\x02\x03",

            "真正的元凶，自然就是通过让猎兵团袭击\x01",
            "克洛斯贝尔市，可以从中获取某些利益的势力……\x02\x03",

            "另外，这股势力还拥有\x01",
            "能够与最高级的猎兵团\x01",
            "订立长期契约的雄厚资金……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0064
    ChrTalk(
        0x101,
        "#11P#00011F……啊。\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7203", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0065
    ChrTalk(
        0x9,
        "#5P#03504F嗯，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "#6P#03401F……真相往往就潜藏在\x01",
            "令人难以置信的可能性之中。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        "#00105F等、等一下！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        "#12P#00208F通、通过这些条件来分析……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#00307F符合条件的对象\x01",
            "不就只剩一个了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00002F#11P这、这个……\x01",
            "现在还不能下结论。\x02\x03",

            "#00006F雷克特大尉、雾香小姐。\x02\x03",

            "虽然很感谢二位提供情报，\x01",
            "但我们毕竟立场不同。\x02\x03",

            "#00013F之后的事情就由我们自己……\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_20D0():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_20D0)
    Sleep(50)

    def lambda_20E0():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_20E0)
    Sleep(50)

    def lambda_20F0():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_20F0)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0071
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013F您好！\x01",
            "我是特别任务支援科的班宁斯……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("女性的声音")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "太、太好了！\x01",
            "总算打通了……\x02\x03",

            "罗伊德，我是塞茜尔！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0073
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F塞茜尔姐姐？\x02\x03",

            "#00001F怎么这么慌张……\x01",
            "出什么事了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("塞茜尔的声音")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这、这个……\x02\x03",

            "就在刚才，亚里欧斯先生\x01",
            "到这栋大楼来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0075
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F亚里欧斯先生！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("塞茜尔的声音")

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "然、然后……\x02\x03",

            "他就带着小琪雅\x01",
            "离开了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0077
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F#4S！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("塞茜尔的声音")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "虽然我试图阻拦他们，\x01",
            "但小琪雅……\x02\x03",

            "总之，你们能不能尽快回来？\x01",
            "详细情况就当面说吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0079
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00010F知、知道了！\x01",
            "你就在那里等我们吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 40, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x1)
    Sound(804, 0, 100, 0)

    #C0080
    ChrTalk(
        0x102,
        "#00101F怎、怎么了？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        "#12P#00301F你的脸色很吓人啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 500)

    #C0082
    ChrTalk(
        0x101,
        (
            "#5P#00013F亚里欧斯先生去了支援科，\x01",
            "把琪雅带走了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0083
    ChrTalk(
        0x102,
        "#00105F#4S！？\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0084
    ChrTalk(
        0x104,
        "#12P#00307F#4S你说什么！？\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x103,
        "#12P#00201F这究竟是……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#5P#00010F总之，我们先回支援科再说！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)

    #C0087
    ChrTalk(
        0x101,
        (
            "#11P#00007F雾香小姐、雷克特先生！\x01",
            "我们就此告辞了！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        "#6P#03400F好的，万事小心。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        "#5P#03509F嗯，加油吧～\x02",
    )

    CloseMessageWindow()

    def lambda_2629():

        label("loc_2629")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2629")

    QueueWorkItem2(0x8, 2, lambda_2629)
    OP_68(400, 1100, 103800, 3000)
    MoveCamera(30, 15, 0, 3000)
    SetCameraDistance(19500, 3000)
    BeginChrThread(0x103, 3, 0, 4)
    Sleep(250)
    BeginChrThread(0x104, 3, 0, 4)
    Sleep(250)
    BeginChrThread(0x101, 3, 0, 4)
    Sleep(250)
    BeginChrThread(0x102, 3, 0, 4)
    Sleep(600)
    Sound(103, 0, 100, 0)
    WaitChrThread(0x102, 3)
    Sound(104, 0, 100, 0)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1100, 110450, 0)
    MoveCamera(30, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrSubChip(0x9, 0x1)
    OP_0D()
    Sleep(300)

    #C0090
    ChrTalk(
        0x9,
        (
            "#03506F#5P那个小姑娘果然是\x01",
            "这一切的『钥匙』呢。\x02\x03",

            "#03508F我说，你觉得还来得及吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        "#03401F#5P这个嘛……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    #C0092
    ChrTalk(
        0x8,
        "#03403F#5P……恐怕很难呢。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    SetScenarioFlags(0x23, 6)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3F2 end

    def Function_4_27A6(): pass

    label("Function_4_27A6")

    OP_92(0xFE, 0x0, 0x18894, 0x1F4)

    def lambda_27B8():
        OP_95(0xFE, 0, 0, 101000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27B8)
    WaitChrThread(0xFE, 1)

    def lambda_27D6():
        OP_95(0xFE, 0, 0, 98000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27D6)

    def lambda_27F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27F0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_4_27A6 end

    SaveToFile()

Try(main)
