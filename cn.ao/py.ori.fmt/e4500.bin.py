from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4500.bin",                # FileName
        "e4500",                    # MapName
        "e4500",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4500",                  # 0
        "约纳的声音",             # 1
        "地形",                   # 2
        "水面",                   # 3
        "SE控制",                 # 4
    ))

    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(296, 0)                                        # 0

    ScpFunction((
        "Function_0_128",          # 00, 0
        "Function_1_160",          # 01, 1
        "Function_2_161",          # 02, 2
        "Function_3_8AC",          # 03, 3
        "Function_4_8EA",          # 04, 4
        "Function_5_12DB",         # 05, 5
        "Function_6_130E",         # 06, 6
        "Function_7_2916",         # 07, 7
        "Function_8_2A14",         # 08, 8
    ))


    def Function_0_128(): pass

    label("Function_0_128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_13C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_15F")

    label("loc_13C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_150")
    ClearScenarioFlags(0x22, 1)
    Event(0, 4)
    Jump("loc_15F")

    label("loc_150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_15F")
    ClearScenarioFlags(0x22, 2)
    Event(0, 6)

    label("loc_15F")

    Return()

    # Function_0_128 end

    def Function_1_160(): pass

    label("Function_1_160")

    Return()

    # Function_1_160 end

    def Function_2_161(): pass

    label("Function_2_161")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map/mprain00.eff")
    LoadChrToIndex("chr/ch02902.itc", 0x1E)
    SoundLoad(483)
    SoundLoad(126)
    SetChrPos(0x101, -950, 210, -1600, 180)
    SetChrPos(0x109, 0, 210, -1750, 180)
    SetChrPos(0x102, 950, 210, -1600, 180)
    SetChrPos(0x105, 800, 900, 0, 180)
    SetChrPos(0x103, -1130, 900, -660, 180)
    SetChrPos(0x104, -70, 900, 360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    SetChrPos(0x9, 0, 0, 0, 180)
    OP_D5(0x9, 0x0, 0x2BF20, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    SetChrPos(0xA, 0, 0, 0, 180)
    OP_D5(0xA, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x1, 0x5A)
    OP_71(0x1, 0x3E8, 0x7CF, 0x0, 0x20)
    PlayBGM("ed7151", 0)
    BeginChrThread(0xB, 1, 0, 3)
    PlayEffect(0x0, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x9C4)
    OP_11(0x95, 0xA0, 0xB5, 0x1E, 0x190, 0x9C4)
    Sound(128, 1, 50, 0)
    OP_68(-770, 3300, -4220, 0)
    MoveCamera(150, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(28820, 0)
    FadeToBright(1000, 0)
    OP_68(-1940, 4000, 9830, 6500)
    MoveCamera(172, -3, 0, 6500)
    OP_6E(650, 6500)
    SetCameraDistance(21530, 6500)
    Sleep(4500)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
    OP_11(0xB7, 0xDA, 0xDD, 0x1E, 0x190, 0x9C4)
    StopSound(128, 1000, 100)
    Sleep(500)
    StopEffect(0x7, 0x2)
    OP_6F(0x79)
    Sleep(1500)
    OP_68(-1080, 2150, -2460, 0)
    MoveCamera(44, 16, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    Fade(500)
    OP_0D()
    Sleep(300)

    #C0001
    ChrTalk(
        0x103,
        (
            "#00203F#5P……和天气预报说的一样，\x01",
            "到了午后，天气就转晴了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        (
            "#00306F#5P说不定这也是\x01",
            "女神在帮我们呢。\x02\x03",

            "#00301F老实说，接下来还不知\x01",
            "会遇到怎样的危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x105,
        (
            "#10304F#5P不过，比起在雨中探索，\x01",
            "总算是好得多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x109,
        (
            "#10108F#5P……说起最大的可能，\x01",
            "应该是『幻兽』吧，还是说……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00106F#5P老实说，从如今这种状况来看，\x01",
            "任何情况都有可能发生呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00003F#5P……亚里欧斯先生他们\x01",
            "不知会在何时抵达。\x02\x03",

            "#00008F我们就先行一步，\x01",
            "尽快确认林小姐她们的安危吧。\x02\x03",

            "#00001F视具体情况……\x01",
            "或许还有联络\x01",
            "警备队的必要。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x109,
        "#10101F#5P……嗯。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x104,
        (
            "#00301F#5P二位姐姐……\x01",
            "你们一定不要有事啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0009
    ChrTalk(
        0x103,
        (
            "#00205F#5P……这是……\x02\x03",

            "#00207F探测到湿度正在急速上升，\x01",
            "请大家注意……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_677():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_677)
    Sleep(50)

    def lambda_687():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_687)
    Sleep(50)

    def lambda_697():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_697)
    Sleep(50)

    def lambda_6A7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A7)
    Sleep(500)

    #C0010
    ChrTalk(
        0x101,
        "#00011F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1F40)
    OP_7D(0xC0, 0xE0, 0xFF, 0x0, 0xAF0)
    OP_11(0x90, 0xB0, 0xD0, 0x1, 0x32, 0xAF0)
    Sleep(500)
    OP_68(-2630, 2150, -3190, 3000)
    MoveCamera(51, 12, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(19410, 3000)
    OP_6F(0x79)
    Sleep(500)

    #C0011
    ChrTalk(
        0x105,
        "#10301F#6P这是……雾！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#00107F#6P直、直到刚才，\x01",
            "天气都还很晴朗啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x109,
        "#10107F#5P罗、罗伊德警官……该怎么办！？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00010F#5P啧……\x02\x03",

            "#00007F减慢速度，\x01",
            "慎重前进！\x02\x03",

            "缇欧，你能感知到\x01",
            "岩壁的接近吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#00201F#5P嗯，应该没问题……！\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00310F#5P事到如今，\x01",
            "也只好硬上了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_11(0x90, 0xB0, 0xD0, 0x1, 0x1E, 0xAF0)
    SetCameraDistance(20410, 2800)
    Sleep(800)
    StopSound(126, 2000, 50)
    StopSound(483, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x105, 0x4)
    WaitBGM()
    OP_24(0x7E)
    OP_24(0x1E3)
    SetScenarioFlags(0x22, 0)
    NewScene("m4200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_161 end

    def Function_3_8AC(): pass

    label("Function_3_8AC")

    Sound(126, 2, 50, 0)
    Sound(483, 2, 20, 0)
    Sleep(200)
    OP_25(0x1E3, 0x1E)
    Sleep(200)
    OP_25(0x1E3, 0x28)
    Sleep(200)
    OP_25(0x1E3, 0x32)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Sleep(200)
    OP_25(0x1E3, 0x46)
    Sleep(200)
    OP_25(0x1E3, 0x50)
    Sleep(200)
    OP_25(0x1E3, 0x5A)
    Return()

    # Function_3_8AC end

    def Function_4_8EA(): pass

    label("Function_4_8EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02902.itc", 0x1E)
    SoundLoad(483)
    SoundLoad(126)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis265.itp")
    SetChrPos(0x101, -800, 210, -1600, 180)
    SetChrPos(0x109, 0, 210, -1750, 180)
    SetChrPos(0x102, 950, 210, -1600, 180)
    SetChrPos(0x105, -1100, 780, 1450, 180)
    SetChrPos(0x103, 300, 780, 450, 180)
    SetChrPos(0x104, 900, 780, 1250, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x105, 0x4)
    PlayBGM("ed7560", 0)
    BeginChrThread(0xB, 1, 0, 5)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    SetChrPos(0xA, 0, 0, 0, 180)
    OP_74(0x1, 0x5A)
    OP_71(0x1, 0x7CF, 0x3E8, 0x0, 0x20)
    OP_68(250, 2150, 10000, 0)
    MoveCamera(345, 138, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(106500, 0)
    FadeToBright(1000, 0)
    OP_68(0, 2150, 5750, 3000)
    SetCameraDistance(88650, 3000)
    OP_0D()
    Sleep(1500)
    OP_68(1470, 2150, -5770, 0)
    MoveCamera(320, 175, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(34500, 0)
    Fade(1000)
    OP_68(20, 2150, -4920, 4500)
    MoveCamera(332, 175, 0, 4500)
    SetCameraDistance(22000, 4500)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-810, 2150, 460, 0)
    MoveCamera(327, 158, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(13000, 1500)
    OP_6F(0x79)

    #C0017
    ChrTalk(
        0x102,
        (
            "#00106F#5P……真没想到，『银』的\x01",
            "真实身份竟然会是莉夏小姐……\x02\x03",

            "#00108F我一直都以为\x01",
            "肯定是个男人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x105,
        (
            "#10303F#6P她在穿着『银』的那身打扮时，\x01",
            "似乎会刻意改变自己的气息。\x02\x03",

            "#10301F说不定连体型\x01",
            "都做了改变。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(250)

    #C0019
    ChrTalk(
        0x109,
        (
            "#10111F#5P普、普通人\x01",
            "能做到那种事吗？\x02\x03",

            "#10106F……话说回来，我们最近已经遇到\x01",
            "好几个不普通的人了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#00206F#6P连我的感知能力\x01",
            "都被她骗过了……\x02\x03",

            "#00200F不过，罗伊德前辈\x01",
            "好像并不是十分惊讶啊……？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00003F#5P……嗯，是啊。\x02\x03",

            "#00008F就在不久之前，\x01",
            "我曾和莉夏聊过几句……\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_25(0x1E3, 0x32)
    OP_25(0x7E, 0x14)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_25(0x1E3, 0x28)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "……我从很小的时候开始……\x01",
            "就将那个目标视为人生的全部了。\x02\x03",

            "从极其久远的往昔开始，\x01",
            "我的祖先便世代继承那条道路……\x02\x03",

            "现如今，早已不知\x01",
            "为何要踏上那条道路了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    OP_25(0x1E3, 0x32)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Sleep(200)
    OP_25(0x1E3, 0x46)
    Sleep(100)

    #C0023
    ChrTalk(
        0x101,
        (
            "#00006F#5P其实我当时就已经有点怀疑了，\x01",
            "只是并没有朝那个方向深入思考……\x02\x03",

            "#00001F如今看来，我的脑海中似乎一直留有\x01",
            "她就是『银』这个假设呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#00101F#5P原来发生过那种事……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(150)

    #C0025
    ChrTalk(
        0x104,
        (
            "#00306F#6P……仔细想想，如果只是个普通的外行人，\x01",
            "根本不可能在那么短的时间内就被\x01",
            "破格提拔为彩虹剧团的二号主角啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#00006F#5P是啊，但因为她是被伊莉娅小姐\x01",
            "强行拉进剧团的，而且做了一系列特训，\x01",
            "所以当时并没觉得有什么奇怪。\x02\x03",

            "#00008F而且，『银』出现的时期\x01",
            "与莉夏来到克洛斯贝尔的时间\x01",
            "也正好吻合。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        (
            "#00201F#6P『黑月』的曹先生等人\x01",
            "是否已经了解到她的真实身份了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x105,
        (
            "#10304F#6P这个嘛，站在她的立场来考虑，\x01",
            "应该会把自己的身份隐瞒起来吧。\x02\x03",

            "#10300F如果随意暴露自己的身份，\x01",
            "只会遭到别人的要挟和操控而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#00108F#5P……如此看来，\x01",
            "我们还是别把她的真实身份\x01",
            "泄露出去为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#00003F#5P是啊，姑且向科长报告一下，\x01",
            "接下来就暂观事态的发展吧。\x02\x03",

            "#00013F而且……相比『黑月』，\x01",
            "现在还是『赤色星座』的问题更加紧迫。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#00303F#6P是啊……\x02\x03",

            "#00301F叔叔他们在\x01",
            "这种时候突然行踪不明，\x01",
            "恐怕是在充分准备下而行动的。\x02\x03",

            "依我看，他们多半就要一口气发动猛攻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#00001F#5P是吗……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x109,
        (
            "#10101F#5P……看来有必要联络\x01",
            "索妮亚司令呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-180, 2150, 7610, 3500)
    MoveCamera(327, 164, 0, 3500)
    OP_6E(950, 3500)
    SetCameraDistance(13010, 3500)
    Sleep(1500)
    StopSound(126, 3000, 50)
    StopSound(483, 3000, 70)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM(-1, -1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x7E)
    OP_24(0x1E3)
    SetScenarioFlags(0x22, 0)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_8EA end

    def Function_5_12DB(): pass

    label("Function_5_12DB")

    Sound(126, 2, 50, 0)
    Sound(483, 2, 20, 0)
    Sleep(400)
    OP_25(0x1E3, 0x1E)
    Sleep(400)
    OP_25(0x1E3, 0x28)
    Sleep(300)
    OP_25(0x1E3, 0x32)
    Sleep(300)
    OP_25(0x1E3, 0x3C)
    Sleep(300)
    OP_25(0x1E3, 0x46)
    Sleep(300)
    Return()

    # Function_5_12DB end

    def Function_6_130E(): pass

    label("Function_6_130E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    LoadChrToIndex("chr/ch00302.itc", 0x1F)
    SoundLoad(483)
    SoundLoad(126)
    SoundLoad(803)
    SoundLoad(894)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    LoadEffect(0x0, "event\\ev315_00.eff")
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 800, 900, -100, 180)
    SetChrPos(0x102, -800, 900, 100, 180)
    SetChrPos(0x103, 100, 900, 1000, 180)
    SetChrPos(0x104, 0, 420, -1750, 180)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    SetChrPos(0x9, 0, 0, 0, 180)
    OP_D5(0x9, 0x0, 0x2BF20, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    SetChrPos(0xA, 0, 0, 0, 180)
    OP_D5(0xA, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x1, 0x5A)
    OP_71(0x1, 0x3E8, 0x7CF, 0x0, 0x20)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 700, 300, -100, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x104, 0, 0, 7)
    OP_F0(0x0, 0xA)
    OP_F0(0x1, 0x1F4)
    OP_68(0, 1800, -10000, 0)
    MoveCamera(25, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    BeginChrThread(0xB, 1, 0, 3)
    FadeToBright(1000, 0)
    OP_68(0, 1800, 40000, 9000)
    MoveCamera(155, 10, 0, 5000)
    SetCameraDistance(24000, 5000)
    Sleep(7000)
    OP_0D()
    Fade(1000)
    OP_68(-20, 1800, -110, 0)
    MoveCamera(126, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(18500, 2500)
    SetChrPos(0x104, 0, 420, -1450, 180)
    BeginChrThread(0x104, 1, 0, 8)
    OP_6F(0x79)
    OP_0D()

    #C0034
    ChrTalk(
        0x101,
        "#00001F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#00106F#6P幸好调到了一艘警用小艇，\x01",
            "总算是可以出发了……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#00203F#6P……米修拉姆好像\x01",
            "已经被彻底封锁起来了。\x02\x03",

            "#00201F主题公园和各家商店的\x01",
            "营业人员也都撤离了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#00306F#5P按照我们原本的猜测，\x01",
            "他们也有可能是去了湿地……\x02\x03",

            "#00301F但如今看来，显然还是\x01",
            "前往米修拉姆了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00008F#5P艾莉……\x01",
            "你没能和玛丽亚贝尔小姐\x01",
            "取得联络吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#00106F#6P……嗯，这几天\x01",
            "完全找不到她。\x02\x03",

            "#00108FＩＢＣ大楼遭到爆破之后，\x01",
            "她好像一直在忙着处理各种善后工作……\x02",
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

    #C0040
    ChrTalk(
        0x104,
        (
            "#00303F#5P那个大小姐暂且不提……\x02\x03",

            "#00301F雷克特和雾香小姐\x01",
            "暗示的那种可能性会是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#00206F#6P指使猎兵团袭击克洛斯贝尔的\x01",
            "真正黑手并非埃雷波尼亚帝国……\x02\x03",

            "#00201F而是迪塔·库罗伊斯市长……\x01",
            "不对，他现在已经是总统了。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#00008F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    #C0043
    ChrTalk(
        0x102,
        (
            "#00106F#12P……罗伊德，\x01",
            "你不必在意我的感受。\x02\x03",

            "#00108F其实，从昨天开始，\x01",
            "我就一直没能联系到外公……\x02\x03",

            "#00101F据管家海尔玛先生说，\x01",
            "外公很可能已经被软禁在\x01",
            "兰花塔了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0044
    ChrTalk(
        0x101,
        "#00005F#5P……！？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#00208F#6P……这……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x104,
        "#00306F#5P已经完全暴露反派面目了吗……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00006F#5P如果迪塔市长真的是\x01",
            "这一系列事件的幕后黑手……\x02\x03",

            "一切矛盾与疑问就\x01",
            "都可以得到解答了。\x02\x03",

            "#00008F在这种假设下，『赤色星座』与『结社』\x01",
            "就是他雇佣的行动部队与协助者……\x02\x03",

            "#00013F而魔人化的瓦鲁多……\x01",
            "甚至连『教团』都有可能\x01",
            "是被他利用的棋子。\x02",
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

    #C0048
    ChrTalk(
        0x102,
        "#00107F#12P连『Ｄ∴Ｇ教团』也是……！？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#00305F#5P瓦鲁多也就罢了……\x01",
            "难道连约亚西姆也被他利用了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        "#00208F#6P怎么会……不过……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#00003F#5P当然，他们之间存在\x01",
            "直接联系的可能性很低。\x02\x03",

            "从约亚西姆的言行来看，\x01",
            "似乎并不存在其他幕后黑手。\x02\x03",

            "#00001F不过，他有可能是在毫无察觉\x01",
            "的情况下遭到了他人利用。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#00206F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#00108F#12P说起来，我们至今都没能\x01",
            "查明到底是谁从太阳堡垒带走了\x01",
            "琪雅呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#00303F#5P而且还把她混进了\x01",
            "『黑之竞拍会』的拍卖品之中……\x02\x03",

            "#00301F仔细想想，如果那件事情是人为的，\x01",
            "『普通人』根本不可能做得到。\x02\x03",

            "除非是『银』或『结社成员』\x01",
            "这种级别的家伙……\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0055
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013F您好……！\x01",
            "我是特别任务支援科的罗伊德！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("少年的声音")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "太好了！终于接通了！\x02\x03",

            "我想让缇欧也听到，\x01",
            "你设置成扬声模式吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0057
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F是约纳吗？\x01",
            "明白了，我这就切换模式。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(804, 0, 100, 0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x101, 0x6)
    OP_0D()
    Sleep(300)

    #C0058
    ChrTalk(
        0x103,
        "#00201F#6P约纳，发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S还问发生了什么事！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S克洛斯贝尔的导力网络中……\x01",
            "潜伏着可怕的怪物！！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x101,
        "#00011F#5P怪物……？\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        "#00105F#12P那、那是什么意思？\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S一开始，我只是在网络边缘\x01",
            "发现了一些奇怪的数据构造体！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S因为都是意义不明的排列，\x01",
            "所以我本以为只是些垃圾数据……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S但经过进一步的调查，\x01",
            "我发现它们居然是由『结社』\x01",
            "所使用的代码进化而来的！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#00208F#6P『星辰代码』……\x02\x03",

            "#00201F也就是说，那是『结社』\x01",
            "设下的某种陷阱吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S不，从日期来看，\x01",
            "那已经是近五年前的东西了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S我记得克洛斯贝尔正是在\x01",
            "那个时期导入导力网络的吧！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        (
            "#00205F#6P嗯，是的……\x02\x03",

            "#00201F……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#00103F#12P向自治州政府提议\x01",
            "导入导力网络的正是\x01",
            "ＩＢＣ集团……\x02\x03",

            "#00108F正因如此，导入了财团技术的\x01",
            "ＩＢＣ与这项计划有着很深的关联……\x02\x03",

            "#00110F甚至到了熟知整个网络\x01",
            "基干部分的地步……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        "#00307F#5P喂喂，这也就是说……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0072
    ChrTalk(
        0x101,
        (
            "#00003F#5P约纳，\x01",
            "所谓的怪物到底是什么？\x02\x03",

            "#00001F它能引起什么问题？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S这、这个，目前还在解析中……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S不过，那绝对是个\x01",
            "可以覆盖整个导力网络\x01",
            "的巨大系统！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S而且，似乎还配备了\x01",
            "能与其进行联动的\x01",
            "现实系统！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x103,
        "#00201F#6P现实系统……？\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#00108F#12P现实……\x01",
            "也就是说，并不是导力网络的世界吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S嗯，地下空间的全部区域……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S都在这个系统的控制之下\x01",
            "与兰花塔连接在一起，\x01",
            "甚至还连接着米修拉姆那边！\x07\x00\x02",
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

    #C0080
    ChrTalk(
        0x101,
        "#00007F#5P米修拉姆……！？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        "#00310F#5P居然在现在听到了这个名字！？\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S总之！\x01",
            "解析完毕之后，我会再联系你们的！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11P#2S虽然不知道你们正在做些什么，\x01",
            "但一定要多加小心啊！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(813, 0, 70, 0)
    Sleep(200)
    Sound(894, 2, 80, 0)
    Sleep(100)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    StopSound(894, 2000, 70)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0084
    ChrTalk(
        0x104,
        (
            "#00306F#5P……喂喂，\x01",
            "这关联证据未免也太多了吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x103,
        (
            "#00206F#6P虽然目前还不知道那个系统\x01",
            "是为了什么目的而搭建的……\x02\x03",

            "#00208F但除了财团与『结社』之外，\x01",
            "能搭建那种巨大系统的\x01",
            "势力似乎也只有……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        "#00106F#12P#30W………………………………\x02",
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
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0087
    ChrTalk(
        0x101,
        (
            "#00006F#5P我们现在还是继续\x01",
            "前往米修拉姆吧。\x02\x03",

            "#00013F琪雅……亚里欧斯先生……\x01",
            "还有一切问题的答案都在那里等着我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1800, -3000, 3000)

    def lambda_2838():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2838)
    Sleep(50)

    def lambda_2848():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2848)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    Sleep(1000)
    EndChrThread(0x104, 0x1)
    Fade(1000)
    OP_68(0, 1800, -20000, 0)
    MoveCamera(180, 15, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(18500, 0)
    OP_68(0, 3800, 40000, 10000)
    MoveCamera(180, 0, 0, 7000)
    Sleep(5000)
    StopSound(126, 3000, 50)
    StopSound(483, 3000, 90)
    Sleep(2000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x8, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7565", "ed7561")
    ReplaceBGM("ed7160", "ed7561")
    OP_24(0x323)
    OP_24(0x37E)
    SetScenarioFlags(0x22, 1)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_130E end

    def Function_7_2916(): pass

    label("Function_7_2916")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A13")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296F")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(333)
    Jump("loc_2A0E")

    label("loc_296F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29BD")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_2A0E")

    label("loc_29BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A0B")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -8000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(166)
    Jump("loc_2A0E")

    label("loc_2A0B")

    Sleep(233)

    label("loc_2A0E")

    Jump("Function_7_2916")

    label("loc_2A13")

    Return()

    # Function_7_2916 end

    def Function_8_2A14(): pass

    label("Function_8_2A14")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A4C")
    OP_82(0x0, 0xF, 0x1388, 0x3E8)
    Sleep(1000)
    OP_82(0x0, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("Function_8_2A14")

    label("loc_2A4C")

    Return()

    # Function_8_2A14 end

    SaveToFile()

Try(main)
