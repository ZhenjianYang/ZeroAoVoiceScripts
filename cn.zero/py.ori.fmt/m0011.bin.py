from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m0011.bin",                # FileName
        "m0011",                    # MapName
        "m0011",                    # Location
        0x0067,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 103, 0, 2, 0, 3],
    )

    BuildStringList((
        "m0011",                  # 0
        "勇猛·小鼠",             # 1
        "MapThread",              # 2
        "bm0011",                 # 3
        "bm0011",                 # 4
        "bm0011",                 # 5
        "bm0011",                 # 6
        "bm0010",                 # 7
        "bm0010",                 # 8
        "bm0010",                 # 9
        "bm0010",                 # 10
        "bm0013",                 # 11
        "bm0013",                 # 12
        "bm0013",                 # 13
        "bm0013",                 # 14
        "bm0010",                 # 15
    ))

    ATBonus("ATBonus_3FC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2A23", 14,  2,   10,  8,   2,   2,   0)
    Sepith("Sepith_2A13", 4,   10,  14,  5,   2,   0,   2)
    Sepith("Sepith_2A2B", 0,   0,   0,   14,  8,   8,   8)
    Sepith("Sepith_2A1B", 7,   14,  6,   4,   0,   3,   3)

    MonsterBattlePostion("MonsterBattlePostion_49C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4C4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_4C8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4CC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4D0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4D4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_47C", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_48C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_4E8", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_4EC", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_4F0", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_4F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 2, 13, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_8A4", 0x0000, 22, 6, 45, 4, 1, 25, 0, "bm0010", "Sepith_2A23", 60, 30, 10, 0,
        (
            ("ms60400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms60400.dat", "ms60400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_47C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms60400.dat", "ms60400.dat", "ms60400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_808", 0x0000, 22, 6, 45, 4, 1, 30, 0, "bm0010", "Sepith_2A13", 60, 30, 10, 0,
        (
            ("ms62000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms62000.dat", "ms62000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_47C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms62000.dat", "ms62000.dat", "ms62000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_940", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0010", "Sepith_2A2B", 60, 30, 10, 0,
        (
            ("ms75500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms75500.dat", "ms75500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_47C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms75500.dat", "ms75500.dat", "ms75500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4FC", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0011", "Sepith_2A1B", 60, 30, 10, 0,
        (
            ("ms69000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4DC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms69000.dat", "ms69000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_47C", "MonsterBattlePostion_4DC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms69000.dat", "ms75500.dat", "ms69000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4DC", "ed7400", "ed7403", "ATBonus_3FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_634", 0x0000, 22, 6, 45, 4, 1, 25, 0, "bm0011", "Sepith_2A23", 60, 30, 10, 0,
        (
            ("ms60400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4DC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms60400.dat", "ms60400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_47C", "MonsterBattlePostion_4DC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms60400.dat", "ms62000.dat", "ms60400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4DC", "ed7400", "ed7403", "ATBonus_3FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BB0", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0013", "Sepith_2A2B", 60, 30, 10, 0,
        (
            ("ms75500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms75500.dat", "ms75500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_47C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms75500.dat", "ms75500.dat", "ms75500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9DC", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0013", "Sepith_2A1B", 60, 30, 10, 0,
        (
            ("ms69000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms69000.dat", "ms69000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_47C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms69000.dat", "ms69000.dat", "ms69000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4BC", "ed7400", "ed7403", "ATBonus_3FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_598", 0x0000, 22, 6, 45, 4, 1, 30, 0, "bm0011", "Sepith_2A13", 60, 30, 10, 0,
        (
            ("ms62000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4DC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms62000.dat", "ms62000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_47C", "MonsterBattlePostion_4DC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms62000.dat", "ms69000.dat", "ms62000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4DC", "ed7400", "ed7403", "ATBonus_3FC"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6D0", 0x0000, 22, 6, 45, 4, 1, 40, 0, "bm0011", "Sepith_2A2B", 60, 30, 10, 0,
        (
            ("ms75500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4DC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms75500.dat", "ms75500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_47C", "MonsterBattlePostion_4DC", "ed7400", "ed7403", "ATBonus_3FC"),
            ("ms75500.dat", "ms60400.dat", "ms75500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_49C", "MonsterBattlePostion_4DC", "ed7400", "ed7403", "ATBonus_3FC"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_C4C", 0x0000, 22, 6, 45, 0, 1, 0, 0, "bm0010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms69000.dat", "ms69000.dat", "ms69000.dat", "ms69000.dat", "ms69000.dat", "ms69000.dat", 0, 0, "MonsterBattlePostion_43C", "MonsterBattlePostion_4BC", "ed7401", "ed7403", "ATBonus_3FC"),
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
        "monster/ch69050.itc",               # 10
        "monster/ch69051.itc",               # 11
        "monster/ch62050.itc",               # 12
        "monster/ch62051.itc",               # 13
        "monster/ch60450.itc",               # 14
        "monster/ch60450.itc",               # 15
        "monster/ch75550.itc",               # 16
        "monster/ch75550.itc",               # 17
    ))

    DeclNpc(200000,  500,     100000,  0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(99930,   -420,    0,       0x1010000,    "BattleInfo_8A4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-197640, 202000,  0,       0x1010000,    "BattleInfo_808", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-203290, 199810,  0,       0x1010000,    "BattleInfo_940", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-200400, 291320,  200,     0x1010000,    "BattleInfo_4FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-200400, 318920,  0,       0x1010000,    "BattleInfo_634", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-200860, 399310,  0,       0x1010000,    "BattleInfo_808", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-95630,  499590,  0,       0x1010000,    "BattleInfo_BB0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-104600, 495420,  0,       0x1010000,    "BattleInfo_BB0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(103410,  499680,  0,       0x1010000,    "BattleInfo_9DC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(197670,  402040,  0,       0x1010000,    "BattleInfo_808", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(199560,  307890,  200,     0x1010000,    "BattleInfo_598", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(199500,  290930,  200,     0x1010000,    "BattleInfo_6D0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(199840,  200050,  0,       0x1010000,    "BattleInfo_8A4", 0,   20,  0xFFFF, 4,  5)

    DeclActor(100000,  0,       5000,    1200,    100000,  1000,    5000,    0x007C, 0,  5,  0x0000)
    DeclActor(-100000, 0,       500000,  1200,    -100000, 1000,    500000,  0x007C, 0,  6,  0x0000)
    DeclActor(200000,  0,       100000,  1200,    200000,  1000,    100000,  0x007C, 0,  7,  0x0000)
    DeclActor(2000,    0,       0,       1200,    2500,    1000,    0,       0x007C, 0,  8,  0x0000)
    DeclActor(0,       0,       602000,  1200,    0,       1000,    602500,  0x007C, 0,  10, 0x0000)
    DeclActor(2600,    0,       92500,   2000,    2600,    1000,    92500,   0x007C, 0,  12, 0x0000)
    DeclActor(-197300, 0,       301000,  2000,    -197300, 1000,    301000,  0x007C, 0,  13, 0x0000)
    DeclActor(202800,  0,       315860,  2000,    202800,  1000,    315860,  0x007C, 0,  14, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_D30",          # 00, 0
        "Function_1_D4D",          # 01, 1
        "Function_2_D78",          # 02, 2
        "Function_3_DDA",          # 03, 3
        "Function_4_16A2",         # 04, 4
        "Function_5_17C2",         # 05, 5
        "Function_6_18F8",         # 06, 6
        "Function_7_1A2E",         # 07, 7
        "Function_8_1C28",         # 08, 8
        "Function_9_1DAA",         # 09, 9
        "Function_10_1EF1",        # 0A, 10
        "Function_11_2073",        # 0B, 11
        "Function_12_21BA",        # 0C, 12
        "Function_13_2324",        # 0D, 13
        "Function_14_24A7",        # 0E, 14
        "Function_15_2622",        # 0F, 15
    ))


    def Function_0_D30(): pass

    label("Function_0_D30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D4C")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_D30")

    label("loc_D4C")

    Return()

    # Function_0_D30 end

    def Function_1_D4D(): pass

    label("Function_1_D4D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D6F")
    Sound(148, 0, 100, 0)
    Sleep(900)
    Jump("loc_D72")

    label("loc_D6F")

    Sleep(30)

    label("loc_D72")

    Jump("Function_1_D4D")

    label("loc_D77")

    Return()

    # Function_1_D4D end

    def Function_2_D78(): pass

    label("Function_2_D78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBF")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA5")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)
    Jump("loc_DBF")

    label("loc_DA5")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBF")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)

    label("loc_DBF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD9")
    Event(0, 15)

    label("loc_DD9")

    Return()

    # Function_2_D78 end

    def Function_3_DDA(): pass

    label("Function_3_DDA")

    ClearScenarioFlags(0x0, 0)
    BeginChrThread(0x9, 0, 0, 1)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 0, 0, 94000, 4000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 2)), scpexpr(EXPR_END)), "loc_E39")
    SetBarrier(0x2, 0x0, 0x1)
    SetMapObjFrame(0xA, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xD, "m00gim01", 0x2, "stop_kp")
    Jump("loc_E7C")

    label("loc_E39")

    SetBarrier(0x3, 0x0, 0x1)
    SetMapObjFrame(0xA, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xD, "m00gim01", 0x2, "rotate")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E7C")
    SetScenarioFlags(0x0, 0)

    label("loc_E7C")

    SetBarrier(0x0, 0x1, 0x1, 0x0, -200000, 0, 285500, 4000, 2000, 0)
    SetBarrier(0x0, 0x2, 0x1, 0x0, -200000, 0, 297500, 4000, 2000, 0)
    SetBarrier(0x0, 0x3, 0x1, 0x0, -200000, 0, 302500, 4000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 3)), scpexpr(EXPR_END)), "loc_F28")
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetMapObjFrame(0xB, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xE, "m00gim01", 0x2, "stop_kp")
    SetMapObjFrame(0xF, "m00gim01", 0x2, "stop_kp")
    Jump("loc_F98")

    label("loc_F28")

    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetMapObjFrame(0xB, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xE, "m00gim01", 0x2, "rotate")
    SetMapObjFrame(0xF, "m00gim01", 0x2, "rotate")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x86), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F98")
    SetScenarioFlags(0x0, 0)

    label("loc_F98")

    SetBarrier(0x0, 0x4, 0x1, 0x0, 200000, 0, 314000, 4000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 4)), scpexpr(EXPR_END)), "loc_1002")
    SetBarrier(0x2, 0x4, 0x1)
    SetMapObjFrame(0xC, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0x10, "m00gim01", 0x2, "stop_kp")
    SetMapObjFrame(0x11, "m00gim01", 0x2, "stop_kp")
    Jump("loc_1058")

    label("loc_1002")

    SetBarrier(0x3, 0x4, 0x1)
    SetMapObjFrame(0xC, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0x10, "m00gim01", 0x2, "rotate")
    SetMapObjFrame(0x11, "m00gim01", 0x2, "rotate")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1058")
    SetScenarioFlags(0x0, 0)

    label("loc_1058")

    SetMapObjFrame(0x8, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0x9, "m00ele00", 0x2, "down_kp")
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
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166C")
    OP_70(0x12, 0x0)
    Jump("loc_1670")

    label("loc_166C")

    OP_70(0x12, 0x1E)

    label("loc_1670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1683")
    OP_70(0x13, 0x0)
    Jump("loc_1687")

    label("loc_1683")

    OP_70(0x13, 0x1E)

    label("loc_1687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169A")
    OP_70(0x14, 0x0)
    Jump("loc_169E")

    label("loc_169A")

    OP_70(0x14, 0x1E)

    label("loc_169E")

    Call(0, 4)
    Return()

    # Function_3_DDA end

    def Function_4_16A2(): pass

    label("Function_4_16A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16C8")
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    Jump("loc_16D2")

    label("loc_16C8")

    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)

    label("loc_16D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x86), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1705")
    SetChrFlags(0xE, 0x8)
    Jump("loc_170A")

    label("loc_1705")

    ClearChrFlags(0xE, 0x8)

    label("loc_170A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_172B")
    SetChrFlags(0x12, 0x8)
    Jump("loc_1730")

    label("loc_172B")

    ClearChrFlags(0x12, 0x8)

    label("loc_1730")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7B), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1751")
    SetChrFlags(0x13, 0x8)
    Jump("loc_1756")

    label("loc_1751")

    ClearChrFlags(0x13, 0x8)

    label("loc_1756")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7E), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1777")
    SetChrFlags(0x14, 0x8)
    Jump("loc_177C")

    label("loc_1777")

    ClearChrFlags(0x14, 0x8)

    label("loc_177C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7F), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_179D")
    SetChrFlags(0x16, 0x8)
    Jump("loc_17A2")

    label("loc_179D")

    ClearChrFlags(0x16, 0x8)

    label("loc_17A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17BB")
    SetMapObjFlags(0x12, 0x4)
    Jump("loc_17C1")

    label("loc_17BB")

    ClearMapObjFlags(0x12, 0x4)

    label("loc_17C1")

    Return()

    # Function_4_16A2 end

    def Function_5_17C2(): pass

    label("Function_5_17C2")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18AF")
    Sound(14, 0, 100, 0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1841")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10B, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_18AA")

    label("loc_1841")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x12, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18AA")

    Jump("loc_18EC")

    label("loc_18AF")

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

    label("loc_18EC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_17C2 end

    def Function_6_18F8(): pass

    label("Function_6_18F8")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E5")
    Sound(14, 0, 100, 0)
    OP_71(0x13, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x649, 1)"), scpexpr(EXPR_END)), "loc_1977")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x649),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10B, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_19E0")

    label("loc_1977")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x649),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x649),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x13, 0x1E, 0x0, 0x0, 0x0)

    label("loc_19E0")

    Jump("loc_1A22")

    label("loc_19E5")

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

    label("loc_1A22")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_18F8 end

    def Function_7_1A2E(): pass

    label("Function_7_1A2E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BEA")
    Sound(14, 0, 100, 0)
    OP_71(0x14, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B27")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1A87():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A87)

    def lambda_1AA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1AA1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0007
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
    Battle("BattleInfo_C4C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1B08"),
        (2, "loc_1B17"),
        (1, "loc_1B24"),
        (SWITCH_DEFAULT, "loc_1B27"),
    )


    label("loc_1B08")

    SetScenarioFlags(0x75, 2)
    OP_70(0x14, 0x1E)
    Sleep(500)
    Jump("loc_1B27")

    label("loc_1B17")

    OP_70(0x14, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1B24")

    OP_B7(0x0)
    Return()

    label("loc_1B27")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x7E, 1)"), scpexpr(EXPR_END)), "loc_1B7E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10B, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1BE5")

    label("loc_1B7E")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x14, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1BE5")

    Jump("loc_1C1C")

    label("loc_1BEA")

    FadeToDark(300, 0, 100)

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

    label("loc_1C1C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1A2E end

    def Function_8_1C28(): pass

    label("Function_8_1C28")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0011
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA2")
    Fade(500)
    SetChrPos(0x0, 600, 0, -600, 90)
    SetChrPos(0x1, 600, 0, 600, 90)
    SetChrPos(0x2, -600, 0, -600, 90)
    SetChrPos(0x3, -600, 0, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D02")
    SetChrPos(0x4, -1800, 0, -600, 90)
    SetChrPos(0x5, -1800, 0, 600, 90)
    Jump("loc_1D21")

    label("loc_1D02")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D21")
    SetChrPos(0x4, -1800, 0, 0, 90)

    label("loc_1D21")

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
    SetMapObjFrame(0x8, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0010", 0, 0, 0)
    IdleLoop()

    label("loc_1DA2")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1C28 end

    def Function_9_1DAA(): pass

    label("Function_9_1DAA")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x8, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, -600, 90)
    OP_90(0x1, 600, 30000, 600, 90)
    OP_90(0x2, -600, 30000, -600, 90)
    OP_90(0x3, -600, 30000, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E7D")
    OP_90(0x4, -1800, 30000, -600, 90)
    OP_90(0x5, -1800, 30000, 600, 90)
    Jump("loc_1E9C")

    label("loc_1E7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E9C")
    OP_90(0x4, -1800, 30000, 0, 90)

    label("loc_1E9C")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, 0, 3000)
    SetMapObjFrame(0x8, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x8)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1DAA end

    def Function_10_1EF1(): pass

    label("Function_10_1EF1")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0012
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206B")
    Fade(500)
    SetChrPos(0x0, -600, 0, 600600, 0)
    SetChrPos(0x1, 600, 0, 600600, 0)
    SetChrPos(0x2, -600, 0, 599400, 0)
    SetChrPos(0x3, 600, 0, 599400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FCB")
    SetChrPos(0x4, -600, 0, 598200, 0)
    SetChrPos(0x5, 600, 0, 598200, 0)
    Jump("loc_1FEA")

    label("loc_1FCB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FEA")
    SetChrPos(0x4, 0, 0, 598200, 0)

    label("loc_1FEA")

    OP_68(600, 1000, 600000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(600, 6000, 600000, 3000)
    SetMapObjFrame(0x9, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0000", 0, 0, 0)
    IdleLoop()

    label("loc_206B")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1EF1 end

    def Function_11_2073(): pass

    label("Function_11_2073")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x9, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, 600000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, -600, 30000, 600600, 0)
    OP_90(0x1, 600, 30000, 600600, 0)
    OP_90(0x2, -600, 30000, 599400, 0)
    OP_90(0x3, 600, 30000, 599400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2146")
    OP_90(0x4, -600, 30000, 598200, 0)
    OP_90(0x5, 600, 30000, 598200, 0)
    Jump("loc_2165")

    label("loc_2146")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2165")
    OP_90(0x4, 0, 30000, 598200, 0)

    label("loc_2165")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, 600000, 3000)
    SetMapObjFrame(0x9, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x9)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_2073 end

    def Function_12_21BA(): pass

    label("Function_12_21BA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 2)), scpexpr(EXPR_END)), "loc_21F7")
    TalkBegin(0xFF)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "换气扇已经停止了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_2323")

    label("loc_21F7")

    EventBegin(0x1)

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有换气扇的控制装置。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_231C")
    Fade(500)
    SetChrPos(0x0, 980, 0, 91450, 45)
    SetChrPos(0x1, 390, 0, 89020, 0)
    SetChrPos(0x2, -1310, 0, 89020, 0)
    SetChrPos(0x3, -540, 0, 87480, 0)
    OP_68(-280, 1000, 93440, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    OP_0D()
    SetMapObjFrame(0xA, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1500)
    OP_93(0x0, 0x0, 0x1F4)
    Sleep(500)
    Fade(500)
    SetMapObjFrame(0xD, "m00gim01", 0x2, "stop")
    Sound(149, 0, 100, 0)
    ClearScenarioFlags(0x0, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    OP_0D()
    SetBarrier(0x2, 0x0, 0x1)
    SetScenarioFlags(0x54, 2)

    label("loc_231C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_2323")

    Return()

    # Function_12_21BA end

    def Function_13_2324(): pass

    label("Function_13_2324")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 3)), scpexpr(EXPR_END)), "loc_2361")
    TalkBegin(0xFF)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "换气扇已经停止了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_24A6")

    label("loc_2361")

    EventBegin(0x1)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有换气扇的控制装置。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249F")
    Fade(500)
    SetChrPos(0x0, -198980, 0, 299900, 45)
    SetChrPos(0x1, -200000, 0, 300540, 90)
    SetChrPos(0x2, -199850, 0, 298750, 90)
    SetChrPos(0x3, -201540, 0, 299290, 90)
    OP_68(-200710, 1000, 297410, 0)
    MoveCamera(45, 37, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(28500, 0)
    OP_0D()
    SetMapObjFrame(0xB, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1500)
    OP_93(0x0, 0x0, 0x1F4)
    Sleep(500)
    Fade(500)
    SetMapObjFrame(0xE, "m00gim01", 0x2, "stop")
    SetMapObjFrame(0xF, "m00gim01", 0x2, "stop")
    Sound(149, 0, 100, 0)
    ClearScenarioFlags(0x0, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    OP_0D()
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetScenarioFlags(0x54, 3)

    label("loc_249F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_24A6")

    Return()

    # Function_13_2324 end

    def Function_14_24A7(): pass

    label("Function_14_24A7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 4)), scpexpr(EXPR_END)), "loc_24E4")
    TalkBegin(0xFF)
    SetChrName("")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "换气扇已经停止了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_2621")

    label("loc_24E4")

    EventBegin(0x1)

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有换气扇的控制装置。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_261A")
    Fade(500)
    SetChrPos(0x0, 200990, 0, 315630, 90)
    SetChrPos(0x1, 200590, 0, 317000, 180)
    SetChrPos(0x2, 199210, 0, 317000, 180)
    SetChrPos(0x3, 199790, 0, 318370, 180)
    OP_68(198870, 1200, 309960, 0)
    MoveCamera(45, 36, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(24000, 0)
    OP_0D()
    SetMapObjFrame(0xC, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1500)
    OP_93(0x0, 0xB4, 0x1F4)
    Sleep(500)
    Fade(500)
    SetMapObjFrame(0x10, "m00gim01", 0x2, "stop")
    SetMapObjFrame(0x11, "m00gim01", 0x2, "stop")
    Sound(149, 0, 100, 0)
    ClearScenarioFlags(0x0, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    OP_0D()
    SetBarrier(0x2, 0x4, 0x1)
    SetScenarioFlags(0x54, 4)

    label("loc_261A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_2621")

    Return()

    # Function_14_24A7 end

    def Function_15_2622(): pass

    label("Function_15_2622")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(0, 1100, 86000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -300, 150, 84000, 0)
    SetChrPos(0x103, 300, 150, 84000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_26A7():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0x14FF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26A7)

    def lambda_26C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26C1)
    Sleep(400)

    def lambda_26D5():
        OP_96(0xFE, 0x258, 0x0, 0x14FF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_26D5)

    def lambda_26EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_26EF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, -500, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    MoveCamera(65, 40, 0, 4000)
    SetCameraDistance(19500, 4000)
    Sleep(3700)

    def lambda_2788():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0x15F90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2788)
    Sleep(50)

    def lambda_27A5():
        OP_96(0xFE, 0x258, 0x0, 0x15F90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27A5)
    OP_6F(0x50)
    Fade(500)
    OP_68(0, 1000, 92000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    #C0019
    ChrTalk(
        0x101,
        "#12P#0011F这、这是什么……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#0200F给地下空间换气用的\x01",
            "巨大换气扇。\x02\x03",

            "好像只有遇到灾害或紧急状况\x01",
            "的时候才会运转……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧操作了便携式终端。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Sound(849, 0, 100, 0)
    Sleep(1000)

    #C0022
    ChrTalk(
        0x103,
        (
            "#0203F……查到了过去的事例。\x02\x03",

            "#0201F看起来，它们之所以会开始运转，\x01",
            "很有可能是因为控制失灵。\x02\x03",

            "好像还有其它几台也是如此。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0023
    ChrTalk(
        0x101,
        (
            "#6P#0003F是吗……\x02\x03",

            "#0001F这样的话，还是\x01",
            "逐个去将它们停下比较好吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x2D, 0x1F4)

    #C0024
    ChrTalk(
        0x103,
        (
            "#0202F嗯，\x01",
            "可以用那边的装置来操作。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 89000, 0)
    SetScenarioFlags(0xA1, 1)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_15_2622 end

    SaveToFile()

Try(main)
