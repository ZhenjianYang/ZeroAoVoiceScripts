from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1100.bin",                # FileName
        "t1100",                    # MapName
        "t1100",                    # Location
        0x0046,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 70, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1100",                  # 0
        "黒服",                   # 1
        "黒服",                   # 2
        "黒服",                   # 3
        "黒服",                   # 4
        "ガルシア",               # 5
        "ホテル・デルフィニア方面",# 6
    ))

    AddCharChip((
        "chr/ch36000.itc",                   # 00
        "chr/ch36100.itc",                   # 01
    ))

    DeclNpc(-2299,   0,       18149,   180,  453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(2299,    0,       18149,   180,  453,  0x0, 0,   1,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  0.0,                   0.0,                   -1.0,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -0.0,                  0.19999998807907104,   1.0])

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "ホテル・デルフィニア方面")

    ScpFunction((
        "Function_0_1CC",          # 00, 0
        "Function_1_284",          # 01, 1
        "Function_2_2B3",          # 02, 2
        "Function_3_349",          # 03, 3
        "Function_4_12A0",         # 04, 4
        "Function_5_12DE",         # 05, 5
        "Function_6_1323",         # 06, 6
        "Function_7_1368",         # 07, 7
        "Function_8_137E",         # 08, 8
        "Function_9_1394",         # 09, 9
        "Function_10_13AA",        # 0A, 10
        "Function_11_13C0",        # 0B, 11
    ))


    def Function_0_1CC(): pass

    label("Function_0_1CC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_20C"),
        (1, "loc_218"),
        (2, "loc_224"),
        (3, "loc_230"),
        (4, "loc_23C"),
        (5, "loc_248"),
        (6, "loc_254"),
        (SWITCH_DEFAULT, "loc_260"),
    )


    label("loc_20C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_218")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_224")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_230")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_23C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_248")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_254")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_260")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_26C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_283")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_283")

    Return()

    # Function_0_1CC end

    def Function_1_284(): pass

    label("Function_1_284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_295")
    Event(0, 3)

    label("loc_295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_END)), "loc_2B2")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)

    label("loc_2B2")

    Return()

    # Function_1_284 end

    def Function_2_2B3(): pass

    label("Function_2_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F3")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "t1100_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1100_sky_y", 0x1, 0x1)
    Jump("loc_317")

    label("loc_2F3")

    SetMapObjFrame(0xFF, "t1100_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1100_sky_y", 0x0, 0x1)

    label("loc_317")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_342")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_342")

    Sound(126, 1, 80, 0)
    Return()

    # Function_2_2B3 end

    def Function_3_349(): pass

    label("Function_3_349")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch36000.itc", 0x1E)
    LoadChrToIndex("chr/ch36100.itc", 0x1F)
    LoadChrToIndex("chr/ch02200.itc", 0x20)
    OP_68(0, 1600, -23850, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19210, 0)
    SetChrPos(0x101, 0, 0, -21970, 0)
    SetChrPos(0x102, -780, 0, -22750, 0)
    SetChrPos(0x103, 850, 0, -23240, 0)
    SetChrPos(0x104, 180, 0, -24710, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1600, -22350, 1700)
    Sleep(1500)
    OP_0D()
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

    #C0001
    ChrTalk(
        0x101,
        "#0013F#5Pあ……！\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        "#0301F#11Pアレか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(3790, 500, 33620, 0)
    MoveCamera(26, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(80770, 0)
    PlaceName2(340, 200, "c_plac21", 0x0, 3000)
    MoveCamera(37, 23, 0, 8000)
    OP_6F(0x40)
    Sleep(500)
    Fade(500)
    OP_68(0, 1600, -22350, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19210, 0)
    OP_0D()
    Sleep(500)

    #C0003
    ChrTalk(
        0x101,
        (
            "#0001F#5Pあれがハルトマン議長邸……\x02\x03",

            "#0003Fすごいな……\x01",
            "屋敷というより城みたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#0103F#5Pまあ、クロスベルでは\x01",
            "昔からの名士の家系だから……\x02\x03",

            "#0100Fあの屋敷も、百年近く前、\x01",
            "帝国の統治時代の総督邸として\x01",
            "建てられたものだと聞いているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#0306F#11Pそれにしたってデカすぎだろ。\x02\x03",

            "#0301F帝国の大貴族じゃねえんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        (
            "#0203F#11Pあんな場所を使って\x01",
            "開かれるという《競売会》……\x02\x03",

            "#0200F相当、大規模なものみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0008F#5Pああ──\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0008
    ChrTalk(
        0x101,
        "#0013F#5Pあれは……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1500, 26500, 0)
    MoveCamera(36, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20210, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1500, 25000, 5000)
    SetChrPos(0xC, -10, 800, 29110, 0)
    SetChrPos(0xA, -10, 800, 29110, 0)
    SetChrPos(0xB, -10, 800, 29110, 0)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 3, 0, 5)
    Sleep(1000)
    BeginChrThread(0xB, 3, 0, 6)
    Sleep(1000)
    BeginChrThread(0xC, 3, 0, 4)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis064.itp")

    #C0009
    ChrTalk(
        0xC,
        (
            "#3103F#5P──警備の手筈は例年通りだ。\x02\x03",

            "#3101Fだが、今年は《黒月》どもが\x01",
            "仕掛けてくる可能性も考えられる。\x02\x03",

            "招待カードを持ったヤツ以外は\x01",
            "誰であろうと通すんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        "#12P承知しました！\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xB,
        "#6P若頭の方はどうされます？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xC,
        (
            "#3104F#5P俺は屋敷内部の警戒に当たる。\x02\x03",

            "何しろ神出鬼没なヤツだ。\x01",
            "警戒しすぎる事はねえだろう。\x02\x03",

            "#3100F……そういえば、\x01",
            "出品物は全部搬入されたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        "#6Pええ、今朝方。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xB,
        "#6P例の人形が最後みたいですね。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xC,
        (
            "#3104F#5P今回の目玉の一つか……\x01",
            "どれだけの値が付くことやら。\x02\x03",

            "#3101Fまあいい、開場まであと数時間だ。\x02\x03",

            "くれぐれも気を抜くんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        "#6Pはい……！\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xA,
        "#12Pお疲れさまです！\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x1F4)

    def lambda_AF0():
        OP_95(0xFE, -10, 800, 29110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_AF0)
    Sleep(1200)

    def lambda_B0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B0D)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xC, 2)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    Sleep(500)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sleep(30)
    Sound(890, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Fade(1000)
    SetChrPos(0x101, -3000, 0, -28000, 0)
    SetChrPos(0x102, -3570, 0, -29080, 0)
    SetChrPos(0x103, -2930, 0, -30390, 0)
    SetChrPos(0x104, -2350, 0, -28980, 0)
    OP_68(-2890, 3000, -29150, 0)
    MoveCamera(351, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(15440, 0)
    OP_68(-2890, 1500, -29150, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0018
    ChrTalk(
        0x104,
        (
            "#0301F#6P──出やがったか。\x02\x03",

            "あのオッサンも早速、\x01",
            "中に詰めているらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#0201F#6Pたしかガルシアという\x01",
            "元猟兵の若頭さんでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        (
            "#0103F#6Pパーティの開場は\x01",
            "たしか夜の７時から……\x02\x03",

            "#0101Fもう警備を始めるみたいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0021
    ChrTalk(
        0x101,
        (
            "#0001F#5Pああ……\x01",
            "それだけ警戒してるんだろう。\x02\x03",

            "#0008F……しかし参ったな。\x02\x03",

            "いくら招待カードがあっても\x01",
            "簡単には中に入れなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#0306F#6Pまあ、俺たちも結構、\x01",
            "連中に面が割れちまってるしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0206F#6P何か手立てを講じる必要が\x01",
            "ありそうな感じですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#0003F#5P……………………………\x02\x03",

            "#0000F……とりあえず、\x01",
            "いったんここから離れよう。\x02\x03",

            "ここで連中に見つかったら\x01",
            "元も子もなくなりそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        "#0100F#6Pそうね……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_E7B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E7B)
    Sleep(100)

    def lambda_E8B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E8B)

    def lambda_E98():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E98)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_68(-2860, 1500, -32040, 3000)

    def lambda_EDE():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EDE)
    Sleep(200)

    def lambda_EF6():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EF6)
    Sleep(200)

    def lambda_F0E():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F0E)
    Sleep(400)

    def lambda_F26():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F26)
    Sleep(1000)
    VolumeBGM(0x28, 0x1F4)
    FadeToDark(500, 0, -1)
    Sound(915, 0, 100, 0)
    OP_0D()
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x101, 0x1)
    OP_C7(0x0, 0x800)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(200)
    Sound(2179, 255, 65, 0)    #voice#KeA
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C7(0x1, 0x800)
    FadeToBright(500, 0)
    OP_68(-2860, 1500, -32040, 0)
    MoveCamera(351, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(17870, 0)
    BeginChrThread(0x103, 3, 0, 8)
    BeginChrThread(0x102, 3, 0, 9)
    BeginChrThread(0x104, 3, 0, 10)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0026
    ChrTalk(
        0x101,
        "#0005F#5Pえ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)

    def lambda_1036():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1036)
    Sleep(100)

    def lambda_1046():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1046)

    def lambda_1053():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1053)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Fade(1000)
    OP_68(7430, 7600, 6620, 0)
    MoveCamera(329, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(54410, 0)
    OP_68(2020, 7600, 3200, 8000)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(5, 250, -1, -1)

    #A0027
    AnonymousTalk(
        0x101,
        (
            "#0005F#5P#40W（…………今のは……………）\x02\x03",

            "#0001F#40W（………空耳……それとも………）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(1000)
    OP_68(-2860, 3000, -32040, 0)
    MoveCamera(351, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(17870, 0)
    OP_68(-2860, 1500, -32040, 4000)
    OP_6F(0x1)
    OP_0D()

    #C0028
    ChrTalk(
        0x103,
        "#0205F#6P#N……ロイドさん？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0029
    ChrTalk(
        0x102,
        "#0105F#6Pどうしたの？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#0008F#5Pいや……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0031
    ChrTalk(
        0x101,
        (
            "#0006F#5P──ゴメン。\x01",
            "気のせいだったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        "#0100F#6P？？？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#0300F#12Pよく分からんが\x01",
            "とっとと行こうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        "#0200F#6P#N………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0xA4, 1)
    OP_29(0x47, 0x1, 0x2)
    EventEnd(0x5)
    NewScene("t1010", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_3_349 end

    def Function_4_12A0(): pass

    label("Function_4_12A0")


    def lambda_12A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12A5)
    OP_95(0xFE, -50, 800, 27060, 2000, 0x1)
    OP_95(0xFE, 0, 400, 25800, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_4_12A0 end

    def Function_5_12DE(): pass

    label("Function_5_12DE")


    def lambda_12E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12E3)
    OP_95(0xFE, -50, 800, 27060, 2000, 0x1)
    OP_95(0xFE, 700, 0, 23800, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_5_12DE end

    def Function_6_1323(): pass

    label("Function_6_1323")


    def lambda_1328():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1328)
    OP_95(0xFE, -50, 800, 27060, 2000, 0x1)
    OP_95(0xFE, -700, 0, 23800, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_6_1323 end

    def Function_7_1368(): pass

    label("Function_7_1368")


    def lambda_136D():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_136D)
    Return()

    # Function_7_1368 end

    def Function_8_137E(): pass

    label("Function_8_137E")


    def lambda_1383():
        OP_9B(0x0, 0xFE, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1383)
    Return()

    # Function_8_137E end

    def Function_9_1394(): pass

    label("Function_9_1394")


    def lambda_1399():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1399)
    Return()

    # Function_9_1394 end

    def Function_10_13AA(): pass

    label("Function_10_13AA")


    def lambda_13AF():
        OP_9B(0x0, 0xFE, 0x0, 0x640, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13AF)
    Return()

    # Function_10_13AA end

    def Function_11_13C0(): pass

    label("Function_11_13C0")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1451")

    #C0035
    ChrTalk(
        0x101,
        (
            "#0001F今、ルバーチェの連中に\x01",
            "見つかるのは避けたいな。\x02\x03",

            "カードはあるけど\x01",
            "すんなり通してはくれなそうだし、\x01",
            "どうしたものか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1570")

    #C0036
    ChrTalk(
        0x151,
        (
            "#5705F……あれ、ブティックに\x01",
            "向かってたんじゃなかったのかい？\x02\x03",

            "#5702Fそのまま入って\x01",
            "マフィアの連中に見つかるのも\x01",
            "それはそれで楽しそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#0006Fい、いや……\x01",
            "それは遠慮しとくよ。\x02\x03",

            "#0001F連中の目をかいくぐる為にも\x01",
            "ブティックで正装してこよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15C2")

    label("loc_1570")


    #C0038
    ChrTalk(
        0x101,
        (
            "#0001Fここには見張りがいる……\x01",
            "会場に向かう前に\x01",
            "ブティックで正装してこよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C2")

    Sleep(50)
    SetChrPos(0x0, 0, 200, -1700, 180)
    EventEnd(0x4)
    OP_68(0, 1600, -1700, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    Return()

    # Function_11_13C0 end

    SaveToFile()

Try(main)
