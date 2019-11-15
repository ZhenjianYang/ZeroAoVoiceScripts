from ZeroScenarioHelper import *

def main():
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
        "魔兽",                   # 1
        "魔兽",                   # 2
        "魔兽",                   # 3
        "魔兽",                   # 4
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

    Sepith("Sepith_4852", 2,   0,   3,   2,   1,   0,   2)
    Sepith("Sepith_483A", 3,   1,   2,   0,   1,   2,   1)
    Sepith("Sepith_484A", 1,   4,   0,   2,   0,   2,   1)
    Sepith("Sepith_4842", 1,   2,   0,   4,   1,   1,   0)

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
        "BattleInfo_914", 0x0000, 3, 6, 45, 10, 1, 40, 0, "bm0001", "Sepith_4852", 75, 25, 0, 0,
        (
            ("ms61700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_790", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_6E0"),
            ("ms61700.dat", "ms61700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_770", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_6E0"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7F0", 0x0000, 3, 6, 45, 6, 1, 40, 0, "bm0001", "Sepith_483A", 75, 25, 0, 0,
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
        "BattleInfo_8D0", 0x0000, 3, 6, 45, 6, 1, 25, 0, "bm0001", "Sepith_484A", 100, 0, 0, 0,
        (
            ("ms73100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_790", "MonsterBattlePostion_7D0", "ed7400", "ed7403", "ATBonus_6E0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_860", 0x0000, 3, 6, 45, 6, 1, 30, 0, "bm0001", "Sepith_4842", 75, 25, 0, 0,
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
        "Function_10_1535",        # 0A, 10
        "Function_11_1639",        # 0B, 11
        "Function_12_176F",        # 0C, 12
        "Function_13_181C",        # 0D, 13
        "Function_14_190F",        # 0E, 14
        "Function_15_1D3C",        # 0F, 15
        "Function_16_1EC0",        # 10, 16
        "Function_17_2007",        # 11, 17
        "Function_18_218B",        # 12, 18
        "Function_19_22C8",        # 13, 19
        "Function_20_244C",        # 14, 20
        "Function_21_2593",        # 15, 21
        "Function_22_2D0E",        # 16, 22
        "Function_23_2E2E",        # 17, 23
        "Function_24_31F5",        # 18, 24
        "Function_25_37B3",        # 19, 25
        "Function_26_3835",        # 1A, 26
        "Function_27_39F2",        # 1B, 27
        "Function_28_3A7E",        # 1C, 28
        "Function_29_3C5F",        # 1D, 29
        "Function_30_3CCF",        # 1E, 30
        "Function_31_3D3F",        # 1F, 31
        "Function_32_3F7A",        # 20, 32
        "Function_33_3FF8",        # 21, 33
        "Function_34_44C4",        # 22, 34
        "Function_35_47BC",        # 23, 35
        "Function_36_47E7",        # 24, 36
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14EC")
    Sound(14, 0, 100, 0)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F4, 1)"), scpexpr(EXPR_END)), "loc_147E")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10A, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_14E7")

    label("loc_147E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14E7")

    Jump("loc_1529")

    label("loc_14EC")

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

    label("loc_1529")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_13FF end

    def Function_10_1535(): pass

    label("Function_10_1535")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160A")
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
            "#56I地之耀晶片×２０\x01\x07\x02",

            "#57I水之耀晶片×２０\x01\x07\x02",

            "#58I火之耀晶片×２０\x01\x07\x02",

            "#59I风之耀晶片×２０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10A, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1627")

    label("loc_160A")


    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1627")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1535 end

    def Function_11_1639(): pass

    label("Function_11_1639")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1726")
    Sound(14, 0, 100, 0)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_16B8")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10A, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1721")

    label("loc_16B8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0007
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
    OP_71(0x11, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1721")

    Jump("loc_1763")

    label("loc_1726")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
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

    label("loc_1763")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1639 end

    def Function_12_176F(): pass

    label("Function_12_176F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17ED")
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
            "#14I烟雾弹×５\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10A, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_180A")

    label("loc_17ED")


    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_180A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_176F end

    def Function_13_181C(): pass

    label("Function_13_181C")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0011
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F1")
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

    label("loc_18F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_190D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_190D")

    Return()

    # Function_13_181C end

    def Function_14_190F(): pass

    label("Function_14_190F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CC4")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A50")

    #C0012
    ChrTalk(
        0x101,
        (
            "#0005F这种地方居然有\x01",
            "通向地面的梯子啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#0200F上面好像是地下道的出入口呢。\x01",
            "……不过在数据库中\x01",
            "并没有记载。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        "#0305F为什么是打开的啊？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#0103F这个……也许是管理这里的\x01",
            "市政厅职员忘记把它关闭了吧。\x02\x03",

            "#0100F稍后还是和他们\x01",
            "联络一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#0003F是啊……就这么办吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 3)
    Jump("loc_1CBC")

    label("loc_1A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9B")

    #C0017
    ChrTalk(
        0x101,
        (
            "#0005F这种地方居然有\x01",
            "通向地面的梯子啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        (
            "#0200F上面好像是地下道的出入口呢。\x01",
            "……不过在数据库中\x01",
            "并没有记载。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，原来如此，\x01",
            "是从这里进来的吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x197,
        (
            "对、对不起……\x01",
            "擅自就跑进来……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#0100F现在说这些也没用了呢。\x02\x03",

            "比起这个，当务之急还是\x01",
            "赶快去找你的朋友吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x197,
        "是、是的……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C6F")

    label("loc_1B9B")

    SetChrName("")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有个通向外部的梯子。\x02\x03",

            "似乎连接着中央广场的地下道出入口。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0024
    ChrTalk(
        0x197,
        (
            "对、对不起……\x01",
            "我们擅自就\x01",
            "跑进来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#0100F现在说这些也没用了呢。\x02\x03",

            "比起这个，当务之急还是\x01",
            "赶快去找你的朋友吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x197,
        "是、是的……！\x02",
    )

    CloseMessageWindow()

    label("loc_1C6F")

    SetScenarioFlags(0x4B, 1)
    Jump("loc_1CBC")

    label("loc_1C77")

    SetChrName("")

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有个通向外部的梯子。\x02\x03",

            "似乎连接着中央广场的地下道出入口。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1CBC")

    TalkEnd(0xFF)
    Jump("loc_1D3B")

    label("loc_1CC4")

    EventBegin(0x1)

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个梯子。\x01",
            "要上去吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D29")
    EventEnd(0x5)
    NewScene("c010C", 111, 0, 0)
    IdleLoop()
    Jump("loc_1D34")

    label("loc_1D29")

    EventEnd(0x5)
    NewScene("c0100", 111, 0, 0)
    IdleLoop()

    label("loc_1D34")

    Jump("loc_1D3B")

    label("loc_1D39")

    EventEnd(0x5)

    label("loc_1D3B")

    Return()

    # Function_14_190F end

    def Function_15_1D3C(): pass

    label("Function_15_1D3C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0029
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB8")
    Fade(500)
    SetChrPos(0x0, 99400, 0, 600, 0)
    SetChrPos(0x1, 100600, 0, 600, 0)
    SetChrPos(0x2, 99400, 0, -600, 0)
    SetChrPos(0x3, 100600, 0, -600, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E16")
    SetChrPos(0x4, 99400, 0, -1800, 0)
    SetChrPos(0x5, 100600, 0, -1800, 0)
    Jump("loc_1E35")

    label("loc_1E16")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E35")
    SetChrPos(0x4, 100000, 0, -1800, 0)

    label("loc_1E35")

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

    label("loc_1EB8")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_1D3C end

    def Function_16_1EC0(): pass

    label("Function_16_1EC0")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F95")
    OP_90(0x4, 99400, 0, -1800, 0)
    OP_90(0x5, 100600, 0, -1800, 0)
    Jump("loc_1FB4")

    label("loc_1F95")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB4")
    OP_90(0x4, 100000, 0, -1800, 0)

    label("loc_1FB4")

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

    # Function_16_1EC0 end

    def Function_17_2007(): pass

    label("Function_17_2007")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0030
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2183")
    Fade(500)
    SetChrPos(0x0, 99400, 0, 100600, 0)
    SetChrPos(0x1, 100600, 0, 100600, 0)
    SetChrPos(0x2, 99400, 0, 99400, 0)
    SetChrPos(0x3, 100600, 0, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20E1")
    SetChrPos(0x4, 99400, 0, 98200, 0)
    SetChrPos(0x5, 100600, 0, 98200, 0)
    Jump("loc_2100")

    label("loc_20E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2100")
    SetChrPos(0x4, 100000, 0, 98200, 0)

    label("loc_2100")

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

    label("loc_2183")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_2007 end

    def Function_18_218B(): pass

    label("Function_18_218B")
    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2256")
    OP_90(0x4, 99400, 0, 98200, 0)
    OP_90(0x5, 100600, 0, 98200, 0)
    Jump("loc_2275")

    label("loc_2256")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2275")
    OP_90(0x4, 100000, 0, 98200, 0)

    label("loc_2275")

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

    # Function_18_218B end

    def Function_19_22C8(): pass

    label("Function_19_22C8")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0031
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2444")
    Fade(500)
    SetChrPos(0x0, 600, 0, 399400, 90)
    SetChrPos(0x1, 600, 0, 400600, 90)
    SetChrPos(0x2, -600, 0, 399400, 90)
    SetChrPos(0x3, -600, 0, 400600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23A2")
    SetChrPos(0x4, -1800, 0, 399400, 90)
    SetChrPos(0x5, -1800, 0, 400600, 90)
    Jump("loc_23C1")

    label("loc_23A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C1")
    SetChrPos(0x4, -1800, 0, 400000, 90)

    label("loc_23C1")

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

    label("loc_2444")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_19_22C8 end

    def Function_20_244C(): pass

    label("Function_20_244C")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2521")
    OP_90(0x4, -1800, 0, 399400, 90)
    OP_90(0x5, -1800, 0, 400600, 90)
    Jump("loc_2540")

    label("loc_2521")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2540")
    OP_90(0x4, -1800, 0, 400000, 90)

    label("loc_2540")

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

    # Function_20_244C end

    def Function_21_2593(): pass

    label("Function_21_2593")

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
        "#5P#0001F这里就是『地下空间』……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#11P#0101F虽然之前也有所耳闻，\x01",
            "但真没想到都市的地下\x01",
            "还会有如此广阔的现代化区域……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        (
            "#7P#0305F哈～真让人吃惊呀。\x02\x03",

            "本来还以为会是残存多年的\x01",
            "中世纪地下水道呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#6P#0200F根据数据库中的记录，\x01",
            "这里似乎是与二十年前的都市计划\x01",
            "同时开始建造的场所。\x02\x03",

            "除了供水管道、污水管道、\x01",
            "垃圾处理设施之外，之后好像\x01",
            "还增设了导力缆线及各种相关设备。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_27EF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27EF)
    Sleep(150)

    def lambda_27FF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_27FF)
    Sleep(50)

    def lambda_280F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_280F)
    Sleep(50)

    def lambda_281F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_281F)
    WaitChrThread(0x103, 2)

    #C0036
    ChrTalk(
        0x101,
        (
            "#5P#0006F……嗯，这里确实\x01",
            "算是预料之外的场所。\x02\x03",

            "#0001F不过，上面好像就是\x01",
            "中央广场一带吧？\x02\x03",

            "广场下面居然就有魔兽在徘徊吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#6P#0203F这里平时都处于封锁状态，\x01",
            "所以魔兽并不会在都市中出现……\x02\x03",

            "不过，听说偶尔也会发生工程现场\x01",
            "的作业人员遭受袭击的事件。\x02\x03",

            "#0200F但目前，警察局方面似乎\x01",
            "并没有余力采取充分的应对措施。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#5P#0008F……是吗………\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#11P#0101F所以才需要我们特别任务支援科……\x01",
            "就是这么回事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#7P#0304F哈，这么解释的话，\x01",
            "也就容易理解了啊。\x02",
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
            "#5P#0003F──情况已经明白了。\x02\x03",

            "#0001F暂且不说这是否属于搜查官的职责范围，\x01",
            "总之，确实是必须处理的工作。\x02\x03",

            "把它当作测试也好，别的也罢，\x01",
            "让我们把它认真完成吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        "#12P#0309F噢～噢～真够正经的啊。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        (
            "#11P#0104F不过，确实如此。\x02\x03",

            "#0100F仔细熟悉每一步基本要领，\x01",
            "脚踏实地地稳妥前进吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        "#6P#0203F……了解。\x02",
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

    def lambda_2B96():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B96)
    Sleep(150)

    def lambda_2BA6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2BA6)
    Sleep(50)

    def lambda_2BB6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2BB6)
    Sleep(50)

    def lambda_2BC6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2BC6)
    WaitChrThread(0x103, 2)
    CloseMessageWindow()
    OP_6F(0x79)
    Sound(828, 0, 100, 0)

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※这是安置在危险区域的\x01",
            "  导力回复装置。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※按○键调查此装置，并选择  \x01",
            "  『在这里休息』后，\x01",
            "  就可以恢复全部ＨＰ、ＥＰ值。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※当队伍陷入危险状况时，\x01",
            "  可以来此处进行回复。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0048
    ChrTalk(
        0x101,
        (
            "#11P#0000F（好，如果遇到了什么危险，\x01",
            "  就回到这里进行回复吧。）\x02",
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

    # Function_21_2593 end

    def Function_22_2D0E(): pass

    label("Function_22_2D0E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_2D39")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D91")

    label("loc_2D39")

    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "要观看战斗教程吗？",
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
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_2D91")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2DA7"),
        (1, "loc_2DB2"),
        (SWITCH_DEFAULT, "loc_2E14"),
    )


    label("loc_2DA7")

    SetScenarioFlags(0x49, 5)
    Call(0, 23)
    Jump("loc_2E23")

    label("loc_2DB2")

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
    Jump("loc_2E23")

    label("loc_2E14")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E23")

    label("loc_2E23")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_2D0E end

    def Function_23_2E2E(): pass

    label("Function_23_2E2E")

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
        "#0101F#5P（……出现了……！）\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        "#0301F#5P（这么快就出来了啊。）\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#0201F#5P（……那就是魔兽……）\x02",
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
            "#0003F#5P（这是我们这组阵容的初次实战……）\x02\x03",

            "#0001F（慎重小心地迎战吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CB")
    Sound(828, 0, 100, 0)

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※在太远的距离是无法看到魔兽的。\x01",
            "  拉近一定距离之后，魔兽就会现形。\x02\x03",

            "※根据接触方式的不同，战斗开始时的状况会发生变化。\x01",
            "  接触魔兽的背后而进入战斗，战局会对我方有利，\x01",
            "  如果被魔兽从背后接触到自己，则会陷入不利的战况。\x02\x03",

            "※此外，在场景移动中按下○键，  \x01",
            "  排列在队首的角色\x01",
            "  便会向敌人发起直接攻击。\x02\x03",

            "※如果攻击魔兽的背后，\x01",
            "  便可使其陷入气绝状态，进而停止行动。\x02\x03",

            "※与陷入气绝状态的魔兽接触，\x01",
            "  便能以更加有利的状态开始战斗。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    label("loc_31CB")

    OP_CA(0x1, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x0, 0, 0, 87500, 0)
    SetScenarioFlags(0x40, 4)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_23_2E2E end

    def Function_24_31F5(): pass

    label("Function_24_31F5")

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
        "#0000F#11P好……总算是打倒了啊。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#0304F#11P哈，好像也不是\x01",
            "那么难对付的对手嘛。\x02",
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
            "#0104F#11P不过，借此机会，大家倒是互相\x01",
            "熟悉了一下彼此的战斗习惯呢。\x02\x03",

            "#0100F缇欧那魔导杖的性能\x01",
            "倒真是让我吃了一惊……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-2160, 2000, 92630, 1500)

    def lambda_340E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_340E)
    Sleep(50)

    def lambda_341E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_341E)
    Sleep(50)

    def lambda_342E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_342E)
    OP_6F(0x1)

    #C0058
    ChrTalk(
        0x101,
        (
            "#0000F#5P……确实。\x02\x03",

            "从那根法杖中施放出来的，\x01",
            "果然是魔法之类的吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0059
    ChrTalk(
        0x103,
        (
            "#0203F#6P嗯，确实没错。\x02\x03",

            "#0200F虽然和普通的魔法不同，\x01",
            "存在打偏的可能性……\x02\x03",

            "但并不需要驱动时间，所以其效果\x01",
            "与近距离魔法相同。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#0300F#11P嗯，这样一来，我们的战术\x01",
            "好像就变得更加多样化了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)

    #C0061
    ChrTalk(
        0x103,
        (
            "#0204F#6P#N这件新装备的目的也正是如此。\x02\x03",

            "#0200F还有，我身上穿戴的\x01",
            "这件胸甲──\x02",
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
            "#0200F#6P──可以和魔导杖进行联动，\x01",
            "进而启动\x01",
            "展开防御力场的功能。\x02\x03",

            "#0204F抗击打能力要比看上去强得多，\x01",
            "所以，就算把我安排在前线位置应该也没问题……\x02",
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
            "#0102F#5P原来如此……\x01",
            "还真是最先进的装备啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#0309F哈，那以后就要\x01",
            "多多依靠你啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#0008F#5P嗯～不过……\x02\x03",

            "要是让女孩子挡在我们\x01",
            "前面，果然还是有点……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0066
    ChrTalk(
        0x103,
        "#0211F#12P（瞪……）\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        "#0012F#5P……不，我什么都没说。\x02",
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

    # Function_24_31F5 end

    def Function_25_37B3(): pass

    label("Function_25_37B3")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    #C0068
    ChrTalk(
        0x101,
        (
            "#0001F这是我们这组阵容的初次实战。\x02\x03",

            "为了找找感觉，熟悉战斗，\x01",
            "还是不要逃跑，全力迎战吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -150, 0, 111280, 180)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_25_37B3 end

    def Function_26_3835(): pass

    label("Function_26_3835")

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
            "#0305F#12P噢……这家伙看起来\x01",
            "好像又软又有弹性啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#0001F#12P对付这种类型的魔兽，比起使用武器\x01",
            "攻击，还是导力魔法更加有效吧。\x02\x03",

            "#0000F各位，不要光用普通攻击，\x01",
            "也试着用魔法来战斗吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        "#0100F#12P嗯，说得也是呢。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        "#0204F#12P了解。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x0, -95300, 0, 199300, 270)
    SetScenarioFlags(0x44, 1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_26_3835 end

    def Function_27_39F2(): pass

    label("Function_27_39F2")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    #C0073
    ChrTalk(
        0x101,
        (
            "#0001F试着与魔兽交战吧。\x02\x03",

            "#0000F那只魔兽虽然看起来很危险……\x01",
            "但只要使用攻击魔法，应该就可以打倒。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -108410, 0, 199890, 90)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_27_39F2 end

    def Function_28_3A7E(): pass

    label("Function_28_3A7E")

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
            "#0000F#12P好，这次我们就\x01",
            "尝试使用战技来战斗吧。\x02\x03",

            "与魔法组合使用的话，\x01",
            "战术手段应该就会拓展不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        "#0204F#12P嗯，试试看吧。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#0304F#12P呵呵，终于轮到我大显身手了。\x02\x03",

            "#0309F就用本大爷的必杀技将它们华丽地解决吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#0106F#12P呼，可不要得意忘形过了头，\x01",
            "不小心受伤啊。\x02",
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

    # Function_28_3A7E end

    def Function_29_3C5F(): pass

    label("Function_29_3C5F")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    #C0078
    ChrTalk(
        0x101,
        (
            "#0000F这次就用战技\x01",
            "来和魔兽战斗吧。\x02\x03",

            "必须要确认一下大家的拿手战技啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -200160, 0, 205020, 180)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_29_3C5F end

    def Function_30_3CCF(): pass

    label("Function_30_3CCF")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    #C0079
    ChrTalk(
        0x101,
        (
            "#0000F这次就用战技\x01",
            "来和魔兽战斗吧。\x02\x03",

            "必须要确认一下大家的拿手战技啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -200060, 0, 194270, 0)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_30_3CCF end

    def Function_31_3D3F(): pass

    label("Function_31_3D3F")

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
            "#0305F喔……还有吗。\x02\x03",

            "#0306F开始觉得和这种小东西战斗\x01",
            "变得相当麻烦了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0003F既然如此，我们就试试Ｓ战技吧。\x02\x03",

            "#0001F使用Ｓ战技或Ｓ爆发技的话，\x01",
            "应该就能将普通魔兽一击打倒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        (
            "#0203F就是ＣＰ值超过１００时\x01",
            "便可以使用的超级战技吧。\x02\x03",

            "#0201F了解。\x01",
            "大家差不多已经熟悉战斗了，\x01",
            "就来试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#0102F我拥有回复系的\x01",
            "Ｓ战技，如果遇到危险，\x01",
            "就让我来负责回复吧。\x02",
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

    # Function_31_3D3F end

    def Function_32_3F7A(): pass

    label("Function_32_3F7A")

    EventBegin(0x1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)

    #C0084
    ChrTalk(
        0x101,
        (
            "#0000F这次就来试试Ｓ战技吧。\x02\x03",

            "这是非常强力的超级战技，\x01",
            "应该可以将普通魔兽一击打倒。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -200300, 0, 316760, 180)
    ClearMapFlags(0x8000000)
    EventEnd(0x4)
    Return()

    # Function_32_3F7A end

    def Function_33_3FF8(): pass

    label("Function_33_3FF8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-100000, 2100, -8800, 0)
    MoveCamera(40, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_90(0x101, -99400, 3800, -12600, 0)
    OP_90(0x103, -100600, 3800, -13300, 0)

    def lambda_405B():
        OP_96(0xFE, 0xFFFE7708, 0x0, 0xFFFFED40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_405B)
    Sleep(50)

    def lambda_4078():
        OP_96(0xFE, 0xFFFE7BB8, 0x0, 0xFFFFED40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4078)
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
            "#12P#0001F那么……如果要去Ａ区域的下层，\x01",
            "应该乘坐右边的升降机下去吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 3)), scpexpr(EXPR_END)), "loc_41AE")

    #C0086
    ChrTalk(
        0x103,
        (
            "#6P#0203F是的。\x02\x03",

            "#0200F下去之后，里面有一部\x01",
            "被锁住的升降机，\x01",
            "还记得吗？\x02\x03",

            "只要输入认证代码就能启动，\x01",
            "然后便可以乘它进入下层区域了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4231")

    label("loc_41AE")


    #C0087
    ChrTalk(
        0x103,
        (
            "#6P#0203F是的。\x02\x03",

            "#0200F下去之后，里面应该\x01",
            "有一部被锁住的升降机……\x02\x03",

            "只要输入认证代码就能启动，\x01",
            "然后便可以乘它进入下层区域了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4231")

    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0088
    ChrTalk(
        0x101,
        "#6P#0000F原来如此……\x02",
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
            "#0005F#11P不过，那个什么认证代码，\x01",
            "你是怎么得到的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x103,
        (
            "#6P#0203F以前，在使用ＩＢＣ的终端\x01",
            "查找约纳的位置时，\x01",
            "偶然得到的。\x02\x03",

            "我想多半可以直接使用。\x02",
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
            "#0001F#11P……这样做没问题吗？\x01",
            "擅自就拿来使用……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        (
            "#6P#0204F地下空间本来就属于\x01",
            "克洛斯贝尔市的公共设施，所以从\x01",
            "法律方面来说，应该是没有问题的……\x02\x03",

            "#0202F现在这么做只不过是稍微简化了手续，\x01",
            "免去了申请这一步骤而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#0012F#11P是、是这样啊？\x02\x03",

            "#0000F嗯～……算了。\x01",
            "总之，我们就下去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        "#6P#0202F好的。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -100000, 0, -4800, 0)
    SetScenarioFlags(0xA0, 6)
    OP_C7(0x0, 0x1000)
    OP_29(0x45, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44AA")
    OP_29(0x1D, 0x4, 0x40)
    Jump("loc_44BC")

    label("loc_44AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44BC")
    OP_29(0x1D, 0x4, 0x40)

    label("loc_44BC")

    OP_E0(0x0)
    Call(0, 7)
    EventEnd(0x5)
    Return()

    # Function_33_3FF8 end

    def Function_34_44C4(): pass

    label("Function_34_44C4")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4760")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4584")

    #C0095
    ChrTalk(
        0x102,
        (
            "#0100F罗伊德，难道不去找\x01",
            "另外一个孩子吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#0000F也、也是啊。\x01",
            "如果他发生什么意外，可就来不及了……\x02\x03",

            "现在赶快去找另一个孩子吧。\x01",
            "他多半就在下层区域。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4758")

    label("loc_4584")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_461D")

    #C0097
    ChrTalk(
        0x101,
        (
            "#0000F……等一下。\x01",
            "现在必须要去寻找另一个孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#0100F是啊，从目前的状况来看，\x01",
            "他应该就在下层区域中……\x02\x03",

            "现在赶快去找他吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4758")

    label("loc_461D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46B9")

    #C0099
    ChrTalk(
        0x101,
        (
            "#0000F……等一下。\x01",
            "现在必须要去寻找另一个孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        (
            "#0200F是啊。\x01",
            "根据如今的状况来看，\x01",
            "他应该就在下层区域中……\x02\x03",

            "现在快点去找他吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4758")

    label("loc_46B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4758")

    #C0101
    ChrTalk(
        0x101,
        (
            "#0000F……等一下。\x01",
            "现在必须要去寻找另一个孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#0300F啊，说的对。\x01",
            "按照现在的状况来看，\x01",
            "他应该就在下层区域里吧……\x02\x03",

            "现在赶快去找他吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4758")

    SetScenarioFlags(0x0, 0)
    Jump("loc_47A5")

    label("loc_4760")


    #C0103
    ChrTalk(
        0x101,
        (
            "#0000F现在必须要赶快\x01",
            "去找另一个孩子……\x02\x03",

            "去下层区域展开搜索吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47A5")

    Sleep(50)
    SetChrPos(0x0, -100000, 0, -4500, 0)
    EventEnd(0x4)
    Return()

    # Function_34_44C4 end

    def Function_35_47BC(): pass

    label("Function_35_47BC")

    TalkBegin(0xFF)
    SetChrName("")

    #A0104
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁，\x01",
            "无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_35_47BC end

    def Function_36_47E7(): pass

    label("Function_36_47E7")

    TalkBegin(0xFF)
    SetChrName("")

    #A0105
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁，\x01",
            "无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_36_47E7 end

    SaveToFile()

Try(main)
