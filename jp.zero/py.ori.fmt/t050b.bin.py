from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "鉱山長ホフマン",         # 1
        "鉱員マルロ",             # 2
        "鉱員ガンツ",             # 3
        "魔獣",                   # 4
        "魔獣",                   # 5
        "魔獣",                   # 6
        "SE制御",                 # 7
        "BT050b",                 # 8
        "マインツ山道",           # 9
        "マインツ鉱山",           # 10
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

    PlaceName(11.0, 0.0, -23.0, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-32.0, 0.0, 62.0, 0x0000, 0x0000, "マインツ鉱山")
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
        "Function_6_F48",          # 06, 6
        "Function_7_F72",          # 07, 7
        "Function_8_1D62",         # 08, 8
        "Function_9_1D9E",         # 09, 9
        "Function_10_1DBC",        # 0A, 10
        "Function_11_1DFB",        # 0B, 11
        "Function_12_1E2C",        # 0C, 12
        "Function_13_1E48",        # 0D, 13
        "Function_14_1E67",        # 0E, 14
        "Function_15_1EAD",        # 0F, 15
        "Function_16_1EFF",        # 10, 16
        "Function_17_1F51",        # 11, 17
        "Function_18_1FA3",        # 12, 18
        "Function_19_2009",        # 13, 19
        "Function_20_204C",        # 14, 20
        "Function_21_26BA",        # 15, 21
        "Function_22_2712",        # 16, 22
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
            "……おし。\x01",
            "とりあえず全員帰ったみてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "ガンツとマルロの奴は\x01",
            "酒場に行ったみてえだが……\x01",
            "まぁ、屋内にいる分には問題ねぇか。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#0005Fあの……\x01",
            "ここで何をしているんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0004
    ChrTalk(
        0x8,
        "ああ、鉱山の扉を閉めてるのよ。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "たまに魔獣が湧くこともあるから\x01",
            "中に誰も残ってねぇか\x01",
            "確認しなきゃなんねぇんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#0005F魔獣が……\x02",
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
            "#0105F……ロイド、どうしたの？\x02\x03",

            "なにか考えてたみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7C4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C4)

    def lambda_7D1():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7D1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0008
    ChrTalk(
        0x101,
        (
            "#0001Fああ、うん……\x02\x03",

            "#0000F作戦開始までの時間、\x01",
            "ここで少しでも\x01",
            "鍛えられないかと思ってさ。\x02",
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
            "#0300Fそりゃ、いい考えかも\x01",
            "しれねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#0203F街道に出ているほどの\x01",
            "時間もありませんしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "……何の話だ？\x02",
    )

    CloseMessageWindow()

    def lambda_905():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_905)

    def lambda_912():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_912)

    def lambda_91F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_91F)

    def lambda_92C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_92C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0012
    ChrTalk(
        0x101,
        "#0000Fあの、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは事情を話し、\x01",
            "鉱山を使わせてもらえないか持ちかけた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x8,
        "ふむ、そういうことか。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "だが、中に入れるわけにはいかねぇな。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "よそ者を中に入れて怪我でもさせたら\x01",
            "鉱山長として示しがつかねえからよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#0006F……そ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#0103Fこればかりは流石に仕方ないわね……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "……と、言いたいところだが。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0005F……え。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "見たところ、お前らも\x01",
            "鉱員に負けず劣らずタフに\x01",
            "できているようだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "荒らさねぇって約束できるなら\x01",
            "特別に許可してやってもいいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#0000F本当ですか！\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        "#0309Fハハ、なかなか気前がいいッスね。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "なに、俺もマックスを怪我さした\x01",
            "狼の野郎に、何とか一泡吹かせてやりたくてよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "それをお前らがやってくれるってんだ、\x01",
            "喜んで協力させてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "よし、ちょっと待ってな。\x02",
    )

    CloseMessageWindow()

    def lambda_C47():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C47)
    WaitChrThread(0x8, 1)
    Sound(809, 0, 100, 0)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ホフマンは鉱山の扉の鍵を開けた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_C8D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C8D)
    WaitChrThread(0x8, 1)

    #C0029
    ChrTalk(
        0x8,
        (
            "それじゃあ、せいぜい\x01",
            "怪我しねぇように気をつけな。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "ああそれと、左奥にある扉の奥は廃坑になってる。\x01",
            "そっちの方は入れねぇからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#0000Fいえ、十分です。\x01",
            "ありがとうございます！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "いいってことよ。\x01",
            "そんじゃ、狼のことは任せたぜ。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 1)

    def lambda_D94():

        label("loc_D94")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_D94")

    QueueWorkItem2(0x101, 1, lambda_D94)

    def lambda_DA6():

        label("loc_DA6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_DA6")

    QueueWorkItem2(0x102, 1, lambda_DA6)

    def lambda_DB8():

        label("loc_DB8")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_DB8")

    QueueWorkItem2(0x103, 1, lambda_DB8)

    def lambda_DCA():

        label("loc_DCA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_DCA")

    QueueWorkItem2(0x104, 1, lambda_DCA)
    Sleep(6000)

    def lambda_DDF():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DDF)

    def lambda_DEC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DEC)

    def lambda_DF9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DF9)

    def lambda_E06():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E06)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0033
    ChrTalk(
        0x103,
        (
            "#0200F何はともあれ、これで\x01",
            "鉱山を使うことができますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#0000Fああ、作戦を開始する前に\x01",
            "十分に鍛えておこう。\x02",
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

    def Function_6_F48(): pass

    label("Function_6_F48")

    TalkBegin(0xFF)
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_6_F48 end

    def Function_7_F72(): pass

    label("Function_7_F72")

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

    def lambda_11F6():
        OP_97(0xFE, 0x1964, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11F6)

    def lambda_1210():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1210)
    Sleep(800)

    def lambda_1224():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1224)

    def lambda_123E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_123E)
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

    def lambda_1288():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1288)
    Sleep(300)

    def lambda_12A5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12A5)
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
            "#11Pヒック……\x01",
            "ちょいと飲みすぎちまったか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(300)

    #C0037
    ChrTalk(
        0x9,
        "#5Pしかし遅くなっちゃったな。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "#5P町長に早めに帰るよう\x01",
            "言われたばかりなのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        "#11Pあーん、例の魔獣の話かよ？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xA,
        (
            "#11Pけっ、こちとらカジノを我慢して\x01",
            "毎日穴掘りばかりやってんだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xA,
        (
            "#11Pせめて酒くらい\x01",
            "好きなように呑ませろってんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            "#5Pいつも週末には街に出て\x01",
            "カジノに入り浸ってるくせに……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "#5Pそれで全部スッてくるんだから\x01",
            "店にはいいお得意様だよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "#11Pう、うるせえ。\x01",
            "店に貯金してるだけだっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xA,
        (
            "#11P見てろよ～……\x01",
            "次はルーレットで大当たりを出して\x01",
            "今までの分を取り戻してやるからなぁ！\x02",
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
        "#11Pんー……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        "#5Pあれ、今の……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_15E7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15E7)
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
        "#5Pひっ……なんだぁ！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x9, 0xD, 500)

    #C0049
    ChrTalk(
        0x9,
        "#11Pま、まさか……例の狼！？\x02",
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
        "#5Pよ、よ、寄るなぁ……！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        "#11Pた、助けて……女神#4Rエイドス#様……！\x02",
    )

    CloseMessageWindow()

    #N0052
    NpcTalk(
        0x104,
        "青年の声",
        (
            "#4P──アンタら。\x01",
            "できれば目を塞いでな。\x02",
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
        "#11Pウォン！？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xC,
        "#11Pバウバウッ……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)

    #C0055
    ChrTalk(
        0xA,
        "#11Pうおっ……なんだ！？\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        "#5Pい、今のは……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    SetCameraDistance(21000, 1500)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_1A0C():
        OP_95(0xFE, 5960, 0, 50660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A0C)

    def lambda_1A26():
        OP_95(0xFE, 5990, 0, 43230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A26)

    def lambda_1A40():
        OP_95(0xFE, 7630, 0, 43280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A40)

    def lambda_1A5A():
        OP_95(0xFE, -790, 0, 44080, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A5A)
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
            "#0304F#1Pスタングレネードさ。\x02\x03",

            "#0302F訓練された犬っコロにも\x01",
            "少しは利くんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 500)
    Sleep(300)

    #C0058
    ChrTalk(
        0xA,
        "#11Pあ、あんたら……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    #C0059
    ChrTalk(
        0x9,
        "#5Pひ……昼間の？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0007F#2P話は後で！\x01",
            "宿に避難してください！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        "#5Pあ、ああ……！\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        "#11Pうう、何だってんだ！？\x02",
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
        "#11Pグルルル……\x02",
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
        "#5Pバウバウ！！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#0301F#1P意表はつけたが……\x01",
            "かなり手強そうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#0007Fよし……\x01",
            "このまま撃退するぞ！\x02",
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

    # Function_7_F72 end

    def Function_8_1D62(): pass

    label("Function_8_1D62")


    def lambda_1D67():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D67)
    WaitChrThread(0xA, 1)

    def lambda_1D84():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1D84)
    WaitChrThread(0xA, 2)
    Return()

    # Function_8_1D62 end

    def Function_9_1D9E(): pass

    label("Function_9_1D9E")


    def lambda_1DA3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1DA3)
    WaitChrThread(0x9, 1)
    Return()

    # Function_9_1D9E end

    def Function_10_1DBC(): pass

    label("Function_10_1DBC")

    OP_82(0x0, 0x12C, 0x1770, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    SetCameraDistance(19580, 150)
    OP_6F(0x79)
    CancelBlur(1000)
    SetCameraDistance(17580, 1000)
    OP_6F(0x79)
    Return()

    # Function_10_1DBC end

    def Function_11_1DFB(): pass

    label("Function_11_1DFB")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1E17():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E17)
    Return()

    # Function_11_1DFB end

    def Function_12_1E2C(): pass

    label("Function_12_1E2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E47")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_12_1E2C")

    label("loc_1E47")

    Return()

    # Function_12_1E2C end

    def Function_13_1E48(): pass

    label("Function_13_1E48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E66")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_13_1E48")

    label("loc_1E66")

    Return()

    # Function_13_1E48 end

    def Function_14_1E67(): pass

    label("Function_14_1E67")

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

    # Function_14_1E67 end

    def Function_15_1EAD(): pass

    label("Function_15_1EAD")

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

    # Function_15_1EAD end

    def Function_16_1EFF(): pass

    label("Function_16_1EFF")

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

    # Function_16_1EFF end

    def Function_17_1F51(): pass

    label("Function_17_1F51")

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

    # Function_17_1F51 end

    def Function_18_1FA3(): pass

    label("Function_18_1FA3")

    OP_93(0xFE, 0x13B, 0x1F4)
    OP_95(0xFE, 1190, 0, 49990, 4000, 0x0)
    OP_95(0xFE, 860, 0, 54460, 4000, 0x0)

    def lambda_1FD7():
        OP_95(0xFE, -1950, 440, 54350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1FD7)
    Sleep(500)

    def lambda_1FF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1FF4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_1FA3 end

    def Function_19_2009(): pass

    label("Function_19_2009")

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

    # Function_19_2009 end

    def Function_20_204C(): pass

    label("Function_20_204C")

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
            "#0003F#2Pふう……\x01",
            "さすがに手強かったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#0101F#4Pこうして見ると……\x01",
            "狼というよりは犬みたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        (
            "#0201F#2Pやはり訓練された\x01",
            "軍用犬でしょうか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1350, 150, 47770, 3000)
    OP_6F(0x1)

    def lambda_22CA():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_22CA)
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
        "軍用犬",
        "……グルルル………\x02",
    )

    CloseMessageWindow()

    def lambda_2328():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2328)

    def lambda_2341():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2341)
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
        "軍用犬",
        "#5Pバウ……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 1, 0, 21)
    SetChrChipByIndex(0xC, 0x29)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xC, 0xE1, 0x1F4)
    OP_63(0xC, 0xFFFFFC7C, 1900, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0xC, 0, 0, 12)

    def lambda_23E3():
        OP_95(0xFE, 140, 0, 38070, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_23E3)
    Sleep(750)
    SetChrChipByIndex(0xD, 0x29)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xD, 0xE1, 0x1F4)
    OP_63(0xD, 0xFFFFFC7C, 1900, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0xD, 0, 0, 12)

    def lambda_2432():
        OP_95(0xFE, 140, 0, 38070, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2432)
    Sleep(750)
    SetChrChipByIndex(0xB, 0x29)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xB, 0xE1, 0x1F4)
    OP_63(0xB, 0xFFFFFC7C, 1900, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0xB, 0, 0, 12)

    def lambda_2481():
        OP_95(0xFE, 140, 0, 38070, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2481)
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
        "#0205Fあ……！\x02",
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
            "#0301F#2Pちっ……\x01",
            "まだ余力があんのかよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#0007F問題ない！\x01",
            "このまま追いかけるぞ！\x02\x03",

            "多分、逃げていった先に\x01",
            "マフィアたちがいるはずだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        "#0107F#4Pええ……！\x02",
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

    def lambda_2616():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2616)

    def lambda_262B():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_262B)

    def lambda_2640():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2640)

    def lambda_2655():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2655)
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

    # Function_20_204C end

    def Function_21_26BA(): pass

    label("Function_21_26BA")

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

    # Function_21_26BA end

    def Function_22_2712(): pass

    label("Function_22_2712")

    EventBegin(0x1)

    #C0076
    ChrTalk(
        0x101,
        (
            "#0001Fもう日が暮れたな……\x02\x03",

            "#0003F深夜には町に襲撃があるはずだ。\x01",
            "街道に出るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 650, -2000, -4920, 0)
    EventEnd(0x4)
    Return()

    # Function_22_2712 end

    SaveToFile()

Try(main)
