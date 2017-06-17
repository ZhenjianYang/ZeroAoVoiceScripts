from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9082.bin",                # FileName
        "m9082",                    # MapName
        "m9082",                    # Location
        0x00C3,                     # MapIndex
        "ed7356",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 195, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9082",                  # 0
        "アリオス",               # 1
        "台詞表示用ダミーキャラ", # 2
        "アリオスお供",           # 3
        "アリオスお供",           # 4
        "エフェクト表示用ダミーキャラ",# 5
        "bm9069",                 # 6
    ))

    ATBonus("ATBonus_1D8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_298", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 3, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 13, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_27C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_280", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_284", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_288", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_28C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_290", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2B8", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm9069", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02401.dat", "ms85401.dat", "ms85501.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_298", "MonsterBattlePostion_278", "ed7527", "ed7453", "ATBonus_1D8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51744.itc",                   # 00
    ))

    DeclNpc(0,       12000,   211500,  180,  389,  0x0, 0,   0,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       13100,   204699,  305,  508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   0.0,                   185.0,                 11.0,                  225.0,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.1666666716337204,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -30.83333396911621,    -2.200000047683716,    1.0])

    DeclActor(3500,    0,       155000,  1200,    3500,    1000,    155000,  0x007C, 0,  3,  0x0000)

    ChipFrameInfo(940, 0)                                        # 0

    ScpFunction((
        "Function_0_3AC",          # 00, 0
        "Function_1_3F8",          # 01, 1
        "Function_2_517",          # 02, 2
        "Function_3_78F",          # 03, 3
        "Function_4_88B",          # 04, 4
        "Function_5_B0F",          # 05, 5
        "Function_6_C62",          # 06, 6
        "Function_7_CC3",          # 07, 7
        "Function_8_D24",          # 08, 8
        "Function_9_D37",          # 09, 9
        "Function_10_575F",        # 0A, 10
        "Function_11_578A",        # 0B, 11
        "Function_12_57B5",        # 0C, 12
        "Function_13_57E0",        # 0D, 13
        "Function_14_580B",        # 0E, 14
        "Function_15_5836",        # 0F, 15
        "Function_16_585A",        # 10, 16
        "Function_17_586C",        # 11, 17
        "Function_18_587E",        # 12, 18
        "Function_19_5890",        # 13, 19
        "Function_20_589C",        # 14, 20
        "Function_21_58EA",        # 15, 21
        "Function_22_5938",        # 16, 22
        "Function_23_5961",        # 17, 23
        "Function_24_59AB",        # 18, 24
        "Function_25_59D8",        # 19, 25
        "Function_26_5A04",        # 1A, 26
        "Function_27_5A27",        # 1B, 27
        "Function_28_5A70",        # 1C, 28
        "Function_29_5AB9",        # 1D, 29
        "Function_30_5AD5",        # 1E, 30
        "Function_31_5B49",        # 1F, 31
        "Function_32_76AE",        # 20, 32
        "Function_33_76F7",        # 21, 33
        "Function_34_7761",        # 22, 34
        "Function_35_7FDC",        # 23, 35
        "Function_36_7FEC",        # 24, 36
        "Function_37_7FFB",        # 25, 37
        "Function_38_800D",        # 26, 38
        "Function_39_801F",        # 27, 39
        "Function_40_802B",        # 28, 40
        "Function_41_8079",        # 29, 41
        "Function_42_80C7",        # 2A, 42
        "Function_43_80EE",        # 2B, 43
    ))


    def Function_0_3AC(): pass

    label("Function_0_3AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BD")
    Event(0, 4)

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3D1")
    ClearScenarioFlags(0x22, 0)
    Event(0, 31)
    Jump("loc_3F7")

    label("loc_3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3E5")
    ClearScenarioFlags(0x22, 1)
    Event(0, 34)
    Jump("loc_3F7")

    label("loc_3E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F7")
    Event(0, 8)

    label("loc_3F7")

    Return()

    # Function_0_3AC end

    def Function_1_3F8(): pass

    label("Function_1_3F8")

    OP_F0(0x1, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_414")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_414")

    OP_1B(0x1, 0x0, 0x5)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_431")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_431")

    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x2, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_4BE")
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    OP_70(0x1, 0x96)
    Jump("loc_50A")

    label("loc_4BE")

    SetMapObjFrame(0xFF, "magi10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x1, 0x1)
    OP_70(0x1, 0x3C)

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_516")
    Call(0, 42)

    label("loc_516")

    Return()

    # Function_1_3F8 end

    def Function_2_517(): pass

    label("Function_2_517")

    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73E")

    #C0001
    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#00001F……完全に気を失ってる。\x01",
            "命に別状もなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x104,
        (
            "#00306Fさすがにとんでもねえ相手だったな……\x01",
            "俺たち全員相手にあそこまでやるとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x103,
        "#00208Fさすがは《風の剣聖》……ですね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_641")

    #C0005
    ChrTalk(
        0x10A,
        "#00603Fフン……よく勝てたものだ。\x02",
    )

    CloseMessageWindow()

    label("loc_641")


    #C0006
    ChrTalk(
        0x101,
        (
            "#00003Fシズクちゃんも心配しているだろうし、\x01",
            "すぐにでもメルカバに運びたいけど……\x02\x03",

            "#00001F……この先にはマリアベルさんと\x01",
            "イアン先生が待ち構えている。\x02\x03",

            "#00003F申し訳ないけど、\x01",
            "今は後回しにさせてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        "#00100Fそうね……行きましょう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 0)
    Jump("loc_78B")

    label("loc_73E")


    #C0008
    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "完全に気を失っているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_78B")

    TalkEnd(0x8)
    Return()

    # Function_2_517 end

    def Function_3_78F(): pass

    label("Function_3_78F")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87C")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x0, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x0, 0x0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x0, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_87C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_78F end

    def Function_4_88B(): pass

    label("Function_4_88B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event/ev202_00.eff")
    OP_68(-340, 13500, 219060, 0)
    MoveCamera(29, 41, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12970, 0)
    SetChrPos(0x0, 0, 12000, 222000, 180)
    SetChrPos(0x1, 0, 12000, 222000, 180)
    SetChrPos(0x2, 0, 12000, 222000, 180)
    SetChrPos(0x3, 0, 12000, 222000, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_99B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_99B)

    def lambda_9AC():
        OP_95(0xFE, -240, 12000, 218120, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9AC)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A03)

    def lambda_A14():
        OP_95(0xFE, -1420, 12000, 218280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A14)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_A71)

    def lambda_A82():
        OP_95(0xFE, 1060, 12000, 218310, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A82)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AD9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_AD9)

    def lambda_AEA():
        OP_95(0xFE, -2780, 12000, 218680, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_AEA)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_88B end

    def Function_5_B0F(): pass

    label("Function_5_B0F")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event/evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_B68():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B68)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BB3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_BB3)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BFE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_BFE)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C49():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_C49)
    Sleep(1000)
    NewScene("m9008", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_5_B0F end

    def Function_6_C62(): pass

    label("Function_6_C62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C7A")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_C7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C92")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_C92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAA")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_CAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC2")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_CC2")

    Return()

    # Function_6_C62 end

    def Function_7_CC3(): pass

    label("Function_7_CC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CDB")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_CDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF3")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_CF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D0B")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_D0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D23")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_D23")

    Return()

    # Function_7_CC3 end

    def Function_8_D24(): pass

    label("Function_8_D24")

    EventBegin(0x0)
    StopBGM(0xFA0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_8_D24 end

    def Function_9_D37(): pass

    label("Function_9_D37")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    LoadChrToIndex("apl/ch51233.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("chr/ch02450.itc", 0x25)
    LoadChrToIndex("monster/ch85450.itc", 0x26)
    LoadChrToIndex("monster/ch60051.itc", 0x27)
    LoadChrToIndex("monster/ch85550.itc", 0x28)
    LoadChrToIndex("monster/ch60051.itc", 0x29)
    LoadChrToIndex("apl/ch51743.itc", 0x2A)
    LoadEffect(0x0, "event/ev602_01.eff")
    LoadEffect(0x1, "event/eva06_02.eff")
    LoadEffect(0x2, "event/eva06_01.eff")
    LoadEffect(0x3, "event/ev17013.eff")
    SoundLoad(128)
    SoundLoad(825)
    SoundLoad(832)
    SoundLoad(881)
    SoundLoad(833)
    SoundLoad(4064)
    SoundLoad(4077)
    SoundLoad(4065)
    SoundLoad(4066)
    SoundLoad(4067)
    SetChrPos(0x101, 0, 25000, 181800, 0)
    SetChrPos(0x102, 1100, 25000, 181100, 0)
    SetChrPos(0x103, 200, 25000, 180000, 0)
    SetChrPos(0x104, -1100, 25000, 180750, 0)
    SetChrPos(0xF4, -650, 25000, 179250, 0)
    SetChrPos(0xF5, 850, 25000, 179000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 12000, 210000, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 0, 12000, 198500, 0)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, -2500, 12000, 211500, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 2500, 12000, 211500, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    BeginChrThread(0xA, 2, 0, 29)
    BeginChrThread(0xB, 2, 0, 29)
    ClearChrFlags(0xC, 0x80)
    OP_68(0, 13000, 180500, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    Sleep(500)
    OP_68(0, 13000, 188000, 4500)
    MoveCamera(0, 38, 0, 4500)
    OP_6E(600, 4500)
    SetCameraDistance(24000, 4500)
    FadeToBright(1000, 0)

    def lambda_102A():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_102A)
    Sleep(50)

    def lambda_1042():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1042)
    Sleep(50)

    def lambda_105A():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_105A)
    Sleep(50)

    def lambda_1072():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1072)
    Sleep(50)

    def lambda_108A():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_108A)
    Sleep(50)

    def lambda_10A2():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_10A2)
    OP_0D()
    Sleep(2400)
    OP_C9(0x0, 0x80000000)

    #N0011
    NpcTalk(
        0x8,
        "男性の声",
        "#4064V#6P#30W#16A──至ったか。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    PlayBGM("ed7356", 0)
    BeginChrThread(0x101, 0, 0, 10)
    Sleep(50)
    BeginChrThread(0x102, 0, 0, 11)
    Sleep(50)
    BeginChrThread(0x103, 0, 0, 12)
    Sleep(50)
    BeginChrThread(0x104, 0, 0, 13)
    Sleep(50)
    BeginChrThread(0xF4, 0, 0, 14)
    Sleep(50)
    BeginChrThread(0xF5, 0, 0, 15)
    OP_68(-410, 13300, 205280, 4000)
    MoveCamera(47, 16, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(16180, 4000)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0012
    ChrTalk(
        0x101,
        "#00001F#12P……アリオスさん。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#00301F#12Pもう、あの長官の格好は\x01",
            "してねぇんだな……？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0014
    AnonymousTalk(
        0x8,
        (
            "クロイス氏の要請とはいえ、\x01",
            "元々、無理のある人事だからな。\x02\x03",

            "独立国の無効宣言があった以上、\x01",
            "俺にあれを着る資格はない。\x02\x03",

            "国防長官でも、遊撃士でもなく……\x02\x03",

            "ただの無頼の剣士として\x01",
            "ここに立っていると思うがいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1406")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13DE")
    OP_FC(0xFFF4)
    Jump("loc_13E1")

    label("loc_13DE")

    OP_FC(0xC)

    label("loc_13E1")


    #C0015
    ChrTalk(
        0x10A,
        "#00600F#13Pマクレイン……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1455")

    label("loc_1406")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1455")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1430")
    OP_FC(0xFFF4)
    Jump("loc_1433")

    label("loc_1430")

    OP_FC(0xC)

    label("loc_1433")


    #C0016
    ChrTalk(
        0x109,
        "#10113F#13Pアリオスさん……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1455")


    #C0017
    ChrTalk(
        0x102,
        "#00108F#12Pどうしてそこまで……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        "#00206F#12P……律儀すぎです。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0019
    ChrTalk(
        0x101,
        (
            "#00004F#12P……はは、参ったな……\x02\x03",

            "#00008F聞きたい事が色々ありすぎて\x01",
            "整理できていないんですけど……\x02\x03",

            "#00000Fまずは“答え合わせ”をしても\x01",
            "構いませんか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#01404Fああ#5P──元よりそのつもりだ。\x02\x03",

            "#01400F聞くがいい……\x01",
            "ただ１つのことを除いて\x01",
            "全てに答えよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#00003F#12Pそれでは……\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)

    label("loc_15EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A20")
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(0, 0)
    MenuCmd(1, 0, "５年前の“事故”について")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1647")
    MenuCmd(1, 0, "イアン弁護士との関係について")

    label("loc_1647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1670")
    MenuCmd(1, 0, "黒の競売会でのキーアについて")

    label("loc_1670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1697")
    MenuCmd(1, 0, "ガイが亡くなった日について")

    label("loc_1697")

    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16D1"),
        (1, "loc_234B"),
        (2, "loc_2D7F"),
        (3, "loc_3A13"),
        (SWITCH_DEFAULT, "loc_3A1B"),
    )


    label("loc_16D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2208")

    #C0022
    ChrTalk(
        0x101,
        (
            "#00008F#12P……辛いことを聞くようで\x01",
            "申し訳ありませんが……\x02\x03",

            "#00001F５年前の“事故”について\x01",
            "教えてもらえませんか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#01403F#5Pああ……\x01",
            "もはや隠す必要もあるまい。\x02\x03",

            "#01400F５年前、表通りで起きた\x01",
            "運搬車の爆発事故……\x02\x03",

            "お前たちも気付いているように、\x01",
            "あれは帝国と共和国の諜報戦の\x01",
            "結果として起きたものだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#00106F#12Pやはり……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1982")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_185D")
    OP_FC(0xFFF4)
    Jump("loc_1860")

    label("loc_185D")

    OP_FC(0xC)

    label("loc_1860")


    #C0025
    ChrTalk(
        0x10A,
        "#00608F#13P………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0026
    ChrTalk(
        0x8,
        (
            "#01402F#5Pフフ、当然一課では\x01",
            "その事実を把握していた筈だな？\x02\x03",

            "#01403Fそして帝国・共和国派に配慮した\x01",
            "上層部の判断で、当然のように\x01",
            "握りつぶされたわけだが……\x02\x03",

            "#01400Fその事自体に失望はあっても\x01",
            "今さら恨みはない。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x10A,
        "#00606F#13P……言葉も無い。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1982")


    #C0028
    ChrTalk(
        0x103,
        (
            "#00208F#12P……それでアリオスさんの\x01",
            "奥さんとシズクちゃんは……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#01403F#5Pああ……サヤの命は失われ、\x01",
            "シズクの光は奪われた。\x02\x03",

            "#01408Fあれから５年……\x01",
            "両国の諜報機関が整備されたことで\x01",
            "無為な破壊工作は無くなったが……\x02\x03",

            "#01401F数十年に渡る暗闘の結果、\x01",
            "サヤたちと同じような被害者は\x01",
            "少なからず出ていた。\x02\x03",

            "#01403Fロイド──お前の両親や\x01",
            "イアン先生の家族を含めてな。\x02",
        )
    )

    CloseMessageWindow()
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0030
    ChrTalk(
        0x101,
        "#00005F#12P#4S！？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        "#00307F#12Pなんだと……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 6)), scpexpr(EXPR_END)), "loc_1CE2")

    #C0032
    ChrTalk(
        0x102,
        (
            "#00101F#12Pロ、ロイドのご両親って\x01",
            "確か……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        "#00208F#12P１５年前の飛行船事故で……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#00006F#12Pああ……前に話した通りだ。\x02\x03",

            "#00008F俺は物心付いたばかりで\x01",
            "ほとんど覚えていないけど……\x02\x03",

            "#00013Fじゃあ、その時に……\x01",
            "イアン先生の家族というのも？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DFD")

    label("loc_1CE2")


    #C0035
    ChrTalk(
        0x102,
        "#00105F#12Pロ、ロイドのご両親が！？\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        "#00206F#12P……初耳です……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#00006F#12P俺の両親は……\x01",
            "１５年前、就航したばかりの\x01",
            "飛行船の事故で亡くなっている……\x02\x03",

            "#00008F俺は物心付いたばかりで\x01",
            "ほとんど覚えていないけど……\x02\x03",

            "#00013Fじゃあ、その時に……\x01",
            "イアン先生の家族というのも？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DFD")


    #C0038
    ChrTalk(
        0x8,
        (
            "#01403F#5Pああ、奥さんとお子さん２人が\x01",
            "それに乗っていたと聞いている。\x02\x03",

            "俺にはシズクが残されたが……\x01",
            "全てを失った彼の嘆きと哀しみは\x01",
            "想像も付かないくらいだろう。\x02\x03",

            "#01400Fそしてその時、ガイとイアン先生も\x01",
            "同じ遺族として知り合っている筈だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#00001F#12P……………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F70")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F45")
    OP_FC(0xFFF4)
    Jump("loc_1F48")

    label("loc_1F45")

    OP_FC(0xC)

    label("loc_1F48")


    #C0040
    ChrTalk(
        0x109,
        "#10106F#13P……そ、そんな事が……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1F70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FDA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F9A")
    OP_FC(0xFFF4)
    Jump("loc_1F9D")

    label("loc_1F9A")

    OP_FC(0xC)

    label("loc_1F9D")


    #C0041
    ChrTalk(
        0x10A,
        (
            "#00606F#13Pその情報は一課でも\x01",
            "把握されていなかった……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1FDA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2044")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2004")
    OP_FC(0xFFF4)
    Jump("loc_2007")

    label("loc_2004")

    OP_FC(0xC)

    label("loc_2007")


    #C0042
    ChrTalk(
        0x105,
        (
            "#10401F#13P……なるほど。\x01",
            "そんな因縁があったとはね……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2044")


    #C0043
    ChrTalk(
        0x8,
        (
            "#01403F#5P……そして５年前の事件の後、\x01",
            "俺は警察を辞め、\x01",
            "遊撃士協会の門戸を叩いた。\x02\x03",

            "警察への失望、シズクの入院費用の捻出、\x01",
            "色々と理由はあったが……\x02\x03",

            "#01408F単に、サヤを失った哀しみから\x01",
            "逃れたかっただけかもしれない。\x02\x03",

            "#01400Fその気になれば幾らでもある\x01",
            "遊撃士の仕事に没頭することでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#00008F#12Pアリオスさん……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2200")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21B0")
    OP_FC(0xFFF4)
    Jump("loc_21B3")

    label("loc_21B0")

    OP_FC(0xC)

    label("loc_21B3")


    #C0045
    ChrTalk(
        0x106,
        (
            "#10706F#13P（……今まで《銀#2Rイン#》が殺めた\x01",
            "  標的たちの家族も……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2200")

    SetScenarioFlags(0x0, 0)
    Jump("loc_2346")

    label("loc_2208")


    #C0046
    ChrTalk(
        0x8,
        (
            "#01403F#5P５年前、表通りで起きた\x01",
            "サヤの命とシズクの光を奪った\x01",
            "運搬車の爆発事故……\x02\x03",

            "#01401Fあれは帝国と共和国の\x01",
            "諜報戦の結果起きたものだった。\x02\x03",

            "そして１５年前の飛行船事故も\x01",
            "同じ理由で起きている。\x02\x03",

            "#01403Fその結果……ガイとお前の両親や\x01",
            "イアン先生の家族の命が奪われた。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#00008F#12P……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2346")

    Jump("loc_3A1B")

    label("loc_234B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C91")

    #C0048
    ChrTalk(
        0x101,
        (
            "#00006F#12P……ずっと疑問に思っていた\x01",
            "事があったんです。\x02\x03",

            "#00001Fどうしてディーターさんたちと\x01",
            "貴方の存在が結び付くのかと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0049
    ChrTalk(
        0x8,
        "#01405F#5Pほう……？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        (
            "#00106F#12P……確かにおじさまやベルは\x01",
            "経済や金融、クロイス家に関係する\x01",
            "教団の情報には詳しそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#00303F#12P帝国と共和国の水面下での暗闘……\x02\x03",

            "#00301Fそのあたりの事情にまで\x01",
            "通じているのは違和感があるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        (
            "#00203F#12Pお互い接点が無い両名……\x02\x03",

            "#00201Fなのに大統領になったディーターさんは\x01",
            "アリオスさんを国防長官に指名した……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2623")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2585")
    OP_FC(0xFFF4)
    Jump("loc_2588")

    label("loc_2585")

    OP_FC(0xC)

    label("loc_2588")


    #C0053
    ChrTalk(
        0x10A,
        (
            "#00606F#13P……なるほど、そういう事か。\x02\x03",

            "#00601Fその両者を結びつけたのが\x01",
            "イアン先生だったという訳か。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00001F#12Pええ……\x01",
            "──違いますか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2796")

    label("loc_2623")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_264D")
    OP_FC(0xFFF4)
    Jump("loc_2650")

    label("loc_264D")

    OP_FC(0xC)

    label("loc_2650")


    #C0055
    ChrTalk(
        0x105,
        (
            "#10406F#13P……なるほど、そういう事か。\x02\x03",

            "#10401Fその両者を結びつけたのが\x01",
            "あの熊ヒゲ先生だった訳だね？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0056
    ChrTalk(
        0x101,
        (
            "#00001F#12Pああ……\x01",
            "──違いますか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2796")

    label("loc_26EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2796")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2715")
    OP_FC(0xFFF4)
    Jump("loc_2718")

    label("loc_2715")

    OP_FC(0xC)

    label("loc_2718")


    #C0057
    ChrTalk(
        0x109,
        (
            "#10108F#13Pひょっとして……\x02\x03",

            "#10101Fその両者を結びつけたのが\x01",
            "イアン先生……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00001F#12Pああ……\x01",
            "──違いますか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2796")


    #C0059
    ChrTalk(
        0x8,
        "#01404F#5Pフフ……その通りだ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 224, 0, 480, 256, 10, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0060
    AnonymousTalk(
        0x8,
        (
            "#01402F警察時代、お前たちと同じく、\x01",
            "俺とガイもイアン先生の情報には\x01",
            "随分と助けられたものだった。\x02\x03",

            "教団のロッジ制圧作戦でも\x01",
            "民間のアドバイザーとして\x01",
            "協力していたくらいの情報通だ。\x02\x03",

            "#01403Fそして遊撃士になった後も……\x01",
            "彼とは頻繁に情報交換していた。\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(1, 224, 0, 480, 256, 65296, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    OP_CB(0x1, 0x3, 0xAAFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0061
    AnonymousTalk(
        0x8,
        (
            "#01403F#5P一方で先生は、ＩＢＣの法務を通じて\x01",
            "クロイス父娘と昔から親交があった。\x02\x03",

            "#01401Fそして──あらゆる情報と要素は\x01",
            "先生のところに集約・統合され……\x02\x03",

            "クロイス氏は彼に誘導されるまま、\x01",
            "様々な政治工作と《至宝》の力による\x01",
            "クロスベル独立を成し遂げた。\x02\x03",

            "#01403Fその裏で、彼とマリアベル嬢によって\x01",
            "真の計画が進められているとも知らずに。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(800, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_0D()
    Sleep(300)

    #C0062
    ChrTalk(
        0x101,
        "#00013F#12P真の計画……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        "#00108F#12P『碧き零の計画』ですか……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "#01403F#5Pそう……サヤたちの事故についても\x01",
            "先生はいち早く真相に気付いていた。\x02\x03",

            "そして俺に事情を打ち明け……\x01",
            "俺も計画に協力する事となった。\x02\x03",

            "#01400Fこれが経緯#4Rいきさつ#の全てだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#00008F#12P………………………………\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#00206F#12P全てはイアン先生と\x01",
            "マリアベルさんの掌#2Rてのひら#の上……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        "#00301F#12P……とんでもねぇ話だぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D7A")

    label("loc_2C91")


    #C0068
    ChrTalk(
        0x8,
        (
            "#01403F#5Pクロイス氏と俺……\x01",
            "接点のない２人を結びつけたのが\x01",
            "他ならぬイアン先生だった。\x02\x03",

            "彼は、５年前の事故についても\x01",
            "いち早く真相に気付いて\x01",
            "俺を『碧#2Rあお#き零#2Rゼロ#の計画』へと誘い……\x02\x03",

            "#01400Fそして俺もまた、それに応じた。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7A")

    Jump("loc_3A1B")

    label("loc_2D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B0")

    #C0069
    ChrTalk(
        0x101,
        (
            "#00006F#12P……これも同じく、\x01",
            "疑問に思っていた事ですが……\x02\x03",

            "#00013Fキーアを《太陽の砦》の地下から\x01",
            "連れ出したのはアリオスさんですね？\x02\x03",

            "そして《黒の競売会》に出品される\x01",
            "ローゼンベルク人形と入れ替えたのも。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        "#00105F#12Pそ、そういえば……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        (
            "#00206F#12P確かにその問題も完全には\x01",
            "明らかになっていませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "#01404F#5Pああ、その通りだ。\x02\x03",

            "#01402Fそれに関しては先生ではなく、\x01",
            "マリアベル嬢の主導だったがな。\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis303.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis304.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0073
    AnonymousTalk(
        0x8,
        (
            "#01403Fどうやら彼女はヨアヒムの動きを\x01",
            "完全に把握していたようでな……\x02\x03",

            "#01401F彼女の転位術で俺たちは容易く\x01",
            "最下層の祭壇に辿りつき、\x01",
            "あの子を揺籃#4Rゆりかご#から解放した。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0074
    AnonymousTalk(
        0x8,
        (
            "#01403Fそして俺は、レミフェリア方面から\x01",
            "運ばれてきたローゼンベルク人形と\x01",
            "あの子をすり替えた。\x02\x03",

            "#01400Fそのローゼンベルク人形自体も\x01",
            "ルバーチェ側に気づかれないように\x01",
            "マリアベル嬢が用意したものだがな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, -1, 3)

    #A0075
    AnonymousTalk(
        0x102,
        "#00106F……そんな事まで……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)

    #C0076
    ChrTalk(
        0x101,
        (
            "#00006F#12Pしかし……\x01",
            "そんな事をしてマリアベルさんに\x01",
            "何の意味があったんですか？\x02\x03",

            "#00013F計画にキーアが必要ならそのまま\x01",
            "保護すれば良かったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "#01403F#5P一つは《黒月#4Rヘイユエ#》も巻き込んで\x01",
            "ルバーチェ側の面目を失墜させ、\x01",
            "自滅の第一歩とすること……\x02\x03",

            "#01400Fもし、競売会の場で\x01",
            "彼女が目覚めることになったら\x01",
            "マリアベル嬢が動いたはずだ。\x02\x03",

            "動揺する客とマルコーニを前に\x01",
            "ＩＢＣの名を出してあの子の保護を\x01",
            "買って出るつもりだったのだろう。\x02\x03",

            "#01404F《黒月》が動いたら\x01",
            "別の展開もあっただろうが……\x02\x03",

            "いずれにせよ、あの時は\x01",
            "この俺も会場内に潜伏していた#28R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲#。\x02\x03",

            "#01402Fどんな展開になったとしても\x01",
            "収拾できる態勢は整っていたわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        (
            "#00306F#12Pなんつーか……\x01",
            "ウルトラＣすぎんだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        "#00211F#12P用意周到すぎます……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3540")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34E2")
    OP_FC(0xFFF4)
    Jump("loc_34E5")

    label("loc_34E2")

    OP_FC(0xC)

    label("loc_34E5")


    #C0080
    ChrTalk(
        0x106,
        (
            "#10708F#13P……確かにあの時、\x01",
            "他にも何者かが潜んでいるような\x01",
            "気配を感じましたけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3540")


    #C0081
    ChrTalk(
        0x8,
        (
            "#01403F#5Pそしてもう一つは……\x02\x03",

            "#01401Fあのような特異な状況で\x01",
            "《至宝》を目覚めさせることで\x01",
            "潜在能力を見極めるという事だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0082
    ChrTalk(
        0x103,
        "#00205F#12Pキーアの潜在能力を見極める？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        "#00101F#12Pど、どういう事ですか……？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "#01403F#5Pさて──マリアベル嬢が\x01",
            "そう言っていたというだけだ。\x02\x03",

            "#01408F恐らく、あの子を長き眠りから\x01",
            "目覚めさせる条件の一つなのかも\x01",
            "しれないが……\x02\x03",

            "#01400Fいずれにせよ、女神の導きか、\x01",
            "それとも単なる偶然か、\x01",
            "彼女はお前たちの前で目覚めた。\x02\x03",

            "マリアベル嬢にしたら\x01",
            "完全に想定外だった筈だが……\x02\x03",

            "#01403Fあの子がお前たちに引き取られ、\x01",
            "一緒に暮らす事になったのも含めて\x01",
            "歓迎しているかのようだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#00008F#12P………………………………\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#00306F#12P……ダメだ。\x01",
            "ワケが分からねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        (
            "#00108F#12P……ベル……\x01",
            "いったい何のつもりで……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A0E")

    label("loc_38B0")


    #C0088
    ChrTalk(
        0x8,
        (
            "#01403F#5P《太陽の砦》からキーアを解放し、\x01",
            "競売会の場に運び込んだのは\x01",
            "マリアベル嬢の主導によるものだ。\x02\x03",

            "#01408Fその狙いは、ルバーチェを崩壊に導き、\x01",
            "状況をコントロールするためでも\x01",
            "あったようだが……\x02\x03",

            "#01401F特異な状況で彼女を目覚めさせ、\x01",
            "潜在能力を見極めるという目的も\x01",
            "一方ではあったようだ。\x02\x03",

            "#01403Fそれ以上のことは\x01",
            "残念ながら俺にも分からない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0E")

    Jump("loc_3A1B")

    label("loc_3A13")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3A1B")

    label("loc_3A1B")

    Jump("loc_15EA")

    label("loc_3A20")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0089
    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W……それじゃあ……\x02\x03",

            "#00008F兄貴が亡くなった日の事……\x01",
            "……その真実を教えて貰えますか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AEE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3ACD")
    OP_FC(0xFFF4)
    Jump("loc_3AD0")

    label("loc_3ACD")

    OP_FC(0xC)

    label("loc_3AD0")


    #C0090
    ChrTalk(
        0x10A,
        "#00601F#13P……っ………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3AEE")


    #C0091
    ChrTalk(
        0x103,
        "#00208F#12P……ぁ………\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        "#01403F#5P#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0093
    ChrTalk(
        0x8,
        "#01400F#5P#30Wいいだろう──\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sound(883, 0, 60, 0)
    Sleep(2300)
    Sound(128, 2, 10, 0)
    Sleep(150)
    OP_25(0x80, 0x14)
    Sleep(150)
    OP_25(0x80, 0x1E)
    Sleep(150)
    OP_25(0x80, 0x28)
    Sleep(150)
    OP_25(0x80, 0x32)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0094
    AnonymousTalk(
        0x8,
        (
            "#3C#30W……サヤを亡くして\x01",
            "警察を離れてから２年……\x02\x03",

            "俺はイアン先生たちの計画に協力し、\x01",
            "幾つもの工作を成し遂げていた……\x02\x03",

            "いずれも後ろ暗い……\x01",
            "陰謀めいた工作ばかりだ。\x02\x03",

            "だが、ギルド関係者を始め、\x01",
            "それを誰かに感付かれることは\x01",
            "遂になかった。\x02\x03",

            "ガイ・バニングス……\x01",
            "かつての俺の相棒を除いては。\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7560", 0)
    CreatePortrait(0, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07800.itp")
    OP_CB(0x0, 0x3, 0xEEFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0095
    AnonymousTalk(
        0x8,
        (
            "#3C#30Wガイは……あいつは\x01",
            "凄まじいほどの嗅覚と粘り強さで\x01",
            "様々な陰謀と秘密に迫っていた。\x02\x03",

            "帝国と共和国による暗闘……\x02\x03",

            "ハルトマン議長とルバーチェ、\x01",
            "そしてＤ∴Ｇ教団残党の動き……\x02\x03",

            "その更に背後にある、\x01",
            "クロイス家の計画にまで……\x02\x03",

            "そして──\x02\x03",

            "あの雨の日、ガイは俺を\x01",
            "着工したばかりのオルキスタワーの\x01",
            "建設現場に呼び出した……\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_25(0x80, 0x3C)
    Sleep(200)
    OP_25(0x80, 0x46)
    Sleep(200)
    OP_25(0x80, 0x50)
    Sleep(200)
    OP_25(0x80, 0x5A)
    Sleep(200)
    OP_25(0x80, 0x64)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis305.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0096
    AnonymousTalk(
        0x8,
        (
            "#3C#30W無論、計画の詳細までは\x01",
            "掴んでいなかったが……\x02\x03",

            "ガイの推測は驚くほど的確で\x01",
            "計画の全体像を捉えていた。\x02\x03",

            "教団とマフィアを利用した\x01",
            "クロイス氏の政界進出……\x02\x03",

            "外国勢力の仕業に見せかけて\x01",
            "クロスベル市を襲撃させることで\x01",
            "独立の気運を煽ること……\x02\x03",

            "更にはクロイス家の“何か”で\x01",
            "大陸全土を威圧・主導する事……\x02\x03",

            "信じ難いことに\x01",
            "そんな事まで指摘してのけた。\x02\x03",

            "そして──\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 0, 512, 512, 0, 65296, 512, 512, 0, 0, 512, 512, 0xFF000000, 0x0, "c_vis330.itp")
    CreatePortrait(1, 0, 0, 512, 512, 0, 0, 512, 512, 0, 0, 512, 512, 0xFFFFFF, 0x0, "c_vis331.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x7D0, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFC5680, 0x7D0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x0)
    OP_CB(0x1, 0x3, 0xFF000000, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(534, 0, 80, 0)
    Sleep(100)
    PlayEffect(0x3, 0x3, 0xC, 0x0, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(372, 0, 40, 0)
    Sleep(200)
    Sound(540, 0, 100, 0)
    Sound(511, 0, 100, 0)
    Sleep(400)
    Sound(540, 0, 100, 0)
    Sound(372, 0, 40, 0)
    Sound(566, 0, 50, 0)
    Sleep(200)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis306.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(50)
    BeginChrThread(0x8, 0, 0, 30)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0097
    AnonymousTalk(
        0x8,
        (
            "#3C#30W……手を引けという\x01",
            "俺の言葉をガイは受け入れず……\x02\x03",

            "俺たちは雨の中、死闘を始めた。\x02\x03",

            "武術の腕は俺がやや上……\x01",
            "だが、ガイには揺るぎない\x01",
            "意志による力がみなぎっていた。\x02\x03",

            "何十合と打ち合い、\x01",
            "お互いの体力を奪い合いながら\x01",
            "雨の中の死闘は続き……\x02\x03",

            "そして──\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(800)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis307.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0098
    AnonymousTalk(
        0x8,
        (
            "#3C#30Wそしてガイは……\x01",
            "命を落とすこととなった。\x02\x03",

            "当然、あいつのトンファーを\x01",
            "現場から持ち去ったのは俺だ。\x02\x03",

            "トンファーに無数に刻まれた刀傷から\x01",
            "犯人を特定されたくなかったからだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    StopSound(128, 1000, 100)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4514")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44BD")
    OP_FC(0xFFF4)
    Jump("loc_44C0")

    label("loc_44BD")

    OP_FC(0xC)

    label("loc_44C0")


    #C0099
    ChrTalk(
        0x109,
        "#10106F#13P#30Wそんな事が……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0100
    ChrTalk(
        0x103,
        "#00208F#12P#30W……………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_456A")

    label("loc_4514")


    #C0101
    ChrTalk(
        0x101,
        "#00008F#12P#30W……………………………\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        "#00206F#12P#30W……そんな事が…………\x02",
    )

    CloseMessageWindow()

    label("loc_456A")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(500)

    #C0103
    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W……これがあの雨の日、\x01",
            "起こった事件のあらましだ。\x02\x03",

            "#01408Fその後、マフィアの手下が現れ、\x01",
            "ガイのバッジを持って行かれたのは\x01",
            "さすがに想定外だったが……\x02\x03",

            "#01400Fいずれにしても、これで大体の\x01",
            "疑問には答えられただろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#00003F#12P───いえ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0105
    ChrTalk(
        0x8,
        "#01405F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#00006F#12P当然知っているでしょうが、\x01",
            "兄貴の死因は銃撃#4R㈲　㈲#によるものです。\x02\x03",

            "#00001Fその事についての説明が\x01",
            "無かったみたいですが……？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "#01403F#5P……警察にいた頃に\x01",
            "拳銃の扱いは習得している。\x02\x03",

            "#01401Fしつこく喰い下がってくる\x01",
            "面倒な相手に業を煮やして\x01",
            "使ったまでだが……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_480D")
    OP_FC(0xFFF4)
    Jump("loc_4810")

    label("loc_480D")

    OP_FC(0xC)

    label("loc_4810")


    #C0108
    ChrTalk(
        0x10A,
        (
            "#00606F#13P嘘だな──マクレイン。\x02\x03",

            "#00601Fそのような死闘の中で\x01",
            "別の得物を構える余裕など\x01",
            "あるものか。\x02\x03",

            "ましてや相手の背中から\x01",
            "止めを刺すなど不可能だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4956")

    label("loc_48B0")


    #C0109
    ChrTalk(
        0x101,
        (
            "#00013F#12P──それは嘘だ。\x02\x03",

            "#00006Fそんな死闘の中で\x01",
            "別の得物を構える余裕など\x01",
            "ある訳がないでしょう。\x02\x03",

            "#00001Fましてや相手の背中から\x01",
            "止めを刺すなんて不可能です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4956")

    StopBGM(0xFA0)

    #C0110
    ChrTalk(
        0x8,
        "#01401F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x104,
        "#00303F#12Pまあ、道理ってヤツだな。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#00108F#12Pいったい“誰”が\x01",
            "ガイさんを撃ったのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#00201F#12P……話してください。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 22)
    WaitChrThread(0x8, 0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7356", 0)
    MoveCamera(43, 13, 0, 20000)
    Sleep(500)

    #C0114
    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W──何を言われようと\x01",
            "ガイを死に追いやったのは\x01",
            "俺以外の何者でもない。\x02\x03",

            "#01400Fそして俺は……\x01",
            "かつての相棒を犠牲にしてまで\x01",
            "計画に協力する道を選んだ。\x02\x03",

            "そして今もなお……\x01",
            "いたいけな少女の想いを利用して\x01",
            "計画を完了させようとしている。\x02\x03",

            "#01403F全てはサヤのため……\x01",
            "そしてシズクの未来のために。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        "#00001F#12P……アリオスさん……\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        (
            "#00108F#12Pシズクちゃんがこんな事して\x01",
            "喜ぶとでも……？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W無論、喜ぶわけがない。\x02\x03",

            "#01401Fだが──\x01",
            "クロスベルという地の呪いは\x01",
            "あの子から母と光を奪った。\x02\x03",

            "そしてクロスベルが\x01",
            "大陸のこの位置にある以上、\x01",
            "呪いは決して消えることはない。\x02\x03",

            "#01403F──人の世の理を超越した\x01",
            "“奇蹟”でも起きない限りは。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#00005F#12P……！？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 23)
    WaitChrThread(0x8, 0)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0119
    ChrTalk(
        0x8,
        (
            "#01400F#5P#30W３年前ガイは……\x01",
            "俺のことを一言も責めず、\x01",
            "死闘の果てに命を落とした。\x02\x03",

            "そして《至宝》となった彼女#4Rキーア#は\x01",
            "シズクの目を治してくれた。\x02\x03",

            "#01403Fもはや──\x01",
            "後戻りできる道理はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetCameraDistance(15370, 800)
    BeginChrThread(0x8, 0, 0, 24)
    Sleep(500)
    PlayEffect(0x1, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    Sound(825, 2, 50, 0)
    Sound(832, 2, 100, 0)
    Sound(881, 0, 50, 0)
    Sound(833, 0, 50, 0)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x8,
        (
            "#01403F#5P#30W……承服できなければ\x01",
            "力をもって止めてみるがいい。\x02\x03",

            "#01401F兄の遺#2Rのこ#したそのトンファーで……\x02\x03",

            "#01407F見事、兄の仇を討って\x01",
            "大切なものを取り戻すための道を\x01",
            "切り拓いてみせるがいい……！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0121
    ChrTalk(
        0x101,
        (
            "#00006F#12P……分かりました。\x02\x03",

            "#00001Fだが──兄貴の仇を\x01",
            "取るつもりは毛頭ありません。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    BeginChrThread(0x101, 0, 0, 16)
    WaitChrThread(0x101, 0)
    PlayEffect(0x2, 0x0, 0x101, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(881, 0, 50, 0)
    Sound(833, 0, 50, 0)
    OP_25(0x339, 0x46)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7527", 0)
    SetCameraDistance(18370, 20000)
    Sleep(1000)

    #C0122
    ChrTalk(
        0x101,
        (
            "#00003F#12Pガイ・バニングスの\x01",
            "意志を継いで立ち上げられた\x01",
            "ささやかな部署として……\x02\x03",

            "#00001Fシズクちゃんを始め、\x01",
            "大勢の人々の想いを託された\x01",
            "《特務支援課》として……\x02\x03",

            "#00007F貴方という《壁》を乗り越え、\x01",
            "キーアを取り戻して……\x01",
            "本当の意味で事件を解決してみせる！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0123
    ChrTalk(
        0x8,
        "#01405F#5P……！\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#00302F#12Pハハ……\x01",
            "さすがは俺らのリーダー！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        (
            "#00101F#12Pオルキスタワーで待っている\x01",
            "シズクちゃんのためにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x103,
        "#00201F#12P……絶対に退#2Rひ#けません……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5270")
    OP_FC(0xFFF4)
    Jump("loc_5273")

    label("loc_5270")

    OP_FC(0xC)

    label("loc_5273")


    #C0127
    ChrTalk(
        0x10A,
        (
            "#00604F#13Pフッ……\x01",
            "仕方のないヤツらだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_52A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5302")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52CC")
    OP_FC(0xFFF4)
    Jump("loc_52CF")

    label("loc_52CC")

    OP_FC(0xC)

    label("loc_52CF")


    #C0128
    ChrTalk(
        0x105,
        (
            "#10402F#13Pフフ……\x01",
            "このノリが支援課だよね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5302")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5353")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_532C")
    OP_FC(0xFFF4)
    Jump("loc_532F")

    label("loc_532C")

    OP_FC(0xC)

    label("loc_532F")


    #C0129
    ChrTalk(
        0x109,
        "#10107F#13P全力で援護します！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5353")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53E1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_537D")
    OP_FC(0xFFF4)
    Jump("loc_5380")

    label("loc_537D")

    OP_FC(0xC)

    label("loc_5380")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53B9")

    #C0130
    ChrTalk(
        0x106,
        "#10701F#13P私も……力の限り！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_53E1")

    label("loc_53B9")


    #C0131
    ChrTalk(
        0x106,
        "#10707F#13P全力でお手伝いします！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_53E1")

    BeginChrThread(0x102, 0, 0, 17)
    BeginChrThread(0x103, 0, 0, 18)
    BeginChrThread(0x104, 0, 0, 19)
    BeginChrThread(0xF4, 0, 0, 20)
    BeginChrThread(0xF5, 0, 0, 21)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0132
    ChrTalk(
        0x8,
        "#01404F#4077V#5P#30W#35Aフフ──いいだろう。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x8, 0, 0, 25)
    WaitChrThread(0x8, 0)
    Sound(817, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 27)
    BeginChrThread(0xB, 3, 0, 28)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_68(180, 13300, 207000, 20000)
    MoveCamera(43, 13, 0, 20000)
    SetCameraDistance(14120, 20000)
    CreatePortrait(0, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu01402.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    BeginChrThread(0x8, 0, 0, 26)

    #A0133
    AnonymousTalk(
        0x8,
        (
            "#4065V#40W#70A八葉一刀流、ニの型奥義皆伝、\x01",
            "アリオス・マクレイン……\x02\x03",

            "#4066V#74A一身上の都合により、義に背き、\x01",
            "道を外れ、勝手を貫かせてもらう！\x02\x03",

            "#4067V#30A来るがいい──特務支援課！\x02",
        )
    )
    #Auto

    WaitChrThread(0x8, 0)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)
    SetMessageWindowPos(330, 100, -1, -1)
    SetChrName("ロイドたち")
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #A0134
    AnonymousTalk(
        0xFF,
        "#4S#12Aおおっ！\x02",
    )
    #Auto

    Sound(2153, 255, 90, 0)    #voice#Elie
    Sound(2343, 255, 100, 1)    #voice#Randy
    Sound(2249, 255, 100, 2)    #voice#Tio
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_568B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5682")
    OP_FC(0x4)
    Sound(2478, 255, 100, 4)    #voice#Noel
    Jump("loc_568B")

    label("loc_5682")

    OP_FC(0x3)
    Sound(2478, 255, 100, 3)    #voice#Noel

    label("loc_568B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56B8")
    Sound(2417, 255, 100, 4)    #voice#Lazy
    Jump("loc_56BE")

    label("loc_56B8")

    Sound(2417, 255, 100, 3)    #voice#Lazy

    label("loc_56BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56EB")
    Sound(2544, 255, 100, 4)    #voice#Dudley
    Jump("loc_56F1")

    label("loc_56EB")

    Sound(2544, 255, 100, 3)    #voice#Dudley

    label("loc_56F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5724")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_571E")
    Sound(3174, 255, 100, 4)    #voice#Rixia
    Jump("loc_5724")

    label("loc_571E")

    Sound(3174, 255, 100, 3)    #voice#Rixia

    label("loc_5724")

    Sound(2055, 255, 100, 5)    #voice#Lloyd
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Battle("BattleInfo_2B8", 0x0, 0x0, 0x100, 0x45, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Call(0, 31)
    Return()

    # Function_9_D37 end

    def Function_10_575F(): pass

    label("Function_10_575F")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0x2EE0, 0x318BC, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_10_575F end

    def Function_11_578A(): pass

    label("Function_11_578A")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0x2EE0, 0x313E4, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_578A end

    def Function_12_57B5(): pass

    label("Function_12_57B5")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0x2EE0, 0x30EB2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_57B5 end

    def Function_13_57E0(): pass

    label("Function_13_57E0")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0x2EE0, 0x3116E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_57E0 end

    def Function_14_580B(): pass

    label("Function_14_580B")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0x2EE0, 0x313DA, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_580B end

    def Function_15_5836(): pass

    label("Function_15_5836")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0x2EE0, 0x31312, 0xFA0, 0x0)
    Return()

    # Function_15_5836 end

    def Function_16_585A(): pass

    label("Function_16_585A")

    Sleep(150)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_585A end

    def Function_17_586C(): pass

    label("Function_17_586C")

    Sleep(300)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_586C end

    def Function_18_587E(): pass

    label("Function_18_587E")

    Sleep(450)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_587E end

    def Function_19_5890(): pass

    label("Function_19_5890")

    Sleep(450)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_5890 end

    def Function_20_589C(): pass

    label("Function_20_589C")

    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58BC")
    Sound(540, 0, 50, 0)
    Jump("loc_58E1")

    label("loc_58BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_58E1")
    Sound(531, 0, 100, 0)

    label("loc_58E1")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_589C end

    def Function_21_58EA(): pass

    label("Function_21_58EA")

    Sleep(750)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_590A")
    Sound(540, 0, 50, 0)
    Jump("loc_592F")

    label("loc_590A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_592F")
    Sound(531, 0, 100, 0)

    label("loc_592F")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_58EA end

    def Function_22_5938(): pass

    label("Function_22_5938")

    SetChrChipByIndex(0x8, 0x2A)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    Return()

    # Function_22_5938 end

    def Function_23_5961(): pass

    label("Function_23_5961")

    SetChrChipByIndex(0x8, 0x2A)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    Sound(932, 0, 60, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    SetChrSubChip(0xFE, 0x4)
    Sleep(375)
    SetChrSubChip(0xFE, 0x5)
    Sleep(125)
    Sound(859, 0, 100, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(125)
    SetChrSubChip(0xFE, 0x7)
    Sleep(500)
    Return()

    # Function_23_5961 end

    def Function_24_59AB(): pass

    label("Function_24_59AB")

    SetChrSubChip(0xFE, 0x7)
    Sleep(125)
    SetChrSubChip(0xFE, 0x8)
    Sleep(125)
    SetChrSubChip(0xFE, 0x9)
    Sleep(125)
    SetChrSubChip(0xFE, 0xA)
    Sleep(125)
    Sound(812, 0, 100, 0)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0xB)
    Return()

    # Function_24_59AB end

    def Function_25_59D8(): pass

    label("Function_25_59D8")

    SetChrSubChip(0xFE, 0xB)
    Sleep(125)
    SetChrSubChip(0xFE, 0xC)
    Sleep(125)
    SetChrSubChip(0xFE, 0xD)
    Sleep(125)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0xE)
    Sleep(250)
    Sound(859, 0, 60, 0)
    Sleep(250)
    Return()

    # Function_25_59D8 end

    def Function_26_5A04(): pass

    label("Function_26_5A04")

    SetChrSubChip(0xFE, 0xE)
    Sleep(91)
    Sound(540, 0, 40, 0)
    SetChrSubChip(0xFE, 0xF)
    Sleep(91)
    SetChrSubChip(0xFE, 0x10)
    Sleep(91)
    SetChrSubChip(0xFE, 0x11)
    Sleep(364)
    Return()

    # Function_26_5A04 end

    def Function_27_5A27(): pass

    label("Function_27_5A27")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_27_5A27 end

    def Function_28_5A70(): pass

    label("Function_28_5A70")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_28_5A70 end

    def Function_29_5AB9(): pass

    label("Function_29_5AB9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5AD4")
    OP_A1(0xFE, 0x4B0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_29_5AB9")

    label("loc_5AD4")

    Return()

    # Function_29_5AB9 end

    def Function_30_5AD5(): pass

    label("Function_30_5AD5")

    OP_CB(0x0, 0x0, 0xFFFFE0C0, 0x0, 0x6E, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x1770, 0x0, 0x5A, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFF060, 0x0, 0x46, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x7D0, 0x0, 0x32, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1E, 0x0)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_30_5AD5 end

    def Function_31_5B49(): pass

    label("Function_31_5B49")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("apl/ch51744.itc", 0x26)
    LoadEffect(0x0, "event/ev17084.eff")
    LoadEffect(0x1, "event/ev17085.eff")
    SoundLoad(128)
    SoundLoad(4078)
    SoundLoad(4079)
    OP_68(-80, 13300, 209040, 0)
    MoveCamera(358, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(16500, 2500)
    SetChrPos(0x101, 0, 12000, 207440, 0)
    SetChrPos(0x102, 1120, 12000, 206200, 0)
    SetChrPos(0x103, 420, 12000, 204870, 0)
    SetChrPos(0x104, -1270, 12000, 205570, 0)
    SetChrPos(0xF4, -2540, 11990, 206190, 0)
    SetChrPos(0xF5, 2540, 12000, 205990, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 12000, 211500, 180)
    BeginChrThread(0x8, 0, 0, 32)
    OP_68(0, 13000, 210000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(15800, 12000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_C9(0x0, 0x80000000)

    #C0135
    ChrTalk(
        0x8,
        (
            "#01404F#4078V#5P#80W#30A………フフ…………\x02\x03",

            "#4079V#60Aロイド……他の者たちも……\x01",
            "……本当に強くなったな。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 13100, 208700, 0)
    MoveCamera(46, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14680, 0)
    EndChrThread(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    OP_0D()
    Sleep(500)

    #C0136
    ChrTalk(
        0x101,
        (
            "#00006F#12P#40W……はあっ……はあっ……\x02\x03",

            "#00008Fだとしたら……アリオスさんが\x01",
            "目標になってくれたからです……\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        (
            "#00306F#12P#40W確かに……アンタがいなけりゃ\x01",
            "ここまでは行けなかったかもな……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        "#00206F#12P#40W……同感です……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x102,
        (
            "#00108F#12P#40Wいつも目指すべき《壁》として\x01",
            "遥か先に居てくれましたから……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "#01402F#5P#40Wフフ……まったく……\x02\x03",

            "#01404Fそのように言われる資格など\x01",
            "そもそも無いというのに……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0141
    ChrTalk(
        0x101,
        (
            "#00003F#12P#30W……アリオスさん。\x02\x03",

            "#00001Fあの日、兄貴を撃ったのは\x01",
            "イアン先生ですね……？\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60AC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6088")
    OP_FC(0xFFF4)
    Jump("loc_608B")

    label("loc_6088")

    OP_FC(0xC)

    label("loc_608B")


    #C0142
    ChrTalk(
        0x10A,
        "#00605F#13P#30W……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_60FB")

    label("loc_60AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60FB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60D6")
    OP_FC(0xFFF4)
    Jump("loc_60D9")

    label("loc_60D6")

    OP_FC(0xC)

    label("loc_60D9")


    #C0143
    ChrTalk(
        0x109,
        "#10105F#13P#30W……ぁ……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_60FB")


    #C0144
    ChrTalk(
        0x104,
        "#00301F#12P#30Wそいつは……\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "#01403F#5P#40W………………………………\x02\x03",

            "#01400F……何故、そう思う……？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W単なる消去法です……\x02\x03",

            "#00008F……事件の背景を考えると……\x01",
            "先生以外に容疑者がいるとしたら\x01",
            "ディーターさんかマリアベルさん……\x02\x03",

            "#00001Fただ、ディーターさんには\x01",
            "計画の全ては伝えられていないようだし、\x01",
            "マリアベルさんも兄貴とは接点がない……\x02\x03",

            "#00006Fだが……イアン先生は\x01",
            "兄貴ともかなり親しいようでした……\x02\x03",

            "そして……国外の出張も多く、\x01",
            "自衛の必要がある先生ならば\x01",
            "拳銃に慣れていてもおかしくない……\x02\x03",

            "#00013F……どうですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "#01403F#5P#40W……６０点だな……\x02\x03",

            "#01402Fだが……及第点は\x01",
            "付けざるを得ないようだ……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    Sound(128, 2, 30, 0)
    Sleep(150)
    OP_25(0x80, 0x28)
    Sleep(150)
    OP_25(0x80, 0x32)
    Sleep(150)
    OP_25(0x80, 0x3C)
    Sleep(150)
    OP_25(0x80, 0x46)
    Sleep(150)
    OP_25(0x80, 0x50)
    Sleep(150)
    OP_25(0x80, 0x5A)
    Sleep(150)
    OP_25(0x80, 0x64)
    Sleep(300)
    Sound(884, 0, 100, 0)
    Sleep(3000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis308.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis317.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("ガイ")

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40Wはあっ、はあっ……\x02\x03",

            "……なあ、アリオス……\x02\x03",

            "お互い限界みたいだし……\x01",
            "今日のところは休戦にしねぇか？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)
    SetChrName("アリオス")

    #A0149
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40W……何を馬鹿な……\x02\x03",

            "知られた以上、お前をここから\x01",
            "帰すわけにはいかん……\x02\x03",

            "来月の式を無事迎えたくば\x01",
            "殺す気でかかって来るがいい……！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("ガイ")

    #A0150
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40Wんなの出来るワケねえだろ……\x02\x03",

            "そしたらお前やシズクちゃんを\x01",
            "式に呼べねえだろうが……？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 140, -1, -1)
    SetChrName("アリオス")

    #A0151
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "……！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("ガイ")

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40W安心しろ……お前らの計画は\x01",
            "誰にも話しちゃいない……\x02\x03",

            "ダドリーあたりに\x01",
            "協力してもらおうかと思ったが……\x01",
            "アイツも融通効かねぇからな。\x02\x03",

            "セルゲイさんにだって\x01",
            "まだ相談してないんだぜ……？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 140, -1, -1)
    SetChrName("アリオス")

    #A0153
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#40Wお前……\x02\x03",

            "……それを聞いて\x01",
            "俺が好都合と判断するとは\x01",
            "思わないのか……？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("ガイ")

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30Wいや……？\x01",
            "だってお前、不器用だし。\x02\x03",

            "じゃなかったらこんな場所に\x01",
            "ノコノコ一人では来ねぇだろ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 140, -1, -1)
    SetChrName("アリオス")

    #A0155
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30Wくっ……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("ガイ")

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30Wとにかく……このあたりにして\x01",
            "今から呑みにでも行こうぜ？\x02\x03",

            "そうでなくてもここ２年、\x01",
            "ロクに話も出来なかったし……\x02\x03",

            "弟と彼女の自慢話くらい、\x01",
            "させろっつーの。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 150, -1, -1)
    SetChrName("アリオス")

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30Wフッ……相変わらずだな。\x02\x03",

            "弟はたしか……\x01",
            "もう１５になるんだったか？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 160, -1, -1)
    SetChrName("ガイ")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30Wああ、俺に似ずに結構な秀才でな。\x02\x03",

            "どこかの高等学校あたりに\x01",
            "行かせたいと思ってるんだが……\x02\x03",

            "……まあいいや。\x01",
            "雨だし《ガランテ》にでも──\x02",
        )
    )

    CloseMessageWindow()
    Sound(567, 0, 100, 0)
    Sleep(200)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(80, 160, -1, -1)
    SetChrName("ガイ")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#60Wあ───\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 140, -1, -1)
    SetChrName("アリオス")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30W！？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis309.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x2EE, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    SetMessageWindowPos(330, 160, -1, -1)
    SetChrName("アリオス")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30W先生……！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 180, -1, -1)
    SetChrName("ガイ")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#50W……ハハ……\x02\x03",

            "……なるほど……\x01",
            "黒幕はアンタだったか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(885, 0, 80, 0)
    Sound(811, 0, 80, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis310.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis318.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis319.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis320.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x3, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    SetMessageWindowPos(30, 160, -1, -1)
    SetChrName("イアン弁護士")

    #A0163
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30W……悪いな、ガイ君。\x02\x03",

            "ご両親のことを考えたら\x01",
            "君も誘うべきかと思ったが……\x02\x03",

            "多分、君は絶対#4R㈲　㈲#に賛同しないと\x01",
            "確信できてしまったのでね。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 140, -1, -1)
    SetChrName("アリオス")

    #A0164
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30W……先生………\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 200, -1, -1)
    SetChrName("ガイ")

    #A0165
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#50Wハハ……当たりですよ……\x02\x03",

            "……先生が付いてるなら\x01",
            "多分……その計画ってのも\x01",
            "上手く運ぶでしょう……\x02\x03",

            "でも……きっと……\x01",
            "俺の代わりは現れますよ……？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(40, 160, -1, -1)
    SetChrName("イアン弁護士")

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30Wああ……そうだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 140, -1, -1)
    SetChrName("アリオス")

    #A0167
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30Wガイ……！\x01",
            "……しっかりしろ……！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(210, 200, -1, -1)
    SetChrName("ガイ")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#60Wゲホッ……あぁ……\x01",
            "……しまったなァ……\x02\x03",

            "#80Wこんな事になるなら……\x01",
            "ロイドと……セシルに……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(885, 0, 90, 0)
    Sleep(100)
    Sound(811, 0, 90, 0)
    Sound(862, 0, 40, 0)
    StopBGM(0x1770)
    Sleep(2000)
    StopSound(128, 2000, 100)
    WaitBGM()
    SetCameraDistance(16180, 3000)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FC3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F94")
    OP_FC(0xFFF4)
    Jump("loc_6F97")

    label("loc_6F94")

    OP_FC(0xC)

    label("loc_6F97")


    #C0169
    ChrTalk(
        0x10A,
        "#00608F#13P#30W……………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6FC3")


    #C0170
    ChrTalk(
        0x103,
        "#00213F#12P#30W………ガイさん………\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        "#00108F#12P#30W……そんな事が……\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        "#00308F#12P#30W因果な話だぜ……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#00006F#12P#30W……ありがとう。\x01",
            "兄貴の最期を教えてくれて。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x8,
        (
            "#01404F#5P#40W……礼を言うな……\x02\x03",

            "#01400Fイアン先生は……\x01",
            "多分、揺らがないだろう……\x02\x03",

            "そして……\x01",
            "キーアの決意も固いようだ……\x02\x03",

            "#01404F#50W２人を崩せるかどうか……\x01",
            "お前たちの全てをぶつけてみろ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(898, 0, 100, 0)

    def lambda_714F():
        OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_714F)
    WaitChrThread(0x8, 2)
    BeginChrThread(0x8, 0, 0, 33)
    WaitChrThread(0x8, 0)
    Sleep(250)
    PlayBGM("ed7356", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(700)
    Sound(202, 0, 100, 0)
    Sound(181, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 12050, 208000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    Sleep(2000)
    OP_68(0, 13400, 208000, 0)
    MoveCamera(30, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(42000, 0)
    Fade(500)
    SetCameraDistance(44000, 5000)
    OP_0D()
    Sound(223, 0, 50, 0)
    Sound(293, 0, 60, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -8810, 11000, 195890, 250, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -18740, 11000, 207720, 240, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -8810, 11000, 219990, 277, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 2340, 11000, 226130, 26, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 14640, 11000, 216150, 34, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 14650, 11000, 200000, 64, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    OP_75(0x2, 0x1, 0x7D0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -14190, 4900, 215730, 314, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 3670, 8000, 223960, 85, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 16510, 5300, 208790, 89, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -14840, 11000, 200070, 295, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -14870, 11000, 216410, 326, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -2400, 11000, 226170, 334, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 8990, 11000, 220020, 80, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 18340, 11000, 208220, 120, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 8860, 11000, 195800, 110, -40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1580, 4700, 224260, 271, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 16370, 8500, 219180, 44, -33, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 6440, 1300, 196290, 113, -13, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 23440, -900, 210080, 119, -13, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sleep(100)
    Sleep(100)
    Sleep(100)
    Sleep(100)
    Sleep(100)
    Sleep(100)
    FadeToDark(1500, 0, -1)
    OP_24(0x80)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    SetScenarioFlags(0x22, 2)
    NewScene("m9008", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_5B49 end

    def Function_32_76AE(): pass

    label("Function_32_76AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76F6")
    SetChrSubChip(0xFE, 0x8)
    Sleep(150)
    SetChrSubChip(0xFE, 0x9)
    Sleep(150)
    SetChrSubChip(0xFE, 0xA)
    Sleep(150)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0xC)
    Sleep(150)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0xA)
    Sleep(150)
    SetChrSubChip(0xFE, 0x9)
    Sleep(150)
    Jump("Function_32_76AE")

    label("loc_76F6")

    Return()

    # Function_32_76AE end

    def Function_33_76F7(): pass

    label("Function_33_76F7")

    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sound(811, 0, 40, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(300)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    Sound(811, 0, 80, 0)
    SetChrSubChip(0xFE, 0xF)
    Sleep(100)
    Sound(862, 0, 30, 0)
    Sleep(300)
    Return()

    # Function_33_76F7 end

    def Function_34_7761(): pass

    label("Function_34_7761")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    Call(0, 43)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("chr/ch00056.itc", 0x25)
    LoadEffect(0x0, "event/ev17012.eff")
    SetChrPos(0x101, -430, 12000, 207440, 0)
    SetChrPos(0x102, 470, 12000, 206000, 0)
    SetChrPos(0x103, -1370, 12000, 204870, 0)
    SetChrPos(0x104, 1370, 12000, 204570, 0)
    SetChrPos(0xF4, -2540, 12000, 205690, 0)
    SetChrPos(0xF5, 2400, 12000, 205790, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0xF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 12000, 211500, 180)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    SetMapObjFlags(0x2, 0x4)
    OP_68(0, 13050, 222000, 0)
    MoveCamera(16, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31500, 0)
    SetCameraDistance(29500, 2600)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 12000, 222000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(935, 0, 80, 0)
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    Sleep(600)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    OP_68(0, 12800, 208700, 0)
    MoveCamera(46, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18410, 0)
    Fade(500)
    OP_0D()
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 36)
    BeginChrThread(0x102, 0, 0, 37)
    BeginChrThread(0x103, 0, 0, 38)
    BeginChrThread(0x104, 0, 0, 39)
    BeginChrThread(0xF4, 0, 0, 40)
    BeginChrThread(0xF5, 0, 0, 41)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(100)
    OP_68(160, 12800, 209170, 2000)
    MoveCamera(44, 18, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(17490, 2000)
    BeginChrThread(0x101, 0, 0, 35)
    WaitChrThread(0x101, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A62")

    #C0175
    ChrTalk(
        0x102,
        "#00108F#12Pロイド……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B5E")

    label("loc_7A62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A99")

    #C0176
    ChrTalk(
        0x103,
        "#00208F#12P……ロイドさん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B5E")

    label("loc_7A99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AC8")

    #C0177
    ChrTalk(
        0x104,
        "#00308F#12Pロイド……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B5E")

    label("loc_7AC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AFB")

    #C0178
    ChrTalk(
        0x105,
        "#10408F#12P……ロイド……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B5E")

    label("loc_7AFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B2E")

    #C0179
    ChrTalk(
        0x109,
        "#10108F#12Pロイドさん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B5E")

    label("loc_7B2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B5E")

    #C0180
    ChrTalk(
        0x106,
        "#10708F#12P……ロイドさん。\x02",
    )

    CloseMessageWindow()

    label("loc_7B5E")


    #C0181
    ChrTalk(
        0x101,
        (
            "#00004F#11P#30Wはは……\x02\x03",

            "#00008F……これでやっと……\x01",
            "兄貴に届けた気がする。\x02\x03",

            "#00002Fありがとう……\x01",
            "みんなのおかげだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x104,
        (
            "#00304F#12Pはは……\x01",
            "何言ってんだっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#00204F#12P……ロイドさんの意志が\x01",
            "アリオスさんという《壁》を\x01",
            "突き崩したんだと思います。\x02\x03",

            "#00208Fそしてガイさんの死という\x01",
            "過去の暗闇に光を当てた……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        (
            "#00104F#12Pええ……私たちは\x01",
            "その手伝いをしただけだわ。\x02\x03",

            "#00108F次ばかりは手伝いなんて\x01",
            "言っていられないけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D50")

    #C0185
    ChrTalk(
        0x106,
        "#10703F#12P……そうですね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7DB7")

    label("loc_7D50")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D88")

    #C0186
    ChrTalk(
        0x109,
        "#10106F#12P……そうですね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7DB7")

    label("loc_7D88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DB7")

    #C0187
    ChrTalk(
        0x105,
        "#10406F#12P……そうだね。\x02",
    )

    CloseMessageWindow()

    label("loc_7DB7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E0B")

    #C0188
    ChrTalk(
        0x104,
        (
            "#00308F#12Pベルお嬢さんにイアン先生、\x01",
            "それにキー坊か……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_7EB8")

    label("loc_7E0B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E5E")

    #C0189
    ChrTalk(
        0x105,
        (
            "#10408F#12Pマリアベル嬢に熊ヒゲ先生、\x01",
            "それにキーアか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EB8")

    label("loc_7E5E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EB8")

    #C0190
    ChrTalk(
        0x109,
        (
            "#10108F#12Pマリアベルさんにイアン先生、\x01",
            "それにキーアちゃんですか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EB8")


    #C0191
    ChrTalk(
        0x101,
        "#00006F#11P#30W……ああ……\x02",
    )

    CloseMessageWindow()
    OP_68(350, 12800, 208640, 1000)
    MoveCamera(37, 17, 0, 1000)

    def lambda_7EFA():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7EFA)
    Sleep(300)

    def lambda_7F0A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_7F0A)
    OP_6F(0x79)

    #C0192
    ChrTalk(
        0x101,
        (
            "#00003F#5P最後の《領域》も解放した。\x02\x03",

            "#00000Fとりあえず……\x01",
            "《神域》の終点に戻ろう。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17740, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    SetChrPos(0x0, 0, 12000, 202500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_37()
    SetScenarioFlags(0x1A9, 4)
    OP_29(0xB2, 0x1, 0x8)
    ModifyEventFlags(0, 0, 0x80)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x22, 2)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_34_7761 end

    def Function_35_7FDC(): pass

    label("Function_35_7FDC")

    OP_9B(0x0, 0xFE, 0x162, 0x320, 0x3E8, 0x0)
    Return()

    # Function_35_7FDC end

    def Function_36_7FEC(): pass

    label("Function_36_7FEC")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_7FEC end

    def Function_37_7FFB(): pass

    label("Function_37_7FFB")

    Sleep(200)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_7FFB end

    def Function_38_800D(): pass

    label("Function_38_800D")

    Sleep(300)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_800D end

    def Function_39_801F(): pass

    label("Function_39_801F")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_39_801F end

    def Function_40_802B(): pass

    label("Function_40_802B")

    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_804B")
    Sound(540, 0, 50, 0)
    Jump("loc_8070")

    label("loc_804B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8070")
    Sound(531, 0, 100, 0)

    label("loc_8070")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_40_802B end

    def Function_41_8079(): pass

    label("Function_41_8079")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8099")
    Sound(540, 0, 50, 0)
    Jump("loc_80BE")

    label("loc_8099")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80BE")
    Sound(531, 0, 100, 0)

    label("loc_80BE")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_8079 end

    def Function_42_80C7(): pass

    label("Function_42_80C7")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_42_80C7 end

    def Function_43_80EE(): pass

    label("Function_43_80EE")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_8110")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_8128")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_8140")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8163")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8186")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81A9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_81A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81C7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_81C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81E5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_81E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8203")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8203")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_822C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_822C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8255")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8279")

    label("loc_8255")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DC(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8279")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8279")

    Return()

    # Function_43_80EE end

    SaveToFile()

Try(main)
