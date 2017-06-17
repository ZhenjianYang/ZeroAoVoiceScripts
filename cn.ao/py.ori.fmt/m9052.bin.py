from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9052.bin",                # FileName
        "m9052",                    # MapName
        "m9052",                    # Location
        0x00C0,                     # MapIndex
        "ed7351",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 192, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9052",                  # 0
        "谢莉",                   # 1
        "念对白用的角色模型",     # 2
        "谢莉带领的魔兽",         # 3
        "谢莉带领的魔兽",         # 4
        "bm9039",                 # 5
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 3, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 13, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_E4", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm9039", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03401.dat", "ms81000.dat", "ms81000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7540", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51739.itc",                   # 00
    ))

    DeclNpc(0,       35000,   26500,   180,  389,  0x0, 0,   1,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 8,   0.0,                   7.0,                   34.0,                  156.25,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -1.399999976158142,    -6.800000190734863,    1.0])

    DeclActor(5000,    33000,   -6500,   1200,    5000,    34000,   -6500,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(892, 0)                                        # 0

    ScpFunction((
        "Function_0_2D4",          # 00, 0
        "Function_1_30F",          # 01, 1
        "Function_2_4FB",          # 02, 2
        "Function_3_7AA",          # 03, 3
        "Function_4_887",          # 04, 4
        "Function_5_B07",          # 05, 5
        "Function_6_C5A",          # 06, 6
        "Function_7_C9B",          # 07, 7
        "Function_8_CD8",          # 08, 8
        "Function_9_26E1",         # 09, 9
        "Function_10_270C",        # 0A, 10
        "Function_11_2737",        # 0B, 11
        "Function_12_2762",        # 0C, 12
        "Function_13_278D",        # 0D, 13
        "Function_14_27B8",        # 0E, 14
        "Function_15_27E3",        # 0F, 15
        "Function_16_27F5",        # 10, 16
        "Function_17_2807",        # 11, 17
        "Function_18_2813",        # 12, 18
        "Function_19_2825",        # 13, 19
        "Function_20_2856",        # 14, 20
        "Function_21_289F",        # 15, 21
        "Function_22_28E8",        # 16, 22
        "Function_23_2907",        # 17, 23
        "Function_24_2928",        # 18, 24
        "Function_25_31BC",        # 19, 25
        "Function_26_31E3",        # 1A, 26
        "Function_27_31F8",        # 1B, 27
        "Function_28_393E",        # 1C, 28
        "Function_29_3950",        # 1D, 29
        "Function_30_3962",        # 1E, 30
        "Function_31_3974",        # 1F, 31
        "Function_32_3980",        # 20, 32
        "Function_33_39CB",        # 21, 33
        "Function_34_3A19",        # 22, 34
        "Function_35_3E23",        # 23, 35
        "Function_36_3E80",        # 24, 36
        "Function_37_3EA1",        # 25, 37
        "Function_38_3EBC",        # 26, 38
        "Function_39_3EE3",        # 27, 39
        "Function_40_4190",        # 28, 40
        "Function_41_41B1",        # 29, 41
    ))


    def Function_0_2D4(): pass

    label("Function_0_2D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E5")
    Event(0, 4)

    label("loc_2E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2FF")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 24)
    Jump("loc_30E")

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_30E")
    ClearScenarioFlags(0x22, 1)
    Event(0, 27)

    label("loc_30E")

    Return()

    # Function_0_2D4 end

    def Function_1_30F(): pass

    label("Function_1_30F")

    OP_F0(0x1, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_328")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_3E4")
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_7s", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0s", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_5d", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_6n", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0d", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0n", 0x0, 0x1)
    Jump("loc_492")

    label("loc_3E4")

    SetMapObjFrame(0xFF, "magi10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_7s", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0s", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_5d", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_6n", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0d", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0n", 0x1, 0x1)

    label("loc_492")

    OP_1B(0x1, 0x0, 0x5)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AF")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CC")
    OP_1B(0x1, 0x0, 0x22)
    OP_1B(0x0, 0x0, 0x27)

    label("loc_4CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DD")
    Call(0, 38)

    label("loc_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4F4")
    Sound(124, 1, 60, 0)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_4FA")

    label("loc_4F4")

    Sound(124, 1, 80, 0)

    label("loc_4FA")

    Return()

    # Function_1_30F end

    def Function_2_4FB(): pass

    label("Function_2_4FB")

    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_761")

    #C0001
    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x103,
        (
            "#00203F……好像已经晕过去了，\x01",
            "看起来应该没受致命伤……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B7")

    #C0003
    ChrTalk(
        0x106,
        (
            "#10701F……怎么办？\x01",
            "倒是可以把她\x01",
            "抬到梅尔卡瓦……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC")

    label("loc_5B7")


    #C0004
    ChrTalk(
        0x102,
        (
            "#00101F该怎么办？\x01",
            "倒是可以把她\x01",
            "抬到梅尔卡瓦……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EC")


    #C0005
    ChrTalk(
        0x104,
        (
            "#00301F不，还是不要\x01",
            "那么做为好。\x02\x03",

            "#00306F如果她在舰内醒过来，\x01",
            "恐怕会非常危险，\x01",
            "暂时就先别管她了。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00003F也对……\x01",
            "不管怎么说，她还是敌人啊。\x02\x03",

            "#00000F谨慎起见，还是为她进行\x01",
            "最低限度的治疗吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        "#00100F是啊，那么……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人为谢莉\x01",
            "做了应急救治处理。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    OP_0D()

    #C0009
    ChrTalk(
        0x102,
        "#00104F……嗯，这样就可以了。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00000F好，那我们就走吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CE, 6)
    Jump("loc_7A6")

    label("loc_761")


    #C0011
    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好像已经完全昏迷了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7A6")

    TalkEnd(0x8)
    Return()

    # Function_2_4FB end

    def Function_3_7AA(): pass

    label("Function_3_7AA")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87A")
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

    label("loc_87A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_7AA end

    def Function_4_887(): pass

    label("Function_4_887")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(-510, 35500, 34190, 0)
    MoveCamera(46, 51, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17100, 0)
    SetChrPos(0x0, 0, 35000, 36000, 180)
    SetChrPos(0x1, 0, 35000, 36000, 180)
    SetChrPos(0x2, 0, 35000, 36000, 180)
    SetChrPos(0x3, 0, 35000, 36000, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_997():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_997)

    def lambda_9A8():
        OP_95(0xFE, -640, 35000, 32810, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9A8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_9FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_9FF)

    def lambda_A10():
        OP_95(0xFE, -1720, 35000, 33060, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A10)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_A6D)

    def lambda_A7E():
        OP_95(0xFE, 930, 35000, 34060, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A7E)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_AD5)

    def lambda_AE6():
        OP_95(0xFE, -2850, 35000, 33620, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_AE6)
    WaitChrThread(0x3, 1)
    Sleep(1000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_4_887 end

    def Function_5_B07(): pass

    label("Function_5_B07")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_B60():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B60)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BAB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_BAB)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_BF6)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_C41)
    Sleep(1000)
    NewScene("m9002", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_5_B07 end

    def Function_6_C5A(): pass

    label("Function_6_C5A")

    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C72")
    OP_CF(0x1, 0xF5, 0x4)

    label("loc_C72")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C86")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_C86")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C9A")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_C9A")

    Return()

    # Function_6_C5A end

    def Function_7_C9B(): pass

    label("Function_7_C9B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAF")
    OP_CF(0x1, 0xF5, 0x4)

    label("loc_CAF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC3")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_CC3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD7")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_CD7")

    Return()

    # Function_7_C9B end

    def Function_8_CD8(): pass

    label("Function_8_CD8")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04600.itp")
    CreatePortrait(1, 224, 0, 480, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04602.itp")
    LoadChrToIndex("chr/ch03450.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    SoundLoad(3260)
    SoundLoad(3261)
    SoundLoad(3262)
    SoundLoad(3263)
    SoundLoad(3964)
    SoundLoad(3965)
    SoundLoad(3966)
    SoundLoad(3967)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E16")
    Call(0, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE2")
    OP_CF(0x1, 0xF5, 0x4)
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_DE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFC")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_DFC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E16")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_E16")

    LoadChrToIndex("chr/ch03454.itc", 0x25)
    LoadChrToIndex("monster/ch81050.itc", 0x26)
    LoadChrToIndex("apl/ch51738.itc", 0x27)
    LoadEffect(0x0, "event\\ev602_01.eff")
    SetChrPos(0x102, -650, 35000, -750, 0)
    SetChrPos(0x101, -1100, 33000, 750, 0)
    SetChrPos(0x103, 200, 33000, 0, 0)
    SetChrPos(0x104, 1100, 33000, 1100, 0)
    SetChrPos(0xF4, 0, 33000, 1800, 0)
    SetChrPos(0xF5, 850, 33000, -1000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 35000, 25000, 180)
    ClearChrFlags(0x9, 0x80)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 2300, 38000, 18000, 0)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, -2100, 35000, 26000, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 2100, 35000, 26000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 35400, -800, 0)
    MoveCamera(60, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 36200, 6000, 3900)
    MoveCamera(55, 20, 0, 3900)
    OP_6E(600, 3900)
    SetCameraDistance(17280, 3900)
    FadeToBright(1000, 0)

    def lambda_103E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_103E)
    Sleep(100)

    def lambda_1056():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1056)
    Sleep(100)

    def lambda_106E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_106E)
    Sleep(100)

    def lambda_1086():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1086)
    Sleep(100)

    def lambda_109E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_109E)
    Sleep(100)

    def lambda_10B6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_10B6)
    OP_0D()
    Sleep(2100)
    StopBGM(0x9C4)
    StopSound(124, 3000, 80)
    OP_C9(0x0, 0x80000000)

    #N0014
    NpcTalk(
        0x9,
        "少女的声音",
        "#3964V#N#30W#20A啊哈……终于来了！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_24(0xF7C)
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
    OP_C9(0x1, 0x80000000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7571", 0)
    BeginChrThread(0xF4, 0, 0, 9)
    Sleep(50)
    BeginChrThread(0x104, 0, 0, 10)
    Sleep(50)
    BeginChrThread(0x103, 0, 0, 11)
    Sleep(50)
    BeginChrThread(0x101, 0, 0, 13)
    Sleep(50)
    BeginChrThread(0x102, 0, 0, 12)
    Sleep(50)
    BeginChrThread(0xF5, 0, 0, 14)
    OP_68(-1300, 36600, 19180, 4000)
    MoveCamera(41, 14, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(14680, 4000)
    OP_6F(0x79)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF5, 0)

    #C0015
    ChrTalk(
        0x106,
        "#10701F#12P『血腥谢莉』……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00306F#12P呼……\x01",
            "这次竟然如此耐心地等着我们啊。\x02\x03",

            "#00301F要是换作平时的你，\x01",
            "肯定会忍耐不住，主动发起袭击的。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#04606F#5P哼，真过分啊，\x01",
            "兰迪哥。\x02\x03",

            "#04602F不过，说的也没错。如果只有兰迪哥\x01",
            "和你们几个，我自然会迅速出击，完成歼灭。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        "#00310F#12P……喂。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        "#00211F#12P（真是太乱来了……）\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        (
            "#00109F#12P（啊、啊哈哈……\x01",
            "  好像不是在开玩笑。）\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0021
    AnonymousTalk(
        0x8,
        (
            "那么，莉夏……\x02\x03",

            "你现在已经有足够斗志了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0022
    AnonymousTalk(
        0x106,
        "#10708F………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x15E, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(400)

    #A0023
    AnonymousTalk(
        0x8,
        (
            "在彩虹剧团未能了结的一战……\x02\x03",

            "令人心情无比愉快的『厮杀』……\x01",
            "就让我们立刻开始吧。\x02\x03",

            "我正是为此才在这里\x01",
            "等着你的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetMessageWindowPos(14, 280, -1, 3)
    OP_C9(0x0, 0x80000000)

    #A0024
    AnonymousTalk(
        0x106,
        "#10703F#3260V#30W#15A我拒绝。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
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
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x64, 1800, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0025
    ChrTalk(
        0x101,
        "#00005F#6P#N哎……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_165C")

    #C0026
    ChrTalk(
        0x10A,
        "#00605F#12P哦……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_16B9")

    label("loc_165C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_168A")

    #C0027
    ChrTalk(
        0x105,
        "#10402F#12P嘿……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_16B9")

    label("loc_168A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16B9")

    #C0028
    ChrTalk(
        0x109,
        "#10105F#12P莉夏小姐……？\x02",
    )

    CloseMessageWindow()

    label("loc_16B9")

    OP_63(0x8, 0x64, 1800, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0029
    ChrTalk(
        0x8,
        (
            "#04601F#5P等、等一下！\x02\x03",

            "都来到这里了，\x01",
            "怎么能说这种话！？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x106,
        (
            "#10703F#12P你和我……\x01",
            "的确有某些方面很相似。\x02\x03",

            "#10708F我身为『银』……\x01",
            "从儿时起，便接受着\x01",
            "那样的教育。\x02\x03",

            "#10701F你多半也是从刚刚懂事的时候开始，\x01",
            "就已经投身于名为战场的世界了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#04605F#5P啊……嗯，算是吧。\x02\x03",

            "#04604F初次实战是在九岁，\x01",
            "好像和兰迪哥一样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#00308F#12P哼……只能说\x01",
            "老爸和叔叔\x01",
            "都是疯子。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#04609F#5P不过，我从来都没有\x01",
            "讨厌过这种生活哦。\x02\x03",

            "#04602F虽然有时的确会很疼、很艰苦，\x01",
            "但战场充满了吸引力，\x01",
            "没有任何东西能比它更让我兴奋。\x02\x03",

            "莉夏难道不是这样想的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x106,
        (
            "#10706F#12P很遗憾……我对战斗的感情\x01",
            "既非喜爱，也非厌恶。\x02\x03",

            "#10708F在我看来，杀戮就如同\x01",
            "空气一般……\x02\x03",

            "即使夺去目标的性命，\x01",
            "我也不会有什么特别的感慨。\x02\x03",

            "#10710F从这层意义上说，我也许比你\x01",
            "更加缺少人类应有的感情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#00001F#6P#N……莉夏。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0036
    ChrTalk(
        0x102,
        "#00108F#12P莉夏小姐……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#04606F#5P唔，真可怜啊。\x02\x03",

            "#04602F不过，也还好吧。\x01",
            "反正你又找到了彩虹剧团\x01",
            "这个新乐子。\x02\x03",

            "#04609F对我来说，\x01",
            "莉夏是不是『银』\x01",
            "都无所谓哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x28, 0x0, 0x7D0, 0xC8)

    #C0038
    ChrTalk(
        0x106,
        "#10708F#12P………你……………\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x103,
        "#00206F#12P………好过分。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#00306F#12P……你……\x01",
            "真是彻底疯了……\x02\x03",

            "#00311F你真的明白自己\x01",
            "做了什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "#04605F#5P是指袭击彩虹剧团的事情吗？\x02\x03",

            "#04606F如果不那样做，\x01",
            "莉夏就不愿意\x01",
            "认真和我厮杀嘛。\x02\x03",

            "#04600F我也觉得那样做有些不好，但是没办法啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        "#00310F#12P……唔………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C17")

    #C0043
    ChrTalk(
        0x10A,
        "#00606F#12P无法沟通啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C80")

    label("loc_1C17")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C4D")

    #C0044
    ChrTalk(
        0x105,
        "#10406F#12P……无法沟通呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C80")

    label("loc_1C4D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C80")

    #C0045
    ChrTalk(
        0x109,
        "#10108F#12P根本不能沟通呢……\x02",
    )

    CloseMessageWindow()

    label("loc_1C80")


    #C0046
    ChrTalk(
        0x101,
        "#00008F#6P#N……莉夏……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0047
    ChrTalk(
        0x106,
        (
            "#10704F#11P没关系，\x01",
            "我很明白她的想法。\x02\x03",

            "#10708F如果我在『银』的道路上\x01",
            "找到了快乐……\x02\x03",

            "#10710F肯定也会成为一个\x01",
            "和她一样的人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        "#04605F#5P？？？\x02",
    )

    CloseMessageWindow()
    OP_68(-1210, 36600, 19580, 750)
    MoveCamera(40, 14, 0, 750)

    def lambda_1D5A():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1D5A)
    OP_6F(0x79)
    Sleep(300)

    #C0049
    ChrTalk(
        0x106,
        (
            "#10703F#12P谢莉小姐，\x01",
            "我可以坦白地告诉你。\x02\x03",

            "#10701F我不想死。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x64, 1800, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0050
    ChrTalk(
        0x8,
        "#04605F#5P…………哎？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x106,
        (
            "#10706F#12P在来到克洛斯贝尔之前……\x01",
            "我一直都觉得死亡\x01",
            "并不是什么大不了的事情。\x02\x03",

            "#10708F不，也许我以前从来都没有\x01",
            "思考过自己的死亡。\x02\x03",

            "#10710F不过，我现在很想活下去。\x02\x03",

            "我想活下去，\x01",
            "想和重要的人们一起\x01",
            "追逐那新发现的光芒。\x02\x03",

            "#10704F所以……\x01",
            "我无法接受你的\x01",
            "『厮杀』挑战。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#00002F#6P#N莉夏……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0053
    ChrTalk(
        0x102,
        "#00104F#12P#N莉夏小姐……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0054
    ChrTalk(
        0x104,
        (
            "#00302F#12P……说的很好啊，\x01",
            "莉夏。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x64, 1800, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0055
    ChrTalk(
        0x8,
        (
            "#04601F#5P……既然如此……\x02\x03",

            "#04606F既然如此，你为何还要\x01",
            "特意到这种地方来……？\x02\x03",

            "#04602F你难道不想和我\x01",
            "痛快一战吗……？\x02\x03",

            "你难道不想给再也无法站起来\x01",
            "的伊莉娅报仇吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x106,
        (
            "#10703F#12P伊莉娅小姐\x01",
            "一定会重新站起来的。\x02\x03",

            "#10701F所以，我并没有\x01",
            "向你复仇的理由。\x02\x03",

            "#10706F如果你真的很想接受复仇，\x01",
            "那就等伊莉娅小姐康复之后\x01",
            "去见她吧。\x02\x03",

            "#10710F我想她多半会赏你一记\x01",
            "重重的大耳光。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0057
    ChrTalk(
        0x8,
        "#04601F#5P……唔……！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        "#00012F#6P#N……哈哈………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0059
    ChrTalk(
        0x103,
        (
            "#00204F#12P的确，以伊莉娅小姐的作风来说，\x01",
            "只需那种程度的教训，就会把事情一笔勾销了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x106,
        (
            "#10704F#12P至于我特意与罗伊德警官他们\x01",
            "一同来此的理由……\x02\x03",

            "那就是为了向你和我自己\x01",
            "证明一件事情──\x02\x03",

            "#10702F现在的我，比你更强。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x64, 1800, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0061
    ChrTalk(
        0x8,
        "#04605F#5P#4S！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(531, 0, 60, 0)
    Sound(540, 0, 60, 0)
    MoveCamera(38, 14, 0, 750)
    BeginChrThread(0x106, 0, 0, 23)
    WaitChrThread(0x106, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7540", 0)
    SetCameraDistance(13000, 30000)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0062
    ChrTalk(
        0x106,
        (
            "#10703F#3261V#12P#40W#40A我穿越了黑暗，\x01",
            "寻找到了崭新的光辉……\x02\x03",

            "#3262V#40A而你一味沉浸在染满鲜血的硝烟之路，\x01",
            "注定及不上我。\x02\x03",

            "#10701F#3263V#25A我现在就要证明这一点。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    def lambda_2356():
        OP_A6(0xFE, 0x0, 0x28, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2356)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_2376():
        OP_A6(0xFE, 0x0, 0x28, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2376)
    WaitChrThread(0x8, 2)
    Sleep(300)
    Sleep(500)
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    Sleep(200)
    Sound(531, 0, 100, 0)
    Sleep(300)

    #C0063
    ChrTalk(
        0x8,
        (
            "#04604F#5P#30W……啊哈哈……\x01",
            "莉夏，你真是太棒了……\x02\x03",

            "你让我现在的情绪……\x01",
            "……远比准备单纯厮杀时兴奋得多……\x02\x03",

            "#04611F来克洛斯贝尔……\x01",
            "真是个正确的决定啊……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-130, 36600, 19430, 0)
    MoveCamera(358, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15180, 0)
    SetCameraDistance(14180, 1500)
    OP_0D()
    SetChrSubChip(0x106, 0x2)
    OP_A0(0x8, 1800, 0x0, 0x4)
    Sound(817, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 20)
    BeginChrThread(0xA, 2, 0, 22)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 21)
    BeginChrThread(0xB, 2, 0, 22)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x79)
    SetCameraDistance(11000, 24000)
    Sleep(800)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0064
    AnonymousTalk(
        0x8,
        (
            "#3965V#5P#40W#35A很好！\x01",
            "那我们就赶快开始吧！\x02\x03",

            "#3966V#30A兰迪哥，你们也\x01",
            "一起来吧！\x02\x03",

            "#3967V#35A一定要努力跟上我们\x01",
            "的战斗节奏哦！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    BeginChrThread(0x101, 0, 0, 15)
    BeginChrThread(0x102, 0, 0, 16)
    BeginChrThread(0x103, 0, 0, 17)
    BeginChrThread(0x104, 0, 0, 18)
    BeginChrThread(0xF5, 0, 0, 19)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Sleep(150)

    #C0065
    ChrTalk(
        0x104,
        "#00307F#12P#N#10A不要大意……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00007F#6P#N#38A开始迎击！\x01",
            "全力援护莉夏！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, 160, -1, -1)
    SetChrName("众同伴")
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #A0067
    AnonymousTalk(
        0xFF,
        "#4S#12A噢噢！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x100, 0x46, 0xFF)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x106, 0x2)
    ClearChrFlags(0x106, 0x1000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 24)
    Return()

    # Function_8_CD8 end

    def Function_9_26E1(): pass

    label("Function_9_26E1")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0x88B8, 0x4614, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_9_26E1 end

    def Function_10_270C(): pass

    label("Function_10_270C")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0x88B8, 0x413C, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_10_270C end

    def Function_11_2737(): pass

    label("Function_11_2737")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0x88B8, 0x3C0A, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_2737 end

    def Function_12_2762(): pass

    label("Function_12_2762")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0x88B8, 0x3EC6, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_2762 end

    def Function_13_278D(): pass

    label("Function_13_278D")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0x88B8, 0x4132, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_278D end

    def Function_14_27B8(): pass

    label("Function_14_27B8")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0x88B8, 0x406A, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_27B8 end

    def Function_15_27E3(): pass

    label("Function_15_27E3")

    Sleep(50)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_27E3 end

    def Function_16_27F5(): pass

    label("Function_16_27F5")

    Sleep(100)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_27F5 end

    def Function_17_2807(): pass

    label("Function_17_2807")

    Sleep(150)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_2807 end

    def Function_18_2813(): pass

    label("Function_18_2813")

    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_2813 end

    def Function_19_2825(): pass

    label("Function_19_2825")

    Sleep(250)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_284D")
    Sound(531, 0, 100, 0)

    label("loc_284D")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_2825 end

    def Function_20_2856(): pass

    label("Function_20_2856")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_20_2856 end

    def Function_21_289F(): pass

    label("Function_21_289F")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_21_289F end

    def Function_22_28E8(): pass

    label("Function_22_28E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2906")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_22_28E8")

    label("loc_2906")

    Return()

    # Function_22_28E8 end

    def Function_23_2907(): pass

    label("Function_23_2907")

    SetChrChipByIndex(0x106, 0x27)
    SetChrSubChip(0x106, 0x0)
    SetChrFlags(0x106, 0x2)
    SetChrFlags(0x106, 0x1000)
    SetChrSubChip(0x106, 0x0)
    Sleep(143)
    SetChrSubChip(0x106, 0x1)
    Sleep(429)
    Return()

    # Function_23_2907 end

    def Function_24_2928(): pass

    label("Function_24_2928")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("apl/ch51739.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadEffect(0x0, "event/ev17082.eff")
    SoundLoad(3968)
    SoundLoad(3969)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29D5")
    Call(0, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29A1")
    OP_CF(0x1, 0xF5, 0x4)
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_29A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29BB")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_29BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29D5")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_29D5")

    LoadChrToIndex("chr/ch00356.itc", 0x25)
    SetChrPos(0x101, -2540, 35000, 20690, 0)
    SetChrPos(0x102, -1270, 35000, 20070, 0)
    SetChrPos(0x103, 420, 35000, 19370, 0)
    SetChrPos(0x104, 1120, 35000, 20700, 0)
    SetChrPos(0xF4, 0, 35000, 22340, 0)
    SetChrPos(0xF5, 2540, 35000, 20490, 0)
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
    SetChrPos(0x8, 0, 35000, 26500, 90)
    OP_8E(0x8, "谢莉")
    OP_68(-120, 35300, 23440, 0)
    MoveCamera(160, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27500, 0)
    SetCameraDistance(22800, 4000)
    FadeToBright(1500, 0)
    PlayBGM("ed7568", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x238), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    #C0068
    ChrTalk(
        0x8,
        (
            "#04606F#6P#80W#30A呼……呼…#1500W…\x01",
            "#04609F#40W#4S……啊哈哈哈哈哈哈哈……！\x02\x03",

            "#04602F#3969V#40A输了呢……\x01",
            "还真的让你成功证明了……\x02",
        )
    )
    #Auto

    Sleep(3000)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrSubChip(0x8, 0x1)
    OP_68(0, 36100, 23500, 0)
    MoveCamera(46, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14680, 0)
    OP_0D()
    Sleep(300)
    #Sound(2632, 255, 100, 0)    #voice#Rixia

    #C0069
    ChrTalk(
        0x106,
        "#10706F#12P#40W#31A呼……呼……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #C0070
    ChrTalk(
        0x8,
        (
            "#04604F#5P#40W不过……\x01",
            "……稍微有些犯规吧……？\x02\x03",

            "#04600F兰迪哥他们一拥而上也就罢了……\x01",
            "你好像还拥有不止自己一人的力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x106,
        (
            "#10704F#12P#40W……这正是……\x01",
            "我所寻找到的力量……\x02\x03",

            "#10710F如果你有什么不满……\x01",
            "不妨也试着去寻找这种力量如何……？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "#04604F#5P#40W呵呵……现在好像\x01",
            "已经来不及找了……\x02\x03",

            "#04602F算啦……既然如此，\x01",
            "你就赶快杀了我吧……\x02\x03",

            "#04604F事到如今，我已经……\x01",
            "……没有什么未了的心事了……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x106,
        (
            "#10706F#12P#40W……都说过不会杀你了……\x02\x03",

            "#10701F请认真听别人说话啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "#04606F#5P#40W啧……哎哎……\x02\x03",

            "本来还以为可以\x01",
            "在心情最棒的时候死掉呢……\x02",
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
    OP_63(0xF5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0075
    ChrTalk(
        0x104,
        (
            "#00307F#11P喂！\x01",
            "不要再耍小性子了！\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "#04604F#5P#40W啊哈哈……！\x01",
            "兰迪哥……好凶啊……\x02\x03",

            "#04601F话说在先……\x01",
            "爸爸可在前面等着你们……\x02\x03",

            "你们最好……\x01",
            "拿出全部觉悟哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        (
            "#00306F#11P……哼，\x01",
            "不用你说我也知道。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "#04604F#5P#40W小哥，你们也……\x01",
            "呼……尽量加油吧……\x02\x03",

            "那个『剑圣』也很厉害……\x01",
            "……大小姐似乎也相当危险……\x02\x03",

            "#04606F另外……那个孩子……\x01",
            "看起来好像非常痛苦……\x02\x03",

            "#04600F为了让她恢复笑容……\x01",
            "……你们可要努力……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#00001F#12P#N……嗯，\x01",
            "那当然。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0080
    ChrTalk(
        0x8,
        (
            "#04606F#5P#50W……不行了……完全没力气啦……\x02\x03",

            "#04604F#60W莉夏……\x01",
            "下次还要……一起玩哟……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20680, 4500)
    MoveCamera(46, 25, 0, 4500)
    BeginChrThread(0x8, 0, 0, 26)
    WaitChrThread(0x8, 0)
    Sleep(300)
    Sound(202, 0, 100, 0)
    Sound(181, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 35050, 23440, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    Sleep(1000)
    StopSound(124, 3000, 60)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m9050", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_2928 end

    def Function_25_31BC(): pass

    label("Function_25_31BC")

    OP_9B(0x0, 0xFE, 0x15E, 0xDAC, 0x7D0, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    Sound(802, 0, 50, 0)
    Sound(805, 0, 20, 0)
    Sleep(150)
    Return()

    # Function_25_31BC end

    def Function_26_31E3(): pass

    label("Function_26_31E3")

    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    Return()

    # Function_26_31E3 end

    def Function_27_31F8(): pass

    label("Function_27_31F8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51739.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3283")
    Call(0, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_324F")
    OP_CF(0x1, 0xF5, 0x4)
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_324F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3269")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_3269")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3283")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_3283")

    LoadChrToIndex("chr/ch00350.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_329C")
    Call(0, 6)

    label("loc_329C")

    LoadEffect(0x0, "event/ev17012.eff")
    SetChrPos(0x101, -2540, 35000, 20690, 0)
    SetChrPos(0x102, -1270, 35000, 20070, 0)
    SetChrPos(0x103, 420, 35000, 19370, 0)
    SetChrPos(0x104, 1120, 35000, 20700, 0)
    SetChrPos(0xF4, 0, 35000, 22340, 0)
    SetChrPos(0xF5, 2540, 35000, 20490, 0)
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
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 35000, 26500, 90)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    OP_68(0, 36000, 36000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31500, 0)
    SetCameraDistance(29500, 2600)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 35000, 36000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(500)
    Sound(935, 0, 80, 0)
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    Sleep(600)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(-320, 36100, 21970, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15780, 0)
    OP_0D()
    Sleep(300)
    BeginChrThread(0x101, 0, 0, 28)
    BeginChrThread(0x102, 0, 0, 29)
    BeginChrThread(0x103, 0, 0, 30)
    BeginChrThread(0x104, 0, 0, 31)
    BeginChrThread(0xF4, 0, 0, 32)
    BeginChrThread(0xF5, 0, 0, 33)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    #C0081
    ChrTalk(
        0x106,
        "#10706F#11P……呼……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        (
            "#00108F#12P真是个……\x01",
            "不安分的孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#00306F#11P呼……\x01",
            "抱歉，我妹妹给大家添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#00000F#6P不过……她好像\x01",
            "也很关心琪雅呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_3592():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3592)
    Sleep(50)

    def lambda_35A2():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_35A2)
    Sleep(50)

    def lambda_35B2():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_35B2)
    Sleep(50)

    def lambda_35C2():
        TurnDirection(0xF5, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_35C2)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF5, 0)

    #C0085
    ChrTalk(
        0x101,
        (
            "#00001F#6P莉夏，\x01",
            "你的身体不要紧吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x106,
        (
            "#10704F#11P……是的，\x01",
            "多亏有大家支援。\x02\x03",

            "#10708F而且……伊莉娅小姐给予我的力量\x01",
            "一直在我的体内。\x02\x03",

            "#10710F所以才能取得这一战的胜利。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36C5")

    #C0087
    ChrTalk(
        0x109,
        "#10109F#11P呵呵，原来如此……\x02",
    )

    CloseMessageWindow()
    Jump("loc_372C")

    label("loc_36C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36FB")

    #C0088
    ChrTalk(
        0x105,
        "#10404F#11P呵呵，原来如此。\x02",
    )

    CloseMessageWindow()
    Jump("loc_372C")

    label("loc_36FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_372C")

    #C0089
    ChrTalk(
        0x10A,
        "#00604F#11P呵……原来如此。\x02",
    )

    CloseMessageWindow()

    label("loc_372C")


    #C0090
    ChrTalk(
        0x103,
        (
            "#00202F#12P如此看来，\x01",
            "谢莉小姐的确是\x01",
            "毫无胜算。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x106,
        (
            "#10704F#11P嗯……\x01",
            "我绝对不可能输给她。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x106, 0xE1, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_END)), "loc_37FA")

    #C0092
    ChrTalk(
        0x106,
        (
            "#10702F#5P这样一来，我想这个『领域』\x01",
            "就会彻底开放了。\x02\x03",

            "我们暂且返回入口处如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_384F")

    label("loc_37FA")


    #C0093
    ChrTalk(
        0x106,
        (
            "#10702F#5P这样一来，我想这个『领域』\x01",
            "就会彻底开放了。\x02\x03",

            "我们暂且返回入口处如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_384F")


    #C0094
    ChrTalk(
        0x101,
        "#00000F#6P嗯，同意。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x8, 500)
    Sleep(300)

    #C0095
    ChrTalk(
        0x104,
        (
            "#00308F#11P至于这家伙……\x01",
            "算啦，也只能把她扔在这里，\x01",
            "等她自己醒来了。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16030, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    SetChrPos(0x0, 0, 35000, 18500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_37()
    SetScenarioFlags(0x1A8, 3)
    OP_29(0xB2, 0x1, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    OP_1B(0x1, 0x0, 0x22)
    OP_1B(0x0, 0x0, 0x27)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7351", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_27_31F8 end

    def Function_28_393E(): pass

    label("Function_28_393E")

    Sleep(200)
    Sound(805, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_393E end

    def Function_29_3950(): pass

    label("Function_29_3950")

    Sleep(300)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_3950 end

    def Function_30_3962(): pass

    label("Function_30_3962")

    Sleep(400)
    Sound(805, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_3962 end

    def Function_31_3974(): pass

    label("Function_31_3974")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_3974 end

    def Function_32_3980(): pass

    label("Function_32_3980")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_399D")
    Sound(540, 0, 50, 0)
    Jump("loc_39C2")

    label("loc_399D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39C2")
    Sound(531, 0, 50, 0)

    label("loc_39C2")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_3980 end

    def Function_33_39CB(): pass

    label("Function_33_39CB")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39EB")
    Sound(540, 0, 50, 0)
    Jump("loc_3A10")

    label("loc_39EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A10")
    Sound(531, 0, 50, 0)

    label("loc_3A10")

    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_39CB end

    def Function_34_3A19(): pass

    label("Function_34_3A19")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51739.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A52")
    Call(0, 6)

    label("loc_3A52")

    LoadEffect(0x1, "event/evwarp.eff")
    SoundLoad(3979)
    SoundLoad(3980)
    SoundLoad(3981)
    SoundLoad(3982)
    OP_8E(0x8, "谢莉")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 35000, 26500, 90)
    SetChrPos(0xF5, 650, 35000, 33200, 0)
    SetChrPos(0x102, -650, 35000, 33200, 0)
    SetChrPos(0x103, 1850, 35000, 33900, 0)
    SetChrPos(0x104, -1850, 35000, 33900, 0)
    SetChrPos(0x101, 650, 35000, 32500, 0)
    SetChrPos(0xF4, -650, 35000, 32500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_92(0xF5, 0x0, 0x8CA0, 0x0)
    OP_92(0x101, 0x0, 0x8CA0, 0x0)
    OP_92(0x102, 0x0, 0x8CA0, 0x0)
    OP_92(0x103, 0x0, 0x8CA0, 0x0)
    OP_92(0x104, 0x0, 0x8CA0, 0x0)
    OP_92(0xF4, 0x0, 0x8CA0, 0x0)
    OP_68(-1040, 37000, 33640, 0)
    MoveCamera(31, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(16230, 8000)
    FadeToBright(1000, 0)
    Sleep(400)
    BeginChrThread(0xF5, 0, 0, 35)
    Sleep(900)
    BeginChrThread(0x102, 0, 0, 35)
    Sleep(600)
    BeginChrThread(0x103, 0, 0, 35)
    Sleep(600)
    BeginChrThread(0x104, 0, 0, 35)
    Sleep(600)
    BeginChrThread(0x101, 0, 0, 35)
    Sleep(800)
    BeginChrThread(0xF4, 0, 0, 35)
    Sleep(600)
    StopBGM(0x1770)
    OP_6F(0x79)
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 36)
    WaitChrThread(0x8, 0)
    Sleep(500)

    #C0096
    ChrTalk(
        0x8,
        "#04601F#12P#N………………………………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-3200, 37000, 36160, 0)
    OP_68(-2950, 37000, 32200, 2500)
    MoveCamera(142, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(8510, 0)
    OP_63(0x8, 0xFFFFFEA2, 1050, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x8)
    OP_6F(0x79)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0097
    ChrTalk(
        0x8,
        (
            "#04606F#3979V#5P#50W唉……趁着刚才的机会，\x01",
            "明明可以砍下好几个人的脑袋……\x02\x03",

            "#04600F#3980V#50W真是的……\x01",
            "……我的脑子是不是出问题了……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF8C)
    Sleep(300)
    OP_63(0x8, 0xFFFFFEA2, 1050, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)
    BeginChrThread(0x8, 0, 0, 37)
    WaitChrThread(0x8, 0)
    Sleep(300)
    SetCameraDistance(20940, 20000)
    Sleep(500)

    #C0098
    ChrTalk(
        0x8,
        "#04606F#3981V#5P#60W#40A#3S不行……这次真是撑不住了……\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(1500)

    #C0099
    ChrTalk(
        0x8,
        (
            "#04606F#3982V#5P#60W#60A#2S……看来还是……\x01",
            "接受『他们』的招揽……比较好吧……？\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    StopSound(124, 1000, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_37()
    SetScenarioFlags(0x1A8, 4)
    WaitBGM()
    Sleep(1000)
    EventEnd(0x5)
    NewScene("m9002", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_34_3A19 end

    def Function_35_3E23(): pass

    label("Function_35_3E23")

    OP_95(0xFE, 0, 36000, 36000, 1500, 0x0)
    Sound(936, 0, 80, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_35_3E23 end

    def Function_36_3E80(): pass

    label("Function_36_3E80")

    SetChrSubChip(0xFE, 0x4)
    Sound(358, 0, 50, 0)
    Sleep(150)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0x5)
    Fade(250)
    OP_0D()
    Sleep(450)
    Return()

    # Function_36_3E80 end

    def Function_37_3EA1(): pass

    label("Function_37_3EA1")

    SetChrSubChip(0xFE, 0x6)
    Sound(358, 0, 40, 0)
    Sleep(150)
    Sound(531, 0, 40, 0)
    SetChrSubChip(0xFE, 0x7)
    Sleep(300)
    Return()

    # Function_37_3EA1 end

    def Function_38_3EBC(): pass

    label("Function_38_3EBC")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_38_3EBC end

    def Function_39_3EE3(): pass

    label("Function_39_3EE3")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51739.itc", 0x1E)
    LoadEffect(0x1, "event/evwarp.eff")
    SoundLoad(3979)
    SoundLoad(3980)
    SoundLoad(3981)
    SoundLoad(3982)
    OP_8E(0x8, "谢莉")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, 35000, 26500, 90)
    OP_68(1800, 34000, 10000, 0)
    OP_68(1800, 34000, 28300, 2500)
    OP_6E(600, 0)
    SetCameraDistance(15180, 0)
    FadeToBright(1000, 0)
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 40)
    WaitChrThread(0x8, 0)
    Sleep(500)

    #C0100
    ChrTalk(
        0x8,
        "#04601F#12P#N………………………………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_63(0x8, 0xFFFFFEA2, 1400, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x8)
    OP_6F(0x79)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0101
    ChrTalk(
        0x8,
        (
            "#04606F#3979V#5P#50W唉……趁着刚才的机会，\x01",
            "明明可以砍下好几个人的脑袋……\x02\x03",

            "#04600F#3980V#50W真是的……\x01",
            "……我的脑子是不是出问题了……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF8C)
    Sleep(300)
    OP_63(0x8, 0xFFFFFEA2, 1400, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)
    BeginChrThread(0x8, 0, 0, 41)
    WaitChrThread(0x8, 0)
    Sleep(300)
    SetCameraDistance(20940, 20000)
    Sleep(500)

    #C0102
    ChrTalk(
        0x8,
        "#04606F#3981V#5P#60W#40A#3S不行……这次真是撑不住了……\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(1500)

    #C0103
    ChrTalk(
        0x8,
        (
            "#04606F#3982V#5P#60W#60A#2S……看来还是……\x01",
            "接受『他们』的招揽……比较好吧……？\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    StopSound(124, 1000, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_37()
    SetScenarioFlags(0x1A8, 4)
    WaitBGM()
    Sleep(1000)
    EventEnd(0x5)
    NewScene("m9050", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_39_3EE3 end

    def Function_40_4190(): pass

    label("Function_40_4190")

    SetChrSubChip(0xFE, 0x3)
    Sound(358, 0, 50, 0)
    Sleep(150)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0x2)
    Fade(250)
    OP_0D()
    Sleep(450)
    Return()

    # Function_40_4190 end

    def Function_41_41B1(): pass

    label("Function_41_41B1")

    SetChrSubChip(0xFE, 0x2)
    Sound(358, 0, 40, 0)
    Sleep(150)
    Sound(531, 0, 40, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    Return()

    # Function_41_41B1 end

    SaveToFile()

Try(main)
