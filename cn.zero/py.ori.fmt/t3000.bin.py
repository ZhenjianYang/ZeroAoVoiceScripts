from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t3000.bin",                # FileName
        "t3000",                    # MapName
        "t3000",                    # Location
        0x005B,                     # MapIndex
        "ed7202",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 91, 0, 2, 0, 3],
    )

    BuildStringList((
        "t3000",                  # 0
        "玲",                     # 1
        "艾丝蒂尔",               # 2
        "约修亚",                 # 3
        "约鲁古老人",             # 4
        "魔兽",                   # 5
        "魔兽",                   # 6
        "魔兽",                   # 7
        "魔兽",                   # 8
        "魔兽",                   # 9
        "魔兽",                   # 10
        "SE控制",                 # 11
        "bt3000",                 # 12
        "玛因兹山道",             # 13
    ))

    ATBonus("ATBonus_330", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_410", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 4, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 12, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_400", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_404", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_408", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 5, 5, 45)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_430", 0x0062, 32, 6, 0, 0, 1, 0, 0, "bt3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75400.dat", "ms75400.dat", "ms76300.dat", "ms76300.dat", "ms76300.dat", "ms76300.dat", 0, 0, "MonsterBattlePostion_410", "MonsterBattlePostion_3F0", "ed7405", "ed7403", "ATBonus_330"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 14,  2.0,                   26.5,                  0.0,                   225.0,                 [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.3333333432674408,   -5.300000190734863,    -0.0,                  1.0])

    DeclActor(-7090,   0,       24320,   1200,    -7090,   2500,    24320,   0x007C, 0,  19, 0x0000)
    DeclActor(2070,    250,     26860,   1200,    2070,    1500,    26860,   0x007C, 0,  20, 0x0000)
    DeclActor(2000,    2500,    47300,   1200,    2000,    4000,    47300,   0x007C, 0,  21, 0x0000)

    PlaceName(-1.6100000143051147, 0.0, -23.0, 0x0000, 0x0000, "玛因兹山道")

    ScpFunction((
        "Function_0_4CC",          # 00, 0
        "Function_1_4E8",          # 01, 1
        "Function_2_505",          # 02, 2
        "Function_3_537",          # 03, 3
        "Function_4_59E",          # 04, 4
        "Function_5_FFB",          # 05, 5
        "Function_6_1020",         # 06, 6
        "Function_7_1045",         # 07, 7
        "Function_8_106A",         # 08, 8
        "Function_9_108F",         # 09, 9
        "Function_10_1724",        # 0A, 10
        "Function_11_1893",        # 0B, 11
        "Function_12_18B5",        # 0C, 12
        "Function_13_1D0D",        # 0D, 13
        "Function_14_3622",        # 0E, 14
        "Function_15_3A6A",        # 0F, 15
        "Function_16_5145",        # 10, 16
        "Function_17_5CD8",        # 11, 17
        "Function_18_5D01",        # 12, 18
        "Function_19_5D2D",        # 13, 19
        "Function_20_5D8E",        # 14, 20
        "Function_21_5E18",        # 15, 21
    ))


    def Function_0_4CC(): pass

    label("Function_0_4CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E7")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_4CC")

    label("loc_4E7")

    Return()

    # Function_0_4CC end

    def Function_1_4E8(): pass

    label("Function_1_4E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_504")
    OP_A1(0xFE, 0x4E2, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_4E8")

    label("loc_504")

    Return()

    # Function_1_4E8 end

    def Function_2_505(): pass

    label("Function_2_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51B")
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_536")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_536")

    Return()

    # Function_2_505 end

    def Function_3_537(): pass

    label("Function_3_537")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_55A")
    Jump("loc_59D")

    label("loc_55A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_59D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 4)), scpexpr(EXPR_END)), "loc_571")
    Jump("loc_59D")

    label("loc_571")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_590")
    ModifyEventFlags(1, 0, 0x80)
    OP_65(0x1, 0x1)
    OP_66(0x2, 0x1)
    Jump("loc_59D")

    label("loc_590")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_59D")

    label("loc_59D")

    Return()

    # Function_3_537 end

    def Function_4_59E(): pass

    label("Function_4_59E")

    EventBegin(0x0)
    Fade(500)
    OP_68(17500, 600, 38730, 0)
    MoveCamera(49, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(28710, 0)
    SetChrPos(0x101, 2000, 0, 26250, 0)
    SetChrPos(0x102, 1000, 0, 25000, 0)
    SetChrPos(0x103, 3000, 0, 25500, 0)
    SetChrPos(0x104, 2000, 0, 24000, 0)
    SetMapObjFlags(0x0, 0x1000)
    OP_68(1770, 3090, 45860, 10000)
    MoveCamera(45, 14, 0, 10000)
    SetCameraDistance(59000, 10000)
    PlaceName2(100, 200, "c_plac16", 0x0, 5000)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(2020, 1500, 25360, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17600, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0001
    ChrTalk(
        0x101,
        (
            "#11P#0001F嗯，还是和以前一样，\x01",
            "好像没人在呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        (
            "#6P#0104F不过，伊梅尔达夫人好像\x01",
            "刚才还跟这里的人联络过……\x02\x03",

            "#0100F小玲应该\x01",
            "也还逗留在这里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        (
            "#12P#0203F……虽然很微弱，\x01",
            "但我从建筑物里感受到了一点气息。\x02\x03",

            "#0200F不过不清楚\x01",
            "那是不是人的气息……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#11P#0005F连缇欧都不能确定吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)

    #C0005
    ChrTalk(
        0x104,
        (
            "#12P#0303F我说，罗伊德。\x02\x03",

            "#0301F如果约修亚他们之前说的\x01",
            "『结社』那件事是真的话……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_829():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_829)
    Sleep(50)

    def lambda_839():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_839)
    Sleep(50)

    def lambda_849():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_849)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0006
    ChrTalk(
        0x101,
        (
            "#5P#0006F……嗯，我也想过这个问题。\x02\x03",

            "#0001F这个工房与『结社』\x01",
            "或许存在一定关联——是吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        "#12P#0303F差不多吧。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#6P#0106F确、确实也有\x01",
            "那种可能性……\x02\x03",

            "#0108F不过，还是觉得太不可思议了，\x01",
            "所以一时还无法反应过来……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        (
            "#11P#0201F但从玲的情况来看的话，\x01",
            "也确实有点可能……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 20, -1, -1)
    SetChrName("老人的声音")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──原来如此，\x01",
            "你们就是玲所说的\x01",
            "警察小鬼吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
    Fade(500)
    MoveCamera(0, 27, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x101, 1, 0, 5)
    BeginChrThread(0x102, 1, 0, 6)
    BeginChrThread(0x103, 1, 0, 7)
    BeginChrThread(0x104, 1, 0, 8)
    OP_0D()
    Sleep(2000)
    EndChrThread(0x101, 0x1)

    def lambda_AAE():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AAE)
    EndChrThread(0x102, 0x1)

    def lambda_ABF():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABF)
    EndChrThread(0x103, 0x1)

    def lambda_AD0():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AD0)
    EndChrThread(0x104, 0x1)

    def lambda_AE1():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AE1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0011
    ChrTalk(
        0x101,
        "#5P#0005F啊……！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#6P#0105F这声音是从哪里传来的……！？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("老人的声音")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "看来你们是受伊梅尔达的\x01",
            "委托才来这里的吧……\x02\x03",

            "不过很不巧，我的作品\x01",
            "还没有廉价到\x01",
            "被区区掮客玩弄于股掌的地步。\x02\x03",

            "你们快给我回去吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x101,
        "#5P#0008F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#12P#0306F嘁，虽然您说的\x01",
            "也都是事实……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#5P#0203F我们确实无可反驳。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("老人的声音")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……呵呵，话虽如此……\x02\x03",

            "但你们不辞辛苦地来到这里，\x01",
            "如果连门都不让进，你们是不会死心的吧。\x02\x03",

            "看在你们关照过玲的份上，\x01",
            "倒也不是不能给你们一次机会。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0018
    ChrTalk(
        0x102,
        "#6P#0105F机会……吗？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#5P#0001F那到底是……？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("老人的声音")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "没什么，只是试试\x01",
            "你们的实力到了什么程度而已。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(809, 0, 100, 0)
    Sleep(600)

    def lambda_DE8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DE8)
    Sleep(50)

    def lambda_DF8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DF8)
    Sleep(50)

    def lambda_E08():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E08)
    Sleep(50)

    def lambda_E18():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E18)
    Sleep(300)
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("老人的声音")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──锁打开了。\x02\x03",

            "如果你们愿意尝试的话，\x01",
            "就打开门进来。\x02\x03",

            "呵呵，不过……\x01",
            "你们可要有所『觉悟』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    MoveCamera(35, 27, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_0D()
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0022
    ChrTalk(
        0x102,
        "#6P#0108F怎、怎么办……？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#11P#0001F看来，\x01",
            "只要我们一踏进这扇门，\x01",
            "就一定会发生点『什么』啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#12P#0301F应该不会\x01",
            "埋有地雷吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#11P#0206F……或许会比这\x01",
            "更加糟糕也说不定。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2000, 0, 25250, 0)
    ClearMapObjFlags(0x0, 0x1000)
    OP_29(0x30, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_4_59E end

    def Function_5_FFB(): pass

    label("Function_5_FFB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_101F")
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(500)
    Jump("Function_5_FFB")

    label("loc_101F")

    Return()

    # Function_5_FFB end

    def Function_6_1020(): pass

    label("Function_6_1020")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1044")
    OP_93(0x102, 0xE1, 0x1C2)
    Sleep(500)
    OP_93(0x102, 0x13B, 0x1C2)
    Sleep(500)
    Jump("Function_6_1020")

    label("loc_1044")

    Return()

    # Function_6_1020 end

    def Function_7_1045(): pass

    label("Function_7_1045")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1069")
    OP_93(0x103, 0x87, 0x1C2)
    Sleep(550)
    OP_93(0x103, 0x2D, 0x1C2)
    Sleep(550)
    Jump("Function_7_1045")

    label("loc_1069")

    Return()

    # Function_7_1045 end

    def Function_8_106A(): pass

    label("Function_8_106A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_108E")
    OP_93(0x104, 0x87, 0x1F4)
    Sleep(450)
    OP_93(0x104, 0xE1, 0x1F4)
    Sleep(450)
    Jump("Function_8_106A")

    label("loc_108E")

    Return()

    # Function_8_106A end

    def Function_9_108F(): pass

    label("Function_9_108F")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "开门进入\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10CF")
    Return()

    label("loc_10CF")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("monster/ch76350.itc", 0x22)
    LoadChrToIndex("monster/ch75450.itc", 0x23)
    LoadChrToIndex("monster/ch76352.itc", 0x24)
    OP_68(2000, 1500, 25500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 2000, 0, 26250, 0)
    SetChrPos(0x102, 1000, 0, 25000, 0)
    SetChrPos(0x103, 3000, 0, 25500, 0)
    SetChrPos(0x104, 2000, 0, 24000, 0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrChipByIndex(0xD, 0x22)
    SetChrChipByIndex(0xE, 0x22)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xC, -1000, 5000, 33250, 45)
    SetChrPos(0xD, -1000, 5250, 37250, 135)
    SetChrPos(0xE, 5000, 5500, 33250, 315)
    SetChrPos(0xF, 5000, 5750, 37250, 225)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 1, 0, 0)
    BeginChrThread(0xD, 1, 0, 0)
    BeginChrThread(0xE, 1, 0, 0)
    BeginChrThread(0xF, 1, 0, 0)
    SetChrChipByIndex(0x10, 0x23)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x10, 1000, 0, 28750, 180)
    SetChrPos(0x11, 3000, 0, 41250, 180)
    SetChrPos(0x11, 3000, 0, 41250, 180)
    OP_A7(0x10, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0x11, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    BeginChrThread(0x10, 1, 0, 1)
    BeginChrThread(0x11, 1, 0, 1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x0)

    def lambda_1331():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1331)
    Sleep(50)

    def lambda_134E():
        OP_97(0x102, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_134E)
    Sleep(50)

    def lambda_136B():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_136B)
    Sleep(50)

    def lambda_1388():
        OP_97(0x103, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1388)
    OP_68(2000, 1500, 34500, 5000)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0026
    ChrTalk(
        0x103,
        "#12P#0207F大家小心……！\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    WaitChrThread(0x101, 1)

    def lambda_140A():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_140A)
    WaitChrThread(0x102, 1)

    def lambda_141B():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_141B)
    WaitChrThread(0x104, 1)

    def lambda_142C():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_142C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    Fade(500)
    OP_68(320, 1500, 37700, 0)
    MoveCamera(269, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18870, 0)
    Sleep(500)
    BeginChrThread(0x12, 1, 0, 11)
    Sleep(1000)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0xB, 1, 0, 10)
    OP_68(1060, 1500, 34190, 7000)
    MoveCamera(53, 30, 0, 7000)
    OP_6E(510, 7000)
    SetCameraDistance(20000, 7000)

    def lambda_1503():
        OP_97(0x103, 0x0, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1503)
    WaitChrThread(0x103, 1)

    def lambda_1521():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1521)

    def lambda_152E():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_152E)

    def lambda_153B():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_153B)

    def lambda_1548():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1548)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    WaitChrThread(0xB, 1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0027
    ChrTalk(
        0x101,
        "#11P#0007F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        "#5P#0107F天、天使和怪物吗……！？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#5P#0310F喂喂！\x01",
            "这也太出人意料了吧！？\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 8000)
    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)

    #C0030
    ChrTalk(
        0x101,
        "#11P#0010F唔……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        "#5P#0307F来了啊！\x02",
    )

    CloseMessageWindow()
    Fade(200)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    SetChrChipByIndex(0xC, 0x24)
    SetChrChipByIndex(0xD, 0x24)
    SetChrChipByIndex(0xE, 0x24)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x1)
    SetChrSubChip(0xE, 0x2)
    SetChrSubChip(0xF, 0x3)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(16000, 400)
    Sleep(400)
    CancelBlur(0)
    Battle("BattleInfo_430", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 13)
    Return()

    # Function_9_108F end

    def Function_10_1724(): pass

    label("Function_10_1724")


    def lambda_1729():
        OP_97(0xC, 0x0, 0xFFFFEC78, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1729)

    def lambda_1743():
        OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1743)
    Sleep(50)

    def lambda_1757():
        OP_97(0xD, 0x0, 0xFFFFEB7E, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1757)

    def lambda_1771():
        OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_1771)
    Sleep(50)

    def lambda_1785():
        OP_97(0xE, 0x0, 0xFFFFEA84, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1785)

    def lambda_179F():
        OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_179F)
    Sleep(50)

    def lambda_17B3():
        OP_97(0xF, 0x0, 0xFFFFE98A, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_17B3)

    def lambda_17CD():
        OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_17CD)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xF, 3)
    Sound(868, 0, 100, 0)

    def lambda_1804():
        OP_97(0x10, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1804)

    def lambda_181E():
        OP_A7(0x10, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_181E)
    Sleep(50)

    def lambda_1832():
        OP_97(0x11, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1832)

    def lambda_184C():
        OP_A7(0x11, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_184C)
    WaitChrThread(0x10, 3)

    def lambda_1861():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1861)
    WaitChrThread(0x11, 3)

    def lambda_1876():
        OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1876)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x11, 3)
    Return()

    # Function_10_1724 end

    def Function_11_1893(): pass

    label("Function_11_1893")

    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)
    Return()

    # Function_11_1893 end

    def Function_12_18B5(): pass

    label("Function_12_18B5")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "开门进入\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18F5")
    Return()

    label("loc_18F5")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("monster/ch76350.itc", 0x22)
    LoadChrToIndex("monster/ch75450.itc", 0x23)
    LoadChrToIndex("monster/ch76352.itc", 0x24)
    OP_68(2000, 1500, 25500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 2000, 0, 26250, 0)
    SetChrPos(0x102, 1000, 0, 25000, 0)
    SetChrPos(0x103, 3000, 0, 25500, 0)
    SetChrPos(0x104, 2000, 0, 24000, 0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrChipByIndex(0xD, 0x22)
    SetChrChipByIndex(0xE, 0x22)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xC, -1000, 5000, 33250, 45)
    SetChrPos(0xD, -1000, 5250, 37250, 135)
    SetChrPos(0xE, 5000, 5500, 33250, 315)
    SetChrPos(0xF, 5000, 5750, 37250, 225)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 1, 0, 0)
    BeginChrThread(0xD, 1, 0, 0)
    BeginChrThread(0xE, 1, 0, 0)
    BeginChrThread(0xF, 1, 0, 0)
    SetChrChipByIndex(0x10, 0x23)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x10, 1000, 0, 28750, 180)
    SetChrPos(0x11, 3000, 0, 41250, 180)
    OP_A7(0x10, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0x11, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    BeginChrThread(0x10, 1, 0, 1)
    BeginChrThread(0x11, 1, 0, 1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x0)

    def lambda_1B46():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B46)
    Sleep(50)

    def lambda_1B63():
        OP_97(0x102, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B63)
    Sleep(50)

    def lambda_1B80():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B80)
    Sleep(50)

    def lambda_1B9D():
        OP_97(0x103, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B9D)
    OP_68(2000, 1500, 35500, 5000)
    OP_6F(0x79)
    StopBGM(0xFA0)
    OP_68(1060, 1500, 34190, 6000)
    MoveCamera(53, 30, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(20000, 7000)
    BeginChrThread(0x12, 1, 0, 11)
    BeginChrThread(0xB, 1, 0, 10)

    def lambda_1C09():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C09)

    def lambda_1C16():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C16)

    def lambda_1C23():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C23)

    def lambda_1C30():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C30)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xB, 1)
    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)
    Fade(200)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    SetChrChipByIndex(0xC, 0x24)
    SetChrChipByIndex(0xD, 0x24)
    SetChrChipByIndex(0xE, 0x24)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x1)
    SetChrSubChip(0xE, 0x2)
    SetChrSubChip(0xF, 0x3)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(16000, 400)
    Sleep(400)
    CancelBlur(0)
    Battle("BattleInfo_430", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 13)
    Return()

    # Function_12_18B5 end

    def Function_13_1D0D(): pass

    label("Function_13_1D0D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3124")
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("monster/ch76350.itc", 0x22)
    LoadChrToIndex("monster/ch75450.itc", 0x23)
    LoadChrToIndex("chr/ch06600.itc", 0x24)
    LoadEffect(0x0, "event\\ev503_00.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03900.itp")
    OP_68(1350, 1500, 34720, 0)
    MoveCamera(53, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16870, 0)
    SetCameraDistance(18870, 5000)
    SetChrPos(0x101, 2000, 0, 36250, 315)
    SetChrPos(0x102, 1000, 0, 35000, 225)
    SetChrPos(0x103, 3000, 0, 35500, 45)
    SetChrPos(0x104, 2000, 0, 34000, 135)
    SetChrPos(0xB, 2000, 2500, 46500, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x22)
    SetChrChipByIndex(0xD, 0x22)
    SetChrChipByIndex(0xE, 0x22)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xC, -1000, 0, 33250, 45)
    SetChrPos(0xD, -1000, 0, 37250, 135)
    SetChrPos(0xE, 5000, 0, 33250, 315)
    SetChrPos(0xF, 5000, 0, 37250, 225)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    BeginChrThread(0xC, 1, 0, 0)
    BeginChrThread(0xD, 1, 0, 0)
    BeginChrThread(0xE, 1, 0, 0)
    BeginChrThread(0xF, 1, 0, 0)
    SetChrChipByIndex(0x10, 0x23)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x10, 1000, 0, 30750, 0)
    SetChrPos(0x11, 3000, 0, 39250, 180)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    BeginChrThread(0x10, 1, 0, 1)
    BeginChrThread(0x11, 1, 0, 1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_1F7F():
        OP_A6(0xC, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1F7F)
    PlayEffect(0x0, 0x0, 0xC, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_1FD2():
        OP_A6(0xD, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1FD2)
    PlayEffect(0x0, 0x1, 0xD, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_2025():
        OP_A6(0xE, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2025)
    PlayEffect(0x0, 0x2, 0xE, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_2078():
        OP_A6(0xF, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2078)
    PlayEffect(0x0, 0x3, 0xF, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_20CB():
        OP_A6(0x10, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_20CB)
    PlayEffect(0x0, 0x4, 0x10, 0x0, 0, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_211E():
        OP_A6(0x11, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_211E)
    PlayEffect(0x0, 0x5, 0x11, 0x0, 0, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(868, 0, 100, 0)

    def lambda_217E():
        OP_A7(0xC, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_217E)
    Sleep(50)

    def lambda_2192():
        OP_A7(0xD, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_2192)
    Sleep(50)

    def lambda_21A6():
        OP_A7(0xE, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_21A6)
    Sleep(50)

    def lambda_21BA():
        OP_A7(0xF, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_21BA)
    Sleep(50)

    def lambda_21CE():
        OP_A7(0x10, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_21CE)
    Sleep(50)

    def lambda_21E2():
        OP_A7(0x11, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_21E2)
    WaitChrThread(0xC, 3)
    StopEffect(0x0, 0x2)

    def lambda_21FA():
        OP_A7(0xC, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_21FA)
    WaitChrThread(0xD, 3)
    StopEffect(0x1, 0x2)

    def lambda_2212():
        OP_A7(0xD, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_2212)
    WaitChrThread(0xE, 3)
    StopEffect(0x2, 0x2)

    def lambda_222A():
        OP_A7(0xE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_222A)
    WaitChrThread(0xF, 3)
    StopEffect(0x3, 0x2)

    def lambda_2242():
        OP_A7(0xF, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_2242)
    WaitChrThread(0x10, 3)
    StopEffect(0x4, 0x2)

    def lambda_225A():
        OP_A7(0x10, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_225A)
    WaitChrThread(0x11, 3)
    StopEffect(0x5, 0x2)

    def lambda_2272():
        OP_A7(0x11, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2272)
    WaitChrThread(0xC, 3)
    EndChrThread(0xC, 0x2)
    EndChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    WaitChrThread(0xD, 3)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xD, 0x1)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    WaitChrThread(0xE, 3)
    EndChrThread(0xE, 0x2)
    EndChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    WaitChrThread(0xF, 3)
    EndChrThread(0xF, 0x2)
    EndChrThread(0xF, 0x1)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    WaitChrThread(0x10, 3)
    EndChrThread(0x10, 0x2)
    EndChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    WaitChrThread(0x11, 3)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x11, 0x1)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    CancelBlur(0)
    OP_6F(0x10)
    Sleep(500)

    #C0032
    ChrTalk(
        0x101,
        "#11P#0010F这、这是……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#5P#0101F发条和齿轮……？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#11P#0201F看来……\x01",
            "好像是『人偶』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#5P#0306F喂喂，这算哪门子人偶啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 2)), scpexpr(EXPR_END)), "loc_23CF")

    #N0036
    NpcTalk(
        0xB,
        "老人的声音",
        (
            "哼……\x01",
            "浪费我的时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2432")

    label("loc_23CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 1)), scpexpr(EXPR_END)), "loc_240A")

    #N0037
    NpcTalk(
        0xB,
        "老人的声音",
        "算了，你们也就是这种程度吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2432")

    label("loc_240A")


    #N0038
    NpcTalk(
        0xB,
        "老人的声音",
        (
            "嗯，好像\x01",
            "还有点本事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2432")

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

    #C0039
    ChrTalk(
        0x101,
        "#11P#0005F啊……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)

    def lambda_24DF():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24DF)

    def lambda_24EC():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24EC)

    def lambda_24F9():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_24F9)

    def lambda_2506():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2506)
    OP_68(6130, 1500, 47630, 0)
    MoveCamera(53, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    OP_68(1580, 1500, 36060, 4500)
    MoveCamera(53, 24, 0, 4500)
    OP_6E(510, 4500)
    SetCameraDistance(15880, 4500)
    ClearChrFlags(0xB, 0x4)
    OP_97(0xB, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    SetChrFlags(0xB, 0x4)
    OP_6F(0x79)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0040
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "我叫约鲁古，\x01",
            "是罗赞贝尔克的人偶师。\x02\x03",

            "你们是克洛斯贝尔警察局·特别\x01",
            "任务支援科的小鬼们吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0041
    ChrTalk(
        0x101,
        "#12P#0001F是、是的……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#12P#0101F那个，您是从\x01",
            "小玲那边听说的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xB,
        (
            "#5P#3903F不用问那孩子，\x01",
            "我虽然隐居已久，\x01",
            "但这种程度的情报还是知道的。\x02\x03",

            "#3900F虽然有点无趣……\x01",
            "但约定就是约定，\x02\x03",

            "你们拿走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0xB, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x359),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x359, 1)
    OP_98(0xB, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)

    #C0045
    ChrTalk(
        0x101,
        "#12P#0005F谢、谢谢……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#11P#0205F……没想到您\x01",
            "这么轻易就交给我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xB,
        (
            "#5P#3903F呵呵……\x01",
            "人偶有人偶自己的命运。\x02\x03",

            "即使落到了卑鄙的掮客手里，\x01",
            "也有可能会遇到\x01",
            "一位值得托付的主人。\x02\x03",

            "#3900F……人偶也和人一样，\x01",
            "命运如何全要看女神的安排。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        "#12P#0305F原来如此啊……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        (
            "#12P#0106F您能这么想，\x01",
            "也是帮了我们一个大忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#12P#0013F不、不过……！\x02\x03",

            "#0007F刚才的天使和怪物\x01",
            "到底是什么啊！？\x02\x03",

            "莫非是玲所属的\x01",
            "那个『结社』的……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "#5P#3903F──班宁斯搜查官。\x02\x03",

            "#3901F……你现在有工夫来\x01",
            "关心那种事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x101,
        "#12P#0011F哎！？\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "#5P#3903F我只是个『人偶师』罢了，\x01",
            "仅此而已。\x02\x03",

            "现在你们所面对的，发生在此地的\x01",
            "各种问题……\x02\x03",

            "我跟那些，\x01",
            "都没有直接关系。\x02\x03",

            "#3901F即便是这样，你们还想\x01",
            "去窥探那深不见底的深渊吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        "#12P#0010F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        (
            "#5P#3903F玲也是一样……\x02\x03",

            "那孩子的命运\x01",
            "和你们也不会有\x01",
            "直接的关联。\x02\x03",

            "#3900F在你们担心这些没用的问题之前，\x01",
            "应该还有更值得你们关注的人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#12P#0005F啊……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#12P#0103F……是指小琪雅吧。\x02\x03",

            "#0101F她被当做您所制作的人偶，\x01",
            "成为了拍卖会的货物……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#11P#0201F不过，看来这些情报\x01",
            "您已经全都知晓了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#12P#0301F老爷爷，关于阿琪，\x01",
            "您知道些什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xB,
        (
            "#5P#3903F呵呵，我刚才说过了，\x01",
            "人偶有人偶自己的命运。\x02\x03",

            "#3900F我所制作的人偶，\x01",
            "在经过坎坷命运的历练后，\x01",
            "也有可能会获得生命，成为真正的人类。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        "#11P#0205F哎？\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#12P#0011F什么！？\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xB,
        (
            "#5P#3903F呵呵，不过印象中，\x01",
            "我好像没有做过跟那小女孩\x01",
            "一个模样的人偶。\x02\x03",

            "#3900F估计只是有人\x01",
            "冒用了罗赞贝尔克这名字而已吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        "#12P#0106F呼……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#12P#0006F……这玩笑可真刺激心脏啊。\x02\x03",

            "#0001F也就是说，您真的对\x01",
            "琪雅的事一无所知吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        (
            "#5P#3901F至少，她被混入竞拍会货物\x01",
            "这件事我不知道。\x02\x03",

            "对此，我想玲也一样不知道吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        "#12P#0008F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#12P#0308F哼，还以为或许\x01",
            "会有点线索……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        (
            "#12P#0105F话说回来……\x01",
            "小玲在里面吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        (
            "#5P#3903F不在，她刚好出门了。\x02\x03",

            "#3900F那孩子比较随心所欲，\x01",
            "所以你们来这里也见不到她的。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(300)
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

    #C0071
    ChrTalk(
        0x101,
        "#12P#0011F那、那个……！？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xB,
        (
            "#11P#3903F──话我就说到这里。\x02\x03",

            "你们快点把人偶\x01",
            "给伊梅尔达送去吧。\x02\x03",

            "#3900F跟她说，钱还是\x01",
            "汇到以往的账号里。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2000, 4000, 46500, 5000)
    ClearChrFlags(0xB, 0x4)
    OP_97(0xB, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    SetChrFlags(0xB, 0x4)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_79(0x1)

    def lambda_3018():
        OP_97(0xB, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3018)

    def lambda_3032():
        OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3032)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Sound(890, 0, 100, 0)
    OP_79(0x1)
    Sleep(1000)
    Sound(809, 0, 100, 0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(2000, 600, 36250, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, 2000, 0, 36250, 0)
    SetChrPos(0x1, 2000, 0, 36250, 0)
    SetChrPos(0x2, 2000, 0, 36250, 0)
    SetChrPos(0x3, 2000, 0, 36250, 0)
    ModifyEventFlags(1, 0, 0x80)
    OP_65(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_29(0x30, 0x1, 0x5)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Jump("loc_3621")

    label("loc_3124")

    LoadChrToIndex("chr/ch00053.itc", 0x1E)
    LoadChrToIndex("chr/ch00153.itc", 0x1F)
    LoadChrToIndex("chr/ch00253.itc", 0x20)
    LoadChrToIndex("chr/ch00353.itc", 0x21)
    OP_68(2200, 800, 25700, 0)
    MoveCamera(34, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19460, 0)
    SetChrPos(0x101, 2000, 0, 25250, 0)
    SetChrPos(0x102, 1000, 0, 24000, 0)
    SetChrPos(0x103, 3000, 0, 24500, 0)
    SetChrPos(0x104, 2000, 0, 23000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x101, 0x3)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x103, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    OP_71(0x0, 0xA, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_32(0xFF, 0xFE, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 2)), scpexpr(EXPR_END)), "loc_3333")
    SetMessageWindowPos(25, 20, -1, -1)
    SetChrName("老人的声音")

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──用蛮力是行不通的。\x02\x03",

            "曙光宣告人偶会反弹物理攻击，\x01",
            "如果不管它们的话，还会引发强烈的大爆炸。\x02\x03",

            "而天使们能够解除魔法，\x01",
            "所以这两者的组合可谓最强。\x02\x03",

            "想要战胜这个组合……\x01",
            "你们就必须用头脑来战斗。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x30, 0x1, 0x4)
    Jump("loc_356F")

    label("loc_3333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 1)), scpexpr(EXPR_END)), "loc_33E8")
    SetMessageWindowPos(25, 20, -1, -1)
    SetChrName("老人的声音")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──不行啊，真让人看不下去。\x02\x03",

            "天使们会迅速\x01",
            "解除魔法的驱动。\x02\x03",

            "采取以战技为中心的战术吧，\x01",
            "那样的话，应该能打得稍微像样一点了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD3, 2)
    OP_29(0x30, 0x1, 0x3)
    Jump("loc_356F")

    label("loc_33E8")

    SetMessageWindowPos(25, 20, -1, -1)
    SetChrName("老人的声音")

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──真不像话啊，\x01",
            "重新开始吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(2140, 800, 24900, 1500)
    MoveCamera(34, 22, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(18490, 1500)
    OP_6F(0x79)
    OP_A6(0x101, 0x0, 0x14, 0x1F4, 0x7D0)
    Sleep(300)

    #C0076
    ChrTalk(
        0x101,
        "#11P#0010F#30W呼……\x02",
    )

    CloseMessageWindow()
    OP_A6(0x102, 0x0, 0x14, 0x1F4, 0x7D0)
    Sleep(300)

    #C0077
    ChrTalk(
        0x102,
        "#6P#0108F#30W刚、刚才那些到底是什么……\x02",
    )

    CloseMessageWindow()
    OP_A6(0x103, 0x0, 0x14, 0x1F4, 0x7D0)
    Sleep(300)

    #C0078
    ChrTalk(
        0x103,
        (
            "#11P#0206F#30W怎么看都不像\x01",
            "是普通的魔兽啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x104, 0x0, 0x14, 0x1F4, 0x7D0)
    Sleep(300)

    #C0079
    ChrTalk(
        0x104,
        (
            "#12P#0301F#30W不管怎样，反正用一般的\x01",
            "办法肯定行不通……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD3, 1)
    OP_29(0x30, 0x1, 0x2)

    label("loc_356F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_68(2000, 600, 25250, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, 2000, 0, 25250, 0)
    SetChrPos(0x1, 2000, 0, 25250, 0)
    SetChrPos(0x2, 2000, 0, 25250, 0)
    SetChrPos(0x3, 2000, 0, 25250, 0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)

    label("loc_3621")

    Return()

    # Function_13_1D0D end

    def Function_14_3622(): pass

    label("Function_14_3622")

    EventBegin(0x0)
    Fade(500)
    OP_68(2000, 1500, 29500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17600, 0)
    SetChrPos(0x101, 2000, 0, 30250, 180)
    SetChrPos(0x102, 1000, 0, 29000, 180)
    SetChrPos(0x103, 3000, 0, 29500, 180)
    SetChrPos(0x104, 2000, 0, 28000, 180)
    OP_68(2000, 1500, 24500, 3000)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(120, 0, 100, 0)

    def lambda_36C3():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_36C3)
    Sleep(50)

    def lambda_36E0():
        OP_97(0x103, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_36E0)
    Sleep(50)

    def lambda_36FD():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36FD)
    Sleep(50)

    def lambda_371A():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_371A)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(120, 0, 100, 0)

    def lambda_3757():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3757)
    Sleep(50)

    def lambda_3767():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3767)
    Sleep(50)

    def lambda_3777():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3777)
    Sleep(50)

    def lambda_3787():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3787)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_79(0x0)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0080
    ChrTalk(
        0x101,
        "#11P#0008F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        (
            "#12P#0303F结社──『噬身之蛇』吗……\x02\x03",

            "#0301F虽然不知道刚才那位老爷爷\x01",
            "身份立场如何，\x01",
            "但那群人好像很不得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        (
            "#11P#0206F刚才的人偶……\x01",
            "即使是爱普斯泰恩财团\x01",
            "也做不出来啊。\x02\x03",

            "#0201F而利贝尔的ＺＣＦ好像\x01",
            "也才刚刚开始研究开发……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#6P#0106F罗赞贝尔克工房……\x01",
            "没想到这个地方\x01",
            "竟然会有如此多的谜团……\x02\x03",

            "#0108F……看样子，我们目前的确\x01",
            "没有余力探查下去呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#11P#0006F是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    TurnDirection(0x101, 0x104, 500)

    def lambda_39C4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39C4)
    Sleep(50)

    def lambda_39D4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_39D4)
    Sleep(300)

    #C0085
    ChrTalk(
        0x101,
        (
            "#5P#0000F……总之，先把这个箱子\x01",
            "送到古董店吧。\x02\x03",

            "伊梅尔达夫人还在等着我们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        "#12P#0300F嗯。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2000, 0, 25250, 0)
    ModifyEventFlags(0, 0, 0x80)
    OP_66(0x1, 0x1)
    OP_65(0x2, 0x1)
    SetScenarioFlags(0xD3, 4)
    EventEnd(0x5)
    Return()

    # Function_14_3622 end

    def Function_15_3A6A(): pass

    label("Function_15_3A6A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09500.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    OP_68(11740, 600, 78670, 0)
    MoveCamera(21, 13, 0, 0)
    MoveCamera(21, 11, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(103740, 0)
    SetChrPos(0x101, 680, 0, 12320, 0)
    SetChrPos(0x102, 1760, 0, 10960, 0)
    SetChrPos(0x103, -290, 0, 11070, 0)
    SetChrPos(0x104, 540, 0, 9730, 0)
    OP_68(12220, 600, 58030, 10000)
    PlaceName2(100, 200, "c_plac16", 0x0, 5000)
    FadeToBright(1000, 0)
    Sleep(4000)

    def lambda_3B57():
        OP_95(0xFE, 950, 0, 20480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B57)

    def lambda_3B71():
        OP_95(0xFE, 2040, 0, 19440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B71)

    def lambda_3B8B():
        OP_95(0xFE, -300, 0, 19600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3B8B)

    def lambda_3BA5():
        OP_95(0xFE, 620, 0, 18330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3BA5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(1210, 3000, 27080, 0)
    MoveCamera(27, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26530, 0)
    OP_68(1210, 600, 27080, 6000)
    OP_6F(0x1)
    OP_0D()

    #C0087
    ChrTalk(
        0x101,
        "#0005F#11P这里是……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        (
            "#0105F好有个性的建筑啊。\x02\x03",

            "#0101F看起来也不像是废墟，\x01",
            "应该有人居住吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x104, 0x13B, 0x1F4)

    #C0089
    ChrTalk(
        0x104,
        "#0305F哦，这里有个牌子。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    SetCameraDistance(22690, 0)
    OP_68(-5310, 800, 24820, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21610, 2500)
    SetChrPos(0x101, -6340, 120, 21700, 0)
    SetChrPos(0x102, -7980, 0, 21620, 0)
    SetChrPos(0x103, -8050, 0, 20110, 0)
    SetChrPos(0x104, -6570, 120, 19980, 0)
    OP_6F(0x10)
    OP_0D()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("")

    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『罗赞贝尔克工房』\x01",
            "无关人员禁止进入。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0091
    ChrTalk(
        0x102,
        "#0102F#6P啊，这里就是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0092
    ChrTalk(
        0x101,
        "#0005F#2P艾莉，你知道些什么吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0093
    ChrTalk(
        0x102,
        (
            "#0100F#6P嗯，这是一家很有名的人偶工房哦。\x02\x03",

            "听说里面有一位专门制作\x01",
            "高价古典人偶的天才人偶师。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0094
    ChrTalk(
        0x104,
        (
            "#0300F#2P咦……\x01",
            "竟然还有这种工房啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x103,
        (
            "#0203F#12P我也听说过\x01",
            "这个名字……\x02\x03",

            "#0200F这里的作品，\x01",
            "在拍卖会上好像都会被炒到天价。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0096
    ChrTalk(
        0x102,
        (
            "#0104F#5P嗯……这家工房的作品我也见过几件，\x01",
            "感觉就像艺术品一样呢。\x02\x03",

            "#0100F虽然听说过这个工房就在克洛斯贝尔，\x01",
            "但没想到会是这么偏僻的地方。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0097
    ChrTalk(
        0x101,
        (
            "#0003F#5P天才人偶师吗……\x02\x03",

            "#0001F看那牌子上面的警告，\x01",
            "感觉好像很不好接触啊，\x01",
            "不知道对方愿不愿意见我们呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 1650, 0, 20130, 270)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(100)

    #N0098
    NpcTalk(
        0x8,
        "少女的声音",
        "#1P──爷爷他出门了哦。\x02",
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

    def lambda_40E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_40E8)
    OP_68(-2610, 800, 21420, 4000)
    MoveCamera(55, 14, 0, 4000)

    def lambda_4115():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4115)

    def lambda_4122():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4122)
    Sleep(50)

    def lambda_4132():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4132)

    def lambda_413F():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_413F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0099
    ChrTalk(
        0x101,
        "#0005F#5P咦……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        "#0105F#3P（女孩子……？）\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#0200F#3P（是这个工房里的\x01",
            "  孩子吗……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-3240, 800, 21630, 2000)
    OP_97(0x8, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
    OP_6F(0x1)

    #N0102
    NpcTalk(
        0x8,
        "穿连衣裙的少女",
        (
            "#3309F#11P呵呵，你们好。\x02\x03",

            "#3300F大哥哥，你们是谁？\x02\x03",

            "来这里有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#0005F#6P那个……\x02",
    )

    CloseMessageWindow()
    OP_68(-2600, 800, 21080, 2000)
    OP_95(0x101, -4470, 0, 20870, 1600, 0x0)
    TurnDirection(0x101, 0x8, 500)
    OP_6F(0x1)

    #C0104
    ChrTalk(
        0x101,
        (
            "#0004F#6P我们不是什么可疑的人哦。\x02\x03",

            "#0000F我们是克洛斯贝尔市的\x01",
            "警察。\x02",
        )
    )

    CloseMessageWindow()

    #N0105
    NpcTalk(
        0x8,
        "穿连衣裙的少女",
        (
            "#3305F#11P啊，原来是警察啊。\x02\x03",

            "#3304F呵呵，我只在市内\x01",
            "看见过警察……\x02\x03",

            "#3300F你们也会来这种地方巡逻吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#0005F#6P啊，那个……\x01",
            "我们不是来巡逻的。\x02\x03",

            "#0000F只是想来询问一下关于\x01",
            "这附近魔兽出没的事情。\x02",
        )
    )

    CloseMessageWindow()

    #N0107
    NpcTalk(
        0x8,
        "穿连衣裙的少女",
        (
            "#3305F#11P这附近出没的魔兽……\x01",
            "你们想知道是什么魔兽，是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#0106F#6P听说是狼形的魔兽。\x02\x03",

            "#0101F你从爷爷那里\x01",
            "听说过什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0109
    NpcTalk(
        0x8,
        "穿连衣裙的少女",
        (
            "#3303F#11P没有，没听说过哦。\x02\x03",

            "#3308F不过，对了……\x01",
            "刚才我听到从远方\x01",
            "传来了一声嚎叫。\x02\x03",

            "#3300F应该就是那只魔兽了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0001F#6P嗯，没错。\x02\x03",

            "你刚才说爷爷出门了吧。\x01",
            "那工房里就没有别人了吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0111
    NpcTalk(
        0x8,
        "穿连衣裙的少女",
        (
            "#3300F#11P嗯，没有哦。\x02\x03",

            "不过爷爷说他傍晚的时候\x01",
            "会回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#0003F#6P这样啊……\x02\x03",

            "#0001F──刚才说过了，\x01",
            "这附近好像有\x01",
            "危险的魔兽出没。\x02\x03",

            "所以在爷爷回来之前，\x01",
            "你能不能乖乖待在里面呢？\x02",
        )
    )

    CloseMessageWindow()

    #N0113
    NpcTalk(
        0x8,
        "穿连衣裙的少女",
        (
            "#3305F#11P可以是可以……\x02\x03",

            "#3304F呵呵，但跟着大哥哥你们\x01",
            "好像也会很有意思啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#0005F#6P哎……\x02",
    )

    CloseMessageWindow()

    #N0115
    NpcTalk(
        0x8,
        "穿连衣裙的少女",
        (
            "#3302F#11P你们不是在和狼先生\x01",
            "玩抓鬼游戏吗？\x02\x03",

            "#3309F还是在玩躲猫猫呢？\x01",
            "呵呵，好像很有趣呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0x103,
        (
            "#0204F#3P确实……\x01",
            "这么说也没错。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        (
            "#0302F#6P哈哈，这小姑娘\x01",
            "好有意思啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0011F#6P那个……\x01",
            "因为不知道会发生什么事，\x01",
            "所以不方便带着你哦。\x02\x03",

            "#0006F所以，抱歉……\x01",
            "你能乖乖待在工房里吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0119
    NpcTalk(
        0x8,
        "穿连衣裙的少女",
        (
            "#3301F#11P真是无聊啊。\x02\x03",

            "只要『他』痊愈，\x01",
            "就不会那么无聊了……\x02\x03",

            "#3304F真没办法，\x01",
            "今天也偷偷跑去那边\x01",
            "和小雀斑玩吧。\x02\x03",

            "还是去玻璃之城\x01",
            "玩比较好呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0120
    ChrTalk(
        0x101,
        "#0005F#6P偷偷跑去那边……？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x102,
        "#0105F#3P玻璃之城……？\x02",
    )

    CloseMessageWindow()

    #N0122
    NpcTalk(
        0x8,
        "穿连衣裙的少女",
        (
            "#3309F#11P呵呵，我在自言自语啦。\x02\x03",

            "#3302F对了──\x01",
            "还没有自我介绍呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("穿连衣裙的少女")

    #A0123
    AnonymousTalk(
        0xFF,
        (
            "呵呵……\x01",
            "请叫我玲。\x02\x03",

            "本来我还想介绍一个人\x01",
            "给你们的。\x02\x03",

            "但他的右脚受伤了，\x01",
            "正在接受爷爷的治疗。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0124
    ChrTalk(
        0x101,
        (
            "#0000F#6P这、这样啊。\x01",
            "（是指人偶吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "#3304F#11P呵呵，看来狼先生\x01",
            "很聪明啊。\x02\x03",

            "我也想跟它玩一玩呢……\x01",
            "但玲已经是大人了，\x01",
            "所以不会再任性了哦。\x02\x03",

            "#3302F加油哦，支援科的哥哥姐姐们。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#0012F#6P啊……谢谢。\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x102,
        "#0102F#3P你也要小心一点哦。\x02",
    )

    CloseMessageWindow()

    def lambda_4B54():

        label("loc_4B54")

        TurnDirection(0x101, 0x8, 500)
        Yield()
        Jump("loc_4B54")

    QueueWorkItem2(0x101, 1, lambda_4B54)

    def lambda_4B66():

        label("loc_4B66")

        TurnDirection(0x102, 0x8, 500)
        Yield()
        Jump("loc_4B66")

    QueueWorkItem2(0x102, 1, lambda_4B66)

    def lambda_4B78():

        label("loc_4B78")

        TurnDirection(0x103, 0x8, 500)
        Yield()
        Jump("loc_4B78")

    QueueWorkItem2(0x103, 1, lambda_4B78)

    def lambda_4B8A():

        label("loc_4B8A")

        TurnDirection(0x104, 0x8, 500)
        Yield()
        Jump("loc_4B8A")

    QueueWorkItem2(0x104, 1, lambda_4B8A)
    OP_93(0x8, 0x0, 0x190)
    OP_95(0x8, 1950, 0, 25620, 2000, 0x0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x0)
    OP_68(-4220, 600, 23220, 4000)
    MoveCamera(45, 14, 0, 4000)

    def lambda_4BE8():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4BE8)
    Sleep(1000)

    def lambda_4C05():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4C05)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_6F(0x1)

    #C0128
    ChrTalk(
        0x103,
        (
            "#0204F#6P……好特别的\x01",
            "女孩子啊。\x02\x03",

            "#0202F是那位久负盛名的人偶师的\x01",
            "孙女吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0129
    ChrTalk(
        0x104,
        (
            "#0304F#11P应该是吧。\x02\x03",

            "#0302F话说回来，这小鬼\x01",
            "思想很成熟啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0130
    ChrTalk(
        0x102,
        (
            "#0109F#5P呵呵，\x01",
            "不是很可爱嘛。\x02\x03",

            "#0102F加上有些神秘的语调，\x01",
            "就更有魅力了……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        "#0001F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C0132
    ChrTalk(
        0x102,
        "#0105F#6P罗伊德，怎么了吗？\x02",
    )

    CloseMessageWindow()

    def lambda_4D9A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4D9A)
    Sleep(50)

    def lambda_4DAA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4DAA)
    WaitChrThread(0x104, 1)

    #C0133
    ChrTalk(
        0x104,
        (
            "#0305F#6P什么嘛，\x01",
            "怎么突然一副丢了魂的表情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x103,
        "#0200F#6P你发现什么了吗……？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#0003F#5P不……\x01",
            "其实没什么大不了的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0136
    ChrTalk(
        0x101,
        (
            "#0001F#11P只是，那孩子\x01",
            "最后是不是说了一句\x01",
            "『支援科的哥哥姐姐们』啊……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    Sleep(300)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0137
    ChrTalk(
        0x102,
        "#0101F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        (
            "#0205F#6P这样说来……\x01",
            "我们当时并没有自我介绍过吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#0301F#6P那小鬼是怎么\x01",
            "知道我们的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#0006F#11P算了，或许是看过克洛斯贝尔时代周刊，\x01",
            "知道了支援科的事吧。\x02\x03",

            "很有可能因为这样，\x01",
            "刚才才认出了我们……\x02\x03",

            "#0000F但即使如此，\x01",
            "那孩子还是给人一种不可思议的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        "#0300F#6P嗯……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        "#0203F#6P……确实是。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#0003F#11P……总之，狼形魔兽\x01",
            "好像没来这一带。\x02\x03",

            "#0000F我们先回刚才的三岔路口，\x01",
            "然后再前往矿山镇吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x102,
        "#0100F#6P嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetCameraDistance(21860, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -8080, 0, 19380, 180)
    SetScenarioFlags(0x64, 5)
    OP_29(0x40, 0x1, 0x4)
    ClearMapObjFlags(0x0, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_3A6A end

    def Function_16_5145(): pass

    label("Function_16_5145")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(2050, 3100, 45140, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 2750, 0, 23000, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 1250, 0, 23080, 0)
    SetChrPos(0x101, 2000, 0, 10250, 0)
    SetChrPos(0x102, 1000, 0, 9000, 0)
    SetChrPos(0x103, 3000, 0, 9500, 0)
    SetChrPos(0x104, 2000, 0, 8000, 0)
    OP_68(2910, 600, 25220, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_6F(0x1)
    Fade(500)
    OP_68(2000, 1200, 23000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_0D()
    OP_64(0x9)
    OP_64(0xA)
    Sleep(1000)

    #C0145
    ChrTalk(
        0x9,
        (
            "#0808F……嗯，\x01",
            "好像没人在啊……\x02\x03",

            "#0801F约修亚，\x01",
            "真的就是这里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        (
            "#0903F……虽然并没有确凿的证据，\x01",
            "但我觉得可能性很高。\x02\x03",

            "#0908F只是关于『十三工房』的事，\x01",
            "我也不太清楚。\x02\x03",

            "好像是一个将传承了古代\x01",
            "技术的十二个工房\x01",
            "整合为一体的技术网……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "#0803F这个人偶工房\x01",
            "就是其中之一吧……\x02\x03",

            "#0801F……这里确实很像\x01",
            "那孩子会来的地方。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_53E0():
        OP_93(0xA, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_53E0)
    WaitChrThread(0xA, 2)

    #C0148
    ChrTalk(
        0xA,
        (
            "#0901F怎么办，艾丝蒂尔。\x02\x03",

            "我进去调查一下人偶工房吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_542B():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_542B)
    WaitChrThread(0x9, 2)

    #C0149
    ChrTalk(
        0x9,
        (
            "#0804F……不，不用。\x02\x03",

            "现在我们并不是在和『结社』\x01",
            "正面对抗。\x02\x03",

            "#0802F如果不能在真正意义上\x01",
            "抓住那孩子，\x01",
            "我们的行动也就偏离了目标呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "#0904F……是吗。\x02\x03",

            "#0900F『竞拍会』那边也挺让人担心的，\x01",
            "现在还是把主要精力集中到那边吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x9,
        "#0800F好，就这么办。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#0005F啊……\x01",
            "艾丝蒂尔和约修亚……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    OP_68(2000, 1200, 21750, 5000)
    SetCameraDistance(19500, 5000)

    def lambda_55B2():
        OP_95(0xFE, 2000, 0, 20250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_55B2)
    Sleep(50)

    def lambda_55CF():
        OP_95(0xFE, 1000, 0, 19000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_55CF)
    Sleep(50)

    def lambda_55EC():
        OP_95(0xFE, 3000, 0, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_55EC)
    Sleep(50)

    def lambda_5609():
        OP_95(0xFE, 2000, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5609)

    def lambda_5623():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5623)

    def lambda_5630():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5630)

    #C0153
    ChrTalk(
        0x9,
        "#0805F#5P咦……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        "#0905F你们……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 2)
    WaitChrThread(0xA, 2)
    OP_6F(0x51)

    #C0155
    ChrTalk(
        0x104,
        "#0305F喂喂，这可真巧啊。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        (
            "#0202F……难怪我刚才就觉得\x01",
            "那气息似曾相识。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        (
            "#0813F#5P罗、罗伊德，你们……\x01",
            "为什么会在这里啊？\x02\x03",

            "#0801F……难道\x01",
            "你们来这个工房有事要办？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#0005F没有，只是路经山道，\x01",
            "顺便来这里逛逛而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x102,
        (
            "#0105F艾丝蒂尔你们呢？\x01",
            "来这个人偶工房有事要办吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x9,
        (
            "#0809F#5P那、那个……\x01",
            "确实有点事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        (
            "#0904F是私事，\x01",
            "但这里好像没人在。\x02\x03",

            "#0900F……话说回来，昨天辛苦你们了啊。\x01",
            "身体感觉还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#0012F还行，就是肌肉有点酸痛。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        (
            "#0300F不过你们还真是\x01",
            "有精力啊，活蹦乱跳的。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x9,
        (
            "#0802F#5P哈哈哈，可能是因为平时\x01",
            "就经常在郊外东奔西跑吧？\x02\x03",

            "#0806F……那个，抱歉。\x01",
            "我们差不多该\x01",
            "回市里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        "#0902F所以就先告辞了。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#0002F这样啊……\x01",
            "路上小心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        "#0809F嗯，你们也要小心哦！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0xA, 2, 0, 18)

    def lambda_5942():

        label("loc_5942")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5942")

    QueueWorkItem2(0x101, 2, lambda_5942)

    def lambda_5954():

        label("loc_5954")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5954")

    QueueWorkItem2(0x102, 2, lambda_5954)

    def lambda_5966():

        label("loc_5966")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5966")

    QueueWorkItem2(0x103, 2, lambda_5966)

    def lambda_5978():

        label("loc_5978")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5978")

    QueueWorkItem2(0x104, 2, lambda_5978)
    Sleep(2000)
    OP_68(1000, 1200, 18000, 3000)
    Sleep(4000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    Sleep(500)
    OP_68(2000, 1200, 19000, 3500)
    MoveCamera(51, 23, 0, 3500)
    SetCameraDistance(17500, 3500)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_6F(0x1)

    def lambda_5A4E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A4E)

    def lambda_5A5B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5A5B)

    def lambda_5A68():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5A68)

    def lambda_5A75():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5A75)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)

    #C0168
    ChrTalk(
        0x104,
        (
            "#0301F很明显有什么事\x01",
            "瞒着我们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        (
            "#0200F不过不像是\x01",
            "心中有愧的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        (
            "#0106F#3P嗯……我们也不能\x01",
            "对别人的私事刨根问底啊。\x02\x03",

            "#0100F这里好像没人在呢，\x01",
            "我们也回去吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 0)), scpexpr(EXPR_END)), "loc_5BB6")

    #C0171
    ChrTalk(
        0x101,
        (
            "#0003F嗯……好的。\x02\x03",

            "#0008F（……之前就是在这里\x01",
            "  第一次遇见了玲……）\x02\x03",

            "（难道那两个人\x01",
            "  也认识她吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C2A")

    label("loc_5BB6")


    #C0172
    ChrTalk(
        0x101,
        (
            "#0003F嗯……好的。\x02\x03",

            "#0008F（……之前就是在这里\x01",
            "  第一次遇见了那个女孩子……）\x02\x03",

            "（难道那两个人\x01",
            "  也认识她吗？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C2A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(2000, 600, 20250, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, 2000, 0, 20250, 0)
    SetChrPos(0x1, 2000, 0, 20250, 0)
    SetChrPos(0x2, 2000, 0, 20250, 0)
    SetChrPos(0x3, 2000, 0, 20250, 0)
    SetScenarioFlags(0xB7, 2)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_16_5145 end

    def Function_17_5CD8(): pass

    label("Function_17_5CD8")

    OP_95(0xFE, 5000, 0, 20750, 2000, 0x0)
    OP_95(0xFE, 1000, 0, 0, 2000, 0x0)
    Return()

    # Function_17_5CD8 end

    def Function_18_5D01(): pass

    label("Function_18_5D01")

    Sleep(50)
    OP_95(0xFE, 4750, 0, 21000, 2000, 0x0)
    OP_95(0xFE, 750, 0, 0, 2000, 0x0)
    Return()

    # Function_18_5D01 end

    def Function_19_5D2D(): pass

    label("Function_19_5D2D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   『罗赞贝尔克工房』\x01",
            "无关人员禁止进入。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_5D2D end

    def Function_20_5D8E(): pass

    label("Function_20_5D8E")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5D9F")
    Jump("loc_5DFB")

    label("loc_5D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_5DFB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_5DBA")
    Jump("loc_5DFB")

    label("loc_5DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 1)), scpexpr(EXPR_END)), "loc_5DCF")
    Call(0, 12)
    TalkEnd(0xFF)
    Return()

    label("loc_5DCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_5DE8")
    Call(0, 9)
    TalkEnd(0xFF)
    Return()

    label("loc_5DE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_5DFB")
    Call(0, 4)
    TalkEnd(0xFF)
    Return()

    label("loc_5DFB")

    SetChrName("")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门紧闭着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_20_5D8E end

    def Function_21_5E18(): pass

    label("Function_21_5E18")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门紧锁着。\x01",
            "老人没有要出来的意思。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_21_5E18 end

    SaveToFile()

Try(main)
