from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4100.bin",                # FileName
        "e4100",                    # MapName
        "e4100",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, -74000, 0, -2500, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4100",                  # 0
        "神狼蔡特",               # 1
        "守护骑士瓦吉",           # 2
        "守护骑士凯文",           # 3
        "随从骑士莉丝",           # 4
        "正骑士阿巴斯",           # 5
        "神狼蔡特",               # 6
        "梅尔卡瓦",               # 7
        "梅尔卡瓦",               # 8
        "梅尔卡瓦光学迷彩",       # 9
        "梅尔卡瓦光学迷彩",       # 10
        "SE控制",                 # 11
    ))

    DeclNpc(0,       0,       0,       0,    229,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(568, 0)                                        # 0

    ScpFunction((
        "Function_0_238",          # 00, 0
        "Function_1_248",          # 01, 1
        "Function_2_25E",          # 02, 2
        "Function_3_346D",         # 03, 3
        "Function_4_34D9",         # 04, 4
        "Function_5_3556",         # 05, 5
        "Function_6_357B",         # 06, 6
        "Function_7_35A0",         # 07, 7
        "Function_8_35CD",         # 08, 8
        "Function_9_361C",         # 09, 9
        "Function_10_3695",        # 0A, 10
        "Function_11_370E",        # 0B, 11
        "Function_12_3742",        # 0C, 12
        "Function_13_375E",        # 0D, 13
        "Function_14_37B6",        # 0E, 14
        "Function_15_3821",        # 0F, 15
        "Function_16_38B0",        # 10, 16
        "Function_17_3908",        # 11, 17
        "Function_18_3973",        # 12, 18
        "Function_19_3A02",        # 13, 19
        "Function_20_3A1A",        # 14, 20
        "Function_21_3A59",        # 15, 21
        "Function_22_3AA4",        # 16, 22
        "Function_23_3B1F",        # 17, 23
        "Function_24_3B49",        # 18, 24
        "Function_25_3B89",        # 19, 25
        "Function_26_3BB2",        # 1A, 26
        "Function_27_3BCA",        # 1B, 27
    ))


    def Function_0_238(): pass

    label("Function_0_238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_247")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_247")

    Return()

    # Function_0_238 end

    def Function_1_248(): pass

    label("Function_1_248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_25D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_25D")

    Return()

    # Function_1_248 end

    def Function_2_25E(): pass

    label("Function_2_25E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xFE, 0x0)
    LoadChrToIndex("chr/ch03100.itc", 0x1E)
    LoadChrToIndex("chr/ch06710.itc", 0x1F)
    LoadChrToIndex("chr/ch11400.itc", 0x20)
    LoadChrToIndex("chr/ch11500.itc", 0x21)
    LoadChrToIndex("apl/ch51620.itc", 0x22)
    LoadChrToIndex("apl/ch51614.itc", 0x23)
    LoadChrToIndex("apl/ch51615.itc", 0x24)
    LoadChrToIndex("chr/ch00056.itc", 0x25)
    LoadChrToIndex("apl/ch51619.itc", 0x26)
    SoundLoad(2917)
    SoundLoad(2918)
    SoundLoad(2919)
    SoundLoad(2920)
    SoundLoad(962)
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(496)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis413.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10401.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12100.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13800.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04300.itp")
    SetChrPos(0x101, -129880, 4000, -26390, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x1)
    SetChrFlags(0x101, 0x2000)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1000)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x2, 0x8)
    OP_49()
    SetChrPos(0x8, -127870, 4000, -35110, 0)
    OP_93(0x8, 0x5A, 0x0)
    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0xA, 0x32, 0x1, 0x20)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x8000)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1C84), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x2, 0x97, 0xAA, 0x1, 0x20)
    OP_D3(0x101, 0x2, "Null_senaka(42)")
    SetMapObjFrame(0x2, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x2, "879mabuta:Layer2(44)", 0x0, 0x1)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_78(0x0, 0xE)
    OP_78(0x1, 0xF)
    OP_78(0x4, 0x10)
    OP_78(0x5, 0x11)
    SetChrPos(0xE, -136010, -1150, -71530, 0)
    SetChrPos(0x10, -136010, -1150, -71530, 0)
    SetChrPos(0xF, -123270, -1350, -76920, 0)
    SetChrPos(0x11, -123270, -1350, -76920, 0)
    OP_93(0xE, 0x0, 0x15E)
    OP_93(0x10, 0x0, 0x15E)
    OP_93(0xF, 0x0, 0x15E)
    OP_93(0x11, 0x0, 0x15E)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x7, 0x1000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1000, 0, 0, 0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 2000, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 3000, 0, 0, 0)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 4000, 0, 0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    OP_70(0x3, 0x0)
    Sound(132, 2, 100, 0)
    BeginChrThread(0x12, 1, 0, 20)
    Sleep(2000)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_68(-207000, 1650, -16820, 0)
    MoveCamera(333, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(74640, 0)
    SetChrPos(0x8, -225000, 0, -24000, 0)
    BeginChrThread(0x8, 0, 0, 3)
    OP_68(-165050, 1650, -5550, 6000)
    MoveCamera(312, 34, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(56890, 6000)
    PlaceName2(340, 200, "c_plac65", 0x0, 0)
    Sleep(4500)
    StopSound(962, 2000, 40)
    Sleep(1000)
    FadeToDark(500, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x0)
    SetChrPos(0x8, -132000, 4000, -31000, 0)
    OP_93(0x8, 0x46, 0x0)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    SetChrFlags(0x8, 0x1)
    OP_93(0x101, 0x0, 0x0)
    SetChrSubChip(0x101, 0x3)
    OP_68(-129830, 6900, -28710, 0)
    MoveCamera(262, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    Sleep(1000)
    BeginChrThread(0x12, 1, 0, 21)
    FadeToBright(500, 0)
    SetCameraDistance(15390, 6000)
    Sleep(500)
    BeginChrThread(0x101, 0, 0, 4)
    Sleep(1000)
    OP_68(-129750, 7300, -28810, 4500)
    MoveCamera(263, 11, 0, 4500)
    OP_6E(600, 4500)
    OP_0D()
    Sleep(1000)
    SetChrPos(0xD, -128370, 7200, -29090, 0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x101, 0)
    Sleep(500)
    Sleep(500)
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x101,
        (
            "#00008F#5P这里是……\x01",
            "共和国一侧的国境啊。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 5)
    Sleep(1500)

    #C0002
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P逃到了这里，国防军的\x01",
            "那些家伙应该没办法追来了。\x02",
        )
    )

    WaitChrThread(0x8, 0)
    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P先休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)
    Sleep(150)

    #C0004
    ChrTalk(
        0x101,
        (
            "#00006F#12P#N谢谢了，蔡特，\x01",
            "这次真是多亏有你相救……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0005
    ChrTalk(
        0x101,
        "#00011F#5P哎……\x02",
    )

    CloseMessageWindow()
    OP_68(-146110, 10500, -23540, 3000)
    MoveCamera(260, 9, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15390, 3000)
    OP_6F(0x79)

    #C0006
    ChrTalk(
        0x101,
        "#00007F#6P#N那是……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0007
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#6P#N笼罩着克洛斯贝尔市，\x01",
            "类似于『结界』的东西。\x02\x03",

            "『得到许可』的事物\x01",
            "可以自由出入……\x02\x03",

            "但没有得到许可的事物\x01",
            "绝对不可能通行穿越。\x02\x03",

            "人或交通工具都是一样……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0008
    ChrTalk(
        0x101,
        "#00013F#6P#N……竟然有那种东西……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-129830, 6900, -28710, 0)
    MoveCamera(262, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    Fade(500)
    OP_0D()
    OP_68(-129830, 6900, -28710, 80000)
    MoveCamera(235, 19, 0, 80000)
    OP_6E(600, 80000)
    SetCameraDistance(20000, 80000)
    Sleep(500)

    #C0009
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P另外，『灵智之草』正在整个\x01",
            "克洛斯贝尔地区内疯狂绽放。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P甚至可以说，\x01",
            "如今的克洛斯贝尔已与\x01",
            "『至宝』一体化了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    #C0011
    ChrTalk(
        0x101,
        (
            "#00008F#12P那个『灵智之草』\x01",
            "究竟是什么东西？\x02\x03",

            "听说它与流动在地下的\x01",
            "七耀脉存在着一定关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P当年的『幻之至宝』为了了解\x01",
            "人类与地上的事物而开放此花，\x01",
            "可以把它理解为至宝的眼睛。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P『至宝』与精神世界通过此物相连接，\x01",
            "会使周围的空间产生扭曲。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P原本不会出现在这个世界的\x01",
            "『幻兽』相继出现，\x01",
            "大概也是由于这个缘故。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00006F#12P原来如此……\x02\x03",

            "#00008F……『Ｄ∴Ｇ教团』当年曾\x01",
            "举行过种种惨无人道的仪式……\x02\x03",

            "#00013F他们会在仪式中使用\x01",
            "以灵智之草为原料的『真知』，\x01",
            "也是有原因的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P嗯，众多因实验而牺牲的人\x01",
            "拥有大量知识与人格……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P那些庞大的情报恐怕正是通过\x01",
            "『真知』，传送给沉睡在\x01",
            "『太阳堡垒』的『她』。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P传送过去的情报会自动组织，\x01",
            "形成产生高等人格\x01",
            "所需的苗床……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P就这样，经过长达五百年的时光，\x01",
            "『至宝』的『核心』终于苏醒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00006F#12P#40W………………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0021
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P我能告诉你的\x01",
            "也只有这些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P『他们』处心积虑地制定了完善的计划，\x01",
            "最终导致了如今的状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P在这种状况下，\x01",
            "可供你选择的路实在是相当少。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P就这样逃往异国，\x01",
            "直到事态的热度慢慢消退如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00004F#12P哈哈，说得也是啊……\x02\x03",

            "#00008F……如果逃亡到卡尔瓦德，\x01",
            "可以投奔到叔叔家，\x01",
            "或许是个不错的选择呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-130699, 6500, -28440, 0)
    MoveCamera(264, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17590, 0)
    Fade(500)
    OP_0D()
    Sleep(300)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    #C0026
    ChrTalk(
        0x101,
        (
            "#00006F#6P不过，还是不要了。\x02\x03",

            "#00000F因为我还没有确认到\x01",
            "自己最想了解的真相。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P什么……？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00003F#6P为了确认它……\x01",
            "我需要很多人的力量。\x02\x03",

            "这包括艾莉、缇欧、兰迪，\x01",
            "以及其他众人的力量……\x02\x03",

            "#00008F为此……\x01",
            "我也必须要回去。\x02\x03",

            "#00000F真是不好意思，\x01",
            "枉你特意把我送到这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P你要确认的真相是什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#00004F#6P那还用问吗？\x02",
    )

    CloseMessageWindow()
    OP_68(-129470, 6300, -28970, 0)
    MoveCamera(263, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12800, 0)
    Fade(500)
    OP_0D()
    TurnDirection(0x101, 0xD, 500)
    Sleep(300)

    #C0032
    ChrTalk(
        0x101,
        (
            "#00008F#12P抛开她的力量与来历不谈……\x02\x03",

            "#00000F我只想知道……\x01",
            "琪雅那孩子究竟想怎么样。\x02\x03",

            "如果不把她夺回，恐怕很难\x01",
            "让她吐露真实想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#N…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0034
    ChrTalk(
        0x101,
        (
            "#00006F#12P而且，也许琪雅正在承受\x01",
            "连当年的『至宝』\x01",
            "都不堪忍受的重压……\x02\x03",

            "我又怎能将她置于\x01",
            "那样的环境中。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0035
    ChrTalk(
        0x101,
        (
            "#00010F#12P#4S就算要把总统和亚里欧斯先生打倒，\x01",
            "我也必须将琪雅带回来！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#N呵呵……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    StopBGM(0xFA0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x2000)
    SetChrFlags(0xC, 0x2000)
    SetChrFlags(0xA, 0x2000)
    SetChrFlags(0xB, 0x2000)
    BeginChrThread(0x9, 0, 0, 7)
    BeginChrThread(0xC, 0, 0, 8)
    BeginChrThread(0xA, 0, 0, 9)
    BeginChrThread(0xB, 0, 0, 10)
    Sleep(100)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xD, -133920, 8200, -35070, 0)
    OP_C9(0x0, 0x80000000)

    #N0037
    NpcTalk(
        0x9,
        "少年的声音",
        "#11P#2917V#30W#38A#N啊哈哈，真是个疼爱孩子的爸爸呢。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x101,
        "#00011F#12P哎……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)
    OP_68(-137840, 4800, -46130, 0)
    MoveCamera(235, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18330, 0)
    Fade(500)
    OP_68(-133770, 4600, -39110, 4000)
    MoveCamera(227, 20, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(19660, 4000)
    BeginChrThread(0x8, 0, 0, 11)
    BeginChrThread(0x101, 0, 0, 12)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_6F(0x79)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)

    #C0039
    ChrTalk(
        0x101,
        (
            "#00005F#6P#N瓦吉，你为何会……\x02\x03",

            "#00011F阿巴斯……\x01",
            "连莉丝小姐……还有你也在！？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("阿巴斯")

    #A0040
    AnonymousTalk(
        0xFF,
        "好久不见了，班宁斯。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("莉丝修女")

    #A0041
    AnonymousTalk(
        0xFF,
        "好久不见。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("凯文神父")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            "哟，我们都已经\x01",
            "四个月没见了吧？\x02\x03",

            "看来你还记得我，真让人开心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)

    #C0043
    ChrTalk(
        0x101,
        (
            "#00006F#6P#N记得你和莉丝小姐\x01",
            "隶属于教会的『星杯骑士团』……\x02\x03",

            "#00007F瓦吉，莫非你也……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)
    #Sound(2430, 255, 100, 0)    #voice#Lazy

    #N0044
    NpcTalk(
        0x9,
        "瓦吉",
        "#10404F#5P呵呵……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7356", 0)
    OP_68(-133770, 4600, -39110, 100000)
    MoveCamera(227, 19, 0, 100000)
    OP_6E(600, 100000)
    SetCameraDistance(16860, 100000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0045
    AnonymousTalk(
        0x9,
        (
            "#2918V#30W七耀教会·星杯骑士团成员。\x02\x03",

            "#2919V守护骑士第九位──\x01",
            "『苍之圣典』瓦吉·赫米斯菲亚。\x02\x03",

            "#2920V今后还请继续指教哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB68)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_C9(0x1, 0x80000000)

    #C0046
    ChrTalk(
        0x101,
        "#00011F#6P………………………（目瞪口呆）\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xC,
        (
            "#12102F#5P顺便一提，\x01",
            "我是骑士团中的一名正骑士。\x02\x03",

            "辅佐瓦吉就是我的主要任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#00015F#6P……啊啊！先等一下！事情发生得\x01",
            "太过突然，我的脑子一时还有点混乱。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0049
    ChrTalk(
        0x101,
        (
            "#00011F#6P说、说起来……\x02\x03",

            "在初次见到莉丝小姐时，\x01",
            "你们两个好像什么话都没有说……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xB,
        (
            "#13806F#11P……抱歉，\x01",
            "我们当时是故意装作互不相识的。\x02\x03",

            "#13802F因为赫米斯菲亚大人的\x01",
            "潜入调查是极秘任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "#10404F#5P正是如此，多亏有她前来，\x01",
            "艾拉尔达大主教的注意力\x01",
            "完全被吸引开了。\x02\x03",

            "#10402F哎呀呀，真是帮了大忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xB,
        "#13804F#11P能发挥作用，是我的荣幸。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xA,
        (
            "#04306F#11P哈，因为无论怎么看，\x01",
            "莉丝都不像是个\x01",
            "普通的修女呢。\x02\x03",

            "#04302F大主教肯定会感到不知所措。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        (
            "#13803F#11P……过誉了。\x02\x03",

            "#13811F话说回来，我觉得凯文\x01",
            "根本就没有这样说别人的资格呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0055
    ChrTalk(
        0x101,
        (
            "#00012F#6P（他们四人……好像没有\x01",
            "  一个像是普通的神职人员呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "#10404F#5P好了，新一次的\x01",
            "自我介绍就到此为止吧。\x02\x03",

            "#10400F我们出现在此地，\x01",
            "是因为它的召唤。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x104, 0x1F4)

    #C0057
    ChrTalk(
        0x101,
        "#00011F#6P蔡特吗……？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 5)
    WaitChrThread(0x8, 0)
    SetChrPos(0xD, -132240, 7300, -35100, 0)

    #C0058
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#N嗯，是我叫他们来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#N我想，如果你的决意已经不容动摇，\x01",
            "便需要可靠的协助者。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#00005F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_1CE6():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CE6)
    BeginChrThread(0x8, 0, 0, 6)
    SetChrPos(0xD, -133920, 8200, -35070, 0)
    Sleep(500)

    #C0061
    ChrTalk(
        0x9,
        (
            "#10406F#5P骑士团事先就已\x01",
            "派我潜入克洛斯贝尔……\x02\x03",

            "#10401F由此可见，骑士团对此次事态\x01",
            "有着一定程度的预测。\x02\x03",

            "只是，关于库罗伊斯家的阴谋，\x01",
            "还有琪雅的真实身份，\x01",
            "一直都有很多不明之处。\x02\x03",

            "日前与它再会之后，\x01",
            "总算是了解了整个事件的内幕。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xC,
        (
            "#12100F#5P不过，『幻之至宝』\x01",
            "已经毁灭，取而代之的则是\x01",
            "由人类创造的新至宝……\x02\x03",

            "对于以回收『古代遗物』为任务的骑士团而言，\x01",
            "目前的情况超出了职责范围。\x02\x03",

            "我们已经不具备可以\x01",
            "继续介入此事的理由。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        (
            "#04303F#11P话虽如此，但既然\x01",
            "此次事态与『结社』存在关联，\x01",
            "我们也不能放任不管……\x02\x03",

            "#04300F所以，我们希望将『你』\x01",
            "当作介入的理由。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00001F#6P……！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "#10404F#5P事情就是这样。\x02\x03",

            "#10402F我们准备以向你\x01",
            "提供协助的形式\x01",
            "来介入此次事件。\x02\x03",

            "如何？罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#00008F#6P#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0067
    ChrTalk(
        0x101,
        (
            "#00006F#6P我要先确认一件事。\x02\x03",

            "#00013F你们……\x01",
            "准备如何处理琪雅？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0068
    ChrTalk(
        0x9,
        "#10408F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        "#04306F#11P……真是个很难回答的问题啊。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        (
            "#13808F#11P不过，敷衍式的回答\x01",
            "恐怕毫无意义。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "#12100F#5P嗯，还是坦诚告知\x01",
            "真实情况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "#10403F#5P……是啊。\x02\x03",

            "#10401F老实说，\x01",
            "『零之至宝』的危险性\x01",
            "恐怕远超『空之至宝』。\x02\x03",

            "它目前还没有展示出\x01",
            "真正的力量，\x01",
            "但却已经造成如此严重的状况了。\x02\x03",

            "#10406F你知道大陆诸国\x01",
            "目前的情况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#00005F#6P不……\x02\x03",

            "#00001F……只是听说了帝国\x01",
            "开始内战的传闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "#04306F#11P至于内战爆发的直接原因，\x01",
            "正是由于进攻克洛斯贝尔的\x01",
            "帝国军师团全军覆没。\x02\x03",

            "#04308F帝国军的自尊心很强，\x01",
            "在受挫之后，又陆续派出了多个师团，\x01",
            "但全都被那些智能兵器打得溃不成军……\x02\x03",

            "#04301F趁着帝国军陷入混乱的机会，\x01",
            "贵族势力的联合军发起闪电战，\x01",
            "迅速占领了帝都。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0075
    ChrTalk(
        0xC,
        (
            "#12100F#5P最终，铁血宰相遭到枪击而倒下，\x01",
            "从此下落不明……\x02\x03",

            "覆盖帝国全域的内战\x01",
            "已经开始进入持久战了。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xB,
        (
            "#13803F#11P至于共和国，\x01",
            "以克洛斯贝尔的事件为开端，\x01",
            "发生了经济恐慌……\x02\x03",

            "#13801F恐怖行动频繁发生，\x01",
            "政府已经发表了紧急局势宣言。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#00006F#6P……是吗……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#10403F#5P而其它国家自然也\x01",
            "无法完全避免恐慌与混乱。\x02\x03",

            "特别是那些以往一直被\x01",
            "帝国和共和国所控制的地区，\x01",
            "也已经开始了充满火药味的行动。\x02\x03",

            "#10408F在这种情况下，迪塔总统\x01",
            "已经开始鼓动各地势力加盟了。\x02\x03",

            "#10401F劝说他们以克洛斯贝尔为盟主，\x01",
            "共同建立新的秩序。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x101,
        (
            "#00013F#6P…………………………………\x02\x03",

            "#00003F……显然是倚仗着\x01",
            "『至宝』的力量吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "#10404F#5P当然。\x02\x03",

            "那可是能够轻松击退号称\x01",
            "大陆最强的帝国军的力量。\x02\x03",

            "#10408F另外，虽然他们如今只有\x01",
            "『结社』提供的三架智能兵器……\x02\x03",

            "#10402F但如果今后将其增产，\x01",
            "并全部注入『至宝』的力量，\x01",
            "随后派往整个大陆，又会如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#00010F#6P唔……\x02\x03",

            "#00007F……琪雅……\x01",
            "那孩子绝对不会做出那种事！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xC,
        (
            "#12100F#5P顺便一说，那些智能兵器\x01",
            "并不是由至宝操纵的。\x02\x03",

            "它们只是得到了至宝的力量，\x01",
            "可以理解为能够自律行动的『守护者』。\x02\x03",

            "和那个名叫玲的女孩所操控的那架\x01",
            "叫做『帕蒂尔·玛蒂尔』的机体相同。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        "#00011F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "#04306F#11P……也就是说，\x01",
            "那些智能兵器只是在擅自行动，\x01",
            "和那孩子的意志完全无关吧？\x02\x03",

            "#04301F不仅如此，而且很有可能\x01",
            "正在被其他人所利用。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xB,
        (
            "#13806F#11P和琪雅的意志无关……\x02\x03",

            "#13808F又拥有那么强大的『力量』，\x01",
            "这种危险性确实不能无视呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#00008F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_68(-132290, 5000, -37670, 0)
    MoveCamera(1, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    Fade(500)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0087
    ChrTalk(
        0x101,
        (
            "#00003F#11P我明白你们的想法了。\x02\x03",

            "#00001F哪怕目的不同也无所谓，\x01",
            "我想请你们协助我。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0088
    ChrTalk(
        0x9,
        (
            "#10405F#6P哎……？\x02\x03",

            "#10402F本以为你肯定会\x01",
            "严词拒绝这个提议呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00006F#11P目前的事态确实不是\x01",
            "我一个人能够应对的……\x02\x03",

            "#00008F拖得越久，那孩子就会受越多的苦，\x01",
            "因此必须要尽早解决……\x02\x03",

            "#00010F……但是！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(812, 0, 100, 0)
    SetCameraDistance(14300, 500)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x6)
    OP_0D()
    Sleep(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13000, 250)
    Sound(802, 0, 70, 0)
    SetChrSubChip(0x101, 0x7)
    OP_6F(0x79)
    CancelBlur(0)
    OP_82(0x96, 0x0, 0xBB8, 0x1F4)

    #C0090
    ChrTalk(
        0x101,
        (
            "#00007F#11P我话说在前！如果你们\x01",
            "擅自定下处理琪雅的方式！\x02\x03",

            "我无论如何也会\x01",
            "全力阻止的！\x02\x03",

            "#00003F不只是我！\x01",
            "艾莉、缇欧、兰迪\x01",
            "肯定也会说出同样的话！\x02\x03",

            "#00013F这和道理或法律完全无关！\x01",
            "只是因为我们是那孩子的『监护人』！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xB,
        "#13805F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        "#12102F#6P………嗯……………\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "#04304F#6P哈哈，长着一张文弱清秀的脸，\x01",
            "却是个相当热血的小兄弟呢。\x02\x03",

            "#04302F瓦吉，我总算明白\x01",
            "你为何会对他感兴趣了。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "#10409F#6P呵呵，就算说我爱他\x01",
            "也不为过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#00010F#11P瓦吉！我是很认真的！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_68(-133770, 4600, -39110, 0)
    MoveCamera(227, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16860, 0)
    Fade(500)
    OP_68(-133450, 4400, -39970, 2000)
    MoveCamera(227, 22, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14450, 2000)
    OP_0D()
    BeginChrThread(0x9, 0, 0, 25)
    WaitChrThread(0x9, 0)
    Sleep(800)

    #C0096
    ChrTalk(
        0x9,
        (
            "#10403F#5P身为星杯骑士团的骑士，\x01",
            "我以女神爱德丝的名义发誓──\x02\x03",

            "关于那孩子的处理方式，\x01",
            "我们一定会征询\x01",
            "你们的意见。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-133770, 4600, -39110, 1500)
    MoveCamera(227, 19, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(16860, 1500)
    Sleep(500)
    SetChrSubChip(0x9, 0x0)
    Sleep(130)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x1000)
    OP_6F(0x79)

    #C0097
    ChrTalk(
        0x9,
        (
            "#10406F#5P……以我们的立场来说，\x01",
            "最多也只能承诺到这种程度了。\x02\x03",

            "#10402F意下如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00006F#6P嗯……这样就足够了。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xC,
        "#12102F#5P已经做出决定了啊。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        (
            "#04304F#11P好，那我们就\x01",
            "赶快开始行动吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    BeginChrThread(0xA, 2, 0, 26)
    Sound(812, 0, 100, 0)
    BeginChrThread(0x12, 1, 0, 22)
    StopSound(132, 1000, 30)
    OP_68(-134270, 4400, -39100, 2500)
    MoveCamera(227, 19, 0, 2500)
    OP_6E(600, 2500)
    SetCameraDistance(16860, 2500)
    OP_6F(0x79)

    #C0101
    ChrTalk(
        0x101,
        "#00005F#6P什、什么……？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P嗯……\x01",
            "真是让人怀念的声音啊。\x02\x03",

            "教会的『天之车』吗？\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    OP_75(0x6, 0x1, 0x0)
    OP_75(0x7, 0x1, 0x0)
    SetChrPos(0xE, -136010, 41150, -71530, 0)
    SetChrPos(0x10, -136010, 41150, -71530, 0)
    SetChrPos(0xF, -123270, 46350, -76920, 0)
    SetChrPos(0x11, -123270, 46350, -76920, 0)
    BeginChrThread(0xE, 0, 0, 13)
    BeginChrThread(0xF, 0, 0, 16)
    BeginChrThread(0x101, 1, 0, 19)
    BeginChrThread(0x12, 1, 0, 23)
    BeginChrThread(0xA, 2, 0, 27)
    OP_68(-126850, 7200, -36760, 3000)
    MoveCamera(185, -18, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(9560, 3000)
    Sleep(1500)
    WaitChrThread(0xA, 2)

    def lambda_3082():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3082)
    Sleep(30)

    def lambda_3092():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3092)
    Sleep(30)

    def lambda_30A2():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_30A2)
    Sleep(30)

    def lambda_30B2():
        OP_93(0xC, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_30B2)
    Sleep(30)

    def lambda_30C2():
        OP_93(0xB, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_30C2)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xB, 0)
    OP_6F(0x79)
    OP_68(-126020, 9000, -47760, 9000)
    MoveCamera(188, 23, 0, 9000)
    OP_6E(600, 9000)
    SetCameraDistance(24000, 9000)
    BeginChrThread(0x8, 0, 0, 5)
    Sleep(4000)
    Sound(942, 0, 100, 0)
    Sleep(2000)
    Sound(942, 0, 100, 0)
    Sleep(2000)
    Sleep(500)

    #C0103
    ChrTalk(
        0x101,
        "#00011F#12P#N飞、飞艇……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_6F(0x79)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    BeginChrThread(0x12, 1, 0, 24)
    Fade(500)
    OP_68(-132090, 5900, -41380, 0)
    MoveCamera(359, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Sleep(300)

    #C0104
    ChrTalk(
        0xB,
        (
            "#13804F#5P这是星杯骑士团所使用的作战艇，\x01",
            "名为『梅尔卡瓦』。\x02\x03",

            "#13802F不仅拥有隐形机能，\x01",
            "而且还配备了光学迷彩机能。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "#10403F#5P我们将要驾驶它，\x01",
            "秘密潜入克洛斯贝尔的领空……\x02\x03",

            "#10400F做好心理准备了吗？罗伊德。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0106
    ChrTalk(
        0x101,
        "#00007F#11P#4S嗯！当然！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-167100, 6900, -14880, 0)
    MoveCamera(262, 6, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(52800, 0)
    Fade(500)
    SetCameraDistance(48800, 20000)
    OP_0D()
    StopSound(496, 1000, 30)
    StopSound(497, 1000, 30)
    Sleep(800)
    SetMessageWindowPos(0, 170, -1, -1)

    #A0107
    AnonymousTalk(
        0x101,
        (
            "#00003F#6P#N#30W（琪雅……\x01",
            "  ……还有大家……）\x02\x03",

            "#00013F#30W（一定要等我啊……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(48800, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_24(0x3C2)
    OP_24(0x84)
    OP_24(0x1F1)
    OP_24(0x1F0)
    OP_29(0xAE, 0x1, 0x2)
    OP_29(0xAE, 0x4, 0x10)
    SubItemNumber('蓝花', 1)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x22, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_25E end

    def Function_3_346D(): pass

    label("Function_3_346D")

    SetChrPos(0xFE, -250000, 0, -28000, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -225000, 0, -24000)
    OP_9F(0x1, -210000, 0, -20750)
    OP_9F(0x1, -193000, 0, -15500)
    OP_9F(0x1, -173000, 0, -10500)
    OP_9F(0x1, -130000, 0, -5220)
    OP_9F(0x2, 0xFE, 20000, 0x6)
    Return()

    # Function_3_346D end

    def Function_4_34D9(): pass

    label("Function_4_34D9")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    OP_D3(0x101, 0xFF, "")
    Sound(809, 0, 40, 0)
    OP_9D(0xFE, 0xFFFDFF4E, 0xFA0, 0xFFFF92A0, 0xFA, 0x3E8)
    Sound(326, 0, 40, 0)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_4_34D9 end

    def Function_5_3556(): pass

    label("Function_5_3556")

    ClearMapObjFlags(0x2, 0x20)
    OP_79(0x2)
    OP_71(0x2, 0x1A4, 0x1AE, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0x1AE, 0x1D6, 0x0, 0x20)
    Return()

    # Function_5_3556 end

    def Function_6_357B(): pass

    label("Function_6_357B")

    ClearMapObjFlags(0x2, 0x20)
    OP_79(0x2)
    OP_71(0x2, 0x1D6, 0x1E0, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    Return()

    # Function_6_357B end

    def Function_7_35A0(): pass

    label("Function_7_35A0")

    SetChrPos(0xFE, -137500, 4019, -45600, 30)
    OP_95(0xFE, -133390, 4000, -39760, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_7_35A0 end

    def Function_8_35CD(): pass

    label("Function_8_35CD")

    SetChrPos(0xFE, -138450, 3480, -47600, 90)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -137500, 4019, -45600)
    OP_9F(0x2, 0xFE, 2000, 0x2)
    OP_95(0xFE, -132640, 4000, -40680, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_8_35CD end

    def Function_9_361C(): pass

    label("Function_9_361C")

    SetChrPos(0xFE, -144000, -40, -56500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x0, 0x0)
    OP_9F(0x1, -144000, 600, -54730)
    OP_9F(0x1, -141500, 2350, -50000)
    OP_9F(0x1, -139000, 3300, -48000)
    OP_9F(0x1, -137500, 4019, -45600)
    OP_9F(0x2, 0xFE, 3000, 0x2)
    OP_95(0xFE, -134290, 4000, -38890, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_9_361C end

    def Function_10_3695(): pass

    label("Function_10_3695")

    SetChrPos(0xFE, -144000, 600, -54730, 30)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -144000, 600, -54730)
    OP_9F(0x1, -141500, 2350, -50000)
    OP_9F(0x1, -139000, 3300, -48000)
    OP_9F(0x1, -137500, 4019, -45600)
    OP_9F(0x2, 0xFE, 3000, 0x2)
    OP_95(0xFE, -135320, 4000, -38530, 2000, 0x0)
    OP_93(0xFE, 0x23, 0x1F4)
    Return()

    # Function_10_3695 end

    def Function_11_370E(): pass

    label("Function_11_370E")

    OP_71(0x2, 0x1D6, 0x1E0, 0x0, 0x0)
    SetChrPos(0x8, -131250, 4000, -31250, 215)
    OP_93(0x8, 0xD7, 0x1F4)
    OP_79(0x2)
    OP_71(0x2, 0x3D, 0x64, 0x0, 0x20)
    Return()

    # Function_11_370E end

    def Function_12_3742(): pass

    label("Function_12_3742")

    OP_95(0xFE, -130300, 4000, -36350, 2000, 0x0)
    OP_93(0xFE, 0xD7, 0x1F4)
    Return()

    # Function_12_3742 end

    def Function_13_375E(): pass

    label("Function_13_375E")

    Sleep(1000)
    OP_71(0x4, 0x65, 0xA0, 0x1, 0x20)
    BeginChrThread(0xE, 1, 0, 14)
    BeginChrThread(0x10, 1, 0, 14)
    Sleep(4000)
    Sound(202, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x4)
    OP_75(0x0, 0x1, 0x0)
    OP_75(0x0, 0x2, 0x1F4)
    Sleep(500)
    Sound(920, 0, 100, 0)
    OP_75(0x4, 0x1, 0x3E8)
    OP_75(0x6, 0x2, 0x1F4)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x10, 1)
    Return()

    # Function_13_375E end

    def Function_14_37B6(): pass

    label("Function_14_37B6")

    OP_96(0xFE, 0xFFFDECB6, 0x3E8, 0xFFFEE896, 0x1770, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0x1F4, 0xFFFEE896, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0x0, 0xFFFEE896, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFE0C, 0xFFFEE896, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFC18, 0xFFFEE896, 0x3E8, 0x1)
    BeginChrThread(0xFE, 3, 0, 15)
    Return()

    # Function_14_37B6 end

    def Function_15_3821(): pass

    label("Function_15_3821")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38AF")
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFB50, 0xFFFEE896, 0x190, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFAEC, 0xFFFEE896, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFB50, 0xFFFEE896, 0xC8, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFCE0, 0xFFFEE896, 0x190, 0x1)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFD44, 0xFFFEE896, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFDECB6, 0xFFFFFCE0, 0xFFFEE896, 0xC8, 0x1)
    Jump("Function_15_3821")

    label("loc_38AF")

    Return()

    # Function_15_3821 end

    def Function_16_38B0(): pass

    label("Function_16_38B0")

    Sleep(2000)
    OP_71(0x5, 0x65, 0xA0, 0x1, 0x20)
    BeginChrThread(0xF, 1, 0, 17)
    BeginChrThread(0x11, 1, 0, 17)
    Sleep(4000)
    Sound(202, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x4)
    OP_75(0x1, 0x1, 0x0)
    OP_75(0x1, 0x2, 0x1F4)
    Sleep(500)
    Sound(920, 0, 100, 0)
    OP_75(0x5, 0x1, 0x3E8)
    OP_75(0x7, 0x2, 0x1F4)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x11, 1)
    Return()

    # Function_16_38B0 end

    def Function_17_3908(): pass

    label("Function_17_3908")

    OP_96(0xFE, 0xFFFE1E7A, 0x3E8, 0xFFFED388, 0x1770, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0x1F4, 0xFFFED388, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0x0, 0xFFFED388, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFE0C, 0xFFFED388, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFC18, 0xFFFED388, 0x3E8, 0x1)
    BeginChrThread(0xFE, 3, 0, 18)
    Return()

    # Function_17_3908 end

    def Function_18_3973(): pass

    label("Function_18_3973")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A01")
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFB50, 0xFFFED388, 0x190, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFAEC, 0xFFFED388, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFB50, 0xFFFED388, 0xC8, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFCE0, 0xFFFED388, 0x190, 0x1)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFD44, 0xFFFED388, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0xFFFE1E7A, 0xFFFFFCE0, 0xFFFED388, 0xC8, 0x1)
    Jump("Function_18_3973")

    label("loc_3A01")

    Return()

    # Function_18_3973 end

    def Function_19_3A02(): pass

    label("Function_19_3A02")

    Sleep(1000)
    OP_95(0xFE, -130310, 4100, -40610, 2000, 0x0)
    Return()

    # Function_19_3A02 end

    def Function_20_3A1A(): pass

    label("Function_20_3A1A")

    Sound(962, 2, 10, 0)
    Sleep(400)
    OP_25(0x3C2, 0xF)
    Sleep(400)
    OP_25(0x3C2, 0x14)
    Sleep(400)
    OP_25(0x3C2, 0x19)
    Sleep(400)
    OP_25(0x3C2, 0x1E)
    Sleep(400)
    OP_25(0x3C2, 0x23)
    Sleep(400)
    OP_25(0x3C2, 0x28)
    Sleep(400)
    OP_25(0x3C2, 0x2D)
    Sleep(400)
    OP_25(0x3C2, 0x32)
    Return()

    # Function_20_3A1A end

    def Function_21_3A59(): pass

    label("Function_21_3A59")

    OP_25(0x84, 0x5F)
    Sleep(200)
    OP_25(0x84, 0x5A)
    Sleep(200)
    OP_25(0x84, 0x55)
    Sleep(200)
    OP_25(0x84, 0x50)
    Sleep(200)
    OP_25(0x84, 0x4B)
    Sleep(200)
    OP_25(0x84, 0x46)
    Sleep(200)
    OP_25(0x84, 0x41)
    Sleep(200)
    OP_25(0x84, 0x3C)
    Sleep(200)
    OP_25(0x84, 0x32)
    Sleep(200)
    OP_25(0x84, 0x28)
    Sleep(200)
    OP_25(0x84, 0x1E)
    Return()

    # Function_21_3A59 end

    def Function_22_3AA4(): pass

    label("Function_22_3AA4")

    Sound(497, 2, 0, 0)
    Sound(496, 2, 0, 0)
    Sleep(300)
    OP_25(0x1F1, 0x5)
    OP_25(0x1F0, 0x5)
    Sleep(300)
    OP_25(0x1F1, 0xA)
    OP_25(0x1F0, 0xA)
    Sleep(300)
    OP_25(0x1F1, 0xF)
    OP_25(0x1F0, 0xF)
    Sleep(300)
    OP_25(0x1F1, 0x14)
    OP_25(0x1F0, 0x14)
    Sleep(300)
    OP_25(0x1F1, 0x19)
    OP_25(0x1F0, 0x19)
    Sleep(300)
    OP_25(0x1F1, 0x1E)
    OP_25(0x1F0, 0x1E)
    Sleep(300)
    OP_25(0x1F1, 0x23)
    OP_25(0x1F0, 0x23)
    Sleep(300)
    OP_25(0x1F1, 0x28)
    OP_25(0x1F0, 0x28)
    Sleep(300)
    OP_25(0x1F1, 0x2D)
    OP_25(0x1F0, 0x2D)
    Sleep(300)
    OP_25(0x1F1, 0x32)
    OP_25(0x1F0, 0x32)
    Return()

    # Function_22_3AA4 end

    def Function_23_3B1F(): pass

    label("Function_23_3B1F")

    OP_25(0x1F1, 0x37)
    OP_25(0x1F0, 0x37)
    Sleep(200)
    OP_25(0x1F1, 0x3C)
    OP_25(0x1F0, 0x3C)
    Sleep(200)
    OP_25(0x1F1, 0x41)
    OP_25(0x1F0, 0x41)
    Sleep(200)
    OP_25(0x1F1, 0x46)
    OP_25(0x1F0, 0x46)
    Return()

    # Function_23_3B1F end

    def Function_24_3B49(): pass

    label("Function_24_3B49")

    OP_25(0x1F1, 0x41)
    OP_25(0x1F0, 0x41)
    Sleep(200)
    OP_25(0x1F1, 0x3C)
    OP_25(0x1F0, 0x3C)
    Sleep(200)
    OP_25(0x1F1, 0x37)
    OP_25(0x1F0, 0x37)
    Sleep(200)
    OP_25(0x1F1, 0x32)
    OP_25(0x1F0, 0x32)
    Sleep(200)
    OP_25(0x1F1, 0x2D)
    OP_25(0x1F0, 0x2D)
    Sleep(200)
    OP_25(0x1F1, 0x28)
    OP_25(0x1F0, 0x28)
    Return()

    # Function_24_3B49 end

    def Function_25_3B89(): pass

    label("Function_25_3B89")

    Sleep(500)
    SetChrChipByIndex(0x9, 0x23)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x1000)
    Sleep(120)
    SetChrSubChip(0x9, 0x0)
    Sleep(120)
    SetChrSubChip(0x9, 0x1)
    Sound(802, 0, 100, 0)
    Sleep(300)
    Return()

    # Function_25_3B89 end

    def Function_26_3BB2(): pass

    label("Function_26_3BB2")

    SetChrChipByIndex(0xA, 0x24)
    Fade(250)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Return()

    # Function_26_3BB2 end

    def Function_27_3BCA(): pass

    label("Function_27_3BCA")

    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    Return()

    # Function_27_3BCA end

    SaveToFile()

Try(main)
