from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1390.bin",                # FileName
        "t1390",                    # MapName
        "t1390",                    # Location
        0x0000,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1390",                  # 0
        "职员亨克斯",             # 1
        "中年男性",               # 2
        "咪雪的头",               # 3
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(256, 0)                                        # 0

    ScpFunction((
        "Function_0_100",          # 00, 0
        "Function_1_127",          # 01, 1
        "Function_2_13A",          # 02, 2
        "Function_3_12B9",         # 03, 3
        "Function_4_1304",         # 04, 4
        "Function_5_134F",         # 05, 5
    ))


    def Function_0_100(): pass

    label("Function_0_100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_114")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_126")

    label("loc_114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_126")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 5)

    label("loc_126")

    Return()

    # Function_0_100 end

    def Function_1_127(): pass

    label("Function_1_127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_139")
    VolumeBGM(0x50, 0x32)
    ClearScenarioFlags(0x0, 0)

    label("loc_139")

    Return()

    # Function_1_127 end

    def Function_2_13A(): pass

    label("Function_2_13A")

    EventBegin(0x0)
    VolumeBGM(0x50, 0x3E8)
    FadeToDark(0, 0, -1)
    OP_68(-3080, 2600, -370, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19020, 0)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch28100.itc", 0x20)
    SoundLoad(2679)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x101, -4170, 0, 610, 90)
    SetChrPos(0x102, -2300, 0, 570, 270)
    SetChrPos(0x104, -2550, 0, 1990, 225)
    SetChrPos(0x109, -3870, 0, 2290, 180)
    SetChrPos(0x105, -3280, 0, -1000, 315)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x103, 210, 0, -4420, 0)
    SetChrPos(0x8, 210, 0, -4420, 0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-3080, 1600, -370, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0001
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F……如、如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        "#00100F呵呵，很可爱哦。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x109,
        "#10109F嗯，非常适合你呢！\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F（全身都被包裹住了，\x01",
            "  好像也没什么适不适合的……）\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，穿着它的感觉如何？\x01",
            "看起来好像会很热啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201F嗯……\x01",
            "里面充满\x01",
            "热气呢。\x02\x03",

            "#05203F另外，虽然高度合适，\x01",
            "但穿起来非常肥大，\x01",
            "恐怕会有些行动不便。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#00300F这种细枝末节的小事\x01",
            "就不要计较啦。\x02\x03",

            "#00306F啧，真羡慕呢。\x01",
            "可以明目张胆地和那些\x01",
            "喜欢咪西的女孩亲密接触～\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F喂，不要把别人说得那么不堪！\x01",
            "真是的……\x02\x03",

            "#05205F……哎？\x01",
            "对了，缇欧去哪里了？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#00105F说起来，\x01",
            "她刚才和工作人员谈了几句，\x01",
            "然后就不知去什么地方了……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("缇欧的声音")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我在这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-910, 1600, -2190, 3000)
    MoveCamera(289, 20, 0, 3000)

    def lambda_577():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_577)
    Sleep(50)

    def lambda_587():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_587)
    Sleep(50)

    def lambda_597():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_597)
    Sleep(50)

    def lambda_5A7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A7)
    Sleep(50)

    def lambda_5B7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B7)
    OP_6F(0x79)
    Sound(121, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 3)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 4)

    def lambda_5DE():

        label("loc_5DE")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_5DE")

    QueueWorkItem2(0x101, 1, lambda_5DE)

    def lambda_5F0():

        label("loc_5F0")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_5F0")

    QueueWorkItem2(0x102, 1, lambda_5F0)

    def lambda_602():

        label("loc_602")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_602")

    QueueWorkItem2(0x104, 1, lambda_602)

    def lambda_614():

        label("loc_614")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_614")

    QueueWorkItem2(0x109, 1, lambda_614)

    def lambda_626():

        label("loc_626")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_626")

    QueueWorkItem2(0x105, 1, lambda_626)
    OP_68(-1670, 1600, -1050, 3000)
    MoveCamera(305, 23, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17980, 3000)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x8, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x79)

    #C0011
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205F哎……\x01",
            "是、是缇欧吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    #C0012
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#2679V咪嘻嘻，人家是咪雪哦☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xA77)
    OP_C9(0x1, 0x80000000)

    #C0013
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "哥哥真是的，\x01",
            "连我都认不出了吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        "#00305F呼～又一个让人羡慕的家伙……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BC")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆在间章是否与咪雪会过面？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【曾经会面】\x01",      # 0
            "【没有会面】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_7BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_8EE")

    #C0016
    ChrTalk(
        0x102,
        (
            "#00102F好可爱……\x01",
            "好可爱啊，缇欧！\x02\x03",

            "#00105F这个角色\x01",
            "好像是……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522F嗯，是咪西\x01",
            "的妹妹『咪雪』。\x02\x03",

            "#05524F总是温柔地守护着粗枝大叶、\x01",
            "常把事情搞得一团糟的哥哥，\x01",
            "是个很出色的女孩。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F（温、温柔地……）\x02\x03",

            "#05203F说起来，\x01",
            "我们上次来奇幻乐园的\x01",
            "时候也曾见到过它呢……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A09")

    label("loc_8EE")


    #C0019
    ChrTalk(
        0x102,
        (
            "#00102F好可爱……\x01",
            "好可爱啊，缇欧！\x02\x03",

            "#00105F不过，这个角色\x01",
            "究竟是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522F哦，是咪西\x01",
            "的妹妹『咪雪』。\x02\x03",

            "#05524F总是温柔地守护着粗枝大叶、\x01",
            "常把事情搞得一团糟的哥哥，\x01",
            "是个很出色的女孩。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F（温、温柔地……）\x02\x03",

            "#05203F说起来，\x01",
            "我之前也听说\x01",
            "咪西有个妹妹……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A09")


    #C0022
    ChrTalk(
        0x8,
        (
            "哎呀呀，这孩子\x01",
            "刚才突然找我借\x01",
            "咪雪的扮演服。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "咪雪的轮值时间很宽松，\x01",
            "暂时还用不到这套服装，\x01",
            "所以我就答应她了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x109,
        (
            "#10105F原、原来如此……\x02\x03",

            "不过，你突然穿上这套衣服，\x01",
            "莫非是想……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524F我要在一旁帮忙，协助罗伊德\x01",
            "前辈完成扮演咪西的工作。\x02\x03",

            "#05521F如果他出现什么差错，\x01",
            "我就会毫不留情地踢过去。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0026
    ChrTalk(
        0x105,
        (
            "#10309F哈哈，这就是妹妹的爱之鞭策吗～\x01",
            "好幸福的哥哥啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F还是饶了我吧……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0028
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201F……哎，对了，难道不先\x01",
            "指导指导我的演技吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C04():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C04)
    Sleep(50)

    def lambda_C14():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C14)
    Sleep(50)

    def lambda_C24():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C24)
    Sleep(50)

    def lambda_C34():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C34)
    Sleep(50)

    def lambda_C44():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C44)
    Sleep(300)

    #C0029
    ChrTalk(
        0x8,
        (
            "很抱歉，\x01",
            "实在是来不及了。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "马上就要到\x01",
            "咪西巡游的时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "好啦，只要用心模仿咪西的言行，\x01",
            "就一定没问题的！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F（真、真是不安……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "另外，上午的巡游结束之后，\x01",
            "还要在主题公园内的广场上\x01",
            "举行咪西舞蹈表演。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "关于舞蹈表演，这里有一本我写的演技说明手册，\x01",
            "里面记录了这个部分的重要事项。\x01",
            "……快速阅读一次并记住它吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "查阅了\x01",
            "舞蹈表演手册。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要充满热情，\x01",
            "且富有想象力地跳舞！\x01\x01",
            "※在演出的最后，\x01",
            "　一定不要忘记喊出咪西的\x01",
            "　标志性口号『ＥＮＪＯＹ咪西☆』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x104,
        "#00306F这、这可真是……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        (
            "#10112F未免也太\x01",
            "敷衍了事了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "老实说，\x01",
            "扮演咪西的工作一向都是\x01",
            "交给演员自由发挥的。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "自主题公园开园以来，\x01",
            "从没编写过一本\x01",
            "正规工作手册。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "好啦，万一出现失误，\x01",
            "只要随机应变，勉强应付过去就是了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0042
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524F既然由我担任指导，\x01",
            "就绝不允许出现任何失误。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F你、你要做什么……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0044
    ChrTalk(
        0x8,
        (
            "哦……到时间了，\x01",
            "请尽快做好准备吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10A4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10A4)
    Sleep(50)

    def lambda_10B4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10B4)
    Sleep(50)

    def lambda_10C4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10C4)
    Sleep(50)

    def lambda_10D4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10D4)
    Sleep(300)

    #C0045
    ChrTalk(
        0x102,
        (
            "#00100F那我们就去\x01",
            "园内随意逛逛，\x01",
            "借此打发时间吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x105,
        "#10300F呵呵，我们走了，祝二位幸运。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F好，我们也出发吧，罗伊德前辈。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205F啊……嗯嗯……\x02\x03",

            "#05203F（总之……现在也只能\x01",
            "  在脑中拼命回想至今为止\x01",
            "  对咪西的一切印象了。）\x02\x03",

            "#05200F（另外……舞蹈表演时的标志性\x01",
            "  口号是『ＥＮＪＯＹ咪西☆』。\x01",
            "  一定要牢牢记住。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "那么，\x01",
            "为了孩子们的梦想，\x01",
            "请努力加油吧！！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "一切都拜托你们了！\x01",
            "咪西！咪雪！！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x0)
    OP_29(0x86, 0x1, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("t1030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_13A end

    def Function_3_12B9(): pass

    label("Function_3_12B9")


    def lambda_12BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12BE)

    def lambda_12CF():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12CF)
    WaitChrThread(0x103, 1)
    OP_95(0x103, -1210, 0, -1620, 2000, 0x0)
    TurnDirection(0x103, 0x101, 500)
    Return()

    # Function_3_12B9 end

    def Function_4_1304(): pass

    label("Function_4_1304")


    def lambda_1309():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1309)

    def lambda_131A():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_131A)
    WaitChrThread(0x8, 1)
    OP_95(0x8, -10, 0, -300, 2000, 0x0)
    OP_93(0x8, 0x10E, 0x1F4)
    Return()

    # Function_4_1304 end

    def Function_5_134F(): pass

    label("Function_5_134F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("apl/ch51403.itc", 0x20)
    LoadChrToIndex("chr/ch47300.itc", 0x22)
    SoundLoad(802)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x1)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x9, 0x22)
    SetChrFlags(0x9, 0x8000)
    OP_68(1860, 2600, 260, 0)
    MoveCamera(320, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15130, 0)
    SetChrPos(0x101, 380, 0, 1140, 90)
    SetChrPos(0x103, 2500, 0, 1020, 270)
    SetChrPos(0x9, 210, 0, -4420, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_68(1860, 1600, 260, 3000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()

    #C0051
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F……嘿。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x20)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1370, 200, 310, 180)
    Sound(802, 0, 100, 0)
    OP_0D()

    #C0052
    ChrTalk(
        0x103,
        "#05526F呼……全身都是汗呢。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00009F哈哈……\x01",
            "你真是非常卖力呢。\x02\x03",

            "#00000F辛苦啦，缇欧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_160A")

    #C0054
    ChrTalk(
        0x103,
        (
            "#05522F哪里，罗伊德前辈的表演\x01",
            "才是真正的无可挑剔。\x02\x03",

            "#05524F……那个……最后能\x01",
            "一起跳舞，真是很开心……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#00009F哎，那个……哈哈……\x01",
            "总觉得有些不好意思呢。\x02\x03",

            "#00003F……好啦，\x01",
            "我们差不多也该\x01",
            "去和大家会合了。\x02\x03",

            "#00005F但咪西的真正扮演者\x01",
            "好像还没到呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1708")

    label("loc_160A")


    #C0056
    ChrTalk(
        0x103,
        (
            "#05522F罗伊德前辈也辛苦了。\x01",
            "虽然表演得有些拙劣，\x01",
            "但至少顺利完成了任务。\x02\x03",

            "#05524F我特意担任指导，\x01",
            "总算没有白费力气。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……\x01",
            "你真是帮大忙了呢。\x02\x03",

            "#00003F……好啦，\x01",
            "我们差不多也该\x01",
            "去和大家会合了。\x02\x03",

            "#00005F但咪西的真正扮演者\x01",
            "怎么还没到……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1708")


    #C0058
    ChrTalk(
        0x103,
        "#05520F说起来，真是好慢……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("中年男性的声音")

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S哇哈哈哈！\x01",
            "让你们久等啦！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(1590, 1600, -1210, 3000)

    def lambda_17B2():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17B2)
    Sleep(50)

    def lambda_17C2():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_17C2)
    OP_6F(0x1)
    Sound(121, 0, 100, 0)
    ClearChrFlags(0x9, 0x80)

    def lambda_17DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_17DC)

    def lambda_17ED():
        OP_95(0xFE, 370, 0, -2050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_17ED)
    WaitChrThread(0x9, 1)
    Sleep(300)

    #C0060
    ChrTalk(
        0x101,
        "#00011F哎…………？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        "#05521F…………！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(300)

    #C0062
    ChrTalk(
        0x9,
        "嗝……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    #C0063
    ChrTalk(
        0x9,
        "哇哈哈！抱歉抱歉！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "医生给我开的那种药\x01",
            "只能在饭后服用。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "但我今天没吃成早饭，\x01",
            "所以中午一不留神\x01",
            "就吃多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "……对了，你们把我的扮演服\x01",
            "放到那个柜子里了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x103)

    #C0067
    ChrTalk(
        0x9,
        (
            "……嗯？\x01",
            "干嘛瞪大眼睛看着我？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "话说回来，看你们两个有些面熟，\x01",
            "好像曾在哪里见过……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "不管怎么说，这次真是多谢帮忙啦。\x01",
            "对这座奇幻乐园来说，\x01",
            "咪西是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "你们出色地填补了\x01",
            "我不在时留下的空缺啊。\x01",
            "哇哈哈哈……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "哦，没时间在这里闲聊了。\x01",
            "我还得赶快换衣服，\x01",
            "准备今天下午的工作呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-720, 1600, -10, 3000)

    def lambda_1A78():

        label("loc_1A78")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1A78")

    QueueWorkItem2(0x101, 1, lambda_1A78)

    def lambda_1A8A():

        label("loc_1A8A")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1A8A")

    QueueWorkItem2(0x103, 1, lambda_1A8A)
    OP_95(0x9, -2860, 0, -1350, 2000, 0x0)
    OP_95(0x9, -4080, 0, 260, 2000, 0x0)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(1000)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x103)
    VolumeBGM(0x46, 0x3E8)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Sound(898, 0, 100, 0)
    Sleep(1000)
    Sound(1000, 0, 100, 0)
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()
    VolumeBGM(0x50, 0x3E8)
    OP_93(0x9, 0x5A, 0x1F4)

    #N0072
    NpcTalk(
        0x9,
        "咪西",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "变身完毕～☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0073
    NpcTalk(
        0x9,
        "咪西",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "小哥哥，小姐姐，\x01",
            "真是多谢你们啦！\x01",
            "今天多亏有你们帮忙～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0074
    NpcTalk(
        0x9,
        "咪西",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "接下来的工作就交给我吧～！\x01",
            "咪嘻嘻，再见啦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1590, 1600, -1210, 3000)
    OP_95(0x9, -2860, 0, -1350, 2000, 0x0)
    OP_95(0x9, 370, 0, -2050, 2000, 0x0)

    def lambda_1C1D():
        OP_95(0xFE, 210, 0, -4420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C1D)
    Sound(121, 0, 100, 0)
    Sleep(500)

    def lambda_1C40():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1C40)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    OP_93(0x103, 0xB4, 0x1F4)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    Sound(890, 0, 100, 0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x103)

    #C0075
    ChrTalk(
        0x101,
        (
            "#00005F（真、真不愧是专业演员啊……\x01",
            "  连声调都完全改变了……）\x02\x03",

            "#00006F（虽然称得上是\x01",
            "  完美的咪西……可是……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0076
    ChrTalk(
        0x101,
        (
            "#00011F#4S（和扮演者的反差\x01",
            "  未免也太大了吧！？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0077
    ChrTalk(
        0x101,
        "#00006F……咳咳，那个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0078
    ChrTalk(
        0x101,
        (
            "#00012F总、总之，\x01",
            "我们赶快去找大家吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        "#05520F………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(1000)
    SetScenarioFlags(0x22, 3)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_134F end

    SaveToFile()

Try(main)
