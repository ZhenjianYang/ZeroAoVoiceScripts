from ScenarioHelper import *

def main():
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
        "战鬼西格蒙德",           # 1
        "显示台词用人物模型",     # 2
        "西格蒙德带领的魔兽",     # 3
        "西格蒙德带领的魔兽",     # 4
        "SE控制",                 # 5
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
        "Function_3_7F2",          # 03, 3
        "Function_4_8D6",          # 04, 4
        "Function_5_B5E",          # 05, 5
        "Function_6_CB7",          # 06, 6
        "Function_7_D18",          # 07, 7
        "Function_8_D79",          # 08, 8
        "Function_9_DDA",          # 09, 9
        "Function_10_E3B",         # 0A, 10
        "Function_11_2C57",        # 0B, 11
        "Function_12_2C82",        # 0C, 12
        "Function_13_2CAD",        # 0D, 13
        "Function_14_2CD8",        # 0E, 14
        "Function_15_2D03",        # 0F, 15
        "Function_16_2D2E",        # 10, 16
        "Function_17_2D59",        # 11, 17
        "Function_18_2D76",        # 12, 18
        "Function_19_2DA5",        # 13, 19
        "Function_20_2DC8",        # 14, 20
        "Function_21_2DDA",        # 15, 21
        "Function_22_2DEC",        # 16, 22
        "Function_23_2DF8",        # 17, 23
        "Function_24_2E46",        # 18, 24
        "Function_25_2E94",        # 19, 25
        "Function_26_2EDD",        # 1A, 26
        "Function_27_2F26",        # 1B, 27
        "Function_28_2F7D",        # 1C, 28
        "Function_29_2F97",        # 1D, 29
        "Function_30_2FC6",        # 1E, 30
        "Function_31_35CF",        # 1F, 31
        "Function_32_3612",        # 20, 32
        "Function_33_3EED",        # 21, 33
        "Function_34_3F42",        # 22, 34
        "Function_35_3F68",        # 23, 35
        "Function_36_3F77",        # 24, 36
        "Function_37_3F86",        # 25, 37
        "Function_38_3F92",        # 26, 38
        "Function_39_3FA4",        # 27, 39
        "Function_40_3FDE",        # 28, 40
        "Function_41_4012",        # 29, 41
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A9")

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
            "#00301F好像已经完全昏迷了……\x02\x03",

            "#00306F看样子，并没有受到致命伤。\x01",
            "……哎呀呀，真是强韧得可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        "#00104F……我们是不是应该把他送到梅尔卡瓦上？\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00001F说的也对……\x01",
            "他可是袭击克洛斯贝尔的犯人，\x01",
            "要是能逮捕他，自然最好不过。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x103,
        (
            "#00203F……但实在太危险了。\x02\x03",

            "#00200F既然他没有生命之忧，\x01",
            "我觉得还是把他留在这里比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#00303F嗯，他应该不会在短时间之内苏醒，\x01",
            "不用担心他醒来之后追击我们。\x02\x03",

            "#00300F现在还是继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CE, 7)
    Jump("loc_7EE")

    label("loc_7A9")


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
            "好像已经完全昏迷了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7EE")

    TalkEnd(0x8)
    Return()

    # Function_2_5BE end

    def Function_3_7F2(): pass

    label("Function_3_7F2")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0009
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C7")
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

    label("loc_8C7")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_7F2 end

    def Function_4_8D6(): pass

    label("Function_4_8D6")

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

    def lambda_9EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9EA)

    def lambda_9FB():
        OP_95(0xFE, -230, 4000, 68330, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9FB)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A52)

    def lambda_A63():
        OP_95(0xFE, -1240, 4000, 68690, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A63)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_AC0)

    def lambda_AD1():
        OP_95(0xFE, 1150, 4000, 68650, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AD1)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B28():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_B28)

    def lambda_B39():
        OP_95(0xFE, -2400, 4000, 69350, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B39)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_8D6 end

    def Function_5_B5E(): pass

    label("Function_5_B5E")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event/evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BB7)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C02():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_C02)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C4D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_C4D)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_C98)
    StopSound(825, 1000, 40)
    Sleep(1000)
    NewScene("m9005", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_5_B5E end

    def Function_6_CB7(): pass

    label("Function_6_CB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CCF")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_CCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE7")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_CE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CFF")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_CFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D17")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_D17")

    Return()

    # Function_6_CB7 end

    def Function_7_D18(): pass

    label("Function_7_D18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D30")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_D30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D48")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_D48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D60")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_D60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D78")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_D78")

    Return()

    # Function_7_D18 end

    def Function_8_D79(): pass

    label("Function_8_D79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D91")
    LoadChrToIndex("chr/ch03156.itc", 0x29)

    label("loc_D91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DA9")
    LoadChrToIndex("chr/ch03253.itc", 0x29)

    label("loc_DA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC1")
    LoadChrToIndex("chr/ch0295F.itc", 0x29)

    label("loc_DC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DD9")
    LoadChrToIndex("chr/ch00953.itc", 0x29)

    label("loc_DD9")

    Return()

    # Function_8_D79 end

    def Function_9_DDA(): pass

    label("Function_9_DDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF2")
    LoadChrToIndex("chr/ch03156.itc", 0x2A)

    label("loc_DF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E0A")
    LoadChrToIndex("chr/ch03253.itc", 0x2A)

    label("loc_E0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E22")
    LoadChrToIndex("chr/ch0295F.itc", 0x2A)

    label("loc_E22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E3A")
    LoadChrToIndex("chr/ch00953.itc", 0x2A)

    label("loc_E3A")

    Return()

    # Function_9_DDA end

    def Function_10_E3B(): pass

    label("Function_10_E3B")

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

    def lambda_1138():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1138)
    Sleep(50)

    def lambda_1150():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1150)
    Sleep(50)

    def lambda_1168():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1168)
    Sleep(50)

    def lambda_1180():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1180)
    Sleep(50)

    def lambda_1198():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1198)
    Sleep(50)

    def lambda_11B0():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_11B0)
    OP_0D()
    Sleep(1600)
    StopBGM(0x7D0)
    OP_C9(0x0, 0x80000000)

    #N0010
    NpcTalk(
        0x9,
        "豪爽的声音",
        (
            "#3847V#11P#N#38A#30W哼哼，\x01",
            "已经突破前哨战了吗？\x02",
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
        "#00311F#12P叔叔……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#00013F#12P西格蒙德·奥兰多……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13DC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13A8")
    OP_FC(0xFFF4)
    Jump("loc_13AB")

    label("loc_13A8")

    OP_FC(0xC)

    label("loc_13AB")


    #C0013
    ChrTalk(
        0x10A,
        "#00601F#13P『赤色星座』的副团长吗……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1461")

    label("loc_13DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1438")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1406")
    OP_FC(0xFFF4)
    Jump("loc_1409")

    label("loc_1406")

    OP_FC(0xC)

    label("loc_1409")


    #C0014
    ChrTalk(
        0x109,
        "#10101F#13P『赤色星座』的副团长……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1461")

    label("loc_1438")


    #C0015
    ChrTalk(
        0x102,
        "#00101F#12P『赤色星座』的副团长……\x02",
    )

    CloseMessageWindow()

    label("loc_1461")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_148B")
    OP_FC(0xFFF4)
    Jump("loc_148E")

    label("loc_148B")

    OP_FC(0xC)

    label("loc_148E")


    #C0016
    ChrTalk(
        0x106,
        (
            "#10708F#13P『赤色战鬼』……\x01",
            "是最强的猎兵之一呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1563")

    label("loc_14CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_152F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14F4")
    OP_FC(0xFFF4)
    Jump("loc_14F7")

    label("loc_14F4")

    OP_FC(0xC)

    label("loc_14F7")


    #C0017
    ChrTalk(
        0x105,
        (
            "#10408F#13P『赤色战鬼』……\x01",
            "最强的猎兵之一。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1563")

    label("loc_152F")


    #C0018
    ChrTalk(
        0x103,
        (
            "#00208F#12P『赤色战鬼』……\x01",
            "是最强的猎兵之一。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1563")

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
            "哼哼……不错。\x02\x03",

            "能与我对抗的人，也就只有\x01",
            "『斗神』和『猎兵王』而已……\x02\x03",

            "在他们二人同归于尽之后，\x01",
            "我恐怕已经是最强的了。\x02\x03",

            "当然，也只是『现如今』而已。\x02",
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
            "#04503F#5P兰道夫……\x01",
            "你应该也已经察觉到了吧？\x02\x03",

            "克洛斯贝尔发生了如此状况，\x01",
            "埃雷波尼亚帝国也爆发了动乱，\x01",
            "整个大陆已经迎来了动荡的时代。\x02\x03",

            "#04501F我们这些猎兵在今后肯定会有\x01",
            "比以往更多的用武之地。\x02\x03",

            "恐怖分子的气焰日渐高涨，\x01",
            "『蛇』与『教会』的暗斗不断激化，\x01",
            "而游击士们恐怕也会更加活跃。\x02\x03",

            "#04504F我想你应该切身感觉到了。\x02\x03",

            "#04502F注定会结束的和平时代， \x01",
            "如今已经正式宣告完结了。\x02",
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
        "#00010F#12P……少胡扯了……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#00108F#12P可是……\x01",
            "他说的并没有错。\x02\x03",

            "#00106F由于克洛斯贝尔的事件……\x01",
            "还有帝国的内战和共和国的动乱，\x01",
            "整个大陆正在激烈动荡……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#00201F#12P难道说……\x01",
            "就算克洛斯贝尔不发生这起事件，\x01",
            "这一切依然是不可避免的吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19C2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1951")
    OP_FC(0xFFF4)
    Jump("loc_1954")

    label("loc_1951")

    OP_FC(0xC)

    label("loc_1954")


    #C0026
    ChrTalk(
        0x106,
        (
            "#10703F#13P……确实如此，导火索\x01",
            "已经在大陆各地点燃了。\x02\x03",

            "#10701F克洛斯贝尔事件也只是\x01",
            "一个契机罢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1AF9")

    label("loc_19C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A5B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19EC")
    OP_FC(0xFFF4)
    Jump("loc_19EF")

    label("loc_19EC")

    OP_FC(0xC)

    label("loc_19EF")


    #C0027
    ChrTalk(
        0x10A,
        (
            "#00606F#13P……的确，导火索\x01",
            "已在大陆每一个角落点燃。\x02\x03",

            "#00601F克洛斯贝尔事件也仅仅\x01",
            "是个契机而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_1AF9")

    label("loc_1A5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AF9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A85")
    OP_FC(0xFFF4)
    Jump("loc_1A88")

    label("loc_1A85")

    OP_FC(0xC)

    label("loc_1A88")


    #C0028
    ChrTalk(
        0x105,
        (
            "#10406F#13P……导火索已在大陆各地点燃，\x01",
            "这的确是不可否认的事实。\x02\x03",

            "#10401F克洛斯贝尔事件只是\x01",
            "一个契机而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1AF9")


    #C0029
    ChrTalk(
        0x104,
        (
            "#00306F嗯#12P……没错。\x02\x03",

            "#00311F而且我确实……\x01",
            "切身感受到了这一切……\x02\x03",

            "这是风暴将至的预感……\x01",
            "战争的气息正在逐渐逼近。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#00008F#12P……兰迪……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#04502F#5P呵呵，这正是你的猎兵之血\x01",
            "已经深入骨髓的证据……\x02\x03",

            "流淌在你体内的奥兰多一族的\x01",
            "战士之血，正是那所谓的『业障』。\x02\x03",

            "#04503F但是，兰道夫……\x01",
            "你为何至今都没有醒悟？\x02\x03",

            "#04501F你为何要伪装自己，\x01",
            "过着那种安稳的生活？\x02",
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
            "#04501F#5P这是最后的机会了。\x01",
            "兰道夫，继承『斗神』之位吧。\x02\x03",

            "至于有所不足的地方，\x01",
            "我会代替大哥，好好教导你的。\x02\x03",

            "#04504F等你成为『赤色星座』\x01",
            "名副其实的团长时……\x02\x03",

            "#04502F你就可以随心所欲地帮助你想帮助的人了。\x02",
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
            "#04504F#5P呵呵，当然了，\x01",
            "你就算想帮克洛斯贝尔也没有问题。\x02\x03",

            "#04502F无论此次事态如何发展，\x01",
            "克洛斯贝尔也都要面对\x01",
            "前途渺茫、多灾多难的未来。\x02\x03",

            "就算是为了你的同伴们，\x01",
            "你也应该做出正确的选择……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#00010F#12P……可恶……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#00107F#12P你……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        "#00211F#12P……也太会趁人之危了吧……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 17)
    WaitChrThread(0x104, 3)
    Sleep(200)

    def lambda_1ED5():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1ED5)
    WaitChrThread(0x104, 2)
    Sleep(300)

    #C0039
    ChrTalk(
        0x104,
        (
            "#00304F#12P#30W呵呵，原来如此……\x02\x03",

            "#00312F在这种时候还可以保持冷静，\x01",
            "用合理的言辞来说服我……\x02\x03",

            "真不愧是『赤色战鬼』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#04504F#5P这正是猎兵的生存之本……\x01",
            "我想你应该也很清楚。\x02\x03",

            "#04502F和平的时代已经去而不返，\x01",
            "现如今，你就算想继续抵抗，\x01",
            "也已没有『立足之地』了。\x02\x03",

            "既然如此，还有继续犹豫的必要吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        "#00303F#12P也许你说的没错……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 18)
    WaitChrThread(0x104, 3)
    Sleep(350)

    #C0042
    ChrTalk(
        0x104,
        "#00301F#12P可是，我的回答是ＮＯ。\x02",
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
        "#04505F#5P………哦………？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#00315F#12P看样子，你的不肖侄儿已经\x01",
            "彻底走上歪路了哦……\x02\x03",

            "#00304F他在动荡的时代中追求和平，\x01",
            "在充满欺瞒的世界里寻求正义……\x02\x03",

            "而且，他既不浪漫，也不抱有幻想，\x01",
            "只是和同伴们一起脚踏实地，\x01",
            "努力做着自己力所能及的事……\x02\x03",

            "#00302F并由此找到了\x01",
            "自己的『立足之地』。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#00214F#12P兰迪前辈……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2299")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_227C")
    OP_FC(0xFFF4)
    Jump("loc_227F")

    label("loc_227C")

    OP_FC(0xC)

    label("loc_227F")


    #C0046
    ChrTalk(
        0x109,
        "#10100F#13P前辈……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2299")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22E8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22C3")
    OP_FC(0xFFF4)
    Jump("loc_22C6")

    label("loc_22C3")

    OP_FC(0xC)

    label("loc_22C6")


    #C0047
    ChrTalk(
        0x10A,
        "#00604F#13P哼，大言不惭……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_22E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2346")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2312")
    OP_FC(0xFFF4)
    Jump("loc_2315")

    label("loc_2312")

    OP_FC(0xC)

    label("loc_2315")


    #C0048
    ChrTalk(
        0x105,
        (
            "#10402F#13P呵呵，似乎已经被\x01",
            "某人传染了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2346")


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
            "#00303F#12P以此为『立足之地』，\x01",
            "就可以向自己的『业障』发起抗争。\x02\x03",

            "#00308F我要与那令人怀念的战场生涯……\x01",
            "还有那个只能化身为修罗\x01",
            "活下去的自己彻底诀别。\x02",
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
        "#00301F#12P#30W这就是——我要做的了断。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#00002F#12P兰迪……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        "#00104F#12P……我们也会见证到底的。\x02",
    )

    CloseMessageWindow()
    StopSound(130, 3000, 30)
    StopSound(825, 3000, 60)
    Sleep(300)

    def lambda_24AA():
        OP_A6(0xFE, 0x1E, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_24AA)
    WaitChrThread(0x8, 2)
    Sleep(800)

    def lambda_24CA():
        OP_A6(0xFE, 0x28, 0x28, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_24CA)
    WaitChrThread(0x8, 2)
    Sleep(1000)

    #C0054
    ChrTalk(
        0x8,
        (
            "#04502F#5P#30W……哼哼………\x02\x03",

            "#04504F…………哈哈哈哈…………\x02\x03",

            "#04501F你的废话说完了吗？\x02",
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
        "#00010F#12P唔……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        "#00210F#12P#N……哇……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_266C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2642")
    OP_FC(0xFFF4)
    Jump("loc_2645")

    label("loc_2642")

    OP_FC(0xC)

    label("loc_2645")


    #C0057
    ChrTalk(
        0x106,
        "#10707F#13P好强的斗气……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2719")

    label("loc_266C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26C2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2696")
    OP_FC(0xFFF4)
    Jump("loc_2699")

    label("loc_2696")

    OP_FC(0xC)

    label("loc_2699")


    #C0058
    ChrTalk(
        0x105,
        "#10410F#13P好惊人的斗气……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2719")

    label("loc_26C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2719")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26EC")
    OP_FC(0xFFF4)
    Jump("loc_26EF")

    label("loc_26EC")

    OP_FC(0xC)

    label("loc_26EF")


    #C0059
    ChrTalk(
        0x10A,
        "#00610F#13P竟有如此强烈的斗气……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2719")


    #C0060
    ChrTalk(
        0x8,
        (
            "#04504F#5P呵呵……好吧。\x02\x03",

            "既然如此，我就认可你站在那脆弱的\x01",
            "『立足之地』上所发起的抗争……\x02\x03",

            "#04501F不过……你应该明白吧？\x02\x03",

            "既然你已经把话说得如此坚定了，\x01",
            "我也就不能再对你手下留情……\x02",
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
        "#00303F#2771V#12P#30W#20A嗯，求之不得。\x02",
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
            "#00301F#2772V#12P#30W#46A赌上老爸和你教给我的战技，\x01",
            "还有我的全部实力……\x02\x03",

            "#00307F#2773V#40A我要把你这个最强猎兵\x01",
            "打得落花流水！\x02",
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
            "#04504F#3850V#5P#30W#27A呵呵……有趣。\x02\x03",

            "#04512F#3851V#30W#50A既然如此，我就将你吞噬，\x01",
            "亲自继承『斗神』之位！\x02\x03",

            "#3852V#30W#50A这也是我唯一能献给\x01",
            "生下个废物儿子的大哥的祭礼！\x02",
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
            "#3848V#5P#40W#30A来，接招吧……\x02\x03",

            "#3849V#30W#67A尝尝我『赤色战鬼』这蹂躏过\x01",
            "无数战场的双战斧吧！\x02",
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
        "#00107F#6P#N#10A……要来了……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00007F#12P#37A开始迎击……！\x01",
            "全力掩护兰迪！\x02",
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

    # Function_10_E3B end

    def Function_11_2C57(): pass

    label("Function_11_2C57")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0xFA0, 0xD69C, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_2C57 end

    def Function_12_2C82(): pass

    label("Function_12_2C82")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0xFA0, 0xD1C4, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_2C82 end

    def Function_13_2CAD(): pass

    label("Function_13_2CAD")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0xFA0, 0xCC92, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_2CAD end

    def Function_14_2CD8(): pass

    label("Function_14_2CD8")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0xFA0, 0xCF4E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_14_2CD8 end

    def Function_15_2D03(): pass

    label("Function_15_2D03")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0xFA0, 0xD1BA, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_15_2D03 end

    def Function_16_2D2E(): pass

    label("Function_16_2D2E")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0xFA0, 0xD0F2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_16_2D2E end

    def Function_17_2D59(): pass

    label("Function_17_2D59")

    SetChrChipByIndex(0x104, 0x28)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x1000)
    SetChrSubChip(0xFE, 0x1)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(429)
    Return()

    # Function_17_2D59 end

    def Function_18_2D76(): pass

    label("Function_18_2D76")

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

    # Function_18_2D76 end

    def Function_19_2DA5(): pass

    label("Function_19_2DA5")

    SetChrChipByIndex(0x104, 0x28)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x1000)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(429)
    Return()

    # Function_19_2DA5 end

    def Function_20_2DC8(): pass

    label("Function_20_2DC8")

    Sleep(150)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_2DC8 end

    def Function_21_2DDA(): pass

    label("Function_21_2DDA")

    Sleep(300)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_2DDA end

    def Function_22_2DEC(): pass

    label("Function_22_2DEC")

    Sleep(450)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_2DEC end

    def Function_23_2DF8(): pass

    label("Function_23_2DF8")

    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E18")
    Sound(540, 0, 50, 0)
    Jump("loc_2E3D")

    label("loc_2E18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E3D")
    Sound(531, 0, 100, 0)

    label("loc_2E3D")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_2DF8 end

    def Function_24_2E46(): pass

    label("Function_24_2E46")

    Sleep(750)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E66")
    Sound(540, 0, 50, 0)
    Jump("loc_2E8B")

    label("loc_2E66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E8B")
    Sound(531, 0, 100, 0)

    label("loc_2E8B")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_2E46 end

    def Function_25_2E94(): pass

    label("Function_25_2E94")

    PlayEffect(0x0, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_25_2E94 end

    def Function_26_2EDD(): pass

    label("Function_26_2EDD")

    PlayEffect(0x0, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_26_2EDD end

    def Function_27_2F26(): pass

    label("Function_27_2F26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F7C")
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
    Jump("Function_27_2F26")

    label("loc_2F7C")

    Return()

    # Function_27_2F26 end

    def Function_28_2F7D(): pass

    label("Function_28_2F7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F96")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_28_2F7D")

    label("loc_2F96")

    Return()

    # Function_28_2F7D end

    def Function_29_2F97(): pass

    label("Function_29_2F97")

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

    # Function_29_2F97 end

    def Function_30_2FC6(): pass

    label("Function_30_2FC6")

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
            "#04510F#6P#40W………呵呵…………\x02\x03",

            "#04511F没想到，你竟能凭着那样的『立足之地』……\x01",
            "……奋战到如此地步……\x02\x03",

            "不过……\x01",
            "这也正是你如今的力量……\x02",
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
            "#00306F#12P#30W……是啊……\x01",
            "抱歉，我要将这种信念贯彻到底……\x02\x03",

            "#00301F不过，终究还是……\x01",
            "……很对不起你和老爸呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "#04510F#5P#40W呵呵……事到如今，何必再说这些……\x02\x03",

            "#04511F……而且，你不做个了断，\x01",
            "一直那样随波逐流地混日子，\x01",
            "才是最对不起我们的做法……\x02\x03",

            "虽然嘴上不曾提起……\x01",
            "……但大哥一直都很担心你……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        "#00308F#12P#30W……是吗……老爸他……\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_3377():
        OP_A6(0xFE, 0x0, 0x23, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3377)
    Sleep(800)

    #C0071
    ChrTalk(
        0x8,
        (
            "#04510F#5P#50W呵呵……不过……\x01",
            "如果看到你现在这种状态，\x01",
            "大哥应该也会略感欣慰吧……\x02\x03",

            "#60W……你这份顽强的信念，\x01",
            "是否能够……贯彻到底……\x02\x03",

            "就以你今后的人生……\x01",
            "……来证明……给我们看吧……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_3456():
        OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3456)
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

    # Function_30_2FC6 end

    def Function_31_35CF(): pass

    label("Function_31_35CF")

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

    # Function_31_35CF end

    def Function_32_3612(): pass

    label("Function_32_3612")

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
        "#00005F#11P#30W啊……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#00102F#12P#30W……我、我们……赢了吗……？\x02",
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
        "#00206F#12P#40W……呼……呼……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3973")
    OP_FC(0xFFF4)
    Jump("loc_3976")

    label("loc_3973")

    OP_FC(0xB)

    label("loc_3976")


    #C0075
    ChrTalk(
        0x109,
        (
            "#10106F#13P#40W真不敢相信……\x01",
            "……我们真的赢了吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3A76")

    label("loc_39B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A21")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39E2")
    OP_FC(0xFFF4)
    Jump("loc_39E5")

    label("loc_39E2")

    OP_FC(0xB)

    label("loc_39E5")


    #C0076
    ChrTalk(
        0x10A,
        (
            "#00606F#13P#40W太难以置信了……\x01",
            "我们竟然赢了……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3A76")

    label("loc_3A21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A76")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A4B")
    OP_FC(0xFFF4)
    Jump("loc_3A4E")

    label("loc_3A4B")

    OP_FC(0xB)

    label("loc_3A4E")


    #C0077
    ChrTalk(
        0x106,
        "#10706F#13P#40W……这是奇迹啊……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3A76")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AE5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AA0")
    OP_FC(0xFFF4)
    Jump("loc_3AA3")

    label("loc_3AA0")

    OP_FC(0xB)

    label("loc_3AA3")


    #C0078
    ChrTalk(
        0x105,
        (
            "#10402F#13P#40W这次实在要……\x01",
            "……感谢女神的保佑啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3B96")

    label("loc_3AE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B41")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B0F")
    OP_FC(0xFFF4)
    Jump("loc_3B12")

    label("loc_3B0F")

    OP_FC(0xB)

    label("loc_3B12")


    #C0079
    ChrTalk(
        0x106,
        "#10702F#13P#40W……简直是奇迹啊……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3B96")

    label("loc_3B41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B96")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B6B")
    OP_FC(0xFFF4)
    Jump("loc_3B6E")

    label("loc_3B6B")

    OP_FC(0xB)

    label("loc_3B6E")


    #C0080
    ChrTalk(
        0x10A,
        "#00602F#13P#40W……真是奇迹呢……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3B96")


    #C0081
    ChrTalk(
        0x104,
        "#00306F#11P#30W……是啊………\x02",
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
            "#00000F#12P#30W……不管嘴上怎么说……\x01",
            "他们依然是『家人』呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#00202F#12P#30W他好像一直都在……\x01",
            "担心着兰迪前辈呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#00306F#11P#30W是啊……我也明白的。\x02\x03",

            "#00303F我们家族的作风\x01",
            "一向都是如此强硬……\x02\x03",

            "#00300F……不管怎么说……\x01",
            "这样一来，总算是彻底做了个了断。\x02",
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
            "#00304F#5P这个『领域』好像也开放了呢。\x02\x03",

            "#00302F总之……\x01",
            "我们先返回入口吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        "#00104F#12P说的也是……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00002F#12P……辛苦你了，兰迪。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x103,
        "#00204F#12P辛苦了……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        "#00309F#5P哈哈，也辛苦你们了。\x02",
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

    # Function_32_3612 end

    def Function_33_3EED(): pass

    label("Function_33_3EED")


    def lambda_3EF2():
        OP_A6(0xFE, 0x0, 0x19, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3EF2)
    Sleep(700)
    OP_9B(0x0, 0xFE, 0x162, 0x320, 0x3E8, 0x0)
    OP_95(0xFE, -1200, 4100, 63800, 1000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_3EED end

    def Function_34_3F42(): pass

    label("Function_34_3F42")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, 650, 4100, 59850, 1500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(700)
    Return()

    # Function_34_3F42 end

    def Function_35_3F68(): pass

    label("Function_35_3F68")

    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_3F68 end

    def Function_36_3F77(): pass

    label("Function_36_3F77")

    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_3F77 end

    def Function_37_3F86(): pass

    label("Function_37_3F86")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_37_3F86 end

    def Function_38_3F92(): pass

    label("Function_38_3F92")

    Sleep(200)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_38_3F92 end

    def Function_39_3FA4(): pass

    label("Function_39_3FA4")

    Sleep(300)
    Sound(514, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x29)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FD9")
    SetChrSubChip(0xFE, 0x2)
    Jump("loc_3FDD")

    label("loc_3FD9")

    SetChrSubChip(0xFE, 0x0)

    label("loc_3FDD")

    Return()

    # Function_39_3FA4 end

    def Function_40_3FDE(): pass

    label("Function_40_3FDE")

    Sleep(400)
    SetChrChipByIndex(0xFE, 0x2A)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_400D")
    SetChrSubChip(0xFE, 0x2)
    Jump("loc_4011")

    label("loc_400D")

    SetChrSubChip(0xFE, 0x0)

    label("loc_4011")

    Return()

    # Function_40_3FDE end

    def Function_41_4012(): pass

    label("Function_41_4012")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x7)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_41_4012 end

    SaveToFile()

Try(main)
