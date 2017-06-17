from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "コパン",                 # 1
        "ペーター",               # 2
        "ヒュドラアーマー",       # 3
        "車",                     # 4
        "バス",                   # 5
        "br2000",                 # 6
        "br2000",                 # 7
        "br2000",                 # 8
        "br2000",                 # 9
        "br2000",                 # 10
        "br2000",                 # 11
        "br2000",                 # 12
        "クロスベル市方面",       # 13
        "人形工房方面",           # 14
        "鉱山町マインツ方面",     # 15
    ))

    ATBonus("ATBonus_4B4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2CF1", 0,   10,  3,   0,   2,   0,   5)
    Sepith("Sepith_2D01", 10,  2,   0,   4,   0,   5,   2)
    Sepith("Sepith_2CE9", 4,   0,   1,   10,  5,   3,   0)
    Sepith("Sepith_2CF9", 9,   0,   4,   0,   2,   0,   7)
    Sepith("Sepith_2CE1", 10,  0,   0,   4,   3,   5,   0)
    Sepith("Sepith_2D21", 32,  32,  32,  32,  32,  32,  32)

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
        "BattleInfo_67C", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_2CF1", 30, 40, 20, 10,
        (
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_80C", 0x0010, 14, 6, 90, 0, 1, 5, 0, "br2000", "Sepith_2D01", 30, 40, 20, 10,
        (
            ("ms77400.dat", 0, 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms77400.dat", "ms77400.dat", 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_744", 0x0000, 14, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_2CE9", 30, 40, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_8D4", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_2CF9", 30, 40, 20, 10,
        (
            ("ms69400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms69400.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms69400.dat", "ms69700.dat", "ms69800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms69400.dat", "ms69700.dat", "ms69800.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_5B4", 0x0000, 14, 6, 45, 10, 1, 30, 0, "br2000", "Sepith_2CE1", 30, 40, 20, 10,
        (
            ("ms62500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms62500.dat", "ms62500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms62500.dat", "ms65900.dat", "ms62500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
            ("ms62500.dat", "ms62500.dat", "ms65500.dat", "ms62500.dat", 0, 0, 0, 0, "MonsterBattlePostion_4F4", "MonsterBattlePostion_574", "ed7400", "ed7403", "ATBonus_4B4"),
        )
    )

    BattleInfo(
        "BattleInfo_99C", 0x0000, 14, 6, 90, 8, 1, 50, 0, "br2000", "Sepith_2D21", 30, 40, 20, 10,
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

    PlaceName(-1.0, 0.0, -15.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(38.25, 0.0, 116.25, 0x0000, 0x0000, "人形工房方面")
    PlaceName(-86.0, 0.0, 235.0, 0x0000, 0x0000, "鉱山町マインツ方面")
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
        "Function_5_10CE",         # 05, 5
        "Function_6_10E2",         # 06, 6
        "Function_7_10F6",         # 07, 7
        "Function_8_110D",         # 08, 8
        "Function_9_11C4",         # 09, 9
        "Function_10_12E5",        # 0A, 10
        "Function_11_1428",        # 0B, 11
        "Function_12_14BD",        # 0C, 12
        "Function_13_1606",        # 0D, 13
        "Function_14_1739",        # 0E, 14
        "Function_15_180D",        # 0F, 15
        "Function_16_196E",        # 10, 16
        "Function_17_1D5E",        # 11, 17
        "Function_18_1ED2",        # 12, 18
        "Function_19_2BB6",        # 13, 19
        "Function_20_2C30",        # 14, 20
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBB")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱の中から強力な魔獣の気配を感じる。\x01",
            "【推定魔獣レベル３５】\x01",
            "宝箱を開きますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBB")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_EBB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1088")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB6")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_F14():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F14)

    def lambda_F2E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F2E)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_F97"),
        (2, "loc_FA6"),
        (1, "loc_FB3"),
        (SWITCH_DEFAULT, "loc_FB6"),
    )


    label("loc_F97")

    SetScenarioFlags(0x72, 3)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_FB6")

    label("loc_FA6")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_FB3")

    OP_B7(0x0)
    Return()

    label("loc_FB6")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA2, 1)"), scpexpr(EXPR_END)), "loc_1013")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x104, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1083")

    label("loc_1013")

    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xA2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xA2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1083")

    Jump("loc_10C2")

    label("loc_1088")

    FadeToDark(300, 0, 100)

    #A0005
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

    label("loc_10C2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_E18 end

    def Function_5_10CE(): pass

    label("Function_5_10CE")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 5)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_5_10CE end

    def Function_6_10E2(): pass

    label("Function_6_10E2")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_10E2 end

    def Function_7_10F6(): pass

    label("Function_7_10F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7C, 0)), scpexpr(EXPR_END)), "loc_1107")
    ClearScenarioFlags(0x7C, 0)
    Jump("loc_110C")

    label("loc_1107")

    SetChrFlags(0x14, 0x80)

    label("loc_110C")

    Return()

    # Function_7_10F6 end

    def Function_8_110D(): pass

    label("Function_8_110D")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "クロスベル市北口\x01",      # 0
            "鉱山町マインツ\x01",        # 1
            "やめる\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119C")
    Call(0, 9)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_11BC")

    label("loc_119C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BC")
    Call(0, 10)
    ClearMapFlags(0x8000000)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_11BC")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_110D end

    def Function_9_11C4(): pass

    label("Function_9_11C4")

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

    def lambda_129F():
        OP_95(0xFE, -31020, 0, 111190, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_129F)
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

    # Function_9_11C4 end

    def Function_10_12E5(): pass

    label("Function_10_12E5")

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

    def lambda_13C0():
        OP_95(0xFE, -28360, 0, 100110, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_13C0)
    Sleep(500)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xC, 1)

    def lambda_13ED():
        OP_9E(0xFE, 0xFFFF67A8, 0x19064, 0xFFFF15A0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_13ED)
    WaitChrThread(0xC, 1)
    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_10_12E5 end

    def Function_11_1428(): pass

    label("Function_11_1428")

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

    # Function_11_1428 end

    def Function_12_14BD(): pass

    label("Function_12_14BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_15C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1579")

    #C0007
    ChrTalk(
        0xFE,
        "今日聞いたんすけどー。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "支部長たち、\x01",
            "今度リベール王国から\x01",
            "凄腕の釣師を呼ぶそうっすよ。\x02",
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
        "……なんか気になるっすねー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15C4")

    label("loc_1579")


    #C0011
    ChrTalk(
        0xFE,
        (
            "凄腕ってトコが\x01",
            "カチンと来るっつーか。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "ちょっと気になるっすねー。\x02",
    )

    CloseMessageWindow()

    label("loc_15C4")

    Jump("loc_1602")

    label("loc_15C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1602")

    #C0013
    ChrTalk(
        0xFE,
        "………ぼけ～…………\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "いい天気だ～……\x02",
    )

    CloseMessageWindow()

    label("loc_1602")

    TalkEnd(0xFE)
    Return()

    # Function_12_14BD end

    def Function_13_1606(): pass

    label("Function_13_1606")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1735")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16BA")

    #C0015
    ChrTalk(
        0xFE,
        (
            "うふふ、実は私と支部長で\x01",
            "ちょっとしたイベントを\x01",
            "考えていまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "コパン君は普段から\x01",
            "単独行動ばかりですから、\x01",
            "参加して欲しいんですけどねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1735")

    label("loc_16BA")


    #C0017
    ChrTalk(
        0xFE,
        (
            "今度の記念祭には\x01",
            "ちょっとしたイベントを\x01",
            "考えているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "うふふ、コパン君も\x01",
            "参加してくれると嬉しいですねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1735")

    TalkEnd(0xFE)
    Return()

    # Function_13_1606 end

    def Function_14_1739(): pass

    label("Function_14_1739")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0019
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1808")
    OP_E0(0x2)
    MiniGame(0x6, 0x6, 0xFFFF0088, 0x0, 0x27434, 0x67, 0xFFFF2EA0, 0xFFFFF448, 0x272F4)

    label("loc_1808")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_14_1739 end

    def Function_15_180D(): pass

    label("Function_15_180D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_181E")
    Call(0, 8)
    Jump("loc_196D")

    label("loc_181E")

    TalkBegin(0xFF)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18B1")

    #C0022
    ChrTalk(
        0x101,
        (
            "#0000F今日はバスは使わないでおこう。\x02\x03",

            "調査の為には、街道も\x01",
            "足で歩いた方が良さそうだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1967")

    label("loc_18B1")


    #C0023
    ChrTalk(
        0x104,
        (
            "#0300Fふむ、マインツ方面のバスは\x01",
            "１時間に１本くらい\x01",
            "あるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#0006Fバスが使えれば\x01",
            "楽なんだけどなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#0108F（２人とも余裕があるのが\x01",
            "  ちょっと悔しいわね……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1967")

    SetScenarioFlags(0x0, 2)
    TalkEnd(0xFF)

    label("loc_196D")

    Return()

    # Function_15_180D end

    def Function_16_196E(): pass

    label("Function_16_196E")

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

    def lambda_1A46():
        OP_95(0xFE, -30700, 0, 104000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A46)

    def lambda_1A60():
        OP_95(0xFE, -29300, 0, 104000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A60)

    def lambda_1A7A():
        OP_95(0xFE, -30700, 0, 102600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A7A)

    def lambda_1A94():
        OP_95(0xFE, -29300, 0, 102600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A94)
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
            "#0001F#5Pどうやらここが\x01",
            "山道の分岐点みたいだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0301F#12Pふむ、狼型魔獣ってのは\x01",
            "見当たらなさそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0103F#11Pまた他の場所に\x01",
            "移動したのかもしれないわね。\x02",
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
            "#0105F#6P左の方が鉱山町方面として……\x01",
            "あちらの方には何があるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C63():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C63)
    Sleep(50)

    def lambda_1C73():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C73)
    Sleep(50)

    def lambda_1C83():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C83)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)

    #C0030
    ChrTalk(
        0x103,
        (
            "#0205F#6P……データベースにも\x01",
            "該当する情報はありません。\x02\x03",

            "#0201F一応、調べた方が\x01",
            "いいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#0001F#6Pああ……\x01",
            "先に進む前に確かめてみよう。\x02",
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

    # Function_16_196E end

    def Function_17_1D5E(): pass

    label("Function_17_1D5E")

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

    def lambda_1E5D():
        OP_95(0xFE, -67630, 0, 159580, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E5D)
    Sleep(1550)
    Sound(458, 0, 100, 0)

    def lambda_1E80():
        OP_9E(0xFE, 0xFFFF54B6, 0x27524, 0xFFFF7748, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E80)
    Sleep(2050)

    def lambda_1E9E():
        OP_95(0xFE, -53340, 250, 135000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E9E)
    WaitChrThread(0xB, 1)
    OP_0D()
    OP_6F(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_1D5E end

    def Function_18_1ED2(): pass

    label("Function_18_1ED2")

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
            "#6P#0205F……何度見てもすごいですね。\x01",
            "こんなに間近で滝を見られるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#12P#0100Fえぇ、こんな立派な滝は\x01",
            "外国にもそうそう無いわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#6P#0000Fなんていうかこう、\x01",
            "見ていると落ち着いて来るな。\x02\x03",

            "#0004F心が洗われるってのは\x01",
            "こういうことをいうのかも\x01",
            "しれないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#12P#0304Fおぉ、なんなら\x01",
            "滝修行でもしてみるか？\x02\x03",

            "#0309Fふんどし一丁で滝に当たれば、\x01",
            "悟りが開けるかも知れねぇぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#6P#0006F……危なそうだから遠慮しとくよ。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#6P#0211F……というか、見苦しいものを\x01",
            "想像させないでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#12P#0309Fはっはっは、照れるなよ。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれはともかく……\x01",
            "グレイスさんに依頼された写真、\x01",
            "ここならいいものが撮れそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_282C")
    TurnDirection(0x101, 0x102, 500)

    #C0040
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれじゃあエリィ、\x01",
            "撮影をお願いできるかな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0041
    ChrTalk(
        0x102,
        (
            "#12P#0108Fえ、ええ。\x01",
            "ちょっと自信はないけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0042
    ChrTalk(
        0x104,
        (
            "#12P#0300Fいやいや、大丈夫だろ。\x02\x03",

            "ちょっとレンズを覗いて\x01",
            "パチリと撮っちまえば\x01",
            "終わりじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0043
    ChrTalk(
        0x102,
        (
            "#12P#0103Fあのねぇ……\x01",
            "いい写真を撮るのは\x01",
            "そんな簡単なことじゃないのよ。\x02\x03",

            "#0100Fフレームの中に\x01",
            "対象物をどう収めるか、\x01",
            "構成を練らなきゃいけないし……\x02\x03",

            "天気や風の影響で\x01",
            "写真の印象もガラリと変わってしまう。\x02\x03",

            "ある一瞬を逃したら\x01",
            "二度と撮れないことだって\x01",
            "あるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        (
            "#6P#0200F素人とプロの写真を見比べると\x01",
            "一目で違いが分かりますからね。\x02\x03",

            "#0203F粗雑な人には、その繊細さが\x01",
            "理解できないかも知れませんが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0045
    ChrTalk(
        0x104,
        (
            "#12P#0306Fぐっ……\x01",
            "誰のことを言ってんだ、誰の。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#6P#0000Fま、まぁまぁ。\x01",
            "ここはエリィに任せてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#12P#0100Fそれじゃあ……\x01",
            "やってみるわね。\x02",
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
            "#12P#0103F……ふぅ。\x01",
            "念のため何枚か撮っておいたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#6P#0000Fどうやら撮れたみたいだな。\x02\x03",

            "出来栄えはどんな感じだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        (
            "#12P#0100F実際に現像してみないと\x01",
            "分からないけど……\x02\x03",

            "少なくとも、\x01",
            "悪い写真ではないとは思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x103,
        (
            "#6P#0200Fエリィさんも\x01",
            "カンを取り戻せたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#12P#0300Fふーん……\x01",
            "俺にはさっぱりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#6P#0000Fまたこういう場所を見つけたら\x01",
            "写真に収めていこう。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7A")

    label("loc_282C")

    TurnDirection(0x101, 0x102, 500)

    #C0054
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれじゃあ……\x01",
            "エリィ、撮影を頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        "#12P#0100Fええ、分かったわ。\x02",
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
            "#12P#0103F……ふぅ。\x01",
            "こんなところかしら。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_29C4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_29DB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_29F2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_2A09")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2A20")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_2A37")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2A4E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2A65")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_2A7C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B26")

    #C0057
    ChrTalk(
        0x101,
        (
            "#6P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "これでグレイスさんに提示された\x01",
            "５枚ってノルマは達成できた。\x01",
            "これでいつでも提出できそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7A")

    label("loc_2B26")


    #C0058
    ChrTalk(
        0x101,
        (
            "#6P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7A")

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

    # Function_18_1ED2 end

    def Function_19_2BB6(): pass

    label("Function_19_2BB6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南・クロスベル市　　１５９セルジュ\x01",
            "北・鉱山町マインツ　１５２セルジュ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_2BB6 end

    def Function_20_2C30(): pass

    label("Function_20_2C30")

    EventBegin(0x1)

    #C0060
    ChrTalk(
        0x101,
        (
            "#0005F右手にも山道があるみたいだ……\x01",
            "先にそっちを調べてみよう。\x02",
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

    # Function_20_2C30 end

    SaveToFile()

Try(main)
