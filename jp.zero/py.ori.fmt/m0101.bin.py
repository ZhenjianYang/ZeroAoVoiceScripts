from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ヨナ",                   # 1
        "食器",                   # 2
        "食器",                   # 3
        "食器",                   # 4
        "食器",                   # 5
        "食器",                   # 6
        "食器",                   # 7
        "ジェットトータス",       # 8
        "ギーヌーナ",             # 9
        "SE制御",                 # 10
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

    Sepith("Sepith_C807", 12,  1,   8,   0,   3,   7,   0)
    Sepith("Sepith_C7F7", 0,   12,  5,   0,   7,   2,   6)
    Sepith("Sepith_C80F", 0,   0,   0,   10,  7,   7,   7)
    Sepith("Sepith_C7FF", 8,   0,   12,  0,   0,   5,   7)

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
        "BattleInfo_778", 0x0000, 18, 6, 60, 6, 1, 25, 0, "bm0101", "Sepith_C807", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
        )
    )

    BattleInfo(
        "BattleInfo_5E8", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_C7F7", 30, 45, 20, 5,
        (
            ("ms63800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms63800.dat", "ms63800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms63800.dat", "ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
        )
    )

    BattleInfo(
        "BattleInfo_B60", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_C80F", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_548", "MonsterBattlePostion_5A8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_528", "MonsterBattlePostion_5A8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_548", "MonsterBattlePostion_5A8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_528", "MonsterBattlePostion_5A8", "ed7400", "ed7403", "ATBonus_4E8"),
        )
    )

    BattleInfo(
        "BattleInfo_840", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_C80F", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_568", "MonsterBattlePostion_5C8", "ed7400", "ed7403", "ATBonus_4E8"),
        )
    )

    BattleInfo(
        "BattleInfo_6B0", 0x0000, 18, 6, 60, 6, 1, 30, 0, "bm0101", "Sepith_C7FF", 30, 45, 20, 5,
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
        "Function_6_17F0",         # 06, 6
        "Function_7_193D",         # 07, 7
        "Function_8_1A8A",         # 08, 8
        "Function_9_1C9D",         # 09, 9
        "Function_10_4A48",        # 0A, 10
        "Function_11_4D22",        # 0B, 11
        "Function_12_4E80",        # 0C, 12
        "Function_13_4F8B",        # 0D, 13
        "Function_14_4FA7",        # 0E, 14
        "Function_15_4FC3",        # 0F, 15
        "Function_16_4FDF",        # 10, 16
        "Function_17_54D5",        # 11, 17
        "Function_18_5667",        # 12, 18
        "Function_19_57AE",        # 13, 19
        "Function_20_583F",        # 14, 20
        "Function_21_6081",        # 15, 21
        "Function_22_60DD",        # 16, 22
        "Function_23_64C1",        # 17, 23
        "Function_24_8F35",        # 18, 24
        "Function_25_8FEF",        # 19, 25
        "Function_26_B13A",        # 1A, 26
        "Function_27_B1F4",        # 1B, 27
        "Function_28_B238",        # 1C, 28
        "Function_29_B2A1",        # 1D, 29
        "Function_30_B82F",        # 1E, 30
        "Function_31_C702",        # 1F, 31
        "Function_32_C71D",        # 20, 32
        "Function_33_C763",        # 21, 33
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AA")
    Sound(14, 0, 100, 0)
    OP_71(0x14, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D8")
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
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_16B9"),
        (2, "loc_16C8"),
        (1, "loc_16D5"),
        (SWITCH_DEFAULT, "loc_16D8"),
    )


    label("loc_16B9")

    SetScenarioFlags(0x74, 6)
    OP_70(0x14, 0x1E)
    Sleep(500)
    Jump("loc_16D8")

    label("loc_16C8")

    OP_70(0x14, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_16D5")

    OP_B7(0x0)
    Return()

    label("loc_16D8")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x86, 1)"), scpexpr(EXPR_END)), "loc_1735")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_17A5")

    label("loc_1735")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x14, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17A5")

    Jump("loc_17E4")

    label("loc_17AA")

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

    label("loc_17E4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_15DD end

    def Function_6_17F0(): pass

    label("Function_6_17F0")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18EC")
    Sound(14, 0, 100, 0)
    OP_71(0x15, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_1875")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_18E7")

    label("loc_1875")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x15, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18E7")

    Jump("loc_1931")

    label("loc_18EC")

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

    label("loc_1931")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_17F0 end

    def Function_7_193D(): pass

    label("Function_7_193D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A39")
    Sound(14, 0, 100, 0)
    OP_71(0x16, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_19C2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1A34")

    label("loc_19C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x16, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A34")

    Jump("loc_1A7E")

    label("loc_1A39")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
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

    label("loc_1A7E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_193D end

    def Function_8_1A8A(): pass

    label("Function_8_1A8A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C57")
    Sound(14, 0, 100, 0)
    OP_71(0x17, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B85")
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x10, 0x0, 0)
    OP_98(0x10, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1AE3():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1AE3)

    def lambda_1AFD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1AFD)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_1B66"),
        (2, "loc_1B75"),
        (1, "loc_1B82"),
        (SWITCH_DEFAULT, "loc_1B85"),
    )


    label("loc_1B66")

    SetScenarioFlags(0x74, 7)
    OP_70(0x17, 0x1E)
    Sleep(500)
    Jump("loc_1B85")

    label("loc_1B75")

    OP_70(0x17, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1B82")

    OP_B7(0x0)
    Return()

    label("loc_1B85")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E2, 1)"), scpexpr(EXPR_END)), "loc_1BE2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1C52")

    label("loc_1BE2")

    FadeToDark(300, 0, 100)

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x17, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1C52")

    Jump("loc_1C91")

    label("loc_1C57")

    FadeToDark(300, 0, 100)

    #A0014
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

    label("loc_1C91")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1A8A end

    def Function_9_1C9D(): pass

    label("Function_9_1C9D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D31")
    Jump("loc_1D7B")

    label("loc_1D31")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D51")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D7B")

    label("loc_1D51")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D71")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D7B")

    label("loc_1D71")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D7B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_21A8")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E4F")

    #C0015
    ChrTalk(
        0x8,
        (
            "#2306Fうあ～、アッタマ痛え～……\x02\x03",

            "#2310F寝起きじゃ上手く\x01",
            "キーボードが打てね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0006Fまったく……顔でも洗って\x01",
            "しゃんとして来たらどうだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A3")

    label("loc_1E4F")


    #C0017
    ChrTalk(
        0x8,
        (
            "#2300Fんー、なんだよ……\x01",
            "どっかに出かけるワケ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0000Fああ、ちょっとね。\x02\x03",

            "#0005F……なんだヨナ、\x01",
            "やけに食い付きが悪いな？\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F6B")
    Jump("loc_1FB5")

    label("loc_1F6B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F8B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FB5")

    label("loc_1F8B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FAB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FB5")

    label("loc_1FAB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FB5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0019
    ChrTalk(
        0x8,
        (
            "#2306F……さっき仮眠とって\x01",
            "起きたばっかりなんだよ……\x02\x03",

            "そのくらい察しろっての……\x01",
            "これだからノーミソの回転が\x01",
            "悪い人間はよー……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0006Fはあ、まったく……\x02\x03",

            "#0001F（俺も人のこと言えないけど\x01",
            "  不規則な生活をしてるよな。）\x02\x03",

            "#0003F（やっぱり一度、財団の方に\x01",
            "  連絡した方がいいんじゃ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        (
            "#0211F……ロイドさん。\x01",
            "保護者的な顔つきになってます。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 750)

    #C0022
    ChrTalk(
        0x101,
        "#0011Fへ……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        "#0100Fクスクス……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#0304Fやれやれ……\x01",
            "お前もホントお人好しだねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_21A3")

    Jump("loc_4A40")

    label("loc_21A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2805")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_23CE")

    #C0025
    ChrTalk(
        0x8,
        (
            "#2310Fくそっ、この\x01",
            "天才ヨナ様に向かって……\x01",
            "覚えてろよっ……！\x02\x03",

            "あんたらの目玉が\x01",
            "飛び出るくらいの情報を\x01",
            "集めてきてやるからなっ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2369")

    #C0026
    ChrTalk(
        0x10A,
        (
            "#0603Fせいぜいその調子で\x01",
            "情報を集めておけ……\x02\x03",

            "後で追って問い合わせる。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#2305Fへ……？\x02\x03",

            "#2301Fだ、誰だよオッサン！\x01",
            "ボクはアンタなんかとは\x01",
            "取引しないぜっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x10A,
        (
            "#0600Fじきに分かる。\x01",
            "さっさと仕事をしろ、情報屋。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0000F（はは、やっぱり捜査一課は\x01",
            "  全部掴んでいるか……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C9")

    label("loc_2369")


    #C0030
    ChrTalk(
        0x103,
        (
            "#0203F（情報屋としてのプライドが\x01",
            "  傷付いたみたいですね。\x01",
            "  ……まあどうでもいいですが。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C9")

    Jump("loc_2800")

    label("loc_23CE")

    SetChrSubChip(0x8, 0x0)
    OP_63(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x8,
        (
            "#2306Fちぇっ、なんだよ～。\x01",
            "今日はロクな情報がないじゃん。\x02\x03",

            "てっきりマフィアどもの抗争に\x01",
            "進展があると思ったのにさ～。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_250D")
    Jump("loc_2557")

    label("loc_250D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_252D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2557")

    label("loc_252D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_254D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2557")

    label("loc_254D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2557")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Sleep(1000)

    #C0032
    ChrTalk(
        0x8,
        (
            "#2305Fおっ、丁度良かった。\x02\x03",

            "#2302Fなあアンタら、\x01",
            "なんか良い情報持ってねえ？\x02\x03",

            "#2309F今なら３割増しで\x01",
            "買い取ってやるけど～？\x02",
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
            "#0006Fうーん、どうやら\x01",
            "無駄足だったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        "#0108Fひょっとしたらと思ったけど……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#0203Fまあ、情報通を気取っても\x01",
            "どこか抜けている子ですから。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2721")

    #C0036
    ChrTalk(
        0x10A,
        "#0603F……フム、この程度か。\x02",
    )

    CloseMessageWindow()

    label("loc_2721")

    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0037
    ChrTalk(
        0x8,
        (
            "#2305Fな、なんだよその反応……\x02\x03",

            "#2307F分かった、今から潜って\x01",
            "アンタらの欲しい情報を\x01",
            "取ってきてやる！\x02\x03",

            "ほら、何でも\x01",
            "いいから言ってみろよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        (
            "#0300Fはは……お前も\x01",
            "結構意地っ張りだよなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    SetScenarioFlags(0xCD, 2)

    label("loc_2800")

    Jump("loc_4A40")

    label("loc_2805")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_2A66")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_28E2")

    #C0039
    ChrTalk(
        0x8,
        (
            "#2301Fここからここまでが\x01",
            "Ａランクで、ここからはＢ……\x02\x03",

            "ルバーチェが新たに\x01",
            "どこかの猟兵団を雇ったって噂は\x01",
            "……まあ怪しいからＣでいいか。\x02\x03",

            "#2304Fさーて、どのくらい\x01",
            "お得意様が喰い付くかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A61")

    label("loc_28E2")


    #C0040
    ChrTalk(
        0x8,
        (
            "#2309Fキタキタキタ～！\x02\x03",

            "黒月襲撃に関する情報が\x01",
            "続々集まって来やがったぜ～っ！\x02\x03",

            "#2301Fあとは重要度ごとにランク付けして\x01",
            "パッケージングすれば……\x02\x03",

            "#2309Fうひゃひゃひゃ！\x01",
            "ボロ儲け間違いナシだぜぇ！\x02",
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
        "#0006F（集中してるみたいだな……）\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#0200F（まあ、放っておきましょう。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2A61")

    Jump("loc_4A40")

    label("loc_2A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2E59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2B54")

    #C0043
    ChrTalk(
        0x8,
        (
            "#2305Fさ、最初はボクも驚いたんだよ！\x01",
            "すっげービッグニュースだったからさ。\x02\x03",

            "#2303Fそれをつい、\x01",
            "あんたらに話しちまったから\x01",
            "代金分を少し返してくれって話じゃん。\x02\x03",

            "#2300Fそんなに怒んなよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#0006Fまったく……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E54")

    label("loc_2B54")

    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ヨナは宅配ピザを頬張っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0046
    ChrTalk(
        0x8,
        (
            "#2303Fムシャムシャ……ごっくん。\x02\x03",

            "#2300Fで、どうだったんだよ、\x01",
            "黒月の事務所は！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_END)), "loc_2C8E")

    #C0047
    ChrTalk(
        0x101,
        (
            "#0003Fああ、確かにあれは……\x01",
            "………………………………\x02\x03",

            "#0001F……ヨナ、まさかとは思うが。\x02\x03",

            "この情報を導力ネット上で\x01",
            "売りさばいたりしないよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        "#2305Fギクッ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D4B")

    label("loc_2C8E")


    #C0049
    ChrTalk(
        0x101,
        (
            "#0000Fああ、まだ見てないよ。\x01",
            "これから行ってくる所だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "#2306Fチッ、なんだよ……\x02\x03",

            "ぱぱっと見てきて\x01",
            "知らせてくんなきゃダメだろ。\x02\x03",

            "#2300F首なが～くして\x01",
            "待ってる客もいるんだからさぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D4B")


    #C0051
    ChrTalk(
        0x104,
        (
            "#0306Fなんだ、情報を流したのは\x01",
            "そういう腹積もりかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#0200Fヨナ……覚悟はいいですか？\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#2305Fわああっ、その……\x02\x03",

            "#2306F情報料分、少しでも\x01",
            "返してもらおうと思っただけだろっ！\x01",
            "そんなに怒んなよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        (
            "#0106F（この子の場合\x01",
            "  態度が問題なのよね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2E54")

    Jump("loc_4A40")

    label("loc_2E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_31B2")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 1)), scpexpr(EXPR_END)), "loc_2F14")

    #C0055
    ChrTalk(
        0x8,
        (
            "#2306Fむにゃむにゃ……\x02\x03",

            "#2311F……むぐぐっ、んがっ……\x01",
            "《仔猫#4Rキティ#》めぇ……よくもォ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#0012F（相変わらずレンに\x01",
            "  翻弄されてるのかな……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31AD")

    label("loc_2F14")


    #C0057
    ChrTalk(
        0x8,
        "#2303Fくかー……むにゃむにゃ……\x02",
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
        "#0305F寝てやがる……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x109,
        (
            "#0500Fもしかして……\x01",
            "この子がフランの言っていた\x01",
            "《情報屋》ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#0104Fええ、そうよ。\x01",
            "……日中はダメみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#0206F夜型人間のヨナに\x01",
            "今の時間は厳しいかと。\x02\x03",

            "#0202F……つまり今の時間帯なら\x01",
            "簡単にハッキングを\x01",
            "仕掛けることができます。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 750)

    #C0062
    ChrTalk(
        0x101,
        (
            "#0005Fな、なるほど……\x02\x03",

            "#0006Fってかダメだろティオ、\x01",
            "ハッキングなんて……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 750)

    #C0063
    ChrTalk(
        0x103,
        (
            "#0204Fまだ犯罪ではありませんが……\x01",
            "それにたまにしか仕掛けてません。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#0006Fう、うーん。\x02\x03",

            "#0001Fせめて必要なときだけとかに\x01",
            "限定してくれよ……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 1)

    label("loc_31AD")

    Jump("loc_4A40")

    label("loc_31B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_364C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 3)), scpexpr(EXPR_END)), "loc_32C2")

    #C0065
    ChrTalk(
        0x8,
        (
            "#2306F《黒の競売会》に関しては\x01",
            "ボクが譲ってやった情報が\x01",
            "元になったみたいだし……\x02\x03",

            "#2301Fその、今回は\x01",
            "ちょっとしたサービスだ。\x01",
            "ありがたく思えよなっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x153,
        (
            "#1110Fあれー？\x01",
            "なんかカオあかいよー？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#2311F#4Sだああ～～っ……\x01",
            "うるせーっつーの！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3647")

    label("loc_32C2")


    #C0068
    ChrTalk(
        0x153,
        (
            "#1105F……あれー？\x01",
            "時々ティオとたんまつで\x01",
            "話してるヒトだー。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "#2305Fおっと、例のガキンチョと\x01",
            "支援課のおでましじゃん。\x02\x03",

            "#2302Fハッ、１週間ぶりに浴びる\x01",
            "外の日の光はどうよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#0006Fお前にだけは\x01",
            "言われたくないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "#2304F裏の競売会に潜り込む方が\x01",
            "イカレてるつーの。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_342C")

    #C0072
    ChrTalk(
        0x102,
        (
            "#0101Fそれでヨナ君、結局\x01",
            "キーアちゃんについての情報は？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D0")

    label("loc_342C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_347A")

    #C0073
    ChrTalk(
        0x103,
        (
            "#0201Fヨナ、それで結局\x01",
            "キーアについての情報は……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D0")

    label("loc_347A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34D0")

    #C0074
    ChrTalk(
        0x104,
        (
            "#0301Fそんでヨナ公、\x01",
            "キー坊についての情報は\x01",
            "結局どうだったんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D0")


    #C0075
    ChrTalk(
        0x8,
        (
            "#2305Fあー、あれから\x01",
            "一応思いつく限りは\x01",
            "全部探ってみたけどさぁ……\x02\x03",

            "#2301F身元も経緯も全く無し。\x01",
            "少なくとも導力ネット上には\x01",
            "存在しないって言い切れるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#0003Fやっぱりそうか……\x02\x03",

            "#0000Fサンキュー、\x01",
            "今回は世話になったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "#2307Fべ、別にアンタらに\x01",
            "協力したわけじゃ……\x02",
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
            "#2306F情報料はまけとくから、\x01",
            "今度何かいいネタ回せよなっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 3)

    label("loc_3647")

    Jump("loc_4A40")

    label("loc_364C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_38AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_36EA")

    #C0079
    ChrTalk(
        0x8,
        (
            "#2302Fま、どこに行くにしても\x01",
            "せいぜい気を付けなよ。\x02\x03",

            "今日で祭りも締めってんで\x01",
            "大した人出らしいし。\x01",
            "警察もどたばたしそうだよな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A5")

    label("loc_36EA")


    #C0080
    ChrTalk(
        0x8,
        (
            "#2301Fんー、なんだよアンタら。\x01",
            "どっかに出かけんのか？\x02\x03",

            "#2305Fそういや今日って最終日か。\x01",
            "あの《黒の競売会#10Rシュバルツオークション#》のある……\x02",
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
            "#2309Fハハ、んなわけねえよな！\x02\x03",

            "#2302Fま、どこに行くにしても\x01",
            "せいぜい気を付けなよ。\x02\x03",

            "今日で祭りも締めってんで\x01",
            "大した人出らしいじゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#0301F相変わらず\x01",
            "生意気なガキだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#0006Fむしろそっちこそ\x01",
            "ネット上でトラブらないように\x01",
            "気を付けて欲しい所なんだが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_38A5")

    Jump("loc_4A40")

    label("loc_38AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3AC9")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3933")

    #C0084
    ChrTalk(
        0x8,
        (
            "#2310F《仔猫》はボクと同じ\x01",
            "引きこもり野郎のはず……\x02\x03",

            "リアルの祭りに参加するはずが\x01",
            "………ぶつぶつ…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AC4")

    label("loc_3933")


    #C0085
    ChrTalk(
        0x8,
        (
            "#2310Fチクショウ……《仔猫》のやつ\x01",
            "今日はさっぱり現れない！\x02\x03",

            "#2305Fまさか、パレードを見に\x01",
            "出かけちまったとか……\x02\x03",

            "#2303Fいや、そんな事はありえねえ。\x01",
            "《仔猫》はボクと同じ\x01",
            "引きこもり野郎のはず……\x02\x03",

            "リアルの祭りに参加するはずが\x01",
            "………ぶつぶつ…………\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#0006F（意味はよく判らないが……\x01",
            "  《仔猫》を同類と\x01",
            "  決めて掛かってるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x103,
        (
            "#0202F（ヨナはこう見えて\x01",
            "  寂しがり屋ですから。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3AC4")

    Jump("loc_4A40")

    label("loc_3AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3F6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3B7A")

    #C0088
    ChrTalk(
        0x8,
        (
            "#2310Fティオ・プラトー、\x01",
            "《仔猫》の次はアンタを負かすからな。\x02\x03",

            "覚えとけよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x103,
        (
            "#0205Fヨナ……\x01",
            "意外と暇なようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        "#2311Fうっ、うるせー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F6A")

    label("loc_3B7A")


    #C0091
    ChrTalk(
        0x101,
        (
            "#0002Fヨナ、昨日は\x01",
            "有益な情報をありがとう。\x01",
            "参考になったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "#2309Fだろ～？\x01",
            "特にあの《黒の競売会#10Rシュバルツオークション#》……\x02\x03",

            "#2305F……あ、ちゃんと\x01",
            "データを見たのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#0103Fミシュラムで大々的に開かれる\x01",
            "盗品オークション兼、裏の社交界……\x02\x03",

            "#0101Fさすがに驚かされたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "#2309Fハッ、いい反応してくれるじゃん。\x02\x03",

            "#2304Fボクも前までは半信半疑だったんだが\x01",
            "偶然いい情報ソースを見つけちまってさ。\x02\x03",

            "#2302Fあんたらが好きそうだと思って\x01",
            "紛れ込ませておいたのさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x103,
        "#0206Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "#2302Fあ、ティオ。\x01",
            "あれ解くのにどれくらい掛かった？\x02\x03",

            "#2309F１時間くらい苦戦してくれてると\x01",
            "ボクとしちゃ\x01",
            "二ヤッとできるんだけどな！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x103,
        (
            "#0204F……３０秒もいりません。\x01",
            "ヨナ、あなたの思考パターンは\x01",
            "非常に読みやすいですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        "#2307Fうがあっ……！？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#0306Fヨナ公、そろそろ\x01",
            "ティオすけにちょっかい出すの\x01",
            "やめたらどうだ？\x02\x03",

            "#0300Fお前じゃ勝てねえって。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "#2310Fくっそー、次こそ、\x01",
            "次こそは……！\x02",
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

    label("loc_3F6A")

    Jump("loc_4A40")

    label("loc_3F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_41A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3FF6")

    #C0101
    ChrTalk(
        0x8,
        (
            "#2301Fと、とにかく\x01",
            "《第３制御端末》に急げよ。\x02\x03",

            "#2306F《仔猫》が現れてからじゃ\x01",
            "間に合わねえんだからさぁ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41A4")

    label("loc_3FF6")


    #C0102
    ChrTalk(
        0x8,
        (
            "#2300Fハッカー《仔猫》は\x01",
            "半年くらい前から現れて\x01",
            "ちょっかい掛けてきやがるんだ。\x02\x03",

            "#2302Fヘッ、だが今日こそは\x01",
            "この天才ヨナ様が\x01",
            "ゼッタイ尻尾掴んでやるぜ。\x02\x03",

            "#2301F《第３制御端末》は\x01",
            "クロスベル駅前から入れる\x01",
            "ジオフロントＡ区画の奥だ。\x02\x03",

            "ほら、２人とも\x01",
            "もたもたしてんじゃねーよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x103,
        "#0203Fヨナ、少々態度が大きいですね。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#0006F今すぐ協力を\x01",
            "取りやめてもいいんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#2306Fスミマセン、お２人とも\x01",
            "どうか急いでください……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_41A4")

    Jump("loc_4A40")

    label("loc_41A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 4)), scpexpr(EXPR_END)), "loc_41BA")
    Call(0, 10)
    Jump("loc_4A40")

    label("loc_41BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_43C3")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4237")

    #C0106
    ChrTalk(
        0x8,
        (
            "#2310Fよ、よりにもよって\x01",
            "僕のあの秘密をっ……\x02\x03",

            "ゼッタイに許さねぇ！\x01",
            "（カタカタカタカタカタ）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43BE")

    label("loc_4237")


    #C0107
    ChrTalk(
        0x8,
        (
            "#2311Fあーもう！\x01",
            "今度という今度は許さないぞ！\x02\x03",

            "#2310F見てろよ～っ……（カタカタカタ）\x02",
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
        "#0305Fヨナ公、なに熱くなってんだ？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            "#0206Fさあ……\x02\x03",

            "#0201Fでも、どうやら本気モードに\x01",
            "なっているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        "#0005Fそ、そうなのか。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#0106Fうーん、悪さをしないと\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_43BE")

    Jump("loc_4A40")

    label("loc_43C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4687")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_44A7")

    #C0112
    ChrTalk(
        0x8,
        (
            "#2306F記念祭っつっても\x01",
            "お得意様からの注文は\x01",
            "ふつーに来てるんだよ。\x02\x03",

            "こっちも仕事柄\x01",
            "手が離せないワケ。\x02\x03",

            "#2302Fま、何か面白い情報が\x01",
            "入ったら教えてやるよ。\x02\x03",

            "#2309F売れそうにない\x01",
            "クズ情報だけだけどな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4682")

    label("loc_44A7")


    #C0113
    ChrTalk(
        0x8,
        (
            "#2305Fなんだアンタらかよ。\x01",
            "……なんか用？\x02\x03",

            "#2302Fあ、もしかして記念祭だからって\x01",
            "浮かれちまってるわけ？\x02\x03",

            "#2309Fハッ、これだから\x01",
            "リアルの連中は始末が悪いよな～！\x02\x03",

            "ボクには行事ごとなんざ関係ねえし？\x01",
            "外に出るつもりもサラサラないっての！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#0006Fいつ来てもこの調子だな。\x02\x03",

            "#0001F相変わらずハッキングも\x01",
            "やりまくってるみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#0204Fまったくです。\x01",
            "昨日は散々負かしてあげたのに。\x02",
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
            "#2310Fティオ・プラトー！\x01",
            "いつか絶対負かすからな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_4682")

    Jump("loc_4A40")

    label("loc_4687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4945")

    #C0117
    ChrTalk(
        0x8,
        (
            "#2305Fそういえば……\x02\x03",

            "#2300Fアンタら、よくあの\x01",
            "ガラクタどもを突破できたな？\x02\x03",

            "#2302F銀の旦那ほどじゃないにしても\x01",
            "そこそこやるみたいじゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0005Fガラクタどもって\x01",
            "あの機械仕掛けの……？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x103,
        (
            "#0211Fまさかヨナ……\x01",
            "あなたが造って放ったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "#2306F違うって。\x01",
            "ハードはボクの専門じゃないだろ。\x02\x03",

            "#2300Fなんか、どこぞの技術者が造った\x01",
            "自動清掃装置の試作品らしいぜ？\x02\x03",

            "#2302F元々、地下に捨てられてたのを\x01",
            "何とか解析しようとしたら\x01",
            "暴走させちゃったんだけどさ～。\x02",
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
        "#0006F（やっぱり一枚噛んでたか……）\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x103,
        (
            "#0211F（……まあ、財団の研究所でも\x01",
            "  こんな悪戯ばかりしてた訳です。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x94, 1)
    Jump("loc_4A40")

    label("loc_4945")


    #C0123
    ChrTalk(
        0x8,
        (
            "#2302Fま、そこそこやるっつっても\x01",
            "銀の旦那には敵わないだろうけどな～。\x02\x03",

            "星見の塔だっけ？\x01",
            "行くんなら覚悟決めた方が\x01",
            "いいんじゃねーの。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A3D")

    #C0124
    ChrTalk(
        0x101,
        "#0006F（……どうにも生意気な奴だな……）\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        (
            "#0300F（ま、ともかく\x01",
            "  準備だけはしていこうぜ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A3D")

    SetScenarioFlags(0x0, 0)

    label("loc_4A40")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_1C9D end

    def Function_10_4A48(): pass

    label("Function_10_4A48")


    #C0126
    ChrTalk(
        0x8,
        (
            "#2305Fなに？\x01",
            "もう用事はいいのかよ？\x02",
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
            "【他の用事を片付ける】\x01",          # 0
            "【用事は一通り済んでいる】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4ADD"),
        (1, "loc_4B44"),
        (SWITCH_DEFAULT, "loc_4D21"),
    )


    label("loc_4ADD")


    #C0127
    ChrTalk(
        0x8,
        (
            "#2302Fハッ、だったら\x01",
            "とっとと済ませてきなよ。\x02\x03",

            "それまでこっちは\x01",
            "セッティングをしとくからさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D21")

    label("loc_4B44")


    #C0128
    ChrTalk(
        0x8,
        (
            "#2309Fよーし、だったら細かい\x01",
            "打ち合わせをしちまおうぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#0100Fじゃあ、私とランディは\x01",
            "警察本部の方に向かうわね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0130
    ChrTalk(
        0x104,
        (
            "#0300Fロイド。\x01",
            "ティオすけの事は頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0131
    ChrTalk(
        0x101,
        (
            "#0004Fああ、任せてくれ。\x02\x03",

            "#0000F……ランディは\x01",
            "仕事をサボったりするなよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x104,
        (
            "#0309Fギクッ……\x01",
            "ははっ、そんな滅相もない。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0133
    ChrTalk(
        0x102,
        "#0104Fまあ、私が一応監視してるから。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0134
    ChrTalk(
        0x102,
        "#0102Fティオちゃん、頑張ってね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0135
    ChrTalk(
        0x103,
        "#0202F……はい、エリィさんも。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x28, 0x3E8)
    Sleep(800)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    Call(0, 29)

    label("loc_4D21")

    Return()

    # Function_10_4A48 end

    def Function_11_4D22(): pass

    label("Function_11_4D22")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E44")
    SetChrName("")

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机の上には乱雑に\x01",
            "宅配ピザが置かれている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0137
    ChrTalk(
        0x101,
        (
            "#0006Fどういう食生活をしてるんだよ、\x01",
            "まったく……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0138
    ChrTalk(
        0x101,
        (
            "#0005Fあ、でもこれ位なら\x01",
            "食材があれば作れそうだよな。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1B2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xC)
    Jump("loc_4E7C")

    label("loc_4E44")

    SetChrName("")

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机の上には乱雑に\x01",
            "宅配ピザが置かれている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4E7C")

    TalkEnd(0xFF)
    Return()

    # Function_11_4D22 end

    def Function_12_4E80(): pass

    label("Function_12_4E80")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0141
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F6D")
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

    label("loc_4F6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F89")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_4F89")

    Return()

    # Function_12_4E80 end

    def Function_13_4F8B(): pass

    label("Function_13_4F8B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_4F8B end

    def Function_14_4FA7(): pass

    label("Function_14_4FA7")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_4FA7 end

    def Function_15_4FC3(): pass

    label("Function_15_4FC3")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_4FC3 end

    def Function_16_4FDF(): pass

    label("Function_16_4FDF")


    #A0142
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水位調整用の制御装置がある。\x01",
            "操作しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54D4")
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50CB")
    SetChrPos(0x0, 107620, -6000, 200, 0)
    SetChrPos(0x1, 108620, -6000, -600, 0)
    SetChrPos(0x2, 106620, -6000, -600, 0)
    SetChrPos(0x3, 107620, -6000, -1900, 0)
    OP_68(107660, -5000, 850, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28500, 0)
    Jump("loc_51D2")

    label("loc_50CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5151")
    SetChrPos(0x0, 85000, -6000, 101000, 0)
    SetChrPos(0x1, 83800, -6000, 101000, 0)
    SetChrPos(0x2, 83800, -6000, 99800, 0)
    SetChrPos(0x3, 85000, -6000, 99800, 0)
    OP_68(84580, -5000, 101000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27000, 0)
    Jump("loc_51D2")

    label("loc_5151")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51D2")
    SetChrPos(0x0, 201500, -6000, 184020, 90)
    SetChrPos(0x1, 200000, -6000, 184620, 90)
    SetChrPos(0x2, 200000, -6000, 184220, 90)
    SetChrPos(0x3, 198500, -6000, 184020, 90)
    OP_68(201500, -5000, 184020, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33500, 0)

    label("loc_51D2")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 6)), scpexpr(EXPR_END)), "loc_535D")
    SetMapObjFrame(0xE, "m01gim01", 0x2, "off")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "off")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5276")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_52F5")

    label("loc_5276")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52B8")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_52F5")

    label("loc_52B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52F5")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_52F5")

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
    Jump("loc_54D4")

    label("loc_535D")

    SetMapObjFrame(0xE, "m01gim01", 0x2, "on")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53F4")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_5473")

    label("loc_53F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5436")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_5473")

    label("loc_5436")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5473")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_5473")

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

    label("loc_54D4")

    Return()

    # Function_16_4FDF end

    def Function_17_54D5(): pass

    label("Function_17_54D5")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0143
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターの制御パネルがある。\x01",
            "操作しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_565F")
    Fade(500)
    SetChrPos(0x0, 600, 0, 600, 90)
    SetChrPos(0x1, 600, 0, -600, 90)
    SetChrPos(0x2, -600, 0, -600, 90)
    SetChrPos(0x3, -600, 0, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55BF")
    SetChrPos(0x4, -1800, 0, -600, 90)
    SetChrPos(0x5, -1800, 0, 600, 90)
    Jump("loc_55DE")

    label("loc_55BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55DE")
    SetChrPos(0x4, -1800, 0, 0, 90)

    label("loc_55DE")

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

    label("loc_565F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_54D5 end

    def Function_18_5667(): pass

    label("Function_18_5667")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_573A")
    OP_90(0x4, -1800, 0, -600, 90)
    OP_90(0x5, -1800, 0, 600, 90)
    Jump("loc_5759")

    label("loc_573A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5759")
    OP_90(0x4, -1800, 0, 0, 90)

    label("loc_5759")

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

    # Function_18_5667 end

    def Function_19_57AE(): pass

    label("Function_19_57AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_583E")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【中を覗いてみる】\x01",      # 0
            "【やめておく】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_581A"),
        (1, "loc_5837"),
        (SWITCH_DEFAULT, "loc_583C"),
    )


    label("loc_581A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x13, 0x10)
    OP_65(0x4, 0x1)
    Call(0, 23)
    Jump("loc_583C")

    label("loc_5837")

    Jump("loc_583C")

    label("loc_583C")

    EventEnd(0x3)

    label("loc_583E")

    Return()

    # Function_19_57AE end

    def Function_20_583F(): pass

    label("Function_20_583F")

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
    SetChrName("少年の声")

    #A0144
    AnonymousTalk(
        0xFF,
        "帝国方面の主要投資事業一覧……\x02",
    )

    CloseMessageWindow()

    #A0145
    AnonymousTalk(
        0xFF,
        "カルバード方面の各種相場一覧……\x02",
    )

    CloseMessageWindow()

    #A0146
    AnonymousTalk(
        0xFF,
        (
            "レミフェリア方面の\x01",
            "三大製薬会社の販売実績……\x02",
        )
    )

    CloseMessageWindow()

    #A0147
    AnonymousTalk(
        0xFF,
        (
            "リベール方面は……\x01",
            "新型導力機関#8Rオーバルエンジン#の納入先一覧か。\x02",
        )
    )

    CloseMessageWindow()

    #A0148
    AnonymousTalk(
        0xFF,
        (
            "さすがクロスベル。\x01",
            "一通りの情報は入ってくるな。\x02",
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
    SetChrName("ソバカス少年")

    #A0149
    AnonymousTalk(
        0xFF,
        (
            "へへ……大漁、大漁♪\x02\x03",

            "いやぁ、今回も\x01",
            "チョロイ仕事だったよなぁ。\x02\x03",

            "データベースを適当に漁ってれば\x01",
            "お客の欲しがるお宝情報をゲーット！\x02\x03",

            "まだセキュリティ意識が薄いから\x01",
            "今ならやりたい放題だもんなぁ。\x02\x03",

            "なんか人生ナメちゃいそーだぜ㈱\x02",
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
        "ソバカス少年",
        (
            "#5P#2310Fマズ……冷えたら\x01",
            "ピザなんて喰えたもんじゃないな。\x02\x03",

            "#2302Fやっぱりピザも情報も\x01",
            "熱いうちが一番ってことか。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)

    #N0151
    NpcTalk(
        0x8,
        "ソバカス少年",
        (
            "#5P#2304Fさーてと……\x01",
            "ここから先はプライベートだ。\x02\x03",

            "ＩＢＣの端末を攻略するか……\x01",
            "《仔猫#4Rキティ#》の正体を突き止めるか。\x02\x03",

            "#2302Fハッ……\x01",
            "なかなか楽しませてくれるじゃん。\x02",
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
        "ソバカス少年",
        "#6P#2305F導力メール……？\x02",
    )

    CloseMessageWindow()
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    FadeToDark(0, 0, -1)
    Sleep(500)
    SetChrName("ソバカス少年")

    #A0153
    AnonymousTalk(
        0xFF,
        (
            "#2301F『拝啓、ヨナ・セイクリッド殿……』\x02\x03",

            "『貴殿の腕を見込んで\x01",
            "  相談したき儀あり……』\x02\x03",

            "#2305Fへえ、出所はっと……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(849, 0, 100, 0)
    Sleep(800)
    SetChrName("ソバカス少年")

    #A0154
    AnonymousTalk(
        0xFF,
        (
            "#2301F……どこかの大型端末を\x01",
            "経由してじゃなさそうだ。\x02\x03",

            "港湾区のルーターより転送……\x02\x03",

            "#2305F#30W…………………………………………\x02\x03",

            "#40W……《黒月貿易公司》………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 21)
    SetChrName("ソバカス少年")

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
        "ソバカス少年",
        (
            "#6P#2304F……《銀#2Rイン#》か……\x02\x03",

            "#2302Fハハッ！\x01",
            "面白くなってきたじゃん。\x02",
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

    # Function_20_583F end

    def Function_21_6081(): pass

    label("Function_21_6081")

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

    # Function_21_6081 end

    def Function_22_60DD(): pass

    label("Function_22_60DD")

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
        "#0005F（この音楽は……）\x02",
    )

    CloseMessageWindow()
    OP_68(499600, 1000, 204800, 2000)
    OP_6F(0x1)

    def lambda_6209():
        OP_96(0xFE, 0x7A2B0, 0x0, 0x316A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6209)
    Sleep(50)

    def lambda_6226():
        OP_96(0xFE, 0x7A2B0, 0x0, 0x312B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6226)
    Sleep(50)

    def lambda_6243():
        OP_96(0xFE, 0x79D38, 0x0, 0x316A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6243)
    Sleep(50)

    def lambda_6260():
        OP_96(0xFE, 0x79D38, 0x0, 0x312B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6260)
    WaitChrThread(0x101, 1)

    def lambda_627E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_627E)
    WaitChrThread(0x102, 1)

    def lambda_628F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_628F)
    WaitChrThread(0x103, 1)

    def lambda_62A0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_62A0)
    WaitChrThread(0x104, 1)

    def lambda_62B1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_62B1)
    WaitChrThread(0x104, 2)

    #C0158
    ChrTalk(
        0x104,
        "#12P#0301F（どうやら誰かいるみてぇだな。）\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        (
            "#4P#0203F（おそらく『第８制御端末』は\x01",
            "  この先にあるのではないかと……）\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#4P#0101F（ということは……\x01",
            "  この先に《銀#2Rイン#》とハッカーが？）\x02",
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

    def lambda_63E1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_63E1)
    Sleep(50)

    def lambda_63F1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_63F1)
    Sleep(50)

    def lambda_6401():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6401)
    Sleep(300)

    #C0161
    ChrTalk(
        0x101,
        (
            "#0003F#5P（とにかく中を覗いてみよう……）\x02\x03",

            "#0001F（《銀》がいるかもしれないから\x01",
            "  みんな、気をつけてくれ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        "#4P#0101F（ええ……！）\x02",
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

    # Function_22_60DD end

    def Function_23_64C1(): pass

    label("Function_23_64C1")

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
    SetChrName("ソバカス少年")

    #A0163
    AnonymousTalk(
        0xFF,
        (
            "さ～てと。\x01",
            "今日も荒稼ぎするかね～。\x02\x03",

            "まずはラインフォルト社の\x01",
            "新型鉄道車両のスペック……\x02\x03",

            "それからヴェルヌ社の\x01",
            "高級スポーツ車のスペック……\x02\x03",

            "へえ、ＺＣＦでは新しい型の\x01",
            "定期飛行船を開発してんのか……\x02\x03",

            "オーバルギアの開発といい\x01",
            "あそこも相当飛ばしてるよなぁ。\x02",
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
        "#11P#0005F（……あれって……）\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        (
            "#0105F（どうやら《銀#2Rイン#》では\x01",
            "  無いみたいだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x104,
        "#4P#0301F（なんだぁ、あのガキは？）\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x103,
        "#12P#0206F（……やっぱり……）\x02",
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
        "ソバカス少年",
        (
            "#12P#2304Fしっかし、《銀》の旦那も\x01",
            "銀耀石#6Rアルジェム#の結晶とは気前がいいよな。\x02\x03",

            "このサイズだと、１万ミラくらいには\x01",
            "なるんじゃないかね～。\x02\x03",

            "#2302Fへへっ、明日あたりに\x01",
            "《ナインヴァリ》で換金するかね。\x02\x03",

            "ギヨームのオッサンの所で\x01",
            "新型のパーツも買っておきたいし。\x02",
        )
    )

    CloseMessageWindow()
    Sound(850, 0, 100, 0)
    Sleep(1000)

    #N0169
    NpcTalk(
        0x8,
        "ソバカス少年",
        (
            "#12P#2309Fハハ、それにしても\x01",
            "旦那も無駄なことするよな～。\x02\x03",

            "あんなメールを送ったところで\x01",
            "ここまで辿り着けるワケないじゃん。\x02\x03",

            "#2302Fこのヨナ様の足取りを追えるヤツなんて\x01",
            "ゼムリア大陸捜してもいないっつーの！\x02",
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
        "ロイドの声",
        "──それはどうかな。\x02",
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

    def lambda_6BA5():
        OP_96(0xFE, 0x79AE0, 0xC8, 0x49AE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6BA5)

    def lambda_6BBF():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6BBF)
    Sound(820, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)

    #N0171
    NpcTalk(
        0x8,
        "ソバカス少年",
        "#5P#2305Fなっ……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)

    #C0172
    ChrTalk(
        0x101,
        (
            "#0001F#6Pどうやら君が……\x01",
            "《ハッカー》みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        (
            "#4P#0301Fおいおい……\x01",
            "まだ本当にガキじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #N0174
    NpcTalk(
        0x8,
        "ソバカス少年",
        "#5P#2305Fな、なんだアンタら……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0175
    NpcTalk(
        0x8,
        "ソバカス少年",
        (
            "#5P#2307Fま、まさか《銀》の旦那が言ってた\x01",
            "『特務支援課』かよ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        "#0003F#6Pああ、その通りだ。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x102,
        (
            "#0101Fどうやら《銀》とは\x01",
            "本当に面識があるみたいね……\x02",
        )
    )

    CloseMessageWindow()

    #N0178
    NpcTalk(
        0x8,
        "ソバカス少年",
        (
            "#5P#2310Fい、いや、あり得るもんか！\x02\x03",

            "この天才ヨナ様の足跡を追って\x01",
            "ここまで辿り着けるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#12P#0206F……相変わらずですね。\x01",
            "ヨナ・セイクリッド。\x02",
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
            "#5P#2305Fティオ・プラトー！？\x02\x03",

            "ど、どうしてここに……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        (
            "#12P#0203Fそれはこちらの台詞です。\x02\x03",

            "#0211F財団を出奔#4Rしゅっぽん#したあなたが\x01",
            "どうしてこんな所に……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F02():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6F02)
    Sleep(50)

    def lambda_6F12():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6F12)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)
    Sleep(300)

    #C0182
    ChrTalk(
        0x101,
        "#5P#0011Fティオ、知り合いなのか？\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#12P#0203Fエプスタイン財団の\x01",
            "同じ研究所にいた事があります。\x02\x03",

            "#0200Fもっとも専門が違ったので\x01",
            "それほど親交はありませんでしたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x8,
        (
            "#5P#2310Fくそっ、そうか……\x02\x03",

            "アンタならあのモードを使えば\x01",
            "ボクの痕跡を追えるハズだよな……\x02\x03",

            "#2311Fああもう、分かってたら\x01",
            "もっと念入りに仕掛けたのにっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        (
            "#12P#0204F詰めが甘いですね、ヨナ。\x02\x03",

            "#0211Fそんな事だから、悪戯をして\x01",
            "財団に大損害を与えるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x8,
        "#5P#2301Fう、うっせーな。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x104,
        "#0305Fなんだぁ、その大損害ってのは？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0188
    ChrTalk(
        0x103,
        (
            "#6P#0206F彼は幼少から、財団の研究所で\x01",
            "システムエンジニアとしての\x01",
            "英才教育を受けていたのですが……\x02\x03",

            "悪戯がひどく、ある時、\x01",
            "研究成果の一つを台無しにして\x01",
            "大損害を出してしまったんです。\x02\x03",

            "#0211Fそして、それを怒られるのが嫌で\x01",
            "出奔してしまったらしくて……\x02",
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
        "#5P#0001Fな、なんだそりゃ……\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        (
            "#5P#0106Fふう……\x01",
            "どんな理由かと思えば。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        (
            "#0306Fやれやれ……\x01",
            "見たまんまのガキってわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        (
            "#5P#2310Fク、クソ……\x01",
            "言いたい放題言いやがって……\x02\x03",

            "#2307Fティオ・プラトー！\x01",
            "財団に告げ口したりすんなよ！？\x02\x03",

            "したらアンタの恥ずかしい秘密を\x01",
            "導力ネットにばらまいてやるからな！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x8, 500)
    Sleep(300)

    #C0193
    ChrTalk(
        0x103,
        (
            "#12P#0204Fどうぞご勝手に。\x02\x03",

            "#0202F別に、知られて恥ずかしい\x01",
            "秘密なんてありませんし……\x02\x03",

            "あったとしても、あなたに\x01",
            "掴まれるような隙は見せませんし。\x02\x03",

            "#0204Fネットにばらまかれたとしても\x01",
            "すぐに対処できるでしょうから。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x8,
        "#5P#2310Fく、くう～……！\x02",
    )

    CloseMessageWindow()

    def lambda_74B3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_74B3)
    Sleep(50)

    def lambda_74C3():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_74C3)
    Sleep(50)

    def lambda_74D3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_74D3)
    Sleep(300)

    #C0195
    ChrTalk(
        0x102,
        "#0102Fふふっ……\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x104,
        (
            "#4P#0304Fはは、ティオすけの方が\x01",
            "完全に役者が上みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#0001F#6Pそれで……ヨナと言ったな。\x02\x03",

            "君はどうしてここに？\x01",
            "一体、何をしているんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "#5P#2301Fっせえな、アンタに\x01",
            "そんなことを話す義理は──\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x103,
        (
            "#12P#0201F答えなさい、ヨナ。\x02\x03",

            "この場所に辿り着かれた時点で\x01",
            "ゲームはあなたの負けです。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x8,
        (
            "#5P#2310Fぐっ……分かったよ。\x02\x03",

            "#2306Fボクはな、今このクロスベルで\x01",
            "《情報屋》をやってるんだ。\x02",
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
        "#0005F#6P情報屋……？\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x104,
        (
            "#4P#0301Fおいおい……\x01",
            "ガキには似合わねぇ言葉だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x8,
        (
            "#5P#2304Fハッ、今時の情報屋は\x01",
            "年齢#4Rトシ#なんか関係ないつーの。\x02\x03",

            "#2302Fこのクロスベルには\x01",
            "とにかく色んな情報が集まってくる。\x02\x03",

            "帝国、共和国、リベール、レミフェリア、\x01",
            "レマンからアルテリアまで……\x02\x03",

            "それに加えて、色んな会社や\x01",
            "国際企業の支社なんかも多いしな。\x02\x03",

            "そういった所の情報が\x01",
            "導力ネットを通じて流れるんだよ。\x02\x03",

            "#2309Fまだセキュリティ意識も低いから\x01",
            "美味しい情報を喰い放題ってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x102,
        "#0105Fそ、それって……\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        "#0013F#6Pどう考えても違法じゃないのか？\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x103,
        (
            "#12P#0206Fいえ、まだ試行段階なので\x01",
            "取り締まる法律はありませんね。\x02\x03",

            "#0200Fいずれ法制化は\x01",
            "時間の問題かと思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x8,
        (
            "#5P#2304Fま、このクロスベルは\x01",
            "そこらへんも甘そうだしね～。\x02\x03",

            "財団のラボも飽き飽きしてたから\x01",
            "ここで《情報屋》を開いたってわけ。\x02\x03",

            "#2302Fへへ、お得意様もかなりいるし、\x01",
            "ガッポリ儲けさせてもらってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x104,
        (
            "#4P#0306Fやれやれ……\x01",
            "世の中舐めてやがんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x103,
        (
            "#12P#0204Fしかし、わたしが\x01",
            "クロスベル警察に出向してたのは\x01",
            "知らなかったみたいですし……\x02\x03",

            "#0202F少々、情報屋としては甘いのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x8,
        (
            "#5P#2306Fうぐっ……仕方ないだろ！\x02\x03",

            "#2310Fボクだってクロスベルの事を\x01",
            "全部は把握してねーんだし！\x02\x03",

            "《仔猫》の相手だってあるから\x01",
            "色々と忙しいんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x103,
        "#12P#0205F《仔猫#4Rキティ#》……？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "#5P#2305Fこ、こっちのことだっつーの。\x02\x03",

            "#2301F……って、まさか……\x01",
            "アンタが《仔猫》じゃないよな？\x02\x03",

            "いつクロスベルに来たんだよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        (
            "#12P#0206F質問の意味が分かりませんが……\x02\x03",

            "#0200Fわたしがクロスベルに来たのは\x01",
            "２ヶ月ほど前のことですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        (
            "#5P#2306Fだよな……\x01",
            "ハッキングのクセも全然違うし。\x02",
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
            "#0003F#6P話はよく分からないが……\x02\x03",

            "#0013Fそろそろ答えてもらおう。\x01",
            "《銀#2Rイン#》とはどういう関係だ？\x02",
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
            "#0001F#6Pあのメールを送ったのが\x01",
            "君なのは確かなんだろう？\x02\x03",

            "なぜ、あんなものを送った？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        "#5P#2304F……フン、まあいいか。\x02",
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

    def lambda_7E44():
        OP_96(0xFE, 0x79EC8, 0x0, 0x493E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7E44)
    WaitChrThread(0x8, 1)
    Sleep(300)

    #C0220
    ChrTalk(
        0x8,
        "#2300F#5Pほらよ、受け取りな。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x325),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x325, 1)
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
            "今こそ門は開かれた。\x01",
            "いざ《星の塔》に挑み、\x01",
            "我が望みを受け取るがよい。\x07\x00\x02",
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
        "#0005F#6Pこれは……！\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x102,
        "#0101F《銀》からの伝言……！？\x02",
    )

    CloseMessageWindow()

    def lambda_8037():
        OP_96(0xFE, 0x79BA8, 0xC8, 0x4982C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8037)
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
            "#5P#2300F《銀》の旦那からの依頼でね。\x02\x03",

            "アンタらにメールを送って\x01",
            "ここに辿り着けたらそのカードを\x01",
            "渡せって言われていたんだ。\x02\x03",

            "#2306F……まさか本当に\x01",
            "辿り着くとは思わなかったけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x104,
        (
            "#4P#0304Fフン、なるほどな。\x02\x03",

            "#0305Fそんじゃお前、《銀》ってのに\x01",
            "何度も会ったことがあんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "#5P#2300Fああ、お得意様の一人だぜ。\x02\x03",

            "たまにここに直接来ては\x01",
            "色々情報を買ってくれるんだ。\x02\x03",

            "#2306Fま、こんな変な依頼を\x01",
            "引き受けたのは初めてだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        "#0001F#6Pここに《銀》が……\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x103,
        "#12P#0201Fどういう人物なんですか？\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        (
            "#5P#2300Fいや、いつも黒衣をまとって\x01",
            "仮面を着けてるから知らねーし。\x02\x03",

            "#2302F何でも、カルバードの東方人街の\x01",
            "伝説の殺し屋なんだろ？\x02\x03",

            "#2309Fカッケーよな、クールだぜ！\x02",
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
        "#0011F#6Pクールって……\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x104,
        (
            "#4P#0306Fやれやれ……\x01",
            "恐いもの知らずな小僧だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x102,
        (
            "#0108Fでも、《銀》が私たちを\x01",
            "誘っているのは確かみたいね。\x02\x03",

            "#0101F何か話したいことが\x01",
            "あるような文面だったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        (
            "#5P#2300Fああ、そうみたいだぜ？\x02\x03",

            "何の用事かは知らないけど\x01",
            "アンタたちを試したいんだとさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#0013F#6Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x104,
        (
            "#4P#0302Fヘッ、ずいぶんと\x01",
            "ふざけた犯罪者じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x103,
        (
            "#6P#0201Fしかし、この《星の塔》というのは\x01",
            "何のことなんでしょうか……？\x02\x03",

            "何かの暗喩みたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        (
            "#0008F#5P《星の塔》……\x01",
            "どこかで聞いたことがあるような。\x02",
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
            "#0105Fもしかして……\x02\x03",

            "#0101Fクロスベルの郊外にある\x01",
            "《星見の塔》のことかしら。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8602():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8602)
    Sleep(50)

    def lambda_8612():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8612)
    Sleep(50)

    def lambda_8622():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8622)
    Sleep(200)

    #C0240
    ChrTalk(
        0x101,
        (
            "#5P#0005Fあ……\x02\x03",

            "#0001Fウルスラ間道の途中に見える\x01",
            "あの中世の塔のことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x104,
        (
            "#4P#0306Fおいおい、あんな所まで\x01",
            "俺らを呼び出そうってのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x102,
        (
            "#0103Fでも、他に手がかりはないわ。\x02\x03",

            "#0101Fここは行ってみるしか\x01",
            "ないんじゃないかしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        (
            "#5P#0004F──ああ、俺も賛成だ。\x02\x03",

            "#0000F準備をしたらすぐにでも\x01",
            "南口から出るとして……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8779():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8779)
    Sleep(50)

    def lambda_8789():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8789)

    def lambda_8796():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8796)
    Sleep(50)

    def lambda_87A6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_87A6)
    Sleep(300)

    #C0244
    ChrTalk(
        0x104,
        (
            "#4P#0301F……問題はこの小僧を\x01",
            "どうするってことかね。\x02",
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
            "#5P#2305Fな、なんだよ……\x01",
            "もうボクに用はないだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#0001F#6Pあのな……このジオフロントは\x01",
            "クロスベル市の施設だ。\x02\x03",

            "どう考えても不法占拠だろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x8,
        (
            "#5P#2310Fふ、ふん……使われてない場所を\x01",
            "有効活用して何が悪いってんだ。\x02\x03",

            "#2307Fそれに、ジオフロントを\x01",
            "勝手に利用しちゃいけませんって\x01",
            "法律は無いはずだぜ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x101,
        "#0003F#6Pそういうのを屁理屈って言うんだ。\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        (
            "#0106Fそれに、こんな場所で\x01",
            "暮らしていたら危ないでしょう？\x02\x03",

            "#0101F魔獣だって徘徊しているし、\x01",
            "食生活にも問題ありそうだし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(498400, 900, 300530, 1200)

    def lambda_8A15():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8A15)
    Sleep(200)

    def lambda_8A25():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8A25)
    Sleep(50)

    def lambda_8A35():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8A35)
    Sleep(50)

    def lambda_8A45():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8A45)
    OP_6F(0x1)

    #C0250
    ChrTalk(
        0x103,
        (
            "#11P#0211F……ですね。\x01",
            "宅配ピザの箱ばっかりですし。\x02\x03",

            "#0205Fというか、まさかここまで\x01",
            "運んでもらっているんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "#5P#2304Fんなわけねーじゃん。\x02\x03",

            "#2302Fゲートを出たあたりまで\x01",
            "いつも届けてもらってるんだ。\x02\x03",

            "それに、このすぐ先に、\x01",
            "出口近くに通じている\x01",
            "排気ダクトがあるからな。\x02\x03",

            "#2309Fそっちを使えば\x01",
            "安全に出られるってわけさ♪\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x104,
        (
            "#2P#0306Fダメだコイツ……\x01",
            "引きこもる気満々じゃねえか。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(499400, 900, 301200, 1000)

    def lambda_8BEC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8BEC)
    Sleep(50)

    def lambda_8BFC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8BFC)
    Sleep(50)

    def lambda_8C0C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8C0C)
    Sleep(50)
    OP_93(0x104, 0x10E, 0x190)
    OP_6F(0x1)

    #C0253
    ChrTalk(
        0x101,
        (
            "#0006F#6Pはあ、こっちも忙しいから\x01",
            "この場は見逃すけど……\x02\x03",

            "#0001Fあんまり悪さをしたり、\x01",
            "やり過ぎたりするんじゃないぞ？\x02\x03",

            "恨みを買って危ない目に\x01",
            "遭ったりするかもしれないんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        "#0106Fそうね……それも心配だわ。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        (
            "#5P#2304Fハッ、そんなヘマするかよ。\x02\x03",

            "#2302Fま、アンタらも\x01",
            "欲しい情報があったら来なよ。\x02\x03",

            "ただし、ボクは高いぜ？\x02\x03",

            "#2309F安月給の新米警察官なんかに\x01",
            "払えるとは思えないけどな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        "#0013F#6Pこいつ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(150)

    #C0257
    ChrTalk(
        0x103,
        (
            "#6P#0202Fまあまあ、ロイドさん。\x02\x03",

            "#0204Fいざとなれば、\x01",
            "わたしがここにハッキングして\x01",
            "必要な情報を貰えば済みますし。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0258
    ChrTalk(
        0x8,
        "#5P#4S#2310Fおい！？\x02",
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

    # Function_23_64C1 end

    def Function_24_8F35(): pass

    label("Function_24_8F35")


    def lambda_8F3A():
        OP_96(0xFE, 0x7A058, 0x0, 0x48FF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F3A)
    Sleep(400)

    def lambda_8F57():
        OP_96(0xFE, 0x7A440, 0x0, 0x49188, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8F57)
    Sleep(400)

    def lambda_8F74():
        OP_96(0xFE, 0x7A058, 0x0, 0x48AE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8F74)
    Sleep(400)

    def lambda_8F91():
        OP_96(0xFE, 0x7A5D0, 0x0, 0x48DA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8F91)
    WaitChrThread(0x101, 1)

    def lambda_8FAF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8FAF)
    WaitChrThread(0x102, 1)

    def lambda_8FC0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8FC0)
    WaitChrThread(0x103, 1)

    def lambda_8FD1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8FD1)
    WaitChrThread(0x104, 1)

    def lambda_8FE2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8FE2)
    WaitChrThread(0x104, 2)
    Return()

    # Function_24_8F35 end

    def Function_25_8FEF(): pass

    label("Function_25_8FEF")

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

    def lambda_90CE():
        OP_96(0xFE, 0x79AE0, 0xC8, 0x49AE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_90CE)

    def lambda_90E8():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_90E8)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)

    #C0259
    ChrTalk(
        0x8,
        "#2302Fお、よく来たじゃん。\x02",
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

    def lambda_91C6():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_91C6)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 3)

    #C0260
    ChrTalk(
        0x101,
        "#12P#0001Fよく来たじゃん、じゃないだろ。\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        (
            "#0200Fわたしの助けが欲しいそうですが\x01",
            "一体、どのような用件ですか？\x02",
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
            "いや～、実はさ。\x02\x03",

            "ハッキングの手伝いを\x01",
            "アンタにして欲しいんだよね。\x02",
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
        "#5P#0203F……帰ります。\x02",
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
            "#2307F#5Pちょ、ちょっと待ったぁ！\x02\x03",

            "どうしていきなり\x01",
            "帰ろうとするんだよっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        "#12P#0006Fそりゃ、当たり前だろ……\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        "#4P#0301Fったく、ふざけたガキだな。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x102,
        (
            "#0106Fいきなり犯罪を手伝えというのは\x01",
            "少し乱暴すぎると思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x8,
        (
            "#2301F#5Pだから別に、今のところは\x01",
            "犯罪じゃないんだってば！\x02\x03",

            "それに企業とかＩＢＣとかに\x01",
            "仕掛けるわけじゃねーっての！\x02\x03",

            "ちょっと厄介な相手の\x01",
            "尻尾を掴むってだけの話さ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x103, 0x8, 500)

    #C0269
    ChrTalk(
        0x103,
        "#0200F……厄介な相手？\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x8,
        (
            "#2302F#5Pおっ、喰い付いたな？\x02\x03",

            "#2303Fあのさ、とりあえず\x01",
            "話だけでも聞いてくんねーかな？\x02\x03",

            "#2300Fアンタも絶対に\x01",
            "興味がある話だと思うし。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x103,
        (
            "#0203F……分かりました。\x02\x03",

            "#0211Fただし、つまらない話だった場合、\x01",
            "少し痛い目に遭ってもらいます。\x02\x03",

            "『ポムっと！』で２０連鎖くらい\x01",
            "喰らってもらうとか。\x02",
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
            "#2306F#5P本当にやられたら屈辱的すぎるんで\x01",
            "マジでカンベンしてください……\x02",
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
        "#0205F《仔猫#4Rキティ#》……？\x02",
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
            "#6P#0001F可愛らしい名前だけど……\x01",
            "本当にそんなハッカーがいるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x8,
        (
            "#11P#2303Fハッ、嘘言っても仕方ねーだろ。\x02\x03",

            "#2301F初めてそいつと遭遇したのは\x01",
            "半年くらい前のことだったな……\x02\x03",

            "幾つかの会社にハッキングしてたら\x01",
            "突然、何者かに追跡#4Rトレース#されたんだ。\x02\x03",

            "#2306Fそん時は慌てて侵入経路を切断して\x01",
            "何とか逃げたんだけど……\x02\x03",

            "そん時に、こっちを小馬鹿にするように\x01",
            "《仔猫#4Rキティ#》って Ｈ Ｎ #7Rハンドルネーム#を\x01",
            "こっちに送りつけてきたんだ！\x02\x03",

            "#2310Fそれ以来、たまにこっちの仕事に\x01",
            "チョッカイかけて来るんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        "#6P#0006Fう、うーん……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x102,
        (
            "#6P#0101F聞いた話だと、ハッカーというのは\x01",
            "とても珍しい存在らしいけれど……\x02\x03",

            "本当に、あなた以外にも\x01",
            "そんな人がクロスベルにいるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x8,
        (
            "#11P#2303Fああ、ぜってー間違いないね！\x02\x03",

            "#2307Fそりゃあ、最初はボクだって\x01",
            "何かの間違いかと思ったぜ！\x02\x03",

            "ボクに匹敵する天才ハッカーが\x01",
            "この街に、もう一人いるなんてさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        (
            "#11P#0211F……匹敵するというより、\x01",
            "どう考えてもその《仔猫》の方が\x01",
            "腕は上だと思いますけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x8, 0x0, 0xF, 0x1F4, 0xBB8)
    Sleep(150)

    #C0280
    ChrTalk(
        0x8,
        "#11P#2310Fうぐっ……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        (
            "#11P#0204Fまあ、あなたの本来の専門は\x01",
            "システム言語の開発ですし……\x02\x03",

            "#0202Fハッキングで負けたからといって\x01",
            "あまり気落ちしなくていいかと。\x02",
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
            "#5P#2307F余計な慰めはいいんだよっ！\x02\x03",

            "#2310Fと、とにかくボクとしては\x01",
            "そいつに一矢報いてやりたいんだ！\x02\x03",

            "何とかアドレスを割り出して\x01",
            "アクセスポイントを掴んでやる！\x02\x03",

            "その手伝いを頼みたいんだよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x103,
        "#11P#0203Fふむ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0284
    ChrTalk(
        0x103,
        (
            "#11P#0201F……今日、《仔猫》がネットに\x01",
            "現れるという保証はあるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#5P#2304Fハッ、こっちもそれなりに\x01",
            "分析と対策をしてきてるんでね。\x02\x03",

            "#2302Fどうやら《仔猫》はいつも\x01",
            "ネットに張り付いているわけじゃ\x01",
            "ないみたいだが……\x02\x03",

            "ヤツが興味を持ちそうなネタを\x01",
            "ネットにバラ撒いておいたんだ。\x02\x03",

            "今までの傾向からいって\x01",
            "《仔猫》が現れる可能性は９０％。\x02\x03",

            "#2309Fこれを逃がす手はねーだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x103,
        (
            "#11P#0208Fなるほど……\x02\x03",

            "#0204F──となると\x01",
            "どちらか片方が囮役になって\x01",
            "《仔猫》をおびき寄せる……\x02\x03",

            "その間、もう片方が\x01",
            "別のアクセスポイントから\x01",
            "《仔猫》の侵入経路を割り出す……\x02\x03",

            "#0202Fそれを何度か繰り返して\x01",
            "《仔猫》を追い込んでいく……\x02\x03",

            "そういった段取りでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x8,
        (
            "#5P#2300Fヘッ、さすがだな。\x02\x03",

            "#2304Fアンタだったら、あのモードを使えば\x01",
            "《仔猫》の処理に追いつけるハズだ。\x02\x03",

            "ボクだって、色々準備はしてるから\x01",
            "スピードじゃ負けるつもりはないしな。\x02\x03",

            "#2302F２対１なら絶対に尻尾を掴めるはずだぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x103,
        "#11P#0203F──２つ、問題が。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x8,
        "#5P#2305Fへ……？\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x103,
        (
            "#11P#0201Fまず、ハッキングの支援をするのに\x01",
            "適当な端末が必要ということです。\x02\x03",

            "支援課の端末は\x01",
            "ハッキングのリスクを考えると\x01",
            "あまり使いたくありませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x8,
        (
            "#5P#2302Fだったら、丁度いい場所がある。\x02\x03",

            "ジオフロントＡ区画の下層に\x01",
            "『第３制御端末』ってのがあるんだ。\x02\x03",

            "こことはコアルーターが別だから\x01",
            "挟み撃ちにはうってつけのハズさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x103,
        (
            "#11P#0205Fなるほど……\x01",
            "都合が良さそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        "#6P#0012F（う、うーん。）\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        "#0301F（話がまるで分からねぇ。）\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x102,
        "#6P#0100F（さすがに専門的すぎるわね。）\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        (
            "#11P#0206Fただ、もう一つは──\x02\x03",

            "#0201Fこの忙しい時に、それなりの時間を\x01",
            "取られてしまうという事です。\x02",
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
        "#6P#0005Fそれは……\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        "#6P#0106F……ちょっと問題ね。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x104,
        (
            "#0306F昨日もレースかなんかで\x01",
            "午後の時間を使っちまったしな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0300
    ChrTalk(
        0x8,
        (
            "#11P#2307Fおいおい、そりゃないぜ！？\x02\x03",

            "支援要請だっけ？\x01",
            "それって別に、必ずやんなきゃ\x01",
            "いけないモンじゃないんだろ？\x02\x03",

            "見返りに情報も渡すんだから\x01",
            "付き合ってくれてもいいじゃん！？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#6P#0006Fでもなぁ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0302
    ChrTalk(
        0x103,
        (
            "#11P#0204F──ですから、この件は\x01",
            "わたし一人で引き受けます。\x02\x03",

            "#0202Fロイドさんたちはこのまま\x01",
            "支援業務を続けてください。\x02",
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
        "#6P#0005Fティオ……！？\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        "#6P#0101Fで、でも……\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        (
            "#11P#0202F役割分担するだけの話です。\x02\x03",

            "どの道、ハッキングになれば\x01",
            "わたし一人がいれば十分ですし。\x02\x03",

            "皆さんだって、わたし一人が抜けても\x01",
            "通常の支援業務に支障はないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#0301Fだが、そのもう一つの端末ってのは\x01",
            "駅前のジオフロントの奥にあるんだろ？\x02\x03",

            "さすがにちょいと危なくねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x103,
        (
            "#2P#0204Fまあ、何とかなるのではないかと。\x02\x03",

            "もうあそこの魔獣であれば\x01",
            "わたし一人でも対処できそうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x102,
        "#6P#0108Fティオちゃん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0309
    ChrTalk(
        0x101,
        (
            "#6P#0004F──なら、こうしよう。\x02\x03",

            "#0000F俺がティオに付き添うから\x01",
            "エリィとランディは警察本部の\x01",
            "手伝いに回ってくれないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0310
    ChrTalk(
        0x103,
        "#11P#0205Fえ……\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x104,
        (
            "#0300Fああ、いいんじゃねえか？\x02\x03",

            "さすがにティオすけ一人を\x01",
            "行かせるってのもアレだしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        (
            "#6P#0103Fそうね、私もそれは反対。\x02\x03",

            "#0100F本部も忙しいでしょうから\x01",
            "雑用は幾らでもあるでしょうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        "#11P#0208Fで、でも……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0314
    ChrTalk(
        0x8,
        (
            "#5P#2300Fいいじゃん別に。\x01",
            "遠慮することじゃねーだろ？\x02\x03",

            "アンタって、そういうのを\x01",
            "気にするようなタイプだったっけ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(150)

    #C0315
    ChrTalk(
        0x103,
        "#11P#0201F…………………（キッ）\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(800)
    OP_64(0x8)

    #C0316
    ChrTalk(
        0x8,
        "#5P#2305Fわわっ、なに怒ってんだよ～っ？\x02",
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
            "#11P#0202F……分かりました。\x02\x03",

            "その代わり、今日片付けたい用事は\x01",
            "今のうちに片付けてしまいましょう。\x02\x03",

            "多分、一度始めてしまったら\x01",
            "夕方くらいまで時間を取られそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        "#6P#0000Fああ、そうみたいだな。\x02",
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
            "【他の用事を片付ける】\x01",          # 0
            "【用事は一通り済んでいる】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AC7E"),
        (1, "loc_AE1A"),
        (SWITCH_DEFAULT, "loc_B139"),
    )


    label("loc_AC7E")

    SetChrSubChip(0x8, 0x0)
    Sleep(300)
    OP_29(0x45, 0x1, 0x1)

    #C0320
    ChrTalk(
        0x8,
        (
            "#11P#2302Fハッ、だったら\x01",
            "とっとと済ませてきなよ。\x02\x03",

            "それまでこっちは\x01",
            "セッティングをしとくからさ。\x02",
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
    Sleep(10)
    PlayBGM("ed7521", 0)
    EventEnd(0x5)
    Jump("loc_B139")

    label("loc_AE1A")

    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0321
    ChrTalk(
        0x8,
        (
            "#11P#2309Fよーし、だったら細かい\x01",
            "打ち合わせをしちまおうぜ！\x02",
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

    def lambda_AEB2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AEB2)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0322
    ChrTalk(
        0x102,
        (
            "#12P#0100Fじゃあ、私とランディは\x01",
            "警察本部の方に向かうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x104,
        (
            "#0300F#5Pロイド。\x01",
            "ティオすけの事は頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0324
    ChrTalk(
        0x101,
        (
            "#6P#0004Fああ、任せてくれ。\x02\x03",

            "#0000F……ランディは\x01",
            "仕事をサボったりするなよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x104,
        (
            "#0309F#5Pギクッ……\x01",
            "ははっ、そんな滅相もない。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x102,
        "#12P#0104Fまあ、私が一応監視してるから。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0327
    ChrTalk(
        0x102,
        "#6P#0102Fティオちゃん、頑張ってね。\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x103,
        "#0202F#11P……はい、エリィさんも。\x02",
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
    Jump("loc_B139")

    label("loc_B139")

    Return()

    # Function_25_8FEF end

    def Function_26_B13A(): pass

    label("Function_26_B13A")


    def lambda_B13F():
        OP_96(0xFE, 0x7A058, 0x0, 0x48FF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B13F)
    Sleep(400)

    def lambda_B15C():
        OP_96(0xFE, 0x7A440, 0x0, 0x49188, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B15C)
    Sleep(400)

    def lambda_B179():
        OP_96(0xFE, 0x7A120, 0x0, 0x48A80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B179)
    Sleep(400)

    def lambda_B196():
        OP_96(0xFE, 0x7A5D0, 0x0, 0x48DA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B196)
    WaitChrThread(0x103, 1)

    def lambda_B1B4():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B1B4)
    WaitChrThread(0x102, 1)

    def lambda_B1C5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B1C5)
    WaitChrThread(0x101, 1)

    def lambda_B1D6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B1D6)
    WaitChrThread(0x104, 1)

    def lambda_B1E7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B1E7)
    WaitChrThread(0x104, 2)
    Return()

    # Function_26_B13A end

    def Function_27_B1F4(): pass

    label("Function_27_B1F4")


    def lambda_B1F9():
        OP_95(0xFE, 499700, 0, 291700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B1F9)
    Sleep(500)
    SetChrSubChip(0x103, 0x1)
    WaitChrThread(0x102, 1)

    def lambda_B21E():
        OP_95(0xFE, 499700, 0, 287700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B21E)
    WaitChrThread(0x102, 1)
    Return()

    # Function_27_B1F4 end

    def Function_28_B238(): pass

    label("Function_28_B238")


    def lambda_B23D():
        OP_95(0xFE, 495400, 0, 295400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B23D)
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    WaitChrThread(0x104, 1)

    def lambda_B269():
        OP_95(0xFE, 499700, 0, 291700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B269)
    WaitChrThread(0x104, 1)

    def lambda_B287():
        OP_95(0xFE, 499700, 0, 287700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B287)
    WaitChrThread(0x104, 1)
    Return()

    # Function_28_B238 end

    def Function_29_B2A1(): pass

    label("Function_29_B2A1")

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
            "#2302F#5P──そんじゃ、向こうに到着したら\x01",
            "エニグマでこっちに連絡してくれよ。\x02\x03",

            "ミッションを開始すっからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x103,
        "#6P#0202F分かりました。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#12P#0006F……よく分からないけど\x01",
            "あまりやりすぎないでくれよ？\x02\x03",

            "#0001F導力ネットを利用している人に\x01",
            "迷惑をかけるのは駄目だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        (
            "#2303F#5Pハッ、言われるまでもねぇよ。\x02\x03",

            "#2300Fボクもティオも、多分《仔猫》も、\x01",
            "一般ユーザーに気付かれるような\x01",
            "素人くさいマネをするもんか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0333
    ChrTalk(
        0x103,
        (
            "#6P#0204Fネットという領域の水面下で\x01",
            "２対１の鬼ごっこをする……\x02\x03",

            "#0202Fそんな感じになるハズなので\x01",
            "心配はいらないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#12P#0000Fうーん……\x01",
            "まあ、それならいいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x8,
        (
            "#2309F#5Pそんじゃ、ヨロシク頼んだぜ～。\x02\x03",

            "#2302Fさーて、腹ごしらえに\x01",
            "ピザでも頼んでおこうかな～♪\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B5FD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B5FD)
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_B611():
        OP_95(0xFE, 499800, 15, 209700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B611)
    Sleep(100)

    def lambda_B62E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B62E)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_71(0x13, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x13)
    SetMapObjFlags(0x13, 0x10)
    OP_68(500550, 1000, 207480, 1000)

    def lambda_B67D():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B67D)
    Sleep(50)

    def lambda_B68D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B68D)
    OP_6F(0x1)

    #C0336
    ChrTalk(
        0x101,
        (
            "#0003F#11Pやれやれ……\x02\x03",

            "#0000Fそれじゃあ、ここを出て\x01",
            "クロスベル駅の方に向かおう。\x02\x03",

            "ジオフロントＡ区画の\x01",
            "奥にある場所だったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x103,
        (
            "#6P#0204Fはい、《第３制御端末》ですね。\x02\x03",

            "#0202F細かい位置については\x01",
            "到着した時に説明します。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        "#0000F了解、それじゃあ行こうか。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)

    def lambda_B7BB():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B7BB)
    Sleep(100)

    def lambda_B7CB():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B7CB)
    WaitChrThread(0x101, 2)

    def lambda_B7DC():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B7DC)
    WaitChrThread(0x103, 2)

    def lambda_B7F5():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B7F5)
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

    # Function_29_B2A1 end

    def Function_30_B82F(): pass

    label("Function_30_B82F")

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
        "#0205Fローゼンベルク工房……？\x02",
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
            "#0005F#5Pちょ、ちょっと待て。\x02\x03",

            "#0001Fローゼンベルク工房って\x01",
            "人形を作っている工房だろう？\x02\x03",

            "北の山道の途中にあった……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x8,
        (
            "#2306F#11Pそうだよ、その通りですよ！\x02\x03",

            "#2310Fでも《仔猫》のアドレスを解析したら\x01",
            "そこがアクセスポイントって出たんだ！\x02\x03",

            "ハッ！\x01",
            "何の冗談だよ、これは！？\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        "#6P#0208F確かに……不可解ですね。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0343
    ChrTalk(
        0x101,
        (
            "#0001F#5P……どういう事なんだ？\x02\x03",

            "あの工房に《仔猫》がいたら\x01",
            "何かおかしいことでもあるのか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(200)

    #C0344
    ChrTalk(
        0x103,
        (
            "#6P#0206Fその……\x02\x03",

            "#0201F現在、自治州内に敷かれている\x01",
            "《導力ネットワーク》網は\x01",
            "市内とウルスラ病院くらいなんです。\x02\x03",

            "あとは湖の対岸にある保養地、\x01",
            "ミシュラムくらいでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0345
    ChrTalk(
        0x101,
        "#0005F#5Pあ……\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x8,
        (
            "#2303F#11P……無線の導力波は不安定だから\x01",
            "普通の導力通信にしか使われない。\x02\x03",

            "大量の情報のやり取りをする\x01",
            "導力ネットは基本的に有線なんだ。\x02\x03",

            "#2310Fウルスラ病院とミシュラムだって\x01",
            "湖底に導力ケーブルが通ってるし……\x02\x03",

            "でもどう考えても、山道外れの工房に\x01",
            "導力ケーブルが敷かれてるワケがない！\x02\x03",

            "#2311Fああもう！\x01",
            "どういうトリックなんだよ～っ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0347
    ChrTalk(
        0x101,
        "#0003F#5Pうーん……\x02",
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
        "#0008F#5P（………まさかな……………）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0349
    ChrTalk(
        0x103,
        (
            "#6P#0203F──まあ、謎は残されましたが\x01",
            "収穫はあったみたいで何よりです。\x02\x03",

            "#0202Fそれでは報酬を頂きましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x8,
        (
            "#2306F#11Pはあ……分かったっつーの。\x02\x03",

            "アンタらの助けがなかったら\x01",
            "ここまで辿り着けなかったしな。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x330),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を入手した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x330, 1)
    Sleep(300)

    #C0352
    ChrTalk(
        0x101,
        (
            "#0001F#5Pこれが……\x01",
            "俺たちが興味を示す情報か。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x8,
        (
            "#2303F#11P……ぶっちゃけて言うと\x01",
            "《ルバーチェ》絡みの情報。\x02\x03",

            "#2300F関連情報もまとめといたから\x01",
            "アンタらには重宝すんじゃねーの？\x02",
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
        "#0005F#5Pそれは……\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x103,
        (
            "#6P#0201F……なるほど。\x01",
            "確かに一番知りたい情報ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        (
            "#2306F#11P言っとくけど、知ってるヤツなら\x01",
            "全部知ってるような情報ばかりだぜ？\x02\x03",

            "たとえば警察の上層部なんかは\x01",
            "とっくに掴んでるネタばかりだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x101,
        (
            "#0004F#5Pいや、助かるよ。\x02\x03",

            "#0000Fそういう情報が回ってこなくて\x01",
            "ちょっと困ってた所だったからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        "#2303F#11Pあっそ、よかったじゃん。\x02",
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
            "#2311F#11Pあ～もう……今日はもう寝る！\x02\x03",

            "また明日、さっきの手がかりを元に\x01",
            "《仔猫》の正体を迫ってやるからな～！\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x101,
        (
            "#0012Fはは、まあ程々にな。\x02\x03",

            "#0000Fせっかくの記念祭なんだから\x01",
            "引きこもってばかりいないで\x01",
            "デートでもしてきたらどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x8,
        (
            "#2310F#11Pう、うるせー。\x01",
            "余計なお世話だっつーの！\x02\x03",

            "この弟系草食男子を装った\x01",
            "喰いまくりのリア充野郎が！\x02",
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
            "#0013F#5P……意味不明だけど、\x01",
            "不当に中傷してるみたいだな？\x02",
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
            "#6P#0203Fそういえば……\x02\x03",

            "ロイドさん、記念祭の初日に\x01",
            "セシルさんとデートしてましたね。\x02",
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
        "#0005F#5Pへ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_C548")

    #C0365
    ChrTalk(
        0x103,
        (
            "#6P#0211Fその後も、ノエルさんたち姉妹と\x01",
            "両手に花で楽しく過ごしたとか……\x02\x03",

            "なるほど、経験者の\x01",
            "言葉には重みがありますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5C9")

    label("loc_C548")


    #C0366
    ChrTalk(
        0x103,
        (
            "#6P#0211Fその後も、ランディさんと一緒に\x01",
            "看護師さんたちと楽しく過ごしたとか。\x02\x03",

            "なるほど、経験者の\x01",
            "言葉には重みがありますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5C9")

    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0367
    ChrTalk(
        0x101,
        (
            "#0012F#5Pその、ティオさん。\x01",
            "何が仰りたいんでしょう……？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x103,
        "#6P#0204Fいえ、特に何も。\x02",
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

    # Function_30_B82F end

    def Function_31_C702(): pass

    label("Function_31_C702")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C71C")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x0, 0x2)
    Jump("Function_31_C702")

    label("loc_C71C")

    Return()

    # Function_31_C702 end

    def Function_32_C71D(): pass

    label("Function_32_C71D")

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

    # Function_32_C71D end

    def Function_33_C763(): pass

    label("Function_33_C763")

    EventBegin(0x1)

    #C0369
    ChrTalk(
        0x101,
        (
            "#0001F（そこの部屋に\x01",
            "  犯人がいるはずだ……）\x02\x03",

            "（とにかく中を覗いてみよう。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 502470, 0, 199800, 270)
    EventEnd(0x4)
    Return()

    # Function_33_C763 end

    SaveToFile()

Try(main)
