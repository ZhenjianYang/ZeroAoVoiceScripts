from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9014.bin",                # FileName
        "m9014",                    # MapName
        "m9014",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9014",                  # 0
        "琪雅",                   # 1
        "琪雅",                   # 2
        "SE控制",                 # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(336, 0)                                        # 0

    ScpFunction((
        "Function_0_150",          # 00, 0
        "Function_1_160",          # 01, 1
        "Function_2_165",          # 02, 2
        "Function_3_1647",         # 03, 3
        "Function_4_1683",         # 04, 4
        "Function_5_16A3",         # 05, 5
        "Function_6_16C7",         # 06, 6
        "Function_7_16F2",         # 07, 7
        "Function_8_172A",         # 08, 8
        "Function_9_175C",         # 09, 9
        "Function_10_1780",        # 0A, 10
        "Function_11_17A4",        # 0B, 11
        "Function_12_17E3",        # 0C, 12
        "Function_13_1807",        # 0D, 13
        "Function_14_1832",        # 0E, 14
        "Function_15_1856",        # 0F, 15
        "Function_16_1888",        # 10, 16
        "Function_17_18EF",        # 11, 17
        "Function_18_1921",        # 12, 18
        "Function_19_199B",        # 13, 19
        "Function_20_19C5",        # 14, 20
        "Function_21_1A56",        # 15, 21
        "Function_22_1AE7",        # 16, 22
        "Function_23_1B78",        # 17, 23
        "Function_24_1BBC",        # 18, 24
        "Function_25_1BF0",        # 19, 25
    ))


    def Function_0_150(): pass

    label("Function_0_150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_15F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_15F")

    Return()

    # Function_0_150 end

    def Function_1_160(): pass

    label("Function_1_160")

    OP_F0(0x1, 0x320)
    Return()

    # Function_1_160 end

    def Function_2_165(): pass

    label("Function_2_165")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10800.itc", 0x1E)
    LoadChrToIndex("chr/ch10801.itc", 0x1F)
    LoadChrToIndex("apl/ch51757.itc", 0x21)
    LoadChrToIndex("apl/ch51753.itc", 0x22)
    LoadChrToIndex("apl/ch51754.itc", 0x23)
    LoadEffect(0x0, "battle/cr036301.eff")
    SoundLoad(3336)
    SoundLoad(3649)
    SoundLoad(3650)
    SoundLoad(3651)
    SoundLoad(3652)
    SoundLoad(3653)
    SoundLoad(3654)
    SoundLoad(111)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    SetChrPos(0x101, -2250, 0, 2500, 135)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xD0, 0xD0, 0xD0, 0xFF, 0x0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 400, 0, 0, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 400, -500, 0, 180)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x1)
    SetMapObjFrame(0xFF, "point16_add", 0x2, "night")
    SetMapObjFrame(0xFF, "break00_add", 0x2, "night")
    SetMapObjFrame(0xFF, "break01_add", 0x2, "night")
    SetMapObjFrame(0xFF, "break02_add", 0x2, "night")
    SetMapObjFrame(0xFF, "break03_add", 0x2, "night")
    SetMapObjFrame(0xFF, "yuka00", 0x2, "night")
    SetMapObjFrame(0xFF, "point_add", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm02_add", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm03_add", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm04_add", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm05_add", 0x2, "night")
    OP_68(400, 850, 0, 0)
    MoveCamera(330, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(48000, 0)
    Sound(111, 2, 50, 0)
    FadeToBright(3000, 0)
    SetCameraDistance(38000, 9000)
    PlaceName2(340, 200, "c_plac69", 0x0, 3000)
    Sleep(6000)
    OP_A7(0x8, 0xE0, 0xE0, 0xE0, 0xFF, 0xBB8)
    OP_6F(0x79)
    Fade(1000)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 2000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_0D()
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#11P#60W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #N0002
    NpcTalk(
        0x101,
        "声音",
        "#3336V#5P#N#40W#16A找到你啦。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_68(-200, 850, 460, 2500)
    MoveCamera(330, 17, 0, 2500)
    OP_6E(700, 2500)
    SetCameraDistance(12800, 2500)
    BeginChrThread(0x101, 0, 0, 3)
    WaitChrThread(0x101, 0)
    OP_6F(0x79)

    #C0003
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12305F#11P#60W#15A………………………………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0004
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#3649V#11P#60W#25A……为……什么………？\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(800)

    #C0005
    ChrTalk(
        0x101,
        (
            "#00000F#5P#30W因为我能听到你的声音呀。\x02\x03",

            "#00004F我一直都……\x01",
            "听得到琪雅的声音。\x02\x03",

            "只要竖起耳朵，用心聆听……\x02\x03",

            "#00002F就能明白……\x01",
            "……琪雅的心声是从何处传来的了。\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Sleep(300)

    #C0006
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12314F#11P#40W是吗……嘿嘿……\x02\x03",

            "#12308F……可是琪雅……\x01",
            "并没有资格让\x01",
            "罗伊德对我这么好……\x02\x03",

            "#12306F因为……因为我……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00003F#5P#30W琪雅，你错了。\x02\x03",

            "#00013F无论你是如何诞生于世的──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0008
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12311F#3650V#11P#4S#30W#20A根本没有错！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetCameraDistance(11500, 30000)
    BeginChrThread(0x8, 1, 0, 5)
    WaitChrThread(0x8, 1)

    #C0009
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12307F#12P#40W我并不是真正的人类，\x01",
            "心和灵魂都不是真的……！\x02\x03",

            "所以没资格让你们如此温柔地\x01",
            "照顾我、保护我！\x02\x03",

            "#12311F可……\x01",
            "……可我却……！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 6)
    WaitChrThread(0x8, 1)

    def lambda_761():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_761)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_781():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_781)
    WaitChrThread(0x8, 2)
    Sleep(500)

    #C0010
    ChrTalk(
        0x101,
        "#00008F#5P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x8, 0)
    SetCameraDistance(10400, 100000)
    PlayBGM("ed7581", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x245), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    BeginChrThread(0x101, 1, 0, 8)
    WaitChrThread(0x101, 1)

    #C0011
    ChrTalk(
        0x101,
        (
            "#00002F#5P#30W……琪雅。\x02\x03",

            "从你来到我们身边的那一天算起，\x01",
            "已经过去了半年多……\x02\x03",

            "#00004F你知道自己在这段日子\x01",
            "为我们带来了多少幸福吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#12P#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    #C0013
    ChrTalk(
        0x101,
        (
            "#00000F#5P#30W恐怕与你感受到的幸福是一样的，\x01",
            "甚至更在那之上。\x02\x03",

            "#00002F琪雅……\x01",
            "你与我们生活在一起，难道并不快乐吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0014
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12307F#12P#30W很快乐……！\x01",
            "非常……非常幸福……！\x02\x03",

            "#12311F可是……\x01",
            "也许一切都是因为我用自己的\x01",
            "能力控制了你们的感觉！\x02\x03",

            "也许只是因为我操控了\x01",
            "最为重要的大家的想法！\x02\x03",

            "#12316F#40W所以……\x01",
            "………所以……………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_A2C():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A2C)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_A4C():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A4C)
    WaitChrThread(0x8, 2)
    Sleep(500)

    #C0015
    ChrTalk(
        0x101,
        "#00001F#5P#30W……………………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0)
    BeginChrThread(0x101, 1, 0, 10)
    WaitChrThread(0x101, 1)
    Sleep(300)
    BeginChrThread(0x101, 1, 0, 11)
    WaitChrThread(0x101, 1)

    #C0016
    ChrTalk(
        0x101,
        "#00003F#5P#30W好啦。\x02",
    )

    CloseMessageWindow()

    def lambda_AD1():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AD1)
    WaitChrThread(0x8, 2)
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 13)
    WaitChrThread(0x8, 1)
    BeginChrThread(0x101, 1, 0, 14)
    WaitChrThread(0x101, 1)

    #C0017
    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W其实……\x01",
            "我并不在意是否受到过操控。\x02\x03",

            "#00004F因为我们完全没有遭到操控的感觉，\x01",
            "而且，如果是那种形式的操控，\x01",
            "就算真的遭受过也没有关系啊。\x02\x03",

            "#00000F有些存在本身就会被\x01",
            "大家无条件地怜爱并产生\x01",
            "保护的欲望，比如小猫或婴儿。\x02\x03",

            "琪雅所谓的『能力』，\x01",
            "其实也只有这种程度而已吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12317F#12P#40W…………啊……………\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00004F#5P而且，我们一起度过的那段时间，\x01",
            "并不是由那种『能力』所创造的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis311.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0020
    AnonymousTalk(
        0x101,
        (
            "#40W#3C琪雅和我一起练习烹饪，\x01",
            "挤在一张床上睡懒觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(1, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis386.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)

    #A0021
    AnonymousTalk(
        0x101,
        (
            "#40W#3C和艾莉一起读书，\x01",
            "到屋顶给大家晾衣服。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis387.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(500)

    #A0022
    AnonymousTalk(
        0x101,
        (
            "#40W#3C和缇欧一起做扫除，\x01",
            "购买咪西的限定周边。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(1, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis388.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)

    #A0023
    AnonymousTalk(
        0x101,
        (
            "#40W#3C和兰迪一起玩扑克，\x01",
            "去露天店铺买东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis389.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(500)

    #A0024
    AnonymousTalk(
        0x101,
        (
            "#40W#3C和科长一起洗碗，\x01",
            "和蔡特、柯贝一起午睡。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    CreatePortrait(1, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis390.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)

    #C0025
    ChrTalk(
        0x101,
        (
            "#00000F#5P琪雅，你真的认为\x01",
            "这些全都是『虚假』的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12308F#12P#40W………这…………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)
    BeginChrThread(0x8, 1, 0, 16)
    WaitChrThread(0x8, 1)
    Sleep(300)

    #C0027
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#12P#40W………并不是……虚假的。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00002F#5P#30W所以说，对我们而言，\x01",
            "这些就是不容置疑的『真实』。\x02\x03",

            "#00004F只要我们还拥有这份『真实』……\x02\x03",

            "无论今后要面对怎样的困难，\x01",
            "也绝对不会认输。\x02\x03",

            "#00000F所以，琪雅……\x01",
            "你没必要一个人背负一切。\x02\x03",

            "连同琪雅在内，\x01",
            "我们大家共同努力就好啦。\x02\x03",

            "#00009F这才是所谓的『同伴』……\x01",
            "以及『家人』，不是吗？\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 15)
    WaitChrThread(0x101, 1)
    OP_C9(0x0, 0x80000000)

    #C0029
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12317F#3651V#12P#40W#40A……罗伊……德…………\x02\x03",

            "#12316F#3652V#50W#60A罗伊德……罗伊德……！！\x02",
        )
    )
    #Auto

    Sleep(3000)
    BeginChrThread(0x8, 1, 0, 17)
    WaitChrThread(0x8, 1)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0xA, 1, 0, 25)
    PlayEffect(0x0, 0xFF, 0x8, 0x41, 0, 350, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x10)
    Sleep(1000)
    OP_68(-400, 850, 400, 1000)
    MoveCamera(330, 17, 0, 1000)
    OP_6E(700, 1000)
    SetCameraDistance(10000, 1000)
    BeginChrThread(0x8, 1, 0, 18)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    #C0030
    ChrTalk(
        0x8,
        (
            "#05817F#3653V#12P#40W#58A……呜呜……啊啊啊啊……！\x02\x03",

            "#3654V#45A#4S哇啊啊啊啊啊啊啊啊……！\x02",
        )
    )
    #Auto

    Sleep(8000)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    #C0031
    ChrTalk(
        0x101,
        (
            "#00002F#5P#30W……琪雅………\x02\x03",

            "#00004F哈哈……\x01",
            "撞得还是这么准呢。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 19)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x101, 1, 0, 20)
    BeginChrThread(0x8, 1, 0, 21)
    Sleep(1000)
    BeginChrThread(0xA, 1, 0, 24)
    SetMapObjFrame(0xFF, "point16_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "break00_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "break01_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "break02_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "break03_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "yuka00", 0x2, "to_d")
    SetMapObjFrame(0xFF, "point_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm02_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm03_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm04_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm05_add", 0x2, "to_d")
    Sleep(2500)

    #C0032
    ChrTalk(
        0x101,
        (
            "#00004F#5P#55A#30W好啦，回去吧，\x01",
            "大家还在等着我们呢。\x02\x03",

            "#00002F#40A我就这样抱着你回去，\x01",
            "一定要牢牢抓紧哦。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0033
    ChrTalk(
        0x8,
        "#05818F#12P#25A#40W嗯……嗯……！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x101, 1, 0, 22)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x101, 1, 0, 23)
    Sleep(700)
    OP_68(0, 500, 0, 4000)
    MoveCamera(205, 13, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(11500, 4000)
    OP_6F(0x79)
    Sleep(1500)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    StopSound(111, 1000, 40)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("m9012", 0, 20, 0)
    IdleLoop()
    Return()

    # Function_2_165 end

    def Function_3_1647(): pass

    label("Function_3_1647")

    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_1658():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1658)
    OP_9B(0x1, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
    CancelBlur(0)
    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_3_1647 end

    def Function_4_1683(): pass

    label("Function_4_1683")

    Sleep(300)

    def lambda_168B():
        OP_A6(0xFE, 0x19, 0x0, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_168B)
    Sleep(500)
    Return()

    # Function_4_1683 end

    def Function_5_16A3(): pass

    label("Function_5_16A3")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(111)
    SetChrSubChip(0xFE, 0x2)
    Sleep(111)
    SetChrSubChip(0xFE, 0x3)
    Sleep(333)
    Return()

    # Function_5_16A3 end

    def Function_6_16C7(): pass

    label("Function_6_16C7")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(300)
    Return()

    # Function_6_16C7 end

    def Function_7_16F2(): pass

    label("Function_7_16F2")

    OP_9B(0x0, 0xFE, 0xD, 0x6A4, 0x3E8, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(200)
    Sound(812, 0, 60, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x14)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    Fade(250)
    OP_0D()
    Return()

    # Function_7_16F2 end

    def Function_8_172A(): pass

    label("Function_8_172A")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x13)
    Sleep(167)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    Return()

    # Function_8_172A end

    def Function_9_175C(): pass

    label("Function_9_175C")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0x1)
    Sleep(167)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    Return()

    # Function_9_175C end

    def Function_10_1780(): pass

    label("Function_10_1780")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(167)
    SetChrSubChip(0xFE, 0x6)
    Sleep(167)
    SetChrSubChip(0xFE, 0x7)
    Sleep(500)
    Return()

    # Function_10_1780 end

    def Function_11_17A4(): pass

    label("Function_11_17A4")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(571)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0x8, 0x7)
    BeginChrThread(0x8, 1, 0, 12)
    SetChrSubChip(0xFE, 0xA)
    Sleep(429)
    WaitChrThread(0x8, 1)
    Return()

    # Function_11_17A4 end

    def Function_12_17E3(): pass

    label("Function_12_17E3")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(429)
    Return()

    # Function_12_17E3 end

    def Function_13_1807(): pass

    label("Function_13_1807")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0xC)
    Sleep(571)
    Return()

    # Function_13_1807 end

    def Function_14_1832(): pass

    label("Function_14_1832")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(429)
    Return()

    # Function_14_1832 end

    def Function_15_1856(): pass

    label("Function_15_1856")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(429)
    Return()

    # Function_15_1856 end

    def Function_16_1888(): pass

    label("Function_16_1888")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xC)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xF)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xC)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xF)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xC)
    Return()

    # Function_16_1888 end

    def Function_17_18EF(): pass

    label("Function_17_18EF")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xC)
    Sleep(125)
    SetChrSubChip(0xFE, 0xB)
    Sleep(125)
    SetChrSubChip(0xFE, 0xA)
    Sleep(125)
    SetChrSubChip(0xFE, 0x9)
    Sleep(125)
    SetChrSubChip(0xFE, 0x8)
    Sleep(500)
    Return()

    # Function_17_18EF end

    def Function_18_1921(): pass

    label("Function_18_1921")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0x10)
    Sleep(125)
    SetChrSubChip(0xFE, 0x11)
    Sleep(125)
    SetChrSubChip(0xFE, 0x12)
    Sleep(125)
    SetChrFlags(0xFE, 0x20)
    OP_9D(0xFE, 0x96, 0x0, 0x0, 0x32, 0x3E8)
    ClearChrFlags(0xFE, 0x20)
    Sound(812, 0, 100, 0)

    def lambda_1976():
        OP_A6(0xFE, 0x1E, 0x0, 0x3E8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1976)
    SetChrSubChip(0xFE, 0x13)
    Sleep(50)
    Sound(811, 0, 80, 0)
    Sleep(325)
    Return()

    # Function_18_1921 end

    def Function_19_199B(): pass

    label("Function_19_199B")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(898, 0, 20, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xE)
    Sleep(500)
    Return()

    # Function_19_199B end

    def Function_20_19C5(): pass

    label("Function_20_19C5")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xE)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0x11)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0xE)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0x11)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0xE)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0x11)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0xE)
    Return()

    # Function_20_19C5 end

    def Function_21_1A56(): pass

    label("Function_21_1A56")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x13)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x16)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x13)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x16)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x13)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x16)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x13)
    Return()

    # Function_21_1A56 end

    def Function_22_1AE7(): pass

    label("Function_22_1AE7")

    Fade(500)
    OP_68(-400, 950, 400, 800)
    SetCameraDistance(11000, 800)
    Sound(802, 0, 50, 0)
    Sound(898, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xF)
    SetChrFlags(0x8, 0x8)
    OP_0D()
    SetChrSubChip(0xFE, 0xF)
    Sleep(167)
    SetChrSubChip(0xFE, 0xC)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xE)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xC)
    Sleep(167)
    SetChrSubChip(0xFE, 0xC)
    Sleep(500)
    SetChrSubChip(0xFE, 0x10)
    Sleep(167)
    SetChrSubChip(0xFE, 0x11)
    Sleep(167)
    SetChrSubChip(0xFE, 0x10)
    Sleep(167)
    SetChrSubChip(0xFE, 0xF)
    Sleep(833)
    Return()

    # Function_22_1AE7 end

    def Function_23_1B78(): pass

    label("Function_23_1B78")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    OP_93(0xFE, 0xB4, 0x0)
    Sleep(700)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x1)
    Return()

    # Function_23_1B78 end

    def Function_24_1BBC(): pass

    label("Function_24_1BBC")

    Sleep(100)
    Sound(1022, 0, 100, 0)
    Sleep(3300)
    Sound(1022, 0, 100, 0)
    Sleep(3300)
    Sound(1022, 0, 100, 0)
    Sleep(3400)
    Sound(1022, 0, 100, 0)
    Sleep(1500)
    Sound(934, 0, 70, 0)
    Sound(1002, 0, 100, 0)
    Return()

    # Function_24_1BBC end

    def Function_25_1BF0(): pass

    label("Function_25_1BF0")

    Sound(934, 0, 100, 0)
    Sleep(1000)
    Sound(222, 0, 50, 0)
    Sleep(500)
    Sound(928, 0, 100, 0)
    Return()

    # Function_25_1BF0 end

    SaveToFile()

Try(main)
