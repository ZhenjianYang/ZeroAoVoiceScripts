from ZeroScenarioHelper import *

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
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 24, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1160",                  # 0
        "皮埃尔副局长",           # 1
        "索妮亚副司令",           # 2
        "诺艾尔",                 # 3
    ))

    AddCharChip((
        "chr/ch06402.itc",                   # 00
        "chr/ch06400.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_1B8",          # 01, 1
        "Function_2_1D0",          # 02, 2
        "Function_3_9DE",          # 03, 3
        "Function_4_A17",          # 04, 4
        "Function_5_1126",         # 05, 5
        "Function_6_3A0C",         # 06, 6
        "Function_7_3A50",         # 07, 7
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_194")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_1B7")

    label("loc_194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1A8")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 5)
    Jump("loc_1B7")

    label("loc_1A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_1B7")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 2)

    label("loc_1B7")

    Return()

    # Function_0_180 end

    def Function_1_1B8(): pass

    label("Function_1_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CF")

    Return()

    # Function_1_1B8 end

    def Function_2_1D0(): pass

    label("Function_2_1D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x1B, 0x0)
    ClearScenarioFlags(0x93, 6)
    OP_C7(0x1, 0x1000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_68(40710, 1200, -390, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20840, 0)
    SetChrPos(0x101, 41600, 0, -2500, 0)
    SetChrPos(0x103, 40600, 0, -2750, 0)
    SetChrPos(0x102, 41600, 0, -4000, 0)
    SetChrPos(0x104, 40600, 0, -4250, 0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x8,
        "#5P……然后呢？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "#5P你们说已经找到了，\x01",
            "是真的吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        "#12P#0000F嗯，那当然。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#12P#0106F副局长，请您这次\x01",
            "一定要仔细保存好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "#5P什么啊，你到底想说什么。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#5P#5P不过就是一枚戒指罢了……\x01",
            "我怕老婆这件事\x01",
            "难道有那么滑稽吗，啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#12P#0006F不，那个……\x01",
            "总之，先容我报告吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(2000, 0)
    OP_0D()

    #C0008
    ChrTalk(
        0x101,
        (
            "#12P#0003F……事情就是这样。\x02\x03",

            "#0001F最后是女公关\x01",
            "交还给我们的……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        "#5P什、什、什么……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41320, 30, 1710, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_68(40720, 1200, -2260, 3000)
    OP_95(0x8, 43880, 30, 1710, 2000, 0x0)
    OP_95(0x8, 43880, 30, -870, 2000, 0x0)
    OP_95(0x8, 41100, 30, -870, 2000, 0x0)
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 3)

    #C0010
    ChrTalk(
        0x8,
        (
            "#5P一、一定是什么\x01",
            "地方搞错了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "#5P我、我怎么会……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#12P#0300F这看起来好像就是您说的红耀石戒指，\x01",
            "应该没有搞错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#12P#0203F蔡特也利用嗅觉确认\x01",
            "过了，没有错。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#12P#0000F那个，这就是我们\x01",
            "发现的那个戒指。\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x1F4, 0x3E8, 0x0)
    EndChrThread(0x8, 0x1)
    OP_95(0x8, 41600, 30, -870, 3000, 0x0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0x8, 0xB4, 0x2EE)
    Sleep(750)
    OP_95(0x8, 41600, 30, -1250, 1000, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#800M红耀石的结婚戒指\x07\x00",
            "交出了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_98(0x101, 0x0, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_93(0x8, 0x0, 0x1F4)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0016
    ChrTalk(
        0x8,
        "#5P哎～咳咳！\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    #C0017
    ChrTalk(
        0x8,
        (
            "#5P做得很好，\x01",
            "你们可以走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#5P不过呢，这次的事情\x01",
            "绝对要保密。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "#5P当然也包括那个赛尔盖哦。\x01",
            "绝对不能和任何人说！\x01",
            "──明白了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#12P#0205F呼，可是，\x01",
            "蔡特的功绩还没……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 750)

    #C0021
    ChrTalk(
        0x8,
        "#5P（瞪眼）……！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#12P#0211F明白了……\x01",
            "（稍后申请给它购买一些\x01",
            "　奖励用的肉骨头好了。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D9():

        label("loc_7D9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7D9")

    QueueWorkItem2(0x0, 1, lambda_7D9)

    def lambda_7EB():

        label("loc_7EB")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7EB")

    QueueWorkItem2(0x1, 1, lambda_7EB)

    def lambda_7FD():

        label("loc_7FD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7FD")

    QueueWorkItem2(0x2, 1, lambda_7FD)

    def lambda_80F():

        label("loc_80F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_80F")

    QueueWorkItem2(0x3, 1, lambda_80F)
    OP_95(0x8, 43880, 30, -1250, 2000, 0x0)
    OP_95(0x8, 43880, 30, 0, 2000, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    #C0023
    ChrTalk(
        0x8,
        (
            "#5P呼呼……总算是得救了啊，\x01",
            "应该算是得救了吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(2000)

    #C0024
    ChrTalk(
        0x104,
        "#12P#0300F（好像有种奇妙的爽快感啊。）\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        "#12P#0100F（总算是解决了一件事啊。）\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#12P#0000F（哈哈……别再打扰他了，\x01",
            "　我们差不多也该回去工作了吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        "#6P#0200F（嗯，就这么办吧。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【遗失的结婚戒指】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SubItemNumber(0x33D, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x15, 0x1, 0x9)
    OP_29(0x15, 0x4, 0x10)
    SetScenarioFlags(0x5C, 2)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1D0 end

    def Function_3_9DE(): pass

    label("Function_3_9DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A16")
    OP_95(0x8, 42500, 30, -870, 3000, 0x0)
    OP_95(0x8, 40500, 30, -870, 3000, 0x0)
    Jump("Function_3_9DE")

    label("loc_A16")

    Return()

    # Function_3_9DE end

    def Function_4_A17(): pass

    label("Function_4_A17")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(41000, 1900, -500, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 41100, 0, -2500, 0)
    SetChrPos(0x102, 40100, 0, -2500, 0)
    SetChrPos(0x103, 39100, 0, -2500, 0)
    SetChrPos(0x104, 42100, 0, -2500, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    Sound(818, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("听上去很神经质的声音")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            "#4S──真是的！\x01",
            "究竟打算要干什么啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    OP_68(41000, 900, -500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0030
    ChrTalk(
        0x8,
        (
            "#5P竟然多管闲事，擅自去\x01",
            "处理和任务无关的事情……！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#5P而且还被那个亚里欧斯·马克莱因\x01",
            "给抢走了功劳……！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "#5P更、更气人的是，\x01",
            "居然还让《克洛斯贝尔时代周刊》的\x01",
            "人看了笑话！！！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#12P#0011F那个，但是……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x190)

    #C0034
    ChrTalk(
        0x8,
        "#5P#4S闭嘴，找借口也没用！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#5P#3S真是的，所以说\x01",
            "我才反对设立什么新部门！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "#5P要不是因为那个惹人讨厌的\x01",
            "赛尔盖提出了交换条件，\x01",
            "我才不会同意这种事……！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#12P#0105F那个，交换条件是……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0038
    ChrTalk(
        0x8,
        "#5P#4S唔～这和你们没有关系！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0039
    ChrTalk(
        0x8,
        (
            "#1P#2S等、等一下……\x01",
            "……对了，有办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#1P#2S如果连一名部下都没有，\x01",
            "那个瘟神也就无计可施了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0041
    ChrTalk(
        0x8,
        "#5P你们几个，我也不想说太难听的话了。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#5P在一两天之内，给我主动从\x01",
            "『特别任务支援科』这个部门辞职。\x02",
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

    #C0043
    ChrTalk(
        0x101,
        "#12P#0005F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#2P#0301F喂喂……\x01",
            "这话从何说起啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#6P#0211F……完全不明白您的意思。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "#5P很简单，就是字面上的意思。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#5P反正也只是个连半年都支撑不下去的部门，\x01",
            "绝对不可能立下什么功绩的。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#5P反而有可能被卷入一些问题中，\x01",
            "给自己的工作经历增添污点……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#5P你们不觉得很愚蠢吗？\x02",
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

    #C0050
    ChrTalk(
        0x8,
        (
            "#5P罗伊德的志愿是搜查官吧？\x01",
            "那就把你转到搜查科的某个岗位吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#5P至于其他人，我也会把你们\x01",
            "调到更加适合自己的新岗位上。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#5P我说，这不是坏事，可不要误解我的好意啊。\x01",
            "给你们一个晚上的时间，好好考虑一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_A17 end

    def Function_5_1126(): pass

    label("Function_5_1126")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05700.itc", 0x1E)
    LoadChrToIndex("chr/ch00800.itc", 0x1F)
    LoadChrToIndex("apl/ch50109.itc", 0x20)
    OP_68(-2000, 1100, 15900, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, -2300, 0, 16500, 180)
    SetChrPos(0x102, -1700, 0, 16500, 180)
    SetChrPos(0x103, -2300, 0, 16500, 180)
    SetChrPos(0x104, -1700, 0, 16500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02000.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00500.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0053
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "警察局总部三层──\x07\x00\x02",
        )
    )

    Sleep(2500)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_68(-2000, 1100, 12900, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(160, 0, 100, 0)
    Sleep(1000)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)

    def lambda_12E5():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x300C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12E5)

    def lambda_12FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12FF)
    Sleep(350)

    def lambda_1313():
        OP_96(0xFE, 0xFFFFFA88, 0x0, 0x300C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1313)

    def lambda_132D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_132D)
    Sleep(350)

    def lambda_1341():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1341)

    def lambda_135B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_135B)
    Sleep(350)

    def lambda_136F():
        OP_96(0xFE, 0xFFFFFA88, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_136F)

    def lambda_1389():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1389)
    WaitChrThread(0x101, 1)

    def lambda_139E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_139E)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    WaitChrThread(0x102, 1)

    def lambda_13C4():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_13C4)
    WaitChrThread(0x103, 1)

    def lambda_13D5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_13D5)
    WaitChrThread(0x104, 1)

    def lambda_13E6():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_13E6)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    #C0054
    ChrTalk(
        0x104,
        (
            "#0306F竟然又被那个讨厌的\x01",
            "副局长叫来了啊……\x02\x03",

            "#0301F到底有什么事啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯～……\x01",
            "说是有客人在等我们。\x02\x03",

            "#0000F我想应该并不是只为了\x01",
            "训话或批评而把我们叫来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        (
            "#0203F……但我感觉，不管怎样\x01",
            "都会被挖苦讽刺一番呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#0106F是啊……\x01",
            "算了，让他随便说去吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1509():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1509)
    Sleep(100)

    def lambda_1519():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1519)
    Sleep(50)

    def lambda_1529():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1529)
    Sleep(50)

    def lambda_1539():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1539)
    WaitChrThread(0x101, 2)
    OP_68(-2000, 1100, 9900, 3000)

    def lambda_155B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_155B)
    Sleep(100)
    WaitChrThread(0x102, 2)

    def lambda_157C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_157C)
    Sleep(50)
    WaitChrThread(0x103, 2)

    def lambda_159D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_159D)
    Sleep(100)
    WaitChrThread(0x104, 2)

    def lambda_15BE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15BE)
    Sleep(2500)
    Fade(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_68(700, 1100, 2300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 700, 30, 2300, 90)
    SetChrPos(0x102, 700, 30, 900, 90)
    SetChrPos(0x103, -500, 30, 2300, 90)
    SetChrPos(0x104, -500, 30, 900, 90)
    OP_68(3700, 1100, 2300, 2000)

    def lambda_1673():
        OP_96(0xFE, 0xE74, 0x1E, 0x8FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1673)
    Sleep(50)

    def lambda_1690():
        OP_96(0xFE, 0xE74, 0x1E, 0x384, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1690)
    Sleep(50)

    def lambda_16AD():
        OP_96(0xFE, 0x9C4, 0x1E, 0x8FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16AD)
    Sleep(50)

    def lambda_16CA():
        OP_96(0xFE, 0x9C4, 0x1E, 0x384, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16CA)
    WaitChrThread(0x101, 1)

    def lambda_16E8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16E8)
    WaitChrThread(0x102, 1)

    def lambda_16F9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_16F9)
    WaitChrThread(0x103, 1)

    def lambda_170A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_170A)
    WaitChrThread(0x104, 1)

    def lambda_171B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_171B)
    WaitChrThread(0x104, 2)

    def lambda_172C():
        OP_95(0xFE, 3700, 0, 3200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_172C)
    WaitChrThread(0x101, 1)
    Sleep(300)
    Sound(811, 0, 100, 0)
    Sleep(800)

    #C0058
    ChrTalk(
        0x101,
        (
            "#2P#0001F──特别任务支援科，\x01",
            "班宁斯等四名成员前来报到。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 3500, 0, 5200, 0)

    #N0059
    NpcTalk(
        0x8,
        "听上去很神经质的声音",
        "#2S#5P哼……进来吧。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#2P#0003F打扰了。\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_79(0x0)
    Sleep(300)

    def lambda_1828():
        OP_95(0xFE, 3700, 0, 4500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1828)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_68(41270, 1000, -4180, 0)
    MoveCamera(55, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x8, 42100, 30, 1900, 180)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 42100, 30, -900, 180)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 43000, 0, -1400, 180)
    SetChrPos(0x101, 41000, 0, -7000, 0)
    SetChrPos(0x102, 41000, 0, -7000, 0)
    SetChrPos(0x103, 41000, 0, -7000, 0)
    SetChrPos(0x104, 41000, 0, -7000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(41840, 1000, -2380, 2500)
    SetCameraDistance(22000, 2500)

    def lambda_197C():
        OP_96(0xFE, 0x9EFC, 0x0, 0xFFFFF0C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_197C)

    def lambda_1996():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1996)
    Sleep(350)

    def lambda_19AA():
        OP_96(0xFE, 0xA348, 0x0, 0xFFFFF0C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19AA)

    def lambda_19C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_19C4)
    Sleep(350)

    def lambda_19D8():
        OP_96(0xFE, 0x9EFC, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19D8)

    def lambda_19F2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_19F2)
    Sleep(350)

    def lambda_1A06():
        OP_96(0xFE, 0xA348, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A06)

    def lambda_1A20():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1A20)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)

    #C0061
    ChrTalk(
        0x101,
        "#6P#0005F（哎，那个制服是……）\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        "#6P#0105F（好像是……警备队的成员吧？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_1AC2():
        OP_96(0xFE, 0xA348, 0x0, 0xFFFFEAE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1AC2)
    #Sound(1365, 255, 100, 0)    #voice#Randy
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0063
    ChrTalk(
        0x104,
        "#11P#0307F#4S咦咦……！？#3S\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #N0064
    NpcTalk(
        0x9,
        "戴眼镜的女性",
        (
            "#2004F#5P哎呀，这算是打招呼吗，\x01",
            "兰迪·奥兰多。\x02\x03",

            "#2002F『咦咦』是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#12P#0309F啊，不不……\x01",
            "应该说是稍微有点出乎意料吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BB0():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BB0)
    Sleep(50)

    def lambda_1BC0():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1BC0)
    Sleep(50)
    TurnDirection(0x103, 0x104, 500)

    #C0066
    ChrTalk(
        0x101,
        "#5P#0005F怎么，你们认识吗？\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x103,
        (
            "#6P#0211F这种反应，感觉好像是\x01",
            "做过什么亏心事一样呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        "#5P哎～咳咳！\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        "#5P你们几个，快点敬礼！\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "#5P这位是担任警备队副司令的\x01",
            "索妮亚二校！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1CC8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CC8)
    Sleep(50)

    def lambda_1CD8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CD8)
    Sleep(50)
    OP_93(0x103, 0x0, 0x1F4)

    #C0071
    ChrTalk(
        0x101,
        "#6P#0005F警备队的副司令……！\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        "#12P#0101F失、失礼了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0073
    ChrTalk(
        0x103,
        (
            "#6P#0208F（所谓二校，在普通的军队中\x01",
            "　应该就相当于中校吧……）\x02\x03",

            "（原来是这么了不起的人吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#0306F#12P（那还用说……\x01",
            "　她可是警备队中真正的二把手啊。）\x02\x03",

            "#0300F（但要说身为指挥官的领导力，\x01",
            "　则是毫无疑问的Ｎｏ．１了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "#2004F#5P呵呵……\x01",
            "请不用那么拘谨。\x02\x03",

            "#2000F你们就是『特别任务支援科』的成员吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#6P#0000F是、是的。\x02\x03",

            "今天找我们特别任务支援科，\x01",
            "是有何要事呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        "#5P哼哼，你们应该感到光荣。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "#5P像你们这种毫无用处的新手\x01",
            "竟然也会被叫来啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_93(0x9, 0x15E, 0x1F4)

    #C0079
    ChrTalk(
        0x9,
        (
            "#12P#2003F……副局长，\x01",
            "交代的事情就由我来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        "#5P可、可是……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "#5P……明白了，\x01",
            "那就全部交给您吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        "#12P#2000F谢谢。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0083
    AnonymousTalk(
        0x9,
        (
            "──正式自我介绍一下。\x01",
            "我是克洛斯贝尔警备队的副司令，\x01",
            "索妮亚·贝尔茨。\x02\x03",

            "今日来此，是希望借助你们\x01",
            "『特别任务支援科』的力量。\x02\x03",

            "首先，容我先将事情的情况\x01",
            "向你们大概介绍一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    SetCameraDistance(21500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    OP_68(41300, 900, -2100, 0)
    MoveCamera(47, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x9, 42200, 0, -2100, 270)
    SetChrPos(0xA, 42500, 0, -3000, 270)
    SetChrPos(0x101, 39700, 0, -2600, 90)
    SetChrPos(0x102, 39700, 0, -1600, 90)
    SetChrPos(0x104, 38400, 0, -2500, 90)
    SetChrPos(0x103, 38400, 0, -1500, 90)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0084
    AnonymousTalk(
        0x101,
        "#0001F魔兽侵害事件的调查……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(22500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0085
    ChrTalk(
        0x9,
        (
            "#2003F#11P嗯，正是。\x02\x03",

            "#2000F在最近这一个月左右，自治州各地\x01",
            "都相继发生了某种特定魔兽的侵害事件。\x02\x03",

            "希望你们能够\x01",
            "帮忙进行调查。\x02",
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

    #C0086
    ChrTalk(
        0x101,
        (
            "#6P#0011F请、请稍等一下。\x02\x03",

            "不是克洛斯贝尔市内……\x01",
            "而是调查市外的魔兽侵害事件吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        "#2000F#11P啊，有什么异议吗？\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#6P#0003F不、不……并非如此。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#0101F#6P那个，警备队方面\x01",
            "应该已经在进行调查了吧？\x02\x03",

            "在这种情况下，还有我们\x01",
            "可以帮忙的余地吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "#2006F#11P嗯～有很多呢。\x02\x03",

            "#2001F如果说是普通的魔兽侵害事件，\x01",
            "令人费解的疑点也过多了。\x02\x03",

            "光靠我们的调查实在是不够，\x01",
            "情况目前已经陷入僵局了。\x02\x03",

            "所以说，希望能有人从\x01",
            "别的视角来切入调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#6P#0005F别的视角吗？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "#2003F#11P没错，也就是说，并非以职业警备队员的视角，\x01",
            "而是以职业搜查官的视角来调查。\x02\x03",

            "#2000F从这层意义上来说，\x01",
            "也并不是非要找你们支援科不可。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(300)

    #C0093
    ChrTalk(
        0x9,
        (
            "#2002F#2P比如说，也可以去拜托知名\x01",
            "精英部门——『搜查一科』之类的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    #C0094
    ChrTalk(
        0x8,
        (
            "#5P不，那个……哈哈。\x01",
            "虽然我很乐意为您介绍。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        "#5P但是，那个，那些家伙一直都非常忙。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    #C0096
    ChrTalk(
        0x9,
        (
            "#2004F#11P──就是这样，\x01",
            "因为有种种原因，\x01",
            "所以最后就指名要找你们了。\x02\x03",

            "#2000F是不是有什么为难之处呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#6P#0002F不，没有……\x02\x03",

            "#0004F──我明白了。\x01",
            "既然发生了这种事，我们很愿意提供协助。\x02\x03",

            "#0001F不过，说是要对魔兽侵害事件进行调查，\x01",
            "但具体应该做些什么好呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    #C0098
    ChrTalk(
        0x9,
        "#5P#2000F──诺艾尔，把那东西给他。\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    #Sound(1491, 255, 100, 0)    #voice#Noel

    #N0099
    NpcTalk(
        0xA,
        "女性队员",
        "#11P#0500F是。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(40840, 900, -2120, 1000)

    def lambda_2789():

        label("loc_2789")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_2789")

    QueueWorkItem2(0x102, 2, lambda_2789)

    def lambda_279B():

        label("loc_279B")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_279B")

    QueueWorkItem2(0x103, 2, lambda_279B)

    def lambda_27AD():
        OP_95(0xFE, 40500, 0, -2800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_27AD)
    WaitChrThread(0xA, 1)

    def lambda_27CB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_27CB)
    EndChrThread(0x102, 0x2)

    def lambda_27DC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_27DC)
    EndChrThread(0x103, 0x2)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    #Sound(1492, 255, 100, 0)    #voice#Noel
    SetChrName("女性队员")

    #A0100
    AnonymousTalk(
        0xFF,
        "──请。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(60, 180, -1, -1)

    #A0101
    AnonymousTalk(
        0x101,
        "#0000F啊，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0102
    ChrTalk(
        0x101,
        "#6P#0005F（哎，这个人……？）\x02",
    )

    CloseMessageWindow()

    #N0103
    NpcTalk(
        0xA,
        "女性队员",
        "#11P#0505F嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#6P#0003F不，没什么……不好意思。\x02\x03",

            "#0008F（嗯～……\x01",
            "　感觉好像在什么地方见过。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0105
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D4, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(41300, 900, -2100, 1000)

    def lambda_29B8():
        OP_96(0xFE, 0xA604, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_29B8)
    WaitChrThread(0xA, 1)
    Sleep(500)
    OP_64(0x101)
    Sleep(300)

    #C0106
    ChrTalk(
        0x101,
        "#6P#0001F这是……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x102,
        "#0101F#5P警备队的调查报告书啊。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "#2003F#11P我们这边调查得知的案情，\x01",
            "都已经写在这上面了。\x02\x03",

            "#2000F希望各位看完那份调查简介，\x01",
            "然后就立刻展开调查工作。\x02\x03",

            "这也是为了避免给你们增添先入为主的多余观点。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2AC1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2AC1)
    Sleep(100)
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(200)

    #C0109
    ChrTalk(
        0x102,
        "#0100F#6P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#6P#0000F既然是这样，\x01",
            "那么我们稍后就看。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "#2004F#11P呵呵，那就拜托了。\x02\x03",

            "#2002F那么，不好意思，\x01",
            "我们就先行告辞了。\x02\x03",

            "今后会与支援科直接进行沟通，\x01",
            "如果发现了什么，就来向我报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#6P#0000F明白了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(300)

    #C0113
    ChrTalk(
        0x9,
        (
            "#2000F#12P──副局长，\x01",
            "实在是打扰了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "#5P不不，哪里哪里。\x01",
            "不用客气，欢迎再来。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    def lambda_2C31():

        label("loc_2C31")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2C31")

    QueueWorkItem2(0x101, 2, lambda_2C31)

    def lambda_2C43():

        label("loc_2C43")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2C43")

    QueueWorkItem2(0x102, 2, lambda_2C43)

    def lambda_2C55():

        label("loc_2C55")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2C55")

    QueueWorkItem2(0x103, 2, lambda_2C55)

    def lambda_2C67():

        label("loc_2C67")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2C67")

    QueueWorkItem2(0x104, 2, lambda_2C67)

    def lambda_2C79():
        OP_95(0xFE, 40500, 0, -3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2C79)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x104, 500)
    Sleep(300)

    #C0115
    ChrTalk(
        0x9,
        (
            "#2002F#11P呵呵……\x02\x03",

            "看起来，你好像已经\x01",
            "非常适应现在的工作了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x104,
        (
            "#0302F#6P这个，哈哈……\x02\x03",

            "#0304F嗯，比起监视国境和演习，\x01",
            "确实还是在这里过得愉快啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "#2004F#11P那就好……\x01",
            "不枉我将你介绍到这里了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(300)

    #C0118
    ChrTalk(
        0x9,
        "#6P#2000F诺艾尔，我们走吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)
    #Sound(1478, 255, 100, 0)    #voice#Noel

    #N0119
    NpcTalk(
        0xA,
        "女性队员",
        "#0500F#5P是。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sound(1498, 255, 100, 0)    #voice#Noel
    Sleep(1000)
    OP_68(41300, 1000, -3600, 2000)
    BeginChrThread(0x9, 3, 0, 6)
    BeginChrThread(0xA, 3, 0, 7)
    WaitChrThread(0x9, 3)
    EndChrThread(0x104, 0x2)

    def lambda_2E26():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2E26)
    WaitChrThread(0xA, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(39100, 1000, -2100, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21850, 0)
    OP_93(0x8, 0xE1, 0x0)
    SetChrPos(0x102, 39700, 0, -1500, 180)
    SetChrPos(0x103, 38400, 0, -1400, 180)
    OP_0D()

    #C0120
    ChrTalk(
        0x104,
        "#6P#0300F呼～……真是吓我一跳。\x02",
    )

    CloseMessageWindow()

    def lambda_2EE4():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EE4)
    Sleep(100)
    TurnDirection(0x102, 0x104, 500)
    Sleep(200)

    #C0121
    ChrTalk(
        0x101,
        (
            "#11P#0000F莫非是你在警备队\x01",
            "时期的长官吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0122
    ChrTalk(
        0x104,
        (
            "#6P#0300F是啊……\x01",
            "不过倒也不是直属上司。\x02\x03",

            "只是在训练和军事演习的时候，\x01",
            "曾经多次接受过她的指导。\x02\x03",

            "#0306F虽然是个美人，但发怒的\x01",
            "时候可是超级恐怖啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#0200F#5P对兰迪前辈发怒的话，\x01",
            "原因八成是生活态度之类的吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#5P#0104F呵呵，我想也是。\x02\x03",

            "#0100F他好像总会引起一些\x01",
            "和女性有关的麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#11P#0005F说起来……\x02\x03",

            "#0001F陪同在副司令身边的那位\x01",
            "女性队员，你也认识吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#6P#0300F不……\x01",
            "是个从没见过的生面孔。\x02\x03",

            "多半是负责辅佐副司令的\x01",
            "唐古拉姆门队员吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0127
    ChrTalk(
        0x104,
        (
            "#6P#0305F嗯，这么一说，\x01",
            "你好像很在意她啊？\x02\x03",

            "#0309F怎么回事，怎么回事，\x01",
            "难不成是对人家一见钟情了吗～？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3184():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3184)
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0128
    ChrTalk(
        0x102,
        "#5P#0111F哎呀……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        "#0211F#5P………………………（瞪～）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0130
    ChrTalk(
        0x101,
        (
            "#11P#0011F不、不是啦，\x01",
            "才没有那种事。\x02\x03",

            "只是，感觉好像曾在\x01",
            "什么地方见到过她……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0131
    ChrTalk(
        0x8,
        "#4S咳咳！#3S\x02",
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
    OP_68(40800, 800, 0, 1200)
    SetCameraDistance(22800, 1200)

    def lambda_32F0():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_32F0)
    Sleep(50)

    def lambda_3300():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3300)
    Sleep(50)

    def lambda_3310():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3310)
    Sleep(50)

    def lambda_3320():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3320)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x79)

    #C0132
    ChrTalk(
        0x101,
        "#0005F#12P啊……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "#5P……你们几个，一直在那里说些无聊的话，\x01",
            "到底还想说到什么时候？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        "#5P难道说……你们是……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "#5P受赛尔盖之类的家伙所指示，\x01",
            "故意来这里戏弄我的吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        "#12P#0011F不、不是，怎么会！\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        "#0103F#6P那个……我们这就告辞了。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "#5P哼……\x01",
            "那就赶快出去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "#5P真是的，竟然全都\x01",
            "无视我的忠告……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "#5P这样做意味着什么，\x01",
            "你们肯定也心知肚明吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#12P#0001F这……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        "#6P#0301F喂喂……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "#5P哼哼，算啦，你们就赶快到\x01",
            "荒山里起早贪黑地寻找魔兽吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "#5P要不然，干脆全员一起\x01",
            "调职到警备队里如何啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        "#5P最好再把那个可憎的赛尔盖也一起带上。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x103,
        "#6P#0211F………………………………\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        "#0103F#6P……告辞了。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23300, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(3700, 1000, 3500, 0)
    MoveCamera(55, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 3700, 0, 4000, 180)
    SetChrPos(0x102, 3700, 0, 4000, 180)
    SetChrPos(0x103, 3700, 0, 4000, 180)
    SetChrPos(0x104, 3700, 0, 4000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    OP_68(3700, 1100, 1400, 2500)

    def lambda_36B7():
        OP_96(0xFE, 0xE74, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36B7)

    def lambda_36D1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36D1)
    Sleep(500)

    def lambda_36E5():
        OP_96(0xFE, 0x125C, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36E5)

    def lambda_36FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_36FF)
    Sleep(500)

    def lambda_3713():
        OP_96(0xFE, 0xA8C, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3713)

    def lambda_372D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_372D)
    Sleep(500)

    def lambda_3741():
        OP_96(0xFE, 0xE74, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3741)

    def lambda_375B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_375B)
    Sleep(500)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)
    WaitChrThread(0x101, 1)

    def lambda_3788():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3788)
    WaitChrThread(0x102, 1)

    def lambda_3799():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3799)
    WaitChrThread(0x103, 1)

    def lambda_37AA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_37AA)
    WaitChrThread(0x104, 1)

    def lambda_37BB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_37BB)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    #C0148
    ChrTalk(
        0x104,
        (
            "#0306F#5P真是的……\x01",
            "那家伙还是那么惹人讨厌啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x103,
        "#0203F#6P……刚才真希望有个耳塞。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#11P#0106F算了，其实我们刚才\x01",
            "也有一点做得不对的地方。\x02\x03",

            "#0101F……但还是觉得\x01",
            "他的言行太过粗暴恶劣了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#12P#0003F──不管这些了，\x01",
            "就算和他针锋相对也没什么意义。\x02\x03",

            "#0001F总之，我们还是先回去\x01",
            "研究一下调查报告书吧。\x02\x03",

            "然后，还要决定调查方针，\x01",
            "展开进一步的行动。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3932():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3932)
    Sleep(50)
    TurnDirection(0x103, 0x101, 500)
    Sleep(200)

    #C0152
    ChrTalk(
        0x102,
        (
            "#5P#0100F是啊，这看起来似乎\x01",
            "不像是普通的魔兽侵害事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x103,
        (
            "#6P#0200F令人费解的疑点……\x01",
            "究竟是指什么呢？\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1126 end

    def Function_6_3A0C(): pass

    label("Function_6_3A0C")

    OP_93(0x9, 0xB4, 0x1F4)

    def lambda_3A18():
        OP_95(0xFE, 40500, 0, -7500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A18)
    Sleep(1000)

    def lambda_3A35():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3A35)
    Sound(103, 0, 100, 0)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Return()

    # Function_6_3A0C end

    def Function_7_3A50(): pass

    label("Function_7_3A50")

    Sleep(600)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)

    def lambda_3A60():
        OP_95(0xFE, 40500, 0, -5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3A60)
    WaitChrThread(0xA, 1)

    def lambda_3A7E():
        OP_95(0xFE, 40500, 0, -7500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3A7E)
    Sleep(500)

    def lambda_3A9B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3A9B)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    Return()

    # Function_7_3A50 end

    SaveToFile()

Try(main)
