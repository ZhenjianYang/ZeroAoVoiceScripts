from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0510.bin",                # FileName
        "c0510",                    # MapName
        "c0510",                    # Location
        0x0029,                     # MapIndex
        "ed7302",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0510",                  # 0
        "达德利搜查官",           # 1
        "艾玛搜查官",             # 2
        "警官",                   # 3
        "警官",                   # 4
        "警官",                   # 5
        "警官",                   # 6
        "警官",                   # 7
    ))

    AddCharChip((
        "chr/ch30000.itc",                   # 00
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)

    ChipFrameInfo(368, 0)                                        # 0

    ScpFunction((
        "Function_0_170",          # 00, 0
        "Function_1_220",          # 01, 1
        "Function_2_24A",          # 02, 2
        "Function_3_260",          # 03, 3
        "Function_4_11EF",         # 04, 4
    ))


    def Function_0_170(): pass

    label("Function_0_170")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1A8"),
        (1, "loc_1B4"),
        (2, "loc_1C0"),
        (3, "loc_1CC"),
        (4, "loc_1D8"),
        (5, "loc_1E4"),
        (6, "loc_1F0"),
        (SWITCH_DEFAULT, "loc_1FC"),
    )


    label("loc_1A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_1FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_208")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_208")

    label("loc_21F")

    Return()

    # Function_0_170 end

    def Function_1_220(): pass

    label("Function_1_220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_22F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)

    label("loc_22F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_249")
    Event(0, 4)

    label("loc_249")

    Return()

    # Function_1_220 end

    def Function_2_24A(): pass

    label("Function_2_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_END)), "loc_25F")
    ClearMapObjFlags(0x1F, 0x4)
    ClearMapObjFlags(0x20, 0x4)

    label("loc_25F")

    Return()

    # Function_2_24A end

    def Function_3_260(): pass

    label("Function_3_260")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("chr/ch30500.itc", 0x1F)
    LoadChrToIndex("apl/ch51258.itc", 0x20)
    SoundLoad(803)
    SoundLoad(3461)
    SoundLoad(3462)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    OP_68(-40, 1270, 8290, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 680, 30, -2029, 0)
    SetChrPos(0x103, 680, 30, -3530, 0)
    SetChrPos(0x109, 680, 30, -5030, 0)
    SetChrPos(0x102, -740, 30, -3060, 0)
    SetChrPos(0x104, -740, 30, -4560, 0)
    SetChrPos(0x105, -740, 30, -6060, 0)
    SetChrPos(0xA, 4740, 0, 6180, 225)
    SetChrPos(0xB, 4150, 0, 4200, 315)
    SetChrPos(0xC, 2490, 30, 4750, 89)
    SetChrPos(0xD, -4270, 0, 9250, 270)
    SetChrPos(0xE, -5740, 0, 9250, 89)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 660, 20, 8390, 270)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -1000, 20, 8490, 90)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetCameraDistance(21000, 3000)
    FadeToBright(1000, 0)
    Sleep(2500)
    OP_64(0x8)
    OP_64(0x9)
    Sound(103, 0, 100, 0)
    Sleep(300)

    #N0001
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "打扰了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4A5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4A5)
    Sleep(50)

    def lambda_4B5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4B5)
    WaitChrThread(0x8, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_C9(0x0, 0x80000000)

    #A0002
    AnonymousTalk(
        0x8,
        "#5P#3461V#30W你们来了啊。\x02",
    )

    CloseMessageWindow()
    OP_24(0xD85)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_68(-820, 1270, 6090, 3300)

    def lambda_576():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_576)
    Sleep(50)

    def lambda_58E():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58E)
    Sleep(50)

    def lambda_5A6():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A6)
    Sleep(50)

    def lambda_5BE():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BE)
    Sleep(50)

    def lambda_5D6():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5D6)
    Sleep(50)

    def lambda_5EE():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5EE)
    OP_6F(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrPos(0x101, -20, 30, 6270, 0)
    SetChrPos(0x102, 770, 30, 5670, 0)
    SetChrPos(0x103, -950, 30, 4190, 0)
    SetChrPos(0x104, -1320, 30, 5770, 0)
    SetChrPos(0x109, 250, 30, 3960, 0)
    SetChrPos(0x105, -2050, 30, 4030, 0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrPos(0x8, -100, 20, 8400, 180)
    SetChrPos(0x9, -1000, 20, 8900, 180)
    OP_68(-510, 2280, 6790, 0)
    MoveCamera(38, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19700, 0)
    Sleep(1000)
    OP_68(-510, 1280, 6790, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0003
    ChrTalk(
        0x9,
        "#5P呼，你们总算到了。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00006F#12P十分抱歉，\x01",
            "因为手上还有些工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        "#00301F#6P可以把目前的状况告诉我们吗？\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#00606F#5P正如之前所说，\x01",
            "这栋建筑物内现已空无一人。\x02\x03",

            "#00600F之前有近百名人员\x01",
            "出入于此……\x02\x03",

            "但如今，所有人都已经由\x01",
            "地下空间离去，并且行踪不明。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        "#00105F#12P经由地下空间……？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        (
            "#00205F#12P可是……这里并没有\x01",
            "通往地下空间的道路吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "#5P……从现场情况来看，他们似乎是\x01",
            "用爆破的方式强行炸出了道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "#5P我们已经在里面发现了一条\x01",
            "通往地下空间Ｂ区域的通道。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x109,
        "#10107F#12P居、居然做了那种事……！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x105,
        (
            "#10306F#12P哎呀呀……\x01",
            "真是一群危险至极的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#00606F#5P不仅如此，\x01",
            "鲁巴彻当时用于走私的仓库\x01",
            "也被他们大面积改造过。\x02\x03",

            "#00610F变成了完全可以进行\x01",
            "重武器训练与整备的场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00013F#12P……！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#00303F#6P……呼，对叔叔他们来说，\x01",
            "这种小事不足为奇。\x02\x03",

            "#00301F他们本来就是一群战斗狂，\x01",
            "为了保证随时可以应对实战，\x01",
            "平时一直都会通过训练来保持敏锐的战斗感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        "#5P……原来如此。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 500)
    Sleep(300)

    #C0017
    ChrTalk(
        0x8,
        (
            "#00603F#5P奥兰多，我就不拐弯抹角了。\x02\x03",

            "#00601F他们的目标是『黑月』吗？\x01",
            "还是要对车站或空港发动恐怖袭击？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B3C():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B3C)
    Sleep(50)

    def lambda_B4C():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B4C)
    Sleep(50)

    def lambda_B5C():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B5C)
    Sleep(50)

    def lambda_B6C():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B6C)
    Sleep(50)

    def lambda_B7C():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B7C)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0018
    ChrTalk(
        0x104,
        (
            "#00306F#6P这我可就不知道了……\x01",
            "不过，如果目标是『黑月』，他们应该\x01",
            "不会以这种方式来刻意隐藏踪迹。\x02\x03",

            "#00308F至于车站与空港……\x01",
            "他们要想占领这些地方，根本就是小事一桩。\x02\x03",

            "#00311F所以，那些家伙很可能\x01",
            "是在谋划一起更加惊人的事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        "#00201F#12P也就是说……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        (
            "#00107F#11P难道他们想占领\x01",
            "兰花塔吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        (
            "#00305F#5P也有这种可能……\x02\x03",

            "#00306F……不过，好像有些不符合\x01",
            "他们的喜好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x105,
        "#10305F#6P哦？喜好指的是什么？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#00308F#5P……以猎兵的特性来说，\x01",
            "在野外战和游击战中是最能发挥本领的……\x02\x03",

            "#00303F所以他们一般都很喜欢在那种\x01",
            "适合突袭、愚弄正规军的复杂地形战斗。\x02\x03",

            "#00301F比如整个城市的街区……\x01",
            "或是地势起伏较多的山岳地带。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#00005F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        (
            "#10101F#12P确、确实有道理……\x01",
            "在那种地带，车辆的行动也很受限制。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        "#00610F#5P啧，也就是说——\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(300)
    TurnDirection(0x9, 0x8, 500)

    def lambda_EE2():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EE2)
    Sleep(30)

    def lambda_EF2():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EF2)
    Sleep(30)

    def lambda_F02():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F02)
    Sleep(30)

    def lambda_F12():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F12)
    Sleep(30)

    def lambda_F22():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F22)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    SetChrSubChip(0x8, 0x1)
    Sound(804, 0, 100, 0)
    OP_24(0x323)

    #C0027
    ChrTalk(
        0x8,
        (
            "#00603F#11P我是搜查一科的达德利。\x02\x03",

            "#00605F啊，科长，\x01",
            "您辛苦了……\x02\x03",

            "#30W………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0028
    ChrTalk(
        0x8,
        "#00607F#3462V#4S#11P什么！？\x02",
    )

    CloseMessageWindow()
    OP_24(0xD86)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(150)

    #C0029
    ChrTalk(
        0x101,
        "#00013F#12P（怎、怎么了……？）\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        "#00108F#12P（偏偏在这个时候……）\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        "#00311F#6P………………………………\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x8, 0x0)
    Sleep(600)

    #C0032
    ChrTalk(
        0x9,
        (
            "#5P达、达德利长官，\x01",
            "到底发生了什么事……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0033
    ChrTalk(
        0x8,
        (
            "#00603F#5P……是警备队发来的联络。\x02\x03",

            "#00608F有个来历不明的武装集团\x01",
            "出现在了玛因兹山道地区！\x02\x03",

            "#00610F正在巡逻中的部队\x01",
            "已经被他们击溃了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(250, 40, -1, -1)
    SetChrName("众人")
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #A0034
    AnonymousTalk(
        0xFF,
        "#5S！！！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(30000, 5000)
    Sleep(1500)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x323)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 4)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_260 end

    def Function_4_11EF(): pass

    label("Function_4_11EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1500, 50000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -600, 0, 47800, 0)
    SetChrPos(0x102, 600, 0, 47800, 0)
    SetChrPos(0x103, -600, 0, 46300, 0)
    SetChrPos(0x104, 600, 0, 46300, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_129E():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_129E)
    Sleep(50)

    def lambda_12BB():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_12BB)
    Sleep(50)

    def lambda_12D8():
        OP_97(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_12D8)
    Sleep(50)

    def lambda_12F5():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_12F5)
    FadeToBright(1000, 0)
    OP_68(0, 1500, 52000, 2000)
    Sleep(300)

    def lambda_132C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_132C)
    Sleep(50)

    def lambda_1340():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1340)
    Sleep(700)

    def lambda_1354():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1354)
    Sleep(50)

    def lambda_1368():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1368)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(0, 100, 57000, 2000)
    MoveCamera(35, 35, 0, 2000)
    SetCameraDistance(19500, 2000)
    OP_6F(0x79)

    #C0035
    ChrTalk(
        0x103,
        (
            "#00201F看来他\x01",
            "已经先到了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00001F是啊……\x01",
            "加强警觉，我们也下去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 51000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 4)
    EventEnd(0x5)
    Return()

    # Function_4_11EF end

    SaveToFile()

Try(main)
