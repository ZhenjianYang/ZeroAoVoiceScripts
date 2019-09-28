from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r4010.bin",                # FileName
        "r4010",                    # MapName
        "r4010",                    # Location
        0x00A3,                     # MapIndex
        "ed7250",
        0x00000000,                 # Flags
        ("r4010", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x24,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 100000, 0, 0, 1, 163, 0, 3, 0, 4],
    )

    BuildStringList((
        "r4010",                  # 0
        "红耀辣椒",               # 1
        "红耀辣椒",               # 2
        "硬岩龙",                 # 3
        "硬岩龙",                 # 4
        "寒冰至尊",               # 5
        "车",                     # 6
        "列车",                   # 7
        "SE控制",                 # 8
        "br4000",                 # 9
        "br4000",                 # 10
        "br4000",                 # 11
        "br4000",                 # 12
        "br4000",                 # 13
        "br4000",                 # 14
        "br4000",                 # 15
        "br4000",                 # 16
        "克洛斯贝尔市·贝尔加德门方向",# 17
        "警察学校",               # 18
    ))

    ATBonus("ATBonus_454", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_474", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_27AD", 3,   0,   6,   1,   3,   2,   0)
    Sepith("Sepith_27A5", 5,   0,   0,   3,   3,   3,   0)
    Sepith("Sepith_2795", 4,   2,   3,   2,   1,   1,   1)
    Sepith("Sepith_278D", 2,   2,   0,   4,   3,   0,   3)
    Sepith("Sepith_279D", 2,   2,   0,   2,   2,   2,   4)

    MonsterBattlePostion("MonsterBattlePostion_4B4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4CC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_514", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_518", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_51C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_520", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_524", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_528", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_52C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_530", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_494", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_49C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_534", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_538", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_53C", 2, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_540", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_544", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_548", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_54C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_550", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_874", 0x0000, 51, 6, 60, 8, 1, 30, 0, "br4000", "Sepith_27AD", 20, 20, 30, 20,
        (
            ("ms78700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms78700.dat", "ms78700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms78700.dat", "ms78700.dat", "ms78700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms78700.dat", "ms78700.dat", "ms83000.dat", "ms78700.dat", 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
        )
    )

    BattleInfo(
        "BattleInfo_7AC", 0x0000, 51, 6, 60, 8, 1, 40, 0, "br4000", "Sepith_27A5", 20, 40, 30, 10,
        (
            ("ms81600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms81600.dat", "ms81600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms81600.dat", "ms81600.dat", "ms81600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms81600.dat", "ms81600.dat", "ms81600.dat", "ms81600.dat", 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
        )
    )

    BattleInfo(
        "BattleInfo_61C", 0x0000, 51, 6, 60, 8, 1, 35, 0, "br4000", "Sepith_2795", 20, 40, 30, 10,
        (
            ("ms84700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms84700.dat", "ms84700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms84700.dat", "ms84700.dat", "ms84700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms84700.dat", "ms84700.dat", "ms84700.dat", "ms84700.dat", 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
        )
    )

    BattleInfo(
        "BattleInfo_554", 0x0000, 51, 6, 60, 8, 1, 25, 0, "br4000", "Sepith_278D", 20, 40, 30, 10,
        (
            ("ms78900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms78900.dat", "ms78900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms78900.dat", "ms78900.dat", "ms78900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms78900.dat", "ms78900.dat", "ms78900.dat", "ms78900.dat", 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
        )
    )

    BattleInfo(
        "BattleInfo_6E4", 0x0000, 51, 6, 60, 8, 1, 30, 0, "br4000", "Sepith_279D", 20, 20, 30, 20,
        (
            ("ms78600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms78600.dat", "ms78600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms78600.dat", "ms78600.dat", "ms78600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
            ("ms78600.dat", "ms78600.dat", "ms83000.dat", "ms78600.dat", 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_454"),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_9C4", 0x0000, 100, 6, 0, 0, 1, 0, 0, "br4000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63100.dat", "ms63100.dat", "ms63100.dat", "ms63100.dat", "ms63100.dat", "ms63100.dat", 0, 0, "MonsterBattlePostion_534", "MonsterBattlePostion_514", "ed7451", "ed7453", "ATBonus_474"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_93C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br4000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms78700.dat", "ms78700.dat", "ms78700.dat", "ms78700.dat", "ms78700.dat", "ms78700.dat", "ms78700.dat", "ms78700.dat", "MonsterBattlePostion_494", "MonsterBattlePostion_514", "ed7453", "ed7453", "ATBonus_454"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_980", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br4000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_514", "ed7453", "ed7453", "ATBonus_454"),
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
        "monster/ch78950.itc",               # 10
        "monster/ch78951.itc",               # 11
        "monster/ch84750.itc",               # 12
        "monster/ch84751.itc",               # 13
        "monster/ch78650.itc",               # 14
        "monster/ch78651.itc",               # 15
        "monster/ch81650.itc",               # 16
        "monster/ch81651.itc",               # 17
        "monster/ch78750.itc",               # 18
        "monster/ch78751.itc",               # 19
        "monster/ch60750.itc",               # 1A
        "monster/ch60750.itc",               # 1B
        "monster/ch63150.itc",               # 1C
        "monster/ch63150.itc",               # 1D
    ))

    DeclNpc(85910,   12000,   42040,   270,  485,  0x0, 0,   24,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(20270,   11750,   26950,   270,  485,  0x0, 0,   24,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(85910,   12000,   42040,   270,  485,  0x0, 0,   26,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(20270,   11750,   26950,   270,  485,  0x0, 0,   26,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(80559,   18500,   89440,   180,  484,  0x0, 0,   28,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(8510,    70340,   3720,    0x1010104,    "BattleInfo_874", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(53880,   77990,   4990,    0x1010104,    "BattleInfo_7AC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(67370,   38810,   7490,    0x1010035,    "BattleInfo_61C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(32009,   34250,   11150,   0x10100AA,    "BattleInfo_554", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(5340,    11350,   11810,   0x1010096,    "BattleInfo_874", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(7500,    -44510,  18000,   0x101014C,    "BattleInfo_7AC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-33250,  -82690,  24000,   0x1010140,    "BattleInfo_6E4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-69850,  -86710,  24000,   0x1010126,    "BattleInfo_554", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(88950,   46450,   12000,   0x1010087,    "BattleInfo_61C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(84500,   87290,   18000,   0x1010077,    "BattleInfo_874", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(73770,   26630,   23000,   0x10100AA,    "BattleInfo_6E4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(36900,   14730,   21000,   0x101015E,    "BattleInfo_7AC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(29220,   660,     20500,   0x101015E,    "BattleInfo_554", 0,   16,  0xFFFF, 0,  1)

    DeclActor(80560,   18000,   89440,   1200,    80560,   19000,   89440,   0x007C, 0,  5,  0x0000)
    DeclActor(-17440,  24000,   -82060,  1200,    -17440,  25000,   -82060,  0x007C, 0,  6,  0x0000)
    DeclActor(85910,   12000,   42040,   1200,    85910,   12000,   42040,   0x007C, 0,  7,  0x0000)
    DeclActor(20270,   11750,   26950,   1200,    20270,   11750,   26950,   0x007C, 0,  8,  0x0000)

    PlaceName(0.0, 0.0, 150.0, 0x0000, 0x0000, "克洛斯贝尔市·贝尔加德门方向")
    PlaceName(-140.0, 0.0, -80.0, 0x0000, 0x0000, "警察学校")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 2
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 7
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 8
    ChipFrameInfo(1299, 0, [1, 2, 0, 3, 4, 0])                   # 9

    ScpFunction((
        "Function_0_ACC",          # 00, 0
        "Function_1_AE8",          # 01, 1
        "Function_2_B07",          # 02, 2
        "Function_3_B24",          # 03, 3
        "Function_4_FF5",          # 04, 4
        "Function_5_145A",         # 05, 5
        "Function_6_16E8",         # 06, 6
        "Function_7_1841",         # 07, 7
        "Function_8_1B6B",         # 08, 8
        "Function_9_1E95",         # 09, 9
        "Function_10_20FE",        # 0A, 10
        "Function_11_2171",        # 0B, 11
        "Function_12_21E4",        # 0C, 12
        "Function_13_2265",        # 0D, 13
        "Function_14_22CA",        # 0E, 14
        "Function_15_22E3",        # 0F, 15
        "Function_16_231D",        # 10, 16
        "Function_17_232D",        # 11, 17
        "Function_18_26EC",        # 12, 18
    ))


    def Function_0_ACC(): pass

    label("Function_0_ACC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AE7")
    OP_A1(0xFE, 0x320, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_ACC")

    label("loc_AE7")

    Return()

    # Function_0_ACC end

    def Function_1_AE8(): pass

    label("Function_1_AE8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B06")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_AE8")

    label("loc_B06")

    Return()

    # Function_1_AE8 end

    def Function_2_B07(): pass

    label("Function_2_B07")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B23")
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_2_B07")

    label("loc_B23")

    Return()

    # Function_2_B07 end

    def Function_3_B24(): pass

    label("Function_3_B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_B38")
    ClearScenarioFlags(0x22, 0)
    Event(0, 9)
    Jump("loc_B47")

    label("loc_B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_B47")
    ClearScenarioFlags(0x22, 1)
    Event(0, 17)

    label("loc_B47")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FF4")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDD")
    SetScenarioFlags(0x38, 0)

    label("loc_BDD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF3")
    SetScenarioFlags(0x38, 1)

    label("loc_BF3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C09")
    SetScenarioFlags(0x38, 2)

    label("loc_C09")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1F")
    SetScenarioFlags(0x38, 3)

    label("loc_C1F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C35")
    SetScenarioFlags(0x38, 4)

    label("loc_C35")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4B")
    SetScenarioFlags(0x38, 5)

    label("loc_C4B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C61")
    SetScenarioFlags(0x38, 6)

    label("loc_C61")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C77")
    SetScenarioFlags(0x38, 7)

    label("loc_C77")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8D")
    SetScenarioFlags(0x39, 0)

    label("loc_C8D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA3")
    SetScenarioFlags(0x39, 1)

    label("loc_CA3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB9")
    SetScenarioFlags(0x39, 2)

    label("loc_CB9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCF")
    SetScenarioFlags(0x39, 3)

    label("loc_CCF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE5")
    SetScenarioFlags(0x39, 4)

    label("loc_CE5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFB")
    SetScenarioFlags(0x39, 5)

    label("loc_CFB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D11")
    SetScenarioFlags(0x39, 6)

    label("loc_D11")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D27")
    SetScenarioFlags(0x39, 7)

    label("loc_D27")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3D")
    SetScenarioFlags(0x3A, 0)

    label("loc_D3D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D53")
    SetScenarioFlags(0x3A, 1)

    label("loc_D53")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D69")
    SetScenarioFlags(0x3A, 2)

    label("loc_D69")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7F")
    SetScenarioFlags(0x3A, 3)

    label("loc_D7F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D95")
    SetScenarioFlags(0x3A, 4)

    label("loc_D95")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAB")
    SetScenarioFlags(0x3A, 5)

    label("loc_DAB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC1")
    SetScenarioFlags(0x3A, 6)

    label("loc_DC1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD7")
    SetScenarioFlags(0x3A, 7)

    label("loc_DD7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DED")
    SetScenarioFlags(0x3B, 0)

    label("loc_DED")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E03")
    SetScenarioFlags(0x3B, 1)

    label("loc_E03")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E19")
    SetScenarioFlags(0x3B, 2)

    label("loc_E19")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2F")
    SetScenarioFlags(0x3B, 3)

    label("loc_E2F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E45")
    SetScenarioFlags(0x3B, 4)

    label("loc_E45")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5B")
    SetScenarioFlags(0x3B, 5)

    label("loc_E5B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E71")
    SetScenarioFlags(0x3B, 6)

    label("loc_E71")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E87")
    SetScenarioFlags(0x3B, 7)

    label("loc_E87")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9D")
    SetScenarioFlags(0x3D, 5)

    label("loc_E9D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB3")
    SetScenarioFlags(0x3D, 6)

    label("loc_EB3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC9")
    SetScenarioFlags(0x3D, 7)

    label("loc_EC9")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F04")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_FF4")

    label("loc_F04")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F27")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_FF4")

    label("loc_F27")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4A")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_FF4")

    label("loc_F4A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6D")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_FF4")

    label("loc_F6D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F90")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_FF4")

    label("loc_F90")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB3")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_FF4")

    label("loc_FB3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD6")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_FF4")

    label("loc_FD6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF4")
    SetScenarioFlags(0x3C, 7)

    label("loc_FF4")

    Return()

    # Function_3_B24 end

    def Function_4_FF5(): pass

    label("Function_4_FF5")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF2D100C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1010")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1023")
    OP_1B(0x1, 0x0, 0x12)

    label("loc_1023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10A7")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_10A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1176")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x12C, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    ClearMapObjFlags(0x1E, 0x4)
    ClearMapObjFlags(0x1F, 0x4)
    Jump("loc_121E")

    label("loc_1176")

    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1F, 0x4)

    label("loc_121E")

    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1391")
    OP_70(0x0, 0x0)
    Jump("loc_1395")

    label("loc_1391")

    OP_70(0x0, 0x1E)

    label("loc_1395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A8")
    OP_70(0x1, 0x0)
    Jump("loc_13AC")

    label("loc_13A8")

    OP_70(0x1, 0x1E)

    label("loc_13AC")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_140D")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 85910, 12000, 42040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_140D")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1459")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, 20270, 11750, 26950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1459")

    Return()

    # Function_4_FF5 end

    def Function_5_145A(): pass

    label("Function_5_145A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14EA")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从宝箱中感觉到了强大魔兽的气息。\x01",
            "【推测魔兽等级１００】\x01",
            "要打开宝箱吗?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14EA")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_14EA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16AA")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E7")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1547():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1547)

    def lambda_1561():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1561)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

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
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_9C4", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_15C8"),
        (2, "loc_15D7"),
        (1, "loc_15E4"),
        (SWITCH_DEFAULT, "loc_15E7"),
    )


    label("loc_15C8")

    SetScenarioFlags(0x214, 4)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_15E7")

    label("loc_15D7")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_15E4")

    OP_B9(0x0)
    Return()

    label("loc_15E7")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('辰星铃', 1)"), scpexpr(EXPR_END)), "loc_163E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E4, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_16A5")

    label("loc_163E")

    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0xA6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0xA6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_16A5")

    Jump("loc_16DC")

    label("loc_16AA")

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

    label("loc_16DC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_145A end

    def Function_6_16E8(): pass

    label("Function_6_16E8")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1812")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 40)
    AddSepith(0x1, 40)
    AddSepith(0x2, 40)
    AddSepith(0x3, 40)
    AddSepith(0x4, 40)
    AddSepith(0x5, 40)
    AddSepith(0x6, 40)

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×４０\x01\x07\x02",

            "#57I水之耀晶片×４０\x01\x07\x02",

            "#58I火之耀晶片×４０\x01\x07\x02",

            "#59I风之耀晶片×４０\x01\x07\x02",

            "#60I时之耀晶片×４０\x01\x07\x02",

            "#61I空之耀晶片×４０\x01\x07\x02",

            "#62I幻之耀晶片×４０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E4, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_182F")

    label("loc_1812")


    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_182F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_16E8 end

    def Function_7_1841(): pass

    label("Function_7_1841")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19DF")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_END)), "loc_19C0")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BB")
    ClearScenarioFlags(0x3B, 4)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_19B8")
    ClearScenarioFlags(0x39, 4)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_18E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_18E3)
    TurnDirection(0x8, 0x0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    PlayEffect(0x7, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_93C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B3")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_199A")
    Call(1, 5)
    Jump("loc_19B3")

    label("loc_199A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_19B0")
    Call(1, 4)
    Jump("loc_19B3")

    label("loc_19B0")

    Call(1, 3)

    label("loc_19B3")

    Jump("loc_19BB")

    label("loc_19B8")

    Call(1, 1)

    label("loc_19BB")

    Jump("loc_19D6")

    label("loc_19C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_19D6")
    ClearScenarioFlags(0x39, 4)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_19D6")

    TalkEnd(0xFF)
    Return()

    label("loc_19DF")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 4)), scpexpr(EXPR_END)), "loc_1B50")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4B")
    ClearScenarioFlags(0x3B, 4)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_1B48")
    ClearScenarioFlags(0x39, 4)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1A73():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1A73)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_980", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B43")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B2A")
    Call(1, 5)
    Jump("loc_1B43")

    label("loc_1B2A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B40")
    Call(1, 4)
    Jump("loc_1B43")

    label("loc_1B40")

    Call(1, 3)

    label("loc_1B43")

    Jump("loc_1B4B")

    label("loc_1B48")

    Call(1, 1)

    label("loc_1B4B")

    Jump("loc_1B66")

    label("loc_1B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 4)), scpexpr(EXPR_END)), "loc_1B66")
    ClearScenarioFlags(0x39, 4)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1B66")

    TalkEnd(0xFF)
    Return()

    # Function_7_1841 end

    def Function_8_1B6B(): pass

    label("Function_8_1B6B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D09")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 5)), scpexpr(EXPR_END)), "loc_1CEA")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE5")
    ClearScenarioFlags(0x3B, 5)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1CE2")
    ClearScenarioFlags(0x39, 5)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1C0D)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_93C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CDD")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CC4")
    Call(1, 5)
    Jump("loc_1CDD")

    label("loc_1CC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CDA")
    Call(1, 4)
    Jump("loc_1CDD")

    label("loc_1CDA")

    Call(1, 3)

    label("loc_1CDD")

    Jump("loc_1CE5")

    label("loc_1CE2")

    Call(1, 1)

    label("loc_1CE5")

    Jump("loc_1D00")

    label("loc_1CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1D00")
    ClearScenarioFlags(0x39, 5)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1D00")

    TalkEnd(0xFF)
    Return()

    label("loc_1D09")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 5)), scpexpr(EXPR_END)), "loc_1E7A")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E75")
    ClearScenarioFlags(0x3B, 5)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1E72")
    ClearScenarioFlags(0x39, 5)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1D9D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1D9D)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_980", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6D")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E54")
    Call(1, 5)
    Jump("loc_1E6D")

    label("loc_1E54")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E6A")
    Call(1, 4)
    Jump("loc_1E6D")

    label("loc_1E6A")

    Call(1, 3)

    label("loc_1E6D")

    Jump("loc_1E75")

    label("loc_1E72")

    Call(1, 1)

    label("loc_1E75")

    Jump("loc_1E90")

    label("loc_1E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1E90")
    ClearScenarioFlags(0x39, 5)
    OP_65(0x3, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1E90")

    TalkEnd(0xFF)
    Return()

    # Function_8_1B6B end

    def Function_9_1E95(): pass

    label("Function_9_1E95")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SoundLoad(451)
    SoundLoad(468)
    ClearChrFlags(0xD, 0x80)
    OP_78(0x2, 0xD)
    OP_49()
    SetChrPos(0xD, -125220, 26000, -79440, 90)
    OP_D5(0xD, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x3, 0xE)
    OP_49()
    SetChrPos(0xE, 10000, -3750, 10000, 270)
    OP_D5(0xE, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    OP_70(0x3, 0x0)
    BeginChrThread(0xE, 3, 0, 14)
    BeginChrThread(0xF, 1, 0, 15)
    FadeToBright(1000, 0)
    OP_68(-38790, 5750, -22440, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(143620, 0)
    OP_68(-33700, 5750, -28610, 9000)
    Sleep(1500)
    Sound(457, 0, 100, 0)
    Sound(468, 2, 60, 0)
    BeginChrThread(0xD, 3, 0, 10)
    OP_6F(0x79)
    OP_0D()
    Sound(458, 0, 100, 0)
    Sleep(500)
    Fade(1000)
    EndChrThread(0xD, 0x3)
    BeginChrThread(0xD, 3, 0, 11)
    OP_68(-38960, 22850, -72660, 0)
    MoveCamera(40, 14, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(32850, 0)
    OP_68(-38960, 27050, -72660, 8000)
    Sleep(7500)
    OP_0D()
    Fade(1000)
    EndChrThread(0xD, 0x3)
    BeginChrThread(0xD, 3, 0, 12)
    OP_68(-23640, 22550, -19540, 0)
    MoveCamera(44, 32, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(76720, 0)
    OP_68(18990, 22550, 23670, 13000)
    Sleep(11000)
    OP_0D()
    Fade(1000)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xF, 0x1)
    BeginChrThread(0xD, 3, 0, 13)
    BeginChrThread(0xF, 1, 0, 16)
    Sound(458, 0, 100, 0)
    OP_68(7330, 11850, 67750, 0)
    MoveCamera(83, 6, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12000, 0)
    OP_68(7330, 7450, 67750, 8500)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xD, 0x3)
    SetChrFlags(0xD, 0x80)
    EndChrThread(0xE, 0x3)
    SetChrFlags(0xE, 0x80)
    EndChrThread(0xF, 0x1)
    SetScenarioFlags(0x22, 1)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1E95 end

    def Function_10_20FE(): pass

    label("Function_10_20FE")

    SetChrPos(0xFE, -125220, 26000, -79440, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -110680, 26000, -82190)
    OP_9F(0x1, -94330, 25230, -81680)
    OP_9F(0x1, -78460, 24000, -86620)
    OP_9F(0x1, -57100, 24000, -86370)
    OP_9F(0x1, -39440, 24000, -77350)
    OP_9F(0x1, -22540, 20070, -56370)
    OP_9F(0x2, 0xFE, 10500, 0x6)
    Return()

    # Function_10_20FE end

    def Function_11_2171(): pass

    label("Function_11_2171")

    SetChrPos(0xFE, -56780, 24000, -88590, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -37290, 24000, -76670)
    OP_9F(0x1, -22050, 19860, -55310)
    OP_9F(0x1, -2630, 18400, -46870)
    OP_9F(0x1, 10840, 15340, -19370)
    OP_9F(0x1, 3980, 13730, 3190)
    OP_9F(0x1, 24440, 11750, 28620)
    OP_9F(0x2, 0xFE, 10500, 0x6)
    Return()

    # Function_11_2171 end

    def Function_12_21E4(): pass

    label("Function_12_21E4")

    SetChrPos(0xFE, 7090, 17120, -35580, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 10530, 14920, -15510)
    OP_9F(0x1, 5300, 13810, 2850)
    OP_9F(0x1, 16890, 11750, 24750)
    OP_9F(0x1, 35570, 10880, 34450)
    OP_9F(0x1, 55740, 8790, 37320)
    OP_9F(0x1, 77460, 6000, 46930)
    OP_9F(0x1, 83090, 6000, 56300)
    OP_9F(0x2, 0xFE, 10500, 0x6)
    Return()

    # Function_12_21E4 end

    def Function_13_2265(): pass

    label("Function_13_2265")

    SetChrPos(0xFE, 76500, 6000, 70060, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 64660, 5080, 74450)
    OP_9F(0x1, 47210, 5000, 68760)
    OP_9F(0x1, 27370, 5000, 65830)
    OP_9F(0x1, 9960, 4019, 69510)
    OP_9F(0x1, -410, 430, 85040)
    OP_9F(0x2, 0xFE, 10500, 0x6)
    Return()

    # Function_13_2265 end

    def Function_14_22CA(): pass

    label("Function_14_22CA")

    Sleep(10500)
    Sound(451, 2, 70, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x30D40, 0x2EE0, 0x1)
    Return()

    # Function_14_22CA end

    def Function_15_22E3(): pass

    label("Function_15_22E3")

    Sleep(9000)
    Sound(451, 2, 0, 0)
    OP_25(0x1C3, 0x0)
    Sleep(500)
    OP_25(0x1C3, 0xA)
    Sleep(500)
    OP_25(0x1C3, 0xA)
    Sleep(500)
    OP_25(0x1C3, 0x14)
    Sleep(500)
    OP_25(0x1C3, 0x1E)
    Sleep(500)
    OP_25(0x1C3, 0x28)
    Sleep(8500)
    StopSound(451, 3000, 40)
    Return()

    # Function_15_22E3 end

    def Function_16_231D(): pass

    label("Function_16_231D")

    Sleep(5000)
    Sound(494, 0, 100, 0)
    StopSound(468, 1000, 60)
    Return()

    # Function_16_231D end

    def Function_17_232D(): pass

    label("Function_17_232D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51619.itc", 0x1E)
    SetChrPos(0x101, -119850, 26000, -82000, 90)
    OP_68(-109200, 27500, -82550, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 3000)

    def lambda_2395():
        OP_95(0xFE, -109200, 26000, -82550, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2395)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_0D()

    #C0016
    ChrTalk(
        0x101,
        "#00006F#5P呼、呼……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)

    #C0017
    ChrTalk(
        0x101,
        "#00003F#11P……女神保佑。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    Fade(1000)
    OP_68(-30150, 26650, -66900, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(39800, 0)
    OP_68(-30150, 22950, -66900, 10000)
    OP_0D()
    Sleep(2000)
    SetMessageWindowPos(10, 20, -1, -1)

    #A0018
    AnonymousTalk(
        0x101,
        (
            "#00013F（『灵智之草』……）\x02\x03",

            "（在我被拘留的这段时间，\x01",
            "  都已经蔓延到这里了啊……）\x02\x03",

            "#00008F（……莫非与琪雅\x01",
            "  有关吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(1000)
    OP_68(-109200, 27000, -82550, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 2000)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    OP_0D()
    Sleep(100)

    #C0019
    ChrTalk(
        0x101,
        (
            "#00003F#5P（……总之，\x01",
            "  首先要逃离此地。）\x02\x03",

            "（先逃到西克洛斯贝尔街道再说吧。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetCameraDistance(13900, 500)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x101, 0x3)
    Sleep(100)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0020
    ChrTalk(
        0x101,
        (
            "#5P#00010F（……思考所有可行路线，\x01",
            "  无论如何也要顺利逃脱……！）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(13750, 1000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "加尔西亚\x01",
            "脱离了队伍。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_49()
    OP_D7(0x1E)
    OP_37()
    OP_32(0xFF, 0xFE, 0x0)
    SetChrPos(0x0, -100900, 26000, -82000, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x184, 4)
    OP_29(0xAE, 0x1, 0x1)
    OP_C9(0x1, 0x8000)
    OP_1B(0x1, 0x0, 0x12)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayBGM("ed7251", 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_232D end

    def Function_18_26EC(): pass

    label("Function_18_26EC")

    EventBegin(0x1)
    OP_E2(0x3)

    #C0022
    ChrTalk(
        0x101,
        (
            "#00003F（加尔西亚，我绝对不会\x01",
            "  白白浪费你的援助……）\x02\x03",

            "#00001F走吧！\x01",
            "没时间磨磨蹭蹭了！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -116750, 26000, -81820, 94)
    OP_E2(0x2)
    EventEnd(0x4)
    Return()

    # Function_18_26EC end

    SaveToFile()

Try(main)
