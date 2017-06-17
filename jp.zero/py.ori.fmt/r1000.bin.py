from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1000.bin",                # FileName
        "r1000",                    # MapName
        "r1000",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00000000,                 # Flags
        ("r1000", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 0, 0, 1],
    )

    BuildStringList((
        "r1000",                  # 0
        "バス",                   # 1
        "車00",                   # 2
        "車01",                   # 3
        "車02",                   # 4
        "車03",                   # 5
        "SE制御",                 # 6
        "br1000",                 # 7
        "br1000",                 # 8
        "br1000",                 # 9
        "br1000",                 # 10
        "br1000",                 # 11
        "クロスベル市方面",       # 12
        "ベルガード門方面",       # 13
    ))

    ATBonus("ATBonus_51C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_326A", 11,  3,   8,   0,   8,   0,   0)
    Sepith("Sepith_3272", 11,  0,   5,   7,   0,   0,   7)
    Sepith("Sepith_32B2", 4,   4,   10,  2,   0,   5,   5)
    Sepith("Sepith_32AA", 13,  13,  0,   4,   0,   0,   0)
    Sepith("Sepith_32C2", 12,  7,   4,   3,   6,   14,  7)

    MonsterBattlePostion("MonsterBattlePostion_57C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_580", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_584", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_588", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_58C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_590", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5DC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_5E0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_5E4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_5E8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_5EC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_5F0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_5F4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_55C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_560", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_564", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_568", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_56C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_570", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_574", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_578", 2, 13, 180)

    # monster count: 9

    BattleInfo(
        "BattleInfo_5FC", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_326A", 30, 40, 20, 10,
        (
            ("ms60900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms60900.dat", "ms60900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms60900.dat", "ms70400.dat", "ms60900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms60900.dat", "ms60900.dat", "ms74800.dat", "ms60900.dat", 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
        )
    )

    BattleInfo(
        "BattleInfo_6C4", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_3272", 30, 40, 20, 10,
        (
            ("ms74800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms74800.dat", "ms74800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms74800.dat", "ms70400.dat", "ms74800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms74800.dat", "ms74800.dat", "ms60900.dat", "ms74800.dat", 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
        )
    )

    BattleInfo(
        "BattleInfo_78C", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_32B2", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
        )
    )

    BattleInfo(
        "BattleInfo_854", 0x0000, 17, 6, 60, 8, 1, 30, 0, "br1000", "Sepith_32AA", 30, 40, 20, 10,
        (
            ("ms71500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms71500.dat", "ms71500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms71500.dat", "ms71900.dat", "ms71500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms71500.dat", "ms71500.dat", "ms70400.dat", "ms71500.dat", 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
        )
    )

    BattleInfo(
        "BattleInfo_91C", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br1000", "Sepith_32C2", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
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
        "monster/ch60950.itc",               # 10
        "monster/ch60951.itc",               # 11
        "monster/ch74850.itc",               # 12
        "monster/ch74851.itc",               # 13
        "monster/ch71950.itc",               # 14
        "monster/ch71950.itc",               # 15
        "monster/ch71550.itc",               # 16
        "monster/ch71551.itc",               # 17
        "monster/ch60750.itc",               # 18
        "monster/ch60750.itc",               # 19
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-36920,  25180,   -2000,   0x1010000,    "BattleInfo_5FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-27400,  39160,   -2000,   0x1010000,    "BattleInfo_6C4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-61100,  16450,   -2000,   0x1010000,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-82360,  38870,   -2000,   0x1010000,    "BattleInfo_854", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-76380,  52370,   -2000,   0x1010000,    "BattleInfo_5FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-99040,  47600,   -2000,   0x1010000,    "BattleInfo_6C4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-93520,  16270,   -2000,   0x1010000,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-30170,  11920,   -2000,   0x1010000,    "BattleInfo_91C", 0,   24,  0xFFFF, 10, 11)
    DeclMonster(-103540, 6520,    -1080,   0x1010000,    "BattleInfo_91C", 0,   24,  0xFFFF, 10, 11)

    DeclActor(-98650,  -2000,   50740,   1200,    -98650,  -1000,   50740,   0x007C, 0,  2,  0x0000)
    DeclActor(-26460,  -2000,   42260,   1200,    -26460,  -1000,   42260,   0x007C, 0,  3,  0x0000)
    DeclActor(-4330,   -2000,   5700,    1200,    -4330,   -1000,   5700,    0x007C, 0,  22, 0x0000)
    DeclActor(-100260, -1990,   14160,   1200,    -100260, -1990,   14160,   0x007C, 0,  4,  0x0000)
    DeclActor(-6170,   -2000,   11420,   1200,    -6170,   0,       11420,   0x007C, 0,  23, 0x0000)
    DeclActor(-3320,   -2000,   13000,   800,     -3320,   -500,    13020,   0x007C, 0,  11, 0x0000)
    DeclActor(-7980,   -2000,   13000,   800,     -7980,   -500,    13000,   0x007C, 0,  12, 0x0000)
    DeclActor(-10240,  -2000,   13000,   800,     -10240,  -500,    13000,   0x007C, 0,  13, 0x0000)
    DeclActor(-14600,  -2000,   12970,   800,     -14600,  -500,    12970,   0x007C, 0,  14, 0x0000)
    DeclActor(-17290,  -2000,   13580,   800,     -17290,  -500,    13580,   0x007C, 0,  15, 0x0000)
    DeclActor(-21800,  -2000,   16000,   800,     -21800,  -500,    16000,   0x007C, 0,  16, 0x0000)
    DeclActor(-24050,  -2000,   16800,   800,     -24050,  -500,    16800,   0x007C, 0,  17, 0x0000)
    DeclActor(-28160,  -2000,   17520,   800,     -28160,  -500,    17520,   0x007C, 0,  18, 0x0000)
    DeclActor(-11530,  -2000,   5320,    1500,    -11530,  -300,    5320,    0x007C, 0,  27, 0x0000)

    PlaceName(23.0, 0.0, 4.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(-137.0, 0.0, -28.0, 0x0000, 0x0000, "ベルガード門方面")
    PlaceName(-4.0, 0.0, 5.900000095367432, 0x0000, 0x0055, "")
    PlaceName(-6.400000095367432, 0.0, 13.0, 0x0000, 0x0056, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_AB8",          # 00, 0
        "Function_1_DA5",          # 01, 1
        "Function_2_146D",         # 02, 2
        "Function_3_15BA",         # 03, 3
        "Function_4_1707",         # 04, 4
        "Function_5_171B",         # 05, 5
        "Function_6_1734",         # 06, 6
        "Function_7_17EF",         # 07, 7
        "Function_8_1913",         # 08, 8
        "Function_9_19A8",         # 09, 9
        "Function_10_1F5A",        # 0A, 10
        "Function_11_2049",        # 0B, 11
        "Function_12_20AD",        # 0C, 12
        "Function_13_2126",        # 0D, 13
        "Function_14_2184",        # 0E, 14
        "Function_15_21FD",        # 0F, 15
        "Function_16_233D",        # 10, 16
        "Function_17_23B6",        # 11, 17
        "Function_18_2418",        # 12, 18
        "Function_19_2491",        # 13, 19
        "Function_20_2504",        # 14, 20
        "Function_21_2696",        # 15, 21
        "Function_22_28D0",        # 16, 22
        "Function_23_29E3",        # 17, 23
        "Function_24_29F1",        # 18, 24
        "Function_25_30BE",        # 19, 25
        "Function_26_3101",        # 1A, 26
        "Function_27_31DC",        # 1B, 27
    ))


    def Function_0_AB8(): pass

    label("Function_0_AB8")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xF9, 7)
    SetScenarioFlags(0xFB, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ADD")
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF3")
    Event(0, 26)

    label("loc_AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_B02")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 8)

    label("loc_B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_B1A")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_B1A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DA1")
    ClearScenarioFlags(0x7A, 0)
    ClearScenarioFlags(0x7A, 1)
    ClearScenarioFlags(0x7A, 2)
    ClearScenarioFlags(0x7A, 3)
    ClearScenarioFlags(0x7A, 4)
    ClearScenarioFlags(0x7A, 5)
    ClearScenarioFlags(0x7A, 6)
    ClearScenarioFlags(0x7A, 7)
    ClearScenarioFlags(0x7B, 0)
    ClearScenarioFlags(0x7B, 1)
    ClearScenarioFlags(0x7B, 2)
    ClearScenarioFlags(0x7B, 3)
    ClearScenarioFlags(0x7B, 4)
    ClearScenarioFlags(0x7B, 5)
    ClearScenarioFlags(0x7B, 6)
    ClearScenarioFlags(0x7B, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B80")
    SetScenarioFlags(0x7A, 0)

    label("loc_B80")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B96")
    SetScenarioFlags(0x7A, 1)

    label("loc_B96")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAC")
    SetScenarioFlags(0x7A, 2)

    label("loc_BAC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC2")
    SetScenarioFlags(0x7A, 3)

    label("loc_BC2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD8")
    SetScenarioFlags(0x7A, 4)

    label("loc_BD8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEE")
    SetScenarioFlags(0x7A, 5)

    label("loc_BEE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C04")
    SetScenarioFlags(0x7A, 6)

    label("loc_C04")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1A")
    SetScenarioFlags(0x7A, 7)

    label("loc_C1A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C30")
    SetScenarioFlags(0x7B, 0)

    label("loc_C30")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C46")
    SetScenarioFlags(0x7B, 1)

    label("loc_C46")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5C")
    SetScenarioFlags(0x7B, 2)

    label("loc_C5C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C72")
    SetScenarioFlags(0x7B, 3)

    label("loc_C72")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C88")
    SetScenarioFlags(0x7B, 4)

    label("loc_C88")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9E")
    SetScenarioFlags(0x7B, 5)

    label("loc_C9E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB4")
    SetScenarioFlags(0x7B, 6)

    label("loc_CB4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCA")
    SetScenarioFlags(0x7B, 7)

    label("loc_CCA")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D05")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_DA1")

    label("loc_D05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1C")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_DA1")

    label("loc_D1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D33")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_DA1")

    label("loc_D33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4A")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_DA1")

    label("loc_D4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D61")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_DA1")

    label("loc_D61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D78")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_DA1")

    label("loc_D78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8F")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_DA1")

    label("loc_D8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA1")
    SetScenarioFlags(0x7C, 7)

    label("loc_DA1")

    Call(0, 5)
    Return()

    # Function_0_AB8 end

    def Function_1_DA5(): pass

    label("Function_1_DA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBE")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_DC4")

    label("loc_DBE")

    OP_10(0x0, 0x1)
    OP_10(0x2, 0x0)

    label("loc_DC4")

    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x3, 0x4)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F8")
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    ClearMapObjFlags(0x3, 0x4)
    OP_66(0x4, 0x1)
    Jump("loc_10FD")

    label("loc_10F8")

    OP_16(0x3, 0x3, 0x1, 0x0)

    label("loc_10FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1110")
    OP_70(0x1, 0x0)
    Jump("loc_1114")

    label("loc_1110")

    OP_70(0x1, 0x1E)

    label("loc_1114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1127")
    OP_70(0x2, 0x0)
    Jump("loc_112B")

    label("loc_1127")

    OP_70(0x2, 0x1E)

    label("loc_112B")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 0)), scpexpr(EXPR_END)), "loc_1188")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -100260, -1990, 14160, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1188")

    OP_78(0x4, 0x9)
    OP_78(0x5, 0xA)
    OP_78(0x6, 0xB)
    OP_78(0x7, 0xC)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x4, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x5, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x6, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x7, "chukin", 0x0, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    OP_65(0x9, 0x1)
    OP_65(0xA, 0x1)
    OP_65(0xB, 0x1)
    OP_65(0xC, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_124A")
    Jump("loc_146C")

    label("loc_124A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1311")
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    SetChrPos(0xA, -12350, -2000, 13000, 270)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0xB, -19900, -2000, 15000, 300)
    OP_D3(0xB, 0x0, 0x493E0, 0x0, 0x0)
    SetChrPos(0xC, -26000, -2000, 17180, 280)
    OP_D3(0xC, 0x0, 0x445C0, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12E2")
    Jump("loc_130C")

    label("loc_12E2")

    ClearMapObjFlags(0x4, 0x4)
    SetChrPos(0x9, -5500, -2000, 13000, 270)
    OP_D3(0x9, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_130C")

    Jump("loc_146C")

    label("loc_1311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_146C")
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    SetChrPos(0x9, -5500, -2000, 13000, 270)
    OP_D3(0x9, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0xA, -12350, -2000, 13000, 270)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0xB, -19900, -2000, 15000, 300)
    OP_D3(0xB, 0x0, 0x493E0, 0x0, 0x0)
    SetChrPos(0xC, -26000, -2000, 17180, 280)
    OP_D3(0xC, 0x0, 0x445C0, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_13D3")
    Jump("loc_146C")

    label("loc_13D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_146C")
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    OP_66(0x7, 0x1)
    OP_66(0x8, 0x1)
    OP_66(0x9, 0x1)
    OP_66(0xA, 0x1)
    OP_66(0xB, 0x1)
    OP_66(0xC, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_141B")
    SetMapObjFrame(0x4, "chukin", 0x1, 0x1)

    label("loc_141B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_1436")
    SetMapObjFrame(0x5, "chukin", 0x1, 0x1)

    label("loc_1436")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_1451")
    SetMapObjFrame(0x6, "chukin", 0x1, 0x1)

    label("loc_1451")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_146C")
    SetMapObjFrame(0x7, "chukin", 0x1, 0x1)

    label("loc_146C")

    Return()

    # Function_1_DA5 end

    def Function_2_146D(): pass

    label("Function_2_146D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1569")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_14F2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x118, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1564")

    label("loc_14F2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1564")

    Jump("loc_15AE")

    label("loc_1569")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
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

    label("loc_15AE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_146D end

    def Function_3_15BA(): pass

    label("Function_3_15BA")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B6")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_163F")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x118, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_16B1")

    label("loc_163F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_16B1")

    Jump("loc_16FB")

    label("loc_16B6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_16FB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_15BA end

    def Function_4_1707(): pass

    label("Function_4_1707")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_4_1707 end

    def Function_5_171B(): pass

    label("Function_5_171B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1733")
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_1733")

    Return()

    # Function_5_171B end

    def Function_6_1734(): pass

    label("Function_6_1734")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ベルガード門\x01",                # 0
            "停留所（警察学校付近）\x01",      # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C7")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_17E7")

    label("loc_17C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E7")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()

    label("loc_17E7")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_1734 end

    def Function_7_17EF(): pass

    label("Function_7_17EF")

    Fade(1000)
    OP_68(-9910, -1400, 11630, 0)
    MoveCamera(39, 32, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(24500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -5700, -2000, 5500, 0)
    SetChrPos(0x1, -7000, -2000, 5500, 0)
    SetChrPos(0x2, -8300, -2000, 5500, 0)
    SetChrPos(0x3, -9600, -2000, 5500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0x8)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x8, -34340, -2000, 9000, 0)
    OP_D3(0x8, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_18CA():
        OP_95(0xFE, -8200, -2000, 9000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18CA)
    Sleep(1500)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_7_17EF end

    def Function_8_1913(): pass

    label("Function_8_1913")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -5770, -2000, 5580, 270)
    SetChrPos(0x1, -5770, -2000, 5580, 270)
    SetChrPos(0x2, -5770, -2000, 5580, 270)
    SetChrPos(0x3, -5770, -2000, 5580, 270)
    OP_68(-5770, -1400, 5580, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_8_1913 end

    def Function_9_19A8(): pass

    label("Function_9_19A8")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F52")

    Menu(
        0,
        32,
        26,
        1,
        (
            "警備隊車両で移動をする\x01",      # 0
            "ここで休憩をする\x01",            # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EEF")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A58")
    MenuCmd(1, 1, "★クロスベル市・中央広場")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1A74")

    label("loc_1A58")

    MenuCmd(1, 1, "　クロスベル市・中央広場")

    label("loc_1A74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA6")
    MenuCmd(1, 1, "★クロスベル市・東出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_1AC0")

    label("loc_1AA6")

    MenuCmd(1, 1, "　クロスベル市・東出口")

    label("loc_1AC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF2")
    MenuCmd(1, 1, "★クロスベル市・西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1B0C")

    label("loc_1AF2")

    MenuCmd(1, 1, "　クロスベル市・西出口")

    label("loc_1B0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B3E")
    MenuCmd(1, 1, "★クロスベル市・南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1B58")

    label("loc_1B3E")

    MenuCmd(1, 1, "　クロスベル市・南出口")

    label("loc_1B58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8A")
    MenuCmd(1, 1, "★クロスベル市・北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1BA4")

    label("loc_1B8A")

    MenuCmd(1, 1, "　クロスベル市・北出口")

    label("loc_1BA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BCE")
    MenuCmd(1, 1, "★タングラム門")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1BE0")

    label("loc_1BCE")

    MenuCmd(1, 1, "　タングラム門")

    label("loc_1BE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C0A")
    MenuCmd(1, 1, "★ベルガード門")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1C1C")

    label("loc_1C0A")

    MenuCmd(1, 1, "　ベルガード門")

    label("loc_1C1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C4A")
    MenuCmd(1, 1, "★ウルスラ医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1C60")

    label("loc_1C4A")

    MenuCmd(1, 1, "　ウルスラ医科大学")

    label("loc_1C60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C8A")
    MenuCmd(1, 1, "★アルモリカ村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1C9C")

    label("loc_1C8A")

    MenuCmd(1, 1, "　アルモリカ村")

    label("loc_1C9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CC8")
    MenuCmd(1, 1, "★マインツ鉱山町")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1CDC")

    label("loc_1CC8")

    MenuCmd(1, 1, "　マインツ鉱山町")

    label("loc_1CDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D0E")
    MenuCmd(1, 1, "★マインツ山道・隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1D28")

    label("loc_1D0E")

    MenuCmd(1, 1, "　マインツ山道・隧道内")

    label("loc_1D28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D4E")
    MenuCmd(1, 1, "★星見の塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1D5C")

    label("loc_1D4E")

    MenuCmd(1, 1, "　星見の塔")

    label("loc_1D5C")

    MenuCmd(1, 1, "　やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EE0")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)    #voice#Noel
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x3)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E33"),
        (1, "loc_1E41"),
        (2, "loc_1E4F"),
        (3, "loc_1E5D"),
        (4, "loc_1E6B"),
        (5, "loc_1E79"),
        (6, "loc_1E87"),
        (7, "loc_1E95"),
        (8, "loc_1EA3"),
        (9, "loc_1EB1"),
        (10, "loc_1EBF"),
        (11, "loc_1ECD"),
        (SWITCH_DEFAULT, "loc_1EDB"),
    )


    label("loc_1E33")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EDB")

    label("loc_1E41")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EDB")

    label("loc_1E4F")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EDB")

    label("loc_1E5D")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EDB")

    label("loc_1E6B")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EDB")

    label("loc_1E79")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EDB")

    label("loc_1E87")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EDB")

    label("loc_1E95")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EDB")

    label("loc_1EA3")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EDB")

    label("loc_1EB1")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EDB")

    label("loc_1EBF")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EDB")

    label("loc_1ECD")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EDB")

    label("loc_1EDB")

    Jump("loc_1EEA")

    label("loc_1EE0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EEA")

    Jump("loc_1F4D")

    label("loc_1EEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3A")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_1F4D")

    label("loc_1F3A")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F4D")

    Jump("loc_19C2")

    label("loc_1F52")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_19A8 end

    def Function_10_1F5A(): pass

    label("Function_10_1F5A")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -6360, -2000, 9850, 180)
    SetChrPos(0x1, -6360, -2000, 9850, 180)
    SetChrPos(0x2, -6360, -2000, 9850, 180)
    SetChrPos(0x3, -6360, -2000, 9850, 180)
    SetChrPos(0x4, -6360, -2000, 9850, 180)
    SetChrPos(0x5, -6360, -2000, 9850, 180)
    Sleep(1)
    OP_68(-6360, -1400, 9850, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_202E")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_2034")

    label("loc_202E")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_2034")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1F5A end

    def Function_11_2049(): pass

    label("Function_11_2049")

    TalkBegin(0xFF)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ラインフォルト社製の自家用車のようだ。\x02\x03",

            "車両ナンバーは『ＥＷ　３１００』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBD, 5)
    Call(0, 20)
    TalkEnd(0xFF)
    Return()

    # Function_11_2049 end

    def Function_12_20AD(): pass

    label("Function_12_20AD")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_20F8")
    SetChrName("")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "違法駐車の警告ステッカーが\x01",
            "貼られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2122")

    label("loc_20F8")

    Call(0, 19)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2122")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x4, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x2)

    label("loc_2122")

    TalkEnd(0xFF)
    Return()

    # Function_12_20AD end

    def Function_13_2126(): pass

    label("Function_13_2126")

    TalkBegin(0xFF)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ヴェルヌ社製の自家用車のようだ。\x02\x03",

            "車両ナンバーは『ＣＺ　３３２３』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBD, 6)
    Call(0, 20)
    TalkEnd(0xFF)
    Return()

    # Function_13_2126 end

    def Function_14_2184(): pass

    label("Function_14_2184")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_21CF")
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "違法駐車の警告ステッカーが\x01",
            "貼られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_21F9")

    label("loc_21CF")

    Call(0, 19)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F9")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x5, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x4)

    label("loc_21F9")

    TalkEnd(0xFF)
    Return()

    # Function_14_2184 end

    def Function_15_21FD(): pass

    label("Function_15_21FD")

    TalkBegin(0xFF)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ヴェルヌ社製の導力運搬車のようだ。\x02\x03",

            "車両ナンバーは『ＣＬ　１１０１』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_229E")

    #C0013
    ChrTalk(
        0x101,
        (
            "#0001F（確か東口にも\x01",
            "  あったはずのナンバーだ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2333")

    label("loc_229E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22B7")
    Call(0, 21)
    Jump("loc_2333")

    label("loc_22B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2326")

    #C0014
    ChrTalk(
        0x101,
        (
            "#0005F（あれ…………？）\x02\x03",

            "#0003F（このナンバー、どこかで見た事が\x01",
            "  あるような……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2333")

    label("loc_2326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2333")
    SetScenarioFlags(0xBC, 4)

    label("loc_2333")

    SetScenarioFlags(0xBD, 7)
    Call(0, 20)
    TalkEnd(0xFF)
    Return()

    # Function_15_21FD end

    def Function_16_233D(): pass

    label("Function_16_233D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2388")
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "違法駐車の警告ステッカーが\x01",
            "貼られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_23B2")

    label("loc_2388")

    Call(0, 19)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B2")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x6, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x6)

    label("loc_23B2")

    TalkEnd(0xFF)
    Return()

    # Function_16_233D end

    def Function_17_23B6(): pass

    label("Function_17_23B6")

    TalkBegin(0xFF)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ラインフォルト社製の高級車のようだ。\x02\x03",

            "車両ナンバーは『ＥＤ　００２８』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 0)
    Call(0, 20)
    TalkEnd(0xFF)
    Return()

    # Function_17_23B6 end

    def Function_18_2418(): pass

    label("Function_18_2418")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2463")
    SetChrName("")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "違法駐車の警告ステッカーが\x01",
            "貼られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_248D")

    label("loc_2463")

    Call(0, 19)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248D")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x7, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x8)

    label("loc_248D")

    TalkEnd(0xFF)
    Return()

    # Function_18_2418 end

    def Function_19_2491(): pass

    label("Function_19_2491")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "警告ステッカーを貼りますか？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        1,
        (
            "【貼る】\x01",          # 0
            "【貼らない】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Return()

    # Function_19_2491 end

    def Function_20_2504(): pass

    label("Function_20_2504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2695")

    #C0019
    ChrTalk(
        0x101,
        (
            "#0003Fよし……これで\x01",
            "全車両のナンバーを\x01",
            "チェックしたかな。\x02\x03",

            "#0000F残りのステッカーを貼ってから\x01",
            "報告に戻ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        "#0300Fうっし、そうするかね。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#0100F別に急ぎではないみたいだし、\x01",
            "もう一度確認しつつ戻るのも\x01",
            "いいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#0200F間違って貼っていても\x01",
            "はがす事は出来ませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0000Fハハ……\x01",
            "まあ大丈夫だとは思うけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x17, 0x1, 0x13)

    label("loc_2695")

    Return()

    # Function_20_2504 end

    def Function_21_2696(): pass

    label("Function_21_2696")

    EventBegin(0x0)
    Fade(500)
    OP_E0(0x1)
    OP_68(-16510, -1000, 12930, 0)
    MoveCamera(35, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19610, 0)
    SetChrPos(0x101, -16190, -2000, 12370, 315)
    SetChrPos(0x102, -16030, -2000, 13480, 270)
    SetChrPos(0x103, -15170, -2000, 12270, 315)
    SetChrPos(0x104, -17080, -2000, 10620, 0)
    OP_0D()

    #C0024
    ChrTalk(
        0x101,
        (
            "#11P#0005F……………………？\x02\x03",

            "#0001Fこのナンバー……\x01",
            "東口にもなかったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#5P#0105Fそういえば……\x01",
            "あったかも知れないわ。\x02\x03",

            "#0101F運搬車じゃ\x01",
            "なかった気がするけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        (
            "#11P#0200F同じナンバーの車両なんて\x01",
            "本来あるはずはありませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#12P#0303Fふむ……認可は\x01",
            "受けているナンバーだな。\x02\x03",

            "#0300Fま、一応覚えといた方が\x01",
            "いいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#11P#0000Fそうだな……\x01",
            "後で広域防犯課の方にも\x01",
            "報告しておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_E0(0x0)
    Call(0, 5)
    SetChrPos(0x0, -16190, -2000, 12370, 315)
    OP_29(0x17, 0x1, 0x14)
    EventEnd(0x5)
    Return()

    # Function_21_2696 end

    def Function_22_28D0(): pass

    label("Function_22_28D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2981")
    TalkBegin(0xFF)

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0030
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "凶悪な魔獣出没中との通報を受け、\x01",
            "現在運行を見合わせております。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x95, 2)
    TalkEnd(0xFF)
    Jump("loc_29E2")

    label("loc_2981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29DF")
    TalkBegin(0xFF)

    #C0031
    ChrTalk(
        0x101,
        (
            "#0001Fバスを待っている場合じゃない……\x01",
            "コリン君を探しに行こう！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_29E2")

    label("loc_29DF")

    Call(0, 6)

    label("loc_29E2")

    Return()

    # Function_22_28D0 end

    def Function_23_29E3(): pass

    label("Function_23_29E3")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_23_29E3 end

    def Function_24_29F1(): pass

    label("Function_24_29F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x3)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(840)
    OP_68(8300, 2400, -2710, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(15190, 0)
    SetChrPos(0x101, 15950, 0, -140, 270)
    SetChrPos(0x102, 17240, 0, 710, 270)
    SetChrPos(0x103, 16970, 0, -1080, 270)
    SetChrPos(0x104, 18870, 0, 780, 270)
    SetChrPos(0x160, 18510, 0, -770, 270)
    FadeToBright(1000, 0)
    SetCameraDistance(13690, 3000)

    def lambda_2AD2():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AD2)

    def lambda_2AE7():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2AE7)

    def lambda_2AFC():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2AFC)

    def lambda_2B11():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B11)

    def lambda_2B26():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2B26)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x160, 1)
    OP_6F(0x79)
    OP_0D()
    TurnDirection(0x101, 0x103, 500)

    #C0032
    ChrTalk(
        0x101,
        (
            "#0001F#5Pティオ。\x01",
            "念のため周辺を探ってくれるか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B8F():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B8F)

    def lambda_2B9C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B9C)
    Sleep(100)

    def lambda_2BAC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BAC)

    def lambda_2BB9():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BB9)
    Sleep(100)

    def lambda_2BC9():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2BC9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x160, 1)

    #C0033
    ChrTalk(
        0x103,
        "#0203F#12P了解です。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x103, 0xE1, 0x1F4)
    Sound(1278, 255, 100, 0)    #voice#Tio
    Sleep(800)
    VolumeBGM(0x3C, 0x3E8)
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sound(820, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 25)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(500)
    EndChrThread(0xD, 0x1)
    TurnDirection(0x103, 0x101, 500)

    #C0034
    ChrTalk(
        0x103,
        (
            "#0208F#12P……どうやら街の近辺には\x01",
            "いないようですね。\x02\x03",

            "#0201F６０セルジュほど先に\x01",
            "運搬車の反応はありましたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#0301F#5Pってことは、まずは運搬車の\x01",
            "所まで行ったほうがよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x160,
        (
            "#3305F#11Pふぅん、魔導杖か。\x02\x03",

            "#3304F似たようなものを\x01",
            "《教授》も持っていたけれど……\x02\x03",

            "#3302Fエプスタインの人たちも\x01",
            "面白いオモチャを作ったものね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E91():
        TurnDirection(0xFE, 0x160, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E91)

    def lambda_2E9E():
        TurnDirection(0xFE, 0x160, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E9E)
    Sleep(100)

    def lambda_2EAE():
        TurnDirection(0xFE, 0x160, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2EAE)

    def lambda_2EBB():
        TurnDirection(0xFE, 0x160, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2EBB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0037
    ChrTalk(
        0x101,
        "#0005F#6P教授……？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        (
            "#0205F#6P財団の最新技術の精華と\x01",
            "似たような物を持っていた……\x02\x03",

            "#0201F……あなた、ひょっとして……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x160,
        (
            "#3309F#11Pクスクス……\x02\x03",

            "#3304Fそれよりも今は\x01",
            "先に進むことにしましょう。\x02\x03",

            "#3302F可愛い、可愛いあの子が\x01",
            "かわいそうな事になる前に。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#0001F#6P……もちろんだ。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#0103F#5Pとにかく急ぎましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_37()
    OP_68(10000, 600, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 10000, 0, 0, 270)
    SetChrPos(0x1, 10000, 0, 0, 270)
    SetChrPos(0x2, 10000, 0, 0, 270)
    SetChrPos(0x3, 10000, 0, 0, 270)
    SetChrPos(0x4, 10000, 0, 0, 270)
    OP_E0(0x2)
    SetScenarioFlags(0xA3, 0)
    OP_24(0x348)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_24_29F1 end

    def Function_25_30BE(): pass

    label("Function_25_30BE")

    OP_25(0x348, 0x5A)
    Sleep(50)
    OP_25(0x348, 0x50)
    Sleep(50)
    OP_25(0x348, 0x46)
    Sleep(50)
    OP_25(0x348, 0x3C)
    Sleep(50)
    OP_25(0x348, 0x32)
    Sleep(50)
    OP_25(0x348, 0x28)
    Sleep(50)
    OP_25(0x348, 0x1E)
    Sleep(50)
    OP_25(0x348, 0x14)
    Sleep(50)
    OP_25(0x348, 0xA)
    Sleep(50)
    OP_24(0x348)
    Return()

    # Function_25_30BE end

    def Function_26_3101(): pass

    label("Function_26_3101")

    EventBegin(0x0)
    Sleep(1000)
    OP_68(-5690, 600, 4440, 4000)
    MoveCamera(45, 25, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(24500, 4000)
    OP_6F(0x79)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "停留所の看板を調べると、\x01",
            "導力バスに乗ることができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "選択した行き先へ素早く移動することができ、\x01",
            "各地を効率的に回ることが可能です。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 7)
    EventEnd(0x5)
    Return()

    # Function_26_3101 end

    def Function_27_31DC(): pass

    label("Function_27_31DC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "東・クロスベル市\x01",
            "西・ベルガード門　１９８セルジュ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_31DC end

    SaveToFile()

Try(main)
