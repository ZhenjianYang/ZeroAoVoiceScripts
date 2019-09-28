from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t0620.bin",                # FileName
        "t0620",                    # MapName
        "t0620",                    # Location
        0x006A,                     # MapIndex
        "ed7301",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 106, 0, 0, 0, 1],
    )

    BuildStringList((
        "t0620",                  # 0
        "bt0610",                 # 1
        "bt0610",                 # 2
        "bt0610",                 # 3
        "bt0610",                 # 4
        "bt0610",                 # 5
        "bt0610",                 # 6
        "bt0610",                 # 7
        "bt0610",                 # 8
    ))

    ATBonus("ATBonus_2CC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_123E", 10,  7,   0,   7,   9,   6,   9)
    Sepith("Sepith_1236", 0,   17,  5,   0,   12,  10,  12)
    Sepith("Sepith_122E", 7,   7,   0,   0,   9,   15,  9)
    Sepith("Sepith_1226", 13,  0,   7,   14,  0,   4,   9)

    MonsterBattlePostion("MonsterBattlePostion_30C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_31C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_390", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_394", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_398", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_39C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_32C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_340", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 8, 14, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_3AC", 0x0000, 23, 6, 45, 6, 1, 40, 0, "bt0610", "Sepith_123E", 65, 35, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_30C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_41C", 0x0000, 23, 6, 45, 6, 1, 25, 0, "bt0610", "Sepith_1236", 65, 35, 0, 0,
        (
            ("ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_30C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            ("ms60800.dat", "ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_48C", 0x0000, 23, 6, 45, 6, 1, 25, 0, "bt0610", "Sepith_122E", 65, 35, 0, 0,
        (
            ("ms65801.dat", "ms65801.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_30C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            ("ms65801.dat", "ms61701.dat", "ms65801.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4FC", 0x0000, 23, 6, 45, 6, 1, 50, 0, "bt0610", "Sepith_1226", 65, 35, 0, 0,
        (
            ("ms61701.dat", "ms61701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_30C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            ("ms61701.dat", "ms65801.dat", "ms61701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_56C", 0x0400, 23, 6, 45, 6, 1, 40, 0, "bt0610", "Sepith_123E", 65, 35, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_30C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5DC", 0x0400, 23, 6, 45, 6, 1, 25, 0, "bt0610", "Sepith_1236", 65, 35, 0, 0,
        (
            ("ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_30C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            ("ms60800.dat", "ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_64C", 0x0400, 23, 6, 45, 6, 1, 25, 0, "bt0610", "Sepith_122E", 65, 35, 0, 0,
        (
            ("ms65801.dat", "ms65801.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_30C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            ("ms65801.dat", "ms61701.dat", "ms65801.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6BC", 0x0400, 23, 6, 45, 6, 1, 50, 0, "bt0610", "Sepith_1226", 65, 35, 0, 0,
        (
            ("ms61701.dat", "ms61701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_30C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
            ("ms61701.dat", "ms65801.dat", "ms61701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_38C", "ed7400", "ed7403", "ATBonus_2CC"),
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
        "monster/ch64850.itc",               # 10
        "monster/ch64851.itc",               # 11
        "monster/ch60850.itc",               # 12
        "monster/ch60850.itc",               # 13
        "monster/ch65850.itc",               # 14
        "monster/ch65851.itc",               # 15
        "monster/ch61750.itc",               # 16
        "monster/ch61750.itc",               # 17
    ))

    DeclMonster(24880,   114060,  50,      0x1010000,    "BattleInfo_3AC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(24730,   141020,  4550,    0x1010000,    "BattleInfo_41C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(18920,   159820,  6750,    0x1010000,    "BattleInfo_48C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(29570,   162040,  6750,    0x1010000,    "BattleInfo_4FC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(61090,   190220,  7500,    0x1010000,    "BattleInfo_3AC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(91740,   195770,  9000,    0x1010000,    "BattleInfo_41C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(24880,   114060,  50,      0x1810000,    "BattleInfo_56C", 1498, 16,  0xFFFF, 0,  1)
    DeclMonster(24730,   141020,  4550,    0x1810000,    "BattleInfo_5DC", 1499, 18,  0xFFFF, 2,  3)
    DeclMonster(18920,   159820,  6750,    0x1810000,    "BattleInfo_64C", 1500, 20,  0xFFFF, 4,  5)
    DeclMonster(29570,   162040,  6750,    0x1810000,    "BattleInfo_6BC", 1501, 22,  0xFFFF, 6,  7)
    DeclMonster(61090,   190220,  7500,    0x1810000,    "BattleInfo_56C", 1502, 16,  0xFFFF, 0,  1)
    DeclMonster(91740,   195770,  9000,    0x1810000,    "BattleInfo_5DC", 1503, 18,  0xFFFF, 2,  3)

    DeclActor(-74400,  0,       126120,  1200,    -74400,  1000,    126120,  0x007C, 0,  3,  0x0000)
    DeclActor(-108460, 0,       147860,  1200,    -108460, 1000,    147860,  0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_7A4",          # 00, 0
        "Function_1_839",          # 01, 1
        "Function_2_B8A",          # 02, 2
        "Function_3_BB3",          # 03, 3
        "Function_4_CE9",          # 04, 4
        "Function_5_E1F",          # 05, 5
    ))


    def Function_0_7A4(): pass

    label("Function_0_7A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7B2")
    Jump("loc_838")

    label("loc_7B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_838")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7ED")
    ClearChrFlags(0xE, 0x80)

    label("loc_7ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FC")
    ClearChrFlags(0xF, 0x80)

    label("loc_7FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80B")
    ClearChrFlags(0x10, 0x80)

    label("loc_80B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81A")
    ClearChrFlags(0x11, 0x80)

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_829")
    ClearChrFlags(0x12, 0x80)

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_838")
    ClearChrFlags(0x13, 0x80)

    label("loc_838")

    Return()

    # Function_0_7A4 end

    def Function_1_839(): pass

    label("Function_1_839")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0C")
    OP_70(0x0, 0x0)
    Jump("loc_B10")

    label("loc_B0C")

    OP_70(0x0, 0x1E)

    label("loc_B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B23")
    OP_70(0x1, 0x0)
    Jump("loc_B27")

    label("loc_B23")

    OP_70(0x1, 0x1E)

    label("loc_B27")

    Sound(124, 1, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B86")
    Event(0, 5)

    label("loc_B86")

    Call(0, 2)
    Return()

    # Function_1_839 end

    def Function_2_B8A(): pass

    label("Function_2_B8A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BAC")
    SetMapObjFlags(0x0, 0x4)
    Jump("loc_BB2")

    label("loc_BAC")

    ClearMapObjFlags(0x0, 0x4)

    label("loc_BB2")

    Return()

    # Function_2_B8A end

    def Function_3_BB3(): pass

    label("Function_3_BB3")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA0")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('痊愈之药', 1)"), scpexpr(EXPR_END)), "loc_C32")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x114, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_C9B")

    label("loc_C32")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C9B")

    Jump("loc_CDD")

    label("loc_CA0")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
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

    label("loc_CDD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_BB3 end

    def Function_4_CE9(): pass

    label("Function_4_CE9")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD6")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('复苏药', 1)"), scpexpr(EXPR_END)), "loc_D68")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_DD1")

    label("loc_D68")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_DD1")

    Jump("loc_E13")

    label("loc_DD6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_E13")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_CE9 end

    def Function_5_E1F(): pass

    label("Function_5_E1F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(43180, 550, 128970, 0)
    MoveCamera(44, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(30730, 0)
    SetChrPos(0x101, 37520, 3000, 126230, 180)
    SetChrPos(0x102, 38800, 3000, 126340, 180)
    SetChrPos(0x103, 37750, 3000, 127850, 180)
    SetChrPos(0x104, 39090, 3000, 127870, 180)
    SetCameraDistance(29730, 3000)

    def lambda_EAD():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EAD)

    def lambda_EC7():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EC7)

    def lambda_EE1():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EE1)

    def lambda_EFB():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EFB)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_F2F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F2F)

    def lambda_F3C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F3C)

    def lambda_F49():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F49)

    def lambda_F56():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F56)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0007
    ChrTalk(
        0x101,
        (
            "#6P#0000F……看来刚才那个应该就是\x01",
            "最后一只魔兽了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        (
            "#5P#0203F嗯，应该是的。\x02\x03",

            "#0200F废坑内已经\x01",
            "感觉不到魔兽的气息了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#11P#0306F呼～终于搞定了啊。\x02\x03",

            "在这么大的一个废坑里走来走去，\x01",
            "实在累死人了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        (
            "#12P#0100F呵呵，辛苦了。\x02\x03",

            "那么，罗伊德……\x01",
            "我们快回去\x01",
            "向镇长报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#6P#0000F嗯，好的。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#11P#0306F呜……我已经走不动啦。\x02\x03",

            "#0309F……罗伊德。\x01",
            "背我到出口吧⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0013
    ChrTalk(
        0x101,
        (
            "#6P#0003F我拒绝。\x02\x03",

            "#0000F别闹了，\x01",
            "快点走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        "#11P#0306F哼，薄情鬼。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1C, 0x1, 0x4)
    SetChrName("")
    SetMessageWindowPos(-1, 40, -1, -1)

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "自动返回镇长家吗？\x07\x00",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【返回镇长家】\x01",      # 0
            "【放弃】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E2")
    StopBGM(0xFA0)
    WaitBGM()
    NewScene("t0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_11F5")

    label("loc_11E2")

    SetChrPos(0x0, 38640, 3050, 124280, 180)
    EventEnd(0x5)

    label("loc_11F5")

    Return()

    # Function_5_E1F end

    SaveToFile()

Try(main)
