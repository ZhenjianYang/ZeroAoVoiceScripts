from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0010.bin",                # FileName
        "e0010",                    # MapName
        "e0010",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e0010",                  # 0
        "運転手",                 # 1
        "乗客",                   # 2
        "乗客",                   # 3
        "乗客",                   # 4
        "黒髪の女性",             # 5
        "お婆さん",               # 6
        "老人",                   # 7
        "貿易商",                 # 8
        "女性",                   # 9
        "兄",                     # 10
        "妹",                     # 11
        "父親",                   # 12
        "男の子",                 # 13
        "SE制御",                 # 14
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_268",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_2B5",          # 02, 2
        "Function_3_A86",          # 03, 3
        "Function_4_AAB",          # 04, 4
        "Function_5_103A",         # 05, 5
        "Function_6_1390",         # 06, 6
        "Function_7_13C9",         # 07, 7
        "Function_8_1402",         # 08, 8
        "Function_9_143E",         # 09, 9
        "Function_10_147A",        # 0A, 10
        "Function_11_14C2",        # 0B, 11
        "Function_12_152D",        # 0C, 12
        "Function_13_158E",        # 0D, 13
        "Function_14_15D2",        # 0E, 14
        "Function_15_1698",        # 0F, 15
        "Function_16_33DC",        # 10, 16
        "Function_17_3420",        # 11, 17
        "Function_18_3464",        # 12, 18
    ))


    def Function_0_268(): pass

    label("Function_0_268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_27C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)
    Jump("loc_2B3")

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_290")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 4)
    Jump("loc_2B3")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_2A4")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 5)
    Jump("loc_2B3")

    label("loc_2A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_2B3")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 15)

    label("loc_2B3")

    Return()

    # Function_0_268 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    Return()

    # Function_1_2B4 end

    def Function_2_2B5(): pass

    label("Function_2_2B5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50119.itc", 0x22)
    LoadChrToIndex("chr/ch20402.itc", 0x23)
    LoadChrToIndex("chr/ch20302.itc", 0x24)
    LoadChrToIndex("chr/ch22302.itc", 0x25)
    SoundLoad(468)
    OP_68(46910, 1100, -180, 0)
    MoveCamera(328, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16350, 0)
    OP_68(52300, 1100, -180, 10000)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x25)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0x101, 52250, 0, 800, 0)
    SetChrPos(0x102, 55000, 150, 200, 270)
    SetChrPos(0x103, 55000, 150, 1450, 270)
    SetChrPos(0x104, 53300, 150, 1700, 180)
    SetChrPos(0x8, 43870, -200, 1800, 270)
    SetChrPos(0x9, 46150, 150, -1840, 270)
    SetChrPos(0xA, 48050, 150, 1880, 270)
    SetChrPos(0xB, 48050, 150, 880, 270)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Sound(468, 2, 100, 0)
    BeginChrThread(0x101, 3, 0, 3)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0001
    ChrTalk(
        0x101,
        "#0000F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        "#0100F#6P綺麗な夕暮れね……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        (
            "#0203F#4Pはい……\x01",
            "何だか目に痛いくらいです。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    #C0004
    ChrTalk(
        0x104,
        (
            "#0304F#11Pは～、しかし導力車ってのは\x01",
            "ずいぶんと楽チンだよなぁ。\x02\x03",

            "#0300F支援課#6Rウ  チ#でも専用の車が\x01",
            "使えりゃ良かったんだが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0005
    ChrTalk(
        0x101,
        (
            "#0006F#6Pまあ、無理だろうな。\x02\x03",

            "#0000F他の捜査課では車が\x01",
            "使われているみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)

    #C0006
    ChrTalk(
        0x103,
        (
            "#0200F#4P……確か捜査一課では、\x01",
            "捜査員一人一人に専用車が\x01",
            "用意されているはずです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0007
    ChrTalk(
        0x101,
        "#0005F#5Pそ、そうなのか！？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0106F#6Pそれはさすがに\x01",
            "優遇しすぎだと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#0306F#5Pやれやれ……\x01",
            "こういう時に日陰者は辛いねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#0006F#5Pまあ、無いものねだりを\x01",
            "したって仕方ないし……\x02\x03",

            "#0000Fそれに街道を歩くのだって\x01",
            "結構な鍛錬にはなると思うぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        (
            "#0203F#4P不本意ですが……\x01",
            "そうかもしれませんね。\x02\x03",

            "#0211Fでも、さすがに今日は\x01",
            "これ以上の調査はしませんよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#0003F#5Pああ、残りは北の鉱山町だ。\x02\x03",

            "#0000Fさっきも言ったように、\x01",
            "今日は帰ったら調書をまとめて\x01",
            "明日、改めて訪ねてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        "#0206F#4Pふう……了解です。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        (
            "#0109F#6Pふふ……\x01",
            "流石に疲れたものね、今日は。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sleep(200)
    OP_63(0x104, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    #C0015
    ChrTalk(
        0x104,
        (
            "#0309F#11Pうーん……\x01",
            "でもセシルさん、良かったなぁ。\x02\x03",

            "#0307Fよし、今度は合コンにかこつけて\x01",
            "個人的にお近づきを……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0016
    ChrTalk(
        0x101,
        "#0006F#6Pランディは元気だなぁ……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    BeginChrThread(0x15, 0, 0, 16)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    WaitChrThread(0x15, 0)
    OP_24(0x1D4)
    SetScenarioFlags(0x5C, 0)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_2B5 end

    def Function_3_A86(): pass

    label("Function_3_A86")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AAA")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_3_A86")

    label("loc_AAA")

    Return()

    # Function_3_A86 end

    def Function_4_AAB(): pass

    label("Function_4_AAB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch21102.itc", 0x22)
    LoadChrToIndex("chr/ch21602.itc", 0x23)
    LoadChrToIndex("apl/ch50382.itc", 0x24)
    SoundLoad(468)
    OP_68(147980, 1000, 1450, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16170, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B35")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_B5C")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B4B")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_B5C")

    label("loc_B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B5C")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_B5C")

    SetChrFlags(0xEF, 0x4)
    SetChrFlags(0x153, 0x2)
    SetChrFlags(0x153, 0x10)
    SetChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x153, 0x24)
    SetChrSubChip(0x153, 0x0)
    SetChrPos(0x101, 148050, 150, 1800, 180)
    SetChrPos(0x153, 147350, 350, 1800, 0)
    SetChrPos(0xEF, 146600, 150, 1800, 180)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 145000, 150, 790, 90)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 145000, 150, -100, 90)
    SetMapObjFrame(0xFF, "bg00_y", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    BeginChrThread(0x101, 3, 0, 3)
    FadeToBright(1000, 0)
    OP_68(146980, 1000, 1450, 3000)
    OP_0D()
    OP_6F(0x1)
    Sound(2033, 255, 100, 0)    #voice#KeA
    Sleep(1800)
    SetChrSubChip(0x153, 0x1)
    Sleep(300)

    #C0017
    ChrTalk(
        0x153,
        (
            "#1109F#5Pねえねえロイド！\x01",
            "すっごくキレイだね～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0xEF, 0x1)
    Sleep(200)

    #C0018
    ChrTalk(
        0x101,
        "#0011F#11Pちょ、声が大きいって……！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xEF, 0x0)
    Sleep(100)
    SetChrSubChip(0xEF, 0x2)
    Sleep(200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_D0D")

    #C0019
    ChrTalk(
        0x102,
        (
            "#0106F#11Pす、すみません……\x01",
            "うるさくしてしまって。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D90")

    label("loc_D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_D52")

    #C0020
    ChrTalk(
        0x103,
        (
            "#0206F#11P……すみません。\x01",
            "うるさくしてしまって。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D90")

    label("loc_D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_D90")

    #C0021
    ChrTalk(
        0x104,
        (
            "#0306F#11P申し訳ないッス。\x01",
            "うるさくしちまって。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D90")


    #C0022
    ChrTalk(
        0x9,
        (
            "#5Pふふ、いいのよ。\x01",
            "子供は元気なのが一番だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xA,
        (
            "#1Pふぉふぉ、どなたかの\x01",
            "お見舞いにでも行くのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#0000F#11Pいえ、ちょっと病院の先生に\x01",
            "相談することがありまして……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x153, 0x0)

    #C0025
    ChrTalk(
        0x153,
        (
            "#1107F#5Pねえねえ、あっちに\x01",
            "ちっちゃい島が見えるよ～！\x02\x03",

            "#1109Fヘンな形してて面白いね～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xEF, 0x0)
    Sleep(100)
    SetChrSubChip(0xEF, 0x1)

    #C0026
    ChrTalk(
        0x101,
        "#0012F#12Pやれやれ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_F4A")

    #C0027
    ChrTalk(
        0x102,
        (
            "#0102F#6Pふふ……\x01",
            "大好評みたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB9")

    label("loc_F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_F84")

    #C0028
    ChrTalk(
        0x103,
        (
            "#0202F#6Pくす……\x01",
            "大好評みたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB9")

    label("loc_F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_FB9")

    #C0029
    ChrTalk(
        0x104,
        (
            "#0309F#6Pははっ……\x01",
            "大好評みてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB9")

    SetCameraDistance(15670, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    ClearChrFlags(0x153, 0x4)
    ClearChrFlags(0x153, 0x2)
    ClearChrFlags(0x153, 0x10)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    BeginChrThread(0x15, 0, 0, 16)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x15, 0)
    OP_24(0x1D4)
    SetScenarioFlags(0x5C, 1)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_AAB end

    def Function_5_103A(): pass

    label("Function_5_103A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 2600, -500, -450, 270)
    SetChrPos(0x102, 2600, -500, 450, 270)
    SetChrPos(0x103, 3700, -500, 450, 270)
    SetChrPos(0x104, 3700, -500, -450, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(900, 900, 0, 0)
    MoveCamera(270, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17800, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFrame(0xFF, "bg00_y", 0x2, "stop")
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_68(400, 900, 0, 2500)
    BeginChrThread(0x101, 3, 0, 6)
    BeginChrThread(0x102, 3, 0, 7)
    BeginChrThread(0x103, 3, 0, 8)
    BeginChrThread(0x104, 3, 0, 9)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(0, 900, 0, 0)
    OP_68(0, 900, -2500, 4000)
    MoveCamera(320, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17800, 0)
    Sleep(1500)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 11)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 12)
    Sleep(150)
    BeginChrThread(0x103, 3, 0, 13)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_68(0, 500, 500, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17800, 0)
    SetChrPos(0x101, 600, 0, -4800, 0)
    SetChrPos(0x102, 800, 0, 2300, 0)
    SetChrPos(0x103, 0, 0, 3700, 0)
    SetChrPos(0x104, -800, 0, 2600, 0)
    OP_68(0, 500, 4500, 6000)

    def lambda_126E():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_126E)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    OP_0D()

    #C0030
    ChrTalk(
        0x101,
        (
            "#0008F#6P花や見舞いの品が\x01",
            "座席に残っている……\x02\x03",

            "#0013Fどうやら病院に行く\x01",
            "途中だったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        "#0106F#6Pええ……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        (
            "#0208F#6Pぬいぐるみ……\x01",
            "子供の患者さんへの\x01",
            "お見舞い品でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        "#0306F#6Pああ……そうだろうな。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(17200, 2500)
    OP_6F(0x79)
    OP_0D()
    SetScenarioFlags(0x5C, 2)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_103A end

    def Function_6_1390(): pass

    label("Function_6_1390")


    def lambda_1395():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1395)

    def lambda_13AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13AA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_6_1390 end

    def Function_7_13C9(): pass

    label("Function_7_13C9")


    def lambda_13CE():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13CE)

    def lambda_13E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13E3)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_7_13C9 end

    def Function_8_1402(): pass

    label("Function_8_1402")


    def lambda_1407():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1407)
    Sleep(500)

    def lambda_141F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_141F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x12C)
    Return()

    # Function_8_1402 end

    def Function_9_143E(): pass

    label("Function_9_143E")


    def lambda_1443():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1443)
    Sleep(500)

    def lambda_145B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_145B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_9_143E end

    def Function_10_147A(): pass

    label("Function_10_147A")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_1486():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1486)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_14A6():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14A6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_147A end

    def Function_11_14C2(): pass

    label("Function_11_14C2")

    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_14D1():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14D1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_14F1():
        OP_9B(0x0, 0xFE, 0x0, 0x898, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14F1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_1511():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1511)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_14C2 end

    def Function_12_152D(): pass

    label("Function_12_152D")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_1539():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1539)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_1559():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1559)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_1579():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1579)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_152D end

    def Function_13_158E(): pass

    label("Function_13_158E")

    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_159D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_159D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_15BD():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_15BD)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_158E end

    def Function_14_15D2(): pass

    label("Function_14_15D2")

    EventBegin(0x0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【老人】\x01",            # 0
            "【お婆さん】\x01",        # 1
            "【黒髪の女性】\x01",      # 2
            "【若い女性】\x01",        # 3
            "【貿易商】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1645"),
        (1, "loc_1653"),
        (2, "loc_1661"),
        (3, "loc_166F"),
        (4, "loc_167D"),
        (SWITCH_DEFAULT, "loc_168B"),
    )


    label("loc_1645")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0xE)
    Jump("loc_168B")

    label("loc_1653")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0xF)
    Jump("loc_168B")

    label("loc_1661")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0x10)
    Jump("loc_168B")

    label("loc_166F")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0x11)
    Jump("loc_168B")

    label("loc_167D")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0x12)
    Jump("loc_168B")

    label("loc_168B")

    SetScenarioFlags(0x5C, 0)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_15D2 end

    def Function_15_1698(): pass

    label("Function_15_1698")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50119.itc", 0x22)
    LoadChrToIndex("chr/ch07302.itc", 0x23)
    LoadChrToIndex("chr/ch24102.itc", 0x24)
    LoadChrToIndex("chr/ch20802.itc", 0x25)
    LoadChrToIndex("chr/ch33000.itc", 0x26)
    LoadChrToIndex("chr/ch24500.itc", 0x27)
    LoadChrToIndex("chr/ch21202.itc", 0x28)
    LoadChrToIndex("chr/ch21302.itc", 0x29)
    LoadChrToIndex("chr/ch21002.itc", 0x2A)
    LoadChrToIndex("chr/ch21402.itc", 0x2B)
    SoundLoad(474)
    OP_68(47090, 1100, -430, 0)
    MoveCamera(328, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23180, 0)
    OP_68(51930, 1100, 120, 8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x28)
    SetChrSubChip(0x11, 0x2)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x1)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x2A)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x2B)
    SetChrSubChip(0x14, 0x2)
    SetChrPos(0x101, 52250, 150, 1700, 180)
    SetChrPos(0x102, 55000, 150, 200, 270)
    SetChrPos(0x103, 55000, 150, 1450, 270)
    SetChrPos(0x104, 53300, 150, 1700, 180)
    SetChrPos(0x8, 43870, -200, 1800, 270)
    SetChrPos(0xC, 48000, 150, -2000, 270)
    SetChrPos(0xD, 44000, 150, -2000, 270)
    SetChrPos(0xE, 46000, 150, -2000, 270)
    SetChrPos(0xF, 50270, -250, -2029, 225)
    SetChrPos(0x10, 49540, -250, 1520, 270)
    SetChrPos(0x11, 48000, 150, 600, 270)
    SetChrPos(0x12, 48000, 150, 1600, 270)
    SetChrPos(0x13, 46000, 150, 600, 270)
    SetChrPos(0x14, 46000, 150, 1600, 270)
    SetMapObjFrame(0xFF, "bg00_y", 0x0, 0x1)
    PlayBGM("ed7516", 0)
    Sound(474, 2, 0, 0)
    BeginChrThread(0x15, 0, 0, 17)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x15, 0x0)

    #C0034
    ChrTalk(
        0x101,
        (
            "#5P#0001F（まずは……\x01",
            "　偽ブランド業者の\x01",
            "　情報を整理しよう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#12P#0203F（偽ブランド業者たちは\x01",
            "　駅、空港、そしてタングラム門に\x01",
            "　ルートを分けて来ている……）\x02\x03",

            "#0200F（警察本部に寄せられた情報だと、\x01",
            "　確かそういうことでしたね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#5P#0000F（ああ、その通り。）\x02\x03",

            "#0003F（そして、情報が確かなら、\x01",
            "　容疑者はこのバスの乗客の\x01",
            "　誰かということになる。）\x02\x03",

            "（そして……\x01",
            "　これだけの情報があれば、\x01",
            "　ある一つの事実が浮かぶ。）\x02\x03",

            "#0001F（おそらく、このバスに乗っている\x01",
            "　偽ブランド業者は……）\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【単独行動している】\x01",          # 0
            "【二人組で行動している】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B82"),
        (1, "loc_20E8"),
        (SWITCH_DEFAULT, "loc_2871"),
    )


    label("loc_1B82")

    OP_60(0x0)
    OP_2C(0x1B, 0x1)

    #C0037
    ChrTalk(
        0x101,
        (
            "#5P#0001F（……単独行動をしている。）\x02\x03",

            "#0003F（それも、偽ブランド業者のグループでも\x01",
            "　リーダー的な存在のはずだ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        (
            "#11P#0305F（おいおい、マジかよ……\x01",
            "　リーダー格がたった一人で\x01",
            "　行動してるってのか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#12P#0105F（考えられなくもないけど……\x01",
            "　その根拠はどこにあるの？）\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#5P#0004F（簡単な話さ。）\x02\x03",

            "（奴らは商売をするために、\x01",
            "　クロスベルに偽物の商品を\x01",
            "　運び込まなければならない。）\x02\x03",

            "#0000F（そのルートとして使うには、\x01",
            "　バス移動のタングラム門は不適切だ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#12P#0203F（確かに……そうですね。）\x02\x03",

            "#0200F（わたしが偽ブランド業者だったら、\x01",
            "　おそらく、駅と空港でクロスベル入りする\x01",
            "　仲間たちに運び屋をさせます。）\x02\x03",

            "（国境門と違って、駅や空港では\x01",
            "　共和国・帝国からの入国時に\x01",
            "　厳密なチェックはありませんから。）\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#11P#0303F（加えて、荷物運びなんて危ない橋、\x01",
            "　下っ端に渡らせるのが定石だ。）\x02\x03",

            "（消去法でいけば……\x01",
            "　駅か空港のルートで\x01",
            "　手下どもにブツを運ばせて……）\x02\x03",

            "#0301F（リーダーは少ない荷物だけ持って、\x01",
            "　怪しまれる危険もなく悠々と\x01",
            "　クロスベルに向かってるってことか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#5P#0000F（そういうこと。）\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#12P#0103F（状況証拠ではあるけど……\x01",
            "　説得力はあるわね。）\x02\x03",

            "#0101F（そうなると、二人組である\x01",
            "　兄妹と親子連れの旅行者は\x01",
            "　容疑者から外れることになる。）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#5P#0001F（……ああ、そして……）\x02\x03",

            "#0003F（さっきの乗客と話しているとき……\x01",
            "　気になることを言っていた人がいた。）\x02\x03",

            "（恐らく、その人物が\x01",
            "　偽ブランド業者のリーダーだ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2871")

    label("loc_20E8")

    OP_60(0x0)

    #C0046
    ChrTalk(
        0x101,
        (
            "#5P#0003F（……二人組で行動をしている。）\x02\x03",

            "#0001F（多分、偽ブランド業者のグループでは\x01",
            "　運び屋的な存在のはずだ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        "#11P#0305F（……二人組の運び屋！？）\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#5P#0001F（奴らは商売をするために、\x01",
            "　クロスベルに偽ブランド商品を\x01",
            "　運び込まなければならない。）\x02\x03",

            "#0003F（単独で荷物を持ち込むのは\x01",
            "　かなり厳しいと見ていいだろう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#11P#0305F（ってことは……\x01",
            "　あの兄妹の旅行者か、\x01",
            "　親子連れになるのか？）\x02\x03",

            "#0306F（そりゃあ……いくらなんでも\x01",
            "　意表を突かれたぜ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        "#12P#0200F（……本当にそうなのでしょうか。）\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#5P#0005F（……へっ？）\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        (
            "#12P#0203F（もしわたしが偽ブランド業者だったら……\x01",
            "　おそらく、駅と空港でクロスベル入りする\x01",
            "　仲間たちに運び屋をさせます。）\x02\x03",

            "#0200F（国境門と違って、駅や空港では\x01",
            "　共和国・帝国からの入国時に\x01",
            "　厳密なチェックはありませんから。）\x02\x03",

            "（ですから、タングラム門は\x01",
            "　荷物を運び入れるルートとして\x01",
            "　不適切なはずです。）\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#12P#0103F（確かに……）\x02\x03",

            "#0101F（そうなると、恐らく\x01",
            "　このバスに乗っている業者は……\x01",
            "　単独行動をしている可能性が高いわ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        "#5P#0005F単独行動……！？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        (
            "#12P#0101F（ええ、それも……\x01",
            "　偽ブランド業者のグループでも\x01",
            "　リーダー的な存在のはずよ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#11P#0305F（……そうか……）\x02\x03",

            "#0303F（荷物運びなんて危ない橋、\x01",
            "　下っ端に渡らせるのが定石だ。）\x02\x03",

            "（消去法でいけば……\x01",
            "　駅か空港のルートで\x01",
            "　手下どもにブツを運ばせて……）\x02\x03",

            "#0301F（リーダーは少ない荷物だけ持って、\x01",
            "　怪しまれる危険もなく悠々と\x01",
            "　クロスベルに向かってるってことか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#5P#0005F（そういうことか……）\x02\x03",

            "#0006F（ありがとう、みんな。\x01",
            "　考えが足りなかったみたいだ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#12P#0100F（ふふ、いいのよ。\x01",
            "　あなただけに任せきりにしていては\x01",
            "　私たちも成長できないし。）\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        "#12P#0200F（いつまでもおいしい所は渡しません。）\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        "#11P#0309F（はは、だな。）\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#5P#0001F（でも、そうすると……\x01",
            "　１人だけ、怪しい人物が\x01",
            "　浮かび上がるな。）\x02\x03",

            "#0003F（さっきの乗客と話しているとき……\x01",
            "　気になることを言っていた人がいた。）\x02\x03",

            "#0001F（恐らく、その人物が\x01",
            "　偽ブランド業者のリーダーだ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2871")

    label("loc_2871")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0062
    ChrTalk(
        0x104,
        "#11P#0301F（さっき言ってたヤツのことか……）\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        "#12P#0203F（……残る容疑者は５名です。）\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(45920, 1100, -1670, 0)
    MoveCamera(358, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(18520, 0)
    OP_0D()
    SetMessageWindowPos(350, 0, -1, -1)

    #A0064
    AnonymousTalk(
        0x103,
        (
            "#0200F\x09",
            "（①クロスベルに釣りをしにきたという\x01",
            "  　偏屈な老人。）\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(43880, 1100, -1880, 0)
    MoveCamera(358, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(18520, 0)
    OP_0D()

    #A0065
    AnonymousTalk(
        0x103,
        (
            "#0200F（②３年ぶりに孫に会いにきたという\x01",
            "  　優しそうなお婆さん。）\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(48010, 1100, -1960, 0)
    MoveCamera(52, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(17640, 0)
    OP_0D()

    #A0066
    AnonymousTalk(
        0x103,
        (
            "#0200F（③普通ではない雰囲気を感じさせる\x01",
            "  　黒髪の女性。）\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(49460, 1100, 1460, 0)
    MoveCamera(335, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(18520, 0)
    OP_0D()

    #A0067
    AnonymousTalk(
        0x103,
        (
            "#0200F（④その女性を疑り深く見ていた\x01",
            "  　若い女性。）\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(50240, 1100, -1870, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(19450, 0)
    OP_0D()

    #A0068
    AnonymousTalk(
        0x103,
        (
            "#0200F（⑤そして、クロスベルと共和国を\x01",
            "  　行き来しているという貿易商……）\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(51930, 1100, 120, 0)
    MoveCamera(328, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23180, 0)
    OP_0D()

    #C0069
    ChrTalk(
        0x102,
        "#12P#0105F（でも、本当にこの中に……？）\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#5P#0003F（……ああ、間違いない。）\x02\x03",

            "#0001F（その中にいる\x01",
            "　偽ブランド業者のリーダーは……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3327")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【老人】\x01",            # 0
            "【お婆さん】\x01",        # 1
            "【黒髪の女性】\x01",      # 2
            "【若い女性】\x01",        # 3
            "【貿易商】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C99"),
        (1, "loc_2CCC"),
        (2, "loc_2CFF"),
        (3, "loc_2D2E"),
        (4, "loc_2D61"),
        (SWITCH_DEFAULT, "loc_2D96"),
    )


    label("loc_2C99")

    OP_60(0x0)

    #C0071
    ChrTalk(
        0x101,
        "#5P#0001F（……あの、老人だ。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xE)
    Jump("loc_2D96")

    label("loc_2CCC")

    OP_60(0x0)

    #C0072
    ChrTalk(
        0x101,
        "#5P#0001F（あの、お婆さんだ。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xF)
    Jump("loc_2D96")

    label("loc_2CFF")

    OP_60(0x0)

    #C0073
    ChrTalk(
        0x101,
        "#5P#0001F（黒髪の女性だ。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x10)
    Jump("loc_2D96")

    label("loc_2D2E")

    OP_60(0x0)

    #C0074
    ChrTalk(
        0x101,
        "#5P#0001F（あの、若い女性だ。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x11)
    Jump("loc_2D96")

    label("loc_2D61")

    OP_60(0x0)

    #C0075
    ChrTalk(
        0x101,
        "#5P#0001F（あの、貿易商の人だ。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x12)
    Jump("loc_2D96")

    label("loc_2D96")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0076
    ChrTalk(
        0x104,
        "#11P#0301F（……間違いないんだな？）\x02",
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【間違いない】\x01",      # 0
            "【考え直す】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E08"),
        (1, "loc_3109"),
        (SWITCH_DEFAULT, "loc_3322"),
    )


    label("loc_2E08")

    OP_60(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xF)"), scpexpr(EXPR_END)), "loc_2E1D")
    OP_2C(0x1B, 0x2)

    label("loc_2E1D")


    #C0077
    ChrTalk(
        0x101,
        (
            "#5P#0001F（……ああ。\x01",
            "　偽ブランド業者のリーダーは、\x01",
            "　あの人以外に考えられない。）\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x102,
        "#12P#0105F（そう……なのね。）\x02",
    )

    CloseMessageWindow()
    Sound(801, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("アナウンス")

    #A0079
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──このバスは、まもなく\x01",
            "クロスベル市東口に到着します。\x02",
        )
    )

    CloseMessageWindow()

    #A0080
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "お降りの際は、\x01",
            "お忘れ物の無い様ご注意下さい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0081
    ChrTalk(
        0x103,
        "#12P#0200F（そろそろ着くようですね。）\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        "#12P#0101F（……本番ね。）\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#5P#0001F（到着したら、いよいよ\x01",
            "　容疑者の確保にかかる。）\x02\x03",

            "（みんな、気を引き締めていてくれ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        (
            "#11P#0304F（言われなくても分かってるぜ。）\x02\x03",

            "#0300F（まずはロイド、\x01",
            "　お前が容疑者のツラの皮を\x01",
            "　引っぺがしてやれ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#5P#0001F（ああ、任せてくれ……！）\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    OP_68(47810, 1100, -1860, 0)
    MoveCamera(44, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(18710, 0)
    OP_0D()
    SetCameraDistance(17710, 2000)
    OP_6F(0x10)

    #C0086
    ChrTalk(
        0xC,
        "#11P#3403F………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3322")

    label("loc_3109")

    OP_60(0x0)

    #C0087
    ChrTalk(
        0x101,
        (
            "#5P#0003F（……そう言われると、\x01",
            "　ちょっと自信がないかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        "#11P#0306F（ガクッ……なんだそりゃ！）\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        "#12P#0106F（はぁ……しっかりしてよ。）\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#5P#0011F（ご、ごめん、\x01",
            "　もう一度考え直すからさ。）\x02\x03",

            "#0003F（あの時……\x01",
            "  あからさまにおかしな事を\x01",
            "  口走っている人がいた。）\x02\x03",

            "（絶対にあり得るはずのないことを\x01",
            "  さも、当たり前のことのように……)\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#11P#0300F（もうすぐクロスベル市に着いちまう。\x01",
            "　ビシッと決めてくれよ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#5P#0001F（この中にいる\x01",
            "　偽ブランド業者のリーダーは……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x2, 0xE)
    OP_29(0x1B, 0x2, 0xF)
    OP_29(0x1B, 0x2, 0x10)
    OP_29(0x1B, 0x2, 0x11)
    OP_29(0x1B, 0x2, 0x12)
    Jump("loc_3322")

    label("loc_3322")

    Jump("loc_2C19")

    label("loc_3327")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x15, 0, 0, 18)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x15, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
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
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_24(0x1DA)
    SetScenarioFlags(0x5C, 0)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1698 end

    def Function_16_33DC(): pass

    label("Function_16_33DC")

    OP_25(0x1D4, 0x5A)
    Sleep(80)
    OP_25(0x1D4, 0x50)
    Sleep(80)
    OP_25(0x1D4, 0x46)
    Sleep(80)
    OP_25(0x1D4, 0x3C)
    Sleep(80)
    OP_25(0x1D4, 0x32)
    Sleep(80)
    OP_25(0x1D4, 0x28)
    Sleep(80)
    OP_25(0x1D4, 0x1E)
    Sleep(80)
    OP_25(0x1D4, 0x14)
    Sleep(80)
    OP_25(0x1D4, 0xA)
    Sleep(80)
    OP_25(0x1D4, 0x0)
    Return()

    # Function_16_33DC end

    def Function_17_3420(): pass

    label("Function_17_3420")

    OP_25(0x1DA, 0xA)
    Sleep(80)
    OP_25(0x1DA, 0x14)
    Sleep(80)
    OP_25(0x1DA, 0x1E)
    Sleep(80)
    OP_25(0x1DA, 0x28)
    Sleep(80)
    OP_25(0x1DA, 0x32)
    Sleep(80)
    OP_25(0x1DA, 0x3C)
    Sleep(80)
    OP_25(0x1DA, 0x46)
    Sleep(80)
    OP_25(0x1DA, 0x50)
    Sleep(80)
    OP_25(0x1DA, 0x5A)
    Sleep(80)
    OP_25(0x1DA, 0x64)
    Return()

    # Function_17_3420 end

    def Function_18_3464(): pass

    label("Function_18_3464")

    OP_25(0x1DA, 0x5A)
    Sleep(80)
    OP_25(0x1DA, 0x50)
    Sleep(80)
    OP_25(0x1DA, 0x46)
    Sleep(80)
    OP_25(0x1DA, 0x3C)
    Sleep(80)
    OP_25(0x1DA, 0x32)
    Sleep(80)
    OP_25(0x1DA, 0x28)
    Sleep(80)
    OP_25(0x1DA, 0x1E)
    Sleep(80)
    OP_25(0x1DA, 0x14)
    Sleep(80)
    OP_25(0x1DA, 0xA)
    Sleep(80)
    OP_25(0x1DA, 0x0)
    Return()

    # Function_18_3464 end

    SaveToFile()

Try(main)
