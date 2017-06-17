from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t050b.bin",                # FileName
        "t050B",                    # MapName
        "t050B",                    # Location
        0x003C,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 60, 0, 3, 0, 4],
    )

    BuildStringList((
        "t050b",                  # 0
        "霍夫曼矿山长",           # 1
        "矿工玛尔罗",             # 2
        "矿工冈兹",               # 3
        "魔兽",                   # 4
        "魔兽",                   # 5
        "魔兽",                   # 6
        "SE控制",                 # 7
        "BT050b",                 # 8
        "玛因兹山道",             # 9
        "玛因兹矿山",             # 10
    ))

    ATBonus("ATBonus_288", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_2A8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_32C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_330", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_334", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_338", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_33C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_340", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_348", 0x0002, 16, 6, 0, 0, 0, 0, 0, "BT050b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75600.dat", "ms75600.dat", "ms75600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2A8", "MonsterBattlePostion_328", "ed7401", "ed7403", "ATBonus_288"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch26300.itc",                   # 01
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

    DeclNpc(-24969,  11439,   56069,   270,  401,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-4600,   -2000,   28700,   1500,    -4600,   -500,    28700,   0x007C, 0,  6,  0x0000)

    PlaceName(11.0, 0.0, -23.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-32.0, 0.0, 62.0, 0x0000, 0x0000, "玛因兹矿山")
    PlaceName(-19.75, 0.0, 45.75, 0x0000, 0x0053, "")
    PlaceName(-3.0, 0.0, 49.0, 0x0000, 0x0052, "")
    PlaceName(-4.5, 0.0, 28.600000381469727, 0x0000, 0x0055, "")

    ScpFunction((
        "Function_0_3E8",          # 00, 0
        "Function_1_4A0",          # 01, 1
        "Function_2_4F1",          # 02, 2
        "Function_3_50C",          # 03, 3
        "Function_4_53F",          # 04, 4
        "Function_5_584",          # 05, 5
        "Function_6_DFA",          # 06, 6
        "Function_7_E22",          # 07, 7
        "Function_8_1B7A",         # 08, 8
        "Function_9_1BB6",         # 09, 9
        "Function_10_1BD4",        # 0A, 10
        "Function_11_1C13",        # 0B, 11
        "Function_12_1C44",        # 0C, 12
        "Function_13_1C60",        # 0D, 13
        "Function_14_1C7F",        # 0E, 14
        "Function_15_1CC5",        # 0F, 15
        "Function_16_1D17",        # 10, 16
        "Function_17_1D69",        # 11, 17
        "Function_18_1DBB",        # 12, 18
        "Function_19_1E21",        # 13, 19
        "Function_20_1E64",        # 14, 20
        "Function_21_2490",        # 15, 21
        "Function_22_24E8",        # 16, 22
    ))


    def Function_0_3E8(): pass

    label("Function_0_3E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_428"),
        (1, "loc_434"),
        (2, "loc_440"),
        (3, "loc_44C"),
        (4, "loc_458"),
        (5, "loc_464"),
        (6, "loc_470"),
        (SWITCH_DEFAULT, "loc_47C"),
    )


    label("loc_428")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_434")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_440")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_44C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_458")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_464")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_470")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_47C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_488")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_49F")

    Return()

    # Function_0_3E8 end

    def Function_1_4A0(): pass

    label("Function_1_4A0")

    OP_95(0xFE, -23810, 11440, 54160, 3000, 0x0)
    OP_95(0xFE, -20240, 11440, 54160, 3000, 0x0)
    OP_95(0xFE, -18970, 11440, 55670, 3000, 0x0)
    OP_95(0xFE, -14930, 9560, 55670, 3000, 0x0)
    Return()

    # Function_1_4A0 end

    def Function_2_4F1(): pass

    label("Function_2_4F1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50B")
    TurnDirection(0xFE, 0x8, 100)
    Sleep(10)
    Jump("Function_2_4F1")

    label("loc_50B")

    Return()

    # Function_2_4F1 end

    def Function_3_50C(): pass

    label("Function_3_50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_520")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 7)
    Jump("loc_52F")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_52F")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 20)

    label("loc_52F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53E")
    ClearChrFlags(0x8, 0x80)

    label("loc_53E")

    Return()

    # Function_3_50C end

    def Function_4_53F(): pass

    label("Function_4_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54F")
    ClearMapObjFlags(0x6, 0x10)

    label("loc_54F")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_567")
    OP_1B(0x0, 0x0, 0x16)

    label("loc_567")

    SoundDistance(0x84, 0xFFFFF678, 0x1B4E, 0x15766, 0x2710, 0xC350, 0x64, 0x0)
    Return()

    # Function_4_53F end

    def Function_5_584(): pass

    label("Function_5_584")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-22000, 13400, 56100, 0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, -22770, 11440, 55720, 270)
    SetChrPos(0x102, -22770, 11440, 57320, 270)
    SetChrPos(0x103, -21040, 11440, 55740, 270)
    SetChrPos(0x104, -21040, 11440, 57320, 270)
    FadeToBright(500, 0)
    OP_0D()
    Sound(810, 0, 100, 0)

    #C0001
    ChrTalk(
        0x8,
        (
            "……哦，\x01",
            "总之，全员似乎已经都回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "冈兹和玛尔罗\x01",
            "好像去酒馆了……\x01",
            "嗯，反正只要是待在建筑物内就没问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#0005F请问……\x01",
            "您在这里做什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0004
    ChrTalk(
        0x8,
        "啊，在关矿山的门。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "有时候会有魔兽跑出来，\x01",
            "所以必须要确认一下，\x01",
            "看看里面还有没有人。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#0005F魔兽吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_93(0x102, 0xB4, 0x12C)

    #C0007
    ChrTalk(
        0x102,
        (
            "#0105F……罗伊德，你怎么了？\x02\x03",

            "好像想到了什么啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_77C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77C)

    def lambda_789():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_789)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0008
    ChrTalk(
        0x101,
        (
            "#0001F啊，是的……\x02\x03",

            "#0000F我在想，作战开始之前，\x01",
            "大概能在这里稍微\x01",
            "锻炼一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0009
    ChrTalk(
        0x104,
        (
            "#0300F啊，这个主意\x01",
            "好像不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#0203F确实，也没时间\x01",
            "离开城镇去郊外了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "……你们想做什么？\x02",
    )

    CloseMessageWindow()

    def lambda_8A5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A5)

    def lambda_8B2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B2)

    def lambda_8BF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8BF)

    def lambda_8CC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8CC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0012
    ChrTalk(
        0x101,
        "#0000F啊，是这样的……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德说明了事情缘由，\x01",
            "询问是否可以进入矿山锻炼。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x8,
        "嗯，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "但是，里面是禁止进入的。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "如果外人进去受伤的话，\x01",
            "身为矿山长，实在是无法交代。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#0006F……是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#0103F既然您这么说，那就没办法了……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "……虽然本来是这样啦。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0005F……哎？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "看起来，你们的身体素质\x01",
            "似乎也不错，应该不输给\x01",
            "我们这些矿工……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "如果答应我不在里面胡闹，\x01",
            "我就破例让你们进去。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#0000F真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        "#0309F哈哈，很大度嘛。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "哪里，那些该死的狼不是弄伤了\x01",
            "马库斯吗，我也希望它们能被狠狠教训一顿。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "既然你们来帮忙，\x01",
            "我当然很乐意协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "好，稍等一下。\x02",
    )

    CloseMessageWindow()

    def lambda_B55():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B55)
    WaitChrThread(0x8, 1)
    Sound(809, 0, 100, 0)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "霍夫曼用钥匙打开矿山大门。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_B95():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B95)
    WaitChrThread(0x8, 1)

    #C0029
    ChrTalk(
        0x8,
        (
            "那么，请各位务必要小心，\x01",
            "注意不要受伤啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "对了，左边深处的门里面是废坑。\x01",
            "不要进去哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#0000F嗯，明白了。\x01",
            "谢谢您！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "别客气，\x01",
            "那么，那些狼就交给你们了。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 1)

    def lambda_C56():

        label("loc_C56")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_C56")

    QueueWorkItem2(0x101, 1, lambda_C56)

    def lambda_C68():

        label("loc_C68")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_C68")

    QueueWorkItem2(0x102, 1, lambda_C68)

    def lambda_C7A():

        label("loc_C7A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_C7A")

    QueueWorkItem2(0x103, 1, lambda_C7A)

    def lambda_C8C():

        label("loc_C8C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_C8C")

    QueueWorkItem2(0x104, 1, lambda_C8C)
    Sleep(6000)

    def lambda_CA1():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CA1)

    def lambda_CAE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CAE)

    def lambda_CBB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CBB)

    def lambda_CC8():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CC8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0033
    ChrTalk(
        0x103,
        (
            "#0200F不管怎么说，\x01",
            "这样一来，就可以进入矿山了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#0000F嗯，在作战开始前，\x01",
            "好好锻炼一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_68(-21980, 13440, 56060, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x101, -21980, 11440, 56060, 270)
    SetChrPos(0x102, -21980, 11440, 56060, 270)
    SetChrPos(0x103, -21980, 11440, 56060, 270)
    SetChrPos(0x104, -21980, 11440, 56060, 270)
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()
    SetMapObjFlags(0x6, 0x10)
    SetScenarioFlags(0x68, 2)
    EventEnd(0x5)
    Return()

    # Function_5_584 end

    def Function_6_DFA(): pass

    label("Function_6_DFA")

    TalkBegin(0xFF)
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_6_DFA end

    def Function_7_E22(): pass

    label("Function_7_E22")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch26200.itc", 0x1E)
    LoadChrToIndex("chr/ch30700.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00051.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00151.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00251.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch00351.itc", 0x27)
    LoadChrToIndex("monster/ch75650.itc", 0x28)
    LoadChrToIndex("monster/ch75651.itc", 0x29)
    LoadChrToIndex("monster/ch75653.itc", 0x2A)
    LoadChrToIndex("apl/ch50121.itc", 0x2B)
    LoadEffect(0x0, "event\\ev100_00.eff")
    SoundLoad(843)
    SetChrPos(0x101, 8700, 0, 56240, 90)
    SetChrPos(0x102, 9160, 0, 41110, 90)
    SetChrPos(0x103, 10870, 0, 41130, 90)
    SetChrPos(0x104, -4490, 2920, 44010, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0x9, 0x4)
    SetChrPos(0xA, -1950, 440, 54350, 90)
    SetChrPos(0x9, -1950, 440, 54350, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(843, 2, 100, 0)
    OP_68(-1910, 3550, 66890, 0)
    MoveCamera(326, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(110410, 0)
    OP_68(-1910, -550, 66890, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(0, 750, 54400, 0)
    MoveCamera(305, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29280, 0)
    SetCameraDistance(27780, 3000)
    OP_6F(0x10)
    Sleep(500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(105, 0, 100, 0)
    OP_79(0x0)
    Sleep(700)

    def lambda_10A6():
        OP_97(0xFE, 0x1964, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10A6)

    def lambda_10C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10C0)
    Sleep(800)

    def lambda_10D4():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10D4)

    def lambda_10EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10EE)
    Sleep(1000)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(106, 0, 100, 0)
    OP_79(0x0)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    TurnDirection(0xA, 0x9, 500)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Sleep(500)
    OP_93(0xA, 0xB4, 0x1F4)

    def lambda_1138():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1138)
    Sleep(300)

    def lambda_1155():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1155)
    Sleep(2000)
    BeginChrThread(0xE, 1, 0, 19)
    Fade(1000)
    OP_68(3730, 1050, 46330, 0)
    MoveCamera(305, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20800, 0)
    SetCameraDistance(19000, 2000)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x9, 1)
    EndChrThread(0xE, 0x1)
    TurnDirection(0xA, 0x9, 500)
    Sleep(300)

    #C0036
    ChrTalk(
        0xA,
        (
            "#11P唔咕……\x01",
            "是不是喝得太多了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(300)

    #C0037
    ChrTalk(
        0x9,
        "#5P话说回来，已经很晚了啊。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "#5P镇长明明才说过让我们\x01",
            "早点回去的……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        "#11P哦，是因为魔兽的事吧？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xA,
        (
            "#11P嘁，我可是都忍着没去『巴鲁卡』，\x01",
            "每天努力地挖矿呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xA,
        (
            "#11P至少也该让我\x01",
            "尽情喝点酒吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            "#5P话说你平时每周末都会进城，\x01",
            "然后一直泡在『巴鲁卡』里……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "#5P而且次次都输个精光，\x01",
            "真是店里的摇钱树啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "#11P住、住嘴，\x01",
            "我只是把钱暂时存在店里而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xA,
        (
            "#11P走着瞧吧……\x01",
            "我下次玩轮盘时一定会转出个大的，\x01",
            "把至今为止输掉的都赢回来！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(836, 0, 100, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0046
    ChrTalk(
        0xA,
        "#11P嗯……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        "#5P咦，刚才那是……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_143F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_143F)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0xA, 1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetCameraDistance(20500, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xB, 13370, 0, 47650, 270)
    SetChrPos(0xC, 3460, 0, 55100, 180)
    SetChrPos(0xD, 3200, 0, 39330, 0)
    BeginChrThread(0xB, 3, 0, 15)
    BeginChrThread(0xC, 3, 0, 16)
    BeginChrThread(0xD, 3, 0, 17)
    Sleep(100)
    Sound(832, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xA, 0xB, 500)

    #C0048
    ChrTalk(
        0xA,
        "#5P呀……怎么回事！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x9, 0xD, 500)

    #C0049
    ChrTalk(
        0x9,
        "#11P难、难道……是那些狼！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetCameraDistance(17580, 1000)
    BeginChrThread(0xB, 3, 0, 14)
    BeginChrThread(0xC, 3, 0, 14)
    BeginChrThread(0xD, 3, 0, 14)
    Sleep(200)
    BeginChrThread(0xA, 3, 0, 8)
    BeginChrThread(0x9, 3, 0, 9)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0x9, 3)
    OP_6F(0x10)
    Sleep(500)

    #C0050
    ChrTalk(
        0xA,
        "#5P别、别、别过来……！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        "#11P救、救救我……爱德丝女神……！\x02",
    )

    CloseMessageWindow()

    #N0052
    NpcTalk(
        0x104,
        "青年的声音",
        (
            "#4P──你们两个，\x01",
            "最好闭上眼睛。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)
    OP_64(0xA)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x104, 500)
    TurnDirection(0x9, 0x104, 500)
    Sound(1298, 255, 100, 0)    #voice#Randy
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 4310, 0, 47660, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(814, 0, 100, 0)
    Sleep(1800)
    Sound(555, 0, 100, 0)
    Sleep(700)
    Sound(555, 0, 100, 0)
    Sleep(300)
    BeginChrThread(0x104, 3, 0, 10)
    Sound(556, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(250)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 11)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 11)
    Sleep(100)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0xD, 3, 0, 11)
    Sleep(1000)

    #C0053
    ChrTalk(
        0xB,
        "#11P汪！？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xC,
        "#11P嗷嗷……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)

    #C0055
    ChrTalk(
        0xA,
        "#11P哇……怎么回事！？\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        "#5P刚、刚才那是……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    SetCameraDistance(21000, 1500)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_1848():
        OP_95(0xFE, 5960, 0, 50660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1848)

    def lambda_1862():
        OP_95(0xFE, 5990, 0, 43230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1862)

    def lambda_187C():
        OP_95(0xFE, 7630, 0, 43280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_187C)

    def lambda_1896():
        OP_95(0xFE, -790, 0, 44080, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1896)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)
    OP_0D()

    #C0057
    ChrTalk(
        0x104,
        (
            "#0304F#1P是闪光弹。\x02\x03",

            "#0302F即使是对付被训练过的狗，\x01",
            "也稍微管点用吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 500)
    Sleep(300)

    #C0058
    ChrTalk(
        0xA,
        "#11P你、你们……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    #C0059
    ChrTalk(
        0x9,
        "#5P是……是白天的？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0007F#2P有什么话之后再说！\x01",
            "请去旅舍里避难！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        "#5P啊，好的……！\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        "#11P唔，到底是怎么回事！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x9, 3, 0, 18)
    Sleep(500)
    BeginChrThread(0xA, 3, 0, 18)
    Sleep(2100)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(105, 0, 100, 0)
    OP_79(0x0)
    WaitChrThread(0x9, 3)
    OP_64(0x9)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    WaitChrThread(0xA, 3)
    OP_64(0xA)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Sleep(200)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(106, 0, 100, 0)
    OP_79(0x0)
    Sleep(500)
    Fade(250)
    EndChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 0, 0, 13)
    OP_0D()
    TurnDirection(0xB, 0x103, 0)

    #C0063
    ChrTalk(
        0xB,
        "#11P呜噜噜噜……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    EndChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 0, 0, 13)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 13)
    OP_0D()
    TurnDirection(0xC, 0x101, 500)
    TurnDirection(0xD, 0x104, 500)

    #C0064
    ChrTalk(
        0xC,
        "#5P嗷嗷！！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#0301F#1P没想到……\x01",
            "好像挺棘手的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#0007F好……\x01",
            "一鼓作气击退它们！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    StopBGM(0x7D0)
    OP_24(0x34B)
    Battle("BattleInfo_348", 0x30200011, 0x0, 0x0, 0xD, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    Call(0, 20)
    Return()

    # Function_7_E22 end

    def Function_8_1B7A(): pass

    label("Function_8_1B7A")


    def lambda_1B7F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1B7F)
    WaitChrThread(0xA, 1)

    def lambda_1B9C():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1B9C)
    WaitChrThread(0xA, 2)
    Return()

    # Function_8_1B7A end

    def Function_9_1BB6(): pass

    label("Function_9_1BB6")


    def lambda_1BBB():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BBB)
    WaitChrThread(0x9, 1)
    Return()

    # Function_9_1BB6 end

    def Function_10_1BD4(): pass

    label("Function_10_1BD4")

    OP_82(0x0, 0x12C, 0x1770, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    SetCameraDistance(19580, 150)
    OP_6F(0x79)
    CancelBlur(1000)
    SetCameraDistance(17580, 1000)
    OP_6F(0x79)
    Return()

    # Function_10_1BD4 end

    def Function_11_1C13(): pass

    label("Function_11_1C13")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1C2F():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C2F)
    Return()

    # Function_11_1C13 end

    def Function_12_1C44(): pass

    label("Function_12_1C44")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C5F")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_12_1C44")

    label("loc_1C5F")

    Return()

    # Function_12_1C44 end

    def Function_13_1C60(): pass

    label("Function_13_1C60")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C7E")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_13_1C60")

    label("loc_1C7E")

    Return()

    # Function_13_1C60 end

    def Function_14_1C7F(): pass

    label("Function_14_1C7F")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 12)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x7D0, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 13)
    Return()

    # Function_14_1C7F end

    def Function_15_1CC5(): pass

    label("Function_15_1CC5")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 12)
    OP_95(0xFE, 8670, 0, 47200, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 13)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_1CC5 end

    def Function_16_1D17(): pass

    label("Function_16_1D17")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 12)
    OP_95(0xFE, 3260, 0, 50500, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 13)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_16_1D17 end

    def Function_17_1D69(): pass

    label("Function_17_1D69")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 12)
    OP_95(0xFE, 3200, 0, 42450, 4000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 13)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_1D69 end

    def Function_18_1DBB(): pass

    label("Function_18_1DBB")

    OP_93(0xFE, 0x13B, 0x1F4)
    OP_95(0xFE, 1190, 0, 49990, 4000, 0x0)
    OP_95(0xFE, 860, 0, 54460, 4000, 0x0)

    def lambda_1DEF():
        OP_95(0xFE, -1950, 440, 54350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DEF)
    Sleep(500)

    def lambda_1E0C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E0C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_1DBB end

    def Function_19_1E21(): pass

    label("Function_19_1E21")

    OP_25(0x34B, 0x5A)
    Sleep(100)
    OP_25(0x34B, 0x50)
    Sleep(100)
    OP_25(0x34B, 0x46)
    Sleep(100)
    OP_25(0x34B, 0x3C)
    Sleep(100)
    OP_25(0x34B, 0x32)
    Sleep(100)
    OP_25(0x34B, 0x28)
    Sleep(100)
    OP_25(0x34B, 0x1E)
    Sleep(100)
    OP_25(0x34B, 0x14)
    Sleep(100)
    OP_25(0x34B, 0xA)
    Sleep(100)
    OP_24(0x34B)
    Return()

    # Function_19_1E21 end

    def Function_20_1E64(): pass

    label("Function_20_1E64")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00051.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00151.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00251.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch00351.itc", 0x27)
    LoadChrToIndex("monster/ch75650.itc", 0x28)
    LoadChrToIndex("monster/ch75651.itc", 0x29)
    LoadChrToIndex("apl/ch50121.itc", 0x2A)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 4200, 0, 48980, 180)
    SetChrPos(0x102, 6050, 0, 49360, 180)
    SetChrPos(0x103, 5020, 0, 50820, 180)
    SetChrPos(0x104, 3410, 0, 50610, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xB, 0x2A)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2A)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 2580, 0, 45100, 0)
    SetChrPos(0xC, 4270, 0, 42920, 0)
    SetChrPos(0xD, 5490, 0, 44910, 0)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_68(1350, 150, 47770, 0)
    MoveCamera(301, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23200, 0)
    OP_68(1350, 150, 49270, 2000)
    OP_0D()
    OP_6F(0x1)

    #C0067
    ChrTalk(
        0x101,
        (
            "#0003F#2P呼……\x01",
            "真是费了一番力气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#0101F#4P仔细一看……\x01",
            "与其说是狼，好像更像狗呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        (
            "#0201F#2P果然是受过训练的\x01",
            "军犬吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1350, 150, 47770, 3000)
    OP_6F(0x1)

    def lambda_20CE():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_20CE)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    WaitChrThread(0xC, 2)
    Sound(836, 0, 100, 0)

    #N0070
    NpcTalk(
        0xC,
        "军犬",
        "……呜噜噜噜………\x02",
    )

    CloseMessageWindow()

    def lambda_212A():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_212A)

    def lambda_2143():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2143)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    WaitChrThread(0xB, 2)
    WaitChrThread(0xD, 2)

    #N0071
    NpcTalk(
        0xD,
        "军犬",
        "#5P汪……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 1, 0, 21)
    SetChrChipByIndex(0xC, 0x29)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xC, 0xE1, 0x1F4)
    OP_63(0xC, 0xFFFFFC7C, 1900, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0xC, 0, 0, 12)

    def lambda_21E1():
        OP_95(0xFE, 140, 0, 38070, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_21E1)
    Sleep(750)
    SetChrChipByIndex(0xD, 0x29)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xD, 0xE1, 0x1F4)
    OP_63(0xD, 0xFFFFFC7C, 1900, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0xD, 0, 0, 12)

    def lambda_2230():
        OP_95(0xFE, 140, 0, 38070, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2230)
    Sleep(750)
    SetChrChipByIndex(0xB, 0x29)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xB, 0xE1, 0x1F4)
    OP_63(0xB, 0xFFFFFC7C, 1900, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0xB, 0, 0, 12)

    def lambda_227F():
        OP_95(0xFE, 140, 0, 38070, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_227F)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0072
    ChrTalk(
        0x103,
        "#0205F啊……！\x02",
    )

    CloseMessageWindow()
    OP_64(0xB)
    WaitChrThread(0xB, 1)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_64(0xC)
    WaitChrThread(0xC, 1)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_64(0xD)
    WaitChrThread(0xD, 1)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    #C0073
    ChrTalk(
        0x104,
        (
            "#0301F#2P嘁……\x01",
            "还有力气吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#0007F没问题！\x01",
            "我们追上去！\x02\x03",

            "它们大概会逃窜到\x01",
            "黑手党所在的地方！\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        "#0107F#4P嗯……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)

    def lambda_23EC():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23EC)

    def lambda_2401():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2401)

    def lambda_2416():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2416)

    def lambda_242B():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_242B)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    EndChrThread(0xE, 0x1)
    SetScenarioFlags(0x5C, 0)
    NewScene("r206B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_1E64 end

    def Function_21_2490(): pass

    label("Function_21_2490")

    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(500)
    Sound(832, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Return()

    # Function_21_2490 end

    def Function_22_24E8(): pass

    label("Function_22_24E8")

    EventBegin(0x1)

    #C0076
    ChrTalk(
        0x101,
        (
            "#0001F太阳已经下山了啊……\x02\x03",

            "#0003F他们应该会在深夜袭击矿山镇，\x01",
            "我们还是不要出去了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 650, -2000, -4920, 0)
    EventEnd(0x4)
    Return()

    # Function_22_24E8 end

    SaveToFile()

Try(main)
