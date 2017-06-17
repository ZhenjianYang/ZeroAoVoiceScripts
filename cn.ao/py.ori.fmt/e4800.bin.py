from ScenarioHelper import *

def main():
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
        "雷蒙德搜查官",           # 1
        "假货商",                 # 2
        "共和国恐怖分子",         # 3
        "共和国恐怖分子",         # 4
        "共和国恐怖分子",         # 5
        "SE控制",                 # 6
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
        "Function_5_BEB",          # 05, 5
        "Function_6_C2F",          # 06, 6
        "Function_7_1A5D",         # 07, 7
        "Function_8_1A94",         # 08, 8
        "Function_9_1ACB",         # 09, 9
        "Function_10_1B02",        # 0A, 10
        "Function_11_1B3A",        # 0B, 11
        "Function_12_1B72",        # 0C, 12
        "Function_13_1BAA",        # 0D, 13
        "Function_14_1BE2",        # 0E, 14
        "Function_15_327E",        # 0F, 15
        "Function_16_32AE",        # 10, 16
        "Function_17_32DE",        # 11, 17
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
            "#00000F雷蒙德警官……\x01",
            "不要紧吧？\x02\x03",

            "其实只要交给我们\x01",
            "就可以了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "不、不行……\x01",
            "再怎么说，这也是\x01",
            "警督交给我的任务啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "才不会让你们把\x01",
            "所有风头都抢去～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DD")

    #C0004
    ChrTalk(
        0x102,
        (
            "#00100F呵呵……\x01",
            "那我们就一起加油吧。\x02\x03",

            "话说回来，\x01",
            "假货商跑到哪里去了……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A45")

    label("loc_8DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_935")

    #C0005
    ChrTalk(
        0x103,
        (
            "#00200F呵呵……\x01",
            "要对您刮目相看了。\x02\x03",

            "不过，\x01",
            "假货商在哪里……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A45")

    label("loc_935")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_999")

    #C0006
    ChrTalk(
        0x104,
        (
            "#00300F哈哈……\x01",
            "真有斗志，佩服佩服。\x02\x03",

            "不过，那个老婆婆\x01",
            "跑到哪里去了……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A45")

    label("loc_999")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F5")

    #C0007
    ChrTalk(
        0x109,
        (
            "#10100F啊哈哈……\x01",
            "还真是辛苦呢。\x02\x03",

            "话说回来，\x01",
            "假货商去哪里了……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A45")

    label("loc_9F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A45")

    #C0008
    ChrTalk(
        0x105,
        (
            "#10300F呵呵……\x01",
            "斗志可嘉呢。\x02\x03",

            "不过，那位女士去哪里了……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A45")

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
            "#00003F……多半是通过这种通风口，\x01",
            "从某节车厢的车顶潜逃进车内了吧。\x02\x03",

            "#00000F我们只要从后部车厢开始，\x01",
            "按顺序搜查，应该就能追到她了。\x02\x03",

            "雷蒙德警官，我们行动吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "啊、啊啊，嗯！\x01",
            "一定要把她捉到！\x02",
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

    def Function_5_BEB(): pass

    label("Function_5_BEB")

    OP_95(0xFE, -42770, -480, -2630, 2000, 0x0)
    OP_95(0xFE, -45480, -410, -2520, 2000, 0x0)
    OP_95(0xFE, -45940, -150, -1320, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_5_BEB end

    def Function_6_C2F(): pass

    label("Function_6_C2F")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC8")
    SetChrPos(0x102, 26910, -800, -3100, 0)
    Jump("loc_D5B")

    label("loc_CC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CEE")
    SetChrPos(0x103, 26910, -800, -3100, 0)
    Jump("loc_D5B")

    label("loc_CEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D14")
    SetChrPos(0x104, 26910, -800, -3100, 0)
    Jump("loc_D5B")

    label("loc_D14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D3A")
    SetChrPos(0x109, 26910, -800, -3100, 0)
    Jump("loc_D5B")

    label("loc_D3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D5B")
    SetChrPos(0x105, 26910, -800, -3100, 0)

    label("loc_D5B")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E06")
    BeginChrThread(0x102, 1, 0, 8)
    Jump("loc_E6D")

    label("loc_E06")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E21")
    BeginChrThread(0x103, 1, 0, 8)
    Jump("loc_E6D")

    label("loc_E21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E3C")
    BeginChrThread(0x104, 1, 0, 8)
    Jump("loc_E6D")

    label("loc_E3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E57")
    BeginChrThread(0x109, 1, 0, 8)
    Jump("loc_E6D")

    label("loc_E57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E6D")
    BeginChrThread(0x105, 1, 0, 8)

    label("loc_E6D")

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

    def lambda_F67():
        OP_9D(0xFE, 0x4FBA, 0x0, 0x32, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F67)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FB4")

    def lambda_F97():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F97)
    Jump("loc_1077")

    label("loc_FB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE6")

    def lambda_FC9():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FC9)
    Jump("loc_1077")

    label("loc_FE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1018")

    def lambda_FFB():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FFB)
    Jump("loc_1077")

    label("loc_1018")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_104A")

    def lambda_102D():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_102D)
    Jump("loc_1077")

    label("loc_104A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1077")

    def lambda_105F():
        OP_9D(0xFE, 0x5492, 0x0, 0x3B6, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_105F)

    label("loc_1077")

    Sleep(50)

    def lambda_107F():
        OP_9D(0xFE, 0x5348, 0xFFFFFFBA, 0xFFFFFD12, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_107F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x1A1, 1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopSound(860, 500, 70)
    StopSound(861, 500, 70)

    #C0011
    ChrTalk(
        0x1A1,
        "哇哇哇哇！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#00005F怎、怎么回事……！？\x02",
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
            "#00001F曾在通商会议中发动袭击的\x01",
            "共和国恐怖分子……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xA,
        "你们好像是克洛斯贝尔的警察吧……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xA,
        "虽然不知你们为何而来，但最好立刻止步！\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        "要是再敢继续追，小心没命！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_125A")

    #C0017
    ChrTalk(
        0x102,
        (
            "#00105F……似、似乎真的是恐怖分子呢。\x02\x03",

            "#00106F但完全不明白\x01",
            "他们为何会成为\x01",
            "假货商的同伴……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140B")

    label("loc_125A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12D1")

    #C0018
    ChrTalk(
        0x103,
        (
            "#00201F……看来真的是恐怖分子呢。\x02\x03",

            "#00206F但他们为何会成为\x01",
            "假货商的同伴呢？\x01",
            "真是想不明白……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140B")

    label("loc_12D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_134B")

    #C0019
    ChrTalk(
        0x104,
        (
            "#00301F啧……从装备来看，\x01",
            "确实是恐怖分子。\x02\x03",

            "#00306F但他们为何要\x01",
            "当假货商的手下？\x01",
            "真是搞不懂……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140B")

    label("loc_134B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13B6")

    #C0020
    ChrTalk(
        0x109,
        (
            "#10101F那装备是……\x01",
            "果然没错！\x02\x03",

            "#10106F可、可是，他们为何会\x01",
            "成为假货商的同伴……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140B")

    label("loc_13B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_140B")

    #C0021
    ChrTalk(
        0x105,
        (
            "#10305F哼……\x01",
            "果然没猜错啊。\x02\x03",

            "#10309F莫非是那位女士暗藏的底牌？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140B")


    #C0022
    ChrTalk(
        0x101,
        (
            "#00003F不管怎么说……\x01",
            "这样的威胁是不可能\x01",
            "令我们屈服的。\x02\x03",

            "#00007F我们上！制服他们！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x1A1,
        (
            "哇、哇哇……\x01",
            "等一下～！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1485():
        OP_95(0xFE, 17910, 0, 70, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1485)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14C9")

    def lambda_14AF():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14AF)
    Jump("loc_1580")

    label("loc_14C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14F8")

    def lambda_14DE():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14DE)
    Jump("loc_1580")

    label("loc_14F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1527")

    def lambda_150D():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_150D)
    Jump("loc_1580")

    label("loc_1527")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1556")

    def lambda_153C():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_153C)
    Jump("loc_1580")

    label("loc_1556")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1580")

    def lambda_156B():
        OP_95(0xFE, 19150, 0, 990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_156B)

    label("loc_1580")


    def lambda_1585():
        OP_95(0xFE, 19750, 0, -620, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_1585)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1650")
    SetChrPos(0x102, 20650, 0, 990, 270)
    Jump("loc_16E3")

    label("loc_1650")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1676")
    SetChrPos(0x103, 20650, 0, 990, 270)
    Jump("loc_16E3")

    label("loc_1676")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_169C")
    SetChrPos(0x104, 20650, 0, 990, 270)
    Jump("loc_16E3")

    label("loc_169C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16C2")
    SetChrPos(0x109, 20650, 0, 990, 270)
    Jump("loc_16E3")

    label("loc_16C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16E3")
    SetChrPos(0x105, 20650, 0, 990, 270)

    label("loc_16E3")

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
        "怎、怎么回事，他们究竟是……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xB,
        (
            "啧……虽然那个金发的家伙不值一提，\x01",
            "但另外两人似乎不能小看呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        (
            "不管怎么说，我们已经争取到了时间，\x01",
            "暂且撤退吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        "好！\x02",
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
        "好、好可怕……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#00010F可恶……\x01",
            "又让他们逃走了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18BA")

    #C0030
    ChrTalk(
        0x102,
        (
            "#00103F不过，他们现在已经\x01",
            "无路可逃了。\x02\x03",

            "#00100F保持警惕，继续追吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A23")

    label("loc_18BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1914")

    #C0031
    ChrTalk(
        0x103,
        (
            "#00203F但他们应该已经\x01",
            "无处可逃了。\x02\x03",

            "#00200F保持警觉，继续追吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A23")

    label("loc_1914")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_196E")

    #C0032
    ChrTalk(
        0x104,
        (
            "#00303F但他们现在已经\x01",
            "无处可逃了。\x02\x03",

            "#00301F提高警惕，继续追吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A23")

    label("loc_196E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19CA")

    #C0033
    ChrTalk(
        0x109,
        (
            "#10103F但他们现在已经\x01",
            "无处可退了。\x02\x03",

            "#10101F提高警惕，继续追击吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A23")

    label("loc_19CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A23")

    #C0034
    ChrTalk(
        0x105,
        (
            "#10304F不过，他们恐怕已经\x01",
            "无路可逃了。\x02\x03",

            "#10300F保持警觉，继续追吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A23")

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

    # Function_6_C2F end

    def Function_7_1A5D(): pass

    label("Function_7_1A5D")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 22420, -220, -2090, 4000, 0x0)
    OP_95(0xFE, 17910, 0, 70, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_7_1A5D end

    def Function_8_1A94(): pass

    label("Function_8_1A94")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 22670, -440, -2580, 4000, 0x0)
    OP_95(0xFE, 19750, 0, 990, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_8_1A94 end

    def Function_9_1ACB(): pass

    label("Function_9_1ACB")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 22380, -230, -2140, 4000, 0x0)
    OP_95(0xFE, 19350, 0, -750, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_9_1ACB end

    def Function_10_1B02(): pass

    label("Function_10_1B02")

    OP_95(0xFE, 15020, -220, 2070, 4000, 0x0)
    OP_95(0xFE, 17110, -100, 980, 4000, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_10_1B02 end

    def Function_11_1B3A(): pass

    label("Function_11_1B3A")

    OP_95(0xFE, 15260, -240, -2280, 4000, 0x0)
    OP_95(0xFE, 17280, 0, -680, 4000, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_11_1B3A end

    def Function_12_1B72(): pass

    label("Function_12_1B72")

    OP_93(0xFE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 15020, -220, 2070, 5000, 0x0)
    OP_95(0xFE, 7250, -230, 2260, 5000, 0x0)
    Return()

    # Function_12_1B72 end

    def Function_13_1BAA(): pass

    label("Function_13_1BAA")

    OP_93(0xFE, 0xE1, 0x1F4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 15260, -240, -2280, 5000, 0x0)
    OP_95(0xFE, 7300, -210, -2020, 5000, 0x0)
    Return()

    # Function_13_1BAA end

    def Function_14_1BE2(): pass

    label("Function_14_1BE2")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C95")
    SetChrPos(0x102, -22520, -370, -2480, 270)
    Jump("loc_1D28")

    label("loc_1C95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CBB")
    SetChrPos(0x103, -22520, -370, -2480, 270)
    Jump("loc_1D28")

    label("loc_1CBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CE1")
    SetChrPos(0x104, -22520, -370, -2480, 270)
    Jump("loc_1D28")

    label("loc_1CE1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D07")
    SetChrPos(0x109, -22520, -370, -2480, 270)
    Jump("loc_1D28")

    label("loc_1D07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D28")
    SetChrPos(0x105, -22520, -370, -2480, 270)

    label("loc_1D28")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DE3")
    BeginChrThread(0x102, 1, 0, 16)
    Jump("loc_1E4A")

    label("loc_1DE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DFE")
    BeginChrThread(0x103, 1, 0, 16)
    Jump("loc_1E4A")

    label("loc_1DFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E19")
    BeginChrThread(0x104, 1, 0, 16)
    Jump("loc_1E4A")

    label("loc_1E19")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E34")
    BeginChrThread(0x109, 1, 0, 16)
    Jump("loc_1E4A")

    label("loc_1E34")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E4A")
    BeginChrThread(0x105, 1, 0, 16)

    label("loc_1E4A")

    Sleep(200)
    BeginChrThread(0x1A1, 1, 0, 17)
    WaitChrThread(0x1A1, 1)

    #C0035
    ChrTalk(
        0x101,
        "#00007F站住！！\x02",
    )

    CloseMessageWindow()

    def lambda_1E71():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1E71)
    Sleep(100)

    def lambda_1E81():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E81)
    Sleep(100)

    def lambda_1E91():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1E91)
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
            "#5P哼……真是些\x01",
            "纠缠不休的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#5P不过，好在得到了几个\x01",
            "预料之外的帮手。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00003F……这次终于把你\x01",
            "堵在死路了。\x02\x03",

            "#00001F到此地步，你已经\x01",
            "完全没有逃脱的可能了。\x01",
            "请放弃抵抗，老老实实地投降吧。\x02\x03",

            "你们几名恐怖分子\x01",
            "自然也是一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x1A1,
        "没、没错～赶快投降吧～！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xA,
        "呜……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        "确实如此……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        "已经没希望了……\x02",
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
            "#5P哎呀呀……\x01",
            "现在的年轻人\x01",
            "可真是缺乏毅力。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2138")

    #C0045
    ChrTalk(
        0x102,
        (
            "#00105F这是什么意思……？\x02\x03",

            "#00106F难道你仍然\x01",
            "妄想逃走吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2279")

    label("loc_2138")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_218A")

    #C0046
    ChrTalk(
        0x103,
        (
            "#00205F什么意思……？\x02\x03",

            "#00203F难道仍然妄想\x01",
            "逃走吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2279")

    label("loc_218A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21D8")

    #C0047
    ChrTalk(
        0x104,
        (
            "#00305F此话怎讲……？\x02\x03",

            "#00306F难道你仍然\x01",
            "妄想逃走？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2279")

    label("loc_21D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2234")

    #C0048
    ChrTalk(
        0x109,
        (
            "#10105F这、这是什么意思？\x02\x03",

            "#10101F你该不会是\x01",
            "仍然妄想逃走吧……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2279")

    label("loc_2234")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2279")

    #C0049
    ChrTalk(
        0x105,
        (
            "#10305F哦……？\x02\x03",

            "#10302F看来你仍然\x01",
            "妄想逃跑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2279")


    #C0050
    ChrTalk(
        0x9,
        "#5P妄想……？哈！！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "#5P事到如今，你竟然还会\x01",
            "说出这种幼稚的蠢话。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "#5P……当这辆列车抵达阿尔泰尔市时，\x01",
            "局势就会完全由我掌控了！\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "#5P因为共和国是我的家乡，\x01",
            "我对那里的地形了如指掌！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "#5P等到列车停下的一瞬间，\x01",
            "我就可以溜之大吉了！\x02",
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
            "#00006F溜、溜之大吉……\x02\x03",

            "#00011F已经到此地步了，\x01",
            "你居然还想\x01",
            "逃跑！？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "哼……！\x01",
            "臭小子，给我听好！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0057
    ChrTalk(
        0x9,
        (
            "#5P#5S只要这个世界还没灭亡……\x01",
            "整个大陆都是我的脱身之处！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0058
    ChrTalk(
        0x9,
        (
            "#5P#5S在你们真正\x01",
            "追到我之前……\x01",
            "我是绝对不会束手就擒的！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0059
    ChrTalk(
        0x9,
        (
            "#5P#5S听明白了吗！？\x01",
            "你们这群蠢货！#3S\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        "哦哦哦……！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xC,
        "我们也来帮忙！！\x02",
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
            "#00006F这、这个……\x01",
            "虽然语无伦次……\x01",
            "但她好像真的打算继续逃跑呢。\x02\x03",

            "不过，以这位老婆婆的性格来说，\x01",
            "会顽抗到底也是意料之中的情况……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x1A1,
        (
            "我、我一定……\x01",
            "一定不会让你逃跑的！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x1A1,
        (
            "因为这是警督交付给我\x01",
            "的重要任务！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2673")

    #C0065
    ChrTalk(
        0x102,
        "#00105F雷蒙德警官……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2757")

    label("loc_2673")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26B2")

    #C0066
    ChrTalk(
        0x103,
        (
            "#00205F雷蒙德警官……\x01",
            "……说的没错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2757")

    label("loc_26B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26E6")

    #C0067
    ChrTalk(
        0x104,
        "#00302F嘿嘿，很有干劲嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2757")

    label("loc_26E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2721")

    #C0068
    ChrTalk(
        0x109,
        (
            "#10102F雷蒙德警官……\x01",
            "说的没错！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2757")

    label("loc_2721")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2757")

    #C0069
    ChrTalk(
        0x105,
        (
            "#10302F呼……\x01",
            "呵呵，很有斗志嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2757")


    #C0070
    ChrTalk(
        0x101,
        (
            "#00001F既然如此……\x01",
            "我们也只能在这里\x01",
            "将他们捕获了。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27C0")
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_282F")

    label("loc_27C0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27DD")
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_282F")

    label("loc_27DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27FA")
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_282F")

    label("loc_27FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2817")
    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_282F")

    label("loc_2817")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_282F")
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)

    label("loc_282F")

    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1A1, 0x27)
    SetChrSubChip(0x1A1, 0x0)
    OP_0D()

    #C0071
    ChrTalk(
        0x101,
        (
            "#00007F我们上吧！\x01",
            "立刻将他们制服！\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "#5P……我都说过\x01",
            "很多次了。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0073
    ChrTalk(
        0x9,
        (
            "#5P#5S你们要是抓得到我的话，\x01",
            "就来试试看吧！！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0074
    ChrTalk(
        0x9,
        "#5P#5S你们几个给我上！干掉他们！！#3S\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_310", 0x30200011, 0x0, 0x0, 0x21, 0xFF)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2956")

    label("loc_294C")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2956")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A51")
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    Jump("loc_2A6B")

    label("loc_2A51")

    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    label("loc_2A6B")

    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -41450, -10, -50, 90)
    SetChrPos(0x101, -36930, 0, -130, 270)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ACD")
    SetChrPos(0x102, -35010, -90, 810, 270)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_2B80")

    label("loc_2ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AFB")
    SetChrPos(0x103, -35010, -90, 810, 270)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_2B80")

    label("loc_2AFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B29")
    SetChrPos(0x104, -35010, -90, 810, 270)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_2B80")

    label("loc_2B29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B57")
    SetChrPos(0x109, -35010, -90, 810, 270)
    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2B80")

    label("loc_2B57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B80")
    SetChrPos(0x105, -35010, -90, 810, 270)
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)

    label("loc_2B80")

    SetChrPos(0x1A1, -35640, -130, -1310, 270)
    SetChrChipByIndex(0x1A1, 0x27)
    SetChrSubChip(0x1A1, 0x0)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0075
    ChrTalk(
        0x101,
        "#00006F呼……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x1A1,
        "总、总算解决了啊……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C04")
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_2C73")

    label("loc_2C04")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C21")
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_2C73")

    label("loc_2C21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C3E")
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_2C73")

    label("loc_2C3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C5B")
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_2C73")

    label("loc_2C5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C73")
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    label("loc_2C73")

    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x1A1, 0xFF)
    SetChrSubChip(0x1A1, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D8A")

    #C0077
    ChrTalk(
        0xA,
        "唔～唔唔……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xB,
        "呃…………\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        "#5P可、可恶……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#00003F（唔……连老婆婆都遭到攻击了，\x01",
            "　似乎有点可怜呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "#5P你、你们等着……\x01",
            "此仇不报，我绝不罢休……\x02",
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
    Jump("loc_2F1C")

    label("loc_2D8A")

    OP_2C(0x81, 0x1)

    #C0082
    ChrTalk(
        0x9,
        (
            "#5P怎……怎么会……\x01",
            "怎么会这样啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "#5P你、你们几个，振作一点！\x01",
            "拿出毅力来啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        "唔～唔唔……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xB,
        "呃…………\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        "#5P可、可恶……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "#5P看、看……\x01",
            "看看你们干的好事！！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "#5P既然如此，\x01",
            "就算从列车上跳下去，\x01",
            "我也必须要逃走……！！\x02",
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
            "#00006F那、那样做肯定\x01",
            "会受重伤的，\x01",
            "请别干傻事。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        "#5P唔……！！\x02",
    )

    CloseMessageWindow()

    label("loc_2F1C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F91")

    #C0091
    ChrTalk(
        0x102,
        (
            "#00106F还、还真是\x01",
            "顽固得可怕啊……\x02\x03",

            "#00101F恐怖分子都失去战斗能力了，\x01",
            "她却还不放弃抵抗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3139")

    label("loc_2F91")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FFE")

    #C0092
    ChrTalk(
        0x103,
        (
            "#00206F……顽固程度真是\x01",
            "超出预料。\x02\x03",

            "#00200F恐怖分子都倒下了，\x01",
            "她却还不放弃抵抗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3139")

    label("loc_2FFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_307B")

    #C0093
    ChrTalk(
        0x104,
        (
            "#00306F呼，这老婆婆还是\x01",
            "和以前一样顽固不堪啊。\x02\x03",

            "#00301F恐怖分子都被我们制服了，\x01",
            "她却还要继续抵抗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3139")

    label("loc_307B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30DB")

    #C0094
    ChrTalk(
        0x109,
        (
            "#10106F呜……真是顽固得可怕啊。\x02\x03",

            "#10101F也许比恐怖分子\x01",
            "还要难缠呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3139")

    label("loc_30DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3139")

    #C0095
    ChrTalk(
        0x105,
        (
            "#10302F哈哈……\x01",
            "这位女士真是强健啊。\x02\x03",

            "#10300F我看她比恐怖分子\x01",
            "都厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3139")


    #C0096
    ChrTalk(
        0x101,
        (
            "#00006F呼……真是的。\x02\x03",

            "#00000F雷蒙德警官，\x01",
            "接下来要如何\x01",
            "处理他们呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x1A1,
        "唔，这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x1A1,
        (
            "马上就要抵达阿尔泰尔市了，\x01",
            "我们联络共和国军，把这些\x01",
            "家伙交给他们来处理吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00003F也对……\x01",
            "他们好像都是共和国人，\x01",
            "这应该是最妥善的选择。\x02\x03",

            "#00000F好，那我们这就去\x01",
            "找乘务员帮忙吧。\x02",
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

    # Function_14_1BE2 end

    def Function_15_327E(): pass

    label("Function_15_327E")

    OP_95(0xFE, -35330, -200, -1940, 4000, 0x0)
    OP_95(0xFE, -36930, 0, -130, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_327E end

    def Function_16_32AE(): pass

    label("Function_16_32AE")

    OP_95(0xFE, -34700, -190, -1850, 4000, 0x0)
    OP_95(0xFE, -35010, -90, 810, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_16_32AE end

    def Function_17_32DE(): pass

    label("Function_17_32DE")

    OP_95(0xFE, -34350, -530, -2710, 4000, 0x0)
    OP_95(0xFE, -35640, -130, -1310, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_17_32DE end

    SaveToFile()

Try(main)
