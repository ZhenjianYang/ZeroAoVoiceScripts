from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m1020.bin",                # FileName
        "m1020",                    # MapName
        "m1020",                    # Location
        0x006C,                     # MapIndex
        "ed7304",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, -35000, 0, 0, 1, 108, 0, 1, 0, 2],
    )

    BuildStringList((
        "m1020",                  # 0
        "傀儡士兵",               # 1
        "傀儡士兵",               # 2
        "活斧头",                 # 3
        "SE控制",                 # 4
        "bm1020",                 # 5
        "bm1020",                 # 6
        "bm1000",                 # 7
        "bm1020",                 # 8
    ))

    ATBonus("ATBonus_204", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_2104", 0,   0,   14,  5,   3,   7,   6)
    Sepith("Sepith_210C", 0,   15,  0,   6,   4,   5,   5)

    MonsterBattlePostion("MonsterBattlePostion_254", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_258", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_25C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_260", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_268", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_26C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_270", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_234", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_238", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_23C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_240", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_244", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_248", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_24C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_250", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 0, 0, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_3BC", 0x0000, 21, 6, 60, 4, 1, 30, 0, "bm1020", "Sepith_2104", 40, 30, 20, 10,
        (
            ("ms64600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_254", "MonsterBattlePostion_2B4", "ed7400", "ed7403", "ATBonus_204"),
            ("ms64600.dat", "ms64600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_234", "MonsterBattlePostion_2B4", "ed7400", "ed7403", "ATBonus_204"),
            ("ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_254", "MonsterBattlePostion_2B4", "ed7400", "ed7403", "ATBonus_204"),
            ("ms64600.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_234", "MonsterBattlePostion_2B4", "ed7400", "ed7403", "ATBonus_204"),
        )
    )

    BattleInfo(
        "BattleInfo_2F4", 0x0000, 21, 6, 60, 4, 1, 30, 0, "bm1020", "Sepith_210C", 40, 30, 20, 10,
        (
            ("ms62800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_254", "MonsterBattlePostion_2B4", "ed7400", "ed7403", "ATBonus_204"),
            ("ms62800.dat", "ms62800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_234", "MonsterBattlePostion_2B4", "ed7400", "ed7403", "ATBonus_204"),
            ("ms62800.dat", "ms64600.dat", "ms62800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_254", "MonsterBattlePostion_2B4", "ed7400", "ed7403", "ATBonus_204"),
            ("ms62800.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_234", "MonsterBattlePostion_2B4", "ed7400", "ed7403", "ATBonus_204"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_4C8", 0x0000, 21, 6, 45, 0, 1, 0, 0, "bm1020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms64600.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", "ms64600.dat", "ms62800.dat", 0, 0, "MonsterBattlePostion_234", "MonsterBattlePostion_2B4", "ed7401", "ed7403", "ATBonus_204"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_484", 0x0002, 21, 6, 45, 0, 1, 0, 0, "bm1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63300.dat", "ms63300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2D4", "MonsterBattlePostion_2B4", "ed7401", "ed7403", "ATBonus_204"),
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
        "monster/ch63350.itc",               # 10
        "monster/ch63351.itc",               # 11
        "monster/ch62850.itc",               # 12
        "monster/ch62850.itc",               # 13
        "monster/ch64650.itc",               # 14
        "monster/ch64650.itc",               # 15
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-5650,   1500,    30610,   0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-31440,  3550,    0,       0x1010000,    "BattleInfo_3BC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-620,    25220,   0,       0x1010000,    "BattleInfo_2F4", 0,   18,  0xFFFF, 2,  3)

    DeclActor(-5650,   0,       30610,   1200,    -5650,   1000,    30610,   0x007C, 0,  3,  0x0000)
    DeclActor(-18970,  0,       -2900,   1200,    -18970,  1000,    -2900,   0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5

    ScpFunction((
        "Function_0_58C",          # 00, 0
        "Function_1_5AB",          # 01, 1
        "Function_2_5D1",          # 02, 2
        "Function_3_760",          # 03, 3
        "Function_4_95A",          # 04, 4
        "Function_5_A90",          # 05, 5
        "Function_6_17E0",         # 06, 6
        "Function_7_17FF",         # 07, 7
        "Function_8_181C",         # 08, 8
        "Function_9_186E",         # 09, 9
        "Function_10_18BE",        # 0A, 10
        "Function_11_18DC",        # 0B, 11
        "Function_12_18F6",        # 0C, 12
        "Function_13_1910",        # 0D, 13
    ))


    def Function_0_58C(): pass

    label("Function_0_58C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5AA")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_58C")

    label("loc_5AA")

    Return()

    # Function_0_58C end

    def Function_1_5AB(): pass

    label("Function_1_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C1")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_5D0")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_5D0")

    Return()

    # Function_1_5AB end

    def Function_2_5D1(): pass

    label("Function_2_5D1")

    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_744")
    OP_70(0x0, 0x0)
    Jump("loc_748")

    label("loc_744")

    OP_70(0x0, 0x1E)

    label("loc_748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B")
    OP_70(0x1, 0x0)
    Jump("loc_75F")

    label("loc_75B")

    OP_70(0x1, 0x1E)

    label("loc_75F")

    Return()

    # Function_2_5D1 end

    def Function_3_760(): pass

    label("Function_3_760")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91C")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_859")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_7B9():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7B9)

    def lambda_7D3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7D3)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

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
    WaitChrThread(0xA, 1)
    Battle("BattleInfo_4C8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_83A"),
        (2, "loc_849"),
        (1, "loc_856"),
        (SWITCH_DEFAULT, "loc_859"),
    )


    label("loc_83A")

    SetScenarioFlags(0x75, 0)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_859")

    label("loc_849")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_856")

    OP_B7(0x0)
    Return()

    label("loc_859")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('白色帆布鞋', 1)"), scpexpr(EXPR_END)), "loc_8B0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '白色帆布鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11A, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_917")

    label("loc_8B0")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '白色帆布鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '白色帆布鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_917")

    Jump("loc_94E")

    label("loc_91C")

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

    label("loc_94E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_760 end

    def Function_4_95A(): pass

    label("Function_4_95A")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A47")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('复苏药', 1)"), scpexpr(EXPR_END)), "loc_9D9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11A, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_A42")

    label("loc_9D9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A42")

    Jump("loc_A84")

    label("loc_A47")

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

    label("loc_A84")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_95A end

    def Function_5_A90(): pass

    label("Function_5_A90")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00850.itc", 0x26)
    LoadChrToIndex("chr/ch00851.itc", 0x27)
    LoadChrToIndex("monster/ch63350.itc", 0x28)
    LoadChrToIndex("monster/ch63351.itc", 0x29)
    OP_68(50, -500, 570, 0)
    MoveCamera(74, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(74590, 0)
    SetChrPos(0x101, -620, 0, -38390, 0)
    SetChrPos(0x102, 650, 0, -38440, 0)
    SetChrPos(0x103, 50, 0, -40770, 0)
    SetChrPos(0x104, 1330, 0, -39600, 0)
    SetChrPos(0x109, -750, 0, -39780, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, -2600, 0, -31400, 135)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x9, 4000, 0, -30000, 225)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    MoveCamera(55, 18, 0, 10000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(170, 1600, -29170, 0)
    MoveCamera(30, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20640, 0)
    OP_68(170, 300, -29170, 3000)

    def lambda_C2F():
        OP_95(0xFE, -590, 0, -33170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C2F)

    def lambda_C49():
        OP_95(0xFE, 850, 0, -33090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C49)

    def lambda_C63():
        OP_95(0xFE, 10, 0, -35420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C63)

    def lambda_C7D():
        OP_95(0xFE, 1680, 0, -34170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C7D)

    def lambda_C97():
        OP_95(0xFE, -580, 0, -34360, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C97)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0008
    ChrTalk(
        0x101,
        "#0005F#6P这是……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#0102F#12P……好漂亮，\x01",
            "看起来像是中世纪的建筑物……\x02\x03",

            "那个发光的东西\x01",
            "是萤火虫吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x109,
        (
            "#0500F#6P嗯，好像是的。\x02\x03",

            "#0506F自从这座塔被封锁之后，\x01",
            "已经搁置了将近十年。\x02\x03",

            "虽然我始终认为，还是仔细\x01",
            "调查一下为好……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        (
            "#0306F#12P哎，没办法，毕竟那个司令从不干正事。\x02\x03",

            "能想象得到，就算向他提出建议，\x01",
            "也会以浪费预算为由，遭到驳回的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x104, 500)
    Sleep(150)

    #C0012
    ChrTalk(
        0x109,
        (
            "#0506F#6P呼，是啊……\x02\x03",

            "#0501F前辈，你曾经在那种\x01",
            "司令的手下工作，很辛苦吧？\x02\x03",

            "如果是我的话，一定办不到。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x109, 500)

    #C0013
    ChrTalk(
        0x104,
        (
            "#0309F#11P哈哈，所以我才\x01",
            "来当警察了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x109,
        "#0505F#6P啊，原来如此。\x02",
    )

    CloseMessageWindow()

    def lambda_EF0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EF0)
    Sleep(50)

    def lambda_F00():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F00)
    Sleep(300)

    #C0015
    ChrTalk(
        0x102,
        (
            "#0105F#5P哎呀……但是，\x02\x03",

            "你辞去警备队工作的原因，\x01",
            "不是和女性问题有关吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#0000F#5P说起来，以前你确实是那么说的。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#0305F#11P这个……\x01",
            "哈哈，也有那方面的原因吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x109,
        (
            "#0503F#6P嗯～好奇怪啊。\x02\x03",

            "#0500F好像很少听贝尔加德门的朋友们\x01",
            "提起过兰迪前辈朝三暮四、\x01",
            "为人轻浮之类的话题……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#0309F#11P啊～男女关系其实\x01",
            "也分为很多种的。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        "#0205F#12P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 500)

    #C0021
    ChrTalk(
        0x101,
        (
            "#0005F#5P怎么了，缇欧？\x01",
            "想到什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10D4():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10D4)

    def lambda_10E1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10E1)
    Sleep(50)

    def lambda_10F1():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10F1)

    def lambda_10FE():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10FE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0022
    ChrTalk(
        0x103,
        (
            "#0208F#12P不……\x02\x03",

            "#0201F……总觉得这个地方\x01",
            "好像稍微有些奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#0005F#5P有些奇怪……？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        "#0301F#11P怎么回事？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#0203F#12P地、水、火、风……\x02\x03",

            "#0201F除了这四种属性以外，还感觉到了其它上级属性\x01",
            "也在对这个地方产生影响。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0026
    ChrTalk(
        0x102,
        "#0101F#5P那么，所谓的属性是指……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x109,
        "#0501F#5P导力魔法的属性吗？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#0203F#12P……是的。\x02\x03",

            "#0201F地、水、火、风这四种属性的魔法，\x01",
            "是很多魔兽的弱点，对吧……？\x02\x03",

            "但是，身为上级属性的\x01",
            "时、空、幻这三种魔法，\x01",
            "虽然很强大，但却不会克制特定的魔兽……\x02\x03",

            "我感觉，在这里，这个法则似乎被扭曲了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0006F#5P嗯……\x01",
            "虽然还不太明白。\x02\x03",

            "#0001F不过，简单来说的话，就是这里的\x01",
            "魔法效果和其它地方不一样？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        "#0206F#12P嗯，差不多吧。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 1, 0, 11)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_149D():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_149D)

    def lambda_14AA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14AA)
    Sleep(50)

    def lambda_14BA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14BA)

    def lambda_14C7():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14C7)

    def lambda_14D4():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14D4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0031
    ChrTalk(
        0x101,
        "#0005F#11P这个声音是……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        "#0301F魔兽吗……？\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xB, 0x1)
    Fade(1000)
    SetChrPos(0x109, -750, 0, -34740, 315)
    SetChrPos(0x103, 510, 0, -35150, 315)
    OP_68(-11600, 1500, -20800, 0)
    MoveCamera(9, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    OP_68(-2660, 1500, -33360, 10000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -13700, 0, -19290, 135)
    SetChrPos(0x9, -15890, 0, -17160, 135)
    OP_82(0x0, 0x32, 0xBB8, 0x2328)
    BeginChrThread(0x8, 3, 0, 8)
    Sleep(50)
    BeginChrThread(0x9, 3, 0, 9)
    OP_0D()
    Sleep(3000)
    Fade(1000)
    OP_68(-2020, 1900, -33810, 0)
    OP_68(-1730, 1900, -34090, 0)
    MoveCamera(344, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16560, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0033
    ChrTalk(
        0x101,
        "#0011F#12P什么……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    OP_6F(0x1)
    Sleep(500)

    #C0034
    ChrTalk(
        0x109,
        "#0507F#12P这、这是……！？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#0307F#12P喂喂……\x01",
            "开什么玩笑！？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        "#0107F稍后再说……魔兽要过来了！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    BeginChrThread(0x8, 3, 0, 10)
    BeginChrThread(0x9, 3, 0, 10)
    SetCameraDistance(12560, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    Battle("BattleInfo_484", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    Call(0, 13)
    Return()

    # Function_5_A90 end

    def Function_6_17E0(): pass

    label("Function_6_17E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17FE")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_6_17E0")

    label("loc_17FE")

    Return()

    # Function_6_17E0 end

    def Function_7_17FF(): pass

    label("Function_7_17FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_181B")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_7_17FF")

    label("loc_181B")

    Return()

    # Function_7_17FF end

    def Function_8_181C(): pass

    label("Function_8_181C")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 7)
    BeginChrThread(0xB, 1, 0, 12)
    OP_95(0xFE, -6670, 0, -26030, 2000, 0x0)
    OP_95(0xFE, -5830, 0, -31660, 2000, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 6)
    TurnDirection(0xFE, 0x109, 500)
    Return()

    # Function_8_181C end

    def Function_9_186E(): pass

    label("Function_9_186E")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 7)
    OP_95(0xFE, -6730, 0, -26130, 2000, 0x0)
    OP_95(0xFE, -4360, 0, -29180, 2000, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    EndChrThread(0xB, 0x1)
    BeginChrThread(0xFE, 0, 0, 6)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_9_186E end

    def Function_10_18BE(): pass

    label("Function_10_18BE")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 7)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    Return()

    # Function_10_18BE end

    def Function_11_18DC(): pass

    label("Function_11_18DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18F5")
    Sound(867, 0, 80, 0)
    Sleep(1000)
    Jump("Function_11_18DC")

    label("loc_18F5")

    Return()

    # Function_11_18DC end

    def Function_12_18F6(): pass

    label("Function_12_18F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_190F")
    Sound(867, 0, 100, 0)
    Sleep(1000)
    Jump("Function_12_18F6")

    label("loc_190F")

    Return()

    # Function_12_18F6 end

    def Function_13_1910(): pass

    label("Function_13_1910")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00850.itc", 0x26)
    LoadChrToIndex("monster/ch63350.itc", 0x28)
    LoadChrToIndex("monster/ch63352.itc", 0x2A)
    OP_68(-3650, 1900, -31720, 0)
    MoveCamera(344, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16560, 0)
    SetChrPos(0x101, -590, 0, -33170, 315)
    SetChrPos(0x102, 850, 0, -33090, 315)
    SetChrPos(0x103, 510, 0, -35150, 315)
    SetChrPos(0x104, 1680, 0, -34170, 315)
    SetChrPos(0x109, -750, 0, -34740, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x8, -4520, 0, -28310, 135)
    SetChrPos(0x9, -7180, 0, -29770, 135)
    LoadEffect(0x0, "event\\ev602_00.eff")
    FadeToBright(1000, 0)
    OP_0D()
    OP_82(0x0, 0x32, 0xBB8, 0xBB8)
    SetChrFlags(0x8, 0x20)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x9, 0x20)
    EndChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)

    def lambda_1AA4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1AA4)
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1500, 2000, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_1AF4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1AF4)
    PlayEffect(0x0, 0x1, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1500, 2000, 1500, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sleep(500)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)

    def lambda_1B53():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1B53)

    def lambda_1B64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1B64)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    OP_68(-2020, 1900, -33810, 3000)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0037
    ChrTalk(
        0x101,
        "#0007F#11P刚、刚才那是什么……！？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        (
            "#0506F#5P明显和普通的魔兽\x01",
            "不一样……\x02\x03",

            "#0501F但是，里面似乎也没有\x01",
            "人类在操纵……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#0108F#11P难、难、难道是……亡灵吗？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x103,
        (
            "#0203F#11P不太清楚……\x01",
            "看起来也不像是\x01",
            "导力装置之类的机器。\x02\x03",

            "#0201F是中世纪魔法师制造的\x01",
            "类似傀儡的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        (
            "#0306F#11P喂喂……\x01",
            "那种东西为什么到现在还会动啊。\x02\x03",

            "#0301F难道说，这也是\x01",
            "『银』布下的陷阱吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#0003F#11P……不清楚。\x02\x03",

            "#0001F但是，缇欧刚才\x01",
            "说得好像没错。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        (
            "#0106F#11P是啊……战斗的时候，\x01",
            "也感到和以往不一样。\x02\x03",

            "#0108F时、空、幻──三种上级属性吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        (
            "#0200F#11P恐怕是发生了\x01",
            "灵气方面的错乱。\x02\x03",

            "#0206F除此之外，我也就\x01",
            "不太清楚了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x109)

    #C0045
    ChrTalk(
        0x109,
        (
            "#0503F#5P……看起来，放着这里不管，\x01",
            "确实是个错误……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)
    Sleep(300)

    #C0046
    ChrTalk(
        0x109,
        (
            "#0501F#6P──各位，我们走吧。\x02\x03",

            "我无论如何都想\x01",
            "好好调查一下这座塔的内部。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F01():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F01)
    Sleep(50)

    def lambda_1F11():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F11)
    Sleep(50)

    def lambda_1F21():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F21)
    Sleep(50)

    def lambda_1F31():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F31)
    Sleep(200)

    #C0047
    ChrTalk(
        0x101,
        (
            "#0001F#5P嗯……\x01",
            "慎重地开始探索吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16810, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在中世纪遗迹等特定场所，\x01",
            "时、空、幻这三种属性会产生影响。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "除了对魔兽的有效属性有所增加之外，\x01",
            "还会出现拥有奇妙效果的ＡＴ奖励，\x01",
            "请务必注意。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x20)
    OP_D5(0x22)
    OP_D5(0x24)
    OP_D5(0x26)
    OP_D5(0x28)
    OP_D5(0x2A)
    OP_37()
    OP_68(0, 1500, -35500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 0, 0, -35500, 0)
    SetChrPos(0x1, 0, 0, -35500, 0)
    SetChrPos(0x2, 0, 0, -35500, 0)
    SetChrPos(0x3, 0, 0, -35500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x84, 3)
    OP_29(0x43, 0x1, 0x9)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_13_1910 end

    SaveToFile()

Try(main)
