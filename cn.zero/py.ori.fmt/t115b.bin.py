from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t115b.bin",                # FileName
        "t115b",                    # MapName
        "t115b",                    # Location
        0x0049,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 73, 0, 2, 0, 3],
    )

    BuildStringList((
        "t115b",                  # 0
        "客人",                   # 1
        "雷克特",                 # 2
        "犬１",                   # 3
        "犬２",                   # 4
        "犬３",                   # 5
        "SE控制",                 # 6
        "bt114b",                 # 7
    ))

    ATBonus("ATBonus_2A4", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_2E4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_348", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_34C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_350", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_354", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_358", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_35C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_360", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_364", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt114b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67100.dat", "ms67100.dat", "ms67100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2E4", "MonsterBattlePostion_344", "ed7509", "ed7000", "ATBonus_2A4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch33100.itc",                   # 00
        "chr/ch00000.itc",                   # 01
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

    DeclNpc(-90,     0,       -270,    180,  385,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 5,   0.0,                   0.0,                   -1.0,                  2500.0,                [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 12,  0.0,                   0.0,                   -1.0,                  2500.0,                [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -0.0,                  0.20000000298023224,   1.0])

    ScpFunction((
        "Function_0_3EC",          # 00, 0
        "Function_1_4A4",          # 01, 1
        "Function_2_4CF",          # 02, 2
        "Function_3_50E",          # 03, 3
        "Function_4_54E",          # 04, 4
        "Function_5_640",          # 05, 5
        "Function_6_16BC",         # 06, 6
        "Function_7_1711",         # 07, 7
        "Function_8_1766",         # 08, 8
        "Function_9_17BB",         # 09, 9
        "Function_10_1810",        # 0A, 10
        "Function_11_1869",        # 0B, 11
        "Function_12_18C2",        # 0C, 12
        "Function_13_1F6A",        # 0D, 13
        "Function_14_1F86",        # 0E, 14
        "Function_15_1FA5",        # 0F, 15
        "Function_16_1FCA",        # 10, 16
    ))


    def Function_0_3EC(): pass

    label("Function_0_3EC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_42C"),
        (1, "loc_438"),
        (2, "loc_444"),
        (3, "loc_450"),
        (4, "loc_45C"),
        (5, "loc_468"),
        (6, "loc_474"),
        (SWITCH_DEFAULT, "loc_480"),
    )


    label("loc_42C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_438")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_444")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_450")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_45C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_468")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_474")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_480")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_48C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_4A3")

    Return()

    # Function_0_3EC end

    def Function_1_4A4(): pass

    label("Function_1_4A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CE")
    OP_94(0xFE, 0xFFFFF7A4, 0xFFFFF40C, 0x8CA, 0x8C0, 0x3E8)
    Sleep(300)
    Jump("Function_1_4A4")

    label("loc_4CE")

    Return()

    # Function_1_4A4 end

    def Function_2_4CF(): pass

    label("Function_2_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4DD")
    Jump("loc_50D")

    label("loc_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4EB")
    Jump("loc_50D")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_504")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_50D")

    label("loc_504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_50D")

    label("loc_50D")

    Return()

    # Function_2_4CF end

    def Function_3_50E(): pass

    label("Function_3_50E")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53E")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_547")

    label("loc_547")

    Sound(124, 1, 100, 0)
    Return()

    # Function_3_50E end

    def Function_4_54E(): pass

    label("Function_4_54E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E9")

    #C0001
    ChrTalk(
        0xFE,
        (
            "还有一些时间，\x01",
            "所以我正在参观这座宅邸。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "话说回来，这设备真是好惊人啊……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "能感受到哈尔特曼议长那\x01",
            "令人难以想象的权威呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_63C")

    label("loc_5E9")


    #C0004
    ChrTalk(
        0xFE,
        "话说回来，这设备真是好惊人啊……\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "议长宅邸想必也是由\x01",
            "著名建筑家设计的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63C")

    TalkEnd(0xFE)
    Return()

    # Function_4_54E end

    def Function_5_640(): pass

    label("Function_5_640")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch07400.itc", 0x1E)
    LoadChrToIndex("apl/ch50357.itc", 0x1F)
    LoadChrToIndex("apl/ch50358.itc", 0x20)
    LoadChrToIndex("apl/ch50359.itc", 0x21)
    LoadEffect(0x0, "eff\\mgm03_00.eff")
    LoadEffect(0x1, "eff\\mgm03_01.eff")
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03500.itp")
    FadeToBright(1000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_744")
    OP_68(-4460, 1750, -10210, 0)
    MoveCamera(30, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16910, 0)
    OP_68(-750, 1750, -5060, 6000)
    BeginChrThread(0x101, 3, 0, 6)
    BeginChrThread(0xEF, 3, 0, 7)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    OP_6F(0x1)
    Jump("loc_799")

    label("loc_744")

    OP_68(4460, 1750, -10210, 0)
    MoveCamera(330, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16910, 0)
    OP_68(750, 1750, -5060, 6000)
    BeginChrThread(0x101, 3, 0, 8)
    BeginChrThread(0xEF, 3, 0, 9)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    OP_6F(0x1)

    label("loc_799")

    OP_0D()
    Fade(1000)
    OP_68(0, -450, -4840, 0)
    MoveCamera(0, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15190, 0)
    OP_68(0, 1750, -4840, 4000)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xEF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_8E8")

    #C0006
    ChrTalk(
        0x101,
        (
            "#5103F#5P……我说，艾莉。\x02\x03",

            "#5108F把这种设备建造在室内，\x01",
            "你觉得大概需要花费多少米拉？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        (
            "#5306F#11P你、你就算问我，\x01",
            "我也估算不出来啊……\x02\x03",

            "#5308F这种设备，即使在贵族的城堡里，\x01",
            "应该也是十分罕见的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A82")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_9AB")

    #C0008
    ChrTalk(
        0x101,
        (
            "#5103F#5P……我说，缇欧。\x02\x03",

            "#5108F把这种设备建造在室内，\x01",
            "你觉得大概需要花费多少米拉？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        (
            "#5406F#11P这种问题，问我也没用……\x02\x03",

            "#5411F只是，看上去需要花费一笔\x01",
            "相当夸张的费用呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A82")

    label("loc_9AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_A82")

    #C0010
    ChrTalk(
        0x101,
        (
            "#5103F#5P……我说，兰迪。\x02\x03",

            "#5108F把这种设备建造在室内，\x01",
            "你觉得大概需要花费多少米拉？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        (
            "#5606F#11P不知道，也不想知道。\x02\x03",

            "#5601F只是，仅仅是这一座宅邸，\x01",
            "花费的金钱恐怕就和\x01",
            "建立一个小规模要塞差不多了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A82")

    BeginChrThread(0x9, 3, 0, 10)

    #C0012
    ChrTalk(
        0x101,
        (
            "#5106F#5P呼……哈尔特曼议长吗……\x02\x03",

            "#5113F虽说是个家世悠久的名门望族，\x01",
            "但没想到居然会拥有如此庞大的资产啊……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0013
    ChrTalk(
        0x9,
        "#3507F#4S哇！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B5D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5D)

    def lambda_B6A():
        OP_93(0xFE, 0x167, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B6A)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    #C0014
    ChrTalk(
        0x101,
        "#5111F#6P什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_BE7")

    #C0015
    ChrTalk(
        0x102,
        "#5301F#12P你、你是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C3A")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_C15")

    #C0016
    ChrTalk(
        0x103,
        "#5401F#12P……你是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C3A")

    label("loc_C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_C3A")

    #C0017
    ChrTalk(
        0x104,
        "#5601F#12P你是……！？\x02",
    )

    CloseMessageWindow()

    label("loc_C3A")

    OP_64(0x101)
    OP_64(0xEF)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0018
    AnonymousTalk(
        0x9,
        (
            "两位，晚上好啊。\x02\x03",

            "看样子，你们似乎盛装打扮了一番，\x01",
            "好像还挺合身的嘛。\x02\x03",

            "呵呵，看来你们还是知道出席\x01",
            "晚宴是要身着正装的呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0019
    ChrTalk(
        0x101,
        "#5106F#6P那个，你打扮成那样，有资格评论我们吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_DCD")

    #C0020
    ChrTalk(
        0x102,
        (
            "#5311F#12P你那种打扮，再怎么说也\x01",
            "太过随意了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4F")

    label("loc_DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_E0F")

    #C0021
    ChrTalk(
        0x103,
        "#5411F#12P……你穿成那样，一点说服力也没有呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E4F")

    label("loc_E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_E4F")

    #C0022
    ChrTalk(
        0x104,
        (
            "#5605F#12P再怎么说，\x01",
            "你打扮得也未免太过随意了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4F")


    #C0023
    ChrTalk(
        0x9,
        (
            "#3504F#5P哈尔特曼那个大叔也说了啊，\x01",
            "就像回到自己家里一样，\x01",
            "请大家尽情放松享乐吧。\x02\x03",

            "#3500F你们也不要那么拘谨，\x01",
            "玩得开心一点吧。\x02\x03",

            "#3507F当然啦，说到玩，和我比起来，\x01",
            "你们还差得远呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-1480, 1750, -4040, 0)
    MoveCamera(36, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14360, 0)
    SetChrPos(0x9, 0, 0, -1960, 180)
    OP_0D()
    Fade(250)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x5)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0024
    ChrTalk(
        0x101,
        "#5111F#6P哎……\x02",
    )

    CloseMessageWindow()
    OP_A1(0x9, 0x5DC, 0x2, 0x6, 0x7)
    Sleep(500)
    OP_A1(0x9, 0x5DC, 0x2, 0x0, 0x1)
    Sleep(500)
    OP_A1(0x9, 0x5DC, 0x2, 0x2, 0x3)

    #C0025
    ChrTalk(
        0x9,
        (
            "#3500F#5P嗯，我看看……\x02\x03",

            "#3509F好，就在那边吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    SetChrSubChip(0x9, 0x5)
    OP_68(3440, 1950, -3240, 0)
    MoveCamera(29, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14360, 0)
    SetChrPos(0x9, 8330, 350, -1270, 180)
    SetChrPos(0x101, 4120, 0, -1320, 90)
    SetChrPos(0xEF, 2210, 0, -2180, 90)
    OP_68(5440, 1950, -3150, 3000)
    OP_6F(0x1)
    OP_0D()
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    Sound(541, 0, 100, 0)
    OP_A1(0x9, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    Sleep(300)
    Sound(12, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 8330, -1000, -4850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0026
    ChrTalk(
        0x101,
        (
            "#5111F#6P等一下，你突然抛竿，\x01",
            "要做什么啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_11AF")

    #C0027
    ChrTalk(
        0x102,
        (
            "#5306F#6P#N难、难以置信……\x02\x03",

            "#5301F话说回来，这种地方\x01",
            "应该也钓不到鱼啊──\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1265")

    label("loc_11AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1207")

    #C0028
    ChrTalk(
        0x103,
        (
            "#5406F#6P#N太随便了……\x02\x03",

            "#5411F话说回来，这个地方\x01",
            "怎么可能钓到鱼──\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1265")

    label("loc_1207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1265")

    #C0029
    ChrTalk(
        0x104,
        (
            "#5606F#6P#N喂喂……\x01",
            "这也太随便了吧。\x02\x03",

            "#5601F说起来，这个地方\x01",
            "好像钓不到鱼啊──\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1265")

    Sleep(500)
    OP_A1(0x9, 0x3E8, 0x4, 0x3, 0x4, 0x5, 0x6)

    #C0030
    ChrTalk(
        0x9,
        (
            "#40A#3505F#5P#20W啊……#1000W……\x01",
            "#20W嗯#500W，#20W哦哦#500W，#20W哈#500W……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0031
    ChrTalk(
        0x9,
        "#3509F#4S#5P#10A来了来了～！\x02",
    )
    #Auto

    Sleep(1100)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)
    Sound(11, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 8330, -1000, -4850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x9, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_13B3")

    #C0032
    ChrTalk(
        0x102,
        "#5305F#6P#N……钓上来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_140C")

    label("loc_13B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_13E0")

    #C0033
    ChrTalk(
        0x103,
        "#5405F#6P#N……钓上来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_140C")

    label("loc_13E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_140C")

    #C0034
    ChrTalk(
        0x104,
        "#5605F#6P#N……真能钓上来啊。\x02",
    )

    CloseMessageWindow()

    label("loc_140C")

    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x9,
        (
            "#3500F#5P嗯，看来今天\x01",
            "收获不小呢。\x02\x03",

            "#3504F嗯，这个就送给小黑\x01",
            "当礼物好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#5106F#6P好像是一种\x01",
            "观赏用的金鱼呢……\x02\x03",

            "#5113F──不对，\x01",
            "这样做不太好吧！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x10)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(300)
    OP_93(0x9, 0x10E, 0x320)

    #C0037
    ChrTalk(
        0x9,
        (
            "#3509F#11P哈哈哈哈，那么，后会有期啦！\x02\x03",

            "#3502F呵呵，祝你们也\x01",
            "钓到大鱼哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#5105F#6P哎──\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 11)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xEF)
    WaitChrThread(0x9, 3)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Sleep(500)
    OP_68(2960, 1850, -3490, 2000)
    OP_6F(0x1)

    #C0039
    ChrTalk(
        0x101,
        "#5112F#5P#40W这个嘛……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_160D")

    #C0040
    ChrTalk(
        0x102,
        (
            "#5306F#6P呼，算啦……\x01",
            "就当什么都没看到吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1684")

    label("loc_160D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1647")

    #C0041
    ChrTalk(
        0x103,
        (
            "#5411F#6P……深究多虑\x01",
            "也只会浪费时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1684")

    label("loc_1647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1684")

    #C0042
    ChrTalk(
        0x104,
        (
            "#5606F#6P该怎么说呢……\x01",
            "还是不要和他太认真了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1684")

    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetChrPos(0x0, 0, 0, -1500, 180)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xA5, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_5_640 end

    def Function_6_16BC(): pass

    label("Function_6_16BC")

    SetChrPos(0x101, -4000, 0, 10, 90)

    def lambda_16D2():
        OP_95(0xFE, -1870, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16D2)
    WaitChrThread(0x101, 1)

    def lambda_16F0():
        OP_95(0xFE, -600, 0, -4350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16F0)
    WaitChrThread(0x101, 1)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_6_16BC end

    def Function_7_1711(): pass

    label("Function_7_1711")

    SetChrPos(0xEF, -5540, 130, 10, 90)

    def lambda_1727():
        OP_95(0xFE, -2480, 0, -150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1727)
    WaitChrThread(0xEF, 1)

    def lambda_1745():
        OP_95(0xFE, 600, 0, -4350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1745)
    WaitChrThread(0xEF, 1)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_7_1711 end

    def Function_8_1766(): pass

    label("Function_8_1766")

    SetChrPos(0x101, 4000, 0, 10, 90)

    def lambda_177C():
        OP_95(0xFE, 1870, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_177C)
    WaitChrThread(0x101, 1)

    def lambda_179A():
        OP_95(0xFE, -600, 0, -4350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_179A)
    WaitChrThread(0x101, 1)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_8_1766 end

    def Function_9_17BB(): pass

    label("Function_9_17BB")

    SetChrPos(0xEF, 5540, 130, 10, 90)

    def lambda_17D1():
        OP_95(0xFE, 2480, 0, -150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_17D1)
    WaitChrThread(0xEF, 1)

    def lambda_17EF():
        OP_95(0xFE, 600, 0, -4350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_17EF)
    WaitChrThread(0xEF, 1)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_9_17BB end

    def Function_10_1810(): pass

    label("Function_10_1810")

    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xFE, -10310, 0, -20, 180)

    def lambda_1831():
        OP_95(0xFE, 0, 0, -250, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1831)
    WaitChrThread(0xFE, 1)

    def lambda_184F():
        OP_95(0xFE, 0, 0, -3100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_184F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_1810 end

    def Function_11_1869(): pass

    label("Function_11_1869")

    OP_93(0xFE, 0x5A, 0x320)

    def lambda_1875():
        OP_95(0xFE, 15120, 0, 0, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1875)
    WaitChrThread(0xFE, 1)

    def lambda_1893():
        OP_95(0xFE, 16660, 0, 0, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1893)

    def lambda_18AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18AD)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_11_1869 end

    def Function_12_18C2(): pass

    label("Function_12_18C2")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_190F")
    LoadChrToIndex("monster/ch67150.itc", 0x23)
    LoadChrToIndex("monster/ch67151.itc", 0x24)
    LoadChrToIndex("monster/ch67152.itc", 0x25)
    Jump("loc_1921")

    label("loc_190F")

    LoadChrToIndex("monster/ch75650.itc", 0x23)
    LoadChrToIndex("monster/ch75651.itc", 0x24)
    LoadChrToIndex("monster/ch75652.itc", 0x25)

    label("loc_1921")

    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xC, 0x4)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A16")
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A16")

    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xA, -14100, 0, -240, 90)
    SetChrPos(0xB, -15770, 0, 850, 90)
    SetChrPos(0xC, -17360, 0, -440, 90)
    SetChrPos(0x101, 6750, 0, -20, 270)
    SetChrPos(0xEF, 8800, 350, 860, 270)
    SetChrPos(0x105, 9500, 350, -880, 270)
    SetChrPos(0x133, 7200, 350, -340, 270)
    OP_68(3000, 1600, -190, 0)
    MoveCamera(330, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16250, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15250, 1500)

    def lambda_1AF0():
        OP_95(0xFE, 2620, 0, 210, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AF0)

    def lambda_1B0A():
        OP_95(0xFE, 3820, 0, 1420, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1B0A)

    def lambda_1B24():
        OP_95(0xFE, 4650, 0, -870, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1B24)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)
    OP_0D()
    Sound(836, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-8950, 1600, -1070, 0)
    MoveCamera(305, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11500, 0)
    SetCameraDistance(14000, 1500)
    BeginChrThread(0xA, 0, 0, 13)
    BeginChrThread(0xB, 0, 0, 13)
    BeginChrThread(0xC, 0, 0, 13)
    BeginChrThread(0xD, 1, 0, 16)

    def lambda_1BFB():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BFB)

    def lambda_1C10():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C10)

    def lambda_1C25():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1C25)
    OP_6F(0x10)
    OP_0D()

    #C0043
    ChrTalk(
        0x133,
        (
            "#5805F#1P哇……！\x01",
            "好像来了很多哦！？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#0010F#1P唔……\x01",
            "竟然在屋内放狗！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xC, 1)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    Fade(1000)
    OP_68(-2740, 1200, 170, 0)
    MoveCamera(315, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15230, 0)
    OP_68(1640, 1200, 170, 1200)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 14)
    BeginChrThread(0xB, 0, 0, 14)
    BeginChrThread(0xC, 0, 0, 14)
    SetChrPos(0xA, -610, 0, -20, 90)
    SetChrPos(0xB, -2100, 0, 1450, 90)
    SetChrPos(0xC, -3870, 0, -1040, 90)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1DA7")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    Jump("loc_1DCE")

    label("loc_1DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1DBD")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_1DCE")

    label("loc_1DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1DCE")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_1DCE")

    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    OP_6F(0x1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1E0F")

    #C0045
    ChrTalk(
        0x102,
        "#0107F#11P必须想办法击退它们……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E7E")

    label("loc_1E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1E4B")

    #C0046
    ChrTalk(
        0x103,
        "#0207F#11P……总之，先想办法击退它们吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E7E")

    label("loc_1E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1E7E")

    #C0047
    ChrTalk(
        0x104,
        "#0307F#11P看来，也只有先击退它们了！\x02",
    )

    CloseMessageWindow()

    label("loc_1E7E")


    #C0048
    ChrTalk(
        0x105,
        "#0407F#12P……来了！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0xA, 3, 0, 15)
    Sleep(100)
    BeginChrThread(0xB, 3, 0, 15)
    BeginChrThread(0xC, 3, 0, 15)
    Sleep(200)
    Sound(814, 0, 100, 0)
    SetCameraDistance(12230, 400)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(400)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x3)
    Battle("BattleInfo_364", 0x0, 0x0, 0x0, 0x10, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrFlags(0x133, 0x80)
    SetChrBattleFlags(0x133, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x0, 0, 0, 0, 270)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xA7, 0)
    EventEnd(0x5)
    Return()

    # Function_12_18C2 end

    def Function_13_1F6A(): pass

    label("Function_13_1F6A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F85")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_13_1F6A")

    label("loc_1F85")

    Return()

    # Function_13_1F6A end

    def Function_14_1F86(): pass

    label("Function_14_1F86")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FA4")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_14_1F86")

    label("loc_1FA4")

    Return()

    # Function_14_1F86 end

    def Function_15_1FA5(): pass

    label("Function_15_1FA5")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    SetChrSubChip(0xFE, 0x3)
    OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1770, 0x0)
    Return()

    # Function_15_1FA5 end

    def Function_16_1FCA(): pass

    label("Function_16_1FCA")

    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Return()

    # Function_16_1FCA end

    SaveToFile()

Try(main)
