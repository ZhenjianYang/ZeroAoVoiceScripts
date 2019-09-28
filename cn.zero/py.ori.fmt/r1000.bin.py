from ZeroScenarioHelper import *

def main():
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
        "巴士",                   # 1
        "车00",                   # 2
        "车01",                   # 3
        "车02",                   # 4
        "车03",                   # 5
        "SE控制",                 # 6
        "br1000",                 # 7
        "br1000",                 # 8
        "br1000",                 # 9
        "br1000",                 # 10
        "br1000",                 # 11
        "克洛斯贝尔市方向",       # 12
        "贝尔加德门方向",         # 13
    ))

    ATBonus("ATBonus_51C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_302C", 11,  3,   8,   0,   8,   0,   0)
    Sepith("Sepith_3034", 11,  0,   5,   7,   0,   0,   7)
    Sepith("Sepith_3074", 4,   4,   10,  2,   0,   5,   5)
    Sepith("Sepith_306C", 13,  13,  0,   4,   0,   0,   0)
    Sepith("Sepith_3084", 12,  7,   4,   3,   6,   14,  7)

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
        "BattleInfo_5FC", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_302C", 30, 40, 20, 10,
        (
            ("ms60900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms60900.dat", "ms60900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms60900.dat", "ms70400.dat", "ms60900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms60900.dat", "ms60900.dat", "ms74800.dat", "ms60900.dat", 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
        )
    )

    BattleInfo(
        "BattleInfo_6C4", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_3034", 30, 40, 20, 10,
        (
            ("ms74800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms74800.dat", "ms74800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms74800.dat", "ms70400.dat", "ms74800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms74800.dat", "ms74800.dat", "ms60900.dat", "ms74800.dat", 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
        )
    )

    BattleInfo(
        "BattleInfo_78C", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_3074", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
        )
    )

    BattleInfo(
        "BattleInfo_854", 0x0000, 17, 6, 60, 8, 1, 30, 0, "br1000", "Sepith_306C", 30, 40, 20, 10,
        (
            ("ms71500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms71500.dat", "ms71500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms71500.dat", "ms71900.dat", "ms71500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
            ("ms71500.dat", "ms71500.dat", "ms70400.dat", "ms71500.dat", 0, 0, 0, 0, "MonsterBattlePostion_55C", "MonsterBattlePostion_5DC", "ed7400", "ed7403", "ATBonus_51C"),
        )
    )

    BattleInfo(
        "BattleInfo_91C", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br1000", "Sepith_3084", 40, 35, 25, 0,
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

    PlaceName(23.0, 0.0, 4.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(-137.0, 0.0, -28.0, 0x0000, 0x0000, "贝尔加德门方向")
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
        "Function_3_15A3",         # 03, 3
        "Function_4_16D9",         # 04, 4
        "Function_5_16ED",         # 05, 5
        "Function_6_1706",         # 06, 6
        "Function_7_17B9",         # 07, 7
        "Function_8_18DD",         # 08, 8
        "Function_9_1972",         # 09, 9
        "Function_10_1F0A",        # 0A, 10
        "Function_11_1FF9",        # 0B, 11
        "Function_12_2053",        # 0C, 12
        "Function_13_20BE",        # 0D, 13
        "Function_14_2114",        # 0E, 14
        "Function_15_217F",        # 0F, 15
        "Function_16_22A3",        # 10, 16
        "Function_17_230E",        # 11, 17
        "Function_18_236A",        # 12, 18
        "Function_19_23D5",        # 13, 19
        "Function_20_2438",        # 14, 20
        "Function_21_2584",        # 15, 21
        "Function_22_277C",        # 16, 22
        "Function_23_285F",        # 17, 23
        "Function_24_286D",        # 18, 24
        "Function_25_2EA6",        # 19, 25
        "Function_26_2EE9",        # 1A, 26
        "Function_27_2FA0",        # 1B, 27
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155A")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅰ', 1)"), scpexpr(EXPR_END)), "loc_14EC")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x118, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1555")

    label("loc_14EC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1555")

    Jump("loc_1597")

    label("loc_155A")

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

    label("loc_1597")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_146D end

    def Function_3_15A3(): pass

    label("Function_3_15A3")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1690")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('复苏药', 1)"), scpexpr(EXPR_END)), "loc_1622")
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
    SetScenarioFlags(0x118, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_168B")

    label("loc_1622")

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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_168B")

    Jump("loc_16CD")

    label("loc_1690")

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

    label("loc_16CD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_15A3 end

    def Function_4_16D9(): pass

    label("Function_4_16D9")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_4_16D9 end

    def Function_5_16ED(): pass

    label("Function_5_16ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1705")
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_1705")

    Return()

    # Function_5_16ED end

    def Function_6_1706(): pass

    label("Function_6_1706")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "贝尔加德门\x01",                  # 0
            "停靠站（警察学校附近）\x01",      # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1791")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_17B1")

    label("loc_1791")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B1")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()

    label("loc_17B1")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_1706 end

    def Function_7_17B9(): pass

    label("Function_7_17B9")

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

    def lambda_1894():
        OP_95(0xFE, -8200, -2000, 9000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1894)
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

    # Function_7_17B9 end

    def Function_8_18DD(): pass

    label("Function_8_18DD")

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

    # Function_8_18DD end

    def Function_9_1972(): pass

    label("Function_9_1972")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_198C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F02")

    Menu(
        0,
        32,
        26,
        1,
        (
            "使用警备队车辆进行移动\x01",      # 0
            "在此处休息\x01",                  # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E9F")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1A")
    MenuCmd(1, 1, "★克洛斯贝尔市·中央广场")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1A36")

    label("loc_1A1A")

    MenuCmd(1, 1, "　克洛斯贝尔市·中央广场")

    label("loc_1A36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A68")
    MenuCmd(1, 1, "★克洛斯贝尔市·东出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_1A82")

    label("loc_1A68")

    MenuCmd(1, 1, "　克洛斯贝尔市·东出口")

    label("loc_1A82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB4")
    MenuCmd(1, 1, "★克洛斯贝尔市·西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1ACE")

    label("loc_1AB4")

    MenuCmd(1, 1, "　克洛斯贝尔市·西出口")

    label("loc_1ACE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B00")
    MenuCmd(1, 1, "★克洛斯贝尔市·南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1B1A")

    label("loc_1B00")

    MenuCmd(1, 1, "　克洛斯贝尔市·南出口")

    label("loc_1B1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4C")
    MenuCmd(1, 1, "★克洛斯贝尔市·北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1B66")

    label("loc_1B4C")

    MenuCmd(1, 1, "　克洛斯贝尔市·北出口")

    label("loc_1B66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8E")
    MenuCmd(1, 1, "★唐古拉姆门")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1B9E")

    label("loc_1B8E")

    MenuCmd(1, 1, "　唐古拉姆门")

    label("loc_1B9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC6")
    MenuCmd(1, 1, "★贝尔加德门")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1BD6")

    label("loc_1BC6")

    MenuCmd(1, 1, "　贝尔加德门")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C04")
    MenuCmd(1, 1, "★乌尔斯拉医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1C1A")

    label("loc_1C04")

    MenuCmd(1, 1, "　乌尔斯拉医科大学")

    label("loc_1C1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C44")
    MenuCmd(1, 1, "★阿尔摩利卡村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1C56")

    label("loc_1C44")

    MenuCmd(1, 1, "　阿尔摩利卡村")

    label("loc_1C56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C80")
    MenuCmd(1, 1, "★矿山镇玛因兹")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1C92")

    label("loc_1C80")

    MenuCmd(1, 1, "　矿山镇玛因兹")

    label("loc_1C92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CC2")
    MenuCmd(1, 1, "★玛因兹山道·隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1CDA")

    label("loc_1CC2")

    MenuCmd(1, 1, "　玛因兹山道·隧道内")

    label("loc_1CDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D00")
    MenuCmd(1, 1, "★星见之塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1D0E")

    label("loc_1D00")

    MenuCmd(1, 1, "　星见之塔")

    label("loc_1D0E")

    MenuCmd(1, 1, "　放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E90")
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
        (0, "loc_1DE3"),
        (1, "loc_1DF1"),
        (2, "loc_1DFF"),
        (3, "loc_1E0D"),
        (4, "loc_1E1B"),
        (5, "loc_1E29"),
        (6, "loc_1E37"),
        (7, "loc_1E45"),
        (8, "loc_1E53"),
        (9, "loc_1E61"),
        (10, "loc_1E6F"),
        (11, "loc_1E7D"),
        (SWITCH_DEFAULT, "loc_1E8B"),
    )


    label("loc_1DE3")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E8B")

    label("loc_1DF1")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E8B")

    label("loc_1DFF")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E8B")

    label("loc_1E0D")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E8B")

    label("loc_1E1B")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E8B")

    label("loc_1E29")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E8B")

    label("loc_1E37")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E8B")

    label("loc_1E45")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E8B")

    label("loc_1E53")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E8B")

    label("loc_1E61")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E8B")

    label("loc_1E6F")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E8B")

    label("loc_1E7D")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E8B")

    label("loc_1E8B")

    Jump("loc_1E9A")

    label("loc_1E90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E9A")

    Jump("loc_1EFD")

    label("loc_1E9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EEA")
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
    Jump("loc_1EFD")

    label("loc_1EEA")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EFD")

    Jump("loc_198C")

    label("loc_1F02")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1972 end

    def Function_10_1F0A(): pass

    label("Function_10_1F0A")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FDE")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_1FE4")

    label("loc_1FDE")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_1FE4")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1F0A end

    def Function_11_1FF9(): pass

    label("Function_11_1FF9")

    TalkBegin(0xFF)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎是莱恩福尔特公司制造的私家车。\x02\x03",

            "车牌号为『ＥＷ　３１００』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBD, 5)
    Call(0, 20)
    TalkEnd(0xFF)
    Return()

    # Function_11_1FF9 end

    def Function_12_2053(): pass

    label("Function_12_2053")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2090")
    SetChrName("")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "贴上违章停车的\x01",
            "警告标志了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_20BA")

    label("loc_2090")

    Call(0, 19)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BA")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x4, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x2)

    label("loc_20BA")

    TalkEnd(0xFF)
    Return()

    # Function_12_2053 end

    def Function_13_20BE(): pass

    label("Function_13_20BE")

    TalkBegin(0xFF)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎是乌尔努公司制造的私家车。\x02\x03",

            "车牌号为『ＣＺ　３３２３』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBD, 6)
    Call(0, 20)
    TalkEnd(0xFF)
    Return()

    # Function_13_20BE end

    def Function_14_2114(): pass

    label("Function_14_2114")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2151")
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "贴上违章停车的\x01",
            "警告标志了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_217B")

    label("loc_2151")

    Call(0, 19)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217B")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x5, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x4)

    label("loc_217B")

    TalkEnd(0xFF)
    Return()

    # Function_14_2114 end

    def Function_15_217F(): pass

    label("Function_15_217F")

    TalkBegin(0xFF)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎是乌尔努公司制造的导力搬运车。\x02\x03",

            "车牌号为『ＣＬ　１１０１』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_2212")

    #C0013
    ChrTalk(
        0x101,
        (
            "#0001F（这个号码\x01",
            "  似乎在东出口出现过……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2299")

    label("loc_2212")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_222B")
    Call(0, 21)
    Jump("loc_2299")

    label("loc_222B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_228C")

    #C0014
    ChrTalk(
        0x101,
        (
            "#0005F（咦…………？）\x02\x03",

            "#0003F（这个号码，总觉得好像\x01",
            "  在哪见过……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2299")

    label("loc_228C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2299")
    SetScenarioFlags(0xBC, 4)

    label("loc_2299")

    SetScenarioFlags(0xBD, 7)
    Call(0, 20)
    TalkEnd(0xFF)
    Return()

    # Function_15_217F end

    def Function_16_22A3(): pass

    label("Function_16_22A3")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_22E0")
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "贴上违章停车的\x01",
            "警告标志了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_230A")

    label("loc_22E0")

    Call(0, 19)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230A")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x6, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x6)

    label("loc_230A")

    TalkEnd(0xFF)
    Return()

    # Function_16_22A3 end

    def Function_17_230E(): pass

    label("Function_17_230E")

    TalkBegin(0xFF)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎是莱恩福尔特公司制造的高级轿车。\x02\x03",

            "车牌号为『ＥＤ　００２８』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 0)
    Call(0, 20)
    TalkEnd(0xFF)
    Return()

    # Function_17_230E end

    def Function_18_236A(): pass

    label("Function_18_236A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_23A7")
    SetChrName("")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "贴上违章停车的\x01",
            "警告标志了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_23D1")

    label("loc_23A7")

    Call(0, 19)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23D1")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x7, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x8)

    label("loc_23D1")

    TalkEnd(0xFF)
    Return()

    # Function_18_236A end

    def Function_19_23D5(): pass

    label("Function_19_23D5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要贴上警告标志吗？",
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
            "【贴】\x01",        # 0
            "【不贴】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Return()

    # Function_19_23D5 end

    def Function_20_2438(): pass

    label("Function_20_2438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2583")

    #C0019
    ChrTalk(
        0x101,
        (
            "#0003F好……这样一来，\x01",
            "就检查完所有车辆的\x01",
            "车牌号了。\x02\x03",

            "#0000F贴完余下的标志\x01",
            "就回去报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        "#0300F好，就那么办吧。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#0100F也不是很赶时间，\x01",
            "进行二次确认之后再回去\x01",
            "也许比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#0200F虽然就算贴错，\x01",
            "也没法再撕下来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……\x01",
            "我觉得应该没问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x17, 0x1, 0x13)

    label("loc_2583")

    Return()

    # Function_20_2438 end

    def Function_21_2584(): pass

    label("Function_21_2584")

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

            "#0001F这个号码……\x01",
            "在东出口也出现过吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#5P#0105F说起来……\x01",
            "也许是出现过呢。\x02\x03",

            "#0101F但那边的好像\x01",
            "并不是搬运车。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        (
            "#11P#0200F车牌号相同的车辆\x01",
            "本来是不可能存在的……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#12P#0303F呼……似乎是\x01",
            "得到准停许可的车牌号。\x02\x03",

            "#0300F哎，先记着\x01",
            "比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#11P#0000F是啊……\x01",
            "之后也向公共安全科的\x01",
            "各位进行报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_E0(0x0)
    Call(0, 5)
    SetChrPos(0x0, -16190, -2000, 12370, 315)
    OP_29(0x17, 0x1, 0x14)
    EventEnd(0x5)
    Return()

    # Function_21_2584 end

    def Function_22_277C(): pass

    label("Function_22_277C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2815")
    TalkBegin(0xFF)

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x02",
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
            "接到有凶恶魔兽出没的通报，\x01",
            "现已暂停运行。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x95, 2)
    TalkEnd(0xFF)
    Jump("loc_285E")

    label("loc_2815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_285B")
    TalkBegin(0xFF)

    #C0031
    ChrTalk(
        0x101,
        (
            "#0001F来不及等巴士了……\x01",
            "去寻找柯林吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_285E")

    label("loc_285B")

    Call(0, 6)

    label("loc_285E")

    Return()

    # Function_22_277C end

    def Function_23_285F(): pass

    label("Function_23_285F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_23_285F end

    def Function_24_286D(): pass

    label("Function_24_286D")

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

    def lambda_294E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_294E)

    def lambda_2963():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2963)

    def lambda_2978():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2978)

    def lambda_298D():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_298D)

    def lambda_29A2():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_29A2)
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
            "#0001F#5P缇欧，谨慎起见，\x01",
            "你先来探查一下周边的情况好吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A13():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A13)

    def lambda_2A20():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A20)
    Sleep(100)

    def lambda_2A30():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A30)

    def lambda_2A3D():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A3D)
    Sleep(100)

    def lambda_2A4D():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2A4D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x160, 1)

    #C0033
    ChrTalk(
        0x103,
        "#0203F#12P了解。\x02",
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
            "#0208F#12P……似乎不在这\x01",
            "附近呢。\x02\x03",

            "#0201F前方约６０赛尔矩处\x01",
            "有搬运车的反应。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#0301F#5P也就是说，先去搬运车那里\x01",
            "似乎比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x160,
        (
            "#3305F#11P喔，魔导杖吗？\x02\x03",

            "#3304F『教授』也有类似的\x01",
            "东西……\x02\x03",

            "#3302F爱普斯泰恩的人\x01",
            "也做出了有趣的玩具呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2CAF():
        TurnDirection(0xFE, 0x160, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CAF)

    def lambda_2CBC():
        TurnDirection(0xFE, 0x160, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CBC)
    Sleep(100)

    def lambda_2CCC():
        TurnDirection(0xFE, 0x160, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2CCC)

    def lambda_2CD9():
        TurnDirection(0xFE, 0x160, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CD9)
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
            "#0205F#6P持有与财团最新技术之精华\x01",
            "类似的东西……\x02\x03",

            "#0201F……你，莫非是……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x160,
        (
            "#3309F#11P呵呵……\x02\x03",

            "#3304F比起那个，眼下\x01",
            "还是先继续前进吧。\x02\x03",

            "#3302F在那个非常、非常可爱的孩子\x01",
            "遭遇不幸之前。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#0001F#6P……当然。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#0103F#5P总之加快脚步吧。\x02",
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

    # Function_24_286D end

    def Function_25_2EA6(): pass

    label("Function_25_2EA6")

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

    # Function_25_2EA6 end

    def Function_26_2EE9(): pass

    label("Function_26_2EE9")

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
            "调查停靠站的告示牌后，\x01",
            "就能乘坐导力巴士。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "进而便可迅速移动至所选目的地，\x01",
            "以更高的效率来往于各处。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 7)
    EventEnd(0x5)
    Return()

    # Function_26_2EE9 end

    def Function_27_2FA0(): pass

    label("Function_27_2FA0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东·克洛斯贝尔市\x01",
            "西·贝尔加德门　  １９８赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_2FA0 end

    SaveToFile()

Try(main)
