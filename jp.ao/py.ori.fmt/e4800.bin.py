from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4800.bin",                # FileName
        "e4800",                    # MapName
        "e4800",                    # Location
        0x00A0,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 160, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4800",                  # 0
        "レイモンド捜査官",       # 1
        "偽ブランド商",           # 2
        "共和国系テロリスト",     # 3
        "共和国系テロリスト",     # 4
        "共和国系テロリスト",     # 5
        "SE制御",                 # 6
        "be4800",                 # 7
        "be4800",                 # 8
    ))

    ATBonus("ATBonus_1CC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_28C", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_200", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_204", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 8, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 0, 0, 180)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_2CC", 0x00CA, 255, 6, 45, 3, 3, 30, 0, "be4800", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42500.dat", "ms42500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_1EC", "ed7507", "ed7453", "ATBonus_1CC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_310", 0x00CA, 255, 6, 45, 3, 3, 30, 0, "be4800", 0x00000000, 100, 0, 0, 0,
        (
            ("ms24100.dat", "ms42500.dat", "ms42500.dat", "ms42500.dat", 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_1EC", "ed7507", "ed7453", "ATBonus_1CC"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 14,  -26.5,                 0.15000000596046448,   -2.0,                  1406.25,               [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666667014360428,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.06666667014360428,   0.0,                   5.300000190734863,     -0.010000000707805157, 0.13333334028720856,   1.0])

    ChipFrameInfo(924, 0)                                        # 0

    ScpFunction((
        "Function_0_39C",          # 00, 0
        "Function_1_3D7",          # 01, 1
        "Function_2_447",          # 02, 2
        "Function_3_640",          # 03, 3
        "Function_4_695",          # 04, 4
        "Function_5_C41",          # 05, 5
        "Function_6_C85",          # 06, 6
        "Function_7_1B81",         # 07, 7
        "Function_8_1BB8",         # 08, 8
        "Function_9_1BEF",         # 09, 9
        "Function_10_1C26",        # 0A, 10
        "Function_11_1C5E",        # 0B, 11
        "Function_12_1C96",        # 0C, 12
        "Function_13_1CCE",        # 0D, 13
        "Function_14_1D06",        # 0E, 14
        "Function_15_35FA",        # 0F, 15
        "Function_16_362A",        # 10, 16
        "Function_17_365A",        # 11, 17
    ))


    def Function_0_39C(): pass

    label("Function_0_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3B0")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)
    Jump("loc_3D6")

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3C4")
    ClearScenarioFlags(0x22, 1)
    Event(0, 6)
    Jump("loc_3D6")

    label("loc_3C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_3D6")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    Event(0, 2)

    label("loc_3D6")

    Return()

    # Function_0_39C end

    def Function_1_3D7(): pass

    label("Function_1_3D7")

    OP_F0(0x1, 0x7D0)
    SetMapObjFrame(0xFF, "huta01b", 0x0, 0x1)
    SetMapObjFrame(0xFF, "huta02a", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_423")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_43A")
    OP_24(0x339)
    OP_24(0x1C3)
    ClearScenarioFlags(0x0, 0)
    Jump("loc_446")

    label("loc_43A")

    Sound(825, 1, 60, 0)
    Sound(451, 1, 80, 0)

    label("loc_446")

    Return()

    # Function_1_3D7 end

    def Function_2_447(): pass

    label("Function_2_447")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(451)
    SoundLoad(825)
    CreatePortrait(0, 128, 4, 640, 68, 0, 20, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis501.itp")
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xFF, 0xDC, 0xDC, 0x0, 0x0)
    OP_11(0xFF, 0xBD, 0xAC, 0x3C, 0x320, 0x0)
    OP_68(-14000, 0, 0, 0)
    MoveCamera(100, 42, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(140000, 0)
    BeginChrThread(0xD, 1, 0, 3)
    MoveCamera(107, 42, 0, 7000)
    SetCameraDistance(90000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_25(0x339, 0x3C)
    Fade(1000)
    OP_68(-18000, 1000, 0, 0)
    MoveCamera(132, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(76000, 0)
    OP_68(-18000, -1000, 0, 7600)
    SetCameraDistance(46000, 7600)
    OP_0D()
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    Fade(500)
    OP_68(75000, -4500, 0, 0)
    MoveCamera(270, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(55000, 0)
    OP_25(0x339, 0x64)
    Sound(455, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F40)
    OP_68(-75000, -4500, 0, 8000)
    MoveCamera(270, 25, 0, 8000)
    SetCameraDistance(55000, 8000)
    Sleep(6000)
    StopSound(451, 2000, 70)
    StopSound(825, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_447 end

    def Function_3_640(): pass

    label("Function_3_640")

    Sound(825, 2, 0, 0)
    Sound(451, 2, 0, 0)
    Sleep(200)
    OP_25(0x339, 0xA)
    OP_25(0x1C3, 0xA)
    Sleep(200)
    OP_25(0x339, 0x14)
    OP_25(0x1C3, 0x14)
    Sleep(200)
    OP_25(0x339, 0x1E)
    OP_25(0x1C3, 0x1E)
    Sleep(200)
    OP_25(0x339, 0x28)
    OP_25(0x1C3, 0x28)
    Sleep(200)
    OP_25(0x1C3, 0x32)
    Sleep(200)
    OP_25(0x1C3, 0x3C)
    Sleep(200)
    OP_25(0x1C3, 0x46)
    Sleep(200)
    OP_25(0x1C3, 0x50)
    Return()

    # Function_3_640 end

    def Function_4_695(): pass

    label("Function_4_695")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30200.itc", 0x1E)
    OP_68(-38500, 800, 570, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13160, 0)
    SetChrChipByIndex(0x8, 0x1E)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x101, -39650, 0, 30, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_71A")
    SetChrPos(0x102, -38330, 0, 1030, 225)
    Jump("loc_7AD")

    label("loc_71A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_740")
    SetChrPos(0x103, -38330, 0, 1030, 225)
    Jump("loc_7AD")

    label("loc_740")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_766")
    SetChrPos(0x104, -38330, 0, 1030, 225)
    Jump("loc_7AD")

    label("loc_766")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78C")
    SetChrPos(0x109, -38330, 0, 1030, 225)
    Jump("loc_7AD")

    label("loc_78C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AD")
    SetChrPos(0x105, -38330, 0, 1030, 225)

    label("loc_7AD")

    SetChrPos(0x8, -37780, 0, -710, 315)
    PlayBGM("ed7561", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x231), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x101,
        (
            "#00000Fレイモンドさん……\x01",
            "大丈夫ですか！？\x02\x03",

            "俺たちに任せてくれても\x01",
            "よかったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "い、いや～……\x01",
            "一応これ、僕が警部に\x01",
            "任された事件だしね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "君たちばっかりにいいカッコは\x01",
            "させられないかな～って。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90B")

    #C0004
    ChrTalk(
        0x102,
        (
            "#00100Fふふ……\x01",
            "ありがとうございます。\x02\x03",

            "ところで、\x01",
            "偽ブランド商は……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85")

    label("loc_90B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_963")

    #C0005
    ChrTalk(
        0x103,
        (
            "#00200Fふふ……\x01",
            "見直しました。\x02\x03",

            "それで、\x01",
            "偽ブランド商は……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85")

    label("loc_963")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9CB")

    #C0006
    ChrTalk(
        0x104,
        (
            "#00300Fはは……\x01",
            "見上げた根性だぜ。\x02\x03",

            "で、あのバーさんは\x01",
            "どこいきやがった……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85")

    label("loc_9CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2F")

    #C0007
    ChrTalk(
        0x109,
        (
            "#10100Fあはは……\x01",
            "ありがとうございます。\x02\x03",

            "ところで、\x01",
            "偽ブランド商は……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A85")

    label("loc_A2F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A85")

    #C0008
    ChrTalk(
        0x105,
        (
            "#10300Fフフ……\x01",
            "その意気やよし、だね。\x02\x03",

            "さて、あのマダムは……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A85")

    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(700)
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_93(0x101, 0xE1, 0x1F4)
    OP_68(-42630, 800, -350, 3000)
    MoveCamera(42, 27, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(14660, 3000)
    BeginChrThread(0x101, 1, 0, 5)
    Sleep(1500)
    OP_93(0x1, 0x10E, 0x1F4)
    OP_93(0x8, 0x10E, 0x1F4)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    Sleep(500)
    Fade(500)
    Sound(105, 0, 100, 0)
    SetMapObjFrame(0xFF, "huta01a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "huta01b", 0x1, 0x1)
    OP_0D()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00003F……多分、どこかの車両の屋根から\x01",
            "これを使って車内に逃げ込んだんだろう。\x02\x03",

            "#00000F後部車両から順に洗っていけば\x01",
            "追い詰められるはずだ。\x02\x03",

            "レイモンドさん、行きましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "あ、ああもちろん！\x01",
            "絶対捕まえてやるさ！\x02",
        )
    )

    CloseMessageWindow()
    StopSound(825, 1000, 60)
    StopSound(451, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0xA0, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 5)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_4_695 end

    def Function_5_C41(): pass

    label("Function_5_C41")

    OP_95(0xFE, -42770, -480, -2630, 2000, 0x0)
    OP_95(0xFE, -45480, -410, -2520, 2000, 0x0)
    OP_95(0xFE, -45940, -150, -1320, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_5_C41 end

    def Function_6_C85(): pass

    label("Function_6_C85")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch42550.itc", 0x1E)
    LoadChrToIndex("chr/ch42551.itc", 0x1F)
    LoadEffect(0x0, "battle/cr425100.eff")
    SoundLoad(860)
    SoundLoad(861)
    OP_68(26540, 660, -1340, 0)
    MoveCamera(36, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13440, 0)
    SetChrPos(0x101, 25610, -210, -1990, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D1E")
    SetChrPos(0x102, 26910, -800, -3100, 0)
    Jump("loc_DB1")

    label("loc_D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D44")
    SetChrPos(0x103, 26910, -800, -3100, 0)
    Jump("loc_DB1")

    label("loc_D44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D6A")
    SetChrPos(0x104, 26910, -800, -3100, 0)
    Jump("loc_DB1")

    label("loc_D6A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D90")
    SetChrPos(0x109, 26910, -800, -3100, 0)
    Jump("loc_DB1")

    label("loc_D90")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB1")
    SetChrPos(0x105, 26910, -800, -3100, 0)

    label("loc_DB1")

    SetChrPos(0x1A1, 26970, -140, -1380, 180)
    SetChrChipByIndex(0xA, 0x1F)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 7250, -230, 2260, 90)
    SetChrChipByIndex(0xB, 0x1F)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 7300, -210, -2020, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(21380, 780, -150, 3000)
    MoveCamera(36, 30, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(13440, 3000)
    BeginChrThread(0x101, 1, 0, 7)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E5C")
    BeginChrThread(0x102, 1, 0, 8)
    Jump("loc_EC3")

    label("loc_E5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E77")
    BeginChrThread(0x103, 1, 0, 8)
    Jump("loc_EC3")

    label("loc_E77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E92")
    BeginChrThread(0x104, 1, 0, 8)
    Jump("loc_EC3")

    label("loc_E92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAD")
    BeginChrThread(0x109, 1, 0, 8)
    Jump("loc_EC3")

    label("loc_EAD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EC3")
    BeginChrThread(0x105, 1, 0, 8)

    label("loc_EC3")

    Sleep(500)
    BeginChrThread(0x1A1, 1, 0, 9)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x1A1, 1)
    StopBGM(0x7D0)
    Sound(860, 2, 80, 0)
    Sound(861, 2, 80, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 17890, 0, 1310, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0x1, 0xFF, 0x0, 18360, 0, -950, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrFlags(0x0, 0x10)
    SetChrFlags(0x1, 0x10)
    SetChrFlags(0x1A1, 0x10)
    Sound(809, 0, 100, 0)

    def lambda_FBD():
        OP_9D(0xFE, 0x4FBA, 0x0, 0x32, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FBD)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_100A")

    def lambda_FED():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FED)
    Jump("loc_10CD")

    label("loc_100A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_103C")

    def lambda_101F():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_101F)
    Jump("loc_10CD")

    label("loc_103C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_106E")

    def lambda_1051():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1051)
    Jump("loc_10CD")

    label("loc_106E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10A0")

    def lambda_1083():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1083)
    Jump("loc_10CD")

    label("loc_10A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10CD")

    def lambda_10B5():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10B5)

    label("loc_10CD")

    Sleep(50)

    def lambda_10D5():
        OP_9D(0xFE, 0x5348, 0xFFFFFFBA, 0xFFFFFD12, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_10D5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x1A1, 1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopSound(860, 500, 70)
    StopSound(861, 500, 70)

    #C0011
    ChrTalk(
        0x1A1,
        "うわわわっ！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#00005Fな、なんだ……！？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7507", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(19560, 800, 0, 3000)
    MoveCamera(36, 30, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(13440, 3000)
    BeginChrThread(0xA, 1, 0, 10)
    BeginChrThread(0xB, 1, 0, 11)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)

    #C0013
    ChrTalk(
        0x101,
        (
            "#00001F通商会議を狙った\x01",
            "共和国のテロリスト……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xA,
        "どうやらクロスベル警察のようだな……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xA,
        "事情は知らないが、足止めさせてもらう！\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        "それ以上追跡を続けるなら命はないぞ！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12CC")

    #C0017
    ChrTalk(
        0x102,
        (
            "#00105F……ど、どうやら本物みたいね。\x02\x03",

            "#00106Fなんで偽ブランド商の\x01",
            "味方をしているかは\x01",
            "全然分からないけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14BD")

    label("loc_12CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1351")

    #C0018
    ChrTalk(
        0x103,
        (
            "#00201F……どうやら本物のようですね。\x02\x03",

            "#00206Fなぜ偽ブランド商の\x01",
            "味方をしているか\x01",
            "意味が分かりませんが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14BD")

    label("loc_1351")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13E9")

    #C0019
    ChrTalk(
        0x104,
        (
            "#00301Fチッ……あの装備、\x01",
            "どうやら間違いないようだぜ。\x02\x03",

            "#00306Fなんで偽ブランド商の\x01",
            "手下になっちまってるかは\x01",
            "分からねえが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14BD")

    label("loc_13E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_145E")

    #C0020
    ChrTalk(
        0x109,
        (
            "#10101Fあの装備……\x01",
            "間違いないみたいです！\x02\x03",

            "#10106Fで、でもなんで\x01",
            "偽ブランド商の味方を……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14BD")

    label("loc_145E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14BD")

    #C0021
    ChrTalk(
        0x105,
        (
            "#10305Fふうん……\x01",
            "間違いないみたいだね。\x02\x03",

            "#10309Fあのマダムの隠し玉かな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14BD")


    #C0022
    ChrTalk(
        0x101,
        (
            "#00003Fとにかく……\x01",
            "この程度の脅しに\x01",
            "屈するわけにはいかない。\x02\x03",

            "#00007F制圧するぞ、みんな！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x1A1,
        (
            "ひ、ひええ……\x01",
            "ちょっと待ってよ～！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_154B():
        OP_95(0xFE, 17910, 0, 70, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_154B)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_158F")

    def lambda_1575():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1575)
    Jump("loc_1646")

    label("loc_158F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15BE")

    def lambda_15A4():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15A4)
    Jump("loc_1646")

    label("loc_15BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15ED")

    def lambda_15D3():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15D3)
    Jump("loc_1646")

    label("loc_15ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_161C")

    def lambda_1602():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1602)
    Jump("loc_1646")

    label("loc_161C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1646")

    def lambda_1631():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1631)

    label("loc_1646")


    def lambda_164B():
        OP_95(0xFE, 19750, 0, -620, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_164B)
    Sleep(200)
    Battle("BattleInfo_2CC", 0x30200011, 0x0, 0x0, 0x25, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1A1, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    LoadChrToIndex("chr/ch42553.itc", 0x1E)
    LoadChrToIndex("chr/ch42500.itc", 0x1F)
    LoadChrToIndex("chr/ch42551.itc", 0x20)
    OP_68(19560, 800, 0, 0)
    MoveCamera(36, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13440, 0)
    SetChrPos(0x101, 19410, 0, 70, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1716")
    SetChrPos(0x102, 20650, 0, 990, 270)
    Jump("loc_17A9")

    label("loc_1716")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_173C")
    SetChrPos(0x103, 20650, 0, 990, 270)
    Jump("loc_17A9")

    label("loc_173C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1762")
    SetChrPos(0x104, 20650, 0, 990, 270)
    Jump("loc_17A9")

    label("loc_1762")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1788")
    SetChrPos(0x109, 20650, 0, 990, 270)
    Jump("loc_17A9")

    label("loc_1788")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17A9")
    SetChrPos(0x105, 20650, 0, 990, 270)

    label("loc_17A9")

    SetChrPos(0x1A1, 21250, 0, -620, 270)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 17110, -100, 980, 90)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 17280, 0, -680, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0024
    ChrTalk(
        0xA,
        "な、なんだこいつら……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xB,
        (
            "ちっ……あの金髪はまだしも、\x01",
            "あの２人は侮れんようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        (
            "ひとまず時間は稼げた、\x01",
            "いったん引くぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        "応！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    OP_0D()
    BeginChrThread(0xA, 1, 0, 12)
    BeginChrThread(0xB, 1, 0, 13)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    #C0028
    ChrTalk(
        0x1A1,
        "こ、怖かった……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#00010Fくっ……\x01",
            "また逃がしたか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1982")

    #C0030
    ChrTalk(
        0x102,
        (
            "#00103Fでも、さすがにこれ以上の\x01",
            "逃げ場はないはずよ。\x02\x03",

            "#00100F気を引き締めていきましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B47")

    label("loc_1982")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19F8")

    #C0031
    ChrTalk(
        0x103,
        (
            "#00203Fでも、さすがにこれ以上の\x01",
            "逃げ場はないはずです。\x02\x03",

            "#00200F気を引き締めていきましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B47")

    label("loc_19F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A62")

    #C0032
    ChrTalk(
        0x104,
        (
            "#00303Fさすがにこれ以上の\x01",
            "逃げ場はないはずだ。\x02\x03",

            "#00301F気を引き締めていこうぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B47")

    label("loc_1A62")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AD8")

    #C0033
    ChrTalk(
        0x109,
        (
            "#10103Fでも、さすがにこれ以上の\x01",
            "逃げ場はないはずです。\x02\x03",

            "#10101F気を引き締めていきましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B47")

    label("loc_1AD8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B47")

    #C0034
    ChrTalk(
        0x105,
        (
            "#10304Fいや、さすがにこれ以上の\x01",
            "逃げ場はないはずだ。\x02\x03",

            "#10300F気を引き締めていくとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B47")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetChrPos(0x0, 15470, -90, -890, 270)
    OP_37()
    OP_29(0x81, 0x1, 0x6)
    OP_29(0x81, 0x1, 0x7)
    SetScenarioFlags(0x173, 6)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_6_C85 end

    def Function_7_1B81(): pass

    label("Function_7_1B81")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 22420, -220, -2090, 4000, 0x0)
    OP_95(0xFE, 17910, 0, 70, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_7_1B81 end

    def Function_8_1BB8(): pass

    label("Function_8_1BB8")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 22670, -440, -2580, 4000, 0x0)
    OP_95(0xFE, 19750, 0, 990, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_8_1BB8 end

    def Function_9_1BEF(): pass

    label("Function_9_1BEF")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 22380, -230, -2140, 4000, 0x0)
    OP_95(0xFE, 19350, 0, -750, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_9_1BEF end

    def Function_10_1C26(): pass

    label("Function_10_1C26")

    OP_95(0xFE, 15020, -220, 2070, 4000, 0x0)
    OP_95(0xFE, 17110, -100, 980, 4000, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_10_1C26 end

    def Function_11_1C5E(): pass

    label("Function_11_1C5E")

    OP_95(0xFE, 15260, -240, -2280, 4000, 0x0)
    OP_95(0xFE, 17280, 0, -680, 4000, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_11_1C5E end

    def Function_12_1C96(): pass

    label("Function_12_1C96")

    OP_93(0xFE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 15020, -220, 2070, 5000, 0x0)
    OP_95(0xFE, 7250, -230, 2260, 5000, 0x0)
    Return()

    # Function_12_1C96 end

    def Function_13_1CCE(): pass

    label("Function_13_1CCE")

    OP_93(0xFE, 0xE1, 0x1F4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 15260, -240, -2280, 5000, 0x0)
    OP_95(0xFE, 7300, -210, -2020, 5000, 0x0)
    Return()

    # Function_13_1CCE end

    def Function_14_1D06(): pass

    label("Function_14_1D06")

    EventBegin(0x0)
    Fade(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch42500.itc", 0x1E)
    LoadChrToIndex("chr/ch42552.itc", 0x1F)
    LoadChrToIndex("chr/ch24100.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch02950.itc", 0x25)
    LoadChrToIndex("chr/ch03050.itc", 0x26)
    LoadChrToIndex("apl/ch51720.itc", 0x27)
    OP_68(-38140, 1300, -300, 0)
    MoveCamera(332, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18670, 0)
    SetChrPos(0x101, -23650, -380, -2500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DB9")
    SetChrPos(0x102, -22520, -370, -2480, 270)
    Jump("loc_1E4C")

    label("loc_1DB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DDF")
    SetChrPos(0x103, -22520, -370, -2480, 270)
    Jump("loc_1E4C")

    label("loc_1DDF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E05")
    SetChrPos(0x104, -22520, -370, -2480, 270)
    Jump("loc_1E4C")

    label("loc_1E05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E2B")
    SetChrPos(0x109, -22520, -370, -2480, 270)
    Jump("loc_1E4C")

    label("loc_1E2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E4C")
    SetChrPos(0x105, -22520, -370, -2480, 270)

    label("loc_1E4C")

    SetChrPos(0x1A1, -21360, -370, -2470, 270)
    SetChrChipByIndex(0xA, 0x1E)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -39510, -10, -30, 270)
    SetChrChipByIndex(0xB, 0x1E)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -40270, -10, -1410, 315)
    SetChrChipByIndex(0xC, 0x1E)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -40300, -10, 1210, 225)
    SetChrChipByIndex(0x9, 0x20)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -41450, -10, -50, 90)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 15)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F07")
    BeginChrThread(0x102, 1, 0, 16)
    Jump("loc_1F6E")

    label("loc_1F07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F22")
    BeginChrThread(0x103, 1, 0, 16)
    Jump("loc_1F6E")

    label("loc_1F22")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F3D")
    BeginChrThread(0x104, 1, 0, 16)
    Jump("loc_1F6E")

    label("loc_1F3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F58")
    BeginChrThread(0x109, 1, 0, 16)
    Jump("loc_1F6E")

    label("loc_1F58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F6E")
    BeginChrThread(0x105, 1, 0, 16)

    label("loc_1F6E")

    Sleep(200)
    BeginChrThread(0x1A1, 1, 0, 17)
    WaitChrThread(0x1A1, 1)

    #C0035
    ChrTalk(
        0x101,
        "#00007F待てッ！！\x02",
    )

    CloseMessageWindow()

    def lambda_1F97():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1F97)
    Sleep(100)

    def lambda_1FA7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1FA7)
    Sleep(100)

    def lambda_1FB7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1FB7)
    WaitChrThread(0xC, 1)
    Fade(500)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    OP_0D()

    #C0036
    ChrTalk(
        0x9,
        (
            "#5Pフン……どこまでも\x01",
            "しつこいヤツらだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#5Pま、この子たちは\x01",
            "思わぬ拾い物だったけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00003F……今度こそ、\x01",
            "本当に追い詰めましたよ。\x02\x03",

            "#00001Fこれ以上逃げるのは\x01",
            "絶対に不可能のはずです。\x01",
            "あきらめて投降してください。\x02\x03",

            "もちろん、そこにいる\x01",
            "テロリストのあなた達もです。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x1A1,
        "そ、そうだ～、投降しろ～！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xA,
        "う……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        "確かに……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        "このあたりが限界か……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "#5Pやれやれ……\x01",
            "近頃の若いもんは、\x01",
            "根性が足りないねえ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22B4")

    #C0045
    ChrTalk(
        0x102,
        (
            "#00105Fどういうことですか……？\x02\x03",

            "#00106Fまさか、まだ\x01",
            "逃げられるつもりなんじゃ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_244B")

    label("loc_22B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_231E")

    #C0046
    ChrTalk(
        0x103,
        (
            "#00205Fどういうことです……？\x02\x03",

            "#00203Fまさか、まだ\x01",
            "逃げられるつもりですか……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_244B")

    label("loc_231E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2384")

    #C0047
    ChrTalk(
        0x104,
        (
            "#00305Fどういうことだ……？\x02\x03",

            "#00306Fまさか、まだ\x01",
            "逃げるつもりだっつーのか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_244B")

    label("loc_2384")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23F2")

    #C0048
    ChrTalk(
        0x109,
        (
            "#10105Fど、どういうことですか？\x02\x03",

            "#10101Fまさか、まだ\x01",
            "逃げられるつもりなんじゃ……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_244B")

    label("loc_23F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_244B")

    #C0049
    ChrTalk(
        0x105,
        (
            "#10305Fふうん……？\x02\x03",

            "#10302Fまだ逃げられるつもりで\x01",
            "いるようだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_244B")


    #C0050
    ChrTalk(
        0x9,
        "#5Pつもり……？　ハッ！！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "#5Pまだそんな甘っちょろいことを\x01",
            "言ってるとはねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "#5P……列車がアルタイル市にさえ\x01",
            "ついちまえばこっちのもんさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "#5Pなんせ、共和国なら\x01",
            "こちらの方が土地勘はあるからねえ！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "#5P列車が止まった瞬間、\x01",
            "トンズラこかせてもらうよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0055
    ChrTalk(
        0x101,
        (
            "#00006Fト、トンズラって……\x02\x03",

            "#00011Fこの期に及んで、\x01",
            "まだ走って逃げるつもり\x01",
            "なんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "ハッ……！\x01",
            "いいかい、よくお聞き！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0057
    ChrTalk(
        0x9,
        (
            "#5P#5Sこの大陸の続く限り……\x01",
            "全てはアタシの逃げ道たりえるのさ！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0058
    ChrTalk(
        0x9,
        (
            "#5P#5Sあんたらがアタシに\x01",
            "足で追いつけない限り……\x01",
            "アタシが捕まることもない！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0059
    ChrTalk(
        0x9,
        (
            "#5P#5S分かったかい、\x01",
            "このトンチキどもが！#3S\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        "おおお……！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xC,
        "ついていきますぜ！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x101,
        (
            "#00006Fう、うーん……\x01",
            "めちゃくちゃな根拠だけど……\x01",
            "本当に逃げ切れるつもりらしいな。\x02\x03",

            "このお婆さんなら\x01",
            "本当にやりそうで怖いけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x1A1,
        (
            "こ、こっちだって……\x01",
            "逃がすわけにはいかないよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x1A1,
        (
            "なんたって、警部に任された\x01",
            "大事な任務なんだからさ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28BD")

    #C0065
    ChrTalk(
        0x102,
        "#00105Fレイモンドさん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_29B5")

    label("loc_28BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2902")

    #C0066
    ChrTalk(
        0x103,
        (
            "#00205Fレイモンドさん……\x01",
            "……そうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B5")

    label("loc_2902")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2938")

    #C0067
    ChrTalk(
        0x104,
        "#00302Fへへ、気合をみせな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29B5")

    label("loc_2938")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2979")

    #C0068
    ChrTalk(
        0x109,
        (
            "#10102Fレイモンドさん……\x01",
            "そうですね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B5")

    label("loc_2979")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29B5")

    #C0069
    ChrTalk(
        0x105,
        (
            "#10302Fふうん……\x01",
            "フフ、いいじゃない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B5")


    #C0070
    ChrTalk(
        0x101,
        (
            "#00001Fだったら……\x01",
            "やっぱりここで\x01",
            "捕まえるしかなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A26")
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_2A95")

    label("loc_2A26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A43")
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_2A95")

    label("loc_2A43")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A60")
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_2A95")

    label("loc_2A60")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A7D")
    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2A95")

    label("loc_2A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A95")
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)

    label("loc_2A95")

    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1A1, 0x27)
    SetChrSubChip(0x1A1, 0x0)
    OP_0D()

    #C0071
    ChrTalk(
        0x101,
        (
            "#00007Fいくぞ、みんな！\x01",
            "奴らを無力化する！\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "#5P……だから、何度も\x01",
            "言ってるじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0073
    ChrTalk(
        0x9,
        (
            "#5P#5Sアタシを捕まえられるもんなら、\x01",
            "捕まえてみなってねええええ！！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0074
    ChrTalk(
        0x9,
        "#5P#5S──さあお前たち、やっておしまい！！#3S\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_310", 0x30200011, 0x0, 0x0, 0x21, 0xFF)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BF2")

    label("loc_2BE8")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BF2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-38140, 1300, -300, 0)
    MoveCamera(332, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18670, 0)
    LoadChrToIndex("chr/ch42553.itc", 0x1E)
    LoadChrToIndex("chr/ch24153.itc", 0x1F)
    LoadChrToIndex("chr/ch24100.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch02950.itc", 0x25)
    LoadChrToIndex("chr/ch03050.itc", 0x26)
    LoadChrToIndex("apl/ch51720.itc", 0x27)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -39510, -10, -30, 90)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -40270, -10, -1410, 90)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -40300, -10, 1210, 90)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CED")
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    Jump("loc_2D07")

    label("loc_2CED")

    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    label("loc_2D07")

    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -41450, -10, -50, 90)
    SetChrPos(0x101, -36930, 0, -130, 270)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D69")
    SetChrPos(0x102, -35010, -90, 810, 270)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_2E1C")

    label("loc_2D69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D97")
    SetChrPos(0x103, -35010, -90, 810, 270)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_2E1C")

    label("loc_2D97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DC5")
    SetChrPos(0x104, -35010, -90, 810, 270)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_2E1C")

    label("loc_2DC5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DF3")
    SetChrPos(0x109, -35010, -90, 810, 270)
    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2E1C")

    label("loc_2DF3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E1C")
    SetChrPos(0x105, -35010, -90, 810, 270)
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)

    label("loc_2E1C")

    SetChrPos(0x1A1, -35640, -130, -1310, 270)
    SetChrChipByIndex(0x1A1, 0x27)
    SetChrSubChip(0x1A1, 0x0)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0075
    ChrTalk(
        0x101,
        "#00006Fふう……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x1A1,
        "な、なんとかなったあ……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EA6")
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_2F15")

    label("loc_2EA6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EC3")
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_2F15")

    label("loc_2EC3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EE0")
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_2F15")

    label("loc_2EE0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EFD")
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2F15")

    label("loc_2EFD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F15")
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    label("loc_2F15")

    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1A1, 0xFF)
    SetChrSubChip(0x1A1, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3050")

    #C0077
    ChrTalk(
        0xA,
        "う、う～～ん……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xB,
        "きゅう…………\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        "#5Pぢ、ぢぐじょ～……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#00003F（うーん、お婆さんまで攻撃するのは\x01",
            "　ちょっと可哀想だったかな？）\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "#5Pあ、アンタたち……\x01",
            "タダじゃ済まないからねええ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_3224")

    label("loc_3050")

    OP_2C(0x81, 0x1)

    #C0082
    ChrTalk(
        0x9,
        (
            "#5Pそ……そんな……\x01",
            "そんなバカなぁああ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "#5Pア、アンタたち、しっかりおし！\x01",
            "根性をみせるんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        "う、う～～ん……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xB,
        "きゅう…………\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        "#5Pち、ちくしょう……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "#5Pアンタたち……\x01",
            "よくもやってくれたねェ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "#5Pこうなったら、\x01",
            "列車から飛び降りてでも\x01",
            "逃げ切って……！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0089
    ChrTalk(
        0x101,
        (
            "#00006Fさ、さすがにそれは\x01",
            "無事に済まないと思うので\x01",
            "止めてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        "#5Pくっ……！！\x02",
    )

    CloseMessageWindow()

    label("loc_3224")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32A1")

    #C0091
    ChrTalk(
        0x102,
        (
            "#00106Fほ、ほんとうに\x01",
            "ものすごい執念よね……\x02\x03",

            "#00101Fテロリストたちは\x01",
            "みんなノビちゃってるのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3471")

    label("loc_32A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_331A")

    #C0092
    ChrTalk(
        0x103,
        (
            "#00206F……考えられないくらい\x01",
            "タフですね。\x02\x03",

            "#00200Fテロリストたちは\x01",
            "全員ノビてるというのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3471")

    label("loc_331A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3397")

    #C0093
    ChrTalk(
        0x104,
        (
            "#00306Fかーっ、相変わらず\x01",
            "執念深いバーさんだぜ。\x02\x03",

            "#00301Fテロリストたちは\x01",
            "全員ノビてるってのによ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3471")

    label("loc_3397")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3401")

    #C0094
    ChrTalk(
        0x109,
        (
            "#10106Fう……すごい執念ですね。\x02\x03",

            "#10101Fテロリストたちより\x01",
            "タフなんじゃあ……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3471")

    label("loc_3401")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3471")

    #C0095
    ChrTalk(
        0x105,
        (
            "#10302Fハハ……\x01",
            "なんとも力強いマダムだ。\x02\x03",

            "#10300Fテロリストなんかより\x01",
            "断然強いんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3471")


    #C0096
    ChrTalk(
        0x101,
        (
            "#00006Fはあ……まったくだ。\x02\x03",

            "#00000Fさて、レイモンドさん。\x01",
            "彼らの身柄ですけど、\x01",
            "どうしたらいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x1A1,
        "うーん、そうだねえ。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x1A1,
        (
            "もうすぐアルタイル市に着くし、\x01",
            "連絡して共和国軍に引き渡すのが\x01",
            "いいんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00003Fまあ……\x01",
            "みんな共和国人みたいですし、\x01",
            "それが無難でしょうね。\x02\x03",

            "#00000Fそれじゃあ、車掌さんに\x01",
            "連絡を頼むとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    StopSound(451, 1000, 80)
    StopSound(825, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t5000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1D06 end

    def Function_15_35FA(): pass

    label("Function_15_35FA")

    OP_95(0xFE, -35330, -200, -1940, 4000, 0x0)
    OP_95(0xFE, -36930, 0, -130, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_35FA end

    def Function_16_362A(): pass

    label("Function_16_362A")

    OP_95(0xFE, -34700, -190, -1850, 4000, 0x0)
    OP_95(0xFE, -35010, -90, 810, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_16_362A end

    def Function_17_365A(): pass

    label("Function_17_365A")

    OP_95(0xFE, -34350, -530, -2710, 4000, 0x0)
    OP_95(0xFE, -35640, -130, -1310, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_17_365A end

    SaveToFile()

Try(main)
