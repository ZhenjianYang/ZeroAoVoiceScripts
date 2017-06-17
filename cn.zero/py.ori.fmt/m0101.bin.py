from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m0101.bin",                # FileName
        "m0101",                    # MapName
        "m0101",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -3000, 0, 0, 0, 0, 1, 104, 0, 2, 0, 3],
    )

    BuildStringList((
        "m0101",                  # 0
        "约纳",                   # 1
        "餐具",                   # 2
        "餐具",                   # 3
        "餐具",                   # 4
        "餐具",                   # 5
        "餐具",                   # 6
        "餐具",                   # 7
        "黑玉乌龟",               # 8
        "蛇虎鱼",                 # 9
        "SE控制",                 # 10
        "bm0101",                 # 11
        "bm0101",                 # 12
        "bm0101",                 # 13
        "bm0101",                 # 14
        "bm0100",                 # 15
        "bm0100",                 # 16
        "bm0100",                 # 17
        "bm0100",                 # 18
        "bm0100",                 # 19
        "bm0100",                 # 20
    ))

    ATBonus("ATBonus_4E8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_BB87", 12,  1,   8,   0,   3,   7,   0)
    Sepith("Sepith_BB77", 0,   12,  5,   0,   7,   2,   6)
    Sepith("Sepith_BB8F", 0,   0,   0,   10,  7,   7,   7)
    Sepith("Sepith_BB7F", 8,   0,   12,  0,   0,   5,   7)

    MonsterBattlePostion("MonsterBattlePostion_588", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_58C", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_590", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A0", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_5D8", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_5DC", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_5E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_568", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_56C", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_570", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_574", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_578", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_57C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_580", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_584", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_548", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_54C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_550", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_554", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_558", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_55C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_560", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_564", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C4", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_528", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_52C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_530", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_534", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_538", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_53C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_540", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_544", 2, 13, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_778", 0x0000, 18, 6, 60, 6, 1, 25, 0, "bm0101", "Sepith_BB87", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
        )
    )

    BattleInfo(
        "BattleInfo_5E8", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_BB77", 30, 45, 20, 5,
        (
            ("ms63800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms63800.dat", "ms63800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms63800.dat", "ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
        )
    )

    BattleInfo(
        "BattleInfo_B60", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_BB8F", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_548", "MonsterBattlePostion_5A8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_528", "MonsterBattlePostion_5A8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_548", "MonsterBattlePostion_5A8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_528", "MonsterBattlePostion_5A8", "ed7400", "ed7403", "ATBonus_4E8"),
        )
    )

    BattleInfo(
        "BattleInfo_840", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_BB8F", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
        )
    )

    BattleInfo(
        "BattleInfo_6B0", 0x0000, 18, 6, 60, 6, 1, 30, 0, "bm0101", "Sepith_BB7F", 30, 45, 20, 5,
        (
            ("ms68700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms68700.dat", "ms68700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms68700.dat", "ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_C28", 0x0000, 18, 6, 60, 0, 1, 0, 0, "bm0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75800.dat", "ms75800.dat", "ms75800.dat", "ms68700.dat", "ms68700.dat", "ms75800.dat", 0, 0, "MonsterBattlePostion_528", "MonsterBattlePostion_5A8", "ed7401", "ed7403", "ATBonus_4E8"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C6C", 0x0000, 18, 6, 60, 0, 1, 0, 0, "bm0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63800.dat", "ms63800.dat", "ms68700.dat", "ms63800.dat", "ms63800.dat", "ms68700.dat", 0, 0, "MonsterBattlePostion_528", "MonsterBattlePostion_5A8", "ed7401", "ed7403", "ATBonus_4E8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch06100.itc",                   # 00
        "chr/ch06102.itc",                   # 01
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
        "monster/ch63850.itc",               # 10
        "monster/ch63851.itc",               # 11
        "monster/ch68750.itc",               # 12
        "monster/ch68750.itc",               # 13
        "monster/ch75850.itc",               # 14
        "monster/ch75851.itc",               # 15
        "monster/ch60550.itc",               # 16
        "monster/ch60550.itc",               # 17
    ))

    DeclNpc(498200,  200,     302000,  0,    261,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(109959,  -5500,   19,      0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(92000,   -8500,   90500,   0,    484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(99960,   100050,  -10000,  0x1010000,    "BattleInfo_778", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(100360,  200740,  0,       0x1010000,    "BattleInfo_5E8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-290,    199690,  0,       0x1010000,    "BattleInfo_B60", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(109910,  99810,   -7000,   0x1010000,    "BattleInfo_840", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(200810,  94840,   0,       0x1010000,    "BattleInfo_778", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(199760,  195940,  -10000,  0x1010000,    "BattleInfo_6B0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(202350,  204410,  -10000,  0x1010000,    "BattleInfo_5E8", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 33,  504.5,                 200.0,                 -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -252.25,               -100.0,                0.20000000298023224,   1.0])

    DeclActor(109960,  -6000,   20,      1200,    109960,  -5000,   20,      0x007C, 0,  5,  0x0000)
    DeclActor(109970,  -3000,   113430,  1200,    109970,  -2000,   113430,  0x007C, 0,  6,  0x0000)
    DeclActor(190010,  -4000,   200010,  1200,    190010,  -3000,   200010,  0x007C, 0,  7,  0x0000)
    DeclActor(92000,   -9000,   90500,   1200,    92000,   -8000,   90500,   0x007C, 0,  8,  0x0000)
    DeclActor(500000,  150,     208500,  1200,    500000,  1150,    208500,  0x007C, 0,  19, 0x0000)
    DeclActor(2000,    0,       0,       1200,    2500,    1000,    0,       0x007C, 0,  17, 0x0000)
    DeclActor(108000,  -6000,   2500,    2000,    108000,  -5000,   2500,    0x007C, 0,  13, 0x0000)
    DeclActor(85500,   -6000,   103000,  2000,    85500,   -5000,   103000,  0x007C, 0,  14, 0x0000)
    DeclActor(203430,  -6000,   184020,  2000,    203430,  -5000,   184020,  0x007C, 0,  15, 0x0000)
    DeclActor(320000,  -1000,   302800,  1200,    320000,  500,     302800,  0x007C, 0,  12, 0x0000)
    DeclActor(496130,  0,       296360,  1200,    496130,  1000,    296360,  0x007C, 0,  11, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7

    ScpFunction((
        "Function_0_D98",          # 00, 0
        "Function_1_DB5",          # 01, 1
        "Function_2_DD4",          # 02, 2
        "Function_3_E94",          # 03, 3
        "Function_4_1503",         # 04, 4
        "Function_5_15DD",         # 05, 5
        "Function_6_17D7",         # 06, 6
        "Function_7_190D",         # 07, 7
        "Function_8_1A43",         # 08, 8
        "Function_9_1C3D",         # 09, 9
        "Function_10_46C0",        # 0A, 10
        "Function_11_493E",        # 0B, 11
        "Function_12_4A8A",        # 0C, 12
        "Function_13_4B7D",        # 0D, 13
        "Function_14_4B99",        # 0E, 14
        "Function_15_4BB5",        # 0F, 15
        "Function_16_4BD1",        # 10, 16
        "Function_17_50B7",        # 11, 17
        "Function_18_5239",        # 12, 18
        "Function_19_5380",        # 13, 19
        "Function_20_5405",        # 14, 20
        "Function_21_5BC3",        # 15, 21
        "Function_22_5C1F",        # 16, 22
        "Function_23_5FC1",        # 17, 23
        "Function_24_8733",        # 18, 24
        "Function_25_87ED",        # 19, 25
        "Function_26_A606",        # 1A, 26
        "Function_27_A6C0",        # 1B, 27
        "Function_28_A704",        # 1C, 28
        "Function_29_A76D",        # 1D, 29
        "Function_30_AC7D",        # 1E, 30
        "Function_31_BA88",        # 1F, 31
        "Function_32_BAA3",        # 20, 32
        "Function_33_BAE9",        # 21, 33
    ))


    def Function_0_D98(): pass

    label("Function_0_D98")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DB4")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_D98")

    label("loc_DB4")

    Return()

    # Function_0_D98 end

    def Function_1_DB5(): pass

    label("Function_1_DB5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DD3")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_DB5")

    label("loc_DD3")

    Return()

    # Function_1_DB5 end

    def Function_2_DD4(): pass

    label("Function_2_DD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFC")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFC")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)

    label("loc_DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_E0A")
    Jump("loc_E37")

    label("loc_E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E29")
    SetChrPos(0x8, 497850, 200, 296250, 270)
    Jump("loc_E37")

    label("loc_E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_END)), "loc_E37")
    Jump("loc_E37")

    label("loc_E37")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E56")
    Event(0, 22)
    Jump("loc_E70")

    label("loc_E56")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E70")
    Event(0, 25)

    label("loc_E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_E84")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 20)
    Jump("loc_E93")

    label("loc_E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_E93")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 30)

    label("loc_E93")

    Return()

    # Function_2_DD4 end

    def Function_3_E94(): pass

    label("Function_3_E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x86), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EDB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x209), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x28, 0xC8)
    Jump("loc_EF8")

    label("loc_EDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x209), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x64, 0xC8)

    label("loc_EF8")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F14")
    ClearMapObjFlags(0x13, 0x10)
    OP_66(0x4, 0x1)

    label("loc_F14")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F28")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_F28")

    ClearMapObjFlags(0x18, 0x10)
    OP_70(0x18, 0x1E)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x86), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F67")
    SetMapFlags(0x2000)
    OP_E0(0x0)
    Jump("loc_F6C")

    label("loc_F67")

    ClearMapFlags(0x2000)

    label("loc_F6C")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 106000, -6000, 0, 6000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 98000, -6000, 0, 6000, 2000, 90000)
    SetBarrier(0x0, 0x2, 0x1, 0x0, 100000, -7380, 89000, 4000, 2000, 0)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 100000, -7800, 110000, 4000, 2000, 0)
    SetBarrier(0x0, 0x4, 0x1, 0x0, 96000, -7000, 100000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, 104000, -7000, 100000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x6, 0x1, 0x0, 92000, -8000, 96000, 4000, 2000, 0)
    SetBarrier(0x0, 0x7, 0x1, 0x0, 0, -7000, 100000, 4000, 2000, 0)
    SetBarrier(0x0, 0x8, 0x1, 0x0, 0, -7000, 92000, 4000, 2000, 0)
    SetBarrier(0x0, 0x9, 0x1, 0x0, 200000, -8000, 190000, 8000, 2000, 0)
    SetBarrier(0x0, 0xA, 0x1, 0x0, 200000, -8000, 210000, 8000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 6)), scpexpr(EXPR_END)), "loc_1128")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetBarrier(0x2, 0x8, 0x1)
    SetBarrier(0x3, 0x9, 0x1)
    SetBarrier(0x3, 0xA, 0x1)
    SetMapObjFrame(0xE, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "Null", 0x2, "high")
    Jump("loc_1199")

    label("loc_1128")

    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetBarrier(0x3, 0x8, 0x1)
    SetBarrier(0x2, 0x9, 0x1)
    SetBarrier(0x2, 0xA, 0x1)
    SetMapObjFrame(0xE, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "Null", 0x2, "low")

    label("loc_1199")

    SetMapObjFrame(0x11, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x3, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x3, "light01", 0x0, 0x1)
    SetMapObjFrame(0x4, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x4, "light01", 0x0, 0x1)
    SetMapObjFrame(0x5, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x5, "light01", 0x0, 0x1)
    SetMapObjFrame(0x6, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x6, "light01", 0x0, 0x1)
    SetMapObjFrame(0x7, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x7, "light01", 0x0, 0x1)
    SetMapObjFrame(0x8, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x8, "light01", 0x0, 0x1)
    SetMapObjFrame(0x9, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x9, "light01", 0x0, 0x1)
    SetMapObjFrame(0xA, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xA, "light01", 0x0, 0x1)
    SetMapObjFrame(0xB, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xB, "light01", 0x0, 0x1)
    SetMapObjFrame(0xC, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xC, "light01", 0x0, 0x1)
    SetMapObjFrame(0xD, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xD, "light01", 0x0, 0x1)
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B6")
    OP_70(0x14, 0x0)
    Jump("loc_14BA")

    label("loc_14B6")

    OP_70(0x14, 0x1E)

    label("loc_14BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CD")
    OP_70(0x15, 0x0)
    Jump("loc_14D1")

    label("loc_14CD")

    OP_70(0x15, 0x1E)

    label("loc_14D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E4")
    OP_70(0x16, 0x0)
    Jump("loc_14E8")

    label("loc_14E4")

    OP_70(0x16, 0x1E)

    label("loc_14E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14FB")
    OP_70(0x17, 0x0)
    Jump("loc_14FF")

    label("loc_14FB")

    OP_70(0x17, 0x1E)

    label("loc_14FF")

    Call(0, 4)
    Return()

    # Function_3_E94 end

    def Function_4_1503(): pass

    label("Function_4_1503")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1525")
    SetMapObjFlags(0x14, 0x4)
    Jump("loc_152B")

    label("loc_1525")

    ClearMapObjFlags(0x14, 0x4)

    label("loc_152B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156A")
    SetChrFlags(0x15, 0x8)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x17, 0x4)
    Jump("loc_157B")

    label("loc_156A")

    ClearChrFlags(0x15, 0x8)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x17, 0x4)

    label("loc_157B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15AB")
    SetChrFlags(0x18, 0x8)
    SetMapObjFlags(0x16, 0x4)
    Jump("loc_15B6")

    label("loc_15AB")

    ClearChrFlags(0x18, 0x8)
    ClearMapObjFlags(0x16, 0x4)

    label("loc_15B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D7")
    SetChrFlags(0x16, 0x8)
    Jump("loc_15DC")

    label("loc_15D7")

    ClearChrFlags(0x16, 0x8)

    label("loc_15DC")

    Return()

    # Function_4_1503 end

    def Function_5_15DD(): pass

    label("Function_5_15DD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1799")
    Sound(14, 0, 100, 0)
    OP_71(0x14, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D6")
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xF, 0x0, 0)
    OP_98(0xF, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1636():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1636)

    def lambda_1650():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1650)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)

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
    WaitChrThread(0xF, 1)
    Battle("BattleInfo_C28", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_16B7"),
        (2, "loc_16C6"),
        (1, "loc_16D3"),
        (SWITCH_DEFAULT, "loc_16D6"),
    )


    label("loc_16B7")

    SetScenarioFlags(0x74, 6)
    OP_70(0x14, 0x1E)
    Sleep(500)
    Jump("loc_16D6")

    label("loc_16C6")

    OP_70(0x14, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_16D3")

    OP_B7(0x0)
    Return()

    label("loc_16D6")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('风耀珠', 1)"), scpexpr(EXPR_END)), "loc_172D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '风耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1794")

    label("loc_172D")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '风耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '风耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x14, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1794")

    Jump("loc_17CB")

    label("loc_1799")

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

    label("loc_17CB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_15DD end

    def Function_6_17D7(): pass

    label("Function_6_17D7")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C4")
    Sound(14, 0, 100, 0)
    OP_71(0x15, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('痊愈之药', 1)"), scpexpr(EXPR_END)), "loc_1856")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_18BF")

    label("loc_1856")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x15, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18BF")

    Jump("loc_1901")

    label("loc_18C4")

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

    label("loc_1901")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_17D7 end

    def Function_7_190D(): pass

    label("Function_7_190D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FA")
    Sound(14, 0, 100, 0)
    OP_71(0x16, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('中回复药', 1)"), scpexpr(EXPR_END)), "loc_198C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_19F5")

    label("loc_198C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x16, 0x1E, 0x0, 0x0, 0x0)

    label("loc_19F5")

    Jump("loc_1A37")

    label("loc_19FA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
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

    label("loc_1A37")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_190D end

    def Function_8_1A43(): pass

    label("Function_8_1A43")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BFF")
    Sound(14, 0, 100, 0)
    OP_71(0x17, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3C")
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x10, 0x0, 0)
    OP_98(0x10, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1A9C():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A9C)

    def lambda_1AB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1AB6)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x10, 1)
    Battle("BattleInfo_C6C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1B1D"),
        (2, "loc_1B2C"),
        (1, "loc_1B39"),
        (SWITCH_DEFAULT, "loc_1B3C"),
    )


    label("loc_1B1D")

    SetScenarioFlags(0x74, 7)
    OP_70(0x17, 0x1E)
    Sleep(500)
    Jump("loc_1B3C")

    label("loc_1B2C")

    OP_70(0x17, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1B39")

    OP_B7(0x0)
    Return()

    label("loc_1B3C")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('符文长袍', 1)"), scpexpr(EXPR_END)), "loc_1B93")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '符文长袍'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1BFA")

    label("loc_1B93")

    FadeToDark(300, 0, 100)

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '符文长袍'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '符文长袍'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x17, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1BFA")

    Jump("loc_1C31")

    label("loc_1BFF")

    FadeToDark(300, 0, 100)

    #A0014
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

    label("loc_1C31")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1A43 end

    def Function_9_1C3D(): pass

    label("Function_9_1C3D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CD1")
    Jump("loc_1D1B")

    label("loc_1CD1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1CF1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D1B")

    label("loc_1CF1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D11")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D1B")

    label("loc_1D11")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D1B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_20E6")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DD1")

    #C0015
    ChrTalk(
        0x8,
        (
            "#2306F呜啊～头好疼～……\x02\x03",

            "#2310F刚刚睡醒，根本就\x01",
            "没法顺利敲键盘啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0006F真是的……不然先去\x01",
            "洗个脸如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E1")

    label("loc_1DD1")


    #C0017
    ChrTalk(
        0x8,
        (
            "#2300F嗯～怎么回事……\x01",
            "你们要去哪里吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0000F嗯，稍微有点事。\x02\x03",

            "#0005F……怎么了，约纳，\x01",
            "我们来得不是时候吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EE1")
    Jump("loc_1F2B")

    label("loc_1EE1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F01")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F2B")

    label("loc_1F01")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F21")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F2B")

    label("loc_1F21")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F2B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0019
    ChrTalk(
        0x8,
        (
            "#2306F……刚才小睡了一下，\x01",
            "刚刚睡醒呢……\x02\x03",

            "这种事情看还看不出来吗……\x01",
            "所以说，真受不了你们这种\x01",
            "大脑迟钝的人啊～……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0006F呼，真是的……\x02\x03",

            "#0001F（虽然我也没资格说别人，\x01",
            "  但他的生活真是很没规律啊。）\x02\x03",

            "#0003F（果然还是应该和\x01",
            "  财团那边联络一下吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        (
            "#0211F……罗伊德前辈\x01",
            "一副监护人的表情呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 750)

    #C0022
    ChrTalk(
        0x101,
        "#0011F哎……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        "#0100F呵呵……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#0304F哎呀哎呀……\x01",
            "你也真是个老好人呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20E1")

    Jump("loc_46B8")

    label("loc_20E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_26F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_22E0")

    #C0025
    ChrTalk(
        0x8,
        (
            "#2310F可恶，竟敢小看我\x01",
            "天才约纳大人……\x01",
            "给我记住……！\x02\x03",

            "我一定会收集到\x01",
            "惊人的秘密情报，\x01",
            "让你们瞠目结舌！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2287")

    #C0026
    ChrTalk(
        0x10A,
        (
            "#0603F就保持这种干劲继续\x01",
            "搜集情报吧……\x02\x03",

            "稍后还会来问你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#2305F哎……？\x02\x03",

            "#2301F你、你这大叔是谁啊！\x01",
            "我才不要和你这种人\x01",
            "做什么交易呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x10A,
        (
            "#0600F到时候你就会知道我是谁了。\x01",
            "赶快工作吧，情报商。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0000F（哈哈，搜查一科果然已经\x01",
            "  对约纳的情况了如指掌了吗……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22DB")

    label("loc_2287")


    #C0030
    ChrTalk(
        0x103,
        (
            "#0203F（他作为情报商的自尊心\x01",
            "  好像受到伤害了呢。\x01",
            "  ……算了，反正也无所谓。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22DB")

    Jump("loc_26F4")

    label("loc_22E0")

    SetChrSubChip(0x8, 0x0)
    OP_63(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x8,
        (
            "#2306F嘁，什么嘛～\x01",
            "今天可没什么好情报。\x02\x03",

            "本来我还以为，那些黑手党之间的争斗\x01",
            "一定会出现什么新情况呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_240F")
    Jump("loc_2459")

    label("loc_240F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_242F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2459")

    label("loc_242F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_244F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2459")

    label("loc_244F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2459")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Sleep(1000)

    #C0032
    ChrTalk(
        0x8,
        (
            "#2305F哦，来得正好。\x02\x03",

            "#2302F我说，你们几个，\x01",
            "手头有没有什么好情报啊？\x02\x03",

            "#2309F现在，我可以出比平时高三成的价格\x01",
            "向你们收购哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    #C0033
    ChrTalk(
        0x101,
        (
            "#0006F嗯～看起来，我们\x01",
            "好像是白跑一趟了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        "#0108F本来还抱有一些希望的……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#0203F算了，虽然以情报通自居，\x01",
            "但终究也只是个靠不住的孩子而已。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2621")

    #C0036
    ChrTalk(
        0x10A,
        "#0603F……哼，只有这种程度吗？\x02",
    )

    CloseMessageWindow()

    label("loc_2621")

    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0037
    ChrTalk(
        0x8,
        (
            "#2305F什、什么嘛，这是什么反应……\x02\x03",

            "#2307F明白了，我现在就开始调查，\x01",
            "一定会取得你们\x01",
            "想要的情报的！\x02\x03",

            "好了，需要什么的话，\x01",
            "就尽管说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        (
            "#0300F哈哈……你还真是\x01",
            "相当争强好胜呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    SetScenarioFlags(0xCD, 2)

    label("loc_26F4")

    Jump("loc_46B8")

    label("loc_26F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_2922")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_27C4")

    #C0039
    ChrTalk(
        0x8,
        (
            "#2301F从这里到这里\x01",
            "是Ａ等级，从这里开始是Ｂ……\x02\x03",

            "鲁巴彻从某些地方新雇来了\x01",
            "猎兵团的传闻……\x01",
            "……算了，可信度不高，标成Ｃ级就行了。\x02\x03",

            "#2304F好了～那么，\x01",
            "今天会有多少客人呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_291D")

    label("loc_27C4")


    #C0040
    ChrTalk(
        0x8,
        (
            "#2309F找到了，找到了～！\x02\x03",

            "关于黑月受袭的情报，\x01",
            "已经陆陆续续收集到啦～！\x02\x03",

            "#2301F接下来，就是标记上重要度级别，\x01",
            "然后再打包保存……\x02\x03",

            "#2309F哈哈哈哈！\x01",
            "这下肯定会大赚一笔啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0041
    ChrTalk(
        0x101,
        "#0006F（好像很专注呢……）\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#0200F（算了，先不要管他了。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_291D")

    Jump("loc_46B8")

    label("loc_2922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2CB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_29F0")

    #C0043
    ChrTalk(
        0x8,
        (
            "#2305F一、一开始连我也很吃惊呢！\x01",
            "真是个惊人的大新闻啊。\x02\x03",

            "#2303F结果我一时激动过头，\x01",
            "就忍不住告诉了你们，\x01",
            "你们是不是该付我点酬金啊。\x02\x03",

            "#2300F不要那么生气嘛～\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0006F真是的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CB0")

    label("loc_29F0")

    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "约纳大口吃着外卖比萨。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0046
    ChrTalk(
        0x8,
        (
            "#2303F（嚼嚼嚼……咽下）\x02\x03",

            "#2300F对了，那边怎么样了，\x01",
            "就是黑月的事务所！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_2B16")

    #C0047
    ChrTalk(
        0x101,
        (
            "#0003F啊，那个吗……\x01",
            "………………………………\x02\x03",

            "#0001F……约纳，也许没必要提醒你。\x02\x03",

            "不过，这些情报，你可\x01",
            "一定不要在导力网络上贩卖啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        "#2305F呜啊，知道啦……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BCB")

    label("loc_2B16")


    #C0049
    ChrTalk(
        0x101,
        (
            "#0000F黑月那边，我们还没有去看呢，\x01",
            "现在正准备过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "#2306F嘁，什么嘛……\x02\x03",

            "快点去看，看完之后\x01",
            "可一定要来告诉我啊。\x02\x03",

            "#2300F还有很多客人伸长了脖子，\x01",
            "焦急地等待着我的消息呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BCB")


    #C0051
    ChrTalk(
        0x104,
        (
            "#0306F什么嘛，原来你把情报告诉我们\x01",
            "就是为了这个啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#0200F约纳……你胆子不小啊。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#2305F哇啊啊，那个……\x02\x03",

            "#2306F我只是想稍微\x01",
            "赚点情报费而已啊，\x01",
            "用得着那么生气吗～\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        (
            "#0106F（这个孩子的态度\x01",
            "  确实成问题呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2CB0")

    Jump("loc_46B8")

    label("loc_2CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2FEA")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 1)), scpexpr(EXPR_END)), "loc_2D5C")

    #C0055
    ChrTalk(
        0x8,
        (
            "#2306F（嗯嗯）……\x02\x03",

            "#2311F……唔唔唔，啊……\x01",
            "可恶的『小猫』……你竟敢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#0012F（还是和以前一样，\x01",
            "  又被玲轻松戏耍了吗……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE5")

    label("loc_2D5C")


    #C0057
    ChrTalk(
        0x8,
        "#2303F哼～……嗯嗯……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0058
    ChrTalk(
        0x104,
        "#0305F睡着了……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x109,
        (
            "#0500F难道说……\x01",
            "这个孩子就是芙兰所说的\x01",
            "『情报商』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#0104F嗯，是啊。\x01",
            "……不过他好像没法在白天工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#0206F约纳是个夜猫子，现在这个时间\x01",
            "对他来说可能有点勉强吧。\x02\x03",

            "#0202F……也就是说，在现在这个时间段，\x01",
            "应该可以通过导力网络\x01",
            "轻松侵入这里。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 750)

    #C0062
    ChrTalk(
        0x101,
        (
            "#0005F原、原来如此……\x02\x03",

            "#0006F不对！这么做是不行的，缇欧。\x01",
            "黑客这种行为……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 750)

    #C0063
    ChrTalk(
        0x103,
        (
            "#0204F目前来说，并不算是犯罪……\x01",
            "而且我也只是偶尔为之罢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#0006F嗯、嗯～那好吧。\x02\x03",

            "#0001F不过，只有才万不得已的\x01",
            "情况下才能这么做哦……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 1)

    label("loc_2FE5")

    Jump("loc_46B8")

    label("loc_2FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_344E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 3)), scpexpr(EXPR_END)), "loc_30DA")

    #C0065
    ChrTalk(
        0x8,
        (
            "#2306F关于『黑之竞拍会』，\x01",
            "我提供的情报好像\x01",
            "起到了很大作用……\x02\x03",

            "#2301F那个，这次就算是稍微\x01",
            "给你们一点特别服务。\x01",
            "可要好好感谢我啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x153,
        (
            "#1110F咦～？\x01",
            "脸为什么红了呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#2311F#4S哇啊啊～～……\x01",
            "真多嘴～～！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3449")

    label("loc_30DA")


    #C0068
    ChrTalk(
        0x153,
        (
            "#1105F……咦～？\x01",
            "是经常和缇欧用终端\x01",
            "说话的那个人～\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "#2305F哦，和当时说的那个小鬼头\x01",
            "一起出门了啊。\x02\x03",

            "#2302F哈哈，都一个星期没有出门了，\x01",
            "感觉外面的阳光怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#0006F唯独不想被你这种\x01",
            "从不出门的家伙这样说啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "#2304F明明是偷偷潜入地下竞拍会\x01",
            "的你们更奇怪嘛～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_323C")

    #C0072
    ChrTalk(
        0x102,
        (
            "#0101F那么，约纳，你最后找到了\x01",
            "什么关于琪雅的情报吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D2")

    label("loc_323C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3286")

    #C0073
    ChrTalk(
        0x103,
        (
            "#0201F约纳，最后有没有\x01",
            "发现关于琪雅的情报……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32D2")

    label("loc_3286")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32D2")

    #C0074
    ChrTalk(
        0x104,
        (
            "#0301F那么，阿约，\x01",
            "你最后有没有找到\x01",
            "关于阿琪的情报啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D2")


    #C0075
    ChrTalk(
        0x8,
        (
            "#2305F啊～自那之后，\x01",
            "我已经竭尽全力，\x01",
            "把一切该找的地方都找过了……\x02\x03",

            "#2301F但完全查不到她的身世与经历。\x01",
            "至少现在基本可以断言，导力网络中\x01",
            "根本就不存在有关她的资料呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#0003F果然是这样吗……\x02\x03",

            "#0000F谢啦，\x01",
            "这次真是麻烦你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "#2307F我、我可没打算要\x01",
            "帮助你们的……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0078
    ChrTalk(
        0x8,
        (
            "#2306F情报费什么的都好说，\x01",
            "下次要是有什么重大消息，就来告诉我吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 3)

    label("loc_3449")

    Jump("loc_46B8")

    label("loc_344E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3661")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_34DC")

    #C0079
    ChrTalk(
        0x8,
        (
            "#2302F算了，不管你们要去什么地方，\x01",
            "总之小心一点吧。\x02\x03",

            "今天庆典就要结束了，\x01",
            "人流量可真是惊人。\x01",
            "警察忙得不可开交呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_365C")

    label("loc_34DC")


    #C0080
    ChrTalk(
        0x8,
        (
            "#2301F嗯～怎么，是你们啊。\x01",
            "要去什么地方吗？\x02\x03",

            "#2305F说起来，今天是最终日了吧。\x01",
            "也就是那个『黑之竞拍会』的……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0081
    ChrTalk(
        0x8,
        (
            "#2309F哈哈，终究是不可能的吧！\x02\x03",

            "#2302F算了，不管你们要去什么地方，\x01",
            "总之小心一点吧。\x02\x03",

            "今天庆典就要结束了，\x01",
            "人流量可真是惊人。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#0301F还真是一如既往\x01",
            "狂妄自大的小鬼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#0006F我们才应该提醒你\x01",
            "小心一点，不要在网络上\x01",
            "惹出什么麻烦呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_365C")

    Jump("loc_46B8")

    label("loc_3661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_386E")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_36F2")

    #C0084
    ChrTalk(
        0x8,
        (
            "#2310F『小猫』应该和我一样，\x01",
            "也是个不爱出门的家伙……\x02\x03",

            "不会参加现实生活中的庆典吧……\x01",
            "………（自言自语）…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3869")

    label("loc_36F2")


    #C0085
    ChrTalk(
        0x8,
        (
            "#2310F可恶……『小猫』那家伙，\x01",
            "今天完全都没有出现。\x02\x03",

            "#2305F难道是出去\x01",
            "观赏游行了吗……\x02\x03",

            "#2303F不不，才不会吧。\x01",
            "『小猫』应该和我一样，\x01",
            "也是个不爱出门的家伙……\x02\x03",

            "不会参加现实生活中的庆典吧……\x01",
            "………（自言自语）…………\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#0006F（虽然不太明白……\x01",
            "  但他好像已经擅自将『小猫』\x01",
            "  归为自己的同类了呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x103,
        (
            "#0202F（约纳跟外表相反，其实\x01",
            "  也是个容易感到寂寞的人呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3869")

    Jump("loc_46B8")

    label("loc_386E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3919")

    #C0088
    ChrTalk(
        0x8,
        (
            "#2310F缇欧·普拉托\x01",
            "在我打败『小猫』之后，下一个就轮到你了，\x02\x03",

            "做好觉悟吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x103,
        (
            "#0205F约纳……\x01",
            "你还真是意外地清闲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        "#2311F吵、吵死了～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C84")

    label("loc_3919")


    #C0091
    ChrTalk(
        0x101,
        (
            "#0002F约纳，多谢你昨天\x01",
            "提供的有益情报，\x01",
            "对我们有很大帮助。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "#2309F对吧～？\x01",
            "特别是那个『黑之竞拍会』……\x02\x03",

            "#2305F……啊，你们仔细\x01",
            "看过资料了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#0103F在米修拉姆召开的大规模集会，\x01",
            "期间会拍卖来路不正的赃物，还有地下社交界……\x02\x03",

            "#0101F这可真是让人大吃一惊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "#2309F哈，很不错的反应嘛。\x02\x03",

            "#2304F我以前也是半信半疑的，\x01",
            "但在偶然间发现了一处可靠的情报来源。\x02\x03",

            "#2302F我觉得你们大概会感兴趣，\x01",
            "所以就告诉你们了！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x103,
        "#0206F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "#2302F啊，缇欧。\x01",
            "解开那个要花多长时间？\x02\x03",

            "#2309F如果要苦战一个小时的话，\x01",
            "未免也太慢了。换作是我，\x01",
            "这个时间足够完成两次了！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x103,
        (
            "#0204F……三十秒都用不了。\x01",
            "因为，约纳你的思维模式\x01",
            "非常容易看穿。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        "#2307F呜啊……！？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#0306F阿约，\x01",
            "你还是放弃和\x01",
            "阿缇纠缠吧。\x02\x03",

            "#0300F你是赢不了她的。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "#2310F可恶！下次，\x01",
            "下次一定要……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)

    label("loc_3C84")

    Jump("loc_46B8")

    label("loc_3C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3E8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D02")

    #C0101
    ChrTalk(
        0x8,
        (
            "#2301F总、总之，赶快去\x01",
            "『第３控制终端』吧。\x02\x03",

            "#2306F如果等到『小猫』出现之后，\x01",
            "可就来不及了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E8A")

    label("loc_3D02")


    #C0102
    ChrTalk(
        0x8,
        (
            "#2300F黑客『小猫』是在\x01",
            "大约半年前出现，\x01",
            "并开始对我进行各种挑衅的。\x02\x03",

            "#2302F嘿嘿，但本天才\x01",
            "约纳大人今天一定会\x01",
            "抓住那家伙的尾巴。\x02\x03",

            "#2301F『第３控制终端』\x01",
            "在地下空间Ａ区域的深处，\x01",
            "要从克洛斯贝尔车站前的入口进入。\x02\x03",

            "好啦，你们两个\x01",
            "就不要再磨磨蹭蹭了～！\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x103,
        "#0203F约纳，你的态度似乎有点狂妄哦。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#0006F我们就算放弃\x01",
            "与你的合作也无所谓。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#2306F对不起，两位，\x01",
            "请你们尽量迅速一些……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3E8A")

    Jump("loc_46B8")

    label("loc_3E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 4)), scpexpr(EXPR_END)), "loc_3EA0")
    Call(0, 10)
    Jump("loc_46B8")

    label("loc_3EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4069")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F07")

    #C0106
    ChrTalk(
        0x8,
        (
            "#2310F而、而且竟然还\x01",
            "把我的那个秘密给……\x02\x03",

            "绝对不能原谅！\x01",
            "（狂敲键盘）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4064")

    label("loc_3F07")


    #C0107
    ChrTalk(
        0x8,
        (
            "#2311F啊～真是的！\x01",
            "下次绝对不会再饶过你了！\x02\x03",

            "#2310F给我看着吧～……（狂敲键盘）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0108
    ChrTalk(
        0x104,
        "#0305F阿约好像干劲十足啊？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            "#0206F大概吧……\x02\x03",

            "#0201F看起来，好像终于开始\x01",
            "认真起来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        "#0005F是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#0106F嗯～只要不是在干\x01",
            "坏事就好……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_4064")

    Jump("loc_46B8")

    label("loc_4069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4343")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_416B")

    #C0112
    ChrTalk(
        0x8,
        (
            "#2306F就算是在纪念庆典期间，\x01",
            "那些老顾客还是和平时一样，\x01",
            "会来关照我的生意。\x02\x03",

            "我也是很有职业操守的，\x01",
            "所以忙得不可开交啊。\x02\x03",

            "#2302F哈，如果得到了什么有趣的情报，\x01",
            "我会告诉你们的。\x02\x03",

            "#2309F不过只能告诉你们那种\x01",
            "卖不出价钱的小情报而已哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_433E")

    label("loc_416B")


    #C0113
    ChrTalk(
        0x8,
        (
            "#2305F什么，是你们啊。\x01",
            "……有事吗？\x02\x03",

            "#2302F啊，莫非是因为纪念庆典到了，\x01",
            "所以你们在四处游玩吗？\x02\x03",

            "#2309F哈，所以说你们这些凡人\x01",
            "还真是让人头痛啊～！\x02\x03",

            "那种活动和我的行程根本就没有关系啦！\x01",
            "我完全都没有外出的打算呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#0006F不管什么时候来，他都是这样呢。\x02\x03",

            "#0001F而且还是和平时一样，\x01",
            "一直在四处窃取情报……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#0204F真是的，昨天明明刚被我打了个落花流水，\x01",
            "今天却还是这么有精神。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0x8,
        (
            "#2310F缇欧·普拉托！\x01",
            "总有一天，我绝对会打败你的！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_433E")

    Jump("loc_46B8")

    label("loc_4343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BF")

    #C0117
    ChrTalk(
        0x8,
        (
            "#2305F说起来……\x02\x03",

            "#2300F你们干得很好嘛，\x01",
            "顺利解决了那些破铜烂铁啊。\x02\x03",

            "#2302F虽然还达不到银大哥的水平，\x01",
            "但也相当不错了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0005F破铜烂铁…\x01",
            "是指那些机械装置……？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x103,
        (
            "#0211F约纳，难道说……\x01",
            "那是你制造之后放在那里的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "#2306F不是，\x01",
            "我的专业又不是硬件制造。\x02\x03",

            "#2300F那些好像是某位技术人员\x01",
            "发明的自动清扫装置的试制品。\x02\x03",

            "#2302F原本就被丢弃在地下，\x01",
            "我尝试对它们进行了一番解析，\x01",
            "不过最后失控了呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0121
    ChrTalk(
        0x101,
        "#0006F（果然还是与他脱不了干系吗……）\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x103,
        (
            "#0211F（……算了，他在财团的研究所里\x01",
            "  也经常搞出这种恶作剧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x94, 1)
    Jump("loc_46B8")

    label("loc_45BF")


    #C0123
    ChrTalk(
        0x8,
        (
            "#2302F算了，虽然你们还算有一套，\x01",
            "但应该还是敌不过银大哥的～\x02\x03",

            "目的地是星见之塔吗？\x01",
            "如果决定要去的话，\x01",
            "最好提前做好心理准备哦～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B5")

    #C0124
    ChrTalk(
        0x101,
        "#0006F（……真是个嚣张的家伙啊……）\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        (
            "#0300F（算了，不管怎么说，\x01",
            "  我们确实应该做好充分准备。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46B5")

    SetScenarioFlags(0x0, 0)

    label("loc_46B8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_1C3D end

    def Function_10_46C0(): pass

    label("Function_10_46C0")


    #C0126
    ChrTalk(
        0x8,
        (
            "#2305F怎么？\x01",
            "你们的事情已经搞定了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还有其它事情需要处理】\x01",      # 0
            "【所有事情都已经解决了】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4757"),
        (1, "loc_47A4"),
        (SWITCH_DEFAULT, "loc_493D"),
    )


    label("loc_4757")


    #C0127
    ChrTalk(
        0x8,
        (
            "#2302F呼，那就赶快\x01",
            "去处理啊。\x02\x03",

            "在那之前，我就先来\x01",
            "做一些设置工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_493D")

    label("loc_47A4")


    #C0128
    ChrTalk(
        0x8,
        (
            "#2309F好～那么就立刻开始\x01",
            "商量具体分工吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#0100F那，我就和兰迪\x01",
            "去警察局总部了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0130
    ChrTalk(
        0x104,
        (
            "#0300F罗伊德，\x01",
            "阿缇就拜托你啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0131
    ChrTalk(
        0x101,
        (
            "#0004F嗯，交给我吧。\x02\x03",

            "#0000F……兰迪，\x01",
            "工作可别偷懒哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x104,
        (
            "#0309F（戳中软肋）……\x01",
            "哈哈，我什么时候偷过懒。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0133
    ChrTalk(
        0x102,
        "#0104F算了，反正有我在旁边监督呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0134
    ChrTalk(
        0x102,
        "#0102F缇欧，加油哦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0135
    ChrTalk(
        0x103,
        "#0202F……是，艾莉前辈也请加油。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x28, 0x3E8)
    Sleep(800)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    Call(0, 29)

    label("loc_493D")

    Return()

    # Function_10_46C0 end

    def Function_11_493E(): pass

    label("Function_11_493E")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A56")
    SetChrName("")

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "桌子上杂乱无章地\x01",
            "放置着外卖比萨。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0137
    ChrTalk(
        0x101,
        (
            "#0006F这是什么饮食生活啊，\x01",
            "真是的……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0138
    ChrTalk(
        0x101,
        (
            "#0005F啊，不过，这种食物的话，\x01",
            "只要有食材，应该就可以自己做呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '热酪比萨'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xC)
    Jump("loc_4A86")

    label("loc_4A56")

    SetChrName("")

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "桌子上杂乱无章地\x01",
            "放置着外卖比萨。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4A86")

    TalkEnd(0xFF)
    Return()

    # Function_11_493E end

    def Function_12_4A8A(): pass

    label("Function_12_4A8A")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0141
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B5F")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x12, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x12, 0x0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x12)
    OP_71(0x12, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x12, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_4B5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B7B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_4B7B")

    Return()

    # Function_12_4A8A end

    def Function_13_4B7D(): pass

    label("Function_13_4B7D")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_4B7D end

    def Function_14_4B99(): pass

    label("Function_14_4B99")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_4B99 end

    def Function_15_4BB5(): pass

    label("Function_15_4BB5")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_4BB5 end

    def Function_16_4BD1(): pass

    label("Function_16_4BD1")


    #A0142
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是调整水位用的控制装置。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50B6")
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CAD")
    SetChrPos(0x0, 107620, -6000, 200, 0)
    SetChrPos(0x1, 108620, -6000, -600, 0)
    SetChrPos(0x2, 106620, -6000, -600, 0)
    SetChrPos(0x3, 107620, -6000, -1900, 0)
    OP_68(107660, -5000, 850, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28500, 0)
    Jump("loc_4DB4")

    label("loc_4CAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D33")
    SetChrPos(0x0, 85000, -6000, 101000, 0)
    SetChrPos(0x1, 83800, -6000, 101000, 0)
    SetChrPos(0x2, 83800, -6000, 99800, 0)
    SetChrPos(0x3, 85000, -6000, 99800, 0)
    OP_68(84580, -5000, 101000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27000, 0)
    Jump("loc_4DB4")

    label("loc_4D33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DB4")
    SetChrPos(0x0, 201500, -6000, 184020, 90)
    SetChrPos(0x1, 200000, -6000, 184620, 90)
    SetChrPos(0x2, 200000, -6000, 184220, 90)
    SetChrPos(0x3, 198500, -6000, 184020, 90)
    OP_68(201500, -5000, 184020, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33500, 0)

    label("loc_4DB4")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 6)), scpexpr(EXPR_END)), "loc_4F3F")
    SetMapObjFrame(0xE, "m01gim01", 0x2, "off")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "off")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E58")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_4ED7")

    label("loc_4E58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E9A")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_4ED7")

    label("loc_4E9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ED7")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_4ED7")

    OP_0D()
    Sound(157, 2, 100, 0)
    SetMapObjFrame(0xFF, "null", 0x2, "down")
    Sleep(4000)
    OP_24(0x9D)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetBarrier(0x3, 0x8, 0x1)
    SetBarrier(0x2, 0x9, 0x1)
    SetBarrier(0x2, 0xA, 0x1)
    ClearScenarioFlags(0x54, 6)
    Jump("loc_50B6")

    label("loc_4F3F")

    SetMapObjFrame(0xE, "m01gim01", 0x2, "on")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FD6")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_5055")

    label("loc_4FD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5018")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_5055")

    label("loc_5018")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5055")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_5055")

    OP_0D()
    Sound(157, 2, 100, 0)
    SetMapObjFrame(0xFF, "null", 0x2, "up")
    Sleep(4000)
    OP_24(0x9D)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetBarrier(0x2, 0x8, 0x1)
    SetBarrier(0x3, 0x9, 0x1)
    SetBarrier(0x3, 0xA, 0x1)
    SetScenarioFlags(0x54, 6)

    label("loc_50B6")

    Return()

    # Function_16_4BD1 end

    def Function_17_50B7(): pass

    label("Function_17_50B7")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0143
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有可以操作升降机的控制面板。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5231")
    Fade(500)
    SetChrPos(0x0, 600, 0, 600, 90)
    SetChrPos(0x1, 600, 0, -600, 90)
    SetChrPos(0x2, -600, 0, -600, 90)
    SetChrPos(0x3, -600, 0, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5191")
    SetChrPos(0x4, -1800, 0, -600, 90)
    SetChrPos(0x5, -1800, 0, 600, 90)
    Jump("loc_51B0")

    label("loc_5191")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51B0")
    SetChrPos(0x4, -1800, 0, 0, 90)

    label("loc_51B0")

    OP_68(600, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(600, 6000, 0, 3000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0100", 0, 0, 0)
    IdleLoop()

    label("loc_5231")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_50B7 end

    def Function_18_5239(): pass

    label("Function_18_5239")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, 600, 90)
    OP_90(0x1, 600, 30000, -600, 90)
    OP_90(0x2, -600, 30000, -600, 90)
    OP_90(0x3, -600, 30000, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_530C")
    OP_90(0x4, -1800, 0, -600, 90)
    OP_90(0x5, -1800, 0, 600, 90)
    Jump("loc_532B")

    label("loc_530C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_532B")
    OP_90(0x4, -1800, 0, 0, 90)

    label("loc_532B")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, 0, 3000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x11)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_18_5239 end

    def Function_19_5380(): pass

    label("Function_19_5380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5404")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【窥视里面】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_53E0"),
        (1, "loc_53FD"),
        (SWITCH_DEFAULT, "loc_5402"),
    )


    label("loc_53E0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x13, 0x10)
    OP_65(0x4, 0x1)
    Call(0, 23)
    Jump("loc_5402")

    label("loc_53FD")

    Jump("loc_5402")

    label("loc_5402")

    EventEnd(0x3)

    label("loc_5404")

    Return()

    # Function_19_5380 end

    def Function_20_5405(): pass

    label("Function_20_5405")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    OP_68(498200, 1000, 302000, 0)
    MoveCamera(0, 25, 0, 0)
    MoveCamera(0, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 498200, 200, 302000, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02300.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis122.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis154.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis123.itp")
    OP_C9(0x0, 0x4, 0x0, 0x0, 0x0)
    Sound(850, 0, 90, 0)
    Sleep(1500)
    PlayBGM("ed7521", 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("少年的声音")

    #A0144
    AnonymousTalk(
        0xFF,
        "帝国方面的主要投资事业一览……\x02",
    )

    CloseMessageWindow()

    #A0145
    AnonymousTalk(
        0xFF,
        "卡尔瓦德方面的各种行情一览……\x02",
    )

    CloseMessageWindow()

    #A0146
    AnonymousTalk(
        0xFF,
        (
            "雷米菲利亚方面的\x01",
            "三大制药公司的销售成绩……\x02",
        )
    )

    CloseMessageWindow()

    #A0147
    AnonymousTalk(
        0xFF,
        (
            "还有利贝尔方面……\x01",
            "是新型导力引擎的进货点一览吗？\x02",
        )
    )

    CloseMessageWindow()

    #A0148
    AnonymousTalk(
        0xFF,
        (
            "真不愧是克洛斯贝尔，\x01",
            "各种情报都能收集到呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("长雀斑的少年")

    #A0149
    AnonymousTalk(
        0xFF,
        (
            "嘿嘿……收获不少，收获不少¤\x02\x03",

            "哎呀，这次的工作\x01",
            "也很轻松啊。\x02\x03",

            "只要在数据库里稍微找一找，\x01",
            "就能得到客户需要的珍贵情报啦！\x02\x03",

            "大家的安全意识都还很薄弱，\x01",
            "我根本就是随心所欲嘛。\x02\x03",

            "人生真是太轻松了⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    SetCameraDistance(18000, 3000)
    OP_68(498200, 900, 302000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    Sound(857, 0, 100, 0)
    Sleep(2000)
    OP_63(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)
    Sleep(300)

    #N0150
    NpcTalk(
        0x8,
        "长雀斑的少年",
        (
            "#5P#2310F真难吃……比萨凉了之后，\x01",
            "简直就是难以下咽啊。\x02\x03",

            "#2302F比萨也好，情报也好，\x01",
            "果然都是要趁热享用才美味呀。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)

    #N0151
    NpcTalk(
        0x8,
        "长雀斑的少年",
        (
            "#5P#2304F那么～……\x01",
            "接下来就要干点私事啦。\x02\x03",

            "是要攻克ＩＢＣ的终端呢……\x01",
            "还是查明『小猫』的真正身份呢。\x02\x03",

            "#2302F哈……\x01",
            "有趣的活动还真多呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(824, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0152
    NpcTalk(
        0x8,
        "长雀斑的少年",
        "#6P#2305F导力邮件……？\x02",
    )

    CloseMessageWindow()
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    FadeToDark(0, 0, -1)
    Sleep(500)
    SetChrName("长雀斑的少年")

    #A0153
    AnonymousTalk(
        0xFF,
        (
            "#2301F『约纳·塞克里德先生敬启……』\x02\x03",

            "『久闻阁下技艺了得，\x01",
            "  特此致信商谈……』\x02\x03",

            "#2305F嘿，发信地址是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(849, 0, 100, 0)
    Sleep(800)
    SetChrName("长雀斑的少年")

    #A0154
    AnonymousTalk(
        0xFF,
        (
            "#2301F……好像并不是通过\x01",
            "某个大型终端发出的。\x02\x03",

            "是通过港湾区的路由器转发的……\x02\x03",

            "#2305F#30W…………………………………………\x02\x03",

            "#40W……『黑月贸易公司』………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 21)
    SetChrName("长雀斑的少年")

    #A0155
    AnonymousTalk(
        0xFF,
        "#2309F#4SＹＥＡＨ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(0, 0)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(500)

    #N0156
    NpcTalk(
        0x8,
        "长雀斑的少年",
        (
            "#6P#2304F……是『银』吗……\x02\x03",

            "#2302F哈哈！\x01",
            "这可真有意思。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x101, 3)
    StopBGM(0xFA0)
    WaitBGM()
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_57(0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_E3(0xB)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_5405 end

    def Function_21_5BC3(): pass

    label("Function_21_5BC3")

    OP_C9(0x3, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0x640, 0xFFFFFB50, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1)
    OP_CA(0x0, 0xFF, 0x0)
    Return()

    # Function_21_5BC3 end

    def Function_22_5C1F(): pass

    label("Function_22_5C1F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(490300, 1000, 199800, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 491000, 0, 200300, 90)
    SetChrPos(0x102, 491000, 0, 199300, 90)
    SetChrPos(0x103, 489600, 0, 199300, 90)
    SetChrPos(0x104, 489600, 0, 200300, 90)
    FadeToBright(1000, 0)
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
    Sleep(1000)

    #C0157
    ChrTalk(
        0x101,
        "#0005F（这音乐是……）\x02",
    )

    CloseMessageWindow()
    OP_68(499600, 1000, 204800, 2000)
    OP_6F(0x1)

    def lambda_5D49():
        OP_96(0xFE, 0x7A2B0, 0x0, 0x316A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D49)
    Sleep(50)

    def lambda_5D66():
        OP_96(0xFE, 0x7A2B0, 0x0, 0x312B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D66)
    Sleep(50)

    def lambda_5D83():
        OP_96(0xFE, 0x79D38, 0x0, 0x316A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5D83)
    Sleep(50)

    def lambda_5DA0():
        OP_96(0xFE, 0x79D38, 0x0, 0x312B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5DA0)
    WaitChrThread(0x101, 1)

    def lambda_5DBE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DBE)
    WaitChrThread(0x102, 1)

    def lambda_5DCF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5DCF)
    WaitChrThread(0x103, 1)

    def lambda_5DE0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5DE0)
    WaitChrThread(0x104, 1)

    def lambda_5DF1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5DF1)
    WaitChrThread(0x104, 2)

    #C0158
    ChrTalk(
        0x104,
        "#12P#0301F（好像是有人在呢。）\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        (
            "#4P#0203F（『第８控制终端』恐怕\x01",
            "  就在前方呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#4P#0101F（也就是说……\x01",
            "  『银』和黑客就在前方吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    def lambda_5EEF():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5EEF)
    Sleep(50)

    def lambda_5EFF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5EFF)
    Sleep(50)

    def lambda_5F0F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5F0F)
    Sleep(300)

    #C0161
    ChrTalk(
        0x101,
        (
            "#0003F#5P（总之，先看看里面的情况吧……）\x02\x03",

            "#0001F（『银』说不定就在里面，\x01",
            "  各位，请务必小心。）\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        "#4P#0101F（嗯……！）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 499600, 0, 202400, 0)
    ClearMapObjFlags(0x13, 0x10)
    OP_66(0x4, 0x1)
    SetScenarioFlags(0x83, 5)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_22_5C1F end

    def Function_23_5FC1(): pass

    label("Function_23_5FC1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis034.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02300.itp")
    OP_68(498200, 900, 302000, 0)
    MoveCamera(25, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 499800, 150, 207400, 0)
    SetChrPos(0x102, 500500, 150, 206700, 0)
    SetChrPos(0x103, 499400, 0, 206200, 0)
    SetChrPos(0x104, 500200, 0, 205600, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 498200, 200, 302000, 0)
    ClearMapObjFlags(0x13, 0x10)
    OP_70(0x13, 0x1)
    SetMapFlags(0x2000)
    SetMapFlags(0x8000000)
    OP_E0(0x0)
    VolumeBGM(0x64, 0x3E8)
    SetCameraDistance(21500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("长雀斑的少年")

    #A0163
    AnonymousTalk(
        0xFF,
        (
            "那么～\x01",
            "今天也大捞一笔吧～\x02\x03",

            "首先是莱恩福尔特公司的\x01",
            "新型铁路用车的规格……\x02\x03",

            "然后是乌尔努公司的\x01",
            "高级跑车的规格……\x02\x03",

            "嘿，ＺＣＦ正在开发\x01",
            "新型的定期飞行船吗……\x02\x03",

            "再加上不久前开发的导力装甲，\x01",
            "那里的技术也一直在飞速发展啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    VolumeBGM(0x28, 0x3E8)
    Fade(500)
    OP_68(499800, 1000, 207900, 0)
    MoveCamera(36, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0164
    ChrTalk(
        0x101,
        "#11P#0005F（……那是……）\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        (
            "#0105F（看起来好像\x01",
            "  并不是『银』呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x104,
        "#4P#0301F（怎么回事，那个小鬼是干什么的？）\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        "#12P#0206F（……果然……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    VolumeBGM(0x64, 0x3E8)
    Fade(500)
    OP_68(498200, 900, 302000, 0)
    MoveCamera(25, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    OP_0D()
    Sleep(500)

    #N0168
    NpcTalk(
        0x8,
        "长雀斑的少年",
        (
            "#12P#2304F不过，银大哥竟然会付给我\x01",
            "银耀石的结晶，出手真够阔绰的。\x02\x03",

            "这种大小的话，大概能\x01",
            "卖到一万米拉左右吧～\x02\x03",

            "#2302F嘿嘿，明天有空的话\x01",
            "就去『纳因瓦利』换钱吧。\x02\x03",

            "然后还想去基约姆大叔那里\x01",
            "买些新型零件。\x02",
        )
    )

    CloseMessageWindow()
    Sound(850, 0, 100, 0)
    Sleep(1000)

    #N0169
    NpcTalk(
        0x8,
        "长雀斑的少年",
        (
            "#12P#2309F哈，话说回来，\x01",
            "银大哥也真是多此一举呢～\x02\x03",

            "光是发一封那样的邮件，\x01",
            "他们根本就不可能找到这个地方吧。\x02\x03",

            "#2302F能追查到我约纳大人行踪的人，\x01",
            "即使在整个塞姆里亚大陆中也找不出一个～！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 500000, 0, 294300, 0)
    SetChrPos(0x102, 501000, 0, 294300, 0)
    SetChrPos(0x103, 500000, 0, 293300, 0)
    SetChrPos(0x104, 501000, 0, 293300, 0)

    #N0170
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "──那可不一定。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x20)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(499400, 900, 301200, 2500)
    MoveCamera(11, 15, 0, 2500)
    BeginChrThread(0x101, 3, 0, 24)
    Sleep(1000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)

    def lambda_6619():
        OP_96(0xFE, 0x79AE0, 0xC8, 0x49AE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6619)

    def lambda_6633():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6633)
    Sound(820, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)

    #N0171
    NpcTalk(
        0x8,
        "长雀斑的少年",
        "#5P#2305F什么……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)

    #C0172
    ChrTalk(
        0x101,
        (
            "#0001F#6P看起来……\x01",
            "你就是那个『黑客』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        (
            "#4P#0301F喂喂……\x01",
            "真的是他吗，他只是个小鬼而已啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0174
    NpcTalk(
        0x8,
        "长雀斑的少年",
        "#5P#2305F干、干什么，你们……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0175
    NpcTalk(
        0x8,
        "长雀斑的少年",
        (
            "#5P#2307F难、难道你们就是银大哥\x01",
            "所说的『特别任务支援科』吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        "#0003F#6P嗯，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x102,
        (
            "#0101F看起来，你好像\x01",
            "确实认识『银』呢……\x02",
        )
    )

    CloseMessageWindow()

    #N0178
    NpcTalk(
        0x8,
        "长雀斑的少年",
        (
            "#5P#2310F不、不对，怎么可能啊！\x02\x03",

            "竟然能追查到天才约纳大人的行踪，\x01",
            "一直找到这里来……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#12P#0206F……你还是一点都没变啊，\x01",
            "约纳·塞克里德。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0180
    ChrTalk(
        0x8,
        (
            "#5P#2305F缇欧·普拉托！？\x02\x03",

            "你、你为什么会在这里……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        (
            "#12P#0203F那是我的台词。\x02\x03",

            "#0211F从财团逃离的你\x01",
            "为什么会在这种地方……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_692E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_692E)
    Sleep(50)

    def lambda_693E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_693E)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)
    Sleep(300)

    #C0182
    ChrTalk(
        0x101,
        "#5P#0011F缇欧，你认识他吗？\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#12P#0203F我们曾在爱普斯泰恩财团的\x01",
            "同一处研究所中工作过。\x02\x03",

            "#0200F但因为负责的专业不同，\x01",
            "所以也并没有很深的交情。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x8,
        (
            "#5P#2310F可恶，原来是这样啊……\x02\x03",

            "如果是你的话，只要使用那个模式，\x01",
            "确实有可能追查到我的踪迹……\x02\x03",

            "#2311F啊啊，真是的！早知如此，\x01",
            "我就谨慎一点，多做些隐蔽工作了！\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        (
            "#12P#0204F真是功亏一篑呢，约纳。\x02\x03",

            "#0211F正因为有时缺根神经，你才会做出那种\x01",
            "恶作剧，还给财团造成了重大损失。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x8,
        "#5P#2301F吵、吵死人了，真多嘴～\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x104,
        "#0305F怎么，什么大损失啊？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0188
    ChrTalk(
        0x103,
        (
            "#6P#0206F为了将约纳培养成系统工程师，\x01",
            "财团从他幼年时期开始，\x01",
            "就一直对他施行精英式教育……\x02\x03",

            "但他的恶作剧实在是太过分了，\x01",
            "最后使一项研究成果化为乌有，\x01",
            "造成了十分重大的损失。\x02\x03",

            "#0211F然后，因为不想面对惹怒他人的后果，\x01",
            "就从财团中逃跑了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0189
    ChrTalk(
        0x101,
        "#5P#0001F这、这算什么事啊……\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        (
            "#5P#0106F呼……\x01",
            "我还以为是什么理由呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        (
            "#0306F哎呀哎呀……\x01",
            "跟外表一样，就只是个小鬼而已啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        (
            "#5P#2310F可、可恶……\x01",
            "竟然肆无忌惮地乱说……\x02\x03",

            "#2307F缇欧·普拉托！\x01",
            "你可不要向财团告密啊！？\x02\x03",

            "要是你敢那么做，我就把你那些\x01",
            "羞耻的秘密全部都公布到导力网络上！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x8, 500)
    Sleep(300)

    #C0193
    ChrTalk(
        0x103,
        (
            "#12P#0204F请便。\x02\x03",

            "#0202F我并没有什么羞于告人\x01",
            "的秘密……\x02\x03",

            "就算真的有，也不会露出破绽，\x01",
            "被你抓到。\x02\x03",

            "#0204F最后，即使真的被你发到了网络上，\x01",
            "我也可以马上采取对策。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x8,
        "#5P#2310F呜、呜啊～……！\x02",
    )

    CloseMessageWindow()

    def lambda_6E87():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6E87)
    Sleep(50)

    def lambda_6E97():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E97)
    Sleep(50)

    def lambda_6EA7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6EA7)
    Sleep(300)

    #C0195
    ChrTalk(
        0x102,
        "#0102F呵呵……\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x104,
        (
            "#4P#0304F哈哈，还是阿缇厉害啊，\x01",
            "完全占了上风呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#0001F#6P那么……你叫约纳是吧。\x02\x03",

            "你为什么会在这种地方呢？\x01",
            "到底在做些什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "#5P#2301F吵死了，我有什么义务\x01",
            "非要告诉你们──\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x103,
        (
            "#12P#0201F请回答，约纳。\x02\x03",

            "从我们到达这个地方开始，\x01",
            "你就已经在这场游戏中输掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x8,
        (
            "#5P#2310F呜……我明白啦。\x02\x03",

            "#2306F我嘛，目前正在克洛斯贝尔\x01",
            "干『情报商』这个行当呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0201
    ChrTalk(
        0x101,
        "#0005F#6P情报商……？\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x104,
        (
            "#4P#0301F喂喂……\x01",
            "这个职业可不适合你这种小鬼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x8,
        (
            "#5P#2304F哈哈，现在的情报商\x01",
            "可是不分年龄的啦～\x02\x03",

            "#2302F在克洛斯贝尔，可以收集到\x01",
            "各种各样的情报。\x02\x03",

            "帝国、共和国、利贝尔、雷米菲利亚，\x01",
            "从列曼到亚尔特利亚……\x02\x03",

            "再加上各种公司，还有\x01",
            "国际企业的分公司也不在少数。\x02\x03",

            "这些地方的情报都是通过导力网络\x01",
            "而流传的。\x02\x03",

            "#2309F而他们的安全意识普遍都还很低，\x01",
            "所以我可以随意品尝这些美味的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x102,
        "#0105F这、这样的话……\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        "#0013F#6P不管怎么看，都是违法的吧？\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x103,
        (
            "#12P#0206F不，因为导力网络还在试验运营的阶段，\x01",
            "所以目前并没有相关法律出台。\x02\x03",

            "#0200F法制的完善化虽然也只是\x01",
            "时间问题，但如今……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x8,
        (
            "#5P#2304F算啦，克洛斯贝尔在这方面\x01",
            "一向都很有问题呢～\x02\x03",

            "财团的研究所我早就待烦了，\x01",
            "所以就在这里做起了情报生意。\x02\x03",

            "#2302F嘿嘿，来找我的客人真是不少，\x01",
            "所以我也赚到了不少钱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x104,
        (
            "#4P#0306F哎呀哎呀……\x01",
            "不要小看了这个社会啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x103,
        (
            "#12P#0204F不过，你好像并不知道\x01",
            "我被外派至克洛斯贝尔\x01",
            "的警察局了呢……\x02\x03",

            "#0202F身为情报商，你的能力是不是稍显不足啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x8,
        (
            "#5P#2306F呜……那也是没办法的吧！\x02\x03",

            "#2310F即使是我，也不可能对克洛斯贝尔\x01",
            "的所有事情都了如指掌吧～！\x02\x03",

            "我还要和『小猫』战斗，\x01",
            "现在忙得很呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x103,
        "#12P#0205F『小猫』……？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "#5P#2305F是、是我的私事啦，和你无关～\x02\x03",

            "#2301F……嗯，难道说……\x01",
            "『小猫』该不会是你吧？\x02\x03",

            "你是什么时候来克洛斯贝尔的？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        (
            "#12P#0206F根本不明白你的问题是什么意思……\x02\x03",

            "#0200F不过，我来克洛斯贝尔的时间，\x01",
            "大概是两个月之前吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        (
            "#5P#2306F这样啊，果然不是你……\x01",
            "黑客手段的特征也明显不同。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x103,
        "#12P#0205F？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#0003F#6P虽然不太明白你在说什么……\x02\x03",

            "#0013F不过，差不多也该回答我的问题了吧。\x01",
            "你和『银』到底是什么关系？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x8,
        "#5P#2300F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#0001F#6P发送那封邮件的人\x01",
            "就是你，没错吧？\x02\x03",

            "你为什么要发那种东西？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        "#5P#2304F……哼，算啦。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrPos(0x8, 498600, 200, 301100, 150)
    ClearChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()

    def lambda_775E():
        OP_96(0xFE, 0x79EC8, 0x0, 0x493E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_775E)
    WaitChrThread(0x8, 1)
    Sleep(300)

    #C0220
    ChrTalk(
        0x8,
        "#2300F#5P把这个拿去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '梅琳的伞'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('梅琳的伞', 1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(300)
    SetMessageWindowPos(-1, 130, -1, -1)
    SetChrName("")

    #A0222
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "如今，门扉已然开启。\x01",
            "立即前往星之塔，\x01",
            "完成吾之所愿。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
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
    Sleep(1000)

    #C0223
    ChrTalk(
        0x101,
        "#0005F#6P这是……！\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x102,
        "#0101F『银』写的传言吗……！？\x02",
    )

    CloseMessageWindow()

    def lambda_7931():
        OP_96(0xFE, 0x79BA8, 0xC8, 0x4982C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7931)
    WaitChrThread(0x8, 1)
    Fade(250)
    SetChrPos(0x8, 498400, 200, 301800, 90)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x2)
    Sound(820, 0, 100, 0)
    OP_0D()

    #C0225
    ChrTalk(
        0x8,
        (
            "#5P#2300F是银大哥给我的委托哦。\x02\x03",

            "他让我向你们发送邮件，\x01",
            "还说，如果你们能找到这里，\x01",
            "就把这张卡片交给你们。\x02\x03",

            "#2306F……不过，完全没想到\x01",
            "你们真的能找到这里来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x104,
        (
            "#4P#0304F哼，原来如此啊。\x02\x03",

            "#0305F那么，你和那个『银』\x01",
            "是不是已经见过好几次面了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "#5P#2300F嗯，他是我的常客之一。\x02\x03",

            "偶尔会亲自到我这里来，\x01",
            "购买各种各样的情报。\x02\x03",

            "#2306F哈，不过，像这种奇怪的委托，\x01",
            "我倒是第一次接受呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        "#0001F#6P『银』来过这里……\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x103,
        "#12P#0201F他是什么样的人物呢？\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        (
            "#5P#2300F哦，他一直都裹着一身黑衣，\x01",
            "而且还戴着面具，所以我也不知道～\x02\x03",

            "#2302F不过，他好像就是卡尔瓦德东方人街\x01",
            "那个传说中的杀手吧？\x02\x03",

            "#2309F真帅啊，实在太酷了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0231
    ChrTalk(
        0x101,
        "#0011F#6P酷吗……\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x104,
        (
            "#4P#0306F哎呀哎呀……\x01",
            "真是个不知道什么叫害怕的小鬼。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x102,
        (
            "#0108F不过，『银』在邀请我们过去，\x01",
            "这是可以确定的了。\x02\x03",

            "#0101F从留言上来看，好像是\x01",
            "有什么事情想和我们说……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        (
            "#5P#2300F嗯，好像就是这样。\x02\x03",

            "虽然不知道具体有什么事，\x01",
            "不过好像说是想试试你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#0013F#6P唔……\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x104,
        (
            "#4P#0302F嘿，还真是个\x01",
            "胆大妄为的犯罪者啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x103,
        (
            "#6P#0201F不过，这上面所说的『星之塔』\x01",
            "是指什么呢……？\x02\x03",

            "看起来，好像是某种暗喻……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        (
            "#0008F#5P『星之塔』……\x01",
            "好像曾在什么地方听说过呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C0239
    ChrTalk(
        0x102,
        (
            "#0105F莫非是……\x02\x03",

            "#0101F位于克洛斯贝尔郊外的\x01",
            "『星见之塔』吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7E82():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E82)
    Sleep(50)

    def lambda_7E92():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7E92)
    Sleep(50)

    def lambda_7EA2():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7EA2)
    Sleep(200)

    #C0240
    ChrTalk(
        0x101,
        (
            "#5P#0005F啊……\x02\x03",

            "#0001F是位于乌尔斯拉间道中段的\x01",
            "那座中世纪时期的塔吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x104,
        (
            "#4P#0306F喂喂，他竟然要把我们\x01",
            "叫到那种地方吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x102,
        (
            "#0103F可是，我们也没有其它线索啊。\x02\x03",

            "#0101F以目前的情况来看，\x01",
            "也只能过去看看了吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        (
            "#5P#0004F──嗯，我也赞成。\x02\x03",

            "#0000F准备好了的话，\x01",
            "马上就前往南出口……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7FD9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7FD9)
    Sleep(50)

    def lambda_7FE9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7FE9)

    def lambda_7FF6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7FF6)
    Sleep(50)

    def lambda_8006():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8006)
    Sleep(300)

    #C0244
    ChrTalk(
        0x104,
        (
            "#4P#0301F……问题是，要怎么\x01",
            "处理这个小鬼呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0245
    ChrTalk(
        0x8,
        (
            "#5P#2305F什、什么嘛……\x01",
            "已经不关我的事了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#0001F#6P我说啊……这个地下空间\x01",
            "可是克洛斯贝尔的公共设施哦。\x02\x03",

            "不管怎么看，你这都算是非法侵占吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x8,
        (
            "#5P#2310F哼、哼……我只是把无人使用的地方\x01",
            "善加利用而已，这有什么不好的。\x02\x03",

            "#2307F而且，法律中也没有\x01",
            "『不许擅自使用地下空间』\x01",
            "这一条吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x101,
        "#0003F#6P你这根本就是强词夺理。\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        (
            "#0106F而且，你生活在这种地方，\x01",
            "也是很危险的吧？\x02\x03",

            "#0101F不但附近有魔兽徘徊，\x01",
            "吃饭问题也很难解决……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(498400, 900, 300530, 1200)

    def lambda_8239():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8239)
    Sleep(200)

    def lambda_8249():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8249)
    Sleep(50)

    def lambda_8259():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8259)
    Sleep(50)

    def lambda_8269():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8269)
    OP_6F(0x1)

    #C0250
    ChrTalk(
        0x103,
        (
            "#11P#0211F……是啊，\x01",
            "屋子里全都是一些外卖比萨的餐盒。\x02\x03",

            "#0205F不过，比萨竟然\x01",
            "还能送到这种地方来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "#5P#2304F那怎么可能嘛～\x02\x03",

            "#2302F每次都是让他们送到出口附近，\x01",
            "然后我自己去取的。\x02\x03",

            "从这里再往前走，\x01",
            "有个可以通到出口\x01",
            "附近的排气管道哦。\x02\x03",

            "#2309F从那里穿过去的话，\x01",
            "就可以安全地直接离开啦¤\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x104,
        (
            "#2P#0306F这家伙可真是没救了……\x01",
            "已经完全打算在此定居了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(499400, 900, 301200, 1000)

    def lambda_83EE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_83EE)
    Sleep(50)

    def lambda_83FE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_83FE)
    Sleep(50)

    def lambda_840E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_840E)
    Sleep(50)
    OP_93(0x104, 0x10E, 0x190)
    OP_6F(0x1)

    #C0253
    ChrTalk(
        0x101,
        (
            "#0006F#6P唉，我们现在也挺忙的，\x01",
            "就先不要管他了……\x02\x03",

            "#0001F不过，你可一定不要做坏事，\x01",
            "凡事都要适可而止哦。\x02\x03",

            "如果太过乱来，也许会招人怨恨，\x01",
            "到时候，你的处境可就危险了。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        "#0106F是啊……这方面也很让人担心。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        (
            "#5P#2304F哈，我怎么会犯那种低级错误。\x02\x03",

            "#2302F好啦，如果你们以后想要什么情报，\x01",
            "也可以过来找我。\x02\x03",

            "不过，价钱可不便宜哦。\x02\x03",

            "#2309F我想，像你们这种薪水微薄\x01",
            "的新警察大概是支付不起的吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        "#0013F#6P这小子……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(150)

    #C0257
    ChrTalk(
        0x103,
        (
            "#6P#0202F算了算了，罗伊德前辈。\x02\x03",

            "#0204F如果真有什么需要，\x01",
            "我就用黑客手段侵入这里，\x01",
            "把想要的情报直接拿走就是了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0258
    ChrTalk(
        0x8,
        "#5P#4S#2310F喂！？\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x8, 498200, 200, 302000, 0)
    SetChrSubChip(0x8, 0x0)
    OP_68(500600, 1000, 296300, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33000, 0)
    SetChrPos(0x0, 500600, 0, 296300, 180)
    SetChrPos(0x1, 500600, 0, 296300, 180)
    SetChrPos(0x2, 500600, 0, 296300, 180)
    SetChrPos(0x3, 500600, 0, 296300, 180)
    OP_70(0x13, 0x0)
    SetMapObjFlags(0x13, 0x10)
    SetScenarioFlags(0x83, 6)
    OP_29(0x43, 0x1, 0x7)
    Sleep(500)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_23_5FC1 end

    def Function_24_8733(): pass

    label("Function_24_8733")


    def lambda_8738():
        OP_96(0xFE, 0x7A058, 0x0, 0x48FF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8738)
    Sleep(400)

    def lambda_8755():
        OP_96(0xFE, 0x7A440, 0x0, 0x49188, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8755)
    Sleep(400)

    def lambda_8772():
        OP_96(0xFE, 0x7A058, 0x0, 0x48AE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8772)
    Sleep(400)

    def lambda_878F():
        OP_96(0xFE, 0x7A5D0, 0x0, 0x48DA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_878F)
    WaitChrThread(0x101, 1)

    def lambda_87AD():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_87AD)
    WaitChrThread(0x102, 1)

    def lambda_87BE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_87BE)
    WaitChrThread(0x103, 1)

    def lambda_87CF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_87CF)
    WaitChrThread(0x104, 1)

    def lambda_87E0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_87E0)
    WaitChrThread(0x104, 2)
    Return()

    # Function_24_8733 end

    def Function_25_87ED(): pass

    label("Function_25_87ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50090.itc", 0x22)
    OP_68(498200, 900, 302000, 0)
    MoveCamera(25, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 498200, 200, 302000, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02300.itp")
    SetCameraDistance(21500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    SetChrFlags(0x8, 0x20)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_88CC():
        OP_96(0xFE, 0x79AE0, 0xC8, 0x49AE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_88CC)

    def lambda_88E6():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_88E6)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)

    #C0259
    ChrTalk(
        0x8,
        "#2302F哦，你们来得正好。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x103, 500000, 0, 294300, 0)
    SetChrPos(0x102, 501000, 0, 294300, 0)
    SetChrPos(0x101, 500000, 0, 293300, 0)
    SetChrPos(0x104, 501000, 0, 293300, 0)
    OP_68(499400, 900, 301200, 2500)
    MoveCamera(11, 15, 0, 2500)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(2000)
    Fade(250)
    SetChrPos(0x8, 498600, 200, 301100, 150)
    ClearChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    OP_92(0x8, 0x79EC8, 0x493E0, 0x0)
    OP_0D()

    def lambda_89C2():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_89C2)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 3)

    #C0260
    ChrTalk(
        0x101,
        "#12P#0001F现在不该说『来得正好』吧。\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        (
            "#0200F你不是说有事想要我们帮忙吗，\x01",
            "到底是什么事情？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0262
    AnonymousTalk(
        0x8,
        (
            "那个～其实呢……\x02\x03",

            "是关于黑客技术方面的事啦，\x01",
            "希望你能帮帮我。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_93(0x103, 0xA0, 0x1F4)

    #C0263
    ChrTalk(
        0x103,
        "#5P#0203F……我回去了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0264
    ChrTalk(
        0x8,
        (
            "#2307F#5P等、等一下啦！\x02\x03",

            "为什么突然\x01",
            "就要回去啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        "#12P#0006F那个，这不是理所当然的嘛……\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        "#4P#0301F真是的，好一个爱乱来的小鬼。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x102,
        (
            "#0106F竟然让警察协助犯罪行为，\x01",
            "未免也太过异想天开了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x8,
        (
            "#2301F#5P所以说，我现在想做的\x01",
            "并不是什么犯罪行为啦！\x02\x03",

            "而且要侵入的并不是\x01",
            "某些企业或者ＩＢＣ之类的地方！\x02\x03",

            "只是想把某个难缠对手的\x01",
            "狐狸尾巴抓住而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x103, 0x8, 500)

    #C0269
    ChrTalk(
        0x103,
        "#0200F……难缠对手？\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x8,
        (
            "#2302F#5P哦，有兴趣了吗？\x02\x03",

            "#2303F那个，总之，\x01",
            "至少先听我把话说完，可以吧～？\x02\x03",

            "#2300F而且我觉得你们也绝对\x01",
            "会有兴趣的。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x103,
        (
            "#0203F……明白了。\x02\x03",

            "#0211F不过，如果只是一些无聊的事情，\x01",
            "我就会让你稍微吃点苦头的。\x02\x03",

            "比如说，让你在『波波碰』里\x01",
            "尝尝二十连锁攻击的滋味。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0272
    ChrTalk(
        0x8,
        (
            "#2306F#5P那也未免太过屈辱了，\x01",
            "拜托你还是饶了我吧……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_68(496800, 1400, 296600, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 495000, 200, 296300, 90)
    SetChrPos(0x102, 495000, 200, 295400, 90)
    SetChrPos(0x103, 497700, 200, 295400, 270)
    SetChrPos(0x104, 495000, 200, 297200, 90)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 497700, 200, 296600, 270)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x18)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 495850, 250, 296400, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x18)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 495850, 250, 295900, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x18)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 495850, 250, 296900, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x18)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 496850, 250, 296400, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x18)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 496850, 250, 295900, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetMapObjFrame(0xFF, "pizza", 0x0, 0x1)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0273
    AnonymousTalk(
        0x103,
        "#0205F『小猫』……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    OP_68(496800, 900, 296600, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0274
    ChrTalk(
        0x101,
        (
            "#6P#0001F名字倒是很可爱……\x01",
            "真有这样的黑客吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x8,
        (
            "#11P#2303F哈，我没有说谎的必要吧？\x02\x03",

            "#2301F初次遇见那家伙，\x01",
            "大约是在半年之前……\x02\x03",

            "就在我入侵几个公司的网络时，\x01",
            "突然遭到了某人的跟踪。\x02\x03",

            "#2306F当时，我慌慌张张地切断了入侵路径，\x01",
            "总算是逃脱了……\x02\x03",

            "然后，对方似乎是为了羞辱我，\x01",
            "还把自己的绰号『小猫』\x01",
            "发送到了我这里！\x02\x03",

            "#2310F自那之后，时不时地\x01",
            "就来找我麻烦，影响我的买卖！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        "#6P#0006F嗯、嗯～……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x102,
        (
            "#6P#0101F据我所知，黑客在目前\x01",
            "还是相当少见的……\x02\x03",

            "除了你之外，在克洛斯贝尔\x01",
            "真的还有这样的人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x8,
        (
            "#11P#2303F有啊，绝对没错！\x02\x03",

            "#2307F那个，最开始的时候，\x01",
            "我也以为是搞错了。\x02\x03",

            "在这个城市里，怎么可能会有\x01",
            "能与我匹敌的天才黑客嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        (
            "#11P#0211F……说匹敌好像不太恰当，\x01",
            "不管怎么看，都觉得那个『小猫』\x01",
            "的技术在你之上呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x8, 0x0, 0xF, 0x1F4, 0xBB8)
    Sleep(150)

    #C0280
    ChrTalk(
        0x8,
        "#11P#2310F呜啊……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        (
            "#11P#0204F算了，毕竟你本来的专业\x01",
            "是系统语言的开发……\x02\x03",

            "#0202F就算在黑客技术方面输给对方，\x01",
            "也不用太过失落。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    #C0282
    ChrTalk(
        0x8,
        (
            "#5P#2307F我可不需要这种多余的安慰！\x02\x03",

            "#2310F总、总而言之，\x01",
            "我必须要报这一箭之仇！\x02\x03",

            "无论如何，也要查出对方的地址，\x01",
            "掌握到那家伙的具体访问点！\x02\x03",

            "所以请你帮帮我吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x103,
        "#11P#0203F唔……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0284
    ChrTalk(
        0x103,
        (
            "#11P#0201F……你能保证『小猫』\x01",
            "今天会在网络上现身吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#5P#2304F哈，我毕竟也做过\x01",
            "很充分的分析和策划啦。\x02\x03",

            "#2302F看起来，『小猫』好像\x01",
            "并不是一直都泡在网络上的，\x01",
            "不过……\x02\x03",

            "我已经把很多对方可能会感兴趣的消息\x01",
            "散布在了网络上。\x02\x03",

            "从对方目前为止的行动倾向来推测，\x01",
            "『小猫』出现的可能性高达９０％。\x02\x03",

            "#2309F所以绝对不能放过这次机会，对吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x103,
        (
            "#11P#0208F原来如此……\x02\x03",

            "#0204F──也就是说，\x01",
            "我们之中，要有一方负责充当诱饵，\x01",
            "吸引『小猫』的注意力……\x02\x03",

            "在这期间，另一方\x01",
            "则通过其它访问点\x01",
            "来查明『小猫』的入侵路径……\x02\x03",

            "#0202F然后多次重复这个过程，\x01",
            "最终把『小猫』逼进死胡同……\x02\x03",

            "计划大致就是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x8,
        (
            "#5P#2300F嘿，你果然有一套啊。\x02\x03",

            "#2304F如果是你的话，只要使用那个模式，\x01",
            "应该可以跟得上『小猫』的处理速度。\x02\x03",

            "而我也做足了各方面的准备工作，\x01",
            "在速度上绝对不会输给对方。\x02\x03",

            "#2302F二对一的话，绝对可以抓住小猫的尾巴！\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x103,
        "#11P#0203F──但我有两个问题。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x8,
        "#5P#2305F哎……？\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x103,
        (
            "#11P#0201F首先，为了对你的黑客行动进行支援，\x01",
            "我需要合适的终端装置。\x02\x03",

            "但考虑到黑客行动的风险性，\x01",
            "我不太愿意使用\x01",
            "支援科的终端。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x8,
        (
            "#5P#2302F这样的话，倒是正好有个合适的地方。\x02\x03",

            "在地下空间Ａ区域的下层，\x01",
            "有一个『第３控制终端』。\x02\x03",

            "那里用的服务器和这里的不同，\x01",
            "应该可以顺利实现两面夹击。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x103,
        (
            "#11P#0205F原来如此……\x01",
            "看来条件很合适呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        "#6P#0012F（嗯、嗯～）\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        "#0301F（完全听不懂他们在说什么啊。）\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x102,
        "#6P#0100F（毕竟太专业了呢。）\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        (
            "#11P#0206F不过，还有另一个问题──\x02\x03",

            "#0201F在如此忙碌的时期，我们怎么可以\x01",
            "为了这种事情而浪费大量时间呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0297
    ChrTalk(
        0x101,
        "#6P#0005F那个……\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        "#6P#0106F……这确实也是个问题呢。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x104,
        (
            "#0306F昨天参加赛跑就已经\x01",
            "耗掉了一个下午的时间啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0300
    ChrTalk(
        0x8,
        (
            "#11P#2307F喂喂，别这么说啊！？\x02\x03",

            "你们的工作都是支援请求吧？\x01",
            "其中总有一些可做可不做，\x01",
            "大可延后完成的事情吧？\x02\x03",

            "我会给你们提供一些贵重情报当作回礼的，\x01",
            "所以帮我一次也没什么吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#6P#0006F可是……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0302
    ChrTalk(
        0x103,
        (
            "#11P#0204F──所以，这项委托\x01",
            "就由我一个人来接受吧。\x02\x03",

            "#0202F罗伊德前辈，你们就请\x01",
            "继续处理其它支援工作吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x104, 0x2)
    Sleep(1000)

    #C0303
    ChrTalk(
        0x101,
        "#6P#0005F缇欧……！？\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        "#6P#0101F可、可是……\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        (
            "#11P#0202F只是一次普通的分工而已。\x02\x03",

            "既然是黑客方面的事情，\x01",
            "有我一个人也就足够了。\x02\x03",

            "至于大家，就算少了我一个人，\x01",
            "应该也不会妨碍到一般支援工作的完成吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#0301F可是，另一个终端是在车站前面的\x01",
            "那个地下空间的深处吧？\x02\x03",

            "多少也有些危险吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x103,
        (
            "#2P#0204F没关系，我会设法解决的。\x02\x03",

            "如果是那种地方的魔兽，\x01",
            "凭我一个人应该就能够应付了。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x102,
        "#6P#0108F缇欧……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0309
    ChrTalk(
        0x101,
        (
            "#6P#0004F──那么，不如这样好了。\x02\x03",

            "#0000F我陪缇欧一起处理这边的事，\x01",
            "艾莉和兰迪回警察局总部帮忙，\x01",
            "怎么样？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0310
    ChrTalk(
        0x103,
        "#11P#0205F哎……\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x104,
        (
            "#0300F嗯，这主意不错哦。\x02\x03",

            "再怎么说，也不应该让阿缇\x01",
            "孤身涉险嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        (
            "#6P#0103F是啊，我也反对缇欧自己去。\x02\x03",

            "#0100F反正总部那边的杂事根本忙不完，\x01",
            "多一个人或少一个人也没什么区别。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        "#11P#0208F可、可是……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0314
    ChrTalk(
        0x8,
        (
            "#5P#2300F这不是很好嘛，\x01",
            "用不着太客气吧～？\x02\x03",

            "原来你是那种会在意\x01",
            "这类事情的人吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(150)

    #C0315
    ChrTalk(
        0x103,
        "#11P#0201F…………………（瞪）\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(800)
    OP_64(0x8)

    #C0316
    ChrTalk(
        0x8,
        "#5P#2305F哇哇，你生什么气嘛～？\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x103,
        "#11P#0203F……………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0318
    ChrTalk(
        0x103,
        (
            "#11P#0202F……明白了。\x02\x03",

            "既然如此，尽量在今天之内\x01",
            "把该做的事情都做完吧。\x02\x03",

            "我想，一旦开始行动，\x01",
            "不到太阳下山大概是不会结束的。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        "#6P#0000F嗯，看起来确实如此呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xA0, 4)
    OP_29(0x45, 0x4, 0x2)
    OP_29(0x45, 0x1, 0x0)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还有其它事情需要处理】\x01",      # 0
            "【所有事情都已经解决了】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A19B"),
        (1, "loc_A32A"),
        (SWITCH_DEFAULT, "loc_A605"),
    )


    label("loc_A19B")

    SetChrSubChip(0x8, 0x0)
    Sleep(300)
    OP_29(0x45, 0x1, 0x1)

    #C0320
    ChrTalk(
        0x8,
        (
            "#11P#2302F呼，那就赶快\x01",
            "去处理啊。\x02\x03",

            "在那之前，我就先来\x01",
            "做一些设置工作。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    SetChrPos(0x8, 498200, 200, 302000, 0)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_68(500600, 1000, 296300, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33000, 0)
    SetChrPos(0x0, 500600, 0, 296300, 180)
    SetChrPos(0x1, 500600, 0, 296300, 180)
    SetChrPos(0x2, 500600, 0, 296300, 180)
    SetChrPos(0x3, 500600, 0, 296300, 180)
    SetMapObjFrame(0xFF, "pizza", 0x1, 0x1)
    Sleep(10)
    PlayBGM("ed7521", 0)
    EventEnd(0x5)
    Jump("loc_A605")

    label("loc_A32A")

    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0321
    ChrTalk(
        0x8,
        (
            "#11P#2309F好～那么就立刻开始\x01",
            "商量具体分工吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 495400, 0, 295400, 90)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 495400, 0, 297200, 90)
    Sound(820, 0, 100, 0)
    OP_0D()

    def lambda_A3B4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A3B4)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0322
    ChrTalk(
        0x102,
        (
            "#12P#0100F那，我就和兰迪\x01",
            "去警察局总部了。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x104,
        (
            "#0300F#5P罗伊德，\x01",
            "阿缇就拜托你啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0324
    ChrTalk(
        0x101,
        (
            "#6P#0004F嗯，交给我吧。\x02\x03",

            "#0000F……兰迪，\x01",
            "工作可别偷懒哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x104,
        (
            "#0309F#5P（戳中软肋）……\x01",
            "哈哈，我什么时候偷过懒。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x102,
        "#12P#0104F算了，反正有我在旁边监督呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0327
    ChrTalk(
        0x102,
        "#6P#0102F缇欧，加油哦。\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x103,
        "#0202F#11P……是，艾莉前辈也请加油。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 27)
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 28)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x102, 0x3)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x104, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    Sleep(10)
    PlayBGM("ed7521", 0)
    VolumeBGM(0x28, 0xC8)
    Call(0, 29)
    Jump("loc_A605")

    label("loc_A605")

    Return()

    # Function_25_87ED end

    def Function_26_A606(): pass

    label("Function_26_A606")


    def lambda_A60B():
        OP_96(0xFE, 0x7A058, 0x0, 0x48FF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A60B)
    Sleep(400)

    def lambda_A628():
        OP_96(0xFE, 0x7A440, 0x0, 0x49188, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A628)
    Sleep(400)

    def lambda_A645():
        OP_96(0xFE, 0x7A120, 0x0, 0x48A80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A645)
    Sleep(400)

    def lambda_A662():
        OP_96(0xFE, 0x7A5D0, 0x0, 0x48DA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A662)
    WaitChrThread(0x103, 1)

    def lambda_A680():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A680)
    WaitChrThread(0x102, 1)

    def lambda_A691():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A691)
    WaitChrThread(0x101, 1)

    def lambda_A6A2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A6A2)
    WaitChrThread(0x104, 1)

    def lambda_A6B3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A6B3)
    WaitChrThread(0x104, 2)
    Return()

    # Function_26_A606 end

    def Function_27_A6C0(): pass

    label("Function_27_A6C0")


    def lambda_A6C5():
        OP_95(0xFE, 499700, 0, 291700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A6C5)
    Sleep(500)
    SetChrSubChip(0x103, 0x1)
    WaitChrThread(0x102, 1)

    def lambda_A6EA():
        OP_95(0xFE, 499700, 0, 287700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A6EA)
    WaitChrThread(0x102, 1)
    Return()

    # Function_27_A6C0 end

    def Function_28_A704(): pass

    label("Function_28_A704")


    def lambda_A709():
        OP_95(0xFE, 495400, 0, 295400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A709)
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    WaitChrThread(0x104, 1)

    def lambda_A735():
        OP_95(0xFE, 499700, 0, 291700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A735)
    WaitChrThread(0x104, 1)

    def lambda_A753():
        OP_95(0xFE, 499700, 0, 287700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A753)
    WaitChrThread(0x104, 1)
    Return()

    # Function_28_A704 end

    def Function_29_A76D(): pass

    label("Function_29_A76D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(500080, 1000, 207690, 0)
    MoveCamera(36, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x101, 500400, 0, 205500, 0)
    SetChrPos(0x103, 499300, 0, 205600, 0)
    SetChrPos(0x8, 499800, 150, 207700, 180)
    OP_70(0x13, 0xA)
    ClearMapObjFlags(0x13, 0x10)
    FadeToBright(1000, 0)
    OP_0D()

    #C0329
    ChrTalk(
        0x8,
        (
            "#2302F#5P──那么，等你们到了那边之后，\x01",
            "就用艾尼格玛和我联络吧。\x02\x03",

            "到时就开始作战！\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x103,
        "#6P#0202F明白了。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#12P#0006F……虽然不太懂，\x01",
            "但尽量不要做得太过火啊。\x02\x03",

            "#0001F不能给使用导力网络\x01",
            "的人们制造麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        (
            "#2303F#5P哈，这种事还用得着你说啊。\x02\x03",

            "#2300F我也好，缇欧也好，还有那个『小猫』，\x01",
            "我们都不是那种会被\x01",
            "普通用户察觉到的外行人啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0333
    ChrTalk(
        0x103,
        (
            "#6P#0204F在名为『网络』领域里，暗中\x01",
            "展开二对一的捉迷藏……\x02\x03",

            "#0202F大概就是这种感觉，\x01",
            "所以没必要担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯～……\x01",
            "算了，既然如此，应该就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x8,
        (
            "#2309F#5P那就请多指教了啊～\x02\x03",

            "#2302F嗯～肚子也有点饿了，\x01",
            "不然就叫份比萨好了～¤\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AA61():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AA61)
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_AA75():
        OP_95(0xFE, 499800, 15, 209700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AA75)
    Sleep(100)

    def lambda_AA92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AA92)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_71(0x13, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x13)
    SetMapObjFlags(0x13, 0x10)
    OP_68(500550, 1000, 207480, 1000)

    def lambda_AAE1():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AAE1)
    Sleep(50)

    def lambda_AAF1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AAF1)
    OP_6F(0x1)

    #C0336
    ChrTalk(
        0x101,
        (
            "#0003F#11P真拿他没办法……\x02\x03",

            "#0000F那么，我们就从这里出去，\x01",
            "向克洛斯贝尔车站进发吧。\x02\x03",

            "是在地下空间Ａ区域\x01",
            "的深处吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x103,
        (
            "#6P#0204F对，『第３控制终端』就在那里。\x02\x03",

            "#0202F至于具体位置，\x01",
            "等到了那里之后再做说明。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        "#0000F明白，那我们就出发吧。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)

    def lambda_AC09():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AC09)
    Sleep(100)

    def lambda_AC19():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AC19)
    WaitChrThread(0x101, 2)

    def lambda_AC2A():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC2A)
    WaitChrThread(0x103, 2)

    def lambda_AC43():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AC43)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0x5C, 1)
    NewScene("c000C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_A76D end

    def Function_30_AC7D(): pass

    label("Function_30_AC7D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    LoadChrToIndex("apl/ch50330.itc", 0x20)
    LoadChrToIndex("apl/ch50331.itc", 0x21)
    LoadChrToIndex("apl/ch50090.itc", 0x22)
    SoundLoad(909)
    OP_68(496800, 1400, 296600, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 495000, 200, 296900, 90)
    SetChrPos(0x103, 495000, 200, 295700, 90)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 497700, 200, 296300, 270)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x18)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 495850, 250, 296700, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x18)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 495850, 250, 295900, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x18)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 496850, 250, 296300, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetMapObjFrame(0xFF, "pizza", 0x0, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis051.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0339
    AnonymousTalk(
        0x103,
        "#0205F罗赞贝尔克工房……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(496800, 900, 296600, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0340
    ChrTalk(
        0x101,
        (
            "#0005F#5P等、等一下。\x02\x03",

            "#0001F罗赞贝尔克工房……\x01",
            "就是那个制作人偶的工房吧？\x02\x03",

            "位于北部山道的途中……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x8,
        (
            "#2306F#11P是啊，正是如此！\x02\x03",

            "#2310F不过，在对『小猫』的地址进行解析之后，\x01",
            "查到访问点的位置就是那里！\x02\x03",

            "哈！\x01",
            "开什么玩笑啊，这怎么可能！？\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        "#6P#0208F确实是……难以理解呢。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0343
    ChrTalk(
        0x101,
        (
            "#0001F#5P……怎么回事？\x02\x03",

            "『小猫』在那个工房里，\x01",
            "难道是件很奇怪的事情吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(200)

    #C0344
    ChrTalk(
        0x103,
        (
            "#6P#0206F那个……\x02\x03",

            "#0201F目前铺设在自治州范围内\x01",
            "的导力网络，基本只覆盖了\x01",
            "市内与乌尔斯拉医院。\x02\x03",

            "至于其它地方，最多也就是位于湖对岸\x01",
            "的那个疗养地，米修拉姆吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0345
    ChrTalk(
        0x101,
        "#0005F#5P啊……\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x8,
        (
            "#2303F#11P……因为无线导力波不太稳定，\x01",
            "所以目前只能用于普通的导力通讯装置中。\x02\x03",

            "而需要传送大量情报资料的导力网络，\x01",
            "基本都是使用有线装置的。\x02\x03",

            "#2310F像乌尔斯拉医院和米修拉姆，\x01",
            "都是在湖底架设了导力缆线……\x02\x03",

            "不管怎么想，远在山道尽头的工房里\x01",
            "也不可能铺设导力缆线啊！\x02\x03",

            "#2311F啊，真是的！\x01",
            "这到底是什么花招啊～！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0347
    ChrTalk(
        0x101,
        "#0003F#5P嗯～……\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x32, 0x1F4)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x320)

    #C0348
    ChrTalk(
        0x101,
        "#0008F#5P（………难道说……………）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0349
    ChrTalk(
        0x103,
        (
            "#6P#0203F──算了，虽然还残留着一些未解的谜团，\x01",
            "但我们也有收获，这就已经不错了。\x02\x03",

            "#0202F那么，我们可以收取报酬了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x8,
        (
            "#2306F#11P呼……知道了。\x02\x03",

            "如果没有你们的帮助，\x01",
            "肯定也查不到这么多啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0351
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '沉重货物'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('沉重货物', 1)
    Sleep(300)

    #C0352
    ChrTalk(
        0x101,
        (
            "#0001F#5P这个……\x01",
            "就是我们会感兴趣的情报吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x8,
        (
            "#2303F#11P……坦白地说，\x01",
            "这是有关『鲁巴彻』的情报。\x02\x03",

            "#2300F而且还附带着一些相关信息资料，\x01",
            "对你们来说，应该是很贵重的吧～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0354
    ChrTalk(
        0x101,
        "#0005F#5P这个……\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x103,
        (
            "#6P#0201F……原来如此，\x01",
            "确实可以说是我们最想了解的情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        (
            "#2306F#11P我先把话说在前面，这些情报，\x01",
            "那些该知道的家伙们都已经全部知道了哦。\x02\x03",

            "比如说，像警察局的高层人物之类的，\x01",
            "大概已经对这些有所掌握了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x101,
        (
            "#0004F#5P没关系，这就足够了。\x02\x03",

            "#0000F我们完全找不到这方面的情报，\x01",
            "正好觉得有些头疼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        "#2303F#11P啊，是吗，那就好。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_68(497430, 900, 296660, 1000)
    SetCameraDistance(17100, 1000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 497700, 250, 296000, 0)
    Sound(804, 0, 100, 0)
    Sound(909, 2, 100, 0)
    BeginChrThread(0x8, 3, 0, 31)
    OP_0D()
    Sleep(1000)

    #C0359
    ChrTalk(
        0x8,
        (
            "#2311F#11P啊～真是的……我要睡了！\x02\x03",

            "明天要以刚才取得的那些线索为基础，\x01",
            "继续追查『小猫』的身份～！\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x101,
        (
            "#0012F哈哈，量力而行吧。\x02\x03",

            "#0000F难得的纪念庆典，\x01",
            "不要老是闷在这种地方，\x01",
            "偶尔也出去约个会如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x8,
        (
            "#2310F#11P吵、吵死了～\x01",
            "不需要你来多管闲事～！\x02\x03",

            "你这个伪装成温和无害的娃娃脸，\x01",
            "实际上却四处沾花惹草的人生赢家！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0362
    ChrTalk(
        0x101,
        (
            "#0013F#5P……完全不明白你在说什么，\x01",
            "不过似乎是不当的恶意中伤啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    #C0363
    ChrTalk(
        0x103,
        (
            "#6P#0203F说起来……\x02\x03",

            "罗伊德前辈在纪念庆典的第一天\x01",
            "就和塞茜尔小姐约会了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    #C0364
    ChrTalk(
        0x101,
        "#0005F#5P哎……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_B8E6")

    #C0365
    ChrTalk(
        0x103,
        (
            "#6P#0211F之后又左拥右抱，和诺艾尔上士姐妹\x01",
            "一起享受快乐时光……\x02\x03",

            "原来如此，有经验的人，\x01",
            "说出的话就是很有分量呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B95B")

    label("loc_B8E6")


    #C0366
    ChrTalk(
        0x103,
        (
            "#6P#0211F之后又和兰迪前辈一起，\x01",
            "与那些护士小姐开心地玩了个够。\x02\x03",

            "原来如此，有经验的人，\x01",
            "说出的话就是很有分量呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B95B")

    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0367
    ChrTalk(
        0x101,
        (
            "#0012F#5P那个，缇欧小姐，\x01",
            "您好像话中有话啊……？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x103,
        "#6P#0204F不，没什么。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17600, 2000)
    FadeToDark(2000, 0, -1)
    BeginChrThread(0x11, 1, 0, 32)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x11, 1)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_24(0x38D)
    SetScenarioFlags(0x5C, 5)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_AC7D end

    def Function_31_BA88(): pass

    label("Function_31_BA88")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BAA2")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x0, 0x2)
    Jump("Function_31_BA88")

    label("loc_BAA2")

    Return()

    # Function_31_BA88 end

    def Function_32_BAA3(): pass

    label("Function_32_BAA3")

    Sleep(500)
    OP_25(0x38D, 0x5A)
    Sleep(200)
    OP_25(0x38D, 0x50)
    Sleep(200)
    OP_25(0x38D, 0x46)
    Sleep(200)
    OP_25(0x38D, 0x3C)
    Sleep(200)
    OP_25(0x38D, 0x32)
    Sleep(200)
    OP_25(0x38D, 0x28)
    Sleep(200)
    OP_25(0x38D, 0x1E)
    Sleep(200)
    OP_25(0x38D, 0x14)
    Sleep(200)
    OP_25(0x38D, 0xA)
    Sleep(200)
    OP_24(0x38D)
    Return()

    # Function_32_BAA3 end

    def Function_33_BAE9(): pass

    label("Function_33_BAE9")

    EventBegin(0x1)

    #C0369
    ChrTalk(
        0x101,
        (
            "#0001F（犯人应该就在\x01",
            "  那个房间里……）\x02\x03",

            "（总之，先看看里面的情况吧。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 502470, 0, 199800, 270)
    EventEnd(0x4)
    Return()

    # Function_33_BAE9 end

    SaveToFile()

Try(main)
