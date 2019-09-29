from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r0100.bin",                # FileName
        "r0100",                    # MapName
        "r0100",                    # Location
        0x0061,                     # MapIndex
        "ed7201",
        0x00000000,                 # Flags
        ("r0100", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 97, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0100",                  # 0
        "魔兽",                   # 1
        "魔兽",                   # 2
        "魔兽",                   # 3
        "魔兽",                   # 4
        "魔兽",                   # 5
        "br0100",                 # 6
        "br0100",                 # 7
        "br0100",                 # 8
        "br0100",                 # 9
        "br0100",                 # 10
        "br0100",                 # 11
        "克洛斯贝尔市·唐古拉姆门方向",# 12
        "阿尔摩利卡村方向",       # 13
    ))

    ATBonus("ATBonus_548", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2C5D", 0,   2,   0,   7,   3,   5,   0)
    Sepith("Sepith_2C55", 3,   0,   7,   0,   2,   1,   4)
    Sepith("Sepith_2C4D", 6,   3,   0,   0,   4,   3,   1)
    Sepith("Sepith_2C6D", 2,   0,   7,   1,   4,   2,   1)
    Sepith("Sepith_2C75", 34,  15,  25,  15,  0,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_5A8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_608", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_60C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_610", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_614", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_618", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_61C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_620", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_624", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_588", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_58C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_590", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 2, 13, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_628", 0x0000, 10, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_2C5D", 30, 45, 25, 0,
        (
            ("ms63900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A8", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            ("ms63900.dat", "ms63900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            ("ms63900.dat", "ms62600.dat", "ms63900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A8", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6C4", 0x0000, 10, 6, 45, 6, 1, 50, 0, "br0100", "Sepith_2C55", 30, 45, 25, 0,
        (
            ("ms62600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A8", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            ("ms62600.dat", "ms62600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            ("ms62600.dat", "ms66200.dat", "ms62600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A8", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_760", 0x0000, 10, 6, 45, 6, 1, 30, 0, "br0100", "Sepith_2C4D", 30, 45, 25, 0,
        (
            ("ms62200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A8", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            ("ms62200.dat", "ms62200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            ("ms62200.dat", "ms69800.dat", "ms62200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A8", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7FC", 0x0000, 10, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_2C6D", 30, 45, 25, 0,
        (
            ("ms69800.dat", "ms69800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            ("ms69800.dat", "ms63900.dat", "ms69800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A8", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            ("ms69800.dat", "ms69900.dat", "ms62600.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_898", 0x0400, 17, 6, 45, 6, 1, 30, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68901.dat", "ms68901.dat", "ms68901.dat", "ms68901.dat", "ms68901.dat", "ms68901.dat", "ms68901.dat", "ms68901.dat", "MonsterBattlePostion_588", "MonsterBattlePostion_608", "ed7401", "ed7403", "ATBonus_548"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_8DC", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_2C75", 40, 35, 25, 0,
        (
            ("ms76201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A8", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            ("ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_588", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
            ("ms76201.dat", "ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A8", "MonsterBattlePostion_608", "ed7400", "ed7403", "ATBonus_548"),
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
        "monster/ch63950.itc",               # 10
        "monster/ch63951.itc",               # 11
        "monster/ch62650.itc",               # 12
        "monster/ch62651.itc",               # 13
        "monster/ch62250.itc",               # 14
        "monster/ch62250.itc",               # 15
        "monster/ch69850.itc",               # 16
        "monster/ch69850.itc",               # 17
        "monster/ch68950.itc",               # 18
        "monster/ch68951.itc",               # 19
        "monster/ch76250.itc",               # 1A
        "monster/ch76251.itc",               # 1B
    ))

    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   25,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   25,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   25,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   25,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   25,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(7430,    10740,   0,       0x1010000,    "BattleInfo_628", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-26680,  23160,   0,       0x1010000,    "BattleInfo_6C4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-47820,  49480,   0,       0x1010000,    "BattleInfo_760", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-82330,  83810,   0,       0x1010000,    "BattleInfo_7FC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-68630,  134320,  2000,    0x1010000,    "BattleInfo_628", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-88070,  136430,  2000,    0x1010000,    "BattleInfo_6C4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-28450,  88010,   0,       0x1810000,    "BattleInfo_898", 1078, 24,  0xFFFF, 8,  9)
    DeclMonster(10730,   40540,   -1000,   0x1810000,    "BattleInfo_898", 1079, 24,  0xFFFF, 8,  9)
    DeclMonster(740,     78220,   -1000,   0x1810000,    "BattleInfo_898", 1080, 24,  0xFFFF, 8,  9)
    DeclMonster(-16390,  76670,   -1000,   0x1810000,    "BattleInfo_898", 1081, 24,  0xFFFF, 8,  9)
    DeclMonster(-11580,  63140,   -1000,   0x1810000,    "BattleInfo_898", 1082, 24,  0xFFFF, 8,  9)
    DeclMonster(-20900,  36230,   0,       0x1010000,    "BattleInfo_8DC", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-75890,  91810,   0,       0x1010000,    "BattleInfo_8DC", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 10,  -29.729999542236328,   66.20999908447266,     -1.0,                  81.0,                  [0.11785110831260681,  0.23570236563682556,   -0.0,                  0.0,                   -0.11785118281841278,  0.23570221662521362,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   11.306639671325684,    -8.59841251373291,     0.1428571492433548,    1.0])
    DeclEvent(0x0000, 0, 12,  -29.729999542236328,   66.20999908447266,     -1.0,                  81.0,                  [0.11785110831260681,  0.23570236563682556,   -0.0,                  0.0,                   -0.11785118281841278,  0.23570221662521362,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   11.306639671325684,    -8.59841251373291,     0.1428571492433548,    1.0])

    DeclActor(-84150,  2000,    144490,  1200,    -84150,  3000,    144490,  0x007C, 0,  3,  0x0000)
    DeclActor(3220,    -1000,   92260,   1200,    3220,    0,       92260,   0x007C, 0,  4,  0x0000)
    DeclActor(4000,    -1000,   42910,   1200,    4000,    0,       42910,   0x007C, 0,  5,  0x0000)
    DeclActor(9820,    0,       10930,   1200,    9820,    1000,    10930,   0x007C, 0,  6,  0x0000)
    DeclActor(-29400,  0,       66620,   2000,    -29400,  1500,    66620,   0x007C, 0,  14, 0x0000)
    DeclActor(-28660,  0,       24760,   1200,    -28660,  0,       24760,   0x007C, 0,  7,  0x0000)
    DeclActor(-55620,  0,       75240,   1200,    -55620,  0,       75240,   0x007C, 0,  8,  0x0000)
    DeclActor(-18960,  0,       48760,   5000,    -18960,  0,       48760,   0x007C, 0,  13, 0x0000)

    PlaceName(-5.0, 0.0, -45.0, 0x0000, 0x0000, "克洛斯贝尔市·唐古拉姆门方向")
    PlaceName(-50.0, 0.0, 172.0, 0x0000, 0x0000, "阿尔摩利卡村方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(1299, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1250, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 8
    ChipFrameInfo(2500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 11

    ScpFunction((
        "Function_0_A44",          # 00, 0
        "Function_1_AFC",          # 01, 1
        "Function_2_B61",          # 02, 2
        "Function_3_119B",         # 03, 3
        "Function_4_12D1",         # 04, 4
        "Function_5_1407",         # 05, 5
        "Function_6_153D",         # 06, 6
        "Function_7_1673",         # 07, 7
        "Function_8_1687",         # 08, 8
        "Function_9_169B",         # 09, 9
        "Function_10_16B4",        # 0A, 10
        "Function_11_1D70",        # 0B, 11
        "Function_12_1F5C",        # 0C, 12
        "Function_13_1FD8",        # 0D, 13
        "Function_14_2B3B",        # 0E, 14
    ))


    def Function_0_A44(): pass

    label("Function_0_A44")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_A84"),
        (1, "loc_A90"),
        (2, "loc_A9C"),
        (3, "loc_AA8"),
        (4, "loc_AB4"),
        (5, "loc_AC0"),
        (6, "loc_ACC"),
        (SWITCH_DEFAULT, "loc_AD8"),
    )


    label("loc_A84")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_AE4")

    label("loc_A90")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_AE4")

    label("loc_A9C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_AE4")

    label("loc_AA8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_AE4")

    label("loc_AB4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_AE4")

    label("loc_AC0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_AE4")

    label("loc_ACC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AE4")

    label("loc_AD8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AE4")

    label("loc_AE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AFB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AE4")

    label("loc_AFB")

    Return()

    # Function_0_A44 end

    def Function_1_AFC(): pass

    label("Function_1_AFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B21")
    ClearChrFlags(0x13, 0x80)

    label("loc_B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B30")
    ClearChrFlags(0x14, 0x80)

    label("loc_B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3F")
    ClearChrFlags(0x15, 0x80)

    label("loc_B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4E")
    ClearChrFlags(0x16, 0x80)

    label("loc_B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5D")
    ClearChrFlags(0x17, 0x80)

    label("loc_B5D")

    Call(0, 9)
    Return()

    # Function_1_AFC end

    def Function_2_B61(): pass

    label("Function_2_B61")

    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F10")
    OP_70(0x0, 0x0)
    Jump("loc_F14")

    label("loc_F10")

    OP_70(0x0, 0x1E)

    label("loc_F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F27")
    OP_70(0x1, 0x0)
    Jump("loc_F2B")

    label("loc_F27")

    OP_70(0x1, 0x1E)

    label("loc_F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3E")
    OP_70(0x2, 0x0)
    Jump("loc_F42")

    label("loc_F3E")

    OP_70(0x2, 0x1E)

    label("loc_F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F55")
    OP_70(0x3, 0x0)
    Jump("loc_F59")

    label("loc_F55")

    OP_70(0x3, 0x1E)

    label("loc_F59")

    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 0)), scpexpr(EXPR_END)), "loc_FBF")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -28660, 0, 24760, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)
    Jump("loc_1018")

    label("loc_FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 1)), scpexpr(EXPR_END)), "loc_1018")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -55620, 0, 75240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)

    label("loc_1018")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -29410, 0, 66630, 10000, 2000, 45000)
    SetMapObjFrame(0xFF, "Null_door", 0x2, "open")
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1074")
    SetMapObjFrame(0xFF, "Null_door", 0x2, "close")
    SetBarrier(0x3, 0x0, 0x1)
    OP_66(0x4, 0x1)

    label("loc_1074")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_108F")
    Jump("loc_10E1")

    label("loc_108F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_10A6")
    ModifyEventFlags(1, 1, 0x80)
    Jump("loc_10E1")

    label("loc_10A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_10D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10CF")
    Event(0, 11)

    label("loc_10CF")

    Jump("loc_10E1")

    label("loc_10D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_10E1")

    label("loc_10E1")

    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_10F3")
    Jump("loc_1130")

    label("loc_10F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1130")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_110D")
    Jump("loc_1130")

    label("loc_110D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_111F")
    Jump("loc_1130")

    label("loc_111F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_1130")
    OP_66(0x7, 0x1)

    label("loc_1130")

    SoundDistance(0x7B, 0x57DA, 0xFFFFFC22, 0xB0AE, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E1(0xD8E, 0xFFFFFC22, 0xD4B2)
    OP_E1(0xFFFFF678, 0xFFFFFC22, 0xFF50)
    OP_E1(0x4EC, 0xFFFFFC22, 0x109C8)
    OP_E1(0xFFFFED5E, 0xFFFFFC18, 0x1195E)
    OP_E1(0xFFFFE700, 0xFFFFFDF8, 0x1451E)
    OP_E1(0xFFFFFE02, 0xFFFFFDF8, 0x1C7B4)
    Return()

    # Function_2_B61 end

    def Function_3_119B(): pass

    label("Function_3_119B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1288")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x643, 1)"), scpexpr(EXPR_END)), "loc_121A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x643),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x102, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1283")

    label("loc_121A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x643),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x643),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1283")

    Jump("loc_12C5")

    label("loc_1288")

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

    label("loc_12C5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_119B end

    def Function_4_12D1(): pass

    label("Function_4_12D1")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BE")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1350")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
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
    SetScenarioFlags(0x102, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_13B9")

    label("loc_1350")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13B9")

    Jump("loc_13FB")

    label("loc_13BE")

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

    label("loc_13FB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_12D1 end

    def Function_5_1407(): pass

    label("Function_5_1407")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F4")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x33, 1)"), scpexpr(EXPR_END)), "loc_1486")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x102, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_14EF")

    label("loc_1486")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x33),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x33),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14EF")

    Jump("loc_1531")

    label("loc_14F4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_1531")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1407 end

    def Function_6_153D(): pass

    label("Function_6_153D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162A")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_15BC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
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
    SetScenarioFlags(0x102, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1625")

    label("loc_15BC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
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
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1625")

    Jump("loc_1667")

    label("loc_162A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
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

    label("loc_1667")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_153D end

    def Function_7_1673(): pass

    label("Function_7_1673")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 0)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_1673 end

    def Function_8_1687(): pass

    label("Function_8_1687")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 1)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1687 end

    def Function_9_169B(): pass

    label("Function_9_169B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_16B3")
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)

    label("loc_16B3")

    Return()

    # Function_9_169B end

    def Function_10_16B4(): pass

    label("Function_10_16B4")

    EventBegin(0x0)
    Fade(500)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    OP_68(-31360, 1500, 64599, 0)
    MoveCamera(357, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17060, 0)
    SetChrPos(0x101, -30900, 0, 65400, 45)
    SetChrPos(0x102, -32000, 0, 65390, 45)
    SetChrPos(0x103, -31280, 0, 63830, 45)
    SetChrPos(0x104, -32610, 0, 63700, 45)
    SetChrPos(0x8, -28450, 0, 88010, 135)
    SetChrPos(0x9, 3100, -1000, 35060, 0)
    SetChrPos(0xA, 740, -1000, 78220, 270)
    SetChrPos(0xB, -16390, -1000, 76670, 135)
    SetChrPos(0xC, -11580, -1000, 63140, 315)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
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

    #C0013
    ChrTalk(
        0x101,
        "#5P#0005F这是……！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_68(-28540, 1000, 87990, 0)
    MoveCamera(71, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20760, 0)
    OP_68(-17430, 1500, 75900, 5000)
    MoveCamera(52, 25, 0, 5000)
    Sleep(4900)
    Fade(500)
    OP_68(-3110, 1000, 39950, 0)
    MoveCamera(70, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20760, 0)
    OP_68(-11940, 1000, 63130, 5000)
    MoveCamera(98, 31, 0, 5000)
    SetCameraDistance(16770, 5000)
    OP_6F(0x79)
    Fade(500)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_68(-31360, 1200, 64599, 0)
    MoveCamera(357, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18060, 0)
    SetCameraDistance(17060, 1000)
    OP_0D()
    OP_6F(0x79)

    #C0014
    ChrTalk(
        0x103,
        (
            "#6P#0200F看来这里就是\x01",
            "阿尔摩利卡村的私有地，\x01",
            "确认无误了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#5P#0101F话说回来……\x01",
            "居然跑进来这么多魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#5P#0303F而且，比起在\x01",
            "外面游荡的家伙们，这些\x01",
            "好像要更难对付啊。\x02\x03",

            "#0301F也许是受到上个月魔兽事件的影响，\x01",
            "这些家伙被赶出了觅食地，\x01",
            "所以才从人烟稀少的地方聚集到这里了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#5P#0003F是受鲁巴彻放出的\x01",
            "军犬的影响吗……\x02\x03",

            "#0001F……好吧……\x01",
            "在这里聊天也无济于事，\x01",
            "将锁打开吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, -29840, 0, 66270, 2000, 0x0)
    Sound(809, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "使用了私有地的钥匙。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMapObjFrame(0xFF, "Null_door", 0x2, "anime")
    Sound(851, 0, 100, 0)
    Sleep(1500)

    #C0019
    ChrTalk(
        0x101,
        "#5P#0003F……这样就行了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0020
    ChrTalk(
        0x101,
        (
            "#11P#0001F接下来将消灭私有地的魔兽！\x01",
            "各位，要上了！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        "#5P#0101F是！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        "#5P#0301F交给我吧！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        "#6P#0200F开始吧。\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 0, 0x80)
    OP_68(-29840, 1000, 66270, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x0, -29840, 0, 66270, 45)
    SetChrPos(0x1, -29840, 0, 66270, 45)
    SetChrPos(0x2, -29840, 0, 66270, 45)
    SetChrPos(0x3, -29840, 0, 66270, 45)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_65(0x4, 0x1)
    SetMapObjFrame(0xFF, "Null_door", 0x2, "open")
    SetBarrier(0x2, 0x0, 0x1)
    SetScenarioFlags(0x0, 0)
    OP_29(0xD, 0x1, 0x1)
    Call(0, 9)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -28450, 0, 88010, 0)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 10730, -1000, 40540, 0)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 740, -1000, 78220, 0)
    ClearChrFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -16390, -1000, 76670, 0)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -11580, -1000, 63140, 0)
    ClearChrFlags(0x17, 0x4)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_16B4 end

    def Function_11_1D70(): pass

    label("Function_11_1D70")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    OP_68(-16510, 0, 74800, 0)
    MoveCamera(71, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19430, 0)
    SetChrPos(0x101, -17420, -1000, 75920, 135)
    SetChrPos(0x102, -15210, -1000, 76100, 225)
    SetChrPos(0x103, -17620, -1000, 73700, 45)
    SetChrPos(0x104, -15540, -1000, 73630, 315)
    SetCameraDistance(18430, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0024
    ChrTalk(
        0x101,
        (
            "#6P#0003F……好，刚才的似乎就是\x01",
            "最后一群了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#12P#0200F歼灭完成……\x01",
            "这一带的魔兽气息\x01",
            "已经完全消失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        "#11P#0306F真是的，让人费那么大的劲。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#5P#0100F呵呵，最后将它们全部消灭了，\x01",
            "这不是已经很好了嘛。\x02\x03",

            "……那么，去向特鲁塔村长\x01",
            "报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#6P#0000F是啊，要快点让村长安下心来。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0xD, 0x1, 0x2)
    SetChrPos(0x0, -17420, -1000, 75920, 135)
    ModifyEventFlags(1, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_11_1D70 end

    def Function_12_1F5C(): pass

    label("Function_12_1F5C")

    EventBegin(0x1)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【返回阿尔摩利卡村】\x01",      # 0
            "【放弃】\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FC1")
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    OP_24(0x7B)
    WaitBGM()
    ClearMapFlags(0x8000000)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FD7")

    label("loc_1FC1")

    Sleep(50)
    SetChrPos(0x0, -26840, -140, 69350, 45)
    EventEnd(0x5)

    label("loc_1FD7")

    Return()

    # Function_12_1F5C end

    def Function_13_1FD8(): pass

    label("Function_13_1FD8")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-21240, 2200, 44210, 0)
    MoveCamera(38, 8, 2, 0)
    OP_6E(600, 0)
    SetCameraDistance(13590, 0)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    LoadChrToIndex("apl/ch50387.itc", 0x1E)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, -22370, 0, 48680, 65)
    SetChrPos(0x102, -21150, 0, 47760, 65)
    SetChrPos(0x103, -21330, 0, 46270, 65)
    SetChrPos(0x104, -20270, 0, 45630, 65)
    FadeToBright(500, 0)
    OP_0D()

    #C0029
    ChrTalk(
        0x102,
        (
            "#6P#0100F古道边的田园风景……\x01",
            "这么一看，真是很漂亮呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#12P#0300F是啊。\x01",
            "上次来消灭魔兽的时候，\x01",
            "没能好好欣赏……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        (
            "#12P#0200F在这里吃便当的话，\x01",
            "食物似乎也会变得很美味呢。\x02\x03",

            "虽然因为有魔兽在，\x01",
            "所以估计不会吃得很顺利……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#6P#0000F不过，这里的风景对于\x01",
            "开车兜风来说，真是再合适不过了。\x02\x03",

            "像哈罗德先生那样\x01",
            "经常要跑遍整个自治州的商人，\x01",
            "应该会觉得这种风景相当亲切吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#6P#0100F嗯，一定是那样没错吧。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，格蕾丝小姐委托我们拍摄的照片，\x01",
            "在这里似乎能拍到很不错的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27F2")
    TurnDirection(0x101, 0x102, 500)

    #C0035
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么艾莉，\x01",
            "可以拜托你来拍照吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0036
    ChrTalk(
        0x102,
        (
            "#6P#0108F哎，好的。\x01",
            "虽然我没什么自信……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0037
    ChrTalk(
        0x104,
        (
            "#12P#0300F哪里哪里，应该没问题吧。\x02\x03",

            "只要看看镜头，\x01",
            "然后咔嚓一下拍下来\x01",
            "不就搞定了嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0038
    ChrTalk(
        0x102,
        (
            "#6P#0106F我说你啊……\x01",
            "要拍出好照片，\x01",
            "可没有那么简单哦。\x02\x03",

            "#0100F要注意确认\x01",
            "拍摄对象有没有被收入取景框中，\x01",
            "还要构思摄影角度……\x02\x03",

            "而且受到天气和风的影响，\x01",
            "照片所呈现出的感觉也会有很大不同。\x02\x03",

            "有时只要错过那一瞬的时机，\x01",
            "就再也拍不到\x01",
            "那么好的风景了。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x103,
        (
            "#12P#0200F外行和专家所拍出的照片，\x01",
            "差别可是一目了然的。\x02\x03",

            "#0203F不过，某些粗神经的人\x01",
            "大概无法理解这种细致的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#12P#0306F唔……\x01",
            "你在说谁啊，说谁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#6P#0000F好啦好啦，\x01",
            "总之就交给艾莉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#6P#0100F那么……\x01",
            "我来试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x41, 0x1F4)
    OP_93(0x101, 0x41, 0x1F4)
    OP_93(0x103, 0x41, 0x1F4)
    OP_93(0x104, 0x41, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x102,
        (
            "#6P#0103F……呼，\x01",
            "为了保险起见，我多拍了几张。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#6P#0000F看样子，似乎已经拍好了呢。\x02\x03",

            "感觉怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#6P#0100F在没有实际显像出来之前，\x01",
            "还无法确定……\x02\x03",

            "不过，我觉得至少\x01",
            "不会很差吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#12P#0200F艾莉前辈似乎\x01",
            "找回感觉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#12P#0300F哼……\x01",
            "反正只有我完全搞不懂。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#6P#0000F如果发现了这种风景漂亮的地方，\x01",
            "就再拍些照片吧。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AFC")

    label("loc_27F2")

    TurnDirection(0x101, 0x102, 500)

    #C0049
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么……\x01",
            "艾莉，麻烦你拍照了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        "#6P#0100F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x41, 0x1F4)
    OP_93(0x101, 0x41, 0x1F4)
    OP_93(0x103, 0x41, 0x1F4)
    OP_93(0x104, 0x41, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0051
    ChrTalk(
        0x102,
        (
            "#6P#0103F……呼，\x01",
            "大概就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2974")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2974")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_298B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_298B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_29A2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_29B9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_29D0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_29E7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_29FE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2A15")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_2A2C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ABC")

    #C0052
    ChrTalk(
        0x101,
        (
            "#6P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "这样一来，就拍完了格蕾丝小姐\x01",
            "所要求的五张照片了。\x01",
            "现在随时都可以去交付了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AFC")

    label("loc_2ABC")


    #C0053
    ChrTalk(
        0x101,
        (
            "#6P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -18960, 0, 48760, 90)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x1E)
    OP_29(0x18, 0x1, 0x2)
    Sleep(500)
    OP_37()
    ClearMapFlags(0x8000000)
    Call(0, 9)
    OP_65(0x7, 0x1)
    EventEnd(0x5)
    Return()

    # Function_13_1FD8 end

    def Function_14_2B3B(): pass

    label("Function_14_2B3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BE8")
    EventBegin(0x1)
    Sound(810, 0, 100, 0)

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门似乎上了锁。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【打开门】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE1")
    Sound(809, 0, 100, 0)
    Sleep(500)
    SetMapObjFrame(0xFF, "Null_door", 0x2, "anime")
    Sound(851, 0, 100, 0)
    Sleep(1500)
    SetScenarioFlags(0x0, 0)
    SetMapObjFrame(0xFF, "Null_door", 0x2, "open")
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)

    label("loc_2BE1")

    EventEnd(0x5)
    Jump("loc_2C24")

    label("loc_2BE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_2BFD")
    Call(0, 10)
    Jump("loc_2C24")

    label("loc_2BFD")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门似乎上了锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2C24")

    Return()

    # Function_14_2B3B end

    SaveToFile()

Try(main)
