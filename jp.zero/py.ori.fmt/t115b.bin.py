from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "招待客",                 # 1
        "レクター",               # 2
        "犬１",                   # 3
        "犬２",                   # 4
        "犬３",                   # 5
        "SE制御",                 # 6
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
        "Function_5_65A",          # 05, 5
        "Function_6_17B6",         # 06, 6
        "Function_7_180B",         # 07, 7
        "Function_8_1860",         # 08, 8
        "Function_9_18B5",         # 09, 9
        "Function_10_190A",        # 0A, 10
        "Function_11_1963",        # 0B, 11
        "Function_12_19BC",        # 0C, 12
        "Function_13_2074",        # 0D, 13
        "Function_14_2090",        # 0E, 14
        "Function_15_20AF",        # 0F, 15
        "Function_16_20D4",        # 10, 16
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F9")

    #C0001
    ChrTalk(
        0xFE,
        (
            "まだ少し時間があるので\x01",
            "屋敷を見せてもらっているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "しかし、すごいなこの設備は……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "ハルトマン議長の\x01",
            "底知れない権威の強さを感じるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_656")

    label("loc_5F9")


    #C0004
    ChrTalk(
        0xFE,
        "しかし、すごいなこの設備は……\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "この議長邸もさぞ高名な建築家が\x01",
            "設計したのだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_656")

    TalkEnd(0xFE)
    Return()

    # Function_4_54E end

    def Function_5_65A(): pass

    label("Function_5_65A")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75E")
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
    Jump("loc_7B3")

    label("loc_75E")

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

    label("loc_7B3")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_912")

    #C0006
    ChrTalk(
        0x101,
        (
            "#5103F#5P……なあ、エリィ。\x02\x03",

            "#5108Fこういう設備を屋内に造るのに\x01",
            "どのくらいのミラが必要だと思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        (
            "#5306F#11Pわ、私だって\x01",
            "さすがに見当も付かないわよ……\x02\x03",

            "#5308Fこんな設備、お城にだって\x01",
            "そうそうは無いと思うし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADC")

    label("loc_912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_9EB")

    #C0008
    ChrTalk(
        0x101,
        (
            "#5103F#5P……なあ、ティオ。\x02\x03",

            "#5108Fこういう設備を屋内に造るのに\x01",
            "どのくらいのミラが必要だと思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        (
            "#5406F#11Pわたしに聞かれても……\x02\x03",

            "#5411Fただ、馬鹿馬鹿しいほどの\x01",
            "ミラが必要にはなりそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADC")

    label("loc_9EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_ADC")

    #C0010
    ChrTalk(
        0x101,
        (
            "#5103F#5P……なあ、ランディ。\x02\x03",

            "#5108Fこういう設備を屋内に造るのに\x01",
            "どのくらいのミラが必要だと思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        (
            "#5606F#11P判らん、判りたくもねぇ。\x02\x03",

            "#5601Fただ、この屋敷一つだけで、\x01",
            "小規模の要塞と同じくらいの\x01",
            "ミラは掛かっていそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADC")

    BeginChrThread(0x9, 3, 0, 10)

    #C0012
    ChrTalk(
        0x101,
        (
            "#5106F#5Pはあ……ハルトマン議長か。\x02\x03",

            "#5113F昔からの名門とはいえ、\x01",
            "そこまでの資産家なのか……？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0013
    ChrTalk(
        0x9,
        "#3507F#4Sわっ！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_BAB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BAB)

    def lambda_BB8():
        OP_93(0xFE, 0x167, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_BB8)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    #C0014
    ChrTalk(
        0x101,
        "#5111F#6Pなっ……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_C39")

    #C0015
    ChrTalk(
        0x102,
        "#5301F#12Pあ、あなたは……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C92")

    label("loc_C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_C6B")

    #C0016
    ChrTalk(
        0x103,
        "#5401F#12P……あなたは……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C92")

    label("loc_C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_C92")

    #C0017
    ChrTalk(
        0x104,
        "#5601F#12Pてめえ……！？\x02",
    )

    CloseMessageWindow()

    label("loc_C92")

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
            "よう、お二人さん。\x02\x03",

            "ドレスアップしたようだが\x01",
            "なかなか似合ってるじゃないか。\x02\x03",

            "ふむふむ、パーティに正装して\x01",
            "来るだけの分別はあるみたいだな。\x02",
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
        "#5106F#6Pいや、その格好で言われても。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_E2F")

    #C0020
    ChrTalk(
        0x102,
        (
            "#5311F#12Pさすがにラフすぎる\x01",
            "格好だと思いますけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA9")

    label("loc_E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_E69")

    #C0021
    ChrTalk(
        0x103,
        "#5411F#12P……説得力ゼロではないかと。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA9")

    label("loc_E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_EA9")

    #C0022
    ChrTalk(
        0x104,
        (
            "#5605F#12Pいくらなんでも\x01",
            "さすがにラフすぎねぇか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA9")


    #C0023
    ChrTalk(
        0x9,
        (
            "#3504F#5Pハルトマンのオッサンも\x01",
            "自分の家のように\x01",
            "寛#2Rくつろ#げとか言ってたからなァ。\x02\x03",

            "#3500Fアンタらもぼちぼち\x01",
            "楽しんでるようで何よりだ。\x02\x03",

            "#3507Fま、オレに\x01",
            "較べたらまだまだだけどな！\x02",
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
        "#5111F#6Pへ……\x02",
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
            "#3500F#5Pんー、どれどれ……\x02\x03",

            "#3509Fお、あの辺りにするか。\x02",
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
            "#5111F#6Pちょ、いきなり\x01",
            "何をやってるんですか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1223")

    #C0027
    ChrTalk(
        0x102,
        (
            "#5306F#6P#Nし、信じられない……\x02\x03",

            "#5301Fというか、こんな場所で\x01",
            "魚が釣れるはずが──\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F7")

    label("loc_1223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1289")

    #C0028
    ChrTalk(
        0x103,
        (
            "#5406F#6P#Nフリーダムすぎです……\x02\x03",

            "#5411Fそもそもこんな場所で\x01",
            "魚が釣れるはずが──\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F7")

    label("loc_1289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_12F7")

    #C0029
    ChrTalk(
        0x104,
        (
            "#5606F#6P#Nおいおい……\x01",
            "フリーダムすぎんだろ。\x02\x03",

            "#5601Fつうか、こんな場所で\x01",
            "魚が釣れるわけが──\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F7")

    Sleep(500)
    OP_A1(0x9, 0x3E8, 0x4, 0x3, 0x4, 0x5, 0x6)

    #C0030
    ChrTalk(
        0x9,
        (
            "#40A#3505F#5P#20Wおっ…#1000W…\x01",
            "#20Wおっ#500W、#20Wおおっ#500W、#20Wおっ#500W、\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0031
    ChrTalk(
        0x9,
        "#3509F#4S#5P#10A来た来たァ～！\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_144D")

    #C0032
    ChrTalk(
        0x102,
        "#5305F#6P#N……釣れちゃった。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14A6")

    label("loc_144D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_147C")

    #C0033
    ChrTalk(
        0x103,
        "#5405F#6P#N……釣れました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14A6")

    label("loc_147C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_14A6")

    #C0034
    ChrTalk(
        0x104,
        "#5605F#6P#N……釣れんのか。\x02",
    )

    CloseMessageWindow()

    label("loc_14A6")

    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x9,
        (
            "#3500F#5Pよーし、今日はなかなか\x01",
            "良いものが釣れたなァ。\x02\x03",

            "#3504Fうむ、これはクロへの\x01",
            "土産に持って行ってやろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#5106F#6P鑑賞用の金魚の\x01",
            "一種みたいだけど……\x02\x03",

            "#5113F──ていうか\x01",
            "さすがにマズイんじゃ！？\x02",
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
            "#3509F#11Pふはは、それではさらばだ！\x02\x03",

            "#3502Fま、アンタらの方も\x01",
            "良いモン釣れるといいなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#5105F#6Pえ──\x02",
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
        "#5112F#5P#40Wえーっと……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_16F3")

    #C0040
    ChrTalk(
        0x102,
        (
            "#5306F#6Pまあ、その……\x01",
            "見なかった事にしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177E")

    label("loc_16F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_173B")

    #C0041
    ChrTalk(
        0x103,
        (
            "#5411F#6P……深く考えるだけ\x01",
            "時間の無駄ではないかと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177E")

    label("loc_173B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_177E")

    #C0042
    ChrTalk(
        0x104,
        (
            "#5606F#6Pなんつーか……\x01",
            "気にしたら負けな気がするぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177E")

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

    # Function_5_65A end

    def Function_6_17B6(): pass

    label("Function_6_17B6")

    SetChrPos(0x101, -4000, 0, 10, 90)

    def lambda_17CC():
        OP_95(0xFE, -1870, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17CC)
    WaitChrThread(0x101, 1)

    def lambda_17EA():
        OP_95(0xFE, -600, 0, -4350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17EA)
    WaitChrThread(0x101, 1)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_6_17B6 end

    def Function_7_180B(): pass

    label("Function_7_180B")

    SetChrPos(0xEF, -5540, 130, 10, 90)

    def lambda_1821():
        OP_95(0xFE, -2480, 0, -150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1821)
    WaitChrThread(0xEF, 1)

    def lambda_183F():
        OP_95(0xFE, 600, 0, -4350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_183F)
    WaitChrThread(0xEF, 1)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_7_180B end

    def Function_8_1860(): pass

    label("Function_8_1860")

    SetChrPos(0x101, 4000, 0, 10, 90)

    def lambda_1876():
        OP_95(0xFE, 1870, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1876)
    WaitChrThread(0x101, 1)

    def lambda_1894():
        OP_95(0xFE, -600, 0, -4350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1894)
    WaitChrThread(0x101, 1)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_8_1860 end

    def Function_9_18B5(): pass

    label("Function_9_18B5")

    SetChrPos(0xEF, 5540, 130, 10, 90)

    def lambda_18CB():
        OP_95(0xFE, 2480, 0, -150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_18CB)
    WaitChrThread(0xEF, 1)

    def lambda_18E9():
        OP_95(0xFE, 600, 0, -4350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_18E9)
    WaitChrThread(0xEF, 1)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_9_18B5 end

    def Function_10_190A(): pass

    label("Function_10_190A")

    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xFE, -10310, 0, -20, 180)

    def lambda_192B():
        OP_95(0xFE, 0, 0, -250, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_192B)
    WaitChrThread(0xFE, 1)

    def lambda_1949():
        OP_95(0xFE, 0, 0, -3100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1949)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_190A end

    def Function_11_1963(): pass

    label("Function_11_1963")

    OP_93(0xFE, 0x5A, 0x320)

    def lambda_196F():
        OP_95(0xFE, 15120, 0, 0, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_196F)
    WaitChrThread(0xFE, 1)

    def lambda_198D():
        OP_95(0xFE, 16660, 0, 0, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_198D)

    def lambda_19A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_19A7)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_11_1963 end

    def Function_12_19BC(): pass

    label("Function_12_19BC")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A09")
    LoadChrToIndex("monster/ch67150.itc", 0x23)
    LoadChrToIndex("monster/ch67151.itc", 0x24)
    LoadChrToIndex("monster/ch67152.itc", 0x25)
    Jump("loc_1A1B")

    label("loc_1A09")

    LoadChrToIndex("monster/ch75650.itc", 0x23)
    LoadChrToIndex("monster/ch75651.itc", 0x24)
    LoadChrToIndex("monster/ch75652.itc", 0x25)

    label("loc_1A1B")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B10")
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B10")

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

    def lambda_1BEA():
        OP_95(0xFE, 2620, 0, 210, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BEA)

    def lambda_1C04():
        OP_95(0xFE, 3820, 0, 1420, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1C04)

    def lambda_1C1E():
        OP_95(0xFE, 4650, 0, -870, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C1E)
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

    def lambda_1CF5():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1CF5)

    def lambda_1D0A():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1D0A)

    def lambda_1D1F():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1D1F)
    OP_6F(0x10)
    OP_0D()

    #C0043
    ChrTalk(
        0x133,
        (
            "#5805F#1Pわぁ……！\x01",
            "なんかいっぱい来たよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#0010F#1Pくっ……\x01",
            "屋内に犬を放つなんて！\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1EB1")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    Jump("loc_1ED8")

    label("loc_1EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1EC7")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_1ED8")

    label("loc_1EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1ED8")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_1ED8")

    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    OP_6F(0x1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1F19")

    #C0045
    ChrTalk(
        0x102,
        "#0107F#11P何とか撃退しないと……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F86")

    label("loc_1F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1F53")

    #C0046
    ChrTalk(
        0x103,
        "#0207F#11P……とにかく撃退しましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F86")

    label("loc_1F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1F86")

    #C0047
    ChrTalk(
        0x104,
        "#0307F#11Pとにかく撃退するしかねぇ！\x02",
    )

    CloseMessageWindow()

    label("loc_1F86")


    #C0048
    ChrTalk(
        0x105,
        "#0407F#12P……来るよ！\x02",
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

    # Function_12_19BC end

    def Function_13_2074(): pass

    label("Function_13_2074")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_208F")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_13_2074")

    label("loc_208F")

    Return()

    # Function_13_2074 end

    def Function_14_2090(): pass

    label("Function_14_2090")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20AE")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_14_2090")

    label("loc_20AE")

    Return()

    # Function_14_2090 end

    def Function_15_20AF(): pass

    label("Function_15_20AF")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    SetChrSubChip(0xFE, 0x3)
    OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1770, 0x0)
    Return()

    # Function_15_20AF end

    def Function_16_20D4(): pass

    label("Function_16_20D4")

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

    # Function_16_20D4 end

    SaveToFile()

Try(main)
