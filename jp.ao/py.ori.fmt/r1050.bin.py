from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1050.bin",                # FileName
        "r1050",                    # MapName
        "r1050",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x05,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 1, 0, 2],
    )

    BuildStringList((
        "r1050",                  # 0
        "ソーニャ司令",           # 1
        "ドノバン警部",           # 2
        "グレイス",               # 3
        "ミレイユ三尉",           # 4
        "レイモンド捜査官",       # 5
        "レインズ",               # 6
        "警官",                   # 7
        "警官",                   # 8
        "警官",                   # 9
        "警備隊員",               # 10
        "警備隊員",               # 11
        "警備隊員",               # 12
        "警備隊員",               # 13
        "車掌",                   # 14
    ))

    AddCharChip((
        "chr/ch05700.itc",                   # 00
        "chr/ch30300.itc",                   # 01
        "chr/ch06000.itc",                   # 02
        "chr/ch32600.itc",                   # 03
        "chr/ch30200.itc",                   # 04
        "chr/ch28100.itc",                   # 05
        "chr/ch30000.itc",                   # 06
        "chr/ch31200.itc",                   # 07
        "chr/ch31300.itc",                   # 08
        "chr/ch28302.itc",                   # 09
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   4,   255,  0)

    DeclActor(-8780,   0,       -820,    3000,    -8780,   3000,    -820,    0x007C, 0,  19, 0x0000)
    DeclActor(-14130,  0,       -620,    2000,    -14130,  3000,    -620,    0x007C, 0,  20, 0x0000)
    DeclActor(-36100,  0,       9060,    3000,    -36100,  2000,    9560,    0x007C, 0,  21, 0x0000)
    DeclActor(-55520,  0,       9690,    3000,    -55520,  2000,    10190,   0x007C, 0,  22, 0x0000)
    DeclActor(-65239,  0,       9800,    3000,    -65239,  2000,    10300,   0x007C, 0,  23, 0x0000)

    ChipFrameInfo(956, 0)                                        # 0

    ScpFunction((
        "Function_0_3BC",          # 00, 0
        "Function_1_46C",          # 01, 1
        "Function_2_4A3",          # 02, 2
        "Function_3_4EC",          # 03, 3
        "Function_4_65A",          # 04, 4
        "Function_5_DA1",          # 05, 5
        "Function_6_E51",          # 06, 6
        "Function_7_10BB",         # 07, 7
        "Function_8_13FA",         # 08, 8
        "Function_9_1638",         # 09, 9
        "Function_10_1822",        # 0A, 10
        "Function_11_19A7",        # 0B, 11
        "Function_12_1C5E",        # 0C, 12
        "Function_13_1CD9",        # 0D, 13
        "Function_14_1D69",        # 0E, 14
        "Function_15_1DF6",        # 0F, 15
        "Function_16_1E80",        # 10, 16
        "Function_17_1F27",        # 11, 17
        "Function_18_1FA5",        # 12, 18
        "Function_19_2008",        # 13, 19
        "Function_20_239F",        # 14, 20
        "Function_21_26DC",        # 15, 21
        "Function_22_26EA",        # 16, 22
        "Function_23_26F8",        # 17, 23
        "Function_24_2706",        # 18, 24
        "Function_25_30AC",        # 19, 25
        "Function_26_42FB",        # 1A, 26
        "Function_27_455F",        # 1B, 27
        "Function_28_65B1",        # 1C, 28
    ))


    def Function_0_3BC(): pass

    label("Function_0_3BC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3F4"),
        (1, "loc_400"),
        (2, "loc_40C"),
        (3, "loc_418"),
        (4, "loc_424"),
        (5, "loc_430"),
        (6, "loc_43C"),
        (SWITCH_DEFAULT, "loc_448"),
    )


    label("loc_3F4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_400")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_40C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_418")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_424")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_430")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_43C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_448")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_454")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_454")

    label("loc_46B")

    Return()

    # Function_0_3BC end

    def Function_1_46C(): pass

    label("Function_1_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47D")
    Call(0, 3)

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_493")
    SetMapFlags(0x10000000)
    Event(0, 25)

    label("loc_493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4A2")
    ClearScenarioFlags(0x22, 0)
    Event(0, 27)

    label("loc_4A2")

    Return()

    # Function_1_46C end

    def Function_2_4A3(): pass

    label("Function_2_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_4B5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B5")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EB")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)

    label("loc_4EB")

    Return()

    # Function_2_4A3 end

    def Function_3_4EC(): pass

    label("Function_3_4EC")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_541")
    SetChrFlags(0xA, 0x10)

    label("loc_541")

    SetChrChipByIndex(0x15, 0x9)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56B")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x12, 0x10)

    label("loc_56B")

    SetChrPos(0x8, 4770, 0, 5830, 180)
    SetChrPos(0x9, -23110, 0, -1910, 315)
    SetChrPos(0xA, 2240, 0, -2630, 288)
    SetChrPos(0xB, -58480, 0, -11340, 225)
    SetChrPos(0xC, -29410, 0, -6490, 346)
    SetChrPos(0xD, 1110, 0, -4130, 279)
    SetChrPos(0xE, -35240, 0, -6360, 315)
    SetChrPos(0xF, -44860, 0, -8410, 77)
    SetChrPos(0x10, -56970, 160, 900, 137)
    SetChrPos(0x11, 4230, 0, 3880, 359)
    SetChrPos(0x12, 5440, 0, 3940, 359)
    SetChrPos(0x13, -59570, 0, -12240, 45)
    SetChrPos(0x14, -67820, 170, 440, 180)
    SetChrPos(0x15, -52090, 0, -18010, 98)
    Return()

    # Function_3_4EC end

    def Function_4_65A(): pass

    label("Function_4_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D01")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -50420, 0, -17890, 270)
    SetChrPos(0x102, -50870, 0, -16710, 225)
    SetChrPos(0x104, -49670, 0, -18710, 270)
    SetChrPos(0x103, -49820, 0, -17210, 270)
    SetChrPos(0x109, -50030, 0, -15940, 225)
    SetChrPos(0x105, -49100, 0, -15920, 225)
    OP_68(-48700, 2210, -19060, 0)
    MoveCamera(302, 24, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(12640, 0)
    OP_0D()
    Sleep(500)

    #C0001
    ChrTalk(
        0xFE,
        "はあ、酷い目にあったよ。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "運ばれた人たちに比べたら\x01",
            "無傷の僕はまだいいほう\x01",
            "なんだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "まさかこんな風に\x01",
            "列車が脱線するなんてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#12P#00003F列車に乗っていた\x01",
            "車掌さんみたいですね。\x02\x03",

            "#00000Fよろしければ、事故当時の事を\x01",
            "聞かせていただけませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "ああ、僕の話せることだったら\x01",
            "何でも話させてもらいたいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "さっき、あっちにいる刑事さんに\x01",
            "聞かれたときはロクな話ができなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "何しろ、あっという間の\x01",
            "出来事だったからねえ。\x01",
            "ちょっと混乱してるというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            "#12P#10106Fうーん、これだけの事故ですし\x01",
            "鮮明に思い出せなくても\x01",
            "仕方ないかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#12P#00108F事故のショックも\x01",
            "あると思いますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#12P#00003Fこの際、小さなことでも\x01",
            "構いません。\x02\x03",

            "#00001F何か気になったことは\x01",
            "ありませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "気になったこと……\x01",
            "うーん……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0012
    ChrTalk(
        0xFE,
        "あ、そういえば……！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        "#12P#00305F#6P何かあったのか？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "脱線事故の直前、運転士に\x01",
            "通信で業務連絡をしてたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "途中で突然、彼が叫んだんだ。\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0016
    ChrTalk(
        0xFE,
        "『うわあっ、なんだ！？』……ってね。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "事故が起こったのはそのすぐ後さ。\x01",
            "先頭車両が脱線して、連結車両も\x01",
            "次々とそれに続いていったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "そうして……\x01",
            "今に至るって言うわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#12P#00200F『うわあっ、なんだ！？』\x01",
            "という叫び声……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x105,
        (
            "#12P#10302Fまるで、信じられない物でも#18R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲#\x01",
            "目にしたかのような#18R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲#セリフだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#12P#00003F運転士さんは一体、\x01",
            "何を見たんだろう……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 6)
    OP_29(0xA8, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD5")
    Call(0, 26)
    Return()

    label("loc_CD5")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -50180, 0, -17560, 257)
    EventEnd(0x5)
    Jump("loc_DA0")

    label("loc_D01")

    TalkBegin(0xFE)

    #C0022
    ChrTalk(
        0xFE,
        (
            "脱線事故の直前、\x01",
            "通信で業務連絡をしてた時に\x01",
            "運転士が突然叫んだんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "『うわあっ、なんだ！？』……ってね。\x01",
            "脱線事故が起こったのはそのすぐ後さ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_DA0")

    Return()

    # Function_4_65A end

    def Function_5_DA1(): pass

    label("Function_5_DA1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_E4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBF")
    Call(0, 11)
    Jump("loc_E4D")

    label("loc_DBF")


    #C0024
    ChrTalk(
        0xFE,
        (
            "#02003F重機が来るまでは、\x01",
            "私たち警備隊も現場検証に\x01",
            "協力させてもらうわ。\x02\x03",

            "#02000F隊員たちにも\x01",
            "言い含めておいたから、\x01",
            "自由に調査して頂戴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4D")

    TalkEnd(0xFE)
    Return()

    # Function_5_DA1 end

    def Function_6_E51(): pass

    label("Function_6_E51")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1036")

    #C0025
    ChrTalk(
        0xFE,
        (
            "やれやれ、改めて見ても\x01",
            "とんでもない大事故だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "これでよく１人も死者が\x01",
            "出なかったもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        (
            "#00200Fほとんどの乗客は\x01",
            "共和国に振替輸送されるか、\x01",
            "病院に運ばれたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00006F出来ればその人たちからも\x01",
            "話を聞きたかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "まあ、仕方ないだろう。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "そうだ、向こうで休んでいる\x01",
            "車掌には話を聞いたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "さっき俺たちが話を聞いた時は\x01",
            "大した情報は得られなかったが、\x01",
            "今なら何か思い出したかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "忘れずに話を聞いておくんだな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 2)
    Jump("loc_10B7")

    label("loc_1036")


    #C0033
    ChrTalk(
        0xFE,
        (
            "向こうで休んでいる\x01",
            "車掌には話を聞いたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "すぐに事故当時の事を聞ける\x01",
            "唯一の人物だ、忘れずに\x01",
            "聞き込みをしておくんだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B7")

    TalkEnd(0xFE)
    Return()

    # Function_6_E51 end

    def Function_7_10BB(): pass

    label("Function_7_10BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1353")

    #C0035
    ChrTalk(
        0xFE,
        (
            "#02102Fどう、ロイド君。\x01",
            "何か新しいことは分かったかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00006Fいえ、まだ何とも言えませんね。\x02\x03",

            "#00001Fグレイスさんは何か、\x01",
            "気づいた事はありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "#02106Fうーん、そうねえ。\x01",
            "列車事故自体はたまにあるけど……\x02\x03",

            "#02101F今回はやっぱり、\x01",
            "タイミングと場所の両方が\x01",
            "悪すぎだと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        (
            "#00108F……そうですね。\x01",
            "ただでさえ独立提唱の関係で\x01",
            "緊張状態が続いてる時ですし……\x02\x03",

            "#00103Fもしかしたら、何らかの意図が\x01",
            "働いている可能性も……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "#02106Fま、何の証拠もない話だし\x01",
            "あたしの考えを押し付ける\x01",
            "つもりもないけどね。\x02\x03",

            "#02109Fとにかく、調査のほうは\x01",
            "頑張ってちょうだい！\x01",
            "何か分かったら取材させてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00002Fはは、分かりました。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x17B, 1)
    Jump("loc_13F6")

    label("loc_1353")


    #C0041
    ChrTalk(
        0xFE,
        (
            "#02103F列車事故自体はたまにあるけど……\x01",
            "今回はタイミングと場所が最悪ね。\x02\x03",

            "#02109Fまあとにかく、調査のほうは\x01",
            "頑張ってちょうだい！\x01",
            "何か分かったら取材させてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F6")

    TalkEnd(0xFE)
    Return()

    # Function_7_10BB end

    def Function_8_13FA(): pass

    label("Function_8_13FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CC")

    #C0042
    ChrTalk(
        0x104,
        (
            "#00300Fミレイユ、\x01",
            "そっちの復旧作業の方はどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "#07901Fええ、あなたたちの調査と\x01",
            "平行して進めてはいるけど……\x02\x03",

            "#07906Fやっぱり、一度重機を使って\x01",
            "列車自体を動かさないと\x01",
            "手の出しようがないわね。\x02\x03",

            "#07900Fとりあえず、今は散らばった\x01",
            "破片なんかを撤去してるところよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#00003Fやっぱり、俺たちも手伝って……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "#07904Fいえ、それには及ばないわ。\x01",
            "あなたたちは調査に\x01",
            "専念してちょうだい。\x02\x03",

            "#07902F私たちの方でも、\x01",
            "何か分かったら報せるわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 4)
    Jump("loc_1634")

    label("loc_15CC")


    #C0046
    ChrTalk(
        0xFE,
        (
            "#07904Fあなたたちは調査に\x01",
            "専念してちょうだい。\x02\x03",

            "#07902F私たちの方でも、\x01",
            "何か分かったら報せるわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1634")

    TalkEnd(0xFE)
    Return()

    # Function_8_13FA end

    def Function_9_1638(): pass

    label("Function_9_1638")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179E")

    #C0047
    ChrTalk(
        0xFE,
        (
            "一応、倒れた車両の中も\x01",
            "調べられるだけ調べたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "内部には大した手がかりは\x01",
            "なさそうだったよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x105,
        (
            "#10302F怪しい物とかは\x01",
            "置かれてなかったのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "ああ、あったのは乗客の\x01",
            "荷物とかばっかりだったけど、\x01",
            "特に怪しい物はなかったかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "外的な要因によって\x01",
            "起きた事故なのは\x01",
            "間違いないだろうね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        "#00303Fふむ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17B, 3)
    Jump("loc_181E")

    label("loc_179E")


    #C0053
    ChrTalk(
        0xFE,
        (
            "倒れた車両の内部には\x01",
            "大した手がかりは\x01",
            "なさそうだったよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "外的な要因によって\x01",
            "起きた事故なのは\x01",
            "間違いないだろうね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181E")

    TalkEnd(0xFE)
    Return()

    # Function_9_1638 end

    def Function_10_1822(): pass

    label("Function_10_1822")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190B")

    #C0055
    ChrTalk(
        0xFE,
        (
            "はあ、ここまでの事故現場となると、\x01",
            "見てるだけでもショックですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "でも、真実を伝えるためには\x01",
            "いい写真をたくさん撮らないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "１枚の写真が何かの\x01",
            "証拠になることだって、\x01",
            "十分にありえる事ですもんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19A3")

    label("loc_190B")


    #C0058
    ChrTalk(
        0xFE,
        (
            "事故現場の取材は\x01",
            "ショッキングだけど……\x01",
            "いい写真をたくさん撮らないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "１枚の写真が何かの\x01",
            "証拠になることだって、\x01",
            "十分にありえる事ですもんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A3")

    TalkEnd(0xFE)
    Return()

    # Function_10_1822 end

    def Function_11_19A7(): pass

    label("Function_11_19A7")

    OP_4B(0x8, 0x0)
    OP_4B(0x11, 0x0)
    OP_4B(0x12, 0x0)

    #C0060
    ChrTalk(
        0x8,
        (
            "#02000Fあなたたち、\x01",
            "重機が到着するまで\x01",
            "あとどのくらいかかりそう？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x11,
        (
            "はい、３０分も待たずに\x01",
            "到着する予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x12,
        (
            "しかし、調査に時間をとって\x01",
            "大丈夫なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x12,
        (
            "もし夕方までに片側線路を\x01",
            "復旧できなかったら……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "#02005Fできなかったら……？\x01",
            "そんな心配は必要ないわ。\x02\x03",

            "#02001Fどんな事をしてでも、\x01",
            "必ずやらなければ\x01",
            "ならないのだから。\x02\x03",

            "#02003F……あなた達も、それは\x01",
            "分かっているはずね？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x11,
        "#5P#1Kハ、ハッ！！\x02",
    )


    #C0066
    ChrTalk(
        0x12,
        "#6P#1Kハ、ハッ！！\x02",
    )

    OP_57(0x1)
    OP_5A()

    #C0067
    ChrTalk(
        0x104,
        "#00306F（相変わらずスパルタだぜ……）\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x109,
        "#10102F（ソーニャ司令らしいです。）\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00006F（せっかくチャンスを\x01",
            "  与えてもらったんだ……）\x02\x03",

            "#00001F（なんとしても事故の原因を\x01",
            "  突き止めないとな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0x0)
    OP_4C(0x11, 0x0)
    OP_4C(0x12, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x17B, 0)
    Return()

    # Function_11_19A7 end

    def Function_12_1C5E(): pass

    label("Function_12_1C5E")

    TalkBegin(0xFE)

    #C0070
    ChrTalk(
        0xFE,
        (
            "うーん、あんまり近づくと\x01",
            "危険そうだなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "今はバランスを保ってるけど、\x01",
            "何かの拍子に倒れたらどうしよう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1C5E end

    def Function_13_1CD9(): pass

    label("Function_13_1CD9")

    TalkBegin(0xFE)

    #C0072
    ChrTalk(
        0xFE,
        (
            "あーあー、ガラスやら何やらが\x01",
            "散らばっちまってら……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "線路の上に小石一つでもあると\x01",
            "危ないんだ、夕方までに\x01",
            "全部拾っておかないと。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1CD9 end

    def Function_14_1D69(): pass

    label("Function_14_1D69")

    TalkBegin(0xFE)

    #C0074
    ChrTalk(
        0xFE,
        (
            "こんな両方の線路にかぶさるように\x01",
            "脱線しちゃうなんてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "乗っていた旅行客や帰省客たちも、\x01",
            "さぞ恐ろしい思いをしただろうな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1D69 end

    def Function_15_1DF6(): pass

    label("Function_15_1DF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_1E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E14")
    Call(0, 11)
    Jump("loc_1E7C")

    label("loc_1E14")


    #C0076
    ChrTalk(
        0xFE,
        (
            "重機は３０分と待たずに\x01",
            "到着する予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "それまでに、少しずつでも\x01",
            "作業を進めておかなければ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7C")

    TalkEnd(0xFE)
    Return()

    # Function_15_1DF6 end

    def Function_16_1E80(): pass

    label("Function_16_1E80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 0)), scpexpr(EXPR_END)), "loc_1F23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9E")
    Call(0, 11)
    Jump("loc_1F23")

    label("loc_1E9E")


    #C0078
    ChrTalk(
        0xFE,
        (
            "調査は必要、だけど予定を\x01",
            "遅らせる事はできない、か……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "まあ、仕方ないな。\x01",
            "恐ろしく大変だろうけど、\x01",
            "頑張ってみるしかないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F23")

    TalkEnd(0xFE)
    Return()

    # Function_16_1E80 end

    def Function_17_1F27(): pass

    label("Function_17_1F27")

    TalkBegin(0xFE)

    #C0080
    ChrTalk(
        0xFE,
        (
            "連絡を受けた時は、\x01",
            "ここまでの事故とは\x01",
            "思いませんでしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "線路の補修に使う資材も\x01",
            "相当な量が必要そうですね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1F27 end

    def Function_18_1FA5(): pass

    label("Function_18_1FA5")

    TalkBegin(0xFE)

    #C0082
    ChrTalk(
        0xFE,
        (
            "線路が大きく\x01",
            "千切れてしまっているな。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "このあたりから脱線が\x01",
            "始まったんだろうか……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1FA5 end

    def Function_19_2008(): pass

    label("Function_19_2008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_231E")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -5900, 0, -3220, 315)
    SetChrPos(0x103, -5230, 0, -1840, 315)
    SetChrPos(0x104, -5870, 0, -4650, 315)
    SetChrPos(0x105, -4270, 0, -990, 315)
    SetChrPos(0x109, -7140, 0, -4500, 315)
    SetChrPos(0x102, -4660, 0, -3090, 315)
    OP_68(-8420, 1510, -430, 0)
    MoveCamera(322, 8, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(17870, 0)
    OP_0D()
    Sleep(500)

    #C0084
    ChrTalk(
        0x102,
        "#12P#00100Fこの車両は機関車ね。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x103,
        (
            "#12P#00203F導力列車の走行における\x01",
            "最も重要な車両ですね。\x02\x03",

            "#00200F内部にはラインフォルト社製の\x01",
            "列車用オーバルエンジンと\x01",
            "運転室があるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x105,
        (
            "#12P#10305Fふむ、それにしても\x01",
            "なんだか違和感がないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#6P#00303Fああ、想像していたより\x01",
            "だいぶ傷が少ねえ気がするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x109,
        (
            "#6P#10105Fた、確かに……\x01",
            "先頭車両なのにちょっと\x01",
            "不自然な感じですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#12P#00001Fああ……\x01",
            "正面から何かに衝突したなら\x01",
            "ここまで綺麗じゃないはずだ。\x02\x03",

            "#00008Fとなると、脱線の原因は\x01",
            "他にありそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 3)
    OP_29(0xA8, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22F2")
    Call(0, 26)
    Return()

    label("loc_22F2")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -6920, 0, -2370, 315)
    EventEnd(0x5)
    Jump("loc_239E")

    label("loc_231E")

    TalkBegin(0xFF)

    #C0090
    ChrTalk(
        0x101,
        (
            "#00003F正面から何かに衝突したなら\x01",
            "ここまで綺麗じゃないはずだ。\x02\x03",

            "#00008Fとなると、脱線の原因は\x01",
            "他にあるはずだけど……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_239E")

    Return()

    # Function_19_2008 end

    def Function_20_239F(): pass

    label("Function_20_239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_266A")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -14120, 0, -3340, 33)
    SetChrPos(0x102, -15310, 0, -3410, 33)
    SetChrPos(0x103, -13250, 0, -3620, 33)
    SetChrPos(0x104, -12440, 0, -4610, 33)
    SetChrPos(0x109, -13500, 0, -4730, 33)
    SetChrPos(0x105, -14610, 0, -4320, 33)
    OP_68(-13690, 2009, -2900, 0)
    MoveCamera(345, 9, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(16170, 0)
    OP_0D()
    Sleep(500)

    #C0091
    ChrTalk(
        0x101,
        "#6P#00005Fなんだ、これは……？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        (
            "#6P#10105F落石の可能性がありましたが、\x01",
            "もしかしてここに衝突を……？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#6P#00203F球状の凹みを見る限り\x01",
            "可能性はありそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        (
            "#6P#00301Fうーむ……だったら\x01",
            "凹んだ部分の真ん中にある\x01",
            "爪痕みたいな傷はなんなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x105,
        (
            "#6P#10300Fそれに、よく考えると\x01",
            "随分高い位置についてる\x01",
            "みたいだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        (
            "#6P#00108Fうーん……単なる落石じゃ\x01",
            "こんな傷はつかないわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#6P#00003F一体何が衝突したんだろう……？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 4)
    OP_29(0xA8, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_263E")
    Call(0, 26)
    Return()

    label("loc_263E")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -13530, 0, -2950, 45)
    EventEnd(0x5)
    Jump("loc_26DB")

    label("loc_266A")

    TalkBegin(0xFF)

    #C0098
    ChrTalk(
        0x102,
        (
            "#00108Fうーん……単なる落石じゃ\x01",
            "こんな傷はつかないわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        "#00003F一体何が衝突したんだろう……？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_26DB")

    Return()

    # Function_20_239F end

    def Function_21_26DC(): pass

    label("Function_21_26DC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_21_26DC end

    def Function_22_26EA(): pass

    label("Function_22_26EA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_22_26EA end

    def Function_23_26F8(): pass

    label("Function_23_26F8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Return()

    # Function_23_26F8 end

    def Function_24_2706(): pass

    label("Function_24_2706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF5")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27A5")
    SetChrPos(0x101, -35490, 0, 7260, 0)
    SetChrPos(0x102, -38000, 0, 7070, 300)
    SetChrPos(0x103, -36900, 0, 7230, 330)
    SetChrPos(0x104, -34470, 0, 6820, 60)
    SetChrPos(0x109, -34930, 0, 5800, 60)
    SetChrPos(0x105, -36170, 0, 6550, 0)
    Jump("loc_2894")

    label("loc_27A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_281F")
    SetChrPos(0x101, -55340, 0, 8020, 30)
    SetChrPos(0x102, -57740, 0, 8050, 330)
    SetChrPos(0x103, -56530, 0, 8270, 0)
    SetChrPos(0x104, -54080, 0, 7400, 60)
    SetChrPos(0x109, -56190, 0, 6600, 30)
    SetChrPos(0x105, -57360, 0, 7060, 300)
    Jump("loc_2894")

    label("loc_281F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2894")
    SetChrPos(0x101, -62900, 0, 8740, 0)
    SetChrPos(0x102, -65170, 0, 7220, 300)
    SetChrPos(0x103, -64310, 0, 8130, 330)
    SetChrPos(0x104, -61540, 0, 8920, 30)
    SetChrPos(0x109, -61980, 0, 7950, 60)
    SetChrPos(0x105, -63300, 0, 7610, 0)

    label("loc_2894")

    OP_68(-12460, 600, 9000, 0)
    MoveCamera(23, 46, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28500, 0)
    OP_68(-65230, 600, 11100, 11000)
    MoveCamera(23, 35, 0, 4000)
    Sleep(11500)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2916")
    OP_68(-35670, 600, 9060, 0)
    MoveCamera(14, 37, 0, 0)
    Jump("loc_2971")

    label("loc_2916")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2946")
    OP_68(-54950, 600, 10680, 0)
    MoveCamera(21, 22, 0, 0)
    Jump("loc_2971")

    label("loc_2946")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2971")
    OP_68(-63520, 600, 10610, 0)
    MoveCamera(353, 23, 0, 0)

    label("loc_2971")

    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sleep(500)

    #C0100
    ChrTalk(
        0x101,
        (
            "#12P#00005Fこの岩壁の傷……\x01",
            "ずいぶん大きくついてるな。\x02\x03",

            "#00001F一面が抉れたようになってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        (
            "#6P#00105F地面にも抉れた跡が残ってるわね。\x01",
            "左側に脱線したということかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x105,
        (
            "#6P#10305Fところで、岩壁についている\x01",
            "この青っぽい色はなんだろうね？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x103,
        (
            "#6P#00200Fどうやら、何らかの塗料が\x01",
            "付着しているみたいですが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B0B")
    OP_68(-30920, 800, 4590, 3000)
    MoveCamera(76, 34, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(22500, 3000)
    Jump("loc_2B8A")

    label("loc_2B0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4D")
    OP_68(-30920, 800, 4590, 4000)
    MoveCamera(76, 34, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(22500, 3000)
    Jump("loc_2B8A")

    label("loc_2B4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B8A")
    OP_68(-30920, 800, 4590, 5000)
    MoveCamera(76, 34, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(22500, 5000)

    label("loc_2B8A")


    def lambda_2B8F():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2B8F)
    Sleep(50)

    def lambda_2B9F():
        OP_93(0xFE, 0x64, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B9F)
    Sleep(50)

    def lambda_2BAF():
        OP_93(0xFE, 0x6E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BAF)
    Sleep(50)

    def lambda_2BBF():
        OP_93(0xFE, 0x69, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2BBF)
    Sleep(50)

    def lambda_2BCF():
        OP_93(0xFE, 0x64, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BCF)
    Sleep(50)

    def lambda_2BDF():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BDF)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D4E")

    #C0104
    ChrTalk(
        0x109,
        (
            "#N#10100F#12P列車を見る限り……\x01",
            "車体に使われている\x01",
            "青色の塗料みたいです。\x02\x03",

            "#10103F列車と岩壁が接触して、\x01",
            "そのまま少しの間走行した……\x01",
            "その証拠にはなりそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        (
            "#6P#00301Fああ、だが……\x01",
            "ここまで長く引き摺った様な\x01",
            "傷がつくもんなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#N#6P#00003Fどんな状況だったら\x01",
            "こんな傷がつくか、改めて\x01",
            "考える必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EAA")

    label("loc_2D4E")

    SetMessageWindowPos(220, 140, -1, -1)

    #A0107
    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10100F列車を見る限り……\x01",
            "車体に使われている\x01",
            "青色の塗料みたいです。\x02\x03",

            "#10103F列車と岩壁が接触して、\x01",
            "そのまま少しの間走行した……\x01",
            "その証拠にはなりそうですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #A0108
    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00301Fああ、だが……\x01",
            "ここまで長く引き摺った様な\x01",
            "傷がつくもんなのか？\x02",
        )
    )

    CloseMessageWindow()

    #A0109
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003Fどんな状況だったら\x01",
            "こんな傷がつくか、改めて\x01",
            "考える必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_2EAA")

    OP_5A()
    SetScenarioFlags(0x17A, 5)
    OP_29(0xA8, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F70")
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EFE")
    OP_68(-35670, 600, 9060, 0)
    MoveCamera(14, 37, 0, 0)
    Jump("loc_2F59")

    label("loc_2EFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2E")
    OP_68(-54950, 600, 10680, 0)
    MoveCamera(21, 22, 0, 0)
    Jump("loc_2F59")

    label("loc_2F2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F59")
    OP_68(-63520, 600, 10610, 0)
    MoveCamera(353, 23, 0, 0)

    label("loc_2F59")

    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Call(0, 26)
    Return()

    label("loc_2F70")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FA9")
    SetChrPos(0x0, -35980, 0, 7690, 339)
    Jump("loc_2FEE")

    label("loc_2FA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FCE")
    SetChrPos(0x0, -56210, 0, 8260, 24)
    Jump("loc_2FEE")

    label("loc_2FCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FEE")
    SetChrPos(0x0, -65200, 0, 8340, 294)

    label("loc_2FEE")

    EventEnd(0x5)
    Jump("loc_30AB")

    label("loc_2FF5")

    TalkBegin(0xFF)

    #C0110
    ChrTalk(
        0x109,
        (
            "#10100F岩壁の傷跡に付着した塗料……\x01",
            "状況から考えて列車のものと\x01",
            "断定していいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#00000Fどんな状況だったら\x01",
            "こんな傷がつくか、改めて\x01",
            "考える必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_30AB")

    Return()

    # Function_24_2706 end

    def Function_25_30AC(): pass

    label("Function_25_30AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, 10050, 0, -10800, 315)
    SetChrPos(0x102, 9850, 0, -11950, 315)
    SetChrPos(0x103, 11450, 0, -12190, 315)
    SetChrPos(0x104, 11600, 0, -10950, 315)
    SetChrPos(0x109, 10250, 0, -13300, 315)
    SetChrPos(0x105, 11600, 0, -13350, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3210")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Call(0, 3)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0x8, -800, 0, 6350, 180)
    SetChrPos(0x9, -2000, 0, 6350, 180)
    SetChrPos(0xA, -1400, 0, 4550, 0)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)

    label("loc_3210")

    OP_68(10700, 1300, -11950, 0)
    MoveCamera(315, 29, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19750, 0)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    SetCameraDistance(18750, 2500)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0112
    ChrTalk(
        0x101,
        "#00013F#12P……！\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x109,
        "#10107F#6Pこ、これは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    ReplaceBGM("ed7205", "ed7151")
    Fade(1000)
    OP_68(-65000, 1500, -500, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(38750, 0)
    OP_68(-10000, 1500, -500, 15000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrPos(0x101, 6880, 0, -2350, 315)
    SetChrPos(0x104, 8500, 0, -4240, 315)
    SetChrPos(0x109, 7880, 0, -1770, 315)
    SetChrPos(0x102, 8189, 0, -3020, 315)
    SetChrPos(0x103, 7170, 0, -3840, 315)
    SetChrPos(0x105, 9130, 0, -2510, 315)
    OP_68(-1400, 1000, 5450, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19400, 0)
    SetCameraDistance(17900, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0114
    ChrTalk(
        0xA,
        (
            "#02103F#6Pいや～、大変な事故が\x01",
            "起こってしまいましたね！\x02\x03",

            "#02101Fズバリ、脱線事故の原因は！？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        "#5P見ての通り、現在調査中だ。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "#5P考えられるとしたら線路への落石で\x01",
            "先頭車両が脱線したってトコだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "#02003F#11P申し訳ないけど、ここから先は\x01",
            "マスコミにはお引取り願いするわ。\x02\x03",

            "#02000Fすぐに復旧作業に\x01",
            "取り掛かる必要がありますから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0x5A, 0x1F4)

    #C0118
    ChrTalk(
        0xA,
        "#02105F#6Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        "#5P司令、それは……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(150)

    #C0120
    ChrTalk(
        0x8,
        (
            "#02006F#12P警察として、現場検証を\x01",
            "優先したいお気持ちは分かります。\x02\x03",

            "#02001Fですがこの横断鉄道は\x01",
            "ゼムリア大陸における大動脈……\x02\x03",

            "既に鉄道公社、帝国・共和国方面、\x01",
            "更にはディーター市長からも\x01",
            "大至急の復旧が要請されています。\x02\x03",

            "我々警備隊としては\x01",
            "その要請に応えなくてはなりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        "#5Pいや、理屈は判りますがね……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        (
            "#02101F#6Pでも、事故の原因が判らないと\x01",
            "再発の恐れがあるんじゃ……？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(200)

    #C0123
    ChrTalk(
        0x8,
        (
            "#02003F#11Pそれに関しては、\x01",
            "復旧と並行するしかないでしょう。\x02\x03",

            "#02001Fとにかく遅くとも、夕方までには\x01",
            "片側の路線を空ける必要があります。\x02\x03",

            "手配した重機が到着する前に──\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        "#00011F#5P待ってください！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_389B():
        OP_93(0x8, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_389B)
    Sleep(50)

    def lambda_38AB():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_38AB)
    Sleep(50)

    def lambda_38BB():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_38BB)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    Sleep(100)
    Fade(500)
    OP_68(3340, 1400, 1660, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20650, 0)
    OP_68(780, 1400, 3820, 3000)
    SetCameraDistance(20650, 3000)

    def lambda_3927():
        OP_9B(0x0, 0x101, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3927)
    Sleep(0)

    def lambda_393F():
        OP_9B(0x0, 0x109, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_393F)
    Sleep(0)

    def lambda_3957():
        OP_9B(0x0, 0x102, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3957)
    Sleep(0)

    def lambda_396F():
        OP_9B(0x0, 0x103, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_396F)
    Sleep(0)

    def lambda_3987():
        OP_9B(0x0, 0x104, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3987)
    Sleep(0)

    def lambda_399F():
        OP_9B(0x0, 0x105, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_399F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()

    #C0125
    ChrTalk(
        0x8,
        "#02005F#11Pあなた達……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        "#02105F#5Pあら、ロイド君たち！？\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        "#5Pおお、来たのかよ。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x109,
        (
            "#10106F#12Pあの、司令……\x02\x03",

            "#10113F現場検証もしないで\x01",
            "復旧作業に入るんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#02006F#11Pあなたも警備隊の所属ならば\x01",
            "この路線の重要性は判るでしょう。\x02\x03",

            "#02001Fそれに言いたくはないけれど……\x02\x03",

            "復旧が遅れれば、\x01",
            "それだけで帝国と共和国の横槍を\x01",
            "招くことに繋がりかねないわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0130
    ChrTalk(
        0x109,
        "#10111F#12Pそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        "#00106F#6P……十分に考えられますね。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "#5Pふう、それを言われますと\x01",
            "こちらも強くは出れませんなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "#02106F#5Pうーん、でもこちらには\x01",
            "真実を追究するという使命が……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0134
    ChrTalk(
        0x101,
        (
            "#00003F#6P──ソーニャ司令。\x02\x03",

            "#00001F３０分、いえ重機が来るまで\x01",
            "俺たちに時間をもらえませんか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0135
    ChrTalk(
        0x8,
        "#02005F#11Pあなた達に……？\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#00006F#6Pええ、現在のクロスベルで\x01",
            "今回の事故が起こったこと……\x02\x03",

            "#00001F自分にはとても、\x01",
            "単なる偶然とは思えません。\x02\x03",

            "本当に“必然性”は無いのか\x01",
            "見極めるべきではないでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        "#02001F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        (
            "#00201F#6P例の《幻獣》による\x01",
            "被害の可能性もありますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#00300F#6Pま、気休め程度に任せてくれても\x01",
            "いいんじゃないッスか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0140
    ChrTalk(
        0x8,
        (
            "#02006F#11P……そうね、私としたことが\x01",
            "少しばかり焦っていたようだわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)

    #C0141
    ChrTalk(
        0x8,
        (
            "#02002F#12P──ドノバン警部。\x01",
            "まずは現場検証を優先しましょう。\x02\x03",

            "代わりに復旧作業が始まれば\x01",
            "そちらに集中させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x9,
        "#5Pええ、こちらも異存ありません。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x2D, 0x1F4)

    #C0143
    ChrTalk(
        0xA,
        (
            "#02109F#6Pあのー、できれば\x01",
            "あたしたちの取材も……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)

    #C0144
    ChrTalk(
        0x8,
        (
            "#02003F#11P復旧作業が始まるまでは\x01",
            "どうぞご自由に。\x02\x03",

            "#02000Fただし……\x01",
            "現場検証の邪魔はしないように。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        "#02110F#6Pええ、それは勿論！\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#00001F#6P警部、自分たちの方も\x01",
            "現場検証に入らせてもらっても？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_40FE():
        OP_93(0x8, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_40FE)
    Sleep(50)

    def lambda_410E():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_410E)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0xA, 0)

    #C0147
    ChrTalk(
        0x9,
        "#5Pおお、手分けするとしよう。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            "#5Pそうそう、向こうの方に\x01",
            "列車に乗っていた車掌が休んでいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            "#5P運転士は病院に運ばれちまったが\x01",
            "そいつから事故当時の話は聞けるだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#00003F#6P了解しました。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x105,
        "#10302F#12Pそれじゃあ捜査開始だね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(21150, 1500)
    OP_6F(0x79)
    OP_0D()
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Call(0, 3)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    SetChrPos(0x0, -1000, 0, 1850, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x163, 1)
    OP_29(0xA8, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_25_30AC end

    def Function_26_42FB(): pass

    label("Function_26_42FB")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0152
    ChrTalk(
        0x101,
        (
            "#00003F……よし、これで大体、\x01",
            "必要な情報は集まったな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_43D5():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_43D5)
    Sleep(50)

    def lambda_43E5():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_43E5)
    Sleep(50)

    def lambda_43F5():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_43F5)
    Sleep(50)

    def lambda_4405():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4405)
    Sleep(50)

    def lambda_4415():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4415)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    #C0153
    ChrTalk(
        0x109,
        "#10105Fえ、もうですか！？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x103,
        "#00202F……さすがロイドさん。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        (
            "#00306F俺なんざ、アテが外れて\x01",
            "訳が判らなくなったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x105,
        (
            "#10302F僕の方も幾つか\x01",
            "気付いたことがあるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        (
            "#00101Fどうする？\x01",
            "早速、情報を検討してみる？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#00000Fああ……\x01",
            "司令や警部たちも呼ぼう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Call(0, 27)
    Return()

    # Function_26_42FB end

    def Function_27_455F(): pass

    label("Function_27_455F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis257.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis258.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis259.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis260.itp")
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(852)
    SoundLoad(891)
    SetChrPos(0x101, 200, 0, 2550, 0)
    SetChrPos(0x102, -650, 0, 2100, 0)
    SetChrPos(0x103, 1500, 0, 2050, 0)
    SetChrPos(0x104, -800, 0, 1100, 0)
    SetChrPos(0x109, 850, 0, 1450, 0)
    SetChrPos(0x105, 1050, 0, 400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    SetChrPos(0x8, 0, 0, 4500, 180)
    SetChrPos(0x9, -1000, 0, 4750, 180)
    SetChrPos(0xA, 2250, 0, 4100, 225)
    SetChrPos(0xB, 800, 0, 4950, 180)
    SetChrPos(0xC, -900, 0, 5850, 180)
    SetChrPos(0xD, 600, 0, 6100, 180)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_68(90, 900, 3590, 0)
    MoveCamera(310, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21550, 0)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    SetCameraDistance(20650, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0159
    ChrTalk(
        0x8,
        (
            "#02001F#11Pさてと……\x01",
            "何か判明した事はあるかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        (
            "#00006F#6Pええ、まず最初に落石などが\x01",
            "線路に落ちた可能性ですが……\x02\x03",

            "#00001Fそれは真っ先に否定できると\x01",
            "言ってもいいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xC,
        "#11Pそ、そりゃまたどうして？\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x9,
        (
            "#5Pつまり、それを裏付ける\x01",
            "証拠があるってんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        "#00000F#6Pはい、それは──\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0164
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K落石を否定できる根拠は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "車掌が聞いた運転士の叫び\x01",          # 0
            "機関車先端の傷の少なさ\x01",            # 1
            "機関車の右側の大きく凹んだ跡\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_49AC"),
        (1, "loc_4ABE"),
        (2, "loc_4B3F"),
        (SWITCH_DEFAULT, "loc_4C7D"),
    )


    label("loc_49AC")


    #C0165
    ChrTalk(
        0x105,
        (
            "#10306F#6P──いや、それ自体は\x01",
            "落石の反証にならないんじゃない？\x02\x03",

            "#10301F進行方向に突然、落石が落ちて\x01",
            "悲鳴を上げた可能性もあるしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#00008F#5Pそうか……確かに。\x02\x03",

            "#00013F……となると、やっぱり\x01",
            "機関車先端の傷の少なさだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x105,
        "#10302F#6Pああ、僕もそう思うよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C7D")

    label("loc_4ABE")

    OP_2C(0xA8, 0x2)

    #C0168
    ChrTalk(
        0x101,
        (
            "#00003F#6P色々、怪しげな証拠は\x01",
            "見つかっていますが……\x02\x03",

            "#00013F決定的なのは、機関車先端の\x01",
            "傷の少なさだと思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C7D")

    label("loc_4B3F")

    OP_2C(0xA8, 0x1)

    #C0169
    ChrTalk(
        0x105,
        (
            "#10306F#6P──いや、確かにそれは\x01",
            "重要な手がかりかもしれないけど\x01",
            "落石の反証にならないんじゃない？\x02\x03",

            "#10300F右側の崖から落石が転がり落ちて\x01",
            "ぶつかった可能性だってあるんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#00008F#5Pそうか……確かに。\x02\x03",

            "#00013F……となると、やっぱり\x01",
            "機関車先端の傷の少なさだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x105,
        "#10302F#6Pああ、僕もそう思うよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C7D")

    label("loc_4C7D")


    #C0172
    ChrTalk(
        0x8,
        "#02005F#11Pどういう事かしら？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "#07901F#11P確かに、機関車の先端には\x01",
            "特に傷が無かったけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    SetMessageWindowPos(300, 200, -1, -1)

    #A0174
    AnonymousTalk(
        0x101,
        (
            "#00003F普通、落石で脱線する場合、\x01",
            "線路上に落ちた岩が先頭車両と\x01",
            "ぶつかった場合だと思います。\x02\x03",

            "その結果、スピードに乗った\x01",
            "巨大な質量がバランスを崩し、\x01",
            "線路から外れて脱線する……\x02\x03",

            "#00001Fそれ以外に、ここまで派手に\x01",
            "脱線する事は考えにくい筈です。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0175
    ChrTalk(
        0xA,
        "#02101F#12Pおお、なるほど……！\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x9,
        (
            "#5Pなのに機関車の先端には\x01",
            "傷らしい傷が見当たらない。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        (
            "#5P一番ありそうな可能性が\x01",
            "真っ先に消えたってわけか！\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "#02006F#11P……成程。\x01",
            "確かに見過ごせない事実ね。\x02\x03",

            "#02001Fそれじゃあ、他に考えられる\x01",
            "脱線の可能性はあるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#00008F#6Pはい……\x01",
            "最初は、何らかの爆発物が\x01",
            "使われたかと思ったんですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4F96():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4F96)
    Sleep(50)

    def lambda_4FA6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4FA6)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    #C0180
    ChrTalk(
        0x102,
        "#00101F#5Pそ、それって！？\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x109,
        (
            "#10107F#6P何らかの武装集団が\x01",
            "テロ工作をしたとか……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x104,
        (
            "#00303F#6P──いや、その可能性は\x01",
            "俺も真っ先に思い当たってな。\x02\x03",

            "#00301F一通り見渡してみたんだが\x01",
            "どうやら爆発物が\x01",
            "使われた形跡は全くねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xB,
        (
            "#07906F#11Pそうね、今のところ\x01",
            "こちらも見つけていないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#00003F#6Pそうなると\x01",
            "他に考えられるとしたら……\x02\x03",

            "#00013F“何か”に機関車の右側から\x01",
            "体当たりされた可能性でしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0185
    ChrTalk(
        0x9,
        "#5Pな、なにぃ！？\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xC,
        (
            "#11Pた、体当たりって、\x01",
            "そんなムチャクチャな……！\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        (
            "#02105F#12P車のレースのデッドヒートなら\x01",
            "そういう事はありそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0188
    ChrTalk(
        0x103,
        (
            "#00203F#12Pなるほど……\x02\x03",

            "#00201F機関車の右側にあった\x01",
            "大きく凹んだ部分ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#00008F#5Pああ、多分こういう事が\x01",
            "起きたんじゃないかと思う。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 0, -1, -1)

    #A0190
    AnonymousTalk(
        0x101,
        (
            "#00003Fその“何か”は、走行中の列車の\x01",
            "機関車の真横に降り立った。\x02\x03",

            "#00001F運転士さんが上げた叫び声というのは\x01",
            "多分、その時のものだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 200, -1, -1)

    #A0191
    AnonymousTalk(
        0x101,
        (
            "#00008F“何か”はそのまま併走しながら\x01",
            "機関車の右側から体当たりをして……\x02\x03",

            "横からのベクトルを加えられた\x01",
            "機関車は左側に脱線してしまう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(0, 200, -1, -1)

    #A0192
    AnonymousTalk(
        0x101,
        (
            "#00013Fそして“何か”は機関車を\x01",
            "左の岩壁に押し続けて……\x02\x03",

            "長い傷跡を岩壁に残した挙句に\x01",
            "ようやく停車させた。\x02\x03",

            "#00003Fそして後続の客車はこんな風に\x01",
            "バラバラな形で脱線する事になった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x9)
    OP_64(0xC)
    OP_64(0x8)
    OP_64(0xB)
    OP_64(0xA)
    OP_64(0xD)

    #C0193
    ChrTalk(
        0x101,
        (
            "#00000F#6P……とりあえずこれが\x01",
            "現時点での仮説なんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xC,
        "#11Pはあああっ……！\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        "#07902F#11P……見事だわ。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "#5Pいやはや、推理にかけちゃ、\x01",
            "兄貴を越えたんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xA,
        (
            "#02104F#12P確かに……\x01",
            "ガイさんはもっと直感で\x01",
            "捜査するタイプでしたもんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        "#00309F#6Pおいおい、大好評じゃねえか。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#00109F#5Pふふっ……\x01",
            "何だか誇らしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        (
            "#10302F#6Pやれやれ、僕もそこまでは\x01",
            "まとめ切れなかったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "#02004F#11Pふふ、大したものね。\x02\x03",

            "#02001F──それでロイド君。\x02\x03",

            "そこまでした“何か”というのは\x01",
            "やはり魔獣なのかしら？\x02\x03",

            "それも最近現れた《幻獣》とか？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#00008F#6Pそうですね……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K事故を起こした“何か”とは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "《幻獣》の可能性が高い\x01",      # 0
            "まだ断言はできない\x01",          # 1
        )
    )

    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis261.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis262.itp")
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5A76"),
        (1, "loc_5C05"),
        (SWITCH_DEFAULT, "loc_5D6E"),
    )


    label("loc_5A76")


    #C0204
    ChrTalk(
        0x101,
        (
            "#00006F#6Pええ、走行する列車を\x01",
            "脱線させることが出来るほどの\x01",
            "力の持ち主です。\x02\x03",

            "#00001F大型の幻獣と考えるのが\x01",
            "一番自然だと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#00205F#12Pですが、ロイドさん。\x02\x03",

            "#00200F幻獣が出現した割には\x01",
            "上位属性の気配は感じませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        "#00011F#5Pそうか、それがあったか……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x8,
        (
            "#02006F#11P……ふむ、昨日の報告にあった\x01",
            "《蒼い花》も咲いてなさそうだし……\x02\x03",

            "#02008Fそれでは一体、どんな存在が？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D6E")

    label("loc_5C05")

    OP_2C(0xA8, 0x1)

    #C0208
    ChrTalk(
        0x101,
        (
            "#00006F#6P確かに、走行する列車を\x01",
            "脱線させることが出来るほどの\x01",
            "力の持ち主です。\x02\x03",

            "#00008F大型の幻獣と考えるのが\x01",
            "自然だとは思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x103,
        (
            "#00203F#12Pですが、幻獣が出現した割には\x01",
            "上位属性の気配は感じません……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x105,
        (
            "#10308F#6Pあの《蒼い花》も\x01",
            "ここらには咲いてなさそうだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x8,
        (
            "#02006F#11P確かにそうね……\x02\x03",

            "#02008Fそれでは一体、どんな存在が？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D6E")

    label("loc_5D6E")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    #C0212
    ChrTalk(
        0x101,
        (
            "#00006F#6P（他に考えられるとしたら\x01",
            "  《結社》の人形兵器だろうけど……）\x02\x03",

            "#00008F（こんな風に直接、動く連中なのか？）\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    Sound(891, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(2000)
    CancelBlur(1000)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0213
    ChrTalk(
        0xB,
        "#07905F#11Pい、今のは……！？\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        "#11Pま、魔獣の吠え声……！？\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        (
            "#00108F#5Pそ、それにしては\x01",
            "不気味すぎる感じが……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x103,
        "#00201F#6Pセンサーを起動します……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(300)
    OP_68(600, 900, 3450, 1500)

    def lambda_6078():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6078)

    def lambda_6085():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6085)

    def lambda_6092():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6092)

    def lambda_609F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_609F)

    def lambda_60AC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_60AC)

    def lambda_60B9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_60B9)

    def lambda_60C6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_60C6)

    def lambda_60D3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_60D3)

    def lambda_60E0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_60E0)

    def lambda_60ED():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_60ED)

    def lambda_60FA():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_60FA)

    def lambda_6107():
        OP_95(0xFE, 2500, 0, 2050, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6107)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x103, 3, 0, 28)
    Sleep(3000)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(200)
    OP_93(0xA, 0x0, 0x1F4)
    Sleep(100)
    OP_93(0xA, 0x10E, 0x1F4)
    Sleep(200)
    TurnDirection(0xA, 0xD, 500)

    #C0217
    ChrTalk(
        0xA,
        (
            "#02101F#6Pどこ、どこにいるの！？\x02\x03",

            "レインズ君、\x01",
            "何とかカメラに収めなさい！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xD,
        "#5P無茶言わないで下さいよ～！\x02",
    )

    CloseMessageWindow()
    Sound(891, 0, 50, 0)
    Sleep(1000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x103, 3)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7203", 0)
    ReplaceBGM("ed7205", "ed7203")
    ReplaceBGM("ed7250", "ed7203")
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(500)

    #C0219
    ChrTalk(
        0x103,
        (
            "#00207F#12P──距離１０セルジュ！\x01",
            "西へ遠ざかっていきます……！\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#00010F#5Pくっ……\x02\x03",

            "#00007Fみんな、追いかけるぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x104,
        "#00307F#5Pああ、合点承知だ！\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x109,
        "#10101F#6P了解しました！\x02",
    )

    CloseMessageWindow()

    def lambda_62F4():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_62F4)
    Sleep(50)

    def lambda_6304():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6304)
    Sleep(50)

    def lambda_6314():
        OP_93(0xA, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_6314)
    Sleep(50)

    def lambda_6324():
        OP_93(0xB, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_6324)
    Sleep(50)

    def lambda_6334():
        OP_93(0xC, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_6334)
    Sleep(50)

    def lambda_6344():
        OP_93(0xD, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6344)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)

    #C0223
    ChrTalk(
        0x9,
        "#5Pおいおい、無茶すんなよ！？\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xB,
        "#07907F#11P警備隊からも増援を！\x02",
    )

    CloseMessageWindow()

    def lambda_63B1():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_63B1)
    Sleep(50)

    def lambda_63C1():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_63C1)
    Sleep(50)

    def lambda_63D1():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_63D1)
    Sleep(50)

    def lambda_63E1():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_63E1)
    Sleep(50)

    def lambda_63F1():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_63F1)
    Sleep(50)

    def lambda_6401():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6401)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0225
    ChrTalk(
        0x101,
        (
            "#00013F#6Pいえ、そちらは\x01",
            "復旧作業に専念してください！\x02\x03",

            "まずは俺たちで追ってみます！\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xB,
        "#07906F#11Pくっ……そうだったわね。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "#02003F#11P……そろそろ重機も到着する。\x01",
            "お言葉に甘えるしかなさそうね。\x02\x03",

            "#02001F何かあったら駆けつけるから\x01",
            "必ず連絡してきなさい！\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x109,
        "#10107F#6P了解しました！\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x105,
        "#10308F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(21650, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_24(0x354)
    SetScenarioFlags(0x22, 1)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_455F end

    def Function_28_65B1(): pass

    label("Function_28_65B1")

    Sound(2192, 255, 80, 0)    #voice#Tio
    Sleep(800)
    Fade(250)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sound(812, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sound(357, 0, 70, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xFE, 0x5, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    label("loc_6650")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_666D")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("loc_6650")

    label("loc_666D")

    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Fade(250)
    Sound(812, 0, 100, 0)
    StopSound(852, 500, 100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    Return()

    # Function_28_65B1 end

    SaveToFile()

Try(main)
