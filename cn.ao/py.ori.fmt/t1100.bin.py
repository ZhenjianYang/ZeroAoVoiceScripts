from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1100.bin",                # FileName
        "t1100",                    # MapName
        "t1100",                    # Location
        0x0046,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 70, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1100",                  # 0
        "猎兵扎克斯",             # 1
        "猎兵",                   # 2
        "猎兵",                   # 3
        "猎兵",                   # 4
        "猎兵",                   # 5
        "军犬",                   # 6
        "军犬",                   # 7
        "SE控制",                 # 8
        "bt1010",                 # 9
        "翠雀酒店方向",           # 10
    ))

    ATBonus("ATBonus_280", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_340", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 10, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_324", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_328", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_32C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_330", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_334", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_338", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_360", 0x004A, 255, 6, 45, 3, 3, 30, 0, "bt1010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42002.dat", "ms41902.dat", "ms41902.dat", "ms86100.dat", "ms86100.dat", 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_320", "ed7540", "ed7453", "ATBonus_280"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51706.itc",                   # 00
        "chr/ch00000.itc",                   # 01
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   0.0,                   1.5,                   -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -0.5,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 18,  0.0,                   0.0,                   -1.0,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -0.0,                  0.19999998807907104,   1.0])

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "翠雀酒店方向")

    ChipFrameInfo(1008, 0)                                       # 0

    ScpFunction((
        "Function_0_3F0",          # 00, 0
        "Function_1_411",          # 01, 1
        "Function_2_4C6",          # 02, 2
        "Function_3_1538",         # 03, 3
        "Function_4_154B",         # 04, 4
        "Function_5_155E",         # 05, 5
        "Function_6_1568",         # 06, 6
        "Function_7_1583",         # 07, 7
        "Function_8_15A4",         # 08, 8
        "Function_9_15C5",         # 09, 9
        "Function_10_1BFA",        # 0A, 10
        "Function_11_1C17",        # 0B, 11
        "Function_12_1C34",        # 0C, 12
        "Function_13_1C4C",        # 0D, 13
        "Function_14_1C64",        # 0E, 14
        "Function_15_1C8D",        # 0F, 15
        "Function_16_1CA3",        # 10, 16
        "Function_17_2259",        # 11, 17
        "Function_18_22F3",        # 12, 18
    ))


    def Function_0_3F0(): pass

    label("Function_0_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_401")
    Event(0, 2)

    label("loc_401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_410")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)

    label("loc_410")

    Return()

    # Function_0_3F0 end

    def Function_1_411(): pass

    label("Function_1_411")

    SetMapObjFrame(0xFF, "t1100_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1100_sky_y", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_44D")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_476")
    Call(0, 17)

    label("loc_476")

    Sound(126, 1, 80, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4A3")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_4C5")

    label("loc_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_4C5")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)

    label("loc_4C5")

    Return()

    # Function_1_411 end

    def Function_2_4C6(): pass

    label("Function_2_4C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x52, 0xFF, 0xFF)
    LoadChrToIndex("apl/ch51323.itc", 0x1E)
    SetChrPos(0x101, 0, 0, -32000, 0)
    SetChrPos(0x153, 0, 0, -17000, 0)
    OP_68(0, 1000, -17000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1000, -21500, 6000)
    MoveCamera(0, 20, 0, 6000)
    SetCameraDistance(28000, 6000)
    Sleep(3500)

    def lambda_562():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_562)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xFA0)
    BeginChrThread(0xF, 1, 0, 7)

    #C0001
    ChrTalk(
        0x101,
        "#00001F#6P#N（竟然在这种地方……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1000, -16500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    #C0002
    ChrTalk(
        0x153,
        "#01108F#40W#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        "#00002F#12P#N琪雅，原来你在这里啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x153, 0xB4, 0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    #C0004
    ChrTalk(
        0x153,
        "#01102F#5P罗伊德……\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, -17000, 5000)
    SetCameraDistance(21000, 5000)

    def lambda_6AE():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFBD98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AE)

    def lambda_6C8():

        label("loc_6C8")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6C8")

    QueueWorkItem2(0x153, 2, lambda_6C8)
    Sleep(4000)

    def lambda_6DD():
        OP_96(0xFE, 0x1F4, 0x0, 0xFFFFBD98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_6DD)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 1)
    EndChrThread(0x153, 0x2)
    OP_6F(0x79)
    Fade(1000)
    OP_68(3790, 500, 33620, 0)
    MoveCamera(26, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(80770, 0)
    PlaceName2(340, 40, "c_plac73", 0x0, 3000)
    MoveCamera(37, 23, 0, 8000)
    OP_6F(0x40)
    Sleep(500)

    #C0005
    ChrTalk(
        0x101,
        (
            "#00004F#12P#N哈哈，真令人怀念啊。\x02\x03",

            "#00000F……还记得吗？\x01",
            "我们当时就是一起从这里逃走的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0006
    ChrTalk(
        0x153,
        (
            "#01104F#12P#N嘿嘿嘿……\x01",
            "当然不可能忘记。\x02\x03",

            "#01121F因为琪雅的记忆\x01",
            "就是从这里开始的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00002F#12P#N……说得也是。\x02\x03",

            "#00008F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0008
    ChrTalk(
        0x153,
        (
            "#01103F#12P#N罗伊德……\x02\x03",

            "#01101F虽然琪雅当时是在这个地方出现的……\x01",
            "但以前应该一直都待在其它地方吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00003F#12P#N嗯……\x02\x03",

            "#00001F……你果然很在意\x01",
            "自己的身世啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0010
    ChrTalk(
        0x153,
        (
            "#01106F#12P#N……嗯。\x02\x03",

            "不知为什么，最近渐渐开始\x01",
            "在意这个问题了……\x02\x03",

            "#01108F虽然你们早就告诉过我，\x01",
            "说我是在很久以前出生的……\x02\x03",

            "#01112F但我直到最近才理解\x01",
            "其中的含义……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0011
    ChrTalk(
        0x101,
        "#00008F#12P#N是吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1000, -17000, 0)
    MoveCamera(42, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(19000, 50000)
    OP_0D()
    OP_93(0x153, 0x0, 0x1F4)
    Sleep(300)

    #C0012
    ChrTalk(
        0x153,
        (
            "#01122F#11P嘿嘿……\x02\x03",

            "#01121F一直都有罗伊德、艾莉……\x01",
            "还有缇欧、兰迪和大家陪着我……\x02\x03",

            "滴、隆他们，\x01",
            "还有玛布尔老师也都对我很好……\x02\x03",

            "#01108F每天都过得非常开心……\x02\x03",

            "#01106F#30W但偶尔……偶尔却会觉得\x01",
            "自己是孤独无依的……\x02\x03",

            "#30W……就像被遗忘在了\x01",
            "漆黑的空洞中……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x190)
    Sleep(150)

    #C0013
    ChrTalk(
        0x101,
        "#00001F#6P琪雅……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(670, 1000, -16940, 1500)
    Sleep(400)

    def lambda_B5E():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5E)
    OP_93(0x153, 0x10E, 0x190)
    WaitChrThread(0x101, 1)
    Fade(250)
    Sound(898, 0, 70, 0)
    BeginChrThread(0x101, 3, 0, 3)
    BeginChrThread(0x153, 3, 0, 4)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x153, 3)
    OP_0D()
    OP_6F(0x1)

    #C0014
    ChrTalk(
        0x153,
        (
            "#01123F#40W#11P对不起……对不起。\x02\x03",

            "我本来并不想把这种话\x01",
            "说出来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00006F#6P傻孩子，何必这么见外呢。\x02\x03",

            "#00008F你是觉得……很难开口吧？\x02\x03",

            "#00001F因为不想让本来就已经很消沉\x01",
            "的我们再为你担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x153,
        "#01114F#40W#11P…………（点头）\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#00000F#6P其实……你恰恰想错了，琪雅。\x02\x03",

            "#00004F琪雅依靠我们，找我们倾诉，\x01",
            "反倒能使我们振奋精神呢。\x02\x03",

            "在这种情况下，我们会在心里对自己说\x01",
            "『绝不能输』，从而鼓起干劲。\x02\x03",

            "#00002F所以，你根本就不必那么见外哦。\x02\x03",

            "#00009F至少还有我会永远\x01",
            "守护在琪雅身边的。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x153,
        (
            "#01102F#30W#11P…………啊………………\x02\x03",

            "#30W#01104F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x153)
    Fade(250)
    Sound(812, 0, 70, 0)
    BeginChrThread(0x101, 3, 0, 5)
    BeginChrThread(0x153, 3, 0, 6)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x153, 3)
    OP_0D()
    Sleep(150)

    #C0019
    ChrTalk(
        0x153,
        "#01109F#11P嘿嘿嘿，谢谢。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A1(0x153, 0x4B0, 0x6, 0x7, 0x8, 0x7, 0x6, 0x7, 0x8)
    Sleep(150)

    #C0020
    ChrTalk(
        0x153,
        (
            "#01101F#11P可是，这样一来，\x01",
            "就没人愿意嫁给你了吧？\x02\x03",

            "带着我这种小累赘，\x01",
            "女孩子们肯定都会躲得远远的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0021
    ChrTalk(
        0x101,
        (
            "#00012F#6P你这些乱七八糟的东西……\x01",
            "到底是从哪里学来的啊？\x02\x03",

            "#00011F哎，莫非是在图书馆\x01",
            "的图书中看到的？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x153,
        (
            "#01111F#11P嗯……也有这方面的原因吧。\x02\x03",

            "#01100F只要在市里和各种各样的人聊天，\x01",
            "不知不觉就能了解到这些事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00006F#6P想学习知识也要适可而止啊……\x02\x03",

            "#00000F话说回来，\x01",
            "我离结婚还早呢。\x02\x03",

            "我大哥也是在二十五岁左右的时候\x01",
            "才有了结婚的打算。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x153,
        (
            "#01105F#11P罗伊德的大哥？\x02\x03",

            "#01106F……已经\x01",
            "不在了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00004F#6P嗯，已经过世很久了。\x02\x03",

            "#00000F我现在的年纪比大哥离世时小七岁……\x01",
            "在成为能够独当一面的男子汉之前，\x01",
            "不会去考虑结婚的事情。\x02\x03",

            "#00012F再说，现在本来\x01",
            "也没有结婚的对象啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x153)
    Sleep(100)
    OP_A1(0x153, 0x5DC, 0x4, 0x7, 0x6, 0x7, 0x8)
    Sleep(200)

    #C0026
    ChrTalk(
        0x153,
        (
            "#01105F#11P七年之后……\x02\x03",

            "琪雅几岁？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#00005F#6P哦，你现在九岁……\x02\x03",

            "#00004F七年后就十六岁了……\x01",
            "哈哈，比现在的缇欧还大呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x153,
        (
            "#01103F#11P嗯……\x02\x03",

            "#01101F到了那个年纪以后，\x01",
            "琪雅就可以结婚了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0029
    ChrTalk(
        0x101,
        (
            "#00011F#6P#4S哎哎！？\x02\x03",

            "#00006F不不，再怎么说，\x01",
            "十六岁结婚也太早了吧！？\x02\x03",

            "#00008F不过，只要监护人同意，\x01",
            "年满十六岁就可以结婚了……\x02\x03",

            "#00007F还、还是不行！\x01",
            "我是绝对不会同意的！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x153,
        (
            "#01111F#11P唔……并不是\x01",
            "那个意思啦。\x02\x03",

            "#01104F……嘿嘿嘿，不过……是这样啊……\x02\x03",

            "#01121F琪雅根本就不必担心……\x01",
            "对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#00004F#6P当然，没有任何事情需要担心。\x02\x03",

            "#00000F好啦，我们差不多\x01",
            "也该去主题公园了。\x02\x03",

            "你不是一直都很期待吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x153,
        (
            "#01109F#11P嘿嘿嘿……\x02\x03",

            "#01110F滴还让我回去之后\x01",
            "告诉她主题公园是个\x01",
            "什么样的地方呢。\x02\x03",

            "而且我们约好了，等滴的眼睛\x01",
            "治好以后，要一起来这里玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00004F#6P是吗……\x02\x03",

            "#00002F好，既然如此，\x01",
            "我们就更要尽兴游玩了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x153, 0x5DC, 0x6, 0x9, 0xA, 0xB, 0xA, 0x9, 0x8)
    Sleep(100)

    #C0034
    ChrTalk(
        0x153,
        "#01109F#11P嗯！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    ClearChrFlags(0x153, 0x2)
    OP_49()
    OP_D7(0x1E)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    BeginChrThread(0xF, 1, 0, 8)
    SetChrPos(0x0, 0, 0, -12000, 180)
    SetScenarioFlags(0x145, 2)
    OP_29(0xA5, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_2_4C6 end

    def Function_3_1538(): pass

    label("Function_3_1538")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x10, 0x11, 0x12)
    Return()

    # Function_3_1538 end

    def Function_4_154B(): pass

    label("Function_4_154B")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_4_154B end

    def Function_5_155E(): pass

    label("Function_5_155E")

    OP_A1(0xFE, 0x3E8, 0x3, 0x13, 0x14, 0x15)
    Return()

    # Function_5_155E end

    def Function_6_1568(): pass

    label("Function_6_1568")

    SetChrPos(0xFE, 750, 0, -17000, 270)
    OP_A1(0xFE, 0x3E8, 0x3, 0x3, 0x4, 0x5)
    Return()

    # Function_6_1568 end

    def Function_7_1583(): pass

    label("Function_7_1583")

    OP_25(0x7E, 0x46)
    Sleep(200)
    OP_25(0x7E, 0x3C)
    Sleep(200)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x7E, 0x28)
    Sleep(200)
    OP_25(0x7E, 0x1E)
    Return()

    # Function_7_1583 end

    def Function_8_15A4(): pass

    label("Function_8_15A4")

    OP_25(0x7E, 0x28)
    Sleep(200)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x7E, 0x3C)
    Sleep(200)
    OP_25(0x7E, 0x46)
    Sleep(200)
    OP_25(0x7E, 0x50)
    Return()

    # Function_8_15A4 end

    def Function_9_15C5(): pass

    label("Function_9_15C5")

    EventBegin(0x0)
    FadeToDark(300, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00251.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch00351.itc", 0x23)
    LoadChrToIndex("chr/ch02950.itc", 0x24)
    LoadChrToIndex("chr/ch02951.itc", 0x25)
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch03151.itc", 0x27)
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch03251.itc", 0x29)
    LoadChrToIndex("chr/ch41950.itc", 0x2A)
    LoadChrToIndex("chr/ch41951.itc", 0x2B)
    LoadChrToIndex("chr/ch41952.itc", 0x2C)
    LoadChrToIndex("chr/ch42050.itc", 0x2D)
    LoadChrToIndex("chr/ch42051.itc", 0x2E)
    LoadChrToIndex("monster/ch86150.itc", 0x2F)
    LoadChrToIndex("monster/ch86151.itc", 0x30)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 600, 0, 5100, 0)
    OP_90(0x103, 500, 0, 3300, 0)
    OP_90(0x104, -700, 0, 5200, 0)
    OP_90(0x105, -500, 0, 3500, 0)
    OP_90(0x106, 1500, 0, 4350, 0)
    OP_90(0x109, -1500, 0, 4050, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x24)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x28)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 0x2F)
    SetChrChipByIndex(0xE, 0x2F)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 10)
    BeginChrThread(0xE, 0, 0, 10)
    SetChrPos(0x8, 0, 0, 20000, 180)
    SetChrPos(0x9, -2000, 0, 19500, 180)
    SetChrPos(0xC, 2000, 0, 19500, 180)
    SetChrPos(0xD, -1300, 0, 23000, 180)
    SetChrPos(0xE, 1300, 0, 23000, 180)
    OP_68(0, 1000, 17000, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(18500, 3000)
    FadeToBright(1000, 0)
    BeginChrThread(0xF, 1, 0, 15)

    def lambda_181B():
        OP_9B(0x0, 0x101, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_181B)
    Sleep(50)

    def lambda_1833():
        OP_9B(0x0, 0x103, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1833)
    Sleep(50)

    def lambda_184B():
        OP_9B(0x0, 0x104, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_184B)
    Sleep(50)

    def lambda_1863():
        OP_9B(0x0, 0x109, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1863)
    Sleep(50)

    def lambda_187B():
        OP_9B(0x0, 0x105, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_187B)
    Sleep(50)

    def lambda_1893():
        OP_9B(0x0, 0x106, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1893)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(0, 1000, 16000, 0)
    OP_68(350, 1000, 17640, 1500)
    MoveCamera(41, 16, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0035
    ChrTalk(
        0x8,
        (
            "#5P啧，没想到你们会发动急袭，\x01",
            "一路硬闯过来……！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#00312F#12P扎克斯，\x01",
            "你驻守在这里，也就表示……\x01",
            "这是最后一道关卡了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        "#5P……不错，兰道夫队长。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#5P但我们身为『赤色星座』的成员，\x01",
            "绝对不会让你们\x01",
            "通过此处！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0039
    ChrTalk(
        0x8,
        "#5P#4S各位！拿出干劲来！\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    #C0040
    ChrTalk(
        0x8,
        (
            "#5P如果守不住这里，\x01",
            "副团长和大小姐一定会宰了我们！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0x9C4, 0xFA)

    #C0041
    ChrTalk(
        0x9,
        "#5P是！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0x9C4, 0xFA)

    #C0042
    ChrTalk(
        0xC,
        "#5P全力干掉他们！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#00007F#12P正合我意！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x106,
        (
            "#10707F#12P彩虹剧团的那笔帐，\x01",
            "现在就要你们偿还……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(11000, 500)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    BeginChrThread(0x8, 3, 0, 13)
    BeginChrThread(0x9, 3, 0, 12)
    BeginChrThread(0xC, 3, 0, 12)
    BeginChrThread(0xD, 3, 0, 14)
    BeginChrThread(0xE, 3, 0, 14)

    def lambda_1B2C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B2C)

    def lambda_1B41():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B41)

    def lambda_1B56():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B56)

    def lambda_1B6B():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1B6B)

    def lambda_1B80():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1B80)

    def lambda_1B95():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1B95)
    Sleep(200)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x106, 0x1)
    Battle("BattleInfo_360", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 16)
    Return()

    # Function_9_15C5 end

    def Function_10_1BFA(): pass

    label("Function_10_1BFA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C16")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_10_1BFA")

    label("loc_1C16")

    Return()

    # Function_10_1BFA end

    def Function_11_1C17(): pass

    label("Function_11_1C17")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C33")
    OP_A1(0xFE, 0x960, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_11_1C17")

    label("loc_1C33")

    Return()

    # Function_11_1C17 end

    def Function_12_1C34(): pass

    label("Function_12_1C34")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
    Return()

    # Function_12_1C34 end

    def Function_13_1C4C(): pass

    label("Function_13_1C4C")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
    Return()

    # Function_13_1C4C end

    def Function_14_1C64(): pass

    label("Function_14_1C64")

    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 11)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
    Return()

    # Function_14_1C64 end

    def Function_15_1C8D(): pass

    label("Function_15_1C8D")

    Sleep(2200)
    Sound(805, 0, 70, 0)
    Sound(531, 0, 70, 0)
    Sound(540, 0, 20, 0)
    Return()

    # Function_15_1C8D end

    def Function_16_1CA3(): pass

    label("Function_16_1CA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("chr/ch42053.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00356.itc", 0x26)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 600, 0, 16100, 0)
    OP_90(0x103, 500, 0, 14300, 0)
    OP_90(0x104, -700, 0, 16200, 0)
    OP_90(0x105, -500, 0, 14500, 0)
    OP_90(0x106, 1500, 0, 15350, 0)
    OP_90(0x109, -1500, 0, 15050, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    Call(0, 17)
    SetChrPos(0x9, -2500, 0, 21000, 0)
    SetChrPos(0xC, 2000, 0, 22500, 45)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x3)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 200, 0, 19100, 180)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    VolumeBGM(0x32, 0x7D0)
    OP_68(-360, 1000, 18310, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15250, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14250, 2000)
    OP_6F(0x79)
    OP_0D()

    def lambda_1E64():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1E64)
    WaitChrThread(0x8, 2)
    Sleep(500)

    #C0045
    ChrTalk(
        0x8,
        (
            "#5P#40W……啧……\x01",
            "兰道夫队长……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#5P#40W你比在团里的时候……\x01",
            "还要强得多呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#00306F#12P嗯，我毕竟在如今的工作岗位上\x01",
            "经受过各种锻炼。\x02\x03",

            "#00300F这就是战斗经验的差距，是经验啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#5P#40W呼……\x01",
            "战斗经验居然比每天都在战斗\x01",
            "的我们还要丰富吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#5P#40W那到底是什么工作岗位……\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_1FAE():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1FAE)
    WaitChrThread(0x8, 2)
    Sleep(500)
    Fade(500)
    Sound(514, 0, 100, 0)
    OP_68(-230, 1000, 18600, 500)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, -500, 0, 18250, 0)
    OP_0D()
    Sleep(300)

    #C0050
    ChrTalk(
        0x8,
        "#60W#5P#2S……小……心………\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#60W#5P#2S里面有………\x01",
            "………那些家伙的………\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        "#60W#5P#2S………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #C0053
    ChrTalk(
        0x101,
        "#00008F#12P……昏过去了？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#00306F#11P嗯……\x01",
            "完全失去意识了。\x02\x03",

            "#00311F『那些家伙的』……？\x01",
            "那是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#00208F#12P也许是某些机关陷阱，\x01",
            "或是其他敌人……？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        (
            "#10403F#12P唔，虽然不清楚，\x01",
            "但还是小心一些为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x109,
        (
            "#10101F#12P……如果需要疗伤，\x01",
            "最好趁现在处理一下。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14500, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x64, 0x7D0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    Call(0, 17)
    SetChrPos(0x0, 0, 0, 11900, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 0)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_1CA3 end

    def Function_17_2259(): pass

    label("Function_17_2259")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, 1100, 0, 15000, 0)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, -2500, 0, 18000, 0)
    SetChrChipByIndex(0xC, 0x0)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, 2000, 0, 19500, 45)
    Return()

    # Function_17_2259 end

    def Function_18_22F3(): pass

    label("Function_18_22F3")

    EventBegin(0x1)

    #C0058
    ChrTalk(
        0x101,
        (
            "#00000F这边是迎宾馆。\x02\x03",

            "在出席今晚的晚餐会之前，\x01",
            "并不需要过去。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 200, -1700, 180)
    OP_68(0, 700, -1700, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(37000, 0)
    EventEnd(0x4)
    Return()

    # Function_18_22F3 end

    SaveToFile()

Try(main)
