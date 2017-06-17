from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9000.bin",                # FileName
        "m9000",                    # MapName
        "m9000",                    # Location
        0x00BE,                     # MapIndex
        "ed7353",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 190, 0, 1, 0, 2],
    )

    BuildStringList((
        "m9000",                  # 0
        "グレイス",               # 1
        "神狼ツァイト",           # 2
        "フラン",                 # 3
        "ヨナ",                   # 4
        "アッバス",               # 5
        "メルカバ玖号機",         # 6
    ))

    AddCharChip((
        "chr/ch06000.itc",                   # 00
        "chr/ch02708.itc",                   # 01
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-15500,  -4980,   -23200,  180,  405,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(14000,   -2000,   13500,   1200,    14000,   -1000,   13500,   0x007C, 0,  12, 0x0000)

    ChipFrameInfo(468, 0)                                        # 0

    ScpFunction((
        "Function_0_1D4",          # 00, 0
        "Function_1_284",          # 01, 1
        "Function_2_2CC",          # 02, 2
        "Function_3_36F",          # 03, 3
        "Function_4_38B",          # 04, 4
        "Function_5_396",          # 05, 5
        "Function_6_6D9",          # 06, 6
        "Function_7_9B1",          # 07, 7
        "Function_8_D0C",          # 08, 8
        "Function_9_F50",          # 09, 9
        "Function_10_F75",         # 0A, 10
        "Function_11_F87",         # 0B, 11
        "Function_12_1176",        # 0C, 12
        "Function_13_1366",        # 0D, 13
        "Function_14_1F66",        # 0E, 14
        "Function_15_1F92",        # 0F, 15
        "Function_16_1FCF",        # 10, 16
        "Function_17_1FF8",        # 11, 17
        "Function_18_202B",        # 12, 18
        "Function_19_205E",        # 13, 19
        "Function_20_2091",        # 14, 20
        "Function_21_20B0",        # 15, 21
        "Function_22_20CF",        # 16, 22
        "Function_23_20EE",        # 17, 23
        "Function_24_2135",        # 18, 24
        "Function_25_2168",        # 19, 25
        "Function_26_2491",        # 1A, 26
    ))


    def Function_0_1D4(): pass

    label("Function_0_1D4")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
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

    # Function_0_1D4 end

    def Function_1_284(): pass

    label("Function_1_284")

    Call(0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2A4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x22, 0)
    Event(0, 13)
    Jump("loc_2CB")

    label("loc_2A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA")
    Event(0, 11)
    Jump("loc_2CB")

    label("loc_2BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    Event(0, 10)

    label("loc_2CB")

    Return()

    # Function_1_284 end

    def Function_2_2CC(): pass

    label("Function_2_2CC")

    OP_F0(0x1, 0x320)
    OP_1B(0x1, 0x0, 0x9)
    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327")
    OP_70(0x1, 0x3C)
    SetMapObjFrame(0x3, "black_add", 0x2, "night")
    SetMapObjFrame(0x3, "blue", 0x2, "night")
    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x2)
    Jump("loc_357")

    label("loc_327")

    OP_70(0x1, 0x0)
    SetMapObjFrame(0x3, "black_add", 0x2, "day")
    SetMapObjFrame(0x3, "blue", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_stop", 0x1, 0x2)

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A")
    OP_70(0x2, 0x3C)
    Jump("loc_36E")

    label("loc_36A")

    OP_70(0x2, 0x0)

    label("loc_36E")

    Return()

    # Function_2_2CC end

    def Function_3_36F(): pass

    label("Function_3_36F")

    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -4750, -3200, -10350, 0)
    Return()

    # Function_3_36F end

    def Function_4_38B(): pass

    label("Function_4_38B")

    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    Return()

    # Function_4_38B end

    def Function_5_396(): pass

    label("Function_5_396")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_56E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B4")
    Call(0, 6)
    Jump("loc_569")

    label("loc_3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC")

    #C0001
    ChrTalk(
        0x9,
        (
            "#01203F#3Cかつて《幻の至宝#8Rデ ミ ウ ル ゴ ス#》は\x01",
            "自らを消滅させることを選んだ……\x02\x03",

            "#01200Fキーアが同じ結論に\x01",
            "辿り着いてしまう可能性は、\x01",
            "ないとは言えんだろう。\x02\x03",

            "人の子よ、見事キーアを取り戻し、\x01",
            "それを阻止して見せるがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_569")

    label("loc_4AC")


    #C0002
    ChrTalk(
        0x9,
        (
            "#01203F#3Cキーアが《幻の至宝#8Rデ ミ ウ ル ゴ ス#》と\x01",
            "同じ結論に辿り着いてしまう可能性は、\x01",
            "ないとは言えんだろう。\x02\x03",

            "#01200F人の子よ、見事キーアを取り戻し、\x01",
            "それを阻止して見せるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_569")

    Jump("loc_6D5")

    label("loc_56E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_6D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_658")

    #C0003
    ChrTalk(
        0x9,
        (
            "#01203F#3C《大樹》のどこかに\x01",
            "キーアがいるのは間違いあるまい。\x02\x03",

            "#01200Fおそらくは最も深き場所……\x01",
            "あのクロイス家の娘、そして\x01",
            "黒幕である弁護士と共にな。\x02\x03",

            "私の助けが必要になったら\x01",
            "いつでも呼び出すがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6D5")

    label("loc_658")


    #C0004
    ChrTalk(
        0x9,
        (
            "#01203F#3C《大樹》のどこかに\x01",
            "キーアがいるのは間違いあるまい。\x02\x03",

            "#01200F私の助けが必要になったら\x01",
            "いつでも呼び出すがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D5")

    TalkEnd(0xFE)
    Return()

    # Function_5_396 end

    def Function_6_6D9(): pass

    label("Function_6_6D9")


    #C0005
    ChrTalk(
        0x9,
        (
            "#01203F#3Cかつて《幻の至宝#8Rデ ミ ウ ル ゴ ス#》は\x01",
            "自らを消滅させることを選んだ……\x02\x03",

            "ロイド、おぬしにはそう話したな。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00001F暴走して、守るべき人々を\x01",
            "傷つけてしまうのを防ぐため……\x01",
            "そういう話だったな。\x02\x03",

            "#00003F……《零の至宝》であるキーアも、\x01",
            "そうなってしまうのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            "#01200F#3C……それは分からぬ。\x02\x03",

            "だが、キーアは《零の至宝》となり\x01",
            "ついには女神に匹敵する力を持つ\x01",
            "《大樹》をも生み出した。\x02\x03",

            "それほどまでの大いなる力を、\x01",
            "この先、制御していける保証は\x01",
            "今のところどこにもない。\x02\x03",

            "#01203F《幻の至宝#8Rデ ミ ウ ル ゴ ス#》と同じ結論に\x01",
            "辿り着いてしまう可能性は、\x01",
            "ないとは言えんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00003Fそうか……\x02\x03",

            "#00001Fいや、絶対にさせるもんか。\x01",
            "俺たちがいる限り……！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        "#01200F#3C……フフ、それでこそおぬしだ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 0)
    Return()

    # Function_6_6D9 end

    def Function_7_9B1(): pass

    label("Function_7_9B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CF")
    Call(0, 8)
    Jump("loc_B71")

    label("loc_9CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AED")

    #C0010
    ChrTalk(
        0x8,
        (
            "#02105Fまさかロイド君たちが\x01",
            "あのアリオス・マクレインを\x01",
            "倒しちゃうなんてね。\x02\x03",

            "#02102Fふふっ、\x01",
            "大きく成長してくれて\x01",
            "お姉さんは嬉しいゾ☆\x02\x03",

            "#02104Fあなたたちなら、もうなんだって\x01",
            "乗り越えていけると思うわ。\x02\x03",

            "#02109Fこのままみんなで、\x01",
            "最高のハッピーエンドを迎えましょ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B71")

    label("loc_AED")


    #C0011
    ChrTalk(
        0x8,
        (
            "#02104Fあなたたちなら、もうなんだって\x01",
            "乗り越えていけると思うわ。\x02\x03",

            "#02109Fこのままみんなで、\x01",
            "最高のハッピーエンドを迎えましょ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B71")

    Jump("loc_D08")

    label("loc_B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C98")

    #C0012
    ChrTalk(
        0x8,
        (
            "#02104Fあたしは《大樹》にいる間に\x01",
            "出来るだけ写真を撮っておくわ。\x02\x03",

            "#02100Fそれに、通信社に戻ったら\x01",
            "今回の事件の真実を\x01",
            "記事になくちゃならない……\x02\x03",

            "#02102Fだからロイド君たち、\x01",
            "頑張ってこの事件を解決してね！\x02\x03",

            "#02109Fあたしに最高の三面記事を\x01",
            "書かせてちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_D08")

    label("loc_C98")


    #C0013
    ChrTalk(
        0x8,
        (
            "#02100Fロイド君たち、\x01",
            "頑張ってこの事件を解決してね！\x02\x03",

            "#02109Fあたしに最高の三面記事を\x01",
            "書かせてちょうだい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D08")

    TalkEnd(0xFE)
    Return()

    # Function_7_9B1 end

    def Function_8_D0C(): pass

    label("Function_8_D0C")


    #C0014
    ChrTalk(
        0x8,
        (
            "#02105Fあのアリオス・マクレインを\x01",
            "倒しちゃったみたいね？\x02\x03",

            "#02106Fはあ～……\x01",
            "まさかロイド君たちが\x01",
            "そこまでやるなんて……\x02\x03",

            "#02109F《クロスベルの英雄》も\x01",
            "代替わりの時が来たってことかしら。\x01",
            "いや～、大スクープじゃないの！\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00004Fはは……持ち上げすぎですよ。\x02\x03",

            "#00000Fそれに、クロスベルにとって\x01",
            "アリオスさんが英雄というのは\x01",
            "依然、変わらないと思いますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#02104Fふふっ……\x01",
            "ロイド君も成長したわね。\x02\x03",

            "#02102Fアリオスさんを超えた\x01",
            "あなたたちなら、もうなんだって\x01",
            "乗り越えていけると思うわ。\x02\x03",

            "#02109Fこのままみんなで、\x01",
            "最高のハッピーエンドを迎えましょ！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#00000Fはい！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 0)
    Return()

    # Function_8_D0C end

    def Function_9_F50(): pass

    label("Function_9_F50")

    EventBegin(0x2)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    EventEnd(0x5)
    NewScene("e3020", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_9_F50 end

    def Function_10_F75(): pass

    label("Function_10_F75")

    EventBegin(0x2)
    FadeToDark(0, 0, -1)
    OP_0D()
    PartySelect(2)
    EventEnd(0x5)
    Return()

    # Function_10_F75 end

    def Function_11_F87(): pass

    label("Function_11_F87")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SoundLoad(497)
    Call(0, 4)
    ClearChrFlags(0xD, 0x80)
    OP_78(0x0, 0xD)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    SetMapObjFlags(0x4, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0xD, -20000, 8250, -17000, 0)
    OP_D5(0xD, 0x0, 0x4F588, 0x0, 0x0)

    def lambda_1014():
        OP_96(0xFE, 0xFFFFB1E0, 0xFFFFDFC6, 0xFFFFBD98, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1014)

    def lambda_102E():
        OP_D5(0xFE, 0x0, 0x4CE78, 0x0, 0x2328)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_102E)
    OP_68(-20000, 12500, -17000, 0)
    MoveCamera(20, -25, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(40000, 0)
    OP_68(-20000, -1250, -17000, 10000)
    MoveCamera(10, 20, 0, 10000)
    SetCameraDistance(35000, 10000)
    SetEventSkip(0x0, "loc_10C5")
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(7000)
    StopSound(497, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_10C5")

    EndChrThread(0xD, 0x1)
    EndChrThread(0xD, 0x2)
    SetChrPos(0xD, -20000, -8250, -17000, 315)
    OP_D5(0xD, 0x0, 0x4CE78, 0x0, 0x0)
    OP_70(0x0, 0x116)
    ClearMapObjFlags(0x4, 0x4)
    Call(0, 3)
    ClearChrFlags(0x0, 0x80)
    ClearChrBattleFlags(0x0, 0x8000)
    ClearChrFlags(0x1, 0x80)
    ClearChrBattleFlags(0x1, 0x8000)
    ClearChrFlags(0x2, 0x80)
    ClearChrBattleFlags(0x2, 0x8000)
    ClearChrFlags(0x3, 0x80)
    ClearChrBattleFlags(0x3, 0x8000)
    OP_68(-16200, -980, -20800, 0)
    MoveCamera(10, 16, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, -16200, -4980, -20800, 135)
    OP_69(0xFF, 0x0)
    Sleep(500)
    ClearMapFlags(0x8000000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_F87 end

    def Function_12_1176(): pass

    label("Function_12_1176")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 0)), scpexpr(EXPR_END)), "loc_11B7")
    TalkBegin(0xFF)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もう反応しないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_1360")

    label("loc_11B7")

    EventBegin(0x1)

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クリスタルがある。\x01",
            "触れますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135E")
    Fade(500)
    SetChrPos(0x0, 12730, -2000, 12430, 54)
    SetChrPos(0x1, 12050, -2000, 13180, 54)
    SetChrPos(0x2, 11370, -2000, 11590, 54)
    SetChrPos(0x3, 10590, -2000, 12660, 54)
    OP_68(10200, 2000, 10420, 0)
    MoveCamera(16, 48, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Sleep(500)
    SetMapObjFrame(0x3, "black_add", 0x2, "to_d")
    SetMapObjFrame(0x3, "blue", 0x2, "to_d")
    Sleep(1000)
    Sound(211, 0, 100, 0)
    Sleep(2000)
    SetMapObjFrame(0x3, "black_add", 0x2, "day")
    SetMapObjFrame(0x3, "blue", 0x2, "day")
    Fade(500)
    OP_68(5100, 1000, -3760, 0)
    MoveCamera(10, 32, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(22000, 0)
    OP_0D()
    Sound(155, 2, 100, 0)
    OP_71(0x1, 0x3C, 0x0, 0x0, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x7D0)
    Sleep(2000)
    OP_70(0x1, 0x0)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0xC8, 0x3E8, 0x64)
    Sleep(1500)
    SetMapObjFrame(0xFF, "CA_stop", 0x1, 0x2)
    SetScenarioFlags(0x1B0, 0)

    label("loc_135E")

    EventEnd(0x5)

    label("loc_1360")

    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1176 end

    def Function_13_1366(): pass

    label("Function_13_1366")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1388")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_1388")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139C")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_139C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B0")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_13B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C4")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_13C4")

    LoadChrToIndex("chr/ch06100.itc", 0x1E)
    LoadChrToIndex("chr/ch06710.itc", 0x1F)
    LoadChrToIndex("chr/ch06900.itc", 0x20)
    LoadChrToIndex("chr/ch06000.itc", 0x21)
    LoadChrToIndex("apl/ch50010.itc", 0x22)
    LoadEffect(0x0, "event\\eva02_00.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis064.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis065.itp")
    SetMapObjFlags(0x4, 0x4)
    SetChrPos(0x101, -10750, -5000, -17000, 0)
    SetChrPos(0x102, -11650, -4900, -16800, 0)
    SetChrPos(0x103, -11500, -4900, -17650, 0)
    SetChrPos(0x104, -13350, -5000, -18600, 0)
    SetChrPos(0x109, -12150, -5000, -18750, 0)
    SetChrPos(0x105, -14400, -5000, -20000, 0)
    SetChrPos(0x106, -11200, -5000, -18950, 0)
    SetChrPos(0x10A, -12750, -5000, -19450, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -17200, -5000, -19900, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -16200, -4900, -20850, 0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -17300, -4900, -19700, 0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -4750, -3200, -10350, 0)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(14280, 6300, -9970, 0)
    MoveCamera(331, 2, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(20430, 0)
    Sleep(1000)
    PlayBGM("ed7353", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x161), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    OP_68(14280, 6300, -9970, 10000)
    MoveCamera(355, -1, 0, 10000)
    OP_6E(1000, 10000)
    SetCameraDistance(6250, 10000)
    OP_0D()
    PlaceName2(340, 200, "c_plac57", 0x0, 3000)
    OP_6F(0x79)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x8, 0, 0, 25)
    BeginChrThread(0xC, 0, 0, 14)
    BeginChrThread(0x10A, 0, 0, 17)
    BeginChrThread(0x106, 0, 0, 18)
    BeginChrThread(0x105, 0, 0, 19)
    BeginChrThread(0x109, 0, 0, 20)
    BeginChrThread(0x104, 0, 0, 21)
    BeginChrThread(0x103, 0, 0, 22)
    BeginChrThread(0x102, 0, 0, 23)
    BeginChrThread(0x101, 0, 0, 24)
    OP_68(-12130, 6300, -25840, 8000)
    MoveCamera(5, 4, 0, 8000)
    OP_6E(1000, 8000)
    SetCameraDistance(55600, 8000)
    OP_6F(0x79)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0xA, 0, 0, 15)
    BeginChrThread(0xB, 0, 0, 16)
    OP_68(-9070, -2500, -16590, 0)
    MoveCamera(26, 3, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(17460, 0)
    Fade(500)
    OP_0D()
    OP_68(-11740, -4400, -13060, 7000)
    MoveCamera(339, 15, 0, 7000)
    OP_6E(1000, 7000)
    SetCameraDistance(15430, 7000)
    OP_6F(0x79)
    OP_68(-9910, -3500, -15330, 0)
    MoveCamera(345, 13, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(7890, 0)
    Fade(500)
    OP_0D()
    Sleep(500)

    #C0020
    ChrTalk(
        0x101,
        "#00007F#6P……ここは……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        "#00108F#6P本当にあの大樹の中……？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#00301F#6P確かにデカイ樹だったが\x01",
            "ここまでじゃねえだろ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#00208F#6P……空間そのものが\x01",
            "歪んでしまっている……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x2)
    SetChrPos(0x8, -4750, -3200, -10350, 0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    OP_68(-9240, 4700, -5380, 0)
    MoveCamera(3, 8, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(12530, 0)
    OP_68(-8600, 7000, -5750, 6000)
    MoveCamera(2, -28, 0, 6000)
    OP_6E(1000, 6000)
    SetCameraDistance(23250, 6000)
    OP_6F(0x79)
    Sleep(1000)
    VolumeBGM(0x3C, 0x1F4)
    FadeToDark(500, 0, -1)
    Sound(824, 0, 80, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    Sleep(200)
    Sound(4130, 255, 100, 0)    #voice#KeA
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    Sleep(200)
    Sound(3044, 255, 100, 0)    #voice#KeA
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    FadeToBright(800, 0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(500)

    #C0024
    ChrTalk(
        0x101,
        "#00013F#5P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_68(-10420, -3600, -12460, 6000)
    MoveCamera(321, 19, 0, 6000)
    OP_6E(1000, 6000)
    SetCameraDistance(16760, 6000)
    Sleep(3000)
    OP_6F(0x79)

    #C0025
    ChrTalk(
        0xA,
        (
            "#01909F#6Pはあああっ……\x01",
            "すっごくキレイ……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x109,
        (
            "#10101F#6P外にあったのとは\x01",
            "また別の大樹……？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x106,
        (
            "#10708F#6P#N無数の光が……\x01",
            "樹に吸い込まれていますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0028
    ChrTalk(
        0xB,
        (
            "#02300F#6Pなんつーか……導力ネットの\x01",
            "概念イメージみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#02109F#6Pうーん、それにしても\x01",
            "シャッターチャンスばかりだわ！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 26)
    Sleep(2000)
    Fade(500)
    OP_68(-9910, -3500, -15330, 0)
    MoveCamera(345, 13, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(8280, 0)
    OP_0D()
    Sleep(300)

    #C0030
    ChrTalk(
        0xC,
        (
            "#12100F#6P──ここより先は、\x01",
            "重力の歪みが発生しているため、\x01",
            "メルカバを進められないようだ。\x02\x03",

            "徒歩で行くより道は無かろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x105,
        (
            "#10406F#5Pやれやれ、面倒だね。\x02\x03",

            "#10400Fまあ、外にだったら\x01",
            "メルカバで離脱も出来そうだ。\x02\x03",

            "いざとなったら《大樹》の外に\x01",
            "出ることも出来ると思うよ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0032
    ChrTalk(
        0x101,
        "#00001F#11Pそうか……判った。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)
    Sleep(300)

    #C0033
    ChrTalk(
        0x10A,
        (
            "#00603F#6Pいずれにせよ、探索班と\x01",
            "待機班を決める必要があるだろう。\x02\x03",

            "#00601F悠長に眺めている余裕はない。\x01",
            "すぐに動くぞ、バニングス。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 500)
    Sleep(100)

    #C0034
    ChrTalk(
        0x101,
        "#00007F#5Pはい……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    OP_68(-8600, 7000, -5750, 0)
    MoveCamera(2, -28, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(5000, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0035
    ChrTalk(
        0x101,
        (
            "#00003F#6P#N（あの大樹のどこかに\x01",
            "  キーアがいるはずだ……）\x02\x03",

            "#00013F（……絶対に………\x01",
            "  何としても見付け出してみせる！）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(3000, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_37()
    ClearMapObjFlags(0x4, 0x4)
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    OP_37()
    SetChrPos(0x0, -8000, -4990, -15300, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -1750, -3000, -7890, 0)
    BeginChrThread(0x8, 0, 0, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A7, 2)
    OP_29(0xB2, 0x1, 0x1)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0x6, 0x0, 0x64)
    ClearMapFlags(0x8000000)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_13_1366 end

    def Function_14_1F66(): pass

    label("Function_14_1F66")

    Sleep(2500)
    OP_95(0xFE, -15500, -4900, -21500, 2000, 0x0)
    OP_95(0xFE, -12100, -5000, -18300, 2000, 0x0)
    Return()

    # Function_14_1F66 end

    def Function_15_1F92(): pass

    label("Function_15_1F92")

    OP_95(0xFE, -15800, -4900, -21200, 1000, 0x0)
    OP_95(0xFE, -14120, -4900, -21350, 1000, 0x0)
    OP_95(0xFE, -13200, -5000, -20500, 1000, 0x0)
    Return()

    # Function_15_1F92 end

    def Function_16_1FCF(): pass

    label("Function_16_1FCF")

    OP_95(0xFE, -16000, -4900, -21350, 2000, 0x0)
    OP_95(0xFE, -14000, -5000, -19600, 2000, 0x0)
    Return()

    # Function_16_1FCF end

    def Function_17_1FF8(): pass

    label("Function_17_1FF8")

    Sleep(2250)
    OP_95(0xFE, -9850, -4900, -16800, 2000, 0x0)
    OP_95(0xFE, -8250, -5000, -17100, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_1FF8 end

    def Function_18_202B(): pass

    label("Function_18_202B")

    Sleep(2000)
    OP_95(0xFE, -8800, -5000, -16350, 3000, 0x0)
    OP_95(0xFE, -6750, -5000, -16000, 3000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_18_202B end

    def Function_19_205E(): pass

    label("Function_19_205E")

    Sleep(2300)
    OP_95(0xFE, -11750, -5000, -17500, 2000, 0x0)
    OP_95(0xFE, -11250, -5000, -16350, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_19_205E end

    def Function_20_2091(): pass

    label("Function_20_2091")

    Sleep(2100)
    OP_95(0xFE, -7350, -5000, -14500, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_20_2091 end

    def Function_21_20B0(): pass

    label("Function_21_20B0")

    Sleep(2150)
    OP_95(0xFE, -10300, -5000, -15500, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_21_20B0 end

    def Function_22_20CF(): pass

    label("Function_22_20CF")

    Sleep(1900)
    OP_95(0xFE, -9000, -5000, -15500, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_22_20CF end

    def Function_23_20EE(): pass

    label("Function_23_20EE")

    Sleep(1800)
    OP_95(0xFE, -11900, -4800, -16700, 2000, 0x0)
    OP_95(0xFE, -10300, -5000, -13500, 2000, 0x0)
    OP_95(0xFE, -10000, -5000, -14000, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_23_20EE end

    def Function_24_2135(): pass

    label("Function_24_2135")

    Sleep(1700)
    OP_95(0xFE, -9050, -4900, -15150, 2000, 0x0)
    OP_95(0xFE, -9120, -5000, -13060, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_24_2135 end

    def Function_25_2168(): pass

    label("Function_25_2168")

    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2178():
        OP_96(0xFE, 0xFFFFF538, 0xFFFFF448, 0xFFFFE796, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2178)

    def lambda_2192():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2192)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 30, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_21FA():
        OP_96(0xFE, 0xFFFFFF74, 0xFFFFF448, 0xFFFFE53E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21FA)

    def lambda_2214():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2214)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 50, 0)
    Sleep(1000)

    label("loc_226F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2488")
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2287():
        OP_96(0xFE, 0xFFFFF948, 0xFFFFF448, 0xFFFFD9F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2287)

    def lambda_22A1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22A1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2309():
        OP_95(0xFE, -4800, -3200, -10140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2309)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(2000)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_238C():
        OP_96(0xFE, 0xFFFFF538, 0xFFFFF448, 0xFFFFE796, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_238C)

    def lambda_23A6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23A6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_240E():
        OP_96(0xFE, 0xFFFFFF74, 0xFFFFF448, 0xFFFFE53E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_240E)

    def lambda_2428():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2428)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 100, 0)
    Sleep(1000)
    Jump("loc_226F")

    label("loc_2488")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_2168 end

    def Function_26_2491(): pass

    label("Function_26_2491")

    Sleep(200)

    label("loc_2494")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2577")
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_24AC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_24AC)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 100, 0)
    Sleep(700)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2510():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2510)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 100, 0)
    Sleep(700)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(4000)
    Jump("loc_2494")

    label("loc_2577")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    Return()

    # Function_26_2491 end

    SaveToFile()

Try(main)
