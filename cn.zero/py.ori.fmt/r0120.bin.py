from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r0120.bin",                # FileName
        "r0120",                    # MapName
        "r0120",                    # Location
        0x0061,                     # MapIndex
        "ed7201",
        0x00000000,                 # Flags
        ("r0120", "r0000_1", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 97, 0, 3, 0, 4],
    )

    BuildStringList((
        "r0120",                  # 0
        "车",                     # 1
        "阿尔弗雷德",             # 2
        "头罩掠食虫",             # 3
        "MapThread",              # 4
        "br0100",                 # 5
        "br0100",                 # 6
        "br0100",                 # 7
        "br0100",                 # 8
        "br0100",                 # 9
        "br0100",                 # 10
        "br0100",                 # 11
        "克洛斯贝尔市·唐古拉姆门方向",# 12
        "阿尔摩利卡村方向",       # 13
        "古战场方向",             # 14
    ))

    ATBonus("ATBonus_584", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_249D", 6,   3,   0,   0,   4,   3,   1)
    Sepith("Sepith_24AD", 0,   2,   0,   7,   3,   5,   0)
    Sepith("Sepith_24BD", 2,   0,   7,   1,   4,   2,   1)
    Sepith("Sepith_24A5", 3,   0,   7,   0,   2,   1,   4)
    Sepith("Sepith_24B5", 1,   7,   0,   3,   0,   1,   5)
    Sepith("Sepith_24C5", 34,  15,  25,  15,  0,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_5E4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5EC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5FC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_600", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_644", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_648", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_64C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_650", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_654", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_658", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_65C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_660", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_5C4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5DC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E0", 2, 13, 180)

    # monster count: 17

    BattleInfo(
        "BattleInfo_79C", 0x0000, 10, 6, 45, 6, 1, 30, 0, "br0100", "Sepith_249D", 30, 45, 20, 5,
        (
            ("ms62200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms62200.dat", "ms62200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms62200.dat", "ms69800.dat", "ms62200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms62200.dat", "ms61800.dat", "ms62200.dat", "ms61800.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
        )
    )

    BattleInfo(
        "BattleInfo_664", 0x0000, 10, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_24AD", 30, 45, 25, 0,
        (
            ("ms63900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms63900.dat", "ms63900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms63900.dat", "ms62600.dat", "ms63900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_864", 0x0000, 10, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_24BD", 30, 45, 25, 0,
        (
            ("ms69800.dat", "ms69800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms69800.dat", "ms63900.dat", "ms69800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms69800.dat", "ms69900.dat", "ms62600.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_700", 0x0000, 10, 6, 45, 6, 1, 50, 0, "br0100", "Sepith_24A5", 30, 45, 25, 0,
        (
            ("ms62600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms62600.dat", "ms62600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms62600.dat", "ms66200.dat", "ms62600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_900", 0x0000, 10, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_24B5", 30, 45, 25, 5,
        (
            ("ms64500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms64500.dat", "ms64500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms64500.dat", "ms62600.dat", "ms64500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms64500.dat", "ms62600.dat", "ms64500.dat", "ms61800.dat", 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
        )
    )

    BattleInfo(
        "BattleInfo_A0C", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_24C5", 40, 35, 25, 0,
        (
            ("ms76201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            ("ms76201.dat", "ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5E4", "MonsterBattlePostion_644", "ed7400", "ed7403", "ATBonus_584"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_9C8", 0x0000, 10, 6, 45, 0, 1, 0, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62600.dat", "ms62600.dat", "ms62600.dat", "ms62600.dat", "ms62600.dat", "ms62600.dat", 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_644", "ed7401", "ed7403", "ATBonus_584"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch21000.itc",                   # 00
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
        "monster/ch64550.itc",               # 18
        "monster/ch64551.itc",               # 19
        "monster/ch76250.itc",               # 1A
        "monster/ch76251.itc",               # 1B
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(11039,   3009,    77480,   270,  385,  0x0, 0,   0,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-25709,  2000,    168059,  0,    484,  0x0, 0,   18,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-31520,  37060,   3000,    0x1010000,    "BattleInfo_79C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-50480,  40250,   1000,    0x1010000,    "BattleInfo_664", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-6300,   63280,   3000,    0x1010000,    "BattleInfo_864", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-10530,  85710,   3000,    0x1010000,    "BattleInfo_700", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-51040,  94660,   2000,    0x1010000,    "BattleInfo_900", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-56360,  74870,   2000,    0x1010000,    "BattleInfo_79C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-40900,  149790,  2009,    0x1010000,    "BattleInfo_664", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-17280,  116460,  2000,    0x1010000,    "BattleInfo_664", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-21030,  137120,  1000,    0x1010000,    "BattleInfo_864", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-60400,  152360,  2000,    0x1010000,    "BattleInfo_664", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-77600,  151590,  1500,    0x1010000,    "BattleInfo_900", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(40390,   71780,   5000,    0x1010000,    "BattleInfo_79C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(77400,   80820,   9000,    0x1010000,    "BattleInfo_664", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(72370,   108020,  9000,    0x1010000,    "BattleInfo_864", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-23200,  48960,   3000,    0x1010000,    "BattleInfo_A0C", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-46680,  101000,  2000,    0x1010000,    "BattleInfo_A0C", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-72140,  162220,  2710,    0x1010000,    "BattleInfo_A0C", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 15,  16.0,                  76.0,                  2.5,                   64.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -8.0,                  -9.5,                  -0.5,                  1.0])

    DeclActor(-49820,  1000,    48270,   1200,    -49820,  2000,    48270,   0x007C, 0,  5,  0x0000)
    DeclActor(-55330,  2000,    72560,   1200,    -55330,  3000,    72560,   0x007C, 0,  6,  0x0000)
    DeclActor(-25710,  1000,    168060,  1200,    -25710,  2000,    168060,  0x007C, 0,  7,  0x0000)
    DeclActor(86490,   9000,    96960,   1200,    86490,   10000,   96960,   0x007C, 0,  8,  0x0000)
    DeclActor(39750,   5000,    90020,   1200,    39750,   6000,    90020,   0x007C, 0,  9,  0x0000)
    DeclActor(-79110,  1500,    147760,  1200,    -79110,  2500,    147760,  0x007C, 0,  10, 0x0000)
    DeclActor(7820,    3000,    74900,   1200,    7820,    4500,    74900,   0x007C, 0,  16, 0x0000)
    DeclActor(-41000,  1750,    29960,   1200,    -41000,  1750,    29960,   0x007C, 0,  11, 0x0000)
    DeclActor(-61320,  2040,    165270,  1500,    -61320,  3740,    165270,  0x007C, 0,  17, 0x0000)

    PlaceName(-2.0, 0.0, -22.0, 0x0000, 0x0000, "克洛斯贝尔市·唐古拉姆门方向")
    PlaceName(-95.0, 0.0, 210.0, 0x0000, 0x0000, "阿尔摩利卡村方向")
    PlaceName(128.0, 0.0, 122.0, 0x0000, 0x0000, "古战场方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(1299, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 11

    ScpFunction((
        "Function_0_B80",          # 00, 0
        "Function_1_C38",          # 01, 1
        "Function_2_C54",          # 02, 2
        "Function_3_CC5",          # 03, 3
        "Function_4_D27",          # 04, 4
        "Function_5_1761",         # 05, 5
        "Function_6_1897",         # 06, 6
        "Function_7_19EC",         # 07, 7
        "Function_8_1BE6",         # 08, 8
        "Function_9_1D1C",         # 09, 9
        "Function_10_1E52",        # 0A, 10
        "Function_11_1F88",        # 0B, 11
        "Function_12_1F9C",        # 0C, 12
        "Function_13_1FBA",        # 0D, 13
        "Function_14_211C",        # 0E, 14
        "Function_15_22E5",        # 0F, 15
        "Function_16_2377",        # 10, 16
        "Function_17_23EC",        # 11, 17
    ))


    def Function_0_B80(): pass

    label("Function_0_B80")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_BC0"),
        (1, "loc_BCC"),
        (2, "loc_BD8"),
        (3, "loc_BE4"),
        (4, "loc_BF0"),
        (5, "loc_BFC"),
        (6, "loc_C08"),
        (SWITCH_DEFAULT, "loc_C14"),
    )


    label("loc_BC0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_C20")

    label("loc_BCC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_C20")

    label("loc_BD8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_C20")

    label("loc_BE4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_C20")

    label("loc_BF0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_C20")

    label("loc_BFC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_C20")

    label("loc_C08")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C20")

    label("loc_C14")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C20")

    label("loc_C20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C37")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C20")

    label("loc_C37")

    Return()

    # Function_0_B80 end

    def Function_1_C38(): pass

    label("Function_1_C38")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C53")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_C38")

    label("loc_C53")

    Return()

    # Function_1_C38 end

    def Function_2_C54(): pass

    label("Function_2_C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 1)), scpexpr(EXPR_END)), "loc_CC4")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CC4")
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sleep(2000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
    StopEffect(0x0, 0x2)
    ClearScenarioFlags(0xBA, 1)
    Jump("loc_CC4")

    label("loc_CC4")

    Return()

    # Function_2_C54 end

    def Function_3_CC5(): pass

    label("Function_3_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_CD7")
    ClearScenarioFlags(0x5C, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 14)

    label("loc_CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D23")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CF6")
    Jump("loc_D23")

    label("loc_CF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_D0D")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_D23")

    label("loc_D0D")

    SetChrPos(0x9, 10370, 3000, 75310, 270)
    ClearChrFlags(0x9, 0x80)

    label("loc_D23")

    Call(0, 12)
    Return()

    # Function_3_CC5 end

    def Function_4_D27(): pass

    label("Function_4_D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D3E")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 7800, 3010, 75130, 20000, 2000, 90000)
    SetMapObjFlags(0x7, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_DF3")
    SetMapObjFrame(0xFF, "bridge_before", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bridge_after", 0x1, 0x1)
    SetBarrier(0x2, 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB8")
    ClearMapObjFlags(0x7, 0x4)
    SetBarrier(0x3, 0x0, 0x1)
    OP_66(0x6, 0x1)

    label("loc_DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DEE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_DD7")
    Jump("loc_DEE")

    label("loc_DD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_DE9")
    Jump("loc_DEE")

    label("loc_DE9")

    ModifyEventFlags(1, 0, 0x80)

    label("loc_DEE")

    Jump("loc_E20")

    label("loc_DF3")

    SetMapObjFrame(0xFF, "bridge_before", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bridge_after", 0x0, 0x1)
    SetBarrier(0x3, 0x0, 0x1)

    label("loc_E20")

    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1345")
    OP_70(0x0, 0x0)
    Jump("loc_1349")

    label("loc_1345")

    OP_70(0x0, 0x1E)

    label("loc_1349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135C")
    OP_70(0x1, 0x0)
    Jump("loc_1360")

    label("loc_135C")

    OP_70(0x1, 0x1E)

    label("loc_1360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1373")
    OP_70(0x2, 0x0)
    Jump("loc_1377")

    label("loc_1373")

    OP_70(0x2, 0x1E)

    label("loc_1377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138A")
    OP_70(0x3, 0x0)
    Jump("loc_138E")

    label("loc_138A")

    OP_70(0x3, 0x1E)

    label("loc_138E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A1")
    OP_70(0x4, 0x0)
    Jump("loc_13A5")

    label("loc_13A1")

    OP_70(0x4, 0x1E)

    label("loc_13A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B8")
    OP_70(0x5, 0x0)
    Jump("loc_13BC")

    label("loc_13B8")

    OP_70(0x5, 0x1E)

    label("loc_13BC")

    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 4)), scpexpr(EXPR_END)), "loc_1419")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -41000, 1750, 29960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x7, 0x1)

    label("loc_1419")

    LoadEffect(0x0, "map/mpr3000.eff")
    BeginChrThread(0xB, 0, 0, 2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16AF")
    ClearScenarioFlags(0x7A, 0)
    ClearScenarioFlags(0x7A, 1)
    ClearScenarioFlags(0x7A, 2)
    ClearScenarioFlags(0x7A, 3)
    ClearScenarioFlags(0x7A, 4)
    ClearScenarioFlags(0x7A, 5)
    ClearScenarioFlags(0x7A, 6)
    ClearScenarioFlags(0x7A, 7)
    ClearScenarioFlags(0x7B, 0)
    ClearScenarioFlags(0x7B, 1)
    ClearScenarioFlags(0x7B, 2)
    ClearScenarioFlags(0x7B, 3)
    ClearScenarioFlags(0x7B, 4)
    ClearScenarioFlags(0x7B, 5)
    ClearScenarioFlags(0x7B, 6)
    ClearScenarioFlags(0x7B, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148E")
    SetScenarioFlags(0x7A, 0)

    label("loc_148E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A4")
    SetScenarioFlags(0x7A, 1)

    label("loc_14A4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BA")
    SetScenarioFlags(0x7A, 2)

    label("loc_14BA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D0")
    SetScenarioFlags(0x7A, 3)

    label("loc_14D0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E6")
    SetScenarioFlags(0x7A, 4)

    label("loc_14E6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FC")
    SetScenarioFlags(0x7A, 5)

    label("loc_14FC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1512")
    SetScenarioFlags(0x7A, 6)

    label("loc_1512")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1528")
    SetScenarioFlags(0x7A, 7)

    label("loc_1528")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_153E")
    SetScenarioFlags(0x7B, 0)

    label("loc_153E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1554")
    SetScenarioFlags(0x7B, 1)

    label("loc_1554")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156A")
    SetScenarioFlags(0x7B, 2)

    label("loc_156A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1580")
    SetScenarioFlags(0x7B, 3)

    label("loc_1580")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1596")
    SetScenarioFlags(0x7B, 4)

    label("loc_1596")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AC")
    SetScenarioFlags(0x7B, 5)

    label("loc_15AC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C2")
    SetScenarioFlags(0x7B, 6)

    label("loc_15C2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D8")
    SetScenarioFlags(0x7B, 7)

    label("loc_15D8")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1613")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_16AF")

    label("loc_1613")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162A")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_16AF")

    label("loc_162A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1641")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_16AF")

    label("loc_1641")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1658")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_16AF")

    label("loc_1658")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_166F")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_16AF")

    label("loc_166F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1686")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_16AF")

    label("loc_1686")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169D")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_16AF")

    label("loc_169D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16AF")
    SetScenarioFlags(0x7C, 7)

    label("loc_16AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16C0")
    OP_24(0x7B)
    Jump("loc_1751")

    label("loc_16C0")

    SoundDistance(0x7B, 0xFFFFB06E, 0xBC2, 0xFFFFD008, 0x3A98, 0xC350, 0x64, 0x0)
    OP_E1(0xD8EA, 0x5DC, 0xFFFFC8F6)
    OP_E1(0x45D8, 0x5DC, 0x140DC)
    OP_E1(0xFFFFAAB0, 0x7D0, 0x190D2)
    OP_E1(0xFFFF633E, 0x5DC, 0x1C840)
    OP_E1(0xFFFF650A, 0x5DC, 0x20364)
    OP_E1(0xFFFF650A, 0x5DC, 0x20364)
    OP_E1(0xFFFF8BFC, 0x7D0, 0x23870)
    OP_E1(0xFFFF84F4, 0x7D0, 0x2698A)
    OP_E1(0xFFFE762C, 0x7D0, 0x38400)

    label("loc_1751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1760")
    OP_16(0x3, 0x2, 0x1, 0x0)

    label("loc_1760")

    Return()

    # Function_4_D27 end

    def Function_5_1761(): pass

    label("Function_5_1761")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184E")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('复苏药', 1)"), scpexpr(EXPR_END)), "loc_17E0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x102, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1849")

    label("loc_17E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '复苏药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1849")

    Jump("loc_188B")

    label("loc_184E")

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

    label("loc_188B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1761 end

    def Function_6_1897(): pass

    label("Function_6_1897")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BD")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 20)
    AddSepith(0x1, 20)
    AddSepith(0x2, 20)
    AddSepith(0x3, 20)
    AddSepith(0x4, 20)
    AddSepith(0x5, 20)
    AddSepith(0x6, 20)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×２０\x01\x07\x02",

            "#57I水之耀晶片×２０\x01\x07\x02",

            "#58I火之耀晶片×２０\x01\x07\x02",

            "#59I风之耀晶片×２０\x01\x07\x02",

            "#60I时之耀晶片×２０\x01\x07\x02",

            "#61I空之耀晶片×２０\x01\x07\x02",

            "#62I幻之耀晶片×２０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x103, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_19DA")

    label("loc_19BD")


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

    label("loc_19DA")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1897 end

    def Function_7_19EC(): pass

    label("Function_7_19EC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA8")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE5")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1A45():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A45)

    def lambda_1A5F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1A5F)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    #A0006
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
    Battle("BattleInfo_9C8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1AC6"),
        (2, "loc_1AD5"),
        (1, "loc_1AE2"),
        (SWITCH_DEFAULT, "loc_1AE5"),
    )


    label("loc_1AC6")

    SetScenarioFlags(0x74, 0)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_1AE5")

    label("loc_1AD5")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1AE2")

    OP_B7(0x0)
    Return()

    label("loc_1AE5")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('银耀珠', 1)"), scpexpr(EXPR_END)), "loc_1B3C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '银耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x103, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1BA3")

    label("loc_1B3C")

    FadeToDark(300, 0, 100)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '银耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '银耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1BA3")

    Jump("loc_1BDA")

    label("loc_1BA8")

    FadeToDark(300, 0, 100)

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

    label("loc_1BDA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_19EC end

    def Function_8_1BE6(): pass

    label("Function_8_1BE6")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD3")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('痊愈之药', 1)"), scpexpr(EXPR_END)), "loc_1C65")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x103, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1CCE")

    label("loc_1C65")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1CCE")

    Jump("loc_1D10")

    label("loc_1CD3")

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

    label("loc_1D10")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1BE6 end

    def Function_9_1D1C(): pass

    label("Function_9_1D1C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E09")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('土人偶', 1)"), scpexpr(EXPR_END)), "loc_1D9B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '土人偶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x103, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1E04")

    label("loc_1D9B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '土人偶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '土人偶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E04")

    Jump("loc_1E46")

    label("loc_1E09")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
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

    label("loc_1E46")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1D1C end

    def Function_10_1E52(): pass

    label("Function_10_1E52")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3F")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅰ', 1)"), scpexpr(EXPR_END)), "loc_1ED1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0016
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
    SetScenarioFlags(0x103, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1F3A")

    label("loc_1ED1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0017
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
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1F3A")

    Jump("loc_1F7C")

    label("loc_1F3F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0018
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

    label("loc_1F7C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1E52 end

    def Function_11_1F88(): pass

    label("Function_11_1F88")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 4)
    OP_65(0x7, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_11_1F88 end

    def Function_12_1F9C(): pass

    label("Function_12_1F9C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FB9")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)

    label("loc_1FB9")

    Return()

    # Function_12_1F9C end

    def Function_13_1FBA(): pass

    label("Function_13_1FBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1FCE")
    Jump("loc_2118")

    label("loc_1FCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_20E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_202D")

    #C0019
    ChrTalk(
        0x9,
        (
            "请一定要帮助游击士\x01",
            "找到失踪的\x01",
            "那对情侣游客。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        "拜托你们了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20E4")

    label("loc_202D")


    #C0021
    ChrTalk(
        0x9,
        (
            "你们是……\x01",
            "那个特别任务支援科的人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            "刚才有游击士来了，\x01",
            "他已经进去搜索游客了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "关于你们的事我也听说了。\x01",
            "你们是要去协助游击士的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        (
            "请一定要找到\x01",
            "那对情侣游客。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20E4")

    Jump("loc_2118")

    label("loc_20E9")


    #C0025
    ChrTalk(
        0x9,
        (
            "……唔，果然是走到\x01",
            "这条路的深处去了吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2118")

    TalkEnd(0xFE)
    Return()

    # Function_13_1FBA end

    def Function_14_211C(): pass

    label("Function_14_211C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-46600, 3000, 158700, 0)
    MoveCamera(47, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(36500, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x6, 0x4)
    OP_78(0x6, 0x8)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x8, -66000, 2000, 159000, 90)
    OP_D3(0x8, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x79, 0xB4, 0x0, 0x20)
    Sound(457, 0, 100, 0)
    Sleep(1000)
    OP_6B(0x8)
    Sleep(200)

    def lambda_21C8():
        OP_95(0xFE, -49200, 2000, 159000, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_21C8)
    PlayBGM("ed7105", 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_21F3():
        OP_9E(0xFE, 0xFFFF3FD0, 0x24608, 0x1FBD0, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_21F3)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x8, 1)
    Fade(1000)
    OP_6B(0xFF)
    OP_68(-45980, 3000, 133440, 0)
    MoveCamera(39, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(36500, 0)
    OP_68(-45980, 0, 133440, 4000)
    Sound(458, 0, 100, 0)

    def lambda_2263():
        OP_95(0xFE, -48000, 2000, 135200, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2263)
    Sleep(1260)

    def lambda_2280():
        OP_9E(0xFE, 0xFFFF6B90, 0x1E910, 0xFFFF5038, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2280)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x8, 1)

    def lambda_22A3():
        OP_95(0xFE, -52000, 2000, 109000, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22A3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x8, 0x1)
    Sleep(3000)
    ClearScenarioFlags(0x0, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("e0310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_211C end

    def Function_15_22E5(): pass

    label("Function_15_22E5")

    EventBegin(0x1)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0x0, 500)

    #C0026
    ChrTalk(
        0x9,
        "你们几个，等一下！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "前方的古战场\x01",
            "有魔兽徘徊，\x01",
            "非常危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "我不能让无关人员\x01",
            "进入里面。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    OP_93(0x9, 0x10E, 0x0)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x0, 6820, 3010, 75770, 270)
    EventEnd(0x4)
    Return()

    # Function_15_22E5 end

    def Function_16_2377(): pass

    label("Function_16_2377")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "前方是古战场。\x01",
            "内部十分危险，\x01",
            "严禁入内。\x01",
            "         ～管理局～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_2377 end

    def Function_17_23EC(): pass

    label("Function_17_23EC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0030
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西北·阿尔摩利卡村\x01",
            "　南·克洛斯贝尔市　２７４赛尔矩\x01",
            "　　　　唐古拉姆门　２３２赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_23EC end

    SaveToFile()

Try(main)
