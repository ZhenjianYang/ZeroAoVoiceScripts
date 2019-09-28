from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r1020.bin",                # FileName
        "r1020",                    # MapName
        "r1020",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00000000,                 # Flags
        ("r1020", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 2, 0, 3],
    )

    BuildStringList((
        "r1020",                  # 0
        "比利",                   # 1
        "列车",                   # 2
        "br1000",                 # 3
        "br1000",                 # 4
        "br1000",                 # 5
        "br1000",                 # 6
        "br1000",                 # 7
        "br1000",                 # 8
        "br1000",                 # 9
        "克洛斯贝尔市方向",       # 10
        "贝尔加德门方向",         # 11
    ))

    ATBonus("ATBonus_4B4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_322A", 0,   8,   0,   12,  4,   8,   0)
    Sepith("Sepith_323A", 0,   13,  0,   13,  0,   0,   4)
    Sepith("Sepith_3222", 4,   2,   11,  0,   0,   8,   5)
    Sepith("Sepith_325A", 4,   4,   10,  2,   0,   5,   5)
    Sepith("Sepith_3232", 4,   4,   4,   10,  3,   3,   3)
    Sepith("Sepith_326A", 12,  7,   4,   3,   6,   14,  7)

    MonsterBattlePostion("MonsterBattlePostion_514", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_518", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_51C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_520", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_524", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_528", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_52C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_530", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_574", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_578", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_57C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_580", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_584", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_588", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_58C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_590", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_4F4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4FC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_500", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_504", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_508", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_50C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_510", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_5B4", 0x0000, 17, 6, 60, 8, 1, 40, 0, "br1000", "Sepith_322A", 30, 40, 20, 10,
        (
            ("ms70300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms70300.dat", "ms70300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms70300.dat", "ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_67C", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_323A", 30, 40, 20, 10,
        (
            ("ms70500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms70500.dat", "ms70500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms70500.dat", "ms70400.dat", "ms70500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms70500.dat", "ms70500.dat", "ms70400.dat", "ms70500.dat", 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_8D4", 0x0000, 17, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_3222", 30, 40, 20, 10,
        (
            ("ms63200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_744", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_325A", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_80C", 0x0000, 17, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_3232", 30, 40, 20, 10,
        (
            ("ms70400.dat", "ms70400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms70400.dat", "ms70400.dat", "ms70400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_9E0", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br1000", "Sepith_326A", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_99C", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72401.dat", "ms72401.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_594", "MonsterBattlePostion_574", "ed7401", "ed7403", "ATBonus_4B4"),
            (),
            (),
            (),
        )
    )

    # event battle count: 1

    AddCharChip((
        "chr/ch23600.itc",                   # 00
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
        "monster/ch70350.itc",               # 10
        "monster/ch70351.itc",               # 11
        "monster/ch70550.itc",               # 12
        "monster/ch70550.itc",               # 13
        "monster/ch71950.itc",               # 14
        "monster/ch71950.itc",               # 15
        "monster/ch70450.itc",               # 16
        "monster/ch70451.itc",               # 17
        "monster/ch63250.itc",               # 18
        "monster/ch63251.itc",               # 19
        "monster/ch72450.itc",               # 1A
        "monster/ch72450.itc",               # 1B
        "monster/ch60750.itc",               # 1C
        "monster/ch60750.itc",               # 1D
    ))

    DeclNpc(-84500,  0,       18899,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-16250,  -32920,  0,       0x1010000,    "BattleInfo_5B4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-31700,  -5730,   0,       0x1010000,    "BattleInfo_67C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-47140,  -40730,  -1000,   0x1010000,    "BattleInfo_8D4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-72720,  -30360,  -1000,   0x1010000,    "BattleInfo_744", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-67110,  -42180,  -1000,   0x1010000,    "BattleInfo_5B4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-66360,  4440,    -10,     0x1010000,    "BattleInfo_8D4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-105190, -11350,  -10,     0x1010000,    "BattleInfo_80C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-115390, -20350,  -10,     0x1010000,    "BattleInfo_80C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-125510, -7100,   -10,     0x1010000,    "BattleInfo_67C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-14910,  -19080,  0,       0x1010000,    "BattleInfo_9E0", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-66880,  -6860,   0,       0x1010000,    "BattleInfo_9E0", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-100640, 4780,    0,       0x1010000,    "BattleInfo_9E0", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-76100,  -38740,  500,     0x185002D,    "BattleInfo_99C", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 12,  -76.5,                 9.0,                   -1.0,                  2500.0,                [0.14142131805419922,  0.035355351865291595,  -0.0,                  0.0,                   -0.14142140746116638,  0.035355329513549805,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   12.091523170471191,    2.386486530303955,     0.20000000298023224,   1.0])
    DeclEvent(0x0040, 0, 9,   -76.0999984741211,     -38.7400016784668,     -2.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   9.512499809265137,     4.84250020980835,      0.5,                   1.0])

    DeclActor(-31810,  -50,     -1990,   1200,    -31810,  950,     -1990,   0x007C, 0,  4,  0x0000)
    DeclActor(-107180, -50,     -24250,  1200,    -107180, 950,     -24250,  0x007C, 0,  5,  0x0000)
    DeclActor(-4460,   0,       -4850,   1200,    -4460,   0,       -4850,   0x007C, 0,  6,  0x0000)
    DeclActor(-66530,  -1000,   -40600,  1200,    -66530,  -1000,   -40600,  0x007C, 0,  7,  0x0000)
    DeclActor(-122090, -10,     -9540,   1200,    -122090, -10,     -9540,   0x007C, 0,  8,  0x0000)
    DeclActor(-82960,  0,       28280,   5000,    -82960,  0,       28280,   0x007C, 0,  13, 0x0000)

    PlaceName(25.0, 0.0, 10.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(-160.0, 0.0, -16.0, 0x0000, 0x0000, "贝尔加德门方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_B48",          # 00, 0
        "Function_1_C00",          # 01, 1
        "Function_2_C1F",          # 02, 2
        "Function_3_C36",          # 03, 3
        "Function_4_15B3",         # 04, 4
        "Function_5_16E9",         # 05, 5
        "Function_6_181F",         # 06, 6
        "Function_7_1833",         # 07, 7
        "Function_8_1847",         # 08, 8
        "Function_9_185B",         # 09, 9
        "Function_10_1A7D",        # 0A, 10
        "Function_11_1A9B",        # 0B, 11
        "Function_12_1B05",        # 0C, 12
        "Function_13_2288",        # 0D, 13
        "Function_14_312D",        # 0E, 14
    ))


    def Function_0_B48(): pass

    label("Function_0_B48")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_B88"),
        (1, "loc_B94"),
        (2, "loc_BA0"),
        (3, "loc_BAC"),
        (4, "loc_BB8"),
        (5, "loc_BC4"),
        (6, "loc_BD0"),
        (SWITCH_DEFAULT, "loc_BDC"),
    )


    label("loc_B88")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_BE8")

    label("loc_B94")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_BE8")

    label("loc_BA0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_BE8")

    label("loc_BAC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_BE8")

    label("loc_BB8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_BE8")

    label("loc_BC4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_BE8")

    label("loc_BD0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BE8")

    label("loc_BDC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BE8")

    label("loc_BE8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BFF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BE8")

    label("loc_BFF")

    Return()

    # Function_0_B48 end

    def Function_1_C00(): pass

    label("Function_1_C00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C1E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_C00")

    label("loc_C1E")

    Return()

    # Function_1_C00 end

    def Function_2_C1F(): pass

    label("Function_2_C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C32")
    ClearChrFlags(0x8, 0x80)

    label("loc_C32")

    Call(0, 10)
    Return()

    # Function_2_C1F end

    def Function_3_C36(): pass

    label("Function_3_C36")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6F")
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)

    label("loc_C6F")

    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x3, 0x4)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_13D5")
    Jump("loc_1412")

    label("loc_13D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1412")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_13EF")
    Jump("loc_1412")

    label("loc_13EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_1401")
    Jump("loc_1412")

    label("loc_1401")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_1412")
    OP_66(0x5, 0x1)

    label("loc_1412")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1434")
    SetChrFlags(0x16, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_1448")

    label("loc_1434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1448")
    ClearChrFlags(0x16, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1448")

    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x16, 0x100)
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1476")
    OP_70(0x0, 0x0)
    Jump("loc_147A")

    label("loc_1476")

    OP_70(0x0, 0x1E)

    label("loc_147A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148D")
    OP_70(0x1, 0x0)
    Jump("loc_1491")

    label("loc_148D")

    OP_70(0x1, 0x1E)

    label("loc_1491")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 4)), scpexpr(EXPR_END)), "loc_14FB")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -4460, 0, -4850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)
    Jump("loc_15B2")

    label("loc_14FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 5)), scpexpr(EXPR_END)), "loc_1559")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -66530, -1000, -40600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)
    Jump("loc_15B2")

    label("loc_1559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 6)), scpexpr(EXPR_END)), "loc_15B2")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -122090, -10, -9540, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_15B2")

    Return()

    # Function_3_C36 end

    def Function_4_15B3(): pass

    label("Function_4_15B3")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A0")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅰ', 1)"), scpexpr(EXPR_END)), "loc_1632")
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
    SetScenarioFlags(0x118, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_169B")

    label("loc_1632")

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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_169B")

    Jump("loc_16DD")

    label("loc_16A0")

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

    label("loc_16DD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_15B3 end

    def Function_5_16E9(): pass

    label("Function_5_16E9")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D6")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('土人偶', 1)"), scpexpr(EXPR_END)), "loc_1768")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x118, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_17D1")

    label("loc_1768")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17D1")

    Jump("loc_1813")

    label("loc_17D6")

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

    label("loc_1813")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16E9 end

    def Function_6_181F(): pass

    label("Function_6_181F")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 4)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_181F end

    def Function_7_1833(): pass

    label("Function_7_1833")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 5)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_1833 end

    def Function_8_1847(): pass

    label("Function_8_1847")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1847 end

    def Function_9_185B(): pass

    label("Function_9_185B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 2)), scpexpr(EXPR_END)), "loc_1865")
    Return()

    label("loc_1865")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【消灭】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1931"),
        (SWITCH_DEFAULT, "loc_1948"),
    )


    label("loc_1931")

    Sleep(500)
    OP_90(0x0, -70820, -1000, -33900, 225)
    EventEnd(0x5)
    Return()

    label("loc_1948")

    Battle("BattleInfo_99C", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(-70820, 0, -33900, 0)
    OP_90(0x0, -70820, -1000, -33900, 225)
    OP_90(0x1, -70820, -1000, -33900, 225)
    OP_90(0x2, -70820, -1000, -33900, 225)
    OP_90(0x3, -70820, -1000, -33900, 225)
    OP_90(0x4, -70820, -1000, -33900, 225)
    OP_90(0x5, -70820, -1000, -33900, 225)
    OP_90(0x6, -70820, -1000, -33900, 225)
    OP_90(0x7, -70820, -1000, -33900, 225)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_1A0A"),
        (1, "loc_1A0D"),
        (SWITCH_DEFAULT, "loc_1A10"),
    )


    label("loc_1A0A")

    EventEnd(0x5)
    Return()

    label("loc_1A0D")

    OP_B7(0x0)
    Return()

    label("loc_1A10")

    EventBegin(0x1)
    SetChrFlags(0x16, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_0D()
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "消灭了通缉魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x79, 2)
    OP_29(0x2F, 0x4, 0x10)
    OP_29(0x2F, 0x4, 0x2)
    OP_29(0x2F, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_9_185B end

    def Function_10_1A7D(): pass

    label("Function_10_1A7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A9A")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_1A9A")

    Return()

    # Function_10_1A7D end

    def Function_11_1A9B(): pass

    label("Function_11_1A9B")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        (
            "啊啊，如果我当时认真\x01",
            "确认装货情况的话，\x01",
            "就不会发生这种……！\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "总、总之，\x01",
            "请找到那个孩子！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1A9B end

    def Function_12_1B05(): pass

    label("Function_12_1B05")

    EventBegin(0x0)
    OP_E0(0x3)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_93(0x8, 0xE1, 0x0)
    Fade(1000)
    OP_68(-75330, 1300, 6410, 0)
    MoveCamera(20, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(-75840, 1300, 7500, 1500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BCA")
    SetChrPos(0x101, -75760, 0, 7730, 315)
    SetChrPos(0x102, -74340, 0, 7660, 315)
    SetChrPos(0x103, -75880, 0, 5340, 315)
    SetChrPos(0x104, -73920, 0, 5600, 315)
    SetChrPos(0x160, -74970, 0, 4520, 315)
    Jump("loc_1CFD")

    label("loc_1BCA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C32")
    SetChrPos(0x101, -74340, 0, 7660, 315)
    SetChrPos(0x102, -75760, 0, 7730, 315)
    SetChrPos(0x103, -75880, 0, 5340, 315)
    SetChrPos(0x104, -73920, 0, 5600, 315)
    SetChrPos(0x160, -74970, 0, 4520, 315)
    Jump("loc_1CFD")

    label("loc_1C32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C9A")
    SetChrPos(0x101, -75880, 0, 5340, 315)
    SetChrPos(0x102, -74340, 0, 7660, 315)
    SetChrPos(0x103, -75760, 0, 7730, 315)
    SetChrPos(0x104, -73920, 0, 5600, 315)
    SetChrPos(0x160, -74970, 0, 4520, 315)
    Jump("loc_1CFD")

    label("loc_1C9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CFD")
    SetChrPos(0x101, -73920, 0, 5600, 315)
    SetChrPos(0x102, -74340, 0, 7660, 315)
    SetChrPos(0x103, -75880, 0, 5340, 315)
    SetChrPos(0x104, -75760, 0, 7730, 315)
    SetChrPos(0x160, -74970, 0, 4520, 315)

    label("loc_1CFD")

    OP_0D()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D46")

    #C0011
    ChrTalk(
        0x101,
        "#0005F#11P啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD0")

    label("loc_1D46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D75")

    #C0012
    ChrTalk(
        0x102,
        "#0101F#11P找到了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD0")

    label("loc_1D75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA4")

    #C0013
    ChrTalk(
        0x103,
        "#0201F#11P发现目标……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD0")

    label("loc_1DA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DD0")

    #C0014
    ChrTalk(
        0x104,
        "#0301F#11P原来在这里吗！\x02",
    )

    CloseMessageWindow()

    label("loc_1DD0")

    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-84580, 900, 18690, 0)
    MoveCamera(37, 19, 0, 0)
    MoveCamera(18, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19950, 0)
    SetCameraDistance(18950, 2000)
    SetChrPos(0x101, -78290, 0, 11660, 315)
    SetChrPos(0x102, -76720, 0, 12340, 315)
    SetChrPos(0x103, -77250, 0, 10600, 315)
    SetChrPos(0x104, -75680, 0, 11560, 315)
    SetChrPos(0x160, -79910, 0, 11150, 315)
    OP_6F(0x79)
    OP_0D()

    #C0015
    ChrTalk(
        0x8,
        (
            "#11P呜呜呜……\x01",
            "……快点来啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        "#11P这样下去，那个孩子会……！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, -73080, 0, 15330, 315)

    #C0017
    ChrTalk(
        0x101,
        "#0007F#1P喂——！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrPos(0x101, -78290, 0, 11660, 315)
    OP_93(0x8, 0x87, 0x1F4)
    OP_68(-83980, 900, 18240, 2500)

    def lambda_1F2E():
        OP_95(0xFE, -83600, 0, 17100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F2E)

    def lambda_1F48():
        OP_95(0xFE, -82500, 0, 18200, 2900, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F48)

    def lambda_1F62():
        OP_95(0xFE, -82500, 0, 16000, 2800, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F62)

    def lambda_1F7C():
        OP_95(0xFE, -81400, 0, 17100, 2700, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F7C)
    Sleep(500)

    def lambda_1F99():
        OP_95(0xFE, -84900, 0, 16600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_1F99)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0018
    ChrTalk(
        0x8,
        "#5P来、来了吗！\x02",
    )

    WaitChrThread(0x160, 1)
    OP_93(0x160, 0x0, 0x1F4)
    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "#5P太好了……\x01",
            "你们来得很快啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0001F#12P不，让您久等了。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x160,
        (
            "#3303F#6P──我说，大哥哥。\x02\x03",

            "#3301F在那个孩子不见了之后，\x01",
            "你有没有听见悲鸣或呻吟声？\x02\x03",

            "或者是类似\x01",
            "有东西落下悬崖的声音。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_20AD():
        TurnDirection(0xFE, 0x160, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20AD)

    def lambda_20BA():
        TurnDirection(0xFE, 0x160, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20BA)
    Sleep(100)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_20DC():
        TurnDirection(0xFE, 0x160, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20DC)

    def lambda_20E9():
        TurnDirection(0xFE, 0x160, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20E9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0022
    ChrTalk(
        0x8,
        "#5P咦咦咦咦……？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#5P没、没有！\x01",
            "我想应该没有听到……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x160,
        (
            "#3304F#6P……那么，\x01",
            "很有可能还平安无事呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x160, 0x101, 500)
    Sleep(300)

    #C0025
    ChrTalk(
        0x160,
        "#3300F#6P大哥哥，赶快前进吧。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#0005F#11P啊，是啊……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        "#0302F#11P（哈哈，怎么说呢……）\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0108F#11P（对情况的判断十分正确……\x01",
            "  怎么看都不像是小孩子的思路呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        "#0206F#11P（这下能相信她是『小猫』了。）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -83600, 0, 17100, 315)
    OP_4C(0x8, 0xFF)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xA3, 1)
    OP_29(0x46, 0x1, 0xD)
    OP_E0(0x2)
    Call(0, 10)
    EventEnd(0x5)
    Return()

    # Function_12_1B05 end

    def Function_13_2288(): pass

    label("Function_13_2288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2368")
    TalkBegin(0xFF)
    OP_93(0x0, 0x15E, 0x0)

    #C0030
    ChrTalk(
        0x101,
        (
            "#0001F（格蕾丝小姐委托我们拍摄的照片，\x01",
            "  似乎能在这里拍到……）\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x160,
        (
            "#3301F……大哥哥？\x01",
            "你在干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#0003F啊、抱歉。\x02\x03",

            "#0001F（……眼下没有拍照的\x01",
            "  闲暇了。\x01",
            "  快点去寻找柯林吧。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_312C")

    label("loc_2368")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-84950, -100, 31330, 0)
    MoveCamera(27, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23410, 0)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, -84440, 0, 26710, 350)
    SetChrPos(0x102, -82980, 0, 27830, 350)
    SetChrPos(0x103, -86040, 0, 27310, 35)
    SetChrPos(0x104, -81800, 0, 26750, 35)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x3, 0x9)
    OP_49()
    SetChrPos(0x9, -120000, -15000, 56000, 0)
    OP_D3(0x9, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0033
    ChrTalk(
        0x101,
        "#12P#0000F这是……横贯大陆的铁路轨道吗。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        (
            "#12P#0300F连接帝国和共和国的铁轨……\x01",
            "贯穿了克洛斯贝尔自治州\x01",
            "的正中央啊。\x02\x03",

            "#0303F仔细想想的话，确实很了不起呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#12P#0103F克洛斯贝尔的商品流通\x01",
            "也要依靠货物列车来支撑……\x02\x03",

            "#0100F说它是克洛斯贝尔如今的\x01",
            "象征也没错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#12P#0003F格蕾丝小姐委托我们拍摄的那些照片……\x01",
            "加进一张行驶中的列车的照片\x01",
            "似乎也不错……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_25E6():
        OP_93(0xFE, 0x131, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_25E6)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    def lambda_260F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_260F)

    def lambda_261C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_261C)

    def lambda_2629():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2629)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0037
    ChrTalk(
        0x101,
        (
            "#12P#0005F……？\x01",
            "怎么了，缇欧？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        "#6P#0200F……列车似乎正在接近。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0039
    ChrTalk(
        0x101,
        "#12P#0011F你、你说什么！？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#12P#0305F喂喂，\x01",
            "这就是所谓的\x01",
            "拍摄时机吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2727():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2727)
    WaitChrThread(0x101, 1)

    #C0041
    ChrTalk(
        0x101,
        "#12P#0011F艾、艾莉！准备好相机！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D1D")

    #C0042
    ChrTalk(
        0x102,
        (
            "#12P#0105F知、知道了……\x01",
            "稍等一下！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x15E, 0x1F4)
    OP_93(0x101, 0x15E, 0x1F4)
    OP_93(0x103, 0x15E, 0x1F4)
    OP_93(0x104, 0x15E, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    BeginChrThread(0x9, 3, 0, 14)
    Sleep(2000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    WaitChrThread(0x9, 3)
    OP_6F(0x79)

    #C0043
    ChrTalk(
        0x103,
        "#6P#0200F…………走掉了呢。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#12P#0300F刚才说不定是我第一次\x01",
            "好好观察\x01",
            "列车行驶的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2938():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2938)

    def lambda_2945():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2945)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    #C0045
    ChrTalk(
        0x101,
        "#12P#0000F艾莉……照片拍得怎么样了？\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    TurnDirection(0x102, 0x101, 500)

    #C0046
    ChrTalk(
        0x102,
        (
            "#12P#0100F大概……没问题吧。\x01",
            "在它通过这里之前，\x01",
            "总算来得及按下了快门。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0047
    ChrTalk(
        0x104,
        (
            "#12P#0300F什么啊，那样就没问题了吧。\x02\x03",

            "所谓摄影，不就是只要按下相机的快门\x01",
            "就能拍摄成功了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0048
    ChrTalk(
        0x102,
        (
            "#12P#0106F我说你啊……\x01",
            "要拍出好照片，\x01",
            "可没有那么简单哦。\x02\x03",

            "#0100F要注意确认\x01",
            "拍摄对象有没有被收入取景框中，\x01",
            "还要构思摄影角度……\x02\x03",

            "而且受到天气和风的影响，\x01",
            "照片所呈现出的感觉也会有很大不同。\x02\x03",

            "就像刚才一样，有的照片只要错过\x01",
            "那一瞬的时机，就再也拍不到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        (
            "#6P#0200F外行和专家所拍出的照片，\x01",
            "差别可是一目了然的。\x02\x03",

            "#0203F不过，某些粗神经的人\x01",
            "大概无法理解这种细致的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0050
    ChrTalk(
        0x104,
        (
            "#12P#0306F唔……\x01",
            "你在说谁啊，说谁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#12P#0000F总之……\x01",
            "艾莉干得很漂亮，\x01",
            "没有错过拍摄时机。\x02\x03",

            "对于久违的摄影，\x01",
            "这次虽然并不是很正式……\x01",
            "但你应该已经找回摄影的感觉了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0052
    ChrTalk(
        0x102,
        (
            "#12P#0100F也许吧。\x01",
            "在没有实际显像出来之前，\x01",
            "还无法确定……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#12P#0000F如果发现了这种风景漂亮的地方，\x01",
            "就再拍些照片吧。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30DD")

    label("loc_2D1D")


    #C0054
    ChrTalk(
        0x102,
        "#12P#0105F知、知道了……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x15E, 0x1F4)
    OP_93(0x101, 0x15E, 0x1F4)
    OP_93(0x103, 0x15E, 0x1F4)
    OP_93(0x104, 0x15E, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    BeginChrThread(0x9, 3, 0, 14)
    Sleep(2000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    WaitChrThread(0x9, 3)

    #C0055
    ChrTalk(
        0x103,
        "#6P#0200F…………走掉了呢。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#12P#0300F刚才说不定是我第一次\x01",
            "仔细观察\x01",
            "列车行驶的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#12P#0000F……艾莉，照片拍得怎么样了？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#12P#0100F因为拍摄对象是移动中的物体，\x01",
            "所以有些紧张……\x01",
            "不过，嗯，大概没问题吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2F37")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_2F4E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2F65")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_2F7C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2F93")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_2FAA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2FC1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2FD8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_2FEF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_308E")

    #C0059
    ChrTalk(
        0x101,
        (
            "#12P#0000F是吗……没有错过拍摄时机，\x01",
            "干得漂亮，辛苦了。\x02\x03",

            "这样一来，就拍完了格蕾丝小姐\x01",
            "所要求的五张照片了。\x01",
            "现在随时都可以去交付了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30DD")

    label("loc_308E")


    #C0060
    ChrTalk(
        0x101,
        (
            "#12P#0000F是吗……没有错过拍摄时机，\x01",
            "干得漂亮，辛苦了。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30DD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -84030, 0, 26840, 350)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x7)
    SetChrFlags(0x9, 0x80)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x3, 0x1000)
    ClearMapFlags(0x8000000)
    OP_37()
    Call(0, 10)
    OP_65(0x5, 0x1)
    Sleep(500)
    EventEnd(0x5)

    label("loc_312C")

    Return()

    # Function_13_2288 end

    def Function_14_312D(): pass

    label("Function_14_312D")


    def lambda_3132():
        OP_95(0xFE, 80000, -15000, 56000, 25000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3132)
    Sound(451, 0, 100, 0)
    Fade(500)
    OP_68(-77630, 200, 37840, 0)
    MoveCamera(341, 31, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19310, 0)
    OP_0D()
    OP_68(-80740, 200, 33810, 4000)
    MoveCamera(58, 26, 0, 4000)
    OP_6E(510, 2000)
    SetCameraDistance(19310, 2000)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    Fade(1000)
    OP_68(-84950, -100, 31330, 0)
    MoveCamera(27, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23410, 0)
    OP_0D()
    Return()

    # Function_14_312D end

    SaveToFile()

Try(main)
