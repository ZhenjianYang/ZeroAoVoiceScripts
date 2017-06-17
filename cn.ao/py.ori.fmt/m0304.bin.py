from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m0304.bin",                # FileName
        "m0304",                    # MapName
        "m0304",                    # Location
        0x0000,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "m0304",                  # 0
        "雷因兹",                 # 1
        "SE控制",                 # 2
    ))

    AddCharChip((
        "chr/ch28100.itc",                   # 00
    ))

    DeclNpc(0,       0,       1629,    0,    261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(232, 0)                                        # 0

    ScpFunction((
        "Function_0_E8",           # 00, 0
        "Function_1_198",          # 01, 1
        "Function_2_1A8",          # 02, 2
        "Function_3_1A9",          # 03, 3
        "Function_4_229",          # 04, 4
        "Function_5_1B02",         # 05, 5
    ))


    def Function_0_E8(): pass

    label("Function_0_E8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_120"),
        (1, "loc_12C"),
        (2, "loc_138"),
        (3, "loc_144"),
        (4, "loc_150"),
        (5, "loc_15C"),
        (6, "loc_168"),
        (SWITCH_DEFAULT, "loc_174"),
    )


    label("loc_120")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_12C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_138")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_144")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_150")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_15C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_168")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_174")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_180")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_197")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_197")

    Return()

    # Function_0_E8 end

    def Function_1_198(): pass

    label("Function_1_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1A7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)

    label("loc_1A7")

    Return()

    # Function_1_198 end

    def Function_2_1A8(): pass

    label("Function_2_1A8")

    Return()

    # Function_2_1A8 end

    def Function_3_1A9(): pass

    label("Function_3_1A9")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "我想，今后应该还会有\x01",
            "以Ｒ＆Ａ调查所成员的\x01",
            "身份与各位见面的机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "总之，我会在这里祝愿\x01",
            "各位的突击作战取得成功。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_1A9 end

    def Function_4_229(): pass

    label("Function_4_229")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    BeginChrThread(0x9, 1, 0, 5)
    OP_68(1090, 0, -8490, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19760, 0)
    SetChrPos(0x101, 0, 0, -10650, 0)
    SetChrPos(0x102, 1100, 0, -10650, 0)
    SetChrPos(0x103, -1100, 0, -10650, 0)
    SetChrPos(0x104, 0, 0, -10650, 0)
    SetChrPos(0xF4, -1100, 0, -10650, 0)
    SetChrPos(0xF5, 1100, 0, -10650, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)

    #A0003
    AnonymousTalk(
        0x101,
        (
            "#00001F果然可以通向\x01",
            "地下空间呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0004
    AnonymousTalk(
        0x102,
        (
            "#00103F看样子，似乎是\x01",
            "Ｄ区域的一角……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0005
    AnonymousTalk(
        0x103,
        (
            "#00205F……气息越来越明显了。\x02\x03",

            "#00203F虽然人数只有一名……\x01",
            "但确实有人在这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_418")

    #A0006
    AnonymousTalk(
        0x10A,
        "#00601F（就在这道门的里面吗……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_491")

    label("loc_418")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_457")

    #A0007
    AnonymousTalk(
        0x109,
        "#10101F（就在这道门的里面吧……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_491")

    label("loc_457")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_491")

    #A0008
    AnonymousTalk(
        0x106,
        "#10701F（就在这道门的里面吧……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_491")


    #A0009
    AnonymousTalk(
        0x103,
        "#00201F（嗯，不会有错。）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_509")

    #A0010
    AnonymousTalk(
        0x105,
        (
            "#10400F（这里是仓库？还是其它什么地方？\x01",
            "  门上有窗呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5B4")

    label("loc_509")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_561")

    #A0011
    AnonymousTalk(
        0x106,
        (
            "#10705F（这里是仓库吗？还是其它什么地方？\x01",
            "  门上有窗呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5B4")

    label("loc_561")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B4")

    #A0012
    AnonymousTalk(
        0x109,
        (
            "#10105F（这里是仓库吗？还是其它什么地方？\x01",
            "  门上有窗呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5B4")


    #A0013
    AnonymousTalk(
        0x101,
        (
            "#00003F（不清楚……\x01",
            "  但这倒是很方便。）\x02\x03",

            "#00000F（就在这里窥视一下\x01",
            "  里面的状况吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x9, 0x1)
    OP_68(950, 0, 3180, 0)
    MoveCamera(42, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16090, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(10)
    PlayBGM("ed7302", 0)

    #N0014
    NpcTalk(
        0x8,
        "？？？",
        (
            "是的，上校……\x01",
            "好的、好的……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0015
    NpcTalk(
        0x8,
        "？？？",
        (
            "哎？我又那样叫了吗？\x01",
            "啊哈哈……抱歉啦，所长。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#00005F#N（那背影……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0017
    ChrTalk(
        0x102,
        (
            "#00105F#N（莫非是……\x01",
            "  克洛斯贝尔通讯社\x01",
            "  的雷因兹先生？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0018
    ChrTalk(
        0x103,
        "#00205F#N（他在这种地方做什么……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x8, 0x0, 500)
    Sleep(300)

    #C0019
    ChrTalk(
        0x8,
        (
            "#5P那个……藏在后面的是\x01",
            "支援科的各位吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#5P如果方便，\x01",
            "可否过来聊聊呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        (
            "#00306F#N哎呀呀……\x01",
            "原来他已经察觉到了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00001F#N虽然不能大意，但我们\x01",
            "还是照他所说，过去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(980, 900, -2510, 4500)
    MoveCamera(39, 16, 0, 4500)
    OP_6E(600, 4500)
    SetCameraDistance(18630, 4500)
    Sleep(2000)

    def lambda_865():
        OP_97(0xFE, 0x0, 0x0, 0x10CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_865)

    def lambda_87F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_87F)
    Sleep(100)

    def lambda_893():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_893)

    def lambda_8AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8AD)
    Sleep(100)

    def lambda_8C1():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8C1)

    def lambda_8DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8DB)
    Sleep(500)

    def lambda_8EF():
        OP_97(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8EF)

    def lambda_909():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_909)
    Sleep(100)

    def lambda_91D():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_91D)

    def lambda_937():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_937)
    Sleep(100)

    def lambda_94B():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_94B)

    def lambda_965():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_965)
    WaitChrThread(0xF5, 1)

    #C0023
    ChrTalk(
        0x8,
        "#5P哈哈，果然是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#5P但真没想到\x01",
            "会在这样的地方\x01",
            "与各位见面。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(590, 400, 910, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16820, 3000)

    def lambda_9F4():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F4)
    Sleep(50)

    def lambda_A11():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A11)
    Sleep(50)

    def lambda_A2E():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A2E)
    Sleep(50)

    def lambda_A4B():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A4B)
    Sleep(50)

    def lambda_A68():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A68)
    Sleep(50)

    def lambda_A85():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A85)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)

    #C0025
    ChrTalk(
        0x101,
        "#12P#00001F嗯，我们也一样。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#12P#00103F克洛斯贝尔通讯社的\x01",
            "新入职记者兼摄影师，\x01",
            "格蕾丝小姐的搭档……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#12P#00303F呼，会在这种地方相遇，\x01",
            "也就表示你的身份不止如此了吧。\x02\x03",

            "#00301F既然如此，就不要再装模作样了，\x01",
            "赶快告诉我们你的真实身份如何？\x02\x03",

            "你早就察觉到了我们，\x01",
            "却完全没有掩饰的意思，\x01",
            "显然也没打算隐瞒吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#5P嗯，不过我并没有\x01",
            "伪装过自己的性格呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#5P其实我是某家\x01",
            "民间调查公司的职员。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0030
    ChrTalk(
        0x101,
        "#12P#00005F民间调查公司……？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#5P嗯，是位于\x01",
            "利贝尔的\x01",
            "『Ｒ＆Ａ调查所』。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#12P#00105F『Ｒ＆Ａ调查所』……\x01",
            "似乎曾在什么地方\x01",
            "听到过这个名字……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D1F")

    #C0033
    ChrTalk(
        0x10A,
        "#12P#00603F唔，我只知道公司名而已……\x02",
    )

    CloseMessageWindow()

    label("loc_D1F")


    #C0034
    ChrTalk(
        0x8,
        (
            "#5P嗯，毕竟只是一家\x01",
            "最近刚刚成立的小公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#5P不过，理查德所长\x01",
            "应该还是比较有名的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ECA")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0036
    ChrTalk(
        0x102,
        (
            "#12P#00105F莫非是……\x01",
            "曾隶属于利贝尔王国军的\x01",
            "理查德前上校吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x10A,
        "#12P#00600F原来如此……这样一来，我就可以理解了。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#5P#00005F艾莉、达德利警官……\x01",
            "你们知道那个人？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x10A,
        (
            "#12P#00603F嗯，亚兰·理查德——\x02\x03",

            "#00600F……两年前，曾在利贝尔\x01",
            "策动政变事件的\x01",
            "前情报部军官。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA6")

    label("loc_ECA")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0040
    ChrTalk(
        0x102,
        (
            "#12P#00105F莫非是……\x01",
            "曾隶属于利贝尔王国军的\x01",
            "理查德前上校吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#5P#00005F艾莉，你知道那个人？\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#12P#00103F嗯，亚兰·理查德——\x02\x03",

            "#00101F……是两年前在利贝尔\x01",
            "策动政变事件的\x01",
            "前情报部军官。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA6")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x101,
        "#5P#00005F策动那起政变事件的……？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#12P#00103F是的，但在利贝尔异变事件中，\x01",
            "他为了挽救陷于危难的国家\x01",
            "而做出了卓越贡献……\x02\x03",

            "#00100F因此在异变事件结束后，\x01",
            "得到了女王陛下的正式恩赦。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#5P#00005F得到恩赦……\x02\x03",

            "#00003F原来如此，在那之后，\x01",
            "他就充分利用自身经历，\x01",
            "建立了一家调查公司啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1126")

    #C0046
    ChrTalk(
        0x106,
        (
            "#12P#10703F听起来……\x01",
            "似乎是个相当精干的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11AD")

    label("loc_1126")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_116B")

    #C0047
    ChrTalk(
        0x105,
        (
            "#12P#10402F呵呵，似乎是个\x01",
            "相当优秀的人物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11AD")

    label("loc_116B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11AD")

    #C0048
    ChrTalk(
        0x109,
        (
            "#12P#10106F听起来……\x01",
            "似乎是个相当优秀的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11AD")


    #C0049
    ChrTalk(
        0x8,
        (
            "#5P嗯，真不愧是支援科的各位，\x01",
            "竟然对这些事情也了解得如此详细。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "#5P既然如此，你们应该可以\x01",
            "明白我的立场了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#12P#00003F嗯，基本上明白了。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        (
            "#12P#00101F但是，你为何要向我们\x01",
            "透露自己的真实身份呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#5P哦，因为我觉得\x01",
            "在今后的工作中也许会有\x01",
            "与各位打交道的机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#5P既然如此，早说晚说\x01",
            "也没什么区别。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#5P顺便一提，我并没有把\x01",
            "这些事情告诉通讯社的任何人，\x01",
            "包括格蕾丝小姐在内。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "#5P提出这种要求也许有些过分，\x01",
            "但希望各位能替我保密。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，由此看来，\x01",
            "你只是身处\x01",
            "第三方的人士。\x02\x03",

            "我们自然不会\x01",
            "泄露你的秘密。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#5P非常感谢，\x01",
            "我就知道各位会答应。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        (
            "#12P#00203F对了，我之前听说，\x01",
            "由于受雾气的影响，\x01",
            "导力通讯很难连接……\x02\x03",

            "#00205F但你那部通讯器\x01",
            "好像却能正常使用呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        "#5P哦，你说这个啊。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "#5P虽然也会受到雾气的影响，\x01",
            "但这部通讯器可以发送出\x01",
            "信号比较强的导力波。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#5P不过，最大范围也只能覆盖到\x01",
            "稍微超过克洛斯贝尔的区域而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#5P所长已经亲自\x01",
            "前往阿尔泰尔市了，\x01",
            "因此可以与我接通。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15A3")

    #C0064
    ChrTalk(
        0x10A,
        (
            "#12P#00603F原来如此……\x01",
            "在这种状况下，配合得真是出色啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1642")

    label("loc_15A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15F6")

    #C0065
    ChrTalk(
        0x105,
        (
            "#12P#10404F原来如此……\x01",
            "在这种状况下，配合得还真出色啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1642")

    label("loc_15F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1642")

    #C0066
    ChrTalk(
        0x109,
        (
            "#12P#10105F原来如此……\x01",
            "在这种状况下，配合得真是默契。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1642")


    #C0067
    ChrTalk(
        0x104,
        (
            "#12P#00303F那部通讯器……\x01",
            "好像是带有加密通讯\x01",
            "功能的类型吧？\x02\x03",

            "#00302F你做事简直比\x01",
            "军人还要严谨啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "#5P哈哈，这真是\x01",
            "太过奖了……\x01",
            "你对这种东西还真了解啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "#5P不管怎么说，毕竟不能让\x01",
            "国防军解析到通讯内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "#5P不过这种通讯器\x01",
            "的性能固然很强，\x01",
            "但价格也相对很高昂。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "#5P副所长曾叮嘱过我无数次，\x01",
            "无论发生什么事，都不能把它弄坏，\x01",
            "在搬运的时候我都非常小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "#5P因此请各位替我保密，\x01",
            "一定不要把我藏身在此处\x01",
            "的事情告诉任何人。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18D2")

    #C0073
    ChrTalk(
        0x106,
        "#12P#10703F……真是很有民间风格的发言啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1962")

    label("loc_18D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1921")

    #C0074
    ChrTalk(
        0x109,
        (
            "#12P#10103F该怎么说呢……\x01",
            "真是很有民间风格的发言啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1962")

    label("loc_1921")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1962")

    #C0075
    ChrTalk(
        0x105,
        "#12P#10404F呵呵，真是很有民间风格的发言啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1962")


    #C0076
    ChrTalk(
        0x8,
        (
            "#5P哈哈，没错，\x01",
            "实在是很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "#5P……先不说这些啦，\x01",
            "咱们已经聊很久了。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "#5P接下来，我还要\x01",
            "在这里继续与外界\x01",
            "人士联络……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "#5P各位在突击兰花塔\x01",
            "的时候一定要\x01",
            "多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#12P#00006F嗯……哎？我们好像\x01",
            "并没有和你提到过这件事吧……\x02\x03",

            "#00000F算啦，已经没有多少时间了，\x01",
            "我们这就告辞了。\x02\x03",

            "#00001F雷因兹先生，你在这里行动时，\x01",
            "也一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        "#5P嗯，当然。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x23, 1)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_229 end

    def Function_5_1B02(): pass

    label("Function_5_1B02")

    Sound(32, 0, 30, 0)
    Sleep(700)
    Sound(33, 0, 20, 0)
    Sleep(700)
    Sound(32, 0, 40, 0)
    Sleep(700)
    Sound(33, 0, 30, 0)
    Sleep(700)

    label("loc_1B26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B48")
    Sound(32, 0, 50, 0)
    Sleep(700)
    Sound(33, 0, 40, 0)
    Sleep(700)
    Jump("loc_1B26")

    label("loc_1B48")

    Return()

    # Function_5_1B02 end

    SaveToFile()

Try(main)
