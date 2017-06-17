from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0000.bin",                # FileName
        "m0000",                    # MapName
        "m0000",                    # Location
        0x0067,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 103, 0, 5, 0, 6],
    )

    BuildStringList((
        "m0000",                  # 0
        "魔獣",                   # 1
        "魔獣",                   # 2
        "魔獣",                   # 3
        "魔獣",                   # 4
        "bm0001",                 # 5
        "bm0001",                 # 6
        "bm0001",                 # 7
        "bm0001",                 # 8
        "bm0001",                 # 9
        "bm0001",                 # 10
        "bm0000",                 # 11
        "bm0001",                 # 12
    ))

    ATBonus("ATBonus_6E0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_720", 100, 5, 1, 0, 1, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0)

    Sepith("Sepith_4C0E", 2,   0,   3,   2,   1,   0,   2)
    Sepith("Sepith_4BF6", 3,   1,   2,   0,   1,   2,   1)
    Sepith("Sepith_4C06", 1,   4,   0,   2,   0,   2,   1)
    Sepith("Sepith_4BFE", 1,   2,   0,   4,   1,   1,   0)

    MonsterBattlePostion("MonsterBattlePostion_790", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_794", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_798", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_79C", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A8", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7AC", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D0", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_7D4", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D8", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_7DC", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_7E0", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_7E4", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_7E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_770", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_774", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_778", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_77C", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_780", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_784", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_788", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_78C", 9, 15, 180)

    # monster count: 10

    BattleInfo(
        "BattleInfo_914", 0x0000, 3, 6, 45, 10, 1, 40, 0, "bm0001", "Sepith_4C0E", 75, 25, 0, 0,
        (
            ("ms61700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_790", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_6E0"),
            ("ms61700.dat", "ms61700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_770", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_6E0"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7F0", 0x0000, 3, 6, 45, 6, 1, 40, 0, "bm0001", "Sepith_4BF6", 75, 25, 0, 0,
        (
            ("ms60100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_790", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_6E0"),
            ("ms60100.dat", "ms60100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_770", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_6E0"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_984", 0x0000, 1, 6, 0, 0, 0, 0, 2, "bm0001", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60100.dat", "ms60100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_770", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_720"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9C8", 0x0000, 1, 6, 0, 0, 0, 0, 3, "bm0001", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73100.dat", "ms73100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_770", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_720"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A0C", 0x0000, 1, 6, 0, 0, 0, 0, 4, "bm0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60300.dat", "ms60300.dat", "ms60300.dat", "ms60300.dat", 0, 0, 0, 0, "MonsterBattlePostion_790", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_720"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A50", 0x0000, 1, 6, 0, 0, 0, 0, 5, "bm0001", 0x00000000, 100, 0, 0, 0,
        (
            ("ms61700.dat", "ms61700.dat", "ms61700.dat", "ms61700.dat", 0, 0, 0, 0, "MonsterBattlePostion_770", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_720"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_8D0", 0x0000, 3, 6, 45, 6, 1, 25, 0, "bm0001", "Sepith_4C06", 100, 0, 0, 0,
        (
            ("ms73100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_790", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_6E0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_860", 0x0000, 3, 6, 45, 6, 1, 30, 0, "bm0001", "Sepith_4BFE", 75, 25, 0, 0,
        (
            ("ms60300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_790", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_6E0"),
            ("ms60300.dat", "ms60300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_770", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_6E0"),
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
        "monster/ch60150.itc",               # 10
        "monster/ch60151.itc",               # 11
        "monster/ch60350.itc",               # 12
        "monster/ch60351.itc",               # 13
        "monster/ch73150.itc",               # 14
        "monster/ch73151.itc",               # 15
        "monster/ch61750.itc",               # 16
        "monster/ch61750.itc",               # 17
    ))

    DeclNpc(-209,    0,       97279,   0,    385,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-102120, 0,       199509,  90,   385,  0x0, 0,   20,  0,   0,   3,   255, 255, 255,  0)
    DeclNpc(-200190, 100,     199740,  90,   385,  0x0, 0,   18,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(-200100, 0,       294179,  180,  385,  0x0, 0,   22,  0,   0,   4,   255, 255, 255,  0)

    DeclMonster(-200100, 294180,  0,       0x1010000,    "BattleInfo_914", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-106700, 399680,  0,       0x1010000,    "BattleInfo_7F0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-97580,  396200,  0,       0x1010000,    "BattleInfo_7F0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-210,    97280,   0,       0x1810000,    "BattleInfo_984", 2,   16,  0xFFFF, 0,  1)
    DeclMonster(-102120, 199510,  0,       0x181005A,    "BattleInfo_9C8", 670, 20,  0xFFFF, 4,  5)
    DeclMonster(-200190, 199740,  100,     0x181005A,    "BattleInfo_A0C", 588, 18,  0xFFFF, 2,  3)
    DeclMonster(-200100, 294180,  0,       0x18100B4,    "BattleInfo_A50", 669, 22,  0xFFFF, 6,  7)
    DeclMonster(-210,    97280,   0,       0x1010000,    "BattleInfo_7F0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-102120, 199510,  0,       0x1010000,    "BattleInfo_8D0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-200190, 199740,  100,     0x1010000,    "BattleInfo_860", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 21,  -100.0,                -5.0,                  -1.0,                  25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   19.999998092651367,    2.5,                   0.19999998807907104,   1.0])
    DeclEvent(0x0000, 0, 34,  -100.0,                -7.050000190734863,    -1.0,                  25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   19.999998092651367,    3.5250000953674316,    0.19999998807907104,   1.0])
    DeclEvent(0x0000, 0, 25,  -0.10999999940395355,  113.54000091552734,    0.15000000596046448,   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.02199999801814556,   -56.77000045776367,    -0.029999999329447746, 1.0])
    DeclEvent(0x0000, 0, 27,  -112.47000122070312,   199.7899932861328,     -0.0,                  156.25,                [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  1.0,                   0.0,                   22.493999481201172,    -39.9579963684082,     0.0,                   1.0])
    DeclEvent(0x0000, 0, 29,  -199.9600067138672,    207.3300018310547,     0.1599999964237213,    25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   39.992000579833984,    -103.66500091552734,   -0.03199999779462814,  1.0])
    DeclEvent(0x0000, 0, 30,  -200.0,                192.57000732421875,    0.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   39.999996185302734,    -96.28500366210938,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 32,  -200.0,                319.0,                 0.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   39.999996185302734,    -159.5,                -0.0,                  1.0])

    DeclActor(100000,  0,       2000,    1200,    100000,  1000,    2500,    0x007C, 0,  15, 0x0000)
    DeclActor(100000,  0,       102000,  1200,    100000,  1000,    102500,  0x007C, 0,  17, 0x0000)
    DeclActor(2000,    0,       400000,  1200,    2500,    1000,    400000,  0x007C, 0,  19, 0x0000)
    DeclActor(5000,    0,       200000,  1200,    5000,    1000,    200000,  0x007C, 0,  9,  0x0000)
    DeclActor(-200000, 0,       104000,  1200,    -200000, 1000,    104000,  0x007C, 0,  10, 0x0000)
    DeclActor(-100000, 0,       404500,  1200,    -100000, 1000,    404500,  0x007C, 0,  11, 0x0000)
    DeclActor(-194710, 4000,    405550,  1200,    -194710, 5500,    405550,  0x007C, 0,  14, 0x0000)
    DeclActor(-97500,  0,       5000,    1200,    -97500,  1500,    5000,    0x007C, 0,  13, 0x0000)
    DeclActor(-90570,  0,       0,       1200,    -90570,  1500,    0,       0x007C, 0,  35, 0x0000)
    DeclActor(100000,  0,       11820,   1200,    100000,  1500,    11820,   0x007C, 0,  36, 0x0000)
    DeclActor(-205000, 0,       200000,  1200,    -205000, 1000,    200000,  0x007C, 0,  12, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3])                         # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_B88",          # 00, 0
        "Function_1_C40",          # 01, 1
        "Function_2_C5D",          # 02, 2
        "Function_3_C7C",          # 03, 3
        "Function_4_C9B",          # 04, 4
        "Function_5_CB7",          # 05, 5
        "Function_6_DDA",          # 06, 6
        "Function_7_12F2",         # 07, 7
        "Function_8_134D",         # 08, 8
        "Function_9_13FF",         # 09, 9
        "Function_10_154C",        # 0A, 10
        "Function_11_165E",        # 0B, 11
        "Function_12_17AB",        # 0C, 12
        "Function_13_1866",        # 0D, 13
        "Function_14_1971",        # 0E, 14
        "Function_15_1E2A",        # 0F, 15
        "Function_16_1FBE",        # 10, 16
        "Function_17_2105",        # 11, 17
        "Function_18_2299",        # 12, 18
        "Function_19_23D6",        # 13, 19
        "Function_20_256A",        # 14, 20
        "Function_21_26B1",        # 15, 21
        "Function_22_2ED6",        # 16, 22
        "Function_23_300A",        # 17, 23
        "Function_24_3423",        # 18, 24
        "Function_25_3A3D",        # 19, 25
        "Function_26_3ABF",        # 1A, 26
        "Function_27_3C98",        # 1B, 27
        "Function_28_3D2C",        # 1C, 28
        "Function_29_3F2B",        # 1D, 29
        "Function_30_3FA1",        # 1E, 30
        "Function_31_4017",        # 1F, 31
        "Function_32_4274",        # 20, 32
        "Function_33_42FA",        # 21, 33
        "Function_34_482E",        # 22, 34
        "Function_35_4B58",        # 23, 35
        "Function_36_4B93",        # 24, 36
    ))


    def Function_0_B88(): pass

    label("Function_0_B88")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_BC8"),
        (1, "loc_BD4"),
        (2, "loc_BE0"),
        (3, "loc_BEC"),
        (4, "loc_BF8"),
        (5, "loc_C04"),
        (6, "loc_C10"),
        (SWITCH_DEFAULT, "loc_C1C"),
    )


    label("loc_BC8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_C28")

    label("loc_BD4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_C28")

    label("loc_BE0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_C28")

    label("loc_BEC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_C28")

    label("loc_BF8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_C28")

    label("loc_C04")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_C28")

    label("loc_C10")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C28")

    label("loc_C1C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C28")

    label("loc_C28")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C3F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C28")

    label("loc_C3F")

    Return()

    # Function_0_B88 end

    def Function_1_C40(): pass

    label("Function_1_C40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C5C")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_C40")

    label("loc_C5C")

    Return()

    # Function_1_C40 end

    def Function_2_C5D(): pass

    label("Function_2_C5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C7B")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_C5D")

    label("loc_C7B")

    Return()

    # Function_2_C5D end

    def Function_3_C7C(): pass

    label("Function_3_C7C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C9A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_3_C7C")

    label("loc_C9A")

    Return()

    # Function_3_C7C end

    def Function_4_C9B(): pass

    label("Function_4_C9B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CB6")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_4_C9B")

    label("loc_CB6")

    Return()

    # Function_4_C9B end

    def Function_5_CB7(): pass

    label("Function_5_CB7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1D")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE4")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)
    Jump("loc_D1D")

    label("loc_CE4")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D03")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)
    Jump("loc_D1D")

    label("loc_D03")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1D")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 20)

    label("loc_D1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D37")
    Event(0, 22)

    label("loc_D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_D46")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 33)

    label("loc_D46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D57")
    SetScenarioFlags(0x58, 0)

    label("loc_D57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D68")
    SetScenarioFlags(0x58, 1)

    label("loc_D68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D83")
    Event(0, 26)

    label("loc_D83")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D9E")
    Event(0, 28)

    label("loc_D9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB9")
    Event(0, 31)

    label("loc_DB9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x81), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DD6")
    OP_C7(0x0, 0x1000)

    label("loc_DD6")

    Call(0, 7)
    Return()

    # Function_5_CB7 end

    def Function_6_DDA(): pass

    label("Function_6_DDA")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0xD, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0xE, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58, 0)), scpexpr(EXPR_END)), "loc_EA1")
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x2, "light00", 0x1, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jump("loc_EE5")

    label("loc_EA1")

    SetMapObjFrame(0x2, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x2, "light00", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x1, 0x1)
    SetMapObjFrame(0x2, "light01", 0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x8, 0x1)

    label("loc_EE5")

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
    OP_65(0x9, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58, 1)), scpexpr(EXPR_END)), "loc_101F")
    SetMapObjFrame(0xB, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xB, "light01", 0x0, 0x1)
    SetMapObjFrame(0xB, "sign00", 0x1, 0x1)
    SetMapObjFrame(0xB, "light00", 0x1, 0x1)
    SetMapObjFlags(0xB, 0x10)
    Jump("loc_1063")

    label("loc_101F")

    SetMapObjFrame(0xB, "sign00", 0x0, 0x1)
    SetMapObjFrame(0xB, "light00", 0x0, 0x1)
    SetMapObjFrame(0xB, "sign01", 0x1, 0x1)
    SetMapObjFrame(0xB, "light01", 0x1, 0x1)
    ClearMapObjFlags(0xB, 0x10)
    OP_66(0x9, 0x1)

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1076")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1087")
    Event(0, 24)

    label("loc_1087")

    OP_10(0x19, 0x0)
    OP_10(0x1E, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A6")
    OP_10(0x10, 0x0)
    OP_10(0x1D, 0x1)
    Jump("loc_10AC")

    label("loc_10A6")

    OP_10(0x10, 0x1)
    OP_10(0x1D, 0x0)

    label("loc_10AC")

    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121F")
    OP_70(0xF, 0x0)
    Jump("loc_1223")

    label("loc_121F")

    OP_70(0xF, 0x1E)

    label("loc_1223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1236")
    OP_70(0x10, 0x0)
    Jump("loc_123A")

    label("loc_1236")

    OP_70(0x10, 0x1E)

    label("loc_123A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124D")
    OP_70(0x11, 0x0)
    Jump("loc_1251")

    label("loc_124D")

    OP_70(0x11, 0x1E)

    label("loc_1251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1264")
    OP_70(0x13, 0x0)
    Jump("loc_1268")

    label("loc_1264")

    OP_70(0x13, 0x1E)

    label("loc_1268")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1280")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1280")

    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    ModifyEventFlags(0, 6, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12AD")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12C1")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_12C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12DA")
    ModifyEventFlags(1, 4, 0x80)
    ModifyEventFlags(1, 5, 0x80)

    label("loc_12DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12EE")
    ModifyEventFlags(1, 6, 0x80)

    label("loc_12EE")

    Call(0, 8)
    Return()

    # Function_6_DDA end

    def Function_7_12F2(): pass

    label("Function_7_12F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1301")
    ClearChrFlags(0xF, 0x80)

    label("loc_1301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1310")
    ClearChrFlags(0x10, 0x80)

    label("loc_1310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131F")
    ClearChrFlags(0x11, 0x80)

    label("loc_131F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132E")
    ClearChrFlags(0x12, 0x80)

    label("loc_132E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134C")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0xC, 0x80)

    label("loc_134C")

    Return()

    # Function_7_12F2 end

    def Function_8_134D(): pass

    label("Function_8_134D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1373")
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x13, 0x8)
    Jump("loc_1390")

    label("loc_1373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1382")
    ClearChrFlags(0xF, 0x8)

    label("loc_1382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_END)), "loc_1390")
    ClearChrFlags(0x13, 0x8)

    label("loc_1390")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BF")
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x15, 0x8)
    Jump("loc_13D8")

    label("loc_13BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D3")
    ClearChrFlags(0x11, 0x8)
    Jump("loc_13D8")

    label("loc_13D3")

    ClearChrFlags(0x15, 0x8)

    label("loc_13D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13F9")
    SetChrFlags(0xD, 0x8)
    Jump("loc_13FE")

    label("loc_13F9")

    ClearChrFlags(0xD, 0x8)

    label("loc_13FE")

    Return()

    # Function_8_134D end

    def Function_9_13FF(): pass

    label("Function_9_13FF")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14FB")
    Sound(14, 0, 100, 0)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F4, 1)"), scpexpr(EXPR_END)), "loc_1484")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10A, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_14F6")

    label("loc_1484")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14F6")

    Jump("loc_1540")

    label("loc_14FB")

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

    label("loc_1540")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_13FF end

    def Function_10_154C(): pass

    label("Function_10_154C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1627")
    Sound(14, 0, 100, 0)
    OP_71(0x10, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x10, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 20)
    AddSepith(0x1, 20)
    AddSepith(0x2, 20)
    AddSepith(0x3, 20)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×２０\x01\x07\x02",

            "#57I水のセピス×２０\x01\x07\x02",

            "#58I火のセピス×２０\x01\x07\x02",

            "#59I風のセピス×２０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10A, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_164C")

    label("loc_1627")


    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_164C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_154C end

    def Function_11_165E(): pass

    label("Function_11_165E")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175A")
    Sound(14, 0, 100, 0)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_16E3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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
    SetScenarioFlags(0x10A, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1755")

    label("loc_16E3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0007
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
    OP_71(0x11, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1755")

    Jump("loc_179F")

    label("loc_175A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
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

    label("loc_179F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_165E end

    def Function_12_17AB(): pass

    label("Function_12_17AB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182F")
    Sound(14, 0, 100, 0)
    OP_71(0x13, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x13, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddItemNumber(0x20D, 5)

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#14I煙り玉×５\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10A, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_1854")

    label("loc_182F")


    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1854")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_17AB end

    def Function_13_1866(): pass

    label("Function_13_1866")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0011
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1953")
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

    label("loc_1953")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_196F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_196F")

    Return()

    # Function_13_1866 end

    def Function_14_1971(): pass

    label("Function_14_1971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DA6")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ADC")

    #C0012
    ChrTalk(
        0x101,
        (
            "#0005Fこんな所に\x01",
            "地上に出るはしごが……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#0200F上はマンホールのようですね。\x01",
            "……データベースには\x01",
            "記載されていませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        "#0305Fなんで開きっぱなしなんだ？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#0103Fさあ……管理している市庁舎が\x01",
            "閉め忘れたのかもしれないわね。\x02\x03",

            "#0100Fあとで連絡を\x01",
            "入れておいた方がいいかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#0003Fそうだな……そうしようか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 3)
    Jump("loc_1D9E")

    label("loc_1ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4B")

    #C0017
    ChrTalk(
        0x101,
        (
            "#0005Fこんな所に\x01",
            "地上に出るはしごが……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        (
            "#0200F上はマンホールのようですね。\x01",
            "……データベースには\x01",
            "記載されていませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#0300Fははあ、なるほど。\x01",
            "ここから入っちまったわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x197,
        (
            "す、すみません……\x01",
            "勝手なことしちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#0100F今は言っても仕方ないわ。\x02\x03",

            "それより、早くあなたの\x01",
            "お友達を探しましょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x197,
        "は、はい……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D47")

    label("loc_1C4B")

    SetChrName("")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "外に出るはしごがある。\x02\x03",

            "中央広場のマンホールに繋がっているようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0024
    ChrTalk(
        0x197,
        (
            "す、すみません……\x01",
            "ボクたちが勝手に\x01",
            "入り込んじゃったばっかりに……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#0100F今は言っても仕方ないわ。\x02\x03",

            "それより、早くあなたの\x01",
            "お友達を探しましょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x197,
        "は、はい……！\x02",
    )

    CloseMessageWindow()

    label("loc_1D47")

    SetScenarioFlags(0x4B, 1)
    Jump("loc_1D9E")

    label("loc_1D4F")

    SetChrName("")

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "外に出るはしごがある。\x02\x03",

            "中央広場のマンホールに繋がっているようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1D9E")

    TalkEnd(0xFF)
    Jump("loc_1E29")

    label("loc_1DA6")

    EventBegin(0x1)

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハシゴがある。\x01",
            "登りますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E17")
    EventEnd(0x5)
    NewScene("c010C", 111, 0, 0)
    IdleLoop()
    Jump("loc_1E22")

    label("loc_1E17")

    EventEnd(0x5)
    NewScene("c0100", 111, 0, 0)
    IdleLoop()

    label("loc_1E22")

    Jump("loc_1E29")

    label("loc_1E27")

    EventEnd(0x5)

    label("loc_1E29")

    Return()

    # Function_14_1971 end

    def Function_15_1E2A(): pass

    label("Function_15_1E2A")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0029
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FB6")
    Fade(500)
    SetChrPos(0x0, 99400, 0, 600, 0)
    SetChrPos(0x1, 100600, 0, 600, 0)
    SetChrPos(0x2, 99400, 0, -600, 0)
    SetChrPos(0x3, 100600, 0, -600, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F14")
    SetChrPos(0x4, 99400, 0, -1800, 0)
    SetChrPos(0x5, 100600, 0, -1800, 0)
    Jump("loc_1F33")

    label("loc_1F14")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F33")
    SetChrPos(0x4, 100000, 0, -1800, 0)

    label("loc_1F33")

    OP_68(100000, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(100000, -4000, 0, 2000)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0001", 0, 0, 0)
    IdleLoop()

    label("loc_1FB6")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_1E2A end

    def Function_16_1FBE(): pass

    label("Function_16_1FBE")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(100000, -4000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 99400, -10000, 600, 0)
    OP_90(0x1, 100600, -10000, 600, 0)
    OP_90(0x2, 99400, -10000, -600, 0)
    OP_90(0x3, 100600, -10000, -600, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2093")
    OP_90(0x4, 99400, 0, -1800, 0)
    OP_90(0x5, 100600, 0, -1800, 0)
    Jump("loc_20B2")

    label("loc_2093")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20B2")
    OP_90(0x4, 100000, 0, -1800, 0)

    label("loc_20B2")

    Sound(145, 0, 100, 0)
    OP_68(100000, 1000, 0, 3000)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xC)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_16_1FBE end

    def Function_17_2105(): pass

    label("Function_17_2105")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0030
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2291")
    Fade(500)
    SetChrPos(0x0, 99400, 0, 100600, 0)
    SetChrPos(0x1, 100600, 0, 100600, 0)
    SetChrPos(0x2, 99400, 0, 99400, 0)
    SetChrPos(0x3, 100600, 0, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21EF")
    SetChrPos(0x4, 99400, 0, 98200, 0)
    SetChrPos(0x5, 100600, 0, 98200, 0)
    Jump("loc_220E")

    label("loc_21EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_220E")
    SetChrPos(0x4, 100000, 0, 98200, 0)

    label("loc_220E")

    OP_68(100000, 1000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(100000, -4000, 100000, 2000)
    SetMapObjFrame(0xD, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0011", 0, 0, 0)
    IdleLoop()

    label("loc_2291")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_2105 end

    def Function_18_2299(): pass

    label("Function_18_2299")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xD, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(100000, -4000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 99400, -10000, 100600, 0)
    OP_90(0x1, 100600, -10000, 100600, 0)
    OP_90(0x2, 99400, -10000, 99400, 0)
    OP_90(0x3, 100600, -10000, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2364")
    OP_90(0x4, 99400, 0, 98200, 0)
    OP_90(0x5, 100600, 0, 98200, 0)
    Jump("loc_2383")

    label("loc_2364")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2383")
    OP_90(0x4, 100000, 0, 98200, 0)

    label("loc_2383")

    Sound(145, 0, 100, 0)
    OP_68(100000, 1000, 100000, 3000)
    SetMapObjFrame(0xD, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xD)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_18_2299 end

    def Function_19_23D6(): pass

    label("Function_19_23D6")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0031
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2562")
    Fade(500)
    SetChrPos(0x0, 600, 0, 399400, 90)
    SetChrPos(0x1, 600, 0, 400600, 90)
    SetChrPos(0x2, -600, 0, 399400, 90)
    SetChrPos(0x3, -600, 0, 400600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C0")
    SetChrPos(0x4, -1800, 0, 399400, 90)
    SetChrPos(0x5, -1800, 0, 400600, 90)
    Jump("loc_24DF")

    label("loc_24C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24DF")
    SetChrPos(0x4, -1800, 0, 400000, 90)

    label("loc_24DF")

    OP_68(0, 1000, 400000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(0, -4000, 400000, 2000)
    SetMapObjFrame(0xE, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0001", 0, 0, 0)
    IdleLoop()

    label("loc_2562")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_19_23D6 end

    def Function_20_256A(): pass

    label("Function_20_256A")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xE, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(0, -4000, 400000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, -10000, 399400, 90)
    OP_90(0x1, 600, -10000, 400600, 90)
    OP_90(0x2, -600, -10000, 399400, 90)
    OP_90(0x3, -600, -10000, 400600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_263F")
    OP_90(0x4, -1800, 0, 399400, 90)
    OP_90(0x5, -1800, 0, 400600, 90)
    Jump("loc_265E")

    label("loc_263F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_265E")
    OP_90(0x4, -1800, 0, 400000, 90)

    label("loc_265E")

    Sound(145, 0, 100, 0)
    OP_68(0, 1000, 400000, 3000)
    SetMapObjFrame(0xE, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xE)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_20_256A end

    def Function_21_26B1(): pass

    label("Function_21_26B1")

    EventBegin(0x0)
    OP_E0(0x1)
    Fade(1000)
    OP_68(-100000, 3500, 0, 0)
    MoveCamera(55, 32, 0, 0)
    OP_6E(840, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -100000, 100, 1200, 0)
    SetChrPos(0x102, -98800, 100, 0, 90)
    SetChrPos(0x103, -101200, 100, 0, 270)
    SetChrPos(0x104, -100000, 100, -1200, 180)
    OP_68(-100000, 500, 0, 7000)
    MoveCamera(35, 24, 0, 7000)
    SetCameraDistance(22000, 7000)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    Sleep(500)
    Fade(500)
    OP_68(-100000, 1100, 0, 0)
    MoveCamera(65, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    #C0032
    ChrTalk(
        0x101,
        "#5P#0001Fここが『ジオフロント』……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#11P#0101F話には聞いていたけど\x01",
            "こんな場所が都市の地下に\x01",
            "広がっていたなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        (
            "#7P#0305Fは～、たまげたな。\x02\x03",

            "中世の地下水道あたりが\x01",
            "残っている場所かと思ったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#6P#0200Fデータベースの記録によると\x01",
            "２０年前の都市計画と同時に\x01",
            "建造が開始された場所らしいです。\x02\x03",

            "上水道、下水道、ゴミ処理施設に加え、\x01",
            "導力ケーブルや各種プラントなども\x01",
            "後から増設されたようですね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_292F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_292F)
    Sleep(150)

    def lambda_293F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_293F)
    Sleep(50)

    def lambda_294F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_294F)
    Sleep(50)

    def lambda_295F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_295F)
    WaitChrThread(0x103, 2)

    #C0036
    ChrTalk(
        0x101,
        (
            "#5P#0006F……いや、これは確かに\x01",
            "予想外の場所だったかもしれない。\x02\x03",

            "#0001Fしかし、この上はたしか\x01",
            "中央広場あたりになるんだよな？\x02\x03",

            "その下に魔獣が徘徊しているのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#6P#0203F普段は封鎖されているため\x01",
            "都市に現れることはありませんが……\x02\x03",

            "たまに工事現場の作業員の方々が\x01",
            "襲われてケガをする事があるようです。\x02\x03",

            "#0200Fですが現在、警察の方では\x01",
            "対処しきれていないみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#5P#0008F……そうか………\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#11P#0101Fそのための特務支援課……\x01",
            "ということかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#7P#0304Fま、それならそれで、\x01",
            "判りやすくていいけどな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0041
    ChrTalk(
        0x101,
        (
            "#5P#0003F──状況は判った。\x02\x03",

            "#0001F捜査官の役目かどうかはともかく、\x01",
            "必要な仕事であるのは確かみたいだ。\x02\x03",

            "テストであるかどうかは別にして\x01",
            "きちんとやり遂げておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        "#12P#0309Fおーおー、真面目だねぇ。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        (
            "#11P#0104Fでも、確かにそうね。\x02\x03",

            "#0100F一つ一つ基本を確かめながら\x01",
            "確実に進んでいきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        "#6P#0203F……了解です。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-97900, 1100, 4730, 2000)
    MoveCamera(65, 20, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(20000, 2000)

    def lambda_2D28():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D28)
    Sleep(150)

    def lambda_2D38():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2D38)
    Sleep(50)

    def lambda_2D48():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2D48)
    Sleep(50)

    def lambda_2D58():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2D58)
    WaitChrThread(0x103, 2)
    CloseMessageWindow()
    OP_6F(0x79)
    Sound(828, 0, 100, 0)

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※この機械は危険なマップに配置された\x01",
            "  オーブメントの回復装置です。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※この装置を○ボタンで調べて\x01",
            "  『ここで休憩する』を選択すると、\x01",
            "  ＨＰ、ＥＰが全回復します。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※パーティが危険な状態になったら\x01",
            "  ここで回復しましょう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0048
    ChrTalk(
        0x101,
        (
            "#11P#0000F（よし、危なくなったら\x01",
            "  ここまで戻って回復しておこう。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -100000, 100, 0, 0)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0x40, 3)
    OP_29(0x3C, 0x1, 0x1)
    OP_E0(0x0)
    Call(0, 7)
    EventEnd(0x5)
    Return()

    # Function_21_26B1 end

    def Function_22_2ED6(): pass

    label("Function_22_2ED6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_2F01")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F6D")

    label("loc_2F01")

    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "戦闘のチュートリアルを見ますか？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【はい】\x01",        # 0
            "【いいえ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_2F6D")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F83"),
        (1, "loc_2F8E"),
        (SWITCH_DEFAULT, "loc_2FF0"),
    )


    label("loc_2F83")

    SetScenarioFlags(0x49, 5)
    Call(0, 23)
    Jump("loc_2FFF")

    label("loc_2F8E")

    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)
    SetScenarioFlags(0x44, 1)
    SetScenarioFlags(0x44, 2)
    SetScenarioFlags(0x53, 6)
    SetScenarioFlags(0x49, 4)
    SetScenarioFlags(0x53, 5)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    ModifyEventFlags(0, 6, 0x80)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_2FFF")

    label("loc_2FF0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FFF")

    label("loc_2FFF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_2ED6 end

    def Function_23_300A(): pass

    label("Function_23_300A")

    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -900, 0, 88300, 0)
    SetChrPos(0x102, 400, 0, 88300, 0)
    SetChrPos(0x103, -900, 0, 87300, 0)
    SetChrPos(0x104, 400, 0, 87300, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis201.itp")
    OP_68(-2370, 2000, 94890, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(17390, 0)
    SetCameraDistance(16970, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0050
    ChrTalk(
        0x102,
        "#0101F#5P（……いた……！）\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        "#0301F#5P（さっそくお出でなすったな。）\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#0201F#5P（……あれが魔獣……）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-2330, 2000, 89270, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18390, 0)
    OP_0D()

    #C0053
    ChrTalk(
        0x101,
        (
            "#0003F#5P（このメンバーでの初実戦だ……）\x02\x03",

            "#0001F（慎重に、確実に仕掛けよう。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F9")
    Sound(828, 0, 100, 0)

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※魔獣の姿は、遠くからでは見えません。\x01",
            "  ある程度近づくと姿が見えるようになります。\x02\x03",

            "※接触の仕方によって、戦闘開始時の状況が変化します。\x01",
            "  魔獣の背後から接触すれば有利に、\x01",
            "  自分たちの背後を取られると不利になります。\x02\x03",

            "※また、フィールド移動中に○ボタンを押すと、\x01",
            "  先頭のキャラクターが\x01",
            "  敵を攻撃するアクションを取ります。\x02\x03",

            "※攻撃を魔獣の背中にヒットさせると\x01",
            "  魔獣を気絶させて、動きを止めることができます。\x02\x03",

            "※魔獣が気絶した状態で接触すれば、\x01",
            "  より有利な状態で戦闘を開始することができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    label("loc_33F9")

    OP_CA(0x1, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x0, 0, 0, 87500, 0)
    SetScenarioFlags(0x40, 4)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_23_300A end

    def Function_24_3423(): pass

    label("Function_24_3423")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    OP_68(-2120, 2000, 94220, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, -900, 0, 94300, 0)
    SetChrPos(0x102, 400, 0, 94300, 0)
    SetChrPos(0x103, -1600, 0, 92800, 0)
    SetChrPos(0x104, 1100, 0, 92800, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis006.itp")
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetCameraDistance(19000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0055
    ChrTalk(
        0x101,
        "#0000F#11Pよし……何とか倒せたか。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#0304F#11Pま、そこまで手強い\x01",
            "相手じゃなかったみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0057
    ChrTalk(
        0x102,
        (
            "#0104F#11Pでも、これでお互いのスタイルも\x01",
            "何となく掴めたわね。\x02\x03",

            "#0100Fティオちゃんの魔導杖の性能は\x01",
            "ちょっと驚かされたけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-2160, 2000, 92630, 1500)

    def lambda_3652():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3652)
    Sleep(50)

    def lambda_3662():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3662)
    Sleep(50)

    def lambda_3672():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3672)
    OP_6F(0x1)

    #C0058
    ChrTalk(
        0x101,
        (
            "#0000F#5P……確かに。\x02\x03",

            "あの杖から放たれたのは\x01",
            "やっぱり魔法#4Rアーツ#のたぐいなのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0059
    ChrTalk(
        0x103,
        (
            "#0203F#6Pええ、そうなりますね。\x02\x03",

            "#0200F通常のアーツと違って\x01",
            "外す可能性はありますが……\x02\x03",

            "駆動時間なしに近距離のアーツを\x01",
            "発動しているのと同じ効果です。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#0300F#11Pふむ、そうなると\x01",
            "色々と戦術に幅が出そうだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)

    #C0061
    ChrTalk(
        0x103,
        (
            "#0204F#6P#Nそのための新装備です。\x02\x03",

            "#0200Fそれと、わたしが付けている\x01",
            "この胸甲ですが──\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #A0062
    AnonymousTalk(
        0x103,
        (
            "#0200F#6P──魔導杖と連動して\x01",
            "一種の防御フィールドを\x01",
            "展開する働きを持っています。\x02\x03",

            "#0204F見た目より打たれ強いので\x01",
            "前に出ても問題はないかと……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0063
    ChrTalk(
        0x102,
        (
            "#0102F#5Pなるほど……\x01",
            "まさに最先端の装備ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#0309Fま、せいぜい頼りに\x01",
            "させてもらうとしようかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#0008F#5Pうーん、でもなぁ……\x02\x03",

            "女の子を矢面に\x01",
            "立たせるのはちょっと……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0066
    ChrTalk(
        0x103,
        "#0211F#12P（ジロリ……）\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        "#0012F#5P……いえ、何でもありません。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -900, 0, 94300, 0)
    ClearScenarioFlags(0x0, 2)
    SetScenarioFlags(0x40, 5)
    ModifyEventFlags(0, 2, 0x80)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_37()
    ClearMapFlags(0x8000000)
    Call(0, 7)
    EventEnd(0x5)
    Return()

    # Function_24_3423 end

    def Function_25_3A3D(): pass

    label("Function_25_3A3D")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    #C0068
    ChrTalk(
        0x101,
        (
            "#0001Fこのパーティでの初実戦だ。\x02\x03",

            "感触を確かめるためにも、\x01",
            "逃げずに戦いを挑んでみよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -150, 0, 111280, 180)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_25_3A3D end

    def Function_26_3ABF(): pass

    label("Function_26_3ABF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_68(-100220, 2000, 197860, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(17850, 0)
    SetCameraDistance(16850, 2000)
    SetChrPos(0x101, -95300, 0, 199300, 270)
    SetChrPos(0x102, -95300, 0, 200500, 270)
    SetChrPos(0x103, -94100, 0, 199300, 270)
    SetChrPos(0x104, -94100, 0, 200500, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0069
    ChrTalk(
        0x104,
        (
            "#0305F#12Pおっと……なにやら\x01",
            "プヨプヨしたのがいやがるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#0001F#12Pああいう魔獣には、武器での攻撃よりも\x01",
            "導力魔法#8Rア  ー  ツ#の方が有効だろう。\x02\x03",

            "#0000Fみんな、通常攻撃だけじゃなく\x01",
            "アーツも使って戦おう。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        "#0100F#12Pええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        "#0204F#12P了解です。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x0, -95300, 0, 199300, 270)
    SetScenarioFlags(0x44, 1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_26_3ABF end

    def Function_27_3C98(): pass

    label("Function_27_3C98")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    #C0073
    ChrTalk(
        0x101,
        (
            "#0001F魔獣に戦いを挑んでみよう。\x02\x03",

            "#0000Fあの魔獣は厄介そうだけど……\x01",
            "攻撃アーツを使えば必ず倒せるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -108410, 0, 199890, 90)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_27_3C98 end

    def Function_28_3D2C(): pass

    label("Function_28_3D2C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_68(-198820, 1150, 198900, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20170, 0)
    SetCameraDistance(19170, 2000)
    SetChrPos(0x101, -195700, 0, 199000, 270)
    SetChrPos(0x102, -195700, 0, 200200, 270)
    SetChrPos(0x103, -194500, 0, 199000, 270)
    SetChrPos(0x104, -194500, 0, 200200, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0074
    ChrTalk(
        0x101,
        (
            "#0000F#12Pよし、今度は戦技#4Rクラフト#を使って\x01",
            "戦ってみよう。\x02\x03",

            "アーツと組み合わせれば\x01",
            "戦術の幅がかなり広がるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        "#0204F#12Pええ、やってみましょう。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#0304F#12Pフッフッフ、見せ場が来やがったな。\x02\x03",

            "#0309F俺様の必殺技で派手にきめてやるぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#0106F#12Pふう、調子に乗って\x01",
            "怪我しないようにね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x0, -195700, 0, 199000, 270)
    SetScenarioFlags(0x44, 2)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_28_3D2C end

    def Function_29_3F2B(): pass

    label("Function_29_3F2B")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    #C0078
    ChrTalk(
        0x101,
        (
            "#0000F今度はクラフトで\x01",
            "魔獣と戦ってみよう。\x02\x03",

            "皆の得意な技も確かめないとな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -200160, 0, 205020, 180)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_29_3F2B end

    def Function_30_3FA1(): pass

    label("Function_30_3FA1")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    #C0079
    ChrTalk(
        0x101,
        (
            "#0000F今度はクラフトで\x01",
            "魔獣と戦ってみよう。\x02\x03",

            "皆の得意な技も確かめないとな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -200060, 0, 194270, 0)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_30_3FA1 end

    def Function_31_4017(): pass

    label("Function_31_4017")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0xB, 0x80)
    OP_68(-200470, 2000, 288110, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22670, 0)
    SetCameraDistance(21670, 2000)
    SetChrPos(0x101, -199200, 0, 287270, 0)
    SetChrPos(0x102, -200610, 0, 287270, 0)
    SetChrPos(0x103, -200610, 0, 285570, 0)
    SetChrPos(0x104, -199200, 0, 285570, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0080
    ChrTalk(
        0x104,
        (
            "#0305Fおっと……まだいやがったか。\x02\x03",

            "#0306Fチマチマ戦うのも\x01",
            "面倒になってきたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0003Fなら、Ｓクラフトを使ってみようか。\x02\x03",

            "#0001FＳクラフトやＳブレイクを使えば\x01",
            "大抵の魔獣は一撃で倒せるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        (
            "#0203FＣＰが１００を超えると\x01",
            "使える大技ですね。\x02\x03",

            "#0201F了解です。\x01",
            "戦闘にも慣れてきましたし\x01",
            "使ってみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#0102F私は回復系の\x01",
            "Ｓクラフトを持っているから、\x01",
            "危なくなったら声をかけて頂戴ね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x0, -200070, 0, 286380, 0)
    SetScenarioFlags(0x49, 3)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_31_4017 end

    def Function_32_4274(): pass

    label("Function_32_4274")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    #C0084
    ChrTalk(
        0x101,
        (
            "#0000F今度はＳクラフトを使ってみよう。\x02\x03",

            "強力な大技だから、\x01",
            "大抵の魔獣は一撃で倒せるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -200300, 0, 316760, 180)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_32_4274 end

    def Function_33_42FA(): pass

    label("Function_33_42FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-100000, 2100, -8800, 0)
    MoveCamera(40, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_90(0x101, -99400, 3800, -12600, 0)
    OP_90(0x103, -100600, 3800, -13300, 0)

    def lambda_435D():
        OP_96(0xFE, 0xFFFE7708, 0x0, 0xFFFFED40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_435D)
    Sleep(50)

    def lambda_437A():
        OP_96(0xFE, 0xFFFE7BB8, 0x0, 0xFFFFED40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_437A)
    OP_68(-100000, 1100, -4800, 4000)
    MoveCamera(40, 25, 0, 4000)
    SetCameraDistance(19500, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)

    #C0085
    ChrTalk(
        0x101,
        (
            "#12P#0001Fさてと……Ａ区画の下層というと\x01",
            "右にあるエレベーターを降りるんだったか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 3)), scpexpr(EXPR_END)), "loc_44E0")

    #C0086
    ChrTalk(
        0x103,
        (
            "#6P#0203Fはい。\x02\x03",

            "#0200F降りた先の奥に、ロックされた\x01",
            "エレベーターがあったのを\x01",
            "覚えていますか？\x02\x03",

            "認証コードを打ち込めば起動するので\x01",
            "そこから下層エリアに行けるはずです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4585")

    label("loc_44E0")


    #C0087
    ChrTalk(
        0x103,
        (
            "#6P#0203Fはい。\x02\x03",

            "#0200F降りた先の奥に、ロックされた\x01",
            "エレベーターが１基あるんですが……\x02\x03",

            "認証コードを打ち込めば起動するので\x01",
            "そこから下層エリアに行けるはずです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4585")

    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0088
    ChrTalk(
        0x101,
        "#6P#0000Fなるほど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    TurnDirection(0x101, 0x103, 500)

    #C0089
    ChrTalk(
        0x101,
        (
            "#0005F#11Pって、認証コードなんか\x01",
            "どうやって手に入れたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x103,
        (
            "#6P#0203F以前、ＩＢＣの端末で\x01",
            "ヨナの居場所を突き止めた時に\x01",
            "偶然手に入れました。\x02\x03",

            "多分、そのまま使えると思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0091
    ChrTalk(
        0x101,
        (
            "#0001F#11P……大丈夫なのか？\x01",
            "勝手に使ったりして。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        (
            "#6P#0204Fジオフロントそのものは\x01",
            "クロスベル市の施設ですから\x01",
            "法的には問題ないかと……\x02\x03",

            "#0202F単に、問い合わせの手順を\x01",
            "短縮しただけのことです。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#0012F#11Pそ、そういうもんか？\x02\x03",

            "#0000Fうーん……まあいいか。\x01",
            "とにかく降りてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        "#6P#0202Fはい。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -100000, 0, -4800, 0)
    SetScenarioFlags(0xA0, 6)
    OP_C7(0x0, 0x1000)
    OP_29(0x45, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4814")
    OP_29(0x1D, 0x4, 0x40)
    Jump("loc_4826")

    label("loc_4814")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4826")
    OP_29(0x1D, 0x4, 0x40)

    label("loc_4826")

    OP_E0(0x0)
    Call(0, 7)
    EventEnd(0x5)
    Return()

    # Function_33_42FA end

    def Function_34_482E(): pass

    label("Function_34_482E")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48F6")

    #C0095
    ChrTalk(
        0x102,
        (
            "#0100Fロイド、もう一人の子を\x01",
            "探さなくていいの……？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#0000Fそ、そうだな。\x01",
            "何かあってからじゃ遅い……\x02\x03",

            "今はもう一人の子供を捜そう。\x01",
            "多分下のフロアにいるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AEC")

    label("loc_48F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4999")

    #C0097
    ChrTalk(
        0x101,
        (
            "#0000F……待ってくれ。\x01",
            "今はもう一人の子供を捜さないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#0100Fそうね、状況からして\x01",
            "下のフロアに居そうだし……\x02\x03",

            "今は先を急ぎましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AEC")

    label("loc_4999")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A43")

    #C0099
    ChrTalk(
        0x101,
        (
            "#0000F……待ってくれ。\x01",
            "今はもう一人の子供を捜さないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        (
            "#0200Fそうですね。\x01",
            "状況からして\x01",
            "下のフロアに居そうですし……\x02\x03",

            "今は先を急ぎましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AEC")

    label("loc_4A43")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AEC")

    #C0101
    ChrTalk(
        0x101,
        (
            "#0000F……待ってくれ。\x01",
            "今はもう一人の子供を捜さないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#0300Fおっと、そうだな。\x01",
            "状況からして\x01",
            "下のフロアに居そうだし……\x02\x03",

            "今は先を急ぐとすっか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AEC")

    SetScenarioFlags(0x0, 0)
    Jump("loc_4B41")

    label("loc_4AF4")


    #C0103
    ChrTalk(
        0x101,
        (
            "#0000F今はもう一人の子供を\x01",
            "探さないと……\x02\x03",

            "下のフロアを捜索してみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B41")

    Sleep(50)
    SetChrPos(0x0, -100000, 0, -4500, 0)
    EventEnd(0x4)
    Return()

    # Function_34_482E end

    def Function_35_4B58(): pass

    label("Function_35_4B58")

    TalkBegin(0xFF)
    SetChrName("")

    #A0104
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉はロックされており、\x01",
            "開きそうもない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_35_4B58 end

    def Function_36_4B93(): pass

    label("Function_36_4B93")

    TalkBegin(0xFF)
    SetChrName("")

    #A0105
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉はロックされており、\x01",
            "開きそうもない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_36_4B93 end

    SaveToFile()

Try(main)
