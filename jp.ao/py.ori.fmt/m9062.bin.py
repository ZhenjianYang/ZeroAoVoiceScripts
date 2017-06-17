from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ヴァルド",               # 1
        "魔人ヴァルド",           # 2
        "台詞表示用ダミーキャラ", # 3
        "ヴァルドお供",           # 4
        "ヴァルドお供",           # 5
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
        "Function_3_8EA",          # 03, 3
        "Function_4_B6A",          # 04, 4
        "Function_5_CBD",          # 05, 5
        "Function_6_CFE",          # 06, 6
        "Function_7_D3B",          # 07, 7
        "Function_8_2F99",         # 08, 8
        "Function_9_2FC4",         # 09, 9
        "Function_10_2FEF",        # 0A, 10
        "Function_11_301A",        # 0B, 11
        "Function_12_3045",        # 0C, 12
        "Function_13_3070",        # 0D, 13
        "Function_14_309B",        # 0E, 14
        "Function_15_30B3",        # 0F, 15
        "Function_16_30CB",        # 10, 16
        "Function_17_30E3",        # 11, 17
        "Function_18_3101",        # 12, 18
        "Function_19_311F",        # 13, 19
        "Function_20_3158",        # 14, 20
        "Function_21_317E",        # 15, 21
        "Function_22_3194",        # 16, 22
        "Function_23_31AA",        # 17, 23
        "Function_24_31DB",        # 18, 24
        "Function_25_3224",        # 19, 25
        "Function_26_326D",        # 1A, 26
        "Function_27_328A",        # 1B, 27
        "Function_28_336B",        # 1C, 28
        "Function_29_48B2",        # 1D, 29
        "Function_30_48F1",        # 1E, 30
        "Function_31_4929",        # 1F, 31
        "Function_32_4974",        # 20, 32
        "Function_33_4990",        # 21, 33
        "Function_34_4A5C",        # 22, 34
        "Function_35_4AB5",        # 23, 35
        "Function_36_4B01",        # 24, 36
        "Function_37_4C3F",        # 25, 37
        "Function_38_4D5B",        # 26, 38
        "Function_39_4DB4",        # 27, 39
        "Function_40_4DC2",        # 28, 40
        "Function_41_4E82",        # 29, 41
        "Function_42_4F02",        # 2A, 42
        "Function_43_4F22",        # 2B, 43
        "Function_44_4F37",        # 2C, 44
        "Function_45_4F5F",        # 2D, 45
        "Function_46_4FEC",        # 2E, 46
        "Function_47_5079",        # 2F, 47
        "Function_48_5121",        # 30, 48
        "Function_49_5916",        # 31, 49
        "Function_50_592D",        # 32, 50
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_899")

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
            "#00001Fヴァルド……\x01",
            "完全に気絶してるみたいだな。\x02\x03",

            "#00004Fさっきは激励してくれたけど……\x01",
            "こいつも素直じゃないよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、そうね。\x01",
            "キーアちゃんの事も\x01",
            "気遣ってくれたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x103,
        (
            "#00200Fともあれ、メルカバまで\x01",
            "運んだほうがよさそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00306Fだが、コイツを運ぶのは、\x01",
            "俺でもちっと厳しいぜ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80B")

    #C0006
    ChrTalk(
        0x105,
        (
            "#10400Fまあ、後でアッバスを連れて来て\x01",
            "手伝ってもらうのがいいだろうね。\x02\x03",

            "#10403Fこの辺りはもう安全みたいだし、\x01",
            "彼の心配は要らないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00000Fああ、そうだな。\x01",
            "今は先に進むとしようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_891")

    label("loc_80B")


    #C0008
    ChrTalk(
        0x101,
        (
            "#00003F後でアッバスを連れて来て\x01",
            "手伝ってもらうのがいいだろう。\x02\x03",

            "#00000Fこの辺りはもう安全みたいだし……\x01",
            "今は先に進むとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_891")

    SetScenarioFlags(0x1CE, 5)
    Jump("loc_8E6")

    label("loc_899")


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
            "完全に気を失っているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8E6")

    TalkEnd(0x8)
    Return()

    # Function_2_5C5 end

    def Function_3_8EA(): pass

    label("Function_3_8EA")

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

    def lambda_9FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9FA)

    def lambda_A0B():
        OP_95(0xFE, -230, 0, 42280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A0B)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_A62():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A62)

    def lambda_A73():
        OP_95(0xFE, -1220, 0, 42680, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A73)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_AD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_AD0)

    def lambda_AE1():
        OP_95(0xFE, 840, 0, 42720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AE1)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_B38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_B38)

    def lambda_B49():
        OP_95(0xFE, -2270, 0, 43450, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B49)
    WaitChrThread(0x3, 1)
    Sleep(1000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_3_8EA end

    def Function_4_B6A(): pass

    label("Function_4_B6A")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_BC3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BC3)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C0E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_C0E)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C59():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_C59)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CA4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_CA4)
    Sleep(1000)
    NewScene("m9002", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_4_B6A end

    def Function_5_CBD(): pass

    label("Function_5_CBD")

    OP_CF(0x1, 0xF4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD5")
    OP_CF(0x1, 0xF5, 0x5)

    label("loc_CD5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE9")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_CE9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CFD")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_CFD")

    Return()

    # Function_5_CBD end

    def Function_6_CFE(): pass

    label("Function_6_CFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D12")
    OP_CF(0x1, 0xF5, 0x5)

    label("loc_D12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D26")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_D26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D3A")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_D3A")

    Return()

    # Function_6_CFE end

    def Function_7_D3B(): pass

    label("Function_7_D3B")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E0E")
    Call(0, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DDA")
    OP_CF(0x1, 0xF5, 0x5)
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_DDA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF4")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_DF4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E0E")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_E0E")

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

    def lambda_10D7():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_10D7)
    Sleep(50)

    def lambda_10EF():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10EF)
    Sleep(50)

    def lambda_1107():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1107)
    Sleep(50)

    def lambda_111F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_111F)
    Sleep(50)

    def lambda_1137():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1137)
    Sleep(50)

    def lambda_114F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_114F)
    OP_0D()
    Sleep(2400)
    StopBGM(0x7D0)
    OP_C9(0x0, 0x80000000)

    #N0011
    NpcTalk(
        0xA,
        "青年の声",
        (
            "#3580V#6P#30Wククク……\x01",
            "待ちくたびれちまったぜ。\x02",
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
        "#10401F#12P……ヴァルド。\x02",
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
            "ハッ、どうやらその姿が\x01",
            "てめぇの仕事着ってわけだ。\x02\x03",

            "《星杯騎士団》……\x01",
            "教会の極秘部隊だったか？\x02",
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
            "#10406F#12Pまあね。\x02\x03",

            "#10404F個人的にはテスタメンツの時の\x01",
            "スタイルの方が好きだけど。\x02\x03",

            "#10402Fああ、ホストの時に着ている\x01",
            "スーツなんかも悪くないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#01604F#5Pクク……\x01",
            "相変わらず悪趣味な野郎だぜ。\x02\x03",

            "#01602Fチャラけたバイトのやりすぎで\x01",
            "頭がマヒしてんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        (
            "#10403F#12P君に言われたくないね。\x02\x03",

            "#10401F“力”を手に入れても\x01",
            "その悪趣味な木刀は\x01",
            "手放していないみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#01603F#5P当たり前だ……\x01",
            "こいつは“象徴”だからな。\x02\x03",

            "#01601Fてめぇみたいな小器用なヤツには\x01",
            "込められない魂が宿ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x105,
        (
            "#10406F#12Pその割には旧市街のアパート、\x01",
            "キックでぶっ壊したそうじゃない？\x02\x03",

            "#10400F列車を脱線させたのだって\x01",
            "ただの力任せだったみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "#01602F#5Pクク、よく知ってやがるな。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x105,
        (
            "#10404F#12P知りたくもないのに\x01",
            "勝手に耳に飛び込んできてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        "#01604F#5Pククク……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x105,
        "#10402F#12Pフフフ……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17FE")

    #C0023
    ChrTalk(
        0x109,
        (
            "#10112F#12P（何だかんだ言って\x01",
            "  気が合ってるのかな……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A1")

    label("loc_17FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_184D")

    #C0024
    ChrTalk(
        0x10A,
        (
            "#00606F#12P（フン……\x01",
            "  不良同士、気が合うことだ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A1")

    label("loc_184D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18A1")

    #C0025
    ChrTalk(
        0x106,
        (
            "#10710F#12P（な、なんだかある意味、\x01",
            "  気が合ってるような……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A1")


    #C0026
    ChrTalk(
        0x103,
        "#00204F#12P#N（……ですね。）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0027
    ChrTalk(
        0x104,
        "#00300F#12P#N（ま、腐れ縁だろうからな。）\x02",
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

    def lambda_1927():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1927)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0029
    ChrTalk(
        0x101,
        (
            "#00006F#12P──ヴァルド。\x01",
            "改めて確認させてくれ。\x02\x03",

            "#00013F君にその“力”を……\x01",
            "いや《グノーシス》を与えたのは\x01",
            "マリアベルさんか？\x02",
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
            "#01605F#5Pああ、あの青いクスリか？\x02\x03",

            "#01604Fそういやそんな名前を\x01",
            "言ってやがった気もするな。\x02",
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
        "#00005F#12P紅色の方じゃないのか……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        (
            "#00205F#12P#N確か“魔人化”するのは\x01",
            "紅色の方だったはず……\x02\x03",

            "#00201Fそれなのに、どうして……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0034
    ChrTalk(
        0x8,
        (
            "#01602F#5Pクク、あのオンナ曰く、\x01",
            "俺は“合ってる”そうだぜ？\x02\x03",

            "ヤバイ方を使わなくても\x01",
            "最大限の“チカラ”を\x01",
            "引き出せる素質があるらしい。\x02\x03",

            "#01604Fま、そのあたりの理屈なんざ、\x01",
            "どうだっていいけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#00310F#12P#Nよくねえっての……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0036
    ChrTalk(
        0x102,
        (
            "#00101F#12P#Nまさかベルは、貴方以外にも\x01",
            "その薬を渡しているの……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0037
    ChrTalk(
        0x8,
        (
            "#01605F#5Pさて……\x01",
            "そんな様子は無かったがな。\x02\x03",

            "#01604Fクク、得体の知れねえアマだが\x01",
            "個人的には嫌いじゃねぇぜ？\x02\x03",

            "#01602F自分自身の欲望に\x01",
            "どこまでも忠実ってところはな。\x02",
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
            "#10406F#12Pそして君は\x01",
            "彼女の甘言に唆#2Rそそのか#されて……\x02\x03",

            "#10408F際限のない“力”を\x01",
            "求めるようになったわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#01604F#5Pクク……違うな。\x02\x03",

            "俺が“チカラ”に焦がれるのは\x01",
            "ガキの頃からだ……\x02",
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

    def lambda_1E94():
        OP_A6(0xFE, 0x0, 0xA, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E94)
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
            "#01608F#5P#30W呑んだくれのオヤジが死んでから\x01",
            "旧市街に一人放り出されて……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F98():
        OP_A6(0xFE, 0x0, 0x14, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F98)
    Sleep(500)

    #C0042
    ChrTalk(
        0x8,
        (
            "#01603F#5P#30Wケンカに明け暮れながら\x01",
            "バイパーとイグニスっていう\x01",
            "“聖域”を手に入れて……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2012():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2012)
    Sleep(500)

    #C0043
    ChrTalk(
        0x8,
        (
            "#01601F#30Wてめぇという喧嘩相手が現れて\x01",
            "熱くなっていた時ですら\x01",
            "奥底でくすぶり続けていた……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x1)
    Sound(817, 0, 60, 0)
    Sound(825, 2, 70, 0)
    Sound(832, 2, 100, 0)

    def lambda_20A5():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_20A5)
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    #C0044
    ChrTalk(
        0x101,
        "#00010F#12P#20Aくっ……\x02",
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
            "#01611F#5P#52A#4Sそれが俺の──\x01",
            "“チカラ”への渇望ってわけだ！\x02",
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

    def lambda_2472():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2472)
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
        "#00208F#12P#Nっ……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2693")

    #C0048
    ChrTalk(
        0x109,
        "#10110F#12P#Nくっ……あの時より！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2708")

    label("loc_2693")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26CC")

    #C0049
    ChrTalk(
        0x106,
        "#10712F#12P#N……“鬼”……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2708")

    label("loc_26CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2708")

    #C0050
    ChrTalk(
        0x10A,
        "#00610F#12P#Nこれが報告にあった……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2708")

    BeginChrThread(0x9, 3, 0, 20)
    Sleep(2000)
    SetMessageWindowPos(20, -1, -1, -1)

    #A0051
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40Wクク……\x01",
            "さあ、てめぇも見せてみろや……\x02",
        )
    )

    CloseMessageWindow()

    #A0052
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W“チカラ”への渇望……\x01",
            "……俺と同類である証を……！\x07\x00\x02",
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
            "#10406F#11P……いいだろう。\x02\x03",

            "#10408Fだが……\x01",
            "僕のそれは君と同じじゃない。\x02",
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
            "#40Wなにィ……\x07\x00\x02",
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
        "#00005F#5Pこれは……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29E3")

    #C0056
    ChrTalk(
        0x109,
        "#10105F#5P金色の……紋様……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A02")

    label("loc_29E3")


    #C0057
    ChrTalk(
        0x104,
        "#00305F#11P金の……紋様？\x02",
    )

    CloseMessageWindow()

    label("loc_2A02")


    #C0058
    ChrTalk(
        0x102,
        "#00101F#11P《聖痕#4Rスティグマ#》……！\x02",
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
            "#10403F#11P#30Wこの印が顕#2Rあらわ#れたせいで……\x01",
            "全てを手に入れ、全てを失くした。\x02\x03",

            "家族も、故郷も、未来も何もかも……\x02\x03",

            "#10408F“力”に絶望しつつ馴れ合いながら\x01",
            "偽りの生を生きていく……\x02\x03",

            "#10401Fそれが“僕”──ワジ・ヘミスフィアだ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 100, -1, -1)

    #A0060
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W……てめえ……\x07\x00\x02",
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
        "守護騎士ワジ",
        (
            "#10403F#2921V#6P#N#50A#30W──守護騎士#8Rド ミ ニ オ ン#第九位、\x01",
            "《蒼の聖典》ワジ・ヘミスフィア……\x02\x03",

            "#2922V#50Aこの金色の輝きをもって\x01",
            "君の“チカラ”を折らせてもらう。\x02\x03",

            "#10400F#2923V#20A──覚悟はいいかい？\x02",
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
            "#3581V#4S#43A#30Wクカカ、上等だよ……！\x07\x00\x02",
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
            "#3582V#4S#50W#55Aてめぇという贄#2Rニエ#を喰らうことで\x01",
            "俺の“チカラ”は完成する……！\x02",
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
            "#48A#3583V#5S#50Wさあ……\x01",
            "決着を付けるとしようぜえええッ！！\x07\x00\x02",
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

    # Function_7_D3B end

    def Function_8_2F99(): pass

    label("Function_8_2F99")

    OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x1)
    OP_96(0xFE, 0x0, 0x0, 0x7364, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_8_2F99 end

    def Function_9_2FC4(): pass

    label("Function_9_2FC4")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x460, 0x0, 0x6E28, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_9_2FC4 end

    def Function_10_2FEF(): pass

    label("Function_10_2FEF")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0x1A4, 0x0, 0x68F6, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_10_2FEF end

    def Function_11_301A(): pass

    label("Function_11_301A")

    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFFB0A, 0x0, 0x6BB2, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_301A end

    def Function_12_3045(): pass

    label("Function_12_3045")

    OP_9B(0x0, 0xFE, 0x0, 0x1996, 0xFA0, 0x1)
    OP_96(0xFE, 0xFFFFF614, 0x0, 0x6E1E, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_12_3045 end

    def Function_13_3070(): pass

    label("Function_13_3070")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0xFA0, 0x1)
    OP_96(0xFE, 0x9EC, 0x0, 0x6D56, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_13_3070 end

    def Function_14_309B(): pass

    label("Function_14_309B")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_309B end

    def Function_15_30B3(): pass

    label("Function_15_30B3")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_30B3 end

    def Function_16_30CB(): pass

    label("Function_16_30CB")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_30CB end

    def Function_17_30E3(): pass

    label("Function_17_30E3")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_17_30E3 end

    def Function_18_3101(): pass

    label("Function_18_3101")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_3101 end

    def Function_19_311F(): pass

    label("Function_19_311F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_313A")
    Sound(540, 0, 50, 0)
    Jump("loc_3140")

    label("loc_313A")

    Sound(531, 0, 100, 0)

    label("loc_3140")

    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_311F end

    def Function_20_3158(): pass

    label("Function_20_3158")

    Sound(892, 0, 100, 0)
    OP_71(0x0, 0x1B9, 0x1C2, 0x1, 0x0)
    OP_74(0x0, 0x5)
    OP_79(0x0)
    OP_71(0x0, 0x1C3, 0x1D6, 0x1, 0x20)
    Return()

    # Function_20_3158 end

    def Function_21_317E(): pass

    label("Function_21_317E")

    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    OP_71(0x0, 0xB, 0x32, 0x0, 0x20)
    Return()

    # Function_21_317E end

    def Function_22_3194(): pass

    label("Function_22_3194")

    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    OP_71(0x0, 0x3FC, 0x410, 0x0, 0x20)
    Return()

    # Function_22_3194 end

    def Function_23_31AA(): pass

    label("Function_23_31AA")

    OP_71(0x0, 0x408, 0x410, 0x0, 0x0)
    OP_79(0x0)
    Sound(892, 0, 80, 0)
    OP_71(0x0, 0x411, 0x41A, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0xB, 0x32, 0x0, 0x20)
    Return()

    # Function_23_31AA end

    def Function_24_31DB(): pass

    label("Function_24_31DB")

    PlayEffect(0x2, 0x5, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_24_31DB end

    def Function_25_3224(): pass

    label("Function_25_3224")

    PlayEffect(0x2, 0x6, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_25_3224 end

    def Function_26_326D(): pass

    label("Function_26_326D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3289")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_26_326D")

    label("loc_3289")

    Return()

    # Function_26_326D end

    def Function_27_328A(): pass

    label("Function_27_328A")

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

    # Function_27_328A end

    def Function_28_336B(): pass

    label("Function_28_336B")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3419")
    Call(0, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33E5")
    OP_CF(0x1, 0xF5, 0x5)
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_33E5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33FF")
    OP_CF(0x1, 0xF5, 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_33FF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3419")
    OP_CF(0x1, 0xF5, 0x9)
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_3419")

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
            "#3584V#4S#40Aオオオオオオオッ……！\x02",
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
            "#3585V#4S#65Aワジィィィ……てめぇぇえええッ！\x07\x00\x02",
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
        "#00010F#12Pくっ……！？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        "#00310F#12Pなんて野郎だ……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3860")

    #C0069
    ChrTalk(
        0x109,
        (
            "#10108F#12Pも、もうとっくに\x01",
            "体力が尽きているのに……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F5")

    label("loc_3860")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38A9")

    #C0070
    ChrTalk(
        0x106,
        (
            "#10708F#12Pもう既に体力は\x01",
            "尽きているのに……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F5")

    label("loc_38A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38F5")

    #C0071
    ChrTalk(
        0x10A,
        (
            "#00607F#12Pもうとっくに体力は\x01",
            "尽きているはずだぞ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38F5")

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
            "#10406F#12P本当ならあの雨の日……\x01",
            "こうしておくべきだった。\x02\x03",

            "#10408F全力と言いつつ……\x01",
            "君の身を案じてしまった。\x02",
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
            "#10403F#12P星杯の騎士でも、\x01",
            "《聖痕》の持ち主でもなく……\x02\x03",

            "テスタメンツのリーダー、\x01",
            "ワジ・ヘミスフィアとしての\x01",
            "最高の一撃をお見舞いするよ。\x02\x03",

            "#10402F君と初めて会った時みたいにね。\x02",
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
            "#40Wクク……カカカ……\x02",
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
            "#4S上等だ……！\x01",
            "返り討ちにしてやらあああッ！！\x07\x00\x02",
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
            "#40W#13A………ぁ……………\x07\x00\x02",
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
        "#10411F#2924V#5P#40Wおやすみ#15A#8Rグーテナハト#──\x02",
    )
    #Auto

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
            "#12A#5S#40Aオオオオオ……ッ！？\x07\x00\x02",
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
        "#10407F#6P#5S#40W#38Aおおおおッ……！\x02",
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
        "#00205F#6P#Nあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4134")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_410D")
    OP_FC(0x6)
    Jump("loc_4110")

    label("loc_410D")

    OP_FC(0xC)

    label("loc_4110")


    #C0082
    ChrTalk(
        0x109,
        "#10102F#13P#Nやった……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_41CF")

    label("loc_4134")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4183")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_415E")
    OP_FC(0x6)
    Jump("loc_4161")

    label("loc_415E")

    OP_FC(0xC)

    label("loc_4161")


    #C0083
    ChrTalk(
        0x106,
        "#10702F#13P#Nやった……\x02",
    )

    CloseMessageWindow()
    Jump("loc_41CF")

    label("loc_4183")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41CF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41AD")
    OP_FC(0x6)
    Jump("loc_41B0")

    label("loc_41AD")

    OP_FC(0xC)

    label("loc_41B0")


    #C0084
    ChrTalk(
        0x10A,
        "#00602F#13P#Nやったか……\x02",
    )

    CloseMessageWindow()

    label("loc_41CF")

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

    def lambda_42F2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_42F2)
    OP_75(0x0, 0x1, 0x5DC)
    Sleep(1500)
    ClearMapObjFlags(0x0, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_6F(0x79)
    Sleep(1000)

    #C0085
    ChrTalk(
        0x101,
        "#00002F#11P元の姿に……！\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        "#00106F#5Pよかった……\x02",
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

    def lambda_43CE():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_43CE)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_43EE():
        OP_A6(0xFE, 0x0, 0x50, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_43EE)
    WaitChrThread(0x8, 2)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 43)
    WaitChrThread(0x8, 3)

    #C0087
    ChrTalk(
        0x8,
        (
            "#01602F#5P#50W……クク……トドメまで\x01",
            "あの日と同じとは……\x02\x03",

            "ザマぁねえな……本当に……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x105,
        (
            "#10406F#11P#30Wまあ、魔人化した状態じゃ\x01",
            "あそこが限界ってことだろう。\x02\x03",

            "#10404F君の“力”を扱うセンスは\x01",
            "本物だと思うし……\x02\x03",

            "#10400Fちゃんと修行を積んだら\x01",
            "さらに強くなれると思うけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "#01608F#5P#50Wフン……言われなくても\x01",
            "……足掻いてやるぜ……\x02\x03",

            "ワジ……いつかテメエを\x01",
            "這いつくばらせるためによ……\x02\x03",

            "#01604Fだが……今回だけは……\x01",
            "……負けを認めて……やらぁ……\x02",
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
            "#01601F#5P#50Wそれと……\x01",
            "オイ……テメエら……\x02",
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
            "#01603F#5P#50Wテメエらがどうなろうと\x01",
            "知ったこっちゃ……ねぇが……\x02\x03",

            "あのガキが景気悪いツラしてんのは……\x01",
            "……気に喰わねぇ……\x02\x03",

            "#01601F#51Wせいぜい……気張るんだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#00205F#12Pあ……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00002F#12Pヴァルド……\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        (
            "#00304F#12Pハッ……\x01",
            "言われるまでもねぇっての。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        "#00102F#12P……ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        "#01604F#5P#60W………クク…………\x02",
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

    # Function_28_336B end

    def Function_29_48B2(): pass

    label("Function_29_48B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48F0")
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(2800)
    CancelBlur(500)
    Sleep(800)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(2750)
    CancelBlur(500)
    Sleep(800)
    Jump("Function_29_48B2")

    label("loc_48F0")

    Return()

    # Function_29_48B2 end

    def Function_30_48F1(): pass

    label("Function_30_48F1")

    PlayEffect(0x8, 0x5, 0x8, 0x1, 0, 50, 0, 0, 0, 0, 2000, 1000, 2000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_30_48F1 end

    def Function_31_4929(): pass

    label("Function_31_4929")


    def lambda_492E():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_492E)

    def lambda_4943():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4943)
    Sleep(350)
    Sound(196, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x0, 0x96, 0xBB8, 0x2BC)
    Return()

    # Function_31_4929 end

    def Function_32_4974(): pass

    label("Function_32_4974")

    OP_71(0x0, 0x3A3, 0x3A7, 0x1, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x3CA, 0x3DE, 0x1, 0x20)
    Return()

    # Function_32_4974 end

    def Function_33_4990(): pass

    label("Function_33_4990")

    Sleep(200)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x80, 0x0)

    def lambda_49BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_49BB)
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

    # Function_33_4990 end

    def Function_34_4A5C(): pass

    label("Function_34_4A5C")

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

    # Function_34_4A5C end

    def Function_35_4AB5(): pass

    label("Function_35_4AB5")

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

    # Function_35_4AB5 end

    def Function_36_4B01(): pass

    label("Function_36_4B01")

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

    label("loc_4B3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C20")
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
    Jump("loc_4B3E")

    label("loc_4C20")

    SetChrSubChip(0xFE, 0x5)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Return()

    # Function_36_4B01 end

    def Function_37_4C3F(): pass

    label("Function_37_4C3F")

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

    def lambda_4D25():
        OP_A6(0xFE, 0x96, 0x96, 0x96, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D25)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0x13)
    Sleep(150)
    OP_71(0x0, 0x21E, 0x226, 0x0, 0x0)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(150)
    Return()

    # Function_37_4C3F end

    def Function_38_4D5B(): pass

    label("Function_38_4D5B")

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

    # Function_38_4D5B end

    def Function_39_4DB4(): pass

    label("Function_39_4DB4")

    Sleep(1000)
    SetChrSubChip(0x105, 0x9)
    Fade(250)
    OP_0D()
    Return()

    # Function_39_4DB4 end

    def Function_40_4DC2(): pass

    label("Function_40_4DC2")

    SetChrSubChip(0xFE, 0xA)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4DD6():
        OP_9C(0xFE, 0x0, 0x708, 0x0, 0x73A, 0x514)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DD6)
    Sound(321, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x105, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    EndChrThread(0xFE, 0x1)
    OP_82(0x96, 0x96, 0xBB8, 0x3E8)
    Sound(815, 0, 100, 0)
    Sound(666, 0, 100, 0)
    Sleep(400)

    def lambda_4E57():
        OP_9C(0xFE, 0x0, 0xFFFFFB1E, 0x0, 0xFA, 0x4B0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E57)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0xB)
    Sleep(100)
    Return()

    # Function_40_4DC2 end

    def Function_41_4E82(): pass

    label("Function_41_4E82")

    BeginChrThread(0xFE, 3, 0, 42)

    def lambda_4E8D():
        OP_9C(0xFE, 0x0, 0x0, 0x9C4, 0xDAC, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4E8D)
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

    # Function_41_4E82 end

    def Function_42_4F02(): pass

    label("Function_42_4F02")

    OP_71(0x0, 0x244, 0x231, 0x1, 0x0)
    OP_D5(0xFE, 0xFFFEB3F8, 0x2BF20, 0x0, 0x9C4)
    Return()

    # Function_42_4F02 end

    def Function_43_4F22(): pass

    label("Function_43_4F22")

    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x9)
    Sleep(150)
    SetChrSubChip(0xFE, 0xA)
    Sleep(300)
    Return()

    # Function_43_4F22 end

    def Function_44_4F37(): pass

    label("Function_44_4F37")

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

    # Function_44_4F37 end

    def Function_45_4F5F(): pass

    label("Function_45_4F5F")

    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari04_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari05_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari99_add", 0x0, 0x1)
    Return()

    # Function_45_4F5F end

    def Function_46_4FEC(): pass

    label("Function_46_4FEC")

    SetMapObjFrame(0xFF, "hikari00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari04_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari05_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari99_add", 0x1, 0x1)
    Return()

    # Function_46_4FEC end

    def Function_47_5079(): pass

    label("Function_47_5079")

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

    # Function_47_5079 end

    def Function_48_5121(): pass

    label("Function_48_5121")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5142")
    Call(0, 5)

    label("loc_5142")

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
        "#10406F#11P#30Wふう……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00004F#11P……お疲れ、ワジ。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x103,
        "#00202F#12Pお疲れ様でした。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x105,
        (
            "#10404F#11P#30Wフフ……\x01",
            "さすがに疲れたかな。\x02",
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

    def lambda_54E7():
        OP_9B(0x0, 0xFE, 0x0, 0x190, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54E7)
    WaitChrThread(0x101, 1)

    #C0101
    ChrTalk(
        0x101,
        "#00005F#11Pお、おい！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_556F")

    #C0102
    ChrTalk(
        0x109,
        "#10111F#11Pワジ君……！？\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x102,
        "#00101F#12Pだ、大丈夫……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_55B1")

    label("loc_556F")


    #C0104
    ChrTalk(
        0x102,
        "#00105F#12Pワジ君……！？\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        "#00301F#12P大丈夫かよ……！？\x02",
    )

    CloseMessageWindow()

    label("loc_55B1")


    #C0106
    ChrTalk(
        0x105,
        (
            "#10406F#11P#40Wはぁ……《聖痕》の力を使うと\x01",
            "……どうしても反動があってね……\x02\x03",

            "#10408Fさすがにちょっと……\x01",
            "……飛ばしすぎたかな……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_568A")

    #C0107
    ChrTalk(
        0x109,
        (
            "#10106F#11Pまったく君は……\x01",
            "本当に無茶ばかりして……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5714")

    label("loc_568A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56C4")

    #C0108
    ChrTalk(
        0x10A,
        "#00606F#11Pフン、無茶をする……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5714")

    label("loc_56C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5714")

    #C0109
    ChrTalk(
        0x106,
        (
            "#10706F#11P……無理もありません。\x01",
            "あれほど巨大な相手に……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5714")


    #C0110
    ChrTalk(
        0x101,
        "#00013F#11P……大丈夫なのか？\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x105,
        (
            "#10404F#11P#30Wまあ、何とかね……\x02\x03",

            "#10400F──よっと。\x02",
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
            "#10403F#5P多分これで、この《領域》を\x01",
            "解放した事になるはずだ……\x02\x03",

            "#10401Fヴァルドは後で回収するとして\x01",
            "いったん門のところに戻ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#00000F#11P分かった……\x01",
            "戻ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        "#00302F#6Pほらよ、肩を貸すぜ。\x02",
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

    # Function_48_5121 end

    def Function_49_5916(): pass

    label("Function_49_5916")

    TurnDirection(0xFE, 0x105, 500)
    OP_9B(0x0, 0xFE, 0x161, 0x9C4, 0x5DC, 0x0)
    Return()

    # Function_49_5916 end

    def Function_50_592D(): pass

    label("Function_50_592D")

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

    # Function_50_592D end

    SaveToFile()

Try(main)
