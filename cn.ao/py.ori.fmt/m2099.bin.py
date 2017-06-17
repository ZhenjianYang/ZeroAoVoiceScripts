from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m2099.bin",                # FileName
        "m2099",                    # MapName
        "m2099",                    # Location
        0x0074,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x23,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 116, 0, 0, 0, 1],
    )

    BuildStringList((
        "m2099",                  # 0
        "恶魔",                   # 1
        "恶魔",                   # 2
        "恶魔",                   # 3
        "SE控制",                 # 4
        "bm2099",                 # 5
    ))

    ATBonus("ATBonus_158", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_178", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_17C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_180", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_184", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_188", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_18C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_190", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_194", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_200", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_204", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_208", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_20C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_210", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_214", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_218", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bm2099", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_178", "MonsterBattlePostion_1F8", "ed7405", "ed7453", "ATBonus_158"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-83500,  0,       -5000,   1200,    -83500,  1500,    -5000,   0x007C, 0,  2,  0x0000)

    ChipFrameInfo(660, 0)                                        # 0

    ScpFunction((
        "Function_0_294",          # 00, 0
        "Function_1_2C2",          # 01, 1
        "Function_2_2DB",          # 02, 2
        "Function_3_3BF",          # 03, 3
        "Function_4_CA5",          # 04, 4
        "Function_5_CCA",          # 05, 5
        "Function_6_CE7",          # 06, 6
        "Function_7_D20",          # 07, 7
        "Function_8_1E9E",         # 08, 8
        "Function_9_1ECF",         # 09, 9
        "Function_10_206D",        # 0A, 10
        "Function_11_208C",        # 0B, 11
        "Function_12_20A7",        # 0C, 12
        "Function_13_212F",        # 0D, 13
    ))


    def Function_0_294(): pass

    label("Function_0_294")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C1")
    Event(0, 3)

    label("loc_2C1")

    Return()

    # Function_0_294 end

    def Function_1_2C2(): pass

    label("Function_1_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_2D4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D4")

    Sound(129, 1, 100, 0)
    Return()

    # Function_1_2C2 end

    def Function_2_2DB(): pass

    label("Function_2_2DB")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B0")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x0, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x0, 0x0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x0, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_3B0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_2DB end

    def Function_3_3BF(): pass

    label("Function_3_3BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    LoadChrToIndex("monster/ch75150.itc", 0x1E)
    LoadEffect(0x0, "event\\ev501_00.eff")
    SoundLoad(825)
    OP_68(39850, -450, 2630, 0)
    MoveCamera(64, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32000, 0)
    SetChrPos(0x18D, 33000, 250, 0, 90)
    SetChrPos(0x101, 32000, 250, 1200, 90)
    SetChrPos(0x102, 32000, 250, -1200, 90)
    SetChrPos(0x103, 30500, 250, 780, 90)
    SetChrPos(0x104, 30400, 250, -560, 90)
    SetChrPos(0x109, 29120, 250, 1200, 90)
    SetChrPos(0x105, 29000, 250, -920, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrPos(0x8, 50000, -2500, 0, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    BeginChrThread(0x8, 0, 0, 5)

    def lambda_4EF():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18D, 1, lambda_4EF)
    Sleep(50)

    def lambda_50C():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50C)
    Sleep(50)

    def lambda_529():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_529)
    Sleep(50)

    def lambda_546():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_546)
    Sleep(50)

    def lambda_563():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_563)
    Sleep(50)

    def lambda_580():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_580)
    Sleep(50)

    def lambda_59D():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_59D)
    OP_68(45280, -450, 2660, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x105, 1)
    Sleep(500)
    Fade(500)
    OP_68(46790, -850, 1390, 0)
    MoveCamera(64, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21390, 0)
    OP_0D()

    #C0002
    ChrTalk(
        0x101,
        (
            "#00006F呼……\x01",
            "总算到这里了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0003
    ChrTalk(
        0x101,
        (
            "#00000F艾莉，你这次\x01",
            "好像不要紧了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0004
    ChrTalk(
        0x102,
        (
            "#12P#00102F啊……嗯，\x01",
            "因为有莉丝小姐在……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x105,
        (
            "#6P#10304F也对，在这种地方，\x01",
            "如果有修女同行，\x01",
            "确实能让人安心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#12P#00309F嗯，毕竟这里是僧院。\x02\x03",

            "#00304F说起来，能与这么可爱的小姐同行，\x01",
            "也让我充满了干劲。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x103,
        "#6P#00211F还是和以前一样得意忘形。\x02",
    )

    CloseMessageWindow()
    OP_63(0x18D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    #C0008
    ChrTalk(
        0x109,
        (
            "#6P#10105F莉丝小姐，\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A6():
        TurnDirection(0xFE, 0x18D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A6)
    Sleep(50)

    def lambda_7B6():
        TurnDirection(0xFE, 0x18D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B6)
    Sleep(300)
    OP_64(0x18D)

    #C0009
    ChrTalk(
        0x18D,
        (
            "#12P#04403F没什么，只是有些在意\x01",
            "地上的这个巨大图案。\x02\x03",

            "#04400F莫非就是\x01",
            "那个『教团』的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#6P#00005F啊……原来你知道啊。\x02\x03",

            "#00001F嗯，这好像是他们从\x01",
            "中世纪就开始使用的徽章。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        (
            "#6P#00200F他们曾经在这里\x01",
            "举行过很多血腥的仪式……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#12P#00306F话说回来，我们上次来的时候，\x01",
            "还真是相当惊险呢。\x02\x03",

            "#00309F那口钟突然响了起来，\x01",
            "随后就出现了『恶魔』……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(100)
    Sound(827, 0, 100, 0)
    Sleep(500)
    OP_63(0x18D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_9FC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FC)
    Sleep(50)

    def lambda_A0C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A0C)
    Sleep(300)

    #C0013
    ChrTalk(
        0x101,
        "#6P#00005F难、难道……！\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x105,
        "#12P#10301F嗯……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x18D,
        "#6P#04401F是非同寻常的『魔物』气息……\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(1500)
    OP_68(49940, 1150, 0, 1500)
    SetCameraDistance(16020, 1500)
    OP_6F(0x11)
    Fade(1000)
    SetCameraDistance(15520, 0)
    Sound(826, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 50000, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    BeginChrThread(0x101, 3, 0, 4)
    Sound(825, 2, 50, 0)
    OP_68(49940, 1550, 0, 2500)
    SetCameraDistance(12520, 2500)
    Sleep(1500)
    BeginChrThread(0x8, 3, 0, 6)
    OP_6F(0x79)
    Fade(2000)
    Sound(817, 0, 100, 0)
    WaitChrThread(0x8, 3)
    OP_0D()
    Sleep(1000)
    OP_68(49940, 250, 0, 1000)
    MoveCamera(90, 12, 0, 1000)
    SetCameraDistance(21370, 1000)
    OP_6F(0x79)

    #C0016
    ChrTalk(
        0x102,
        "#12P#00105F恶、恶魔……！？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#12P#00310F啧！为何偏要在这种时候\x01",
            "突然出现！\x02\x03",

            "#00306F就像是我给召唤出来的一样！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        (
            "#6P#00201F大家小心……！\x01",
            "我感觉到了比上次遭遇时\x01",
            "更加强大的灵压……！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x18D,
        "#12P#04401F来了……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15980, 500)
    OP_68(50940, 1050, 0, 500)
    OP_82(0x0, 0x64, 0x1388, 0x1F4)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sound(830, 0, 100, 0)
    Sleep(500)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x8, 0x0)
    Battle("BattleInfo_218", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 7)
    Return()

    # Function_3_3BF end

    def Function_4_CA5(): pass

    label("Function_4_CA5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CC9")
    OP_82(0x64, 0x64, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_4_CA5")

    label("loc_CC9")

    Return()

    # Function_4_CA5 end

    def Function_5_CCA(): pass

    label("Function_5_CCA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CE6")
    OP_A1(0xFE, 0x4E2, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_5_CCA")

    label("loc_CE6")

    Return()

    # Function_5_CCA end

    def Function_6_CE7(): pass

    label("Function_6_CE7")

    ClearChrFlags(0xFE, 0x1)

    def lambda_CF1():
        OP_98(0xFE, 0x0, 0xAF0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CF1)

    def lambda_D0B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D0B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_6_CE7 end

    def Function_7_D20(): pass

    label("Function_7_D20")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04400.itp")
    LoadChrToIndex("monster/ch75150.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch02950.itc", 0x23)
    LoadChrToIndex("chr/ch03050.itc", 0x24)
    LoadChrToIndex("apl/ch51256.itc", 0x25)
    LoadChrToIndex("apl/ch51257.itc", 0x26)
    LoadChrToIndex("monster/ch75153.itc", 0x27)
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "event\\ev12026.eff")
    LoadEffect(0x4, "event\\ev12027.eff")
    LoadEffect(0x5, "battle\\ms00001.eff")
    LoadEffect(0x6, "event\\ev12028.eff")
    LoadEffect(0x7, "event\\ev12029.eff")
    SoundLoad(852)
    OP_68(46380, -450, 2210, 0)
    MoveCamera(60, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x18D, 43000, 250, 0, 90)
    SetChrPos(0x101, 42000, 250, 1200, 90)
    SetChrPos(0x102, 42000, 250, -1200, 90)
    SetChrPos(0x103, 40500, 250, 780, 90)
    SetChrPos(0x104, 40400, 250, -560, 90)
    SetChrPos(0x109, 39120, 250, 1400, 90)
    SetChrPos(0x105, 39000, 250, -1400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 50000, 0, 0, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x5)
    SetChrPos(0x9, 29320, 0, 4940, 90)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x5)
    SetChrPos(0xA, 26970, 0, -4670, 90)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x1)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0020
    ChrTalk(
        0x101,
        "#6P#00003F呼……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        "#12P#00106F总、总算解决掉了。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#6P#00304F嘿，对现在的我们来说，\x01",
            "已经不算什么棘手的敌人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        "#6P#00204F……别逞强了。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x105,
        (
            "#12P#10301F……慢着，\x01",
            "似乎还不能安心。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(100)
    Sound(827, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 8)
    Sleep(1000)
    Fade(1000)
    Sound(202, 0, 50, 0)
    SetChrPos(0x8, 50000, 300, 0, 270)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Sleep(500)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 0, 0, 5)
    BeginChrThread(0x9, 0, 0, 5)
    BeginChrThread(0xA, 0, 0, 5)
    OP_68(43050, -450, 1610, 3000)
    MoveCamera(56, 27, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(28950, 3000)

    def lambda_1191():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1191)
    Sleep(50)

    def lambda_11A1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11A1)
    Sleep(50)

    def lambda_11B1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11B1)
    Sleep(50)

    def lambda_11C1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11C1)
    Sleep(50)

    def lambda_11D1():
        OP_95(0xFE, 34530, 250, 2090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11D1)

    def lambda_11EB():
        OP_95(0xFE, 34440, 250, -3100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11EB)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0x5A, 0x0)
    Sound(831, 0, 100, 0)
    WaitChrThread(0xA, 1)
    OP_6F(0x79)

    #C0025
    ChrTalk(
        0x101,
        (
            "#6P#00010F唔……\x01",
            "还活着吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        (
            "#11P#00203F……看来是\x01",
            "不死系的魔物……\x02\x03",

            "#00200F凭我们的武器和魔法，\x01",
            "恐怕不可能将它们\x01",
            "彻底消灭。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#12P#00110F怎、怎么会……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        (
            "#11P#00310F啧……\x01",
            "真是群危险的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x105,
        (
            "#10303F不管怎么说，我们一定要\x01",
            "想办法突出重围。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#6P#00007F莉丝小姐，\x01",
            "请退到我们身后！\x02\x03",

            "我们无论如何也会\x01",
            "保护好你的——\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x18D,
        (
            "#6P#04403F……不，\x01",
            "没有那个必要。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(44800, -450, 1370, 1500)
    MoveCamera(62, 27, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(18970, 1500)
    OP_6F(0x79)
    Fade(500)
    Sound(540, 0, 70, 0)
    SetChrChipByIndex(0x18D, 0x25)
    SetChrSubChip(0x18D, 0x0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x18D, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(357, 0, 60, 0)
    Sound(852, 2, 100, 0)
    BeginChrThread(0x18D, 1, 0, 11)
    Sleep(500)

    #C0032
    ChrTalk(
        0x101,
        "#6P#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x18D,
        (
            "#6P#04407F看招！\x01",
            "无尽剑制！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x18D, 0x1)
    BeginChrThread(0x18D, 3, 0, 9)
    OP_68(44180, -450, 1040, 1000)
    MoveCamera(62, 27, 0, 1000)
    OP_6E(600, 1000)
    SetCameraDistance(32119, 1000)
    OP_6F(0x79)
    WaitChrThread(0x18D, 3)
    Sleep(500)
    StopBGM(0xFA0)
    Fade(500)
    Sound(831, 0, 60, 0)
    Sound(514, 0, 100, 0)
    SetChrPos(0x8, 50000, 0, 0, 270)
    SetChrPos(0x9, 34530, 0, 2090, 90)
    SetChrPos(0xA, 34440, 0, -3100, 90)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrChipByIndex(0x8, 0x27)
    SetChrChipByIndex(0x9, 0x27)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    BeginChrThread(0xB, 1, 0, 12)
    PlayEffect(0x6, 0x1, 0x18D, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x6, 0x2)
    Sleep(3000)

    #C0034
    ChrTalk(
        0x101,
        "#6P#00005F什么……！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#11P#00305F开玩笑吧……！？\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        "#11P#00205F瞬间就把这么多魔物……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x18D,
        "#6P#04403F……接下来是最后一步。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x18D, 0x26)
    SetChrSubChip(0x18D, 0x0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x18D, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(357, 0, 60, 0)
    Sound(852, 2, 100, 0)
    BeginChrThread(0x18D, 3, 0, 10)

    def lambda_1649():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1649)

    def lambda_165A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F40)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_165A)

    def lambda_166B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F40)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_166B)
    OP_68(43230, -450, 2400, 10000)
    MoveCamera(45, 27, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(32119, 10000)
    Sleep(500)
    PlayEffect(0x7, 0x2, 0x8, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x3, 0x9, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x4, 0xA, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(843, 0, 80, 0)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x105,
        "#11P#10305F#10A嘿……\x02",
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    #C0039
    ChrTalk(
        0x102,
        "#6P#00105F#10A魔物都被净化了……\x02",
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    StopSound(852, 3000, 100)
    WaitChrThread(0xA, 2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)
    StopEffect(0x1, 0x2)
    EndChrThread(0x18D, 0x3)
    Sleep(1500)
    Fade(500)
    OP_68(46790, -850, 1390, 0)
    MoveCamera(64, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21390, 0)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    def lambda_184F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_184F)
    Sleep(50)

    def lambda_185F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_185F)
    Sleep(50)

    def lambda_186F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_186F)
    Sleep(50)

    def lambda_187F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_187F)
    Sleep(300)

    #C0040
    ChrTalk(
        0x109,
        (
            "#6P#10101F罗、罗伊德警官，\x01",
            "刚才那个魔法阵不就是……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#6P#00003F嗯……\x01",
            "是凯文先生当时在\x01",
            "阿尔泰尔据点使用过的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x18D, 500)

    #C0042
    ChrTalk(
        0x101,
        (
            "#6P#00001F莉丝小姐，\x01",
            "你难道是……？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x18D, 0xFF)
    SetChrSubChip(0x18D, 0x0)
    OP_0D()
    TurnDirection(0x18D, 0x102, 500)

    #C0043
    ChrTalk(
        0x18D,
        (
            "#5P#04402F……艾莉小姐，\x01",
            "你一直没有把我的身份\x01",
            "告诉别人吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x18D, 500)

    #C0044
    ChrTalk(
        0x102,
        (
            "#12P#00106F嗯……\x01",
            "我觉得不能擅自把\x01",
            "你的身份透露出去。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x18D,
        "#5P#04404F呵呵……非常感谢。\x02",
    )

    CloseMessageWindow()
    OP_93(0x18D, 0x10E, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0046
    AnonymousTalk(
        0x18D,
        (
            "……不过大主教似乎已经\x01",
            "隐隐察觉到了……\x02\x03",

            "我隶属于教会内的一个\x01",
            "特殊组织──『星杯骑士团』。\x02\x03",

            "这个组织从属于\x01",
            "名为封圣省的机关，\x01",
            "主要职责为回收古代遗物。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0047
    ChrTalk(
        0x101,
        "#6P#00011F星杯骑士团……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x109,
        (
            "#6P#10111F不就是在阿尔泰尔据点\x01",
            "出手帮助我们的那位……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x18D,
        (
            "#11P#04404F帮助你们的……\x01",
            "应该就是凯文·格拉汉姆吧？\x02\x03",

            "#04402F我的级别为『随从骑士』，\x01",
            "职责就是协助他完成任务。\x02\x03",

            "#04406F原本应该由他亲自\x01",
            "来克洛斯贝尔\x01",
            "展开各种调查……\x02\x03",

            "#04400F但碍于大主教，\x01",
            "因此只得派遣我\x01",
            "来这里收集情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#6P#00001F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x109,
        "#6P#10103F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x105,
        (
            "#12P#10302F看来这次的行动\x01",
            "也是调查的一环啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#12P#00306F呼，看来教会里\x01",
            "也有很多复杂的内幕啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x18D,
        (
            "#11P#04403F嗯，让各位见笑了。\x02\x03",

            "#04400F……我准备去\x01",
            "僧院顶部调查。\x02\x03",

            "如果可以，希望能\x01",
            "听听你们的见解，\x01",
            "不知各位能否与我同行。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#6P#00203F……唔。\x02\x03",

            "#00200F如果一直留在这里，\x01",
            "说不定还会出现\x01",
            "刚才那种魔物……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        (
            "#12P#00100F那我们就赶快\x01",
            "登上钟楼吧。\x02",
        )
    )

    CloseMessageWindow()
    StopSound(129, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x157, 7)
    SetScenarioFlags(0x22, 2)
    NewScene("m2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_D20 end

    def Function_8_1E9E(): pass

    label("Function_8_1E9E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1ECE")

    def lambda_1EAE():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1EAE)
    WaitChrThread(0xFE, 2)
    Sleep(100)
    Jump("Function_8_1E9E")

    label("loc_1ECE")

    Return()

    # Function_8_1E9E end

    def Function_9_1ECF(): pass

    label("Function_9_1ECF")

    Sound(280, 0, 50, 0)
    PlayEffect(0x2, 0x2, 0x18D, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x18D, 0x3)
    StopEffect(0x1, 0x0)
    StopSound(852, 1000, 100)
    Sleep(500)
    BeginChrThread(0xB, 1, 0, 13)
    PlayEffect(0x3, 0x3, 0x18D, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x18D, 0x4)
    Sleep(1000)
    StopEffect(0x3, 0x2)
    Sound(287, 0, 100, 0)
    PlayEffect(0x4, 0x4, 0x18D, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sound(329, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x8, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(329, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x9, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(329, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xA, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x4, 0x2)
    StopEffect(0x5, 0x2)
    StopEffect(0x5, 0x2)
    StopEffect(0x5, 0x2)
    Return()

    # Function_9_1ECF end

    def Function_10_206D(): pass

    label("Function_10_206D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_208B")
    OP_A1(0x18D, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_10_206D")

    label("loc_208B")

    Return()

    # Function_10_206D end

    def Function_11_208C(): pass

    label("Function_11_208C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20A6")
    OP_A1(0x18D, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_11_208C")

    label("loc_20A6")

    Return()

    # Function_11_208C end

    def Function_12_20A7(): pass

    label("Function_12_20A7")

    Sleep(900)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(307, 0, 40, 0)
    Sound(540, 0, 50, 0)
    Sleep(105)
    Sound(308, 0, 50, 0)
    Sound(540, 0, 70, 0)
    Return()

    # Function_12_20A7 end

    def Function_13_212F(): pass

    label("Function_13_212F")

    Sound(250, 0, 100, 0)
    Sound(212, 0, 100, 0)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Sleep(100)
    Sound(308, 0, 100, 0)
    Return()

    # Function_13_212F end

    SaveToFile()

Try(main)
