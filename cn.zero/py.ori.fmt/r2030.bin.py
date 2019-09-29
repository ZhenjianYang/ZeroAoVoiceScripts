from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r2030.bin",                # FileName
        "r2030",                    # MapName
        "r2030",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2030", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 2, 0, 3],
    )

    BuildStringList((
        "r2030",                  # 0
        "克潘",                   # 1
        "彼德",                   # 2
        "巨甲水螅",               # 3
        "车",                     # 4
        "巴士",                   # 5
        "br2000",                 # 6
        "br2000",                 # 7
        "br2000",                 # 8
        "br2000",                 # 9
        "br2000",                 # 10
        "br2000",                 # 11
        "br2000",                 # 12
        "克洛斯贝尔市方向",       # 13
        "人偶工房方向",           # 14
        "矿山镇玛因兹方向",       # 15
    ))

    ATBonus("ATBonus_4B4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2ABA", 0,   10,  3,   0,   2,   0,   5)
    Sepith("Sepith_2ACA", 10,  2,   0,   4,   0,   5,   2)
    Sepith("Sepith_2AB2", 4,   0,   1,   10,  5,   3,   0)
    Sepith("Sepith_2AC2", 9,   0,   4,   0,   2,   0,   7)
    Sepith("Sepith_2AAA", 10,  0,   0,   4,   3,   5,   0)
    Sepith("Sepith_2AEA", 32,  32,  32,  32,  32,  32,  32)

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
    MonsterBattlePostion("MonsterBattlePostion_594", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 0, 0, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_67C", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_2ABA", 30, 40, 20, 10,
        (
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_80C", 0x0010, 14, 6, 90, 0, 1, 5, 0, "br2000", "Sepith_2ACA", 30, 40, 20, 10,
        (
            ("ms77400.dat", 0, 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms77400.dat", "ms77400.dat", 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_744", 0x0000, 14, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_2AB2", 30, 40, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_8D4", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_2AC2", 30, 40, 20, 10,
        (
            ("ms69400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms69400.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms69400.dat", "ms69700.dat", "ms69800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms69400.dat", "ms69700.dat", "ms69800.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_5B4", 0x0000, 14, 6, 45, 10, 1, 30, 0, "br2000", "Sepith_2AAA", 30, 40, 20, 10,
        (
            ("ms62500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms62500.dat", "ms62500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms62500.dat", "ms65900.dat", "ms62500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms62500.dat", "ms62500.dat", "ms65500.dat", "ms62500.dat", 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_99C", 0x0000, 14, 6, 90, 8, 1, 50, 0, "br2000", "Sepith_2AEA", 30, 40, 20, 10,
        (
            ("ms66402.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms66402.dat", "ms66402.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms66402.dat", "ms66402.dat", "ms66402.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms66402.dat", "ms66402.dat", "ms66402.dat", "ms66402.dat", 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_A64", 0x0000, 35, 6, 0, 0, 1, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms77800.dat", "ms77800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_594", "MonsterBattlePostion_574", "ed7401", "ed7403", "ATBonus_4B4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50166.itc",                   # 00
        "apl/ch50165.itc",                   # 01
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
        "monster/ch62550.itc",               # 10
        "monster/ch62551.itc",               # 11
        "monster/ch65950.itc",               # 12
        "monster/ch65951.itc",               # 13
        "monster/ch65550.itc",               # 14
        "monster/ch65551.itc",               # 15
        "monster/ch77450.itc",               # 16
        "monster/ch77450.itc",               # 17
        "monster/ch69450.itc",               # 18
        "monster/ch69450.itc",               # 19
        "monster/ch66450.itc",               # 1A
        "monster/ch66450.itc",               # 1B
        "monster/ch77850.itc",               # 1C
        "monster/ch77851.itc",               # 1D
    ))

    DeclNpc(-61770,  0,       150589,  90,   405,  0x0, 0,   0,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-59430,  0,       145979,  45,   405,  0x0, 0,   1,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-55750,  7500,    67959,   180,  484,  0x0, 0,   28,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-7080,   38670,   1500,    0x1010000,    "BattleInfo_67C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-51440,  65480,   6000,    0x1010000,    "BattleInfo_80C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-34210,  55840,   0,       0x1010000,    "BattleInfo_744", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-22190,  95940,   0,       0x1010000,    "BattleInfo_8D4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-35010,  114720,  0,       0x1010000,    "BattleInfo_8D4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(2700,    112600,  3810,    0x1010000,    "BattleInfo_5B4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-73010,  151070,  0,       0x1010000,    "BattleInfo_67C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-29990,  100980,  0,       0x1010000,    "BattleInfo_99C", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 16,  -29.84000015258789,    82.05000305175781,     -1.0,                  2500.0,                [0.05000000074505806,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.4919999837875366,    -16.410001754760742,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 20,  -42.72999954223633,    124.55999755859375,    -0.5,                  256.0,                 [0.17677663266658783,  0.08838837593793869,   -0.0,                  0.0,                   -0.17677675187587738,  0.08838831633329391,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   29.57297706604004,     -7.232813358306885,    0.10000000149011612,   1.0])

    DeclActor(-55750,  6000,    67960,   1200,    -55750,  7000,    67960,   0x007C, 0,  4,  0x0000)
    DeclActor(-26000,  0,       116600,  1500,    -26000,  1500,    116600,  0x007C, 0,  15, 0x0000)
    DeclActor(-64190,  0,       161190,  1200,    -53600,  -2000,   160500,  0x007C, 0,  14, 0x0000)
    DeclActor(-32950,  0,       55220,   1200,    -32950,  0,       55220,   0x007C, 0,  5,  0x0000)
    DeclActor(-66470,  0,       184850,  1200,    -66470,  0,       184850,  0x007C, 0,  6,  0x0000)
    DeclActor(-61640,  0,       151360,  5000,    -61640,  0,       151360,  0x007C, 0,  18, 0x0000)
    DeclActor(-38630,  0,       101340,  1500,    -38630,  1700,    101340,  0x007C, 0,  19, 0x0000)

    PlaceName(-1.0, 0.0, -15.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(38.25, 0.0, 116.25, 0x0000, 0x0000, "人偶工房方向")
    PlaceName(-86.0, 0.0, 235.0, 0x0000, 0x0000, "矿山镇玛因兹方向")
    PlaceName(-26.0, 0.0, 116.5999984741211, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_B8C",          # 00, 0
        "Function_1_BAB",          # 01, 1
        "Function_2_BC8",          # 02, 2
        "Function_3_C40",          # 03, 3
        "Function_4_E18",          # 04, 4
        "Function_5_10A1",         # 05, 5
        "Function_6_10B5",         # 06, 6
        "Function_7_10C9",         # 07, 7
        "Function_8_10E0",         # 08, 8
        "Function_9_1191",         # 09, 9
        "Function_10_12B2",        # 0A, 10
        "Function_11_13F5",        # 0B, 11
        "Function_12_148A",        # 0C, 12
        "Function_13_15AF",        # 0D, 13
        "Function_14_1688",        # 0E, 14
        "Function_15_1750",        # 0F, 15
        "Function_16_189D",        # 10, 16
        "Function_17_1C37",        # 11, 17
        "Function_18_1DAB",        # 12, 18
        "Function_19_2997",        # 13, 19
        "Function_20_2A0D",        # 14, 20
    ))


    def Function_0_B8C(): pass

    label("Function_0_B8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BAA")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_B8C")

    label("loc_BAA")

    Return()

    # Function_0_B8C end

    def Function_1_BAB(): pass

    label("Function_1_BAB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BC7")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_BAB")

    label("loc_BC7")

    Return()

    # Function_1_BAB end

    def Function_2_BC8(): pass

    label("Function_2_BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_BD6")
    Jump("loc_C1E")

    label("loc_BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_BF8")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    Jump("loc_C1E")

    label("loc_BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C15")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    Jump("loc_C1E")

    label("loc_C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_C1E")

    label("loc_C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_C2D")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 17)

    label("loc_C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_C3C")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 11)

    label("loc_C3C")

    Call(0, 7)
    Return()

    # Function_2_BC8 end

    def Function_3_C40(): pass

    label("Function_3_C40")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C58")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_C58")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C6A")
    Jump("loc_CA7")

    label("loc_C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_CA7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C84")
    Jump("loc_CA7")

    label("loc_C84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_C96")
    Jump("loc_CA7")

    label("loc_C96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_CA7")
    OP_66(0x5, 0x1)

    label("loc_CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBA")
    OP_70(0x0, 0x0)
    Jump("loc_CBE")

    label("loc_CBA")

    OP_70(0x0, 0x1E)

    label("loc_CBE")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 5)), scpexpr(EXPR_END)), "loc_D24")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -32950, 0, 55220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)
    Jump("loc_D7D")

    label("loc_D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 6)), scpexpr(EXPR_END)), "loc_D7D")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -66470, 0, 184850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_D7D")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D95")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_D95")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -53600, -3000, 160500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundDistance(0x7A, 0xFFFF2C20, 0x0, 0x3087C, 0x2710, 0x13880, 0x64, 0x0)
    OP_E1(0xFFFFADBC, 0x0, 0x20E54)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E17")
    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_E17")

    Return()

    # Function_3_C40 end

    def Function_4_E18(): pass

    label("Function_4_E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA7")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从宝箱中感觉到了高级魔兽的气息。\x01",
            "【推定魔兽等级３５】\x01",
            "要打开宝箱吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA7")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_EA7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1063")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA0")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_F00():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F00)

    def lambda_F1A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F1A)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xA, 1)
    Battle("BattleInfo_A64", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_F81"),
        (2, "loc_F90"),
        (1, "loc_F9D"),
        (SWITCH_DEFAULT, "loc_FA0"),
    )


    label("loc_F81")

    SetScenarioFlags(0x72, 3)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_FA0")

    label("loc_F90")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_F9D")

    OP_B7(0x0)
    Return()

    label("loc_FA0")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA2, 1)"), scpexpr(EXPR_END)), "loc_FF7")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x104, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_105E")

    label("loc_FF7")

    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0xA2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0xA2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_105E")

    Jump("loc_1095")

    label("loc_1063")

    FadeToDark(300, 0, 100)

    #A0005
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

    label("loc_1095")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_E18 end

    def Function_5_10A1(): pass

    label("Function_5_10A1")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 5)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_5_10A1 end

    def Function_6_10B5(): pass

    label("Function_6_10B5")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_10B5 end

    def Function_7_10C9(): pass

    label("Function_7_10C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7C, 0)), scpexpr(EXPR_END)), "loc_10DA")
    ClearScenarioFlags(0x7C, 0)
    Jump("loc_10DF")

    label("loc_10DA")

    SetChrFlags(0x14, 0x80)

    label("loc_10DF")

    Return()

    # Function_7_10C9 end

    def Function_8_10E0(): pass

    label("Function_8_10E0")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "克洛斯贝尔市北出口\x01",      # 0
            "矿山镇玛因兹\x01",            # 1
            "放弃\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1169")
    Call(0, 9)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1189")

    label("loc_1169")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1189")
    Call(0, 10)
    ClearMapFlags(0x8000000)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_1189")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_10E0 end

    def Function_9_1191(): pass

    label("Function_9_1191")

    Fade(1000)
    OP_68(-31260, 600, 114980, 0)
    MoveCamera(26, 35, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(23500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -24980, 0, 115700, 225)
    SetChrPos(0x1, -24420, 0, 115080, 225)
    SetChrPos(0x2, -23880, 0, 114510, 225)
    SetChrPos(0x3, -23300, 0, 113860, 225)
    ClearChrFlags(0xC, 0x80)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x1, 0x2)
    OP_78(0x1, 0xC)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xC, -44260, 0, 125040, 45)
    OP_D3(0xC, 0x0, 0xAFC8, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)

    def lambda_126C():
        OP_95(0xFE, -31020, 0, 111190, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_126C)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xC, 1)
    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_9_1191 end

    def Function_10_12B2(): pass

    label("Function_10_12B2")

    Fade(1000)
    OP_68(-27890, 600, 110180, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(23500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -24980, 0, 115700, 225)
    SetChrPos(0x1, -24420, 0, 115080, 225)
    SetChrPos(0x2, -23880, 0, 114510, 225)
    SetChrPos(0x3, -23300, 0, 113860, 225)
    ClearChrFlags(0xC, 0x80)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x1, 0x2)
    OP_78(0x1, 0xC)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xC, -29790, 0, 93520, 0)
    OP_D3(0xC, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)

    def lambda_138D():
        OP_95(0xFE, -28360, 0, 100110, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_138D)
    Sleep(500)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xC, 1)

    def lambda_13BA():
        OP_9E(0xFE, 0xFFFF67A8, 0x19064, 0xFFFF15A0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_13BA)
    WaitChrThread(0xC, 1)
    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_10_12B2 end

    def Function_11_13F5(): pass

    label("Function_11_13F5")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -24980, 0, 115700, 225)
    SetChrPos(0x1, -24980, 0, 115700, 225)
    SetChrPos(0x2, -24980, 0, 115700, 225)
    SetChrPos(0x3, -24980, 0, 115700, 225)
    OP_68(-24980, 600, 115700, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_11_13F5 end

    def Function_12_148A(): pass

    label("Function_12_148A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1570")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1530")

    #C0007
    ChrTalk(
        0xFE,
        "我今天听说了～\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "分部长他们\x01",
            "下次要从利贝尔王国\x01",
            "请来一位技艺超群的钓师哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "……真令人在意的说～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_156B")

    label("loc_1530")


    #C0011
    ChrTalk(
        0xFE,
        (
            "大概超群这个词\x01",
            "令人有些不爽吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "真有点在意的说～\x02",
    )

    CloseMessageWindow()

    label("loc_156B")

    Jump("loc_15AB")

    label("loc_1570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_15AB")

    #C0013
    ChrTalk(
        0xFE,
        "………(发呆～)…………\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "天气真好啊～……\x02",
    )

    CloseMessageWindow()

    label("loc_15AB")

    TalkEnd(0xFE)
    Return()

    # Function_12_148A end

    def Function_13_15AF(): pass

    label("Function_13_15AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1684")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162B")

    #C0015
    ChrTalk(
        0xFE,
        (
            "呵呵，其实我和分部长\x01",
            "设想了一个\x01",
            "小活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "克潘平时\x01",
            "总是单独行动，\x01",
            "真希望他能参加呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1684")

    label("loc_162B")


    #C0017
    ChrTalk(
        0xFE,
        (
            "在这次的纪念庆典，\x01",
            "我们筹划了一个\x01",
            "小活动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "呵呵，要是克潘\x01",
            "也能来参加就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1684")

    TalkEnd(0xFE)
    Return()

    # Function_13_15AF end

    def Function_14_1688(): pass

    label("Function_14_1688")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0019
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
    )

    CloseMessageWindow()
    OP_68(-65120, 3500, 159810, 1500)
    MoveCamera(58, 36, 0, 1500)
    OP_6E(370, 1500)
    SetCameraDistance(25720, 1500)
    Sleep(1000)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要钓鱼吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174B")
    OP_E0(0x2)
    MiniGame(0x6, 0x6, 0xFFFF0088, 0x0, 0x27434, 0x67, 0xFFFF2EA0, 0xFFFFF448, 0x272F4)

    label("loc_174B")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_14_1688 end

    def Function_15_1750(): pass

    label("Function_15_1750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1761")
    Call(0, 8)
    Jump("loc_189C")

    label("loc_1761")

    TalkBegin(0xFF)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17E2")

    #C0022
    ChrTalk(
        0x101,
        (
            "#0000F今天还是不要坐巴士了吧。\x02\x03",

            "为了进行调查，\x01",
            "还是徒步走一走比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1896")

    label("loc_17E2")


    #C0023
    ChrTalk(
        0x104,
        (
            "#0300F唔，开往玛因兹方向的巴士，\x01",
            "似乎是一个小时\x01",
            "来一辆啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#0006F如果坐巴士的话，\x01",
            "就会轻松很多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#0108F（他们两个都是一副轻松自若的样子，\x01",
            "  令人有点不甘心呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1896")

    SetScenarioFlags(0x0, 2)
    TalkEnd(0xFF)

    label("loc_189C")

    Return()

    # Function_15_1750 end

    def Function_16_189D(): pass

    label("Function_16_189D")

    EventBegin(0x0)
    OP_E0(0x3)
    Fade(1000)
    OP_68(-68240, 3000, 154870, 0)
    MoveCamera(50, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(46000, 0)
    SetChrPos(0x101, -30810, 0, 99000, 0)
    SetChrPos(0x102, -29380, 0, 99060, 0)
    SetChrPos(0x103, -30840, 0, 97470, 0)
    SetChrPos(0x104, -29420, 0, 97610, 0)
    OP_68(-51220, 3000, 134370, 12000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(8530, 600, 113580, 0)
    MoveCamera(85, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(56000, 0)
    SetCameraDistance(53000, 6000)
    OP_6F(0x10)
    OP_0D()
    Fade(1000)

    def lambda_1975():
        OP_95(0xFE, -30700, 0, 104000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1975)

    def lambda_198F():
        OP_95(0xFE, -29300, 0, 104000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_198F)

    def lambda_19A9():
        OP_95(0xFE, -30700, 0, 102600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19A9)

    def lambda_19C3():
        OP_95(0xFE, -29300, 0, 102600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19C3)
    OP_68(-30480, 4400, 103110, 0)
    MoveCamera(30, 13, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(20770, 0)
    OP_68(-30480, 2400, 103110, 4000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(-30480, 1400, 103110, 0)
    MoveCamera(30, 13, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(14500, 0)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()

    #C0026
    ChrTalk(
        0x101,
        (
            "#0001F#5P看来，这里似乎\x01",
            "就是山道的岔路口呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0301F#12P唔，好像看不到\x01",
            "什么狼形魔兽啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0103F#11P可能又移动到\x01",
            "其它地方去了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-28670, 1400, 102930, 1000)
    OP_93(0x102, 0x5A, 0x190)
    OP_6F(0x1)

    #C0029
    ChrTalk(
        0x102,
        (
            "#0105F#6P左边是矿山镇方向……\x01",
            "那边是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B58():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B58)
    Sleep(50)

    def lambda_1B68():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B68)
    Sleep(50)

    def lambda_1B78():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B78)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)

    #C0030
    ChrTalk(
        0x103,
        (
            "#0205F#6P……数据库里也\x01",
            "没有相应的情报。\x02\x03",

            "#0201F也许还是去调查一下\x01",
            "比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#0001F#6P嗯……\x01",
            "在前进之前，先去确认一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -30700, 0, 104000, 0)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0x64, 4)
    OP_29(0x40, 0x1, 0x3)
    OP_E0(0x2)
    Call(0, 7)
    EventEnd(0x5)
    Return()

    # Function_16_189D end

    def Function_17_1C37(): pass

    label("Function_17_1C37")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-66420, 2100, 151650, 0)
    MoveCamera(19, 10, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(28380, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x2)
    SetMapObjFlags(0x2, 0x400)
    SetChrFlags(0xB, 0x8000)
    OP_78(0x2, 0xB)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_D3(0xB, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x2, 0x1E)
    OP_70(0x2, 0x0)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0xFA, 0x0)
    SetMapObjFrame(0xFF, "model11_shade", 0x0, 0x1)
    Sound(487, 0, 100, 0)
    OP_68(-61690, 2100, 149860, 7000)
    FadeToBright(1000, 0)
    SetChrPos(0xB, -68170, 250, 169170, 180)

    def lambda_1D36():
        OP_95(0xFE, -67630, 0, 159580, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1D36)
    Sleep(1550)
    Sound(458, 0, 100, 0)

    def lambda_1D59():
        OP_9E(0xFE, 0xFFFF54B6, 0x27524, 0xFFFF7748, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1D59)
    Sleep(2050)

    def lambda_1D77():
        OP_95(0xFE, -53340, 250, 135000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1D77)
    WaitChrThread(0xB, 1)
    OP_0D()
    OP_6F(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_1C37 end

    def Function_18_1DAB(): pass

    label("Function_18_1DAB")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-62080, 2900, 146930, 0)
    MoveCamera(28, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(15120, 0)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, -63780, 0, 154290, 90)
    SetChrPos(0x102, -62070, 0, 153010, 90)
    SetChrPos(0x103, -63380, 0, 151590, 90)
    SetChrPos(0x104, -61980, 0, 150430, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0032
    ChrTalk(
        0x103,
        (
            "#6P#0205F……不管看多少次，也都觉得很壮观呢。\x01",
            "竟然能在这么近的地方观赏瀑布……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#12P#0100F嗯，这么壮观的瀑布，\x01",
            "在国外也很少见呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#6P#0000F怎么说呢，只要看着它，\x01",
            "就感觉心情好像平静下来了。\x02\x03",

            "#0004F心灵受到洗涤，\x01",
            "说的大概就是\x01",
            "这种感觉吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#12P#0304F噢噢，这样的话，\x01",
            "要不要来个瀑布修行呢？\x02\x03",

            "#0309F穿条兜裆布，盘坐在瀑布之下，\x01",
            "说不定会突然开窍，领悟出什么呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#6P#0006F……好像很危险，还是算了吧。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#6P#0211F……在那之前，实在是太丢脸了，\x01",
            "请不要让人想象到那种场景。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#12P#0309F哈哈哈，不要害羞嘛。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#6P#0000F这个暂且不提……\x01",
            "格蕾丝小姐委托我们拍摄的照片，\x01",
            "在这里似乎能拍到很不错的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_264F")
    TurnDirection(0x101, 0x102, 500)

    #C0040
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么艾莉，\x01",
            "可以拜托你来拍照吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0041
    ChrTalk(
        0x102,
        (
            "#12P#0108F哎，好的。\x01",
            "虽然我没什么自信……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0042
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

    #C0043
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

            "有时只要错过那一瞬的时机，\x01",
            "就再也拍不到\x01",
            "那么好的风景了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
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

    #C0045
    ChrTalk(
        0x104,
        (
            "#12P#0306F唔……\x01",
            "你在说谁啊，说谁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#6P#0000F好啦好啦，\x01",
            "总之就交给艾莉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#12P#0100F那么……\x01",
            "我来试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x5A, 0x1F4)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_93(0x103, 0x5A, 0x1F4)
    OP_93(0x104, 0x5A, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
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

    #C0048
    ChrTalk(
        0x102,
        (
            "#12P#0103F……呼，\x01",
            "为了保险起见，我多拍了几张。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#6P#0000F看样子，似乎已经拍好了呢。\x02\x03",

            "感觉怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        (
            "#12P#0100F在没有实际显像出来之前，\x01",
            "还无法确定……\x02\x03",

            "不过，我觉得至少\x01",
            "不会很差吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x103,
        (
            "#6P#0200F艾莉前辈似乎\x01",
            "找回感觉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#12P#0300F哼……\x01",
            "反正只有我完全搞不懂。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#6P#0000F如果发现了这种风景漂亮的地方，\x01",
            "就再拍些照片吧。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_295B")

    label("loc_264F")

    TurnDirection(0x101, 0x102, 500)

    #C0054
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么……\x01",
            "艾莉，麻烦你拍照了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        "#12P#0100F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x5A, 0x1F4)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_93(0x103, 0x5A, 0x1F4)
    OP_93(0x104, 0x5A, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
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

    #C0056
    ChrTalk(
        0x102,
        (
            "#12P#0103F……呼，\x01",
            "大概就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_27D3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_27D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_27EA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_27EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2801")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2801")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_2818")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2818")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_282F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_282F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_2846")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2846")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_285D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_285D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2874")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2874")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_288B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_288B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291B")

    #C0057
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
    Jump("loc_295B")

    label("loc_291B")


    #C0058
    ChrTalk(
        0x101,
        (
            "#6P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_295B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -61640, 0, 151360, 90)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x6)
    Sleep(500)
    ClearMapFlags(0x8000000)
    OP_37()
    OP_65(0x5, 0x1)
    EventEnd(0x5)
    Return()

    # Function_18_1DAB end

    def Function_19_2997(): pass

    label("Function_19_2997")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南·克洛斯贝尔市　　１５９赛尔矩\x01",
            "北·矿山镇玛因兹　　１５２赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_2997 end

    def Function_20_2A0D(): pass

    label("Function_20_2A0D")

    EventBegin(0x1)

    #C0060
    ChrTalk(
        0x101,
        (
            "#0005F右边好像也有山道……\x01",
            "先去那边调查吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -37920, 0, 119750, 135)
    OP_68(-37920, 600, 119750, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    EventEnd(0x4)
    Return()

    # Function_20_2A0D end

    SaveToFile()

Try(main)
