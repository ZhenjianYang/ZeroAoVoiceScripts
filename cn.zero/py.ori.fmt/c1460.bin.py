from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1460.bin",                # FileName
        "c1460",                    # MapName
        "c1460",                    # Location
        0x0034,                     # MapIndex
        "ed7302",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 52, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1460",                  # 0
        "瓦鲁多",                 # 1
        "艾莉",                   # 2
        "缇欧",                   # 3
        "魔兽",                   # 4
        "魔兽",                   # 5
        "魔兽",                   # 6
        "魔兽",                   # 7
        "魔兽",                   # 8
        "勇猛·小鼠",             # 9
        "bc1470",                 # 10
        "bc1470",                 # 11
        "bc1460",                 # 12
        "bc1460",                 # 13
        "bc1470",                 # 14
        "bc1460",                 # 15
    ))

    ATBonus("ATBonus_4F0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_510", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_530", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_534", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_538", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_53C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_540", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_544", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_548", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_54C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_5C4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 5, 5, 45)

    # monster count: 9

    BattleInfo(
        "BattleInfo_658", 0x0400, 14, 6, 45, 10, 1, 40, 0, "bc1460", 0x00000000, 100, 0, 0, 0,
        (
            ("ms69001.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, 0, 0, 0, "MonsterBattlePostion_530", "MonsterBattlePostion_5B0", "ed7400", "ed7403", "ATBonus_4F0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_69C", 0x0400, 14, 6, 45, 10, 1, 30, 0, "bc1460", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62001.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, 0, 0, 0, "MonsterBattlePostion_530", "MonsterBattlePostion_5B0", "ed7400", "ed7403", "ATBonus_4F0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5D0", 0x0400, 14, 6, 45, 10, 1, 40, 0, "bc1470", 0x00000000, 100, 0, 0, 0,
        (
            ("ms69001.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, 0, 0, 0, "MonsterBattlePostion_530", "MonsterBattlePostion_5B0", "ed7400", "ed7403", "ATBonus_4F0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_614", 0x0400, 14, 6, 45, 10, 1, 30, 0, "bc1470", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62001.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, 0, 0, 0, "MonsterBattlePostion_530", "MonsterBattlePostion_5B0", "ed7400", "ed7403", "ATBonus_4F0"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_6E0", 0x0000, 14, 6, 45, 0, 1, 0, 0, "bc1470", 0x00000000, 100, 0, 0, 0,
        (
            ("ms69001.dat", "ms69001.dat", "ms69001.dat", "ms69001.dat", 0, 0, 0, 0, "MonsterBattlePostion_530", "MonsterBattlePostion_5B0", "ed7401", "ed7403", "ATBonus_4F0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_724", 0x0012, 15, 6, 45, 0, 1, 0, 0, "bc1460", 0x00000000, 100, 0, 0, 0,
        (
            ("ms64900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", "ms75900.dat", 0, "MonsterBattlePostion_530", "MonsterBattlePostion_5B0", "ed7401", "ed7403", "ATBonus_510"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00200.itc",                   # 01
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
        "monster/ch64950.itc",               # 14
        "monster/ch64951.itc",               # 15
        "monster/ch75950.itc",               # 16
    ))

    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(1750,    0,       1500,    270,  389,  0x0, 0,   0,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(1750,    0,       3000,    315,  389,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-100000, 800,     211000,  0,    389,  0x0, 0,   20,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-102519, 0,       212080,  45,   389,  0x0, 0,   22,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-97589,  0,       212080,  315,  389,  0x0, 0,   22,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-101849, 29,      209210,  0,    389,  0x0, 0,   22,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-98279,  29,      209210,  0,    389,  0x0, 0,   22,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-84000,  4000,    156000,  0,    484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(6980,    54510,   30,      0x1010000,    "BattleInfo_658", 887, 16,  0xFFFF, 0,  1)
    DeclMonster(55560,   6870,    30,      0x1010000,    "BattleInfo_69C", 888, 18,  0xFFFF, 2,  3)
    DeclMonster(-117250, -610,    0,       0x1010000,    "BattleInfo_5D0", 889, 16,  0xFFFF, 0,  1)
    DeclMonster(-104370, 56030,   30,      0x1010000,    "BattleInfo_614", 890, 18,  0xFFFF, 2,  3)
    DeclMonster(-107980, -53770,  30,      0x1010000,    "BattleInfo_658", 891, 16,  0xFFFF, 0,  1)
    DeclMonster(-96040,  159080,  0,       0x1010000,    "BattleInfo_614", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-45210,  156150,  30,      0x1010000,    "BattleInfo_658", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-108220, 98340,   0,       0x1010000,    "BattleInfo_658", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-108620, 93580,   0,       0x1010000,    "BattleInfo_69C", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 17,  -5.46999979019165,     10.09000015258789,     0.0,                   6.25,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3999999761581421,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   2.734999895095825,     -4.035999774932861,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 20,  -130.0,                0.0,                   0.0,                   16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   65.0,                  -0.0,                  -0.0,                  1.0])
    DeclEvent(0x0000, 0, 21,  -100.0,                162.0,                 3.5,                   6.25,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3999999761581421,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   50.0,                  -64.79999542236328,    -0.6999999284744263,   1.0])

    DeclActor(-110000, 0,       -51000,  1200,    -110000, 1000,    -51000,  0x007C, 0,  7,  0x0000)
    DeclActor(-100000, 0,       161000,  1200,    -100000, 1000,    161000,  0x007C, 0,  8,  0x0000)
    DeclActor(-84000,  3500,    156000,  1200,    -84000,  4500,    156000,  0x007C, 0,  9,  0x0000)
    DeclActor(57000,   0,       -500,    1200,    57000,   1000,    -500,    0x007C, 0,  10, 0x0000)
    DeclActor(-95500,  0,       57000,   1200,    -95500,  1000,    57000,   0x007C, 0,  11, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3

    ScpFunction((
        "Function_0_80C",          # 00, 0
        "Function_1_8C4",          # 01, 1
        "Function_2_8DC",          # 02, 2
        "Function_3_8FB",          # 03, 3
        "Function_4_918",          # 04, 4
        "Function_5_A31",          # 05, 5
        "Function_6_DC5",          # 06, 6
        "Function_7_F4E",          # 07, 7
        "Function_8_1084",         # 08, 8
        "Function_9_11BA",         # 09, 9
        "Function_10_13B4",        # 0A, 10
        "Function_11_149D",        # 0B, 11
        "Function_12_15A1",        # 0C, 12
        "Function_13_1748",        # 0D, 13
        "Function_14_197C",        # 0E, 14
        "Function_15_1CB4",        # 0F, 15
        "Function_16_1E3D",        # 10, 16
        "Function_17_20E3",        # 11, 17
        "Function_18_2220",        # 12, 18
        "Function_19_2F13",        # 13, 19
        "Function_20_2F2E",        # 14, 20
        "Function_21_301C",        # 15, 21
        "Function_22_32A6",        # 16, 22
        "Function_23_3560",        # 17, 23
        "Function_24_3E1D",        # 18, 24
        "Function_25_3E3C",        # 19, 25
        "Function_26_3E5B",        # 1A, 26
        "Function_27_3E7A",        # 1B, 27
        "Function_28_3E99",        # 1C, 28
    ))


    def Function_0_80C(): pass

    label("Function_0_80C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_84C"),
        (1, "loc_858"),
        (2, "loc_864"),
        (3, "loc_870"),
        (4, "loc_87C"),
        (5, "loc_888"),
        (6, "loc_894"),
        (SWITCH_DEFAULT, "loc_8A0"),
    )


    label("loc_84C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8AC")

    label("loc_858")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8AC")

    label("loc_864")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8AC")

    label("loc_870")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8AC")

    label("loc_87C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8AC")

    label("loc_888")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8AC")

    label("loc_894")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8AC")

    label("loc_8A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8AC")

    label("loc_8AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8C3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8AC")

    label("loc_8C3")

    Return()

    # Function_0_80C end

    def Function_1_8C4(): pass

    label("Function_1_8C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8DB")
    OP_A0(0xFE, 1000, 0x0, 0xFB)
    Jump("Function_1_8C4")

    label("loc_8DB")

    Return()

    # Function_1_8C4 end

    def Function_2_8DC(): pass

    label("Function_2_8DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FA")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_8DC")

    label("loc_8FA")

    Return()

    # Function_2_8DC end

    def Function_3_8FB(): pass

    label("Function_3_8FB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_917")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_3_8FB")

    label("loc_917")

    Return()

    # Function_3_8FB end

    def Function_4_918(): pass

    label("Function_4_918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_926")
    Jump("loc_A30")

    label("loc_926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_961")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_A30")

    label("loc_961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A30")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_97B")
    Jump("loc_9AC")

    label("loc_97B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_997")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_9AC")

    label("loc_997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AC")
    Event(0, 14)

    label("loc_9AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9EA")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Jump("loc_A30")

    label("loc_9EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_END)), "loc_9F8")
    SetChrFlags(0x11, 0x80)

    label("loc_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 0)), scpexpr(EXPR_END)), "loc_A06")
    SetChrFlags(0x12, 0x80)

    label("loc_A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 1)), scpexpr(EXPR_END)), "loc_A14")
    SetChrFlags(0x13, 0x80)

    label("loc_A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 2)), scpexpr(EXPR_END)), "loc_A22")
    SetChrFlags(0x14, 0x80)

    label("loc_A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 3)), scpexpr(EXPR_END)), "loc_A30")
    SetChrFlags(0x15, 0x80)

    label("loc_A30")

    Return()

    # Function_4_918 end

    def Function_5_A31(): pass

    label("Function_5_A31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4A")
    OP_10(0x0, 0x0)
    OP_10(0x19, 0x1)
    Jump("loc_A50")

    label("loc_A4A")

    OP_10(0x0, 0x1)
    OP_10(0x19, 0x0)

    label("loc_A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6C")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_A83")

    label("loc_A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A83")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_A83")

    label("loc_A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A96")
    OP_70(0x9, 0x0)
    Jump("loc_A9A")

    label("loc_A96")

    OP_70(0x9, 0x1E)

    label("loc_A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAD")
    OP_70(0xA, 0x0)
    Jump("loc_AB1")

    label("loc_AAD")

    OP_70(0xA, 0x1E)

    label("loc_AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC4")
    OP_70(0xB, 0x0)
    Jump("loc_AC8")

    label("loc_AC4")

    OP_70(0xB, 0x1E)

    label("loc_AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADB")
    OP_70(0xC, 0x0)
    Jump("loc_ADF")

    label("loc_ADB")

    OP_70(0xC, 0x1E)

    label("loc_ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF2")
    OP_70(0xD, 0x0)
    Jump("loc_AF6")

    label("loc_AF2")

    OP_70(0xD, 0x1E)

    label("loc_AF6")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_B71")
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "break", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "all01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x2)
    Jump("loc_BCA")

    label("loc_B71")

    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "break", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "all11", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA03", 0x1, 0x2)
    SetMapObjFrame(0xFF, "break", 0x1, 0x2)

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C40")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3B")
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "break", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "all01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x2)

    label("loc_C3B")

    Jump("loc_DC1")

    label("loc_C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_DC1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C5A")
    Jump("loc_DC1")

    label("loc_C5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_CD0")
    OP_1B(0x0, 0x0, 0x1C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8A")
    SetScenarioFlags(0x0, 3)
    Event(0, 22)

    label("loc_C8A")

    Jump("loc_CCB")

    label("loc_C8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC0")
    SetScenarioFlags(0x0, 2)
    OP_E0(0x0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_CC0")

    Jump("loc_CCB")

    label("loc_CC5")

    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 2)

    label("loc_CCB")

    Jump("loc_DC1")

    label("loc_CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 0)), scpexpr(EXPR_END)), "loc_D21")
    OP_1B(0x0, 0x0, 0x1C)
    ModifyEventFlags(1, 2, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D14")
    SetScenarioFlags(0x0, 2)
    OP_E0(0x0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_D14")

    Jump("loc_D1C")

    label("loc_D19")

    ClearScenarioFlags(0x0, 2)

    label("loc_D1C")

    Jump("loc_DC1")

    label("loc_D21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_D3D")
    OP_1B(0x0, 0x0, 0x1C)
    ModifyEventFlags(1, 1, 0x80)
    Jump("loc_DC1")

    label("loc_D3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_D54")
    ModifyEventFlags(1, 0, 0x80)
    Jump("loc_DC1")

    label("loc_D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_END)), "loc_DC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D9E")
    Event(0, 15)
    Jump("loc_DC1")

    label("loc_D9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DC1")
    Event(0, 16)

    label("loc_DC1")

    Call(0, 6)
    Return()

    # Function_5_A31 end

    def Function_6_DC5(): pass

    label("Function_6_DC5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE6")
    SetChrFlags(0x11, 0x8)
    Jump("loc_DEB")

    label("loc_DE6")

    ClearChrFlags(0x11, 0x8)

    label("loc_DEB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E12")
    SetChrFlags(0x12, 0x8)
    SetMapObjFlags(0xC, 0x4)
    Jump("loc_E1D")

    label("loc_E12")

    ClearChrFlags(0x12, 0x8)
    ClearMapObjFlags(0xC, 0x4)

    label("loc_E1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E59")
    SetChrFlags(0x13, 0x8)
    Jump("loc_E5E")

    label("loc_E59")

    ClearChrFlags(0x13, 0x8)

    label("loc_E5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E7C")
    SetChrFlags(0x14, 0x8)
    SetMapObjFlags(0xD, 0x4)
    Jump("loc_E87")

    label("loc_E7C")

    ClearChrFlags(0x14, 0x8)
    ClearMapObjFlags(0xD, 0x4)

    label("loc_E87")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EAE")
    SetChrFlags(0x15, 0x8)
    SetMapObjFlags(0x9, 0x4)
    Jump("loc_EB9")

    label("loc_EAE")

    ClearChrFlags(0x15, 0x8)
    ClearMapObjFlags(0x9, 0x4)

    label("loc_EB9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF8")
    SetChrFlags(0x16, 0x8)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    Jump("loc_F09")

    label("loc_EF8")

    ClearChrFlags(0x16, 0x8)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)

    label("loc_F09")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F26")
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    Jump("loc_F30")

    label("loc_F26")

    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)

    label("loc_F30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F48")
    SetChrFlags(0x17, 0x8)
    Jump("loc_F4D")

    label("loc_F48")

    ClearChrFlags(0x17, 0x8)

    label("loc_F4D")

    Return()

    # Function_6_DC5 end

    def Function_7_F4E(): pass

    label("Function_7_F4E")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_103B")
    Sound(14, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('加长枪管', 1)"), scpexpr(EXPR_END)), "loc_FCD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x4B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1036")

    label("loc_FCD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x4B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x4B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1036")

    Jump("loc_1078")

    label("loc_103B")

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

    label("loc_1078")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_F4E end

    def Function_8_1084(): pass

    label("Function_8_1084")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1171")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('珐琅凉鞋', 1)"), scpexpr(EXPR_END)), "loc_1103")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x644),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_116C")

    label("loc_1103")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x644),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x644),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_116C")

    Jump("loc_11AE")

    label("loc_1171")

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

    label("loc_11AE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1084 end

    def Function_9_11BA(): pass

    label("Function_9_11BA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1376")
    Sound(14, 0, 100, 0)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B3")
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x10, 0x0, 0)
    OP_98(0x10, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1213():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1213)

    def lambda_122D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_122D)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)

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
    WaitChrThread(0x10, 1)
    Battle("BattleInfo_6E0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1294"),
        (2, "loc_12A3"),
        (1, "loc_12B0"),
        (SWITCH_DEFAULT, "loc_12B3"),
    )


    label("loc_1294")

    SetScenarioFlags(0x74, 2)
    OP_70(0xB, 0x1E)
    Sleep(500)
    Jump("loc_12B3")

    label("loc_12A3")

    OP_70(0xB, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_12B0")

    OP_B7(0x0)
    Return()

    label("loc_12B3")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('机动战斗服', 1)"), scpexpr(EXPR_END)), "loc_130A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1371")

    label("loc_130A")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x5E1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x5E1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xB, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1371")

    Jump("loc_13A8")

    label("loc_1376")

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

    label("loc_13A8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_11BA end

    def Function_10_13B4(): pass

    label("Function_10_13B4")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146E")
    Sound(14, 0, 100, 0)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xC, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x4, 40)
    AddSepith(0x5, 40)
    AddSepith(0x6, 40)

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I时之耀晶片×４０\x01\x07\x02",

            "#61I空之耀晶片×４０\x01\x07\x02",

            "#62I幻之耀晶片×４０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x111, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_148B")

    label("loc_146E")


    #A0012
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

    label("loc_148B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_13B4 end

    def Function_11_149D(): pass

    label("Function_11_149D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1572")
    Sound(14, 0, 100, 0)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xD, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 40)
    AddSepith(0x1, 40)
    AddSepith(0x2, 40)
    AddSepith(0x3, 40)

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×４０\x01\x07\x02",

            "#57I水之耀晶片×４０\x01\x07\x02",

            "#58I火之耀晶片×４０\x01\x07\x02",

            "#59I风之耀晶片×４０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x111, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_158F")

    label("loc_1572")


    #A0014
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

    label("loc_158F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_149D end

    def Function_12_15A1(): pass

    label("Function_12_15A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1627")

    #C0015
    ChrTalk(
        0x9,
        (
            "#0100F如果魔兽想要逃跑，\x01",
            "我和缇欧会想办法处理的。\x02\x03",

            "罗伊德，兰迪，\x01",
            "你们也要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_32(0x0, 0xFC, 0x0)
    OP_32(0x3, 0xFC, 0x0)
    OP_32(0x0, 0xFD, 0x270F)
    OP_32(0x3, 0xFD, 0x270F)
    Sound(8, 0, 100, 0)
    Sleep(800)
    Jump("loc_1744")

    label("loc_1627")


    #C0016
    ChrTalk(
        0x9,
        (
            "#0100F如果魔兽想要逃跑，\x01",
            "我和缇欧会想办法处理的。\x02\x03",

            "罗伊德、兰迪，\x01",
            "他那边就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        "#0309F噢，交给我们吧！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "#0105F……对了，稍等一下。\x01",
            "我随身带着些回复药。\x02",
        )
    )

    CloseMessageWindow()
    OP_32(0x0, 0xFC, 0x0)
    OP_32(0x3, 0xFC, 0x0)
    OP_32(0x0, 0xFD, 0x270F)
    OP_32(0x3, 0xFD, 0x270F)
    Sound(8, 0, 100, 0)
    Sleep(800)

    #C0019
    ChrTalk(
        0x9,
        "#0100F你们两个，可不要太乱来哦？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0000F明白，总之我们先去看看情况吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1744")

    TalkEnd(0xFE)
    Return()

    # Function_12_15A1 end

    def Function_13_1748(): pass

    label("Function_13_1748")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_17CC")

    #C0021
    ChrTalk(
        0xA,
        (
            "#0203F从魔兽目前的气息来探测，\x01",
            "似乎还残留着相当多的数目呢。\x02\x03",

            "#0200F你们两位\x01",
            "请一定要小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_32(0x0, 0xF8, 0x270F)
    OP_32(0x3, 0xF8, 0x270F)
    Sound(8, 0, 100, 0)
    Sleep(800)
    Jump("loc_1978")

    label("loc_17CC")


    #C0022
    ChrTalk(
        0xA,
        (
            "#0200F魔兽的气息好像\x01",
            "从深处一直持续到这边……\x02\x03",

            "你们两位\x01",
            "请一定要小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0003F嗯，对了，缇欧……\x02\x03",

            "#0000F如果觉得有什么不对劲，\x01",
            "不要客气，\x01",
            "尽管和我说就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xA,
        (
            "#0200F好的。\x02\x03",

            "#0203F……对不起，\x01",
            "因为我刚才并不是很有自信。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧操作了魔导杖上的装置。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0026
    ChrTalk(
        0xA,
        (
            "#0200F虽然不算多，但还有剩余导力。\x01",
            "请你们两位拿去使用吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_32(0x0, 0xF8, 0x270F)
    OP_32(0x3, 0xF8, 0x270F)
    Sound(8, 0, 100, 0)
    Sleep(800)

    #C0027
    ChrTalk(
        0x104,
        "#0302F多谢啦，阿缇。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0000F那我们就不客气了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1978")

    TalkEnd(0xFE)
    Return()

    # Function_13_1748 end

    def Function_14_197C(): pass

    label("Function_14_197C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1250, 0, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17640, 0)
    SetChrPos(0x101, 500, 0, -2500, 0)
    SetChrPos(0x102, -500, 0, -2750, 0)
    SetChrPos(0x103, 500, 0, -4000, 0)
    SetChrPos(0x104, -500, 0, -4250, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1A2B():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A2B)
    Sleep(50)

    def lambda_1A48():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A48)
    Sleep(50)

    def lambda_1A65():
        OP_97(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A65)
    Sleep(50)

    def lambda_1A82():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A82)
    OP_68(0, 1250, 2000, 2000)
    FadeToBright(1000, 0)
    Sleep(200)

    def lambda_1AB9():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AB9)
    Sleep(50)

    def lambda_1ACD():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1ACD)
    Sleep(50)

    def lambda_1AE1():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1AE1)
    Sleep(50)

    def lambda_1AF5():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1AF5)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_1B0F():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B0F)
    WaitChrThread(0x103, 1)

    def lambda_1B20():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B20)
    WaitChrThread(0x104, 1)

    def lambda_1B31():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B31)

    #C0029
    ChrTalk(
        0x101,
        (
            "#0003F这里就是公寓的内部吗……\x01",
            "咳、咳咳……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0306F积了好多灰啊，\x01",
            "而且还真是宽敞呢。\x02",
        )
    )

    CloseMessageWindow()
    Sound(837, 0, 100, 0)
    Sleep(1500)
    Sound(838, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0031
    ChrTalk(
        0x102,
        "#0101F好像，有魔兽呢。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        (
            "#0201F嗯……似乎\x01",
            "在各处徘徊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#0003F委托的内容是清除魔兽，\x01",
            "所以有必要将全部魔兽都打倒。\x02\x03",

            "#0001F各位，谨慎前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, 2500, 0)
    OP_29(0xA, 0x1, 0x2)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_14_197C end

    def Function_15_1CB4(): pass

    label("Function_15_1CB4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-116040, 1250, 90, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17640, 0)
    SetChrPos(0x101, -115250, 0, -750, 315)
    SetChrPos(0x102, -115500, 0, 750, 225)
    SetChrPos(0x103, -116750, 0, -750, 45)
    SetChrPos(0x104, -117000, 0, 750, 135)
    FadeToBright(1000, 0)
    OP_0D()

    #C0034
    ChrTalk(
        0x102,
        (
            "#5P#0101F这样……大概就算是\x01",
            "全部清除完毕了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#11P#0003F是啊，我们应该\x01",
            "去过全部的房间了……\x02\x03",

            "#0001F不知道有没有遗漏，\x01",
            "返回途中顺便巡视一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        "#6P#0309F明白。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#12P#0203F……………………\x01",
            "嗯，说得也是……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -115250, 0, 0, 90)
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0xA, 0x1, 0x3)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_15_1CB4 end

    def Function_16_1E3D(): pass

    label("Function_16_1E3D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1250, 9000, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 750, 0, 10000, 225)
    SetChrPos(0x102, -750, 0, 9750, 135)
    SetChrPos(0x103, 750, 0, 8500, 315)
    SetChrPos(0x104, -750, 0, 8250, 45)
    SetChrPos(0x8, 0, 0, -2500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0038
    ChrTalk(
        0x102,
        (
            "#5P#0101F这样……大概就算是\x01",
            "全部清除完毕了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#11P#0003F是啊，我们应该\x01",
            "去过全部的房间了……\x02\x03",

            "#0001F不知道有没有遗漏，\x01",
            "返回途中顺便巡视一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        "#6P#0309F明白。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#12P#0203F……………………\x01",
            "嗯，说得也是……\x02",
        )
    )

    CloseMessageWindow()

    #N0042
    NpcTalk(
        0x8,
        "凶狠的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x1),
            "……喂，你们几个，\x01",
            "上蹿下跳得吵死人啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2055():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2055)

    def lambda_2062():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2062)

    def lambda_206F():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_206F)

    def lambda_207C():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_207C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0043
    ChrTalk(
        0x101,
        "#0005F哎……？\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1250, 0, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_29(0xA, 0x1, 0x3)
    Call(0, 18)
    Return()

    # Function_16_1E3D end

    def Function_17_20E3(): pass

    label("Function_17_20E3")

    EventBegin(0x1)
    SetChrPos(0x8, 0, 0, -2500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    #N0044
    NpcTalk(
        0x8,
        "凶狠的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x1),
            "#5P……喂，你们几个，\x01",
            "上蹿下跳得吵死人啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2198():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2198)

    def lambda_21A5():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_21A5)

    def lambda_21B2():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21B2)

    def lambda_21BF():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_21BF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0045
    ChrTalk(
        0x101,
        "#0005F哎……？\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1250, 0, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Call(0, 18)
    Return()

    # Function_17_20E3 end

    def Function_18_2220(): pass

    label("Function_18_2220")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02100.itc", 0x1E)
    OP_68(-640, 1250, 810, 0)
    MoveCamera(42, 35, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15760, 0)
    SetChrPos(0x101, 500, 0, 7750, 180)
    SetChrPos(0x104, -500, 0, 8000, 180)
    SetChrPos(0x102, 500, 0, 9500, 180)
    SetChrPos(0x103, -500, 0, 9750, 180)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, -2500, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_68(0, 1250, -500, 1500)

    def lambda_22ED():
        OP_97(0x8, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22ED)

    def lambda_2307():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2307)
    Sound(103, 0, 100, 0)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)

    #C0046
    ChrTalk(
        0x8,
        (
            "#1601F#12P在『鬼火』的附近\x01",
            "折腾些什么呢。\x01",
            "……倒是说啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_236F():
        OP_97(0x101, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_236F)
    Sleep(50)

    def lambda_238C():
        OP_97(0x104, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_238C)
    Sleep(50)

    def lambda_23A9():
        OP_97(0x102, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23A9)
    Sleep(50)

    def lambda_23C6():
        OP_97(0x103, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23C6)
    OP_68(-750, 1650, 1230, 3000)
    MoveCamera(49, 26, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15800, 3000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)

    #C0047
    ChrTalk(
        0x104,
        "#5P#0306F怎么，是你啊。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#5P#0000F说起来，\x01",
            "剑蛇帮的据点\x01",
            "好像就在这附近啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#12P#1604F呵呵……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)

    #C0050
    ChrTalk(
        0x8,
        "#12P#1609F#4S哈哈哈哈哈……呼！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#5P#0005F有、有什么好笑的。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#12P#1602F哈哈哈……！\x01",
            "你们怎么会搞成这种灰头土脸的狼狈样啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x103,
        "#5P#0200F是……是吗……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        (
            "#5P#0103F这也没办法啊，\x01",
            "毕竟我们刚刚和魔兽交战过。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#12P#1602F哈，魔兽吗？\x02\x03",

            "#1603F像这种废弃多年的旧屋里，\x01",
            "大多都会有魔兽出现吧。\x01",
            "这在旧城区里可是很常见的。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#5P#0005F常……常见吗……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#5P#0301F这里果然是个环境\x01",
            "恶劣的场所啊。\x02",
        )
    )

    CloseMessageWindow()
    Sound(837, 0, 100, 0)
    Sleep(1500)
    Sound(838, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x8)

    #C0058
    ChrTalk(
        0x8,
        (
            "#12P#1602F呵呵……你们折腾了\x01",
            "这么半天，结果不是\x01",
            "也没有搞定吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#5P#0001F真、真奇怪啊……\x01",
            "明明应该是已经把\x01",
            "所有的房间都检查过一遍了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        (
            "#5P#0203F说不定……\x02\x03",

            "#0200F魔兽已经在此地\x01",
            "繁殖了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2817():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2817)

    def lambda_2824():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2824)

    def lambda_2831():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2831)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0061
    ChrTalk(
        0x103,
        (
            "#5P#0200F……其实，我一直\x01",
            "都能感觉到它们的气息。\x02\x03",

            "而且是在这栋屋子的深处。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#11P#0005F是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#12P#1602F哼哼，都这种时候了还在悠闲地商量？\x01",
            "真是一群不中用的家伙啊。\x02\x03",

            "#1600F你们这群警察就回到街上，\x01",
            "继续巡逻去吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2930():
        OP_97(0x8, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2930)
    BeginChrThread(0x101, 2, 0, 19)
    BeginChrThread(0x104, 2, 0, 19)
    BeginChrThread(0x102, 2, 0, 19)
    BeginChrThread(0x103, 2, 0, 19)
    Sleep(200)

    def lambda_2965():
        OP_98(0x101, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2965)

    def lambda_297F():
        OP_98(0x104, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_297F)
    Sleep(100)

    def lambda_299C():
        OP_98(0x102, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_299C)

    def lambda_29B6():
        OP_98(0x103, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29B6)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x102, 0x2)

    #C0064
    ChrTalk(
        0x102,
        "#12P#0105F等、等一下！？\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#12P#0001F慢着，你一个人要去干什么……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-2770, 1250, 6170, 0)
    MoveCamera(65, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16430, 0)
    SetChrPos(0x8, -1390, 0, 6440, 315)
    BeginChrThread(0x101, 2, 0, 19)
    BeginChrThread(0x104, 2, 0, 19)
    BeginChrThread(0x102, 2, 0, 19)
    BeginChrThread(0x103, 2, 0, 19)
    OP_95(0x8, -5500, 0, 10000, 2000, 0x0)

    def lambda_2AAE():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2AAE)
    OP_95(0x8, -10000, -2000, 10000, 2000, 0x0)
    WaitChrThread(0x8, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x102, 0x2)
    Sleep(600)
    OP_68(-1280, 1250, 4610, 3000)
    MoveCamera(65, 24, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16430, 3000)
    OP_6F(0x79)

    #C0066
    ChrTalk(
        0x104,
        "#12P#0306F他还真去里面了啊？\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#11P#0101F以他的性格来说，\x01",
            "大概是想亲自去解决那些\x01",
            "吵闹的魔兽吧……\x02",
        )
    )

    CloseMessageWindow()
    Sound(837, 0, 100, 0)
    Sound(818, 0, 100, 0)
    Sleep(1000)
    OP_82(0xC8, 0x64, 0x7D0, 0x320)
    Sound(834, 0, 100, 0)
    Sleep(1500)
    Sound(838, 0, 100, 0)
    Sleep(1000)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0068
    ChrTalk(
        0x104,
        "#12P#0301F……不要紧吗？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#11P#0003F是啊……就算是瓦鲁多，\x01",
            "单独行动终究也不安全……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(10, 1250, 2660, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16140, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0070
    ChrTalk(
        0x101,
        (
            "#12P#0001F艾莉、缇欧，\x01",
            "抱歉，这里交给你们可以吗？\x02\x03",

            "#0003F经他那么疯狂一闹，\x01",
            "或许会有受惊的魔兽\x01",
            "逃到外面去也说不定。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D24():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D24)

    def lambda_2D31():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D31)

    def lambda_2D3E():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D3E)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0071
    ChrTalk(
        0x102,
        "#5P#0100F#5P明白，我们在这里看守就行了吧。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        (
            "#5P#0200F你们两位要去\x01",
            "把瓦鲁多先生带回来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#12P#0001F嗯，至少也得去看看他那边的状况。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        "#6P#0306F嗯，这种判断应该很妥当。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0075
    ChrTalk(
        0x104,
        (
            "#6P#0300F那我们就赶快\x01",
            "走吧，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#11P#0001F是啊……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_68(0, 1000, 2500, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x0, 0, 0, 2500, 0)
    SetChrPos(0x1, 0, 0, 2500, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_E0(0x0)
    ClearScenarioFlags(0x6F, 1)
    ClearChrFlags(0x13, 0x80)
    OP_1B(0x0, 0x0, 0x1C)
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0xA, 0x1, 0x4)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_18_2220 end

    def Function_19_2F13(): pass

    label("Function_19_2F13")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F2D")
    TurnDirection(0xFE, 0x8, 500)
    Sleep(200)
    Jump("Function_19_2F13")

    label("loc_2F2D")

    Return()

    # Function_19_2F13 end

    def Function_20_2F2E(): pass

    label("Function_20_2F2E")

    EventBegin(0x0)
    Fade(500)
    OP_68(-132910, 1000, 3230, 0)
    MoveCamera(41, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16170, 0)
    SetChrPos(0x101, -132000, 0, 1500, 0)
    SetChrPos(0x104, -133000, 0, 1250, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0077
    ChrTalk(
        0x101,
        (
            "#0005F#12P木箱……\x01",
            "难道里面还有房间吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        "#0301F#6P总之，先进去看看吧！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 1, 0x80)
    SetChrPos(0x0, -132500, 0, 1500, 0)
    SetScenarioFlags(0x71, 0)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_20_2F2E end

    def Function_21_301C(): pass

    label("Function_21_301C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-97470, 4500, 165000, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -98740, 3500, 163210, 45)
    SetChrPos(0x104, -99750, 3500, 163400, 45)
    SetChrPos(0x8, -91930, 3500, 169750, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0079
    NpcTalk(
        0x8,
        "瓦鲁多的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x1),
            "#4S看招……！！\x02",
        )
    )

    CloseMessageWindow()
    Sound(590, 0, 100, 0)
    Sleep(100)
    Sound(830, 0, 100, 0)
    Sound(819, 0, 100, 0)
    Sleep(1000)
    Sound(532, 0, 100, 0)
    Sleep(200)
    Sound(830, 0, 100, 0)
    Sleep(1000)

    #C0080
    ChrTalk(
        0x101,
        "#0005F#11P在前面的房间吗……？\x02",
    )

    CloseMessageWindow()

    #N0081
    NpcTalk(
        0x8,
        "瓦鲁多的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x1),
            "#4S……哼……这可恶的东西………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0xC8, 0x64, 0x7D0, 0x4B0)
    Sound(813, 0, 100, 0)
    Sleep(500)
    Sound(830, 0, 100, 0)
    Sound(819, 0, 100, 0)

    #N0082
    NpcTalk(
        0x8,
        "瓦鲁多的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x1),
            "#4S……呜啊………！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0083
    ChrTalk(
        0x104,
        (
            "#5P#0305F喂喂，听起来情况\x01",
            "似乎很不妙吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#11P#0001F所以说，单独行动\x01",
            "太危险了啊……！\x02\x03",

            "兰迪，我们突击吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_64(0x104)

    #C0085
    ChrTalk(
        0x104,
        "#5P#0301F了解！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 2, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x0, -98740, 3500, 163210, 45)
    OP_29(0xA, 0x1, 0x6)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_21_301C end

    def Function_22_32A6(): pass

    label("Function_22_32A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x15, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch00351.itc", 0x21)
    LoadChrToIndex("chr/ch02153.itc", 0x22)
    OP_68(-100520, 1200, 212080, 0)
    MoveCamera(43, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19760, 0)
    SetChrPos(0x101, -99500, 0, 197250, 0)
    SetChrPos(0x104, -100500, 0, 197000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x116, 0x22)
    SetChrSubChip(0x116, 0x3)
    SetChrPos(0x116, -100000, 0, 213500, 180)
    ClearChrFlags(0x116, 0x80)
    ClearChrBattleFlags(0x116, 0x8000)
    SetChrFlags(0xB, 0x8000)
    BeginChrThread(0xB, 0, 0, 2)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    BeginChrThread(0xC, 0, 0, 3)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 3)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    BeginChrThread(0xE, 0, 0, 3)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    BeginChrThread(0xF, 0, 0, 3)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)
    SetCameraDistance(18760, 2000)
    OP_6F(0x79)

    #C0086
    ChrTalk(
        0x116,
        (
            "#5P#1607F呼、呼……\x02\x03",

            "可恶……！！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-100310, 1000, 209140, 2500)

    def lambda_343E():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_343E)

    def lambda_3458():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3458)
    Sleep(50)

    def lambda_346C():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_346C)

    def lambda_3486():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3486)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(100)
    Sound(808, 0, 100, 0)
    OP_0D()
    OP_6F(0x1)

    #C0087
    ChrTalk(
        0x101,
        "#12P#0007F瓦鲁多，不要勉强！\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        "#12P#0307F我们这就来增援！\x02",
    )

    CloseMessageWindow()

    def lambda_3508():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3508)

    def lambda_3522():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3522)
    Sleep(200)
    Battle("BattleInfo_724", 0x30200011, 0x0, 0x0, 0x15, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x104, 0x1)
    Call(0, 23)
    Return()

    # Function_22_32A6 end

    def Function_23_3560(): pass

    label("Function_23_3560")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x15, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00350.itc", 0x1F)
    LoadChrToIndex("chr/ch02153.itc", 0x20)
    LoadChrToIndex("chr/ch02100.itc", 0x21)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    OP_68(-100740, 1200, 210550, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -99500, 0, 209250, 0)
    SetChrPos(0x104, -100500, 0, 209000, 0)
    SetChrPos(0x102, -99500, 0, 199250, 0)
    SetChrPos(0x103, -100500, 0, 199000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x104, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -100000, 0, 213500, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    #C0089
    ChrTalk(
        0x101,
        "#12P#0010F呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        "#6P#0306F还真是难对付啊。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#12P#0003F嗯，而且还没有\x01",
            "缇欧和艾莉的援护……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(100)
    Sound(808, 0, 100, 0)
    OP_68(-100180, 1200, 212390, 3000)

    def lambda_3731():
        OP_97(0x101, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3731)
    Sleep(50)

    def lambda_374E():
        OP_97(0x104, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_374E)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0092
    ChrTalk(
        0x101,
        "#12P#0000F瓦鲁多，没事吧？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        "#5P#1603F哼……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0094
    ChrTalk(
        0x8,
        (
            "#5P#1601F你们可真是\x01",
            "多管闲事啊。\x02\x03",

            "#1607F难道是看不起本大爷吗？\x01",
            "啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0095
    ChrTalk(
        0x101,
        "#12P#0006F怎么这时候还要找麻烦……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        (
            "#12P#0300F算了，本来也没想过\x01",
            "会被不良分子感谢啊。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-101130, 1000, 205900, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21830, 0)
    Sleep(500)
    OP_68(-100390, 1400, 209890, 4000)
    Sound(103, 0, 100, 0)

    def lambda_38EA():
        OP_97(0x102, 0x0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38EA)

    def lambda_3904():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3904)
    Sleep(50)

    def lambda_3918():
        OP_97(0x103, 0x0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3918)

    def lambda_3932():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3932)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    OP_0D()
    OP_6F(0x1)

    #C0097
    ChrTalk(
        0x102,
        (
            "#12P#0101F你们两个都没事吧！？\x01",
            "我们听到了很大的响声，所以……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0098
    ChrTalk(
        0x104,
        (
            "#5P#0304F哈哈，算是没事吧。\x01",
            "不过某位老兄刚才倒是相当危险呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "#5P#1607F喂，红毛，\x01",
            "想让我把你的脑袋给敲碎吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x103, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_93(0x103, 0x2D, 0x2EE)
    Sleep(500)
    OP_93(0x103, 0x13B, 0x2EE)
    Sleep(500)
    OP_93(0x103, 0xD7, 0x2EE)
    Sleep(500)

    #C0100
    ChrTalk(
        0x103,
        (
            "#6P#0203F魔兽的气息……\x02\x03",

            "#0200F好像完全消失了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x101, 1, 0, 24)
    BeginChrThread(0x102, 1, 0, 25)
    BeginChrThread(0x104, 1, 0, 26)
    BeginChrThread(0x8, 1, 0, 27)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x8, 1)

    #C0101
    ChrTalk(
        0x101,
        "#11P#0005F真的哦……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#6P#0304F变得安静了啊。\x02\x03",

            "#0300F果然是因为把它们的首领解决掉了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#5P#1603F哼……无聊，\x01",
            "这样就结束了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x8, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_68(-100920, 1500, 208170, 3000)
    BeginChrThread(0x101, 1, 0, 19)

    #C0104
    ChrTalk(
        0x101,
        "#5P#0005F瓦鲁多……？\x02",
    )

    OP_97(0x8, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    CloseMessageWindow()

    def lambda_3BDF():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BDF)

    def lambda_3BEC():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3BEC)

    def lambda_3BF9():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3BF9)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0105
    ChrTalk(
        0x8,
        (
            "#12P#1601F今天可真够倒霉的，\x01",
            "回去继续喝酒了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0106
    ChrTalk(
        0x8,
        (
            "#12P#1601F……还有，你们几个，\x01",
            "不要在旧城区擅自乱来啊。\x02\x03",

            "#1607F旧城区可是本大爷的地盘。\x01",
            "要是事情办完了，就赶快给我离开吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3CCC():
        OP_93(0x101, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CCC)

    def lambda_3CD9():
        OP_93(0x102, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3CD9)

    def lambda_3CE6():
        OP_93(0x103, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3CE6)

    def lambda_3CF3():
        OP_93(0x104, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3CF3)
    OP_97(0x8, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0107
    ChrTalk(
        0x102,
        (
            "#5P#0104F呼……这好像是他\x01",
            "掩饰害羞的表现呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#5P#0306F哎呀呀，那家伙\x01",
            "还是一点都没变呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#11P#0003F算啦……\x02\x03",

            "#0000F清除魔兽的工作似乎算是顺利完成了，\x01",
            "我们去向伊梅尔达夫人报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        "#6P#0200F是啊，我们走吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0580", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_3560 end

    def Function_24_3E1D(): pass

    label("Function_24_3E1D")

    OP_93(0x101, 0x87, 0x2EE)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x2EE)
    Sleep(500)
    OP_93(0x101, 0x2D, 0x2EE)
    Sleep(500)
    Return()

    # Function_24_3E1D end

    def Function_25_3E3C(): pass

    label("Function_25_3E3C")

    OP_93(0x102, 0xB4, 0x2EE)
    Sleep(500)
    OP_93(0x102, 0x2D, 0x2EE)
    Sleep(500)
    OP_93(0x102, 0x13B, 0x2EE)
    Sleep(500)
    Return()

    # Function_25_3E3C end

    def Function_26_3E5B(): pass

    label("Function_26_3E5B")

    OP_93(0x104, 0x10E, 0x2EE)
    Sleep(500)
    OP_93(0x104, 0x13B, 0x2EE)
    Sleep(500)
    OP_93(0x104, 0x0, 0x2EE)
    Sleep(500)
    Return()

    # Function_26_3E5B end

    def Function_27_3E7A(): pass

    label("Function_27_3E7A")

    OP_93(0x8, 0xE1, 0x2EE)
    Sleep(500)
    OP_93(0x8, 0x87, 0x2EE)
    Sleep(500)
    OP_93(0x8, 0xB4, 0x2EE)
    Sleep(500)
    Return()

    # Function_27_3E7A end

    def Function_28_3E99(): pass

    label("Function_28_3E99")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F1F")
    TurnDirection(0x104, 0x101, 0)

    #C0111
    ChrTalk(
        0x104,
        (
            "#0305F喂，罗伊德，我们不是\x01",
            "要去把瓦鲁多那家伙带回来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#0001F啊，对哦。\x01",
            "还是优先解决这件事吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F98")

    label("loc_3F1F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F98")
    TurnDirection(0x101, 0x104, 0)

    #C0113
    ChrTalk(
        0x101,
        (
            "#0005F等一下，兰迪。\x01",
            "现在先去确认一下瓦鲁多那边的状况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        (
            "#0301F噢，对啊。\x01",
            "赶快去里面吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F98")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 1000, 0)
    EventEnd(0x4)
    Return()

    # Function_28_3E99 end

    SaveToFile()

Try(main)
