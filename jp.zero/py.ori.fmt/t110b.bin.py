from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t110b.bin",                # FileName
        "t110b",                    # MapName
        "t110b",                    # Location
        0x0046,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 70, 0, 2, 0, 3],
    )

    BuildStringList((
        "t110b",                  # 0
        "黒服",                   # 1
        "黒服",                   # 2
        "マフィア",               # 3
        "マフィア",               # 4
        "マフィア",               # 5
        "マフィア",               # 6
        "マフィア",               # 7
        "招待客",                 # 8
        "招待客",                 # 9
        "偃月輪",                 # 10
        "偃月輪",                 # 11
        "偃月輪",                 # 12
        "偃月輪",                 # 13
        "ホテル・デルフィニア方面",# 14
    ))

    AddCharChip((
        "chr/ch36000.itc",                   # 00
        "chr/ch36100.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch26800.itc",                   # 03
        "apl/ch50363.itc",                   # 04
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   2,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   3,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 31,  0.0,                   0.0,                   -1.0,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -0.0,                  0.19999998807907104,   1.0])

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "ホテル・デルフィニア方面")

    ScpFunction((
        "Function_0_36C",          # 00, 0
        "Function_1_424",          # 01, 1
        "Function_2_425",          # 02, 2
        "Function_3_446",          # 03, 3
        "Function_4_47A",          # 04, 4
        "Function_5_56D",          # 05, 5
        "Function_6_EE7",          # 06, 6
        "Function_7_1DC9",         # 07, 7
        "Function_8_1DF9",         # 08, 8
        "Function_9_1E29",         # 09, 9
        "Function_10_1E59",        # 0A, 10
        "Function_11_1E89",        # 0B, 11
        "Function_12_1EDE",        # 0C, 12
        "Function_13_1F15",        # 0D, 13
        "Function_14_336B",        # 0E, 14
        "Function_15_33C7",        # 0F, 15
        "Function_16_3428",        # 10, 16
        "Function_17_3489",        # 11, 17
        "Function_18_34FE",        # 12, 18
        "Function_19_3567",        # 13, 19
        "Function_20_35DC",        # 14, 20
        "Function_21_3651",        # 15, 21
        "Function_22_36BA",        # 16, 22
        "Function_23_36D9",        # 17, 23
        "Function_24_3701",        # 18, 24
        "Function_25_3729",        # 19, 25
        "Function_26_376F",        # 1A, 26
        "Function_27_3809",        # 1B, 27
        "Function_28_384F",        # 1C, 28
        "Function_29_38FF",        # 1D, 29
        "Function_30_3945",        # 1E, 30
        "Function_31_39EE",        # 1F, 31
    ))


    def Function_0_36C(): pass

    label("Function_0_36C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3AC"),
        (1, "loc_3B8"),
        (2, "loc_3C4"),
        (3, "loc_3D0"),
        (4, "loc_3DC"),
        (5, "loc_3E8"),
        (6, "loc_3F4"),
        (SWITCH_DEFAULT, "loc_400"),
    )


    label("loc_3AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_400")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_40C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_423")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_423")

    Return()

    # Function_0_36C end

    def Function_1_424(): pass

    label("Function_1_424")

    Return()

    # Function_1_424 end

    def Function_2_425(): pass

    label("Function_2_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_436")
    Event(0, 5)

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_445")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_445")

    Return()

    # Function_2_425 end

    def Function_3_446(): pass

    label("Function_3_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 3)), scpexpr(EXPR_END)), "loc_452")
    Call(0, 4)

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_45B")

    label("loc_45B")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_473")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_473")

    Sound(126, 1, 80, 0)
    Return()

    # Function_3_446 end

    def Function_4_47A(): pass

    label("Function_4_47A")

    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, 2500, 0, -10500, 315)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x2)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, 1340, 0, -12150, 135)
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xD, -1950, 0, -13510, 315)
    SetChrChipByIndex(0xE, 0x4)
    SetChrSubChip(0xE, 0x2)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x1)
    SetChrPos(0xE, 1910, 0, -15040, 180)
    Return()

    # Function_4_47A end

    def Function_5_56D(): pass

    label("Function_5_56D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08100.itc", 0x1E)
    OP_68(0, 1800, -27300, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(20000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5FF")
    SetChrPos(0x101, -600, 0, -30250, 0)
    SetChrPos(0x102, 600, 0, -31250, 315)
    SetChrPos(0x103, 1250, 0, -33500, 315)
    SetChrPos(0x104, 1990, 0, -32500, 315)
    Jump("loc_69E")

    label("loc_5FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_651")
    SetChrPos(0x101, -600, 0, -30250, 0)
    SetChrPos(0x102, 1250, 0, -33500, 315)
    SetChrPos(0x103, 600, 0, -31250, 315)
    SetChrPos(0x104, 1990, 0, -32500, 315)
    Jump("loc_69E")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_69E")
    SetChrPos(0x101, -600, 0, -30250, 0)
    SetChrPos(0x102, 1990, 0, -32500, 315)
    SetChrPos(0x103, 1250, 0, -33500, 315)
    SetChrPos(0x104, 600, 0, -31250, 315)

    label("loc_69E")

    FadeToBright(1000, 0)
    OP_68(0, 900, -27300, 3000)
    OP_6F(0x1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_713")
    TurnDirection(0x102, 0x101, 300)

    #C0001
    ChrTalk(
        0x102,
        (
            "#5304F#2P私の方は問題ないわ。\x02\x03",

            "#5300Fそろそろ行きましょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF")

    label("loc_713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_778")
    TurnDirection(0x103, 0x101, 300)

    #C0002
    ChrTalk(
        0x103,
        (
            "#5403F#2P……わたしの方は\x01",
            "特に問題ありません。\x02\x03",

            "#5401Fそろそろ行きますか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF")

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_7CF")
    TurnDirection(0x104, 0x101, 300)

    #C0003
    ChrTalk(
        0x104,
        (
            "#5604F#2P俺の方はいつでもいいぜ。\x02\x03",

            "#5600Fそろそろ行くとするかよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CF")

    TurnDirection(0x101, 0xEF, 400)

    #C0004
    ChrTalk(
        0x101,
        "#5003F#5Pああ……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【オークション会場に入る】\x01",      # 0
            "【まだ入らない】\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_853"),
        (1, "loc_D78"),
        (SWITCH_DEFAULT, "loc_EE6"),
    )


    label("loc_853")

    StopBGM(0xBB8)
    Sleep(150)
    Fade(1000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(882, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは伊達メガネを付けた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0006
    ChrTalk(
        0x101,
        (
            "#5100F#5P──準備はＯＫだ。\x01",
            "オークション会場に入ろう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_A17")

    #C0007
    ChrTalk(
        0x102,
        "#5304F#2Pええ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        (
            "#0201F#12Pロイドさん、エリィさん。\x01",
            "……どうかお気をつけて。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x1F4)

    #C0009
    ChrTalk(
        0x104,
        (
            "#0301F#12P打ち合わせ通り、俺たちは\x01",
            "この辺りで待機してるぜ。\x02\x03",

            "何かあったらすぐに\x01",
            "エニグマで連絡してこいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#5102F#5Pああ。\x01",
            "そっちの方も気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x102,
        "#5302F#5Pそれじゃあ行って来るわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C8C")

    label("loc_A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_B55")

    #C0012
    ChrTalk(
        0x103,
        "#5404F#2P……了解しました。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        (
            "#0101F#12Pロイド、ティオちゃん。\x01",
            "くれぐれも気をつけてね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x87, 0x1F4)

    #C0014
    ChrTalk(
        0x104,
        (
            "#0301F#12P打ち合わせ通り、俺たちは\x01",
            "この辺りで待機しているぜ。\x02\x03",

            "何かあったらすぐに\x01",
            "エニグマで連絡してこいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#5102F#5Pああ。\x01",
            "そっちの方も気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#5402F#5P……それでは行ってきます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C8C")

    label("loc_B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_C8C")

    #C0017
    ChrTalk(
        0x104,
        "#5604F#2Pよし、行くか。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        (
            "#0201F#12Pロイドさん、ランディさん。\x01",
            "……どうかお気をつけて。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x87, 0x1F4)

    #C0019
    ChrTalk(
        0x102,
        (
            "#0101F#12P打ち合わせ通り、私たちは\x01",
            "この付近で待機しているわ。\x02\x03",

            "何かあったらすぐに\x01",
            "エニグマで連絡してきてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#5102F#5Pああ。\x01",
            "そっちの方も気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#5602F#5Pそんじゃ、行って来るぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_C8C")

    WaitBGM()
    PlayBGM("ed7125", 0)

    def lambda_C96():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C96)

    def lambda_CA3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_CA3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_68(0, 2600, -27300, 6000)

    def lambda_CC9():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CC9)

    def lambda_CDE():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_CDE)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_D5(0x1E)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrChipPat(0x0, 0x1, 0x51)
    LoadChrChipPat()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_D4D")
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    Jump("loc_D70")

    label("loc_D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_D61")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    Jump("loc_D70")

    label("loc_D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_D70")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)

    label("loc_D70")

    Call(0, 6)
    Jump("loc_EE6")

    label("loc_D78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_DFC")

    #C0022
    ChrTalk(
        0x102,
        (
            "#5303F……分かった。\x01",
            "でも、そんなに時間はないわ。\x02\x03",

            "#5301Fなるべく他の招待客に紛れて\x01",
            "会場に入るようにしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_E69")

    #C0023
    ChrTalk(
        0x103,
        (
            "#5403F……了解しました。\x02\x03",

            "#5401Fただ、他の招待客がいるうちに\x01",
            "入った方がいいかと思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECB")

    label("loc_E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_ECB")

    #C0024
    ChrTalk(
        0x104,
        (
            "#5605Fなんだ、入らないのか？\x02\x03",

            "#5601F他の招待客がいるうちに\x01",
            "入っちまった方がいいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("t101B", 101, 0, 0)
    IdleLoop()
    Jump("loc_EE6")

    label("loc_EE6")

    Return()

    # Function_5_56D end

    def Function_6_EE7(): pass

    label("Function_6_EE7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50354.itc", 0x1E)
    LoadChrToIndex("apl/ch50355.itc", 0x1F)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, 600, 0, 23800, 180)
    SetChrPos(0x9, -600, 0, 23800, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0xF, -340, 200, 1500, 0)
    SetChrPos(0x10, 770, 200, 750, 0)
    SetChrPos(0x101, 600, 0, -19500, 0)
    SetChrPos(0xEF, -600, 0, -21000, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    OP_70(0x0, 0xA)
    ClearMapObjFlags(0x0, 0x10)
    FadeToBright(1000, 0)
    OP_68(0, 500, 1470, 0)
    MoveCamera(36, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44890, 0)
    OP_68(0, 500, 22520, 15000)

    def lambda_FF8():
        OP_95(0xFE, 600, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FF8)

    def lambda_1012():
        OP_95(0xFE, -600, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1012)

    def lambda_102C():
        OP_95(0xFE, -600, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_102C)

    def lambda_1046():
        OP_95(0xFE, 600, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1046)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    Sleep(1000)
    BeginChrThread(0x8, 3, 0, 7)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 8)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    BeginChrThread(0xF, 3, 0, 11)
    Sleep(1000)
    BeginChrThread(0x10, 3, 0, 11)
    Sleep(2000)
    BeginChrThread(0x8, 3, 0, 9)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 10)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    Sleep(1000)
    OP_0D()
    Fade(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    SetChrPos(0x8, 600, 0, 23800, 180)
    SetChrPos(0x9, -600, 0, 23800, 180)
    SetChrPos(0x101, 600, 0, 13500, 0)
    SetChrPos(0xEF, -600, 0, 12500, 0)
    OP_68(0, 1000, 22320, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21700, 0)
    SetCameraDistance(19200, 3000)

    def lambda_113F():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_113F)

    def lambda_1154():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1154)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1191():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1191)
    Sleep(100)

    def lambda_11A9():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11A9)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x10)

    #C0025
    ChrTalk(
        0x8,
        "#5Pようこそ、《黒の競売会#10Rシュバルツオークション#》へ。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        "#5P招待カードを見せていただけますか？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        "#5100F#11Pああ、これでいいかな。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはマフィアと思しき黒服に\x01",
            "金の薔薇が刻まれたカードを渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0029
    ChrTalk(
        0x8,
        "#5P……確かに。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        (
            "#5P念のためお名前を\x01",
            "伺ってもよろしいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#5105F#11Pえっと……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0032
    ChrTalk(
        0x101,
        (
            "#5104F#11P──ガイ・バニングスだ。\x01",
            "身分は明かす必要はないだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        "#5Pええ、それはもちろん。\x02",
    )

    CloseMessageWindow()

    def lambda_1390():

        label("loc_1390")

        TurnDirection(0xFE, 0xEF, 500)
        Yield()
        Jump("loc_1390")

    QueueWorkItem2(0x8, 1, lambda_1390)
    Sleep(300)

    #C0034
    ChrTalk(
        0x8,
        "#5Pそちらの方は……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_16A8")

    #C0035
    ChrTalk(
        0x102,
        (
            "#5304F#12Pふふ、お疲れさま。\x02\x03",

            "#5300F私の方は事情があって、\x01",
            "身分を明かせないのだけど……\x02\x03",

            "こういう催しでもあるし、\x01",
            "別に構わないのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        "#5Pえ、ええ、まあ……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#5Pですが一応、そちらのガイ様との\x01",
            "ご関係を伺ってもよろしいですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0x102, 0x2BC, 0x0, 0x1F4, 0x7D0, 0x0)
    Fade(250)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    EndChrThread(0x8, 0x1)
    Sleep(300)

    #C0038
    ChrTalk(
        0x102,
        (
            "#5309F#12Pあら、恋人には見えない？\x02\x03",

            "#5302Fふふ……と言っても、\x01",
            "まだお父様とお母様には\x01",
            "内緒にしている関係なんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#5106F#11Pゴメン、僕が君の身分に\x01",
            "釣り合わないばっかりに……\x02\x03",

            "#5101Fでも、きっと事業を成功させて\x01",
            "ご両親にお嬢さんをくださいって\x01",
            "頼めるように頑張るから……！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        "#5309F#12Pふふっ、期待してるわね。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "#5Pコホン……失礼しました。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        "#5Pそれではガイ様、お連れ様。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "#5Pどうか存分に、今宵の競売会を\x01",
            "お楽しみになってください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D46")

    label("loc_16A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_19FD")
    TurnDirection(0x103, 0x101, 400)
    Sleep(300)

    #C0044
    ChrTalk(
        0x103,
        (
            "#5406F#6P……あの、兄さま。\x02\x03",

            "#5408Fこの方たちに名前を\x01",
            "教える必要がありますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#5104F#11Pああ、その必要はないよ。\x02\x03",

            "#5101F──この子は僕の妹だ。\x01",
            "何か問題があるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "#5Pいえ、とんでもない。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#5Pただ……\x01",
            "あまり似てらっしゃらない\x01",
            "ご兄妹ですね？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x190)

    #C0048
    ChrTalk(
        0x103,
        (
            "#5404F#12P……ええ、当然かと。\x02\x03",

            "#5402Fわたしは母さまの連れ子。\x01",
            "兄さまとは血が繋がっていませんから。\x02\x03",

            "#5409Fもちろん結婚だって出来ますし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0049
    ChrTalk(
        0x101,
        (
            "#5106F#11Pまったく……\x01",
            "あまりマセた事を言わない。\x02\x03",

            "#5102F──まあ、我が家にも\x01",
            "色々と事情があってね。\x02\x03",

            "ちなみにこの子は\x01",
            "結構な鑑識眼を持っている。\x02\x03",

            "今回のオークションの出物を\x01",
            "目利きしてもらうつもりだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        (
            "#5402F#12Pふふ……\x01",
            "楽しみですね、兄さま。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "#5Pはは、仲の良いご兄妹ですな。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        "#5Pそれではガイ様、妹君。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "#5Pどうか存分に、今宵の競売会を\x01",
            "お楽しみになってください。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x1)
    Jump("loc_1D46")

    label("loc_19FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1D46")

    #C0054
    ChrTalk(
        0x104,
        (
            "#5600F#12Pああ、俺はこの坊ちゃんの\x01",
            "幼なじみにして悪友って所だ。\x02\x03",

            "#5609Fいや～、コイツ、\x01",
            "ちょっと真面目すぎるからさ。\x02\x03",

            "こういった大人の催しで\x01",
            "色々と経験積ませてやろうと\x01",
            "出席を勧めてやったんだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0055
    ChrTalk(
        0x101,
        (
            "#5111F#11Pそ、そんな事まで\x01",
            "喋らなくてもいいだろう！？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        "#5Pはは、なるほど。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#5P確かに良い経験には\x01",
            "なるかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#5106F#11Pまったく、いいかげん\x01",
            "子供扱いは止めてくれよ。\x02\x03",

            "#5101F今回だって、君に勧められたから\x01",
            "来たわけじゃないんだからな。\x02\x03",

            "その、将来のことも考えて\x01",
            "色々と社会勉強をだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#5604F#12P分かった分かった。\x01",
            "そうムキになるなっての。\x02\x03",

            "#5602F──噂によると、なかなか\x01",
            "豪勢な出品物ばかりって話だが……\x02\x03",

            "期待しちまってもいいのかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0060
    ChrTalk(
        0x8,
        "#5Pええ、それはもう。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        "#5Pそれではガイ様、お連れ様。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "#5Pどうか存分に、今宵の競売会を\x01",
            "お楽しみになってください。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x1)

    label("loc_1D46")

    BeginChrThread(0x8, 3, 0, 7)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 8)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    OP_68(0, 1000, 23820, 3000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1D98")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    BeginChrThread(0x101, 3, 0, 12)
    BeginChrThread(0x102, 3, 0, 12)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    Jump("loc_1DAF")

    label("loc_1D98")

    BeginChrThread(0x101, 3, 0, 11)
    Sleep(750)
    BeginChrThread(0xEF, 3, 0, 11)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)

    label("loc_1DAF")

    OP_6F(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_EE7 end

    def Function_7_1DC9(): pass

    label("Function_7_1DC9")


    def lambda_1DCE():
        OP_98(0xFE, 0x2BC, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DCE)

    def lambda_1DE8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1DE8)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_7_1DC9 end

    def Function_8_1DF9(): pass

    label("Function_8_1DF9")


    def lambda_1DFE():
        OP_98(0xFE, 0xFFFFFD44, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DFE)

    def lambda_1E18():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E18)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_8_1DF9 end

    def Function_9_1E29(): pass

    label("Function_9_1E29")


    def lambda_1E2E():
        OP_98(0xFE, 0xFFFFFD44, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E2E)

    def lambda_1E48():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E48)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_9_1E29 end

    def Function_10_1E59(): pass

    label("Function_10_1E59")


    def lambda_1E5E():
        OP_98(0xFE, 0x2BC, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E5E)

    def lambda_1E78():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E78)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_10_1E59 end

    def Function_11_1E89(): pass

    label("Function_11_1E89")


    def lambda_1E8E():
        OP_95(0xFE, 0, 0, 24380, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E8E)
    WaitChrThread(0xFE, 1)

    def lambda_1EAC():
        OP_95(0xFE, 0, 800, 29450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1EAC)
    Sleep(2000)

    def lambda_1EC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1EC9)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_11_1E89 end

    def Function_12_1EDE(): pass

    label("Function_12_1EDE")


    def lambda_1EE3():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1EE3)
    Sleep(3500)

    def lambda_1F00():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F00)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_12_1EDE end

    def Function_13_1F15(): pass

    label("Function_13_1F15")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31100.itc", 0x22)
    LoadChrToIndex("chr/ch31150.itc", 0x23)
    LoadChrToIndex("chr/ch31151.itc", 0x24)
    LoadChrToIndex("chr/ch31153.itc", 0x25)
    LoadChrToIndex("chr/ch31900.itc", 0x26)
    LoadChrToIndex("chr/ch31952.itc", 0x27)
    LoadChrToIndex("chr/ch31951.itc", 0x28)
    LoadChrToIndex("chr/ch31953.itc", 0x29)
    LoadChrToIndex("apl/ch50372.itc", 0x2A)
    LoadEffect(0x0, "event\\ev310_00.eff")
    LoadEffect(0x1, "battle\\ms00001.eff")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xA, 2500, 0, -16500, 0)
    SetChrPos(0xB, -2500, 0, -16500, 0)
    SetChrPos(0xC, 0, 0, -17500, 0)
    SetChrPos(0xD, 1000, 0, -15500, 0)
    SetChrPos(0xE, -1000, 0, -15500, 0)
    SetChrChipByIndex(0x11, 0x2A)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x2A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x11, 0, 0, 50000, 0)
    SetChrPos(0x12, 0, 0, 50000, 0)
    BeginChrThread(0x11, 0, 0, 22)
    BeginChrThread(0x12, 0, 0, 22)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    OP_A7(0x13, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0x14, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 800, 29650, 180)
    SetChrPos(0xEF, 0, 800, 29650, 180)
    SetChrPos(0x105, 0, 800, 29650, 180)
    SetChrPos(0x133, 0, 800, 29650, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_215A")
    SetChrPos(0x103, 600, 200, -14600, 0)
    SetChrPos(0x104, -600, 200, -14600, 0)
    Jump("loc_21B5")

    label("loc_215A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_218A")
    SetChrPos(0x102, 600, 200, -14600, 0)
    SetChrPos(0x104, -600, 200, -14600, 0)
    Jump("loc_21B5")

    label("loc_218A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_21B5")
    SetChrPos(0x103, 600, 200, -14600, 0)
    SetChrPos(0x102, -600, 200, -14600, 0)

    label("loc_21B5")

    OP_68(0, 1100, 32500, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26840, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(25840, 2500)
    OP_6F(0x79)
    OP_0D()
    Sound(121, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(0, 1100, 21000, 3500)
    MoveCamera(0, 30, 0, 3500)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(300)
    BeginChrThread(0xEF, 3, 0, 15)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 16)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 1100, -2600, 0)
    MoveCamera(325, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25840, 0)
    SetCameraDistance(20320, 4000)
    OP_6F(0x10)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x105, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1100, -3200, 2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2339")

    def lambda_2304():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2304)
    Sleep(300)

    def lambda_231C():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_231C)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_23BA")

    label("loc_2339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_237C")

    def lambda_2347():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2347)
    Sleep(300)

    def lambda_235F():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_235F)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_23BA")

    label("loc_237C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_23BA")

    def lambda_238A():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_238A)
    Sleep(300)

    def lambda_23A2():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23A2)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)

    label("loc_23BA")

    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23ED")

    #C0063
    ChrTalk(
        0x103,
        "#0201F#6Pロイドさん……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_240D")

    label("loc_23ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_240D")

    #C0064
    ChrTalk(
        0x104,
        "#0307F#6Pロイド！\x02",
    )

    CloseMessageWindow()

    label("loc_240D")


    #C0065
    ChrTalk(
        0x101,
        (
            "#0002F#11Pよかった……\x01",
            "無事、合流できたか！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_24BE")

    #C0066
    ChrTalk(
        0x104,
        (
            "#0306F#6Pはあ……\x01",
            "ヒヤヒヤさせやがるな──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0067
    ChrTalk(
        0x104,
        "#0305F#6Pって、なんだその子は！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2548")

    label("loc_24BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2548")

    #C0068
    ChrTalk(
        0x102,
        (
            "#0106F#6Pふう……\x01",
            "ヒヤヒヤさせてくれるわね──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0069
    ChrTalk(
        0x102,
        (
            "#0105F#6Pって……\x01",
            "どうしたの、その子！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2597")

    #C0070
    ChrTalk(
        0x102,
        (
            "#0106F#11P通信で伝えたでしょう？\x01",
            "女の子を一人保護したって。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2626")

    label("loc_2597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_25E0")

    #C0071
    ChrTalk(
        0x103,
        (
            "#0206F#11P通信で伝えたように\x01",
            "保護した女の子ですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2626")

    label("loc_25E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2626")

    #C0072
    ChrTalk(
        0x104,
        (
            "#0309F#11P通信で言っただろ？\x01",
            "女の子を一人保護したって。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2626")


    #N0073
    NpcTalk(
        0x101,
        "キーア",
        (
            "#5805F#5Pねえねえ、ロイド。\x01",
            "このヒトたち、ミカタなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#0004F#11Pああ、信頼できる仲間さ。\x02\x03",

            "#0000F時間がない、早くここから──\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)

    #N0075
    NpcTalk(
        0xD,
        "男の声",
        "#2Pハッ、そうは行くかよ！\x02",
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1200, -7000, 2500)
    MoveCamera(310, 20, 0, 2500)
    OP_6E(560, 2500)
    SetCameraDistance(21000, 2500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_27EA")

    def lambda_27D0():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27D0)

    def lambda_27DD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_27DD)
    Jump("loc_2835")

    label("loc_27EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2812")

    def lambda_27F8():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27F8)

    def lambda_2805():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2805)
    Jump("loc_2835")

    label("loc_2812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2835")

    def lambda_2820():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2820)

    def lambda_282D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_282D)

    label("loc_2835")


    def lambda_283A():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_283A)
    Sleep(50)

    def lambda_2852():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2852)
    Sleep(50)

    def lambda_286A():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_286A)
    Sleep(50)

    def lambda_2882():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2882)
    Sleep(50)

    def lambda_289A():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_289A)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    OP_0D()

    #C0076
    ChrTalk(
        0x101,
        "#0010F#11Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x105,
        (
            "#0406F#2Pやれやれ……\x01",
            "読まれていたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xD,
        (
            "#6Pクク、若頭の指示通り、\x01",
            "張っておいて正解だったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xE,
        (
            "#5Pなるほど……\x01",
            "警察の小僧どもだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xE,
        (
            "#5Pハッ、さすがにオイタが\x01",
            "過ぎたみてぇだなァ……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(150)
    Fade(500)
    SetCameraDistance(20500, 500)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x2)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x2)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x2)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x2)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C8C")
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x101,
        "#0007F#11Pなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#0307F#11P導力式の重機関銃──\x01",
            "なんて物を持ち出しやがる！\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        (
            "#0201F#11Pしかも帝国製#6Rラインフォルト#の\x01",
            "最新式みたいですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xD,
        (
            "#6Pクク……\x01",
            "抵抗してもいいんだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xE,
        (
            "#5Pハハ、この間合いだったら\x01",
            "あっという間にミンチだろうがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        "#0110F#11Pくっ……\x02",
    )

    CloseMessageWindow()

    #N0087
    NpcTalk(
        0x101,
        "キーア",
        (
            "#5801F#5Pねえねえ、ロイド……\x02\x03",

            "もしかしてこれが\x01",
            "“ぴんち”っていうやつ？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#0013F#11Pああ……\x01",
            "どうやらそうみたいだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0089
    ChrTalk(
        0x105,
        (
            "#0404F#11Pいや……\x01",
            "まだみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#0005F#11Pえ──\x02",
    )

    CloseMessageWindow()

    label("loc_2C8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E4D")
    Fade(500)
    OP_68(-11030, 3200, -1010, 0)
    MoveCamera(310, 8, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(23000, 0)
    Sleep(300)
    OP_68(-140, 1200, -10540, 1500)
    MoveCamera(300, 28, 0, 1500)
    SetCameraDistance(17930, 1500)
    BeginChrThread(0x11, 3, 0, 26)
    Sleep(1350)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(500)

    #C0091
    ChrTalk(
        0xE,
        "#4S#5Pがっ……！？\x05\x02",
    )

    BeginChrThread(0xE, 3, 0, 17)
    Sleep(100)

    #C0092
    ChrTalk(
        0xD,
        "#4S#6Pうぐっ……！？\x05\x02",
    )

    BeginChrThread(0xD, 3, 0, 18)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x11, 3)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0093
    ChrTalk(
        0xA,
        "#5Pなっ……\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xB,
        "#5Pなんだ……！？\x02",
    )

    CloseMessageWindow()

    label("loc_2E4D")

    Fade(500)
    OP_68(2450, 800, -11290, 0)
    MoveCamera(224, 35, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(30050, 0)
    OP_68(0, 800, -9180, 3000)
    MoveCamera(305, 25, 0, 3000)
    SetCameraDistance(20000, 3000)
    BeginChrThread(0x11, 3, 0, 28)
    BeginChrThread(0x12, 3, 0, 30)
    Sleep(1650)
    OP_82(0x1F4, 0x0, 0xBB8, 0x96)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(500)

    #C0095
    ChrTalk(
        0xB,
        "#4S#5Pぎゃっ……！\x05\x02",
    )

    BeginChrThread(0xB, 3, 0, 19)
    Sleep(1600)
    OP_82(0x1F4, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(500)

    #C0096
    ChrTalk(
        0xC,
        "#4S#6Pぐはっ……！\x05\x02",
    )

    BeginChrThread(0xC, 3, 0, 21)
    Sleep(150)

    #C0097
    ChrTalk(
        0xA,
        "#4S#6Pうおっ……！\x05\x02",
    )

    BeginChrThread(0xA, 3, 0, 20)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_68(0, 1100, -3200, 2500)
    MoveCamera(325, 13, 0, 2500)
    OP_6E(500, 2500)
    SetCameraDistance(21000, 2500)
    OP_6F(0x79)

    #N0098
    NpcTalk(
        0x101,
        "キーア",
        (
            "#5805F#5Pほえ～っ……\x02\x03",

            "#5810F黒いヒトたち\x01",
            "やられちゃったよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        "#0011F#11Pい、今のは……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30E1")
    OP_93(0x104, 0x0, 0x1F4)

    #C0100
    ChrTalk(
        0x104,
        (
            "#0301F#6P屋敷の方から\x01",
            "飛んできたみたいだが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3116")

    label("loc_30E1")


    #C0101
    ChrTalk(
        0x104,
        (
            "#0301F#11P屋敷の方から\x01",
            "飛んできたみたいだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3116")


    #C0102
    ChrTalk(
        0x105,
        (
            "#0404F#11Pフフ、どうやら他にも\x01",
            "助っ人がいたみたいだね。\x02\x03",

            "#0402F詮索は後にして\x01",
            "逃げた方がいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#0007F#11Pああ……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31ED")
    OP_93(0x102, 0x0, 0x1F4)

    #C0104
    ChrTalk(
        0x102,
        (
            "#0101F#6P今なら丁度、\x01",
            "水上バスが来ているはずよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3233")

    label("loc_31ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3233")
    OP_93(0x103, 0x0, 0x1F4)

    #C0105
    ChrTalk(
        0x103,
        (
            "#0201F#6P今なら丁度、\x01",
            "水上バスが来ています……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3275")
    OP_93(0x104, 0x0, 0x1F4)

    #C0106
    ChrTalk(
        0x104,
        "#0307F#6Pとにかく波止場に向かうぞ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_32B9")

    label("loc_3275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_32B9")
    OP_93(0x103, 0x0, 0x1F4)

    #C0107
    ChrTalk(
        0x103,
        (
            "#0201F#6P……とにかく\x01",
            "波止場に向かいましょう！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32B9")

    FadeToDark(1000, 0, -1)
    SetCameraDistance(20000, 2000)
    OP_6F(0x10)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x5A, 3)
    Call(0, 4)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_49()
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    OP_70(0x0, 0x0)
    ClearMapObjFlags(0x0, 0x10)
    SetScenarioFlags(0xA7, 3)
    OP_29(0x47, 0x1, 0x12)
    EventEnd(0x5)
    Return()

    # Function_13_1F15 end

    def Function_14_336B(): pass

    label("Function_14_336B")


    def lambda_3370():
        OP_9B(0x0, 0xFE, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3370)

    def lambda_3385():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3385)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_98(0xFE, 0x0, 0x0, 0x0, 0x0, 0x0)

    def lambda_33B2():
        OP_9B(0x0, 0xFE, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33B2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_336B end

    def Function_15_33C7(): pass

    label("Function_15_33C7")


    def lambda_33CC():
        OP_9B(0x0, 0xFE, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33CC)

    def lambda_33E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33E1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_98(0xFE, 0x258, 0x0, 0x0, 0x0, 0x0)

    def lambda_340E():
        OP_95(0xFE, -600, 200, -1700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_340E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_33C7 end

    def Function_16_3428(): pass

    label("Function_16_3428")


    def lambda_342D():
        OP_9B(0x0, 0xFE, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_342D)

    def lambda_3442():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3442)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_98(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x0, 0x0)

    def lambda_346F():
        OP_95(0xFE, 600, 200, -2200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_346F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_3428 end

    def Function_17_3489(): pass

    label("Function_17_3489")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1000, 900, -10500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_34D3():
        OP_9D(0xFE, 0xFFFFFC18, 0x0, 0xFFFFCB44, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34D3)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_17_3489 end

    def Function_18_34FE(): pass

    label("Function_18_34FE")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 1000, 900, -10500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_3542():
        OP_9D(0xFE, 0x3E8, 0x0, 0xFFFFC950, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3542)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_18_34FE end

    def Function_19_3567(): pass

    label("Function_19_3567")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -2500, 900, -11500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_35B1():
        OP_9D(0xFE, 0xFFFFE4A8, 0xFFFFD8F0, 0xFFFFCD38, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35B1)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Sound(927, 0, 100, 0)
    Return()

    # Function_19_3567 end

    def Function_20_35DC(): pass

    label("Function_20_35DC")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 2500, 900, -11500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_3626():
        OP_9D(0xFE, 0x9C4, 0x0, 0xFFFFCF2C, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3626)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_20_35DC end

    def Function_21_3651(): pass

    label("Function_21_3651")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 900, -12500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_3695():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFFCB44, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3695)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_21_3651 end

    def Function_22_36BA(): pass

    label("Function_22_36BA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36D8")
    OP_A1(0xFE, 0xFA0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_22_36BA")

    label("loc_36D8")

    Return()

    # Function_22_36BA end

    def Function_23_36D9(): pass

    label("Function_23_36D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3700")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_23_36D9")

    label("loc_3700")

    Return()

    # Function_23_36D9 end

    def Function_24_3701(): pass

    label("Function_24_3701")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3728")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_24_3701")

    label("loc_3728")

    Return()

    # Function_24_3701 end

    def Function_25_3729(): pass

    label("Function_25_3729")

    SetChrPos(0xFE, 0, 0, 14500, 0)
    OP_9E(0xFE, 0x0, 0x7D0, 0xFFFEA070, 0xEA60, 0x0)

    def lambda_3754():
        OP_9E(0xFE, 0x0, 0x7D0, 0xFFFD40E0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3754)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_3729 end

    def Function_26_376F(): pass

    label("Function_26_376F")

    PlayEffect(0x0, 0xFF, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(926, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0x13, 3, 0, 25)
    BeginChrThread(0xFE, 2, 0, 23)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37F8")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_37CA")

    label("loc_37F8")

    WaitChrThread(0x13, 3)
    EndChrThread(0xFE, 0x2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_26_376F end

    def Function_27_3809(): pass

    label("Function_27_3809")

    SetChrPos(0xFE, -2500, 0, 16000, 0)
    OP_9E(0xFE, 0xFFFFF63C, 0x8CA, 0x13880, 0xEA60, 0x0)

    def lambda_3834():
        OP_9E(0xFE, 0xFFFFF63C, 0x8CA, 0x347D8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3834)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_3809 end

    def Function_28_384F(): pass

    label("Function_28_384F")

    PlayEffect(0x0, 0xFF, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(926, 0, 100, 0)
    SetChrFlags(0xFE, 0x800)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0x13, 3, 0, 27)
    BeginChrThread(0xFE, 2, 0, 23)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38E9")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_NEG), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_38AF")

    label("loc_38E9")

    WaitChrThread(0x13, 3)
    EndChrThread(0xFE, 0x2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x800)
    Return()

    # Function_28_384F end

    def Function_29_38FF(): pass

    label("Function_29_38FF")

    SetChrPos(0xFE, 0, 0, 15000, 0)
    OP_9E(0xFE, 0x0, 0x3E8, 0xFFFDF0A8, 0xEA60, 0x0)

    def lambda_392A():
        OP_9E(0xFE, 0x0, 0x3E8, 0xFFFDF0A8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_392A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_38FF end

    def Function_30_3945(): pass

    label("Function_30_3945")

    Sleep(2000)
    PlayEffect(0x0, 0xFF, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(926, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0x14, 3, 0, 29)
    BeginChrThread(0xFE, 2, 0, 24)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39DD")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_NEG), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_39A3")

    label("loc_39DD")

    WaitChrThread(0x14, 3)
    EndChrThread(0xFE, 0x2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_30_3945 end

    def Function_31_39EE(): pass

    label("Function_31_39EE")

    EventBegin(0x1)

    #C0108
    ChrTalk(
        0x101,
        (
            "#0001F引き返している場合じゃない……\x01",
            "この子を連れて波止場へ急ごう！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 200, -1700, 180)
    EventEnd(0x4)
    Return()

    # Function_31_39EE end

    SaveToFile()

Try(main)
