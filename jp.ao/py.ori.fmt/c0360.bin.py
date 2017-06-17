from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0360.bin",                # FileName
        "c0360",                    # MapName
        "c0360",                    # Location
        0x002D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0360",                  # 0
        "イメルダ夫人",           # 1
        "人形",                   # 2
        "人形",                   # 3
        "女の子",                 # 4
    ))

    AddCharChip((
        "chr/ch09000.itc",                   # 00
        "apl/ch51445.itc",                   # 01
    ))

    DeclNpc(94540,   29,      6329,    0,    453,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(94199,   1049,    8100,    180,  453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(95099,   1049,    8100,    180,  453,  0x0, 2,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-570,    0,       6100,    1200,    -570,    1500,    6100,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(384, 0)                                        # 0

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_230",          # 01, 1
        "Function_2_2C0",          # 02, 2
        "Function_3_349",          # 03, 3
        "Function_4_3F3",          # 04, 4
        "Function_5_7D7",          # 05, 5
        "Function_6_2F8C",         # 06, 6
        "Function_7_2FD7",         # 07, 7
        "Function_8_3022",         # 08, 8
        "Function_9_306D",         # 09, 9
        "Function_10_30B8",        # 0A, 10
        "Function_11_3103",        # 0B, 11
        "Function_12_314E",        # 0C, 12
        "Function_13_31A3",        # 0D, 13
        "Function_14_31EE",        # 0E, 14
        "Function_15_3239",        # 0F, 15
        "Function_16_3284",        # 10, 16
        "Function_17_32CF",        # 11, 17
        "Function_18_331A",        # 12, 18
        "Function_19_3365",        # 13, 19
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1B8"),
        (1, "loc_1C4"),
        (2, "loc_1D0"),
        (3, "loc_1DC"),
        (4, "loc_1E8"),
        (5, "loc_1F4"),
        (6, "loc_200"),
        (SWITCH_DEFAULT, "loc_20C"),
    )


    label("loc_1B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_200")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_20C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_22F")

    Return()

    # Function_0_180 end

    def Function_1_230(): pass

    label("Function_1_230")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_253")
    Event(0, 5)

    label("loc_253")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BF")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0xA, 0x2)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BF")

    Return()

    # Function_1_230 end

    def Function_2_2C0(): pass

    label("Function_2_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_309")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_348")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_348")

    Return()

    # Function_2_2C0 end

    def Function_3_349(): pass

    label("Function_3_349")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "車雑誌『月間カーマニアvol.3』がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x374, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EF")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "ペイントパターン\x01\x07\x02",

            "『ディープカラー』\x07\x00",
            "を覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x374, 1)

    label("loc_3EF")

    TalkEnd(0xFF)
    Return()

    # Function_3_349 end

    def Function_4_3F3(): pass

    label("Function_4_3F3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74F")

    #C0003
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、それにしても……\x01",
            "あんたたちもご苦労だったねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "おかげさまで、この姉妹人形に\x01",
            "ようやく買い手がつくかもしれないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00101Fその……イメルダさんは\x01",
            "怖くないんですか？\x02\x03",

            "#00106F化けて出てくるような人形を\x01",
            "売り払ったりしたら、\x01",
            "た、祟られたりするんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、オバケが怖くて\x01",
            "こんな商売をやってられるかい！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "この倉庫に保管しているものにも、\x01",
            "いくつか妖しい品があるからねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "何なら、持ち主が次々と不幸になるっていう\x01",
            "いわくつきの指輪でも触ってみるかい？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_615")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_615")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63E")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_63E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_667")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_667")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68D")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_68D")

    Sleep(1000)

    #C0009
    ChrTalk(
        0x101,
        "#00012Fけ、結構です。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#00203F（……そういう品が一箇所に\x01",
            "  集まっていたせいで、霊的な場が\x01",
            "  生まれたのかもしれませんね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        "#00306F（け、結局このバーさんが原因かよ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x179, 2)
    Jump("loc_7D3")

    label("loc_74F")


    #C0012
    ChrTalk(
        0x8,
        (
            "おかげさまで、この姉妹人形に\x01",
            "ようやく買い手がつくかもしれないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、あんたたちには\x01",
            "感謝させてもらわないとねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D3")

    TalkEnd(0x8)
    Return()

    # Function_4_3F3 end

    def Function_5_7D7(): pass

    label("Function_5_7D7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch44400.itc", 0x1E)
    OP_68(-130, 1000, -130, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -2070, 0, -1990, 45)
    SetChrPos(0x102, -2070, 0, -1990, 45)
    SetChrPos(0x103, -2070, 0, -1990, 45)
    SetChrPos(0x104, -2070, 0, -1990, 45)
    SetChrPos(0x109, -2070, 0, -1990, 45)
    SetChrPos(0x105, -2070, 0, -1990, 45)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 7)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 8)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 9)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 10)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 11)
    OP_68(2840, 1000, 2910, 3000)
    OP_6F(0x1)
    StopBGM(0xFA0)
    WaitChrThread(0x105, 3)

    #C0014
    ChrTalk(
        0x101,
        (
            "#00000Fすみません、どなたか\x01",
            "いらっしゃいますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0015
    ChrTalk(
        0x104,
        (
            "#00305F……やっぱだれも\x01",
            "いないんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#00105Fでも、届け先の住所は\x01",
            "確かにここのはずよ。\x02\x03",

            "#00103F玄関にも鍵は\x01",
            "かかってなかったし……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 13000, 1030, 2280, 270)

    #N0017
    NpcTalk(
        0xB,
        "女の子の声",
        "……おにいちゃんたち、だあれ？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B51():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B51)
    Sleep(50)

    def lambda_B61():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B61)
    Sleep(50)

    def lambda_B71():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B71)
    Sleep(50)

    def lambda_B81():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B81)
    Sleep(50)

    def lambda_B91():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B91)
    Sleep(50)

    def lambda_BA1():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BA1)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    Fade(500)
    OP_68(10720, 1000, 3550, 0)
    MoveCamera(43, 34, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    OP_68(3490, 1000, 2870, 5000)
    OP_95(0xB, 4650, 0, 2360, 2000, 0x0)
    WaitChrThread(0xB, 1)
    OP_6F(0x1)

    #C0018
    ChrTalk(
        0x109,
        "#10105Fあ……？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        "#00105Fひ、人が……？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00005Fえ、えっと……\x01",
            "お嬢ちゃん、今お家に一人かい？\x02\x03",

            "#00000Fお兄さんたちは\x01",
            "荷物を届けに来たんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xB,
        (
            "あっ、もしかして……\x01",
            "届いたのかしら！？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        "ね、上がって上がって！\x02",
    )

    CloseMessageWindow()
    OP_95(0xB, 9850, 1030, 2520, 2000, 0x0)

    def lambda_D2A():
        OP_95(0xFE, 9500, 1050, 10700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D2A)
    Sleep(500)

    def lambda_D47():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D47)
    Sleep(50)

    def lambda_D57():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D57)
    Sleep(500)

    def lambda_D67():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D67)
    Sleep(50)

    def lambda_D77():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D77)
    Sleep(50)

    def lambda_D87():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D87)
    Sleep(50)

    def lambda_D97():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D97)
    WaitChrThread(0x105, 1)

    #C0023
    ChrTalk(
        0x105,
        (
            "#10309Fハハ、ろくに話を\x01",
            "聞いていない感じだね。\x02\x03",

            "#10300F察するに、あの子宛ての\x01",
            "荷物なのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#00106Fお、おかしいわ……\x02\x03",

            "#00101Fあんな子がいたなんて\x01",
            "聞いたことないもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#00306Fしかし……現実にこうして\x01",
            "出会っちまったわけだしなあ。\x02\x03",

            "#00301F一体どういうことなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#00003F分からないけど……\x02\x03",

            "#00000Fとりあえず、\x01",
            "中に入ってみよう。\x02\x03",

            "あの子からなにか\x01",
            "聞けるかもしれないしね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(8870, 2000, 11100, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_93(0xB, 0x10E, 0x0)
    SetChrPos(0x101, 8080, 1000, 11140, 90)
    SetChrPos(0x102, 7530, 1000, 10180, 90)
    SetChrPos(0x103, 7480, 1000, 11830, 90)
    SetChrPos(0x109, 6000, 1000, 10040, 90)
    SetChrPos(0x104, 6800, 1000, 10800, 90)
    SetChrPos(0x105, 5800, 1000, 11440, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0027
    ChrTalk(
        0x101,
        "#00000Fえっと、これが届けにきた荷物だよ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x33A, 1)

    #C0029
    ChrTalk(
        0xB,
        "わ～い、やっと帰ってきたぁ！\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x87, 0x1F4)
    Sleep(300)

    #C0030
    ChrTalk(
        0xB,
        "……うんしょ、と。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x3)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x2)
    SetChrPos(0xA, 10640, 1650, 10400, 270)
    Sound(802, 0, 70, 0)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    #C0031
    ChrTalk(
        0x104,
        (
            "#00305F（……随分ボロそうな人形だな。）\x02\x03",

            "（こいつもローゼンベルク製の\x01",
            "  アンティークドールってやつか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00103F（ううん、そこまで高価なものじゃ\x01",
            "  ないみたいだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00002Fもしかして、この人形は\x01",
            "君のものなのかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x1F4)
    Sleep(300)

    #C0034
    ChrTalk(
        0xB,
        "モノじゃないよ～！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xB,
        (
            "だいじなだいじな妹なの。\x01",
            "うふふ、いいこいいこ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#00106Fそうなんだ……\x02\x03",

            "#00109Fえ、ええっと。\x01",
            "ちゃんと届いてよかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        "うん、ありがとうね。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        (
            "それじゃ、ちょっとこの子を\x01",
            "わたしの部屋に連れてってくるね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x87, 0x1F4)
    Sleep(300)
    Fade(500)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x2)
    Sound(802, 0, 70, 0)
    Sleep(700)
    BeginChrThread(0xB, 3, 0, 12)

    def lambda_1305():

        label("loc_1305")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1305")

    QueueWorkItem2(0x101, 1, lambda_1305)

    def lambda_1317():

        label("loc_1317")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1317")

    QueueWorkItem2(0x102, 1, lambda_1317)

    def lambda_1329():

        label("loc_1329")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1329")

    QueueWorkItem2(0x103, 1, lambda_1329)

    def lambda_133B():

        label("loc_133B")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_133B")

    QueueWorkItem2(0x104, 1, lambda_133B)

    def lambda_134D():

        label("loc_134D")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_134D")

    QueueWorkItem2(0x109, 1, lambda_134D)

    def lambda_135F():

        label("loc_135F")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_135F")

    QueueWorkItem2(0x105, 1, lambda_135F)
    OP_68(2500, 2000, 15400, 5000)
    MoveCamera(45, 27, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(22000, 5000)
    OP_0D()
    Sleep(500)
    WaitChrThread(0xB, 3)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_13BC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_13BC)

    def lambda_13CD():
        OP_97(0xFE, 0x0, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13CD)
    Sleep(500)
    SetChrFlags(0xB, 0x80)
    OP_0D()
    Sleep(500)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)
    Sleep(500)
    Fade(500)
    OP_68(6820, 2000, 11510, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20850, 0)
    OP_93(0x103, 0x13B, 0x0)
    OP_0D()

    #C0039
    ChrTalk(
        0x109,
        (
            "#10103Fうーん……\x01",
            "結局なんなんでしょう。\x02\x03",

            "#10100F家に他の家族がいる\x01",
            "気配もありませんし……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x103,
        "#00203F………………………………\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#00005F……？\x01",
            "ティオ、どうした？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        (
            "#00203F……いえ、多分\x01",
            "気のせいだとは思うんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 410, 0, 410, 45)
    OP_4B(0x8, 0xFF)

    #N0043
    NpcTalk(
        0x8,
        "老婆の声",
        "#4S──これっ、だれかいるのかい！？\x02",
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1626():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1626)
    Sleep(50)

    def lambda_1636():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1636)
    Sleep(50)

    def lambda_1646():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1646)
    Sleep(50)

    def lambda_1656():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1656)
    Sleep(50)

    def lambda_1666():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1666)
    Sleep(50)

    def lambda_1676():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1676)
    WaitChrThread(0x105, 1)

    #C0044
    ChrTalk(
        0x101,
        "#00005F……い、今の声は……？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#00105Fお客さん……かしら？\x02\x03",

            "親御さんは\x01",
            "留守にしてるみたいだし、\x01",
            "私たちが出てあげましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#00000Fあ、ああ……そうだな。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(670, 1000, 1090, 0)
    MoveCamera(13, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19760, 0)
    SetChrPos(0x101, 9840, 1030, 1950, 270)
    SetChrPos(0x103, 10930, 1030, 1890, 270)
    SetChrPos(0x104, 12090, 1030, 1840, 270)
    SetChrPos(0x102, 9820, 1030, 3070, 270)
    SetChrPos(0x109, 10940, 1030, 3020, 270)
    SetChrPos(0x105, 12100, 1030, 2970, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(2140, 1000, 1810, 5000)
    SetCameraDistance(21780, 5000)

    def lambda_17F3():
        OP_95(0xFE, 2500, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17F3)
    Sleep(50)

    def lambda_1810():
        OP_95(0xFE, 2500, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1810)
    Sleep(50)

    def lambda_182D():
        OP_95(0xFE, 3700, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_182D)
    Sleep(50)

    def lambda_184A():
        OP_95(0xFE, 3700, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_184A)
    Sleep(50)

    def lambda_1867():
        OP_95(0xFE, 4900, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1867)
    Sleep(50)

    def lambda_1884():
        OP_95(0xFE, 4900, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1884)
    WaitChrThread(0x101, 1)

    def lambda_18A2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18A2)
    WaitChrThread(0x102, 1)

    def lambda_18B3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18B3)
    WaitChrThread(0x103, 1)

    def lambda_18C4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18C4)
    WaitChrThread(0x109, 1)

    def lambda_18D5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18D5)
    WaitChrThread(0x104, 1)

    def lambda_18E6():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_18E6)
    WaitChrThread(0x105, 1)

    def lambda_18F7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_18F7)
    OP_6F(0x79)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00005Fあ……\x01",
            "アンティークショップの。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "おや、アンタたち……\x01",
            "こんな所で何をしてるんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#00012Fえっとまあ、\x01",
            "仕事で伺ったところ\x01",
            "だったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        "#00105Fこのお宅に何か御用でしょうか？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0051
    ChrTalk(
        0x8,
        (
            "……仕事？\x01",
            "何を言ってるんだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "この家には\x01",
            "１０年以上前から\x01",
            "だれも入居してないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "しばらくアタシの\x01",
            "アンティークショップの\x01",
            "物置になってるくらいさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0054
    ChrTalk(
        0x8,
        (
            "……なんだい、\x01",
            "その腑に落ちないような顔は。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B45():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B45)
    WaitChrThread(0x102, 1)

    def lambda_1B56():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B56)
    WaitChrThread(0x103, 1)

    def lambda_1B67():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B67)
    WaitChrThread(0x109, 1)

    def lambda_1B78():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B78)
    WaitChrThread(0x104, 1)

    def lambda_1B89():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1B89)
    WaitChrThread(0x105, 1)

    def lambda_1B9A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1B9A)

    #C0055
    ChrTalk(
        0x104,
        (
            "#00305F……ど、どういうことだ？\x02\x03",

            "婆さんの所有する\x01",
            "物件だったのはいいとしても……\x02\x03",

            "#00303F俺たちゃ、確かにさっき\x01",
            "女の子と話してたよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        "#10306Fそのはずだけどね。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x109,
        (
            "#10101F……ね、念のため\x01",
            "さっきの女の子に\x01",
            "話を聞いてみましょう。\x02\x03",

            "何か事情があるのかも\x01",
            "しれませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00003Fそ、そうだな……\x02\x03",

            "#00001Fたしかリビングの奥の部屋に\x01",
            "行ってたはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "これこれ、アタシを無視して\x01",
            "話を進めるんじゃないよ。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)

    def lambda_1D4A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D4A)
    WaitChrThread(0x102, 1)

    def lambda_1D5B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D5B)
    WaitChrThread(0x103, 1)

    def lambda_1D6C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D6C)
    WaitChrThread(0x109, 1)

    def lambda_1D7D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D7D)
    WaitChrThread(0x104, 1)

    def lambda_1D8E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D8E)
    WaitChrThread(0x105, 1)

    def lambda_1D9F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D9F)

    #C0060
    ChrTalk(
        0x103,
        "#00205F………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0xB, 0x1)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x2)
    SetChrPos(0xB, 94200, 1050, 8100, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrSubChip(0xA, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrPos(0xA, 95100, 1050, 8100, 180)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(99920, 1250, -140, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 100100, 0, -1950, 0)
    SetChrPos(0x103, 100100, 0, -1950, 0)
    SetChrPos(0x102, 100100, 0, -1950, 0)
    SetChrPos(0x104, 100100, 0, -1950, 0)
    SetChrPos(0x109, 100100, 0, -1950, 0)
    SetChrPos(0x105, 100100, 0, -1950, 0)
    SetChrPos(0x8, 100100, 0, -1950, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 14)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 15)
    Sleep(500)
    OP_68(100100, 1250, 2940, 3000)
    BeginChrThread(0x104, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 17)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 18)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 19)
    WaitChrThread(0x105, 3)
    OP_6F(0x1)

    #C0061
    ChrTalk(
        0x101,
        (
            "#00005Fあ、あれ？\x01",
            "さっきの女の子はどこに……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        "#00305Fどっかに隠れてんのか……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 500)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0063
    ChrTalk(
        0x102,
        (
            "#00105Fロ、ロイド……\x01",
            "あ、あ、あれ見て……！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00005Fえ……\x02",
    )

    CloseMessageWindow()

    def lambda_2078():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2078)
    Sleep(50)

    def lambda_2088():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2088)
    Sleep(50)

    def lambda_2098():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2098)
    Sleep(50)

    def lambda_20A8():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_20A8)
    Sleep(50)

    def lambda_20B8():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_20B8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    Sleep(50)

    def lambda_20DF():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_20DF)
    OP_68(94650, 1250, 8100, 5000)
    MoveCamera(45, 24, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(19000, 5000)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(97220, 1250, 4330, 0)
    MoveCamera(24, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    OP_0D()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00005Fあの人形……\x01",
            "片方は俺たちが届けた\x01",
            "モノだけど……\x02\x03",

            "#00011Fも、もう片方って……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x105,
        "#10301Fさっきの女の子に瓜二つだね。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(100210, 1250, 1840, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    OP_93(0x8, 0x0, 0x0)
    OP_0D()

    #C0067
    ChrTalk(
        0x8,
        (
            "……アンタたち。\x01",
            "いい加減アタシにも\x01",
            "事情を説明したらどうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "事と次第によっちゃ、\x01",
            "不法侵入で訴えてもいいんだよ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_228F():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_228F)
    Sleep(50)

    def lambda_229F():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_229F)
    Sleep(50)

    def lambda_22AF():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_22AF)
    Sleep(50)

    def lambda_22BF():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22BF)
    Sleep(50)

    def lambda_22CF():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_22CF)
    Sleep(50)

    def lambda_22DF():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_22DF)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    #C0069
    ChrTalk(
        0x101,
        (
            "#00006Fわ、わかりました。\x01",
            "実は、その……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "荷物を届けに訪れたことと、\x01",
            "出迎えた少女が人形の片方に\x01",
            "瓜二つなことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0071
    ChrTalk(
        0x8,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "……ヒヒャヒャ、なるほどねえ。\x01",
            "ヤツの言っていたような事が\x01",
            "まさに起こったってわけだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    Sleep(1000)

    #C0073
    ChrTalk(
        0x109,
        "#10105Fえ、えっと……どういうことですか？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "そこの人形の片方はね、\x01",
            "昔、アタシが外国で\x01",
            "仕入れてきたモンさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "どこぞの旧い名家の娘たちに\x01",
            "似せて作られたという、\x01",
            "いわくつきの物でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "娘たちは双子だったから\x01",
            "２体１組の人形が作られたそうだが、\x01",
            "入手できたのは片方だけでねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "悪い品じゃないんだが、\x01",
            "不思議と買い手がつかない\x01",
            "妙な人形だったのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00005F……えっと、その話に\x01",
            "一体何の関係が……？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        "やれやれ、意外と鈍いねえ。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "要するにだ、\x01",
            "人形がこの場所に届いたことや\x01",
            "妙な少女が現れたこと……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "それらは人形自身が\x01",
            "命を持って成したことかも\x01",
            "しれないってことさね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0082
    ChrTalk(
        0x101,
        "#00011F#4S……はあ！？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "昔から『人形には命が宿る』なんて\x01",
            "うそぶいてるヤツがいてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、案外本当の\x01",
            "ことだったのかもしれないねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28E8")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "前編の人形工房クエストを？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",            # 0
            "【クリアしている】\x01",        # 1
            "【クリアしていない】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28D4")
    OP_29(0x30, 0x4, 0x10)
    Jump("loc_28E8")

    label("loc_28D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E8")
    OP_29(0x30, 0x3, 0x10)

    label("loc_28E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2963")

    #C0086
    ChrTalk(
        0x101,
        (
            "#00005F命が宿るって……\x02\x03",

            "#00003Fた、確かに以前ヨルグ老人\x01",
            "そんなことを言ってたような\x01",
            "気がしますけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B6")

    label("loc_2963")


    #C0087
    ChrTalk(
        0x101,
        (
            "#00005F命が宿るって……\x02\x03",

            "#00006Fさすがにありえない\x01",
            "話のような気がしますけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B6")


    #C0088
    ChrTalk(
        0x102,
        (
            "#00105Fそ、それじゃあ……\x01",
            "人形のお化けが出たって\x01",
            "ことですか！？\x02\x03",

            "#00106Fそ、そんな事って……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A1D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A1D)
    Sleep(300)

    #C0089
    ChrTalk(
        0x103,
        (
            "#00203Fまあ、真偽はともかく……\x02\x03",

            "#00200Fどうやらこの屋敷は\x01",
            "何らかの霊的な“場”と\x01",
            "なっているようです。\x02\x03",

            "例の《塔》や《僧院》と同じ、\x01",
            "上位三属性の気配というか……\x02\x03",

            "それが何らかの霊的な現象を\x01",
            "引き起こしたのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B0F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B0F)
    Sleep(50)

    def lambda_2B1F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B1F)
    Sleep(50)

    def lambda_2B2F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B2F)
    Sleep(50)

    def lambda_2B3F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2B3F)
    Sleep(50)

    def lambda_2B4F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B4F)
    WaitChrThread(0x105, 1)

    #C0090
    ChrTalk(
        0x102,
        "#00105Fれ、霊的って……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x105,
        (
            "#10302Fそれでなんだか\x01",
            "様子がおかしかったわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        (
            "#00301Fにわかには信じられねえ\x01",
            "話だと思ったが……\x02\x03",

            "#00306Fティオすけが言うと\x01",
            "マジに思えてくるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x109,
        (
            "#10112Fま、まさかって\x01",
            "感じですけどね……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……！\x01",
            "なかなかリアクションが\x01",
            "いいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C87():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2C87)
    Sleep(50)

    def lambda_2C97():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2C97)
    Sleep(50)

    def lambda_2CA7():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2CA7)
    Sleep(50)

    def lambda_2CB7():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CB7)
    Sleep(50)

    def lambda_2CC7():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2CC7)
    Sleep(50)

    def lambda_2CD7():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2CD7)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    #C0095
    ChrTalk(
        0x8,
        (
            "ま、所詮は世捨て人の戯言だし\x01",
            "信じようも信じまいも\x01",
            "アンタたちの勝手だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        "一つだけ、確かなことがあるよ。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#00005Fそ、それは……？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "あの姉妹人形が揃った今、\x01",
            "やっとこさ買い手がつくかも\x01",
            "しれないってことさね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……\x01",
            "こりゃあとんだ拾いモン\x01",
            "だったねえ。\x02",
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
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x104,
        "#00306F身も蓋もない婆さんだなあ……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#00006Fま、まあともかく……\x01",
            "これで荷物は届け終わったんだ。\x02\x03",

            "#00000Fカプア特急便の人に、\x01",
            "報告に行くとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#00106Fそ、そうね。\x01",
            "早く行きましょう……！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("t3510", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_7D7 end

    def Function_6_2F8C(): pass

    label("Function_6_2F8C")


    def lambda_2F91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F91)

    def lambda_2FA2():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FA2)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 3150, 0, 3230, 2000, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    Return()

    # Function_6_2F8C end

    def Function_7_2FD7(): pass

    label("Function_7_2FD7")


    def lambda_2FDC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2FDC)

    def lambda_2FED():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FED)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 3000, 0, 2100, 2000, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Return()

    # Function_7_2FD7 end

    def Function_8_3022(): pass

    label("Function_8_3022")


    def lambda_3027():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3027)

    def lambda_3038():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3038)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 2140, 0, 3620, 2000, 0x0)
    OP_93(0x103, 0x2D, 0x1F4)
    Return()

    # Function_8_3022 end

    def Function_9_306D(): pass

    label("Function_9_306D")


    def lambda_3072():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3072)

    def lambda_3083():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3083)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 1840, 0, 2420, 2000, 0x0)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_9_306D end

    def Function_10_30B8(): pass

    label("Function_10_30B8")


    def lambda_30BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_30BD)

    def lambda_30CE():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_30CE)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 900, 30, 2330, 2000, 0x0)
    OP_93(0x109, 0x2D, 0x1F4)
    Return()

    # Function_10_30B8 end

    def Function_11_3103(): pass

    label("Function_11_3103")


    def lambda_3108():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3108)

    def lambda_3119():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3119)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 1900, 30, 1240, 2000, 0x0)
    OP_93(0x105, 0x2D, 0x1F4)
    Return()

    # Function_11_3103 end

    def Function_12_314E(): pass

    label("Function_12_314E")

    OP_97(0xB, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_97(0xB, 0xFFFFE34A, 0x0, 0x0, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_97(0xB, 0x0, 0x0, 0x60E, 0x7D0, 0x0)
    Return()

    # Function_12_314E end

    def Function_13_31A3(): pass

    label("Function_13_31A3")


    def lambda_31A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_31A8)

    def lambda_31B9():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31B9)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 100000, 30, 4000, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_13_31A3 end

    def Function_14_31EE(): pass

    label("Function_14_31EE")


    def lambda_31F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_31F3)

    def lambda_3204():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3204)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 98890, 30, 3530, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_14_31EE end

    def Function_15_3239(): pass

    label("Function_15_3239")


    def lambda_323E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_323E)

    def lambda_324F():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_324F)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 101030, 30, 3100, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_15_3239 end

    def Function_16_3284(): pass

    label("Function_16_3284")


    def lambda_3289():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3289)

    def lambda_329A():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_329A)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 99700, 30, 2800, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_16_3284 end

    def Function_17_32CF(): pass

    label("Function_17_32CF")


    def lambda_32D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_32D4)

    def lambda_32E5():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_32E5)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 99500, 0, 1800, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_17_32CF end

    def Function_18_331A(): pass

    label("Function_18_331A")


    def lambda_331F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_331F)

    def lambda_3330():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3330)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 100860, 0, 1800, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_18_331A end

    def Function_19_3365(): pass

    label("Function_19_3365")


    def lambda_336A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_336A)

    def lambda_337B():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_337B)
    WaitChrThread(0x8, 1)
    OP_95(0x8, 100000, 0, 500, 2000, 0x0)
    Return()

    # Function_19_3365 end

    SaveToFile()

Try(main)
