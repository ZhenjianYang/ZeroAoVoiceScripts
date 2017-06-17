from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t152b.bin",                # FileName
        "t152b",                    # MapName
        "t152b",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 1, 0, 2],
    )

    BuildStringList((
        "t152b",                  # 0
        "マフィア",               # 1
        "マフィア",               # 2
        "看護師メイファ",         # 3
        "看護師シロン",           # 4
        "セシル",                 # 5
        "bt152b",                 # 6
    ))

    ATBonus("ATBonus_22C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_26C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_270", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_274", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_300", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_304", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_30C", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt152b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31103.dat", "ms67101.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch29800.itc",                   # 00
        "chr/ch29900.itc",                   # 01
        "apl/ch50362.itc",                   # 02
        "apl/ch50363.itc",                   # 03
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(204550,  0,       53200,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(204550,  0,       52250,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  100.0,                 9.0,                   -1.0,                  144.0,                 [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -12.5,                 -3.0,                  0.20000001788139343,   1.0])

    DeclActor(155770,  0,       53330,   1500,    155770,  1500,    53330,   0x007C, 0,  14, 0x0000)

    ScpFunction((
        "Function_0_38C",          # 00, 0
        "Function_1_444",          # 01, 1
        "Function_2_46E",          # 02, 2
        "Function_3_4B2",          # 03, 3
        "Function_4_4E2",          # 04, 4
        "Function_5_629",          # 05, 5
        "Function_6_745",          # 06, 6
        "Function_7_2BB4",         # 07, 7
        "Function_8_2BFA",         # 08, 8
        "Function_9_2C17",         # 09, 9
        "Function_10_2C32",        # 0A, 10
        "Function_11_2C51",        # 0B, 11
        "Function_12_2F20",        # 0C, 12
        "Function_13_2F9B",        # 0D, 13
        "Function_14_3424",        # 0E, 14
    ))


    def Function_0_38C(): pass

    label("Function_0_38C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3CC"),
        (1, "loc_3D8"),
        (2, "loc_3E4"),
        (3, "loc_3F0"),
        (4, "loc_3FC"),
        (5, "loc_408"),
        (6, "loc_414"),
        (SWITCH_DEFAULT, "loc_420"),
    )


    label("loc_3CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_3D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_3E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_3F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_3FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_408")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_414")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_420")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_42C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_443")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_443")

    Return()

    # Function_0_38C end

    def Function_1_444(): pass

    label("Function_1_444")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45E")
    Event(0, 13)

    label("loc_45E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_46D")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 6)

    label("loc_46D")

    Return()

    # Function_1_444 end

    def Function_2_46E(): pass

    label("Function_2_46E")

    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A0")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B1")
    Call(0, 12)

    label("loc_4B1")

    Return()

    # Function_2_46E end

    def Function_3_4B2(): pass

    label("Function_3_4B2")

    TalkBegin(0xFE)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "マフィアは気を失っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_3_4B2 end

    def Function_4_4E2(): pass

    label("Function_4_4E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CF")

    #C0002
    ChrTalk(
        0xFE,
        (
            "私たち、勤務が終わったから\x01",
            "部屋でおしゃべりしてたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "いきなり黒服の人や犬が入ってきて、\x01",
            "怖くて身動きがとれなかったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "あなたたちが来てくれて\x01",
            "ようやく安心できたわ。\x01",
            "ありがとう、礼を言うわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_625")

    label("loc_5CF")

    TurnDirection(0xFE, 0xB, 0)

    #C0005
    ChrTalk(
        0xFE,
        (
            "……まだ外に黒服や犬が\x01",
            "うろついてるのね……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "シロン、離れちゃだめよ。\x02",
    )

    CloseMessageWindow()

    label("loc_625")

    TalkEnd(0xFE)
    Return()

    # Function_4_4E2 end

    def Function_5_629(): pass

    label("Function_5_629")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E3")

    #C0007
    ChrTalk(
        0xFE,
        (
            "セシル先輩や他の看護師さんたちは、\x01",
            "夜勤のシフトで病棟に残っているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "が、頑張って助けてあげてください。\x01",
            "私はメイファちゃんと\x01",
            "ここに隠れてますから……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_741")

    label("loc_6E3")


    #C0009
    ChrTalk(
        0xFE,
        (
            "はぁ～…………\x01",
            "安心したら気が抜けちゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "あ、あれ……\x01",
            "脚が震えて動かない……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_741")

    TalkEnd(0xFE)
    Return()

    # Function_5_629 end

    def Function_6_745(): pass

    label("Function_6_745")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    LoadChrToIndex("apl/ch50411.itc", 0x1F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05500.itp")
    OP_68(151770, 800, 52760, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21940, 0)
    SetChrPos(0x101, 148870, 0, 55580, 45)
    SetChrPos(0x102, 149220, 0, 54230, 0)
    SetChrPos(0x104, 151350, 0, 55460, 315)
    SetChrPos(0x103, 150150, 100, 57600, 270)
    SetChrFlags(0x103, 0x2)
    SetChrFlags(0x103, 0x10)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x1F)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, 150080, 0, 55940, 0)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    FadeToBright(1000, 0)
    OP_68(150040, 800, 56760, 4000)
    OP_6F(0x79)
    OP_0D()

    #C0011
    ChrTalk(
        0xC,
        (
            "#1309F#11Pふふ……\x01",
            "良かったわね、ただの貧血で。\x02\x03",

            "#1300Fしばらくしたら\x01",
            "すぐに目を覚ますと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#0006F#6Pそっか……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        "#0102F#12Pよ、良かった……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        (
            "#0306F#11Pああ……\x01",
            "どうなる事かと思ったぜ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0015
    ChrTalk(
        0xC,
        (
            "#1306F#11Pでも、ごめんなさい。\x01",
            "私のベッドを使わせて。\x02\x03",

            "#1301Fちょうど病棟の方に\x01",
            "空いている個室がなくて……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9AE():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9AE)
    Sleep(50)

    def lambda_9BE():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9BE)
    Sleep(300)

    #C0016
    ChrTalk(
        0x101,
        (
            "#0002F#6Pいや、助かったよ。\x02\x03",

            "ここの方がティオも\x01",
            "落ち着けるかもしれないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        (
            "#0104F#12Pセシルさん……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)

    #C0018
    ChrTalk(
        0xC,
        (
            "#1309F#5Pふふ、気にしないで。\x02\x03",

            "#1300F今夜は私も夜勤があるし、\x01",
            "何だったらこのまま朝まで\x01",
            "寝てもらっても構わないから。\x02\x03",

            "それじゃ、私は失礼するわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#0002F#6Pあ、うん……お疲れさま。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        (
            "#0302F#11Pあざーす！\x01",
            "お疲れさまでした！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(150040, 800, 55260, 3000)

    def lambda_B5A():

        label("loc_B5A")

        TurnDirection(0x101, 0xC, 500)
        Yield()
        Jump("loc_B5A")

    QueueWorkItem2(0x101, 1, lambda_B5A)

    def lambda_B6C():

        label("loc_B6C")

        TurnDirection(0x102, 0xC, 500)
        Yield()
        Jump("loc_B6C")

    QueueWorkItem2(0x102, 1, lambda_B6C)

    def lambda_B7E():

        label("loc_B7E")

        TurnDirection(0x104, 0xC, 500)
        Yield()
        Jump("loc_B7E")

    QueueWorkItem2(0x104, 1, lambda_B7E)
    BeginChrThread(0xC, 3, 0, 7)
    WaitChrThread(0xC, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_6F(0x79)
    Sleep(1000)

    def lambda_BB5():
        OP_92(0xFE, 0x24A40, 0xD890, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BB5)
    WaitChrThread(0x102, 1)
    OP_68(150000, 800, 57600, 3500)
    MoveCamera(33, 21, 0, 3500)

    def lambda_BE8():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE8)

    def lambda_BF5():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BF5)

    def lambda_C02():
        OP_95(0xFE, 150080, 0, 55440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C02)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    TurnDirection(0x102, 0x103, 500)
    OP_6F(0x79)

    #C0021
    ChrTalk(
        0x101,
        (
            "#0008F#6P……ティオ……\x01",
            "もう少し早く気付ければ……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#0106F#12P考えてみれば、ヨアヒム先生の\x01",
            "話を聞いている最中くらいから\x01",
            "様子がおかしかったものね……\x02\x03",

            "#0108Fそれも確か……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#0306F#11P悪魔を崇拝する連中が\x01",
            "造ったっていう薬の話か……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)

    #C0024
    ChrTalk(
        0x103,
        (
            "#5P#40W#2S──いいですよ。\x01",
            "何を聞いてくれても……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    BeginChrThread(0x103, 0, 0, 8)
    OP_0D()
    Sleep(500)

    #C0025
    ChrTalk(
        0x101,
        "#0002F#6Pティオ……起きたのか。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        "#0102F#12Pよかった……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0304F#12Pったく……\x01",
            "心配かけやがって。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x103, 0x0)
    Fade(250)
    Sound(1276, 255, 90, 0)    #voice#Tio
    Sound(804, 0, 100, 0)
    OP_A1(0x103, 0x3E8, 0x6, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23)
    OP_0D()
    Sleep(300)
    OP_A1(0x103, 0x3E8, 0x5, 0x24, 0x25, 0x1A, 0x1B, 0x1C)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(800)

    #A0028
    AnonymousTalk(
        0x103,
        (
            "#40Wあまり……\x01",
            "気を遣わないで下さい。\x02\x03",

            "薬物捜査に携わる人間として\x01",
            "皆さんは聞く必要がある……\x02\x03",

            "わたしの知っている情報を。\x02",
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
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0029
    ChrTalk(
        0x101,
        (
            "#0006F#6P……あのな、ティオ。\x02\x03",

            "#0000F俺たちがティオの気の進まない話を\x01",
            "わざわざ聞こうとすると思うのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        "#5505F#5P#40Wえ……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        (
            "#0100F#12Pもちろん捜査も大事だけど\x01",
            "それとこれとは話が全く別よ。\x02\x03",

            "#0104F私たちにとって、あなたは\x01",
            "同じ仕事に携わる同僚だけど……\x02\x03",

            "#0102Fそれ以前に、何よりも\x01",
            "代えがたい仲間だと思っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        "#5508F#5P#40W……ぁ………\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#0300F#12P他人には秘めておきたい\x01",
            "そいつならではの事情はあるさ。\x02\x03",

            "#0306Fま、俺の過去については\x01",
            "ちょいとばかりバレちまったが……\x02\x03",

            "#0303Fティオすけ、お前がそれを\x01",
            "知られたくねぇってんなら……\x02\x03",

            "#0302F俺らは全力でお前に協力するさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        "#5506F#5P#40Wエリィさん……ランディさん……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#0000F#6P……そういう事だ。\x02\x03",

            "#0003Fでも、もしティオが\x01",
            "俺たちに話したいんだったら……\x02\x03",

            "話すことで少しでも気持ちを\x01",
            "軽くできるんだったら……\x02\x03",

            "#0002Fだったらその重荷は\x01",
            "ぜひ受け持たせて欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#5508F#5P#40W……ロイドさん………\x02\x03",

            "#5510F#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    Sleep(500)

    #C0037
    ChrTalk(
        0x103,
        (
            "#5504F#5P#30Wふふ……よくそんなに\x01",
            "恥ずかしい台詞を言えますね。\x02\x03",

            "ロイドさんだけでなく、\x01",
            "エリィさんもランディさんも……\x02\x03",

            "#5511Fお２人ともロイドさんに\x01",
            "影響されてるんじゃないですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#0309F#12Pハハ、そうかもな。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#0104F#12Pうーん、確かに\x01",
            "否定はできないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#0006F#6P否定してくれよ……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    #C0041
    ChrTalk(
        0x103,
        "#5509F#5P#40W……ふふ…………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    Sound(820, 0, 100, 0)
    SetChrPos(0x103, 150000, 200, 56750, 270)
    OP_A1(0x103, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_0D()
    Sleep(500)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    Sleep(500)

    #C0042
    ChrTalk(
        0x103,
        (
            "#5506F#5Pロイドさんには\x01",
            "前に少し話しましたが……\x02\x03",

            "わたしは５歳の頃、\x01",
            "両親と離れ離れになりました。\x02\x03",

            "#5508Fとある狂信的な宗教団体に\x01",
            "拉致されることによって……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    SetCameraDistance(21000, 100000)

    #C0043
    ChrTalk(
        0x101,
        "#0013F#6P！？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#0101F#12Pあ……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        "#0310F#12P……そいつは……\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x3, 0x2, 0x1, 0x0)
    Sleep(300)

    #C0046
    ChrTalk(
        0x103,
        (
            "#5508F#5Pその教団の真の教義や目的は\x01",
            "今でも判らないそうですが……\x02\x03",

            "ただ彼らは、女神を否定し、\x01",
            "悪魔を崇拝することで\x01",
            "何かを得ようとしていました。\x02\x03",

            "#5506Fわたしを含めた他の子供たちは……\x01",
            "その“供物#4Rくもつ#”だったんだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#0001F#6P供物……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        (
            "#5502F#5P供物といっても\x01",
            "生贄とかじゃありません……\x02\x03",

            "#5506F……そんな目に遭った子も\x01",
            "いたのかもしれませんが……\x02\x03",

            "その教団は、幾つもの拠点#4Rロッジ#を持ち\x01",
            "ロッジごとに様々な方法での\x01",
            "“儀式”を試みていたようでした。\x02\x03",

            "#5508Fそしてわたしが連れて行かれた\x01",
            "ロッジで行われていたのは……\x02\x03",

            "“儀式”という名の人体実験でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#0107F#12Pじ、人体実験……！？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        (
            "#0301F#12Pひょっとして、\x01",
            "お前の感応力のことか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sleep(300)

    #C0051
    ChrTalk(
        0x103,
        (
            "#5503F#5P#30W……はい。\x02\x03",

            "薬物を投与され……\x01",
            "全身にセンサーを付けられ……\x02\x03",

            "考え付く限りのやり方で\x01",
            "五感を高める試みが行われました。\x02\x03",

            "#5508F更には強制的な暗示と\x01",
            "精神的な負荷をかけることで\x01",
            "霊感のようなものまで高められ……\x02\x03",

            "３年間……\x01",
            "それが毎日のように続きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#0013F#6P………あ…………\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        "#0108F#12P……そ、そんな…………\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        "#0303F#12P………………………………\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x2, 0x2A, 0x2B)

    #C0055
    ChrTalk(
        0x103,
        (
            "#5502F#5P#30Wそれでもわたしは……\x01",
            "幸運な方だったかもしれません。\x02\x03",

            "わたし以外の子は……\x01",
            "全員が耐え切れませんでした。\x02\x03",

            "#5508F一人、また一人と\x01",
            "周りから子供がいなくなって……\x02\x03",

            "ついに一人になった頃、\x01",
            "わたしは手に入れていました……\x02\x03",

            "#5506F分厚い岩壁の向こうで\x01",
            "他の子たちが上げた最期の悲鳴を\x01",
            "聴き取れるくらいの感応力を……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#0010F#6P……っ……！！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#0106F#12Pティオ……ちゃん……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        "#0308F#12P……外道どもが………\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        "#5508F#5P#40W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x7, 0x2B, 0x2A, 0x4, 0x3, 0x2, 0x1, 0x0)

    #C0060
    ChrTalk(
        0x103,
        (
            "#5502F#5P──そんな時でした。\x02\x03",

            "わたしのいたロッジに\x01",
            "ロイドさんのお兄さんが……\x01",
            "ガイさんが乗り込んできたのは。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x101,
        "#0011F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        (
            "#5503F#5Pガイさんを含めたチームは\x01",
            "教団の信者たちを無力化しながら\x01",
            "ロッジを制圧していきました。\x02\x03",

            "抵抗は激しく、制圧された途端、\x01",
            "自決する者が殆んどだったそうです。\x02\x03",

            "#5508Fそうした屍を踏み越えながら\x01",
            "“儀式の間”にたどり着いて……\x02\x03",

            "ガイさんは、ただ一人の\x01",
            "生き残った子供を発見しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#0008F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        (
            "#5506F#5Pガイさんに保護された時……　\x01",
            "わたしは衰弱しきっていました。\x02\x03",

            "そしてこの病院に連れて来られ、\x01",
            "数ヶ月のあいだ療養して……\x02\x03",

            "#5508F……そこから先は以前、\x01",
            "ロイドさんに話したとおりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#0003F#6P……そうか………\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        "#0106F#12P……ティオちゃん………\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sleep(300)

    #C0067
    ChrTalk(
        0x103,
        (
            "#5504F#5P……皮肉なものですね。\x02\x03",

            "あれだけお世話になって\x01",
            "感謝していた人だったのに……\x02\x03",

            "#5502F３年前、ガイさんが\x01",
            "亡くなった事を聞かされた時、\x01",
            "わたしは余り哀しくなかったんです。\x02\x03",

            "#5508Fまるで、手に入れた力と引き換えに\x01",
            "人間らしい感情を失ったような……\x02\x03",

            "そんな不思議な感慨すらありました。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0008F#6Pティオ……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        "#0308F#12P………………………………\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x103,
        (
            "#5504F#5P……多分わたしは\x01",
            "聞きたかったんだと思います。\x02\x03",

            "眩しいくらいに前向きで\x01",
            "力強かったあの人に……\x02\x03",

            "わたしのような“欠けた存在”が\x01",
            "どう生きたらいいのかを……\x02\x03",

            "#5508Fでも結局、その答えは聞けず、\x01",
            "エプスタイン財団に引き取られて……\x02\x03",

            "そして支援課に来て、\x01",
            "皆さんと一緒に暮らしていて……\x02\x03",

            "#5506F#40Wやっぱり……\x01",
            "今でもよく分からないんです。\x02\x03",

            "#40Wどう、生きたらいいのか……\x02\x03",

            "#40W……どうして……\x01",
            "わたしが生きているのか。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0071
    ChrTalk(
        0x102,
        "#0101F#12P……ティオちゃん……！\x02",
    )

    CloseMessageWindow()
    OP_68(150220, 800, 57570, 1200)
    BeginChrThread(0x102, 3, 0, 10)
    WaitChrThread(0x102, 3)
    StopBGM(0xFA0)
    Sleep(500)
    OP_A1(0x103, 0x3E8, 0x3, 0x5, 0x6, 0x7)
    Sleep(300)
    Fade(1000)
    SetCameraDistance(20500, 0)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrSubChip(0x103, 0x8)
    Sound(820, 0, 100, 0)
    OP_0D()
    #Sound(1269, 255, 65, 0)    #voice#Tio

    #C0072
    ChrTalk(
        0x103,
        "#5P#30W……あ………\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x4, 0x8, 0x9, 0xA, 0x9)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)

    #N0073
    NpcTalk(
        0x103,
        "エリィ",
        (
            "#0103F#11Pいいじゃない……！\x01",
            "分からなくったって……！\x02\x03",

            "#0107Fそんなのは私たちだって\x01",
            "あなたと同じなんだから……！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x103,
        "#5505F#5P#30W………え…………\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#0003F#6P……なぜ生きてるのか、\x01",
            "どう生きればいいのか……\x02\x03",

            "そんなのが判ってる人間なんて\x01",
            "そうそういるもんじゃないさ。\x02\x03",

            "#0000F俺も、エリィも、ランディも。\x01",
            "誰だって同じさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#0304F#12Pハハ、俺なんざ特に、\x01",
            "自分の道を見失った口だが……\x02\x03",

            "#0302Fそれでもティオすけ。\x01",
            "お前、真面目すぎるんだよ。\x02\x03",

            "そんな難しい問題を\x01",
            "急いで解いてどうするんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x3, 0xA, 0xB, 0xC)

    #C0077
    ChrTalk(
        0x103,
        "#5506F#5P#30W……で、でも………\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#0004F#6Pそれでも気になるなら……\x01",
            "答えを探し続ければいい。\x02\x03",

            "ただ、焦る必要はないし、\x01",
            "一人で探す必要だってないんだ。\x02\x03",

            "#0000F俺たちが一緒に探すからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        "#5508F#5P#40W………ぁ……………\x02",
    )

    CloseMessageWindow()

    #N0080
    NpcTalk(
        0x103,
        "エリィ",
        (
            "#0104F#11Pもちろん私もよ……\x02\x03",

            "ランディだって課長だって\x01",
            "キーアちゃんやツァイトだって\x01",
            "みんな力になってくれるわ……\x02\x03",

            "あなたが、その難しい問題の\x01",
            "答えを見つけられるのを……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        "#5510F#5P#40W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_A1(0x103, 0x3E8, 0x4, 0xF, 0x10, 0x11, 0x12)

    #C0082
    ChrTalk(
        0x103,
        (
            "#5508F#5P#40W……エリィさんもランディさんも\x01",
            "ロイドさんに感化されたみたいに……\x02\x03",

            "#5513F本当に……聞いてるこちらが……\x01",
            "恥ずかしくなってきてしまいます……\x02\x03",

            "……どうしてそんな………\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0309F#12Pま、それも巡り合わせだろ。\x02\x03",

            "支援課を選んじまった時点で\x01",
            "俺たちは同じ、誰かさんの被害者だ。\x02",
        )
    )

    CloseMessageWindow()

    #N0084
    NpcTalk(
        0x103,
        "エリィ",
        (
            "#0109F#11Pふふっ、そうね……\x02\x03",

            "#0102Fそういう恥ずかしい思いも\x01",
            "分かち合ってもらわないとね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0085
    ChrTalk(
        0x101,
        (
            "#0012F#6Pなんで俺が加害者になってるのか\x01",
            "分からないけど……\x02\x03",

            "#0000Fまあ、分かち合うってのは\x01",
            "俺も賛成だよ。\x02\x03",

            "#0004F恥ずかしい思いだけじゃなく、\x01",
            "辛い思いや、苦しい思い……\x02\x03",

            "それからもちろん、\x01",
            "嬉しい思いや、楽しい思いも。\x02\x03",

            "#0002Fそれが“仲間”ってもんだろ？\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x3, 0x12, 0x13, 0x14)
    #Sound(1277, 255, 100, 0)    #voice#Tio
    OP_A1(0x103, 0x5DC, 0x4, 0x15, 0x16, 0x17, 0x16)
    OP_A1(0x103, 0x5DC, 0x4, 0x15, 0x16, 0x17, 0x16)
    OP_A1(0x103, 0x5DC, 0x4, 0x15, 0x16, 0x17, 0x16)
    Sleep(150)

    #C0086
    ChrTalk(
        0x103,
        (
            "#5512F#5P#40W……ああもう………\x02\x03",

            "恥ずかしくて……暑苦しくて……\x01",
            "……こんなに居たたまれないのに……\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x4, 0x17, 0x18, 0x19, 0x18)
    Sleep(150)

    #C0087
    ChrTalk(
        0x103,
        (
            "#5513F#5P#40W……でも……\x01",
            "何だか悪くない気分です……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 0, 0, 9)
    FadeToDark(2000, 0, -1)
    SetCameraDistance(22000, 3000)
    OP_6F(0x10)
    OP_0D()
    Sleep(1000)
    SetChrName("")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちはティオと共に\x01",
            "バスに乗って夜のクロスベル市へと戻った。\x02\x03",

            "支援課に戻って、疲れたティオを\x01",
            "自室で早めに休ませた後……\x02\x03",

            "ロイドたちは改めてセルゲイと話をする事にした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    EndChrThread(0x103, 0x3)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x2)
    ClearChrFlags(0x103, 0x10)
    ClearChrFlags(0x103, 0x4)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 6)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_745 end

    def Function_7_2BB4(): pass

    label("Function_7_2BB4")


    def lambda_2BB9():
        OP_95(0xFE, 150120, 0, 49160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BB9)
    Sleep(2700)
    Sound(103, 0, 100, 0)
    Sleep(300)

    def lambda_2BDF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BDF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sound(104, 0, 100, 0)
    Return()

    # Function_7_2BB4 end

    def Function_8_2BFA(): pass

    label("Function_8_2BFA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C16")
    OP_A1(0xFE, 0x3E8, 0x3, 0x1F, 0x1E, 0x1D)
    Sleep(4000)
    Jump("Function_8_2BFA")

    label("loc_2C16")

    Return()

    # Function_8_2BFA end

    def Function_9_2C17(): pass

    label("Function_9_2C17")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C31")
    OP_A1(0xFE, 0x3E8, 0x4, 0x15, 0x16, 0x17, 0x16)
    Jump("Function_9_2C17")

    label("loc_2C31")

    Return()

    # Function_9_2C17 end

    def Function_10_2C32(): pass

    label("Function_10_2C32")


    def lambda_2C37():
        OP_96(0xFE, 0x24BBC, 0x0, 0xDB92, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C37)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_2C32 end

    def Function_11_2C51(): pass

    label("Function_11_2C51")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("chr/ch31000.itc", 0x23)
    LoadChrToIndex("chr/ch31050.itc", 0x24)
    LoadChrToIndex("chr/ch31051.itc", 0x25)
    LoadChrToIndex("chr/ch31100.itc", 0x26)
    LoadChrToIndex("chr/ch31150.itc", 0x27)
    LoadChrToIndex("chr/ch31151.itc", 0x28)
    OP_68(99060, 1000, 12500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 97690, 0, 11720, 270)
    SetChrPos(0x102, 98330, 0, 10890, 270)
    SetChrPos(0x103, 99270, 0, 12710, 270)
    SetChrPos(0x104, 100540, 0, 12610, 270)
    SetChrPos(0x106, 99810, 0, 10770, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, 85000, 0, 12690, 90)
    SetChrPos(0x9, 85000, 0, 11100, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(92640, 1000, 12400, 0)
    OP_68(97340, 1000, 12400, 1750)
    SetCameraDistance(17500, 1750)

    def lambda_2E33():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2E33)

    def lambda_2E48():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2E48)
    Sleep(750)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(500)
    Battle("BattleInfo_30C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Call(0, 12)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    SetChrPos(0x0, 98700, 0, 11800, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE1, 1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_2C51 end

    def Function_12_2F20(): pass

    label("Function_12_2F20")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x8, 93740, 0, 13280, 270)
    SetChrPos(0x9, 94870, 0, 10340, 90)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_12_2F20 end

    def Function_13_2F9B(): pass

    label("Function_13_2F9B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(200880, 900, 52400, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 199450, 0, 49200, 0)
    SetChrPos(0x102, 200570, 0, 49200, 0)
    SetChrPos(0x103, 199450, 0, 47900, 0)
    SetChrPos(0x104, 200570, 0, 47900, 0)
    SetChrPos(0x106, 200000, 0, 46600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    FadeToBright(1000, 0)
    OP_68(201940, 900, 53610, 3000)

    def lambda_3092():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3092)

    def lambda_30A7():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30A7)

    def lambda_30BC():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_30BC)

    def lambda_30D1():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30D1)

    def lambda_30E6():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_30E6)
    Sleep(200)

    def lambda_30FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30FE)

    def lambda_310F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_310F)
    Sleep(500)

    def lambda_3123():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3123)

    def lambda_3134():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3134)
    Sleep(500)

    def lambda_3148():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3148)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_3161():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3161)

    def lambda_316E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_316E)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_3183():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3183)

    def lambda_3190():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3190)
    WaitChrThread(0x106, 1)

    def lambda_31A1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_31A1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_321E():
        TurnDirection(0xFE, 0x101, 600)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_321E)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3240():
        TurnDirection(0xFE, 0x101, 600)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3240)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)

    #C0089
    ChrTalk(
        0xA,
        "#5Pひっ……！\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xB,
        "#11Pや、やだっ……！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        (
            "#0100F#6P安心してください。\x01",
            "私たちは警察の人間です。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0092
    ChrTalk(
        0xB,
        "#11Pお、女のヒト……？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "#5P警察の人って……\x01",
            "助けに来てくれたの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        (
            "#0103F#6Pええ、侵入者を制圧しながら\x01",
            "安全を確保している状況です。\x02\x03",

            "#0101Fどうかしばらくの間、\x01",
            "ここで待っていてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        "#5Pわ、わかったわ。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xB,
        "#11Pが、頑張ってください～！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    SetChrPos(0x0, 200200, 0, 52410, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0xE1, 2)
    OP_29(0x4D, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_13_2F9B end

    def Function_14_3424(): pass

    label("Function_14_3424")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetChrName("")

    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セシルとロイド、\x01",
            "そして精悍な顔つきの青年が写った\x01",
            "写真が立てかけられている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3551")

    #A0098
    AnonymousTalk(
        0x101,
        (
            "#0008F（……セシル姉と\x01",
            "  兄貴と撮った写真だ。）\x02\x03",

            "（俺も肌身離さず持ってるけど、\x01",
            "  セシル姉も飾ってたんだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35DA")

    label("loc_3551")


    #A0099
    AnonymousTalk(
        0x101,
        (
            "#0005F（あ……セシル姉と\x01",
            "  兄貴と撮った写真だ。）\x02\x03",

            "#0003F（この写真があるって事は\x01",
            "  もしかしてここが\x01",
            "  セシル姉の寮部屋なのかな？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35DA")

    SetScenarioFlags(0x69, 5)

    label("loc_35DD")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_14_3424 end

    SaveToFile()

Try(main)
