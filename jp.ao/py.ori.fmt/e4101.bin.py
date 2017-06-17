from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4101.bin",                # FileName
        "e4101",                    # MapName
        "e4101",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4101",                  # 0
        "特務支援車",             # 1
        "運搬車",                 # 2
        "アリアンロード",         # 3
        "神速のデュバリィ",       # 4
        "魔弓のエンネア",         # 5
        "剛毅のアイネス",         # 6
        "ミンネス",               # 7
        "猫型魔獣",               # 8
        "猫型魔獣",               # 9
        "猫型魔獣",               # 10
        "猫型魔獣",               # 11
        "猫型魔獣",               # 12
        "槍",                     # 13
        "共和国戦車",             # 14
        "共和国戦車",             # 15
        "共和国戦車",             # 16
        "共和国戦車",             # 17
        "共和国飛行艇",           # 18
        "共和国飛行艇",           # 19
        "共和国飛行艇",           # 20
        "共和国飛行艇",           # 21
        "SE制御",                 # 22
        "ダミー",                 # 23
        "ダミー",                 # 24
        "ダミー",                 # 25
        "ダミー",                 # 26
        "ダミー",                 # 27
        "br2000",                 # 28
    ))

    ATBonus("ATBonus_3B8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_3D8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_45C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_460", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_464", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_468", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_46C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_470", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_478", 0x0042, 255, 6, 45, 3, 3, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms82004.dat", "ms82004.dat", "ms82004.dat", "ms82004.dat", "ms82004.dat", 0, 0, 0, "MonsterBattlePostion_3D8", "MonsterBattlePostion_458", "ed7453", "ed7453", "ATBonus_3B8"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1364, 0)                                       # 0

    ScpFunction((
        "Function_0_554",          # 00, 0
        "Function_1_5A0",          # 01, 1
        "Function_2_5A1",          # 02, 2
        "Function_3_5B6",          # 03, 3
        "Function_4_108F",         # 04, 4
        "Function_5_10F1",         # 05, 5
        "Function_6_1145",         # 06, 6
        "Function_7_1199",         # 07, 7
        "Function_8_11A9",         # 08, 8
        "Function_9_11B9",         # 09, 9
        "Function_10_11C9",        # 0A, 10
        "Function_11_11D9",        # 0B, 11
        "Function_12_11E9",        # 0C, 12
        "Function_13_11F9",        # 0D, 13
        "Function_14_123F",        # 0E, 14
        "Function_15_137D",        # 0F, 15
        "Function_16_13C3",        # 10, 16
        "Function_17_161D",        # 11, 17
        "Function_18_166A",        # 12, 18
        "Function_19_16BF",        # 13, 19
        "Function_20_170B",        # 14, 20
        "Function_21_17C2",        # 15, 21
        "Function_22_19BD",        # 16, 22
        "Function_23_1A67",        # 17, 23
        "Function_24_3C3E",        # 18, 24
        "Function_25_3C58",        # 19, 25
        "Function_26_3C7B",        # 1A, 26
        "Function_27_3C8E",        # 1B, 27
        "Function_28_3CA7",        # 1C, 28
        "Function_29_3D27",        # 1D, 29
        "Function_30_3DB5",        # 1E, 30
        "Function_31_3DF0",        # 1F, 31
        "Function_32_3E51",        # 20, 32
        "Function_33_3EA3",        # 21, 33
        "Function_34_3EE1",        # 22, 34
        "Function_35_3F1F",        # 23, 35
        "Function_36_3F49",        # 24, 36
        "Function_37_3F73",        # 25, 37
    ))


    def Function_0_554(): pass

    label("Function_0_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_568")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)
    Jump("loc_59F")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_57C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 14)
    Jump("loc_59F")

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_590")
    ClearScenarioFlags(0x22, 2)
    Event(0, 16)
    Jump("loc_59F")

    label("loc_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_59F")
    ClearScenarioFlags(0x22, 3)
    Event(0, 23)

    label("loc_59F")

    Return()

    # Function_0_554 end

    def Function_1_5A0(): pass

    label("Function_1_5A0")

    Return()

    # Function_1_5A0 end

    def Function_2_5A1(): pass

    label("Function_2_5A1")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Return()

    # Function_2_5A1 end

    def Function_3_5B6(): pass

    label("Function_3_5B6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x7, "event/ev15070.eff")
    LoadEffect(0x9, "event/eva03_01.eff")
    OP_F3(200000)
    Call(0, 2)
    SoundLoad(924)
    SoundLoad(497)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 0, 0, 0, 0)
    OP_74(0x0, 0x1E)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0x15)
    OP_93(0x15, 0x10E, 0x0)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 0, 0, 0, 0)
    OP_74(0x1, 0x1E)
    SetMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    OP_78(0x1, 0x16)
    OP_93(0x16, 0x10E, 0x0)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 0, 0, 0, 0)
    OP_74(0x9, 0x1E)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    OP_78(0x9, 0x17)
    OP_93(0x17, 0x10E, 0x0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x17, 0x40)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 0, 0, 0, 0)
    OP_74(0xA, 0x1E)
    SetMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0xA, 0x4)
    OP_78(0xA, 0x18)
    OP_93(0x18, 0x10E, 0x0)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x18, 0x40)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 0, 0, 0, 0)
    OP_74(0x2, 0x1E)
    SetMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0x19)
    OP_93(0x19, 0x10E, 0x0)
    OP_71(0x2, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 0, 0, 0, 0)
    OP_74(0x3, 0x1E)
    SetMapObjFlags(0x3, 0x1000)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0x1A)
    OP_93(0x1A, 0x10E, 0x0)
    OP_71(0x3, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 0, 0, 0, 0)
    OP_74(0x7, 0x1E)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    OP_78(0x7, 0x1B)
    OP_93(0x1B, 0x10E, 0x0)
    OP_71(0x7, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 0, 0, 0, 0)
    OP_74(0x8, 0x1E)
    SetMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    OP_78(0x8, 0x1C)
    OP_93(0x1C, 0x10E, 0x0)
    OP_71(0x8, 0x3D, 0x78, 0x0, 0x20)
    OP_68(-170690, -2150, -14350, 0)
    MoveCamera(259, 176, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(90630, 0)
    OP_68(-174690, -2150, -14350, 5500)
    OP_11(0xD0, 0xD0, 0xFF, 0x32, 0x226, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    PlaceName2(340, 200, "c_plac65", 0x0, 0)
    OP_6F(0x79)
    OP_11(0xD0, 0xD0, 0xFF, 0x1E, 0x15E, 0x0)
    BeginChrThread(0x1D, 1, 0, 13)
    Sound(497, 2, 50, 0)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetChrPos(0x15, -9000, 0, -1600, 270)
    SetChrPos(0x16, 3600, 0, -3700, 270)
    SetChrPos(0x17, 40000, 0, -3200, 270)
    SetChrPos(0x18, 77100, 0, -3200, 270)
    OP_FF(0x9, 0x320, 0x320, 0x320)
    OP_FF(0xA, 0x2BC, 0x2BC, 0x2BC)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    SetChrPos(0x19, -1000, 18000, -13000, 270)
    SetChrPos(0x1A, 45000, 15000, -6000, 270)
    SetChrPos(0x1B, 85000, 36500, 4059, 270)
    SetChrPos(0x1C, 64000, 35500, 6360, 270)
    OP_FF(0x0, 0x3E8, 0x3E8, 0x3E8)
    OP_FF(0x1, 0x3E8, 0x3E8, 0x3E8)
    OP_FF(0x9, 0x1F4, 0x1F4, 0x1F4)
    OP_FF(0xA, 0x1F4, 0x1F4, 0x1F4)
    Fade(500)
    OP_68(-89570, 2650, -10430, 0)
    MoveCamera(83, -7, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(6260, 0)
    PlayEffect(0x7, 0x0, 0x19, 0x5, -6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x1, 0x19, 0x5, 6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x2, 0x1A, 0x5, -6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x3, 0x1A, 0x5, 6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x4, 0x1B, 0x5, -3200, 500, 125, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x5, 0x1B, 0x5, 3200, 500, 125, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x6, 0x1C, 0x5, -3200, 500, 125, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x7, 0x1C, 0x5, 3200, 500, 125, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x15, 0, 0, 5)
    BeginChrThread(0x16, 0, 0, 6)
    BeginChrThread(0x17, 0, 0, 7)
    BeginChrThread(0x18, 0, 0, 8)
    BeginChrThread(0x19, 0, 0, 9)
    BeginChrThread(0x1A, 0, 0, 10)
    BeginChrThread(0x1B, 0, 0, 11)
    BeginChrThread(0x1C, 0, 0, 12)
    MoveCamera(83, -9, 0, 5500)
    OP_0D()
    Sleep(4500)
    OP_68(-89570, 1650, -10430, 18000)
    MoveCamera(290, 7, 0, 18000)
    SetCameraDistance(5500, 14000)
    Sleep(4000)
    BlurSwitch(0xBB8, 0x77FFFFFF, 0x0, 0x1, 0xA)
    Sleep(4000)
    CancelBlur(2000)
    Sleep(2000)
    EndChrThread(0x1D, 0x1)
    OP_25(0x39C, 0x28)
    OP_25(0x1F1, 0x64)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    StopEffect(0x5, 0x0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x1A, 0x0)
    EndChrThread(0x1B, 0x0)
    EndChrThread(0x1C, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    OP_71(0x2, 0x3D, 0x78, 0x0, 0x20)
    OP_71(0x3, 0x3D, 0x78, 0x0, 0x20)
    OP_71(0x7, 0x3D, 0x78, 0x0, 0x20)
    OP_71(0x8, 0x3D, 0x78, 0x0, 0x20)
    SetChrPos(0x19, 4000, 12450, 3090, 0)
    SetChrPos(0x1A, 20000, 18600, 6160, 0)
    SetChrPos(0x1B, -21000, 8000, -12000, 0)
    SetChrPos(0x1C, 7000, 11000, -14000, 0)
    OP_93(0x19, 0x10B, 0x0)
    OP_93(0x1A, 0x10B, 0x0)
    OP_93(0x1B, 0x10B, 0x0)
    OP_93(0x1C, 0x10B, 0x0)
    SetChrPos(0x15, -39000, 0, -1600, 270)
    SetChrPos(0x16, -21600, 0, -4200, 270)
    SetChrPos(0x17, -4000, 0, -3200, 270)
    SetChrPos(0x18, 15100, 0, -2800, 270)
    OP_FF(0x0, 0x384, 0x384, 0x384)
    OP_FF(0x1, 0x384, 0x384, 0x384)
    OP_FF(0x9, 0x384, 0x384, 0x384)
    OP_FF(0xA, 0x384, 0x384, 0x384)
    OP_FF(0x2, 0x384, 0x384, 0x384)
    OP_FF(0x3, 0x3E8, 0x3E8, 0x3E8)
    OP_FF(0x7, 0x1C2, 0x1C2, 0x1C2)
    OP_FF(0x8, 0x226, 0x226, 0x226)
    PlayEffect(0x7, 0xFF, 0x19, 0x5, -5760, 1000, 225, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x19, 0x5, 5760, 1000, 225, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x1A, 0x5, -6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x1A, 0x5, 6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x1B, 0x5, -2880, 450, 112, 0, 0, 0, 450, 450, 450, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x1B, 0x5, 2880, 450, 112, 0, 0, 0, 450, 450, 450, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x1C, 0x5, -3520, 550, 138, 0, 0, 0, 550, 550, 550, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0x1C, 0x5, 3520, 550, 138, 0, 0, 0, 550, 550, 550, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0x1B, 0x5, 0, 0, 0, 180, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9, 0xFF, 0x1B, 0x5, 0, 0, 0, 180, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_11(0xD0, 0xD0, 0xFF, 0x55, 0x1F3, 0x0)
    Fade(500)
    OP_68(-33540, 1650, -1540, 0)
    MoveCamera(278, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(71590, 0)
    OP_68(-83980, 1650, -6630, 12000)
    MoveCamera(274, 19, 0, 12000)
    OP_6E(600, 12000)
    SetCameraDistance(71590, 12000)
    BeginChrThread(0x15, 0, 0, 5)
    BeginChrThread(0x16, 0, 0, 6)
    BeginChrThread(0x17, 0, 0, 7)
    BeginChrThread(0x18, 0, 0, 8)
    BeginChrThread(0x19, 0, 0, 9)
    BeginChrThread(0x1A, 0, 0, 10)
    BeginChrThread(0x1B, 0, 0, 11)
    BeginChrThread(0x1C, 0, 0, 12)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_0D()
    CancelBlur(2000)
    Sleep(2000)
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sleep(8000)
    StopSound(924, 2000, 40)
    StopSound(497, 2000, 100)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("t1490", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_5B6 end

    def Function_4_108F(): pass

    label("Function_4_108F")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 37450, 0, -2200)
    OP_9F(0x1, -124100, 0, -3550)
    OP_9F(0x1, -155100, 0, -7150)
    OP_9F(0x1, -186100, 0, -13850)
    OP_9F(0x1, -222900, 0, -23800)
    OP_9F(0x1, -268250, 0, -29550)
    OP_9F(0x2, 0xFE, 3000, 0x6)
    Return()

    # Function_4_108F end

    def Function_5_10F1(): pass

    label("Function_5_10F1")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -124100, 0, -2450)
    OP_9F(0x1, -155100, 0, -6050)
    OP_9F(0x1, -186100, 0, -12750)
    OP_9F(0x1, -222900, 0, -22700)
    OP_9F(0x1, -268250, 0, -28150)
    OP_9F(0x2, 0xFE, 7000, 0x6)
    Return()

    # Function_5_10F1 end

    def Function_6_1145(): pass

    label("Function_6_1145")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -124100, 0, -6050)
    OP_9F(0x1, -155100, 0, -9650)
    OP_9F(0x1, -186100, 0, -16350)
    OP_9F(0x1, -222900, 0, -26300)
    OP_9F(0x1, -268250, 0, -32049)
    OP_9F(0x2, 0xFE, 7000, 0x6)
    Return()

    # Function_6_1145 end

    def Function_7_1199(): pass

    label("Function_7_1199")

    OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x1B58, 0x1)
    Return()

    # Function_7_1199 end

    def Function_8_11A9(): pass

    label("Function_8_11A9")

    OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x1B58, 0x1)
    Return()

    # Function_8_11A9 end

    def Function_9_11B9(): pass

    label("Function_9_11B9")

    OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x1B58, 0x1)
    Return()

    # Function_9_11B9 end

    def Function_10_11C9(): pass

    label("Function_10_11C9")

    OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x1AF4, 0x1)
    Return()

    # Function_10_11C9 end

    def Function_11_11D9(): pass

    label("Function_11_11D9")

    OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x1A90, 0x1)
    Return()

    # Function_11_11D9 end

    def Function_12_11E9(): pass

    label("Function_12_11E9")

    OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0x1A2C, 0x1)
    Return()

    # Function_12_11E9 end

    def Function_13_11F9(): pass

    label("Function_13_11F9")

    Sound(924, 2, 10, 0)
    Sleep(500)
    OP_25(0x39C, 0x14)
    Sleep(500)
    OP_25(0x39C, 0x1E)
    Sleep(500)
    OP_25(0x39C, 0x28)
    Sleep(500)
    OP_25(0x39C, 0x32)
    Sleep(500)
    OP_25(0x39C, 0x3C)
    Sleep(500)
    OP_25(0x39C, 0x46)
    Sleep(1000)
    OP_25(0x39C, 0x50)
    Sleep(1000)
    OP_25(0x39C, 0x5A)
    Sleep(1000)
    OP_25(0x39C, 0x64)
    Return()

    # Function_13_11F9 end

    def Function_14_123F(): pass

    label("Function_14_123F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(952)
    SoundLoad(145)
    SetChrPos(0x0, -185300, 15250, -52700, 0)
    Call(0, 2)
    OP_68(-185300, 30750, -52700, 0)
    MoveCamera(45, -15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(-185300, 16500, -52700, 5000)
    MoveCamera(45, 0, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(16250, 5000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-185300, 15750, -52700, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    OP_68(-185300, 16250, -52700, 3000)
    SetCameraDistance(25000, 7000)
    BeginChrThread(0x1D, 1, 0, 15)
    OP_71(0x6, 0x0, 0xD2, 0x0, 0x8)
    OP_79(0x6)
    Sound(952, 2, 100, 0)
    OP_71(0x6, 0xD2, 0x12C, 0x0, 0x20)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    StopSound(952, 500, 100)
    OP_0D()
    OP_24(0x91)
    SetScenarioFlags(0x22, 0)
    NewScene("e4830", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_123F end

    def Function_15_137D(): pass

    label("Function_15_137D")

    Sound(140, 0, 100, 0)
    Sleep(500)
    Sound(145, 2, 100, 0)
    Sleep(1200)
    OP_24(0x91)
    Sound(143, 0, 60, 0)
    Sleep(200)
    Sound(145, 2, 100, 0)
    Sleep(1900)
    OP_24(0x91)
    Sound(143, 0, 60, 0)
    Sleep(200)
    Sound(145, 2, 100, 0)
    Sleep(2400)
    OP_24(0x91)
    Sound(143, 0, 60, 0)
    Return()

    # Function_15_137D end

    def Function_16_13C3(): pass

    label("Function_16_13C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x4, 0x8)
    OP_49()
    OP_D5(0x8, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_71(0x4, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x8, 1, 0, 21)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x5, 0x9)
    OP_49()
    OP_D5(0x9, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x9, 1, 0, 22)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_68(-236580, 1250, -26430, 0)
    MoveCamera(34, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30020, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8)
    OP_6B(0x1E)
    BeginChrThread(0x1E, 1, 0, 20)
    Sleep(500)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8)
    LoadEffect(0x0, "battle/cr003200.eff")
    LoadEffect(0x1, "event/ev12013.eff")
    OP_F3(990000)
    SoundLoad(469)
    Sound(469, 2, 100, 0)
    BeginChrThread(0x1D, 1, 0, 19)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrPos(0x1F, -197980, 50, -12890, 90)
    SetChrPos(0x21, -187980, 50, -12890, 90)
    BeginChrThread(0x1F, 1, 0, 17)
    BeginChrThread(0x21, 1, 0, 18)
    Sleep(2000)
    Sleep(1900)
    SetChrPos(0x20, -160530, 50, -10830, 90)
    SetChrPos(0x22, -150530, 50, -10830, 90)
    BeginChrThread(0x20, 1, 0, 17)
    BeginChrThread(0x22, 1, 0, 18)
    Sleep(2000)
    Sleep(3100)
    SetChrPos(0x1F, -108310, 50, -780, 90)
    SetChrPos(0x21, -98310, 50, -780, 90)
    BeginChrThread(0x1F, 1, 0, 17)
    BeginChrThread(0x21, 1, 0, 18)
    Sleep(600)
    SetChrPos(0x20, -101150, 50, -3960, 90)
    SetChrPos(0x22, -91150, 50, -3960, 90)
    BeginChrThread(0x20, 1, 0, 17)
    BeginChrThread(0x22, 1, 0, 18)
    Sleep(1400)
    Sleep(600)
    Sleep(2500)
    StopSound(469, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 6)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_13C3 end

    def Function_17_161D(): pass

    label("Function_17_161D")

    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
    Sleep(2000)
    Return()

    # Function_17_161D end

    def Function_18_166A(): pass

    label("Function_18_166A")

    Sleep(500)
    Sleep(2000)
    OP_82(0x12C, 0x1F4, 0xBB8, 0x190)
    Sound(196, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_18_166A end

    def Function_19_16BF(): pass

    label("Function_19_16BF")

    Sleep(1200)
    Sound(457, 0, 100, 0)
    Sleep(2000)
    Sound(486, 0, 100, 0)
    Sound(492, 0, 100, 0)
    Sleep(2500)
    Sound(458, 0, 100, 0)
    Sleep(1400)
    Sound(492, 0, 100, 0)
    Sleep(3100)
    Sound(494, 0, 100, 0)
    Sleep(2000)
    Sound(494, 0, 100, 0)
    Sound(487, 0, 100, 0)
    Sleep(1000)
    Sound(492, 0, 100, 0)
    Return()

    # Function_19_16BF end

    def Function_20_170B(): pass

    label("Function_20_170B")

    SetChrPos(0xFE, -235580, 0, -26430, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -233580, 0, -26430)
    OP_9F(0x1, -209600, 0, -21900)
    OP_9F(0x1, -195960, 0, -16980)
    OP_9F(0x2, 0xFE, 10600, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -169890, 0, -10880)
    OP_9F(0x2, 0xFE, 10600, 0x6)
    OP_9F(0x1, -139150, 0, -4810)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -110490, 0, -2720)
    OP_9F(0x1, -88320, 0, -2970)
    OP_9F(0x1, -38320, 0, -2510)
    OP_9F(0x1, 28510, 0, -2510)
    OP_9F(0x2, 0xFE, 10600, 0x6)
    Return()

    # Function_20_170B end

    def Function_21_17C2(): pass

    label("Function_21_17C2")

    SetChrPos(0xFE, -248580, 0, -25430, 0)
    OP_9F(0x0, 0xFE)
    Sound(494, 0, 100, 0)
    OP_9F(0x1, -248580, 0, -25430)
    OP_9F(0x1, -211600, 0, -19900)
    OP_9F(0x2, 0xFE, 12500, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -197960, 0, -14980)
    OP_9F(0x1, -192500, 0, -16980)
    OP_9F(0x1, -185500, 0, -15480)
    OP_9F(0x1, -180500, 0, -14000)
    OP_9F(0x1, -169890, 0, -12500)
    OP_9F(0x2, 0xFE, 12000, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -169890, 0, -12500)
    OP_9F(0x1, -156500, 0, -9600)
    OP_9F(0x1, -152500, 0, -6000)
    OP_9F(0x1, -145500, 0, -4500)
    OP_9F(0x2, 0xFE, 10700, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -145500, 0, -4500)
    OP_9F(0x1, -130150, 0, -2200)
    OP_9F(0x2, 0xFE, 10700, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -130150, 0, -2200)
    OP_9F(0x1, -105490, 0, -1200)
    OP_9F(0x1, -101490, 0, -4100)
    OP_9F(0x1, -97500, 0, -4200)
    OP_9F(0x2, 0xFE, 10700, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -97500, 0, -4200)
    OP_9F(0x1, -96500, 0, -4100)
    OP_9F(0x1, -95500, 0, -3400)
    OP_9F(0x1, -92500, 0, -1100)
    OP_9F(0x1, -89500, 0, -1100)
    OP_9F(0x1, -86500, 0, -1100)
    OP_9F(0x2, 0xFE, 10700, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -86500, 0, -1100)
    OP_9F(0x1, -79320, 0, -1710)
    OP_9F(0x1, -70320, 0, -1810)
    OP_9F(0x1, -40320, 0, -2110)
    OP_9F(0x1, 26510, 0, -3510)
    OP_9F(0x2, 0xFE, 9300, 0x6)
    Return()

    # Function_21_17C2 end

    def Function_22_19BD(): pass

    label("Function_22_19BD")

    SetChrPos(0xFE, -224580, 0, -26430, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -223580, 0, -26430)
    OP_9F(0x1, -206600, 0, -21900)
    OP_9F(0x1, -192960, 0, -16980)
    OP_9F(0x1, -166890, 0, -10880)
    OP_9F(0x1, -134150, 0, -4810)
    OP_9F(0x2, 0xFE, 10500, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -106490, 0, -2720)
    OP_9F(0x1, -85320, 0, -2970)
    OP_9F(0x1, -35320, 0, -2510)
    OP_9F(0x1, 31510, 0, -2510)
    OP_9F(0x2, 0xFE, 10500, 0x6)
    Return()

    # Function_22_19BD end

    def Function_23_1A67(): pass

    label("Function_23_1A67")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch45200.itc", 0x1E)
    LoadChrToIndex("apl/ch51546.itc", 0x1F)
    LoadChrToIndex("monster/ch82051.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch02950.itc", 0x25)
    LoadChrToIndex("chr/ch03050.itc", 0x26)
    LoadChrToIndex("apl/ch51544.itc", 0x27)
    LoadChrToIndex("monster/ch82050.itc", 0x28)
    SoundLoad(469)
    SoundLoad(868)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x5, 0x9)
    OP_49()
    OP_D5(0x9, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x9, 1, 0, 29)
    OP_68(-82750, 1250, -3000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32500, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8)
    OP_6B(0x1E)
    BeginChrThread(0x1E, 1, 0, 28)
    Sleep(500)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x14, 0x27)
    SetChrSubChip(0x14, 0x0)
    LoadEffect(0x1, "event/ev15100.eff")
    LoadEffect(0x2, "event/ev15101.eff")
    LoadEffect(0x3, "event/ev10010.eff")
    LoadEffect(0x4, "event/ev15102.eff")
    Sound(469, 2, 100, 0)
    Sound(494, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3500)
    Sound(288, 0, 100, 0)
    BeginChrThread(0x1D, 2, 0, 25)
    OP_82(0x3E8, 0x7D0, 0xBB8, 0x320)
    PlayEffect(0x1, 0x0, 0xFF, 0x0, -167950, 0, -11810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0xFF, 0x0, -167950, 0, -11810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x14, -167950, 0, -11810, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    Sleep(500)
    Sound(487, 0, 100, 0)

    #N0001
    NpcTalk(
        0x9,
        "ミンネス",
        "#11A何ィィィィィイッ！？\x02",
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    Sleep(500)
    Sound(200, 0, 80, 0)
    Sound(880, 0, 100, 0)
    OP_24(0x1D5)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x8)
    OP_82(0x12C, 0x4B0, 0xBB8, 0x1F4)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -160750, 1850, 1110, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(868, 2, 30, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -159400, 2150, 2080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2500)
    OP_6B(0xFF)
    OP_68(-171180, 1250, -4430, 3000)
    MoveCamera(14, 28, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(29580, 3000)

    def lambda_1D8F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1D8F)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x4, 0x8)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_71(0x4, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x8, 1, 0, 30)
    OP_6F(0x79)
    Sound(492, 0, 100, 0)
    WaitChrThread(0x8, 1)
    StopSound(459, 500, 90)
    OP_71(0x4, 0x5B, 0x78, 0x1, 0x8)
    Sleep(500)

    #N0002
    NpcTalk(
        0x8,
        "エリィ",
        "#00105Fこ、これは一体……！？\x02",
    )

    CloseMessageWindow()

    #N0003
    NpcTalk(
        0x8,
        "ティオ",
        (
            "#00205F凄まじい衝撃を\x01",
            "受けたようですけど……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    StopSound(868, 3000, 20)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-168010, 1250, -6300, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16780, 0)
    SetChrPos(0x101, -169400, 50, -6500, 90)
    SetChrPos(0x102, -169300, 50, -7900, 90)
    SetChrPos(0x104, -169300, 50, -5100, 90)
    SetChrPos(0x109, -171200, 50, -6500, 90)
    SetChrPos(0x103, -171000, 50, -7900, 90)
    SetChrPos(0x105, -171000, 50, -5100, 90)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -164500, 50, -6100, 270)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    #C0004
    ChrTalk(
        0xE,
        (
            "い、一体何が……\x01",
            "起こったというのだっ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#00003Fよく分からないけど……\x02\x03",

            "#00001F……年貢の納め時だ。\x01",
            "おとなしく投降してもらおうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)

    #C0006
    ChrTalk(
        0xE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xE,
        (
            "……クククッ……\x01",
            "クククククッ…………！！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0008
    ChrTalk(
        0xE,
        "#5Sクハハハハハハハッ……！！#3S\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xE,
        (
            "……いいでしょう……\x01",
            "私もいよいよ女神に見放されたようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xE,
        (
            "しかし……私は転んでも\x01",
            "ただでは起きないタチでしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xE,
        (
            "こうなったら、貴方方も\x01",
            "地獄の道連れにして差し上げましょう！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    OP_68(-165130, 1250, -4310, 2000)
    MoveCamera(52, 30, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(16780, 2000)
    OP_93(0xE, 0x2D, 0x1F4)

    def lambda_226A():

        label("loc_226A")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_226A")

    QueueWorkItem2(0x101, 1, lambda_226A)

    def lambda_227C():

        label("loc_227C")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_227C")

    QueueWorkItem2(0x102, 1, lambda_227C)

    def lambda_228E():

        label("loc_228E")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_228E")

    QueueWorkItem2(0x103, 1, lambda_228E)

    def lambda_22A0():

        label("loc_22A0")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_22A0")

    QueueWorkItem2(0x104, 1, lambda_22A0)

    def lambda_22B2():

        label("loc_22B2")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_22B2")

    QueueWorkItem2(0x109, 1, lambda_22B2)

    def lambda_22C4():

        label("loc_22C4")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_22C4")

    QueueWorkItem2(0x105, 1, lambda_22C4)
    OP_95(0xE, -163200, 50, -3580, 4000, 0x0)
    Sound(454, 0, 100, 0)
    OP_71(0x5, 0xF1, 0x10E, 0x1, 0x8)
    Sleep(1500)
    OP_93(0xE, 0x10E, 0x1F4)
    OP_6F(0x79)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7453", 0)
    BeginChrThread(0xF, 1, 0, 31)
    Sleep(200)
    Sound(948, 0, 80, 0)
    WaitChrThread(0xF, 1)
    BeginChrThread(0xF, 1, 0, 32)
    BeginChrThread(0x1D, 1, 0, 24)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0x10, 1, 0, 31)
    WaitChrThread(0x10, 1)
    BeginChrThread(0x10, 1, 0, 33)
    OP_68(-169280, 1250, -6210, 3000)
    MoveCamera(25, 30, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(21690, 3000)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x25)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)
    Sleep(200)
    BeginChrThread(0x11, 1, 0, 31)
    WaitChrThread(0x11, 1)
    BeginChrThread(0x11, 1, 0, 34)
    BeginChrThread(0x12, 1, 0, 31)
    WaitChrThread(0x12, 1)
    BeginChrThread(0x12, 1, 0, 35)
    BeginChrThread(0x13, 1, 0, 31)
    WaitChrThread(0x13, 1)
    BeginChrThread(0x13, 1, 0, 36)

    def lambda_2498():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2498)

    def lambda_24A5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_24A5)

    def lambda_24B2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_24B2)

    def lambda_24BF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_24BF)

    def lambda_24CC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_24CC)

    def lambda_24D9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_24D9)
    WaitChrThread(0x13, 1)
    OP_6F(0x79)
    EndChrThread(0x1D, 0x1)
    Sound(911, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2578")

    #C0012
    ChrTalk(
        0x109,
        "#10107F#11Pこ、これは……！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#00310F赤い星座のクーガーか……！\x02\x03",

            "#00307F気をつけろ、\x01",
            "この数は油断できねえぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260C")

    label("loc_2578")


    #C0014
    ChrTalk(
        0x109,
        "#10107F#11Pこ、これは……！？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#00310F赤い星座のクーガー……\x01",
            "叔父貴どもと繋がってやがったか！\x02\x03",

            "#00307F気をつけろ、この数は油断できねえぞ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260C")


    #C0016
    ChrTalk(
        0xE,
        (
            "クハハハッ……\x01",
            "食われろ、食われてしまえっ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x105,
        "#10307F……来るよ！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#00007F迎え撃つぞ！！\x02",
    )

    CloseMessageWindow()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_478", 0x30200011, 0x0, 0x100, 0x9, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x4, "event/ev15102.eff")
    LoadEffect(0x5, "event/evwarp.eff")
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -159400, 2150, 2080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x4, 0x8)
    SetChrPos(0x8, -177440, 0, -7510, 0)
    OP_D5(0x8, 0x0, 0xFE74, 0x0, 0x0)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x5, 0x9)
    SetChrPos(0x9, -160890, 0, 880, 0)
    OP_D5(0x9, 0x0, 0xD836, 0x0, 0x0)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    LoadChrToIndex("chr/ch45200.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch02950.itc", 0x23)
    LoadChrToIndex("chr/ch03050.itc", 0x24)
    LoadChrToIndex("chr/ch03500.itc", 0x25)
    LoadChrToIndex("chr/ch43100.itc", 0x26)
    LoadChrToIndex("chr/ch43300.itc", 0x27)
    LoadChrToIndex("chr/ch43200.itc", 0x28)
    LoadChrToIndex("apl/ch51546.itc", 0x29)
    LoadChrToIndex("apl/ch51544.itc", 0x2A)
    LoadChrToIndex("chr/ch00051.itc", 0x2B)
    LoadChrToIndex("chr/ch00151.itc", 0x2C)
    LoadChrToIndex("chr/ch00251.itc", 0x2D)
    LoadChrToIndex("chr/ch00351.itc", 0x2E)
    LoadChrToIndex("chr/ch02951.itc", 0x2F)
    LoadChrToIndex("chr/ch03051.itc", 0x30)
    SoundLoad(3893)
    SoundLoad(868)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    OP_68(-168010, 1250, -6300, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16780, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, -169400, 50, -6500, 90)
    SetChrPos(0x102, -169300, 50, -7900, 135)
    SetChrPos(0x104, -169300, 50, -5100, 45)
    SetChrPos(0x109, -171200, 50, -6500, 225)
    SetChrPos(0x103, -171000, 50, -7900, 45)
    SetChrPos(0x105, -171000, 50, -5100, 270)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -164500, 50, -6100, 270)
    SetChrChipByIndex(0x14, 0x2A)
    SetChrSubChip(0x14, 0x0)
    SetChrPos(0x14, -167950, 0, -11810, 0)
    PlayBGM("ed7111", 0)
    BeginChrThread(0x1D, 2, 0, 25)
    Sound(868, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0019
    ChrTalk(
        0x101,
        "#00006Fふう、やったか……！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    def lambda_29CC():
        TurnDirection(0x101, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29CC)
    Sleep(50)

    def lambda_29DC():
        TurnDirection(0x102, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_29DC)
    Sleep(50)

    def lambda_29EC():
        TurnDirection(0x104, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_29EC)
    Sleep(50)

    def lambda_29FC():
        TurnDirection(0x103, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_29FC)
    Sleep(50)

    def lambda_2A0C():
        TurnDirection(0x105, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2A0C)
    Sleep(50)

    def lambda_2A1C():
        TurnDirection(0x109, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A1C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)

    #C0020
    ChrTalk(
        0xE,
        (
            "バ……バカな……\x01",
            "バカなあああああ……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "猟兵の使役する魔獣だぞ！？\x01",
            "自治州の警察ごときに……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x105,
        "#10302Fフフ、見くびってもらっちゃ困るね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2B76")

    #C0023
    ChrTalk(
        0x104,
        (
            "#00304Fま、猟兵の魔獣だからって\x01",
            "素人に使いこなせるモンじゃ\x01",
            "ねぇってこった。\x02\x03",

            "#00301Fあきらめてお縄に付くんだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C2E")

    label("loc_2B76")


    #C0024
    ChrTalk(
        0x104,
        (
            "#00304Fどうやら、叔父貴どもの\x01",
            "御用商人の一人だったみてぇだが……\x02\x03",

            "#00300Fま、猟兵の魔獣だからって\x01",
            "素人に使いこなせるモンじゃ\x01",
            "ねぇってこった。\x02\x03",

            "#00301Fあきらめてお縄に付くんだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2E")


    #C0025
    ChrTalk(
        0xE,
        "う……うぐぐぅ…………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x29)
    SetChrSubChip(0xE, 0x0)
    OP_0D()

    #C0026
    ChrTalk(
        0x103,
        (
            "#00203F《赤い星座》との関係は取り調べで\x01",
            "みっちりと喋ってもらいましょう。\x02\x03",

            "#00200F姿を消した彼らについて\x01",
            "なにか情報が得られるかもしれませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#00306Fあー、そいつはあんまし\x01",
            "期待できねえかもな。\x02\x03",

            "#00301F所詮は取引相手ってだけだろうし……\x01",
            "ロクな情報は持ってねえと思うぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#00003Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#00105Fそれにしても……\x01",
            "さっき運搬車を止めたのは\x01",
            "なんだったのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        (
            "#10105Fそうですね……\x02\x03",

            "何か槍のような物が\x01",
            "飛んできたように見えましたけど。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -153500, 6050, 3990, 225)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -152000, 6050, 6500, 225)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -153500, 6050, 6500, 225)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -155000, 6050, 6500, 225)
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x101,
        "#00001F……みんな、気をつけろ。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        "#00105Fえっ……？\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    #N0033
    NpcTalk(
        0xA,
        "？？？",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3893V#30Wフフ、流石に気付かれましたか。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF35)
    OP_C9(0x1, 0x80000000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7580", 0)
    EndChrThread(0x1D, 0x2)
    BeginChrThread(0x1D, 2, 0, 26)
    OP_68(-151950, 6050, 4880, 5000)
    MoveCamera(19, 32, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(18780, 5000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    def lambda_2F9F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2F9F)
    Sleep(10)

    def lambda_2FAF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2FAF)
    Sleep(30)

    def lambda_2FBF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2FBF)
    Sleep(10)

    def lambda_2FCF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2FCF)
    Sleep(10)

    def lambda_2FDF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2FDF)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0034
    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "あの数の魔獣を退ける程度の\x01",
            "実力は備えていたようですね。\x02\x03",

            "湿地帯で出会った時よりは\x01",
            "着実に力を増している……\x02\x03",

            "力添えをする必要も\x01",
            "無かったかもしれません。\x02",
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
    Fade(500)
    OP_68(-153340, 3650, 1560, 0)
    MoveCamera(29, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26890, 0)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xD, 0xB4, 0x0)

    def lambda_3150():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3150)

    def lambda_315D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_315D)

    def lambda_316A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_316A)

    def lambda_3177():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3177)

    def lambda_3184():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3184)

    def lambda_3191():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3191)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2D)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2F)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x30)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x103, 0x1000)
    SetChrFlags(0x104, 0x1000)
    SetChrFlags(0x109, 0x1000)
    SetChrFlags(0x105, 0x1000)
    SetChrPos(0x101, -159820, 0, -12540, 45)
    SetChrPos(0x102, -158320, 0, -12540, 45)
    SetChrPos(0x104, -161320, 0, -12540, 45)
    SetChrPos(0x109, -159820, 0, -14540, 45)
    SetChrPos(0x103, -158320, 0, -14540, 45)
    SetChrPos(0x105, -161320, 0, -14540, 45)
    OP_0D()

    def lambda_3253():
        OP_95(0xFE, -152130, 0, -270, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3253)

    def lambda_326D():
        OP_95(0xFE, -150960, 0, -470, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_326D)

    def lambda_3287():
        OP_95(0xFE, -153660, 0, -470, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3287)

    def lambda_32A1():
        OP_95(0xFE, -152130, 0, -2970, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_32A1)

    def lambda_32BB():
        OP_95(0xFE, -150960, 0, -2670, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_32BB)

    def lambda_32D5():
        OP_95(0xFE, -153660, 0, -2670, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_32D5)
    WaitChrThread(0x101, 1)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)

    def lambda_3301():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3301)
    WaitChrThread(0x102, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)

    def lambda_3320():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3320)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)

    def lambda_3339():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3339)
    WaitChrThread(0x109, 1)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)

    def lambda_3352():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3352)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)

    def lambda_336B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_336B)
    WaitChrThread(0x105, 1)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x0)

    def lambda_3384():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3384)
    WaitChrThread(0x105, 1)

    #C0035
    ChrTalk(
        0x109,
        "#10107Fあ、あれは……湿地帯にいた！？\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        "#00201Fでは、さっき飛んできた槍は……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#00003F《鋼の聖女》アリアンロード……\x01",
            "確か、そう呼ばれていたな。\x02\x03",

            "#00013F……一体、何が目的だ？\x01",
            "何故俺たちを助けるような真似をする？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-148790, 3050, 8370, 30000)
    MoveCamera(51, 26, 0, 30000)
    OP_6E(600, 30000)
    SetCameraDistance(25170, 30000)

    #C0038
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900F……そこにいる者が\x01",
            "我が流儀に反していたからです。\x02\x03",

            "戦の世であれば、己が命を繋げるために\x01",
            "時として罪を犯すこともあるでしょう。\x02\x03",

            "ですが傷付きし者たちへの善意を\x01",
            "ただ掠め取ろうとするなど言語道断。\x02\x03",

            "流儀も、矜持も、覚悟すらもない……\x01",
            "そのような下種な振る舞いを\x01",
            "まかり通らせる訳にはいきません。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#00105Fそ、それじゃあ……\x01",
            "ミンネスの犯罪を止める為に……？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x105,
        (
            "#10302Fへえ……\x01",
            "怪しげな秘密結社の人間が\x01",
            "よくそんな事を言えたものだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#04900Fどのように捉えてもらっても。\x02\x03",

            "──次に見#2Rまみ#える時までに\x01",
            "一層、精進するがいいでしょう。\x02\x03",

            "我が槍の一閃の前に\x01",
            "儚く散りたくないのであれば。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(3894, 255, 100, 0)    #voice#Arianrhod
    Sleep(1500)
    BeginChrThread(0x1D, 1, 0, 27)
    PlayEffect(0x5, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3742():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3742)
    Sleep(600)
    PlayEffect(0x5, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_378D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_378D)
    Sleep(50)
    PlayEffect(0x5, 0xFF, 0xC, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_37D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_37D8)
    Sleep(50)
    PlayEffect(0x5, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3823():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3823)
    Sleep(1200)
    StopBGM(0x1388)
    OP_68(-151980, 550, -460, 3000)
    MoveCamera(38, 28, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(21150, 3000)
    OP_6F(0x79)

    #C0042
    ChrTalk(
        0x101,
        "#00006F……行ったみたいだな。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    def lambda_38BC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38BC)

    def lambda_38C9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_38C9)

    def lambda_38D6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_38D6)

    def lambda_38E3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_38E3)

    def lambda_38F0():
        OP_93(0xFE, 0x140, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_38F0)

    def lambda_38FD():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_38FD)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x104,
        (
            "#00306Fマジでこのためだけに\x01",
            "姿を現したみてぇだな……\x02\x03",

            "#00301Fったく……\x01",
            "本当にどういう連中なんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        (
            "#00201Fいずれにせよ、\x01",
            "《結社》については今後も\x01",
            "警戒する必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        (
            "#10306F#6P確かにね……\x01",
            "色々と得体の知れない\x01",
            "連中みたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#00103F……ねえ、ロイド。\x01",
            "ひとまずミンネスを連行しましょう？\x02\x03",

            "#00100Fずっとここで\x01",
            "考えていても仕方ないでしょうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#00003F……ああ、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x109,
        (
            "#10100F#12P念の為、警備隊に\x01",
            "応援を頼んでみましょうか。\x02\x03",

            "厳戒態勢中ですが、\x01",
            "護送車くらいなら\x01",
            "回してもらえると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#00000Fああ、それがいいかもな。\x01",
            "連絡をたのむよ、ノエル。\x02",
        )
    )

    CloseMessageWindow()
    StopSound(868, 1000, 15)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは\x01",
            "駆けつけた護送車と共に\x01",
            "ミンネスを連行し……\x02",
        )
    )

    CloseMessageWindow()

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "事の顛末をクロスベル空港で待つ\x01",
            "ビリーとリカルドに伝えた。\x02",
        )
    )

    CloseMessageWindow()

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ビリーと共に\x01",
            "ウルスラ病院に赴くのだった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_1A67 end

    def Function_24_3C3E(): pass

    label("Function_24_3C3E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C57")
    Sound(845, 0, 100, 0)
    Sleep(500)
    Jump("Function_24_3C3E")

    label("loc_3C57")

    Return()

    # Function_24_3C3E end

    def Function_25_3C58(): pass

    label("Function_25_3C58")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C7A")
    Sound(203, 0, 15, 0)
    Sleep(800)
    Sound(203, 0, 10, 0)
    Sleep(1000)
    Jump("Function_25_3C58")

    label("loc_3C7A")

    Return()

    # Function_25_3C58 end

    def Function_26_3C7B(): pass

    label("Function_26_3C7B")

    Sleep(800)
    Sound(203, 0, 5, 0)
    Sleep(800)
    Sound(203, 0, 5, 0)
    Return()

    # Function_26_3C7B end

    def Function_27_3C8E(): pass

    label("Function_27_3C8E")

    Sound(223, 0, 50, 0)
    Sleep(500)
    Sound(936, 0, 90, 0)
    Sleep(600)
    Sound(936, 0, 60, 0)
    Return()

    # Function_27_3C8E end

    def Function_28_3CA7(): pass

    label("Function_28_3CA7")

    SetChrPos(0xFE, -222580, 0, -26430, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -222580, 0, -26430)
    OP_9F(0x1, -211600, 0, -21900)
    OP_9F(0x1, -197960, 0, -16980)
    OP_9F(0x1, -163890, 0, -10880)
    OP_9F(0x2, 0xFE, 10200, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -162890, 0, -9880)
    OP_9F(0x1, -160890, 0, 880)
    OP_9F(0x2, 0xFE, 10500, 0x6)
    Return()

    # Function_28_3CA7 end

    def Function_29_3D27(): pass

    label("Function_29_3D27")

    SetChrPos(0xFE, -228580, 0, -26430, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -228580, 0, -26430)
    OP_9F(0x1, -211600, 0, -21900)
    OP_9F(0x1, -197960, 0, -16980)
    OP_9F(0x1, -171890, 0, -10880)
    OP_9F(0x2, 0xFE, 10600, 0x6)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -171890, 0, -10880)
    OP_9F(0x1, -169000, 0, -8200)
    OP_9F(0x1, -160890, 0, 880)
    OP_9F(0x2, 0xFE, 8000, 0x6)
    Return()

    # Function_29_3D27 end

    def Function_30_3DB5(): pass

    label("Function_30_3DB5")

    SetChrPos(0xFE, -188460, 50, -12620, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -188460, 50, -12620)
    OP_9F(0x1, -177440, 50, -7510)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_30_3DB5 end

    def Function_31_3DF0(): pass

    label("Function_31_3DF0")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x8000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -163420, 550, -1890, 220)

    def lambda_3E1B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E1B)
    Sound(809, 0, 60, 0)
    OP_9D(0xFE, 0xFFFD7C4A, 0x0, 0xFFFFF25E, 0x2BC, 0x7D0)
    Sound(30, 0, 100, 0)
    Sound(48, 0, 100, 0)
    Return()

    # Function_31_3DF0 end

    def Function_32_3E51(): pass

    label("Function_32_3E51")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_95(0xFE, -166160, 0, -9990, 4000, 0x0)
    OP_95(0xFE, -170080, 50, -10770, 4000, 0x0)
    OP_95(0xFE, -173280, 50, -9200, 4000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_3E51 end

    def Function_33_3EA3(): pass

    label("Function_33_3EA3")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_95(0xFE, -166910, 50, -1870, 4000, 0x0)
    OP_95(0xFE, -169250, 50, -1610, 4000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_3EA3 end

    def Function_34_3EE1(): pass

    label("Function_34_3EE1")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_95(0xFE, -166160, 0, -9990, 4000, 0x0)
    OP_95(0xFE, -169960, 50, -10200, 4000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_3EE1 end

    def Function_35_3F1F(): pass

    label("Function_35_3F1F")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_95(0xFE, -166010, 50, -7030, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_3F1F end

    def Function_36_3F49(): pass

    label("Function_36_3F49")

    BeginChrThread(0xFE, 0, 0, 37)
    OP_95(0xFE, -166150, 50, -3370, 4000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_3F49 end

    def Function_37_3F73(): pass

    label("Function_37_3F73")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F7E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F9A")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("loc_3F7E")

    label("loc_3F9A")

    Return()

    # Function_37_3F73 end

    SaveToFile()

Try(main)
