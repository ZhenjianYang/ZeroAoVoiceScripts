from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m0202.bin",                # FileName
        "m0202",                    # MapName
        "m0202",                    # Location
        0x00A7,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 167, 0, 2, 0, 3],
    )

    BuildStringList((
        "m0202",                  # 0
        "火焰橡皮怪",             # 1
        "火焰橡皮怪",             # 2
        "bm0200",                 # 3
        "bm0200",                 # 4
        "bm0200",                 # 5
        "bm0200",                 # 6
        "bm0200",                 # 7
    ))

    ATBonus("ATBonus_354", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1B5F", 8,   6,   10,  4,   4,   4,   4)
    Sepith("Sepith_1B57", 6,   6,   0,   14,  4,   4,   6)
    Sepith("Sepith_1B4F", 2,   0,   20,  2,   4,   5,   2)

    MonsterBattlePostion("MonsterBattlePostion_3B4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_418", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_41C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_420", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_424", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_428", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_42C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_394", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 2, 13, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_5C4", 0x0000, 74, 6, 60, 6, 1, 30, 0, "bm0200", "Sepith_1B5F", 40, 30, 20, 10,
        (
            ("ms84900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_414", "ed7450", "ed7453", "ATBonus_354"),
            ("ms84900.dat", "ms84900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_394", "MonsterBattlePostion_414", "ed7450", "ed7453", "ATBonus_354"),
            ("ms84900.dat", "ms84900.dat", "ms84900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_414", "ed7450", "ed7453", "ATBonus_354"),
            ("ms84900.dat", "ms84900.dat", "ms84900.dat", "ms84900.dat", 0, 0, 0, 0, "MonsterBattlePostion_394", "MonsterBattlePostion_414", "ed7450", "ed7453", "ATBonus_354"),
        )
    )

    BattleInfo(
        "BattleInfo_4FC", 0x0000, 74, 6, 60, 6, 1, 30, 0, "bm0200", "Sepith_1B57", 40, 30, 20, 10,
        (
            ("ms79000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_414", "ed7450", "ed7453", "ATBonus_354"),
            ("ms79000.dat", "ms79000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_394", "MonsterBattlePostion_414", "ed7450", "ed7453", "ATBonus_354"),
            ("ms79000.dat", "ms79000.dat", "ms79000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_414", "ed7450", "ed7453", "ATBonus_354"),
            ("ms79000.dat", "ms79000.dat", "ms79000.dat", "ms79000.dat", 0, 0, 0, 0, "MonsterBattlePostion_394", "MonsterBattlePostion_414", "ed7450", "ed7453", "ATBonus_354"),
        )
    )

    BattleInfo(
        "BattleInfo_434", 0x0000, 74, 6, 60, 6, 1, 30, 0, "bm0200", "Sepith_1B4F", 40, 30, 20, 10,
        (
            ("ms84800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_414", "ed7450", "ed7453", "ATBonus_354"),
            ("ms84800.dat", "ms84800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_394", "MonsterBattlePostion_414", "ed7450", "ed7453", "ATBonus_354"),
            ("ms84800.dat", "ms84800.dat", "ms84800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3B4", "MonsterBattlePostion_414", "ed7450", "ed7453", "ATBonus_354"),
            ("ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", 0, 0, 0, 0, "MonsterBattlePostion_394", "MonsterBattlePostion_414", "ed7450", "ed7453", "ATBonus_354"),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_68C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm0200", 0x00000000, 100, 0, 0, 0,
        (
            ("ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", "MonsterBattlePostion_394", "MonsterBattlePostion_414", "ed7451", "ed7453", "ATBonus_354"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6D0", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm0200", 0x00000000, 100, 0, 0, 0,
        (
            ("ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", "ms84800.dat", "MonsterBattlePostion_394", "MonsterBattlePostion_414", "ed7451", "ed7453", "ATBonus_354"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch84850.itc",               # 10
        "monster/ch84850.itc",               # 11
        "monster/ch79050.itc",               # 12
        "monster/ch79050.itc",               # 13
        "monster/ch84950.itc",               # 14
        "monster/ch84951.itc",               # 15
    ))

    DeclNpc(0,       500,     -505000, 0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-206000, 500,     -318000, 0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-4530,   -206720, -4000,   0x101002D,    "BattleInfo_5C4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-210120, -207240, -16000,  0x101002D,    "BattleInfo_4FC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-202090, -186250, -16000,  0x10100A0,    "BattleInfo_434", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-202730, -181970, -16000,  0x10100A9,    "BattleInfo_434", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-200080, -191790, -8000,   0x1010164,    "BattleInfo_5C4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-203880, -207710, -8000,   0x101013B,    "BattleInfo_434", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-184710, -191950, -8000,   0x1010113,    "BattleInfo_4FC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-198380, -318250, 0,       0x1010144,    "BattleInfo_5C4", 0,   20,  0xFFFF, 4,  5)

    DeclActor(6000,    0,       -8500,   1200,    6000,    1000,    -8500,   0x007C, 0,  10, 0x0000)
    DeclActor(-208500, 0,       -598000, 1200,    -208500, 1000,    -598000, 0x007C, 0,  12, 0x0000)
    DeclActor(-196700, -16000,  -207800, 2000,    -196700, -15000,  -207800, 0x007C, 0,  8,  0x0000)
    DeclActor(-197800, 0,       -335800, 2000,    -197800, 1000,    -335800, 0x007C, 0,  9,  0x0000)
    DeclActor(0,       0,       -505000, 1200,    0,       1000,    -505000, 0x007C, 0,  4,  0x0000)
    DeclActor(-182000, -8000,   -194000, 1200,    -182000, -7000,   -194000, 0x007C, 0,  5,  0x0000)
    DeclActor(-206000, 0,       -318000, 1200,    -206000, 1000,    -318000, 0x007C, 0,  6,  0x0000)
    DeclActor(-200000, -8000,   -3000,   1200,    -200000, -7000,   -3000,   0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 5

    ScpFunction((
        "Function_0_794",          # 00, 0
        "Function_1_7B0",          # 01, 1
        "Function_2_7CC",          # 02, 2
        "Function_3_7FB",          # 03, 3
        "Function_4_A50",          # 04, 4
        "Function_5_C4E",          # 05, 5
        "Function_6_D89",          # 06, 6
        "Function_7_1194",         # 07, 7
        "Function_8_12FB",         # 08, 8
        "Function_9_146A",         # 09, 9
        "Function_10_15D9",        # 0A, 10
        "Function_11_1750",        # 0B, 11
        "Function_12_1880",        # 0C, 12
        "Function_13_19F7",        # 0D, 13
    ))


    def Function_0_794(): pass

    label("Function_0_794")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AF")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_794")

    label("loc_7AF")

    Return()

    # Function_0_794 end

    def Function_1_7B0(): pass

    label("Function_1_7B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7CB")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_7B0")

    label("loc_7CB")

    Return()

    # Function_1_7B0 end

    def Function_2_7CC(): pass

    label("Function_2_7CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E3")
    Event(0, 11)

    label("loc_7E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FA")
    Event(0, 13)

    label("loc_7FA")

    Return()

    # Function_2_7CC end

    def Function_3_7FB(): pass

    label("Function_3_7FB")

    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83F")
    SetMapObjFrame(0xA, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0xA, "Null_color2", 0x0, 0x1)
    Jump("loc_864")

    label("loc_83F")

    SetMapObjFrame(0xA, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0xA, "Null_color2", 0x1, 0x1)

    label("loc_864")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A2")
    SetMapObjFrame(0xB, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0xB, "Null_color2", 0x0, 0x1)
    Jump("loc_8C7")

    label("loc_8A2")

    SetMapObjFrame(0xB, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0xB, "Null_color2", 0x1, 0x1)

    label("loc_8C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 1)), scpexpr(EXPR_END)), "loc_902")
    SetMapObjFrame(0xC, "lock_g", 0x1, 0x1)
    SetMapObjFrame(0xC, "lock_r", 0x0, 0x1)
    SetMapObjFrame(0xFF, "Null_gm01", 0x2, "off")
    Jump("loc_950")

    label("loc_902")

    SetMapObjFrame(0xC, "lock_g", 0x0, 0x1)
    SetMapObjFrame(0xC, "lock_r", 0x1, 0x1)
    SetMapObjFrame(0xFF, "Null_gm01", 0x2, "on")
    OP_C3(0x0, 0x1, 0x3, 0x1F4, 0x0, 0x2, -198000, -17000, -174000, -206000, -15000, -190000)

    label("loc_950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 2)), scpexpr(EXPR_END)), "loc_98B")
    SetMapObjFrame(0xD, "lock_g", 0x1, 0x1)
    SetMapObjFrame(0xD, "lock_r", 0x0, 0x1)
    SetMapObjFrame(0xFF, "Null_gm02", 0x2, "off")
    Jump("loc_9D9")

    label("loc_98B")

    SetMapObjFrame(0xD, "lock_g", 0x0, 0x1)
    SetMapObjFrame(0xD, "lock_r", 0x1, 0x1)
    SetMapObjFrame(0xFF, "Null_gm02", 0x2, "on")
    OP_C3(0x1, 0x1, 0x3, 0x3E8, 0x0, 0x2, -200500, -1000, -314500, -208500, 1000, -322500)

    label("loc_9D9")

    LoadEffect(0x11, "eff\\\\trapdmg1.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A00")
    OP_70(0x0, 0x0)
    Jump("loc_A04")

    label("loc_A00")

    OP_70(0x0, 0x1E)

    label("loc_A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A17")
    OP_70(0x1, 0x0)
    Jump("loc_A1B")

    label("loc_A17")

    OP_70(0x1, 0x1E)

    label("loc_A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2E")
    OP_70(0x2, 0x0)
    Jump("loc_A32")

    label("loc_A2E")

    OP_70(0x2, 0x1E)

    label("loc_A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A45")
    OP_70(0xE, 0x0)
    Jump("loc_A49")

    label("loc_A45")

    OP_70(0xE, 0x1E)

    label("loc_A49")

    Sound(133, 1, 100, 0)
    Return()

    # Function_3_7FB end

    def Function_4_A50(): pass

    label("Function_4_A50")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C10")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x207, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4D")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_AAD():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AAD)

    def lambda_AC7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AC7)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_68C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_B2E"),
        (2, "loc_B3D"),
        (1, "loc_B4A"),
        (SWITCH_DEFAULT, "loc_B4D"),
    )


    label("loc_B2E")

    SetScenarioFlags(0x207, 2)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_B4D")

    label("loc_B3D")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_B4A")

    OP_B9(0x0)
    Return()

    label("loc_B4D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('美臭', 1)"), scpexpr(EXPR_END)), "loc_BA4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_C0B")

    label("loc_BA4")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0xB5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0xB5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C0B")

    Jump("loc_C42")

    label("loc_C10")

    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_C42")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_A50 end

    def Function_5_C4E(): pass

    label("Function_5_C4E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D40")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('月亮灵摆', 1)"), scpexpr(EXPR_END)), "loc_CD1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x48),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_D3B")

    label("loc_CD1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x48),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x48),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D3B")

    Jump("loc_D7D")

    label("loc_D40")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_D7D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_C4E end

    def Function_6_D89(): pass

    label("Function_6_D89")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小丑', 0x4)"), scpexpr(EXPR_END)), "loc_F96")
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F54")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E91")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_DF1():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_DF1)

    def lambda_E0B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E0B)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x9, 1)
    Battle("BattleInfo_6D0", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_E72"),
        (2, "loc_E81"),
        (1, "loc_E8E"),
        (SWITCH_DEFAULT, "loc_E91"),
    )


    label("loc_E72")

    SetScenarioFlags(0x217, 7)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_E91")

    label("loc_E81")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_E8E")

    OP_B9(0x0)
    Return()

    label("loc_E91")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('琥耀珠', 1)"), scpexpr(EXPR_END)), "loc_EE8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x73),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_F4F")

    label("loc_EE8")

    FadeToDark(300, 0, 100)

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x73),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x73),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F4F")

    Jump("loc_F86")

    label("loc_F54")

    FadeToDark(300, 0, 100)

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_F86")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Jump("loc_1193")

    label("loc_F96")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1156")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1093")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_FF3():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FF3)

    def lambda_100D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_100D)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x9, 1)
    Battle("BattleInfo_6D0", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1074"),
        (2, "loc_1083"),
        (1, "loc_1090"),
        (SWITCH_DEFAULT, "loc_1093"),
    )


    label("loc_1074")

    SetScenarioFlags(0x217, 7)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_1093")

    label("loc_1083")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1090")

    OP_B9(0x0)
    Return()

    label("loc_1093")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('小丑', 1)"), scpexpr(EXPR_END)), "loc_10EA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xEA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1151")

    label("loc_10EA")

    FadeToDark(300, 0, 100)

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0xEA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0xEA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1151")

    Jump("loc_1188")

    label("loc_1156")

    FadeToDark(300, 0, 100)

    #A0015
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1188")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)

    label("loc_1193")

    Return()

    # Function_6_D89 end

    def Function_7_1194(): pass

    label("Function_7_1194")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CC")
    Sound(14, 0, 100, 0)
    OP_74(0xE, 0x1E)
    OP_71(0xE, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xE, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 150)
    AddSepith(0x1, 150)
    AddSepith(0x2, 150)
    AddSepith(0x3, 150)
    AddSepith(0x4, 150)
    AddSepith(0x5, 150)
    AddSepith(0x6, 150)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×１５０\x01\x07\x02",

            "#57I水之耀晶片×１５０\x01\x07\x02",

            "#58I火之耀晶片×１５０\x01\x07\x02",

            "#59I风之耀晶片×１５０\x01\x07\x02",

            "#60I时之耀晶片×１５０\x01\x07\x02",

            "#61I空之耀晶片×１５０\x01\x07\x02",

            "#62I幻之耀晶片×１５０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1FC, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_12E9")

    label("loc_12CC")


    #A0017
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_12E9")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1194 end

    def Function_8_12FB(): pass

    label("Function_8_12FB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 1)), scpexpr(EXPR_END)), "loc_1334")
    TalkBegin(0xFF)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "已经不能动了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_1469")

    label("loc_1334")

    EventBegin(0x1)

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个开关。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1462")
    Fade(500)
    OP_68(-198050, -16000, -207760, 0)
    MoveCamera(50, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    Sleep(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xC, "lock_g", 0x1, 0x1)
    SetMapObjFrame(0xC, "lock_r", 0x0, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-203640, -16000, -183780, 0)
    MoveCamera(50, 43, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    OP_0D()
    Sleep(500)
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0xFF, "Null_gm01", 0x2, "off_")
    Sleep(1000)
    SetMapObjFrame(0xFF, "Null_gm01", 0x2, "off")
    Sleep(1500)
    SetScenarioFlags(0x194, 1)
    OP_C3(0x0, 0x1, 0x0, 0x5DC, 0x0, 0x2, -198000, -17000, -174000, -206000, -15000, -190000)

    label("loc_1462")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_1469")

    Return()

    # Function_8_12FB end

    def Function_9_146A(): pass

    label("Function_9_146A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 2)), scpexpr(EXPR_END)), "loc_14A3")
    TalkBegin(0xFF)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "已经不能动了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_15D8")

    label("loc_14A3")

    EventBegin(0x1)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个开关。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D1")
    Fade(500)
    OP_68(-199050, 0, -335290, 0)
    MoveCamera(65, 38, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21500, 0)
    OP_0D()
    Sleep(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xD, "lock_g", 0x1, 0x1)
    SetMapObjFrame(0xD, "lock_r", 0x0, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-203730, 0, -317620, 0)
    MoveCamera(62, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_0D()
    Sleep(500)
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0xFF, "Null_gm02", 0x2, "off_")
    Sleep(1000)
    SetMapObjFrame(0xFF, "Null_gm02", 0x2, "off")
    Sleep(1500)
    SetScenarioFlags(0x194, 2)
    OP_C3(0x1, 0x1, 0x0, 0x5DC, 0x0, 0x2, -198000, -17000, -174000, -206000, -15000, -190000)

    label("loc_15D1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_15D8")

    Return()

    # Function_9_146A end

    def Function_10_15D9(): pass

    label("Function_10_15D9")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有可以操控升降机的控制面板。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1748")
    Fade(500)
    SetChrPos(0x0, 5500, 0, -7000, 180)
    SetChrPos(0x1, 6500, 0, -7000, 180)
    SetChrPos(0x2, 5500, 0, -6000, 180)
    SetChrPos(0x3, 6500, 0, -6000, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16A5")
    SetChrPos(0x13E, 6000, 0, -5000, 180)

    label("loc_16A5")

    OP_68(5500, 0, -5000, 0)
    MoveCamera(42, 49, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0xA, 0x1FE, 0x258, 0x0, 0x0)
    Sleep(200)
    OP_68(5500, 2500, -18000, 3800)
    MoveCamera(22, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0200", 101, 0, 0)
    IdleLoop()

    label("loc_1748")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_15D9 end

    def Function_11_1750(): pass

    label("Function_11_1750")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0xA, 0x258)
    Sleep(1)
    OP_68(3010, 4500, -16239, 0)
    MoveCamera(21, 51, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 4000, 3000, -16500, 270)
    OP_90(0x1, 4000, 3000, -17500, 270)
    OP_90(0x2, 5000, 3000, -16500, 270)
    OP_90(0x3, 5000, 3000, -17500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17FD")
    SetChrPos(0x13E, 6000, -2500, -18500, 270)

    label("loc_17FD")

    Sound(145, 0, 100, 0)
    OP_68(4300, 0, -2620, 3200)
    MoveCamera(43, 43, 0, 3200)
    OP_71(0xA, 0x258, 0x1FE, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xA)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0xA, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0xA, "Null_color2", 0x1, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_1750 end

    def Function_12_1880(): pass

    label("Function_12_1880")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有可以操控升降机的控制面板。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19EF")
    Fade(500)
    SetChrPos(0x0, -207500, 0, -598500, 270)
    SetChrPos(0x1, -207500, 0, -597500, 270)
    SetChrPos(0x2, -206500, 0, -598500, 270)
    SetChrPos(0x3, -206500, 0, -597500, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_194C")
    SetChrPos(0x13E, -205500, 0, -598000, 270)

    label("loc_194C")

    OP_68(-204030, 0, -597760, 0)
    MoveCamera(53, 52, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0xB, 0x2F8, 0x3B6, 0x0, 0x0)
    Sleep(200)
    OP_68(-217000, -2000, -598550, 3800)
    MoveCamera(62, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0209", 100, 0, 0)
    IdleLoop()

    label("loc_19EF")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_1880 end

    def Function_13_19F7(): pass

    label("Function_13_19F7")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0xB, 0x352)
    Sleep(1)
    OP_68(-216430, -2500, -599400, 0)
    MoveCamera(72, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, -218000, -2500, -600500, 180)
    OP_90(0x1, -219000, -2500, -600500, 180)
    OP_90(0x2, -218000, -2500, -599500, 180)
    OP_90(0x3, -219000, -2500, -599500, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AA4")
    SetChrPos(0x13E, -218500, -2500, -598500, 180)

    label("loc_1AA4")

    Sound(145, 0, 100, 0)
    OP_68(-203210, 0, -600870, 3200)
    MoveCamera(38, 39, 0, 3200)
    OP_71(0xB, 0x352, 0x2F8, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xB)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0xB, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0xB, "Null_color2", 0x1, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_19F7 end

    SaveToFile()

Try(main)
