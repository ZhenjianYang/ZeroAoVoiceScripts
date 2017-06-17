from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ゴーレム兵",             # 1
        "ゴーレム兵",             # 2
        "リヴィングアクス",       # 3
        "SE制御",                 # 4
        "bm1020",                 # 5
        "bm1020",                 # 6
        "bm1000",                 # 7
        "bm1020",                 # 8
    ))

    ATBonus("ATBonus_204", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_22B6", 0,   0,   14,  5,   3,   7,   6)
    Sepith("Sepith_22BE", 0,   15,  0,   6,   4,   5,   5)

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
        "BattleInfo_3BC", 0x0000, 21, 6, 60, 4, 1, 30, 0, "bm1020", "Sepith_22B6", 40, 30, 20, 10,
        (
            ("ms64600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_254", "MonsterBattlePostion_2B4", "ed7400", "ed7403", "ATBonus_204"),
            ("ms64600.dat", "ms64600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_234", "MonsterBattlePostion_2B4", "ed7400", "ed7403", "ATBonus_204"),
            ("ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_254", "MonsterBattlePostion_2B4", "ed7400", "ed7403", "ATBonus_204"),
            ("ms64600.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_234", "MonsterBattlePostion_2B4", "ed7400", "ed7403", "ATBonus_204"),
        )
    )

    BattleInfo(
        "BattleInfo_2F4", 0x0000, 21, 6, 60, 4, 1, 30, 0, "bm1020", "Sepith_22BE", 40, 30, 20, 10,
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
        "Function_4_973",          # 04, 4
        "Function_5_AC0",          # 05, 5
        "Function_6_18B0",         # 06, 6
        "Function_7_18CF",         # 07, 7
        "Function_8_18EC",         # 08, 8
        "Function_9_193E",         # 09, 9
        "Function_10_198E",        # 0A, 10
        "Function_11_19AC",        # 0B, 11
        "Function_12_19C6",        # 0C, 12
        "Function_13_19E0",        # 0D, 13
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92D")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85B")
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
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_83C"),
        (2, "loc_84B"),
        (1, "loc_858"),
        (SWITCH_DEFAULT, "loc_85B"),
    )


    label("loc_83C")

    SetScenarioFlags(0x75, 0)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_85B")

    label("loc_84B")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_858")

    OP_B7(0x0)
    Return()

    label("loc_85B")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x648, 1)"), scpexpr(EXPR_END)), "loc_8B8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x648),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11A, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_928")

    label("loc_8B8")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x648),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x648),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_928")

    Jump("loc_967")

    label("loc_92D")

    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_967")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_760 end

    def Function_4_973(): pass

    label("Function_4_973")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6F")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_9F8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11A, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_A6A")

    label("loc_9F8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A6A")

    Jump("loc_AB4")

    label("loc_A6F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_AB4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_973 end

    def Function_5_AC0(): pass

    label("Function_5_AC0")

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

    def lambda_C5F():
        OP_95(0xFE, -590, 0, -33170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C5F)

    def lambda_C79():
        OP_95(0xFE, 850, 0, -33090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C79)

    def lambda_C93():
        OP_95(0xFE, 10, 0, -35420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C93)

    def lambda_CAD():
        OP_95(0xFE, 1680, 0, -34170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CAD)

    def lambda_CC7():
        OP_95(0xFE, -580, 0, -34360, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CC7)
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
        "#0005F#6Pこれは……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#0102F#12P……すごいわね……\x01",
            "中世の建造物だそうだけど。\x02\x03",

            "あの光っているのは\x01",
            "蛍か何かかしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x109,
        (
            "#0500F#6Pうーん、そうみたいですね。\x02\x03",

            "#0506Fどうもこの塔、封鎖されてから\x01",
            "十年近く放置されてるみたいで。\x02\x03",

            "本当は、ちゃんと調査をした方が\x01",
            "いいとは思うんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        (
            "#0306F#12Pま、あの事なかれ主義の司令だ。\x02\x03",

            "提案しても予算の無駄だって\x01",
            "却下するのは目に見えてそうだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x104, 500)
    Sleep(150)

    #C0012
    ChrTalk(
        0x109,
        (
            "#0506F#6Pはあ、そうなんですよね……\x02\x03",

            "#0501F先輩、よくあんな司令の\x01",
            "下で働いていましたよね？\x02\x03",

            "あたしにはとても無理ですよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x109, 500)

    #C0013
    ChrTalk(
        0x104,
        (
            "#0309F#11Pハハ、だから俺も\x01",
            "警察なんかにいるんじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x109,
        "#0505F#6Pあ、なるほど。\x02",
    )

    CloseMessageWindow()

    def lambda_F74():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F74)
    Sleep(50)

    def lambda_F84():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F84)
    Sleep(300)

    #C0015
    ChrTalk(
        0x102,
        (
            "#0105F#5Pあら……でも。\x02\x03",

            "あなたが警備隊を辞めたのは\x01",
            "女性関係が原因じゃなかったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#0000F#5Pそういや、そんな話をしてたな。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#0305F#11Pおっと……\x01",
            "まあ、それもあるけどよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x109,
        (
            "#0503F#6Pんー、おかしいなぁ。\x02\x03",

            "#0500Fベルガード門にいる友達からは\x01",
            "ランディ先輩の浮いた話って\x01",
            "あんまり聞きませんでしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#0309F#11Pあー、色々あんだよ。\x01",
            "男と女の関係ってのはな。\x02",
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
            "#0005F#5Pどうした、ティオ？\x01",
            "何か気になるのか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1188():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1188)

    def lambda_1195():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1195)
    Sleep(50)

    def lambda_11A5():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11A5)

    def lambda_11B2():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11B2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0022
    ChrTalk(
        0x103,
        (
            "#0208F#12Pいえ……\x02\x03",

            "#0201F……どうやらこの場所は、\x01",
            "少々、変わっているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#0005F#5P変わっている……？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        "#0301F#11Pどういう事だ？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#0203F#12P地・水・火・風……\x02\x03",

            "#0201F４属性以外の上位属性が\x01",
            "働いている気配を感じます。\x02",
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
        "#0101F#5Pえっと、それって……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x109,
        "#0501F#5P導力魔法#8Rオーバルアーツ#の属性のこと？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#0203F#12P……はい。\x02\x03",

            "#0201F地・水・火・風のアーツが\x01",
            "弱点という魔獣はいますよね……？\x02\x03",

            "ですが、上位属性である\x01",
            "時・空・幻のアーツに関しては\x01",
            "強力ですが弱点の魔獣はいない……\x02\x03",

            "その法則が歪んでいる感じです。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0006F#5Pうーん……\x01",
            "よく分からないけれど。\x02\x03",

            "#0001F要するに、アーツの効き方が\x01",
            "他の場所とは違っているんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        "#0206F#12Pええ、まあ。\x02",
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

    def lambda_1569():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1569)

    def lambda_1576():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1576)
    Sleep(50)

    def lambda_1586():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1586)

    def lambda_1593():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1593)

    def lambda_15A0():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15A0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0031
    ChrTalk(
        0x101,
        "#0005F#11Pこの音は……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        "#0301F魔獣か……？\x02",
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
        "#0011F#12Pな……！？\x02",
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
        "#0507F#12Pこ、これは……！？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#0307F#12Pおいおい……\x01",
            "こいつは何の冗談だ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        "#0107F話は後よ……来るわ！\x02",
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

    # Function_5_AC0 end

    def Function_6_18B0(): pass

    label("Function_6_18B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18CE")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_6_18B0")

    label("loc_18CE")

    Return()

    # Function_6_18B0 end

    def Function_7_18CF(): pass

    label("Function_7_18CF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18EB")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_7_18CF")

    label("loc_18EB")

    Return()

    # Function_7_18CF end

    def Function_8_18EC(): pass

    label("Function_8_18EC")

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

    # Function_8_18EC end

    def Function_9_193E(): pass

    label("Function_9_193E")

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

    # Function_9_193E end

    def Function_10_198E(): pass

    label("Function_10_198E")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 7)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    Return()

    # Function_10_198E end

    def Function_11_19AC(): pass

    label("Function_11_19AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19C5")
    Sound(867, 0, 80, 0)
    Sleep(1000)
    Jump("Function_11_19AC")

    label("loc_19C5")

    Return()

    # Function_11_19AC end

    def Function_12_19C6(): pass

    label("Function_12_19C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19DF")
    Sound(867, 0, 100, 0)
    Sleep(1000)
    Jump("Function_12_19C6")

    label("loc_19DF")

    Return()

    # Function_12_19C6 end

    def Function_13_19E0(): pass

    label("Function_13_19E0")

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

    def lambda_1B74():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1B74)
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1500, 2000, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_1BC4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1BC4)
    PlayEffect(0x0, 0x1, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1500, 2000, 1500, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sleep(500)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)

    def lambda_1C23():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1C23)

    def lambda_1C34():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1C34)
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
        "#0007F#11Pな、何だ今のは……！？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        (
            "#0506F#5P明らかに普通の魔獣とは\x01",
            "違いましたね……\x02\x03",

            "#0501Fかといって人間が\x01",
            "入っていたわけでもない……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#0108F#11Pま、ま、まさか……亡霊とか？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x103,
        (
            "#0203F#11Pよく分かりませんが……\x01",
            "導力仕掛けのカラクリでは\x01",
            "無さそうですね。\x02\x03",

            "#0201F中世に魔道師が造ったという\x01",
            "ゴーレムみたいなものでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        (
            "#0306F#11Pおいおい……\x01",
            "何でそんなものが動いてんだよ。\x02\x03",

            "#0301Fひょっとしてこれも\x01",
            "《銀》の罠なんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#0003F#11P……分からない。\x02\x03",

            "#0001Fただ、さっきティオが\x01",
            "言った事は正しかったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        (
            "#0106F#11Pそうね……戦っている時、\x01",
            "今までにはない感じがしたわ。\x02\x03",

            "#0108F時・空・幻──上位三属性か。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        (
            "#0200F#11Pおそらく霊的な乱れが\x01",
            "発生しているのではないかと。\x02\x03",

            "#0206Fそれ以上の事は\x01",
            "ちょっと分かりませんが……\x02",
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
            "#0503F#5P……どうやら放置していたのは\x01",
            "完全に間違いだったみたいですね……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)
    Sleep(300)

    #C0046
    ChrTalk(
        0x109,
        (
            "#0501F#6P──行きましょう、皆さん。\x02\x03",

            "あたしとしても、この塔の中を\x01",
            "ちゃんと調べたくなってきました。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_208B():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_208B)
    Sleep(50)

    def lambda_209B():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_209B)
    Sleep(50)

    def lambda_20AB():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20AB)
    Sleep(50)

    def lambda_20BB():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20BB)
    Sleep(200)

    #C0047
    ChrTalk(
        0x101,
        (
            "#0001F#5Pああ……\x01",
            "慎重に探索を開始しよう。\x02",
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
            "中世の遺跡など特定の場所では\x01",
            "時・空・幻の三属性が働いています。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有効属性のパラメーターが増える上に\x01",
            "奇妙な効果を持つＡＴボーナスが\x01",
            "出現するようになるため注意してください。\x07\x00\x02",
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

    # Function_13_19E0 end

    SaveToFile()

Try(main)
