from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9062.bin",                # FileName
        "m9062",                    # MapName
        "m9062",                    # Location
        0x00C1,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 193, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9062",                  # 0
        "瓦鲁多",                 # 1
        "魔人瓦鲁多",             # 2
        "显示台词用人物模型",     # 3
        "瓦鲁多带领的魔兽",       # 4
        "瓦鲁多带领的魔兽",       # 5
        "bm9049",                 # 6
    ))

    ATBonus("ATBonus_154", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_214", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_218", 3, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_21C", 13, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_220", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_224", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_228", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_22C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_230", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_200", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_204", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_208", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_20C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_210", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_234", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm9049", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88301.dat", "ms81401.dat", "ms81401.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_214", "MonsterBattlePostion_1F4", "ed7540", "ed7453", "ATBonus_154"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51112.itc",                   # 00
    ))

    DeclNpc(0,       0,       38500,   270,  389,  0x0, 4,   0,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(836, 0)                                        # 0

    ScpFunction((
        "Function_0_344",          # 00, 0
        "Function_1_3C0",          # 01, 1
        "Function_2_5C5",          # 02, 2
        "Function_3_856",          # 03, 3
        "Function_4_AD6",          # 04, 4
        "Function_5_C29",          # 05, 5
        "Function_6_C6A",          # 06, 6
        "Function_7_CA7",          # 07, 7
        "Function_8_2D7D",         # 08, 8
        "Function_9_2DA8",         # 09, 9
        "Function_10_2DD3",        # 0A, 10
        "Function_11_2DFE",        # 0B, 11
        "Function_12_2E29",        # 0C, 12
        "Function_13_2E54",        # 0D, 13
        "Function_14_2E7F",        # 0E, 14
        "Function_15_2E97",        # 0F, 15
        "Function_16_2EAF",        # 10, 16
        "Function_17_2EC7",        # 11, 17
        "Function_18_2EE5",        # 12, 18
        "Function_19_2F03",        # 13, 19
        "Function_20_2F3C",        # 14, 20
        "Function_21_2F62",        # 15, 21
        "Function_22_2F78",        # 16, 22
        "Function_23_2F8E",        # 17, 23
        "Function_24_2FBF",        # 18, 24
        "Function_25_3008",        # 19, 25
        "Function_26_3051",        # 1A, 26
        "Function_27_306E",        # 1B, 27
        "Function_28_314F",        # 1C, 28
        "Function_29_45FE",        # 1D, 29
        "Function_30_463D",        # 1E, 30
        "Function_31_4675",        # 1F, 31
        "Function_32_46C0",        # 20, 32
        "Function_33_46DC",        # 21, 33
        "Function_34_47A8",        # 22, 34
        "Function_35_4801",        # 23, 35
        "Function_36_484D",        # 24, 36
        "Function_37_498B",        # 25, 37
        "Function_38_4AA7",        # 26, 38
        "Function_39_4B00",        # 27, 39
        "Function_40_4B0E",        # 28, 40
        "Function_41_4BCE",        # 29, 41
        "Function_42_4C4E",        # 2A, 42
        "Function_43_4C6E",        # 2B, 43
        "Function_44_4C83",        # 2C, 44
        "Function_45_4CAB",        # 2D, 45
        "Function_46_4D38",        # 2E, 46
        "Function_47_4DC5",        # 2F, 47
        "Function_48_4E6D",        # 30, 48
        "Function_49_55F4",        # 31, 49
        "Function_50_560B",        # 32, 50
    ))


    def Function_0_344(): pass

    label("Function_0_344")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_355")
    Event(0, 3)

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_366")
    Event(0, 7)

    label("loc_366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_37D")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 28)
    Jump("loc_3BF")

    label("loc_37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_391")
    ClearScenarioFlags(0x22, 1)
    Event(0, 48)
    Jump("loc_3BF")

    label("loc_391")

    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, -200, 38500, 225)
    SetChrSubChip(0x8, 0x0)

    label("loc_3BF")

    Return()

    # Function_0_344 end

    def Function_1_3C0(): pass

    label("Function_1_3C0")

    OP_F0(0x1, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_3D9")

    OP_1B(0x0, 0x0, 0x4)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_43A")
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    Jump("loc_482")

    label("loc_43A")

    SetMapObjFrame(0xFF, "magi10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x1, 0x1)

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_51C")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari05_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari99_add", 0x0, 0x1)
    Jump("loc_5B8")

    label("loc_51C")

    OP_C3(0x0, 0x6, 0x3, 0x1E, 0x0, 0x1, -20000, -4000, 40000, 5000, 30000, 0)
    OP_C3(0x1, 0x6, 0x3, 0x1E, 0x0, 0x1, 20000, -4000, 40000, 5000, 30000, 0)
    OP_C3(0x2, 0x6, 0x3, 0x1E, 0x0, 0x1, 20000, -4000, 27000, 5000, 30000, 0)
    OP_C3(0x3, 0x6, 0x3, 0x1E, 0x0, 0x1, -20000, -4000, 27000, 5000, 30000, 0)
    LoadEffect(0x11, "eff\\\\trapdmg0.eff")

    label("loc_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_5C4")
    Call(0, 50)

    label("loc_5C4")

    Return()

    # Function_1_3C0 end

    def Function_2_5C5(): pass

    label("Function_2_5C5")

    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_811")

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
            "#00001F瓦鲁多……\x01",
            "看来他已经完全晕过去了。\x02\x03",

            "#00004F在晕倒之前还在鼓励我们……\x01",
            "这家伙可真是不坦率啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，是啊。\x01",
            "他好像也很\x01",
            "担心琪雅……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x103,
        (
            "#00200F总而言之，先把他\x01",
            "送到梅尔卡瓦吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00306F可是连我都很难\x01",
            "抬得动这家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79F")

    #C0006
    ChrTalk(
        0x105,
        (
            "#10400F算啦，稍后把阿巴斯带过来，\x01",
            "让他也帮帮忙吧。\x02\x03",

            "#10403F反正这一带已经安全了，\x01",
            "应该不必担心他的安危。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00000F嗯，没错，\x01",
            "现在还是继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_809")

    label("loc_79F")


    #C0008
    ChrTalk(
        0x101,
        (
            "#00003F稍后把阿巴斯带过来，\x01",
            "让他也帮帮忙吧。\x02\x03",

            "#00000F反正这一带已经安全了，\x01",
            "我们现在还是继续前进吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_809")

    SetScenarioFlags(0x1CE, 5)
    Jump("loc_852")

    label("loc_811")


    #C0009
    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "已经完全昏迷了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_852")

    TalkEnd(0x8)
    Return()

    # Function_2_5C5 end

    def Function_3_856(): pass

    label("Function_3_856")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(-790, 1500, 43820, 0)
    MoveCamera(55, 54, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12970, 0)
    SetChrPos(0x0, 0, 0, 45000, 180)
    SetChrPos(0x1, 0, 0, 45000, 180)
    SetChrPos(0x2, 0, 0, 45000, 180)
    SetChrPos(0x3, 0, 0, 45000, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_966():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_966)

    def lambda_977():
        OP_95(0xFE, -230, 0, 42280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_977)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_9CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_9CE)

    def lambda_9DF():
        OP_95(0xFE, -1220, 0, 42680, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9DF)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A3C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_A3C)

    def lambda_A4D():
        OP_95(0xFE, 840, 0, 42720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A4D)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AA4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_AA4)

    def lambda_AB5():
        OP_95(0xFE, -2270, 0, 43450, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_AB5)
    WaitChrThread(0x3, 1)
    Sleep(1000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_3_856 end

    def Function_4_AD6(): pass

    label("Function_4_AD6")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_B2F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B2F)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_B7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_B7A)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BC5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_BC5)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C10():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_C10)
    Sleep(1000)
    NewScene("m9002", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_4_AD6 end

    def Function_5_C29(): pass

    label("Function_5_C29")

    OP_CF(0x1, 0xF4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C41")
    OP_CF(0x1, 0xF5, 0x5)

    label("loc_C41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C55")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_C55")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C69")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_C69")

    Return()

    # Function_5_C29 end

    def Function_6_C6A(): pass

    label("Function_6_C6A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C7E")
    OP_CF(0x1, 0xF5, 0x5)

    label("loc_C7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C92")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_C92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA6")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_CA6")

    Return()

    # Function_6_C6A end

    def Function_7_CA7(): pass

    label("Function_7_CA7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01600.itp")
    LoadChrToIndex("chr/ch02150.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch03150.itc", 0x23)
    SoundLoad(2921)
    SoundLoad(2922)
    SoundLoad(2923)
    SoundLoad(3580)
    SoundLoad(3581)
    SoundLoad(3582)
    SoundLoad(3583)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D7A")
    Call(0, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D46")
    OP_CF(0x1, 0xF5, 0x5)
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_D46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D60")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_D60")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D7A")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_D7A")

    LoadChrToIndex("monster/ch81450.itc", 0x26)
    LoadChrToIndex("monster/ch81450.itc", 0x27)
    LoadChrToIndex("apl/ch51761.itc", 0x28)
    LoadEffect(0x0, "event/ev602_01.eff")
    LoadEffect(0x1, "event/ev602_02.eff")
    LoadEffect(0x2, "event/ev602_01.eff")
    LoadEffect(0x3, "event/ev17004.eff")
    LoadEffect(0x4, "event/ev17005.eff")
    LoadEffect(0x5, "event/ev14006.eff")
    SoundLoad(825)
    SoundLoad(832)
    SoundLoad(154)
    SetChrPos(0xF4, 0, 0, 11800, 0)
    SetChrPos(0x101, 900, 0, 11100, 0)
    SetChrPos(0x103, 200, 0, 10000, 0)
    SetChrPos(0x102, -900, 0, 10750, 0)
    SetChrPos(0x104, -600, 0, 9250, 0)
    SetChrPos(0xF5, 800, 0, 9000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1000)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 0, 0, 36500, 180)
    SetChrPos(0x9, 0, 0, 37000, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, 0, 1000, 28000, 0)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x4)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, -3000, 300, 38000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x4)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xC, 3000, 300, 38000, 180)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    BeginChrThread(0xB, 2, 0, 26)
    BeginChrThread(0xC, 2, 0, 26)
    OP_68(0, 1000, 15500, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_68(0, 1000, 18000, 4500)
    MoveCamera(0, 38, 0, 4500)
    OP_6E(600, 4500)
    SetCameraDistance(24000, 4500)
    Sound(154, 2, 80, 0)
    FadeToBright(1000, 0)

    def lambda_1043():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1043)
    Sleep(50)

    def lambda_105B():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_105B)
    Sleep(50)

    def lambda_1073():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1073)
    Sleep(50)

    def lambda_108B():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_108B)
    Sleep(50)

    def lambda_10A3():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10A3)
    Sleep(50)

    def lambda_10BB():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_10BB)
    OP_0D()
    Sleep(2400)
    StopBGM(0x7D0)
    OP_C9(0x0, 0x80000000)

    #N0011
    NpcTalk(
        0xA,
        "青年的声音",
        (
            "#3580V#6P#30W哼哼哼……\x01",
            "我已经等得不耐烦了。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDFC)
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
    PlayBGM("ed7561", 0)
    BeginChrThread(0x101, 0, 0, 9)
    BeginChrThread(0x102, 0, 0, 11)
    BeginChrThread(0x103, 0, 0, 10)
    BeginChrThread(0x104, 0, 0, 12)
    BeginChrThread(0xF4, 0, 0, 8)
    BeginChrThread(0xF5, 0, 0, 13)
    OP_68(0, -200, 32150, 4000)
    MoveCamera(0, 33, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(18390, 4000)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)
    StopSound(154, 4000, 80)
    Fade(500)
    OP_68(-140, 1300, 32580, 0)
    MoveCamera(44, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16140, 0)
    OP_0D()
    Sleep(300)

    #C0012
    ChrTalk(
        0x105,
        "#10401F#12P……瓦鲁多。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0013
    AnonymousTalk(
        0x8,
        (
            "哼，看你这身打扮，\x01",
            "应该是工作装吧？\x02\x03",

            "『星杯骑士团』……\x01",
            "教会的极秘部队，没错吧？\x02",
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

    #C0014
    ChrTalk(
        0x105,
        (
            "#10406F#12P不错。\x02\x03",

            "#10404F但就我个人而言，还是更加喜欢\x01",
            "圣书会服装的设计风格。\x02\x03",

            "#10402F哦，做男公关时穿的那套\x01",
            "西装也很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#01604F#5P哼哼……\x01",
            "你这家伙还是老样子，品位真低啊。\x02\x03",

            "#01602F难道是那种不三不四的工作干多了，\x01",
            "连脑子都出问题了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        (
            "#10403F#12P你可没资格说我啊。\x02\x03",

            "#10401F看看你自己，都已经\x01",
            "得到了现在的力量，却还是\x01",
            "不肯扔掉那把难看的木刀。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#01603F#5P那当然……\x01",
            "这把武器可是我的象征。\x02\x03",

            "#01601F里面寄宿着你这种爱耍小聪明的\x01",
            "家伙永远都无法拥有的灵魂。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x105,
        (
            "#10406F#12P但你当时可是用脚把\x01",
            "旧城区的那栋公寓踩烂的吧？\x02\x03",

            "#10400F让列车脱轨的那次也是，\x01",
            "完全都是依靠蛮力而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "#01602F#5P哼哼，你了解得还真清楚。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x105,
        (
            "#10404F#12P我本不想了解，\x01",
            "无奈流言太多了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        "#01604F#5P哼哼哼……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x105,
        "#10402F#12P呵呵呵……\x02",
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
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1700")

    #C0023
    ChrTalk(
        0x109,
        (
            "#10112F#12P（他们两人的关系\x01",
            "  其实挺不错吧……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179D")

    label("loc_1700")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_174F")

    #C0024
    ChrTalk(
        0x10A,
        (
            "#00606F#12P（哼……\x01",
            "  同为不良混混，倒是意气相投。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179D")

    label("loc_174F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_179D")

    #C0025
    ChrTalk(
        0x106,
        (
            "#10710F#12P（总、总觉得他们两人的\x01",
            "  关系还挺不错呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179D")


    #C0026
    ChrTalk(
        0x103,
        "#00204F#12P#N（……是啊。）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0027
    ChrTalk(
        0x104,
        "#00300F#12P#N（嗯，这就是所谓的孽缘吧。）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0028
    ChrTalk(
        0x101,
        "#00008F#12P………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_1821():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1821)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0029
    ChrTalk(
        0x101,
        (
            "#00006F#12P瓦鲁多，\x01",
            "我再问你一次。\x02\x03",

            "#00013F令你得到这种力量的……\x01",
            "不，把『真知』交给你的人……\x01",
            "是玛丽亚贝尔小姐吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        "#00108F#12P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0031
    ChrTalk(
        0x8,
        (
            "#01605F#5P哦，你是指那种蓝色药片吗？\x02\x03",

            "#01604F如此说来，她好像\x01",
            "提到过那个名字。\x02",
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

    #C0032
    ChrTalk(
        0x101,
        "#00005F#12P不是红色的吗……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        (
            "#00205F#12P#N能产生『魔人化』效果的\x01",
            "应该是红色药片啊……\x02\x03",

            "#00201F但你为何……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0034
    ChrTalk(
        0x8,
        (
            "#01602F#5P呵呵，据那女人所说，\x01",
            "我好像很适合这种药物。\x02\x03",

            "我具有即使不吞服\x01",
            "那种危险的红色药物，\x01",
            "也可以引发出力量的资质。\x02\x03",

            "#01604F算了，这方面的具体缘由，\x01",
            "倒也没必要追根究底。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#00310F#12P#N当然有必要啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0036
    ChrTalk(
        0x102,
        (
            "#00101F#12P#N难道除了你之外，\x01",
            "贝尔还把药给了其他人……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0037
    ChrTalk(
        0x8,
        (
            "#01605F#5P这个嘛……\x01",
            "应该没有。\x02\x03",

            "#01604F呵呵，虽然那个女人来历不明，\x01",
            "但我并不讨厌她。\x02\x03",

            "#01602F那种坚决忠于自己欲望的\x01",
            "性格更是让人欣赏。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        "#00106F#12P#N…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0039
    ChrTalk(
        0x105,
        (
            "#10406F#12P所以你就\x01",
            "接受了她的怂恿……\x02\x03",

            "#10408F开始寻求\x01",
            "无限强大的『力量』。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#01604F#5P哼哼……你错了。\x02\x03",

            "我从儿时开始，\x01",
            "就一直在渴求强大的『力量』……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetCameraDistance(15140, 20000)
    Sound(805, 0, 50, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x28)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(350)

    def lambda_1CFA():
        OP_A6(0xFE, 0x0, 0xA, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1CFA)
    Sleep(800)
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

    #C0041
    ChrTalk(
        0x8,
        (
            "#01608F#5P#30W自从我那酒鬼老爸死了之后，\x01",
            "我就一直在旧城区独自生活……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1DFA():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1DFA)
    Sleep(500)

    #C0042
    ChrTalk(
        0x8,
        (
            "#01603F#5P#30W在日复一日的打架斗殴之中，\x01",
            "我建立了剑蛇帮，并拥有了\x01",
            "那个名为鬼火的『圣域』……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E78():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E78)
    Sleep(500)

    #C0043
    ChrTalk(
        0x8,
        (
            "#01601F#30W在你这个劲敌出现之后，\x01",
            "我虽然感到热血沸腾，\x01",
            "但心底却仍然觉得不满足……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x1)
    Sound(817, 0, 60, 0)
    Sound(825, 2, 70, 0)
    Sound(832, 2, 100, 0)

    def lambda_1F01():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F01)
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    #C0044
    ChrTalk(
        0x101,
        "#00010F#12P#20A唔……\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        "#10410F#12P#20A…………………………………\x02",
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0x101, 0, 0, 14)
    Sleep(50)
    BeginChrThread(0xF4, 0, 0, 15)
    Sleep(50)
    BeginChrThread(0x102, 0, 0, 17)
    Sleep(50)
    BeginChrThread(0x103, 0, 0, 16)
    Sleep(50)
    BeginChrThread(0x104, 0, 0, 18)
    Sleep(50)
    BeginChrThread(0xF5, 0, 0, 19)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    Sleep(800)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #C0046
    ChrTalk(
        0x8,
        (
            "#01611F#5P#52A#4S这全都是因为──\x01",
            "我对力量的强烈渴求啊！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Fade(500)
    EndChrThread(0x8, 0x1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 950, 35470, 0)
    MoveCamera(33, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12320, 0)
    SetCameraDistance(10000, 3200)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 27)
    Sound(889, 0, 100, 0)
    OP_0D()
    Sleep(1400)
    OP_68(0, 1700, 35470, 1000)
    WaitChrThread(0x8, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(3551, 255, 100, 0)    #voice#Wald
    SetCameraDistance(10000, 1300)
    OP_82(0xC8, 0x64, 0xBB8, 0x3E8)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_68(0, 3900, 35500, 900)
    SetCameraDistance(8360, 900)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sound(817, 0, 100, 0)
    OP_82(0x64, 0xC8, 0xBB8, 0x3E8)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_82(0xC8, 0x64, 0xBB8, 0x3E8)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0xFF, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1200, 2000, 1200, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0xC8, 0xBB8, 0x3E8)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_82(0xC8, 0x64, 0xBB8, 0x3E8)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_78(0x0, 0x9)
    OP_93(0x9, 0xB4, 0x0)

    def lambda_22C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_22C6)
    ClearMapObjFlags(0x0, 0x4)
    OP_71(0x0, 0x65, 0x78, 0x0, 0x20)
    Sleep(200)
    OP_87(0x5, 0xFF, 0x0, "Null_vertic(1)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(300)
    CancelBlur(500)
    Sleep(300)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(700)
    StopSound(825, 1000, 70)
    StopSound(832, 1000, 100)
    OP_68(0, 2900, 33500, 0)
    MoveCamera(332, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13250, 0)
    MoveCamera(28, 11, 0, 4000)
    Fade(500)
    OP_71(0x0, 0x44C, 0x460, 0x0, 0x20)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_6F(0x79)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Fade(1000)
    SetChrPos(0x8, 0, 0, 35500, 180)
    SetChrPos(0x9, 0, 0, 35500, 180)
    OP_68(-970, 2200, 31180, 0)
    MoveCamera(40, 6, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12730, 0)
    SetCameraDistance(14730, 2000)
    BeginChrThread(0x9, 3, 0, 23)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0047
    ChrTalk(
        0x103,
        "#00208F#12P#N啊……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24E9")

    #C0048
    ChrTalk(
        0x109,
        "#10110F#12P#N唔……比那时候更强了！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2560")

    label("loc_24E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2522")

    #C0049
    ChrTalk(
        0x106,
        "#10712F#12P#N……『鬼』……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2560")

    label("loc_2522")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2560")

    #C0050
    ChrTalk(
        0x10A,
        "#00610F#12P#N这就是报告中所提到的……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2560")

    BeginChrThread(0x9, 3, 0, 20)
    Sleep(2000)
    SetMessageWindowPos(20, -1, -1, -1)

    #A0051
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W哼哼……\x01",
            "来吧，你也让我见识一下吧……\x02",
        )
    )

    CloseMessageWindow()

    #A0052
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W你对『力量』的渴求……\x01",
            "……与我身为同类的证据……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(0, 2100, 31770, 0)
    MoveCamera(138, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12500, 0)
    SetChrPos(0x8, 0, 0, 36500, 180)
    SetChrPos(0x9, -500, 0, 36500, 180)
    OP_0D()
    Sleep(300)

    #C0053
    ChrTalk(
        0x105,
        (
            "#10406F#11P……好吧。\x02\x03",

            "#10408F但是……\x01",
            "我与你并不相同。\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x1D7, 0x1E0, 0x1, 0x0)
    BeginChrThread(0x8, 3, 0, 21)
    Sleep(500)
    SetMessageWindowPos(50, 100, -1, -1)

    #A0054
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W什么……\x07\x00\x02",
        )
    )

    OP_79(0x0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(895, 0, 50, 0)
    PlayEffect(0x3, 0x1, 0x105, 0x5, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(832, 2, 100, 0)
    PlayEffect(0x4, 0x2, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    StopBGM(0xFA0)
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
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0055
    ChrTalk(
        0x101,
        "#00005F#5P这是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2823")

    #C0056
    ChrTalk(
        0x109,
        "#10105F#5P金色的……图纹……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2842")

    label("loc_2823")


    #C0057
    ChrTalk(
        0x104,
        "#00305F#11P金之……图纹？\x02",
    )

    CloseMessageWindow()

    label("loc_2842")


    #C0058
    ChrTalk(
        0x102,
        "#00101F#11P『圣痕』……！\x02",
    )

    CloseMessageWindow()
    Sound(895, 0, 70, 0)
    StopEffect(0x1, 0x2)
    PlayEffect(0x3, 0x3, 0x105, 0x5, 0, 0, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x2, 0x2)
    PlayEffect(0x4, 0x4, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7540", 0)
    SetCameraDistance(11000, 8000)
    Sleep(500)

    #C0059
    ChrTalk(
        0x105,
        (
            "#10403F#11P#30W这个印记的显现……\x01",
            "使我得到了一切，也失去了一切。\x02\x03",

            "家人、故乡、未来……以及所有的一切……\x02\x03",

            "#10408F我对这种『力量』感到绝望，同时也在\x01",
            "努力控制它，并过着充满伪装的生活……\x02\x03",

            "#10401F这就是我——瓦吉·赫米斯菲亚。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 100, -1, -1)

    #A0060
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W……你这家伙……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    SetChrPos(0x8, 0, 0, 36500, 180)
    SetChrPos(0x9, 0, 0, 36500, 180)
    OP_68(-50, 1800, 30300, 0)
    MoveCamera(359, 5, -1, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(13000, 30000)
    Sleep(300)
    Sound(895, 0, 100, 0)
    Sound(223, 0, 100, 0)
    StopEffect(0x3, 0x2)
    PlayEffect(0x3, 0x1, 0x105, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x4, 0x2)
    PlayEffect(0x4, 0x2, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #N0061
    NpcTalk(
        0x105,
        "守护骑士瓦吉",
        (
            "#10403F#2921V#6P#N#50A#30W守护骑士第九位──\x01",
            "『苍之圣典』瓦吉·赫米斯菲亚……\x02\x03",

            "#2922V#50A将以这金色的光辉\x01",
            "来折服你的『力量』。\x02\x03",

            "#10400F#2923V#20A做好心理准备了吗？\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    Sound(892, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x3F2, 0x3FC, 0x0, 0x0)
    BeginChrThread(0x8, 3, 0, 22)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0062
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3581V#4S#43A#30W哈哈哈，很好……！\x07\x00\x02",
        )
    )
    #Auto

    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    Sound(817, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 24)
    Sleep(100)
    BeginChrThread(0xC, 3, 0, 25)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0063
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3582V#4S#50W#55A将你这个祭品吞噬之后，\x01",
            "我的『力量』就将彻底完美……！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(532, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x83, 0x8C, 0x1, 0x0)
    Sleep(1000)

    #A0064
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#48A#3583V#5S#50W来吧……\x01",
            "就让我们做个了断吧！！\x07\x00\x02",
        )
    )
    #Auto

    Sleep(2000)
    OP_82(0xC8, 0xC8, 0xBB8, 0x9C4)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDFF)
    OP_C9(0x1, 0x80000000)
    Sound(893, 0, 100, 0)
    Sound(892, 0, 100, 0)
    Sound(833, 0, 50, 0)
    OP_71(0x0, 0x8D, 0x90, 0x1, 0x0)
    Sleep(50)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(450)
    CancelBlur(500)
    SetScenarioFlags(0x0, 0)
    Battle("BattleInfo_234", 0x30200011, 0x0, 0x100, 0x1D, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 28)
    OP_37()
    Return()

    # Function_7_CA7 end

    def Function_8_2D7D(): pass

    label("Function_8_2D7D")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0x7364, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_8_2D7D end

    def Function_9_2DA8(): pass

    label("Function_9_2DA8")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0x0, 0x6E28, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_9_2DA8 end

    def Function_10_2DD3(): pass

    label("Function_10_2DD3")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0x0, 0x68F6, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_10_2DD3 end

    def Function_11_2DFE(): pass

    label("Function_11_2DFE")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0x0, 0x6BB2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_2DFE end

    def Function_12_2E29(): pass

    label("Function_12_2E29")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0x0, 0x6E1E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_2E29 end

    def Function_13_2E54(): pass

    label("Function_13_2E54")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0x0, 0x6D56, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_2E54 end

    def Function_14_2E7F(): pass

    label("Function_14_2E7F")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_2E7F end

    def Function_15_2E97(): pass

    label("Function_15_2E97")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_2E97 end

    def Function_16_2EAF(): pass

    label("Function_16_2EAF")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_2EAF end

    def Function_17_2EC7(): pass

    label("Function_17_2EC7")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_2EC7 end

    def Function_18_2EE5(): pass

    label("Function_18_2EE5")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_2EE5 end

    def Function_19_2F03(): pass

    label("Function_19_2F03")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F1E")
    Sound(540, 0, 50, 0)
    Jump("loc_2F24")

    label("loc_2F1E")

    Sound(531, 0, 100, 0)

    label("loc_2F24")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_2F03 end

    def Function_20_2F3C(): pass

    label("Function_20_2F3C")

    Sound(892, 0, 100, 0)
    OP_71(0x0, 0x1B9, 0x1C2, 0x1, 0x0)
    OP_74(0x0, 0x5)
    OP_79(0x0)
    OP_71(0x0, 0x1C3, 0x1D6, 0x1, 0x20)
    Return()

    # Function_20_2F3C end

    def Function_21_2F62(): pass

    label("Function_21_2F62")

    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    OP_71(0x0, 0xB, 0x32, 0x0, 0x20)
    Return()

    # Function_21_2F62 end

    def Function_22_2F78(): pass

    label("Function_22_2F78")

    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    OP_71(0x0, 0x3FC, 0x410, 0x0, 0x20)
    Return()

    # Function_22_2F78 end

    def Function_23_2F8E(): pass

    label("Function_23_2F8E")

    OP_71(0x0, 0x408, 0x410, 0x0, 0x0)
    OP_79(0x0)
    Sound(892, 0, 80, 0)
    OP_71(0x0, 0x411, 0x41A, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0xB, 0x32, 0x0, 0x20)
    Return()

    # Function_23_2F8E end

    def Function_24_2FBF(): pass

    label("Function_24_2FBF")

    PlayEffect(0x2, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_24_2FBF end

    def Function_25_3008(): pass

    label("Function_25_3008")

    PlayEffect(0x2, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_25_3008 end

    def Function_26_3051(): pass

    label("Function_26_3051")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_306D")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_26_3051")

    label("loc_306D")

    Return()

    # Function_26_3051 end

    def Function_27_306E(): pass

    label("Function_27_306E")

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
    SetChrSubChip(0xFE, 0x6)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x9)
    Sleep(100)
    SetChrSubChip(0xFE, 0xA)
    Sleep(100)
    SetChrSubChip(0xFE, 0xB)
    Sleep(100)
    SetChrSubChip(0xFE, 0xC)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xF)
    Sleep(100)
    SetChrSubChip(0xFE, 0x10)
    Sleep(100)
    SetChrSubChip(0xFE, 0x11)
    Sleep(100)
    SetChrSubChip(0xFE, 0x12)
    Sleep(100)
    SetChrSubChip(0xFE, 0x13)
    Sleep(100)
    SetChrSubChip(0xFE, 0x14)
    Sleep(100)
    SetChrSubChip(0xFE, 0x15)
    Sleep(100)
    SetChrSubChip(0xFE, 0x16)
    Sleep(100)
    SetChrSubChip(0xFE, 0x17)
    Sleep(100)
    SetChrSubChip(0xFE, 0x18)
    Sleep(100)
    SetChrSubChip(0xFE, 0x19)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1C)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1F)
    Sleep(100)
    Return()

    # Function_27_306E end

    def Function_28_314F(): pass

    label("Function_28_314F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch03150.itc", 0x23)
    LoadChrToIndex("chr/ch03151.itc", 0x25)
    LoadChrToIndex("chr/ch03156.itc", 0x27)
    LoadChrToIndex("apl/ch51737.itc", 0x28)
    SoundLoad(832)
    SoundLoad(825)
    SoundLoad(3584)
    SoundLoad(3585)
    SoundLoad(2924)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31FD")
    Call(0, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31C9")
    OP_CF(0x1, 0xF5, 0x5)
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_31C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31E3")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_31E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31FD")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_31FD")

    LoadEffect(0x0, "event/ev17011.eff")
    LoadEffect(0x1, "event/ev17091.eff")
    LoadEffect(0x2, "battle/cr004000.eff")
    LoadEffect(0x3, "battle/cr004001.eff")
    LoadEffect(0x4, "eff/cutin30.eff")
    LoadEffect(0x5, "battle/cr004100.eff")
    LoadEffect(0x6, "event/ev17008.eff")
    LoadEffect(0x7, "event/ev17005.eff")
    LoadEffect(0x8, "event/ev17092.eff")
    LoadEffect(0x9, "event/ev17080.eff")
    LoadEffect(0xA, "event/ev17009.eff")
    SetChrPos(0x101, 1120, 0, 28600, 0)
    SetChrPos(0x102, -1270, 0, 27570, 0)
    SetChrPos(0x103, 420, 0, 26870, 0)
    SetChrPos(0x104, -2540, 0, 28190, 0)
    SetChrPos(0xF4, 0, 0, 29540, 0)
    SetChrPos(0xF5, 2540, 0, 27990, 0)
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
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x0, 0x4)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 0, 0, 36000, 180)
    SetChrPos(0x9, 0, 0, 36000, 180)
    OP_78(0x0, 0x9)
    OP_93(0x9, 0xB4, 0x0)
    SetChrFlags(0x9, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_71(0x0, 0x65, 0x78, 0x0, 0x20)
    OP_87(0xA, 0x3, 0x0, "Null_vertic(1)", 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_68(0, 3500, 35890, 0)
    MoveCamera(24, 7, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(8500, 3000)
    BeginChrThread(0x8, 0, 0, 30)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7543", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(833, 0, 60, 0)
    Sound(825, 2, 100, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x8, 1, 0, 29)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #A0065
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3584V#4S#40A呜噢噢噢噢噢噢……！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(800)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #A0066
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3585V#4S#65A瓦吉……你这混蛋！！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_68(-450, 1000, 30720, 0)
    MoveCamera(39, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14700, 0)
    Fade(500)
    CancelBlur(500)
    EndChrThread(0x8, 0x1)
    CancelBlur(500)
    OP_0D()

    #C0067
    ChrTalk(
        0x101,
        "#00010F#12P唔……！？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        "#00310F#12P好、好顽强的家伙……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3630")

    #C0069
    ChrTalk(
        0x109,
        (
            "#10108F#12P他、他的体力应该\x01",
            "早就耗尽了啊……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B7")

    label("loc_3630")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3677")

    #C0070
    ChrTalk(
        0x106,
        (
            "#10708F#12P他的体力应该\x01",
            "已经耗尽了才对……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B7")

    label("loc_3677")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36B7")

    #C0071
    ChrTalk(
        0x10A,
        (
            "#00607F#12P他的体力应该\x01",
            "已经耗尽了啊……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B7")

    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x105)
    Sleep(500)
    OP_68(340, 1000, 31940, 800)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    OP_9B(0x0, 0x105, 0x0, 0x21C, 0x320, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    OP_6F(0x79)

    #C0072
    ChrTalk(
        0x105,
        (
            "#10406F#12P其实，在下雨的那一天……\x01",
            "我就应该这么做了。\x02\x03",

            "#10408F那时，我虽然声称要拿出全力……\x01",
            "却还是心存顾虑，不想使你受伤。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(895, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x7, 0x2, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1300)
    SetMessageWindowPos(50, 50, -1, -1)

    #A0073
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "……！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0074
    ChrTalk(
        0x105,
        (
            "#10403F#12P现在的我，既不是星杯骑士，\x01",
            "也不是『圣痕』的宿主……\x02\x03",

            "就让我作为圣书会的首领——\x01",
            "瓦吉·赫米斯菲亚，\x01",
            "让你彻底领教最强的一击吧。\x02\x03",

            "#10402F就如第一次与你相遇时那样。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 2000, 31850, 0)
    MoveCamera(0, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(13500, 2000)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, 60, -1, -1)

    #A0075
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W哼哼……哈哈哈……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_6F(0x79)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    #A0076
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S很好……！\x01",
            "就把当时的账一并算清吧！！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EndChrThread(0x8, 0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x392, 0x3A2, 0x1, 0x0)
    Sound(532, 0, 100, 0)
    OP_68(0, 3400, 31000, 0)
    MoveCamera(352, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14750, 0)
    Fade(500)
    OP_68(70, 3000, 33350, 1200)
    MoveCamera(62, 39, 17, 1200)
    OP_6E(600, 1200)
    SetCameraDistance(11430, 1200)
    OP_0D()
    OP_6F(0x79)
    OP_79(0x0)
    OP_52(0x105, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x105, 0, 0, 33)
    BeginChrThread(0x9, 1, 0, 32)
    BeginChrThread(0x9, 0, 0, 31)
    Sound(893, 0, 100, 0)
    Sound(3549, 255, 100, 0)    #voice#Wald
    OP_68(70, 1800, 33350, 400)
    MoveCamera(15, 7, 17, 400)
    OP_6E(600, 400)
    SetCameraDistance(11430, 400)
    OP_6F(0x79)
    Sleep(250)
    OP_68(-410, 800, 32090, 750)
    MoveCamera(314, 17, 0, 750)
    OP_6E(600, 750)
    SetCameraDistance(13430, 750)
    OP_6F(0x79)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrFlags(0x105, 0x4)
    OP_52(0x105, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    SetMessageWindowPos(280, 40, -1, -1)

    #A0077
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#13A………啊……………\x07\x00\x02",
        )
    )
    #Auto

    SetChrChip(0x1, 0x105, 0x0, 0x0)
    StopEffect(0x5, 0x2)
    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0078
    ChrTalk(
        0x105,
        "#10411F#2924V#5P#40W晚安……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    OP_68(50, 2000, 31400, 200)
    MoveCamera(317, 11, 0, 200)
    OP_6E(600, 200)
    SetCameraDistance(9380, 200)
    BeginChrThread(0x105, 0, 0, 35)
    Sleep(200)
    EndChrThread(0x105, 0x0)
    Call(0, 45)
    SetChrPos(0x8, 0, 0, 35000, 180)
    SetChrPos(0x9, 0, 0, 35000, 180)
    SetChrPos(0x105, 0, 2200, 33150, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x105, 0, 0, 36)
    OP_68(0, 2900, 33850, 0)
    MoveCamera(310, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(7500, 0)
    Fade(500)
    OP_0D()
    Sound(2390, 255, 100, 0)    #voice#Lazy
    Sleep(2000)
    Sleep(500)
    #Sound(3551, 255, 100, 0)    #voice#Wald
    SetMessageWindowPos(200, 20, -1, -1)

    #A0079
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#12A#5S#40A呜噢噢噢噢噢……！？\x07\x00\x02",
        )
    )
    #Auto

    Sleep(2000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x105, 0)
    BeginChrThread(0x105, 0, 0, 37)
    Sleep(500)
    SetCameraDistance(10000, 1500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(500)
    CancelBlur(500)
    Sound(3093, 255, 100, 0)    #voice#Lazy
    Sleep(1000)
    OP_6F(0x79)
    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    BeginChrThread(0x105, 0, 0, 38)
    Sleep(500)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x3CA, 0x3DE, 0x1, 0x20)
    OP_68(1000, 1500, 33500, 0)
    MoveCamera(239, 31, 1, 0)
    OP_6E(600, 0)
    SetCameraDistance(8630, 0)
    Fade(500)
    OP_71(0x0, 0x231, 0x244, 0x1, 0x0)
    OP_0D()
    WaitChrThread(0x105, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 39)
    #Sound(2868, 255, 100, 0)    #voice#Lazy

    #C0080
    ChrTalk(
        0x105,
        "#10407F#6P#5S#40W#38A噢噢噢噢噢……！\x02",
    )
    #Auto

    OP_6F(0x79)
    CloseMessageWindow()
    StopSound(825, 1000, 100)
    BeginChrThread(0x105, 0, 0, 40)
    Sleep(400)
    OP_68(150, 1500, 34250, 700)
    MoveCamera(320, 16, 1, 700)
    OP_6E(600, 700)
    SetCameraDistance(14060, 700)
    Sleep(400)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(300)
    BeginChrThread(0x9, 0, 0, 41)
    Sleep(1700)
    CancelBlur(500)
    Sleep(100)
    StopEffect(0x3, 0x2)
    OP_6F(0x79)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x9, 0)
    Sound(3544, 255, 100, 0)    #voice#Wald
    SetMessageWindowPos(-1, -1, -1, -1)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    Sleep(700)
    Sleep(1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(350, 1300, 33250, 0)
    MoveCamera(7, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15380, 0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    ClearChrFlags(0xF4, 0x2)
    ClearChrFlags(0xF4, 0x1000)
    Fade(500)
    OP_0D()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(800)

    #C0081
    ChrTalk(
        0x103,
        "#00205F#6P#N啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EDE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EB9")
    OP_FC(0x6)
    Jump("loc_3EBC")

    label("loc_3EB9")

    OP_FC(0xC)

    label("loc_3EBC")


    #C0082
    ChrTalk(
        0x109,
        "#10102F#13P#N赢了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F75")

    label("loc_3EDE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F2B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F08")
    OP_FC(0x6)
    Jump("loc_3F0B")

    label("loc_3F08")

    OP_FC(0xC)

    label("loc_3F0B")


    #C0083
    ChrTalk(
        0x106,
        "#10702F#13P#N赢了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F75")

    label("loc_3F2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F75")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F55")
    OP_FC(0x6)
    Jump("loc_3F58")

    label("loc_3F55")

    OP_FC(0xC)

    label("loc_3F58")


    #C0084
    ChrTalk(
        0x10A,
        "#00602F#13P#N赢了吗……\x02",
    )

    CloseMessageWindow()

    label("loc_3F75")

    StopSound(832, 1000, 100)
    StopEffect(0x1, 0x2)
    Sleep(500)
    StopEffect(0x2, 0x2)
    Sleep(800)
    Fade(250)
    OP_0D()
    Sound(825, 2, 80, 0)
    Sound(843, 0, 100, 0)
    PlayEffect(0x1, 0x4, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(-760, 1300, 37770, 0)
    MoveCamera(0, 40, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(16500, 2000)
    Sleep(500)
    StopEffect(0x4, 0x2)
    Fade(1000)
    Sound(223, 0, 100, 0)
    Sound(817, 0, 100, 0)
    StopSound(825, 1000, 80)
    Call(0, 46)
    BeginChrThread(0x8, 0, 0, 47)
    SetChrPos(0x8, 0, -200, 38500, 225)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x4)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)

    def lambda_4098():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4098)
    OP_75(0x0, 0x1, 0x5DC)
    Sleep(1500)
    ClearMapObjFlags(0x0, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_6F(0x79)
    Sleep(1000)

    #C0085
    ChrTalk(
        0x101,
        "#00002F#11P变回原状了……！\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        "#00106F#5P太好了……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(230, 1200, 35730, 0)
    MoveCamera(38, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13640, 0)
    SetChrSubChip(0x8, 0x8)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    Sleep(50)
    WaitChrThread(0x8, 0)

    def lambda_4174():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4174)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_4194():
        OP_A6(0xFE, 0x0, 0x50, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4194)
    WaitChrThread(0x8, 2)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 43)
    WaitChrThread(0x8, 3)

    #C0087
    ChrTalk(
        0x8,
        (
            "#01602F#5P#50W……呵呵……没想到连\x01",
            "最后一击都和那天一模一样……\x02\x03",

            "真是……太丢人了……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x105,
        (
            "#10406F#11P#30W好啦，在魔人化状态下，\x01",
            "这已经是你的极限了。\x02\x03",

            "#10404F老实说，你的确拥有\x01",
            "掌控力量的天赋……\x02\x03",

            "#10400F今后如果努力修炼，\x01",
            "一定会变得更强的。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "#01608F#5P#50W哼……不用你说……\x01",
            "……我也一定会努力的……\x02\x03",

            "瓦吉……总有一天……\x01",
            "要把你打得趴在地上起不来……\x02\x03",

            "#01604F但……这次就……\x01",
            "……老老实实地……认输好了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_68(500, 800, 33060, 0)
    MoveCamera(30, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19350, 0)
    Fade(500)
    OP_0D()
    Sleep(300)

    #C0090
    ChrTalk(
        0x8,
        (
            "#01601F#5P#50W还有……\x01",
            "喂……你们几个……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0091
    ChrTalk(
        0x8,
        (
            "#01603F#5P#50W虽然你们的下场\x01",
            "如何都和我……没有关系……\x02\x03",

            "但那个小鬼总是一脸忧郁……\x01",
            "……我实在是看不下去……\x02\x03",

            "#01601F#51W你们就……尽量加油吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#00205F#12P啊……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00002F#12P瓦鲁多……\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        (
            "#00304F#12P呼……\x01",
            "这还用你说。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        "#00102F#12P……谢谢。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        "#01604F#5P#60W………唔唔…………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 44)
    WaitChrThread(0x8, 3)
    EndChrThread(0x8, 0x1)
    SetCameraDistance(25350, 4500)
    MoveCamera(30, 20, 0, 4500)
    Sleep(1000)
    Sound(202, 0, 100, 0)
    Sound(181, 0, 80, 0)
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 0, 50, 33620, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    Sleep(3300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x340)
    SetScenarioFlags(0x22, 0)
    NewScene("m9060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_314F end

    def Function_29_45FE(): pass

    label("Function_29_45FE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_463C")
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(2800)
    CancelBlur(500)
    Sleep(800)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(2750)
    CancelBlur(500)
    Sleep(800)
    Jump("Function_29_45FE")

    label("loc_463C")

    Return()

    # Function_29_45FE end

    def Function_30_463D(): pass

    label("Function_30_463D")

    PlayEffect(0x8, 0x5, 0x8, 0x1, 0, 50, 0, 0, 0, 0, 2000, 1000, 2000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_30_463D end

    def Function_31_4675(): pass

    label("Function_31_4675")


    def lambda_467A():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_467A)

    def lambda_468F():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_468F)
    Sleep(350)
    Sound(196, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x0, 0x96, 0xBB8, 0x2BC)
    Return()

    # Function_31_4675 end

    def Function_32_46C0(): pass

    label("Function_32_46C0")

    OP_71(0x0, 0x3A3, 0x3A7, 0x1, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x3CA, 0x3DE, 0x1, 0x20)
    Return()

    # Function_32_46C0 end

    def Function_33_46DC(): pass

    label("Function_33_46DC")

    Sleep(200)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x80, 0x0)

    def lambda_4707():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4707)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x6A4, 0x0, 0xFFFFFDDA, 0xFA, 0x44C)
    Sleep(200)
    StopEffect(0x2, 0x2)
    PlayEffect(0x6, 0x2, 0x105, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 3, 0, 34)
    Sound(844, 0, 100, 0)
    OP_9C(0xFE, 0xFFFFF95C, 0xFA, 0x64, 0x5DC, 0x3E8)
    ClearChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 3)
    Sound(326, 0, 70, 0)
    Return()

    # Function_33_46DC end

    def Function_34_47A8(): pass

    label("Function_34_47A8")

    Sleep(450)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(550)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_34_47A8 end

    def Function_35_4801(): pass

    label("Function_35_4801")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    Sound(251, 0, 100, 0)
    Sound(238, 0, 50, 0)
    OP_9C(0xFE, 0x4E2, 0x4E2, 0xFA0, 0x514, 0x9C4)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_35_4801 end

    def Function_36_484D(): pass

    label("Function_36_484D")

    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)

    label("loc_488A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_496C")
    SetChrSubChip(0xFE, 0x1)
    Sound(534, 0, 50, 0)
    Sound(541, 0, 100, 0)
    Sleep(50)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 200, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    OP_71(0x0, 0x21D, 0x226, 0x0, 0x0)
    Sound(260, 0, 60, 0)
    Sound(501, 0, 40, 0)
    SetChrSubChip(0xFE, 0x1)
    Sound(541, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 200, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    OP_71(0x0, 0x21D, 0x226, 0x0, 0x0)
    Jump("loc_488A")

    label("loc_496C")

    SetChrSubChip(0xFE, 0x5)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Return()

    # Function_36_484D end

    def Function_37_498B(): pass

    label("Function_37_498B")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(561, 0, 100, 0)
    Sound(881, 0, 80, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(1200)
    Sound(265, 0, 80, 0)
    Sound(501, 0, 50, 0)
    Sound(833, 0, 100, 0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_74(0x0, 0x5)
    OP_71(0x0, 0x21D, 0x21E, 0x0, 0x0)
    OP_82(0x0, 0x96, 0xBB8, 0x2BC)

    def lambda_4A71():
        OP_A6(0xFE, 0x96, 0x96, 0x96, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A71)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0x13)
    Sleep(150)
    OP_71(0x0, 0x21E, 0x226, 0x0, 0x0)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(150)
    Return()

    # Function_37_498B end

    def Function_38_4AA7(): pass

    label("Function_38_4AA7")

    ClearChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0x2BC, 0x0, 0xFFFFFE0C, 0x2EE, 0x3E8)
    Sound(326, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x8)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Return()

    # Function_38_4AA7 end

    def Function_39_4B00(): pass

    label("Function_39_4B00")

    Sleep(1000)
    SetChrSubChip(0x105, 0x9)
    Fade(250)
    OP_0D()
    Return()

    # Function_39_4B00 end

    def Function_40_4B0E(): pass

    label("Function_40_4B0E")

    SetChrSubChip(0xFE, 0xA)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4B22():
        OP_9C(0xFE, 0x0, 0x708, 0x0, 0x73A, 0x514)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B22)
    Sound(321, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x105, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    EndChrThread(0xFE, 0x1)
    OP_82(0x96, 0x96, 0xBB8, 0x3E8)
    Sound(815, 0, 100, 0)
    Sound(666, 0, 100, 0)
    Sleep(400)

    def lambda_4BA3():
        OP_9C(0xFE, 0x0, 0xFFFFFB1E, 0x0, 0xFA, 0x4B0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BA3)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0xB)
    Sleep(100)
    Return()

    # Function_40_4B0E end

    def Function_41_4BCE(): pass

    label("Function_41_4BCE")

    BeginChrThread(0xFE, 3, 0, 42)

    def lambda_4BD9():
        OP_9C(0xFE, 0x0, 0x0, 0x9C4, 0xDAC, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4BD9)
    OP_9C(0xFE, 0x0, 0x258, 0x3E8, 0x9C4, 0x12C)
    OP_82(0x96, 0x96, 0xBB8, 0x3E8)
    Sound(833, 0, 100, 0)
    Sound(627, 0, 100, 0)
    OP_93(0xFE, 0xE1, 0x0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x800)
    Return()

    # Function_41_4BCE end

    def Function_42_4C4E(): pass

    label("Function_42_4C4E")

    OP_71(0x0, 0x244, 0x231, 0x1, 0x0)
    OP_D5(0xFE, 0xFFFEB3F8, 0x2BF20, 0x0, 0x9C4)
    Return()

    # Function_42_4C4E end

    def Function_43_4C6E(): pass

    label("Function_43_4C6E")

    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x9)
    Sleep(150)
    SetChrSubChip(0xFE, 0xA)
    Sleep(300)
    Return()

    # Function_43_4C6E end

    def Function_44_4C83(): pass

    label("Function_44_4C83")

    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0xA)
    Sleep(100)
    Sound(862, 0, 20, 0)
    SetChrSubChip(0xFE, 0x9)
    Sleep(100)
    Sound(811, 0, 100, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(300)
    Return()

    # Function_44_4C83 end

    def Function_45_4CAB(): pass

    label("Function_45_4CAB")

    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari05_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari99_add", 0x0, 0x1)
    Return()

    # Function_45_4CAB end

    def Function_46_4D38(): pass

    label("Function_46_4D38")

    SetMapObjFrame(0xFF, "hikari00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari04_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari05_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari99_add", 0x1, 0x1)
    Return()

    # Function_46_4D38 end

    def Function_47_4DC5(): pass

    label("Function_47_4DC5")

    StopSound(154, 1000, 50)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari03_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari04_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari05_add", 0x0, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "hikari99_add", 0x0, 0x1)
    Sleep(200)
    Return()

    # Function_47_4DC5 end

    def Function_48_4E6D(): pass

    label("Function_48_4E6D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E8E")
    Call(0, 5)

    label("loc_4E8E")

    LoadChrToIndex("chr/ch03156.itc", 0x1F)
    LoadEffect(0x0, "event/ev17012.eff")
    SetChrPos(0x101, 120, 0, 30600, 354)
    SetChrPos(0x102, -2270, 0, 29570, 21)
    SetChrPos(0x103, -580, 0, 28870, 2)
    SetChrPos(0x104, -3540, 0, 30190, 35)
    SetChrPos(0xF4, -300, 0, 32650, 0)
    SetChrPos(0xF5, 1540, 0, 29990, 338)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, 0, -200, 38500, 225)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari05_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari99_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_04_add", 0x0, 0x1)
    OP_68(0, 50, 45000, 0)
    MoveCamera(39, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31500, 0)
    SetCameraDistance(29500, 2600)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Fade(500)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 45000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(935, 0, 80, 0)
    SetMapObjFrame(0xFF, "magi10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "magi11_add", 0x1, 0x1)
    Sleep(200)
    SetMapObjFrame(0xFF, "point_add", 0x1, 0x1)
    Sleep(600)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(-1720, 1100, 32000, 0)
    MoveCamera(39, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13330, 0)
    OP_0D()
    Sleep(300)

    #C0097
    ChrTalk(
        0x105,
        "#10406F#11P#30W呼……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00004F#11P……辛苦你了，瓦吉。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x103,
        "#00202F#12P辛苦你了。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x105,
        (
            "#10404F#11P#30W呵呵……\x01",
            "确实很累呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(811, 0, 50, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x105, 0x1F)
    SetChrSubChip(0x105, 0x0)
    Sleep(500)
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
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5225():
        OP_9B(0x0, 0xFE, 0x0, 0x190, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5225)
    WaitChrThread(0x101, 1)

    #C0101
    ChrTalk(
        0x101,
        "#00005F#11P喂、喂喂！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52AB")

    #C0102
    ChrTalk(
        0x109,
        "#10111F#11P瓦吉……！？\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x102,
        "#00101F#12P没、没事吧……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_52E9")

    label("loc_52AB")


    #C0104
    ChrTalk(
        0x102,
        "#00105F#12P瓦吉……！？\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        "#00301F#12P不要紧吧……！？\x02",
    )

    CloseMessageWindow()

    label("loc_52E9")


    #C0106
    ChrTalk(
        0x105,
        (
            "#10406F#11P#40W呼……一旦使用『圣痕』的力量，\x01",
            "就必然会产生这种副作用……\x02\x03",

            "#10408F我这次似乎……\x01",
            "……玩得太过火了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53AA")

    #C0107
    ChrTalk(
        0x109,
        (
            "#10106F#11P你可真是的……\x01",
            "总是这么乱来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542E")

    label("loc_53AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53E0")

    #C0108
    ChrTalk(
        0x10A,
        "#00606F#11P哼，真是乱来……\x02",
    )

    CloseMessageWindow()
    Jump("loc_542E")

    label("loc_53E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_542E")

    #C0109
    ChrTalk(
        0x106,
        (
            "#10706F#11P……这也是没办法的事啊，\x01",
            "毕竟对手那么巨大……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_542E")


    #C0110
    ChrTalk(
        0x101,
        "#00013F#11P……没事吧？\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x105,
        (
            "#10404F#11P#30W嗯，不要紧……\x02\x03",

            "#10400F好了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_68(-1720, 1100, 32000, 800)
    MoveCamera(44, 12, 0, 800)
    OP_6E(600, 800)
    SetCameraDistance(13330, 800)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_6F(0x79)
    TurnDirection(0x105, 0x101, 400)
    Sleep(150)

    #C0112
    ChrTalk(
        0x105,
        (
            "#10403F#5P如此一来，这个『领域』\x01",
            "应该就开放了……\x02\x03",

            "#10401F我们先返回入口吧，\x01",
            "稍后再回来接瓦鲁多。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#00000F#11P知道了……\x01",
            "我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        "#00302F#6P来，我扶你吧。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 0, 0, 49)
    SetCameraDistance(12600, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    EndChrThread(0x104, 0x0)
    SetChrPos(0x0, 0, 0, 32619, 0)
    SetChrSubChip(0x8, 0x4)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_37()
    SetScenarioFlags(0x1A7, 7)
    OP_29(0xB2, 0x1, 0x3)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7354", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x162), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_48_4E6D end

    def Function_49_55F4(): pass

    label("Function_49_55F4")

    TurnDirection(0xFE, 0x105, 500)
    OP_9B(0x0, 0xFE, 0x161, 0x9C4, 0x5DC, 0x0)
    Return()

    # Function_49_55F4 end

    def Function_50_560B(): pass

    label("Function_50_560B")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x1000)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_50_560B end

    SaveToFile()

Try(main)
