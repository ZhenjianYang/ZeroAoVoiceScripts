from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9072.bin",                # FileName
        "m9072",                    # MapName
        "m9072",                    # Location
        0x00C2,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 1500, 0, 0, 1, 194, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9072",                  # 0
        "戦鬼シグムント",         # 1
        "台詞表示用ダミーキャラ", # 2
        "シグムントお供",         # 3
        "シグムントお供",         # 4
        "SE制御",                 # 5
        "bm9059",                 # 6
    ))

    ATBonus("ATBonus_1D8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_298", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 3, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 13, 9, 180)
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
        "BattleInfo_2B8", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm9059", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03301.dat", "ms81200.dat", "ms81200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_298", "MonsterBattlePostion_278", "ed7458", "ed7453", "ATBonus_1D8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51742.itc",                   # 00
    ))

    DeclNpc(0,       4000,    63500,   180,  389,  0x0, 0,   0,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 10,  0.0,                   35.0,                  3.0,                   625.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -7.0,                  -0.6000000238418579,   1.0])

    DeclActor(3750,    0,       10000,   1200,    3750,    1000,    10000,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(932, 0)                                        # 0

    ScpFunction((
        "Function_0_3A4",          # 00, 0
        "Function_1_3E2",          # 01, 1
        "Function_2_5BE",          # 02, 2
        "Function_3_830",          # 03, 3
        "Function_4_92C",          # 04, 4
        "Function_5_BB4",          # 05, 5
        "Function_6_D0D",          # 06, 6
        "Function_7_D6E",          # 07, 7
        "Function_8_DCF",          # 08, 8
        "Function_9_E30",          # 09, 9
        "Function_10_E91",         # 0A, 10
        "Function_11_2E4E",        # 0B, 11
        "Function_12_2E79",        # 0C, 12
        "Function_13_2EA4",        # 0D, 13
        "Function_14_2ECF",        # 0E, 14
        "Function_15_2EFA",        # 0F, 15
        "Function_16_2F25",        # 10, 16
        "Function_17_2F50",        # 11, 17
        "Function_18_2F6D",        # 12, 18
        "Function_19_2F9C",        # 13, 19
        "Function_20_2FBF",        # 14, 20
        "Function_21_2FD1",        # 15, 21
        "Function_22_2FE3",        # 16, 22
        "Function_23_2FEF",        # 17, 23
        "Function_24_303D",        # 18, 24
        "Function_25_308B",        # 19, 25
        "Function_26_30D4",        # 1A, 26
        "Function_27_311D",        # 1B, 27
        "Function_28_3174",        # 1C, 28
        "Function_29_318E",        # 1D, 29
        "Function_30_31BD",        # 1E, 30
        "Function_31_37B8",        # 1F, 31
        "Function_32_37FB",        # 20, 32
        "Function_33_410A",        # 21, 33
        "Function_34_415F",        # 22, 34
        "Function_35_4185",        # 23, 35
        "Function_36_4194",        # 24, 36
        "Function_37_41A3",        # 25, 37
        "Function_38_41AF",        # 26, 38
        "Function_39_41C1",        # 27, 39
        "Function_40_41FB",        # 28, 40
        "Function_41_422F",        # 29, 41
    ))


    def Function_0_3A4(): pass

    label("Function_0_3A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B5")
    Event(0, 4)

    label("loc_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3CF")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 30)
    Jump("loc_3E1")

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3E1")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 2)
    Event(0, 32)

    label("loc_3E1")

    Return()

    # Function_0_3A4 end

    def Function_1_3E2(): pass

    label("Function_1_3E2")

    OP_F0(0x1, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3FB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_3FB")

    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x1, 0x0, 0x5)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_439")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_END)), "loc_4D9")
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point16_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "yuka_15_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x0, 0x1)
    Jump("loc_56B")

    label("loc_4D9")

    SetMapObjFrame(0xFF, "magi10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point16_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "yuka_15_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x1, 0x1)

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57C")
    Call(0, 41)

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_597")
    OP_24(0x82)
    Sound(825, 1, 40, 0)
    Jump("loc_5BD")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5B1")
    OP_24(0x82)
    Sound(825, 1, 60, 0)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_5BD")

    label("loc_5B1")

    Sound(130, 1, 60, 0)
    Sound(825, 1, 60, 0)

    label("loc_5BD")

    Return()

    # Function_1_3E2 end

    def Function_2_5BE(): pass

    label("Function_2_5BE")

    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DF")

    #C0001
    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        (
            "#00301F完全に落ちているみてえだが……\x02\x03",

            "#00306Fどうやら致命傷は負ってねえみてえだ。\x01",
            "……やれやれ、タフすぎだっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        "#00104F……メルカバに運んだ方がいいかしら？\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00001Fそうだな……\x01",
            "クロスベル市襲撃事件の実行犯だし、\x01",
            "逮捕できるならそうしたいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x103,
        (
            "#00203F……さすがに危険かと。\x02\x03",

            "#00200F命に別状もないなら、この場所に\x01",
            "放置したほうが賢明だとおもいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#00303Fま、しばらくは目も覚まさないだろうし\x01",
            "追撃してくる心配もねえだろう。\x02\x03",

            "#00300F今は先に進むとしようぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CE, 7)
    Jump("loc_82C")

    label("loc_7DF")


    #C0007
    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0008
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

    label("loc_82C")

    TalkEnd(0x8)
    Return()

    # Function_2_5BE end

    def Function_3_830(): pass

    label("Function_3_830")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0009
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91D")
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

    label("loc_91D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_830 end

    def Function_4_92C(): pass

    label("Function_4_92C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event/ev202_00.eff")
    OP_69(0x1, 0x0)
    OP_68(-830, 5000, 70360, 0)
    MoveCamera(47, 43, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14220, 0)
    SetChrPos(0x0, 0, 4000, 72000, 180)
    SetChrPos(0x1, 0, 4000, 72000, 180)
    SetChrPos(0x2, 0, 4000, 72000, 180)
    SetChrPos(0x3, 0, 4000, 72000, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A40():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A40)

    def lambda_A51():
        OP_95(0xFE, -230, 4000, 68330, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A51)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AA8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_AA8)

    def lambda_AB9():
        OP_95(0xFE, -1240, 4000, 68690, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AB9)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_B16)

    def lambda_B27():
        OP_95(0xFE, 1150, 4000, 68650, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B27)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B7E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_B7E)

    def lambda_B8F():
        OP_95(0xFE, -2400, 4000, 69350, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B8F)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_92C end

    def Function_5_BB4(): pass

    label("Function_5_BB4")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event/evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_C0D)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_C58)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_CA3)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_CEE)
    StopSound(825, 1000, 40)
    Sleep(1000)
    NewScene("m9005", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_5_BB4 end

    def Function_6_D0D(): pass

    label("Function_6_D0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D25")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_D25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D3D")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_D3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D55")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_D55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D6D")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_D6D")

    Return()

    # Function_6_D0D end

    def Function_7_D6E(): pass

    label("Function_7_D6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D86")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_D86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D9E")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_D9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB6")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_DB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DCE")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_DCE")

    Return()

    # Function_7_D6E end

    def Function_8_DCF(): pass

    label("Function_8_DCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE7")
    LoadChrToIndex("chr/ch03056.itc", 0x29)

    label("loc_DE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFF")
    LoadChrToIndex("chr/ch03253.itc", 0x29)

    label("loc_DFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E17")
    LoadChrToIndex("chr/ch0295F.itc", 0x29)

    label("loc_E17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2F")
    LoadChrToIndex("chr/ch00953.itc", 0x29)

    label("loc_E2F")

    Return()

    # Function_8_DCF end

    def Function_9_E30(): pass

    label("Function_9_E30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E48")
    LoadChrToIndex("chr/ch03056.itc", 0x2A)

    label("loc_E48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E60")
    LoadChrToIndex("chr/ch03253.itc", 0x2A)

    label("loc_E60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E78")
    LoadChrToIndex("chr/ch0295F.itc", 0x2A)

    label("loc_E78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E90")
    LoadChrToIndex("chr/ch00953.itc", 0x2A)

    label("loc_E90")

    Return()

    # Function_9_E30 end

    def Function_10_E91(): pass

    label("Function_10_E91")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04500.itp")
    CreatePortrait(1, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu04501.itp")
    LoadChrToIndex("chr/ch03300.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("chr/ch03350.itc", 0x25)
    LoadChrToIndex("chr/ch03354.itc", 0x26)
    LoadChrToIndex("monster/ch81250.itc", 0x27)
    LoadChrToIndex("apl/ch51778.itc", 0x28)
    LoadEffect(0x0, "event/ev602_01.eff")
    LoadEffect(0x1, "event/ev17001.eff")
    LoadEffect(0x2, "event/ev305_00.eff")
    SoundLoad(825)
    SoundLoad(832)
    SoundLoad(2771)
    SoundLoad(2772)
    SoundLoad(2773)
    SoundLoad(3847)
    SoundLoad(3850)
    SoundLoad(3851)
    SoundLoad(3852)
    SoundLoad(3848)
    SoundLoad(3849)
    SetChrPos(0x101, 1100, 5000, 38100, 0)
    SetChrPos(0x102, -1100, 5000, 37750, 0)
    SetChrPos(0x103, 200, 5000, 37000, 0)
    SetChrPos(0x104, 0, 5000, 38800, 0)
    SetChrPos(0xF4, -650, 5000, 36250, 0)
    SetChrPos(0xF5, 850, 5000, 36000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 4000, 62000, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 5000, 4000, 56500, 0)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, -3500, 4400, 63500, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 3500, 4400, 63500, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    BeginChrThread(0xA, 2, 0, 27)
    BeginChrThread(0xB, 2, 0, 27)
    OP_68(0, 3000, 42800, 0)
    MoveCamera(55, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 5000, 44800, 2500)
    MoveCamera(63, 29, 0, 2500)
    OP_6E(600, 2500)
    SetCameraDistance(15680, 2500)
    FadeToBright(1000, 0)

    def lambda_118E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_118E)
    Sleep(50)

    def lambda_11A6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11A6)
    Sleep(50)

    def lambda_11BE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11BE)
    Sleep(50)

    def lambda_11D6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11D6)
    Sleep(50)

    def lambda_11EE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_11EE)
    Sleep(50)

    def lambda_1206():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1206)
    OP_0D()
    Sleep(1600)
    StopBGM(0x7D0)
    OP_C9(0x0, 0x80000000)

    #N0010
    NpcTalk(
        0x9,
        "豪胆な声",
        (
            "#3847V#11P#N#38A#30Wクク──\x01",
            "前哨戦を潜り抜けたか。\x02",
        )
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
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    OP_68(-140, 5300, 57850, 4000)
    MoveCamera(43, 12, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(16860, 4000)
    BeginChrThread(0x104, 0, 0, 11)
    Sleep(50)
    BeginChrThread(0x101, 0, 0, 12)
    Sleep(50)
    BeginChrThread(0x103, 0, 0, 13)
    Sleep(50)
    BeginChrThread(0x102, 0, 0, 14)
    Sleep(50)
    BeginChrThread(0xF4, 0, 0, 15)
    Sleep(50)
    BeginChrThread(0xF5, 0, 0, 16)
    OP_6F(0x79)
    BeginChrThread(0xC, 1, 0, 29)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    #C0011
    ChrTalk(
        0x104,
        "#00311F#12P叔父貴……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#00013F#12Pシグムント・オルランド……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_143C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1408")
    OP_FC(0xFFF4)
    Jump("loc_140B")

    label("loc_1408")

    OP_FC(0xC)

    label("loc_140B")


    #C0013
    ChrTalk(
        0x10A,
        "#00601F#13P《赤い星座》の副団長か……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_14C1")

    label("loc_143C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1498")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1466")
    OP_FC(0xFFF4)
    Jump("loc_1469")

    label("loc_1466")

    OP_FC(0xC)

    label("loc_1469")


    #C0014
    ChrTalk(
        0x109,
        "#10101F#13P《赤い星座》の副団長……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_14C1")

    label("loc_1498")


    #C0015
    ChrTalk(
        0x102,
        "#00101F#12P《赤い星座》の副団長……\x02",
    )

    CloseMessageWindow()

    label("loc_14C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_152E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14EB")
    OP_FC(0xFFF4)
    Jump("loc_14EE")

    label("loc_14EB")

    OP_FC(0xC)

    label("loc_14EE")


    #C0016
    ChrTalk(
        0x106,
        (
            "#10708F#13P《赤の戦鬼》……\x01",
            "最強の猟兵の一人ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_15D3")

    label("loc_152E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1599")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1558")
    OP_FC(0xFFF4)
    Jump("loc_155B")

    label("loc_1558")

    OP_FC(0xC)

    label("loc_155B")


    #C0017
    ChrTalk(
        0x105,
        (
            "#10408F#13P《赤の戦鬼》……\x01",
            "最強の猟兵の一人だね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_15D3")

    label("loc_1599")


    #C0018
    ChrTalk(
        0x103,
        (
            "#00208F#12P《赤の戦鬼》……\x01",
            "最強の猟兵の一人ですか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D3")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0019
    AnonymousTalk(
        0x8,
        (
            "クク……その通りだ。\x02\x03",

            "俺と張ると言ったら《闘神》と\x01",
            "《猟兵王》くらいだったが……\x02\x03",

            "その２人が相討ちになった後では、\x01",
            "俺が最強と言えるかもしれん。\x02\x03",

            "──あくまで“現時点”ではな。\x02",
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

    #C0020
    ChrTalk(
        0x104,
        "#00305F#12P……！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#04503F#5Pランドルフ……\x01",
            "最早お前も気付いている筈だ。\x02\x03",

            "このクロスベルの状況と\x01",
            "エレボニア帝国の乱れによって\x01",
            "大陸は激動の時代を迎えた。\x02\x03",

            "#04501F今まで以上に、俺たち猟兵の\x01",
            "活躍の場は増えていくだろう。\x02\x03",

            "テロリストどもは気勢を上げ、\x01",
            "《蛇》と《教会》の暗闘は広がり、\x01",
            "遊撃士どもは躍起となるだろう。\x02\x03",

            "#04504F貴様も肌で感じているはずだ。\x02\x03",

            "#04502F──まさに終わるべくして\x01",
            "平和な時代が終わったのだと。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        "#00311F#12P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00010F#12P……勝手なことを……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#00108F#12Pでも……\x01",
            "あながち間違ってはいないわ。\x02\x03",

            "#00106Fクロスベルの事件……\x01",
            "そして帝国の内戦と共和国の混乱で\x01",
            "大陸は今、大きく揺らいでいる……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#00201F#12Pもしかして……\x01",
            "クロスベルの事件が起きなくても\x01",
            "不可避だった……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A8F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19FE")
    OP_FC(0xFFF4)
    Jump("loc_1A01")

    label("loc_19FE")

    OP_FC(0xC)

    label("loc_1A01")


    #C0026
    ChrTalk(
        0x106,
        (
            "#10703F#13P……大陸の至る所で導火線が\x01",
            "くすぶっていたのは確かです。\x02\x03",

            "#10701Fクロスベルの事件はあくまで\x01",
            "きっかけでしかないでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1BFA")

    label("loc_1A8F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B46")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AB9")
    OP_FC(0xFFF4)
    Jump("loc_1ABC")

    label("loc_1AB9")

    OP_FC(0xC)

    label("loc_1ABC")


    #C0027
    ChrTalk(
        0x10A,
        (
            "#00606F#13P……大陸の至る所で導火線が\x01",
            "くすぶっていたのは確かだ。\x02\x03",

            "#00601Fクロスベルの事件はあくまで\x01",
            "きっかけとなったにすぎん。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1BFA")

    label("loc_1B46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BFA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B70")
    OP_FC(0xFFF4)
    Jump("loc_1B73")

    label("loc_1B70")

    OP_FC(0xC)

    label("loc_1B73")


    #C0028
    ChrTalk(
        0x105,
        (
            "#10406F#13P……大陸の至る所で導火線が\x01",
            "くすぶっていたのは確かさ。\x02\x03",

            "#10401Fクロスベルの事件はあくまで\x01",
            "きっかけとなったにすぎない。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1BFA")


    #C0029
    ChrTalk(
        0x104,
        (
            "#00306Fああ#12P……そうだろうな。\x02\x03",

            "#00311Fそして確かに……\x01",
            "俺はそれを肌で感じていた。\x02\x03",

            "嵐の予感を……\x01",
            "戦場の匂いが立ち込めるのを。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#00008F#12P……ランディ……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#04502F#5Pクク、それこそ貴様が\x01",
            "骨の髄まで猟兵である証拠……\x02\x03",

            "そしてオルランドの一族に流れる、\x01",
            "戦士としての血の“業#2Rカルマ#”だ。\x02\x03",

            "#04503Fなのにランドルフ……\x01",
            "なぜ貴様は未だ目を覚まさない？\x02\x03",

            "#04501Fどうして自分を偽りながら\x01",
            "安穏な生を送っていられるのだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        "#00311F#12P#30W……………………………………\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#04501F#5P──これが最後だ。\x01",
            "ランドルフ、《闘神》を継げ。\x02\x03",

            "足りない部分は兄貴の代わりに\x01",
            "俺が仕込んでやる。\x02\x03",

            "#04504Fそして名実共に《赤い星座》の\x01",
            "団長となった暁には……\x02\x03",

            "#04502Fどこに肩入れするも望むままだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0034
    ChrTalk(
        0x104,
        "#00305F#12P……！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#04504F#5Pクク、無論このクロスベルに\x01",
            "肩入れしてやるのもいいだろう。\x02\x03",

            "#04502Fこの件がどう転んだとしても、\x01",
            "間違いなく相当な苦難が\x01",
            "待ち受けているだろうからな。\x02\x03",

            "“お仲間”のためにも\x01",
            "なるかもしれんぞ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#00010F#12P……くっ……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#00107F#12P貴方は……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        "#00211F#12P……足元見すぎです……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 17)
    WaitChrThread(0x104, 3)
    Sleep(200)

    def lambda_201C():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_201C)
    WaitChrThread(0x104, 2)
    Sleep(300)

    #C0039
    ChrTalk(
        0x104,
        (
            "#00304F#12P#30Wクク、なるほどな……\x02\x03",

            "#00312F冷徹かつ合理的に、\x01",
            "猛き衝動を飼い慣らす……\x02\x03",

            "さすがは《赤の戦鬼#8Rオーガ・ロッソ#》だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#04504F#5Pそれが猟兵の猟兵たる由縁……\x01",
            "貴様も分かっているのだろう。\x02\x03",

            "#04502F平和な時代が去った以上、\x01",
            "貴様が抗#2Rあらが#う“足場”は\x01",
            "どこにも無いはずだ。\x02\x03",

            "ならば迷う余地はあるまい？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        "#00303F#12Pそうかもしれねぇな……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 18)
    WaitChrThread(0x104, 3)
    Sleep(350)

    #C0042
    ChrTalk(
        0x104,
        "#00301F#12P──だが、答えはＮＯだ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x8,
        "#04505F#5P………ほう………？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#00315F#12Pどうやらアンタの不出来な甥は\x01",
            "道を外れちまったらしいぜ……？\x02\x03",

            "#00304F激動の時代に平和を求め、\x01",
            "欺瞞#4R ぎ まん#の世に正義を求める……\x02\x03",

            "しかもロマンや幻想もなく、\x01",
            "自分たちが出来ることを\x01",
            "地道に積み重ねる事によって……\x02\x03",

            "#00302F──そんな“足場”を\x01",
            "見出しちまってるんだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#00214F#12Pランディさん……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_241A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23FD")
    OP_FC(0xFFF4)
    Jump("loc_2400")

    label("loc_23FD")

    OP_FC(0xC)

    label("loc_2400")


    #C0046
    ChrTalk(
        0x109,
        "#10100F#13P先輩……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_241A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_246B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2444")
    OP_FC(0xFFF4)
    Jump("loc_2447")

    label("loc_2444")

    OP_FC(0xC)

    label("loc_2447")


    #C0047
    ChrTalk(
        0x10A,
        "#00604F#13Pフッ、生意気な……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_246B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24D3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2495")
    OP_FC(0xFFF4)
    Jump("loc_2498")

    label("loc_2495")

    OP_FC(0xC)

    label("loc_2498")


    #C0048
    ChrTalk(
        0x105,
        (
            "#10402F#13Pフフ、誰かさんから\x01",
            "クサさが移ったのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_24D3")


    #C0049
    ChrTalk(
        0x8,
        "#04501F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        (
            "#00303F#12Pこの“足場”をもって\x01",
            "俺は俺の“業”に抗わせてもらう。\x02\x03",

            "#00308Fあの懐かしい戦場の日々……\x01",
            "修羅として生きるしかなかった\x01",
            "俺自身と完全に決別する。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 19)
    WaitChrThread(0x104, 3)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0051
    ChrTalk(
        0x104,
        "#00301F#12P#30Wこれが──俺なりのけじめだ。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#00002F#12Pランディ……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        "#00104F#12P……私たちも見届けるわ。\x02",
    )

    CloseMessageWindow()
    StopSound(130, 3000, 30)
    StopSound(825, 3000, 60)
    Sleep(300)

    def lambda_2643():
        OP_A6(0xFE, 0x1E, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2643)
    WaitChrThread(0x8, 2)
    Sleep(800)

    def lambda_2663():
        OP_A6(0xFE, 0x28, 0x28, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2663)
    WaitChrThread(0x8, 2)
    Sleep(1000)

    #C0054
    ChrTalk(
        0x8,
        (
            "#04502F#5P#30W……クク………\x02\x03",

            "#04504F…………ハハハハ…………\x02\x03",

            "#04501F──御託はそれだけか？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    BeginChrThread(0x8, 0, 0, 28)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(1000)
    PlayEffect(0x1, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x258, 0x1770, 0x1F4)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(256, 0, 80, 0)
    Sound(881, 0, 70, 0)
    OP_24(0x339)
    Sleep(1)
    Sound(825, 2, 80, 0)
    Sound(832, 2, 100, 0)
    Sleep(800)
    SetCameraDistance(17860, 20000)

    #C0055
    ChrTalk(
        0x101,
        "#00010F#12Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        "#00210F#12P#N……うぁっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_280F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27E5")
    OP_FC(0xFFF4)
    Jump("loc_27E8")

    label("loc_27E5")

    OP_FC(0xC)

    label("loc_27E8")


    #C0057
    ChrTalk(
        0x106,
        "#10707F#13Pなんて闘気……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_28B4")

    label("loc_280F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2865")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2839")
    OP_FC(0xFFF4)
    Jump("loc_283C")

    label("loc_2839")

    OP_FC(0xC)

    label("loc_283C")


    #C0058
    ChrTalk(
        0x105,
        "#10410F#13Pなんて闘気だ……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_28B4")

    label("loc_2865")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_288F")
    OP_FC(0xFFF4)
    Jump("loc_2892")

    label("loc_288F")

    OP_FC(0xC)

    label("loc_2892")


    #C0059
    ChrTalk(
        0x10A,
        "#00610F#13Pこの闘気は……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_28B4")


    #C0060
    ChrTalk(
        0x8,
        (
            "#04504F#5Pフフ……いいだろう。\x02\x03",

            "その頼りなき“足場”をもって\x01",
            "貴様の抗#2Rあらが#いを認めよう……\x02\x03",

            "#04501Fだが……分かっているな？\x02\x03",

            "そこまで言い切ったからには\x01",
            "もはや手加減はできぬと……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_C9(0x0, 0x80000000)

    #C0061
    ChrTalk(
        0x104,
        "#00303F#2771V#12P#30W#20Aああ──望むところだ。\x02",
    )
    #Auto

    CloseMessageWindow()
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(1000)
    PlayEffect(0x2, 0x0, 0x104, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    Sound(256, 0, 80, 0)
    Sound(881, 0, 70, 0)
    WaitChrThread(0x104, 0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7458", 0)
    MoveCamera(48, 14, 0, 20000)
    Sleep(800)

    #C0062
    ChrTalk(
        0x104,
        (
            "#00301F#2772V#12P#30W#46A親父とアンタから学んだ戦技と\x01",
            "持てる力の全てを掛けて……\x02\x03",

            "#00307F#2773V#40A最強の猟兵であるアンタを\x01",
            "ブチのめさせてもらう！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #C0063
    ChrTalk(
        0x8,
        (
            "#04504F#3850V#5P#30W#27Aクク……面白い。\x02\x03",

            "#04512F#3851V#30W#50Aならば俺は、貴様を喰らって\x01",
            "《闘神》を継ぐことにしよう！\x02\x03",

            "#3852V#30W#50A不出来な息子を持った兄貴への\x01",
            "せめてもの手向けとしてな！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(-140, 5300, 57850, 0)
    MoveCamera(359, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17860, 0)
    SetCameraDistance(14860, 20000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    Sound(802, 0, 100, 0)
    Sound(531, 0, 50, 0)
    Sound(358, 0, 80, 0)
    Sleep(300)
    Sound(817, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 25)
    BeginChrThread(0xB, 3, 0, 26)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    Sleep(100)
    BeginChrThread(0x101, 0, 0, 20)
    BeginChrThread(0x102, 0, 0, 21)
    BeginChrThread(0x103, 0, 0, 22)
    BeginChrThread(0xF4, 0, 0, 23)
    BeginChrThread(0xF5, 0, 0, 24)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_A0(0x8, 1800, 0x0, 0x4)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0064
    AnonymousTalk(
        0x8,
        (
            "#3848V#5P#40W#30Aさあ、受けてみろ……\x02\x03",

            "#3849V#30W#67A戦場を喰らい、蹂躙し尽くす、\x01",
            "《赤の戦鬼#8Rオーガ・ロッソ#》の双戦斧を！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Sleep(300)

    #C0065
    ChrTalk(
        0x102,
        "#00107F#6P#N#10A……来るわ……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00007F#12P#37A迎撃開始……！\x01",
            "全力でランディを援護する！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Battle("BattleInfo_2B8", 0x0, 0x0, 0x100, 0x47, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    EndChrThread(0x8, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 30)
    Return()

    # Function_10_E91 end

    def Function_11_2E4E(): pass

    label("Function_11_2E4E")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0xFA0, 0xD69C, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_2E4E end

    def Function_12_2E79(): pass

    label("Function_12_2E79")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0xFA0, 0xD1C4, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_2E79 end

    def Function_13_2EA4(): pass

    label("Function_13_2EA4")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0xFA0, 0xCC92, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_2EA4 end

    def Function_14_2ECF(): pass

    label("Function_14_2ECF")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0xFA0, 0xCF4E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_2ECF end

    def Function_15_2EFA(): pass

    label("Function_15_2EFA")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0xFA0, 0xD1BA, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_15_2EFA end

    def Function_16_2F25(): pass

    label("Function_16_2F25")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0xFA0, 0xD0F2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_2F25 end

    def Function_17_2F50(): pass

    label("Function_17_2F50")

    SetChrChipByIndex(0x104, 0x28)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x1000)
    SetChrSubChip(0xFE, 0x1)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(429)
    Return()

    # Function_17_2F50 end

    def Function_18_2F6D(): pass

    label("Function_18_2F6D")

    SetChrChipByIndex(0x104, 0x28)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(110)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)
    SetChrChipByIndex(0x104, 0xFF)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_2F6D end

    def Function_19_2F9C(): pass

    label("Function_19_2F9C")

    SetChrChipByIndex(0x104, 0x28)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x1000)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(429)
    Return()

    # Function_19_2F9C end

    def Function_20_2FBF(): pass

    label("Function_20_2FBF")

    Sleep(150)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_2FBF end

    def Function_21_2FD1(): pass

    label("Function_21_2FD1")

    Sleep(300)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_2FD1 end

    def Function_22_2FE3(): pass

    label("Function_22_2FE3")

    Sleep(450)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_2FE3 end

    def Function_23_2FEF(): pass

    label("Function_23_2FEF")

    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_300F")
    Sound(540, 0, 50, 0)
    Jump("loc_3034")

    label("loc_300F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3034")
    Sound(531, 0, 100, 0)

    label("loc_3034")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_2FEF end

    def Function_24_303D(): pass

    label("Function_24_303D")

    Sleep(750)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_305D")
    Sound(540, 0, 50, 0)
    Jump("loc_3082")

    label("loc_305D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3082")
    Sound(531, 0, 100, 0)

    label("loc_3082")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_303D end

    def Function_25_308B(): pass

    label("Function_25_308B")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_25_308B end

    def Function_26_30D4(): pass

    label("Function_26_30D4")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_26_30D4 end

    def Function_27_311D(): pass

    label("Function_27_311D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3173")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
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
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Jump("Function_27_311D")

    label("loc_3173")

    Return()

    # Function_27_311D end

    def Function_28_3174(): pass

    label("Function_28_3174")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_318D")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_28_3174")

    label("loc_318D")

    Return()

    # Function_28_3174 end

    def Function_29_318E(): pass

    label("Function_29_318E")

    OP_25(0x82, 0x3C)
    Sleep(200)
    OP_25(0x82, 0x37)
    Sleep(200)
    OP_25(0x82, 0x32)
    Sleep(200)
    OP_25(0x82, 0x2D)
    Sleep(200)
    OP_25(0x82, 0x28)
    Sleep(200)
    OP_25(0x82, 0x23)
    Sleep(200)
    OP_25(0x82, 0x1E)
    Return()

    # Function_29_318E end

    def Function_30_31BD(): pass

    label("Function_30_31BD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51742.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadEffect(0x0, "event/ev17083.eff")
    SetChrPos(0x101, 1120, 4000, 58200, 0)
    SetChrPos(0x102, -1270, 4000, 57570, 0)
    SetChrPos(0x103, 420, 4000, 56870, 0)
    SetChrPos(0x104, 0, 4000, 59440, 0)
    SetChrPos(0xF4, -2540, 4000, 58190, 0)
    SetChrPos(0xF5, 2540, 4000, 57990, 0)
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
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 4000, 63500, 180)
    OP_68(0, 4800, 62000, 0)
    MoveCamera(180, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16300, 0)
    SetCameraDistance(14300, 2500)
    PlayBGM("ed7543", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)
    OP_6F(0x79)

    #C0067
    ChrTalk(
        0x8,
        (
            "#04510F#6P#40W………クク…………\x02\x03",

            "#04511Fまさかあんな“足場”で……\x01",
            "……そこまで踏ん張るとは……\x02\x03",

            "だが……\x01",
            "それもまた今の貴様の力か……\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x8, 0x1)
    OP_68(-150, 5400, 60750, 0)
    MoveCamera(39, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14680, 0)
    OP_0D()
    Sleep(300)

    #C0068
    ChrTalk(
        0x104,
        (
            "#00306F#12P#30W……ああ……\x01",
            "悪いが貫き通させてもらう……\x02\x03",

            "#00301Fアンタと親父には……\x01",
            "……不義理をしちまうけどな……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "#04510F#5P#40Wクク……今さらなんだ……？\x02\x03",

            "#04511F……それに一番の不義理は\x01",
            "けじめも取らずにのうのうと\x01",
            "流れていたことだろう……\x02\x03",

            "一言も言わなかったが……\x01",
            "……兄貴も心配していたぞ……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        "#00308F#12P#30W……そうか……親父が……\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_3568():
        OP_A6(0xFE, 0x0, 0x23, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3568)
    Sleep(800)

    #C0071
    ChrTalk(
        0x8,
        (
            "#04510F#5P#50Wクク……だが……\x01",
            "少しは兄貴に顔向けできる\x01",
            "顔になったようだ……\x02\x03",

            "#60W……その強がりが\x01",
            "どこまで……貫き通せるか……\x02\x03",

            "これからの生き様で……\x01",
            "……証明……してみせろ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_363F():
        OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_363F)
    WaitChrThread(0x8, 2)
    Fade(500)
    BeginChrThread(0x8, 0, 0, 31)
    Sleep(300)
    OP_68(-40, 5400, 62080, 1000)
    WaitChrThread(0x8, 0)
    Sleep(200)
    Sound(202, 0, 100, 0)
    Sound(181, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 4050, 60140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    Sleep(2300)
    Sleep(500)
    MoveCamera(38, 20, 0, 4500)
    SetCameraDistance(20600, 4500)
    Sleep(3000)
    StopSound(825, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, -900, 58000, 0)
    MoveCamera(24, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(46500, 0)
    SetCameraDistance(50000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(202, 0, 70, 0)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "yuka_15_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x0, 0x1)
    Fade(500)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m9005", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_31BD end

    def Function_31_37B8(): pass

    label("Function_31_37B8")

    SetChrSubChip(0xFE, 0x2)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(429)
    SetChrSubChip(0xFE, 0x6)
    Sound(811, 0, 100, 0)
    Sound(898, 0, 100, 0)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sound(862, 0, 50, 0)
    Sound(833, 0, 50, 0)
    Sleep(429)
    Return()

    # Function_31_37B8 end

    def Function_32_37FB(): pass

    label("Function_32_37FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51742.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 6)
    Call(0, 7)
    LoadChrToIndex("chr/ch00056.itc", 0x25)
    LoadChrToIndex("chr/ch00156.itc", 0x26)
    LoadChrToIndex("chr/ch00256.itc", 0x27)
    LoadChrToIndex("chr/ch00356.itc", 0x28)
    Call(0, 8)
    Call(0, 9)
    LoadEffect(0x0, "event/ev17012.eff")
    SetChrPos(0x101, 1120, 4000, 58200, 0)
    SetChrPos(0x102, -1270, 4000, 57570, 0)
    SetChrPos(0x103, 420, 4000, 56870, 0)
    SetChrPos(0x104, 0, 4000, 59440, 0)
    SetChrPos(0xF4, -2540, 4000, 58190, 0)
    SetChrPos(0xF5, 2540, 4000, 57990, 0)
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
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x7)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 4000, 63500, 180)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "yuka_15_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x0, 0x1)
    OP_68(0, 4500, 72000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31500, 0)
    SetCameraDistance(29500, 2600)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 4000, 72000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(935, 0, 80, 0)
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    Sleep(600)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(-280, 5100, 60700, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15710, 0)
    Fade(500)
    OP_0D()
    Sleep(300)

    #C0072
    ChrTalk(
        0x101,
        "#00005F#11P#30Wあ……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#00102F#12P#30W……か……勝った……？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 36)
    BeginChrThread(0x102, 0, 0, 37)
    BeginChrThread(0x103, 0, 0, 38)
    BeginChrThread(0xF4, 0, 0, 39)
    BeginChrThread(0xF5, 0, 0, 40)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    #C0074
    ChrTalk(
        0x103,
        "#00206F#12P#40W……はあはあ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B9F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B56")
    OP_FC(0xFFF4)
    Jump("loc_3B59")

    label("loc_3B56")

    OP_FC(0xB)

    label("loc_3B59")


    #C0075
    ChrTalk(
        0x109,
        (
            "#10106F#13P#40W信じられない……\x01",
            "……本当に勝てたなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3C5F")

    label("loc_3B9F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C0A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BC9")
    OP_FC(0xFFF4)
    Jump("loc_3BCC")

    label("loc_3BC9")

    OP_FC(0xB)

    label("loc_3BCC")


    #C0076
    ChrTalk(
        0x10A,
        (
            "#00606F#13P#40W信じられん……\x01",
            "よく勝てたものだ……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3C5F")

    label("loc_3C0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C5F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C34")
    OP_FC(0xFFF4)
    Jump("loc_3C37")

    label("loc_3C34")

    OP_FC(0xB)

    label("loc_3C37")


    #C0077
    ChrTalk(
        0x106,
        "#10706F#13P#40W……奇蹟ですね……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3C5F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CCE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C89")
    OP_FC(0xFFF4)
    Jump("loc_3C8C")

    label("loc_3C89")

    OP_FC(0xB)

    label("loc_3C8C")


    #C0078
    ChrTalk(
        0x105,
        (
            "#10402F#13P#40W今度ばかりは……\x01",
            "……女神に感謝だね……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3D7B")

    label("loc_3CCE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D28")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CF8")
    OP_FC(0xFFF4)
    Jump("loc_3CFB")

    label("loc_3CF8")

    OP_FC(0xB)

    label("loc_3CFB")


    #C0079
    ChrTalk(
        0x106,
        "#10702F#13P#40W……奇蹟ですね……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3D7B")

    label("loc_3D28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D7B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D52")
    OP_FC(0xFFF4)
    Jump("loc_3D55")

    label("loc_3D52")

    OP_FC(0xB)

    label("loc_3D55")


    #C0080
    ChrTalk(
        0x10A,
        "#00602F#13P#40W……奇蹟だな……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3D7B")


    #C0081
    ChrTalk(
        0x104,
        "#00306F#11P#30W……ああ………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    BeginChrThread(0x104, 0, 0, 35)
    WaitChrThread(0x104, 0)
    Sleep(500)
    OP_68(-350, 5100, 61510, 1200)
    MoveCamera(38, 15, 0, 1200)
    OP_6E(600, 1200)
    SetCameraDistance(15710, 1200)
    OP_99(0x104, 0x8, 0x9C4, 0x4B0, 0x0)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)

    #C0082
    ChrTalk(
        0x104,
        "#00308F#11P#30W………………………………\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#00000F#12P#30W……何だかんだ言って……\x01",
            "“家族”だったんだな……？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#00202F#12P#30Wランディさんのこと……\x01",
            "……心配していたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#00306F#11P#30Wああ……分かってたさ。\x02\x03",

            "#00303F荒っぽいのはウチの一族の\x01",
            "流儀みたいなモンだからな……\x02\x03",

            "#00300F……だが……\x01",
            "これで何とかけじめは付けた。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_68(-300, 5100, 60840, 1100)
    OP_93(0x104, 0xB4, 0x190)
    OP_6F(0x79)

    #C0086
    ChrTalk(
        0x104,
        (
            "#00304F#5P《領域》も解放できたみてぇだ。\x02\x03",

            "#00302Fとりあえず……\x01",
            "門の所まで戻るとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        "#00104F#12Pそうね……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00002F#12P……お疲れ、ランディ。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x103,
        "#00204F#12Pお疲れさまでした……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        "#00309F#5Pハハ、そっちこそな。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    SetChrPos(0x0, 0, 4000, 57300, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_37()
    SetScenarioFlags(0x1A9, 0)
    OP_29(0xB2, 0x1, 0x6)
    ModifyEventFlags(0, 0, 0x80)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7354", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x162), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_32_37FB end

    def Function_33_410A(): pass

    label("Function_33_410A")


    def lambda_410F():
        OP_A6(0xFE, 0x0, 0x19, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_410F)
    Sleep(700)
    OP_9B(0x0, 0xFE, 0x162, 0x320, 0x3E8, 0x0)
    OP_95(0xFE, -1200, 4100, 63800, 1000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_410A end

    def Function_34_415F(): pass

    label("Function_34_415F")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, 650, 4100, 59850, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(700)
    Return()

    # Function_34_415F end

    def Function_35_4185(): pass

    label("Function_35_4185")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_4185 end

    def Function_36_4194(): pass

    label("Function_36_4194")

    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_4194 end

    def Function_37_41A3(): pass

    label("Function_37_41A3")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_41A3 end

    def Function_38_41AF(): pass

    label("Function_38_41AF")

    Sleep(200)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_41AF end

    def Function_39_41C1(): pass

    label("Function_39_41C1")

    Sleep(300)
    Sound(514, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x29)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41F6")
    SetChrSubChip(0xFE, 0x2)
    Jump("loc_41FA")

    label("loc_41F6")

    SetChrSubChip(0xFE, 0x0)

    label("loc_41FA")

    Return()

    # Function_39_41C1 end

    def Function_40_41FB(): pass

    label("Function_40_41FB")

    Sleep(400)
    SetChrChipByIndex(0xFE, 0x2A)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_422A")
    SetChrSubChip(0xFE, 0x2)
    Jump("loc_422E")

    label("loc_422A")

    SetChrSubChip(0xFE, 0x0)

    label("loc_422E")

    Return()

    # Function_40_41FB end

    def Function_41_422F(): pass

    label("Function_41_422F")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x7)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_41_422F end

    SaveToFile()

Try(main)
