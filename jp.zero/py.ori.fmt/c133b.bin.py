﻿from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c133b.bin",                # FileName
        "c133b",                    # MapName
        "c133b",                    # Location
        0x001B,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "c133b",                  # 0
        "エリィ",                 # 1
    ))

    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_C8",           # 00, 0
        "Function_1_FB",           # 01, 1
        "Function_2_FC",           # 02, 2
        "Function_3_462",          # 03, 3
        "Function_4_883",          # 04, 4
        "Function_5_CBF",          # 05, 5
    ))


    def Function_0_C8(): pass

    label("Function_0_C8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3")
    Event(0, 3)
    Jump("loc_FA")

    label("loc_E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_F7")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_FA")

    label("loc_F7")

    Event(0, 2)

    label("loc_FA")

    Return()

    # Function_0_C8 end

    def Function_1_FB(): pass

    label("Function_1_FB")

    Return()

    # Function_1_FB end

    def Function_2_FC(): pass

    label("Function_2_FC")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_68(600, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x0, 2200, 0, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_166")
    SetChrPos(0x1, 500, 0, -500, 90)

    label("loc_166")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_185")
    SetChrPos(0x2, 500, 0, 500, 90)

    label("loc_185")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A4")
    SetChrPos(0x3, -700, 0, 0, 90)

    label("loc_1A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C3")
    SetChrPos(0x4, -1900, 0, -600, 90)

    label("loc_1C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E2")
    SetChrPos(0x5, -1900, 0, 600, 90)

    label("loc_1E2")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_250")

    Menu(
        0,
        10,
        10,
        0,
        (
            "★【１６Ｆ】\x01",      # 0
            "　【 １Ｆ 】\x01",      # 1
            "　【 Ｂ５ 】\x01",      # 2
            "　【降りる】\x01",      # 3
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FF")

    label("loc_250")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【１６Ｆ】\x01",      # 0
            "★【 １Ｆ 】\x01",      # 1
            "　【 Ｂ５ 】\x01",      # 2
            "　【降りる】\x01",      # 3
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FF")

    label("loc_2AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【１６Ｆ】\x01",      # 0
            "　【 １Ｆ 】\x01",      # 1
            "★【 Ｂ５ 】\x01",      # 2
            "　【降りる】\x01",      # 3
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FF")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_326")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_3A3")

    label("loc_326")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_35F")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_3A3")

    label("loc_35F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_398")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_3A3")

    label("loc_398")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_3A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_403")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3CE"),
        (1, "loc_3DE"),
        (2, "loc_3EE"),
        (SWITCH_DEFAULT, "loc_3FE"),
    )


    label("loc_3CE")

    EventEnd(0x5)
    NewScene("c134B", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FE")

    label("loc_3DE")

    EventEnd(0x5)
    NewScene("c131B", 101, 0, 0)
    IdleLoop()
    Jump("loc_3FE")

    label("loc_3EE")

    EventEnd(0x5)
    NewScene("c1320", 103, 0, 0)
    IdleLoop()
    Jump("loc_3FE")

    label("loc_3FE")

    Jump("loc_461")

    label("loc_403")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_41F"),
        (1, "loc_435"),
        (2, "loc_44B"),
        (SWITCH_DEFAULT, "loc_461"),
    )


    label("loc_41F")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c134B", 100, 0, 0)
    IdleLoop()
    Jump("loc_461")

    label("loc_435")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c131B", 101, 0, 0)
    IdleLoop()
    Jump("loc_461")

    label("loc_44B")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1320", 103, 0, 0)
    IdleLoop()
    Jump("loc_461")

    label("loc_461")

    Return()

    # Function_2_FC end

    def Function_3_462(): pass

    label("Function_3_462")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -4500, 0, 0, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_4FE():
        OP_96(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FE)

    def lambda_518():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_518)
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0001
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000Fはい、特務支援課、\x01",
            "ロイド・バニングスです！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性の声")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、私だ。\x01",
            "ディーター・クロイスだ。\x02\x03",

            "すまない、警察本部からの\x01",
            "連絡あたりと勘違いさせたかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0003
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006Fい、いえ……\x02\x03",

            "#0001Fもしかして、どこかと連絡が\x01",
            "取れたのでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ディーターの声")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いや、残念ながらまだだ。\x02\x03",

            "実は、ゲート前の警備員から\x01",
            "気になる報告があってね。\x02\x03",

            "休憩中に悪いが、私の部屋まで\x01",
            "来てくれないだろうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0005
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F分かりました。\x01",
            "すぐに伺います。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Fade(250)
    SetChrSubChip(0x101, 0x4)
    Sound(807, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0006
    ChrTalk(
        0x101,
        (
            "#0008F（警備員からの報告……\x01",
            "  ……嫌な感じがするな。）\x02\x03",

            "#0001F（一応、装備だけでも\x01",
            "  ちゃんと確認しておこう。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetScenarioFlags(0xE4, 4)
    OP_29(0x4E, 0x1, 0x1)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x326)
    EventEnd(0x5)
    Call(0, 2)
    Return()

    # Function_3_462 end

    def Function_4_883(): pass

    label("Function_4_883")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(861)
    OP_68(600, -3000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x102, 600, 0, -600, 90)
    SetChrPos(0x101, 600, 0, 600, 90)
    SetChrPos(0x103, -600, 0, -800, 90)
    SetChrPos(0x104, -600, 0, 800, 90)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 1000, 0, 0, 90)
    BeginChrThread(0x101, 3, 0, 5)
    Sound(861, 2, 100, 0)
    OP_68(600, 1000, 0, 5000)
    SetCameraDistance(18500, 5000)
    FadeToBright(4000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)

    #C0007
    ChrTalk(
        0x101,
        "#0004F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        "#0102F#5P絶対に……守らないとね。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        "#6P#0201F……はい……！\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x104,
        (
            "#6P#0303F一応言っておくが……\x01",
            "クロスベル警備隊は精鋭だ。\x02\x03",

            "操られているとはいえ、\x01",
            "薬の影響も馬鹿にはならねぇ。\x02\x03",

            "#0301F多分、今までで一番、\x01",
            "厳しい戦いが待ってるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#0004F#5Pああ……分かってる。\x02\x03",

            "#0000F俺たちのチームワークが\x01",
            "試されるってことだな。\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(17500, 800)

    def lambda_AE8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AE8)
    Sleep(50)

    def lambda_AF8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AF8)
    Sleep(50)

    def lambda_B08():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B08)
    Sleep(50)

    def lambda_B18():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B18)
    WaitChrThread(0x101, 2)
    OP_6F(0x10)
    CancelBlur(0)
    Sleep(300)

    #C0012
    ChrTalk(
        0x101,
        (
            "#0003F#5P──まずは導力爆弾の撤去。\x02\x03",

            "#0013Fそのままゲート前で\x01",
            "隊員たちの突入を阻止する。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0013
    ChrTalk(
        0x101,
        (
            "#0007F#5P女神の加護を！\x01",
            "くれぐれも気をつけてくれ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    #Sound(1153, 255, 100, 0)    #voice#Elie
    #Sound(1249, 255, 100, 1)    #voice#Tio
    #Sound(1343, 255, 100, 2)    #voice#Randy

    #C0014
    ChrTalk(
        0x8,
        "#0107F#1K#2Pええ！\x02",
    )


    #C0015
    ChrTalk(
        0x103,
        "#0201F#1K#6Pはい……！\x02",
    )


    #C0016
    ChrTalk(
        0x104,
        "#0307F#1K#1Pおおっ！\x02",
    )

    OP_57(0x1)
    OP_5A()
    FadeToDark(2000, 0, -1)
    Sound(862, 0, 100, 0)
    OP_24(0x35D)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    EndChrThread(0x101, 0x3)
    OP_6F(0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C98")
    OP_29(0x31, 0x4, 0x40)
    Jump("loc_CAA")

    label("loc_C98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAA")
    OP_29(0x31, 0x4, 0x40)

    label("loc_CAA")

    SetScenarioFlags(0xE7, 5)
    SetScenarioFlags(0x5F, 1)
    OP_24(0x35D)
    EventEnd(0x5)
    NewScene("c131B", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_4_883 end

    def Function_5_CBF(): pass

    label("Function_5_CBF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CE3")
    OP_82(0x0, 0x14, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_5_CBF")

    label("loc_CE3")

    Return()

    # Function_5_CBF end

    SaveToFile()

Try(main)
