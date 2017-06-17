from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ヴァルド",               # 1
        "エリィ",                 # 2
        "ティオ",                 # 3
        "魔獣",                   # 4
        "魔獣",                   # 5
        "魔獣",                   # 6
        "魔獣",                   # 7
        "魔獣",                   # 8
        "ジェラルム・ポー",       # 9
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
        "Function_8_109B",         # 08, 8
        "Function_9_11E8",         # 09, 9
        "Function_10_13FB",        # 0A, 10
        "Function_11_14F2",        # 0B, 11
        "Function_12_1604",        # 0C, 12
        "Function_13_17E5",        # 0D, 13
        "Function_14_1A61",        # 0E, 14
        "Function_15_1DD7",        # 0F, 15
        "Function_16_1F6C",        # 10, 16
        "Function_17_2220",        # 11, 17
        "Function_18_235F",        # 12, 18
        "Function_19_309A",        # 13, 19
        "Function_20_30B5",        # 14, 20
        "Function_21_31AF",        # 15, 21
        "Function_22_3443",        # 16, 22
        "Function_23_370D",        # 17, 23
        "Function_24_4014",        # 18, 24
        "Function_25_4033",        # 19, 25
        "Function_26_4052",        # 1A, 26
        "Function_27_4071",        # 1B, 27
        "Function_28_4090",        # 1C, 28
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104A")
    Sound(14, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x4B, 1)"), scpexpr(EXPR_END)), "loc_FD3")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1045")

    label("loc_FD3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x4B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x4B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1045")

    Jump("loc_108F")

    label("loc_104A")

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

    label("loc_108F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_F4E end

    def Function_8_109B(): pass

    label("Function_8_109B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1197")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x644, 1)"), scpexpr(EXPR_END)), "loc_1120")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1192")

    label("loc_1120")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x644),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x644),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1192")

    Jump("loc_11DC")

    label("loc_1197")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_11DC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_109B end

    def Function_9_11E8(): pass

    label("Function_9_11E8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B5")
    Sound(14, 0, 100, 0)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E3")
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x10, 0x0, 0)
    OP_98(0x10, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1241():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1241)

    def lambda_125B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_125B)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)

    #A0007
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
    Battle("BattleInfo_6E0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_12C4"),
        (2, "loc_12D3"),
        (1, "loc_12E0"),
        (SWITCH_DEFAULT, "loc_12E3"),
    )


    label("loc_12C4")

    SetScenarioFlags(0x74, 2)
    OP_70(0xB, 0x1E)
    Sleep(500)
    Jump("loc_12E3")

    label("loc_12D3")

    OP_70(0xB, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_12E0")

    OP_B7(0x0)
    Return()

    label("loc_12E3")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E1, 1)"), scpexpr(EXPR_END)), "loc_1340")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_13B0")

    label("loc_1340")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5E1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5E1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xB, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13B0")

    Jump("loc_13EF")

    label("loc_13B5")

    FadeToDark(300, 0, 100)

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

    label("loc_13EF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_11E8 end

    def Function_10_13FB(): pass

    label("Function_10_13FB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14BB")
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
            "#60I時のセピス×４０\x01\x07\x02",

            "#61I空のセピス×４０\x01\x07\x02",

            "#62I幻のセピス×４０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x111, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_14E0")

    label("loc_14BB")


    #A0012
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

    label("loc_14E0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_13FB end

    def Function_11_14F2(): pass

    label("Function_11_14F2")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CD")
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
            "#56I地のセピス×４０\x01\x07\x02",

            "#57I水のセピス×４０\x01\x07\x02",

            "#58I火のセピス×４０\x01\x07\x02",

            "#59I風のセピス×４０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x111, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_15F2")

    label("loc_15CD")


    #A0014
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

    label("loc_15F2")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_14F2 end

    def Function_12_1604(): pass

    label("Function_12_1604")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16A0")

    #C0015
    ChrTalk(
        0x9,
        (
            "#0100F魔獣が外に出ようとしたら\x01",
            "私とティオちゃんで何とかするわ。\x02\x03",

            "ロイド、ランディ。\x01",
            "そっちも頑張ってね。\x02",
        )
    )

    CloseMessageWindow()
    OP_32(0x0, 0xFC, 0x0)
    OP_32(0x3, 0xFC, 0x0)
    OP_32(0x0, 0xFD, 0x270F)
    OP_32(0x3, 0xFD, 0x270F)
    Sound(8, 0, 100, 0)
    Sleep(800)
    Jump("loc_17E1")

    label("loc_16A0")


    #C0016
    ChrTalk(
        0x9,
        (
            "#0100F魔獣が外に出ようとしたら\x01",
            "私とティオちゃんで何とかするわ。\x02\x03",

            "ロイド、ランディ。\x01",
            "彼の方は頼んだわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        "#0309Fおう、任せとけ！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "#0105F……そうだ、ちょっと待って。\x01",
            "手持ちの回復薬があるから。\x02",
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
        "#0100F２人とも、無茶はしないでね？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0000F了解、とにかく様子を見てくるよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_17E1")

    TalkEnd(0xFE)
    Return()

    # Function_12_1604 end

    def Function_13_17E5(): pass

    label("Function_13_17E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1873")

    #C0021
    ChrTalk(
        0xA,
        (
            "#0203F魔獣の気配からすると\x01",
            "まだ相当数が残っているようです。\x02\x03",

            "#0200Fお２人とも、\x01",
            "気をつけてください。\x02",
        )
    )

    CloseMessageWindow()
    OP_32(0x0, 0xF8, 0x270F)
    OP_32(0x3, 0xF8, 0x270F)
    Sound(8, 0, 100, 0)
    Sleep(800)
    Jump("loc_1A5D")

    label("loc_1873")


    #C0022
    ChrTalk(
        0xA,
        (
            "#0200F魔獣の気配は\x01",
            "奥の方から続いているようです……\x02\x03",

            "お２人とも、\x01",
            "気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0003Fああ、というかティオ……\x02\x03",

            "#0000F違和感があったのなら\x01",
            "遠慮せずに言ってくれて\x01",
            "良かったんだぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xA,
        (
            "#0200Fはい。\x02\x03",

            "#0203F……すみません、\x01",
            "あまり自信が無かったもので。\x02",
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
            "ティオは魔導杖のユニットを操作した。\x02",
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
            "#0200F少しですが余剰導力があります。\x01",
            "お２人で使ってください。\x02",
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
        "#0302Fサンキュー、ティオすけ。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0000F使わせてもらうよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1A5D")

    TalkEnd(0xFE)
    Return()

    # Function_13_17E5 end

    def Function_14_1A61(): pass

    label("Function_14_1A61")

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

    def lambda_1B10():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B10)
    Sleep(50)

    def lambda_1B2D():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B2D)
    Sleep(50)

    def lambda_1B4A():
        OP_97(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B4A)
    Sleep(50)

    def lambda_1B67():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B67)
    OP_68(0, 1250, 2000, 2000)
    FadeToBright(1000, 0)
    Sleep(200)

    def lambda_1B9E():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B9E)
    Sleep(50)

    def lambda_1BB2():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1BB2)
    Sleep(50)

    def lambda_1BC6():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1BC6)
    Sleep(50)

    def lambda_1BDA():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1BDA)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_1BF4():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BF4)
    WaitChrThread(0x103, 1)

    def lambda_1C05():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C05)
    WaitChrThread(0x104, 1)

    def lambda_1C16():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C16)

    #C0029
    ChrTalk(
        0x101,
        (
            "#0003Fここがアパートの内部か……\x01",
            "ごほ、ごほごほ……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0306Fすげえホコリが積もってるな。\x01",
            "それに結構広そうだぜ。\x02",
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
        "#0101F魔獣、いそうね。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        (
            "#0201Fええ……あちこち\x01",
            "走り回っているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#0003F依頼は掃討ということだったし\x01",
            "全ての魔獣を倒す必要がある。\x02\x03",

            "#0001Fみんな、気を引き締めていこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, 2500, 0)
    OP_29(0xA, 0x1, 0x2)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_14_1A61 end

    def Function_15_1DD7(): pass

    label("Function_15_1DD7")

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
            "#5P#0101Fこれで……一通り\x01",
            "掃討が終わったんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#11P#0003Fそうだな、部屋は\x01",
            "全て回ったはずだ……\x02\x03",

            "#0001F見落としが無いか\x01",
            "巡回しつつ戻ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        "#6P#0309Fラジャ。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#12P#0203F……………………\x01",
            "はい、そうですね……\x02",
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

    # Function_15_1DD7 end

    def Function_16_1F6C(): pass

    label("Function_16_1F6C")

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
            "#5P#0101Fこれで……一通り\x01",
            "掃討が終わったんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#11P#0003Fそうだな、部屋は\x01",
            "全て回ったはずだ……\x02\x03",

            "#0001F見落としが無いか\x01",
            "巡回しつつ戻ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        "#6P#0309Fラジャ。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#12P#0203F……………………\x01",
            "はい、そうですね……\x02",
        )
    )

    CloseMessageWindow()

    #N0042
    NpcTalk(
        0x8,
        "獰猛そうな声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x1),
            "……おいテメエら、\x01",
            "ドタバタうるせえぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2192():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2192)

    def lambda_219F():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_219F)

    def lambda_21AC():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21AC)

    def lambda_21B9():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_21B9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0043
    ChrTalk(
        0x101,
        "#0005Fえ……？\x02",
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

    # Function_16_1F6C end

    def Function_17_2220(): pass

    label("Function_17_2220")

    EventBegin(0x1)
    SetChrPos(0x8, 0, 0, -2500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    #N0044
    NpcTalk(
        0x8,
        "獰猛そうな声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x1),
            "#5P……おいテメエら、\x01",
            "ドタバタうるせえぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_22D7():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22D7)

    def lambda_22E4():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22E4)

    def lambda_22F1():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_22F1)

    def lambda_22FE():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22FE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0045
    ChrTalk(
        0x101,
        "#0005Fえ……？\x02",
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

    # Function_17_2220 end

    def Function_18_235F(): pass

    label("Function_18_235F")

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

    def lambda_242C():
        OP_97(0x8, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_242C)

    def lambda_2446():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2446)
    Sound(103, 0, 100, 0)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)

    #C0046
    ChrTalk(
        0x8,
        (
            "#1601F#12Pイグニスの隣で\x01",
            "サツが何やってやがる。\x01",
            "……アア？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_24B0():
        OP_97(0x101, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24B0)
    Sleep(50)

    def lambda_24CD():
        OP_97(0x104, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_24CD)
    Sleep(50)

    def lambda_24EA():
        OP_97(0x102, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24EA)
    Sleep(50)

    def lambda_2507():
        OP_97(0x103, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2507)
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
        "#5P#0306F何だアンタかよ。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#5P#0000Fそういえば、\x01",
            "サーベルバイパーの\x01",
            "溜まり場の近くだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#12P#1604Fクク……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)

    #C0050
    ChrTalk(
        0x8,
        "#12P#1609F#4Sハハハハハ……ッ！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#5P#0005Fな、何がおかしい。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#12P#1602Fハハハ……！\x01",
            "お前ら、ホコリまみれだぜ！\x02",
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
        "#5P#0200Fそう、ですか……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        (
            "#5P#0103F仕方がないわよ。\x01",
            "魔獣と格闘していたんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#12P#1602Fハッ、魔獣か。\x02\x03",

            "#1603F大方古い廃屋にでも\x01",
            "沸きやがったんだろ。\x01",
            "旧市街じゃよくあることだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#5P#0005Fよく、あるのか。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#5P#0301Fやっぱ環境的には\x01",
            "よくねえ場所だよなぁ。\x02",
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
            "#12P#1602Fクク……あれだけ\x01",
            "ドタバタしてた癖に\x01",
            "まだ終わってねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#5P#0001Fお、おかしいな……\x01",
            "全部の部屋を\x01",
            "見回ったはずなんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        (
            "#5P#0203Fもしかして……\x02\x03",

            "#0200F魔獣はここで\x01",
            "繁殖しているのかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_297E():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_297E)

    def lambda_298B():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_298B)

    def lambda_2998():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2998)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0061
    ChrTalk(
        0x103,
        (
            "#5P#0200F……実は、ずっと\x01",
            "気配を感じています。\x02\x03",

            "それも大分奥の方から。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#11P#0005Fそうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#12P#1602Fクク、今ごろそんな相談か？\x01",
            "手際の悪い連中だぜ。\x02\x03",

            "#1600Fサツは帰って\x01",
            "街の巡回でもしてな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A87():
        OP_97(0x8, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A87)
    BeginChrThread(0x101, 2, 0, 19)
    BeginChrThread(0x104, 2, 0, 19)
    BeginChrThread(0x102, 2, 0, 19)
    BeginChrThread(0x103, 2, 0, 19)
    Sleep(200)

    def lambda_2ABC():
        OP_98(0x101, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ABC)

    def lambda_2AD6():
        OP_98(0x104, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2AD6)
    Sleep(100)

    def lambda_2AF3():
        OP_98(0x102, 0x1F4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2AF3)

    def lambda_2B0D():
        OP_98(0x103, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B0D)
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
        "#12P#0105Fちょっ、ちょっと！？\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#12P#0001F待ってくれ、１人で何を……\x02",
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

    def lambda_2C09():
        OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C09)
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
        "#12P#0306F奥にいっちまったぞ？\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#11P#0101F彼の性格からすると\x01",
            "耳障りな魔獣を始末しに行った、\x01",
            "という所かしら……\x02",
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
        "#12P#0301F……大丈夫なのか？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#11P#0003Fそうだな……いくらヴァルドでも\x01",
            "単独行動はよくない……\x02",
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
            "#12P#0001Fエリィ、ティオ。\x01",
            "すまない、ここを頼めるか？\x02\x03",

            "#0003F彼の派手さ加減からすると\x01",
            "驚いた魔獣が\x01",
            "外に逃げ出てしまうかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2EA7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2EA7)

    def lambda_2EB4():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2EB4)

    def lambda_2EC1():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2EC1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0071
    ChrTalk(
        0x102,
        "#5P#0100F#5P了解、見張りということね。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        (
            "#5P#0200Fお２人の方は\x01",
            "ヴァルドさんを連れ戻しに？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#12P#0001Fああ、様子だけは見てくるよ。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        "#6P#0306F判断としちゃ妥当だろうな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0075
    ChrTalk(
        0x104,
        (
            "#6P#0300Fさくっと\x01",
            "行ってこようぜ、ロイド。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#11P#0001Fああ……！\x02",
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

    # Function_18_235F end

    def Function_19_309A(): pass

    label("Function_19_309A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30B4")
    TurnDirection(0xFE, 0x8, 500)
    Sleep(200)
    Jump("Function_19_309A")

    label("loc_30B4")

    Return()

    # Function_19_309A end

    def Function_20_30B5(): pass

    label("Function_20_30B5")

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
            "#0005F#12P木箱が……\x01",
            "奥にまだ部屋があったのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        "#0301F#6Pともかく入ってみようぜ！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 1, 0x80)
    SetChrPos(0x0, -132500, 0, 1500, 0)
    SetScenarioFlags(0x71, 0)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_20_30B5 end

    def Function_21_31AF(): pass

    label("Function_21_31AF")

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
        "ヴァルドの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x1),
            "#4Sオラァ……！！\x02",
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
        "#0005F#11Pこの先の部屋か……？\x02",
    )

    CloseMessageWindow()

    #N0081
    NpcTalk(
        0x8,
        "ヴァルドの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x1),
            "#4S……ッ……コノヤロウ………\x02",
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
        "ヴァルドの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x1),
            "#4S……ぐはっ………！？\x02",
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
            "#5P#0305Fおいおい、\x01",
            "何かやべえんじゃねえか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#11P#0001Fだから単独行動は\x01",
            "危険なんだ……！\x02\x03",

            "ランディ、突入するぞ！\x02",
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

    # Function_21_31AF end

    def Function_22_3443(): pass

    label("Function_22_3443")

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
            "#5P#1607Fハア、ハア……\x02\x03",

            "クソがァ……！！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-100310, 1000, 209140, 2500)

    def lambda_35E3():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35E3)

    def lambda_35FD():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35FD)
    Sleep(50)

    def lambda_3611():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3611)

    def lambda_362B():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_362B)
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
        "#12P#0007Fヴァルド、無理をするな！\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        "#12P#0307F今加勢してやるぜ！\x02",
    )

    CloseMessageWindow()

    def lambda_36B5():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36B5)

    def lambda_36CF():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_36CF)
    Sleep(200)
    Battle("BattleInfo_724", 0x30200011, 0x0, 0x0, 0x15, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x104, 0x1)
    Call(0, 23)
    Return()

    # Function_22_3443 end

    def Function_23_370D(): pass

    label("Function_23_370D")

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
        "#12P#0010Fハア、ハア……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        "#6P#0306F結構手強かったな。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#12P#0003Fああ、ティオとエリィの\x01",
            "サポートも無かったし……\x02",
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

    def lambda_38F0():
        OP_97(0x101, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38F0)
    Sleep(50)

    def lambda_390D():
        OP_97(0x104, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_390D)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0092
    ChrTalk(
        0x101,
        "#12P#0000Fヴァルド、平気か？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        "#5P#1603Fフン……\x02",
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
            "#5P#1601F余計な手出し\x01",
            "してんじゃねえぞ。\x02\x03",

            "#1607F俺を舐めてるのか？\x01",
            "アア！？\x02",
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
        "#12P#0006Fここで絡まないでくれ……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        (
            "#12P#0300Fま、不良に感謝されようとは\x01",
            "思っちゃねえけどな。\x02",
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

    def lambda_3ABB():
        OP_97(0x102, 0x0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3ABB)

    def lambda_3AD5():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3AD5)
    Sleep(50)

    def lambda_3AE9():
        OP_97(0x103, 0x0, 0x0, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AE9)

    def lambda_3B03():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3B03)
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
            "#12P#0101F２人とも大丈夫！？\x01",
            "すごい物音がしたけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0098
    ChrTalk(
        0x104,
        (
            "#5P#0304Fハハ、何とかな。\x01",
            "若干１名が危ねえトコだったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "#5P#1607Fオイ赤毛、\x01",
            "頭カチ割られてえのか！？\x02",
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
            "#6P#0203F魔獣の気配が……\x02\x03",

            "#0200F完全に消えたようですね。\x02",
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
        "#11P#0005F本当だ……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#6P#0304F静かになったな。\x02\x03",

            "#0300Fやっぱ頭#2Rヘッド#を潰したせいか。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#5P#1603Fフン……下らねぇ。\x01",
            "これで終わりかよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x8, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_68(-100920, 1500, 208170, 3000)
    BeginChrThread(0x101, 1, 0, 19)

    #C0104
    ChrTalk(
        0x101,
        "#5P#0005Fヴァルド……？\x02",
    )

    OP_97(0x8, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    CloseMessageWindow()

    def lambda_3DB4():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DB4)

    def lambda_3DC1():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3DC1)

    def lambda_3DCE():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3DCE)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0105
    ChrTalk(
        0x8,
        (
            "#12P#1601F今日はケチがついた。\x01",
            "帰って飲み直す。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0106
    ChrTalk(
        0x8,
        (
            "#12P#1601F……それとテメエら、旧市街で\x01",
            "勝手な真似してんじゃねえぞ。\x02\x03",

            "#1607F旧市街#6Rこ  こ#は俺の縄張りだ。\x01",
            "用が済んだらとっとと出ていけや！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3EB5():
        OP_93(0x101, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EB5)

    def lambda_3EC2():
        OP_93(0x102, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EC2)

    def lambda_3ECF():
        OP_93(0x103, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3ECF)

    def lambda_3EDC():
        OP_93(0x104, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3EDC)
    OP_97(0x8, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0107
    ChrTalk(
        0x102,
        (
            "#5P#0104Fふう……彼なりの\x01",
            "照れ隠しみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#5P#0306Fやれやれ、あいつも\x01",
            "相変わらずだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#11P#0003Fまあいいさ……\x02\x03",

            "#0000F掃討も無事完了したみたいだ。\x01",
            "イメルダさんに報告に行こうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        "#6P#0200Fそうですね、行きましょう。\x02",
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

    # Function_23_370D end

    def Function_24_4014(): pass

    label("Function_24_4014")

    OP_93(0x101, 0x87, 0x2EE)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x2EE)
    Sleep(500)
    OP_93(0x101, 0x2D, 0x2EE)
    Sleep(500)
    Return()

    # Function_24_4014 end

    def Function_25_4033(): pass

    label("Function_25_4033")

    OP_93(0x102, 0xB4, 0x2EE)
    Sleep(500)
    OP_93(0x102, 0x2D, 0x2EE)
    Sleep(500)
    OP_93(0x102, 0x13B, 0x2EE)
    Sleep(500)
    Return()

    # Function_25_4033 end

    def Function_26_4052(): pass

    label("Function_26_4052")

    OP_93(0x104, 0x10E, 0x2EE)
    Sleep(500)
    OP_93(0x104, 0x13B, 0x2EE)
    Sleep(500)
    OP_93(0x104, 0x0, 0x2EE)
    Sleep(500)
    Return()

    # Function_26_4052 end

    def Function_27_4071(): pass

    label("Function_27_4071")

    OP_93(0x8, 0xE1, 0x2EE)
    Sleep(500)
    OP_93(0x8, 0x87, 0x2EE)
    Sleep(500)
    OP_93(0x8, 0xB4, 0x2EE)
    Sleep(500)
    Return()

    # Function_27_4071 end

    def Function_28_4090(): pass

    label("Function_28_4090")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4122")
    TurnDirection(0x104, 0x101, 0)

    #C0111
    ChrTalk(
        0x104,
        (
            "#0305Fおいロイド、ヴァルドの奴を\x01",
            "連れ戻すんじゃなかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#0001Fっと、そうだった。\x01",
            "そっちを優先しよう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_419F")

    label("loc_4122")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_419F")
    TurnDirection(0x101, 0x104, 0)

    #C0113
    ChrTalk(
        0x101,
        (
            "#0005F待ってくれランディ。\x01",
            "今はヴァルドの方を確認したい。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        (
            "#0301Fっと、そうか。\x01",
            "奥に急ごうぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_419F")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 1000, 0)
    EventEnd(0x4)
    Return()

    # Function_28_4090 end

    SaveToFile()

Try(main)
