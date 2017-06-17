from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m0100.bin",                # FileName
        "m0100",                    # MapName
        "m0100",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 104, 0, 1, 0, 2],
    )

    BuildStringList((
        "m0100",                  # 0
        "地下空间管理员",         # 1
        "bm0101",                 # 2
        "bm0101",                 # 3
        "bm0101",                 # 4
        "bm0101",                 # 5
        "bm0100",                 # 6
        "bm0100",                 # 7
        "bm0100",                 # 8
        "bm0100",                 # 9
    ))

    ATBonus("ATBonus_2F4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_39C7", 8,   0,   12,  0,   0,   5,   7)
    Sepith("Sepith_39CF", 12,  1,   8,   0,   3,   7,   0)
    Sepith("Sepith_39D7", 0,   0,   0,   10,  7,   7,   7)
    Sepith("Sepith_39BF", 0,   12,  5,   0,   7,   2,   6)

    MonsterBattlePostion("MonsterBattlePostion_394", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_360", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_364", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_334", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_340", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 2, 13, 180)

    # monster count: 9

    BattleInfo(
        "BattleInfo_4BC", 0x0000, 18, 6, 60, 6, 1, 30, 0, "bm0101", "Sepith_39C7", 30, 45, 20, 5,
        (
            ("ms68700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_394", "MonsterBattlePostion_3D4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms68700.dat", "ms68700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_374", "MonsterBattlePostion_3D4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_394", "MonsterBattlePostion_3D4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms68700.dat", "ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, "MonsterBattlePostion_374", "MonsterBattlePostion_3D4", "ed7400", "ed7403", "ATBonus_2F4"),
        )
    )

    BattleInfo(
        "BattleInfo_8A4", 0x0000, 18, 6, 60, 6, 1, 25, 0, "bm0100", "Sepith_39CF", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_354", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_334", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_354", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_334", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
        )
    )

    BattleInfo(
        "BattleInfo_64C", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_39D7", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_394", "MonsterBattlePostion_3D4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_374", "MonsterBattlePostion_3D4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_394", "MonsterBattlePostion_3D4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_374", "MonsterBattlePostion_3D4", "ed7400", "ed7403", "ATBonus_2F4"),
        )
    )

    BattleInfo(
        "BattleInfo_714", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_39BF", 30, 45, 20, 5,
        (
            ("ms63800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_354", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms63800.dat", "ms63800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_334", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_354", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms63800.dat", "ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, "MonsterBattlePostion_334", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
        )
    )

    BattleInfo(
        "BattleInfo_7DC", 0x0000, 18, 6, 60, 6, 1, 30, 0, "bm0100", "Sepith_39C7", 30, 45, 20, 5,
        (
            ("ms68700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_354", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms68700.dat", "ms68700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_334", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_354", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms68700.dat", "ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, "MonsterBattlePostion_334", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
        )
    )

    BattleInfo(
        "BattleInfo_584", 0x0000, 18, 6, 60, 6, 1, 25, 0, "bm0101", "Sepith_39CF", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_394", "MonsterBattlePostion_3D4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_374", "MonsterBattlePostion_3D4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_394", "MonsterBattlePostion_3D4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_374", "MonsterBattlePostion_3D4", "ed7400", "ed7403", "ATBonus_2F4"),
        )
    )

    BattleInfo(
        "BattleInfo_96C", 0x0000, 18, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_39D7", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_354", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_334", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_354", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_334", "MonsterBattlePostion_3B4", "ed7400", "ed7403", "ATBonus_2F4"),
        )
    )

    AddCharChip((
        "chr/ch26000.itc",                   # 00
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
        "monster/ch63850.itc",               # 10
        "monster/ch63851.itc",               # 11
        "monster/ch68750.itc",               # 12
        "monster/ch68750.itc",               # 13
        "monster/ch75850.itc",               # 14
        "monster/ch75851.itc",               # 15
        "monster/ch60550.itc",               # 16
        "monster/ch60550.itc",               # 17
    ))

    DeclNpc(93000,   0,       3400,    225,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)

    DeclMonster(194920,  60,      0,       0x1010000,    "BattleInfo_4BC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(399500,  10,      0,       0x1010000,    "BattleInfo_8A4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(199710,  -100350, 0,       0x1010000,    "BattleInfo_64C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(199570,  -203180, 0,       0x1010000,    "BattleInfo_714", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(300340,  -100040, 4000,    0x1010000,    "BattleInfo_7DC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(214950,  -16210,  4000,    0x1010000,    "BattleInfo_584", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(199840,  -3150,   4000,    0x1010000,    "BattleInfo_64C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(199810,  199380,  0,       0x1010000,    "BattleInfo_714", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(299660,  303250,  0,       0x1010000,    "BattleInfo_96C", 0,   22,  0xFFFF, 6,  7)

    DeclActor(200000,  0,       -200000, 1200,    200000,  1000,    -200000, 0x007C, 0,  4,  0x0000)
    DeclActor(300000,  0,       300000,  1200,    300000,  1000,    300000,  0x007C, 0,  5,  0x0000)
    DeclActor(0,       0,       102000,  1200,    0,       1000,    102500,  0x007C, 0,  10, 0x0000)
    DeclActor(100000,  0,       202000,  1200,    100000,  1000,    202500,  0x007C, 0,  12, 0x0000)
    DeclActor(402000,  0,       200000,  1200,    402500,  1000,    200000,  0x007C, 0,  14, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7

    ScpFunction((
        "Function_0_AD8",          # 00, 0
        "Function_1_B90",          # 01, 1
        "Function_2_C82",          # 02, 2
        "Function_3_1255",         # 03, 3
        "Function_4_134F",         # 04, 4
        "Function_5_1485",         # 05, 5
        "Function_6_15BB",         # 06, 6
        "Function_7_189C",         # 07, 7
        "Function_8_2213",         # 08, 8
        "Function_9_2D35",         # 09, 9
        "Function_10_2D50",        # 0A, 10
        "Function_11_2ED4",        # 0B, 11
        "Function_12_301B",        # 0C, 12
        "Function_13_319F",        # 0D, 13
        "Function_14_32E6",        # 0E, 14
        "Function_15_346A",        # 0F, 15
        "Function_16_35B1",        # 10, 16
    ))


    def Function_0_AD8(): pass

    label("Function_0_AD8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_B18"),
        (1, "loc_B24"),
        (2, "loc_B30"),
        (3, "loc_B3C"),
        (4, "loc_B48"),
        (5, "loc_B54"),
        (6, "loc_B60"),
        (SWITCH_DEFAULT, "loc_B6C"),
    )


    label("loc_B18")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_B78")

    label("loc_B24")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_B78")

    label("loc_B30")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_B78")

    label("loc_B3C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_B78")

    label("loc_B48")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_B78")

    label("loc_B54")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_B78")

    label("loc_B60")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B78")

    label("loc_B6C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B78")

    label("loc_B78")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B8F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B78")

    label("loc_B8F")

    Return()

    # Function_0_AD8 end

    def Function_1_B90(): pass

    label("Function_1_B90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF6")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBD")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)
    Jump("loc_BF6")

    label("loc_BBD")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDC")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_BF6")

    label("loc_BDC")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF6")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)

    label("loc_BF6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C10")
    Event(0, 16)

    label("loc_C10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C2D")
    OP_C7(0x0, 0x1000)

    label("loc_C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_C81")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C50")
    Jump("loc_C81")

    label("loc_C50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_C66")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_C81")

    label("loc_C66")

    SetChrPos(0x8, 89500, 0, 6000, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x80)

    label("loc_C81")

    Return()

    # Function_1_B90 end

    def Function_2_C82(): pass

    label("Function_2_C82")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C96")
    VolumeBGM(0x64, 0x64)

    label("loc_C96")

    SetMapObjFrame(0xF, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0x10, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up_kp")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_CE4")
    ClearMapObjFlags(0x14, 0x10)
    OP_70(0x14, 0x1E)
    Jump("loc_CEA")

    label("loc_CE4")

    ClearMapObjFlags(0x14, 0x10)

    label("loc_CEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D09")
    OP_10(0x1E, 0x0)
    OP_10(0x28, 0x1)
    OP_10(0x1F, 0x0)
    OP_10(0x29, 0x1)
    Jump("loc_D15")

    label("loc_D09")

    OP_10(0x1E, 0x1)
    OP_10(0x28, 0x0)
    OP_10(0x1F, 0x1)
    OP_10(0x29, 0x0)

    label("loc_D15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D64")
    Sound(122, 1, 100, 0)
    Jump("loc_D67")

    label("loc_D64")

    OP_24(0x7A)

    label("loc_D67")

    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_EB2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_DDF")
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x1, "light00", 0x1, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jump("loc_E1F")

    label("loc_DDF")

    SetMapObjFrame(0x1, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x1, "light00", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x1, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57, 7)), scpexpr(EXPR_END)), "loc_E6D")
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x2, "light00", 0x1, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jump("loc_EAD")

    label("loc_E6D")

    SetMapObjFrame(0x2, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x2, "light00", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x2, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_EAD")

    Jump("loc_F32")

    label("loc_EB2")

    SetMapObjFrame(0x1, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x1, "light00", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x1, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    SetMapObjFrame(0x2, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x2, "light00", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x2, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_F32")

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
    SetMapObjFrame(0xE, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xE, "light01", 0x0, 0x1)
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1201")
    OP_70(0x12, 0x0)
    Jump("loc_1205")

    label("loc_1201")

    OP_70(0x12, 0x1E)

    label("loc_1205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1218")
    OP_70(0x13, 0x0)
    Jump("loc_121C")

    label("loc_1218")

    OP_70(0x13, 0x1E)

    label("loc_121C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1251")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_1251")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_123F")
    Jump("loc_1251")

    label("loc_123F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_1251")
    OP_1B(0x7, 0x0, 0x8)

    label("loc_1251")

    Call(0, 3)
    Return()

    # Function_2_C82 end

    def Function_3_1255(): pass

    label("Function_3_1255")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129B")
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    Jump("loc_12AA")

    label("loc_129B")

    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)

    label("loc_12AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CB")
    SetChrFlags(0xA, 0x8)
    Jump("loc_12D0")

    label("loc_12CB")

    ClearChrFlags(0xA, 0x8)

    label("loc_12D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12FA")
    SetChrFlags(0xB, 0x8)
    Jump("loc_12FF")

    label("loc_12FA")

    ClearChrFlags(0xB, 0x8)

    label("loc_12FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1320")
    SetChrFlags(0xD, 0x8)
    Jump("loc_1325")

    label("loc_1320")

    ClearChrFlags(0xD, 0x8)

    label("loc_1325")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1343")
    SetChrFlags(0xC, 0x8)
    SetMapObjFlags(0x12, 0x4)
    Jump("loc_134E")

    label("loc_1343")

    ClearChrFlags(0xC, 0x8)
    ClearMapObjFlags(0x12, 0x4)

    label("loc_134E")

    Return()

    # Function_3_1255 end

    def Function_4_134F(): pass

    label("Function_4_134F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143C")
    Sound(14, 0, 100, 0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('Ｕ材料', 1)"), scpexpr(EXPR_END)), "loc_13CE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1437")

    label("loc_13CE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x12, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1437")

    Jump("loc_1479")

    label("loc_143C")

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

    label("loc_1479")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_134F end

    def Function_5_1485(): pass

    label("Function_5_1485")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1572")
    Sound(14, 0, 100, 0)
    OP_71(0x13, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅰ', 1)"), scpexpr(EXPR_END)), "loc_1504")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅰ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10C, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_156D")

    label("loc_1504")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅰ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅰ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x13, 0x1E, 0x0, 0x0, 0x0)

    label("loc_156D")

    Jump("loc_15AF")

    label("loc_1572")

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

    label("loc_15AF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1485 end

    def Function_6_15BB(): pass

    label("Function_6_15BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_176D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_166E")

    #C0007
    ChrTalk(
        0x8,
        (
            "供水管道的管理是在Ｂ区域进行的，\x01",
            "另外此处还集中有净水设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "如果Ｂ区域发生了异常状况，\x01",
            "城市机能将有可能陷入瘫痪……\x01",
            "请查明发生异常的原因！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1768")

    label("loc_166E")


    #C0009
    ChrTalk(
        0x8,
        (
            "地下空间根据各自机能的不同，\x01",
            "被划分为四个区域。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "例如，Ａ区域负责控制\x01",
            "所有的排气、换气工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "Ｂ区域负责供水管道的管理\x01",
            "以及净水设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "如果Ｂ区域发生了异常状况，\x01",
            "城市机能将有可能陷入瘫痪……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "请各位务必查明\x01",
            "发生异常的原因！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1768")

    Jump("loc_1898")

    label("loc_176D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1781")
    Call(0, 7)
    Jump("loc_1898")

    label("loc_1781")


    #C0014
    ChrTalk(
        0x8,
        (
            "真头疼啊……\x01",
            "在这种时候，协会的游击士\x01",
            "却全部出去执行任务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "虽然也向警察局那边\x01",
            "发送了支援请求……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "唉，但不知道他们\x01",
            "能否注意到呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1898")

    #C0017
    ChrTalk(
        0x101,
        (
            "#0005F（向警察局发出了请求……\x01",
            "  莫非是发给我们了吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        (
            "#0200F（看来还是去检查一下\x01",
            "  支援科的终端为好吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1898")

    TalkEnd(0xFE)
    Return()

    # Function_6_15BB end

    def Function_7_189C(): pass

    label("Function_7_189C")

    EventBegin(0x0)
    Fade(500)
    OP_68(91900, 1500, 1520, 0)
    MoveCamera(4, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22740, 0)
    SetChrPos(0x101, 91970, 0, 1640, 45)
    SetChrPos(0x102, 91120, 0, 1980, 45)
    SetChrPos(0x103, 91050, 0, 720, 45)
    SetChrPos(0x104, 90040, 0, 940, 45)
    OP_93(0x8, 0xE1, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0019
    ChrTalk(
        0x8,
        "#11P莫非，你们就是……！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#12P#0000F克洛斯贝尔警察局·特别任务支援科。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        (
            "#6P#0200FＢ区域的下层部分\x01",
            "发生了异常事态吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "#11P正是……\x01",
            "那里的情况变得很奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#11P遍布在地下的供水管道似乎\x01",
            "出现了局部断水的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0024
    ChrTalk(
        0x101,
        "#12P#0005F哎！？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        "#5P#0105F这究竟是为什么……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#11P因为目前只有一部分管道出现了\x01",
            "这种情况，所以市民们还没有察觉到……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#11P但再这样下去的话，恐怕\x01",
            "市内各处都会开始断水了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "#11P希望各位能尽快展开调查。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#12P#0003F明、明白了。\x02\x03",

            "#0001F下层区域，也就是……\x01",
            "平时无法进入的地方对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#11P嗯，那里有个上锁的大门。\x01",
            "我现在就去解锁，\x01",
            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(90000, 1200, 6500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x8, 90000, 150, 7250, 0)
    SetChrPos(0x101, 90500, 0, 5750, 0)
    SetChrPos(0x102, 89500, 0, 5500, 0)
    SetChrPos(0x103, 90500, 0, 4250, 0)
    SetChrPos(0x104, 89500, 0, 4000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x1, "light00", 0x1, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Sound(72, 0, 100, 0)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0031
    ChrTalk(
        0x8,
        (
            "#5P乘坐这扇门后的升降机，\x01",
            "就可以降至下层区域了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "#5P看起来，异常状况似乎是\x01",
            "发生在下层区域的最深处……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#5P我想情况大概会很棘手，\x01",
            "但还是希望各位能去确认一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#11P#0000F明白了。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#12P#0203F……那个，\x01",
            "请稍等。\x02\x03",

            "#0200F如果要去下层区域的最深处，\x01",
            "从那边的大门过去会比较快吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_68(110000, 1500, 6500, 3000)
    OP_6F(0x79)

    #C0036
    ChrTalk(
        0x104,
        (
            "#2P#0305F莫非那里有可以\x01",
            "直接通往最下层的升降机吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        (
            "#2P#0100F说起来，其它区域\x01",
            "好像也都是相同的构造呢……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(90000, 1200, 6500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    OP_0D()

    #C0038
    ChrTalk(
        0x8,
        (
            "#5P……确实，从那边可以直接\x01",
            "下降至下层区域的最深处。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#5P但我之前去确认过一次，\x01",
            "不知为什么，升降机没有\x01",
            "从下面升上来。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#5P导力还在正常运作，\x01",
            "看起来好像也没有什么故障……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        "#12P#0200F嗯，很奇怪呢。\x02",
    )

    CloseMessageWindow()

    def lambda_1FCA():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FCA)
    Sleep(50)

    def lambda_1FDA():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FDA)
    Sleep(50)

    def lambda_1FEA():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1FEA)
    Sleep(50)

    def lambda_1FFA():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1FFA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0042
    ChrTalk(
        0x101,
        (
            "#11P#0003F……看起来，这应该\x01",
            "也是异常事态之一呢。\x02\x03",

            "#0001F总之，我们就从这边\x01",
            "前往下层区域吧。\x02\x03",

            "其内部似乎相当广阔，\x01",
            "尽量先做好充足的准备吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        (
            "#6P#0101F是啊……\x01",
            "不过我们还要去医院，\x01",
            "并没有太多的时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#12P#0300F那么，做好准备之后，\x01",
            "就赶快前往地下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【地下空间的异变调查】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(90000, 1000, 5750, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33000, 0)
    SetChrPos(0x0, 90000, 0, 5750, 0)
    SetChrPos(0x1, 90000, 0, 5750, 0)
    SetChrPos(0x2, 90000, 0, 5750, 0)
    SetChrPos(0x3, 90000, 0, 5750, 0)
    SetChrPos(0x8, 93000, 0, 3400, 225)
    OP_29(0x34, 0x1, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_7_189C end

    def Function_8_2213(): pass

    label("Function_8_2213")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    LoadChrToIndex("apl/ch50544.itc", 0x1E)
    OP_68(109900, 1150, 8000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 109400, 1500, 9250, 180)
    SetChrPos(0x102, 110400, 1500, 9500, 180)
    SetChrPos(0x103, 109400, 1500, 10750, 180)
    SetChrPos(0x104, 110400, 1500, 11000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x2, "light00", 0x1, 0x1)
    Sound(72, 0, 100, 0)
    Sleep(500)
    OP_71(0x2, 0x1, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x2)
    OP_68(109900, 1150, 3000, 3000)

    def lambda_233F():
        OP_97(0x101, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_233F)

    def lambda_2359():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2359)
    Sleep(50)

    def lambda_236D():
        OP_97(0x102, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_236D)

    def lambda_2387():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2387)
    Sleep(50)

    def lambda_239B():
        OP_97(0x103, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_239B)

    def lambda_23B5():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_23B5)
    Sleep(50)

    def lambda_23C9():
        OP_97(0x104, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23C9)

    def lambda_23E3():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_23E3)
    Sleep(2000)
    Fade(500)
    OP_68(93000, 1150, 3400, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    OP_93(0x8, 0x5A, 0x1F4)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_97(0x8, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)

    def lambda_2461():
        OP_97(0x8, 0x2710, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2461)
    Sleep(1000)
    Fade(500)
    OP_68(109620, 1150, 2220, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    EndChrThread(0x8, 0x1)
    SetChrPos(0x8, 104900, 0, 500, 180)

    def lambda_24C6():

        label("loc_24C6")

        TurnDirection(0x101, 0x8, 0)
        Yield()
        Jump("loc_24C6")

    QueueWorkItem2(0x101, 1, lambda_24C6)

    def lambda_24D8():

        label("loc_24D8")

        TurnDirection(0x102, 0x8, 0)
        Yield()
        Jump("loc_24D8")

    QueueWorkItem2(0x102, 1, lambda_24D8)

    def lambda_24EA():

        label("loc_24EA")

        TurnDirection(0x103, 0x8, 0)
        Yield()
        Jump("loc_24EA")

    QueueWorkItem2(0x103, 1, lambda_24EA)

    def lambda_24FC():

        label("loc_24FC")

        TurnDirection(0x104, 0x8, 0)
        Yield()
        Jump("loc_24FC")

    QueueWorkItem2(0x104, 1, lambda_24FC)

    def lambda_250E():
        OP_97(0x8, 0x1388, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_250E)
    OP_0D()
    OP_71(0x2, 0xA, 0x1, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x0, 0x1F4)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)

    #C0046
    ChrTalk(
        0x8,
        "#12P你们……！？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "#12P为什么会从这边……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#12P莫非……升降机\x01",
            "已经可以使用了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#5P#0003F嗯，总之，先让\x01",
            "我们做个大致报告吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(109940, 1150, 560, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 109400, 1500, 2250, 180)
    SetChrPos(0x102, 110400, 1500, 2500, 180)
    SetChrPos(0x103, 109400, 1500, 3750, 180)
    SetChrPos(0x104, 110400, 1500, 4000, 180)
    TurnDirection(0x101, 0x104, 0)
    TurnDirection(0x102, 0x103, 0)
    TurnDirection(0x103, 0x102, 0)
    TurnDirection(0x104, 0x101, 0)
    SetChrPos(0x8, 109900, 0, 500, 180)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0050
    ChrTalk(
        0x8,
        "#12P嗯嗯、嗯嗯……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#12P原来是这样啊！\x01",
            "既然如此，就可以暂时安心了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#12P明白了，\x01",
            "我也马上回去。\x02",
        )
    )

    CloseMessageWindow()
    Sound(807, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_68(109620, 1150, 2220, 2000)
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_2758():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2758)
    Sleep(50)

    def lambda_2768():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2768)
    Sleep(50)

    def lambda_2778():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2778)
    Sleep(50)

    def lambda_2788():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2788)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0053
    ChrTalk(
        0x101,
        "#5P#0000F已经没问题了吗？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#12P嗯，供水管道好像已经\x01",
            "完全恢复原状了。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#12P谢谢啊！\x01",
            "多亏你们几个了。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        (
            "#11P#0100F哪里，毕竟这也是\x01",
            "我们的分内之事……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#5P#0304F哎，只要顺利恢复原状就好。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#12P是啊，我当时还在想，\x01",
            "到底该怎么办才好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#12P不过，真是没想到啊，\x01",
            "区区魔兽居然能让这\x01",
            "地下空间的机能瘫痪。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "#12P看来，今后也有必要考虑\x01",
            "一些相应对策了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#5P#0001F……是啊。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        "#5P#0203F………………………………\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#12P算了，不管怎么说，\x01",
            "大家真是辛苦了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "#12P因为还有一些恢复工作要去做，\x01",
            "我就先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        "#11P#0100F您辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        "#5P#0300F慢走～\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    BeginChrThread(0x101, 1, 0, 9)
    BeginChrThread(0x102, 1, 0, 9)
    BeginChrThread(0x103, 1, 0, 9)
    BeginChrThread(0x104, 1, 0, 9)
    OP_97(0x8, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_68(109900, 1150, 3000, 1000)

    def lambda_2A94():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A94)
    Sleep(50)

    def lambda_2AA4():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2AA4)
    Sleep(50)

    def lambda_2AB4():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2AB4)
    Sleep(50)

    def lambda_2AC4():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2AC4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0067
    ChrTalk(
        0x101,
        (
            "#12P#0003F……无论怎么想，\x01",
            "我都不认为那是普通的魔兽。\x02\x03",

            "#0001F说实话，本来是想和游击士\x01",
            "协会那边商讨一下的，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#11P#0103F黑手党，还有失踪者……\x01",
            "我们目前还是应该优先处理那边的事情呢。\x02\x03",

            "#0101F总之，都已经耽误这么多时间了，\x01",
            "我们就赶快向乌尔斯拉医院出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#5P#0301F是啊，再磨磨蹭蹭，\x01",
            "太阳都该下山了。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x103,
        "#6P#0203F……是啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【地下空间的异变调查】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_37()
    OP_68(109900, 1000, 3200, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33000, 0)
    SetChrPos(0x0, 109900, 0, 3200, 180)
    SetChrPos(0x1, 109900, 0, 3200, 180)
    SetChrPos(0x2, 109900, 0, 3200, 180)
    SetChrPos(0x3, 109900, 0, 3200, 180)
    SetScenarioFlags(0x57, 7)
    OP_29(0x34, 0x1, 0x3)
    OP_29(0x34, 0x4, 0x10)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_8_2213 end

    def Function_9_2D35(): pass

    label("Function_9_2D35")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D4F")
    TurnDirection(0xFE, 0x8, 500)
    Sleep(200)
    Jump("Function_9_2D35")

    label("loc_2D4F")

    Return()

    # Function_9_2D35 end

    def Function_10_2D50(): pass

    label("Function_10_2D50")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0072
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ECC")
    Fade(500)
    SetChrPos(0x0, 600, 0, 100600, 0)
    SetChrPos(0x1, -600, 0, 100600, 0)
    SetChrPos(0x2, -600, 0, 99400, 0)
    SetChrPos(0x3, 600, 0, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E2A")
    SetChrPos(0x4, -600, 0, 98200, 0)
    SetChrPos(0x5, 600, 0, 98200, 0)
    Jump("loc_2E49")

    label("loc_2E2A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E49")
    SetChrPos(0x4, 0, 0, 98200, 0)

    label("loc_2E49")

    OP_68(0, 1000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(0, -4000, 100000, 2000)
    SetMapObjFrame(0xF, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0110", 0, 0, 0)
    IdleLoop()

    label("loc_2ECC")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_2D50 end

    def Function_11_2ED4(): pass

    label("Function_11_2ED4")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xF, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(0, -4000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, -10000, 100600, 0)
    OP_90(0x1, -600, -10000, 100600, 0)
    OP_90(0x2, -600, -10000, 99400, 0)
    OP_90(0x3, 600, -10000, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FA9")
    OP_90(0x4, -600, -10000, 98200, 0)
    OP_90(0x5, 600, -10000, 98200, 0)
    Jump("loc_2FC8")

    label("loc_2FA9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FC8")
    OP_90(0x4, 0, -10000, 98200, 0)

    label("loc_2FC8")

    Sound(145, 0, 100, 0)
    OP_68(0, 1000, 100000, 3000)
    SetMapObjFrame(0xF, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xF)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_2ED4 end

    def Function_12_301B(): pass

    label("Function_12_301B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0073
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3197")
    Fade(500)
    SetChrPos(0x0, 100600, 0, 200600, 0)
    SetChrPos(0x1, 99400, 0, 200600, 0)
    SetChrPos(0x2, 99400, 0, 199400, 0)
    SetChrPos(0x3, 100600, 0, 199400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30F5")
    SetChrPos(0x4, 99400, 0, 198200, 0)
    SetChrPos(0x5, 100600, 0, 198200, 0)
    Jump("loc_3114")

    label("loc_30F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3114")
    SetChrPos(0x4, 100000, 0, 198200, 0)

    label("loc_3114")

    OP_68(100000, 1000, 200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(100000, -4000, 200000, 2000)
    SetMapObjFrame(0x10, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0113", 0, 0, 0)
    IdleLoop()

    label("loc_3197")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_301B end

    def Function_13_319F(): pass

    label("Function_13_319F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0x10, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(100000, -4000, 200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 100600, -10000, 200600, 0)
    OP_90(0x1, 99400, -10000, 200600, 0)
    OP_90(0x2, 99400, -10000, 199400, 0)
    OP_90(0x3, 100600, -10000, 199400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3274")
    OP_90(0x4, 99400, -10000, 198200, 0)
    OP_90(0x5, 100600, -10000, 198200, 0)
    Jump("loc_3293")

    label("loc_3274")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3293")
    OP_90(0x4, 100000, -10000, 198200, 0)

    label("loc_3293")

    Sound(145, 0, 100, 0)
    OP_68(100000, 1000, 200000, 3000)
    SetMapObjFrame(0x10, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x10)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_319F end

    def Function_14_32E6(): pass

    label("Function_14_32E6")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0074
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3462")
    Fade(500)
    SetChrPos(0x0, 400600, 0, 200600, 90)
    SetChrPos(0x1, 400600, 0, 199400, 90)
    SetChrPos(0x2, 399400, 0, 199400, 90)
    SetChrPos(0x3, 399400, 0, 200600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33C0")
    SetChrPos(0x4, 398200, 0, 199400, 90)
    SetChrPos(0x5, 398200, 0, 200600, 90)
    Jump("loc_33DF")

    label("loc_33C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33DF")
    SetChrPos(0x4, 398200, 0, 200000, 90)

    label("loc_33DF")

    OP_68(400000, 1000, 200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(400000, -4000, 200000, 2000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0101", 0, 0, 0)
    IdleLoop()

    label("loc_3462")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_32E6 end

    def Function_15_346A(): pass

    label("Function_15_346A")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(400000, -4000, 200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 400600, -10000, 200600, 90)
    OP_90(0x1, 400600, -10000, 199400, 90)
    OP_90(0x2, 399400, -10000, 199400, 90)
    OP_90(0x3, 399400, -10000, 200600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_353F")
    OP_90(0x4, 398200, 0, 199400, 90)
    OP_90(0x5, 398200, 0, 200600, 90)
    Jump("loc_355E")

    label("loc_353F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_355E")
    OP_90(0x4, 398200, 0, 200000, 90)

    label("loc_355E")

    Sound(145, 0, 100, 0)
    OP_68(400000, 1000, 200000, 3000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x11)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_346A end

    def Function_16_35B1(): pass

    label("Function_16_35B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(110000, 500, 1500, 0)
    MoveCamera(60, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 84500, 0, -200, 90)
    SetChrPos(0x102, 84500, 0, 300, 90)
    SetChrPos(0x103, 84500, 0, -200, 90)
    SetChrPos(0x104, 84500, 0, 300, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_68(95000, 500, 1500, 8000)
    SetCameraDistance(25000, 8000)
    FadeToBright(1000, 0)
    Sleep(5000)

    def lambda_3692():
        OP_96(0xFE, 0x15888, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3692)

    def lambda_36AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36AC)
    Sleep(500)

    def lambda_36C0():
        OP_96(0xFE, 0x15888, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36C0)

    def lambda_36DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_36DA)
    Sleep(500)

    def lambda_36EE():
        OP_96(0xFE, 0x15374, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_36EE)

    def lambda_3708():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3708)
    Sleep(500)

    def lambda_371C():
        OP_96(0xFE, 0x15374, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_371C)

    def lambda_3736():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3736)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)
    Sleep(500)
    Fade(500)
    OP_68(88130, 1000, 160, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    OP_0D()

    #C0075
    ChrTalk(
        0x101,
        (
            "#0001F#6P这就是地下空间的Ｂ区域啊。\x02\x03",

            "单从外观来看，好像\x01",
            "和Ａ区域没什么不同呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x103,
        (
            "#6P#0203F根据数据库中的资料，\x01",
            "这里似乎是管理着克洛斯贝尔市\x01",
            "的供水管道设施的一角。\x02\x03",

            "#0200F犯人使用的『第８控制终端』\x01",
            "应该就在上层的某个地方。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3878():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3878)
    Sleep(50)

    def lambda_3888():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3888)
    Sleep(50)

    def lambda_3898():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3898)
    Sleep(50)

    def lambda_38A8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_38A8)
    Sleep(300)

    #C0077
    ChrTalk(
        0x102,
        (
            "#5P#0106F从邮件的内容来看……\x02\x03",

            "#0101F对方很可能就在那里\x01",
            "等着我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        (
            "#5P#0303F到底是有话要说，\x01",
            "还是有什么陷阱……\x02\x03",

            "#0301F总之，还是小心为好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#0013F#11P嗯……小心慎重地前进吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 87000, 0, 0, 90)
    SetScenarioFlags(0x83, 3)
    OP_29(0x43, 0x1, 0x6)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_16_35B1 end

    SaveToFile()

Try(main)
