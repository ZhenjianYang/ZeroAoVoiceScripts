from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4200.bin",                # FileName
        "e4200",                    # MapName
        "e4200",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4200",                  # 0
        "神狼蔡特",               # 1
        "神狼蔡特",               # 2
        "罗伊德",                 # 3
        "罗伊德",                 # 4
        "SE控制",                 # 5
    ))

    DeclNpc(0,       0,       0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(20500,   4500,    0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(15500,   5500,    0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(16000,   4949,    0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(328, 0)                                        # 0

    ScpFunction((
        "Function_0_148",          # 00, 0
        "Function_1_158",          # 01, 1
        "Function_2_16D",          # 02, 2
        "Function_3_1CBD",         # 03, 3
        "Function_4_1D34",         # 04, 4
        "Function_5_1D68",         # 05, 5
        "Function_6_1D90",         # 06, 6
        "Function_7_1DB8",         # 07, 7
        "Function_8_1DD5",         # 08, 8
        "Function_9_1DEB",         # 09, 9
    ))


    def Function_0_148(): pass

    label("Function_0_148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_157")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_157")

    Return()

    # Function_0_148 end

    def Function_1_158(): pass

    label("Function_1_158")

    OP_F0(0x1, 0x4B0)
    OP_11(0x7B, 0xB4, 0xD5, 0xA, 0x190, 0x0)
    Return()

    # Function_1_158 end

    def Function_2_16D(): pass

    label("Function_2_16D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51620.itc", 0x20)
    SoundLoad(132)
    SoundLoad(962)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    OP_49()
    SetChrPos(0x8, 16000, 0, 0, 0)
    OP_D5(0x8, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x32, 0x1, 0x20)
    SetChrFlags(0x8, 0x1)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x206C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x97, 0xAA, 0x1, 0x20)
    OP_D3(0x101, 0x0, "Null_senaka(42)")
    SetMapObjFrame(0x0, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x0, "879mabuta:Layer2(44)", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x1)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x20)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 1, 0, 3)
    BeginChrThread(0xC, 2, 0, 4)
    Sleep(4000)
    PlayBGM("ed7304", 0)
    OP_68(32000, 5000, 0, 0)
    MoveCamera(330, 5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(69420, 0)
    FadeToBright(1000, 0)
    OP_68(17500, 5800, 0, 6000)
    MoveCamera(320, 18, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(18500, 6000)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xC, 0x2)
    OP_68(17550, 6100, 0, 30000)
    MoveCamera(326, 3, 0, 30000)
    OP_6E(500, 30000)
    SetCameraDistance(15500, 30000)
    Sleep(500)

    #C0001
    ChrTalk(
        0xA,
        "#00011F#5P女神派遣的圣兽……？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P嗯，这样形容\x01",
            "比较便于理解。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P在很久以前，女神将伟大的\x01",
            "『七至宝』赠予人类……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P而我们的使命就是\x01",
            "见证其未来的发展。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xA,
        (
            "#00003F#5P『我们』？难道说……\x02\x03",

            "#00001F曾在利贝尔的异变中\x01",
            "出现的那条龙也是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P嗯，真聪明。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P古代龙雷格纳特\x01",
            "正是我的同胞。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P为了见证『空之至宝』的情况，\x01",
            "它原本一直留在利贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P但在『使命』已经完成的现今，\x01",
            "我也不知道它的去向。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        (
            "#00006F#5P听、听得我一头雾水……\x02\x03",

            "#00008F也就是说，你从很久以前开始，\x01",
            "就一直生活在克洛斯贝尔……？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P嗯，从一千二百年前\x01",
            "的『大崩坏』之前开始。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P当年的『幻之至宝』\x01",
            "为何会消失……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P在那之后，某些人为了让至宝重现，\x01",
            "又做了些什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P像这类事情，我倒也了解一二。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(17150, 6100, 0, 0)
    MoveCamera(313, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    Fade(500)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 8)
    WaitChrThread(0x101, 1)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    Sleep(500)

    #C0015
    ChrTalk(
        0xA,
        (
            "#00006F#5P……老实说，这些事情\x01",
            "是我无论如何也难以调查清楚的。\x02\x03",

            "#00008F继承了女神至宝的\x01",
            "库罗伊斯家族为何会失去至宝……\x02\x03",

            "从而使琪雅\x01",
            "背负上那样的\x01",
            "使命……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    #C0016
    ChrTalk(
        0xA,
        (
            "#00001F#5P拜托你，\x01",
            "请一定要告诉我。\x02\x03",

            "在一千二百年前，究竟发生了什么？\x02\x03",

            "还有，在五百年前，\x01",
            "琪雅又经历了什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(18000, 5500, 0, 2500)
    MoveCamera(310, 3, 0, 2500)
    OP_6E(500, 2500)
    SetCameraDistance(11000, 2500)
    Sleep(1000)

    #C0017
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P好。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P其实我正是为此\x01",
            "才出现在你的面前的。\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Sleep(300)
    SetMapObjFrame(0x0, "879mabuta:Layer1(43)", 0x1, 0x1)
    SetMapObjFrame(0x0, "879mabuta:Layer2(44)", 0x1, 0x1)
    StopBGM(0x1770)
    StopSound(132, 4000, 100)
    StopSound(962, 4000, 60)
    Sleep(800)

    #C0019
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P授予此地的女神至宝……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P是司掌『幻』之属性的\x01",
            "『虚神』。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0021
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P『幻』是掌控思想与认知，\x01",
            "并能控制『因果』的属性。\x02\x03",

            "由于拥有蕴藏着如此力量的至宝，\x01",
            "以当时的库罗伊斯家族为中心的\x01",
            "一派人类产生了一种渴望……\x02\x03",

            "那就是取代女神爱德丝……\x01",
            "成为大地上的『神』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis272.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 170, -1, -1)

    #A0022
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P了解人类、了解大地上的一切，\x01",
            "控制因果，进而引导人类……\x02\x03",

            "听起来，似乎与可以无限满足\x01",
            "人类欲望的『空之至宝』\x01",
            "有不少共通之处吧？\x02\x03",

            "但由于『幻之至宝』\x01",
            "被女神赋予了高等人格，\x01",
            "因此并没有重蹈『空之至宝』的覆辙。\x02\x03",

            "它拥有阻止人类堕落，并引导人类\x01",
            "走向正确道路的睿智与判断力……\x02\x03",

            "因此，它本可以将人类\x01",
            "引导至正确的道路。\x02\x03",

            "但很可惜，至宝的『心』\x01",
            "也是有承受极限的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis273.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(250, 160, -1, -1)

    #A0023
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P各式各样的人性、数之不尽的罪孽，\x01",
            "以及存在于世间的无数扭曲现实……\x02\x03",

            "『幻之至宝』能够理解这些，并展开引导，\x01",
            "也就意味着它拥有与人类相同的『情感』。\x02\x03",

            "而它的『心』，便在这过程中\x01",
            "渐渐破损、崩坏。\x02\x03",

            "如果再这样下去，早晚会失控，\x01",
            "伤害到自己本应守护的人类……\x02\x03",

            "领悟到这一点的至宝，\x01",
            "经过百般苦恼后，最终做出了一个决定──\x02\x03",

            "那就是解除『自己存在于世』这一因果，\x01",
            "令自己从这个世界上彻底消失。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(16500, 5800, 0, 0)
    MoveCamera(322, 6, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    Sound(223, 0, 60, 0)
    Sound(934, 0, 70, 0)
    FadeToDark(0, 16777215, -1)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    Sleep(1000)
    Sound(934, 0, 40, 0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(700)
    Sound(132, 2, 100, 0)
    Sound(962, 2, 60, 0)
    Sleep(300)
    FadeToBright(1500, 16777215)
    OP_0D()
    SetMapObjFrame(0x0, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x0, "879mabuta:Layer2(44)", 0x0, 0x1)
    Sleep(300)

    #C0024
    ChrTalk(
        0xA,
        (
            "#00006F#5P……怎么会……\x02\x03",

            "#00013F但这样一来，\x01",
            "后世的人们就会……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P嗯，他们因为至宝的毁灭而\x01",
            "陷入无尽的困惑、悲伤与恐惧。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P但却完全不去反省一下，\x01",
            "想想事情为何会发展成这样，\x01",
            "至宝又为何会做出那种决定……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P而是像着了魔一样，想制造出一个\x01",
            "与消失的至宝完全同等的东西。\x02",
        )
    )

    CloseMessageWindow()
    StopSound(132, 1500, 100)
    StopSound(962, 1500, 60)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0028
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P不用说，在最初阶段，\x01",
            "他们也只能毫无头绪地盲目摸索。\x02\x03",

            "但经过七百年的尝试，\x01",
            "他们积累了各种各样的知识，\x01",
            "并创造出了一套独有的技术体系。\x02\x03",

            "那就是可以从无到有地使新事物诞生，\x01",
            "名为『炼金术』的魔导技术。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis274.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 170, -1, -1)

    #A0029
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P就这样，他们在此地展开了\x01",
            "一项极其惊人的远大计划。\x02\x03",

            "他们培养了『教团』这个傀儡，\x01",
            "并将新至宝的『核心』\x01",
            "交给教团成员来培育……\x02\x03",

            "随后，他们将『炼成』\x01",
            "这一概念应用至极限，\x01",
            "并在此地构筑了巨大的『式』……\x02\x03",

            "这就是库罗伊斯家族的\x01",
            "炼金术师们从数百年前\x01",
            "开始施行的计划。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis275.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(180, 170, -1, -1)

    #A0030
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P为了确保计划所需要的资金，\x01",
            "他们披上了『银行家』\x01",
            "这一外皮……\x02\x03",

            "另一方面，『教团』为了使他们的信仰对象，\x01",
            "也就是至宝的『核心』从漫长的沉睡中苏醒，\x01",
            "开始蠢蠢欲动。\x02\x03",

            "就这样，又过了五百年，\x01",
            "最终迎来了如今这样的局面。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_68(17150, 6100, 0, 0)
    MoveCamera(315, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    Sound(132, 2, 100, 0)
    Sound(962, 2, 60, 0)
    SetChrSubChip(0x101, 0x2)
    FadeToBright(1500, 0)
    OP_0D()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)

    #C0031
    ChrTalk(
        0xA,
        (
            "#00006F#5P……真是太惊人了。\x02\x03",

            "#00008F不过……总算了解到\x01",
            "整个事件的全貌了。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    OP_68(17500, 5800, 0, 2500)

    #C0032
    ChrTalk(
        0xA,
        (
            "#00003F#5P蔡特，\x01",
            "玛丽亚贝尔小姐曾将\x01",
            "琪雅称作『零之至宝』。\x02\x03",

            "#00013F那是什么意思？\x02\x03",

            "莫非与当年消失的\x01",
            "『幻之至宝』不同？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P很遗憾……\x01",
            "我也不了解这个问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P恐怕是库罗伊斯家族在\x01",
            "经历了一千二百年的执著之后，\x01",
            "终于掌握到了『某些东西』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P凭借着最新发现的成果，\x01",
            "他们想要再现的并不只是\x01",
            "与『幻之至宝』等同的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P而是创造出力量超越\x01",
            "『幻之至宝』的『零之至宝』。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 1, 0, 5)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis276.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 160, -1, -1)

    #A0037
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P以那架白色智能兵器的力量为例。\x02\x03",

            "那并不是智能兵器本身的力量，\x01",
            "应该是通过『至宝』而得到的力量。\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis277.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    SetMessageWindowPos(0, 150, -1, -1)

    #A0038
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P而『幻之至宝』并不具备\x01",
            "那种使巨大事物\x01",
            "瞬间消失的力量。\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis278.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(300)
    SetMessageWindowPos(0, 150, -1, -1)

    #A0039
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P说起来，\x01",
            "那种毁灭空间的力量\x01",
            "与『空』属性的特征更加相符。\x02\x03",

            "假如那还不是『零之至宝』的全部力量……\x01",
            "那就连我都无法想象\x01",
            "其潜在能力有多么惊人了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 2, 0, 6)
    OP_68(17150, 6100, 0, 0)
    MoveCamera(315, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)

    #C0040
    ChrTalk(
        0xA,
        (
            "#00008F#5P……是吗……\x02\x03",

            "#00003F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    Sleep(500)

    #C0041
    ChrTalk(
        0xA,
        (
            "#00006F#5P还有一个问题想问你。\x02\x03",

            "#00008F从你刚才那些话来分析，\x01",
            "那孩子……\x02\x03",

            "#00001F……琪雅她……\x01",
            "并不是普通的人类吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P…………嗯。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P她属于似人又非人的存在。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P为了使『至宝』重现\x01",
            "而创造出来的『核心』。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P恐怕是利用炼金术的奥义\x01",
            "而炼成的『人造生命』。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xA,
        "#00008F#30W#5P………………………………\x02",
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis279.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis280.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis281.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(300)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis282.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)
    BeginChrThread(0x101, 1, 0, 8)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0047
    ChrTalk(
        0xA,
        (
            "#00006F#5P#30W（琪雅大概……知道这个真相\x01",
            "  已经有一段时间了吧。）\x02\x03",

            "（但她却仍然在我们面前\x01",
            "  硬装出一副那样的笑容……）\x02\x03",

            "#00008F（…………琪雅……………）\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 2, 0, 7)
    MoveCamera(30, 5, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(52000, 6000)
    Sleep(1000)
    OP_68(12000, 5000, 0, 5000)
    StopBGM(0x1770)
    Sleep(2000)
    StopSound(132, 4000, 100)
    StopSound(962, 4000, 60)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    EndChrThread(0xC, 0x1)
    EndChrThread(0xC, 0x2)
    SetScenarioFlags(0x22, 0)
    NewScene("e4100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_16D end

    def Function_3_1CBD(): pass

    label("Function_3_1CBD")

    Sound(132, 2, 20, 0)
    Sleep(200)
    OP_25(0x84, 0x19)
    Sleep(200)
    OP_25(0x84, 0x1E)
    Sleep(200)
    OP_25(0x84, 0x23)
    Sleep(200)
    OP_25(0x84, 0x28)
    Sleep(200)
    OP_25(0x84, 0x2D)
    Sleep(200)
    OP_25(0x84, 0x32)
    Sleep(200)
    OP_25(0x84, 0x37)
    Sleep(200)
    OP_25(0x84, 0x3C)
    Sleep(200)
    OP_25(0x84, 0x41)
    Sleep(200)
    OP_25(0x84, 0x46)
    Sleep(2000)
    OP_25(0x84, 0x4B)
    Sleep(200)
    OP_25(0x84, 0x50)
    Sleep(200)
    OP_25(0x84, 0x55)
    Sleep(200)
    OP_25(0x84, 0x5A)
    Sleep(200)
    OP_25(0x84, 0x5F)
    Sleep(200)
    OP_25(0x84, 0x64)
    Return()

    # Function_3_1CBD end

    def Function_4_1D34(): pass

    label("Function_4_1D34")

    Sleep(200)
    Sound(962, 2, 30, 0)
    Sleep(2000)
    OP_25(0x3C2, 0x23)
    Sleep(400)
    OP_25(0x3C2, 0x28)
    Sleep(400)
    OP_25(0x3C2, 0x2D)
    Sleep(400)
    OP_25(0x3C2, 0x32)
    Sleep(400)
    OP_25(0x3C2, 0x37)
    Sleep(400)
    OP_25(0x3C2, 0x3C)
    Return()

    # Function_4_1D34 end

    def Function_5_1D68(): pass

    label("Function_5_1D68")

    OP_25(0x3C2, 0x37)
    Sleep(100)
    OP_25(0x3C2, 0x32)
    Sleep(100)
    OP_25(0x3C2, 0x2D)
    Sleep(100)
    OP_25(0x3C2, 0x28)
    Sleep(100)
    OP_25(0x3C2, 0x23)
    Sleep(100)
    OP_25(0x3C2, 0x1E)
    Return()

    # Function_5_1D68 end

    def Function_6_1D90(): pass

    label("Function_6_1D90")

    OP_25(0x3C2, 0x23)
    Sleep(100)
    OP_25(0x3C2, 0x28)
    Sleep(100)
    OP_25(0x3C2, 0x2D)
    Sleep(100)
    OP_25(0x3C2, 0x32)
    Sleep(100)
    OP_25(0x3C2, 0x37)
    Sleep(100)
    OP_25(0x3C2, 0x3C)
    Return()

    # Function_6_1D90 end

    def Function_7_1DB8(): pass

    label("Function_7_1DB8")

    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x0)
    Sleep(850)
    SetChrSubChip(0x101, 0x4)
    Sleep(1500)
    SetChrSubChip(0x101, 0x5)
    Sleep(1000)
    Return()

    # Function_7_1DB8 end

    def Function_8_1DD5(): pass

    label("Function_8_1DD5")

    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)
    Return()

    # Function_8_1DD5 end

    def Function_9_1DEB(): pass

    label("Function_9_1DEB")

    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)
    Return()

    # Function_9_1DEB end

    SaveToFile()

Try(main)
