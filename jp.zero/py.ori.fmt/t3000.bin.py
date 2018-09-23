from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "レン",                   # 1
        "エステル",               # 2
        "ヨシュア",               # 3
        "ヨルグ老人",             # 4
        "魔獣",                   # 5
        "魔獣",                   # 6
        "魔獣",                   # 7
        "魔獣",                   # 8
        "魔獣",                   # 9
        "魔獣",                   # 10
        "SE制御",                 # 11
        "bt3000",                 # 12
        "マインツ山道",           # 13
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

    PlaceName(-1.6100000143051147, 0.0, -23.0, 0x0000, 0x0000, "マインツ山道")

    ScpFunction((
        "Function_0_4CC",          # 00, 0
        "Function_1_4E8",          # 01, 1
        "Function_2_505",          # 02, 2
        "Function_3_537",          # 03, 3
        "Function_4_59E",          # 04, 4
        "Function_5_10E4",         # 05, 5
        "Function_6_1109",         # 06, 6
        "Function_7_112E",         # 07, 7
        "Function_8_1153",         # 08, 8
        "Function_9_1178",         # 09, 9
        "Function_10_181F",        # 0A, 10
        "Function_11_198E",        # 0B, 11
        "Function_12_19B0",        # 0C, 12
        "Function_13_1E18",        # 0D, 13
        "Function_14_393D",        # 0E, 14
        "Function_15_3DEC",        # 0F, 15
        "Function_16_57E8",        # 10, 16
        "Function_17_64FD",        # 11, 17
        "Function_18_6526",        # 12, 18
        "Function_19_6552",        # 13, 19
        "Function_20_65C3",        # 14, 20
        "Function_21_6659",        # 15, 21
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
            "#11P#0001Fうーん、相変わらず\x01",
            "人の気配がないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        (
            "#6P#0104Fでも、イメルダさんが\x01",
            "通信で話していたみたいだし……\x02\x03",

            "#0100Fレンちゃんも\x01",
            "滞在しているはずなのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        (
            "#12P#0203F……微かではありますが\x01",
            "建物の中から気配は感じます。\x02\x03",

            "#0200F人の気配かどうかは\x01",
            "分かりませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#11P#0005Fティオにも分からないのか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)

    #C0005
    ChrTalk(
        0x104,
        (
            "#12P#0303Fなあ、ロイド。\x02\x03",

            "#0301F前にヨシュアたちが言ってた\x01",
            "《結社》の話が本当なら……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_84D():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84D)
    Sleep(50)

    def lambda_85D():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85D)
    Sleep(50)

    def lambda_86D():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_86D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0006
    ChrTalk(
        0x101,
        (
            "#5P#0006F……ああ、それは俺も思った。\x02\x03",

            "#0001Fこの工房が《結社》ってのと\x01",
            "関係があるかもしれない──だろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        "#12P#0303Fまーな。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#6P#0106Fた、確かにその可能性は\x01",
            "考えられるのよね……\x02\x03",

            "#0108Fかなり荒唐無稽な話だったから\x01",
            "いまいちピンと来ないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        (
            "#11P#0201Fレンさんを見ている限り、\x01",
            "現実味もありそうですが……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 20, -1, -1)
    SetChrName("老人の声")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──なるほど。\x01",
            "お前たちがレンの言っていた\x01",
            "警察の若造というわけか。\x07\x00\x02",
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

    def lambda_B10():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B10)
    EndChrThread(0x102, 0x1)

    def lambda_B21():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B21)
    EndChrThread(0x103, 0x1)

    def lambda_B32():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B32)
    EndChrThread(0x104, 0x1)

    def lambda_B43():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B43)
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
        "#5P#0005Fな……！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#6P#0105Fどこから聞こえて……！？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("老人の声")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どうやらイメルダから\x01",
            "頼まれてやって来たようだが……\x02\x03",

            "あいにく、わしの作品は\x01",
            "ブローカーごときに\x01",
            " 弄#2Rもてあそ#ばれるほど安くはない。\x02\x03",

            "とっとと帰ってもらおうか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x101,
        "#5P#0008Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#12P#0306Fチッ、確かにそう言われちゃ\x01",
            "それまでなんだがよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#5P#0203Fグゥの音も出ませんね。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("老人の声")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……フフ、とはいえ……\x02\x03",

            "こんな場所まで出向いて\x01",
            "門前払いでは気も済むまい。\x02\x03",

            "レンが世話になった借りもあるし、\x01",
            "チャンスをやらんでもない。\x07\x00\x02",
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
        "#6P#0105Fチャンス……ですか？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#5P#0001Fそれは一体……？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("老人の声")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なに、お前たちがどの程度かを\x01",
            "試させてもらうだけだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(809, 0, 100, 0)
    Sleep(600)

    def lambda_E81():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E81)
    Sleep(50)

    def lambda_E91():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E91)
    Sleep(50)

    def lambda_EA1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EA1)
    Sleep(50)

    def lambda_EB1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EB1)
    Sleep(300)
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("老人の声")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──鍵は解除した。\x02\x03",

            "その気があれば、門を開いて\x01",
            "敷地の中に入ってくるがいい。\x02\x03",

            "フフ、ただし……\x01",
            "“覚悟”だけはしてもらおうか。\x07\x00\x02",
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
        "#6P#0108Fど、どうするの……？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#11P#0001Fどうやら門に入ったら\x01",
            "“何か”が起きるのは\x01",
            "確かみたいだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#12P#0301Fまさか地雷でも埋まってる\x01",
            "ワケじゃねぇだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#11P#0206F……ひょっとしたら\x01",
            "もっとタチが悪いかもしれません。\x02",
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

    def Function_5_10E4(): pass

    label("Function_5_10E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1108")
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(500)
    Jump("Function_5_10E4")

    label("loc_1108")

    Return()

    # Function_5_10E4 end

    def Function_6_1109(): pass

    label("Function_6_1109")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_112D")
    OP_93(0x102, 0xE1, 0x1C2)
    Sleep(500)
    OP_93(0x102, 0x13B, 0x1C2)
    Sleep(500)
    Jump("Function_6_1109")

    label("loc_112D")

    Return()

    # Function_6_1109 end

    def Function_7_112E(): pass

    label("Function_7_112E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1152")
    OP_93(0x103, 0x87, 0x1C2)
    Sleep(550)
    OP_93(0x103, 0x2D, 0x1C2)
    Sleep(550)
    Jump("Function_7_112E")

    label("loc_1152")

    Return()

    # Function_7_112E end

    def Function_8_1153(): pass

    label("Function_8_1153")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1177")
    OP_93(0x104, 0x87, 0x1F4)
    Sleep(450)
    OP_93(0x104, 0xE1, 0x1F4)
    Sleep(450)
    Jump("Function_8_1153")

    label("loc_1177")

    Return()

    # Function_8_1153 end

    def Function_9_1178(): pass

    label("Function_9_1178")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "門を開けて中に入る\x01",      # 0
            "やめておく\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C8")
    Return()

    label("loc_11C8")

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

    def lambda_142A():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_142A)
    Sleep(50)

    def lambda_1447():
        OP_97(0x102, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1447)
    Sleep(50)

    def lambda_1464():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1464)
    Sleep(50)

    def lambda_1481():
        OP_97(0x103, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1481)
    OP_68(2000, 1500, 34500, 5000)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0026
    ChrTalk(
        0x103,
        "#12P#0207F皆さん……！\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    WaitChrThread(0x101, 1)

    def lambda_1501():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1501)
    WaitChrThread(0x102, 1)

    def lambda_1512():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1512)
    WaitChrThread(0x104, 1)

    def lambda_1523():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1523)
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

    def lambda_15FA():
        OP_97(0x103, 0x0, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15FA)
    WaitChrThread(0x103, 1)

    def lambda_1618():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1618)

    def lambda_1625():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1625)

    def lambda_1632():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1632)

    def lambda_163F():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_163F)
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
        "#11P#0007Fなあっ……！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        "#5P#0107Fて、天使と化物……！？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#5P#0310Fおいおい！\x01",
            "予想外すぎんだろ！？\x02",
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
        "#11P#0010Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        "#5P#0307F来るぞ！\x02",
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

    # Function_9_1178 end

    def Function_10_181F(): pass

    label("Function_10_181F")


    def lambda_1824():
        OP_97(0xC, 0x0, 0xFFFFEC78, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1824)

    def lambda_183E():
        OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_183E)
    Sleep(50)

    def lambda_1852():
        OP_97(0xD, 0x0, 0xFFFFEB7E, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1852)

    def lambda_186C():
        OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_186C)
    Sleep(50)

    def lambda_1880():
        OP_97(0xE, 0x0, 0xFFFFEA84, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1880)

    def lambda_189A():
        OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_189A)
    Sleep(50)

    def lambda_18AE():
        OP_97(0xF, 0x0, 0xFFFFE98A, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_18AE)

    def lambda_18C8():
        OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_18C8)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xF, 3)
    Sound(868, 0, 100, 0)

    def lambda_18FF():
        OP_97(0x10, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_18FF)

    def lambda_1919():
        OP_A7(0x10, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1919)
    Sleep(50)

    def lambda_192D():
        OP_97(0x11, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_192D)

    def lambda_1947():
        OP_A7(0x11, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1947)
    WaitChrThread(0x10, 3)

    def lambda_195C():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_195C)
    WaitChrThread(0x11, 3)

    def lambda_1971():
        OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1971)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x11, 3)
    Return()

    # Function_10_181F end

    def Function_11_198E(): pass

    label("Function_11_198E")

    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)
    Sleep(1200)
    Sound(888, 0, 100, 0)
    Return()

    # Function_11_198E end

    def Function_12_19B0(): pass

    label("Function_12_19B0")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "門を開けて中に入る\x01",      # 0
            "やめておく\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A00")
    Return()

    label("loc_1A00")

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

    def lambda_1C51():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C51)
    Sleep(50)

    def lambda_1C6E():
        OP_97(0x102, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C6E)
    Sleep(50)

    def lambda_1C8B():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C8B)
    Sleep(50)

    def lambda_1CA8():
        OP_97(0x103, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CA8)
    OP_68(2000, 1500, 35500, 5000)
    OP_6F(0x79)
    StopBGM(0xFA0)
    OP_68(1060, 1500, 34190, 6000)
    MoveCamera(53, 30, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(20000, 7000)
    BeginChrThread(0x12, 1, 0, 11)
    BeginChrThread(0xB, 1, 0, 10)

    def lambda_1D14():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D14)

    def lambda_1D21():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D21)

    def lambda_1D2E():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D2E)

    def lambda_1D3B():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D3B)
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

    # Function_12_19B0 end

    def Function_13_1E18(): pass

    label("Function_13_1E18")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C7")
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

    def lambda_208A():
        OP_A6(0xC, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_208A)
    PlayEffect(0x0, 0x0, 0xC, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_20DD():
        OP_A6(0xD, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_20DD)
    PlayEffect(0x0, 0x1, 0xD, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_2130():
        OP_A6(0xE, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2130)
    PlayEffect(0x0, 0x2, 0xE, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_2183():
        OP_A6(0xF, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2183)
    PlayEffect(0x0, 0x3, 0xF, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_21D6():
        OP_A6(0x10, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_21D6)
    PlayEffect(0x0, 0x4, 0x10, 0x0, 0, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_2229():
        OP_A6(0x11, 0x0, 0x14, 0x0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2229)
    PlayEffect(0x0, 0x5, 0x11, 0x0, 0, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(868, 0, 100, 0)

    def lambda_2289():
        OP_A7(0xC, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_2289)
    Sleep(50)

    def lambda_229D():
        OP_A7(0xD, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_229D)
    Sleep(50)

    def lambda_22B1():
        OP_A7(0xE, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_22B1)
    Sleep(50)

    def lambda_22C5():
        OP_A7(0xF, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_22C5)
    Sleep(50)

    def lambda_22D9():
        OP_A7(0x10, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_22D9)
    Sleep(50)

    def lambda_22ED():
        OP_A7(0x11, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_22ED)
    WaitChrThread(0xC, 3)
    StopEffect(0x0, 0x2)

    def lambda_2305():
        OP_A7(0xC, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_2305)
    WaitChrThread(0xD, 3)
    StopEffect(0x1, 0x2)

    def lambda_231D():
        OP_A7(0xD, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_231D)
    WaitChrThread(0xE, 3)
    StopEffect(0x2, 0x2)

    def lambda_2335():
        OP_A7(0xE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_2335)
    WaitChrThread(0xF, 3)
    StopEffect(0x3, 0x2)

    def lambda_234D():
        OP_A7(0xF, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_234D)
    WaitChrThread(0x10, 3)
    StopEffect(0x4, 0x2)

    def lambda_2365():
        OP_A7(0x10, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2365)
    WaitChrThread(0x11, 3)
    StopEffect(0x5, 0x2)

    def lambda_237D():
        OP_A7(0x11, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_237D)
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
        "#11P#0010Fこ、これは……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#5P#0101Fゼンマイと歯車……？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#11P#0201Fどうやら……\x01",
            "“人形”だったようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#5P#0306Fおいおい、どんな人形だよ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 2)), scpexpr(EXPR_END)), "loc_24FA")

    #N0036
    NpcTalk(
        0xB,
        "老人の声",
        (
            "フン……\x01",
            "余計な時間を取らせおって。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2559")

    label("loc_24FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 1)), scpexpr(EXPR_END)), "loc_2529")

    #N0037
    NpcTalk(
        0xB,
        "老人の声",
        "まあ、この程度か。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2559")

    label("loc_2529")


    #N0038
    NpcTalk(
        0xB,
        "老人の声",
        (
            "ふむ、それなりに\x01",
            "使えるようだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2559")

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
        "#11P#0005Fあ……\x02",
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

    def lambda_2606():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2606)

    def lambda_2613():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2613)

    def lambda_2620():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2620)

    def lambda_262D():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_262D)
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
            "わしの名はヨルグ。\x01",
            "ローゼンベルクの人形師だ。\x02\x03",

            "クロスベル警察、\x01",
            "特務支援課の小僧どもだな？\x02",
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
        "#12P#0001Fえ、ええ……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#12P#0101Fえっと、レンちゃんに\x01",
            "お聞きになったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xB,
        (
            "#5P#3903Fあの子に聞かずとも\x01",
            "その程度の情報くらい\x01",
            "世捨て人の耳にも届く。\x02\x03",

            "#3900F少々面白くはないが……\x01",
            "約束は約束だ。\x02\x03",

            "持っていくがいい。\x02",
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
            "を受け取った。\x02",
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
        "#12P#0005Fど、どうも……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#11P#0205F……随分あっさりと\x01",
            "渡してくれるんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xB,
        (
            "#5P#3903Fフフ……\x01",
            "人形には人形の運命があろう。\x02\x03",

            "下種なブローカーの手に渡ろうと\x01",
            "真に引き取られるべき相手と\x01",
            "巡り合う可能性もある。\x02\x03",

            "#3900F……人と同じく\x01",
            "全ては女神の巡り合わせだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        "#12P#0305Fなるほどねぇ……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        (
            "#12P#0106Fそう言っていただけると\x01",
            "こちらも助かりますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#12P#0013Fそ、それよりも……！\x02\x03",

            "#0007Fさっきの天使や化物は\x01",
            "いったい何なんですか！？\x02\x03",

            "やはりレンが属しているという\x01",
            "《結社》の……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "#5P#3903F──バニングス捜査官。\x02\x03",

            "#3901F……そのような事まで\x01",
            "気にしている余裕はあるのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x101,
        "#12P#0011Fっ！？\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "#5P#3903Fわしはただの“人形師”だ。\x01",
            "それ以上でも、以下でもない。\x02\x03",

            "今、お前たちが直面している\x01",
            "この地をめぐる様々な問題……\x02\x03",

            "それらに直接、\x01",
            "関わっているわけでもない。\x02\x03",

            "#3901Fなのに、底知れぬ深淵を\x01",
            "覗き込むつもりかと聞いている。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        "#12P#0010Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        (
            "#5P#3903Fレンにしても同じ……\x02\x03",

            "あの子をめぐる因縁は\x01",
            "お前たちと直接、\x01",
            "絡んでいるわけではない。\x02\x03",

            "#3900F余計な気遣いをする前に\x01",
            "他に気に掛ける相手がおろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#12P#0005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#12P#0103F……キーアちゃんの事ですね。\x02\x03",

            "#0101F貴方の人形という名目で\x01",
            "出品される所だった訳ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#11P#0201Fどうやら、その程度の情報は\x01",
            "とっくにご存知のようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#12P#0301F爺さん、あんたキー坊のこと、\x01",
            "なんか知ってんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xB,
        (
            "#5P#3903Fフフ、先ほども言ったように\x01",
            "人形には人形の運命がある。\x02\x03",

            "#3900Fわしが手がけた人形が\x01",
            "数奇な運命を経て命を宿らせ、\x01",
            "人間になった可能性もあるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        "#11P#0205Fえ。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#12P#0011Fなっ！？\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xB,
        (
            "#5P#3903Fフフ、伝え聞く限り、\x01",
            "その娘と同じような面差しの\x01",
            "人形を手がけたことは無いな。\x02\x03",

            "#3900F単にローゼンベルクの名を\x01",
            "何者かに利用されただけだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        "#12P#0106Fふうっ……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#12P#0006F……心臓に悪い冗談ですね。\x02\x03",

            "#0001Fそれでは本当に\x01",
            "キーアの事はご存知ないと？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        (
            "#5P#3901F少なくとも、競売会の場に\x01",
            "紛れ込んでいた事情は知らぬ。\x02\x03",

            "それに関してはレンも同じだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        "#12P#0008Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#12P#0308Fフン、少しは手がかりが\x01",
            "あると思ったんだがな……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        (
            "#12P#0105Fそういえば……\x01",
            "レンちゃんは中にいるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        (
            "#5P#3903Fいや、丁度出かけている。\x02\x03",

            "#3900F気まぐれな子だからな。\x01",
            "ここに会いに来ても無駄だ。\x02",
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
        "#12P#0011Fあ、あの……！？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xB,
        (
            "#11P#3903F──話はここまでだ。\x02\x03",

            "とっととイメルダに\x01",
            "その人形を届けに戻るがいい。\x02\x03",

            "#3900F代金はいつもの口座に\x01",
            "振り込むように伝えておけ。\x02",
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

    def lambda_32BB():
        OP_97(0xB, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_32BB)

    def lambda_32D5():
        OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_32D5)
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
    Jump("loc_393C")

    label("loc_33C7")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 2)), scpexpr(EXPR_END)), "loc_3600")
    SetMessageWindowPos(25, 20, -1, -1)
    SetChrName("老人の声")

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──力押しは無駄だ。\x02\x03",

            "ティルドーンは物理攻撃を反射する上、\x01",
            "放っておくと場の崩壊を引き起こす。\x02\x03",

            "アーツを解除する天使#4Rアンヘル#たちとの連携は\x01",
            "無二の強さを持つと言えるだろう。\x02\x03",

            "この連携を如何に突き崩すか……\x01",
            "少しは頭を使って戦うのだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x30, 0x1, 0x4)
    Jump("loc_388A")

    label("loc_3600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 1)), scpexpr(EXPR_END)), "loc_36E3")
    SetMessageWindowPos(25, 20, -1, -1)
    SetChrName("老人の声")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──駄目だな、見世物にもならんぞ。\x02\x03",

            "天使#4Rアンヘル#たちは\x01",
            "素早い動きでアーツの駆動を解除する。\x02\x03",

            "戦技#4Rクラフト#を中心とした戦法を組み立ててみろ。\x01",
            "少しはマシになるだろう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD3, 2)
    OP_29(0x30, 0x1, 0x3)
    Jump("loc_388A")

    label("loc_36E3")

    SetMessageWindowPos(25, 20, -1, -1)
    SetChrName("老人の声")

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──話にならんな。\x01",
            "出直してくるがいい。\x07\x00\x02",
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
        "#11P#0010F#30Wくっ……\x02",
    )

    CloseMessageWindow()
    OP_A6(0x102, 0x0, 0x14, 0x1F4, 0x7D0)
    Sleep(300)

    #C0077
    ChrTalk(
        0x102,
        "#6P#0108F#30Wい、いったい今のは……\x02",
    )

    CloseMessageWindow()
    OP_A6(0x103, 0x0, 0x14, 0x1F4, 0x7D0)
    Sleep(300)

    #C0078
    ChrTalk(
        0x103,
        (
            "#11P#0206F#30Wどう考えても普通の魔獣では\x01",
            "ありませんでしたが……\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x104, 0x0, 0x14, 0x1F4, 0x7D0)
    Sleep(300)

    #C0079
    ChrTalk(
        0x104,
        (
            "#12P#0301F#30Wいずれにせよ、一筋縄じゃ\x01",
            "行かねぇのは確かだな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD3, 1)
    OP_29(0x30, 0x1, 0x2)

    label("loc_388A")

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

    label("loc_393C")

    Return()

    # Function_13_1E18 end

    def Function_14_393D(): pass

    label("Function_14_393D")

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

    def lambda_39DE():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39DE)
    Sleep(50)

    def lambda_39FB():
        OP_97(0x103, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_39FB)
    Sleep(50)

    def lambda_3A18():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A18)
    Sleep(50)

    def lambda_3A35():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A35)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(120, 0, 100, 0)

    def lambda_3A72():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A72)
    Sleep(50)

    def lambda_3A82():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A82)
    Sleep(50)

    def lambda_3A92():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A92)
    Sleep(50)

    def lambda_3AA2():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AA2)
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
            "#12P#0303F結社──《身喰らう蛇#10Rウ ロ ボ ロ ス#》か。\x02\x03",

            "#0301Fさっきの爺さんが\x01",
            "どういう立場かは知らねぇが\x01",
            "とんでもない連中みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        (
            "#11P#0206Fさっきの人形……\x01",
            "エプスタイン財団でも\x01",
            "同等のものを作るのは不可能です。\x02\x03",

            "#0201FリベールのＺＣＦでは研究開発が\x01",
            "始まっているそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#6P#0106Fローゼンベルク工房……\x01",
            "まさかここまで得体の知れない\x01",
            "所だったなんて……\x02\x03",

            "#0108F……確かに今の私たちには\x01",
            "手に余るかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#11P#0006Fそうだな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    TurnDirection(0x101, 0x104, 500)

    def lambda_3D32():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D32)
    Sleep(50)

    def lambda_3D42():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3D42)
    Sleep(300)

    #C0085
    ChrTalk(
        0x101,
        (
            "#5P#0000F……とにかくこのトランクを\x01",
            "アンティーク屋に届けよう。\x02\x03",

            "イメルダさんが待ってるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        "#12P#0300Fだな。\x02",
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

    # Function_14_393D end

    def Function_15_3DEC(): pass

    label("Function_15_3DEC")

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

    def lambda_3ED9():
        OP_95(0xFE, 950, 0, 20480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3ED9)

    def lambda_3EF3():
        OP_95(0xFE, 2040, 0, 19440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EF3)

    def lambda_3F0D():
        OP_95(0xFE, -300, 0, 19600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3F0D)

    def lambda_3F27():
        OP_95(0xFE, 620, 0, 18330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F27)
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
        "#0005F#11Pここは……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        (
            "#0105F随分、雰囲気のある建物ね。\x02\x03",

            "#0101F廃墟という感じでもないし、\x01",
            "誰か住んでいそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x104, 0x13B, 0x1F4)

    #C0089
    ChrTalk(
        0x104,
        "#0305Fお、そこに看板が出てるぜ。\x02",
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
            "   『ローゼンベルク工房』\x01",
            "関係者以外の立ち入りを禁ずる。\x07\x00\x02",
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
        "#0102F#6Pああ、ここが……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0092
    ChrTalk(
        0x101,
        "#0005F#2Pエリィ、知ってるのか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0093
    ChrTalk(
        0x102,
        (
            "#0100F#6Pええ、その筋では有名な人形工房よ。\x02\x03",

            "高価なアンティークドールを手がける\x01",
            "天才人形師がいると言われているわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0094
    ChrTalk(
        0x104,
        (
            "#0300F#2Pへえ……\x01",
            "そんな工房があるのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x103,
        (
            "#0203F#12Pわたしも名前くらいは\x01",
            "聞いたことがあります……\x02\x03",

            "#0200Fたしかオークションなどで\x01",
            "途方もない値が付けられるとか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0096
    ChrTalk(
        0x102,
        (
            "#0104F#5Pええ……幾つか見た事があるけど\x01",
            "まさに芸術品という感じだったわ。\x02\x03",

            "#0100Fクロスベルにあるとは聞いてたけど\x01",
            "こんな人里離れた場所にあったのね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0097
    ChrTalk(
        0x101,
        (
            "#0003F#5P天才人形師か……\x02\x03",

            "#0001F看板の警告といい、\x01",
            "気難しそうな雰囲気だけど\x01",
            "話を聞かせてもらえないかな？\x02",
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
        "少女の声",
        "#1P──おじいさんなら留守よ。\x02",
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

    def lambda_44E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_44E7)
    OP_68(-2610, 800, 21420, 4000)
    MoveCamera(55, 14, 0, 4000)

    def lambda_4514():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4514)

    def lambda_4521():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4521)
    Sleep(50)

    def lambda_4531():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4531)

    def lambda_453E():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_453E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0099
    ChrTalk(
        0x101,
        "#0005F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        "#0105F#3P（女の子……？）\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#0200F#3P（この工房の\x01",
            "  子供でしょうか……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-3240, 800, 21630, 2000)
    OP_97(0x8, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
    OP_6F(0x1)

    #N0102
    NpcTalk(
        0x8,
        "ドレスの少女",
        (
            "#3309F#11Pうふふ、こんにちは。\x02\x03",

            "#3300Fお兄さんたち、だあれ？\x02\x03",

            "この工房に何の用かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#0005F#6Pえっと……\x02",
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
            "#0004F#6Pその、怪しい者じゃないよ。\x02\x03",

            "#0000F俺たちは、クロスベル市の\x01",
            "警察の人間なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #N0105
    NpcTalk(
        0x8,
        "ドレスの少女",
        (
            "#3305F#11Pあら、警察のヒトなんだ。\x02\x03",

            "#3304Fふぅん、警察のヒトって\x01",
            "街でしか見たことないけど……\x02\x03",

            "#3300Fこんな所にも見回りに来るのね？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#0005F#6Pああ、その……\x01",
            "見回りに来たわけじゃないんだ。\x02\x03",

            "#0000Fこの辺りに出る魔獣について\x01",
            "話を聞かせてもらえないかと思って。\x02",
        )
    )

    CloseMessageWindow()

    #N0107
    NpcTalk(
        0x8,
        "ドレスの少女",
        (
            "#3305F#11Pこの辺りに出る魔獣……\x01",
            "どんな魔獣について知りたいの？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#0106F#6Pその、狼の姿をした魔獣なの。\x02\x03",

            "#0101Fおじいさんから\x01",
            "聞いたことはないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #N0109
    NpcTalk(
        0x8,
        "ドレスの少女",
        (
            "#3303F#11Pううん、聞いたことないわ。\x02\x03",

            "#3308Fでも、そうね……\x01",
            "さっき遠吠えみたいな声が\x01",
            "遠くから聞こえてきたけど。\x02\x03",

            "#3300Fそれのことかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0001F#6Pああ、そうなんだ。\x02\x03",

            "おじいさんは留守って言ったね。\x01",
            "工房には他に誰もいないのかい？\x02",
        )
    )

    CloseMessageWindow()

    #N0111
    NpcTalk(
        0x8,
        "ドレスの少女",
        (
            "#3300F#11Pええ、そうよ。\x02\x03",

            "夕方には戻ってくるって\x01",
            "言ってたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#0003F#6Pそうか……\x02\x03",

            "#0001F──さっきも言ったように、\x01",
            "この辺りで危険な魔獣が\x01",
            "うろついているみたいなんだ。\x02\x03",

            "おじいさんが帰るまで\x01",
            "おうちの中に居てくれるかい？\x02",
        )
    )

    CloseMessageWindow()

    #N0113
    NpcTalk(
        0x8,
        "ドレスの少女",
        (
            "#3305F#11P別に構わないけど……\x02\x03",

            "#3304Fうふふ、お兄さんたちに\x01",
            "付いていくのも面白そうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#0005F#6Pへ……\x02",
    )

    CloseMessageWindow()

    #N0115
    NpcTalk(
        0x8,
        "ドレスの少女",
        (
            "#3302F#11Pだって、その狼さんと\x01",
            "鬼ゴッコをしてるんでしょう？\x02\x03",

            "#3309Fそれとも隠れん坊かしら？\x01",
            "うふふ、とっても楽しそうだわ。\x02",
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
            "#0204F#3P確かに……\x01",
            "そう言えなくもないですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        (
            "#0302F#6Pはは、なかなか\x01",
            "面白いお嬢ちゃんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0011F#6Pえっと……\x01",
            "何があるかも分からないから\x01",
            "ちょっと連れて行けないんだ。\x02\x03",

            "#0006Fゴメン……\x01",
            "家の中にいてくれないかな？\x02",
        )
    )

    CloseMessageWindow()

    #N0119
    NpcTalk(
        0x8,
        "ドレスの少女",
        (
            "#3301F#11Pもう、つまらないわ。\x02\x03",

            "《彼》が直っていれば\x01",
            "タイクツなのも紛れるのに……\x02\x03",

            "#3304F仕方ないから今日も\x01",
            "あっちに潜ってソバカス君と\x01",
            "遊んであげようかしら？\x02\x03",

            "それともガラスのお城に\x01",
            "遊びに行ってみようかしら？\x02",
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
        "#0005F#6Pあっちに潜って……？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x102,
        "#0105F#3Pガラスのお城……？\x02",
    )

    CloseMessageWindow()

    #N0122
    NpcTalk(
        0x8,
        "ドレスの少女",
        (
            "#3309F#11Pうふふ、こちらの事よ。\x02\x03",

            "#3302Fそうだ──\x01",
            "まだ名乗ってなかったわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("ドレスの少女")

    #A0123
    AnonymousTalk(
        0xFF,
        (
            "うふふ……\x01",
            "レンって呼んでちょうだい。\x02\x03",

            "本当はもう一人、\x01",
            "紹介したい子がいるんだけど。\x02\x03",

            "あいにく右足を怪我してて\x01",
            "おじいさんの治療を受けてるの。\x02",
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
            "#0000F#6Pそ、そうなのか。\x01",
            "（人形かなにかの話かな……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "#3304F#11Pうふふ、どうやら狼さん、\x01",
            "とっても頭がいいみたいね。\x02\x03",

            "ちょっと遊んでみたいけど……\x01",
            "レンはもう大人だから\x01",
            "あんまりワガママは言わないわ。\x02\x03",

            "#3302F頑張ってね、支援課のお兄さんたち。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#0012F#6Pあ、ああ……ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x102,
        "#0102F#3Pあなたも気をつけてね。\x02",
    )

    CloseMessageWindow()

    def lambda_513F():

        label("loc_513F")

        TurnDirection(0x101, 0x8, 500)
        Yield()
        Jump("loc_513F")

    QueueWorkItem2(0x101, 1, lambda_513F)

    def lambda_5151():

        label("loc_5151")

        TurnDirection(0x102, 0x8, 500)
        Yield()
        Jump("loc_5151")

    QueueWorkItem2(0x102, 1, lambda_5151)

    def lambda_5163():

        label("loc_5163")

        TurnDirection(0x103, 0x8, 500)
        Yield()
        Jump("loc_5163")

    QueueWorkItem2(0x103, 1, lambda_5163)

    def lambda_5175():

        label("loc_5175")

        TurnDirection(0x104, 0x8, 500)
        Yield()
        Jump("loc_5175")

    QueueWorkItem2(0x104, 1, lambda_5175)
    OP_93(0x8, 0x0, 0x190)
    OP_95(0x8, 1950, 0, 25620, 2000, 0x0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x0)
    OP_68(-4220, 600, 23220, 4000)
    MoveCamera(45, 14, 0, 4000)

    def lambda_51D3():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_51D3)
    Sleep(1000)

    def lambda_51F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_51F0)
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
            "#0204F#6P……なかなか\x01",
            "ユニークな女の子でしたね。\x02\x03",

            "#0202Fその有名な人形師の\x01",
            "お孫さんあたりでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0129
    ChrTalk(
        0x104,
        (
            "#0304F#11Pま、そんな所だろ。\x02\x03",

            "#0302Fしかし随分とまあ、\x01",
            "マセたガキンチョだったな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0130
    ChrTalk(
        0x102,
        (
            "#0109F#5Pふふ、とっても\x01",
            "可愛い子だったじゃない。\x02\x03",

            "#0102Fちょっと謎めいた言い方が\x01",
            "また魅力的っていうか……\x02",
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
        "#0105F#6Pロイド、どうしたの？\x02",
    )

    CloseMessageWindow()

    def lambda_53D7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_53D7)
    Sleep(50)

    def lambda_53E7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_53E7)
    WaitChrThread(0x104, 1)

    #C0133
    ChrTalk(
        0x104,
        (
            "#0305F#6Pなんだよ。\x01",
            "狐につままれたみたいな顔して。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x103,
        "#0200F#6P何か気になることでも……？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#0003F#5Pいや……\x01",
            "大した事じゃないんだけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0136
    ChrTalk(
        0x101,
        (
            "#0001F#11Pあの子、最後に\x01",
            "『支援課のお兄さんたち』って\x01",
            "言ってなかったか……？\x02",
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
        "#0101F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        (
            "#0205F#6Pそういえば……\x01",
            "名乗っていませんでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#0301F#6P何であんなガキンチョが\x01",
            "俺たちのことを知ってんだよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#0006F#11Pまあ、クロスベルタイムズを見て\x01",
            "支援課の事を知ったのかもしれない。\x02\x03",

            "それで俺たちがそうだと\x01",
            "気付いた可能性はあるけど……\x02\x03",

            "#0000Fそれにしたって\x01",
            "不思議な子だなと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        "#0300F#6Pふむ……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        "#0203F#6P……確かに。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#0003F#11P……まあ、とりあえず狼型魔獣は\x01",
            "こちらの方には来ていないみたいだ。\x02\x03",

            "#0000Fいったん、三叉路まで戻って\x01",
            "鉱山町の方に向かおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x102,
        "#0100F#6Pええ、分かったわ。\x02",
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

    # Function_15_3DEC end

    def Function_16_57E8(): pass

    label("Function_16_57E8")

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
            "#0808F……うーん。\x01",
            "人気#4Rひとけ#は無さそうだけど……\x02\x03",

            "#0801Fねえヨシュア。\x01",
            "本当にここがそうなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        (
            "#0903F……確証はないけど\x01",
            "その可能性は高いと思う。\x02\x03",

            "#0908Fただ《十三工房》については\x01",
            "僕も知らない事が多いんだ。\x02\x03",

            "古#2Rいにしえ#の技術を今に伝える\x01",
            "１２の工房を一つにまとめた\x01",
            "ネットワークらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "#0803Fそのうちの１つが\x01",
            "この人形工房ってわけね……\x02\x03",

            "#0801F……いかにもあの子が\x01",
            "居そうな場所ではあるけど。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5ADD():
        OP_93(0xA, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5ADD)
    WaitChrThread(0xA, 2)

    #C0148
    ChrTalk(
        0xA,
        (
            "#0901Fどうする、エステル。\x02\x03",

            "やっぱり僕が調べて来ようか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B2C():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5B2C)
    WaitChrThread(0x9, 2)

    #C0149
    ChrTalk(
        0x9,
        (
            "#0804F……ううん、いいわ。\x02\x03",

            "今は《結社》と直接、\x01",
            "やり合ってるわけじゃないし。\x02\x03",

            "#0802F本当の意味で\x01",
            "あの子を捕まえなくっちゃ\x01",
            "ルール違反になりそうだもん。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "#0904F……そうか。\x02\x03",

            "#0900F《競売会》の方も気になるし\x01",
            "今はそっちを気に懸けておこうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x9,
        "#0800Fうん、そうしましょ。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#0005Fあれっ……\x01",
            "エステルとヨシュア……！？\x02",
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

    def lambda_5CD3():
        OP_95(0xFE, 2000, 0, 20250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5CD3)
    Sleep(50)

    def lambda_5CF0():
        OP_95(0xFE, 1000, 0, 19000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5CF0)
    Sleep(50)

    def lambda_5D0D():
        OP_95(0xFE, 3000, 0, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5D0D)
    Sleep(50)

    def lambda_5D2A():
        OP_95(0xFE, 2000, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5D2A)

    def lambda_5D44():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5D44)

    def lambda_5D51():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5D51)

    #C0153
    ChrTalk(
        0x9,
        "#0805F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        "#0905F君たちは……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 2)
    WaitChrThread(0xA, 2)
    OP_6F(0x51)

    #C0155
    ChrTalk(
        0x104,
        "#0305Fおいおい、こりゃ驚きだな。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        (
            "#0202F……覚えのある気配が\x01",
            "すると思ってましたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        (
            "#0813F#5Pロ、ロイド君たち……\x01",
            "どうしてここに？\x02\x03",

            "#0801F……もしかして\x01",
            "この工房に用事でもあるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#0005Fいや、山道に出たついでに\x01",
            "足を延ばしただけだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x102,
        (
            "#0105Fエステルさんたちこそ\x01",
            "こちらの人形工房に用でも？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x9,
        (
            "#0809F#5Pえ、えっと……\x01",
            "ちょっと事情があって。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        (
            "#0904F個人的な用で訪ねたんだけど\x01",
            "留守にしているみたいだね。\x02\x03",

            "#0900F……それより、昨日はお疲れさま。\x01",
            "身体の方は平気かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#0012Fああ、軽く筋肉痛だけどね。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        (
            "#0300Fそういうお前さんたちの方は\x01",
            "ピンピンしてやがるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x9,
        (
            "#0802F#5Pあはは、普段から街道を\x01",
            "歩き回ってるからかしら？\x02\x03",

            "#0806F……えっと、ゴメンなさい。\x01",
            "あたしたちそろそろ\x01",
            "街に戻らないといけなくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        "#0902Fお先に失礼させてもらうよ。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#0002Fそっか……\x01",
            "それじゃあ気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        "#0809Fうん、ロイド君たちもね！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0xA, 2, 0, 18)

    def lambda_60F5():

        label("loc_60F5")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_60F5")

    QueueWorkItem2(0x101, 2, lambda_60F5)

    def lambda_6107():

        label("loc_6107")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6107")

    QueueWorkItem2(0x102, 2, lambda_6107)

    def lambda_6119():

        label("loc_6119")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6119")

    QueueWorkItem2(0x103, 2, lambda_6119)

    def lambda_612B():

        label("loc_612B")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_612B")

    QueueWorkItem2(0x104, 2, lambda_612B)
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

    def lambda_6201():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6201)

    def lambda_620E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_620E)

    def lambda_621B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_621B)

    def lambda_6228():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6228)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)

    #C0168
    ChrTalk(
        0x104,
        (
            "#0301F何かあからさまに\x01",
            "隠し事をしてやがったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        (
            "#0200Fでも、後ろめたい感じでは\x01",
            "無かったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        (
            "#0106F#3Pうーん……あんまり\x01",
            "詮索するわけにもいかないし。\x02\x03",

            "#0100Fこちらも留守みたいだし、\x01",
            "私たちも引き返しましょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 0)), scpexpr(EXPR_END)), "loc_63C5")

    #C0171
    ChrTalk(
        0x101,
        (
            "#0003Fああ……そうしよう。\x02\x03",

            "#0008F（……前にここで\x01",
            "  レンと初めて会ったけど……）\x02\x03",

            "（ひょっとしてあの２人、\x01",
            "  彼女の知り合いなのかな？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_644F")

    label("loc_63C5")


    #C0172
    ChrTalk(
        0x101,
        (
            "#0003Fああ……そうしよう。\x02\x03",

            "#0008F（……前にここで\x01",
            "  女の子と会ったけど……）\x02\x03",

            "（ひょっとしてあの２人、\x01",
            "  彼女の知り合いなのかな？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_644F")

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

    # Function_16_57E8 end

    def Function_17_64FD(): pass

    label("Function_17_64FD")

    OP_95(0xFE, 5000, 0, 20750, 2000, 0x0)
    OP_95(0xFE, 1000, 0, 0, 2000, 0x0)
    Return()

    # Function_17_64FD end

    def Function_18_6526(): pass

    label("Function_18_6526")

    Sleep(50)
    OP_95(0xFE, 4750, 0, 21000, 2000, 0x0)
    OP_95(0xFE, 750, 0, 0, 2000, 0x0)
    Return()

    # Function_18_6526 end

    def Function_19_6552(): pass

    label("Function_19_6552")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   『ローゼンベルク工房』\x01",
            "関係者以外の立ち入りを禁ずる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_6552 end

    def Function_20_65C3(): pass

    label("Function_20_65C3")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_65D4")
    Jump("loc_6630")

    label("loc_65D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_6630")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_65EF")
    Jump("loc_6630")

    label("loc_65EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 1)), scpexpr(EXPR_END)), "loc_6604")
    Call(0, 12)
    TalkEnd(0xFF)
    Return()

    label("loc_6604")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_661D")
    Call(0, 9)
    TalkEnd(0xFF)
    Return()

    label("loc_661D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6630")
    Call(0, 4)
    TalkEnd(0xFF)
    Return()

    label("loc_6630")

    SetChrName("")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_20_65C3 end

    def Function_21_6659(): pass

    label("Function_21_6659")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっている。\x01",
            "老人が出てくる気配もない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_21_6659 end

    SaveToFile()

Try(main)
